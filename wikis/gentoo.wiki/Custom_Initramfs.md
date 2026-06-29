[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**initramfs** is a root filesystem that is embedded into the kernel and loaded at an early stage of the boot process. It is the successor of *initrd*. It provides early userspace which can do things the kernel can\'t easily do by itself during the boot process.

Using *initramfs* is optional. By default, the kernel initializes hardware using built-in drivers, mounts the specified root partition, and loads the [init system](https://wiki.gentoo.org/wiki/Init_system "Init system") of the installed Linux distribution. The init system then loads additional modules and starts services until it eventually presents a log in dialog. This is a good default behavior and sufficient for many users. *initramfs* is for users with advanced requirements; for users who need to do things as early as possible, even before the root partition is mounted.

Typically, an *initramfs* is not needed, but may be necessary for:

-   Mounting an encrypted, logical, or otherwise special root partition
-   Providing a minimalistic rescue shell (if something goes wrong)
-   Customize the boot process (e.g., print a welcome message)
-   Load modules necessary to boot (e.g., third party storage drivers)
-   Anything the kernel can\'t do that\'s usually handled in user space

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Basics]](#Basics)
    -   [[2.1] [Directory structure]](#Directory_structure)
        -   [[2.1.1] [Device nodes]](#Device_nodes)
    -   [[2.2] [Applications]](#Applications)
        -   [[2.2.1] [Busybox]](#Busybox)
    -   [[2.3] [Init]](#Init)
    -   [[2.4] [Packaging]](#Packaging)
        -   [[2.4.1] [Kernel configuration]](#Kernel_configuration)
        -   [[2.4.2] [Embedding into the Kernel]](#Embedding_into_the_Kernel)
        -   [[2.4.3] [Creating a separate file]](#Creating_a_separate_file)
            -   [[2.4.3.1] [Using GRUB]](#Using_GRUB)
        -   [[2.4.4] [External file list]](#External_file_list)
    -   [[2.5] [Finalizing]](#Finalizing)
-   [[3] [Functionality]](#Functionality)
    -   [[3.1] [Rescue shell]](#Rescue_shell)
        -   [[3.1.1] [Force entry into the rescue shell]](#Force_entry_into_the_rescue_shell)
    -   [[3.2] [Dynamic devices]](#Dynamic_devices)
        -   [[3.2.1] [devtmpfs]](#devtmpfs)
        -   [[3.2.2] [mdev]](#mdev)
    -   [[3.3] [Mount by UUID or label]](#Mount_by_UUID_or_label)
        -   [[3.3.1] [Kernel parameters]](#Kernel_parameters)
    -   [[3.4] [LVM]](#LVM)
    -   [[3.5] [Software RAID]](#Software_RAID)
        -   [[3.5.1] [mdadm]](#mdadm)
    -   [[3.6] [DM-Crypt]](#DM-Crypt)
        -   [[3.6.1] [Encrypted keyfile]](#Encrypted_keyfile)
    -   [[3.7] [Networking]](#Networking)
        -   [[3.7.1] [Static IP]](#Static_IP)
        -   [[3.7.2] [DHCP]](#DHCP)
        -   [[3.7.3] [DNS]](#DNS)
    -   [[3.8] [Custom keyboard layout]](#Custom_keyboard_layout)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Static vs. dynamic binaries]](#Static_vs._dynamic_binaries)
        -   [[4.1.1] [lddtree]](#lddtree)
    -   [[4.2] [Kernel panics]](#Kernel_panics)
    -   [[4.3] [Job control]](#Job_control)
    -   [[4.4] [Salvaging]](#Salvaging)
        -   [[4.4.1] [Dismantling the Kernel]](#Dismantling_the_Kernel)
        -   [[4.4.2] [Extracting the cpio archive]](#Extracting_the_cpio_archive)
    -   [[4.5] [Integrated initramfs does not always update]](#Integrated_initramfs_does_not_always_update)
    -   [[4.6] [Command not found]](#Command_not_found)
    -   [[4.7] [Disappearing root]](#Disappearing_root)
    -   [[4.8] [Variations for switch_root]](#Variations_for_switch_root)
-   [[5] [Examples]](#Examples)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Prerequisites]

There are countless ways to make an *initramfs*. An *initramfs* need not be manually created. There are tools such as [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") or [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") that can do the work. With a bit of luck, one of them might work out of the box for the required use-case, and the user need not bother with how *initramfs* works and what it does. If none of these tools can do the job automatically, their functionality may have to be extended manually, or an *initramfs* may need to be \"hand made\".

An *initramfs* contains at *least* one file called [[**/init**]]. This file is executed by the kernel as the main init process (PID 1). It has to do all the work. In addition, there can be any number of additional files and directories that are required by [[**/init**]]. They are usually files often found on any other root filesystem, such as [/dev] for device nodes, [/proc] for kernel information, [/bin] for binaries, and so on. The structure of an *initramfs* can be simple, or it can be complicated, depending on use-case requirements.

When the kernel mounts the *initramfs*, the target root partition is not yet mounted, so it can\'t access any of the files there. That means there is nothing but the *initramfs*. So everything required must be included in the *initramfs*. If a shell is required, it must be included in the *initramfs*. To be able to mount something, a mount utility must be included. To load a module, the *initramfs* has to provide both the module, as well as a utility to load it. If the utility depends on libraries in order to work, the libraries must be included as well. This seems complicated, and it is, because the *initramfs* has to function independently.

## [Basics]

This section will show the *easy and straightforward way to initramfs creation*, to make a functional - albeit minimalistic - *initramfs* which then can extend according to the use-case.

### [Directory structure]

Create a basic *initramfs* directory structure that will later become the *initramfs* root. For consistency work in [/usr/src/initramfs], but any location would do. Adapt accordingly.

`root `[`#`]`mkdir --parents /usr/src/initramfs/ `

#### [Device nodes]

Most things the *initramfs* does will require a couple of device nodes to be present, especially the device for the root partition. Throughout this document, [/dev/sda1] will be used as example device. Copy basic device nodes from the root filesystem to the *initramfs* example location:

`root `[`#`]`cp --archive /dev/ /usr/src/initramfs/dev/`

Which devices are needed depends entirely on what the system is going to use *initramfs* for. Please adapt to the system needs.

** Note**\
More advanced approaches to device nodes are covered in the [Dynamic devices](#Dynamic_devices) section.

### [Applications]

Any binary needed to execute at boot needs to be copied into the *initramfs* layout. Make sure to also copy any libraries that the binaries require. To see what libraries any particular binary requires, use the [ldd] tool. For example, the [[[dev-util/strace]](https://packages.gentoo.org/packages/dev-util/strace)[]] binary requires:

`user `[`$`]`ldd /usr/bin/strace`

        linux-vdso.so.1 (0x00007fff271ff000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f5b954fe000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f5b958a9000)

This shows that for [/usr/bin/strace] to work in the *initramfs*, the following must be done:

-   [/usr/bin/strace] must be copied to [/usr/src/initramfs/bin]
-   [/lib64/libc.so.6] must be copied to [/usr/src/initramfs/lib64]
-   [/lib64/ld-linux-x86-64.so.2] must be copied to [/usr/src/initramfs/lib64]

The exception is [linux-vdso.so.1] which is provided by the kernel. It does not need to be copied to the *initramfs*.

Some applications might depend on other files and libraries to work. For example, [[[app-editors/nano]](https://packages.gentoo.org/packages/app-editors/nano)[]] needs a terminfo file [/usr/share/terminfo/l/linux] from [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]], so copy it to the *initramfs* as well. To find these dependencies, tools like [equery] and [strace] prove to be most helpful.

#### [Busybox]

Instead of collecting countless utilities and libraries (and never seeing the end of it), just use [busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox"). It\'s a set of utilities for rescue and embedded systems, it contains a shell, utilities like [ls], [mkdir], [cp], [mount], [insmod], and many more - all in a single binary called [/bin/busybox]. For [busybox] to work properly in a *initramfs*, emerge it with the `static` USE flag enabled, then copy the [/bin/busybox] binary into the *initramfs* layout as [/usr/src/initramfs/bin/busybox]:

Set the useflags `static` and `-pam` to /etc/portage/package.use/busybox

`root `[`#`]`nano /etc/portage/package.use/busybox`

[FILE] **`/etc/portage/package.use/busybox`busybox**

    sys-apps/busybox static -pam

`root `[`#`]`emerge --ask --verbose sys-apps/busybox `

`root `[`#`]`cp --archive /bin/busybox /usr/src/initramfs/bin/busybox `

** Note**\
Use [ldd] to verify that the binary is static.

### [Init]

The file structure of the *initramfs* is almost complete. The only thing that is missing is [[**/init**]] itself, the executable in the root of the *initramfs* that is executed by the kernel. Because [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]] includes a fully functional shell, this means that the [[**/init**]] binary can be written as a simple shell script (instead of making it a complicated application written in Assembler or C that needs to compile).

The following example shows a minimalistic shell script, based on the [busybox] shell:

[FILE] **`/usr/src/initramfs/init`minimalistic /init example**

    #!/bin/busybox sh

    # Mount the /proc and /sys filesystems.
    mount -t proc none /proc
    mount -t sysfs none /sys

    # Do your stuff here.
    echo "This script just mounts and boots the rootfs, nothing else!"

    # Mount the root filesystem.
    mount -o ro /dev/sda1 /mnt/root

    # Clean up.
    umount /proc
    umount /sys

    # Boot the real thing.
    exec switch_root /mnt/root /sbin/init

This example needs some device nodes to work, mainly the root block device. Change the script and copy the corresponding [/dev/] node to fit the system needs.

Don\'t forget to make the [[**/init**]] file executable:

`root `[`#`]`chmod +x /usr/src/initramfs/init`

### [Packaging]

An *initramfs* directory can be packed into a [CPIO](https://wiki.gentoo.org/wiki/Cpio "Cpio") archive, optionally with compression, or it can be built directly into the kernel itself.

When built as a separate image, it must be loaded by the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") or with the *initrd=* arg in the kernel commandline.

** Tip**\
Embedding the initramfs into the kernel can make bootloader configuration, [EFI Stub booting](https://wiki.gentoo.org/wiki/EFI_Stub "EFI Stub"), and [Secure Booting](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") easier.

#### [Kernel configuration]

With either method, there is a need to enable Initial RAM filesystem and RAM disk (initramfs/initrd) support.

[KERNEL] **CONFIG_BLK_DEV_INITRD=y**

    General setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support

** Warning**\
Also enable all drivers, filesystems, compression methods and other settings that are required for booting and accessing the root partition. If selecting such drivers as modules, the module files must be collected and integrated into the *initramfs* and loaded in [[**/init**]]. Generally this means *a lot* of unnecessary extra work, so just use built-in drivers.

#### [Embedding into the Kernel]

To embed the *initramfs* directly into the kernel image, set `CONFIG_INITRAMFS_SOURCE` to the root of the *initramfs* directory, (e.g. [/usr/src/initramfs]):

[KERNEL] **CONFIG_INITRAMFS_SOURCE=\"/usr/src/initramfs\"**

    General setup  --->
        (/usr/src/initramfs) Initramfs source file(s)

On compilation, the kernel will automatically collect the files into a cpio archive and embed it into the kernel image. The kernel will have to be rebuilt any time a change is made to the *initramfs* directory.

** Tip**\
`CONFIG_INITRAMFS_SOURCE` can be pointed to a .cpio file, though this is usually needless trouble.

If the kernel is compressed, which by default it is with gzip, disabling compression for the embedded initramfs achieves smaller kernel filesizes and faster startups. This happens because when the kernel as a whole is compressed, elements of the initram shared with the kernel can be deduplicated. It is more performant because it skips the second stage of decompression of the initram.

[KERNEL] **CONFIG_INITRAMFS_COMPRESSION_NONE=y**

    General setup  --->
        Built-in initramfs compression mode (None)  --->
            ( ) LZMA
            ( ) XZ
            ( ) LZO
            ( ) LZ4
            ( ) ZSTD
            (X) None

#### [Creating a separate file]

To use a standalone archive file, adjust the kernel settings accordingly:

[KERNEL] **Support inital ramdisk/ramfs compressed using \<compression_method\>**

    General setup  --->
        () Initramfs source file(s)
        [*]   Support initial ramdisk/ramfs compressed using gzip
        [ ]   Support initial ramdisk/ramfs compressed using bzip2
        [ ]   Support initial ramdisk/ramfs compressed using LZMA
        [ ]   Support initial ramdisk/ramfs compressed using XZ
        [ ]   Support initial ramdisk/ramfs compressed using LZO
        [ ]   Support initial ramdisk/ramfs compressed using LZ4

For this example [gzip] is sufficient.

** Warning**\
Not supporting the compression method of a loaded *initramfs* archive **will** cause a **kernel panic** when booting!

Create a standalone archive file by running the following commands:

`root `[`#`]`cd /usr/src/initramfs `

`root `[`#`]`find . -print0 | cpio --null --create --verbose --format=newc | gzip --best > /boot/custom-initramfs.cpio.gz `

This will create a file called [custom-initramfs.cpio.gz] in [/boot]. Now instruct the bootloader to load this file along with the kernel.

** Note**\
The [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") also provides [/usr/src/linux/usr/gen_init_cpio], which is used when embedding the *initramfs* and can also build the cpio archive.

##### [Using GRUB]

In case of GRUB, do this with the **initrd** line:

[FILE] **`/boot/grub/grub.cfg`GRUB initrd example**

    linux 3.12.6-gentoo
    initrd custom-initramfs.cpio.gz

** Warning**\
If unfamiliar with bootloader configuration, please refer to [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB").

In order to make this usable with [grub-mkconfig], the filename [custom-initramfs.cpio.gz] must be included in the GRUB helper scripts:

[FILE] **`/etc/grub.d/10_linux`grub-mkconfig helper script**

    [...]
    initrd_real=
    for i in "initrd.img-$" "initrd-$.img" "initrd-$.gz" "custom-initramfs.cpio.gz" \
         "initrd-$" "initramfs-$.img" \
    [...]

[FILE] **`/etc/grub.d/10_linux_xen`grub-mkconfig helper script**

    [...]
    initrd_real=
    for i in "initrd.img-$" "initrd-$.img" "initrd-$.gz" "custom-initramfs.cpio.gz" \
       "initrd-$" "initramfs-$.img" \
    [...]

** Note**\
It is also possible to use the variable `$` for the filename in the helper script. This means that the file itself has to be renamed as well. The variable content corresponds to the output of [uname \--kernel-release].

After applying the changes, the file will be recognized running [grub-mkconfig]; the output may look like the following:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-4.14.83-gentoo
    Found initrd image: /boot/custom-initramfs.cpio.gz
    done

#### [External file list]

An external file list, or cpio list, describes files to be included into the *initramfs*. This file list is processed by an utility that comes with the Linux kernel, [usr/gen_init_cpio]. It can be used for both embedded and standalone *initramfs*, either by using it as [INITRAMFS_SOURCE] directly or by running the utility from a shell. This lets the *initramfs* be built dynamically, always using the latest files from the system, but compared to populating a real directory [/usr/src/initramfs], it is less intuitive and requires more knowledge in regards to *device nodes* and such. The command [file] will prove as very useful to get information from special *block* or *character* devices.

** Warning**\
This method is for advanced users. Skip this section, if not comfortable with the next steps.

A minimalistic list may look like so:

[FILE] **`/usr/src/initramfs.list`cpio list example**

    # Custom Initramfs minimal example
    dir /dev 0755 0 0
    file /init /usr/src/initramfs/init 0755 0 0

Create the cpio archive, compress it, and move it to [/boot]:

`root `[`#`]` cd /usr/src/linux `

`root `[`#`]` usr/gen_init_cpio ../initramfs.list > ../initramfs.cpio `

`root `[`#`]` gzip --best ../initramfs.cpio `

`root `[`#`]` mv ../initramfs.cpio.gz /boot `

After that update the bootloader entries!

Instead of creating the list manually, the cpio list and archive can be generated by two tools that are provided by the kernel source files. They may need to be compiled first (this is documented [here](https://wiki.gentoo.org/wiki/Early_Userspace_Mounting#Requirements "Early Userspace Mounting")).

`root `[`#`]`/usr/src/linux/usr/gen_initramfs.sh -h`

    Usage:
    /usr/src/linux/usr/gen_initramfs_list.sh [-o <file>] [-u <uid>] [-g <gid>]  ...
            -o <file>      Create compressed initramfs file named <file> using
                           gen_init_cpio and compressor depending on the extension
            -u <uid>       User ID to map to user ID 0 (root).
                           <uid> is only meaningful if <cpio_source> is a
                           directory.  "squash" forces all files to uid 0.
            -g <gid>       Group ID to map to group ID 0 (root).
                           <gid> is only meaningful if <cpio_source> is a
                           directory.  "squash" forces all files to gid 0.
            <cpio_source>  File list or directory for cpio archive.
                           If <cpio_source> is a .cpio file it will be used
                           as direct input to initramfs.
            -d             Output the default cpio list.

    All options except -o and -l may be repeated and are interpreted
    sequentially and immediately.  -u and -g states are preserved across
    <cpio_source> options so an explicit "-u 0 -g 0" is required
    to reset the root/group mapping.

Using the previously created directory structure in [/usr/src/initramfs], it may be executed as follows:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`usr/gen_initramfs.sh -o ../custom-initramfs.cpio /usr/src/initramfs `

`root `[`#`]`ls -l .. `

    total 1656
    -rw-r--r--  1 root root 1675784 Dec  9 03:12 custom-initramfs.cpio
    drwxr-xr-x 12 root root    4096 Dec  9 00:16 initramfs
    lrwxrwxrwx  1 root root      20 Nov 23 19:12 linux -> linux-4.14.83-gentoo
    drwxr-xr-x 26 root root    4096 Dec  9 00:58 linux-4.14.83-gentoo
    -rw-r--r--  1 root root    4830 Dec  9 01:07 README

The script creates a cpio list by analyzing all directories and files within [/usr/src/initramfs]. It then executes [usr/gen_init_cpio] to generate the cpio archive file.

** Note**\
The current working directory must be [/usr/src/linux], since the shell script uses the relative path [usr/gen_init_cpio].

After that, compress the [cpio archive] via [gzip]:

`root `[`#`]`gzip /usr/src/custom-initramfs.cpio`

This creates the archive [/usr/src/custom-initramfs.cpio.gz].

All steps can be done manually to make the process clearer:

`root `[`#`]`usr/gen_initramfs.sh /usr/src/initramfs | tee ../initramfs.list `

    #####################
    # /usr/src/initramfs
    # Last modified: 1544312413.9519881540

    dir /bin 755 0 0
    file /bin/busybox /usr/src/initramfs/bin/busybox 755 0 0
    dir /dev 755 0 0
    nod /dev/console 600 0 0 c 5 1
    nod /dev/null 666 0 0 c 1 3
    nod /dev/sda1 660 0 6 b 8 1
    nod /dev/tty 666 0 5 c 5 0
    dir /etc 755 0 0
    file /init /usr/src/initramfs/init 744 0 0
    dir /lib64 755 0 0
    dir /lib 755 0 0
    dir /mnt 755 0 0
    dir /mnt/root 755 0 0
    dir /proc 755 0 0
    dir /root 700 0 0
    dir /sbin 755 0 0
    dir /sys 755 0 0

`root `[`#`]`usr/gen_init_cpio ../initramfs.list > ../initramfs.cpio `

`root `[`#`]`gzip --best ../initramfs.cpio `

`root `[`#`]`ls -l .. `

    total 1660
    drwxr-xr-x 12 root root    4096 Dec  9 00:16 initramfs
    -rw-r--r--  1 root root 1675800 Dec  9 03:44 initramfs.cpio.gz
    -rw-r--r--  1 root root     593 Dec  9 03:31 initramfs.list
    lrwxrwxrwx  1 root root      20 Nov 23 19:12 linux -> linux-4.14.83-gentoo
    drwxr-xr-x 26 root root    4096 Dec  9 00:58 linux-4.14.83-gentoo
    -rw-r--r--  1 root root    4830 Dec  9 01:07 README

The file [initramfs.cpio.gz] can now be moved to [/boot].

`root `[`#`]`mv ../initramfs.cpio.gz /boot`

** Warning**\
Do not forget to update the bootloader entries afterwards!

** Note**\
In order to always have the latest binaries etc. in the initramfs, it is possible to write a shell script^[\[1\]](#cite_note-1)^ which copies the files and calls the above tools. Hardlinks do not work, as the inode will change when the original file gets overwritten, whereas the hardlink points to the old inode. Symbolic links do not work, as they will be recognised as *slink* and not as *file* when using [gen_initramfs.sh]; this will render the initramfs **unusable**.\
Remember: Be **absolutely** sure that binaries on the system are either compiled statically or have the needed libraries! Package-based USE flags can be set in [/etc/portage/package.use].

### [Finalizing]

** Tip**\
Testing an initramfs directory by chrooting into the directory and targeting the *init* script is not a perfect test, but can be useful.

Now reboot the machine. On boot, the kernel will extract the files from the *initramfs* archive automatically and execute the [[**/init**]] script, which in turn should then take care of mounting of the root partition and execute the init system of the installed Linux distribution.

## [Functionality]

The following sections describe how to extend the [[**/init**]] script with more advanced functionality.

### [Rescue shell]

To be dropped to a rescue shell if an error occurs, add the following function to [[**/init**]] and call it when something goes wrong.

[FILE] **`/usr/src/initramfs/init`Rescue shell functionality**

    rescue_shell()

In the example below, the [rescue_shell] will be executed if the root partition fails to mount:

[FILE] **`/usr/src/initramfs/init`Invoking the rescue shell**

    mount -o ro /dev/sda1 /mnt/root || rescue_shell

#### [Force entry into the rescue shell]

Occasionally, it might be useful to be able to interrupt the boot process and enter the rescue shell. For example, it\'s useful for root password (or PAM configuration) recovery or for [[**/init**]] debugging itself.

A standard way of doing this is by passing `rdinit=/bin/sh` or `rdinit=/bin/bb` kernel command line option. However, this is a rarely known option. It also requires /bin/sh or /bin/bb symlinks/files to be built into initramfs instead of being installed at runtime with `busybox install -s`. It\'s possible to call it like `rdinit="/bin/busybox sh"` but this is even more obscure.

For convenience, it might be useful to implement Dracut-inspired `rd.break` option used for a similar purpose (legacy name was `rdbreak`). Similarly, it\'s possible to handle more widely known `init=/bin/sh` option in the same manner.

[FILE] **`/usr/src/initramfs/init`Option to drop to the rescue shell**

    break_requested() "
    }

    if [[ -n "$(break_requested)" ]] ; then
        rescue_shell
    fi

    umount /proc
    umount /sys
    umount /dev

    exec switch_root /newroot /sbin/init

### [Dynamic devices]

For populating [/dev] dynamically, use either devtmpfs or mdev. Please note that the kernel can take some time detecting devices (such as external USB drives), so a [sleep] statement may need to be added to the script.

#### [devtmpfs]

Provided by the kernel, devtmpfs is designed to offer device nodes during early boot.

[KERNEL] **CONFIG_DEVTMPFS=y**

    Device Drivers  --->
        Generic Driver Options  --->
            [*] Maintain a devtmpfs filesystem to mount at /dev

Include the following snippet in the [[**/init**]] script to have it mount at boot:

[FILE] **`/usr/src/initramfs/init`mount devtmpfs**

    mount -t devtmpfs none /dev

Don\'t forget to unmount it again in the cleanup phase of the script:

[FILE] **`/usr/src/initramfs/init`umount devtmpfs**

    umount /dev

#### [mdev]

Although devtmpfs is the preferred solution today, alternatively use mdev, the udev replacement of [busybox].

[KERNEL] **CONFIG_UEVENT_HELPER=y**

    Device Drivers  --->
        Generic Driver Options  --->
            [*] Support for uevent helper

For mdev to work, make [/sbin/mdev] a symlink to [/bin/busybox] in the *initramfs*.

`root `[`#`]`ln --symbolic ../bin/busybox /usr/src/initramfs/sbin/mdev`

Then add the following snippet to [[**/init**]], after mounting [/proc] and [/sys]:

[FILE] **`/usr/src/initramfs/init`Adding mdev support to /init**

    echo /sbin/mdev > /proc/sys/kernel/hotplug
    mdev -s

### [Mount by UUID or label]

With [Dynamic devices](#Dynamic_devices) enabled, it may be preferable to use UUID or label to mount the root partition instead of using a static device name. For that purpose, [busybox] comes with a utility called [findfs].

[FILE] **`/usr/src/initramfs/init`mount using findfs**

    mount -o ro $(findfs UUID=845b2454-42a3-19ef-6ec5-238a358c365b) /mnt/root
    # or
    mount -o ro $(findfs LABEL=myroot) /mnt/root

Doing it this way is simple, but it means that the UUID or label is hardcoded in the [[**/init**]]. Alternatively, see [Kernel parameters](#Kernel_parameters).

#### [Kernel parameters]

Using kernel parameters instead of hardcoding device names or UUIDs, there will be a need to parse [/proc/cmdline]. There are many ways to do so, the following method is just an example to give the general idea. It uses string manipulation of the shell and only supports `key=value` parameters. Add the following function to [[**/init**]] and call it whenever kernel parameter is needed.

[FILE] **`/usr/src/initramfs/init`Adding a simple cmdline parser function**

    cmdline() =}"
        value="$"
        [ "$" != "" ] && echo "$"
    }

The function is called with the name of the kernel parameter in question. In the example below, it uses the root parameter to mount the root partition:

[FILE] **`/usr/src/initramfs/init`Mount rootfs by cmdline**

    mount -o ro $(findfs $(cmdline root)) /mnt/root

It works for both `root=/dev/sda1` and `root=UUID=845b2454` but will fail when the parameter is missing.

### [LVM]

If the root partition is located on a logical volume, include the [LVM](https://wiki.gentoo.org/wiki/LVM#Using_LVM_in_an_initramfs "LVM") binary in the *initramfs*. Get a static binary by enabling the `static` USE flag for [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]]. Copy it to the *initramfs* [/sbin] directory.

** Note**\
The static LVM binary may also be called [/sbin/lvm.static]. Use [ldd] to verify that the binary is static.

`root `[`#`]`cp --archive /sbin/lvm /usr/src/initramfs/sbin/lvm`

Now, enable the LVM root partition in [[**/init**]]. This example assumes that the volume group is called **VG**, and the root volume is called **root**. Replace them with the names the system used when creating the volume.

[FILE] **`/usr/src/initramfs/init`Setting up the root volume**

    lvm vgscan --mknodes # creates /dev/mapper/control
    lvm lvchange -a y VG/root
    lvm vgscan --mknodes # creates /dev/mapper/VG-root and /dev/VG/root

The root partition may then be called [/dev/VG/root] or [/dev/mapper/VG-root].

** Note**\
Calling [vgscan] is optional, but recommended, just in case device nodes are missing.

Recent versions of [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] rely on [[[sys-fs/udev]](https://packages.gentoo.org/packages/sys-fs/udev)[]] to create the named LV device nodes, but there is no udev in a simple *initramfs*. The following choices are available:

-   Use [vgscan] as shown above (simplest solution)
-   [Mount by UUID or label](#Mount_by_UUID_or_label) instead of using [/dev/VG/root]. It works because [findfs] is happy with just [/dev/dm-42]
-   Build a LVM binary with the `-udev` USE flag (specifically for the *initramfs* only!)
-   Disable udev dependency by including a minimal [/etc/lvm/lvm.conf] in the *initramfs*:

[FILE] **`/usr/src/initramfs/etc/lvm/lvm.conf`Disable udev in lvm.conf**

    devices
    activation

### [Software RAID]

Normally the Linux kernel will automatically scan for any \"Linux raid autodetect\" partitions and start as many software RAIDs as it can find. But if using an *initramfs*, the kernel will not automatically scan for RAIDs until it is told to. In the following example instructs the kernel to scan for software RAIDs and start as many as it can find. This will actually start all autodetected arrays, not just [/dev/md0]:

[FILE] **`/usr/src/initramfs/init`Adding RAID autodetect support to /init**

    raidautorun /dev/md0

** Note**\
[\"Linux raid autodetect\"](https://raid.wiki.kernel.org/index.php/RAID_superblock_formats#A_Note_about_kernel_autodetection_of_different_superblock_formats) won\'t work for any recent setups, unless specifically set up with partitions of type \"fd\" and used 0.90 metadata for the Software RAID.

#### [mdadm]

Without \"Linux raid autodetect\" partitions, or if an advanced RAID setup is required, include [**mdadm**] in the *initramfs*. A static binary may be made by enabling the `static` USE flag for [[[sys-fs/mdadm]](https://packages.gentoo.org/packages/sys-fs/mdadm)[]].

Copy the binary [/sbin/mdadm] and [/etc/mdadm.conf] into the *initramfs*:

`root `[`#`]`cp --archive /sbin/mdadm /usr/src/initramfs/sbin `

`root `[`#`]`cp --archive /etc/mdadm.conf /usr/src/initramfs/etc `

** Note**\
Use [mdadm \--detail \--scan] if there is not yet a [mdadm.conf].

Edit the [mdadm.conf] in the *initramfs* as required. An example [mdadm.conf] follows:

[FILE] **`/usr/src/initramfs/etc/mdadm.conf`mdadm.conf example**

    DEVICE /dev/sd?*
    ARRAY /dev/md0 UUID=627125a5:abce6b82:6c738e49:50adadae

This [mdadm.conf] will scan all [/dev/sd?\*] devices and assemble the RAID device fitting the UUID 627125a5:abce6b82:6c738e49:50adadae.

** Note**\
If [mdadm.conf] has additional conditions such as metadata and name, it may be more practical to remove them. The UUID alone should be sufficient.

Now Software RAID can be initialized in [[**/init**]]:

[FILE] **`/usr/src/initramfs/init`Assemble software RAIDs with mdadm**

    mdadm --assemble --scan

With this, the root partition [/dev/md0] should be able to be mounted.

### [DM-Crypt]

If the root partition is LUKS encrypted, include the cryptsetup binary in the *initramfs*. A static binary may be made by setting the `static` USE flag for [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]]. Copy it to the *initramfs* [/sbin] directory. Since cryptsetup also often requires the use of the kernel\'s random device, include them as well.

** Note**\
If having problems getting a static cryptsetup binary, try `nettle` or `kernel` instead of the default `gcrypt` USE flag. The `udev` USE flag may also need to be disabled for both cryptsetup and its dependencies.

Recompile the package [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] with the new USE flags. For example:

`root `[`#`]`USE="-gcrypt nettle static" emerge --ask --verbose sys-fs/cryptsetup `

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild   R    ] sys-fs/cryptsetup-1.7.5-r1::gentoo  USE="nettle* nls static* udev -gcrypt* -kernel -libressl -openssl -pwquality -python -reencrypt -static-libs -urandom" PYTHON_TARGETS="python2_7 python3_6 -python3_4 -python3_5 (-python3_7)" 0 KiB

    Total: 1 package (1 reinstall), Size of downloads: 0 KiB

    Would you like to merge these packages? [Yes/No]

It might also be needed to compile the package [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]] with the `static-libs` USE flag:

`root `[`#`]`USE="static-libs" emerge --ask --verbose sys-fs/lvm2 `

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild  N     ] sys-devel/autoconf-archive-2018.03.13::gentoo  635 KiB
    [ebuild  N     ] dev-libs/libaio-0.3.110::gentoo  USE="static-libs -test" ABI_X86="(64) -32 (-x32)" 42 KiB
    [ebuild  N     ] dev-util/boost-build-1.65.0::gentoo  USE="-examples -python -test" PYTHON_TARGETS="python2_7" 80,662 KiB
    [ebuild  N     ] dev-libs/boost-1.65.0:0/1.65.0::gentoo  USE="nls static-libs threads -context -debug -doc -icu -mpi -python -tools" ABI_X86="(64) -32 (-x32)" PYTHON_TARGETS="python2_7 python3_6 -python3_4 -python3_5" 0 KiB
    [ebuild  N     ] sys-block/thin-provisioning-tools-0.7.0::gentoo  USE="-static -test" 226 KiB
    [ebuild  N     ] sys-fs/lvm2-2.02.145-r2::gentoo  USE="readline static-libs thin udev (-clvm) (-cman) -corosync -device-mapper-only -lvm1 -lvm2create_initrd -openais (-selinux) -static -systemd" 0 KiB

    Total: 6 packages (6 new), Size of downloads: 81,563 KiB

    Would you like to merge these packages? [Yes/No]

After that copy over the binary files:

`root `[`#`]`cp --archive /dev/ /usr/src/initramfs/dev `

`root `[`#`]`cp --archive /sbin/cryptsetup /usr/src/initramfs/sbin/cryptsetup `

Now it is possible to unlock the encrypted root partition in [[**/init**]]:

[FILE] **`/usr/src/initramfs/init`Setting up LUKS encryption in /init**

    cryptsetup --tries 5 luksOpen /dev/sda1 luksroot

Once the passphrase is entered, the root partition will be available as [/dev/mapper/luksroot].

#### [Encrypted keyfile]

If encrypted keyfiles are required, use [cryptsetup] to encrypt them. It keeps the *initramfs* simple as that\'s the encryption tool already present - no need to add other binaries. Plus, unlike some of the alternatives, it offers a nice password prompt.

The following example creates a random 512 byte key, encrypted with LUKS, and adds it to the LUKS container [/dev/sda1].

** Note**\
\* Current versions of cryptsetup use 4096 instead of 2056 blocks for LUKS metadata. With the `--align-payload=1` parameter, it is back to 2056 blocks.

-   [cryptsetup] also offers `--keyfile-size` and `--keyfile-offset` options, which can be used for other key sizes or multiple keys in one container.

`root `[`#`]`dd if=/dev/zero of=/usr/src/initramfs/root/key.luks count=2057 `

`root `[`#`]`cryptsetup --align-payload=1 luksFormat /usr/src/initramfs/root/key.luks `

`root `[`#`]`cryptsetup open --type luks /usr/src/initramfs/root/key.luks lukskey `

`root `[`#`]`dd if=/dev/urandom of=/dev/mapper/lukskey `

`root `[`#`]`cryptsetup luksAddKey /dev/sda1 /dev/mapper/lukskey `

Unlocking the root device using this key in the [[**/init**]] can then be done like this:

[FILE] **`/usr/src/initramfs/init`LUKS encryption with keyfiles**

    # Obtain the key
    cryptsetup --tries 5 luksOpen /root/key.luks lukskey

    # Unlock the root partition
    cryptsetup --key-file /dev/mapper/lukskey open --type luks /dev/sda1 luksroot

    # Clean up the key
    cryptsetup close lukskey

As before, the root partition should then be available as [/dev/mapper/luksroot].

### [Networking]

If networking is required in *initramfs*, all required network related drivers have to be built into the kernel, and the network interfaces must be configured in [[**/init**]]. How exactly this has to be done, depends on the network situation. The following sections cover only the most common cases.

#### [Static IP]

If the network situation allows the use of a static network IP, it is possible to set it up using the [ifconfig] and [route] commands, both of which are included in Busybox. This is by far the easiest solution, so if it\'s at all possible, go for it.

[FILE] **`/usr/src/initramfs/init`Static network IP setup in /init**

    ifconfig eth0 10.0.2.15
    route add default gw 10.0.2.2

#### [DHCP]

To obtain a dynamic IP address from the network\'s DHCP server, a DHCP client is required. Busybox comes with a minimalistic DHCP client called [udhcpc], which is sufficient for most users. Unfortunately, [udhcpc] has a dependency: it requires the help of a separate script to actually configure the network interface. An example for such a script is included in the Busybox distribution, but it\'s not installed by Gentoo. It must be obtained directly from the Busybox tarball (it\'s called [examples/udhcp/simple.script]) or [download it from the Busybox project page](https://git.busybox.net/busybox/plain/examples/udhcp/simple.script).

Copy the script to the *initramfs* and make it executable.

`root `[`#`]`cp simple.script /usr/src/initramfs/bin `

`root `[`#`]`chmod +x /usr/src/initramfs/bin/simple.script `

Edit the script\'s first line to read [#!/bin/busybox sh] or create a symlink for [/bin/sh]:

`root `[`#`]`ln --symbolic busybox /usr/src/initramfs/bin/sh`

Now, it\'s possible to obtain a dynamic IP address for eth0 using DHCP:

[FILE] **`/usr/src/initramfs/init`Network setup using DHCP**

    ifconfig eth0 up
    udhcpc -t 5 -q -s /bin/simple.script

#### [DNS]

The network should be up and running now. However, that\'s only if exactly which IPs to talk to is known. If only a host or domain name is known, it\'s a different story entirely. In that case, it will be required to be able to resolve hostnames. Unfortunately, this is where our luck leaves us. Until now, everything could be done with just the static binary of Busybox - however, this is not the case with DNS.

** Note**\
Additional libraries are required to make DNS work.

This is because [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] itself dynamically includes additional libraries for DNS lookups. As long as that functionality is not required, everything should work, but if it is needed, there is no choice but to include those libraries in the *initramfs*. The only alternative would be building Busybox against another libc such as [[[sys-libs/uclibc]](https://packages.gentoo.org/packages/sys-libs/uclibc)[]], however that would go beyond the scope of this article.

This is a good chance to demonstrate how to use ([[[dev-util/strace]](https://packages.gentoo.org/packages/dev-util/strace)[]]) to reveal hidden dependencies.

`user `[`$`]`strace busybox ping wiki.gentoo.org 2>&1 | grep open`

    open("/etc/nsswitch.conf", O_RDONLY|O_CLOEXEC) = 3
    open("/etc/host.conf", O_RDONLY|O_CLOEXEC) = 3
    open("/etc/resolv.conf", O_RDONLY|O_CLOEXEC) = 3
    open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
    open("/lib64/libnss_files.so.2", O_RDONLY|O_CLOEXEC) = 3
    open("/lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
    open("/lib64/ld-linux-x86-64.so.2", O_RDONLY|O_CLOEXEC) = 3
    open("/etc/hosts", O_RDONLY|O_CLOEXEC)  = 3
    open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
    open("/lib64/libnss_dns.so.2", O_RDONLY|O_CLOEXEC) = 3
    open("/lib64/libresolv.so.2", O_RDONLY|O_CLOEXEC) = 3
    open("/etc/resolv.conf", O_RDONLY|O_CLOEXEC) = 3

The command accesses quite a lot of files, some of which are mandatory for it to work.

Copy the necessary libraries to the *initramfs*:

`root `[`#`]`cp /lib64/libnss_.so.2 /lib64/.so.2 /lib64/libc.so.6 /usr/src/initramfs/lib64`

Create a [/etc/resolv.conf] with at least one useable nameserver. Note that this step may be done automatically if using [DHCP](#DHCP).

`root `[`#`]`echo nameserver 10.0.2.3 > /usr/src/initramfs/etc/resolv.conf`

With this, DNS lookups should now work.

** Note**\
If it still does not work, this bug may be at cause: [bug 17250](https://sourceware.org/bugzilla/show_bug.cgi?id=17250). As a workaround, set `LD_LIBRARY_PATH="/lib64"` and try again.

### [Custom keyboard layout]

Busybox provides *loadkmap* to set keyboard layout. Since it only accepts binary keymaps, they must be converted first.

`root `[`#`]`cp /usr/share/keymaps/path/to/your/prefered/keymap.map.gz . `

`root `[`#`]`gzip -d keymap.map.gz `

`root `[`#`]`loadkeys -b keymap.map > /usr/src/initramfs/keymap.bmap `

Clean up:

`root `[`#`]`rm keymap.map`

Now just update the init-script:

[FILE] **`/usr/src/initramfs/init`Change keyboard layout**

    loadkmap < /keymap.bmap

## [Troubleshooting]

The following section tries to provide help with common issues and pitfalls.

### [Static vs. dynamic binaries]

Any custom binaries needed to be used in the *initramfs* before mounting have to be fully functional, independent from any files installed on the root partition. This is much easier to achieve with static binaries (which usually work as single file) than with dynamic binaries (which need any number of additional libraries to work).

Gentoo provides static binaries for some ebuilds. Check if the ebuild for the binary offers a `static` or `-dynamic` USE flag. This is by far the easiest method to get a static binary, but unfortunately only a select few ebuilds support it.

Many applications also offer static builds with an option in their configure scripts. There is no standard name for the option, it may be `--enable-static` or something similar. When compiling a package manually, check the list of available options by using [./configure \--help] to see if the package supports building static binaries.

It is possible to check whether or not a binary is static by using the [ldd] command. The [strace] command is also very useful to find out about additional dependencies. By using [equery files] it is possible to see which files a certain package has brought into the system, some of which may also be candidates for additional dependencies of that package.

** Note**\
\* See [Applications](#Applications) for a [ldd] usage example.

-   See [DNS](#DNS) for a [strace] usage example.

Including libraries into the *initramfs* in order to make a dynamic executable work is a last resort only. It makes the *initramfs* much larger than necessary and harder to maintain, as the dependencies might change with every update of the program in question.

#### [lddtree]

If deciding to go with dynamic binaries, [[[app-misc/pax-utils]](https://packages.gentoo.org/packages/app-misc/pax-utils)[]] comes with a Python script [lddtree] which will handle the collection of libraries:

** Note**\
If the [\--copy-to-tree] option is missing, enable the `python` useflag.

`root `[`#`]`lddtree --copy-to-tree /usr/src/initramfs /usr/bin/nano `

That will copy the binary and all its libraries to the *initramfs* structure - but not any of the runtime dependencies. For more details refer to [lddtree \--help].

### [Kernel panics]

When working with *initramfs* and writing custom init scripts for it, the following kernel panic may be encountered on boot:

    Kernel panic - not syncing: Attempted to kill init!

This is not an error in the kernel, but an error in the [[**/init**]] script. This script is executed as the init process with PID 1. Unlike other processes, the PID 1 init process is special. It is the only process that is started by the kernel on boot. It\'s the process that takes care of starting other processes (boot process, init scripts) which in turn start other processes (daemons, login prompts, X), which in turn start other processes (bash, window manager, browser, \...). The init process is the mother of all other processes, and therefore it mustn\'t be killed. On shutdown, it\'s again the init process that takes care of cleaning up by shutting down other processes first, then running processes that will unmount the filesystems, until it is safe to actually do a shutdown without corrupting anything.

If there is some error in the [[**/init**]] script, that causes the init process to end, this basically means there are no processes left to run, there is nothing that could take care of cleaning up, and the kernel has no choice but to panic. For this reason there are some things in [[**/init**]] that can\'t be done like in a normal shell script, like using return or exit, or letting the script just run a series of commands and then simply end.

If [[**/init**]] should end, pass the responsibility of the init process to another process using **exec**. See the examples above how **exec** is used to either run /sbin/init of the mounted root partition or to run a rescue shell in case something went wrong.

### [Job control]

While working with *initramfs*, especially the [Rescue shell](#Rescue_shell), this message mya be encountered:

    /bin/sh: can't access tty; job control turned off

The lack of job control is usually not a problem, since [[**/init**]] is not supposed to be interactive. However, to work with the Busybox shell on a regular basis, being unable to control programs with [Ctrl]+[C] or [Ctrl]+[Z] can easily become a huge issue. In worst case, if job control is not available, and a program refuses to quit, reboot.

The [job control section in the Busybox FAQ](https://www.busybox.net/FAQ.html#job_control) offers some help here. Either use:

`root `[`#`]`setsid sh -c 'exec sh </dev/tty1 >/dev/tty1 2>&1'`

or:

`root `[`#`]`setsid cttyhack sh`

to start a shell on tty1 with job control enabled.

### [Salvaging]

If for whatever reason the [/usr/src/initramfs] structure was lost, but either the kernel image with the built-in *initramfs*, or the separate cpio archive is still available, it\'s possible to salvage it from there. Although it may be easier to just redo it from scratch - after the first try, doing it again should be a piece of cake. So this is just in case.

#### [Dismantling the Kernel]

Skip this step if the *initramfs* is a separate cpio archive already. Otherwise, it will be required to get the built-in cpio archive out of the kernel image. To do that, dismantle it, which isn\'t easy, since the kernel image is a combination of boot sector and compressed archive itself. It also depends on the compression is being used for the kernel and for the *initramfs*. For simplicity, this example assumes bzip2 - however, the principle is the same for other compression methods.

The utility of choice when dismantling kernel images is [[[app-misc/binwalk]](https://packages.gentoo.org/packages/app-misc/binwalk)[]]. It analyzes arbitrary files for known signatures, and prints their offsets. While there are usually a bunch of false matches in the output, it should be easy to pick the correct ones.

`user `[`$`]`binwalk bzImage`

    DECIMAL     HEX         DESCRIPTION
    -------------------------------------------------------------------------------------------------------------------
    15949       0x3E4D      bzip2 compressed data, block size = 900k
    3042172     0x2E6B7C    LZMA compressed data, properties: 0x9A, dictionary size: 4194304 bytes, uncompressed size: 9439488 bytes
    4433597     0x43A6BD    LZMA compressed data, properties: 0xD8, dictionary size: 16777216 bytes, uncompressed size: 4213785 bytes
    8530175     0x8228FF    ELF (NetBSD)

** Note**\
Newer versions also support [binwalk \--extract] which will extract all found offsets directly.

A less sophisticated method would be to use [grep] to search for signatures. For bzip2, this is **BZh**. For gzip, use **\$\'\\x1f\'\$\'\\x8b\'**.

`user `[`$`]`grep --text --byte-offset --only-matching BZh bzImage`

    15949:BZh
    3946909:BZh

In this case the offset we are looking for is **15949** bytes. Now extract the compressed kernel image:

`user `[`$`]`dd if=bzImage bs=15949 skip=1 | bunzip2 > Image`

This yeilds the uncompressed kernel image. Somewhere within this image resides the compressed *initramfs* archive, so just iterate the previous process to find it. Depending on the kernel configuration, it might be another bzip2, gzip, or cpio container.

`user `[`$`]`binwalk Image `

`user `[`$`]`grep --text --byte-offset --only-matching BZh Image `

Suppose the offset is 171424 bytes this time. Now extract the *initramfs* cpio archive:

`user `[`$`]`dd if=Image bs=171424 skip=1 | bunzip2 > initramfs.cpio`

To verify that a cpio archive was actually retreived from that, use the [file] command:

`user `[`$`]`file initramfs.cpio`

    initramfs.cpio: ASCII cpio archive (SVR4 with no CRC)

#### [Extracting the cpio archive]

If the *initramfs* cpio archive was a separate file, it needs to be uncompressed first.

`user `[`$`]`gunzip initramfs.cpio.gz`

To extract the uncompressed [initramfs.cpio]:

** Warning**\
This will overwrite files in the current directory. Do it in [/tmp/initramfs/] or similar.

`user `[`$`]`cpio --extract --make-directories --format=newc --no-absolute-filenames < initramfs.cpio`

With this, the *initramfs* structure should have been recovered.

### [Integrated initramfs does not always update]

If the *initramfs* is integrated into the kernel (instead of using a separate file), there\'s a possibility that a [make bzImage] does not actually update it every time. This could result in making changes to the *initramfs* but actually keep booting using the old, buggy one. In this case, manually delete the integrated image to force the kernel to integrate a fresh *initramfs* archive:

`root `[`#`]`rm /usr/src/linux/usr/initramfs_data.cpio*`

Alternatively, run [make clean], but then the entire kernel will need to be recompiled.

### [Command not found]

In Gentoo, busybox is configured as standalone shell by default, which allows busybox to execute its own applets directly. Without this setting, Busybox commands ([mkdir], [mount], \...) won\'t work unless there is explicitly a symlink created for them. This can be done at the top of the [[**/init**]] script:

[FILE] **`/usr/src/initramfs/init`Install Busybox symlinks to /init**

    #!/bin/busybox sh

    # Install symlinks to all busybox applets first.
    /bin/busybox mkdir -p /usr/sbin /usr/bin /sbin /bin
    /bin/busybox --install -s

    # ...everything else below...

Alternatively, create the symlinks directly in [/usr/src/initramfs] so they will already be included in the *initramfs*.

`root `[`#`]`mkdir -p /usr/src/initramfs/ `

`root `[`#`]`chroot /usr/src/initramfs /bin/busybox --install -s `

### [Disappearing root]

If the encrypted root (with cryptsetup/LUKS), for example [/dev/mapper/gentoo-root], is disappearing after the [switch_root] command it is possible to recreate the device by entering:

`root `[`#`]`dmsetup mknodes `

### [Variations for switch_root]

Some init setups require proc, sys and dev to be mounted before starting up. If having trouble with [switch_root] in initramfs setup, try replacing the [umount] command with a [mount \--move] in the init script.

For example, replace this.

[FILE] **`/usr/src/initramfs/init`umount commands**

    # Clean up
    umount /proc
    umount /sys
    umount /dev

    # Boot the real thing
    exec switch_root /newroot /sbin/init

With this.

[FILE] **`/usr/src/initramfs/init`mount \--move commands**

    # Clean up
    mount --move /proc /newroot/proc
    mount --move /sys /newroot/sys
    mount --move /dev /newroot/dev

    # Boot the real thing
    exec switch_root /newroot /sbin/init

** Important**\
[umount] is used to ensure that \"real\" init systems, like OpenRC, start in a clean state. Ideally, use umount if it is possible in this circumstance.

## [Examples]

See [Custom_Initramfs/Examples](https://wiki.gentoo.org/wiki/Custom_Initramfs/Examples "Custom Initramfs/Examples") for fully functional examples of finished [[**/init**]] scripts.

## [See also]

-   [Initramfs\_-\_make_your_own](https://wiki.gentoo.org/wiki/Initramfs_-_make_your_own "Initramfs - make your own") --- build an initramfs which does not contain kernel modules.
-   [Initramfs/Guide](https://wiki.gentoo.org/wiki/Initramfs/Guide "Initramfs/Guide") --- covers the concepts of the initramfs as well as how to properly create and manage initramfs instances.
-   [Early Userspace Mounting](https://wiki.gentoo.org/wiki/Early_Userspace_Mounting "Early Userspace Mounting") --- how to build a custom minimal [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") that checks the [/usr] filesystem and pre-mounts [/usr]. Another worth to read article about custom initramfs

## [External resources]

-   Official initramfs documentation locally ([less [/usr/src/linux/Documentation/filesystems/ramfs-rootfs-initramfs.txt]]) or [online at kernel.org](https://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt)
-   [Linux® From Scratch - About initramfs](http://www.linuxfromscratch.org/blfs/view/stable/postlfs/initramfs.html)

## [References]

1.  [[[↑](#cite_ref-1)] [[update initramfs using bash](https://codeberg.org/keks24/update-initramfs)]]