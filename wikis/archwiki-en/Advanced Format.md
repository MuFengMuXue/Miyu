# Advanced Format

The minimum physical storage unit of a hard disk drive (HDD) is a sector. The solid state drive (SSD) equivalent is a page.Storage device firmware abstract away their physical sectors into logical sectors that software can operate on. The size of this sector refers to the size of the smallest addressable unit on the disk.

; Physical sector size: This is the smallest unit a physical storage device claims it can write atomically. For HDDs, it is the actual size of sectors in a platter. Traditionally, the physical sector size for HDDs was 512 bytes, meaning that each sector could hold 512 bytes of data. However, with the introduction of Advanced Format HDDs, the physical sector size was increased to 4096 bytes (4 KiB) for increased storage density and improved error correction capabilities. SSDs do not expose their actual NAND flash memory page size, which typically ranges from 4 KiB to 16 KiB, instead their reported physical sector size is the same as their logical sector size. For NVMe SSDs, if it is available, the [https://www.nvmexpress.org/wp-content/uploads/NVM-Express-1_2a.pdf Atomic Write Unit Power Fail (AWUPF) parameter value is used.
; Logical sector size: The logical sector size, also known as the operating system sector size, represents the size of the sectors exposed to the operating system and applications. It is the sector size used for reading from and writing to the storage device at the software level. The logical sector size can differ from the physical sector size. For example, an Advanced Format HDD with a physical sector size of 4096 bytes may still present a logical sector size of 512 bytes for compatibility with older systems and applications.

The different "layers", namely the device, stacked block devices, and file systems, should utilize the same sector sizes. If they do not, the mapping process from the firmware's translation layer, although usually transparent, will result in overhead that can be avoided.

You can check the reported logical and physical sector sizes of storage devices with lsblk:

*  is the logical sector size (addressable unit used by the operating system).
*  is the physical sector size as reported by the device.

Alternatively,  entries can be queried:

 $ cat /sys/class/block/drive/queue/physical_block_size
 $ cat /sys/class/block/drive/queue/logical_block_size

Sector sizes can also be seen in fdisk, smartctl and hdparm output.

These values again reflect what the device reports but may not be accurate for SSDs or NVMe drives, which often abstract or omit true physical characteristics.

For more detailed information on NVMe drives, such as supported LBA formats and atomic write unit granularity (if available), the following NVMe CLI commands may help:
 # nvme id-ns /dev/nvme0n1 | grep -i lbaf
 # nvme id-ctrl /dev/nvme0n1 | grep -i awupf

However, many drives will show only a single LBA format (e.g., , meaning 512-byte logical blocks), and an  value of , indicating no atomic write unit information is provided.

## Changing sector size
Some NVMe drives and "enterprise" SATA hard disk drives support changing their reported sector size using standard NVMe ( from NVM Command Set Specification 1.0 or later) or ATA ( from ATA Command Set - 4 or later) commands, respectively. For hard disk drives this changes the logical sector size in order to match the physical sector size for optimal performance. While for NVMe solid state drives, both the reported logical and physical sector size values get changed.

SATA solid state drives typically do not support changing their sector size. Exception are certain Intel SATA SSDs that can change the reported physical sector size, but not the logical sector size.Follow #Intel to change their reported physical sector size.

Changing the sector size of a drive is a complex process that requires low-level formatting. As an alternative, you can manually specify the desired sector size when creating file systems on the drive to get optimal performance. See #dm-crypt and #File systems.

## Advanced Format hard disk drives
To determine if the sector size of an Advanced Format hard disk drive can be changed, use the hdparm utility:

 # hdparm -I /dev/sdX  grep 'Sector size:'

Advanced Format drives whose Sector Configuration Log lists multiple logical sector sizes will show a list of them:

Hard disk drives which do not support multiple changeable logical sector sizes will simply report the current sector sizes. E.g., an Advanced Format 512e drive:

For optimal performance on these types of drives, ensure the #dm-crypt sector size or #File systems block size is at least 4096 bytes and aligns to it.

An Advanced Format 4Kn drive:

4Kn drives already have the optimal configuration out of the box and do not need special considerations when partitioning/formatting. They can be simply used as is.

If your SATA HDD supports multiple logical sector sizes and the optional ATA command  (usually only available in so-called "enterprise" class HDDs), you can use hdparm to change between the supported logical sector sizes.

To set it to 4096 bytes, i.e. 4Kn, run:

 # hdparm --set-sector-size 4096 --please-destroy-my-drive /dev/sdX

Afterwards, hdparm should report the logical sector size as 4096 bytes:

## NVMe solid state drives
Most solid state drives (SSDs) report their logical block address size as 512 bytes, even though they use larger blocks physically—typically 4 KiB, 8 KiB, or sometimes larger.

To check the formatted logical block address size (FLBAS) of an NVMe drive,  use the  utility in addition with Identify Namespace command:

*  is the number of extra metadata bytes per logical block address (LBA). As this is not well supported under Linux, it is best to select a format with a value of 0 here.
*  indicates which format will provide degraded, good, better or best performance.

smartctl can also display the supported logical block address sizes, but it does not provide user friendly descriptions. E.g.:

To change the logical block address size, use  and specify the preferred value with the  parameter:

This should take just a few seconds to proceed.

## Using manufacturer specific programs
If the above generic utilities do not allow changing the sector size, it may still be possible to change it using a utility from the drive's manufacturer.

## Intel
For Intel use the [https://downloadcenter.intel.com/download/29337/Intel-Memory-and-Storage-Tool-CLI-Command-Line-Interface-?product=83425 Intel Memory and Storage (MAS) Tool () with the  option. Notice that only reported physical sector size will be changed, logical sector size will remain the same.

## Seagate
Seagate provides . The utilities can be used on non-Seagate drives too since they use standard ATA and NVMe commands.

Scan all drives to find the correct one, and print info from the one you found:

 # openSeaChest_Basics --scan
 # openSeaChest_Basics -d /dev/sdX -i

Should print out information about the drive. Make sure to check the serial number.

Check the logical block sizes supported by the drive:

 # openSeaChest_Format -d /dev/sdX --showSupportedFormats

If 4096 is listed, you can change the logical sector size to it as follows:

 # openSeaChest_Format -d /dev/sdX --setSectorSize=4096 --confirm this-will-erase-data-and-may-render-the-drive-inoperable

This will take a couple of minutes, after which your drive now uses a 4 KiB native sector size.

## Partition alignment
Aligning partitions correctly avoids excessive read-modify-write cycles. A typical practice for personal computers is to have each partition's start and size aligned to 1 MiB (1 048 576 bytes) marks. This covers all common page and block size scenarios, as it is divisible by all commonly used sizes—1 MiB, 512 KiB, 128 KiB, 4 KiB, and 512 B.

* fdisk, cfdisk and sfdisk handle alignment automatically.
* gdisk and cgdisk handle alignment automatically.
** sgdisk by default only aligns the start of partitions. Use the / option to additionally enable partition size/end alignment.
* Parted only aligns the start of the partition, but not the size/end. When creating partitions, make sure to specify the partition end in mebibytes or a larger IEC binary unit.

checkpartitionsalignment.sh is a bash script that checks for alignment using Parted and awk.

## dm-crypt
As of Cryptsetup 2.4.0,  automatically detects the optimal encryption sector size for LUKS2 format However, for this to work, the device needs to report the correct default sector size, see #Changing sector size.

After using , you can check the sector size used by the LUKS2 volume with

 # cryptsetup luksDump device | grep sector

If the default sector size is incorrect, you can force create a LUKS2 container with a 4 KiB sector size and otherwise default options with:

 # cryptsetup luksFormat --sector-size=4096 device

The command will abort on an error if the requested size does not match your device:

If you encrypted your device with the wrong sector size, the device can be re-encrypted by running:

 # cryptsetup reencrypt --sector-size=4096 device

## File systems
On 4Kn disks (4096 byte physical sector size and 4096 byte logical sector size) all mkfs utilities will use a block size of 4096 bytes. On 512e (4096 byte physical sector size, 512 byte logical sector size) and 512n (512 byte physical sector size and 512 byte logical sector size) disks, each mkfs utility behaves differently.

{| class="wikitable"
|+ File system block size in bytes on non-4Kn disks
! mkfs utility !! 512e disk !! 512n disk
|-
| mkfs.bcachefs ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  || 1 || 1
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|-
|  ||  ||
|}

#  defaults to 1024 byte sectors for file systems smaller than 512 MiB and 4096 byte sectors for 512 MiB and larger.

If the storage device does not report the correct sector size, you can explicitly format the partitions according to the physical sector size.

In particular shingled magnetic recording (SMR) drives that are firmware-managed are severely and negatively impacted if using a logical sector size of 512 bytes if their physical sector size is of 4096 bytes. Those drives have different performance writing zones and remapping reallocation occurs while being idle, but during heavy active writes (e.g., RAID resilvering, backups, writing many small files, rsync, etc.), a different file system sector size could drop write speed to single digit megabytes/second, as the higher performance write areas get depleted, and the sector translation layer gets overworked on the shingled areas.

Here are some examples to set the 4096-byte sector size explicitly:

* exFAT:
* ext4:
* FAT:
* NTFS-3G:
* UDF:
* XFS:
* [https://openzfs.github.io/openzfs-docs/Project%20and%20Community/FAQ.html#advanced-format-disks ZFS:

## Known issues
## Syslinux and FAT
Syslinux does not support FAT file systems with a sector size other than 512 bytes.

## Troubleshooting
## NVMe drives fail to format
Some NVMe drives do not support the  command, which is required to change the sector size (LBA format). This is still compliant with the NVMe specification. The issue may also present itself as  or . If this is the case, review the links under References below.

To check whether your drive supports the Format NVM command:

 # nvme id-ctrl /dev/nvme0 | grep oacs

Look at the  field (Optional Admin Command Support), which is a bitmask. Format NVM support corresponds to bit 1 (value ).
If bit 1 is not set, your controller does not support Format NVM and you will not be able to change the LBA format.

Example (Format NVM not supported):

 oacs      : 0x1d

Convert  to binary:
→ Bit 1 is not set (second bit from the right is 0)
→ Format NVM is not supported

In some cases, formatting still fails even when Format NVM is supported. This is commonly seen on drives using Pyrite but notably not OPAL security, especially on Intel platforms using S0ix (Modern Standby). In other cases,  may report Format NVM as unsupported, yet formatting works after a suspend/resume cycle.

## Workarounds
* Disable S0ix (Modern Standby) in firmware (set sleep mode to S3 / S2idle)
* Add kernel parameter:
* Suspend/resume the system before formatting

## Affected models
Known on Hynix PC601, Lenovo and Dell laptops, Samsung and WD SN750 drives.
