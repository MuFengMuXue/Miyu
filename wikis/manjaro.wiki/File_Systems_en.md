[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-File+Systems&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=File_Systems "File Systems (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=File_Systems/tr "Dosya Sistemleri (6% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=File_Systems/fr "Systèmes de fichiers (24% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=File_Systems/ru "Файловые системы (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=File_Systems/fa "File Systems/fa (6% translated)")

## Contents

-   [[1] [Linux]](#Linux)
    -   [[1.1] [Ext2 → Ext3 → Ext4]](#Ext2_.E2.86.92_Ext3_.E2.86.92_Ext4)
        -   [[1.1.1] [Install]](#Install)
    -   [[1.2] [Btrfs]](#Btrfs)
        -   [[1.2.1] [Install]](#Install_2)
    -   [[1.3] [ReiserFS → reiser4]](#ReiserFS_.E2.86.92_reiser4)
        -   [[1.3.1] [Install]](#Install_3)
-   [[2] [Windows]](#Windows)
    -   [[2.1] [NTFS]](#NTFS)
        -   [[2.1.1] [Install]](#Install_4)
-   [[3] [DOS]](#DOS)
    -   [[3.1] [FAT16 → FAT32 (+VFAT)]](#FAT16_.E2.86.92_FAT32_.28.2BVFAT.29)
        -   [[3.1.1] [Install]](#Install_5)
    -   [[3.2] [exFAT]](#exFAT)
        -   [[3.2.1] [Install]](#Install_6)
-   [[4] [macOS]](#macOS)
    -   [[4.1] [HFS → HFS+]](#HFS_.E2.86.92_HFS.2B)
        -   [[4.1.1] [Install from AUR]](#Install_from_AUR)
-   [[5] [Others]](#Others)
    -   [[5.1] [XFS]](#XFS)
    -   [[5.2] [ZFS]](#ZFS)
-   [[6] [Comparisions]](#Comparisions)
-   [[7] [See also]](#See_also)

This page provides information on some of the filesystems commonly used in Manjaro. It also shows where and how they are used. Further information on these and other filesystems can be found in the ARCH Wiki.

A filesystem manages the space on a storage medium (hard disk, SSD \...). It makes this memory available to the operating system so that files can be saved and read again. Each of the following filesystems has advantages and disadvantages. They are mostly developed for a special purpose and are therefore used in a certain environment.

## [Linux]

filesystems that are mostly used under Linux.

Note that many filesystem drivers are already included in the Linux kernel. You may not need anything else to mount, read, or write these filesystems. But there are packages with additional tools. You may need them to format, check, repair, modify, or optimize such filesystems. So if you regularly use a filesystem, it is a good idea to install the appropriate tools.

### [][Ext2 → Ext3 → Ext4]

Ext4 was previously the default file system in Manjaro. It is the successor to the most widely used Linux file systems (Ext3, Ext2) and promises improved design, higher performance, reliability, and more features compared to its predecessors.

If you are using Ext2 or Ext3, you can convert the partition to Ext4. Ext4 uses journaling, checksums and write barriers and is therefore more robust against damage.

Currently Ext4 is fully supported in Win10 and OsX. Support for ext4 has been built in since WSL is included in Win10 (2016).

see [Ext4@kernel.org](https://ext4.wiki.kernel.org/), [Ext4@ARCH-wiki](https://wiki.archlinux.org/title/Ext4), [Ext4@wikipedia](https://de.wikipedia.org/wiki/Ext4)\
For advanced optimizations see [Improving Ext4 performance@Archwiki](https://wiki.archlinux.org/index.php/Ext4#Improving_performance).

#### [Install]

In Manjaro, e2fsprogs is already installed

### [[Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs")]

A modern **C**opy **o**n **W**rite filesystem for Linux aimed at implementing advanced features while also focusing on **fault tolerance**, **repair** and **easy administration**. [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs") not only is a filesystem, but also is partly a volume manager, software-raid, backup-tool, and it is flash-friendly.

[Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs") is now the default file system in Manjaro. Because [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs") works differently, some things may seem unfamiliar and strange. The [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs") page is therefore a good starting point for finding answers and gaining a better understanding of [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs").

Development of Btrfs started in 2007. Since that time, Btrfs is a part of the Linux kernel and is under active development. The Btrfs code base is **[stable](https://btrfs.wiki.kernel.org/index.php/Status) .** However, new features are still under development. Its main features and benefits are:

-   **Snapshots** which do not make a full copy of files
-   **RAID** - support for software-based RAID 0, RAID 1, RAID 10
-   **Self-healing** - checksums for data and metadata, automatic detection of silent data corruptions

see [Btrfs](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs"), [Btrfs@kernel.org](https://btrfs.wiki.kernel.org/index.php/Main_Page), [Btrfs@ARCH-wiki](https://wiki.archlinux.org/title/Btrfs), [Btrfs@wikipedia](https://de.wikipedia.org/wiki/Btrfs)

\

**Maintenance**

------------------------------------------------------------------------

When using snapshots, you must be particularly careful not to use up all the space on the file system -\> [Btrfs#Out_of_space](//wiki.manjaro.org/index.php?title=Btrfs#Out_of_space "Btrfs")

#### [Install]

[user \$ ][ pamac install btrfs-progs [COPY TO CLIPBOARD]]

\

### [][ReiserFS → reiser4]

ReiserFS was the first journaling filesystem to be included in the standard kernel. It was actively used by some distros some time ago, but is not currently widely used. Reiser4 is the successor to ReiserFS(3). However, Reiser4 seems not to be integrated in the kernel yet.

\

**As of kernel 6.13**

------------------------------------------------------------------------

reiserFS will no longer be supported.

see [Reiser4@ARCH-wiki](https://wiki.archlinux.org/title/Reiser4), [ReiserFS@wikipedia](https://en.wikipedia.org/wiki/ReiserFS), [Reiser4@wikipedia](https://en.wikipedia.org/wiki/Reiser4), [Reiser4@kernel.org](https://reiser4.wiki.kernel.org/)

#### [Install]

[user \$ ][ pamac install reiserfsprogs reiser4progs [COPY TO CLIPBOARD]]

\

## [Windows]

filesystems mostly used in windows

### [NTFS]

It is the most widely used filesystem on windows these days. It does exist in different versions, but unlike FAT32, all of them offer the following points:

-   Large files\> 4GB
-   Long file names with UTF16 up to 255 characters
-   Rights management, ACL
-   Journaling of metadata
-   Compression, encryption, \...

Currently there are some restrictions when using NTFS with Linux. If windows is suddenly switched off or goes into hibernating, the NTFS filesystem is left in a \"dirty-state\". When Windows starts again, NTFS is the first to be cleaned. This operation is currently not supported by the Linux driver. Then Linux shows the NTFS filesystem as read-only to be on the safe side. The same thing may happen, when NTFS becomes damaged.

see [NTFS@ARCH-wiki](https://wiki.archlinux.org/title/NTFS), [NTFS@wikipedia](https://en.wikipedia.org/wiki/NTFS)

\

**If you regularly switch between Windows and Linux**

------------------------------------------------------------------------

You should switch off \"hibernation\", \"Hybrid Boot\", \"Fast Boot\" in Windows. Then Linux has always full (read / write) access to NTFS drives.

-   [all-of-my-files-are-in-read-only-mode@forum](https://forum.manjaro.org/t/all-of-my-files-are-in-read-only-mode/83777/7)

\

**If your NTFS file system becomes corrupted**

------------------------------------------------------------------------

It is strongly recommended that you only repair the file system using the original Windows tools. Anything else is highly risky.

#### [Install]

[user \$ ][ pamac install ntfs-3g [COPY TO CLIPBOARD]]

\

## [DOS]

filesystems under DOS and early windows on a lot of floppydisks and USB-sticks

### [][FAT16 → FAT32 (+VFAT)]

This is a traditional filesystem under DOS and early Windows versions. Even today it can be found on many floppy disks, USB sticks and hard drives. It is supported by all types of operating systems and is therefore often used to exchange files, to pass them on, or to keep them accessible to both operating systems in the case of dualboot.

Even with FAT32, this comes not without its disadvantages.

-   no support for user rights or xattr
-   severely restricted file names (8.3 or LFN for VFAT, no distinction between lowercase and uppercase)
-   no files over 2GB (FAT16) 4GB (FAT32)
-   no journaling
-   not robust

\

**Warning**

------------------------------------------------------------------------

FAT Filesystems do not use journaling. Data on such filesystems is vulnerable to irreparable corruption due to *improper ejection or power outage*.

see [FAT@ARCH-wiki](https://wiki.archlinux.org/title/FAT), [FAT@wikipedia](https://en.wikipedia.org/wiki/File_Allocation_Table)

#### [Install]

[user \$ ][ pamac install dosfstools [COPY TO CLIPBOARD]]

\

### [exFAT]

Microsoft developed the exFAT (Extended File Allocation Table) in 2006 and optimized it for flash memories such as USB sticks and SD cards. It can store large files and large numbers of files, and it can manage very large partitions. It is supported by Linux, Windows, macOS and many other devices and is one of the most compatible filesystems. ExFAT is included in Linux 5.4 and higher.

-   Flash friendly
-   No support for user rights or xattr
-   Files over 4 GB
-   Checksums for metadata
-   No journal
-   Not robust

\

**Warning**

------------------------------------------------------------------------

exFAT FS does not use journaling. Data on such a filesystem is vulnerable to irreparable corruption due to *improper ejection or power outage*.

see [ExFAT@wikipedia](https://en.wikipedia.org/wiki/ExFAT)

#### [Install]

[user \$ ][ pamac install exfatprogs [COPY TO CLIPBOARD]]

\

## [macOS]

Filesystems mostly used in macOS

### [][HFS → HFS+]

see [HFSPlus@wikipedia](https://en.wikipedia.org/wiki/HFS_Plus)

#### [Install from AUR]

[user \$ ][ pamac install hfsprogs [COPY TO CLIPBOARD]]

\

## [Others]

### [XFS]

see [XFS@ARCH-wiki](https://wiki.archlinux.org/title/XFS)

### [ZFS]

see [ZFS@ARCH-wiki](https://wiki.archlinux.org/title/ZFS)

## [Comparisions]

  -------------- ------------------ ------------------- -------------- --------------
  Filesystem     Manjaro            Win10               OSX            Win9x, DOS

  btrfs          ● btrfs-progs      ▷ ExtFS, WinBtrfs   \-             \-

  ext2           ●                  ▷ ExtFS             ●

  ext3/4         ●                  ▷ ExtFS             ?

  reiser3        ● reiser4progs     ▷ RFSTool           ?              \-

  NTFS           ○ ntfs-3g\         ●                   ?
                 ▶ 5.15?? ntfs3

  FAT32          ● dosfstools       ●                   ●              ●

  exFAT          ▶ 5.4 exfatprogs   ●                   ?              ?

  HFS            ○ hfsprogs (AUR)   ?                   ●

  XFS            ?                  ▷ ExtFS             ?

  ZFS            ?                  ?                   ?

  F2FS           ?                  ?                   ?

  JFS            ?                  ?                   ?
  -------------- ------------------ ------------------- -------------- --------------

  : Possible usage of Filesystems

    ● = fully supported, additional tools to install
    ▶ = included since kernel x.x.x
    ○ = partially supported
    ▷ = possible via external tools
    ? = feel free to extend ;-)

  ------------------------- --------------------------- ----------------- ----------- -------- ------- ------- ------- -------
  Properties                btrfs                       ext4              ext3        ext2     XFS     ZFS     F2FS    JFS

  journaling                ● full                      ● ordered         ● ordered   \-       ●

  barriers                  ●                           ●                 ?           \-

  checksum                  ● full                      ◎ metadata        \-          \-

  kompression               ●,\                         \-                \-          \-
                            [zstd ▶ 4.14/5.1]

  encryption                \-                          ▶ 4.13            \-          \-

  snapshots                 ●                           \-                \-          \-

  TRIM possible             ▶ 4.3                       ▶ 2.6.33          \-          \-

  xattr, ACL                ACL                         ACL               ?           ◎        ACL

  small repair              ● auto                      ● fsck            ● fsck      ● fsck

  journal repair            ● auto 3.2                  ● fsck            ● fsck      ● fsck

  repair after power loss   ● auto, scrub               ● tune2fs, fsck   ?           \-

  RAID                      0, 1, 10                    \-                \-          \-

  since                     2009                        2008              2001        1993
  ------------------------- --------------------------- ----------------- ----------- -------- ------- ------- ------- -------

  : Some important properties

# [See also]

[Wikipedia:exFAT](https://en.wikipedia.org/wiki/ExFAT)\
[Wikipedia:Comparison of filesystems](https://en.wikipedia.org/wiki/Comparison_of_file_systems)\
[Archwiki:filesystems](https://wiki.archlinux.org/index.php/Filesystems)\