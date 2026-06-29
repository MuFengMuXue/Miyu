# ASUS ROG Zephyrus G16 (2023) GU603

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio (Intel) ||  ||
|-
| Audio (NVIDIA) ||  ||
|}

## Installation
Before installing Arch Linux, it may be required to disable the built-in Intel Rapid Storage Technology drivers in the BIOS.

## Accessibility
## Firmware
During boot, press  or  to enter the BIOS menu. You can also press  to select the boot device.

Out of the box, the laptop has a boot animation with audio. In the BIOS setup menu, you can disable the audio by navigating to Advanced Mode (), and setting Animation Post Logo Audio in the Advanced tab to Disabled. You cannot disable the animation.

## Disable IRST drivers
In the BIOS setup menu, you can disable the IRST drivers by navigating to Advanced Mode ()
, and set Enable VMD Controller in the VMD Setup menu on the Advanced tab to Disabled.

## Audio
Audio functions out of the box from kernel versions starting from 6.7. For older kernels, see the fix on ASUS Linux Wiki if you experience distorted audio, which is likely due to bass speakers or the amplifier not initializing correctly.

Audio from the internal speakers is handled by the Intel card, while external monitors connected through the HDMI or USB-C port closest to the 3.5mm aux jack are handled by the NVIDIA card.

## Keyboard LED
Should work out of the box with the latest version of asusctl.

## Function keys
{| class="wikitable"
|-
! Key !! Visible? !! Marked? !! Effect
|-
| Volume Up1 ||  ||  ||
|-
| Volume Down1 ||  ||  ||
|-
| Mic Mute1 ||  ||  ||
|-
| ROG Logo1 ||  ||  ||
|-
|  ||  ||  || Toggles Super lock
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

# These are the special keys positioned above the fuller layout, sometimes labeled with M1 to M4 (with no effect to operation).
