# Lenovo ThinkPad T25

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Mobile broadband || ||
|-
| Webcam || ||
|-
| IR Camera || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Fingerprint Reader || ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo T25 Anniversary Edition laptop. It is based on the Lenovo T470 laptop so most of the hardware is identical and therefore should work like the T470.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware (e.g. bios and peripherals)
As of writing, the current BIOS version is 1.54. By visiting the downloads section (T25) an ISO can be downloaded and burned to disk which will perform the update from Lenovo. Or extracted and copied on a USB Stick.

## Kernel and hardware support
Hardware video acceleration with Kaby Lake seems to work fine via va-api.

As noted in Intel graphics, the  driver seems to cause more issue than the builtin  Xorg driver.
Works fine without the intel driver (on a Skylake configuration).

138a:0097 will hopefully be supported as part of Validity90.
Since the hardware is the same as in the T470 model, the fingerprint reader guide probably will work.

## Screen backlight
With the  driver ( the  brightness control is not working.
It is possible that, with the good  kernel parameters, the backlight related keys do their job.

Other workaround exists, such as described on this post or in the wiki acpid#Enabling backlight control.
Using the  package as a  replacement works well.
You can also check this repository as a base to add the ACPI rules to call  when backlight keys are pressed.

## UEFI boot
After configuring the BIOS setup to allow UEFI boot (either UEFI only or both), it works flawlessly.

## Special buttons
See Laptop/Lenovo#Special buttons, an additional key has to be added for this model:

{| class="wikitable"  style="text-align:center"
|-
! Key combination !! Scancode !! Keycode
|-
|  ||  ||
|}

## Touchpad and trackpoint
Touchpad and trackpoint share bandwidth, so using them at the same time makes trackpoint slow, jumpy, and abrupt. Disabling the touchpad either in BIOS or via xinput does not fix the problem, so the trackpoint becomes unusable each time the touchpad is occasionally touched.

The touchpad is also accessible over secondary bus (SMBUS/RMI), allowing to leave the full bandwidth for the trackpoint. The kernel source code contains the whitelist of supported devices, which does not include LEN008e (T25 touchpad). You can enforce this feature setting  parameter of  module to . For instance, using the kernel command line: .
