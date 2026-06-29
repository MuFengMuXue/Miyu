[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Virt-manager&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Virt-manager "Virt-manager (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Virt-manager/tr "Virt-manager (4% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Virt-manager/ru "Virt-manager (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [I want to know more]](#I_want_to_know_more)
-   [[3] [What we absolutely must know]](#What_we_absolutely_must_know)
-   [[4] [Install virt-manager, qemu and all dependencies]](#Install_virt-manager.2C_qemu_and_all_dependencies)
-   [[5] [Using Virt-Manager for guest creation]](#Using_Virt-Manager_for_guest_creation)
    -   [[5.1] [Install guest additions]](#Install_guest_additions)
    -   [[5.2] [Tune the display settings]](#Tune_the_display_settings)
    -   [[5.3] [File sharing between host and guest]](#File_sharing_between_host_and_guest)
    -   [[5.4] [Optimize vCPU]](#Optimize_vCPU)
-   [[6] [Lab: Windows 11]](#Lab:_Windows_11)
    -   [[6.1] [Prepare]](#Prepare)
    -   [[6.2] [Install]](#Install)
    -   [[6.3] [Final Setup]](#Final_Setup)
-   [[7] [References]](#References)

# [Overview]

[![Topbar logo.png](/images/4/47/Topbar_logo.png)](//wiki.manjaro.org/index.php?title=File:Topbar_logo.png)

\

**tip**

------------------------------------------------------------------------

Have you heard about Virtualbox to virtualize operating systems like Linux and Windows or Mac? It \'a good software, but not the only one! Don\'t forget VMware, Gnome Boxes and \...virt-manager.

\

------------------------------------------------------------------------

**[Virt-manager](https://virt-manager.org/)** uses **[libvirt](http://libvirt.org/)** and it\'s a manager of many **[hypervisors](https://libvirt.org/drivers.html)**, including the one that we want to use here: QEMU/KVM.

------------------------------------------------------------------------

\

**Why do I need to virtualize?**

-   To learn about a new O.S.

<!-- -->

-   To configure a hardware that has a setup only for that operating system

<!-- -->

-   To use a software that only works on another

# [I want to know more]

[![Hypervisor 1.png](/images/9/92/Hypervisor_1.png)](//wiki.manjaro.org/index.php?title=File:Hypervisor_1.png)

\
1. **[Virtualization](https://en.wikipedia.org/wiki/Virtualization)**\
2. **[Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)**\
3. **[Virtual machine](https://en.wikipedia.org/wiki/Virtual_machine)**\

# [What we absolutely must know]

\
1. What is my CPU. Identify it and make sure it\'s at least a quad core. **TAKE A LOOK AT** **[CPU-World](http://www.cpu-world.com/CPUs/CPU.html)**\
2. Check if the \'virtualization parameters\' are enabled on BIOS using

[user \$ ][ LC_ALL=C lscpu [COPY TO CLIPBOARD]]

\

3\. How much memory I have. Check the RAM and verify that is at least 4GB.\
4. The amount of free space on my hard drive. The virtual machine can use a disk image file so extra partitions are not necessary.

**Note**

------------------------------------------------------------------------

You can also use raw partition specific for virtual machines. See [partitioning](https://wiki.archlinux.org/title/Partitioning) for more information

5\. The minimum hardware requirements of the operating system you want to install as a virtual machine.\

# [][Install virt-manager, qemu and all dependencies]

\
From terminal:

[user \$ ][ sudo pacman -S \--needed virt-manager qemu-desktop libvirt edk2-ovmf dnsmasq iptables-nft [COPY TO CLIPBOARD]]

\

For TPM support:

[user \$ ][ sudo pacman -S \--asdeps swtpm [COPY TO CLIPBOARD]]

\

Enable and start service

[user \$ ][ sudo systemctl enable libvirtd.service [COPY TO CLIPBOARD]]

\

Add user to *libvirt,* *libvirt-qemu* and *kvm* groups to use the **system**-level virtual machines (qemu:///system).

[user \$ ][ sudo usermod -a -G libvirt,libvirt-qemu,kvm \$USER [COPY TO CLIPBOARD]]

\

Note that you will need to restart userspace for the groups to become active. To restart userspace

[user \$ ][ systemctl soft-reboot [COPY TO CLIPBOARD]]

\

**Note**

------------------------------------------------------------------------

1.  You don\'t need this step to run system-level virtual machines. However, virt-manager will prompt for sudoer\'s password when launch if the user is not in the *libvirt* group
2.  You can also create **user**-level virtual machines (qemu:///session) and use without sudoer\'s privelige. However, some features such as [VirtioFS file sharing](https://libvirt.org/kbase/virtiofs.html) may be unavailable in qemu:///session

# [Using Virt-Manager for guest creation]

0\. Prepare installation image. If you\'re going to install Windows, prepare the [Virtio driver](https://www.linux-kvm.org/page/WindowsGuestDrivers/Download_Drivers) image too.

\

**Tip**

------------------------------------------------------------------------

You can also find the [virtio-win](https://aur.archlinux.org/packages/virtio-win) package in AUR. The image is located in **/var/lib/libvirt/images**, which is the default [directory pool](https://libvirt.org/storage.html#StorageBackendDir) of qemu:///system

1\. Launch menu Virtual Machine Manager. It should already have a [LXC](https://libvirt.org/drvlxc.html) connection. You can disconnect and remove it if you don\'t use LXC.

2\. Go to File, choose Add Connection and choose hypervisor QEMU/KVM, or QEMU/KVM user session if you don\'t want **system**-level virtual machines. Click on connect.

3\. You need directory pools to store the disk images of virtual machines or the ISO file of CD/DVD. Double click qemu/kvm, go on storage and add by clicking + the path to the folder where you have the iso and the folder where create the virtual machine.

\

**tip**

------------------------------------------------------------------------

Advice: use a different partition than the root. In case you need to reinstall your operating system you don\'t lose the VM that already ready-to-start.

4\. Click on create a new virtual machine: select **Local install media (ISO image or CDROM)**, and select the installation ISO image and OS type (if not detected).

5\. How many CPU assign and how much memory? (check the recommended requirements of O.S. that you are installing)

6\. Create the file system of the virtual machine by selecting **Select or create custom storage** and click **Manage\...**. Under your desired directory pool, create the volume of the virtual machine (default in qcow2 format). How many GB? Check the recommended requirements O.S. you install.

7.Assign a name to the machine and flag **customize configuration before install**. You have access to the screen with all the hardware that will be virtualized, do a check if there is all that is needed to initialize and launch the installer.

8\. In *Overview*, change the firmware to UEFI for future-proof capacity.

9\. Change the type of SATA Disk 1 (the disk image of the creating virtual machine) to *virtio* for better performance. Change discard mode to *unmap*, and then apply the change. You should notice the device name would change from SATA Disk 1 to VirtIO Disk 1.

**Warning**

------------------------------------------------------------------------

If you\'re installing Windows, make sure to create a new SATA CDROM device and select the **virtio-win** image as the media, so that the Windows Installer can load the driver to recognize the disk. The virtio storage driver should be located at somewhere like *E:\\viostor\\w10\\amd64*

10\. Set the NIC type to virtio too for better network performance.

**Note**

------------------------------------------------------------------------

If you\'re installing Windows, once the system if ready, make sure to install all the virtio drivers so that your virtIO network can work normally

11\. Add TPM chip, select **TIS** model through **Emulated device** backend.

12\. Add a watchdog to reboot the guest when it hangs. Leave the settings as default.

13\. And a hardware RNG, to get entropy from the host.

14\. Click on the top to start installation.

\

**Warning**

------------------------------------------------------------------------

**All these steps are visible on youtube.** **[\>\>\> PLAY THIS](https://youtu.be/DiUG_hlLk3c)**

[![YouTube 1.png](/images/thumb/2/23/YouTube_1.png/300px-YouTube_1.png)](//wiki.manjaro.org/index.php?title=File:YouTube_1.png)

[](//wiki.manjaro.org/index.php?title=File:YouTube_1.png "Enlarge")

## [Install guest additions]

Once the VM is started and running you have to install the [spice guest tools](https://www.spice-space.org/download.html).

For Windows is a single package: spice-guest-tools-xxxx.exe

For linux are: spice-vdagent and xf86-video-qxl. If you visrtualize a linux distro you can install them with their package manager

Visit: **[Spice download](http://www.spice-space.org/download.html)**

## [Tune the display settings]

The default model of display card is QXL. If your virtual machine is Linux system, you can change it to virtio and enable 3D acceleration for better graphic performance.\
Windows virtual machine, however doesn\'t support virtio display yet. Nevertheless, we can increase its VGA memory from the default 16 MB to 64 MB to allow higher display resolution and slightly better 2D graphical performance.\
To do so, we need to edit the XML file of the virtual machine.

1.  In virt-manager, go to edit \> preference, and check **Enable XML edit**.
2.  In virtual machine details, go to display card. Under the XML tab, change the value of **vgamem** to 65536, then apply the change.

\

## [File sharing between host and guest]

For Linux guests, Virtio-FS and 9p are available for file sharing. See [ArchWiki](https://wiki.archlinux.org/title/Libvirt#Sharing_data_between_host_and_guest) for more information.\
For Windows guest, the easiest way to share file between host and guest is through [SAMBA](https://wiki.manjaro.org/index.php/Using_Samba_in_your_File_Manager).

1.  Create a SAMBA usershare
2.  In Windows guest, enter **\\\\192.168.122.1** in the file explorer, and you should be able to see the usershare on your host.
3.  Map that SAMBA usershare to a new drive, and connect to it with the appropriate credential. That\'s it.

Check [this article](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_virtualization/sharing-files-between-the-host-and-its-virtual-machines_configuring-and-managing-virtualization#sharing-files-between-the-host-and-windows-virtual-machines_sharing-files-between-the-host-and-its-virtual-machines) for more information.\

## [Optimize vCPU]

Check [this article](https://docs.fedoraproject.org/en-US/Fedora/13/html/Virtualization_Guide/ch25s06.html) to customize vCPU topology for better performance.\
For example, my CPU has 1 socket, 8 cores, and 16 threads in total. The automatic topology assigns 4 sockets, 1 core, and 1 thread to my guest. After changing it to 1 socket, 4 cores, and 1 thread, the performance increases significantly.\

# [Lab: Windows 11]

Windows Setup provides for setting up virtual Windows system for lab purpose. It can be for testing software or for pentesting.

For a continued use of Windows you will need a valid license key to run a virtualized Windows.

## [Prepare]

-   Create a new virtual machine
-   Select a Windows 11 ISO file
-   Accept the defaults clicking Next until you reach the final screen
-   Tick the box Customize configuration before install and click Finish
-   In the Overview pane - set vm firmware to BIOS and click Apply
-   Click the button Begin Installation

## [Install]

Before starting the installer press ShiftF10 so launch the Windows Cmd utility and launch regedit.

-   Expand HKEY_LOCAL_MACHINE\\SYSTEM\\Setup
-   Add new key named LabConfig
-   Add new DWORD value with name BypassTPMCheck and change the value to 1.
-   Add new DWORD value with name BypassRAMCheck and change the value to 1.
-   Add new DWORD value with name BypassSecureBootCheck and change the value to 1.

Close the registry editor and exit the shell, then continue the installer

## [Final Setup]

During last stage the installer will insist in network access but you may want use a local account instead of the required Microsoft account.

This can be disabled using the Cmd utility ShiftF10

-   enter OOBE\\BYPASSNRO and press Enter
-   close the Cmd utility
-   back in the setup window click I don\'t have internet

# [References]

**[Virt-manager](https://virt-manager.org/)**\
**[Libvirt](http://libvirt.org/)**\
**[Qemu](http://wiki.qemu.org/Main_Page)**\
**[x86 virtualization](https://en.wikipedia.org/wiki/X86_virtualization)**\
**[Intel-vt](http://ark.intel.com/Products/VirtualizationTechnology)**\
**[Amd-v](http://www.amd.com/en-gb/innovations/software-technologies/processors-for-business/virtualization)**\