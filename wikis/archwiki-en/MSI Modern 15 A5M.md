# MSI Modern 15 A5M

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard || PS/2 ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM ||  ||
|}

## Installation
Secure Boot needs to be disabled at first startup and after UEFI updates.

Sometimes Wi-Fi may not work properly (not connecting to networks). That issue can be solved by powering off laptop and holding power button for 60 seconds to reset BIOS settings.

## Firmware
Secure Boot functions well with custom keys, make sure to disable automatic reverting to factory keys.

## Accessibility
The BIOS interface is keyboard driven and does not require the use of a mouse.

## Thermals
Fan control can be tuned by installing .

## Battery
Battery charge limit can be tuned by  (PR: https://github.com/YoyPa/isw/issues/41).

According to MSI Center Pro there is 3 modes:

* Mode "Best for Mobility" (Charge the battery to 100% all the time)
 # isw -s 0xef 228
* Mode "Balanced" (Charge the battery when under 70%, stop at 80%)
 # isw -s 0xef 208
* Mode "Best for Battery" (Charge the battery when under 50%, stop at 60%)
 # isw -s 0xef 188

## Keyboard
Toggle  key always on with . The keyboard backlight works properly.
The LEDs on the  (Audio mute) and  (Microphone status) keys do not work.

It is possible to control keyboard backlight with  widget after installing .

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
|  ||  ||  || Keyboard brightness change
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Screen projection
|-
|  ||  ||  ||
|-
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Screen overclocking
Laptops with the 089RU model number have a B156HAN02.1 panel that can be stably overclocked from 60 Hz to 90 Hz by modifying edid settings.

## Troubleshooting
Using commands such as:

 # isw -cp MSI_ADDRESS_DEFAULT
 # isw -s 0xef 228

may fail showing the following error:

 /sys/kernel/debug/ec/ec0/io: No such file or directory

The solution is the following command:

 # modprobe ec_sys
