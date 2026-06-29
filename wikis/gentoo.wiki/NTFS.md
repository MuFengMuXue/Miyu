This page contains [[changes](https://wiki.gentoo.org/index.php?title=NTFS&oldid=1317678&diff=1417908)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/NTFS/de "NTFS (10% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/NTFS/hu "NTFS (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/NTFS/ru "NTFS (69% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/NTFS/zh-cn "NTFS (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/NTFS/ja "NTFS (100% translated)")

*Not to be confused with [NFS](https://wiki.gentoo.org/wiki/NFS "NFS").*

**Resources**

[[]][NTFS](https://en.wikipedia.org/wiki/NTFS "wikipedia:NTFS")

[[]][NTFS-3G](https://en.wikipedia.org/wiki/NTFS-3G "wikipedia:NTFS-3G")

[[]][NTFS-3G documentation](https://www.tuxera.com/community/ntfs-3g-manual/)

**NTFS** (**N**ew **T**echnology **F**ile **S**ystem) is a proprietary disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") by Microsoft for Windows (NT-based) and WindowsNT-based operating systems.

There are two primary methods to achieve NTFS support when using Linux. Linux kernel 5.15 provides the new driver NTFSv3 with full support of NTFS filesystem including compression capabilities. There is also a [FUSE](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace "Filesystem in Userspace") filesystem driver called NTFS-3G - a slow but more stable and time-tested solution.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Native support]](#Native_support)
        -   [[1.1.2] [NTFS-3G (FUSE implementation)]](#NTFS-3G_.28FUSE_implementation.29)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [NTFS-3G]](#NTFS-3G)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Creation]](#Creation)
    -   [[2.2] [Mount]](#Mount)
        -   [[2.2.1] [Native support]](#Native_support_2)
        -   [[2.2.2] [FUSE (NTFS-3G)]](#FUSE_.28NTFS-3G.29)
        -   [[2.2.3] [BitLocker]](#BitLocker)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [NTFS-3G]](#NTFS-3G_2)
        -   [[3.1.1] [Force mount NTFS partition after Windows was hibernated]](#Force_mount_NTFS_partition_after_Windows_was_hibernated)
        -   [[3.1.2] [ntfsfix]](#ntfsfix)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

Before Linux kernel 5.15, the mainlined old NTFS kernel driver *had very limited functional support for NTFS*. The kernel configuration information defines support as \"partial, but safe\". The old driver could overwrite existing files but is not capable of file or directory creation, deletion, or renaming. As of Linux 5.15 the old NTFS code was replaced by new Paragon\'s in-kernel NTFS driver named \"NTFSv3\". This driver is more fully featured and supports full read/write and compression capabilities.

Most NTFS users will want to enable the [FUSE-powered NTFS-3G implementation](https://wiki.gentoo.org/wiki/NTFS#NTFS-3G_.28FUSE_implementation.29 "NTFS") for systems running pre-5.15 kernels.

#### [[] Native support]

On Linux 5.15 and later following kernel options must be enabled for new NTFSv3 driver:

[KERNEL] **Enabling new NTFSv3 driver with optional support for reading Windows compressed files (lxz/xpress) (`CONFIG_NTFS3_FS`, `CONFIG_NTFS3_LZX_XPRESS`)**

    File systems  --->
        DOS/FAT/NT Filesystems  --->
            <*> NTFS Read-Write file system support Search for <code>CONFIG_NTFS3_FS</code> to find this item.
            <*> activate support of external compressions lzx/xpress Search for <code>CONFIG_NTFS3_LZX_XPRESS</code> to find this item.

#### [][[] NTFS-3G (FUSE implementation)]

The following kernel options must be enabled for NTFS read/write capabilities over FUSE in Linux before 5.15:

[KERNEL] **Enabling NTFS over FUSE using NTFS-3G (`CONFIG_FUSE_FS`)**

    File systems  --->
        <*> FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.

After kernel version 6.8, the following kernel option must also be enabled; otherwise \"Can\'t open blockdev\" errors appear in [dmesg], and NTFS-3G cannot be used:

[KERNEL] **Needed for NTFS-3G (`CONFIG_BLK_DEV_WRITE_MOUNTED`)**

    Enable the block layer  --->
        <*> Allow writing to mounted block devices Search for <code>CONFIG_BLK_DEV_WRITE_MOUNTED</code> to find this item.

The [[[sys-fs/ntfs3g]](https://packages.gentoo.org/packages/sys-fs/ntfs3g)[]] package is also required (see the [emerge section](https://wiki.gentoo.org/wiki/NTFS#Emerge "NTFS") below).

### [[] Emerge]

#### [NTFS-3G]

** Important**\
The following package is only necessary when using NTFS-3G. It is *not required* for native support!

Because NTFS-3G is a FUSE-based filesystem, it requires user space utilities. FUSE is short for [Filesystem in Userspace](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace "Filesystem in Userspace"), which has certain disadvantages compared to a filesystem driver in kernelspace, namely less performance.

If you experience \"read only filesystem\" errors, it may be necessary to enable the `suid` USE flag.

### [USE flags for] [sys-fs/ntfs3g](https://packages.gentoo.org/packages/sys-fs/ntfs3g) [[]] [Open source read-write NTFS driver that runs under FUSE]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+fuse`](https://packages.gentoo.org/useflags/+fuse)               Enable ntfs-3g FUSE driver
  [`+mount-ntfs`](https://packages.gentoo.org/useflags/+mount-ntfs)   Install mount.ntfs symlink
  [`+ntfsprogs`](https://packages.gentoo.org/useflags/+ntfsprogs)     Enable ntfsprogs
  [`acl`](https://packages.gentoo.org/useflags/acl)                   Add support for Access Control Lists
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ntfsdecrypt`](https://packages.gentoo.org/useflags/ntfsdecrypt)   Build and install the ntfsdecrypt application.
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`suid`](https://packages.gentoo.org/useflags/suid)                 Enable setuid root program(s)
  [`xattr`](https://packages.gentoo.org/useflags/xattr)               Add support for extended attributes (filesystem-stored metadata)
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-07 17:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

After reviewing [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") and making adjustments as necessary, install the FUSE user space tools. This will enable the manipulation of NTFS filesystems:

`root `[`#`]`emerge --ask sys-fs/ntfs3g`

## [Usage]

### [Creation]

** Warning**\
The [mkfs.ntfs] command irreversibly destroys the contents of the partition it is told to format. Be sure to select the right partition before running this command!

To create an NTFS filesystem on the [/dev/sda1] partition (needs `ntfsprogs` USE flag):

`root `[`#`]`mkfs.ntfs /dev/sdyX`

Please replace [/dev/sdyX] with the actual partition you want to format.

### [Mount]

There are several ways to mount a NTFS filesystem:

-   [mount](https://wiki.gentoo.org/wiki/Mount "Mount") - Manual mounting.
-   [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") - Automatic mount at boot time.
-   [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") - Automatic mount at demand.
-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") - Automatic mount on access.

#### [Native support]

Using the native NTFS3 driver that is included in Linux kernel 5.15 and newer:

`root `[`#`]`mount -t ntfs3 /dev/device /path/to/mountpoint`

** Note**\
Running [mount /dev/device /path/to/mountpoint] may fail even when the `ntfs3` driver is loaded. One reason could be that the line `ntfs3` is not present in [/etc/filesystems], which may be the desired preset. In this case simply ensure the command is executed with `-t ntfs3`.

#### [][FUSE (NTFS-3G)]

Using the read/write capable driver provided by the ntfs3g package:

`root `[`#`]`mount -t ntfs-3g /dev/device /path/to/mountpoint`

#### [BitLocker]

See also: [UEFI Dual boot with Windows 7/8, section BitLocker](https://wiki.gentoo.org/wiki/UEFI_Dual_boot_with_Windows_7/8#BitLocker "UEFI Dual boot with Windows 7/8").

**Resources**

[[]][cryptsetup (8)](http://man7.org/linux/man-pages/man8/cryptsetup.8.html)

[[]][crypttab (5)](http://man7.org/linux/man-pages/man5/crypttab.5.html)

Linux [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") has native support for [BitLocker](https://en.wikipedia.org/wiki/BitLocker "wikipedia:BitLocker") and BitLocker to Go, except for very old variants (such as Windows Vista). While [cryptsetup] can read the BitLocker header `bitlk`, the main requirement is that the Linux kernel must have support for the encryption algorithm in use.

** Tip**\
For further details on dm-crypt, refer to the corresponding manpages: `cryptsetup (8)`, `crypttab (5)`

To use a Windows filesystem that is BitLocker encrypted on Linux, the first step is to get the BitLocker recovery key for that volume in Microsoft Windows. Example for such a recovery key:

[FILE] **`00112233-4455-6677-8899-AABBCCDDEEFF.key`BitLocker recovery key for specific volume UUID**

    001122-334455-667788-990011-223344-556677-890123-456789

** Tip**\
Consult Microsoft\'s support infrastructure on how to get the unique BitLocker recovery key. At the time of this writing, the following support webpage describes the process for Windows 10 and 11: [Find your BitLocker recovery key](https://support.microsoft.com/en-us/windows/find-your-bitlocker-recovery-key-6b71ad27-0b89-ea08-f143-056f5ab347d6).

On Linux, [cryptsetup] can automatically decrypt volumes that are configured in [/etc/crypttab]. When using a [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), see [sys-fs/cryptsetup configuration](https://wiki.gentoo.org/wiki/Systemd#sys-fs.2Fcryptsetup_configuration "Systemd") for a persistent configuration (i.e. automatic BitLocker decryption on start-up).

First, store the recovery key in a file. A convenient place to store encryption keys could be e.g. [/etc/cryptsetup-keys.d]. If the Windows\' BitLocker volume ID was, as in the above example, `00112233-4455-6677-8899-AABBCCDDEEFF`, you may want to create [/etc/cryptsetup-keys.d/00112233-4455-6677-8899-AABBCCDDEEFF.key].

`root `[`#`]`mkdir /etc/cryptsetup-keys.d `

`root `[`#`]`echo 001122-334455-667788-990011-223344-556677-890123-456789 > /etc/cryptsetup-keys.d/00112233-4455-6677-8899-AABBCCDDEEFF.key `

** Warning**\
As with all encryption keys, extreme caution is advised for granting access to such keys. Because the BitLocker key is stored in unencrypted plain text, access to the file containing the key should be restricted:

`root `[`#`]`chmod 444 /etc/cryptsetup-keys.d/*.*`

Next, find the BitLocker partition identification. This can be anything supported by Linux, such as any `UUID` or `LABEL`. The following example uses the partition UUID, identified with [gdisk] (alternatively [parted] may be used) and [lsblk]:

`root `[`#`]`gdisk -l /dev/nvme0n1 `

    GPT fdisk (gdisk) version 1.0.9

    Partition table scan:
      MBR: protective
      BSD: not present
      APM: not present
      GPT: present

    Found valid GPT with protective MBR; using GPT.
    Disk /dev/nvme0n1: 3907029168 sectors, 1.8 TiB
    Model: SSD0000SSD2G
    Sector size (logical/physical): 512/512 bytes
    Disk identifier (GUID): FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
    Partition table holds up to 128 entries
    Main partition table begins at sector 2 and ends at sector 33
    First usable sector is 34, last usable sector is 3907029134
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 4205 sectors (2.1 MiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            2048          534527   260.0 MiB   EF00  EFI system partition
       2          534528          567295   16.0 MiB    0C01  Microsoft reserved
       3          567296      3902930943   1.8 TiB     0700  Windows boot partition
       4      3902932992      3907028991   2.0 GiB     2700  Windows RE

`root `[`#`]`lsblk -o +PARTUUID `

    NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS      PARTUUID
    nvme0n1                   259:0    0  1,8T  0 disk
    ├─nvme0n1p1               259:1    0  260M  0 part                   00000000-0000-0000-0000-000000000000
    ├─nvme0n1p2               259:2    0   16M  0 part                   00000000-1111-0000-0000-000000000000
    ├─nvme0n1p3               259:3    0  1,8T  0 part                   00112233-aabb-4455-ccdd-66778899eeff
    └─nvme0n1p4               259:4    0    2G  0 part                   00000000-2222-0000-0000-000000000000

In the above example we can see that the Windows partition is partition number 3, [/dev/nvme0n1p3], and that its partition UUID or `PARTUUID` is `00112233-aabb-4455-ccdd-66778899eeff`. Note that this partition UUID is different from the volume UUID given by BitLocker on Windows.

Then, reference the recovery key file, which stores the key in plain text format, in [/etc/crypttab]:

[FILE] **`/etc/crypttab`crypttab configuration**

    windows_bitlk  PARTUUID=00112233-aabb-4455-ccdd-66778899eeff  /etc/cryptsetup-keys.d/00112233-4455-6677-8899-AABBCCDDEEFF.key  bitlk,discard,nofail

** Note**\
It will also work to use the device path, e.g. `/dev/nvme0n1p3`, directly, instead of the partition UUID, e.g. `PARTUUID=00112233-aabb-4455-ccdd-66778899eeff`, but with the disadvantage that updating the various configuration files is required with certain modifications to the system configuration, like changing device numbers: `nvme0n1` may become `nvme1n1` when SSDs are moved or an SSD is added. Also, you may choose a different name for the the mapper device, in the example `windows_bitlk`, as well as the name for the file containing the BitLocker recovery key, e.g. instead of the BitLocker UUID assigned by Windows you might want to name the file specific to its purpose, like [Windows-BitLocker-volume.key] or [Additional-Data-Volume-BitLocker.key]. Make sure to change the designations in the examples to those actually used on your system.

For [/etc/crypttab], you may add/remove options to your linking. E.g. the `nofail` option prevents a systemd startup error in case the BitLocker volume is unavailable for some reason. Without it the system boot-up will, in the case that BitLocker decryption fails, halt, giving access only to a systemd rescue shell.

To automatically mount a BitLocker encrypted NTFS partition, [/etc/fstab] must be configured as well. The NTFS partition must refer to its decrypted cryptsetup name, e.g. [/dev/mapper/windows_bitlk]. An example could be:

[FILE] **`/etc/fstab`fstab NTFS BitLocker example**

    /dev/mapper/windows_bitlk  /mnt/windows  ntfs3  noatime,discard,sys_immutable,showmeta,acl,hidden,hide_dot_files,nofail  0 0

As in [/etc/crypttab], in [/etc/fstab] the `nofail` option again prevents errors in case the BitLocker decryption failed for some reason or when the NTFS partition happens to be *dirty*, i.e. to prevent filesystem corruption the NTFS partition would not be mounted, but at the same time the startup with systemd will not fail.

After the next reboot the Windows NTFS partition should be both decrypted and mounted. The BitLocker volume can, however, also be decrypted on a running system, without a reboot:

`root `[`#`]`cryptsetup open --type bitlk --allow-discards --key-file /etc/cryptsetup-keys.d/00112233-4455-6677-8899-AABBCCDDEEFF.key /dev/nvme0n1p3 windows_bitlk `

`root `[`#`]`mount /mnt/windows `

Thereafter every operation on the NTFS partition may be started as with any regular (unencrypted) volume:

`root `[`#`]`umount /mnt/windows`

`root `[`#`]`ntfsfix -n /dev/mapper/windows_bitlk `

    Mounting volume... OK
    Processing of $MFT and $MFTMirr completed successfully.
    Checking the alternate boot sector... OK
    NTFS volume version is 3.1.
    NTFS partition /dev/mapper/windows_bitlk was processed successfully.

## [Troubleshooting]

### [NTFS-3G]

#### [Force mount NTFS partition after Windows was hibernated]

NTFS file systems controlled by Windows may be hibernated instead of cleanly shutdown in order to save on system start times. When this occurs it will not be possible to mount the NTFS partition unless the [hiberfil.sys] file is removed. The following command can be used to force-mount a hibernated partition, which *will result in the hiberfile being removed;* **all data in the file will be lost.** Windows will have to perform a clean boot in order to resume operation:

`root `[`#`]`mount -t ntfs-3g -o remove_hiberfile /path/to/device /path/to/mountpoint`

On the Windows system, in order to prevent unclean shutdowns from Windows it is possible to run [powercfg /h off] from an Administrator command prompt. This will *disable* hibernation which will most likely increase boot times when booting Windows, but has the benefit of cleanly unmounting the drive.

** Tip**\
If obtaining Administrator access to prevent hibernation is not possible on a Windows 10 system, then try the following workaround:

1.  Boot Windows to the Windows login screen.
2.  Click the power button (bottom right hand corner), then press and hold the [shift] key and click *Restart*.
3.  Choose advanced options, then reboot to the UEFI firmware settings.
4.  Once in the UEFI firmware, choose the appropriate boot entry for Linux.

This should forcing Windows to perform a clean shutdown, which will enable a clean filesystem mount for NTFS-3G.

#### [ntfsfix]

Occasionally it is necessary to fix an NTFS formatted partition from a Linux system. [ntfsfix] is the tool for the job:

`root `[`#`]`ntfsfix /dev/nvme0n1p3`

    Mounting volume... $MFTMirr does not match $MFT (record 3).
    FAILED
    Attempting to correct errors...
    Processing $MFT and $MFTMirr...
    Reading $MFT... OK
    Reading $MFTMirr... OK
    Comparing $MFTMirr to $MFT... FAILED
    Correcting differences in $MFTMirr record 3...OK
    Processing of $MFT and $MFTMirr completed successfully.
    Setting required flags on partition... OK
    Going to empty the journal ($LogFile)... OK
    Checking the alternate boot sector... OK
    NTFS volume version is 3.1.
    NTFS partition /dev/nvme0n1p3 was processed successfully.

## [See also]

-   [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") --- [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows).
-   [Dislocker](https://wiki.gentoo.org/wiki/Dislocker "Dislocker") --- [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE")-based [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") driver capable of reading [NTFS] BitLocker encrypted partitions.
-   [UEFI Dual boot with Windows 7/8](https://wiki.gentoo.org/wiki/UEFI_Dual_boot_with_Windows_7/8 "UEFI Dual boot with Windows 7/8") --- describes how to dual boot Microsoft Windows on a UEFI computer.

## [External resources]

-   [NTFS at Microsoft\'s TechNet](https://technet.microsoft.com/en-us/library/cc758691%28v=ws.10%29.aspx)
-   [Linux kernel NTFS filesystem documentation](https://docs.kernel.org/filesystems/ntfs.html)
-   [Linux kernel NTFS3 filesystem documentation](https://docs.kernel.org/filesystems/ntfs3.html)

## [References]