# Dell Latitude 7490

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
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

The Latitude 7490 is virtually identical to the Dell Latitude 7480 with the exception of an upgrade to Kabylake-R processors (8th gen).

## What works
* Basic hardware (display, touchpad, trackpoint, keyboard, Wi-Fi, Ethernet, Bluetooth, audio, hibernation, etc.)
* Keyboard backlight control
* Screen backlight control
* Fn/Hotkeys, including Fn-lock
* Contact SmartCard reader
* Qualcomm Snapdragon X7 LTE Modem
* USB-C (connected to Android phone, was able to charge phone and read files)
* USB-C power delivery
* DisplayPort Alternate Mode for USB-C
* USB-C Display port with D6000 docking station (triple screen with dual 4k works) + power delivery
* Thunderbolt 3.0 (shows up in gnome-settings, works with Dell TB16 dock (Ethernet, DisplayPort @120hz, USB, power delivery, etc))

## What does not work
* Fingerprint reader (tracked at https://gitlab.freedesktop.org/libfprint/libfprint/issues/88)
* Presumably NFC

## What was not tested
* Contactless SmartCard (probably works since it was detected by
* TPM 2.0 (There is an error in the output of dmesg, )

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Mute Microphone
|-
|  ||  ||  || Num Lock
|-
|  ||  ||  || Scroll Lock
|-
|  ||  ||  || Unobtrusive mode
|-
|  ||  ||  || Inputs
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || , will hard-block Wi-Fi and soft-block Bluetooth. Press again to disable
|-
|  || 3 ||   ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default

## Bluetooth
Do not set control to auto for Bluetooth module (0cf3:e007), otherwise sound via Bluetooth headset may tear when Wi-Fi is actively used. If you have TLP, set  to .

It helps in some cases, but with some devices (e.g. CMF Buds Pro) none of any troubleshooting tips helped. Sound is choppy and unstable all the time.

Better solution might be replacing Wi-Fi card, for example Intel Wi-Fi. Unlike thinkpads there is no device whitelist, so there will no difficulties with replacing network card.

## Accessibility
## BIOS Settings Overview
The "BIOS Settings" interface can be reached by pressing  during POST.

The BIOS settings page itself is GUI based, with black text on a white background. There is a panel taking approximately 20% of the screen on the left, containing various sub-categories of settings. The main panel takes 80% of the screen to the right, and contains the settings associated with each sub-category. The font is relatively large, and toggle switches will appear as light grey if set to 'off', and turn light blue if set to 'on'.

The GUI does not have any built-in screen reader or other accessibility settings, but due to its simple colour scheme, and relatively large text size, it should be somewhat accessible for partially sighted people using an external screen reader as an accessibility aid. However, it is a GUI-based interface with lots of available settings, and lots of visual clutter in text form. As such it is likely to be difficult to navigate for people with severe visual impairment or total blindness, who are using an external reader alone. It is possible to enable/disable "Help Text", and "Advanced Setup" using two toggle switches that appear in the top left corner of the screen; disabling them should help reduce this clutter and improve readability (but may also hide useful info/settings!).

There are "Show all" and "Search" functions available towards the top right of the screen, which can ease navigation considerably.

The BIOS can be updated through the "One-Time Boot Menu" (press  during POST).

## BIOS Settings Navigation
The "BIOS Settings" interface can be navigated using a keyboard, or mouse - with mouse being the preferred mode. Keyboard navigation keys are as follows:

{| class="wikitable"
|-
! Key
! Effect
|-
|     || Moves to the previous field.
|-
|   || Moves to the next field.
|-
|  || Selects a value in the selected field (if applicable) or follow the link in the field.
|-
|  || Expands or collapses a drop-down list, if applicable.
|-
|    || Moves to the next focus area
|-
|    || Scrolls the currently selected view up.
|-
|    || Scrolls the currently selected view down.
|-
|    || Moves to the previous page until you view the main screen. Pressing Esc in the main screen displays a message that prompts you to save any unsaved changes and restarts the system.
|}
