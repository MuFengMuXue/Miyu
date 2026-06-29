# Chrome OS devices/Custom firmware

## Why flash a custom firmware?
## Pros
* Allows the use of a UEFI coreboot payload (with MrChromebox's custom firmware).
* May reduce boot time.
* Removes the Developer Mode screen that some users find annoying.
* Enables VMX in models in which it is not active by default.
* Fixes some issues (like suspend).

## Cons
* Dangerous, and has the potential to render a device unusable.
* Cannot boot stock Chrome OS (you can install Arnold the Bat’s Chromium OS build and it should be possible to upgrade it to full blown Chrome OS with a script if the user desires).
* Custom-BIOS specific bugs may occur.

## Flashing the custom firmware
There are several approaches for flashing a custom firmware:
* Use MrChromebox's Firmware Utility Script.
* Use John Lewis' script.
* Manually with , in this case you will need to obtain the firmware by yourself or to compile it from the coreboot sources (official or Chromium OS fork).

## Disable the hardware write protection
See the Disabling the hardware write protection at the Firmware write protection.

## Flashing with MrChromebox's Firmware Utility Script
## Introduction to the firmware
MrChromebox's firmware for Chromebooks and Chromeboxes has some differences compared to other third-party custom firmware, namely:

* A UEFI implementation via the Tianocore coreboot payload.

* Updates for the Embedded Controller (EC) of some of the devices it supports, solving some bugs associated with other custom firmware.

* Built based on the latest coreboot upstream, rather than on the frozen source snapshot provided by Google.

* Source code and build scripts available on github

## Understanding the script
## What MrChromebox's Firmware Utility Script script does ?
* Automatically downloads statically compiled 64-bit versions of chromium , , and .
* Automatically detects your device/board name, current firmware, and hardware write-protect state
* Provides the option to backup your current firmware on USB (when flashing full/custom UEFI firmware).
* Automatically disables, clears, sets, and enables the software write protection as needed.
* Provides choice between RW_LEGACY, BOOT_STUB, and UEFI Full ROM firmware (types available vary based on device).
* Provides the ability to set the stock firmware's GBB flags outside of ChromeOS
* Provides the ability to remove the white Developer Mode splash screen (select models only)
* Writes and verifies the custom firmware.

## What the script does not do ?
* Does not make you a sandwich.

## Flashing the firmware
Ensure that your device is supported by looking at the supported device list. For some devices there is a legacy SeaBIOS (non-UEFI) firmware also available, although those are deprecated and will generally not receive further updates. Legacy firmware images also do not provide Embedded Controller updates.

If a UEFI ROM for your device is available, you can flash the Full ROM firmware using the Firmware Utility Script (after ensuring that you have removed your device's firmware write-protection screw). After successfully flashing the firmware, you can follow the Installation guide and install Arch Linux just like on any UEFI computer. Systemd-boot is the recommended boot loader since it installs itself by default in , the path that this firmware tries to boot from by default.

## Using the script from Arch Linux
You will need to install  and . Furthermore, to ensure that  can correctly flash the firmware it is necessary to boot with both the  and the  Kernel parameters. This is due to an issue with the chromium build of  used by the script, which is required since upstream  cannot be used to set/clear the software write-protect state or range.

## Flashing with John Lewis' script
## Understanding the script
## What John Lewis'  script does ?
* Automatically downloads Chromium OS 64bit version of .
* Backup your current firmware.
* Disables software write protection by running .
* Checks the Chromebook product name with  and download the proper custom firmware.
* Writes the custom firmware.

## What the script does not do ?
* Does not ask for confirmation.
* Does not check if the hardware write protection is disabled.
* Does not confirm the compatibility of a custom firmware to a specific Chromebook sub-model.

## Conclusions
* Make sure you disabled the hardware write protection.
* Read the FAQ.
* Confirm that your Chromebook model is supported, if your model is untested then visit the coreboot on Chromebooks Google+ community and ask for advice.

## Running the script in Chrome OS
* Access your command prompt via VT-2 ()
* Enter the command shown on the Download ROM page at John Lewis site.
* After the script exited copy the backed up firmware to an external storage before rebooting the system.

You should now have a custom firmware installed on your device, cross your fingers and reboot.

If you flashed the firmware as part of the installation process then continue by following Chrome OS devices#Installing Arch Linux, if the custom firmware boots the installation media correctly then you might want to enable back the hardware write protection.

## Running the script in Arch Linux
* Install .
* Enter the command shown on the Download ROM page at John Lewis site.
* After the script exited copy the backed up firmware to an external storage before rebooting the system.

You should now have a custom firmware installed on your device, cross you fingers and reboot.

If the custom firmware boots Arch Linux correctly then you might want to enable back the hardware write protection, although John Lewis states that it is not necessary and will only make upgrading more difficult later. However, if you do not re-enable it you want to be careful not to use flashrom.

## Manually with flashrom
The use of the upstream  package is discouraged as it is missing operations like ,  and it will not write firmware successfully to the ROM of the Chromebook unless it already been programmed externally (i.e. flashing by another device over SPI with SOIC clip), this is why it is recommended to use Chromium OS's .

## Get flashrom for Arch Linux
Download a 64-bit statically linked Chromium OS's  version from https://johnlewis.ie/flashrom and make it executable.

## Get flashrom for Chrome OS
Chrome OS already includes .

## Basic use of flashrom
* Disable software write protection before writing to the firmware chip.
 # flashrom --wp-disable

* Backup firmware from the firmware chip.
 # flashrom -r old_firmware.bin

* Write firmware to the firmware chip.
 # flashrom -w new_firmware.bin

## Flashing back stock firmware
Disable the hardware write protection and follow the how to manually flash firmware with  to flash the backup of your stock firmware.

## Unbricking your Chrome OS device
## Required tools
* Programmer, both the Raspberry Pi and the Bus Pirate are mentioned as compatible devices on the flashrom wiki. The Bus Pirate preferable as it will allow you to use Chromium OS's version of  that supports  and  flags.
* SOIC clip is recommended, see * Female jumper wires.
* If you want to use Chromium OS's  another Linux machine (32bit or 64bit) is required.

## General idea on the unbricking process
* Connect the jumper wires to the programmer and the SOIC clip.
* Connect the SOIC clip to the ROM chip.
* If your programmer is running Linux (Raspberry Pi) then modprobe the spi modules.
* If your programmer is not running Linux then connect it to your Linux machine.
* Write the firmware with , you might need to disable software write protection by running  with the  flag (this is why Chromium OS's  is handy).

## Recommended reading about unbricking
* Flashrom's wiki pages on [https://wiki.flashrom.org/ISP ISP, Bus Pirate, Raspberry Pi and SOIC8.
* coreboot's wiki page on Chromebooks.
* Examples of unbricking the C720: guide, pictures.
* Example of unbricking HP Chromebox: guide

## Firmware write protection
The firmware (coreboot and its payloads) is stored on a SPI flash chip (usually SOIC8), portions of which are protected from writing by a combination of hardware and software measures.

As long as the write protection has not been disabled and the protected range not cleared (set to 0,0), any changes made to the unprotected (RW) parts of the firmware (mainly SeaBIOS) can be reverted via either a booted Chrome OS install or Chrome OS recovery media.

There are two parts to the firmware write protection: hardware and software.

## Hardware write protection
The hardware write protection is an electrical circuit which prevents writing to the software protection special registers; it is normally enforced by the grounding of the !WP pin on the SOIC8 chip.  Thus the hardware write protection only protects directly these special registers, but indirectly also the data in the firmware chip.

Early Chromebook models (2012-2013) used a jumper or switch to implement hardware write protection.  Most models from 2014-2017 used a screw, and Kabylake/Apollolake (and newer) models from 2017 on use the battery sense line (so disconnecting the battery is necessary to disable the hardware write protect).

## Software write protection
The software write protection is implemented via a special register on the firmware chip, which contain an enabled/disabled flag, as well as one or more ranges of addresses to be protected / marked as read-only.

## Understanding the Process of Disabling the Write Protection
To fully disable the write protection one would need to:
* Disable the hardware write protection of the special software register.
* Change the value of the special software register to disable software write protection, and clear the range of the protected addresses so no data will be protected (start and end at 0).

Conclusion: If one disables the software write protection and does not enable it back, then even if the hardware write protection is re-enabled, the firmware chip will remain unprotected.

## Disabling the hardware write protection
To find the location of the hardware write-protect screw/switch/jumper and how to disable it visit the ArchWiki page for your Chromebook model (see Chromebook Models). If there is no information about your device on the ArchWiki then turn to Developer Information for Chrome OS Devices and coreboot's Chromebooks page.

## Disabling the software write protection
Chromium OS's  can manipulate the software write protection special registers.
* Read the status of the software write protection special registers.
 # flashrom --wp-status
* Disable or enable the software write protection.
 # flashrom --wp-disable
* Change software write protection addresses range.
 # flashrom --wp-range 0 0

For more details on Chromium OS's  and how to obtain it, see #Manually with flashrom.
