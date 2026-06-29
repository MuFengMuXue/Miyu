# Lenovo IdeaPad Yoga 13

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| SD card reader ||  ||
|-
| Touchscreen ||  ||
|-
| Motion sensor ||  ||
|}

{| class="wikitable sortable"
|-
! Feature
! Status
|-
| CPU Frequency Scaling|| not tested
|-
| Hibernation || not tested
|-
| Wireless/Bluetooth || with troubles
|-
| Wireless/Wi-Fi || with troubles
|}

## Display
## Backlight
Control of brightness only works after suspend. After wake up, you can control brightness via f11 (less bright) and f12 (more bright).
However, it is not brightness problem, but keyboard buttons' problem. To control brightness while loaded from scratch, you can do the following command:

 # cat 4882 > /sys/class/backlight/intel_backlight/brightness

This will change brightness value to 4882. It is maximum brightness level. You can choose some other value, of course.

## Touchscreen
One touch works out of the box. But it works like a mouse.

## Function keys
In addition to the keyboard, there are some extra Lenovo keys:

*Volume + and - work as intended
*Recovery button has no effect while computer is running
*Screen rotation lock button simulates pressing Super + o
*Windows button under the screen simulates pressing Super. Also gives haptic feedback, currently not controllable by software.

Most media buttons work out of the box:
*Mute on F1 works
*Vol- on F2 works
*Vol+ on F3 works
*Close on F4 works
*Refresh on F5 works
*Disable touchpad on F6 works, but also types the ± symbol
*Airplane mode on F7 does not work
*Choose application on F8 simulates pressing ctrl+alt+tab. The keys are pressed and instantly released, which (depending on your DE) may not have the intended effect.
*Disable display on F9 works
*Change video output on F10 simulates pressing ctrl+p
*Brightness- on F11 works
*Brightness+ on F12 works

## Wi-Fi
See Wireless network configuration#rtl8xxxu.
