# I2C

I²C or I2C (Inter-IC) is a synchronous, multi-controller/multi-target (controller/target), packet switched, single-ended, serial communication bus invented in 1982 by Philips Semiconductors.

It is used by many hardware boards to communicate with general purpose I/O (GPIO) devices.

A similar extension of I2C is SMBus which is more specifically used for hardware monitoring purposes.

## Installation
I2C kernel modules already exist in most default kernel packages.

Userspace tools can be installed from . Bleeding edge is on .

SMBus-specific tools can be installed from .

## Module loading
In some cases it might be required to load the module at boot:

This will not be needed after  is fixed.

Depending on your system and usage, other hardware-specific modules such as  or  might have to be loaded as well.

If the modules are properly loaded, you should see the  devices.

Permission for using the  devices can be granted by adding the user to the  user group.

## Usage
 can detect all the active I2C devices:

When an I2C device is connected to a known bus,  can probe it for active addresses:

Be wary that this program can confuse your I2C bus, cause data loss and worse.
