**Resources**

[[]][Home](http://elementary.io/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Elementary_OS "wikipedia:Elementary OS")

[[]][GitHub](https://github.com/elementary)

[[]][Ebuild repository](https://github.com/pimvullers/elementary)

**Pantheon** is a lightweight, modular desktop environment primarily written in Vala and GTK. It was originally written for use with Elementary OS, but is in the process of being ported to Gentoo.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [elementary ebuild repository (overlay)]](#elementary_ebuild_repository_.28overlay.29)
        -   [[1.1.1] [Method 1. eselect repostiory]](#Method_1._eselect_repostiory)
        -   [[1.1.2] [Method 2. repos.conf]](#Method_2._repos.conf)
    -   [[1.2] [Profile]](#Profile)
        -   [[1.2.1] [OpenRC]](#OpenRC)
        -   [[1.2.2] [systemd]](#systemd)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
    -   [[2.2] [package.use]](#package.use)
    -   [[2.3] [Keywording]](#Keywording)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Reporting issues]](#Reporting_issues)
-   [[5] [External resources]](#External_resources)

## [Prerequisites]

Users should be aware that the *elementary* [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") is undergoing rapid development, thus the following instructions are subject to significant changes.

### [][elementary ebuild repository (overlay)]

Pantheon currently resides in the elementary ebuild repository. There are two methods for installing repositories in Gentoo:

1.  The [eselect repository] method.
2.  The manual [repos.conf] method.

#### [Method 1. eselect repostiory]

Ensure [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] is installed. See [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") for full details.

`root `[`#`]`emerge --ask app-eselect/eselect-repostitory`

[eselect repository] will create an automatic repos.conf entry. When ready, run:

`root `[`#`]`eselect repository enable elementary `

`root `[`#`]`emaint sync --repo elementary `

#### [Method 2. repos.conf]

Create a file in the [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] directory (create the [repos.conf] directory first if it does not exist) called [elementary.conf]. Fill the file\'s contents with the following code:

[FILE] **`/etc/portage/repos.conf/elementary.conf`**

    [elementary]
    location = /var/db/repos/elementary
    sync-type = git
    sync-uri = https://github.com/pimvullers/elementary.git
    auto-sync = yes

Pull in the new repo:

`root `[`#`]`emaint sync --repo elementary`

### [Profile]

Profile changes can be non trivial. Please ensure the profile version, like 23.0 below, does not change without following the corresponding [news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base"). Avoid, for example, changing from an [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") profile to a [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") profile, or vice versa, without consulting the appropriate documentation.

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Profile_(Portage)#Changing_profile "Profile (Portage)") before performing any profile changes.

Setting a GNOME desktop profile for the system will help prepare the base system for pantheon to be installed:

#### [OpenRC]

When using OpenRC, select:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop/gnome`

#### [systemd]

** Warning**\
Read the [[systemd]](https://wiki.gentoo.org/wiki/Systemd "Systemd") documentation before changing to a [systemd] profile.

systemd users will need the GNOME profile with systemd on the end:

`root `[`#`]`eselect profile set default/linux/amd64/23.0/desktop/gnome/systemd`

## [Installation]

### [Emerge]

The pantheon meta-package pulls in the necessary packages. This can be done by emerging just the pantheon-base/pantheon-shell meta package and then select the desired elementary applications:

`root `[`#`]`emerge --ask pantheon-base/pantheon-shell`

Then, for example, emerge Audience and Pantheon terminal:

`root `[`#`]`emerge --ask media-video/audience x11-terms/pantheon-terminal`

### [package.use]

Ensure that `X` and `-gnome`USE flag is included in the system\'s global [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). It is also possible to remove the requirement of webkit-gtk by setting `gnome-online-accounts`

### [Keywording]

Those that wish to test the latest version of Pantheon then add the \~arch (unstable) keyword in order to allow the installation of the latest version of Pantheon package atoms. For now, only the **[\~amd64]** and **[\~x86]** keywords are supported (although in the future and with more testing other architectures may be supported, arch testers are always welcomed to help with this.)

It is wise to provide Portage with only the explicit instructions Patheon needs for (dependent) packages that require keywording. Copy the following list in the [package.accept_keywords] file:

[FILE] **`/etc/portage/package.accept_keywords`**

    pantheon-base/pantheon
    mail-client/postler
    pantheon-base/pantheon-shell
    gnome-base/gnome-desktop
    x11-themes/elementary-icon-theme
    x11-themes/elementary-theme
    x11-libs/granite
    dev-libs/folks
    pantheon-base/marlin
    dev-util/euclide
    media-sound/noise
    app-office/dexter
    net-libs/gnome-online-accounts
    app-editors/scratch
    pantheon-base/switchboard
    x11-terms/pantheon-terminal
    app-office/maya
    dev-db/sqlheavy
    pantheon-base/plank
    net-libs/liboauth
    x11-libs/bamf
    dev-libs/libgweather
    media-libs/clutter
    dev-python/rdflib
    dev-libs/libgdata
    x11-libs/pango
    dev-libs/glib
    dev-libs/libpeas
    gnome-base/gsettings-desktop-schemas
    media-libs/cogl
    x11-libs/varka
    pantheon-base/cerbere
    x11-libs/gtk+
    x11-wm/mutter
    x11-themes/elementary-wallpapers
    dev-libs/libindicator
    pantheon-base/slingshot
    app-dicts/lingo
    gnome-extra/zeitgeist
    dev-libs/libzeitgeist
    dev-libs/libpeas
    x11-wm/gala
    dev-libs/gobject-introspection
    pantheon-base/wingpanel
    x11-libs/gdk-pixbuf
    dev-libs/gobject-introspection-common
    dev-python/isodate
    gnome-extra/evolution-data-server
    x11-libs/vte
    dev-libs/libindicate
    app-office/ergo
    dev-lang/vala
    dev-libs/contractor
    dev-libs/libdbusmenu
    net-news/feedler
    dev-libs/libunity
    media-video/eidete
    media-video/audience
    pantheon-extra/dropoff
    app-office/footnote
    pantheon-base/pantheon-print
    mail-client/geary
    dev-libs/dee
    media-video/snap
    media-libs/clutter-gst
    media-video/cheese
    x11-libs/mx
    dev-util/fix-la-relink-command
    www-client/midori

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose pantheon-base/pantheon-shell`

## [Troubleshooting]

### [Reporting issues]

As mentioned in the beginning, the elementary repository is undergoing rapid development, just like the upstream elementary OS project. This means that things might break, or do not work properly yet. If you discover any issues, or if you want to contribute, just create a [new issue](https://github.com/pimvullers/elementary/issues/new) on the [elementary ebuild repository](https://github.com/pimvullers/elementary) Github project or contact the [maintainer](mailto:elementary@vullersmail.nl).

## [External resources]

-   [Launchpad page (for Pantheon developers).](https://launchpad.net/elementary)
-   [OS\' old distribution location (deprecated as of 2015-04-11).](http://sourceforge.net/projects/elementaryos/Elementary)