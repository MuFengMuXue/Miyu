GPU passthrough is a technology that allows the Linux kernel to directly present an internal PCI GPU to a virtual machine. It allows you to run a virtual machine with Linux or Windows 10+ with near native performance. In most cases this will be used for gaming or anything that requires GPU performance.

It is also known as IOMMU or VFIO and the best way to get a virtual machine running with GPU passthrough is by using QEMU.

In case of the Thinkpad P53 (and maybe other high end Thinkpads) it does work well due to the muxed GPU hardware and the decent IOMMU layout. The external HDMI port is directly wired to the Nvidia GPU while the internal Intel GPU will only output to the laptop display.

Since it is complicated enough already, this guide will only cover a basic setup for Thinkpad P53 series running Gentoo as host on the laptop display and Windows 10 as guest on a monitor connected to the HDMI port. For this reason it will not include instructions for audio passthrough or dynamic switching of the Nvidia GPU between host and guest and assume the Nvidia GPU to be soley for QEMU. Switching the Nvidia GPU between host and guest is known to work. There are several ways to accomplish this with some of them having issues here and there.

** Note**\
While this guide covers a virtual machine running Windows 10, it should be similar when using Linux.

** Note**\
This guide will cover the Thinkpad P53 but it might also work with any other P series Thinkpad or other high end Thinkpads with a dedicated Nvidia GPU.

**Resources**

[[]][IOMMU](https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit "wikipedia:Input–output memory management unit")

[[]][QEMU](https://en.wikipedia.org/wiki/QEMU "wikipedia:QEMU")

[[]][Virtual Machine Manager](https://en.wikipedia.org/wiki/Virtual_Machine_Manager "wikipedia:Virtual Machine Manager")

## Contents

-   [[1] [Obstacles]](#Obstacles)
-   [[2] [Hardware requirements]](#Hardware_requirements)
-   [[3] [Preparation]](#Preparation)
    -   [[3.1] [BIOS Settings]](#BIOS_Settings)
    -   [[3.2] [Extract activated vBIOS from system]](#Extract_activated_vBIOS_from_system)
        -   [[3.2.1] [Dump activated vBIOS to file]](#Dump_activated_vBIOS_to_file)
    -   [[3.3] [Extract vBIOS from BIOS update]](#Extract_vBIOS_from_BIOS_update)
        -   [[3.3.1] [Install VBiosFinder]](#Install_VBiosFinder)
        -   [[3.3.2] [Download the BIOS update]](#Download_the_BIOS_update)
        -   [[3.3.3] [Let VBiosFinder extract the vBIOS]](#Let_VBiosFinder_extract_the_vBIOS)
    -   [[3.4] [Patching OVMF firmware with vBIOS]](#Patching_OVMF_firmware_with_vBIOS)
        -   [[3.4.1] [Install Docker]](#Install_Docker)
        -   [[3.4.2] [Download and run the patch]](#Download_and_run_the_patch)
    -   [[3.5] [Create a fake battery]](#Create_a_fake_battery)
-   [[4] [Installation]](#Installation)
    -   [[4.1] [Kernel]](#Kernel)
    -   [[4.2] [QEMU]](#QEMU)
        -   [[4.2.1] [libvirt]](#libvirt)
            -   [[4.2.1.1] [User permissions]](#User_permissions)
            -   [[4.2.1.2] [Starting the service]](#Starting_the_service)
        -   [[4.2.2] [Virt-Manager]](#Virt-Manager)
-   [[5] [Enable VFIO]](#Enable_VFIO)
    -   [[5.1] [Check the IOMMU layout]](#Check_the_IOMMU_layout)
    -   [[5.2] [Modules]](#Modules)
        -   [[5.2.1] [Blacklist Nvidia Modules]](#Blacklist_Nvidia_Modules)
        -   [[5.2.2] [Load the VFIO Modules]](#Load_the_VFIO_Modules)
        -   [[5.2.3] [Selecting Nvidia GPU / Audio]](#Selecting_Nvidia_GPU_.2F_Audio)
    -   [[5.3] [Grub]](#Grub)
-   [[6] [Creating a virtual Intel GVT-g GPU]](#Creating_a_virtual_Intel_GVT-g_GPU)
    -   [[6.1] [List supported MDEV types]](#List_supported_MDEV_types)
    -   [[6.2] [Create a UUID]](#Create_a_UUID)
    -   [[6.3] [Device creation]](#Device_creation)
    -   [[6.4] [Check the result]](#Check_the_result)
-   [[7] [Virtual Machine setup]](#Virtual_Machine_setup)
    -   [[7.1] [Create a new virtual machine]](#Create_a_new_virtual_machine)
    -   [[7.2] [Add external keyboard and mouse]](#Add_external_keyboard_and_mouse)
    -   [[7.3] [Replace the OVMF firmware]](#Replace_the_OVMF_firmware)
    -   [[7.4] [Add virtual Intel GPU]](#Add_virtual_Intel_GPU)
    -   [[7.5] [Add Nvidia GPU]](#Add_Nvidia_GPU)
    -   [[7.6] [Add fake battery]](#Add_fake_battery)
    -   [[7.7] [Finishing touches]](#Finishing_touches)
    -   [[7.8] [Install Windows]](#Install_Windows)
    -   [[7.9] [Download Nvidia drivers]](#Download_Nvidia_drivers)
-   [[8] [References]](#References)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Obstacles]

There are a number of obstacles in order to successfully pass the Nvidia GPU into a Windows guest system and make it work with the Nvidia drivers. Most of them are related to decisions by Nvidia. While we only expect the powerful Nvidia GPU to work inside the VM, it needs both GPUs to be passed into the VM. But due to Intel GVT-g technology, we will pass a virtualized GPU to it. This Intel GPU will do nothing more then allow the driver to be installed.

The laptop comes with 3 different versions of vBIOS. We extract one version of it from the BIOS update file and another one with the active Nvidia GPU from within the system. The extracted one from BIOS update needs to be patched against OVMF firmware and the other vBIOS needs to exist inside the VM next to a fake battery.

** Note**\
Even if this guide covers vBIOS extraction and patching a firmware, all of this will only be used in the VM. No GPU flashing or changes to the hardware will happen. Even BIOS updates are optional and expected to be done as provided by Lenovo.

## [Hardware requirements]

To proceed with the installation you will need a dedicated monitor connected to the HDMI port and also a mouse & keyboard connected to USB. Usage of docking stations hasn\'t been tested.

## [Preparation]

You need to have the external monitor connected during this setup.

** Note**\
In this guide, we will use `/opt/qemu` to store the files. Create it or use a directory of your choice.

### [BIOS Settings]

While optional, it is recommended to update to the latest BIOS version, check [the official page](https://support.lenovo.com/us/en/downloads/ds540999-bios-update-utility-bootable-cd-for-windows-10-64-bit-linux-thinkpad-p53-p73).

The following settings are needed.

[CODE]

    Config -> Display -> Hybrid Graphics
    Security -> Secure Boot -> Disabled
    Security -> Virtualization -> Intel Virtualization Technology -> Enabled
    Security -> Virtualization -> Intel VT-d Feature -> Enabled
    Startup -> UEFI/Legacy Boot -> UEFI Only

### [Extract activated vBIOS from system]

For this step you\'ll need the Nvidia card to be active and running with propretary drivers within your Gentoo system. It needs to display some output while doing so.

** Note**\
You can skip this step if the external monitor is showing something already.

Make sure you have the Nvidia card enabled globally as well as the `xinerama` USE flag:

[FILE] **`/etc/portage/make.conf`**

    ...
    USE="xinerama"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965 iris nvidia

\
If you\'ve changed this setting, please update your system:

`root `[`#`]`emerge -uND world`

Make sure the Nvidia card is loaded and the external monitor is used when starting X11:

[FILE] **`/etc/X11/xorg.conf.d/10-nvidia.conf`**

    Section "ServerLayout"
        Identifier "layout"
        Screen 0 "nvidia"
        Inactive "intel"
    EndSection

    Section "Device"
        Identifier "nvidia"
        Driver "nvidia"
        BusID "01:00:0"
        Option "RegistryDwords" "EnableBrightnessControl=1"
    EndSection

    Section "Screen"
        Identifier "nvidia"
        Device "nvidia"
        Option "AllowEmptyInitialConfiguration"
    EndSection

    Section "Device"
        Identifier "intel"
        Driver "modesetting"
    EndSection

    Section "Screen"
        Identifier "intel"
        Device "intel"
    EndSection

Restart your system and make sure the external monitor is showing X11 output. If that\'s ok, you need to get the Bus ID for the Nvidia card:

#### [Dump activated vBIOS to file]

`user `[`$`]`lspci -D | grep NVIDIA`

    0000:00:01.0 VGA compatible controller: NVIDIA Corporation TU117GLM [Quadro T2000 Mobile / Max-Q] (rev a1)
    0000:00:01.0 Audio device: NVIDIA Corporation Device 10fa (rev a1)

You can now dump the rom. Make sure you have the right Bus ID. With the ID shown from the output above, it would work like this:

`root `[`#`]`echo 1 > /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/rom`

`root `[`#`]`cat /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/rom > /opt/qemu/nvidia-active-vbios.rom`

`root `[`#`]`echo 0 > /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/rom`

### [Extract vBIOS from BIOS update]

We will use **VBiosFinder** to extract the vBIOS that is part of the BIOS update.

#### [Install VBiosFinder]

This a one time task. Once you have the vBIOS extracted you won\'t need the tool again. There is currently no Ebuild for this tool and dependencies in Portage or any known overlay. The tool is based on Ruby and installing it on Gentoo might cause packages (so called bundles) to be installed by 3rd party package manager. The setup on Gentoo will not be covered as it needs quite a bit of dealing with Ruby. Since we deal with virtual machines, it might quicker to just spin up a throwaway VM based on any other distribution and install it there.

** Note**\
You may want to keep this VM to patch the OVMF firmware later on.

Clone their repository from [their Github page](https://github.com/coderobe/VBiosFinder) and follow the instructions on the site to install the tool and it\'s dependencies. Make sure to place [Rom-Parser](https://github.com/awilliam/rom-parser) (you may need to compile it first) and [UEFIExtract](https://github.com/LongSoft/UEFITool/tree/new_engine) as binaries into the `3rdparty` subdirectory.

Your 3rdparty directory should look like this:

`user `[`$`]`ls ./3rdparty`

    UEFIExtract
    rom-parser

#### [Download the BIOS update]

If you\'ve not downloaded it already, please head over to [the official page](https://support.lenovo.com/us/en/downloads/ds540999-bios-update-utility-bootable-cd-for-windows-10-64-bit-linux-thinkpad-p53-p73) and download the `BIOS Update Utility` from it. Pick the .exe file for Windows 10 which should be between 15 to 20MB.

Place the downloaded file into the VBiosFinder main directory.

#### [Let VBiosFinder extract the vBIOS]

For some reason the VBiosFinder seems to need the full path the downloaded file. If everything is correct, you should see output like this:

`user `[`$`]`./vbiosfinder extract /home/user/vBiosFinder/n2nuj18w.exe`

    output will be stored in '/home/user/vBiosFinder/tmp-vbiosfinder'
    checking for ruby... yes
    checking for innoextract... yes
    checking for upx... yes
    checking for 7z... yes
    trying to extract ./n2nuj18w.exe
    found innoextract archive
    Extracting "version 1.31-1.14(N2NET46W-N2NHT29W)" - setup data version 5.5.7 (unicode)
    ...
    finding vbios
    12 possible candidates
    checking for rom-parser... yes
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Found VBIOS for device 8086:0406!
    Job done. Extracted files can be found in /home/user/vBiosFinder/tmp-vbiosfinder/../output
    Cleaning up garbage

The output directory should look like this:

`user `[`$`]`ls ./output`

    bios_n2nuj18w.exe
    body.bin
    vbios_8086_0406_1.rom

The vBIOS we are looking for would be `vbios_8086_0406_1.rom`. Place it to the other files:

`root `[`#`]`cp ./output/vbios_8086_0406_1.rom /opt/qemu/bios-vbios.rom`

### [Patching OVMF firmware with vBIOS]

OVMF is an open-source UEFI firmware for QEMU virtual machines.

There is an Ebuild for the OVMF firmware in Portage but it would need extensive editing to get the vBIOS and other patches included. Even more so, since the patches are not compatible to the version in Portage. We will use an independend approach with Docker.

#### [Install Docker]

You need to install [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") on your host system or into the throwaway VM you may have installed earlier.

#### [Download and run the patch]

Once you have Docker in place, you can clone the required [repository](https://github.com/T-vK/ovmf-with-vbios-patch) to some place and compile it with the patches:

`user `[`$`]`git clone `[`https://github.com/T-vK/ovmf-with-vbios-patch.git`](https://github.com/T-vK/ovmf-with-vbios-patch.git)

`user `[`$`]`cd ovmf-with-vbios-patch && mkdir ./build && mkdir ./roms`

`user `[`$`]`sudo docker build -t ovmf-vbios-patch .`

Once that process is finished, place the extracted vBIOS into the `roms` directory:

`user `[`$`]`cp /opt/qemu/bios-vbios.rom ./roms`

Run the patch and check if it was working correctly:

`user `[`$`]`sudo docker run --rm -ti -v "$(pwd)/build:/build:z" -v "$(pwd)/roms:/roms:z" -e "VROM=bios-vbios.rom" ovmf-vbios-patch`

    Building OVMF with a VBIOS for bios-vbios.rom
    make: Entering directory '/edk2/BaseTools'
    ...
    - Done -
    Build end time: 10:36:01, Sep.14 2021
    Build total time: 00:01:13

Once done, you should find the patched OVMF files in the `build` directory:

`user `[`$`]`ls ./build`

    OVMF_CODE.fd
    OVMF_VARS.fd

There you have the patched OVMF firmware with the included vBIOS. Place it to the other files:

`root `[`#`]`cp ./build/OVMF* /opt/qemu/`

### [Create a fake battery]

The Nvidia GPU driver will check for an existing battery in your system. Since passing through the real battery is out of the question, we will need to fake the battery into the virtual machine.

Create a file with the following content:

[FILE] **`/tmp/battery.txt`**

    U1NEVKEAAAAB9EJPQ0hTAEJYUENTU0RUAQAAAElOVEwYEBkgoA8AFVwuX1NCX1BDSTAGABBMBi5f
    U0JfUENJMFuCTwVCQVQwCF9ISUQMQdAMCghfVUlEABQJX1NUQQCkCh8UK19CSUYApBIjDQELcBcL
    cBcBC9A5C1gCCywBCjwKPA0ADQANTElPTgANABQSX0JTVACkEgoEAAALcBcL0Dk=

Convert it into a binary file:

`user `[`$`]`base64 --decode /tmp/battery.txt > /tmp/battery.dat`

Copy the `battery.dat` to the other files:

`root `[`#`]`cp ./battery.dat /opt/qemu/`

## [Installation]

### [Kernel]

** Note**\
It is important to add VFIO related options as modules. This allows you to add parameters when loading.

[KERNEL] **Kernel 5.10.52 (gentoo-sources)**

    [*] Virtualization --->
      <*> Kernel-based Virtual Machine (KVM) support
        <*> KVM for Intel (and compatible) processors support
        < > KVM for AMD processors support
        [*] Audit KVM MMU
    Device Drivers --->
      Graphics support  --->
        < > Nouveau (NVIDIA) cards
        <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
          (*) Force probe driver for selected new Intel hardware
          [*] Enable capturing GPU state following a hang
          [*] Always enable userptr support
          [*] Enable Intel GVT-g graphics virtualization host support
          [M] Enable KVM/VFIO support for Intel GVT-g
      <M> VFIO Non-Privileged userspace driver framework  --->
        [*] VFIO No-IOMMU support  ----
        <M> VFIO support for PCI devices
        [*] VFIO PCI support for VGA devices
        [*] VFIO PCI extensions for Intel graphics (GVT-d)
        <M> Mediated device driver framework
        <M> VFIO driver for Mediated devices
      [*] IOMMU Hardware Support --->
        [*] IOMMU passthrough by default
        [ ] AMD IOMMU support
        [*] Support for Intel IOMMU using DMA Remapping Devices
          [*] Support for Shared Virtual Memory with Intel IOMMU
          [*] Enable Intel DMA Remapping Devices by default
        [*] Support for Interrupt Remapping
      [*] VHOST drivers
        <*> Host kernel accelerator for virtio net
        [*] Cross-endian support for vhost

### [QEMU]

** Note**\
You may also check the [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") page.

Set the QEMU targets according to your system:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu QEMU_SOFTMMU_TARGETS: x86_64
    app-emulation/qemu QEMU_USER_TARGETS: x86_64

The QEMU package comes with a larger list of possible USE flags. You may want to check those USE flags and set them according to your planned setup. This is a recommended set of flags:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/qemu usb spice snappy lzo vhost-user-fs numa io-uring fuse

After reviewing and adding any desired USE flags, emerge [[[app-emulation/qemu]](https://packages.gentoo.org/packages/app-emulation/qemu)[]]:

`root `[`#`]`emerge --ask app-emulation/qemu`

#### [libvirt]

** Note**\
There might be additional kernel configuration needed for libvirt. Please check the output during install.

As well as QEMU, libvirt comes with a number of Use flags. Please check those flags and set them according to your setup. These are recommended USE flags for libvirt:

[FILE] **`/etc/portage/package.use/qemu`**

    app-emulation/libvirt pcap virt-network numa fuse

After reviewing and adding any desired USE flags, emerge [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]]:

`root `[`#`]`emerge --ask app-emulation/libvirt`

##### [User permissions]

After emerging, to run virt-manager as a normal user, ensure each user has been added to the `libvirt` group:

`root `[`#`]`usermod -a -G libvirt <user>`

##### [Starting the service]

The service needs to be started. It\'s also a good idea to enabled in order to be around once we restart the system. This can be done with:

With OpenRC:

`root `[`#`]`/etc/init.d/libvirtd start && rc-update add libvirtd `

With Systemd:

`root `[`#`]`systemctl enable --now libvirtd `

#### [Virt-Manager]

Virt-Manager allows you to manage virtual machines using a destop UI.

Install [[[app-emulation/virt-manager]](https://packages.gentoo.org/packages/app-emulation/virt-manager)[]]:

`root `[`#`]`emerge --ask app-emulation/virt-manager`

## [Enable VFIO]

### [Check the IOMMU layout]

Passing through any PCI device can only be done with all devices at once within the same group. Except for the PCI root device. The group layout on the P53 is well organized and suitable for this task. You can check the layout like this:

`user `[`$`]`for d in /sys/kernel/iommu_groups/*/devices/*; do n=$; n=$; printf 'IOMMU Group %s ' "$n"; lspci -nns "$"; done;`

    ...
    IOMMU Group 1 00:01.0 PCI bridge [0604]: Intel Corporation 6th-9th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 07)
    IOMMU Group 1 01:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU117GLM [Quadro T2000 Mobile / Max-Q] [10de:1fb8] (rev a1)
    IOMMU Group 1 01:00.1 Audio device [0403]: NVIDIA Corporation Device [10de:10fa] (rev a1)
    ...

The Nvidia GPU with its audio device should look similar on your system. In order to pass through the Nvidia GPU you\'ll also need to pass through the audio device.

### [Modules]

#### [Blacklist Nvidia Modules]

To prevent the host from holding on to the Nvidia GPU we need to blacklist the drivers.

[FILE] **`/etc/modprobe.d/nvidia.conf`**

    blacklist nvidia
    blacklist nvidia-drm

#### [Load the VFIO Modules]

[FILE] **`/etc/modules-load.d/vfio.conf`**

    kvmgt
    vfio-pci
    vfio-iommu-type1
    vfio-mdev

#### [][Selecting Nvidia GPU / Audio]

** Note**\
Make sure to get the correct numbers as there are 2 GPUs and audio devices (Intel and Nvidia). Do not mix them!

You need to pass the device IDs of the PCI devices for Nvidia GPU and Audio. Check the PCI list with `lspci -nn` and copy the IDs into this file accordingly:

[FILE] **`/etc/modprobe.d/vfio.conf`**

    options vfio-pci ids=10de:1fb8,10de:10fa

Adding device IDs like this, will block it from the host system.

### [Grub]

The following parameters need to be added to the Grub command line in order to enable VFIO and IOMMU at boot time:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX=" ... i915.enable_gvt=1 iommu=pt intel_iommu=on"

** Note**\
At this point, it would be a good idea to reboot the system. This should load all the required modules and enable VFIO on the selected devices. You may not be able to go on with the next step otherwise.

## [Creating a virtual Intel GVT-g GPU]

** Note**\
This only works with Intel CPUs up to 9th generation.^[\[1\]](#cite_note-1)^

As explained before, this virtual GVT-g GPU is needed for the Nvidia drivers to install and run properly. It will be seen in guest as a regular Intel GPU.

Get the ID for your Intel GPU with:

`user `[`$`]`lspci -D -nn | grep UHD`

    0000:00:02.0 VGA compatible controller [0300]: Intel Corporation UHD Graphics 630 (Mobile) [8086:3e9b]

`0000:00:02.0` is the ID in question. It should be similar on your system.

### [List supported MDEV types]

** Note**\
If you can\'t find the MDEV directory. GVT-g isn\'t working for you yet. Please make sure you\'ve followed the steps above accordingly and rebooted the machine with GRUB kernel options in place.

If you have VFIO with GVT-g working, you should be able to get a list of possible MDEV types:

`user `[`$`]`ls /sys/bus/pci/devices/0000:00:02.0/mdev_supported_types`

    i915-GVTg_V5_2 # 256MB VRAM
    i915-GVTg_V5_4 # 128MB VRAM
    i915-GVTg_V5_8 # 64MB VRAM

It\'s still ok if you only have one or two of them listed. You need to pick one of them while any of them are good for the task. The difference between them is basically the amout of resources you\'ll have assigned to it. Since we are not using it other then providing it to the Nvidia driver, the least amout of RAM should do it.

### [Create a UUID]

The UUID will be assigned to the device:

`user `[`$`]`uuidgen`

    722189c3-517e-4d42-a8ab-369daabb5f7f

We will use this example in the guide. You can use it too or create one of your own.

### [Device creation]

The virtual GPU device can be created using a single command:

`root `[`#`]`echo "722189c3-517e-4d42-a8ab-369daabb5f7f" > "/sys/bus/pci/devices/0000:00:02.0/mdev_supported_types/i915-GVTg_V5_8/create"`

If you want the device to be created at boot time, you can do it with a custom script:

Using OpenRC:

[FILE] **`/etc/local.d/intel_mdev.start`**

    #!/bin/bash

    GVT_PCI="0000:00:02.0"
    GVT_GUID="722189c3-517e-4d42-a8ab-369daabb5f7f"
    MDEV_TYPE="i915-GVTg_V5_8"

    echo "$" > "/sys/bus/pci/devices/$/mdev_supported_types/$/create"

Please add your UUID and make sure the script can be executed:

`root `[`#`]`chmod +x /etc/local.d/intel_mdev.start`

Using Systemd:

There is no local.d when using Systemd. You need to place the above script somewhere on your system (lets say `/usr/local/sbin/start-intel-mdev.sh`), make it executable and write a unit file to start it:

[FILE] **`/etc/systemd/system/start-intel-mdev.service`**

    [Unit]
    Description=Create a virtual GPU with Intel GVT-d

    [Service]
    Type=oneshot
    ExecStart=/usr/local/sbin/start-intel-mdev.sh

    [Install]
    WantedBy=multi-user.target

Start the script on boot:

`root `[`#`]`systemctl enable start-intel-mdev`

### [Check the result]

If you did everything correct, you should see an output like this after a reboot:

`user `[`$`]`dmesg | grep mdev`

    [ 1410.959917] vfio_mdev 722189c3-517e-4d42-a8ab-369daabb5f7f: Adding to iommu group 25
    [ 1410.959918] vfio_mdev 722189c3-517e-4d42-a8ab-369daabb5f7f: MDEV: group_id = 25

## [Virtual Machine setup]

At this point, you should have everything together to get the virtual machine going with your real Nvidia GPU. In order to prepare the virtual machine, you need to create it without installing Windows right away. We\'ll need to add everything first and install Windows with the Nvidia GPU in place.

### [Create a new virtual machine]

Create a new virtual machine using Virt-Manager. For this guide we will use the name **win10**. Select your Windows ISO file and click through the menu and add RAM and CPUs as you see fit. Once you reach `Ready to begin the installation`, you need to make sure you\'ve checked the option to `Customize configuration before install`.

Click `Finish` to enter the configuration.

Make the following changes in the upcoming configuration window:

[CODE]

    Overview -> Hypervisor Details -> Chipset -> Q35
    Overview -> Hypervisor Details -> Firmware -> UEFI x86_64: /usr/share/edk2-ovmf/OVMF_CODE.fd

Once you\'ve set this, click `Begin Installation` but don\'t install Windows yet. Just let the counter go through and shut down the virtual machine after it.

### [Add external keyboard and mouse]

The virtual machine will not use the internal laptop keyboard / touchpad. So you need to add the connected USB keyboard and mouse with USB passthrough. This is doable from within Virt-Manager.

Open the VM in Virt-Manager again and go to the configuration window. Click `Add Hardware` and select `USB Host Device`. Add mouse and keyboard from the list to the virtual machine.

### [Replace the OVMF firmware]

We\'ve simply added the default OVMF firmware in the initial configuration window. We will replace it with the one we\'ve patched earlier.

Edit the XML file using the `virsh` editor:

`root `[`#`]`virsh edit win10`

[CODE]

    <domain ...>
      ...
      <os>
        <type ...>hvm</type>
        <loader readonly='yes' type='pflash'>/opt/qemu/OVMF_CODE.fd</loader>
        <nvram>...</nvram>
      </os>
      ...
    </domain>

Leave the editor and it should save the file.

### [Add virtual Intel GPU]

It\'s time to add the virtual Intel GPU. For this you\'ll need the UUID of the device, you\'ve assigned to it earlier:

`root `[`#`]`virsh edit win10`

[CODE]

    <domain ...>
    ...
      <devices>
        ...
        <hostdev mode='subsystem' type='mdev' managed='no' model='vfio-pci' display='off'>
          &lt;source>
            <address uuid='722189c3-517e-4d42-a8ab-369daabb5f7f'/>
          &lt;/source>
          <address type='pci' domain='0x0000' bus='0x06' slot='0x00' function='0x0'/>
        </hostdev>
        ...
      </devices>
    </domain>

Exit the editor to save the file. If it complains about a existing bus ID, you need to increment the `bus='0x06'` value.

### [Add Nvidia GPU]

This is the point where you will add the Nvidia GPU into the virtual machine. You\'ll also add the Nvidia HDMI audio device. You also need to add the extraced vBIOS rom to it. Otherwise it will just return a blank screen.

`root `[`#`]`virsh edit win10`

[CODE]

    <domain ...>
    ...
      <devices>
        ...
        <hostdev mode='subsystem' type='pci' managed='yes'>
          &lt;source>
            <address domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
          &lt;/source>
          <rom file='/opt/qemu/nvidia-active-vbios.rom'/>
          <address type='pci' domain='0x0000' bus='0x07' slot='0x00' function='0x0'/>
        </hostdev>
        <hostdev mode='subsystem' type='pci' managed='yes'>
          &lt;source>
            <address domain='0x0000' bus='0x01' slot='0x00' function='0x1'/>
          &lt;/source>
          <rom file='/opt/qemu/nvidia-active-vbios.rom'/>
          <address type='pci' domain='0x0000' bus='0x08' slot='0x00' function='0x0'/>
        </hostdev>
        ...
      </devices>
    </domain>

### [Add fake battery]

Don\'t miss out to add the fake battery. Otherwise you might run into trouble installing the Nvidia GPU drivers:

`root `[`#`]`virsh edit win10`

This will also require you to update the XML specifications in the very first line:

[CODE]

    <domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
    ...
      <qemu:commandline>
        <qemu:arg value='-acpitable'/>
        <qemu:arg value='file=/opt/qemu/battery.dat'/>
      </qemu:commandline>
    </domain>

### [Finishing touches]

Remove the following devices from the list as they will mostly cause trouble in this setup:

[CODE]

    Video QXL
    Display Spice
    Channel spice
    USB Redirector 1
    USB Redirector 2

### [Install Windows]

Just install Windows with the Virtio drivers from `app-emulation/virtio-win`. The drivers for the Intel GPU should be downloaded by itself after a while. You could trigger this manually in the Windows device manager.

### [Download Nvidia drivers]

Check your Nvidia GPU model:

`user `[`$`]`lspci | grep NVIDIA`

    01:00.0 VGA compatible controller: NVIDIA Corporation TU117GLM [Quadro T2000 Mobile / Max-Q] (rev a1)
    01:00.1 Audio device: NVIDIA Corporation Device 10fa (rev a1)

In our example it\'s a `Quadro T2000 Mobile`

You need to visit the [Nvidia drivers site](https://www.nvidia.de/Download/index.aspx?lang=en) and download the driver for your GPU from it.

The selection would be (as of September 2021):

[CODE]

    Product Type: NVIDIA RTX / Quadro
    Product Series: Quadro Series (Notebooks)
    Product: Quadro T2000
    Operating System: Windows 10
    Download Type: Production Branch / Studio
    Language: English (US)

## [References]

1.  [[[↑](#cite_ref-1)] [[Ice Lake support?](https://github.com/intel/gvt-linux/issues/126), accessed 13th September 2021]]

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [GPU passthrough with virt-manager, QEMU, and KVM](https://wiki.gentoo.org/wiki/GPU_passthrough_with_virt-manager,_QEMU,_and_KVM "GPU passthrough with virt-manager, QEMU, and KVM") --- directly present an internal PCI GPU as-is for direct use by a virtual machine

## [External resources]

-   [https://github.com/coderobe/VBiosFinder](https://github.com/coderobe/VBiosFinder) - VBiosFinder
-   [https://github.com/T-vK/ovmf-with-vbios-patch](https://github.com/T-vK/ovmf-with-vbios-patch) - ovmf-with-vbios-patch
-   [https://wiki.archlinux.org/title/Intel_GVT-g](https://wiki.archlinux.org/title/Intel_GVT-g) - Arch Wiki - Intel GVT-g
-   [https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF) - Arch Wiki - PCI passthrough via OVMF
-   [https://www.reddit.com/r/VFIO](https://www.reddit.com/r/VFIO) - Reddit - VFIO
-   [https://www.reddit.com/r/VFIO/comments/modwuh/experiencespotentially_a_guide_gvt_dgpu](https://www.reddit.com/r/VFIO/comments/modwuh/experiencespotentially_a_guide_gvt_dgpu) - Reddit - GVT + dGPU passthrough on a laptop (Thinkpad P50 - Muxed)
-   [https://www.reddit.com/r/VFIO/comments/ma0s7j/how_to_dump_gpu_vbios_on_linux](https://www.reddit.com/r/VFIO/comments/ma0s7j/how_to_dump_gpu_vbios_on_linux) - Reddit - How to dump GPU VBIOS on linux?
-   [https://lantian.pub/en/article/modify-computer/laptop-intel-nvidia-optimus-passthrough.lantian](https://lantian.pub/en/article/modify-computer/laptop-intel-nvidia-optimus-passthrough.lantian) - Lan Tian Blog - Intel and NVIDIA GPU Passthrough on a Optimus MUXless Laptop
-   [https://github.com/bryansteiner/gpu-passthrough-tutorial](https://github.com/bryansteiner/gpu-passthrough-tutorial) - Bryan Steiner - GPU Passthrough Tutorial
-   [https://www.heiko-sieger.info/running-windows-10-on-linux-using-kvm-with-vga-passthrough](https://www.heiko-sieger.info/running-windows-10-on-linux-using-kvm-with-vga-passthrough) - Heiko Sieger - Running Windows 10 on Linux using KVM with VGA Passthrough