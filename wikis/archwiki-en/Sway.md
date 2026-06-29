# Sway

Sway (contracted from SirCmpwn's Wayland compositor is a compositor for Wayland designed to be fully compatible with i3. According to [https://swaywm.org the official website:
:Sway is a tiling Wayland compositor and a drop-in replacement for the i3 window manager for X11. It works with your existing i3 configuration and supports most of i3's features, plus a few extras.

If you are interested in eye-candy,  exists as a fork of sway with popular eye-candy effects.

 is another fork of sway with a scrolling layout like PaperWM or niri. It also supports animations, window content scaling and several overview modes.

## Installation
Sway can be installed with the  package. Always update wlroots when you update sway, due to tight dependencies.

You may also install , , and  to lock your screen, set up an idle manager, and set wallpapers, respectively.

The default application launcher is  and the default terminal emulator is foot. Before starting sway it is advisable to either install them or set a new launcher and terminal in the configuration. For other Wayland-compatible versions of some useful i3 packages you can look at the migration guide on the Sway wiki.

## Starting
Before Sway can be started, it needs access to your hardware devices such as your keyboard, mouse, and graphics card. The collection of these hardware devices is called a seat, as mentioned in 。

On Arch Linux, Sway can get access to your seat using either

*  and , or
* , which will be installed alongside Sway as a dependency of

If  is already installed on your system, Sway should automatically get access to your seat.

Alternatively, if  is not installed on your system and you want to use  instead, add yourself to the  user group and enable/start , then re-log.

You can pick one of the following methods to start Sway.

## Manually
To start Sway, simply type  in the Linux console.

## Automatically on TTY login
Similarly to X, Sway can be started by adding the following to your shell initialization file (see Command-line shell#Login shell):

For more details, see Xinit#Autostart X at login

## From a display manager
The sway session is located at . It is automatically recognized by modern display managers like GDM and SDDM.

It is also possible to start sway as a systemd user service through the display manager.

Also you can use text-based session manager, see Display manager#Console.

## Configuration
If you already use i3, you may copy your i3 configuration to  and it should work out of the box. Otherwise, copy the sample configuration file located at  to . See  for information on the configuration.

## Keymap
By default, sway starts with the US QWERTY keymap. To configure per-input:

{{hc|~/.config/sway/config|
input * {
    xkb_layout "us,de,ru"
    xkb_variant "colemak,,typewriter"
    xkb_options "grp:win_space_toggle"
}

input  xkb_model "pc101"
}}

More details are available in  and .

The keymap can also be configured using environment variables (, , etc.) when starting . The configuration options take precedence over environment variables.

## Typematic delay and rate
To change typematic delay and rate, you can add the following lines to your  section:

## Statusbar
Sway ships with a default status bar in the form of swaybar which runs in a pure Wayland environment. swaybar can call a shell script or other program to show information in the status bar. See  and  for details.

Installing i3status is an option to obtain a practical, default status bar under Wayland. All you have to do is add the following snippet at the end of your sway config:

{{hc|~/.config/sway/config|
bar {
    status_command i3status
}
}}

If you want to enable colored output for i3status, you need to adjust the following part in the i3status configuration:

{{hc|~/.config/i3status/config|2=
general {
    colors = true
    interval = 5
}
}}

## Outputs
The  command in  allows for the detailed configuration of different display outputs. This includes settings for wallpaper, scale factor, position, and more. You can combine multiple output commands into one line, as needed.

Outputs can be specifically addressed by employing their designated output names, by universally matching all outputs with , or through utilizing the distinct names of the displays (a string consisting of the make, model and serial). For example:

You can get a list of output names and additional information using the command:

 $ swaymsg -t get_outputs

For a deeper dive into configurations and additional options, consult .

## Wallpaper
The displaying of a wallpaper in sway is handled by a dedicated program. The simplest example is , which  can manage directly.  must be installed if needed in order to run the  command.

The following line, which can be included anywhere in sway's configuration file, sets a background image on all displays:

Of course  should be replaced with the path to an existing image file.

Solid colors may be set as follows:

 output * bg #000000 solid_color

See the Sway wiki for additional tools and utilities for wallpaper management.

## HiDPI
## Automatic
Sway automatically applies integer scaling by default. If the following conditions hold: * The screen provides valid physical dimension information via EDID.
* Both dimensions have a ratio of  (DPI) of at least 192.
* The screen resolution has a height of at least 1200px.

then Sway will use 2x scaling. Some devices, such as the Framework Laptop 16, have a DPI that is close to (but not quite) 192. In these cases, you may want to manually configure fractional scaling.

## Manual
Set your displays scale factor with the  command in your configuration file. The scale factor can be fractional, but it is usually 2 for HiDPI screens.

You can find your display name with the following command:

 $ swaymsg -t get_outputs

## Tearing
By default, sway will synchronize frame updates (vsync) to make frame-perfect output without tearing, at the cost of latency. But in some cases it is useful to disable vsync to make output more smooth (e.g. video games):

## Input devices
It is possible to tweak specific input device configurations. For example, to enable tap-to-click and natural scrolling for all touchpads:

{{hc|~/.config/sway/config|
input type:touchpad {
    tap enabled
    natural_scroll enabled
}
}}

To set the configuration for a particular touchpad, use  to obtain a device identifier and use it instead of .

More documentation and options like acceleration profiles or disabling input entirely can be found in .

If you use a graphics tablet, see Graphics tablet#Sway.

## Touch display mapping
Touch input targets for touch displays used in a multi-display environment can be mapped to only that touch display.

## Custom keybindings
Special keys on your keyboard can be used to execute commands, for example to control volume, monitor brightness or media players:

For details and alternative utilities, see:

* PulseAudio#Keyboard volume control,
* WirePlumber#Keyboard volume control,
* ALSA#Keyboard volume control,
* Backlight#Backlight utilities,
* MPRIS.

To allow a keybinding to be executed while the lockscreen is active add the  parameter to bindsym.

 bindsym --locked XF86AudioPlay exec playerctl play-pause

## Graphical indicator bars
It is often desirable to have the current level of some percentage-valued setting, such as brightness or volume, be indicated by a graphical bar when it is adjusted. A good option for providing this facility in Sway is  (alternatively ), which provides a subset of the functionality of the popular X tool  but as a native Wayland utility implementing the layer-shell protocol. See the [https://github.com/francma/wob project website for usage examples.

## Overview of workspaces
If you are using a lot of workspaces with a lot of windows and cannot follow what is where any more, then  can come in handy. It is an overlay that shows schemas for all workspaces to make navigation in sway easier. It shows program names, window titles, supports multi-output setup. See the project page for more information.

## Idle
Sway has a dedicated idle management daemon named  to handle idling sessions. There are different ways to start and parameterize the daemon. The simplest is to use the configuration of sway itself.  accepts a multitude of arguments to configure events like  (a.k.a. idling),  (not idle anymore, after a timeout),  etc. See  for more details and further explanations of the events. Each event can then be assigned an action. To assign multiple actions to an event simply repeat the trigger.

The following instructs  to lock the screen after 30 minutes and turn it off five seconds after:

To turn off a locked screen much sooner e.g. after 10 seconds, grep the process list for your locking manager and execute  accordingly like so:

 timeout 10 'if pgrep -x swaylock; then swaymsg "output * power off"; fi' resume 'if pgrep -x swaylock; then swaymsg "output * power on"; fi'

In order to lock the screen before suspending and pause any playing media, append the following instruction to the swayidle command:

 before-sleep 'playerctl pause; swaylock -f'

If you do not want swaylock to trigger while videos are playing in Firefox, Chrome or VLC, you can use  to listen for dbus screensaver inhibit requests and invoke swayidle-inhibit. Programs like Firefox, Chrome and VLC emit these events to prevent the system from going idle.

## Screen content shown briefly upon resume
Using , might cause screen content to be briefly shown upon resume.  To mitigate this, you can let logind to ignore lid events and use sway to handle lid and power button events.

We use  option for suspending the system when the lid is toggled during lock screen. If you are using clamshell mode, you can unset the lid binding with .  is for suspending the computer again during accidental wake-ups.

logind integration is considered buggy and is hard to maintain. See also === Floating windows ===

To enable floating windows or window assignments, open the application and then use the , the , the  and the  attributes to enable floating windows/window assignments. The following command will list the properties of all the open windows.

 $ swaymsg -t get_tree

To get only the 's of all open windows use:

 $ swaymsg -t get_tree | grep "app_id"

To get the  of the focused window use:

 $ swaymsg -t get_tree | jq -r '..|try select(.focused == true)'

X11 windows do not have an  property. However, you can use attributes like , ,  and/or the  to match them. You can search the output of  and create fine grained rules for your windows.

This is similar to using  to find the  or  attributes in X11.

When using multiple monitors, the floating scratchpad window can get too large, covering more than one monitor. This command centers and resizes the floating window to 80% of the current monitor's size:

 $ swaymsg move position center; swaymsg resize set 80ppt 80ppt

## Clipboard
Please see Clipboard#Wayland.

## Xresources
Copy  to  to use them in Sway.

## Xwayland
See Wayland#Xwayland for details and an overview of available packages.

The use of Xwayland is enabled by default.

If you would like to disable Xwayland entirely and run a "pure" Wayland session, set the following to deactivate the use of Xwayland:

If you would like to be able to tell at a glance which windows are using Xwayland, set the following:

## Use another wlroots renderer
To use another renderer such as Vulkan, see Wayland#Use another renderer for wlroots based compositor.

## Autostart
See i3#Autostart, adjusting the configuration file name for sway.

## Tips and tricks
## Activating numlock on startup
By default, sway initially disables the  key on startup. To enable it on startup, set the  input configurations to  for your keyboards. For example, to do so on all keyboards, add the following line to your sway configuration:

In either case, the  keys may be toggled by pressing the relevant keys on a keyboard.

## Current keyboard layout
The current keyboard layout can be retrieved as follows, where  needs to be replaced with your keyboard's identifier:

 $ swaymsg -t get_inputs  jq -r '.[  select(.identifier == "kbd_identifier")  .xkb_active_layout_name'

## Compose key
To set up  as the compose key:

 $ swaymsg 'input * xkb_options compose:prsc'

The available key combinations can be looked up as shown in Xorg/Keyboard configuration#Configuring compose key. The combinations for the compose key can also be configured in the XCompose file. Applications need to be restarted for this change to take effect.

## Backlight toggle
To turn off (and on) your displays with a key (e.g. ) bind the following script in your Sway :

Or you can use the toggle option directly, but you need to specify an output explicitly if you have multiple monitors:

 $ swaymsg "output output_name power toggle"

## Screen capture and screen sharing
See Screen capture#Wayland.

## Color temperature adjustment
See Backlight#Wayland.

## Color profile
It is possible to use a color profile by adding the following line to your config file:

## Control swaynag with the keyboard
Swaynag, the default warning/prompt program shipped with sway, only supports user interaction with the mouse. A helper program such as  may be used to enable interaction via keyboard shortcuts.

Swaynagmode works by first launching swaynag, then listening for signals which trigger actions such as selecting the next button, dismissing the prompt, or accepting the selected button. These signals are sent by launching another instance of the swaynagmode script itself with a control argument, such as  or .

Swaynagmode by default triggers the sway mode  upon initialization, followed by  on exit. This makes it easy to define keybindings in your sway configuration:

{{hc|~/.config/sway/config|
set $nag exec swaynagmode
mode "nag" {
  bindsym {
    Ctrl+d    mode "default"

    Ctrl+c    $nag --exit
    q         $nag --exit
    Escape    $nag --exit

    Return    $nag --confirm

    Tab       $nag --select prev
    Shift+Tab $nag --select next

    Left      $nag --select next
    Right     $nag --select prev

    Up        $nag --select next
    Down      $nag --select prev
  }
}
}}

Note that, beginning in sway version 1.2, mode names are case-sensitive.

You can configure sway to use swaynagmode with the configuration command .

## Change cursor theme and size
To set the cursor theme and size:

Where  can be set to or replaced by a specific value like ,  or , and  a value like .

You can inspect their values with  and .

Note that you need to reload the application to see the changes.

## Manage Sway-specific daemons with systemd
Systemd provides a  which is a user unit which is active whenever any graphical session is running, whether Xorg or Wayland. User services which should run in all graphical environments can be bound to that target. It also allows for a window-manager-specific target to be bound to  to start and stop services which should run only under that window manager. See

Users may want to start some services/daemons (such as  or kanshi) only when the current window manager is Sway, and they may also want these services to stop when Sway stops. Additionally, users who are running  may want to have the services be in separate cgroups so that a single memory-hungry service does not take down the whole Sway session (see the Fedora bug report).

Some or all of this functionality is provided by Arch Sway packages. For example, both  and  provide a  drop-in file (see #Configuration).

If you intend to provide functionality using the roll-your-own method described below or by using a specialist package such as ,  or , you should consider removing files that provide the same functionality.

This functionality can be provided on a roll-your-own basis by creating a  and let those daemons/services wanted by . This systemd target should be a user target (see systemd/User). For example:

Then, add the following line to Sway's configuration file (for example, append the line to , or add a new file to ):

With the above line in the configuration file, whenever Sway starts, it also activates .

Finally, link the desired services to . You can find an example at kanshi#Manage kanshi with systemd.

When the linked user unit is enabled, it is only activated when Sway is running and deactivated when Sway stops.

The creation of the  file and the importing of the environment can also be accomplished by installing . In addition to separating services into cgroups, sway-systemd also places each GUI application in its own cgroup. This enables imposition of per-cgroup resource constraints on individual application. See the sway-systemd README. Alternatively, a more comprehensive solution is provided by .

## Change screen resolution after start
You can use the graphical programs , ,  or the terminal program  to change the resolution, rotate and arrange displays or set the scaling factor.

## Create headless outputs
Create outputs not related to a physical video interface, HEADLESS-1, HEADLESS-2, etc.:

 $ swaymsg create_output

Print a description of the new output:

 $ swaymsg -pt get_outputs | grep -A 10 HEADLESS

Configure the new output with the  command, for example:

{{hc|1=~/.config/sway/config|2=
output HEADLESS-1 {
pos 1920,0
mode 1280x720@75Hz
}
}}

## Change modifier to CapsLock and keep Super
To change the modifier key to  and keep the Super key functional on a US keyboard layout, create  with contents

{{hc|~/.config/xkb/symbols/custom|2=
xkb_symbols "basic" {
    include "us"
    name"English (US Custom)";
    key  { [ Hyper_L  };
    modifier_map Mod4 { Hyper_L };
    key  { [ Super_L ] };
    modifier_map Mod5 { Super_L };
};
}}

For other languages, edit the second and third lines. Then include this keyboard layout in your sway config near the top of the file:

## Access headless Sway session remotely using VNC
The following code can, for example, be run over SSH to start a headless Sway session and access it remotely over VNC.

 is a VNC server for wlroots-based Wayland compositors and can serve a headless Sway session.

Start a headless Sway session by setting  to  and (optionally)  to  (see the FAQ of wayvnc):

 $ WLR_BACKENDS=headless WLR_LIBINPUT_NO_DEVICES=1 sway

Now, run  to serve the VNC server:

 $ WAYLAND_DISPLAY=wayland-1 wayvnc

## Output hotplug hook
If you want to do something when an output is connected or disconnected, look at kanshi.

## Troubleshooting
## Application launchers
 functions relatively well in Sway, but runs under Xwayland and suffers from an issue where it can become unresponsive if the cursor is moved to a native Wayland window. The reason for this issue is that Wayland clients/windows do not have access to input devices unless they have focus of the screen. The Xwayland server is itself a client to the Wayland compositor, so one of its Xwayland clients must have focus for it to access user input. However, once one of its clients has focus, it can gather input and make it available to all Xwayland clients through the X11 protocol. Hence, moving the cursor to an Xwayland window and pressing Escape should fix the issue, and sometimes running  does too.

 is a native Wayland dmenu replacement. Both can optionally be combined with  to provide a Wayland-native combination for launching desktop files (as i3-dmenu-desktop does). For example:

 j4-dmenu-desktop --dmenu='bemenu -i --nb "#3f3f3f" --nf "#dcdccc" --fn "pango:DejaVu Sans Mono 12"' --term='termite'

You may need to set  environment variable to "wayland" if you choose not to disable Xwayland.

You can also build your own with a floating terminal and fzf as discussed in a GitHub issue.

Also  binary provided by  package can serve as launcher, offering both Xwayland and native Wayland support.

 now works in Wayland while still supporting an X11 session.

 is a command launcher, that provides some of the same features as rofi but running under Wayland. wofi lacks some features from rofi like an SSH mode and a window-switching mode. It is based on  library and use GTK3 for rendering. It works pretty well with sway.

 is an application launcher for wlroots based Wayland compositors, similar to rofi's drun mode.

## Virtualization
Sway works with both VirtualBox and VMware ESXi.

For Sway to work in QEMU, QEMU must be started with . See also QEMU#qxl.

## Unable to start Sway from tty
For ESXi, you need to enable 3D support under the Hardware Configuration > Video card settings. See also VMware#Enable 3D graphics on Intel, Optimus and AMD.

## No visible cursor
When using certain graphics drivers (e.g. the VMSVGA graphics controller or the proprietary NVIDIA driver), the cursor is invisible. This can be fixed by using software cursors as discussed in $ export WLR_NO_HARDWARE_CURSORS=1

## Sway socket not detected
Using a  argument, such as , will sometimes return the message:

 sway socket not detected.
 ERROR: Unable to connect to

when run inside a terminal multiplexer (such as GNU Screen or tmux). This means  could not connect to the socket provided in your .

To view what the current value of  is, type:

To work around this problem, you may try attaching to a socket based on the running sway process:

 $ export SWAYSOCK=/run/user/$(id -u)/sway-ipc.$(id -u).$(pgrep -x sway).sock

To avoid this error, run the command outside of a multiplexer.

## Failed to connect to a Wayland server
Tmux creates local environment variables for each session (to see them type: ). Therefore, if you re-attach to a previous tmux session with [https://github.com/tmux-plugins/tmux-resurrect tmux-resurrect or tmux-continuum, or your tmux server runs before sway starts, the environment variables are outdated.

You can use  to instruct tmux to update them whenever you attach to the session by adding the following to your :

 set-option -g update-environment "DISPLAY WAYLAND_DISPLAY SWAYSOCK SSH_AUTH_SOCK"

## Unable to retrieve socket path
Requesting messages from  on a tty may return the following message:

 Unable to retrieve socket path

 environment variable is set after launching Sway, therefore a workaround to this error is to request  in a terminal inside Sway.

## Keybindings and keyboard layouts
By default, if you are using more than one keyboard layout, e.g. , bindings may become broken when you switch on some secondary layout.

Thanks to https://github.com/swaywm/sway/pull/3058, all you need is to add  key to sensitive  lines like this:

{{bc|
bindsym --to-code {
  $mod+$left focus left
  $mod+$down focus down
  $mod+$up focus up
  $mod+$right focus right
}
}}

Alternatively you can create a variable  and then replace all instances of  with  like so:

## Java applications
Some Java-based applications will display blank screen when opened, for example any JetBrains editor such as IntelliJ, CLion, or PyCharm. To mitigate this, the application can be started with the  environment variable set to 1.

If you start the application from a launcher like  or , you might want to modify the application desktop entry as shown in Desktop entries#Modify environment variables.

Some issues with Java applications have been fixed in OpenJDK 11 and Sway 1.5. However, certain applications require additional configuration to use newer versions of OpenJDK, in the case of Android Studio you must set . The JRE has a hardcoded list of known window managers in which Sway is not present. If you experience grey panels, mislocated menus, or improperly resized windows, see Java#Impersonate another window manager.

## Scroll on border
If using the mouse scroll wheel on an application's border crashes sway, you could use  for the  (e.g. Firefox).

## Program cannot open display
If a program crashes on start with the error message "cannot open display", it is likely that the program you are using is an X11 program. You can use the Xwayland compatibility layer to run X11 programs under Wayland, see #Xwayland for details.

## Mouse not working in WINE applications
When running programs, WINE expects a primary monitor to be set, which can cause issues (such as clicks not registering) as Wayland has no concept of a primary monitor. Instead, you can specify a primary monitor for Xwayland to use via xrandr by adding this line to your Sway configuration:

For this to work your display position offset needs to be 0,0 because of a bug [https://github.com/swaywm/sway/issues/6651 in sway.

Note that XWAYLAND0 (or any XWAYLAND display name) may not represent your monitor, and may be susceptible to change in different sessions. Instead, you can specify the first XWAYLAND display using this line instead:

 exec_always xrandr --output $(xrandr | grep -m 1 XWAYLAND | awk '{print $1;}') --primary

You may need to adjust these lines to suit your needs. You can find out which displays are mapped to what names by using the  command with no arguments.

## Flickering in games with NVIDIA GPUs
Although proprietary graphics drivers like NVIDIA are officially not supported, it is possible to use them, even for gaming. If you choose to do so, you may encounter flickering on the upper half of the screen, which can be worked around by replacing  with , or manually compiling your own version with the patch.

## Screencast / WebRTC not working
Make sure to have this in you config:
 include /etc/sway/config.d/*
However, some git packages from the aur don't provide /etc/sway/config.d at all. In that case, add to your config:
 exec dbus-update-activation-environment DISPLAY I3SOCK SWAYSOCK WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=sway
