# Zram

zram, formerly called compcache, is a Linux kernel module for creating a compressed block device in RAM, i.e. a RAM disk with on-the-fly disk compression. The block device created with zram can then be used for swap or as a general-purpose RAM disk. The two most common uses for zram are for the storage of temporary files () and as a swap device. Initially, zram had only the latter function, hence the original name "compcache" ("compressed cache").

## Usage as swap
Initially the created zram block device does not reserve or use any RAM. Only as files need or want to be swapped out, they will be compressed and moved into the zram block device. The zram block device will then dynamically grow or shrink as required.

Even when assuming that zstd only achieves a conservative 1:2 compression ratio (real world data shows a common ratio of 1:3), zram will offer the advantage of being able to store more content in RAM than without memory compression.

A simple size to start with is half of the total system memory.

## Manually
To set up one zstd compressed zram device with half the system memory capacity and a higher-than-normal priority (only for the current session):

 # modprobe zram
 # zramctl /dev/zram0 --algorithm zstd --size "$(($(grep -Po 'MemTotal:\s*\K\d+' /proc/meminfo)/2))KiB"
 # mkswap -U clear /dev/zram0
 # swapon --discard --priority 100 /dev/zram0

To disable it again, either reboot or run:

 # swapoff /dev/zram0
 # modprobe -r zram

A detailed explanation of all steps, options and potential problems is provided in the official documentation of the zram module.

For a permanent solution, use a method from one of the following sections.

## Using a udev rule
The example below describes how to set up swap on zram automatically at boot with a single udev rule and an fstab entry. No additional packages are needed to make this work.

Explicitly load the module at boot:

Create the following udev rule adjusting the  attribute as necessary:

{{hc|/etc/udev/rules.d/99-zram.rules|2=
ACTION=="add", KERNEL=="zram0", ATTR{initstate}=="0", ATTR{comp_algorithm}="zstd", ATTR{disksize}="4G", TAG+="systemd"
}}

Add  to your fstab with a higher than default priority and the  option:

## Using zram-generator
 is a systemd-related project hosted under its GitHub organization that makes use of its conventions and mechanisms.

It provides  units to automatically initialize zram devices without users needing to enable/start the template or its instances. See .

To use it, install , and create  with the following:

This is sufficient to get a zram device called  created with the default options (see  for their current values).

By default the zram device will use half the RAM size but no more than 4 GiB: e.g. it will create a 2 GiB zram device if you have 4 GiB of RAM, but only a 4 GiB zram device if you have 8 GiB of memory or more.

If you wish to change this, use the
 parameter:

This will allow the zram device to use half the total amount of memory up to 16 GiB ( compares the two values and picks the smallest).

* if you want to unconditionally allow the zram device to use half the memory, use
* for a fixed size, use e.g. .

See  for graphs and a more complex example.

To use a different compression algorithm than the kernel's current default, use
:

Subsequent algorithms are used for recompression.

See  for a list of all available options.

Once a configuration has been defined, run daemon-reload and start your configured  instance ( matching the numerical instance-ID, in the example it is ).

You can check the swap status of your configured  device(s) by reading the unit status of your  instance(s), by using , or by using .

## Using zramswap
 provides an automated script for setting up a swap with a higher priority and a default size of 20% of the RAM size of your system. To do this automatically on every boot, enable .

## Tips and tricks
## Checking zram statistics
Use . Example:

* DISKSIZE = 32G: this zram device will store up to 32 GiB of uncompressed data.
* DATA = 1.9G: currently, 1.9 GiB (uncompressed) of data is being stored in this zram device
* COMPR = 318.6M: the 1.9 GiB uncompressed data was compressed to 318.6 MiB
* TOTAL = 424.9M: including metadata, the 1.9 GiB of uncompressed data is using up 424.9 MiB of physical RAM

## Compression algorithm
Use  after creating the zram device N to get the available compression algorithms, as well as the currently selected one (included in brackets).

Results with  6.17.9.arch1-1 using default options:
 lzo-rle lzo lz4 lz4hc deflate 842

## Multiple zram devices
By default, loading the  module creates a single  device.

If you need more than one  device, specify the amount using the  kernel module parameter or [https://docs.kernel.org/admin-guide/blockdev/zram.html#add-remove-zram-devices add them as needed afterwards.

## Optimizing swap on zram
Since zram behaves differently than disk swap, we can configure the system's swap to take full potential of the zram advantages:

Explanation of the configuration:

These values are what Pop!_OS uses. That Pop!_OS GitHub pull request also links to some testing done by users on r/Fedora, which determined that  is ideal. They also found a high swappiness value to be ideal, which matches what is suggested by the kernel docs:

:The default value is 60.
:For in-memory swap, like zram or zswap, as well as hybrid setups that have swap on faster devices than the filesystem, values beyond 100 can be considered. For example, if the random IO against the swap device is on average 2x faster than IO from the filesystem, swappiness should be 133 (x + 2x = 200, 2x = 133.33).

On a system with a hard drive, random I/O against the in-memory device would be orders of magnitude faster than I/O against the filesystem, so swappiness should be ~200. Even on a system with a fast SSD, a high swappiness value may be ideal.

## Enabling a backing device for a zram block
zram can be configured to push incompressible pages to a specified block device:

To add a backing device manually:

 # echo /dev/sdX > /sys/block/zram0/backing_dev

To add a backing device to your zram block device using zram-generator, update  with the following under your  device you want the backing device added to:

Incompressible pages can then be pushed to the block device by executing:

 # echo huge > /sys/block/zramX/writeback

## Using zram for non-swap purposes
zram can also be used as a generic RAM-backed block device, e.g. a  with less physical memory usage, but slightly lower performance. However there are some caveats:

* There is no partition table support (no automatic creation of ).
* The block size is fixed to 4 kiB.

The obvious way around this is to stack a loop device on-top the zram, using losetup, specifying the desired block size using the  option and the  option to process partition tables and automatic creation of the partition loop devices.

Copy the disk image to the new , then create a loop device. If the disk image has a partition table, the block size of the loop device must match the block size used by the partition table, which is typically 512 or 4096 bytes.

 # losetup -f -b 512 -P /dev/zramx

 # mount /dev/loop0p1 /mnt/boot
 # mount /dev/loop0p2 /mnt/root
