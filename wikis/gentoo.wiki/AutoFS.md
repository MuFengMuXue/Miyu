This page contains [[changes](https://wiki.gentoo.org/index.php?title=AutoFS&oldid=1235063&diff=1438754)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/AutoFS/de "AutoFS/de (90% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/AutoFS/hu "AutoFS/hu (100% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/AutoFS/ta "AutoFS/ta (43% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/AutoFS/ja "AutoFS/ja (100% translated)")

**AutoFS** is a program that uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") automounter to automatically [mount](https://wiki.gentoo.org/wiki/Mount "Mount") [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on demand. It works with USB flash drives and external hard drives, network shares, [CDROM](https://wiki.gentoo.org/wiki/CDROM "CDROM")/DVD/[Blu-ray](https://wiki.gentoo.org/wiki/Blu-ray "Blu-ray"), and so on.

AutoFS works by monitoring directories on the local filesystem. Whenever a program tries to access one of those directories, AutoFS will mount something on that directory. The directories to monitor, as well as what to mount on them, are specified in the AutoFS configuration files such as [/etc/autofs/autofs.master]. Examples of how to configure AutoFS mounts are given down the page, under [Usage](https://wiki.gentoo.org/wiki/AutoFS#Usage "AutoFS").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel configuration]](#Kernel_configuration)
    -   [[1.2] [Userspace program]](#Userspace_program)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [/etc/conf.d/autofs]](#.2Fetc.2Fconf.d.2Fautofs)
        -   [[2.2.2] [/etc/autofs/autofs.conf]](#.2Fetc.2Fautofs.2Fautofs.conf)
        -   [[2.2.3] [/etc/autofs/auto.master]](#.2Fetc.2Fautofs.2Fauto.master)
        -   [[2.2.4] [/etc/autofs/auto.misc]](#.2Fetc.2Fautofs.2Fauto.misc)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Direct AutoFS mounts]](#Direct_AutoFS_mounts)
    -   [[3.2] [Indirect AutoFS mounts]](#Indirect_AutoFS_mounts)
    -   [[3.3] [Useful options]](#Useful_options)
    -   [[3.4] [Non-file maps]](#Non-file_maps)
    -   [[3.5] [Simple Windows-like Samba share mounting]](#Simple_Windows-like_Samba_share_mounting)
-   [[4] [Syslog]](#Syslog)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [External resources]](#External_resources)

## [[] Installation]

AutoFS requires a kernel module and a userspace program.

** Note**\
To mount a filesystem (whether with AutoFS, or manually), the corresponding mount helper needs to be installed at the time of mounting. For example, [[[sys-fs/ntfs3g]](https://packages.gentoo.org/packages/sys-fs/ntfs3g)[]] or something equivalent is required to mount an [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS") filesystem. Some filesystems may also require changes to the kernel configuration. Check the wiki page for the specific filesystem to see what software and configuration will be required.

### [[] Kernel configuration]

The following kernel option activates the kernel functionality required for automounting.

[KERNEL]

    File systems --->
        <*/M> Kernel automounter version 4 support (also supports v3)

** Note**\
If the option is set to [M], the partition that contains the module file must already be mounted before AutoFS can work.

### [[] Userspace program]

As with most Linux filesystems, in addition to the relevant option being enabled in the kernel, the userspace package must be installed to actually handle the mounting.

### [USE flags for] [net-fs/autofs](https://packages.gentoo.org/packages/net-fs/autofs) [[]] [Kernel based automounter]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+libtirpc`](https://packages.gentoo.org/useflags/+libtirpc)           Use TiRPC library instead of SunRPC
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                     Install LDAP module
  [`mount-locking`](https://packages.gentoo.org/useflags/mount-locking)   Enable locking to prevent corruption of /etc/mtab in the presence of concurrent auto-mounting. If enabled, recursive auto-mounting (eg. using autofs to bind or loop mount a filesystem which is itself auto-mounted) is not possible.
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                     Enable SASL support in the LDAP module
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Install it with the following command:

`root `[`#`]`emerge --ask net-fs/autofs`

### [[] Additional software]

To be able to mount [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") file systems, the [[[net-fs/nfs-utils]](https://packages.gentoo.org/packages/net-fs/nfs-utils)[]] package is required:

`root `[`#`]`emerge --ask net-fs/nfs-utils`

For [CIFS](https://wiki.gentoo.org/wiki/CIFS "CIFS") file systems the [[[net-fs/cifs-utils]](https://packages.gentoo.org/packages/net-fs/cifs-utils)[]] package is additionally required:

`root `[`#`]`emerge --ask net-fs/cifs-utils`

For WebDAV file systems the [[[net-fs/davfs2]](https://packages.gentoo.org/packages/net-fs/davfs2)[]] package is required:

`root `[`#`]`emerge --ask net-fs/davfs2`

## [[] Configuration]

### [[] Service]

The AutoFS daemon needs to be running for automounting to work.

#### [[] OpenRC]

Add AutoFS to the default runlevel:

`root `[`#`]`rc-update add autofs default`

To begin using the automounter before rebooting, start it manually:

`root `[`#`]`/etc/init.d/autofs start`

Of course it is advisable to edit the configuration files first, as described below. If AutoFS is already running when the configuration is edited, run the following command to reload the configuration:

`root `[`#`]`/etc/init.d/autofs reload`

### [[] Files]

The default installation of AutoFS provides the following four configuration files:

  -------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                           Description
  [/etc/conf.d/autofs]        This file can be used to pass command-line options to the `automount` program. Most users will not need to edit this file.
  [/etc/autofs/autofs.conf]   This file defines some default parameters for AutoFS, such as the location of the master map file and the default timeout that causes an inactive mount to be disconnected. Most users will not need to edit this file.
  [/etc/autofs/auto.master]   This is the **\"master map\"**, effectively an index to the \"map files\" and other resources that tell AutoFS what to mount and where. Most users *will* need to edit this file.
  [/etc/autofs/auto.misc]     This is an example of a **\"map file\"** which is referenced by the master map. It specifies what to mount and where to mount it. Most users *will* need to edit this file.
  -------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [][/etc/conf.d/autofs]

[/etc/conf.d/autofs] is the configuration file that corresponds to the initscript [/etc/init.d/autofs]. For basic AutoFS usage, there is no need to modify this file.

The file defines two variables:

-   `USE_MISC_DEVICE`: If this is set to `"yes"`, the initscript will create the device file [/dev/autofs].
-   `OPTIONS`: This contains command-line arguments to be passed to `automount`. Run `man 8 automount` to view the manual page which lists all the allowed options.

** Note**\
`automount` may be given one non-option argument, the filename of the master map, but for most users the default value (`auto.master`) is fine. If you do want to change the master map filename, setting the `master_map_name` configuration variable in [/etc/autofs/autofs.conf] is probably a better way to do it. The rest of this page assumes the master map filename has been left at the default value.

#### [][/etc/autofs/autofs.conf]

[/etc/autofs/autofs.conf] is AutoFS\'s own configuration file. The default installation is well commented, and the options that can be specified in this file are also documented in the manual page, which can be viewed by running

`user `[`$`]`man 5 autofs.conf`

There is typically no need to modify this file.

#### [][/etc/autofs/auto.master]

[/etc/autofs/auto.master] is the (default) *\"master map\"*. Each line describes an AutoFS mount.

** Tip**\
Basic usage is described in [man auto.master]

** Warning**\
AutoFS does not use the terms \"mount\" and \"mount point\" in quite the same way as `/bin/mount` or [[/etc/fstab]](https://wiki.gentoo.org/wiki/Fstab "Fstab").

The typical configuration line for this file takes following format:

[CODE]

    mount-point [map-type[,format]:]map [options]

** Important**\
Indirect maps will be created, similarly to [mkdir -p] and is removed when the filesystem is unmounts.

`mount-point` specifies a directory for AutoFS to watch, and `map` that tells AutoFS what to mount there. For details, see [Usage](https://wiki.gentoo.org/wiki/AutoFS#Usage "AutoFS").

After handling the first two (whitespace-separated) fields as `mount-point` and `map` respectively, anything else on the line is treated as an option to be passed to either AutoFS\'s [automount] (if it starts with a dash), or [mount] (if it does not). Options passed to [mount] will follow the `-o` switch. See [Usage](https://wiki.gentoo.org/wiki/AutoFS#Usage "AutoFS") for an example.

** Important**\
The comments in `auto.master` say the format is `key [ -mount-options-separated-by-comma ] location`. As of version 5.1.2, that is wrong. That format applies to entries in map files, such as [/etc/autofs/auto.misc].

#### [][/etc/autofs/auto.misc]

[/etc/autofs/auto.misc] is an example of a *\"map file\"*. Only those map files actually referenced in the master map file are actually used by AutoFS, so it is safe to rename or delete this file as long as you edit [/etc/autofs/auto.master] to match. You can also create additional map files following the same syntax. By convention, map files are named with the pattern [/etc/autofs/auto.\*].

Lines in this file take the following format:

[FILE] **`/etc/autofs/auto.misc`**

    key             [-options]                                   location

Here `key` specifies a unique key associated with the AutoFS mount, which forms part or all of the path at which the filesystem will be mounted. `location` tells AutoFS what filesystem to mount there. `-options` is a comma-separated list of options to pass to [mount], except for some special options which are handled by AutoFS (such as `fstype`). For details, see [Usage](https://wiki.gentoo.org/wiki/AutoFS#Usage "AutoFS") below, or view the manual page by running

`user `[`$`]`man 5 autofs`

## [[] Usage]

** Important**\
Autofs mounts will not be mounted until access is attempted. This means it cannot be used to simply automatically mount devices added to the system.

AutoFS mounts are specified in [/etc/autofs/auto.master]

Example configuration:

[FILE] **`/etc/autofs/auto.master`Mount blockdevices, defined in [/etc/autofs/auto.blockdev], at [/media/blockdev], with a timeout of 5 minutes**

    /media/blockdev    /etc/autofs/auto.blockdev   --timeout=5

[FILE] **`/etc/autofs/auto.blockdev`Automatically mount block devices under [/dev] at [/media/blockdev] indirectly**

    *   -fstype=auto            :dev/&

The location of the map takes the format `host:path`. In this case, it is `auto.blockdev`, which references [/etc/autofs/auto.blockdev]. The `host` component may be left empty to refer to a path on the local machine. Otherwise, the named path from the named remote host will be mounted using [NFS](https://wiki.gentoo.org/wiki/Nfs-utils "Nfs-utils").

With this configuration, [/media/blockdev] will be created when the [autofs] service is started. If a device exists at [/dev/sda1] and access to [/media/blockdev/sda1] is attempted, the device at that location should automatically mount there.

There are two kinds of AutoFS mounts, direct and indirect.

### [[] Direct AutoFS mounts]

For a direct AutoFS mount, the `mount-point` is `/-`, and `key` in the map file is the full path at which the filesystem will be mounted. For example, the manual pages for AutoFS include an example like this:

[FILE] **`/etc/autofs/auto.master`**

    /-              /etc/autofs/auto.data

[FILE] **`/etc/autofs/auto.data`**

    /tst/sbin       bogus:/usr/sbin

These lines tell AutoFS to watch the directory [/tst/sbin]. If a program tries to access anything in that directory, AutoFS will mount the directory `/usr/sbin` from the remote host `bogus` on the local directory `/tst/sbin`. In other words, it will effectively execute the command

`root `[`#`]`mount -t nfs bogus:/usr/sbin /tst/sbin`

An example of mounting a local device might look like this:

[FILE] **`/etc/autofs/auto.master`**

    /-              /etc/autofs/auto.local

[FILE] **`/etc/autofs/auto.local`**

    /mnt/stuff      -fstype=ext4    :/dev/sdd1

This will effectively execute the command

`root `[`#`]`mount -t ext4 /dev/sdd1 /mnt/stuff`

### [[] Indirect AutoFS mounts]

For an indirect AutoFS mount, the `mount-point` is a directory path, and `map` is the full path to a file which describes rules for mounting devices inside that directory. For example, the default installation includes the following line (though it is commented out):

[FILE] **`/etc/autofs/auto.master`**

    /misc           /etc/autofs/auto.misc

This line would tell AutoFS to watch files and directories under [/misc] for filesystem accesses. When a program tries to access something under [/misc], AutoFS will use the configuration in [/etc/autofs/auto.misc] to determine whether to automatically mount something. Each (non-comment, non-empty) line in that file corresponds to something that AutoFS will be able to mount under [/misc]. For example, the line

[FILE] **`/etc/autofs/auto.misc`**

    cd              -fstype=iso9660,ro,nosuid,nodev     :/dev/cdrom

tells AutoFS to watch [/misc/cd]. When a program tries to access this directory, AutoFS will effectively run the command

`root `[`#`]`mount -t iso9660 -o ro,nosuid,nodev /dev/cdrom /misc/cd`

Here are some other examples:

[FILE] **`/etc/autofs/auto.master`**

    /mnt/auto           /etc/autofs/auto.misc

[FILE] **`/etc/autofs/auto.misc`**

    # The file above will use the mount-point /mnt/auto | mount options | device, network share etc.

    # network share mounted via NFSv3 on /mnt/auto/data
    data            -rw,vers=3,soft,async                        192.0.2.1:/tank1/data
    # network share mounted via CIFS on /mnt/auto/data1
    data1           -fstype=cifs,credentials=/root/smb.txt       ://192.0.2.1/data1
    # memory stick used regulary with known UUID, for example a Kindle
    kindle          -fstype=vfat,rw,uid=1000                     :UUID="4CBF-23A2"

Indirect mounts allow AutoFS to use wildcards. For example, if users\' home directories are stored on a different machine and mounted over NFS, AutoFS could be configured as follows:

[FILE] **`/etc/autofs/auto.master`**

    /home           /etc/autofs/auto.home

[FILE] **`/etc/autofs/auto.home`**

    *               neighborhood:/export/home/&

This way, when a user `larry` logs in and accesses some files in their home directory, AutoFS will effectively run the command:

`root `[`#`]`mount -t nfs neighborhood:/export/home/larry /home/larry`

### [[] Useful options]

These options can be given in the master map file.

-   `--timeout=<seconds>` specifies the number of seconds that an automounted filesystem can go unused before AutoFS unmounts it.
-   `--ghost` or `browse` (no dash in the latter form) can be useful for indirect mounts. It causes AutoFS to create the directory on which something would be mounted when the [automount] daemon starts up, rather than only when the directory is accessed.

For a full description of options, run

`user `[`$`]`man 5 auto.master`

### [[] Non-file maps]

In [/etc/autofs/auto.master], instead of merely specifying `map`, the second column can take a more complicated form such as `map-type:map`, which allows the map to be something other than a file. For instance, it can be an executable which prints out map specifications (the lines that would be included in a map file), or any of various types of databases. For a full description of recognized types, run

`user `[`$`]`man 5 auto.master`

### [[] Simple Windows-like Samba share mounting]

Here is a way to automatically mount network [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") shares, as Windows does. This configuration allows automounting a share by issuing the following command in a shell:

`user `[`$`]`cd /net/192.0.2.1/share`

or navigating to [/net/192.0.2.1/share] in a filesystem browser or dialog. The files inside will appear as if they were located on the local machine.

** Important**\
For this to work, [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") must be installed and configured prior to mounting.

[FILE] **`/etc/autofs/auto.master`**

    /net     file:/etc/autofs/auto.smbm    --ghost --nonstrict

[FILE] **`/etc/autofs/auto.smbm`**

    *        -fstype=autofs,-Dhost=&       file://etc/autofs/auto.share

[FILE] **`/etc/autofs/auto.share`**

    *         -fstype=cifs,username=guest,password=,file_mode=0664,dir_mode=0775,uid=netmount,gid=netmount,port=139     ://$/&

## [Syslog]

Configuring [[syslog-ng]](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") to redirect logs to a custom file such as [/var/log/autofs.log] requires setting up filters and log paths in the [syslog-ng] configuration. This determines which events are logged and where they are recorded. The following provides guidance on configuring [syslog-ng] to handle logs for the AutoFS service.

To begin, open the [syslog-ng] configuration file using root permissions:

`root `[`#`]`vim /etc/syslog-ng/syslog-ng.conf`

A filter for messages from the \'autofs\' service can be created within this file. The \'autofs\' service logs can be filtered by matching the program name as shown in the following configuration snippet:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Filter for autofs**

    filter f_autofs ;

After establishing the filter, define the log path that incorporates it, directing the output to the specified log file. Add the following lines to set the log path accordingly:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Log path for autofs**

    destination d_autofs ;
    log ;

Conclude the configuration by restarting the [syslog-ng] service to enforce the changes:

`root `[`#`]`/etc/init.d/syslog-ng restart`

To effectively activate syslog and ensure maximum debugging for the specified configuration, set the appropriate option flags in the AutoFS configuration file. Add the flag `OPTIONS="--debug"` to the file located at [/etc/conf.d/autofs]. After setting this option, proceed to restart the AutoFS service:

`root `[`#`]`/etc/init.d/autofs restart`

## [[] Troubleshooting]

In case of mount failure or problems use following steps to narrow the source of the issue.

Stop the autofs service:

`root `[`#`]`/etc/init.d/autofs stop`

Run the `automount` daemon in the foreground to log to stderr, add the verbose option to view logging of general status and progress messages in the current running terminal:

`root `[`#`]`automount -f -v`

As a regular system user mount the filesystem by changing into the directory:

`user `[`$`]`cd /net/gentoo`

Verify the output running the daemon in foreground and with verbose mode. *Example failure message displayed in the output below*:

`root `[`#`]`automount -f -v`

    Starting automounter version 5.1.6, master map auto.master
    using kernel protocol version 5.05
    mounted indirect on /net with timeout 300, freq 75 seconds
    attempting to mount entry /net/gentoo
    >> mount: /net/gentoo: bad option; for several filesystems (e.g. nfs, cifs) you might need a /sbin/mount.<type> helper program.
    mount(generic): failed to mount //example.net/larry (type cifs) on /net/gentoo
    failed to mount /net/gentoo

## [[] External resources]

-   [Automount mini-Howto](https://tldp.org/HOWTO/Automount.html) on The Linux Documentation Project website
-   [AutoFS page](https://help.ubuntu.com/community/Autofs) on the Ubuntu Community Help Wiki