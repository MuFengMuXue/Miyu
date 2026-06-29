# Lenovo ThinkPad T14/T14s (Intel) Gen 5

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| TrackPoint ||  ||
|-
| Touch screen ||  ||
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
| NPU ||  ||
|}

The Lenovo ThinkPad T14/T14s (Intel) Gen 5 was introduced in July 2024. It features a 14" screen, 1st generation Intel Core Ultra processors, and integrated Intel Arc graphics. Everything works out the box with kernel >=6.12.

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

## T14 links
* https://ubuntu.com/certified/202405-34010

## T14s links
* https://ubuntu.com/certified/202404-33920/22.04%20LTS

## Linux Hardware Database probe
This includes detailed hardware information, including vendor IDs.

* https://linux-hardware.org/?probe=29fa2f4fdf
