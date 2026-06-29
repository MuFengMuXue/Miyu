# PCI passthrough via OVMF/Troubleshooting

If your issue is not mentioned below, you may want to browse QEMU#Troubleshooting.

## QEMU 4.0: Unable to load graphics drivers/BSOD/Graphics stutter after driver install using Q35
Starting with QEMU 4.0, the Q35 machine type changes the default  from  to , which breaks some guest devices, such as NVIDIA graphics (the driver fails to load / black screen / code 43 / graphics stutters, usually when mouse moving).

Switch to full KVM mode instead by adding  under libvirt's  tag in your virtual machine configuration or by adding  in the  QEMU arg.

## QEMU 5.0: host-passthrough with kernel version 5.5 to 5.8.1 when using Zen 2 processors: Windows 10 BSOD loop 'KERNEL SECURITY CHECK FAILURE'
Starting with QEMU 5.0 virtual machines running on Zen 2 and kernels newer than 5.4 will cause a BSOD loop of: 'KERNEL SECURITY CHECK FAILURE'. This can be fixed by either updating to kernel version 5.8.2 or higher, or disabling STIBP:

    ...

    ...

This requires libvirt 6.5 or higher. On older versions, several workarounds exist:

* Switch CPU mode from  to . This only works on libvirt 6.4 or lower.
* Manually patch  in order to revert this commit.
* On qemu commandline, add  to the cpu flags string. This can also be invoked through libvirt via a  entry.

## "Error 43: Driver failed to load" with mobile (Optimus/max-q) NVIDIA GPUs
This error occurs because the NVIDIA driver wants to check the status of the power supply. If no battery is present, the driver does not work. Whether Libvirt or QEMU, by default none of them provide the possibility to simulate a battery. This might also result in a reduced screen resolution and the NVIDIA Desktop Manager refusing to load when right-clicking the desktop, saying it requires Windows 10, a compatible GPU and the NVIDIA graphics driver.

You can however create and add a custom acpi table file to the virtual machine which will do the work.

First you have to create the custom acpi table file by saving the following file as SSDT1.dat (base64 encoded here):

Next you must add the processed file to the main domain of the virtual machine:

Make sure your XML file has the correct namespace in the  tag as visible above, otherwise the XML verification will fail == "BAR 3: cannot reserve [mem" error in dmesg after starting virtual machine ==

With respect to this article:

If you still have code 43 check  for memory reservation errors after starting up your virtual machine, if you have similar it could be the case:

 vfio-pci 0000:09:00.0: BAR 3: cannot reserve 0xf0000000-0xf1ffffff 64bit pref

Find out a PCI Bridge your graphics card is connected to. This will give actual hierarchy of devices:

 $ lspci -t

Before starting the virtual machine run the following lines, replacing IDs with actual values from previous output.

 # echo 1 > /sys/bus/pci/devices/0000\:00\:03.1/remove
 # echo 1 > /sys/bus/pci/rescan

In addition try adding kernel parameter  which also helps with hotplugging issues.

## UEFI (OVMF) compatibility in VBIOS
With respect to this article:

Error 43 can be caused by the GPU's VBIOS without UEFI support. To check whenever your VBIOS supports it, you will have to use rom-parser:

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
A possible solution consists of enabling MSI (Message Signal-Based Interrupts) instead of the default (Line-Based Interrupts).

In order to check whether MSI is supported or enabled, run the following command as root:

 # lspci -vs device | grep 'MSI:'

where  is the GPU's PCI address (e.g. ).

The output should be similar to:

 Capabilities: MSI: Enable- Count=1/1 Maskable- 64bit+

A  after  means MSI is supported, but not used by the virtual machine, while a  says that the virtual machine is using it.

The procedure to enable it is quite complex, instructions and an overview of the setting can be found [https://forums.guru3d.com/showthread.php?t=378044 here.

On a Linux guest you can use  to see if there is option to enable MSI, for example:

 $ modinfo snd_hda_intel | grep msi

If there is, one can enable it by adding the relevant option to a custom modprobe.d file:

Other hints can be found on the lime-technology's wiki, or in this article.

A UI tool called MSI Utility (FOSS Version 2) works with Windows 10 64-bit and simplifies the process.

In order to fix the issues, enabling MSI on the  function of a NVIDIA card

 01:00.0 VGA compatible controller: NVIDIA Corporation GM206 GTX 960 (rev a1) (prog-if 00 controller)

is not enough; it will also be required to enable it on the other function

 01:00.1 Audio device: NVIDIA Corporation Device 0fba (rev a1)

to fix the issue.

## No HDMI audio output on host when intel_iommu is enabled
If after enabling  the HDMI output device of Intel GPU becomes unusable on the host, setting the kernel parameters  might bring the audio back. Please read iommu.html for details about setting .

## X does not start after enabling vfio_pci
This is related to the host GPU being detected as a secondary GPU, which causes X to fail/crash when it tries to load a driver for the guest GPU. To circumvent this, a Xorg configuration file specifying the BusID for the host GPU is required. The correct BusID can be acquired from  or the Xorg log Note that the value from the  output is hexadecimal and should be converted to decimal in the  file.

## Chromium ignores integrated graphics for acceleration
Chromium and friends will try to detect as many GPUs as they can in the system and pick which one is preferred (usually discrete NVIDIA/AMD graphics).

It tries to pick a GPU by looking at PCI devices, not OpenGL renderers available in the system. The result is that Chromium may ignore the integrated GPU available for rendering and try to use the dedicated GPU bound to the  driver (and unusable on the host system), regardless of whenever a guest virtual machine is running or not.

This results in software rendering being used (leading to higher CPU load, which may also result in choppy video playback, scrolling and general lack of smoothness).

This can be fixed by explicitly telling Chromium which GPU you want to use.

## Virtual machine only uses one core
For some users, even if IOMMU is enabled and the core count is set to more than , the virtual machine still only uses one CPU core and thread. To solve this enable "Manually set CPU topology" in virt-manager and set it to the desirable amount of CPU sockets, cores and threads. Keep in mind that "Threads" refers to the thread count per CPU core, not the total count.

## Passthrough seems to work but no output is displayed
If you are using virt-manager, ensure that UEFI firmware is selected for your virtual machine. Also, make sure you have passed the correct device to the virtual machine.

## Host lockup after virtual machine shutdown
This issue seems to primarily affect users running a Windows 10 guest and usually after the virtual machine has been run for a prolonged period of time: the host will experience multiple CPU core lockups (see [https://bbs.archlinux.org/viewtopic.php?id=206050&p=2).

To fix this try enabling Message Signal-Based Interrupts (MSI) on the GPU passed through to the guest. A good guide for how to do this can be found in You can also download this application for Windows here [https://github.com/TechtonicSoftware/MSIInturruptEnabler that should make the process easier.

## Host lockup if guest is left running during sleep
VFIO-enabled virtual machines tend to become unstable if left running through a sleep/wakeup cycle and have been known to cause the host machine to lockup when an attempt is then made to shut them down.

In order to avoid this, one can simply prevent the host from going into sleep while the guest is running using the following libvirt hook script and systemd unit. The hook file needs executable permissions to work.

## Bluescreen at boot since Windows 10 1803
Since Windows 10 1803, there is a problem when you are using "host-passthrough" as cpu model. The machine may be unable to boot and it either starts boot looping or you may get a BSOD.
You can workaround this by using the following kernel parameter:

 # echo 1 > /sys/module/kvm/parameters/ignore_msrs

To make it permanently you can create a modprobe.d file :

To prevent clogging up dmesg with "ignored rdmsr" messages you can additionally add:

 options kvm report_ignored_msrs=0

## AMD Ryzen / BIOS updates (AGESA) yields "Error: internal error: Unknown PCI header type ‘127’"
AMD users have been experiencing breakage of their KVM setups after updating the BIOS on their motherboard. There is a kernel patch, (see Kernel/Arch build system for instruction on compiling kernels with custom patches) that can resolve the issue as of now (28th July 2019), but this is not the first time AMD has made an error of this very nature, so take this into account if you are considering updating your BIOS in the future as a VFIO user.

## AMD GPU not resetting properly yielding "Error: internal error: Unknown PCI header type ‘127’" (Separate issue from the one above)
Passing through an AMD GPU may result into a problem known as the "AMD reset bug". Upon power cycling the guest, the GPU does not properly reset its state, which causes the device to malfunction until the host is also rebooted. This is usually paired with a  driver error in a Windows guest, and the message  in the libvirt log on the host.

In the past, this meant having to use workarounds to manually reset the GPU, or resorting to the use of kernel patches that were unlikely to land in upstream.
Currently, the recommended solution that does not require patching of the kernel is to install  or  and making sure the  kernel module is loaded before booting the guest.

For convenience, you can load the module automatically, either at boot time or with a libvirt hook:

Make the file executable, if needed.

## Host crashes when hotplugging NVIDIA card with USB
If attempting to hotplug an NVIDIA card with a USB port, you may have to blacklist the  driver. You can achieve this by creating a modprobe.d file:

## Host unable to boot and stuck in black screen after enabling vfio
If debug kernel messages during boot are enabled by adding with the  kernel parameters, you may see boot stuck with the last message similar to:

 vfio-pci 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=none

This can be mitigated by disconnecting the passed-through GPU from your monitor. You may reconnect the passed-through GPU to a monitor after the host has booted.

If you do not want to plug the cable in each time you boot the host, you can disable the framebuffer in your boot loader to bypass this message. For UEFI systems you can add  as a kernel parameter. For legacy support, use  instead or in conjunction. Note that doing this may cause issues with Xorg.

If you encounter problems with Xorg, the following solution may help (remember to substitute with your own values):

## AER errors when passing through PCIe USB hub
In some cases, passing through a PCIe USB hub, such as one connected to the guest GPU, might fail with AER errors similar to the following:

 kernel: pcieport 0000:00:01.1: AER: Uncorrected (Non-Fatal) error received: 0000:00:01.1
 kernel: pcieport 0000:00:01.1: AER: PCIe Bus Error: severity=Uncorrected (Non-Fatal), type=Transaction Layer, (Requester ID)
 kernel: pcieport 0000:00:01.1: AER:   device error status/mask=00100000/00000000
 kernel: pcieport 0000:00:01.1: AER:    [20 UnsupReq               (First)
 kernel: pcieport 0000:00:01.1: AER:   TLP Header: 00000000 00000000 00000000 00000000
 kernel: pcieport 0000:00:01.1: AER: device recovery successful

## Reserved Memory Region Reporting (RMRR) Conflict
If you run into an issue passing through a device because of the BIOS's usage of RMRR, like the error below:

 vfio-pci 0000:01:00.1: Device is ineligible for IOMMU domain attach due to platform RMRR requirement. Contact your platform vendor.

You can try the patches here: == Too-low frequency limit for AMD GPU passed-through to virtual machine ==

On some machines with AMD GPUs, binding the devices to  may be insufficient to prevent interference from the host, since the amdgpu driver on the host may query global ATIF methods which can alter the behavior of the GPU.

For example, a user with a Dell Precision 7540 laptop containing a Radon Pro WX 3200 AMD GPU reported that, with the AMD GPU bound to , the passed-through AMD GPU was limited to  instead of the correct  limit. Blacklisting the amdgpu kernel module using the kernel command line was a workaround.

See [https://lore.kernel.org/regressions/092b825a-10ff-e197-18a1-d3e3a097b0e3@leemhuis.info/T/ this kernel mailing list discussion for further details.

## Host clocksource is HPET rather than TSC
If the clocksource of your host machine is HPET, you may see severely crippled performance in games. While this issue also occurs when running games outside of a virtual machine, unaware users will likely begin troubleshooting their virtual machine when the issue is actually with their host system.

To see your current clocksource, run this command on your host machine:

 $ cat /sys/devices/system/clocksource/clocksource*/current_clocksource

If your clocksource is HPET, you can try to force it to TSC by setting the kernel parameters  and . See this Reddit thread for more information.

## Code 43 while Resizable Bar is turned on in the bios
If you own a GPU that supports Resizable BAR / SAM and have the corresponding BIOS option enabled, you might get code 43 because this feature is disabled in QEMU Linux Kernel release 6.1 added option to manipulate PCIe Resizable BARs through sysfs, so you can try permanently resizing it using a udev rule:

{{hc|/etc/udev/rules.d/01-amd.rules|2=
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource0_resize}="14"
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x1002", ATTR{device}=="0x73bf", ATTR{resource2_resize}="8"
}}

Alternatively, to temporarily resize the PCIe BAR, you can write the new size to , where device_address is the address of your GPU, such as  (note that for changing this parameter, no driver can be loaded for the device).

You can confirm values using .

AMD graphics processors may require a specific value to be set for BAR 2, which is 8 MB, even though the maximum supported value is 256 MB. However, this requirement may depend on several factors, such as the QEMU version on your system. If you have already exhausted other options to prevent error code 43, set the value to  in the  file, which will force BAR 2 to be set to 8 MB.

## Operating system hangs
If your virtualized OS (particularly Windows) hangs when the GPU is attached, you can also try opening your motherboard's settings and:

* disabling ,
* disabling ,
* enabling ,
* changing  from  to a specific value,
* switching your  from  to .

At the very least, VEGA cards seem to be picky about those settings and won't actually work unless you change them.

## GPU timeouts when running games in the virtual machine
Starting with recent kernels (6.12+ for AMD, 5.x for Intel), split lock detection is enabled by default. This causes a forced 10ms pause for the process creating the split lock, which can result in GPU timeouts and similar virtual machine hanging. This behavior can be disabled by running:

 # sysctl -w kernel.split_lock_mitigate=0

This can be applied automatically with a sysctl configuration file:

## vfio: DMA mapping failed, unable to continue
When starting the virtual machine, an error like  may occur and prevent the VM from booting. To fix this, add the following to the XML file: [https://github.com/tianocore/edk2/discussions/4662#discussioncomment-6541549

If directly using QEMU, the example above would be .

If the VM still doesn't work, try decreasing the value (like 39 and 0x27, respectively).

You can use  to see the actual address size of your CPU and use it rather than the values shown above. Unless you need a large address space, it's safer to choose the physical address size intead of the virtual size.

## vIOMMU: Failed to set vIOMMU: aw-bits X > host aw-bits Y
When starting the virtual machine, an error like the following may occur:

 libvirt.libvirtError: internal error: QEMU unexpectedly closed the monitor (vm='win11'): 2025-08-30T21:38:26.333149Z qemu-system-x86_64: -device {"driver":"vfio-pci","host":"0000:03:00.0","id":"hostdev0","bus":"pci.5","addr":"0x0"}: vfio 0000:03:00.0: Failed to set vIOMMU: aw-bits 48 > host aw-bits 39

Add   to the following section in your XML. Usually on x86 the default is either 39 or 48 bits but you can use your own CPU's address size instead.

For more information:

* [https://forum.proxmox.com/threads/vm-wont-start-with-pci-passthrough-after-upgrade-to-9-0.169586/post-795732 Proxmox forum thread discussing this
* libvirt options

## The VM stucks during boot when using Looking Glass
Sometimes, when using Looking Glass, the VM may get stuck indefinitely at the boot process This might be caused by divergences between P-Core and E-Core specs on new processors with hybrid architectures.

To solve this, follow these instructions. It's better to pick the physical address size instead of the virtual address size [https://www.reddit.com/r/VFIO/comments/16a8xzb/comment/le7obu0/.
