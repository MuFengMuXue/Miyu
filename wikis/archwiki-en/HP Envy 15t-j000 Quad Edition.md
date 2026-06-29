# HP Envy 15t-j000 Quad Edition

{| class="wikitable archwiki-table-laptop"
! Device !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Fingerprint Reader || ||
|}

The HP Envy 15t-j000 Quad Edition is a laptop released in 2013.

## Installation
This laptop has secure boot enabled by default. In order to install Arch this should be disabled. UEFI should be set to legacy mode.

## Battery and Power Management
The rated battery life for this laptop is 9hrs and with configuration 5.5 hrs is usually possible.

Install , , , , ,  and .

Start/enable  and

See TLP for details on its configuration and the page dedicated to the microcode for explanation on loading it.

## Trackpad
The trackpad for this laptop supports a virtual scroll wheel. To enable it, comment out the following:

## GPU
If you have the version of this laptop with an NVIDIA card, see NVIDIA Optimus.

## Fingerprint Reader
This laptop comes with a fingerprint reader but there is no Linux driver for it.

## mSATA SSD
This laptop has a mSATA bay that can be used as a cache for a hard drive. See Bcache or LVM#Cache for details.
