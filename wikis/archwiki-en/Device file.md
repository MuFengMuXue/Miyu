# Device file

From Wikipedia:
:In Unix-like operating systems, a device file or special file is an interface to a device driver that appears in a file system as if it were an ordinary file.

On Linux they are in the  directory, according to the Filesystem Hierarchy Standard.

On Arch Linux the device nodes are managed by udev.

## Block devices
A block device is a special file that provides buffered access to a hardware device. For a detailed description and comparison of virtual file system devices, see Wikipedia:Device file#Block devices.

## Block device names
The beginning of the device name specifies the kernel's used driver subsystem to operate the block device.

## SCSI
Storage devices, like hard disks, SSDs and flash drives, that support the SCSI command (SCSI, SAS, UASP), ATA (PATA, SATA) or USB mass storage connection are handled by the kernel's SCSI driver subsystem. They all share the same naming scheme.

The name of these devices starts with . It is then followed by a lower-case letter starting from  for the first discovered device (),  for the second discovered device (), and so on.

Examples:

*  - device , the first discovered device.
*  - device , the fifth discovered device.

## NVMe
The name of storage devices, like SSDs, that are attached via NVM Express (NVMe) starts with . It is then followed by a number starting from  for the device controller,  for the first discovered NVMe controller,  for the second, and so on. Next is the letter "n" and a number starting from  expressing the namespace on a controller, i.e.  for first discovered namespace on first discovered controller,  for second discovered namespace on first discovered controller, and so on.

Examples:

*  - device  on controller , the first discovered device on the first discovered controller.
*  - device  on controller , the fifth discovered device on the third discovered controller.

## MMC
{{Expansion|Mention {{ic|/dev/mmcblkXboot{0,1}}}and [https://git.kernel.org/torvalds/c/97548575bef38abd06690a5a6f6816200c7e77f7.|Talk:Partitioning#mmcblk0p&#123;1,2,3,4&#125;, mmcblk0boot&#123;0,1&#125;, mmcblk0rpmb}}

SD cards, MMC cards and eMMC storage devices are handled by the kernel's  driver and name of those devices start with . It is then followed by a number starting from  for the device, i.e.  for first discovered device,  for second discovered device and so on.

Examples:

*  - device , the first discovered device.
*  - device , the fifth discovered device.

## SCSI optical disc drive
The name of optical disc drives (ODDs), that are attached using one of the interfaces supported by the SCSI driver subsystem, start with . The name is then followed by a number starting from  for the device, ie.  for the first discovered device,  for the second discovered device, and so on.

Udev also provides  that is a symbolic link to . The name will always be  regardless of the drive's supported disc types or the inserted media.

Examples:

*  - optical disc drive , the first discovered optical disc drive.
*  - optical disc drive , the fifth discovered optical disc drive.
*  - a symbolic link to .

## virtio-blk
The name of drives attached to a virtio block device (virtio-blk) interface start with . It is then followed by a lower-case letter starting from  for the first discovered device (),  for the second discovered device (), and so on.

Examples:

*  - device , the first discovered device.
*  - device , the fifth discovered device.

## Partition
Partition device names are a combination of the drive's device name and the partition number assigned to them in the partition table, i.e. . For drives whose device name ends with a number, the drive name and partition number is separated with the letter "p", i.e. .

Examples:

*  - partition  on .
*  - partition  on .
*  - partition  on .
*  - partition  on .
*  - partition  on .

## Utilities
## lsblk
The  package provides the  utility which lists block devices, for example:

In the example above, only one device is available (), and that device has three partitions ( to ), each with a different file system.

You can use the / option to enable a specific list of output columns:

The above is based on the options provided by the / argument with removal of UUID and addition of partition label and disk size, which are useful when identifying multiple disks. See  for a full list of supported columns.

## wipefs
wipefs can list or erase file system, RAID or partition-table signatures (magic strings) from the specified device to make the signatures invisible for . It does not erase the file systems themselves nor any other data from the device.

See  for more information.

For example, to erase all signatures from the device  and create a signature backup  file for each signature:

 # wipefs --all --backup /dev/sdb

## Pseudo-devices
Device nodes that do not have a physical device.

* :/dev/random, see
* :/dev/shm
* /dev/null, /dev/zero, see
* /dev/full, see
* :/dev/ttyX, where X is a number
