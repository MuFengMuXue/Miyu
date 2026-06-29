# Dell Latitude E7440

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| SD Card reader ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  || ?
|-
| Fingerprint reader || ||
|-
|}
The Dell Latitude E7440 is a business Ultrabook™. Generally speaking, it has nice support of (Arch) Linux.

## Installation
## Update the firmware
The firmware update process does not need an operating system and it can be done with the BIOS utilities of the laptop. A USB flash drive can be prepared on another computer. The latest BIOS firmware, which is an .exe file, can be downloaded from the Dell website. On Windows, the firmware can be burned with Rufus into a bootable USB flash drive. USB Flash drive can be made UEFI/GPT bootable. After the USB flash is prepared, plug the USB flash stick, boot the laptop by pressing  and follow the instructions to boot the USB flash. After the firmware update, during reboot press  and check whether the shown BIOS version is the one which is burned.

## Secure Boot
The Arch Linux kernel is not signed by default, thus it cannot be booted if Secure Boot is enabled in the BIOS. If you want to use the Secure Boot, see Secure Boot to prepare the kernel. The signed kernel itself can be booted by a signed boot loader, e.g.  from Ubuntu.

## Drivers
* Intel graphics for HD4400 graphics card.
* Wireless#iwlwifi for Intel 7260 Wi-Fi card. This driver is from Intel and also part of the Arch Linux package repository.
* Synaptics for Touchpad
* Fan speed control#Dell laptops to control fan speed. There is only one fan on this laptop, detected on the right. Do not forget to disable BIOS fan speed control to be able to use custom fan speed config.

## What does not work
* Webcam does not work with Virtualbox (as of 4.3.6-1), but it works with native programs.
* There is no driver for the fingerprint sensor.
* Occasionally crashes/freezes/hangs when docked and then changing display modes
** Tested with Dell E-Port Plus II, using two external monitors together with the laptop display (three displays total)
*  cannot read the temperature of the hard disk. Use  instead.
* As of August 2019, there is no known way how to update the firmware of the SSD. Also not known where to find the most up-to-date firmware.

## Troubleshooting
## "Invalid partition table!" when booting
If you use BIOS+MBR boot method and msdos partition table, the BIOS may show this error message before entering Syslinux or other boot loaders. To bypass it, press . To prevent it, put the "boot" flag on a primary partition (instead of a logical partition). You may refer to the wiki page of your boot loader to see how this works. It may be a "kindly reminder" to Windows users, since Windows can only boot on primary partitions.

## Freeze before going to suspend when lid is closed
This seems to be related to https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1301601.
Workaround 2 helps decrease frequency of freezes. Create:

## Wi-Fi problems with Bluetooth enabled
Severe Wi-Fi problems (decreasing traffic, connection drops) with Bluetooth enabled. Workaround is to switch it off when not needed. This bug seems to be router-specific (e.g. with a Fritzbox).

## Wi-Fi problems when coming back from suspend state
When your Wi-Fi is gone after resume try going to BIOS and deactivate the functionality to turn Wi-Fi and WWAN down when an Ethernet cable is connected.
