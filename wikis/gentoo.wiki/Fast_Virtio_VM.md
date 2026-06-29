[]  As of **2024-08-26**, the information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Fast_Virtio_VM&action=edit).

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fast_Virtio_VM&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This page explains a way to build a blazing fast Gentoo VM under [KVM](https://wiki.gentoo.org/wiki/QEMU "QEMU") using Virtio and mdev.

## Contents

-   [[1] [Steps]](#Steps)
    -   [[1.1] [Use a fast computer]](#Use_a_fast_computer)
    -   [[1.2] [Use ext2]](#Use_ext2)
    -   [[1.3] [Kernel]](#Kernel)
    -   [[1.4] [Kernel boot options]](#Kernel_boot_options)
    -   [[1.5] [Use a static IP]](#Use_a_static_IP)
    -   [[1.6] [Use mdev]](#Use_mdev)
    -   [[1.7] [Configure mdev]](#Configure_mdev)
    -   [[1.8] [Prelink]](#Prelink)
    -   [[1.9] [OpenRC]](#OpenRC)
    -   [[1.10] [tmpfs]](#tmpfs)
-   [[2] [Results]](#Results)

## [Steps]

### [Use a fast computer]

No really, this is probably the most important thing of all, don\'t expect a 2 second booting VM if you are on a P3 with a slow IDE disk. This tutorial is Build on a CentOS 6.2 KVM HypverVisor on a Dual QuadCore Xeon 2.4Ghz with 8 (v)CPU\'s and 2GB RAM assigned to the VM. The disk file is on an SSD (old Intel x25-M 80GB, so there is more to gain if you use a faster SSD).

### [Use ext2]

It has the fastest mount time.

### [Kernel]

Compile the kernel with:

-   VirtIO support
-   Hugetlb support

<!-- -->

-   NO usb support (Unless planning to passthrough USB from the host).
-   NO HID support (see above).
-   NO extended video/device drivers/filesystem drivers that will not be used. (duh)
-   NO fuse support (Slow\...)
-   NO modules (Slower\...)

### [Kernel boot options]

-   noapic (APIC is for hardware management, and since we are in VM and the hardware is managed by our host, we don\'t need it).
-   notsc (TSC is CPU clock synchronization, not needed in a VM).

Because they cannot be removed from the kernel itself, no need these as kernel boot options.

### [Use a static IP]

DHCP is slow.

### [Use mdev]

Replace [udev](https://wiki.gentoo.org/wiki/Udev "Udev") with [mdev](https://wiki.gentoo.org/wiki/Mdev "Mdev") (BusyBox), udev is dead slow vs mdev.

### [Configure mdev]

Remove useless mdev devices (tun,tap, all sound, hd\*, sd\*, fd\*, md\*, grsec(\*), zap, dvb, v4l stuff)

### [Prelink]

Prelink all binaries:

`root `[`#`]`emerge --ask prelink`

`root `[`#`]`prelink -amRf`

### [OpenRC]

Use [rc-update](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") to delete all non-essential daemons (git, consolefont, devfs, keymaps, modules, sysfs, swclock, staticroute)

### [tmpfs]

Use [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") for [/tmp] and [/var/run] (will not necessarily speedup boot, but for startup services that [/tmp] heavily, it might help).

## [Results]

I created my own boot time init script, which echoes the current kernel uptime.

Please keep in mind that all of this is without \*any\* dirty tricks like initrd or [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). It\'s just static sequential boot. Even using parallel start of services (thru `RC_PARALLEL="yes"`) would slow down the system.