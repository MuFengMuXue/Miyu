This page contains [[changes](https://wiki.gentoo.org/index.php?title=Play.it&diff=1402378)] which are not marked for translation.

**Resources**

[[]][Ebuild repository](https://framagit.org/BetaRays/gentoo-overlay)

[[]][GitWeb](https://git.dotslashplay.it/play.it)

[[]][Official documentation](https://doc.dotslashplay.it/)

[./play.it] is [libre software](https://en.wikipedia.org/wiki/Free_software "wikipedia:Free software") that automates the build of native packages for multiple distributions, including Gentoo, from [DRM-free](https://en.wikipedia.org/wiki/Digital_rights_management "wikipedia:Digital rights management") installers for commercial games. The generated packages are then installed using the standard tools provided by the distribution.

Native Linux games are supported, as well as games developed for other systems thanks to tools like [Wine](https://wiki.gentoo.org/wiki/Wine "Wine"), [DOSBox](https://wiki.gentoo.org/wiki/Games/emulation#DOSBox "Games/emulation") and [ScummVM](https://wiki.gentoo.org/wiki/Games/engines#ScummVM "Games/engines").

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
-   [[3] [Contact]](#Contact)
-   [[4] [See also]](#See_also)

## [Installation]

An [overlay](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") is provided allowing for an easy installation of [./play.it] on Gentoo: [BetaRayʼs Gentoo overlay](https://framagit.org/BetaRays/gentoo-overlay)

## [Usage]

Assuming the game installer is called [setup.exe], using [./play.it] to install a game is a two-steps process:

1.  Run [./play.it] by giving it the path to the game installer:

    :::: cmd-box


    `user `[`$`]`play.it ~/Downloads/setup.exe`


    ::::
2.  Follow the [emerge](https://wiki.gentoo.org/wiki/Portage "Portage") instructions provided at the end of the process, or use the provided [quickunpkg script](https://downloads.dotslashplay.it/resources/gentoo/).

## [Contact]

Contact information can be found [here](https://doc.dotslashplay.it/contact.en.xhtml).

## [See also]

-   [Games/engines](https://wiki.gentoo.org/wiki/Games/engines "Games/engines") --- provides an overview of game engines available in the ::gentoo ebuild repository.
-   [Games/emulation](https://wiki.gentoo.org/wiki/Games/emulation "Games/emulation") --- provides an overview of game emulators available in the ::gentoo ebuild repository.
-   [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") --- an application compatibility layer that allows [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "wikipedia:Microsoft Windows") software to run on Linux and other [POSIX](https://en.wikipedia.org/wiki/POSIX "wikipedia:POSIX")-compliant operating systems.