# Lenovo ThinkPad T550

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth (Intel) ||  ||
|-
| Bluetooth (Realtek) ||  ||
|-
| Webcam ||  ||
|-
| rowspan="2" | Ethernet ||  ||
|-
|  ||
|-
| Wi-Fi (Intel) ||  ||
|-
| Wi-Fi (Realtek) ||  ||
|-
| WWAN (Ericsson) ||  ||
|-
| WWAN (Sierra) ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad || ||
|-
| Touchscreen ||  ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|}

The larger 15-inch variant of the Lenovo ThinkPad T450.

## Backlight
See Backlight#Kernel command-line options to have the ACPI and backlight function properly.  is another kernel parameter required for this.

## Wi-Fi
See Lenovo ThinkPad T440s#Wi-Fi; the T550 and the T440s share the same Realtek-variant Wi-Fi card.

## Video
The T550 is only able to drive three displays at once. If you are using a one-to-three DisplayPort adapter, you will need to disable the laptop display () in order to use three external displays. Expect a heavy delay (1-2 seconds) while adjusting displays via DisplayPort with .

## SD card reader
See Lenovo ThinkPad T440s#SD card reader; the T550 and T440s share the same SD card reader (but with different sub-device IDs). See also https://linux-hardware.org/?id=pci:10ec-5227-17aa-2223.

## USB
Enabling Always On USB in the UEFI BIOS makes the forward-most USB port on the right side of the laptop (i.e., the charging port) unusable in Linux. Disabling this feature in re-enables the port.

## Function keys
By default, the function keys behave as multimedia keys instead of actual function keys. This behaviour can be changed in the UEFI BIOS settings so that  to  are used as standard function keys and special multimedia features are only triggered with the use of the  key.
