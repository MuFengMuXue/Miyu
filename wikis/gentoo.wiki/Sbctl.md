[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Sbctl&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/Foxboron/sbctl)

[[]][Package information](https://packages.gentoo.org/packages/app-crypt/sbctl)

[sbctl] (Secure boot manager) is a user-friendly secure boot key manager written in GO.

sbctl is capable of setting up [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot"), creating, enrolling, and managing keys, whilst also keeping track of files that need to be signed in the boot chain, verifying signed files, and checking secure boot status on your system.

This wiki page goes over how to install and use sbctl for setting up secure boot on your system. Please note that sbctl will enroll keys directly into the system\'s firmware. For alternatives methods that do not touch firmware settings, see the wiki page for [Shim](https://wiki.gentoo.org/wiki/Shim "Shim").

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [sbctl status]](#sbctl_status)
    -   [[2.2] [Generate new keys]](#Generate_new_keys)
    -   [[2.3] [Enroll keys into efi variables]](#Enroll_keys_into_efi_variables)
-   [[3] [Signing]](#Signing)
    -   [[3.1] [Signing the bootloader]](#Signing_the_bootloader)
        -   [[3.1.1] [GRUB]](#GRUB)
        -   [[3.1.2] [Systemd-boot]](#Systemd-boot)
        -   [[3.1.3] [Efibootmgr]](#Efibootmgr)
    -   [[3.2] [Signing the kernel]](#Signing_the_kernel)
        -   [[3.2.1] [Kernel]](#Kernel)
        -   [[3.2.2] [Unified kernel image]](#Unified_kernel_image)
    -   [[3.3] [Automated signing]](#Automated_signing)
-   [[4] [Verifying and checking status]](#Verifying_and_checking_status)
    -   [[4.1] [Verifying files]](#Verifying_files)
    -   [[4.2] [Checking secureboot status]](#Checking_secureboot_status)
-   [[5] [Configuration]](#Configuration)
    -   [[5.1] [Files]](#Files)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-crypt/sbctl](https://packages.gentoo.org/packages/app-crypt/sbctl) [[]] [Secure Boot key manager]

  ----------------------------------------------------------------- -----------------------------------------
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-31 22:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-crypt/sbctl`

## [Usage]

### [sbctl status]

Check the status of sbctl, secure boot must be turned off to enter setup mode.

`user `[`$`]`sbctl status`

    Installed: ✘ Sbctl is not installed
    Setup Mode: ✘ Enabled
    Secure Boot:    ✘ Disabled

### [Generate new keys]

Create new keys for signing efi variables.

`root `[`#`]`sbctl create-keys`

    Created Owner UUID a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
    Creating secure boot keys...✔
    Secure boot keys created!

### [Enroll keys into efi variables]

Enroll generated keys into efi variables with Microsoft vendor keys.

`root `[`#`]`sbctl enroll-keys -m `

    Enrolling keys to EFI variables...
    With vendor keys from microsoft...✔
    Enrolled keys to the EFI variables!

** Warning**\
Enrolling generated keys without vendor keys can be dangerous and could potentially brick a system, *including but not limited* to systems without integrated GPUs. See the [Arch Wiki](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Enrolling_Option_ROM_digests) and [sbctl](https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom) pages on Option ROM.

## [Signing]

** Tip**\
The [sbctl install hook](https://github.com/Foxboron/sbctl/blob/master/contrib/kernel-install/91-sbctl.install) automatically signs the following boot components when using [kernel-install] (see [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel")). However, the [[[secureboot]](https://packages.gentoo.org/useflags/secureboot)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] `USE` flag can also be used, given that the `SECUREBOOT_SIGN_KEY` and `SECUREBOOT_SIGN_CERT` are pointing to the newly generated key and certificate found in [/var/lib/sbctl/keys/db/].

### [Signing the bootloader]

#### [GRUB]

Signing the grub efi binary to be used in the boot chain.

`root `[`#`]`sbctl sign -s /efi/EFI/gentoo/grubx64.efi`

    ✔ Signed /efi/EFI/gentoo/grubx64.efi

** Note**\
Use [sbctl sign -s] instead of [sbctl sign] to automatically save files to be signed to [/var/lib/sbctl/files.json].

#### [Systemd-boot]

Signing the systemd-boot efi binary to be used in the boot chain.

`root `[`#`]`sbctl sign -s /efi/EFI/systemd/systemd-bootx64.efi`

    ✔ Signed /efi/EFI/systemd/systemd-bootx64.efi

#### [Efibootmgr]

Signing the efibootmgr efi binary to be used in the boot chain.

`root `[`#`]`sbctl sign -s /efi/EFI/BOOT/BOOTX64.efi`

    ✔ Signed /efi/EFI/BOOT/BOOTX64.efi

### [Signing the kernel]

#### [Kernel]

Signing the kernel image to be used in the boot chain.

`root `[`#`]`sbctl sign -s /boot/vmlinuz`

    ✔ Signed /boot/vmlinuz

#### [Unified kernel image]

Signing the unified kernel image to be used in the boot chain.

`root `[`#`]`sbctl sign -s /efi/EFI/Linux/linux-x.y.z-gentoo.efi`

    ✔ Signed /efi/EFI/Linux/linux-x.y.z-gentoo.efi

### [Automated signing]

Keys generated by `sbctl` can be used to [automatically sign](https://wiki.gentoo.org/wiki/Secure_Boot#USE_flags "Secure Boot") any EFI binaries installed by portage.

[FILE] **`/etc/portage/make.conf`make.conf**

    USE="$ secureboot modules-sign"
    # Default sbctl key locations
    MODULES_SIGN_KEY="/var/lib/sbctl/keys/db/db.key"
    MODULES_SIGN_CERT="/var/lib/sbctl/keys/db/db.pem"
    SECUREBOOT_SIGN_KEY="/var/lib/sbctl/keys/db/db.key"
    SECUREBOOT_SIGN_CERT="/var/lib/sbctl/keys/db/db.pem"

This only impacts newly installed EFI binaries; previously installed EFI binaries must still be manually signed with an above process.

## [Verifying and checking status]

### [Verifying files]

To check if all files are signed run.

`root `[`#`]`sbctl verify`

    Verifying file database and EFI images in /efi...
    ✔ /efi/EFI/gentoo/grubx64.efi is signed
    ✔ /efi/EFI/systemd/systemd-bootx64.efi is signed
    ✔ /efi/EFI/BOOT/BOOTX64.efi is signed
    ✔ /boot/vmlinuz is signed
    ✔ /efi/EFI/Linux/linux-x.y.z-gentoo.efi is signed

If files were not signed the command will output.

`root `[`#`]`sbctl verify`

    Verifying file database and EFI images in /efi...
    ✘ /efi/EFI/gentoo/grubx64.efi is not signed
    ✘ /efi/EFI/systemd/systemd-bootx64.efi is not signed
    ✘ /efi/EFI/BOOT/BOOTX64.efi is not signed
    ✘ /boot/vmlinuz is  not signed
    ✘ /efi/EFI/Linux/linux-x.y.z-gentoo.efi is not signed

### [Checking secureboot status]

To check if sbctl is installed correctly run.

`user `[`$`]`sbctl status`

    Installed: ✓ sbctl is installed
    Owner GUID: a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
    Setup Mode: ✔ Disabled
    Secure Boot:    ✘ Disabled
    Vendor Keys:    microsoft

After reboot the command will output.

`user `[`$`]`sbctl status`

    Installed: ✓ sbctl is installed
    Owner GUID: a9fbbdb7-a05f-48d5-b63a-08c5df45ee70
    Setup Mode: ✓ Disabled
    Secure Boot:    ✓ Enabled
    Vendor Keys:    microsoft

** Note**\
Once the sbctl setup is complete your next reboot will automatically enable secureboot upon boot.

## [Configuration]

By default sbctl does not need any configuration however if you wish to add paths to custom keys, binary paths, and kernel paths you can configure the file found in [/etc/sbctl/sbctl.conf.]

[FILE] **`/etc/sbctl/sbctl.conf`Default configuration**

    ---
    keydir: /var/lib/sbctl/keys
    guid: /var/lib/sbctl/GUID
    files_db: /var/lib/sbctl/files.json
    landlock: true
    db_additions:
    - microsoft
    files:
    - path: /boot/vmlinuz
      output: /boot/vmlinuz
    - path: /efi/EFI/Linux/linux-x.y.z-gentoo.efi
      output: /efi/EFI/Linux/linux-x.y.z-gentoo.efi
    keys:
      pk:
        privkey: /var/lib/sbctl/keys/PK/PK.key
        pubkey: /var/lib/sbctl/keys/PK/PK.pem
        type: file
      kek:
        privkey: /var/lib/sbctl/keys/KEK/KEK.key
        pubkey: /var/lib/sbctl/keys/KEK/KEK.pem
        type: file
      db:
        privkey: /var/lib/sbctl/keys/db/db.key
        pubkey: /var/lib/sbctl/keys/db/db.pem
        type: file

### [Files]

-   [/var/lib/sbctl] - Sbctl storage directory.
-   [/etc/sbctl/sbctl.conf] - Sbctl configuration file.
-   [/var/lib/sbctl/files.json] - File containing list of efi binaries to be signed.
-   [/var/lib/sbctl/GUID] Owner identification. Randomly generated UUID.
-   [/var/lib/sbctl/keys] - Keys directory.

## [See also]

-   [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") --- an enhancement of the security of the pre-boot process of a [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") system.
-   [Installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") --- a collection of scripts to automatically install new [kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel") and update [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") configuration
-   [Unified Kernel Image](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image") --- a single executable which can be [booted directly from UEFI firmware](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), or automatically sourced by boot-loaders with little or no configuration.