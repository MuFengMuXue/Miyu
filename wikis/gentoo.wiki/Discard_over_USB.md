The aim of this article is to enable discard/trim operational for block devices connected via the systems [USB](https://wiki.gentoo.org/wiki/USB "USB") bus.

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [What it does]](#What_it_does)
    -   [[1.2] [Why is USB special]](#Why_is_USB_special)
-   [[2] [Prerequsites]](#Prerequsites)
-   [[3] [Testing that trim is supported]](#Testing_that_trim_is_supported)
    -   [[3.1] [Find the USB attached storage]](#Find_the_USB_attached_storage)
    -   [[3.2] [Investigate support]](#Investigate_support)
    -   [[3.3] [Enabling trim]](#Enabling_trim)
    -   [[3.4] [Testing trim support]](#Testing_trim_support)
        -   [[3.4.1] [initramfs fragment]](#initramfs_fragment)
    -   [[3.5] [Auto enabling trim]](#Auto_enabling_trim)
-   [[4] [Closing notes]](#Closing_notes)

## [Overview]

### [What it does]

Trim and discard are two different names for the same thing.

The mount option is called discard, the [fstrim] command does the same thing but not as it happens. Both inform the underlying block device about space that the filesystem was using but has been returned to the free pool. In general this is a good thing as FLASH based devices can only change memory cells in one direction. They must be erased before they can be rewritten. Erase is a slow operation, much slower than write, so discard gives the block device the information it needs to erase the discarded blocks in good time before they need to be rewritten. This in turn maintains the write performance of the device.

### [Why is USB special]

With NVME or SATA connected FLASH devices, trim/discard just works. When a USB adapter is involved trim is usually disabled by default and need to be enable before it can be used.

Readers who have moved a FLASH based block device to a USB enclosure may have noticed a dmesg warning \"Discard is not supported\".

## [Prerequsites]

-   A USB3 link to the FLASH device. USB2 cannot support trim.
-   A USB3 to FLASH bridge that actually supports trim
-   [[[sys-apps/sg3_utils]](https://packages.gentoo.org/packages/sys-apps/sg3_utils)[]]
-   [[[sys-apps/usbutils]](https://packages.gentoo.org/packages/sys-apps/usbutils)[]]

** Note**\
Some USB3 to flash bridges can have their firmware upgraded to support trim.

## [Testing that trim is supported]

To get the required tools:

`root `[`#`]`emerge sys-apps/sg3_utils sys-apps/usbutils`

### [Find the USB attached storage]

Plug the drive in and inspect the end of dmesg.

If there is only one drive it will be [/dev/sda].

The remainder of this document will use [/dev/sda]. Readers are expected to adjust that to suit their own individual circumstances.

### [Investigate support]

`root `[`#`]`find /sys/ -name provisioning_mode -exec grep -H .  + | sort`

    /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode:full

Notice the `provisioning_mode:full` section in the prior output. That shows that trim is disabled even if its supported. It needs to show as `unmap`.

`root `[`#`]`sg_vpd -p bl /dev/sda`

     Block limits VPD page (SBC):
      Write same non-zero (WSNZ): 0
      Maximum compare and write length: 0 blocks [Command not implemented]
      Optimal transfer length granularity: 1 blocks
      Maximum transfer length: 65535 blocks
      Optimal transfer length: 65535 blocks
      Maximum prefetch transfer length: 65535 blocks
      Maximum unmap LBA count: 4194240
      Maximum unmap block descriptor count: 1
      Optimal unmap granularity: 1 blocks
      Unmap granularity alignment valid: false
      Unmap granularity alignment: 0 [invalid]
      Maximum write same length: 0 blocks [not reported]
      Maximum atomic transfer length: 0 blocks [not reported]
      Atomic alignment: 0 [unaligned atomic writes permitted]
      Atomic transfer length granularity: 0 [no granularity requirement
      Maximum atomic transfer length with atomic boundary: 0 blocks [not reported]
      Maximum atomic boundary size: 0 blocks [can only write atomic 1 block]

The Unmap entries are important here. Make a note of the `Maximum unmap LBA count:` value to use it later.

A report like

     Maximum unmap LBA count: 0 [Unmap command not implemented]
     Maximum unmap block descriptor count: 0 [Unmap command not implemented]
     Optimal unmap granularity: 0 blocks [not reported]

means that trim is not supported, so stop there.

`root `[`#`]`sg_readcap -l /dev/sda`

     Read Capacity results:
       Protection: prot_en=0, p_type=0, p_i_exponent=0
       Logical block provisioning: lbpme=0, lbprz=0
       Last LBA=500118191 (0x1dcf32af), Number of logical blocks=500118192
       Logical block length=512 bytes
       Logical blocks per physical block exponent=0
       Lowest aligned LBA=0
     Hence:
       Device size: 256060514304 bytes, 244198.3 MiB, 256.06 GB

The `Logical block length` from that output is necessary to take note of.

### [Enabling trim]

Change the provisioning_mode to unmap

`root `[`#`]`echo unmap > /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode`

Using the `Maximum unmap LBA count` and `Logical block length`, multiply the two numbers together to arrive at the discard_max_bytes for the device.

`root `[`#`]`echo '4194240*512' | bc `

    2147450880

Set this with

`root `[`#`]`echo 2147450880 > /sys/block/sda/queue/discard_max_bytes`

Verify That the changes happened by checking for `provisioning_mode:unmap`.

`root `[`#`]`find /sys/ -name provisioning_mode -exec grep -H .  + | sort`

    /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb2/2-2/2-2:1.0/host0/target0:0:0/0:0:0:0/scsi_disk/0:0:0:0/provisioning_mode:unmap

`provisioning_mode:disabled` indicates that trim is not supported. Revert provisioning_mode to full and stop.

That\'s trim enabled until the next boot.

### [Testing trim support]

Be sure that the filesystem(s) to be trimmed are mounted.

`root `[`#`]`fstrim -av`

This will list each filesystem with the space that it trimmed. It will be slow the first time as the entire free space pool will be trimmed. We have to trust that the drive will not erase already erased space.

** Note**\
Logical Volumes need a reboot before they will support trim

** Warning**\
Its not always that simple for LVM on SSD over USB. For some drives/installs, trim needs to be enabled before the logical volumes are started. With root in LVM, that means in the initrd. It gets worse too. Some SSDs do not become ready until they have done internal housekeeping. That can take a very long time. 10 minutes is common. 24 hours is known too.

`root `[`#`]`lsblk --discard `

    NAME                     DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
    sda                             0        4K       4G         0
    ├─sda1                          0        4K       4G         0
    └─sda2                          0        4K       4G         0
      ├─Pi4_Router-root             0        0B       0B         0

Shows that the underlying /dev/sda and /dev/sda2 support trim but it is not enabled on the logical volume Pi4_Router-root.

#### [initramfs fragment]

The following init fragment has been tested on a Pi 4 for a single SSD connected to any of the USB3 ports. It should work if a USB3 hub is in use too.

    # Fails if /dev/sda is doing internal operations, so test for it, - sleep if its not there.
    # rootwait can't wait for root in a logical volume as the LVM must be started first
    # rinse and repeat.
       echo "Waiting for sda to become ready ... maybe"
       until  [ -b "/dev/sda" ]; do
            sleep 5
       done

    # Using kernel device names is horrible. What if the device is not sda ?

    # Enable discards after sda is alive and before vgchange -ay
    # find host0 wherever it is. That will be sda.
    host0=$(find /sys/ -name provisioning_mode | grep host0)

    # and set provisioning_mode to unmap show some debug
    echo $host0
    sleep 5
    echo "unmap" > $host0

    # Once /dev/sda exists, vgchange -ay won't do nothing and return success.

    # Then start LVM
    vgchange -ay || rescue_shell "Some/All Volume Groups failed to start"

### [Auto enabling trim]

The above manual changes will not be preserved across reboots. (e)udev users need to write a rule.

Discover the the Vendor and Device ID of the USB device that represents the FLASH device.

`root `[`#`]`lsusb`

     Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
     Bus 002 Device 002: ID 174c:55aa ASMedia Technology Inc. ASM1051E SATA 6Gb/s bridge, ASM1053E SATA 6Gb/s bridge, ASM1153 SATA 3Gb/s bridge,  ASM1153E SATA 6Gb/s bridge
     Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
     Bus 001 Device 003: ID 046d:c517 Logitech, Inc. LX710 Cordless Desktop Laser
     Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
     Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Here, the SATA 6Gb/s bridge makes it easy to spot. The ID required is `ID 174c``:``55aa`. That\'s the VendorID and DeviceID parts in order.

Use that in a udev rule

[FILE] **`/etc/udev/rules.d/10-trim.rules`**

    ACTION=="add|change", ATTRS=="<VendorID>", ATTRS=="<ProductID>", SUBSYSTEM=="scsi_disk", ATTR="unmap"

Reboot to test.

`root `[`#`]`fstrim -av`

should trim all the filesystem again.

## [Closing notes]

There is a debate over using the discard option in /etc/fstab or running fstrim in a weekly or monthly cron job. The debate centers around the write amplification caused by performing needless erases cycles. As its non trivial to investigate the trim behavior of individual devices, this author recommends either the cron job approach or making fstrim part of the routine tidying up after a \@world update.