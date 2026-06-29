**Resources**

[[]][Home](https://jwilm.io/blog/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/alacritty)

[[]][GitHub](https://github.com/alacritty/alacritty)

[[]][wiki on upstream github](https://github.com/alacritty/alacritty/wiki)

[Alacritty] is a [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") focused on simplicity and performance. The performance goal means it *should*^[\[1\]](#cite_note-1)^ be faster than any other terminal emulators available. The simplicity goal means it does not have features such as tabs or splits (which can be provided by some [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), or [terminal multiplexers](https://wiki.gentoo.org/wiki/Recommended_tools#Terminal_multiplexers "Recommended tools"))^[\[2\]](#cite_note-2)^.

[Alacritty] is written in [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language) "wikipedia:Rust (programming language)") and GPU-accelerated using [OpenGL](https://en.wikipedia.org/wiki/OpenGL "wikipedia:OpenGL").

## Contents

-   [[1] [USE flags]](#USE_flags)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
    -   [[3.2] [Migration from YAML to TOML]](#Migration_from_YAML_to_TOML)
    -   [[3.3] [Font configuration]](#Font_configuration)
    -   [[3.4] [Colors configuration]](#Colors_configuration)
    -   [[3.5] [Transparent background]](#Transparent_background)
    -   [[3.6] [Configuration with tabbed]](#Configuration_with_tabbed)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Using fcitx]](#Using_fcitx)
    -   [[4.2] [Colorful LS]](#Colorful_LS)
    -   [[4.3] [Window title]](#Window_title)
        -   [[4.3.1] [Bash]](#Bash)
        -   [[4.3.2] [Zsh]](#Zsh)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [USE flags]

### [USE flags for] [x11-terms/alacritty](https://packages.gentoo.org/packages/x11-terms/alacritty) [[]] [GPU-accelerated terminal emulator]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)             Add support for X11
  [`debug`](https://packages.gentoo.org/useflags/debug)       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-05 03:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Installation]

### [Emerge]

Install [[[x11-terms/alacritty]](https://packages.gentoo.org/packages/x11-terms/alacritty)[]] package:

`root `[`#`]`emerge --ask x11-terms/alacritty`

## [Configuration]

### [Files]

[alacritty] does not automatically create or install a configuration file, but it will search for one in the following locations:

-   [\$XDG_CONFIG_HOME/alacritty/alacritty.yml]
-   [\$XDG_CONFIG_HOME/alacritty.yml]
-   [\$HOME/.config/alacritty/alacritty.yml]
-   [\$HOME/.alacritty.yml]

Configuration files with currently supported values are provided with [each upstream release](https://github.com/alacritty/alacritty/releases). On Gentoo, depending on the version installed, the file can be found in the following location. Be sure to adjust the `PV` ( **p**ackage **v**ersion) value to align with whatever version is currently installed on the system.

** Note**\
Since only one copy of alacritty can be installed at a time, use a wildcard to reference the documentation directory for it: `/usr/share/doc/alacritty-*/`

The default configuration can be created in a users\' home directory with the following commands:

`user `[`$`]`mkdir --parents ~/alacritty `

`user `[`$`]`bzcat /usr/share/doc/alacritty-$/alacritty.yml.bz2 > ~/alacritty/alacritty.yml `

** Warning**\
The configuration file is [YAML](https://en.wikipedia.org/wiki/YAML "wikipedia:YAML")-formatted. Preserving the indentation is critical (YAML is indentation sensitive!). The configuration file uses the [TOML](https://en.wikipedia.org/wiki/TOML "wikipedia:TOML") format since version 0.13.0

By default [alacritty] will reload the configuration automatically when changes have been written into the file. This behavior can be disabled with the following invocation:

`user `[`$`]`alacritty --no-live-config-reload`

This can also be disabled via the configuration file:

[FILE] **`~/.config/alacritty/alacritty.yml`disable live reload**

    # Live config reload (changes require restart)
    live_config_reload: false

The configuration file should be downloaded and edited from the [repository\'s release page](https://github.com/alacritty/alacritty/releases). Explanations are provided in the configuration file.

** Important**\
Make sure, that the adapted configuration file is compatible with the current installation of [Alacritty]. It might be, that version differences cause compatibility issues.

### [Migration from YAML to TOML]

Since since version 0.13.0, the [TOML](https://en.wikipedia.org/wiki/TOML "wikipedia:TOML") configuration format is used by alacritty. Users with an existing YAML configuration can use the **migrate** subcommand to convert their current configuration:

`user `[`$`]`alacritty migrate`

### [Font configuration]

One can run the following command and copy the desired font name:

`user `[`$`]`fc-list -f '%\n' | awk '!x[$0]++'`

Changing the default font by editing the config file.

[FILE] **`~/.config/alacritty/alacritty.yml`font configure**

    # Font configuration (changes require restart)
    font:
      # The normal (roman) font face to use.
      normal:
        family: Hack
        # Style can be specified to pick a specific face.
        style: Regular

      # The bold font face
      bold:
        family: Hack
        # Style can be specified to pick a specific face.
        # style: Bold

      # The italic font face
      italic:
        family: Hack
        # Style can be specified to pick a specific face.
        # style: Italic
      size: 11.0

This will change the font to one provided by [[[media-fonts/hack]](https://packages.gentoo.org/packages/media-fonts/hack)[]], given that the package is installed.

** Note**\
This method uses defaults for all other settings.

### [Colors configuration]

The easiest way is to code Alacritty theme directory and include the relevant theme :

`user `[`$`]`mkdir -p ~/.config/alacritty/themes `

`user `[`$`]`git clone --branch yaml `[`https://github.com/alacritty/alacritty-theme`](https://github.com/alacritty/alacritty-theme)` ~/.config/alacritty/themes`

** Note**\
The latest version uses the toml file format, so we need to use the yaml branch.

For example, with Gruvbox Light:

[FILE] **`~/.config/alacritty/alacritty.yml`color schemes**

    import:
        ~/.config/alacritty/themes/gruvbox_light.yaml

More schemes can be found from this page: [alacritty Wiki of Color schemes](https://github.com/alacritty/alacritty/wiki/Color-schemes).

### [Transparent background]

[FILE] **`~/.config/alacritty/alacritty.yml`Set background opacity to 0.8**

    window:
       opacity: 0.8

### [Configuration with [tabbed]]

Since [Alacritty] does not support tabs intentionally^[\[3\]](#cite_note-3)^, one can use [[[x11-misc/tabbed]](https://packages.gentoo.org/packages/x11-misc/tabbed)[]]:

`user `[`$`]`tabbed -r 2 alacritty --embed ""`

See the man page for more information;

`user `[`$`]`man 1 tabbed`

## [Troubleshooting]

### [Using fcitx]

This needs [[[app-i18n/fcitx]](https://packages.gentoo.org/packages/app-i18n/fcitx)[]] and [[[x11-wm/i3]](https://packages.gentoo.org/packages/x11-wm/i3)[]] installed. The initialization file should look like this:

[FILE] **`~/.xprofile or ~/.xinitrc`**

    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"
    eval "$(dbus-launch --sh-syntax --exit-with-session)"

    exec i3

The most important thing is to start [i3](https://wiki.gentoo.org/wiki/I3 "I3") last.

### [Colorful LS]

** Note**\
The output of `ls` (should) be colorful by default, so this is optional.

To modify `ls` to have colorful output, add the following in `/etc/DIR_COLORS`

[FILE] **`/etc/DIR_COLORS`**

    TERM alacritty

See [related GitHub issue](https://github.com/alacritty/alacritty/issues/2210).

### [Window title]

The default title is: `Alacritty`. This can be changed via the shell.

#### [Bash]

In [Bash](https://wiki.gentoo.org/wiki/Bash "Bash"), one can set the window title by manipulating the environment variable `PROMPT_COMMAND`.

The following will set the window title to: `username@hostname:cwd`.

[FILE] **`~/.bashrc`window title bar**

    # set PROMPT_COMMAND
    PROMPT_COMMAND=$'printf "\033]0;%s@%s:%s\007" "$" "$" "$"'

#### [Zsh]

In [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh"), one can set the window title by using the functions `precmd()` and `preexec()`:

The following will set the window title to: `username@hostname: zsh[shell_level] cwd_or_current_command`

For example, when user `larry` is in the `/etc/conf.d` directory, this will be the title bar:

`larry@gentoo.local: zsh[4] /etc/conf.d`

While executing `tail -f /var/log/*`:

`larry@gentoo.local: zsh[4] tail -f /var/log/*`

[FILE] **`~/.zshrc`window title bar**

    if [[ "$" != "" && "$" == "alacritty" ]]
    then
        precmd()


        preexec()
        \a"
        }
    fi

## [See also]

-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).

## [External resources]

-   [Rust Meetup January 2017](https://air.mozilla.org/rust-meetup-january-2017/) - A short talk about [Alacritty] at the Rust Meetup January 2017 (starts at 57:00).

## [References]

1.  [[[↑](#cite_ref-1)] [[https://github.com/kovidgoyal/kitty/issues/2701#issuecomment-636497270](https://github.com/kovidgoyal/kitty/issues/2701#issuecomment-636497270) [https://lwn.net/Articles/751763/](https://lwn.net/Articles/751763/)]]
2.  [[[↑](#cite_ref-2)] [Joe Wilm, [Announcing [Alacritty], a GPU-accelerated terminal emulator](https://jwilm.io/blog/announcing-alacritty/), jwilm.io. Retrieved on December 6, 2018]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/alacritty/alacritty/tree/v0.5.0#faq](https://github.com/alacritty/alacritty/tree/v0.5.0#faq)]]