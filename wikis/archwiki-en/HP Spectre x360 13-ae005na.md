# HP Spectre x360 13-ae005na

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Video || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Pen input || ||
|-
| Webcam || ||
|-
| Card reader || ||
|-
| Fingerprint sensor || ||
|}

This article covers specific configuration of this laptop. Currently based on experience with Gnome, running on Wayland.

## Installation
Disable Secure Boot in the UEFI ( to bring up menu, then  for configuration,  for Boot options). Proceed with the installation guide.

## Issues and Further Configuration
## Audio
The laptop has a Realtek ALC295 Codec with a 4 speaker system built in. Currently only the 2 speakers on the underside of the machine will work out of the box.
The additional speakers can be enabled using hdajackretask from the  package. To accomplish this, with the Realtek ALC295 codec selected, override pin  to Internal Speaker (LFE) and pin  to Internal Speaker. The option to show unconnected pins may need to be selected.

More information at https://bugzilla.kernel.org/show_bug.cgi?id=189331

## HiDPI
Follow HiDPI for recommendations here. Gnome works out of the box, but other software may need more configuration.

## Auto Rotation
See Tablet PC#Automatic rotation for common methods of achieving this. Installing  worked with no further configuration needed on Gnome.
