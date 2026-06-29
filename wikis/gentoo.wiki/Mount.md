This page contains [[changes](https://wiki.gentoo.org/index.php?title=Mount&oldid=1225862&diff=1306796)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Mount/es "Mount (27% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Mount/hu "Csatolás (mount) (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Mount/pl "Montowanie (25% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Mount/ja "マウント (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/mount_(Unix) "wikipedia:mount (Unix)")

[[]][Man page](http://man7.org/linux/man-pages/man8/mount.8.html)

**Mounting** typically involves the attaching of an additional [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") to the currently accessible filesystem of a computer.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [List mounts]](#List_mounts)
    -   [[2.2] [Mount filesystem]](#Mount_filesystem)
    -   [[2.3] [Unmount a filesystem]](#Unmount_a_filesystem)
    -   [[2.4] [Mount options]](#Mount_options)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Mounting as non-superuser]](#Mounting_as_non-superuser)
    -   [[3.2] [Mounting removable media]](#Mounting_removable_media)
    -   [[3.3] [Mounting Windows shares (CIFS)]](#Mounting_Windows_shares_.28CIFS.29)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

The [mount] command is part of the [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux") package. In Gentoo Linux, [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] is part of the system set and is installed on all Gentoo systems by default.

If for some strange and unordinary reason it is missing it can be re-installed by running a simple [emerge] command (always use the `--oneshot` option). This can also be used after changing [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"):

`root `[`#`]`emerge --ask --oneshot sys-apps/util-linux`

## [Usage]

`root `[`#`]`mount --help`

    Usage:
     mount [-lhV]
     mount -a [options]
     mount [options] [--source] <source> | [--target] <directory>
     mount [options] <source> <directory>
     mount <operation> <mountpoint> [<target>]

    Mount a filesystem.

    Options:
     -a, --all               mount all filesystems mentioned in fstab
     -c, --no-canonicalize   don't canonicalize paths
     -f, --fake              dry run; skip the mount(2) syscall
     -F, --fork              fork off for each device (use with -a)
     -T, --fstab       alternative file to /etc/fstab
     -i, --internal-only     don't call the mount.<type> helpers
     -l, --show-labels       show also filesystem labels
     -m, --mkdir[=<mode>]    alias to '-o X-mount.mkdir[=<mode>]'
     -n, --no-mtab           don't write to /etc/mtab
         --options-mode <mode>
                             what to do with options loaded from fstab
         --options-source <source>
                             mount options source
         --options-source-force
                             force use of options from fstab/mtab
     -o, --options <list>    comma-separated list of mount options
     -O, --test-opts <list>  limit the set of filesystems (use with -a)
     -r, --read-only         mount the filesystem read-only (same as -o ro)
     -t, --types <list>      limit the set of filesystem types
         --source <src>      explicitly specifies source (path, label, uuid)
         --target <target>   explicitly specifies mountpoint
         --target-prefix
                             specifies path used for all mountpoints
     -v, --verbose           say what is being done
     -w, --rw, --read-write  mount the filesystem read-write (default)
     -N, --namespace <ns>    perform mount in another namespace

     -h, --help              display this help
     -V, --version           display version

    Source:
     -L, --label <label>     synonym for LABEL=<label>
     -U, --uuid <uuid>       synonym for UUID=<uuid>
     LABEL=<label>           specifies device by filesystem label
     UUID=<uuid>             specifies device by filesystem UUID
     PARTLABEL=<label>       specifies device by partition label
     PARTUUID=<uuid>         specifies device by partition UUID
     ID=<id>                 specifies device by udev hardware ID
     <device>                specifies device by path
     <directory>             mountpoint for bind mounts (see --bind/rbind)
     <file>                  regular file for loopdev setup

    Operations:
     -B, --bind              mount a subtree somewhere else (same as -o bind)
     -M, --move              move a subtree to some other place
     -R, --rbind             mount a subtree and all submounts somewhere else
     --make-shared           mark a subtree as shared
     --make-slave            mark a subtree as slave
     --make-private          mark a subtree as private
     --make-unbindable       mark a subtree as unbindable
     --make-rshared          recursively mark a whole subtree as shared
     --make-rslave           recursively mark a whole subtree as slave
     --make-rprivate         recursively mark a whole subtree as private
     --make-runbindable      recursively mark a whole subtree as unbindable

    For more details see mount(8).

### [List mounts]

Show mounted filesystems by running the mount command with no arguments or options:

`root `[`#`]`mount`

** Tip**\
There is also a more visual way of showing mounted filesystems using the [findmnt] tool also provided by [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]. For more details see [man 8 findmnt].

### [Mount filesystem]

To mount a filesystem, a [device file](https://wiki.gentoo.org/wiki/Device_file "Device file"), [UUID or label](https://wiki.gentoo.org/wiki//etc/fstab#UUIDs_and_labels "/etc/fstab") or other means of locating the partition or data source and a mount point are required. Non-system relevant filesystems are normally mounted in the [/mnt] directory. The proper syntax for mounting a file system is as follows:

`root `[`#`]`mount <DEVICE> <DIRECTORY>`

For further details, see [man 8 mount].

The [/media] directory is generally used to mount removable devices such as USB drives or SD cards. After determining which device the USB drive shows up as, a command like the following could be used to mount its contents to a newly created [usb] folder in [/media]:

`root `[`#`]`mkdir /media/usb `

`root `[`#`]`mount /dev/sdb1 /media/usb `

** Tip**\
A mount from [fstab](https://wiki.gentoo.org/wiki/Fstab "Fstab") may by mounted by providing just the mountpoint, or device name, for example:

`root `[`#`]`mount /dev/sdb1`

If you trying to mount ISO and getting error about UDF filesystem - check that in kernel enabled **CONFIG_UDF_FS**.

### [Unmount a filesystem]

To unmount a filesystem, the device file or the mount point can be specified:

`root `[`#`]`umount <DEVICE>`

`root `[`#`]`umount <DIRECTORY>`

Invocation information:

`user `[`$`]`umount --help`

    Usage:
     umount [-hV]
     umount -a [options]
     umount [options] <source> | <directory>

    Unmount filesystems.

    Options:
     -a, --all               unmount all filesystems
     -A, --all-targets       unmount all mountpoints for the given device in the
                               current namespace
     -c, --no-canonicalize   don't canonicalize paths
     -d, --detach-loop       if mounted loop device, also free this loop device
         --fake              dry run; skip the umount(2) syscall
     -f, --force             force unmount (in case of an unreachable NFS system)
     -i, --internal-only     don't call the umount.<type> helpers
     -n, --no-mtab           don't write to /etc/mtab
     -l, --lazy              detach the filesystem now, clean up things later
     -O, --test-opts <list>  limit the set of filesystems (use with -a)
     -R, --recursive         recursively unmount a target with all its children
     -r, --read-only         in case unmounting fails, try to remount read-only
     -t, --types <list>      limit the set of filesystem types
     -v, --verbose           say what is being done
     -q, --quiet             suppress 'not mounted' error messages
     -N, --namespace <ns>    perform umount in another namespace

     -h, --help              display this help
     -V, --version           display version

    For more details see umount(8).

### [Mount options]

Sometimes, mounting a filesystem requires special options:

`root `[`#`]`mount [OPTIONS] <DEVICE> <DIRECTORY>`

  -------------------------- --------------------------------------------------------------------------------------------------------------------------
  Option                     Description
  `-f`                       Simulate the mount
  `-t`                       Specify the filesystem, e.g [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4")
  `-o OPTION1,OPTION2,...`   Specify the mount options (see below)
  `-a`                       Mount all filesystems in [/etc/fstab]
  -------------------------- --------------------------------------------------------------------------------------------------------------------------

  : Program options:

The filesystem being used must support the mount option being passed. Many options are common, but some *are* filesystem specific.

** Note**\
It is advised to always consult [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page") of both [mount] and the particular filesystem (for example [[[ext4(5)]](https://man.archlinux.org/man/ext4.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] or [[[xfs(5)]](https://man.archlinux.org/man/xfs.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]).

  ------------ --------------------------------------------------------------------------------------------------------------------------------------------------------
  Option       Description
  `defaults`   Use the default mount options: `rw`, `suid`, `dev`, `exec`, `auto`, `nouser`, `async`.
  `auto`       Mount the filesystem automatically on boot.
  `noauto`     Do not mount the filesystem automatically on boot.
  `ro`         Mount the filesystem read-only.
  `rw`         Mount the filesystem read-write.
  `sw`         Mount a [swap](https://wiki.gentoo.org/wiki/Swap "Swap") partition.
  `atime`      Update inode access times on every read.
  `relatime`   Update inode access times only on writes to improve I/O performance.
  `noatime`    Never update inode access times for best I/O performance.
  `sync`       Sync drive after each write. Can shorten lifespan for e.g. some flash drives.
  `async`      Sync drive asynchronously.
  `discard`    The equivalent of [trim support](https://wiki.gentoo.org/wiki/SSD#Dealing_with_empty_blocks "SSD") on Linux.
  `exec`       Allow execution of binaries.
  `noexec`     Do not allow execution of binaries.
  `suid`       Follow SUID and SGID bits.
  `nosuid`     Do not follow SUID and SGID bits.
  `user`       Allow a user to mount the filesystem. Implies `nodev`, `noexec`, and `nosuid` options unless explicitly setting `dev`, `exec`, or `suid` respectively.
  `users`      Allow every user to mount the filesystem.
  `nouser`     Allow only \"root\" to mount the filesystem.
  ------------ --------------------------------------------------------------------------------------------------------------------------------------------------------

  : Mount options:

Mount options of already-mounted filesystems can be changed using `remount` option. For example, setting a filesystem on [/dev/foo] to be mounted as read-write can be achieved using:

`root `[`#`]`mount -o remount,rw /dev/foo /dir`

## [Tips]

### [Mounting as non-superuser]

According to [man mount], only the superuser can mount filesystems. However, when [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") contains the `user` option on a line, any user will be capable of mounting the corresponding partition, device, drive, etc.

### [Mounting removable media]

See the relevant section in the [Removable media](https://wiki.gentoo.org/wiki/Removable_media#Mounting_removable_media "Removable media") article.

### [][Mounting Windows shares (CIFS)]

Despite [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") entries, non-superuser mounts of Windows shares will fail (for security reasons). In the following example is found a [fstab] entry for Windows share; pay close attention to the `cifs` option:

[FILE] **`/etc/fstab`**

    [...]
    //server/folder /home/larry/winmount cifs noauto,user 0 0
    [...]

`user `[`$`]`mount /home/larry/winmount`

    This program is not installed setuid root -  "user" CIFS mounts not supported.

The solution is to use [sudo mount /home/larry/winmount] in combination with a corresponding entry in [/etc/sudoers] to allow passwordless mounting.

** Warning**\
Be sure to understand the [sudo configuration](https://wiki.gentoo.org/wiki/Sudo#Configuration "Sudo") before editing the [/etc/sudoers] file!

[FILE] **`/etc/sudoers`**

    [...]
    larry    ALL = NOPASSWD: /bin/mount  /home/larry/winmount/, /bin/mount  /home/larry/winmount
    larry    ALL = NOPASSWD: /bin/umount /home/larry/winmount/, /bin/umount /home/larry/winmount
    [...]

## [See also]

-   [Mounting partitions in the Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook/Mounting_partitions "Security Handbook/Mounting partitions")
-   [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") --- a configuration file that defines how and where the main [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") are to be mounted, especially at boot time.
-   [Removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") --- any media that is easily removed from a system.
-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") --- a program that uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") automounter to automatically [mount] [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on demand.
-   [Udevil](https://wiki.gentoo.org/wiki/Udevil "Udevil") --- a small auto-mount utility created to be a \"a hassle-free replacement for [udisks](https://wiki.gentoo.org/wiki/Udisks "Udisks").\"
-   [CurlFtpFS](https://wiki.gentoo.org/wiki/CurlFtpFS "CurlFtpFS") --- allows for [mounting] an FTP folder as a regular directory to the local directory tree.
-   [USB/Guide](https://wiki.gentoo.org/wiki/USB/Guide#Mounting_a_USB_mass_storage_device "USB/Guide") - Mounting a USB Mass Storage device
-   [UUIDs and labels](https://wiki.gentoo.org/wiki/Removable_media#UUIDs_and_labels "Removable media")

## [References]

1.  [[[↑](#cite_ref-1)] [[http://www.linfo.org/mounting.html](http://www.linfo.org/mounting.html)]]