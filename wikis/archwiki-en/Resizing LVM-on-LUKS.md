# Resizing LVM-on-LUKS

This article follows the process of resizing an LVM-on-LUKS-on-GPT partition. You can also use GParted GUI tool to resize LUKS partition, which may be easier and quicker for beginners.

## Method
The filesystem we work on will have the following structure:

The goal is to clear up unused space and create a new partition, , without any data loss. All filesystems are assumed to be .

The entire process should run from a live USB Arch system to avoid any filesystem corruption.

## Process
## Shrink LVM-on-LUKS
## Boot and setup
Boot into your live USB flash installation media.

Decrypt the LUKS volume:

 # cryptsetup luksOpen /dev/sda2 cryptdisk

## Resize filesystem and LVM logical volume
Follow these instructions.

You can run a  just to make sure nothing broke:

 # e2fsck -f /dev/vgroup/lvhome

## Resize LVM physical Volume
To calculate the new LVM physical volume size, use a simple formula: :

Using the formula above: .

Resize the volume. Note the "B" (Bytes) appended to the end of the value for size. This command is safe since it will exit early if the new size would not fit all the existing extents:

 # pvresize --setphysicalvolumesize 487814332416B /dev/mapper/cryptdisk

## Resize LUKS volume
To calculate the new LUKS volume size, use a simple formula:

 (116303 extents + 1 unusable extent) * 4194304 B/extent / 512 B/sector = 952762368 sectors

Resize the LUKS volume:

 # cryptsetup -b $NEW_LUKS_SECTOR_COUNT resize cryptdisk

## Resize the partition
To calculate the new partition size, use a simple formula: . The  is because parted takes an inclusive sector end parameter.

Close the LUKS volume to resize offline. You will probably need to deactivate LVM volumes on the cryptdisk or it will not close.

 # vgchange -a n vgroup
 # cryptsetup close cryptdisk

Use  to resize the partition:

 # parted /dev/sda
  (parted) unit
  Unit?  s
  (parted) p
  ...
   2      8003584s  2000408575s  1992404992s

Using the formula above returns:

 (parted) resizepart 2 960770047
  Warning: Shrinking a partition can cause data loss, are you sure you want to continue?
  Yes/No? y
  (parted) q

At this point you can reopen the LUKS volume and remount partitions. You will need to manually reactive the LVM partitions since if you manually deactivated them above.

 # cryptsetup luksOpen /dev/sda2 cryptdisk
 # vgchange -a y vgroup

## Enlarge LVM on LUKS
Enlarging a LVM-on-LUKS logical partition, for instance after migrating to a larger hard disk, is done in the opposite way - from the outermost to the innermost partition:

 primary partition(LUKS device{volume group[(logical partition1)(logical partition2-->)})

## Preparation
Create a new partition on the new hard disk of wanted size, f.i. by using GNU Parted, and clone the old partition , containing your LUKS container, into the new partition :

 # dd if=/dev/sdX1 of=/dev/sdY1 bs=4M

## Extending the physical segments of the cryptdevice
Now, open the cryptdevice  on the new hard disk:

 # cryptsetup open /dev/sdY1 CryptDisk

Take a look at your current physical volume. In this example, we have a cryptdevice  containing a volume group  of two partitions  and :

By taking the total physical extents (PE) times the PE's size, we get the total size of the physical volume (PV), in this case 118.75 GiB. Although pvdisplay does not show the free extents, we can enlarge the PV to use all the available remaining space of the partition:

 # pvresize /dev/mapper/CryptDisk

Now we get:

Note the free extents at the end of the PV. Calculate the size difference by taking the free physical extends times PE size - in that case (60922-30399)*4 MiB = 119.2 GiB.

## Resizing the logical volume
Now we are going to resize the second logical volume (LV), in this case containing the /home partition, by the size of the free physical extents minus some safety space:

 # lvresize -L +119G /dev/CryptVolumeGroup/home

Note the new size of the second logical volume. Calculate its total size by taking the total logical extends time the PE size - in that case 53438 * 4 MiB = 208.7 GiB:

## Resizing the encrypted volume
Now we are going to resize the encrypted volume itself. By taking in account the total size of the logical volume minus some safety space:

 # resize2fs -p /dev/CryptVolumeGroup/Home 208G
Execute e2fsck, if asked. That's it.
