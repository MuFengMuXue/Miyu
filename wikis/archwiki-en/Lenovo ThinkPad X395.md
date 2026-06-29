# Lenovo ThinkPad X395

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| Touchscreen ||  ||
|-
| Video ||  ||
|-
| rowspan="2" | Webcam ||  ||
|-
|  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| MicroSD-Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Firmware
BIOS firmware updates are provided directly by Lenovo, available in the form of an OS-agnostic BIOS Update Bootable ISO image; to update you BIOS firmware, follow the instructions in the README file therein. In particular, notice that you do not need to follow any of the instructions at Flashing BIOS from Linux.

Alternatively, fwupd has been successful at updating the system firmware to '1.27 (R13ET53W)' and fingerprint reader to '10.01.3478575' without incedent on a 20NMS0H76D SKU.

## Function keys
The media keys all works (with the exception of the  key which does not seem to send any event at all).

These are the three physical buttons above the touchpad, designed to be used in conjunction with the TrackPoint; they work out-of-the-box.

## Power management
TLP prevents plugged in USB devides from working when running on battery. This can be fixed by blacklisting power management of PCI device
