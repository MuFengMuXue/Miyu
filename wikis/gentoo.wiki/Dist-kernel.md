**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel")][Project](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel")

[[]][Kernel configuration](https://github.com/projg2/gentoo-kernel-config)

[[]][Kernel binary package building](https://github.com/projg2/binpkg-docker)

[[]][Kernel installation](https://github.com/projg2/installkernel-gentoo)

[[]][Fedora upstream](https://src.fedoraproject.org/rpms/kernel/tree/rawhide)

The Distribution Kernels and associated tools are a (semi-)automatic way of configuring, building and installing kernels with the package manager. These kernel packages have three goals:

1.  Covering kernel maintenance wholly using packages (install via emerge, upgrade as part of \@world upgrade), without requiring additional actions from the user or resorting to non-portable hacks.
2.  Providing a default configuration that works on the widest practical range of systems, for users who are not interested in configuring their own kernel from scratch.
3.  Supporting different bootloaders and [/boot] layouts (such as GRUB, systemd-boot, rEFInd, EFI stub) with minimal effort, including deploying self-built kernel binary packages over a fleet of heterogeneous systems.

See the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Distribution_kernels "Handbook:AMD64/Installation/Kernel") for setting up a distribution kernel during installation.

## Contents

-   [[1] [Current packages]](#Current_packages)
-   [[2] [Installation]](#Installation)
-   [[3] [Signed kernel modules]](#Signed_kernel_modules)
-   [[4] [Secure Boot]](#Secure_Boot)
-   [[5] [Using LLVM]](#Using_LLVM)
-   [[6] [Generic UKI]](#Generic_UKI)
-   [[7] [Using custom initramfs and UKI generators]](#Using_custom_initramfs_and_UKI_generators)
    -   [[7.1] [Debian\'s installkernel]](#Debian.27s_installkernel)
    -   [[7.2] [Systemd\'s kernel-install]](#Systemd.27s_kernel-install)
-   [[8] [Modifying kernel configuration]](#Modifying_kernel_configuration)
    -   [[8.1] [Preparing a modified kernel config]](#Preparing_a_modified_kernel_config)
    -   [[8.2] [Using savedconfig]](#Using_savedconfig)
    -   [[8.3] [Using /etc/kernel/config.d]](#Using_.2Fetc.2Fkernel.2Fconfig.d)
-   [[9] [See also]](#See_also)

## [Current packages]

The following packages are provided:

-   [[[sys-kernel/vanilla-kernel]](https://packages.gentoo.org/packages/sys-kernel/vanilla-kernel)[]] (built from source, customizable)
-   [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] (built from source, customizable)
-   [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] (prebuilt)

The project currently maintains two LTS branches (5.4 and 5.10), plus newer branches that are marked stable at the time. Usually, the last EOL version is also kept for a short time.

## [Installation]

** Tip**\
If using out-of-source kernel modules like [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] or [[[sys-fs/zfs]](https://packages.gentoo.org/packages/sys-fs/zfs)[]], add `USE="dist-kernel"` to [/etc/portage/make.conf] to ensure those packages are automatically rebuilt during kernel upgrades.

The Distribution Kernel can either be compiled from source:

`root `[`#`]`emerge -av sys-kernel/gentoo-kernel`

...or as a prebuilt binary:

`root `[`#`]`emerge -av sys-kernel/gentoo-kernel-bin`

** Note**\
If cusomizing the kernel\'s config, it is necessary to use the first method, and build it from source.

For updating the bootloader\'s configuration files:

-   When using [systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot"), enable the [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]].
-   When using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), enable the [[[grub]](https://packages.gentoo.org/useflags/grub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] to automatically run [grub-mkconfig] after upgrades.
-   When using [rEFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd"), enable the [[[refind]](https://packages.gentoo.org/useflags/refind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] to automatically install png logo files for each kernel entry.

\
It is possible to use a hook in [/etc/kernel/\*.d/] to automatically update other bootloaders, or run arbitrary commands at the time of kernel installation.

## [Signed kernel modules]

The `modules-sign` global USE flag can be used to automatically sign the compiled kernel modules. When the flag is enabled, the `MODULES_SIGN_HASH`, `MODULES_SIGN_KEY` (and optionally `MODULES_SIGN_CERT`) environment variables can be set to control the key (or pkcs11 URI) and hashing algorithm (default: SHA512). When `MODULES_SIGN_KEY` is unset the kernel build system will automatically generate a new key.

[FILE] **`/etc/portage/make.conf`make.conf**

    MODULES_SIGN_KEY="..."
    MODULES_SIGN_HASH="..."

As of version 6.4.13 the modules in the pre-built kernel packages (e.g. [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]) are pre-signed though enforcement of valid module signatures is not enabled by default for these kernels. Enforcement can be enabled with the `module.sig_enforce=1` kernel command line argument, or by enabling [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"). For these kernels, the key that was used to sign the in-tree modules is not available to sign out-of-tree modules. In this case, if module signature enforcement is enabled, any out-of-tree modules must be signed with a different key, and the certificate belonging to this key must be inserted into the kernel\'s keychain using [Shim](https://wiki.gentoo.org/wiki/Shim "Shim"), see the [Signed kernel module support](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support") and [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") article for more details.

## [Secure Boot]

The `secureboot` global USE flag can be used to automatically sign the generated kernel images for use with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"). When the flag is enabled the `SECUREBOOT_SIGN_KEY` and `SECUREBOOT_SIGN_CERT` must be used to specify which key (or pkcs11 URI) and certificate should be used. When using [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") it is required that the kernel modules are also signed, see the above section for more information on this.

[FILE] **`/etc/portage/make.conf`make.conf**

    SECUREBOOT_SIGN_KEY="..."
    SECUREBOOT_SIGN_CERT="..."

As of version 6.4.13 the kernel image in the pre-built kernel packages (e.g. [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]) is pre-signed. The certificate belonging to this signature can be found in `/usr/src/linux-x.y.z-gentoo-dist/certs/signing_key.x509`. As with other kernel packages, this certificate must be accepted by the [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware or [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") in order to boot with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") enabled.

** Note**\
To successfully boot with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") enabled any bootloaders involved in the boot-chain must also be signed. Additionally the firmware must be configured to accept the used certificate, or alternatively [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") can be used as pre-loader.

## [Using LLVM]

If using LLVM, setting `CC` and friends is sufficient in [/etc/portage/package.env]. There is no need to set `LLVM=1`.

Per the kernel [documentation](https://docs.kernel.org/kbuild/llvm.html#the-llvm-argument), setting `LLVM` is just shorthand for setting the various toolchain tool variables appropriately. It\'s better to be precise with what configuration is requested.

## [Generic UKI]

As of version 6.6.9 it is possible to install a generic [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") alongside the kernel with the `generic-uki` USE flag on **[amd64]** and **[arm64]** systems. As with plain kernel images and kernel modules, this UKI is pre-signed in [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]]. To use generic UKI, manual creation of an initramfs or Unified Kernel Image must be disabled in [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel"), this is done by disabling the USE flags relating to initramfs and UKI generators:

[FILE] **`/etc/portage/package.use/installkernel`package.use**

    sys-kernel/gentoo-kernel generic-uki
    sys-kernel/gentoo-kernel-bin generic-uki
    sys-kernel/installkernel -dracut -ugrd -ukify

\

** Warning**\
This is an experimental feature! It is known to work on systemd systems via [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot") or [EFI Stub](https://wiki.gentoo.org/wiki/EFI_Stub "EFI Stub") booting. It will likely not work on systems using openrc or musl due to the inclusion of systemd and other executables built against glibc in the prebuilt initramfs. Issues have also been observed trying to boot this generic UKI with [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"). Additionally, the generic UKI requires that the system\'s UEFI implementation is 64 bit, which may not be the case on older systems despite having a 64 bit CPU. On these systems the generic initramfs image may still be used, but a custom UKI must be built as described above. When trying the generic UKI or initramfs for the first time, always ensure that an alternative method of booting the system is available.

## [Using custom initramfs and UKI generators]

To use custom unsupported initramfs generators, **disable** the `initramfs` USE flag. Then, install an appropriate plugin for the used [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") implementation:

### [][Debian\'s installkernel]

For [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]\[-systemd\] initramfs and UKI plugins are installed in [/etc/kernel/preinst.d]. The plugin must place the generated initramfs and/or UKI as an `initrd` or `uki.efi` file respectively, in `$`. Additionally it should respect the `$` and/or `$` variables.

### [][Systemd\'s kernel-install]

For [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]\[systemd\] initramfs and UKI plugins are installed in [/etc/kernel/install.d], the file name must have the suffix `.install`. The plugin must place the generated initramfs and/or UKI as an `initrd` or `uki.efi` file respectively, in `$`. Additionally it should respect the `$` and/or `$` variables.

## [Modifying kernel configuration]

** Note**\
By default, a rather full-featured config is used. These steps are only necessary if a customized configuration is required.

** Warning**\
To customize, use the from-source packages [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] or [[[sys-kernel/vanilla-kernel]](https://packages.gentoo.org/packages/sys-kernel/vanilla-kernel)[]], and not the the `-bin` variant(s).

The modern versions of Distribution Kernels support two mechanisms for changing the kernel configuration: savedconfig and/or config snippets.

savedconfig

config snippets

### [Preparing a modified kernel config]

The easiest way to modify the current kernel configuration is to run one the configuration UIs in the kernel build tree. To do that, select a kernel ebuild and run it up to the configure phase. For example:

`root `[`#`]`ebuild /var/db/repos/gentoo/sys-kernel/gentoo-kernel/gentoo-kernel-5.9.8.ebuild configure`

     * linux-5.9.tar.xz BLAKE2B SHA512 size ;-) ...                          [ ok ]
     * genpatches-5.9-8.base.tar.xz BLAKE2B SHA512 size ;-) ...              [ ok ]
     * genpatches-5.9-8.extras.tar.xz BLAKE2B SHA512 size ;-) ...            [ ok ]
     * kernel-x86_64-fedora.config.5.9.2 BLAKE2B SHA512 size ;-) ...         [ ok ]
     * Starting with 5.7.9, Distribution Kernels are switching from Arch
     * Linux configs to Fedora.  Please keep a backup kernel just in case.
    >>> Unpacking source...
    >>> Unpacking linux-5.9.tar.xz to /tmp/portage/sys-kernel/gentoo-kernel-5.9.8/work
    [...]
    make[1]: Leaving directory '/tmp/portage/sys-kernel/gentoo-kernel-5.9.8/work/modprep'
    >>> Source configured.

Note the directory used by make. Enter it and run a kernel configuration tool such as nconfig or menuconfig:

`root `[`#`]`cd /var/tmp/portage/sys-kernel/gentoo-kernel-5.9.8/work/modprep`

`root `[`#`]`make nconfig`

After saving changes, the new config will be written to the [.config] file (in the modprep directory).

### [Using savedconfig]

To use savedconfig, put the kernel config into an appropriate [/etc/portage/savedconfig] directory. The filename can either match the package name, or name with version. For example, creating the following file will apply the same configuration anytime a version of the `gentoo-kernel` package is emerged:

`root `[`#`]`cp /var/tmp/portage/sys-kernel/gentoo-kernel-5.9.8/work/modprep/.config /etc/portage/savedconfig/sys-kernel/gentoo-kernel`

Afterward, enable the `savedconfig` USE flag on the relevant kernel package, then re-emerge the package:

`root `[`#`]`echo "sys-kernel/gentoo-kernel savedconfig" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask sys-kernel/gentoo-kernel`

Note that the default Gentoo kernel configuration will not used if savedconfig has been enabled. When using an outdated configuration file, unset symbols (a.k.a newly added symbols) will take the upstream kernel\'s default values rather than Gentoo\'s default configuration. It is important to note there could be differences between the two.

### [][Using /etc/kernel/config.d]

** Tip**\
To easily generate [.config] snippets, change to the [/var/tmp/portage/sys-kernel/gentoo-kernel-\<version\>/work/modprep] directory (replacing `<version>` with the appropriate version number), then run:

\

`user `[`$`]`../linux-*/scripts/diffconfig -m .config.old .config | tee -a /etc/kernel/config.d/my-kernel.config`

To use the config.d approach, put a config override file into [/etc/kernel/config.d] directory. Make sure that the file has [.config] suffix. All files present in that directory will be merged in lexical order to the default Gentoo config.

For example:

[FILE] **`/etc/kernel/config.d/50test.config`**

    # CONFIG_HZ_300 is not set
    CONFIG_HZ_1000=y
    CONFIG_HZ=1000

Note that the \'is not set\' comments unset options.

Using different option files for different kernel versions or variants is not supported via the config.d configuration method at the moment.

## [See also]

-   [Savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") --- a USE flag that preserves the saved configuration files upon package updates.
-   [Distribution kernel project page](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") --- maintains sys-kernel/\*-kernel packages.
-   [News item](https://www.gentoo.org/news/2020/09/15/distribution-kernel.html)