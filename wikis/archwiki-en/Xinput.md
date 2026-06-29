# Xinput

xinput is a utility to configure and test X input devices, such as mice, keyboards, and touchpads. It is found in the  package.

## Usage
## List devices
To list what xinput devices are available, use:

A  may be identified by its name () or ID ().

When being executed in a startup script, it is recommended that you use the name, as the ID may change following a reboot and lead to inconsistencies.

## List properties
To list all the properties of a device that can be set, use the following command:

 $ xinput list-props device

This may yield results like such:

Each  can be identified using its name () or number ().

As with devices, it is recommended to use the name in startup scripts, as the ID may change, albeit less often.

## Set device properties
Properties of devices can be set one or more (up to three) values. The syntax for setting a property to a value is:

 $ xinput set-prop device property values

Where  is replaced with the value(s) of the property.

For an instance, to enable tapping with the above output. Either of the following commands could be used:

 $ xinput set-prop "DELL0ABC:DE F123:4567 Touchpad" "libinput Tapping Enabled" 1

or

 $ xinput set-prop 10 338 1

On success, no output should be produced.

## Usage examples
Below are some of the ways xinput can be used.

## Remove the middle and right mouse buttons
 $ xinput set-button-map mouse-device 1 1 1

The above command will make middle and right mouse button to function like the left button. Putting zeros will disable them.

 $ xinput set-button-map mouse-device 1 0 0
