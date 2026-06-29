# Improving performance

This article provides information on basic system diagnostics relating to performance as well as steps that may be taken to reduce resource consumption or to otherwise optimize the system with the end-goal being either perceived or documented improvements to a system's performance. See also Gaming#Improving performance for additional gaming and low latency specific advice.

## The basics
## Know your system
The best way to tune a system is to target bottlenecks, or subsystems which limit overall speed. The system specifications can help identify them.

* If the computer becomes slow when large applications (such as LibreOffice and Firefox) run at the same time, check if the amount of RAM is sufficient. Use the following command, and check the "available" column:
* If boot time is slow, and applications take a long time to load at first launch (only), then the hard drive is likely to blame. The speed of a hard drive can be measured with the  command:
* If CPU load is consistently high even with enough RAM available, then try to lower CPU usage by disabling running daemons and/or processes. This can be monitored in several ways, for example with ,  or any other system monitoring tool:
* If applications using direct rendering are slow (i.e those which use the GPU, such as video players, games, or even a window manager), then improving GPU performance should help. The first step is to verify if direct rendering is actually enabled. This is indicated by the  command, part of the  package, which should return  when used:
* When running a desktop environment, disabling (unused) visual desktop effects may reduce GPU usage. Use a more lightweight environment or create a custom environment if the current does not meet the hardware and/or personal requirements.
* Using an optimized kernel improves performance. Generally,  is a good option. However, the default kernel can be tweaked as shown in certain parts of this article to perform better.

## Benchmarking
The effects of optimization are often difficult to judge. They can however be measured by benchmarking tools.

## Storage devices
## Sector size
Check that your NVMe drives and Advanced Format hard disk drives are using the optimal logical sector size.

## Partitioning
Make sure that your partitions are properly aligned.

## Multiple drives
If you have multiple disks available, you can set them up as a software RAID for serious speed improvements.

Creating swap on a separate disk can also help quite a bit, especially if your machine swaps frequently.

## An SSD as a cache for an HDD
When forgoing hard disk drives is not an option, a solid state drive can be added as a caching layer to improve the read and/or write speeds and reduce the noise from random access. The options to accomplish this include LVM#Cache, Bcache and Bcachefs#SSD caching.

## Layout on HDDs
If using a traditional spinning HDD, your partition layout can influence the system's performance. Sectors at the beginning of the drive (closer to the outside of the disk) are faster than those at the end. Also, a smaller partition requires less movements from the drive's head, and so speed up disk operations. Therefore, it is advised to create a small partition (15-20GiB, more or less depending on your needs) only for your system, as near to the beginning of the drive as possible. Other data (pictures, videos) should be kept on a separate partition, and this is usually achieved by separating the home directory () from the system ().

## Choosing and tuning your filesystem
Choosing the best filesystem for a specific system is very important because each has its own strengths. The File systems article provides a short summary of the most popular ones. You can also find relevant articles in File systems.

## Mount options
The various *atime options can mitigate the performance penalty of .

Other mount options are filesystem specific, therefore see the relevant articles for the filesystems:

* Ext3
* Ext4#Improving performance
* JFS#Optimizations
* XFS#Performance
* Btrfs#Defragmentation, Btrfs#Compression, and
* ZFS#Tuning
* NTFS#Improving performance

## Tuning kernel parameters
There are several key tunables affecting the performance of block devices, see sysctl#Virtual memory for more information.

## Input/output schedulers
## Background information
The input/output (I/O) scheduler is the kernel component that decides in which order the block I/O operations are submitted to storage devices. It is useful to remind here some specifications of two main drive types because the goal of the I/O scheduler is to optimize the way these are able to deal with read requests:

* An HDD has spinning disks and a head that moves physically to the required location. Therefore, random latency is quite high ranging between 3 and 12ms (whether it is a high end server drive or a laptop drive and bypassing the disk controller write buffer) while sequential access provides much higher throughput. The typical HDD throughput is about 200 I/O operations per second (IOPS).

* An SSD does not have moving parts, random access is as fast as sequential one, typically under 0.1ms, and it can handle multiple concurrent requests. The typical SSD throughput is greater than 10,000 IOPS, which is more than needed in common workload situations.

If there are many processes making I/O requests to different storage parts, thousands of IOPS can be generated while a typical HDD can handle only about 200 IOPS. There is a queue of requests that have to wait for access to the storage. This is where the I/O schedulers plays an optimization role.

## The scheduling algorithms
One way to improve throughput is to linearize access: by ordering waiting requests by their logical address and grouping the closest ones. Historically this was the first Linux I/O scheduler called elevator.

One issue with the elevator algorithm is that it is not optimal for a process doing sequential access: reading a block of data, processing it for several microseconds then reading next block and so on. The elevator scheduler does not know that the process is about to read another block nearby and, thus, moves to another request by another process at some other location. The anticipatory I/O scheduler overcomes the problem: it pauses for a few milliseconds in anticipation of another close-by read operation before dealing with another request.

While these schedulers try to improve total throughput, they might leave some unlucky requests waiting for a very long time. As an example, imagine the majority of processes make requests at the beginning of the storage space while an unlucky process makes a request at the other end of storage. This potentially infinite postponement of the process is called starvation. To improve fairness, the deadline algorithm was developed. It has a queue ordered by address, similar to the elevator, but if some request sits in this queue for too long then it moves to an "expired" queue ordered by expire time. The scheduler checks the expire queue first and processes requests from there and only then moves to the elevator queue. Note that this fairness has a negative impact on overall throughput.

The Completely Fair Queuing (CFQ) approaches the problem differently by allocating a timeslice and a number of allowed requests by queue depending on the priority of the process submitting them. It supports cgroup that allows to reserve some amount of I/O to a specific collection of processes. It is in particular useful for shared and cloud hosting: users who paid for some IOPS want to get their share whenever needed. Also, it idles at the end of synchronous I/O waiting for other nearby operations, taking over this feature from the anticipatory scheduler and bringing some enhancements. Both the anticipatory and the elevator schedulers were decommissioned from the Linux kernel replaced by the more advanced alternatives presented below.

The Budget Fair Queuing (BFQ) is based on CFQ code and brings some enhancements. It does not grant the disk to each process for a fixed time-slice but assigns a "budget" measured in number of sectors to the process and uses heuristics. It is a relatively complex scheduler, it may be more adapted to rotational drives and slow SSDs because its high per-operation overhead, especially if associated with a slow CPU, can slow down fast devices. The objective of BFQ on personal systems is that for interactive tasks, the storage device is virtually as responsive as if it was idle. In its default configuration it focuses on delivering the lowest latency rather than achieving the maximum throughput, which can sometimes greatly accelerate the startup of applications on hard drives.

Kyber is a recent scheduler inspired by active queue management techniques used for network routing. The implementation is based on "tokens" that serve as a mechanism for limiting requests. A queuing token is required to allocate a request, this is used to prevent starvation of requests. A dispatch token is also needed and limits the operations of a certain priority on a given device. Finally, a target read latency is defined and the scheduler tunes itself to reach this latency goal. The implementation of the algorithm is relatively simple and it is deemed efficient for fast devices.

## Kernel's I/O schedulers
While some of the early algorithms have now been decommissioned, the official Linux kernel supports a number of I/O schedulers. The Multi-Queue Block I/O Queuing Mechanism (blk-mq) maps I/O queries to multiple queues, the tasks are distributed across threads and therefore CPU cores. Within this framework the following schedulers are available:

* None, where no queuing algorithm is applied.
* mq-deadline, the adaptation of the deadline scheduler (see below) to multi-threading.
* Kyber
* BFQ

## Changing I/O scheduler
To list the available schedulers for a device and the active scheduler (in brackets):

To list the available schedulers for all devices:

To change the active I/O scheduler to bfq for device sda, use:

 # echo ''bfq > /sys/block/sda''/queue/scheduler

The process to change I/O scheduler, depending on whether the disk is rotating or not can be automated and persist across reboots. For example the udev rules below set the scheduler to bfq for rotational drives, bfq for SSD/eMMC drives and none for NVMe drives:

{{hc|/etc/udev/rules.d/60-ioschedulers.rules|
# HDD
ACTION=="add|change", KERNEL=="sdATTR{queue/rotational}=="1", ATTR{queue/scheduler}="bfq"

# SSD
ACTION=="add|change", KERNEL=="sd[a-z*|mmcblkATTR{queue/rotational}=="0", ATTR{queue/scheduler}="bfq"

# NVMe SSD
ACTION=="add|change", KERNEL=="nvme[0-9*", ENV{DEVTYPE}=="disk", ATTR{queue/scheduler}="none"
}}

Reboot or force udev#Loading new rules.

## Tuning I/O scheduler
Each of the kernel's I/O scheduler has its own tunables, such as the latency time, the expiry time or the FIFO parameters. They are helpful in adjusting the algorithm to a particular combination of device and workload. This is typically to achieve a higher throughput or a lower latency for a given utilization.
The tunables and their description can be found within the kernel documentation.

To list the available tunables for a device, in the example below sdb which is using deadline, use:

To improve deadlines throughput at the cost of latency, one can increase  with the command:

## Power management configuration and write cache
When dealing with traditional rotational disks (HDDs) you may want to completely disable or lower power saving features, and check if the write cache is enabled.

See Hdparm#Power management configuration and Hdparm#Write cache.

Afterwards, you can make a udev rule to apply them on boot-up.

## Reduce disk reads/writes
Avoiding unnecessary access to slow storage drives is good for performance and also increasing lifetime of the devices, although on modern hardware the difference in life expectancy is usually negligible.

## Show disk writes
The  package can sort by disk writes, and show how much and how frequently programs are writing to the disk. See  for details.

## Relocate files to tmpfs
Relocate files, such as your browser profile, to a tmpfs file system, for improvements in application response as all the files are now stored in RAM:

* Refer to Profile-sync-daemon for syncing browser profiles. Certain browsers might need special attention, see e.g. Firefox on RAM.
* Refer to Anything-sync-daemon for syncing any specified folder.
* Refer to Makepkg#Improving build times for improving compile times by building packages in tmpfs.

## File systems
Refer to corresponding file system page in case there were performance improvements instructions, see the list at #Choosing and tuning your filesystem.

## Swap space
See Swap#Performance for details.

## Writeback interval and buffer size
See Sysctl#Virtual memory for details.

## Disable core dumps
See Core dump#Disabling automatic core dumps.

## Storage I/O scheduling with ionice
Many tasks such as backups do not rely on a short storage I/O delay or high storage I/O bandwidth to fulfill their task, they can be classified as background tasks. On the other hand quick I/O is necessary for good UI responsiveness on the desktop. Therefore it is beneficial to reduce the amount of storage bandwidth available to background tasks, whilst other tasks are in need of storage I/O. This can be achieved by making use of the Linux I/O scheduler BFQ, which allows setting different priorities for processes.

The I/O priority of a background process can be reduced to the "Idle" level by starting it with

 $ ionice -c 3 command

See a short introduction to ionice and  for more information.

## Trimming
For optimal performance, empty blocks of solid state drives should be discarded (a.k.a. trimmed) periodically to optimize random write speeds. See Solid state drive#TRIM for more information.

## Network
## General information
* Kernel networking: see Sysctl#Improving performance
* NIC: see Network configuration#Set device MTU and queue length
* DNS: consider using a caching DNS resolver, see Domain name resolution#DNS servers
* Samba: see Samba#Improve throughput

## Regulatory domain
Different countries have different standards for wireless network services, and you will typically be able to achieve a stronger signal by setting the correct domain for your network configuration. This will typically be configured during setup, but in some cases the settings will not be applied correctly. Check the contents of ; if the value is  (a global setting that is generally more restrictive) or set to the incorrect region, try adding the following kernel parameter, replacing  with the correct country code (e.g.,  for the United States):

 cfg80211.ieee80211_regdom=XX

Then reboot your system.

## Power management
Certain devices have issues whereby their network adapters will incorrectly entering power saving mode while still in use, throttling performance or causing disconnections. If this happens to you, ensure that you upgrade your packages to the latest version to receive any necessary firmware updates, and see Power management#Network interfaces.

## CPU
## Overclocking
Overclocking improves the computational performance of the CPU by increasing its peak clock frequency. The ability to overclock depends on the combination of CPU model and motherboard model. It is most frequently done through the BIOS. Overclocking also has disadvantages and risks. It is neither recommended nor discouraged here.

Many Intel chips will not correctly report their clock frequency to acpi_cpufreq and most other utilities. This will result in excessive messages in dmesg, which can be avoided by unloading and blacklisting the kernel module .
To read their clock speed use i7z from the  package. To check for correct operation of an overclocked CPU, it is recommended to do stress testing.

## Frequency scaling
See CPU frequency scaling.

## CPU scheduler
The default CPU scheduler in the mainline Linux kernel is EEVDF.

*
*
*

## Real-time kernel
Some applications such as running a TV tuner card at full HD resolution (1080p) may benefit from using a realtime kernel.

## Adjusting priorities of processes
See also  and .

## Ananicy
Ananicy CPP is a daemon, available as  or , for auto adjusting the nice levels of executables. The nice level represents the priority of the executable when allocating CPU resources.

## cgroups
See cgroups.

## LimitCPU
LimitCPU is a program to limit the CPU usage percentage of a specific process. After installing , you may limit the CPU usage of a process's PID using a scale of 0 to 100 times the number of CPU cores that the computer has. For example, with eight CPU cores the percentage range will be 0 to 800. Usage:

 $ limitcpu -l 50 -p 5081

## irqbalance
The purpose of  is to distribute hardware interrupts across processors on a multiprocessor system in order to increase performance. It can be controlled by the provided .

## Turn off CPU exploit mitigations
Turning off CPU exploit mitigations may improve performance. Use below kernel parameter to disable them all:

 mitigations=off

The explanations of all the switches it toggles are given at kernel.org. You can use  or  (from ) for vulnerability check.

## Tuning compilation for your CPU
Depending on your CPU, you may be able to gain a small performance boost by compiling software tuned for your native CPU microarchitecture with the flag , but any binaries you compile with this flag will be slow or broken on other CPU microarchitectures. If you use this option and want to switch or upgrade your CPU, you need to either recompile your binaries or choose a new CPU that uses the same microarchitecture as your old one. You can apply this option by default for makepkg.

If you compile your own kernel, you can also enable this option during kernel compilation with the  option. However, kernel improvements will be smaller as the kernel forbids extended vector instructions in generic code, which are responsible for the most of performance improvement in regular binaries, so most of the performance improvement will come from much smaller micro-optimizations.

## Graphics
## Xorg configuration
Graphics performance may depend on the settings in ; see the NVIDIA, AMDGPU and Intel articles. Improper settings may stop Xorg from working, so caution is advised.

## Mesa configuration
The performance of the Mesa drivers can be configured via drirc.  (Advanced DRI Configurator) is a GUI tool to configure Mesa drivers by setting options and writing them to the standard drirc file.

## Hardware video acceleration
Hardware video acceleration makes it possible for the video card to decode/encode video.

## Overclocking
As with CPUs, overclocking can directly improve performance, but is generally recommended against. There are several packages, such as  (ATI cards),  (recent AMD cards),  (old NVIDIA - up to Geforce 9), and  for recent NVIDIA cards.

See AMDGPU#Overclocking or NVIDIA/Tips and tricks#Enabling overclocking in nvidia-settings.

## Enabling PCIe resizable BAR
The PCI specification allows larger Base Address Registers (BARs) to be used for exposing PCI devices memory to the PCI Controller. This can result in a performance increase for video cards. Having access to the full video memory improves performance, but also enables optimizations in the graphics driver. The combination of resizable BAR, above 4G decoding and these driver optimizations are what AMD calls AMD Smart Access Memory, available at first on AMD Series 500 chipset motherboards, later expanded to AMD Series 400 and Intel Series 300 and later through UEFI updates. This setting may not be available on all motherboards, and is known to sometimes cause boot problems on certain boards.

If the BAR has a 256M size, the feature is not enabled or not supported:

To enable it, enable the setting named "Above 4G Decode" or ">4GB MMIO" in your motherboard settings. Verify that the BAR is now larger:

Resizable BAR can be verified using , where the GPU BAR size should be larger than 256 MB (example shown is a NVIDIA model 4070Ti Super with 16GB of RAM):

## RAM, swap and OOM handling
## Clock frequency and timings
RAM can run at different clock frequencies and timings, which can be configured in the BIOS. Memory performance depends on both values. Selecting the highest preset presented by the BIOS usually improves the performance over the default setting. Note that increasing the frequency to values not supported by both motherboard and RAM vendor is overclocking, and similar risks and disadvantages apply, see #Overclocking.

## Root on RAM overlay
If running off a slow writing medium (USB, spinning HDDs) and storage requirements are low, the root may be run on a RAM overlay ontop of read only root (on disk). This can vastly improve performance at the cost of a limited writable space to root. See .

## Swap on zram or zswap
Similar benefits (at similar costs) can be achieved using zswap or swap on zram. The two are generally similar in intent although not operation:

* zswap operates as a compressed RAM cache and neither requires (nor permits) extensive userspace configuration. It works in conjunction with a swap device by acting as its cache. Pages that would normally enter swap can enter zswap instead.
* zram is a kernel module which can be used to create a compressed block device in RAM. This compressed block device can be used as a swap device, with no other swap device required to back it up. It comes with many options, including the possibility of using a backing device for holding cold pages.

Because both options involve the swap subsystem, configuration that affects swap also affects these systems. For example, swappiness determines whether the kernel should prioritize dropping file cache or moving pages to swap when memory pressure is high. Because zswap intercepts the action of moving pages to swap and zram acts as the swap, the option would also determine how often these two mechanisms are used.

## Using the graphics card's RAM
In the unlikely case that you have very little RAM and a surplus of video RAM, you can use the latter as swap. See Swap on video RAM.

## Improving system responsiveness under low-memory conditions
On traditional GNU/Linux system, especially for graphical workstations, when allocated memory is overcommitted, the overall system's responsiveness may degrade to a nearly unusable state before either triggering the in-kernel out-of-memory (OOM)-killer or a sufficient amount of memory got free (which is unlikely to happen quickly when the system is unresponsive, as you can hardly close any memory-hungry applications which may continue to allocate more memory). The behaviour also depends on specific setups and conditions, returning to a normal responsive state may take from a few seconds to more than half an hour, which could be a pain to wait in serious scenario like during a conference presentation.

While the behaviour of the kernel as well as the userspace things under low-memory conditions may improve in the future as discussed on kernel and Fedora mailing lists, users can use more feasible and effective options than hard-resetting the system or tuning the  sysctl parameters:

* Manually trigger the kernel OOM-killer with Magic SysRq key, namely .
* Use a userspace OOM daemon to tackle these automatically (or interactively).

Sometimes a user may prefer OOM daemon to SysRq because with kernel OOM-killer you cannot prioritize the process to (or not) terminate. To list some OOM daemons:

*
*
*
*
*
*
*
