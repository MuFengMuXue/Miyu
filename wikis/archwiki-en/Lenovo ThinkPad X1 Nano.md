# Lenovo ThinkPad X1 Nano

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Mobile broadband || ||
|-
| Audio ||  ||
|-
| TouchPad || ||
|-
| TrackPoint || ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth ||  ||
|}

## Power management
At least with all current maintained kernel (> /proc/acpi/wakeup

To execute at every start you can add a systemd service:

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

On the headphone jack, a buzz/noise might be audible that even changes with different CPU usage. The fix is to install the  package and then run

 # hda-verb /dev/snd/hwC0D0 0x1d SET_PIN_WIDGET_CONTROL 0x0

To execute at every start you can add a systemd service:

## Fan control
If you are suffering from overheating or you just want more control you can setup Fan speed control#ThinkPad laptops

## Fingerprint reader
The fingerprint reader works out of the box using . See Fprint.
