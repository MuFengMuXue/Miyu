# ASUS Zenbook Pro UX501

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Webcam ||  ||
|-
| Touchpad || ||
|-
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Zenbook Pro UX501.

For general instructions see Laptop and comparable models from the summary page Laptop/ASUS and ASUS.

## Kernel options
To prevent random lock ups just before or as X loads, add the following option to your boot loader config:

 i915.enable_execlists=0

To get brightness media keys and brightness adjustment working, add the following:

 acpi_osi= acpi_backlight=native

To allow X to start without locking up when the GPU is powered down via bbswitch, replace the  above with:

 acpi_osi=! acpi_osi="Windows 2009"

## Microcode
Be sure to load the latest microcode alongside your kernel to prevent random lock ups while using the modesetting driver.

## Module configuration
Before trying out the fixes below make sure you system is completely up to date.

To fix noise headphone noise use  as explained in Advanced Linux Sound Architecture/Troubleshooting#Wrong model autodetection.

Restoring the laptop from suspend will bring the noise back. In order to fix this use https://github.com/dakatapetrov/zenbook-pro-ux501vw-sound-fix.

To enable power-saving functionality for the Intel graphics card create:

But be careful with . It may cause screen freezing.

## Fan control
To setup variable fan control, install the  package and load the  module at boot:

## Virtual terminal fonts
The 4K resolution causes the default virtual terminal font to be extremely small, and the loss of detail caused by the fact that the UX501 uses a false-4K Pentile display instead of a true-4K display can make it even more difficult to read.

See HiDPI#Linux console (tty), a good balance between size and readability is .

## Headphones not detected
To attempt to scan for your headphones again run:

 # alsactl restore

## Unable to boot installer (error: out of memory)
To fix this, download and install the latest BIOS update.
