# Lenovo ThinkPad T14 (AMD) Gen 2

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Trackpoint || ||
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
| MicoSD-card reader ||  ||
|-
| Audio || ||
|-
| Wi-Fi ||  ||
|-
| WWAN ||  ||
|-
| TPM ||  ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader ||  ||
|-
| NFC reader || ??? ||
|}

## Accessibility
High contrast black on white with large type. Unfortunately the selected menu item is indicated with faint dotted lines, which would make it hard to read for those with visual limitations. Under the Config tab, there is a Setup UI item that toggles the BIOS look-and-feel back to the old-school Thinkpad grey-blue-and-white, all-text, keyboard navigation mode, which may be easier. A table of navigation keys is found under the heading "Navigate in the UEFI BIOS interface" on p.31 of the user guide.

This device has no diagnostic LEDs but relies on audible beep codes. However, those codes can be translated into visible form by using Lenovo's SmartBeep app. This is described under the heading "Beep errors" on p.53 of the user guide.

## Firmware
## fwupd
fwupd supports the UEFI BIOS, the webcam, the fingerprint reader and the NVMe controller.

## November 2021 security update
On November 4, 2021 Lenovo pushed System Firmware Version 1.12, a UEFI/BIOS update, to LVFS. This is described as a security update (although without further detail). See LVFS page for this update.

## Secure boot
For a number of Lenovo laptops of the same cohort, it has been reported that deleting SecureBoot keys and substituting your own keys bricks the motherboard. Further, Lenovo classifies this as caused-by-customer and thus outside the scope of warranty coverage. See here for Lenovo forum threads on XC17,T14s and T14 (AMD) Gen 1.

You break it, you keep both pieces.

Note that keeping the Lenovo Certificates should not brick the machine according to this thread.

## Realtek Ethernet
 shows two distinct Ethernet controllers:

 is the RJ45 port.  is the proprietary connector next to the 2nd USB Type-C port for use in the Lenovo ThinkPad Ultra Docking Station or with a Lenovo ThinkPad Ethernet Extension Cable Gen 2 cable.

Check  to see what interface has carrier and then set up that interface.

## Mobile broadband
According to the service manual the only supported WWAN card is the Quectel EM120R-GL.

This modem is confirmed working after following the FCC unlock procedure outlined in the ThinkPad mobile Internet#FCC unlock a Quectel modem page.

## Unreliable mic mute LED
See Lenovo ThinkPad T14 (AMD) Gen 3#Mute Mic LED always on.

## Synaptics touchpad RMI bus non-functional
The Synaptics touchpad uses the  module rather than its native RMI bus, which is qualitatively superior. dmesg says:

Following that advice by adding  to the kernel command line results in a different complaint:

For more, see the relevant thread in the Lenovo Ubuntu forums and related kernel bug report.

## Freezing Trackpad
The trackpad may freeze randomly. The cure is to unload the psmouse module with rmmod and reload it with modprobe.

## Fingerprint reader unavailable after suspend
There have been reports that while the fingerprint reader works well with fprintd after a cold start (including wake from hibernation) it vanishes from the list of available devices after sleep or suspend.  As of July 2022, with the latest system firmware updates applied, this issue now seems to be resolved.

## Sleep mode (S3)
Sleep mode and, in particular, the lid switch are slow and flaky unless the sleep mode is set to Linux rather than Windows 10 in the UEFI. Be sure that you have logged out of, rather than suspending, any Windows installation before changing this.

See Power management/Suspend and hibernate for more details.

## Function keys
{| class="wikitable"
! Key !! Visible? !! Marked? !! Effect
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
|  ||  ||  || Controls the keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles ePrivacy screen (if it's supported)
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

## PCI Express Card Reader
The on-board reader requires the  kernel module to be loaded.  This can be enabled at boot by adding a file in  with the module name.

## Touchscreen
Blacklist kernel module  to make touchscreen work.

See BBS#274704 for more information.
