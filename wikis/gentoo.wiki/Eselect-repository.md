This page contains [[changes](https://wiki.gentoo.org/index.php?title=Eselect/Repository&oldid=1260304&diff=1389052)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Eselect/Repository/es "Eselect/Repository (12% translated)")
-   [français](https://wiki.gentoo.org/wiki/Eselect/Repository/fr "Eselect/Repository (12% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Eselect/Repository/hu "Eselect/Repository (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Eselect/Repository/ru "eselect/repository (96% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Eselect/Repository/ta "eselect/repository/ta (21% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Eselect/Repository/zh-cn "Eselect/Repository (83% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Eselect/Repository/ja "eselect/repository (100% translated)")

**Resources**

[[]][GitHub](https://github.com/mgorny/eselect-repository)

[[]][Package information](https://packages.gentoo.org/packages/app-eselect/eselect-repository)

[eselect-repository] is an [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") module for configuring [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). Ebuild repository configuration files are stored in [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")].

** See also**\
For further options see [man repository.eselect].

** Note**\
This utility supersedes [layman](https://wiki.gentoo.org/wiki/Layman "Layman") for listing, configuring, and handling synchronization of alternate repositories. There are still some exceptions for which layman can supplement eselect-repository, when using version control systems that Portage does not natively sync (e.g. darcs and g-sorcery).

[eselect-repository] is written and maintained by Gentoo\'s [Michał Górny (mgorny)](https://wiki.gentoo.org/wiki/User:MGorny "User:MGorny") .

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Initial setup]](#Initial_setup)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [repos.gentoo.org]](#repos.gentoo.org)
        -   [[3.1.1] [Listing ebuild repositories registered with repos.gentoo.org]](#Listing_ebuild_repositories_registered_with_repos.gentoo.org)
        -   [[3.1.2] [Add ebuild repositories from repos.gentoo.org]](#Add_ebuild_repositories_from_repos.gentoo.org)
    -   [[3.2] [Add repositories]](#Add_repositories)
    -   [[3.3] [Disable repositories without removing contents]](#Disable_repositories_without_removing_contents)
    -   [[3.4] [Disable repositories and remove contents]](#Disable_repositories_and_remove_contents)
    -   [[3.5] [Create a new ebuild repository]](#Create_a_new_ebuild_repository)
-   [[4] [See also]](#See_also)

## [[] Installation]

### [USE flags]

### [USE flags for] [app-eselect/eselect-repository](https://packages.gentoo.org/packages/app-eselect/eselect-repository) [[]] [Manage repos.conf via eselect]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+git`](https://packages.gentoo.org/useflags/+git)             Enable git (version control system) support
  [`mercurial`](https://packages.gentoo.org/useflags/mercurial)   Support mercurial sync-type.
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 06:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

`root `[`#`]`emerge --ask app-eselect/eselect-repository`

## [[] Configuration]

### [[] Initial setup]

The [repos.conf] file or directory as configured by the `REPOS_CONF` variable in [/etc/eselect/repository.conf], must exist before the module will function properly. The [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Defining_a_custom_repository "Handbook:AMD64/Portage/CustomTree") prefers to have it as a directory, and some tools will not work otherwise:

`root `[`#`]`mkdir -p /etc/portage/repos.conf`

### [[] Files]

Paths and options can be changed in [/etc/eselect/repository.conf]. This file has comments and is self-explanatory.

## [[] Usage]

** Tip**\
Repositories can be synced after being configured, using Portage\'s [emaint](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository"):

`root `[`#`]`emaint sync -r foo`

### [[] repos.gentoo.org]

Gentoo allows users and developers to register [repositories on repos.gentoo.org](https://repos.gentoo.org/), for public consumption. [eselect repository] will fetch and read the known list.

#### [[] Listing ebuild repositories registered with repos.gentoo.org]

[eselect repository] can print all repositories listed on repos.gentoo.org:

`user `[`$`]`eselect repository list`

    Available repositories:
      [1]   foo
      [2]   bar
      [3]   baz
      [4]   cross #
      [5]   good *
      [6]   my_overlay @

-   Installed, enabled repositories are suffixed with a \* character.
-   Repositories suffixed with #, need their sync information updated (via disable/enable) or were customized by the user.
-   Repositories suffixed with @ are not listed by name in the official, published list.

\
Use the `-i` option to show currently configured repositories only:

`user `[`$`]`eselect repository list -i`

#### [[] Add ebuild repositories from repos.gentoo.org]

Syntax: enable (\<name\>\|\<index\>)\...

`root `[`#`]`eselect repository enable foo bar baz`

### [[] Add repositories]

Syntax:

`root `[`#`]`eselect repository add <name> <sync-type> <sync-uri>`

The most common sync methods are git and rsync. Other options are cvs, mercurial, svn, websync and zipfile.

The formats and required packages are as follows:

git [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] installed by default

`root `[`#`]`eselect repository add test git https://github.com/test/test.git`

rsync [[[net-misc/rsync]](https://packages.gentoo.org/packages/net-misc/rsync)[]] installed by default

`root `[`#`]`eselect repository add test rsync rsync://example.com/path`

mercurial [[[dev-vcs/mercurial]](https://packages.gentoo.org/packages/dev-vcs/mercurial)[]]

`root `[`#`]`eselect repository add test hg https://example.com/path`

*Note that eselect/repository needs to be compiled with the \`mercurial\` USE flag.*

cvs [[[dev-vcs/cvs]](https://packages.gentoo.org/packages/dev-vcs/cvs)[]]

`root `[`#`]`eselect repository add test cvs :ext:anoncvs@example.com:/var/cvsroot`

svn [[[dev-vcs/subversion]](https://packages.gentoo.org/packages/dev-vcs/subversion)[]]

`root `[`#`]`eselect repository add test svn https://example.com/repos/name/trunk`

webrsync installed with portage, [[[app-portage/emerge-delta-webrsync]](https://packages.gentoo.org/packages/app-portage/emerge-delta-webrsync)[]] can be installed to reduce bandwidth usage.

`root `[`#`]`eselect repository add test webrsync https://example.com/path`

zipfile installed by default

`root `[`#`]`eselect repository add test zipfile https://example.com/file.zip`

To sync the new repository which is called test in this example, however change this to match the name of the repository that is set.

`root `[`#`]`emaint sync --repo test`

For more information on synchronization in Gentoo, please see [Ebuild_repository](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") before use.

** Warning**\
While the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") is either written or [reviewed](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") by Gentoo developers, and the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository has some developer oversight, that is not always the case for other ebuild repositories. It is possible that some ebuilds repositories might contain vulnerable, badly broken or, theoretically, even malicious software.

### [[] Disable repositories without removing contents]

Syntax: disable \[-f\] (\<name\>\|\<index\>)\...

`root `[`#`]`eselect repository disable foo bar`

The `-f` option is required for repositories not registered with repos.gentoo.org, and those without sync attributes. Use with care.

### [[] Disable repositories and remove contents]

Syntax: remove \[-f\] (\<name\>\|\<index\>)\...

`root `[`#`]`eselect repository remove bar baz`

The `-f` option is required for repositories not registered with repos.gentoo.org, and those without sync attributes. Use with care.

### [[] Create a new ebuild repository]

The create subcommand will [create an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") skeleton, and configure it with Portage:

Syntax: create \<name\> \[\\]

`root `[`#`]`eselect repository create <ebuild_repository_name>`

    Adding <ebuild_repository_name> to /etc/portage/repos.conf ...
    Repository <ebuild_repository_name> created and added

## [[] See also]

-   [Eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect") --- a tool for administration and configuration on Gentoo systems.
-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").
-   [Project:Portage/Sync](https://wiki.gentoo.org/wiki/Project:Portage/Sync "Project:Portage/Sync")