**Resources**

[[]][GitHub](https://github.com/Aorimn/dislocker)

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/dislocker)

**Dislocker** is [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE")-based [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") driver capable of reading [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS") BitLocker encrypted partitions.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Example]](#Example)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/dislocker`

## [Configuration]

### [Files]

**A note on fstab**

BitLocker partitions can be mount-ed using the [/etc/fstab] file and dislocker\'s long options. The line below is an example line, which has to be adapted to each case:

[FILE] **`/etc/fstab`**

    /dev/sda2 /mnt/dislocker fuse.dislocker user-password=blah,nofail 0 0

## [Example]

With the sample [/etc/fstab] as above, make sure the two mount points [/mnt/dislocker] and [/mnt/clear] exist. Then:

`root `[`#`]`mount /dev/sda2 `

`root `[`#`]`mount -o loop /mnt/dislocker/dislocker-file /mnt/clear `

The first mount creates the file [/mnt/dislocker/dislocker-file], which is the raw unencrypted NTFS from inside the BitLocker partition. The second command mounts that NTFS partition onto [/mnt/clear].

## [See also]

-   [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS") --- a proprietary disk [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") by Microsoft for Windows (NT-based) and WindowsNT-based operating systems.
-   [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") --- [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") originally created for use with MS-DOS (and later pre-NT Microsoft Windows).