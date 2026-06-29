Attempt at describing a **modern git workflow** for contributing to Gentoo, with [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") and [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev").

This tries to be an alternative to the [Gentoo git workflow](https://wiki.gentoo.org/wiki/Gentoo_git_workflow "Gentoo git workflow") page which acts as more of a reference than a guide or tutorial.

## Contents

-   [[1] [Tools]](#Tools)
-   [[2] [Checking for issues]](#Checking_for_issues)
-   [[3] [Committing changes]](#Committing_changes)
    -   [[3.1] [pkgdev]](#pkgdev)
    -   [[3.2] [pkgcommit]](#pkgcommit)
    -   [[3.3] [Examples]](#Examples)
        -   [[3.3.1] [Preparing a working repository]](#Preparing_a_working_repository)
        -   [[3.3.2] [Bumping app-misc/scrub]](#Bumping_app-misc.2Fscrub)
    -   [[3.4] [Contributing the change]](#Contributing_the_change)
        -   [[3.4.1] [Fixing the inevitable]](#Fixing_the_inevitable)
    -   [[3.5] [Bumping app-misc/scrub without pkgdev]](#Bumping_app-misc.2Fscrub_without_pkgdev)
-   [[4] [Updating an outdated branch]](#Updating_an_outdated_branch)
-   [[5] [See Also]](#See_Also)
-   [[6] [External resources]](#External_resources)

## [Tools]

The previous tooling, [repoman], handled both QA scanning as well as acting as a commit helper.

The new workflow is split into two major components:

1.  scanning for QA issues (pkgcheck)
2.  committing the changes (pkgdev, or the far more spartan [pkgcommit] if desired)

First, install these essential tools:

`root `[`#`]`emerge --ask dev-util/pkgcheck dev-util/pkgdev`

Optionally, install these bits:

-   [[[app-portage/mgorny-dev-scripts]](https://packages.gentoo.org/packages/app-portage/mgorny-dev-scripts)[]] for additional helpers like [pkgdiff-mg] to [diff] (build system) changes between versions. Their use is optional but it\'s worth reading over the [list](https://github.com/mgorny/mgorny-dev-scripts#mgorny-dev-scripts) available.
-   [[[app-portage/iwdevtools]](https://packages.gentoo.org/packages/app-portage/iwdevtools)[]] for file diff (compare old/new, check if e.g. files now missing), [rcd] helper to navigate packages, detecting missing dependencies via ELF NEEDED, etc.

`root `[`#`]`emerge --ask app-portage/mgorny-dev-scripts app-portage/iwdevtools`

## [Checking for issues]

pkgcheck is a QA scanning tool equivalent to the \"check\" part of repoman. Its main use is [pkgcheck scan] (equivalent to [repoman full -dx]).

See [pkgcheck#Examples](https://wiki.gentoo.org/wiki/Pkgcheck#Examples "Pkgcheck").

## [Committing changes]

### [pkgdev]

pkgdev is a commit helper, equivalent to the \"commit\" part of repoman.

Its main uses are:

-   [pkgdev commit] (equivalent to [repoman commit]), and
-   [pkgdev manifest] (equivalent to [repoman manifest])

See [pkgdev#Examples](https://wiki.gentoo.org/wiki/Pkgdev#Examples "Pkgdev").

### [pkgcommit]

[pkgcommit] is a [helper tool](https://github.com/mgorny/mgorny-dev-scripts#pkgcommit) from [[[app-portage/mgorny-dev-scripts]](https://packages.gentoo.org/packages/app-portage/mgorny-dev-scripts)[]]. It is not part of the pkgcore suite. It just generates the commit summary based on the current directory (no \"smart generation\" based on the actual changes like pkgdev).

### [Examples]

The overall [method](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds#Demonstration_by_example "Basic guide to write Gentoo Ebuilds") is always the same:

1.  Enter a repository
2.  Navigate to a package (using [[[app-misc/scrub]](https://packages.gentoo.org/packages/app-misc/scrub)[]] as an example)
3.  Make some changes
4.  Run [pkgdev commit] (recommended) or alternatively [pkgcommit]

#### [Preparing a working repository]

First, create a fork of ::gentoo under current user. Afterwards, clone ::gentoo locally, and add a fork as a remote:

`user `[`$`]`git clone git@github.com:gentoo/gentoo.git ~/git/gentoo `

`user `[`$`]`git remote add $ git@github.com:$/gentoo.git `

#### [][Bumping app-misc/scrub]

** Tip**\
Using [[[app-portage/iwdevtools]](https://packages.gentoo.org/packages/app-portage/iwdevtools)[]], a shortcut tool [rcd] can be used to quickly jump to a package.

This example uses [pkgdev]. When calling [pkgdev commit], it calls [pkgcheck scan] automatically.

First, enter the repository the old fashioned way, or through [rcd]:

`user `[`$`]`cd ~/git/gentoo/app-misc/scrub `

`user `[`$`]`rcd scrub # equivalent as above `

Install the dependencies of the package:

`root `[`#`]`emerge -av1o --with-test-deps app-misc/scrub`

Copy the old ebuild as a basis for new changes and regenerate the Manifest:

`user `[`$`]`cp scrub-2.6.0.ebuild scrub-2.6.1.ebuild `

`user `[`$`]`pkgdev manifest`

Go read the upstream release notes! Then compare the build system changes using [pkgdiff-mg -b] from [[[app-portage/mgorny-dev-scripts]](https://packages.gentoo.org/packages/app-portage/mgorny-dev-scripts)[]].

`user `[`$`]`pkgdiff-mg -b scrub-2.6.0.ebuild scrub-2.6.1.ebuild`

Adapt the ebuild as needed:

`user `[`$`]`$EDITOR scrub-2.6.1.ebuild`

Optionally run [pkgcheck scan] to check for QA issues during the work/change process:

`user `[`$`]`pkgcheck scan`

Test it out (repeat as necessary, delete any [/var/tmp/portage/app-misc/scrub-2.6.1] directory as root, if it complains about permissions):

`user `[`$`]`ebuild scrub-2.6.1.ebuild clean test install`

When working locally, it is possible to try to merge it\... but there might be permission issues, since Portage drops privileges to the portage user:

`root `[`#`]`ebuild scrub-2.6.1.ebuild merge`

Try running the tool too (ideally *use* it):

`user `[`$`]`scrub --version`

    scrub version 2.6.1

Commit the changes once ready (note that the command from the commit command shows [pkgcheck scan] results):

`user `[`$`]`git add scrub-2.6.1.ebuild && pkgdev commit `

    app-misc/scrub
      DeprecatedEapi: version 2.6.0: uses deprecated EAPI 6
      RedundantVersion: version 2.6.0: slot(0) keywords are overshadowed by version: 2.6.1
    [master 65b81235dc06d] app-misc/scrub: add 2.6.1
     2 files changed, 17 insertions(+)
     create mode 100644 app-misc/scrub/scrub-2.6.1.ebuild

If rev-bumping an ebuild, make sure to remove the outdated revision:

`user `[`$`]`git add scrub-2.6.1-r1.ebuild && git rm scrub-2.6.1.ebuild`

### [Contributing the change]

Afterwards it is possible to push the commit to it with pkgdev as follows:

`user `[`$`]`pkgdev push $ `

Now a [PR](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests#Step_3:_User_makes_a_pull_request "GitHub Pull Requests") may be asked for from the local repo to ::gentoo.

#### [Fixing the inevitable]

Some mistakes are common on the way of contribution, and things will have to be rebased for them to be accepted.

Reuse the last commit, rebase all new changes into a single commit:

`user `[`$`]`git commit -C HEAD `

`user `[`$`]`` git rebase -i origin/HEAD # or check the correct commit with `git log`  ``

** Tip**\
Work on a new branch before doing any patching to make life easier! Create and go to a new branch with [git checkout -b my_very_special_changes], and when done, simply return with [git checkout master].

The git rebase command will open the [\$EDITOR], where there will probably be two [pick] lines. Change the first line to [reword] and the second line to [fixup]. Aftewards, it can be pushed to the local repo again:

`user `[`$`]`git push $ `

If a commit is accidentally pushed without rebasing it, simply [git push \--force \$ ] to the local repo. It\'s not the end of the world.

### [][Bumping app-misc/scrub without pkgdev]

[mgorny](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") describes on his blog an [alternative workflow](https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/) (from before pkgdev was created) based on [pkgcommit] and [pkgcheck scan \--commits].

It can be roughly summarized as:

1.  Make changes
2.  [pkgcommit]
3.  [pkgcheck scan \--commits]
4.  Make changes based on pkgcheck output
5.  [git-fixup]
6.  [pkgcheck scan \--commits]
7.  \...
8.  Once done, [git rebase -i \--autosquash]

## [Updating an outdated branch]

Sometimes a Pull Request can become stale and depend on new dependencies or USE flags not currently in the forked branch. This can potentially result in thousands of commits being accidentally pushed to the Pull Request if it is not properly backtracked and updated.

First, reset the branch (in this example, the feature branch) to the last commit from the master branch (in this example, it was one commit ago):

`user `[`$`]`git reset --soft HEAD~1`

Stash the working changes:

`user `[`$`]`git stash`

Now, checkout master and fetch the new changes into the desired branch:

`user `[`$`]`git checkout master`

`user `[`$`]`git fetch origin master:feature`

Next, checkout the feature branch again and pop the stash:

`user `[`$`]`git checkout feature`

`user `[`$`]`git stash pop`

Finally, commit the new changes on top of the updated feature branch:

`user `[`$`]`pkgdev commit --signoff`

## [See Also]

-   [GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests") --- how to contribute to Gentoo by creating [pull requests on GitHub](https://github.com/gentoo/gentoo/pulls).
-   [Gentoo git workflow](https://wiki.gentoo.org/wiki/Gentoo_git_workflow "Gentoo git workflow") --- outlines some rules and best-practices regarding the typical workflow for ebuild developers using [git].
-   [Pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") --- a [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")-based QA utility for ebuild repos.
-   [Pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.

## [External resources]

-   [https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/](https://blogs.gentoo.org/mgorny/2019/12/12/a-better-ebuild-workflow-with-pure-git-and-pkgcheck/)