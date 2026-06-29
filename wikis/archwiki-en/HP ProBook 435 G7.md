# HP ProBook 435 G7

{| class="wikitable archwiki-table-laptop"
! Device !! PCI/USB ID !! Working?
|-
| Intel graphics || ||
|-
| Audio || ||
|-
| Microphone || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Accelerometer || ||
|-
| Touchpad || ||
|-
| SD-card reader || ||
|-
| Webcam || ||
|-
| Fingerprint reader ||  ||
|}

## Firmware
HP does not provide update files for Linux. Download a file for Windows and using offline USB storage update does not work.

To update BIOS:
* connect laptop to a LAN
* enter bios by pressing  on boot
* check for BIOS updates
* follow instructions for upgrading or roll back

## Tablet mode
This laptop has a sensor built in to detect if it is in tablet mode.

When in tablet mode, the keyboard is disabled. See Tablet PC#Automatic rotation for auto-rotation.

## Fingerprint Reader
This laptop has a fingerprint reader.

The fingerprint device is supported by . The firmware needs to be upgraded via .

Currently,  is buggy and does not let you update your device correctly.
Downgrade to  to install the correct firmware.

## Common problems
## Fn lock, Fn+Shift
Fn lock and  combinations do not work with BIOS firmware  and . Roll back to BIOS  version to fix.

## Touchpad unresponsive
Touchpad stops working with BIOS  sometimes. Reboot or restart  to fix:

 # rmmod i2c_hid_acpi
 # rmmod i2c_hid
 # modprobe i2c_hid_acpi
 # modprobe i2c_hid

This can be executed at boot for a quick fix, e.g. via a systemd service.
