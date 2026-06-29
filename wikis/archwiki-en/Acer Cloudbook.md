# Acer Cloudbook

At least four different versions of this laptop exist: AO1-131-C9PM and AO1-131-C620 with a 11" screen, and AO1-431-C2YR and AO1-431-C7F9 with a 14" screen. All of them also have slightly different hardware (e.g. wireless card).

## Hardware
Processor: Intel Celeron N3050 @ 1.60GHz

Video: Intel Corporation Device 22b1 (rev 21)

Audio: Intel Corporation Device 2284 (rev 21)

## AO1-431-C2YR
{| class="wikitable archwiki-table-laptop"
! Device !! Working?
|-
| Intel graphics ||
|-
| Wireless ||
|-
| Audio ||
|-
| Touchpad ||
|-
| Webcam ||
|-
| Card Reader ||
|-
| Bluetooth ||
|}

Wireless NIC: Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter 802.11b/g/n (rev 01)

## AO1-431-C7F9 (possibly)
Wireless NIC: Intel Corporation Dual Band Wireless AC 3160 (rev 83)

## BIOS configuration
* Touchpad: Basic
* Boot Mode: Legacy
* Boot priority order: the eMMC block device needs to have a lower boot priority than the USB bootable device.

Then save and exit.

## Kernel parameters
Without these options, the installation image will not load at all:
* edd=off
* noapic

Therefore these parameters needs to be added at the end of the kernel parameters' line of the boot launcher:
 linux /vmlinuz-linux ... edd=off noapic

## Installation
* Everything should function without any issues thanks to the previous kernel parameters, proceed to install the image as normal.
** The module for the wireless NIC is included with the kernel, so Wi-Fi works out of the box.
* Do not forget to add edd=off noapic to the kernel parameters of the boot launcher's configuration file.

## Installation (UEFI mode)
* No additional kernel parameters are needed.
* The UEFI firmware may be hardcoded to boot from Microsoft's EFI boot loader at  (tested on AO1-431-C2YR, BIOS 1.06)

## BIOS configuration
* Touchpad: Basic
* Boot Mode: UEFI
* Boot priority order: the eMMC block device needs to have a lower boot priority than the USB bootable device.
* Secure Boot: Disabled, or use BIOS menu to trust the Arch ISO boot loader.

Then save and exit.

## Troubleshooting
## GDM
If Gnome/GDM is installed and started, the login page will flicker up-to the point that it becomes nonfunctional. See GDM#Use Xorg backend.

## High load average on idle
The kernel module rtsx_usb_ms is loaded at boot time yet is non-functional (the kernel thread associated to the module when inspecting with top is a zombified process) and unnecessary for the system to function. The module can safely be blacklisted.

## Bluetooth
At least in AO1-431-C8G8 bluetooth device is deactivated via RF-kill by default. After activating it works flawlessly with bluez.
