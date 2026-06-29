[[]][Package information](https://packages.gentoo.org/packages/net-misc/dropbear)

If you have followed [Rootfs encryption](https://wiki.gentoo.org/wiki/Rootfs_encryption "Rootfs encryption") and would like to unlock the root device remotely you can using [Dropbear](https://wiki.gentoo.org/wiki/Dropbear "Dropbear").

This document assumes you have configured encryption using [Dracut](https://wiki.gentoo.org/wiki/Rootfs_encryption#Dracut "Rootfs encryption") with [Systemd](https://wiki.gentoo.org/wiki/Rootfs_encryption#Systemd "Rootfs encryption") and booting using [Grub](https://wiki.gentoo.org/wiki/Grub "Grub").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Configure dropbear]](#Configure_dropbear)
    -   [[1.3] [Dracut module]](#Dracut_module)
    -   [[1.4] [Grub]](#Grub)
-   [[2] [Usage]](#Usage)

## [Installation]

### [Emerge]

Install dropbear

`root `[`#`]`emerge --ask net-misc/dropbear`

### [Configure dropbear]

Generate the dropbear server host keys

`root `[`#`]`dropbear -R`

Edit [/etc/dropbear/authorized_keys] with the SSH public key(s) you will use to access the machine.

### [Dracut module]

Create the module directory

`root `[`#`]`mkdir /usr/lib/dracut/modules.d/50dropbear`

Create the script which starts dropbear replace 2222 with your port of choice.

[FILE] **`/usr/lib/dracut/modules.d/50dropbear/dropbear-init.sh`**

    #!/bin/sh
    echo "Starting Dropbear SSH server..."
    dropbear -E -s -j -k -p 2222 &

Create the script used to unlock the disks.

[FILE] **`/usr/lib/dracut/modules.d/50dropbear/unlock.sh`**

    #!/bin/sh
    for f in $(systemctl list-units | awk '/systemd.*activating/ ')
    do
        systemctl start "$f"
    done

Create the script which will configure the module.

[FILE] **`/usr/lib/dracut/modules.d/50dropbear/module-setup.sh`**

    #!/bin/sh

    check()

    depends()

    install()

Allow executing the scripts

`root `[`#`]`chmod u+x /usr/lib/dracut/modules.d/50dropbear/dropbear-init.sh /usr/lib/dracut/modules.d/50dropbear/unlock.sh /usr/lib/dracut/modules.d/50dropbear/module-setup.sh `

Updated the initramfs

`root `[`#`]`dracut --force`

### [Grub]

Edit [/etc/default/grub] and configure the network parameters, this assumes you\'ve already added rd.luks.uuid

[FILE] **`/etd/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="rd.luks.uuid=fbb4fc25-3fa7-4ff7-aeca-b867be758f80 rd.neednet=1 ip=single-dhcp

Update the grub config

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

## [Usage]

SSH into the machine

`user `[`$`]` ssh -p 2222 root@xxx.xxx.xxx.xxx`

Then unlock the drive

`root `[`#`]`unlock`

    -sh-5.2# unlock
    🔐 Please enter passphrase for disk DISK (luks-fbb4fc25-3fa7-4ff7-aeca-b867be758f80): (press TAB for no echo)

Dropbear will automatically close the connection once the passphrase is accepted.