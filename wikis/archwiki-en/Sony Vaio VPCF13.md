# Sony Vaio VPCF13

## Xorg video issues
X server did not start properly with Nvidia drivers installed by pacman. I use one downloaded fron Nvidia web. Then I installed them by running downloaded script.
After thet, the Xserver runs just fine.

## Display backlight regulation
The previously provided solution is slightly out of date, and causes GPU acceleration related issues for those using Nvidia Drivers, possibly specific to the 340.xx drivers. The GPU issues (related to PowerMizer flags) can lead to diminished 3D application returns.

 This addition was used with 340.96 drivers with a 310M.
 The original solution was sourced from: https://code.google.com/p/vaio-f11-linux/wiki/NVIDIASetup. Relevant to F11 series, but is valid with F13 series as well.

For those using Nvidia drivers (possibly specifically 340.xx), add this line to the "Device" section of /etc/X11/xorg.conf.d/20-nvidia.conf:

 Option "RegistryDwords" "EnableBrightnessControl=1"

If the above mentioned addition does not work, the original line added in the "Device" section of /etc/X11/xorg.conf is:

 Option "RegistryDwords" "EnableBrightnessControl=1;PowerMizerEnable=0x1;PerfLevelSrc=0x3333;PowerMizerLevel=0x3;PowerMizerDefault=0x3;PowerMizerDefaultAC=0x3"

It is recommended to attempt adding one flag, testing to see if control is gained, then if not, adding another, to avoid possible unnecessary graphical collisions.

----

Previously mentioned additions/packages that may be useful, but are not up-to-date/irrelevant anymore:

 sony_laptop module addition: MODULES=(sony_laptop) in /etc/rc.conf

## Suspend to RAM
While using KDE, suspending uses pm-utils. Because of USB-3 ports it is necessary to unload module xhci_hcd before suspend. This can be done by following steps.

Then edit the file in /etc/pm/config.d/defaults with SUSPEND_MODULES="xhci_hcd"

## Sources
* https://help.ubuntu.com/community/Laptop/Sony/Vaio/FSeries/Maverick
* https://superuser.com/questions/208217/looking-for-ubuntu-10-10-driver-for-geforce-gt-425m-gpu
* https://code.google.com/p/vaio-f11-linux/wiki/AutoDimmingBacklightDaemon
