[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=KiCad&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://www.kicad.org/)

[[]][Official documentation](https://docs.kicad.org/)

[[]][Package information](https://packages.gentoo.org/packages/sci-electronics/kicad)

[[]][Wikipedia](https://en.wikipedia.org/wiki/KiCad "wikipedia:KiCad")

[[]][GitLab](https://gitlab.com/kicad)

[[]][Bugs (upstream)](https://gitlab.com/kicad/code/kicad/-/issues)

[[]][[#kicad](ircs://irc.libera.chat/#kicad)] ([[webchat](https://web.libera.chat/#kicad)])

KiCad is a cross-platform and open-source electronics design automation (EDA) suite for creation of electronic schematic diagrams and printed circuit board (PCB) artwork. Jean-Pierre Charras began development of the program in 1992^[\[1\]](#cite_note-1)^ in order to have \"a tool to teach electronics to his students, and also to learn how to code in C++\".^[\[2\]](#cite_note-2)^ CERN has contributed to its development since 2013^[\[3\]](#cite_note-3)^ and KiCad joined the Linux Foundation in 2019.^[\[4\]](#cite_note-4)^ The \"Ki\" part of the program name was based on a friend\'s company\'s name^[\[5\]](#cite_note-5)^ because other options were taken already.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
    -   [[1.4] [Flatpak]](#Flatpak)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [Vendor libraries]](#Vendor_libraries)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [KiCad-Push-to-DigiKey]](#KiCad-Push-to-DigiKey)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [sci-electronics/kicad](https://packages.gentoo.org/packages/sci-electronics/kicad) [[]] [Electronic Schematic and PCB design tools]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`examples`](https://packages.gentoo.org/useflags/examples)   Install examples, usually source code
  [`nls`](https://packages.gentoo.org/useflags/nls)             Add Native Language Support (using gettext - GNU locale utilities)
  [`openmp`](https://packages.gentoo.org/useflags/openmp)       Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)     Enable dev-libs/wayland backend
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 21:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [sci-electronics/kicad-meta](https://packages.gentoo.org/packages/sci-electronics/kicad-meta) [[]] [Electronic Schematic and PCB design tools (meta package)]

  ----------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`minimal`](https://packages.gentoo.org/useflags/minimal)   Do not install extra data like 3D packages and templates.
  ----------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 09:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerging [[[sci-electronics/kicad]](https://packages.gentoo.org/packages/sci-electronics/kicad)[]] will install the basic program.

`root `[`#`]`emerge --ask sci-electronics/kicad`

### [Additional software]

To install all of:

-   [[[sci-electronics/kicad-footprints]](https://packages.gentoo.org/packages/sci-electronics/kicad-footprints)[]]
-   [[[sci-electronics/kicad-packages3d]](https://packages.gentoo.org/packages/sci-electronics/kicad-packages3d)[]]
-   [[[sci-electronics/kicad-symbols]](https://packages.gentoo.org/packages/sci-electronics/kicad-symbols)[]]
-   [[[sci-electronics/kicad-templates]](https://packages.gentoo.org/packages/sci-electronics/kicad-templates)[]]

at once,

`root `[`#`]`emerge --ask sci-electronics/kicad-meta`

The KiCad footprint libraries can be individually downloaded [here](https://kicad.github.io/footprints/) if desired.

### [Flatpak]

A KiCad [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") is available.^[\[6\]](#cite_note-6)^

`user `[`$`]`flatpak install flathub org.kicad.KiCad`

## [Configuration]

### [Environment variables]

The following paths can be viewed and edited under \'Preferernces\' \> \'Configure Paths\...\'.

-   KICAD7_3DMODEL_DIR: Base path of 3D models used in footprints.
-   KICAD7_3RD_PARTY: Location for plugins, libraries, and color themes installed by the Plugin and Content Manager.
-   KICAD7_FOOTPRINT_DIR: Base path of footprint library files.
-   KICAD7_SYMBOL_DIR: Base path of symbol library files.
-   KICAD7_TEMPLATE_DIR: Location of project templates installed with KiCad.
-   KICAD_USER_DIR: Location of local user content, such as libraries, plugins and themes.
-   KICAD_USER_TEMPLATE_DIR: Location of personal project templates.

### [Files]

User configuration files are stored in [\~/.config/kicad].

The default path for user content (KICAD_USER_DIR) is [\~/.local/share/kicad/\<version\>].

### [Vendor libraries]

There is a currently unmaintained^[\[7\]](#cite_note-7)^ DigiKey Symbol and Footprint Library for KiCad 5,^[\[8\]](#cite_note-8)^ as well as a partner library from suppliers.^[\[9\]](#cite_note-9)^

## [Usage]

Additional libraries, plugins and themes can be installed via the Plugin and Content Manager (PCM). Some libraries not distributed via the official KiCad respository, such as [Espressif KiCad Library](https://github.com/espressif/kicad-libraries), are installed by downloading the release and adding via PCM.

### [KiCad-Push-to-DigiKey]

DigiKey recently released an add-on to assist with collection of parts in a schematic file and pushing them to their myLists service.^[\[10\]](#cite_note-10)^

## [Troubleshooting]

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sci-electronics/kicad`

## [See also]

-   [3D Printing](https://wiki.gentoo.org/wiki/3D_Printing "3D Printing")
-   [Embedded Handbook](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook")
-   [Project:Electronics](https://wiki.gentoo.org/wiki/Project:Electronics "Project:Electronics")
-   [Project:Science](https://wiki.gentoo.org/wiki/Project:Science "Project:Science")

## [External resources]

-   [https://klc.kicad.org/](https://klc.kicad.org/) --- KiCad Library Convention: a set of requirements for contributing to the official KiCad libraries
-   [https://ohwr.org/project/cern-kicad/wikis/home](https://ohwr.org/project/cern-kicad/wikis/home) --- CERN BE-CO-HT Contributions to KiCad
-   [https://ohwr.org/welcome](https://ohwr.org/welcome) --- the Open Hardware Repository
-   [https://www.amazon.com/Complete-Reference-Manual-Jean-Pierre-Charras/dp/1680921274](https://www.amazon.com/Complete-Reference-Manual-Jean-Pierre-Charras/dp/1680921274) --- KiCad Complete Reference Manual, 2018 edition
-   [https://www.kicad.org/made-with-kicad/](https://www.kicad.org/made-with-kicad/) --- A list of projects made by users, along with links to their respective git repositories.
-   [https://dev-docs.kicad.org/en/contribute/](https://dev-docs.kicad.org/en/contribute/) --- Guidance on contributing to KiCad

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.kicad.org/about/kicad/](https://www.kicad.org/about/kicad/)]]
2.  [[[↑](#cite_ref-2)] [[https://cernandsocietyfoundation.cern/news/kicad-tool-sharing-learning-and-developing](https://cernandsocietyfoundation.cern/news/kicad-tool-sharing-learning-and-developing)]]
3.  [[[↑](#cite_ref-3)] [[https://www.kicad.org/sponsors/inkind/](https://www.kicad.org/sponsors/inkind/)]]
4.  [[[↑](#cite_ref-4)] [[https://web.archive.org/web/20211118163340/https://www.linuxfoundation.org/press-release/kicad-joins-linux-foundation-to-advance-electronic-design-automation/](https://web.archive.org/web/20211118163340/https://www.linuxfoundation.org/press-release/kicad-joins-linux-foundation-to-advance-electronic-design-automation/)]]
5.  [[[↑](#cite_ref-5)] [[https://lists.launchpad.net/kicad-developers/msg27528.html](https://lists.launchpad.net/kicad-developers/msg27528.html)]]
6.  [[[↑](#cite_ref-6)] [[https://flathub.org/apps/org.kicad.KiCad](https://flathub.org/apps/org.kicad.KiCad)]]
7.  [[[↑](#cite_ref-7)] [[https://github.com/Digi-Key/digikey-kicad-library/blob/master/README.md](https://github.com/Digi-Key/digikey-kicad-library/blob/master/README.md)]]
8.  [[[↑](#cite_ref-8)] [[https://www.digikey.co.uk/en/resources/design-tools/kicad](https://www.digikey.co.uk/en/resources/design-tools/kicad)]]
9.  [[[↑](#cite_ref-9)] [[https://github.com/digi-key/digikey-partner-kicad-library](https://github.com/digi-key/digikey-partner-kicad-library)]]
10. [[[↑](#cite_ref-10)] [[https://github.com/Digi-Key/KiCad-Push-to-DigiKey](https://github.com/Digi-Key/KiCad-Push-to-DigiKey)]]