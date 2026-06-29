**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")][Project](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentoolkit)

[[]][GitWeb](https://gitweb.gentoo.org/proj/gentoolkit.git)

[[]][Bugs (upstream)](https://bugs.gentoo.org/)

**epkginfo** is a tool used to display package metadata information. It is a shortcut to using the [equery meta] command.

epkginfo is part of [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

[epkginfo] comes as part of the Gentoolkit suite. It, along with the rest of the tools, can be installed by running:

`root `[`#`]`emerge --ask app-portage/gentoolkit`

Please see the [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") article for information on the other tools included in the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package.

## [Usage]

### [Invocation]

As mentioned above [epkginfo] can be invoked two different ways:

-   [epkginfo]
-   [equery meta]

Using the shorter method:

`user `[`$`]`epkginfo --help`

    Usage: epkginfo [options] pkgspec

    Display metadata about a given package.

    options
     -h, --help              display this help message
     -d, --description       show an extended package description
     -H, --herd              show the herd(s) for the package
     -k, --keywords          show keywords for all matching package versions
     -l, --license           show licenses for the best maching version
     -m, --maintainer        show the maintainer(s) for the package
     -S, --stablreq          show STABLEREQ arches (cc's) for all matching package versions
     -u, --useflags          show per-package USE flag descriptions
     -U, --upstream          show package's upstream information
     -x, --xml               show the plain metadata.xml file

## [See also]

-   [Eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean") --- a tool for cleaning repository source files and binary packages.
-   [Equery](https://wiki.gentoo.org/wiki/Equery "Equery") --- a tool to make several common [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") operations simpler.
-   [Egencache](https://wiki.gentoo.org/wiki/Egencache "Egencache") --- a tool that (re)builds metadata information for the Portage package database.