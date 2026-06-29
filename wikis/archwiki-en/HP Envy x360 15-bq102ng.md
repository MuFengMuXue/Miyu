# HP Envy x360 15-bq102ng

The HP Envy X360 15-bq102ng was released in 2017. It has a Ryzen Mobile 5 2500u with an integrated Vega 8 GPU and 8GB of DDR4 RAM.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| Camera || ||
|-
| Card Reader ||  ||
|-
| Sensors ||  ||
|-
|}

## Installation
This laptop has Secure Boot enabled by default. To start the installer you need to disable it in the UEFI. Then you can just boot the installer in UEFI mode and just install like a normal UEFI system.

## Battery and Power Management
On Linux 4.17 I get about 5 hours on light load, like watching youtube. Installing  is a good idea. Suspend and Hibernate works.

## Orientation sensor
See Tablet PC#Automatic rotation

## Hard Drive
Built-in NVMe drive works with advertised speed. Blockdevices are loacated at . There is an empty bay for an additional SATA 2.5 inch drive, but you have to buy a proprietary cable.

## Freezes
On some devices the laptop freezes randomly (e.g. when surfing on Youtube). A workaround is to set these kernel parameters: .
