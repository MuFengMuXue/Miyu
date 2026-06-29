This page contains [[changes](https://wiki.gentoo.org/index.php?title=EFI_stub&oldid=1415626&diff=1420569)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/EFI_stub/es "Módulo EFI (82% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/EFI_stub/hu "EFI stub/hu (94% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/EFI_stub/ja "EFI スタブ (94% translated)")

**Resources**

[[]][Official documentation](https://www.kernel.org/doc/html/latest/admin-guide/efi-stub.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)

[[]][Wikipedia](https://en.wikipedia.org/wiki/EFI_system_partition "wikipedia:EFI system partition")

[[]]This article has some todo items:\

-   CONFIG_PM_STD_PARTITION for hibernation

An **EFI (boot) stub**^[\[1\]](#cite_note-1)^ is a kernel that is an EFI executable (i.e., can boot directly from UEFI); EFI stub kernels may boot with or without a bootloader.

## Contents

-   [[1] [Kernel configuration]](#Kernel_configuration)
    -   [[1.1] [EFI stub support]](#EFI_stub_support)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Automated]](#Automated)
        -   [[2.1.1] [Systemd kernel-install]](#Systemd_kernel-install)
        -   [[2.1.2] [Traditional installkernel]](#Traditional_installkernel)
    -   [[2.2] [Manual]](#Manual)
        -   [[2.2.1] [Root partition configuration]](#Root_partition_configuration)
            -   [[2.2.1.1] [Option 1: Configuring it into the kernel]](#Option_1:_Configuring_it_into_the_kernel)
            -   [[2.2.1.2] [Option 2: Configuring it into UEFI]](#Option_2:_Configuring_it_into_UEFI)
        -   [[2.2.2] [Optional: Kernel with initramfs]](#Optional:_Kernel_with_initramfs)
        -   [[2.2.3] [Optional: Embedded initramfs]](#Optional:_Embedded_initramfs)
            -   [[2.2.3.1] [EFI configuration]](#EFI_configuration)
        -   [[2.2.4] [Optional: Booting without dedicated UEFI entry]](#Optional:_Booting_without_dedicated_UEFI_entry)
        -   [[2.2.5] [Backup kernel]](#Backup_kernel)
-   [[3] [Microcode loading]](#Microcode_loading)
-   [[4] [Optional: Signing for Secure Boot]](#Optional:_Signing_for_Secure_Boot)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Kernel configuration]

### [EFI stub support]

The following kernel configuration options must be enabled:

[KERNEL] **Enable EFI stub support for Kernels 6.1+**

    Processor type and features  --->
        [*] EFI runtime service support Search for <code>CONFIG_EFI</code> to find this item.
        [*]     EFI stub support Search for <code>CONFIG_EFI_STUB</code> to find this item.
        [ ]     EFI mixed-mode support (OPTIONAL) Search for <code>CONFIG_EFI_MIXED</code> to find this item.

** Note**\
EFI mixed-mode support is only required to boot a 64-bit kernel from 32-bit firmware if the CPU supports 64-bit mode and EFI handover is enabled.

## [Installation]

** Tip**\
If an [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) does not exist, please follow the steps [to set it up](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#Creating_the_EFI_System_Partition_.28ESP.29 "Handbook:AMD64/Installation/Disks") first.

### [Automated]

** Warning**\
Since UEFI implementations differ between vendors, EFI Stub booting is not guaranteed to work for all UEFI systems; ensure a backup boot method is available before attempting (automated) EFI Stub booting.

Automated EFI stub booting is provided by [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] when the [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled; this relocates the regular boot layout from [/boot] to the [EFI/Gentoo] directory on the ESP.

#### [Systemd kernel-install]

When both the [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags are enabled on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]], [kernel-install] calls [kernel-bootcfg] from [[[app-emulation/virt-firmware]](https://packages.gentoo.org/packages/app-emulation/virt-firmware)[]] to add or remove a boot entry for the installed or removed kernel. [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") is called automatically by the kernel\'s [make install] or by the [Distribution Kernels\'](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") post-install phase; therefore, no special action is required when installing a new kernel, though the `kernel-bootcfg-boot-successful` init service from [[[app-emulation/virt-firmware]](https://packages.gentoo.org/packages/app-emulation/virt-firmware)[]] should be enabled to automatically make an entry for a new kernel permanent when it successfully boots.

For systemd systems:

`root `[`#`]`systemctl enable --now kernel-bootcfg-boot-successful.service`

For OpenRC systems:

`root `[`#`]`rc-update add kernel-bootcfg-boot-successful default`

When the to-be-registered kernel image is not a [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") (UKI), a kernel command line for the new entry is read from:

-   [/etc/kernel/cmdline], or
-   [/usr/lib/kernel/cmdline], or
-   [/proc/cmdline]

in this order. In addition, the `initrd=` kernel command line argument is automatically added if an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") was generated while installing the kernel. If on the other hand the to-be-registered kernel is a UKI, then no command line is added to the new entry; instead, the command line built into the UKI is used and the contents of this built-in command line are usually read from the same files when the UKI is generated.

** Tip**\
The initramfs and kernel command line may also be embedded into the kernel: see the sections [below](https://wiki.gentoo.org/wiki/EFI_stub#Optional:_Embedded_initramfs "EFI stub") for more information.

#### [Traditional installkernel]

When the [[[efistub]](https://packages.gentoo.org/useflags/efistub)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] but the [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is disabled [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") calls [uefi-mkconfig] from [[[sys-boot/uefi-mkconfig]](https://packages.gentoo.org/packages/sys-boot/uefi-mkconfig)[]] to dynamically update the UEFI configuration; if the [shim](https://wiki.gentoo.org/wiki/Shim "Shim") EFI executable is present in the same directory as the kernel image, the kernels will be chainloaded via Shim.

### [Manual]

With the kernel configured with EFI Stub support and assuming the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is mounted at [/efi], create a separate directory below [/efi/EFI]:

`root `[`#`]`mkdir -p /efi/EFI/example`

** Note**\
On some systems [/efi/EFI] or [/efi/efi] (in lowercase) may already exist (assuming the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is mounted at [/efi]). The [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") file system of the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is not case-sensitive, but case-preserving (VFAT); with the default VFAT mount options, the above command will work in both cases. See the [case sensitivity section in the FAT article](https://wiki.gentoo.org/wiki/FAT#Case_sensitivity "FAT") for further details.

The kernel is created from the current kernel directory and copied to the new directory. This will install the kernel to [/efi/EFI/example/bzImage.efi]:

`/usr/src/linux #``make && make modules_install && cp arch/x86/boot/bzImage /efi/EFI/example/bzImage.efi`

** Tip**\
It is recommended when upgrading the kernel to keep an older version which is known to work:

`user `[`$`]`tree -L 3 /efi`

     /efi
     └── EFI
         └── example
             ├── bzImage-6.1.67.efi
             └── bzImage-6.1.70.efi

#### [Root partition configuration]

To boot directly from [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"), the kernel or its initramfs must know where to find the root partition of the system to be booted; when using a bootmanager like grub, the kernel gets the root\'s path from the bootmanager via the command line; when using a stub kernel, **two options** may be used to give the kernel this information - choose one of these options:

##### [Option 1: Configuring it into the kernel]

[KERNEL] **Root Partition information for Kernels 6.1+**

    Processor type and features  --->
        [*] Built-in kernel command line
        (root=PARTUUID=adf55784-15d9-4ca3-bb3f-56de0b35d88d rw)

** Important**\
The value **adf55784-15d9-4ca3-bb3f-56de0b35d88d** is an example and must be replaced with the real root\'s UUID, which can be obtained by using the [blkid] command:

`root `[`#`]`blkid | grep sda3 `

```
/dev/sda3: UUID="d1e0c1e0-3a40-42c5-8931-cfa2c7deae32" TYPE="ext4" PARTUUID="adf55784-15d9-4ca3-bb3f-56de0b35d88d"
```

The *partition\'s* PARTUUID is distinct from the *filesystem\'s* UUID; the UUID refers to the unique filesystem partition and must be used with a initramfs, while the PARTUUID refers to the disk partition and can be used when booting a kernel.

##### [Option 2: Configuring it into UEFI]

To add an entry with command line arguments:

`root `[`#`]`efibootmgr --create --disk /dev/sda --label "Gentoo EFI Stub" --loader "\EFI\example\bzImage.efi" -u "root=/dev/sda3"`

** Important**\
When using a initramfs, setting the root location using a **PARTUUID** or (filesystem) **UUID** is generally preferable and less error prone.

More examples may be found in [Creating a boot entry](https://wiki.gentoo.org/wiki/Efibootmgr#Creating_a_boot_entry "Efibootmgr").

#### [Optional: Kernel with initramfs]

When using a kernel with an external initramfs (as a CPIO archive), additional steps are necessary. There is always an initramfs file when building a dist-kernel or using genkernel; when using a dist-kernel, this initramfs is named \"initrd\" and is in [/usr/src/linux-6.1.57-gentoo-dist/arch/x86/boot/initrd] and it must be copied into the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"):

`root `[`#`]`cp /path/to/my/initramfs/myinitrd.cpio.gz /efi/EFI/example/initrd.cpio.gz`

Now the kernel needs its initramfs, and the initramfs needs its root; UEFI must provide both:

`root `[`#`]`efibootmgr -c -d /dev/sda -p 1 -L "Gentoo EFI Stub" -l '\EFI\example\bzImage.efi' -u 'root=UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx initrd=\EFI\example\initrd.cpio.gz'`

A Forum post explains in more detail, solving some user errors in the process: [Forums topic - Booting UEFI without Grub](https://forums.gentoo.org/viewtopic-p-8805827.html#8805827)

When using [Early Userspace Mounting](https://wiki.gentoo.org/wiki/Early_Userspace_Mounting "Early Userspace Mounting"), the [Generating the Initramfs](https://wiki.gentoo.org/wiki/Early_Userspace_Mounting#Generating_the_Initramfs "Early Userspace Mounting") and [Using a Stub Kernel](https://wiki.gentoo.org/wiki/Early_Userspace_Mounting#Using_a_Stub_Kernel "Early Userspace Mounting") sections also provide a more thorough explanation.

#### [Optional: Embedded initramfs]

It\'s also possible to embed the initramfs directly into the kernel. Advantages include: the initramfs being verified by [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") when verifying the kernel, a simplified boot process and EFI partition, and making loading the kernel by hand easier (because callers needn\'t specify the initramfs). Disadvantages include reduced flexibility, potential mistakes, and an unconventional boot setup.

** Warning**\
If your initramfs contains [Microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode"), it is critical (for security) that it receives updates; when embedded, the initramfs can\'t update independently of the kernel and a **kernel rebuild will be necessary every time the initramfs is updated**. In particular, please ensure that if:

`root `[`#`]`make clean`

is not run prior to rebuilding the kernel,

`root `[`#`]`rm usr/initramfs_data.cpio`

is run to clear the cached initramfs CPIO archive from the last build.

-   When the initramfs has an update, the kernel is rebuilt and reinstalled.
-   If the initramfs is managed by [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]], it is updated **before** the kernel.

The kernel supports both CPIO files (e.g., as produced by [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut")) and source directories (which are to be compressed into a CPIO archive). The following shows the latter with [/usr/src/initramfs]; however, it should be substituted with [/path/to/my/initramfs/myinitrd.cpio.gz] if the former case is desired (it usually is, unless using a [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs")).

[KERNEL] **Embedding the initramfs into the kernel**

    General Setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
        (/usr/src/initramfs) Initramfs source file(s)

##### [EFI configuration]

To ensure everything is functioning properly, the kernel may be booted without the [initrd] command line argument.

To create the UKI entry:

`root `[`#`]`efibootmgr --create --disk /dev/sda --label "Gentoo EFI Stub" --loader "\EFI\example\bzImage.efi"`

#### [Optional: Booting without dedicated UEFI entry]

UEFI specifies that when booting from a particular ESP, the default behavior is to load an EFI executable from a specific path, dependent on the host architecture: for example, on an AMD64 system, an EFI stub placed at [\$(ESP)\\efi\\boot\\bootx64.efi] would be automatically loaded when booting from that ESP.

Combined with setting the relevant drive\'s boot priority, this setup can automatically boot the kernel upon power-on without entering a boot menu whilst still preserving the option to do so if desired.

This can be used to circumvent the use of efibootmgr and the creation of UEFI entries with the cost of less flexibility; it runs the risk of rendering the system unbootable if a new, broken kernel were to be installed to the default path.

#### [Backup kernel]

It is recommended to always have a backup kernel; if a bootmanager like grub is already installed, it should not be uninstalled because grub can boot a stub kernel just like a normal kernel. Another possibility working with an additional UEFI entry: before installing a new kernel, the current one can be copied from [/efi/EFI/example] to [/efi/EFI/backup]. In the example below, other names were used and the second UEFI entry was created with [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"):

`root `[`#`]`efibootmgr`

```
BootCurrent: 0002
Timeout: 1 seconds
BootOrder: 0002,0000,0001
Boot0000* Secure        HD(1,GPT,0adcbfee-21aa-42ea-9a9a-2e53bd05e6a2,0x800,0x7f800)/File(\EFI\secure\bzImage.efi)
Boot0001* gentoo        HD(1,GPT,0adcbfee-21aa-42ea-9a9a-2e53bd05e6a2,0x800,0x7f800)/File(\EFI\gentoo\grubx64.efi)
Boot0002* Backup        HD(1,GPT,0adcbfee-21aa-42ea-9a9a-2e53bd05e6a2,0x800,0x7f800)/File(\EFI\backup\bzImage.efi)
```

## [Microcode loading]

When using a kernel without an initramfs, it is recommended to load the microcode described in the following articles:

-   [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode#New_method_without_initram-fs.2Fdisk_.28efistub_compatible.29 "Intel microcode").
-   [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode#Supplying_the_microcode_files_to_the_kernel "AMD microcode").

## [Optional: Signing for Secure Boot]

If [Secure Booting](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") this kernel, it must be signed with **sbsign**, part of [[[app-crypt/sbsigntools]](https://packages.gentoo.org/packages/app-crypt/sbsigntools)[]]:

`root `[`#`]`sbsign --key  --cert  /efi/EFI/example/bzImage.efi`

More information is available at [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot#Signing_Boot_Files "Secure Boot").

** Warning**\
It is not possible to EFI Stub boot via [[[sys-boot/shim]](https://packages.gentoo.org/packages/sys-boot/shim)[]] due to the vanilla EFI Stub missing the required `.sbat` sbat section; as such, the used signing keys must be registered directly with the UEFI firmware to EFI Stub boot with Secure Boot enabled. See the [UKI](https://wiki.gentoo.org/wiki/UKI "UKI") wiki page for an alternate EFI Stub boot method that supports booting via [shim](https://wiki.gentoo.org/wiki/Shim "Shim").

## [Troubleshooting]

** Tip**\
Some rare UEFI implementations do not accept individual EFI entries; in this case, it often works to use the *removable media boot path*, see [EFI System Partition #removable media](https://wiki.gentoo.org/wiki/EFI_System_Partition#Removable_media "EFI System Partition") for details. For example, this command will copy the kernel for an amd64 UEFI:

`root `[`#`]`cp /usr/src/linux/arch/x86/boot/bzImage /efi/EFI/boot/bootx64.efi`

Be advised that this is against the UEFI specification as it circumvents the boot selection on internal drives (which are configured using EFI boot entries).

** Tip**\
If command [/usr/lib/kernel/postinst.d/95-efistub-uefi-mkconfig.install] fails during the first install (no EFI kernel found), use [mkdir /efi/Gentoo] to create an empty folder.

-   [Forum topic - BIOS losing the names of the EFI ESPs](https://forums.gentoo.org/viewtopic-p-8447788.html#8447788)

<!-- -->

-   Older kernels compiled with [gcc:10](https://archives.gentoo.org/gentoo-dev/message/60c4f4b7c219f85aa1cfeba5bd630893) [crashed at boot](https://trofi.github.io/posts/213-gcc-10-in-gentoo.html#linux-crash) ([[[bug #721734#c4]](https://bugs.gentoo.org/show_bug.cgi?id=721734#c4)[]]).

<!-- -->

-   Users of [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] can specify the root partition path with the `root=` parameter using [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"):

`root `[`#`]`efibootmgr -c -L "Gentoo Linux" -l '\EFI\Gentoo\bootx64.efi' -u 'root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' `

To create a boot entry with hibernation on swap partition:

`root `[`#`]`efibootmgr -c -L "Gentoo Linux" -l '\EFI\Gentoo\bootx64.efi' -u 'root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX resume=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' `

## [See also]

-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") --- a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.
-   [Architecture specific kernel configuration (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel#Architecture_specific_kernel_configuration "Handbook:AMD64/Installation/Kernel")
-   [REFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd") --- a boot manager for UEFI platforms.
-   [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") --- a single executable which can be [booted directly from UEFI firmware], or automatically sourced by boot-loaders with little or no configuration.

## [External resources]

-   [Linux Kernel Documentation on EFI Stub](https://www.kernel.org/doc/html/latest/admin-guide/efi-stub.html)
-   [EFI Stub - booting without a bootloader](http://blog.realcomputerguy.com/2012/05/efi-stub-booting-without-bootloader.html) Blog posting which this article is partially based on.
-   [EFI bootloaders](http://www.rodsbooks.com/efi-bootloaders/) listing alternative ways to boot a UEFI system.
-   [Gentoo Forums: Suspend and Hibernate with UEFI](https://forums.gentoo.org/viewtopic-p-8111048.html#8111048)
-   [http://www.kroah.com/log/blog/2013/09/02/booting-a-self-signed-linux-kernel/](http://www.kroah.com/log/blog/2013/09/02/booting-a-self-signed-linux-kernel/)

## [References]

1.  [[[↑](#cite_ref-1)] [The kernel doc lacks unification in the terminology. The doc page [\[1\]](https://www.kernel.org/doc/html/latest/admin-guide/efi-stub.html) is titled \"(the) EFI Boot Stub\", but the word \"EFI stub\" is also used.]]