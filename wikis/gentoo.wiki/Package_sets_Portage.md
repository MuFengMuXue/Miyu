**Package sets** are lists of packages used by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). They define the packages that make up the base system and those that are installed based on system administrator action. This article describes package sets in high detail and includes a list of all typically available sets on a Gentoo system.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Static sets]](#Static_sets)
        -   [[1.1.1] [\@selected-packages]](#.40selected-packages)
        -   [[1.1.2] [\@selected-sets]](#.40selected-sets)
        -   [[1.1.3] [\@selected]](#.40selected)
        -   [[1.1.4] [\@system]](#.40system)
        -   [[1.1.5] [\@profile]](#.40profile)
        -   [[1.1.6] [\@world]](#.40world)
    -   [[1.2] [Dynamic sets]](#Dynamic_sets)
        -   [[1.2.1] [\@changed-deps]](#.40changed-deps)
        -   [[1.2.2] [\@deprecated-live-rebuild]](#.40deprecated-live-rebuild)
        -   [[1.2.3] [\@downgrade]](#.40downgrade)
        -   [[1.2.4] [\@installed]](#.40installed)
        -   [[1.2.5] [\@live-rebuild]](#.40live-rebuild)
        -   [[1.2.6] [\@module-rebuild]](#.40module-rebuild)
        -   [[1.2.7] [\@preserved-rebuild]](#.40preserved-rebuild)
        -   [[1.2.8] [\@rebuilt-binaries]](#.40rebuilt-binaries)
        -   [[1.2.9] [\@security]](#.40security)
        -   [[1.2.10] [\@unavailable]](#.40unavailable)
        -   [[1.2.11] [\@unavailable-binaries]](#.40unavailable-binaries)
        -   [[1.2.12] [\@x11-module-rebuild]](#.40x11-module-rebuild)
    -   [[1.3] [Custom sets]](#Custom_sets)
        -   [[1.3.1] [Example: \@larrys-custom-set]](#Example:_.40larrys-custom-set)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Installing a set]](#Installing_a_set)
    -   [[2.2] [Listing]](#Listing)
        -   [[2.2.1] [Available sets]](#Available_sets)
        -   [[2.2.2] [Packages within a set]](#Packages_within_a_set)
            -   [[2.2.2.1] [Portage]](#Portage)
            -   [[2.2.2.2] [pkgcore]](#pkgcore)
            -   [[2.2.2.3] [eix]](#eix)
            -   [[2.2.2.4] [equery]](#equery)
        -   [[2.2.3] [Packages that belong to a set]](#Packages_that_belong_to_a_set)
-   [[3] [See also]](#See_also)

## [Configuration]

### [Static sets]

All Gentoo systems have six static sets, defined in the [/usr/share/portage/config/sets/portage.conf] file maintained by Portage, which specify the packages that make up the system. Three sets include \"**\@selected-**\" as a prefix in their name and refer to the member sets and their packages which the system administrator has *selected* to be installed.

The sets titled **\@system** and **\@profile** define a static list of packages which are required for the base system to operate as intended. These two sets are defined by the Gentoo development team.

The *\@world* set is a superset consisting of the sum of the members of the previously mentioned sets.

#### [][\@selected-packages]

The **selected-packages** set is the list of packages found in the [world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") ([/var/lib/portage/world]). It is a static list of packages that have been explicitly installed by the system administrator. Adding a package to this set can be avoided by passing the `--oneshot` option to [emerge].

#### [][\@selected-sets]

The **\@selected-sets** set is a [superset](https://en.wikipedia.org/wiki/superset "wikipedia:superset"): a union of any and all custom sets emerged by the system administrator. It includes a list of every package that been explicitly installed onto the system by a result of inclusion of an installed set (except if `--oneshot` was used - see below). The members of this set are listed in the [/var/lib/portage/world_sets] file. The file will be empty if the system administrator has not (yet) emerged any custom sets.

If the `--oneshot` option was passed when installing a custom set then the packages included in the set will not be listed, nor will the custom set be recorded in the [world_sets] file.

#### [][\@selected]

The **\@selected** set is a [superset](https://en.wikipedia.org/wiki/superset "wikipedia:superset"): a union of **\@selected-packages** and **\@selected-sets**. That is to say, the output of this set includes all packages intentionally installed by the system administrator.

Take careful note that packages which are listed in the **\@selected** set may or may not include packages which are *also* defined in the *\@system* or *\@profile* sets by Gentoo developers. It is unwise to blindly uninstall packages from this set. Portage will provide a warning when attemping to unmerge a package which is defined in the *\@system* or *\@profile* set.

#### [][\@system]

The **\@system** set (along with the following **\@profile** set) defines the base set of packages on a Gentoo system. The **\@system** set is maintained by the Gentoo development team.

As of 2026-03-04, the **\@system** set contains:

-   [[[app-admin/eselect]](https://packages.gentoo.org/packages/app-admin/eselect)[]]
-   [[[app-alternatives/awk]](https://packages.gentoo.org/packages/app-alternatives/awk)[]]
-   [[[app-alternatives/bzip2]](https://packages.gentoo.org/packages/app-alternatives/bzip2)[]]
-   [[[app-alternatives/gzip]](https://packages.gentoo.org/packages/app-alternatives/gzip)[]]
-   [[[app-alternatives/sh]](https://packages.gentoo.org/packages/app-alternatives/sh)[]]
-   [[[app-alternatives/tar]](https://packages.gentoo.org/packages/app-alternatives/tar)[]]
-   [[[app-arch/bzip2]](https://packages.gentoo.org/packages/app-arch/bzip2)[]]
-   [[[app-arch/gzip]](https://packages.gentoo.org/packages/app-arch/gzip)[]]
-   [[[app-arch/tar]](https://packages.gentoo.org/packages/app-arch/tar)[]]
-   [[[app-arch/xz-utils]](https://packages.gentoo.org/packages/app-arch/xz-utils)[]]
-   [[[app-shells/bash]](https://packages.gentoo.org/packages/app-shells/bash)[]]
-   [[[dev-build/make]](https://packages.gentoo.org/packages/dev-build/make)[]]
-   [[[net-mail/mailbase]](https://packages.gentoo.org/packages/net-mail/mailbase)[]]
-   [[[net-misc/iputils]](https://packages.gentoo.org/packages/net-misc/iputils)[]]
-   [[[net-misc/rsync]](https://packages.gentoo.org/packages/net-misc/rsync)[]]
-   [[[net-misc/wget]](https://packages.gentoo.org/packages/net-misc/wget)[]]
-   [[[sec-keys/openpgp-keys-gentoo-release]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-release)[]]
-   [[[sys-apps/baselayout]](https://packages.gentoo.org/packages/sys-apps/baselayout)[]]
-   [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]]
-   [[[sys-apps/diffutils]](https://packages.gentoo.org/packages/sys-apps/diffutils)[]]
-   [[[sys-apps/file]](https://packages.gentoo.org/packages/sys-apps/file)[]]
-   [[[sys-apps/findutils]](https://packages.gentoo.org/packages/sys-apps/findutils)[]]
-   [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]]
-   [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]]
-   [[[sys-apps/iproute2]](https://packages.gentoo.org/packages/sys-apps/iproute2)[]]
-   [[[sys-apps/kbd]](https://packages.gentoo.org/packages/sys-apps/kbd)[]]
-   [[[sys-apps/kmod]](https://packages.gentoo.org/packages/sys-apps/kmod)[]]
-   [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]]
-   [[[sys-apps/man-pages]](https://packages.gentoo.org/packages/sys-apps/man-pages)[]]
-   [[[sys-apps/net-tools]](https://packages.gentoo.org/packages/sys-apps/net-tools)[]]
-   [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]]
-   [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]]
-   [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]
-   [[[sys-apps/which]](https://packages.gentoo.org/packages/sys-apps/which)[]]
-   [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]]
-   [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]
-   [[[sys-devel/gnuconfig]](https://packages.gentoo.org/packages/sys-devel/gnuconfig)[]]
-   [[[sys-devel/patch]](https://packages.gentoo.org/packages/sys-devel/patch)[]]
-   [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]]
-   [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]]
-   [[[sys-process/psmisc]](https://packages.gentoo.org/packages/sys-process/psmisc)[]]
-   [[[virtual/dev-manager]](https://packages.gentoo.org/packages/virtual/dev-manager)[]]
-   [[[virtual/editor]](https://packages.gentoo.org/packages/virtual/editor)[]]
-   [[[virtual/libc]](https://packages.gentoo.org/packages/virtual/libc)[]]
-   [[[virtual/man]](https://packages.gentoo.org/packages/virtual/man)[]]
-   [[[virtual/os-headers]](https://packages.gentoo.org/packages/virtual/os-headers)[]]
-   [[[virtual/package-manager]](https://packages.gentoo.org/packages/virtual/package-manager)[]]
-   [[[virtual/pager]](https://packages.gentoo.org/packages/virtual/pager)[]]
-   [[[virtual/service-manager]](https://packages.gentoo.org/packages/virtual/service-manager)[]]
-   [[[virtual/ssh]](https://packages.gentoo.org/packages/virtual/ssh)[]]

#### [][\@profile]

The **profile** set (along with **\@system** defined in the preceding section) define the base set of packages on a Gentoo system. The differences between the two is described in the man pages of Portage but the distinction does not usually matter to the system administrator. The packages that make up this set are determined by the system\'s profile and/or computer\'s architecture.

#### [][\@world]

The **\@world** set is the largest [superset](https://en.wikipedia.org/wiki/superset "wikipedia:superset") on a Gentoo system: a union of **\@selected**, **\@system**, and **\@profile** sets. That is to say the **\@world** set includes *all* packages installed on the system: those defined by the system administrator and those defined by the Gentoo development team.

** Note**\
It is conceptually important to understand the **\@world** set is *[superset](https://en.wikipedia.org/wiki/superset "wikipedia:superset")* of all of the aforementioned sets. It does not merely represent the packages from the *world file* itself. The world file is represented by the [\@selected-packages set](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)").

### [Dynamic sets]

Portage maintains additional dynamic sets that are based on the state of the package database or the type of packages installed on the system. Unlike the previous sets, these dynamically maintained sets cannot be used to define packages that should be installed. These sets are listed in the [/usr/share/portage/config/sets/portage.conf] file and are determined and maintained by Portage. They are therefore not intended to be modified by the system administrator.

#### [][\@changed-deps]

**changed-deps** is the set of packages that have [changed dependencies](https://wiki.gentoo.org/wiki/Project:Portage/Changed_dependencies "Project:Portage/Changed dependencies").

#### [][\@deprecated-live-rebuild]

**deprecated-live-rebuild** is the older way to get the set of live packages.

#### [][\@downgrade]

**downgrade** is the set of packages that have an installed version that is higher than the highest visible ebuild version.

#### [][\@installed]

**installed** is the set of all installed packages.

#### [][\@live-rebuild]

**live-rebuild** is the set of live (category/package-9999) packages.

#### [][\@module-rebuild]

**module-rebuild** is the set of out of kernel modules, packages that own files in [/lib/modules].

#### [][\@preserved-rebuild]

**preserved-rebuild** is the set of packages that are using [preserved libraries](https://wiki.gentoo.org/wiki/Preserve-libs "Preserve-libs").

#### [][\@rebuilt-binaries]

**rebuilt-binaries** is the set of binary package that can be replaced with packages that have been rebuilt.

#### [][\@security]

**security** is the set of packages for which there is a new [GLSA](https://wiki.gentoo.org/wiki/GLSA "GLSA").

#### [][\@unavailable]

**unavailable** is the set of installed packages that do not have an ebuild.

#### [][\@unavailable-binaries]

**unavailable-binaries** is the set of installed packages that do not have a binary package.

#### [][\@x11-module-rebuild]

**x11-module-rebuild** is the set of packages that own files inside [/usr/lib/xorg/modules] with the exception of the package that owns [/usr/bin/Xorg].

### [Custom sets]

There are two types of custom sets:

-   static, as defined in [[/etc/portage/sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets")]
-   dynamic, as defined in [/etc/portage/sets.conf]

#### [][Example: \@larrys-custom-set]

**larrys-custom-set** is an example of a custom set as defined by the system administrator. Custom sets are defined as files in the [[/etc/portage/sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets")] directory can be easily installed or rebuilt as a group by the package manager. Members defined within a custom set in this way are static and will only change via direct modification by the system administrator.

Once a list of packages have been defined, install a custom set via:

`root `[`#`]`emerge --ask @larrys-custom-set`

In addition to emerging the packages, the set itself will be added to **\@selected-sets** and therefore the individual packages within the set also be part of **\@selected**. This is fine if the packages in Larry\'s set are all admin defined packages. However if some of the packages in Larry\'s set are only dependencies, then problems are likely to occur over time because the package will continue to be updated even if it is no longer required. This is equivalent to having a package\'s *dependencies* in the world file.

To emerge a custom set without adding the package(s) to the **\@selected-sets** run:

`root `[`#`]`emerge --ask --oneshot @larrys-custom-set`

To stop using a custom set, deselect it:

`root `[`#`]`emerge --deselect @larrys-custom-set`

** Warning**\
It is dangerous to use `--unmerge` with sets. Doing so with certain packages listed in a set could render the system inoperable if a critical system package is removed.

After deselection, issue a dependency clean. This will safely remove packages that are no longer on the system:

`root `[`#`]`emerge --ask --depclean`

## [Usage]

### [Installing a set]

Sets can be passed as an argument to the emerge command:

`user `[`$`]`emerge -p @world`

### [Listing]

#### [Available sets]

The list of available sets can be found by:

`user `[`$`]`emerge --list-sets`

    changed-deps
    deprecated-live-rebuild
    downgrade
    installed
    larrys-defined-set
    live-rebuild
    module-rebuild
    preserved-rebuild
    profile
    rebuilt-binaries
    security
    selected
    selected-packages
    selected-sets
    system
    unavailable
    unavailable-binaries
    world
    x11-module-rebuild

#### [Packages within a set]

Various tools can be used to list packages included within the system set. With the exceptions of [eix] and [pquery], the tools below preface the set name with an `@` character.

##### [Portage]

The [emerge] command can be used to list packages included in sets using the following options:

`user `[`$`]`emerge -pqeO @<set>`

Or using long options:

`user `[`$`]`emerge --pretend --quiet --emptytree --nodeps @<set>`

##### [pkgcore]

Using [pquery] (from [[[sys-apps/pkgcore]](https://packages.gentoo.org/packages/sys-apps/pkgcore)[]]):

`user `[`$`]`pquery --pkgset <set>`

##### [eix]

To receive a compact listing which emulates the listing output from other commands via [[eix](https://wiki.gentoo.org/wiki/Eix "Eix")] (from [[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]]), issue:

`user `[`$`]`eix --compact @<set>`

For a non-compact listing, issue:

`user `[`$`]`eix @<set>`

Where `<set>` is one of `system` (@system), `world` (@world), `selected` (@selected), etc\... See [man eix] or the [eix article for more usage examples](https://wiki.gentoo.org/wiki/Eix#usage "Eix").

##### [equery]

Using [equery] (from [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]]):

`user `[`$`]`equery list @<set>`

#### [Packages that belong to a set]

It is possible to search for specific packages that are defined within one or many custom sets with the following command, replace `` with the package name as appropriate:

`user `[`$`]`grep -ir  /etc/portage`

## [See also]

-   [/etc/portage/sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets") --- an optional directory that is used to create user defined package sets
-   [Selected-packages set (Portage)](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- contains the user-selected \"world\" packages that are listed in the [/var/lib/portage/world] file.