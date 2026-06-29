**Resources**

[[]][Home](https://www.qemu.org/docs/master/index.html)

[[]][Official documentation](https://www.qemu.org/docs/master/index.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/https://www.wikipedia.com/QEMU "wikipedia:https://www.wikipedia.com/QEMU")

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/qemu)

[[]][GitLab](https://gitlab.com/qemu-project/qemu)

[[]][Official project wiki](https://wiki.qemu.org/Main_Page)

[[]][Bugs (upstream)](https://gitlab.com/groups/qemu-project/-/issues)

[[]][Blog](https://www.qemu.org/blog/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/qemu)

[qemu-img] is a QEMU disk image utility

The program is used to create, snapshot, clone, and shutdown disk image.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
    -   [[3.2] [Files]](#Files)
    -   [[3.3] [User permissions]](#User_permissions)
-   [[4] [Usage]](#Usage)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Introduction]

[qemu-img] creates, maintains, appends, and converts a block storage unit for use with most any virtual machines.

A complete list of storage format ([-f \<format-type\>]) option are:

  ----------------------------------------------------------------------------------------------------------------- --------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Format Option ([-f])   Format Type     Description
  blkdebug                                                                                                          pseudo-format   Used to inject rule-based errors into a block storage in exercising various error code path within [qcow2] block driver. Primarily used with QEMU unit test cases.
  blklogwrites                                                                                                      pseudo          Writes log of write operations on a monitored backend (host-side) block storage file.
  blkverify                                                                                                         pseudo          Performs correctness of block integrity by monitoring for data corruption on the guest-side (inside); useful with [blklogwrites] and [blkdebug] unit tests.
  bochs                                                                                                             read-only       Bochs image format
  cloop                                                                                                             read-only       Linux compressed loop image used commonly with compressed CD-ROMs image format (such as Knoppix CD-ROM).
  compress
  copy-before-write
  copy-on-read
  dmg                                                                                                               read-only       Apple Disk Image
  file
  ftp
  ftps
  gluster                                                                                                           network         Accesses the user space distributed file system
  host_cdrom
  host_device
  http
  https
  iscsi                                                                                                             network         Accesses the remote SCSI device.
  iser
  luks                                                                                                              pseudo          [luks] is used to open the LUKS v1 backing storage for copy-on-write operations
  nbd                                                                                                               network         Access remote image device that were exported using Network Block Device protocol
  nfs
  null-aio
  null-co
  nvme                                                                                                              block           Access the NVM Express (NVMe) storage controllers directly by userspace driver in QEMU. Useful for fastest operation.
  parallels                                                                                                         read-only       Parallels virtual machine image format
  preallocate                                                                                                       filter          A shim-module for pre-allocation some additional space when writing beyond file\'s EOF. Good for slow-allocation system.
  qcow                                                                                                              block           Older version of [qcow2].
  qcow2                                                                                                             block           The most common choice of file format in QEMU virtual machines.
  qed                                                                                                               block           Original QEMU block image format. Obsoleted by [qcow2] and [qcow] format.
  quorum
  raw                                                                                                               block           The simplest way for guest OS to directly write as-is to the host OS block storage.
  rbd
  replication                                                                                                       pseudo          Used to open the backing storage device for copy-on-write operations
  snapshot-access
  ssh                                                                                                               network         Accesses the disk images on a remote SSH server
  throttle
  vdi                                                                                                               block           VirtualBox v1.1 compatible image format
  vhdx                                                                                                              block           Hyper-V compatible image format
  vmdk                                                                                                              block           VMware 3 and 4 compatible image format
  vpc                                                                                                               block           VirtualPC compatible image format. A headerless block disk image used for backing stores. Often used with obsoleted [qed] image format.
  vvfat                                                                                                             block           Virtual [VFAT](https://wiki.gentoo.org/wiki/VFAT "VFAT") file system that is commonly found in Microsoft Windows and MS-DOS and clones. Can handle 12-bit, 16-bit, and 32-bit VFAT.
  ----------------------------------------------------------------------------------------------------------------- --------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Installation]

See [QEMU Installation](https://wiki.gentoo.org/wiki/QEMU#Installation "QEMU") for installation of [qemu-img].

## [Configuration]

### [Environment variables]

A list of all environment variables that are read and checked by the [qemu-img] command:

\

-   `SDL_VIDEODRIVER` - Sets to either [x11] or [sdl] if cannot be automatically determined.
-   `LISTEN_FDNAMES` - Pass the socket name descriptor(s) of the QEMU Disk Block Device to the `systemd-socketd` socket activation daemon.
-   `LISTEN_FDS` - Pass the file descriptor(s) (`fd`s) of the QEMU Disk Block Device to the `systemd-socketd` socket activation daemon.
-   `LISTEN_PID` - Pass the process ID (`PID`) of the QEMU Disk Block Device to the `systemd-socketd` socket activation daemon.
-   `QEMU_MODULE_DIR` - Base directory path spec to the QEMU modules.
-   `QEMU_AUDIO_DRV`
-   `QEMU_PATH`
-   `G_MESSAGES_DEBUG` - Error reporting
-   `QEMU_STRACE` - Enable \<cmd\>strace\</cmd\> (only on BSD)
-   `XDG_RUNTIME_DIR` - pass audio settings to the PulseAudio daemon/driver.

### [Files]

Files that are read by the host-side OS [qemu-img] command:

-   [/dev/cdrom]
-   [/dev/fdset]
-   [/dev/null]
-   [/dev/vfio/\<device-name\>]
-   [/proc/\<PID\>/cmdline]
-   [/proc/self/exe]
-   [/proc/self/fd]
-   [/proc/sys/vm/overcommit_memory]
-   [/sys/bus/pci/devices/%s/iommu_group]

\
Files that are written by the host-side OS [qemu-img] command:

-   [/var/run/qemu/qemu-socket-\<TMPID\>]
-   [/var/tmp/]

\

### [User permissions]

To use [qemu-img] as a non-root user, ensure each user has been added to the [qemu] group:

`root `[`#`]`gpasswd -a <user> qemu`

See [qemu-img configuration](https://wiki.gentoo.org/wiki/QEMU#Configuration "QEMU") for more setup on enabling user to use the [qemu-img] command.

## [Usage]

The [qemu-img] can be checked by running:

`root `[`#`]`qemu-img info /dev/sda`

    image: /dev/sda
    file format: raw
    virtual size: 187 GiB (201188179968 bytes)
    disk size: 0 B
    }}

    === Invocation ===

    [`#`]`emerge --ask --depclean --verbose app-emulation/qemu-img`

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [QEMU/Front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends") --- facilitate VM management and use

\

## [External resources]