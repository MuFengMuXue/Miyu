# HP Envy x360 13-ar0002nf

{| class="wikitable archwiki-table-laptop"
|-
! Hardware
! PCI/USB ID
! Working?
|-
| GPU
|
|
|-
| Wi-Fi
|
|
|-
| Bluetooth
|
|
|-
| Audio
|
|
|-
| Touchpad
|
|
|-
| Camera
|
|
|-
| Card reader
|
|
|-
| Sensors
|
|
|-
| Fingerprint reader
|
|
|}

The HP Envy x360 13-ar0002nf was released in 2019 and has an AMD R5 3500U CPU with an integrated Radeon Vega 8 GPU, 6GB of RAM (8GB - 2GB hardware reserved) and a 1080p display.

## Installation
This laptop has Secure Boot enabled by default. To start the installer you need to disable it in the UEFI. Then you can just boot the installer in UEFI mode and just install like a normal UEFI system. You can start using Secure Boot in Linux via Unified Extensible Firmware Interface/Secure Boot.

## Battery and power management
Comes with a 53Wh battery, and with Laptop Mode Tools or TLP in use, yields about 10 hours of battery life under light usage. Under heavy load, battery life dwindles to 4 hours.
This laptop unfortunately only comes with  () sleep state out of the box, which causes many problems in resuming from sleep. It is however possible to patch the ACPI tables in order to add in  sleep, which restores perfect functionality. See this forum post.

## Audio
You need to install  to use hdajackretask. Within the utility, tick Show unconnected pins, then override the following:

* Pin  to Internal Speaker (LFE)
* Pins  and  to Internal Speaker
* Then click Install boot override and reboot

This is the simplest way to get the exact desired functionality for this model, as it is possible to get a configuration where the top bar fires, but where volume can no longer be controlled with instructions for other models.

## Orientation sensor
You currently need to install  and reboot to make the orientation sensor work.

## Touchscreen and stylus
Everything works out of the box, both for touch and stylus use. If using a stylus, the system can differentiate between the stylus, and properly does palm rejection if using something like Xournal++. The experience is exactly the same as with Windows. This has only been tested with a HP stylus.

## Accessibility
The laptop comes with the standard Insyde H20 UEFI firmware setup, which might be easier to parse into OCR software. The laptop also has backlit keys with 2 levels of brightness, if necessary.
No diagnostic LEDs nor beep codes appear to be present in the firmware.

## Firmware
It seems like the System Firmware and UEFI dbx fields are correctly supported by fwupd.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?
! Marked?
! Effect
|-
|
|
|
| No effect (Windows help key)
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
| + alias
|-
|
|
|
| Cycles through key  brightness
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|}
