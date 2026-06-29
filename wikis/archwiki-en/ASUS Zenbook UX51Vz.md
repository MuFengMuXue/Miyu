# ASUS Zenbook UX51Vz

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Zenbook UX51Vz ultrabook.

See the page for its 13" variant ASUS Zenbook Prime UX31A that has mostly orthogonal information to those here (may be only partially applicable to UX51Vz)

## Installation
The UX51Vz comes in a variety of configurations, most of those sold in western Europe come with two SSDs (2x128GB or 2x256GB) in an Intel Rapid Storage (aka Intel Matrix) RAID 0 configuration.
To install Arch Linux on the UX51Vz, you can follow the official Installation guide. Since the UX51Vz uses UEFI and GPT, make sure to also read the UEFI, GPT and Arch boot process#Boot loader pages. The only way to preserve the pre-installed Windows instance is to install Arch with RAID without breaking up the RAID 0 array. See RAID with the only difference that you should not create arrays, only assemble.

To report the RAID information from the Option ROM (for instance "Intel(R) Matrix Storage Manager"):
 mdadm --detail-platform

To get general details:
 mdadm -D /dev/md127

To examine information (including members):
 mdadm -E /dev/md127

This is the important part that uses imsm (Intel Matrix) metadata! To assemble the RAID array inside the container, and/or to start it (the -e option declares the style of RAID metadata (superblock) to be used):
 mdadm -I -e imsm /dev/md127

To check the current state:
 cat /proc/mdstat

To add it to the configuration file (to be activated automagically at boot):
 mdadm --examine --scan >> /etc/mdadm.conf

Then proceed with partitioning and file systems creation as usual.

## Boot from USB medium
Press  to get into the boot menu. If the USB bootable device is not listed, enter the configuration menu and directly press  to save. Press  again on reboot: This time the USB bootable device should appear in the menu.

Select 'Boot Arch Linux (x86_64)" and press . The installation system will be booted and you will end up with a terminal.

## Function keys
The function keys are largely the same as described in ASUS Zenbook Prime UX31A. This goes for both screen backlight (which actually works out of the box on KDE as of June 2013) and keyboard backlight.

## Solid State Drive
Check Solid State Drives

## Touchpad
See  ASUS Zenbook Prime UX31A, the touchpad is the same.

## Powersave management
For automatic powersaving when on battery configure Laptop Mode Tools. For manual power saving see Power saving. Also check out Powertop.

The UX51Vz can run a little hot, this is especially true for the HiDPI variant (aka UX51VZH) because the discrete GPU is always on. Be sure to check out Linux Thermal Daemon (available as  in the AUR), which proactively controls thermal using P-states, T-states, and the Intel power clamp driver. It can do wonders for temperature management while avoiding to spin up the fans.

## Additional resources
*https://help.ubuntu.com/community/AsusZenbookPrime
*https://ubuntuforums.org/showthread.php?t=2005999
*Wikipedia:Zenbook#UX32.2C UX42 and UX52
*https://bertrandbenoit.blogspot.it/2011/07/manage-intel-raid-under-gnulinux-using.html
