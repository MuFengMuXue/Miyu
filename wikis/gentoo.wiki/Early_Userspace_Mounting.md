[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This article will detail how to build a custom minimal [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") that checks the [/usr] filesystem and pre-mounts [/usr]. This has become necessary for affected configurations because of various changes in [udev](https://wiki.gentoo.org/wiki/Udev "Udev") (see [[[bug #364235]](https://bugs.gentoo.org/show_bug.cgi?id=364235)[]]).

In this article we\'ll be working with the following:

-   [Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox")
-   An initramfs content list
-   The [gen_init_cpio] and [gen_initramfs.sh] utilities, provided by the kernel itself.

The initramfs also contains the required libraries and binaries to run an [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") fsck. Most of the code to run the fsck is coming from the [/etc/init.d/fsck] script.

When using any other [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") than ext4, add the required binaries / libraries into the initramfs list.

Basically, the init script is doing following actions:

1.  Mounts the root partition on [/mnt/root] as read-only.
2.  Symlinks the [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") from the root partition to the initramfs environment.
3.  Checks the filesystem of our [/usr] device using the embedded [/sbin/fsck] binary.
4.  Mounts [/usr], then moves it to [/mnt/root/usr] using the `--move` mount parameter.
5.  Switches to real root and executes [init].

The article also assumes we are working in [/usr/src/initramfs], so for the sake of ease, begin with creating this directory.

## Contents

-   [[1] [Requirements]](#Requirements)
-   [[2] [System preparation]](#System_preparation)
-   [[3] [Generating the Initramfs]](#Generating_the_Initramfs)
    -   [[3.1] [Building as an embedded Initramfs]](#Building_as_an_embedded_Initramfs)
    -   [[3.2] [Building as an external CPIO archive]](#Building_as_an_external_CPIO_archive)
-   [[4] [Bootloader configuration]](#Bootloader_configuration)
    -   [[4.1] [Configuring GRUB]](#Configuring_GRUB)
    -   [[4.2] [Configuring LILO]](#Configuring_LILO)
-   [[5] [Using a Stub Kernel]](#Using_a_Stub_Kernel)
-   [[6] [Result]](#Result)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Requirements]

The most important package here is [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]] as it provides utilities suitable for an initramfs. It is also critical that to emerge it with `static` USE flag enabled:

`root `[`#`]`USE="static" emerge --ask sys-apps/busybox`

** Note**\
Enabling the `static` USE flag will disable PAM support, regardless if its enabled or not.

Make sure that the running kernel is built with the *devtmpfs* option enabled. It is required by the init script below and [udev](https://wiki.gentoo.org/wiki/Udev "Udev"):

[KERNEL]

     Device Drivers  --->
       Generic Driver Options  --->
           [*] Maintain a devtmpfs filesystem to mount at /dev Search for <code>CONFIG_DEVTMPFS</code> to find this item.

Next up is the [initramfs_list] file which will tell [gen_initramfs.sh] how to construct the initramfs:

[FILE] **`/usr/src/initramfs/initramfs_list`**

    # directory structure
    dir /proc       755 0 0
    dir /usr        755 0 0
    dir /bin        755 0 0
    dir /sys        755 0 0
    dir /var        755 0 0
    dir /lib        755 0 0
    dir /sbin       755 0 0
    #dir /lib64      755 0 0
    #dir /lib32      755 0 0
    dir /mnt        755 0 0
    dir /mnt/root   755 0 0
    dir /etc        755 0 0
    dir /root       700 0 0
    dir /dev        755 0 0

    # busybox
    file /bin/busybox /bin/busybox 755 0 0

    # libraries required by /sbin/fsck.ext4 and /sbin/fsck
    file    /lib/ld-linux.so.2      /lib/ld-linux.so.2                  755 0 0
    file    /lib/libext2fs.so.2     /lib/libext2fs.so.2                 755 0 0
    file    /lib/libcom_err.so.2    /lib/libcom_err.so.2                755 0 0
    file    /lib/libpthread.so.0    /lib/libpthread.so.0                755 0 0
    file    /lib/libblkid.so.1      /lib/libblkid.so.1                  755 0 0
    file    /lib/libmount.so.1      /lib/libmount.so.1                  755 0 0
    file    /lib/libuuid.so.1       /lib/libuuid.so.1                   755 0 0
    file    /lib/libe2p.so.2        /lib/libe2p.so.2                    755 0 0
    file    /lib/libc.so.6          /lib/libc.so.6                      755 0 0
    file    /lib/librt.so.1         /lib/librt.so.1                     755 0 0
    file    /lib/libdl.so.2         /lib/libdl.so.2                     755 0 0

    file    /sbin/fsck              /sbin/fsck                          755 0 0
    file    /sbin/fsck.ext4         /sbin/fsck.ext4                     755 0 0

    # our init script
    file    /init                   /usr/src/initramfs/init             755 0 0

** Note**\
Please note that if the computer under maintenance is running the **[amd64]** version, it is necessary to do a bit of editing. Reference lib64 rather than lib for the libraries required by [/sbin/fsck.ext4] and [/sbin/fsck]. Additionally, the ld-linux library needs to explicitly point to the x86-64 version. For example, the first three lines of that section would now be:

[FILE] **`/usr/src/initramfs/initramfs_list`**

    # libraries required by /sbin/fsck.ext4 and /sbin/fsck
    file    /lib64/ld-linux-x86-64.so.2      /lib64/ld-linux-x86-64.so.2                  755 0 0
    file    /lib64/libext2fs.so.2   /lib64/libext2fs.so.2               755 0 0

Once all the libraries are pointing to their 64bit counterparts it is also necessary to uncomment the lines under #directory structure. The script has now been adapted for **[amd64]** usage.

Copy and save the contents of the above to [/usr/src/initramfs/initramfs_list] after adjusting for the current architecutre.

Last up is the actual [init] file which will execute the initramfs:

[FILE] **`/usr/src/initramfs/init`**

    #!/bin/busybox sh

    rescue_shell()

    uuidlabel_root()

    check_filesystem()

    # temporarily mount proc and sys
    mount -t proc none /proc
    mount -t sysfs none /sys
    mount -t devtmpfs none /dev

    # disable kernel messages from popping onto the screen
    echo 0 > /proc/sys/kernel/printk

    # clear the screen
    clear

    # mounting rootfs on /mnt/root
    uuidlabel_root || rescue_shell "Error with uuidlabel_root"

    # space separated list of mountpoints that ...
    mountpoints="/usr" #note: you can add more than just usr, but make sure they are declared in /usr/src/initramfs/initramfs_list

    # ... we want to find in /etc/fstab ...
    ln -s /mnt/root/etc/fstab /etc/fstab

    # ... to check filesystems and mount our devices.
    for m in $mountpoints ; do
        check_filesystem $m

        echo "Mounting $m"
        # mount the device and ...
        mount $m || rescue_shell "Error while mounting $m"

        # ... move the tree to its final location
        mount --move $m "/mnt/root"$m || rescue_shell "Error while moving $m"
    done

    echo "All done. Switching to real root."

    # clean up. The init process will remount proc sys and dev later
    umount /proc
    umount /sys
    umount /dev

    # switch to the real root and execute init
    exec switch_root /mnt/root /sbin/init

Copy and save the contents of the above to [/usr/src/initramfs/init].

## [System preparation]

In fstab, we must set the sixth field for the `/usr` entry to `0`, this will prevent the [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") fsck init script to try to check the filesystem for the already mounted [/usr]:

[FILE] **`/etc/fstab`**

    /dev/sdb3   /usr    ext4   noatime  0 0

## [Generating the Initramfs]

### [Building as an embedded Initramfs]

It is not necessary to compile [gen_init_cpio] or make it executable because these steps will be handled when building the kernel with [make]. Both files, [initramfs_list] and [init] must be copied into [/usr/src/initramfs/]. For an embedded initramfs one line is missing and must be **added** to [initramfs_list]

[FILE] **`/usr/src/initramfs/initramfs_list`**

    nod /dev/console 0600 0 0 c 5 1

This kernel configuration will do all steps to include all needed files in an embedded initramfs.

For embedding the initramfs directly into the kernel image, the [initramfs_list] must be coded in **Initramfs source file(s)** (`CONFIG_INITRAMFS_SOURCE`) in the kernel (directly under the **Initial RAM filesystem and RAM disk (initramfs/initrd) support** (`CONFIG_BLK_DEV_INITRD`) option):

[KERNEL] **CONFIG_INITRAMFS_SOURCE=\"/usr/src/initramfs/initramfs_list\"**

     General setup  --->
       [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support Search for <code>CONFIG_BLK_DEV_INITRD</code> to find this item.
       (/usr/src/initramfs/initramfs_list) Initramfs source file(s) Search for <code>CONFIG_INITRAMFS_SOURCE</code> to find this item.
       [*]   Support initial ramdisk/ramfs compressed using gzip Search for <code>CONFIG_RD_GZIP</code> to find this item.
       Built-in initramfs compression mode (Gzip)  --->

### [Building as an external CPIO archive]

The [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") sources provide the [gen_init_cpio] and [gen_initramfs.sh] utilities. The [gen_init_cpio] utility does not come prepackaged and needs to be built:

`root `[`#`]`make -C /usr/src/linux/usr/ gen_init_cpio`

Make sure that these two are executable:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`chmod +x usr/gen_init_cpio usr/gen_initramfs.sh `

** Note**\
For older Kernels exchange usr/ with scripts/

Run the [gen_initramfs.sh] script with the `-o` argument pointing to where we want the initramfs image to be placed followed by the path to our [initramfs_list] file:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`usr/gen_initramfs.sh -o /boot/initrd.cpio /usr/src/initramfs/initramfs_list `

After that compress the file [/boot/initrd.cpio] via [gzip]:

`root `[`#`]`gzip --best /boot/initrd.cpio`

This will create the archive [/boot/initrd.cpio.gz].

## [Bootloader configuration]

To use the external initramfs, the [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") needs to be configured as shown below for GRUB and LILO as examples. For an embedded Initramfs this is not necessary !

### [Configuring GRUB]

Add the `initrd` line to [/boot/grub/grub.conf]:

[FILE] **`grub.conf`**

    title Gentoo Linux <version>
    root (hd0,0)
    kernel /boot/kernel-<version>-gentoo
    initrd /boot/initrd.cpio.gz

### [Configuring LILO]

Add the `initrd` and `append` line to [/etc/lilo.conf]:

[FILE] **`lilo.conf`**

    image = /boot/vmlinuz-<version>-gentoo
      #root = /dev/sda4
      label = gentoo
      read-only
      append = "real_root=/dev/sda4"
      initrd = boot/initrd.cpio.gz

## [Using a Stub Kernel]

If no bootmanager is used (UEFI boots a stub kernel directly) the UUID of the root partition must be configured into the built-in kernel command line or as parameter in the UEFI boot entry (see next paragraph):

[KERNEL]

     Processor type and features  --->
       [*] Built-in kernel command line Search for <code>CONFIG_CMDLINE_BOOL</code> to find this item.
       (root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx) Built-in kernel command string Search for <code>CONFIG_CMDLINE</code> to find this item.

When using an external Initramfs [initrd.cpio.gz] must be copied to the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") and initrd= must use the correct path. Set the parameter initrd= only in an UEFI boot entry. It does not work when setting it in the built-in kernel command line. In this case it is recommended to set both parameter in this UEFI boot entry. Example:

`root `[`#`]`efibootmgr -c -d /dev/sda -p 1 -L "Gentoo" -l '\EFI\gentoo\bzImage.efi' -u 'root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx initrd=\EFI\gentoo\initrd.cpio.gz'`

See more here: [Efibootmgr#Creating_a_boot_entry](https://wiki.gentoo.org/wiki/Efibootmgr#Creating_a_boot_entry "Efibootmgr")

## [Result]

When booting, the output looks like this:

[CODE] **output of the initramfs when booting**

    Mounting rootfs
    Checking local filesystem :  /usr
    /dev/sdb3: clean, 285754/1640160 files, 1663220/6556528 blocks
    Mounting /usr
    (Potentially other fs checks on other partitions here...)
    All done. Switching to real root.
    INIT: version 2.88 booting

        OpenRC 0.9.8.4 is starting up Gentoo Linux (i686)

    Press I to enter interactive boot mode
    [...]

## [See also]

-   [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs") --- the successor of *initrd*. It provides early userspace which can do things the kernel can\'t easily do by itself during the boot process.
-   [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") --- a file [archiving](https://wiki.gentoo.org/wiki/Data_compression "Data compression") utility

## [External resources]

-   [http://jootamam.net/howto-initramfs-image.htm](http://jootamam.net/howto-initramfs-image.htm)
-   [http://whitehathouston.com/documentation/gentoo/initramfs_howto.htm](http://whitehathouston.com/documentation/gentoo/initramfs_howto.htm) Link seems dead
-   [http://www.landley.net/writing/rootfs-howto.html](http://www.landley.net/writing/rootfs-howto.html)
-   [https://forums.gentoo.org/viewtopic-p-7038132.html](https://forums.gentoo.org/viewtopic-p-7038132.html)