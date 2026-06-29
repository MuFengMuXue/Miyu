# Lenovo ThinkPad X220

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth || ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint Reader ||  ||
|}

## Installation
The X220 can not boot from a GPT disk in  mode, it is necessary to either switch to  booting or create a MBR Partition Table.

## Firmware
fwupd does not support this device yet.

To update the firmware on the device, get the latest bootable CD and follow the steps in Flashing BIOS from Linux#Bootable optical disk emulation.

## Power management
After waking up the device from suspend, the device might get stuck in a reboot loop.
This can be caused by the EFI storage getting too full. To free up some space, clear the pstore:

 # mkdir -p /dev/pstore
 # mount -t pstore pstore /dev/pstore

Nothing important should be here, but check first anyway:

 # ls /dev/pstore

Then empty the directory:

 # rm /dev/pstore/*

Next some EFI variables. These are used/created by pstore, but everyone should have had them even though the pstore data was deleted using the above commands:

 # rm /sys/firmware/efi/efivars/dump-type0-*

## Microphone
The internal microphone can generate a lot of static or hissing, the workaround is to mute the right mic input channel.

## Touchpad
If the touchpad is jumpy/imprecise, create the following configuration:

Then follow the steps at Map scancodes to keycodes#Using udev.

See Fedora bug #1264453 for more details.

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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
