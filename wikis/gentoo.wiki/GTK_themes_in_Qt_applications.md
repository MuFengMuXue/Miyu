[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GTK_themes_in_Qt_applications&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This guide will explain how to set up Qt to adopt the same style as GTK.

## Contents

-   [[1] [Setup]](#Setup)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Qt5]](#Qt5)
    -   [[2.2] [Qt3 / Qt4]](#Qt3_.2F_Qt4)
    -   [[2.3] [Tips]](#Tips)
-   [[3] [GTK 2 alternative]](#GTK_2_alternative)
-   [[4] [External resources]](#External_resources)

## [Setup]

The GTK style for Qt can be built by setting the `gtk` `USE` flag for [[[dev-qt/qtwidgets]](https://packages.gentoo.org/packages/dev-qt/qtwidgets)[]].

Set the `gtk` `USE` flag:

[FILE] **`/etc/portage/package.use`**

    dev-qt/qtwidgets gtk

Now rebuild the package with its new `USE` flag:

`root `[`#`]`emerge --ask --changed-use --oneshot dev-qt/qtwidgets`

## [Configuration]

### [Qt5]

** Note**\
This section is a stub (it explains what to do but not how to do it). You can help by completing it.

Qt5 will try to inherit the configuration of the current desktop environment.

In some desktop environments, Qt5 does not pick up the configuration. This can sometimes be fixed by using the GNOME or KDE desktop preference utility and setting the `XDG_CURRENT_DESKTOP` environment variable to `KDE` or `GNOME` respectively.

Alternatively you could use the [[[x11-misc/qt5ct]](https://packages.gentoo.org/packages/x11-misc/qt5ct)[]] application and set the `QT_QPA_PLATFORMTHEME` environment variable to `qt5ct`. The \"oxygen\" icon packs may sometimes be necessary.

### [][Qt3 / Qt4]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=GTK_themes_in_Qt_applications&action=edit).

** Note**\
Qt5 doesn\'t have the [qtconfig] program. When encountering the following error, an alternative configuration method should be used:

    qtconfig: could not exec '/usr/lib64/qt5/bin/qtconfig': No such file or directory

Reselecting the preferred theme may be necessary for Qt applications using [qtconfig] (from [[[dev-qt/qt3support]](https://packages.gentoo.org/packages/dev-qt/qt3support)[]]):

`user `[`$`]`qtconfig`

Alternatively, the previous configuration files may be removed:

`user `[`$`]`rm -r ~/.config/Trolltech*`

Select the **Default** theme to use the system settings or set it to use the **GTK** style explicitly by selecting **GTK** theme.

### [Tips]

-   Individual applications might have their own configuration settings for their GUI, e.g. in VLC this is located in Tools → Preferences.

## [GTK 2 alternative]

An alternative for users of GTK 2 and Qt5 is using the QtCurve cross-toolkit theme:

`root `[`#`]`emerge --ask x11-themes/qtcurve`

The downsides of this method are that it\'s not available for GTK 3 yet, and currently the only configuration GUI needs Qt5 and KDE Frameworks 5.

## [External resources]

-   [*Uniform look for Qt and GTK applications*](https://wiki.archlinux.org/index.php/Uniform_look_for_Qt_and_GTK_applications) on Archlinux\'s wiki
-   [*Configuration of Qt5 apps under environments other than KDE Plasma*](https://wiki.archlinux.org/index.php/qt#Configuration_of_Qt5_apps_under_environments_other_than_KDE_Plasma) on Archlinux\'s wiki