# HP Spectre x360 15-ch025nd

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (AMD) ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Webcam ||  ||
|-
| Touchpad || PS/2 ||
|-
| Touchscreen ||  ||
|-
| Card Reader ||  ||
|-
| Accelerometer ||  ||
|}

This model was released in February 2016.

* Intel Core i7-8705G with Intel HD Graphics 630 (3.1 GHz, up to 4.1 GHz, 8 MB cache, 4 cores)
* 15.6" 4K (3840x2160) Ultra HD IPS WLED multitouch display
* 16 GB LPDDR3-1866 SDRAM
* 2 TB M.2 SSD
* 2 USB Type C Thunderbolt port, 1 USB 3.0 Type A ports, 1 HDMI port, 1 headphone/microphone jack
* 1 SD media card reader
* 802.11ac (2x2) and Bluetooth 4.0
* Bang & Olufsen quad speakers
* 6-cell, 64.5 Wh Li-ion battery
* Webcam
* Backlit keyboard

## Installation
Installing Arch was mostly without hiccup, you do need to disable Secure Boot ( for UEFI options;  for boot options). Dual boot was not tested. The laptop does not have a CD drive, so you have to use a USB stick. The UEFI also would not startup from the USB stick, but you can browse the USB, and choose the  to startup from.

## Audio
Only the front speakers work out of the box.

## Accelerometer
The accelerometer is not found by any userspace programs,  gives the following output:

The accelerometer is connected to a new Intel Integrated Sensor Hub which is not supported by the kernel yet, but can be manually bound to the  driver:
