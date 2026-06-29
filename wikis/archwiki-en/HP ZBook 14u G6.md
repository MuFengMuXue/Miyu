# HP ZBook 14u G6

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (AMD) ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| LTE Modem ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Camera ||  ||
|-
| Fingerprint reader  ||  ||
|-
| Bluetooth ||  ||
|-
| Touchscreen || ||
|-
| Smartcard reader || ||
|-
| NFC reader || ||
|}
The HP ZBook 14u G6, is a lightweight mobile workstation introduced in late 2019. It features a 14", up to 64GB of RAM, NVMe storage, 8th-gen Intel Core processors, integrated Intel UHD 620 graphics and optionally a dedicated AMD Pro WX 3200 Mobile.

## Sleep/Suspend
S3 suspend will work out-of-the-box as long as Intel microcode is loaded.

## Graphics
As long as  and  are installed, PRIME will work with the default configuration.  The GPU will automatically power off completely when not in use.

All video outputs (HDMI, USB-C) are connected directly to the Intel UHD 620 Graphics.

Intel GVT-g is compatible with this laptop.

## Function keys
Pressing and holding the fn key actually makes the function keys emit regular F* keysyms, so it works in a sort of inverted fashion for the top row keys.
There is no physical 'Insert' key.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || + instead of
|-
|  ||  ||  ||
|-
|  ||  ||  ||  instead of
|-
|  ||  ||  ||  instead of
|-
|  ||  ||  || , built-in key LED does not work
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , built-in key LED does not work
|-
|  ||  ||  || Changes keyboard backlight intensity: ON/100% -> ON/50% -> OFF/0%
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|  ||  ||  ||  +
|-
|  ||  ||  ||  +
|-
|  ||  ||  ||  +
|-
|  ||  ||  ||  +
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
|  ||  ||  || Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  +
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd handles this by default

Pressing the F11 () also results in:
 kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0xf8 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes e078 ' to make it known.
 kernel: atkbd serio0: Unknown key released (translated set 2, code 0xf8 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes e078 ' to make it known.

Pressing the F13 (share screen) results in:
 kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0x6d on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 6d ' to make it known.
 kernel: atkbd serio0: Unknown key released (translated set 2, code 0x6d on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 6d ' to make it known.

Pressing the F14 (accept phone call) results in:
 kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0x66 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 66 ' to make it known.
 kernel: atkbd serio0: Unknown key released (translated set 2, code 0x66 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 66 ' to make it known.

Pressing the F15 (hang up call) results in:
 kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0x65 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 65 ' to make it known.
 kernel: atkbd serio0: Unknown key released (translated set 2, code 0x65 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes 65 ' to make it known.

## Touchpad
The touchpad itself and the lower pair of buttons are visible as the "SYNA3091:00 06CB:82F5 Touchpad"; upper pair of buttons belongs to the "PS/2 Generic Mouse", however.
"SynPS/2 Synaptics TouchPad" and "SYNA3091:00 06CB:82F5 Mouse" are visible, but do not produce any events.

## Additional hardware
The laptop contains an M.2-2242 B-key slot, designated for the LTE modem. Alternatively, one could install an additional SATA SSD.

## Additional resources
* Dell XPS 13 9370 quirks: Some pointers on getting Watt usage down to ~2W, Intel video powersaving features might be interesting, see also the Intel graphics page for interesting power-saving options.
* How to fix volume control (ALSA problem) This is where the volume fix came from originally.
