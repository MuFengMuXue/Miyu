This page contains [[changes](https://wiki.gentoo.org/index.php?title=Smbnetfs&diff=1427323)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Smbnetfs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://sourceforge.net/projects/smbnetfs/)

[[]][GitWeb](https://sourceforge.net/p/smbnetfs/git/ci/master/tree/)

smbnetfs is a [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE")-based filesystem for SMB/CIFS shares. It enables each user to mount Windows-based network shares within their own userspace.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
        -   [[2.1.1] [Credentials]](#Credentials)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

See the [Kernel section](https://wiki.gentoo.org/wiki/FUSE#Kernel "FUSE") of the FUSE article for kernel confirmation.

### [USE flags]

### [USE flags for] [net-fs/smbnetfs](https://packages.gentoo.org/packages/net-fs/smbnetfs) [[]] [FUSE filesystem for SMB shares]

  ----------------------------------------------------------- ----------------------------------------------------------------------
  [`keyring`](https://packages.gentoo.org/useflags/keyring)   Enable support for freedesktop.org Secret Service API password store
  ----------------------------------------------------------- ----------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install the userspace utilities:

`root `[`#`]`emerge --ask net-fs/smbnetfs`

## [Configuration]

### [Files]

Import files related to smbnetfs include:

-   [[\~/.smb/smbnetfs.conf]](#Credentials) - The local (user-specific) configuration file. This file is not installed in user home directories by default (see below).

#### [Credentials]

Create the [\~/.smb] directory, then copy the configuration file to the configuration location. Note: depending on which version of the software was installed, the filesystem path could change. Determining the version of the software Portage installed will help determine the name of the first network path in the [bunzip2] command:

`user `[`$`]`mkdir ~/.smb `

`user `[`$`]`bunzip2 -c /usr/share/doc/smbnetfs-0.6.0/smbnetfs.conf.bz2 > ~/.smb/smbnetfs.conf `

Next, modify the configuration file in order to gain network authentication. There are different methods of inputting authentication credentials: GNOME Keyring (which can be effective if the GNOME desktop environment is being used) or username/password fields in the [smbnetfs.conf] file itself.

For example, when entering username/password in the configuration file, uncomment the following line and add appropriate values. `guest` should be substituted with the username and the next set of quotes should include the password:

[FILE] **`~/.smb/smbnetfs.conf`**

    #auth                   "guest" ""

** Warning**\
Anyone who has access to read the files in the user\'s home directory will be able to see the username/password information contained in the [\~/.smb/smbnetfs.conf] file above. Lock down the [/home] directory for maximum security.

## [Usage]

### [Invocation]

[smbnetfs] needs to know where to mount the shares. If a directory for them does not yet exist create one, then mount things there:

`user `[`$`]`mkdir ~/mnt `

`user `[`$`]`smbnetfs ~/mnt `

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-fs/smbnetfs`

## [See also]

-   [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") --- a re-implementation of the [SMB/CIFS] networking protocol, a Microsoft Windows alternative to Network File System ([NFS](https://wiki.gentoo.org/wiki/NFS "NFS")).

## [External resources]