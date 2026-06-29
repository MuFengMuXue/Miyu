[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (use of [2nd person pronouns](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Avoid_first_and_second_person_writing "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

** Note**\
Some of the policies and suggestions listed here may need refreshing. If in doubt, please refer to the official standard of [GLEP 66](https://www.gentoo.org/glep/glep-0066.html).

This article outlines some rules and best-practices regarding the typical workflow for ebuild developers using [git].

Developers are encouraged to use [[pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck")] and [[pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev")].

## Contents

-   [[1] [Commit policy]](#Commit_policy)
    -   [[1.1] [Atomicity]](#Atomicity)
    -   [[1.2] [Commit message format]](#Commit_message_format)
-   [[2] [Branching model]](#Branching_model)
    -   [[2.1] [Branch naming convention]](#Branch_naming_convention)
    -   [[2.2] [About rebasing]](#About_rebasing)
    -   [[2.3] [About merging]](#About_merging)
-   [[3] [Remote model]](#Remote_model)
-   [[4] [Best practices]](#Best_practices)
-   [[5] [Repository settings]](#Repository_settings)
    -   [[5.1] [Summary]](#Summary)
    -   [[5.2] [Cloning]](#Cloning)
    -   [[5.3] [Configuration]](#Configuration)
        -   [[5.3.1] [Signoff]](#Signoff)
        -   [[5.3.2] [GPG configuration]](#GPG_configuration)
            -   [[5.3.2.1] [Creating a key]](#Creating_a_key)
            -   [[5.3.2.2] [Setting it up]](#Setting_it_up)
-   [[6] [Workflow walkthrough]](#Workflow_walkthrough)
    -   [[6.1] [Common ebuild work]](#Common_ebuild_work)
    -   [[6.2] [Pull requests from developers and users]](#Pull_requests_from_developers_and_users)
        -   [[6.2.1] [using pram]](#using_pram)
        -   [[6.2.2] [git am method]](#git_am_method)
        -   [[6.2.3] [git cherry-pick method]](#git_cherry-pick_method)
-   [[7] [Tips and tricks]](#Tips_and_tricks)
    -   [[7.1] [Working with git]](#Working_with_git)
    -   [[7.2] [Diffs for revision bumps]](#Diffs_for_revision_bumps)
    -   [[7.3] [Using the gentoo git checkout as a local tree]](#Using_the_gentoo_git_checkout_as_a_local_tree)
    -   [[7.4] [Github pull request made easy]](#Github_pull_request_made_easy)
    -   [[7.5] [Grafting Gentoo history onto the active repository]](#Grafting_Gentoo_history_onto_the_active_repository)
    -   [[7.6] [Preventing \'git repack -a\' from touching huge packs]](#Preventing_.27git_repack_-a.27_from_touching_huge_packs)
    -   [[7.7] [Retaining commit author information]](#Retaining_commit_author_information)
    -   [[7.8] [A cli-tool to crawl through pull requests]](#A_cli-tool_to_crawl_through_pull_requests)
    -   [[7.9] [Automatic git pull/rebase merge involving conflicts with KEYWORDS]](#Automatic_git_pull.2Frebase_merge_involving_conflicts_with_KEYWORDS)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [And summarizing it all, \...]](#And_summarizing_it_all.2C_...)

## [Commit policy]

-   Atomic commits (one logical change).
-   All commits must be pkgcheck-valid (exceptions only on right-hand branches).
-   Commits may span across multiple ebuilds/directories if it\'s one logical change.
-   Every commit on the left-most line of the history (that is, all the commits following the first parent of each commit) must be GPG signed by a Gentoo developer.
-   [pkgcheck scan] must be run from all related ebuild directories (or related category directories or top-level directory) on the tip of the local master branch (as in: right before pushing and also after resolving push-conflicts).

### [Atomicity]

-   Commits in git are cheap and local, so use them often.
-   Split version bumps and ebuild cleanup in separate commits (makes reverting ebuild removals much easier).
-   One may break atomicity in order to make a commit pkgcheck-valid (or reconsidering the order you commit in, e.g. license first, then the new ebuild).

### [Commit message format]

-   All lines max 75 characters.
-   If `CATEGORY/PN` is very long and the 75 character limit is impossible to obey, it is OK to exceed the limit in this case.
-   First line brief explanation.
-   Second line *always* empty.
-   Optional detailed multiline explanation must start at the third line.
-   Commits that affect primarily a particular subsystem should prepend the following code to the first line of the commit message:
    -   Single package -\> `CATEGORY/PN:`
    -   Profile directory -\> `profiles:`
    -   Eclass directory -\> `ECLASSNAME.eclass:`
    -   Licenses directory -\> `licenses:`
    -   Metadata directory -\> `metadata:`
    -   A whole category -\> `CATEGORY:`
-   If the change affects multiple directories, but is mostly related to a particular subsystem, then prepend the subsystem which best reflects the intention (e.g. you add a new license, but also modify profiles/license_groups).
-   It is also encouraged to use tag formats such as `Acked-by:`, `Suggested-by:`, and so on. Please review the [kernel patch guideline](https://www.kernel.org/doc/Documentation/process/submitting-patches.rst) for additional tag variants.

**Example**

    app-misc/foo: version bump to 0.5

    Bump to 0.5. This also fixes security
    bug 93829 and introduces the new USE flag 'bar'.

    Bug: https://bugs.gentoo.org/93829
    Acked-by: Hans Wurst <hans@gentoo.org>
    Reported-by: Alice Wonderland <alice@foo.com>
    Signed-off-by: A Developer <example@gentoo.org>

## [Branching model]

-   The primary production-ready branch is [master](https://gitweb.gentoo.org/repo/gentoo.git/log/) (users will pull from here), there are **only fast-forward** pushes allowed.
-   There may be developer-specific, task-specific, project-specific branches, etc.

### [Branch naming convention]

-   Developer branches: `dev/<name>`
-   Project branches: `project/<name>`
-   If in doubt, or if the branch could be useful to others, discuss the naming on-list beforehand.

### [About rebasing]

-   Primary use case: in case of a non-fast-forward push conflict to remote master, try [git pull \--rebase=preserve] first; if that yields complicated conflicts, abort the rebase and continue with a regular merge (if the conflicts are trivial or even expected, e.g. arch teams keywording/stabilizing stuff, then stick to the rebase).
-   To preserve merges during a rebase use [git rebase \--preserve-merges \...] (if appropriate, e.g. for user branches).
-   Don\'t use `--preserve-merges` if you do an interactive rebase (see BUGS in git-rebase manpage).
-   Commits that are not on the remote master branch yet may be rewritten/squashed/splitted etc via interactive rebase, however the rebase must never span beyond those commits.
-   Never rebase on already pushed commits.
-   There are no particular rules for rebasing on non-master remote branches, but be aware that others might base their work on them.
-   There are no particular rules for rebasing non-remote branches, as long as they don\'t clutter the history when merged back into master.

### [About merging]

-   **Do not *ever* commit implicit merges done by git pull**. It is possible to set [git config \--local pull.ff only] to avoid git implicitly creating those.
-   We essentially never use merge commits in [::gentoo]. GLEP 66 does [allow](https://www.gentoo.org/glep/glep-0066.html#id6) for them in some cases but this isn\'t used in practice.

## [Remote model]

We have a main developer repository where developers work and commit (every Gentoo ebuild developer has direct push access). For every push into the repository, automated magic things merge stuff into user sync repository and update the metadata cache there.

User sync repository is for power users that want to fetch via [git]. It\'s quite fast and efficient for frequent updates, and also saves space by being free of the ChangeLog files.

On top of the user sync repository, rsync is propagated.

## [Best practices]

-   Before starting work on a local master, it\'s good to pull the latest changeset from the remote master.
-   It might be a good idea for projects/developers to accumulate changes either in their own branch or a separate repository and only push to remote master in intervals (that decreases the push rate and potential conflicts).

## [Repository settings]

### [Summary]

This is a summary of all the needed commands:

`user `[`$`]`git config --local user.signingkey 0xLONG-GPG-KEY `

`user `[`$`]`git config --local commit.gpgsign 1 `

`user `[`$`]`git config --local push.gpgsign 1 `

`user `[`$`]`git config --local pull.rebase true `

`user `[`$`]`git config --local --unset pull.ff`

For details, read on!

### [Cloning]

Clone the repository. This will make a shallow clone and speed up clone time:

`user `[`$`]`git clone --depth=50 git+ssh://git@git.gentoo.org/repo/gentoo.git`

Using the git+ssh:// protocol of course requires the user\'s SSH public key on the server. To get the full history, just omit `--depth=50` from the above command.

To make contributions via pull-requests, fork the repository (e.g. via GitHub) and then add it as a remote to a local git clone:

`user `[`$`]`git remote add fork ssh://git@github.com:yourusername/gentoo.git`

### [Configuration]

All developers should at least have the following configuration settings in their local developer repository. These setting will be written to [.git/config] and can also be edited manually. Run these from within the repository cloned in the step above:

`user `[`$`]`cd gentoo `

`user `[`$`]`git config --local user.name "Your Full Name" `

`user `[`$`]`git config --local user.email "example@gentoo.org" `

`user `[`$`]`git config --local pull.rebase true `

`user `[`$`]`git config --local --unset pull.ff `

`user `[`$`]`git config --local push.default simple`

#### [Signoff]

This is separate from signing commits or pushes. Gentoo requires that contributions comply with [GLEP 76](https://www.gentoo.org/glep/glep-0076.html) and the [Certificate of Origin](https://www.gentoo.org/glep/glep-0076.html#certificate-of-origin) is provided by contributors.

For commits or [git] operations outside of [[pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev")], some more (optional) work is needed.

Have git enable it for [git format-patch] too:

`user `[`$`]`cd gentoo `

`user `[`$`]`git config --local format.signoff yes`

But [git] does not support forcing it for [git commit]. Instead, [git commit -s] must be used. There are workarounds for this on Stack Overflow [here](https://stackoverflow.com/questions/41881722/how-can-i-force-git-commit-s-using-git-commit-command).

#### [GPG configuration]

##### [Creating a key]

Technically, it\'s not required to have a key as a non-developer, but [metadata/layout.conf] in [::gentoo] requires signed commits from people pushing. It\'s therefore easier with tooling to just use [gpg] and set it up even if technically as a contributor, commits don\'t need to be signed (as the developer pushing it will sign their commits).

See [Project:Infrastructure/Generating GLEP 63 based OpenPGP keys](https://wiki.gentoo.org/wiki/Project:Infrastructure/Generating_GLEP_63_based_OpenPGP_keys "Project:Infrastructure/Generating GLEP 63 based OpenPGP keys").

##### [Setting it up]

** Tip**\
If [pkgdev commit -s] fails with e.g. \'error: gpg failed to sign the data\', try enabling debug output:

`user `[`$`]`GIT_TRACE=1 pkgdev commit -s `

    [...]
    13:34:45.989010 run-command.c:664       trace: run_command: gpg --status-fd=2 -bsau 0xLONG-GPG-KEY
    error: gpg failed to sign the data

Executing the exact [gpg] command can help with debugging the real issue:

`user `[`$`]`gpg --status-fd=2 -bsau 0xLONG-GPG-KEY`

** Tip**\
Often, [gpg] needs to be told which TTY is being used for [gpg-agent] purposes. Set [GPG_TTY=\$(tty)] in this case.

To get the GPG key run this command. It should be the top line (starting with pub). If there is more than one key with the UID it will need to be selected manually (from the list of returned keys).

`user `[`$`]`gpg --list-public-keys --keyid-format 0xlong example@gentoo.org`

`user `[`$`]`git config --local user.signingkey 0xLONG-GPG-KEY `

`user `[`$`]`git config --local commit.gpgsign 1 `

`user `[`$`]`git config --local push.gpgsign 1 `

## [Workflow walkthrough]

[![Cycle of usercontributions.png](/images/thumb/6/6c/Cycle_of_usercontributions.png/300px-Cycle_of_usercontributions.png)](https://wiki.gentoo.org/wiki/File:Cycle_of_usercontributions.png)

These are just examples and people may choose different local workflows (especially in terms of when to stage/commit) as long as the end result works and is pkgcheck-checked. These examples try to be very safe, but basic.

Before doing anything, make sure the local git tree is in a correct state and the correct branch is checked out.

`user `[`$`]`git status`

### [Common ebuild work]

1.  Pull in the latest changeset, before starting work:

    :::: cmd-box


    `user `[`$`]`git pull --rebase origin master`


    ::::
2.  Do the work (including removing files)
3.  Confirm the ebuild directory is the current working directory
4.  Create the manifest:

    :::: cmd-box


    `user `[`$`]`pkgdev manifest`


    ::::
5.  Stage files (including removed ones), if any:

    :::: cmd-box


    `user `[`$`]`git add <new-files> <changed-files> <removed-files>`


    ::::

    :::::
    ** Note**\
    A shortcut for staging all files in the current dir (and subdirs) would be:

    :::: cmd-box


    `user `[`$`]`git add -- .`


    ::::
    :::::
6.  Check for errors:

    :::: cmd-box


    `user `[`$`]`pkgcheck scan`


    ::::

    ::::::::
    ** Warning**\
    [pkgcheck] checks the files on filesystem level and doesn\'t really know what changes are staged or committed! So make sure the ebuild directory is clean and there are no unstaged changes or untracked files when running pkgcheck. To check for such changes/files, run:

    :::: cmd-box


    `user `[`$`]`git status`


    ::::

    To clean up unstaged changes and untracked files run:

    ::::: cmd-box


    `user `[`$`]`git checkout -- .`





    `user `[`$`]`git clean -i`


    :::::
    ::::::::

    1.  If errors occur, fix them and continue from point 4
7.  Commit the files:

    :::: cmd-box


    `user `[`$`]`pkgdev commit -s`


    ::::

    and enter a meaningful commit message
8.  Push to the dev repository:

    :::: cmd-box


    `user `[`$`]`git push --signed origin master`


    ::::

    :::::
    ** Note**\
    You may use [pkgdev] here to push and optionally perform a rebase pull and scan of the commits analogous to point 1 below:

    :::: cmd-box


    `user `[`$`]`pkgdev push --pull --signed origin master`


    ::::
    :::::

    1.  If updates were rejected because of non-fast-forward push, try:

        :::: cmd-box


        `user `[`$`]`git pull --rebase=merges -S"$(git config --get user.signingkey)" origin master`


        ::::

        first, then run:

        :::: cmd-box


        `user `[`$`]`pkgcheck scan --commits`


        ::::

        and continue from point 8.

        :::::
        ** Note**\
        You may skip running [pkgcheck] another time if you have manually verified that the commits you are missing are totally unrelated to your work (e.g. only affect a package that is not in the dependency chain of yours). You can do so via:

        :::: cmd-box


        `user `[`$`]`git diff $(git merge-base master remotes/origin/master) remotes/origin/master`


        ::::
        :::::

        1.  If the rebase fails, but the conflicts are trivial and don\'t contain useful information (such as keyword stabilization), fix the conflicts and finish the rebase via:

            ::::: cmd-box


            `user `[`$`]`git mergetool`





            `user `[`$`]`git rebase --continue`


            :::::

            and continue from point 4
        2.  If the rebase fails and the conflicts are complicated or you think the information is useful, continue with a regular merge:

            ::::: cmd-box


            `user `[`$`]`git rebase --abort`





            `user `[`$`]`git merge remotes/origin/master`


            :::::

            1.  If merge conflicts occur, fix them via:

                :::: cmd-box


                `user `[`$`]`git mergetool`


                ::::

                and continue from point 4

                :::
                ** Warning**\
                A merge conflict is not to be taken lightly. It could indicate miscommunication in one way or another (e.g. several people working on the same ebuild), so fix that first and try to clarify the situation.
                :::
            2.  If no merge conflicts occur, run:

                :::: cmd-box


                `user `[`$`]`pkgcheck scan --commits`


                ::::

                and continue from point 8 above.

### [Pull requests from developers and users]

#### [using pram]

[[[app-portage/pram]](https://packages.gentoo.org/packages/app-portage/pram)[]] is a tool to help merge pull requests easily.

1.  Open the pull request assigned for you, or whatever you want to work on. We use [https://github.com/gentoo/gentoo/pull/12345](https://github.com/gentoo/gentoo/pull/12345) as an example.
2.  Make sure that everything is done correctly and that every commit has proper sign-off included.
3.  Apply and automatically close the pull request to ::gentoo repo via

    :::::: cmd-box


    `user `[`$`]`git pull`





    `user `[`$`]`pram 12345`





    `user `[`$`]`git push`


    ::::::

** Note**\
Always run [pkgcheck] before pushing:

`user `[`$`]`pkgcheck scan --commits`

** Note**\
[pram] can be used to merge PRs made to other repo than [gentoo/gentoo/]. Check its homepage or manpage for more info.

#### [git am method]

1.  Find a pull request you wish to merge, [https://github.com/gentoo/gentoo/pull/1](https://github.com/gentoo/gentoo/pull/1) as an example.
2.  Ensure your checkout is up to date:

    :::: cmd-box


    `user `[`$`]`git pull`


    ::::
3.  Fetch and apply chosen commit:

    :::: cmd-box


    `user `[`$`]`curl -s -L "`[`https://github.com/gentoo/gentoo/pull/1.patch`](https://github.com/gentoo/gentoo/pull/1.patch)`" | git am -sS`


    ::::
4.  You can review the changes with:

    ::::: cmd-box


    `user `[`$`]`git log remotes/origin/master..HEAD`





    `user `[`$`]`git diff remotes/origin/master..HEAD`


    :::::
5.  Make sure chosen commit didn\'t break things

    :::: cmd-box


    `user `[`$`]`pkgcheck scan --commits`


    ::::
6.  Push your changes

    :::: cmd-box


    `user `[`$`]`git push --signed`


    ::::

#### [git cherry-pick method]

1.  Identify the remote URL and the branch to be merged.
2.  Add a new remote:

    :::: cmd-box


    `user `[`$`]`git remote add <remote-name> <url>`


    ::::
3.  Fetch the changes:

    :::: cmd-box


    `user `[`$`]`git fetch <remote-name> <branch>`


    ::::
4.  You may review the changes manually first:

    ::::: cmd-box


    `user `[`$`]`git log master..remotes/<remote-name>/<branch>`





    `user `[`$`]`git diff master..remotes/<remote-name>/<branch>`


    :::::
5.  Checkout the remote branch:

    :::: cmd-box


    `user `[`$`]`git checkout remotes/<remote-name>/<branch>`


    ::::

    (you are now in detached HEAD mode)
6.  Test the ebuilds and run pkgcheck:

    :::: cmd-box


    `user `[`$`]`pkgcheck scan`


    ::::
7.  If everything is fine, switch back to master:

    :::: cmd-box


    `user `[`$`]`git checkout master`


    ::::
8.  Ensure your master branch is curent:

    :::: cmd-box


    `user `[`$`]`git pull`


    ::::
9.  If it\'s just one commit, do:

    :::: cmd-box


    `user `[`$`]`git cherry-pick <commit-hash>`


    ::::
10. If there are multiple commits in one consistent range, do:

    :::: cmd-box


    `user `[`$`]`git cherry-pick <first-new-commit-hash>^..<latest-new-commit-hash>`


    ::::
11. Push your changes

    :::: cmd-box


    `user `[`$`]`git push --signed`


    ::::

** Note**\
Alternatively, you can create a new local branch where you pull in the remote changes instead of working directly in detached HEAD mode on remotes/\<remote-name\>/\<branch\>.

## [Tips and tricks]

### [Working with git]

Staging files can be tedious, especially on the CLI. To mitigate this, it is possible to use the graphical clients [gitk] (for browsing history) and [git gui] (for staging/unstaging changes etc.). This will require enabling the `tk` USE flag for [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]].

### [Diffs for revision bumps]

Suppose you are making a new revision of the `app-foo/bar` package---you are removing `app-foo/bar-1.0.0` and replacing it with the new revision `app-foo/bar-1.0.0-r1`. In that case, git (by default) sees two changes: removal of the file `bar-1.0.0.ebuild` and addition of the file `bar-1.0.0-r1.ebuild`. If you attempt to view your changes with `git diff` or `git show`, you\'ll get a useless diff containing the entirety of both files.

Git can be coerced into showing the diff between the old and new revisions even though they live in separate files. The following command-line options specify how hard git should try to find files that have been copied or renamed:

`user `[`$`]`git diff --find-renames --find-copies --find-copies-harder`

In the common case, searching for renames is enough. To make that behavior the default easily:

`user `[`$`]`git config --local diff.renames true`

### [Using the gentoo git checkout as a local tree]

To use a git development checkout as a local tree, two things are required:

1.  make sure the directory has the correct access rights
2.  generate/get metadata-cache, dtd, glsa, projects.xml, and news yourself

For the latter, there are example hooks for [portage](https://github.com/hasufell/portage-gentoo-git-config) and [paludis](https://github.com/hasufell/paludis-gentoo-git-config). You should probably skip the files *[[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")/gentoo.conf]* and *[/etc/paludis/repositories/gentoo.conf]* respectively, so that portage/paludis doesn\'t mess up your checkout (as in: disable auto-sync).

** Warning**\
The linked hooks are WIP and may be subject to change!

### [Github pull request made easy]

[cd] into your gentoo Git repository and add these lines to the repo\'s [.git/config] file:

    [remote "github"]
      url = git@github.com:gentoo/gentoo.git
      fetch = +refs/heads/*:refs/remotes/github/*
      fetch = +refs/pull/*/head:refs/remotes/github/pr/*

Now type:

`user `[`$`]`git fetch github`

git should go and fetch all pull requests, and list them as branches.

`user `[`$`]`git branch -a`

Each pull request will now be displayed as a branch name, each with a different name such as \"remotes/github/pr/123\". For instance if you wish to fetch changes brought by [https://github.com/gentoo/gentoo/pull/105](https://github.com/gentoo/gentoo/pull/105), simply type:

`user `[`$`]`git checkout remotes/github/pr/105`

to checkout the pull request.

### [Grafting Gentoo history onto the active repository]

To graft the historical Gentoo repository onto your current one simply run:

`user `[`$`]`git remote add historical `[`https://anongit.gentoo.org/git/archive/repo/gentoo-2.git`](https://anongit.gentoo.org/git/archive/repo/gentoo-2.git)

`user `[`$`]`git fetch historical`

** Note**\
The historical repository has a size of 8.4 GiB. If you have problems with cloning from the above location, you can use its Github mirror as an alternative:

`user `[`$`]`git remote set-url historical `[`https://github.com/gentoo/gentoo-historical-2.git`](https://github.com/gentoo/gentoo-historical-2.git)

`user `[`$`]`git fetch historical`

`user `[`$`]`git replace --graft 56bd759df1d0c750a065b8c845e93d5dfa6b549d cvs-final-2015-08-08`

The general syntax of the last command is:

`user `[`$`]`git replace --graft <first new commit> <last old commit>`

(This may be useful if you\'re not using the official versions of the repositories.)

Once the history is merged, git will behave as if it is one big repo, and it should still be possible to push from that to Gentoo as the head is untouched. Merging the history will remove the gpg signature on the initial gentoo commit (since it is being modified to do the graft).

### [][Preventing \'git repack -a\' from touching huge packs]

Normally [git repack -a] (invoked by [git gc]) tries to repack everything into a single pack. If the local repository contains a few huge packs already (commits from initial clone, grafted history pack), the repack can take really long and be truly memory-consuming.

To avoid that, mark the huge pack files for keeping. In this case, [git repack -a] won\'t touch those packs and instead focus on repacking everything else. As a result, you can get most of the benefits of repacking with major time saving.

`user `[`$`]`cd .git/refs/packs`

`user `[`$`]`ls -lh`

    total 2.2G
    -r--r--r-- 1 mgorny mgorny  17M Oct  3 16:14 pack-05c10cc8ef170fd182619ef32ec4007e5f32f46d.idx
    -r--r--r-- 1 mgorny mgorny 219M Oct  5 16:12 pack-05c10cc8ef170fd182619ef32ec4007e5f32f46d.pack
    -r--r--r-- 1 mgorny mgorny  27K Oct  5 14:09 pack-107a6ca6e4b781d12cc452a651a478daac3b3d95.idx
    -r--r--r-- 1 mgorny mgorny 978K Oct  5 16:12 pack-107a6ca6e4b781d12cc452a651a478daac3b3d95.pack
    -r--r--r-- 1 mgorny mgorny  25K Oct  6 08:14 pack-10f2b4a18cd1a99dcbc502987eb130680221b558.idx
    -r--r--r-- 1 mgorny mgorny 770K Oct  6 08:14 pack-10f2b4a18cd1a99dcbc502987eb130680221b558.pack
    -r--r--r-- 1 mgorny mgorny 197M Oct  3 18:06 pack-412c2dda845a79854872afaf5f9cd4ea896aef38.idx
    -r--r--r-- 1 mgorny mgorny 1.7G Oct  3 18:05 pack-412c2dda845a79854872afaf5f9cd4ea896aef38.pack
    -r--r--r-- 1 mgorny mgorny 5.1K Oct  5 15:38 pack-460c1a0fc0e6fc76d367e2b4010c879ce9b062e2.idx
    -r--r--r-- 1 mgorny mgorny 187K Oct  5 16:12 pack-460c1a0fc0e6fc76d367e2b4010c879ce9b062e2.pack
    -r--r--r-- 1 mgorny mgorny 1.4M Oct  6 08:49 pack-5a593371028f920159f628208955707a9153962a.idx
    -r--r--r-- 1 mgorny mgorny  24M Oct  6 08:49 pack-5a593371028f920159f628208955707a9153962a.pack
    -r--r--r-- 1 mgorny mgorny  14K Oct  4 08:41 pack-c90e9378fa114d9a603c3ea40c4ff76e2d4cbac6.idx
    -r--r--r-- 1 mgorny mgorny 401K Oct  5 16:12 pack-c90e9378fa114d9a603c3ea40c4ff76e2d4cbac6.pack

Once you identify the huge packs you\'d like to keep (`05c10cc8ef170fd182619ef32ec4007e5f32f46d` and `412c2dda845a79854872afaf5f9cd4ea896aef38` in this case), create [.keep] files for them:

`user `[`$`]`touch pack-05c10cc8ef170fd182619ef32ec4007e5f32f46d.keep pack-412c2dda845a79854872afaf5f9cd4ea896aef38.keep`

### [Retaining commit author information]

It is important that appropriate credit is given when committing on behalf of others. Git can natively differentiate between who authored a commit and who pushed it ([example](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=f6485aff0129ae4c8df5a211af1a51d03ecb6de4)), and most methods of merging handle this automatically.

If you have applied someone else\'s changes manually or made local edits to a PR, check that the author field is accurate:

`user `[`$`]`git log --format=fuller`

If necessary, amend the commit to give credit where it is due:

`user `[`$`]`git commit --amend --author="Joe Smith <jsmith@example.org>"`

If it is necessity to credit several authors, add trailer lines like `Co-authored-by: Name Surname <nsurname@example.org>` (as currently supported by major Git hosts like GitHub and GitLab) to the long commit description part:

    app-misc/foo: version bump to 0.5

    Bump to 0.5. This also fixes security
    bug 93829 and introduces the new USE flag 'bar'.

    Bug: https://bugs.gentoo.org/93829
    Acked-by: Hans Wurst <hans@gentoo.org>
    Co-authored-by: Jane Doe <jdoe@example.org>
    Reported-by: Alice Wonderland <alice@foo.com>
    Signed-off-by: Joe Smith <jsmith@example.org>
    Signed-off-by: A Developer <example@gentoo.org>

### [A cli-tool to crawl through pull requests]

[gengee](https://github.com/wimmuskee/gengee) is a tool that makes queries through [[gentoo/gentoo/] pull requests](https://github.com/gentoo/gentoo/pulls). It can show \"outdated\" pull requests, ie where a newer version is added to ::gentoo tree, where a linked bug is already closed, or where package in question has been removed from ::gentoo. You can use it to query pull requests assigned to certain maintainers, or opened by certain authors.

`user `[`$`]`gengee-query -m python@gentoo.org`

`user `[`$`]`gengee-query -a juippis`

`user `[`$`]`gengee-query -l "need assignment"`

and so much more.

Check the homepage for an ebuild, info on how to set it up and documentation on how to use it.

### [][Automatic git pull/rebase merge involving conflicts with KEYWORDS]

[gentoolkit](https://packages.gentoo.org/packages/app-portage/gentoolkit) above version 0.50 has a tool called [merge-driver-ekeyword] which can be utilized as a git\'s merge driver for conflicts with KEYWORDS in ebuilds. This is especially handy for any arch tester. Please see the [original announcement](https://archives.gentoo.org/gentoo-dev/message/b4fb2bf79a7df1933601606a40abe215).

To utilize the tool, browse to your development repository\'s location, and add these to [./.git/config]

[FILE] **`./.git/config`**

    [merge "keywords"]
    name = KEYWORDS merge driver
    driver = merge-driver-ekeyword %O %A %B %P

And add the following into [./.git/info/attributes]

[FILE] **`./.git/info/attributes`**

    *.ebuild merge=keywords

## [See also]

-   [Standard git workflow](https://wiki.gentoo.org/wiki/Standard_git_workflow "Standard git workflow") --- describing a **modern git workflow** for contributing to Gentoo, with [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") and [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev")
-   [GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests") --- how to contribute to Gentoo by creating [pull requests on GitHub](https://github.com/gentoo/gentoo/pulls).
-   [Git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")
-   [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") --- a [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")-based QA utility for ebuild repos.
-   [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.
-   [Project:Infrastructure/Git_migration](https://wiki.gentoo.org/wiki/Project:Infrastructure/Git_migration "Project:Infrastructure/Git migration")
-   [Project:Repository_mirror_and_CI](https://wiki.gentoo.org/wiki/Project:Repository_mirror_and_CI "Project:Repository mirror and CI")
-   [Gentoo on Codeberg](https://www.gentoo.org/news/2026/02/16/codeberg.html)

## [External resources]

-   [Git Tutorial by Lars Vogel](http://www.vogella.com/tutorials/Git/article.html)
-   [Tips and Tricks on gitready](http://gitready.com/)
-   [kernel patch guideline](https://www.kernel.org/doc/Documentation/process/submitting-patches.rst)
-   [gentoo gitweb](https://gitweb.gentoo.org/repo/gentoo.git)
-   [gentoo github mirror](https://github.com/gentoo/gentoo)
-   [https://github.com/gentoo-mirror/gentoo](https://github.com/gentoo-mirror/gentoo) - Gentoo repository on [Gentoo repository mirrors](https://github.com/gentoo-mirror)

## [][And summarizing it all, \...]

[http://xkcd.com/1597/](http://xkcd.com/1597/)