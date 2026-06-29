# Lenovo ThinkPad T495s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
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
| Smartcard Reader ||  ||
|-
|}

This article covers the installation and configuration of Arch Linux on a Lenovo T495s laptop.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Fingerprint reader
The fingerprint reader works: use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader".

fprint has more details on how to setup the fingerprint, for PAM-based authentication for example.

## Backlight
Backlight works correctly by manipulating the values, between 0-255, inside  or using a backlight managing utility.

 requires masking as it seems to be triggered and fails on boot.

## Firmware
Although the fwupd utility works to update some of the components, Lenovo does not support BIOS updates for the T495s yet. A BIOS update Bootable CD iso that is OS agnostic may be downloaded from Lenovo supporthttps://pcsupport.lenovo.com/.
