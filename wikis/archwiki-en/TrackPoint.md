# TrackPoint

The TrackPoint is Lenovo's trademark for the pointing stick in the middle of the keyboard. It is supported by  and . On Wayland, only the  driver can be chosen from.

Default Xorg behavior supports click and point. For the  driver middle-click and scrolling requires extra configuration.

## GUI configuration
Install the  package.

## Middle button scroll
When using , middle-button scrolling is enabled by default.

When using , middle-button scrolling is supported via xinput from the  package. For example:

## Xorg configuration
Alternative to an  configuration, you can also create an Xorg#Configuration for the driver. For example, as , replacing  with the device name from xinput:

 Section "InputClass"
     Identifier	"Trackpoint Wheel Emulation"
     Driver "evdev"
     MatchProduct	"TPPS/2 IBM TrackPoint"
     MatchDevicePath	"/dev/input/event*"
     Option		"EmulateWheel"		"true"
     Option		"EmulateWheelButton"	"2"
     Option		"Emulate3Buttons"	"false"
     Option		"XAxisMapping"		"6 7"
     Option		"YAxisMapping"		"4 5"
 EndSection

## Two-button trackpoints
On two-button trackpoints, using , the scroll button can be set to right-click button without removing functionality.

Replacing device with the device name from :

 $ xinput set-prop "device" "libinput Button Scrolling Button" 3

## Sysfs attributes
TrackPoints expose their attributes as files in . For example, to manually enable the tap-to-click functionality:

 # echo -n 1 > /sys/devices/platform/i8042/serio1/press_to_select

## Configuration at boot
## udev rule
This rule increases the trackpoint speed and enables tap to select (see above) on boot.

{{hc|1=/etc/udev/rules.d/10-trackpoint.rules|2=
ACTION=="add", SUBSYSTEM=="input", ATTR{name}=="TPPS/2 IBM TrackPoint", ATTR{device/sensitivity}="240", ATTR{device/press_to_select}="1"
}}

## systemd.path unit
There have been reports on the forums that the attributes/files under  appear too late in the boot process for the above (or similar) udev rule(s) to have an effect on them. Instead, a systemd.path unit can be used to configure attributes of the TrackPoint.

First create an executable script named e.g.  that sets the TrackPoint attributes as shown in the #Sysfs attributes section.

The following example disables the trackpoint in some laptops, leaving the trackpoint left and right buttons (the ones over the touchpad) keep working just fine (however, if one disables the TrackPoint directly from the UEFI/BIOS settings, right and left trackpoint buttons will necessarily be disabled).

Afterwards, create the following systemd units. Make sure that all attributes modified by the script are listed with .

Finally, enable and start the  systemd unit.

## udev hwdb entry
Libinput applies its own parameters to sysfs based on entries in the udev hardware database. This is the behavior on systems running a Wayland compositor, as libinput is the only supported input interface in that environment. Changes made prior to the start of a Wayland compositor or X session will be overwritten.

To override libinput's default settings, add a local hwdb entry:

You can find various vendor/model keys in the udev hardware database. Note that since this commit libinput ignores the POINTINGSTICK_CONST_ACCEL parameter and uses POINTINGSTICK_SENSITIVITY. The range is 0-255.

Update the hardware database index, then to test the changes prior to restarting your compositor or X session, first find your device input node  using:

 # libinput list-devices

Run the following to generate some debug output:

 # udevadm trigger /sys/class/input/eventX
 # udevadm test /sys/class/input/eventX

Finally, restart your Wayland compositor or X session to apply the changes.

## device-quirks
With the  switch to the new device-quirks -style configuration files, you can adjust trackpoint parameters via local overrides in .

For example, to override the pointing speed, create the following file:

For more information, see libinput: Installing temporary local device quirks

## Troubleshooting
## Trackpoint is not detected or is detected after X minutes
This appears to be a kernel bug.A workaround is passing  to the  module as a kernel module parameter. However, this disables scrolling with the clickpad and the two-finger middle click.

 psmouse proto=bare

For some ThinkPad models with Elantech touchpad the Trackpoint and the corresponding hardware buttons do not get recognized. The above mentioned command does work but disables the two finger scrolling on the touchpad. To keep two finger interactions possible, use the following kernel module parameter:

 psmouse elantech_smbus=0

## Trackpoint buttons do not always work
If you discover that disabling the touchpad in the BIOS disables the wrong buttons and/or that the trackpoint buttons are very unreliable a workaround is to pass  to the  module as a kernel module parameter.

## Two-finger scroll ceases to work after suspending
On some laptops, psmouse seems to fail on start up, or after suspend:

 psmouse serio1: synaptics: Unable to initialize device

One workaround is to use add  to  as a kernel module parameter.

## Trackpoint moves on its own
On some ThinkPads the TrackPoint cursor moves spontaneously after release and it does not stop. This happens because of a low value of the  parameter (e.g. ), you need to change it to  or  to fix the problem. This can be done with a udev rule:

{{hc|/etc/udev/rules.d/10-trackpoint.rules|2=
ACTION=="add", SUBSYSTEM=="input", ATTR{name}=="TPPS/2 IBM TrackPoint", ATTR{device/drift_time}="25"
}}

If this method does not fix your issue, change the psmouse protocol to  (i.e. add  to your kernel parameters). This way the trackpoint will be identified as a "PS/2 Generic Mouse" instead of using the dedicated kernel driver.

If you do not need the cursor, you can use a libinput quirks override to disable cursor events. Button events will continue to work.

## Middle-click paste triggered while scrolling
Clicking the middle mouse button pastes from the PRIMARY selection by default, which is an inconvenience when using the middle mouse button to scroll with the TrackPoint. See Clipboard#Disabling middle-click paste to disable this behavior.
