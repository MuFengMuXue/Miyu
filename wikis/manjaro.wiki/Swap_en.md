[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Swap&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Swap/de "Auslagerungsspeicher (Swap) (38% translated)") • ‎[English](//wiki.manjaro.org/index.php?title=Swap "Swap (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Swap/fr "Swap (94% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Swap/ru "Swap (100% translated)")

\

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Do I Need Swap]](#Do_I_Need_Swap)
-   [[3] [How Much Swap do I Need]](#How_Much_Swap_do_I_Need)
-   [[4] [Displaying Swap Information]](#Displaying_Swap_Information)
-   [[5] [Using a Swap Partition]](#Using_a_Swap_Partition)
    -   [[5.1] [Creating and Enabling a Swap Partition]](#Creating_and_Enabling_a_Swap_Partition)
-   [[6] [Using a Swapfile]](#Using_a_Swapfile)
    -   [[6.1] [Creating and Enabling a Static Swapfile]](#Creating_and_Enabling_a_Static_Swapfile)
    -   [[6.2] [Swapfiles on BTRFS]](#Swapfiles_on_BTRFS)
    -   [[6.3] [Swapfiles on ZFS]](#Swapfiles_on_ZFS)
-   [[7] [Tuning & Performance Considerations]](#Tuning_.26_Performance_Considerations)
-   [[8] [See Also]](#See_Also)

# [Overview]

Swap space is used to extend the amount of memory(RAM) available for running programs.

-   Without swap space, if you run out of memory, applications *will* be terminated up to and including the entire system crashing.
-   With swap space available to the system, the kernel can take less frequently accessed memory pages from inactive applications / services and write them to disk (\"swapping\" them), allowing more actual RAM to be available for active applications.

\
There are three different ways in which swap can be managed in Manjaro:

-   A swap partition
-   A swap file
-   zswap

\
This article tries to be as comprehensive as possible but even more information can be found in the [articles linked below](//wiki.manjaro.org/index.php?title=Swap#See_Also "Swap")

# [Do I Need Swap]

That is a question that cannot be answered without having a look at your configuration and even with plenty of available memory, it is often used as a safety net or even sometimes due to specific application requirements so have a look at the following non-exhaustive list:

-   If you use hibernation: *yes, you need swap!*
-   If you have services that are not always active, but are still running all the time: *yes, you need swap!*
-   If you have an application that allocates virtual memory directly for temporary storage instead of RAM: *yes, you need swap!*
-   If you have an application that has a memory leak: *yes, you need swap!*
-   If you have a server with 1TB of RAM that you\'re using as a desktop without applications allocating virtual memory or having memory leaks: *No, you don\'t need swap!*

# [How Much Swap do I Need]

The amount of swap you need is highly variable based on *your* specific applications and workload. There is no universal formula on swap size without monitoring usage over a period of time. A reasonable place to start would be:

-   For less than 4GB of physical memory (RAM), it\'s highly recommended that the swap space should, as a base minimum, be equal to the amount of RAM. Also, it\'s recommended that the swap space is maximum twice the amount of RAM depending upon the amount of disk space available for the system because of diminishing returns.
-   For more modern systems (\>4GB), your swap space should be at a minimum be ROUNDUP(SQRT(RAM)) I.E. the square root of your RAM size rounded up to the next GB. **However, if you use hibernation**, you need a minimum of physical memory (RAM) size **plus** ROUNDUP(SQRT(RAM)). The maximum, is again twice the amount of RAM, again because of diminishing returns.
-   The only downside to having more swap space than you will actually use, is the disk space you will be reserving for it cannot be used for application or system data.

The \"diminishing returns\" means that if you need more swap space than twice your RAM size, you would be better off adding more RAM as Hard Disk Drive (HDD) access is about 10³ slower than RAM access, so something that would take 1 second, suddenly takes more than 15 minutes! And on a Solid State Drive (SSD) the same operation that took 1 second in RAM will still take about 1 minute on that SSD!

Taking into account all of the above, this brings us to the following table: (last 3 columns denote swap space)

           RAM   No hibernation    With Hibernation  Maximum
           1GB              1GB                 2GB      2GB
           2GB              2GB                 3GB      4GB
           3GB              3GB                 5GB      6GB
           4GB              4GB                 6GB      8GB

           RAM   No hibernation    With Hibernation  Maximum
           5GB              2GB                 7GB     10GB
           6GB              2GB                 8GB     12GB
           8GB              3GB                11GB     16GB
          12GB              3GB                15GB     24GB
          16GB              4GB                20GB     32GB
          24GB              5GB                29GB     48GB
          32GB              6GB                38GB     64GB
          64GB              8GB                72GB    128GB
         128GB             11GB               139GB    256GB
         256GB             16GB               272GB    512GB
         512GB             23GB               535GB      1TB
           1TB             32GB              1056GB      2TB
           2TB             46GB              2094GB      4TB
           4TB             64GB              4160GB      8TB
           8TB             91GB              8283GB     16TB

**Note**

------------------------------------------------------------------------

The largest server one of the authors of this wiki article has ever installed had, indeed, 8TB of RAM and even that machine has the above swap settings, so why not your machine?

# [Displaying Swap Information]

The command `swapon` will display your current swap information. For example:

    swapon
    NAME      TYPE      SIZE   USED PRIO
    /dev/sda7 partition  20G  44.3M   -2

The following script will:

-   show whether zswap is active or not and if active, give zswap parameters if run with the `sudo` command
-   display a list of all applications / services that take up swap and how much they take up in descending order

<!-- -->

    #!/bin/bash
    #Check whether running as root
    if [ "$(whoami)" = 'root' ]; then
      dmesg | grep "zswap:" | grep --silent "load"
      if [ $? -eq 0 ]; then
        # zswap is active
        echo "zswap information:"
        grep --recursive --color=none . /sys/kernel/debug/zswap/
        read -n 1 -s -r -p "Press any key to continue"
      else
        echo "[warning] zswap not active. Continuing"
      fi
    else
      echo "[warning] Not running as root: skipping zswap info"
    fi
    for szFile in /proc/*/status ; do
      awk '/VmSwap|Name/END' "$szFile"
    done | sort --key 2 --numeric --reverse | more

# [Using a Swap Partition]

A swap partition is the traditional way of managing swap. In this scenario, a dedicated partition (or partitions) are created for holding swap.

## [Creating and Enabling a Swap Partition]

To create a swap partition, you need enough unallocated disk space to create an additional partition. If you do not have enough space, skip to the next section [#Using_a_Swapfile](#Using_a_Swapfile). A swap partition can be created in any disk management / partition management tool and should be set as type `linuxswap`.

Once you have a swap partition you will need to initialize the swap partition with `mkswap`. For example, if your swap partition is `/dev/sda3`, you could use the command:

    sudo mkswap /dev/sda3

Next we need to enable the swap partition with the `swapon` command. Following our example above this could be done with:

    sudo swapon /dev/sda3

In order to ensure that the swap is enabled at boot we can add an entry to `/etc/fstab`. It is best to use the UUID instead of the device name for this purpose. You can add the line to fstab manually or using the command:

    sudo bash -c "echo UUID=$(lsblk -no UUID /dev/sda3) none swap defaults 0 0 >> /etc/fstab"

If you would like to have more than one swap partition, simply repeat the steps above for any additional partitions.

\

**Note**

------------------------------------------------------------------------

Be sure to replace /dev/sda3 in the above commands with your actual swap partition.

\

**Tip**

------------------------------------------------------------------------

*If you\'re using a HDD* (spinning rust) put the swap partition \*at the beginning of the disk\* as the speed of the disk is higher on the outside tracks. On an SSD this doesn\'t matter.

# [Using a Swapfile]

Using a swap partition has one major disadvantage: Changing the size of swap or adding swap requires repartitioning the disk. In current Linux kernels, it is possible to use a swap file instead of a dedicated partition and as from kernel 2.6 onwards there is no performance difference any more between the two.

## [Creating and Enabling a Static Swapfile]

**Tip**

------------------------------------------------------------------------

There is no reason you can\'t have both a swap partition and a swapfile. This is an easy way to add more swap without repartitioning.

\
First create and intialize the file to hold the swap. For example, to create a 4GB swapfile, you could use the command:

    sudo dd if=/dev/zero of=/swapfile bs=1M count=4096 status=progress

\
Set the appropriate permissions on the file. It should be readable and writable only by `root`. This can be done with the command:

    sudo chmod 600 /swapfile

\
Next we need to format and enable the swapfile:

    sudo mkswap /swapfile

    sudo swapon /swapfile

\
In order to ensure that the swap is enabled at boot we can add an entry to `/etc/fstab`. You can add the line to fstab manually or using the command:

    sudo bash -c "echo /swapfile none swap defaults 0 0 >> /etc/fstab"

\

## [Swapfiles on BTRFS]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                      | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                  |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                      |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** Please see official btrfs documentaion ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Swap/en&action=edit&redlink=1 "Talk:Swap/en (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                              |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[Official btrfs documentation on swapfile](https://btrfs.readthedocs.io/en/latest/Swapfile.html)

As of kernel 5.0 and higher, swapfiles are supported on btfrs. They still require some special handling in addition to the above steps.

Prior to running the `dd` step above, you should run these commands:

    sudo truncate -s 0 /swapfile
    sudo chattr +C /swapfile
    sudo btrfs property set /swapfile compression none

\
These commands create an empty swapfile, disable COW for that file and ensure that compression is disabled.

\

\

**Tip**

------------------------------------------------------------------------

To stay compatible with Timeshift, it is necessary to create the swapfile outside the root subvolume \"@\".

[root \# ][ btrfs subvolume create /@swapfile [COPY TO CLIPBOARD]]

\

Just replace /swapfile with /@swapfile/swapfile.

\

## [Swapfiles on ZFS]

zfs doesn\'t support swapfiles, however you can achieve a similar benefit using a zvol as a swap volume.

\
Detailed instructions on how to accomplish this can be found in this [ZoL guide](https://github.com/zfsonlinux/pkg-zfs/wiki/HOWTO-use-a-zvol-as-a-swap-device).

# [][Tuning & Performance Considerations]

Although swap seems like a great way to expand memory, excessive swap use will cause severe performance degradation, as mentioned before.

There are couple of parameters that can be used to tune swap utilization. These are swappiness and vfs_cache_pressure. To see your current settings for these you can use the following commands:

    cat /proc/sys/vm/swappiness
    cat /proc/sys/vm/vfs_cache_pressure

`swappiness` controls how likely a page is to be transferred to swap. This value represents the percentage of the free memory before activating swap. The lower the value, the less swapping is used and the more memory pages are kept in physical memory where:

-   0 disables swap
-   60 is the default value which is ideal for a server that is memory-starved and running a lot of services
-   100 is very aggressive swapping.

For *most* desktop computers the recommended value is 10: Theoretically, this means to only start swapping when RAM usage reaches around 90 percent.

`vfs_cache_pressure` used to be a percentage value that controls the tendency of the kernel to *reclaim* the memory which is used for caching of directory and inode objects with a default value of 100 on Kernels \<5.4. On Kernels \>=5.4 can be increased beyond 100. Increasing this value will increase the rate in which these objects are removed from the RAM cache. Decreasing it will allow these objects to be cached in memory longer, consuming additional RAM over time. Depending on your specific workload, increasing or decreasing this value too far can have significant negative impacts on system performance. Experimentation is needed to find the appropriate balance and the default value is reasonable. In general, it is more common to optimize swappiness before experimenting with vfs_cache_pressure.

To set these values you can use the command `sysctl`. For example, to set the swappiness value to 10 you could use:

    sudo sysctl vm.swappiness=10

\
**There is no preset defined answer on the optimal values for these parameters.** Experimentation is needed to find the optimum configuration for your specific hardware and workload.

\

# [See Also]

-   The Arch Wiki page on [swap](https://wiki.archlinux.org/index.php/Swap)
-   The Arch Wiki page on [zswap](https://wiki.archlinux.org/index.php/Zswap)
-   The Linux kernel documentation on [zswap](https://www.kernel.org/doc/Documentation/vm/zswap.txt)
-   The Linux kernel documentation on [swappiness and vfs_cache_pressure](https://www.kernel.org/doc/Documentation/sysctl/vm.txt)
-   The ZFS on Linux guide on [Swap Volumes](https://github.com/zfsonlinux/pkg-zfs/wiki/HOWTO-use-a-zvol-as-a-swap-device)