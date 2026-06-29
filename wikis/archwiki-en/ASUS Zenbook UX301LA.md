# ASUS Zenbook UX301LA

This page contains information specific to the ASUS Zenbook UX301LA. Some of it may also be applicable to similar models, depending on the specific configuration. You might also want to look at ASUS Zenbook Prime UX31A.

## Installation
The UX301LA and similar models come with Windows 8 pre-installed, using UEFI and a GUID Partition Table scheme.

## Booting from USB
Boot the machine with the USB medium plugged in. You can try pressing  to get a boot menu and select your USB device. If it is not showing, then try booting while pressing . You will be booted into a BIOS menu. Go to  and select your USB medium. You will have to choose a specific  file - for an Arch bootable USB it is . Then under the Boot tab, change the boot device you just made to be higher priority than Windows Boot Manager. Make sure to save your changes on exit, and the system should reboot into the device.

## Partitioning
Whatever partition scheme you desire, make sure to use  if you want to keep any of the other existing partitions since  does not support the GPT scheme already on the machine. If you want to use a GParted live CD/USB, you will need to run  as root where the  is the node in  other than  before you start the GParted application.

## Installing Arch
See Installation guide.

If your machine comes with RAID 0 then add  to your mkinitcpio HOOKS and regenerate the initramfs.

When you install GRUB, follow the instructions for UEFI Systems. Your ESP (EFI system partition) should be the first partition in your scheme.

## Function Keys
All function keys except the backlight seem to work out of the box (as of Arch default kernel 3.12.7). To fix the backlight keys, add  as a kernel parameter.

## KDE and Keyboard Backlight
You may need to run the following command on login to fix keyboard backlight control.

## Display
Check HiDPI.

## Touchpad
xinput lists it as "ETPS/2 Elantech Touchpad" but it works with a  driver. See Touchpad Synaptics for detail.

## Wi-Fi
See Wireless network configuration#iwlwifi

## Battery Issues
Many have been experiencing an issue with the battery not properly charging under Linux. There is a thread about this on the Ubuntu Forums. Holding down the power button to do a clean reboot seems to be a workaround, but the issue has not been resolved yet, and those who have sent their laptops in for repair have reported that it did not resolve the issue.

## Heat
As you have probably noticed, the UX301 family of laptops will reach 80° Celsius doing the most remedial of tasks, and upwards of 90° while watching videos. You may want to consider installing and configuring .

## Helpful Links
*ASUS Zenbook Prime UX31A
*RAID
*TLP (Pre-configured power saving)
*Ubuntu UX302 Page
*Ubuntu Forums UX302 thread
*InsanelyMac(OSX86) thread with hardware info, etc.
