# Huawei MateBook 14s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Keyboard || PS/2 ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Installation
Secure Boot must be disabled in the BIOS to boot an Arch Linux install medium. Other than that, the installation can proceed normally.

## Accessibility
The BIOS is text-based, OCR-friendly, and usable with the keyboard only.

## Firmware
 detects the SSD, serial bus controller, USB camera, USB4 host controller, system firmware, and UEFI device firmware.

## Function keys
To make function keys trigger – by default and special functions with , write 1 to . This setting survives reboots, so writing once suffices.

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
|  || 3 ||  || Cycle keyboard backlight (no/low/high)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
| Dictation key (above 7) || 3 ||  || Does nothing by default
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || Toggles Wi-Fi via rfkill
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||   || Nothing; supposed to toggle display refresh rate between 60 and 90Hz
|-
|  || 3 ||   || Nothing; supposed to toggle performance mode
|-
|  ||  ||   ||
|-
|  ||  ||   ||
|-
|  ||  ||   ||
|-
|  ||  ||   ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# Not visible to  by default, but detected by the kernel () and can be handled as described in map scancodes to keycodes.

## Audio
Sound Open Firmware is required. The speakers and microphones work well but not perfectly out of the box; the audio jack has some issues which are being addressedUntil the issue is fixed upstream, some workarounds can make the device usable.

## Headphones
To use headphones plugged in the audio jack, until the fixes are incorporated upstream, you can use this workaround [https://github.com/thesofproject/linux/issues/3350#issuecomment-1301070327 (which uses  from ):

## Enable speaker and disable headphones
First, move the output to the speaker DAC:

 # hda-verb /dev/snd/hwC0D0 0x16 0x701 0x0001

Then, enable the speaker:

 # hda-verb /dev/snd/hwC0D0 0x17 0x70C 0x0002

Finally, disable the headphones:

 # hda-verb /dev/snd/hwC0D0 0x1 0x715 0x2

## Disable a speaker and enable headphones
First, move the output to the headphones DAC:

 # hda-verb /dev/snd/hwC0D0 0x16 0x701 0x0000

Then, disable the speaker:

 # hda-verb /dev/snd/hwC0D0 0x17 0x70C 0x0000

Afterwards, pin the output mode:

 # hda-verb /dev/snd/hwC0D0 0x1 0x717 0x2

Then, enable the pin:

 # hda-verb /dev/snd/hwC0D0 0x1 0x716 0x2

Finally, clear the pin value:

 # hda-verb /dev/snd/hwC0D0 0x1 0x715 0x0

In both cases, if using ALSA ensure the outputs are unmuted using  or ; if using PulseAudio, ensure the correct output (speaker/headphone) is selected using  or .

## ALSA
With plain ALSA you will have issues with simultaneous audio output from multiple sources that can be fixed with the following:

which unfortunately renders the microphones unusable.

## PulseAudio
If using PulseAudio, both simultaneous audio output and the microphones will kind of work (only the two left microphones). However, to have audio output through the speakers you should run the  script from #Enable speaker and disable headphones after launching PulseAudio.

## Battery protection
The  driver is available in the mainline kernel.

You can set the thresholds by writing directly to the file:

 # echo '40 70' > /sys/devices/platform/huawei-wmi/charge_control_thresholds

or you can use tools such as TLP:

## Display
The native resolution (2520x1680) is fully recognized and the refresh rate is set to 90Hz but it can be changed to 60Hz and 48Hz. Decreasing the refresh rate means less screen fluidity but also longer battery life
