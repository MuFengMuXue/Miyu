# Mouse acceleration

## Disabling mouse acceleration
Install the  package, providing the commandline tool  to configure devices .

Using Xorg, libinput sets itself as the default driver with . To activate the  profile for our pointer device, we need to set the  profile to  and the  and  profile options to .

Find out your device id:

 # xinput

The first number indicates the default acceleration profile, the second number indicates the flat profile (No Acceleration), and the third number indicates a custom profile. To activate the flat profile:

 # xinput set-prop "deviceid" "libinput Accel Profile Enabled" 0 1 0

Confirm the changes:

 # xinput list-props "deviceid"

Make it persistent by adding the option to the pointer section:

## Disable mouse acceleration in GDM
Disable mouse acceleration in GDM with Wayland:

 dbus-launch gsettings set org.gnome.desktop.peripherals.mouse accel-profile 'flat'

## Configuring mouse acceleration
Setting the mouse acceleration depends on the windowing protocol you are using: either Xorg or Wayland.

* On Xorg, there are several ways of setting mouse acceleration
:* by editing Xorg configuration files
:*  and  which provide xset and xinput respectively
:* and configuration interfaces common in desktop environments.

* If you are using Wayland, the events are controlled via libinput. It is the compositor's job to expose the settings brought by libinput. There is currently no standard way to change settings across compositors.[https://www.reddit.com/r/gnome/comments/3upay2/wayland_where_are_the_mouse_acceleration_options/
* GNOME manages mouse acceleration by itself. A choice between "adaptive" and "flat" profiles can be chosen by installing  and editing the value in org/gnome/desktop/peripherals/mouse/acceleration-profile. Alternatively,  can also be used to edit the org/gnome/desktop/peripherals/mouse/acceleration-profile.

## Mouse acceleration with libinput
When using the adaptive pointer acceleration profile, libinput calculates the mouse acceleration depending on the DPI and the parameter  libinput relies on the resolution reported by evdev [https://wayland.freedesktop.org/libinput/doc/latest/normalization-of-relative-motion.html. Feedback settings set with  are effectively ignored. When using the flat pointer acceleration profile, the acceleration factor is constant regardless of the velocity of the pointer. This provides 1:1 movement between the device and the pointer on-screen.

## Changing the acceleration
Find the id of your device with  and set the acceleration speed with the following command. Note that the acceleration speed has to be in the range of Check [https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#ptraccel-linear this plot to see the impact of different acceleration speed values.

 $ xinput --set-prop  'libinput Accel Speed'

Confirm your changes with the following:

 $ xinput --list-props

## Persistent configuration
libinput does not store configuration options, it is up to the caller to manage these. Under Wayland configuration is restored by the desktop environment. Under X  reads the xorg configuration files and applies the options https://wayland.freedesktop.org/libinput/doc/latest/faqs.html#how-do-i-configure-my-device-on-x. To make changes persistent under X create a file like this:

For further options see .

## Setting mouse acceleration
## In Xorg configuration
See  for details.

Examples:

You can also assign settings to specific hardware by using "MatchProduct", "MatchVendor" and other matches inside class sections. Run  to find out the product name and vendor to match:

 $ lsusb -v | grep -e idProduct -e idVendor

If you are unable to identify your device, try running . Some devices the use Logitech Unifying Receiver share the same USB connection therefore, the mouse do not appear using

## Using xinput
First, get a list of devices plugged in (ignore any virtual pointers):

 $ xinput list

Take note of the ID. You may also use the full name in commands if the ID is prone to changing.

Get a list of available properties and their current values available for modification with

 $ xinput list-props 9

where  is the ID of the device you wish to use. Or

 $ xinput list-props "mouse name"

where  is the name of your mouse given by .

Example, changing the property of  to 2:

 $ xinput --set-prop "mouse name" "Device Accel Constant Deceleration" 2

To make it permanent, edit Xorg configuration (see above) or add commands to xprofile. The latter will not affect speed in a display manager.

## Configuration example
You may need to resort to using more than one method to achieve your desired mouse settings. Example to configure a generic optical mouse:
First, slow down the default movement speed 3 times so that it is more precise.

 $ xinput --set-prop 9 'Device Accel Constant Deceleration' 3

Then, enable acceleration and make it 3 times faster after moving past 6 units.

 $ xset mouse 3 6

If you are satisfied with the results, store the preceding commands in .
