This page contains [[changes](https://wiki.gentoo.org/index.php?title=Installkernel&oldid=1407896&diff=1435403)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Installkernel/fr "Installkernel/fr (2% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Installkernel/hu "Installkernel (88% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Installkernel/ja "Installkernel (91% translated)")

**Resources**

[[]][GitHub](https://github.com/projg2/installkernel-gentoo)

**Installkernel** is a collection of scripts to automatically install new [kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel") and update [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") configuration.

Additional automation plugins, for example:

-   generate an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs")
-   generate a [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image")
-   update the bootloader configuration

are installed and/or enabled via the USE flags on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] as shown below:

## Contents

-   [[1] [Quick start]](#Quick_start)
-   [[2] [Implementations]](#Implementations)
-   [[3] [Systemd\'s kernel-install]](#Systemd.27s_kernel-install)
    -   [[3.1] [Configuration]](#Configuration)
        -   [[3.1.1] [layout]](#layout)
            -   [[3.1.1.1] [compat]](#compat)
            -   [[3.1.1.2] [efistub]](#efistub)
            -   [[3.1.1.3] [grub]](#grub)
            -   [[3.1.1.4] [bls]](#bls)
            -   [[3.1.1.5] [uki]](#uki)
        -   [[3.1.2] [initrd_generator]](#initrd_generator)
        -   [[3.1.3] [uki_generator]](#uki_generator)
    -   [[3.2] [kernel-install commands]](#kernel-install_commands)
        -   [[3.2.1] [kernel-install add]](#kernel-install_add)
        -   [[3.2.2] [kernel-install remove]](#kernel-install_remove)
        -   [[3.2.3] [kernel-install inspect]](#kernel-install_inspect)
        -   [[3.2.4] [kernel-install list]](#kernel-install_list)
        -   [[3.2.5] [kernel-install add-all]](#kernel-install_add-all)
    -   [[3.3] [Runtime overrides]](#Runtime_overrides)
    -   [[3.4] [Customization]](#Customization)
    -   [[3.5] [Descriptions of plugin scripts]](#Descriptions_of_plugin_scripts)
-   [[4] [Debian\'s installkernel]](#Debian.27s_installkernel)
    -   [[4.1] [Configuration]](#Configuration_2)
        -   [[4.1.1] [layout]](#layout_2)
            -   [[4.1.1.1] [efistub]](#efistub_2)
            -   [[4.1.1.2] [uki]](#uki_2)
        -   [[4.1.2] [initrd_generator]](#initrd_generator_2)
        -   [[4.1.3] [uki_generator]](#uki_generator_2)
    -   [[4.2] [Runtime overrides]](#Runtime_overrides_2)
    -   [[4.3] [Customization]](#Customization_2)
    -   [[4.4] [Descriptions of plugin scripts]](#Descriptions_of_plugin_scripts_2)
-   [[5] [Install chroot check]](#Install_chroot_check)
    -   [[5.1] [Dracut]](#Dracut)
        -   [[5.1.1] [Set root UUID]](#Set_root_UUID)
        -   [[5.1.2] [Disable hostonly_cmdline]](#Disable_hostonly_cmdline)
        -   [[5.1.3] [Blank /etc/cmdline]](#Blank_.2Fetc.2Fcmdline)
    -   [[5.2] [UgRD]](#UgRD)
-   [[6] [USE configuration to boot layout mapping]](#USE_configuration_to_boot_layout_mapping)
    -   [[6.1] [Systemd kernel-install (USE=+systemd)]](#Systemd_kernel-install_.28USE.3D.2Bsystemd.29)
        -   [[6.1.1] [Layouts with GRUB]](#Layouts_with_GRUB)
            -   [[6.1.1.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images)
        -   [[6.1.2] [Layouts with systemd-boot]](#Layouts_with_systemd-boot)
            -   [[6.1.2.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_2)
        -   [[6.1.3] [Layouts with rEFInd]](#Layouts_with_rEFInd)
            -   [[6.1.3.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_3)
        -   [[6.1.4] [Layouts without GRUB/systemd-boot/rEFInd (other bootloaders)]](#Layouts_without_GRUB.2Fsystemd-boot.2FrEFInd_.28other_bootloaders.29)
            -   [[6.1.4.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_4)
    -   [[6.2] [Traditional installkernel (USE=-systemd)]](#Traditional_installkernel_.28USE.3D-systemd.29)
        -   [[6.2.1] [Layouts with GRUB]](#Layouts_with_GRUB_2)
            -   [[6.2.1.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_5)
        -   [[6.2.2] [Layouts with rEFInd]](#Layouts_with_rEFInd_2)
            -   [[6.2.2.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_6)
        -   [[6.2.3] [Layouts without GRUB/systemd-boot/rEFInd (other bootloaders)]](#Layouts_without_GRUB.2Fsystemd-boot.2FrEFInd_.28other_bootloaders.29_2)
            -   [[6.2.3.1] [Layouts with Unified Kernel Images]](#Layouts_with_Unified_Kernel_Images_7)
-   [[7] [See also]](#See_also)

## [Quick start]

This wiki page provides a complete overview of the capabilities and options offered by the Installkernel ecosystem; however, this may be an overwhelming amount of information which is not relevant for the vast majority of users. Thus, a briefer summary is provided here.

At the most basic level [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] is set up similar to packages that one would otherwise find in the `app-alternatives/` category meaning that the intention is for the user to enable or disable certain USE flags based on the desired configuration and then emerge the package. The package will take care of setting up the appropriate configuration, installing the required scripts, and pulling in the necessary dependencies. Only users who wish to use unsupported, advanced, or otherwise custom configurations might need to dig deeper and write their own configuration files or scripts; for those users, the full documentation of the Gentoo installkernel ecosystem is provided in the remaining sections.

For example:

-   A user who opts for a simple and classic setup with [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") as the bootloader and [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") as the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") generator should enable the [[[grub]](https://packages.gentoo.org/useflags/grub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags.
-   A user who instead wishes to use [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot") without any [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") should enable only the [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag.
-   A user who does not wish to use any [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") and instead would like to boot directly from [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") into an [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") generated with [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and containing an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") generated with [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") should enable the [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], and [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags.

\
A full overview of the available USE flags is provided below.

### [USE flags for] [sys-kernel/installkernel](https://packages.gentoo.org/packages/sys-kernel/installkernel) [[]] [Gentoo fork of installkernel script from debianutils]

  --------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------
  [`dracut`](https://packages.gentoo.org/useflags/dracut)               Generate an initramfs or UKI on each kernel installation
  [`efistub`](https://packages.gentoo.org/useflags/efistub)             EXPERIMENTAL: Update UEFI configuration on each kernel installation
  [`grub`](https://packages.gentoo.org/useflags/grub)                   Re-generate grub.cfg on each kernel installation, used grub.cfg is overridable with GRUB_CFG env var
  [`refind`](https://packages.gentoo.org/useflags/refind)               Install a Gentoo icon for rEFInd alongside the (unified) kernel image, used icon is overridable with REFIND_ICON env var
  [`systemd`](https://packages.gentoo.org/useflags/systemd)             Use systemd\'s kernel-install to install kernels, overridable with SYSTEMD_KERNEL_INSTALL env var
  [`systemd-boot`](https://packages.gentoo.org/useflags/systemd-boot)   Use systemd-boot\'s native layout by default
  [`ugrd`](https://packages.gentoo.org/useflags/ugrd)                   Generate an initramfs using UGRD on each kernel installation
  [`uki`](https://packages.gentoo.org/useflags/uki)                     Install UKIs to ESP/EFI/Linux for EFI stub booting and/or bootloaders with support for auto-discovering UKIs
  [`ukify`](https://packages.gentoo.org/useflags/ukify)                 Build an UKI with systemd\'s ukify on each kernel installation
  --------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 19:15] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Warning**\
Some nonsensical combinations of USE flags are blocked via [REQUIRED_USE](https://wiki.gentoo.org/index.php?title=REQUIRED_USE&action=edit&redlink=1 "REQUIRED USE (page does not exist)") constraints. For example, one cannot use more than one [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") generator, and [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot") requires the use of systemd\'s kernel-install via the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag. Of special note though is that enabling multiple USE flags for bootloaders is **not** blocked. This is because it is sometimes, but not always, possible to sucessfully configure a system to support booting with multiple bootloaders in parralel. For example, one can sucesfully combine [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] with [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], but only if [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is used as well. Such configurations are not supported officially and as such users will run into weird egde cases. Bottom line: **do not blindly enable USE flags**!.

## [Implementations]

The package [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] provides two different paths of managing kernel installation. The first is [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")\'s [kernel-install], the second is the more traditional [installkernel] originating from Debian. Gentoo strives to ensure a rough feature parity between both implementations.

The [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag changes which implementation is used by default, this default may be overridden with the `SYSTEMD_KERNEL_INSTALL` environment variable or with the `--(no-)systemd` argument. In general systemd\'s [kernel-install] is the more modern implementation, and it is therefore recommended and enabled by default on systemd profiles. Users who do not wish to use systemd tooling may fallback on Gentoo\'s Debian-based [installkernel] implementation instead.

## [][Systemd\'s kernel-install]

To select this installation method, enable the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag or set `SYSTEMD_KERNEL_INSTALL=1` in the environment.

[FILE] **`/etc/portage/package.use/installkernel`**

    sys-kernel/installkernel systemd

`root `[`#`]`emerge --ask sys-kernel/installkernel`

Or

[FILE] **`/etc/env.d/99systemd-kernel-install`**

    SYSTEMD_KERNEL_INSTALL=1

`root `[`#`]`env-update`

** Tip**\
Systemd\'s [kernel-install] can not only install kernels ([kernel-install add]), it can also handle kernel removal ([kernel-install remove]). If [kernel-install] is installed it will automatically be called by [eclean-kernel](https://wiki.gentoo.org/wiki/Kernel/Removal#Using_eclean-kernel "Kernel/Removal").

### [Configuration]

Configuration of [kernel-install] is done in [/etc/kernel/install.conf] and [/usr/lib/kernel/install.conf], where the former takes precedence over the latter. Three configuration options can be set:

[FILE] **`/etc/kernel/install.conf`**

    layout=
    initrd_generator=
    uki_generator=

The default [/usr/lib/kernel/install.conf] configuration file is provided by [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]. Of course the configuration may also be changed manually in [/etc/kernel/install.conf].

** Warning**\
[/etc/kernel/install.conf] overrides [/usr/lib/kernel/install.conf] as a whole! When [/etc/kernel/install.conf] exists all settings in [/usr/lib/kernel/install.conf] are ignored. Therefore, when the intention is to only override one setting, the user must also copy the other settings which should not be overridden from [/usr/lib/kernel/install.conf] to [/etc/kernel/install.conf].

#### [layout]

Upstream systemd supports the `Boot Loader Specification` type 1 ([layout=bls]) and type 2 ([layout=uki]) layout. The type 1 layout is used by [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot"), the type 2 layout is intended to be used for Unified Kernel Images and is supported by [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), systemd-boot and [refind](https://wiki.gentoo.org/wiki/Refind "Refind").

Gentoo also supports a more traditional layout intended for use with GRUB ([layout=grub]), which is very similar (but not identical) to the layout used by Debian\'s installkernel as described above. This layout may also be used in other cases where a more basic and traditional layout is desired. To use GRUB in combination with [Unified Kernel Images](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image"), use the [uki] layout instead.

When the [[[grub]](https://packages.gentoo.org/useflags/grub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], and [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are all disabled, the kernels will be installed in a layout that is mostly backwards compatible with Debian\'s installkernel ([layout=compat]).

When multiple layout-specifying flags are enabled, the `uki` layout (enabled by the [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag) takes precedence over the `bls` layout (enabled by the [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag), which in turn takes precedence over the `grub` layout (enabled by the [[[grub]](https://packages.gentoo.org/useflags/grub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag).

An overview of each layout is shown in the sections below:

##### [compat]

The compat layout is very similar, but not identical, to the layout used by Debian\'s traditional installkernel:

[CODE] **compat layout**

    /boot/initramfs-x.y.z-gentoo-dist.img          # If USE=dracut (or other initramfs generator)
    /boot/kernel-x.y.z-gentoo-dist

##### [efistub]

The efistub layout is identical to the compat layout, but relocated to the [EFI system partition](https://wiki.gentoo.org/wiki/EFI_system_partition "EFI system partition") for [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") booting. The kernel image gains the `.efi` suffix as some firmware vendors enforce this:

[CODE] **efistub layout**

    /$/EFI/Gentoo/initramfs-x.y.z-gentoo-dist.img      # If USE=dracut (or other initramfs generator)
    /$/EFI/Gentoo/kernel-x.y.z-gentoo-dist.efi

** Warning**\
Whether or not (automated) EFI stub booting works is highly dependent on the UEFI vendor. This is considered an advanced and experimental feature.

##### [grub]

The grub layout is identical to the `compat` layout, with an added [grub.cfg], used by [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"):

[CODE] **grub layout**

    /boot/grub/grub.cfg
    /boot/initramfs-x.y.z-gentoo-dist.img           # If USE=dracut (or other initramfs generator)
    /boot/kernel-x.y.z-gentoo-dist

##### [bls]

The `Bootloader Specification Type 1` or `bls` layout, used by [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot"):

[CODE] **bls layout**

    /$/gentoo/x.y.z-gentoo-dist/initrd          # If USE=dracut (or other initramfs generator)
    /$/gentoo/x.y.z-gentoo-dist/linux
    /$/loader/entries/gentoo-x.y.z-gentoo-dist.conf

##### [uki]

The `Bootloader Specification Type 2` or `uki` layout:

[CODE] **uki layout**

    /boot/grub/grub.cfg                               # If USE=grub

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

#### [initrd_generator]

This setting controls which plugin should be used to generate the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). Currently the only package that installs such a plugin is [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") from [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]]. This setting is exposed to the plugins as `$`. When the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled, this setting is automatically set to `dracut`. Otherwise this setting is automatically set to `none`.

#### [uki_generator]

This setting controls which plugin should be used to generate the Unified Kernel Image. Currently two packages provide such a plugin: [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") (via the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] and [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]]). This setting is exposed to the plugins as `$` When the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled, this setting is automatically set to `ukify`. When the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is disabled, but the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are enabled, this setting is automatically set to `dracut`. Otherwise this setting is automatically set to `none`.

### [kernel-install commands]

Below an overview is provided of the available commands in systemd\'s [kernel-install].

#### [kernel-install add]

(Re-)installs a kernel version. This command is called by [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] if the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled.

`root `[`#`]`kernel-install [OPTIONS...] add KERNEL-VERSION KERNEL-IMAGE [INITRD-FILE...]`

#### [kernel-install remove]

Uninstalls a kernel version. This command is called by [[[app-admin/eclean-kernel]](https://packages.gentoo.org/packages/app-admin/eclean-kernel)[]] if it is available.

`root `[`#`]`kernel-install [OPTIONS...] remove KERNEL-VERSION`

#### [kernel-install inspect]

Prints an overview of parameters that will be used when installing a kernel version.

`root `[`#`]`kernel-install [OPTIONS...] inspect [KERNEL-VERSION] [KERNEL-IMAGE] [INITRD-FILE...]`

#### [kernel-install list]

Prints an overview of all installed kernel versions. Meaning all kernel versions for which a directory is present in [/lib/modules].

`root `[`#`]`kernel-install [OPTIONS...] list`

#### [kernel-install add-all]

(Re-)installs all kernel versions. Iterates [kernel-install add] over each kernel for which a [vmlinuz] file is present in the associated [/lib/modules] directory.

`root `[`#`]`kernel-install [OPTIONS...] add-all`

### [Runtime overrides]

When the dracut and ukify plugins are enabled (i.e. the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and/or [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are enabled) they may be skipped at runtime by overriding the default configuration provided by [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] at [/usr/lib/kernel/install.conf] with a custom configuration at [/etc/kernel/install.conf]. This may be useful on systems that have both the distribution kernels installed and manually configured kernels where the former enforces the enablement of the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag but the latter might not require an initramfs at all.

For example:

[FILE] **`/etc/kernel/install.conf`**

    layout=compat
    initrd_generator=none
    uki_generator=none

Note that this override will apply to all installed kernels. It is also possible to specify several different configurations and switch between them at runtime using the `KERNEL_INSTALL_CONF_ROOT` environment variable.

For example:

[FILE] **`/etc/manual-kernel/install.conf`**

    layout=compat
    initrd_generator=none
    uki_generator=none

`root `[`#`]`KERNEL_INSTALL_CONF_ROOT=/etc/manual-kernel make install`

Another method of overriding the default kernel installation is to use the `KERNEL_INSTALL_PLUGINS` environment variable. When this variable is set, only the specified plugins are run.

For example:

`root `[`#`]`KERNEL_INSTALL_PLUGINS="90-compat.install 90-loaderentry.install 90-uki-copy.install" make install`

### [Customization]

Custom plugins, which for example, generate a initramfs or UKI, or update the bootloader configuration, may be installed into [/etc/kernel/install.d]. An initramfs plugin should install a file named [initrd] on the [\$. A UKI plugin should install a file named [uki.efi] in the [\$. All plugin files must have the [.install] suffix. Plugins in [/etc/kernel/install.d] override default plugins in [/usr/lib/kernel/install.d] with the same name.

### [Descriptions of plugin scripts]

In exection order, the `install.d` plugins

[/usr/lib/kernel/install.d/00-00machineid-directory.install]

<!-- -->

[/usr/lib/kernel/install.d/05-check-config.install]

<!-- -->

[/usr/lib/kernel/install.d/10-copy-prebuilt.install]

<!-- -->

[/usr/lib/kernel/install.d/35-amd-microcode-systemd.install]

<!-- -->

[/usr/lib/kernel/install.d/35-intel-microcode-systemd.install]

<!-- -->

[/usr/lib/kernel/install.d/40-dkms.install]

<!-- -->

[/usr/lib/kernel/install.d/50-depmod.install]

<!-- -->

[/usr/lib/kernel/install.d/52-dracut.install]

<!-- -->

[/usr/lib/kernel/install.d/52-ugrd.install]

<!-- -->

[/usr/lib/kernel/install.d/85-check-diskspace.install]

<!-- -->

[/usr/lib/kernel/install.d/90-compat.install]

<!-- -->

[/usr/lib/kernel/install.d/90-loaderentry.install]

<!-- -->

[/usr/lib/kernel/install.d/90-runlilo.install]

<!-- -->

[/usr/lib/kernel/install.d/90-uki-copy.install]

<!-- -->

[/usr/lib/kernel/install.d/90-zz-update-static.install]

<!-- -->

[/usr/lib/kernel/install.d/91-grub-mkconfig.install]

<!-- -->

[/usr/lib/kernel/install.d/91-sbctl.install]

<!-- -->

[/usr/lib/kernel/install.d/95-efistub-kernel-bootcfg.install]

<!-- -->

[/usr/lib/kernel/install.d/95-refind-copy-icon.install]

<!-- -->

[/usr/lib/kernel/install.d/99-write-log.install]

## [][Debian\'s installkernel]

To select this installation method, disable the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag or set `SYSTEMD_KERNEL_INSTALL=0` in the environment.

[FILE] **`/etc/portage/package.use/installkernel`**

    sys-kernel/installkernel -systemd

`root `[`#`]`emerge --ask sys-kernel/installkernel`

Or

[FILE] **`/etc/env.d/99no-systemd-kernel-install`**

    SYSTEMD_KERNEL_INSTALL=0

`root `[`#`]`env-update`

** Note**\
Since the traditional [installkernel] installs the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") and/or [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") (UKI) at the same place as the kernel image in the kernel sources tree, these files may be left-over when switching from a configuration with initramfs and/or Unified Kernel Image to one without. In this situation these files may have to be cleaned up manually from the kernel source tree to ensure they are not picked up and installed by [installkernel].

### [Configuration]

Configuration of [kernel-install] is done in [/etc/kernel/install.conf] and [/usr/lib/kernel/install.conf], where the former takes precedence over the latter. Three configuration options can be set:

[FILE] **`/etc/kernel/install.conf`**

    layout=
    initrd_generator=
    uki_generator=

The default [/usr/lib/kernel/install.conf] configuration file is provided by [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]. Of course the configuration may also be changed manually in [/etc/kernel/install.conf].

** Warning**\
[/etc/kernel/install.conf] overrides [/usr/lib/kernel/install.conf] as a whole! When [/etc/kernel/install.conf] exists, all settings in [/usr/lib/kernel/install.conf] are ignored. Therefore, when the intention is to only override one setting, the user must also copy the other settings which should not be overridden from [/usr/lib/kernel/install.conf] to [/etc/kernel/install.conf].

#### [layout]

Debian\'s traditional installkernel installs the kernel and initramfs or Unified Kernel Image in a layout that looks like this:

[CODE] **traditional layout**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/grub/grub.cfg                               # If USE=grub
    /boot/initramfs-x.y.z-gentoo-dist.img             # If USE=dracut (or another initramfs generator)
    /boot/vmlinuz-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist.png               # If USE=refind

##### [efistub]

If the [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled, then the install tree is relocated to the EFI System Partition (ESP) and the kernel image gains the `.efi` suffix.

[CODE] **efistub layout**

    /$/EFI/Gentoo/System.map-x.y.z-gentoo-dist
    /$/EFI/Gentoo/config-x.y.z-gentoo-dist
    /$/EFI/Gentoo/initramfs-x.y.z-gentoo-dist.img            # If USE=dracut (or another initramfs generator)
    /$/EFI/Gentoo/vmlinuz-x.y.z-gentoo-dist.efi

##### [uki]

If the [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled, then generated Unified Kernel Image is installed to the [EFI/Linux] directory on the EFI System Partition (ESP).

[CODE] **uki layout**

    /boot/grub/grub.cfg                                          # If USE=grub

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png               # If USE=refind

#### [initrd_generator]

This setting controls which utility should be used to generate the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). This setting is exposed to the plugins as `$`.

The following options are available:

-   [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] - Use Dracut to generate an initramfs.
-   [[[ugrd]](https://packages.gentoo.org/useflags/ugrd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] - Use [UgRD](https://wiki.gentoo.org/wiki/UgRD "UgRD") to generate an initramfs.
-   `none` - Do not generate an initramfs on kernel installs.

<!-- -->

    When the dracut USE flag is enabled, this setting is automatically set to dracut. This setting is otherwise automatically set

#### [uki_generator]

This setting controls which plugin should be used to generate the Unified Kernel Image. Currently two packages provide such a plugin: [[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") (via the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] and [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]]). This setting is exposed to the plugins as `$` When the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled, this setting is automatically set to `ukify`. When the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is disabled, but the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are enabled, this setting is automatically set to `dracut`. Otherwise this setting is automatically set to `none`.

### [Runtime overrides]

When the dracut and ukify plugins are installed (i.e. the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and/or [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are enabled) they may be skipped at runtime using the `INSTALLKERNEL_INITRD_GENERATOR` and `INSTALLKERNEL_UKI_GENERATOR` environment variables. This may be useful on systems that have both the distribution kernels installed and manually configured kernels where the former enforces the enabling of the [[[dracut]](https://packages.gentoo.org/useflags/dracut)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag but the latter might not require an initramfs at all.

`root `[`#`]`INSTALLKERNEL_INITRD_GENERATOR=none INSTALLKERNEL_UKI_GENERATOR=none make install`

Alternatively, these settings may be set permanently using [/etc/kernel/install.conf]:

[FILE] **`/etc/kernel/install.conf`**

    layout=compat
    initrd_generator=none
    uki_generator=none

Note that this override will apply to all installed kernels. It is also possible to specify several different configurations and switch between them at runtime using the `INSTALLKERNEL_CONF_ROOT` environment variable.

For example:

[FILE] **`/etc/manual-kernel/install.conf`**

    layout=compat
    initrd_generator=none
    uki_generator=none

`root `[`#`]`INSTALLKERNEL_CONF_ROOT=/etc/manual-kernel make install`

Another method of overriding the default kernel installation is to use the `INSTALLKERNEL_PREINST_PLUGINS` and `INSTALLKERNEL_POSTINST_PLUGINS` environment variables. When these variables are set, only the specified plugins are run.

For example:

`root `[`#`]`INSTALLKERNEL_POSTINST_PLUGINS="91-grub-mkconfig.install" make install`

### [Customization]

Custom plugins, which for example, generate [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") or [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") (UKI) may be installed into [/etc/kernel/preinst.d]. An initramfs plugin should install a file named [initrd] on the [\$, and it should respect the `INSTALLKERNEL_INITRD_GENERATOR` environment variable. A UKI plugin should install a file named [uki.efi] on the [\$ and it should respect the `INSTALLKERNEL_UKI_GENERATOR` environment variable.

Additionally custom plugins, which for example, update the bootloader configuration may be installed in [/etc/kernel/postinst.d].

Plugins in [/etc/kernel/preinst.d] or [/etc/kernel/postinst.d] override default plugins in [/usr/lib/kernel/preinst.d] and [/usr/lib/kernel/postinst.d] with the same name.

### [Descriptions of plugin scripts]

In exection order, the `preinst.d` plugins

[/usr/lib/kernel/preinst.d/35-amd-microcode.install]

<!-- -->

[/usr/lib/kernel/preinst.d/35-intel-microcode.install]

<!-- -->

[/usr/lib/kernel/preinst.d/52-dracut.install]

<!-- -->

[/usr/lib/kernel/preinst.d/52-ugrd.install]

<!-- -->

[/usr/lib/kernel/preinst.d/60-ukify.install]

<!-- -->

[/usr/lib/kernel/preinst.d/99-check-diskspace.install]

In execution order, the `postinst.d` plugins

[/usr/lib/kernel/postinst.d/40-dkms.install]

<!-- -->

[/usr/lib/kernel/postinst.d/91-grub-mkconfig.install]

<!-- -->

[/usr/lib/kernel/postinst.d/95-efistub-uefi-mkconfig.install]

<!-- -->

[/usr/lib/kernel/postinst.d/95-refind-copy-icon.install]

<!-- -->

[/usr/lib/kernel/postinst.d/99-write-log.install]

<!-- -->

[/usr/lib/kernel/postinst.d/90-runlilo.install]

## [Install chroot check]

Bootloaders such as [systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot") and [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") use the kernel arguments of the running system as set in [/proc/cmdline] by default. While this is useful on an already installed system, when installing a kernel from a chroot, it means the system will use the host systems boot options which often won\'t be useful to the system that is now being set up. An example of this is when using Gentoo live media, the bootloaders will inherit the live media\'s kernel arguments and use them on the next boot. As a result the system will try and fail to load the squashfs image of the live media.

Many users don\'t know this issue exists because other distributions hide this from the user. Gentoo on the other hands supports such a wide variety of configuration that it is not possible to make assumptions about the desired kernel command line.

Therefore installkernel provides a sanity check for users which will cause a fatal error if a chroot was detected without an explicitly configured kernel command line. The user is asked to create the file [/etc/cmdline] to overwrite the assumption made by bootloaders.

Below are some of ways to satisfy this check:

** Important**\
Only one selection is required in the following subsection, if unsure of which to use then go with the first listed for now. It\'s always possible to switch at a later date if required.

### [Dracut]

#### [Set root UUID]

The Handbook recommends setting the root UUID inside a config file in [/etc/dracut.conf.d].

First, the [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") config directory must be created if it does not already exist:

`root `[`#`]`mkdir /etc/dracut.conf.d`

With that directory created, [blkid] can be used to get the filesystem UUID of the root filesystem:

`user `[`$`]`blkid`

/dev/sda3: UUID=\"2122cd72-94d7-4dcc-821e-3705926deecc\"

Using this UUID as an example, where the root filesystem is on [/dev/sda3] with the UUID `2122cd72-94d7-4dcc-821e-3705926deecc`, the following configuration can be used:

[FILE] **`/etc/dracut.conf.d/00-installkernel.conf`**

    kernel_cmdline=" root=UUID=2122cd72-94d7-4dcc-821e-3705926deecc " # Note leading and trailing spaces

#### [Disable hostonly_cmdline]

By default, Dracut uses `hostonly_cmdline` which configures the initramfs cmdline based on the current [/proc/cmdline]. When installing, this will contain info about the livecd itself and not the chroot, which can cause issues. To disable this:

[FILE] **`/etc/dracut.conf.d/00-hostonly.conf`**

    hostonly_cmdline="no"

#### [][Blank /etc/cmdline]

For some systems no config at all is needed, this can be achieved by creating a blank [/etc/cmdline] file.

`root `[`#`]`touch /etc/cmdline`

### [UgRD]

By design, [UgRD](https://wiki.gentoo.org/wiki/UgRD "UgRD") does not require manual config for root info, so this check can generally be ignored.

To use UgRD instead of dracut:

[FILE] **`/etc/portage/package.use/installkernel`**

    sys-kernel/installkernel ugrd -dracut

`root `[`#`]`emerge --ask --verbose --oneshot sys-kernel/installkernel`

## [USE configuration to boot layout mapping]

The code boxes below maps possible [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] USE configurations to how the kernel and related files will be installed. It may be useful for users who are unsure which USE configuration suits their setup. `ESP` refers to the mount point of the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") which may be [/efi], [/boot], [/boot/efi] or [/boot/EFI]. `generic-uki` refers to the [[[generic-uki]](https://packages.gentoo.org/useflags/generic-uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on the [Distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel").

** Tip**\
For all layouts (except for the `bls type 1` layout for systemd-boot) [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] supports updating an unversioned symlink or file at the same location as the installed kernel images. For example, if the kernel images are installed as [/efi/EFI/Gentoo/kernel-x.y.z-gentoo-dist.efi] then [/efi/EFI/Gentoo/kernel.efi] will be updated every time a kernel is installed if this file or symlink exists.

### [][Systemd kernel-install (USE=+systemd)]

#### [Layouts with GRUB]

Plain kernel image installation.

[CODE] **-generic-uki -dracut systemd -systemd-boot -uki -ukify grub -refind**

    /boot/grub/grub.cfg
    /boot/kernel-x.y.z-gentoo-dist

Plain kernel image installation, with initramfs generated by dracut.

[CODE] **-generic-uki dracut systemd -systemd-boot -uki -ukify grub -refind**

    /boot/grub/grub.cfg
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist

Plain kernel image installation, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot -uki -ukify grub -refind**

    /boot/grub/grub.cfg
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, uki is generated with ukify and is then installed to the ESP.

[CODE] **-generic-uki -dracut systemd -systemd-boot uki ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki -ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and includes a initramfs generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot uki -ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

#### [Layouts with systemd-boot]

Plain kernel image installation.

[CODE] **-generic-uki -dracut systemd systemd-boot -uki -ukify -grub -refind**

    /$/gentoo/x.y.z-gentoo-dist/linux
    /$/loader/entries/gentoo-x.y.z-gentoo-dist.conf

Plain kernel image installation, with initramfs generated by dracut.

[CODE] **-generic-uki dracut systemd systemd-boot -uki -ukify -grub -refind**

    /$/gentoo/x.y.z-gentoo-dist/initrd
    /$/gentoo/x.y.z-gentoo-dist/linux
    /$/loader/entries/gentoo-x.y.z-gentoo-dist.conf

Plain kernel image installation, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd systemd-boot -uki -ukify -grub -refind**

    /$/gentoo/x.y.z-gentoo-dist/initrd
    /$/gentoo/x.y.z-gentoo-dist/linux
    /$/loader/entries/gentoo-x.y.z-gentoo-dist.conf

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, uki is generated with ukify and is then installed to the ESP.

[CODE] **-generic-uki -dracut systemd systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and includes a initramfs generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

#### [Layouts with rEFInd]

Plain kernel image installation with icon for rEFInd.

[CODE] **-generic-uki -dracut systemd -systemd-boot -uki -ukify -grub refind**

    /boot/kernel-x.y.z-gentoo-dist
    /boot/kernel-x.y.z-gentoo-dist.png

Plain kernel image installation, with a initramfs generated by dracut and icon for rEFInd.

[CODE] **-generic-uki dracut systemd -systemd-boot -uki -ukify -grub refind**

    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist
    /boot/kernel-x.y.z-gentoo-dist.png

Plain kernel image installation with icon for rEFInd, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot -uki -ukify -grub refind**

    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist
    /boot/kernel-x.y.z-gentoo-dist.png

##### [Layouts with Unified Kernel Images]

Unified kernel image installation with icon for rEFInd, uki is generated with ukify and is then installed to the ESP.

[CODE] **-generic-uki -dracut systemd -systemd-boot uki ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki -ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is generated with ukify and includes a initramfs generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot uki -ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

#### [][Layouts without GRUB/systemd-boot/rEFInd (other bootloaders)]

Plain kernel image installation.

[CODE] **-generic-uki -dracut systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/kernel-x.y.z-gentoo-dist

Plain kernel image installation, with a initramfs generated by dracut.

[CODE] **-generic-uki dracut systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist

Plain kernel image installation, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/kernel-x.y.z-gentoo-dist

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, uki is generated with ukify and is then installed to the ESP.

[CODE] **-generic-uki -dracut systemd -systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and includes a initramfs generated with dracut and is then installed to the ESP.

[CODE] **-generic-uki dracut systemd -systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut systemd -systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

### [][Traditional installkernel (USE=-systemd)]

#### [Layouts with GRUB]

Plain kernel image installation.

[CODE] **-generic-uki -dracut -systemd -systemd-boot -uki -ukify grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/grub/grub.cfg
    /boot/vmlinuz-x.y.z-gentoo-dist

Plain kernel image installation, with initramfs generated by dracut.

[CODE] **-generic-uki dracut -systemd -systemd-boot -uki -ukify grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/grub/grub.cfg
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist

Plain kernel image installation, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut -systemd -systemd-boot -uki -ukify grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/grub/grub.cfg
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, with an uki generated by dracut (`uki` has no effect since there is no unified kernel image).

[CODE] **-generic-uki dracut -systemd -systemd-boot uki -ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and is then copied to the ESP.

[CODE] **-generic-uki -dracut -systemd -systemd-boot uki ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and includes a initramfs generated with dracut and is then copied to the ESP.

[CODE] **-generic-uki dracut -systemd -systemd-boot uki ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is pregenerated by the distribution kernel package and is then copied to the ESP.

[CODE] **generic-uki -dracut -systemd -systemd-boot uki -ukify grub -refind**

    /boot/grub/grub.cfg

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

#### [Layouts with rEFInd]

Plain kernel image installation with icon for rEFInd.

[CODE] **-generic-uki -dracut -systemd -systemd-boot -uki -ukify -grub refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist.png

Plain kernel image installation, with a initramfs generated by dracut and icon for rEFInd.

[CODE] **-generic-uki dracut -systemd -systemd-boot -uki -ukify -grub refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist.png

Plain kernel image installation with icon for rEFInd, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut -systemd -systemd-boot -uki -ukify -grub refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist.png

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, with a initramfs generated by dracut.

[CODE] **-generic-uki dracut -systemd -systemd-boot uki -ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is generated with ukify and is then copied to the ESP.

[CODE] **-generic-uki -dracut -systemd -systemd-boot uki ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is generated with ukify and includes a initramfs generated with dracut and is then copied to the ESP.

[CODE] **-generic-uki dracut -systemd -systemd-boot uki ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

Unified kernel image installation with icon for rEFInd, uki is pregenerated by the distribution kernel package and is then copied to the ESP.

[CODE] **generic-uki -dracut -systemd -systemd-boot uki -ukify -grub refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi
    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.png

#### [][Layouts without GRUB/systemd-boot/rEFInd (other bootloaders)]

Plain kernel image installation.

[CODE] **-generic-uki -dracut -systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/vmlinuz-x.y.z-gentoo-dist

Plain kernel image installation, with a initramfs generated by dracut.

[CODE] **-generic-uki dracut -systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist

Plain kernel image installation, initramfs is pregenerated by the distribution kernel package.

[CODE] **generic-uki -dracut -systemd -systemd-boot -uki -ukify -grub -refind**

    /boot/System.map-x.y.z-gentoo-dist
    /boot/config-x.y.z-gentoo-dist
    /boot/initramfs-x.y.z-gentoo-dist.img
    /boot/vmlinuz-x.y.z-gentoo-dist

##### [Layouts with Unified Kernel Images]

Unified kernel image installation, with uki generated by dracut.

[CODE] **-generic-uki dracut -systemd -systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and is then copied to the ESP.

[CODE] **-generic-uki -dracut -systemd -systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is generated with ukify and includes a initramfs generated with dracut and is then copied to the ESP.

[CODE] **-generic-uki dracut -systemd -systemd-boot uki ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

Unified kernel image installation, uki is pregenerated by the distribution kernel package and is then copied to the ESP.

[CODE] **generic-uki -dracut -systemd -systemd-boot uki -ukify -grub -refind**

    /$/EFI/Linux/gentoo-x.y.z-gentoo-dist.efi

## [See also]

-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") --- a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures.
-   [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot") --- a minimal [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot manager.
-   [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")
-   [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") --- is used to prepare Linux systems during boot before the **init** process starts.
-   [Project:Distribution_Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") --- maintains sys-kernel/\*-kernel packages.