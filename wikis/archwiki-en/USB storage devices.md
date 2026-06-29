# USB storage devices

This document describes how to use the popular USB memory sticks with Linux. However, it is also valid for other devices such as digital cameras that act as if they were just a USB storage device.

If you have an up-to-date system with the standard Arch kernel and a modern desktop environment, your device should just show up on your desktop, with no need to open a console.

## Auto-mounting with udisks
This is the easiest and most frequently used method. It is used by many desktop environments, but can be used separately too.

See Udisks for detailed information, including a list of mount helpers.

## Manual mounting
## Getting a kernel that supports usb_storage
If you do not use a custom-made kernel, you are ready to go; all Arch Linux stock kernels are properly configured. If you do use a custom-made kernel, ensure it is compiled with SCSI-Support, SCSI-Disk-Support and usb_storage. If you use the latest udev, you may just plug your device in and the system will automatically load all necessary kernel modules.

## Identifying device
The first thing one needs to access a storage device is its identifier assigned by kernel. See File systems#Identify existing file systems for details.

Newly plugged-in devices are usually shown in the journal.

## Mounting USB memory
See File systems#Mount a file system.

If  does not recognize the file system of the device you can try to use the  argument, see  for details. If mounting does not work, you can try to recreate the file system or even repartition the disk.

## Allow writing by regular users
If you want non-root users to be able to write to the USB stick, you can issue the following command:

 # mount -o gid=users,fmask=113,dmask=002 /dev/sda1 /mnt/usbstick

If it does not work, make sure that the file system is mountable and writable as root, see the previous section for details.

## As normal user with fstab
See FAT#Writing to FAT32 as normal user if you want normal user to do the mount/unmount action.

## Mount tools
Multiple mount tools facilitate mounting as a regular user.

## Troubleshooting
## No USB storage devices are detected
If you have connected your USB storage device and it is not listed by lsblk but appears in the journal without being assigned a block device, see General troubleshooting#Cannot use some peripherals after kernel upgrade.

Also ensure that your BIOS has both XHCI Handoff and EHCI Handoff enabled, but this is usually not an issue with most modern devices.

## Device not shutting down after unmounting all partitions
Failure to power off a device might result in:
* a hard disk drive not parking its head, making a faint scratching sound while spinning out and degrading the device or
* a solid-state drive (especially older) not flushing its cache buffers or updating its mapping tables, and losing data [https://www.kingston.com/us/solutions/servers-data-centers/ssd-power-loss-protection.

When you unmount the partitions, the device is still powered on. You should ask the system to turn it off first in order to safely remove it: # echo 1 > /sys/block/disk_name/device/delete

If you use udisks, you can use these commands: [https://unix.stackexchange.com/a/178648

 $ udisksctl unmount -b /dev/sdXY
 $ udisksctl power-off -b /dev/sdX

## Device is detected but does not register as mountable
udev is shipped with a default set of rules, found in , including one for ignoring some specific devices for various reasons. Some hardware devices, such as digital cameras, portable recorders, etc., may format usb storage in a way that results in the ignore rules to be triggered. You can check if one of these rules was applied with the following command and then find the corresponding conditions in the defaults:

 $ udevadm info --attribute-walk --name=device_name | grep UDISKS_IGNORE

If this is the case and your device has this property set to "1", you can override it with a custom rule, following udev#Example.
