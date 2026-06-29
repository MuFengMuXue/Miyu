# Calibrating Touchscreen

To use multiple displays (some of which are touchscreens), you need to tell Xorg the mapping between the touch surface and the screen. This can be done using  to set the touchscreen's coordinate transformation matrix.

This is a guide to do that, the old-fashioned way, in cases when xrandr does not know about your separate screens because they have been merged into one (e.g., when using TwinView).  Everyone else, please go to Touchscreen to do it the easy way.

You will need to run the  command every time you attach the monitor or log in. Or course, you can add the command to your session-autostart.
You can also use Udev to automate this.

## Using nVidia's TwinView
## Get to know your system
## Your screen
Using TwinView, X will see all your Screens as one big screen. You can get your total height and width by executing

 $ xrandr  grep \* # xrandr uses "*" to identify the screen being used

You should see a line like this:

 3600x1230      50.0*

what means, your total width is 3600 and your total height is 1230.

## Your touch device
Your next job is to get your device's name. Execute

 $ xinput list

and find it by its name. Find the item containing , which is usually your own device name. E.g. if the line can look like this

 ⎜   ↳ Acer T230H                              	id=24	pointer  (2)

your device name is

 Acer T230H

Execute

 $ xinput list-props "Device Name"

and make sure there is a property called

 Coordinate Transformation Matrix

If not, you probably selected the wrong device, use another one.

## Touch area
You need to shrink your touch area into a rectangle which is smaller than the total screen. This means, you have to know four values:
* Height of touch area
* Width of touch area
* horizontal offset (x offset) (amount of pixels between the left edge of your total screen and the left edge of your touch area)
* vertical offset (y offset) (amount of pixels between the top edge of your total screen and the top edge of your touch area)

## Calculate the Coordinate Transformation Matrix
Now, calculate these as accurate as possible:
* c0 = touch_area_width / total_width
* c2 = touch_area_height / total_height
* c1 = touch_area_x_offset / total_width
* c3 = touch_area_y_offset / total_height

The matrix is
 [ c0 0  c1 ]
 [ 0  c2 c3 ]
 [ 0  0  1  ]
which is represented as a row-by-row array:
 c0 0 c1 0 c2 c3 0 0 1

## Apply the Matrix
Execute
 $ xinput set-prop "Device Name" --type=float "Coordinate Transformation Matrix" c0 0 c1 0 c2 c3 0 0 1
e.g.
 $ xinput set-prop "Acer T230H" --type=float "Coordinate Transformation Matrix" 0.533333333 0 0 0 0.87804878 0.12195122 0 0 1
to calibrate your touchscreen device. Now, it should work properly.

## Do it automatically via a udev rule
Create a file something like  with contents like this:

{{hc|/etc/udev/rules.d/99-acer-touch.rules|2=
ENV{ID_VENDOR_ID}=="2149",ENV{ID_MODEL_ID}=="2703",ENV{WL_OUTPUT}="DVI1",ENV{LIBINPUT_CALIBRATION_MATRIX}="1 0 0  0 1 0"
}}

Substitute your own touchscreen's vendor ID, model ID, the xrandr output name, and the calibration matrix that you calculated above.  This is based on the assumption that you are using the libinput driver for your touchscreen.

## Wayland
Using  you can calibrate your touchscreen on Wayland compositors. See the libinput documentation.

If you have  installed, you can use the  utility to get the transformation matrix. You can then apply it using a udev rule.

## Troubleshooting
If, after following these instructions, multiple clicks occur in different places when you touch the screen, you will need to build the  package using the ABS, applying this patch before you build the package. (This patch fails on the current xorg source, but the bug is present on at least 1 system.)

## Using libinput
The  package provides a few utilities to debug input events:

* The  command provides a list of events emitted by all devices, including the touchscreen driver. You can use the  option to get more information.
*  provides a graphical debug environment. This can be useful to verify visually that the transformation matrix has the correct values.
*  lists all input devices. This can be useful to identify the name and eventual attributes of an input device. Using this command you can also verify that the transformation matrix was applied correctly.

For more information see the troubleshooting section of the libinput page.
