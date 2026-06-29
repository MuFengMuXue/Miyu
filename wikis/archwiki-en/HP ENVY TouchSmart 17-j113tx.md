# HP ENVY TouchSmart 17-j113tx

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) || ||
|-
| Audio ||  ||
|-
| Touchscreen ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Card Reader ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint Sensor ||  ||
|}
This page applies to the HP ENVY TouchSmart 17-j113tx.

## Touchscreen
The integrated display includes a Touchscreen.

## Audio
The laptop has integrated 4.1 speakers. Stereo sound works successfully from the front two speakers without intervention under ALSA.

The other speakers are not recognised or used by default; they can be mapped using the hdajackretask utility from the  package, and it appears the correct combination is the same as for other contemporary HP ENVY models:

{| class="wikitable"
! Pin ID !! Override Mapping
|-
| 0x0d || Internal speaker
|-
| 0x0f || Internal speaker (Back)
|-
| 0x10 || Internal speaker (LFE)
|}

## Function keys
The integrated numeric keypad is dual-function, and defaults to scrolling actions unless  is enabled. There is no  key and there is no indicator light for .

The integrated Function keys are also dual-function, and default to either system control actions or assigned Functions depending on what is configured in the Firmware Setup Utility (reversible at runtime by using the  key in combination). The system control actions are:

{| class="wikitable"
! Key(s) !! Control Action !! Status (assuming appropriate software)
|-
|  ||  || No hardware action by default, but may trigger a software action (meant to be a 'Help' key under Windows).
|-
| ,  || Monitor Brightness Down/Up || Works for integrated display.
|-
|  ||  || No hardware action by default, but may trigger a software action (meant to switch video output under Windows).
|-
|  || || Not captured (activates and deactivates the keyboard backlight, which appears to be hardware controlled).
|-
| , ,  || Volume Mute/Down/Up || Works, including the LED that shows when volume is muted.
|-
| , ,  || Media Previous/Play/Next || Works.
|-
|  || || Not captured (activates and deactivates Wi-Fi and Bluetooth transceivers, with a LED that changes depending on this state).
|}

## Fingerprint sensor
Currently not supported by Fprint, according to the project website. The  package may offer some hope, but this has not (yet) been tested on this model.
