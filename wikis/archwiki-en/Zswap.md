# Zswap

zswap is a kernel feature that provides a compressed RAM cache for swap pages. Pages which would otherwise be swapped out to disk are instead compressed and stored into a memory pool in RAM. Once the pool is full or the RAM is exhausted, the least recently used (LRU) page is decompressed and written to disk, as if it had not been intercepted. After the page has been decompressed into the swap cache, the compressed version in the pool can be freed.

The difference compared to zram is that zswap works in conjunction with a swap device while zram with swap created on top of it is a swap device in RAM that does not require a backing swap device.

## Toggling zswap
zswap can be toggled at runtime, by writing either  (to enable) or  (to disable) to . For example, to disable it at runtime:

 # echo 0 > /sys/module/zswap/parameters/enabled

To disable zswap permanently on kernels where it is enabled by default, add  to your kernel parameters.

## Customizing zswap
## Current parameters
zswap has several customizable parameters. The live settings can be displayed using:

See the zswap documentation for the description of the different parameters.

The boot time load message showing the initial configuration can be retrieved with:

## Set parameters
## Using sysfs
Each setting can be changed at runtime via the sysfs interface. For example, to change the  parameter:

 # echo lz4 > /sys/module/zswap/parameters/compressor

## Using kernel boot parameters
To persist the parameter change, the corresponding option, for example , must be added to the kernel boot parameter. Therefore to set permanently all the above settings, the following kernel parameters must be added:

 zswap.enabled=1 zswap.shrinker_enabled=1 zswap.compressor=lz4 zswap.max_pool_percent=30

When changing the compression algorithm via a boot parameter, ensure the corresponding compression module is loaded early during boot (refer to #Compression algorithm).

## Maximum pool size
The memory pool is not preallocated, it is allowed to grow up to a certain limit in percentage of the total memory available, by default up to 20% of the total RAM. Once this threshold is reached, pages are evicted from the pool into the swap device. The maximum compressed pool size is controlled with the parameter .

## Shrinker
The shrinker, when enabled, causes zswap to shrink the pool by evicting cold pages to swap when memory pressure is high. This reduces the amount of cold data in the pool and, in the author's synthetic benchmark, helps avoid wasting CPU time on compressing and decompressing cold pages. It can be turned on with the parameter .

## Compression algorithm
For page compression, zswap uses compressor modules provided by the kernel's cryptographic API. In official kernels the zstd compression algorithm is used by default but this can be changed with  at boot time. Other options include deflate, lzo, 842, lz4 and lz4hc.

There is no issue changing the compression at runtime using sysfs but zswap starts in this case with zstd and switches at a later stage to the defined algorithm. To start zswap with another algorithm straight away, this must be set via the kernel boot parameters and the corresponding module must be loaded early by the kernel. This can be achieved by following these steps:

# Add the modules required for the chosen compressor to the mkinitcpio#MODULES array.
# Regenerate the initramfs.
# Set the compression algorithm using the  kernel parameter.

On next boot, see #Current parameters to check if zswap now uses the requested compressor.

## Disable writeback
zswap has a per-cgroup option to disable writeback (i.e. to prevent writes to disk).

See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation for an example use case.

## Zswap statistics
To see zswap statistics you can run this:
