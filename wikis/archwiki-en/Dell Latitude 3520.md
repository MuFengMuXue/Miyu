# Dell Latitude 3520

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Ethernet || ||
|-
| Bluetooth ||  ||
|-
| SD-card reader || ||
|-
| Audio ||  ||
|-
| Wireless ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Installation
Disable Secure Boot to boot the live USB. Most drivers work out of the box in the Arch Linux Installation medium.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

This device has a diagnostic LED which may visualize beep codes in some cases. See the "Diagnostic LED" section in the service manual for more details. The service manual also contains shortcuts which are needed to trigger certain features, such as the boot menu and settings ().

## Firmware
Dell website provides firmware updates for Docks which can be installed using fwupd, although this has not been tested yet. https://www.dell.com/support/home/en-us/product-support/product/latitude-15-3520-laptop/drivers

## Bluetooth
Bluetooth works out of the box.

After suspending, Bluetooth may stop working. Restart  to fix it.
