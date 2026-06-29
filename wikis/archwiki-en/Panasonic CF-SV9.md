# Panasonic CF-SV9

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Infrared Camera || ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|-
| Light sensor || ||
|}

## Firmware
System firmware, UEFI firmware, firmware for Thunderbolt controller and touchpad, and SSD firmware can be updated via fwupd.

## Touchpad
## Circular scrolling
The device has a relatively small round-shape touchpad, so the ability to configure circular scrolling is important for usability (since the touchpad area is too small for gestures). As of 06/27/2020, libinput does not have support for circular scrolling, which means you cannot get circular scrolling in Wayland. Under Xorg, with  installed, circular scrolling works fine with the following configuration section

Note: On the Panasonic Let's Note Model CF-SV7
If you found that you cannot move the cursor with the above, but can click you can try commenting out the LeftEdge, RightEdge, TopEdge and Bottom sections. It seems the touchpad on the SV7 differs slighty enough the defintions listed above make the entire circular touch pad a scroll wheel. I was able to scroll using the center of the pad.

After saving the file, restart Xorg.

## Fix touchpad delays after system wake from sleep
Touchpad starts to behave badly and introduce pointer moving delays after system wake up from sleep. To address the issue,  kernel module must be unloaded and loaded back again. The following script does the job:

## Audio
Requires Sound Open Firmware to fully function.

## Fingerprint reader
Synaptics FS7600

## Function keys
Keys - & - work out of the box.
Keys - do not work and do not produce any key codes. According to drivers/platform/x86/panasonic-laptop.c, these buttons are supposed to perform the following functions:

 { KE_KEY, 7, { KEY_SLEEP } },
 { KE_KEY, 8, { KEY_PROG1 } }, /* Change CPU boost */
 { KE_KEY, 9, { KEY_BATTERY } },
 { KE_KEY, 10, { KEY_SUSPEND } },
