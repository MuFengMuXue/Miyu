# ASUS Zenbook Q408UG

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Audio ||  ||
|-
| Audio Processor ||  ||
|-
| Bluetooth ||  ||
|-
| Card Reader ||  ||
|-
| Headphone jack || ||
|-
| HDMI port || ||
|-
| GPU (AMD, integrated) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Keyboard || ||
|-
| Microphone (integrated) || ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|}

A 14" Ryzen 5500U-powered laptop with a metal chassis, released in early 2021.

## Installation
No special kernel parameters or firmware were needed for a typical installation.

However, the keyboard often does not work in initial boot (initramfs). If early keyboard is needed, for example with password-based full disk encryption, some mkinitcpio configuration is necessary.

The following was used to get a reliably working keyboard in initramfs. It is unknown if all the items are necessary, but they at least appear to get the job done.

## Accessibility
The initial BIOS / Setup screen is highly graphical and somewhat mouse-driven. However, the menu can be switched to a more traditional one, which is called "Advance" mode. It uses the arrow, enter, escape, etc keys for all navigation. Press F7 at the first BIOS screen to switch to that "Advance" mode.
