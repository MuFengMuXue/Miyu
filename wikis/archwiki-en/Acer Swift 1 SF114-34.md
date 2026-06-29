# Acer Swift 1 SF114-34

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint Sensor ||  ||
|}

Information about the Acer Swift 1 SF114-34.

## Installation
Press  on boot to enter the BIOS. Set a supervisor password under the Security tab and then disable Secure Boot under the Boot tab. You can now remove the supervisor password.

## Fingerprint sensor
 does not support the model.

## Suspension
Suspension does not work, device wakes up immediately.

Find a "RP" device with enabled status (usually RP05) with the following command:

 $ cat /proc/acpi/wakeup

This is what is causing the issue, and you will need to disable it. Create:

Enable/start it and suspension should now work properly.
