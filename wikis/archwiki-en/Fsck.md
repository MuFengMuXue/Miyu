# Fsck

fsck stands for "file system check" and it is used to check and optionally repair one or more Linux file systems. Normally, the fsck program will try to handle file systems on different physical disk drives in parallel to reduce the total amount of time needed to check all of the file systems (see ).

The Arch Linux boot process conveniently takes care of the fsck procedure for you and will check all relevant partitions on your drive(s) automatically on every boot. Hence, there is usually no need to resort to the command-line.

## Boot time checking
## Mechanism
There are two players involved:

# mkinitcpio offers you the option to fsck your root file system before mounting it via the  hook. If you do this, you should mount root read-write via the appropriate  kernel parameter.https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/commit/449b3e543c
# systemd will fsck all file systems having a fsck pass number greater than 0 (either with #fstab options or a user-supplied unit file). For the root file system, it also has to be mounted read-only initially with the kernel parameter  and only then remounted read-write from fstab (note that the  mount option implies ).

The first option is the recommended default, and what you will end up with if you follow the Installation guide. If you want to go with option 2 instead, you should remove the  hook from  and use  on the kernel command-line. The kernel parameter  can be used to make sure fsck is disabled entirely for both options.

## Forcing the check
If you use the  mkinitcpio hook, you can force fsck at boot time by passing  as a kernel parameter. This will check every file system you have on the machine.

Alternatively, systemd provides , which checks all configured file systems, which were not checked in the initramfs. However, checking the root file system this way causes a delay in the boot process, because the file system has to be remounted.

## Automatically answer yes to all repair questions
The boot time fsck checks might end up saying

This happens when you need to apply some changes to fix the file system which are not considered completely safe, and thus require fsck to be run manually.

You can set  to automatically apply all suggested change (i.e. answer yes to all questions) by setting the  kernel command line option to . (Other possible values are  and .) Check the documentation  for the meaning of these options.

## Tips and tricks
## Attempt to repair damaged blocks
To automatically repair damaged portions of an ext2/ext3/ext4 or FAT file system, run:

 # fsck -a

## Repair damaged blocks interactively
This is useful for when files on the boot partition have changed, and the journal failed to properly update. In this case, unmount the boot partition, and run the following code to repair damaged portions:

 # fsck -r drive

## Changing the check frequency
By default, fsck checks a file system every 30 boots (counted individually for each partition). To change the frequency of checking, run:

 # tune2fs -c 20 /dev/sda1

In this example,  is the number of boots between two checks.

Note that  would make it scan at every boot, while  would stop scanning altogether.

If you wish to see the frequency number and the current mount count for a specific partition, use:

 # dumpe2fs -h /dev/sda1  grep -i 'mount count'

## fstab options
fstab is a system configuration file and is used to tell the Linux kernel which partitions (file systems) to mount and where on the file system tree.

A typical  entry may look like this:

 /dev/sda1   /         ext4      defaults       0  1
 /dev/sda2   /other    ext4      defaults       0  2
 /dev/sda3   /win      ntfs-3g   defaults       0  0

The 6th column (in bold) is the fsck option.

*  — do not check.
*  — first file system (partition) to check;  (root partition) should be set to .
*  — all other file systems to be checked.

## Troubleshooting
## Can't run fsck on a separate /usr partition
# Make sure you have the required hooks in  and that you remembered to re-generate your initramfs image after editing this file.
# Check your fstab! Only the root partition needs  at the end, everything else should have either  or . Carefully inspect it for other typos, as well.

## ext2fs: no external journal
There are times (due to power failure) in which an ext(3/4) file system can corrupt beyond normal repair. Normally, there will be a prompt from fsck indicating that it cannot find an external journal. In this case, run the following commands:

Unmount the partition based on its directory

 # umount directory

Write a new journal to the partition

 # tune2fs -j /dev/partition

Run an fsck to repair the partition

 # fsck -p /dev/partition
