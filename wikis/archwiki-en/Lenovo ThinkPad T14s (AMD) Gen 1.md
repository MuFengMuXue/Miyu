# Lenovo ThinkPad T14s (AMD) Gen 1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wi-Fi || ||
|-
| Audio || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Mobile broadband || ||
|-
| Bluetooth ||  ||
|-
| Smartcard reader ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo Thinkpad T14s (AMD) Gen 1 laptop.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
Updating the firmware using the fwupd utility works as long as all the relevant options are enabled in the BIOS (Enable Windows Update UEFI Update). A BIOS update Bootable CD ISO that is OS agnostic may be downloaded from https://pcsupport.lenovo.com/.

The UEFI BIOS can also be updated without using fwupd; see Flashing BIOS from Linux#Bootable optical disk emulation for more information (and heed the warning at the top of the article). A charged battery and AC power are required for a successful update. Avoid having any addons/docks plugged in when performing the BIOS update.

## Secure boot
This is a problem that is similar to one which has been reported on some other Lenovo laptops and is likely due to a faulty firmware. If the device is stuck in a boot loop after replacing the Secure Boot keys, the only way to repair it is by replacing the mainboard of the device. Hopefully, the issue will get fixed with a firmware update in the future.

## Fingerprint sensor
The fingerprint sensor works: use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader".

fprint has more details on how to setup the fingerprint, for PAM-based authentication for example.

If the fingerprint reader is not detected by fwupd but is detected by  you will need to reset the fingerprint reader in the UEFI.

## Backlight
Backlight works correctly by manipulating the values, between 0-255, inside  or using a backlight managing utility.

## Smartcard reader
Seems to work and read cards. Following instructions from smartcards.

## Power management
## Enabling S3 sleep
For Suspend to work as expected, in the UEFI setup, under Config > Power set the option Sleep State to Linux.

Reboot and verify whether deep sleep is available, as explained in Power management/Suspend and hibernate#Changing suspend method.

## Mobile broadband
The only supported WWAN card is the Fibocom L850-GL, a PCIe card without any Linux drivers (and most probably never will get any, it is an Apple owned chipset now). All the existing WWAN workaround involve flashing a Sierra Wireless (Qualcomm) WWAN to escape the BIOS whitelist by enumerating slowly. This however does not work in the T14s, the card is entirely disabled and not even visible in lsusb. It is possible that the USB lanes are disabled on the M.2 port.

There exists an alpha-quality driver for the Fibocom L850-GL. The L860 is not proposed in the T14s AMD but is in the T14s Intel and a Linux mainline driver is being worked on by Lenovo for it. See Xmm7360-pci for more information.

## Wireless
See Lenovo ThinkPad T14 (AMD) Gen 1#Wireless

## Microphone
The microphone may not be operational. A possible fix is to blacklist the  module (to allow newer kernels to use ?)

## Webcam
The webcam needs the  USB 3.0 chipset firmware.

## Install videos
* T14s Arch video playlist
