This page contains [[changes](https://wiki.gentoo.org/index.php?title=Filesystem_in_Userspace&oldid=1300514&diff=1429106)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace/hu "Fájlrendszer a felhasználói térben (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace/zh-cn "用户空间文件系统 (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace/ja "Filesystem in Userspace (100% translated)")

**Resources**

[[]][GitHub](https://github.com/libfuse/libfuse)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Filesystem_in_Userspace "wikipedia:Filesystem in Userspace")

**F**ilesystem in **U**ser**s**pac**e** (FUSE) provides a way for users to mount file systems without needing special permissions (mounting in Linux is generally reserved to those with administrative privileges).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Mounting filesystems]](#Mounting_filesystems)
    -   [[3.3] [Unmounting filesystems]](#Unmounting_filesystems)
-   [[4] [Removal]](#Removal)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [AppImages]](#AppImages)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Enable support for FUSE**

    File systems  --->
        <*> FUSE (Filesystem in Userspace) support

### [USE flags]

### [USE flags for] [sys-fs/fuse](https://packages.gentoo.org/packages/sys-fs/fuse) [[]] [An interface for filesystems implemented in userspace]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+suid`](https://packages.gentoo.org/useflags/+suid)               Enable setuid root program(s)
  [`examples`](https://packages.gentoo.org/useflags/examples)         Install examples, usually source code
  [`io-uring`](https://packages.gentoo.org/useflags/io-uring)         Enable the use of io_uring for efficient asynchronous IO and system requests
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)       Enable SystemTap/DTrace tracing
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 14:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

As with most file systems, after building support for the file system into the kernel be sure to install the user space tools:

`root `[`#`]`emerge --ask sys-fs/fuse`

## [Configuration]

### [Files]

The following configuration files are available for FUSE:

-   [/etc/fuse.conf]

There are two configuration variables available in the [fuse.conf] file:

-   `mount_max` - Sets the maximum number of FUSE mounts allowed to non-root users (defaults to 1000 if unset).
-   `user_allow_other` - Allows non-root users to specify the `allow_other` or `allow_root` mount options. This is disabled for security reasons.

## [Usage]

### [Invocation]

`user `[`$`]`fusermount3 -h`

    fusermount3: [options] mountpoint
    Options:
     -h                 print help
     -V                 print version
     -o opt[,opt...]   mount options
     -u                 unmount
     -q                 quiet
     -z                 lazy unmount

### [Mounting filesystems]

Use the [fusermount3] command:

`user `[`$`]`fusermount3 /path/to/mountpoint`

### [Unmounting filesystems]

Filesystems can be unmounted using either the [umount] *or* the [fusermount3] command:

`user `[`$`]`fusermount3 -u /path/to/mountpoint`

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose sys-fs/fuse`

## [Troubleshooting]

### [AppImages]

You may see an error message like the one below when executing an AppImage.

`user `[`$`]`./app.appimage`

    AppImages require FUSE to run.
    You might still be able to extract the contents of this AppImage
    if you run it with the --appimage-extract option.
    See https://github.com/AppImage/AppImageKit/wiki/FUSE
    for more information

[[[sys-fs/fuse]](https://packages.gentoo.org/packages/sys-fs/fuse)[]] provides [fusermount3] but older AppImages may need `sys-fs/fuse:0`.

`root `[`#`]`emerge --ask sys-fs/fuse:0`

## [See also]

-   [Filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") --- a means to organize data to be retained after a program terminates.

## [External resources]

-   [Writing a FUSE Filesystem: a Tutorial](https://www.cs.nmsu.edu/~pfeiffer/fuse-tutorial/)
-   [FUSE](https://wiki.archlinux.org/index.php/FUSE) (Arch Linux Wiki)