**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Build_System "wikipedia:GNU Build System")

**Autotools** is a build system often used for open source projects. Autotools is a particularly mature project, very commonly preinstalled on modern unix-like systems. Though it has the advantage of being almost ubiquitous, Autotools isn\'t necessarily a user friendly system. [Alternatives](https://wiki.gentoo.org/wiki/Build_automation "Build automation") have been written over the years and have better adoption with newer projects.

## Contents

-   [[1] [\"configure\" scripts]](#.22configure.22_scripts)
-   [[2] [Gentoo development]](#Gentoo_development)
    -   [[2.1] [autotools.eclass]](#autotools.eclass)
    -   [[2.2] [libtool.eclass]](#libtool.eclass)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [][\"configure\" scripts]

Autotools can be used to generate [\"configure\" scripts](https://en.wikipedia.org/wiki/Configure_script "wikipedia:Configure script"). These scripts are used to generate [makefiles](https://wiki.gentoo.org/wiki/Make "Make") that are suitable to be run on the current system.

configure scripts often allow compile-time options, and these options are sometimes exposed through [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") in Gentoo.

configure scripts are run with the [./configure] command.

## [Gentoo development]

The following sections explain eclasses related to autotools.

### [autotools.eclass]

[*autotools* eclass](https://devmanual.gentoo.org/eclass-reference/autotools.eclass/) provides functions and dependencies necessary to reconfigure (bootstrap) autotools files in packages. These are usually used in live ebuilds and when applying patches to [configure.ac] or [Makefile.am] files.

If a package already contains a bootstrapped [configure] and [Makefile], there\'s no need to inherit the eclass or call eautoreconf unless patching the build system.

[CODE] **Example ebuild code using autotools.eclass**

    inherit autotools

    src_prepare()

The *eautoreconf* function, similarly to [autoreconf -vi], regenerates [configure] and template files used by autotools. It should be used instead of custom scripts like [autogen.sh]. It automatically detects use of the following tools and calls necessary auto-reconfiguration commands for them:

-   autoconf,
-   automake,
-   libtool,
-   gettext,
-   glib-gettext,
-   intltool,
-   gtk-doc,
-   gnome-doc.

It also detects the use of the `AC_CONFIG_SUBDIRS` variable and performs the recursive auto-reconfiguration in that case.

### [libtool.eclass]

** Note**\
[libtool.eclass] doesn\'t usually need to be used. It is called by default in [[eautoreconf.eclass](#autotools.eclass)].

The [[libtool.eclass]](https://devmanual.gentoo.org/eclass-reference/libtool.eclass/) is an eclass providing means to apply Gentoo-specific patches and fixes to libtool used in package build system without the need for regenerating build system completely.

## [See also]

-   [Build systems](https://wiki.gentoo.org/wiki/Build_systems "Build systems") --- software that automates the compilation, clean up, and installation stages of the software creation process.

## [External resources]

-   [The Basics of Autotools (Gentoo Developer Handbook)](https://devmanual.gentoo.org/general-concepts/autotools/index.html)