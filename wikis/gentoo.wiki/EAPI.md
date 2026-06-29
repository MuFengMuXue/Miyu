**EAPI** is a version defined in [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") and other package manager related files which informs the package manager about the file syntax and content.

The EAPI versions (and their meaning) are defined in the [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification"). Currently, EAPIs 0 through 9 are defined by the specification and supported by the stable version of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). When writing new ebuilds developers can choose whatever EAPI they think is the best. [Using the features of the latest EAPI is encouraged.](https://projects.gentoo.org/council/meeting-logs/20110308-summary.txt) In the main Gentoo repository, EAPIs 0 to 6 are banned for new ebuilds, whereas EAPI 7 is deprecated.

** Note**\
Commonly used [eclasses](https://wiki.gentoo.org/wiki/Eclass "Eclass") often define their own set of supported EAPIs.

## [See also]

-   [Future EAPI](https://wiki.gentoo.org/wiki/Future_EAPI "Future EAPI") --- collects feature ideas which are being requested for inclusion in a future EAPI specification.

## [External resources]

-   [EAPI cheat sheet](https://projects.gentoo.org/pms/9/eapi-cheatsheet.pdf) (version 9.0, 2025-12-14; PDF)
-   [EAPI Usage and Description](https://devmanual.gentoo.org/ebuild-writing/eapi/) (Gentoo Development Guide)
-   [Devmanual section on EAPI 9](https://devmanual.gentoo.org/ebuild-writing/eapi/#eapi-9)
-   [The ultimate guide to EAPI 8](https://mgorny.pl/articles/the-ultimate-guide-to-eapi-8.html) (Michał Górny\'s blog)
-   [GLEP 83: EAPI deprecation](https://www.gentoo.org/glep/glep-0083.html)