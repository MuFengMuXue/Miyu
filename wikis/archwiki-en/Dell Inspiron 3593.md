# Dell Inspiron 3593

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

## Installation
RAID mode is enabled by default. AHCI mode must be used, otherwise the disks will be invisiblehttps://bbs.archlinux.org/viewtopic.php?id=242282. Using RAID mode will trigger a relevant log message in the journal.

## Firmware
fwupd supports this device.

## Firmware data path
The BIOS stores logs and recovery images in .
Recovery images are stored in  and are 14 MB in size. It appears that there will only be two images at the same time,  and .
Those files will be created when the BIOS was updated.

## Logs
 contains XML files which contain diagnostics data (SupportAssist).
It appears that there will only be two logs at the same time,  and .
Those files will be created when an error happened.

## Power management
After waking up the device from suspend, input lag will occur for approximately 5-10 seconds.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
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
|  ||  ||  ||
|-
|  ||  ||  || Inputs
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || , will hard-block Wi-Fi and soft-block Bluetooth. Press again to disable
|-
| , ,  ||  ||  ||
|-
| , ,  ||  ||  ||
|-
| ,  ||  ||  ||
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
|  ||  ||  ||
|-
|  || 3 ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
