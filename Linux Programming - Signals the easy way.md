Linux Programming - Signals the easy way

# Signals

Signals are the the necessary evil that almost nobody get right. So this is all about dealing with them in a manageable way that will also make them usable again inside a normal program. Lets have a look at some really common mistakes when dealing with signals in the old way when using signal / sigaction.

# Common Mistakes

## Restrictions

Signals handlers have great restrictions on what can be performed. This is because when a signal is delivered to the process the signal will interrupt the process and jump directly into a signal handler which is then executed. This can only be blocked by functions that are signal aware and block the signals during certain critical sections of their code execution. Since this is a relatively expensive operation to do the majority of libc functions do not perform it. This make the majority of libc functions impossible to use in a signal handler. Some examples of these would be free, malloc, syslog and just about anything else that involved either taking a threaded lock or reads / writes any global data structures.

## sigprocmask

I have seen many people use sigprocmask with SIG_UNBLOCK in specific ways that can cause unpredictable results. Particularly when used inside a library. If you consider the following code in a library function it becomes a serious issue which is very difficult to work around. Without changing the library code and getting involved in pushing patches etc..

	[[BLOCK_OPEN]][[BLOCK_OPEN]][[BLOCK_OPEN]]void func() {
	  sigset_t block;
	  sigemptyset(&block);
	  sigaddset(&block, SIGTERM);
	  sigsetmask(SIG_BLOCK, &block, NULL);
	  //DoSomething critical
	  sigsetmask(SIG_UNBLOCK, &block, NULL);
	}
	[[BLOCK_CLOSE]][[BLOCK_CLOSE]]

	[[BLOCK_CLOSE]]

I am sure the above seems to make sense. It would also be highly likely to pass a code review. Since as a function it will work. It will pass all unit tests. Until of course you call it from another function that also requires that you block the same signal. In short signal blocks should be used as a stack and you push / pop various signals to be blocked when required.

	[[BLOCK_OPEN]][[BLOCK_OPEN]][[BLOCK_OPEN]]void myfunc() {
	  sigset_t block;
	  sigset_t old;
	  sigemptyset(&block);
	  sigaddset(&block, SIGTERM);
	  sigsetmask(SIG_BLOCK, &block, &old);
	  //Do something
	  func();
	  //Signal already unblocked by func....
	  //Do something else - corruption occurs.
	  sigsetmask(SIG_SETMASK, &old, NULL);
	}
	[[BLOCK_CLOSE]][[BLOCK_CLOSE]]

	[[BLOCK_CLOSE]]

## signal (the system call)

The older system call signal that was deprecated long ago but is still hanging around for legacy reasons. Its just so badly broken because it does not permit the correct options to be supplied when installing a signal handler. Just like sigprocmask above if installing a signal handler temporary during a certain operation they need ot be used as a stack when removing the temporary signal handler you need to restore the old signal handler. Using signal makes this an impossible operation to perform.

## Trying to catch impossible signals

There are developers out there that try to catch signals like SIGKILL, SIGABRT, SIGSTOP. This is a pointless attempt the signal will NEVER be delivered to the program. With something like SIGKILL the kernel will simply act on it as soon as it can and remove the process from userspace. Not to mention that catching and ignoring SIGSEGV, SIGFPE and SIGBUS will put the program into an unspecified state.

## Threads

There is a really long list of don't do this here for all sorts of reasons. I am only going to include some of the more obvious issues.

- sigprocmask is documented as not thread safe. Use pthread_sigmask instead.
- Though pthread_sigmask is marked as thread safe that specifically means its not going to crash or do something undefined when you use it. However it may also not perform as you except. When you block a signal on a thread it will only be blocked on that specific thread. When a signal is delivered to a process is can simply be executed on another thread. This makes signals blocking across threads somewhat of a painful operation. Typically the solution is to block everything you want to catch on application startup then only enable specific signals on specific threads. Though these blocks can be effective when sending signals using pthread_signal to specific threads.
- SIGALARM and alarm basically becomes useless in many situations as it can only be used in a single thread because of the reasons of thread safty above.
- Some signals will be specific threads anyway. For example SIGSEGV on Linux but this is OS specific and also depends if the signal is blocked by that thread at the time.
- The worst offender I have seen was somebody trying to take a pthread lock inside the signal handler. Then trying to fix the "deadlock" by making the lock recursive!! This was so that a pthread_cond_signal could be sent to get the application to exit.

## SA_RESTART

When installing a signal handler with sigaction and the options for SA_RESTART I had an argument with a tech lead. He would believe that it would restart all system calls after a signal was delivered. No that is not how it works. Any system call that is considered to be slow or blocking can still return an EINTR. Even more so any system call working with data on a file descriptor can also return a short read / write. This often leads to data corruption really fast. I don't ever recommend working in a team of software developers who don't realise that this happens either. Though the solution below will sort this problem out a fair amount.

# Making signals work

So with the above how do you get signals to actually work at all, still have a stable application and at the same time actually make them useful. This solution will work for most of the simple signal handling cases which I would consider to only be the ones which your required to handle. I mean such signals as SIGTERM, SIGUSR1, SIGUSR2, SIGHUP, SIGCHLD, SIGPIPE and possibly SIGALARM. These are typically the signals that would be delivered to the process for external control. SIGTERM for a request to terminate, SIGHUP to re-open log files or re-read a config file.

There is really two options both of which avoiding using signal and sigaction. That is to use sigwaitinfo or signalfd. These work simply by blocking all the signals that you want to catch and handle in the application. The main signal blocking should be done in the main thread prior to any other threads being created. This way all threads will inherit the same set of signal blocks.

The choice between which to use is really quite simple. I would use a signalfd if I was going to tie the signal handling into an event loop using select or poll. Or if you want a dedicated thread and want to save using a file descriptor use sigwaitinfo which has the added advance that no cleanup is required. Both functions work by reading the applications signal queue from the kernel inside the normal context of the application. Since signals will now be processed inside the normal application context that means there are no restrictions as to what can be performed in a signal handler. As you can see in the following example its possible to have the main thread sleep on a condition variable which is then woken up from the signal handler thread.

	[[BLOCK_OPEN]][[BLOCK_OPEN]][[BLOCK_OPEN]]#include <stdio.h>
	#include <stdlib.h>
	#include <pthread.h>
	#include <signal.h>
	#include <errno.h>

	struct exit_wait {
	    pthread_mutex_t lock;
	    pthread_cond_t wait;
	    volatile int running;
	};

	void *worker(void *arg) {
	    struct exit_wait *cond = (struct exit_wait *) arg;

	    if (pthread_mutex_lock(&cond->lock) != 0)
	        abort();

	    while(cond->running) {
	        if (pthread_cond_wait(&cond->wait, &cond->lock) != 0)
	            abort();
	    }

	    if (pthread_mutex_unlock(&cond->lock) != 0)
	        abort();

	    return NULL;
	}

	int main(int argc, char **argv) {
	    struct exit_wait *cond = malloc(sizeof(*cond));
	    pthread_t thd;
	    void *retval = NULL;
	    sigset_t sigs, oldsigs;

	    if (sigemptyset(&sigs) < 0)
	        abort();
	    if (sigaddset(&sigs, SIGTERM) < 0)
	        abort();

	    if (sigprocmask(SIG_BLOCK, &sigs, &oldsigs) < 0)
	        abort();

	    if (pthread_mutex_init(&cond->lock, NULL) != 0)
	        abort();
	    if (pthread_cond_init(&cond->wait, NULL) != 0)
	        abort();
	    cond->running = 1;

	    if (pthread_create(&thd, NULL, worker, cond) != 0)
	        abort();

	    while(cond->running) {
	        siginfo_t info;
	        if (sigwaitinfo(&sigs, &info) < 0)
	        {
	            switch(errno) {
	                case EINTR:
	                    continue;
	                    break;
	                default:
	                    abort();
	            }
	        }

	        switch(info.si_signo) {
	            case SIGTERM:
	                pthread_mutex_lock(&cond->lock);
	                cond->running = 0;
	                pthread_cond_broadcast(&cond->wait);
	                pthread_mutex_unlock(&cond->lock);
	                break;
	            default:
	                printf("Unknown signal %d\n", info.si_signo);
	                break;
	        }

	    }

	    pthread_join(thd, &retval);

	    if (pthread_cond_destroy(&cond->wait) != 0)
	        abort();

	    if (pthread_mutex_destroy(&cond->lock) != 0)
	        abort();

	    if (sigprocmask(SIG_SETMASK, &oldsigs, NULL) < 0)
	        abort();

	    free(cond);
	    return 0;
	}
	[[BLOCK_CLOSE]][[BLOCK_CLOSE]]

	[[BLOCK_CLOSE]]

Something I have found in the past that you can still block signals from a dedicated signal thread but instead of using sigprocmask you have the signal thread block by taking a lock instead.

With this approach I would also try to avoid to block the signals SIGTRAP and SIGINT in this way which are commonly used by debuggers and are required to be processes in the traditional way which can be somewhat limiting so what can be performed with these signals. However using an additional approach of adding these using a handler registered with sigaction will give you the option of forwarding a signal to the application as another signal. If a debugger is involved in the application then it should prevent this from occurring as it should have prevented the application from executing the signal handler. Here is an example of dealing with SIGINT in a predictable which was added with the code above this is so that the program can respond to a Ctrl-c on a terminal.

	[[BLOCK_OPEN]][[BLOCK_OPEN]][[BLOCK_OPEN]]void forward(int sig) {
	    kill(getpid(), SIGTERM);
	}

	void func() { //Really code added to main
	    struct sigaction act, oldact;

	    memset(&act, 0, sizeof(act));
	    act.sa_handler = forward;
	    sigemptyset(&act.sa_mask);
	    act.sa_flags = SA_RESTART;

	    if (sigaction(SIGINT, &act, &oldact) < 0)
	        abort();

	    //Main Loop

	    if (sigaction(SIGINT, &oldact, NULL) < 0)
	        abort();
	}
	[[BLOCK_CLOSE]][[BLOCK_CLOSE]]

	[[BLOCK_CLOSE]]

# Using signals for debugging

To some this might find this approach somewhat of a crazy idea. Mostly I tend to work in C++ and be involved in making some sort of service applications. I would typically also catch SIGUSR1 and SIGUSR2 for being able to perform certain operations. I would route these signals in such a way that by having a global static class that any other class which inherits a specific interface can register with the signal handler. This is extremely useful for being able to dump the major state from all over the application on demand or performance metric for functions to some sort of common logging.