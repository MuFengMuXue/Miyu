**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:PkgCore "Project:PkgCore")][Project](https://wiki.gentoo.org/wiki/Project:PkgCore "Project:PkgCore")

[[]][GitHub](https://github.com/pkgcore/pkgcore)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/pkgcore)

[[]][Official documentation](https://pkgcore.github.io/pkgcore/)

**pkgcore** is an alternative package manager for Gentoo that aims for high performance, extensibility, and a clean design. Written in Python, pkgcore provides an alternative to Portage\'s [emerge] command while also subsuming most of the functionality of the [[eix](https://wiki.gentoo.org/wiki/Eix "Eix")] and [[eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository")] repository management tools.

** Warning**\
pkgcore is still experimental and care should be taken when updating a system

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Updating the system]](#Updating_the_system)
    -   [[3.2] [Searching for a package]](#Searching_for_a_package)
    -   [[3.3] [Installing a package]](#Installing_a_package)
-   [[4] [Removal]](#Removal)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Use the following [emerge] command to install the [[[sys-apps/pkgcore]](https://packages.gentoo.org/packages/sys-apps/pkgcore)[]] package:

`root `[`#`]`emerge --ask sys-apps/pkgcore`

## [Configuration]

If there is no specific pkgcore configuration (that is [/etc/pkgcore.conf] or [\~/.pkgcore.conf]), it reads the Portage configuration and converts it transparently for use. For a detailed explanation of how the pkgcore specific configuration works see [Pkgcore/Configuration](https://wiki.gentoo.org/wiki/Pkgcore/Configuration "Pkgcore/Configuration").

When pkgcore is working in Portage compatibility mode, if [/etc/portage/repos.conf] is defined without mentioning the gentoo repository, which Portage can infer, pkgcore will fail. Refer to [Troubleshooting pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck#error:_repos.conf:_default_repo_.27gentoo.27_is_undefined_or_invalid "Pkgcheck") to move the gentoo repository\'s definition to Portage\'s [repos.conf].

## [Usage]

** Warning**\
[pmerge] is outdated, use at your own risk. use [emerge] instead.

### [Updating the system]

For synchronizing the local copies of the Portage tree and any overlays the [pmaint] utility is used. Then [pmerge] is invoked to update all packages and clean superfluous packages.

`root `[`#`]`pmaint sync `

`root `[`#`]`pmerge --ask --upgrade --deep --newuse `

`root `[`#`]`pmerge --ask --clean --with-bdeps `

### [Searching for a package]

To search for a package use the pquery program:

`user `[`$`]`pquery -nv <query>`

For example, to find some audio software for encoding [ogg] files, one may use the following to find [[[media-sound/vorbis-tools]](https://packages.gentoo.org/packages/media-sound/vorbis-tools)[]].

`user `[`$`]`pquery -nv --description ogg 'media-sound/*'`

** Note**\
Note the quotes around the extended atom to protect from expansion by the shell.

### [Installing a package]

A package can be installed with [pmerge]:

`root `[`#`]`pmerge --ask --verbose <atoms>`

In our example this would be the following:

`root `[`#`]`pmerge --ask --verbose media-sound/vorbis-tools`

[pmerge] is intended to be compatible with Portage. It should be possible to use both [emerge] and [pmerge] on the same system.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/pkgcore`

## [See also]

-   [pkgcheck](https://wiki.gentoo.org/wiki/Pkgcheck "Pkgcheck") --- a [pkgcore]-based QA utility for ebuild repos.
-   [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") --- a collection of tools for Gentoo development.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.

## [External resources]

-   [Upstream documentation](https://pkgcore.github.io/pkgcore/)