k88hudson/git-flight-rules

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='471'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2069' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#flight-rules-for-git)Flight rules for Git

*[English](https://github.com/k88hudson/git-flight-rules/blob/master/README.md) ∙ [Español](https://github.com/k88hudson/git-flight-rules/blob/master/README_es.md) ∙ [Русский](https://github.com/k88hudson/git-flight-rules/blob/master/README_ru.md) ∙ [简体中文](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)∙ [한국어](https://github.com/k88hudson/git-flight-rules/blob/master/README_kr.md) ∙ [Tiếng Việt](https://github.com/k88hudson/git-flight-rules/blob/master/README_vi.md) ∙ [Français](https://github.com/k88hudson/git-flight-rules/blob/master/README_fr.md)*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='472'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2074' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#what-are-flight-rules)What are "flight rules"?

A guide for astronauts (now, programmers using Git) about what to do when things go wrong.

*> Flight Rules*>  are the hard-earned body of knowledge recorded in manuals that list, step-by-step, what to do if X occurs, and why. Essentially, they are extremely detailed, scenario-specific standard operating procedures. [...]

> NASA has been capturing our missteps, disasters and solutions since the early 1960s, when Mercury-era ground teams first started gathering "lessons learned" into a compendium that now lists thousands of problematic situations, from engine failure to busted hatch handles to computer glitches, and their solutions.

— Chris Hadfield, *An Astronaut's Guide to Life*.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='473'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2084' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#conventions-for-this-document)Conventions for this document

For clarity's sake all examples in this document use a customized bash prompt in order to indicate the current branch and whether or not there are staged changes. The branch is enclosed in parentheses, and a `*` next to the branch name indicates staged changes.

All commands should work for at least git version 2.13.0. See the [git website](https://www.git-scm.com/) to update your local git version.

[![68747470733a2f2f6261646765732e6769747465722e696d2f4a6f696e253230436861742e737667](../_resources/aae07787bebc237857279890e95659ca.png)](https://gitter.im/k88hudson/git-flight-rules?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Repositories](https://github.com/k88hudson/git-flight-rules#repositories)
    - [I want to start a local repository](https://github.com/k88hudson/git-flight-rules#i-want-to-start-a-local-repository)
    - [I want to clone a remote repository](https://github.com/k88hudson/git-flight-rules#i-want-to-clone-a-remote-repository)
    - [I set the wrong remote repository](https://github.com/k88hudson/git-flight-rules#i-set-the-wrong-remote-repository)
    - [I want to add code to someone else's repository](https://github.com/k88hudson/git-flight-rules#i-want-to-add-code-to-someone-elses-repository)
        - [Suggesting code via pull requests](https://github.com/k88hudson/git-flight-rules#suggesting-code-via-pull-requests)
        - [I need to update my fork with latest updates from the original repository](https://github.com/k88hudson/git-flight-rules#i-need-to-update-my-fork-with-latest-updates-from-the-original-repository)
- [Editing Commits](https://github.com/k88hudson/git-flight-rules#editing-commits)
    - [What did I just commit?](https://github.com/k88hudson/git-flight-rules#what-did-i-just-commit)
    - [I wrote the wrong thing in a commit message](https://github.com/k88hudson/git-flight-rules#i-wrote-the-wrong-thing-in-a-commit-message)
    - [I committed with the wrong name and email configured](https://github.com/k88hudson/git-flight-rules#i-committed-with-the-wrong-name-and-email-configured)
    - [I want to remove a file from the previous commit](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-file-from-the-previous-commit)
    - [I want to delete or remove my last commit](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-or-remove-my-last-commit)
    - [Delete/remove arbitrary commit](https://github.com/k88hudson/git-flight-rules#deleteremove-arbitrary-commit)
    - [I tried to push my amended commit to a remote, but I got an error message](https://github.com/k88hudson/git-flight-rules#i-tried-to-push-my-amended-commit-to-a-remote-but-i-got-an-error-message)
    - [I accidentally did a hard reset, and I want my changes back](https://github.com/k88hudson/git-flight-rules#i-accidentally-did-a-hard-reset-and-i-want-my-changes-back)
    - [I accidentally committed and pushed a merge](https://github.com/k88hudson/git-flight-rules#i-accidentally-committed-and-pushed-a-merge)
    - [I accidentally committed and pushed files containing sensitive data](https://github.com/k88hudson/git-flight-rules#i-accidentally-committed-and-pushed-files-containing-sensitive-data)
    - [I want to remove a large file from ever existing in repo history](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-large-file-from-ever-existing-in-repo-history)
        - [Recommended Technique: Use third-party bfg](https://github.com/k88hudson/git-flight-rules#recommended-technique-use-third-party-bfg)
        - [Built-in Technique: Use git-filter-branch](https://github.com/k88hudson/git-flight-rules#built-in-technique-use-git-filter-branch)
        - [Final Step: Pushing your changed repo history](https://github.com/k88hudson/git-flight-rules#final-step-pushing-your-changed-repo-history)
    - [I need to change the content of a commit which is not my last](https://github.com/k88hudson/git-flight-rules#i-need-to-change-the-content-of-a-commit-which-is-not-my-last)
- [Staging](https://github.com/k88hudson/git-flight-rules#staging)
    - [I need to add staged changes to the previous commit](https://github.com/k88hudson/git-flight-rules#i-need-to-add-staged-changes-to-the-previous-commit)
    - [I want to stage part of a new file, but not the whole file](https://github.com/k88hudson/git-flight-rules#i-want-to-stage-part-of-a-new-file-but-not-the-whole-file)
    - [I want to add changes in one file to two different commits](https://github.com/k88hudson/git-flight-rules#i-want-to-add-changes-in-one-file-to-two-different-commits)
    - [I staged too many edits, and I want to break them out into a separate commit](https://github.com/k88hudson/git-flight-rules#i-staged-too-many-edits-and-i-want-to-break-them-out-into-a-separate-commit)
    - [I want to stage my unstaged edits, and unstage my staged edits](https://github.com/k88hudson/git-flight-rules#i-want-to-stage-my-unstaged-edits-and-unstage-my-staged-edits)
- [Unstaged Edits](https://github.com/k88hudson/git-flight-rules#unstaged-edits)
    - [I want to move my unstaged edits to a new branch](https://github.com/k88hudson/git-flight-rules#i-want-to-move-my-unstaged-edits-to-a-new-branch)
    - [I want to move my unstaged edits to a different, existing branch](https://github.com/k88hudson/git-flight-rules#i-want-to-move-my-unstaged-edits-to-a-different-existing-branch)
    - [I want to discard my local uncommitted changes (staged and unstaged)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-my-local-uncommitted-changes-staged-and-unstaged)
    - [I want to discard specific unstaged changes](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-specific-unstaged-changes)
    - [I want to discard specific unstaged files](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-specific-unstaged-files)
    - [I want to discard only my unstaged local changes](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-only-my-unstaged-local-changes)
    - [I want to discard all of my untracked files](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-all-of-my-untracked-files)
    - [I want to unstage a specific staged file](https://github.com/k88hudson/git-flight-rules#i-want-to-unstage-a-specific-staged-file)
- [Branches](https://github.com/k88hudson/git-flight-rules#branches)
    - [I want to list all branches](https://github.com/k88hudson/git-flight-rules#i-want-to-list-all-branches)
    - [Create a branch from a commit](https://github.com/k88hudson/git-flight-rules#create-a-branch-from-a-commit)
    - [I pulled from/into the wrong branch](https://github.com/k88hudson/git-flight-rules#i-pulled-frominto-the-wrong-branch)
    - [I want to discard local commits so my branch is the same as one on the server](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-local-commits-so-my-branch-is-the-same-as-one-on-the-server)
    - [I committed to master instead of a new branch](https://github.com/k88hudson/git-flight-rules#i-committed-to-master-instead-of-a-new-branch)
    - [I want to keep the whole file from another ref-ish](https://github.com/k88hudson/git-flight-rules#i-want-to-keep-the-whole-file-from-another-ref-ish)
    - [I made several commits on a single branch that should be on different branches](https://github.com/k88hudson/git-flight-rules#i-made-several-commits-on-a-single-branch-that-should-be-on-different-branches)
    - [I want to delete local branches that were deleted upstream](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-local-branches-that-were-deleted-upstream)
    - [I accidentally deleted my branch](https://github.com/k88hudson/git-flight-rules#i-accidentally-deleted-my-branch)
    - [I want to delete a branch](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-a-branch)
    - [I want to delete multiple branches](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-multiple-branches)
    - [I want to rename a branch](https://github.com/k88hudson/git-flight-rules#i-want-to-rename-a-branch)
    - [I want to checkout to a remote branch that someone else is working on](https://github.com/k88hudson/git-flight-rules#i-want-to-checkout-to-a-remote-branch-that-someone-else-is-working-on)
    - [I want to create a new remote branch from current local one](https://github.com/k88hudson/git-flight-rules#i-want-to-create-a-new-remote-branch-from-current-local-one)
    - [I want to set a remote branch as the upstream for a local branch](https://github.com/k88hudson/git-flight-rules#i-want-to-set-a-remote-branch-as-the-upstream-for-a-local-branch)
    - [I want to set my HEAD to track the default remote branch](https://github.com/k88hudson/git-flight-rules#i-want-to-set-my-head-to-track-the-default-remote-branch)
    - [I made changes on the wrong branch](https://github.com/k88hudson/git-flight-rules#i-made-changes-on-the-wrong-branch)
- [Rebasing and Merging](https://github.com/k88hudson/git-flight-rules#rebasing-and-merging)
    - [I want to undo rebase/merge](https://github.com/k88hudson/git-flight-rules#i-want-to-undo-rebasemerge)
    - [I rebased, but I don't want to force push](https://github.com/k88hudson/git-flight-rules#i-rebased-but-i-dont-want-to-force-push)
    - [I need to combine commits](https://github.com/k88hudson/git-flight-rules#i-need-to-combine-commits)
        - [Safe merging strategy](https://github.com/k88hudson/git-flight-rules#safe-merging-strategy)
        - [I need to merge a branch into a single commit](https://github.com/k88hudson/git-flight-rules#i-need-to-merge-a-branch-into-a-single-commit)
        - [I want to combine only unpushed commits](https://github.com/k88hudson/git-flight-rules#i-want-to-combine-only-unpushed-commits)
        - [I need to abort the merge](https://github.com/k88hudson/git-flight-rules#i-need-to-abort-the-merge)
    - [I need to update the parent commit of my branch](https://github.com/k88hudson/git-flight-rules#i-need-to-update-the-parent-commit-of-my-branch)
    - [Check if all commits on a branch are merged](https://github.com/k88hudson/git-flight-rules#check-if-all-commits-on-a-branch-are-merged)
    - [Possible issues with interactive rebases](https://github.com/k88hudson/git-flight-rules#possible-issues-with-interactive-rebases)
        - [The rebase editing screen says 'noop'](https://github.com/k88hudson/git-flight-rules#the-rebase-editing-screen-says-noop)
        - [There were conflicts](https://github.com/k88hudson/git-flight-rules#there-were-conflicts)
- [Stash](https://github.com/k88hudson/git-flight-rules#stash)
    - [Stash all edits](https://github.com/k88hudson/git-flight-rules#stash-all-edits)
    - [Stash specific files](https://github.com/k88hudson/git-flight-rules#stash-specific-files)
    - [Stash with message](https://github.com/k88hudson/git-flight-rules#stash-with-message)
    - [Apply a specific stash from list](https://github.com/k88hudson/git-flight-rules#apply-a-specific-stash-from-list)
- [Finding](https://github.com/k88hudson/git-flight-rules#finding)
    - [I want to find a string in any commit](https://github.com/k88hudson/git-flight-rules#i-want-to-find-a-string-in-any-commit)
    - [I want to find by author/committer](https://github.com/k88hudson/git-flight-rules#i-want-to-find-by-authorcommitter)
    - [I want to list commits containing specific files](https://github.com/k88hudson/git-flight-rules#i-want-to-list-commits-containing-specific-files)
    - [I want to view the commit history for a specific function](https://github.com/k88hudson/git-flight-rules#i-want-to-view-the-commit-history-for-a-specific-function)
    - [Find a tag where a commit is referenced](https://github.com/k88hudson/git-flight-rules#find-a-tag-where-a-commit-is-referenced)
- [Submodules](https://github.com/k88hudson/git-flight-rules#submodules)
    - [Clone all submodules](https://github.com/k88hudson/git-flight-rules#clone-all-submodules)
    - [Remove a submodule](https://github.com/k88hudson/git-flight-rules#remove-a-submodule)
- [Miscellaneous Objects](https://github.com/k88hudson/git-flight-rules#miscellaneous-objects)
    - [Restore a deleted file](https://github.com/k88hudson/git-flight-rules#restore-a-deleted-file)
    - [Delete tag](https://github.com/k88hudson/git-flight-rules#delete-tag)
    - [Recover a deleted tag](https://github.com/k88hudson/git-flight-rules#recover-a-deleted-tag)
    - [Deleted Patch](https://github.com/k88hudson/git-flight-rules#deleted-patch)
    - [Exporting a repository as a Zip file](https://github.com/k88hudson/git-flight-rules#exporting-a-repository-as-a-zip-file)
    - [Push a branch and a tag that have the same name](https://github.com/k88hudson/git-flight-rules#push-a-branch-and-a-tag-that-have-the-same-name)
- [Tracking Files](https://github.com/k88hudson/git-flight-rules#tracking-files)
    - [I want to change a file name's capitalization, without changing the contents of the file](https://github.com/k88hudson/git-flight-rules#i-want-to-change-a-file-names-capitalization-without-changing-the-contents-of-the-file)
    - [I want to overwrite local files when doing a git pull](https://github.com/k88hudson/git-flight-rules#i-want-to-overwrite-local-files-when-doing-a-git-pull)
    - [I want to remove a file from Git but keep the file](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-file-from-git-but-keep-the-file)
    - [I want to revert a file to a specific revision](https://github.com/k88hudson/git-flight-rules#i-want-to-revert-a-file-to-a-specific-revision)
    - [I want to list changes of a specific file between commits or branches](https://github.com/k88hudson/git-flight-rules#i-want-to-list-changes-of-a-specific-file-between-commits-or-branches)
    - [I want Git to ignore changes to a specific file](https://github.com/k88hudson/git-flight-rules#i-want-git-to-ignore-changes-to-a-specific-file)
- [Debugging with Git](https://github.com/k88hudson/git-flight-rules#debugging-with-git)
- [Configuration](https://github.com/k88hudson/git-flight-rules#configuration)
    - [I want to add aliases for some Git commands](https://github.com/k88hudson/git-flight-rules#i-want-to-add-aliases-for-some-git-commands)
    - [I want to add an empty directory to my repository](https://github.com/k88hudson/git-flight-rules#i-want-to-add-an-empty-directory-to-my-repository)
    - [I want to cache a username and password for a repository](https://github.com/k88hudson/git-flight-rules#i-want-to-cache-a-username-and-password-for-a-repository)
    - [I want to make Git ignore permissions and filemode changes](https://github.com/k88hudson/git-flight-rules#i-want-to-make-git-ignore-permissions-and-filemode-changes)
    - [I want to set a global user](https://github.com/k88hudson/git-flight-rules#i-want-to-set-a-global-user)
    - [I want to add command line coloring for Git](https://github.com/k88hudson/git-flight-rules#i-want-to-add-command-line-coloring-for-git)
- [I've no idea what I did wrong](https://github.com/k88hudson/git-flight-rules#ive-no-idea-what-i-did-wrong)
- [Git Shortcuts](https://github.com/k88hudson/git-flight-rules#git-shortcuts)
    - [Git Bash](https://github.com/k88hudson/git-flight-rules#git-bash)
    - [PowerShell on Windows](https://github.com/k88hudson/git-flight-rules#powershell-on-windows)
- [Other Resources](https://github.com/k88hudson/git-flight-rules#other-resources)
    - [Books](https://github.com/k88hudson/git-flight-rules#books)
    - [Tutorials](https://github.com/k88hudson/git-flight-rules#tutorials)
    - [Scripts and Tools](https://github.com/k88hudson/git-flight-rules#scripts-and-tools)
    - [GUI Clients](https://github.com/k88hudson/git-flight-rules#gui-clients)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='474'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2224' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#repositories)Repositories

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='475'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2226' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-start-a-local-repository)I want to start a local repository

To initialize an existing directory as a Git repository:
(my-folder) $ git init

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='476'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2230' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-clone-a-remote-repository)I want to clone a remote repository

To clone (copy) a remote repository, copy the URL for the repository, and run:
$ git clone [url]

This will save it to a folder named the same as the remote repository's. Make sure you have a connection to the remote server you are cloning from (for most purposes this means making sure you are connected to the internet).

To clone it into a folder with a different name than the default repository name:

$ git clone [url] name-of-new-folder

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='477'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2237' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-set-the-wrong-remote-repository)I set the wrong remote repository

There are a few possible problems here:

If you cloned the wrong repository, simply delete the directory created after running `git clone` and clone the correct repository.

If you set the wrong repository as the origin of an existing local repository, change the URL of your origin by running:

$ git remote set-url origin [url of the actual repo]

For more, see [this StackOverflow topic](https://stackoverflow.com/questions/2432764/how-to-change-the-uri-url-for-a-remote-git-repository#2432799).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='478'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2244' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-add-code-to-someone-elses-repository)I want to add code to someone else's repository

Git doesn't allow you to add code to someone else's repository without access rights. Neither does GitHub, which is not the same as Git, but rather a hosted service for Git repositories. However, you can suggest code using patches, or, on GitHub, forks and pull requests.

First, a bit about forking. A fork is a copy of a repository. It is not a git operation, but is a common action on GitHub, Bitbucket, GitLab — or anywhere people host Git repositories. You can fork a repository through the hosted UI.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='479'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2248' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#suggesting-code-via-pull-requests)Suggesting code via pull requests

After you've forked a repository, you normally need to clone the repository to your machine. You can do some small edits on GitHub, for instance, without cloning, but this isn't a github-flight-rules list, so let's go with how to do this locally.

# if you are using ssh$ git clone git@github.com:k88hudson/git-flight-rules.git# if you are using https$ git clone https://github.com/k88hudson/git-flight-rules.git

If you `cd` into the resulting directory, and type `git remote`, you'll see a list of the remotes. Normally there will be one remote - `origin` - which will point to `k88hudson/git-flight-rules`. In this case, we also want a remote that will point to your fork.

First, to follow a Git convention, we normally use the remote name `origin` for your own repository and `upstream` for whatever you've forked. So, rename the `origin` remote to `upstream`

$ git remote rename origin upstream

You can also do this using `git remote set-url`, but it takes longer and is more steps.

Then, set up a new remote that points to your project.
$ git remote add origin git@github.com:YourName/git-flight-rules.git
Note that now you have two remotes.

- `origin` references your own repository.
- `upstream` references the original one.

From origin, you can read and write. From upstream, you can only read.

When you've finished making whatever changes you like, push your changes (normally in a branch) to the remote named `origin`. If you're on a branch, you could use `--set-upstream` to avoid specifying the remote tracking branch on every future push using this branch. For instance:

$ (feature/my-feature) git push --set-upstream origin feature/my-feature

There is no way to suggest a pull request using the CLI using Git (although there are tools, like [hub](http://github.com/github/hub), which will do this for you). So, if you're ready to make a pull request, go to your GitHub (or another Git host) and create a new pull request. Note that your host automatically links the original and forked repositories.

After all of this, do not forget to respond to any code review feedback.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='480'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2267' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-update-my-fork-with-latest-updates-from-the-original-repository)I need to update my fork with latest updates from the original repository

After a while, the `upstream` repository may have been updated, and these updates need to be pulled into your `origin` repo. Remember that like you, other people are contributing too. Suppose that you are in your own feature branch and you need to update it with the original repository updates.

You probably have set up a remote that points to the original project. If not, do this now. Generally we use `upstream` as a remote name:

$ (master) git remote add upstream <link-to-original-repository># $ (master) git remote add upstream git@github.com:k88hudson/git-flight-rules.git

Now you can fetch from upstream and get the latest updates.
$ (master) git fetch upstream

$ (master) git merge upstream/master# or using a single command$ (master) git pull upstream master

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='481'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2274' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#editing-commits)Editing Commits

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='482'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2277' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#what-did-i-just-commit)What did I just commit?

Let's say that you just blindly committed changes with `git commit -a` and you're not sure what the actual content of the commit you just made was. You can show the latest commit on your current HEAD with:

(master)$ git show
Or
$ git log -n1 -p

If you want to see a file at a specific commit, you can also do this (where `<commitid>` is the commit you're interested in):

$ git show <commitid>:filename

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='483'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2285' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-wrote-the-wrong-thing-in-a-commit-message)I wrote the wrong thing in a commit message

If you wrote the wrong thing and the commit has not yet been pushed, you can do the following to change the commit message without changing the changes in the commit:

$ git commit --amend --only

This will open your default text editor, where you can edit the message. On the other hand, you can do this all in one command:

$ git commit --amend --only -m 'xxxxxxx'

If you have already pushed the message, you can amend the commit and force push, but this is not recommended.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='484'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2293' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-committed-with-the-wrong-name-and-email-configured)I committed with the wrong name and email configured

If it's a single commit, amend it

$ git commit --amend --no-edit --author "New Authorname <authoremail@mydomain.com>"

An alternative is to correctly configure your author settings in `git config --global author.(name|email)` and then use

$ git commit --amend --reset-author --no-edit
If you need to change all of history, see the man page for `git filter-branch`.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='485'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2300' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-file-from-the-previous-commit)I want to remove a file from the previous commit

In order to remove changes for a file from the previous commit, do the following:

$ git checkout HEAD^ myfile
$ git add myfile
$ git commit --amend --no-edit

In case the file was newly added to the commit and you want to remove it (from Git alone), do:

$ git rm --cached myfile
$ git commit --amend --no-edit

This is particularly useful when you have an open patch and you have committed an unnecessary file, and need to force push to update the patch on a remote. The `--no-edit` option is used to keep the existing commit message.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='486'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2308' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-or-remove-my-last-commit)I want to delete or remove my last commit

If you need to delete pushed commits, you can use the following. However, it will irreversibly change your history, and mess up the history of anyone else who had already pulled from the repository. In short, if you're not sure, you should never do this, ever.

$ git reset HEAD^ --hard
$ git push --force-with-lease [remote] [branch]

If you haven't pushed, to reset Git to the state it was in before you made your last commit (while keeping your staged changes):

	(my-branch*)$ git reset --soft HEAD@{1}

This only works if you haven't pushed. If you have pushed, the only truly safe thing to do is `git revert SHAofBadCommit`. That will create a new commit that undoes all the previous commit's changes. Or, if the branch you pushed to is rebase-safe (ie. other devs aren't expected to pull from it), you can just use `git push --force-with-lease`. For more, see [the above section](https://github.com/k88hudson/git-flight-rules#deleteremove-last-pushed-commit).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='487'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2315' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#deleteremove-arbitrary-commit)Delete/remove arbitrary commit

The same warning applies as above. Never do this if possible.
$ git rebase --onto SHA1_OF_BAD_COMMIT^ SHA1_OF_BAD_COMMIT
$ git push --force-with-lease [remote] [branch]

Or do an [interactive rebase](https://github.com/k88hudson/git-flight-rules#interactive-rebase) and remove the line(s) corresponding to commit(s) you want to see removed.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='488'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2321' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-tried-to-push-my-amended-commit-to-a-remote-but-i-got-an-error-message)I tried to push my amended commit to a remote, but I got an error message

To https://github.com/yourusername/repo.git! [rejected] mybranch -> mybranch (non-fast-forward)

error: failed to push some refs to 'https://github.com/tanay1337/webmaker.org.git'hint: Updates were rejected because the tip of your current branch is behind

hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards'  in  'git push --help'  for details.

Note that, as with rebasing (see below), amending **replaces the old commit with a new one**, so you must force push (`--force-with-lease`) your changes if you have already pushed the pre-amended commit to your remote. Be careful when you do this – *always* make sure you specify a branch!

(my-branch)$ git push origin mybranch --force-with-lease

In general, **avoid force pushing**. It is best to create and push a new commit rather than force-pushing the amended commit as it will cause conflicts in the source history for any other developer who has interacted with the branch in question or any child branches. `--force-with-lease` will still fail, if someone else was also working on the same branch as you, and your push would overwrite those changes.

If you are *absolutely* sure that nobody is working on the same branch or you want to update the tip of the branch *unconditionally*, you can use `--force` (`-f`), but this should be avoided in general.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/undo-git-reset-hard)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='489'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2332' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-accidentally-did-a-hard-reset-and-i-want-my-changes-back)I accidentally did a hard reset, and I want my changes back

If you accidentally do `git reset --hard`, you can normally still get your commit back, as git keeps a log of everything for a few days.

Note: This is only valid if your work is backed up, i.e., either committed or stashed. `git reset --hard`  *will remove* uncommitted modifications, so use it with caution. (A safer option is `git reset --keep`.)

(master)$ git reflog

You'll see a list of your past commits, and a commit for the reset. Choose the SHA of the commit you want to return to, and reset again:

(master)$ git reset --hard SHA1234
And you should be good to go.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/undo-a-commit-merge)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='490'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2342' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-accidentally-committed-and-pushed-a-merge)I accidentally committed and pushed a merge

If you accidentally merged a feature branch to the main development branch before it was ready to be merged, you can still undo the merge. But there's a catch: A merge commit has more than one parent (usually two).

The command to use
(feature-branch)$ git revert -m 1 <commit>

where the -m 1 option says to select parent number 1 (the branch into which the merge was made) as the parent to revert to.

Note: the parent number is not a commit identifier. Rather, a merge commit has a line `Merge: 8e2ce2d 86ac2e7`. The parent number is the 1-based index of the desired parent on this line, the first identifier is number 1, the second is number 2, and so on.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/undo-sensitive-commit-push)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='491'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2350' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-accidentally-committed-and-pushed-files-containing-sensitive-data)I accidentally committed and pushed files containing sensitive data

If you accidentally pushed files containing sensitive, or private data (passwords, keys, etc.), you can amend the previous commit. Keep in mind that once you have pushed a commit, you should consider any data it contains to be compromised. These steps can remove the sensitive data from your public repo or your local copy, but you **cannot** remove the sensitive data from other people's pulled copies. If you committed a password, **change it immediately**. If you committed a key, **re-generate it immediately**. Amending the pushed commit is not enough, since anyone could have pulled the original commit containing your sensitive data in the meantime.

If you edit the file and remove the sensitive data, then run
(feature-branch)$ git add edited_file
(feature-branch)$ git commit --amend --no-edit
(feature-branch)$ git push --force-with-lease origin [branch]
If you want to remove an entire file (but keep it locally), then run

(feature-branch)$ git rm --cached sensitive_fileecho sensitive_file >> .gitignore

(feature-branch)$ git add .gitignore
(feature-branch)$ git commit --amend --no-edit
(feature-branch)$ git push --force-with-lease origin [branch]
Alternatively store your sensitive data in local environment variables.

If you want to completely remove an entire file (and not keep it locally), then run

(feature-branch)$ git rm sensitive_file
(feature-branch)$ git commit --amend --no-edit
(feature-branch)$ git push --force-with-lease origin [branch]

If you have made other commits in the meantime (i.e. the sensitive data is in a commit before the previous commit), you will have to rebase.

[(L)](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-large-file-from-ever-existing-in-repo-history)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='492'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2362' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-large-file-from-ever-existing-in-repo-history)I want to remove a large file from ever existing in repo history

If the file you want to delete is secret or sensitive, instead see [how to remove sensitive files](https://github.com/k88hudson/git-flight-rules#i-accidentally-committed-and-pushed-files-containing-sensitive-data).

Even if you delete a large or unwanted file in a recent commit, it still exists in git history, in your repo's `.git` folder, and will make `git clone` download unneeded files.

The actions in this part of the guide will require a force push, and rewrite large sections of repo history, so if you are working with remote collaborators, check first that any local work of theirs is pushed.

There are two options for rewriting history, the built-in `git-filter-branch` or [`bfg-repo-cleaner`](https://rtyley.github.io/bfg-repo-cleaner/). `bfg` is significantly cleaner and more performant, but it is a third-party download and requires java. We will describe both alternatives. The final step is to force push your changes, which requires special consideration on top of a regular force push, given that a great deal of repo history will have been permanently changed.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='493'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2368' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#recommended-technique-use-third-party-bfg)Recommended Technique: Use third-party bfg

Using bfg-repo-cleaner requires java. Download the bfg jar from the link [here](https://rtyley.github.io/bfg-repo-cleaner/). Our examples will use `bfg.jar`, but your download may have a version number, e.g. `bfg-1.13.0.jar`.

To delete a specific file.
(master)$ git rm path/to/filetoremove

(master)$ git commit -m "Commit removing filetoremove"(master)$ java -jar ~/Downloads/bfg.jar --delete-files filetoremove

Note that in bfg you must use the plain file name even if it is in a subdirectory.

You can also delete a file by pattern, e.g.:
(master)$ git rm *.jpg

(master)$ git commit -m "Commit removing *.jpg"(master)$ java -jar ~/Downloads/bfg.jar --delete-files *.jpg

With bfg, the files that exist on your latest commit will not be affected. For example, if you had several large .tga files in your repo, and then in an earlier commit, you deleted a subset of them, this call does not touch files present in the latest commit

Note, if you renamed a file as part of a commit, e.g. if it started as `LargeFileFirstName.mp4` and a commit changed it to `LargeFileSecondName.mp4`, running `java -jar ~/Downloads/bfg.jar --delete-files LargeFileSecondName.mp4` will not remove it from git history. Either run the `--delete-files` command with both filenames, or with a matching pattern.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='494'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2378' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#built-in-technique-use-git-filter-branch)Built-in Technique: Use git-filter-branch

`git-filter-branch` is more cumbersome and has less features, but you may use it if you cannot install or run `bfg`.

In the below, replace `filepattern` may be a specific name or pattern, e.g. `*.jpg`. This will remove files matching the pattern from all history and branches.

(master)$ git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch filepattern' --prune-empty --tag-name-filter cat -- --all

Behind-the-scenes explanation:

`--tag-name-filter cat` is a cumbersome, but simplest, way to apply the original tags to the new commits, using the command cat.

`--prune-empty` removes any now-empty commits.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='495'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2386' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#final-step-pushing-your-changed-repo-history)Final Step: Pushing your changed repo history

Once you have removed your desired files, test carefully that you haven't broken anything in your repo - if you have, it is easiest to re-clone your repo to start over. To finish, optionally use git garbage collection to minimize your local .git folder size, and then force push.

(master)$ git reflog expire --expire=now --all && git gc --prune=now --aggressive

(master)$ git push origin --force --tags

Since you just rewrote the entire git repo history, the `git push` operation may be too large, and return the error `“The remote end hung up unexpectedly”`. If this happens, you can try increasing the git post buffer:

(master)$ git config http.postBuffer 524288000
(master)$ git push --force

If this does not work, you will need to manually push the repo history in chunks of commits. In the command below, try increasing `<number>` until the push operation succeeds.

(master)$ git push -u origin HEAD~<number>:refs/head/master --force

Once the push operation succeeds the first time, decrease `<number>` gradually until a conventional `git push` succeeds.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/i-need-to-change-the-content-of-a-commit-which-is-not-my-last)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='496'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2396' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-change-the-content-of-a-commit-which-is-not-my-last)I need to change the content of a commit which is not my last

Consider you created some (e.g. three) commits and later realize you missed doing something that belongs contextually into the first of those commits. This bothers you, because if you'd create a new commit containing those changes, you'd have a clean code base, but your commits weren't atomic (i.e. changes that belonged to each other weren't in the same commit). In such a situation you may want to change the commit where these changes belong to, include them and have the following commits unaltered. In such a case, `git rebase` might save you.

Consider a situation where you want to change the third last commit you made.
(your-branch)$ git rebase -i HEAD~4

gets you into interactive rebase mode, which allows you to edit any of your last three commits. A text editor pops up, showing you something like

pick 9e1d264 The third last commit
pick 4b6e19a The second to last commit
pick f4037ec The last commit
which you change into
edit 9e1d264 The third last commit
pick 4b6e19a The second to last commit
pick f4037ec The last commit

This tells rebase that you want to edit your third last commit and keep the other two unaltered. Then you'll save (and close) the editor. Git will then start to rebase. It stops on the commit you want to alter, giving you the chance to edit that commit. Now you can apply the changes which you missed applying when you initially committed that commit. You do so by editing and staging them. Afterwards you'll run

(your-branch)$ git commit --amend

which tells Git to recreate the commit, but to leave the commit message unedited. Having done that, the hard part is solved.

(your-branch)$ git rebase --continue
will do the rest of the work for you.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='497'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2410' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#staging)Staging

[(L)](https://github.com/k88hudson/git-flight-rules#i-need-to-add-staged-changes-to-the-previous-commit)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='498'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2413' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-add-staged-changes-to-the-previous-commit)I need to add staged changes to the previous commit

(my-branch*)$ git commit --amend

If you already know you don't want to change the commit message, you can tell git to reuse the commit message:

(my-branch*)$ git commit --amend -C HEAD

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='499'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2419' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-stage-part-of-a-new-file-but-not-the-whole-file)I want to stage part of a new file, but not the whole file

Normally, if you want to stage part of a file, you run this:
$ git add --patch filename.x

`-p` will work for short. This will open interactive mode. You would be able to use the `s` option to split the commit - however, if the file is new, you will not have this option. To add a new file, do this:

$ git add -N filename.x

Then, you will need to use the `e` option to manually choose which lines to add. Running `git diff --cached` or`git diff --staged` will show you which lines you have staged compared to which are still saved locally.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/stage-in-two-commits)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='500'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2427' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-add-changes-in-one-file-to-two-different-commits)I want to add changes in one file to two different commits

`git add` will add the entire file to a commit. `git add -p` will allow to interactively select which changes you want to add.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/selective-unstage-edits)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='501'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2431' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-staged-too-many-edits-and-i-want-to-break-them-out-into-a-separate-commit)I staged too many edits, and I want to break them out into a separate commit

`git reset -p` will open a patch mode reset dialog. This is similar to `git add -p`, except that selecting "yes" will unstage the change, removing it from the upcoming commit.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/unstaging-edits-and-staging-the-unstaged)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='502'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2435' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-stage-my-unstaged-edits-and-unstage-my-staged-edits)I want to stage my unstaged edits, and unstage my staged edits

This is tricky. The best I figure is that you should stash your unstaged edits. Then, reset. After that, pop your stashed edits back, and add them.

$ git stash -k
$ git reset --hard
$ git stash pop
$ git add -A

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='503'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2439' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#unstaged-edits)Unstaged Edits

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/move-unstaged-edits-to-new-branch)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='504'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2442' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-move-my-unstaged-edits-to-a-new-branch)I want to move my unstaged edits to a new branch

$ git checkout -b my-branch

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/move-unstaged-edits-to-old-branch)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='505'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2446' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-move-my-unstaged-edits-to-a-different-existing-branch)I want to move my unstaged edits to a different, existing branch

$ git stash
$ git checkout my-branch
$ git stash pop

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/i-want-to-discard-my-local-uncommitted-changes)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='506'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2450' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-my-local-uncommitted-changes-staged-and-unstaged)I want to discard my local uncommitted changes (staged and unstaged)

If you want to discard all your local staged and unstaged changes, you can do this:

(my-branch)$ git reset --hard# or(master)$ git checkout -f
This will unstage all files you might have staged with `git add`:
$ git reset

This will revert all local uncommitted changes (should be executed in repo root):

$ git checkout .
You can also revert uncommitted changes to a particular file or directory:
$ git checkout [some_dir|file.txt]

Yet another way to revert all uncommitted changes (longer to type, but works from any subdirectory):

$ git reset --hard HEAD

This will remove all local untracked files, so only files tracked by Git remain:

$ git clean -fd
`-x` will also remove all ignored files.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='507'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2465' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-specific-unstaged-changes)I want to discard specific unstaged changes

When you want to get rid of some, but not all changes in your working copy.
Checkout undesired changes, keep good changes.
$ git checkout -p# Answer y to all of the snippets you want to drop

Another strategy involves using `stash`. Stash all the good changes, reset working copy, and reapply good changes.

$ git stash -p# Select all of the snippets you want to save$ git reset --hard
$ git stash pop
Alternatively, stash your undesired changes, and then drop stash.

$ git stash -p# Select all of the snippets you don't want to save$ git stash drop

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='508'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2474' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-specific-unstaged-files)I want to discard specific unstaged files

When you want to get rid of one specific file in your working copy.
$ git checkout myFile
Alternatively, to discard multiple files in your working copy, list them all.
$ git checkout myFirstFile mySecondFile

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='509'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2480' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-only-my-unstaged-local-changes)I want to discard only my unstaged local changes

When you want to get rid of all of your unstaged local uncommitted changes
$ git checkout .

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/i-want-to-discard-all-my-untracked-files)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='510'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2485' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-all-of-my-untracked-files)I want to discard all of my untracked files

When you want to get rid of all of your untracked files
$ git clean -f

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/I-want-to-unstage-specific-staged-file)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='511'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2490' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-unstage-a-specific-staged-file)I want to unstage a specific staged file

Sometimes we have one or more files that accidentally ended up being staged, and these files have not been committed before. To unstage them:

$ git reset -- <filename>
This results in unstaging the file and make it look like it's untracked.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='512'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2495' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#branches)Branches

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='513'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2497' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-list-all-branches)I want to list all branches

List local branches
$ git branch
List remote branches
$ git branch -r
List all branches (both local and remote)
$ git branch -a

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='514'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2506' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#create-a-branch-from-a-commit)Create a branch from a commit

$ git checkout -b <branch>  <SHA1_OF_COMMIT>

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='515'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2510' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-pulled-frominto-the-wrong-branch)I pulled from/into the wrong branch

This is another chance to use `git reflog` to see where your HEAD pointed before the bad pull.

(master)$ git reflog
ab7555f HEAD@{0}: pull origin wrong-branch: Fast-forward
c5bc55a HEAD@{1}: checkout: checkout message goes here
Simply reset your branch back to the desired commit:
$ git reset --hard c5bc55a
Done.

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/discard-local-commits)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='516'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2518' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-discard-local-commits-so-my-branch-is-the-same-as-one-on-the-server)I want to discard local commits so my branch is the same as one on the server

Confirm that you haven't pushed your changes to the server.
`git status` should show how many commits you are ahead of origin:

(my-branch)$ git status# On branch my-branch# Your branch is ahead of 'origin/my-branch' by 2 commits.# (use "git push" to publish your local commits)#

One way of resetting to match origin (to have the same as what is on the remote) is to do this:

(master)$ git reset --hard origin/my-branch

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='517'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2526' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-committed-to-master-instead-of-a-new-branch)I committed to master instead of a new branch

Create the new branch while remaining on master:
(master)$ git branch my-branch
Reset the branch master to the previous commit:
(master)$ git reset --hard HEAD^

`HEAD^` is short for `HEAD^1`. This stands for the first parent of `HEAD`, similarly `HEAD^2` stands for the second parent of the commit (merges can have 2 parents).

Note that `HEAD^2` is **not** the same as `HEAD~2` (see [this link](http://www.paulboxley.com/blog/2011/06/git-caret-and-tilde) for more information).

Alternatively, if you don't want to use `HEAD^`, find out what the commit hash you want to set your master branch to (`git log` should do the trick). Then reset to that hash. `git push` will make sure that this change is reflected on your remote.

For example, if the hash of the commit that your master branch is supposed to be at is `a13b85e`:

(master)$ git reset --hard a13b85e
HEAD is now at a13b85e
Checkout the new branch to continue working:
(master)$ git checkout my-branch

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='518'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2540' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-keep-the-whole-file-from-another-ref-ish)I want to keep the whole file from another ref-ish

Say you have a working spike (see note), with hundreds of changes. Everything is working. Now, you commit into another branch to save that work:

(solution)$ git add -A && git commit -m "Adding all changes from this spike into one big commit."

When you want to put it into a branch (maybe feature, maybe `develop`), you're interested in keeping whole files. You want to split your big commit into smaller ones.

Say you have:

- branch `solution`, with the solution to your spike. One ahead of `develop`.
- branch `develop`, where you want to add your changes.

You can solve it bringing the contents to your branch:
(develop)$ git checkout solution -- file1.txt

This will get the contents of that file in branch `solution` to your branch `develop`:

# On branch develop# Your branch is up-to-date with 'origin/develop'.# Changes to be committed:# (use "git reset HEAD <file>..." to unstage)## modified: file1.txt

Then, commit as usual.

Note: Spike solutions are made to analyze or solve the problem. These solutions are used for estimation and discarded once everyone gets clear visualization of the problem. ~ [Wikipedia](https://en.wikipedia.org/wiki/Extreme_programming_practices).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='519'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2556' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-made-several-commits-on-a-single-branch-that-should-be-on-different-branches)I made several commits on a single branch that should be on different branches

Say you are on your master branch. Running `git log`, you see you have made two commits:

(master)$ git log
commit e3851e817c451cc36f2e6f3049db528415e3c114
Author: Alex Lee <alexlee@example.com>Date: Tue Jul 22 15:39:27 2014 -0400
Bug #21 - Added CSRF protectioncommit 5ea51731d150f7ddc4a365437931cd8be3bf3131
Author: Alex Lee <alexlee@example.com>Date: Tue Jul 22 15:39:12 2014 -0400
Bug #14 - Fixed spacing on titlecommit a13b85e984171c6e2a1729bb061994525f626d14
Author: Aki Rose <akirose@example.com>Date: Tue Jul 21 01:12:48 2014 -0400
First commit

Let's take note of our commit hashes for each bug (`e3851e8` for #21, `5ea5173` for #14).

First, let's reset our master branch to the correct commit (`a13b85e`):
(master)$ git reset --hard a13b85e
HEAD is now at a13b85e
Now, we can create a fresh branch for our bug #21:
(master)$ git checkout -b 21
(21)$

Now, let's *cherry-pick* the commit for bug #21 on top of our branch. That means we will be applying that commit, and only that commit, directly on top of whatever our head is at.

(21)$ git cherry-pick e3851e8

At this point, there is a possibility there might be conflicts. See the [**There were conflicts**](https://github.com/k88hudson/git-flight-rules#merge-conflict) section in the [interactive rebasing section above](https://github.com/k88hudson/git-flight-rules#interactive-rebase) for how to resolve conflicts.

Now let's create a new branch for bug #14, also based on master
(21)$ git checkout master
(master)$ git checkout -b 14
(14)$
And finally, let's cherry-pick the commit for bug #14:
(14)$ git cherry-pick 5ea5173

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='520'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2574' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-local-branches-that-were-deleted-upstream)I want to delete local branches that were deleted upstream

Once you merge a pull request on GitHub, it gives you the option to delete the merged branch in your fork. If you aren't planning to keep working on the branch, it's cleaner to delete the local copies of the branch so you don't end up cluttering up your working checkout with a lot of stale branches.

$ git fetch -p upstream
where, `upstream` is the remote you want to fetch from.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='521'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2580' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-accidentally-deleted-my-branch)I accidentally deleted my branch

If you're regularly pushing to remote, you should be safe most of the time. But still sometimes you may end up deleting your branches. Let's say we create a branch and create a new file:

(master)$ git checkout -b my-branch
(my-branch)$ git branch
(my-branch)$ touch foo.txt
(my-branch)$ ls
README.md foo.txt
Let's add it and commit.

(my-branch)$ git add .(my-branch)$ git commit -m 'foo.txt added'(my-branch)$ foo.txt added

1 files changed, 1 insertions(+)
create mode 100644 foo.txt
(my-branch)$ git log
commit 4e3cd85a670ced7cc17a2b5d8d3d809ac88d5012
Author: siemiatj <siemiatj@example.com>Date: Wed Jul 30 00:34:10 2014 +0200
foo.txt added
commit 69204cdf0acbab201619d95ad8295928e7f411d5

Author: Kate Hudson <katehudson@example.com>Date: Tue Jul 29 13:14:46 2014 -0400

Fixes #6: Force pushing after amending commits
Now we're switching back to master and 'accidentally' removing our branch.
(my-branch)$ git checkout master
Switched to branch 'master'Your branch is up-to-date with 'origin/master'.
(master)$ git branch -D my-branch
Deleted branch my-branch (was 4e3cd85).
(master)$ echo oh noes, deleted my branch!oh noes, deleted my branch!

At this point you should get familiar with 'reflog', an upgraded logger. It stores the history of all the action in the repo.

	(master)$ git reflog
	69204cd HEAD@{0}: checkout: moving from my-branch to master
	4e3cd85 HEAD@{1}: commit: foo.txt added
	69204cd HEAD@{2}: checkout: moving from master to my-branch

As you can see we have commit hash from our deleted branch. Let's see if we can restore our deleted branch.

(master)$ git checkout -b my-branch-help

Switched to a new branch 'my-branch-help'(my-branch-help)$ git reset --hard 4e3cd85

HEAD is now at 4e3cd85 foo.txt added
(my-branch-help)$ ls
README.md foo.txt

Voila! We got our removed file back. `git reflog` is also useful when rebasing goes terribly wrong.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='522'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2592' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-a-branch)I want to delete a branch

To delete a remote branch:
(master)$ git push origin --delete my-branch
You can also do:
(master)$ git push origin :my-branch
To delete a local branch:
(master)$ git branch -d my-branch

To delete a local branch that *has not* been merged to the current branch or an upstream:

(master)$ git branch -D my-branch

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='523'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2603' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-delete-multiple-branches)I want to delete multiple branches

Say you want to delete all branches that start with `fix/`:
(master)$ git branch | grep 'fix/'  | xargs git branch -d

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='524'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2607' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-rename-a-branch)I want to rename a branch

To rename the current (local) branch:
(master)$ git branch -m new-name
To rename a different (local) branch:
(master)$ git branch -m old-name new-name

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='525'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2614' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-checkout-to-a-remote-branch-that-someone-else-is-working-on)I want to checkout to a remote branch that someone else is working on

First, fetch all branches from remote:
(master)$ git fetch --all
Say you want to checkout to `daves` from the remote.
(master)$ git checkout --track origin/daves
Branch daves set up to track remote branch daves from origin.
Switched to a new branch 'daves'
(`--track` is shorthand for `git checkout -b [branch] [remotename]/[branch]`)

This will give you a local copy of the branch `daves`, and any update that has been pushed will also show up remotely.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='526'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2622' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-create-a-new-remote-branch-from-current-local-one)I want to create a new remote branch from current local one

$ git push <remote> HEAD

If you would also like to set that remote branch as upstream for the current one, use the following instead:

$ git push -u <remote> HEAD

With the `upstream` mode and the `simple` (default in Git 2.0) mode of the `push.default` config, the following command will push the current branch with regards to the remote branch that has been registered previously with `-u`:

$ git push

The behavior of the other modes of `git push` is described in the [doc of `push.default`](https://git-scm.com/docs/git-config#git-config-pushdefault).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='527'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2630' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-set-a-remote-branch-as-the-upstream-for-a-local-branch)I want to set a remote branch as the upstream for a local branch

You can set a remote branch as the upstream for the current local branch using:

$ git branch --set-upstream-to [remotename]/[branch]# or, using the shorthand:$ git branch -u [remotename]/[branch]

To set the upstream remote branch for another local branch:
$ git branch -u [remotename]/[branch] [local-branch]

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='528'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2637' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-set-my-head-to-track-the-default-remote-branch)I want to set my HEAD to track the default remote branch

By checking your remote branches, you can see which remote branch your HEAD is tracking. In some cases, this is not the desired branch.

$ git branch -r
origin/HEAD -> origin/gh-pages
origin/master
To change `origin/HEAD` to track `origin/master`, you can run this command:
$ git remote set-head origin --auto
origin/HEAD set to master

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='529'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2643' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-made-changes-on-the-wrong-branch)I made changes on the wrong branch

You've made uncommitted changes and realise you're on the wrong branch. Stash changes and apply them to the branch you want:

(wrong_branch)$ git stash
(wrong_branch)$ git checkout <correct_branch>(correct_branch)$ git stash apply

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='530'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2647' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#rebasing-and-merging)Rebasing and Merging

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='531'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2650' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-undo-rebasemerge)I want to undo rebase/merge

You may have merged or rebased your current branch with a wrong branch, or you can't figure it out or finish the rebase/merge process. Git saves the original HEAD pointer in a variable called ORIG_HEAD before doing dangerous operations, so it is simple to recover your branch at the state before the rebase/merge.

(my-branch)$ git reset --hard ORIG_HEAD

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='532'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2655' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-rebased-but-i-dont-want-to-force-push)I rebased, but I don't want to force push

Unfortunately, you have to force push, if you want those changes to be reflected on the remote branch. This is because you have changed the history. The remote branch won't accept changes unless you force push. This is one of the main reasons many people use a merge workflow, instead of a rebasing workflow - large teams can get into trouble with developers force pushing. Use this with caution. A safer way to use rebase is not to reflect your changes on the remote branch at all, and instead to do the following:

(master)$ git checkout my-branch
(my-branch)$ git rebase -i master
(my-branch)$ git checkout master
(master)$ git merge --ff-only my-branch

For more, see [this SO thread](https://stackoverflow.com/questions/11058312/how-can-i-use-git-rebase-without-requiring-a-forced-push).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='533'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2661' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-combine-commits)I need to combine commits

Let's suppose you are working in a branch that is/will become a pull-request against `master`. In the simplest case when all you want to do is to combine *all* commits into a single one and you don't care about commit timestamps, you can reset and recommit. Make sure the master branch is up to date and all your changes committed, then:

(my-branch)$ git reset --soft master
(my-branch)$ git commit -am "New awesome feature"

If you want more control, and also to preserve timestamps, you need to do something called an interactive rebase:

(my-branch)$ git rebase -i master

If you aren't working against another branch you'll have to rebase relative to your `HEAD`. If you want to squash the last 2 commits, for example, you'll have to rebase against `HEAD~2`. For the last 3, `HEAD~3`, etc.

(master)$ git rebase -i HEAD~2

After you run the interactive rebase command, you will see something like this in your text editor:

pick a9c8a1d Some refactoring
pick 01b2fd8 New awesome feature
pick b729ad5 fixup
pick e3851e8 another fix# Rebase 8074d12..b729ad5 onto 8074d12
#

# Commands:# p, pick = use commit

# r, reword = use commit, but edit the commit message

# e, edit  = use commit, but stop  for amending

# s, squash = use commit, but meld into previous commit

# f, fixup = like "squash", but discard this commit's  log message

# x, exec  = run command (the rest of the line) using shell#

# These lines can be re-ordered; they are executed from top  to bottom.

#

# If you remove  a  line here THAT COMMIT WILL BE LOST.

#

# However, if you remove everything, the rebase will be aborted.

#

# Note that empty commits are commented out

All the lines beginning with a `#` are comments, they won't affect your rebase.

Then you replace `pick` commands with any in the list above, and you can also remove commits by removing corresponding lines.

For example, if you want to **leave the oldest (first) commit alone and combine all the following commits with the second oldest**, you should edit the letter next to each commit except the first and the second to say `f`:

pick a9c8a1d Some refactoring
pick 01b2fd8 New awesome featuref b729ad5 fixupf e3851e8 another fix

If you want to combine these commits **and rename the commit**, you should additionally add an `r` next to the second commit or simply use `s` instead of `f`:

pick a9c8a1d Some refactoring
pick 01b2fd8 New awesome features b729ad5 fixups e3851e8 another fix
You can then rename the commit in the next text prompt that pops up.
Newer, awesomer features

# Please enter the commit message for your changes. Lines starting

# with '#' will be ignored, and an empty message aborts the commit.

# rebase in progress; onto 8074d12

# You are currently editing a commit while rebasing branch 'master'  on  '8074d12'.

#

# Changes to be committed:

# modified: README.md

#
If everything is successful, you should see something like this:
(master)$ Successfully rebased and updated refs/heads/master.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='534'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2682' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#safe-merging-strategy)Safe merging strategy

`--no-commit` performs the merge but pretends the merge failed and does not autocommit, giving the user a chance to inspect and further tweak the merge result before committing. `no-ff` maintains evidence that a feature branch once existed, keeping project history consistent.

(master)$ git merge --no-ff --no-commit my-branch

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='535'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2686' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-merge-a-branch-into-a-single-commit)I need to merge a branch into a single commit

(master)$ git merge --squash my-branch

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='536'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2690' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-combine-only-unpushed-commits)I want to combine only unpushed commits

Sometimes you have several work in progress commits that you want to combine before you push them upstream. You don't want to accidentally combine any commits that have already been pushed upstream because someone else may have already made commits that reference them.

(master)$ git rebase -i @{u}

This will do an interactive rebase that lists only the commits that you haven't already pushed, so it will be safe to reorder/fix/squash anything in the list.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='537'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2695' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-abort-the-merge)I need to abort the merge

Sometimes the merge can produce problems in certain files, in those cases we can use the option `abort` to abort the current conflict resolution process, and try to reconstruct the pre-merge state.

(my-branch)$ git merge --abort
This command is available since Git version >= 1.7.4

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='538'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2700' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-need-to-update-the-parent-commit-of-my-branch)I need to update the parent commit of my branch

Say I have a master branch, a feature-1 branch branched from master, and a feature-2 branch branched off of feature-1. If I make a commit to feature-1, then the parent commit of feature-2 is no longer accurate (it should be the head of feature-1, since we branched off of it). We can fix this with `git rebase --onto`.

(feature-2)$ git rebase --onto feature-1 <the first commit in your feature-2 branch that you don't want to bring along> feature-2

This helps in sticky scenarios where you might have a feature built on another feature that hasn't been merged yet, and a bugfix on the feature-1 branch needs to be reflected in your feature-2 branch.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='539'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2705' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#check-if-all-commits-on-a-branch-are-merged)Check if all commits on a branch are merged

To check if all commits on a branch are merged into another branch, you should diff between the heads (or any commits) of those branches:

(master)$ git log --graph --left-right --cherry-pick --oneline HEAD...feature/120-on-scroll

This will tell you if any commits are in one but not the other, and will give you a list of any nonshared between the branches. Another option is to do this:

(master)$ git log master ^feature/120-on-scroll --no-merges

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='540'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2711' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#possible-issues-with-interactive-rebases)Possible issues with interactive rebases

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='541'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2714' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#the-rebase-editing-screen-says-noop)The rebase editing screen says 'noop'

If you're seeing this:

	noop

That means you are trying to rebase against a branch that is at an identical commit, or is *ahead* of your current branch. You can try:

- making sure your master branch is where it should be
- rebase against `HEAD~2` or earlier instead

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='542'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2723' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#there-were-conflicts)There were conflicts

If you are unable to successfully complete the rebase, you may have to resolve conflicts.

First run `git status` to see which files have conflicts in them:
(my-branch)$ git status
On branch my-branch
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)
both modified: README.md

In this example, `README.md` has conflicts. Open that file and look for the following:

<<<<<<< HEAD
some code ========= some code
>>>>>>> new-commit

You will need to resolve the differences between the code that was added in your new commit (in the example, everything from the middle line to `new-commit`) and your `HEAD`.

If you want to keep one branch's version of the code, you can use `--ours` or `--theirs`:

(master*)$ git checkout --ours README.md

- When *merging*, use `--ours` to keep changes from the local branch, or `--theirs` to keep changes from the other branch.
- When *rebasing*, use `--theirs` to keep changes from the local branch, or `--ours` to keep changes from the other branch. For an explanation of this swap, see [this note in the Git documentation](https://git-scm.com/docs/git-rebase#git-rebase---merge).

If the merges are more complicated, you can use a visual diff editor:
(master*)$ git mergetool -t opendiff

After you have resolved all conflicts and tested your code, `git add` the files you have changed, and then continue the rebase with `git rebase --continue`

(my-branch)$ git add README.md
(my-branch)$ git rebase --continue

If after resolving all the conflicts you end up with an identical tree to what it was before the commit, you need to `git rebase --skip` instead.

If at any time you want to stop the entire rebase and go back to the original state of your branch, you can do so:

(my-branch)$ git rebase --abort

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='543'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2746' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#stash)Stash

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='544'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2748' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#stash-all-edits)Stash all edits

To stash all the edits in your working directory
$ git stash
If you also want to stash untracked files, use `-u` option.
$ git stash -u

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='545'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2754' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#stash-specific-files)Stash specific files

To stash only one file from your working directory
$ git stash push working-directory-path/filename.ext
To stash multiple files from your working directory

$ git stash push working-directory-path/filename1.ext working-directory-path/filename2.ext

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='546'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2761' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#stash-with-message)Stash with message

$ git stash save <message>

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='547'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2765' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#apply-a-specific-stash-from-list)Apply a specific stash from list

First check your list of stashes with message using
$ git stash list
Then apply a specific stash from the list using
$ git stash apply "stash@{n}"

Here, 'n' indicates the position of the stash in the stack. The topmost stash will be position 0.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='548'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2772' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#finding)Finding

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='549'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2774' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-find-a-string-in-any-commit)I want to find a string in any commit

To find a certain string which was introduced in any commit, you can use the following structure:

$ git log -S "string to find"
Commons parameters:

- `--source` means to show the ref name given on the command line by which each commit was reached.
- `--all` means to start from every branch.
- `--reverse` prints in reverse order, it means that will show the first commit that made the change.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='550'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2787' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-find-by-authorcommitter)I want to find by author/committer

To find all commits by author/committer you can use:
$ git log --author=<name or email>$ git log --committer=<name or email>

Keep in mind that author and committer are not the same. The `--author` is the person who originally wrote the code; on the other hand, the `--committer`, is the person who committed the code on behalf of the original author.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='551'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2792' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-list-commits-containing-specific-files)I want to list commits containing specific files

To find all commits containing a specific file you can use:
$ git log -- <path to file>

You would usually specify an exact path, but you may also use wild cards in the path and file name:

$ git log -- **/*.js

While using wildcards, it's useful to inform `--name-status` to see the list of committed files:

$ git log --name-status -- **/*.js

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='552'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2801' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-view-the-commit-history-for-a-specific-function)I want to view the commit history for a specific function

To trace the evolution of a single function you can use:
$ git log -L :FunctionName:FilePath

Note that you can combine this with further `git log` options, like [revision ranges](https://git-scm.com/docs/gitrevisions) and [commit limits](https://git-scm.com/docs/git-log/#_commit_limiting).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='553'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2806' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#find-a-tag-where-a-commit-is-referenced)Find a tag where a commit is referenced

To find all tags containing a specific commit:
$ git tag --contains <commitid>

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='554'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2810' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#submodules)Submodules

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='555'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2813' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#clone-all-submodules)Clone all submodules

$ git clone --recursive git://github.com/foo/bar.git
If already cloned:
$ git submodule update --init --recursive

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='556'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2819' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#remove-a-submodule)Remove a submodule

Creating a submodule is pretty straight-forward, but deleting them less so. The commands you need are:

$ git submodule deinit submodulename
$ git rm submodulename
$ git rm --cached submodulename
$ rm -rf .git/modules/submodulename

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='557'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2823' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#miscellaneous-objects)Miscellaneous Objects

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='558'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2825' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#restore-a-deleted-file)Restore a deleted file

First find the commit when the file last existed:
$ git rev-list -n 1 HEAD -- filename
Then checkout that file:

	git checkout deletingcommitid^ -- filename

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='559'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2830' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#delete-tag)Delete tag

$ git tag -d <tag_name>$ git push <remote> :refs/tags/<tag_name>

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='560'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2834' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#recover-a-deleted-tag)Recover a deleted tag

If you want to recover a tag that was already deleted, you can do so by following these steps: First, you need to find the unreachable tag:

$ git fsck --unreachable | grep tag

Make a note of the tag's hash. Then, restore the deleted tag with following, making use of [`git update-ref`](https://git-scm.com/docs/git-update-ref):

$ git update-ref refs/tags/<tag_name>  <hash>
Your tag should now have been restored.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='561'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2841' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#deleted-patch)Deleted Patch

If someone has sent you a pull request on GitHub, but then deleted their original fork, you will be unable to clone their repository or to use `git am` as the [.diff, .patch](https://github.com/blog/967-github-secrets) URLs become unavailable. But you can checkout the PR itself using [GitHub's special refs](https://gist.github.com/piscisaureus/3342247). To fetch the content of PR#1 into a new branch called pr_1:

$ git fetch origin refs/pull/1/head:pr_1
From github.com:foo/bar * [new ref] refs/pull/1/head -> pr_1

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='562'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2845' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#exporting-a-repository-as-a-zip-file)Exporting a repository as a Zip file

$ git archive --format zip --output /full/path/to/zipfile.zip master

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='563'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2848' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#push-a-branch-and-a-tag-that-have-the-same-name)Push a branch and a tag that have the same name

If there is a tag on a remote repository that has the same name as a branch you will get the following error when trying to push that branch with a standard `$ git push <remote> <branch>` command.

$ git push origin <branch>error: dst refspec same matches more than one.
error: failed to push some refs to '<git server>'
Fix this by specifying you want to push the head reference.
$ git push origin refs/heads/<branch-name>

If you want to push a tag to a remote repository that has the same name as a branch, you can use a similar command.

$ git push origin refs/tags/<tag-name>

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='564'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2856' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#tracking-files)Tracking Files

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/i-want-to-change-a-file-names-capitalization-without-changing-the-contents-of-the-file)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='565'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2859' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-change-a-file-names-capitalization-without-changing-the-contents-of-the-file)I want to change a file name's capitalization, without changing the contents of the file

(master)$ git mv --force myfile MyFile

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='566'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2862' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-overwrite-local-files-when-doing-a-git-pull)I want to overwrite local files when doing a git pull

(master)$ git fetch --all
(master)$ git reset --hard origin/master

[(L)](https://github.com/k88hudson/git-flight-rules/blob/master/remove-from-git)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='567'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2866' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-remove-a-file-from-git-but-keep-the-file)I want to remove a file from Git but keep the file

(master)$ git rm --cached log.txt

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='568'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2869' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-revert-a-file-to-a-specific-revision)I want to revert a file to a specific revision

Assuming the hash of the commit you want is c5f567:
(master)$ git checkout c5f567 -- file1/to/restore file2/to/restore

If you want to revert to changes made just 1 commit before c5f567, pass the commit hash as c5f567~1:

(master)$ git checkout c5f567~1 -- file1/to/restore file2/to/restore

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='569'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2875' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-list-changes-of-a-specific-file-between-commits-or-branches)I want to list changes of a specific file between commits or branches

Assuming you want to compare last commit with file from commit c5f567:
$ git diff HEAD:path_to_file/file c5f567:path_to_file/file
Same goes for branches:
$ git diff master:path_to_file/file staging:path_to_file/file

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='570'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2881' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-git-to-ignore-changes-to-a-specific-file)I want Git to ignore changes to a specific file

This works great for config templates or other files that require locally adding credentials that shouldn't be committed.

$ git update-index --assume-unchanged file-to-ignore

Note that this does *not* remove the file from source control - it is only ignored locally. To undo this and tell Git to notice changes again, this clears the ignore flag:

$ git update-index --no-assume-unchanged file-to-stop-ignoring

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='571'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2888' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#debugging-with-git)Debugging with Git

The [git-bisect](https://git-scm.com/docs/git-bisect) command uses a binary search to find which commit in your Git history introduced a bug.

Suppose you're on the `master` branch, and you want to find the commit that broke some feature. You start bisect:

$ git bisect start

Then you should specify which commit is bad, and which one is known to be good. Assuming that your *current* version is bad, and `v1.1.1` is good:

$ git bisect bad
$ git bisect good v1.1.1

Now `git-bisect` selects a commit in the middle of the range that you specified, checks it out, and asks you whether it's good or bad. You should see something like:

$ Bisecting: 5 revision left to test after this (roughly 5 step)
$ [c44abbbee29cb93d8499283101fe7c8d9d97f0fe] Commit message
$ (c44abbb)$
You will now check if this commit is good or bad. If it's good:
$ (c44abbb)$ git bisect good

and `git-bisect` will select another commit from the range for you. This process (selecting `good` or `bad`) will repeat until there are no more revisions left to inspect, and the command will finally print a description of the **first** bad commit.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='572'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2901' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#configuration)Configuration

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='573'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2903' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-add-aliases-for-some-git-commands)I want to add aliases for some Git commands

On OS X and Linux, your git configuration file is stored in `~/.gitconfig`. I've added some example aliases I use as shortcuts (and some of my common typos) in the `[alias]` section as shown below:

[alias] a  =  add amend = commit --amend c  = commit ca  = commit --amend ci  = commit -a  co  = checkout d  =  diff dc =  diff  --changed ds  =  diff  --staged extend  = commit --amend -C HEAD f  = fetch

loll =  log  --graph --decorate --pretty=oneline --abbrev-commit m  = merge
one =  log  --pretty=oneline
outstanding = rebase -i  @{u}
reword = commit --amend --only  s  = status
unpushed =  log  @{u} wc  = whatchanged
wip = rebase -i  @{u}

zap = fetch -p day =  log  --reverse  --no-merges --branches=*  --date=local --since=midnight --author=\"$(git config --get  user.name)\"  delete-merged-branches =  "!f() { git checkout --quiet master && git branch --merged | grep --invert-match '\\*' | xargs -n 1 git branch --delete; git checkout --quiet @{-1}; }; f"

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='574'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2910' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-add-an-empty-directory-to-my-repository)I want to add an empty directory to my repository

You can’t! Git doesn’t support this, but there’s a hack. You can create a .gitignore file in the directory with the following contents:

	 # Ignore everything in this directory
	 *
	 # Except this file
	 !.gitignore

Another common convention is to make an empty file in the folder, titled .gitkeep.

$ mkdir mydir
$ touch mydir/.gitkeep

You can also name the file as just .keep , in which case the second line above would be `touch mydir/.keep`

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='575'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2916' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-cache-a-username-and-password-for-a-repository)I want to cache a username and password for a repository

You might have a repository that requires authentication. In which case you can cache a username and password so you don't have to enter it on every push and pull. Credential helper can do this for you.

$ git config --global credential.helper cache# Set git to use the credential memory cache

$ git config --global credential.helper 'cache --timeout=3600'# Set the cache to timeout after 1 hour (setting is in seconds)

To find a credential helper:
$ git help -a | grep credential# Shows you possible credential helpers
For OS specific credential caching:
$ git config --global credential.helper osxkeychain# For OSX
$ git config --global credential.helper manager# Git for Windows 2.7.3+

$ git config --global credential.helper gnome-keyring# Ubuntu and other GNOME-based distros

More credential helpers can likely be found for different distributions and operating systems.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='576'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2928' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-make-git-ignore-permissions-and-filemode-changes)I want to make Git ignore permissions and filemode changes

$ git config core.fileMode false
If you want to make this the default behaviour for logged-in users, then use:
$ git config --global core.fileMode false

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='577'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2933' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-set-a-global-user)I want to set a global user

To configure user information used across all local repositories, and to set a name that is identifiable for credit when review version history:

$ git config --global user.name “[firstname lastname]”
To set an email address that will be associated with each history marker:
git config --global user.email “[valid-email]”

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='578'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2939' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#i-want-to-add-command-line-coloring-for-git)I want to add command line coloring for Git

To set automatic command line coloring for Git for easy reviewing:
$ git config --global color.ui auto

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='579'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2943' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#ive-no-idea-what-i-did-wrong)I've no idea what I did wrong

So, you're screwed - you `reset` something, or you merged the wrong branch, or you force pushed and now you can't find your commits. You know, at some point, you were doing alright, and you want to go back to some state you were at.

This is what `git reflog` is for. `reflog` keeps track of any changes to the tip of a branch, even if that tip isn't referenced by a branch or a tag. Basically, every time HEAD changes, a new entry is added to the reflog. This only works for local repositories, sadly, and it only tracks movements (not changes to a file that weren't recorded anywhere, for instance).

(master)$ git reflog
0a2e358 HEAD@{0}: reset: moving to HEAD~2
0254ea7 HEAD@{1}: checkout: moving from 2.2 to master
c10f740 HEAD@{2}: checkout: moving from master to 2.2

The reflog above shows a checkout from master to the 2.2 branch and back. From there, there's a hard reset to an older commit. The latest activity is represented at the top labeled `HEAD@{0}`.

If it turns out that you accidentally moved back, the reflog will contain the commit master pointed to (0254ea7) before you accidentally dropped 2 commits.

$ git reset --hard 0254ea7

Using `git reset` it is then possible to change master back to the commit it was before. This provides a safety net in case history was accidentally changed.

(copied and edited from [Source](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='580'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2954' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#git-shortcuts)Git Shortcuts

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='581'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2956' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#git-bash)Git Bash

Once you're comfortable with what the above commands are doing, you might want to create some shortcuts for Git Bash. This allows you to work a lot faster by doing complex tasks in really short commands.

alias sq=squashfunction  squash() {
git rebase -i HEAD~$1}
Copy those commands to your .bashrc or .bash_profile.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='582'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2961' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#powershell-on-windows)PowerShell on Windows

If you are using PowerShell on Windows, you can also set up aliases and functions. Add these commands to your profile, whose path is defined in the `$profile` variable. Learn more at the [About Profiles](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles) page on the Microsoft documentation site.

Set-Alias sq Squash-Commitsfunction  Squash-Commits {
git rebase -i HEAD~$1}

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='583'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2964' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#other-resources)Other Resources

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='584'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2966' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#books)Books

- [Learn Enough Git to Be Dangerous](https://www.learnenough.com/git-tutorial) - A book by Michael Hartl covering Git from basics
- [Pro Git](https://git-scm.com/book/en/v2) - Scott Chacon and Ben Straub's excellent book about Git
- [Git Internals](https://github.com/pluralsight/git-internals-pdf) - Scott Chacon's other excellent book about Git
- [Nasa handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook.pdf)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='585'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2973' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#tutorials)Tutorials

- [19 Git Tips For Everyday Use](https://www.alexkras.com/19-git-tips-for-everyday-use) - A list of useful Git one liners
- [Atlassian's Git tutorial](https://www.atlassian.com/git/tutorials) Get Git right with tutorials from beginner to advanced.
- [Learn Git branching](https://learngitbranching.js.org/) An interactive web based branching/merging/rebasing tutorial
- [Getting solid at Git rebase vs. merge](https://medium.com/@porteneuve/getting-solid-at-git-rebase-vs-merge-4fa1a48c53aa)
- [Git Commands and Best Practices Cheat Sheet](https://zeroturnaround.com/rebellabs/git-commands-and-best-practices-cheat-sheet) - A Git cheat sheet in a blog post with more explanations
- [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out) - A tutorial that dives into Git's internals
- [git-workflow](https://github.com/asmeurer/git-workflow) - [Aaron Meurer](https://github.com/asmeurer)'s howto on using Git to contribute to open source repositories
- [GitHub as a workflow](https://hugogiraudel.com/2015/08/13/github-as-a-workflow/) - An interesting take on using GitHub as a workflow, particularly with empty PRs
- [Githug](https://github.com/Gazler/githug) - A game to learn more common Git workflows
- [learnGitBranching](https://github.com/pcottle/learnGitBranching) - An interactive git visualization to challenge and educate!

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='586'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2986' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#scripts-and-tools)Scripts and Tools

- [firstaidgit.io](http://firstaidgit.io/) A searchable selection of the most frequently asked Git questions
- [git-extra-commands](https://github.com/unixorn/git-extra-commands) - a collection of useful extra Git scripts
- [git-extras](https://github.com/tj/git-extras) - GIT utilities -- repo summary, repl, changelog population, author commit percentages and more
- [git-fire](https://github.com/qw3rtman/git-fire) - git-fire is a Git plugin that helps in the event of an emergency by adding all current files, committing, and pushing to a new branch (to prevent merge conflicts).
- [git-tips](https://github.com/git-tips/tips) - Small Git tips
- [git-town](https://github.com/Originate/git-town) - Generic, high-level Git workflow support! [http://www.git-town.com](http://www.git-town.com/)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='587'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='2995' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/k88hudson/git-flight-rules#gui-clients)GUI Clients

- [GitKraken](https://www.gitkraken.com/) - The downright luxurious Git client,for Windows, Mac & Linux
- [git-cola](https://git-cola.github.io/) - another Git client for Windows and OS X
- [GitUp](https://github.com/git-up/GitUp) - A newish GUI that has some very opinionated ways of dealing with Git's complications
- [gitx-dev](https://rowanj.github.io/gitx/) - another graphical Git client for OS X
- [Sourcetree](https://www.sourcetreeapp.com/) - Simplicity meets power in a beautiful and free Git GUI. For Windows and Mac.
- [Tower](https://www.git-tower.com/) - graphical Git client for OS X (paid)
- [tig](https://jonas.github.io/tig/) - terminal text-mode interface for Git
- [Magit](https://magit.vc/) - Interface to Git implemented as an Emacs package.
- [GitExtensions](https://github.com/gitextensions/gitextensions) - a shell extension, a Visual Studio 2010-2015 plugin and a standalone Git repository tool.
- [Fork](https://git-fork.com/) - a fast and friendly Git client for Mac (beta)
- [gmaster](https://gmaster.io/) - a Git client for Windows that has 3-way merge, analyze refactors, semantic diff and merge (beta)
- [gitk](https://git-scm.com/docs/gitk) - a Git client for linux to allow simple view of repo state.
- [SublimeMerge](https://www.sublimemerge.com/) - Blazing fast, extensible client that provides 3-way merges, powerful search and syntax highlighting, in active development.