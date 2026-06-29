# Hyprland

Hyprland is an independent tiling Wayland compositor written in C++. Noteworthy features of Hyprland include dynamic tiling, tabbed windows, a clean and readable C++ code-base, and a custom renderer that provides window animations, rounded corners, and Dual-Kawase Blur on transparent windows. General usage and configuration is thoroughly documented at Hyprland wiki.

## Installation
Install the  package.

As of #6608, Hyprland uses  as its own rendering backend library. Before that, it bundled its own version of wlroots, which closely followed .

## Configuration
Configuration is done through a single Lua file, typically located at . If the file does not exist, hyprland will automatically generate an example configuration. You can also split your configuration into multiple files and load them using the Lua  function. The default generated configuration can also be found at .

The  file contains directives to configure devices like keyboards and monitors, as well as layout, decoration, and animation settings. You can define window rules, key bindings, and commands to execute at startup.

The configuration is reloaded automatically the moment you save the file. Alternatively, you can reload it manually by executing . For some settings, you may have to restart your Hyprland session.

Settings can also be changed on the fly with hyprctl but they will not be saved.

## Keyboard
## Keymap
By default, Hyprland will use the  layout; you can configure a different layout using the  function:

{{hc|~/.config/hypr/hyprland.lua|2=
-- German Colemak layout
hl.config({
    input = {
        kb_layout = "de",
        kb_variant = "colemak",
    }
})
}}

See the upstream's Wiki for all available options.

## Typematic delay and rate
While Xorg users will be used to having this setting defined at the server level, on Wayland each compositor handles it on its own:

{{hc|~/.config/hypr/hyprland.lua|2=
-- Repeat rate and delay
hl.config({
    input = {
        repeat_rate = 25,
        repeat_delay = 600,
    }
})
}}

## Keyboard backlight
Using keyboard brightness controls in Hyprland is possible. Install  then add the related binds (replace  with ,  or  depending on how your hardware exposes the keyboard backlight):

It is also possible to have on-screen notifications that fire when changes are made.

## Media keys
Using keyboard media controls in Hyprland is possible by making use of  keysyms and an external application like  or  and playerctl:

{{hc|~/.config/hypr/hyprland.lua|2=
-- Volume and Media Control
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("pamixer -i 5"), { repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("pamixer -d 5"), { repeating = true })
hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("pamixer --default-source -m"))
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("pamixer -t"))
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"))
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"))
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"))
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"))
}}

It is also possible to have on-screen notifications that fire when changes are made.

## Touchpad gestures
Being a Wayland compositor, Hyprland has full support for touchpad gestures though they are disabled by default. To enable them, make the following edit using the  function:

{{hc|~/.config/hypr/hyprland.lua|2=
-- Enable touchpad gestures
hl.gesture({
    fingers = 3,
    direction = "horizontal",
    action = "workspace"
})
}}

See the upstream Wiki for all available options.

## Display settings
## Screen sharing
See Screen-sharing.

Being a wlroots-compatible compositor, Hyprland can utilize  to enable screen capture in a range of applications by way of xdg-desktop-portal.

Hyprland also maintains , which supports screen sharing (including region sharing and window sharing), global shortcuts, and has a graphical picker utility. Usage of the portal is further documented in the Hyprland wiki.

It is worth noting that xdg-desktop-portal-hyprland does not include a file picker, for which users can additionally install .

## Setting screen resolution
Hyprland will try to detect your screen resolution automatically and then select either 1x, 1.5x, or 2x screen scaling. However, in some cases it will fail and default to a fail-safe, usually if there are multiple screens present or if you have a hybrid laptop. If everything on your screen is huge then you need to configure your default monitor and resolution.

First find your default monitor using hyprctl:

Then add your monitor to the configuration using the  function:

{{hc|~/.config/hypr/hyprland.lua|2=
-- Monitor details
hl.monitor({
    output = "eDP-1",
    mode = "1920x1080@144",
    position = "0x0",
    scale = 1,
})
}}

 is a position offset used for multi screen setups and the final  is the screen scaling factor.

See the upstream Hyprland Monitors Wiki for more details.

## Settings GUI
There is the  package, a GUI application for monitor arrangement, that supports Hyprland. It is part of the nwg-shell (but works standalone), see nwg-displays github for more details.

## Screen backlight
Install  then add the following binds:

It is also possible to have on-screen notifications that fire when changes are made.

## Autostart
To launch applications or daemons automatically when Hyprland starts, execute commands on the  event:

## Usage
## Starting
## Universal Wayland Session Manager
Universal Wayland Session Manager wraps the compositor and accordingly configured applications and daemons through systemd unit files, allowing you to control them with systemctl.

Hyprland can be started via a Display manager with uwsm by selecting hyprland (uwsm-managed).

You can start Hyprland with uwsm both in a getty via the following script in your login shell:

## Terminal
You can start Hyprland from a getty with the following command:

 $ start-hyprland

## Display managers
While launching from a display manager is not officially supported, users have reported success launching from GDM, SDDM, and others. The upstream wiki maintains a compatibility list with display managers. The  package contains two desktop entries, and all Hyprland AUR packages will generate one automatically.

Both methods provide identical results, plus or minus a few environment variables and services.

## Auto login
Users can automatically login by using a display manager or adapting the method described in Xinit#Autostart X at login.

## hyprctl and IPC
hyprctl is a command line utility that comes installed with Hyprland to communicate with the display server. It allows you to dispatch commands to the server (equivalent to commands in the configuration file, but with a slightly different syntax), set keywords, send queries and request information. See the full documentation.

Hyprland also exposes 2 UNIX Sockets for controlling and getting information about Hyprland via code or command-line utilities. These sockets broadcast events on focus change (windows, workspaces, monitors), creation of windows/workspace, and so on.

Both hyprctl and the IPC sockets can be effectively used in scripts to control Hyprland for complex tasks.

## Autostart
In the Lua configuration, autostarting applications is done by executing commands inside the  event listener.

## Setting environment variables
It is possible to set environment variables directly in  through the  function, which has a different syntax than the env UNIX command used by shells.

The differences are explained on the upstream Wiki.

KDE Frameworks applications such as Dolphin or digiKam may show an empty
Open With menu if  is unset. Set it to match an
installed menu file in , for example:

Use  for  or  for
. Then rebuild the KDE service cache:

## Hypr-Ecosystem
The Hyprland development team are building an ecosystem of applications tailored to be specifically used with Hyprland, these tools will include dispatchers allowing for them to be controlled with  rather than relying on scripts.

Currently the ecosystem consists of:

## Hyprpaper
Hyprpaper is a wallpaper utility; it can be installed with the  package.

## Hyprpicker
Hyprpicker is a utility to grab a colour from a desktop; it can be installed with the  package. It does not require any configuration.

## Hypridle
Hypridle is an idle management daemon; it can be installed with the  package.

## Hyprlock
Hyprlock is a screen lock manager; it can be installed with the  package.

## Hyprcursor
Hyprcursor is a new format for handling screen cursors that offers many improvements over the traditional way; it can be installed with the  package,

## Hyprcursor themes
Cursor themes can be installed from the AUR, for example:

*
*
*
*

Instructions for porting existing themes to Hyprcursor are available on the upstream GitHub repository.

## XDG-Desktop-Portal-Hyprland
Hyprland's own implementation of XDG Desktop Portal. Compatible with other wlroots-based compositors, but provides extra functionality when used on Hyprland. Available through the  package.

## Hyprpolkitagent
Hyprpolkitagent is a polkit authentication daemon.  It can be installed with the  package.

## Hyprsunset
Hyprsunset is a small utility to provide a blue light filter for your system.  It can be installed with the  package.

## Hyprsysteminfo
Hyprsysteminfo is a system information fetching program like  or . It can be installed with the  AUR package.

## Tips and tricks
## File manager
Hyprland requires a wayland-compatible external application if graphical file management is desired. Using  as an example, we simply need to assign it a keybind as follows:

## Application launcher
Hyprland requires a wayland-compatible external application to launch applications. Using  as an example, we simply need to assign it a keybind as follows:

## Idle
Hyprland requires a wayland-compatible external idle management daemon. The most common setup is  and . You can lock your screen manually using a bind as follows:

## Automatic screen locking and suspend
Create the following file:

{{hc|~/.config/hypr/hypridle.conf|2=
general {
    lock_cmd = pidof hyprlock  hyprlock
}

listener {
    timeout = 300
    on-timeout = loginctl lock-session
}

listener {
    timeout = 600
    on-timeout = systemctl suspend
}
}}

Then run it:

## Turning off the screen using DPMS after a timeout period
Hyprland has a built in dispatcher to handle DPMS requests however using it as a direct keybind is not recommended, doing so will result in you not being able to turn the screen back on and will require you to reboot.

Edit the file from above and change it to read:

{{hc|~/.config/hypr/hypridle.conf|2=
general {
    lock_cmd = pidof hyprlock  hyprlock
}

listener {
    timeout = 300
    on-timeout = loginctl lock-session
}

listener {
    timeout = 600
    on-timeout = hyprctl dispatch dpms off
    on-resume = hyprctl dispatch dpms on
}

listener {
    timeout = 900
    on-timeout = systemctl suspend
}
}}

## Status bar
Hyprland requires a wayland-compatible external application to display a status bar. Using  as an example, we simply need to call it as follows:

## Workspace overview
 has a built in, fully customisable module that supports Hyprland workspace switching natively.

See the waybar Wiki for details.

## Polkit authentication
Polkit authentication requires the use of an external authentication agent. Hyprland recommends using  but any should work.

Call it as follows:

## Desktop wallpaper
Hyprland requires a Wayland-compatible external application to manage desktop wallpapers. Using  as an example, we simply need to call it as follows:

Additionally since  requires a configuration file to start; make the file as follows:

{{hc|~/.config/hypr/hyprpaper.conf|2=
wallpaper {
    monitor = monitor
    path = /home/me/amongus.png
    fit_mode = cover
}
}}

Replace monitor with the monitor you would like the wallpaper to be set on, you can grab a list via .  can also be left blank to apply the rule to all monitors.

## Using a script to randomize the wallpaper
Create the following script and make sure it is executable:

Next create a new directory to store wallpapers, something like  should work fine, and populate it with any images you want.

Finally call the script when the specified bind is pressed:

## On screen notifications
On screen notifications for actions like brightness and volume changes are possible by using external notification daemons. This is a very complex topic and covering it completely is beyond the scope of this page. Rather, this section will focus on  so go ahead and install it.

See Desktop notifications for further instructions and Desktop notifications#Standalone for a list of alternatives.

## Mako
Mako is a lightweight notification daemon, you can read  for details. Its configuration file is , icons used for OSD are stored at  and should be in PNG format.

For the rest of this section all the images used by the scripts are available from [https://github.com/SolDoesTech/HyprV4/tree/main/HyprV/mako/icons this GitHub folder.

## Keyboard backlight notifications
First create the following script:

{{hc|~/.config/hypr/scripts/kbbacklight|2=

#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get brightness
get_backlight() {
	LIGHT="$(cat /sys/class/leds/*::kbd_backlight/brightness)"
	echo "${LIGHT}"
}

# Get icons
get_icon() {
	current="$(cat /sys/class/leds/*::kbd_backlight/brightness)"

	if  ("$current" -ge "0") && ("$current" -le "1") ; then
		icon="$iDIR/brightness-20.png"
	elif  ("$current" -ge "1") && ("$current" -le "2") ; then
		icon="$iDIR/brightness-60.png"
	elif  ("$current" -ge "2") && ("$current" -le "3") ; then
		icon="$iDIR/brightness-100.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "Keyboard Brightness : $(brightnessctl -d '*::kbd_backlight' g)"
}

# Increase brightness
inc_backlight() {
	brightnessctl -d *::kbd_backlight set 33%+ && get_icon && notify_user
}

# Decrease brightness
dec_backlight() {
	brightnessctl -d *::kbd_backlight set 33%- && get_icon && notify_user
}

# Zero brightness
zero_backlight() {
	brightnessctl -d *::kbd_backlight s 0%
}

# Full brightness
full_backlight() {
	brightnessctl -d *::kbd_backlight s 100%
}

# Execute accordingly
if  "$1" == "--get" ; then
	brightnessctl -d '*::kbd_backlight' g
elif  "$1" == "--inc" ; then
	inc_backlight
elif  "$1" == "--dec" ; then
	dec_backlight
elif  "$1" == "--zero" ; then
	zero_backlight
elif  "$1" == "--full" ; then
	full_backlight

else
	get_backlight
fi

}}

Then add a new bind, or edit any existing one:

## Media key notifications
First create the following script:

{{hc|~/.config/hypr/scripts/volume|2=
#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get Volume
get_volume() {
	volume=$(pamixer --get-volume)
	echo "$volume"
}

# Get icons
get_icon() {
	current=$(get_volume)
	if  "$current" -eq "0" ; then
		echo "$iDIR/volume-mute.png"
	elif  ("$current" -ge "0") && ("$current" -le "30") ; then
		echo "$iDIR/volume-low.png"
	elif  ("$current" -ge "30") && ("$current" -le "60") ; then
		echo "$iDIR/volume-mid.png"
	elif  ("$current" -ge "60") && ("$current" -le "100") ; then
		echo "$iDIR/volume-high.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_icon)" "Volume : $(get_volume) %"
}

# Increase Volume
inc_volume() {
	pamixer -i 5 && notify_user
}

# Decrease Volume
dec_volume() {
	pamixer -d 5 && notify_user
}

# Toggle Mute
toggle_mute() {
	if [ "$(pamixer --get-mute)" == "false" ]; then
		pamixer -m && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/volume-mute.png" "Volume Switched OFF"
	elif [ "$(pamixer --get-mute)" == "true" ]; then
		pamixer -u && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_icon)" "Volume Switched ON"
	fi
}

# Toggle Mic
toggle_mic() {
	if [ "$(pamixer --default-source --get-mute)" == "false" ]; then
		pamixer --default-source -m && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/microphone-mute.png" "Microphone Switched OFF"
	elif [ "$(pamixer --default-source --get-mute)" == "true" ]; then
		pamixer -u --default-source u && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/microphone.png" "Microphone Switched ON"
	fi
}
# Get icons
get_mic_icon() {
	current=$(pamixer --default-source --get-volume)
	if  "$current" -eq "0" ; then
		echo "$iDIR/microphone.png"
	elif  ("$current" -ge "0") && ("$current" -le "30") ; then
		echo "$iDIR/microphone.png"
	elif  ("$current" -ge "30") && ("$current" -le "60") ; then
		echo "$iDIR/microphone.png"
	elif  ("$current" -ge "60") && ("$current" -le "100") ; then
		echo "$iDIR/microphone.png"
	fi
}
# Notify
notify_mic_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_mic_icon)" "Mic-Level : $(pamixer --default-source --get-volume) %"
}

# Increase MIC Volume
inc_mic_volume() {
	pamixer --default-source -i 5 && notify_mic_user
}

# Decrease MIC Volume
dec_mic_volume() {
	pamixer --default-source -d 5 && notify_mic_user
}

# Execute accordingly
if  "$1" == "--get" ; then
	get_volume
elif  "$1" == "--inc" ; then
	inc_volume
elif  "$1" == "--dec" ; then
	dec_volume
elif  "$1" == "--toggle" ; then
	toggle_mute
elif  "$1" == "--toggle-mic" ; then
	toggle_mic
elif  "$1" == "--get-icon" ; then
	get_icon
elif  "$1" == "--get-mic-icon" ; then
	get_mic_icon
elif  "$1" == "--mic-inc" ; then
	inc_mic_volume
elif  "$1" == "--mic-dec" ; then
	dec_mic_volume
else
	get_volume
fi
}}

Then add the following (or edit any existing binds):

## Screen backlight notifications
First create the following script:

{{hc|~/.config/hypr/scripts/backlight|2=
#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get brightness
get_backlight() {
	LIGHT=$(printf "%.0f\n" $(brightnessctl g))
	echo "${LIGHT}"
}

# Get icons
get_icon() {
	current="$(get_backlight)"
	if  ("$current" -ge "0") && ("$current" -le "19200") ; then
		icon="$iDIR/brightness-20.png"
	elif  ("$current" -ge "19200") && ("$current" -le "38400") ; then
		icon="$iDIR/brightness-40.png"
	elif  ("$current" -ge "38400") && ("$current" -le "57600") ; then
		icon="$iDIR/brightness-60.png"
	elif  ("$current" -ge "57600") && ("$current" -le "76800") ; then
		icon="$iDIR/brightness-80.png"
	elif  ("$current" -ge "76800") && ("$current" -le "96000") ; then
		icon="$iDIR/brightness-100.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "Brightness : $(get_backlight)"
}

# Increase brightness
inc_backlight() {
	brightnessctl s +5% && get_icon && notify_user
}

# Decrease brightness
dec_backlight() {
	brightnessctl s 5%- && get_icon && notify_user
}

# Execute accordingly
if  "$1" == "--get" ; then
	get_backlight
elif  "$1" == "--inc" ; then
	inc_backlight
elif  "$1" == "--dec" ; then
	dec_backlight
else
	get_backlight
fi
}}

Then add the following (or edit any existing binds):

## Keyboard language notifications
To run this script, you need a command-line JSON processor .

First create the following script:

{{hc|~/.config/hypr/scripts/lang|2=
#!/usr/bin/env bash

icon="$HOME/.config/mako/icons/language.png"

# Get language
get_lang() {
	lang=$(hyprctl devices -j | gojq -r '.keyboards| select(.name == "at-translated-set-2-keyboard") | .active_keymap' | cut -c 1-2 | tr 'A-Z' 'a-z')
	case $lang in
		en)
			lang="English language"
			;;
		ru)
			lang="Русский язык"
			;;
		uk)
			lang="Українська мова"
			;;
	esac
	echo $lang
}

# Notify
notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "$(get_lang)"
}}

Then add the following (or edit any existing binds):

{{hc|~/.config/hypr/hyprland.conf|2=
device:at-translated-set-2-keyboard {
    kb_layout = us,ru,ua
    kb_variant = lang
    kb_options = grp:win_space_toggle
}

# Language
bind = SUPER, SPACE, exec, ~/.config/hypr/scripts/lang
}}

## Power control
Hyprland requires a wayland-compatible external application for power control. Using  as an example, we simply need to bind it as follows:

## Clipboard
Wayland clipboard behaviour deletes data when closing the application we copied it from. Other desktop environments work around this by using dedicated clipboard managers and on Hyprland there are multiple compatible choices. See the [https://wiki.hypr.land/Useful-Utilities/Clipboard-Managers/ upstream Wiki for more information.

This section will cover  as it supports copying images as well as text, start by adding the following:

Then create a bind to call the history in your chosen application launcher:

Now pressing  will open up a  window with a clipboard history list.

## Enable/disable devices
To enable/disable devices (e.g. touchpad), first use:
 $ hyprctl devices
to get the name of your device.

Put these lines of code into your configuration file (replace  with the name of your device queried above) to turn the device on/off:

{{hc|~/.config/hypr/hyprland.conf|2=

device {
  name =
  enabled = {true/false}
}

}}

To dynamically switch the device on/off use hyprctl:

 $ hyprctl keyword "device{true|false}

You can also create a keybinding, e.g.:

## Separate dconf profile
In case you do not want to poison settings for other GTK-based DEs, you can use a separate  profile. For example:

Declare new global dconf profile:

Now you can use gsettings and it should not affect other desktop environments.

## KDE Plasma applications not following Qt theming
Even with a Qt theme set, some plasma applications might not follow it. This can be solved by installing  and choosing a KColorScheme or by adding this configuration line in kdeglobals:

## Troubleshooting
## Jetbrains apps focus issues
Jetbrains apps (Pycharm, Intellij) can have strange focus problems such as:

* Unable to drag tab from the tab bar [https://github.com/hyprwm/Hyprland/issues/1120 to either a split, or another tab stack without focus being stolen and the tab being dropped as soon as you drag it past the current tab bar.

* Autocomplete popup window stealing focus until the mouse is moved.

To mitigate the issue add this to hyprlands configuration file:
