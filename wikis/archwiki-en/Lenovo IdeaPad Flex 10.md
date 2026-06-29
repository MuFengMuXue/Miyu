# Lenovo IdeaPad Flex 10

The Lenovo Flex 10 is a flexible dual-mode laptop computer with a 10.1" screen released in 2014. It comes preinstalled with Windows 8/8.1. The Flex 10 hardware is well supported in recent Linux kernels and enjoys good driver support for most of its components.

## Hardware Support
## UEFI
Before installing any other OS (other than the default Windows 8/8.1) it is required to disable the secure boot option in the boot setup menu.

## Video
Works natively with . SNA mode, however, is unstable and can cause occasional screen freezes, using UXA mode is recommended instead.

## Touchpad
Works out of the box with .

## Touchscreen
It works out of the box. See Touchscreen to help configure the default behavior (e.g. enable two-fingers scrolling on Firefox).

## Issues
## ALPM
When suspending to RAM with ALPM  set to anything else than  the device tends to lose connection to SATA storage devices at least while running kernel version 3.18.6. This can be observed for example by entering a virtual console and executing  there. Even before the device enters to suspend state ATA related messages can be seen on the console and the device hangs on resume.

Check current policys with:

 cat /sys/class/scsi_host/host0/link_power_management_policy /sys/class/scsi_host/host1/link_power_management_policy

Change policys to max_performance before suspending to RAM:

 echo max_performance > /sys/class/scsi_host/host0/link_power_management_policy
 echo max_performance > /sys/class/scsi_host/host1/link_power_management_policy

The easiest workaround is to use TLP for power management governing with max_performance set for both SATA ALPM settings in

 # SATA aggressive link power management (ALPM):
 #   min_power, medium_power, max_performance
 SATA_LINKPWR_ON_AC=max_performance
 SATA_LINKPWR_ON_BAT=max_performance

## Touchscreen
The Elan touchscreen in the Flex does not cope well with USB power management while running on Linux kernel version 3.18.6.

Enabling automatic power control for the usb device will immedietly result the touchscreen to stop responding to input. Your usb device ids may vary.

 echo auto > '/sys/bus/usb/devices/1-4.4/power/control';

It seems to be possible to get the touchscreen back on its feet by simply setting always power on option with

 echo on > '/sys/bus/usb/devices/1-4.4/power/control';

Also after suspend or hibernate resume the touchscreen may appear as not responding. Weird enough just by reading some input from /dev/input/mouse1 will get it back to working.

 # dd if=/dev/input/mouse1 of=/dev/null bs=10 count=1

At the moment there is no known real touch input support in addition to the plain mouse emulation.
