**[] Deprecated article**\
\
This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

Sawfish packages was removed from Gentoo repository ([[[bug #637978]](https://bugs.gentoo.org/show_bug.cgi?id=637978)[]])

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://sawfish.tuxfamily.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/sawfish)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Sawfish_(window_manager) "wikipedia:Sawfish (window manager)")

[[]][GitHub](https://github.com/SawfishWM/sawfish)

**Sawfish** is an extensible [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") using a Lisp-based scripting language. Its policy is very minimal compared to most window managers. Its aim is simply to manage windows in the most flexible and attractive manner possible. All high-level WM functions are implemented in Lisp for future extensibility or redefinition. These are some of the features that set Sawfish apart from other window managers:

-   Event hooking: For many events (moving windows etc.) you can customize the way Sawfish will respond.
-   Window matching: When windows are created you can match them to a set of rules and automatically perform actions on them.
-   Flexible theming: Sawfish allows for very different themes to be created and a variety of third-party themes are readily available.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Install [[[x11-wm/sawfish]](https://packages.gentoo.org/packages/x11-wm/sawfish)[]]:

`root `[`#`]`emerge --ask x11-wm/sawfish`

## [Configuration]

There are two ways; using the configurator GUI, or preparing lisp code. The GUI can be run by middle-clicking background -\> \"Customize\". Most customizations similar to other window managers can be done through GUI.

For customizations by lisp, first understand that in the startup, three files are read, in the order: [sawfish-defaults], [\~/.sawfish/custom], [.sawfishrc].

## [External resources]

-   [Sawfish Wiki](http://sawfish.wikia.com)
-   [Sawfish FAQ](http://sawfish.wikia.com/wiki/FAQ)