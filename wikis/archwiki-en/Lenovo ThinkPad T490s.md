# Lenovo ThinkPad T490s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Bluetooth || ||
|-
| Mobile broadband ||  ||
|-
| Fingerprint reader ||  ||
|-
| MicroSD Reader || ||
|}

## Touchpad
Touchpad works. But some users have reported issues with the related Lenovo ThinkPad T490#Touchpad.

Sometimes the kernel may use an incorrect mode for communicating with the touchpad, causing the touchpad to completely cease working. This could happen after upgrading the firmware in Windows. This could be indicated by something like following in the kernel log.

A workaround is to load the psmouse module with  option. You can do so by creating a file  with the following content:

or by applying the  kernel parameter. See  for more info.

## Mobile broadband
Fibocom L830-EB-00 LTE WWAN USB Modem works out of box. Newest models like Fibocom L850-GL USB/PCI can be more problematic because missing PCI motherboard specific driver.

## Fingerprint reader
The fingerprint reader works: use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader".

fprint has more details on how to setup the fingerprint, for PAM-based authentication for example.

## ACPI
The default  script has a check for the device that looks like this:

 ac_adapter)
         case "$2" in
             AC|ACAD|ADP0)

This will not work, since the T490s device is called  which is not matched by the above check. The instructions in Acpid does mention a pattern that does work and it is recommended to use this instead.

## Function keys
Most function keys should work out of the box, but if it does not, bind mentioned keys to below commands:

*  key: .
*  key: .
*  key: .
*  key: .
