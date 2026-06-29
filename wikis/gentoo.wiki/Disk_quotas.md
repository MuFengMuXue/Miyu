**Resources**

[[]][Home](http://sourceforge.net/projects/linuxquota/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Disk_quota "wikipedia:Disk quota")

**Disk quotas** can be implemented by a system administrator as a way to manage restrictions on storage for users or groups of users.

Disk quotas allow the administrator to balance storage resources so that it is possible to manage finite capacity in a suitable way. An example of disk quotas in use would be, for example, a web hosting provider that allocates a certain amount of disk storage space per customer, or to limit certain users from consuming the full resources of the file-system, thereby preventing the file-system filling up and starving other users or the system of storage. There are two types of restrictions that can be put in place, one is [inode] which controls the number of files/directories, and [block] which can restrict based on storage blocks (size). When set limits are reached, it is possible to notify the system administrator or user consuming the resources in question, informing them to take appropriate action.

** Note**\
GFS2, [XFS](https://wiki.gentoo.org/wiki/XFS "XFS"), [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") and some other filesystems use their own quota system. This document only covers [Ext2](https://wiki.gentoo.org/wiki/Ext2 "Ext2"), [Ext3](https://wiki.gentoo.org/wiki/Ext3 "Ext3"), [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4"), [JFS](https://wiki.gentoo.org/wiki/JFS "JFS"), and ocfs2 file systems which are supported by the [[[sys-fs/quota]](https://packages.gentoo.org/packages/sys-fs/quota)[]] package.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [fstab]](#fstab)
    -   [[2.2] [Group quotas (local system)]](#Group_quotas_.28local_system.29)
    -   [[2.3] [Creating the quota files]](#Creating_the_quota_files)
    -   [[2.4] [Enabling quotas]](#Enabling_quotas)
    -   [[2.5] [Checking if quotas are enabled]](#Checking_if_quotas_are_enabled)
    -   [[2.6] [Environment variables]](#Environment_variables)
    -   [[2.7] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
        -   [[3.1.1] [Init scripts]](#Init_scripts)
        -   [[3.1.2] [repquota]](#repquota)
        -   [[3.1.3] [setquota]](#setquota)
        -   [[3.1.4] [edquota]](#edquota)
        -   [[3.1.5] [quotastats]](#quotastats)
        -   [[3.1.6] [quotaon & quotaoff]](#quotaon_.26_quotaoff)
        -   [[3.1.7] [quota]](#quota)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Turning off quotas]](#Turning_off_quotas)
    -   [[4.2] [Removing configuration]](#Removing_configuration)
    -   [[4.3] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Kernel support is required for disk quotas, if support for journaled quotas is required, the option \"Quota formats vfsv0 and vfsv1 support\" also needs to be enabled.

[KERNEL] **Enable support for disk quotas**

    File systems  --->
      [*] Quota support
      [*] Report quota messages through netlink interface
      [ ] Print quota warnings to console (OBSOLETE)
      ...
      <*> Quota format vfsv0 and vfsv1 support

### [USE flags]

### [USE flags for] [sys-fs/quota](https://packages.gentoo.org/packages/sys-fs/quota) [[]] [Linux quota tools]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`ldap`](https://packages.gentoo.org/useflags/ldap)         Add LDAP support (Lightweight Directory Access Protocol)
  [`netlink`](https://packages.gentoo.org/useflags/netlink)   Compile daemon receiving quota messages via netlink
  [`nls`](https://packages.gentoo.org/useflags/nls)           Add Native Language Support (using gettext - GNU locale utilities)
  [`rpc`](https://packages.gentoo.org/useflags/rpc)           Enable quota interaction via RPC
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)         Add support for TCP wrappers
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-20 09:05] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/quota`

## [Configuration]

### [fstab]

To enable quotas, some configuration is required by editing [/etc/fstab] and enabling [usrquota] and/or [grpquota] in the options for each file-system upon which quotas need to be managed. For journaled quota support, add the mount options [jqfmt]. Additional information regarding [/etc/fstab] and filesystem (quota) options can be found by referring to the [[[mount(8)]](https://man.archlinux.org/man/mount.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page. Quotas are set and edited by the quota tools which manage configuration files located in the root of each file-system named [aquota.user], and [aquota.group] for new quota version formats and [quota.user], [quota.group] for older formats.

`root `[`#`]`$EDITOR /etc/fstab`

[FILE] **`/etc/fstab`**

    # <DEV>    <MNTPOINT> <FSTYPE> <MNTOPTIONS>                     <DUMP> <PASS>
    # example line for just usrquota support
    /dev/sda8  /mnt/eg1   ext4     noatime,usrquota                      0 2
    # example line for grpquota
    /dev/sda9  /mnt/eg2   ext4     noatime,grpquota                      0 2
    # example line for usrquota, grpquota and journaled quota support
    /dev/sda10 /home      ext4     noatime,usrquota,grpquota,jqfmt=vfsv0 0 2

After [/etc/fstab] has been edited accordingly, the file-systems need to be remounted. Repeat the following mount command example below for every file-system that has been edited and enabled for quotas.

`root `[`#`]`mount -o remount /home`

### [][Group quotas (local system)]

** Note**\
This is incomplete and needs improvement

It is possible to apply quotas to groups of users, if this is desired a group has to be present on the system to assign the quota to. This creates a new group quotagroup and adds two users to the group, assuming there are already users alice and bob. For creating new users and groups please refer to [Complete_Handbook/Configuring_the_system#User_account](https://wiki.gentoo.org/wiki/Complete_Handbook/Configuring_the_system#User_account "Complete Handbook/Configuring the system") and [Knowledge_Base:Adding_a_user_to_a_group](https://wiki.gentoo.org/wiki/Knowledge_Base:Adding_a_user_to_a_group "Knowledge Base:Adding a user to a group").

`root `[`#`]`groupadd quotagroup `

`root `[`#`]`gpasswd --add alice quotagroup `

`root `[`#`]`gpasswd --add bob quotagroup `

### [Creating the quota files]

After [/etc/fstab] has been edited, the quota files need to be created with the [[[quotacheck(8)]](https://man.archlinux.org/man/quotacheck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command and the `-c` or `--create-files` option. The following command creates the quota files as necessary for user and group quotas on the [/home] filesystem.

`root `[`#`]`quotacheck --user --group --create-files /home `

### [Enabling quotas]

Gentoo provides an init script to run [quotacheck] and initialize quotas when the system starts. The file [/etc/conf.d/quota] can be edited and customized to provide different parameters to the [[[quotacheck(8)]](https://man.archlinux.org/man/quotacheck.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[quotaon(8)]](https://man.archlinux.org/man/quotaon.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] commands if necessary.

`root `[`#`]`$EDITOR /etc/conf.d/quota`

[FILE] **`/etc/conf.d/quota`**

    # /etc/conf.d/quota: config file for /etc/init.d/quota

    # Note: if your console is hooked up to a serial terminal,
    # you prob want to drop the '-v' from the OPTS vars below.

    # Run quotacheck ?
    RUN_QUOTACHECK="yes"

    # Options for quotacheck
    QUOTACHECK_OPTS="-avug"

    # Options for quotaon
    QUOTAON_OPTS="-avug"

    # Options for quotaoff
    QUOTAOFF_OPTS="-avug"

After doing any customization to the [/etc/conf.d/quota] file, it\'s time to start the quota system. The following commands start the quota init script and adds it to the runlevel to persist when the system reboots.

`root `[`#`]`/etc/init.d/quota start `

`root `[`#`]`rc-update add quota default `

### [Checking if quotas are enabled]

To make sure whether quotas are enabled or not, the following command can be executed.

`root `[`#`]`quotaon --print-state --all`

    group quota on /home (/dev/sda10) is on
    user quota on /home (/dev/sda10) is on

### [Environment variables]

?

### [Files]

/etc/quotagrpadmins /etc/quotatab

## [Usage]

The following procedures describe startup and general usage of the tools to administer quotas.

### [Invocation]

The Linux quota tools contain several commands to create and manage filesystem quotas. The following are some basic examples of putting the tools to use.

#### [Init scripts]

Gentoo provides an init script to check quotas and turn quotas on and off. Using the Gentoo init scripts are preferred over using quotaon / quotaoff manually unless it\'s known what is really being done.

Starting quotas through the Gentoo init script

`root `[`#`]`/etc/init.d/quota start `

Stopping quotas through the Gentoo init script

`root `[`#`]`/etc/init.d/quota stop `

#### [repquota]

Displaying summaries of quotas for filesystems

`root `[`#`]`repquota -a`

#### [setquota]

Setting disk quotas on the command line is accomplished with the [[[setquota(8)]](https://man.archlinux.org/man/setquota.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command. From the man page the usage states \<block-softlimit\> \<block-hardlimit\> \<inode-softlimit\> \<inode-hardlimit\> as parameters to be passed when setting quotas, these need to be balanced according to requirements. To unset a quota limit the value can be set at 0 (zero).

To calculate the amount of blocks per GB a command similar to the following can be used, replace 32 with the required GB for the quotas to be set if it\'s required to limit based on [block] (size) usage.

`user `[`$`]`awk '/BLOCK_SIZE[[:blank:]]/' /usr/include/sys/mount.h`

33554432

Once the [inode] and [block] values have been decided, a quota can now be set. The following command sets a soft limit of 30GB, a hard limit of 32GB and removes inode limits for user alice on the [/home] file-system.

** Warning**\
The parameters needs to be researched and tweaked according to requirements just like every other command, do not attempt copy and paste this example just changing the user and file-system or the user in question may be complaining very soon!

`root `[`#`]`setquota -u alice 31457280 33554432 0 0 /home`

#### [edquota]

Editing user or group quotas is accomplished with the [[[edquota(8)]](https://man.archlinux.org/man/edquota.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command, the user or group to be edited, and -a for all filesystems or specify the filesystem with the -f option. The following command will edit the quotas for user bob on the /home filesystem. The set `EDITOR` will be opened to begin editing quotas.

`root `[`#`]`edquota -f /home bob`

    Disk quotas for user bob (uid 1006):
      Filesystem    blocks       soft       hard     inodes     soft     hard
      /dev/sda10        28          0          0         11        0        0

Changing the values allows placing soft or hard limits on the amount of blocks or inodes for user bob, exiting the `EDITOR` and saving the file will apply the specified quotas.

#### [quotastats]

Querying quota statistics

`root `[`#`]`quotastats`

#### [][quotaon & quotaoff]

** Note**\
The [[[quotaon(8)]](https://man.archlinux.org/man/quotaon.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[quotaoff(8)]](https://man.archlinux.org/man/quotaoff.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] can be run when the system starts and shuts down by the Gentoo init scripts, these are just examples to show how the tools can be used.

Turning on filesystem quotas for all filesystems

`root `[`#`]`quotaon -a`

Turning off filesystem quotas for all filesystems

`root `[`#`]`quotaoff -a`

#### [quota]

Displaying users disk usage and limits is accomplished with the [[[quota(1)]](https://man.archlinux.org/man/quota.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command.

`user `[`$`]`quota`

## [Removal]

### [Turning off quotas]

The quotas for each filesystem should be turned off before removal and removed from the runlevel.

`root `[`#`]`/etc/init.d/quota stop `

`root `[`#`]`rc-update del quota default `

### [Removing configuration]

To clean up the system if quotas are not required any more perform the following steps

Edit [/etc/fstab] and remove quota options for filesystems

Remove the aquota.user, and aquota.group or quota.user, quota.group configuration files in the root of the filesystem.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-fs/quota`

## [See also]

-   [Ext2](https://wiki.gentoo.org/wiki/Ext2 "Ext2") - ext2 filesystem.
-   [Ext3](https://wiki.gentoo.org/wiki/Ext3 "Ext3") - ext3 filesystem with journaling support.
-   [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") - Extended file system version 4.
-   [XFS](https://wiki.gentoo.org/wiki/XFS "XFS") - A high-performance journaling filesystem that also provides a quota system.
-   [JFS](https://wiki.gentoo.org/wiki/JFS "JFS") - 64-bit journaling filesystem created by IBM.
-   [Centralized_authentication_using_OpenLDAP](https://wiki.gentoo.org/wiki/Centralized_authentication_using_OpenLDAP "Centralized authentication using OpenLDAP") - Quotas can be used with LDAP

## [External resources]

-   \[[Information on quotas from the ext4 wiki](https://ext4.wiki.kernel.org/index.php/Quota)\]