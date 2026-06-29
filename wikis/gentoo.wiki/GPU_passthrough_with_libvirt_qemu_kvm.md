**GPU passthrough** is a technology that allows the Linux kernel to directly present an internal PCI GPU as-is for direct use by a virtual machine.

The device acts as if it were directly driven by the VM, and the VM detects the PCI device as if it were physically connected. GPU passthrough is also often known as IOMMU, although this is a bit of a misnomer, since the IOMMU is the hardware technology that provides this feature but also provides other features such as some protection from DMA attacks or ability to address 64-bit memory spaces with 32-bit addresses.

The most common application for GPU passthrough is gaming, since GPU passthrough allows a VM direct access to the graphics card with the end result of being able to play games with nearly the same performance as bare metal running the operating system.

**QEMU** (**Q**uick **EMU**lator) is a generic, open source hardware emulator and virtualization suite.

** Note**\
This article typically uses KVM as the accelerator of choice due to its GPL licensing and availability. Without KVM nearly all commands described here will still work (unless KVM specific).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [BIOS and UEFI firmware]](#BIOS_and_UEFI_firmware)
-   [[2] [Hardware]](#Hardware)
-   [[3] [EFI configuration]](#EFI_configuration)
-   [[4] [IOMMU]](#IOMMU)
    -   [[4.1] [IOMMU kernel configuration]](#IOMMU_kernel_configuration)
        -   [[4.1.1] [Editing the kernel parameters]](#Editing_the_kernel_parameters)
    -   [[4.2] [IOMMU groups]](#IOMMU_groups)
-   [[5] [VFIO]](#VFIO)
-   [[6] [libvirt]](#libvirt)
    -   [[6.1] [Windows]](#Windows)
        -   [[6.1.1] [Sound]](#Sound)
            -   [[6.1.1.1] [Passing audio from virtual machine to host via PipeWire directly]](#Passing_audio_from_virtual_machine_to_host_via_PipeWire_directly)
        -   [[6.1.2] [Input Devices]](#Input_Devices)
-   [[7] [QEMU]](#QEMU)
    -   [[7.1] [Minimal]](#Minimal)
    -   [[7.2] [Linux Guest]](#Linux_Guest)
    -   [[7.3] [Using Multiple Monitors]](#Using_Multiple_Monitors)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Code 12 / PCI Resource Allocation Errors in Guest]](#Code_12_.2F_PCI_Resource_Allocation_Errors_in_Guest)
        -   [[8.1.1] [Adjusting PCI Address of GPU inside Guest]](#Adjusting_PCI_Address_of_GPU_inside_Guest)
        -   [[8.1.2] [Switching Host to UEFI 64-bit PCI Resource Addressing]](#Switching_Host_to_UEFI_64-bit_PCI_Resource_Addressing)
        -   [[8.1.3] [Enabling 64-bit PCI Addressing in the Switching the TianoCore UEFI BIOS]](#Enabling_64-bit_PCI_Addressing_in_the_Switching_the_TianoCore_UEFI_BIOS)
    -   [[8.2] [Machine Does Not Boot into UEFI]](#Machine_Does_Not_Boot_into_UEFI)
    -   [[8.3] [Code 43 / nvidia-smi in Windows Guest Cannot Communicate with Nvidia Card]](#Code_43_.2F_nvidia-smi_in_Windows_Guest_Cannot_Communicate_with_Nvidia_Card)
    -   [[8.4] [Hangs during Benchmarks (e.g., 3DMark)]](#Hangs_during_Benchmarks_.28e.g..2C_3DMark.29)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Installation]

### [BIOS and UEFI firmware]

In order to utilize KVM either VT-x or AMD-V must be supported by the processor. VT-x or AMD-V are Intel and AMD\'s respective technologies for permitting multiple operating systems to concurrently execute operations on the processors.

To inspect hardware for virtualization support issue the following command:

`user `[`$`]`grep --color -E "vmx|svm" /proc/cpuinfo`

For a period of time, manufacturers were shipping with virtualization turned off by default in the system BIOS.

## [Hardware]

-   A CPU that supports Intel VT-d or AMD-Vi. Check [List of compatible Intel CPUs (Intel VT-x and Intel VT-d)](https://ark.intel.com/Search/FeatureFilter?productType=processors&VTD=true).
-   A motherboard that supports the aforementioned technologies. To find this out, check in your motherboard\'s BIOS configuration for an option to enable IOMMU or something similar. Chances are that your motherboard will support it if it\'s from 2013 or newer, but make sure to check since this is a niche technology and some manufacturers may save costs by axing it from their motherboards or delivering a defective implementation (such as Gigabyte\'s 2015-2016 series) simply because NORPs never use it.
-   At least two GPUs: one for your physical OS, another for your VM. (You can in theory run your computer headless through SSH or a serial console, but it might not work and you risk locking the user away from your computer if done so).
-   Optional but recommended: Additional monitor, keyboard and mouse.

## [EFI configuration]

Go into BIOS (EFI) settings and turn on **VT-d** and **IOMMU** support.

** Note**\
**VT-d** and **Virtualization** configuration params are same

** Note**\
Some EFIs do not have **IOMMU** configuration settings

## [IOMMU]

IOMMU -- or input--output memory management unit -- is a memory management unit (MMU) that connects a direct-memory-access--capable (DMA-capable) I/O bus to the main memory. The IOMMU maps a device-visible virtual address (I/O virtual address or IOVA) to a physical memory address. In other words, it translates the IOVA into a real physical address.

In an ideal world, every device would have its own IOVA address space and no two devices would share the same IOVA. But in practice this is often not the case. Moreover, the PCI-Express (PCIe) specifications allow PCIe devices to communicate with each other directly, called peer-to-peer transactions, thereby escaping the IOMMU.

That is where PCI Access Control Services (ACS) come to the rescue. ACS is able to tell whether or not these peer-to-peer transactions are possible between any two or more devices, and can disable them. ACS features are implemented within the CPU and the chipset.

Unfortunately, the implementation of ACS varies greatly between different CPU or chip-set models.

### [IOMMU kernel configuration]

To enable IOMMU support in kernel:

[KERNEL]

    Device Drivers --->
      [*] IOMMU Hardware Support --->
                Generic IOMMU Pagetable Support ----
          [*]   AMD IOMMU support
          <*>     AMD IOMMU Version 2 driver
          [*]   Support for Intel IOMMU using DMA Remapping Devices
          [*]     Support for Shared Virtual Memory with Intel IOMMU
          [*]     Enable Intel DMA Remapping Devices by default
          [*]   Support for Interrupt Remapping

If the kernel has CONFIG_TRIM_UNUSED_KSYMS (Trim unused exported kernel symbols) enabled, then there will be a need to whitelist some symbols. Otherwise, error messages of the form [Failed to add group \<n\> to KVM VFIO device: Invalid argument] may occur. See the gentoo forum thread [kernel 4.7.0 breaks pci passthrough \[SOLVED\]](https://forums.gentoo.org/viewtopic-t-1049040-start-0.html) and the kvm mailing list thread [KVM/VFIO passthrough not working when TRIM_UNUSED_KSYMS is enabled](https://lore.kernel.org/kvm/13e90f87-9062-a7e4-99c0-5c6f5c16cad2@gmail.com/) (list of symbols to whitelist in the [second post](https://lore.kernel.org/kvm/a43675ef-197d-2bd5-9505-200ac439df6c@redhat.com/)).

[KERNEL]

    [*] Enable loadable module support --->
        [*]   Trim unused exported kernel symbols
        (/path/to/whitelist) Whitelist of symbols to keep in ksymtab

[FILE] **`/path/to/whitelist`**

    vfio_group_get_external_user
    vfio_external_group_match_file
    vfio_group_put_external_user
    vfio_group_set_kvm
    vfio_external_check_extension
    vfio_external_user_iommu_id
    mdev_get_iommu_device
    mdev_bus_type

Rebuild the kernel.

#### [Editing the kernel parameters]

Now, to enable IOMMU in the kernel, you must enable several kernel command-line parameters. Please add the parameters `iommu=pt intel_iommu=on pcie_acs_override=downstream,multifunction` to your bootloader\'s configuration file or your [/etc/kernel/cmdline].

Then, rebuild the configuration if on GRUB, build a new UKI if you use [unified kernel images](https://wiki.gentoo.org/wiki/Unified_kernel_image "Unified kernel image"), or whatever procedure must be done for your bootloader to ensure the new kernel parameters are going to be used.

** Note**\
If the system hangs after rebooting, check the UEFI\\BIOS IOMMU settings.

Verify IOMMU has been enabled and is operational:

`user `[`$`]`dmesg | grep 'IOMMU enabled'`

    [    0.000000] DMAR: IOMMU enabled

** Note**\
For CPUs on the XEN architecture, run:

`user `[`$`]`lspci -vv | grep -i 'Access Control Services'`

### [IOMMU groups]

Passing through PCI or VGA devices requires you to pass through all devices within an IOMMU group. The exception to this rule is PCI root devices that reside in the same IOMMU group with the device(s) we want to pass through. These root devices cannot be passed through as they often perform important tasks for the host. A number of (Intel) CPUs, usually consumer-grade CPUs with integrated graphics (IGD), share a root device in the same IOMMU group as the first PCIe 16x slot.

`user `[`$`]`for d in /sys/kernel/iommu_groups/*/devices/*; do n=$; n=$; printf 'IOMMU Group %s ' "$n"; lspci -nns "$"; done;`

    ...

    IOMMU Group 13 01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP104 [GeForce GTX 1080] [10de:1b80] (rev a1)

    IOMMU Group 15 02:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon Pro WX 7100] [1002:67c4]

    IOMMU Group 16 02:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580] [1002:aaf0]

    ...

Nvidia in IOMMU Group 13 and AMD Video Card in IOMMU group 15 and 16. Everything looks fine. But if you have buggy IOMMU support and all devices within one IOMMU group, hardware can\'t guarantee good device isolation. Unfortunately, it is not possible to fix that. The only workaround is to use ACS override patch which ignores the IOMMU hardware check. See [ACS override patch (Arch Wiki)](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF#Bypassing_the_IOMMU_groups_%28ACS_override_patch%29).

## [VFIO]

Kernel drivers:

[KERNEL]

    Device Drivers --->
      <M> VFIO Non-Privileged userpsace driver framework --->
          [*]   VFIO No-IOMMU support ----
          <M>   VFIO support for PCI devices
          [*]     VFIO PCI support for VGA devices
          < >   Mediated device driver framework

Search for VGA card IDs and audio device. Run:

`root `[`#`]`lspci -nn`

    ...
    04:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XL/XT [Radeon RX Vega 56/64] [1002:687f] (rev c1)
    04:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:aaf8]
    ..

\
Add PCI IDs for both VGA and audio to VFIO:

[FILE] **`/etc/modprobe.d/vfio.conf`**

    options vfio-pci ids=1002:687f,1002:aaf8

\
Loading KVM and VFIO kernel modules at boot (systemd):

[FILE] **`/etc/modules-load.d/vfio-pci.conf`**

    vfio
    vfio_iommu_type1
    vfio_pci
    kvm
    kvm_intel

## [libvirt]

Ensure you have [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") installed. If you need SPICE or USB redirection support (which depends on SPICE), install [[[app-emulation/qemu\[spice,usbredir\]]](https://packages.gentoo.org/packages/app-emulation/qemu)[]].

### [Windows]

1.  Create a Windows 10/11 VM and install Windows as per usual with [virt-manager].
2.  Edit the VM in [virt-manager] (open the VM and then either click the \"light bulb\" icon or select \"View\" -\> \"Details\" from the menu).
3.  At the bottom left corner of the window, click the \"Add Hardware\" button. (If you don\'t see buttons at the bottom of the screen, ensure your host screen resolution is higher than 1024x768).
4.  Select \"PCI Host Device\" from the left side.
5.  Locate the graphics card device(s) you exported via VFIO earlier (e.g., \"NVIDIA Corporation GM200GL \[Tesla M40\]\", \"AMD/ATI Vega 64\", or \"AMD/ATI Device\"). AMD GPUs have two devices on the PCIe bus, one with video and one with audio output. Windows drivers will only work if both of them are passed to Windows.
6.  Click the \"Finish\" button.
7.  Click the \"Apply\" button.
8.  Attempt to boot the VM.
9.  Inside Windows: open Device Manager to confirm that the device is appearing.
10. Install the appropriate graphics drivers.

If booting is unsuccessful or drivers don\'t load in Windows with an error code like 12 or 34, see \"Troubleshooting\" section at the bottom of this document.

#### [Sound]

`root `[`#`]`mkdir /home/qemu `

`root `[`#`]`cp /home/<user>/.config/pulse /home/qemu `

`root `[`#`]`chown qemu:qemu -R /home/qemu `

Change the home directory for the [qemu] user:

`root `[`#`]`usermod -d /home/qemu qemu`

##### [Passing audio from virtual machine to host via PipeWire directly]

[FILE] **`/etc/libvirt/qemu/.xml`**

    <audio id="1" type="pipewire" runtimeDir="/run/user/1000">
          <input name="qemuinput"/>
          <output name="qemuoutput"/>
        </audio>

#### [Input Devices]

One of the easiest ways of dealing with mouse and keyboard issues when using passthrough is through evdev proxy. This allows the ability to switch the mouse and keyboard between the guest and host with special key combinations. First, identify the mouse and keyboard in [/dev/input]. The easiest way to do this is through the symlink found in [/dev/input/by-id/].

`user `[`$`]`ls -l /dev/input/by-id/*-event-*`

This a list of symlinks to event devices limited to mouse and keyboard entries. In order to access these nodes, either add the user Qemu runs as in the input group or, if using libvirt, edit [/etc/libvirt/qemu.conf] looking for

[FILE] **`/etc/libvirt/qemu.conf`**

    cgroup_device_acl = [
    ...
    ]

Add the symlinks and then restart libvirtd. Next, edit the XML libvirt uses for the domain. Do this by either through [virsh] or using [virt-manager]. With [virt-manager], select the XML tab in the Overview option at the top of the device tree. With [virsh], enter interactive:

`user `[`$`]`virsh --connect qemu:///system`

    Welcome to virsh, the virtualization interactive terminal.

    Type:  'help' for help with commands
           'quit' to quit

`virsh #``list --all `

`virsh #``edit $DOMAIN`

Within the XML tree under the \<devices\> node, add the following lines

[CODE]

        <input type="evdev">
          <source dev="/dev/input/by-id/$YOURMOUSE-event-mouse"/>
        </input>
        <input type="evdev">
          <source dev="/dev/input/by-id/$YOURKEYBOARD-event-kbd" grab="all" repeat="on"/>
        </input>

By default, the key combination to change input between host and guest is both [Ctrl] keys. If multiple GPUs have been passed through to multiple VMs, use the grabToggle argument to change the combination to a fixed set of key combinations that can be found in [the Libvirt documentation](https://libvirt.org/formatdomain.html#input-devices).

## [QEMU]

In case someone wants to use QEMU directly, here are some configurations to get started. In general, as a typical QEMU call will usually require many command-line flags, it is typically advised to place the QEMU call in a bash script and to run it that way. Don\'t forget to make the script file executable!

### [Minimal]

This minimal configuration will simply boot into the BIOS - there aren\'t any drives connected, so there is nothing else for QEMU to do. However, this allows us to verify that the GPU passthrough is actually working.

[FILE] **`MinimalPassthrough.sh`**

    #!/bin/bash

    virsh nodedev-detach pci_0000_09_00_0
    virsh nodedev-detach pci_0000_09_00_1
    qemu-system-x86_64 \
        -nodefaults \
        -enable-kvm \
        -cpu host,kvm=off \
        -m 8G \
        -name "BlankVM" \
        -smp cores=4 \
        -device pcie-root-port,id=pcie.1,bus=pcie.0,addr=1c.0,slot=1,chassis=1,multifunction=on \
        -device vfio-pci,host=09:00.0,bus=pcie.1,addr=00.0,x-vga=on,multifunction=on,romfile=GP107_patched.rom \
        -device vfio-pci,host=09:00.1,bus=pcie.1,addr=00.1 \
        -monitor stdio \
        -nographic \
        -vga none \
        $@

    virsh nodedev-reattach pci_0000_09_00_0
    virsh nodedev-reattach pci_0000_09_00_1

Here\'s an explanation of each line:

1.  `-nodefaults` stops qemu from creating some default devices. Specifically, it creates a VGA device by default, which interferes with our attempt to pass through the video card (in a multi-video card host system this may not be an issue)
2.  `-enable-kvm` enables acceleration
3.  `-cpu host, kvm=off \` this makes the virtual machine match the CPU architecture of the host. `kvm=off` hides the KVM signature from the guest.
4.  `-m 8G` give the guest 8 gigabytes of RAM
5.  `-name "BlankVM"` Gives the virtual machine a name
6.  `-smp cores=4` how many cores the guest should have.
7.  `-device pcie-root-port,id=pcie.1...` a dedicate root port other than pcie.0 is required by amd gpu for windows driver
8.  `-device vfio-pci,host=09:00.0...` add a device using vfio-pci kernel module, from the host\'s address \"09:00.0\"
9.  `...addr=..` video must on .0 and audio on .1 while both video and audio must be on the same pci-root-port other than pcie.0
10. `...x-vga=on` this is an option for the vfio-pci module (citation needed)
11. `...multifunction=on` since our card is doing both audio and video, it needs multifunction
12. `...romfile=GP107_patched.rom` due to known issues on NVIDIA cards, it may be necessary to use a modified vbios. This is how you make qemu use that modified vbios.
13. `-device vfio-pci,host=09:00.1` just like above - this is the audio device that is in the same IOMMU group as the video device.
14. `-monitor stdio` this will drop you into a qemu \"command line\" (they call it a monitor) once you launch the VM, allowing you to do things.
15. `-vga none` this is probably redundant.

As noted above, there are certain known issues with NVIDIA drivers. I used [this tool](https://github.com/sk1080/nvidia-kvm-patcher) to patch my vbios, after first downloading my vbios in windows 10 using [this gpuz tool](https://www.techpowerup.com/gpuz/).

### [Linux Guest]

Here is a slightly more complicated qemu call, that actually loads a Gentoo VM.

[FILE] **`GentooPassthrough.sh`**

    #!/bin/bash

    exec qemu-system-x86_64 \
        -nodefaults \
        -enable-kvm \
        -cpu host,kvm=off,hv_vendor_id=1234567890ab \
        -m 8G \
        -name "Gentoo VM" \
        -smp cores=4 \
        -boot order=d \
        -drive file=Gentoo_VM.img,if=virtio \
        -monitor stdio \
        -serial none \
        -net nic \
        -net user,hostfwd=tcp::50000-:22,hostfwd=tcp::50001-:5900,hostname=gentoo_qemu \
        -nographic \
        -vga none \
        -device vfio-pci,host=09:00.0,x-vga=on,multifunction=on,romfile=GP107_patched.rom \
        -device vfio-pci,host=09:00.1 \
        -usb \
        -device usb-host,vendorid=0x1532,productid=0x0101,id=mouse \
        -device usb-host,vendorid=0x04f2,productid=0x0833,id=keyboard \
        $@

Here is an explanation of the new configuration options:

1.  `...hv_vendor_id=...` despite the patched vbios, the NVIDIA driver still recognized that it is being run in a virtual machine and refuses to load. This \"spoofs\" the vendor id (somewhere) and tricks the driver
2.  `-boot order=d` boot the hard drive first
3.  `-drive file=Gentoo_VM.img,if=virtio` this is a drive that is emulated in the VM. The \"Gentoo_VM.img\" file is a qcow QEMU-style virtual drive file.
4.  `-serial none` May no longer be required.
5.  `-net nic` create a Ethernet in the guest vm
6.  `-net user,hostfwd...` forwards the ports from host 50000 and 50001 to the guest ports 22 and 5900. Now, from the host, you can ssh into the guest using `ssh -p 50000 myuser@127.0.0.1`, and if a vnc server running in the guest on port 5900, it can access it using port 50001 in the host
7.  `-nographic` this may not be needed if you have a dedicated graphics card for the guest
8.  `-usb` emulate a USB device on the guest
9.  `-device usb-host,...` these two lines forward the keyboard and mouse from the host to the guest. The vendorid and productid can be found using [lsusb] in the host.

Please note that without the `hv_vendor_id` portion, a user can boot in and use the console in the guest with the forwarded graphics card. But whenever X is launch, which initialized the proprietary NVIDIA driver, it will fail.

\
The following example does not work with latest nvidia-drivers. The latest driver where it works for me is NVIDIA-Linux-x86_64-470.63.01.run. Here is a little variation of the above qemu script for Gentoo host and Gentoo guest. It uses separate CPUs for the guest. Works on a notebook with Ryzen CPU, where the 2nd NVIDIA GPU is passed through to the guest. The guest runs the NVIDIA driver. Installation is performed according to the Gentoo installation guide using UEFI and a GPT partition table. It uses no custom ROMs.

[FILE] **`gentooPassthrough.sh`**

    #!/bin/bash

    name=genpass
    pid="$"
    cpus="8-15"
    ncpus=8
    cgrouprootfs="/sys/fs/cgroup"
    cgroupfs="$/$"

    echo "PID: $"

    # using separate CPUs for VM
    # cgroup usage see https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
    # 'lscpu -e' to see which cpus to use
    echo "+cpuset" > $/cgroup.subtree_control
    mkdir -p $
    echo $ > $/cpuset.cpus
    echo "root" > $/cpuset.cpus.partition
    echo "$" > $/cgroup.procs

    # setting performance governor for QEMU CPUs
    for i in `seq 8 15` ; do
      echo performance >/sys/devices/system/cpu/cpu$/cpufreq/scaling_governor
    done

    qemu-system-x86_64 \
        -M q35 \
        -monitor stdio \
        -bios /usr/share/edk2-ovmf/OVMF_CODE.fd \
        -accel kvm,kernel-irqchip=on \
        -cpu host,kvm=off \
        -smp $ \
        -m 4G \
        -name "$" \
        -device vfio-pci,host=01:00.0,multifunction=on \
        -device vfio-pci,host=01:00.1 \
        -nographic \
        -vga none \
        -serial none \
        -parallel none \
        -hda hda.qcow2 \
        -usb \
        -device usb-host,vendorid=0x046D,productid=0xC52B \
        $@

    # removing cgroup cpuset
    echo "$" > $/cgroup.procs
    rmdir $

    # setting schedutil governor for qemu cpus
    for i in `seq 8 15` ; do
      echo schedutil >/sys/devices/system/cpu/cpu$/cpufreq/scaling_governor
    done

The kernel of the Gentoo host has been build with [genkernel \--virtio all]. The NVIDIA GPU has been bound to vfio-pci with [/etc/modprobe.d/local.conf] on the host:

[FILE] **`/etc/modprobe.d/local.conf`**

    alias pci:v000010DEd00001F95sv0000103Csd000087B2bc03sc00i00 vfio-pci
    alias pci:v000010DEd000010FAsv0000103Csd000087B2bc04sc03i00 vfio-pci
    options vfio-pci ids=10de:1f95,10de:10fa

This way the internal graphic of the Ryzen processor shows the host on the laptop display, Gentoo guest is displayed on the monitor connected to the HDMI of the NVIDIA graphic. To get sound in the VM, i have to replug the HDMI cable after the VM has booted. Maybe this issue is related to the HDMI cable or the external monitor.

### [Using Multiple Monitors]

An example setup is:

    980ti -> Gentoo Host

    1650 -> Kali VM

    3090 -> Windows 10 VM

This example uses six displays and often want to rotate between guests. If the monitors are able to auto switch to the active link then this will work. For example, to turn off the main display for Linux and switch to Windows use:

    xrandr --output $DISPLAY --off

If using a WM like i3, setting the hotkey that to \$mod4+shift+k. On Windows then it is possible to use the presentation settings to make the change back.

    <windows-key> + p, set secondary monitor

## [Troubleshooting]

### [][Code 12 / PCI Resource Allocation Errors in Guest]

You may find that after installing drivers for the GPU in your guest OS, the drivers do not load and the OS reports an error related to finding a large enough memory region or resources to allocate to the GPU. In a Windows guest, this is typically code 12 (\"This device cannot find enough free resources that it can use\") while in Linux it appears in [dmesg] output as errors like \"BAR XX: no space for \[mem size 0x600000000 64bit pref\]\" or \"BAR XX: failed to assign \[mem size 0x600000000 64bit pref\]\".

Potential causes for this issue include:

-   [virt-manager] has nested the GPU under a PCI bridge but the device and/or drivers require the GPU to be attached to the root PCI bridge.
-   Your host machine is not using UEFI mode, is using CSM/legacy boot mode, or is not using 64-bit PCI memory addressing (aka, \"Above 4g decoding\").
-   The TianoCore UEFI BIOS inside the guest is not using 64-bit addressing.

#### [Adjusting PCI Address of GPU inside Guest]

1.  Edit the VM in [virt-manager] (open the VM and then either click the \"light bulb\" icon or select \"View\" -\> \"Details\" from the menu).
2.  Select \"Overview\" on the left side of the window.
3.  In the tabs at the top of the right side of the window, select the \"XML\" tab to switch into the XML view of the guest.
4.  Locate the `<hostdev>` section(s) for your GPU (the `bus` and `slot` values inside the `source` tag should match the PCI address of your GPU). For example, the snippet for the GPU at `84:00.0` might look like this:

    :::
        <hostdev mode='subsystem' type='pci' managed='yes'>
          <source>
            <address domain='0x0000' bus='0x84' slot='0x00' function='0x0'/>
          </source>
          <address type='pci' domain='0x0000' bus='0x06' slot='0x0' function='0x0'/>
        </hostdev>
    :::
5.  Adjust the `bus` and `slot` attributes of the **second** `address` tag (the one outside the `source` tag) so that the `bus` becomes `0x0` and the `slot` does not conflict with the `slot` value of any other device having a `bus` of `0x0` elsewhere in the XML (a value of `0x10` is often, but not always, safe, if you have a guest with a lot of PCI bridges or other devices at the root).
6.  If your GPU has multiple devices (e.g., it\'s an ATI/AMD card), repeat steps 4 and 5 for each remaining GPU-related device, being sure to set the `bus` and `slot` of each device to the same value while leaving the `function` values (typically, `0x0`, `0x01`, and so on for each additional component of the GPU) alone.
7.  Click the \"Apply\" button.
8.  Confirm that your change to the `bus` and `slot` attributes of the `<hostdev>` section(s) have not been reverted. If they have been reverted, you inadvertently picked slot IDs that conflicted with other devices, and you will need to repeat steps 4-8 again with a different slot ID.
9.  Attempt to boot the guest VM.
10. Confirm that the PCI resource allocation errors no longer appear in the guest.

If you end up with a black screen (typically before even the TianoCode UEFI splash screen), proceed to the next two sections related to 64-bit PCI memory addressing.

#### [Switching Host to UEFI 64-bit PCI Resource Addressing]

** Note**\
If you originally setup Gentoo while in Legacy CSM mode, **you will need to reconfigure your partitions, kernel, and boot loader for EFI**. See the [Gentoo installation handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Preparing_for_a_bootloader "Handbook:AMD64/Installation/Base") for details.

Some GPUs (especially server GPUs like Tesla or Quadro data center GPUs) have so much on-board video RAM that they will not function without 64-bit PCI memory addressing, commonly known as \"Above 4g decoding\". Even on a 64-bit Intel-based system, your host BIOS might be configured to still allocate memory windows for all PCI devices within a 1 gigabyte \"hole\" at the high end of the first 4 gigabytes of your machine\'s memory space, for compatibility with older drivers and older operating systems that were written to work with PCI devices on 32-bit systems. This has no effect on the total RAM you can have in your machine, and when running a 64-bit operating system, it doesn\'t affect your ability to use all the RAM you\'ve installed, but it does affect the ability to use a GPU with 6+ GBs of VRAM since it\'s not possible to fit that VRAM within the small legacy PCI memory region.

To fix this, enter the UEFI BIOS of your host machine, and make sure that you are using the following settings:

-   **UEFI Boot:** Enabled.
-   **CSM Boot:** Disabled (some BIOSes may have you toggle between an EFI vs. CSM or \"Legacy\" boot mode; choose EFI).
-   **Above 4g Decoding:** Enabled (some BIOSes might call this \"64-bit BAR\" or \"64-bit PCI Addressing\").

If you\'ve confirmed that these settings are all correct but you are still not able to use the passed-through GPU, proceed to the next section.

#### [Enabling 64-bit PCI Addressing in the Switching the TianoCore UEFI BIOS]

If enabling 64-bit PCI addressing on the host wasn\'t sufficient to make the device function, it might also need to be enabled in the guest EFI bios. Unfortunately, even if you enter the TianoCore UEFI BIOS Setup, there does not appear to be a setting for this.

Luckily, the setting can be enabled through a snippet added to the guest XML:

1.  Edit the VM in [virt-manager] (open the VM and then either click the \"light bulb\" icon or select \"View\" -\> \"Details\" from the menu).
2.  Select \"Overview\" on the left side of the window.
3.  In the tabs at the top of the right side of the window, select the \"XML\" tab to switch into the XML view of the guest.
4.  At the top of the file, locate the `domain` tag.
5.  Add `xmlns:qemu='`[`http://libvirt.org/schemas/domain/qemu/1.0'`](http://libvirt.org/schemas/domain/qemu/1.0') to the end of the tag. For example, change:

    :::
        <domain type="kvm">
    :::

    To:

    :::
        <domain type="kvm" xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
    :::
6.  Add the following inside the `domain` tag:

    :::
        <qemu:commandline>
          <qemu:arg value='-fw_cfg'/>
          <qemu:arg value='opt/ovmf/X-PciMmio64Mb,string=65536'/>
        </qemu:commandline>
    :::
7.  Click the \"Apply\" button.
8.  Confirm that your changes have not been reverted. If they have been reverted, you may have a typo, and you will need to repeat steps 4-7 again.
9.  Attempt to boot the guest VM.
10. Confirm that the PCI resource allocation errors no longer appear in the guest.

### [Machine Does Not Boot into UEFI]

If you get only a black screen and not even the TianoCore UEFI boot splash before the guest OS loads, the GPU may require 64-bit PCI memory addressing to be enabled. Follow the steps in the [\"Enabling 64-bit PCI Addressing in the Switching the TianoCore UEFI BIOS\" section](#Enabling_64-bit_PCI_Addressing_in_the_Switching_the_TianoCore_UEFI_BIOS) above.

### [][Code 43 / `nvidia-smi` in Windows Guest Cannot Communicate with Nvidia Card]

You may find that after installing drivers for the GPU in Windows, the card fails to initialize and `nvidia-smi` fails to communicate with it. In a Windows guest, Device Manager will typically report code 43 (\"Windows has stopped this device because it has reported problems\") for this situation.

Potential causes for this issue include:

-   [Arch Wiki](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF#QEMU_4.0:_Unable_to_load_graphics_drivers/BSOD/Graphics_stutter_after_driver_install_using_Q35) indicates that sometimes it\'s necessary to add `<ioapic driver='kvm'/>` to the `features` section of the VM so that a KVM-native APIC implementation is used.
-   If you are using a datacenter card (e.g., a Tesla or Quadro) and have using `nvidia-smi` to toggle it into WDDM mode for use as a graphics card, you may still need to [make registry edits](https://www.reddit.com/r/pcmods/comments/nhfwh7/guide_using_an_nvidia_tesla_k80_datacenter_gpu/) to the device configuration so that the Nvidia drivers properly initialize the driver for graphics mode.

### [][Hangs during Benchmarks (e.g., 3DMark)]

Benchmark applications running in a Windows guest may rely on [high-precision timing features](https://bugzilla.redhat.com/show_bug.cgi?id=1789429) that aren\'t fully emulated by QEMU hardware, resulting in a crash when this functionality is accessed. This appears to manifest as the entire guest VM freezing and needing to be halted.

To fix this, you can enable several [\"Hyper-V enablements\"](https://www.qemu.org/docs/master/system/i386/hyperv.html) that make Windows believe it is running on Hyper-V rather than on hardware, enabling the Linux kernel to provide Windows with these features instead of expecting that they will be provided by the emulated hardware:

1.  Edit the VM in [virt-manager] (open the VM and then either click the \"light bulb\" icon or select \"View\" -\> \"Details\" from the menu).
2.  Select \"Overview\" on the left side of the window.
3.  In the tabs at the top of the right side of the window, select the \"XML\" tab to switch into the XML view of the guest.
4.  Locate the `hyperv` tag inside the `features` tag.
5.  Modify the contents of the `hyperv` tag to match the following:

    :::
        <hyperv mode='custom'>
          <relaxed state='on'/>
          <vapic state='on'/>
          <spinlocks state='on' retries='8191'/>
          <vpindex state='on'/>
          <runtime state='on'/>
          <synic state='on'/>
          <stimer state='on'>
            <direct state='on'/>
          </stimer>
          <reset state='off'/>
          <frequencies state='on'/>
          <reenlightenment state='on'/>
          <tlbflush state='on'/>
          <ipi state='on'/>
          <evmcs state='off'/>
        </hyperv>
    :::
6.  Click the \"Apply\" button.
7.  Confirm that your changes have not been reverted. If they have been reverted, you may have a typo, and you will need to repeat steps 4-7 again.
8.  Attempt to boot the guest VM.

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [Virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") --- lightweight GUI application designed for managing virtual machines and containers via the [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") API.
-   [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") --- a generic, open-source hardware emulator and virtualization suite.

## [External resources]

-   [https://heiko-sieger.info/iommu-groups-what-you-need-to-consider/#What_is_IOMMU_and_why_do_I_need_it](https://heiko-sieger.info/iommu-groups-what-you-need-to-consider/#What_is_IOMMU_and_why_do_I_need_it)
-   [https://wiki.installgentoo.com/index.php/PCI_passthrough](https://wiki.installgentoo.com/index.php/PCI_passthrough) - PCI passthrough on gentoo
-   [https://www.reddit.com/r/VFIO/comments/ahg1ta/bsod_when_launching_gpuz/](https://www.reddit.com/r/VFIO/comments/ahg1ta/bsod_when_launching_gpuz/)
-   [https://forum.level1techs.com/t/navi-reset-kernel-patch/147547](https://forum.level1techs.com/t/navi-reset-kernel-patch/147547)
-   [https://forum.level1techs.com/t/linux-host-windows-guest-gpu-passthrough-reinitialization-fix/121097?source_topic_id=121737](https://forum.level1techs.com/t/linux-host-windows-guest-gpu-passthrough-reinitialization-fix/121097?source_topic_id=121737) - AMD GPU on windows guest
-   [https://www.reddit.com/r/VFIO/comments/baa8e3/issue_unable_to_power_on_device_stuck_in_d3/](https://www.reddit.com/r/VFIO/comments/baa8e3/issue_unable_to_power_on_device_stuck_in_d3/)
-   [https://github.com/gnif/vendor-reset](https://github.com/gnif/vendor-reset)
-   [https://www.tsunderechen.io/2021/11/OVMF-PCIE-passthrough-with-large-VRAM-GPU/](https://www.tsunderechen.io/2021/11/OVMF-PCIE-passthrough-with-large-VRAM-GPU/)
-   [https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF) - Useful page to learn some of the more advanced configurations a VM can be set with.
-   [https://github.com/bryansteiner/gpu-passthrough-tutorial](https://github.com/bryansteiner/gpu-passthrough-tutorial) - Lots of screenshots of several steps of this process and even CPU + RAM optimization.