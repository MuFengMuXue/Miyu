[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

This article is an example of using [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") for full disk encryption with [LVM](https://wiki.gentoo.org/wiki/LVM "LVM"). We start at empty disks on SSD. dm-crypt is an implementation of Linux Unified Key Setup (LUKS) disk encryption specification.

The point is to encrypt everything with strong cryptography. USB stick store big keyfile encrypted with short password.

## Contents

-   [[1] [disk partitioning]](#disk_partitioning)
-   [[2] [Steps]](#Steps)
-   [[3] [Full dracut.conf]](#Full_dracut.conf)
-   [[4] [Help scripts]](#Help_scripts)
-   [[5] [Suggestions]](#Suggestions)
-   [[6] [TODO]](#TODO)
-   [[7] [Problems]](#Problems)
-   [[8] [Links]](#Links)

## [disk partitioning]

Btrfs can be replaced to ext4 or any other file system.

    --------------------------------------------------------------------------------
    /dev/sdX
    |--> GRUB BIOS                       2   MB       no fs       GRUB loader itself
    |--> /boot                 boot      512 MB       fat32       GRUB and kernel
    |--> LUKS encrypted                  100%         encrypted   encrypted block device
         |-->  LVM             lvm       100%
               |--> /          root      40  GB       btrfs        root filesystem
               |--> /var       var       20  GB       btrfs        var files
               |--> /home      home      100%         btrfs        user files

## [Steps]

    - Lets create partitions. This partition will contain GRUB files, plain (unencrypted) kernel and kernel initrd:
     - parted /dev/sda
       - mkpart primary fat32 3 515
       - name 2 boot
       - set 2 BOOT on
       - mkpart primary 515 -1
       - name 3 lvm
       - set 3 lvm on
       - set 1 bios_grub on # for GPT table + BIOS Legacy
      - mkfs.vfat -F32 /dev/sdX2
      - modprobe dm-crypt
      - lets create gpg encrypted keyfile at USB stick partition
        - export GPG_TTY=$(tty)
        - gpg --quiet --decrypt /mnt/key/rootkey.gpg | cryptsetup --allow-discards --key-file - luksOpen /dev/sdX3 lvm
        - gpg --quiet --decrypt /mnt/key/rootkey.gpg | cryptsetup --batch-mode --key-file - luksFormat /dev/sdX3 lvm
    - Create LVM inside encrypted block - for SSD TRIM require special options
      - vgcreate vg0 /dev/mapper/lvm  # Create volume group vg0:
      - lvcreate -L 60G -n root vg0  # Create logical volume for /root filesystem
      - lvcreate -L 20G -n var vg0  # Create logical volume for /var filesystem
      - lvcreate -L 7G -n swap vg0  # Create logical volume for swap filesystem
      - lvcreate -l 100%FREE -n home vg0  # Create logical volume for /home filesystem:
      - cryptsetup luksHeaderBackup /dev/sdXn --header-backup-file /tmp/efiboot/luks-header.img  # backup
    - format
      - mkswap -L "swap" /dev/mapper/vg1-swap
      - mkfs.btrfs -L "root" /dev/mapper/vg1-root
      - mkfs.btrfs -L "var" /dev/mapper/vg1-var
      - mkfs.trfs -L "home" /dev/mapper/vg1-home
    - mount
      - mount -o compress=lzo,discard=async /dev/vg0/root/ /mnt/gentoo
      - mkdir /mnt/getnoo/var
      - mount -o compress=lzo,discard=async /dev/vg0/var/ /mnt/gentoo/var
    - tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner # v - verbose
    - mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf
    - mkdir --parents /mnt/gentoo/etc/portage/repos.conf
    - cp /mnt/gentoo/usr/share/portage/config/repos.conf /mnt/gentoo/etc/portage/repos.conf/gentoo.conf
    - cp --dereference /etc/resolv.conf /mnt/gentoo/etc/
    - nano -w /mnt/gentoo/etc/portage/make.conf
      - COMMON_FLAGS="-march=native -O2 -pipe"
      - MAKEOPTS="-j4"
    - chroot! See "Help scripts" below.
    - emerge-webrsync
    - emerge --sync --quiet
    - gcc -v -E -x c /dev/null -o /dev/null -march=native 2>&1 | grep /cc1 | grep mtune
    - replace -march=native
    - emerge --ask  app-portage/cpuid2cpuflags
    - $cpuid2cpuflags >> /etc/portage/make.conf
    - emerge --ask emacs sys-kernel/dracut sys-kernel/gentoo-sources sys-boot/grub sys-fs/lvm2 sys-fs/cryptsetup
      app-crypt/gnupg sys-fs/btrfs-progs
    - USE="-gtk -pango -libkms" emerge --ask sys-boot/plymouth
    - rc-update add lvm boot
    - fstab
    - sfdisk -d /dev/sda > /mnt/img/sda.partition.table.txt # backup partition table
    - findmnt --verify --verbose # verify fstab
    - configure and build Kernel
    - /etc/dracut.conf
      - # Equivalent to -a "module"
      - # located /usr/lib/dracut/modules.d/
      - add_dracutmodules+=" lvm btrfs crypt crypt-gpg dm "
      - filesystems+=" btrfs "
      - kernel_cmdline="rd.luks.key=/luks-key.gpg:UUID=xxxxxx-xxx-xx-xx" # shoud work
      - full: kernel_cmdline="
      - early_microcode="no
      - show_modules="yes"
      - rd.lvm.vg="vg0"
    - dracut --kver 5.15.26-gentoo --force --hostonly --fstab 2>drac_log.txt
    - /etc/dracut.conf: kernel_cmdline shoud be copied to /etc/default/grub:GRUB_CMDLINE_LINUX

## [Full dracut.conf]

[FILE] **`/etc/dracut.conf`**

    # Gentoo specific - from official documentation
    udevdir=/lib/udev
    ro_mnt=yes
    omit_drivers+=" i2o_scsi "

    # for rd.luks.key
    omit_dracutmodules+=" systemd systemd-initrd dracut-systemd i18n systemd-udevd "

    # dm crypt
    add_dracutmodules+=" lvm btrfs crypt-gpg "
    filesystems+=" btrfs "
    early_microcode="no"
    show_modules="yes"
    use_fstab="yes"
    hostonly="yes"
    # rd.luks.key:UUID - partition at USB stick
    # rd.luks.uuid - lvm partition with subpartition /root
    kernel_cmdline="rd.luks.key=/luks-key.gpg:UUID=xxxx-xxxx-xxxx rd.luks.uuid=luks-xxxx-xxxx-xxxx rd.luks rd.lvm rd.lvm.vg=vg0 rd.lvm.lv=vg0/root root=/dev/mapper/vg0-root rootfstype=btrfs rootflags=rw,relatime,compress=lzo,ssd,space_cache=v2,subvolid=5,subvol=/ rd.luks.allow-discards=xxxx-xxx-xxxx(sda3 uuid)"
    # rd.shell rd.debug
    kernel_image="/boot/vmlinuz-5.15.26-gentoo"

    add_drivers+=" i915 " # for X11 early KMS

## [Help scripts]

Decrypt lvm partition (replace \> with \|):

[FILE] **`/mnt/key/open`**

    export GPG_TTY=$(tty)
    gpg --quiet --decrypt /mnt/key/luks-key.gpg > cryptsetup --batch-mode --key-file - luksOpen /dev/sda3 lvm

Mount and chroot:

[FILE] **`/mnt/key/m`**

    mount -t btrfs -o compress=lzo /dev/mapper/vg0-root /mnt/gentoo
    mount --types proc /proc /mnt/gentoo/proc
    mount --rbind /sys /mnt/gentoo/sys
    mount --make-rslave /mnt/gentoo/sys
    mount --rbind /dev /mnt/gentoo/dev
    mount --make-rslave /mnt/gentoo/dev
    mount --rbind /run /mnt/gentoo/run
    mount --make-rslave /mnt/gentoo/run
    chroot /mnt/gentoo /bin/bash

After chroot mount: /var, /boot, /tmp, /home

[FILE] **`/mnt/key/m2`**

    source /etc/profile
    mount -t vfat /dev/sda2 /boot/
    mount -t tmpfs tmpfs /tmp
    mount -t btrfs -o compress=lzo /dev/mapper/vg0-var /var/
    mount -t btrfs -o compress=lzo /dev/mapper/vg0-home /home/
    export PS1="(chroot) $"

## [Suggestions]

-   Move /boot partiton to USB Stick
-   Replace lvm volume with btrfs subvolumes

## [TODO]

-   use \--type LUKS2 parameter for cryptsetup. LUKS1 used by default.

## [Problems]

-   Keyfile can be stolen from USB stick
-   LUKS partition is not headless - no plausible deniability.

## [Links]

1\. [Full Disk Encryption From Scratch Simplified](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch_Simplified "Full Disk Encryption From Scratch Simplified")

2\. [Dm-crypt_full_disk_encryption](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption "Dm-crypt full disk encryption")

3\. [Full_Encrypted_Btrfs/Native_System_Root_Guide](https://wiki.gentoo.org/wiki/Full_Encrypted_Btrfs/Native_System_Root_Guide "Full Encrypted Btrfs/Native System Root Guide")

4\. [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut")