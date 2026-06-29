[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wofi&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://hg.sr.ht/~scoopta/wofi)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/wofi)

**Wofi** is a launcher/menu program for wlroots-based [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") [compositors](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland#Compositors "List of software for Wayland"), such as [Sway](https://wiki.gentoo.org/wiki/Sway "Sway").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Configuration]](#Configuration)
    -   [[1.3] [Usage]](#Usage)
-   [[2] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/wofi`

### [Configuration]

Information about configuring Wofi can be found in the [wofi(5)](https://manpages.debian.org/bookworm/wofi/wofi.5.en.html) man page.

### [Usage]

One way to use Wofi is to create a simple shell script, e.g. [wofi_run.sh], which runs Wofi with a standard set of options and the list of items passed to it:

[FILE] **`wofi_run.sh`**

    #!/bin/sh

    wofi --width=400 --height=260 --hide-scroll --show="$"

Then, to open a dialog box with a list of programs to run:

`user `[`$`]`wofi_run.sh run`

For further details about running wofi, refer to the [wofi(1)](https://manpages.debian.org/bookworm/wofi/wofi.1.en.html) man page. Information about modes available for the `--show` option can be found in the [wofi(7)](https://manpages.debian.org/bookworm/wofi/wofi.7.en.html) man page.

## [See also]

-   [[[x11-misc/rofi]](https://packages.gentoo.org/packages/x11-misc/rofi)[]] - A window switcher, run dialog and dmenu replacement.