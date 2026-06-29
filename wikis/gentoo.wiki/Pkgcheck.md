**Resources**

[[]][Home](https://github.com/pkgcore/pkgcheck#pkgcheck)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/pkgcheck)

**pkgcheck** is a [pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")-based QA utility for ebuild repos.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [Examples]](#Examples)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [error: repos.conf: default repo \'gentoo\' is undefined or invalid]](#error:_repos.conf:_default_repo_.27gentoo.27_is_undefined_or_invalid)
    -   [[5.2] [failed retrieving origin/HEAD commit hash for git repo]](#failed_retrieving_origin.2FHEAD_commit_hash_for_git_repo)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/pkgcheck`

## [Configuration]

Upstream\'s documentation [describes](https://pkgcore.github.io/pkgcheck/man/pkgcheck.html#config-file-support) the config file format and locations.

For example, a configuration file for the current user:

[FILE] **`~/.config/pkgcheck/pkgcheck.conf`**

    [DEFAULT]
    # Enable PerlCheck to the default list of checks (it's not enabled by default upstream)
    checks = +PerlCheck
    # Disable two noisy keywords (checks)
    keywords = -UnstableOnly,-PotentialStable

    [gentoo]
    # Enable network checks when scanning in the 'gentoo' repository with a timeout of 15 seocnds
    # Examples: check for HOMEPAGE which 404s, or for a HTTP -> HTTPS redirect
    net =
    timeout = 15

## [Usage]

The upstream repository [covers usage](https://github.com/pkgcore/pkgcheck#usage) briefly.

pkgcheck has the following subcommands:

-   [pkgcheck scan] - this is the most common command needed: scans the current directory (can take arguments instead) for QA issues
    -   [pkgcheck scan \--net] - enables checks that require network access (can fail if scanning lots of packages).
    -   [pkgcheck scan \--commits] - same as [pkgcheck scan] but restricted to changes in local unpushed commits. Enables additional checks which require more context (like commit message format/length, pushing straight-to-stable, etc).
-   [pkgcheck show] - this lists all possible results (try [pkgcheck show \--checks] etc to find things to disable or change severity of locally if desired)

## [Examples]

The most common pattern is to enter a repository, navigate to a package (using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] as an example), and run [pkgcheck scan], like so:

`user `[`$`]`cd ~/git/gentoo/sys-kernel/gentoo-sources `

`user `[`$`]`pkgcheck scan `

    sys-kernel/gentoo-sources
      DroppedKeywords: version 5.18.11: m68k

To scan packages per maintainer, one could try:

`user `[`$`]`cd ~/git/gentoo `

`user `[`$`]`git grep -l "python@gentoo.org" */*/metadata.xml | cut -d/ -f1-2 | pkgcheck scan - `

    app-arch/brotli
      PythonCompatUpdate: version 1.0.9-r3: PYTHON_COMPAT update available: python3_11
      StableRequest: version 1.0.9-r4: slot(0) no change in 45 days for unstable keywords: [ ~amd64, ~arm, ~arm64, ~hppa, ~ppc, ~ppc64, ~sparc, ~x86 ]

    app-text/cssmin
      PythonCompatUpdate: version 0.2.0: PYTHON_COMPAT update available: python3_11

Or to specifically only check for packages which may be due a [stabilization request](https://wiki.gentoo.org/wiki/Stable_request "Stable request"):

`user `[`$`]`cd ~/git/gentoo `

`user `[`$`]`git grep -l "python@gentoo.org" */*/metadata.xml | cut -d/ -f1-2 | pkgcheck scan -k StableRequest - `

    app-arch/brotli
      StableRequest: version 1.0.9-r4: slot(0) no change in 45 days for unstable keywords: [ ~amd64, ~arm, ~arm64, ~hppa, ~ppc, ~ppc64, ~sparc, ~x86 ]

To get only specific errors:

`user `[`$`]`pkgcheck scan --keywords DoubleEmptyLine `

    app-admin/agru
      DoubleEmptyLine: version 0.1.10: ebuild has unneeded empty line on line: 13

    app-admin/himitsu
      DoubleEmptyLine: version 0.7: ebuild has unneeded empty line on line: 20
      DoubleEmptyLine: version 0.8: ebuild has unneeded empty line on line: 20
      DoubleEmptyLine: version 9999: ebuild has unneeded empty line on line: 20

## [Troubleshooting]

### [][error: repos.conf: default repo \'gentoo\' is undefined or invalid]

See [[[bug #730502]](https://bugs.gentoo.org/show_bug.cgi?id=730502)[]]. This is caused by having a [/etc/portage/repos.conf] defined without mentioning the gentoo repository.

If [/etc/portage/repos.conf] is a directory:

`root `[`#`]`cp /usr/share/portage/config/repos.conf /etc/portage/repos.conf/gentoo.conf`

Alternatively, if it\'s a file:

`root `[`#`]`cat /usr/share/portage/config/repos.conf >> /etc/portage/repos.conf`

### [][failed retrieving origin/HEAD commit hash for git repo]

See the upstream [documentation](https://pkgcore.github.io/pkgcheck/man/pkgcheck.html#git) on git support.

Run [git remote set-head origin master].

## [See also]

-   [Standard git workflow](https://wiki.gentoo.org/wiki/Standard_git_workflow "Standard git workflow") --- describing a **modern git workflow** for contributing to Gentoo, with [pkgcheck] and [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev")
-   [Gentoo git workflow](https://wiki.gentoo.org/wiki/Gentoo_git_workflow "Gentoo git workflow") --- outlines some rules and best-practices regarding the typical workflow for ebuild developers using [git].
-   [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.
-   [Repoman](https://wiki.gentoo.org/wiki/Repoman "Repoman") --- a Python program used to enforce a minimal level of quality assurance in [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") and related metadata added to [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

## [External resources]

-   [Devmanual](https://devmanual.gentoo.org/ebuild-maintenance/git/#committing-to-gentoo.git)