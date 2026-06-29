This document provides instructions on how to set up multipathing services for data storage.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Architectural overview]](#Architectural_overview)
    -   [[3.1] [Typical configuration]](#Typical_configuration)
-   [[4] [Setting up a personal configuration]](#Setting_up_a_personal_configuration)

## [Introduction]

Multipathing services, generally deployed in enterprise environments, provide a means for high performance, load-balanced, and fault-tolerant data storage either locally or via a storage area network (SAN). Multipathing facilitates a single storage device to be transparently accessed across one or more paths. For example, if there are two connections from a server Host Bus Adapter (HBA) to two Fibre Channel switches and then to a SAN, when the HBA module loads and scans the bus, it will read four paths to the SAN: the paths from the server HBA to and from each Fibre Channel switch and at the storage device. Taking advantage of this situation, Multipath allows the system make use of each path simultaneously or independently to ensure a constant and reliable connection to the data in storage. Multipath serves as a failover for all connections points in the event of losing one path making critical data always available due to redundancy in the design and implementation.

In the most basic sense, multipathing is made of two distinct parts: device mapper and multipath mtools. **Device mapper** is the first key element of this application. Administrators are probably familiar with Device Mapper from LVM, EVMS, dm-crypt, or in this case, Multipath. In short, working within the kernel space device mapper takes one block device such as [/dev/sda] (as all SAN based targets will be some type of SCSI device) and maps it to another device.

On a lower level, device mapper creates a virtual block device accepting all of the commands of a regular block device, but passes on the actual data to the real block device. As previously stated, the mapping process is all handled in the kernel space and not in user space.

**Multipath tools** is a set of userspace tools that interacts with the device mapper tools and creates structures for device handling, implementing I/O multipathing at the OS level. In a typical SAN environment there will be multiple paths to the same storage device: a fiber card (or two) on the server that connects to a switch which then connects to the actual storage itself (as in the scenario discussed above). So administrators could possibly see the same device one to four times in such a situation (each card will see the LUN twice, once for each path it has available to it). Thus, a single drive could be recognized as [sda], [sdb], [sdc], and [sdd]. If [/dev/sda] were mounted to [/san1], for instance, it would be going over the singular path from one fiber card to a switch and then to a port on the same storage device. If any of those points were to fail, the system would lose the storage device suddenly and have to unmount and remount with another device ([sdb]).

Consequently, this scenario is not ideal since it uses one out of the four possible paths. This is where the combination of multipath tools and Device Mapper are beneficial. As already explained, Device Mapper creates virtual block devices and then passes information to the real block devices.

## [Installation]

### [Emerge]

You need to emerge [[[sys-fs/multipath-tools]](https://packages.gentoo.org/packages/sys-fs/multipath-tools)[]] and [[[sys-apps/sg3_utils]](https://packages.gentoo.org/packages/sys-apps/sg3_utils)[]]. On the disk, find the `wwid`. For this either run [/lib/udev/scsi_id -g /dev/DEVICE] (provided by [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]]) or use [sg_vpd] (provided by [[[sys-apps/sg3_utils]](https://packages.gentoo.org/packages/sys-apps/sg3_utils)[]]) to do this.

`root `[`#`]`emerge --ask sys-fs/multipath-tools`

`root `[`#`]`/lib/udev/scsi_id -g /dev/DEVICE`

Udev\'s [scsi_id]\'s `-x` option will print useful disk information like environment variables for the shell, in both ASCII and escaped form.

`root `[`#`]`emerge --ask sys-apps/sg3_utils`

`root `[`#`]`/usr/bin/sg_vpd --page=di /dev/DEVICE`

Where DEVICE is the sd device, the ID will come back with a `0x6`. Replace `0x` with `3`, and you will have the proper ID that you\'ll put into the multipath `wwid` in [/etc/multipath.conf]. More on this in the next chapter.

### [Kernel]

To configure Gentoo for multipath, the kernel must have the following settings:

[KERNEL] **Adding multipath support**

    Device Drivers  --->
      SCSI device support  --->
        <*> SCSI target support
        <*> SCSI disk support
        [*] Probe all LUNs on each SCSI device
      [*] Multiple devices driver support (RAID and LVM)  --->
        <*>  Multipath I/O support
        <*>  Device mapper support
        <*>    Multipath target
            ## (Select the appropriate device from the list) (NOTE: Before kernel version 2.6.27)
        <*>      EMC CX/AX multipath support
        <*>      LSI/Engenio RDAC multipath support
        <*>      HP MSA multipath support

** Note**\
`scsi_id` is done by targets. IDE drives have two spots to which you can connect. An administrator has the ability to set a drive as a master and another drive as a slave or set to autoselect by changing the dip switches. scsi_id is similar. Each drive or Logical Unit Number (LUN) has a unique ID, which ranges from 0 to 254. A device that has ID 0 will be discovered before a device that has, for example, ID 120, because it performs a LIP (a scan of the SCSI bus for devices that respond) that starts from 0 and works its way upwards.

In the kernel menu config, make sure `CONFIG_SCSI_MULTI_LUN=y` is set to ensure the SCSI subsystem is able to probe all Logical Unit Numbers (LUNs) (This is recommended as you\'ll stop scanning after ID 0 if you have a device on an ID of `0` but not `1` and then on an ID of `2`. Simply, you\'ll get your device for ID `0` but not `2`.) or whichever device you need for SCSI, such as a QLogic 2400 card, which is in the SCSI low-level drivers area.

For a better understanding, consider the following scenarios:

There are three drives with IDs of 0,1,2. Without the \"probe all LUNs\" setting, you will see IDs 0,1,2 as sda,sdb,sdc - all devices are seen. If you delete the ID 1 drive. IDs 0,2 will still be seen. It might seem to make sense that you would see sda and sdb now (sdc would move to sdb as there is no device to fill it up). However, if you don\'t probe all LUNs, it will perform in the following manner:

Scenario 1: Without \"probe all LUNs\", the scan will start and ID 0 will be seen. ID 0 will be set to sda and then move to find ID 1. If ID 1 is not detected, scanning will stop and be considered complete having perceived to have scanned all devices even if there is a device on ID 2 or any other subsequent ID. Reboot for scenario two.

Scenario 2: If you have \"probe all LUNs\", the scan will start and detect ID 0. This ID will be assigned sda and will continue to detect the next device. If ID 1 is not detected, scanning will continue to find more devices. ID 2 will be located and assigned to be sdb. If no devices (IDs) are detected beyond that, scanning will be considered complete.

** Note**\
Although it seems that it is unfeasible or even unnecessary to have devices spaced many LUNs apart, to account for all options it is necessary to still probe all LUNs. An administrator will encounter many reasons (business or personal) for such a setup. Therefore, the second scenario would be optimal to ensure that all devices are recognized and assigned an ID in the multipath setup process.

So, once you probe all LUNs, all devices will be recognized and assigned an ID in Multipath.

## [Architectural overview]

As part of Multipath Tools, there are priority groups filled with the devices mentioned earlier. After the multipath tools package has been configured and started ([/etc/init.d/multipath start] on OpenRC), list the groups via [multipath -l]. The output will look like the following:

`root `[`#`]`multipath -l`

    EVA_SAN (3600508b4001044ee00013000031e0000)
    [size=300 GB][features="1 queue_if_no_path"][hwhandler="0"]
    \_ round-robin 0 [active]
    \_ 0:0:0:1 sda 8:0  [active]
    \_ round-robin 0 [enabled]
    \_ 0:0:1:1 sdb 8:16 [active]

    EVA_SAN2 (3600508b4001044ee0001300003880000)
    [size=300 GB][features="1 queue_if_no_path"][hwhandler="0"]
    \_ round-robin 0 [active]
    \_ 0:0:0:2 sdc 8:32 [active]
    \_ round-robin 0 [enabled]
    \_ 0:0:1:2 sdd 8:48 [active]

By default, it will pick the first priority group (the first top round-robin for the EVA_SAN2, for instance, being [sdc] ). In this instance, due to round robin it will bounce back and forth. But if one path was to fail, it would push all information to the other path and continue. Only if all the devices in a path fail will it actually fail and go to the secondary priority group.

### [Typical configuration]

A typical Multipath configuration looks like the following:

[CODE] **A typical /etc/multipath.conf file**

    defaults
    blacklist

    multipaths
      devices
      }
    }

** Important**\
On your devices, it is best to [cat /sys/block/sd(device)/device/model] and [cat /sys/block/device/sd(device)/device/vendor], placing both directly into the devices section in [/etc/multipath.conf]. You might not always see the white spacing, and it is part of the name in this case. One reason for the device section is that not every vendor\'s string is in the kernel convention and naming, and the string, as such, is not always detected as required.

A typical multipath configuration utilizing an EVA_SAN where the device information is in the kernel information regarding SAN hardware detection would look like:

[CODE] **EVA_SAN configuration**

    multipaths
      multipath
    }

## [Setting up a personal configuration]

The multipath configuration is fairly simple to accomplish because the only file that needs modification is [/etc/multipath.conf].

To begin, set the **polling interview** to how often (in seconds) path checks will be performed to ensure that the path is alive and healthy.

**selector** will be set at`"round-robin 0"`.

** Note**\
This round-robin value is the only selector value that will be used in this configuration.

**prio_callout** : This one can be quite important, and there are a number of different priorities for different devices, such as:

-   mpath_prio_alua
-   mpath_prio_emc
-   mpath_prio_hds_modular
-   mpath_prio_netapp
-   mpath_prio_tpc

** Note**\
For most people, `mpath_prio_tpc` will suffice as it\'s a conservative checker. Other devices like `mpath_prio_netapp` have special functionality for priority grouping, such as netapps.

** Note**\
In recent versions option `prio` have replaced `prio_callout`.

**path_grouping_policy** has a few different options: failover, multibus, group_by_prio.`Failover` will only have one disk per priority group.`Multibus` will put all devices into one priority group.`Group_by_prio` is done by a \"priority value.\" So routes that have the same priority value will be grouped together, the priority values being determined by the callout.

**no_path_retry** is set to`queue` as most people don\'t want data to fail to send at all. So, if all paths fail, for instance, the I/Os will queue up until the device returns and then sends everything again. Depending on the transfer, this can cause load issues.

**rr_min_io** are the number of I/Os to do per path before switching to the next I/Os in the same group. If [sda] and [sdb] were in the same group, rr_min_io would do 100 I/Os to [sda] then do 100 to [sdb] , bouncing back and forth. This is a setting to tweak for each instance to maximize performance because the data load and size of transfers/request vary by company. The default in the case is`1000` , but some may prefer a smaller number in order to switch ports more often, when possible.

**user_friendly_names** make it easier to see which device you are working with. For example, if you set user_friendly_names to`no` , then you\'ll see WWID instead of EVA_SAN for your device.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **tsunam, Matthew Summers, Richard Anderson, Steve Rucker, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*