**Resources**

[[]][GitHub](https://github.com/uapi-group/specifications/blob/main/specs/unified_kernel_image.md#unified-kernel-image-uki)

A **unified kernel image (UKI)** is a single executable which can be [booted directly from UEFI firmware](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), or automatically sourced by boot-loaders with little or no configuration.

A unified kernel image allows to incorporate all or a subset of the following:

-   an [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") loader like systemd-stub,
-   the kernel command line,
-   [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode"),
-   an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") image,
-   a [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") image,
-   a [splash screen](https://wiki.gentoo.org/wiki/Plymouth "Plymouth").

The resulting executable, and therefore all these elements together can then be easily signed for use with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").

## Contents

-   [[1] [Supported architectures]](#Supported_architectures)
-   [[2] [Dependency installation]](#Dependency_installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Dracut]](#Dracut)
        -   [[3.1.1] [Secure Boot]](#Secure_Boot)
    -   [[3.2] [Ukify]](#Ukify)
        -   [[3.2.1] [Secure Boot]](#Secure_Boot_2)
        -   [[3.2.2] [Measured Boot]](#Measured_Boot)
-   [[4] [Kernel installation]](#Kernel_installation)
-   [[5] [Boot Loaders]](#Boot_Loaders)
    -   [[5.1] [systemd-boot and rEFInd]](#systemd-boot_and_rEFInd)
    -   [[5.2] [GRUB]](#GRUB)
    -   [[5.3] [EFI stub]](#EFI_stub)
        -   [[5.3.1] [Automated EFI stub booting]](#Automated_EFI_stub_booting)
            -   [[5.3.1.1] [Systemd kernel-install]](#Systemd_kernel-install)
            -   [[5.3.1.2] [Traditional installkernel]](#Traditional_installkernel)
-   [[6] [See also]](#See_also)

## [Supported architectures]

A unified kernel image requires a stub loader, e.g. `systemd-stub`. Currently systemd-stub is available for `amd64`, `x86` and `arm64`. On `arm64` the kernel must be configured with `CONFIG_EFI_ZBOOT=y` since `systemd-stub` does not support decompressing the kernel image and as such the kernel must be built with its own decompressor (zboot). This config option exists since kernel version 6.1, and is enabled in version 6.5 and up of [[[gentoo-kernel-bin]](https://packages.gentoo.org/packages/gentoo-kernel-bin)[]]. In [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] and [[[sys-kernel/vanilla-kernel]](https://packages.gentoo.org/packages/sys-kernel/vanilla-kernel)[]] this option is enabled when the [[[secureboot]](https://packages.gentoo.org/useflags/secureboot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled. It may also be configured manually:

[FILE] **`/etc/kernel/config.d/zboot.conf`**

    CONFIG_EFI_ZBOOT=y

## [Dependency installation]

First one needs a \"stub loader\", which is provided by [systemd-stub]. Openrc users have to install [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]], and systemd users need the [[[boot]](https://packages.gentoo.org/useflags/boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]].

To generate a Unified Kernel Image (UKI), one needs [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") or systemd\'s [ukify] tool. Notice ukify cannot generate [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), while Dracut can.

Dracut users needs the [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]].

To use ukify, set the [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag for sys-apps/systemd, and the USE flags [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[ukify]](https://packages.gentoo.org/useflags/ukify)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] for sys-kernel/installkernel.

## [Configuration]

### [Dracut]

The [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") plugin of [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") will automatically pick up the layout setting and generate a UKI. (Then a seperate [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") file won\'t be prepared). This can be set in `install.conf` as follows:

[FILE] **`/usr/lib/kernel/install.conf`**

    layout=uki
    initrd_generator=dracut
    uki_generator=dracut

A Unified Kernel Image may contain a kernel command line, specified via [/etc/dracut.conf]. Note that any kernel command line supplied by the bootloader overrides this include command line, except when [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") is enabled:

[FILE] **`/etc/dracut.conf`**

    kernel_cmdline="..."

** Warning**\
[/etc/kernel/cmdline] is not used when generating Unified Kernel Images with Dracut! This file is used by [ukify] and when generating entries for [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot").

#### [Secure Boot]

To automatically sign the generated UKI for use with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"):

[FILE] **`/etc/dracut.conf`**

    uefi_secureboot_cert="..."
    uefi_secureboot_key="..."

For example, when using keys generated by [[[app-crypt/sbctl]](https://packages.gentoo.org/packages/app-crypt/sbctl)[]]:

[FILE] **`/etc/dracut.conf`**

    uefi_secureboot_cert="/var/lib/sbctl/keys/db/db.pem"
    uefi_secureboot_key="/var/lib/sbctl/keys/db/db.key"

To use a PKCS11 URI instead of a plain key file:

[FILE] **`/etc/dracut.conf`**

    uefi_secureboot_cert="..."
    uefi_secureboot_key="pkcs11:..."
    uefi_secureboot_engine="pkcs11"

** Note**\
To successfully boot with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") enabled the Boot Loader should also be signed if one is used. This can be done using the [sbsign] tool from [[[app-crypt/sbsigntools]](https://packages.gentoo.org/packages/app-crypt/sbsigntools)[]]. Additionally, the [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware should be configured to accept the used key, this can be done manually or alternatively [[[app-crypt/sbctl]](https://packages.gentoo.org/packages/app-crypt/sbctl)[]] can be used to automatically generate and enroll a set of keys. It is also possible to use [shim](https://wiki.gentoo.org/wiki/Shim "Shim") as a pre-loader that is already signed with the 3rd-party Microsoft key, accepted by default on most [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") enabled motherboards.

### [Ukify]

Since [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] version 253 in 2023, the [ukify] tool can be used to generate a unified kernel image. When ukify is used, the included kernel command line is configured in [/etc/kernel/cmdline]. Note that any kernel command line supplied by the bootloader overrides this include command line, except when [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") is enabled.

#### [Secure Boot]

To automatically sign the generated UKI for use with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"):

[FILE] **`/etc/kernel/uki.conf`**

    [UKI]
    SecureBootSigningTool=sbsign
    SecureBootPrivateKey=...
    SecureBootCertificate=...

To use a PKCS11 URI instead of a plain key file:

[FILE] **`/etc/kernel/uki.conf`**

    [UKI]
    SecureBootSigningTool=sbsign
    SecureBootPrivateKey=pkcs11:...
    SecureBootCertificate=...
    SigningEngine=pkcs11

#### [Measured Boot]

To instruct ukify to pre-calculate and sign PCR values for use with [Measured Boot](https://wiki.gentoo.org/index.php?title=Measured_Boot&action=edit&redlink=1 "Measured Boot (page does not exist)"):

[FILE] **`/etc/kernel/uki.conf`**

    [PCRSignature:initrd]
    PCRPrivateKey=...
    PCRPublicKey=...
    Phases=enter-initrd

    [PCRSignature:system]
    PCRPrivateKey=...
    PCRPublicKey=...
    Phases=enter-initrd:leave-initrd
           enter-initrd:leave-initrd:sysinit
           enter-initrd:leave-initrd:sysinit:ready

## [Kernel installation]

With the above configurations, a UKI kernel will automatically be generated and installed. This means it is regardless whether one installs Gentoo\'s distributed kernel or manually run `make install` in the kernel\'s source.

Kernel will be installed as e.g. `/boot/EFI/Linux/4098b3f648d74c13b1f04ccfba7798e8-6.10.11-gentoo-dist`. The format is `<machine-id>-<version number> + suffix.`

## [Boot Loaders]

### [systemd-boot and rEFInd]

[systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot") and [rEFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd") dynamically detect the UKIs installed in the `Linux` directory on the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"), no further configuration is required. Though users of rEFInd might want to enable the [[[refind]](https://packages.gentoo.org/useflags/refind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] to ensure rEFInd will use the correct icon for the installed UKI.

When rEFInd is configured to search for kernels in /boot for example, UKI kernels can be stored there, too.

### [GRUB]

[GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") is capable of loading a UKI payload using the [chainloader] command. Any parameters entered at the end of the [chainloader] command will be passed to the kernel.

For example:

[FILE] **`/etc/grub.d/40_custom`**

    menuentry 'Gentoo GNU/Linux, with Linux 6.11.5-gentoo'

### [EFI stub]

Unified kernel images can also be [booted directly](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") from [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware without the use of any boot loader. [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") can be used to add or remove boot menu entries for unified kernel images:

`root `[`#`]`efibootmgr --create --disk /dev/sdX --part partition_number --label "Gentoo Linux x.y.z" --loader 'EFI\Linux\linux-x.y.z-gentoo.efi' --unicode`

#### [Automated EFI stub booting]

** Warning**\
Many vendors do not follow the UEFI specification exactly. As a result, automated EFI stub booting, as described below, is not guaranteed to work on all systems. For such systems, a light-weight EFI chain-loading solution that is guaranteed to work on all UEFI systems is [systemd-boot](https://wiki.gentoo.org/wiki/Systemd-boot "Systemd-boot").

##### [Systemd kernel-install]

[[[app-emulation/virt-firmware]](https://packages.gentoo.org/packages/app-emulation/virt-firmware)[]] contains the [kernel-bootcfg] tool to assist in the creation and removal of UEFI boot entries for unified kernel images. To set this up, enable the [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] and then enable the init service provided by [[[app-emulation/virt-firmware]](https://packages.gentoo.org/packages/app-emulation/virt-firmware)[]]:

For systemd systems:

`root `[`#`]`systemctl enable --now kernel-bootcfg-boot-successful.service`

For OpenRC systems:

`root `[`#`]`rc-update add kernel-bootcfg-boot-successful default`

** Note**\
The systemd USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] is required, but this flag does not force a dependency on the systemd init system. The dependencies are satisfied by the [[[boot]](https://packages.gentoo.org/useflags/boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[kernel-install]](https://packages.gentoo.org/useflags/kernel-install)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flags on [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]], as such this also works on OpenRC systems.

UEFI boot entries for Unified Kernel Images will now be automatically created and removed. To create one for the currently running kernel the kernel must be reinstalled using either [emerge \--config gentoo-kernel ] (for distribution kernels) or [make install] (for manually managed kernels).

When [[[sys-boot/shim]](https://packages.gentoo.org/packages/sys-boot/shim)[]] is installed and present on to the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"), [kernel-bootcfg] will register unified kernel images for booting via [shim](https://wiki.gentoo.org/wiki/Shim "Shim"). This may be useful for users who wish to boot unified kernel images with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") enabled, without registering custom keys in the system\'s firmware. To setup [kernel-bootcfg] to use shim, install it to the EFI System Partition, while substituting `x64` for the system\'s UEFI architecture and `$` for the mount point of the EFI System Partition:

`root `[`#`]`emerge --ask sys-boot/shim`

`root `[`#`]`cp /usr/share/shim/BOOTX64.EFI $/EFI/Gentoo/shimx64.efi `

`root `[`#`]`cp /usr/share/shim/mmx64.efi $/EFI/Gentoo/mmx64.efi `

In addition to automated registration via [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel"), it is also possible to register a new UKI manually:

`root `[`#`]`kernel-bootcfg --add-uki $/EFI/Linux/linux-x.y.z-gentoo-dist.efi --title x.y.z-gentoo-dist --once`

** Tip**\
The [\--once] argument will register the new entry, but not add it to the boot order yet. Instead it will instruct the system to boot the new UKI on the next reboot once (i.e. set the `BootNext` EFI variable). Upon a successful boot the [kernel-bootcfg-boot-successful] init service will then add the new UKI to the top of the boot order.

And to manually remove an entry for a given UKI:

`root `[`#`]`kernel-bootcfg --remove-uki $/EFI/Linux/linux-x.y.z-gentoo-dist.efi`

##### [Traditional installkernel]

For non-systemd systems, automated EFI Stub booting is implemented using [[[sys-boot/uefi-mkconfig]](https://packages.gentoo.org/packages/sys-boot/uefi-mkconfig)[]]. To set this up, enable the [[[uki]](https://packages.gentoo.org/useflags/uki)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags and disable the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]. Then reinstall the kernel. [uefi-mkconfig] will boot new entries via [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") if [[[sys-boot/shim]](https://packages.gentoo.org/packages/sys-boot/shim)[]] is installed and the shim EFI executable is present in the same directory as the kernel images (i.e. [ESP/EFI/Linux]).

## [See also]

-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") --- a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.
-   [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") --- an enhancement of the security of the pre-boot process of a [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") system.
-   [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") --- an alternative method of managing accepted [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") keys without touching the [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware settings
-   [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") --- an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure and aims to have as little as possible hard-coded into the initramfs.
-   [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")