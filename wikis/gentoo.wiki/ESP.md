Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/EFI_System_Partition/de "EFI System Partition (46% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/EFI_System_Partition/hu "EFI rendszerpartíció (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/EFI_System_Partition/ru "EFI System Partition (43% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/EFI_System_Partition/zh-cn "EFI 系统分区 (4% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/EFI_System_Partition/ja "EFI システムパーティション (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/EFI_system_partition "wikipedia:EFI system partition")

The **EFI system partition (ESP)** is a [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") formatted partition containing the primary [EFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") [boot loader(s)](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") for installed operating systems.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Characteristics]](#Characteristics)
-   [[3] [Size considerations]](#Size_considerations)
-   [[4] [Optional: Mount point]](#Optional:_Mount_point)
-   [[5] [Optional: autofs]](#Optional:_autofs)
-   [[6] [Standard layout]](#Standard_layout)
-   [[7] [UEFI boot items]](#UEFI_boot_items)
    -   [[7.1] [Removable media]](#Removable_media)
-   [[8] [See also]](#See_also)
-   [[9] [References]](#References)

## [[] Kernel]

Advanced partition selection (`CONFIG_PARTITION_ADVANCED`) and EFI GUID Partition support (`CONFIG_EFI_PARTITION`) must be enabled:

[KERNEL] **Enable support for GPT**

    -*- Enable the block layer --->
       Partition Types --->
          [*] Advanced partition selection
          [*] EFI GUID Partition support

ISO8859-1 codepage must be enabled too, in order to mount the [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") EFI partition:

[KERNEL] **Enable ISO8859-1 codepage and support for VFAT**

    -*- File Systems --->
       DOS/FAT/EXFAT/NT Filesystems  --->
          <*> VFAT (Windows-95) fs support
          (437) Default codepage for FAT
          (iso8859-1) Default iocharset for FAT
       Native Language support --->
          [*] NLS ISO 8859-1  (Latin 1; Western European Languages)

## [[] Characteristics]

For creation instructions see [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#Creating_the_EFI_system_partition_.28ESP.29 "Handbook:AMD64/Installation/Disks").

[parted] ([[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]) will show it with the **boot, esp** flags:

`root `[`#`]`parted /dev/sda print`

    Model: ATA SAMSUNG SSD SM84 (scsi)
    Disk /dev/sda: 256GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:

    Number  Start   End     Size    File system  Name                          Flags
     1      1049kB  99.6MB  98.6MB  fat32        EFI System Partition          boot, esp

[gdisk] ([[[sys-apps/gptfdisk]](https://packages.gentoo.org/packages/sys-apps/gptfdisk)[]]) will show it with partition code **EF00**:

`root `[`#`]`gdisk -l /dev/sda`

    GPT fdisk (gdisk) version 1.0.1

    Partition table scan:
      MBR: protective
      BSD: not present
      APM: not present
      GPT: present

    Found valid GPT with protective MBR; using GPT.
    Disk /dev/sda: 500118192 sectors, 238.5 GiB
    Logical sector size: 512 bytes
    Disk identifier (GUID): 1B59C2C8-8795-4625-9718-4D636B005AC1
    Partition table holds up to 128 entries
    First usable sector is 34, last usable sector is 500118158
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 2669 sectors (1.3 MiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            2048          194559   94.0 MiB    EF00  EFI System Partition

Its filesystem can be created [using the **mkfs.fat** command](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#What_is_the_EFI_System_Partition_.28ESP.29.3F "Handbook:AMD64/Installation/Disks"):

`root `[`#`]`mkfs.fat -F 32 /dev/sda1`

## [[] Size considerations]

[Gentoo Handbook recommends](https://wiki.gentoo.org/wiki/Handbook:AMD64/Blocks/Disks#Default_partitioning_scheme "Handbook:AMD64/Blocks/Disks") to allocating 1 GiB for ESP, which is more than enough for any bootloader payloads like [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") kernels or Windows.

## [[] Optional: Mount point]

An entry in [[/etc/fstab]](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System#About_fstab "Handbook:AMD64/Installation/System") might be useful for manually [mounting the ESP](https://wiki.gentoo.org/wiki/EFI_stub_kernel#Installation "EFI stub kernel") but is not needed for booting.

## [[] Optional: autofs]

Mounting the ESP to [/boot/efi/], as was traditionally done, is not recommended. A nested setup complicates implementation of best-practice autofs-style mounts, as establishing the inner autofs will trigger the outer one. Mounting these partitions via autofs (and by extension keeping them unmounted whenever possible) is recommended due to the data integrity and security characteristics of VFAT file systems being effectively nonexistent.

Where [bootloader support](https://uapi-group.org/specifications/specs/boot_loader_specification/) is available use [/boot] for the [XBOOTLDR] partition and [/efi] for the [ESP]. If it is not possible to do so, a [monolithic ESP] should be mounted at [/boot]; [autofs-style](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") mounts should still be used.

** Note**\
systemd, when partitions are configured according to the [Discoverable Partitions Specification](https://uapi-group.org/specifications/specs/discoverable_partitions_specification/), can automatically mount the ESP [used for the current boot] to [/boot] or [/efi] unless a different partition is mounted there \[possibly via [/etc/fstab]\] or the mount point directory is not empty. If both [ESP] and [XBOOTLDR] exist, the [/efi] mount point is used.

For systemd (if not using the GPT auto generator):

[FILE] **`/etc/fstab`Configuring the ESP mountpoint for systemd**

    UUID=56FE-81E0        /efi       vfat    defaults,noatime,uid=0,gid=0,umask=0077,x-systemd.automount,x-systemd.idle-timeout=600 0 2

For OpenRC, use [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") to mount on-demand:

`root `[`#`]`emerge --ask net-fs/autofs`

Setup a [Direct AutoFS Mount](https://wiki.gentoo.org/wiki/AutoFS#Direct_AutoFS_mounts "AutoFS") for the ESP.

[FILE] **`/etc/autofs/auto.master`Configuring autofs to read the \'boot\' file**

    /- /etc/autofs/auto.boot --timeout=600,sync,nodev

Tell AutoFS to watch for access to the paths [/boot] and [/efi] and mount them with [options] from [device].

[FILE] **`/etc/autofs/auto.boot`Configuring the ESP mountpoint**

    /boot    -fstype=vfat,uid=0,gid=0,umask=0077     UUID=AB12-CD34
    /efi     -fstype=vfat,uid=0,gid=0,umask=0077     UUID=EF00-000A

AutoFS needs to be running to watch mountpoints:

`root `[`#`]`rc-update add autofs default`

To use the automounter before rebooting, start it manually:

`root `[`#`]`/etc/init.d/autofs start`

There is no need to add these partitions to [/etc/fstab].

## [[] Standard layout]

There is a standard layout for the ESP. Vendors and distributions are supposed to put their stuff into vendor specific directories.

`user `[`$`]`tree -L 3 /efi`

     /efi
     └── EFI
         ├── BOOT
         │   └── BOOTX64.EFI
         ├── Gentoo
         │   ├── grubx64.efi
         │   ├── initramfs-x.y.z.img
         │   ├── kernel-x.y.z.efi
         │   ├── mmx64.efi
         │   └── shimx64.efi
         ├── Linux
         │   └── gentoo-x.y.z.efi
         ├── Microsoft
         │   ├── Boot
         │   └── Recovery
         ├── refind
         │   └── refind_x64.efi
         └── systemd
             └── systemd-bootx64.efi

Here the Microsoft subtree - and also the Boot subtree^[\[1\]](#cite_note-1)^ - was created by an earlier installation of Windows 10. The Boot subtree is the fallback directory. If UEFI can\'t find any vendor specific directories it will boot from here. In a multiboot environment with properly set up vendor specific subtrees the Boot subtree can be deleted.

## [[] UEFI boot items]

Computers with UEFI provide a boot menu for bootloaders on the ESP. This boot menu is a function of the firmware and is not shown by default. Moreover there is no standard of how to get to the boot menu, but the most common way is to hold (or continuously press) a key on UEFI firmware initialization (also POST, power-on self test). Most UEFI firmware vendors will show the boot menu when one of the function keys on the connected keyboard is pressed. The boot menu may also be available from within the firmware setup (\"BIOS setup\"), which is also accessible when pressing a predefined key. Most commonly [Esc], [Del], [F1], [F2], [F10], [F11] and [F12], and on tablets also the [Volume Up] and [Volume Down] keys are used to either enter the firmware setup or display the boot menu.^[\[2\]](#cite_note-2)^ Please consult your system or mainboard manual for the exact keys and further details.

An installation tool will not only manage the bootloader and other required files on the ESP, it will also manage the addition of an \"EFI boot entry\". EFI boot entries, stored in NVRAM, are like the registration of the bootloader to the firmware. EFI will normally only list bootloaders with a boot entry in the boot menu, therefore it is not sufficient to only copy a bootloader or EFI executable to the ESP. Linux bootloaders will normally automatically add an EFI boot entry on installation of an (U)EFI bootloader, like e.g. GRUB with [grub-install].

Alternatively, a configuration tool for creating, sorting and deleting boot items is often included on UEFI compatible operating systems. The contents of the ESP is visible to these tools and creating a boot item is like choosing the medium from a given selection, then surfing through the ESP and selecting the item, e.g `bzImage-4.9.76-r1-gentoo.efi`. On Linux, [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") can be used for managing the UEFI boot items.

`root `[`#`]`efibootmgr`

    BootCurrent: 0001
    Timeout: 0 seconds
    BootOrder: 0001,0000,2001,2002,2003
    Boot0000* Windows Boot Manager  HD(1,GPT,6d98f360-cb3e-4727-8fed-5ce0c040365d,0x800,0x1400000)/\EFI\Microsoft\Boot\bootmgfw.efiRC
    Boot0001* Linux Boot Manager    HD(1,GPT,6d98f360-cb3e-4727-8fed-5ce0c040365d,0x800,0x1400000)/\EFI\systemd\systemd-bootx64.efi
    Boot2001* EFI USB Device        RC
    Boot2002* EFI DVD/CDROM RC
    Boot2003* EFI Network   RC

In case a bootloader is deleted from the ESP, UEFI will normally delete the EFI boot entry as well on startup, and the bootloader will no longer be available from the boot menu, even when the file is afterwards restored, i.e. copied to the same path on the ESP.

One single exception, where no EFI boot entry is required, is the removable media boot path. On internal (fixed) media, such as the internal HDD or SDD, it is also used as the fallback boot path on most UEFI systems.

### [[] Removable media]

EFI bootloaders on [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") are not configured as boot entries, so tools like [efibootmgr] are not required. Instead the computer firmware identifies removable boot options by looking for a predefined file name unique to the system architecture in use, in a predefined path.^[\[3\]](#cite_note-3)^

Most (U)EFI implementations support the use of the *removable media boot path* as a fallback on internal drives.^[\[4\]](#cite_note-4)^ Even though this is against specification, most systems use it in case the configured EFI boot entries are not working (i.a. a fallback), e.g. in case the boot entries are defunct (like missing files), or the EFI variables (accessible on Linux using [efivarfs](https://wiki.gentoo.org/wiki/Efivarfs "Efivarfs")) are lost, e.g. failure of the persistent store (like when the NVRAM is reset, cleared or becomes corrupted, which may occur when the \"CMOS battery\" fails). With a buggy (U)EFI it may even be the only usable bootloader on that system. Only one such fallback bootloader is possible on a specific system (i.e. architecture), due to the standardized boot path and file names.

  ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------- ----------------------------
  Architecture                                                                             Abbreviation                                                                   File name                              PE executable machine type
  [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") 32-bit                  [IA-32](https://en.wikipedia.org/wiki/IA-32 "wikipedia:IA-32")         \\efi\\boot\\boot**ia32**.efi          0x14c
  x86-64 (amd64)                                                                           [x64](https://en.wikipedia.org/wiki/x64 "wikipedia:x64")               \\efi\\boot\\boot**x64**.efi           0x8664
  Itanium                                                                                  [IA-64](https://en.wikipedia.org/wiki/IA-64 "wikipedia:IA-64")         \\efi\\boot\\boot**ia64**.efi          0x200
  ARM 32-bit                                                                               [AArch32](https://en.wikipedia.org/wiki/AArch32 "wikipedia:AArch32")   \\efi\\boot\\boot**arm**.efi           0x01c2
  ARM 64-bit                                                                               [AArch64](https://en.wikipedia.org/wiki/AArch64 "wikipedia:AArch64")   \\efi\\boot\\boot**aa64**.efi          0xAA64
  [RISC-V](https://en.wikipedia.org/wiki/RISC-V "wikipedia:RISC-V") 32-bit                                                                                        \\efi\\boot\\boot**riscv32**.efi       0x5032
  RISC-V 64-bit                                                                                                                                                           \\efi\\boot\\boot**riscv64**.efi       0x5064
  RISC-V 128-bit                                                                                                                                                          \\efi\\boot\\boot**riscv128**.efi      0x5128
  [Loongson](https://en.wikipedia.org/wiki/Loongson "wikipedia:Loongson") 32-bit   LoongArch32                                                                    \\efi\\boot\\boot**loongarch32**.efi   0x6232
  Loongson 64-bit                                                                          LoongArch64                                                                    \\efi\\boot\\boot**loongarch64**.efi   0x6264
  ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------- ----------------------------

** Note**\
To boot from removable media, the firmware has to look for compatible bootloaders on supported devices, which can be configured in the firmware setup. Like most firmwares, (U)EFI provides a hotkey to show a boot selection (formally known as \"BIOS Boot Specification\" or *BBS*), otherwise (U)EFI will use the configured default boot entry. However, a buggy (U)EFI may default to the *removable media boot path* even on internal drives.

To use the removable media boot path it is sufficient to copy the EFI bootloader to the required path and file name. Should the firmware make use of this fallback, this may also remove the ability to select between configured boot entries, meaning that boot options (as listed with [efibootmgr]) through (U)EFI will not work. Even though every EFI bootloader can be used as fallback, it may be advisable to use a boot manager that itself has the ability to select between boot options, such as [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") or [rEFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd"). From the above example for x64 (amd64):

`root `[`#`]`cp /efi/EFI/Gentoo/grubx64.efi /efi/EFI/boot/bootx64.efi `

** Note**\
The [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") file system of the [EFI System Partition] (ESP) is not case-sensitive, but case-preserving (VFAT). When VFAT has been mounted with *strict* case checking, `check=s`, the path [/efi/EFI/boot/bootx64.efi] from the above example may not work. See the [case sensitivity section in the FAT article](https://wiki.gentoo.org/wiki/FAT#Case_sensitivity "FAT") for further details. Running [tree -L 3 /efi] (when the ESP is mounted under [/efi]) will show the names in use on the individual system, to which the above command has to be changed accordingly.

** Important**\
The fallback bootloader is **not** automatically updated! Every time e.g. GRUB is re-installed (like after a version update, which may contain security fixes), it has to be copied to the fallback boot path *again*, overwriting (updating) the previous version!

The boot manager included in [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), [systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot") (formally Gummiboot), will automatically install to the *removable media boot path*. When [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] with the `boot` USE flag is updated, it is necessary to run [bootctl] again in order to update both bootloader files.

`root `[`#`]`bootctl update`

## [[] See also]

-   [Handbook:AMD64/Installation/Disks#What is the EFI System Partition (ESP)?](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#What_is_the_EFI_System_Partition_.28ESP.29.3F "Handbook:AMD64/Installation/Disks")
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")
-   [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") --- a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.
-   [REFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd") --- a boot manager for UEFI platforms.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://wiki.debian.org/UEFI#Force_grub-efi_installation_to_the_removable_media_path](https://wiki.debian.org/UEFI#Force_grub-efi_installation_to_the_removable_media_path)]]
2.  [[[↑](#cite_ref-2)] [[https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/boot-to-uefi-mode-or-legacy-bios-mode](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/boot-to-uefi-mode-or-legacy-bios-mode)]]
3.  [[[↑](#cite_ref-3)] [[UEFI 2.10 Specification, 3.5.1.1 Removable Media Boot Behavior](https://uefi.org/specs/UEFI/2.10/03_Boot_Manager.html#removable-media-boot-behavior)]]
4.  [[[↑](#cite_ref-4)] [[Debian Wiki -- UEFI: Force grub-efi installation to the removable media path](https://wiki.debian.org/UEFI#Force_grub-efi_installation_to_the_removable_media_path)]]