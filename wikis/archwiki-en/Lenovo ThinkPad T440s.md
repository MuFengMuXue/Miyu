# Lenovo ThinkPad T440s

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth (Intel) ||  ||
|-
| Bluetooth (Realtek) ||  ||
|-
| Webcam (Acer) ||  ||
|-
| rowspan="2" | Webcam (Chicony) ||  ||
|-
|  ||
|-
| Webcam (Lite-On) ||  ||
|-
| rowspan="2" | Ethernet ||  ||
|-
|  ||
|-
| Wi-Fi (Intel) ||  ||
|-
| Wi-Fi (Realtek) ||  ||
|-
| Wi-Fi (Ericsson) ||  ||
|-
| rowspan="2" | WWAN (Sierra) ||  ||
|-
|  ||
|-
| NFC || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad || ||
|-
| Touchscreen ||  ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo T440s laptop.

## Installation
Attempting to use Intel Platform Trusted technology (PTT) when booting in UEFI mode can sometimes prevent the boot loader's  file from being booted. Under Security > Security Chip in the ThinkPad Setup program, select Security Chip Selection > Discrete TPM and Security Chip > Inactive (or Disabled).

## Firmware
fwupd does not support this device yet.

## UEFI BIOS errors
See Lenovo ThinkPad T450(s)#UEFI BIOS errors; the T440s suffers from the same firmware errors as the T450/T450s.

## Tweaks
## Screen resolution and scaling
In order to use the real dpi value create the file ():

Otherwise the default resolution is set to 96dpi.

If you have a 1920x1080 FHD panel installed and find that text and UI elements are too small, it may interest you to consider using display scaling to adjust the size of UI elements to your preference. Integer HiDPI scaling is likely too excessive for a display of this resolution and size, so you will want to consider a fractional scaling solution.

## Touchpad
See T440s Clickpad fix which feels good! for a Touchpad Synaptics configuration which alters the "annoying" behaviour of the clickpad.

See also the recommended kernel parameter in Touchpad Synaptics#Touchpad does not work after resuming from hibernate/suspend.

## Updating the BIOS
See Flashing BIOS from Linux#Bootable optical disk emulation and Updating the BIOS on my ThinkPad T440.

## Wi-Fi
The kernel's  driver for the Realtek Wi-Fi card may have spotty performance, especially when compared to the  driver for the Intel Wi-Fi card. The lwfinger/rtl8192ee repository on GitHub provides an "alternate (vendor) driver for RTL8192EE":

:May offer much better performance than the kernel rtl8192ee driver, especially when used as Access Point.
:Still, it will, with difficulty, barely surpass 50Mbps of uplink, in the best conditions.

Installation instructions can be found in the repository's README.md file. The alternate driver can also be installed with DKMS. See Dynamic Kernel Module Support for more details.

See also https://linux-hardware.org/?id=pci:10ec-818b-10ec-001b.

## SD card reader
The  driver for the Realtek RTS5227 media/SD card reader does not appear to work for all SD cards. MicroSDXC cards in particular may be problematic. Installing the  package instead resolves this issue. Note that a reboot is required after installing.

See also https://linux-hardware.org/?id=pci:10ec-5227-17aa-220c.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
