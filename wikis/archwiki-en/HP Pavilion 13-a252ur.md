# HP Pavilion 13-a252ur

{| class="wikitable archwiki-table-laptop"
| Device || Working
|-
| Graphics||
|-
| Audio ||
|-
| Ethernet ||
|-
| Wi-Fi ||
|-
| Bluetooth ||
|-
| Touchpad ||
|-
| Card reader ||
|-
| Webcam ||
|-
|}

Hardware Information:

* Intel Core i5-5200U (Broadwell)
* 8GB RAM (Up to 16GB)
* Intel HD Graphics 5500
* 128GB SSD
* 1366x768 HD Display
* Touch screen
* Tablet mode
* Dual Speakers
* 2 USB 3.0, single USB 2, HDMI port
* Broadcom BCM43142 ( Wi-Fi + Bluetooth )

## Installation
You have to disable Secure Boot. repeatedly press  during boot to bring up the BIOS setup, navigate to the boot section and disable Secure Boot.

To prevent the system from booting in Legacy mode, it is also recommended to disable CSM/Legacy mode.

## Wi-Fi
For Wi-Fi driver install  package, or  if you use stock non lts kernel.

## Bluetooth
For Bluetooth driver install  package.

## Tablet mode
Keyboard disables and enables out of the box. However, for touchpad it is necessary to create udev rule:

## KDE Plasma
In KDE Plasma 5 it works out of the box.

## Sway
Create  file

In addition,  (with  and ) supports auto show/hide feature, and to enable it when using tablet mode, change the config to

## Kernel parameters
For tablet mode to work correctly, add  as a kernel parameter.
