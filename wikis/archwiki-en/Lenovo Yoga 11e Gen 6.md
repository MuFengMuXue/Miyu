# Lenovo Yoga 11e Gen 6

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| TouchPad ||  (Elan) ||
|-
| Touchscreen ||  (Elan) ||
|-
| Webcam ||  ||
|-
| TPM || - ||
|}

The Lenovo Yoga 11e (Gen 6) is a 2-in-1 replacement for the Thinkpad X1xx series.  Both Chromebook and (originally) Windows-based systems exist.  This page (currently) covers the Windows version.

To ensure you have this version, make sure you have access to the  program and run:

## Installation
EFI booting works without issue.

See #Firmware on how to change UEFI settings, and access the boot menu to load an Arch installation medium.  The overall installation is straightforward.

When installing over wireless, the interface is powered off, and the  hotkey does not function.  The interface can be enabled by running

## Secure Boot
Disabling Secure Boot is not required to install Arch on this hardware.

## EFI/LUKS
Full disk encryption with LUKS is supported.  It is significantly easier to get this working using an EFI boot stub rather than GRUB. In addition to various dm-crypt wiki pages, and [https://gitlab.com/zer0the0ry/arch-linux-install-with-efi-and-luks-encryption may be helpful.

## Firmware
BIOS is accessible via  during system boot.  Default settings appear to work fine.

The boot menu is accessible via .

Firmware upgrades have not been tested.

## Keyboard
No issues.  However, the location of the  and left-side  key may annoy some users.  There is a BIOS setting to swap the two keys.

## Function Keys
{| class="wikitable"
|-
! Key
! Visible? 1
! Marked? 2
! Effect
|-
|  ||  ||  || Toggles Fn lock
|-
|  || 3 ||  ||  returns
|-
|  || 3 ||  ||  returns
|-
|  || 3 ||  ||  returns
|-
|  || 3 ||  || (icon: Mic off)
|-
|  ||  ||  || (icon: Brightness minus)
|-
|  ||  ||  || (icon: Brightness plus)
|-
|  || 3 ||  || (icon: laptop/monitor)
|-
|  ||  ||  ||  4 (icon: wireless)
|-
|  ||  ||  ||  (icon: speech bubble)
|-
|  ||  ||  ||  (icon: Telephone up)
|-
|  ||  ||  ||  (icon: Telephone down)
|-
|  ||  ||  ||  (icon: star)
|-
|  ||  ||  ||
|-
|  ||  ||  ||  (icon: dashed circle with scissors)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  (most other Fn+ combinations do nothing)
|-
|  ||  ||  ||
|-
|  ||  ||  ||  (Screenshot?)
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
#  only returns a , but no  or  events.  No keycodes are seen by .
# Unlike some models,  does *not* send an  keypress event.  However, it should be possible to bind this to rfkill to achive the same result.

The following xbindkeys configuration may be needed to get volume/mic controls working properly:
 "pactl set-sink-mute @DEFAULT_SINK@ toggle"
     m:0x0 + c:121
     XF86AudioMute
 "pactl set-sink-volume @DEFAULT_SINK@ +5%"
     m:0x0 + c:123
     XF86AudioRaiseVolume
 "pactl set-sink-volume @DEFAULT_SINK@ -5%"
     m:0x0 + c:122
     XF86AudioLowerVolume
 "pactl set-source-mute @DEFAULT_SOURCE@ toggle"
     m:0x0 + c:198
     XF86AudioMicMute

## Bluetooth
Bluetooth works, but  may report a "hard blocked" device ( below).

As there is no hardware disable switch on this system (including ), unblocking this device is not possible.  However, the  is the one actually used, so functionality is there.  Some tools may not work correctly, as they assume a single Bluetooth device;  for example.  and  both seem to work fine.

## Touchpad
Rarely, the touchpad will stop responding after resuming from suspend, but the keyboard works fine.  This can be fixed by removing, and re-adding the  module:

## Power Management
This laptop comes with an Intel Core m3-8100Y CPU 1.10GHz CPU.  The rated frequencies range from 400MHz - 3.4GHz.

The  driver is supported, with the  and  governors supported.  CPU scaling works with both governors. Behavior is sometimes inconsistent:  frequencies stay low even under 100% CPU load, or remain high when the system is generally idle.  This behavior is not yet completely understood, but may be similar to Lenovo ThinkPad T480#CPU stuck at minimum frequency

{{Tip|Immediately after resuming from suspend, the CPU is often throttled, even when using the "performance" governor.  Forcing a second suspend/resume (e.g. closing the lid and re-opening) should allow CPU scaling to work properly.  The  program can mitigate this issue without re-suspending.

The short script below will flip the governor between "performance" and "powersave" options.  With minor modification, it can be bound to one of the unused #Function Keys hotkey as a convenient toggle.  It may work on other systems as well.

## Sensors
As this is a tablet, an accelerometer is installed and supported by .

The  may be of interest, although it needs to be converted to Python3, and will have to be modified to detect the ELAN devices (instead of WACOM).

Various temperature sensors are supported by .

The hardware includes neither an ambient light sensor, nor a proximity sensors.
