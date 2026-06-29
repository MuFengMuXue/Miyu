# Lenovo IdeaPad S205

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Card reader ||  ||
|}

## Firmware
The IdeaPad uses a system firmware based on the SecureCore Tiano Platform. It supports UEFI and Legacy booting, but you cannot manually switch between them; which one is used depends whether the disk is partitioned as GPT or MBR. It does not have secure boot.

The firmware has many bugs. If anything related to it does not work, try loading setup defaults.

## Installation
Follow the Installation guide until boot loader installation.

You can not use the GUID Partition Table and still boot using legacy BIOS. If your desired partition layout does not work for MBR you must use UEFI.

## UEFI
While installing the boot loader, you might get the error:

 Failed to create EFI Boot variable entry: No space left on device

The firmware wants the .efi-file to be the UEFI default loader, see UEFI#UEFI boot loader does not show up in firmware menu.

## Wi-Fi
If you are using UEFI, your device might show up as hard blocked. This is due to a bug in the firmware.
You can fix it by doing the following things:

# Go into system firmware settings and reload factory defaults
# If Wi-Fi still does not work, change the boot order so that it boots from PXE (PCI LAN) before booting from Hard Drive.
