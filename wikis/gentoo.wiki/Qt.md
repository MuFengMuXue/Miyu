[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Qt&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Qt "Project:Qt")][Project](https://wiki.gentoo.org/wiki/Project:Qt "Project:Qt")

[[]][Home](https://www.qt.io/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Qt_(software) "wikipedia:Qt (software)")

[[]][GitHub](https://github.com/gentoo/qt)

[[]][[#qt](ircs://irc.libera.chat/#qt)] ([[webchat](https://web.libera.chat/#qt)])

**Qt** (pronounced as /ˈkjuːt/ \"cute\") is a cross-platform application framework that is widely used for developing application software with a graphical user interface (GUI) (in which cases Qt is classified as a widget toolkit), and also used for developing non-GUI programs such as command-line tools and consoles for servers^[\[1\]](#cite_note-1)^.

The current major release of Qt is Qt6^[\[2\]](#cite_note-2)^.

In Gentoo, the ebuilds for Qt and related packages are maintained by [a dedicated team](https://wiki.gentoo.org/wiki/Project:Qt "Project:Qt"). This team also maintains [the official qt overlay](https://gitweb.gentoo.org/proj/qt.git). They are very open to user contributions and volunteers who want to become new developers.

** Important**\
2025-11-04: Due to the increasing effort required, 5.15.18 will be the last bump of Qt5 in Gentoo. Refer to [this post of 2025-08-19](https://public-inbox.gentoo.org/gentoo-dev/1932068.CQOukoFCf9@tuxbrain.fritz.box/) and [this post of 2025-11-02](https://public-inbox.gentoo.org/gentoo-dev/2034629.PYKUYFuaPT@localhost/) for further information.

## Contents

-   [[1] [Installing the Qt libraries]](#Installing_the_Qt_libraries)
-   [[2] [Qt-based desktop environments]](#Qt-based_desktop_environments)
-   [[3] [Compiling programs that use qmake and need Qt5]](#Compiling_programs_that_use_qmake_and_need_Qt5)
-   [[4] [Theming]](#Theming)
    -   [[4.1] [Qt theming outside of KDE]](#Qt_theming_outside_of_KDE)
        -   [[4.1.1] [Kvantum]](#Kvantum)
-   [[5] [Environment variables]](#Environment_variables)
-   [[6] [Frequently asked questions]](#Frequently_asked_questions)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installing the Qt libraries]

Most users will not need to install the Qt libraries intentionally, but can just let them be pulled in as dependencies of the applications they want to use. For those who want the complete set (e.g. for software development purposes), there are [sets](https://gitweb.gentoo.org/proj/qt.git/tree/sets) in the overlay for Qt5.

## [Qt-based desktop environments]

There are currently two Qt-based desktop environments available in Gentoo. The most well-known and best developed one is [KDE Plasma](https://wiki.gentoo.org/wiki/KDE#Plasma "KDE"). There is also a younger and more \"light-weight\" DE: [LXQt](https://wiki.gentoo.org/wiki/LXQt "LXQt") (a merge of Razor-Qt and LXDE). These can be complemented with [KDE Applications](https://wiki.gentoo.org/wiki/KDE#Applications "KDE") and packages from the [Qt Desktop applications](https://wiki.gentoo.org/wiki/Qt_Desktop_applications "Qt Desktop applications") list.

## [Compiling programs that use qmake and need Qt5]

Programs that need Qt5 will need its version of qmake. It is located in [/usr/lib/qt5/bin] and needs to be executed with its full path (i.e., [/usr/lib/qt5/bin/qmake]). After it\'s run, compilation will just work.

Alternatively, one can use [[[dev-qt/qtchooser]](https://packages.gentoo.org/packages/dev-qt/qtchooser)[]] functionality in the development environment. Start with:

`user `[`$`]`qtchooser --help`

## [Theming]

In the context of Qt, a [theme] is a particular combination of \'style\', \'icon theme\', and \'color theme\'.

The default *style* of KDE Plasma is [Breeze], provided by the [[[kde-plasma/breeze]](https://packages.gentoo.org/packages/kde-plasma/breeze)[]] package; the Breeze icon theme is provided by [[[kde-frameworks/breeze-icons]](https://packages.gentoo.org/packages/kde-frameworks/breeze-icons)[]]. A \'Breeze\' theme is also available for [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") ([[[kde-plasma/breeze-grub]](https://packages.gentoo.org/packages/kde-plasma/breeze-grub)[]]) and [Plymouth](https://wiki.gentoo.org/wiki/Plymouth "Plymouth") ([[[kde-plasma/breeze-plymouth]](https://packages.gentoo.org/packages/kde-plasma/breeze-plymouth)[]]).

There doesn\'t appear to be any [XDG directory](https://wiki.gentoo.org/wiki/XDG_directories "XDG directories") specification for themes in general (although there is a specification for [icon themes](https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html) in particular). However, common locations for themes include [\$XDG_DATA_HOME/themes/] and [\~/.themes/].

### [Qt theming outside of KDE]

The primary way to theme Qt applications in a non-KDE environment is [qt6ct], provided by the [[[gui-apps/qt6ct]](https://packages.gentoo.org/packages/gui-apps/qt6ct)[]] package. To use it, ensure that the `QT_QPA_PLATFORMTHEME` is set to `qt6ct` in your environment, e.g. via [\~/.bash_profile]:

[FILE] **`~/.bash_profile`**

    export QT_QPA_PLATFORMTHEME=qt6ct

Themes, as well as things such as preferred fonts, can then be selected by running [qt6ct].

By default, chosen settings are saved to the [\$XDG_CONFIG_HOME/qt6ct/] directory (e.g. [/home/larry/.config/qt6ct/], which is referenced by Qt applications during startup.

However, it is also possible to directly specify a theme without using [qt6ct] by setting the `QT_STYLE_OVERRIDE` variable in your environment, e.g.

[FILE] **`~/.bash_profile`**

    export QT_STYLE_OVERRIDE=adwaita

Additionally, it is possible to pass a style name directly to a Qt application by using the `-style` option. For example, to use the adwaita-dark style ([[[x11-themes/adwaita-qt]](https://packages.gentoo.org/packages/x11-themes/adwaita-qt)[]]) with [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark"):

`user `[`$`]`wireshark -style adwaita-dark`

#### [Kvantum]

[Kvantum] ([[[x11-themes/kvantum]](https://packages.gentoo.org/packages/x11-themes/kvantum)[]]) is an SVG-based system that provides a \'kvantum\' Qt style instead of a platform theme, and then allowing the selection of specific Kvantum styles via the Kvantum system. It can be used by selecting \"kvantum\" as the style in [qt6ct], or by setting the `QT_STYLE_OVERRIDE` environment variable (described above) to `kvantum`.

Kvantum styles can be previewed and selected by running the [kvantummanager] program (or simply previewed by running the [kvantumpreview] program). As of Kvantum 1.1.2, these programs are only built and installed if the `kde` USE flag is enabled on the [[[x11-themes/kvantum]](https://packages.gentoo.org/packages/x11-themes/kvantum)[]] package.

## [Environment variables]

The following tables lists some of the Qt-specific environment variables available.

  ---------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Variable                                       Notes
  `QT_LOGGING_RULES`                  Can be used to help debug issues with Qt applications; refer to [this page on the KDE Community Wiki](https://community.kde.org/Guidelines_and_HOWTOs/Debugging/Using_Error_Messages) for details.
  `QT_QPA_PLATFORMTHEME`              Can be used to specify a theme directly, or set to `qt5ct` to utilize qtct to specify a theme. Refer to the \"[Qt theming outside of KDE](#Qt_theming_outside_of_KDE)\" section, above, for more information.
  `QT_SCALE_FACTOR_ROUNDING_POLICY`   Specifies policy for scaling on High DPI displays. Note also [this comment on how it can affect font rendering](https://bugs.kde.org/show_bug.cgi?id=479891#c27C).
  `QT_STYLE_OVERRIDE`                 Can be used to directly specify a theme without using qtct. Refer to the \"[Qt theming outside of KDE](#Qt_theming_outside_of_KDE)\" and \"[Kvantum](#Kvantum)\" sections, above, for more information.
  ---------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Frequently asked questions]

Please see the [Qt/FAQ](https://wiki.gentoo.org/wiki/Qt/FAQ "Qt/FAQ") page.

## [External resources]

-   [Arch Wiki article about Qt](https://wiki.archlinux.org/index.php/Qt)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://en.wikipedia.org/wiki/Qt\_(software)](https://en.wikipedia.org/wiki/Qt_(software))]]
2.  [[[↑](#cite_ref-2)] [[https://www.qt.io/development/qt-framework/release-cycle](https://www.qt.io/development/qt-framework/release-cycle)]]