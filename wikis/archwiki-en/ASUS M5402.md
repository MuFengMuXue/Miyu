# ASUS M5402

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
| Wi-Fi/Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Laptop works mostly out of the box with a recent Linux kernel (>6.1.x). Keyboard does not work in older versions.

## Audio
Its ALC294-powered headset/internal microphone port does not work out of the box. This workaround can be used to enable the headset microphone.

## Wi-Fi/Bluetooth adapter
Its Mediatek MT7922 pcie card has some issues such as not being detected after a restart. Booting into Windows/disabling fast startup/modprobing mt7921e sometimes fixes the problem.

## Power management
The screen brightness is set to max after a restart/logout. This workaround can be applied to save/restore brightness.

## Function keys
{| class="wikitable"
|-
! Key
! Works?
! Effect
|-
|  ||  || Enables Fn lock
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  || Enables/disables touchpad
|-
|  ||  || Toggles keyboard backlight level
|-
|  ||  || Opens display settings (under xfce)
|-
|  ||  || Toggles microphone (does not light up)
|-
|  ||  || Toggles camera (always lit up)
|-
|  ||  || Snipping tool?
|-
|  ||  || MyAsus
|-
|  ||  || Alt+PrintSc also works as SysRq
|}
