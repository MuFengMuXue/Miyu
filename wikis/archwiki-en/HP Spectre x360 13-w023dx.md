# HP Spectre x360 13-w023dx

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchscreen ||  ||
|-
| Touchpad || PS/2 ||
|-
| Webcam ||  ||
|-
| IR Camera ||  ||
|}
This article covers hardware specific configuration of this laptop, some minor issues remain after customization. These can be performed after an installation of Arch Linux has been finished and the machine rebooted into it.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Hardware info
## Hardware options
This is the model of HP Spectre x360 released in late 2016. Distinctive features include two thunderbolt ports and no digitizer. The main hardware components are

* Intel i7 Kabylake 7500U
* OLED touch screen running at 1920x1080
* 500 GB M.2 SSD
* 16 GB RAM
* 4 speakers

## Installation
Installing arch is straight forward for everything (disable secure boot, F10 for BIOS, F9 for boot options) but one thing: you may have to disable a BIOS option called "fast boot". While this option is activated in BIOS the machine may boot into Windows no matter what you select. If you make to boot into the latest arch ISO (June 2016) on a USB, arch EFI boot menu hangs. After you installed arch, you may activate that option again: no difference in boot performance could be observed with the option activated or deactivated.

## Issues
## Audio
Codec has changed from the previous version, now it is Realtek ALC295:

In best case scenario just one speaker is going to work. There is a bug for that: https://bugzilla.kernel.org/show_bug.cgi?id=189331

## Touchpad
When using synaptics X11 drivers touchpad works but fails to detect palm, which causes problems when typing. Dell XPS13 had similar issue and they fixed it, but HP is not going to do that. Refer to https://github.com/advancingu/XPS13Linux/issues/3

When using libinput drivers palm detection works out of the box.

## Multimedia keys
While the keyboard backlight (f5) and airplane mode (f12) keys work without any intervention, the rest of the fn keys will be nonfunctional out of the box (unless your DE/WM provides this functionality). In the case that it does not, this can be remedied with acpid, allowing the screen brightness, volume, and multimedia back/play/forward keys to work.

Hardware names that the acpi event handler recognizes for these buttons are as follows:

Following the information and examples provided in acpid#Tips and tricks, handlers can be put in  to perform actions on all of these.

Alternatively, a quick solution to get screen backlight control working with the media keys is to use , selecting  in the settings.

## Auto Rotation
See Tablet PC#Automatic rotation for common methods of achieving this, as well as here, for a python auto-rotation script specifically written for this laptop.
