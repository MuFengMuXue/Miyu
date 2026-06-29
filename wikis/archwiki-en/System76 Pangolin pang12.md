# System76 Pangolin pang12

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| Bluetooth ||  ||
|}

This article covers the installation and configuration of Arch Linux on a System76 Pangolin model name "pang12", manufactured in 2023. Specific specifications can be found at the manufacturer's website.

Unlike many previous System76 laptops which were manufactured by Clevo, this model was made by Emdoor.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
System76 develops a special distribution (Pop!_OS) for their computers, and it comes with many tweaks and tools to ensure a seamless end-user experience. Arch does not have these out of the box, but can be installed if desired. They are not necessary for a good user experience with this particular laptop.

## Recovery partition
If you are replacing Pop!_OS on the NVMe that came with your laptop, it is recommended to leave the recovery partition intact.  The BIOS is hard-coded to attempt to boot this on , and this recovery partition can be a handy way to get out of a tight spot if something should happen that renders your Arch install unbootable.

System76 automatically updates this recovery partition from within Pop!_OS;  at present, it is not known how to update it from within Arch Linux.

It may be possible to replace the contents of this recovery partition with any LiveCD you want, but as of now it is not known if anyone has tried.

## Packages
All System76 specific packages can be found in the AUR.

; Modules
*

; Daemons
*
*
*

## Activation
Once you have installed the above, you will need to tell your computer to use them.

; Services

Enable the following services:

*
*
*

; Modules

To make sure all drivers are being loaded correctly, run ; this will automatically add necessary rules to , and execute .

## Accessibility
* Laptop comes with Pop!_OS installed by default, but is ready out of the box to be installed with Arch Linux install media.
* BIOS is fully navigable via keyboard and is simple (blue and light grey with some white), so it may work well with OCR software.
* External hardware guide and LED key
* The BIOS is accessed with the  key.  may work too.

## Firmware
Install the following:
*  (optional if you want to know when there is a BIOS update available)
*  (required if you want to update your BIOS)

To check your current BIOS version and whether there is a new version available, run  as root. Keep in-mind that this is a GTK application, so you need to be running X or Wayland for it to run. (It has no CLI -- it does not even respond to .)

To update your system to the latest firmware on the next boot, run .

## Graphics
This system comes complete with integrated (AMD) graphics. It is suggested to follow the instructions there, including support for Vulkan and hardware acceleration.

## Touchpad
Some Pangolin models have touchpad issues that can surface later. The touchpad registers mouse events when idle (interrupting sleep and suspend to RAM and consuming battery). In extreme case, the laptop mouse being unusable with multiple unintended mouse events (movement/clicks).

System76 and users suggest the following Kernel parameters:

 modprobe.blacklist=psmouse
 i8042.noaux

Sometimes the issue does not get fixed, you might have to contact support and send it for repair.

## Function keys
Keys can be changed between serving as an F key or a Function in bios. By default, (aka on new firmware updates), it will work as the following:

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Vanilla Escape Key
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || No function
|-
|  ||  ||  || No function
|-
|  ||  ||  ||
|-
|  ||  ||  || Keyboard Backlight
|-
|  ||  ||  || No function
|-
|  ||  ||  ||
|-
|  ||  ||  || Multiple, brings up display manager
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
