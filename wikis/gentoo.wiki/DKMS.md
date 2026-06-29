**Resources**

[[]][GitHub](https://github.com/dell/dkms)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support "wikipedia:Dynamic Kernel Module Support")

**DKMS** (Dynamic Kernel Module System) is a distribution agnostic framework for managing out-of-tree [kernel modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules").

DKMS supports:

-   Dynamically building and installing missing kernel modules at boot, via an [init system](https://wiki.gentoo.org/wiki/Init_system "Init system") service.
-   Building and installing out-of-tree kernel modules during installation of a new kernel, via an [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") hook.
-   Managing, building and installing out-of-tree kernel modules, via a command line utility.
-   Automatically [signing](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support") and/or compressing built kernel modules, as well as generating signing keys.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Kernel module signing]](#Kernel_module_signing)
    -   [[2.2] [Kernel module compression]](#Kernel_module_compression)
-   [[3] [Integration with Portage]](#Integration_with_Portage)
-   [[4] [Usage]](#Usage)

## [Installation]

To use DKMS, install the [[[sys-kernel/dkms]](https://packages.gentoo.org/packages/sys-kernel/dkms)[]] package:

`root `[`#`]`emerge --ask sys-kernel/dkms`

### [USE flags for] [sys-kernel/dkms](https://packages.gentoo.org/packages/sys-kernel/dkms) [[]] [Dynamic Kernel Module Support]

  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`systemd`](https://packages.gentoo.org/useflags/systemd)   Enable use of systemd-specific libraries and features like socket activation or session tracking
  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 09:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

DKMS is configured via [/etc/dkms/framework.conf]. Every option is extensively documented in the configuration file, in the subsections below we highlight the options for kernel module signing and compression.

### [Kernel module signing]

DKMS will automatically sign built kernel modules if the target kernel supports this. By default it will use the key and certificate pair at [/var/lib/dkms/mok.key] and [/var/lib/dkms/mok.pub] respectively. Another key may be used by specifying the `mok_signing_key` and `mok_certificate` variables in [/etc/dkms/framework.conf] as shown below:

[FILE] **`/etc/dkms/framework.conf`configuring kernel module signing in DKMS**

    # Location of the key and certificate files used for Secure boot. $kernelver
    # can be used in path to represent the target kernel version.
    #
    # NOTE: If any of the files specified by `mok_signing_key` and
    # `mok_certificate` are non-existant, dkms will re-create both files.
    #
    # mok_signing_key can also be a "pkcs11:..." string for PKCS#11 engine, as
    # long as the sign_file program supports it.
    # (default: /var/lib/dkms):
    mok_signing_key=/root/kernel_key.pem
    mok_certificate=/root/kernel_key.pem

** Tip**\
As of version 3.1.6 of [[[sys-kernel/dkms]](https://packages.gentoo.org/packages/sys-kernel/dkms)[]], DKMS recognizes and automatically uses [Portage\'s](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel#Signed_kernel_modules "Project:Distribution Kernel") `MODULES_SIGN_KEY` and `MODULES_SIGN_CERT` if set in the environment or in [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"). If these variables are not set, then DKMS tries to extract the value of `CONFIG_MODULE_SIG_KEY` from the target kernel configuration. This means that for most cases it is not required to configure kernel module signing for DKMS separately.

### [Kernel module compression]

DKMS will automatically compress kernel modules if the module install tree for the target kernel ([/lib/modules/KV_FULL]) contains compressed kernel modules. The used compression options can be customized as shown below.

[FILE] **`/etc/dkms/framework.conf`configuring kernel module compression in DKMS**

    # Compression settings DKMS uses when compressing modules. The defaults are
    # used, for reasonable compression times. One might instead wish to use
    # maximum compression, at the expense of speed when compressing.
    compress_gzip_opts="-6"
    compress_xz_opts="--check=crc32 --lzma2=dict=1MiB -6"
    compress_zstd_opts="-q -T0 -3"

## [Integration with Portage]

[] This article is a **work in progress**; treat its contents with caution - [Nowa](https://wiki.gentoo.org/wiki/User:Nowa "User:Nowa") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Nowa&action=edit&redlink=1 "User talk:Nowa (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/Nowa "Special:Contributions/Nowa")).

** Note**\
DKMS support is currently only available in the [\"natinst\" repository](https://github.com/Nowa-Ammerlaan/natinst). Packages provided there may be out of sync with the main Gentoo repository. The repository may be enabled with:

`root `[`#`]`eselect repository enable natinst`

Integration with [portage](https://wiki.gentoo.org/wiki/Portage "Portage") is provided by the global [[[dkms]](https://packages.gentoo.org/useflags/dkms)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). When this flag is enabled, the affected packages will install the sources required to build the kernel module(s) to a subdirectory of [/usr/src/], and then register the contained kernel modules with DKMS. Portage will then instruct DKMS to build and install the kernel modules for the [currently selected kernel version](https://wiki.gentoo.org/wiki/Kernel/Upgrade#Default:_Setting_the_link_with_eselect "Kernel/Upgrade"). To enable the [[[dkms]](https://packages.gentoo.org/useflags/dkms)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for all packages containing kernel modules, set the flag in [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"):

[FILE] **`/etc/portage/make.conf`Enabling DKMS**

    USE="dkms"

To trigger a rebuild and reinstallation of a kernel module provided by a dkms-enabled package for the currently running kernel, one can use the `--config` argument for `emerge`:

`root `[`#`]`emerge --config example/package`

** Note**\
When the out-of-tree kernel module management is outsourced to DKMS by enabling the [[[dkms]](https://packages.gentoo.org/useflags/dkms)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") portage will not itself build and install any kernel modules. As such any generated [binary packages](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") will not actually contain any built kernel modules, and will instead contain the kernel module sources and the associated DKMS configuration file(s). An additional consequence of this is that the [[[modules-compress]](https://packages.gentoo.org/useflags/modules-compress)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[modules-sign]](https://packages.gentoo.org/useflags/modules-sign)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are ineffective, see the [configuration](https://wiki.gentoo.org/wiki/DKMS#Configuration "DKMS") section above for instructions on how to configure kernel module compression and signing with DKMS instead.

## [Usage]

DKMS integration with [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") is setup automatically. To additionally also build and install missing kernel modules at boot, enable the DKMS init service:

`root `[`#`]`systemctl enable --now dkms`

To automatically build and install all DKMS registered kernel modules for the currently running kernel:

`root `[`#`]`dkms autoinstall`

To `autoinstall` for a different kernel version instead, add the `-k` argument followed by the target kernel version:

`root `[`#`]`dkms autoinstall -k 6.x.y-gentoo-dist`