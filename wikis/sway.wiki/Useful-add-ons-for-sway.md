Here is a list of apps and scripts for Sway (and probably other Wayland compositors based on wlroots).

Note that pretty much all GTK and KDE apps such as firefox, thunderbird, chromium, even emacs (with the puregtk/emacs-28 branch) can be run as native wayland under sway so they're not listed here.

A collection of user-contributed scripts is available in [sway-contrib](https://github.com/OctopusET/sway-contrib).

An extensible `Guile` scheme bindings for sway with easy to configure modules to manage workspaces, nested keybindings, layouts, and events is available in [guile-swayer](https://github.com/ebeem/guile-swayer).

[WIP] = Work in progress or alpha status

## Login managers

* [greetd](https://git.sr.ht/~kennylevinsen/greetd) - minimal and flexible login manager daemon
  * [gtkgreet](https://git.sr.ht/~kennylevinsen/gtkgreet) - minimal gtk based login manager
  * [qtgreet](https://gitlab.com/marcusbritanicus/QtGreet) - fancy qt based login manager
  * [tuigreet](https://github.com/apognu/tuigreet) - simple graphical console login manager
  * [wlgreet](https://git.sr.ht/~kennylevinsen/wlgreet) - wayland login manager
  * [regreet](https://github.com/rharish101/ReGreet) - Clean and customizable greeter for greetd
* [emptty](https://github.com/tvrzna/emptty/) - dead simple CLI Display Manager on TTY
* [Ly](https://codeberg.org/AnErrupTion/ly) - lightweight TUI (ncurses-like) display manager
* [autologin](https://git.sr.ht/~kennylevinsen/autologin) - automatically logs into the configured user; perfect for computers with a single user and another method of startup authentication (like encrypted hard-drive)
* [uwsm](https://github.com/Vladimir-csp/uwsm) - Universal Wayland Session Manager that wraps sway (or other compositors) into systemd units. Supports integrating into login shell, XDG autostart, environment management, launching applications in units. Extendable with plugins.
* [gdm3](https://gitlab.gnome.org/GNOME/gdm) - Supports starting sway/wayland, comes with a bunch of features out of the box

## Launchers

Generic launchers for GTK or KDE such as [xfce4-appfinder](https://docs.xfce.org/xfce/xfce4-appfinder/start) and krunner work fine but the following were written with sway in mind:

* [kickoff](https://github.com/j0ru/kickoff) - application launcher with a focus on performance and low latency
* ~[lavalauncher](https://git.sr.ht/~leon_plickat/lavalauncher) - simple launcher for Wayland~ (unmaintained)
* [nwg-launchers](https://github.com/nwg-piotr/nwg-launchers) - set of launchers: application grid, dynamic menu, button bar
* [Ulauncher](https://ulauncher.io/) - app launcher
* [wldash](https://sr.ht/~kennylevinsen/wldash/) - dashboard/launcher/control-panel thing for Wayland
* [yofi](https://github.com/l4l/yofi) - minimalistic application launcher for wayland
* [gmenu](https://code.rocketnine.space/tslocum/gmenu) - Desktop application launcher
* [mauncher](https://github.com/mortie/mauncher) - GTK-based alternative to dmenu for Wayland which supports display scaling
* [fuzzel](https://codeberg.org/dnkl/fuzzel) - application launcher, similar to rofi's drun mode
* [term-dmenu](https://github.com/Seirdy/term-dmenu) - Replace dmenu with a floating terminal and FZF
* [sirula](https://github.com/DorianRudolph/sirula) - Simple app launcher for Wayland written in Rust
* [onagre](https://github.com/oknozor/onagre) - [pop-launcher](https://github.com/pop-os/launcher) based application launcher for wayland and X.
* [raffi](https://github.com/chmouel/raffi) - application launcher designed to sit on top of Fuzzel, or, if preferred, operate using its own built‑in interface. 
* [zofi](https://github.com/emskin/zskins/tree/master/crates/zofi) - — a fast Wayland application launcher powered by Zed's GPU rendering engine. Search, select, and launch apps instantly. 

## Menus
* [wmenu](https://codeberg.org/adnano/wmenu) - is an efficient dynamic menu for Sway and wlroots based Wayland compositors.
* [wofi](https://hg.sr.ht/~scoopta/wofi) - rofi inspired menu and launcher for wlroots compositors
* [bemenu](https://github.com/Cloudef/bemenu) - dmenu replacement with Wayland support
* [tofi](https://github.com/philj56/tofi) - Tiny dynamic menu for Wayland
* [wlogout](https://github.com/ArtsyMacaw/wlogout) - wayland based logout menu wlogout
* [rofi](https://github.com/davatorium/rofi) - now supports Wayland since version 2.0.0. Acts as a window switcher, application launcher, ssh launcher, etc. and has a large amount of community-made [themes](https://github.com/davatorium/rofi/wiki/Themes), [plugins](https://github.com/adi1090x/rofi) and [user scripts](https://github.com/davatorium/rofi/wiki/User-scripts) available
* [dmenu-wl](https://github.com/nyyManni/dmenu-wayland) - an efficient dynamic menu for wayland (wlroots).
* [sway-launcher-desktop](https://github.com/Biont/sway-launcher-desktop) - TUI-based launcher menu made with bash and the amazing fzf
* [i3-menu](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-menu) - menu generated from bindsym for learning sway keystrokes and remembering obscure ones (was 'sway-menu' but now also runs on i3wm)
* [sway-mode](https://gitlab.com/wef/dotfiles/-/blob/master/bin/sway-mode) - Head-up-display (HUD) help while running 'modes' such as 'move-mode'
* [sway-fzfify](https://github.com/ldelossa/sway-fzfify) - series of scripts which FZFify your sway desktop.
* [waylogout](https://github.com/loserMcloser/waylogout) - graphical logout/suspend/reboot/shutdown dialog inspired by oblogout and based on code from swaylock-effects.
* [wlr-which-key](https://github.com/MaxVerevkin/wlr-which-key) - Keymap manager for wlroots-based compositors in Rust.
* [sway-yasm](https://github.com/pancsta/sway-yasm) - Manage windows, workspaces, outputs, clipboard and PATH using FZF.

## Display/outputs

* [qkdisplays](https://github.com/tamirzb/qkdisplays) - A helper tool for quickly configuring a multi-monitor setup, built with tiled window managers in mind
* [wob](https://github.com/francma/wob) - lightweight overlay volume/backlight/progress/anything bar for Wayland.
* [mywob](https://gitlab.com/wef/dotfiles/-/blob/master/bin/mywob) - autostarts wob(1)
* [wdisplays](https://github.com/artizirk/wdisplays) - GUI display configurator for wlroots compositors [like arandr(1)] (Mirror since the [upstream](https://github.com/cyclopsian/wdisplays) has been deleted)
* [wlr-randr](https://gitlab.freedesktop.org/emersion/wlr-randr) - manage outputs of a Wayland compositor.
* [wlay](https://github.com/atx/wlay) - Graphical output management for Wayland
* [kanshi](https://gitlab.freedesktop.org/emersion/kanshi) - define output profiles that are automatically enabled and disabled on hotplug. eg, this can be used to turn a laptop's internal screen off when docked.
* [swayrst](https://github.com/Nama/swayrst) - Save and restore your outputs, workspaces and windows
* [fade](https://github.com/user18130814200115-2/swayscrips/tree/main/fade) - Have new windows fade in gradually. This script is alpha (get it;)) at best, you may encounter issues.
* [way-displays](https://github.com/alex-courtis/way-displays) - Manage Your Wayland Displays
* [nwg-displays](https://github.com/nwg-piotr/nwg-displays) - Output management utility for sway Wayland compositor, inspired by wdisplays and wlay.
* [shikane](https://gitlab.com/w0lff/shikane) - dynamic output configuration tool that automatically detects and configures
connected outputs based on a set of profiles.

## Image viewers
* [Oculante](https://github.com/woelper/oculante) - Hardware accelerated image viewer with broad format support and basic editing features.
* [pqiv](https://github.com/phillipberndt/pqiv) - Powerful GTK 3 based command-line image viewer with a minimal UI.
* [imv](https://sr.ht/~exec64/imv/) - Command line image viewer intended for use with tiling window managers. Currently [does not support fractional scaling](https://todo.sr.ht/~exec64/imv/70).
* [mvi](https://github.com/occivink/mpv-image-viewer) - Command line image viewer utilizing mpv
* [ucollage](https://github.com/ckardaris/ucollage) - Extensible command line image viewer inspired by vim.
* [swayimg](https://github.com/artemsen/swayimg) - Image viewer for Sway/Wayland
* ~[vimiv](https://github.com/karlch/vimiv) - Image viewer with vim-like keybindings. (deprecated)~
* [vimiv-qt](https://github.com/karlch/vimiv-qt) - Image viewer with vim-like keybindings using Qt. (Future of vimiv)

> TIP: The `kitty` [terminal](#terminals) emulator has a built-in image viewer, [icat](https://sw.kovidgoyal.net/kitty/kittens/icat/).

> TIP: [ueberzugpp](https://github.com/jstkdng/ueberzugpp) has `tmux` support on `sway`.

## Video Players

* [mpv](https://github.com/mpv-player/mpv) - Command line video player

## Notification
* [mako](https://github.com/emersion/mako) - lightweight notification daemon for Wayland.
* [fnott](https://codeberg.org/dnkl/fnott) - Keyboard driven and lightweight Wayland notification daemon
* [dunst](https://github.com/dunst-project/dunst) - highly configurable and lightweight notification daemon.
* [wayherb](https://github.com/muevoid/Wayherb) - Wayland notifcation port of herbe - daemon-less notifications without D-Bus. Minimal and lightweight.
* [swaync](https://github.com/ErikReider/SwayNotificationCenter) - simple notification daemon with a notification center built with GTK
* [salut](https://gitlab.com/snakedye/salut) - Animated mouse centric notification daemon

## Workspaces
* [workstyle](https://github.com/pierrechevalier83/workstyle) - dynamically rename your workspaces to indicate which programs are running in each one.
* [sworkstyle](https://github.com/Lyr-7D1h/swayest_workstyle) - The main difference between this and workstyle is that this supports exact app names instead of only generic titles.
* [wsdnames.py](https://github.com/nwg-piotr/swayinfo/blob/master/wsdnames.py) - automatically renames workspace title
* [swaysome](https://gitlab.com/hyask/swaysome) - manage workspaces namespaced on a per-screen basis, like awesome wm.
* [swaywsr](https://github.com/pedroscaff/swaywsr) - sway workspace renamer, a port of i3wsr for Sway written in Rust.
* [swaymsg_workspace](https://github.com/berezowski/swaymsg_workspace) - reorder, switch, rename workspaces. (written in Rust)

## Overview
* [sov](https://github.com/milgra/sov) - Similar to [i3-overview](https://github.com/milgra/i3-overview): An overlay that shows schemas for all workspaces to make navigation in sway easier. 
* [exposway](https://github.com/RadioNoiseE/exposway) - Similar to MacOS X Exposé. Provides an overview of all windows.
* [windows](https://github.com/RadioNoiseE/windows) - Successor to [exposway](https://github.com/RadioNoiseE/exposway). Allows window overview and selection.

## Layouts
* [autotiling](https://github.com/nwg-piotr/autotiling) - switch the layout splith/splitv depending on the currently focused window dimensions.
* [autotiling-rs](https://github.com/ammgws/autotiling-rs) - Same idea as autotiling but implemented as a single binary instead of a python script.
* [persway](https://github.com/johnae/persway) - enforces spiral and main-stack layouts
* [swaymonad](https://github.com/nicolasavru/swaymonad) - an auto-tiler that implements Xmonad-like layouts.
* [papersway](https://spwhitton.name/tech/code/papersway/) - PaperWM-style scrollable window management for sway/i3wm.
* [i3-set-layout](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-set-layout?ref_type=heads) - simple bash script for various layouts eg horiz, vert, monocle, spiral, vmv (works on sway and i3)

## Screenshot
* [grim](https://gitlab.freedesktop.org/emersion/grim) - grab images from a Wayland compositor
* [grimshot](https://github.com/OctopusET/sway-contrib/blob/master/grimshot) - script to grab regions from the window. (doesn't take screenshots by itself).
* [slurp](https://github.com/emersion/slurp) - select a region in a Wayland compositor
* [screenshot-bash](https://gitlab.com/Scrumplex/screenshot-bash) - screenshot - upload - copy-url pipeline
* [snag](https://github.com/b0o/snag) - snag screenshots and screencasts with Rofi 
* [swappy](https://github.com/jtheoof/swappy) - screen snapshot & editor
* [swayshot](https://gitlab.com/radio_rogal/swayshot) - Print screen helper for sway adds keyboard shortcuts for screenshots
* [shotman](https://git.sr.ht/~whynothugo/shotman) - takes a screenshot and shows a small thumbnail with basic actions.
* [taiga](https://hg.sr.ht/~scoopta/taiga) - an animated screenshot program
* [wayshot](https://git.sr.ht/~shinyzenith/wayshot) - native screenshot tool for wlroots based compositors such as sway and river written in Rust.
* [flameshot](https://github.com/flameshot-org/flameshot) - Powerful yet simple to use screenshot software
* [sway-screenshot](https://github.com/Gustash/sway-screenshot) - Utility to easily take screenshot in swaywm using your mouse
* [hyprpicker](https://github.com/hyprwm/hyprpicker) - wlroots-compatible Wayland color picker

## Screen magnifiers/zoomer
* [woomer](https://github.com/coffeeispower/woomer) - Zoomer application for Wayland inspired by tsoding's boomer
* [hyprmag](https://github.com/SIMULATAN/hyprmag) - A wlroots-compatible Wayland screen magnifier with basic customization options.

## Brightness
* [brightnessctl](https://github.com/Hummer12007/brightnessctl/) - control device brightness
* ~[light](https://github.com/haikarainen/light) - control backlights~ (unmaintained) (archived)
* [clight](https://github.com/FedeDP/Clight) - C user daemon utility that aims to fully manage your display (And a GUI for it [clight-gui](https://github.com/nullobsi/clight-gui) )
* [wluma](https://github.com/maximbaz/wluma) - automatically adjusts screen brightness based on the screen contents and amount of ambient light around you
* [brillo](https://github.com/CameronNemo/brillo) - controls the brightness of backlight and LED devices on Linux.
* ~[wlr-brightness](https://github.com/mherzberg/wlr-brightness) - adjust the brightness of your screen~ (unmaintained) (archived)
* [wl-gammarelay](https://github.com/jeremija/wl-gammarelay) - daemon with D-Bus interface to control display color temperature and brightness
* [wl-gammarelay-rs](https://github.com/MaxVerevkin/wl-gammarelay-rs) - daemon with D-Bus interface to control display color temperature and brightness written in Rust
* [lumactl](https://github.com/danyspin97/lumactl) - control backlight and external monitor brightness (via DDC)

## Gamma
* [wl-gammactl](https://github.com/mischw/wl-gammactl) - Small GTK GUI application to set contrast, brightness and gamma
* [gammastep](https://gitlab.com/chinstrap/gammastep) - Adjust the color temperature of your screen
* [wlsunset](https://sr.ht/~kennylevinsen/wlsunset/) - Day/night gamma adjustments for Wayland
* [wl-gammarelay](https://github.com/jeremija/wl-gammarelay) - daemon with D-Bus interface to control display color temperature and brightness
* [wl-gammarelay-rs](https://github.com/MaxVerevkin/wl-gammarelay-rs) - daemon with D-Bus interface to control display color temperature and brightness written in Rust

## Colorscheme
* [darkman](https://gitlab.com/WhyNotHugo/darkman) framework for dark-mode and light-mode transitions, implementing org.freedesktop.appearance.color-scheme

## Wallpaper
* [swaybg](https://github.com/swaywm/swaybg) - Wallpaper tool
* [sw_swaybg](https://github.com/pd2s/sw/tree/master/examples/sw_swaybg) - Feature-compatible with original swaybg. Supports more image formats, has fewer dependencies, more cpu-efficient.
* [azote](https://github.com/nwg-piotr/azote) - Wallpaper and colour manager for Sway, i3 and some other WMs
* [wallutils](https://github.com/xyproto/wallutils) - wallpaper manager
* [glpaper](https://hg.sr.ht/~scoopta/glpaper) - wallpaper program that allows you to render glsl shaders as your wallpaper
* [mpvpaper](https://github.com/GhostNaN/mpvpaper) - wallpaper program that allows you to play videos with mpv as your wallpaper
* [qt-video-wlr](https://github.com/xdavidwu/qt-video-wlr) - Qt5 video player
* ~[oguri](https://github.com/vilhalmer/oguri) - very nice animated wallpaper daemon~ (archived and unmaintained)
* [sunpaper](https://github.com/hexive/sunpaper) - linux utility to change wallpaper based on local sunrise and sunset times.
* [wpaperd](https://github.com/danyspin97/wpaperd) - Wallpaper daemon for Wayland that can change the wallpaper after a fixed time.
* [awww](https://codeberg.org/LGFae/awww) -  An Answer to your Wayland Wallpaper Woes.
* [wsbg](https://github.com/saibier/wsbg) - Wallpaper tool with per-workspace configuration
* [wbg](https://codeberg.org/dnkl/wbg) - Super simple wallpaper application for Wayland compositors implementing the layer-shell protocol
* [waypaper](https://github.com/anufrievroman/waypaper) - GUI wallpaper manager for both Wayland and Xorg window managers
* [Waypaper-Engine](https://github.com/0bCdian/Waypaper-Engine) - graphical frontend for setting wallpapers and playlists, using [swww](https://github.com/Horus645/swww) under the hood!
* [WAT](https://github.com/faraday22/WAT) - console based wallpaper changer made in Lua, for sway
* [multibg-wayland](https://github.com/gergo-salyi/multibg-wayland) - Wallpaper tool with per-workspace and per-output images

## Bars & panels

* [swaybar](https://github.com/swaywm/sway) - default bar for sway
* [sw_swaybar](https://github.com/pd2s/sw/tree/master/examples/sw_swaybar) - Almost feature-compatible with original swaybar. Supports tray dbusmenu. Has fewer dependencies, more cpu-efficient.
* [waybar](https://github.com/Alexays/Waybar) - Highly customizable Wayland bar for Sway
* ~~[yambar](https://codeberg.org/dnkl/yambar) - lightweight and configurable status panel~~ (archived)
* [rootbar](https://hg.sr.ht/~scoopta/rootbar) - bar for wlroots based wayland compositors such as sway
* [rwaybar](https://github.com/danieldg/rwaybar)  - bar with configurable widgets and transparent overlay support
* [wapanel](https://github.com/Firstbober/wapanel) - Simple panel for Wayland with decent XFCE-like applets
* [sfwbar](https://github.com/LBCrion/sfwbar) - Sway Floating Window Bar is a taskbar for Sway, focused on a stacking layout workflow
* [nwg-shell](https://github.com/nwg-piotr/nwg-shell) - 'shell' for wl-roots including various other nwg-* components listed here
* [nwg-panel](https://github.com/nwg-piotr/nwg-panel) - GTK-based panel, inspired by Waybar and tint2
* [nwg-dock](https://github.com/nwg-piotr/nwg-dock) - Fully configurable dock featuring pinned buttons, task buttons, the workspace switcher and the launcher button.
* [nwg-menu](https://github.com/nwg-piotr/nwg-menu) - Menu for nwg-shell
* [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer) - launcher for nwg-shell
* [nwg-bar](https://github.com/nwg-piotr/nwg-bar) - simple button bar for nwg-shell
* [nwg-wrapper](https://github.com/nwg-piotr/nwg-wrapper) - display text or images on any layer (eg root)
* [ironbar](https://github.com/JakeStanger/ironbar) - feature-rich bar/panel that is compatible with sway and hyprland and can be customized quite well

### Bar content generators
* [swayrbar](https://sr.ht/~tsdh/swayr/#swayrbar) - swayrbar is a status command for sway's swaybar implementing the [swaybar-protocol](https://man.archlinux.org/man/swaybar-protocol.7)
* [i3status](https://i3wm.org/i3status/) - Status bar generator for i3bar, dzen2, xmobar or similar programs
* [i3blocks](https://github.com/vivien/i3blocks) - feed generator for text based status bars (yes, it works fine with swaybar!)
* [luastatus](https://github.com/shdown/luastatus) - Universal status bar content generator
* [i3status-rs](https://github.com/greshake/i3status-rust) - feature-rich and resource-friendly replacement for i3status, written in pure Rust. It provides a way to display "blocks" of system information (time, battery status, volume, etc) on the i3 bar. It is also compatible with sway.
* [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo) - prints system usage information as text for Waybar custom modules or icon/text for nwg-panel executors
* [statusbar](https://gobytes.dev/statusbar) - fully-featured, customizable, extensible, and well-documented content generator for swaybar/i3bar. It offers a variety of widgets, allows for integration with other generators (listed above), and makes it easy to implement your own widgets using Go.
* [swaybar-commander](https://jasoncarloscox.com/creations/swaybar-commander/) - status command for swaybar that uses the swaybar-protocol to independently update user-defined content blocks
* [ipc_bar](https://github.com/flowthentic/ipc_bar) - IPC bar BASH content generator

## Widgets
* [AGS](https://github.com/Aylur/ags) (Aylur's Gtk Shell) - Library built for [GJS](https://gitlab.gnome.org/GNOME/gjs) (Gnome JavaScript) to allow defining GTK widgets in a declarative way.
* [Eww](https://github.com/elkowar/eww) - standalone widget system made in Rust that allows you to implement your own, custom widgets
* [Gsimplecal](https://github.com/dmedvinsky/gsimplecal) - lightweight calendar applet written in C++ using GTK.
* [wlclock](https://git.sr.ht/~leon_plickat/wlclock) - digital analog clock for Wayland desktops.
* [wl-binclock](https://github.com/dongdigua/wl-binclock) -  colorful binary clock for wayland.
* [wlr-sunclock](https://github.com/sentriz/wlr-sunclock) - desktop widget to show to the sun's shadows on earth.
* [quickshell](https://github.com/quickshell-mirror/quickshell) - Flexible toolkit for making desktop shells with QtQuick, for Wayland and X11.

## Other shell components

* [wlhc](https://git.sr.ht/~whynothugo/wlhc) (Wayland hot corners) - execute a command when the pointer touches a corner of the screen.

## Keyboard/Input
* [swhkd](https://github.com/waycrate/swhkd) - sxhkd clone for Wayland (works on TTY and X11 too)
* [wev](https://git.sr.ht/~sircmpwn/wev) - event debugging similar to xev for X11
* [wshowkeys](https://github.com/ammgws/wshowkeys) - display keypresses (fork with fixes for recent wlroots versions, original [here](https://git.sr.ht/~sircmpwn/wshowkeys))
* [keyd](https://github.com/rvaiya/keyd) -key remapping daemon for linux.
* [xremap](https://github.com/xremap/xremap) - Key remapper for X11 and Wayland
* [dotool](https://git.sr.ht/~geb/dotool) - Command to simulate input anywhere (X11/Wayland/TTYs) [like xdotool(1)]
* [ydotool](https://github.com/ReimuNotMoe/ydotool) - Generic command-line automation tool (no X!) [like xdotool(1)]
* [myautotype](https://gitlab.com/wef/dotfiles/-/blob/master/bin/myautotype) - Hot-keys using ydotool/wtype/xdotools possibly looking up a key-value pair from ~/.config/myautotype
* [wtype](https://github.com/atx/wtype) - xdotool type for wayland
* [clipman](https://github.com/chmouel/clipman) - basic clipboard manager for Wayland, with support for persisting copy buffers after an application exits.
* [copyq](https://hluk.github.io/CopyQ/) - full function clipboard manager (but requires the full KDE/Qt stack)
* [cliphist](https://github.com/sentriz/cliphist) - clipboard history “manager” for wayland (including images) - requires golang-1.16 to build
* [lisgd](https://git.sr.ht/~mil/lisgd) - bind gestures on touchscreens, and unsupported gesture devices via libinput touch events
* [wl-clipboard](https://github.com/bugaevc/wl-clipboard) - Wayland clipboard utilities, wl-copy and wl-paste, to copy data between the clipboard and Unix pipes, sockets, files etc
* [wl-clipboard-history](https://github.com/janza/wl-clipboard-history) - Wayland clipboard history tracker
* [clipmon](https://git.sr.ht/~whynothugo/clipmon) - preserves the clipboard and notifies when an application pastes (for security)
* [swaykbdd](https://github.com/artemsen/swaykbdd) - per-window keyboard layout for Sway
* [i3keys](https://github.com/RasmusLindroth/i3keys) - lists all the keys that are bound to some action in i3 or sway
* [swaynagmode](https://github.com/b0o/swaynagmode) - programmatic control over swaynag, intended for use with keyboard bindings
* [sway-alttab](https://github.com/reisub0/sway-alttab) - simple daemon that keeps track of your last focused window and switches to it on receiving a SIGUSR1. Automatically binds Alt-Tab to the same action.
* [wlrctl](https://git.sr.ht/~brocellous/wlrctl) - command line utility for miscellaneous wlroots Wayland extensions (similar to xdotool). WARNING: requires sway-1.6+
* [waynergy](https://github.com/r-c-f/waynergy) - [WIP] implementation of a synergy client for wlroots compositors
* [swayr](https://sr.ht/~tsdh/swayr/) - urgent-first/LRU window and workspace switcher usable with launcher/menu programs such as wofi.
* [wl-clip-persist](https://github.com/Linus789/wl-clip-persist) - Keep Wayland clipboard even after programs close
* [sway-input-config](https://github.com/Sunderland93/sway-input-config) - Input device configurator for Sway, written on Qt/Python
* [sway-overfocus](https://github.com/korreman/sway-overfocus) - Customizable basic focus commands, so you can navigate between splits while skipping past tabs and stacks.

## Input Method Editors

* [kime](https://github.com/Riey/kime) - [WIP] Korean IME
* [wlanthy](https://github.com/st3r4g/wlanthy) - [WIP] simple Wayland-native Japanese input method based on anthy
* [anthywl](https://github.com/tadeokondrak/anthywl) - [WIP] Japanese input method for sway based on anthy
* [wlhangul](https://gitlab.freedesktop.org/emersion/wlhangul) - [WIP] Hangul input method for Wayland.
* [wlpinyin](https://github.com/xhebox/wlpinyin) - [WIP] experimental minimal wayland IME for Chinese
* [wlchewing](https://github.com/xdavidwu/wlchewing) - [WIP] Wayland Chinese zhuyin input method with libchewing
* [fcitx5](https://github.com/fcitx/fcitx5) - generic input method framework released under LGPL-2.1+

## On-screen keyboards

* [squeekboard](https://gitlab.gnome.org/World/Phosh/squeekboard) - Librem5 keyboard
* [wvkbd](https://github.com/jjsullivan5196/wvkbd) - On-screen keyboard for wlroots that sucks less

## Idle timeout

* [swayidle](https://github.com/swaywm/swayidle) - An idle daemon for wayland compositors
* [wayidle](https://git.sr.ht/~whynothugo/wayidle) - Wait for a single idle timeout
* [wayidle.c](https://git.sr.ht/~whynothugo/wayidle.c) - C port of wayidle — Wait for a single idle timeout

## Locking

* [swaylock](https://github.com/swaywm/swaylock) - screen locking utility for Wayland compositors
* [Waylock](https://github.com/ifreund/waylock) - simple screenlocker for wayland compositors.
* [swaylock-effects](https://github.com/mortie/swaylock-effects) - fork of swaylock which adds built-in screenshots and image manipulation effects like blurring
* [mylock](https://gitlab.com/wef/dotfiles/-/blob/master/bin/mylock) - configure swaylock for various use-cases - safe, at-home, movie modes plus auto downloading of images
* [chayang](https://gitlab.freedesktop.org/emersion/chayang) - gradually dim the screen
* [swaydim](https://codeberg.org/achill/swaydim) - Dims your display using brightnessctl
* [swaylock-plugin](https://github.com/mstoeckl/swaylock-plugin) - fork of swaylock which can use existing wallpaper programs to draw the lockscreen background
* [gtklock](https://github.com/jovanlanik/gtklock) - screen locker with modules for userinfo (incl. photo), powerbar, mpris media controls, others

## Terminals

* [Alacritty](https://github.com/alacritty/alacritty) - fast, cross-platform, OpenGL terminal emulator
* [foot](https://codeberg.org/dnkl/foot/) - fast, lightweight and minimalistic Wayland terminal emulator
* [gnome-terminal](https://help.gnome.org/users/gnome-terminal/stable/) - gnome's terminal
* [kitty](https://sw.kovidgoyal.net/kitty/) - fast, featureful, GPU based terminal emulator
* [Konsole](https://github.com/KDE/konsole) - KDE's Terminal Emulator
* [sakura](https://launchpad.net/sakura) - Simple but powerful libvte based terminal emulator
* [roxterm](https://github.com/realh/roxterm) - terminal emulator intended to provide similar features to gnome-terminal, based on the same VTE library
* [wezterm](https://wezfurlong.org/wezterm) - GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust
* [Ate](https://github.com/andir/ate) - Awesome terminal emulator
* [Germinal](https://github.com/Keruspe/Germinal) - Minimalist vte-based terminal emulator
* [Havoc](https://github.com/ii8/havoc) - minimal terminal emulator for Wayland
* [wraith](https://github.com/gabydd/wraith) — Wayland runtime for ghostty
* [wterm](https://github.com/majestrate/wterm) - An st fork for wayland

## VNC/RDP/SPICE

* [wayvnc](https://github.com/any1/wayvnc) - VNC server for wlroots
* [wlvncc](https://github.com/any1/wlvncc) - Wayland VNC Client (WIP)
* [connections](https://gitlab.gnome.org/GNOME/connections) - Wayland VNC/RDP client - not quite feature complete in released version 3.38 eg no full-screen, buggy config GUI. 3.40 may fix that when released.
* [remotely](https://gitlab.gnome.org/World/Remotely) - wayland VNC client - abandoned by author in favour of connections.
* [vncviewer](https://tigervnc.org) - VNC client - fast, full featured, stable - but uses XWayland.
* [vinagre](https://wiki.gnome.org/Apps/Vinagre) - Wayland VNC/RDP client. VNC support is rather slow.
* [remmina](https://remmina.org/) - Wayland VNC/RDP/SPICE client. VNC support is rather slow.
* [krdc](https://apps.kde.org/krdc/) - Wayland VNC/RDP client. **AVOID** - does not support sway workspaces and took my session down!! Version 20.08.1
* [freerdp](https://www.freerdp.com) - Wayland RDP client (wlfreerdp) which is pretty fast (but needs the -grab-keyboard option to work with sway). Also xfreerdp, a fast XWayland RDP client. Tested against xrdp X11 server. Is there a 'wayrdp' server out there?

## Remote/recording

See also: [Screencast-Compatibility](https://github.com/emersion/xdg-desktop-portal-wlr/wiki/Screencast-Compatibility)

* [waypipe](https://gitlab.freedesktop.org/mstoeckl/waypipe) - waypipe is a proxy for Wayland clients. This makes application forwarding similar to ssh -X feasible.
* [wf-recorder](https://github.com/ammen99/wf-recorder) - Screen recorder for wlroots-based compositors eg swaywm. Uses the `wlr-screencopy-unstable-v1` interface.
* [wl-screenrec](https://github.com/russelltg/wl-screenrec) - Efficient screen recorder for wlroots-based compositors. Requires vaapi support. Uses the `wlr-screencopy-unstable-v1` interface.
* [cute-sway-recorder](https://github.com/it-is-wednesday/cute-sway-recorder) - Screen recorder for wlroots-based window managers, mainly Sway (a graphical Qt wrapper for wf-recorder)
* [obs-studio](https://github.com/obsproject/obs-studio) - capturing, compositing, encoding, recording, and streaming video content, efficiently (see wlrobs)
* [wlrobs](https://hg.sr.ht/~scoopta/wlrobs) - obs-studio plugin that allows you to screen capture on wlroots based wayland compositors
* [obs-gnome-screencast](https://github.com/fzwoch/obs-gnome-screencast) - Small source plugin to use GNOME Screen Cast functionality as a source for OBS Studio
* [green-recorder](https://github.com/dvershinin/green-recorder) - simple desktop recorder for Linux systems which uses the xdg-desktop-portal API.
* [txproto](https://github.com/cyanreg/txproto) - fully scriptable and flexible multimedia streaming/handling program.
* [wdomirror](https://github.com/progandy/wdomirror) - Create a mirror of an output with as little overhead as possible, aspect ratio is not preserved
* [wl-mirror](https://github.com/Ferdi265/wl-mirror) - simple Wayland output mirror client with more useful features.
* [ssr-wlroots](https://github.com/foxcpp/ssr-wlroots) - version of SimpleScreenRecorder with support for wlroots-based compositors (more specifically, those that support wlr-screencopy-v1 and xdg-output). Doesn't support recording area selection and has issues with multiple screens.
* [kooha](https://github.com/SeaDve/Kooha) - Capture your screen in a straightforward and painless way without distractions.

## Misc. Scripts

* [i3-fit-floats](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-fit-floats) - fits floating windows into workspace (was 'sway-fit-floats' but now also runs on i3wm)
* [i3-focus](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-focus) - focus an app by name (sway app_id or X11 class) (was 'sway-focus' but now also runs on i3wm)
* [sway-prep-xwayland]( https://gitlab.com/wef/dotfiles/-/blob/master/bin/sway-prep-xwayland) - prepare for Xwayland
* [i3-prop](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-prop) - show apps properties (similar to xprop) (was 'sway-prop' but now also runs on i3wm)
* [sway-select-window](https://gitlab.com/wef/dotfiles/-/blob/master/bin/sway-select-window) - use bemenu/rofi/wofi to go to a running app
* [sway-start](https://gitlab.com/wef/dotfiles/-/blob/master/bin/sway-start) - startup sway from the console
* [i3-track-firefox](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-track-firefox) - watch firefox (and other apps) and bind Shift-Insert to paste PRIMARY selection (was 'i3-track-firefox' but now also runs on i3wm)
* [i3-track-prev-focus](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-track-prev-focus) - mark container with _prev for rapid switching between apps; also make unfocused windows translucent (was 'sway-track-prev-focus' but now also runs on i3wm)
* [nmcli-rofi](https://github.com/jvanbruegge/dotfiles/blob/master/sway/wifi/nmcli-rofi) - Wofi script to select wifi and VPNs with nmcli
* [sway-new-workspace](https://github.com/nzig/sway-new-workspace) - create bindings for opening a new workspace, or moving windows to a new workspace
* [swaycons](https://github.com/ActuallyAllie/swaycons) - display window icons with font icons
* [sway-font-awesome](https://github.com/iguanajuice/sway-font-awesome) - Font Awesome icons in sway's title bars.
* [i3-toolwait](https://gitlab.com/wef/dotfiles/-/blob/master/bin/i3-toolwait) - serialise apps - similar to the ancient SunOS command toolwait (was 'sway-toolwait' but now also runs on i3wm)
* [vim-sway-nav](https://jasoncarloscox.com/creations/vim-sway-nav/) - Seamless navigation between Sway windows and (Neo)Vim splits with the same key bindings
* [swaycycle](https://github.com/TLINDEN/swaycycle) - Cycle focus through all visible windows on a sway workspace (floating or not) like you do on traditional window managers or desktop environments
* [sway-descratch](https://github.com/TLINDEN/sway-descratch) - Move windows from scratchpad to current workspace, works interactively with rofi.
* [swayipc](https://github.com/TLINDEN/swayipc) - Golang bindings to sway via IPC communication

## Development
* [gtk-layer-shell](https://github.com/wmww/gtk-layer-shell) - library to write GTK applications that use Layer Shell.
* [client toolkit](https://github.com/Smithay/client-toolkit) - toolkit for writing Wayland clients in Rust
* [swc](https://github.com/michaelforney/swc) - library for making a simple Wayland compositor
* [wlroots](https://github.com/swaywm/wlroots) - Pluggable, composable, unopinionated modules for building a Wayland compositor

## Sources

* https://www.reddit.com/r/swaywm/
* https://arewewaylandyet.com/
* https://github.com/swaywm/sway/wiki/i3-Migration-Guide
* https://github.com/ammgws/letssway
* https://wiki.archlinux.org/index.php/Sway
* https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/wikis/home
* https://github.com/rcalixte/awesome-wayland

## Contributing

If you have improvements, please post to [r/swaywm](https://www.reddit.com/r/swaywm/)

Criteria for inclusion (tentative):

* it's on one of the source lists
* it's mentioned on /r/swaywm
* it's open source ie unencumbered by a restricted licence
* it runs on Linux or BSD
* it adds something to the Sway experience
