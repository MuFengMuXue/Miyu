[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Installation_on_libreboot&action=edit).

While the Gentoo handbook is very thorough in detailing the process of installation on a standard [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") environment, Gluglugs or librebooted, refurbished Thinkpads take some special considerations. The purpose of this article is to document some of these considerations to help out any other Gentoo users who decide to take the 100% Free Software philosophy into practice with their installs.

## Contents

-   [[1] [Booting a Gentoo LiveCD Environment from Libreboot]](#Booting_a_Gentoo_LiveCD_Environment_from_Libreboot)
    -   [[1.1] [Manually boot Gentoo from GRUB CLI]](#Manually_boot_Gentoo_from_GRUB_CLI)
-   [[2] [Maintaining FSF Certified Status]](#Maintaining_FSF_Certified_Status)
-   [[3] [Use a Kernel without blobs]](#Use_a_Kernel_without_blobs)
    -   [[3.1] [Method 1 (recommended): Remove proprietary binary blobs from linux-firmware]](#Method_1_.28recommended.29:_Remove_proprietary_binary_blobs_from_linux-firmware)
        -   [[3.1.1] [Installing free firmware]](#Installing_free_firmware)
    -   [[3.2] [Method 2 (not recommended): Use linux-libre sources]](#Method_2_.28not_recommended.29:_Use_linux-libre_sources)
-   [[4] [GRUB Payload]](#GRUB_Payload)
-   [[5] [See also]](#See_also)

## [Booting a Gentoo LiveCD Environment from Libreboot]

After following the directions at [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") to construct a bootable installation medium, you might encounter some issues with the grub scripts the Libreboot developer has written for booting from USB drives. If the directions for loading the isolinux config from USB at [libreboot.org](https://www.libreboot.org/docs/gnulinux/grub_boot_installer.html) are followed, it spits out a three line error code and fails to boot the iso.

### [Manually boot Gentoo from GRUB CLI]

To bypass this you must drop to the GRUB command line and manually specify your LiveCD kernel & initrd before issuing the boot command.

-   First descend to the GRUB command line:

`c`

-   Next issue the [ls] command to verify the location of your Gentoo LiveUSB:

`grub>``ls `

Below is an example output from that command:

`grub>``ls `

    (mem) (proc) (cbfs) (achi0) (achi0,msdos) (usb0)

-   Next specify the location of the Gentoo kernel, making sure to pass any parameters needed for boot. See [man bootparam] or use Google for more kernel parameters. The example below assumes that the Gentoo LiveCD is the only USB drive connected. The `root=/dev/ram0` is *important*, without it there is a **kernel panic.**

`grub>``linux (usb0)/isolinux/gentoo root=/dev/ram0 init=/linuxrc dokeymap looptype=squashfs loop=/image.squashfs cdroot `

** Note**\
If this doesn\'t work, users can try replacing `(usb0)/isolinux/gentoo` with `(usb0)/boot/gentoo`.

-   With the kernel and parameters specified, it\'s just a matter of identifying the initrd:

`grub>``initrd (usb0)/isolinux/gentoo.igz `

-   Finally execute the boot command:

`grub>``boot `

## [Maintaining FSF Certified Status]

While configuring the portage [make.conf] be sure to specify that you want nothing to do with any software which isn\'t completely free. The whole point of this guide is to build a Libre Gentoo system after all. This step has to be done **before emerging any software** or do a manual update with the `--newuse` flag which can result in recompiling a lot of software unnecessarily.

[FILE] **`/etc/portage/make.conf`Instruct portage to allow only free software**

    ACCEPT_LICENSE="@FREE"

See [License Groups](https://wiki.gentoo.org/wiki/License_groups "License groups") for more info.

## [Use a Kernel without blobs]

There are two ways to ensure the kernel won\'t contain any binary blobs.

### [][Method 1 (recommended): Remove proprietary binary blobs from linux-firmware]

The standard [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] package doesn\'t include any firmware **at all**. In gentoo there is a seperate package [[[sys-kernel/linux-fimrware]](https://packages.gentoo.org/packages/sys-kernel/linux-fimrware)[]] that contains both free and non-free firmware. A [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") must be set to prevent portage from installing non-free firmware from this package. Here are instruction on how to install only free firmware from the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]

#### [Installing free firmware]

Set the `-redistributable` USE flag to install only free firmware:

[FILE] **`/etc/portage/package.use`**

    sys-kernel/linux-firmware -redistributable

** Warning**\
The USE flag might be locked according to your profile. To unlock it:

[FILE] **`/etc/portage/profile/use.mask`**

    redistributable

Install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]

`root `[`#`]`emerge --ask --verbose sys-kernel/linux-firmware`

Now the firmware should get emerged with the `@FREE` variable in `ACCEPT_LICENSE`.

### [][Method 2 (not recommended): Use linux-libre sources]

The [Free Software Foundation Latin America](http://www.fsfla.org/ikiwiki/) maintains a Linux kernel fork that has been deprived of any proprietary firmware - it is called [linux-libre](https://www.fsfla.org/ikiwiki/selibre/linux-libre/). You can use this kernel to make a fully free system, but it is not recommended because it won\'t get automatically updated by portage. It is also more difficult to install patches from [Project:Hardened](https://wiki.gentoo.org/wiki/Project:Hardened "Project:Hardened")

You have been warned!

Navigate to [linux-libre.org](http://linux-libre.fsfla.org/pub/linux-libre/releases/) and download the desired kernel source.

`user `[`$`]`links http://linux-libre.fsfla.org/pub/linux-libre/releases/`

When it comes time to [Handbook:Parts/Installation/Kernel](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/Kernel "Handbook:Parts/Installation/Kernel") just extract the kernel source to a safe location and then symlink it to [/usr/src/linux]. The commands below are examples given the current kernel at time of writing, do not copy & paste these commands into ssh.

`user `[`$`]`tar xvjpf linux-libre-3.19.1-gnu.tar.bz2`

`root `[`#`]`ln -s /mnt/gentoo/linux-3.19.1 /mnt/gentoo/usr/src/linux`

## [GRUB Payload]

If you are using GRUB as Libreboot payload, it searches for [libreboot_grub.cfg] files on every partition in [/boot/grub/] and [/grub/]. So you have to place the [grub.cfg] file there.

`root `[`#`]`grub-mkconfig -o /boot/grub/libreboot_grub.cfg`

Possible invocation of [grub-mkconfig], so libreboot-GRUB may find the config file.

Other ways to configure a GRUB Payload are listed on the libreboot site. [\[1\]](https://libreboot.org/docs/gnulinux/grub_cbfs.html)

## [See also]

-   [Lenovo ThinkPad T400](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_T400 "Lenovo ThinkPad T400") --- A ThinkPad with [libreboot support](https://libreboot.org/docs/install/t400_external.html).