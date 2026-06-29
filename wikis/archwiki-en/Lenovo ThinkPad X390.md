# Lenovo ThinkPad X390

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
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

## Installation
AHCI mode is enabled by default. AHCI mode must be used, otherwise the disks will be invisiblehttps://bbs.archlinux.org/viewtopic.php?id=242282. Using RAID mode will trigger a relevant log message in the journal.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

This device has a diagnostic LED which may visualize beep codes in some cases. See the "Diagnostic LED" section in the service manual for more details.
The service manual also contains shortcuts which are needed to trigger certain features, such as for interrupt normal boot and settings ().

## Firmware
The BIOS/UEFI is compatible with fwupd.

## Secure Boot
The BIOS accepts .auth files and supports custom keys well.

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
|  ||  ||  || Disable or set keyboard backlight
|-
|  || 3 ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
