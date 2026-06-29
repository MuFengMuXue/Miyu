# ASUS x205ta

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Keyboard ||  ||
|-
| Touchpad ||  ||
|-
| GPU ||  ||
|-
| Wi-Fi || ||
|-
| Bluetooth || ||
|-
| Webcam ||  ||
|-
| SD-card reader || ||
|-
| Speakers || ||
|-
| Microphone || ||
|}

The ASUS X205TA is an Intel Bay Trail device with a 64-bit CPU and a 32-bit UEFI.

## Installation
See Unified Extensible Firmware Interface#UEFI firmware bitness.

## Accessibility
The firmware setup uses traditional BIOS color scheme, so it might work with OCR software. Navigation is controlled by the arrow keys on the keyboard.

## Firmware
Enter firmware setup by pressing  after turning on the X205TA.

Secure Boot must be turned off to boot Arch:

* Enter firmware setup
* Navigate to the Security tab
* Enter the Secure Boot menu
* For Secure Boot Control, choose the option Disabled
* Save changes and exit

To boot from your USB installation medium:

* Enter firmware setup
* Navigate to the Save & Exit tab
* Select your USB installation medium from the Boot Override section of the menu

## Wi-Fi breaks after hibernation
Use the following script:

and make it the script executable.

## Bluetooth
Install a correct firmware file (e.g.  from Windows 10 driver) as .
See this page for more information on the hcd file.

In order to get bluetooth working create a systemd unit:

and enable the service.

Next, follow the normal steps to activate bluetooth.
