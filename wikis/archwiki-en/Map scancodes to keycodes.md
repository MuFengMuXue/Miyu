# Map scancodes to keycodes

This page assumes that you have read Keyboard input, which provides wider context.

Mapping scancodes to keycodes is part of the keyboard driver's job Since this is achieved in a layer lower than Xorg, Wayland and the Linux console, it will be effective in all. [https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/input-event-codes.h#n64Note that this method can only be used for simple 1:1 key remaps; see Input remap utilities for programs which allow more complex remaps at a similar low level.

The scancode-keycode mapping table is stored in memory by the keyboard driver and any changes made are not persistent (i.e. when you unplug the device or reboot, all changes will be lost).

Systemd has a standardized way to make changes to the mapping table effectively permanent #Using udev. Udev provides an infrastructure to manage devices. That includes running udev rules (tiny scripts) when a device is attached to the computer. Some udev rules perform keyboard remapping using the udev hardware database as a source. With the hardware database, it's possible to target a specific keyboard model for scancode-keycode remappings.
Systemd uses this itself to assign "unknown scancodes" of many keyboard models to the correct keycode. That means your keys are recognized out of the box when your keyboard model has been found in the hardware database (the corresponding .hwdb file can be found under ).

Alternatively, you can automatically run remapping tools when your desktop session starts. For example, by #Using setkeycodes or #Using evmap.
But this way the remappings won't be applied when you plug your keyboard in after your system has booted up or when you reconnect your keyboard.

## Technical background
Since linux kernel version 2.6.37 there are 3 ioctl calls that can change one entry of the mapping table and 3 corresponding calls that can query one entry of the mapping table.
Namely,
*
* {{ic|ioctl(dev_fd, EVIOCSKEYCODE, (unsigned int[) {scancode, keycode})}}
*
modify a mapping table entry and
*
* {{ic|ioctl(dev_fd, EVIOCGKEYCODE, (unsigned int{scancode, keycode})}}
*
query a mapping table entry.
 is a file descriptor pointing to a virtual console (it doesn't matter which virtual console) and  is a file descriptor pointing to a device file.

The  and  ioctl calls are legacy calls because they are unreliable and it can be hard to predict which device they'll operate on. To be specific, they will iterate over connected devices that satisfy specific rules (which can also match devices that do not correspond to a physical keyboard) and return as soon as one device driver doesn't return an error when asked to remap/query a mapping entry. To make things more problematic, some device drivers may not return an error even though the call didn't have any effect, letting the ioctl call return successfully without any changes at all. The iteration's order is the order of initalization of the devices within the kernel (which is random for devices that were plugged in since boot) [https://elixir.bootlin.com/linux/v6.19/source/drivers/tty/vt/keyboard.c.

The legacy  ioctl and  ioctl calls are used by the tools  and .
The device-specific  ioctl calls are used by evmap.

## setkeycodes modifies user-given scancodes
Notice how setkeycodes wants to be helpful and substracts 0xdf80 (-0xe000 + 128) from every scancode bigger or equal to 0xe000 before calling ioctl.
But this may not be very helpful at all and is intransparent to users that want to remap, for example, an USB keyboard.
A scancode of an USB keyboard (to be exact, of the HID protocol) consists of a 16-Bit Usage Page and a 16-Bit Usage ID. The Usage Page for keyboard is 7, normally resulting in a large scancode in the form 0x0007XXXX for USB-keyboard keys. If one passes such a scancode to setkeycodes it modifies that scancode and makes it invalid, resulting in an error.

The reason why setkeycodes processes scancodes passed to it is a bit complicated and requires more background knowledge.

First of all, it's ambiguous what exactly a scancode is.
In this article a scancode is a number (i.e. byte array) that corresponds to a key on the keyboard and can be passed to the keyboard driver to query or set the corresponding keycode.
But this doesn't match the definition the scancode wikipedia article is giving.
According to the wikipedia article scancodes are (either all or a specific subset of) bytes that are transmitted from the keyboard when a key is pressed or released (refered to as protocol scancode from now on).
When a keyboard driver receives protocol scancodes from the keyboard it may or may not process them, before substituting them with a keycode.
In case the driver processes them, the resulting scancode will differ from the original protocol scancode (assuming the driver doesn't also process scancodes received from ioctl calls the same way).
To conclude, the difference between a protocol scancode and a scancode is that a protocol scancode can be more raw (unprocessed) than its corresponding scancode. For a given keyboard, scancodes are defined by the developer of the keyboard driver and protocol scancodes are defined by the protocol.

IBM's PS/2 protocol was the most widely used protocol for keyboards for the last few decades but is barely present nowadays.
Keyboards using PS/2 are handled by the atkbd driver which processes protocol scancodes to scancodes.
In most cases (to be exact, for set 1 and set 2 which are the most popular), PS/2 uses protocol scancodes of the form 0xe0XX for some keys which atkbd then substracts by 0xdf80 to be within the range 0x80 to 0xFF At the time when setkeycodes was written, PS/2 was the dominant keyboard protocol and people commonly used showkey to obtain PS/2 protocol scancodes.
setkeycodes took that into account and was therefore processing user-given PS/2 protocol scancodes into scancodes which are understood by the atkbd driver.
So the reason why setkeycodes is subtracting 0xdf80 is because setkeycodes matured as a keyboard remapping tool for PS/2 keyboards and didn't wanted to change its identity, even through PS/2 is barely present today; only occasionally used for internal laptop keyboards.

## Identifying scancodes
You need to know the scancodes of keys you wish to remap. See Keyboard input#Identifying scancodes for details.

## Using udev
You can use udev's hardware database to override the default scancodes-to-keycodes mapping by following udev#Remap specific device and the update/reload sections after.

## Using setkeycodes
 is a tool to update scancode-keycode mappings of a keyboard. It is best to use it with showkey. See Keyboard input#Using showkey and Keyboard input#Identifying keycodes in console.

Do note that setkeycodes only works as expected with xx and e0xx formatted hexadecimal scancodes. For USB keyboards that use larger scancodes you can do a little workaround by adding 0xdf80 to the scancode number before passing it to setkeycodes (for the reason see #setkeycodes modifies user-given scancodes).

setkeycodes usage is:

 # setkeycodes scancode1 keycode1 scancode2 keycode2 ...

Scancodes are given in hexadecimal (without a leading 0x prefix), keycodes in decimal.

As stated, just executing this command will result in non-persistent changes. The changes can be made permanent by creating a new service:

and enabling .

## Using evmap
[https://github.com/vovcat/evmap evmap is a tool similar to setkeycodes to update scancode-keycode mappings of a keyboard, but it's keyboard specific. That means it requires a device file path of the keyboard you want to apply the remapping on. You'd want to use the corresponding keyboard device file in the folder  since the device file names in here are generated using hardware information, meaning the names (usually) contain information unique to the specific device model they correspond to.

evmaps basic usage is:

 # evmap -d /dev/input/by-id/your-device-file-here -s scancode1=keycode1 -s scancode2=keycode2 ...

Scancodes are given in hexadecimal (without a leading 0x prefix), keycode numbers in decimal or hexadecimal (for which you need to prefix the number with 0x).
You need to pad scancodes to full bytes, e.g. 3 => 03, 23 => 23, 123 => 0123 (otherwise you'll get the non-descriptive error message ).

Instead of keycode numbers you can also use keycode names. You can print the list of all recognized keycode names with the command:

 gcc -E -dM -x c - ' | perl -ne 'if (/^\#define (KEY_(\w+))\s+\S+/) { print "$2\n" }'

As stated, just executing evmap will result in non-persistent changes. The changes can be made permanent by creating a new service:

and enabling .
