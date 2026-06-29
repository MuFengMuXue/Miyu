# Diskless system

From Wikipedia:Diskless node:

:A diskless node (or diskless workstation) is a workstation or personal computer without disk drives, which employs network booting to load its operating system from a server.

## Server configuration
First of all, we must install the following components:
* A DHCP server to assign IP addresses to our diskless nodes.
* A TFTP server to transfer the boot image (a requirement of all PXE option roms).
* A form of network storage (NFS, Samba or NBD) to export the Arch installation to the diskless node.

## DHCP
Install ISC  and configure it:

{{hc|/etc/dhcpd.conf|2=
allow booting;
allow bootp;

authoritative;

option domain-name-servers 10.0.0.1;

option architecture code 93 = unsigned integer 16;

group {
    next-server 10.0.0.1;

    if option architecture = 00:07 {
        filename "/grub/x86_64-efi/core.efi";
    } else {
        filename "/grub/i386-pc/core.0";
    }

    subnet 10.0.0.0 netmask 255.255.255.0 {
        option routers 10.0.0.1;
        range 10.0.0.128 10.0.0.254;
    }
}
}}

RFC:4578 defines the "Client System Architecture Type" dhcp option. In the above configuration, if the PXE client requests an x86_64-efi binary (type 0x7), we appropriately give them one, otherwise falling back to the legacy binary. This allows both UEFI and legacy BIOS clients to boot simultaneously on the same network segment.

Start ISC DHCP systemd service.

## TFTP
The TFTP server will be used to transfer the boot loader, kernel, and initramfs to the client.

Set the TFTP root to . See TFTP for installation and configuration.

## Network storage
The primary difference between using NFS and NBD is while with both you can in fact have multiple clients using the same installation, with NBD (by the nature of manipulating a filesystem directly) you will need to use the  mode to do so, which ends up discarding all writes on client disconnect. In some situations however, this might be highly desirable.

## NFS
Install  on the server.

You will need to add the root of your Arch installation to your NFS exports:

Next, start NFS services:  .

## NBD
Install  and configure it.

Start .

## SKUF
You can boot Arch Linux using the SKUF Network Boot System project, where the root of the file system will be a sparse file located on Samba server.

To get started, install  and create a configuration file:

Start  systemd service

Then, create a  group and users who will be members of it and through whom  mounting on the client machine will happen.
 # groupadd skuf
 # useradd test -g skuf
 # smbpasswd -a test

## Client installation
Next we will create a full Arch Linux installation in a subdirectory on the server. During boot, the diskless client will get an IP address from the DHCP server, then boot from the host using PXE and mount this installation as its root.

## Directory setup
Create a sparse file of at least 2 gibibytes, and create a btrfs filesystem on it (you can of course also use a real block device or LVM if you want).

 # truncate -s 2G /srv/arch.img
 # mkfs.btrfs /srv/arch.img
 # export root=/srv/arch
 # mount --mkdir -o loop,compress=lzo /srv/arch.img "$root"

## Bootstrapping installation
Install  and , and run pacstrap to install the essential packages for the client:

 # pacstrap -K "$root" base linux linux-firmware mkinitcpio-nfs-utils nfs-utils

Now the initramfs needs to be constructed.

## NFS
Trivial modifications to the  hook are required in order for NFSv4 mounting to work (not supported by  – the default for the  hook).

 # sed s/nfsmount/mount.nfs4/ "$root/usr/lib/initcpio/hooks/net" > "$root/usr/lib/initcpio/hooks/netnfs4"
 # cp $root/usr/lib/initcpio/install/net{,nfs4}

The copy of  is unfortunately needed so it does not get overwritten when  is updated on the client installation.

Edit  and add  to ,  to , and  to .

Next, we chroot our installation and run mkinitcpio:

 # arch-chroot "$root" mkinitcpio -p linux

## NBD
The  package needs to be installed on the client. Build it with makepkg and install it:

 # pacman --root "$root" --dbpath "$root/var/lib/pacman" -U mkinitcpio-nbd-0.4-1-any.pkg.tar.xz

You will then need to append  to your  array after ;  will configure your networking for you, but not attempt a NFS mount if  is not specified in the kernel line.

## SKUF
To install Arch Linux on sparse file using SKUF Network Boot System, clone the git repository:
 $ git clone https://github.com/BiteDasher/skuf.git
 $ cd skuf
 $ ./switch-tag latest

Then, build the  package and ISO image which will later be used as a "kickstart" to start the main system using kexec

First of all, you need to tune the method of encrypting your passwords for SAMBA (see for more details):

Set up [https://github.com/BiteDasher/skuf#defaults-setup defaults:

Install required packages:
 # ./install_deps.sh

And finally, build  package:

 $ ./tune_crypt.sh
 $ ./tune_password.sh
 $ ./setup_defaults.sh
 $ ./build_rootfs_tar.sh
 $ ./build_package.sh

ISO image:

 # ./setup_repo.sh
 # ./build_iso.sh

And sparse file with Arch Linux:

 # ./create_image.sh -s SIZE_IN_GIGABYTES additional_packages

Then, move  in .

## Client configuration
In addition to the setup mentioned here, you should also set up your hostname, timezone, locale, and keymap, and follow any other relevant parts of the Installation guide.

## Boot loader
## GRUB
Though poorly documented, GRUB supports being loaded via PXE.

 # pacman --root "$root" --dbpath "$root/var/lib/pacman" -S grub

Create a grub prefix on the target installation for both architectures using .

 # arch-chroot "$root" grub-mknetdir --net-directory=/boot --subdir=grub

Luckily for us, grub-mknetdir creates prefixes for all currently compiled/installed targets, and the  maintainers were nice enough to give us both in the same package, thus grub-mknetdir only needs to be run once.

Now we create a trivial GRUB configuration:

{{hc|# vim "$root/boot/grub/grub.cfg"|2=
menuentry "Arch Linux" {
    linux /vmlinuz-linux quiet add_efi_memmap ip=:::::eth0:dhcp nfsroot=10.0.0.1:/arch
    initrd /initramfs-linux.img
}

menuentry "Arch Linux (NBD)" {
    linux /vmlinuz-linux quiet add_efi_memmap ip=:::::eth0:dhcp nbd_host=10.0.0.1 nbd_name=arch root=/dev/nbd0
    initrd /initramfs-linux.img
}
}}

GRUB will  automatically, so that the kernel and initramfs are transferred via TFTP without any additional configuration, though you might want to set it explicitly if you have any other non-tftp menuentries.

## PXELINUX
PXELINUX is provided by , see PXELINUX for details.

## Additional mountpoints
## NBD root
In late boot, you will want to switch your root filesystem mount to both , and enable , for much improved disk performance in comparison to NFS.

## Client boot
## NBD
If you are using NBD, the need to unmount  on the server before booting a client depends on your configuration:

* If  is disabled, you must unmount  before booting any client. Simultaneous read-write access to the base image will cause corruption.
* If  is enabled, clients only read from the base image and write to a separate cache, so a read-only server-side mount is theoretically safe. A read-write server-side mount is still discouraged while clients are active, as any modification to the base image during a live session risks inconsistency.

This makes things particularly interesting when it comes to kernel updates. You cannot have your client filesystem mounted while you are booting a client, but that also means you need to use a kernel separate from your client filesystem in order to build it.
You will need to first copy  from the client installation to your tftp root (i.e. ).

 # cp -r "$root/boot" /srv/boot

You will then need to umount  before you start the client.

 # umount "$root"

## copyonwrite permissions
To fix this, either transfer ownership of the export directory to the  user:
 # chown nbd: /path/to/export/directory

Or redirect COW cache files to a dedicated directory that the  user already owns, by adding to:

Ensure that directory is also owned by .

## SKUF
Write  to your USB drive, plug it in client computer and select in UEFI/BIOS settings as a boot device.

{{Note|If the client computer has UEFI, you can install  on a ESP partition so you don't have to use a USB flash drive/CD/DVD. To do this, mount  somewhere (like /mnt), then copy {{ic|/mnt/skuf/boot/x86_64/{vmlinuz-linux,initramfs-linux.img} }} to ESP partition and execute  where /dev/sdX is the target disk and Y is the target ESP partition number.}}
