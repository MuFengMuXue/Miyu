# Acer Aspire S7-392

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the Acer Aspire S7-392 Laptop.

This page only applies to the 392 model (4th Gen Intel CPU), and may not be entirely correct for the 391 or 191 models (3rd Gen Intel CPU).

## Compatibility
The laptop works surprisingly well with Arch Linux, requiring minimal or no configuration hacking, depending on your desired setup.

## What works?
* Touchscreen
* Screen Brightness Adjustment
** Requres a window manager or desktop environment with the functionality, such as Xfce, GNOME, or MATE.
** Alternatively, a hotkey daemon such as acpid may provide hotkey functionality (Not tested).
* Keyboard Backlight (And adjustment)
* Most Keyboard Hotkeys
** Wireless Toggle may not work. acpid may work with it (Not tested)
* Wireless Networking

## What does not work, or is weird?
* Touchpad Multitouch Gestures
* Touchscreen stops working after waking up from suspend

## BIOS Setup
The BIOS Setup utility is accessed by pressing Fn+2 at the Acer Logo screen during startup.

## Disable Secure Boot
In order to install Arch on the S7 you need to disable Secure Boot from the BIOS Setup. You need to do  to set a supervisor password. Without it the option to disable Secure boot will be grayed out. Then go to  and set it to  and remove the supervisor password (by setting an empty one).

## Booting
The information in Boot loaders applies here. GRUB is confirmed to work.

## Change Boot from UEFI to BIOS
If desired, you can optionally select whether to use BIOS or UEFI when booting. This is an option in the BIOS Setup utility.

## Boot from USB
Booting from USB is possible by reordering boot devices in the BIOS setup, or by accessing the Boot Menu by pressing the "Fn" key and "=" key simultaneously (Translates to F12).

## UEFI Boot Arch
One some dual-SSD machines the disk that BIOS boots from by default is identified as  rather than . If you are running a RAID it is recommended to leave a GPT partition on both disks. If you get an error after booting that BIOS cannot find a bootable media, but drops you in the boot menu where you can select HDD and it boots from there - you have installed grub on the wrong disk.

## Graphics Drivers
With the default setup, there will be graphics tearing on the S7-392. You can check the "Tear-free video" section of the Intel graphics page for information on fixing tearing.

## Multitouch Gestures
The touchpad works well with , and with  for advanced multitouch gestures.

## Console fonts
Since some of these come with HiDPI displays the default console font is barely readable - refer to Linux console#Fonts on how to change them.

## Wi-Fi instability
This laptop uses Intel Corporation Wireless 7260 Wi-Fi chipset. With the current firmware it might have issues connecting when signal is suboptimal. Disabling power save mode on the chip improves the connection times and connection speed. See Wireless network configuration#Power saving on how to disable it and make it permanent.
