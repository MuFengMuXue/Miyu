The **Master Boot Record (MBR)** is the *de facto* standard boot sector of an IBM PC compatible with [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") as its system firmware. This includes [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") on x86 in BIOS compatibility mode (which UEFI technically calls \"Compatibility Support Module\", or CSM). The Master Boot Record is a 512-byte data structure containing system bootstrap code (on IBM PC compatibles), necessary only when used for booting (i.e. on a system drive), and a [partition table](https://wiki.gentoo.org/wiki/Partition "Partition"). The MBR was first introduced to IBM PCs with PC DOS 2.0 in 1983, hence it is sometimes also called a *DOS-type*^[\[1\]](#cite_note-1)^ or *MS-DOS* partition table.^[\[2\]](#cite_note-2)^

Due to the great success of IBM PC compatibles, the MBR is used on most multi-platform devices such as USB pen drives, and at least supported on a great variety of other platforms. Almost every external storage device (USB pen drives, SD cards, external HDDs or SSDs) is either using MBR partitioning or the [GUID Partition Table](https://wiki.gentoo.org/wiki/GUID_Partition_Table "GUID Partition Table") (GPT; the successor of the MBR on the PC platform). Virtually all partition management tools from [fdisk] to [parted] fully support an MBR-style partition scheme.

Owing its age, the Master Boot Record has a number of limitations:

-   Partitions are limited to 32-bit entries, thus the maximum partition size is circa 2.2 TB under real-world standards (512 byte sectors)
-   The maximum number of primary partitions is fixed at 4
-   BIOS implementations will not be able to address data (like a partition) above 2.2 TB

\

## Contents

-   [[1] [Kernel configuration]](#Kernel_configuration)
-   [[2] [The 2.2 TB barrier]](#The_2.2_TB_barrier)
    -   [[2.1] [The Structure of the Master Boot Record]](#The_Structure_of_the_Master_Boot_Record)
-   [[3] [Master Boot Record Partitions]](#Master_Boot_Record_Partitions)
-   [[4] [Master Boot Records Nested Within GPT Partitions]](#Master_Boot_Records_Nested_Within_GPT_Partitions)
-   [[5] [MBR Backup and Recovery]](#MBR_Backup_and_Recovery)
-   [[6] [See Also]](#See_Also)
-   [[7] [References]](#References)

## [Kernel configuration]

[KERNEL] **Enable MBR support (CONFIG_MSDOS_PARTITION)**

    -*- Enable the block layer
        Partition Types  --->
          [*] Advanced partition selection
          [*]   PC BIOS (MSDOS partition tables) support

## [The 2.2 TB barrier]

The Master Boot Record uses 32 bit values to store sector values (LBA). With the standard sector size of 512 bytes, and the highest 32 bit number of 4,294,967,295, the theoretical capacity maximum of addressable sectors is \~2048 GiB or \~2199 GB, or rounded 2.2 TB.^[\[3\]](#cite_note-3)^

Most if not all BIOS implementations use 32 bit values to access logical sectors (called [LBA](https://en.wikipedia.org/wiki/Logical_block_addressing "wikipedia:Logical block addressing"), as opposed to [C/H/S](https://en.wikipedia.org/wiki/Cylinder-head-sector "wikipedia:Cylinder-head-sector")), so any part of a partition that is defined above 2.2 TB will not be accessible and, as a result, also not bootable. Furthermore most legacy operating systems use drivers that only support 32 bit values as well, which makes 2.2 TB the hard limit in any case. No sector beyond that barrier can be accessed safely.

** Warning**\
Any partition crossing the 32 bit LBA barrier of 2.2 TB is prone to data loss!

Some operating systems, however, are able to process larger sector numbers, because they internally use more than 32 bits to store LBA values. Systems known to do that are e.g. Linux and FreeBSD. As for PCs running Microsoft Windows, any system before Windows 7 cannot be used---or at least not used safely---with partitions above the 2.2 TB barrier. Starting with Windows 7 a simple MBR tweak is possible, which is both valid within the MBR limits and the driver limits (when using the standard drivers from Microsoft). The tweak is to define the last partition just inside the 32 bit LBA range, so the start sector is a valid 32 bit LBA number and the resulting MBR data structure is absolutely correct. The partition size itself is also the largest possible 32 bit value, which roughly gives a total of 4 TB usable disk space on at least two partitions. However, considering that incompatible software that uses 32 bit LBA values for disk access is likely to destroy data when trying to access this last partition, this tweak is hardly worth the risks. Also, since Linux, FreeBSD and Windows systems that support \>32 bit MBR configurations also support the [GUID Partition Table](https://wiki.gentoo.org/wiki/GUID_Partition_Table "GUID Partition Table"), the later will always be the much safer choice.^[\[4\]](#cite_note-4)^

Some systems may be able to handle different sector sizes, like 4096 bytes (also called \"4K sectors/blocks\" or \"Advanced Format\") instead of 512 bytes. If this is the case, and with 32 bits for LBA sector numbers, the MBR limit is increased to \~17.5 TB, making one such big data partition or multiple partitions up to \>17 TB possible. The problem hereby is that most BIOS implementations do not support other sector sizes than 512 bytes, ruling out the use of 4K sectors for boot drives. Neither does most legacy software such as device drivers for IDE/ATA and SATA or system tools (disk or filesystem tools, like `fdisk` or `chkdsk`) support anything other than 512 byte sectors. Certain FireWire and USB enclosures shipped with special device drivers (for Microsoft Windows), allowing a 4K sector size and thus bigger than 2.2 TB MBR partitioning. When such drives are connected to an internal ATA/SATA bus, depending on the actual system, existing partitions may not be usable and data may be corrupted.^[\[5\]](#cite_note-5)^

### [The Structure of the Master Boot Record]

There are several variations of the Master Boot Record, all sharing a similar structure. The MBR introduced with MS-DOS 3.3 can be considered the Standard-MBR.^[\[6\]](#cite_note-6)^ Unfortunately, not all MBR schemas are compatible with all OS implementations.

An early example might look like this:

  -------------- -------------- ------- ----------------------------------------------------------------------------
  Start          Stop           Bytes   Description
  `0x00007c00`   `0x00007dbd`   446     System Bootstrap code area.
  `0x00007dbe`   `0x00007dcd`   16      Partition 1.
  `0x00007dce`   `0x00007ddd`   16      Partition 2.
  `0x00007dde`   `0x00007ded`   16      Partition 3.
  `0x00007dee`   `0x00007dfd`   16      Partition 4.
  `0x00007dfe`   `0x00007dff`   02      Boot signature `0xaa55`, binary on-disk as `55 AA`.^[\[7\]](#cite_note-7)^
  -------------- -------------- ------- ----------------------------------------------------------------------------

  : Typical Early IBM-DOS Master Boot Record

A more modern Master Boot Record implementation has several more entries at the cost of a significantly reduced bootstrap code area. This adds support for a disk formatting time-stamp, and a 32-bit disk signature for use by the OS or [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") if a Protective MBR is required for backwards compatibility.

  -------------- -------------- ------- -------------------------------------------------------
  Start          Stop           Bytes   Description
  `0x00007c00`   `0x00007cd9`   218     Bootstrap code area.
  `0x00007cda`   `0x00007cdb`   02      Padding `0x0000`.
  `0x00007cdc`   `0x00007cdc`   01      Original first physical drive (`0x80`--`0xff`)
  `0x00007cdd`   `0x00007cdd`   01      Seconds 0--59
  `0x00007cde`   `0x00007cde`   01      Minutes 0--59
  `0x00007cdf`   `0x00007cdf`   01      Hours 0--23
  `0x00007ce0`   `0x00007db7`   216     Extended bootstrap code
  `0x00007db8`   `0x00007dbb`   04      Optional disk signature.
  `0x00007dbc`   `0x00007dbd`   02      Copy protection flag (True: `0x5a5a`/False: `0x0000`)
  `0x00007dbe`   `0x00007dcd`   16      Partition 1.
  `0x00007dce`   `0x00007ddd`   16      Partition 2.
  `0x00007dde`   `0x00007ded`   16      Partition 3.
  `0x00007dee`   `0x00007dfd`   16      Partition 4.
  `0x00007dfe`   `0x00007dff`   02      Boot signature `0xaa55`.
  -------------- -------------- ------- -------------------------------------------------------

  : Typical Modern Master Boot Record

## [Master Boot Record Partitions]

  ------- ------ --------- --------------------------------------------------------------------------------------------
  Start   Stop   Bytes     Description
  0x00    0x00   1 byte    Partition boot flag. High bit set when bootable, 0x00 when not; anything else is an error.
  0x01    0x03   3 bytes   Absolute location of first sector, in Cylinder-Head-Sector format.
  0x04    0x04   1 byte    Partition type indicator
  0x05    0x07   3 bytes   Absolute location of last sector, in Cylinder-Head-Sector format.
  0x08    0x0b   4 bytes   Absolute location of first sector, in Logical Block Addressing format.
  0x0c    0x0f   4 bytes   Partition sector count.
  ------- ------ --------- --------------------------------------------------------------------------------------------

  : Partition Table Layout

The structure of individual partition entries is fixed at 16 bytes. This has a number of implications which ultimately limit the MBR format. The first byte indicates whether or not the partition is bootable, but only the 7th bit is significant. No other flags exist. Directions to the first sector of the partition follow, in the antiquated C-H-S format. The partition indicator is only one byte wide, so only 256 unique values are possible. Unfortunately, over the decades many file systems have reserved the same byte value to mean different file systems.

## [Master Boot Records Nested Within GPT Partitions]

It is possible to nest a Master Boot Record --- complete with partition table --- within an outer [GPT](https://wiki.gentoo.org/wiki/GPT "GPT") partition table. This is nearly always done for backwards compatibility by BIOS-based firmware that happen to directly support GPT partition tables or by BIOS loaded as a UEFI application.

In this case, the GPT table\'s MBR entry will contain a single partition which will be of the maximum possible partition size. The partition type at offset `0x00007dc1` will of the type `0xee`. This is called a Protective Master Boot Record.

An MBR record within a GPT partition table always have the following GUID: `024DEE41-33E7-11D3-9D69-0008C781F39F`.

## [MBR Backup and Recovery]

It is possible to backup a Master Boot Record for later recovery with a simple [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") one-liner:

`root `[`#`]`dd if=/dev/<disk> of=~/backup.mbr bs=512 count=1`

Later recovery is possible with the following command:

`root `[`#`]`dd if=backup.mbr of=/dev/<disk>`

## [See Also]

-   [Partition](https://wiki.gentoo.org/wiki/Partition "Partition") --- a means of splitting a block device up to sub-regions.
-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [CMOS BIOS Memory](https://wiki.gentoo.org/wiki/CMOS_BIOS_Memory "CMOS BIOS Memory") --- a few *bytes* of battery-backed SRAM used to preserve [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") settings and Real Time Clock data when a PC is off.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [GPT](https://wiki.gentoo.org/wiki/GPT "GPT") --- a [partitioning](https://wiki.gentoo.org/wiki/Partition "Partition") scheme widely adopted in contemporary computers to organize and manage data on storage devices.
-   [System Initialization of Intel x86 with BIOS Firmware](https://wiki.gentoo.org/wiki/System_Initialization_of_Intel_x86_with_BIOS_Firmware "System Initialization of Intel x86 with BIOS Firmware") --- the process of bringing an Intel x86 system up from a cold start.

## [References]

1.  [[[↑](#cite_ref-1)] [manpage [fdisk.8](https://www.man7.org/linux/man-pages/man8/fdisk.8.html)]]
2.  [[[↑](#cite_ref-2)] [GParted: [How-to Fix Invalid MSDOS Partition Tables](https://gparted.org/h2-fix-msdos-pt.php)]]
3.  [[[↑](#cite_ref-3)] [[https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/support-for-hard-disks-exceeding-2-tb](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/support-for-hard-disks-exceeding-2-tb)]]
4.  [[[↑](#cite_ref-4)] [[https://www.rodsbooks.com/gdisk/workarounds.html](https://www.rodsbooks.com/gdisk/workarounds.html)]]
5.  [[[↑](#cite_ref-5)] [[https://superuser.com/questions/852475/how-can-a-mbr-formatted-hard-drive-exceed-1-81-tib-capacity](https://superuser.com/questions/852475/how-can-a-mbr-formatted-hard-drive-exceed-1-81-tib-capacity)]]
6.  [[[↑](#cite_ref-6)] [[https://thestarman.pcministry.com/asm/mbr/STDMBR.htm](https://thestarman.pcministry.com/asm/mbr/STDMBR.htm)]]
7.  [[[↑](#cite_ref-7)] [[https://thestarman.pcministry.com/asm/mbr/AA55H.html](https://thestarman.pcministry.com/asm/mbr/AA55H.html)]]