# Lenovo IdeaPad Flex 5 14IAU7

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen || ||
|-
| Fingerprint reader ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|-
| Accelerometer || ||
|-
| TPM ||  ||
|}

The Lenovo IdeaPad Flex 5 14IAU7 is a convertible 2-in-1 laptop computer with a 14" touch enabled display, powered by a 12th Gen Intel CPU with integrated graphics.

## Installation
To boot into BIOS:

To bring up the boot entry selection menu:

Remember that in order to be able to boot from external USB, the following BIOS settings have to temporarily be adjusted as follows:

* Security > Device Guard (Disabled)
* Security > Natural File Guard (Disabled)
* Boot > USB boot (Enabled)

## Touch screen and pen
The touchscreen and pen are recognized by the input-wacom driver. For setup information look at Wacom. Pens that use the MPP 2.0 (Microsoft Pen Protocol 2.0) are not compatible with this device.

## Firmware
Lenovo provides .exe files for updating the BIOS and the Intel ME firmware. There is no way to update these through BIOS itself. These firmware updates are not available through LVFS so updating through fwupd is not an option. The only update that comes through LVFS is the UEFI keys database (for device: UEFI dbx).

As of March 2024 and fwupd version 1.9.15, flashing the BIOS update through Linux is not working. Using  to extract the contents of the BIOS firmware update file and trying to flash the .CAP file with  would be an idea of doing this, but is still failing after rebooting to fwupd for the update process.

The easiest way to update is by booting a Windows OS and running the .exe files. For example:

* Dual Boot Windows 10/11, then run the update.
* Have Windows 11 installed in an external SSD or USB-stick and boot from it, then run the update.
* Create your own Windows PE USB-stick (or image and use it for example with Ventoy), boot it, then run the update.
*  Grab a ready Windows PE image (like Hiren's BootCD) and flash it to a USB-stick (or use it for example with Ventoy), boot it, then run the update.

Keep in mind that the "Intel Management Engine Interface Driver" needs to be installed before running the Intel ME firmware update, so remember to download it and have it accessible for install to the temporary Windows PE environment, every time you intent to update the Intel ME firmware.

The BIOS update has no driver prerequisites.

## Fingerprint sensor
The fingerprint sensor is currently not supported by the official libfprint driver. However, there is a custom libfprint build that supports it (, Source code. A prerequisite for the custom driver to work is to flash the fingerprint sensor with goodix-fp-dump, which is a custom firmware for it.

Remember that, if you dual boot Windows 10 or 11, Windows is going to replace the original firmware of the fingerprint sensor at boot. If you want to disable this behavior, you can go to Device Manager in Windows and disable the fingerprint sensor device. This way, the fingerprint sensor firmware is going to remain untouched by Windows and the sensor is going to continue working on Linux. So, in practice, one has to choose which OS the fingerprint sensor is going to work with.
