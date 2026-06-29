# Lenovo ThinkPad T480

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| TrackPoint || PS/2 ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Smart card reader ||  ||
|-
| Mobile internet (Realtek) ||  ||
|-
| Mobile internet (Fibocom) ||  ||
|-
| Fingerprint reader ||  ||
|-
| SD-card reader ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo ThinkPad T480 laptop.

## Accessibility
The UEFI firmware interface relies heavily on visual menus and lacks built-in accessibility features such as text-to-speech or audible beep codes for navigation.

## TrackPoint and touchpad
TrackPoint and touchpad work out of the box and do not seem to have the same issues as the X1 Carbon Gen 6. However, one could benefit from having greatly increased event reporting frequency by enabling the  kernel module option . This can be made permanent with:

For two-finger scrolling activity this gives a boost from 40 Hz to 135 Hz on average. This boost greatly contributes to the Desktop environment scrolling performance and smoothness.  may be of use to find out how frequently the Touchpad reports events. For example, after enabling said option:

Note that units adorned with the "glass Touchpad mod" will not benefit from the elevated Touchpad performance with the procedure above. Running  will also indicate a different Touchpad identifier:

## Power management and throttling
Due to missing Intel Dynamic Platform and Thermal Framework (DPTF) support for Linux, a feature which should detect whether the laptop is used on a desk or on the lap so it can throttle the CPU in the latter case to reduce the temperature is not working, and the CPU is always throttled. A Lenovo employee explained the situation and the solution Lenovo is building in a PDF posted in their forum (archive.org backup of the PDF). The firmware and EFI fixes have been released for a different model and Lenovo has recognized that the T480 is affected. An interim fix is  (GitHub).

## CPU stuck at minimum frequency
A signal called BD PROCHOT inside the laptop can force the CPU to the lowest power state (400 MHz in case of the T470s) regardless of the governor. This is meant to protect the system and can be triggered by many reasons—the CPU temperature rising above 60 °C, using a third party battery, etc. It can be ignored by writing a value to a register This script is an alternative to the app ThrottleStop on Windows. Install  and execute this script after every boot (or make a systemd Oneshot service).

## Firmware
Lenovo provides firmware updates for this device through the Linux Vendor Firmware Service (LVFS). Available updates and changelogs can be found on the [https://fwupd.org/lvfs/search?value=Thinkpad+T480 LVFS website. These include security patches for the Intel Management Engine and the system firmware.

The updates can be installed using fwupd.

## Mobile internet
There is no working Linux driver for the Fibocom L850-GL. See this thread and this thread for more information.

## Screen backlight
Without the Intel driver (), neither xbacklight nor xrandr brightness controls are working. However, the package  provides a drop-in replacement for xbacklight. Apart from installing the package (which conflicts with ), the user must be added to the  group and the following udev rule must be created:

This allows control of the backlight with the  command provided by acpilight, as well as control of the various LEDs on the T480.

## Encryption and keyboard
Assuming an encrypted installation, a prompt is displayed to enter a password to decrypt the disk during the boot process. In some cases it may not be possible to enter the password because the keyboard driver is not loaded yet. To fix this, add the  module to the mkinitcpio  array:

Regenerate the initramfs afterwards.

## Fingerprint reader
The fingerprint reader is supported on Kernel 5.8.1 and newer with . See this Reddit thread for more information.

Install  and register fingerprints with:

 $ fprintd-enroll

Refer to the entry on fingerprint sensor of the Lenovo ThinkPad X270 for general procedures if  is returned. See these steps for alternative instructions.

## Function keys
Some special buttons are not supported by the X server due to a keycode number limit. Certain keys are also handled by other devices other than the keyboard.

{| class="wikitable" style="text-align:center"
|-
! Key !! Visible? !! Marked? !! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles Fn Lock
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles Keyboard Backlight
|}

## ThinkPad Dock
The ThinkPad dock shows up through the thinkpad_acpi driver.

## Docked Audio Configuration
Starting this device when connected to the dock seems to load the sound driver for the dock before the driver for the internal audio. The dock driver uses snd_usb_audio while the internal audio uses snd_hda_intel. If it is desired to have the internal audio to show up as card zero the following can be setup as a quick workaround which reserves the first card slot for when the other driver loads.

More detail for alternate configuration can be inspired from Advanced_Linux_Sound_Architecture#Card_index.
