# Dell Latitude E5430

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
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
| Fingerprint || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

The Dell Latitude E5430 is a business line laptop made for corporate users who have a need for durability. This article will tell you how to get the basic components of the laptop running with Arch.

## Hardware specification
{| class="wikitable"
! HW part
! Description
|-
! CPU
| Intel® Core™ i3, i5 e i7 up to i7-35xxM; Intel® Celeron® Bxxx
|-
! RAM
| SDRAM DDR3 up to 1600 MHz, 2 slots for 1, 2, 4, or 8 GB DIMM
|-
! Chipset
| Chipset Mobile Intel® HM77 Express or QM77 Express
|-
! Graphics
| Intel® HD Graphics 3000 for Intel Core i3/i5/i7 2xxxM and Celeron® Bxxx,or Intel® HD Graphics 4000 for Intel Core i3/i5/i7 3xxxM
|-
! Display
| 14,0" LED backlight anti-glare, HD (1366 x 768) or HD+ (1600 x 900)
|-
! Optical media
| DVD-ROM, DVD+/-RW
|-
! Power
| Lithium ion battery of 4 cells (40 Wh) or 6 cells (60 Wh) with ExpressCharge™, or 9 cells (97 Wh)
|-
! Connection
| Bluetooth 4.0, 1x USB 3.0, 1x USB 3.0/eSata, 2x USB 2.0, 1x HDMI port, 1x VGA port
|}

Physical characteristics
{| class="wikitable"
! Height
| 29,9 mm up to 32,5 mm
|-
! Width
| 350,00 mm
|-
! Depth
| 240,00 mm
|-
! Weight
| 2,04 kg
|}

## Hardware support
In this section you will find some quick information and references for hardware support. See Laptop and Laptop/Dell for more general information on laptops.

## Audio
Audio works out of the box.

PC speaker capability is included. See PC speaker for information on how to disable it and more.

## Bluetooth
Install the  package, start  systemd service and use your preferred front-end to manage connections. See Bluetooth for more information.

## Fingerprint reader
Install the  package, as it is required to create fingerprint signatures. See fprint for more useful information.

## Touchpad
Install the  package. See Laptop#Touchpad.

## Wireless
It has been reported to come with the chip Broadcom BCM43228 embedded in a Dell Wireless 1540 802.11 A/N Dual Band, High Speed Wi-Fi Half Mini-card, which can be confirmed by running the following:

  $ lspci | grep Broadcom | grep -v Ethernet
  02:00.0 Network controller: Broadcom Inc. and subsidiaries BCM43228 802.11a/b/g/n

The driver to be used must be either the reverse-engineered open-source  module together with blob firmware , or the proprietary  module via  or .

See Broadcom wireless and Dell Wireless 1540 on WikiDevi for more info.

## Troubleshooting
## Issue with XKeyboardConfig
While starting the graphic interface, you might come across with the issue !6 reported in xkbcomp's Gitlab issue list at freedesktop Gitlab. It seems to apply to both Xorg and Wayland. During the display server startup, the XKEYBOARD keymap compiler (xkbcomb) reports:

One solution is to comment out the following lines in the file .  The double forward-slash is the comment symbol.

This solution of provided in the forum thread Xkeyboard/xkbcomp gives warnings.
