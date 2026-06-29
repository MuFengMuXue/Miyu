[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (has introduction section, not following blueprint). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[Live ebuilds](https://wiki.gentoo.org/wiki/Live_ebuilds "Live ebuilds") pull directly from upstream VCS, meaning either regressions can be introduced by recent changes not yet in a release, or that one may wish to make use of properties of the VCS (like branches or tags being available). Either way, using *git bisect* with this can be desirable.

This article makes use of some features of *git-r3.eclass* as well as *git bisect*.

Using live ebuilds and [git bisect] can be enormously helpful for debugging issues. This debugging tactic approach is possible for any ebuilds with a version number of \*-9999.

## Contents

-   [[1] [Fundamentals]](#Fundamentals)
-   [[2] [Examples]](#Examples)
    -   [[2.1] [ZFS]](#ZFS)
    -   [[2.2] [GCC example]](#GCC_example)
-   [[3] [Using git bisect run]](#Using_git_bisect_run)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Fundamentals]

The core thing to know is that *git-r3.eclass* allows users to override the repository, branch, tag, or commit used when checking out. This can be used to drive a git bisect either manually or with a script (using *git bisect run*).

When unpacking (at which time fetching is done for live ebuilds), the eclass prints the relevant variables for a particular package. These are:

-   `EGIT_OVERRIDE_REPO_XYZ`
-   `EGIT_OVERRIDE_BRANCH_XYZ`
-   `EGIT_OVERRIDE_COMMIT_XYZ`
-   `EGIT_OVERRIDE_COMMIT_DATE_XYZ`

where *XYZ* is replaced by the normalized version of the URL, excluding the domain part (e.g. \"[https://github.com/openzfs/zfs](https://github.com/openzfs/zfs)\" ends up being OPENZFS_ZFS). These can be set to point to the candidate selected by [git bisect] for testing.

It is recommended that one clones the repository separately and points the ebuild to that using `EGIT_OVERRIDE_REPO_XYZ` rather than trying to drive the whole thing using the clone in [/var/cache/distfiles/git-r3] as it isn\'t checked out in the normal fashion, then run [git bisect start], [git bisect bad some-bad-commit-or-tag], and [git bisect good some-good-commit-or-tag] in there.

## [Examples]

### [ZFS]

Suppose one hits a regression in ZFS. In this example, between ZFS 2.1.4 (last known good version) and ZFS 2.1.6 (being the latest version where a bug is hit).

First, clone ZFS at the `zfs-2.1.5-staging` branch:

`user `[`$`]`git clone `[`https://github.com/openzfs/zfs`](https://github.com/openzfs/zfs)` -b zfs-2.1.5-staging`

Start the bisect:

`user `[`$`]`cd zfs `

`user `[`$`]`git bisect start `

`user `[`$`]`git bisect bad zfs-2.1.5 `

`user `[`$`]`git bisect good zfs-2.1.4`

Create a simple script to allow easily building each commit:

[FILE] **`/tmp/test-zfs.sh`**

    #!/bin/bash

    # EGIT_OVERRIDE_*_* come from the messages shown when fetching a live ebuild, see also bug 764422
    # In this case, OPENZFS_ZFS corresponds to the repository location being cloned from:
    #  github.com/openzfs/zfs
    # This shows up when unpacking as..
    #     >>> Unpacking source...
    #     * Repository id: openzfs_zfs.git
    #     * To override fetched repository properties, use:
    #     *   EGIT_OVERRIDE_REPO_OPENZFS_ZFS
    #     *   EGIT_OVERRIDE_BRANCH_OPENZFS_ZFS
    #     *   EGIT_OVERRIDE_COMMIT_OPENZFS_ZFS
    #     *   EGIT_OVERRIDE_COMMIT_DATE_OPENZFS_ZFS
    #     *
    #     * Fetching https://github.com/openzfs/zfs.git .
    #
    # We want to build the specific commit 'git bisect' has told us to
    export EGIT_OVERRIDE_COMMIT_OPENZFS_ZFS=$(git rev-parse HEAD)
    export EGIT_OVERRIDE_BRANCH_OPENZFS_ZFS=zfs-2.1.5-staging
    # Make sure the live ebuild can be used
    export ACCEPT_KEYWORDS="**"
    # Build the live ebuilds
    emerge -v1 sys-fs/zfs

    echo "If this version is good (need to reboot), run 'git bisect good'."
    echo "If this version is bad (need to reboot), run 'git bisect bad'."

Run [/tmp/test-zfs.sh] repeatedly.

After each run of [emerge] by the script, test out ZFS by rebooting. If it worked, type [git bisect good]. If the bug remained, type [git bisect bad]. Continue until the first bad commit is identified.

\

### [GCC example]

See [GCC/git_bisect](https://wiki.gentoo.org/wiki/GCC/git_bisect "GCC/git bisect").

## [Using git bisect run]

[git bisect] has a \'run\' subcommand which allows running a command or script to determine if a commit is good or bad. Its use isn\'t required but it is handy once the process is familiar to the user. See [https://lwn.net/Articles/317154/](https://lwn.net/Articles/317154/) for more detail.

For example, if [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] is failing in its last-minute sanity-check in `pkg_preinst`, it\'s sufficient to use the following script with the glibc git repository:

[FILE] **`/tmp/test-glibc.sh`**

    #!/bin/bash

    # We want to build the specific commit 'git bisect' has told us to
    export EGIT_OVERRIDE_COMMIT_GLIBC=$(git rev-parse HEAD)
    # Override the default (master) to be the 2.35 release branch
    export EGIT_OVERRIDE_BRANCH_GLIBC=release/2.35/master
    # Allow use of live ebuilds
    export ACCEPT_KEYWORDS="**"
    #USE="vanilla" ...
    emerge -v1 sys-libs/glibc || exit 1

## [See also]

-   [Kernel git-bisect](https://wiki.gentoo.org/wiki/Kernel_git-bisect "Kernel git-bisect") --- a [Git](https://wiki.gentoo.org/wiki/Git "Git") tool to find the commit that caused problems between versions.
-   [Project:Toolchain](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain") --- manages gcc, binutils, glibc, and other toolchain-related packages.

## [External resources]

-   [Git Bisect with Gentoo and Systemd](https://ebadblog.com/git-bisect-with-gentoo-and-systemd)