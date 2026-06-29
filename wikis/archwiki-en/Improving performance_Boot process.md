# Improving performance/Boot process

Improving the boot performance of a system can provide reduced boot wait times and serves as a means to learn more about how certain system files and scripts interact with one another. This article attempts to aggregate methods on how to improve the boot performance of an Arch Linux system.

## Analyzing the boot process
## Using systemd-analyze
systemd provides a tool called  that can be used to show timing details about the boot process, including an svg plot showing units waiting for their dependencies. You can see which unit files are causing your boot process to slow down. You can then optimize your system accordingly.

To see how much time was spent in kernelspace and userspace on boot, simply use:

 $ systemd-analyze

To list the started unit files, sorted by the time each of them took to start up:

 $ systemd-analyze blame

At some points of the boot process, things can not proceed until a given unit succeeds. To see which units find themselves at these critical points in the startup chain, do:

 $ systemd-analyze critical-chain

You can also create an SVG file which describes your boot process graphically, similar to Bootchart:

 $ systemd-analyze plot > plot.svg

See  for details.

## Using bootchart2
You could also use Bootchart2 to visualize the boot sequence.

## Compiling a custom kernel
Compiling a custom kernel can reduce boot time and memory usage. Though with the standardization of the 64-bit architecture and the modular nature of the Linux kernel, these benefits may not be as great as expected. See Kernel#Compilation for more info.

Compression level of modules of official kernel is built with . But  may be better for SSD.

It is recommended to make modules for storage and file system for your root volume built-in to allow running without initramfs.

## Initramfs
If possible in your setup, running without initramfs should provide the fastest way.

mkinitcpio uses the  and  hooks by default. Faster boot times can be achieved by replacing them with . See Mkinitcpio#Common hooks for more details. See also Fsck#Boot time checking if replacing the  hook.

In a similar approach to #Compiling a custom kernel, the initramfs can be slimmed down. A simple way is to include the mkinitcpio  hook. Booster generates initramfs smaller than mkinitcpio or dracut with fast single binary init. See Minimal initramfs or Booster#Removing modules.

Depending on your hardware (processor and storage speed), using  instead of the default  compression option may be quicker since the faster decompression speed at boot time usually offsets the slightly larger size of the initramfs that has to be read from disk. See Mkinitcpio#COMPRESSION.

You can also minimize Microcode image https://gitlab.archlinux.org/archlinux/packaging/packages/intel-ucode/-/merge_requests/2 by intel-ucode if you use running without initramfs or Booster:

## Choose the adequate way to start for services
One central feature of systemd is D-Bus and socket activation. This feature should be preferred for most cases as it causes services to be started only when they are first accessed and is generally a good thing (e.g. having  enabled at boot time is usually not useful for desktop use, enable instead  which will only start the service when actually printing).

However, if you know that a service (like ) will always be started during boot, then the overall boot time might be reduced by starting it as early as possible. This can be achieved (if the service file is set up for it, which in most cases it is) by enabling .

This will cause systemd to start UPower as soon as possible, without causing races with the socket or D-Bus activation.

## Staggered spin-up
Some hardware implements staggered spin-up, which causes the OS to probe ATA interfaces serially, which can spin up the drives one-by-one and reduce the peak power usage. This slows down the boot speed, and on most consumer hardware provides no benefits at all since the drives will already spin-up immediately when the power is turned on. To check if SSS is being used:

 # dmesg | grep SSS

If it was not used during boot, there will be no output.

To disable it, add the  kernel parameter.

## Filesystem mounts
Thanks to mkinitcpio's  hook, you can avoid a possibly costly remount of the root partition by changing  to  on the kernel line: options can be set with . The entry must be removed from the  file, otherwise the  will continue to try applying these settings. Alternatively, one could try to mask that unit.

If Btrfs is in use for the root filesystem, there is no need for a fsck on every boot like other filesystems. If this is the case, mkinitcpio's  hook can be removed. You may also want to mask the , or tell it not to fsck the root filesystem from the kernel command line using . Without mkinitcpio's  hook, systemd will still fsck any relevant filesystems with the

You can also remove API filesystems from , as systemd will mount them itself (see  for a list). It is not uncommon for users to have a  entry carried over from sysvinit, but you may have noticed from the command above that systemd already takes care of this. Ergo, it may be safely removed.

Other filesystems, like  or EFI system partition, can be mounted with custom mount units. Adding  to mount options will buffer all access to that partition, and will fsck and mount it on first access, reducing the number of filesystems it must fsck/mount during the boot process.

## Less output during boot
For some systems, particularly those with an SSD, the slow performance of the TTY is actually a bottleneck, and so less output means faster booting. See the Silent boot article for suggestions.

## Changing boot loader
Changing your boot loader (e.g. a simpler boot loader such as systemd-boot) may reduce boot time by seconds.

If your setup allows it, try using only an EFI boot stub for even shorter boot times.

## Suspend to RAM
The best way to reduce boot time is not booting at all. Consider suspending your system to RAM instead.
