**Resources**

[[]][Home](https://sw.kovidgoyal.net/kitty/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/kitty)

[[]][GitHub](https://github.com/kovidgoyal/kitty)

[[]][Official documentation](https://sw.kovidgoyal.net/kitty/overview/)

**Kitty** is a low-latency, full-featured, modern, [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"), written in C and Python, that offloads rendering to the GPU. Kitty is designed for speed, functionality, and extensibility, aiming to include useful functionality while still remaining fast and light.

By default, a little performance is traded-off against usability, though this can [be adjusted](https://sw.kovidgoyal.net/kitty/conf/#conf-kitty-performance).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Configuration]](#Configuration)
    -   [[1.4] [Files]](#Files)
    -   [[1.5] [Live reload]](#Live_reload)
    -   [[1.6] [Font configuration]](#Font_configuration)
    -   [[1.7] [Colors configuration]](#Colors_configuration)
    -   [[1.8] [Transparent background]](#Transparent_background)
    -   [[1.9] [Tabs]](#Tabs)
    -   [[1.10] [Usage]](#Usage)
    -   [[1.11] [Invocation]](#Invocation)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [fcitx5 pinyin not working]](#fcitx5_pinyin_not_working)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/kitty](https://packages.gentoo.org/packages/x11-terms/kitty) [[]] [Fast, feature-rich, GPU-based terminal]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                   Add support for X11
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`wayland`](https://packages.gentoo.org/useflags/wayland)         Enable dev-libs/wayland backend
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 14:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-terms/kitty`

### [Configuration]

### [Files]

[kitty] does not automatically create or install a configuration file, but it will search for one in the following locations:

-   [\$XDG_CONFIG_HOME/.config/kitty/kitty.conf]
-   [\$KITTY_CONFIG_DIRECTORY/kitty.conf]
-   [\$HOME/.config/kitty/kitty.conf]

Configuration files with currently supported values are provided with [each upstream release](https://github.com/kovidgoyal/kitty/releases). On Gentoo, depending on the version installed, the file can be found in the following location. Be sure to adjust the `PV` ( **p**ackage **v**ersion) value to align with whatever version is currently installed on the system.

The default configuration can be created in a users\' home directory with the following commands:

`user `[`$`]`mkdir --parents ~/.config/kitty `

`user `[`$`]`bzcat /usr/share/doc/kitty-$/kitty.conf.bz2 > ~/.config/kitty/kitty.conf `

### [Live reload]

One can reload the config file within kitty by pressing `ctrl+shift+f5` or sending kitty the SIGUSR1 signal with `kill -SIGUSR1 $KITTY_PID`. See [shortcut-kitty.Reload-kitty.conf](https://sw.kovidgoyal.net/kitty/conf/#shortcut-kitty.Reload-kitty.conf) for more detail.

### [Font configuration]

** Tip**\
It is not recommended to directly edit the font configuration. Try `kitten choose-fonts`.

One can run the following command and copy the desired font name:

`user `[`$`]`fc-list -f '%\n' | awk '!x[$0]++'`

Changing the default font by editing the config file.

[FILE] **`~/.config/kitty/kitty.conf`font configure**

    # Font configuration (changes require restart)
    font_family      hack
    bold_font        auto
    italic_font      auto
    bold_italic_font auto
    font_size 11.0

This will change the font to one provided by [[[media-fonts/hack]](https://packages.gentoo.org/packages/media-fonts/hack)[]], given that the package is installed.

### [Colors configuration]

** Tip**\
Choose from a range of theme packs and apply them immediately. Try `kitten themes`.

[FILE] **`~/.config/kitty/kitty.conf`color schemes**

    # Special
    foreground #...
    background #...

    # Black
    color0 #...
    color8 #...

    # Red
    color1 #...
    color9 #...

    # Green
    color2  #...
    color10 #...

    # Yellow
    color3  #...
    color11 #...

    # Blue
    color4  #...
    color12 #...

    # Magenta
    color5  #...
    color13 #...

    # Cyan
    color6  #...
    color14 #...

    # White
    color7  #...
    color15 #...

    # Cursor
    cursor #...
    cursor_text_color #...

### [Transparent background]

[FILE] **`~/.config/kitty/kitty.conf`transparent background configure**

    # value range is 0 ~ 1
    background_opacity 0.9

### [Tabs]

Kitty supports tabs. The default tab keybindings are as follows:

**New tab**: ctrl+shift+t

**Close tab**: ctrl+shift+q

**Next tab**: ctrl+shift+right

**Previous tab**: ctrl+shift+left

**Next layout**: ctrl+shift+l

**Move tab forward**: ctrl+shift+.

**Move tab backward**: ctrl+shift+,

**Set tab title**: ctrl+shift+alt+t

### [Usage]

### [Invocation]

Kitty will generally be launched from an on screen menu or keyboard shortcut in a user\'s graphical environment.

Kitty may be launched from a shell under X11 or Wayland.

`user `[`$`]`kitty --help`

    Usage: kitty [options] [program-to-run ...]

    Run the kitty terminal emulator. You can also specify the program
    to run inside kitty as normal arguments following the options.
    For example: kitty sh -c "echo hello, world. Press ENTER to quit; read"

    For comprehensive documentation for kitty, please see:
    https://sw.kovidgoyal.net/kitty/

    Options:
      --class=CLS
        Set the class part of the WM_CLASS window property. On Wayland, it sets
        the app id.
        Default: kitty

      --name=NAME
        Set the name part of the WM_CLASS property (defaults to using the value
        from --class)

      --title, -T=TITLE
        Set the window title. This will override any title set by the program
        running inside kitty. So only use this if you are running a program that
        does not set titles. If combined with --session the title will be used
        for all windows created by the session, that do not set their own
        titles.

      --config, -c=CONFIG
        Specify a path to the configuration file(s) to use. All configuration
        files are merged onto the builtin kitty.conf, overriding the builtin
        values. This option can be specified multiple times to read multiple
        configuration files in sequence, which are merged. Use the special value
        NONE to not load a config file.

        If this option is not specified, config files are searched for in the
        order: $XDG_CONFIG_HOME/kitty/kitty.conf, ~/.config/kitty/kitty.conf,
        $XDG_CONFIG_DIRS/kitty/kitty.conf. The first one that exists is used as
        the config file.

        If the environment variable KITTY_CONFIG_DIRECTORY is specified, that
        directory is always used and the above searching does not happen.

        If /etc/xdg/kitty/kitty.conf exists it is merged before (i.e. with lower
        priority) than any user config files. It can be used to specify
        system-wide defaults for all users.

      --override, -o=OVERRIDE
        Override individual configuration options, can be specified multiple
        times. Syntax: name=value. For example: -o font_size=20

      --directory, -d=DIRECTORY
        Change to the specified directory when launching
        Default: .

      --detach
        Detach from the controlling terminal, if any

      --session=SESSION
        Path to a file containing the startup session (tabs, windows, layout,
        programs). Use - to read from STDIN. See the README file for details and
        an example.

      --watcher, -w=WATCHER
        Path to a python file. Appropriately named functions in this file will
        be called for various events, such as when the window is resized,
        focused or closed. See the section on watchers in the launch command
        documentation https://sw.kovidgoyal.net/kitty/launch.html. Relative
        paths are resolved relative to the kitty config directory. Note that
        this watcher will be added only to all initially created windows, not
        new windows created after startup.

      --hold
        Remain open after child process exits. Note that this only affects the
        first window. You can quit by either using the close window shortcut or
        Ctrl+d.

      --single-instance, -1
        If specified only a single instance of kitty will run. New invocations
        will instead create a new top-level window in the existing kitty
        instance. This allows kitty to share a single sprite cache on the GPU
        and also reduces startup time. You can also have separate groups of
        kitty instances by using the --instance-group option

      --instance-group=INSTANCE_GROUP
        Used in combination with the --single-instance option. All kitty
        invocations with the same --instance-group will result in new windows
        being created in the first kitty instance within that group

      --wait-for-single-instance-window-close
        Normally, when using --single-instance, kitty will open a new window in
        an existing instance and quit immediately. With this option, it will not
        quit till the newly opened window is closed. Note that if no previous
        instance is found, then kitty will wait anyway, regardless of this
        option.

      --listen-on=LISTEN_ON
        Tell kitty to listen on the specified address for control messages. For
        example, --listen-on=unix:/tmp/mykitty or
        --listen-on=tcp:localhost:12345. On Linux systems, you can also use
        abstract UNIX sockets, not associated with a file, like this:
        --listen-on=unix:@mykitty. Environment variables in the setting are
        expanded and relative paths are resolved with respect to the temporary
        directory. To control kitty, you can send it commands with kitty @ using
        the --to option to specify this address. This option will be ignored,
        unless you set allow_remote_control to yes in kitty.conf. Note that if
        you run kitty @ within a kitty window, there is no need to specify the
        --to option as it is read automatically from the environment. For UNIX
        sockets, this can also be specified in kitty.conf.

      --start-as=START_AS
        Control how the initial kitty window is created.
        Default: normal
        Choices: normal, minimized, maximized, fullscreen

    Debugging options:
      --version, -v
        The current kitty version

      --dump-commands
        Output commands received from child process to stdout

      --replay-commands=REPLAY_COMMANDS
        Replay previously dumped commands. Specify the path to a dump file
        previously created by --dump-commands. You can open a new kitty window
        to replay the commands with::

            kitty sh -c "kitty --replay-commands /path/to/dump/file; read"

      --dump-bytes=DUMP_BYTES
        Path to file in which to store the raw bytes received from the child
        process

      --debug-gl, --debug-rendering
        Debug rendering commands. This will cause all OpenGL calls to check for
        errors instead of ignoring them. Also prints out miscellaneous debug
        information. Useful when debugging rendering problems

      --debug-keyboard
        This option will cause kitty to print out key events as they are
        received

      --debug-font-fallback
        Print out information about the selection of fallback fonts for
        characters not present in the main font.

      --debug-config
        Print out information about the system and kitty configuration.

    kitty 0.19.3 created by Kovid Goyal

## [Troubleshooting]

### [fcitx5 pinyin not working]

According to the [The Developer](https://github.com/fcitx/fcitx5/issues/281#issuecomment-847296108), kitty is neither GTK nor QT, so try this [environment variable](https://wiki.gentoo.org/wiki/Handbook:X86/Working/EnvVar "Handbook:X86/Working/EnvVar") under X11 or Wayland:

[CODE]

    GLFW_IM_MODULE=ibus