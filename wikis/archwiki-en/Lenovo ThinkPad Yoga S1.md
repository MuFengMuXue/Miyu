# Lenovo ThinkPad Yoga S1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Sensors || ||
|}

## Installation
All you need is to disable Secure Boot and install Arch Linux as usual, Legacy install is also possible

## Video
The screen is very PWMed, so you might need to fix it. Also TearFree video works great

## Sensors
 provides service for ambient light sensor.

For auto-rotation, see Tablet PC#Automatic rotation.

## Power management
Battery functions like charging thresholds can be controlled using the script  together with the kernel module . The TLP power saving tool supports using acpi_call as backend for setting the thresholds as well.

After installing  the device is immediately waking after suspending.
The soloution is to disable XHC in wake events

 # echo XHC > /proc/acpi/wakeup
