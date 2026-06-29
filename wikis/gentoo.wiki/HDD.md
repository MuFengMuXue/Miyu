**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Hard_disk_drive "wikipedia:Hard disk drive")

This article describes the setup of an internal SATA or PATA (IDE) rotational **hard disk drive**.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Hardware detection]](#Hardware_detection)
    -   [[1.2] [BIOS]](#BIOS)
    -   [[1.3] [Kernel]](#Kernel)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Hardware detection]

To choose the right driver, first detect the used storage controller. [lspci](https://wiki.gentoo.org/wiki/Pciutils "Pciutils") can be used for this task:

`root `[`#`]`lspci | grep --color -E "IDE|SATA"`

(At runtime) show identification and feature info (replace `/dev/sdX` with the right device):

`root `[`#`]`hdparm -I /dev/sdX`

For more detailed information see the [hdparm](https://wiki.gentoo.org/wiki/Hdparm "Hdparm") article.

### [BIOS]

For AHCI SATA controllers, check the system\'s [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or firmware to see if if AHCI has been activated.

### [Kernel]

** Note**\
If the root partition is on this drive, the file system drivers have to be built into the kernel.

Activate the following kernel options:

[KERNEL] **`CONFIG_SCSI`, `CONFIG_BLK_DEV_SD`, `CONFIG_ATA_ACPI`, `CONFIG_SATA_PMP`, `CONFIG_SATA_AHCI`, `CONFIG_ATA_BMDMA`, `CONFIG_ATA_SFF`, `CONFIG_ATA_PIIX`**

    Device Drivers --->
      SCSI device support  --->
        <*> SCSI device support
        <*> SCSI disk support
      <*> Serial ATA and Parallel ATA drivers (libata)  --->
        [*] ATA ACPI Support

        # If the drive is connected to a SATA Port Multiplier:
        [*] SATA Port Multiplier support

        # Select the driver for the SATA controller, e.g.:
        <*> AHCI SATA support (ahci)

        # If the drive is connected to an IDE controller:
        [*] ATA BMDMA support
        [*] ATA SFF support (for legacy IDE and PATA)

        # Select the driver for the IDE controller, e.g.:
        <*> Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support (ata_piix)

## [Configuration]

Generally when configuring a hard disk drive one or more [partitions](https://wiki.gentoo.org/wiki/Partition "Partition") will need to be created and [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") written into them.

## [Usage]

Filesystems can be mounted in several ways. Notable methods include:

-   The [[mount](https://wiki.gentoo.org/wiki/Mount "Mount")] command.
-   [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")] file - Automatic mount at boot time (does not support on demand mount).
-   [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") - Automated mount on demand.
-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") - Automated mount on demand.

## [Troubleshooting]

-   See [Libata error messages](https://ata.wiki.kernel.org/index.php/Libata_error_messages)
-   See [E2fsprogs/badblocks](https://wiki.gentoo.org/wiki/E2fsprogs/badblocks "E2fsprogs/badblocks")

## [See also]

-   [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") --- provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux.

## [External resources]

-   [libata wiki](https://ata.wiki.kernel.org/)