# Dell Precision M4600

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU || ||
|-
| Ethernet || ||
|-
| SD-Card slot || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Fingerprint reader || ||
|-
| TPM || ||
|}

## Installation
This laptop shipped with a BIOS only firmware option. A subsequent firmware update introduced the option for UEFI. This option is disabled by default, and must be selected in BIOS.

BIOS settings can be reached by tapping  at the first loading screen.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

## Firmware
fwupd does not support this device yet. Further, there are reports, and experienced by the Author, of this laptop refusing to update the firmware beyond a certain point, potentially due to Secure Firmware Update being enabled in one BIOS update, which then blocks all subsequent updates due to a signature mismatch. There is no known work around at this time, other than replacing the Motherboard.

## Secure Boot
Requires further research. Might be supported, but needs further verification.

## Fingerprint reader
Needs further research.

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
|  ||  ||  ||
|-
|  ||  ||  3 ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# Does not seem to coincide with mark on key

Mute, Volume+, Volume-, Prev, Play/Pause, and Next buttons are present, but currently on my system behave very erratically. To wit, pressed singly, they return a generic keycode.

If pressed two at a time, one of the expected XF86 codes is returned, but it is nearly impossible to guarantee which code it will be.

## Power buttons
This device has two detected power buttons and one sleep button.

(The following is copied from the Dell Latitude 3500 page. As far as I can tell it is correct and accurate, but I was unable to log the PowerButton events on my system.)

In this case,  () is the "real", physical power button. You can verify this by inhibiting the handling of the power button

and recording the events:

Pressing the power button should log an event.

The other detected power button seems to be a virtual, firmware-handled button. This power button will be triggered when your device runs out of battery.
It seems like this is a long button press and it will cause systemd to only wait a few seconds before killing a process, so your machine will most likely only take a few seconds to power off.

## Sleep button
Sleep button is . It appears to work with no necessary configuration.

See  for more information on handling specific keys.
