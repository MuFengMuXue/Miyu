# Alienware m16 R1 AMD

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU (Integrated)||  ||
|-
| GPU (Dedicated)||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM ||  ||
|}

## Installation
Turn off Secure Boot.

## Graphics
There are occasional graphics crashes when you have both GPUs on. You can either:

* Live with it,
* Turn off the hybrid GPU and only activate one in the BIOS,
* Try the kernel parameter .

## USB
When plugging in a device, only power is available from the port and no kernel message that something got plugged in.

This can be fixed by disabling USB autosuspend with the  kernel parameter.
