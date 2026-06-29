This page contains [[changes](https://wiki.gentoo.org/index.php?title=Swap&oldid=1420954&diff=1431378#Swap_files)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Swap/fr "Swap/fr (0% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Swap/hu "Swap (99% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Swap/ja "スワップ (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Memory_paging "wikipedia:Memory paging")

[[]]This article has some todo items:\

-   remove swap files, btrfs swapfile note

*Not to be confused with [Zswap](https://wiki.gentoo.org/wiki/Zswap "Zswap").*

In the Linux/Unix world, the term **swap** is generally used as a synonym for [memory paging](https://en.wikipedia.org/wiki/Memory_paging "wikipedia:Memory paging"). Swap refers to both the act of moving memory pages between memory and a secondary storage.

Linux can use a combination of swap areas - multiple swap devices and/or swap files together. It is also possible to assign different priorities to swap areas.

However, swap space may not be necessary at all depending on the requirements for the system in question. For example, a laptop that [suspends to disk](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate") (hibernation) requires all pages in memory to be stored to disk, so swap is necessary in this case. Server systems equipped with large amount of memory running at a constant load might not require swap at all. For further details, see the dedicated [Knowledge Base](https://wiki.gentoo.org/wiki/Knowledge_Base:Is_swap_space_really_necessary "Knowledge Base:Is swap space really necessary") article.

The Gentoo Handbook recommends, as part of the installation process, a [helpful rule of thumb table](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks#What_about_swap_space.3F "Handbook:AMD64/Installation/Disks") if a user is unsure how much swap is needed. Swap can be created and activated at any time though if a mistake is made.

** Tip**\
Nowadays, having systems with plenty of memory, it may be sufficient to create a swap partition smaller than the available memory. When using hibernation, storing a compressed RAM image inside the swap partition, it\'s a good idea having a swap partition with the size of the installed memory.

## Contents

-   [[1] [Creation]](#Creation)
    -   [[1.1] [Swap Partition]](#Swap_Partition)
    -   [[1.2] [Swap file]](#Swap_file)
-   [[2] [Activation]](#Activation)
-   [[3] [Advanced Swapping]](#Advanced_Swapping)
    -   [[3.1] [Encrypted swap with hibernate option]](#Encrypted_swap_with_hibernate_option)
        -   [[3.1.1] [Using full disk encryption]](#Using_full_disk_encryption)
    -   [[3.2] [Encrypted swap file]](#Encrypted_swap_file)
        -   [[3.2.1] [Creation]](#Creation_2)
        -   [[3.2.2] [Activation (systemd)]](#Activation_.28systemd.29)
        -   [[3.2.3] [Activation (OpenRC)]](#Activation_.28OpenRC.29)
    -   [[3.3] [OpenRC configuration]](#OpenRC_configuration)
-   [[4] [Performance tuning]](#Performance_tuning)
    -   [[4.1] [Prioritization]](#Prioritization)
    -   [[4.2] [Swappiness]](#Swappiness)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Creation]

### [Swap Partition]

Presuming [/dev/sda2] is the partition available to be used for swap, first format the partition as swap.

`root `[`#`]`mkswap /dev/sda2`

### [Swap file]

In order to work around the more rigid constraints of disk partitions, an alternative is to use an on-disk file as swap. Files can be located *inside* disk partitions. This allows flexibility to resize or move the swap space as necessary to meet the demands of the system without having to [repartition](https://wiki.gentoo.org/wiki/Partition "Partition") a disk.

Begin by allocating a new file to be used for the backing store of the swapfile. The size of this file will be the size of the swap space. Standard utilities can be used for this purpose such as [fallocate] from [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]:

`root `[`#`]`fallocate -l 12GiB swapfile`

Then, restrict permissions on the file to root access only.

`root `[`#`]`chmod 600 swapfile`

Then initialize the swapfile:

`root `[`#`]`mkswap swapfile`

** Note**\
If the partition the swapfile is located on is using [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), [swapon] will fail unless the swap file is in its own subvolume and copy-on-write and compression are disabled for the swapfile^[\[1\]](#cite_note-1)^. Assuming a 4GB swap file, the steps would be as follows:

`root `[`#`]` btrfs subvolume create swap_vol `

`root `[`#`]` chattr +C swap_vol `

`root `[`#`]` fallocate -l 4G swap_vol/swapfile `

`root `[`#`]` chmod 600 swap_vol/swapfile `

`root `[`#`]` mkswap swap_vol/swapfile `

Alternatively for Btrfs versions \>=6.1, the swap file can be created in a single command^[\[2\]](#cite_note-2)^:

`root `[`#`]` btrfs subvolume create swap_vol `

`root `[`#`]` chattr +C swap_vol `

`root `[`#`]` btrfs filesystem mkswapfile --size 4G swap_vol/swapfile `

## [Activation]

Before swap can be used, it must be enabled with the [swapon] command. For swap partitions:

`root `[`#`]`swapon /dev/sdb`

or, in case of a swap file:

`root `[`#`]`swapon swapfile`

** Tip**\
It\'s also possible to review the system swaps with [swapon]:

`user `[`$`]`swapon --show`

NAME TYPE SIZE USED PRIO /swapfile file 12G 2.6G 10

While manually activating the swap with [swapon] is fine, there are several methods to automate this process.

Typically swap is added to fstab so that it can be activated along with other file systems during the init process. To do this append a line (adjusting as necessary) to [fstab]:

[FILE] **`/etc/fstab`**

    /dev/sda2 none swap sw 0 0
    /swapfile none swap sw 0 0

Alternatively, on systemd it\'s possible to setup a swap unit^[\[3\]](#cite_note-3)^:

[FILE] **`/etc/systemd/system/swapfile.swap`**

    [Unit]
    Description=Activate /swapfile

    [Swap]
    # Path to the swap file or device
    What=/swapfile
    # Optional: Set priority for the swap space
    Priority=10

    [Install]
    # This tells systemd to start this unit as part of the main swap target
    WantedBy=swap.target

** Tip**\
Swap units must be named after the devices or files they control. Example: the swap device [/dev/sda2] must be configured in a unit file [dev-sda2.swap].

Then activate the unit:

`root `[`#`]`systemctl enable swapfile.swap --now`

The final method for automatically enabling swap is via the Discoverable Partitions Specification^[\[4\]](#cite_note-4)^; by setting the GUID Partition Table (GPT) UUID to the correct value (`0657fd6d-a4ab-43c4-84e5-0933c84b4f4f` aka `SD_GPT_SWAP`. If using Discoverable Partitions, all swap partitions on the disk containing the root partition are automatically enabled. This functionality is init-dependent, but is known to be supported by systemd.

## [Advanced Swapping]

### [Encrypted swap with hibernate option]

Assuming the desired goal is a LUKS encrypted swap partition with the ability to still be able to perform [hibernate](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate") (a.k.a. suspend to disk), the encrypted swap partition needs a known LUKS-key (keyfile, password, etc.). Early in the boot process, the user will be asked to enter the password. The kernel decides whether to regularly boot the system, or to load a hibernated RAM image from swap if the system was hibernated in the previous power state.

The creation of a LUKS encrypted swap partition is not different from any other LUKS encrypted partition, described in [creating an encrypted storage platform](https://wiki.gentoo.org/wiki/Dm-crypt#Creating_an_encrypted_storage_platform "Dm-crypt"). Use [mkswap] instead of [mkfs.\*] to the LUKS encrypted partition to create SWAP. The UUID (i.e., `01b37ea8-74a5-4526-85c7-9fdf6dad34cb`), created when formatting as swap, is needed for the next step:

Tell the bootloader (GRUB) where to resume from if hibernated:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=01b37ea8-74a5-4526-85c7-9fdf6dad34cb"

In addition, (when using OpenRC with dracut, systemd is presumed to be now used for this section of the guide) dracut will need to be told the major and minor number of the associated LUKS device, so it can create an appropriate initrd:

`root `[`#`]`lsblk`

    ..
    └─sdb1                                          8:22   0    32G  0 part
     └─luks-cc166689-4246-41ae-86e8-84705b81ecc2  253:1    0    32G  0 crypt [SWAP]

`root `[`#`]`echo 253:1 > /sys/power/resume `

** Note**\
The default value is `0:0`. [echo] this in again to deactivate hibernation.

** Warning**\
Be careful not to confuse the LUKS UUID (`cc166689-4246-41ae-86e8-84705b81ecc2`) with the swap UUID (`01b37ea8-74a5-4526-85c7-9fdf6dad34cb`).

Finally, the initrd needs to be updated with these changes:

`root `[`#`]`dracut --force `

Do not forget the regular configuration of swap in [/etc/fstab] and restart the system afterwards.

[FILE] **`/etc/fstab`**

    # /dev/sdb1 (SWAP)
    UUID=01b37ea8-74a5-4526-85c7-9fdf6dad34cb               none            swap    sw      0 0

** Note**\
If a LUKS encrypted swap using [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") is already setup by including a configuration in [/etc/conf.d/dmcrypt], it will be obsolete, since this LUKS device will now be opened earlier with the help of the dracut generated initrd.

#### [Using full disk encryption]

When already using [full disk encryption](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption#Dracut "Dm-crypt full disk encryption") with LUKS, a decryption password prompt will appear twice when booting; once to enter the LUKS-key for the system\'s root partition (as before) and once to decrypt the swap partition. It is possible to just decrypt the root partition and then use a LUKS keyfile, stored on the just now decrypted root partition, to decrypt the swap partition automatically. Details and an easy example of how to do this within [/etc/default/grub], can be found on [kernel.org](https://mirrors.edge.kernel.org/pub/linux/utils/boot/dracut/dracut.html#_crypto_luks_key_on_removable_device_support).

### [Encrypted swap file]

It is best practice to encrypt swap files.

** Note**\
This section on encrypted swap file is very useful for hibernate support as it uses the same key for its encrypted swap partition across reboot. For maximum security, use rekey-at-reboot; LVM must be used for encrypted swap partition, and [/dev/mapper/\<vg_group\>\_swap-unencrypted] (not the more direct [/dev/dm-9]) be used in [/etc/fstab]. See [How to create a randomly keyed, encrypted swap partition, referring to it \"by-uuid\".](https://serverfault.com/questions/312123/how-to-create-a-randomly-keyed-encrypted-swap-partition-referring-to-it-by-uu/1031460#1031460)

#### [Creation]

To create a 2 GiB encrypted swap file in the [/opt] directory, run:

`root `[`#`]`cd /opt `

`root `[`#`]`fallocate -l 2GiB swapfile `

`root `[`#`]`chmod 600 swapfile `

`root `[`#`]`cryptsetup --type plain --key-file /dev/urandom open swapfile cryptswap `

`root `[`#`]`mkswap /dev/mapper/cryptswap `

`root `[`#`]`swapon /dev/mapper/cryptswap `

`root `[`#`]`swapon --show`

[FILE] **`/etc/fstab`**

    /dev/mapper/cryptswap none swap sw 0 0

#### [][Activation (systemd)]

** Note**\
Make sure systemd is compiled with cryptsetup support, otherwise [/etc/crypttab] will not be read.

[FILE] **`/etc/crypttab`**

    cryptswap /opt/swapfile /dev/urandom swap

#### [][Activation (OpenRC)]

** Warning**\
The OpenRC dm-crypt daemon uses the `aes-cbc-plain` cipher by default, which is vulnerable ^[\[5\]](#cite_note-5)^ . Therefore, the `options` must be specified to use the `aes-cbc-essiv` cipher instead.

Use this command to check which cipher is being used:

`root `[`#`]`dmsetup table cryptswap`

[FILE] **`/etc/conf.d/dmcrypt`**

    swap=cryptswap
    source=/opt/swapfile
    options='--type plain --key-file /dev/urandom'

Enable the *dmcrypt* service:

`root `[`#`]`rc-update add dmcrypt boot`

If the dm-crypt daemon fails to create the swap at boot, for example, with the following error:

    mkswap: unable to erase bootbits sectors

the swap can be created manually. Disable the dm-crypt daemon and revert the changes made to [/etc/fstab] and [/etc/conf.d/dmcrypt].

Create the shell script `01-swap.start` in [/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d"):

[FILE] **`/etc/local.d/01-swap.start`**

    cryptsetup \
        open \
        --batch-mode \
        --type plain \
        --cipher <same_cipher_as_underlying_luks_device> \
        --key-file /dev/urandom \
        --key-size <same_size_as_underlying_luks_device> \
        --sector-size <same_size_as_underlying_luks_device> \
        /opt/swapfile \
        cryptswap

    mkswap /dev/mapper/cryptswap
    swapon /dev/mapper/cryptswap

The [cipher], [key size] and [sector size] of the underlying LUKS device can be displayed by executing the following command:

`root `[`#`]`cryptsetup status /dev/mapper/<decrypted_partition>`

Next, create `01-swap.stop`:

[FILE] **`/etc/local.d/01-swap.stop`**

    swapoff /dev/mapper/cryptswap
    cryptsetup close cryptswap

Finally, make the scripts executable:

`root `[`#`]`chmod +x /etc/local.d/01-swap.start`

`root `[`#`]`chmod +x /etc/local.d/01-swap.stop`

The swap will be created after a reboot.

### [OpenRC configuration]

When using swap files which are not on the root filesystem, the service ordering in OpenRC should be changed via [/etc/conf.d/swap]:

[FILE] **`/etc/conf.d/swap`**

    # If you are only using local swap partitions, you should not change
    # this file. Otherwise, you need to uncomment the below rc_before line
    # followed by the appropriate rc_need line.
    rc_before="!localmount"
    #
    # If you are using swap files stored on local file systems, uncomment
    # this line.
    rc_need="localmount"
    #
    # If you are using swap files stored on network file systems or swap
    # partitions stored on network block devices such as iSCSI, uncomment
    # this line.
    #rc_need="netmount"

## [Performance tuning]

### [Prioritization]

It is possible to prioritize different swap areas by assigning priority (an integer from 0 to 32767). Higher-priority swap areas are used first. Lower-priority areas are used after exhausting the higher ones. Areas having the same priority are used in a round-robin fashion^[\[6\]](#cite_note-6)^.

The priority can be used for systems using a combination of fast ([ZRAM](https://wiki.gentoo.org/wiki/Zram "Zram") or [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe")-based devices) and slow swap areas ([HDD](https://wiki.gentoo.org/wiki/HDD "HDD")-based devices) to prioritize the former before the latter ones.

For example, prioritizing a fast swap device [/dev/nvme0n1] before a regular swap file [/swapfile] using [/etc/fstab]:

[FILE] **`/etc/fstab`Swap prioritization example**

    /dev/nvme0n1      none        swap        sw,pri=16383        0 0
    /swapfile         none        swap        sw,pri=1            0 0

### [Swappiness]

Kernel allows tuning of the swap usage via [sysctl](https://wiki.gentoo.org/wiki/Procfs#sysctl "Procfs") parameters allowing to adapt the swapping for various workloads.

The `vm.swappiness` parameter controls the ratio between kernel willingness to reclaim file-backed (\"memory cached\" parts files) and anonymous memory pages (application heap and stack) back to their respective backing storage. The value range on recent kernels is 0-200, while the default is 60^[\[7\]](#cite_note-7)^. Values lower than the default represent a preference of keeping the application-related anonymous memory pages in memory at the expense of file-backed pages and vice versa.

The current value can be displayed by:

`user `[`$`]`sysctl vm.swappiness`

    vm.swappiness = 60

The desired swappiness value can be persistently set via:

[FILE] **`/etc/sysctl.d/90-swappiness.conf`Reduced system swappiness**

    vm.swappiness=20

## [See also]

-   [Filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") --- a means to organize data to be retained after a program terminates.
-   [Zram](https://wiki.gentoo.org/wiki/Zram "Zram") --- a [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") feature and set of userspace tools for creating compressible RAM-based block devices.
-   [Zswap](https://wiki.gentoo.org/wiki/Zswap "Zswap") --- a lightweight compressed cache for swap pages.

## [External resources]

-   [Upstream kernel.org documentation on swap suspend](https://www.kernel.org/doc/html/latest/power/swsusp.html#swap-suspend)

## [References]

1.  [[[↑](#cite_ref-1)] [[Swapfile --- BTRFS documentation](https://btrfs.readthedocs.io/en/latest/Swapfile.html)]]
2.  [[[↑](#cite_ref-2)] [[Swapfile --- BTRFS documentation, version 6.1 update](https://btrfs.readthedocs.io/en/latest/Swapfile.html#:~:text=Since%20version%206%2E1%20it%E2%80%99s%20possible%20to%20create%20the%20swapfile%20in%20a%20single%20command%20%28except%20the%20activation%29%3A)]]
3.  [[[↑](#cite_ref-3)] [[Systemd Documentation - systemd.swap](https://www.freedesktop.org/software/systemd/man/latest/systemd.swap.html).]]
4.  [[[↑](#cite_ref-4)] [[Discoverable Partitions Specification](https://uapi-group.org/specifications/specs/discoverable_partitions_specification/).]]
5.  [[[↑](#cite_ref-5)] [[https://gitlab.com/cryptsetup/cryptsetup/-/blob/main/FAQ.md](https://gitlab.com/cryptsetup/cryptsetup/-/blob/main/FAQ.md)]]
6.  [[[↑](#cite_ref-6)] [[swapon(2) - Linux man page](https://linux.die.net/man/2/swapon), die.net. Retrieved on: October 23, 2022]]
7.  [[[↑](#cite_ref-7)] [[Documentation for /proc/sys/vm/ --- The Linux Kernel documentation](https://docs.kernel.org/admin-guide/sysctl/vm.html), kernel.org. Retrieved on October 23, 2022]]