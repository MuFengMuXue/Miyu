**Resources**

[[]][Home](https://www.samba.org)

[[]][Package information](https://packages.gentoo.org/packages/net-fs/samba)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Samba_(software) "wikipedia:Samba (software)")

[[]][GitWeb](https://git.samba.org/)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Samba "Project:Samba")][Project](https://wiki.gentoo.org/wiki/Project:Samba "Project:Samba")

[[]][Guide](https://wiki.gentoo.org/wiki/Samba/Guide "Samba/Guide")

[[]][Official documentation](https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/)

**Samba** is a re-implementation of the [SMB/CIFS](https://wiki.gentoo.org/wiki/Smbnetfs "Smbnetfs") networking protocol, a Microsoft Windows alternative to Network File System ([NFS](https://wiki.gentoo.org/wiki/NFS "NFS")).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Samba]](#Samba)
        -   [[1.2.1] [USE flags]](#USE_flags)
        -   [[1.2.2] [Emerge]](#Emerge)
    -   [[1.3] [CIFS]](#CIFS)
        -   [[1.3.1] [USE flags]](#USE_flags_2)
        -   [[1.3.2] [Emerge]](#Emerge_2)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Services]](#Services)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [CIFS share]](#CIFS_share)
        -   [[2.2.1] [Mount the shared content via CLI]](#Mount_the_shared_content_via_CLI)
        -   [[2.2.2] [Mount the shared content automatically via fstab]](#Mount_the_shared_content_automatically_via_fstab)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Cannot resolve \<server-name\>]](#Cannot_resolve_.3Cserver-name.3E)
    -   [[3.2] [Shutdown process hangs when trying to unmount CIFS shares]](#Shutdown_process_hangs_when_trying_to_unmount_CIFS_shares)
    -   [[3.3] [Client asking for share username/password]](#Client_asking_for_share_username.2Fpassword)
    -   [[3.4] [Samba daemon fails to start without error]](#Samba_daemon_fails_to_start_without_error)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enabling CIFS and SMB2/SMB3 support**

File Systems \-\--\>

       [*] Network File Systems ---> Search for <code>CONFIG_NETWORK_FILESYSTEMS</code> to find this item.
           [*] SMB3 and CIFS support (advanced network filesystem) Search for <code>CONFIG_CIFS</code> to find this item.
               [*] Extended Statistics Search for <code>CONFIG_CIFS_STATS2</code> to find this item.
               [*] Support legacy servers which use less secure dialects Search for <code>CONFIG_CIFS_ALLOW_INSECURE_LEGACY</code> to find this item.
               [*] CIFS Extended Attributes Search for <code>CONFIG_CIFS_XATTR</code> to find this item.
                   [*] CIFS POSIX Extentions Search for <code>CONFIG_CIFS_POSIX</code> to find this item.

### [Samba]

Samba is a full software suite capable of hosting file shares via SMB, connecting to SMB share hosted non-locally, along with many other features. If the system will only need to mount shares hosted on other systems, then jump to the [CIFS section](https://wiki.gentoo.org/wiki/Samba#CIFS "Samba").

#### [USE flags]

### [USE flags for] [net-fs/samba](https://packages.gentoo.org/packages/net-fs/samba) [[]] [Samba Suite Version 4]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+regedit`](https://packages.gentoo.org/useflags/+regedit)                 Enable support for regedit command-line tool
  [`+system-mitkrb5`](https://packages.gentoo.org/useflags/+system-mitkrb5)   Use app-crypt/mit-krb5 instead of app-crypt/heimdal.
  [`acl`](https://packages.gentoo.org/useflags/acl)                           Add support for Access Control Lists
  [`addc`](https://packages.gentoo.org/useflags/addc)                         Enable Active Directory Domain Controller support
  [`ads`](https://packages.gentoo.org/useflags/ads)                           Enable Active Directory support
  [`ceph`](https://packages.gentoo.org/useflags/ceph)                         Enable support for Ceph distributed filesystem via sys-cluster/ceph
  [`client`](https://packages.gentoo.org/useflags/client)                     Enables the client part
  [`cluster`](https://packages.gentoo.org/useflags/cluster)                   Enable support for clustering
  [`cups`](https://packages.gentoo.org/useflags/cups)                         Add support for CUPS (Common Unix Printing System)
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`fam`](https://packages.gentoo.org/useflags/fam)                           Enable FAM (File Alteration Monitor) support
  [`glusterfs`](https://packages.gentoo.org/useflags/glusterfs)               Enable support for Glusterfs filesystem via sys-cluster/glusterfs
  [`gpg`](https://packages.gentoo.org/useflags/gpg)                           Use app-crypt/gpgme for AD DC
  [`iprint`](https://packages.gentoo.org/useflags/iprint)                     Enabling iPrint technology by Novell
  [`json`](https://packages.gentoo.org/useflags/json)                         Enable json audit support through dev-libs/jansson
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                         Add LDAP support (Lightweight Directory Access Protocol)
  [`llvm-libunwind`](https://packages.gentoo.org/useflags/llvm-libunwind)     Use llvm-runtimes/libunwind instead of sys-libs/libunwind
  [`lmdb`](https://packages.gentoo.org/useflags/lmdb)                         Enable LMDB backend for bundled ldb
  [`pam`](https://packages.gentoo.org/useflags/pam)                           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`profiling-data`](https://packages.gentoo.org/useflags/profiling-data)     Enables support for collecting profiling data
  [`python`](https://packages.gentoo.org/useflags/python)                     Add optional support/bindings for the Python language
  [`quota`](https://packages.gentoo.org/useflags/quota)                       Enables support for user quotas
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`snapper`](https://packages.gentoo.org/useflags/snapper)                   Enable vfs_snapper module (requires sys-apps/dbus)
  [`spotlight`](https://packages.gentoo.org/useflags/spotlight)               Enable support for spotlight backend
  [`syslog`](https://packages.gentoo.org/useflags/syslog)                     Enable support for syslog
  [`system-heimdal`](https://packages.gentoo.org/useflags/system-heimdal)     Use app-crypt/heimdal instead of bundled heimdal.
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`unwind`](https://packages.gentoo.org/useflags/unwind)                     Enable libunwind usage for backtraces
  [`winbind`](https://packages.gentoo.org/useflags/winbind)                   Enables support for the winbind auth daemon
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)                 Support for DNS Service Discovery (DNS-SD)
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 19:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Warning**\
Especially when setting up an AD DC: Read the current Samba documentation and release notes. MIT kerberos support is still marked experimental in Samba. System Heimdal support also seems broken at the Samba side - That\'s why, system-heimdal keyword is currently hard masked. For AD DC production environments, running Samba with the bundled heimdal kerberos should be considered at the moment.

#### [Emerge]

Install Samba:

`root `[`#`]`emerge --ask --noreplace net-fs/samba`

Samba can also be installed by setting the global `USE` flag `samba` and updating the system:

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [CIFS]

CIFS utilities are capable of mounting hosted file shares via SMB. If the system will need to do more than mounting SMB shares, then jump to the [Samba section](https://wiki.gentoo.org/wiki/Samba#Samba "Samba").

#### [USE flags]

If the full Samba software suite is not needed, the [[[net-fs/cifs-utils]](https://packages.gentoo.org/packages/net-fs/cifs-utils)[]] package is available:

### [USE flags for] [net-fs/cifs-utils](https://packages.gentoo.org/packages/net-fs/cifs-utils) [[]] [Tools for Managing Linux CIFS Client Filesystems]

  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+acl`](https://packages.gentoo.org/useflags/+acl)         Add support for Access Control Lists
  [`+ads`](https://packages.gentoo.org/useflags/+ads)         Enable Active Directory support and create cifs.idmap binary - idmap support
  [`+caps`](https://packages.gentoo.org/useflags/+caps)       Enable sys-libs/libcap-ng support
  [`+python`](https://packages.gentoo.org/useflags/+python)   Enable support for python and install python tools
  [`creds`](https://packages.gentoo.org/useflags/creds)       cifs credentials support
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`systemd`](https://packages.gentoo.org/useflags/systemd)   Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-15 08:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

Emerge the CIFS user-space tools:

`root `[`#`]`emerge --ask net-fs/cifs-utils`

## [Usage]

Before starting the service, first you need to prepare [/etc/samba/smb.conf], as [smbd] will refuse to start without it. A good starting point is the [/etc/samba/smb.conf.default] file:

`root `[`#`]`cp -i /etc/samba/smb.conf.default /etc/samba/smb.conf`

You will need to edit the [smb.conf] file to add the necessary share definitions. Please consult the [Samba/Guide](https://wiki.gentoo.org/wiki/Samba/Guide "Samba/Guide") to get more information.

### [Services]

#### [OpenRC]

To start Samba when the system boots, add it to the default runlevel:

`root `[`#`]`rc-update add samba default`

To start the Samba service immediately:

`root `[`#`]`rc-service samba start`

For more-advanced service-management information, see the [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") article.

#### [systemd]

For systemd users, the Samba service can be configured to start during boot using [systemctl]:

`root `[`#`]`systemctl enable smb.service`

To start the service immediately issue:

`root `[`#`]`systemctl start smb.service`

### [CIFS share]

#### [Mount the shared content via CLI]

Once the client is fully configured, the shares can soon be accessed.

Create the mount points:

`root `[`#`]`mkdir -p /mnt/My-Disk/ `

Manually mount the exported folders:

`root `[`#`]`mount.cifs //O2-Foobar/Media /mnt/My-Disk/Media -o guest`

`root `[`#`]`mount.cifs //O2-Foobar/Shared /mnt/My-Disk/Shared -o guest`

#### [Mount the shared content automatically via fstab]

To automatically mount guest shares on boot:

[FILE] **`/etc/fstab`**

    //O2-Foobar/Media  /mnt/My-Disk/Media  cifs guest
    //O2-Foobar/Shared /mnt/My-Disk/Shared cifs guest

To define user protected shared which can be mounted manually

[FILE] **`/etc/fstab`**

    //O2-Foobar/Media  /mnt/My-Disk/Media  cifs _netdev,noauto,user=larry
    //O2-Foobar/Shared /mnt/My-Disk/Shared cifs _netdev,noauto,user=larry

These mounts can be mounted with:

`root `[`#`]`mount /mnt/My-Disk/ `

** Note**\
\* In the case of permission problems are encountered when trying to create files and folders on the disk, try to use `gid=<user's_gid>, uid=<user's_uid>`

-   Be sure to replace `<user's_gid>` with the user ID of choice.

## [Troubleshooting]

Some problems may occur when trying to mount new CIFS shares. The following sections attempt to provide resolutions to common problems.

### [][Cannot resolve \<server-name\>]

More specifically, the actual error:

`root `[`#`]`mount.cifs ...`

    "mount error: could not find target server. TCP name foo/bar not found. No ip
    address specified and hostname not found"

This can easily be fixed by editing [/etc/nsswitch] and appending `wins` next to the `hosts` entry:

[FILE] **`/etc/nsswitch`**

    hosts: files dns wins

If this does not work, use the CIFS server\'s IP address instead of the O2-Foobar hostname. The `nmblookup` utility (provided by [[[net-fs/samba]](https://packages.gentoo.org/packages/net-fs/samba)[]]) comes in handy when trying to find the IP address of an CIFS host:

`root `[`#`]`nmblookup O2-Foobar`

### [Shutdown process hangs when trying to unmount CIFS shares]

If the system shutdown hangs at

` `[`*`]` Unmounting network filesystems ...`

then users must make sure the CIFS shares are unmounted properly before [udev](https://wiki.gentoo.org/wiki/Udev "Udev") tries to stop. One way to work around this is to create [local.d](https://wiki.gentoo.org/wiki/Local.d "Local.d") scripts to unmount the CIFS filesystems:

`root `[`#`]`echo "umount -a -t cifs -f" > /etc/local.d/cifs.stop `

`root `[`#`]`chmod a+x /etc/local.d/cifs.stop`

### [][Client asking for share username/password]

If Samba does not start after upgrading to Samba 4.2.11 with the following error:

    ../lib/param/loadparm.c:1082(lp_set_enum_parm)
    WARNING: Ignoring invalid value 'share' for parameter 'security'
    ../source3/smbd/server.c:1256(main)
    error opening config file '/etc/samba/smb.conf'

Change the Samba `security` parameter from `share` to `user`:

[FILE] **`/etc/samba/smb.conf`**

    [global]
    security = user

If guest access is enabled and the client is requesting the share username/password, set the `map to guest` parameter to `bad user`:

[FILE] **`/etc/samba/smb.conf`**

    [global]
    map to guest = bad user

### [Samba daemon fails to start without error]

If Samba daemon does not start:

`root `[`#`]`/etc/init.d/samba restart`

     * samba -> start: smbd ...
     * start-stop-daemon: failed to start `/usr/sbin/smbd' [ !! ]
     * samba -> start: nmbd ...
     * start-stop-daemon: failed to start `/usr/sbin/nmbd' [ !! ]
     * Error: starting services (see system logs)
     * samba -> stop: smbd ...
     * start-stop-daemon: no matching processes found      [ ok ]
     * samba -> stop: nmbd ...
     * start-stop-daemon: no matching processes found      [ ok ]

And Samba logs do not indicate any errors:

[FILE] **`/var/log/samba/log.smbd`**

    [2022/06/04 20:20:48.851120,  0] ../../source3/smbd/server.c:1741(main)
      smbd version 4.16.1 started.
      Copyright Andrew Tridgell and the Samba Team 1992-2022

Check that [/var/lock] has space:

`root `[`#`]`df -h /var/lock`

    Filesystem      Size  Used Avail Use% Mounted on
    tmpfs           1.0M  1.0M     0 100% /var/lock

## [See also]

-   [Samba (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#Samba "Security Handbook/Securing services") - The Security Handbook\'s entry on how to secure a system running Samba.
-   [Samba/Guide](https://wiki.gentoo.org/wiki/Samba/Guide "Samba/Guide") --- provides a details guide showing users how to share files and printers between Windows and \*nix PCs.
-   [Samba/Samba 4 Migration](https://wiki.gentoo.org/wiki/Samba/Samba_4_Migration "Samba/Samba 4 Migration") --- introduces the migration of Samba 3 to Samba 4 with LDAP on Gentoo boxes.
-   [Smbnetfs](https://wiki.gentoo.org/wiki/Smbnetfs "Smbnetfs") --- a [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE")-based filesystem for SMB/CIFS shares.
-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.
-   [Nfs-utils](https://wiki.gentoo.org/wiki/Nfs-utils "Nfs-utils") --- a file system protocol that allows client machines to access network attached filesystems (called exports) from a host system.

## [External resources]

-   [Practical Exercises in Successful Samba Deployment](https://www.samba.org/samba/docs/man/Samba-Guide/)
-   [Samba Howto Collection](https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/)
-   [Samba GUI](https://www.samba.org/samba/GUI/)