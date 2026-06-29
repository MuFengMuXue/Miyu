[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ghostty&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://ghostty.org)

[[]][Package information](https://packages.gentoo.org/packages/x11-terms/ghostty)

[[]][GitHub](https://github.com/ghostty-org/ghostty)

**Ghostty** is a [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") available for Linux and macOS that aims for high performance and a wide feature-set.

Ghostty was first publicly released in December 2024, as *version 1.0.0*.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Choose themes]](#Choose_themes)
        -   [[2.2.1] [Custom themes]](#Custom_themes)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Querying current setup]](#Querying_current_setup)
        -   [[3.2.1] [Show config]](#Show_config)
        -   [[3.2.2] [List keybinds]](#List_keybinds)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Title appears abrupt in system\'s window manager]](#Title_appears_abrupt_in_system.27s_window_manager)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-terms/ghostty](https://packages.gentoo.org/packages/x11-terms/ghostty) [[]] [Fast, feature-rich, and cross-platform terminal emulator]

  ------------------------------------------------------------- --------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)               Add support for X11
  [`+adwaita`](https://packages.gentoo.org/useflags/+adwaita)   Use gui-libs/libadwaita for better GNOME integration
  [`man`](https://packages.gentoo.org/useflags/man)             Build and install man pages
  [`nls`](https://packages.gentoo.org/useflags/nls)             Add Native Language Support (using gettext - GNU locale utilities)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)     Enable dev-libs/wayland backend
  ------------------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 23:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Tip**\
To save time building [Zig](https://wiki.gentoo.org/wiki/Zig "Zig"), there is a precompiled binary package available in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") (using this package may be superfluous for some systems that use [binary package host](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") packages by default).

\
To avoid [[[x11-terms/ghostty]](https://packages.gentoo.org/packages/x11-terms/ghostty)[]] pulling in [[[dev-lang/zig]](https://packages.gentoo.org/packages/dev-lang/zig)[]] as a dependency, [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") [[[dev-lang/zig-bin]](https://packages.gentoo.org/packages/dev-lang/zig-bin)[]] with the [\--oneshot](https://wiki.gentoo.org/wiki/Emerge#Do_not_add_dependencies_to_the_world_file "Emerge") option:

`root `[`#`]`emerge --ask --oneshot dev-lang/zig-bin`

Install [[[x11-terms/ghostty]](https://packages.gentoo.org/packages/x11-terms/ghostty)[]]:

`root `[`#`]`emerge --ask x11-terms/ghostty`

## [Configuration]

### [Files]

-   [\$XDG_CONFIG_HOME/ghostty/config] - main configuration file
-   [\$HOME/.config/ghostty/config] - main configuration file if the `XDG_CONFIG_HOME` [environment variable](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") does not exist

** Note**\
In this article, the Ghostty configuration directory will be listed as [\$XDG_CONFIG_HOME/ghostty/]. If the `XDG_CONFIG_HOME` environment variable is not defined on a given system, replace this with [\$HOME/.config/ghostty/], as evidenced above. (In practice, both of these paths will often resolve to [\~/.config/ghostty/].)

### [Choose themes]

Ghostty has [built-in themes](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/ghostty) that can be previewed using the [+list-themes] action:

`user `[`$`]`ghostty +list-themes`

** Tip**\
In the theme preview interface, press [?] to list available keybindings. The [c] key may be useful to copy the selected theme name to the clipboard.

Set the chosen theme by editing the Ghostty config file:

[FILE] **`$XDG_CONFIG_HOME/ghostty/config`**

    theme = tokyonight

#### [Custom themes]

Ghostty also supports custom themes. Themes must adhere to [Ghostty\'s format](https://ghostty.org/docs/features/theme#authoring-a-custom-theme) and be placed in the [\$XDG_CONFIG_HOME/ghostty/themes/] directory.

Here is an example theme converted from [Manjaro konsole Breath](https://gitlab.manjaro.org/artwork/themes/breath/-/blob/master/konsole/Breath.colorscheme):

[FILE] **`$XDG_CONFIG_HOME/ghostty/themes/Breath`**

    palette = 0=#1e2229
    palette = 1=#ed1515
    palette = 2=#448539
    palette = 3=#f67400
    palette = 4=#1d99f3
    palette = 5=#9b59b6
    palette = 6=#1abc9c
    palette = 7=#fcfcfc
    palette = 8=#7f8c8d
    palette = 9=#c0392b
    palette = 10=#55a649
    palette = 11=#fdbc4b
    palette = 12=#3daee9
    palette = 13=#8e44ad
    palette = 14=#16a085
    palette = 15=#ffffff
    background = #1e2229
    foreground = #17a88b
    cursor-color = #17a88b
    selection-background = #17a88b
    selection-foreground = #1e2229

Once a custom theme file is added, edit the Ghostty config to use it:

[FILE] **`$XDG_CONFIG_HOME/ghostty/config`**

    theme = Breath

** Tip**\
There is a tool to convert konsole themes to the Ghostty format: [konsole2ghosttytheme.bash](https://wiki.gentoo.org/wiki/User:Douglarek/konsole2ghosttytheme.bash "User:Douglarek/konsole2ghosttytheme.bash")

## [Usage]

### [Invocation]

For a listing of invocation options:

`user `[`$`]`ghostty --help`

    Usage: ghostty [+action] [options]

    Run the Ghostty terminal emulator or a specific helper action.

    If no `+action` is specified, run the Ghostty terminal emulator.
    All configuration keys are available as command line options.
    To specify a configuration key, use the `--<key>=<value>` syntax
    where key and value are the same format you'd put into a configuration
    file. For example, `--font-size=12` or `--font-family="Fira Code"`.

    To see a list of all available configuration options, please see
    the `src/config/Config.zig` file. A future update will allow seeing
    the list of configuration options from the command line.

    A special command line argument `-e <command>` can be used to run
    the specific command inside the terminal emulator. For example,
    `ghostty -e top` will run the `top` command inside the terminal.

    On macOS, launching the terminal emulator from the CLI is not
    supported and only actions are supported.

    Available actions:

      +version
      +help
      +list-fonts
      +list-keybinds
      +list-themes
      +list-colors
      +list-actions
      +show-config
      +validate-config
      +crash-report
      +show-face

    Specify `+<action> --help` to see the help for a specific action,
    where `<action>` is one of actions listed below.)

### [Querying current setup]

#### [Show config]

Pass [+show-config] to Ghostty to display the current configuration:

`user `[`$`]`ghostty +show-config`

    font-family = Cascadia Code NF
    font-family-bold = Cascadia Code NF
    font-family-italic = Cascadia Code NF
    font-family-bold-italic = Cascadia Code NF
    font-size = 11
    command = /bin/zsh
    click-repeat-interval = 500
    auto-update-channel = stable

#### [List keybinds]

Pass [+list-keybinds] to Ghostty to display the current keybinds:

`user `[`$`]`ghostty +list-keybinds`

    super + ctrl  + shift + up             resize_split:up,10
    super + ctrl  + shift + equal          equalize_splits
    super + ctrl  + shift + left           resize_split:left,10
    super + ctrl  + shift + down           resize_split:down,10
    super + ctrl  + shift + right          resize_split:right,10
    ctrl  + alt   + shift + j              write_scrollback_file:open
    super + ctrl  + right_bracket          goto_split:next
    super + ctrl  + left_bracket           goto_split:previous
    ctrl  + alt   + up                     goto_split:top
    ctrl  + alt   + left                   goto_split:left
    ctrl  + alt   + down                   goto_split:bottom
    ctrl  + alt   + right                  goto_split:right
    ctrl  + shift + v                      paste_from_clipboard
    ctrl  + shift + a                      select_all
    ctrl  + shift + o                      new_split:right
    ctrl  + shift + c                      copy_to_clipboard
    ctrl  + shift + q                      quit
    ctrl  + shift + n                      new_window
    ctrl  + shift + page_down              jump_to_prompt:1
    ctrl  + shift + comma                  reload_config
    ctrl  + shift + left                   previous_tab
    ctrl  + shift + w                      close_surface
    ctrl  + shift + j                      write_scrollback_file:paste
    ctrl  + shift + right                  next_tab
    ctrl  + shift + page_up                jump_to_prompt:-1
    ctrl  + shift + t                      new_tab
    ctrl  + shift + tab                    previous_tab
    ctrl  + shift + e                      new_split:down
    ctrl  + shift + enter                  toggle_split_zoom
    ctrl  + shift + i                      inspector:toggle
    alt   + five                           goto_tab:5
    alt   + eight                          goto_tab:8
    alt   + three                          goto_tab:3
    alt   + nine                           goto_tab:9
    alt   + two                            goto_tab:2
    alt   + four                           goto_tab:4
    alt   + f4                             close_window
    alt   + one                            goto_tab:1
    alt   + six                            goto_tab:6
    alt   + seven                          goto_tab:7
    ctrl  + comma                          open_config
    ctrl  + page_down                      next_tab
    ctrl  + equal                          increase_font_size:1
    ctrl  + minus                          decrease_font_size:1
    ctrl  + zero                           reset_font_size
    ctrl  + enter                          toggle_fullscreen
    ctrl  + page_up                        previous_tab
    ctrl  + tab                            next_tab
    ctrl  + plus                           increase_font_size:1
    shift + insert                         paste_from_selection
    shift + up                             adjust_selection:up
    shift + left                           adjust_selection:left
    shift + page_up                        scroll_page_up
    shift + end                            scroll_to_bottom
    shift + right                          adjust_selection:right
    shift + page_down                      scroll_page_down
    shift + down                           adjust_selection:down
    shift + home                           scroll_to_top

## [Troubleshooting]

### [][Title appears abrupt in system\'s window manager]

If GTK\'s title appears abrupt in system\'s window manager, turn off the [[[adwaita]](https://packages.gentoo.org/useflags/adwaita)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag firstly:

[FILE] **`/etc/portage/package.use`**

    x11-terms/ghostty -adwaita

Then disable the GTK title:

[FILE] **`$XDG_CONFIG_HOME/ghostty/config`**

    gtk-titlebar = false

## [See also]

-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).

## [External resources]

-   [Ghostty Docs](https://ghostty.org/docs)
-   [A beautiful config generator for Ghostty terminal](https://ghostty.zerebos.com/)