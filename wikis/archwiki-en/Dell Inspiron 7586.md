# Dell Inspiron 7586

{| class="wikitable archwiki-table-laptop"
! Hardware !! Hardware ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Pen ||  ||
|-
| Fingerprint reader ||  ||
|-
| Webcam ||  ||
|-
| Sensors ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| SD card reader || ||
|-
| TPM ||  ||
|}

## Installation
RAID mode is enabled by default. AHCI mode must be used, otherwise the disks will be invisibleUsing RAID mode will trigger a relevant log message in the journal.

Occasionally, USB devices may not show up in the boot menu. Consult #Booting from external media for more information on this topic.

## Accessibility
The appearance of the UEFI settings is relatively simple and not very colorful, so it might work well with OCR software. It does, however, require the user to use a keyboard, mouse, touchpad, touchscreen, or pen.

The service manual contains shortcuts which are needed to trigger certain features, such as the boot menu (), settings (), and power/disk activity LED ().

## Firmware
fwupd does not support this device yet.

As mentioned in #Installation, AHCI mode must be manually enabled in place of RAID mode.

## Secure Boot
Secure Boot is enabled by default. Custom keys may be used.

## ESP files
The UEFI stores logs and recovery images in . These files may be deleted at any time, though deleting the recovery images will prevent the UEFI from recovering itself if it gets damaged.

Recovery images (created when the UEFI is updated) are stored in  and are roughly 15 MB in size. It appears that there will only be two images kept at the same time,  and .

Diagnostic logs (created by Dell SupportAssist PreBoot Diagnostics) are stored in . It appears that there will only be two files kept at the same time,  and .

## Important updates
UEFI version 1.5.0 or above is required to change thermal profiles through  (or [https://www.dell.com/support/contents/en-au/article/product-support/self-support-knowledgebase/software-and-downloads/dell-power-manager Dell Power Manager on Windows). https://www.dell.com/support/home/en-au/drivers/driversdetails?driverid=2fc08&oscode=wt64a&productcode=inspiron-15-7586-2-in-1-laptop

## Booting from external media
Often, external media will not show up in the boot menu. To work around this, open the UEFI settings, navigate to the boot section, and add the standard removable EFI binary at  on the drive's ESP partition to the boot menu.

## Input
## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || A modifier, to be used with other keys.
|-
|  ||  ||  || Function lock. See the note above for more details.
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
| * ||  ||  || Changes keyboard backlight brightness. Rotates through three levels (including zero).
|-
| * ||  ||  ||
|-
| * ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
| , , , , , , ,  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles between LED power and disk usage modes.
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
| Fold screen over 180 degrees ||  ||  || Dell WMI keypress, entering/exiting tablet mode
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.

## Fingerprint reader
Install .

The fingerprint reader requires a proprietary driver.

## Power buttons
This device has one power button and one sleep button.

See  for more information on handling specific keys.
