# Mkinitcpio/Minimal initramfs

This article shows how to create a slim, minimal initramfs for a system with a specific, known and static hardware configuration. The procedure is expounded from Optimizing Bootup With mkinitcpio by Falconindy (Dave Reisner).

## Udev requirement
The big advantage of creating your own initramfs images is that you can eliminate . This hook alone is responsible for quite a bit of size (~700-800 KiB with LZ4 and LZOP, less with other algorithms) in the initramfs image. Not only will the bigger size lead to longer boots (more data to decompress) but initializing  itself will also take some extra time. However, some things require . This includes resolving UUID, LABEL, PARTUUID and PARTLABEL identifiers (workaround hook without-udev) and the assembly of LVM and mdadm devices that contain the  partition. If you are unsure if you need , continue with the directions on this page up until the #Initial test. If not everything works without , re-enable the hook and try again.

Also, while most keyboards (AT, PS/2, USB) do not require the use of the  hook, Logitech USB devices using the Logitech Unified Receiver do. At this point you could either include  in all images or rely on a  image that does.

If you need , your minimization efforts will most likely be in vain. You may still be able to shrink the image size by ~600 KiB, but boot times will not be significantly improved. Continuing on in this scenario can still be a worthwhile learning experience.

## Editing .preset files
In Falconidy's tutorial, he edits  and runs  to create the test initramfs image, leaving the known-good initramfs images on the system untouched.  However, if you blindly run  afterwards, even the  image will be stripped down.

A safer way to prepare for taking the creation of the initramfs files into your own hands is to modify the  files in .  The following example configuration will supplant  with the minimal initramfs image and create a new  image that is built The Arch Way.  If things go wrong, you can rely on the  or  images.  When you are finished, you can drop the  lines from the configuration and remove the  files.

## Finding needed modules
The quickest way to find out what modules you need is to reboot your system with the  initramfs image and add  to the kernel parameters in your boot loader so you get dropped to the command line once the root filesystem is mounted.

Once your system reboots, run the following command to see what modules you need:

 lsmod | awk 'NF==3{print $1}'

{{Note|The  command returns only the first field, using {{ic|{print $1} }}, of every line with exactly 3 fields, enforced by . Module dependencies include the 4th field to show which module pulled in the dependency, thus being filtered out due to that fourth field.  Arch's  takes care of dependencies for legitimate values included in the arrays , , and .}}

Write down the modules that were loaded and type  to continue booting.

Alternatively, Install the package  to help determine necessary modules. Though unmaintained, it can provide valuable information. Also, see Kernel modules to get started with the native tools.

## Initial edit of mkinitcpio.conf
Edit  and modify the  array. A worthwhile note is that  is sourced, so you can build the MODULES array like in a bash script.

 MODULES=()   # filesystems
 MODULES+=()  # storage
 MODULES+=()  # keyboard
 MODULES+=()  # miscellaneous

Add all your modules to the last  line.  As you sort through your modules, you can place them in the appropriate line.

You will also need the binaries to do filesystem checks on the  device and any other mount points in  that have been set to do so.

* For extdevices:
 BINARIES=(fsck fsck.ext[2|3|4 e2fsck)
* For vfat (UEFI boot) partitions:
 BINARIES=(fsck fsck.vfat dosfsck)
* For btrfs single disk device:
 BINARIES=(fsck fsck.btrfs btrfsck)
* For btrfs multi disk device:
 BINARIES=(fsck fsck.btrfs btrfs btrfsck)
* For xfs devices
 BINARIES=(fsck fsck.xfs xfs_repair)

## Initial test
Edit  and run  to rebuild all of your initramfs images.  Then reboot.

Your first boot should be successful if you do not need .  If something does not work (eg, Arch cannot find your root partition or your keyboard does not work) then you will need to go back and remove  from the  parameter in the  line and try again.  If you need , keep in mind that you will not see a significant improvement in boot time and continuing on is only good for a learning experience.

## Sorting out modules
Now that you have a known-good bootable initramfs, it is time to slim down the initramfs even further.  The normal method is to remove a few modules at a time, rebuild the initramfs images, and reboot to see if everything is still OK.  If you find out that everything is not OK, reboot with the  initramfs image and re-add the deleted modules until everything is OK again.  Rinse and repeat until you have only the modules you need.  As this can be a tedious experience, the following lists are provided to give people a head-start in the elimination process.

## Filesystem modules
*
*
*
*

## Storage device modules
* for all SCSI, SATA, and PATA (IDE) devices
* for SATA devices on modern AHCI controllers
* and  for NVMe (M.2, PCIe) devices
* for SATA devices on IDE-mode controllers
* for PATA (IDE) devices
* and  for USB storage devices
* and  for QEMU/KVM VMs using VirtIO for storage

## Keyboard modules
* for AT and PS/2 keyboards, and the emulated keyboard in QEMU/KVM.
*, , and  for normal USB keyboards.
* for Apple keyboards.
*, , and  for Logitech USB keyboards using the Logitech Unified Receiver  (requires the  hook).

## Finishing up
Once you have slimmed your initramfs as far as it will go, remove (or comment-out) the  lines from your  files and remove the  files from .
