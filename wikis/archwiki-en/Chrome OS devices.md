# Chrome OS devices

This article was created to provide information on how to get Arch installed on the series of Chrome OS devices built by Acer, HP, Samsung, Toshiba, and Google. Currently this page is being overhauled, and more model specific pages are being built with some of the information listed below.

## Introduction
## Legacy Boot Mode
All recent Intel-based Chrome OS devices (starting with the 2013 Chromebook Pixel) feature a Legacy Boot Mode, designed to allow the user to boot Linux. Legacy Boot Mode has a dedicated firmware region, , which is designed to be user-writeable (hence the 'RW' notation) and is completely separate from the ChromeOS portion of the firmware (ie, it is safe to update and cannot brick the device). It is enabled by the SeaBIOS payload of coreboot, the open-source firmware used for all Chrome OS devices (with the exception of the first generation of Chromebooks and a few early ARM models).  SeaBIOS behaves like a traditional BIOS that boots into the MBR of the disk, and from there into standard boot loaders like Syslinux and GRUB.

Models with a Core-i based SoC (Haswell, Broadwell, Skylake, KabyLake) mostly ship with a functional Legacy Boot Mode payload; updating to a 3rd party build can provide bug fixes and additional features.  Models with an Atom-based SoC (Baytrail, Braswell, Apollolake) have Legacy Boot Mode capability, but do not ship with a RW_LEGACY/SeaBIOS payload (that part of the firmware is blank).  These models require a 3rd party RW_LEGACY firmware to be loaded for Legacy Boot Mode to be functional.

## Models without Legacy Boot Mode/SeaBIOS
One of the following approaches can be taken in order to install Arch Linux on Chrome OS devices which did not ship with SeaBIOS as part of the installed firmware:

* If the device supports Legacy Boot Mode, but does not ship with a functional  payload (or does not ship with one at all), one can flash a SeaBIOS or edk2 payload to the  part of the firmware. This is 100% safe, as it writes to a user-writeable area of the firmware image which is completely separate from/does not affect ChromeOS.  The easiest way to install/update the RW_LEGACY firmware on your ChromeOS device is via MrChromebox's Firmware Utility Script, which supports the widest range of devices and offers the most up-to-date SeaBIOS and edk2 builds; one can also update the  firmware manually with Chrome OS'  (requires downloading/compiling your own build), or use John Lewis'  script (no longer supported). The MrChromebox script installs SeaBIOS for devices with older firmware, and edk2 for devices with newer firmware.
* Flash a full custom firmware which includes either a SeaBIOS or UEFI payload, and removes all the ChromeOS-specific parts.
* Flash the  part of the firmware. This method replaces the stock ChromeOS payload (depthcharge) with SeaBIOS. This is theoretically a safer approach than flashing the full firmware but there might be some limitations (e.g. no support in suspend or VMX). This is the  option in John Lewis'  script and  option in MrChromebox's.
* Take the ChrUbuntu approach which uses the Chrome OS kernel and modules.
* Build and sign your own kernel, see [https://github.com/drsn0w/chromebook_kernel_tools/blob/master/install_arch_linux.md.

The Installation process described on this page tries to cover the method of installing Arch Linux on models without SeaBIOS by flashing a custom firmware.

## Firmware write protection intro
All Chrome OS devices features firmware write protection, which restricts write access to certain regions of the flash chip. It is important to be aware of it as one might need to disable the hardware write protection as part of the installation process (to update GBB flags or flash a custom firmware).

For more details see Custom firmware for Chrome OS devices#Firmware write protection.

## Prerequisites
* Visit the ArchWiki page for your Chrome OS device.
* If there is no ArchWiki page for your device then before proceeding, gather information about the device and if you succeed in installing Arch Linux, then consider adding a new ArchWiki page for your model (you can use existing pages in Chrome OS devices as examples).
* Read this guide completely and make sure you understand all the steps before making any changes.

## Chrome OS devices
See Chrome OS devices/Chromebook for hardware comparison with details about SeaBIOS availability and storage expansion.

## General hardware recommendations and remarks
* MyDigitalSSD M.2 NGFF SSD drives are probably the most popular choice when upgrading the internal SSD of a Chrome OS device. There are multiple accounts of failing MyDigitalSSD SSD drives at the Acer C720 topic on the Arch forums [https://bbs.archlinux.org/viewtopic.php?pid=1474680#p1474680 and much more on the web. If the SSD was upgraded to a MyDigitalSSD model then it is highly recommended to backup the system and data frequently. It might be advisable to upgrade the SSD with a different brand. Notice that this might be due to a SSD firmware issue so updating the SSD firmware is highly recommended.
* Transcend MTS400 M.2 NGFF SSD drives are failing (at least with stock Coreboot firmware) when ALPM is enabled, ATM there is no SSD firmware update that fixing this bug, so it is highly advisable to disabled ALPM if a power management daemon has been installed (which enabled it), see Resolving SATA power management related errors and [https://superuser.com/questions/887916/transcend-mts400-ssd-crashes-my-acer-c720-chromebook-how-to-disable-sata-power how to disable ALPM in Chrome OS.

## Installation
The general installation procedure:

* Enable developer mode.
* ChromeOS device with functional Legacy Boot Mode/SeaBIOS:
** Enable Legacy Boot Mode.
** Set SeaBIOS as default (optional but highly recommended, requires disabling the write protection).
* ChromeOS device without functional Legacy Boot Mode:
** Flash one of the following types of custom firmware
*** Flash RW_LEGACY firmware (zero risk)
*** Flash BOOT_STUB firmware (very low risk).
*** Flash Full custom firmware (low risk).
* Prepare the installation media.
* Boot Arch Linux installation media and install Arch.

## Enabling developer mode
Developer Mode is necessary in order to access the superuser shell inside ChromeOS, which is required for making changes to the system like allow booting through SeaBIOS.

To enable developer mode:

* Press and hold the  (where  would normally be) keys, then press the  button. This enters Recovery Mode.
** Chromeboxes have a dedicated Recovery button, which should be pressed/held while powering on
* Press  (no prompt). It will ask you to confirm, then the system will revert its state and enable Developer Mode.

## Accessing the superuser shell
After you have enabled the Developer Mode, you will need to access the superuser shell. How you do this depends on whether you have configured ChromeOS or not.

## Accessing the superuser shell without logging into ChromeOS
If you have not configured ChromeOS, just press  (F2 is the "forward" arrow on the top row, →), you will see a login prompt.

* Use  as the username, it should not prompt you for a password.
* Become superuser with sudo, use the command .

## Accessing the superuser shell when logged into ChromeOS
If you have configured ChromeOS already:

* Open a crosh window with .
* Open a bash shell with the  command.
* Become superuser with sudo, use the command  to accomplish that.

## Enabling Legacy Boot Mode
If your ChromeOS device did not ship with Legacy Boot Mode support via SeaBIOS, or you prefer to install a custom firmware, then continue to #Flashing a custom firmware.

This will enable the pre-installed version of SeaBIOS through the Developer Mode screen in coreboot.

* Inside your superuser shell enter:
 # crossystem dev_boot_legacy=1
* Reboot the machine.

You can now start SeaBIOS by pressing  at the white boot splash screen.

You should now have SeaBIOS enabled on your ChromeOS device, if you choose to not set it as default then you can continue to #Installing Arch Linux.

## Boot to SeaBIOS by default
To boot SeaBIOS by default, you will need to run the set_gbb_flags.sh script, which is part of ChromeOS. The script uses flashrom and gbb_utility to read the RO_GBB firmware region, modify the flags, and write it back to flash. The GBB flags can also be set using MrChromebox's Firmware Utility Script under either ChromeOS or Arch (the latter requiring booting with specific kernel parameters to relax memory access restrictions).

* Disable the hardware write protection.
: To find the location of the hardware write-protect screw/switch/jumper and how to disable it, visit the ArchWiki page for your ChromeOS device. If there is no information about your device on the ArchWiki then turn to Developer Information for ChromeOS Devices and coreboot's Chromebooks page.
: More information about the firmware protection available in Chrome OS devices/Custom firmware#Firmware write protection.
* Switch to the superuser shell.
* Disable the software write protection.
 # flashrom --wp-disable
* Check that write protection is disabled.
 # flashrom --wp-status
* Run  with no parameters.
 # /usr/share/vboot/bin/set_gbb_flags.sh
* This will list all of the available flags.  The ones of interest to us are:
 GBB_FLAG_DEV_SCREEN_SHORT_DELAY 0x00000001
 GBB_FLAG_FORCE_DEV_SWITCH_ON 0x00000008
 GBB_FLAG_FORCE_DEV_BOOT_LEGACY 0x00000080
 GBB_FLAG_DEFAULT_DEV_BOOT_LEGACY 0x00000400
* So, to set SeaBIOS as default, with a 1s timeout, prevent accidentally exiting Developer Mode via spacebar, and ensure Legacy Boot Mode remains enabled in the event of battery drain/disconnect, we set the flags as such:
 # /usr/share/vboot/bin/set_gbb_flags.sh 0x489
* Enable back the software write protection.
 # flashrom --wp-enable

Your ChromeOS device now will boot to SeaBIOS by default, you can continue to Installing Arch Linux, if your device is booting correctly then you can optionally re-enable the hardware write protection.

## Flashing a custom firmware
* Disable the hardware write protection.
: You will need to disable hardware write-protect either using a switch, jumper or screw, or by disconnecting the battery. To find out how to disable it visit the ArchWiki page for your ChromeOS device. If there is no information about your device on the ArchWiki then turn to Developer Information for ChromeOS Devices and coreboot's Chromebooks page.
: More information about the firmware protection available in Chrome OS devices/Custom firmware#Firmware write protection.
* Enter the command to run either MrChromebox's or John Lewis's firmware script.
* After the exiting the script, be sure to copy the backed up firmware to an external storage before rebooting the system (if the script does not provide that option for you).

You should now have a custom firmware installed on your device, cross your fingers and reboot.

After flashing the firmware you can continue to #Installing Arch Linux.

## Installing Arch Linux
## Preparing the installation media
Create an Arch Linux Installer USB drive.

## Booting the installation media
* Plug the USB drive to the ChromeOS device and start SeaBIOS with  at the white boot splash screen (if SeaBIOS is not set as default).
* Press  to get a boot menu and select the number corresponding to your USB drive.

The Arch Linux installer boot menu should appear and the installation process can proceed as normal.

After finishing installing Arch Linux continue by following the Post Installation Configuration.

## Post installation configuration
## Patched kernels
It is recommended to use the official  package for most Chrome OS devices with the exception being newer devices which might need patched kernel support.

If your devices requires a patched kernel, it is advised to review the list of patches and decide if the patch list is getting decidedly small enough that you no longer require a patched kernel and instead you can use the official  package instead.

See kernels for more information.

## Video driver
See Intel graphics.

## Touchpad and touchscreen
See Touchpad Synaptics, libinput, and Touchscreen.

## Touchpad and touchscreen kernel modules
Since kernel 3.17 all the related patches merged into the upstream sources, meaning the  package in core supports these devices.

## What to do if your touchpad or touchscreen is not supported?
* Do not worry as the developers should be able to add it by request as the Chromium OS sources includes the related changes.
* You can also try to find the related commits by yourself and create a proper patch, some hints:
** Dig into your Chrome OS system, look at the obvious suspects like boot log,  and .
** The Linux kernel sources for Chromium OS are at ** Each kernel source for the latest Chromium OS release has its own branch, name convention: , where  is the Chromium OS release and  is the kernel version.
** Review the git log of ,  and .

## Touchpad configuration
There are few options how to set the touchpad:

* Visit the ArchWiki page for your Chromebook model (see Chrome OS devices/Chromebook) for touchpad xorg.conf.d file.
* Use a touchpad configuration tool.

## Chromium OS input drivers
 offers a port of the Chromium OS input driver: [https://github.com/hugegreenbug/xf86-input-cmt xf86-input-cmt as an alternative for the Synaptics input driver. It provides tweaked configuration files for most devices, and provides functionality that the Synaptics input driver does not such as palm rejection. Additionally, it enables functionality not enabled by default in the Chromium OS input driver such as tap-to-drag.

Please note, the input driver does not work under some circumstances where you have insufficient permissions to access
This will affect you if you use startx to load a DE/WM session.
If this is the case or if the driver does not load for any other cases, you should run:

 # usermod -a -G input $USER

Where $USER is the current user wanting to use the input driver.

It should also be noted that some users have reported the driver does not work in GDM but works normally after log in.
If you are affected by this, you should run:

 # usermod -a -G input gdm

After reboot, you should be able to use the touchpad normally.

## Fixing suspend
The following are instructions to fix the suspend functionality.
Users of a pre-installed SeaBIOS or John Lewis' pre-built SeaBIOS you will need this fix.
This procedure is not needed with Matt DeVillier's custom firmware since problematic ACPI wake devices (such as ) are firmware-disabled.

There have been a few alternatives discussed and those may work better for some. [https://bbs.archlinux.org/viewtopic.php?pid=1364521#p1364521

To fix suspend, the general idea is to disable the EHCI_PCI module, which interferes with the suspend cycle. There are multiple ways to achieve this.

## With kernel parameters
Add the following to your GRUB configuration:-

Then rebuild your grub config. After rebuilding your GRUB config, reboot your computer.

User reports needing to blacklist  and  instead of the above module to get suspend & resume working on an 11th gen Acer Chromebook CX5500 running Arch Linux via SeaBIOS.

## With systemd
Sometimes the synaptics touchpad, and various other parts of the laptop are used as wakeup devices causing certain movements of the laptop during suspend to end suspend. In order to disable all wakeup devices except for the laptop lid sensor, create the following  file.

{{hc|/usr/local/sbin/suspend-device-fix.sh|
#!/bin/bash

awk '{if ($1 != "LID0" && $3 == "*enabled") print $1}'  /proc/acpi/wakeup
done

exit 0
}}

Now make the file executable

Create a systemd service to execute the script on every boot.

First start . If it properly starts, then enable it to be started on bootup.

Add the following line at the end of  (if it does not exist, just create it) to prevent bad handling of EHCI USB:

Then, create the following  file. Only the Ath9k binding/unbinding lines are listed below; see the alternatives linked above for additional sound suspend handling if you experience issues.

Make sure to make the script executable.

Then rebuild your grub config.

## Fixing audio
## Apollolake based models
A potential solution for solving audio issues on Apollolake based models is using the SOF DSP driver and redefining the topology used in the audio processing pipeline by the firmware.

This will most likely solve issues relating to no audio devices being found or errors relating to topology in the kernel buffer.

The topology was created by a Sound Open Firmware maintainer and tested by MrChromebox (see Github discussion). As stated by MrChromebox, this may introduce audio scaling issues (E.g. audio output range is 0-10 instead of 0-100) and incorrect audio output device types (E.g. headphones instead of speaker).

* Install .
* Download and uncompress sof-apl-da7219.tplg.gz.
* Copy the  topology file to .
* Manually select the SOF DSP driver and specify an alternate path for the SOF firmware by editing two kernel module settings using either modprobe or another method (E.g. boot loader kernel parameters).

## Baytrail based models
Audio on most Baytrail models should work on  since fix merged into 4.19.7 to fix regression in 4.18.15, see bug report [https://lore.kernel.org/lkml/20181030143836.feo7zcxiestylxoo@picard/.

It is likely that you will also need to use  from  to turn on "Left Speaker Mixer Left DAC" and "Right Speaker Mixer Right DAC". For more information, see .

If you use max98090, you may also need to install Sound Open Firmware and symbolically link  to .

## Haswell based models
One or more of followings might help solving audio related issues, setting  module index reported the most useful. It is highly possible that you will not need to make any change.

* Create , the option  will make sure the analog output is the default (and not HDMI), the option  will notify the driver our board model which will make the built-in microphone usable (you can try instead  or ).

* Use the  file from * If having problems with headphones (perhaps no audio playing), try  (requires ) in terminal. Now, ALSA should automatically switch between channels when using headphones/speakers.

## Hotkeys
[https://support.google.com/chromebook/answer/1047364?hl=en The Chromebook function keys recognized as standard – by the kernel, it is preferable to map them accordingly to their appearance. It would also be nice to get the keys , , , ,  which in Chrome OS mapped to : , , , , .

## Using xkeyboard
 2.16-1 added a  model that enables the Chrome OS style functions for the function keys.  You can, for example, set this using .  See the  definition in  for the full mappings.

## Using keyd
keyd () is a powerful low-level tool that intercepts evdev events and allows to remap them in a flexible way (e.g. using arbitrary key combinations or allowing different behaviors on key tap or hold). Unlike other tools the chosen keys are sent using an emulated evdev device, so it works transparently on shell, X11, or Wayland.

The main configuration file is stored on .
To remap the upper row to send function key events if pressed by itself, and  when pressed together with the Meta key the following configuration may be used:

The last rows allows to remap  to , , , ,  to , and  to .

To invert the upper row behavior (i.e.  by default, multimedia keys if pressed together with ) it is sufficient to move the contenents of the two stanzas:

It is also possible to use other keys instead of , all is needed is to change the name of the stanza to the desired key (e.g. , , or  instead of ).

## Using Sxhkd
One way to set the hotkeys would be by using the Sxhkd daemon. Besides , this also requires , , and .

See for an example configuration in .

## Using Xbindkeys
Another way to configure hotkeys would be by using Xbindkeys. Besides  this also requires ,  and .

* See [https://gist.github.com/dhead666/08562a9a760b18b6e758 for an example configuration in .
* See vilefridge's xbindkeys configuration for another example.

## Alternate xbindkeys configuration
Volchange (originated in the defunct Debian User Forums) can manipulate the volume with PulseAudio instead of using . This requires  and .

* Download the raw script of the gist.
* Make it executable.

See for a matching .

## Mapping in GNOME with gsettings set
Some of the function keys can be mapped in Gnome with the advantage of HUD notifications on changes (like volume and brightness changes) which can supplement one of the mapping methods mentioned above. This [https://gist.github.com/dhead666/0b9c1cc9def939705594 linked example maps the brightness and volume actions. Notice that  is required.

## Power key and lid switch handling
## Ignore using logind
Out of the box,  will catch power key and lid switch events and handle them: it will shut down the Chromebook on a power key press, and a suspend on a lid close. However, this policy might be a bit harsh given that the power key is an ordinary key at the top right of the keyboard that might be pressed accidentally.

To configure logind to ignore power key presses and lid switches, add the lines to  below.

Then restart logind for the changes to take effect.

Power key and lid switch events will still be logged to journald by logind. See Power management#ACPI events.

## Ignore by Gnome
Install , open the Tweak Tool and under Power change the Power Button Action.

## Known issues
## Syslinux
Follow Syslinux installation instructions carefully. Try manual installation to see where the problem comes from. If you see Missing Operation System then it may be because you need to use correct boot loader binary. If syslinux does not work try another boot loader such as GRUB.
