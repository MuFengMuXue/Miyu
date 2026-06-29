[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Virtiofs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://virtio-fs.gitlab.io/)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/virtiofsd)

[virtiofs] is a shared file system that lets virtual machines access a directory tree on the host.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [QEMU VMs]](#QEMU_VMs)

## [Installation]

### [USE flags]

### [USE flags for] [app-emulation/virtiofsd](https://packages.gentoo.org/packages/app-emulation/virtiofsd) [[]] [Shared file system for virtual machines]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 10:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-emulation/virtiofsd`

## [Usage]

Start [virtiofsd] with the relevant shared directory, and a path to be used as a socket:

`user `[`$`]`SHARED_DIR=/home/user/share/`

`user `[`$`]`SOCKET_PATH=/tmp/vhostqemu`

`user `[`$`]`/usr/libexec/virtiofsd --shared-dir "$" --socket-path "$" --cache auto`

### [QEMU VMs]

The guest VM needs to be running the Linux kernel, version 5.4 or later, with the `CONFIG_VIRTIO_FS` kernel configuration option enabled.

Start [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") with your preferred options, plus the following:

    -chardev socket,id=char0,path="$"
    -device vhost-user-fs-pci,queue-size=1024,chardev=char0,tag=VHOST_TAG
    -object memory-backend-file,id=mem,size=MEM_SIZE,mem-path=/dev/shm,share=on -numa node,memdev=mem

where `VHOST_TAG` is an arbitrary name (e.g. `myfs`) that will be used with a [[[mount(8)]](https://man.archlinux.org/man/mount.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command inside the guest, and `MEM_SIZE` is the memory size you specified with the `-m` option.

Once logged in on the guest as root, mount the virtiofs using the VHOST_TAG specified when starting QEMU:

`root `[`#`]`mount -t virtiofs myfs /mnt`

The contents of `SHARED_DIR` should now be available in the [/mnt] directory.