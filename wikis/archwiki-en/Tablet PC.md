# Tablet PC

This article aggregates information to get Arch Linux working on a tablet PC. The instructions contain information for getting the touch keyboard, stylus, stylus rotation, and screen rotation to work properly on such devices.

## Stylus
Install .

## On-screen keyboards
See List of applications/Utilities#On-screen keyboards.

## With GNOME
Depending on your device, the default GNOME screen keyboard will work automatically when you tap on text input fields. If "Tablet Mode" detection is not working on your device (mutter issue), you might want to customize Gnome Settings > Accessibility.

Enabling Screen keyboard will allow it to always display when a text input field becomes focused.

Always Show Accessibility Menu will allow you to manually enable or disable this depending on your needs.

## Rotation
## Screen rotation
The following sections show generic solutions, desktop environments or Wayland compositors may offer configuration options for these, sometimes through a graphical interface.

## TTY
Use the following kernel parameterfbcon=rotate:1

## Wayland
Use the following kernel parameter, as detailed in Kernel mode setting#Forcing modes:

 video=DSI-1:panel_orientation=right_side_up

## Xorg
The simplest way is to use :

 $ xrandr --orientation left

On some drivers, this messes-up the DPI: the fonts become unreadable.
The  option is quite old. Using  solves the issue, but we need to specify the  option first:

 $ xrandr --output eDP --rotate left

## Touchscreen and stylus rotation
## With xinput
You can use xinput to turn the stylus, like you would rotate a touchscreen.

To set the stylus input to portrait mode:

 $ xinput set-prop name_of_stylus_or_touch_screen --type=float "Coordinate Transformation Matrix"  0 -1 1 1 0 0 0 0 1

To return to landscape mode:

 $ xinput set-prop name_of_stylus_or_touch_screen --type=float "Coordinate Transformation Matrix"  0  0 0 0 0 0 0 0 0

If your stylus is only listed as keyboard:

Touch the screen with the pen:

Using the now listed pointer, the commands should work as expected, turning the stylus.

## With xsetwacom
If not done yet and in analogy to graphics tablet, an approach to get also the inputs of the touch panel rotated is to install the  Xorg driver just as suggested above. After doing so there are various commands available how to manipulate and manage the inputs of the touch panel.

To set the stylus input to portrait mode:

 $ xsetwacom set stylus Rotate cw

To return to landscape mode:

 $ xsetwacom set stylus Rotate none

In case the device 'stylus' cannot be found, use:

 $ xsetwacom list devices

to get a list of devices.

For example:

 xsetwacom set "Wacom Co.,Ltd. Pen and multitouch sensor Pen stylus" Rotate cw

Source: https://xournal.sourceforge.net/manual.html

If you still cannot change the rotation, you can try to use xinput.

## Automatic rotation
## With Xorg
A simple Xorg auto-rotate script could be implemented as follows (uses ,  and monitor-sensor from ):

Ensure you mark it as executable.

Alternatives using the same principles are [https://gist.githubusercontent.com/ei-grad/4d9d23b1463a99d24a8d/raw/rotate.py rotate.py or 2in1screen.c.

Both will need to be adapted to your actual devices name and/or path.

You can put this in  before the exec line:

Note that there are many other rotate scripts on GitHub, including:

* https://github.com/freundTech/surface-tools/tree/master/autorotate
* https://github.com/andrewrembrandt/surface-autorotate2

## With GNOME
See iio-sensor-proxy. Install the  package.

If you want the rotation, but have the problem that GNOME is adjusting your brightness automatically in a bad way, then you can use these commands to disable it.

For current user, which can also be done via power management GUI:

 $ dbus-launch gsettings set org.gnome.settings-daemon.plugins.power ambient-enabled false

For GDM, which cannot be done via GUI, run as the gdm user:

 dbus-launch gsettings set org.gnome.settings-daemon.plugins.power ambient-enabled false

In the default Wayland mode GNOME screen rotation is broken on some laptops that don't report the screen flip kernel event () and so GNOME does not turn on some tablet features: there is a discussion on [https://gitlab.gnome.org/GNOME/mutter/-/issues/1686 GitLab. Install the  extension to always assume tablet mode when there is a touch screen.

Alternatively use the X11 mode, which you can select from the login screen.

## With a KDE module
Install  and , then restart your Plasma session. Screen rotation should now just work.

For automatic touch screen rotation edit  script, changing the hardcoded input device name to match the one you have (choose from the output of ).

## With rot8
Install  and execute  for Wayland or  for X11.
This integrates well with i3 or sway by using .

To only start rot8 when the tabletmode is enabled, you can use  and modify the handler at  to execute  when the tabletmode event is triggered (you can get the correct event by calling  and trigger the event by flipping your display).

rot8 will automatically detect orientation and rotate modern Linux desktop screen and input devices. For additional configuration see === With Sway ===

A simple Sway auto-rotate script could be implemented as follows (uses monitor-sensor from ):

{{bc|
#!/bin/bash
monitor-sensor | mawk -W interactive '/Accelerometer orientation changed:/ { print $NF; fflush();}' | while read -r line
do
   case "$line" in
       normal) swaymsg output eDP-1 transform 0 ;;
       bottom-up) swaymsg output eDP-1 transform 180 ;;
       right-up) swaymsg output eDP-1 transform 90 ;;
       left-up) swaymsg output eDP-1 transform 270 ;;
   esac
done
}}

Ensure you mark it as executable.

## With Hyprland
A simple Hyprland auto-rotate script could be implemented as follows (uses monitor-sensor from ):

Ensure you mark it as executable, and add it to  or  as an .

## With Labwc
A simple Labwc auto-rotate script could be implemented as follows (uses , , and monitor-sensor from ):

Ensure you mark it as executable.

Keep in mind that the default calibration matrix should be created in , as this script assumes it exists.

## Tablet mode
You can use  or  to configure laptop and tablet modes (e.g. enable/disable keyboard/touchpad/trackpoint, start/kill on-screen keyboard etc.)

If no sensor is detected, it can be manually triggered using .

## Desktop Environments / Window Managers
## i3
Using a tiling window manager like i3 makes a lot of sense for a tablet, where screen space is limited. While that may seem unintuitive at first – think about it: Android, iOS and Windows 10's tablet mode all use tiling window managers. Thus, i3 is an excellent window managers for tablets running Arch. The problem is that i3 is designed to be used with a keyboard, without a mouse, so there are no touch controls built in. For the most part, users will need to build their own, though touch gestures (see #Tips and tricks) or by adding touch button controls to a status bar or panel. Users of the [https://github.com/jaagr/polybar/ polybar status bar can try i3touchmenu.

## Xfce
Xfce works fine on tablets.  However, when xfce-screensaver locks, there is no way to show an on-screen keyboard by default.  One can be enabled by going to   and enabling the  option.  You will also need to add the command required to display your keyboard of choice.  For example, using  enter this command:

## Tips and tricks
## Easystroke
Easystroke is a gesture recognition application, recognizing gestures by a variety of input devices, to include pen stylus, mouse, and touch. Gestures can be used to launch programs, enter text, emulate buttons and keys, and scroll. Easystroke is available in the AUR: .

## Check pen battery
See: Laptop#Battery state

## Launch CellWriter under pen
One useful application of Easystroke is to use it to launch CellWriter right below your mouse pointer.

{{bc|
#!/bin/bash
# Original author: mr_deimos (ubuntuforums.org). February 14, 2010
# Many bugs fixed and improvements made by Ben Wong.  October 20, 2010

# This script toggles the cellwriter letter recognizer window.
# If a cellwriter window is visible, it will be hidden.
# If cellwriter is not already running, this will create a new process.
# If coordinates are specified, the window pops up at those coordinates.
# If coordinates are not specified, the window is toggled, but not moved.

# Implementation Note: this script is trickier than it should be
# because cellwriter does two stupid things. First, it has no
# --get-state option, so we can't tell if it is hidden or not. Second,
# both the notification area applet and the actual program window have
# the same window name in X, which means we can't simply use xwininfo
# to find out if it is showing or not.
#
# (Of course, we wouldn't have to be doing this crazy script at all,
# if cellwriter had a --toggle-window option to toggle showing the
# keyboard, but that's another rant...)
#
# To work around the problem, we'll assume that if the window we got
# information about from xwininfo is smaller than 100 pixels wide, it
# must be an icon in the notification area. This may be the wrong
# assumption, but, oh well...

if | "$1" == "--verbose" ; then
    verbose=echo
    shift
else
    verbose=:
fi

if |  "$1" == "-h"  ||  "$1" == "--help"  ; then
    cat >&2 /dev/null; then
    echo "$(basename $0): Error: Could not connect to your X server." >&2
    exit 1
fi

# Try to obtain CellWriter's window id.
# We can't use "xwininfo -name" b/c that might find the notification icon.
OLDIFS="$IFS"
IFS=$'\n'
for line in $(xwininfo -root -tree | grep CellWriter); do
    line=0x${line#*0x}		# Just to get rid of white space before 0x.
    $verbose -en "Checking: $line\t"
    if $line =~ (0x[A-Fa-f0-9+).*\)\ *(]; then
	id=${BASH_REMATCHwidth=${BASH_REMATCH[2}
	height=${BASH_REMATCHif  $width -gt 100 ; then
	    $verbose "looks good."
	    CW_WIN_ID=$id
	    break;
	else
	    $verbose "too small, ignoring."
	fi
    else
	echo "BUG: The xwininfo regular expression in $0 is broken." >&2
    fi
done
IFS="$OLDIFS"

#Check if Cellwriter's window is visible
if [ "$CW_WIN_ID"  ; then
    CW_MAP_STATE=`xwininfo -id "$CW_WIN_ID"|grep "Map State"|cut -f 2 -d :`
else
    $verbose "Can't find cellwriter window, checking for a running process..."
    if ! pgrep -x cellwriter >& /dev/null; then
	$verbose "No cellwriter process running, starting a new one."
	if  "$x" && "$y" ; then
	    cellwriter --show-window --window-x=$x --window-y=$y &
	else
	    cellwriter --show-window &
	fi
	exit 0
    else
	$verbose "Found a process, so the window has not been created yet."
	$verbose "Pretending the window is UnMapped."
	CW_MAP_STATE=IsUnMapped
    fi
fi

$verbose "Map state: $CW_MAP_STATE"

case "$CW_MAP_STATE" in

    *IsViewable*)		# Window is currently visible.
	$verbose "hiding window"
	cellwriter --hide-window &
	;;

    *IsUnMapped*)		# Window is currently hidden or non-existent.
	if  "$x" && "$y" && "$CW_WIN_ID" ; then
	    $verbose "moving window to $x $y"
	    xdotool windowmove $CW_WIN_ID $x $y
	fi
	$verbose "showing window"
	cellwriter --show-window &    # In bg in case cw is not already running
	;;

    *) 				# This will never happen...
	echo "BUG: cellwriter is neither viewable nor unmapped" >&2
	echo "BUG: ...which means this script, $0, is buggy." >&2
	exit 1
	;;
esac

exit 0
}}

Save the script as cellwriter.sh in either  or , and make it executable.

Then create a gesture in Easystroke tied to the following command:

 cellwriter.sh $EASYSTROKE_X1 $EASYSTROKE_Y1

When you launch it (using the gesture you created), it will open right under your pen.

## Gestures for the Alphabet
You can also use Easystroke to make gestures for the entire alphabet, replacing much of the need for CellWriter. To avoid having to make separate gestures for the upper-case letters, you can use the following script to activate the shift key.

Save the script as keypress.sh in either  or , and make it executable.

Then create a gesture in Easystroke tied to the following command:

 touch /tmp/shift

This will activate the shift key. To activate the letter keys, tie your gestures to the following command:

 keypress.sh $LETTER

Replace  with the letter in the alphabet in question.

So, when you want to enter an upper-case letter, use your gesture for the shift key followed by the letter. If you want a lower-case letter, simply use your gesture for the letter.

## Xournal & Xournal++
## Xournal
Xournal is an application for notetaking, sketching, and keeping a journal using a stylus. Xournal aims to provide superior graphical quality (subpixel resolution) and overall functionality.

You can also extend the functionality of  with patches, to enable things such as autosaving documents and inserting images. See SourceForge for links to all the available patches. To apply a patch, see Patching packages.

## Xournal++
Xournal++ () is the successor to Xournal that is currently in development. If you want a newer version Xournal, then you could try this. It is currently stable with little to no bugs that causes crashes.

## GDM
You can also use CellWriter with GDM. First open  as root with a text editor. Then near the bottom of the file, add the lines in bold as shown:

 fi
 cellwriter --keyboard-only &
 exit 0

You can add  and  to adjust the position of CellWriter accordingly. For example:
 cellwriter --keyboard-only --window-x=512 --window-y=768 &

To start a fully fledged CellWriter instance within the user session, you might want to terminate the instance started with the keyboard-only switch within the gdm context. Add something such as  to your newly created file .

## LightDM
Configuring LightDM to use Onboard for touchscreen login and unlocking is likely the simplest option (and stable) to provide onscreen keyboard login (when using the default GTK greeter).

Ensure  and  are installed and run  to configure onboard to start.

Specifiying  configures the Droid theme and sets the Phone layout.

## Touchegg
Touchegg is a multitouch gesture recognizer. It can recongize up to five finger gestures (tap, drag, pinch, rotate...).

## Troubleshooting
## Wacom Drivers
These commands are useful in troubleshooting:

 wacdump -f tpc /dev/ttyS0
 xidump -l
 xidump -u stylus

If xidump shows that your tablets max resolution is the same as screen resolution, then your wacom driver has rescaled your wacom coordinates to the X server's resolution. To fix this, try recompiling your linuxwacom driver with:

 ./configure --disable-quirk-tablet-rescale

## Screen Rotation support
Some video drivers do not support rotation. To check if your driver supports rotation, check the output of  for the list orientations:

 normal left inverted right
