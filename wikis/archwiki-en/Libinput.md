# Libinput

From the libinput wiki page:

:libinput is a library to handle input devices in Wayland compositors and to provide a generic X.Org input driver. It provides device detection, device handling, input device event processing and abstraction to minimize the amount of custom input code compositors need to provide the common set of functionality that users expect.

The X.Org input driver supports most regular input devices. Particularly notable is the project's goal to provide advanced support for touch (multitouch and gesture) features of touchpads and touchscreens. See the libinput documentation for more information.

## Installation
If you installed either Xorg or Wayland, then Libinput should already be installed as a dependency; there are no necessary extra packages.

* For Wayland, the  package should be installed as a dependency of any graphical environment you use that has Wayland, and no additional driver is needed.
* For Xorg,  is also a dependency. It is "a thin wrapper around libinput and allows for libinput to be used for input devices in X. This driver can be used as as drop-in replacement for evdev and synaptics." It replaces other packages used for input with X (i.e., those prefixed with ).
** You may want to install  to be able to change settings at runtime
* The  package contains the libinput diagnostics tool, which can be helpful in debugging interaction with the library and your hardware - regardless of the display server in use.

## Configuration
For Wayland, there is no libinput configuration file. The configurable options depend on the progress of your desktop environment's support for them (see #Graphical tools) or by applying desktop-agnostic udev rules (see Calibrating Touchscreen#Do it automatically via a udev rule and #Via a udev rule). Also see the [https://wayland.freedesktop.org/libinput/doc/latest/lua-plugins.html libinput plugin system.

For Xorg, a default configuration file for the wrapper is installed to . No extra configuration is necessary for it to autodetect keyboards, touchpads, trackpointers and supported touchscreens.

## Via xinput on Xorg
First, execute:

 # libinput list-devices

It will output the devices on the system and their respective features supported by libinput.

After a restart of the graphical environment, the devices should be managed by libinput with default configuration, if no other drivers are configured to take precedence.

See  for general options to set and information about allowable values. The xinput tool is used to view or change options available for a particular device at runtime. For example:

 $ xinput list

to view all devices and determine their names and numbers. In the following,  is either the name or number identifying the device to operate with.

 $ xinput list-props device

to view and

 $ xinput set-prop device option setting

to change a setting.  can be either the number or the name of the option. For example, to set both options of libinput Click Method Enabled (303), either of the following can be issued:

 $ xinput set-prop 14 303 1 1

or

 $ xinput set-prop 14 "libinput Click Method Enabled" 1 1

## Via Xorg configuration file
See Xorg#Using .conf files for permanent option settings. Logitech Marble Mouse#X11 and #Tapping button re-mapping illustrate examples.

Alternative drivers for Xorg#Input devices can generally be installed in parallel. If you intend to switch driver for a device to use libinput, ensure no legacy configuration files  for other drivers take precedence.

One way to check which devices are managed by libinput is the xorg logfile. For example, the following:

is a notebook without any configuration files in , i.e. devices are auto-detected.

Of course you can elect to use an alternative driver for one device and libinput for others. A number of factors may influence which driver to use. For example, in comparison to Touchpad Synaptics the libinput driver has fewer options to customize touchpad behaviour to one's own taste, but far more programmatic logic to process multitouch events (e.g. palm detection as well). Hence, it makes sense to try the alternative, if you are experiencing problems on your hardware with one driver or the other.

Custom configuration files should be placed in  and following a widely used naming schema  is often chosen as filename.

A basic configuration should have the following structure:

You may define as many sections as you like in a single configuration file (usually one per input device).
To configure the device of your choice specify a filter by using one of the available filters from , e.g.

*  (trackpoint)
*
*
*

The input device can then be configured with any of the lines of . Common options include:

* : tapping a.k.a. tap-to-click
* : trackpad no longer has middle and right button areas and instead two-finger click is a context click and three-finger click is a middle click, see the docs.
* : natural (reverse) scrolling
* : edge (vertical) scrolling

Bear in mind that some of them may only apply to certain devices and you will need to restart X for changes to take effect.

## Via a udev rule
The udev device-manager can be used to configure hardware properties and the libinput project provides documentation for the supported static device configuration via udev.

The following example cherry-picks the first hardware property listed in the documentation () to create a udev rule to calibrate a touchscreen:

 # libinput list-devices

Take note of the Device: name and Kernel path for the relevant input device. In this example the device  is at path  and a rule is created to rotate all touchscreen input by 270 degrees:

{{hc|/etc/udev/rules.d/99-mytouchscreen-calibration.rules|
# Do a 270 degree rotation on the input
ENV{ID_USB_SERIAL}"02eb_114e", ENV{LIBINPUT_CALIBRATION_MATRIX}"0 1 0 -1 0 1"
}}

Then, reload the rules and test to see if your device has registered the rule:

 # udevadm info /dev/input/event0

You should see your  listed there for the device.

Finally, either restart your machine or restart your Wayland desktop.

## Graphical tools
There are different GUI tools:

* GNOME:
** Control center has a basic UI. See GNOME#Mouse and touchpad.
**  offers some additional settings.
* Cinnamon:
** Similar to the GNOME UI, with more options.
* MATE:
** Mouse option available in the settings panel. Also accessible using
* KDE Plasma:
** Keyboard, mouse and controller devices can be configured from System Settings.
* Xfce:
** Configured from the Mouse and Touchpad submenu in .

## Tips and tricks
## Tapping button re-mapping
Swapping two- and three-finger tap for a touchpad is a straight forward example. Instead of the default three-finger tap for pasting, you can configure two-finger tap pasting by setting the  option in your Xorg configuration file. To set 1/2/3-finger taps to left/right/middle, set  to , for left/middle/right set it to .

Remember to remove  if your device is not a touchpad and adjust the  accordingly.

## Manual button re-mapping
For some devices, it is desirable to change the button mapping. A common example is the use of a thumb button instead of the middle button (used in X11 for pasting) on mice where the middle button is part of the mouse wheel. You can query the current button mapping via:

 $ xinput get-button-map device

where device is either the device name or the device ID, as returned by . You can freely permutate the button numbers and write them back. Example:

 $ xinput set-button-map device 1 6 3 4 5 0 7

In this example, we mapped button 6 to be the middle button and disabled the original middle button by assigning it to button 0.
For more information, please read about "ButtonMapping" section in .
This may also be used for Wayland, but be aware both the device number and its button-map will be different. Hence, settings are not directly interchangeable.

Some devices occur several times under the same device name, with a different amount of buttons exposed. The following is an example for reliably changing the button mapping for a Logitech Revolution MX mouse via xinitrc:

You could also use the Xorg configuration file to do that. The trackball used in this example has a physical scroll wheel, devices without one may need to refer the configuration for Logitech Marble Mouse.
The physical buttons in Kensington Slimblade Trackball layout are:

So, for the left hand user, you may use the configuration below. Although the device has no scroll up and scroll down buttons, you cannot disable them in the configuration or some application will not response to the action of the wheel.

## Change touchpad sensitivity
The method of finding the correct thresholds for when libinput registers a touch as DOWN and back UP again can be found in the upstream documentation.

Custom touchpad pressure values can be set via temporary local device quirks. See [https://wayland.freedesktop.org/libinput/doc/latest/device-quirks.html.

## Disable device
## Using environment variable
The  environment variable can be used to prevent initialization of a specific device. This is best set using a udev rule:

{{hc|/etc/udev/rules.d/99-libinput-ignore.rules|2=
ACTION=="addchange", device_delineation, ENV{LIBINPUT_IGNORE_DEVICE}="1"
}}

where device_delineation delineates a specific device using udev syntax. For example, for a whole USB device you would like libinput to ignore, you could use {{ic|1=SUBSYSTEMS=="usb", ATTRS{idVendor}=="vendor_id", ATTRS{idProduct}=="product_id"}} using the IDs from .

Once the file is created, udev will automatically pick up on the change (see Udev#Loading new rules); you just need to reconnect the device for the change to take place.

## Using xinput
To disable a device such as a touchpad, first get its name with  and then disable it with .

To make it permanent, see Autostarting.

To toggle, write a script such as [https://github.com/lahwaacz/Scripts/blob/master/toggle-touchpad.sh.

## Gestures
While the libinput driver already contains logic to process advanced multitouch events like swipe and pinch gestures, the Desktop environment or Window manager might not have implemented actions for all of them yet.

## libinput-gestures
For EWMH (see also wm-spec) compliant window managers, the libinput-gestures utility can be used meanwhile. The program reads libinput gestures (through ) from the touchpad and maps them to gestures according to a configuration file. Hence, it offers some flexibility within the boundaries of libinput's built-in recognition.

To use it, install the  package.

libinput-gestures needs access to the touchpad device. Traditionally, you can set this by adding yourself to the  group, but the more modern and safer approach is to manage access dynamically using udev, logind and acls. For this to work, create a file:

{{hc|/etc/udev/rules.d/71-touchpad.rules|2=
ACTION!="remove", ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
}}

The number at the beginning of the file is important: at index 70, the device property {{ic|ENV{ID_INPUT_TOUCHPAD}}} might be unset, and the  tag needs to be added before index 73 for .

You can use the default system-wide configured swipe and pinch gestures or define your own in a personal configuration file, see the README for details.

If using touchegg, uninstall the  package to prevent conflicts (see ==== fusuma ====

[https://github.com/iberianpig/fusuma Fusuma is a multitouch gesture recognizer, written in Ruby, which can be used as an alternative to libinput-gestures.

Install the  Ruby gem:

 $ gem install fusuma

Alternatively, there is also .

Other than the  Ruby gem you have to install the  Ruby gem or one between the  (for X) and  (generic:  Wayland, X11, etc). Other alternatives are listed here.

Then in  you have to set something like:

Or for :

Same thing for .

The swipe threshold is important for not swiping back too many pages.

Notice that the configure is for three fingers swipe. Two fingers swipe is not supported ==== Gebaar ====

[https://github.com/Coffee2CodeNL/gebaar-libinput Gebaar is another gesture recognizer.
Unlike Fusuma, it does not support pinching (support is planned in the future though) and thresholds, but in addition to swiping left, right, up and down with 3/4 fingers, it also supports diagonal swipes, which Fusuma does not.

There is a fork of gebaar at Gebaar which could be installed through  which supports pinch gestures and adds additional features to original gebaar. Take in mind that this version is currently under active development and introduces configuration changes which makes it incompatable to original Gebaar

## GnomeExtendedGestures
For deeper integration with GNOME, there is GnomeExtendedGestures (). Three finger horizontal and vertical gestures can be configured to perform gnome-shell actions (such as toggling the application overview or cycling between them).

## Scroll with mouse by holding a button
There is a nice trick to optimize scrolling with a mouse or trackball by holding a mouse button (like right or middle button, or some other if the mouse has more buttons) and moving the mouse. Very useful in case your mouse does not have the mouse wheel (often the case with the trackballs). To do that one has to set  to  and specify the mouse button in the  option for the action. Here is an example for configuration to achieve that:

## Mouse wheel scrolling speed scaling
For some mice, especially when using on a HiDPI desktop, the wheel scrolls too slow. A patch is submitted to libinput but it has not been accepted. There is a third-party xf86-input-libinput that incorporates this patch.

This patch introduces a new property  to mice, and you can set a scaling factor like

 $ xinput --set-prop device_name 'libinput Scroll Distance Scale' 2.5 2.5

where the  is the name of your mouse device, listed in .  are the scaling factors, for x- and y-axis, respectively.

Alternatively, install  and restart Xorg, then enlarge y-axis scroll distance to 6 times by

 $ echo 6 > /tmp/libinput_discrete_deltay_multiplier

Here is an example to modify the scaling factor upon focusing change

## Enable the touchpad while typing
By default, libinput disables the mousepad when typing. This is conflicting for some software such as Inkscape which has keybindings that require mouse movement while a key is pressed. One way to enable the touchpad while typing is by adding the following line to the  section of :

 Section "InputClass"
     ...
     Option "DisableWhileTyping" "0"
 EndSection

The same effect can alternatively be accomplished using xinput. The property may be named something like .

## Troubleshooting
First, see whether executing  can support you in debugging the problem, see  for options.

Some inputs require kernel support. The tool evemu-describe from the  package can be used to check:

Compare its output (for example) with a supported trackpad. i.e. a couple of ABS_ axes, a couple of ABS_MT axes and no REL_X/Y axis. For a clickpad the  property should also be set, if it is supported.

## Touchpad not working in GNOME
Ensure the touchpad events are being sent to the GNOME desktop by running the following command:

 $ gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled

Additionally, GNOME may override certain behaviors, like turning off Tapping and forcing Natural Scrolling. In this case the settings must be adapted using GNOMEs  command line tool or a graphical frontend of your choice. For example if you wish to enable Tapping and disable Natural Scrolling for your user, adjust the touchpad key-values like the following:

 $ gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true
 $ gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll false

## Inertial scrolling does not work in KDE
The feature is currently not implemented, see KDE bug 456383. As a workaround for Chromium-based browsers, install the SmoothScroll extension.

## Keys stuck after entering tablet mode
On some Tablet PCs (notably Lenovo Yogas), holding a keyboard key while entering the tablet mode can cause the key be stuck until the tablet mode is disabled. It is sometimes possible to fix this behavior by modifying libinput quirks files. See Issue 914.

For example, find the name of the keyboard device:

Then, create an override file:

 disables behavior that causes the bug. Consult Device quirks for information about configuration format and Match directives that select the device to configure. It is often possible to create an override file based on an existing quirks entry for your particular device. Default quirks files can be found in .
