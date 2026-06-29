# Lenovo ThinkPad Edge E330

This article covers the Arch Linux support for the Lenovo ThinkPad Edge E330s laptop.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Webcam || ||
|-
| Card Reader || ||
|}

## Configuration
## Clickpad
In some cases it is necessary to create:

Also see: https://forums.lenovo.com/t5/Linux-Discussion/lenovo-e330-touchpad-problem-on-ubuntu-12-04-LTS-32-bit/td-p/1053541

## Jumping cursor on touchpad release
A jumping cursor when releasing the finger makes it impossible to hit small objects. Solved with  FingerHigh/Low:

## Troubleshooting
## Brightness control
Brightness can only be switched between darkest and brightest values using OS method.
The fix is to make the  kernel module control it: append  to the kernel line in the boot loader.
