# Lenovo Yoga Pro 7 14ASP9

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| TPM || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## Accessibility
The UEFI offers one mode of operation, GUI.

The GUI can be navigated to some degree via the keyboard.  and  arrow keys to move the selection and  to activate.

## Firmware
fwupd does not support this device yet and likely is not going to.

Lenovo support page for this model only provides .exe installer for UEFI updates. There is no option in the UEFI itself to select a binary blob from USB stick.

## Updating UEFI
A workaround is to install the UEFI from Windows PE. A common choice is Hiren's Boot CD. Boot into the live environment, download the update file and install it.

## Secure boot
The firmware does not have any options to install keys through it, to install keys you can use tools such as sbctl. No Option ROMs appear to be present as per testing with:

See Secure Boot for more details.

## Issues
## Speakers
This laptop by default uses the wrong playback device, defaulting to card 0 instead of card 2 which is the Realtek ALC287. This causes it to only use the bottom two speakers and not the top two woofers. We can fix this by manually changing the device used by creating

and rebooting.

## RDSEED32 is broken
With Linux ≥6.17.7 RDSEED32 error message can be seen during boot:

Error message is related to AMD-SB-7055/CVE-2025-62626 which affects AMD Zen 5 processors.

Fix will arrive in future UEFI versions: Lenovo Security Advisory: LEN-208435

At the moment of writing, UEFI version for Yoga Pro 7 14ASP9 is TBD with target availability 2026-02-27

## LUKS passphrase entry appears frozen
RDSEED32 error message causes Panel Self Refresh (PSR) timing issues so that it seems like it’s frozen on the LUKS passphrase entry.

Disabling PSR fixes the issue.

## Panel Self Refresh issues
PSR can cause flickering and random freezes/crashes on AMD Ryzen AI 300 Series Processors.

It can be disabled by adding  to kernel parameters.

 is part of
 from
drivers/gpu/drm/amd/include/amd_shared.h.

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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
