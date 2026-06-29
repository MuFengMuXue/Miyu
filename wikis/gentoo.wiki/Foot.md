This page contains [[changes](https://wiki.gentoo.org/index.php?title=Foot&diff=1318748)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Foot&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

\

**Resources**

[[]][Home](https://codeberg.org/dnkl/foot)

[[]][Package information](https://packages.gentoo.org/packages/gui-apps/foot)

**Foot** is a minimalist terminal emulator for Wayland written in C.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Font/text configuration]](#Font.2Ftext_configuration)
    -   [[2.2] [Server mode configuration]](#Server_mode_configuration)
    -   [[2.3] [Scrollback configuration]](#Scrollback_configuration)
    -   [[2.4] [Color configuration]](#Color_configuration)
    -   [[2.5] [Example Configuration]](#Example_Configuration)
        -   [[2.5.1] [Minimal Configuration]](#Minimal_Configuration)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Terminal break after SSHing]](#Terminal_break_after_SSHing)
        -   [[4.1.1] [SSH with TERM set]](#SSH_with_TERM_set)
        -   [[4.1.2] [Install terminfo files on destination]](#Install_terminfo_files_on_destination)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

** Note**\
As of the time of writing, the Gentoo package for [foot] doesn\'t support pgo because of inconsistent/poor results, see [[[bug #873625]](https://bugs.gentoo.org/show_bug.cgi?id=873625)[]], in contrast with the upstream benchmarks. ^[\[1\]](#cite_note-1)^

### [USE flags]

### [USE flags for] [gui-apps/foot](https://packages.gentoo.org/packages/gui-apps/foot) [[]] [Fast, lightweight and minimalistic Wayland terminal emulator]

  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+grapheme-clustering`](https://packages.gentoo.org/useflags/+grapheme-clustering)   Enable grapheme clustering support
  [`test`](https://packages.gentoo.org/useflags/test)                                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`utempter`](https://packages.gentoo.org/useflags/utempter)                           Enable utmp support via sys-libs/libutempter
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)                       Verify upstream signatures on distfiles
  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 09:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask gui-apps/foot`

## [Configuration]

Foot\'s user configuration is found at [\~/.config/foot/foot.ini]. The file and directory won\'t be created by default. A template can be found in [/etc/xdg/foot/foot.ini] or [from the upstream repository](https://codeberg.org/dnkl/foot/src/branch/master/foot.ini).

** Tip**\
Detailed information about all config parameters can be viewed with [man foot.ini]

To create the directory for the foot config and copy the example:

`user `[`$`]`mkdir ~/.config/foot`

`user `[`$`]`cp /etc/xdg/foot/foot.ini .config/foot/foot.ini`

### [][Font/text configuration]

Foot has several font configuration options, the `font` parameter can be used to set the terminal font. `font-bold`, `font-italic`, and `font-bold-italic` will automatically try to use variants of the primary font, but can be overridden. `letter-spacing`, `horizontal-letter-offset`, `vertical-letter-offset`, `underline-offset`, `box-drawings-uses-font-glyphs`, and `dpi-aware` options are also available.

[FILE] **`~/.config/foot/foot.ini`Set the font to 8pt Inconsolata**

    font=Inconsolata:size=8

### [Server mode configuration]

Foot supports the operation of a daemon which can be used to reduce overhead. The server handles all wayland communication, VT parsing, and rendering. Additionally, fonts are cached in a single thread, reducing overall memory usage.

** Warning**\
When using the daemon, all clients input and output are multiplexed on a single thread. If a single terminal is very busy, that could cause the rest of slow down as well, this can be mitigated by adding more worker threads. Additionally, if the server crashes **all** clients will crash.

[FILE] **`~/.config/foot/foot.ini`Increase the number of worker threads to use for rendering**

    workers=32

Foot can be started as a server by running [foot -s], this can be added to a window manager startup script to enable it upon login:

[FILE] **`~/.config/sway/config`Start Foot server with Sway if foot-client is the chosen terminal**

    set $term footclient
    exec foot -s

Once the server has been started, clients can be started with [footclient].

** Warning**\
If the configuration file has been updated, the server must be restarted before the configuration is reloaded, this will end all client sessions.

### [Scrollback configuration]

The number of lines saved in the scrollback can be adjusted with:

[FILE] **`~/.config/foot/config`Increase the scrollback length to 16384**

    [scrollback]
    lines=16384

[FILE] **`~/.config/foot/config`Show scrollback positions as a percentage**

    [scrollback]
    indicator-format=percentage

** Note**\
Foot will automatically round the `lines` value up to the nearest power of 2

### [Color configuration]

Colors can be specified with the `foreground`, `background`, `regular`, and `bright` parameters.

The order is `Black`, `Red`, `Green`, `Yellow`, `Blue`, `Magenta`, `Cyan`, `White`.

[FILE] **`~/.config/foot/foot.ini`Dark+**

    [colors]
    foreground=cccccc
    background=1e1e1e

    regular0=000000 # black
    regular1=cd3131 # red
    regular2=0dbc79 # green
    regular3=e5e510 # yellow
    regular4=2472c8 # blue
    regular5=bc3fbc # magenta
    regular6=11a8cd # cyan
    regular7=e5e5e5 # white

    bright0=666666 # bright black
    bright1=f14c4c # bright red
    bright2=23d18b # bright green
    bright3=f5f543 # bright yellow
    bright4=3b8eea # bright blue
    bright5=d670d6 # bright magenta
    bright6=29b8db # bright cyan
    bright7=e5e5e5 # bright white

### [Example Configuration]

#### [Minimal Configuration]

[FILE] **`~/.config/foot/foot.ini`Foot minimal configuration**

    font=Source Code Pro:size=10
    initial-window-size-chars=190x60

This minimal configuration sets the font to *Source Code Pro* with a size of 10. The window will open with 60, 190 character long, lines. All configuration options can be found on foot\'s source repository.^[\[2\]](#cite_note-2)^

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose gui-apps/foot`

## [Troubleshooting]

### [Terminal break after SSHing]

If a SSH connection is made to a destination that does not have the [foot] *terminfo* files [\[1\]](https://codeberg.org/dnkl/foot/wiki#user-content-things-break-after-i-ssh-into-a-remote-machine). This can be corrected in more than one way.

#### [SSH with TERM set]

This can be done multiple ways, by running [export TERM=xterm-256color] once logged in, or starting the SSH session like [TERM=xterm-256color ssh]

`user `[`$`]`TERM=xterm-256color ssh larry@server`

#### [Install terminfo files on destination]

This is very distro-dependent, but this info should be part of the [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]]:

`root `[`#`]`emerge --ask sys-libs/ncurses`

## [See also]

-   [List of software for Wayland](https://wiki.gentoo.org/wiki/List_of_software_for_Wayland "List of software for Wayland") --- various desktop related packages for Wayland
-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).
-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients

## [External resources]

-   [[foot]\'s official installation guide](https://codeberg.org/dnkl/foot/src/branch/master/INSTALL.md)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://codeberg.org/dnkl/foot/src/branch/master/doc/benchmark.md](https://codeberg.org/dnkl/foot/src/branch/master/doc/benchmark.md)]]
2.  [[[↑](#cite_ref-2)] [[https://codeberg.org/dnkl/foot#configuration](https://codeberg.org/dnkl/foot#configuration)]]