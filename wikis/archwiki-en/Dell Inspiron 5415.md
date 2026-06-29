# Dell Inspiron 5415

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
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

## Installation
Before booting into the installation media, disable Secure Boot in your BIOS. The BIOS is accessed by pressing the  key during the POST screen. To access the boot menu directly, press  during the POST screen. Install Arch Linux as usual with the UEFI installation method.

## Accessibility
If you are an individual with accessibility needs, this will unfortunately not be a great device for you. The FN shortcuts, BIOS UI, basic display, and lack of error code beeps are not accommodating for those with accessibility needs. This device contains no diagnostic LEDs aside from the ambiguous status indicator LED near the charge port.

## Firmware
Download the firmware  from the Dell Support Page and copy it to a flash drive formatted in  filesystem.

Reboot and open the boot menu. In the boot menu, select BIOS Flash Update. Select your flash drive (usually fs1) and Begin Flash.
