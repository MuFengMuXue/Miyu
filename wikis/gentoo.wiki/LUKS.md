This page contains [[changes](https://wiki.gentoo.org/index.php?title=Dm-crypt&oldid=1400271&diff=1439643)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Dm-crypt/de "Dm-crypt (33% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Dm-crypt/es "Dm-crypt (67% translated)")
-   [français](https://wiki.gentoo.org/wiki/Dm-crypt/fr "Dm-crypt (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Dm-crypt/hu "dm-crypt (100% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Dm-crypt/pt-br "Dm-crypt (56% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Dm-crypt/ru "Dm-crypt (86% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Dm-crypt/zh-cn "Dm-crypt (81% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Dm-crypt/ja "dm-crypt (97% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Dm-crypt/ko "Dm-crypt/ko (44% translated)")

**Resources**

[[]][Home](https://gitlab.com/cryptsetup/cryptsetup)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dm-crypt "wikipedia:Dm-crypt")

**dm-crypt** is a disk encryption system using the kernels crypto API framework and device mapper subsystem. With dm-crypt, administrators can encrypt entire disks, logical volumes, partitions, but also single files.

The dm-crypt subsystem supports the [Linux Unified Key Setup (LUKS)](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup "wikipedia:Linux Unified Key Setup") structure, which allows for multiple keys to access the encrypted data, as well as manipulate the keys (such as changing the keys, adding additional passphrases, etc.) Although dm-crypt supports non-LUKS setups as well, this article will focus on the LUKS functionality mostly due to its flexibility, manageability as well as broad support in the community.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Kernel Configuration]](#Kernel_Configuration)
    -   [[1.2] [Cryptsetup installation]](#Cryptsetup_installation)
-   [[2] [Encrypted storage]](#Encrypted_storage)
    -   [[2.1] [Benchmark]](#Benchmark)
    -   [[2.2] [Keyfile or passphrase]](#Keyfile_or_passphrase)
    -   [[2.3] [Creating an encrypted storage platform]](#Creating_an_encrypted_storage_platform)
        -   [[2.3.1] [Full disk encryption booting]](#Full_disk_encryption_booting)
    -   [[2.4] [Opening the encrypted storage]](#Opening_the_encrypted_storage)
    -   [[2.5] [Closing the encrypted storage]](#Closing_the_encrypted_storage)
-   [[3] [Manipulating LUKS keys]](#Manipulating_LUKS_keys)
    -   [[3.1] [Listing the slots]](#Listing_the_slots)
    -   [[3.2] [Adding a keyfile or passphrase]](#Adding_a_keyfile_or_passphrase)
    -   [[3.3] [Removing a keyfile or passphrase]](#Removing_a_keyfile_or_passphrase)
    -   [[3.4] [Emptying a slot]](#Emptying_a_slot)
-   [[4] [Automate mounting encrypted file systems]](#Automate_mounting_encrypted_file_systems)
    -   [[4.1] [Configuring dm-crypt]](#Configuring_dm-crypt)
    -   [[4.2] [Configuring fstab]](#Configuring_fstab)
    -   [[4.3] [Add initscript to bootlevel]](#Add_initscript_to_bootlevel)
    -   [[4.4] [Make decrypted device nodes visible]](#Make_decrypted_device_nodes_visible)
-   [[5] [Mounting TrueCrypt/tcplay/VeraCrypt volumes]](#Mounting_TrueCrypt.2Ftcplay.2FVeraCrypt_volumes)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Configuration]

There are two prerequisites before one can start using dm-crypt:

1.  Configuration of the Linux kernel
2.  Installation of the [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] package

### [Kernel Configuration]

To use dm-crypt there are a number of configuration entries that are necessary.

First of all, support for the *device mapper* infrastructure as well as the *crypt target* must be included. The *dm_crypt* module is loaded automatically, no configuration is needed in addition to those described in this page.

[KERNEL] **Enabling device mapper and crypt target**

    [*] Enable loadable module support Search for <code>CONFIG_MODULES</code> to find this item. --->
    Device Drivers --->
      [*] Multiple devices driver support (RAID and LVM) Search for <code>CONFIG_MD</code> to find this item. --->
        <*> Device mapper support Search for <code>CONFIG_BLK_DEV_DM</code> to find this item.
        <*> Crypt target support Search for <code>CONFIG_DM_CRYPT</code> to find this item.

Next, the Linux kernel needs to support the set of cryptographic APIs that the administrator wants to use for encryption. These can be found under the *Cryptographic API* section:

[KERNEL] **Enabling cryptographic API functions**

    [*] Cryptographic API Search for <code>CONFIG_CRYPTO</code> to find this item. --->
      Block ciphers --->
        <*> AES (Advanced Encryption Standard) Search for <code>CONFIG_CRYPTO_AES</code> to find this item.
      Length-preserving ciphers and modes --->
        <*> XTS (XOR Encrypt XOR with ciphertext stealing) Search for <code>CONFIG_CRYPTO_XTS</code> to find this item.
      Hashes, digests, and MACS --->
        <*> SHA-224 and SHA-256 Search for <code>CONFIG_CRYPTO_SHA256</code> to find this item.

\
If the root file system will be encrypted as well, then an initial ram file system needs to be created in which the root filesystem is decrypted before it is mounted. Thus this requires initramfs support as well:

[KERNEL] **Enabling initramfs support**

    General setup  --->
      [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support Search for <code>CONFIG_BLK_DEV_INITRD</code> to find this item.

If using the *tcrypt* encryption option (TrueCrypt/tcplay/VeraCrypt compatibility mode), then the following items will also need to be added to the kernel. Otherwise, cryptsetup will return the following errors: \"*device-mapper: reload ioctl failed: Invalid argument*\" and \"*Kernel doesn\'t support TCRYPT compatible mapping*\".

[KERNEL] **Enabling tcrypt (TrueCrypt/tcplay/VeraCrypt compatibility mode) support**

    Device Drivers --->
      [*] Block Devices Search for <code>CONFIG_BLK_DEV</code> to find this item. --->
        <*> Loopback device support Search for <code>CONFIG_BLK_DEV_LOOP</code> to find this item.
    File systems --->
      <*> FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.
    [*] Cryptographic API Search for <code>CONFIG_CRYPTO</code> to find this item. --->
      Hashes, digests, and MACs --->
        <*> RIPEMD-160 Search for <code>CONFIG_CRYPTO_RMD160</code> to find this item.
        <*> SHA-384 and SHA-512 Search for <code>CONFIG_CRYPTO_SHA512</code> to find this item.
        <*> Whirlpool Search for <code>CONFIG_CRYPTO_WP512</code> to find this item.
      Length-preserving ciphers and modes --->
        <*> LRW (Liskov Rivest Wagner) Search for <code>CONFIG_CRYPTO_LRW</code> to find this item.
      Block ciphers --->
        <*> Serpent Search for <code>CONFIG_CRYPTO_SERPENT</code> to find this item.
        <*> Twofish Search for <code>CONFIG_CRYPTO_TWOFISH</code> to find this item.

### [Cryptsetup installation]

The [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] package provides the [cryptsetup] command, which is used to open or close the encrypted storage as well as manage the passphrases or keys associated with it.

`root `[`#`]`emerge --ask sys-fs/cryptsetup`

## [Encrypted storage]

### [Benchmark]

[cryptsetup] provides a benchmarking tool which will help to decide which setup to choose. The output depends on kernel settings as well as USE flags and destination (HDD, SSD etc.).

`root `[`#`]`cryptsetup benchmark`

    # Tests are approximate using memory only (no storage IO).
    PBKDF2-sha1      3622024 iterations per second for 256-bit key
    PBKDF2-sha256    7410431 iterations per second for 256-bit key
    PBKDF2-sha512    3216490 iterations per second for 256-bit key
    PBKDF2-ripemd160 1157368 iterations per second for 256-bit key
    PBKDF2-whirlpool 1069975 iterations per second for 256-bit key
    argon2i      14 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    argon2id     15 iterations, 1048576 memory, 4 parallel threads (CPUs) for 256-bit key (requested 2000 ms time)
    #     Algorithm |       Key |      Encryption |      Decryption
            aes-cbc        128b      1520.5 MiB/s      4400.1 MiB/s
        serpent-cbc        128b       159.6 MiB/s      1061.9 MiB/s
        twofish-cbc        128b       310.8 MiB/s       662.1 MiB/s
            aes-cbc        256b      1175.8 MiB/s      4025.0 MiB/s
        serpent-cbc        256b       160.0 MiB/s      1054.8 MiB/s
        twofish-cbc        256b       312.6 MiB/s       655.5 MiB/s
            aes-xts        256b      4081.0 MiB/s      4073.5 MiB/s
        serpent-xts        256b       953.7 MiB/s       946.3 MiB/s
        twofish-xts        256b       597.5 MiB/s       616.8 MiB/s
            aes-xts        512b      3733.8 MiB/s      3743.3 MiB/s
        serpent-xts        512b       970.9 MiB/s       964.5 MiB/s
        twofish-xts        512b       598.1 MiB/s       611.3 MiB/s

### [Keyfile or passphrase]

In order to start with encrypted storage, the administrator will need to decide which method to use for the encryption key. With [cryptsetup] the choice is either a passphrase or a keyfile. In case of a keyfile, this can be any file, but it is recommended to use a file with random data which is properly protected (considering that access to this keyfile will mean access to the encrypted data).

To create a keyfile, one can use the [dd] command:

`root `[`#`]`dd if=/dev/urandom of=/etc/keys/enc.key bs=1 count=4096`

In the next sections, we will show every command for both situations - passphrase and keyfile. Of course, only one method is necessary.

### [Creating an encrypted storage platform]

In order to create an encrypted storage platform (which can be a disk, partition, file, \...) use the [cryptsetup] command with the `luksFormat` action.

For instance, to have [/dev/vdb2] as the storage medium for the encrypted data:

`root `[`#`]`cryptsetup -c aes-xts-plain64 -s 512 -y luksFormat /dev/vdb2`

    This will overwrite data on /dev/vdb2 irrevocably.

    Are you sure? (Type uppercase yes): YES
    Enter LUKS passphrase: ...
    Verify passphrase: ...

To use a keyfile instead of a passphrase:

`root `[`#`]`cryptsetup -c aes-xts-plain64 -s 512 -y luksFormat /dev/vdb2 /etc/keys/enc.key`

    This will overwrite data on /dev/vdb2 irrevocably.

    Are you sure? (Type uppercase yes): YES

The `-c aes-xts-plain64` tells [cryptsetup] the cipher used to encrypt the disk (`cat /proc/crypto` will show you all possibilities). `-s 512` tells [cryptsetup] which keylength to use for the real encryption key (unlike the passphrase or keyfile, which are used to access this real encryption key). Finally `-y` forces you to type your password twice.

** Note**\
[XTS](https://en.wikipedia.org/wiki/Disk_encryption_theory#XTS) splits the key into two halves, only one being used for the actual encryption. That means \"aes-xts\" with a 512-bit key actually uses 256 bits for the AES part.

** Important**\
[If] the LUKS header gets damaged, your encrypted data will be lost forever, even if you have a backup of the GPG key and passphrase. Therefore, you may wish to consider backing up this header to a separate device, and storing it securely. See the [LUKS FAQ](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions#6-backup-and-data-recovery) for more details on how to do this.

`root `[`#`]`cryptsetup luksHeaderBackup /dev/sdXn --header-backup-file /tmp/efiboot/luks-header.img`

Be aware, that if you do keep a LUKS header backup in this fashion and subsequently revoke any of the keyslots, the old keys will *still* be usable to unlock the LUKS partition for those with an access to that header backup file.

#### [Full disk encryption booting]

To boot from a fully encrypted device (including encrypted /boot) using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), encrypt using luks1, since luks2 isn\'t fully supported yet. Example command:

`root `[`#`]`cryptsetup -c aes-xts-plain64 -s 512 -y luksFormat --type luks1 /dev/vdb2`

### [Opening the encrypted storage]

In order to open up the encrypted storage (i.e. make the real data accessible through transparent decryption), use the `luksOpen` action.

`root `[`#`]`cryptsetup luksOpen /dev/vdb2 myname`

    Enter passphrase for /dev/vdb2: ...

If a keyfile is used, then the command would look like so:

`root `[`#`]`cryptsetup luksOpen -d /etc/keys/enc.key /dev/vdb2 myname`

When the command finishes successfully, then a new device file called [/dev/mapper/myname] will be made available.

If this is the first time this encrypted device is used, it needs to be formatted. The following example uses the [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") file system but of course any other file system will do:

`root `[`#`]`mkfs.btrfs /dev/mapper/myname`

Once the file system is formatted, or the formatting was already done in the past, then the device file can be mounted on the system:

`root `[`#`]`mount /dev/mapper/myname /home`

** Note**\
See [SSD LUKS](https://wiki.gentoo.org/wiki/SSD#LUKS "SSD") for enabling discard on SSDs.

### [Closing the encrypted storage]

In order to close the encrypted storage (i.e. ensure that the real data is no longer accessible through transparent decryption), use the `luksClose` action:

`root `[`#`]`cryptsetup luksClose myname`

Of course, make sure that the device is no longer in use.

## [Manipulating LUKS keys]

LUKS keys are used to access the real encryption key. They are stored in slots in the header of the (encrypted) partition, disk or file.

### [Listing the slots]

With the `luksDump` action, information about the encrypted partition, disk or file can be shown. This includes the slots:

`root `[`#`]`cryptsetup luksDump /dev/vdb2`

    LUKS header information for /dev/vdb2

    Version:        1
    Cipher name:    aes
    Cipher mode:    xts-plain64
    Hash spec:      sha1
    Payload offset: 4096
    MK bits:        512
    MK digest:      34 3b ec ac 10 af 19 e7 e2 d4 c8 90 eb a8 da 3c e4 4f 2e ce
    MK salt:        ff 7c 7f 53 db 53 48 02 a4 32 dc e0 22 fc a3 51
                    06 ba b3 48 b3 28 13 a8 7a 68 43 d6 46 79 14 fe
    MK iterations:  59375
    UUID:           2921a7c9-7ccb-4300-92f4-38160804e08c

    Key Slot 0: ENABLED
            Iterations:             241053
            Salt:                   90 0f 0f db cf 66 ea a9 6c 7c 0c 0d b0 28 05 2f
                                    8a 5c 14 54 98 62 1a 29 f3 08 25 0c ec c2 b1 68
            Key material offset:    8
            AF stripes:             4000
    Key Slot 1: ENABLED
            Iterations:             273211
            Salt:                   01 4c 26 ed ff 18 75 31 b9 89 5d a6 e0 b5 f4 14
                                    48 d0 23 47 a9 85 78 fb 76 c4 a9 d0 cd 63 fb d7
            Key material offset:    512
            AF stripes:             4000
    Key Slot 2: DISABLED
    Key Slot 3: DISABLED
    Key Slot 4: DISABLED
    Key Slot 5: DISABLED
    Key Slot 6: DISABLED
    Key Slot 7: DISABLED

In the above example, two slots are used. Note that `luksDump` does not give away anything sensitive - it is merely displaying the LUKS header content. No decryption key has to be provided in order to call `luksDump`.

### [Adding a keyfile or passphrase]

In order to add an additional keyfile or passphrase to access the encrypted storage, use the `luksAddKey` action:

`root `[`#`]`cryptsetup luksAddKey /dev/vdb2`

    Enter any passphrase: (Enter a valid, previously used passphrase to unlock the key)
    Enter new passphrase for key slot: ...
    Verify passphrase: ...

To use a keyfile to unlock the key (but still add in a passphrase):

`root `[`#`]`cryptsetup luksAddKey -d /etc/keys/enc.key /dev/vdb2`

    Enter new passphrase for key slot: ...
    Verify passphrase: ...

If a keyfile is to be added (say [/etc/keys/backup.key]):

`root `[`#`]`cryptsetup luksAddKey /dev/vdb2 /etc/keys/backup.key`

Or, to use the first keyfile to unlock the main key:

`root `[`#`]`cryptsetup luksAddKey -d /etc/keys/enc.key /dev/vdb2 /etc/keys/backup.key`

### [Removing a keyfile or passphrase]

With the `luksRemoveKey` action, a keyfile or passphrase can be removed (so they can no longer be used to decrypt the storage):

`root `[`#`]`cryptsetup luksRemoveKey /dev/vdb2`

    Enter LUKS passphrase to be deleted: ...

Or to remove a keyfile:

`root `[`#`]`cryptsetup luksRemoveKey -d /etc/keys/backup.key /dev/vdb2`

Make sure that at least one method for accessing the data is still available. Once a passphrase or keyfile is removed for use, this cannot be recovered again.

### [Emptying a slot]

Suppose the passphrase or keyfile is no longer known, then the slot can be freed. Of course, this does require prior knowledge of which slot that the passphrase or keyfile was stored in.

For instance, to empty out slot 2 (which is the third slot as slots are numbered starting from 0):

`root `[`#`]`cryptsetup luksKillSlot /dev/vdb2 2`

This command will ask for a valid passphrase before continuing. Or one can pass on the keyfile to use:

`root `[`#`]`cryptsetup luksKillSlot -d /etc/keys/enc.key /dev/vdb2 2`

## [Automate mounting encrypted file systems]

Until now, the article focused on manual setup and mounting/unmounting of encrypted file systems. An init service [dmcrypt] exists which automates the decrypting and mounting of encrypted file systems.

### [Configuring dm-crypt]

Edit the [/etc/conf.d/dmcrypt] file and add in entries for each file system. The supported entries are well documented in the file, the below example is just that - an example:

[FILE] **`/etc/conf.d/dmcrypt`Automatically enabling two encrypted file systems**

    # Definition for /dev/mapper/home (for /home)
    target=home
    source=UUID="abcdef12-321a-a324-a88c-cac412befd98"
    key=/etc/keys/home.key
    # If trim is desired, it can be enabled as below.
    # Keep in mind that trim is not enabled by default for a security reason.
    # This configuration is optional, otherwise default options apply.
    options="--allow-discards"

    # Definition for /dev/mapper/local (for /usr/local)
    target=local
    source=UUID="fedcba34-4823-b423-a94c-cadbefda2943"
    key=/etc/keys/local.key

    # Using an encrypted partition as key source.
    target=other
    source=UUID="ff24303e-49e1-4d13-b8ad-fc6b7e1d8174"
    key=/keys/other.key                                # Relative to the root of the encrypted partition.
    remdev=/dev/mapper/home                            # The recently decrypted partition.

    # An empty line is important at the end of the file

If using passphrase instead of a keyfile, you\'ll be prompted for it on boot (given a simple target and source configuration).

Summary of available entries:

  ------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Entry         Description
  **target**    Name of the mapping, will be created at [/dev/mapper/xxx]
  **source**    Encrypted device, i.e: [UUID=xxx] [LABEL=xxx]
  **key**       Key file\'s path used to decrypt [source]
  **remdev**    If the key file is located in a removable device, that device identifier. i.e: [UUID=xxx] [LABEL=xxx]
  **options**   Extra options used internally in [cryptsetup open]. Common options: [\--allow-discards] [\--perf-no_read_workqueue] [\--perf-no_write_workqueue]. Check all available options with [cryptsetup \--help]
  ------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Configuring fstab]

The next step is to configure [/etc/fstab] to automatically mount the (decrypted) file systems when they become available. It is recommended to first obtain the UUID of the decrypted (mounted) file system:

`root `[`#`]`blkid /dev/mapper/home`

    /dev/mapper/home: UUID="4321421a-4321-a6c9-de52-ba6421efab76" TYPE="ext4"

Then, update the [/etc/fstab] file accordingly:

[FILE] **`/etc/fstab`Automounting the decrypted file systems**

    UUID="4321421a-4321-a6c9-de52-ba6421efab76"   /home        ext4   defaults   0   0
    UUID="bdef2432-3bd1-4ab4-523d-badcf234a342"   /usr/local   ext4   defaults   0   0

### [Add initscript to bootlevel]

Don\'t forget to have the [dmcrypt] init service launched at boot:

`root `[`#`]`rc-update add dmcrypt boot`

\

### [Make decrypted device nodes visible]

If you have decrypted/unlocked a device before the services were started for example your root disk in an with an initramfs then it\'s possible that the mapped device is not visible. In this case you can run the following to recreate it.

`root `[`#`]`dmsetup mknodes`

## [][Mounting TrueCrypt/tcplay/VeraCrypt volumes]

`root `[`#`]`cryptsetup --type tcrypt open `*`container-to-mount`*` `*`container-name`*

Replace *container-to-mount* with the device file under [/dev] or the path to the file you wish to open. Upon successful opening, the plaintext device will appear as [/dev/mapper/container-name], which you can `mount` like any normal device.

If you are using key files, supply them using the `--key-file` option, to open a hidden volume, supply the `--tcrypt-hidden` option and for a partition or whole drive that is encrypted in system mode use the `--tcrypt-system` option.

When done, `unmount` the volume, and close the container using the following command:

`root `[`#`]`cryptsetup close `*`container-name`*

## [See also]

-   [rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") --- Encrypting the root [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") can enhance privacy, and prevent unauthorized access.
-   [Full Disk Encryption From Scratch](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch "Full Disk Encryption From Scratch") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.
-   [User:Sakaki/Sakaki\'s EFI Install Guide/Preparing the LUKS-LVM Filesystem and Boot USB Key](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Preparing_the_LUKS-LVM_Filesystem_and_Boot_USB_Key "User:Sakaki/Sakaki's EFI Install Guide/Preparing the LUKS-LVM Filesystem and Boot USB Key")

## [External resources]

-   The [cryptsetup FAQ](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions) hosted on GitLab covers a wide range of frequently asked questions.