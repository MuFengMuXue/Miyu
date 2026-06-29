# Swap

This page provides an introduction to swap space and paging on GNU/Linux. It covers creation and activation of swap partitions and swap files.

From All about Linux swap space:

:Linux divides its physical RAM (random access memory) into chunks of memory called pages. Swapping is the process whereby a page of memory is copied to the preconfigured space on the hard disk, called swap space, to free up that page of memory. The combined sizes of the physical memory and the swap space is the amount of virtual memory available.

Support for swap is provided by the Linux kernel and user-space utilities from the  package.

## Swap space
Swap space can take the form of a disk partition or a file. Users may create a swap space during installation or at any later time as desired. Swap space can be used for two purposes, to extend the virtual memory beyond the installed physical memory (RAM), and also for suspend-to-disk support.

Whether or not it is beneficial to extend the virtual memory with swap depends on the amount of installed physical memory. If the amount of physical memory is less than the amount of memory required to run all the desired programs, then it may be beneficial to enable swap. This avoids out of memory conditions, where the Linux kernel OOM killer mechanism will automatically attempt to free up memory by killing processes. To increase the amount of virtual memory to the required amount, add the necessary difference (or more) as swap space.

The biggest drawback of using swap when running out of memory is its lower performance, see section #Performance. Hence, enabling swap is a matter of personal preference: some prefer programs to be killed over enabling swap and others prefer enabling swap and slower system when the physical memory is exhausted.

To check swap status, use:

 $ swapon --show

Or to show physical memory as well as swap usage:

 $ free -h

## Swap partition
A swap partition can be created with most GNU/Linux partitioning tools. Swap partitions are designated by the partition type GUID  on GPT ( type for gdisk,  type for fdisk) and type ID  on MBR.

To set up a partition as Linux swap area, the  command is used. For example:

 # mkswap /dev/sdxy

To enable the device for paging:

 # swapon /dev/sdxy

See  for the options syntax.

## Enabling at boot
To enable the swap partition at boot time, either:

* use systemd#GPT partition automounting
* or add an entry to . E.g.:

:where the  is the UUID of the swap space.

See fstab for the file syntax, and systemd#systemd.mount - mounting.

## Disabling swap
To deactivate specific swap space:

 # swapoff /dev/sdxy

Alternatively use the  switch to deactivate all swap space.

Since swap is managed by systemd, it will be activated again on the next system startup. To disable the automatic activation of detected swap space permanently, run  to find the responsible .swap unit and mask it.

## Swap file
As an alternative to creating an entire partition, a swap file offers the ability to vary its size on-the-fly, and is more easily removed altogether. This may be especially desirable if disk space is at a premium (e.g. a modestly-sized SSD).

{| class="wikitable sortable"
! File system
! Supports swap files
|-
| Bcachefs
|
|-
| Btrfs
|
|-
| F2FS
|
|-
| ext4
|
|-
| JFS
|
|-
| NILFS2
|
|-
| NTFS3
|
|-
| XFS
|
|-
| ZFS
|
|}

## Swap file creation
Use  to create a swap file the size of your choosing (see Partitioning#Swap for advice). For example, creating a 4 GiB swap file:

 # mkswap -U clear --size 4G --file /swapfile

Activate the swap file:

 # swapon /swapfile

Finally, edit the fstab configuration to add an entry for the swap file:

As an alternative to fstab, a swap unit can be created (see ):

Perform a daemon-reload and enable .

For additional information, see fstab#Usage.

## Swap file removal
To remove a swap file, it must be turned off first and then can be removed:

 # swapoff /swapfile
 # rm -f /swapfile

Finally, remove the relevant entry from .

## Swap encryption
See dm-crypt/Swap encryption.

## Performance
Swap operations are usually significantly slower than directly accessing data in RAM. However, disabling swap entirely to improve performance can sometimes lead to a degradation. If there is not enough physical memory available to hold everything, swapping out nothing leaves less memory available for file system caches, causing more frequent and costly disk usage.

Swap values can be adjusted to help performance:

## Swappiness
When memory usage reaches a certain threshold, the kernel starts looking at active memory and seeing what it can free up. File data can be written out to the file system (if changed), unloaded and re-loaded later; other data must be written to swap before it can be unloaded.

The swappiness sysctl parameter represents the kernel's preference for writing to swap instead of files. It can have a value between 0 and 200, and the default value is 60. A low value causes the kernel to prefer freeing up open files, a high value causes the kernel to try to use swap space, and a value of 100 means IO cost is assumed to be equal.

To check the current swappiness value:

 $ sysctl vm.swappiness

Alternatively, the file  can be read in order to obtain the raw integer value.

To temporarily set the swappiness value:

 # sysctl -w vm.swappiness=35

To set the swappiness value permanently, create a  configuration file. For example:

To have the boot loader set swappiness when loading the kernel, add a kernel parameter, e.g. .

Reasons for choosing a different swappiness can include:

* Lowering the swappiness has been suggested for desktop responsiveness. The argument is that because a lot of perceived performance (responsiveness) is determined by how fast a program responds to user input, anonymous pages (program memory) should be kept in RAM and freeing up open files should be prioritized even at some expense of actual performance.
** The minimal reasonable swappiness is 1 because a swappiness of 0 causes an extreme bias against anonymous page eviction, preventing them from being scanned for reclaiming or swapping except in the most extreme cases of memory contention. It is generally not desired to not reclaim truly unused anonymous pages.
* A higher swappiness of 100 or beyond is desired (by definition) when the IO cost of swapping is equal or lower than the cost of reading from a file. This can happen when the swap is not backed by the disk, especially in the case of zram. This can also happen when swap IO is being intercepted/cached by a lower-cost mechanism such as zswap.

## VFS cache pressure
Another sysctl parameter that affects swap performance is , which controls the tendency of the kernel to reclaim the memory which is used for caching of VFS caches, versus pagecache and swap. Increasing this value increases the rate at which VFS caches are reclaimed. For more information on what it does, see the Linux kernel documentation.

The default value is 100, which states that filesystem cache is about as important as the other caches, so they should be reclaimed at about an equal weight. On desktops it has been argued that filesystem cache is more important than the other caches because filesystem browsing times affects operation latency (perceived responsiveness) more than the other caches, resulting a suggested value of 50. On the other hand, a higher value has been suggested when the VFS cache holds metadata on many small files that are not touched again. For more information on tuning this parameter, see OpenSUSE tuning guide (which recommends experimenting and checking the types of caches via ).

## Priority
If you have more than one swap file or swap partition you should consider assigning a priority value (0 to 32767) for each swap area. The system will use swap areas of higher priority before using swap areas of lower priority. For example, if you have a faster disk and a slower disk, assign a higher priority to the swap area located on the fastest device. Priorities can be assigned in fstab via the  parameter:

 UUID=f9fe0b69-a280-415d-a03a-a32752370dee none swap defaults,pri=100 0 0
 UUID=d7eb6062-01c8-4367-ac1d-3bf1167de8bb none swap defaults,pri=10  0 0

Or via the  parameter of swapon:

 # swapon --priority 100 /dev/sda1

If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them.

## Striping
There is no necessity to use RAID for swap performance reasons. The kernel itself can stripe swapping on several devices, if you just give them the same priority in the  file. Refer to The Software-RAID HOWTO for details.

## Discard (a.k.a. trim)
See Solid state drive#swap.

## Compressed block device in RAM
See Improving performance#Swap on zram or zswap.

## Using the swap space only for hibernation
If you only need swap as a hibernation image storage space, then you can use zswap and disable its writeback so that there are no disk writes from regular swap usage. See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation.
