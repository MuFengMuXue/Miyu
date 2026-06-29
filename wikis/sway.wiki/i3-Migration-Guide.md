Sway is *almost* a drop-in replacement for i3, but you may have to make a few changes to get everything working correctly. Here are a few common ones:

* Use the `output` command to configure outputs instead of xrandr
* Use the `output` command to configure your wallpaper instead of feh
* Use the `input` command to configure input devices
* Replace usage of `i3` specific programs with the equivalent sway tools:
  *  `i3-msg` → `swaymsg`
  * `i3lock` → [`swaylock`](https://github.com/swaywm/swaylock)
  * `i3-nagbar` → `swaynag`
  * `i3bar` → `swaybar`
  * `i3status` → [_Alternative bar content generators_](https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway#bar-content-generators)
* Sway handles quotes slightly differently - commands are handled more like shell commands
* To emulate `xset dpms force off`, use `swayidle timeout 600 'swaymsg "output * dpms off"' resume 'swaymsg "output * dpms on"'` then run `pkill -USR1 swayidle` to trigger timeout immediately.

## Font configuration

Sway does not support X logical font description (XLFD) configuration strings. Instead it uses Pango, and one can use `pango-list | grep [fontname]` to confirm the correct font name. Pango, [as of version 1.44](https://github.com/swaywm/sway/issues/4390), does not support older bitmap fonts (BFD), although it does support bitmap-only OTF fonts.

## Common X11 apps used on i3 with Wayland alternatives

 * xbacklight (backlight management) → [brightnessctl](https://github.com/Hummer12007/brightnessctl/)
 * dunst (notification daemon) → [dunst (supports wayland)](https://github.com/dunst-project/dunst#make-parameters) / [mako](https://github.com/emersion/mako) / [fnott](https://codeberg.org/dnkl/fnott) / [swaync](https://github.com/ErikReider/SwayNotificationCenter)
 * feh (wallpaper setting) → sway output configuration, see `man 5 sway-output` (or ~[oguri](https://github.com/vilhalmer/oguri)~ [swww](https://github.com/Horus645/swww), which supports animated wallpapers), [wbg](https://codeberg.org/dnkl/wbg)
 * scrot (screenshot) → [grim](https://github.com/emersion/grim) + [slurp](https://github.com/emersion/slurp) (or [grimshot](https://github.com/OctopusET/sway-contrib), which wraps around both).
 * picom / compton / xcompmgr (compositor) → built in
 * unclutter (hiding cursor after some time) → `seat <name> hide_cursor <timeout>`
 * xbanish (hiding cursor on keypress) → `seat <name> hide_cursor when-typing enable`
 * xclip / xsel (clipboard copy/paste) → [wl-clipboard](https://github.com/bugaevc/wl-clipboard), [wlsnarf](https://codeberg.org/notchoc/wlsnarf) [wl-clipboard-rs](https://github.com/YaLTeR/wl-clipboard-rs), [wayclip](https://github.com/noocsharp/wayclip)
 * clipster / etc. (clipboard manager) → [cliphist](https://github.com/sentriz/cliphist), [wl-clipboard-history](https://github.com/janza/wl-clipboard-history)
 * xdotool → [wtype](https://github.com/atx/wtype), [wlrctl](https://git.sr.ht/~brocellous/wlrctl), `swaymsg seat <seat> cursor …`, [dotool](https://git.sr.ht/~geb/dotool), [ydotool](https://github.com/ReimuNotMoe/ydotool)
 * xrandr → `swaymsg output …`, [wlr-randr](https://sr.ht/~emersion/wlr-randr/)
 * arandr (GUI to configure outputs) → [wdisplays](https://github.com/artizirk/wdisplays)
 * autorandr → [kanshi](https://sr.ht/~emersion/kanshi/)
 * screenkey (screencast tool to display your keys) → [wshowkeys](https://git.sr.ht/~sircmpwn/wshowkeys), [showmethekey](https://github.com/AlynxZhou/showmethekey/)
 * X11 forwarding → [waypipe](https://gitlab.freedesktop.org/mstoeckl/waypipe/)
 * xev → [wev](https://git.sr.ht/~sircmpwn/wev/)
 * xmodmap → [custom keymap file](https://github.com/swaywm/sway/issues/4250), [interception-tools](https://gitlab.com/interception/linux/tools)
 * xprop → [wlprop](https://gist.github.com/crispyricepc/f313386043395ff06570e02af2d9a8e0#file-wlprop-sh)
 * [xob](https://github.com/florentc/xob) → [wob](https://github.com/francma/wob)
 * [dmenu](https://tools.suckless.org/dmenu/) → [wmenu](https://codeberg.org/adnano/wmenu), [mew](https://codeberg.org/sewn/mew), [bemenu](https://github.com/Cloudef/bemenu), [fuzzel](https://codeberg.org/dnkl/fuzzel), [gmenu](https://code.rocketnine.space/tslocum/gmenu), [wldash](https://github.com/kennylevinsen/wldash)
   * [bemenu](https://github.com/Cloudef/bemenu): To use the same color scheme used in dmenu, use `bemenu-run -p "" --tb "#285577" --hb "#285577" --tf "#eeeeee" --hf "#eeeeee" --nf "#bbbbbb"`
 * [rofi](https://github.com/davatorium/rofi) → [wofi](https://hg.sr.ht/~scoopta/wofi), [rofi patch](https://github.com/davatorium/rofi/pull/1139)
 * ffmpeg x11grab (screen recorder) → [wf-recorder](https://github.com/ammen99/wf-recorder), [txproto](https://github.com/cyanreg/txproto)
 * VNC → [wayvnc](https://github.com/any1/wayvnc)
 * [Redshift](https://github.com/jonls/redshift) → [gammastep](https://gitlab.com/chinstrap/gammastep), [wlsunset](https://git.sr.ht/~kennylevinsen/wlsunset)
 * [slock](https://git.suckless.org/slock/) → [waylock](https://codeberg.org/ifreund/waylock), [wlock](https://codeberg.org/sewn/wlock)
 * [kbdd](https://github.com/qnikst/kbdd) (per-window keyboard layout) → [swaykbdd](https://github.com/artemsen/swaykbdd)
 * [sxhkd](https://github.com/baskerville/sxhkd) (an X daemon that reacts to input events by executing commands), [shkd](https://github.com/baskerville/shkd) (a simple hotkey daemon for the Linux console. ) → [swhkd](https://github.com/waycrate/swhkd)
 * [synergy](https://github.com/symless/synergy-core) (client) → [waynergy](https://github.com/r-c-f/waynergy)
 * [(n)sxiv](https://codeberg.org/nsxiv/nsxiv) (image viewer) → [imv](https://sr.ht/~exec64/imv/)

## X11 Input configuration alternatives

### `xset s off; xset dpms 0 0 0`

Aren't needed because sway doesn't put your monitor into standby by default. But `swayidle` can be used if you want to.

### `xset m 0 0`

Replace with:

```
input "type:pointer" {
  accel_profile flat
  pointer_accel 0
}
```

### `xset r rate 300 50`

Replace with:

```
input "type:keyboard" {
  repeat_delay 300
  repeat_rate  50
}
```

### `xset b off` 

Not supported by sway.

### `setxkbmap -option terminate:ctrl_alt_bksp,caps:super,altwin:menu_win`

Replace with:

```
input "type:keyboard" {
  xkb_options terminate:ctrl_alt_bksp,caps:super,altwin:menu_win
}
```

### Caps Lock as $mod

Some i3 users use `xcape -e 'Super_L=Escape'` so that when Caps Lock is pressed by itself, it acts as Escape. They then remap Caps Lock to Super with `setxkbmap -option caps:super` and use `set $mod Mod4` in i3's config file to set Super as the main modifier.

The idea is that when Caps Lock is pressed by itself, it acts as Escape, which is handy in programs like Vim for returning from Insert mode to Normal mode. When Caps Lock is pressed with another key, it acts like the Super key, so you can switch between desktops by pressing Caps+1, Caps+2, Caps+3, and so on. It's more convenient than pressing Super + number keys because you can do it with one hand. 

To replicate this setup, add the following to `~/.config/sway/config`:

```
set $mod Escape # main modifier variable used in bindsym commands
floating_modifier Mod4 # to avoid config parse error
…
input "type:keyboard" {
    …
    xkb_options caps:escape,…
}
```

## See Also

 * [FAQ](https://github.com/swaywm/sway/wiki)
 * [Differences from i3](https://github.com/swaywm/sway/wiki/Differences-from-i3)
 * The man pages (start with `man sway`)