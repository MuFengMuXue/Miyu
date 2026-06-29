**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/X_resources "wikipedia:X resources")

Also known as the [\~/.Xresources] file.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Syntax]](#Syntax)
    -   [[2.1] [Comments]](#Comments)
    -   [[2.2] [Wildcards]](#Wildcards)
    -   [[2.3] [Constants]](#Constants)
    -   [[2.4] [Includes]](#Includes)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Introduction]

X resources are configuration options for X applications such as the [rxvt-unicode](https://wiki.gentoo.org/wiki/Rxvt-unicode "Rxvt-unicode") terminal emulator. They can also be used for setting the [cursor theme](https://wiki.gentoo.org/wiki/Cursor_themes "Cursor themes"). X resources can be set in [\~/.Xresources].

While most display managers will automatically load this configuration file on startup, it is possible to load the configuration manually by running:

`user `[`$`]`xrdb ~/.Xresources`

The [xrdb] command is provided by the [[[x11-apps/xrdb]](https://packages.gentoo.org/packages/x11-apps/xrdb)[]] package.

## [Syntax]

Configuration options in the [\~/.Xresources] file should respect the following component syntax:

*`name`*`.`*`Class`*`.`*`resource`*`: `*`value`*

** Note**\
In many options the *Class* component is not used.

Examples of existing configuration options:

-   `Xcursor.theme: redglass`
-   `xscreensaver.Dialog.background: #111111`

### [Comments]

Comments start with an exclamation mark or with double slashes. For example:

[CODE]

    ! This is a comment

    // This is also a comment

    /* Multiline comments
    are supported
    as well */

### [Wildcards]

It is possible to use `?` and `*` wildcards to apply a single rule to multiple configuration options. The `?` matches any single component. The `*` matches zero or more components. For example:

`*background: #000000` - Set the given value to all programs/classes which contain a component named *background*.

### [Constants]

Constants can be defined in the following way:

`#define `*`name`*` `*`value`* (for example `#define black #000000`).

### [Includes]

The main [\~/.Xresources] file can be composed of multiple sub-files (e.g. on a per-application basis). The includes can be defined as:

`#include "`*`file_name`*`"`

Example of including application sub-files:

[FILE] **`~/.Xresources`**

    #include ".Xresources.d/urxvt"
    #include ".Xresources.d/xft"

## [See also]

-   [Cursor themes](https://wiki.gentoo.org/wiki/Cursor_themes "Cursor themes") --- provides instructions for cursor theme management on an X11-based system.
-   [Rxvt-unicode](https://wiki.gentoo.org/wiki/Rxvt-unicode "Rxvt-unicode") --- a fast and lightweight [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") with [Xft](https://en.wikipedia.org/wiki/Xft "wikipedia:Xft") and [Unicode](https://en.wikipedia.org/wiki/Unicode "wikipedia:Unicode") support.

## [External resources]

-   [Article on the Arch Linux wiki](https://wiki.archlinux.org/index.php/X_resources)