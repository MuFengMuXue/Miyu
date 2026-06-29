**Resources**

[[]][Home](https://mandoc.bsd.lv/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/mandoc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mandoc "wikipedia:Mandoc")

[mandoc] is a suite of tools for [[[mdoc(7)]](https://mandoc.bsd.lv/man/mdoc.7.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page"), the semantic roff macro language preferred for BSD manual pages, and [[[man(7)]](https://man.archlinux.org/man/man.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], the historical presentation-based roff macro language for UNIX manuals.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [The system-man USE flag]](#The_system-man_USE_flag)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/mandoc](https://packages.gentoo.org/packages/app-text/mandoc) [[]] [Suite of tools compiling mdoc and man]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`cgi`](https://packages.gentoo.org/useflags/cgi)                 build man.cgi web plugin for viewing man pages
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`system-man`](https://packages.gentoo.org/useflags/system-man)   set as the default man provider
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-04 12:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Before enabling the [system-man] `USE` flag, please refer to \"[The system-man USE flag](#The_system-man_USE_flag)\".

### [Emerge]

`root `[`#`]`emerge --ask app-text/mandoc`

### [The system-man USE flag]

The [system-man] `USE` flag makes **mandoc** the default software for accessing man pages.

** Warning**\
During installation, man pages are compressed using the value of the `PORTAGE_COMPRESS` variable, which by default is \"bzip2\". However, [mandoc] does not handle bzip2\'d man pages, so after changing this flag, those man pages will no longer be readable.

To ensure [mandoc] can display man pages, set the value of the `PORTAGE_COMPRESS` variable in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] to \"gzip\" and reinstall packages containing man pages:

[FILE] **`/etc/portage/make.conf`**

    PORTAGE_COMPRESS="gzip"

Alternatively, set `PORTAGE_COMPRESS_EXCLUDE_SUFFIXES` to not compress man pages:

[FILE] **`/etc/portage/make.conf`**

    # man pages suffixes, may not be exhaustive
    PORTAGE_COMPRESS_EXCLUDE_SUFFIXES="[1-9] n [013]p [1357]ssl [1357]ossl 3am 3pcap 3perl 3pm [1-9]bsd"

** Warning**\
`PORTAGE_COMPRESS` and `PORTAGE_COMPRESS_EXCLUDE_SUFFIXES` will not have any effect on packages installed from a [binary host](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")!

Packages that will need to be reinstalled include:

-   [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]]
-   [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]]
-   [[[sys-apps/man-pages]](https://packages.gentoo.org/packages/sys-apps/man-pages)[]]
-   [[[sys-apps/man-pages-posix]](https://packages.gentoo.org/packages/sys-apps/man-pages-posix)[]]
-   [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]]
-   [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]]

For a complete list of packages to be reinstalled, the following command can be used. It requires [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]] and, if using Bash, the `globstar` option:

`user `[`$`]`qfile /usr/share/man/**/*.bz2 | cut -d: -f1 | sort -u`

## [See also]

[man page](https://wiki.gentoo.org/wiki/Man_page "Man page") --- contains system reference documentation. It is found on most Unix-like systems.

## [External resources]

-   The [[[mdoc(7)]](https://mandoc.bsd.lv/man/mdoc.7.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") man page