4 Things You Should Know VSCode Can Do — Without Extensions

# 4 Things You Should Know VSCode Can Do — Without Extensions

[![0*gUEm8u6ZQnlrVFO8.jpg](../_resources/6d52066797729330f24a40c6ab737872.jpg)](https://blog.insiderattack.net/@dpjayasekara?source=post_page-----f3d7803733ae----------------------)

[Deepal Jayasekara](https://blog.insiderattack.net/@dpjayasekara?source=post_page-----f3d7803733ae----------------------)

[Dec 31, 2019](https://blog.insiderattack.net/4-things-you-should-know-vscode-can-do-without-extensions-f3d7803733ae?source=post_page-----f3d7803733ae----------------------) · 3 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='184'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='185' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/f3d7803733ae/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='188'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='189' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/f3d7803733ae/share/facebook?source=post_actions_header---------------------------)

In my opinion, VSCode is the best thing ever happened to the IDE world. It’s super lightweight, feature-rich and free hence without a doubt the best IDE I have ever used in my opinion. The other biggest plus of VSCode is the community of extension developers who made our lives a whole lot easy. But today, I’m going to describe four of the most important things VSCode can do without extensions, which some developers even not know.

Feel free to read more about these in the official VSCode documentation, but first, let me point you to where to look.

## Conditional Breakpoints

We use debug points all the time when debugging. But what if we can instruct the debug point only to hit once a given condition is met? These are called Conditional Breakpoints which are handy in especially when debugging inside loops, isolating specific scenarios and debugging edge-cases.

![1*Vim474kHAsEy-aGuoj9-4Q.gif](../_resources/5d9db0b2eca7d4163f8db2f0ed04adfc.jpg)
![1*Vim474kHAsEy-aGuoj9-4Q.gif](../_resources/294d5908b226fe370f479b579b52338f.gif)
Debugging inside a loop with conditional breakpoints

## Log points

It’s quite common to add `console.log` statements in the code to quickly check whether the application is behaving the way you expected. But the pain of this is that you have to make sure that you have removed every `console.log` you added for debugging before you commit.

Log point is a variant of a debug point which logs a provided message when the debug point is hit. You have access to all of the variables in the scope where log point is added, making Log points extremely valuable and cleaner alternative to good old statements. The hassle of cleaning up adding `console.log`s and removing them is no more.

![1*G7jE2fAyHjxGCCvQc68WSQ.gif](../_resources/7da8430f3c2373e18a2a16a420464c4d.jpg)
Adding log points with variables

## Tasks

VSCode tasks are a great way to bring terminal commands into VS Code (e.g, starting-up dependencies using before debugging). This allows you to quickly run frequently used shell commands with a few keystrokes.

The additional benefit of tasks is that you can even configure a given task to run immediately before a debug session is started or run immediately after a debug session using `[preLaunchTask](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)`[and](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)`[postDebugTask](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)`[properties](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes) in your `launch.json` debug config. This is extremely helpful to automate preparation commands/clean up commands when debugging. (e.g, Startup 3rd party dependencies in docker as `preLaunchTask`, and stopping dependencies once the debug session finishes as a `postDebugTask`).

![1*PKgMKYCI-OXBtiN-q24o7Q.gif](../_resources/1d9a0f4841e5fc36c00d07f1a4602f2d.jpg)

## User Inputs in Tasks and Launch Configurations

If we need to frequently change the arguments of a shell command in a VSCode task, we can define it as a [VSCode input variable](https://code.visualstudio.com/docs/editor/variables-reference#_input-variables) and provide it when the task is about to run. VSCode inputs can be used both in tasks as well as launch configurations which makes them extremely helpful.

![1*jZjyNhN4eIJ3ZnoXDcCE3g.gif](../_resources/c51cafe0a11ccfe2ead0538775101623.jpg)

I hope this might have helped you improve your productivity, and urged you to discover more of what VSCode can do as a FREE IDE.