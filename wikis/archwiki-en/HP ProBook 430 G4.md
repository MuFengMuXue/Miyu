# HP ProBook 430 G4

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Touchpad || PS/2 ||
|-
| Card reader ||  ||
|-
| Webcam || ||
|-
| Fingerprint Reader ||  ||
|}

## Device information
This is a work in progress with information about the HP ProBook 430 G4. There are many configurations for these models of HP Probooks. The information below are given from a model HP ProBook 430 G4/822C, BIOS P85 Ver. 01.03 12/05/2016, shipped with a Core i5-7200U, 8GB, 256GB SSD. The notebook supports exchanging two memory modules and support one 2,5" disc drive and one M.2-SSD. The UEFI bios allows legacy boot.

A review in German is available here: HP ProBook 430 G4 review. Basic hardware works out of the box. No configuration was needed. Information for the "Not tested" units will be posted additionally.

## Backlight
I have not found a solution so far to control the backlight via kernel hardware control keys via kernel. So backlight control works only via software. It works out of the box under Xfce and under i3wm using a custom command "xbacklight -inc/-dec 10".

## ACPI errors
There are lots of acpi related error messages with kernel 4.9.x:

Upstream report: https://bugzilla.kernel.org/show_bug.cgi?id=194833 - this seems to be a BIOS implementation bug.

## Keyboard mapping
To avoid error messages appearing in the output of , add

## PCIe error in dmesg output
This one can be fixed with appending  to the kernel parameter.

## Fix cold boot hang
There seems to be some bug in i2c_i801 module implementation with HP notebooks. To fix system hang at cold boot add this module loading options and regenerate initrds.

See https://www.spinics.net/lists/linux-i2c/msg33938.html for more.
