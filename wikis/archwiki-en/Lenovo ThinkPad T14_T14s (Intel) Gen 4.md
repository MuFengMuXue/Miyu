# Lenovo ThinkPad T14/T14s (Intel) Gen 4

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| TrackPoint ||  ||
|-
| GPU (Intel) ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| Mobile broadband || ||
|-
| Fingerprint reader || ||
|-
| Smartcard Reader || ||
|}

The Lenovo ThinkPad T14/T14s (Intel) Gen 4 was introduced in May 2023. It features a 14" screen, 13th-gen Intel Core processors, and integrated Intel Iris Xe graphics. Everything seems to work pretty much out the box with kernel >=6.11.6.

To ensure you have this version, install the package  and run:

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
## Intel Turbo Boost Max
Check that Intel® Turbo Boost Max Technology 3.0 is enabled using

 $ cat /sys/devices/system/cpu/intel_pstate/no_turbo

An output of 1 means it is not enabled, so you will have to reset your BIOS to defaults. After doing that, running the command again should print 0.
You should be able to see your CPU boosting way higher.

## Sound
This laptop requires Sound Open Firmware for the internal sound card to work.

## Firmware
## fwupd
fwupd supports updating the UEFI BIOS, NVMe SSD, Embedded Controller, Intel Management Engine out of the box.

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
|  ||  ||  || Toggle keyboard backlight3
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# Works out of the box, but it can be controlled by software.

## Mobile broadband
See NetworkManager#Mobile broadband support.

## T14 links
* https://ubuntu.com/certified/202303-31392

## T14s links
* https://ubuntu.com/certified/202305-31639
