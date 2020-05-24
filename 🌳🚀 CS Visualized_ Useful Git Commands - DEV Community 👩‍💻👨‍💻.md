🌳🚀 CS Visualized: Useful Git Commands - DEV Community 👩‍💻👨‍💻

#  CS Visualized: Useful Git Commands

###     [![f497603e-77e4-4cfc-ae1a-a9214062aac4.jpeg](../_resources/9505bbb67c4701ea3c1be13d896264c1.jpg)  Lydia Hallie](https://dev.to/lydiahallie)    [![twitter-logo-42be7109de07f8c991a9832d432c9d12ec1a965b5c0004bca9f6aa829ae43209.png](../_resources/f573ab03b684f7f71ba8c12e699583f1.png)](http://twitter.com/lydiahallie)  [![github-logo-6a5bca60a4ebf959a6df7f08217acd07ac2bc285164fae041eacb8a148b1bab9.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](http://github.com/lydiahallie)  Apr 1  ・9 min read

 [#git](https://dev.to/t/git)  [#computerscience](https://dev.to/t/computerscience)  [#tutorial](https://dev.to/t/tutorial)

Although Git is a very powerful tool, I think most people would agree when I say it can also be... a total nightmare I've always found it very useful to visualize in my head what's happening when working with Git: how are the branches interacting when I perform a certain command, and how will it affect the history? Why did my coworker cry when I did a hard reset on `master`, `force push`ed to origin and `rimraf`'d the `.git` folder?

I thought it would be the perfect use case to create some visualized examples of the most common and useful commands! Many of the commands I'm covering have optional arguments that you can use in order to change their behavior. In my examples, I'll cover the default behavior of the commands without adding (too many) config options!

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  [Merge](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#merge) |  [Rebase](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#rebase) |  [Reset](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#reset) |  [Revert](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#revert) |  [Cherry-Pick](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#cherry-pick) |  [Fetch](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#fetch) |  [Pull](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#pull) |  [Reflog](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#reflog) |

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#merging)  Merging

Having multiple branches is extremely convenient to keep new changes separated from each other, and to make sure you don't accidentally push unapproved or broken changes to production. Once the changes have been approved, we want to get these changes in our production branch!

One way to get the changes from one branch to another is by performing a `git merge`! There are two types of merges Git can perform: a **fast-forward**, or a **no-fast-forward**

This may not make a lot of sense right now, so let's look at the differences!

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#fastforward-raw-ff-endraw-) Fast-forward (`--ff`)

A **fast-forward merge** can happen when the current branch has no extra commits compared to the branch we’re merging. Git is... *lazy* and will first try to perform the easiest option: the fast-forward! This type of merge doesn’t create a new commit, but rather merges the commit(s) on the branch we’re merging right in the current branch

[![894znjv4oo9agqiz4dql.gif](../_resources/80a43c9d8428273cc9cabe71256eb9ef.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--cT4TSe48--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/894znjv4oo9agqiz4dql.gif)

Perfect! We now have all the changes that were made on the `dev` branch available on the `master` branch. So, what's the **no-fast-forward** all about?

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#nofastfoward-raw-noff-endraw-) No-fast-foward (`--no-ff`)

It's great if your current branch doesn't have any extra commits compared to the branch that you want to merge, but unfortunately that's rarely the case! If we committed changes on the current branch that the branch we want to merge doesn't have, git will perform a *no-fast-forward* merge.

With a no-fast-forward merge, Git creates a new *merging commit* on the active branch. The commit's parent commits point to both the active branch and the branch that we want to merge!

[![rf1o2b6eduboqwkigg3w.gif](../_resources/62ff91795bae36fbebac5417ef64d65e.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--zRZ0x2Vc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/rf1o2b6eduboqwkigg3w.gif)

No big deal, a perfect merge! The `master` branch now contains all the changes that we've made on the `dev` branch.

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#merge-conflicts) Merge Conflicts

Although Git is good at deciding how to merge branches and add changes to files, it cannot always make this decision all by itself This can happen when the two branches we're trying to merge have changes on the same line in the same file, or if one branch deleted a file that another branch modified, and so on.

In that case, Git will ask you to help decide which of the two options we want to keep! Let's say that on both branches, we edited the first line in the `README.md`.

[![m3nxmp67mqof5sa3iik9.png](../_resources/0e0a32426780c1af0fbf82aec5469d69.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--jXqGWUai--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m3nxmp67mqof5sa3iik9.png)

If we want to merge `dev` into `master`, this will end up in a merge conflict: would you like the title to be `Hello!` or `Hey!`?

When trying to merge the branches, Git will show you where the conflict happens. We can manually remove the changes we don't want to keep, save the changes, add the changed file again, and commit the changes

[![bcd5ajtoc0g5dxzmpfbq.gif](../_resources/2d172cd27988be50b3650b99fd6e58d4.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--7lBksXwA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bcd5ajtoc0g5dxzmpfbq.gif)

Yay! Although merge conflicts are often quite annoying, it makes total sense: Git shouldn't just *assume* which change we want to keep.

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#rebasing)  Rebasing

We just saw how we could apply changes from one branch to another by performing a `git merge`. Another way of adding changes from one branch to another is by performing a `git rebase`.

A `git rebase`  *copies* the commits from the current branch, and puts these copied commits on top of the specified branch.

[![dwyukhq8yj2xliq4i50e.gif](../_resources/503cc08c3e05fd29566f841aaab4be26.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--EIY4OOcE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/dwyukhq8yj2xliq4i50e.gif)

Perfect, we now have all the changes that were made on the `master` branch available on the `dev` branch!

A big difference compared to merging, is that Git won't try to find out which files to keep and not keep. The branch that we're rebasing always has the latest changes that we want to keep! You won't run into any merging conflicts this way, and keeps a nice linear Git history.

This example shows rebasing on the `master` branch. In bigger projects, however, you usually don't want to do that. A `git rebase`  **changes the history of the project** as new hashes are created for the copied commits!

Rebasing is great whenever you're working on a feature branch, and the master branch has been updated. You can get all the updates on your branch, which would prevent future merging conflicts!

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#interactive-rebase) Interactive Rebase

Before rebasing the commits, we can modify them! We can do so with an *interactive rebase*. An interactive rebase can also be useful on the branch you're currently working on, and want to modify some commits.

There are 6 actions we can perform on the commits we're rebasing:

- `reword`: Change the commit message
- `edit`: Amend this commit
- `squash`: Meld commit into the previous commit
- `fixup`: Meld commit into the previous commit, without keeping the commit's log message
- `exec`: Run a command on each commit we want to rebase
- `drop`: Remove the commit

Awesome! This way, we can have full control over our commits. If we want to remove a commit, we can just `drop` it.

[![msofpv7k6rcmpaaefscm.gif](../_resources/0e19f8d320756a122822dd012b614d69.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--P6jr7igd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/msofpv7k6rcmpaaefscm.gif)

Or if we want to squash multiple commits together to get a cleaner history, no problem!

[![bc1r460xx1i0blu0lnnm.gif](../_resources/df6dafa1130f3dec3d27ce2ce3e930ac.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--VSQt4g1V--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bc1r460xx1i0blu0lnnm.gif)

Interactive rebasing gives you a lot of control over the commits you're trying to rebase, even on the current active branch!

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#resetting)  Resetting

It can happen that we committed changes that we didn't want later on. Maybe it's a `WIP` commit, or maybe a commit that introduced bugs! In that case, we can perform a `git reset`.

A `git reset` gets rid of all the current staged files and gives us control over where `HEAD` should point to.

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#soft-reset) Soft reset

A *soft reset* moves `HEAD` to the specified commit (or the index of the commit compared to `HEAD`), without getting rid of the changes that were introduced on the commits afterward!

Let's say that we don't want to keep the commit `9e78i` which added a `style.css` file, and we also don't want to keep the commit `035cc` which added an `index.js` file. However, we do want to keep the newly added `style.css` and `index.js` file! A perfect use case for a soft reset.

[![je5240aqa5uw9d8j3ibb.gif](../_resources/d8e016059f15e9f8e998aaf56b681eca.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s---GveiZe---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/je5240aqa5uw9d8j3ibb.gif)

When typing `git status`, you'll see that we still have access to all the changes that were made on the previous commits. This is great, as this means that we can fix the contents of these files and commit them again later on!

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#hard-reset) Hard reset

Sometimes, we don't want to keep the changes that were introduced by certain commits. Unlike a soft reset, we shouldn't need to have access to them any more. Git should simply reset its state back to where it was on the specified commit: this even includes the changes in your working directory and staged files!

[![hlh0kowt3hov1xhcku38.gif](../_resources/f34c2538fa3aa266fcea413c2b742a5c.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--GqjwnYkF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hlh0kowt3hov1xhcku38.gif)

Git has discarded the changes that were introduced on `9e78i` and `035cc`, and reset its state to where it was on commit `ec5be`.

* * *

###   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#reverting)  Reverting

Another way of undoing changes is by performing a `git revert`. By reverting a certain commit, we create a *new commit* that contains the reverted changes!

Let's say that `ec5be` added an `index.js` file. Later on, we actually realize we didn't want this change introduced by this commit anymore! Let's revert the `ec5be` commit.

[![3kkd2ahn41zixs12xgpf.gif](../_resources/cd957d4199859604a4e0886ed9a1b191.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--eckmvr2M--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/3kkd2ahn41zixs12xgpf.gif)

Perfect! Commit `9e78i` reverted the changes that were introduced by the `ec5be` commit. Performing a `git revert` is very useful in order to undo a certain commit, without modifying the history of the branch.

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#cherrypicking)  Cherry-picking

When a certain branch contains a commit that introduced changes we need on our active branch, we can `cherry-pick` that command! By `cherry-pick`ing a commit, we create a new commit on our active branch that contains the changes that were introduced by the `cherry-pick`ed commit.

Say that commit `76d12` on the `dev` branch added a change to the `index.js` file that we want in our `master` branch. We don't want the *entire* we just care about this one single commit!

[![2dkjx4yeaal10xyvj29v.gif](../_resources/5416bb03860d585a2232abe9300f1438.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--9vWP_K4S--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/2dkjx4yeaal10xyvj29v.gif)

Cool, the master branch now contains the changes that `76d12` introduced!

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#fetching)  Fetching

If we have a remote Git branch, for example a branch on Github, it can happen that the remote branch has commits that the current branch doesn't have! Maybe another branch got merged, your colleague pushed a quick fix, and so on.

We can get these changes locally, by performing a `git fetch` on the remote branch! It doesn't affect your local branch in any way: a `fetch` simply downloads new data.

[![bulx1voegfji4vwgndh4.gif](../_resources/88ab17c871551045edf2999eacbd42b8.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--38PuARw2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bulx1voegfji4vwgndh4.gif)

We can now see all the changes that have been made since we last pushed! We can decide what we want to do with the new data now that we have it locally.

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#pulling)  Pulling

Although a `git fetch` is very useful in order to get the remote information of a branch, we can also perform a `git pull`. A `git pull` is actually two commands in one: a `git fetch`, and a `git merge`. When we're pulling changes from the origin, we're first fetching all the data like we did with a `git fetch`, after which the latest changes are automatically merged into the local branch.

[![zifpnl1h6a4tk4qdc9sy.gif](../_resources/cdffd653e6deacc8bc19a40bba03d8a6.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s---X5AXldj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/zifpnl1h6a4tk4qdc9sy.gif)

Awesome, we're now perfectly in sync with the remote branch and have all the latest changes!

* * *

##   [(L)](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#reflog)  Reflog

Everyone makes mistakes, and that's totally okay! Sometimes it may feel like you've screwed up your git repo so badly that you just want to delete it entirely.

`git reflog` is a very useful command in order to show a log of all the actions that have been taken! This includes merges, resets, reverts: basically any alteration to your branch.

[![1aqek1py1knwl926ele7.gif](../_resources/73c628fe7f26e902d342d41383a8791e.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--MMUdOS0P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1aqek1py1knwl926ele7.gif))

If you made a mistake, you can easily redo this by resetting `HEAD` based on the information that `reflog` gives us!

Say that we actually didn't want to merge the origin branch. When we execute the `git reflog` command, we see that the state of the repo before the merge is at `HEAD@{1}`. Let's perform a `git reset` to point HEAD back to where it was on `HEAD@{1}`!

[![9z9rhtbw7mrigp0miijz.gif](../_resources/c05eaa5e4fe457e54267aabc95de2e93.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--A1UMM2AH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/9z9rhtbw7mrigp0miijz.gif)

We can see that the latest action has been pushed to the `reflog`!

* * *

Git has so many useful porcelain and plumbing commands, I wish I could cover them all! I know there are many other commands or alterations that I didn't have time for to cover right now - let me know what your favorite/most useful commands are, and I may cover them in another post!

And as always, feel free to reach out to me!

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| ✨ [Twitter](https://www.twitter.com/lydiahallie) | ‍ [Instagram](https://www.instagram.com/theavocoder) |  [GitHub](https://www.github.com/lydiahallie) |  [LinkedIn](https://www.linkedin.com/in/lydia-hallie) |  [YouTube](https://www.youtube.com/channel/UC4EWKIKdKiDtAscQ9BIXwUw) |  [Email](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1#fetchmailto:lydiahallie.dev@gmail.com%22) |