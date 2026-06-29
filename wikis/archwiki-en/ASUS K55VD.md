# ASUS K55VD

{| class="wikitable archwiki-table-laptop"
|+ style="caption-side:bottom;" | 1. Use  for the driver
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Touchpad || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA)1 ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Express Card Reader ||  ||
|}

## Installation
By default, the MTRR size is not set correctly and the MDS bug is present. To set the MTRR size correctly and avoid memory loss, set the following kernel parameters:

 enable_mtrr_cleanup mtrr_spare_reg_nr=1 mtrr_gran_size=32M mtrr_chunk_size=128M

To mitigate MDS, add . The nosmt option disables simultaneous multi-threading so if the decrease in performance is too much, use  instead.

## Firmware
## BIOS update
BIOS updates are only done manually:
# Download the latest BIOS image
# Plug in a USB drive and format it to FAT32
## Find the USB drive's name with
## Install
## Format the USB drive to FAT32
# Copy  file to the USB drive
# Restart the PC and open BIOS with
# Get to the Advanced menu
# Select Start Easy Flash
# Select the  with arrow keys and enter.

## UEFI Shell
Few ASUS laptops (and also K55VD) provide an option called Launch EFI Shell from filesystem device. It is not accessible by default but can be accessible by following the given instructions at Unified Extensible Firmware Interface#Launching UEFI Shell

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# Redirects to , i.e. Windows default shortcut for changing Projection settings.
