# Touchpad Synaptics

This article details the installation and configuration process of the Synaptics input driver for Synaptics (and ALPS) touchpads found on most notebooks.

## Installation
The Synaptics driver can be installed with the package .

## Configuration
The primary method of configuration for the touchpad is through an Xorg server configuration file. After installing xf86-input-synaptics, a default configuration file is located at . Users can copy this file to  and edit it to configure the various driver options available. Refer to the  manual page for a complete list of available options. Machine-specific options can be discovered using #Synclient.

## Frequently used options
The following example file configures some common options, including vertical, horizontal and circular scrolling as well as tap-to-click:

; TapButton1: (integer) configures which mouse-button is reported on a non-corner, one finger tap.
; TapButton2: (integer) configures which mouse-button is reported on a non-corner, two finger tap
; TapButton3: (integer) configures which mouse-button is reported on a non-corner, three finger tap
; RBCornerButton: (integer) configures which mouse-button is reported on a right bottom corner, one finger tap (use  to achieve Ubuntu style tap behaviour for right mouse button in lower right corner)
; RTCornerButton: (integer) as above, but for top right corner, one finger tap.
; VertEdgeScroll: (boolean) enables vertical scrolling while dragging across the right edge of the touch pad.
; HorizEdgeScroll: (boolean) enables horizontal scrolling while dragging across the bottom edge of the touch pad.
; VertTwoFingerScroll: (boolean) enables vertical scrolling using two fingers.
; HorizTwoFingerScroll: (boolean) enables horizontal scrolling using two fingers.
; EmulateTwoFingerMinZ/W: (integer) play with this value to set the precision of two finger scroll.
; FingerLow: (integer) when finger pressure drops below this value, the driver counts it as a release.
; FingerHigh: (integer) when finger pressure goes above this value, the driver counts it as a touch.
; MaxTapTime: Determines how "crisp" a tap must be to be considered a real tap. Decrease the value to require a more crisp tap. Properly adjusting this parameter can reduce false positives when the hands hover over or lightly touch the pad.
; VertScrollDelta and HorizScrollDelta: (integer) configures the speed of scrolling, it is a bit counter-intuitive because higher values produce greater precision and thus slower scrolling. Negative values cause natural scrolling like in macOS.

## Configuration on the fly
Next to the traditional method of configuration, the Synaptics driver also supports on the fly configuration. This means that users can set certain options through a software application, these options are applied immediately without needing to restart Xorg. This is useful to test configuration options before you include them in the configuration file or a script. Note that on the fly configuration is not persistent and lasts only until the Xorg server exists.

## Console tools
*
*

## Graphical tools
*
*

## Xfce
To change these settings in Xfce:

# Open System Settings.
# Click Mouse and Touchpad.
# Change the settings on the Touchpad tab.

## Cinnamon
To change these settings in Cinnamon:

# Open Cinnamon System Settings.
# Click Mouse and Touchpad.
# Change the settings on the Touchpad tab.

## MATE
It is possible to configure the way MATE handles the touchpad:

# Run .
# Edit the keys in the  folder.

To prevent Mate settings daemon from overriding existing settings, do as follows:

# Run .
# Edit .
# Uncheck the active setting.

## Advanced configuration
## Using xinput to determine touchpad capabilities
Depending on your model, synaptic touchpads may have or lack capabilities. We can determine which capabilities your hardware supports by using .

* left, middle and right hardware buttons
* two finger detection
* three finger detection
* configurable resolution

First, find the name of your touchpad:

 $ xinput list

You can now use xinput to find your touchpad's capabilities:

From left to right, this shows:

* : device has a physical left button
* : device does not have a physical middle button
* : device has a physical right button
* : device does not support two-finger detection
* : device does not support three-finger detection
* : device can configure vertical resolution
* : device can configure horizontal resolution

Use  to list all device properties. See  for full documentation of the Synaptics properties.

## Synclient
Synclient can configure every option available to the user as documented in . A full list of the current user settings can be brought up:

 $ synclient -l

Every listed configuration option can be controlled through synclient, for example:

* Enable palm detection:
:
* Configure button events (right button event for two finger tap here):
:
* Disable the touchpad:
:

After you have successfully tried and tested your options through synclient, you can make these changes permanent by adding them to .

## evtest
The tool  can display pressure and placement on the touchpad in real-time, allowing further refinement of the default Synaptics settings. The evtest monitoring can be started with:

 $ evtest /dev/input/eventX

X denotes the touchpad's ID. It can be found by looking at the output of  in the row containing "H:" below your touchpad name.

evtest needs exclusive access to the device which means it cannot be run together with an X server instance. You can either kill the X server or run evtest from a different virtual terminal (e.g., by pressing ).

## xev
The tool  can display taps, clicks, pressure, placement and other measured parameters in real-time, allowing still further refinement of the default Synaptics settings. xev can be run in X and needs no specifics. using the  parameter, it is possible to restrict the types of events that are reported.

## Circular scrolling
Circular scrolling is a feature that Synaptics offers which closely resembles the behaviour of iPods. Instead of (or additional to) scrolling horizontally or vertically, you can scroll circularly. Some users find this faster and more precise. To enable circular scrolling, add the following options to the touchpad device section of :

The option  may be one of the following values, determining which edge circular scrolling should start:

 0    All Edges
 1    Top Edge
 2    Top Right Corner
 3    Right Edge
 4    Bottom Right Corner
 5    Bottom Edge
 6    Bottom Left Corner
 7    Left Edge
 8    Top Left Corner

Specifying something different from zero may be useful if you want to use circular scrolling in conjunction with horizontal and/or vertical scrolling. If you do so, the type of scrolling is determined by the edge you start from.

To scroll fast, draw small circles in the center of your touchpad. To scroll slowly and more precise, draw large circles.

## Natural scrolling
It is possible to enable natural scrolling through Synaptics. Simply use negative values for  and  like so:

## Software toggle
You might want to turn the touchpad on and off with a simple button click or shortcut. This can be done by binding the following xinput-based script:

{{hc|/usr/local/bin/touchpad_toggle.sh|2=
#!/bin/bash

declare -i ID
ID=$(xinput list  grep -Eio '(touchpadglidepoint)\s*id=grep -Eo '[0-9{1,2}')
declare -i STATE
STATE=$(xinput list-props "$ID"  grep 'Device Enabled'  awk '{print $4}')
if [ "$STATE" -eq 1 ]
then
    xinput disable "$ID"
    # echo "Touchpad disabled."
    # notify-send -a 'Touchpad' 'Touchpad Disabled' -i input-touchpad
else
    xinput enable "$ID"
    # echo "Touchpad enabled."
    # notify-send -a 'Touchpad' 'Touchpad Enabled' -i input-touchpad
fi
}}

Alternatively, synclient can be used to toggle the touchpad. However, it can only turn off touch events but not physical clickpad button usage:

## Disable touchpad while typing
## Using the driver's automatic palm detection
First of all you should test if it works properly for your touchpad and if the settings are accurate. Enable palm detection with

 $ synclient PalmDetect=1

Then test the typing. You can tweak the detection by setting the minimum width for the touch to be considered a palm, for example:

 $ synclient PalmMinWidth=8

And you can tweak the minimum pressure required for the touch to be considered a palm, for example:

 $ synclient PalmMinZ=100

Once you have found the correct settings, you can add them to your config file:

 Option "PalmDetect" "1"
 Option "PalmMinWidth" "8"
 Option "PalmMinZ" "100"

## Using syndaemon
 monitors keyboard activity and disables the touchpad while typing. It has several options to control when the disabling occurs. View them with

 $ syndaemon -?

For example, to disable tapping and scrolling for 0.5 seconds after each keypress (ignoring modifier keys like ), use

 $ syndaemon -i 0.5 -t -K -R

Once you have determined the options you like, you should use your login manager or xinitrc to have it run automatically when X starts. The  option will make it start in the background as a daemon.

## Disable touchpad on mouse detection
With the assistance of udev, it is possible to automatically disable the touchpad if an external mouse has been plugged in. To achieve this, use one of the following rules.

## Basic desktop
This is a basic rule generally for non-"desktop environment" sessions:

{{hc|/etc/udev/rules.d/01-touchpad.rules|2=
SUBSYSTEM=="input", KERNEL=="mouseACTION=="add", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/username/.Xauthority", RUN+="/usr/bin/synclient TouchpadOff=1"
SUBSYSTEM=="input", KERNEL=="mouse[0-9*", ACTION=="remove", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/username/.Xauthority", RUN+="/usr/bin/synclient TouchpadOff=0"
}}

If the touchpad is always deactivated at startup, even when no mouse is plugged in, try adding the following criteria between the  and  parameters above:

 ATTRS{name}!="*TouchPad", ATTRS{name}!="*Stick",

## GDM
GDM stores the Xauthority files in  in a randomly-named directory. You should find your actual path to the Xauthority file which can be done using . For some reason, multiple authority files may appear for a user, so a rule like this will be necessary:

{{hc|/etc/udev/rules.d/01-touchpad.rules|2=
SUBSYSTEM=="input", KERNEL=="mouseACTION=="add", PROGRAM="/usr/bin/find /var/run/gdm -name username -print0 -quit", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="$result/database", RUN+="/usr/bin/synclient TouchpadOff=1"
SUBSYSTEM=="input", KERNEL=="mouse[0-9", ACTION=="remove", PROGRAM="/usr/bin/find /var/run/gdm -name username -print0 -quit", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="$result/database", RUN+="/usr/bin/synclient TouchpadOff=0"
}}

Furthermore, you should validate that your udev script is running properly. You can check for the conditions by running  with root privileges.

## With syndaemon running
syndaemon whether started by the user or the desktop environment can conflict with synclient and will need to be disabled. A rule like this will be needed:

{{hc|/etc/udev/rules.d/01-touchpad.rules|2=
SUBSYSTEM=="input", KERNEL=="mouseACTION=="add", PROGRAM="/usr/bin/find /var/run/gdm -name username -print -quit", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="$result/database", RUN+="/bin/sh -c '/usr/bin/synclient TouchpadOff=1 ; sleep 1; /bin/killall syndaemon; '"
}}

## touchpad-state
A  package created around the udev rules in #With syndaemon running is available. It includes a udev rule and script:

 touchpad-state [--off ==== GNOME ====

GNOME users can install the GNOME shell extension [https://extensions.gnome.org/extension/131/touchpad-indicator/ Touchpad Indicator, change Switch Method to Synclient and enable Automatically switch Touchpad On/Off in its preferences.

## KDE
If using Plasma, the  package can be used to manage the touchpad.

## System with multiple X sessions
For an environment where multiple users are present, a slightly different approach is needed to detect the current users X environment. This script will help achieving this:

{{hc|/usr/bin/mouse-pnp-event-handler.sh|2=
#!/bin/sh
## $1 = "add" / "remove"
## $2 = %k from udev

## Set TRACKPAD_NAME according to your configuration.
## Check your trackpad name with:
## find /sys/class/input/ -name mouse* -exec udevadm info -a {} \;  grep 'ATTRS{name}'
TRACKPAD_NAME="SynPS/2 Synaptics TouchPad"

USERLIST=$(w -h  cut -d' ' -f1  sort  uniq)
MOUSELIST=$(find /sys/class/input/ -name mouse*)

for CUR_USER in ${USERLIST}; do
        CUR_USER_XAUTH="$(sudo -Hiu ${CUR_USER} env  grep -e "^HOME="  cut -d'=' -f2)/.Xauthority"

        ## Can't find a way to get another users DISPLAY variable from an isolated root environment. Have to set it manually.
        #CUR_USER_DISPL="$(sudo -Hiu ${CUR_USER} env  grep -e "^DISPLAY="  cut -d'=' -f2)"
        CUR_USER_DISPL=":0"

        export XAUTHORITY="${CUR_USER_XAUTH}"
        export DISPLAY="${CUR_USER_DISPL}"

        if [ -f "${CUR_USER_XAUTH}" ]; then
                case "$1" in
                        "add")
                                /usr/bin/synclient TouchpadOff=1
                                /usr/bin/logger "USB mouse plugged. Disabling touchpad for $CUR_USER. ($XAUTHORITY - $DISPLAY)"
                        ;;
                        "remove")
                                ## Only execute synclient if there are no external USB mice connected to the system.
                                EXT_MOUSE_FOUND="0"
                                for CUR_MOUSE in ${MOUSELIST}; do
                                        if [ "$(cat ${CUR_MOUSE}/device/name)" != "${TRACKPAD_NAME}" ]; then
                                                EXT_MOUSE_FOUND="1"
                                        fi
                                done
                                if [ "${EXT_MOUSE_FOUND}" == "0" ]; then
                                        /usr/bin/synclient TouchpadOff=0
                                        /usr/bin/logger "No additional external mice found. Enabling touchpad for $CUR_USER."
                                else
                                        logger "Additional external mice found. Won't enable touchpad yet for $CUR_USER."
                                fi
                        ;;
                esac
        fi
done
}}

Update the  variable for your system configuration. Run {{ic|find /sys/class/input/ -name mouse* -exec udevadm info -a {} \;  grep 'ATTRS{name}'}} to get a list of useful mice-names. Choose the one for your trackpad.

Then have udev run this script when USB mices are plugged in or out, with these udev rules:

## Buttonless touchpads (aka ClickPads)
Ever more laptops have a special kind of touchpad which has a single mouse button as part of the tracking plate, instead of external buttons. For example, the 2015 Dell XPS 13, HP series 4500 ProBooks, ThinkPad X220 and X1 ThinkPad series have this kind of a touchpad. By default, the whole button area is detected as a left button, so right and middle-click functions and click + drag will not work. It is possible to define two and three finger clicks as right and middle button clicks, and/or to define parts of the click pad surface as right and middle buttons. Note that although the driver registers multiple touches, it does not track individual fingers (as of version 1.7.1) which results in confusing behavior when using physical buttons of a clickpad for drag-and-drop and other gestures: you have to click with two or three fingers but then only move one of them while holding the button down with another. You can look into the  driver for better multitouch support.

Some desktop environments (KDE and GNOME at least) define sane and useful default configurations for clickpads, providing a right button at the bottom right of the pad, recognising two and three-finger clicks anywhere on the pad as right and middle clicks, and providing configuration options to define two and three-finger taps as right and middle clicks. If your desktop does not do this, or if you want more control, you can modify the touchpad section in  (or better, of your custom synaptics configuration file prefixed with a higher number). For example:

The format for the  option is (from ):

The above  option is commonly found in documentation or synaptics packages, and it defines the right half of the bottom 18% of the touchpad as a right button. There is no middle button defined. If you want to define a middle button remember one key piece of information from the manual; edge set to 0 extends to infinity in that direction.

In the following example the right button will occupy the rightmost 40% of the button area and the middle button 20% of it in the center. The leftmost 40% remains as a left button (as does the rest of the clickpad):

 ...
 Option     "SoftButtonAreas"  "60% 0 82% 0 40% 59% 82% 0"
 ...

You can use synclient to check the soft button areas:

If your buttons are not working, soft button areas are not changing, ensure you do not have a synaptics configuration file distributed by a package which is overriding your custom settings (i.e. some AUR packages distribute configurations prefixed with very high numbers).

These settings cannot be modified on the fly with synclient, however, xinput works:

 xinput set-prop "SynPS/2 Synaptics TouchPad" "Synaptics Soft Button Areas" 4000 0 4063 0 3000 4000 4063 0

You cannot use percentages with this command, so look at  to figure out the touchpad x and y-axis ranges.

## Bottom edge correction
In some cases, for example Toshiba Satellite P50, everything work out of the box except often your click are seen as mouse movement and the cursor will jump away just before registering the click. This can be easily solved running

 $ synclient -l | grep BottomEdge

take the BottomEdge value and subtract a the wanted height of your button, then temporary apply with

 $ synclient AreaBottomEdge=4000

when a good value has been found make it a fixed correction with

## Troubleshooting
## Touchpad does not work after resuming from hibernate/suspend
Occasionally touchpads will fail to work when the computer resumes from sleep or hibernation. This can often be corrected without rebooting by

* Switching to a console and back again,
* entering sleep mode again, and resuming again,
* locating the correct kernel module, then removing it and inserting it again, possibly with a specific parameter (e.g. ),
* blacklisting kernel module  may be a permanent option (when the touchpad is handled by another module, e.g. ),
* adding the  kernel parameter solves the issue permanently.

If you are using a laptop computer and your touchpad does not work after switching the laptop's lid, you can just change your power management policy: when closing the lid, 'shutdown the screen' instead of 'suspend'(or 'hibernate'). This is useful for some laptops.

## xorg.conf.d/70-synaptics.conf does not seem to apply in MATE
MATE will by default overwrite various options for your touchpad. This includes configurable features for which there is no graphical configuration within MATE's system control panel. This may cause it to appear that  is not applied. Follow #MATE to prevent this behavior.

## The touchpad is not working, Xorg.0.log shows "Query no Synaptics: 6003C8"
Due to the way Synaptics is currently set-up, 2 instances of the Synaptics module are loaded. We can recognize this situation by opening the xorg log file () and noticing this:

Notice how 2 differently named instances of the module are being loaded. In some cases, this causes the touchpad to become nonfunctional.

We can prevent this double loading by adding  to our  file:

Restart X and check xorg logs again, the error should be gone and the touchpad should be functional.

related bugreport:

related forum topics:

* https://bbs.archlinux.org/viewtopic.php?id=104769
* https://bbs.archlinux.org/viewtopic.php?pid=825690

## Touchpad detected as "PS/2 Generic Mouse" or "Logitech PS/2 mouse"
This can be caused by a number of issues;

## Laptops with touchscreen & touchpad
There also seems to be a problem with laptops which have both a touchscreen & a touchpad, such as the Dell XPS 12 or Dell XPS 13. To fix this, you can blacklist the  driver, this does have the side-effect of disabling the touchscreen though.

This seems to be a known problem. Also see this thread.

Post kernel 3.15, having the module blacklisted may cause touchpad to stop working completely. Removing the blacklist should allow this to start working with limited functionality, see .

## Non-functional Synaptics special abilities (multi-tap, scrolling, etc.)
In some cases, Synaptics touchpads only work partially. Features like two-finger scrolling or two-finger middle-click do not work even if properly enabled. This is probably related to the touchpad is not working problem mentioned above. Fix is the same, prevent double module loading.

If preventing the module from loading twice does not solve your issue, try commenting out the toggle  (which is now included by default in the Synaptics configuration).

## No Multi-touch in some Elantech touchpads
See https://unix.stackexchange.com/questions/28736/what-does-the-i8042-nomux-1-kernel-option-do-during-booting-of-ubuntu.

## Cursor jump
Some users have their cursor inexplicably jump around the screen. There currently no patch for this, but the developers are aware of the problem and are working on it.

Another possibility is that you are experiencing IRQ losses related to the i8042 controller (this device handles the keyboard and the touchpad of many laptops), so you have two possibilities here:

#  the  module.
# Append  to your kernel parameters and reboot your machine.

## Touchpad device is not located at /dev/input/*
If that is the case, you can use this command to display information about your input devices:

 $ cat /proc/bus/input/devices

Search for an input device which has the name "SynPS/2 Synaptics TouchPad". The "Handlers" section of the output specifies what device you need to specify.

Example output:

In this case, the  are  and , so  would be used.

## Firefox and special touchpad events
You can enable/disable some special events that Firefox handles upon tapping or scrolling certain parts of your touchpad by editing the settings of those actions. Type  in your Firefox address bar. To alter options, double-click on the line in question.

## Firefox 17.0 and later
Horizontal scrolling will now by default scroll through pages and not through your history. To reenable Mac-style forward/backward with two-finger swiping, edit:

 mousewheel.default.action.override_x = 2

You may encounter accidental forwards/backwards while scrolling vertically. To change Firefox's sensitivity to horizontal swipes, edit:

 mousewheel.default.delta_multiplier_x

The optimum value will depend on your touchpad and how you use it, try starting with . A negative value will reverse the swipe directions.

## Scrolling and multiple actions with Synaptics on LG laptops
These problems seem to be occurring on several models of LG laptops. Symptoms include: when pressing Mouse Button 1, Synaptics interprets it as ScrollUP and a regular button 1 click; same goes for button 2.

The scrolling issue can be resolved by entering in :

Apparently, when trying to compile this against the latest version of Synaptics it fails. The solution to this is using the Git repository for Synaptics To build the package after downloading the tarball and unpacking it, execute:

 $ cd synaptics-git
 $ makepkg

## Other external mouse issues
First, make sure your section describing the external mouse contains this line (or that the line looks like this):

If the  line is different, change it to the above and try to restart X. If this does not solve your problem, make your touchpad the  in the "Server Layout" section:

and make your external device :

Finally, add this to your external device's section:

If all of the above does not work for you, please check relevant bug trackers for possible bugs, or go through the forums to see if anyone has found a better solution.

## Synaptics loses multitouch detection after rebooting from Windows
Many drivers include a firmware that is loaded into flash memory when the computer boots. This firmware is not necessarily cleared upon shutdown, and is not always compatible with Linux drivers. The only way to clear the flash memory is to shutdown completely rather than using reboot. It is generally considered best practice to never use reboot when switching between operating systems.

## Touchpad not recognized after shutdown
Certain touchpads (Elantech in particular) will fail to be recognized as a device of any sort after a standard shutdown. There are multiple possible solutions to this problem:

* Boot into a Windows partition/install disk and shutdown from there.
* Wait approximately 1 minute before turning on the computer after shutdown.
* As discussed in https://bugzilla.kernel.org/show_bug.cgi?id=81331#c186, a patch has been merged into the stable kernel that provides a fix for Elantech touchpads. Gigabyte P34, P35v2 and X3 models are supported by default. For others (especially rebranded Gigabyte laptops, like XMG's),  can be set as kernel parameter.

## Trackpoint and Clickpad
Newer Thinkpads do not have physical buttons for their Trackpoint anymore and instead use the upper area of the Clickpad for buttons (Left, Middle, Right). Apart from the ergonomic viewpoint this works quite well with current Xorg. Unfortunately, mouse wheel emulation using the middle button is not supported yet. Install  for a patched and properly configured version if you intend to use the Trackpoint.
