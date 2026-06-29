# Lenovo ThinkPad Z13/Z16 Gen 1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| ForcePad ||  ||
|-
| TrackPoint || ||
|-
| TouchScreen || ||
|-
| Stylus || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| IR camera ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Fingerprint reader ||  ||
|-
| USB4 || ||
|-
| TPM || ||
|}

## Lid Switch
As of January 2023, the lid switch will toggle the sleep state of the laptop. Notably, if the computer is already in sleep mode and the lid is then closed, the computer will wake. There is currently no known workaround.

## ForcePad
The ForcePad functions properly as a multi-touch trackpad. The clicking sensation, click sensitivity, and emulated Trackpoint button adjustments can be made using the ELAN Haptic Pad Settings Tool provided by Lenovo.

## TrackPoint
There is a double tap feature in Windows that does not exist for Linux. Otherwise, the TrackPoint is fully functional.

## Fingerprint
The fingerprint scanner works using fprint. There is an entry for the fingerprint scanner in the BIOS full diagnostic tests, but it is skipped during testing, and an individual BIOS test for the scanner is not shown.

## Stylus
The Precision Pen 2 generally works with the optional OLED display, but a stylus configuration must be manually created to use the full functionality.

## Audio
The amplifier will occasionally fail to turn on after waking from suspend. On some distributions, a bug can occur where only one speaker will play and the other speaker has intermittent, soft popping. This can sometimes be fixed by restarting  user unit.

The built-in stereo microphones are reversed and have different gain levels. That is, the left microphone replays on the right speaker and vice versa.

## Webcam
While howdy seems able to enable the USB IR camera (available on some models) this is not accessible by default via a  path despite showing up in . The normal (visible spectrum) camera is functional.

## Display
Marketing material for the Z13 indicates displays have either 100% sRGB or 100% DCI-P3 coverage. It is unclear whether an externally sourced color profile needs to be loaded and whether this will work on all common compositors. An executable is available on the Lenovo support site (&ldquo;ThinkPad monitor INF files&rdquo;) which provides ThinkPad color profiles.

## Firmware
Can be updated via fwupd or manually in the BIOS.

Take caution when running an unattended BIOS diagnostic test. It is possible that the processor remains hot (e.g. 66 Celcius with fans near 5000 RPM) long after the test is complete.

## Power Management
There are typically battery charging adjustments available for ThinkPad laptops that are not available for the Z13.

See Power management/Suspend and hibernate#Changing suspend method.

## USB4
USB4 including PCIe tunneling works for the most part, but it does not seem to be completely stable. This behavior can also be observed under Windows.

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
|  || 3 ||  || Enables Fn lock
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  || 4 Mutes microphone
|-
|  ||  ||  || 5
|-
|  ||  ||  || 5
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  || 3 ||  || Toggles integrated camera
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  || 3 ||  || Cycles keyboard backlight
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  || 4
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || toggle intelligent cooling6
|-
|  ||  ||  || switch to performance profile6
|-
|  ||  ||  || switch to balanced profile6
|-
|  ||  ||  || switch to low power profile6
|-
|  ||  ||  || toggle TrackPoint quick menu (not supported in Linux)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# An LED indicates the state of this switch
# This event is handled by "ThinkPad Extra Buttons"
# This event is handled by "Video Bus"
# Untested (see discussion)

Notably,  will try to close the active window regardless of  or  state.

This is the first ThinkPad model where the  key is not in the corner of the keyboard.  and  can be swapped in the BIOS menu. The keycaps are the same size, so they could theoretically also be swapped to match the BIOS setting.

## ThinkPad Extra Buttons
This input driver has  and lists support for various events:

{| class="mw-collapsible mw-collapsed wikitable"
|-
! Code
! Event
|-
| 113 ||
|-
| 114 ||
|-
| 115 ||
|-
| 120 ||
|-
| 140 ||
|-
| 142 ||
|-
| 144 ||
|-
| 148 ||
|-
| 149 ||
|-
| 152 ||
|-
| 156 ||
|-
| 158 ||
|-
| 171 ||
|-
| 173 ||
|-
| 190 ||
|-
| 191 ||
|-
| 194 ||
|-
| 202 ||
|-
| 205 ||
|-
| 212 ||
|-
| 216 ||
|-
| 217 ||
|-
| 218 ||
|-
| 223 ||
|-
| 224 ||
|-
| 225 ||
|-
| 227 ||
|-
| 228 ||
|-
| 236 ||
|-
| 237 ||
|-
| 238 ||
|-
| 240 ||
|-
| 372 ||
|-
| 374 ||
|-
| 466 ||
|-
| 475 ||
|-
| 476 ||
|-
| 582 ||
|-
| 592 ||
|}

## Troubleshooting
## Wireless
The wireless chip (QCNFA765) does not work with the kernel parameter debugfs=off
