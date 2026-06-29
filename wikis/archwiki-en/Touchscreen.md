# Touchscreen

If you ever tried to set up a touchscreen device in Linux, you might have noticed that it is either working out of the box (besides some calibration), or is very tedious, especially when it is not supported by the kernel.

## Introduction
This article assumes that your touchscreen device is supported by the kernel (e.g. by the usbtouchscreen module). That means there exists a  node for your device. Check out

 $ less /proc/bus/input/devices

to see if your device is listed or try

 # cat /dev/input/eventn

for every of your event nodes while touching the display. If you found the corresponding node, it is likely that you will be able to get the device working.

## Available X11 drivers
There are a lot of touchscreen input drivers for X11 out there. The most common ones are in the extra repository:

*  (likely the default driver if you plug in your touchscreen and it "just works")
* ; see also libinput
*

Less common drivers, not contained in the repository, are:

* xf86-input-magictouch
* xf86-input-mutouch
* xf86-input-plpevtch
* xf86-input-palmax

Proprietary drivers for some devices (e.g. xf86-input-egalax), were available at one point but have become unmaintained: use the open source drivers.

Depending on your touchscreen device choose an appropriate driver. Again, evdev is likely to be the default if your touchscreen "just works."

## Two-fingers scrolling
The two-fingers scrolling has to be implemented on the application side (see this link).
For Firefox, see Firefox/Tweaks#Enable touchscreen gestures.

There is a hack to emulates this scrolling behavior for every application in #Touchegg, but the X server still handles it as text selection (at least with Plasma).

## evdev drivers
## Calibration
Install  (AUR). Then, run xinput_calibrator and follow the instructions.

## Using a touchscreen in a multi-head setup
To use multiple displays (some of which are touchscreens), you need to tell Xorg the mapping between the touch surface and the screen. This can be achieved with xinput as follows.

Take for example the setup of having a wacom tablet and an external monitor;  shows both displays:

You see we have two displays here. LVDS1 and VGA1. LVDS1 is the display internal to the tablet, and VGA1 is the external monitor. We wish to map our stylus input to LVDS1. So we have to find the ID of the stylus input:

We see that we have two stylus inputs. We now need to simply map our inputs to our output like so:

 $ xinput --map-to-output 'Serial Wacom Tablet WACf004 stylus' LVDS1
 $ xinput --map-to-output 'Serial Wacom Tablet WACf004 eraser' LVDS1

You can automate this by putting these commands in your  or similar. The mapping will be lost if the touchscreen is disconnected and re-connected, for example, when switching monitors via a KVM. In that case it is better to use a udev rule. The Calibrating Touchscreen page has an example udev rule for the case when a transformation matrix has been calculated manually and needs to be applied automatically.

## Using xrandr-watch-git to automate map-to-output
There are xrandr events we can capture from a script. Install , create a script  with execution permission to perform map-to-output, for example:

and start, test and enable the systemd/User service .

## Wayland/Weston
On Wayland with sway (or wlroots-based supported compositors) and KDE Plasma, Touchcreens can be mapped to specific screens. There are also tools such as weston-touch-calibrator, but Gnome Wayland uses Xwayland leaving the calibrator unable to locate any touchscreen.

Wayland/Xwayland also masks the xinput list and funnels them down to generic xwayland devices such as "xwayland-pointer","xwayland-relative-pointer","xwayland-touch-pointer", etc. The Wayland method of "Xinput" is "Libinput", but does not have all the same functionality.  The current known method to use touchscreens in a multi-head setup is to force Gnome or KDE to use X11. libinput currently assumes the touchscreen(s) covers all available monitors.

See Sway#Touch display mapping for settings in sway.

For KDE Plasma, the "Touchscreen" menu in System Settings can be used to map a touchscreen to a screen in case the automatic mapping fails to achieve a correct result.

## Touchegg
Touchegg is a multitouch gesture program, only compatible with X, that runs as a user in the background, recognizes gestures, and translates them to more conventional events such as mouse wheel movements, so that you can for example use two fingers to scroll.  But it also interferes with applications or window managers which already do their own gesture recognition.  If you have both a touchpad and a touchscreen, and if the touchpad driver (such as synaptics or libinput) has been configured not to recognize gestures itself, but to pass through the multi-touch events, then Touchegg will recognize gestures on both: this cannot be configured.  In fact it does a better job of recognizing gestures than either the synaptics or libinput touchpad drivers; but on the touchscreen, it is generally better for applications to respond to touch in their own unique ways.  Some Qt and GTK applications do that, but they will not be able to if you have Touchegg "eating" the touch events.  So, Touchegg is useful when you are running mainly legacy applications which do not make their own use of touch events.

The two-fingers scrolling has been disabled in the recent rewrite of touchegg 2.0.
To enable it, install  and see this closed issue.
