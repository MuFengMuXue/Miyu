# GPD Win 3

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Video || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Keyboard || ||
|-
| Controller || ||
|-
| Back buttons || ||
|-
| Vibrator || ||
|-
| Touchscreen || ||
|-
| MicroSD Slot || ||
|-
| Fingerprint sensor || ||
|}

This page provides information about the GPD Win 3.

## Fixes
## Audio
This device requires Sound Open Firmware in order for the soundcard to work.

Additionally, add the following kernel module parameter:

 options snd-intel-dspcfg dsp_driver=1

## Touchscreen
The device firmware does not properly initialize the touchscreen, so a patched goodix module is required.

In addition, the touchscreen must be rotated.

Edit, or create, if it does not exist, the file: .

To fix the touchscreen initialization, install  and reboot your device.

## Suspend
Check Low power S0 idle capability is enabled in the UEFI (it should be by default).

See Power management/Suspend and hibernate#Changing suspend method and verify  is used.

To reduce power consumption during sleep, go to Advanced > RC ACPI Settings in the UEFI and enable CS PL1 Limit and set CS PL1 Value to .

## Known issues
## Deep sleep
Deep sleep is not working and there is no fix.

## Notes
## Tearing when using Xorg and modesetting driver
You must install  driver to alleviate tearing on GPD Win 3 when using Xorg.

You can additionally enable  (see Intel graphics#Tearing), but be aware that there is a noticeable impact on performance.
