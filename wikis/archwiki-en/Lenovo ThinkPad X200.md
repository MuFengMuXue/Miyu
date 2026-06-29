# Lenovo ThinkPad X200

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Audio ||  ||
|-
| Bluetooth || ||
|-
| Ethernet ||  ||
|-
| Fingerprint reader || ||
|-
| GPU ||  ||
|-
| Keyboard || ||
|-
| SD-card reader || ||
|-
| Touchpad || ||
|-
| TPM || ||
|-
| Trackpoint || ||
|-
| Webcam ||  ||
|-
| rowspan="2" | Wi-Fi ||  ||
|-
|  ||
|}

## Firmware
## BIOS card whitelist removal
Like most ThinkPads, the X200(s) / X200T has an FCC enforced whitelist for wireless cards. This means if a third party wireless card is installed via Mini PCIe or PCMCIA slot, the system will not boot. However, there are many individuals who modify and distribute whitelist-free BIOS updates online.

The whitelist-free BIOS for the X200(s) can be found here and the whitelist-free BIOS for the X200T can be found here.

Make sure the BIOS version the system is running matches the cracked version being distributed.

For more information about BIOS flashing and system firmware, please see Flashing BIOS from Linux.

## Coreboot / Libreboot
Coreboot is a fast and flexible open source firmware solution to replace the system BIOS. The ThinkPad X200 is fully supported by Coreboot and good documentation can be found at the Libreboot project's official website. The X200s and X200 Tablet are also partially supported per the Libreboot X200 documentation.

## Fingerprint reader
Install fprint. Support depends on the model variant.

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
|  ||  ||  || Toggle the function of the numeric keys3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles the ThinkLight on T-series laptops.
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
|  ||  || 4 ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || (On Microsoft Windows) open the ThinkPad EasyEject Utility screen.
|-
|  ||  ||  ||
|-
|  ||  ||  || (On Microsoft Windows) enable the FullScreen Magnifier function.
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# The number lock works and is handled in firmware. This is opaque to the software and NmLk itself is not visible to . This is not the same as the number lock found on most keyboards, where the number lock key is visible to software, but keys pressed with the number lock toggled will have the keysym of a keypad key ( versus ).
# Unmarked but documented in the hardware maintenance manual.

## Mute button
If the mute button on the keyboard is not working, then be sure to add  to the kernel parameters.

## Tablet buttons
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
| Button 1 ||  ||  ||
|-
| Button 2 ||  ||  || Possibly changes screen rotation.
|-
| Button 3 ||  ||  || Possibly opens a menu.
|-
| Button 4 ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Screen rotation
The screen rotation hardware button does not work by default. The button must first be assigned to a free keycode. Then it can then be utilized with a script similar to the ones below.

Keycodes can be bound to the execution of scripts in many desktop environments' settings. Environment-independent X applications also exist such as xbindkeys and sxhkd.

## Sway
## Automatic screen rotation
Besides manually switching between vertical and horizontal orientation you probably also want sway to automatically flip the screen upside down when you fold the device into tablet mode. Add this to your sway configuration file:

## Screen rotation button
## X.org
## Hard disk shock protection
The ThinkPad X200 comes with an integrated 2-axis accelerometer providing the possibility of parking the hard drive's disk heads preventing from data loss due to heavy shocks. See HDAPS for details. It may be necessary to set correct invert parameter.

## Power management
To set up an efficient power saving environment, install the  package. A detailed guide how to implement a simplistic power saving environment based upon TLP can be found here.

Fan-control software can be used to further reduce power consumption.

Investigate Powertop and the  package from AUR for more information on measuring actual power consumption.

See Power saving for additional tips.

## Screen calibration
## Loading the correct ICC colour profile
Download x200.icc and move it to . Load the profile with  as follows:

 $ /usr/bin/xcalib -d :0 ~/.color/icc/x200.icc

## Calibrating the digitizer
If the stylus happens to be working very imprecisely, the screen may be in need of calibration. Installing  and running the following command will begin the calibration process.

 # xinput_calibrator --device "Serial Wacom Tablet WACf004 stylus"

To save the calibration settings, create a config file at  with the settings provided by xinput_calibrator.

## Wireless internet
The Thinkpad X200 and X200 Tablet can have any of the following wireless cards supplied by the factory:
* Condor Peak 1x2 HMC WIFI
* EchoPeak 1X2 HMC RUSSIA SKU (WiMAX/WIFI5150) for Russia
* Intel Centrino Wireless-N 1000, Advanced-N 6200, Advanced-N + WiMAx 6250, Ultimate-N 6300
* Intel WiFi Link 5100, 5300
* Intel WiMAX/WiFi Link 5150, 5350
* ThinkPad 11b/g/n Wireless LAN Mini-PCI Express Adapter II, III

All of which are supported by .

If connectivity problems such as a slow connection or aborts are experienced, especially when connected to a WPA2 Enterprise network, then try to load the iwlwifi module with the options , , , . There is no clear recommendation which of these options to be used as for some users  already solves the problem sufficiently, for others . See Wireless network configuration#iwlwifi for more detailed instructions.

## Troubleshooting
## Libreboot uneven backlight brightness problem
In some CCFL display panel libreboot fails to detect the correct PWM brightness value resulting in uneven backlight (summary). To fix this, you need to flash libreboot version 20210522 or newer (download) (warning libreboot 20210522 has a grub font & restart bug, altough shutdown is okay).

## Failed to execute '/usr/sbin/inputattach'
If you see the above error in your logs, copy  to  and comment out SUBSYSTEM of inputattach.

## System feels unresponsive
If your system feels unresponsive and lagging, you can try creating a file called :

 options drm_kms_helper poll=N

## Backlight fails to activate after system resume
On rare occasions the backlight may not activate after resuming. See Problem with display remaining black after resume for possible workarounds.

## PM device: Resume from hibernation error: Failed to restore -19
This is likely to be related to the tpm_tis and tpm modules not being properly unloaded before hibernation. These modules are required by the device listed in the error as 00:0a:

 # dmesg | grep 00:0a
 [    0.377877] pnp 00:0a: Plug and Play ACPI device, IDs PNP0c31 (active)
 [   10.746742] tpm_tis 00:0a: 1.2 TPM (device-id 0x1020, rev-id 6)
 [   10.746751] tpm_tis 00:0a: Intel iTPM workaround enabled
 [   10.866734] tpm_tis 00:0a: TPM is disabled/deactivated (0x6)

To unload the module create the following executable file called , assuming the use of the systemd hibernation procedure:

 #!/bin/sh
 case $1/$2 in
   pre/*)
     echo "Going to $2..."
     modprobe -r tpm
     modprobe -r tpm_tis
     ;;
   post/*)
     echo "Waking up from $2..."
     modprobe tpm
     modprobe tpm_tis
     ;;
 esac

## mei_me 0000:00:03.0: suspend
If you are seeing this error, a workaround is to blacklist the  and  modules. More information can be found here.

## pciehp 0000:00:1c.1:pcie04: Cannot add device at 0000:03:00
See #mei_me 0000:00:03.0: suspend.

## Uhhuh. NMI received for unknown reason 30.
The Thinkpad X200 is known to report the following error on resume from hibernation or suspension:

 Uhhuh. NMI received for unknown reason 30.
 Dazed and confused, but trying to continue
 Do you have a strange power saving mode enabled?

In this case you can disable the high precision event timer (HPET) by adding "nohpet" to your GRUB kernel parameter line.

## High pitched noises
The X200(s) is prone to high pitched, low volume noises originating from the CPU, usually in low power scenarios. One proved solution to this is to disable CPU power control in the BIOS.

High pitched noises may also be emitted from the display's inverter board on CCFL models. This is normal behavior and may or may not be present depending on how much energy the installed display draws.

For more information see == See also ==

* [https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/x200_x200s_x200si_x201_x201i_x201s_hmm_en_43y6632_11.pdf Thinkpad X200, X200s, X200si, X201, X201i, and X201s Hardware Maintenance Manual (12th ed)
* ThinkPad X200 Tablet and X201 Tablet Hardware Maintenance Manual (5th ed)
* Linux Hardware Database: Thinkpad X200 (All)
* Linux Hardware Database: Thinkpad X200 Tablet (All)
* Thinkwiki: X200 Overview
* Thinkwiki: X200 Tablet Overview
* ThinkWiki: How to reduce power consumption
* Trinity.moe: Thinkpad X200 Tablet
