# Lenovo Yoga 2 11

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Card reader || ||
|-
| Audio || ||
|-
| Wireless || ||
|}

## Installation
To access the boot menu and BIOS, use the "alternative" power button: a small circular one on the right, next to the main power button.

Disable secure boot from the BIOS.  Only the UEFI boot mode appears to be available, but the Arch Linux install ISO used supports UEFI boot.

## Power management
The power button works out of the box, however the system reboots after
shutdown.  This appears to be an
xhci-hcd kernel module bug
and can be worked around by unloading the xhci_hcd module before shutdown.  This
can be done via systemd by creating a unit file
/etc/systemd/system/xhci.service containing

and enable/start .

## Function keys
There is a Windows button by the screen, however key down events are only
reported when the button is released (in tandem with the key release event).
