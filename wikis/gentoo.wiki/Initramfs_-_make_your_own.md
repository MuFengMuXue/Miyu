## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Why make your own]](#Why_make_your_own)
    -   [[1.2] [Why use an initramfs]](#Why_use_an_initramfs)
    -   [[1.3] [What makes an initramfs]](#What_makes_an_initramfs)
        -   [[1.3.1] [Filesystem structure]](#Filesystem_structure)
        -   [[1.3.2] [Userspace tools]](#Userspace_tools)
        -   [[1.3.3] [Kernel Modules]](#Kernel_Modules)
    -   [[1.4] [How to use an Initramfs]](#How_to_use_an_Initramfs)
-   [[2] [Construction]](#Construction)
    -   [[2.1] [Example List of Requirements]](#Example_List_of_Requirements)
    -   [[2.2] [Assemble and start mdadm RAID]](#Assemble_and_start_mdadm_RAID)
    -   [[2.3] [Activate Logical Volumes]](#Activate_Logical_Volumes)
    -   [[2.4] [Mount root and possibly other filesystems]](#Mount_root_and_possibly_other_filesystems)
    -   [[2.5] [Interactive Shell for Debug]](#Interactive_Shell_for_Debug)
    -   [[2.6] [Init script to control everything]](#Init_script_to_control_everything)
        -   [[2.6.1] [Elements of the Init Script]](#Elements_of_the_Init_Script)
    -   [[2.7] [Building the Binaries]](#Building_the_Binaries)
    -   [[2.8] [Putting the Pieces Together]](#Putting_the_Pieces_Together)
-   [[3] [Ideas For Further Contributions]](#Ideas_For_Further_Contributions)
-   [[4] [See also]](#See_also)

## [Introduction]

This page describes how to build an initramfs which does not contain kernel modules. That results in a component that is not tied to a specific kernel version. The original author\'s initramfs, built in April 2009 still functions.

The following example covers root in [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") on top of [mdadm](https://raid.wiki.kernel.org/index.php/A_guide_to_mdadm) raid. This is just an example, potential configuration options are limitless. [LUKS](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") could be added, and anything added as an example in this guide can be omitted.

** Important**\
This guide assumes the kernel has all required modules to mount the root filesystem built-in [\<\*\>]. If they are built as external kernel modules [\<M\>], the resulting initramfs will be kernel version dependent, which is covered in [Custom_Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs").

### [Why make your own]

The [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") can be [automatically created](https://wiki.gentoo.org/wiki/Initramfs/Guide#Creating_an_initramfs "Initramfs/Guide") with [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] and [[[sys-kernel/genkernel]](https://packages.gentoo.org/packages/sys-kernel/genkernel)[]]. While both tools are highly capable and can build functional initramfs\', they may not meet all use cases. For some users, the initramfs is worth creating manually, even if only to understand how it works, and what is happening inside.

### [Why use an initramfs]

An initramfs is typically used to assist in the boot process. Some form of initramfs is required to mount systems using [Full Disk Encryption](https://wiki.gentoo.org/wiki/Full_Disk_Encryption "Full Disk Encryption").

** Important**\
When [Secure Booting](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") a system, the initramfs should be embedded into the kernel so that it can be signed.

### [What makes an initramfs]

The initramfs is a root filesystem in a file. It is generally used to contain whatever is required to boot the system, but can contain the entire root filesystem used once booted if that\'s desired.

** Note**\
Originally the root filesystem in a file was called the initrd. The only difference between the two is the internal structure, which doesn\'t change how and why they are used.

#### [Filesystem structure]

An initramfs generally must have some basic filesystem structure, for required mounts and for the included binaries.

The following directory tree describes a basic initramfs:

[CODE] **Initramfs filesystem structure**

    /                 (located at /usr/src/initramfs)
    ├─ sys            Used for the sysfs mount.
    ├─ proc           Used for the procfs mount.
    ├─ dev            Used for the devtmpfs mount.
    ├─ run            Sometimes used by programs such as cryptsetup at runtime.
    ├─ bin            Used for standard binaries.
    ├─ sbin           Used for privileged binaries.
    ├─ lib            Used for 32 bit libraries.
    ├─ lib64          Used for 64 bit libraries.
    ├─ mnt
    │   └─root        Used as a mountpoint for the root filesystem and target for switch_root.
    ├─ etc            Mostly used for the ''fstab''.
    └─ root           Used for the root shell's homedir.

#### [Userspace tools]

Typically, an initramfs provides a filesystem with some tools which are used to assist in booting, or provide a recovery environment.

Common components include:

-   Binaries required to mount the root
    -   *btrfs-progs*
    -   cryptsetup
    -   switch_root
-   Filesystem utilities
    -   blkid
    -   mount
    -   ls
    -   cat
-   Shells
    -   sh
    -   bash

** Tip**\
Instead of manually including many small components, [Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox") can be statically compiled and included as a single file.

** Important**\
Unless the binaries are statically compiled, the required libraries must be included as well.

#### [Kernel Modules]

An initramfs may contain kernel modules, but when making a custom one, it often makes more sense to embed components required to boot into the kernel.

** Note**\
An initramfs only needs to be updated whenever the kernel is updated if it contains modules, if this is not the case, the intiramfs is kernel version agnostic.

### [How to use an Initramfs]

Follow [Custom Initramfs Packaging](https://wiki.gentoo.org/wiki/Custom_Initramfs#Packaging "Custom Initramfs") to embed the initramfs into the kernel or built it into a [CPIO](https://wiki.gentoo.org/wiki/Cpio "Cpio") archive to include via [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") or cmdline argument.

## [Construction]

** Important**\
The example in this page is just that. It will need to be adjusted to suit the individual install

### [Example List of Requirements]

-   Assemble and start mdadm RAID.
-   Activate Logical Volumes
-   Mount root and possibly other filesystems from inside their Logical Volumes
-   A filesystem checker for non root filesystem mounted in the initramfs
-   Interactive Shell for debug
-   Init script to control everything.
-   Other things to suit the install at hand

Now to discover all the binaries required to meet the explicit requirements. They must be included in the initramfs_list.

### [Assemble and start mdadm RAID]

This requires Multiple Device support built into the kernel and the mdadm user space tool.

That\'s [/sbin/mdadm] and all the libraries that it depends on

`user `[`$`]`lddtree /sbin/mdadm`

    |/sbin/mdadm (interpreter => /lib64/ld-linux-x86-64.so.2)
    |    libc.so.6 => /lib64/libc.so.6

** Tip**\
Different USE settings will produce different lists

### [Activate Logical Volumes]

This requires Multiple Device and Logical Volume Manager support built into the kernel and the lvm userspace tool.

`user `[`$`]`lddtree /sbin/lvm`

    /sbin/lvm (interpreter => /lib64/ld-linux-x86-64.so.2)
        libdevmapper-event.so.1.02 => /lib64/libdevmapper-event.so.1.02
            libdevmapper.so.1.02 => /lib64/libdevmapper.so.1.02
                libm.so.6 => /lib64/libm.so.6
        libreadline.so.8 => /lib64/libreadline.so.8
            libtinfow.so.6 => /lib64/libtinfow.so.6
        libblkid.so.1 => /lib64/libblkid.so.1
        libaio.so.1 => /lib64/libaio.so.1
        libc.so.6 => /lib64/libc.so.6

It has a bigger list of dependencies, also including [/lib64/libc.so.6]. Duplicates need only be provided once.

** Note**\
lvm2 takes USE=static, so a monolithic build can be used in the initramfs and a dynamic build used in the man install

### [Mount root and possibly other filesystems]

Most users will want to use mount by filesystem UUID. Not all filesystem are on partitions, so PARTUUID cannot be used.

Mount by filesystem UUID requires the user space mount command

`root `[`#`]`lddtree /bin/mount`

    /bin/mount (interpreter => /lib64/ld-linux-x86-64.so.2)
        libmount.so.1 => /lib64/libmount.so.1
            libblkid.so.1 => /lib64/libblkid.so.1
        libc.so.6 => /lib64/libc.so.6

### [Interactive Shell for Debug]

That will be busybox. Everyone uses busybox. Its small and has lots of utilities too.

`user `[`$`]`lddtree /bin/busybox`

    /bin/busybox (interpreter => None)

My example busybox is statically linked. That\'s a lifesaver when almost nothing works.

### [Init script to control everything]

This is the hard bit. Its all the commands that need to be entered at a root shell, using the initramfs to get started.

If the initramfs only contained busybox, what would need to be entered to boot?

Some error handing is a good idea too, so that debug is possible.

#### [Elements of the Init Script]

Its a shell script so it must start with the shebang line. Its not a comment.

    #!/bin/busybox sh

The error handler is a function which will be called when something goes wrong. It takes one parameter, which is a text string to be printed when it is invoked.

Comments are good for maintenance later.

    rescue_shell()

Parse the root filesystem out of the kernel command line and mount it.

    # allow the use of UUIDs or filesystem lables
    uuidlabel_root()

We only do that once, so it need not be a function but it makes the main flow of the script easier to read.

When things are mounted inside the initramfs, its good to be able check the filesystems first. The localmount service cannot check mounted filesystems.

    # We need this for things that are mounted before localmount runs
    # like /usr and possibly /var
    check_filesystem()

With those functions in support, we can do what\'s needed.

** Tip**\
Notice the comments to make hard coding things easier

    PATH="/sbin:/bin"
    # start for real here
    # temporarily mount proc,sys and dev
    mount -t proc proc /proc
    mount -t sysfs sysfs /sys
    mount -t devtmpfs devtmpfs /dev

    #mdam arrays to assemble
    #boot  UUID : a25b05eb:3db18cbe:afb9312b:d1d97546
    #host  UUID : de8f2cbc:17ca3275:0b69db3c:b9f91a6b
    #kvm   UUID : a3aab047:413ed52d:b15158fc:cdb637ef

    # boot
    /sbin/mdadm --assemble /dev/md0 --uuid=a25b05eb-3db18cbe-afb9312b-d1d97546 || echo "boot failed to assemble"
    /sbin/mdadm --assemble /dev/md1 --uuid=de8f2cbc-17ca3275-0b69db3c-b9f91a6b || rescue_shell "The host RAID set failed to assemble"
    /sbin/mdadm --assemble /dev/md2 --uuid=a3aab047:413ed52d:b15158fc:cdb637ef || echo "THE KVM space did not assemble"

Use `/sbin/mdadm --assemble --run` to start the raid set with missing members, if possible.

** Important**\
root in LVM on RAID on USB requires a sleep to allow USB HDD to be available before mdadm \--assemble runs

Its left as an exercise for the reader to parse the RAID UUID(s) out of the kernel command line.

If boot failed to assemble, it does not impact the boot process as both BIOS and UEFI are not raid aware. Indeed, the boot loader has to read boot to load initramfs to work out that /boot did not assemble. There is no need to call rescue_shell here.

Boot on RAID requires a RAID level and on disk RAID data layout leaves the filesystem untouched. RAID 1 and a raid metadata that lives at the end of the volume works.

Being lazy, start all the logical volumes and call the rescue shell if any one fails. In practice, only the one housing root is required. That\'s a local design decision.

    # Then start LVM
    vgchange -ay || rescue_shell "Some/All Volume Groups failed to start"

With the logical volumes started, we can see root, so mount it

    # mounting rootfs on /mnt/root - from the UUID on the kernel command line
    uuidlabel_root || rescue_shell "Error with uuidlabel_root"

Now mount other filesystems if needed. Typically /usr and /var

    # space separated list of mountpoints that ...
    mountpoints="/usr"
    # /var"
    # ... we want to find in /etc/fstab ...
    /bin/ln -s /mnt/root/etc/fstab /etc/fstab

    # loop through the list of mountpoints
    for m in $mountpoints ; do

    #echo $m

        check_filesystem $m

        echo "Mounting $m"
        # mount the device and ...
        mount $m || rescue_shell "Error while mounting $m"

        # ... move the tree to its final location
        mount --move $m "/mnt/root"$m || rescue_shell "Error while moving $m"
    done

** Tip**\
Set noauto in /etc/fstab for filesystems mounted here

    # That's put all the pieces together, now tidy up

    echo "All done. Switching to real root."

    # clean up. The init process will remount proc sys and dev later
    umount /proc
    umount /sys
    umount /dev

    # switch to the real root and execute init
    exec /sbin/switch_root /mnt/root /sbin/init

That final exec call never returns so nervous readers could add `rescue_shell "Fell off the end of init"` as the very last line.

Actually, with /proc and /dev unmounted, the console output has gone so you won\'t see it. To got any further you need the static /dev nodes created for the initrd in the real /dev before DEVTMPFS is mounted.

** Warning**\
Its a horrible script and has grown to its present state over 20 years or more

### [Building the Binaries]

To avoid using binaries from the live filesystem, the initramfs binaries will be installed in [/root/initramfs/bins]. This allows trivial changes to the init script in years to come without, tracking down all the changed dependencies on the live filesystem. Both ways work. Its a design decision.

The down side of a separate build is that all the dependencies that will not go into the initramfs will be built too.

`root `[`#`]`emerge -av --root=/root/initramfs/bins <list_of_packages>`

Set the USE flags to your liking and build your binaries. This authors preference is to build everything that supports static linking with USE=static.

\<list_of_packages\> depends on what is required of the initramfs. Like the rest of Gentoo its easy to add to if needed.

It looks a bit dated now but the bins package list on the example install is

`user `[`$`]`ls bins/var/db/pkg/*/*/*.ebuild`

    app-arch/bzip2-1.0.8-r1/bzip2-1.0.8-r1.ebuild                  sys-block/thin-provisioning-tools-0.9.0-r1/thin-provisioning-tools-0.9.0-r1.ebuild
    app-arch/gzip-1.11/gzip-1.11.ebuild                            sys-fs/e2fsprogs-1.46.4/e2fsprogs-1.46.4.ebuild
    dev-libs/expat-2.4.3/expat-2.4.3.ebuild                        sys-fs/lvm2-2.02.188-r2/lvm2-2.02.188-r2.ebuild
    dev-libs/libaio-0.3.112/libaio-0.3.112.ebuild                  sys-fs/mdadm-4.2-r1/mdadm-4.2-r1.ebuild
    dev-libs/libpcre-8.45/libpcre-8.45.ebuild                      sys-libs/e2fsprogs-libs-1.46.4-r1/e2fsprogs-libs-1.46.4-r1.ebuild
    dev-libs/libpcre2-10.39/libpcre2-10.39.ebuild                  sys-libs/glibc-2.33-r7/glibc-2.33-r7.ebuild
    dev-libs/libunistring-0.9.10-r1/libunistring-0.9.10-r1.ebuild  sys-libs/libcap-2.62/libcap-2.62.ebuild
    net-dns/libidn2-2.3.2/libidn2-2.3.2.ebuild                     sys-libs/libxcrypt-4.4.25-r1/libxcrypt-4.4.25-r1.ebuild
    sys-apps/acl-2.3.1/acl-2.3.1.ebuild                            sys-libs/ncurses-6.2_p20210619/ncurses-6.2_p20210619.ebuild
    sys-apps/attr-2.5.1/attr-2.5.1.ebuild                          sys-libs/pam-1.5.1_p20210622-r1/pam-1.5.1_p20210622-r1.ebuild
    sys-apps/baselayout-2.7-r3/baselayout-2.7-r3.ebuild            sys-libs/readline-8.1_p1-r1/readline-8.1_p1-r1.ebuild
    sys-apps/busybox-1.34.1/busybox-1.34.1.ebuild                  sys-libs/timezone-data-2021a-r1/timezone-data-2021a-r1.ebuild
    sys-apps/gentoo-functions-0.14/gentoo-functions-0.14.ebuild    sys-libs/zlib-1.2.11-r4/zlib-1.2.11-r4.ebuild
    sys-apps/grep-3.7/grep-3.7.ebuild                              virtual/awk-1/awk-1.ebuild
    sys-apps/systemd-tmpfiles-249.9/systemd-tmpfiles-249.9.ebuild  virtual/libcrypt-2/libcrypt-2.ebuild
    sys-apps/util-linux-2.37.2-r1/util-linux-2.37.2-r1.ebuild      virtual/libiconv-0-r2/libiconv-0-r2.ebuild
    sys-auth/pambase-20210201.1/pambase-20210201.1.ebuild          virtual/libintl-0-r2/libintl-0-r2.ebuild
    sys-auth/passwdqc-2.0.2-r1/passwdqc-2.0.2-r1.ebuild            virtual/tmpfiles-0-r1/tmpfiles-0-r1.ebuild

### [Putting the Pieces Together]

Thats what the initramfs_list file is for.

** Important**\
All the files discovered to be required during design, using lddtree, must be included

Describe the directory structure for the initramfs this example is from an arm64 system. amd64/x86 may differ.

    # directory structure
    dir /proc   755 0 0
    dir /usr        755 0 0
    dir /bin        755 0 0
    dir /sys        755 0 0
    dir /var        755 0 0
    #dir /lib        755 0 0
    dir /lib64  755 0 0
    dir /sbin   755 0 0
    dir /mnt        755 0 0
    dir /mnt/root   755 0 0
    dir /etc        755 0 0
    dir /root   700 0 0
    dir /dev        755 0 0

Make a few critical device nodes

    nod /dev/null   666 0 0 c 1 3
    nod /dev/tty    666 0 0 c 5 0
    nod /dev/console        600 0 0 c 5 1

They are probably not required with modern DEVTMPFS in the kernel. The last line (nod /dev/console) is always required when building an embedded initramfs (even if DEVTMPFS is used).

All the main commands

    # busybox
    # Output file name              Input file name
    file /bin/busybox               /root/initramfs/bins/bin/busybox        755 0 0
    # Need real mount as busybox did not support UUID
    file /bin/mount                 /root/initramfs/bins/bin/mount          755 0 0

    # for raid on lvm
    # Output file name              Input file name
    file /sbin/mdadm                /root/initramfs/bins/sbin/mdadm         755 0 0
    file /sbin/lvm.static           /root/initramfs/bins/sbin/lvm.static    755 0 0

Add some symbolic links to make life easier.

    slink /sbin/vgchange                    /sbin/lvm.static                777 0 0
    slink /sbin/vgscan                      /sbin/lvm.static                777 0 0

    slink /bin/cat                          /bin/busybox                    777 0 0
    slink /bin/cut                          /bin/busybox                    777 0 0
    slink /bin/findfs                       /bin/busybox                    777 0 0
    slink /bin/ln                           /bin/busybox                    777 0 0
    slink /sbin/switch_root                 /bin/busybox                    777 0 0

    slink /lib64/libdl.so.2                 /lib64/libdl-2.33.so            777 0 0

    # libraries required by /sbin/fsck.ext4 and /sbin/fsck
    # The /lib -> /lib64 symlink is mostly harmless but its not right on arm64
    slink   /lib                            /lib64                          777 0 0

The symlinks to /bin/busybox are probably not required as busybox assumes internal commands when a command is not found.

    # libraries required by /sbin/fsck.ext4 and /sbin/fsck
    # The /lib -> /lib64 symlink is mostly harmless but its not right on arm64
    slink   /lib                            /lib64                          777 0 0

All the required libraries too

    # Output file name                      Input file name
    file    /lib/ld-linux-aarch64.so.1  /root/initramfs/bins/lib/ld-linux-aarch64.so.1      755 0 0
    file    /lib64/libext2fs.so.2           /root/initramfs/bins/lib64/libext2fs.so.2           755 0 0
    file    /lib64/libcom_err.so.2          /root/initramfs/bins/lib64/libcom_err.so.2          755 0 0
    file    /lib64/libpthread.so.0          /root/initramfs/bins/lib64/libpthread.so.0          755 0 0
    file    /lib64/libblkid.so.1            /root/initramfs/bins/lib64/libblkid.so.1            755 0 0
    file    /lib64/libuuid.so.1             /root/initramfs/bins/lib64/libuuid.so.1             755 0 0
    file    /lib64/libe2p.so.2              /root/initramfs/bins/lib64/libe2p.so.2              755 0 0
    file    /lib64/libc.so.6                /root/initramfs/bins/lib64/libc.so.6                755 0 0
    file    /lib64/libmount.so.1            /root/initramfs/bins/lib64/libmount.so.1            755 0 0
    file    /lib64/libdl-2.33.so            /root/initramfs/bins/lib64/libdl-2.33.so            755 0 0

    file    /sbin/fsck              /root/initramfs/bins/sbin/fsck                      755 0 0
    file    /sbin/fsck.ext4         /root/initramfs/bins/sbin/fsck.ext4                 755 0 0

    # our init script
    file    /init                   /root/initramfs/init               755 0 0

** Warning**\
This example works with ext4. Choose your `/sbin/fsck.fs_type`

Mount /boot if its not mounted.

`root `[`#`]`/usr/src/linux/usr/gen_init_cpio /root/initramfs/initramfs_list > /boot/<initramfs_name>`

Tell your boot loader about [/boot/\<initramfs_name\>] and reboot to test.

## [Ideas For Further Contributions]

-   Cover LUKS
-   Cover root over NFS (Possible without an initlamfs too)
-   Bring up the network in the initramfs with ssh access
-   Other things

** Warning**\
Networking in the initramfs is a security risk. The initramfs will need to be maintained

## [See also]

-   [Initramfs/Guide](https://wiki.gentoo.org/wiki/Initramfs/Guide "Initramfs/Guide") --- covers the concepts of the initramfs as well as how to properly create and manage initramfs instances.