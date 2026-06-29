# Logitech Racing Wheel

This article describes how to set up a Logitech racing wheel, such as a Formula Force GP or a G27/G29 racing wheel, with Arch Linux.

## Installing
## Identifying
When the wheel is plugged in, the following commands can be used to identify the wheel:

If using a Logitech Wheel, make sure it is set to PS3 mode otherwise it will not work.

## Checking input device
If you do not see your Logitech listed as an input device, you need to install  package. Please memorize the Handlers, here event15 and js0, as these will be necessary to call the tools for testing and configuring the wheel.

## Testing
For testing the wheel there are multiple tools that can be accessed via the command-line. One common tool is  which can be installed via the  or the  packages. An alternative is  which can be installed via the  package. A graphical version of  is available in the AUR as .

To test the wheel with  simply call it with the device handler (in this case with a G29 wheel and js0):

Whenever the input is changed,  will print the full state of the device. In case that only events should be displayed,  can be added as flag.

When using  for testing, instead of the js0 as device handler eventX is needed, which in this case is event15 for a Formula Force GP wheel.  then shows the events coming from the wheel:

, which is provided by , can be used to test the force feedback. The wheel should start to oscillate:

## Configuration
## Oversteer
Logitech wheels can be configured via the  tool from the  package. For general gamepad or joystick settings that may also apply to Logitech wheels, please refer to the Gamepad wiki page.

As of version 0.6.0,  contains compatibility modes for the following wheels:

* Driving Force / Formula EX
* Driving Force Pro
* Driving Force GT
* G25 Racing Wheel
* G27 Racing Wheel
* G29 Racing Wheel

Besides testing the wheel,  allows to configure the following aspects of the wheels:

* Steering hardware lock (in degrees)
* Combining pedals into one axis
* Global force feedback strength
* Manual auto-center force

## new-lg4ff
For older wheels, that use the driver lg4ff and Logitech Classic HID mode, additional settings might be enabled by installing the  device driver. Especially the steering hardware lock is useful in certain racing games such as F1 2017 and Dirt Rally to allow for a more realistic steering experience by setting the hardware lock angle to the value of the actual vehicle (e.g. 360 for F1 cars and 540 for modern rally cars).

Recent wheels, such as the G920, and the G923 Xbox edition, use the new HID++ protocol and hid_logitech_hidpp Logitech driver, and are not compatible with new-lg4ff.

## Wheel specific configuration
## Logitech G923 Xbox Edition
This racing wheel requires signals to be sent to change its usb mode every time it is plugged in. To accomplish this:
* Install
* When the wheel is plugged in run:

 # usb_modeswitch -v 046d -p c26d -M 0f00010142 -C 0x03 -m 01 -r 81

The wheel will then reset itself to the centered position and be available as a racing wheel in games.

## Games
## Flatout 2
The Wheel works without any wine configuration in flatout2. Just the following in-game configuration is needed:

* Force Feedback: On
* Force level: 100%
* Sensitivity: 100%
* Deadzone: 0%
* Controller: Logitech Inc...

* Throttle: Y-Axis left
* Brake: Y-Axis right
* Steer left: X-axis left
* Steer right: X-axis right

## rFactor 2
rFactor 2 does not have functional force feedback with the built-in lg4ff driver (for wheels that use the hid_logitech_hidpp driver, it works as expected). To make it work, the aforementioned  driver must be installed. The driver may not load after rebooting. You can check in the journal:

 logitech 0003:046D:C24F.000B: Force feedback support for Logitech Gaming Wheels (0.2b)

If there is no version number written after  and the FFB still does not work, the driver likely has not loaded and you will need to regenerate the initramfs.

After that, the FFB should work, but it may be inverted. You can fix this by going to  and editing . Find line  and invert its value (typically going from  to ).
