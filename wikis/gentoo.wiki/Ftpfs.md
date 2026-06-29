[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=CurlFtpFS&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Article status**

[[]]This article has some todo items:\

-   Add instructions for using from fstab.
-   Expand article.

**CurlFtpFS** allows for [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") an FTP folder as a regular directory to the local directory tree.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [As a regular user]](#As_a_regular_user)
        -   [[2.1.1] [Mounting]](#Mounting)
        -   [[2.1.2] [Unmounting]](#Unmounting)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

CurlFtpFS needs [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") activated in the kernel:

[KERNEL] **Activating FUSE**

    File systems --->
       <*> FUSE (Filesystem in Userspace) support

### [Emerge]

Install [[[net-fs/curlftpfs]](https://packages.gentoo.org/packages/net-fs/curlftpfs)[]]:

`root `[`#`]`emerge --ask net-fs/curlftpfs`

## [Usage]

### [As a regular user]

First, create a mount point:

`user `[`$`]`mkdir ./ftp`

#### [Mounting]

Then mount the necessary *catalog* from the *server* to this mount point:

`user `[`$`]`curlftpfs ftp://server/catalog/ ./ftp/ -o user=username:password,utf8`

#### [Unmounting]

`user `[`$`]`fusermount -u ./ftp`

## [See also]

-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.