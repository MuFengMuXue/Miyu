# MSI P15

This laptop may also be known as Prestige 15 or A10SC
{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Thunderbolt ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Card reader ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Secure Boot needs to be disabled at first startup, but it can be configured later. This laptop supports keys reset to factory and custom keys install.

This laptop has advanced UEFI settings if desired.

## Wi-Fi
Sometimes the wireless card gets stuck on startup and needs reset, which can also be accomplished by reloading iwlwifi, iwlmvm and restarting wpa_supplicant.

## Function keys
All the function keys should work out of the box, except , ,  and . The latter does not send an Fn input, but rather the proper  key, so this can be easily assigned.
About the other Fn keys,  maps as the keycode 93, so it can be assigned to its original function (touchpad toggle) with xmodmap:

About  and , these send a keycode, and needs to be configured as described in Map scancodes to keycodes using  instead of , as the latter does not seem to work properly. This is achieved modifying the file  or otherwise, adding at the end of the  section the followings:

 evdev:atkbd:dmi:bvn*:bvr*:bd*:svnMicro-Star*:pn*A10SC*:pvr*
  KEYBOARD_KEY_f1=f20
  KEYBOARD_KEY_f2=f21

The microphone mute button should now work out of the box, but the rotate screen one does need a script that toggles the rotation. This can be accomplished by this script

which will need to be saved somewhere with execution permissions, then added to the shortcut menu in the currently used Desktop Environment and lastly enabled to be triggered by . Afterwards, update the hardware database index.

## Home and End buttons
These buttons are mapped to  and  respectively. A helpful solution is to modify the current layout in , where LAYOUT is the current keyboard layout. This is accomplished by writing the following two lines in the default section of the file:

    key   { [     Prior,      Prior,         Home,    Home      ] };
    key   { [      Next,       Next,          End,    End       ] };

## Fingerprint reader
The fingerprint sensor implementation is not currently functioning but there are some promising projects.

python-validity and pam-validity.

There is also the Validity90 project on GitHub to port the Synaptics  device to Linux - but this project has not seen work in years.

## Hibernation
If after hibernation the laptop does not power off but reboots, it is necessary to modify  to the following:
