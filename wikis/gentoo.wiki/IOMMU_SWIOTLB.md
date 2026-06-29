This page contains [[changes](https://wiki.gentoo.org/index.php?title=IOMMU_SWIOTLB&diff=1300608)] which are not marked for translation.

\
This article provides instructions for enabling and configuring **I**nput **O**utput **M**emory **M**anagement **U**nit and the **S**oftware **I**nput **O**utput **T**ranslation **L**ookaside **B**uffer for use with the Linux kernel.

Today\'s computing uses a method of partitioning memory and each device such as a graphics card, PCI device, or USB device has to have memory mapped to be accessed by the device or application.

Traditionally IOMMU was used for memory mapping. This is set up when the system is initialized and can not be dynamically changed as the system is running so chip manufacturers such as Intel and AMD developed more advanced memory management methods.

In the Linux kernel we can manipulate the IOMMU using new mechanisms provided by SWIOTLB for Intel and others for architectures from AMD. 64-bit systems have enabled a huge amount of memory to be used in by the system and this memory needs mapping before it can be used. These kinds of terms are used across the Enterprise area of computing, particularly the Virtual-Machine sector but they can be used by anyone running a Linux kernel.

## Contents

-   [[1] [IOMMU]](#IOMMU)
    -   [[1.1] [Installation]](#Installation)
        -   [[1.1.1] [Kernel]](#Kernel)
    -   [[1.2] [Configuration]](#Configuration)
        -   [[1.2.1] [Generic options]](#Generic_options)
        -   [[1.2.2] [AMD64 systems]](#AMD64_systems)
        -   [[1.2.3] [Intel systems]](#Intel_systems)
-   [[2] [SWIOTLB]](#SWIOTLB)
-   [[3] [SWIOTLB for high input output (such as graphics)]](#SWIOTLB_for_high_input_output_.28such_as_graphics.29)

## [IOMMU]

This is **I**nput **O**utput **M**emory **M**anagement **U**nit. In every system this hardware is integrated into a north bridge controller which sets up the memory and is programmed by the firmware on your main-board. In recent years manufacturers have stopped integrating this as a North-Bridge chip and integrated it into the CPU itself. This is why if you want to upgrade your memory speed, type and so on you are now required to not only change the motherboard but the CPU as well.

Regardless the kernel needs to set up and read the mappings to be able to use your system memory efficiently.

### [Installation]

#### [Kernel]

Move to the kernel directory and open the menuconfig utility:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig `

Set the following options:

[KERNEL] **Example of IOMMU settings kernel**

    Device Drivers  --->
       [*] IOMMU Hardware Support  --->
          Generic IOMMU Pagetable Support  ----
          [*]   AMD IOMMU support
          [*]     Export AMD IOMMU statistics to debugfs
          <M>     AMD IOMMU Version 2 driver
          [*]   Support for Intel IOMMU using DMA Remapping Devices
          [*]     Support for Shared Virtual Memory with Intel IOMMU
          [*]     Enable Intel DMA Remapping Devices by default
          [*]   Support for Interrupt Remapping

The above will allow the kernel to control the mappings in the Memory Mapping controller.

Build and install the kernel:

`root `[`#`]`mount /boot `

`root `[`#`]`make && make modules_install && make install `

### [Configuration]

The following options for controlling aspects of the memory mapping will need to be added to the kernel command-line in order to take effect. Doing so varies depending on the system\'s bootloader. Common bootloaders include [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") and [Lilo](https://wiki.gentoo.org/wiki/Lilo "Lilo"). More information on bootloaders can be found [here](https://wiki.gentoo.org/wiki/Category:Bootloaders "Category:Bootloaders").

#### [Generic options]

  ------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Attribute           Description and options
  ` iommu=off `       This disables the IOMMU driver completely.
  ` iommu=noforce `   Don\'t force hardware IOMMU usage when it is not needed.
  ` iommu=force `     The use of the hardware IOMMU even when it is not actually needed (e.g. because \< 3 GB memory).
  ` iommu=soft `      Use software bounce buffering (SWIOTLB) (default for Intel machines). This can be used to prevent the usage of an available hardware IOMMU. (read bellow for Intel SWIOTLB).
  ------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [AMD64 systems]

  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Attribute                           Description and options

  `amd_iommu=nofullflush`,\           Enable flushing of IO/TLB entries they are unmapped. Otherwise they are flushed before they will be reused, which is a lot of faster.\
  `amd_iommu=fullflush`,\             `off` = do not initialize any AMD IOMMU found in the system.\
  `amd_iommu=off`,\                   `force_isolation` = Force device isolation for all devices. The IOMMU driver is not allowed anymore to lift isolation requirements as needed. This option does not override `iommu=pt`.
  `amd_iommu=force_isolation`

  `amd_iommu_dump=0`,\                This is a boolean option: `0` = disabled, `1` = enabled\
  `amd_iommu_dump=1`                  This is to dump the ACPI table for AMD IOMMU. With this option enabled, AMD IOMMU driver will print ACPI tables for AMD IOMMU during IOMMU initialization.

  `amd_iommu_intr=legacy`,\           Specifies one of the following AMD IOMMU interrupt remapping modes:\
  `amd_iommu_intr=vapic`              `legacy` = Use legacy interrupt remapping.\
                                      `mode.vapic` = Use virtual APIC mode, which allows IOMMU to inject interrupts directly into guest. This mode requires `kvm-amd.avic=1`. (Default when IOMMU HW support is present.)
  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [Intel systems]

Intel generally adopts \"an-always-enable-it-if-it-is-supported\" rule so most options are to turn off or disable the IOMMU functions.

  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Attribute                           Description and options

  `intel_iommu=on`,\                  This is a boolean option: `on` = enabled, `off` = disabled.
  `intel_iommu=off`

  ` intel_iommu=igfx_off `            This option turns off mapping for a graphics card and is the default state for this option. The gfx is mapped as normal device. If a gfx device has a dedicated DMAR unit, the DMAR unit is bypassed by not enabling DMAR with this option. In this case the gfx device will use physical address for DMA.

  ` intel_iommu=forcedac `            With this option iommu will not optimize to look for io virtual address below 32-bit forcing dual address cycle on pci bus for cards supporting greater than 32-bit addressing. The default is to look for translation below 32-bit and if not available then look in the higher range.

  ` intel_iommu=strict `              The default setting for this is disabled. This option on every unmap_single operation will result in a hardware IOTLB flush operation as opposed to batching them for performance.

  ` intel_iommu=sp_off `              Super Page which is by default enabled if supported, you can turn this off using this option.

  ` intel_iommu=ecs_off `             By default, extended context tables will be supported if the hardware advertises that it has support both for the extended tables themselves, and also PASID support. With this option set, extended tables will not be used even on hardware which claims to support them.
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [SWIOTLB]

**S**oft**w**are **I**nput **O**utput **T**ranslation **L**ookaside **B**uffer is an Intel technology which sort of bypasses the IOMMU and allows for a much more configurable memory management interface. Without going into the deep complexity of how this works, page tables are cached in the Lookaside Buffer reducing the need to constantly access physical RAM to map memory. This technology is also referred to as a bounce buffer as the physical address of the memory map is held in this virtual space of and IO is bounced between the physical IO and the Physical memory by this virtual lookaside buffer.

This allows the memory mapping to be carried out quickly and have a physical memory space available for use much faster than if it had to be created physically in RAM and presented to the system as usable.

Each IO TLB is referred to as a slab, this can be found in the [swiotlb.h] kernel header source file:

[FILE] **`/usr/src/linux-*/include/linux/swiotlb.h`**

    * Maximum allowable number of contiguous slabs to map,
     * must be a power of 2.  What is the appropriate value ?
     * The complexity of _single is linearly dependent on this value.

       #define IO_TLB_SEGSIZE   128

     * log of the size of each IO TLB slab.  The number of slabs is command line
     * controllable.
     *

So this means 1MB would be 8 slabs and the value used as the boot parameter is in slabs NOT size.

  ---------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Attribute                          Description and options
  ` swiotlb=n'th amount of slabs `   This specifies the amount of slabs to be used by IOTLB, each slab consists of 128K each which is 8 slabs per 1Mb(1024K), so a 64MB SWIOTLB would consist of 512 slabs. You can increase or decrease this value to allow for more buffering of virtual memory addresses in the buffer or not. Default is 64MB or 512 slabs.
  ` swiotlb=force `                  This option will force all system IO through the SWIOTLB so there will be no IOMMU controlled by the BIOS or the IOMMU driver elsewhere if one existed.
  ---------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [][SWIOTLB for high input output (such as graphics)]

For decades the problem has existed in that how would you get data in and out of the CPU and RAM quickly and efficiently especially for high throughput devices like file IO and graphic cards, etc.

Unfortunately the system is not only having to deal with that IO but many tasks all at the same time, the CPU and RAM may be very fast but if it cannot get the data out by either network, USB, storage device, or onto a screen via a graphics card it is a waste of time having a fast multiprocessing system.

Normally the system holds 4MB for normal operation and allows the rest to be used by other devices. The problem is that if a device overlaps or overflows into another then the system panics and can\'t deal with it. Many new devices like Nvidia graphics cards and SCSI controllers have drivers now that allow the IOMMU values they use to be set.

There is no safe way this value can be set (adjusted) automatically because of the diversity of hardware configurations possible on the market. This means the end user has to design and build the system and decide for each use case the best setting for the system.

If one set a large SWIOTLB then one would need to instruct the driver of a device to utilize the larger amount of memory mapping buffer. Some hardware physically control this in the BIOS while others do not provide any control. For the most part, newer high end hardware permit system administrators to control this by modifying the above kernel options.

Some drivers try to automatically control this but as mentioned above can cause stability issues even kernel panic.

Simply setting a large SWIOTLB will not mean a faster IO will be achieved; the hardware must be instructed to use it. Rule of thumb is if 64MB is available then set a maximum remap IO for the driver of 4MB less. This would be 60MB in this case. If 128MB then max remap for the driver would be 124MB and so on.