Flicker free boot is a Linux feature that seeks to eliminate display flickers that occur during system boot. It was created by Hans de Goede and is available in Fedora since version 30 and can be implemented in on Gentoo systems.

** Warning**\
This is not an easy task to accomplish and might break the system. It is recommended to make a backup of all files in the [/boot] partition before attempting this tutorial. **No support for boot failures will be provided by Gentoo (forums, bugs, email, IRC) when using software outside of the repository. Follow this tutorial at your own risk!**

## Contents

-   [[1] [Testing]](#Testing)
-   [[2] [Requirements]](#Requirements)
    -   [[2.1] [Hardware / Software]](#Hardware_.2F_Software)
    -   [[2.2] [Knowledge]](#Knowledge)
    -   [[2.3] [Summary]](#Summary)
-   [[3] [Installing the required software]](#Installing_the_required_software)
    -   [[3.1] [Setting the correct USE flags for plymouth]](#Setting_the_correct_USE_flags_for_plymouth)
    -   [[3.2] [Using dracut]](#Using_dracut)
    -   [[3.3] [Setting up EFI stub]](#Setting_up_EFI_stub)
    -   [[3.4] [Alternative: setting up systemd-boot (systemd users only)]](#Alternative:_setting_up_systemd-boot_.28systemd_users_only.29)
-   [[4] [See also]](#See_also)
-   [[5] [External References]](#External_References)

## [Testing]

Community members are encouraged to share success or failure results in the following table. This way we can get a more accurate view of which systems obtain success.

  --------------------------- --------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device Model                CPU (Code Name)                                     Notes
  Dell Inspiron 15 5567       Intel Core i7-7500U (Kaby Lake)                     The boot process is completely fluent, using kernel patches from [\[1\]](https://gitlab.freedesktop.org/drm/intel/-/issues/2972) or kernel version below 5.7.
  Dell PowerEdge T20          Intel Xeon E3-1225v3 (Haswell)                      The boot process is around 80% fluent. It flickers once for 2 - 3 sec. Unfortunately it\'s the same when booting from a Microsoft Windows 10 based USB key, so it appears to be the way it was implemented.
  Lenovo ThinkPad P52         Intel Core i7-8750H (Coffee Lake)                   The boot process is completely fluent
  Lenovo Thinkbook 14s Yoga   11th Gen Intel(R) Core(TM) i5-1135G7 (Tiger-Lake)   Works great with the systemd-boot option; tested with =sys-kernel/gentoo-kernel-bin-5.12.8.
  --------------------------- --------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Requirements]

### [][Hardware / Software]

-   A working UEFI setup, preferably with a Intel Skylake (6th Generation) or more recent Intel processor.
-   Older (3rd to 5th Generation Intel Core series processors may work, but are not guaranteed. Test to find out.
-   The Intel integrated (i915) series graphics adapters must be used. Other graphics cards (AMD, NVIDIA, etc.) are not (yet) supported by flicker free boot.
-   The specified system must boot up in native UEFI mode. CSM mode needs to be *disabled*.
-   The specified system must use a manually compiled kernel. Testing with a genkernel created kernel has not been completed.
-   When using older Ivy Bridge / Haswell / Broadwell based systems, it is recommended to use least [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] version 4.20.17 or higher due to a bug that actually causes the screen to go to stand-by mode and turn back on.
-   Kernel version 5.7.0 or higher does not honor the `i915.fastboot` kernel parameter [\[2\]](https://gitlab.freedesktop.org/drm/intel/-/issues/2972). Use the patches located on that bug report or use a version below 5.7.0.
-   This guide assumes the kernel has been configured correctly with the appropriate options for framebuffer support and such.
-   This guide assumes [/dev/sda1] has been configured as the [ESP](https://wiki.gentoo.org/wiki/ESP "ESP") ([/boot/efi]) partition. If it is not, then adjust the commands for the paths accordingly.

### [Knowledge]

-   A working Gentoo setup, preferably configured with EFI stub.
-   Intermediate to advanced knowledge about the Linux boot process.

### [Summary]

This tutorial assumes a working Gentoo setup is in place. This setup boots in (U)EFI mode using GRUB with CSM mode disabled and is using an Intel processor with it\'s own integrated graphics card.

## [Installing the required software]

In order to be able to successfully get everything working, the following software configuration will be needed.

### [Setting the correct USE flags for plymouth]

In order to set the correct use flags for plymouth, you\'ll need to take the following steps:

1.  Run the command:

`root `[`#`]`nano -w /etc/portage/package.use/plymouth`

1.  Add the following line to the file:

[FILE] **`/etc/portage/package.use/plymouth`**

    sys-boot/plymouth libkms pango

1.  1.  NOTE: `libkms` is the minimal requirement for the splash screen to show up. `pango` is required for interactivity (e.g.: This is necessary to have the ability to enter a [LUKS](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") password on a nice graphical screen). The `gtk` and `gdm` USE flags should be added respectively when using [GDM](https://wiki.gentoo.org/wiki/GDM "GDM") as the [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM") with GTK.
    2.  NOTE: Do *NOT* enable the `static-libs` USE flag. This USE flags will plymouth and may causes the package not to compile or display themes.
2.  Press [CTRL]+[o], and press [Enter] and press [CTRL]+[x] in order to save the file.
3.  Now install [[[sys-boot/plymouth]](https://packages.gentoo.org/packages/sys-boot/plymouth)[]]:

`root `[`#`]`emerge --ask --verbose sys-boot/plymouth`

1.  1.  Be sure to verify that the correct USE flags have been set.

### [Using dracut]

This has been tested to work by using the amd64 version of dracut. Using the latest available version of dracut from Portage is recommended.

Install the package:

`root `[`#`]`emerge --ask sys-kernel/dracut`

Then create the initramfs image via:

`root `[`#`]`dracut --hostonly`

More information is available on the [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") page.

### [Setting up EFI stub]

Usage of EFI stub can be found at [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") and [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"). Make the `i915.fastboot=1` kernel parameter is included, and include the path to the initranmfs generated by dracut, like so:

`root `[`#`]`efibootmgr -c -d /dev/sda -p 1 -L "Gentoo" -l '\vmlinuz-5.4.97-gentoo' -u '... i915.fastboot=1 initrd=\initramfs-5.4.97-gentoo.img ...'`

Finally, reboot and hope it works.

### [][Alternative: setting up systemd-boot (systemd users only)]

Alternatively systemd-boot can be configured for a flicker free boot. This seems to be an attractive option for users, who want to use a bootloader some configuration options (e.g. for dual-booting with Windows or another operating system).

Follow the steps from the [systemd/systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot") article to set up systemd-boot.

Next, configure the bootloader entry to look something like the following:

[FILE] **`/boot/efi/loader/entries/gentoo.conf`Default settings**

    title Gentoo Linux
    linux /EFI/Linux/vmlinuz
    initrd /EFI/Linux/initrd.img
    options [...] i915.fastboot=1 quiet splash

## [See also]

-   [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") --- an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure and aims to have as little as possible hard-coded into the initramfs.
-   [Plymouth](https://wiki.gentoo.org/wiki/Plymouth "Plymouth") --- a [bootsplash](https://en.wikipedia.org/wiki/bootsplash "wikipedia:bootsplash") used to show splash screens during system boot and shutdown.
-   [systemd/systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot") --- a minimal [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot manager.

## [External References]

-   [Hans de Goede - Flicker Free Boot FAQ](https://hansdegoede.livejournal.com/20632.html)
-   [Fedora - Flicker Free Boot project page](https://fedoraproject.org/wiki/Changes/FlickerFreeBoot)
-   [Arch Linux - plymouth Wiki page](https://wiki.archlinux.org/index.php/plymouth)