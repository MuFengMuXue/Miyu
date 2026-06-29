This page contains [[changes](https://wiki.gentoo.org/index.php?title=FAT&oldid=1432557&diff=1432862)] which are not marked for translation.

Other languages:

-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/FAT/it "FAT (43% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/FAT/hu "FAT (94% translated)")
-   [русский](https://wiki.gentoo.org/wiki/FAT/ru "FAT (40% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/FAT/zh-cn "FAT (93% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/FAT/ja "FAT (48% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/File_Allocation_Table "wikipedia:File Allocation Table")

The **File Allocation Table (FAT)** - [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows). Currently a later revision of FAT (FAT32) is used for [USB](https://wiki.gentoo.org/wiki/USB "USB") flash disks.^[\[1\]](#cite_note-1)^ It has made its way over to Linux systems and has official support in the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel").

Although FAT32 lacks many of the features inherent in modern file systems, this filesystem can still be found in modern computers, for example, when using [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"). In 2006 Microsoft has developed a new version of FAT (exFAT) that is not backward compatible with the previous version. See the [exFAT](https://wiki.gentoo.org/wiki/ExFAT "ExFAT") article for more info.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Snippet]](#Snippet)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Formatting]](#Formatting)
    -   [[2.2] [Case sensitivity]](#Case_sensitivity)
        -   [[2.2.1] [Manual mount options]](#Manual_mount_options)
        -   [[2.2.2] [Problem cases]](#Problem_cases)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Slow file transfer speeds]](#Slow_file_transfer_speeds)
    -   [[3.2] [Alternative operating system compatible filesystems]](#Alternative_operating_system_compatible_filesystems)
    -   [[3.3] [UTF-8/UTF-16 character hardware bugs]](#UTF-8.2FUTF-16_character_hardware_bugs)
    -   [[3.4] [Unsorted files and folders]](#Unsorted_files_and_folders)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Kernel]

[KERNEL] **Enable FAT support (`CONFIG_VFAT_FS`)**

    File systems  --->
       DOS/FAT/NT Filesystems  --->
          < > MSDOS fs support
          <*> VFAT (Windows-95) fs support
          (437) Default codepage for FAT
          (iso8859-1) Default iocharset for FAT
          [ ]   Enable FAT UTF-8 option by default
       -*- Native language support  --->
          (iso8859-1) Default NLS Option
          <*>   Codepage 437 (United States, Canada)
          <*>   NLS ISO 8859-1  (Latin 1; Western European Languages)
          -*-   NLS UTF-8

#### [Snippet]

[FILE] **`/etc/kernel/config.d/esp-linux6-1-111.config`**

    CONFIG_FAT_FS=y
    CONFIG_MSDOS_FS=y
    CONFIG_VFAT_FS=y
    CONFIG_FAT_DEFAULT_CODEPAGE=437
    CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"

When planning on [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") FAT [partitions](https://wiki.gentoo.org/wiki/Partition "Partition"), users may need to specify a `codepage=` option with mount. In the example above the codepage for the United States and Canada is used, however other codepages can be enabled a necessary. Optionally, users can also set a default codepage for FAT in the kernel configuration. Be sure each codepage value which is to be used has been enabled in the kernel.

** Note**\
Using the `codepage` option via the [mount] will override the settings used in the kernel.

Avoid setting `Default iocharset for fat` to [UTF-8](https://wiki.gentoo.org/wiki/UTF-8 "UTF-8"); it is not recommended. Instead, pass the `utf8=true` option when [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") FAT partitions (this requires `CONFIG_NLS_UTF8` to be enabled in the kernel). For further information see [[[mount(8)]](https://man.archlinux.org/man/mount.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page or see the appropriate kernel documentation at [/usr/src/linux/Documentation/filesystems/vfat.rst]

### [Emerge]

The [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]] package is needed for FAT userspace utilities:

`root `[`#`]`emerge --ask sys-fs/dosfstools`

## [Usage]

### [Formatting]

To create a FAT file system, use [mkfs.fat]:

`user `[`$`]`mkfs.fat --help`

For example, to format the [/dev/sdx9] partition with the FAT32 filesystem with label \"ESP\":

`root `[`#`]`mkfs.fat -v -F 32 -n "ESP" /dev/sdx9`

Resizing can be done using [[[sys-fs/fatresize]](https://packages.gentoo.org/packages/sys-fs/fatresize)[]].

Any FAT filesystem can be mounted with the [[mount](https://wiki.gentoo.org/wiki/Mount "Mount")] command. For FAT12/16/32, the type may be specified with the ` -t vfat` option or the `-t msdos` option if VFAT support is missing from the kernel.

### [Case sensitivity]

In the original FAT file system only short filenames (8.3 or SFN) are possible, and they are being stored in all upper case only. The systems using the original FAT file system were not case-sensitive (like MS-DOS). As extension to FAT, VFAT not only allows long filenames (LFN) but also lower case letters in filenames. VFAT is case-preserving, but for compatibility reasons existing operating systems (such as Microsoft Windows 95 and Windows NT) were still treating filenames case-insensitive. On the other hand, Unix traditionally was strictly case-sensitive.

In Linux `vfat` defaults to treating names case-insensitive (mount option `check=r` for *relaxed*). VFAT can, however, also be mounted with *strict* case-checking, mount option `check=s`, but this can cause problems.

#### [Manual mount options]

** Warning**\
Using anything other than the default options will cause problems! You have been warned! See section [Problem cases](https://wiki.gentoo.org/wiki/FAT#Problem_cases "FAT") for details.

For short names of directories and files (8.3, i.e. \"short filenames\" or SFN) the behavior of how the name is stored in the filesystem and how it is displayed can be changed using mount option `shortname`, which defaults to `mixed` since Linux kernel 2.6.32 (December 2009).^[\[2\]](#cite_note-2)^

  ------------- ------------------------- ----------------------------- -------------------- ------------------------------------------------------------- ---------------------
  file system   mount option              display short name            short name example   store long name                                               long name example

  FAT12\                                                                **`FILENAME.EXT`**                                                                 --
  FAT16\
  FAT32\
  VFAT

                `shortname=lower`         always forced to lower case   `filename.ext`       when the short name is not all upper case                     --

                `shortname=win95`         upper case                    `FILENAME.EXT`       when the short name is not all upper case                     --

                `shortname=winnt`         as is (original)              `FILENAME.EXT`       when the short name is not all lower case or all upper case   --

                `shortname=`**`mixed`**   as is (original)              `FILENAME.EXT`       when the short name is not all upper case                     --

  VFAT                                                                  `FILENA~1.EXT`                                                                     **`FileName.Ext`**

                `shortname=lower`         always forced to lower case   --                   when the short name is not all upper case                     `FileName.Ext`

                `shortname=win95`         upper case                    --                   when the short name is not all upper case                     `FileName.Ext`

                `shortname=winnt`         as is (original)              --                   when the short name is not all lower case or all upper case   `FileName.Ext`

                `shortname=`**`mixed`**   as is (original)              --                   when the short name is not all upper case                     `FileName.Ext`

  VFAT                                                                  `LONGNA~1.EXT`                                                                     **`long name.ext`**

                `shortname=lower`         always forced to lower case   --                   when the short name is not all upper case                     `long name.ext`

                `shortname=win95`         upper case                    --                   when the short name is not all upper case                     `long name.ext`

                `shortname=winnt`         as is (original)              --                   when the short name is not all lower case or all upper case   `long name.ext`

                `shortname=`**`mixed`**   as is (original)              --                   when the short name is not all upper case                     `long name.ext`
  ------------- ------------------------- ----------------------------- -------------------- ------------------------------------------------------------- ---------------------

A special case is an all lower case short filename, e.g. `filename.ext`. If it is created with `shortname=winnt`, no LFN VFAT entry will be created.

  ------------- ----------------------- ----------------------------------------------------------------- -------------------- ----------------------------- --------------------
  file system   mount option            store long name                                                   long name example    display short name            short name example
  VFAT                                                                                                    **`filename.ext`**   →                             `FILENAME.EXT`
                **`shortname=winnt`**   when the short name is not **all lower case** or all upper case   --                   as is (short name)            `FILENAME.EXT`
                `shortname=lower`       --                                                                --                   always forced to lower case   `filename.ext`
                `shortname=win95`       --                                                                --                   upper case                    `FILENAME.EXT`
                `shortname=mixed`       --                                                                --                   as is                         `FILENAME.EXT`
  ------------- ----------------------- ----------------------------------------------------------------- -------------------- ----------------------------- --------------------

If the file is created with `shortname=lower|win95|mixed` however, there will be a VFAT entry (LFN) and a short filename as well, e.g. `FILENA~2.EXT`. Whenever there is an LFN, VFAT will display the LFN, not the SFN. This is particularly tricky since the LFN entry might look like an 8.3 SFN, as in the example `filename.ext`.

  ------------- ------------------------- -------------------- -------------------- --------------------
  file system   mount option              long name example    display short name   short name example
  VFAT                                    **`filename.ext`**                        `FILENA~2.EXT`
                `shortname=lower`         `filename.ext`       lower case           --
                `shortname=win95`         `filename.ext`       upper case           --
                `shortname=winnt`         `filename.ext`       as is                --
                `shortname=`**`mixed`**   `filename.ext`       as is                \~
  ------------- ------------------------- -------------------- -------------------- --------------------

#### [Problem cases]

With the default settings existing file systems will *just work*.^[\[3\]](#cite_note-3)^ Firstly, VFAT currently defaults to relaxed case-checking (mount option `check=r`). This means that names for directories and files below the mount point will always work as long as they otherwise match in any possible combination of upper and lower case spelling, e.g. `filename.ext` will be found even when e.g. `FILENAME.EXT` or `FileName.Ext` is actually present, because the difference is only in case.

And secondly, short names (8.3, SFN) that are not all upper case will get an additional long filename entry to store the case correctly i.e. making VFAT case-preserving (mount option `shortname=mixed`).

** Important**\
On platforms with [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") this is especially important for compatibility with existing directories and files on the [EFI System Partition (ESP)](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"), which is vital for the boot configuration. Systems using FAT and VFAT traditionally haven\'t been case-sensitive, hence it is to be expected that existing directories and filenames differ slightly in their use of upper and lower case letters. With the default settings for `vfat`, Linux is adapting to this convention and treats the whole mount point case-insensitive as well, i.e. [/efi/EFI/boot/bootx64.efi] (assuming the ESP is mounted under [/efi]) and other EFI bootloader paths will always work as expected.

If only Linux is installed and all file references remain exactly the same, everything should also work with strict case-checking (mount option `check=s`). However, since the VFAT file system stores two filenames in some but not all cases, one short (8.3, SFN) and one long name (LFN), conventions regarding the management of those names can cause additional problems. The obvious example is the use of `shortname=winnt`, which will convert a short filename in all lower case to a standard FAT filename in all upper case, and skip creating an LFN counterpart. For example, the filename `bootx64.efi` would be stored as traditional 8.3 short filename (SFN) `BOOTX64.EFI` only. Additionally, `shortname=winnt` will display short filenames as is, so the originally written `bootx64.efi` doesn\'t exist, and together with strict case-checking this will cause big problems under Linux.

## [Troubleshooting]

### [Slow file transfer speeds]

If file transfer speeds are slow (can be viewed using [[iotop]](https://wiki.gentoo.org/wiki/Iotop "Iotop")), ensure the filesystem is mounted with the `async` filesystem option. Edit [/etc/fstab] (or [/etc/autofs/auto.misc] when using autofs) system files as needed, likely removing the `sync` mount option. By default, filesystems are mounted using the `async` mount option.

** Note**\
The filesystem `sync` mount option inhibits slower transfer speeds than the default `async` mount option. The `sync` mount option may cause flash media life-cycle shortening also! See [man mount] option `sync` explanation.

If file transfer speeds are still slow, try remounting the filesystem with the `flush` mount option:

`root `[`#`]`mount -o remount,flush /path/to/mountpoint`

### [Alternative operating system compatible filesystems]

Try UDF filesystem using UDFTools, requiring [[[sys-fs/udftools]](https://packages.gentoo.org/packages/sys-fs/udftools)[]] and Linux kernel UDF filesystem driver. Recently code was added to mkudffs for a fix for creating a mock partition increasing compatibility with Microsoft related operating systems. If using an older Linux kernel, ensure block size is set to 512 for increased compatibility. Most options are now default for compatibility, except for the required `--bootarea=mbr` creating the mock partition.

`root `[`#`]`mkudffs --bootarea=mbr --label=your_label /dev/device_file`

Try Samsung\'s F2FS filesystem.

### [][UTF-8/UTF-16 character hardware bugs]

Sometimes hardware firmware bugs will occur on embedded devices (eg. car radios) when reading their required formatted FAT/FAT32 filesystems containing UTF-8 characters. A workaround is to ensure initially mounting the FAT filesystem using (current default) mount options `codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro`.

For short filenames, `codepage=437` is IBM-PC characters or basically ASCII. For long filenames, `iocharset=iso8859-1` specifies ASCII. The option `shortname=mixed` is default, and can also try `shortname=win95` option. Of which, are all current defaults. Additionally to further remedy UTF-8/UTF-16 incompatible characters, use a loop with [sed] to replace all incompatible UTF-8/UTF-16 characters with an underscore or other ASCII character. (See this [replace_chars.sh](http://rogerx.sdf.org/files/bin/replace_chars.sh) script.)

For reference, this bug was encountered with a Sony car radio. The MEX-GS610BT radio model would hard reset upon attempting to read a USB flash media/drive containing UTF-8/UTF-16 characters.

As mentioned previously, see [/usr/src/linux/Documentation/filesystems/vfat.txt], the Linux Kernel vfat source code documentation, for further explanation on whether to use codepage, iocharset, or utf8 mount options.

### [Unsorted files and folders]

When writing files to the FAT/FAT32 filesystem, devices used for reading the filesystem may show the files and folders as unsorted. Commonly, viewer prefer seeing files and folders sorted alphabetically. Install [[[sys-fs/fatsort]](https://packages.gentoo.org/packages/sys-fs/fatsort)[]], and issue the following command:

`root `[`#`]`fatsort /dev/device_file`

## [See also]

-   [ExFAT](https://wiki.gentoo.org/wiki/ExFAT "ExFAT") --- a Microsoft file system optimized for flash memory storage
-   [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") --- an open source disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") and the most recent version of the extended series of filesystems.
-   [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") --- a copy-on-write (CoW) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") for Linux aimed at implementing advanced features while focusing on fault tolerance, self-healing properties, and easy administration.
-   [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") --- any media that is easily removed from a system.
-   [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") --- a configuration file that defines how and where the main [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") are to be mounted, especially at boot time.

## [External resources]

-   [[/usr/src/linux/Documentation/filesystems/vfat.txt]](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/filesystems/vfat.txt) - Documentation on the VFAT filesystem included with the Linux kernel sources.
-   [FAT filesystem and Linux](https://en.wikipedia.org/wiki/FAT_filesystem_and_Linux "wikipedia:FAT filesystem and Linux") - from Wikipedia

## [References]

1.  [[[↑](#cite_ref-1)] [[https://en.wikipedia.org/wiki/File_Allocation_Table](https://en.wikipedia.org/wiki/File_Allocation_Table)]]
2.  [[[↑](#cite_ref-2)] [FreeDesktop.org [Bug 24129: please mount vfat disks with shortname=mixed](https://bugs.freedesktop.org/show_bug.cgi?id=24129)]]
3.  [[[↑](#cite_ref-3)] [[https://www.kernel.org/doc/html/v6.0/filesystems/vfat.html](https://www.kernel.org/doc/html/v6.0/filesystems/vfat.html)]]