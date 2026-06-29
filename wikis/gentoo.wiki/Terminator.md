[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Terminator&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gnome-terminator.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/terminator)

[[]][GitHub](https://github.com/gnome-terminator/terminator)

**Terminator** (aka GNOME Terminator) is a python-based [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") allowing multiple terminals in the same window.

** Note**\
Not to be confused with the other [terminal emulator of the same name](https://github.com/software-jessies-org/jessies).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/terminator](https://packages.gentoo.org/packages/x11-terms/terminator) [[]] [Multiple GNOME terminals in one window]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-10-03 00:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-terms/terminator`

## [Usage]

### [Invocation]

Terminator will generally be launched from an on-screen menu, or keyboard shortcut, in a user\'s graphical environment.

Terminator may, if needed, be launched from a shell under X11.

`user `[`$`]`terminator --help`

    Usage: terminator [options]

    Options:
      -h, --help            show this help message and exit
      -v, --version         Display program version
      -m, --maximise        Maximise the window
      -M, --maximize        Maximise the window
      -f, --fullscreen      Make the window fill the screen
      -b, --borderless      Disable window borders
      -H, --hidden          Hide the window at startup
      -T FORCEDTITLE, --title=FORCEDTITLE
                            Specify a title for the window
      --geometry=GEOMETRY   Set the preferred size and position of the window(see
                            X man page)
      -e COMMAND, --command=COMMAND
                            Specify a command to execute inside the terminal
      -g CONFIG, --config=CONFIG
                            Specify a config file
      -j CONFIGJSON, --config-json=CONFIGJSON
                            Specify a partial config json file
      -x, --execute         Use the rest of the command line as a command to
                            execute inside the terminal, and its arguments
      --working-directory=DIR
                            Set the working directory
      -i FORCEDICON, --icon=FORCEDICON
                            Set a custom icon for the window (by file or name)
      -r ROLE, --role=ROLE  Set a custom WM_WINDOW_ROLE property on the window
      -l LAYOUT, --layout=LAYOUT
                            Launch with the given layout
      -s, --select-layout   Select a layout from a list
      -p PROFILE, --profile=PROFILE
                            Use a different profile as the default
      -u, --no-dbus         Disable DBus
      -d, --debug           Enable debugging information (twice for debug server)
      --debug-classes=DEBUG_CLASSES
                            Comma separated list of classes to limit debugging to
      --debug-methods=DEBUG_METHODS
                            Comma separated list of methods to limit debugging to
      --new-tab             If Terminator is already running, just open a new tab
      --unhide              If Terminator is already running, just unhide all
                            hidden windows