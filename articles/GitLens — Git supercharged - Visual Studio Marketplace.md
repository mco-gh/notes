GitLens — Git supercharged - Visual Studio Marketplace

[![eamodio.gitlens.png](../_resources/ec6d1ea18a25244f414ccfa44b3218fd.png)](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)[![eamodio.gitlens.png](../_resources/61c42c1599068e0936ef308f9baf797b.png)](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)[![eamodio.gitlens.png](../_resources/5a789b091ac1ec177a65b9d26f0af297.png)](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)[![vscode--dev--community-gitlens-blue.png](../_resources/d0cb220444b3aa4985cfeb80c641dfe5.png)](https://join.slack.com/t/vscode-dev-community/shared_invite/enQtMjIxOTgxNDE3NzM0LWU5M2ZiZDU1YjBlMzdlZjA2YjBjYzRhYTM5NTgzMTAxMjdiNWU0ZmQzYWI3MWU5N2Q1YjBiYmQ4MzY0NDE1MzY)

 [![gitlens-logo.png](../_resources/f51ea0fe06d79e26acb08b6168b26344.png)](https://gitlens.amod.io/)

> GitLens **> supercharges**>  the Git capabilities built into Visual Studio Code. It helps you to **> visualize code authorship**>  at a glance via Git blame annotations and code lens, **> seamlessly navigate and explore**>  Git repositories, **> gain valuable insights**>  via powerful comparison commands, and so much more.

# Sponsors

 [![codestream-light.png](../_resources/8d4c7f7e7bc6b4c42a40b3730ee2019a.png)](https://codestream.com/?utm_source=vscmarket&utm_medium=banner&utm_campaign=gitlens)

  CodeStream enables continuous code review by putting team chat in VS Code. Save discussions about code with your code. Integrates w/Slack.

 [![cresus.png](../_resources/ce9bfb8c397eb3bddba62763c0e54b5a.png)](https://cresus.ch/)

# Support GitLens

While GitLens is generously offered to everyone free of charge, if you find it useful, please consider [**supporting**](https://gitlens.amod.io/#support-gitlens) it.

- [**Become a Sponsor**](https://www.patreon.com/eamodio) — join the growing group of generous [backers](https://github.com/eamodio/vscode-gitlens/blob/master/BACKERS.md)
- [**Donate via PayPal**](https://www.paypal.me/eamodio) or [**Donate via Cash App**](https://cash.me/%24eamodio)

Also please [write a review](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#review-details), [star or fork me on GitHub](https://github.com/eamodio/vscode-gitlens), and [follow me on Twitter](https://twitter.com/eamodio)

# What's new in GitLens 9

- Adds GitLens over Visual Studio Live Share
    - Live Share guests will now have read-only access to GitLens' features
- Adds a new Git virtual file system provider for the [object Object] scheme — closes [#430](https://github.com/eamodio/vscode-gitlens/issues/430)
    - Replaces GitLens' internal handling of file revisions, which allows for better performance, as well as avoiding the use of temp files. It also provides a much better experience when dealing with file encodings, images, etc.
- Adds an *Explore the Repository from Here* ([object Object]) command which opens a virtual workspace folder (uses the Git virtual file system provider) for the repository at the specified point in time (commit, branch, tag, etc) — closes [#398](https://github.com/eamodio/vscode-gitlens/issues/398)
- Adds a new [*Repositories* view](https://github.com/eamodio/vscode-gitlens/tree/master/#repositories-view-), formerly the *GitLens* view, to visualize, navigate, and explore Git repositories — closes [#456](https://github.com/eamodio/vscode-gitlens/issues/456), [#470](https://github.com/eamodio/vscode-gitlens/issues/470), [#494](https://github.com/eamodio/vscode-gitlens/issues/494)
    - Provides a cleaner information-rich view of your opened repositories, more git commands (fetch, push, pull, checkout, stage, unstage, etc), better visibility and accessibility of existing features, and [more](https://github.com/eamodio/vscode-gitlens/tree/master/#repositories-view-)
- Adds a new [*File History* view](https://github.com/eamodio/vscode-gitlens/tree/master/#file-history-view-), formerly the *History* view, to visualize, navigate, and explore the revision history of the current file
    - Provides similar features to the former *History* view as well as quickly toggling file tracking on and off, changing the base (branch, tag, commit, etc) of the file's history, and [more](https://github.com/eamodio/vscode-gitlens/tree/master/#file-history-view-)
- Adds an all-new [*Line History* view](https://github.com/eamodio/vscode-gitlens/tree/master/#line-history-view-) to visualize, navigate, and explore the revision history of the selected lines of current file — closes [#354](https://github.com/eamodio/vscode-gitlens/issues/354)
    - Provides similar features to the *File History* view including quickly toggling line tracking on and off, changing the base (branch, tag, commit, etc) of the selected lines' history, and [more](https://github.com/eamodio/vscode-gitlens/tree/master/#line-history-view-)
- Adds an all-new [*Search Commits* view](https://github.com/eamodio/vscode-gitlens/tree/master/#search-commits-view-) to search and explore commit histories by message, author, files, id, etc — closes [#455](https://github.com/eamodio/vscode-gitlens/issues/455)
    - Provides somewhat similar features to the former *Results* view as well as it is now a persistent view, makes it easier to start a commit search, and [more](https://github.com/eamodio/vscode-gitlens/tree/master/#search-commits-view-)
- Adds an all-new [*Compare* view](https://github.com/eamodio/vscode-gitlens/tree/master/#compare-view-) to visualize comparisons between branches, tags, commits, and more
    - Provides somewhat similar and powerful features to the former *Results* view as well as it is now a persistent view, makes it easier to start a comparison, and [more](https://github.com/eamodio/vscode-gitlens/tree/master/#compare-view-)
- And much more

See the [release notes](https://github.com/eamodio/vscode-gitlens/blob/master/CHANGELOG.md) for the full set of changes

# GitLens

[GitLens](https://gitlens.amod.io/) is an [open-source](https://github.com/eamodio/vscode-gitlens) extension for [Visual Studio Code](https://code.visualstudio.com/) created by [Eric Amodio](https://www.amod.io/).

GitLens simply helps you **better understand code**. Quickly glimpse into whom, why, and when a line or code block was changed. Jump back through history to **gain further insights** as to how and why the code evolved. Effortlessly explore the history and evolution of a codebase.

While GitLens is **powerful and feature rich**, it is also [highly customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gitlens-settings-) to meet your specific needs — find code lens intrusive or the current line blame annotation distracting — no problem, it is quick and easy to turn them off or change how they behave via the built-in [*GitLens Settings* editor](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#configuration), an **interactive editor** covering many of GitLens' powerful settings. While for more advanced customizations, refer to the [GitLens settings docs](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gitlens-settings-) and edit your vscode [user settings](https://code.visualstudio.com/docs/getstarted/settings).

Here are just some of the **features** that GitLens provides,

- an unobtrusive [**current line blame**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#current-line-blame-) annotation at the end of the line with detailed blame information accessible via [**hovers**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hovers-)
- on-demand [**gutter blame**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-) annotations, including a heatmap, for the whole file
- [**authorship code lens**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-) showing the most recent commit and # of authors to the top of files and/or on code blocks
- on-demand [**gutter heatmap**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-heatmap-) annotations to show how recently lines were changed, relative to all the other changes in the file and to now (hot vs. cold)
- on-demand [**recent changes**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#recent-changes-) annotations to highlight lines changed by the most recent commit
- a [**status bar blame**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-blame-) annotation showing author and date for the current line
- many rich Side Bar views
    - a [***Repositories* view**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-) to visualize, navigate, and explore Git repositories
    - a [***File History* view**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#file-history-view-) to visualize, navigate, and explore the revision history of the current file
    - a [***Line History* view**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#line-history-view-) to visualize, navigate, and explore the revision history of the selected lines of current file
    - a [***Search Commits* view**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#search-commits-view-) to search and explore commit histories by message, author, files, id, etc
    - a [***Compare* view**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#compare-view-) to visualize comparisons between branches, tags, commits, and more
- many [**powerful commands**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#navigate-and-explore-) for exploring commits and histories, comparing and navigating revisions, stash access, repository status, etc
- user-defined [**modes**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#modes-) for quickly toggling between sets of settings
- and so much [**more**](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#and-more-)

 ![gitlens-preview.gif](../_resources/0d2d9a58f23bd32743c7858792488955.gif)

# Configuration

 ![settings.png](../_resources/a4149e1af865439330a9b0675d02621a.png)

GitLens has a built-in **interactive settings editor** which provides an easy-to-use interface to configure many of GitLens' powerful features. It can be accessed via the *Open Settings* ([object Object]) command from the [*Command Palette*](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

For more advanced customizations, refer to the [settings documentation](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gitlens-settings-) below.

# Features

### Current Line Blame [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#current-line-blame-)

 ![current-line-blame.png](../_resources/25943188993b5d1fc176321fe6796018.png)

- Adds an unobtrusive, [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#current-line-blame-settings-), and [themable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#themable-colors-), **blame annotation** at the end of the current line
    - Contains the author, date, and message of the current line's most recent commit (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#current-line-blame-settings-))
    - Adds a *Toggle Line Blame Annotations* command ([object Object]) to toggle the blame annotation on and off

* * *

### Gutter Blame [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-)

 ![gutter-blame.png](../_resources/1911fa98f8dc3dcdf967e73e20ee9136.png)

- Adds on-demand, [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-settings-), and [themable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#themable-colors-), **gutter blame annotations** for the whole file
    - Contains the commit message and date, by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-settings-)
    - Adds a **heatmap** (age) indicator on right edge (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-settings-)) of the gutter to provide an easy, at-a-glance way to tell how recently lines were changed ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-settings-), on by default)
        - See the [gutter heatmap](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-Heatmap-) section below for more details
    - Adds a *Toggle File Blame Annotations* command ([object Object]) with a shortcut of [object Object] to toggle the blame annotations on and off
    - Press [object Object] to turn off the annotations

* * *

### Hovers [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hovers-)

#### Current Line Hovers

 ![hovers-current-line.png](../_resources/fd7bccc0deb46023e8b04e67c38330f6.png)

- Adds [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-) Git blame hovers accessible over the current line

##### Details Hover

 ![hovers-current-line-details.png](../_resources/748ae71c7edce5cf2d8eac34f57687d4.png)

- Adds a **details hover** annotation to the current line to show more commit details ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-), on by default)
    - Provides automatic issue linking to Bitbucket, GitHub, GitLab, and Visual Studio Team Services in commit messages
    - Provides a **quick-access command bar** with *Open Changes*, *Blame Previous Revision*, *Open on Remote*, and *Show More Actions* command buttons
    - Click the commit id to execute the *Show Commit Details* command

##### Changes (diff) Hover

 ![hovers-current-line-changes.png](../_resources/681bfee94f8ddd142df24964a7c7c757.png)

- Adds a **changes (diff) hover** annotation to the current line to show the line's previous version ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-), on by default)
    - Click the **Changes** to execute the *Open Changes* command
    - Click the current and previous commit ids to execute the *Show Commit Details* command

#### Annotation Hovers

 ![hovers-annotations.png](../_resources/d8cf05920521ad9cdd9f6c649f6167f4.png)

- Adds [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-) Git blame hovers accessible when annotating

##### Details Hover

 ![hovers-annotations-details.png](../_resources/d4ab2e2a453d5312465f4d8e48dfa7c4.png)

- Adds a **details hover** annotation to each line while annotating to show more commit details ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-), on by default)
    - Provides automatic issue linking to Bitbucket, GitHub, GitLab, and Visual Studio Team Services in commit messages
    - Provides a **quick-access command bar** with *Open Changes*, *Blame Previous Revision*, *Open on Remote*, and *Show More Actions* command buttons
    - Click the commit id to execute the *Show Commit Details* command

##### Changes (diff) Hover

 ![hovers-annotations-changes.png](../_resources/0f88d543952a1c8ea1d7d52dbbc9b645.png)

- Adds a **changes (diff) hover** annotation to each line while annotating to show the line's previous version ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-), on by default)
    - Click the **Changes** to execute the *Open Changes* command
    - Click the current and previous commit ids to execute the *Show Commit Details* command

* * *

### Code Lens [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-)

 ![code-lens.png](../_resources/5158b37a8ecac0cd947eb24e40516838.png)

- Adds Git authorship **code lens** to the top of the file and on code blocks ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-settings-), on by default)
    - **Recent Change** — author and date of the most recent commit for the file or code block
        - Click the code lens to show a **commit file details quick pick menu** with commands for comparing, navigating and exploring commits, and more (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-settings-))
    - **Authors** — number of authors of the file or code block and the most prominent author (if there is more than one)
        - Click the code lens to toggle the file Git blame annotations on and off of the whole file (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-settings-))
        - Will be hidden if the author of the most recent commit is also the only author of the file or block, to avoid duplicate information and reduce visual noise
    - Provides [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-settings-) click behavior for each code lens — choose between one of the following
        - Toggle file blame annotations on and off
        - Compare the commit with the previous commit
        - Show a quick pick menu with details and commands for the commit
        - Show a quick pick menu with file details and commands for the commit
        - Show a quick pick menu with the commit history of the file
        - Show a quick pick menu with the commit history of the current branch
- Adds a *Toggle Git Code Lens* command ([object Object]) with a shortcut of [object Object] to toggle the code lens on and off

* * *

### Gutter Heatmap [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-heatmap-)

 ![heatmap.png](../_resources/e3f41cbdf079588359569fe8032b50d4.png)

- Adds an on-demand **heatmap** to the edge of the gutter to show how recently lines were changed
    - The indicator's [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-heatmap-settings-) color will either be hot or cold based on the age of the most recent change (cold after 90 days by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-heatmap-settings-))
    - The indicator's brightness ranges from bright (newer) to dim (older) based on the relative age, which is calculated from the median age of all the changes in the file
    - Adds *Toggle File Heatmap Annotations* command ([object Object]) to toggle the heatmap on and off
    - Press [object Object] to turn off the annotations

* * *

### Recent Changes [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#recent-changes-)

 ![recent-changes.png](../_resources/13c2c9249f2fa86dfbd42935b9fb9c33.png)

- Adds an on-demand, [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#recent-changes-settings-) and [themable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#themable-colors-), **recent changes annotation** to highlight lines changed by the most recent commit
    - Adds *Toggle Recent File Changes Annotations* command ([object Object]) to toggle the recent changes annotations on and off
    - Press [object Object] to turn off the annotations

* * *

### Status Bar Blame [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-blame-)

 ![status-bar.png](../_resources/8847aba78c150cc47690e55acf6a41e9.png)

- Adds a [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-)  **Git blame annotation** about the current line to the **status bar** ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-), on by default)
    - Contains the commit author and date (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-))
    - Click the status bar item to show a **commit details quick pick menu** with commands for comparing, navigating and exploring commits, and more (by [default](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-))
    - Provides [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-) click behavior — choose between one of the following
        - Toggle file blame annotations on and off
        - Toggle code lens on and off
        - Compare the line commit with the previous commit
        - Compare the line commit with the working tree
        - Show a quick pick menu with details and commands for the commit (default)
        - Show a quick pick menu with file details and commands for the commit
        - Show a quick pick menu with the commit history of the file
        - Show a quick pick menu with the commit history of the current branch

* * *

## Side Bar Views

### Repositories view [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-)

 ![view-repositories.png](../_resources/5a36e3789d7e81651e1357c967c50281.png)

A [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-) view to visualize, navigate, and explore Git repositories

- A toolbar provides quick access to the *Push Repositories*, *Pull Repositories*, *Fetch Repositories*, and *Refresh* commands
    - A context menu provides *Automatic Layout*, *List Layout*, *Tree Layout*, *Enable Automatic Refresh* or *Disable Automatic Refresh*, *Open Settings* commands

The repositories view provides the following features,

- **Repositories** — lists the opened repositories
    - Provides the name of each repository, the name of its current branch, [optionally](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-) its working tree status, and when it was last fetched
        - Indicator dots on each repository icon denote the following:
            - *None* — no upstream or up-to-date with the upstream
            - *Green* — ahead of the upstream
            - *Red* — behind the upstream
            - *Yellow* — both ahead of and behind the upstream
        - An inline toolbar provides quick access to the *Add to Favorites* (when applicable), *Remove from Favorites* (when applicable), *Search Commits*, *Push* ([object Object] for *Push (force)*), *Pull*, and *Fetch* commands
        - A context menu provides access to more common repository commands
        - **Current Branch** — lists the revision (commit) history of the current branch and [optionally](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-) shows its remote tracking branch and status (if available)
            - An inline toolbar provides quick access to the *Compare with Remote* (if available), *Compare with Working Tree*, and *Open Branch on Remote* (if available) commands
            - A context menu provides access to more common branch commands
        - *** Commits Behind** — quickly see and explore the specific commits behind the upstream (i.e. commits that haven't been pulled)
            - Only provided if the current branch is tracking a remote branch and is behind it
            - An inline toolbar provides quick access to the *Pull* command
        - *** Commits Ahead** — quickly see and explore the specific commits ahead of the upstream (i.e. commits that haven't been pushed)
            - Only provided if the current branch is tracking a remote branch and is ahead of it
            - An inline toolbar provides quick access to the *Push* ([object Object] for *Push (force)*) command
        - *** Files Changed** — lists all the "working" changes
            - Expands to a file-based view of all changed files in the working tree ([optionally](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-)) and/or all files in all commits ahead of the upstream
            - An inline toolbar provides quick access to the *Stash All Changes* command
- **Branches** — lists the local branches in the repository
    - An inline toolbar provides quick access to the *Open Branches on Remote* (if available) command
    - Provides the name of each branch, an indicator (check-mark) of the branch is the current one, and [optionally](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-) shows its remote tracking branch and status (if available)
        - Indicator dots on each branch icon denote the following:
            - *None* — no upstream or up-to-date with the upstream
            - *Green* — ahead of the upstream
            - *Red* — behind the upstream
            - *Yellow* — both ahead of and behind the upstream
        - An inline toolbar provides quick access to the *Add to Favorites* (when applicable), *Remove from Favorites* (when applicable), *Checkout*, *Compare with Remote* (if available), *Compare with HEAD* ([object Object] for *Compare with Working Tree*), and *Open Branch on Remote* (if available) commands
        - A context menu provides access to more common branch commands
        - Each branch expands to list its revision (commit) history
            - *** Commits Behind** — quickly see and explore the specific commits behind the upstream (i.e. commits that haven't been pulled)
                - Only provided if the current branch is tracking a remote branch and is behind it
            - *** Commits Ahead** — quickly see and explore the specific commits ahead of the upstream (i.e. commits that haven't been pushed)
                - Only provided if the current branch is tracking a remote branch and is ahead of it
            - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open Commit on Remote* (if available) commands
            - A context menu provides access to more common revision (commit) commands
            - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
                - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
                - A context menu provides access to more common file revision commands
- **Remotes** — lists the remotes in the repository
    - Provides the name of each remote, an indicator of the direction of the remote (fetch, push, both), remote service (if applicable), and repository path
        - An inline toolbar provides quick access to the *Fetch*, and *Open Repository on Remote* (if available) commands
        - A context menu provides access to more common repository and remote commands
        - Each remote expands list its remote branches
            - See the **Branches** above for additional details
- **Stashes** — lists the stashed changes in the repository
    - An inline toolbar provides quick access to the *Stash All Changes*, and *Apply Stash Changes* commands
    - Provides the name of each stashed changes, the date, and an indicator (+x ~x -x) of the changes
        - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Apply Stashed Changes*, and *Delete Stashed Changes* commands
        - A context menu provides access to more common stashed changes commands
        - Each stashed changes expands to list the set of stashed files, complete with status indicators for adds, changes, renames, and deletes
            - An inline toolbar provides quick access to the *Open File*, and *Open File on Remote* (if available) commands
            - A context menu provides access to more common file revision commands
- **Tags** — lists the tags in the repository
    - Provides the name of each tag
        - An inline toolbar provides quick access to the *Checkout, and _Compare with HEAD* ([object Object] for *Compare with Working Tree*) commands
        - A context menu provides access to more common tag commands
        - Each tags expands to list its revision (commit) history
            - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open Commit on Remote* (if available) commands
            - A context menu provides access to more common revision (commit) commands
            - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
                - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
                - A context menu provides access to more common file revision commands

* * *

### File History view [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#file-history-view-)

 ![view-file-history.png](../_resources/f4962d51d8ee3b29c44304d6d8c5a35a.png)

A [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#file-history-view-settings-) view to visualize, navigate, and explore the revision history of the current file

- A toolbar provides quick access to the *Pause File Tracking* or *Resume File Tracking*, *Change Base...*, and *Refresh* commands
- A context menu provides the *Follow Renames* or *Don't Follow Renames*, and *Open Settings* commands

The file history view provides the following features,

- Automatically tracks the current editor and lists the revision (commit) history of the current file
- An inline toolbar provides quick access to the *Open File*, and *Open File on Remote* (if available) commands
- A context menu provides *Open File*, *Open File on Remote* (if available), *Copy Remote Url to Clipboard* (if available), and *Refresh* commands
- Provides the message, author, and date of each revision (commit) — fully [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)
    - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open Commit on Remote* (if available) commands
    - A context menu provides access to more common revision (commit) commands
    - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
        - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
        - A context menu provides access to more common file revision commands

* * *

### Line History view [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#line-history-view-)

 ![view-line-history.png](../_resources/9c6d55ba14d2a51032206193b4bbc630.png)

A [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#line-history-view-settings-) view to visualize, navigate, and explore the revision history of the selected lines of current file

- A toolbar provides quick access to the *Pause File Tracking* or *Resume File Tracking*, *Change Base...*, and *Refresh* commands
- A context menu provides the *Follow Renames* or *Don't Follow Renames*, and *Open Settings* commands

The line history view provides the following features,

- Automatically tracks the current editor selection and lists the revision (commit) history of the selection in current file
- An inline toolbar provides quick access to the *Open File*, and *Open File on Remote* (if available) commands
- A context menu provides *Open File*, *Open File on Remote* (if available), *Copy Remote Url to Clipboard* (if available), and *Refresh* commands
- Provides the message, author, and date of each revision (commit) — fully [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)
    - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open Commit on Remote* (if available) commands
    - A context menu provides access to more common revision (commit) commands
    - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
        - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
        - A context menu provides access to more common file revision commands

* * *

### Search Commits view [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#search-commits-view-)

 ![view-search.png](../_resources/7e67e4ff70e4550eed7e0397545dc52b.png)

A [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#search-commits-view-settings-) view to search and explore commit histories by message, author, files, id, etc

- A toolbar provides quick access to the *Search Commits*, *Keep Results*, *Clear Results*, and *Refresh* commands
- A context menu provides *Automatic Layout*, *List Layout*, *Tree Layout*, *Open Settings* commands
- Use the *Search Commits* command ([object Object]) with a shortcut of [object Object] to search for commits
    - by message — use [object Object] to search for commits with messages that match [object Object] — See [Git docs](https://git-scm.com/docs/git-log#git-log---grepltpatterngt)
    - or, by author — use [object Object] to search for commits with authors that match [object Object] — See [Git docs](https://git-scm.com/docs/git-log#git-log---authorltpatterngt)
    - or, by commit id — use [object Object] to search for a commit with id of [object Object] — See [Git docs](https://git-scm.com/docs/git-log#git-log-ltrevisionrangegt)
    - or, by files — use [object Object] to search for commits with file names that match [object Object] — See [Git docs](https://git-scm.com/docs/git-log---ltpathgt82308203)
    - or, by changes — use [object Object] to search for commits with differences whose patch text contains added/removed lines that match [object Object] — See [Git docs](https://git-scm.com/docs/git-log#git-log--Gltregexgt)
    - or, by changed lines — use [object Object] to search for commits with differences that change the number of occurrences of the specified string (i.e. addition/deletion) in a file — See [Git docs](https://git-scm.com/docs/git-log#git-log--Sltstringgt)

The search commits view provides the following features,

- Provides a semi-persistent results view for searching and exploring commit histories
    - An inline toolbar provides quick access to the *Dismiss* command
    - A context menu provides access to common search commands
    - Provides the message, author, date, and change indicator of each revision (commit) — fully [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)
        - An inline toolbar provides quick access to the *Compare with HEAD* ([object Object] for *Compare with Working Tree*), *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open Commit on Remote* (if available) commands
        - A context menu provides access to more common revision (commit) commands
        - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
            - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
            - A context menu provides access to more common file revision commands
    - Results can be provided by the following commands
        - *Search Commits* command ([object Object])
        - *Show File History* command ([object Object])
        - *Show Commit Details* command ([object Object])

* * *

### Compare view [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#compare-view-)

 ![view-compare.png](../_resources/acd531bdcfcdef51b854d243036ca54e.png)

A [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#compare-view-settings-) view to visualize comparisons between branches, tags, commits, and more

- A toolbar provides quick access to the *Compare Branch or Tag with...*, *Keep Results*, *Clear Results*, and *Refresh* commands
- A context menu provides *Automatic Layout*, *List Layout*, *Tree Layout*, *Open Settings* commands

The compare view provides the following features,

- Provides a semi-persistent results view for comparison operations
    - An inline toolbar provides quick access to the *Swap Comparison*, *Pin Comparison* (when applicable), *Unpin Comparison* (when applicable), *Refresh*, and *Dismiss* commands
    - A context menu provides access to common comparison commands
    - *** Commits** — lists the commits between the compared revisions (branches or commits)
        - Expands to provide the message, author, date, and change indicator of each revision (commit) — fully [customizable](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)
            - Each revision (commit) expands to list its set of changed files, complete with status indicators for adds, changes, renames, and deletes
                - An inline toolbar provides quick access to the *Open File*, *Copy Commit ID to Clipboard* ([object Object] for *Copy Commit Message to Clipboard*), and *Open File on Remote* (if available) commands
                - A context menu provides access to more common file revision commands
    - *** Files Changed** — lists all of the files changed between the compared revisions (branches or commits)
        - Expands to a file-based view of all changed files in the working tree ([optionally](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#compare-view-settings-)) and/or all files in all commits ahead of the upstream
    - Results can be provided by the following commands
        - *Compare with Remote* command ([object Object])
        - *Compare with HEAD* command ([object Object])
        - *Compare with Working Tree* command ([object Object])
        - *Compare with Selected* command ([object Object])
        - *Compare Ancestry with Working Tree* command ([object Object])

* * *

### Modes [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#modes-)

- GitLens supports [user-defined](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#modes-settings-) modes for quickly toggling between sets of settings
    - Adds *Switch Mode* command ([object Object]) to quickly switch the active mode
    - Adds a built-in *Zen* mode which for a zen-like experience, disables many visual features
        - Adds *Toggle Zen Mode* command ([object Object]) to toggle Zen mode
    - Adds a built-in *Review* mode which for reviewing code, enables many visual features
        - Adds *Toggle Review Mode* command ([object Object]) to toggle Review mode
    - Adds the active mode to the **status bar** ([optional](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#modes-settings-), on by default)

* * *

### Navigate and Explore [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#navigate-and-explore-)

- Adds a *Show Last Opened Quick Pick* command ([object Object]) with a shortcut of [object Object] to quickly get back to where you were when the last GitLens quick pick menu closed
- Adds commands to Open files, commits, branches, and the repository on the supported remote services, **Bitbucket, GitHub, GitLab, and Visual Studio Team Services** or a [**user-defined** remote services](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#custom-remotes-settings) — only available if a Git upstream service is configured in the repository
    - Also supports [remote services with custom domains](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#custom-remotes-settings), such as **Bitbucket, Bitbucket Server (previously called Stash), GitHub, GitHub Enterprise, GitLab**
    - *Open Branches on Remote* command ([object Object]) — opens the branches on the supported remote service
    - *Open Branch on Remote* command ([object Object]) — opens the current branch commits on the supported remote service
    - *Open Commit on Remote* command ([object Object]) — opens the commit revision of the current line on the supported remote service
    - *Open File on Remote* command ([object Object]) — opens the current file/revision on the supported remote service
    - *Open Repository on Remote* command ([object Object]) — opens the repository on the supported remote service

#### Branch History

 ![menu-branch-history.png](../_resources/d3ed8701cd624886743d9f80b6ae84cd.png)

- Adds a *Show Current Branch History* command ([object Object]) with a shortcut of [object Object] to show a paged **branch history quick pick menu** of the current branch for exploring its commit history
    - Provides entries to *Show Commit Search* and *Open Branch on <remote-service>* when available
    - Navigate back to the previous quick pick menu via [object Object], if available
    - Navigate pages via [object Object] and [object Object] to go backward and forward respectively
- Adds a *Show Branch History* command ([object Object]) to show a paged **branch history quick pick menu** of the selected branch for exploring its commit history
    - Provides the same features as *Show Current Branch History* above

#### File History

 ![menu-file-history.png](../_resources/6af6db3630eae1417b3073195e423f8e.png)

- Adds a *Show File History* command ([object Object]) to show a paged **file history quick pick menu** of the current file for exploring its commit history
    - Provides additional entries to *Show in View*, *Show Branch History*, and *Open File on <remote-service>* when available
    - Navigate back to the previous quick pick menu via [object Object], if available
    - Navigate pages via [object Object] and [object Object] to go backward and forward respectively

#### Commit Details

 ![menu-commit-details.png](../_resources/369008ab645d53552925c41a09cb1c39.png)

- Adds a *Show Commit Details* command ([object Object]) to show a **commit details quick pick menu** of the most recent commit of the current file
    - Quickly see the set of files changed in the commit, complete with status indicators for adds, changes, renames, and deletes
    - Provides additional entries to *Show in View*, *Open Commit on <remote-service>* when available, *Open Files*, *Open Revisions*, *Open Directory Compare with Previous Revision*, *Open Directory Compare with Working Tree*, *Copy Commit ID to Clipboard*, *Copy Commit Message to Clipboard*
    - Navigate back to the previous quick pick menu via [object Object], if available
    - Use the [object Object] shortcut on an entry to execute it without closing the quick pick menu, if possible — commands that open windows outside of VS Code will still close the quick pick menu unless [[object Object]](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#advanced-settings-) is set
    - Use the [object Object] shortcut on a file entry in the [object Object] section to preview the comparison of the current revision with the previous one

 ![menu-commit-file-details.png](../_resources/88cf07e87e11da6a7668f65a426a8081.png)

- Adds a *Show Commit File Details* command ([object Object]) with a shortcut of [object Object] to show a **file commit details quick pick menu** of the most recent commit of the current file
    - Provides entries to *Open Changes*, *Open Changes with Working File*, *Open File*, *Open Revision*, *Open File on <remote-service>* when available, *Open Revision on <remote-service>* when available, *Copy Commit ID to Clipboard*, *Copy Commit Message to Clipboard*, *Show Commit Details*, *Show File History*, and *Show Previous File History*
    - Navigate back to the previous quick pick menu via [object Object], if available
    - Use the [object Object] shortcut on an entry to execute it without closing the quick pick menu, if possible — commands that open windows outside of VS Code will still close the quick pick menu unless [[object Object]](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#advanced-settings-) is set

#### Repository Status

 ![menu-repo-status.png](../_resources/7558fca0c36b0b3175afe01e8029f8d1.png)

- Adds a *Show Repository Status* command ([object Object]) with a shortcut of [object Object] to show a **repository status quick pick menu** for visualizing the current repository status
    - Quickly see upstream status (if an Git upstream is configured) — complete with ahead and behind information
        - If you are ahead of the upstream, an entry will be shown with the number of commits ahead. Choosing it will show a limited **branch history quick pick menu** containing just the commits ahead of the upstream
        - If you are behind the upstream, an entry will be shown with the number of commits behind. Choosing it will show a limited **branch history quick pick menu** containing just the commits behind the upstream
    - Quickly see all working changes, both staged and unstaged, complete with status indicators for adds, changes, renames, and deletes
    - Provides entries to *Show Stashed Changes*, *Open Changed Files*, and *Close Unchanged Files*
    - Use the [object Object] shortcut on an entry to execute it without closing the quick pick menu, if possible — commands that open windows outside of VS Code will still close the quick pick menu unless [[object Object]](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#advanced-settings-) is set
    - Use the [object Object] shortcut on a file entry in the [object Object] or [object Object] sections to preview the comparison of the working file with the previous revision

#### Stashes

 ![menu-stash-list.png](../_resources/23be6cd688a32174bd36ae8e2180519f.png)

- Adds a *Show Stashed Changes* command ([object Object]) to show a **stashed changes quick pick menu** for exploring your repository stash history
    - Provides additional entries to *Stash All Changes*
    - Navigate back to the previous quick pick menu via [object Object], if available
- Adds a *Stash All Changes* command ([object Object]) to save any working tree changes to the stash — can optionally provide a stash message
    - Also adds the command to the Source Control items context menu to stash an individual or group of files, works with multi-select too!

#### Stash Details

 ![menu-stash-details.png](../_resources/b152e020f9684f124e15f8b8190a3b20.png)

- Stashed changes show a **stash details quick pick menu** which is very similar to the **commit details quick pick menu** above
    - Quickly see the set of files changed in the stash, complete with status indicators for adds, changes, renames, and deletes
    - Provides additional entries to *Apply Stashed Changes* (requires confirmation), *Delete Stashed Changes* (requires confirmation), *Open Files*, *Open Revisions*, *Open Directory Compare with Previous Revision*, *Open Directory Compare with Working Tree*, *Copy Commit Message to Clipboard*
    - Navigate back to the previous quick pick menu via [object Object], if available
    - Use the [object Object] shortcut on an entry to execute it without closing the quick pick menu, if possible — commands that open windows outside of VS Code will still close the quick pick menu unless [[object Object]](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#advanced-settings-) is set
    - Use the [object Object] shortcut on a file entry in the [object Object] section to preview the comparison of the current revision with the previous one
- Adds an *Apply Stashed Changes* command ([object Object]) to chose a stash entry to apply to the working tree from a quick pick menu

* * *

### And More [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#and-more-)

#### Powerful Comparison Tools

- Effortlessly navigate between comparisons via the [object Object] and [object Object] shortcut keys to go back and forth through a file's revisions
- Provides easy access to the following comparison commands via the [object Object] as well as in context via the many provided quick pick menus
- Adds a *Directory Compare Working Tree with...* command ([object Object]) to open the configured Git difftool to compare the working tree with the selected branch or tag
- Adds a *Compare HEAD with Branch or Tag...* command ([object Object]) to compare the index (HEAD) with the selected branch or tag
- Adds a *Compare Working Tree with Branch or Tag...* command ([object Object]) to compare the working tree with the selected branch or tag
- Adds an *Open Changes with Branch or Tag...* command ([object Object]) to compare the current file with the same file on the selected branch or tag
- Adds an *Open Changes with Next Revision* command ([object Object]) with a shortcut of [object Object] to compare the current file/diff with the next commit revision
- Adds an *Open Changes with Previous Revision* command ([object Object]) with a shortcut of [object Object] to compare the current file/diff with the previous commit revision
- Adds an *Open Line Changes with Previous Revision* command ([object Object]) with a shortcut of [object Object] to compare the current file/diff with the previous line commit revision
- Adds an *Open Changes with Revision...* command ([object Object]) to compare the current file with the selected revision of the same file
- Adds an *Open Changes with Working File* command ([object Object]) with a shortcut of [object Object] to compare the most recent commit revision of the current file/diff with the working tree
- Adds an *Open Line Changes with Working File* command ([object Object]) with a shortcut of [object Object] to compare the commit revision of the current line with the working tree

#### Other Commands (not a complete list)

- Adds a *Copy Commit ID to Clipboard* command ([object Object]) to copy the commit id (sha) of the current line to the clipboard or from the most recent commit to the current branch, if there is no current editor
- Adds a *Copy Commit Message to Clipboard* command ([object Object]) to copy the commit message of the current line to the clipboard or from the most recent commit to the current branch, if there is no current editor
- Adds a *Copy Remote Url to Clipboard* command ([object Object]) to copy the remote url of the current file and line to the clipboard
- Adds an *Open Working File"* command ([object Object]) to open the working file for the current file revision
- Adds an *Open Revision...* command ([object Object]) to open the selected revision for the current file
- Adds an *Open Changes (with difftool)* command ([object Object]) to the source control group and source control resource context menus to open the changes of a file or set of files with the configured git difftool
- Adds an *Open All Changes (with difftool)* command ([object Object]) to open all working changes with the configured git difftool
    - Also adds the command to the Source Control group context menu
- Adds an *Directory Compare All Changes* command ([object Object]) to the source control groups to open the configured Git difftool to compare the working tree with HEAD
- Adds a *Open Changed Files* command ([object Object]) to open any files with working tree changes
- Adds a *Close Unchanged Files* command ([object Object]) to close any files without working tree changes

* * *

## GitLens Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gitlens-settings-)

GitLens is highly customizable and provides many configuration settings to allow the personalization of almost all features.

### General Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#general-settings-)Name

Description
[object Object]

Specifies how absolute dates will be formatted by default. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats

[object Object]

Specifies how short absolute dates will be formatted by default. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats

[object Object]
Specifies how dates will be displayed by default
[object Object]
Specifies the style of the gravatar default (fallback) images

[object Object] - a geometric pattern

[object Object] - a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)

[object Object] - a monster with different colors, faces, etc
[object Object] - 8-bit arcade-style pixelated faces
[object Object] - a robot with different colors, faces, etc
[object Object] - a face with differing features and backgrounds
[object Object]
Specifies whether to enable experimental features
[object Object]
Specifies the keymap to use for GitLens shortcut keys

[object Object] - adds an alternate set of shortcut keys that start with [object Object] (⌥ on macOS)

[object Object] - adds a chorded set of shortcut keys that start with [object Object] ([object Object] on macOS)

[object Object] - no shortcut keys will be added
[object Object]

Specifies whether to allow guest access to GitLens features when using Visual Studio Live Share

[object Object]
Specifies which commands will be added to which menus
[object Object]
Specifies how much (if any) output will be sent to the GitLens output channel
[object Object]
Specifies the display mode of the interactive settings editor

[object Object] - only displays common settings
[object Object] - displays all settings
[object Object]
Specifies whether to show What's New after upgrading to new feature releases

### Current Line Blame Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#current-line-blame-settings-)Name

Description
[object Object]

Specifies how to format absolute dates (using the [object Object] token) for the current line blame annotations. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats

[object Object]

Specifies whether to provide a blame annotation for the current line, by default. Use the *Toggle Line Blame Annotations* command ([object Object]) to toggle the annotations on and off for the current window

[object Object]

Specifies the format of the current line blame annotation. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object] — commit id
[object Object] — commit author
[object Object] — commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object] — formatted commit date (format specified by [object Object])
[object Object] — commit date specified by [object Object]
[object Object] — commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies whether the current line blame annotation can be scrolled into view when it is outside the viewport

### Gutter Blame Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-blame-settings-)Name

Description
[object Object]
Specifies whether to show avatar images in the gutter blame annotations
[object Object]

Specifies whether to compact (deduplicate) matching adjacent gutter blame annotations

[object Object]

Specifies how to format absolute dates (using the [object Object] token) in gutter blame annotations. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats

[object Object]

Specifies the format of the gutter blame annotations. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object] — commit id
[object Object] — commit author
[object Object] — commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object] — formatted commit date (format specified by [object Object])
[object Object] — commit date specified by [object Object]
[object Object] — commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies whether to provide a heatmap indicator in the gutter blame annotations

[object Object]

Specifies where the heatmap indicators will be shown in the gutter blame annotations

[object Object] - adds a heatmap indicator on the left edge of the gutter blame annotations

[object Object] - adds a heatmap indicator on the right edge of the gutter blame annotations

[object Object]
Specifies whether to highlight lines associated with the current line
[object Object]
Specifies where the associated line highlights will be shown

[object Object] - adds a gutter glyph
[object Object] - adds a full-line highlight background color
[object Object] - adds a decoration to the overview ruler (scroll bar)
[object Object]

Specifies whether to ignore whitespace when comparing revisions during blame operations

[object Object]
Specifies whether gutter blame annotations will have line separators
[object Object]
Specifies how the gutter blame annotations will be toggled

[object Object] - toggles each file individually
[object Object] - toggles the window, i.e. all files at once

### Hover Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#hover-settings-)Name

Description
[object Object]

Specifies whether to provide a *changes (diff)* hover for all lines when showing blame annotations

[object Object]

Specifies whether to provide a *commit details* hover for all lines when showing blame annotations

[object Object]
Specifies whether to provide any hovers when showing blame annotations
[object Object]
Specifies when to trigger hovers when showing blame annotations

[object Object] - only shown when hovering over the line annotation
[object Object] - shown when hovering anywhere over the line
[object Object]
Specifies whether to show avatar images in hovers
[object Object]
Specifies whether to provide a *changes (diff)* hover for the current line
[object Object]
Specifies whether to provide a *commit details* hover for the current line
[object Object]
Specifies whether to provide any hovers for the current line
[object Object]
Specifies when to trigger hovers for the current line

[object Object] - only shown when hovering over the line annotation
[object Object] - shown when hovering anywhere over the line
[object Object]
Specifies whether to provide any hovers

### Code Lens Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#code-lens-settings-)Name

Description
[object Object]
Specifies the command to be executed when an *authors* code lens is clicked

[object Object] - toggles file blame annotations
[object Object] - compares the current committed file with the previous commit
[object Object] - shows a commit details quick pick
[object Object] - shows a commit file details quick pick
[object Object] - shows a file history quick pick
[object Object] - shows a branch history quick pick
[object Object]

Specifies whether to provide an *authors* code lens, showing number of authors of the file or code block and the most prominent author (if there is more than one)

[object Object]

Specifies whether to provide any Git code lens, by default. Use the *Toggle Git Code Lens* command ([object Object]) to toggle the Git code lens on and off for the current window

[object Object]

Specifies whether to provide any Git code lens on symbols that span only a single line

[object Object]

Specifies the command to be executed when a *recent change* code lens is clicked

[object Object] - toggles file blame annotations
[object Object] - compares the current committed file with the previous commit
[object Object] - shows a commit details quick pick
[object Object] - shows a commit file details quick pick
[object Object] - shows a file history quick pick
[object Object] - shows a branch history quick pick
[object Object]

Specifies whether to provide a *recent change* code lens, showing the author and date of the most recent commit for the file or code block

[object Object]
Specifies where Git code lens will be shown in the document

[object Object] - adds code lens at the top of the document

[object Object] - adds code lens at the start of container-like symbols (modules, classes, interfaces, etc)

[object Object] - adds code lens at the start of block-like symbols (functions, methods, etc) lines

[object Object]

Specifies where Git code lens will be shown in the document for the specified languages

[object Object]

Specifies a set of document symbols where Git code lens will or will not be shown in the document. Prefix with [object Object] to avoid providing a Git code lens for the symbol. Must be a member of [[object Object]](https://code.visualstudio.com/docs/extensionAPI/vscode-api#_a-namesymbolkindaspan-classcodeitem-id660symbolkindspan)

### Gutter Heatmap Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#gutter-heatmap-settings-)Name

Description
[object Object]

Specifies the age of the most recent change (in days) after which the gutter heatmap annotations will be cold rather than hot (i.e. will use [object Object] instead of [object Object])

[object Object]

Specifies the base color of the gutter heatmap annotations when the most recent change is older (cold) than the [object Object] value

[object Object]

Specifies the base color of the gutter heatmap annotations when the most recent change is newer (hot) than the [object Object] value

[object Object]
Specifies how the gutter heatmap annotations will be toggled

[object Object] - toggles each file individually
[object Object] - toggles the window, i.e. all files at once

### Recent Changes Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#recent-changes-settings-)Name

Description
[object Object]
Specifies where the highlights of the recently changed lines will be shown

[object Object] - adds a gutter glyph
[object Object] - adds a full-line highlight background color
[object Object] - adds a decoration to the overview ruler (scroll bar)
[object Object]
Specifies how the recently changed lines annotations will be toggled

[object Object] - toggles each file individually
[object Object] - toggles the window, i.e. all files at once

### Status Bar Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#status-bar-settings-)Name

Description
[object Object]
Specifies the blame alignment in the status bar

[object Object] - aligns to the left
[object Object] - aligns to the right
[object Object]
Specifies the command to be executed when the blame status bar item is clicked

[object Object] - toggles file blame annotations
[object Object] - compares the current line commit with the previous
[object Object] - compares the current line commit with the working tree
[object Object] - toggles Git code lens
[object Object] - shows a commit details quick pick
[object Object] - shows a commit file details quick pick
[object Object] - shows a file history quick pick
[object Object] - shows a branch history quick pick
[object Object]

Specifies the date format of absolute dates shown in the blame information in the status bar. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats

[object Object]
Specifies whether to provide blame information in the status bar
[object Object]

Specifies the format of the blame information in the status bar. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object] — commit id
[object Object] — commit author
[object Object] — commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object] — formatted commit date (format specified by [object Object])
[object Object] — commit date specified by [object Object]
[object Object] — commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies whether to avoid clearing the previous blame information when changing lines to reduce status bar "flashing"

### Repositories View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#repositories-view-settings-)

See also [View Settings](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]

Specifies whether to show avatar images instead of commit (or status) icons in the *Repositories* view

[object Object]

Specifies whether to automatically refresh the *Repositories* view when the repository or the file system changes

[object Object]

Specifies whether to automatically reveal repositories in the *Repositories* view when opening files

[object Object]
Specifies how the *Repositories* view will display branches

[object Object] - displays branches as a list

[object Object] - displays branches as a tree when branch names contain slashes [object Object]

[object Object]
Specifies whether to show the *Repositories* view in a compact display density
[object Object]
Specifies whether to show the *Repositories* view
[object Object]

Specifies whether to compact (flatten) unnecessary file nesting in the *Repositories* view. Only applies when [object Object] is set to [object Object] or [object Object]

[object Object]
Specifies how the *Repositories* view will display files

[object Object] - automatically switches between displaying files as a [object Object] or [object Object] based on the [object Object] value and the number of files at each nesting level

[object Object] - displays files as a list
[object Object] - displays files as a tree
[object Object]

Specifies when to switch between displaying files as a [object Object] or [object Object] based on the number of files in a nesting level in the *Repositories* view. Only applies when [object Object] is set to [object Object]

[object Object]

Specifies whether to include working tree file status for each repository in the *Repositories* view

[object Object]
Specifies where to show the *Repositories* view

[object Object] - adds to the GitLens side bar
[object Object] - adds to the Explorer side bar
[object Object] - adds to the Source Control side bar
[object Object]

Specifies whether to show the tracking branch when displaying local branches in the *Repositories* view

### File History View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#file-history-view-settings-)

See also [View Settings](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]

Specifies whether to show avatar images instead of status icons in the *File History* view

[object Object]
Specifies whether to show the *File History* view
[object Object]
Specifies where to show the *File History* view

[object Object] - adds to the GitLens side bar
[object Object] - adds to the Explorer side bar
[object Object] - adds to the Source Control side bar

### Line History View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#line-history-view-settings-)

See also [View Settings](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]

Specifies whether to show avatar images instead of status icons in the *Line History* view

[object Object]
Specifies whether to show the *Line History* view
[object Object]
Specifies where to show the *Line History* view

[object Object] - adds to the GitLens side bar
[object Object] - adds to the Explorer side bar
[object Object] - adds to the Source Control side bar

### Search View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#search-view-settings-)

See also [View Settings](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]

Specifies whether to show avatar images instead of commit (or status) icons in the *Search Commits* view

[object Object]

Specifies whether to compact (flatten) unnecessary file nesting in the *Search Commits* view

Only applies when [object Object] is set to [object Object] or [object Object]
[object Object]
Specifies whether to show the *Search Commits* view
[object Object]
Specifies how the *Search Commits* view will display files

[object Object] - automatically switches between displaying files as a [object Object] or [object Object] based on the [object Object] value and the number of files at each nesting level

[object Object] - displays files as a list
[object Object] - displays files as a tree
[object Object]

Specifies when to switch between displaying files as a [object Object] or [object Object] based on the number of files in a nesting level in the *Search Commits* view

Only applies when [object Object] is set to [object Object]
[object Object]
Specifies where to show the *Search Commits* view
[object Object] - adds to the GitLens side bar
[object Object] - adds to the Explorer side bar
[object Object] - adds to the Source Control side bar

### Compare View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#compare-view-settings-)

See also [View Settings](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]

Specifies whether to show avatar images instead of commit (or status) icons in the *Compare* view

[object Object]

Specifies whether to compact (flatten) unnecessary file nesting in the *Compare* view. Only applies when [object Object] is set to [object Object] or [object Object]

[object Object]
Specifies whether to show the *Compare* view
[object Object]
Specifies how the *Compare* view will display files

[object Object] - automatically switches between displaying files as a [object Object] or [object Object] based on the [object Object] value and the number of files at each nesting level

[object Object] - displays files as a list
[object Object] - displays files as a tree
[object Object]

Specifies when to switch between displaying files as a [object Object] or [object Object] based on the number of files in a nesting level in the *Compare* view. Only applies when [object Object] is set to [object Object]

[object Object]
Specifies where to show the *Compare* view

[object Object] - adds to the GitLens side bar
[object Object] - adds to the Explorer side bar
[object Object] - adds to the Source Control side bar

### View Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#view-settings-)Name

Description
[object Object]
Specifies the format of a committed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object]
Specifies the description format of a committed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object]

Specifies the format of committed changes in the views. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object]— commit id
[object Object] — commit author
[object Object]— commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object]— formatted commit date (format specified by[object Object])
[object Object] — commit date specified by [object Object]
[object Object]— commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies the description format of committed changes in the views. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object]— commit id
[object Object] — commit author
[object Object]— commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object]— formatted commit date (format specified by[object Object])
[object Object] — commit date specified by [object Object]
[object Object]— commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies the default number of items to show in a view list. Use 0 to specify no limit

[object Object]

Specifies whether to show relative date markers (*Less than a week ago*, *Over a week ago*, *Over a month ago*, etc) on revision (commit) histories in the views

[object Object]
Specifies the format of a stashed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object]
Specifies the description format of a stashed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object]

Specifies the format of stashed changes in the views. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object] — commit id
[object Object] — commit author
[object Object] — commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object]— formatted commit date (format specified by [object Object])
[object Object] — commit date specified by [object Object]
[object Object] — commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]

Specifies the description format of stashed changes in the views. See the [GitLens docs](https://github.com/eamodio/vscode-gitlens/wiki/Advanced-Formatting) for advanced formatting

Available tokens
[object Object] — commit id
[object Object] — commit author
[object Object] — commit message
[object Object] — relative commit date (e.g. 1 day ago)
[object Object]— formatted commit date (format specified by [object Object])
[object Object] — commit date specified by [object Object]
[object Object] — commit author, relative commit date
[object Object] — commit author, commit date specified by [object Object]
[object Object]
Specifies the format of the status of a working or committed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object] — optional indicator if the file is uncommitted
[object Object]

Specifies the description format of the status of a working or committed file in the views

Available tokens
[object Object] — directory name
[object Object] — file name
[object Object] — formatted file name and path
[object Object] — full file path
[object Object] — optional indicator if the file is uncommitted

### Modes Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#modes-settings-)Name

Description
[object Object]
Specifies the active GitLens mode, if any
[object Object]
Specifies whether to provide the active GitLens mode in the status bar
[object Object]
Specifies the active GitLens mode alignment in the status bar

[object Object] - aligns to the left
[object Object] - aligns to the right
[object Object]
Specifies the user-defined GitLens modes

Example — adds heatmap annotations to the built-in *Reviewing* mode
[object Object]

Example — adds a new *Annotating* mode with blame annotations
[object Object]
    [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
    [object Object]
[object Object]

### Advanced Settings [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#advanced-settings-)Name

Description
[object Object]
Specifies the length of abbreviated commit ids (shas)
[object Object]
Specifies additional arguments to pass to the [object Object] command
[object Object]

Specifies the time (in milliseconds) to wait before re-blaming an unsaved document after an edit. Use 0 to specify an infinite wait

[object Object]

Specifies the maximum document size (in lines) allowed to be re-blamed after an edit while still unsaved. Use 0 to specify no maximum

[object Object]

Specifies whether git output will be cached — changing the default is not recommended

[object Object]

Specifies whether file histories will follow renames -- will affect how merge commits are shown in histories

[object Object]

Specifies the maximum number of items to show in a list. Use 0 to specify no maximum

[object Object]
Specifies which messages should be suppressed
[object Object]
Specifies whether to close QuickPick menus when focus is lost
[object Object]
Specifies how many folders deep to search for repositories
[object Object]

Specifies whether to enable GitLens telemetry (even if enabled still abides by the overall [object Object] setting

#### Custom Remotes SettingsName

Description
[object Object]

Specifies user-defined remote (code-hosting) services or custom domains for built-in remote services

Example:
[object Object]

Example:
[object Object]
    [object Object]
    [object Object]
    [object Object]
    [object Object]
    [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
    [object Object]

Example:
[object Object]
    [object Object]
    [object Object]
    [object Object]
    [object Object]
    [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
        [object Object]
    [object Object]

#### Strings SettingsName

Description
[object Object]

Specifies the string to be shown in place of both the *recent change* and *authors* code lens when there are unsaved changes

[object Object]

Specifies the string to be shown in place of the *recent change* code lens when there are unsaved changes

[object Object]

Specifies the string to be shown in place of the *authors* code lens when there are unsaved changes

* * *

## Themable Colors [#](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#themable-colors-)

GitLens defines a set of themable colors which can be provided by vscode themes or directly by the user using [[object Object]](https://code.visualstudio.com/docs/getstarted/themes#_customize-a-color-theme).Name

Description
[object Object]
Specifies the background color of the gutter blame annotations
[object Object]
Specifies the foreground color of the gutter blame annotations
[object Object]

Specifies the foreground color of an uncommitted line in the gutter blame annotations

[object Object]
Specifies the background color of the trailing blame annotation
[object Object]
Specifies the foreground color of the trailing blame annotation
[object Object]

Specifies the background color of the associated line highlights in blame annotations

[object Object]

Specifies the overview ruler color of the associated line highlights in blame annotations

* * *

## Insiders

Add [[object Object]](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens#general-settings-) to your settings to join the insiders channel and get early access to upcoming features. Be aware that because this provides early access expect there to be issues.

* * *

## Contributors ❤

A big thanks to the people that have contributed to this project:

- Loris Bettazza ([@Pustur](https://github.com/Pustur)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=Pustur)
- Tony Brix ([@UziTech](https://github.com/UziTech)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=UziTech)
- Amanda Cameron ([@AmandaCameron](https://github.com/AmandaCameron)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=AmandaCameron)
- Brett Cannon ([@brettcannon](https://github.com/brettcannon)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=brettcannon)
- Ash Clarke ([@ashclarke](https://github.com/ashclarke)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=ashclarke)
- Matt Cooper ([@vtbassmatt](https://github.com/vtbassmatt)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=vtbassmatt)
- Segev Finer ([@segevfiner](https://github.com/segevfiner)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=segevfiner)
- Cory Forsyth ([@bantic](https://github.com/bantic)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=bantic)
- Geoffrey ([@g3offrey](https://github.com/g3offrey)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=g3offrey)
- Yukai Huang ([@Yukaii](https://github.com/Yukaii)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=Yukaii)
- Roy Ivy III ([@rivy](https://github.com/rivy)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=rivy)
- Helmut Januschka ([@hjanuschka](https://github.com/hjanuschka)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=hjanuschka)
- Chris Kaczor ([@ckaczor](https://github.com/ckaczor)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=ckaczor)
- Andrei Korigodski ([@korigod](https://github.com/korigod)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=korigod)
- Peng Lyu ([@rebornix](https://github.com/rebornix)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=rebornix)
- Cédric Malard ([@cmalard](https://github.com/cmalard)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=cmalard)
- Aurelio Ogliari ([@nobitagit](https://github.com/nobitagit)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=nobitagit)
- Maxim Pekurin ([@pmaxim25](https://github.com/pmaxim25)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=pmaxim25)
- Johannes Rieken ([@jrieken](https://github.com/jrieken)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=jrieken)
- ryenus ([@ryenus](https://github.com/ryenus)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=ryenus)
- Zack Schuster ([@zackschuster](https://github.com/zackschuster)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=zackschuster)
- sgtwilko ([@sgtwilko](https://github.com/sgtwilko)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=sgtwilko)
- SpaceEEC ([@SpaceEEC](https://github.com/SpaceEEC)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=SpaceEEC)
- Skybbles // L5474 ([@Luxray5474](https://github.com/Luxray5474)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=Luxray5474)
- Alexey Vasyukov ([@notmedia](https://github.com/notmedia)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=notmedia)
- Zyck ([@qzyse2017](https://github.com/qzyse2017)) — [contributions](https://github.com/eamodio/vscode-gitlens/commits?author=qzyse2017)

Also special thanks to the people that have provided support, testing, brainstorming, etc:

- Brian Canzanella ([@bcanzanella](https://github.com/bcanzanella))
- Matt King ([@KattMingMing](https://github.com/KattMingMing))

And of course the awesome [vscode](https://github.com/Microsoft/vscode/graphs/contributors) team!