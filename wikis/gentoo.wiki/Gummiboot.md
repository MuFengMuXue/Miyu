**Resources**

[[]][Home](https://www.freedesktop.org/wiki/Software/systemd/systemd-boot/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/systemd)

[[]][GitHub](https://github.com/systemd/systemd)

**systemd-boot**, formerly known as *gummiboot* (rubber dinghy), is a minimal [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot manager.

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Pre-Deployment Considerations]](#Pre-Deployment_Considerations)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Kernel]](#Kernel)
    -   [[3.2] [OpenRC]](#OpenRC)
    -   [[3.3] [systemd]](#systemd)
    -   [[3.4] [Installation to the ESP (EFI system partition)]](#Installation_to_the_ESP_.28EFI_system_partition.29)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [loader.conf]](#loader.conf)
    -   [[4.2] [Menu entry files]](#Menu_entry_files)
    -   [[4.3] [Automatically generate menu entries]](#Automatically_generate_menu_entries)
        -   [[4.3.1] [Unified Kernel Images]](#Unified_Kernel_Images)
    -   [[4.4] [Configuration in boot menu]](#Configuration_in_boot_menu)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Secure Boot]](#Secure_Boot)
    -   [[5.2] [ESP file update process]](#ESP_file_update_process)
        -   [[5.2.1] [systemd service]](#systemd_service)
        -   [[5.2.2] [Portage hook]](#Portage_hook)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Failed to open boot loader directory /usr/lib/systemd/boot/efi: No such file or directory]](#Failed_to_open_boot_loader_directory_.2Fusr.2Flib.2Fsystemd.2Fboot.2Fefi:_No_such_file_or_directory)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Features]

-   Bootloader integration with [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") provided by the [bootctl] command.
-   Ability to select next boot.
-   Easy and simple configuration files which can be generated automatically.
-   Auto add Windows and EFI firmware setup entries.
-   Change timeout, default entry, edit [kernel command line](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters") options on the fly from the boot menu.

## [Pre-Deployment Considerations]

The [Boot Loader Specification](https://uapi-group.org/specifications/specs/boot_loader_specification/) outlines a standard for bootloaders to follow. This specification is one of the methods used by systemd-boot to determine the location of the [[ESP]](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") and [XBOOTLDR] partitions.

The ESP and XBOOTLDR partitions must be partitions on a block device. [Mirrored partitions, for example mdadm RAID1 devices, are not supported](https://github.com/systemd/systemd/issues/17298#issuecomment-1288810057). Systems which mirror the bootloader partitons for reliability should not use systemd-boot.

When using XBOOTLDR, the ESP is used to store the bootloader\'s PE32+ files ([.efi] files) and their configuration files, while the XBOOTLDR partition is used to store [Linux kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel"), [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), and configuration files.

** Note**\
The Boot Loader Specification is not yet widely adopted by other bootloaders.

Use [partitioning tools](https://wiki.gentoo.org/wiki/Partitioning_tools "Partitioning tools") to create an XBOOTLDR partition with Partition Type GUID `bc13c2ff-59e6-4262-a352-b275fd6f7172`, and then format that partition with any file system that the target EFI implementation supports (or can be made to support). All EFI implementations support the use of [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") filesystems.

-   If using [fdisk], the Partition Type GUID can be set using the **t** command to change the partition type, and then selecting **136** to set it to \"Linux extended boot\".
-   If using [gdisk], it can be set using the **t** command to change the partition type code, and then specifying hex code **EA00** to set it to \"XBOOTLDR partition\".

The Boot Loader Specification recommends that, when a XBOOTLDR partition exists, it be mounted at [/boot], and the ESP, at [/efi]. These should be mounted using an [autofs] or [automount] implementation so that they are only mounted when needed.

There are many mechanisms for implementing this; for [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") users, the [[[sys-fs/autofs]](https://packages.gentoo.org/packages/sys-fs/autofs)[]] package can be used. For systemd users, either adding the `x-systemd.automount` option to the [/etc/fstab] entry for the XBOOTLDR and ESP partitions, creating a [systemd automount unit](https://blog.tomecek.net/post/automount-with-systemd/), or [Discoverable Partitions Specification](https://uapi-group.org/specifications/specs/discoverable_partitions_specification/) automatically created mounts can be used.

** Note**\
[bootctl] looks for the XBOOTLDR partition is at [/boot]. If it is mounted elsewhere, the `--boot-path` option must be supplied.

## [Installation]

systemd-boot is included within [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] and, for users of non-systemd-init systems, [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]].

### [Kernel]

Because systemd-boot can only load EFI executables, the desired kernel must support EFI stub (`CONFIG_EFI_STUB=y`):

[KERNEL] **Enable EFI stub support (`CONFIG_EFI_STUB`)**

    Processor type and features  --->
        [*] EFI runtime service support
        [*]   EFI stub support
        [ ]     EFI mixed-mode support

### [OpenRC]

Install the [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]] package with the [[[boot]](https://packages.gentoo.org/useflags/boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag enabled:

`root `[`#`]`mkdir -p /etc/portage/package.use `

`root `[`#`]`echo "sys-apps/systemd-utils boot kernel-install" >> /etc/portage/package.use/systemd-utils `

`root `[`#`]`emerge --ask --oneshot --verbose sys-apps/systemd-utils `

### [systemd]

For versions of systemd \>= 254, emerge [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] with the [[[boot]](https://packages.gentoo.org/useflags/boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag enabled:

`root `[`#`]`mkdir -p /etc/portage/package.use `

`root `[`#`]`echo "sys-apps/systemd boot" >> /etc/portage/package.use/systemd `

`root `[`#`]`emerge --ask --oneshot --verbose sys-apps/systemd `

For older versions, the [[[gnuefi]](https://packages.gentoo.org/useflags/gnuefi)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag toggles this functionality:

`root `[`#`]`mkdir -p /etc/portage/package.use `

`root `[`#`]`echo "sys-apps/systemd gnuefi" >> /etc/portage/package.use/systemd `

`root `[`#`]`emerge --ask --oneshot --verbose sys-apps/systemd `

### [][Installation to the ESP (EFI system partition)]

First ensure that the system has booted in UEFI mode - if following command returns an error the system is not booted in UEFI mode:

`root `[`#`]`ls /sys/firmware/efi/efivars`

** Note**\
systemd, when partitions are configured according to the [Discoverable Partitions Specification](https://uapi-group.org/specifications/specs/discoverable_partitions_specification/), can automatically mount the ESP to [/efi] and the XBOOTLDR partition to [/boot].

Then, use [bootctl] to install systemd-boot to the ESP:

`root `[`#`]`bootctl install`

** Note**\
[bootctl] will attempt to automatically identify an ESP mounted at [/efi], [/boot], or [/boot/efi] (in that order). If the ESP is mounted elsewhere, pass the `--esp-path` option to specify the appropriate location.

## [Configuration]

Overview:

-   Main configuration for systemd-boot is done in file [/loader/loader.conf] of the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP).
-   Boot menu entries are generated for each file ending with [.conf] located in [/loader/entries] of the ESP.
-   EFI PE32+ executable files (including kernel EFI stubs) and initramfs files can be placed anywhere in the ESP.

### [loader.conf]

Although its syntax is well documented in [[[loader.conf(5)]](https://man.archlinux.org/man/loader.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], here is the example:

[FILE] **`/efi/loader/loader.conf`**

    default gentoo-sources-kernel
    timeout 3
    # editor no

The name of the *default* entry is the file name of the menu entry file, as created in the next section, without the [.conf] suffix.

### [Menu entry files]

The boot menu will show one entry for each [.conf] file.

Following is an example menu entry file named \"gentoo-sources-kernel\" where the kernel and initramfs are at [/efi/vmlinuz] and [/efi/initramfs] respectively, assuming that the ESP is mounted at [/efi] like in the example from the Handbook:

[FILE] **`/efi/loader/entries/gentoo-sources-kernel.conf`Menu entry file**

    title Gentoo Linux
    linux /vmlinuz
    initrd /initramfs
    options root=/dev/sda3 quiet

For more options please refer to the [Bootloader Specification](https://uapi-group.org/specifications/specs/boot_loader_specification/#type-1-boot-loader-specification-entries)

### [Automatically generate menu entries]

Systemd\'s `kernel-install` can be used to automate the process of generating menu entry files (and initramfs) whenever `make install` is called during a kernel build. It is enabled with the [[[systemd-boot]](https://packages.gentoo.org/useflags/systemd-boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]]:

[FILE] **`/etc/portage/package.use/sd-boot`**

    sys-kernel/installkernel systemd systemd-boot

`root `[`#`]`emerge --ask sys-kernel/installkernel`

The options documented in [[[kernel-install(8)]](https://man.archlinux.org/man/kernel-install.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] can be used to customize the installed menu entries.

As an example, the [kernel cmdline](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters") can be customized by updating [/etc/kernel/cmdline]:

[FILE] **`/etc/kernel/cmdline`**

    root=/dev/sda3
    quiet

#### [Unified Kernel Images]

[Unified kernel images](https://wiki.gentoo.org/wiki/Unified_kernel_image "Unified kernel image") (UKIs) do not require a bootloader entry. Systemd-boot automatically discovers UKIs in the [EFI/Linux] directory on the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition"). If custom options should be applied when booting the UKI then it is possible to automate adding a bootloader entry with these custom options using a [kernel-install] plugin:

[FILE] **`/etc/kernel/install.d/95-uki-with-custom-opts.install`**

    #!/usr/bin/env bash

    COMMAND="$"
    KERNEL_VERSION="$"
    BOOT_DIR_ABS="$"
    KERNEL_IMAGE="$"

    if [[ "$" != "uki" ]]; then
        exit 0
    fi

    if [[ $ == add ]]; then
        cat > "$/loader/entries/1-gentoo-uki-$.conf" <<- EOF
            title Gentoo
            linux /EFI/Linux/$-$.efi
            options <my custom options>
            sort-key <my custom sort key>
        EOF
    elif [[ $ == remove ]]; then
        rm -f "$/loader/entries/1-gentoo-uki-$.conf"
    fi

### [Configuration in boot menu]

The default entry, increase/decrease timeout, edit command line options, and change resolution are accessible right from boot menu. Refer to [[[systemd-boot(7)]](https://man.archlinux.org/man/systemd-boot.7.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]'s KEY-BINDINGS section for keyboard shortcuts.

## [Usage]

### [[] Secure Boot]

If the [[[secureboot]](https://packages.gentoo.org/useflags/secureboot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is enabled on [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] or [[[sys-apps/systemd-utils]](https://packages.gentoo.org/packages/sys-apps/systemd-utils)[]], [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") recognizes the `SECUREBOOT_SIGN_KEY` and `SECUREBOOT_SIGN_CERT` environment variables which allow specifying a key (or pkcs11 URI) and certificate to sign the built EFI executable for use with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"). When [bootctl install] or [bootctl update] are called the signed version will be installed to the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition").

To successfully boot with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") enabled the firmware must be configured to accept the used certificate. Alternatively [[[sys-boot/shim]](https://packages.gentoo.org/packages/sys-boot/shim)[]] can be used to chain-load systemd-boot, the [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") binary is pre-signed with the 3rd-party Microsoft certificate which is accepted by default on most motherboards.

[FILE] **`/etc/portage/make.conf`make.conf**

    SECUREBOOT_SIGN_KEY="..."
    SECUREBOOT_SIGN_CERT="..."

** Note**\
At the time of this writing, the Shim is hard-coded to load and run the file named [grubx64.efi]. This problem can be circumvented by simply copying file [EFI\\systemd\\systemd-bootx64.efi] in the ESP to the directory where the Shim is installed, and renaming the file [grubx64.efi]. See the section below for a phase hook that automates this process.

### [ESP file update process]

Although updates to the systemd-boot related files are maintained by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), it will still be necessary for bootloader related files within the EFI System Partition to be updated each time the package manager updates the files within the package. This will provide important feature enhancement and bug fixes to the files within the ESP.

#### [systemd service]

systemd users can simply enable the service unit [systemd-boot-update] - if a handbook installation was completed this is probably already enabled. [systemd-boot-update] will check if the installed systemd-boot is outdated every time the system boots and will update it if required.

`root `[`#`]`systemctl enable --now systemd-boot-update.service`

#### [Portage hook]

Using a Portage hook (ebuild phase function^[\[1\]](#cite_note-1)^), systemd-boot can be automatically updated whenever the package is updated.

The following phase hook file will update systemd-boot and also set it up to work with [Shim](https://wiki.gentoo.org/wiki/Shim "Shim") if this package is installed.

[FILE] **`/etc/portage/env/sys-apps/systemd-utils`systemd-boot update hook**

    post_pkg_postinst()  || ewarn "Updating systemd-boot failed"

            # If shim is installed, copy it to ESP as well
            if use secureboot; then
                if has_version sys-boot/shim; then
                    ebegin "Updating shim"
                    local return=0
                    local bootpath=$(bootctl -p)
                    local sdbootpath=$/EFI/systemd/systemd-bootx64.efi
                    local grub4shimpath=$/EFI/BOOT/grubx64.efi
                    local shim=$/usr/share/shim/BOOTX64.EFI
                    local mm=$/usr/share/shim/mmx64.efi

                    # Copy shim to $/BOOT/BOOTX64.efi
                    cp "$" "$/EFI/BOOT/" || ( ewarn "Failed to install shim" && return=1 )
                    # And copy the corresponding MokManager
                    cp "$" "$/EFI/BOOT/" || ( ewarn "Failed to install MokManager" && return=1 )
                    # Copy systemd-boot to where shim looks for the bootloader
                    cp $ $ || ( ewarn \
                    "Failed to copy systemd-boot to location expected by shim" && return=1)
                    eend $ || ewarn "Updating shim failed"
                else
                    ewarn "sys-boot/shim is not installed! Ensure that your key is"
                    ewarn "registered with the system firmware or secure boot might fail!"
                fi
            fi
        else
            elog "No installation of systemd-boot detected, not updating"
            elog "systemd-boot. If the system is using systemd-boot as the"
            elog "bootloader then update it manually with: bootctl update."
        fi
    }

## [Troubleshooting]

### [][Failed to open boot loader directory /usr/lib/systemd/boot/efi: No such file or directory]

Problem: Running the [bootctl] command with the [install] or [update] subcommands results in the following output:

`root `[`#`]`bootctl install`

    Failed to open boot loader directory /usr/lib/systemd/boot/efi: No such file or directory

This is because the [bootctl] command cannot locate the architecture specific EFI files within the [/usr/lib/systemd/boot/efi]. Resolve by enabling the [[[boot]](https://packages.gentoo.org/useflags/boot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag and recompiling [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]].

[FILE] **`/etc/portage/package.use/systemd`Enable boot USE flag**

    sys-apps/systemd-254.3 boot

`root `[`#`]`emerge -1uN sys-apps/systemd`

## [See also]

-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

## [External resources]

-   [Boot Loader Specification](https://uapi-group.org/specifications/specs/boot_loader_specification/)
-   [ArchWiki systemd-boot](https://wiki.archlinux.org/title/systemd-boot)

1.  [[[↑](#cite_ref-1)] [[https://dev.gentoo.org/\~zmedico/portage/doc/portage.html#config-bashrc-ebuild-phase-hooks](https://dev.gentoo.org/~zmedico/portage/doc/portage.html#config-bashrc-ebuild-phase-hooks)]]