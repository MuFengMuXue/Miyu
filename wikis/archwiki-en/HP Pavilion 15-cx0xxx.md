# HP Pavilion 15-cx0xxx

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Audio ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Touchpad || ||
|-
| Card reader ||  ||
|-
| Webcam ||  ||
|}

This article covers specific configuration of this laptop.

## Installation
You have to disable Secure Boot. repeatedly press F10 during boot to bring up the BIOS setup, navigate to the boot section and disable Secure Boot.

To prevent the system from booting in Legacy mode, i also recommend to disable CSM/Legacy mode

## Bluetooth
Works out of the box. You may have issues after suspend or a quick reboot. To fix this poweroff the laptop and wait 20 seconds until turning on.

## Card reader
Detected in kernel versions 5.6 and newer. If mounting the card does not work try booting with the kernel parameter  and/or with the kernel parameter .

## Function keys
All media keys work. In order to get the mute LED to work you need to load the  module with the  parameter. This can be done by creating the file:

## Hybrid Graphics
Works with PRIME GPU Offloading with nouveau, and Reverse PRIME with the proprietary NVIDIA drivers.

## Hpfall
Not tested, but  can be used to detect falls and park the hard drive

## Secure Boot
Secure Boot, if set properly works with GRUB and shim.

It works, but UEFI is an absolute mess so I would not recommend anyone getting too deep

## Other
The system will not allow changing to boot order when there is BIOS administrator password set.
