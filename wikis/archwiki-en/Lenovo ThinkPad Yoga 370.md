# Lenovo ThinkPad Yoga 370

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchscreen ||  ||
|-
| Touchpad || ||
|-
| Accelerometer || ||
|-
| Ambient light sensor || ||
|-
| WWAN ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Stylus || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Audio ||  ||
|-
| MicroSD card reader ||  ||
|-
| Smart card reader ||  ||
|}
The Yoga 370 is a convertible Laptop made by Lenovo. It was released in 2017.

## Firmware
This laptop supports Secure Boot with custom signed keys. fwupd seems to also work well and without any problems.

## Installation
This laptop supports both UEFI and BIOS booting mechanisms. To boot in legacy mode, CSM Support must also be enabled in the UEFI BIOS settings.

## Bluetooth
To make Bluetooth work you need to install package  and

## Fingerprint reader
Install .

Start/enable  after installing package.

## Fingerprint reader not working at all
Fingerprint reader may not work, if that happens try to find help on the python-validity GitHub page.

## Fingerprint reader stops working
Sometimes fingerprint reader will stop working after sleep or hibernation for no apparent reason. Enable both  and  if that happens.

Alternatively create a systemd service:

Do not forget to enable .

## Accelerometer and ambient light sensor
See Tablet PC#Automatic rotation for the packages required by your system.

Detecting whether machine is in tablet mode or laptop mode can be done with:

 # cat /dev/input/by-path/platform-thinkpad_acpi-event

When you fold/unfold the device appropriate info should be displayed.

See also Touchscreen.

## Stylus
To check stylus stylus charge, use:

 $ upower -i /org/freedesktop/UPower/devices/tablet_wacom_battery_0 | grep percentage
