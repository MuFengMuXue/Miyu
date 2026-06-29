# MSI GL73 8SC

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (nvidia) ||  ||
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

## SD-Card Reader
Requires  to function.

## Power buttons
This device has two detected power buttons and one sleep button.

In this case,  () is the "real", physical power button. You can verify this by inhibiting the handling of the power button
 # systemd-inhibit --what=handle-power-key sleep 1h
and recording the events:
 # stdbuf -o0 evemu-record /dev/input/event3 > event3

Pressing the power button should log an event.

The other detected power button has not shown any activity during testing.

See  for more information on handling specific keys.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Inputs
|-
|  ||  ||  ||
|-
|  ||  ||  || User Defined
|-
|  ||  ||  || Switches to ECO Power saving mode4
|-
|  ||  ||  ||
|-
|  ||  ||  || Switches between Turbo/Sport/Comfort/ECO Modes4
|-
|  ||  ||  || Turn Airplane Mode on or off4
|-
|  ||  ||  || 3
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
|  ||  ||  || Decreases keyboard backlight brightness
|-
|  ||  ||  || Increases keyboard backlight brightness
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
# This key is not working
