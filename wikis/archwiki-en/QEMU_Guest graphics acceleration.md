# QEMU/Guest graphics acceleration

There are multiple methods for virtual machine graphics display which yield greatly accelerated or near bare metal performance.

## QXL video driver and SPICE client for display
QXL/SPICE is a high-performance display method. However, it is not designed to offer near-bare metal performance.

## PCI GPU passthrough
## PCI VGA/GPU passthrough via OVMF
PCI passthrough currently seems to be the most popular method for optimal performance. This forum thread (now closed, and may be outdated) may be of interest for problem solving. You can use kvm switch to control desktops.

## Single GPU passthrough
Currently, PCI passthrough works for multiple graphics cards only. However, there is a workaround for passing a single graphics card. The problem with this approach is that you have to detach the graphics card from the host and use ssh to control the host from the guest.

When you start the virtual machine, all your GUI apps will be force terminated. However, as a workaround, you can use Xpra to detach to another Display before starting the virtual machine and reattach the Apps to display after shutting down the virtual machine.

If you have NVIDIA GPU, you may need to dump your GPU's vBIOS using  and patch it using vBIOS Patcher.

## Looking Glass
There is a fairly recent passthrough method called Looking Glass. See this guide to getting started, which provides some problem solving and user support. Looking Glass uses DXGI (MS DirectX Graphics Infrastructure) to pass complete frames captured from the virtual machine's passed-through video card, via shared memory, to the host system, where they are read (scraped) by a display client running on the bare-metal host.

Installation and configuration instructions may be found in PCI passthrough via OVMF#Using Looking Glass to stream guest screen to the host.

## GPU virtualization
## LIBVF.IO
LibVF.IO is a Virtualization Framework (Libvirt's alternative) for simplifying the GPU Virtualization. It supports Intel (Intel GVT-g, SR-IOV), NVIDIA (NVIDIA vGPU, SR-IOV) and AMD (AMD SR-IOV). You have to create YAML configurations for each virtual machine. Currently, Intel and NVIDIA GPUs are tested, with limited support for AMD. You can follow this setup guide. You can also check their Wiki. For NVIDIA, you need to unlock the vGPU, see #NVIDIA vGPU and putting it in LIBVF.IO's Optional Folder.

There is also LIME (LIME Is Mediated Emulation) for executing Windows programs in Linux.

This framework was tested for gaming. By default, LibVF.IO uses Looking Glass as Virtual Display but you can change that through YAML configuration.

## NVIDIA vGPU
By default, NVIDIA disabled the vGPU for consumer series (if you own an enterprise card go ahead). However, you can unlock vGPU for your consumer card.

You will also need a vGPU license, though there are some workarounds.

Follow this guide to manually setup a Windows 10 guest with NVIDIA vGPU.

## SR-IOV
Single Root I/O Virtualization is under development by Intel and NVIDIA New GPU Series. There are some AMD GPUs that support this technology such as the W7100.

## Intel i915
The mainline Linux kernel does not yet support the feature, and you will have to install a custom kernel from Intel (also see this GitHub issue for the current status on the mainlining efforts). There is also an i915 DKMS kernel module  to simplify the process (also see i915-sriov-dkms documentation for more information).

To enable the feature on the host you will have to :
* setup IOMMU
* enable GuC
* proceed to #Enabling virtual functions

## Intel Xe
Intel GPUs based on Xe architecture and newer have SR-IOV with the mainline Xe kernel module.

To enable it on the host :
* setup IOMMU
* first test the new experimental Xe driver to check compatibility
* proceed to #Enabling virtual functions

## Enabling Intel i915/Xe virtual functions
* add  or  (depending on your driver) kernel parameter where 7 is the maximum number of virtual function you will create
* edit (if you used the  module) or create the file  to create the virtual functions on boot :
 w /sys/devices/pci0000:00/0000:00:02.0/sriov_numvfs -    -    -    -   7
Don't forget to change  with the number of virtual functions you need.

Don't forget to restart for changes on kernel and kernel parameters to take effect.

You can verify that you virtual functions have been created with . If so, you can then use regular PCI Passthrough on the virtual functions and proceed to #Guest setup.

You might want to disable the GPU virtual functions on the host to avoid conflict between host and guest (also see i915-sriov-dkms documentation blocking VFs.

## Guest setup
* For Xe driver on Linux Guests you will need to enable enable GuC and force probe the Xe driver.
* For i915 driver on Linux guests you will also need to have the supporting i915 module installed using either the intel-lts kernel or . You will also need to enable GuC.
* For Windows guests you must install the latest drivers and set the hypervisor's vendor ID to .

## Intel-specific iGVT-g extension
iGVT-g is limited to integrated Intel graphics on past Intel CPUs (starting from Broadwell and ending with Comet Lake). This is a "software workaround" for older iGPUs that do not support SR-IOV Newer Intel iGPUs can use SR-IOV instead. For more information, see Intel GVT-g.

## Virgil3d virtio-gpu paravirtualized device driver
[https://docs.mesa3d.org/drivers/virgl.html virtio-gpu is a paravirtualized 3d accelerated graphics driver, similar to non-graphics virtio drivers (see virtio driver information and virtio Windows guest drivers). For Linux guests, virtio-gpu is fairly mature, having been available since Linux kernel version 4.4 and QEMU version 2.6. See this Reddit Arch thread and Gerd Hoffmann's blog for using this with libvirt and spice.

For Windows guests, there's currently an active work in progress on a fully functional OpenGL and Direct3D10 driver on the main GitHub repo's pull request. There's also a report that Red Hat also previously worked on the OpenGL driver, including the project summary but abandoned it soon after. Other drivers include the DOD (Windows kernel) driver and the ICD (Windows userland) driver are available. In addition, see this Phoronix article and its comments.

Venus is a Virtio-GPU protocol for Vulkan command serialization. It is available since QEMU version 9.2.0 and Linux kernel version 6.13. See this Github Gist how to use it.
