# OnexPlayer X1 A

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Keyboard/Pointer ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint ||  ||
|-
| Accelerometer || ||
|}

OnexPlayer X1 A is a 10.95" detectable laptop with a 1600x2560 portrait display, touchscreen, and accelerometer for tablet mode.

## Screen orientation
The display panel is physically portrait (1600x2560) and requires rotation for normal laptop use: see Tablet PC#Screen rotation.

## Touchscreen
The touchscreen (NVTK0603) requires calibration to match the display rotation.

## Turbo Button and LED
A Turbo Button and its associated LED are located at the top right corner.
The driver for these has been included in the mainline kernel.

*  controls/indicates the LED state.
*  configures the button behavior:
** When set to , pressing the button generates a keyboard event ().
** When set to , pressing the button only toggles the LED.
