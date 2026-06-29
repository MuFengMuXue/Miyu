# ASUS Zenbook UX333/433/533

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| Card reader || ||
|-
| Bluetooth || ||
|-
| Face recognition sensor || ||
|}

ASUS announced UX333, UX433 and UX533 models. Since these models share almost the same hardware (the only difference is screen size and discrete NVidia GPU), this article covers hardware specific configuration for all ZenBook 13 (UX333), ZenBook 14 (UX433) and ZenBook 15 (UX533).

## Configuration
## Secure Boot (option)
In order to boot any Linux operating system, navigate to BIOS, then hit F7 or click on "Advanced Menu", then the "Security" tab and set "Secure Boot" to .

If the aforementioned "Secure Boot" option is a menu rather than an on-or-off option, click on "Secure Boot", "Key Management", then "Reset to Setup Mode" and confirm in the dialog.

## Sata configuration
If your device is not seen with , you may need to put your sata in AHCI mode.

Navigate to BIOS, then hit  or click on Advanced Menu, then the Sata configuration tab and set it to .

## Video
See Intel Graphics and Hardware Acceleration. For models with discrete Nvidia graphics card, also see NVIDIA Optimus.

## Audio
See PulseAudio.

## Touchpad
See Libinput.

## Facerecognition login
This computer has built-in face recognition sensor.
You can use it with the project Howdy https://github.com/boltgolt/howdy.
See the howdy page for further informations.

## Battery charge threshold
The procedure decribed at Laptop/ASUS#Battery charge threshold works for the UX333, UX433, and UX533.

## Troubleshooting
## Microcode
During boot you might get the message . See Microcode to resolve it.

## Nvidia issues with Bumblebee
It is likely that it is one of these issues:

* You used a power management application (especially Powertop). See bumblebee#Broken power management with kernel 4.8 for more information.
* You suspended your laptop and resumed, and are now unable to start your GPU, see Bumblebee#Failed to initialize the NVIDIA GPU at PCI:1:0:0 (Bumblebee daemon reported: error: %5BXORG%5D (EE) NVIDIA(GPU-0)).

## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

## Tips and tricks
See ASUS Zenbook UX430/UX530#Tips and tricks.
