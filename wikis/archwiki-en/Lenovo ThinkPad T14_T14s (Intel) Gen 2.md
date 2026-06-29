# Lenovo ThinkPad T14/T14s (Intel) Gen 2

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| TrackPoint || PS/2 ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| Mobile broadband ||  ||
|-
| Fingerprint reader ||  ||
|}

The Lenovo ThinkPad T14/T14s (Intel) Gen 2 was introduced in 2020. It features a 14" screen, 11th-gen Intel Core processors, and integrated Intel Iris Xe graphics.

To ensure you have this version, install the package  and run:

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
## Intel Turbo Boost
Check that Intel® Turbo Boost Technology 2.0 is enabled using

 $ cat /sys/devices/system/cpu/intel_pstate/no_turbo

An output of 1 means it is not enabled, so you will have to reset your BIOS to defaults. After doing that, running the command again should print 0.
You should be able to see your CPU boosting way higher.

## Suspend
The BIOS has two options for suspend: Windows and Linux (aka S0ix or "modern standby") and Linux S3. Both S0ix and S3 modes work on this system, but there is a bug that causes the trackpad to become laggy after resuming from S3 suspend.

## Graphics
The onboard Intel Iris Xe graphics requires . Testing the experimental Xe driver is possible, see Intel graphics#Testing the new experimental Xe driver.

Screen tearing might be visible on some desktop environments on this machines built-in display. Installing the  package resolves the issue. Note that there might be caveats in installing the packages as discussed in Intel graphics: users willing to compile  may want to use it instead to   use the TearFree option from the modesetting driver.

## Sound
This laptop requires Sound Open Firmware for the internal sound card to work.
See Linux firmware to see what modules the default kernel loads.

## Mobile broadband
The Quectel EM120 WWAN (4G / LTE) is supported but needs an FCC unlock first.

You may also need to swap to the active physical SIM in case it is stuck with no eSIM profiles.

 # mmcli -m /org/freedesktop/ModemManager1/Modem/3 --set-primary-sim-slot=1

## Accessibility
The UEFI defaults to classic text and phone OCR will work well. It has an option to use classic text display instead of graphical by navigating to Config > Setup UI and choosing Simple Text.

You can choose an external USB drive to boot off by pressing the  key, waiting 10 seconds followed by  to choose the device, usually found at the bottom of the list.

The default configuration will beep when normal startup is interrupted with  /  /  providing audio feedback.

Audio notifications (beep) for Lenovo Power On / TCG OPAL passwords can be enabled by navigating to Config > Beep and Alarm and enabling both Password Beep and Keyboard Beep.

## Firmware
fwupd supports updating the UEFI BIOS, NVMe SSD, and fingerprint reader (via the LVFS testing remote) out of the box.

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || Enables Fn lock
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
|  ||  ||  || Toggle Keyboard Backlight
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.

## Keyboard backlight
There is no button on the keyboard to toggle it, but it can be controlled by software.

If the keyboard backlight does not automatically turn on when typing, you can enable it with either of:

*
* Lenovo ThinkPad X1 Carbon (Gen 2)#Automatically turn on keyboard backlight when typing

## Display
Panel part number is: LP140WF9-SPF2. The color calibration file is available at NotebookCheck under the "Download ICC File" link.

## T14 links
* Product Specifications Reference (PSREF)
* Hardware maintenance manual
* User guide
* https://ubuntu.com/certified/202104-28912

## T14s links
* Product Specifications Reference (PSREF)
* Hardware maintenance manual
* User guide
* https://ubuntu.com/certified/202103-28856
