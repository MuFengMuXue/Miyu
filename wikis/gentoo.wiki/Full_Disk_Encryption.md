**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Disk_encryption "wikipedia:Disk encryption")

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/cryptsetup)

** Important**\
This is an advanced topic and requires some level of background knowledge. [Rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") on the other hand presents an introduction to the topic that is more akin to how other distributions handle disk encryption, which often makes it more desirable for most user needs.

Full disk encryption can be used to help protect data integrity and privacy. [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") can be used to configure drives to be encrypted with LUKS or other formats. This article is a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs. This process can be done as part of a fresh install, or could be performed on a new drive to migrate an existing install. It should be noted that most users don\'t require this level of encryption and is why the Handbook recommends to start with [Rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") first. This allows users to see if they require a stronger level of encryption more easily at a later date.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [LUKS headers]](#LUKS_headers)
        -   [[1.1.1] [Detached headers]](#Detached_headers)
    -   [[1.2] [Key files on a separate volume]](#Key_files_on_a_separate_volume)
    -   [[1.3] [Additional boot complexity]](#Additional_boot_complexity)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
    -   [[2.2] [Additional software]](#Additional_software)
-   [[3] [System preparation]](#System_preparation)
-   [[4] [Disk preparation]](#Disk_preparation)
    -   [[4.1] [Root device formatting]](#Root_device_formatting)
        -   [[4.1.1] [Boot device formatting]](#Boot_device_formatting)
            -   [[4.1.1.1] [Create the ESP]](#Create_the_ESP)
            -   [[4.1.1.2] [Optional: Create the Extended Boot partition]](#Optional:_Create_the_Extended_Boot_partition)
            -   [[4.1.1.3] [Write changes]](#Write_changes)
-   [[5] [LUKS Preparation]](#LUKS_Preparation)
    -   [[5.1] [Detached header]](#Detached_header)
    -   [[5.2] [Passphrase secured LUKS Header]](#Passphrase_secured_LUKS_Header)
        -   [[5.2.1] [Adding a Passphrase to Volume Using GPG Secured Key Files]](#Adding_a_Passphrase_to_Volume_Using_GPG_Secured_Key_Files)
    -   [[5.3] [Key File Secured Header]](#Key_File_Secured_Header)
        -   [[5.3.1] [Key File Creation]](#Key_File_Creation)
            -   [[5.3.1.1] [Basic key file creation]](#Basic_key_file_creation)
            -   [[5.3.1.2] [GPG Symmetrically Encrypted Key File]](#GPG_Symmetrically_Encrypted_Key_File)
            -   [[5.3.1.3] [GPG Asymmetrically Encrypted Key File]](#GPG_Asymmetrically_Encrypted_Key_File)
        -   [[5.3.2] [Key File Usage]](#Key_File_Usage)
            -   [[5.3.2.1] [luksFormat Using a Key File]](#luksFormat_Using_a_Key_File)
            -   [[5.3.2.2] [luksFormat Using a GPG protected keyfile]](#luksFormat_Using_a_GPG_protected_keyfile)
    -   [[5.4] [LUKS Header Backup]](#LUKS_Header_Backup)
-   [[6] [Filesystem Preparation]](#Filesystem_Preparation)
    -   [[6.1] [Open the LUKS volume]](#Open_the_LUKS_volume)
    -   [[6.2] [Format the Filesystems]](#Format_the_Filesystems)
        -   [[6.2.1] [Create optional btrfs subvolumes]](#Create_optional_btrfs_subvolumes)
-   [[7] [Initramfs configuration]](#Initramfs_configuration)
    -   [[7.1] [UgRD]](#UgRD)
        -   [[7.1.1] [Passphrase protected volume]](#Passphrase_protected_volume)
        -   [[7.1.2] [Detached headers]](#Detached_headers_2)
        -   [[7.1.3] [Symmetrically encrypted GPG keyfile]](#Symmetrically_encrypted_GPG_keyfile)
        -   [[7.1.4] [Yubikey Protected GPG keyfile]](#Yubikey_Protected_GPG_keyfile)
        -   [[7.1.5] [Updating an initramfs image]](#Updating_an_initramfs_image)
        -   [[7.1.6] [Manually creating an initramfs image]](#Manually_creating_an_initramfs_image)
        -   [[7.1.7] [Recovery]](#Recovery)
    -   [[7.2] [Dracut]](#Dracut)
        -   [[7.2.1] [Dracut module config]](#Dracut_module_config)
            -   [[7.2.1.1] [GPG config]](#GPG_config)
        -   [[7.2.2] [Dracut cmdline config]](#Dracut_cmdline_config)
            -   [[7.2.2.1] [Passphrase encryption]](#Passphrase_encryption)
            -   [[7.2.2.2] [GPG Keys]](#GPG_Keys)
        -   [[7.2.3] [Systemd]](#Systemd)
        -   [[7.2.4] [Manually generating an image]](#Manually_generating_an_image)
        -   [[7.2.5] [Extracting the initramfs]](#Extracting_the_initramfs)
    -   [[7.3] [Embedding the initramfs]](#Embedding_the_initramfs)
        -   [[7.3.1] [Embedding a directory]](#Embedding_a_directory)
        -   [[7.3.2] [Embedding an image]](#Embedding_an_image)
-   [[8] [Gentoo installation]](#Gentoo_installation)
    -   [[8.1] [Mount the root partition]](#Mount_the_root_partition)
    -   [[8.2] [fstab configuration]](#fstab_configuration)
    -   [[8.3] [Finalizing the Gentoo install]](#Finalizing_the_Gentoo_install)
-   [[9] [Additional information]](#Additional_information)
    -   [[9.1] [SSD tricks]](#SSD_tricks)
-   [[10] [See also]](#See_also)
-   [[11] [References]](#References)

## [Introduction]

True *Full Disk Encryption* is **not** something that helps in most threat models, and it requires using separate storage to store all elements required to boot. These include, but are not limited to:

-   The kernel image
-   The initramfs image
-   Detached headers
-   Keyfiles
-   The bootloader

** Note**\
The specific components required to boot a system depend on the design. The simplest systems could boot from a single kernel image which contains the initramfs, where a LUKS keyslot protected by a passphrase protects the root filesystem.

Storing the kernel, initramfs, and bootloader on a separate device than the rootfs can present more problems than benefits. None of these components should contain sensitive data that would benefit from encryption, and LUKS does not provide data authentication. Storage on another device may increase or decrease the risk of tampering - depending on the threat model.

The authenticity of files used to boot is generally more important than the privacy.

** Tip**\
Encryption provides *privacy*; signing provides *authenticity*

** See also**\
[Secure boot](https://wiki.gentoo.org/wiki/Secure_boot "Secure boot") can be used to *authenticate* boot files.

The ultimate result of *Full Disk Encryption* is a device that when powered off, only has seemingly random data written to the storage. [Rootfs Encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") only reveals that the system likely uses Linux.

** Note**\
If the header files are detached, there is no way to distinguish between a LUKS volume and random data.

### [LUKS headers]

** Important**\
The master key stored in a LUKS header is the final authentication factor protecting encrypted data.

By default, LUKS uses a keyslot system, where volume contents are encrypted using a master key which is protected by any key installed into a LUKS keyslot for that header. This is helpful because multiple keys can be used to decrypt drive contents, and keys can be changed without re-encrypting the volume. This behavior is important to understand because it means that adding a weak key into a keyslot can degrade security, even if the rest of the keyslots are well protected.

#### [Detached headers]

LUKS headers can be detached, meaning they are stored in a file outside of the protected volume, resulting in a partition that truly only contains encrypted data. While this may be beneficial, protection of the headers must be carefully considered. If the headers were obtained, a keyslot could be cracked offline. Improper storage of keyfiles could result in worse protection than the default attached headers.

** Warning**\
The benefits of this separation must be weighed against the risks of a detached header being obtained by an adversary. Reading the headers off a partition already requires physical or privileged system access.

### [Key files on a separate volume]

Key files must ultimately be stored on an unencrypted volume in order to be accessed to decrypt data. Unless these key files are stored safely, they can reduce security. Ideally, key files should be encrypted. GPG works well because smartcards such as a [YubiKey/GPG](https://wiki.gentoo.org/wiki/YubiKey/GPG "YubiKey/GPG") can be used to decrypt the key file.

** Warning**\
Using a LUKS keyslot with a good password is very secure. Using a separate GPG protected keyfile *may* add security with proper implementation, but could potentially reduce security. Using GPG ultimately makes the most sense when using a smartcard.

### [Additional boot complexity]

Without encryption, the boot process is already very complex. Adding any type of root filesystem encryption takes this complexity to another level, because some mechanism must decrypt the root filesystem so the kernel can start the *init* process. Although most LUKS operations are handled by the *dm-crypt* kernel module, userspace tools are required to perform them.

An early boot environment, such as an initramfs, is typically used to perform drive decryption during the boot process. This initramfs does not require much - depending on the encryption scheme. A very simple initramfs could just contain tools such as [mount], [cryptsetup], and [switch_root]. First, [/dev], [/sys], and [/proc] must be mounted, then [cryptsetup] can be used to open and map the drive, and it can finally be mounted and [switch_root] can be used to change to the newly mounted root filesystem and start the init process.

[[[sys-kernel/dracut]](https://packages.gentoo.org/packages/sys-kernel/dracut)[]] is able to handle this with some configuration, while [[[sys-kernel/ugrd]](https://packages.gentoo.org/packages/sys-kernel/ugrd)[]] is built for this specific purpose.

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-fs/cryptsetup`

### [Additional software]

If using GPG to further secure key files:

`root `[`#`]`emerge --ask app-crypt/gnupg`

## [System preparation]

** Important**\
The kernel must be configured according to: [Dm-crypt: Kernel Configuration](https://wiki.gentoo.org/wiki/Dm-crypt#Kernel_Configuration "Dm-crypt").

If this is being followed as part of a fresh Gentoo install, the install procedure can be followed until the following step: [AMD64 Handbook: Designing a partition scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation")

If converting an existing system to an encrypted setup, either new storage must be added, or this procedure could be used to create new partitions using free space, where the data can then be copied after creation.

** Warning**\
Depending on the type of drive, it can be difficult or impossible to truly overwrite portions of the drive where unencrypted, but de-referenced data exists. It is best to do a [Secure wipe](https://wiki.gentoo.org/wiki/Secure_wipe "Secure wipe") using the drive\'s firmware before re-using it.

** Tip**\
If migrating an existing install to an encrypted root filesystem, the existing bootloader partition itself does not need to be modified (unless desired), but the bootloader configuration will need modification to boot from the new encrypted partitions.

## [Disk preparation]

** Important**\
Partitioning typically does not involve modification of any of the data in partitions. If a drive is re-partitioned then encrypted, old data may remain in an unencrypted form until it is overwritten.

** Note**\
Modern storage devices **may not** be securely erased with something like [dd if=/dev/urandom of=/dev/sdX].

** See also**\
For more information, see: [Secure wipe](https://wiki.gentoo.org/wiki/Secure_wipe "Secure wipe").

This example will use GPT as disk partition schema and [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") as boot loader. [fdisk] will be used as the partitioning tool though any partitioning utility will work.

** See also**\
For more information about GPT and EFI, see [Disks (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks").

For full disk encryption with a boot USB:

[CODE]

    /dev/sda
     └── /dev/sda1      [EFI]   /efi      16 GB        fat32       Bootloader, support files, kernel and initramfs
    /dev/nvme0n1
     └── /dev/nvme0n1p1 [ROOT]  (root)    ->END        luks        Encrypted root device, mapped to the name 'root'
          └──  /dev/mapper/root /         ->END        btrfs       root filesystem
                                /home     subvolume                Subvolume created for the home directory
                                /var      subvolume                Subvolume created for the var directory
                                /etc      subvolume                Subvolume created for the etc directory

** Tip**\
Using an external storage device, such as a USB drive, may make sense to use as a boot drive. A USB can be easily removed once the system is booted, debugged more easily than an internal drive.

For full disk encryption, using a separate boot drive with a split boot layout:

[CODE]

    /dev/sda
     ├── /dev/sda1      [EFI]   /efi      1 GB         fat32       Bootloader
     └── /dev/sda2      [BOOTX] /boot     1 GB         ext4        Bootloader support files, kernel and initramfs
    /dev/nvme0n1
     └── /dev/nvme0n1p1 [ROOT]  (root)    ->END        luks        Encrypted root device, mapped to the name 'root'
          └──  /dev/mapper/root /         ->END        btrfs       root filesystem
                                /home     subvolume                Subvolume created for the home directory
                                /var      subvolume                Subvolume created for the var directory
                                /etc      subvolume                Subvolume created for the etc directory

** Important**\
Use of an extended boot partition requires bootloader support.

** Tip**\
Any filesystem type can be used for the root filesystem, but [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") is used here. In most cases, FAT32 must be used for the EFI/boot partitions. If a separate extended boot partition is required, it must be readable by the bootloader.

** Note**\
Some devices will not boot using EFI system partitions which are too small (typically due to sector sizes^[\[1\]](#cite_note-1)^) , **512MB**+ typically works.

### [Root device formatting]

To create a partition layout using fdisk, start by creating a fresh partition table on the root disk, [/dev/nvme0n1]:

`root `[`#`]`fdisk /dev/nvme0n1`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0x81391dbc.

    Command (m for help): g
    Created a new GPT disklabel (GUID: 8D91A3C1-8661-2940-9076-65B815B36906).

With a partition table crated, a new partition spanning the drive can be created by using **n** and then accepting the defaults:

`Command (m for help):``n`

    Partition number (1-128, default 1):
    First sector (2048-1953525134, default 2048):
    Last sector, +/-sectors or +/-size (2048-1953525134, default 1953523711):

    Created a new partition 1 of type 'Linux filesystem' and of size 931.5 GiB.

The **Linux Root (x86-64)** property can be set using **t**:

`Command (m for help):``t`

    Partition number (1, default 1):
    Partition type or alias (type L to list all): 23
    Changed type of partition 'Linux filesystem' to 'Linux Root (x86-64)'.

** Note**\
Setting this property is optional, but if set, should match the architecture of the system.

Finally, the changes can be written with **w**:

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

#### [Boot device formatting]

The boot disk can be setup using a similar process, the main difference is the boot flags will be set as a final step:

`root `[`#`]`fdisk /dev/sda`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0x81391dbc.

    Command (m for help): g

    Created a new GPT disklabel (GUID: 3E57DFCE-CDD9-6F42-8418-F0B6B4A08294).

##### [Create the ESP]

With a fresh partition table, a 1GB partition for the ESP can be created using:

`Command (m for help):``n`

    Partition number (1-128, default 1):
    First sector (2048-121008094, default 2048):
    Last sector, +/-sectors or +/-size (2048-121008094, default 121006079): +1G

    Created a new partition 1 of type 'Linux filesystem' and of size 1 GiB.

** Note**\
This partition could span the entire device if an *Extended Boot* partition is not required.

The **ESP** properties can be set using **t**:

`Command (m for help):``t`

    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

##### [Optional: Create the Extended Boot partition]

The *Extended Boot* partition can be created with:

`Command (m for help):``n`

    Partition number (2-128, default 2):
    First sector (2099200-121008094, default 2099200):
    Last sector, +/-sectors or +/-size (2099200-121008094, default 121008094): +1G

    Created a new partition 2 of type 'Linux filesystem' and of size 1 GiB.

The **Linux Extended Boot** property can be set using **t**:

`Command (m for help):``t`

    Partition number (1-2, default 2):
    Partition type or alias (type L to list all): 142
    Changed type of partition 'Linux filesystem' to 'Linux Extended Boot'.

##### [Write changes]

Changes can be written with **w**:

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

## [LUKS Preparation]

To prepare the encrypted filesystem, [cryptsetup] can be used. Passwords and keys protect key slots on the LUKS header, which contains the master key that actually encrypts the partition data.

** Tip**\
More advanced usage information is available in [man cryptsetup-luksFormat].

** Important**\
Only specify arguments like **\--cipher** if certain that it improves security beyond the sane defaults.

### [Detached header]

** Important**\
The header file must be kept safe. If the header file is lost, all data on the LUKS partition it secured will be irrecoverable.

LUKS partitions can be created with a detached header using `--header ` ex:

`root `[`#`]`cryptsetup luksFormat --header /media/sda2/luks_header.img /dev/nvme0n1p1`

### [Passphrase secured LUKS Header]

The most basic way to configure an encrypted volume is to use:

`root `[`#`]`cryptsetup luksFormat --key-size 512 /dev/nvme0n1p1`

    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters):
    YES
    Enter passphrase for /dev/nvme0n1p1:

** Note**\
For a bit of additional security, the key size can be increased to 512 bits with **\--key-size 512**.

** Warning**\
A keyfile is typically considered to be more secure than a password, but should be password protected. An attacker must *have* the keyfile and *know* the password to break the drive\'s encryption.

** Tip**\
Luks can allow multiple keys/passwords to be used to decrypt a partition. This can potentially decrease security, if password is wanted to recovery purposes, consider using a long **passphrase** and writing it down, or storing it offline.

#### [Adding a Passphrase to Volume Using GPG Secured Key Files]

To add a passphrase to a volume which is already secured using key files, a named pipe must be used for the key file contents:

`root `[`#`]`mkfifo key_pipe`

Then the key can be decrypted to this pipe:

`root `[`#`]`gpg --decrypt key_file > key_pipe &`

A passphrase can be added with:

`root `[`#`]`cryptsetup luksAddKey --key-file key_pipe /dev/nvme0n1p1`

The named pipe can be cleaned up with:

`root `[`#`]`rm key_pipe`

### [Key File Secured Header]

Instead of securing the LUKS keyslots with a passphrase, keyfiles can be used.

** Important**\
Key files should be stored some place other than the devices they encrypt. A key file is a *possession* security factor, while passwords or passphrases are *knowledge* factors. What good is a lock if the keys are attached to it?

** Warning**\
Take great care of this key file, if it is lost, the entire encrypted partition will be inaccessible, if it is stolen, the data is no longer safe. If it is ever written to unencrypted storage, or transmitted over a malicious network, it cannot be considered safe.

** Tip**\
Using [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") to encrypt the key file can help keep it safe, adding a *knowledge* factor to it.

#### [Key File Creation]

** Important**\
This guide shows the keys being written to [/dev/sda2] which would be the boot partition. Formatting is described later. The keys can be stored anywhere the initramfs can read.

Keyfiles can be created and stored in a variety of ways. It is recommended to encrypt keyfiles, so they cannot just be stolen and used.

##### [Basic key file creation]

A basic key file can be created using *dd* and [/dev/urandom]:

`/media/sda2/ #``dd bs=8388608 count=1 if=/dev/urandom of=crypt_key.luks`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 0.014407 s, 582 MB/s

** Tip**\
**cryptsetup \--help** reveals the builtin key size and character size limit. The default is **8388608**, or *8192 \* 1024* (*2\^23*).

##### [GPG Symmetrically Encrypted Key File]

For increased security, the key file can be immediately encrypted with [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG").

** Warning**\
Symmetric encryption, using a password, is a simple method that works on most systems, but is vulnerable to keylogging, similarly to simple password/passphrase based protection.

** Important**\
If using the Gentoo install ISO, it may be necessary to run

`root `[`#`]`export GPG_TTY=$(tty)`

to GPG encrypt data directly from **stdout**. Alternatively, **\--pinentry-mode loopback** can be added as an argument to use stdin pinentry, however, this does not confirm the entry.

`/media/sda2/ #``dd bs=8388608 count=1 if=/dev/urandom | gpg --symmetric --cipher-algo AES256 --output crypt_key.luks.gpg`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 7.50139 s, 1.1 MB/s

##### [GPG Asymmetrically Encrypted Key File]

A key file can be protected using public key cryptography using a smartcard such as a [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey"). [This YubiKey GPG guide](https://wiki.gentoo.org/wiki/YubiKey/GPG "YubiKey/GPG") can be used to generate [GPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") keys on a YubiKey. With the public keys loaded, keys can be encrypted with the key holder as the recipient:

`/media/sda2/ #``dd bs=8388608 count=1 if=/dev/urandom | gpg --recipient larry@gentoo.org --output crypt_key.luks.gpg --encrypt`

    1+0 records in
    1+0 records out
    8388608 bytes (8.4 MB, 8.0 MiB) copied, 7.50139 s, 1.1 MB/s

** Important**\
Dracut must be configured to use the corresponding public key, this is covered in the Dracut section.

When booting, ensure the smartcard is inserted. Dracut will prompt for the PIN, and depending on the configuration, the device may need to be tapped to complete presence detection.

#### [Key File Usage]

##### [luksFormat Using a Key File]

To secure the partition using a plain key file:

`/media/sda2/ #``cryptsetup --key-size 512 luksFormat /dev/nvme0n1p1 crypt_key.luks`

    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters): YES

To add this keyfile to an already encrypted partition:

`/media/sda2/ #``cryptsetup luksAddKey /dev/nvme0n1p1 crypt_key.luks`

    Enter any existing passphrase:

##### [luksFormat Using a GPG protected keyfile]

To secure the partition using a GPG protected key file:

`/media/sda2/ #``gpg --decrypt crypt_key.luks.gpg | cryptsetup luksFormat --key-size 512 /dev/nvme0n1p1 -`

    gpg: AES256.CFB encrypted data
    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p1 irrevocably.

    Are you sure? (Type 'yes' in capital letters): YES

To add the GPG encrypted keyfile to an already encrypted partition, named pipes must be used to avoid decrypting the key to disk, as both **gpg** and **cryptsetup** are expecting input from stdin:

`/media/sda2/ #``mkfifo crypt_key`

`/media/sda2/ #``mkfifo cryptsetup_pass`

Once the files are created, the key must be decrypted to *crypt_key*, and the recovery passphrase must be passed to *cryptsetup_pass*:

`/media/sda2/ #``gpg --decrypt crypt_key.luks.gpg > crypt_key &`

`/media/sda2/ #``read -s -r -p 'LUKS passphrase: ' CRYPT_PASS; echo "$CRYPT_PASS" > cryptsetup_pass &`

Finally, **cat** can be used to pass this information to **cryptsetup**:

`/media/sda2/ #``cat cryptsetup_pass crypt_key | cryptsetup luksAddKey /dev/nvme0n1p1 -`

    gpg: AES256.CFB encrypted data
    gpg: encrypted with 1 passphrase
    [1]-  Done                    read -s -r -p 'LUKS passphrase: ' CRYPT_PASS; echo "$CRYPT_PASS" > cryptsetup_pass
    [2]+  Done                    gpg -d crypt_key.luks.gpg > crypt_key

** Tip**\
LUKS key status can be checked with **cryptsetup luksDump **, ex. **cryptsetup luksDump /dev/nvme0n1p1**.

** Note**\
The named pipes can now be deleted.

### [LUKS Header Backup]

** Important**\
Do not forget this step, keys/passwords are used to decrypt the LUKS header, if it is destroyed for some reason, the remaining data will only be recoverable with the header file.

The headers can be backed up with:

`root `[`#`]`cryptsetup luksHeaderBackup /dev/nvme0n1p1 --header-backup-file crypt_headers.img`

** Note**\
If using detached headers, be sure to back up the header file.

## [Filesystem Preparation]

With the LUKS volume created, it must be mapped so the underlying filesystems can be created.

### [Open the LUKS volume]

The encrypted device must be opened and mapped before it can be used, this can be done with:

`root `[`#`]`cryptsetup luksOpen /dev/nvme0n1p1 root`

** Tip**\
If the LUKS headers are detached, they can be specified with `--header `.

If using a key file:

`/media/sda2/ #``cryptsetup --key-file crypt_key.luks open /dev/nvme0n1p1 root`

If using a GPG encrypted key file:

`/media/sda2/ #``gpg --decrypt crypt_key.luks.gpg | cryptsetup --key-file - open /dev/nvme0n1p1 root`

** Note**\
This command opens [/dev/nvme0n1p1] and maps it under [/dev/mapper/] with the name **root**.

### [Format the Filesystems]

To create a filesystem for [/dev/sda1], the *EFI System Partition* which will contain GRUB. This partition is read by UEFI. Most motherboards can read only a [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT") filesystem:

`root `[`#`]`mkfs.vfat -F32 /dev/sda1`

To create an *Extended Boot* filesystem, which the bootloader will read the kernel and initramfs from:

`root `[`#`]`mkfs.ext4 -L boot /dev/sda2`

** Note**\
This partition can be any filesystem which the bootloader can read. Some bootloaders, such as [systemd-boot](https://wiki.gentoo.org/wiki/Systemd/systemd-boot "Systemd/systemd-boot"), only support filesystems from the firmware (i.e. FAT) and may require additional UEFI drivers to be placed in the EFI System Partition, in order to read ext4 filesystems. When in doubt, default to [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT").

To create the [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") root filesystem on the LUKS partition:

`root `[`#`]`mkfs.btrfs -L rootfs /dev/mapper/root`

** Note**\
The labels are optional, but helpful. They allow for easy mounting without a UUID.

#### [Create optional btrfs subvolumes]

To create subvolumes for [/etc], [/home], and [/var], the filesystem must first be mounted:

`root `[`#`]`mount LABEL=rootfs /mnt/gentoo`

Then each subvolume can be created:

`root `[`#`]`btrfs subvolume create /mnt/gentoo/etc `

`root `[`#`]`btrfs subvolume create /mnt/gentoo/home `

`root `[`#`]`btrfs subvolume create /mnt/gentoo/var`

## [Initramfs configuration]

** Important**\
An initramfs must be used to decrypt and mount the root partition.

[[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] supports 2 initramfs generators:

-   [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") - A dynamic initramfs built on udev.
-   [UgRD](https://wiki.gentoo.org/wiki/UgRD "UgRD") - A minimalistic initramfs built specifically for the host.

### [UgRD]

[UgRD](https://wiki.gentoo.org/wiki/UgRD "UgRD") or \"microgram ramdisk\" is designed specifically to decrypt LUKS volumes on Gentoo systems. It uses [[[app-misc/pax-utils]](https://packages.gentoo.org/packages/app-misc/pax-utils)[]] to resolve libraries for binaries needed in the early boot environment and generates a simple init script to handle this decryption.

Unlike Dracut, UGRD attempts to automatically configure mount and LUKS configuration, and validates the configuration before creating a CPIO. UGRD also makes smaller, simpler, and faster images than Dracut. This is possible because UGRD determines requirements and the boot process at build time, while Dracut is dynamic and responds to events at runtime.

** Tip**\
Users are encouraged to read the generated init file(s) under **[out_dir]** (default [/tmp/initramfs_build]).

UGRD is available in the Gentoo repository and can be installed with:

`root `[`#`]`emerge --ask sys-kernel/ugrd`

`user `[`$`]`ugrd --help`

    ugrd --help
    usage: ugrd [-h] [-d] [-dd] [-v] [--log-file LOG_FILE] [--log-level LOG_LEVEL] [--log-time] [--no-log-color] [--build-logging] [--no-build-logging] [-c CONFIG]
                [-m MODULES] [--kernel-version KERNEL_VERSION] [--clean] [--no-clean] [--compress] [--no-compress] [--rotate] [--no-rotate] [--validate]
                [--no-validate] [--hostonly] [--no-hostonly] [--lspci] [--no-lspci] [--lsmod] [--no-lsmod] [--firmware] [--no-firmware] [--autodetect-root]
                [--no-autodetect-root] [--autodetect-root-luks] [--no-autodetect-root-luks] [--autodetect-root-lvm] [--no-autodetect-root-lvm] [--autodetect-root-dm]
                [--no-autodetect-root-dm] [--no-kmod] [--print-config] [--print-init] [--test] [--test-kernel TEST_KERNEL] [--livecd-label LIVECD_LABEL]
                [out_file]

    MicrogRAM disk initramfs generator

    positional arguments:
      out_file              set the output image location

    options:
      -h, --help            show this help message and exit
      -d, --debug           enable debug mode (level 10)
      -dd, --trace          enable trace debug mode (level 5)
      -v, --version         print the version and exit
      --log-file LOG_FILE   set the path to the log file
      --log-level LOG_LEVEL
                            set the log level
      --log-time            enable log timestamps
      --no-log-color        disable log color
      --build-logging       enable additional build logging
      --no-build-logging    disable additional build logging
      -c CONFIG, --config CONFIG
                            set the config file location
      -m MODULES, --modules MODULES
                            Define config modules to load, comma separated
      --kernel-version KERNEL_VERSION, --kver KERNEL_VERSION
                            set the kernel version
      --clean               clean the build directory at runtime
      --no-clean            disable build directory cleaning
      --compress            compress the final image
      --no-compress         don't compress the final image
      --rotate              rotate old cpio images
      --no-rotate           don't rotate old cpio images
      --validate            enable configuration validation
      --no-validate         disable config validation
      --hostonly            enable hostonly mode, required for automatic kmod detection
      --no-hostonly         disable hostonly mode
      --lspci               use lspci to auto-detect kmods
      --no-lspci            do not use lspci to auto-detect kmods
      --lsmod               use lsmod to auto-detect kmods
      --no-lsmod            do not use lsmod to auto-detect kmods
      --firmware            include firmware files found with modinfo
      --no-firmware         exclude firmware files
      --autodetect-root     autodetect the root partition
      --no-autodetect-root  do not autodetect the root partition
      --autodetect-root-luks
                            autodetect LUKS volumes under the root partition
      --no-autodetect-root-luks
                            do not autodetect root LUKS volumes
      --autodetect-root-lvm
                            autodetect LVM volumes
      --no-autodetect-root-lvm
                            do not autodetect LVM volumes
      --autodetect-root-dm  autodetect DM (LUKS/LVM) root partitions
      --no-autodetect-root-dm
                            do not autodetect root DM volumes
      --no-kmod             Allow images to be built without kmods/kernel info
      --print-config        print the final config dict
      --print-init          print the final init structure
      --test                Tests the image with qemu
      --test-kernel TEST_KERNEL
                            Tests the image with qemu using a specific kernel file.
      --livecd-label LIVECD_LABEL
                            Sets the label for the livecd

** Note**\
[[[sys-kernel/ugrd]](https://packages.gentoo.org/packages/sys-kernel/ugrd)[]] installs default config at [/etc/ugrd/config.toml].

#### [Passphrase protected volume]

If using plain passphrase protection, ugrd should automatically detect it. Look for the following lines when running ugrd:

[CODE]

    INFO     | [root] Detected LUKS volume uuid: 4bb45bd6-9ed9-44b3-b547-b411079f043b
    INFO     | [root] Configuring cryptsetup for LUKS mount (root) on: /dev/nvme1n1p1

#### [Detached headers]

** Important**\
Detaching the headers from a **LUKS** volume removes any **[UUID]** values from the partition. Instead, another identifier needs to be passed to `[cryptsetup.root]`, such as **[PARTUUID]**.

To use UGRD to decrypt a LUKS volume with detached headers, stored at [/boot] (Boot support):

[FILE] **`/etc/ugrd/config.toml`**

    # This configuration should autodetect root/luks info and use detached headers

    modules = [
      "ugrd.kmod.usb",
      "ugrd.crypto.cryptsetup"
    ]

    auto_mounts = ['/boot']

    #[mounts.boot]
    #type = "vfat"
    #uuid = "BDF2-0139"

    [cryptsetup.root]
    header_file = "/boot/luks_header.img"
    # partuuid = f0273847-2754-4961-b64e-307c30097396  # should be autodetected

#### [Symmetrically encrypted GPG keyfile]

To use UGRD with a GPG encrypted keyfile at [/boot/crypt_key.luks.gpg]:

[FILE] **`/etc/ugrd/config.toml`**

    modules = [
      "ugrd.kmod.usb",
      "ugrd.crypto.gpg"
    ]

    auto_mounts = ['/boot']

    [cryptsetup.root]
    #uuid = "4bb45bd6-9ed9-44b3-b547-b411079f043b"  # should be autodetected
    key_type = "gpg"
    key_file = "/boot/crypt_key.luks.gpg"

#### [Yubikey Protected GPG keyfile]

To use UGRD with a YubiKey to decrypt [/boot/crypt_key.luks.gpg] with the public key at [/etc/ugrd/pubkey.gpg]:

[FILE] **`/etc/ugrd/config.toml`**

    modules = [
      "ugrd.kmod.usb",
      "ugrd.crypto.smartcard"
    ]

    sc_public_key = "/etc/ugrd/pubkey.gpg"

    auto_mounts = ['/boot']

    [cryptsetup.root]
    #uuid = "4bb45bd6-9ed9-44b3-b547-b411079f043b"  # should be autodetected
    key_type = "gpg"
    key_file = "/boot/crypt_key.luks.gpg"
    try_nokey = true

** Note**\
**[try_nokey]** under `[cryptsetup.<mapped_name>]` is disabled by default and allows plain passphrase keyslots to be used as a final attempt for decryption.

#### [Updating an initramfs image]

If the **[ugrd]** USE flag is set on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]], the initramfs can be regenerated and reinstalled with:

`root `[`#`]`emerge --config gentoo-kernel`

** Tip**\
This procedure works on any *dist-kernel* package.

#### [Manually creating an initramfs image]

UGRD can be used to create an initramfs image based on the current kernel version simply by running it as root:

`root `[`#`]`ugrd`

    INFO     | Intializing class: InitramfsGenerator
    INFO     | Intializing class: InitramfsConfigDict
    INFO     | Module version: 2.1.0
    INFO     | Processing module: ugrd.base.base
    INFO     | Processing module: ugrd.base.core
    INFO     | Adding library path: /usr/lib64
    INFO     | Processing module: ugrd.fs.mounts
    INFO     | Processing module: ugrd.base.cmdline
    INFO     | Processing module: ugrd.kmod.kmod
    INFO     | Processing module: ugrd.fs.cpio
    INFO     | Processing module: ugrd.base.checks
    INFO     | Loading config file: /etc/ugrd/config.toml
    INFO     | Processing module: ugrd.crypto.smartcard
    INFO     | Processing module: ugrd.crypto.gpg
    INFO     | Processing module: ugrd.base.console
    INFO     | Registered custom init function: custom_init
    INFO     | Processing module: ugrd.crypto.cryptsetup
    INFO     | Adding library path: /usr/lib/gcc/x86_64-pc-linux-gnu/13
    INFO     | Processing module: ugrd.kmod.nvme
    INFO     | Processing module: ugrd.kmod.usb
    INFO     | Processing module: ugrd.kmod.standard_mask
    INFO     | Processing module: ugrd.kmod.nosound
    INFO     | Processing module: ugrd.kmod.novideo
    INFO     | Processing module: ugrd.kmod.nonetwork
    INFO     | [ugrd.crypto.cryptsetup:root] No retries specified, using default: 5
    INFO     | Building initramfs
    INFO     | Detected init at: /usr/bin/init
    WARNING  | Cleaning build directory: /tmp/initramfs_build
    INFO     | Source path for libgcc_s: /usr/lib/gcc/x86_64-pc-linux-gnu/13/libgcc_s.so.1
    INFO     | Found device mapper devices: dm-0
    INFO     | Auto-enabling kernel modules for device: dm_mod
    INFO     | Autodetected root type: btrfs
    INFO     | Autodetected root source: uuid=8537843e-e479-4379-8fc2-a76139d59505
    INFO     | [mounts] Updating mount: root
    INFO     | Auto-enabling module: btrfs
    INFO     | Processing module: ugrd.fs.btrfs
    INFO     | Detected a device mapper mount: /dev/mapper/root
    INFO     | [root] LUKS volume uuid: 20447cd7-5d64-477a-9c95-fdbd30fb61af
    INFO     | [root] Configuring cryptsetup for LUKS mount (root) on: dm-0
    root:
      key_type: gpg
      key_file: /boot/root.luks.gpg
      try_nokey: True
      key_command: gpg --decrypt /boot/root.luks.gpg
      reset_command: gpgconf --reload && gpg --card-status
      retries: 5
      uuid: 20447cd7-5d64-477a-9c95-fdbd30fb61af

    INFO     | Auto-enabling kernel modules for device: nvme
    INFO     | Using detected kernel version: 6.6.47-custom
    INFO     | Adding GPG public key file to dependencies: /etc/ugrd/pubkey.gpg
    INFO     | [deploy_nodes] Skipping real device node creation with mknod, as mknod_cpio is not specified.
    INFO     | Regenerating kernel module metadata files.
    INFO     | Running init generator functions
    INFO     | Init kernel modules: dm_crypt, uhid, nvme, uas, usbcore, scsi_mod, ehci_hcd, ohci_hcd, uhci_hcd, xhci_hcd, vfat, dm_mod, btrfs
    INFO     | Included kernel modules: nvme_core, usb_storage, ehci_pci, fat, nvme_common, crc32c
    WARNING  | 'cryptsetup_prompt' is disabled, if the 'quiet' kernel parameter is not set, the prompt may be hidden under log messages at runtime.
    INFO     | Wrote file: /tmp/initramfs_build/etc/profile
    INFO     | Included functions: check_var, setvar, readvar, prompt_user, retry, edebug, einfo, ewarn, eerror, rd_fail, rd_restart, _find_init, mount_root, parse_cmdline_bool, parse_cmdline_str, get_crypt_dev, mount_base, export_exports, parse_cmdline, load_modules, mount_fstab, crypt_init, mount_cmdline_root, do_switch_root
    INFO     | Wrote file: /tmp/initramfs_build/init_main.sh
    INFO     | Wrote file: /tmp/initramfs_build/init
    INFO     | Wrote file: /tmp/initramfs_build/etc/fstab
    WARNING  | Deleting old file: /tmp/initramfs_out/ugrd-6.6.47-custom.old.1
    INFO     | [1] Cycling file: /tmp/initramfs_out/ugrd-6.6.47-custom.old -> /tmp/initramfs_out/ugrd-6.6.47-custom.old.1
    INFO     | [0] Cycling file: /tmp/initramfs_out/ugrd-6.6.47-custom.cpio -> /tmp/initramfs_out/ugrd-6.6.47-custom.old
    INFO     | Wrote 63.27 MiB to: /tmp/initramfs_out/ugrd-6.6.47-custom.cpio
    INFO     | Completed checks.

** Note**\
By default, [ugrd] will build in [/tmp/initramfs_build] and will output to [/tmp/initramfs_out]. The configuration files above define the output dir to [/usr/src/initramfs].

** Tip**\
The [ugrd] package will install [[[sys-kernel/installkernel-gentoo]](https://packages.gentoo.org/packages/sys-kernel/installkernel-gentoo)[]] hooks automatically, making it run when [make install] is used against the Linux kernel sources.

To create an image for a specific kernel version, and output it to [/boot/]:

`root `[`#`]`ugrd --kver 6.6.47-gentoo /boot/initramfs-6.6.47-gentoo.img`

#### [Recovery]

If a step fails in UGRD, it will generally try to re-exec the init from the top, and will keep attempting this until it is successful, or the device is rebooted.

UGRD attempts to halt and wait for user input before continuing after a failure.

** Note**\
Older versions of UGRD opened a new [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") shell on failure, this isn\'t ideal for security, and was difficult to use properly.

### [Dracut]

** Important**\
This configuration should be done while chrooted, or on a live system.

#### [Dracut module config]

The following modules must be added to the *add_dracutmodules* directive in [/etc/dracut.conf]:

[FILE] **`/etc/dracut.conf`Minimum required components to decrypt LUKS volumes using dracut**

    add_dracutmodules+=" crypt dm rootfs-block "

** Important**\
The spacing for Dracut configuration directives is very important. Ensure there are no spaces between *add_dracutmodules* and *+=\"*, parameters in *add_dracutmodules* must be padded with spaces.

##### [GPG config]

If GPG keys are being used, the following module must also be added: **crypt-gpg**

[FILE] **`/etc/dracut.conf`Minimum required components to decrypt LUKS volumes using dracut**

    add_dracutmodules+=" crypt crypt-gpg dm rootfs-block "

** Important**\
If a smartcard is used to store the private keys for a GPG encrypted key file, [/etc/dracut.conf.d/crypt-public-key.gpg] must be configured to contain the corresponding public key.

#### [Dracut cmdline config]

Dracut can be configured to build with configuration for LUKS hardcoded, first disk information must be obtained:

`root `[`#`]`lsblk -o name,uuid`

    NAME        UUID
    sda
    ├──sda1     BDF2-0139
    └──sda2     0e86bef-30f8-4e3b-ae35-3fa2c6ae705b
    nvme0n1
    └─nvme0n1p1 4bb45bd6-9ed9-44b3-b547-b411079f043b
      └─root    cb070f9e-da0e-4bc5-825c-b01bb2707704

##### [Passphrase encryption]

To open a LUKS volume protected with passphrase encryption:

[FILE] **`/etc/dracut.conf`**

    kernel_cmdline+=" root=UUID=cb070f9e-da0e-4bc5-825c-b01bb2707704 rd.luks.uuid=4bb45bd6-9ed9-44b3-b547-b411079f043b "

##### [GPG Keys]

To open a gpg keyfile protected LUKS volume:

[FILE] **`/etc/dracut.conf`Embed cmdline parameters for rootfs decryption**

    kernel_cmdline+=" root=LABEL=crypt rd.luks.uuid=4bb45bd6-9ed9-44b3-b547-b411079f043b rd.luks.key=/crypt_key.luks.gpg:UUID=0e86bef-30f8-4e3b-ae35-3fa2c6ae705b "

** Note**\
The UUID of the volume containing the keyfiles is specified after the *:* with the `rd.luks.key` argument.

#### [Systemd]

For systemd systems, rebuild with the **cryptsetup** USE-flag:

[FILE] **`/etc/portage/package.use/systemd`**

    sys-apps/systemd cryptsetup

`root `[`#`]`emerge --ask --newuse sys-apps/systemd`

#### [Manually generating an image]

Once Dracut is configured, a new initramfs can be generated by running:

`root `[`#`]`dracut`

** Important**\
Dracut writes the file to [/boot] by default, this must be mounted.

If the initramfs is being generated for a kernel other than the currently active one, **\--kver** must be used:

`root `[`#`]`dracut --kver 6.1.28-gentoo `

This can happen in a situation when the kernel version in the Gentoo Live CD differs from the emerged sys-kernel/gentoo-sources in the kernel compilation process.

** Tip**\
Possible kernel versions can be found by using **ls /lib/modules**.

Dracut has now generated an initramfs, but configuration is not complete. Command line parameters must be set, either by manually adding them to the kernel, or by configuring them into the bootloader.

** Tip**\
Most dracut configuration is described in **man dracut.cmdline**.

#### [Extracting the initramfs]

It\'s possible to use **dracut** to generate an *initramfs* image, then extract this to be built into the kernel.

`/usr/src/initramfs #``/usr/lib/dracut/skipcpio /boot/initramfs-6.1.28-gentoo-initramfs.img | zcat | cpio -ivd`

### [Embedding the initramfs]

An initramfs image can be embedded into the Linux kernel, or a path can be supplied to be packed and embedded.

** Note**\
If using a kernel which requires modules to boot, the *initramfs* must be recreated after the kernel is built once, extracted, then the kernel must be rebuilt to embed the latest *initramfs*. The rebuild should be very quick unless using **make clean**.

** Important**\
If using this method with **GRUB**, be sure to delete or move the generated *initramfs* image, so **grub-mkconfig** does not get confused.

#### [Embedding a directory]

With the *initramfs* unpacked in [/usr/src/initramfs], the kernel can be configured to embed it:

[KERNEL] **Embed the initramfs into the kernel**

    General Setup --->
    [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
        (/usr/src/initramfs) Initramfs source file(s)
    [*]   Support initial ramdisk/ramfs compressed using gzip

.config equivalent:

[CODE] **.config configuration for an embedded initramfs**

    CONFIG_INITRAMFS_SOURCE="/usr/src/initramfs"
    CONFIG_INITRAMFS_ROOT_UID=0
    CONFIG_INITRAMFS_ROOT_GID=0
    CONFIG_RD_GZIP=y
    CONFIG_INITRAMFS_COMPRESSION_GZIP=y

With this configuration, the kernel will automatically embed whatever exists under [/usr/src/initramfs] into the kernel when it is built, and attempt to use it on boot. This is especially useful when [Secure Booting](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").

** Important**\
If this directory is missing character devices, sometimes caused by extracting the image as a non-root user, it may fail to boot if repacked.

#### [Embedding an image]

If the path to a CPIO image is provided instead of a directory, it will be packed into the kernel.

** Important**\
The kernel will fail to boot if a compressed image is provided as **CONFIG_INITRAMFS_SOURCE**.

## [Gentoo installation]

If this procedure is being followed during a Gentoo install (in place of [Handbook:AMD64/Full/Installation#Designing_a_partition_scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation") through [Handbook:AMD64/Full/Installation#Mounting_the_root_partition](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Mounting_the_root_partition "Handbook:AMD64/Full/Installation")), the following steps can be used to mount the created partition, to continue with the install.

### [Mount the root partition]

The logical volume for the root file system can be mounted at this created location with:

`root `[`#`]`mount LABEL=rootfs /mnt/gentoo`

### [fstab configuration]

** Important**\
The correct *fstab* file must be edited, if this is being done before chrooting, ensure the correct path is being used. More information exists in [the filesystem portion of the install guide](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Filesystem_information "Handbook:AMD64/Full/Installation").

For consistent volume mounting, labels and UUIDs must be used.

Block devices and their associated partition IDs can be viewed with:

`root `[`#`]`lsblk -o name,uuid`

    NAME        UUID
    sda
    ├──sda1     BDF2-0139
    └──sda2     0e86bef-30f8-4e3b-ae35-3fa2c6ae705b
    nvme0n1
    └─nvme0n1p1 4bb45bd6-9ed9-44b3-b547-b411079f043b
      └─root    cb070f9e-da0e-4bc5-825c-b01bb2707704

With the partition UUIDs and labels identified, [/etc/fstab](https://wiki.gentoo.org/wiki/Fstab "Fstab") can be edited to add relevant mounts:

[FILE] **`/mnt/gentoo/etc/fstab`**

    # <fs>                                          <mountpoint>    <type>          <opts>          <dump/pass>
    UUID=BDF2-0139                                  /efi            vfat            noauto,noatime  0 1
    LABEL=boot                                      /boot           ext4            noauto,noatime  0 1
    LABEL=rootfs                                    /               btrfs           defaults        0 0

** Note**\
Because the subvolumes are created where they would be mounted, they do not need fstab entries.

### [Finalizing the Gentoo install]

** Important**\
The general install guide should apply. A few considerations must be made, the initial RAM filesystem must be built with support for decrypting the root partition, and the kernel commandline must be configured to pass parameters to the initramfs if required.

At this point, the Gentoo install can be continued normally: [Installing a stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Installing_a_stage_tarball "Handbook:AMD64/Full/Installation")

## [Additional information]

### [SSD tricks]

SSD [trim](https://en.wikipedia.org/wiki/Trim_(computing) "wikipedia:Trim (computing)") allows an operating system to inform a solid-state drive (SSD) which blocks of data are no longer considered in use and can be wiped internally. Because low-level operation of SSDs differs significantly from hard drives, the typical way in which operating systems handle operations like deletes and formats resulted in unanticipated progressive performance degradation of write operations on SSDs. Trimming enables the SSD to more efficiently handle garbage collection, which would otherwise slow future write operations to the involved blocks.

See [SSD LUKS](https://wiki.gentoo.org/wiki/SSD#LUKS "SSD") for enabling discard passthrough.

See [SSD LVM](https://wiki.gentoo.org/wiki/SSD#LVM "SSD") when using LVM.

** Warning**\
Using SSDs and also hybrid drives sacrifices some cryptographic security for speed-improvement and lower power consumption. See [FAQs](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/FrequentlyAskedQuestions) of cryptsetup for the details. Plan with drive\'s degradation and loss of space over time. With or without trim physical destruction of drives without secure-erase is necessary. There are no guarantees that overwriting really changes bits in the drive\'s memory chips. This is not a problem of cryptsetup, LUKS or the kernel but caused by the firmware/ hardware/ vendor- and model-specific algorithms.

When using SSDs and UEFI-boot the boot sequence might be too fast. When entering the correct passphrase, the kernel will complain about missing modules or no root device. Try to add `rootdelay=3` to `GRUB_CMDLINE_LINUX_DEFAULT` in [/etc/default/grub], or directly append it in edit mode of the GRUB menu when booting.

## [See also]

-   [Rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") --- Encrypting the root [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") can enhance privacy, and prevent unauthorized access.
-   [Dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") --- a disk encryption system using the kernels crypto API framework and device mapper subsystem.
-   [Encrypted bootable media with SecureBoot/GRUB/LUKS](https://wiki.gentoo.org/wiki/Encrypted_bootable_media_with_SecureBoot/GRUB/LUKS "Encrypted bootable media with SecureBoot/GRUB/LUKS") --- Encrypting bootable media can enhance privacy, and prevent unauthorized access.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.ctrl.blog/entry/esp-size-guide.html](https://www.ctrl.blog/entry/esp-size-guide.html)]]