# MacBookPro13,3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| Keyboard || PS/2 ||
|-
| Touchbar ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (AMD) ||  ||
|-
| Audio || ||
|-
| Microphone || ||
|-
| Thunderbolt ||  ||
|-
| Suspend || ||
|}

This page covers the following Apple models:

* MacBookPro13,3 15" Late 2016

This laptop has been vastly documented over at https://github.com/Dunedan/mbp-2016-linux

## Installation
Unless you have a local repository on a USB disk, you need a USB to Ethernet adapter or a USB wireless adapter supported natively by the kernel to easily install Arch Linux, since you have to configure the Wi-Fi as per #Wi-Fi via kernel parameters otherwise

## Accessibility
Macs such as this one generally have an intuitive way of booting to an Arch installation medium. Hold  as you are booting the laptop and it will open a graphical boot device selection screen.

The arrow keys are used to select between boot devices. Go to the selection that states EFI Boot with the icon of a USB drive after inserting the installation medium into the computer.

## Wi-Fi
The wireless card works out of the box with , however has bad performance unless you set kernel parameters as per Broadcom wireless#BCM43602 802.11ac Wireless LAN SoC

## Touchpad and keyboard
The touchpad and keyboard works out of the box. Note that the keyboard depended on the touchbar for its function keys which currently does not work.

The keyboard backlight does not work (no solution yet).

## Touchbar
Currently there is no support for the touchbar for T1-based MacBooks.

 shows the touchbar as an "Apple, Inc. Apple Mobile Device Mode":

## Audio
Audio from speakers and headphones do not work. External DACs for audio playback works fine otherwise.

## Suspend
Suspend / hibernate does not work. The problem seems to be the NVMe that does not wake up. A potential solution to this has been offered, at https://bbs.archlinux.org/viewtopic.php?pid=2176149#p2176149.

When booting from an external drive, suspend / hibernate works out of the box.

## Firmware
It is recommended to download the latest MacOS (Monteray) before wiping the device to install Linux on it. This will install the latest firmware for the Macbook.

fwupd supports this device and lists the following devices:
*

## Function keys
Normally, the Touchbar is used as function keys. As the touchbar currently does not work, there is no support for function keys.
