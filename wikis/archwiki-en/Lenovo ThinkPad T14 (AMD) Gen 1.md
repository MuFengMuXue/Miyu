# Lenovo ThinkPad T14 (AMD) Gen 1

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wi-Fi || ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader ||  ||
|-
| Mobile broadband || ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo Thinkpad T14 (AMD) Gen 1 laptop.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
## Secure boot
As of January 2021 deleting Secure Boot keys and installing your own keys (for example by using KeyTool) will brick the device. This is a problem that is similar to one which has been reported on some other Lenovo laptops and is likely due to a faulty firmware. If the device is stuck in a boot loop after replacing the Secure Boot keys, the only way to repair it is by replacing the mainboard of the device. Hopefully, the issue will get fixed with a firmware update in the future.

## Battery issues
In an ongoing Lenovo forums thread, there has been a discussion regarding battery drain issues in suspend/powered-off states. Presumably, laptops with AMD Renoir CPUs and relevant hardware are affected. As of now, BIOS firmware version 1.29 is suggested for use, as version 1.30 introduced significant battery drain; the battery loses up to 50% in 2-3 days while the laptop is in suspend mode.

There is also a suggestion that kernel updates could fix this behavior and that Lenovo and Canonical are working on it.

## Keyboard
As of BIOS 1.35, keyboard event processing does not work correctly and can cause input problems with shortcuts involving the function key. Moreover, typing fast can lead to scrambled or missing keys which is caused by polling issues with the firmware.

## Trackpad
As of BIOS 1.35, disabling the trackpad has no effect in Linux. In the graphical BIOS and in Windows, this function works as intended.

Since kernel 5.18, there are some issue with the track pad after resume (left button not working anymore). A workaround is to set parameter  to the module psmouse.

In a Lenovo forums thread, there has been a discussion regarding touchpad issue with Synaptics firmware PR3584089. Downgrading the version to PR2909640 solves this.

## Time stamp counter
As of BIOS 1.35, the time stamp counter (TSC) can be unusable on a cold boot, as indicated by the following log output:

## Renesas USB controller
As of BIOS 1.35, toggling the state of USB devices in the BIOS can cause the Renesas controller to fail. This will prevent the webcam from being initialized.

## Docking stations
As of BIOS 1.35, video output is unrealiable on both USB3 and mechanical docking stations.

## Webcam
Image quality can be improved by updating the webcam firmware. Unfortunately, webcam firmware updates are not shipped via LVFS. Some cameras firmwares can be possibly updated in Linux following steps.

## Fingerprint sensor
The fingerprint sensor works: use fwupd to install the latest firmware for "Synaptics Prometheus Fingerprint Reader".

fprint has more details on how to setup the fingerprint, for PAM-based authentication for example.

If the fingerprint reader is not detected by fwupd but is detected by , you will need to reset the fingerprint reader in the UEFI.

## Backlight
Backlight works correctly by manipulating the values, between 0-255, inside  or using a backlight managing utility.

## Suspend
S3 suspend works when setting Config > Power > Sleep to Linux in the BIOS.

## Hibernation
As of kernel 5.15.2, the system occasionally has issues with resuming from hibernate, resulting in missing or distorted video output.

## Mobile broadband
Tested, works with xmm7360-pci (see Xmm7360-pci):

## Smartcard reader
Install ,  and  packages and start .
then you can use the pcsc_scan command to read the card informations.

For more information check out Smartcards.

## Wireless
The onboard wireless card is Intel AX200 and it may have microcode issues when used as-is. A possible fix for Wi-Fi disconnects is turning on  antenna aggregation on by creating a modprobe configuration:

Reboot afterwards. Look in Network configuration/Wireless#iwlwifi for details.

## Microphone-LED
The LED of the microphone remains always on. As a workaround install the package  and the LED should remain always off after a reboot.
The microphone toggle itself should work anyway reliable.

## Platform Profiles
Starting with kernel version 5.18, ACPI platform profiles work correctly on AMD ThinkPads and can be managed manually via  at  or automatically via . The following table shows power and thermal limits for the available profiles. The balanced profile is active by default.

{| class="wikitable"
! Mode !! STAPM (W) !! PPT-FAST (W) !! PPT-SLOW (W) !! THM-CORE (°C) !! STT_APU (°C) !! FAN (rpm)
|-
| low-power || 11 || 11 || 11 || 70 || 45 || 3300
|-
| balanced || 20 || 20 || 15 || 86 || 45 || 4400
|-
| performance || 25 || 25 || 23 || 96 || 53 || 5000
|}

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
|  ||  ||  || Toggles the Fn lock
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
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles the PrivacyGuard feature
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
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
