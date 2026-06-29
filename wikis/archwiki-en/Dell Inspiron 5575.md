# Dell Inspiron 5575

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-Card slot ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||

|-
| TPM || ||
|}
This is an install and configuration guide for the Dell Inspiron 15 000 Series (Model 5575) laptop, Ryzen 5 2500U with Vega Mobile graphics.

See the Laptop/Dell chart for information on other Dell laptops.

## Installation
See Installation guide.

## Configuration
## X
Make sure you enable the TearFree option in the xorg file configuration (i.e, ).

 Section "Device"
 	Identifier "AMD"
 	Driver "amdgpu"
 	Option "TearFree" "true"
 EndSection

## Troubleshooting
Along with this section, check AMDGPU#Loading as well.

## Boot
## GRUB
## Booting in blind mode error
Add the line
 insmod all_video
in your grub.cfg

## Screen freezes
The boot process normally gets stuck at certain point of the boot process and the cursor blinking stops. You can check if the caps lock LED still works. If that's the case, it means that only the amdgpu driver is gone. The rest of the system will be functional, meaning:

* You can ssh to that machine
* You can perform login and some debugging commands in blind mode, dumping their output into some files in the hard disk for posterior checks.

The solution is to disable Legacy Boot in the BIOS, so the UEFI mode will be the one used to boot. Tested with Secure Boot turned off

## Display
## Screen Corruption
Running the linux 5.2 kernel can cause screen corruption/scrambling. Passing iommu=soft as kernel parameter fixes the issue.

## Network
## NetworkManager
## Wi-Fi card does not work after sleep
When left idle, NetworkManager will save power by suspending Radio Activity. Suspending the laptop during this state will make it hard/impossible to enable the Wi-Fi after waking up. The solution is to turn off Network Manager power saving feature. Create  with the following contents:

 connection
 wifi.powersave = 2
