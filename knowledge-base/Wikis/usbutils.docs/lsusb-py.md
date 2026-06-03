# NAME

lsusb.py - list USB devices

# SYNOPSIS

**lsusb.py** \[ *options* \]

# DESCRIPTION

**lsusb.py** is a utility for displaying information about USB buses in the system and the devices connected to them. It uses the **usb.ids** file to associate a human-readable name to the vendor and product IDs.

In comparison with **lsusb**(8), this program can display additional information such as the interface speed of a device, and details of a device's interfaces including the driver bound to them and Linux devices provided by the driver, and the details of device and interface endpoints.

# OPTIONS

**-h**, **--help**
Displays options supported by **lsusb**(1).

**-i**, **--interfaces**
Display information about the interfaces of each device, excluding hubs.

**-I**, **--hub-interfaces**
Display information about the interfaces of each device, including hubs., excluding hubs.

**-u**, **--hide-empty-hubs**
Suppress information about hubs that have no devices connected.

**-U**, **--hide-hubs**
Suppress information about hubs, even if they have devices connected.

**-c**, **--color**
Use color

**-C**, **--no-color**
Don't use color

**-e**, **--endpoints**
Include information about device (and interface, with **-i**) endpoints.

**-f**, **--usbids-path**
Overrides the path of the **usb.ids** file.

# SEE ALSO

**lspci**(8), **lsusb**(8), **usbview**(8).

# AUTHOR

Thomas Sailer, \<sailer@ife.ee.ethz.ch\>, Sam Morris \<sam@robots.org.uk\>.
