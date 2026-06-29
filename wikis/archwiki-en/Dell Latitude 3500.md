# Dell Latitude 3500

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
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Installation
RAID mode is enabled by default. AHCI mode must be used, otherwise the disks will be invisibleUsing RAID mode will trigger a relevant log message in the journal.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

This device has a diagnostic LED which may visualize beep codes in some cases. See the "Diagnostic LED" section in the service manual for more details.
The service manual also contains shortcuts which are needed to trigger certain features, such as the boot menu and settings ().

## Firmware
fwupd does not support this device yet.

## Secure Boot
The BIOS accepts .auth files and supports custom keys well.

## Firmware data path
The BIOS stores logs and recovery images in .
Recovery images are stored in  and are 14 MB in size. It appears that there will only be two images at the same time,  and .
Those files will be created when the BIOS was updated.

## Logs
 contains XML files which contain diagnostics data (SupportAssist).
It appears that there will only be two logs at the same time,  and .
Those files will be created when an error happened.

Example log ():

Another example log ():

## Fingerprint reader
Install .

The fingerprint reader requires a proprietary driver.[https://gitlab.freedesktop.org/libfprint/libfprint/-/issues/183

## Bluetooth
Bluetooth works out of the box. Append  to 's arguments to fix some problems with headset buttons.

After suspending, especially when using #Unmarked keybinds, Bluetooth may stop working. Restart  to fix it.

## Power management
After waking up the device from suspend, input lag will occur for approximately 5-10 seconds. Sometimes it will even repeat a key press for up to 32 times but only within this timespan. There is no known fix for this.

## Power buttons
This device has two detected power buttons and one sleep button.

In this case,  () is the "real", physical power button. You can verify this by inhibiting the handling of the power button
 # systemd-inhibit --what=handle-power-key sleep 1h
and recording the events:
 # stdbuf -o0 evemu-record /dev/input/event3 > event3

Pressing the power button should log an event.

The other detected power button seems to be a virtual, firmware-handled button. This power button will be triggered when your device runs out of battery.
The firmware will send many power button presses, so your machine will most likely only take a few seconds to power off because systemd kills the process/unit it is waiting for when the power button is pressed.

See  for more information on handling specific keys.

## Sleep button
There is also a sleep button/suspend key. It is a virtual, firmware-handled key and will be triggered when using one of the #Unmarked keybinds, which would suspend your device.
Use this to inhibit the handling of the suspend key.

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
|  ||  ||  || See #Unmarked keybinds
|-
|  ||  ||  || Inputs
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || , will hard-block Wi-Fi and soft-block Bluetooth. Press again to disable
|-
|  || 3 ||  || , see #Unmarked keybinds
|-
|  || 3 ||  || , see #Unmarked keybinds
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

## Unmarked keybinds
There are several keybinds handled by the BIOS:

{| class="wikitable"
|-
! Key
! Effect
|-
|  || Unobtrusive mode. Has to be enabled in the BIOS in order to work. Deactivates all LEDs and turns off display and sound. Press again to disable.
|-
|  || Suspends device. See #Sleep button. Can not be disabled/configured
|-
|  || Same as https://www.dell.com/community/Latitude/Fn-NumPad0-puts-my-Laptop-to-sleep-How-can-I-disable-this/td-p/7312265. May be an unintended feature
|}
