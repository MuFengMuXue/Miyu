# Graphics tablet

From Wikipedia:Graphics tablet:

:A graphics tablet (also known as a digitizer, digital graphic tablet, pen tablet, drawing tablet, external drawing pad or digital art board) is a computer input device that enables a user to hand-draw images, animations and graphics, with a special pen-like stylus, similar to the way a person draws images with a pencil and paper.

Most graphics tablets will work out of the box with Arch Linux. Additional configuration is required for certain extra features, such as button remapping and adjusting the tablet's aspect ratio. This article explains how to configure your tablet under Xorg with the  driver. For configuration under Wayland, or when using the default  driver, see #Wayland and libinput.

## Kernel support
The Arch Linux kernels include drivers by the linux-wacom and DIGImend projects. linux-wacom supports Wacom devices, while DIGImend supports devices from other manufacturers. Both projects publish a list of supported devices: linux-wacom, DIGImend. After connecting your tablet via USB or Bluetooth, it should show up when running  as root and be listed in . For USB devices, the  command from  should also show your tablet. If your tablet does not show up, or if certain features do not work, see #Device not recognized by the kernel.

## Alternative drivers
*
*
*
*
*
*

## Installation
Install the  Xorg driver. No additional configuration is required for Wacom devices, as the included  file will automatically load the  driver when plugging Wacom devices. If your device is from another manufacturer, you will need to manually configure Xorg to use it with the wacom driver, which will allow configuring it through xsetwacom. Create a file in , where  is your USB ID as seen by :

After restarting X, the command  should now list some devices. If it does not, see #Manual setup.

## Utilities
*
*
*

## Configuration
The Xorg driver can be temporarily configured with , see . Changes are lost after X server restarts or replugging your tablet, see #Permanent configuration to view methods to keep your settings persistent.

List the available devices:

For the  and  commands, devices can be specified by name or id. Scripts should use names because ids can change after X server restarts or replugging.

## Remapping buttons
Xorg treats the buttons on tablets and pens as mouse buttons. Tablet buttons start at 1, pen buttons start at 2 (1 is the tip contact event). Since most applications do not allow mapping shortcuts to mouse buttons, users may be interested in remapping these buttons to keyboard buttons.

If you have not yet remapped your buttons, you can easily identify their numbers with  by running the following command, placing the mouse cursor on the created window and pressing a button:

After identifying the button, you can remap it with xsetwacom. The general mapping syntax is as follows:

 $ xsetwacom set pad-or-stylus Button number keyword arguments

The full list of keywords and their arguments is available in . Here are a few examples:

To remap the button to :

 $ xsetwacom set pad Button 1 "key +ctrl z -ctrl"

To remap the button to mouse button 3:

 $ xsetwacom set pad Button 1 "button 3"

To press mouse button 1 while holding :

 $ xsetwacom set pad Button 1 "key +shift button 1 key -shift"

To clear all custom mappings from the button:

 $ xsetwacom set pad Button 1

## Execute custom commands
Although you cannot map tablet buttons to custom commands directly using xsetwacom, it is possible to map them to a key combination that will activate a custom keybind utility such as Xbindkeys, sxhkd, or the keyboard shortcut configuration system for your window manager or desktop environment.

It is possible to remap the tablet buttons to a function key or mouse button that's not available on your hardware, such as F20 or mouse button 10. This way, you can set up custom commands that are only executed through your tablet's buttons.

## Adjusting aspect ratios
Drawing areas of tablets are generally more square than the usual widescreen display with a 16:9 aspect ratio, leading to a slight vertical compression of your input. To resolve such an aspect ratio mismatch you need to compromise by either reducing the drawing area height (called Force Proportions on Windows) or reducing the screen area width. The former wastes drawing area and the latter prevents you from reaching the right edge of your screen with your Stylus. It is probably still a compromise worth to be made because it prevents your strokes from being skewed.

Find out your tablet's resolution by running:

 $ xsetwacom get stylus Area

## Reducing the drawing area height
Run:

 $ xsetwacom set stylus Area 0 0 tablet_width height

where height is tablet_width * screen_height / screen_width.

The tablet resolution can be reset back to the default using:

 $ xsetwacom set stylus ResetArea

## Reducing the screen area width
Run:

 $ xsetwacom set stylus MapToOutput WIDTHxSCREEN_HEIGHT+0+0

where WIDTH is screen_height * tablet_width / tablet_height.

## Mapping the tablet to a monitor
If you have multiple monitors, it is useful to map your tablet to a single monitor in order to avoid distortions when drawing. This can also be used if you have a graphics tablet with a screen, in order to map the tablet's active area to its own screen.

You can map your tablet to a monitor with the following command, where output is your monitor identifier as reported by xrandr:

 $ xsetwacom set stylus MapToOutput output

For example:

 $ xsetwacom set 'Wacom Intuos S Pen stylus' MapToOutput VGA-0

If this does not work with the Nvidia binary drivers, try using HEAD-0, HEAD-1, ... according to the monitor number.

Alternatively you can use the argument next to switch to the next available monitor.

For example:

 $ xsetwacom set 'Wacom Intuos S Pen stylus' MapToOutput next

If xsetwacom is unable to find your output, you can use the command in #Reducing the screen area width to manually map the tablet to a region matching your monitor. Run:

 $ xsetwacom set stylus MapToOutput SCREEN_WIDTHxSCREEN_HEIGHT+HORIZONTAL_OFFSET+VERTICAL_OFFSET

Where SCREEN_WIDTH and SCREEN_HEIGHT are your monitor's width and height in pixels, while HORIZONTAL_OFFSET and VERTICAL_OFFSET are the coordinates for your desired monitor, starting from the leftmost and highest pixel in your setup. For example, if you have two 1920x1080 monitors side-by-side, and you want to map your tablet to the rightmost monitor, you would run:

 $ xsetwacom set stylus MapToOutput 1920x1080+1920+0

In case xsetwacom does not work, you can try xinput. First, you need to find your stylus ID:

In this case, the stylus ID is 20. To map it to monitor VGA-0, run:

 $ xinput map-to-output 20 VGA-0

If all else fails, you will have to adjust your tablet's Coordinate Transformation Matrix. Instructions to calculate a matrix for your tablet are available in the xf86-input-wacom wiki.

## Pressure curve
Use the Wacom Pressure Curve and Threshold Graph to find P1=red (eg. 50,0) and P2=purple (eg. 100,80) of your desired curve. The x-axis is the input pressure you apply to the pen; the y-axis is the output pressure the application is given.

You can change the pressure curve with:

 $ xsetwacom set stylus PressureCurve x1 y1 x2 y2

## Permanent configuration
## Through xsetwacom via udev and systemd service
It is possible to save your  parameters in a shell script that is autostarted through udev with a custom systemd/User unit file. This approach is more complex than autostarting the shell script through your desktop environment or window manager, however, it will run the script every time the tablet is connected to the computer.

First install  and run  to find the vendor ID of your tablet ( in the example below).

Then create a udev rule to start a systemd unit when the tablet is connected (replace the vendor ID accordingly):

{{hc|/etc/udev/rules.d/99-wacom.rules|2=
ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="056a", TAG+="systemd", ENV{SYSTEMD_USER_WANTS}+="wacom.service"
}}

Prepare the systemd unit file. It is connected to the special  which should be active whenever any graphical session is active, see .

Prepare the script for tablet configuration. When started from the systemd user service, the needed variables  and  should already be set. See systemd/User#DISPLAY and XAUTHORITY for details.

{{hc|wacom-config.sh|
#!/bin/sh

for i in $(seq 10); do
    if xsetwacom list devices | grep -q Wacom; then
        break
    fi
    sleep 1
done

list=$(xsetwacom list devices)
pad=$(echo "${list}" | awk '/pad/{print $7}')
stylus=$(echo "${list}" | xsetwacom list devices | awk '/stylus/{print $7}')

if [ -z "${pad}" ]; then
    exit 0
fi

# configure the buttons on ${stylus} with your xsetwacom commands...
#xsetwacom set "${stylus}" Button 2 11
#...
}}

Finally start/enable the service  with the  flag.

## Compatibility with Xfce4 Display Profiles
If you have a tablet with integrated display and want to seamlessly switch between multiple display profiles in Xfce4, simply listening to udev events might not be enough.
You'll need to change the device settings whenever your display geometry changes. (e.g. Mirrored vs. Side-by-Side Setups).

In these cases you can use  to monitor changes to the active display profile.

{{hc|wacom-config-daemon.sh|
#!/usr/bin/env sh

# Use this to target your specific monitor device
screen_dev="HDMI-A-0"

xfconf-query -c displays -p /ActiveProfile -m | while IFS= read -r; do
  echo "Reconfiguring..."

  # Tested with Wacom Cintiq 16 Pen (stylus/eraser)
  for id in $(xsetwacom list devices | grep -i wacom | awk '/Pen/{print $7}'); do
    xsetwacom set "${id}" MapToOutput "${screen_dev}"
  done
done
}}

Now add this script to your autostart applications in

## Through Xorg.conf
Configuration can be made persistent in xorg.conf and .

You firstly need to find out your product names in the Xorg log file:

For these product names the sections would be:

* The options described in  can be added to sections.
* The product name needs to contain the  value in order for a section to match. Matching of parent devices requires negative matching.
* The  can be arbitrary and is printed into the Xorg log when the section matches. Giving your identifiers a common prefix lets you easily grep for what sections were matched:
* Configuration changes require a X server restart to take effect.

xsetwacom can try to print all current settings of a device in xorg.conf format with:

 $ xsetwacom get device all

## Button remapping
Button remapping through Xorg.conf only allows you to remap the tablet buttons to mouse buttons.

You can then use #Execute custom commands to map these buttons to other commands, or other keys using automation tools.

## Letting libinput take control of the touchpad
As the wacom touchpad normally does not support inverted scrolling it can be desirable to use libinput to take control of the touchpad.

To do this create  with the following contents:

 Section "InputClass"
     Identifier "libinput Wacom touchpad override class"
     MatchUSBID "056a:*"
     MatchDevicePath "/dev/input/event*"
     MatchIsTouchpad "true"
     Driver "libinput"
 EndSection

Reboot afterwards.

See for a more detailed explanation.

## LEDs
See the [https://docs.kernel.org/admin-guide/abi-testing.html#abi-file-testing-sysfs-driver-wacom sysfs-driver-wacom documentation. To make changes without requiring root permissions you will likely want to create a udev rule like so:

Setting the Intuos OLEDs can be done using .

## Application-specific configuration
## Alchemy
 (and ) needs the JPen library to manage stylus pressure. See Digimend documentation about Alchemy.

## Blender
To enable pad buttons and extra pen buttons in Blender, you can create a xsetwacom wrapper to temporarily remap buttons for your blender session.

## DrawPile
 is a drawing whiteboard (network collaborative drawing tool). It manages pressure level on its drawing tools. In the "Freehand" box, a brush icon at the right of each parameter needs to be activated to have pressure management on this parameter. There is only a general curve on the bottom right of the window ("Input" box), that can be applied to stylus, distance and velocity.

## GIMP
To enable proper usage and pressure sensitive painting in GIMP, just go to Edit > Input Devices. Now for each of your eraser, stylus, and cursor devices, set the mode to Screen, and remember to save.

* Please take note that if present, the pad device should be kept disabled as I do not think GIMP supports such things. Alternatively, to use such features of your tablet you should map them to keyboard commands with a program such as Wacom ExpressKeys.
* You should also take note that the tool selected for the stylus is independent to that of the eraser. This can actually be quite handy, as you can have the eraser set to be used as any tool you like.

For more information checkout the Setting up GIMP section of GIMP Talk - Community - Install Guide: Getting Wacom Drawing Tablets To Work In Gimp.

If the above was not enough, you may want to try setting up the tablet's stylus (and eraser) as a second mouse pointer (separating it from your mouse) by using the  and  commands. It can help when GIMP does not start painting even if the stylus touches the tablet.

## Inkscape
Pressure sensitivity in Inkscape is enabled the same way as in GIMP. Go to Edit > Input Devices.... Now for each of your eraser, stylus, and cursor devices, set the mode to Screen, and remember to save.

## Krita
If your tablet does not draw in Krita (clicks/pressure are not registered) but works in the brush selection dialog which has a small test area, try putting Krita in full-screen or canvas-only mode.

Krita only requires that Qt is able to use your tablet to function properly. If your tablet is not working in Krita, then make sure to check it is working in Qt first. The effect of tablet pressure can then be tweaked in the painttop configuration, for example by selecting opacity, then selecting pressure from the drop down and adjusting the curve to your preference.

## MyPaint
 (extra , , note that these brushes are also used on other applications using libmypaint) is a general bitmap drawing application. Its advanced brush settings have been adopted by GIMP, Krita, OpenToonz, and few others and is in integration process in Pencil2D. It is a very light tool that can be used in low-end computers.

In MyPaint, there are general settings about tablets and per brush specific parameters (you can set your own brushes).

General settings are in menu Edit > Edit Preferences.

* The "Pressure" tab is for global pressure mapping.
* The "Devices" tab displays the list of detected input devices with little general information. Each one can be assigned to specific tasks by clicking on their parameter in the "Use for..." (Any Task, Ignore, Non-painting tasks, Navigation only) and "Scroll..." (zoom, pan) columns.
* The "Buttons" tab allows to assign buttons to specific functions.

Brush settings can be accessed by the brush context menu (right click on a tool). You can duplicate an existing tool before making modification, and so, keep the tool with its default preset ("clone" in the context menu).

* To edit brush settings, simply use the Edit Brush settings from the context menu on brush. There are several settings, see the MyPaint documentation for a full description or play with them to discover what they do.

## OpenToonz
 is a professional 2D animation tool, first developed by Studio Ghibli, and used by Ghibli and Folimage among others.

Stylus pressure is managed by default on default tools. There is a checkbox Pressure at the second line, at top right, that can be unchecked to disable pressure management. Several presets can be selected by the menu button at right of Preset, and added or deleted with the +/- buttons.

 brushes can be chosen in the Basics mode (upper right tabs), and then in the column between the drawing area and the exposure sheet: at the "Palette" button, click on "Raster" tab to view the brushes. The brushes can be edited with MyPaint and used in OpenToonz.

## Pencil2D
 is a light 2D animation tool. Each tool that can use the pressure parameter (Pencil, Eraser, Pen and Brush) has a checkbox called "Pressure" that is checked by default to use stylus pressure parameter.

## Xournal++
Xournal++ () is the successor to  and fully supports pressure sensitive stylus input. For configurations, see Input Devices and Stylus in the Edit > Preferences menu.

## Wayland and libinput
When you are using Wayland, graphics tablets are handled by libinput, which relies on information provided by [https://github.com/linuxwacom/libwacom libwacom. In this scenario, configuration through xsetwacom is not possible. You can only configure your tablet through the settings that are available in your desktop environment or Wayland compositor. See to check if your device is fully supported, and for methods to add support to your device.

{| class="wikitable
! Environment or compositor !! Map tablet to monitor || Map tablet to region || Configure tablet buttons !! Documentation
|-
| GNOME ||  ||  ||  || [https://help.gnome.org/users/gnome-help/stable/wacom.html.en
|-
| KDE Plasma ||  ||  ||  ||
|-
| Sway ||  ||  ||  ||
|-
| Hyprland ||  ||  ||  || |-
| River Classic ||  ||  ||  ||
|-
| Niri ||  ||  ||  || [https://yalter.github.io/niri/Configuration%3A-Input.html#pointing-devices
|}

## Sway
## Map to output
This has the same effect of #Mapping the tablet to a monitor, meaning that the tablet will not have an exact aspect ratio match with the output.

Add the following line to your sway configuration file:

Where Identifier is the identifier of your tablet, as read by :

And Display-Name is the identifier of your output, as read by :

## Map to output region
This has the same effect as #Reducing the screen area width. First, you need to figure out the active area for your tablet. Run:

Move your tablet stylus to the bottom right corner to get the maximum ABS_X and ABS_Y values, then add the following line to your sway configuration:

Where width is calculated by output_height * (ABS_X / ABS_Y), and X and Y are the starting coordinates of the region.

For example, if you have two 1920x1080 monitors side-by-side, and you want to map your tablet to a region in the rightmost monitor, use the following line:

## Troubleshooting
## Device not recognized by the kernel
Some tablets may be too recent to be supported by your current kernel. On Wacom devices, this is represented by a "Unknown device_type" message in your dmesg output. In this scenario, it is possible that the out-of-tree version of the drivers have support for your tablet before it is upstreamed to the kernel.

Install  if you have a Wacom tablet, or  if you have a tablet from another manufacturer. You will also need the headers for your current kernel, see DKMS for more information.

## Tablet recognized but xsetwacom and similar tools do not display it
Your logs indicate that the correct driver is selected, and the tablet works. However, when running  or use similar tools that depend on the correct driver, you get an empty list.

A reason might be the execution order of your xorg configuration.  gets executed first, then . The package  contains the file . If there is a catchall for tablets, executed after this file, the previously selected  driver will be overwritten with a generic one that does not work with xsetwacom et. al.

To make sure, check the rules contained in the files executed after  for anything that looks like graphics tablets.

## Manual setup
A manual configuration is done in  or in a separate file in the  directory. The Wacom tablet device is accessed using an input event interface in  which is provided by the kernel driver. The interface number  is likely to change when unplugging and replugging into the same or especially a different USB port. Therefore it is wise to not refer to the device using its concrete  interface (static configuration) but by letting udev dynamically create a symbolic link to the correct  file (dynamic configuration).

## USB-devices
After (re-)plugging in your USB-tablet (or at least after rebooting) some symbolic links should appear in  referring to your tablet device.

If not, your device is likely to be not yet included in the udev configuration from wacom-udev which resides in . Copy the file to  and modify it there.

Add your device to the file by duplicating some line of another device and adapting idVendor,idProduct and the symlink name to your device.
The two id's can be determined using

In this example idVendor is 056a and idProduct 0062. In case you have device with touch (e.g. Bamboo Pen&Touch) you might need to add a second line for the touch input interface. For details check the linuxwacom wiki Fixed device files with udev.

Save the file and reload udev's configuration profile using the command udevadm control --reload-rules Check again the content of /dev/input to make sure that the wacom symlinks appeared. Note that you may need to plug-in the tablet again for the device to appear.

The files of further interest for the Xorg configuration are  and for a touch-device also .

## Static setup
Usually it is recommended to rely on Xorg's auto-detection or to use a dynamic setup. However for an internal tablet device one might consider a static Xorg setup in case autodetection does not work. A static Xorg setup is usually not able to recognize your Wacom tablet when it is connected to a different USB port or even after unplugging and replugging it into the same port, and as such it should be considered as deprecated.

If you insist in using a static setup just refer to your tablet in the Xorg configuration in the next section using the correct  files as one can find out by looking into .

## Xorg configuration
In either case, dynamic or static setup you got now one or two files in  which refer to the correct input event devices of your tablet. All that is left to do is add the relevant information to , or a dedicated file under  . The exact configuration depends on your tablet's features of course.  might give helpful information on what InputDevice sections are needed for your tablet.

An example configuration for a Volito2 might look like this

 Section "InputDevice"
     Driver        "wacom"
     Identifier    "stylus"
     Option        "Device"       "/dev/input/wacom"   # or the corresponding event?? for a static setup
     Option        "Type"         "stylus"
     Option        "USB"          "on"                 # USB ONLY
     Option        "Mode"         "Relative"           # other option: "Absolute"
     Option        "Vendor"       "WACOM"
     Option        "tilt"         "on"  # add this if your tablet supports tilt
     Option        "Threshold"    "5"   # the official linuxwacom howto advises this line
 EndSection
 Section "InputDevice"
     Driver        "wacom"
     Identifier    "eraser"
     Option        "Device"       "/dev/input/wacom"   # or the corresponding event?? for a static setup
     Option        "Type"         "eraser"
     Option        "USB"          "on"                  # USB ONLY
     Option        "Mode"         "Relative"            # other option: "Absolute"
     Option        "Vendor"       "WACOM"
     Option        "tilt"         "on"  # add this if your tablet supports tilt
     Option        "Threshold"    "5"   # the official linuxwacom howto advises this line
 EndSection
 Section "InputDevice"
     Driver        "wacom"
     Identifier    "cursor"
     Option        "Device"       "/dev/input/wacom"   # or the corresponding event?? for a static setup
     Option        "Type"         "cursor"
     Option        "USB"          "on"                  # USB ONLY
     Option        "Mode"         "Relative"            # other option: "Absolute"
     Option        "Vendor"       "WACOM"
 EndSection

Make sure that you also change the path () to your mouse, as it will be  now.

 Section "InputDevice"
     Identifier  "Mouse1"
     Driver      "mouse"
     Option      "CorePointer"
     Option      "Device"             "/dev/input/mouse_udev"
     Option      "SendCoreEvents"     "true"
     Option      "Protocol"           "IMPS/2"
     Option      "ZAxisMapping"       "4 5"
     Option      "Buttons"            "5"
 EndSection

Add this to the ServerLayout section

 InputDevice "cursor" "SendCoreEvents"
 InputDevice "stylus" "SendCoreEvents"
 InputDevice "eraser" "SendCoreEvents"

And finally make sure to update the identifier of your mouse in the ServerLayout section &ndash; as mine went from

 InputDevice    "Mouse0" "CorePointer"

to

 InputDevice    "Mouse1" "CorePointer"

## Mouse moving erratically due to proximity sensor
You can disable the mouse jumping due to a proximity sensor detecting a non-existing stylus. You can find your device with , and after spotting the stylus, disable it with:

 $ xinput disable device

This only works if you are not currently using a stylus.

## Touch arbitration not working on graphic tablets
If you are using libinput, graphic tablets that have a stylus and a touchscreen might not support touch arbitration out of the box because the devices are not grouped into the same libinput device group. You can fix this by writing udev rules. For example, if the touchscreen is recognized with  and the Wacom tablet with , you can create  as a rule that groups these devices into the group :

{{hc|/etc/udev/rules.d/80-touch-arbitration.rules|2=
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0001", ATTRS{idProduct}=="000a", ENV{LIBINPUT_DEVICE_GROUP}="f865e87b"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0002", ATTRS{idProduct}=="000b", ENV{LIBINPUT_DEVICE_GROUP}="f865e87b"
}}

## Reporting issues with non-Wacom tablets
If you have a non-Wacom tablet that has missing features, you can report a tablet test to DIGImend drivers authors in order to include its functionalities into the driver. The DIGImend diagnostic tools are available on the AUR as . You will also need the  and  programs available in .
