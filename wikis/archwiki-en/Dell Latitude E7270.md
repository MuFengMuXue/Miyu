# Dell Latitude E7270

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Integrated GPU ||  ||
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
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Sound
Audio output via the headphone port does not work if the microphone is muted when the laptop is started. Unmuting the microphone fixes the issue, it can be savely muted afterwards.

## Display
According to

The FullHD panel supports psr, but the i915 psr implementation for skylake has known bugs.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Toggles Fn lock
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

## Frozen CPU frequency scaling
If you experience CPU frequency scaling freezing, i.e. your cpu stays at the lowest idle frequency follow these steps:

# shutdown your laptop
# remove back cover
# unplug battery
# hold power button for 20s (Count to 40 to be sure)
# replug battery
# attach back cover
# start laptop and retest

See also .

## What does not work
* Fingerprint Reader (0a5c:5834)
* DW5811e stops working after suspend, presumably the UEFI does initial configuration, needs more testing
** Per LKML runtime power management does not work for the chip (EM7455) used in the DW5811e, disabling runtime pm and reseting the device makes it usable.
