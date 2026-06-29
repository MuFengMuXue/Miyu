# Lenovo ThinkPad S440

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| GPU (Intel) || ||
|-
| GPU (ATi) || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Audio || ||
|-
| Wireless || ||
|}

## Touchpad
Install  to get multi-touch gestures working.

## Keyboard backlight
Currently the  module does not support to turn the keyboard backlight on. But you can turn it off with:

 # echo 0 > /sys/devices/platform/thinkpad_acpi/leds/tpacpi::thinklight/brightness

## Suspend
Works flawlessly with with  or any DE integration. If resuming from suspend works once but not a second time, try disabling Intel's Anti-Theft module in BIOS (see this kernel bug report).
