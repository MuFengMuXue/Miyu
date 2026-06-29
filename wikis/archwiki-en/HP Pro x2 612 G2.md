# HP Pro x2 612 G2

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Mobile Broadband ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchscreen || ||
|-
| Webcam ||  ||
|-
| SD Card Reader ||  ||
|-
| Finger Print Scanner || ||
|-
| Smart Card Reader ||  ||
|-
| Ambient light sensor || ||
|-
| Acceleration sensorMagnetometerGyro || ||
|}

This page is basing on the L5H60EA#ABD version of HP Pro x2 612 G2, it should also work with the other versions. Current UEFI version is 1.0.5.

This page covers the current status of hardware support, pre-installation system configuration tweaks, as well as post-installation recommendations to improve the usability of the system.

The installation process does not differ from any other PC. For installation help please see the Installation guide and UEFI. To set up a dual boot configuration with Windows, refer to Dual boot with Windows.

## Installation
Prior to installation, access the system UEFI firmware by pressing  during boot.

* Secure Boot: disable

Installation of Arch can proceed normally. Refer to the Installation guide for more info.

## Graphics
The HP Pro x2 612 G2 has Intel HD Graphics 615 integrated graphics, see Intel graphics for details.

## Power management
Battery life can be improved by installing  and calibrating it. See Powertop for more info.

It is also possible to deactivate some devices and ports in the UEFI.

* Advanced > Build-In Device options (Example: WWAN)
* Advanced > Port Options (Example: Smart Card)

## Function keys
{| class="wikitable"
|-
! Key
! Visible?
! Working?
! Effect
|-
| Body - Volume down ||  ||  || Volume down
|-
| Body - Volume up ||  ||  || Volume up
|-
|  ||  ||  || Switches the screen image among display devices connected to the system
|-
|  ||  ||  || Decreases the screen brightness
|-
|  ||  ||  || Increases the screen brightness
|-
|  ||  ||  || Mute : the light of the key is not working
|-
|  ||  ||  || Volume down
|-
|  ||  ||  || Volume up
|-
|  ||  ||  || Microphone mute
|-
|  ||  ||  || Keyboard light
|-
|  ||  ||  || Num lock
|-
|  ||  ||  || Calendar
|-
| Keyboard - screen sharing ||  ||  ||
|-
| Keyboard - answer call ||  ||  ||
|-
| Keyboard - end call ||  ||  ||
|}

## Mobile broadband
In order for the system to correctly load the modem, it is necessary to create a rules file under .

Use lsusb (from ) to confirm the USB VendorID and ProductID, then create:

{{hc|/etc/udev/rules.d/lt4132.rules|
ACTION=="add|change", SUBSYSTEM=="usb", ATTR{idVendor}=="03f0", ATTR{idProduct}=="a31d", ATTR{bConfigurationValue}!="3", ATTR{bConfigurationValue}:="0"

ACTION=="add|change", SUBSYSTEM=="usb", ATTR{idVendor}=="03f0", ATTR{idProduct}=="a31d", ATTR{bConfigurationValue}!="3", RUN+="/bin/sh -c 'sleep 1; echo 3 > %S%p/bConfigurationValue'"

ACTION=="add|change", SUBSYSTEM=="net", ATTRS{idVendor}=="03f0", ATTRS{idProduct}=="a31d", ATTR{cdc_ncm/ndp_to_end}=="N", ATTR{cdc_ncm/ndp_to_end}:="Y"
}}

## Known issues
## ACPI errors
There are lots of ACPI related error messages:

Upstream report: https://bugzilla.kernel.org/show_bug.cgi?id=194833 - looks like a HP firmware bug

## After "BIOS" update to 1.05
Errors changed a little after "BIOS update".
