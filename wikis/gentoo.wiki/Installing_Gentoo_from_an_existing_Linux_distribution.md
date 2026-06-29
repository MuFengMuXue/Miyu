This page contains [[changes](https://wiki.gentoo.org/index.php?title=Installation_alternatives&oldid=1385252&diff=1420210#Installing_Gentoo_from_an_existing_Linux_distribution)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Installation_alternatives/de "Alternative Installationsmethoden (63% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Installation_alternatives/es "Métodos alternativos de instalación (45% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Installation_alternatives/it "Alternative di installazione (44% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Installation_alternatives/hu "Telepítési alternatívák (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Installation_alternatives/pl "Installation alternatives/pl (6% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Installation_alternatives/ru "Альтернативные методы установки (69% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Installation_alternatives/zh-cn "其他安装方式 (4% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Installation_alternatives/ja "代替のインストール方法 (50% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Installation_alternatives/ko "Installation alternatives/ko (18% translated)")

[[]]This article has some todo items:\

-   Verify & validate these methods
-   A few more details and references would be helpful
-   Better wording

\
This article describes alternative installation methods, i.e. other than booting the LiveDVD in the optical drive. See also the [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") article for various installation related information.

## Contents

-   [[1] [Installation from non-Gentoo live environments]](#Installation_from_non-Gentoo_live_environments)
-   [[2] [Diskless install using PXE from the LiveCD]](#Diskless_install_using_PXE_from_the_LiveCD)
    -   [[2.1] [TFTP]](#TFTP)
    -   [[2.2] [DHCP]](#DHCP)
    -   [[2.3] [SYSLINUX]](#SYSLINUX)
    -   [[2.4] [GRUB]](#GRUB)
    -   [[2.5] [iPXE]](#iPXE)
-   [[3] [Diskless install using PXE boot and NFS]](#Diskless_install_using_PXE_boot_and_NFS)
    -   [[3.1] [Requirements]](#Requirements)
    -   [[3.2] [Server base setup]](#Server_base_setup)
    -   [[3.3] [Creating the system on the server]](#Creating_the_system_on_the_server)
    -   [[3.4] [Booting the new client]](#Booting_the_new_client)
-   [[4] [Installing Gentoo from an existing Linux distribution]](#Installing_Gentoo_from_an_existing_Linux_distribution)
    -   [[4.1] [Requirements]](#Requirements_2)
    -   [[4.2] [Overview]](#Overview)
    -   [[4.3] [How to make space for Gentoo?]](#How_to_make_space_for_Gentoo.3F)
    -   [[4.4] [Using parted to resize partition]](#Using_parted_to_resize_partition)
    -   [[4.5] [Chrooting]](#Chrooting)
-   [[5] [Booting ISO from a bootloader]](#Booting_ISO_from_a_bootloader)
    -   [[5.1] [Using GRUB]](#Using_GRUB)
    -   [[5.2] [rEFInd]](#rEFInd)
-   [[6] [Booting ISO from UEFI]](#Booting_ISO_from_UEFI)
-   [[7] [See also]](#See_also)

## [Installation from non-Gentoo live environments]

** Important**\
The only *fully supported* method for installing Gentoo is with the *[Minimal Install CD](https://www.gentoo.org/downloads/)*. That said, installing from another, recent, live environment will usually work just as well. [Gentoo support](https://www.gentoo.org/support/) will often still be forthcoming using this method, but be ready to revert to the *Minimal Install CD*, if needed. Of course, in case of issues with other distributions, users will be referred to other channels for help.

** Tip**\
The Handbook is regularly tested to check for installation issues using non-Gentoo media and it is now generally considered safe to follow on distributions as old as Debian Jessie. Please do report issues in [[#gentoo-wiki](ircs://irc.libera.chat/#gentoo-wiki)] ([[webchat](https://web.libera.chat/#gentoo-wiki)]) if it is found to no longer be the case.

Once [chrooted](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Entering_the_new_environment "Handbook:AMD64/Installation/Base"), and with an appropriate [stage](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Installing_a_stage_tarball "Handbook:AMD64/Installation/Stage") tarball, these live images can provide a functional environment to use for compiling and installing Gentoo. These instructions should, in principle, work with most recently created Linux live environments.

There are [many LiveCDs](https://distrowatch.com/search.php?ostype=Linux&category=Live+Medium&origin=All&basedon=All&notbasedon=None&desktop=All&architecture=All&package=All&rolling=All&isosize=All&netinstall=All&language=All&defaultinit=All&status=Active#simple) out there, one example being [Knoppix](https://www.knopper.net/knoppix/index-en.html) (available for **[x86]** and **[amd64]**).

** Warning**\
If anything is saved in the LiveCD\'s home directory while waiting for the Gentoo system to install, it will not be available when rebooting into Gentoo. Be sure to save important files on the hard disk or on some other computer!

Boot from the LiveCD. Open a terminal and run [su -] so the password can be changed. This allows to set the root password for the CD. The sshd daemon can now be configured for remote login if required. Next, create the [/mnt/gentoo] mount point:

`root `[`#`]`mkdir /mnt/gentoo`

At this point, the standard install documentation can be picked up at [Preparing the Disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks"). However, when asked to mount the proc system, issue the following command instead:

`root `[`#`]`mount -o bind /proc /mnt/gentoo/proc`

When unpacking the [stage tarball](https://wiki.gentoo.org/wiki/Stage_tarball "Stage tarball") in [Unpacking the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Unpacking_the_stage_tarball "Handbook:AMD64/Installation/Stage"), be sure to use the following [tar] command options to ensure that proper group IDs are enforced on the unpacked stage:

`root `[`#`]`tar --numeric-owner --xattrs -xvJpf stage3-*.tar.xz -C /mnt/gentoo `

For some distributions, such as Ubuntu, pay particular attention to the warning in the [Mounting the necessary filesystems](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Mounting_the_necessary_filesystems "Handbook:AMD64/Installation/Base") section of the handbook. [[[bug #496328]](https://bugs.gentoo.org/show_bug.cgi?id=496328)[]] may be of interest if issues are still encountered.

Once ready to chroot into the unpacked stage in [Installing Base System](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base "Handbook:AMD64/Installation/Base"), a different chroot command sequence will need to be used. This ensures that the environment variables are properly setup.

** Note**\
Some LiveCDs use a funny environment setup, hence the [env -i] option for cleaning it up to a reasonable state.

`root `[`#`]`chroot /mnt/gentoo /bin/env -i TERM=$TERM /bin/bash `

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile `

`root `[`#`]`export PS1="(chroot) $PS1" `

Finally, know that some Portage `FEATURES` may not work in the LiveCD. Especially watch out for `userpriv` and `usersandbox` values. If there are errors, try disabling some or all of the optional `FEATURES`.

## [Diskless install using PXE from the LiveCD]

This method is easier to configure than PXE boot based on iSCSI or NFS. Multiple machines can boot from the same set of images distributed via TFTP and can be easily extended to also work over HTTP or other protocol.

Having a nice router, or one capable of running open source firmware such as [OpenWRT/LEDE](https://openwrt.org/), is one way to centralize TFTP and DHCP. Getting the firmware online can sometimes be an uphill battle.

Some other distributions including Fedora already distribute images needed to bootstrap a live, or installation, CD. With Gentoo, users need to extract files from the ISO.

`root `[`#`]`emerge --ask --oneshot app-cdr/cdrtools`

** Note**\
When using the iPXE configuration below, the initrd does not have to be combined with squashfs. Simply extract /boot/gentoo, /boot/gentoo.igz, and /image.squashfs into your server\'s root.

[CODE] **Prepare Gentoo in tftproot**

    mkdir -p /tftpboot/gentoo/
    cd /tftpboot/gentoo/
    isoname=/tftpboot/ISO-IMAGES/install-amd64-minimal-20210725T170534Z.iso
    isoinfo -R -i $ -X -find -path /boot/gentoo && mv boot/gentoo kernel && rmdir boot
    isoinfo -R -i $ -X -find -path /image.squashfs
    # combine initrd + squashfs
    (isoinfo -R -i $ -x /boot/gentoo.igz; (echo image.squashfs | cpio -H newc -o)) > network.igz
    rm image.squashfs
    ls -lhF kernel network.igz

These instructions may be sufficient for more experienced users. See below for more directions, depending on the PXE flavor in use. There are different PXE boot-codes, but all of them require a kernel and eventually a ramdisk.

Please take a look at [PXE](https://wiki.gentoo.org/wiki/PXE "PXE") page for details on the alternatives, then come back here.

### [TFTP]

This will be needed in tandem with a DHCP server for most PCs equipped with PXE boot. However, iPXE may be used to boot without a TFTP or DHCP server - see [ipxe.org](http://ipxe.org/) for info on embedding scripts, chainloading, and manual booting. There are still merits to TFTP booting such as wide-range device support.

Install [[[net-ftp/tftp-hpa]](https://packages.gentoo.org/packages/net-ftp/tftp-hpa)[]], make sure it serves [/tftproot] and start it.

Now the TFTP boot service is ready, so the next step is to configure a DHCP service.

### [DHCP]

Setting up a DHCP server on the same machine is possible - just make sure that the booted machines are connected to it. Or just tweak the configuration of an existing router.

Example configuration for OpenWRT DHCP service follows:

[FILE] **`/etc/config/dhcp`**

    config boot linux
            option filename boot/grub/i386-pc/core.0
            option servername boot
            option serveraddress 84.246.161.86

From here, directions will change depending on the PXE boot-code (i.e. SYSLINUX, GRUB, iPXE).

### [SYSLINUX]

[FILE] **`/tftproot/pxelinux.cfg/default`**

    label gentoo install (squashfs/http)
      kernel gentoo/kernel
      initrd gentoo/network.igz
      append root=/dev/ram0 init=/linuxrc  dokeymap looptype=squashfs loop=/image.squashfs  cdroot net.ifnames=0

### [GRUB]

[FILE] **`/tftproot/boot/grub/grub.cfg`**

    menuentry "gentoo install" **

    #!ipxe
    :gentoo
    set boot-url <your server address>
    kernel $/gentoo
    initrd $/gentoo.igz
    initrd $/image.squashfs /image.squashfs.img
    imgargs gentoo root=live:/image.squashfs.img cdroot passwd=root

## [Diskless install using PXE boot and NFS]

### [Requirements]

PXE (Preboot eXecution Environment) is a method for booting computers over a PXE-capable network interface (and using a PXE-supporting BIOS). In case the system does not support PXE boot from the network interface or BIOS, PXE can also be used as a boot method from block devices (like CDs or USBs). In such cases, a minimal boot environment mimics the PXE supporting network card (see also [Etherboot/gPXE](http://etherboot.org)).

### [Server base setup]

Create directories: The first thing to do is to create the directories where the diskless system will be stored. Create a directory called [/diskless] which houses a directory for each diskless client. For the remainder of this howto, the client that is being worked on will be called \'eta\'.

`root `[`#`]`mkdir -p /diskless/eta`

DHCP and TFTP setup: The client will get boot information using DHCP and download all the required files using TFTP.

For dhcpd, just run [emerge dhcp] (or any other DHCP server of choice). Make sure that the correct interface is selected in [/etc/conf.d/dhcpd], and configure it accordingly. Then, add the following on [/etc/dhcp/dhcpd.conf].

** Note**\
This provides a static IP address for the client and the path of a PXE boot image, here [pxegrub]. The MAC address of the ethernet card of the client in the example has to be replaced with the correct MAC address, as well as the directory where the client files will be stored.

[FILE] **`dhcpd.conf`**

    option option-150 code 150 = text ;
    ddns-update-style none ;
    host eta

Next configure the interface in [/etc/conf.d/net] so that it doesn\'t get cleared at bootup. See [/usr/share/doc/openrc-\*/net.example.bz2] for more information.

[FILE] **`/etc/conf.d/net`Ensure the interface (here eth0 as example) is not reconfigured at boot**

    config_eth0="noop"

For TFTP, emerge [[[net-ftp/tftp-hpa]](https://packages.gentoo.org/packages/net-ftp/tftp-hpa)[]]. In [/etc/conf.d/in.tftpd], put the following:

[FILE] **`in.tftpd`**

    INTFTPD_PATH="/diskless"
    INTFTPD_USER="nobody"
    INTFTPD_OPTS="-u $ -l -vvvvvv -p -c -s $"

Emerge [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"):

`root `[`#`]`emerge --ask sys-boot/grub`

Once GRUB is compiled, create the diskless client\'s boot directory:

`root `[`#`]`grub2-mknetdir --net-directory=/diskless/eta`

Original way was to copy the PXE image to the diskless client but the path does not seem to exit anymore.

`root `[`#`]`mkdir /diskless/eta/boot `

`root `[`#`]`cp /usr/lib/grub/pxegrub /diskless/eta/boot/pxegrub `

Then edit its [grub.lst] config file.

`root `[`#`]`nano -w /diskless/eta/boot/grub.lst`

[FILE] **`grub.lst`**

    default 0
    timeout 30

    title=Diskless Gentoo
    root (nd)
    kernel /eta/bzImage ip=dhcp root=/dev/nfs nfsroot=ip.add.re.ss:/diskless/eta

    # For the nfsroot option, the IP address is the one of the server and
    # the directory is the one where the diskless client files are located (on the server).

NFS is quite easy to configure. The only thing that has to be done is to add a line on the [/etc/exports] config file:

[FILE] **`/etc/exports`**

    /diskless/eta eta(rw,sync,no_root_squash)

One important thing to do now is to modify the [/etc/hosts] file to fit requirements.

[FILE] **`/etc/hosts`**

    127.0.0.1 localhost
    192.168.1.10 eta.example.com eta
    192.168.1.20 sigma.example.com sigma

### [Creating the system on the server]

A next step is to reboot the server with a Gentoo installation CD (although experienced administrators can continue without if they are sufficiently versed in Gentoo installations). Follow the standard install procedure as explained in the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") BUT with the following differences: when mounting the file system, execute the next step (where [sdaX] is the partition where the [/diskless] directory was created).

`root `[`#`]`mount /dev/sdaX /mnt/gentoo`

Mounting any other partition is not needed as all of the files will reside in the [/diskless/eta] directory.

This example uses a stage3 tarball. Mount [/proc] to the diskless directory and chroot into it to continue with the install. Then follow the installation manual until kernel configuration.

** Warning**\
Be very careful when extracting the stage tarball to its destination, so as to not end up extracting over an existing installation.

`root `[`#`]`cd /mnt/gentoo/diskless/eta/ `

`root `[`#`]`tar -xvjpf /mnt/cdrom/gentoo/stage3-*.tar.bz2 `

`root `[`#`]`mount -t proc /proc /mnt/gentoo/diskless/eta/proc `

`root `[`#`]`cp /etc/resolv.conf /mnt/gentoo/diskless/eta/etc/resolv.conf `

`root `[`#`]`chroot /mnt/gentoo/diskless/eta/ /bin/bash `

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile `

When doing the [make menuconfig] of the kernel configuration, don\'t forget to enable the following options with the others recommended into the install guide.

[KERNEL] **Necessary options for diskless installations**

    - The network card device support
    (In the kernel, *not* as a module!)

    -*- Networking support --->
      Networking options --->
        [*] TCP/IP networking
        [*] IP: kernel level autoconfiguration
        [*] IP: DHCP support
        [*] IP: BOOTP support

    File systems --->
      [*] Network File Systems --->
        <*> NFS file system support
        [*] Provide NFSv3 client support
        [*] Root file system on NFS

Save the kernel in the chrooted [/] (not in [/boot]) according to the pxegrub setting defined earlier. Next configure the diskless client\'s [/etc/fstab].

[FILE] **`/etc/fstab`**

    /dev/cdroms/cdrom0 /mnt/cdrom iso9660 noauto,ro 0 0

Now to prevent the client from running a filesystem check:

`root `[`#`]`touch /fastboot `

`root `[`#`]`echo "touch /fastboot" >> /etc/conf.d/local.start `

Install [[[net-fs/nfs-utils]](https://packages.gentoo.org/packages/net-fs/nfs-utils)[]] since the client will heavily depend on it:

`root `[`#`]`emerge --ask net-fs/nfs-utils`

Do not install another bootloader because there is already one - pxegrub. Simply finish the install and restart the server. Start the services that are needed to boot the new client: DHCP, TFTPD, and NFS.

`root `[`#`]`service dhcp start `

`root `[`#`]`service in.tftpd start `

`root `[`#`]`service nfs start `

### [Booting the new client]

For the new client to boot properly, the BIOS and the network card need to be configured to use PXE as the first boot method - before CD-ROM or floppy. For help with this consult the hardware manuals or manufacturers website. The network card should get an IP address using DHCP and download the GRUB PXE image using TFTP. Then, a nice black and white GRUB bootmenu should be displayed from where users can select the kernel to boot and press the [Enter] (Return) key. If everything is okay the kernel should boot, mount the root filesystem using NFS and provide a login prompt. Enjoy.

## [Installing Gentoo from an existing Linux distribution]

** Important**\
The only *fully supported* method for installing Gentoo is with the *[Minimal Install CD](https://www.gentoo.org/downloads/)*. That said, installing from another, recent, live environment will usually work just as well. [Gentoo support](https://www.gentoo.org/support/) will often still be forthcoming using this method, but be ready to revert to the *Minimal Install CD*, if needed. Of course, in case of issues with other distributions, users will be referred to other channels for help.

### [Requirements]

In order to install Gentoo from an existing Linux distribution it needs to have the chroot command installed, and have a copy of the Gentoo installation or ISO that\'s desired to install. A network connection is needed to download files during the installation.

### [Overview]

-   First allocate a partition to Gentoo by resizing an existing Linux partition.
-   Mount the partition.
-   [Choose an appropriate stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Choosing_a_stage_tarball "Handbook:AMD64/Installation/Stage") and unpack it to the partition that is mounted.
-   [Configure compile options](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Configuring_compile_options "Handbook:AMD64/Installation/Stage") for Portage.
-   [Mount the necessary filesystems](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Mounting_the_necessary_filesystems "Handbook:AMD64/Installation/Base") and [chroot](https://wiki.gentoo.org/wiki/Installation_alternatives#Chrooting "Installation alternatives") inside the pseudo-system.
-   After entering the new environment, follow Gentoo Handbook from [Mounting the boot partition](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Mounting_the_boot_partition "Handbook:AMD64/Full/Installation") to the end.

### [][How to make space for Gentoo?]

The root partition is the filesystem mounted under [/]. The first example shows the output of [mount] on a system. The second example uses [df] (disk free) to see how much space there is left and how it will be resized. Note that resizing the root partition is not mandatory! Anything else supported by the resizer can be resized, but let\'s talk about that later.

`root `[`#`]`mount`

    /dev/sdb2 on / type ext3 (rw)
    none on /proc type proc (rw)
    none on /dev/pts type devpts (rw,gid=5,mode=620)
    none on /dev/shm type tmpfs (rw,nodev,nosuid,noexec)

`root `[`#`]`df -h`

    Filesystem           Size Used Avail Use% Mounted on
    /dev/sdb2            4.0G 1.9G  2.4G  82% /
    none                  38M    0   38M   0% /dev/shm

As can be seen, the partition mounted as [/] named [/dev/sdb2] has 2.4 GB free. In this case, it was decided to be resized as to leave 400 MB of free space, therefore allocating 2 GB for Gentoo. Not bad, it could have quite some stuff installed. However, 1 GB is deemed enough for most users. So now partition this thing!

### [Using parted to resize partition]

[[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] is extremely useful for resizing partitions. It is included on the [Minimal installation CD](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/Media#Minimal_installation_CD "Handbook:Parts/Installation/Media").

** Note**\
There are other tools for doing resize of partitions as well, but an elaborate description of these tools is outside the scope of this guide.

Look up on that page the type of file system to resize and see if [parted] can do it. If not, some partitions might need to be destroyed to make space for Gentoo. Go ahead downloading the software and install it. In the next step, a problem arises: the Linux root partition needs to be resized, therefore a boot medium with a minimal Linux system must be booted in order to resize [/]. If the partition can be unmounted while still running in Linux then the following steps are not needed. Just install [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] and run it on a chosen unmounted partition to resize. Here\'s how it was done on this system.

** Important**\
Make sure that the operations that are required for partitioning are supported by parted!

** Note**\
Note again that Linux is synonym of \"There\'s one more way to do it\". The objective is to run parted on an unmounted partition so it can do its work. This step might not even be needed to do at all: there may only be the need to umount the filesystem to repartition in the Linux session and run parted on it.

Time to reboot and resize the partition. Do this only after taking a quick look at the parted documentation on the GNU website. The resize can be long for large hard-drives, be patient. Reboot the system with the Minimal installation CD. Run parted to be able to resize the partition. Once this lengthy process is done, continue with installing Gentoo. Reboot back into the old Linux system for now. The drive to operate on is the drive containing the partition that is going to be resized. For example, if the partition to be resized is [/dev/sda3], the drive is [/dev/sda].

`root `[`#`]`parted`

`(parted)``print`

    Disk geometry for /dev/sdb: 0.000-9787.148 megabytes
    Disk label type: msdos
    Minor    Start       End     Type      Filesystem  Flags
    1          0.031   2953.125  primary   ntfs
    3       2953.125   3133.265  primary   linux-swap
    2       3133.266   5633.085  primary   ext3
    4       5633.086   9787.148  extended
    5       5633.117   6633.210  logical
    6       6633.242   9787.148  logical   ext3

`(parted)``help resizepart`

      resizepart NUMBER END                    resize partition NUMBER

    NUMBER is the partition number used by Linux.  On MS-DOS disk labels, the primary partitions
            number from 1 to 4, logical partitions from 5 onwards.
            END is disk location, such as 4GB or 10%.  Negative value counts from the end of the disk.
            For example, -1s specifies exactly the last sector.

`(parted)``resizepart 2 3133.266 4000.000`

** Important**\
Be patient! The computer is working! Just look at the hard drive LED on the case to see its activity. This should take between 2 and 30 minutes.

Once the resize has finished, boot back into the old Linux as described. Then go to [The Gentoo Handbook: Preparing the Disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks") and follow the instructions.

### [[] Chrooting]

When chrooting, use the following command to flush the environment:

`root `[`#`]`env -i HOME=$HOME TERM=$TERM chroot /mnt/gentoo /bin/bash `

`root `[`#`]`/usr/sbin/env-update `

`root `[`#`]`source /etc/profile `

The rest of the instructions are the same as [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Mounting_the_boot_partition "Handbook:AMD64/Installation/Base"). Enjoy!

## [Booting ISO from a bootloader]

The default installation method is to burn the [installation media](https://www.gentoo.org/downloads/) to a USB drive. This way one has to dedicate an entire drive for installation. Instead one can use a bootloader to boot an ISO image saved as an ordinary file in a filesystem, or saved in one partition. It can also be used as a rescue medium after installation.

### [Using GRUB]

In this section we describe [Grub](https://wiki.gentoo.org/wiki/Grub "Grub") configuration.

The point is to extract the kernel boot options and the initramfs option from the iso image. To identify them, mount the iso file somewhere, and read the grub.cfg:

`root `[`#`]` mount -o loop <iso file> <some>/<directory>/ `

`root `[`#`]` cat <some>/<directory>/boot/grub/grub.cfg # typically here `

      ...
      linux /boot/gentoo overlayfs nodhcp looptype=squashfs loop=/image.squashfs cdroot
      initrd /boot/gentoo.igz
      ...

Two steps are necessary. First, you have to specify the loopback device, like this:

[CODE]

    if [ x$feature_platform_search_hint = xy ]; then
      # Use the partition number
      search --no-floppy --fs-uuid --set=isopart --hint-bios=hd0,gpt10 --hint-efi=hd0,gpt10 dccf78a8-6456-4c81-ada8-26e7bc739b53
    else
      # use the uuid
      search --no-floppy --fs-uuid --set=isopart dccf78a8-6456-4c81-ada8-26e7bc739b53
    fi
    # You can omit the if-then construction, and directy choose one clause.

    set isofile="/<iso file image location>"
    loopback loop ($isopart)$isofile
    set root=(loop)

For a complete instruction, see the grub documentation. Here, the partition of the filesystem is specified, and `isofile` is the path to the iso file. Next, modify the above original configuration of the iso image as:

[CODE]

    linux /boot/gentoo iso-scan/filename=$isofile secureconsole root=live:CDLABEL=gentoo-amd64-livegui rd.live.dir=/ rd.live.squashimg=image.squashfs cdroot
    initrd /boot/gentoo.igz

i.e. add `iso-scan/filename=` to the boot option.

Then wrap all inside `menuentry` block in the file `/etc/grub.d/40_custom` and generate grub.cfg as usual. This is [is reported to work](https://forums.gentoo.org/viewtopic-p-8867430.html#8867430) in July 2025.

See also the ArchLinux Wiki article [Multiboot USB drive](https://wiki.archlinux.org/title/Multiboot_USB_drive).

### [rEFInd]

To boot an ISO image from rEFInd, see the page [rEFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd").

## [Booting ISO from UEFI]

In some PCs, the Gentoo LiveDVD iso image can be directly booted from UEFI. For that copy the iso image to a partition:

[CODE]

    dd if=<iso image filename> of=/dev/disk/by-<foo>/<bar> bs=8M

Then in the UEFI boot option, try something like \"boot from EFI\". Some reports a DVD, while others the *drive* (SSD, usb-HDD etc) that stores the image.

## [See also]

-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.
-   [Install Gentoo on a bootable USB stick](https://wiki.gentoo.org/wiki/Install_Gentoo_on_a_bootable_USB_stick "Install Gentoo on a bootable USB stick") --- describes how to install Gentoo onto a USB stick that can be booted on any computer.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Gerald Normandin Jr., Travis Tilley, Oleg Raisky, Alex Garbutt, Alexandre Georges, Magnus Backanda, Faust A. Tanasescu, Daniel Ahlberg, Ken Nowack, Tiemo Kieft, Benny Chuang, Jonathan Smith, and **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*