# Acer Predator Helios Neo 16 PHN16-71

Acer Predator Helios Neo 16

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| MicroSD-card reader || ||
|-
| Speakers || ||
|-
| Microphone || ||
|-
| 3.5mm audio port || ||
|-
| Fan-control || ||
|-
| Keyboard RGB color || ||
|}

## Hardware
This is as of 2025-11-30, kernel version 6.17.9.

## 3.5mm audio port
The port is able to output audio but is unable to receive inputs from a headset mic with the default settings.

After some testing, using the following kernel module parameters lets a headset microphone input be detected, but it disables the in-built laptop microphone.

## Fan control and RGB
On Windows, the fan speed and the color for the keyboard RGB backlight can be set using the proprietary Predator Sense software. There is no equivalent for this software offered by Acer for Linux.

But there are third-party kernel modules that provide fan-control and RGB functionality. These include:
* Linuwu-Sense (an unofficial Linux kernel module for Acer gaming RGB keyboard backlight and Turbo mode for Acer Predator/Nitro), which is tested and working on this model.
* acer-predator-turbo-and-rgb-keyboard-linux-module (status for this model currently unknown; some users have reported it working for them)

## Accessibility
Press the F2 key during boot to enter the simplified UEFI menu. Press F1 to enter the "Advanced" settings and maneuver to the "Boot" category (listed on the left side of the screen). There, the boot order can be changed, and Secure Boot can be disabled.

## Firmware
fwupd does not support this device.

## Function Keys
{| class="wikitable"
|-
! Key
! Visible?
! Marked?
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 1 ||  || Locks screen
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Display toggle
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  /
|-
|  ||  ||  || Dim keyboard backlight
|-
|  ||  ||  || Brighten keyboard backlight
|-
|  ||  ||  || Turns on/off  key. Also (unintentionally?) triggers  when turning  key off.
|}

# Does not seem to be disabled by inhibiting ,,,, or  keys.
