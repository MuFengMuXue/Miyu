[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Fstab&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Fstab "Fstab (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Fstab/tr "Fstab (3% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Fstab/fr "Fstab/fr (89% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Fstab/ru "Fstab (100% translated)")

## Contents

-   [[1] [fstab usage]](#fstab_usage)
-   [[2] [Example File]](#Example_File)
-   [[3] [Field definitions]](#Field_definitions)
    -   [[3.1] [Filesystem Specification]](#Filesystem_Specification)
    -   [[3.2] [Mount Point]](#Mount_Point)
    -   [[3.3] [Filesystem Type]](#Filesystem_Type)
    -   [[3.4] [Mount options]](#Mount_options)
        -   [[3.4.1] [FAT Mount options]](#FAT_Mount_options)
        -   [[3.4.2] [EXT2/3/4 Mount options]](#EXT2.2F3.2F4_Mount_options)
        -   [[3.4.3] [NTFS-3G Mount options]](#NTFS-3G_Mount_options)
    -   [[3.5] [Dump?]](#Dump.3F)
    -   [[3.6] [Pass number]](#Pass_number)
-   [[4] [Tips and tricks]](#Tips_and_tricks)
-   [[5] [See Also]](#See_Also)

# [fstab usage]

The `/etc/fstab` root-owned configuration file is used to define how disk partitions, various other block devices, or remote filesystems should be mounted into the filesystem.

Each filesystem is described in a separate line. These definitions will be converted into systemd mount units dynamically at boot, or when the configuration of the system manager is reloaded.

The `mount --all` command will mount all filesystems mentioned in `fstab`, (except for those whose line contains the `noauto` keyword). The filesystems are mounted following their order in `fstab`. The mount command compares filesystem source and target to detect already mounted filesystems. The kernel table with already mounted filesystems is cached during `mount --all`. This means that all duplicated fstab entries will be mounted.

# [Example File]

Each line in the file describes a filesystem, and contain fields (specified in columns) used to provide information about its mountpoint, the options which should be used when mounting it etc. Each field can be separated from one another either by spaces or tabs:

    # /etc/fstab: static file system information.
    # <file system>                           <mount point>  <type>  <options>                     <dump>
    LABEL=ESP                                 /boot/efi      vfat    umask=0077                         0       2
    /dev/sda5                                 /              ext4    defaults,noatime,discard           0       1
    UUID=18360b04-a96d-4a99-8323-b07717f36a31 none           swap       defaults,discard=pages             0       0
    UUID=b4108631-e051-48d8-b2ff-a1d924a893f1 /home          ext4    defaults,noatime,discard           0       2
    UUID=634E43D367B0A4B1                     /run/media/data    ntfs-3g noauto,x-systemd.automount,x-systemd.device-timeout=10,rw,inherit,permissions,streams_interface=windows,windows_names,compression,norecover,hide_dot_files,hide_hid_files,big_writes 0 2

Each column in the above are the fstab \"fields\" and will be explained in the next section.

# [Field definitions]

## [Filesystem Specification]

This field describes one of each of the following:

-   the block special device
-   remote filesystem
-   filesystem image for loop device to be mounted
-   swap file or swap partition to be enabled

This field generally takes the form of:

-   /dev/XdY
-   LABEL=\< label\>
-   UUID=\<uuid\>

to uniquely identify a filesystem you want to mount. As a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) is necessarily unique, you will find that this is the default in use on more modern systems whereas a device name and label are only in use on older systems, so we\'ll concentrate on UUIDs in this tutorial, but know that if you insist on using these order systems, they still work at the time of this writing.

To get the UUID for all of your devices, execute the command `blkid` elevated to root:

[user \$ ][ sudo blkid [COPY TO CLIPBOARD]]

\

and you\'ll get someting like this:

    /dev/sda1: LABEL_FATBOOT="ESP" LABEL="ESP" UUID="2462-755F" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="EFI system partition" PARTUUID="b86c0cae-3055-4d9e-9e12-1fa1e2cd32d2"
    /dev/sda2: PARTLABEL="Microsoft reserved partition" PARTUUID="b0679b89-007c-441b-88a3-74a39f1f8b2b"
    /dev/sda3: LABEL="WINSYS" BLOCK_SIZE="512" UUID="029873F49873E497" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="f8d444b9-ec60-4ac8-b12a-52448119fad1"
    /dev/sda4: BLOCK_SIZE="512" UUID="0EB23063B2305207" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="cb083fb5-d61c-48e3-a657-ceb363a983b1"
    /dev/sda5: UUID="9b539186-41e9-46f0-a515-1ec6c3544367" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="7bd52fb7-4d7d-412c-bc01-e3c98c7f3bb1"
    /dev/sda6: UUID="b4108631-e051-48d8-b2ff-a1d924a893f0" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="9683d669-e0fd-496a-bd9c-f0e51d0bd561"
    /dev/sda7: UUID="18360b04-a96d-4a99-8323-b07717f36a30" TYPE="swap" PARTUUID="7434de88-dd5c-4ce5-a6e2-4bb65c16eab5"
    /dev/sdb2: UUID="26055107-28cd-457e-9a31-46781de4065d" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="86bdde2c-b92c-43fc-811a-6d0cdc312be1"
    /dev/sdb3: UUID="c9dd0f4c-5793-446e-90bb-d10e27bf4922" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="d02838bd-371c-4673-96ed-8aad73bb6d91"
    /dev/sdc1: LABEL="Win-Data" BLOCK_SIZE="512" UUID="634E43D367B0A4B1" TYPE="ntfs" PARTUUID="ca8d0663-6a6e-4b09-a0d7-05b59d109ab1"

Any one of the output of `blkid` can be used as the first field in the fstab file.

E.G. **all** of the following lines are valid entries *for the first line* of the output of the above example:

    # <file system>                           <mount point>  <type>  <options>                     <dump>
    LABEL=ESP                                 /boot/efi      vfat    umask=0077                         0       2
    UUID=2462-755F                            /boot/efi      vfat    umask=0077                         0       2
    LABEL=EFI\040system\040partition          /boot/efi      vfat    umask=0077                         0       2
    UUID=b86c0cae-3055-4d9e-9e12-1fa1e2cd32d2 /boot/efi      vfat    umask=0077                         0       2

I.E. only one of the above lines should be present in your fstab file to mount the ESP partition, but any of them will work! *However* it is strongly recommended to use the UUID as that is **globally unique!**. This means that if your move a disk to another machine, it will keep its UUID and there is no opportunity for surprises like the computer you\'ve moved the existing disk to suddenly:

-   booting from the **E**FI **S**ystem **P**artition on the new disk instead of its own ESP
-   failing to mount its own Windows partition because you just added another one and this takes precedence (or not: depending on the exact kernel version and filesystem driver resulting in a boot only working 50% of the time and other weird problems)
-   failing to mount a disk because the disk you just inserted into M2 slot #1 gets named /dev/sda and the one in slot #2 which used to be called /dev/sda now suddenly becomes /dev/sdb.
-   etc, etc.

## [Mount Point]

This field describes the mount point (target) inside your filesystem. For swap partitions, this field should be specified as \`none\'. If the name of the mount point contains spaces or tabs these can be escaped as \`\\040\' and \'\\011\' respectively.

For more information on the Linux Filesystem Hierarchy standard refer to the [#See Also](#See_Also) section, but in a nutshell you should specify an existing directory on your filesystem where you want to mount a partition.

In the example `fstab` file above, the following line in it\'s `blkid` output:

    /dev/sdc1: LABEL="Win-Data" BLOCK_SIZE="512" UUID="634E43D367B0A4B1" TYPE="ntfs" PARTUUID="ca8d0663-6a6e-4b09-a0d7-05b59d109ab1"

-   is the Windows D: Drive
-   has an NTFS label of \"Win-Data\"
-   has a Windows UUID of \"634E43D367B0A4B1\" (different from Linux UUIDs)
-   contains the NTFS File System
-   has a partition UUID of \"ca8d0663-6a6e-4b09-a0d7-05b59d109ab1\"

and gets mounted on the `/media/Data` according to this line:

    UUID=634E43D367B0A4B1                     /media/Data    ntfs-3g noauto,x-systemd.automount,x-systemd.device-timeout=10,rw,inherit,permissions,streams_interface=windows,windows_names,compression,norecover,hide_dot_files,hide_hid_files,big_writes 0 2

## [Filesystem Type]

This field describes the type of the filesystem. Linux supports many filesystem types: ext4, xfs, btrfs, f2fs, vfat, ntfs-3g (for Windows compatibility), hfsplus (for Mac Compatibility), tmpfs, sysfs, proc, iso9660 (to allow you to mount CD/DVD ISO files as Read-Only directories), udf, squashfs, nfs, cifs, and many more.

An entry swap denotes a file or partition to be used for swapping. An entry none is useful for bind or move mounts.

More than one type may be specified in a comma-separated list.

Using the same example `fstab` file and \"Win-Data\" line as above, `ntfs-3g` is the file system we\'re mounting this one under although the `blkid` shows `ntfs`. This is simply because the `ntfs` driver is a read-only driver (allowing you to see your Windows files, but not modify them, whereas the `ntfs-3g` (for 3rd generation) allows most NTFS options (except encryption) thus also read-write capabilities:

    UUID=634E43D367B0A4B1                     /media/Data    ntfs-3g noauto,x-systemd.automount,x-systemd.device-timeout=10,rw,inherit,permissions,streams_interface=windows,windows_names,compression,norecover,hide_dot_files,hide_hid_files,big_writes 0 2

## [Mount options]

This field describes the mount options associated with the filesystem.

It is formatted as a comma-separated list of options. It contains at least the type of mount (ro or rw), plus any additional options appropriate to the filesystem type (including performance-tuning options).

Basic filesystem-independent options are:

-   defaults: use default options: rw, suid, dev, exec, auto, nouser, and async.
-   noauto: do not mount when mount -a is given (I.E. at boot time)
-   user: allow any user to mount (I.E. no `sudo` needed)
-   owner: Only allow device owner to mount
-   comment: or x-\<name\> for use by fstab-maintaining programs
-   nofail: do not report errors for this device if it does not exist.

### [FAT Mount options]

TBD

### [][EXT2/3/4 Mount options]

TBD

### [NTFS-3G Mount options]

TBD

## [][Dump?]

This field must be 1 or 0 and is used by `dump` to determine which filesystems need to be dumped in case of a coredump (=crash). Defaults to zero (don't dump) if not present.

## [Pass number]

This field is used by fsck(8) to determine the order in which filesystem checks are done at boot time. The root filesystem *should be* specified with a fs_passno of 1. Other filesystems should have a fs_passno of 2. Filesystems within a drive will be checked sequentially, but filesystems on different drives will be checked at the same time to utilize parallelism available in the hardware.

Defaults to zero (don't check the filesystem) if not present.

# [Tips and tricks]

The default setup will automatically \`fsck\` and \`mount\` filesystems before starting services that need them to be mounted. For example, systemd automatically makes sure that remote filesystem mounts like NFS or Samba are only started after the network has been set up. Therefore, local and remote filesystem mounts specified in \`/etc/fstab\` should work out of the box. See

[user \$ ][ man 5 systemd.mount [COPY TO CLIPBOARD]]

\
for details.

# [See Also]

[https://refspecs.linuxfoundation.org/FHS_3.0/index.html](https://refspecs.linuxfoundation.org/FHS_3.0/index.html)