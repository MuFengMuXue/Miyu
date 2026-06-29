[Samba](https://wiki.gentoo.org/wiki/Samba "Samba") has stackable VFS (Virtual File System) modules that can be used to extend with new features. One such VFS module is [vfs_shadow_copy2]. It is used to expose filesystem snapshots as **Previous Versions** to Windows clients.

This article explores using Samba to expose Shadow Copies as \'Previous Versions\' to Windows clients.

## Contents

-   [[1] [Configuration]](#Configuration)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Configuration]

[FILE] **`/etc/samba/smb.conf`Samba config file**

    [share]
    path = /mnt/pool/share
    comment = Shadow Copy Enabled Share

    vfs objects = shadow_copy2
    shadow:snapdir = /mnt/pool/snapshots/
    shadow:basedir = /mnt/pool/share
    shadow:sort = desc
    shadow:format = share_@GMT_%Y.%m.%d-%H.%M.%S
    shadow:localtime = yes

\
`shadow:format` is used to match the snapshots in `snapdir`

`user `[`$`]`ls -l /mnt/pool/snapshots`

    drwxr-xr-x 1 root    root         1252 Jan  4  2016 share_@GMT_2017.02.11-20.25.31

## [Usage]

Samba will automatically look for new snapshots and export them to Windows. A Windows client can then view them in the file\'s or folder\'s properties. [![Previous Versions as seen by a Windows client](/images/thumb/3/3d/Previous_versions.png/300px-Previous_versions.png)](https://wiki.gentoo.org/wiki/File:Previous_versions.png "Previous Versions as seen by a Windows client")

## [See also]

-   [Btrfs snapshots](https://wiki.gentoo.org/wiki/Btrfs_snapshots "Btrfs snapshots") --- script to **make automatic snapshots with [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs")** filesystem, using [btrfs subvolume list-new] function to create snapshots only when files have changed, so as to create fewer snapshots.
-   [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") --- a re-implementation of the [SMB/CIFS](https://wiki.gentoo.org/wiki/Smbnetfs "Smbnetfs") networking protocol, a Microsoft Windows alternative to Network File System ([NFS](https://wiki.gentoo.org/wiki/NFS "NFS")).
-   [Samba/Guide](https://wiki.gentoo.org/wiki/Samba/Guide "Samba/Guide") --- provides a details guide showing users how to share files and printers between Windows and \*nix PCs.

## [External resources]

-   [Sambs VFS Shadow Copy](https://www.samba.org/samba/docs/man/manpages/vfs_shadow_copy2.8.html)
-   [Sambs VFS modules](https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/VFS.html)
-   [Samba Website](https://www.samba.org/)