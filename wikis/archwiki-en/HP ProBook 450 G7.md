# HP ProBook 450 G7

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
| Touchpad || ||
|-
| SD-card reader || ||
|-
| Webcam || ||
|-
| Fingerprint reader || ||
|}

## Firmware
HP does not provide update files for Linux. Download a file for Windows. To update just follow instructions from your BIOS.

* Download update for your model (e.g. sp79822.exe)
* Format USB driver as FAT32
* Create on this USB driver folder
* Extract downloaded file (e.g. sp79822.exe) with 7z
 $ 7z e sp79822.exe
* Copy extracted files to the created folder  (also the archive sp79822.exe)
* Reboot the system and enter BIOS
* Run BIOS update and follow instructions

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.
