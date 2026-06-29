# Intel QC71

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (nvidia) ||  ||
|-
| Ethernet || ||
|-
| Card Reader || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| Thunderbolt || ||
|-
| Function Keys || ||
|}

The Intel QC71 is also known as Intel NUC 9 Extreme Laptop Kit (LAPQC71), XMG FUSION 15 (powered by TUXEDO), Eluktronics Mag-15, Aftershock / LEVEL 51 Vapor 15 Pro, MAINGEAR ELEMENT and Avell A60 Muv.

## Installation
During the installation an external keyboard might be needed.

## Function Keys
Most  function keys are recognized correctly and given sufficient userspace support they work out of the box. To have working touchpad toggle (Fn + F5), and keyboard brightness up/down keys (Fn + F6/F7, respectively), you can install .

Since BIOS version 0114, it is possible to configure Fn+ESC to toggle the Fn lock. This can be configured in the BIOS or with the  kernel module.

## Lightbar
The LED bar on the front of the device maybe controlled using one of the following:
* the  kernel driver made by TUXEDO Computers; or
* the  kernel module.

## Power management
## Battery charge threshold
Since BIOS version 0114, it is possible to configure a percentage threshold at which charging will stop. This can be configured in the BIOS or with the  kernel module.

## Reduced fan duty cycle and always-on mode
Since BIOS version 0114, it is possible to configure the fans to spin at about 25% of their maximum speed instead of 30% at idle. It is also possible to configure the fans to always be active. These options are configurable in the BIOS or with the  kernel module.

## TUXEDO Control Center
TUXEDO Computers provides their own Control Center named TUXEDO Control Center (short TCC), .

TCC helps you to control fan speed, energy and performance.
