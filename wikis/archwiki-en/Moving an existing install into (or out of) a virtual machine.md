# Moving an existing install into (or out of) a virtual machine

This article describes how to transfer your current Arch Linux installation in or out of a virtual environment (i.e. QEMU, VirtualBox, VMware). A virtual machine uses different hardware, which needs to be addressed by re-generating the initramfs image and possibly adjusting the fstab – especially if it is an SSD.

## Moving out of a virtual machine
Moving out of a virtual environment is relatively easy.

## Set up a shared folder
Setting up a shared folder between the guest virtual machine and the host depends on the hypervisor you use. Please thus refer to their specific wiki page or manual.

If you do not already have an ext4 partition, see File systems.

If you are on Windows, install Ext2Fsd to be able to mount ext volumes.

## Transfer the system
From the virtual machine, open a terminal and transfer the system:

 # rsync -aAXHSv /* /path/to/shared/folder --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found,/home/*/.gvfs}

This can also be done with clonezilla boot disk or dd from a random Linux live-cd. If you are using Virtualbox you need to connect the target drive through USB (or SATA to USB cable) otherwise use an external USB drive to save the disk image (with dd or clonezilla).

## Chroot and reinstall the boot loader
Boot a "live" GNU/Linux distribution, mount the root partition and chroot into it.

Reinstall your boot loader or boot manager: either Syslinux, GRUB or systemd-boot. Do not forget to update the configuration file:  for Syslinux,  for Grub, or the systemd-boot boot entries located in .

## Adjust the fstab
Since your entire root tree has been transferred to a single partition, edit the fstab file to reflect the right partition(s).

Check with the  command, since  is not very useful inside a chroot.

## Re-generate the initramfs image
Because the hardware has changed, while you are still in the chroot, regenerate the initramfs.

And that is about it.

You will most likely need to set up the network, since the virtual machine was probably piggybacking on the host OS's network settings. See Network configuration.

## Moving into a virtual machine
Moving into a virtual environment takes a little more effort.

## Create the container
This will create a 32 GiB raw image:

 # fallocate -l 32GiB -o 1024 /media/Backup/backup.img

If you want to create one the exact size of your root partition, run  and use the value from the  column for the  parameter. Note that you will transfer your entire root tree, so that includes the  and  folders. If you have any separate partitions for those, you need to take them into account when creating the container.

Partition the  file by running your favourite partitioning tool. Create a partition table on it (e.g. ), choose the partition scheme and create the partitions.

Now load the necessary module and mount it as a loopback device, on  (for example):

 # modprobe loop
 # losetup --partscan /dev/loop5 /media/Backup/backup.img

Then create a file system on the partitions, which will appear as , , etc.

## Transfer the system
Mount the loopback device and transfer the system:

 # mount --mkdir /dev/loop5p1 /mnt/Virtual
 # rsync -aAXv /* /mnt/Virtual --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found,/home/*/.gvfs}

## Convert the container to a compatible format
Choose the appropriate command depending on the desired virtual machine.

To convert into a KVM container, use  with the following command line:

 $ qemu-img convert -c -f raw -O qcow /media/backup.img /media/backup.qcow2

To convert into a VirtualBox container, use  with the following command line:

 $ VBoxManage convertfromraw --format VDI /media/backup.img /media/backup.vdi

To convert into a VMware container, use virtualbox with the following command line:

 $ VBoxManage convertfromraw --format VMDK /media/backup.img /media/backup.vmdk

## Chroot and reinstall the boot loader
Connect the container to the virtual machine, along with a Linux LiveCD (e.g. the latest Arch Linux ISO) in the virtual machine's virtual CD-ROM, then start the virtual machine and chroot into it:

 # mount /dev/sda1 /mnt
 # arch-chroot /mnt /bin/bash

Reinstall either Syslinux or GRUB. Do not forget to update its configuration file:

* For Syslinux, it should be  in .
* For GRUB, it is recommended that you automatically re-generate a .

## Adjust the fstab
Since your entire root tree has been transferred to a single partition, edit the fstab file. You may use the UUID or label if you want, but those are more useful in multi-drive, multi-partition configurations (to avoid confusions). For now,  for your entire system is just fine.

## Disable any Xorg-related files
Having an , , , , etc., entry in the  section from one of the Xorg configuration files will prevent it from starting, since you will be using emulated hardware (including the video card). So it is recommended that you move/rename or delete the following:

 # mv /etc/X11/xorg.conf /etc/X11/xorg.conf.bak
 # mv /etc/X11/xorg.conf.d/10-monitor /etc/X11/xorg.conf.d/10-monitor.bak

## Re-generate the initramfs image
Because the hardware has changed, while you are still in the chroot, re-generate the initramfs image and do a proper shutdown:

 # mkinitcpio -p linux
 # exit
 # umount -R /mnt
 # poweroff

Finally, pull out the LiveCD (the ISO file), so that you do not boot back into it, and start the virtual machine.

Enjoy your new virtual environment.

## Troubleshooting
## "mount: special device /dev/loop5p1 does not exist"
Use , for example:

 # losetup --partscan /dev/loop5 /media/Backup/backup.img

This should create device nodes for each partition you have created inside the loop device.

## "Waiting 10 seconds for device /dev/sda1; ERROR: Unable to find root device '/dev/sda1'"
 Waiting 10 seconds for device /dev/sda1 ...
 ERROR: Unable to find root device '/dev/sda1'.
 You are being dropped to a recovery shell
     Type 'exit' to try and continue booting
 sh: cannot access tty; job control turned off
 /# _

It most likely means that you did not run  like you were instructed to, and closed the virtual machine with the "close" button, which is the equivalent of a power outage. Now you need to regenerate your initramfs image. To do that, you can start the virtual machine using the Fallback entry. If you do not have a Fallback entry, press  (for Syslinux) or  (for GRUB) and rename it . After it boots, open up a terminal and run:

 # mkinitcpio -p linux
 # poweroff

## "Missing operating system. FATAL: INT18: BOOT FAILURE"
* You either need to install or reinstall a boot loader. See Arch boot process#Boot loader.
* You are using a Btrfs filesystem with compression for , for which Syslinux currently cannot boot from.
* The boot order from the BIOS or from the virtual machine's settings is not properly set up. Make sure that the drive containing the boot loader is the first one to boot.

## I am asked for the root password, for maintenance
 :: Checking Filesystems                        BUSY
 fsck.ext4: Unable to resolve '...'

This means that you forgot to add the drive's UUID, label or device name in . The UUID is different every time you format it (or in this case, create one from scratch), and they likely do not match. Check with .
