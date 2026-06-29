EAPI 5 introduces two new features related to [slots](https://wiki.gentoo.org/wiki/SLOT "SLOT") and slot dependencies: sub-slots and slot-operators. Slot-operators allow the dependencies of a package to be specified such that slot changes either will (`:=`) or won\'t (`:*`) trigger a rebuild of itself. Sub-slots allow a package to trigger slot-operator rebuilds without needing to explicitly re-SLOT (and therefore allow concurrent installation of) different versions.

The practical upshot of these two features is that when used properly, they will allow portage to determine what packages in the system need to be re-emerged when certain libraries or dependencies are upgraded, thus including them in the emerge list when running [emerge -uDNav \@world], and hopefully eliminating the need for [revdep-rebuild] and other package-rebuild scripts.

## Contents

-   [[1] [Basic example]](#Basic_example)
-   [[2] [Real-world examples]](#Real-world_examples)
    -   [[2.1] [Libtool libraries]](#Libtool_libraries)
    -   [[2.2] [Making perl-cleaner obsolete]](#Making_perl-cleaner_obsolete)
        -   [[2.2.1] [1. Ebuilds for dev-lang/perl need to be sub-slotted]](#1._Ebuilds_for_dev-lang.2Fperl_need_to_be_sub-slotted)
        -   [[2.2.2] [2. perl-module.eclass needs to be updated]](#2._perl-module.eclass_needs_to_be_updated)
        -   [[2.2.3] [3. Dependencies need to be updated for optional Perl modules]](#3._Dependencies_need_to_be_updated_for_optional_Perl_modules)
    -   [[2.3] [Multiple ABIs for X.Org]](#Multiple_ABIs_for_X.Org)
        -   [[2.3.1] [Sub-slotting method]](#Sub-slotting_method)
        -   [[2.3.2] [Use virtuals]](#Use_virtuals)
-   [[3] [External resources]](#External_resources)

## [Basic example]

An overlay contains the following packages, all containing \"SLOT=0\":

    dev-libs/libfoo-1.0
    dev-libs/libfoo-2.0
    dev-libs/libbar-1.0
    dev-libs/libbar-2.0
    app-misc/baz-1.0

app-misc/baz-1.0 contains the following:

    RDEPEND="
     dev-libs/libfoo
     dev-libs/libbar
    "

and after being built, installs [/usr/bin/baz] which is linked to [libfoo.so.1] and [libbar.so].

Without sub-slots and slot-operators, if libfoo-1.0 was upgraded to libfoo-2.0, then \'baz\' would break until re-emerged (i.e. with [revdep-rebuild]). However, we can add slot-operators to the dependencies within app-misc/baz-1.0:

    RDEPEND="
     dev-libs/libfoo:=
     dev-libs/libbar:*
    "

\...and sub-slots to the libraries:

    dev-libs/libfoo-1.0: SLOT="0/1"
    dev-libs/libfoo-2.0: SLOT="0/2"
    dev-libs/libbar-1.0: SLOT="0/1"
    dev-libs/libbar-2.0: SLOT="0/2"

\...would mean that the upgrade of libfoo from 1.0 to 2.0 would automatically trigger a rebuild of package \'baz\'. Also, since baz is linked to any \'libbar\', the upgrade of libbar from 1.0 to 2.0 would -not- automatically trigger a needless rebuild of \'baz\'.

## [Real-world examples]

The following are projects that have been test-implemented on axs\'s developer overlay ([layman -a axs]). They are presented here to show possible best practices of implementing sub-slots and slot-operators.

### [Libtool libraries]

The majority of breakages caused by dependency updates relate to changes in the SONAME of libtool libraries. The most naive approach to fixing this would be to specify a sub-slot for the library ebuild that matches the \$ version in the soname, and use \':=\' slot operators for all ebuilds that RDEPEND on this package. Example:

    xcb-util-0.3.8.ebuild: SLOT="0/0" (as it installs libxcb-util.so.0)
    xcb-util-0.3.9.ebuild: SLOT="0/1" (as it installs libxcb-util.so.1)

    xf86-video-intel-2.19.0.ebuild:
      RDEPEND="dev-libs/xcb-util:="

### [Making perl-cleaner obsolete]

When Perl is upgraded, Perl modules generally need to be reinstalled as they are no longer installed against (or in the right path of) the current version of Perl. Slot-operators and sub-slots can help with this, by triggering rebuilds. Fortunately, all packages that install Perl modules do so via the \'perl-module\' eclass, and so implementing this is very straight-forward and requires very few changes.

#### [][1. Ebuilds for dev-lang/perl need to be sub-slotted]

As only one version of [[[dev-lang/perl]](https://packages.gentoo.org/packages/dev-lang/perl)[]] can be installed at a time, sub-slots are used to define the actual version of Perl while enforcing SLOT=\"0\" behaviour. [perl-cleaner](https://wiki.gentoo.org/wiki/Project:Perl/perl-cleaner "Project:Perl/perl-cleaner") needs only be run when changing \$.\$ versions, and so we will use this for the sub-slot:

    dev-lang/perl-5.12.4.ebuild:SLOT="0/5.12"

Note that a modified \$ could have been used instead of an explicit specification.

#### [2. perl-module.eclass needs to be updated]

In the standard case, perl-module.eclass is in charge of assigning [[[dev-lang/perl]](https://packages.gentoo.org/packages/dev-lang/perl)[]] to \$DEPEND for the ebuilds that inherit it. As such, change the dev-lang/perl atom so that it includes the \':=\' slot operator will automatically trickle down to the perl-module packages.

                    case "$" in
                    yes)
    +                       case "$" in
    +                       5)
    +                               DEPEND="dev-lang/perl:=[-build]"
    +                               ;;
    +                       *)
                                    DEPEND="dev-lang/perl[-build]"
    +                               ;;
    +                       esac
                            RDEPEND="$"
                            ;;
                    esac

#### [3. Dependencies need to be updated for optional Perl modules]

Some packages install their modules based on USE=\"perl\", and have GENTOO_DEPEND_ON_PERL=no set in the ebuild. These packages therefore depend directly on dev-lang/perl and need to have their dependencies updates with the \':=\' slot operator.

    app-misc/g15daemon-1.9.5.3-r5:
     DEPEND="perl? (
    -               dev-lang/perl
    +               dev-lang/perl:=
                    dev-perl/GDGraph
                    >=dev-perl/Inline-0.4
             )

### [Multiple ABIs for X.Org]

x11-base/xorg-server provides three ABIs for various modules (like x11-drivers/\*) that build against it: the \'VIDEODRV\' abi, the \'XINPUT\' abi, and the \'EXTENSION\' abi. Any given version of xorg-server might (or might not) bump any or all of these abis. There are two ways to handle automatic rebuilding of x11-drivers/\* et al. against an upgraded xorg-server:

#### [Sub-slotting method]

The first would follow the dev-lang/perl example above, where xorg-server ebuild would be sub-slotted. However, the sub-slot would need to change every time any of the ABIs changed. A value such as:

    SLOT="0/13.0-18.0-7.0"

\...would work for this as the sub-slot string is made up of the individual ABI versions in the xorg-server sources. Unfortunately, though, this means that all installed x11-drivers/\* would re-emerge on an xorg-server upgrade, even if the abi relevant to that particular package didn\'t change.

#### [Use virtuals]

The second option is to add virtuals for each independent ABI. This has the advantage of being more accurate, since packages can RDEPEND on the particular ABI needed from xorg-server, and therefore each driver will only be rebuilt when the appropriate ABI is bumped. However, from a developer\'s perspective it is significantly more work, as instead of one package to maintain there are four, and both the ABIs themselves as well as the KEYWORDS between them will need to be kept in sync between the xorg-server ebuilds and ebuilds for the relevant virtuals. Although this process can be scripted to avoid the necessary manual lifting, if things get out of sync the end-user experience will suffer greatly.

For this example, we will assume the tree only contains two versions of xorg-server: 1.12.2 and 1.12.4.

    xorg-server-1.12.2:  VIDEODRV_ABI = 12.0 ; XINPUT_ABI = 16.0 ; EXTENSION_ABI = 6.0
    xorg-server-1.12.4:  VIDEODRV_ABI = 12.1 ; XINPUT_ABI = 16.0 ; EXTENSION_ABI = 6.0

1\. Create virtuals for each provided ABI, and ebuilds for each relevant version of said abi

    virtual/x-video-abi/x-video-abi-12.0.ebuild
    virtual/x-video-abi/x-video-abi-12.1.ebuild
    virtual/x-input-abi/x-input-abi-16.0.ebuild
    virtual/x-extension-abi/x-extension-abi-6.0.ebuild

2\. The ebuild contents of each virtual abi is very simple:

    virtual/x-video-abi/x-video-abi-12.0.ebuild:
    # Copyright 1999-2012 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Header: /var/cvsroot/gentoo-x86/virtual/x-video-abi/x-video-abi-0.ebuild,v 1.2 2012/03/07 04:11:36 axs Exp $

    EAPI="5_pre2"
    DESCRIPTION="Virtual for indicating the $abi ABI version of xorg-server"
    HOMEPAGE=""
    SRC_URI=""
    LICENSE=""
    SLOT="0/\$"
    KEYWORDS="alpha amd64 arm hppa ia64 ~mips ppc ppc64 sh sparc x86 ~amd64-fbsd ~x86-fbsd"
    IUSE=""

As the abi can be specified as the package version, this eliminates the need to use an explicit sub-slot. The only difference between each ebuild is the KEYWORDS, as they need to match the xorg-server version in order to keep the virtuals from forcing an upgrade to xorg-server.

    change to make x-video-abi-12.1.ebuild:
     SLOT="0/\$"
    -KEYWORDS="alpha amd64 arm hppa ia64 ~mips ppc ppc64 sh sparc x86 ~amd64-fbsd ~x86-fbsd"
    +KEYWORDS="~alpha ~amd64 ~arm ~hppa ~ia64 ~mips ~ppc ~ppc64 ~sh ~sparc ~x86 ~amd64-fbsd ~x86-fbsd"
     IUSE=""

Note that there are no \*DEPEND in the virtuals. This is because xorg-server will use a `PDEPEND` on the specific virtuals they provide; this matches what already occurs with the \'xorg-drivers\' meta-package.

    xorg-sever-1.12.2.ebuild:
     PDEPEND="
    +        ~virtual/x-video-abi-12.0
    +        ~virtual/x-input-abi-16.0
    +        ~virtual/x-extension-abi-6.0
             xorg? ( >=x11-base/xorg-drivers-$(get_version_component_range 1-2) )"

    xorg-sever-1.12.4.ebuild:
     PDEPEND="
    +        ~virtual/x-video-abi-12.1
    +        ~virtual/x-input-abi-16.0
    +        ~virtual/x-extension-abi-6.0
             xorg? ( >=x11-base/xorg-drivers-$(get_version_component_range 1-2) )"

Testing locally by axs has shown that using `PDEPEND` is the easiest way to ensure that the correct versions of the virtuals are emerged when xorg-server is upgraded or downgraded. Due to xorg-server generally providing multiple versions pf packages at both stable and \~arch keywords, it is difficult to control versioning with only minimum version dependencies, and exact dependencies would need to be bumped every time a new xorg-server ebuild was added to the tree even though ABIs might not change. Also there is the issue of keeping the virtuals properly in sync (and the package manager giving relevant warnings) when an end-user is masking, unmasking, or \~arch keywording just the xorg-server ebuild itself. The `PDEPEND` method above seems to provide the best overall end-user and developer experience at this juncture.

## [External resources]

-   [Devmanual: EAPI Usage and Description -\> EAPI 5 -\> EAPI 5 Metadata](https://devmanual.gentoo.org/ebuild-writing/eapi/#eapi-5-metadata)
-   [Devmanual: Master Index -\> General Concepts -\> Slotting](https://devmanual.gentoo.org/general-concepts/slotting/)