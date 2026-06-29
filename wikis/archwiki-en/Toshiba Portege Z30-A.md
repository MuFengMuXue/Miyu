# Toshiba Portege Z30-A

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| rowspan="2" | Wi-Fi ||  || rowspan="2"
|-
|
|-
| rowspan="2" | Ethernet ||  || rowspan="2"
|-
|
|-
| Card reader ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Smartcart reader ||  ||
|-
| Fingerprint sensor ||  ||
|}

High-performance ultrabook laptop of Toshiba made for professionals and business. Portégé Z30-A has a long-lasting battery, full-size ports in a laptop of 13.3" and 1.2Kg.

## Bluetooth
The  kernel module is auto-loaded but is not necessary and, in fact, is counter-productive since as soon as you disable Bluetooth (e.g. with rfkill), it seems to attempt to re-load the Intel Bluetooth firmware every few seconds. Just blacklist the module, to make it permanent create:

## Wi-Fi
 is needed for the correct working of Wi-Fi, see Network configuration/Wireless.

## Smartcard reader
Works perfectly with  & , see Smartcards.

## Display backlight control
See Backlight.

## Keyboard backlight control
The backlight works correctly if it is configured on BIOS.  kernel module add support for configuring the backlit of the keyboard. However,  does not work. The modules can be changed in  with the modes: 2,8,16.

 # echo 2 > /sys/devices/LNXSYSTM:00/LNXSYBUS:00/TOS6208:00/kbd_backlight_mode

## Fingerprint reader
Fprint has support for it. However, the image usually is wrong (lengthened) and needs two, three or more tries to obtain verifications.
