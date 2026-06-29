# Dell Chromebook 11

The Dell Chromebook 11 (and newer chromebooks in general) features a "legacy boot" mode that makes it easy to boot Linux and other operating systems. The legacy boot mode is provided by the SeaBIOS payload of coreboot. SeaBIOS behaves like a traditional BIOS that boots into the MBR of a disk, and from there into your standard boot loaders like Syslinux and GRUB.

The instructions for getting Arch Linux to work on this machine are similar to the Acer C720 Chromebook, with a few differences.

## Installation
First enable legacy boot / SeaBIOS from the developer mode of Chrome OS. Then install and boot Linux as you would on a traditional x86 BIOS system.

## Enabling Developer Mode
See the Chromebook page.

## Patching SeaBIOS
The version of SeaBIOS that ships with the Dell Chromebook does not work properly, and therefore you must patch it in order to get it to work.

* Open a crosh window with .
* Open a bash shell with the  command.
* Become superuser with
* Download the patched seabios.cbfs from and save it to Downloads.
* Patch SeaBIOS with the following commands:

 # cd ~/Downloads
 # flashrom -r image.rom
 # dd if=seabios.cbfs of=image.rom seek=2 bs=2M conv=notrunc
 # flashrom -w image.rom -i RW_LEGACY

## Enabling SeaBIOS
See Chromebook#Boot to SeaBIOS by default.

## Installing Arch Linux
Continue by following the Installation guide on the Chromebook page.

## Post Installation Configuration
For information on general Chromebook post installation configuration (hotkeys, power key handling ...) see Post installation configuration on the Chromebook page.

## Touchpad Configuration
* Edit Xorg touchpad configuration file
Add the Xorg touchpad configuration below for better usability (increases touchpad sensitivity).

If you want to remove the "Right Click" behavior from the touchpad from the bottom right area (you can still right click with two finger clicks), you should comment out the following section from

## Hardware
## Locating the Write-Protect Screw
Visit [https://www.chromium.org/chromium-os/developer-library/reference/development/developer-information-for-chrome-os-devices/dell-chromebook-11 the Dell Chromebook 11 page on The Chromium Projects.

## Removing the back of the laptop
This video describes the process of removing the back of the Dell Chromebook 11.

## Known Issues
## Touchpad right-click not functioning in X11
If the "Right Click" behavior of the touchpad is not working or it frequently fails to register left mouse clicks, try using the alternative X11 touchpad driver .

## Unable to boot into Linux after exhausting battery
This is due to the 'dev_boot_legacy' flag being stored in volatile memory, and so being lost when the power runs out. This can be solved by enabling booting to SeaBIOS by default.
