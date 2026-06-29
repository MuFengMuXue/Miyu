[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=NVMe&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.nvmexpress.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/NVM_Express "wikipedia:NVM Express")

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/nvme-cli)

[[]][GitWeb](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/tree/drivers/nvme)

[[]][Official documentation](http://www.nvmexpress.org/specifications/)

[NVM Express](https://en.wikipedia.org/wiki/NVM_Express "wikipedia:NVM Express") (**NVMe**) devices are flash memory chips connected to a system via the PCI-E bus (use four-lane max). They are among the fastest memory chips available on the market, faster than [Solid State Drives](https://wiki.gentoo.org/wiki/SSD "SSD") (SSD) connected over the SATA bus.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Identifying the device]](#Identifying_the_device)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [I/O testing]](#I.2FO_testing)
    -   [[3.2] [Performance and maintenance]](#Performance_and_maintenance)
    -   [[3.3] [Kernel I/O scheduler]](#Kernel_I.2FO_scheduler)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [[] Installation]

### [[] Kernel]

**NVM Express block device** (`CONFIG_BLK_DEV_NVME`) must be activated to gain NVMe device support:

[KERNEL]

    Device Drivers --->
      NVME Support --->
        <*> NVM Express block device Search for <code>CONFIG_BLK_DEV_NVME</code> to find this item.

Devices will show up under [/dev/nvme\*].

These are the defaults on other GNU/Linux distributions.

[KERNEL]

    <*> NVM Express block device
    [*] NVMe multipath support
    [*] NVMe hardware monitoring
    <M> NVM Express over Fabrics FC host driver
    <M> NVM Express over Fabrics TCP host driver
    <M> NVMe Target support
      [*]   NVMe Target Passthrough support
      <M>   NVMe loopback device support
      <M>   NVMe over Fabrics FC target driver
      < >     NVMe over Fabrics FC Transport Loopback Test driver (NEW)
      <M>   NVMe over Fabrics TCP target support

### [[] Emerge]

User space tools are available via:

`root `[`#`]`emerge --ask sys-apps/nvme-cli`

## [Configuration]

[Partition tables](https://wiki.gentoo.org/wiki/Partition "Partition") and formatting can be performed the same as any other block device.

### [[] Identifying the device]

There are minor differences in the naming scheme for devices and partitions when compared to SATA devices.

NVMe partitions generally show a **p** before the partition number. NVMe devices also include namespace support, using a **n** before listing the namespace. Therefore the first device in the first namespace with one partition will be at the following location: [/dev/nvme0n1p1]. The device name is nvme0, in namespace 1, and partition 1.

## [[] Usage]

### [][[] I/O testing]

[Hdparm](https://wiki.gentoo.org/wiki/Hdparm "Hdparm") can be used to get the raw read/write speed of a NVMe device. Passing the `-t` option instructs [hdparm] to perform timings of device reads, `-T` performs timings of cache reads, and `--direct` bypasses the page cache and causes reads to go directly from the drive into [hdparm]\'s buffers in raw mode:

`root `[`#`]`hdparm -tT --direct /dev/nvme0n1`

### [[] Performance and maintenance]

Since NVMe devices share the flash memory technology basis with common SSDs, the same performance and longevity considerations apply. For details consult the [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") article.

### [][[] Kernel I/O scheduler]

Thanks to very fast random access times provided by NVMe devices, it is recommended to use the simplest kernel I/O scheduling strategy available^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^. Recent kernels name this strategy as *none*.

** Note**\
Performance impact of the I/O scheduler can vary among different workloads. Always benchmark your particular workload in order to achieve the optimal performance.

Name of the currently used I/O scheduler can be obtained from [sysfs](https://wiki.gentoo.org/wiki/Sysfs "Sysfs"). For example, a [/dev/nvme0n1] device using the *none* scheduler would look as:

`user `[`$`]`cat /sys/block/nvme0n1/queue/scheduler`

    none

In case of having multiple I/O schedulers available in the kernel:

`user `[`$`]`cat /sys/block/nvme0n1/queue/scheduler`

    [none] mq-deadline kyber bfq

It is possible to change the scheduler by writing name of the desired scheduler to the sysfs file:

`root `[`#`]`echo "none" > /sys/block/nvme0n1/queue/scheduler`

This can also be achieved automatically by [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rules:

[FILE] **`/etc/udev/rules.d/60-ioschedulers.rules`NVMe I/O scheduler rules file**

    # Set scheduler for NVMe devices
    ACTION=="add|change", KERNEL=="nvme[0-9]n[0-9]", ATTR="none"

## [[] See also]

-   [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") --- provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux.

## [External resources]

-   [https://metebalci.com/blog/a-quick-tour-of-nvm-express-nvme](https://metebalci.com/blog/a-quick-tour-of-nvm-express-nvme) - An excellent article describing the differences in recent disk drive technology, but focusing on NVMe.
-   [https://wiki.archlinux.org/index.php/NVMe](https://wiki.archlinux.org/index.php/NVMe)
-   [Switching Scheduler --- The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/block/switching-sched.html)
-   [BFQ, Multiqueue-Deadline, or Kyber? Performance Characterization of Linux Storage Schedulers in the NVMe Era](https://atlarge-research.com/pdfs/2024-io-schedulers.pdf)
-   [A Systematic Configuration Space Exploration of the Linux Kyber I/O Scheduler](https://atlarge-research.com/pdfs/hotcloudperf24-kyber.pdf)

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Kernel/Reference/IOSchedulers - Ubuntu Wiki](https://wiki.ubuntu.com/Kernel/Reference/IOSchedulers), Ubuntu Wiki. Retrieved on June 6, 2021]]
2.  [[[↑](#cite_ref-2)] [[Linux 5.6 I/O Scheduler Benchmarks: None, Kyber, BFQ, MQ-Deadline](https://www.phoronix.com/scan.php?page=article&item=linux-56-nvme&num=1), Phoronix. Retrieved on June 6, 2021 ]]