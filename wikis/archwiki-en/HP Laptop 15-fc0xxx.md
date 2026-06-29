# HP Laptop 15-fc0xxx

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Graphics ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam || ||
|-
| Audio ||  ||
|-
| Touchpad || ||
|}

This page covers the installation and configuration of the HP Laptop 15-fc0xxx.

## Installation
This laptop ships with Secure Boot enabled. It must be disabled in the BIOS (accessed via ) to boot the Arch Linux ISO.

## Graphics
The AMDGPU driver is required. For optimal performance, install the  and  packages.

## Firmware
The  package is required for CPU stability. It is also highly recommended to ensure  is installed for Wi-Fi and Bluetooth support.

## Network
The Realtek  is supported by the kernel-tree driver . If performance is unstable or Wi-Fi 6 issues occur, consider testing the  package from the AUR.

## Audio
Audio works out of the box using  and .

## Function keys
{| class="wikitable"
! Key !! Visible? !! Function !! Command
|-
|  ||  || Mute ||
|-
|  ||  || Volume Down ||
|-
|  ||  || Volume Up ||
|-
|  ||  || Mic Mute ||
|-
|  ||  || Brightness Down ||
|-
|  ||  || Brightness Up ||
|}
