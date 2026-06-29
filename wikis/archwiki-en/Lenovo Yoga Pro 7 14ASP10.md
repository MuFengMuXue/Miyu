# Lenovo Yoga Pro 7 14ASP10

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
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| TPM || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
Make sure that you have Linux kernel 6.11 or later on the installation media, otherwise you might encounter problems such as keyboard not working.

## Accessibility
The UEFI offers one mode of operation, GUI.

The GUI can be navigated to some degree via the keyboard.  and  arrow keys to move the selection and  to activate.

## Firmware
fwupd does not support this device yet and likely is not going to.

## Secure boot
The firmware does not have any options to install keys through it, to install keys you can use tools such as sbctl. No Option ROMs appear to be present as per testing with:

See Secure Boot for more details.

## Issues
## Suspend
There have been reports that the NVMe drive fails to resume from suspend with the following line in the kernel log:

 nvme 0000:bf:00.0: Unable to change power state from D3cold to D0, device inaccessible

This renders the system unusable upon resuming.

However there are also reports of the system functioning correctly and not encountering this error.

## Internal Microphone
Internal microphone does not capture any audio input, or it is very quiet and noisy. This issue is due to the lack of a specific audio quirk for this model in the kernel.

## Speakers
This laptop has 4 speakers (2 tweeters and 2 woofers), only tweeters might be working due to the lack of a correct audio quirk.

An audio quirk for this model was added in Linux v6.15. If you are running an older kernel, you might need to cherry-pick this commit: 8d70503068510e6080c2c649cccb154f16de26c9.

## CPU power management
Sometimes CPU gets stuck at the minimum frequency (600 MHz) when switching between AC and battery power.

This appears to be a firmware bug, so updating it to the version QFCN22WW or later fixes the issue.

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
|  ||  ||  || No symbol
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
|-
|  ||  ||  ||
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
