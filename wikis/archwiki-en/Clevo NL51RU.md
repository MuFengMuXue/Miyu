# Clevo NL51RU

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Audio ||  ||
|-
| Webcam ||  ||
|-
| SD-card reader ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
|}

The NL51RU is a device by the taiwanese OEM manufacturer Clevo. It is sold as System76 Pangolin, Tuxedo Aura 15. The hardware is configurable and includes an AMD Ryzen 5 4500U or AMD Ryzen 7 4700U, AMD radeon 6 core integrated graphics, up to 64GB RAM @3200MHz, SSD (SATA or NVMe), microSD card reader, 3g/LTE modem and a HDMI output.

## Firmware
fwupd is supported. Testing showed System firmware and SSD firmware updateable.

## Webcam
The webcam needs to be activated by pressing , otherwise device will not be available.

## Sound
Sound mostly works out of the box, tested with ALSA and PulseAudio. Wrong sound card may be selected by default. Microphone seems to be working out of the box as well.

## Touchpad
The touchpad works out of the box. Scrolling and multi finger touches work, as well as left/right clicks. Gestures seem to be working, tested with .

## Wi-Fi
Wi-Fi seems to work well. When  is installed,  toggles airplane mode.

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
|  ||  ||  || Disables display
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Seems to have same effect as
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles webcam
|-
|  ||  ||  || Toggles airplane mode
|-
|  ||  ||  || Suspend device
|-
|  ||  ||  ||
|-
|  ||  ||  || Switch keyboard backlight color
|-
|  ||  ||  || Toggle keyboard backlight
|-
|  ||  ||  || Decrease keyboard backlight brightness
|-
|  ||  ||  || Increase keyboard backlight brightness
|-
|  ||  ||  || Seems to toggle fan at max speed
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

To make use of some of the  keys (Airplane mode, keyboard backlight), kernel module needs to be added. Installing  from the AUR was tested and enables these keys after reboot.
