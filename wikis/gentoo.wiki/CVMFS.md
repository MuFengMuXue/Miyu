**Resources**

[[]][Home](https://cernvm.cern.ch/portal/filesystem)

CVMFS is a FUSE module which implements an HTTP read-only filesystem.

## Contents

-   [[1] [Concepts]](#Concepts)
-   [[2] [CVMFS server setup]](#CVMFS_server_setup)
    -   [[2.1] [Kernel with aufs options enabled]](#Kernel_with_aufs_options_enabled)
    -   [[2.2] [Apache server configuration]](#Apache_server_configuration)
    -   [[2.3] [Create CVMFS repository]](#Create_CVMFS_repository)
    -   [[2.4] [Repository update]](#Repository_update)
-   [[3] [CVMFS client setup]](#CVMFS_client_setup)
    -   [[3.1] [Installation]](#Installation)
    -   [[3.2] [Reload the updated repository]](#Reload_the_updated_repository)

## [Concepts]

## [CVMFS server setup]

To get an cvmfs server system working you will need the following steps.

### [Kernel with aufs options enabled]

The [[[sys-kernel/aufs-sources]](https://packages.gentoo.org/packages/sys-kernel/aufs-sources)[]] contains Linux Kernel with the aufs support module. First, you must install this package:

`root `[`#`]`emerge -av sys-kernel/aufs-sources`

Note that in order to use [genkernel] to generate Linux kernel and initramfs, with aufs-sources-3.10.25 as an example, you must:

`root `[`#`]` eselect kernel set linux-3.10.25-aufs `

`root `[`#`]` genkernel --menuconfig all `

** Note**\
[linux] is a symbolic link to the real kernel source.

[KERNEL]

    File systems  --->
          [*] FUSE (Filesystem in Userspace) support
          [*] miscellaneous filesystems  --->
           [*]   Aufs (Advanced multi layered unification filesystem) support
           [*]     Detect direct branch access (bypassing aufs)
           [*]     NFS-exportable aufs
           [*]     Readdir in userspace
           [*]     Show whiteouts
           [*]     Ramfs (initramfs/rootfs) as an aufs branch
           [*]     Fuse fs as aufs branch
           [ ]     Debug aufs

### [Apache server configuration]

The cvmfs server utility will use [/srv/cvmfs] as storage location. Therefore, the `DocumentRoot` should be config to the `/srv`.

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    DocumentRoot "/srv"

    <Directory "/srv">
        ....
    </Directory>

`root `[`#`]`/etc/init.d/apache2 restart`

### [Create CVMFS repository]

1\. Build and install cvmfs

Download cvmfs code from github [cvmfs](https://github.com/cvmfs/cvmfs).

The cvmfs build system uses cmake. In order to compile and install, run from the source directory.

`root `[`#`]` mkdir -p build `

`root `[`#`]` cd build `

`root `[`#`]` cmake ../ `

`root `[`#`]` make `

`root `[`#`]` make install `

2\. Create the two directories and ensure adequate space.

-   /cvmfs
-   /srv

3\. Create a new cvmfs server \"file system\" and repository structure:

`root `[`#`]`cvmfs_server mkfs my.test.repo`

If there is an error in creation, remove the repository:

`root `[`#`]`cvmfs_server rmfs my.test.repo`

### [Repository update]

In cvmfs server, switch repo to a copy-on-write enabled cvmfs volume.

`root `[`#`]`cvmfs_server tansaction`

Then, make the necessary changes to the repository.

Run [cvmfs_server publish] to finalize your new repository revision, or run [cvmfs_server abort] to clear all changes and start over again.

`root `[`#`]`cvmfs_server publish`

## [CVMFS client setup]

### [Installation]

Install the cvmfs package from [cvmfs](https://github.com/cvmfs/cvmfs). See the above section.

Install the [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS"). Typically, mounting of cvmfs repositories is handled by AutoFS. For Gentoo, you must both install autofs utility and open kernel option.

Check the [/etc/auto.master] has contains `/cvmfs /etc/auto.cvmfs`. Then, do the base setup:

`root `[`#`]`cvmfs_config setup`

Create [/etc/cvmfs/default.local] to set base options of cvmfs client:

[FILE] **`/etc/cvmfs/default.local`minimal sample of config**

    CVMFS_REPOSITORIES=your.cvmfs.repo
    CVMFS_CACHE_BASE = /path/to/your/cache
    CVMFS_RELOAD_SOCKETS = /path/to/your/cache
    CVMFS_SERVER_URL = http://cvmfs-stratum-one.cern.ch/cvmfs/your.cvmfs.repo
    CVMFS_HTTP_PROXY = DIRECT

Then, use the [cvmfs2] command line to mount cvmfs to local for example:

`root `[`#`]`cvmfs2 -o config=/etc/cvmfs/default.local your.cvmfs.repo path/to/mount/cvmfs`

At last, check if cvmfs mounts correctly.

`root `[`#`]`cvmfs_config probe`

### [Reload the updated repository]

Internally cvmfs checks for file system updates once per hour by default. You can certainly configure a lower update interval. In order to force frequent catalog updates, you can set the configuration variable `CVMFS_MAX_TTL` to a value in seconds. But be warned, that a very short TTL might result in high load on your server infrastructure.

if you want to invest a bit of scripting, you can also use [cvmfs_talk remount] or [cvmfs_config reload] to trigger a reload of the newest snapshot (without service interruption).