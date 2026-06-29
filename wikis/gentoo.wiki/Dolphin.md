[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dolphin&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

*Not to be confused with [the Dolphin console emulator](https://wiki.gentoo.org/wiki/Dolphin_emulator "Dolphin emulator").*

**Resources**

[[]][Home](https://apps.kde.org/dolphin/)

[[]][Package information](https://packages.gentoo.org/packages/kde-apps/dolphin)

[[]][GitHub](https://github.com/KDE)

**Dolphin** is [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")\'s file manager that allows navigating and browsing the contents of hard drives, USB sticks, SD cards, and more. Creating, moving, or deleting files and folders is simple and fast. It is written in C++ and [Qt](https://wiki.gentoo.org/wiki/Qt "Qt").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Tips]](#Tips)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Missing Associations when opening a file in Dolphin]](#Missing_Associations_when_opening_a_file_in_Dolphin)
        -   [[2.1.1] [Sourcing the Menu File]](#Sourcing_the_Menu_File)
        -   [[2.1.2] [Regenerating & Loading the Menu File]](#Regenerating_.26_Loading_the_Menu_File)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [kde-apps/dolphin](https://packages.gentoo.org/packages/kde-apps/dolphin) [[]] [Plasma filemanager focusing on usability]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+handbook`](https://packages.gentoo.org/useflags/+handbook)                 Enable handbooks generation for packages by KDE
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`semantic-desktop`](https://packages.gentoo.org/useflags/semantic-desktop)   Cross-KDE support for semantic search and information retrieval
  [`telemetry`](https://packages.gentoo.org/useflags/telemetry)                 Send anonymized usage information to upstream so they can better understand our users
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 20:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge Dolphin:

`root `[`#`]`emerge --ask kde-apps/dolphin`

### [Tips]

To get archive extraction capabilities within the contextual menu, [[[kde-apps/ark]](https://packages.gentoo.org/packages/kde-apps/ark)[]] can be installed.

## [Troubleshooting]

### [Missing Associations when opening a file in Dolphin]

When using Dolphin through some Window Managers (e.g. [Hyprland](https://wiki.gentoo.org/wiki/Hyprland "Hyprland")) without [[[kde-plasma/plasma-workspace]](https://packages.gentoo.org/packages/kde-plasma/plasma-workspace)[]] installed, opening a file may bring up a blank \"Choose Applications\" menu, even if compatible applications are installed. However, manually specifying an application still works.

This may further be confirmed by checking the logs and/or stdout of the offending application, and looking for a message similar to this:

    "applications.menu"  not found in  QList("/home/youruser/.config/menus", "/etc/xdg/menus")

This happens because no application has created the freedesktop.org Menu File^[\[1\]](#cite_note-1)^, which is responsible for populating this list. Usually, a desktop environment will handle this without user intervention- but in this case, the file is missing.

To fix this issue, first source a menu file, then ensure the \$XDG_MENU_PREFIX variable matches, then regenerate the KDE\'s cache of .desktop/MIME .XML files.

#### [Sourcing the Menu File]

Unfortunately, there is no good solution to sourcing a menu file.

-   KDE provides a Menu File in [[[kde-plasma/plasma-workspace]](https://packages.gentoo.org/packages/kde-plasma/plasma-workspace)[]]- specifically, `plasma-applications.menu`- which will play nicely with the KDE suite, including Dolphin. However, you may not want to emerge this package, as doing so will also install a complete Plasma workspace (if basic). Additionally, consider that this file is made for Plasma- and as such, if the Window Manager environment doesn\'t work well with Plasma\'s configs, this may not be the best option.
-   Most other Desktop Environments provide their own menu files, e.g. [[[gnome-base/gnome-menus]](https://packages.gentoo.org/packages/gnome-base/gnome-menus)[]], which can be used independent of their parent Desktop Environment.
-   There are several tools that can generate a menu file, such as [[[x11-misc/menumaker]](https://packages.gentoo.org/packages/x11-misc/menumaker)[]]. However, these tools are usually tailor-made for a small set of Window Managers, and may not work
-   Alternately, Menu Files can be created by-hand. These menu files are a variant on XML files^[\[2\]](#cite_note-2)^. An example of a flat menu without categories can be found here [\[1\]](https://github.com/mid-kid/config/blob/942efdde89bfd3f72b9a93ba91ee0c670c017811/i3/.config/menus/applications.menu). An editor for Menu Files may be helpful, such as [[[kde-plasma/kmenuedit]](https://packages.gentoo.org/packages/kde-plasma/kmenuedit)[]].

** Note**\
Many applications that need this file will first search for `applications.menu`, and prefer that file if existant. This will work the same way, which is fine\... but this preference may cause unexpected behavior if any packages attempt to use a different Menu File.

#### [][Regenerating & Loading the Menu File]

First, check your \$XDG_MENU_PREFIX variable. Its value has to match the prefix on the menu file, or vice-versa. If they do not match, you must change one or the other. Make sure this is set for your entire login session.

Then, add a line to your session init scripts to run the command `kbuildsycoca6`. This will regenerate the cache.

** Note**\
It\'s unclear if this line must be added. Per kbuildsycoca6\'s man page, this should be automatically regenerated by KService as soon as any of the underlying files change. However, many users have reported success by adding this to their configuration files.^[\[3\]](#cite_note-3)[\[4\]](#cite_note-4)^

Finally, log out and log back in.

## [See also]

-   [File managers](https://wiki.gentoo.org/wiki/File_managers "File managers") --- a computer program that allows for the manipulation of files and directories on a computer\'s [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").
-   [PCManFM](https://wiki.gentoo.org/wiki/PCManFM "PCManFM") --- a powerful yet lightweight file manager application, default file manager of [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE").
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.freedesktop.org/wiki/Specifications/menu-spec/](https://www.freedesktop.org/wiki/Specifications/menu-spec/)]]
2.  [[[↑](#cite_ref-2)] [[https://specifications.freedesktop.org/menu-spec/latest/menu-file-format.html](https://specifications.freedesktop.org/menu-spec/latest/menu-file-format.html)]]
3.  [[[↑](#cite_ref-3)] [[https://bbs.archlinux.org/viewtopic.php?pid=2167673#p2167673](https://bbs.archlinux.org/viewtopic.php?pid=2167673#p2167673)]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/prasanthrangan/hyprdots/issues/1406](https://github.com/prasanthrangan/hyprdots/issues/1406)]]