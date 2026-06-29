# Logitech G13

The Logitech G13 is a 25-key "advanced gameboard" from Logitech's Gaming series, with the intention of replacing the left half of your keyboard whilst gaming. It uses rubber dome key switches for the main 22-keys, mouse-like buttons for the two buttons around the joystick, a joystick (which can be pressed in), four Mode buttons, four option buttons, a menu button, and a backlight toggle.

## Installation
There are a couple options for drivers, but only one that appears to work well today:

* Running the official Logitech Gaming Software under Wine. Despite working fine, the software has a garbage rating on WineHQ, as it cannot actually communicate with USB devices (however, the reports available are quite old, and you may have better luck).
*  is a maintained driver and configuration tool with modern C++ & Java Codebase for the G13, forked from the older linux-g13-driver (see README for more information).
*  is an unmaintained user-space driver.

Both packages will install a g13d daemon and a systemd service that runs g13d as user/group . They will also set up rules for udev to identify your G13 device and automatic starting and stopping of the service by connecting or unplugging by default.

## Usage
After following the steps above, when you reboot and launch g13d (either manually or automatically through systemd), you should receive an image with a "linux inside" logo, "G13", and the GNU logo.

## Configuration
g13d is configured in one of two ways, either by writing commands to , or preferably by specifying keybindings and commands in a configuration file which is read at launch.

When running g13d manually you can specify a configuration file using the  parameter, and when running as a service the file  will be used.

Manual commands can also be evoked one at a time by manually writing to :

For example, to set the display a purple colour:

 $ echo "rgb 177 13 201" > /run/g13d/g13-0

g13 can also handle multiple commands at once:

 $ echo -e "rgb 177 13 201\nbind G4 KEY_W" > /run/g13d/g13-0

## Commands
## rgb
Set the backlight to an rgb colour, values are expressed in decimal from 0 to 255.

 rgb rrr ggg bbb

For example, to set the display green:

 rgb 0 255 0

## bind
Binds a G13 key. All keys are bound to  by default.

 bind g13key actual_key

For example, to setup WASD movement:

See below for how to configure this.

## mod
Sets the backlight status of M1, M2, M3, and MR.

 mod n

Where  is a bitmask. To find the desired state compute the sum of 1 (M1), 2 (M2), 4 (M3) and 8 (MR).

For example, to set M1, M3, and MR on, and turn M2 off (1+4+8=13):

 mod 13

## Keys
Since that can be less than explanatory, here is a diagram showing where the keys physically are on the device:
