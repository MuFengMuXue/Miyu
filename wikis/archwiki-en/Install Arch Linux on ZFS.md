# Install Arch Linux on ZFS

This article details the steps required to install Arch Linux onto a ZFS root file system.

## Create a custom ISO
To install Arch Linux on ZFS, you need to use an installation medium with ZFS kernel modules.

Follow archiso#Installation.

Then follow archiso#Prepare a custom profile to prepare a custom profile (named  in the following example), see also archiso#ArchZFS example.

Then edit the package list file——to add the  kernel and the following ZFS packages:

Make sure to remove  and  (which would pull in the  package) from the list.

You will also need to edit  and append:

You will also need to edit the following files to change  and  entries to  and :

Now we will make an  and  pair of directories to start the build process:

 # mkdir isobuild
 # mkarchiso -v -r -w /tmp/archiso-tmp -o isobuild ~/archlive

You should now have an  in the  directory.

Burn this file to your installation media of choice.

Be sure to test your new ISO with a virtual machine. Run:

 # modprobe zfs
 # zpool status

If it fails, then your zfs module did not build correctly, and you will have to try again.

## Partitioning
ZFS supports both GPT and MBR partition tables. See Partitioning#Choosing between GPT and MBR for information on determining the partition table type to use.

ZFS manages its own partitions, so only a basic partition table scheme is required. The partition that will contain the ZFS file system should be of the type , or "Solaris Root":

Using GRUB on a BIOS (or UEFI machine in legacy boot mode) machine but using a GPT partition table:

You can choose to separate Linux swap partition, or using a zvol, see ZFS#Swap volume, as swap.

If you wish to create a traditional swap partition, see Partitioning#Example layouts.

If you have opted for a boot partition as well as any other non-ZFS system partitions then format them.

## Set up ZFS
First, make sure the ZFS modules are loaded,

 # modprobe zfs

## Create the root zpool
Create your pool and set all default dataset options. All dataset created on the zpool will inherit of each  set at the zpool creation. Default options are detailed in Debian Buster Root on ZFS. Step 2: Disk Formatting.

## Compression and native encryption
This will enable compression and native encryption by default on all datasets:

The options after  control ZFS behavior.
A detailed explanation of them can be found in the  man page.

## Create your datasets
Instead of using conventional disk partitions, ZFS has the concept of datasets to manage your storage. Unlike disk partitions, datasets have no fixed size and allow for different attributes, such as compression, to be applied per dataset. Normal ZFS datasets are mounted automatically by ZFS whilst legacy datasets are required to be mounted using fstab or with the traditional mount command.

One of the most useful features of ZFS is boot environments. Boot environments allow you to create a bootable snapshot of your system that you can revert to at any time instantly by simply rebooting and booting from that boot environment. This can make doing system updates much safer and is also incredibly useful for developing and testing software. In order to be able to use a boot environment manager such as beadm,  (systemd-boot), or  (GRUB) to manage boot environments, your datasets must be configured properly. Key to this are that you split your data directories (such as ) into datasets that are distinct from your system datasets and that you do not place data in the root of the pool as this cannot be moved afterwards.

You should always create a dataset for at least your root filesystem and in nearly all cases you will also want  to be in a separate dataset. You may decide you want your logs to persist over boot environments. If you are a running any software that stores data outside of  (such as is the case for database servers) you should structure your datasets so that the data directories of the software you want to run are separated out from the root dataset.

With these example commands, we will create a basic boot environment compatible configuration comprising of just root and  datasets. It inherits default options from zpool creation.

 # zfs create -o mountpoint=none zroot/data
 # zfs create -o mountpoint=none zroot/ROOT
 # zfs create -o mountpoint=/ -o canmount=noauto zroot/ROOT/default
 # zfs create -o mountpoint=/home zroot/data/home

You can also create your ROOT dataset without having to specify mountpoint to / since GRUB will mount it to / anyway. That gives you possibility to boot into some old versions of root just by cloning it and putting as menuentry of GRUB. In such, you can create ROOT with the following command:

 # zfs create -o mountpoint=/roots/default zroot/ROOT/default

You can store  in your  dataset.

 # zfs create -o mountpoint=/root zroot/data/home/root

## System datasets
To create datasets for system directories, use .

For some examples, please read Debian-Buster-Root-on-ZFS#step-3-system-installation.

 # zfs create -o mountpoint=/var -o canmount=off                 zroot/var
 # zfs create                                                    zroot/var/log
 # zfs create -o mountpoint=/var/log/journal -o acltype=posixacl zroot/var/log/journal
 # zfs create -o mountpoint=/var/lib -o canmount=off             zroot/var/lib
 # zfs create                                                    zroot/var/lib/libvirt
 # zfs create                                                    zroot/var/lib/docker

## Export/Import your pools
To validate your configurations, export then reimport all your zpools.

 # zpool export zroot
 # zpool import -d /dev/disk/by-id -R /mnt zroot -N

If you used native encryption, load zfs key.

 # zfs load-key zroot

Manually mount your rootfs dataset because it uses , then mount all others datasets.

 # zfs mount zroot/ROOT/default
 # zfs mount -a

The ZFS filesystem is now ready to use.

## Configure the root filesystem
If you used legacy datasets, it must be listed in .

Set the bootfs property on the descendant root filesystem so the boot loader knows where to find the operating system.

 # zpool set bootfs=zroot/ROOT/default zroot

If you do not have , create it:

 # zpool set cachefile=/etc/zfs/zpool.cache zroot

Be sure to bring the  file into your new system. This is required later for the ZFS daemon to start.

 # mkdir -p /mnt/etc/zfs
 # cp /etc/zfs/zpool.cache /mnt/etc/zfs/zpool.cache

## Install and configure Arch Linux
Follow the following steps using the Installation guide. It will be noted where special consideration must be taken for ZFSonLinux.

* First mount any legacy or non-ZFS boot or system partitions using the mount command.

* Install the base system.

* The procedure described in Installation guide#Fstab is usually overkill for ZFS. ZFS usually auto mounts its own partitions, so we do not need ZFS partitions in  file, unless the user made legacy datasets of system directories. To generate the  for filesystems, use:

 # genfstab -U -p /mnt >> /mnt/etc/fstab

* Change root into the new system, per Installation guide#Chroot:

 # arch-chroot /mnt

* Edit the :

* You need to add the ArchZFS repository to , sign its key and install  as well as  within the arch-chroot before you can update the ramdisk with ZFS support.

* When creating the initial ramdisk, first edit . Add  to :

 MODULES=(zfs)

Then in , add  before filesystems. Also, move  hook before  so you can type in console if something goes wrong. Your  line should look something like the following:

 HOOKS=(base udev … block zfs filesystems)

* Regenerate the initramfs.

* Add ZFS to your kernel command line

You can now set up your boot loader. You also need to add a kernel parameter to make ZFS bootable:

 root=ZFS=zroot/ROOT/default rw

## Configure systemd ZFS mounts
For your system to be able to reboot without issues, you need to enable the  to auto mount the pools and set the hostid.

For each pool you want automatically mounted execute:

 # zpool set cachefile=/etc/zfs/zpool.cache pool

Enable

In order to mount zfs pools automatically on boot you need to enable,  and .

When running ZFS on root, the machine's hostid will not be available at the time of mounting the root filesystem. There are two solutions to this. You can either place your spl hostid in the kernel parameters in your boot loader. For example, adding , to get your number use the  command.

The other, and suggested, solution is to make sure that there is a hostid in , and then regenerate the initramfs image which will copy the hostid into the initramfs image. To write the hostid file safely you need to use the  command.

To use the libc-generated hostid (recommended):

 # zgenhostid $(hostid)

To use a custom hostid (must be hexadecimal and 8 characters long):

 # zgenhostid deadbeef

To let the tool generate a hostid:

 # zgenhostid

Do not forget to regenerate the initramfs.

## Unmount and restart
We are almost done! If you have a legacy boot partition:

 # umount /mnt/boot

Otherwise:

 # zfs umount -a
 # zfs umount zroot/ROOT/default
 # zpool export zroot

Now reboot.

## Loading password from USB-Stick
It is possible to store password on usb-stick and load it when booting:

Save password on first bytes of usb-stick:

 # dd if=your_password_file bs=32 count=1 of=/dev/disk/by-id/usb_stick

To create partition zfs partition you can either use previous described method with password prompt or pipe with dd:

 # dd if=/dev/disk/by-id/usb_stick bs=32 count=1 | zfs create -o encryption=on -o keyformat=passphrase zroot/ROOT

Next step is modyfing zfs hook. By default zfs prompts for password. You have to change it to have it piped with dd from your pendrive. In order to do so modify  and change line:

 # ! eval zfs load-key "${encryptionroot}"; do

to:

 # ! eval dd if=/dev/disk/by-id/usb_stick bs=32 count=1 | zfs load-key "${encryptionroot}"; do

You are modifying your zfs hook so do not forget to regenerate the initramfs. Now zfs should load password from your usb-stick on boot.

## Troubleshooting
## System fails to boot due to: cannot import zroot: no such pool available
You can try the following steps and see if they can help.

* Use the kernel modules from the ArchZFS repository instead of the DKMS version. You can go back to the DKMS version after a successful boot.
* Remove the  and run:
* Remove the .
* Regenerate the initramfs.

## Zpool refuses to export saying it's busy
Arch-chroot will mount specific kernelspace file systems in the system. If these are not unmounted, the zpool may refuse to dismount properly. If this happens, remount the ZFS partition and run

Then run  against the partition still mounted.

This should allow the zpool to export.
