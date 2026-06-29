# Acer TimelineX

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (ATi) || ||
|-
| Bluetooth || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Webcam || ||
|-
| Card Reader || ||
|}

Hardware is a 4820TG/5820TG, but should be similar for all these laptops.

## ACPI
ACPI works with BIOS v1.18 and higher.

If you do not have Windows installed, you can flash with a FreeDOS thumb drive.

## Bluetooth
On some machines, Bluetooth cannot turn on because of + switching only WLAN. Fixed DSDT table seems to solve the problem.

On the 3820TG, Bluetooth might not work even if + is used to turn it on. (Symptoms include "usb disconnect" messages in dmesg, and the adapter not showing up in hcitool dev.)
In this case, copying  to  helps, see this mailing list thread. If it does not work for you, please change this note!

For some models of 4820TG, Bluetooth can be turned on with acer_wmi driver. To check that the driver is installed:
 lsmod | grep acer_wmi
To check bluetooth state (1 is on, 0 is off):
{{hc|cat /sys/devices/platform/acer-wmi/rfkill/rfkill2/{name,state}|acer-bluetooth
0}}
To turn on bluetooth:
 echo -n 1 > /sys/devices/platform/acer-wmi/rfkill/rfkill2/state

## Wireless (TimelineX 5820)
Wi-Fi driver needs to be installed. Open source brcm80211 driver causes kernel panics; the proprietary broadcom-wl driver works fine.

## Wireless (TimelineX 4820TG)
Wi-Fi driver does not work by default. You need to install  and . See Broadcom wireless for details.

## Display brightness control
Sometimes brightness control for integrated card does not work (at least with the 2.6.36.2-1 kernel). You may add  to the kernel line in the GRUB config to fix this.

## Links
# Ubuntu-it thread
# Usind acpi_call module to switch on/off
