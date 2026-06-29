# Bus Pirate

The Bus Pirate is a versatile tool for communicating with various hardware.

Interfacing a new microchip can be a hassle. Breadboarding a circuit, writing code, hauling out the programmer, or maybe even prototyping a PCB. We never seem to get it right on the first try.

The Bus Pirate is a universal bus interface that talks to most chips from a PC serial terminal, eliminating a ton of early prototyping effort when working with new or unknown chips. Many serial protocols are supported at 0–5.5 volts, more can be added.

## Installation
The drivers for the FTDI chip is included in the kernel, so it should be detected as soon as it is plugged in, and assigned to device .
To check where it got assigned, run:

 # journalctl -k

The output will contain a line that looks something like this:

 # usb 1-4.4: FTDI USB Serial Device converter now attached to ttyUSB0

## Rename the device with udev
It can be annoying to have to look up what  the device gets assigned, so it is a good idea to add a simple udev rule that creates the symlink from  to  when it is plugged in.

To figure out the current path to the bus pirate you can use the  monitor command and then plugging in the device the output should be some thing like this:

After you have plugged it in and the output is given press  to break the text stream.

## Using the Product/Vendor ID
By using the Vendor/Product ID the bus pirate device can be replaced without needing to change the configuration again. To use this method, add the following lines:

{{hc|/etc/udev/rules.d/98-buspirate.rules|2=
# Bus pirate v3
SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", GROUP="users", MODE="0666", SYMLINK+="buspirate"
# Bus pirate v4
SUBSYSTEM=="tty", ATTRS{idVendor}=="04d8", ATTRS{idProduct}=="fb00", GROUP="users", MODE="0666", SYMLINK+="buspirate"
}}

## Using the serial number
You can also do it by serial number, to do this, you will need to find out the serial number of FTDI chip on the bus pirate. This can be achieved by running the following, assuming your device is plugged in:

 # udevadm info --attribute-walk -n /dev/ttyUSBX  | sed -n '/FTDI/,/serial/p'

Now add/create the following udev rule:

{{hc|/etc/udev/rules.d/98-buspirate.rules|2=
SUBSYSTEM=="tty", ATTRS{serial}=="MYSERIALNUMBER", GROUP="users", MODE="0660", SYMLINK+="buspirate"
}}

Load the new rule: at this point, whenever you plug in the device, the symlink should be created.

To verify that, run the udev monitor command mentioned above and it should report some thing like this:

 DEVLINKS=/dev/buspirate

## Communication
To communicate with the device, you can use any of the following, to name a few:

* :
 # minicom -b 115200 -8 -D /dev/buspirate
* :
 # screen /dev/buspirate 115200 8N1
* :
 # picocom -b 115200 /dev/buspirate
* cu from the  package:
 # cu -l /dev/buspirate

Type  and press  and the device should reply with a list of possible commands.
