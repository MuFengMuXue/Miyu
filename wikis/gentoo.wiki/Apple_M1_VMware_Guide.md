This page describes the process of installing Gentoo on VMware Fusion Tech Preview on Apple Silicon Mac. The procedure in this guide has been tested on the following platforms:

-   Apple MacBook Pro, M1 Max CPU, VMware Fusion Tech Preview 22H2
-   Apple MacBook Pro, M1 Max CPU, VMware Player Version 13.6.1 (24319021)

## Contents

-   [[1] [VM Settings]](#VM_Settings)
-   [[2] [Preparing the Disks]](#Preparing_the_Disks)
    -   [[2.1] [Create the EFI System Partition]](#Create_the_EFI_System_Partition)
    -   [[2.2] [Create Root Partition]](#Create_Root_Partition)
-   [[3] [Creating Filesystems]](#Creating_Filesystems)
-   [[4] [Mounting the root partition]](#Mounting_the_root_partition)
-   [[5] [Getting a Stage 3 Tarball]](#Getting_a_Stage_3_Tarball)
    -   [[5.1] [Setting Up make.conf]](#Setting_Up_make.conf)
-   [[6] [Chrooting]](#Chrooting)
    -   [[6.1] [Enter the new rootfs environment]](#Enter_the_new_rootfs_environment)
    -   [[6.2] [Configure Portage]](#Configure_Portage)
    -   [[6.3] [Setting the Timezone]](#Setting_the_Timezone)
-   [[7] [Configuring the Kernel]](#Configuring_the_Kernel)
-   [[8] [Set the Root Password]](#Set_the_Root_Password)
-   [[9] [Bootloader]](#Bootloader)
-   [[10] [Rebooting the System]](#Rebooting_the_System)
-   [[11] [Gnome]](#Gnome)
    -   [[11.1] [Background]](#Background)
    -   [[11.2] [Unmasking Packages and USE flags]](#Unmasking_Packages_and_USE_flags)
    -   [[11.3] [Installing Gnome]](#Installing_Gnome)
    -   [[11.4] [Optional: Installing open-vm-tools]](#Optional:_Installing_open-vm-tools)
    -   [[11.5] [Troubleshooting]](#Troubleshooting)

## [VM Settings]

Before booting the VM, change the settings:

1.  **Hard Disk Bus Type** Go to *VM Settings \> Hard Disk \> Advanced \> Bus Type*. Set bus type to SATA.
2.  **Hard Disk Size** Set the disk size to at least 30 Gbytes.
3.  **Memory Size** Go to *VM Settings \> Processors & Memory* and configure the VM with at least 4 Gbytes of memory.
4.  **Number of CPUs** In *VM Settings \> Processors & Memory* set the number of Processors.

## [Preparing the Disks]

Once the VM is booted, start by preparing the disks using [fdisk]. This guide uses GPT partition table and UEFI firmware.

    livecd ~ # fdisk /dev/sda

     Command (m for help): g
     Created a new GPT disklabel (GUID: A75C1035-8C9C-2749-9F86-73C15F41A835).

    Command (m for help): p
     Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
     Disk model: VMware Virtual S
     Units: sectors of 1 * 512 = 512 bytes
     Sector size (logical/physical): 512 bytes / 512 bytes
     I/O size (minimum/optimal): 512 bytes / 512 bytes
     Disklabel type: gpt
     Disk identifier: A75C1035-8C9C-2749-9F86-73C15F41A835

### [Create the EFI System Partition]

    Command (m for help): n
    Partition number (1-128, default 1): 1
    First sector (2048-83886046, default 2048):
    Last sector, +/-sectors or +/-size (2048-83886046, default 83886046): +256M

    Created a new partition 1 of type 'Linux filesystem' and of size 256 MiB.

    Command (m for help): t
    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

    Command (m for help):

### [Create Root Partition]

Create a second partition, and accept the default values for all prompts:

    Command (m for help): n
    Partition number (2-128, default 2):
    First sector (526336-83886046, default 526336):
    Last sector, +/-sectors or +/-size (526336-83886046, default 83886046):

    Created a new partition 2 of type 'Linux filesystem' and of size 39.7 GiB.

When partitioning is complete, the layout should look like:

    Command (m for help): p
    Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
    Disk model: VMware Virtual S
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: gpt
    Disk identifier: A75C1035-8C9C-2749-9F86-73C15F41A835

    Device      Start      End  Sectors  Size Type
    /dev/sda1    2048   526335   524288  256M EFI System
    /dev/sda2  526336 83886046 83359711 39.7G Linux filesystem

Use the `w` command to write the new partition layout to disk:

    Command (m for help): w
    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

## [Creating Filesystems]

Each of the partitions that were just created needs to have a filesystem stored on it to save files:

`livecd ~ #``mkfs.vfat -F 32 /dev/sda1 `

`livecd ~ #``mkfs.ext4 /dev/sda2`

## [Mounting the root partition]

`livecd ~ #``mount /dev/sda2 /mnt/gentoo`

## [Getting a Stage 3 Tarball]

Go to the Gentoo downloads page and copy the link to the stage 3 tarball. **MAKE SURE TO GET THE ARM64** version. This is a compressed file that contains a minimal filesystem for your new Gentoo installation. Inside the VM, use the [wget] utility to download that stage 3 tarball.

**Before downloading the stage 3**, make sure to [cd /mnt/gentoo], the directory where the rootfs was mounted in the last step.

`livecd ~ #``cd /mnt/gentoo`

`livecd /mnt/gentoo #``wget <URL OF STAGE3>`

Next, extract the tarball into the rootfs:

`livecd /mnt/gentoo #``tar xpf <STAGE3 FILE NAME> --xattrs-include='*.*' --numeric-owner`

### [Setting Up make.conf]

The [make.conf] file has config options that tell Gentoo\'s package manager how to compile packages.

A sample [make.conf] is below

[FILE] **`/etc/portage/make.conf`**

    # These settings were set by the catalyst build script that automatically
    # built this stage.
    # Please consult /usr/share/portage/config/make.conf.example for a more
    # detailed example.
    COMMON_FLAGS="-O2"
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"
    # WARNING: Changing your CHOST is not something that should be done lightly.
    CHOST="aarch64-unknown-linux-gnu"

    # NOTE: This stage was built with the bindist Use flag enabled

    # This sets the language of build output to English.
    # Please keep this setting intact when reporting bugs.
    LC_MESSAGES=C

    USE="-qt5 -kde X gtk gnome -gnome-online-accounts -wireless -bluetooth -ppp"

    MAKEOPTS="-j8"
    ACCEPT_LICENSE="-* @FREE @BINARY-REDISTRIBUTABLE"

[FILE] **`/etc/portage/package.use/00localization`**

    */* LINGUAS: en

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* vmware fbdev

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_ARM: aes sha1 sha2 sha3 crc32 neon v8 vfpv4

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: efi-64

**Note:** The `-march=native` flag seemed to cause problems when compiling ffmpeg, so it has been removed in this sample `make.conf`.

## [Chrooting]

Copy [resolv.conf] which contains DNS server info, into the new rootfs:

`livecd /mnt/gentoo #``cp /etc/resolv.conf /mnt/gentoo/etc/`

Mount a bunch of pseudo filesystems needed by Linux:

`livecd /mnt/gentoo #``mount --types proc /proc /mnt/gentoo/proc `

`livecd /mnt/gentoo #``mount --rbind /sys /mnt/gentoo/sys `

`livecd /mnt/gentoo #``mount --make-rslave /mnt/gentoo/sys `

`livecd /mnt/gentoo #``mount --rbind /dev /mnt/gentoo/dev `

`livecd /mnt/gentoo #``mount --make-rslave /mnt/gentoo/dev `

`livecd /mnt/gentoo #``mount --bind /run /mnt/gentoo/run `

`livecd /mnt/gentoo #``mount --make-slave /mnt/gentoo/run`

### [Enter the new rootfs environment]

`livecd /mnt/gentoo #``chroot /mnt/gentoo /bin/bash `

`livecd /mnt/gentoo #``. /etc/profile `

Mount the [/boot] partition:

`(chroot) livecd / #``mount /dev/sda1 /boot`

### [Configure Portage]

`(chroot) livecd / #``emerge-webrsync `

`(chroot) livecd / #``emerge --sync`

\
Set up your locale by editing the `locale.gen` file.

`(chroot) livecd / #``nano /etc/locale.gen`

\

[FILE] **`/etc/portage/make.conf`**

    #en_US ISO-8859-1
    en_US.UTF-8 UTF-8

\

`(chroot) livecd / #``locale-gen `

`(chroot) livecd / #``eselect locale list `

     [1]   C
     [2]   C.utf8
     [3]   POSIX
     [4]   en_US.utf8
     [5]   C.UTF8 *
     [ ]   (free form)

`(chroot) livecd / #``eselect locale set 4 `

\

Update the `@world` package list:

`(chroot) livecd / #``emerge --ask --verbose --update --deep --newuse @world`

### [Setting the Timezone]

`(chroot) livecd / #``echo "America/Chicago" > /etc/timezone `

`(chroot) livecd / #``emerge --config sys-libs/timezone-data`

## [Configuring the Kernel]

Install the `linux-firmware` and `gentoo-sources` packages:

`(chroot) livecd / #``emerge --ask sys-kernel/linux-firmware `

`(chroot) livecd / #``emerge --ask sys-kernel/gentoo-sources`

`gentoo-sources` gives us the Linux kernel source, which must be hand-built.

`(chroot) livecd / #``eselect kernel list`

     [1] linux-5.15.80-gentoo

`(chroot) livecd / #``eselect kernel set 1 `

`(chroot) livecd / #``cd /usr/src/linux`

`(chroot) livecd /usr/src/linux #``make menuconfig`

The minimum requirement to make the VM boot is enabling the DRM driver in the kernel. This is needed to display a terminal prompt.

[KERNEL] **Enable support for VMware DRM**

    -> Device Drivers
      -> Graphics support
        [*] DRM driver for VMware Virtual GPU

If you also want `open-vm-tools` integration, which provides performance improvements and improved integration with the host (shared clipboard, etc), enable the following in the kernel:

[KERNEL] **Enable support for VMware DRM**

    -> Device Drivers
      -> Network device support
        [*] VMware VMXNET3 ethernet driver

When this guide was written (Jan 2023), most of the host integration features in the kernel were only supported on x86.

After configuring your kernel, you can build and install it. The following command uses `-j10` to start 10 build jobs. Usually the number of build jobs should be the same as the number of CPU cores you configured your VM with. The more build jobs you use, the faster your build will finish.

`(chroot) livecd /usr/src/linux #``make -j10 Image && make -j10 modules && make install && make modules_install`

Install `dhcpcd`, needed to get IP address via DHCP:

`(chroot) livecd /usr/src/linux #``emerge dhcpcd `

`(chroot) livecd /usr/src/linux #``rc-update add dhcpcd default`

\
Find the name of the VM\'s Ethernet interface by looking at the output of `ifconfig`. In this example, it\'s called `ens160`:

    ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 172.16.44.130  netmask 255.255.255.0  broadcast 172.16.44.255
            inet6 fe80::23be:d7df:9454:bb82  prefixlen 64  scopeid 0x20<link>
            ether 00:0c:29:c8:a5:1d  txqueuelen 1000  (Ethernet)
            RX packets 807368  bytes 1097038659 (1.0 GiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 292703  bytes 28455835 (27.1 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
            device interrupt 69  memory 0x38500000-38520000

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 1952  bytes 155712 (152.0 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 1952  bytes 155712 (152.0 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

`(chroot) livecd /usr/src/linux #``nano /etc/conf.d/net`

[FILE] **`/etc/conf.d/net`/etc/conf.d/net example**

    config_ens160="dhcp"

`(chroot) livecd /usr/src/linux #``cd /etc/init.d `

`(chroot) livecd /usr/src/linux #``ln -s net.lo net.ens160 `

`(chroot) livecd /usr/src/linux #``rc-update add net.ens160 default`

      * service net.ens160 added to runlevel default

## [Set the Root Password]

Use the `passwd` utility to set the root password. It might look like your characters aren\'t registering them when you type them, but they are. The utility just doensn\'t print anything on the screen when you\'re typing a password.

`(chroot) livecd /etc/init.d #``passwd`

## [Bootloader]

Installing Grub

`(chroot) livecd /etc/init.d #``emerge --ask --verbose sys-boot/grub`

`(chroot) livecd /etc/init.d #``grub-install --target=arm64-efi --efi-directory=/boot --bootloader-id=Gentoo`

`(chroot) livecd /etc/init.d #``grub-mkconfig -o /boot/grub/grub.cfg`

\

## [Rebooting the System]

`(chroot) livecd /usr/src/linux #``exit `

`(chroot) livecd /usr/src/linux #``cd`

`(chroot) livecd /usr/src/linux #``umount -R /mnt/gentoo`

`(chroot) livecd /usr/src/linux #``reboot`

## [Gnome]

#### [Background]

When this guide was written (Jan 2023), there were a lot of unstable video and device drivers in Gentoo that are required to install Gnome. In order to install the required drivers (vmware mouse and video drivers), we need to manually unmask them.

#### [Unmasking Packages and USE flags]

Need to unmask the fbdev and vmware video drivers to allow them to be installed. Create a new file `/etc/portage/profile/use.mask`:

[FILE] **`/etc/portage/profile/use.mask`/etc/portage/profile/use.mask**

    -video_cards_vmware
    -video_cards_fbdev

Enable gnome-light by providing ACCEPT_KEYWORDS variable. Create the file `/etc/portage/package.accept_keywords/gnome_light` with the following contents:

[FILE] **`/etc/portage/package.accept_keywords/gnome_light`/etc/portage/package.accept_keywords/gnome_light**

    gnome-base/gnome-light **
    x11-drivers/xf86-video-vmware **
    x11-drivers/xf86-video-fbdev **

Set use flags for mesa by creating `/etc/portage/package.use/mesa` with the following contents:

[FILE] **`/etc/portage/package.use/mesa`/etc/portage/package.use/mesa**

    media-libs/mesa xa

#### [Installing Gnome]

Need to set your profile to Gnome Desktop:

`(chroot) livecd /usr/src/linux #``eselect profile list`

    Available profile symlink targets:
      [1]  default/linux/amd64/23.0 (stable)
      [2]  default/linux/amd64/23.0/systemd (stable)
      [3]  default/linux/amd64/23.0/desktop (stable) *
      [4]  default/linux/amd64/23.0/desktop/systemd (stable)
      [5]  default/linux/amd64/23.0/desktop/gnome (stable)
      [6]  default/linux/amd64/23.0/desktop/gnome/systemd (stable)
      [7]  default/linux/amd64/23.0/desktop/plasma (stable)
      [8]  default/linux/amd64/23.0/desktop/plasma/systemd (stable)
      [9]  default/linux/amd64/23.0/no-multilib (stable)
      [10]  default/linux/amd64/23.0/no-multilib/systemd (stable)
      [11]  default/linux/amd64/23.0/no-multilib/hardened (stable)
      [12]  default/linux/amd64/23.0/no-multilib/hardened/systemd (stable)
      [12]  default/linux/amd64/23.0/no-multilib/hardened/selinux (stable)
      [14]  default/linux/amd64/23.0/no-multilib/hardened/selinux/systemd (stable)
      [15]  default/linux/amd64/23.0/no-multilib/prefix (exp)
      [16]  default/linux/amd64/23.0/no-multilib/prefix/kernel-2.6.32+ (exp)
      [17]  default/linux/amd64/23.0/no-multilib/prefix/kernel-2.6.16+ (exp)
      [18]  default/linux/amd64/23.0/no-multilib/prefix/kernel-3.2+ (exp)
      [19]  default/linux/amd64/23.0/llvm (stable)
      [20]  default/linux/amd64/23.0/llvm/systemd (stable)
      [21]  default/linux/amd64/23.0/hardened (stable)
      [22]  default/linux/amd64/23.0/hardened/systemd (stable)
      [23]  default/linux/amd64/23.0/hardened/selinux (stable)
      [24]  default/linux/amd64/23.0/hardened/selinux/systemd (stable)
      [25]  default/linux/amd64/23.0/split-usr (stable)
      [26]  default/linux/amd64/23.0/split-usr/desktop (stable)
      [27]  default/linux/amd64/23.0/split-usr/desktop/gnome (stable)
      [28]  default/linux/amd64/23.0/split-usr/desktop/plasma (stable)
      [29]  default/linux/amd64/23.0/split-usr/no-multilib (stable)
      [30]  default/linux/amd64/23.0/split-usr/no-multilib/selinux (stable)
      [31]  default/linux/amd64/23.0/split-usr/no-multilib/hardened (stable)
      [32]  default/linux/amd64/23.0/split-usr/no-multilib/hardened/selinux (stable)
      [33]  default/linux/amd64/23.0/split-usr/no-multilib/prefix (exp)
      [34]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-2.6.32+ (exp)
      [35]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-2.6.16+ (exp)
      [36]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-3.2+ (exp)
      [37]  default/linux/amd64/23.0/split-usr/llvm (stable)
      [38]  default/linux/amd64/23.0/split-usr/hardened (stable)
      [39]  default/linux/amd64/23.0/split-usr/hardened/selinux (stable)
      [40]  default/linux/amd64/23.0/musl (dev)
      [41]  default/linux/amd64/23.0/musl/llvm (exp)
      [43]  default/linux/amd64/23.0/musl/hardened (exp)
      [43]  default/linux/amd64/23.0/musl/hardened/selinux (exp)
      [44]  default/linux/amd64/23.0/split-usr/musl (dev)
      [45]  default/linux/amd64/23.0/split-usr/musl/llvm (exp)
      [46]  default/linux/amd64/23.0/split-usr/musl/hardened (exp)
      [47]  default/linux/amd64/23.0/split-usr/musl/hardened/selinux (exp)

Enable the mouse driver in the kernel

[KERNEL] **Enable CONFIG_INPUT_MOUSEDEV**

    -> Device Drivers
      -> Input device support
        -> Generic input layer (needed for keyboard, mouse, ...) (INPUT [=y])
          <*> Mouse interface

\

`(chroot) livecd /usr/src/linux #``eselect profile set default/linux/amd64/23.0/desktop/gnome `

`(chroot) livecd /usr/src/linux #``emerge gnome-light`

Start `dbus` service, needed by X (and Gnome)

`(chroot) livecd /usr/src/linux #``/etc/init.d/dbus start `

`(chroot) livecd /usr/src/linux #``rc-update add dbus default`

\
Set display manager to GDM:

`(chroot) livecd /usr/src/linux #``nano /etc/conf.d/display-manager`

[FILE] **`/etc/conf.d/display-manager`/etc/conf.d/display-manager**

    DISPLAYMANAGER="gdm"

\
Start the login manager:

`(chroot) livecd /usr/src/linux #``/etc/init.d/xdm start`

#### [Optional: Installing `open-vm-tools`]

The `open-vm-tools`, provides some nice integration features between host and guest. When this guide was written, a lot of the kernel drivers that are required to support host integration are x86-only, but some stuff (like HGFS file sharing) still works.

Since `open-vm-tools` is still experimental, unmask it:

[FILE] **`/etc/portage/package.accept_keywords/open-vm-tools`/etc/portage/package.accept_keywords/open-vm-tools**

    app-emulation/open-vm-tools **
    dev-libs/libdnet **

Then add USE flags for `open-vm-tools`

[FILE] **`/etc/portage/package.use/open-vm-tools`/etc/portage/package.use/open-vm-tools**

    app-emulation/open-vm-tools gtkmm resolutionkms fuse

\

`(chroot) livecd /usr/src/linux #``emerge open-vm-tools`

\

#### [Troubleshooting]

Check the log file `/var/log/Xorg.0.log` for error messages. Error lines start with `EE`.

\
Packages like `llvm`, `rust`, and others often fail in the link stage because the linker runs out of memory. Error messages are usually cryptic and unhelpful when this happens. If you suspect that your VM is running out of memory, add more swap space to enable the link to complete:

\

`livecd ~ #``mkswap /swapfile `

`livecd ~ #``swapon /swapfile`