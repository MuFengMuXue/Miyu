# Thunderbolt

Thunderbolt 3 works out of the box with recent Linux kernel versions The Linux kernel, starting with version 4.13, supports Thunderbolt Security as well.

## Obtain firmware updates
Some vendors use fwupd to push firmware updates on Linux. For others, browsing on their website will usually allow access to the needed files.

## User device authorization
Modern Thunderbolt devices implement security modes that require user authorization when connecting devices - this is to protect from malicious devices performing DMA attacks or otherwise interfering with the hardware (see [https://trmm.net/Thunderstrike_2 Thunderstrike 2).

The modes currently supported on Linux are:
*  - No security, all devices are connected and initialized by default. In BIOS settings this is typically called Legacy mode.
*  - User authorization is required every time a device is connected. In BIOS settings this is typically called Unique ID.
*  - User authorization is required, but the device is then remembered and does not require re-authorization. In BIOS settings this is typically called One time saved key.
*  - DisplayPort functionality only, no other devices are allowed. In BIOS settings this is typically called Display Port Only.

The security level is normally configured at firmware level; it is recommended to set it to at least . The state of this setting can be queried with:

 $ cat /sys/bus/thunderbolt/devices/domain0/security

## Graphical front-ends
* GNOME has native support for authorizing devices from the UI since version 3.30
* Plasma integration is available from this git repository and from  package

## Automatically connect any device
Users who just want to connect any device without any sort of manual work can create a udev rule as in :

{{hc|/etc/udev/rules.d/99-removable.rules|2=
ACTION=="add", SUBSYSTEM=="thunderbolt", ATTR{authorized}=="0", ATTR{authorized}="1"
}}

## Forcing power
Many OEMs include a method that can be used to force the power of a Thunderbolt controller to an On state. If supported by the machine this will be exposed by the WMI bus with a sysfs attribute called force_power Forcing power may especially be useful when a connected device loses connection or the controller that switches itself off.

To force the power to be on/off, write 1 or 0 to this attribute, e.g. to force power:

 # echo 1 > /sys/bus/wmi/devices/86CCFD48-205E-4A77-9C48-2021CBEDE341/force_power

## Troubleshooting
## PCI buses are not registered
Sometimes when connecting a Thunderbolt device PCI buses might not be registered. This is apparent by having screens working while USB devices fail to register on your computer. This can be solved by issuing a PCI rescan:

 # echo 1 > /sys/bus/pci/rescan

## Automatic PCI bus rescan
For persistent issues with PCI buses not being registered, an automatic rescan can be configured using udev rules. This will trigger a rescan whenever a Thunderbolt device is connected.

Create the PCI rescan bash script:

Make it executable, then create a udev rule that triggers on thunderbolt connection:

{{hc|/etc/udev/rules.d/98-thunderbolt-rescan.rules|2=
ACTION=="change", SUBSYSTEM=="thunderbolt", ATTR{authorized}=="1", RUN+="/usr/local/bin/thunderbolt-rescan.sh"
}}

## Increasing hot-plug bus size and memory
Some motherboards' firmware does not report enough bus and memory sizes to the kernel, causing drivers loading to fail. Add the following to kernel command line to manually set the size.

 pci=hpbussize=0x33,hpmemsize=256M

## Display issues on a Thunderbolt dock
If you have a monitor connected to a Thunderbolt docking station and your system does not detect it, the station may require DisplayLink to work properly. For some docking stations this might also work better than alternative modes of connection.

## Thunderbolt not working during boot
You need to make the  module to your initramfs. See Kernel module#Automatic module loading.
