# HP Spectre x360 13-ap0xxxx

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Mobile broadband ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| Touchscreen ||  ||
|-
| Webcam ||  ||
|-
| Card reader ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Disable Secure Boot: press  to bring up the menu, then  for UEFI,  for Boot options.

You might need to enable Legacy Boot to launch the install media, even on UEFI mode.

Disable the microcode loading if the live environment does not start.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

Blacklist  and .

There is still work needed to support the 4 speakers (only 2 are supported).

## Mute button
All the media keys works but the mute button does not light up.

## Mobile broadband
Some configurations include the Intel XMM 7560 4G LTE modem, an updated version of the 7360 with no Linux kernel driver.

## Fingerprint reader
Not supported at the moment in libfprint, there seems to be a beginning of work to support those types of fingerprint readers here The branch synaptics-driver-20190617 contains code that seems to be able to open the fingerprint reader (if you add the correct device id in ).

Generates an error after opening though so this is not complete yet.

## Tablet mode
Keyboard is automatically deactivated when screen is rotated to tent or tablet mode.

## Auto rotation
Installing  and , autorotation works out of the box except for pen input (does not get rotated). Instead of screenrotator-git, you can use [https://github.com/krupan/laptop-autorotate this script which auto rotates the touchpad, touch screen, and pen.

## Touchscreen pressure sensitivity
The touchscreen seems to use the libinput driver by default, with which pressure sensitivity with the included HP Pen does not work. To get pressure sensitivity install  and force the use of the evdev driver:

The touchscreen should be at , but to make sure you can use a utility like  and verify the location of your touchscreen by testing the input events.

## IR camera
Works with Howdy configured to use  and the patch referenced in https://github.com/boltgolt/howdy/issues/70#issuecomment-439123621
