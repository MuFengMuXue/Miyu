# Lenovo ThinkPad X270

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| rowspan="2" | GPU ||  ||
|-
|  ||
|-
| rowspan="2" | Webcam (Acer) ||  ||
|-
|  ||
|-
| Webcam (Chicony) ||  ||
|-
| Webcam (Lite-On) ||  ||
|-
| rowspan="4" | Ethernet ||  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
| Bluetooth ||  ||
|-
| SD card reader ||  ||
|-
| rowspan="2" | Audio ||  ||
|-
|  ||
|-
| rowspan="2" | Wi-Fi ||  ||
|-
|  ||
|-
| WWAN (Sierra) ||  ||
|-
| WWAN (Fibocom) ||  ||
|-
| Smart card reader ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Firmware
In August of 2018 Lenovo has joined the Linux Vendor Firmware Service (LVFS) project, which enables firmware updates from within the OS.
BIOS updates can be queried for and installed through fwupd.

## Fingerprint reader
Install the  package. Once you have done that, continue with . If that command returns , please check the status of the  service. If the status of the service is not active, stop the service and reset the device , . Start the  service & run  again.

If the fingerprint reader does not work after resume from suspend check if both services  and  are enabled. Since mid 2021 this may not be working, too. A workaround can be found in this forum thread in the last post.

If the fingerprint reader does not work on your lock screen after resuming from suspend as reported in a gnome-shell issue, enable USB persistence as described on fprint#fprintd starts before fingerprint reader device is initialized after resuming from sleep.

## No audio over HDMI
Use  to list all audio devices. Use speaker-test to find the correct device-id for HDMI audio, e.g.

 $ speaker-test -c 2 -r 48000 -D hw:0,7

Once you have identified the correct audio device id, add the device at the end of your :

Finally:

 $ killall pulseaudio
 $ pulseaudio --check

## About webcam partial support
The Lite-On webcam works with  or VLC, but not . This may be related to https://gitlab.gnome.org/GNOME/cheese/-/issues/134.

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
|  ||  ||  || Toggles the Fn lock
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || ?
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
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
