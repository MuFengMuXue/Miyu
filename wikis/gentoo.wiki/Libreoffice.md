**Resources**

[[]][Home](https://www.libreoffice.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-office/libreoffice)

[[]][Pre-compiled binaries - Package information](https://packages.gentoo.org/packages/app-office/libreoffice-bin)

[[]][Official documentation](https://documentation.libreoffice.org/en/english-documentation/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LibreOffice "wikipedia:LibreOffice")

**LibreOffice** is a full office productivity suite. It\'s a successor to OpenOffice.org and strives to be a better and less bloated office suite.^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Binary installation]](#Binary_installation)
-   [[2] [Spell check]](#Spell_check)
-   [[3] [External resources]](#External_resources)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-office/libreoffice](https://packages.gentoo.org/packages/app-office/libreoffice) [[]] [A full office productivity suite]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+branding`](https://packages.gentoo.org/useflags/+branding)           Enable Gentoo specific branding
  [`+cups`](https://packages.gentoo.org/useflags/+cups)                   Add support for CUPS (Common Unix Printing System)
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)                   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`+gtk3`](https://packages.gentoo.org/useflags/+gtk3)                   Enable support for x11-libs/gtk+:3
  [`+mariadb`](https://packages.gentoo.org/useflags/+mariadb)             Prefer mariadb connector over mysql connector
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)   Add support for accessibility (eg \'at-spi\' library)
  [`base`](https://packages.gentoo.org/useflags/base)                     Enable full support for LibreOffice Base databases (involves additional bundled libs)
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)           Enable Bluetooth Support
  [`coinmp`](https://packages.gentoo.org/useflags/coinmp)                 Use sci-libs/coinor-mp as alternative solver
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)   Build with user-specified CFLAGS (unsupported)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`eds`](https://packages.gentoo.org/useflags/eds)                       Enable support for Evolution-Data-Server (EDS)
  [`googledrive`](https://packages.gentoo.org/useflags/googledrive)       Enable support for remote files on Google Drive
  [`gstreamer`](https://packages.gentoo.org/useflags/gstreamer)           Add support for media-libs/gstreamer (Streaming media)
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                       Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`gtk4`](https://packages.gentoo.org/useflags/gtk4)                     Enable support for gui-libs/gtk:4
  [`java`](https://packages.gentoo.org/useflags/java)                     Add support for Java
  [`kde`](https://packages.gentoo.org/useflags/kde)                       Add support for software made by KDE, a free software community
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                     Add LDAP support (Lightweight Directory Access Protocol)
  [`odk`](https://packages.gentoo.org/useflags/odk)                       Build the Office Development Kit
  [`pdfimport`](https://packages.gentoo.org/useflags/pdfimport)           Enable PDF import via the Poppler library
  [`postgres`](https://packages.gentoo.org/useflags/postgres)             Add support for the postgresql database
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                       Add support for the Qt 6 application and UI framework
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)             Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)                 Enable Vulkan usage via the skia library (clang recommended)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 20:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [app-office/libreoffice-bin](https://packages.gentoo.org/packages/app-office/libreoffice-bin) [[]] [A full office productivity suite. Binary package]

  ------------------------------------------------------------------- ------------------------------------------------------------------
  [`java`](https://packages.gentoo.org/useflags/java)                 Add support for Java
  [`offlinehelp`](https://packages.gentoo.org/useflags/offlinehelp)   Install help files locally instead of using the LibreOffice Wiki
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  ------------------------------------------------------------------- ------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 19:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

LibreOffice does not start without a database enabled. Most users should choose one to enable.

** Note**\
For the \'Remote Files\' LibreOffice facility to work, one needs to have a working D-Bus session bus and the `gtk` USE flag enabled on the [[[app-office/libreoffice]](https://packages.gentoo.org/packages/app-office/libreoffice)[]] package, since the \'Remote Files\' feature depends on [GVfs](https://wiki.gentoo.org/wiki/GVfs "GVfs").

### [Emerge]

Install [[[app-office/libreoffice]](https://packages.gentoo.org/packages/app-office/libreoffice)[]]:

`root `[`#`]`emerge --ask --verbose app-office/libreoffice`

### [Binary installation]

Since LibreOffice is such a large package to compile, it is also offered in pre-compiled binaries in [[[app-office/libreoffice-bin]](https://packages.gentoo.org/packages/app-office/libreoffice-bin)[]].

`root `[`#`]`emerge --ask --verbose app-office/libreoffice-bin`

The binary packages are compiled such that they fit to the libraries of a stable Gentoo system. Attempting to use them on an \~arch system may result in difficulties; this is not supported.

The [[[app-office/libreoffice-bin]](https://packages.gentoo.org/packages/app-office/libreoffice-bin)[]] may not be compatible with the use of the *Base* application. In this case it may be necessary to use a source build and enable the [[[java]](https://packages.gentoo.org/useflags/java)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[firebird]](https://packages.gentoo.org/useflags/firebird)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

## [Spell check]

By default, LibreOffice uses [[[app-text/hunspell]](https://packages.gentoo.org/packages/app-text/hunspell)[]] for spell check. To enable spell checking for a specific language, enable the corresponding language in the [L10N](https://wiki.gentoo.org/wiki/Localization "Localization") useflags of hunspell - in [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")].

[FILE] **`/etc/portage/package.use/00local`en_GB location example**

    */*  LINGAS: en
    */*  L10N: en-GB

A package specific to the Finnish language is also available: [[[app-office/libreoffice-voikko]](https://packages.gentoo.org/packages/app-office/libreoffice-voikko)[]].

## [External resources]

-   [The Document Foundation Wiki](https://wiki.documentfoundation.org/Documentation)
-   [LibreOffice Timeline](https://www.libreoffice.org/about-us/libreoffice-timeline/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://opensource.com/article/18/9/libreoffice-history](https://opensource.com/article/18/9/libreoffice-history)]]
2.  [[[↑](#cite_ref-2)] [[https://wiki.documentfoundation.org/History](https://wiki.documentfoundation.org/History)]]