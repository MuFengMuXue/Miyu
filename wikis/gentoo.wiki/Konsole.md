[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Konsole&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://konsole.kde.org)

[[]][Package information](https://packages.gentoo.org/packages/kde-apps/konsole)

[[]][GitHub](https://github.com/KDE)

**Konsole** is [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")\'s [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [kde-apps/konsole](https://packages.gentoo.org/packages/kde-apps/konsole) [[]] [KDE\'s terminal emulator]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+handbook`](https://packages.gentoo.org/useflags/+handbook)   Enable handbooks generation for packages by KDE
  [`X`](https://packages.gentoo.org/useflags/X)                   Add support for X11
  [`debug`](https://packages.gentoo.org/useflags/debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 11:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask kde-apps/konsole`

## [Configuration]

To make the title of a process running in Konsole (e.g. [emerge]) visible in the tab title or window titlebar, add `%w` (window title set by shell) to the `Tab title format`, under \'Tabs\' in the Konsole profile.

## [See also]

-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).