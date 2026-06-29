<h1 align="center">Welcome To The Sway WIKI</h1>
<p align="center">
<a href="#configuration">Configuration</a> &mdash;
<a href="#faq">FAQ</a> &mdash;
<a href="#troubleshooting">Troubleshooting</a>
</p>

**Community-maintained.** Anyone can contribute. If you're planning significant changes, please coordinate with the community on IRC first.

<h2>Getting Started with Sway</h2>

New to Sway? Start here.

Sway is a Wayland-native tiling window manager built on wlroots. Unlike X11 tools like dwm, i3, etc., it's designed from the ground up for modern Wayland. Please read this wiki—it covers the essential knowledge you'll need to configure and use Sway effectively.

<details>
<summary>Learn more about Sway</summary>

<br>

Sway combines two powerful concepts:

- Tiling window manager: Automatically arranges your windows in efficient, non-overlapping tiles
- Keyboard-driven workflow: Control your desktop entirely through keyboard shortcuts

Sway brings the simplicity and efficiency of i3 to modern desktop environments. It's lightweight, fully customizable, and designed for anyone who prefers a keyboard-driven, no-nonsense desktop experience.

</details>


## Before installing

### NVIDIA Users

Sway works best with open-source graphics drivers. The Nvidia proprietary driver isn't officially supported here—but the open-source [Nouveau](https://nouveau.freedesktop.org/) driver is a solid alternative if you're team Nvidia! Please don't ask questions about the Nvidia proprietary driver in this space. If you have a choice of hardware, keep open source support in mind. 

### Intel Users


For Intel users, it is **recommended to install these packages** if you want Sway WM to behave as expected. These **5 essential packages** provide hardware acceleration and peak performance for an optimal experience.



| Package | What It Does |
|---------|--------------|
| **intel-ucode** | CPU security & stability patches |
| **vulkan-intel** | Modern 3D graphics support |
| **intel-media-driver** | Allows Sway to provide better interaction with your CPU and display |
| **libva-intel-driver** | Enables high-quality video playback with GPU acceleration |
| **intel-gpu-tools** | GPU monitoring & troubleshooting |


### Login managers

Some login managers support Wayland, and others don't. If you have issues starting sway and you use a login manager, your first step should be disabling the login manager and running sway as described by `man 1 sway`. If this works, report the bug to your login manager, not to sway.

For a small list of compatible login managers, see the [login manager list on the useful addons page](https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway#login-managers).

You can start sway automatically without a login manager, for example, by adding this to your `.bash_profile` (`.zlogin` or `.zprofile` for Zsh):

```bash
# If running from tty1 start sway
[ "$(tty)" = "/dev/tty1" ] && exec sway
```

With confirmation:
```bash
# Auto-launch Sway on TTY1 login
if [ "$(tty)" = "/dev/tty1" ]; then
    read -p "Start Sway? [y]es or [n]o: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        exec sway
    fi
fi
```

For Fish, create the file ``~/.config/fish/conf.d/sway.fish``
```fish
# If running from tty1 start sway
set TTY1 (tty)
[ "$TTY1" = "/dev/tty1" ] && exec sway
```

Might help with dbus(missing $DBUS_SESSION_BUS_ADDRESS) 
```bash
# If running from tty1 start sway
[ "$(tty)" = "/dev/tty1" ] && exec dbus-run-session sway
```

## Configuration

The suggested location for the sway configuration file is `~/.config/sway/config`. To begin configuring sway, create this directory and copy the default config.

```sh
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/
$EDITOR ~/.config/sway/config
```

Read the default config - it has comments that explain what each option does. Read `man 5 sway` for more information about each config command.

### Display configuration

Sway manages displays for you, **xrandr** should not be used.

Run `swaymsg -t get_outputs` to get a list of output names. Then use the `output` command to arrange your displays.

```
output <identifier> {
   # ...config options...
   mode 3840x1600@143.998Hz
}
```

For detailed information, check the manual. Run `man 5 sway-output`.

#### Multihead

Managing multiple monitors is simple through the use of multiple `output` commands.

e.g., if we want to have a monitor with \<name\> HDMI1 and a resolution of 1920x1080, and to the right of it a laptop monitor with \<name\> eDP1 and a resolution of 1600x900; the following two commands can be placed in your config file:

```
output HDMI1 resolution 1920x1080 position 0 0 
output eDP1 resolution 1600x900 position 1920 0 
```

Take a note that you might want to change the focus of monitor on sway launch. Add this to your sway config:
```
focus output <name-or-identifier>
```
or
```https://wiki.archlinux.org/index.php/NetworkManager#Appindicator
exec swaymsg focus output <name-or-identifier>
```
so it doesn't trigger on reload.

For more details read `man 5 sway-output`.

#### Clamshell Mode
AKA Closed Display mode. This mode is where your laptop lid is closed and you have external monitor(s) as outputs. As of Sway 1.1 you can use switch events to drive certain functionality, such as disabling an output upon a laptop lid being closed. Pass your laptop output name into the following, which can be found with: `swaymsg -t get_outputs` for example `eDP-1`.

```
set $laptop <laptop_output_identifier>
bindswitch --reload --locked lid:on output $laptop disable
bindswitch --reload --locked lid:off output $laptop enable
```

However, when reloading sway while using clamshell mode, the displays may reset (i.e. both displays will be enabled). To stop this, save this shell script:

```sh
#!/bin/sh

LAPTOP_OUTPUT="<LAPTOP>"
LID_STATE_FILE="/proc/acpi/button/lid/LID0/state"

read -r LS < "$LID_STATE_FILE"

case "$LS" in
*open)   swaymsg output "$LAPTOP_OUTPUT" enable ;;
*closed) swaymsg output "$LAPTOP_OUTPUT" disable ;;
*)       echo "Could not get lid state" >&2 ; exit 1 ;;
esac
```

Replace `<LAPTOP>` with the name of the display, ensure lid state file path is correct for your system.

To make sure this script runs whenever Sway is reloaded, add this line to your sway config:

```
exec_always /path/to/script.sh
```

#### HiDPI

HiDPI can be enabled via `output` and its **scale** option.

`output <name> scale <I>`

&lt;I&gt; is the integer scaling factor (usually 2 for HiDPI screens)

If scaling is active, it has to be considered when defining relative positions. For example, if the scaling factor for the left monitor (HDMI1) is 2, the relative position for the right output has to be divided by 2. This example is illustrated by the configuration below:

```
output HDMI1 scale 2
output HDMI1 pos 0 0 res 3200x1800
output eDP1 pos 1600 0 res 1920x1080
```

Note that the x-pos of eDP1 is 1600 = 3200/2.

XWayland application may appear blurry on scaled outputs (see [#2966](https://github.com/swaywm/sway/issues/2966)). One workaround for that is to disable built-in XWayland (with `xwayland disabled`) and use [xwayland-satellite](https://github.com/Supreeeme/xwayland-satellite) that effectively disables scaling for XWayland applications starting from [v0.6](https://github.com/Supreeeme/xwayland-satellite/releases/tag/v0.6).

**Fractional scaling**

Fractional scaling is supported but is not recommended. Your display does not have fractional pixels - and if you enable fractional scaling we cannot display your windows faithfully and your image quality will be degraded, for clients that do not report HiDPI surfaces (including all XWayland clients, but usually does not include modern versions of Wayland-native GUI toolkits). If you use many such programs, you should instead choose the integer scale factor appropriate for your display and configure your software's font size as necessary. If you still want to use fractional scaling, it is as simple as e.g. `output <name> scale 1.5`.

#### Display rotation

`output <name> transform 90` will rotate output `<name>` by 90 degrees clockwise.  Read `man 5 sway-output` and search for `transform` to see other options, like flipping across an axis.

For automatic display rotation via a built-in accelerometer, see [rot8](https://github.com/efernau/rot8).

#### Redshift equivalent

[Redshift](http://jonls.dk/redshift/) adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less if you are working in front of the screen at night. Unfortunately, Redshift does not support Wayland.

However, there is a fork of Redshift called [gammastep](https://gitlab.com/chinstrap/gammastep) which does have Wayland support. On Arch Linux, it is available as an [official package](https://archlinux.org/packages/extra/x86_64/gammastep/).

Other alternatives are [wlsunset](https://git.sr.ht/~kennylevinsen/wlsunset), [wl-gammarelay](https://github.com/jeremija/wl-gammarelay) and [wl-gammarelay-rs](https://github.com/MaxVerevkin/wl-gammarelay-rs).

### Input configuration

A list of input devices is available by running `swaymsg -t get_inputs`. Use the identifier for the device you want to configure in your config file:

```
input <identifier> {
    # ...config options...
}
```

Nothing prevents having multiple configurations for different specific devices:

```
# default layout
input "1:1:AT_Translated_Set_2_keyboard" {
   xkb_layout us
}

# custom layout for an external keyboard
input "1452:591:Custom_Keyboard" {
   xkb_layout YourCustomLayout
}
```

See `man 5 sway-input` for a summary of the available options.

#### Keyboard layout

```
# or input <identifier>
input "type:keyboard" {
    xkb_layout us,de
    xkb_variant ,nodeadkeys
    xkb_options grp:alt_shift_toggle
}
```

See `man 7 xkeyboard-config` for options you can use with the `xkb_layout`, `xkb_model`, `xkb_options`, `xkb_rules`, and `xkb_variant` commands. Separate multiple options with commas.

User-specific settings such as symbols will be loaded from their respective directories in `~/.xkb/` or `$XDG_CONFIG_HOME/xkb/`.

A lot of modifications are available through `xkb_options`. They can be found in `/usr/share/X11/xkb/symbols/{altwin,capslock,compose,ctrl}` and the respective option name in `/usr/share/X11/xkb/rules/base`.

**Examples**:

* Make caps lock work as escape: `xkb_options caps:escape`
* Swap escape and caps lock: `xkb_options caps:swapescape`
* Make caps lock work as control: `xkb_options ctrl:nocaps`
* Make caps lock work as additional control `xkb_options caps:ctrl_modifier`
* Swap left alt and super, *and* set caps lock to escape: `xkb_options altwin:swap_lalt_lwin,caps:escape`
* Make the menu key work as additional super: `xkb_options altwin:menu_win`

Note that to trigger several options, you need to list them separated with a comma, e.g. `xkb_options caps:escape,altwin:swap_lalt_lwin`; if you instead write several `xkb_options`-lines, only the last one will take effect.

#### Load custom xkb keymap file (since [#3999](https://github.com/swaywm/sway/issues/3999))
```
# or input <identifier>
input "type:keyboard" {
    xkb_file ~/.config/xkb/custom
}
```

#### Keyboard repeat delay and rate

```
# or input <identifier>
input "type:keyboard" {
    repeat_delay 500
    repeat_rate 5
}
```

#### Load a modified custom xkb keymap (xmodmap equivalent)

See [#4250](https://github.com/swaywm/sway/issues/4250#issuecomment-711222006)

If you just want to change a couple of keymappings, you can create your own by overriding the keymappings of your usual layout.

```
input type:keyboard {

  # Modified programmer Dvorak. File at ~/.xkb/symbols/dvp_alt_gr_remapped_to_super
  xkb_layout "dvp_alt_gr_remapped_to_super"

  # Capslock key should work as escape key
  # See /usr/share/X11/xkb/rules/xorg.lst for options
  xkb_options caps:escape

  repeat_delay 250
  repeat_rate 45
}
```

The entirety of `~/.xkb/symbols/dvp_alt_gr_remapped_to_super`:

```
default partial alphanumeric_keys
xkb_symbols "basic" {
        include "us(dvp)"
        name[Group1] = "Modified programmer Dvorak";
        key <RALT> { [ Super_L, Super_R ] };
};
```

The full documentation on how to override keymappings is available [at this link](https://www.charvolant.org/doug/xkb/html/node5.html). Here a [slightly digested version](https://git.sr.ht/~jman/dotfiles/tree/refs/heads/master/xkb/README.md) with a practical commented example.

#### Libinput config options

```
input <device name> {
    left_handed enabled
    tap enabled
    natural_scroll disabled
    dwt enabled
    accel_profile "flat" # disable mouse acceleration (enabled by default; to set it manually, use "adaptive" instead of "flat")
    pointer_accel 0.5 # set mouse sensitivity (between -1 and 1)
}
```

See `man 5 sway-input` for all available options.

#### Touch Display Mapping

Touch input targets for touch displays used in a multi-display environment must be mapped to that touch display only.

```
set $display1       "Dell Inc. DELL P2414H VHVTW542165L"
set $display2       "Dell Inc. DELL P2418HT MYDM775F152L"
set $display2-touch "8146:24835:Melfas_LGD_AIT_Touch_Controller"

input $display2-touch map_to_output $display2
```

### Wallpapers

Feh and similar tools do not work on Wayland. Sway supports setting wallpapers if [swaybg](https://github.com/swaywm/swaybg) is installed. You can use this feature through the `output` command, using the **bg** option:

e.g. `output HDMI-A-1 bg ~/wallpaper.png stretch`

See output configuration options in `man 5 sway-output`.

Also, see [[ https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway ]] for more ideas.

### Swaybar configuration

Swaybar supports most of the same features as i3bar, and is configured in the
same way. Add a `bar` section to your config:

```
bar {
    # ...bar options..
}
```

For the full list of options, see `man 5 sway-bar`.

### Comments
Comments are supported in the configuration and start with a `#`
character, optionally with whitespace before it. Comments and commands
on the same line are [not
supported](https://github.com/swaywm/sway/issues/3044#issuecomment-434830261),
because i3 - and thus Sway - supports the `#RRGGBB` syntax for
specifying colours. Therefore, always place comments on their own
line.

Additionally, a commented out line with a trailing backslash
[currently](https://github.com/swaywm/sway/issues/7188) affects the
next line, even if that is not a comment. So, never end a commented
line with a backslash `\`.

## Taking screenshots

X11 tools like `scrot` do not work. Try [grim](https://sr.ht/~emersion/grim/).

[Grimshot](https://github.com/OctopusET/sway-contrib) provides a simpler command line interface if you're looking for something more high level (and relies on grim and slurp internally).

[shotman](https://git.sr.ht/~whynothugo/shotman) is a simple, light, modern UI for screenshooting, also relies on slurp for region selection, and taking screenshot of current active window only works in sway for now.

[flameshot](https://flameshot.org) has a simple and inituitive GUI with various editing tools.

[swappy](https://github.com/jtheoof/swappy) is another tool (written in C, uses GTK and Pango) that pops up a GUI and allows basic operations on the screenshot such as adding text, arrows, circles, squares and choosing colors. Has a config file to customize the GUI. Can also work without `grim`.

Also, see [[ https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway ]] for more ideas.

## Creating screencasts

Try [wf-recorder](https://github.com/ammen99/wf-recorder) for screen recording of wlroots-based compositors like swaywm. If you use OBS Studio, versions newer than 27.0 natively support screen recording using pipewire. For older versions you can use [wlrobs](https://hg.sr.ht/~scoopta/wlrobs) recording plugin for wlroots-based compositors.

Also, see [[ https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway ]] for more ideas.

## Program launchers

- [bemenu](https://github.com/Cloudef/bemenu) works as a dmenu replacement.
- [sway-launcher-desktop](https://github.com/Biont/sway-launcher-desktop): TUI Application launcher with Desktop Entry support.
- [wofi](https://hg.sr.ht/~scoopta/wofi) is a rofi-like launcher.
- [yofi](https://github.com/l4l/yofi) is a minimalistic menu for wayland.
- [tofi](https://github.com/philj56/tofi) is an extremely performant wlroots-specific launcher.
- [raffi](https://github.com/chmouel/raffi) - fuzzel/iced launcher based on yaml configuration.

Also, see [[ https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway ]] for more ideas.

## Screen zooming feature

Not yet possible with swaywm/wlroots. Please [look / get involved here](https://github.com/swaywm/sway/issues/2781).

Also, see [[ https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway ]] for more ideas.

## Setting environmental variables

How you set variables will depend on how sway was started.

Environment variables are inherited from the process that starts sway. You need to set variables there.

Some of the possible options are:
- login manager: check the documentation.
- login shell: export them there before launching sway.
- user service: use the EnvironmentFile= key and an environment file.

More details [here.][SetEnvPage]

## FAQ

### Before asking questions...

Update both sway and wlroots and then try again. Look through [known issues](https://github.com/swaywm/sway/issues) in sway and [known issues](https://gitlab.freedesktop.org/wlroots/wlroots/-/issues) in wlroots. Did you read the man pages? Start with `man sway`. Read your config file, too. And read the log.

### How do I get rid of title bars on applications?

Use the `default_border` command in your config. `default_border normal` shows title bars, whereas `none` and `pixel` do not. The `border` command operates on the currently focused window only. `default_border` is a setting, `border` is an action.

Note that `default_border` only affects new windows. Even after reloading sway, you will need to close and re-open any windows you do not wish to see the title bar on.

When hiding the title bar in a tab or stack container, also check the following.

```
hide_edge_borders --i3 none|vertical|horizontal|both|smart|smart_no_gaps
```

### Where are my tray icons?

Initial tray icon support for swaybar was merged with [#3249](https://github.com/swaywm/sway/pull/3249) pull request. Missing features are tracked in [#3799](https://github.com/swaywm/sway/issues/3799).

### How do I configure urxvt transparency?

urxvt transparency requires "real transparency" settings. Add this to your `.Xresources` and reload via `xrdb ~/.Xresources`:

```
URxvt*depth: 32
URxvt*background: rgba:0000/0000/0200/c800
```

Be aware that this configuration will conflict with the `URxvt.reversevideo` and if you enable the reversevideo option, the text will become transparent instead of the background.

You may wish to add `exec xrdb ~/.Xresources` to your sway config to configure this on startup.

### I'm not using logind but still want DBus/PolKit/power management to work.

What can I do?

If you're using ConsoleKit2, launch sway using

```sh
exec ck-launch-session dbus-launch --sh-syntax --exit-with-session sway
```

Alternatively, you could omit the `ck-launch-session` part.

### xbacklight

xbacklight is, as the name would imply, a tool for X. Instead, you can use [brightnessctl](//github.com/Hummer12007/brightnessctl), [brillo](https://gitlab.com/cameronnemo/brillo) or just directly manipulate `/sys/class/backlight`.

For instance:

```
bindsym --locked XF86MonBrightnessDown exec brightnessctl set 5%-
bindsym --locked XF86MonBrightnessUp exec brightnessctl set 5%+
```

### Which terminal emulator can I use?

You can use either X- or Wayland-native terminal emulator with little difference in terms of functionality.

[Alacritty](https://github.com/jwilm/alacritty), [Kitty](https://sw.kovidgoyal.net/kitty/), [foot](https://codeberg.org/dnkl/foot), [GhosTTY](https://ghostty.org), or [wezterm](https://github.com/wez/wezterm) will use Wayland without additional configuration. You can use VTE-based terminals like GNOME Terminal. X-based `urxvt` is another popular option.

### Why am I getting `Error on line XX […] Unknown key`?

In your config, you should replace at line XX `bindsym` by `bindcode`.

### Locale-specific configuration tricks

#### Workspace switching on the French layout

Because French number keys only produce numbers when Shift is pressed (or Caps Lock is active), you'll need to setup key bindings with the various special characters under the numbers (&, é, ", etc):

```
    # Switch to workspace
    bindsym $mod+ampersand workspace number 1
    bindsym $mod+eacute workspace number 2
    bindsym $mod+quotedbl workspace number 3
    bindsym $mod+apostrophe workspace number 4
    bindsym $mod+parenleft workspace number 5
    bindsym $mod+minus workspace number 6
    bindsym $mod+egrave workspace number 7
    bindsym $mod+underscore workspace number 8
    bindsym $mod+ccedilla workspace number 9
    bindsym $mod+agrave workspace number 10

    # Move focused container to workspace
    bindsym $mod+Shift+ampersand move container to workspace number 1
    bindsym $mod+Shift+eacute move container to workspace number 2
    bindsym $mod+Shift+quotedbl move container to workspace number 3
    bindsym $mod+Shift+apostrophe move container to workspace number 4
    bindsym $mod+Shift+parenleft move container to workspace number 5
    bindsym $mod+Shift+minus move container to workspace number 6
    bindsym $mod+Shift+egrave move container to workspace number 7
    bindsym $mod+Shift+underscore move container to workspace number 8
    bindsym $mod+Shift+ccedilla move container to workspace number 9
    bindsym $mod+Shift+agrave move container to workspace number 10

```

#### Key bindings on a dual US/Russian layout or US/Greek

If you have configured your keyboard with a US and a Russian layout (`input * xkb_layout us,ru`), your bindings using Latin script letters won't work when the Russian keyboard is active (for instance, `$mod+f` won't work, because you can't produce the letter `f` with the Russian layout).

To make key bindings work regardless of the currently active layout, you can use `bindsym --to-code`:

```
bindsym --to-code {
    $mod+b splith
    $mod+v splitv
}
```

### Windows/KDE/gnome launcher shortcut

This will toggle the launcher on a single keypress, but not if a keybind was triggered with that key.
```
bindsym --no-repeat --release Super_L exec pkill $launcher || $launcher
```

### Memorize and switch target windows

Configuration example:
```
# window switch setting
set $mode_set_switch_window "set_switch_window: [0]-[9]"
mode $mode_set_switch_window {
    bindsym 1 mark 1; mode "default"
    bindsym 2 mark 2; mode "default"
    bindsym 3 mark 3; mode "default"
    bindsym 4 mark 4; mode "default"
    bindsym 5 mark 5; mode "default"
    bindsym 6 mark 6; mode "default"
    bindsym 7 mark 7; mode "default"
    bindsym 8 mark 8; mode "default"
    bindsym 9 mark 9; mode "default"
    bindsym 0 mark 0; mode "default"
    bindsym Return mode "default"
    bindsym Escape mode "default"
}
bindsym $mod+ctrl+t mode $mode_set_switch_window
set $mode_switch_window "switch_window: [0]-[9]"
mode $mode_switch_window {
    bindsym 1 [con_mark="1"] focus; mode "default"
    bindsym 2 [con_mark="2"] focus; mode "default"
    bindsym 3 [con_mark="3"] focus; mode "default"
    bindsym 4 [con_mark="4"] focus; mode "default"
    bindsym 5 [con_mark="5"] focus; mode "default"
    bindsym 6 [con_mark="6"] focus; mode "default"
    bindsym 7 [con_mark="7"] focus; mode "default"
    bindsym 8 [con_mark="8"] focus; mode "default"
    bindsym 9 [con_mark="9"] focus; mode "default"
    bindsym 0 [con_mark="0"] focus; mode "default"
    bindsym t mode $mode_set_switch_window
    bindsym Return mode "default"
    bindsym Escape mode "default"
}
bindsym $mod+t mode $mode_switch_window
```

### Move workspace to current output when switching

If you want your workspace to be moved to the current output when you switch to it using `$mod+<number>` instead of you being refocused to a different output where the workspace is currently bound, replace your `bindsym $mod+<number>` lines in your configuration with this (for each `<number>` of course):

```
bindsym $mod+1 [workspace="^1$"] move workspace to output current; workspace number 1
```

### Move all workspace windows

```
set $mode_move_all_workspace_windows "Move all workspace windows to [0-9]?"
mode $mode_move_all_workspace_windows {
    bindsym 1 [workspace=".*"] move to workspace 1; workspace number 1, mode "default"
    bindsym 2 [workspace=".*"] move to workspace 2; workspace number 2, mode "default"
    bindsym 3 [workspace=".*"] move to workspace 3; workspace number 3, mode "default"
    bindsym 4 [workspace=".*"] move to workspace 4; workspace number 4, mode "default"
    bindsym 5 [workspace=".*"] move to workspace 5; workspace number 5, mode "default"
    bindsym 6 [workspace=".*"] move to workspace 6; workspace number 6, mode "default"
    bindsym 7 [workspace=".*"] move to workspace 7; workspace number 7, mode "default"
    bindsym 8 [workspace=".*"] move to workspace 8; workspace number 8, mode "default"
    bindsym 9 [workspace=".*"] move to workspace 9; workspace number 9, mode "default"
    bindsym 0 [workspace=".*"] move to workspace 10; workspace number 10, mode "default"
    # back to normal: Enter or Escape
    bindsym Return mode "default"
    bindsym Escape mode "default"
}
bindsym $mod+shift+ctrl+m mode $mode_move_all_workspace_windows
```

### XDG_CURRENT_DESKTOP environment variable is not being set

Some applications and desktop mechanisms may rely on the `XDG_CURRENT_DESKTOP` environment variable to be set so that the application can accommodate for being ran under sway. Examples include XDG autostart implementations, screensharing in Firefox and many others.

Sway itself does not set this variable, it should be set before sway is started. Sane default would be `sway:wlroots` (specific `sway` as first priority, common `wlroots` after it to be in line with other wlroots compositors). If you start sway from shell profile, export it before sway invocation. If you use a login manager, the login manager will use the DesktopNames attribute inside the `sway.desktop` file. This file may be modified to add `DesktopNames=sway;wlroots` (also see [#7952](https://github.com/swaywm/sway/pull/7952)).

It's not good practice for applications to make use of XDG_CURRENT_DESKTOP in this way, and Firefox has an issue open to try to fix it. Refer to [xpdw's FAQ](https://github.com/emersion/xdg-desktop-portal-wlr/wiki/FAQ#how-do-i-run-xdpw) and [xdpw's Troubleshooting guide](https://github.com/emersion/xdg-desktop-portal-wlr/wiki/%22It-doesn't-work%22-Troubleshooting-Checklist) if your issue is specifically related to screensharing.

### Systemd and dbus activation environments

Some variables need to be exported to systemd and/or dbus activation environments so tools that rely on them work properly. The essential ones are:
`WAYLAND_DISPLAY`, `DISPLAY` (if XWayland is used), `XDG_CURRENT_DESKTOP`, plus Sway's: `SWAYSOCK`, `I3SOCK`, `XCURSOR_SIZE`, `XCURSOR_THEME`.

Export should be performed from context of running sway process, via exec statements in sway's configuration:

```
exec systemctl --user import-environment WAYLAND_DISPLAY DISPLAY XDG_CURRENT_DESKTOP SWAYSOCK I3SOCK XCURSOR_SIZE XCURSOR_THEME
```

If `dbus-broker` dbus implementation is used, that's it. It reuses activation environment of systemd.

If classic `dbus` implementation is used, it requires updating its own separate environment:

```
exec dbus-update-activation-environment WAYLAND_DISPLAY DISPLAY XDG_CURRENT_DESKTOP SWAYSOCK I3SOCK XCURSOR_SIZE XCURSOR_THEME
```

## Troubleshooting

### How do I report issues?

We will expect three things from you: your sway version, your config file, and a debug log. Obtain your version like so:

    swaymsg -t get_version

If this doesn't work, use:

    sway -v

Obtain a debug log like so:

    sway -d 2> ~/sway.log

This will record information about sway's activity when it's running. Briefly reproduce your problem and exit sway. Upload this file, along with your config, to [gist.github.com](https://gist.github.com), and include this in a GitHub issue (or when asking for help on IRC). When preparing a debug log, make it brief - start up sway, do the minimum work necessary to reproduce the error, then close sway. Explain the steps you took in plain English in your GitHub issue as well.

If the problem isn't immediately obvious, you will likely be required to debug it yourself - we are volunteers and only have so much free time.

### I just installed sway. I can move my mouse cursor but my keyboard does not work.

Are you pressing keys that are bound to do anything? **Read the [config file](https://github.com/SirCmpwn/sway/blob/master/config.in).** If `$mod+Return` is bound to `exec foot` (which it is by default) - do you have foot installed? Try `$mod+2` or `$mod+8` - does it switch workspaces?

### I can't run anything.

Check for keyboard shortcuts in the config file to start your launcher. Are you trying to run x applications? You probably don't have [xwayland](https://wayland.freedesktop.org/xserver.html) installed. Consult your distribution's documentation for instructions on installing xwayland.

### My keyboard shortcuts do not work.

If you're running sway on top of X11, with i3 running, i3 will intercept any key presses that would otherwise be sent to sway. If you use the exact same key bindings then sway will never receive them.

### i3-dmenu-desktop does not work.

There's a [patch](https://github.com/i3/i3/pull/2265) but it cannot be merged upstream.  See [issue #511](https://github.com/swaywm/sway/issues/521) for more info.

You can still apply the patch manually though:

```sh
wget 'https://patch-diff.githubusercontent.com/raw/i3/i3/pull/2265.patch'
sudo patch -p0 /usr/bin/i3-dmenu-desktop < 2265.patch
```

### My favorite application isn't displayed right, how can I fix this?

#### Disabling client-side Qt decorations

Qt currently defaults to using the X11 backend instead of its native Wayland backend. To use the Wayland backend, set `QT_QPA_PLATFORM=wayland`. Then Qt will also draw client-side decorations for all windows, to disable this, set `QT_WAYLAND_DISABLE_WINDOWDECORATION="1"`

#### Window rules to adjust sway's borders

If you want to use a particular application's built-in window decorations over the sway borders, you can write a rule like this in your config:

    for_window [app_id="nautilus"] border none

#### Issues with Java applications

* Try to set `_JAVA_AWT_WM_NONREPARENTING=1` in your environment ([Source](https://github.com/swaywm/sway/issues/595)). You can achieve this by appending the following snippet to your `~/.profile` file:
```sh
if [ "$XDG_SESSION_DESKTOP" = "sway" ] ; then
    # https://github.com/swaywm/sway/issues/595
    export _JAVA_AWT_WM_NONREPARENTING=1
fi
```
* Try [wmname](https://tools.suckless.org/x/wmname/) as Suggested ([Source](https://github.com/swaywm/sway/issues/595#issuecomment-214203380)) Package if above don't work. If there is error like ` cannot open display ` then use ` export DISPLAY=:0 `
```sh
wmname LG3D
```

This seems to fix blank windows and menus that are drawn at a wrong offset to the selected menu item.

#### Issues with JetBrains IDE popups/menus losing focus

Some JetBrains IDEs (including Android Studio) ship with a Java 1.8 JRE, but there are fixes included in later JRE versions that are necessary to run properly in Sway. You can instruct your IDE to use a different JRE through an invocation of the form:

```sh
STUDIO_JDK=/usr/lib/jvm/java-11-openjdk-amd64/ /opt/android-studio/bin/studio.sh
```

If you are running Sway 1.4 or earlier, you will also need to upgrade to Sway/wlroots master, as there are necessary fixes there too.

### Status icon doesn't show up

There are two standards for status icons: XEmbed and StatusNotifierItem (SNI). XEmbed is legacy and unimplemented in Sway. SNI is supported by swaybar. If your app uses XEmbed, the status icon won't show up. You should ask them to upgrade to SNI.

For network-manager-applet, see https://wiki.archlinux.org/index.php/NetworkManager#Appindicator

### I run a Linux distribution without systemd and sway does not start.

See [here](https://github.com/swaywm/sway/wiki/Running-Sway-with-seatd,-elogind-or-systemd%E2%80%90logind).

### I have a multi-gpu setup (like intel+nvidia or intel+amd) and sway does not start / Some video cards cannot display / Full screen images, etc. will be corrupted

Unless specified otherwise, `wlroots` will choose a card for you and you could have a similar message in sway's log:

To use a different default card (listed in `/dev/dri/`), set this environment variable before starting sway:

```sh
WLR_DRM_DEVICES=/dev/dri/card1 sway
```

It's likely that you want sway to use the integrated (Intel) card, because probably that's the only one directly connected to the laptop monitor. However, the mapping between node names in `/dev/dri/` and actual cards isn't guaranteed to be the same across reboots.

<!--
TODO: this script is broken, passes the value of the boolean "boot_vga" attr and interprets it as a card number.

This script detects which is the device path of the integrated card and launches sway accordingly:

```sh
#!/bin/sh
val=$(udevadm info -a -n /dev/dri/card1 | grep boot_vga | rev | cut -c 2)
WLR_DRM_DEVICES="/dev/dri/card$val" sway
```
-->

You can also configure multiple graphics cards like so:

```sh
WLR_DRM_DEVICES=/dev/dri/card0:/dev/dri/card1 sway
```

The first card is used for actual rendering, and display buffers are copied to the secondary cards for any displays connected to them.

If your card paths aren't consistent (for example with eGPUs), you cannot use paths from `/dev/dri/by-path`, as they contain the delimiter which (unfortunately) cannot be escaped.\
As a workaround you can create symlinks for the cards with a udev rule (`/etc/udev/rules.d/set-dri-links.rules`):
```
KERNEL=="card*", SUBSYSTEM=="drm", ATTRS{vendor}=="0x1002", ATTRS{device}=="0x747e", SYMLINK+="dri/by-name/egpu"
KERNEL=="card*", SUBSYSTEM=="drm", ATTRS{vendor}=="0x1002", ATTRS{device}=="0x1681", SYMLINK+="dri/by-name/igpu"
```
You can get the ATTRS{vendor} and ATTRS{device} from `udevadm info /dev/dri/cardX --attribute-walk`\
and set the variable as following:
```sh
WLR_DRM_DEVICES=/dev/dri/by-name/egpu:/dev/dri/by-name/igpu
```

### My GTK+3 theme isn't working

See [GTK 3 settings on Wayland](./GTK-3-settings-on-Wayland).

### After unplugging an external display, some applications appear too large on my HiDPI screen

See [wlroots issue #1119](https://github.com/swaywm/wlroots/issues/1119). This is an Xwayland bug fixed in 1.20.9.

Workaround:

1. If it does not exist, create the file  `~/.Xresources`
2. Add the following line to `~/.Xresources`:

   ```
   Xft.dpi: 96
   ```
3. Add the following line to the Sway config:
   ```sh
   exec xrdb -load ~/.Xresources
   ```

### Is an application using Xwayland?

To figure out whether an application uses Xwayland or native Wayland, you can try one of these solutions:

1. Run `xeyes` and move the mouse over the app. The eyes will only move if the window is using Xwayland.
2. Add `for_window [shell=".*"] title_format "%title :: %shell"` to your config file.
3. `swaymsg -t get_tree` dumps information about all windows.

### Mouse events (clicking, scrolling) aren't working on some of my workspaces

If your monitor layouts uses negative pixels, you're probably hitting this issue : https://gitlab.freedesktop.org/xorg/xserver/issues/899

This is a Xwayland bug. The workaround is to rearrange your workspaces to not use negative pixels.

### Xwayland DPI increases after hotplug

This is an [Xwayland bug](https://gitlab.freedesktop.org/xorg/xserver/-/issues/731). This usually results in oversized text. As a workaround, add `Xft.dpi: 96` to `~/.Xresources` and add `exec xrdb -load ~/.Xresources` to your Sway config.

### I can't open links in external applications in Firefox

If you get the message "Firefox is already running", set the environmental variable `MOZ_DBUS_REMOTE=1` (Firefox 74+, dbus required). See explanation here: [https://mastransky.wordpress.com/2020/03/16/wayland-x11-how-to-run-firefox-in-mixed-environment/](https://mastransky.wordpress.com/2020/03/16/wayland-x11-how-to-run-firefox-in-mixed-environment/)

### Android studio draws the menus in the wrong place

Try something like this:

```sh
# For Android Studio
export _JAVA_AWT_WM_NONREPARENTING=1
export STUDIO_JDK=/usr/lib/jvm/java-14-openjdk

# For Gradle
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
```

Adjust the paths so that they point to a valid location on your system.

### GTK+ applications take 20 seconds to start

This is due to GTK+ waiting for `xdg-desktop-portal` to start via D-Bus. This times out because the D-Bus activated service doesn't know what `WAYLAND_DISPLAY` to connect to.

See [Systemd and dbus activation environments](#systemd-and-dbus-activation-environments)

Alternatively, set `GTK_USE_PORTAL=0` in your environment.

More details: https://github.com/swaywm/sway/issues/5732

### Wayland won't let me run apps as root

Generally speaking, running graphical applications as root is discouraged. Modern Linux distributions usually ship with a configured Polkit system which allows applications to request permissions for specific administrative actions as needed. Arch Linux wiki about Polkit is a good source of information https://wiki.archlinux.org/title/Polkit.

As a Sway user, all you probably need to do is run *any* one of the polkit auth agents. When a polkit auth agent is running you will get a prompt when an application supports Polkit and needs administrative permissions for some actions.

Auth agent exact location (and whether they are installed) depend on your distribution. Two most common agents are:
 * polkit-gnome-authentication-agent-1 (GTK/Gnome)
 * polkit-kde-authentication-agent-1 (Qt/KDE)

They usually reside in `/usr/libexec` or `/usr/lib` directories. You will want to put for example following in your sway config:
`exec "/usr/libexec/polkit-gnome-authentication-agent-1"`

If the application does not support Polkit or you are running system without Polkit there is an additional fallback option if you really need to run a gui application as root: `sudo --preserve-env=XDG_RUNTIME_DIR,WAYLAND_DISPLAY <app>` or simply `sudo -E <app>`. This should be a last-resort option however.

### Clutter applications hang at startup

This is ultimately caused by Clutter's reliance on the deprecated `wl_shell` protocol. Unless/until https://gitlab.gnome.org/GNOME/clutter/-/merge_requests/5 is merged, a workaround is to set `CLUTTER_BACKEND=gdk` to have it use gdk rather than attempt to interface directly with the compositor. 

### Sway 1.6 shows garbage or a blank screen on Nouveau

Could manifest as a blank screen where windows or bars are not drawn at all, only the mouse pointer. Could manifest an inactive display where the monitor receives no input at all.

Try setting `WLR_DRM_NO_MODIFIERS=1`. If you have it set, try un-setting it.

Issues when modifiers are enabled are due to two Nouveau bugs, fixed in these merge requests, and released in mesa 21.1.0:

- https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/8500
- https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/3724

### `eglInitialize` errors on with nouveau

This usually means that nouveau doesn't support your GPU. See https://nouveau.freedesktop.org/FeatureMatrix.html

### Sway shows garbage or blank screen on usb-c 3.2 Gen 2 DisplayPort monitor.

Could manifest as blank screen or incomplete terminal output.

Try rendering sway with vulkan using `WLR_RENDERER=vulkan`. (WARNING: Tested on AMD Gpu).

Vulkan-validation layers is required for some distros.
- Arch: [vulkan-validation-layers](https://archlinux.org/packages/extra/x86_64/vulkan-validation-layers/)
- Void: [Vulkan-ValidationLayers](https://github.com/void-linux/void-packages/tree/master/srcpkgs/Vulkan-ValidationLayers)

### How can I setup keyboard volume keys?

You'll need to bind these keys in your configuration file. For instance, if you're using PulseAudio:

```
bindsym --locked XF86AudioMute exec pactl set-sink-mute @DEFAULT_SINK@ toggle
bindsym --locked XF86AudioLowerVolume exec pactl set-sink-volume @DEFAULT_SINK@ -5%
bindsym --locked XF86AudioRaiseVolume exec pactl set-sink-volume @DEFAULT_SINK@ +5%
bindsym --locked XF86AudioMicMute exec pactl set-source-mute @DEFAULT_SOURCE@ toggle
```

If you use wireplumber, setting `-l` flag in `wpctl` can be used to prevent the volume from exceeding a certain level, which is not a feature offered by `pactl`. This example ensures that the volume does not surpass 120%:

```
bindsym --locked XF86AudioMute exec wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
bindsym --locked XF86AudioLowerVolume exec wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- -l 1.2
bindsym --locked XF86AudioRaiseVolume exec wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ -l 1.2
```

[SetEnvPage]: https://github.com/swaywm/sway/wiki/Setting-environmental-variables

### My screen isn't detected when plugged in

Sometimes the kernel driver has trouble detecting hotplugged monitors on some ports. Try this (adapt `card0` and `DP-1` to the GPU and connector you're using):

    echo detect | sudo tee /sys/class/drm/card0-DP-1/status


### How do I utilize `wp-fractional-scale-v1` since Sway 1.9?

[Fractional scale protocol](https://wayland.app/protocols/fractional-scale-v1)

> This protocol allows a compositor to suggest for surfaces to render at fractional scales.

* recent [versions of Chrome/Chromium/Blink Derivatives](https://www.phoronix.com/news/Chrome-fractional-scale-v1) utilize it automatically
* [recent Firefox versions](https://bugzilla.mozilla.org/show_bug.cgi?id=1420259) require `about:config` `widget.wayland.fractional-scale.enabled=true`, which is as of 2024-03 having two bugs. [Context Menu Broken](https://bugzilla.mozilla.org/show_bug.cgi?id=1849109), [Blurred Windows when not maximized](https://bugzilla.mozilla.org/show_bug.cgi?id=1849092)
* [mpv](https://github.com/mpv-player/mpv/issues/8514) in standard configuration/wayland mode will utilize it automatically and appears to have no known issues

### No hardware acceleration since Sway 1.10

Typically this results in error messages like these:

```
vulkan: No DRI3 support detected - required for presentation
Note: you can probably enable DRI3 in your Xorg config
```

or

```
DRI3 not available
```

or VA-API fails to initialize.

Sway 1.10 has removed support for the legacy `wl_drm` Wayland protocol, which is still used by Xwayland 23.2.4 and earlier, libva 2.20.0 and earlier, and AMDVLK.

As a workaround, the legacy `wl_drm` Wayland protocol can be re-enabled manually by passing `-Dlegacy-wl-drm` to Sway.

See:

- [xserver!1236](https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1236)
- [libva#788](https://github.com/intel/libva/pull/788) and [libva#790](https://github.com/intel/libva/pull/790)
- [AMDVLK#351](https://github.com/GPUOpen-Drivers/AMDVLK/issues/351)

### `wmenu` doesn't show command suggestions as you type

```
set $menu dmenu_path | wmenu | xargs swaymsg exec --
```

`dmenu_path` is provided by the package `dmenu`. Because it's often regarded as an optional dependency of Sway, it's likely that you don't have it installed.

UPDATE: Merged PR [#8289](https://github.com/swaywm/sway/pull/8289) has eliminated the dependency on _dmenu_. The default configuration will run `wmenu-run` instead.

```
set $menu wmenu-run
```