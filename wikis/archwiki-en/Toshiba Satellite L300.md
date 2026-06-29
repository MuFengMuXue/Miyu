# Toshiba Satellite L300

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| SD-card reader || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| PCMCIA || ||
|-
| Modem || ||
|-
|}
This document applies to the entire L300 series, in particular the L300-OG1 and L300-12K.

If your laptop is eligible to a BIOS update and has a version lower than v2.20 you probably have fan control problems and the  key and PC speaker might not work. See below for a method to upgrade your BIOS.

## Accessibility
The appearance of the BIOS is pretty simple (blue or dark grey on a light grey background), so it might work well with OCR software. It is fully keyboard driven.

The BIOS is accessed with the  key, while  opens the boot device selection menu.

## Firmware
This device uses a BIOS, it will not be supported by fwupd and does not provide Secure Boot.

## BIOS upgrade
Most of the L300 and L305 series laptops come with the InsydeH2O BIOS version 1.50. This BIOS might results in a dead  key and an improperly controlled fan depending on the exact laptop model (i.e the L300-OG1 needs the BIOS update from 1.50 to 2.20, but on the L300-12K everything is working on version 1.50). Get the fan working properly especially if you wish to use suspend and/or hibernate. The dead  key problem however is not a show stopper. The upgraded BIOS will also mean the PC speaker will start working.
Ensure you get the correct file for your specific model: for example, the latest BIOS version (v2.20 since 2010) for the L300-OG1 is available from Dynabook Canada. Other models can be found starting at Dynabook global website, selecting the region it was sold in, going to the support section for discontinued products and entering either the serial number or choosing from the family/series/model drop-down menus.

This file is a Windows-only executable - it does not contain anything usable under DOS. Nor can this BIOS be flashed using the Linux  application. There are only two ways to flash the ROM with that file:

* Run the file as an executable under a Microsoft Windows environment or,
* Use the undocumented "brick" repair method (below) proposed by Toshiba.

As the first method is straightforward it will not be discussed here. Below is the alternate method outlined for Linux-only users:

# The  file is a  compressed file. Use the command  to extract.
# The only important file is the  file. Rename that file to .
# Copy the  file onto the root directory of a USB flash drive.
# Remove any inserted CD, the power cord, the battery, and the hard drive from your laptop.
# Insert the USB flash drive into a USB port on your laptop.
# Simultaneously hold down the  and  keys.
# Plug in the power cord to the laptop while still holding .
# Press the "Power On" button of laptop while still holding .
# The USB flash drive light should start to flash. You may now release the  keys after a few seconds.
# Leave the laptop for about 1 minute. The ROM is being flashed. Your laptop will eventually turn itself off and it may reboot.
# You may turn off laptop now if it has rebooted successfully. If it just turned itself off then continue...
# Unplug the power cord, remove the USB flash drive, replace the laptop hard drive and battery. Re-plug power cord.
# Reboot laptop and enter the BIOS setup using . You should see that it has successfully upgraded your BIOS.

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
|  ||  ||  || 3
|-
|  ||  ||  || 3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || See Touchpad Synaptics#Software toggle
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  ||
|-
|  ||  ||  || Marking looks like , untested outside of twm.
|-
|  ||  ||  || Marking looks like , untested outside of twm.
|-
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
# Before sending , toggles between secondary functions: either the numeric pad ( to , , , , ) or navigation keys (, , , , , , , ,  and ) while lighting up the corresponding LED on the keyboard.
