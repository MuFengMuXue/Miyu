# PCI passthrough via OVMF

The Open Virtual Machine Firmware (OVMF) is a project to enable UEFI support for virtual machines. Starting with Linux 3.9 and recent versions of QEMU, it is now possible to passthrough a graphics card, offering the virtual machine native graphics performance which is useful for graphic-intensive tasks.

Provided you have a desktop computer with a spare GPU you can dedicate to the host (be it an integrated GPU or an old OEM card, the brands do not even need to match) and that your hardware supports it (see #Prerequisites), it is possible to have a virtual machine of any OS with its own dedicated GPU and near-native performance. For more information on techniques see the background presentation (pdf).

## Prerequisites
A VGA Passthrough relies on a number of technologies that are not ubiquitous as of today and might not be available on your hardware. You will not be able to do this on your machine unless the following requirements are met:

* Your CPU must support hardware virtualization (for kvm) and IOMMU (for the passthrough itself).
** List of compatible Intel CPUs (Intel VT-x and Intel VT-d).
** All AMD CPUs from the Bulldozer generation and up (including Zen) should be compatible.
*** CPUs from the K10 generation (2007) do not have an IOMMU, so you need to have a motherboard with a 890FX or 990FX chipset to make it work, as those have their own IOMMU.
* Your motherboard must also support IOMMU.
** Both the chipset and the BIOS must support it. It is not always easy to tell at a glance whether or not this is the case, but there is a fairly comprehensive list on the matter on the Xen wiki as well as Wikipedia:List of IOMMU-supporting hardware.
* Your guest GPU ROM must support UEFI.
** If you can find any ROM in this list that applies to your specific GPU and is said to support UEFI, you are generally in the clear. All GPUs from 2012 and later should support this, as Microsoft made UEFI a requirement for devices to be marketed as compatible with Windows 8.

You will probably want to have a spare monitor or one with multiple input ports connected to different GPUs (the passthrough GPU will not display anything if there is no screen plugged in and using a VNC or Spice connection will not help your performance), as well as a mouse and a keyboard you can pass to your virtual machine. If anything goes wrong, you will at least have a way to control your host machine this way.

## Setting up IOMMU
Using IOMMU opens to features like PCI passthrough and memory protection from faulty or malicious devices, see Wikipedia:Input-output memory management unit#Advantages and Memory Management (computer programming): Could you explain IOMMU in plain English?.

## Enabling IOMMU
Ensure that AMD-Vi or Intel VT-d is supported by your CPU and enabled in the BIOS settings. These options typically appear alongside other CPU features, which may be located in an overclocking-related menu. They may be listed under their actual names ("VT-d" or "AMD-Vi") or in more ambiguous terms such as "Virtualization Technology," which may or may not be explained in the motherboard manual.

Use dmesg to check whether IOMMU is enabled:

To manually enable IOMMU support, set the correct kernel parameter depending on the type of CPU in use:

* For Intel CPUs (VT-d) set , unless your kernel sets the  config option.
* For AMD CPUs (AMD-Vi), IOMMU support is enabled automatically if the kernel detects IOMMU hardware support from the BIOS.

## Ensuring that the groups are valid
The following script should allow you to see how your various PCI devices are mapped to IOMMU groups. If it does not return anything, you either have not enabled IOMMU support properly or your hardware does not support it.

 #!/bin/bash
 shopt -s nullglob
 for g in $(find /sys/kernel/iommu_groups/* -maxdepth 0 -type d | sort -V); do
     echo "IOMMU Group ${g##*/}:"
     for d in $g/devices/*; do
         echo -e "\t$(lspci -nns ${d##*/})"
     done;
 done;

Example output:

 IOMMU Group 1:
 	00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
 IOMMU Group 2:
 	00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:0e31 (rev 04)
 IOMMU Group 4:
 	00:1a.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 (rev 04)
 IOMMU Group 10:
 	00:1d.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:0e26 (rev 04)
 IOMMU Group 13:
 	06:00.0 VGA compatible controller: NVIDIA Corporation GM204 GTX 970 (rev a1)
 	06:00.1 Audio device: NVIDIA Corporation GM204 High Definition Audio Controller [10de:0fbb (rev a1)

An IOMMU group is the smallest set of physical devices that can be passed to a virtual machine. For instance, in the example above, both the GPU in 06:00.0 and its audio controller in 6:00.1 belong to IOMMU group 13 and can only be passed together. The frontal USB controller, however, has its own group (group 2) which is separate from both the USB expansion controller (group 10) and the rear USB controller (group 4), meaning that any of them could be passed to a virtual machine without affecting the others.

## Gotchas
## Plugging your guest GPU in an unisolated CPU-based PCIe slot
Not all PCIe slots are the same. Most motherboards have PCIe slots provided by both the CPU and the PCH. Depending on your CPU, it is possible that your processor-based PCIe slot does not support isolation properly, in which case the PCI slot itself will appear to be grouped with the device that is connected to it.

 IOMMU Group 1:
 	 00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
 	 01:00.0 VGA compatible controller: NVIDIA Corporation GM107 GTX 750 (rev a2)
 	 01:00.1 Audio device: NVIDIA Corporation Device 0fbc (rev a1)

This is fine so long as only your guest GPU is included in here, such as above. Depending on what is plugged in to your other PCIe slots and whether they are allocated to your CPU or your PCH, you may find yourself with additional devices within the same group, which would force you to pass those as well. If you are ok with passing everything that is in there to your virtual machine, you are free to continue. Otherwise, you will either need to try and plug your GPU in your other PCIe slots (if you have any) and see if those provide isolation from the rest or to install the ACS override patch, which comes with its own drawbacks. See #Bypassing the IOMMU groups (ACS override patch) for more information.

## Isolating the GPU
In order to assign a device to a virtual machine, this device and all those sharing the same IOMMU group must have their driver replaced by a stub driver or a VFIO driver in order to prevent the host machine from interacting with them. In the case of most devices, this can be done on the fly right before the virtual machine starts.

However, due to their size and complexity, GPU drivers do not tend to support dynamic rebinding very well, so you cannot just have some GPU you use on the host be transparently passed to a virtual machine without having both drivers conflict with each other. Because of this, it is generally advised to bind those placeholder drivers manually before starting the virtual machine, in order to stop other drivers from attempting to claim it.

The following section details how to configure a GPU so those placeholder drivers are bound early during the boot process, which makes said device inactive until a virtual machine claims it or the driver is switched back. This is the preferred method, considering it has less caveats than switching drivers once the system is fully online.

Starting with Linux 4.1, the kernel includes vfio-pci. This is a VFIO driver, meaning it fulfills the same role as pci-stub did, but it can also control devices to an extent, such as by switching them into their D3 state when they are not in use.

## Binding vfio-pci via device ID
Vfio-pci normally targets PCI devices by ID, meaning you only need to specify the IDs of the devices you intend to passthrough. For the following IOMMU group, you would want to bind vfio-pci with  and , which will be used as example values for the rest of this section.

Providing the device IDs is done via the kernel module parameter  for .

In case of wanting to keep the HDAudio in the host it can be detached by using the kernel module parameters  for  and  for .

You can use this bash script without kernel  ID. GPU can function in host after calling .

{{bc|
#!/bin/bash

gpu="0000:06:00.0"
aud="0000:06:00.1"
gpu_vd="$(cat /sys/bus/pci/devices/$gpu/vendor) $(cat /sys/bus/pci/devices/$gpu/device)"
aud_vd="$(cat /sys/bus/pci/devices/$aud/vendor) $(cat /sys/bus/pci/devices/$aud/device)"

function bind_vfio {
  echo "$gpu" > "/sys/bus/pci/devices/$gpu/driver/unbind"
  echo "$aud" > "/sys/bus/pci/devices/$aud/driver/unbind"
  echo "$gpu_vd" > /sys/bus/pci/drivers/vfio-pci/new_id
  echo "$aud_vd" > /sys/bus/pci/drivers/vfio-pci/new_id
}

function unbind_vfio {
  echo "$gpu_vd" > "/sys/bus/pci/drivers/vfio-pci/remove_id"
  echo "$aud_vd" > "/sys/bus/pci/drivers/vfio-pci/remove_id"
  echo 1 > "/sys/bus/pci/devices/$gpu/remove"
  echo 1 > "/sys/bus/pci/devices/$aud/remove"
  echo 1 > "/sys/bus/pci/rescan"
}
}}

## Loading vfio-pci early
Since Arch's  has vfio-pci built as a module, we need to force it to load before the graphics drivers have a chance to bind to the card. There are two methods: modprobe configuration, or adding the modules to initramfs.

## modprobe.d
This method loads  when udev loads GPU drivers. This avoids bloating initramfs and slowing boot times unnecessarily.

If you are passing through an NVIDIA GPU and have the proprietary NVIDIA driver installed, use the following instead:

## initramfs
## mkinitcpio
Add , , and  to mkinitcpio:

Also, ensure that the modconf hook is included in the HOOKS list of :

Since new modules have been added to the initramfs configuration, you must regenerate the initramfs.

## booster
Similar to mkinitcpio you need to specify modules to load early:

and then regenerate booster images.

## dracut
Following the same idea, we need to ensure all vfio drivers are in the initramfs. Add the following file to :

Note that we used  instead the usual  option, which will ensure that the drivers are tried to be loaded early via modprobe (Dracut#Early kernel module loading).

As with mkinitcpio, you must regenerate the initramfs afterwards. See dracut for more details.

## Verifying that the configuration worked
Reboot and verify that vfio-pci has loaded properly and that it is now bound to the right devices.

It is not necessary for all devices (or even expected device) from  to be in dmesg output.
Even if a device does not appear, it might still be visible and usable in the guest virtual machine.

## Setting up an OVMF-based guest virtual machine
OVMF is an open-source UEFI firmware for QEMU virtual machines. While it is possible to use SeaBIOS to get similar results to an actual PCI passthrough, the setup process is different and it is generally preferable to use the EFI method if your hardware supports it.

## Configuring libvirt
Libvirt is a wrapper for a number of virtualization utilities that greatly simplifies the configuration and deployment process of virtual machines. In the case of KVM and QEMU, the frontend it provides allows us to avoid dealing with the permissions for QEMU and make it easier to add and remove various devices on a live virtual machine. Its status as a wrapper, however, means that it might not always support all of the latest qemu features, which could end up requiring the use of a wrapper script to provide some extra arguments to QEMU.

Install , , , and . For the default network connection  is required.

Follow Libvirt#Configuration to configure libvirt for use.

You may also need to activate the default libvirt network:
 # virsh net-autostart default
 # virsh net-start default

## Setting up the guest OS
The process of setting up a virtual machine using  is mostly self-explanatory, as most of the process comes with fairly comprehensive on-screen instructions.

However, you should pay special attention to the following steps:

* When the virtual machine creation wizard asks you to name your virtual machine (final step before clicking "Finish"), check the "Customize before install" checkbox.
* In the "Overview" section, set your firmware to "UEFI". If the option is grayed out, make sure that:
** Your hypervisor is running as a system session and not a user session. This can be verified by clicking, then hovering over the session in virt-manager. If you are accidentally running it as a user session, you must open a new connection by clicking "File" > "Add Connection..", then select the option from the drop-down menu station "QEMU/KVM" and not "QEMU/KVM user session".
* In the "CPUs" section, change your CPU model to "host-passthrough". If it is not in the list, you will have to either type it by hand or by using . This will ensure that your CPU is detected properly, since it causes libvirt to expose your CPU capabilities exactly as they are instead of only those it recognizes (which is the preferred default behavior to make CPU behavior easier to reproduce). Without it, some applications may complain about your CPU being of an unknown model.
* If you want to minimize IO overhead, it is easier to setup #Virtio disk before installing

The rest of the installation process will take place as normal using a standard QXL video adapter running in a window. At this point, there is no need to install additional drivers for the rest of the virtual devices, since most of them will be removed later on. Once the guest OS is done installing, simply turn off the virtual machine. It is possible you will be dropped into the UEFI menu instead of starting the installation upon powering your virtual machine for the first time. Sometimes the correct ISO file was not automatically detected and you will need to manually specify the drive to boot. By typing exit and navigating to "boot manager" you will enter a menu that allows you to choose between devices.

## Attaching the PCI devices
With the installation done, it is now possible to edit the hardware details in libvirt and remove virtual integration devices, such as the spice channel and virtual display, the QXL video adapter, the emulated mouse and keyboard and the USB tablet device.

For example, remove the following sections from your XML file:

Since that leaves you with no input devices, you may want to bind a few USB host devices to your virtual machine as well, but remember to leave at least one mouse and/or keyboard assigned to your host in case something goes wrong with the guest. This may be done by using .

At this point, it also becomes possible to attach the PCI device that was isolated earlier; simply click on "Add Hardware" and select the PCI Host Devices you want to passthrough. If everything went well, the screen plugged into your GPU should show the OVMF splash screen and your virtual machine should start up normally. From there, you can setup the drivers for the rest of your virtual machine.

## Video card driver virtualisation detection
Video card drivers by AMD incorporate very basic virtual machine detection targeting Hyper-V extensions. Should this detection mechanism trigger, the drivers will refuse to run, resulting in a black screen.

If this is the case, it is required to modify the reported Hyper-V vendor ID:

Nvidia guest drivers prior to version 465 exhibited a similar behaviour which resulted in a generic error 43 in the card's device manager status. Systems using these older drivers therefore also need the above modification. In addition, they also require hiding the KVM CPU leaf:

Note that the above steps do not equate 'hiding' the virtual machine from Windows or any drivers/programs running in the virtual machine. Also, various other issues not related to any detection mechanism referred to here can also trigger error 43.

## Passing keyboard/mouse via Evdev
If you do not have a spare mouse or keyboard to dedicate to your guest, and you do not want to suffer from the video overhead of Spice, you can setup evdev to share them between your Linux host and your virtual machine.

First, find your keyboard and mouse devices in . Only devices with  in their name are valid. You may find multiple devices associated to your mouse or keyboard, so try  and either hit some keys on the keyboard or wiggle your mouse to see if input comes through, if so you have got the right device. Now add those devices to your configuration:

Replace  and  with your device path. Now you can startup the guest OS and test swapping control of your mouse and keyboard between the host and guest by pressing both the left and right control keys at the same time.

You may also consider switching from PS/2 to Virtio inputs in your configurations. Add these two devices:

The virtio input devices will not actually be used until the guest drivers are installed. QEMU will continue to send key events to the PS2 devices until it detects the virtio input driver initialization. Note that the PS2 devices cannot be removed as they are an internal function of the emulated Q35/440FX chipsets.

## Gotchas
## Using a non-EFI image on an OVMF-based virtual machine
The OVMF firmware does not support booting off non-EFI mediums. If the installation process drops you in a UEFI shell right after booting, you may have an invalid EFI boot media. Try using an alternate Linux/Windows image to determine if you have an invalid media.

## Keyboard Events on Wayland
Wayland blocks mutual access to keyboard events after the session started. To get around this you must start the virtual machine prior to the Wayland session starting.

## Performance tuning
Most use cases for PCI passthroughs relate to performance-intensive domains such as video games and GPU-accelerated tasks. While a PCI passthrough on its own is a step towards reaching native performance, there are still a few ajustments on the host and guest to get the most out of your virtual machine.

## CPU pinning
The default behavior for KVM guests is to run operations coming from the guest as a number of threads representing virtual processors. Those threads are managed by the Linux scheduler like any other thread and are dispatched to any available CPU cores based on niceness and priority queues. As such, the local CPU cache benefits (L1/L2/L3) are lost each time the host scheduler reschedules the virtual CPU thread on a different physical CPU. This can noticeably harm performance on the guest. CPU pinning aims to resolve this by limiting which physical CPUs the virtual CPUs are allowed to run on. The ideal setup is a one to one mapping such that the virtual CPU cores match physical CPU cores while taking hyperthreading/SMT into account.

In addition, in some modern CPUs, groups of cores often share a common L3 cache. In such cases, care should be taken to pin exactly those physical cores that share a particular L3. Failing to do so might lead to cache evictions which could result in microstutters.

## CPU topology
Most modern CPUs support hardware multitasking, also known as hyper-threading on Intel CPUs or SMT on AMD CPUs. Hyper-threading/SMT is simply a very efficient way of running two threads on one CPU core at any given time. You will want to take into consideration that the CPU pinning you choose will greatly depend on what you do with your host while your virtual machine is running.

To find the topology for your CPU run :

 on a 6c/12t Ryzen 5 1600:

 CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE MAXMHZ    MINMHZ
 0   0    0      0    0:0:0:0       yes    3800.0000 1550.0000
 1   0    0      0    0:0:0:0       yes    3800.0000 1550.0000
 2   0    0      1    1:1:1:0       yes    3800.0000 1550.0000
 3   0    0      1    1:1:1:0       yes    3800.0000 1550.0000
 4   0    0      2    2:2:2:0       yes    3800.0000 1550.0000
 5   0    0      2    2:2:2:0       yes    3800.0000 1550.0000
 6   0    0      3    3:3:3:1       yes    3800.0000 1550.0000
 7   0    0      3    3:3:3:1       yes    3800.0000 1550.0000
 8   0    0      4    4:4:4:1       yes    3800.0000 1550.0000
 9   0    0      4    4:4:4:1       yes    3800.0000 1550.0000
 10  0    0      5    5:5:5:1       yes    3800.0000 1550.0000
 11  0    0      5    5:5:5:1       yes    3800.0000 1550.0000

Considering the L3 mapping, it is recommended to pin and isolate CPUs 6–11. Pinning and isolating fewer than these (e.g. 8–11) would result in the host system making use of the L3 cache in core 6 and 7 which would eventually lead to cache evictions and therefore bad performance.

 on a 6c/12t Intel 8700k:

 CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE MAXMHZ    MINMHZ
 0   0    0      0    0:0:0:0       yes    4600.0000 800.0000
 1   0    0      1    1:1:1:0       yes    4600.0000 800.0000
 2   0    0      2    2:2:2:0       yes    4600.0000 800.0000
 3   0    0      3    3:3:3:0       yes    4600.0000 800.0000
 4   0    0      4    4:4:4:0       yes    4600.0000 800.0000
 5   0    0      5    5:5:5:0       yes    4600.0000 800.0000
 6   0    0      0    0:0:0:0       yes    4600.0000 800.0000
 7   0    0      1    1:1:1:0       yes    4600.0000 800.0000
 8   0    0      2    2:2:2:0       yes    4600.0000 800.0000
 9   0    0      3    3:3:3:0       yes    4600.0000 800.0000
 10  0    0      4    4:4:4:0       yes    4600.0000 800.0000
 11  0    0      5    5:5:5:0       yes    4600.0000 800.0000

Since all cores are connected to the same L3 in this example, it does not matter much how many CPUs you pin and isolate as long as you do it in the proper thread pairs. For instance, (0, 6), (1, 7), etc.

As we see above, with AMD Core 0 is sequential with CPU 0 & 1, whereas Intel places Core 0 on CPU 0 & 6.

If you do not need all cores for the guest, it would then be preferable to leave at the very least one core for the host. Choosing which cores one to use for the host or guest should be based on the specific hardware characteristics of your CPU, however Core 0 is a good choice for the host in most cases. If any cores are reserved for the host, it is recommended to pin the emulator and iothreads, if used, to the host cores rather than the VCPUs. This may improve performance and reduce latency for the guest since those threads will not pollute the cache or contend for scheduling with the guest VCPU threads. If all cores are passed to the guest, there is no need or benefit to pinning the emulator or iothreads.

## XML examples
## 4c/1t CPU w/o Hyperthreading Example
## 4c/2t Intel/AMD CPU example (after ComboPI AGESA bios update)
## 4c/2t AMD CPU example (Before ComboPi AGESA bios update)
If you do not intend to be doing any computation-heavy work on the host (or even anything at all) at the same time as you would on the virtual machine, you may want to pin your virtual machine threads across all of your cores, so that the virtual machine can fully take advantage of the spare CPU time the host has available. Be aware that pinning all physical and logical cores of your CPU could induce latency in the guest virtual machine.

## Huge memory pages
When dealing with applications that require large amounts of memory, memory latency can become a problem since the more memory pages are being used, the more likely it is that this application will attempt to access information across multiple memory "pages", which is the base unit for memory allocation. Resolving the actual address of the memory page takes multiple steps, and so CPUs normally cache information on recently used memory pages to make subsequent uses on the same pages faster. Applications using large amounts of memory run into a problem where, for instance, a virtual machine uses 4 GiB of memory divided into 4 KiB pages (which is the default size for normal pages) for a total of 1.04 million pages, meaning that such cache misses can become extremely frequent and greatly increase memory latency. Huge pages exist to mitigate this issue by giving larger individual pages to those applications, increasing the odds that multiple operations will target the same page in succession.

## Transparent huge pages
QEMU will use 2MiB sized transparent huge pages automatically without any explicit configuration in QEMU or Libvirt, subject to some important caveats. When using VFIO the pages are locked in at boot time and transparent huge pages are allocated up front when the virtual machine first boots. If the kernel memory is highly fragmented, or the virtual machine is using a majority of the remaining free memory, it is likely that the kernel will not have enough 2MiB pages to fully satisfy the allocation. In such a case, it silently fails by using a mix of 2MiB and 4KiB pages. Since the pages are locked in VFIO mode, the kernel will not be able to convert those 4KiB pages to huge after the virtual machine starts either. The number of available 2MiB huge pages available to THP is the same as via the #Dynamic huge pages mechanism described in the following sections.

To check how much memory THP is using globally:

To check a specific QEMU instance. QEMU's PID must be substituted in the grep command:

In this example, the virtual machine was allocated 8388608KiB of memory, but only 8087552KiB was available via THP. The remaining 301056KiB are allocated as 4KiB pages. Aside from manually checking, there is no indication when partial allocations occur.  As such, THP's effectiveness is very much dependent on the host system's memory fragmentation at the time of virtual machine startup. If this trade off is unacceptable or strict guarantees are required, #Static huge pages is recommended.

Arch kernels have THP compiled in and enabled by default with  set to  mode.

## Static huge pages
While transparent huge pages should work in the vast majority of cases, they can also be allocated statically during boot. This should only be needed to make use 1 GiB hugepages on machines that support it, since transparent huge pages normally only go up to 2 MiB.

To allocate huge pages at boot, one must simply specify the desired amount on their kernel command line with . For instance, reserving 1024 pages with  and the default size of 2048 KiB per huge page creates 2 GiB worth of memory for the virtual machine to use.

If supported by CPU page size could be set manually. 1 GiB huge page support could be verified by . Setting 1 GiB huge page size via kernel parameters : .

Also, since static huge pages can only be used by applications that specifically request it, you must add this section in your libvirt domain configuration to allow kvm to benefit from them :

## Dynamic huge pages
Hugepages could be allocated manually via  sysctl parameter.

Where  - is the number of huge pages, which default size if 2 MiB.
Pages will be automatically allocated, and freed after the virtual machine stops.

More manual way:

 # echo num > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
 # echo num > /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages

For 2 MiB and 1 GiB page size respectively.
And they should be manually freed in the same way.

It is hardly recommended to drop caches, compact memory and wait a couple of seconds before starting the virtual machine, as there could be not enough free contiguous memory for required huge pages blocks. Especially after some uptime of the host system.

 # echo 3 > /proc/sys/vm/drop_caches
 # echo 1 > /proc/sys/vm/compact_memory

Theoretically, 1 GiB pages works as 2 MiB. But practically - no guaranteed way was found to get contiguous 1 GiB memory blocks. Each consequent request of 1 GiB blocks lead to lesser and lesser dynamically allocated count.

## CPU frequency governor
Depending on the way your CPU governor is configured, the virtual machine threads may not hit the CPU load thresholds for the frequency to ramp up. Indeed, KVM cannot actually change the CPU frequency on its own, which can be a problem if it does not scale up with vCPU usage as it would result in underwhelming performance. An easy way to see if it behaves correctly is to check if the frequency reported by  goes up when running a CPU-intensive task on the guest. If you are indeed experiencing stutter and the frequency does not go up to reach its reported maximum, it may be due to CPU scaling being controlled by the host OS. In this case, try setting all cores to maximum frequency to see if this improves performance. Note that if you are using a modern intel chip with the default pstate driver, cpupower commands will be ineffective, so monitor  to make sure your cpu is actually at max frequency.

## Isolating pinned CPUs
CPU pinning by itself will not prevent other host processes from running on the pinned CPUs. Properly isolating the pinned CPUs can reduce latency in the guest virtual machine.

## With isolcpus kernel parameter
In this example, let us assume you are using CPUs 4-7.
Use the kernel parameters  to completely isolate the CPUs from the kernel. For example:

 isolcpus=4-7 nohz_full=4-7

Then, run  with taskset and chrt:

 # chrt -r 1 taskset -c 4-7 qemu-system-x86_64 ...

The  command will ensure that the task scheduler will round-robin distribute work (otherwise it will all stay on the first cpu). For , the CPU numbers can be comma- and/or dash-separated, like "0,1,2,3" or "0-4" or "1,7-8,10" etc.

See the Internet Archive copy of a Removeddit mirror of a Reddit thread for more info.

## Dynamically isolating CPUs
The isolcpus kernel parameter will permanently reserve CPU cores, even when the guest is not running. A more flexible alternative is to dynamically isolate CPUs when starting the guest. This can be achieved with the following alternatives:

*  (vfio-users post, blog post, example script)
*
* systemd

## Example with systemd
In this example, we assume a host with 12 CPUs, where CPUs 2-5 and 8-11 are pinned to the guest. Then run the following to isolate the host to CPUs 0, 1, 6, and 7:

 # systemctl set-property --runtime -- user.slice AllowedCPUs=0,1,6,7
 # systemctl set-property --runtime -- system.slice AllowedCPUs=0,1,6,7
 # systemctl set-property --runtime -- init.scope AllowedCPUs=0,1,6,7

After shutting down the guest, run the following to reallocate all 12 CPUs back to the host:

 # systemctl set-property --runtime -- user.slice AllowedCPUs=0-11
 # systemctl set-property --runtime -- system.slice AllowedCPUs=0-11
 # systemctl set-property --runtime -- init.scope AllowedCPUs=0-11

You can use a libvirt hook to automatically run the above at startup/shutdown of the guest like so:

Create or edit  with the following content:

Afterwards make it executable.

Restart  and then start your virtual machine. If you create some heavily multithreaded load on your host now, you should see that it keeps your chosen CPUs free from load while the virtual machine can still make use of it. You should also see those CPUs automatically getting fully used by your host once you terminate the virtual machine.

If you have multiple virtual machines and want to pin CPU cores only for some of them (or different amounts of cores for each), you can edit the hook file like so:

Make it executable, if needed.

More examples are contained in the following Reddit threads: [https://www.reddit.com/r/VFIO/comments/gyem88/noob_question_how_to_isolate_cpu_cores/ftaqno1/ Note that this requires systemd 244 or higher, and cgroups v2, which is now enabled by default.

## Improving performance on AMD CPUs
Starting with QEMU 3.1 the TOPOEXT cpuid flag is disabled by default. In order to use hyperthreading (SMT) on AMD CPUs you need to manually enable it:

commit: https://gitlab.com/qemu-project/qemu/-/commit/7210a02c58572b2686a3a8d610c6628f87864aed

## Virtio disk
The default disk types are SATA or IDE emulation out of the box. These controllers offer maximum compatibility but are not suited for efficient virtualization. Two accelerated models exist:  for SCSI emulation and passthrough, or  for a more basic block device emulation.

## Drivers
* Linux guests should support these out of the box on any modern kernel
* macOS has  support starting in Mojave via
* Windows needs the [https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/ Windows virtio drivers.  uses the  driver.  uses the  driver
* Windows can be installed directly onto these disks by selecting 'load driver' on the installer disk selection menu. The windows iso and virtio driver iso should both be attached as regular SATA/IDE cdroms during the installation process
* To switch boot disks to virtio on an existing Windows installation:
** : Add a temporary disk with bus , boot windows & load the driver for the disk, then shutdown and switch the boot disk disk bus to
** : Add a scsi controller with model , boot windows & load the driver for the controller, then shutdown and switch the boot disk bus to  (not virtio)

## Considerations
*  TRIM support is mature, all versions should support it. Traditionally,  has been the preferred approach for this reason
*  TRIM support is new, this requires qemu 4.0+, guest linux kernel 5.0+, guest windows drivers 0.1.173+
* Thin provisioning works by enabling TRIM on a sparse image file: . Unused blocks will be freed and the disk usage will drop (works on both raw and qcow2). Actual on-disk size of a sparse image file may be checked with
* Thin provisioning can also work with block storage such as zfs zvols or thin lvm
* Virt queue count will influence the number of threads inside the guest kernel used for IO processing, suggest using  or more
* Native mode () uses a single threaded model based on linux AIO, is a bit more CPU efficient but may have lower peak performance and does not allow host side caching to be used
* Threaded mode () will spawn dozens of threads on demand as the disk is used. This is less efficient but may perform better if there are enough host cores available to run them, and allows for host side caching to be used
* Modern versions of libvirt will group the dynamic worker threads created when using threaded mode in with the iothread=1 cgroup for pinning purposes. Very old versions of libvirt left these in the emulator cgroup

## IO threads
An IO thread is a dedicated thread for processing disk events, rather than using the main qemu emulator loop. This should not be confused with the worker threads spawned on demand with .

* You can only use one iothread per disk controller. The thread must be assigned to a specific controller with  in the  tag. Furthermore, extra & unassigned iothreads will not be used and do nothing
* In the case of , there is one controller for multiple scsi disks. The iothread is assigned on the controller:
* In the case of , each disk has its own controller. The iothread is assigned in the driver tag under the disk itself:
* Since emulated disks incur a significant amount of CPU overhead, that can lead to vcpu stuttering under high disk load (especially high random IOPS). In this case it helps to pin the IO to different core(s) than your vcpus with

## Examples with libvirt
virtio-scsi + iothread + worker threads + host side writeback caching + full disk block device backend:

virtio-blk + iothread + native aio + no host caching + raw sparse image backend:

Creating the iothreads:

   1

Pinning iothreads:

## Example with virt-manager
This will create a  device:
# Open the virtual machine preferences
# Go to
# Create or choose a storage file
# Select  and
# Click Finish

## Virtio network
The default NIC models rtl8139 or e1000 can be a bottleneck for gigabit+ speeds and have a significant amount of CPU overhead compared to .

* Select  as the model for the NIC with libvirt or use the  device in bare qemu
* Windows needs the  driver from Windows virtio drivers
* Virtio uses vhost-net by default for in-kernel packet processing without exiting to userspace
* Multiqueue can enabled for a further speedup with multiple connections but typically will not boost single stream speeds. For libvirt add  under the interface tag
* Zero copy transmit may also be enabled on macvtap by setting the module parameter  but this may actually have worse performance, see commit

Libvirt example with a bridge:

MACVTAP example with a bridge:

Possible options for mode are 'vepa', 'bridge', 'private', and 'passthrough'.  A guide with decriptions of the differences is available from redhatReplace the source  device with your own device address. You can get your local address with the following command:

## Further tuning
More specialized virtual machine tuning tips are available at [https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/virtualization_tuning_and_optimization_guide/index Red Hat's Virtualization Tuning and Optimization Guide.

## Special procedures
Certain setups require specific configuration tweaks in order to work properly. If you are having problems getting your host or your virtual machine to work properly, see if your system matches one of the cases below and try adjusting your configuration accordingly.

## Using identical guest and host GPUs
Due to how vfio-pci uses your vendor and device id pair to identify which device they need to bind to at boot, if you have two GPUs sharing such an ID pair you will not be able to get your passthrough driver to bind with just one of them. This sort of setup makes it necessary to use a script, so that whichever driver you are using is instead assigned by pci bus address using the  mechanism.

## Script variants
## Passthrough all GPUs but the boot GPU
Here, we will make a script to bind vfio-pci to all GPUs but the boot gpu. Create the following script (and do not forget to make it executable):

{{hc|/usr/local/bin/vfio-pci-override.sh|2=
#!/bin/sh

for i in /sys/bus/pci/devices/*/boot_vga; do
    if [ $(cat "$i") -eq 0 ]; then
        GPU="${i%/boot_vga}"
        AUDIO="$(echo "$GPU"  sed -e "s/0$/1/")"
        USB="$(echo "$GPU"  sed -e "s/0$/2/")"
        echo "vfio-pci" > "$GPU/driver_override"
        if [ -d "$AUDIO" ]; then
            echo "vfio-pci" > "$AUDIO/driver_override"
        fi
        if [ -d "$USB" ]; then
            echo "vfio-pci" > "$USB/driver_override"
        fi
    fi
done

modprobe -i vfio-pci
}}

## Passthrough selected GPU
In this case we manually specify the GPU to bind.

## Passthrough IOMMU Group based of GPU
Simplifying the passthrough of other necessary devices from selected GPU(s).
Things like the graphicscard's onboard Audio, USB and RGB controllers.

## Script installation
Edit :

# Add  to the HOOKS array and  to the FILES array.

Edit :

# Add the following line:
# Regenerate the initramfs and reboot.

## Passing the boot GPU to the guest
The GPU marked as  is a special case when it comes to doing PCI passthroughs, since the BIOS needs to use it in order to display things like boot messages or the BIOS configuration menu. To do that, it makes a copy of the VGA boot ROM which can then be freely modified. This modified copy is the version the system gets to see, which the passthrough driver may reject as invalid. As such, it is generally recommended to change the boot GPU in the BIOS configuration so the host GPU is used instead or, if that is not possible, to swap the host and guest cards in the machine itself.

## Using Looking Glass to stream guest screen to the host
It is possible to make a virtual machine share the monitor, and optionally a keyboard and a mouse with a help of Looking Glass.

## Install the application on the host machine
Go to the project's website and follow the instructions on the "Build" section of the docs. Optionally, you can also install the KVMFR (KVM FrameRelay) kernel module with DKMS, which requires installing the headers package for your kernel(s), like .

## Adding IVSHMEM Device to virtual machines
Looking Glass works by creating a shared memory buffer between a host and a guest. This is a lot faster than streaming frames via localhost, but requires additional setup.

## Calculating the needed memory
You will first need to calculate the memory size to be suitable for your desired maximum resolution using the following formula:

 Width x Height x BPP x 2 = frame size in bytes
 frame size in bytes ÷ 1048576 =  frame size in MiB
 frame size in MiB + 10 = required size in MiB

The result must be rounded up to the nearest power of 2. Finally:

 required size in MiB * 1048576 = required size in bytes

BPP (Bits Per Pixel) is 4 for SDR and 8 for HDR.

Example with 1920x1080 and SDR:

 1920 x 1080 x 4 x 2 = 16,588,800 bytes
 16,588,800 / 1048576 = 15.82 MiB + 10 = 25.82 ---> use 32 MiB (and 33554432 bytes)

## Standard shared memory
This method does not need the KVMFR module to be installed on the host.

With your virtual machine turned off, open the machine configuration:

Replace  with the value that you calculated, in MiB. Next create a configuration file to create the shared memory file on boot:

Replace  with your username.

Ask systemd-tmpfiles to create the shared memory file now without waiting to next boot:

 # systemd-tmpfiles --create /etc/tmpfiles.d/10-looking-glass.conf

## KVMFR module
Alternatively, you can use the KVMFR module (recommended by upstream). After installing it, create the following file:

Replace  with the required value you calculated previously, in MiB. Now simply run .

Loading the module creates the  node. To automatically give your user permission to access it, create the following udev rule:

Sourced from the Looking Glass Discord server. Rule developed after the release of systemd v258, which changed how device nodes are handled. Official Looking Glass documentation will be updated with version B8.

You also need to edit the  file and uncomment the  block, adding  to the list. To make this change active you then must restart .

Finally, edit the virtual machine's XML:

Add the required value, in bytes, that you calculated earlier.

You can load this module automatically at boot time (as suggested by upstream) or whenever a virtual machine starts with a libvirt hook:

Make the hook executable, if needed.

## Installing the IVSHMEM Host to Windows guest
Currently Windows does not notify users about a new IVSHMEM device, it silently installs a dummy driver. To actually enable the device, you have to go into Device Manager and update the driver for the device under the "System Devices" node for "PCI standard RAM Controller".

Download the signed driver from Red Hat. Once the driver is installed, you must download the looking-glass-host package that matches the client you have installed on the host system, and install it on your guest system.

In order to run it you would also need to install Microsoft Visual C++ Redistributable from Microsoft (it can be installed with winget).

The recent version will automatically install a service that starts the daemon on boot. The logs of the host daemon are located at  on the guest system.

## Setting up the null video device
(Retrieved from If you would like to use Spice to give you keyboard and mouse input along with clipboard sync support, make sure you have a  device, then:

* Find your  device, and set
* If you cannot find it, make sure you have a  device, save and edit again

## Starting the client
You can start it once the virtual machine is set up and running with:

 $ looking-glass-client

If you do not want to use Spice to control the guest mouse and keyboard you can disable the Spice server:

 $ looking-glass-client -s

Additionally you may want to start Looking Glass Client in full screen, otherwise the image may be scaled down resulting in poor image fidelity.

 $ looking-glass-client -F

To inhibit your host's screensaver start Looking Glass with the  flag.

 $ looking-glass-client -S

This does not work on some DEs, including KDE. The issue with KDE is likely related to [https://bugs.kde.org/show_bug.cgi?id=383575 this behaviour. To temporarily disable the host's screensaver while using Looking Glass and KDE you can wrap Looking Glass in the following script:

Launch with the  option for further information.

## Configuring the client
The client loads configuration files from the following locations by default:

*

*

*  (usually )

All configuration files are loaded in order. Duplicate entries override earlier ones. This means you can set a system-wide configuration in , and override specific options for just your user in , which is overlayed on top of the system-wide configuration.

When first launched, the client will create the folder  if it does not yet exist.

The format of config files is the commonly known INI format, for example:

## Additional information
Refer to the upstream documentation for further details.

## Swap peripherals to and from the Host
Looking Glass includes a Spice client in order to control mouse movement on the Windows guest. However this may have too much latency for certain applications, such as gaming. An alternative method is passing through specific USB devices for minimal latency. This allows for switching the devices between host and guest.

First create a  file for the device(s) you wish to pass-through, which libvirt will use to identify the device(s).

Replace Colon with the contents of the  command, specific to the device(s) you want to pass-through.

As an example, assume a mouse you want to pass through is . You would replace  with 1532, and  with 0037.

Repeat this process for any additional USB devices you want to pass-through. If your mouse/keyboard has multiple entries in  (perhaps if it is wireless) then create additional XML files for each.

Next a sh script file is needed to tell libvirt what to attach/detach the USB devices to the guest.

Replace with the name of your virtual machine, which can be seen under virt-manager. Additionally replace [USBdevice with the full path to the  file for the device you wish to pass-through. Add additional lines for more than 1 device. For example:

Next, duplicate the script file and replace  with , so the devices are returned to the host after the virtual machine is powered down. Ensure all scripts are executable.

These 2 script files can now be executed to attach or detach your USB devices from the host to the guest virtual machine. It is important to note that they may need to be executed as root. To run the script from the Windows virtual machine, one possibility is using PuTTY to SSH into the host, and execute the script. On Windows PuTTY comes with plink.exe which can execute singular commands over SSH before then logging out, instead of opening a SSH terminal, all in the background.

Replace  with the Host IP Address and $ROOTPASSWORD with the root password.

You may also want to execute the script files using key binds. On Windows one option is Autohotkey, and on the Host Xbindkeys. Because of the need to run the scripts as root, you may also need to use Polkit or Sudo, which can both be used to authenticate specific executables as able to run as root without needing a password.

## Bypassing the IOMMU groups (ACS override patch)
If you find your PCI devices grouped among others that you do not wish to pass through, you may be able to separate them using Alex Williamson's ACS override patch. Make sure you understand the potential risk of doing so.

You will need a kernel with the patch applied. The easiest method to acquiring this is through the  or  package.

In addition, the ACS override patch needs to be enabled with kernel command line options.  The patch file adds the following documentation:

 pcie_acs_override =
         Override missing PCIe ACS support for:
     downstream
         All downstream ports - full ACS capabilties
     multifunction
         All multifunction devices - multifunction ACS subset
     id:nnnn:nnnn
         Specfic device - full ACS capabilities
         Specified as vid:did (vendor/device ID) in hex

The option  should break up as many devices as possible.

After installation and configuration, reconfigure your kernel parameters to load the new kernel with the  option enabled.

## Plain QEMU without libvirt
Instead of setting up a virtual machine with the help of libvirt, plain QEMU commands with custom parameters can be used for running the virtual machine intended to be used with PCI passthrough. This is desirable for some use cases like scripted setups, where the flexibility for usage with other scripts is needed.

To achieve this after #Setting up IOMMU and #Isolating the GPU, follow the QEMU article to setup the virtualized environment, enable KVM on it and use the flag  replacing the identifier (07:00.0) with your actual device's ID that you used for the GPU isolation earlier.

For utilizing the OVMF firmware, make sure the  package is installed, copy the UEFI variables from  to temporary location like  and finally specify the OVMF paths by appending the following parameters to the QEMU command (order matters):

*  for the actual OVMF firmware binary, note the readonly option
*  for the variables

It is recommended to study the QEMU article for ways to enhance the performance by using the virtio drivers and other further configurations for the setup.

You also might have to use the  parameter to forward the host's CPU model info to the virtual machine and fool the virtualization detection used by Nvidia's and possibly other manufacturers' device drivers trying to block the full hardware usage inside a virtualized system.

## Passing through other devices
## USB controller
If your motherboard has multiple USB controllers mapped to multiple groups, it is possible to pass those instead of USB devices. Passing an actual controller over an individual USB device provides the following advantages :

* If a device disconnects or changes ID over the course of an given operation (such as a phone undergoing an update), the virtual machine will not suddenly stop seeing it.
* Any USB port managed by this controller is directly handled by the virtual machine and can have its devices unplugged, replugged and changed without having to notify the hypervisor.
* Libvirt will not complain if one of the USB devices you usually pass to the guest is missing when starting the virtual machine.

Unlike with GPUs, drivers for most USB controllers do not require any specific configuration to work on a virtual machine and control can normally be passed back and forth between the host and guest systems with no side effects.

You can find out which USB devices correspond to which controller and how various ports and devices are assigned to each one of them using this command:

{{hc|1=$ for usb_ctrl in /sys/bus/pci/devices/*/usb*; do pci_path=${usb_ctrl%/*}; iommu_group=$(readlink $pci_path/iommu_group); echo "Bus $(cat $usb_ctrl/busnum) --> ${pci_path##*/} (IOMMU group ${iommu_group##*/})"; lsusb -s ${usb_ctrl#*/usb}:; echo; done|2=
Bus 1 --> 0000:00:1a.0 (IOMMU group 4)
Bus 001 Device 004: ID 04f2:b217 Chicony Electronics Co., Ltd Lenovo Integrated Camera (0.3MP)
Bus 001 Device 007: ID 0a5c:21e6 Broadcom Corp. BCM20702 Bluetooth 4.0 [ThinkPad
Bus 001 Device 008: ID 0781:5530 SanDisk Corp. Cruzer
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Bus 2 --> 0000:00:1d.0 (IOMMU group 9)
Bus 002 Device 006: ID 0451:e012 Texas Instruments, Inc. TI-Nspire Calculator
Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
}}

This laptop has 3 USB ports managed by 2 USB controllers, each with their own IOMMU group. In this example, Bus 001 manages a single USB port (with a SanDisk USB pendrive plugged into it so it appears on the list), but also a number of internal devices, such as the internal webcam and the bluetooth card. Bus 002, on the other hand, does not apprear to manage anything except for the calculator that is plugged into it. The third port is empty, which is why it does not show up on the list, but is actually managed by Bus 002.

Once you have identified which controller manages which ports by plugging various devices into them and decided which one you want to passthrough, simply add it to the list of PCI host devices controlled by the virtual machine in your guest configuration. No other configuration should be needed.

## Passing audio from virtual machine to host via PipeWire directly
This is preferable to passing audio to the pipewire's pulseaudio emulation layer.

(Please change the runtimeDir value from 1000 accordingly to your desktop user uid)

To resolve 'Failed to initialize PW context' error you can modify the qemu configuration to use your user.

## Passing audio from virtual machine to host via PulseAudio
It is possible to route the virtual machine's audio to the host as an application using libvirt. This has the advantage of multiple audio streams being routable to one host output, and working with audio output devices that do not support passthrough. This requires PulseAudio to be running on the host system.

First, install .

Then, remove the comment from the  line. Then add your username in the quotations. This tells QEMU which user's pulseaudio stream to route through.

An emulated audio setup consists of two components: An emulated sound device exposed to the guest and an audio backend connecting the sound device to the host's PulseAudio.

Of the emulated sound devices available, two are of main interest: ICH9 and usb-audio. ICH9 features both output and input but is limited to stereo. usb-audio only features audio output but supports up to 6 channels in 5.1 configuration. For ICH9 remove any pre-existing audio backend in the  section and add:

Note the matching  elements. The example above assumes a single-user system with user ID 1000. Use the  command to find the correct ID. You can also use the  directory if you have multiple users accessing PulseAudio:

If you get crackling or distorted sound, try experimenting with some latency settings. The following example uses 20000 microseconds:

You can also try disabling the software mixer included in QEMU. This should, in theory, be more efficient and allow for lower latencies since mixing will then take place on your host only:

For usb-audio, the corresponding elements read

However, if a 5.1 configuration is required the sound device needs to be configured via QEMU command line arguments:

The  tag has to be set to match the audio backend's  element.  corresponds to  and so on.

## Passing audio from virtual machine to host via JACK and PipeWire
It is also possible to pass the virtual machine's audio to the host via JACK and PipeWire.

First, make sure you have a working PipeWire setup with JACK support.

Next, you will need to tell libvirt to run QEMU as your user:

Do not forget to restart .

As a final preparation, the XML scheme has to be extended to allow passing of environment variables. For this, modify the virtual machine domain configuration

to

Then, you can add the actual audio config to your virtual machine:

Note the matching  elements. Above's example assumes a single-user system with user ID 1000. Use the  command to find the correct ID.

You might have to play with the  values to get to the desired latency without crackling.

## Passing audio from virtual machine to host via Scream
It is possible to pass the virtual machine's audio through a bridged network such as the one provided by Libvirt or by adding a IVSHMEM device to the host by using a application called Scream. This section will only cover using PulseAudio as a receiver on the host.
See the project page for more details and instructions on other methods.

## Using Scream with a bridged network
To use scream via your network you will want to find your bridge name via , in most cases it will be called br0 or virbr0. Below is a example of the command needed to start the Scream application:

 $ scream -o pulse -i virbr0 &

## Adding the IVSHMEM device to use Scream with IVSHMEM
With the virtual machine turned off, edit the machine configuration

In the above configuration, the size of the IVSHMEM device is 2MB (the recommended amount). Change this as needed.

Now refer to #Adding IVSHMEM Device to virtual machines to configure the host to create the shared memory file on boot, replacing  with .

## Configuring the Windows guest for IVSHMEM
The correct driver must be installed for the IVSHMEM device on the guest.
See #Installing the IVSHMEM Host to Windows guest. Ignore the part about .

Install the Scream virtual audio driver on the guest.
If you have secure boot enabled for your virtual machine, you may need to disable it.

Using the registry editor, set the DWORD  to the size of the IVSHMEM device in MB.
Note that scream identifies its IVSHMEM device using its size, so make sure there is only one device of that size (the suggested default is  for 2MB).

Use the following command in an admin CMD shell to create both key and DWORD:  (sourced from scream on Github)

## Configuring the host
Install .

Create a systemd user service to control the receiver:

Edit  with the size of the IVSHMEM device in MiB.

Now start the  user unit.

To have it automatically start on next login, enable the user unit.

## Physical disk/partition
Raw and qcow2 especially can have noticeable overhead for heavy IO. A whole disk or a partition may be used directly to bypass the filesystem and improve I/O performance. If you wish to dual boot the guest OS natively you would need to pass the entire disk without any partitioning. It is suggested to use /dev/disk/by- paths to refer to the disk since /dev/sdX entries can change between boots. To find out which disk/partition is associated with the one you would like to pass:

See #Virtio disk on how to add these with libvirt XML. You can also add the disk with Virt-Manager's Add Hardware menu and then type the disk you want in the Select or create custom storage box, e.g. /dev/disk/by-id/ata-ST1000LM002-9VQ14L_Z0501SZ9

## Gotchas
## Passing through a device that does not support resetting
When the virtual machine shuts down, all devices used by the guest are deinitialized by its OS in preparation for shutdown. In this state, those devices are no longer functional and must then be power-cycled before they can resume normal operation. Linux can handle this power-cycling on its own, but when a device has no known reset methods, it remains in this disabled state and becomes unavailable. Since Libvirt and Qemu both expect all host PCI devices to be ready to reattach to the host before completely stopping the virtual machine, when encountering a device that will not reset, they will hang in a "Shutting down" state where they will not be able to be restarted until the host system has been rebooted. It is therefore recommended to only pass through PCI devices which the kernel is able to reset, as evidenced by the presence of a  file in the PCI device sysfs node, such as .

The following bash command shows which devices can and cannot be reset.

This signals that the xHCI USB controller in 00:14.0 cannot be reset and will therefore stop the virtual machine from shutting down properly, while the integrated sound card in 00:1b.0 and the other two controllers in 00:1a.0 and 00:1d.0 do not share this problem and can be passed without issue.

## Complete setups and examples
For many reasons users may seek to see complete passthrough setup examples.

These examples offer a supplement to existing hardware compatibility lists. Additionally, if you have trouble configuring a certain mechanism in your setup, you might find these examples very valuable. Users there have described their setups in detail, and some have provided examples of their configuration files as well.

We encourage those who successfully build their system from this resource to help improve it by contributing their builds. Due to the many different hardware manufacturers involved, the seemingly significant lack of sufficient documentation, as well as other issues due to the nature of this process, community contributions are necessary.

## Troubleshooting
If your issue is not mentioned below, you may want to browse QEMU#Troubleshooting.

## Host unable to boot when intel_iommu is enabled
Adding  to the kenel parameters together with  may fix the issue.

## QEMU 4.0: Unable to load graphics drivers/BSOD/Graphics stutter after driver install using Q35
Starting with QEMU 4.0, the Q35 machine type changes the default  from  to  which breaks some guest devices, such as nVidia graphics (the driver fails to load / black screen / code 43 / graphics stutters, usually when mouse moving). Switch to full KVM mode instead by adding  under libvirt's  tag in your virtual machine configuration or by adding  in the  QEMU arg.

## QEMU 5.0: host-passthrough with kernel version 5.5 to 5.8.1 when using Zen 2 processors: Windows 10 BSOD loop 'KERNEL SECURITY CHECK FAILURE'
Starting with QEMU 5.0 virtual machines running on Zen 2 and newer kernels than 5.4 will cause a BSOD loop of: 'KERNEL SECURITY CHECK FAILURE'. This can be fixed by either updating to kernel version 5.8.2 or higher, or disabling STIBP:

    ...

    ...

This requires libvirt 6.5 or higher. On older versions, several workarounds exist:
* Switch CPU mode from  to . This only works on libvirt 6.4 or lower.
* Manually patch  in order to revert this commit.
* On qemu commandline, add  to the cpu flags string. This can also be invoked through libvirt via a  entry.

## "Error 43: Driver failed to load" with mobile (Optimus/max-q) nvidia GPUs
This error occurs because the Nvidia driver wants to check the status of the power supply. If no battery is present, the driver does not work. Whether Libvirt or QEMU, by default none of them provide the possibility to simulate a battery. This might also result in a reduced screen resolution and the Nvidia Desktop Manager refusing to load when right-clicking the desktop, saying it requires Windows 10, a compatible GPU and the Nvidia graphics driver.

You can however create and add a custom acpi table file to the virtual machine which will do the work.

First you have to create the custom acpi table file by saving the following file as SSDT1.dat (base64 encoded here):

Next you must add the processed file to the main domain of the virtual machine:

Make sure your XML file has the correct namespace in the  tag as visible above, otherwise the XML verification will fail.

Source

## "BAR 3: cannot reserve error in dmesg after starting virtual machine
With respect to [https://www.linuxquestions.org/questions/linux-kernel-70/kernel-fails-to-assign-memory-to-pcie-device-4175487043/ this article:

If you still have code 43 check dmesg for memory reservation errors after starting up your virtual machine, if you have similar it could be the case:

 vfio-pci 0000:09:00.0: BAR 3: cannot reserve 0xf0000000-0xf1ffffff 64bit pref

Find out a PCI Bridge your graphics card is connected to. This will give actual hierarchy of devices:

 $ lspci -t

Before starting the virtual machine run the following lines, replacing IDs with actual values from previous output.

 # echo 1 > /sys/bus/pci/devices/0000\:00\:03.1/remove
 # echo 1 > /sys/bus/pci/rescan

In addition try adding kernel parameter  which also helps with hotplugging issues.

## UEFI (OVMF) compatibility in VBIOS
With respect to this article:

Error 43 can be caused by the GPU's VBIOS without UEFI support. To check whenever your VBIOS supports it, you will have to use :

 $ git clone https://github.com/awilliam/rom-parser
 $ cd rom-parser && make

Dump the GPU VBIOS:

 # echo 1 > /sys/bus/pci/devices/0000:01:00.0/rom
 # cat /sys/bus/pci/devices/0000:01:00.0/rom > /tmp/image.rom
 # echo 0 > /sys/bus/pci/devices/0000:01:00.0/rom

And test it for compatibility:

To be UEFI compatible, you need a "type 3 (EFI)" in the result. If it is not there, try updating your GPU VBIOS. GPU manufacturers often share VBIOS upgrades on their support pages. A large database of known compatible and working VBIOSes (along with their UEFI compatibility status!) is available on TechPowerUp.

Updated VBIOS can be used in the virtual machine without flashing. To load it in QEMU:

 -device vfio-pci,host=07:00.0,......,romfile=/path/to/your/gpu/bios.bin \

And in libvirt:

One should compare VBIOS versions between host and guest systems using nvflash (Linux versions under Show more versions) or GPU-Z (in Windows guest). To check the currently loaded VBIOS:

And to check a given VBIOS file:

If the external ROM did not work as it should in the guest, you will have to flash the newer VBIOS image to the GPU. In some cases it is possible to create your own VBIOS image with UEFI support using GOPUpd tool, however this is risky and may result in GPU brick.

In order to avoid the irreparable damage to your graphics adapter it is necessary to unload the NVIDIA kernel driver first:

 # modprobe -r nvidia_modeset nvidia

Flashing the VBIOS can be done with:

 # ./nvflash romfile.bin

## Slowed down audio pumped through HDMI on the video card
For some users, the virtual machine's audio slows down/starts stuttering/becomes demonic after a while when it is pumped through HDMI on the video card. This usually also slows down graphics.
A possible solution consists of enabling MSI (Message Signaled-Based Interrupts) instead of the default (Line-Based Interrupts).

In order to check whether MSI is supported or enabled, run the following command as root:

 # lspci -vs $device | grep 'MSI:'

where `$device` is the card's address (e.g. `01:00.0`).

The output should be similar to:

 Capabilities: MSI: Enable- Count=1/1 Maskable- 64bit+

A  after  means MSI is supported, but not used by the virtual machine, while a  says that the virtual machine is using it.

The procedure to enable it is quite complex, instructions and an overview of the setting can be found [https://forums.guru3d.com/showthread.php?t=378044 here.

On a linux guest you can use modinfo to see if there is option to enable MSI (for example: "modinfo snd_hda_intel |grep msi"). If there is, one can enable it by adding the relevant option to a custom omdprobe file - in "/etc/modprobe.d/snd-hda-intel.conf" inserting "options snd-hda-intel enable_msi=1"

Other hints can be found on the lime-technology's wiki, or on this article on VFIO tips and tricks.

A UI tool called MSI Utility (FOSS Version 2) works with Windows 10 64-bit and simplifies the process.

In order to fix the issues enabling MSI on the 0 function of a nVidia card () was not enough; it will also be required to enable it on the other function () to fix the issue.

## No HDMI audio output on host when intel_iommu is enabled
If after enabling  the HDMI output device of Intel GPU becomes unusable on the host then setting the option  (i.e. ) might bring the audio back, please read iommu.html for details about setting .

## X does not start after enabling vfio_pci
This is related to the host GPU being detected as a secondary GPU, which causes X to fail/crash when it tries to load a driver for the guest GPU. To circumvent this, a Xorg configuration file specifying the BusID for the host GPU is required. The correct BusID can be acquired from  or the Xorg log Note that the value from the lspci output is hexadecimal and should be converted to decimal in the .conf file.

## Chromium ignores integrated graphics for acceleration
Chromium and friends will try to detect as many GPUs as they can in the system and pick which one is preferred (usually discrete NVIDIA/AMD graphics). It tries to pick a GPU by looking at PCI devices, not OpenGL renderers available in the system - the result is that Chromium may ignore the integrated GPU available for rendering and try to use the dedicated GPU bound to the  driver, and unusable on the host system, regardless of whenever a guest virtual machine is running or not. This results in software rendering being used (leading to higher CPU load, which may also result in choppy video playback, scrolling and general un-smoothness).

This can be fixed by explicitly telling Chromium which GPU you want to use.

## Virtual machine only uses one core
For some users, even if IOMMU is enabled and the core count is set to more than 1, the virtual machine still only uses one CPU core and thread. To solve this enable "Manually set CPU topology" in  and set it to the desirable amount of CPU sockets, cores and threads. Keep in mind that "Threads" refers to the thread count per CPU, not the total count.

## Passthrough seems to work but no output is displayed
Make sure if you are using virt-manager that UEFI firmware is selected for your virtual machine. Also, make sure you have passed the correct device to the virtual machine.

## Host lockup after virtual machine shutdown
This issue seems to primarily affect users running a Windows 10 guest and usually after the virtual machine has been run for a prolonged period of time: the host will experience multiple CPU core lockups (see [https://bbs.archlinux.org/viewtopic.php?id=206050&p=2). To fix this try enabling Message Signal Interrupts on the GPU passed through to the guest. A good guide for how to do this can be found in You can also download this application for windows here [https://github.com/TechtonicSoftware/MSIInturruptEnabler that should make the process easier.

## Host lockup if guest is left running during sleep
VFIO-enabled virtual machines tend to become unstable if left running through a sleep/wakeup cycle and have been known to cause the host machine to lockup when an attempt is then made to shut them down. In order to avoid this, one can simply prevent the host from going into sleep while the guest is running using the following libvirt hook script and systemd unit. The hook file needs executable permissions to work.

## Bluescreen at boot since Windows 10 1803
Since Windows 10 1803 there is a problem when you are using "host-passthrough" as cpu model. The machine cannot boot and is either boot looping or you get a bluescreen.
You can workaround this by:

 # echo 1 > /sys/module/kvm/parameters/ignore_msrs

To make it permanently you can create a modprobe file :

 options kvm ignore_msrs=1

To prevent clogging up dmesg with "ignored rdmsr" messages you can additionally add:

 options kvm report_ignored_msrs=0

## AMD Ryzen / BIOS updates (AGESA) yields "Error: internal error: Unknown PCI header type ‘127’"
AMD users have been experiencing breakage of their KVM setups after updating the BIOS on their motherboard. There is a kernel patch, (see Kernel/Arch build system for instruction on compiling kernels with custom patches) that can resolve the issue as of now (7/28/19), but this is not the first time AMD has made an error of this very nature, so take this into account if you are considering updating your BIOS in the future as a VFIO user.

## AMD GPU not resetting properly yielding "Error: internal error: Unknown PCI header type ‘127’" (Separate issue from the one above)
Passing through an AMD GPU may result into a problem known as the "AMD reset bug". Upon power cycling the guest, the GPU does not properly reset its state which causes the device to malfunction until the host is also rebooted. This is usually paired with a "code 43" driver error in a Windows guest, and the message "Error: internal error: Unknown PCI header type '127'" in the libvirt log on the host.

In the past, this meant having to use work-arounds to manually reset the GPU, or resorting to the use of kernel patches that were unlikely to land in upstream. Currently, the recommended solution that does not require patching of the kernel is to install  or  and making sure the 'vendor-reset' kernel module is loaded before booting the guest. For convenience, you can load the module automatically.

## Host crashes when hotplugging Nvidia card with USB
If attempting to hotplug an Nvidia card with a USB port, you may have to blacklist the  driver. Do this by adding the line  to .

## Host unable to boot and stuck in black screen after enabling vfio
If debug kernel messages during boot are enabled by adding with the  kernel parameters, you may see boot stuck with the last message similar to:

 vfio-pci 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=none

This can be mitigated by disconnecting the passed-through GPU from your monitor. You may reconnect the passed-through GPU to a monitor after the host has booted.

If you do not want to plug the cable in each time you boot the host. You can disable the framebuffer in your boot loader to bypass this message. For UEFI systems you can add  as a kernel parameter. For legacy support, use  instead or in conjunction. Note that doing this may cause issues with Xorg.

If you encounter problems with Xorg, the following solution may help (remember to substitute with your own values if needed).

## AER errors when passing through PCIe USB hub
In some cases passing through a PCIe USB hub, such as one connected to the guest GPU, might fail with AER errors similar to the following:

 kernel: pcieport 0000:00:01.1: AER: Uncorrected (Non-Fatal) error received: 0000:00:01.1
 kernel: pcieport 0000:00:01.1: AER: PCIe Bus Error: severity=Uncorrected (Non-Fatal), type=Transaction Layer, (Requester ID)
 kernel: pcieport 0000:00:01.1: AER:   device error status/mask=00100000/00000000
 kernel: pcieport 0000:00:01.1: AER:    [20 UnsupReq               (First)
 kernel: pcieport 0000:00:01.1: AER:   TLP Header: 00000000 00000000 00000000 00000000
 kernel: pcieport 0000:00:01.1: AER: device recovery successful

## Reserved Memory Region Reporting (RMRR) Conflict
If you run into an issue passing through a device because of the BIOS's usage of RMRR, like the error below.

 vfio-pci 0000:01:00.1: Device is ineligible for IOMMU domain attach due to platform RMRR requirement. Contact your platform vendor.

You can try the patches here: https://github.com/kiler129/relax-intel-rmrr

## Too-low frequency limit for AMD GPU passed-through to virtual machine
On some machines with AMD GPUs, binding the devices to vfio-pci may be insufficient to prevent interference from the host, since the amdgpu driver on the host may query global ATIF methods which can alter the behavior of the GPU. For example, a user with a Dell Precision 7540 laptop containing a Radon Pro WX 3200 AMD GPU reported that, with the AMD GPU bound to vfio-pci, the passed-through AMD GPU was limited to 501 MHz instead of the correct 1295 MHz limit. Blacklisting the amdgpu kernel module using the kernel command line was a workaround.

See this kernel mailing list discussion for further details.

## Host clocksource is HPET rather than TSC
If the clocksource of your host machine is HPET you may see severely crippled performance in games. While this issue also occurs when running games outside of a virtual machine, unaware users will likely begin troubleshooting their virtual machine when the issue is actually with their host system.

To see your current clocksource, run this command on your host machine:

 $ cat /sys/devices/system/clocksource/clocksource*/current_clocksource

If your clocksource is HPET you can try to force it to TSC by setting the kernel parameters  and . See this Reddit thread for more information.

## Code 43 while Resizable Bar is turned on in the bios
If you own a GPU that supports Resizable BAR / SAM and have the corresponding BIOS option enabled, you might get code 43 because this feature is disabled in QEMU Linux Kernel release 6.1 added option to manipulate PCIe Resizable BARs through sysfs, so you can try permanently resizing it using a udev rule:

{{hc|/etc/udev/rules.d/01-amd.rules|2=
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource0_resize}="14"
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource2_resize}="8"
}}

Alternatively, to temporarily resize the PCIe BAR, you can write the new size to , where device_address is the address of your GPU, such as  (note that for changing this parameter, no driver can be loaded for the device).

You can confirm values using .

AMD graphics processors may require a specific value to be set for BAR 2, which is 8 MB, even though the maximum supported value is 256 MB. However, this requirement may depend on several factors, such as the QEMU version on your system. If you have already exhausted other options to prevent error code 43, set the value to 3 in the  file, which will force BAR 2 to be set to 8 MB.

## Operating system hangs
If your virtualized OS (particularly Windows) hangs when the GPU is attached, you can also try opening your motherboard's settings and:

* disabling ,
* disabling ,
* enabling ,
* changing  from  to a specific value,
* switching your  from  to .

At the very least, VEGA cards seem to be picky about those settings and will not actually work unless you change them.

## GPU timeouts when running games in the virtual machine
Starting with recent kernels (6.12+ for AMD, 5.x for Intel), split lock detection is enabled by default. This causes a forced 10ms pause for the process creating the split lock which can result in GPU timeouts and similar virtual machine hanging. This behavior can be disabled by running:

 # sysctl -w kernel.split_lock_mitigate=0

## vfio: DMA mapping failed, unable to continue
When starting the virtual machine, an error like "qemu: hardware error: vfio: DMA mapping failed, unable to continue" may occur and prevent the virtual machine from booting. To fix this, add the following to the XML file: [https://github.com/tianocore/edk2/discussions/4662#discussioncomment-6541549

If directly using QEMU, the example above would be .

If the virtual machine still does not work, try decreasing the value (like 39 and 0x27, respectively).

You can use  to see the actual address size of your CPU and use it rather than the values shown above. Unless you need a large address space, it's safer to choose the physical address size intead of the virtual size.

## vIOMMU: Failed to set vIOMMU: aw-bits X > host aw-bits Y
When starting the virtual machine, an error like the following may occur:

 libvirt.libvirtError: internal error: QEMU unexpectedly closed the monitor (vm='win11'): 2025-08-30T21:38:26.333149Z qemu-system-x86_64: -device {"driver":"vfio-pci","host":"0000:03:00.0","id":"hostdev0","bus":"pci.5","addr":"0x0"}: vfio 0000:03:00.0: Failed to set vIOMMU: aw-bits 48 > host aw-bits 39

Add   to the following section in your XML. Usually on x86 the default is either 39 or 48 bits but you can use your own CPU's address size instead.

For more information:

* [https://forum.proxmox.com/threads/vm-wont-start-with-pci-passthrough-after-upgrade-to-9-0.169586/post-795732 Proxmox forum thread discussing this
* libvirt options

## The VM stucks during boot when using Looking Glass
Sometimes, when using Looking Glass, the virtual machine may get stuck indefinitely at the boot process This might be caused by divergences between P-Cores and E-Cores specs on new processors with hybrid architectures.

To solve this, follow these instructions. It's better to pick the physical address size instead of the virtual address size [https://www.reddit.com/r/VFIO/comments/16a8xzb/comment/le7obu0/.
