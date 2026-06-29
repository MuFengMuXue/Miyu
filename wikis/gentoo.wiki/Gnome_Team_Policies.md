This page is intended to link or to write down Gnome team policies about its own packages or how packages using Gnome team packages as dependencies should handle some particular aspects.

## Contents

-   [[1] [EAPI]](#EAPI)
-   [[2] [Eclass usage]](#Eclass_usage)
    -   [[2.1] [src_prepare]](#src_prepare)
    -   [[2.2] [G2CONF and src_configure]](#G2CONF_and_src_configure)
    -   [[2.3] [GCONF_DEBUG]](#GCONF_DEBUG)
    -   [[2.4] [GNOME2_LA_PUNT]](#GNOME2_LA_PUNT)
    -   [[2.5] [GNOME2_EAUTORECONF]](#GNOME2_EAUTORECONF)
-   [[3] [Gnome frameworks and dependencies]](#Gnome_frameworks_and_dependencies)
    -   [[3.1] [gnome-keyring and libsecret]](#gnome-keyring_and_libsecret)
    -   [[3.2] [Handling gtk-doc documentation]](#Handling_gtk-doc_documentation)
    -   [[3.3] [GObject Introspection]](#GObject_Introspection)
        -   [[3.3.1] [USE flag]](#USE_flag)
        -   [[3.3.2] [Subslot usage]](#Subslot_usage)
    -   [[3.4] [GTK+ USE-flag and slots usage]](#GTK.2B_USE-flag_and_slots_usage)
    -   [[3.5] [static-libs]](#static-libs)
-   [[4] [Other policies]](#Other_policies)
    -   [[4.1] [ssl]](#ssl)
    -   [[4.2] [avahi vs. zeroconf]](#avahi_vs._zeroconf)
    -   [[4.3] [jabber vs. xmpp]](#jabber_vs._xmpp)

## [EAPI]

Gnome team tries to stay up-to-date with regard to the best available EAPI. Currently this is **EAPI 6**.

Gnome team goal is to have all ebuilds use that EAPI and make best use of its features such as:

-   subslots
-   default configure flags
-   default installed documentation (generally no need to define DOCS)

## [Eclass usage]

Gnome team provides a wide range a functions through its eclasses. Some people see it as bloat, but this is only the bare minimum to ensure packages using Gnome libraries work fine once installed. The amount of code is only the result of keeping backward compatibility with old systems such as scrollkeeper but there is really nothing to fear from the eclass, much more to get wrong by not using it (not regenerating mime and desktop database being the most common example).

Users of the eclass are, obviously, required to pay attention to eclass changes. Most of the time, if not always, they are announced/reviewed on gentoo-dev mailing list and there is little effort to do to keep up to date.

### [src_prepare]

gnome2_src_prepare must be called --- or its behavior replicated to all necessary extents --- as it applies Makefiles fixes as well as environment fixes which would expose your package to build failures^[\[1\]](#cite_note-1)^, sandbox errors^[\[2\]](#cite_note-2)^, etc, on some systems.

For the same reason, if eautoreconf is called, gnome2_src_prepare must be called after.

### [G2CONF and src_configure]

** Note**\
As of EAPI 6, G2CONF support has been removed

This variable has a long history. Recently, on gentoo-dev mailing list, someone brought up the issue that most Gnome ebuilds did configure work in pkg_setup instead of src_configure and this caused extra run-time for no reason for binary packages.

In response to that valid concern, the Gnome team updated its policy to always define a src_configure when there is something to configure and **pass configure switch to gnome2_src_configure function**. Since G2CONF had no other use than defining configure information in pkg_setup, most of its use if now gone and **it should be removed from ebuilds**.

For example, fictitious ebuild:

[FILE] **`foo-1.ebuild`**

    [...]
    src_configure()  = 9999 ]]; then
            G2CONF="$ --enable-debug"
        fi
        G2CONF="$
            --disable-schemas-compile
            --disable-strict-cc
            VALAC=$(type -P valac-0.18)
            VAPIGEN=$(type -P vapigen-0.18)
        "
        gnome2_src_configure
    }

will translate to:

[FILE] **`foo-1.ebuild`**

    [...]
    src_configure()  = 9999 ]]; then
            myconf="$ --enable-debug"
        fi
        gnome2_src_configure \
            --disable-schemas-compile \
            --disable-strict-cc \
            VALAC=$(type -P valac-0.18) \
            VAPIGEN=$(type -P vapigen-0.18) \
            $
    }

### [GCONF_DEBUG]

** Note**\
As of EAPI 6, GCONF_DEBUG support has been removed

Policy being defined at [bug #270919](https://bugs.gentoo.org/show_bug.cgi?id=270919).

### [GNOME2_LA_PUNT]

For EAPI \< 5, when set to \"yes\" will get all .la files removed. For newer EAPIs, it relies in prune_libtool_files function from eutils.eclass, and will behave as follows:

-   When GNOME2_LA_PUNT is unset, prune_libtool_files will be run.
-   When GNOME2_LA_PUNT is set to \"yes\", prune_libtool_files will be run with \"\--modules\" option.
-   When GNOME2_LA_PUNT is set to \"no\", it will do nothing.

### [GNOME2_EAUTORECONF]

You can rely on setting this variable to \"yes\" value to ensure eautoreconf is called at the end of gnome2_src_prepare (default src_prepare, environment resets\...). Please note this variable could be banned in future EAPIs as soon as they handle the user patches and rebuilding of autotools files on their own.

## [Gnome frameworks and dependencies]

### [gnome-keyring and libsecret]

libsecret is a library to access replacing gnome-keyring as the storage for secrets (passwords, etc). Both library used to be pulled in by respective USE flags but they do in fact provide the same service to consuming applications. As such, USE=gnome-keyring must be used for all usage of these two libraries or any future secret storage provider for the Gnome desktop.

### [Handling gtk-doc documentation]

gtk-doc is the framework for documenting libraries for developer audience. It provides tools to extract, compile and install documentation from the source code of the library directly. In Gentoo, this used to be handled by USE=doc for all packages using gnome2.eclass however the behavior was not fit to what users expected.

\
After much discussion gnome team came to the following conclusions:

-   **gtk-doc must always be installed**. gtk-doc is part of the package as distributed by upstream (pre-built), hence it costs no extra CPU time, no extra dependencies and has relatively low disk space requirements. Corollary, there is no need to rebuild documentation, so just pass \--disable-gtk-doc to configure.
-   **gtk-doc must be installed in /usr/share/gtk-doc**. gtk-doc is a framework for documentation, just like any other framework, files targeted for it must be usually be installed in a defined place to be any useful (such as in devhelp). Also, until there is a better solution, this allows users to easily avoid any gtk-doc documentation if they have no use for it by using install-mask feature.
-   **All packages using gtk-doc must BDEPEND on gtk-doc-am**. This package provides macros for autoreconf and tools to relink installed documentation to local resources instead of [http://library.gnome.org](http://library.gnome.org).

### [GObject Introspection]

#### [USE flag]

The introspection USE flag is used to control whether or not a package should install its gobject-introspection description files. This is currently mainly used throughout Gnome for using regular C libraries transparently from languages such as python and javascript.

\
Current policy is:

-   make support optional only when it is possible
-   make use flag **default enabled** when support is optional. Since it is used throughout the Gnome desktop, it is simpler to default it to be enabled since most user will want it and will not want to change this USE flag on a per-package basis when portage will check the dependencies. Exceptions are system packages such as udev until libgudev is eventually split.
-   in all cases make sure to add \[introspection\] or \[introspection?\] (depending on the case) to required dependencies according to build system information and .gir files.

** Note**\
Most of the time introspection support is coupled with vala. Vala support will require introspection in order to build and install .vapi files so do not forget to add REQUIRED_USE.

#### [Subslot usage]

GObject introspection files are subject to API changes as denoted by the version attribute of the repository element (currently 1.2).

In order to properly support the next repository version change, as was exposed by previous transitions, all packages providing .gir files **must depend on dev-libs/gobject-introspection subslot with the := operator**.

This change is best applied on version bumps so that VDB is properly updated.

### [][GTK+ USE-flag and slots usage]

Since the release of gtk+-3, Gentoo has three gtk+ slots in tree. Long ago, packages tried to handle support for both gtk+-1 and gtk+-2 by using USE=gtk and USE=gtk2. However this proved to be confusing. Some packages would have both when actually only one was useful. Some other packages only had USE=gtk for gtk+-2 support. These two simple examples shows that this was the wrong approach. It created much more support than necessary and users were not happy.

\
At the time gtk+-3 was added to the tree, it was discussed on the mailing list and approved by other Gentoo developers that having only USE=gtk to mean \"Enable gtk+ related support\" was the best way to go. This means that having USE=gtk3 to enable gtk+-3 instead of gtk+-2 support is forbidden.

\
This still leaves a few questions for maintainers to resolve hence the following policy:

-   package is an **application** with support for multiple gtk+, maintainer is **free to select whatever slot** he desires to support. It is strongly advised to use gtk+-3 if functionality is equivalent. This is to reduce workload of bugs being triggered with one slot but not the other.
-   package is a **library** shipping gtk+ based library only, it **must be slotted**. Working with upstream on this might be needed for those who do not understand the principles of soname and soversion.
-   package is shipping gtk+ based libraries and gtk+ based utilities. Package **must be slotted** and binaries should be suffixed with slot.
-   package is shipping gtk+ based libraries and non-gtk+ based libraries or utilities. Package **should be split** or if maintenance cost is too high, USE=gtk and USE=gtk3 is allowed to enable support for gtk+:2 and gtk+:3 respectively. This should concern a minority of packages like avahi, gtk-vnc, spice-gtk, etc.

\
Please note that loading a gtk+-3 based library in a gtk+-2 application will fail and crash the application so it is important to properly depend on relevant USE flags and slots.

\
Remember: **gtk USE flag means gtk+ support, whatever slot is needed by the package using it**

### [static-libs]

The Gnome team does not try to provide static libraries for all packages. This is not by laziness, this is just because most libraries being based on gtk+ and gtk+ not being static-linking friendly, this is not something we can have the luxury to spend our time on.

**We only add support for static libraries on user request.**

If for some reason your package provides static libraries, you are free to allow building them behind USE=static-libs, which is the current practice across the tree, as long as you can ensure that it does link correctly of makes working executables.

## [Other policies]

Policies below are not from the Gnome team, they are collected here for sharing purpose and should be annotated with historical references if possible.

### [ssl]

This is not a Gnome team policy per se, just a reminder from old discussions on gentoo-dev mailing list.

-   in case a package supports SSL or TLS for whatever it does with it, it must present this behind a USE=ssl flag.
-   in case multiple SSL backend library are allowed, they must each be presented by a corresponding USE flag, except for the maintainer chosen default and be enabled only when USE=ssl and USE=\$ is set.

For example, library foo has optional support SSL through gnutls, openssl and nss. It will have IUSE=\"ssl gnutls nss\". If user want to enable SSL, he/she will just emerge the package with USE=\"ssl\". If he/she wants SSL support through gnutls, he/she will emerge the package with USE=\"ssl gnutls\".

This policy probably needs updating due to EAPI 4 and 5 features.

### [avahi vs. zeroconf]

This is not a Gnome team policy per se, just a reminder from old discussions on [gentoo-dev mailing list](https://archives.gentoo.org/gentoo-dev/message/3b9c85fc02bf9b2fd1885af019ee96bc).

avahi is the library providing Zeroconf/Rendez-vous support and USE flag must be named after the feature/technology first so USE=zeroconf must be used.

### [jabber vs. xmpp]

This is not a Gnome team policy per se, just a reminder from old discussions on [gentoo-dev mailing list](https://archives.gentoo.org/gentoo-dev/message/93a070f036a9f58330ee164c23844a05).

Jabber is the service that promoted the XMPP protocol. USE flag must be named after the feature/technology first so USE=xmpp must be used.

1.  [[[↑](#cite_ref-1)] [[Submission of DISABLE_DEPRECATED patch](https://archives.gentoo.org/gentoo-dev/message/3d5f78203bf00858f7e99b83c72b3e7e)]]
2.  [[[↑](#cite_ref-2)] [[XDG environment variables related sandbox errors tracker bug](https://bugs.gentoo.org/show_bug.cgi?id=567192)]]