# HP Omen 16-c0140AX

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Integrated) ||  ||
|-
| GPU (Dedicated) ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Card Reader ||  ||
|-
| TPM ||  ||
|}

This page is about the HP Omen 16-c0140AX which is the AMD Advantage variant of the Omen series. Its equipped with a Ryzen 5800H (54W) and Radeon 6600M (100+10W). It features a 144Hz IPS Full HD Anti-Glare Display, 16 GB of 3200MHz Samsung RAM and a WD PC SN730 1TB SSD.

It includes a 81Whr Battery that provides 9 hours of backup on idle if tuned properly. You can have about 7-8 hours of document editing and 5-7 hours of video watching based on how heavy the codec is. It is not advisable to play games while using battery power as it can significantly reduce the battery's lifespan.

## Installation
Before installation, disable Secure Boot in your UEFI (press the  key on boot). Alternatively you can manually setup Secure Boot for added security.

## Firmware
fwupd does not support this device.

## Secure Boot
You can enable Secure Boot Setup Mode from the UEFI Menu, but you will not be able to make modifications such as adding or removing keys. Additionally, the UEFI will accept files that are signed with multiple keys, as long as at least one of the keys is valid.

## Hidden menus
*  - access advanced BIOS Setup which only has a toggle for Precision Boost Overdrive,
*  - pressed while powering on to enter BIOS Recovery mode.

## Power management
## CPU
This laptop supports the amd_pstate CPU scheduler. This provides a slight improvement in CPU performance and a significant improvement in battery life when using the  governor on battery.

## Max performance
The laptop has been seen to have some peculiar performance related issues. All issues were fixed by setting the EC register  to a value of . This value is noted to be set when enabling Performance mode in the Omen Command Center in Windows and is hence safe to modify.

To set the register from shell:

Enabling this does not lead to any unnecessary increase in power consumption, so you can set it to run automatically at startup.

## Temperature monitoring
By default the kernel loads the  module to check CPU thermals, but the  module provides more info and can be installed with :

## Cooling fan
Fan speed can be monitored from the  module via :

Minimal fan boost control is provided by the  module in the sysfs. To activate the Boost feature, simply set  to 0. Conversely, to disable it, set the same parameter to 2. This can be located at .

To do the same from shell:

 # echo 0 > /sys/devices/platform/hp-wmi/hwmon/hwmon*/pwm1_enable

## Fan control Script
The automatic fan speed control is rather bothersome due to the fact that it runs constantly and creates noise even when temperatures are low. Additionally, it does not increase fan speed quickly when temperatures rise. Fortunately, the fan speed can be manually adjusted by writing values to the Embedded Controller (EC).

To simply this process you may use this python script to change, monitor and automatically adjust fan speed based on temperature via the CLI.

## Keyboard
## RGB
The keyboard RGB can be changed using a modified  module. Clone the latest branch of this git repository and then install the kernel module using DKMS. You may do so with these shell commands:

After installing the module (and rebooting) you can modify and read the RGB values in the path

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggle ,
|-
|  ||  ||  || Enables/disables Meta Key
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
