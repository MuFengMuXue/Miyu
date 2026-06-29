Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Device_file/hu "Eszközfájl (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Device_file/ja "デバイスファイル (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Device_file "wikipedia:Device file")

\
A **device file** is an interface for a device driver that appears in a [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") as if it were an ordinary file. Such files allow software to interact with a device driver. They are found in the [[/dev](https://wiki.gentoo.org/wiki//dev "/dev")] directory.

## Contents

-   [[1] [The /dev directory]](#The_.2Fdev_directory)
-   [[2] [Installation]](#Installation)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Creation]](#Creation)
    -   [[3.2] [Permissions]](#Permissions)
    -   [[3.3] [Symlinks]](#Symlinks)
-   [[4] [External resources]](#External_resources)

## [][The /dev directory]

Most Linux users understand that [/dev/sda1] is just a fast way of referring to the first partition on the first disk that the kernel found. That\'s pretty easy, right?

But consider hotpluggable devices like USB, IEEE 1394, hot-swappable PCI, etc. What is the first device for each of these? And for how long? What will the other devices be named when the first one disappears? How will that affect ongoing transactions? Wouldn\'t it be fun if a printing job were suddenly moved from a high-end laser printer to an almost-dead matrix printer just because someone decided to pull the plug on the laser printer (which just happened to be the first printer)?

Enter the device manager. A modern device manager must:

-   Run in userspace.
-   Dynamically create and remove [device files].
-   Provide consistent device naming.
-   Provide a userspace application program interface (API).

Every time a change happens within the device structure, the kernel emits a *uevent* which gets picked up by the device manager. The device manager then follows the rules declared in the [/etc/udev/rules.d], [/run/udev/rules.d] and [/lib/udev/rules.d] directories. Based on the information contained within the uevent, it finds the rule or rules it needs to trigger and performs the required actions. These actions may involve the creation or deletion of device files, and may also trigger the loading of particular firmware files into kernel memory.

\

## [Installation]

Device files in Gentoo are managed by [[udev](https://wiki.gentoo.org/wiki/Udev "Udev")], which will take care of installation of any required files.

Alternatives to [udev] include:

-   [[eudev](https://wiki.gentoo.org/wiki/Eudev "Eudev")]
-   [[mdev](https://wiki.gentoo.org/wiki/Mdev "Mdev")]
-   [[static-dev](https://wiki.gentoo.org/wiki/Old_Fashioned_Gentoo_Install "Old Fashioned Gentoo Install")]

## [Usage]

### [Creation]

Each device (either internal or peripheral) has a corresponding device file. During kernel boot time the kernel detects devices and creates device files in the virtual *[devtmpfs](https://wiki.gentoo.org/wiki/Udev#Kernel "Udev")* filesystem. Then [udev] takes over the device files and stores them in [/dev]. From this point on, [udev] is in charge of creating new device files and deleting unavailable ones.

Information can be obtained by [using [udevadm]](https://wiki.gentoo.org/wiki/Eudev#Using_udevadm "Eudev"):

Get device info using [udevadm info] followed by the device path.

`user `[`$`]`udevadm info -p /devices/pci0000:00/0000:00:1d.7`

### [Permissions]

Like other files, access to device file is restricted by filesystem permissions. The permission to access a device file have to be granted first to a user:

-   Add the user to the group the device file belongs to.

### [Symlinks]

[udev] creates for some device classes additional symlinks. The device file [/dev/cdrom] (first CD-ROM drive) and [/dev/dvd] (first DVD drive) are just symlinks to the device file [/dev/sr0] (first optical drive). You can use the symlinks in programs and config files like every other device file. Other examples are [/dev/input] for input devices or [/dev/disk] for storage devices.

## [External resources]

-   [Managing Device Files](http://swift.siphos.be/linux_sea/hardwaremanagement.html#idm3548298893536) - On Linux Sea by Sven Vermeulen
-   [K1SS --- replace eudev with the device manager of your choosing](https://k1ss.org/wiki/dev/replacing-udev)