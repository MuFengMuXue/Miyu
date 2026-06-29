**Resources**

[[]][Home](https://wezterm.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/wezterm)

[[]][GitHub](https://github.com/wezterm/wezterm)

[[]][Official documentation](https://wezterm.org/config/files.html)

**WezTerm** is a powerful cross-platform terminal emulator and multiplexer implemented in Rust

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Configuration]](#Configuration)
    -   [[1.4] [Files]](#Files)
    -   [[1.5] [Font configuration]](#Font_configuration)
    -   [[1.6] [Colors configuration]](#Colors_configuration)
        -   [[1.6.1] [WezTerm\'s bundled colorschemes]](#WezTerm.27s_bundled_colorschemes)
        -   [[1.6.2] [Defining colors]](#Defining_colors)
    -   [[1.7] [Transparent background]](#Transparent_background)
    -   [[1.8] [Tabs]](#Tabs)
    -   [[1.9] [Usage]](#Usage)
    -   [[1.10] [Invocation]](#Invocation)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/wezterm](https://packages.gentoo.org/packages/x11-terms/wezterm) [[]] [A GPU-accelerated cross-platform terminal emulator and multiplexer]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Enable dev-libs/wayland backend
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-06-02 21:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask x11-terms/wezterm`

### [Configuration]

### [Files]

[WezTerm] does not automatically create or install a configuration file, but it will search for one in the following locations:

-   [\$XDG_CONFIG_HOME/.config/wezterm/wezterm.lua]
-   [\$HOME/.config/wezterm/wezterm.lua]
-   [\$XDG_CONFIG_HOME/wezterm/wezterm.lua]
-   [\$HOME/wezterm/wezterm.lua]
-   [\$HOME/.wezterm.lua]

The default configuration can be created in a users\' home directory with the following commands:

`user `[`$`]`mkdir --parents ~/.config/wezterm `

Paste the following Lua code in wezterm.lua

[FILE] **`~/.config/wezterm/wezterm.lua`Default config**

    -- Pull in the wezterm API
    local wezterm = require 'wezterm'

    -- This will hold the configuration.
    local config = wezterm.config_builder()

    -- This is where configuration choices are applied.

    -- For example, changing the color scheme:
    -- config.color_scheme = 'AdventureTime'

    -- and finally, return the configuration to wezterm
    return config

### [Font configuration]

One can run the following command and copy the desired font name:

`user `[`$`]`fc-list -f '%\n' | awk '!x[$0]++'`

Changing the default font by editing the config file.

[FILE] **`~/.config/wezterm/wezterm.lua`Default config**

    config.font = wezterm.font 'hack'
    -- It's possible to specify some parameters to influence the font selection;
    -- for example, this selects a Bold, Italic font variant.
    config.font =
      wezterm.font('hack', )

This will change the font to one provided by [[[media-fonts/hack]](https://packages.gentoo.org/packages/media-fonts/hack)[]], given that the package is installed.

### [Colors configuration]

** Note**\
WezTerm bundles quite a bit of colorschemes.

#### [][WezTerm\'s bundled colorschemes]

[FILE] **`~/.config/wezterm/wezterm.lua`Bundled**

    -- Setting the colorscheme to Catppuccin Mocha
    config.color_scheme = 'catppuccin-mocha'

#### [Defining colors]

[FILE] **`~/.config/wezterm/wezterm.lua`color schemes**

    config.colors = ,
      brights = ,

### [Transparent background]

[FILE] **`~/.config/wezterm/wezterm.lua`transparent background configure**

    # value range is 0 ~ 1
    config.window_background_opacity = 1.0

### [Tabs]

WezTerm does support tabs, here are keybinds how to use them:

**New tab**: [Ctrl]+[Shift]+[T]

**Close tab**: [Ctrl]+[Shift]+[W]

**Switch between tabs**ː [Ctrl]+[Shift]+[1]-[9]

### [Usage]

### [Invocation]

WezTerm will generally be launched from an on screen menu or keyboard shortcut in a user\'s graphical environment.

WezTerm may be launched from a shell under X11 or Wayland.

`user `[`$`]`wezterm --help`

    Wez's Terminal Emulator
    http://github.com/wez/wezterm

    Usage: wezterm [OPTIONS] [COMMAND]

    Commands:
      start                  Start the GUI, optionally running an alternative program [aliases: -e]
      ssh                    Establish an ssh session
      serial                 Open a serial port
      connect                Connect to wezterm multiplexer
      ls-fonts               Display information about fonts
      show-keys              Show key assignments
      cli                    Interact with experimental mux server
      imgcat                 Output an image to the terminal
      set-working-directory  Advise the terminal of the current working directory by emitting an OSC 7
                                 escape sequence
      record                 Record a terminal session as an asciicast
      replay                 Replay an asciicast terminal session
      shell-completion       Generate shell completion information
      help                   Print this message or the help of the given subcommand(s)

    Options:
      -n, --skip-config                Skip loading wezterm.lua
          --config-file <CONFIG_FILE>  Specify the configuration file to use, overrides the normal
                                       configuration file resolution
          --config <name=value>        Override specific configuration values
      -h, --help                       Print help
      -V, --version                    Print version