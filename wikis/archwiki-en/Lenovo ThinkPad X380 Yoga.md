# Lenovo ThinkPad X380 Yoga

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Graphics ||  ||
|-
| Multi-touch sensor and Pen ||  ||
|-
| Ethernet ||  ||
|-
| WLAN ||  ||
|-
| Bluetooth ||  ||
|-
| WWAN ||  ||
|-
| SIM Card ||  ||
|-
| Smart Card Reader||  ||
|-
| Media Reader ||  ||
|-
| Camera ||  ||
|-
| IR Camera ||  ||
|-
| Light Sensor ||  ||
|-
| G-Sensor ||  ||
|-
| Gyroscope ||  ||
|-
| NFC Reader ||  ||
|-
| Fingerprint Reader ||  ||
|}

The Lenovo ThinkPad X380 Yoga is a versatile 2-in-1 laptop featuring an 8th Gen Intel Core processor, a comfortable keyboard, and a rechargeable stylus. It has a 13.3-inch display and is designed for business use, though its battery life may not be as long as some competitors.

To verify you have the correct version, install the package  and run:

## Firmware
In August of 2018 Lenovo has joined the Linux Vendor Firmware Service (LVFS) project, which enables firmware updates from within the OS.
BIOS updates (and possibly other firmware such as the Thunderbolt controller) can be queried for and installed through fwupd.

## Installation
Disable Secure Boot in the BIOS to boot from a USB stick.

When installing Arch Linux onto this laptop, there are some recommended packages to get the best out of your device.

## Drivers and modules
Most notable your drivers. This laptop comes with the Intel UHD Graphics 620 and a 8th Generation Intel Core i5/i7 Processor. For the processor, install the  package. For the iGPU, refer to the Intel graphics.

The tp_smapi kernel modules are also recommended.

## Touchscreen and stylus
One of the advantages of this laptop is the seamless use of it's touchscreen and stylus. To get both of them working, you need to install a few packages. For the touchscreen and stylus install these packages: ,  and .

## Fingerprint reader
The  driver is required for the fingerprint reader to function. Use  to test and register a print.

## Power management
There are multiple power managers that can be used. The best results were reported with , but TLP did good as well.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Unknown
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Unknown
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggle Keyboard Backlight
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Issues
There have been reports of users not being able to control the fan using the  package. The fan does function nevertheless, it starts spinning usually when the CPU hits above 65°C, otherwise the fan remains inactive.
