# Convert a single drive system to RAID

This guide shows how to convert a functional single-drive system to a RAID 1 setup after adding a second drive, without the need to temporarily store the data on a third drive. The procedure can also be adapted, simplifying it, to the conversion of simple non-root partitions, and to other RAID levels.

## Scenario
This example assumes that the pre-existing disk is , which contains only one partition, , used for the whole system. The newly-added disk is .

## Prepare the new disk
## Partition the disk
The first step is creating the partition on the new disk, , that will be used as the mirror for the RAID array. In general, in this step it is not needed to recreate the exact partitioning scheme of the pre-existing drive; RAID can even be configured on whole disks, and partitions or logical volumes created later.

Make sure that the partition type is set as . See RAID#Prepare the devices and RAID#Partition the devices for more information.

## Create the RAID device
Next, create the RAID array in a degraded state, using only the new disk. Note how the  keyword is specified for the first device: this will be added later.

 # mdadm --create /dev/md0 --level=1 --raid-devices=2 missing /dev/device

Replace device with the one you are wanting to use before running the command.

If you want to use Syslinux, then specify  (for the boot partition). As of Syslinux 6.03, mdadm 1.2 is not yet supported in Syslinux. See also Software RAID and LVM.

Make sure the array has been created correctly by checking :

## Make file system
Create the needed file system on the  device.

## Copy the data on the array
Mount the array:

 # mount --mkdir /dev/md0 /mnt/new-raid

Now copy the data from  to , for example using rsync.

## Boot on the new disk
## Update the boot loader
Create a new entry in the boot loader to load the system from the RAID array in the new disk.

## GRUB legacy
Use your preferred text editor to open .

 --- SNIP ---
 default   0
 color light-blue/black light-cyan/blue

 ## fallback
 fallback 1

 # (0) Arch Linux
 title  Arch Linux - Original Disc
 root   (hd0,0)
 kernel /vmlinuz-linux root=/dev/sda1

 # (1) Arch Linux
 title  Arch Linux - New RAID
 root   (hd1,0)
 #kernel /vmlinuz-linux root=/dev/sda1 ro
 kernel /vmlinuz-linux root=/dev/md0 md=0,/dev/sda1,/dev/sdb1
 --- SNIP ---
Notice we added the  line and duplicated the Arch Linux entry with a different  directive on the kernel line.

Also update the "kopt" and "groot" sections, as shown below, if they are in your  file, because it will make applying distribution kernel updates easier:
 - # kopt=root=UUID=fbafab1a-18f5-4bb9-9e66-a71c1b00977e ro
 + # kopt=root=/dev/md0 ro md=0,/dev/sda1,/dev/sdb1

 ## default GRUB root device
 ## e.g. groot=(hd0,0)
 - # groot=(hd0,0)
 + # groot=(hd0,1)

See GRUB Legacy for more information.

## GRUB
Please refer to GRUB#RAID.

To boot the system from your degraded array, you will need to (1) add the  hook to the HOOKS in  (after the entry for ) and (2) regenerate the initramfs and generate a new configuration file. You can then add a menu entry in  pointing to the raid partitions for boot. This is complicated by the default generation options making use of a primary boot entry, and placing the remaining boot entries in sub-menus. To restore generation of a single entry per-line for each boot option, simply add:

    GRUB_DISABLE_SUBMENU=y

to  and regenerate . Now you can simply add an entry containing either the device files (e.g. ,  or simply use the UUID for each of the raid filesystems. After having done so, the easiest way to add an entry to boot from the degraded arrays is simply to copy the "Arch Linux, with Linux linux" entry and change the UUID to match your arrays as shown in .

## Alter fstab
You need to tell fstab on the new disk where to find the new device. It is recommended to use Persistent block device naming.

## Rebuild the initramfs
## Chroot into the RAID system
 # mount --bind /sys /mnt/new-raid/sys
 # mount --bind /proc /mnt/new-raid/proc
 # mount --bind /dev /mnt/new-raid/dev
 # chroot /mnt/new-raid/

If the chroot command gives you an error like , then use  instead.

## Record mdadm's config
Edit  and change the  line to be your email address, if you want emailed alerts of problems with the RAID 1.

Then save the array configuration with UUIDs to make it easier for the system to find  at boot. If you do not do this, you can get an  error when booting:

 # mdadm --detail --scan >> /etc/mdadm.conf

## Rebuild initcpio
Follow RAID#Configure mkinitcpio.

## Install the boot loader on the RAID array
## GRUB Legacy
Start GRUB:

 # grub --no-floppy

Then we find our two partitions - the current one (hd0,0) (I.e. first disk, first partition), and (hd1,1) (i.e. the partition we just added above, on the second partition of the second drive). Check you get two results here:

 grub> find /boot/grub/stage1
 (hd0,0)
 (hd1,1)

Then we tell GRUB to assume the new second drive is (hd0), i.e. the first disk in the system (when it is not currently the case). If your first disk fails, however, and you remove it, or you change the order disks are detected in the BIOS so that you can boot from your second disk, then your second disk will become the first disk in the system. The MBR will then be correct, your new second drive will have become your first drive, and you will be able to boot from this disk.

 grub> device (hd0) /dev/sdb

Then we install GRUB onto the MBR of our new second drive. Check that the "partition type" is detected as "0xfd", as shown below, to make sure you have the right partition:

 grub> root (hd0,1)
  Filesystem type is ext2fs, partition type 0xfd
 grub> setup (hd0)
  Checking if "/boot/grub/stage1" exists... yes
  Checking if "/boot/grub/stage2" exists... yes
  Checking if "/boot/grub/e2fs_stage1_5" exists... yes
  Running "embed /boot/grub/e2fs_stage1_5 (hd0)"...  16 sectors are embedded. succeeded
  Running "install /boot/grub/stage1 (hd0) (hd0)1+16 p (hd0,1)/boot/grub/stage2 /boot/grub/grub.conf"... succeeded
  Done
 grub> quit

## Verify success
Reboot the computer, making sure it boots from the new RAID disk () and not the original disk (). You may need to change the boot device priorities in your BIOS to do this.

Once the boot loader on the new disk loads, make sure you select to boot the new system entry you created earlier.

Verify you have booted from the RAID array by looking at the output of mount. Also check mdstat again only to confirm which disk is in the array.

If the system boots fine, and the output of the above commands is correct, then you are running off the degraded RAID array, as expected.

## Add original disk to array
## Partition original disk
Copy the partition table from  (newly implemented RAID disk) to  (second disk we are adding to the array) so that both disks have exactly the same layout:

 # sfdisk -d /dev/sdb | sfdisk /dev/sda

Alternative method: this will output the  partition layout to a file, then it is used as input for partitioning .

 # sfdisk -d /dev/sdb > raidinfo-partitions.sdb
 # sfdisk /dev/sda ....................]  recovery =  0.2% (5973824/2930034432) finish=332.5min speed=146528K/sec
      bitmap: 22/22 pages 65536KB chunk

unused devices:
}}
