[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=PINE64_PinePhone_Pro&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]]This article has some todo items:\

-   This article does not conform to the relevant [article blueprint](https://wiki.gentoo.org/wiki/Article_blueprints "Article blueprints").

The **PinePhone** Pro is a flagship arm64 smartphone produced by Pine64, with the goal of supporting user-modifiable operating systems and hardware. It is an upgrade over the existing [PINE64 PinePhone](https://wiki.gentoo.org/wiki/PINE64_PinePhone "PINE64 PinePhone"). It is equipped with a Rockchip hexa-core SoC operating at 1.5GHz, paired with 4GB of dual-channel LPDDR4 RAM, and can boot from either microSD (removable storage) or eMMC (internal storage).

Currently only the Explorer Edition is available, which \"is aimed at Linux developers with an extensive knowledge of embedded systems and/or experience with mobile Linux.\" - meaning that it\'s not yet ready for daily use.

## [Installation]

While any mobile Linux distribution (like postmarketOS) could be used to bootstrap a Gentoo Linux installation, it is recommended doing the initial setup from an existing PC because it\'s faster and allows doing the entire install with a keyboard and mouse. Unless using an aarch64 computer, this will require either Crossdev or the QEMU user space emulator, though both are recommended.

QEMU-user allows running non-native binaries on the host-system, meaning that it is possible to unpack an aarch64 stage3 tarball and chroot into it. This works just fine for most things, but for code compilation it is slow. To solve this problem, also install Crossdev, which allows easily installing a cross compiler toolchain onto the host system. A cross compiler runs native code itself, but outputs machine code for another architecture, in this case aarch64, which means that it will run at full speed!

The most widely used bootloaders on the PinePhone Pro are [u-boot](https://wiki.pine64.org/wiki/Uboot), [Tow-boot](https://tow-boot.org/devices/pine64-pinephonePro.html) and levinboot

** Important**\
Both u-boot and Tow-boot suffer from an annoying bug that causes the device to not charge if the battery gets completely emptied.

### [Option 1: levinboot on SD card]

levinboot is currently in beta-stage and it only supports booting from **either** SD-card or eMMC. levinboot is unusual in that it uses payload partitions to load the kernel, initramfs and device trees. By default, set up three 60M payload partitions with hardcoded GUIDs. The payloads must be created in a specific format and then copied over with a program like dd(1).