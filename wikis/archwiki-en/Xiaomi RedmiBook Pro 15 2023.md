# Xiaomi RedmiBook Pro 15 2023

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth ||  ||
|}

This article covers the installation and configuration of Arch Linux on a RedmiBook Pro 15 2023 Ryzen edition laptop. Almost everything seems to work pretty much out the box.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Display
Color profile for display

## Fingerprint reader
Needs custom driver to work with fprintd

## S3 sleep / s2idle
S3 sleep is not supported. However, s2idle works out of the box and causes no problems with sleep / hibernation.

If you have trouble with waking up, see AMDGPU#Failure to suspend to RAM.

To get S3 to work, one needs to patch ACPI. You ma experience a white screen after wake up with this patch.

## Other ACPI issues
There is error on startup and amdgpu error is dmesg. But seems like theese errors does not touch functionality.

## Speakers
You can use Lenovo ThinkPad P14s (AMD) Gen 4#Speakers tweak to get better sound.

## Function keys
Additional keys by Xiaomi(Cut, settings, AI) needs DKMS driver.

## Other
Great optimization guide for this notebook
