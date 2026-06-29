# HP EliteBook 725 G3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Pointing Stick || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-Card slot || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Smart Card Reader ||  ||
|-
| HP dock connector || ||
|}

A lightweight 12.5" laptop with an AMD CPU.

## Issues
## Backlight
Screen backlight brightness is always at maximum after the startup. The problem is that systemd-backlight@backlight:amdgpu_bl0.service reads the value (saving it before the shutdown) from the /sys/class/backlight/amdgpu_bl0/actual_brightness, which seems to be stuck at some value (249).

Manual adjustment could be done by by writing 0..255 to /sys/class/backlight/amdgpu_bl0/brightness (or by using, for example, ). Reading from there produces the correct value as well.

Possible workaround is to write preferred value to /var/lib/systemd/backlight/pci-0000:00:01.0:backlight:amdgpu_bl0 and make it immutable with chattr.

Seems like the same issue as the one mentioned in the comment 19 of this kernel bug report.

## Wi-Fi
Wi-Fi seems to be unstable (crashes often, losing connection).
 pcieport 0000:00:02.3: pciehp: Slot(0-1): Link Down
 pcieport 0000:00:02.3: pciehp: Slot(0-1): Card not present
 wlan0: deauthenticating from 16:4d:29:d7:48:e9 by local choice (Reason: 3=DEAUTH_LEAVING)

## Sleep/Suspend (S3)
Internal screen does not get re-enabled after wake-up (brightness control works, however).
 [drm:atom_op_jump amdgpu *ERROR* atombios stuck in loop for more than 20secs aborting
 [drm:amdgpu_atom_execute_table_locked amdgpu *ERROR* atombios stuck executing C554 (len 629, WS 0, PS 0) @ 0xC586
 ...
 [drm:dce110_vblank_set amdgpu *ERROR* Failed to get VBLANK!
 [drm:drm_atomic_helper_wait_for_flip_done drm_kms_helper *ERROR* flip_done timed out
 [32701.245908 drm_kms_helper *ERROR* flip_done timed out
 [32711.272605 drm_kms_helper *ERROR* flip_done timed out
 [32721.299354 drm_kms_helper *ERROR* flip_done timed out
 [32721.299517 amdgpu *ERROR* Failed to get VBLANK!

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  || 3  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Changes keyboard backlight intensity: ON/100% -> ON/50% -> OFF/0%
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , built-in key LED does not work
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , built-in key LED does not work
|-
|  || 3 ||  ||
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
# systemd handles this by default

Pressing the Fn+F11 () also results in:
 kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0xf8 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes e078 ' to make it known.
 kernel: atkbd serio0: Unknown key released (translated set 2, code 0xf8 on isa0060/serio0).
 kernel: atkbd serio0: Use 'setkeycodes e078 ' to make it known.

## Touchpad
The touchpad itself and the lower pair of buttons are visible as the "SynPS/2 Synaptics TouchPad"; upper pair of buttons belongs to the "PS/2 Generic Mouse", however.
