This is a reference on how to indicate a specific package when interacting with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").

A **version specifier**, or **atom**, is the precise format used to tell [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") exactly what package to install, with optional version, slot, or [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") of origin. The format is also used in files in [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage"), and generally in Gentoo.

A version specifier is based on the *category/package* pair, with extra information if necessary. In some case the *category* may be omitted, if the package name is unique in all ebuild repositories configured with Portage, for example when using the [emerge] command.

** See also**\
See [man 5 ebuild] and [man emerge] for more detailed information on how Portage uses atoms.

\

Version specifiers are also known as \"*DEPEND atoms*\" in Portage documentation. For the ebuild development perspective, see the [Gentoo Development Guide](https://devmanual.gentoo.org/general-concepts/dependencies/).

## Contents

-   [[1] [Version specifier format]](#Version_specifier_format)
    -   [[1.1] [Basic]](#Basic)
    -   [[1.2] [By version]](#By_version)
    -   [[1.3] [By SLOT]](#By_SLOT)
    -   [[1.4] [By ebuild repository]](#By_ebuild_repository)
-   [[2] [See also]](#See_also)

## [Version specifier format]

### [Basic]

**category/package**

Matches **any version** of a package.

[Example:][**x11-libs/gtk+**]

\

    matches: gtk+-1.2.10-r12
    matches: gtk+-2.24.7
    matches: gtk+-3.0.12-r1

### [By version]

** Note**\
When specifying a package version, a comparison operator **must** be used at the beginning of the atom.

**\~category/package-1.23**

Matches version and any revision.

[Example:][\~sys-devel/gdb-7.3]

\

    matches: gdb-7.3
    matches: gdb-7.3-r1

    does not match: gdb-7.3.1

**=category/package-1.23\***

Matches a version by the version range. Note that there\'s no \"`.`\" before the \"`*`\".

[Example:][=sys-devel/gdb-7.3\*]

\

    matches: gdb-7.3
    matches: gdb-7.3-r1
    matches: gdb-7.3.1

    does not match: gdb-7.30

**=category/package-1.23**

Matches a version exactly.

[Example:][=www-client/firefox-7.0]

\

    matches: firefox-7.0

    does not match: firefox-7.0-r1
    does not match: firefox-7.0.1

**\>=category/package-1.23**

Matches the specified version or any higher version.

[Example:][\>=dev-lang/python-2.7]

\

    matches: python-2.7
    matches: python-2.7.1-r1
    matches: python-3.2.2

**\>category/package-1.23**

Matches a version strictly later than specified.

[Example:][\>dev-lang/python-2.7]

\

    matches: python-2.7-r1
    matches: python-2.7.1
    matches: python-3.2.2

    does not match: python-2.7

**\<category/package-1.23**

Matches a version strictly older than specified.

[Example:][\<dev-python/beautifulsoup-3.2]

\

    matches: dev-python/beautifulsoup-3.1.0.1-r1

    does not match: dev-python/beautifulsoup-3.2.0

**\<=category/package-1.23**

Matches the specified version or any older version.

[Example:][\<=sys-fs/udev-171]

\

    matches: udev-171
    matches: udev-164-r2

    does not match: udev-171-r1

### [By SLOT]

**category/package:2**

Matches package in the specified package [SLOT](https://wiki.gentoo.org/wiki/SLOT "SLOT"). Note that there is no prefix.

[Example:][dev-db/sqlite:0]

\

    matches: sqlite-2.8.16-r5

    does not match: sqlite-3.7.8

### [By ebuild repository]

**category/package::repository**

Matches a package from a specific [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). This can be combined with other specifiers. The official Gentoo repository is `::gentoo`.

[Example:][=media-libs/mesa-9999::x11]

\

    matches: mesa version 9999 from the x11 overlay

    does not match: any version from a different overlay.

## [See also]

-   [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- the main command-line interface to [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")
-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s package manager.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.