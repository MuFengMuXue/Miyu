# HP ProBook 4330s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Audio || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Touchpad || ||
|-
| Card reader || ||
|-
| Webcam || ||
|}

## Fan throttling
The fan can be controlled (throttled) in software, otherwise it never shuts off, even if the BIOS option "Fan always on while on AC power" is disabled. There are two programs supporting the 4330s:

* NoteBook FanControl
* probook_ec.pl script daemonized in Python and in Ruby

## Synaptics Touchpad
The  driver is needed (see Touchpad Synaptics) for the touchpad to work, but the pointstick works out of the box.

## WLAN BIOS whitelist
HP BIOS allows only certain WLAN cards (whitelisting) to be used. This can be worked around by adding the following as the first GRUB command in every OS entry:

 write_dword 0xFED1F418 0x1F501FEB

You can read more on engineering this hack on an archive of its author blog.
