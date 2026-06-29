**翻译状态：**

  * 本文（或部分内容）译自 [Xen](<https://wiki.archlinux.org/title/Xen> "arch:Xen")，最近一次同步于 2023-10-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xen?diff=0&oldid=786572>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xen_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Category:Hypervisors](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:Hypervisors")
  * [Moving an existing install into (or out of) a virtual machine](</wzh/index.php?title=Moving_an_existing_install_into_\(or_out_of\)_a_virtual_machine&action=edit&redlink=1> "Moving an existing install into \(or out of\) a virtual machine（页面不存在）")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:Xen#](<../zh-cn/Talk:Xen.html>) 中讨论）

根据[Xen 概览](<https://wiki.xen.org/wiki/Xen_Overview>): 

    Xen 是一套开源的类型一 hypervisor（又称为裸机 hypervisor），可以在单个设备/宿主机上同时运行多个相同或不同的操作系统实例。Xen 是目前唯一的开源类型一 hypervisor。

Xen hypervisor 是一层轻量的软件，它模拟了计算机的架构，使得可以同时运行多个操作系统。Hypervisor 由计算机上的引导加载器启动；当 hypervisor 加载完成后，它会启动 [dom0](<https://wiki.xen.org/wiki/Dom0>)（即“domain 0”的简称，有时被称为宿主或私有域），在当前案例中使用 Arch Linux。在 _dom0_ 启动完成后，可以从 _dom0_ 启动并控制一个或多个 [domU](<https://wiki.xen.org/wiki/DomU>)（用户域的简称，有时被称为 VMs 或是客户域）。对于 _domU_ 来说，Xen 支持半虚拟化（PV）域，硬件虚拟化域（HVM）及硬件虚拟化包装器中的半虚拟化域（PVH）。更多详细信息可以参考 [Xen.org](<https://wiki.xen.org/wiki/Xen_Overview>)。 

Xen hypervisor 需部署在一套安装完整的底层操作系统上。在安装 Xen hypervisor 前，宿主机上需有一套完全可用并更新到最新的 Arch Linux 系统。系统可以是只包含基础软件包的最小化安装，且无需[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")或是 [Xorg](<../zh-cn/Xorg.html> "Xorg")。 

如果你在从头开始搭建宿主机，可以参考[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")来安装 Arch Linux。 

**警告：** 不要在使用 Xen hypervisor 时运行如 [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 等其它虚拟化软件，这可能会导致系统挂起。详细信息可参考 [bug 报告（不予修复）](<https://www.virtualbox.org/ticket/12146>)。

##  安装

###  系统要求

Xen hypervisor 需要包含于较新 Linux 内核中的内核级支持，相关功能已包含在 [linux](<https://archlinux.org/packages/?name=linux>)包 及 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 Arch 内核软件包中。如需运行 HVM _domU_ ，物理硬件也需要包含 VT-x 或 AMD-V（SVM）虚拟化支持功能。可以在 Xen hypervisor 未运行时执行如下命令来进行验证： 
    
    $ grep -E "(vmx|svm)" --color=always /proc/cpuinfo
    
如果上述命令无结果输出，则说明硬件虚拟化不受支持，即你的硬件无法运行 HVM 类型的 _domU_ （或是 Xen hypervisor 正在运行中）。如果你认为你的 CPU 支持上述任一种功能，则可以在启动时查看宿主机的 BIOS 设置菜单，检查虚拟化相关的选项是否被禁用。如果相关的选项存在并被禁用，则将其启用，接着启动到系统中并再次使用上述命令进行检查。当 PCI 设备支持时，Xen hypervisor 也可以使用 PCI 直通，不需要 _dom0_ 的硬件支持也可以将 PCI 设备直接连接到 _domU_ 。如需使用 PCI 直通，需要 CPU 支持 IOMMU/VT-d 功能。 

### Installation of the Xen hypervisor

To install the Xen hypervisor, [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [xen](<https://aur.archlinux.org/packages/xen/>)AUR package. It provides the Xen hypervisor, current xl interface and all configuration and support files, including systemd services. To run most VMs, you will also need to install [xen-qemu](<https://aur.archlinux.org/packages/xen-qemu/>)AUR. 

For BIOS support in VMs, install [seabios](<https://archlinux.org/packages/?name=seabios>)包. For UEFI support, install [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包. To boot VM-local kernels inside of a PVH VM, install [xen-pvhgrub](<https://aur.archlinux.org/packages/xen-pvhgrub/>)AUR. 

#### Building xen

It is recommended that xen and its components are built in a clean environment, either in a VM or a chroot. When building Xen, there are environmental variables that can be passed to _makepkg_. 

  1. _build_stubdom_ \-- Build the components to run Xen stubdoms, mainly for [dom0 disaggregation](<https://wiki.xenproject.org/wiki/Dom0_Disaggregation>). Components for stubdom are broken off into _xen-stubdom_ if built. Defaults to false.
  2. _boot_dir_ \-- Your boot directory. Defaults to _/boot_.
  3. _efi_dir_ , _efi_mountpoint_ \-- Your EFI directory and mountpoint. Defaults to _/boot_.

Pass these arguments to makepkg as variables: 
    
    $ build_stubdom=true efi_dir="/boot/EFI" makepkg
    
[xen-docs](<https://aur.archlinux.org/packages/xen-docs/>)AUR will be also built for the man pages and documentation. If you choose to build stubdom support, a _xen-stubdom_ package will be built. 

**注意：** The plan for Xen on Arch Linux is to eventually phase stubdom out in favor of PVH domains.

### Modification of the bootloader

**警告：** Never assume your system will boot after changes to the boot system. This might be the most common error new as well as old users do. Make sure you have a alternative way to boot your system like a USB stick or other livemedia **BEFORE** you make changes to your boot system.

The boot loader must be modified to load a special Xen kernel (`xen.gz` or in the case of UEFI `xen.efi`) which is then used to boot the normal kernel. To do this a new bootloader entry is needed. 

#### UEFI

Xen supports booting from UEFI as specified in [Xen EFI systems](<https://xenbits.xen.org/docs/unstable/misc/efi.html>). It also might be necessary to use [efibootmgr](<../zh-cn/UEFI.html#efibootmgr> "UEFI") to set boot order and other parameters. 

First, ensure the `xen.efi` file is in the [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") along with your kernel and ramdisk files. 

Second, Xen requires an ASCII (no UTF-8, UTC-16, etc) configuration file that specifies what kernel should be booted as [dom0](<https://wiki.xen.org/wiki/Dom0>). This file must be placed in the same [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") as the binary. Xen looks for several configuration files and uses the first one it finds. The order of search starts with the `.efi` extension of the binary's name replaced by `.cfg`, then drops trailing name components at `.`, `-` and `_` until a match is found. Typically, a single file named `xen.cfg` is used with the system requirements, such as: 
    
    xen.cfg
    
    [global]
    default=xen
    
    [xen]
    options=console=vga iommu=force:true,qinval:true,debug:true loglvl=all noreboot=true reboot=no vga=ask ucode=scan
    kernel=vmlinuz-linux root=/dev/sdaX rw add_efi_memmap #earlyprintk=xen
    ramdisk=initramfs-linux.img
    
**提示：** See [Xen efi.cfg](<https://xenbits.xen.org/docs/unstable/misc/efi.html>) for additional parameters in this file. For the options line, see [Xen Command Line options](<https://xenbits.xen.org/docs/unstable/misc/xen-command-line.html>) for a full list of options available such as serial console, limiting dom0 vCPU and memory, scheduling, Intel and AMD microcode and more. For example, [Xen Project Best Practices](<https://wiki.xen.org/wiki/Xen_Project_Best_Practices>) dictates to disabling memory ballooning for dom0. To do that, edit the `xen.cfg` line for `options` to specify the additional parameters.

##### Systemd-boot

**提示：** You can continue to boot the [dom0](<https://wiki.xen.org/wiki/Dom0>) kernel directly even after Xen is installed and configured. This can be useful in the event that an Xen installation becomes unbootable or misconfigured. Therefore, it is recommended to keep the original systemd-boot loader entries configured on the system as rescue boot options and just add additional entries for Xen.

**注意：** At the time of the system's [Systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") installation, the ESP partition should have been mounted to `/boot` as this is where the [Xen](<https://aur.archlinux.org/packages/Xen/>)AUR package and EFI binaries were configured and built for, not `/boot/efi`.

Add a new EFI-type loader entry. See [Systemd-boot#EFI Shells or other EFI applications](<../zh-cn/Systemd-boot.html#EFI_Shells_or_other_EFI_applications> "Systemd-boot") for more details. For example: 
    
    /boot/loader/entries/10-xen.conf
    
    title   Xen Hypervisor
    efi     /xen.efi
    
**注意：** The current [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") and Xen efi binary combination does not allow parameters passed on the `efi` line of the loader's entry. However, the Xen documentation states that `-cfg=file.cfg` can be used as an UEFI Shell parameter which is not true for the efi line option. For now, you can only have one Xen EFI entry which limits you to only one configuration file.

##### EFISTUB

It is possible to boot an EFI kernel directly from UEFI by using [EFISTUB](</wzh/index.php?title=EFISTUB&action=edit&redlink=1> "EFISTUB（页面不存在）"). 

Drop to the build-in [UEFI shell](<../zh-cn/UEFI.html#Launching_UEFI_Shell> "UEFI") and call the EFI file directly. For example: 
    
    Shell> fs0:
    FS0:\> xen.efi
    
Note that a `xen.cfg` configuration file in the [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") is still required as outlined above. In addition, a different configuration file may be specified with the `-cfg=file.cfg` parameter. For example: 
    
    Shell> fs0:
    FS0:\> xen.efi -cfg=xen-rescue.cfg
    
These additional configuration files must reside in the same directory as the Xen EFI binary and linux stub files. 

#### BIOS

Xen supports booting from system firmware configured as BIOS. 

##### GRUB

For [GRUB](<../zh-cn/GRUB.html> "GRUB") users, install the [grub-xen-git](<https://aur.archlinux.org/packages/grub-xen-git/>)AUR package for booting _dom0_ as well as building [PvGrub2](<https://wiki.xenproject.org/wiki/PvGrub2>) images for booting user domains. 

The file `/etc/default/grub` can be edited to customize the Xen boot commands. For example, to allocate 512 MiB of RAM to _dom0_ at boot, modify `/etc/default/grub` by replacing the line: 
    
    #GRUB_CMDLINE_XEN_DEFAULT=""
    
with 
    
    GRUB_CMDLINE_XEN_DEFAULT="dom0_mem=512M"
    
More information on GRUB configuration keys for Xen can be found in the [GRUB documentation](<https://www.gnu.org/software/grub/manual/grub/html_node/Simple-configuration.html#Simple-configuration>). 

After customizing the options, update the bootloader configuration with the following command: 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
More information on using the GRUB bootloader is available at [GRUB](<../zh-cn/GRUB.html> "GRUB"). 

###### Building GRUB images for booting guests

Besides the usual platform targets, the [grub-xen-git](<https://aur.archlinux.org/packages/grub-xen-git/>)AUR package builds GRUB for three additional targets that can be used to boot Xen guests: _i386-xen_ , _i386-xen_pvh_ , and _x86_64-xen_. To create a boot image from one of these targets, first create a GRUB configuration file. Depending on your preference, this file can either locate and load a GRUB configuration file in the guest or it could manage more of the boot process from _dom0_. Assuming all that is needed is to locate and load a configuration file in the guest, add the following to a file, 
    
    grub.cfg
    
    search -s root -f /boot/grub/grub.cfg
    configfile /boot/grub/grub.cfg
    
and then create a [GRUB/Tips and tricks#GRUB standalone](<../zh-cn/GRUB/Tips_and_tricks.html#GRUB_standalone> "GRUB/Tips and tricks") image that will incorporate that file: 
    
     # grub-mkstandalone -O x86_64-xen -o /usr/lib/xen/boot/pv-grub2-x86_64-xen "/boot/grub/grub.cfg=./grub.cfg"
    
Lastly, add that image as value of the kernel in the domU configuration file (for a 64-bit guest in this example): 
    
     kernel = "/usr/lib/xen/boot/pv-grub2-x86_64-xen"
    
More examples of configuring GRUB images for GRUB guests can be found in the Xen Project's [PvGrub2 documentation](<https://wiki.xenproject.org/wiki/PvGrub2>). 

##### Syslinux

For [Syslinux](<../zh-cn/Syslinux.html> "Syslinux") users, add a stanza like this to your `/boot/syslinux/syslinux.cfg`: 
    
    LABEL xen
        MENU LABEL Xen
        KERNEL mboot.c32
        APPEND ../xen-X.Y.Z.gz --- ../vmlinuz-linux console=tty0 root=/dev/sdaX ro --- ../initramfs-linux.img
    
where `X.Y.Z` is your xen version and `/dev/sdaX` is your [root partition](<../zh-cn/Fstab.html#Identifying_file_systems> "Fstab"). 

This also requires `mboot.c32` (and `libcom32.c32`) to be in the same directory as `syslinux.cfg`. If you do not have `mboot.c32` in `/boot/syslinux`, copy it from: 
    
    # cp /usr/lib/syslinux/bios/mboot.c32 /boot/syslinux
    
### Creation of a network bridge

Xen requires that network communications between _domU_ and the _dom0_ (and beyond) be set up manually. The use of both DHCP and static addressing is possible, and the choice should be determined by the network topology. Complex setups are possible, see the [Networking](<https://wiki.xen.org/wiki/Xen_Networking>) article on the Xen wiki for details and `/etc/xen/scripts` for scripts for various networking configurations. A basic bridged network, in which a virtual switch is created in _dom0_ that every _domU_ is attached to, can be set up by creating a [network bridge](<../zh-cn/Network_bridge.html> "Network bridge") with the expected name `xenbr0`. 

See [Network bridge#Creating a bridge](<../zh-cn/Network_bridge.html#Creating_a_bridge> "Network bridge") for details. 

#### Systemd-networkd

See [Systemd-networkd#Bridge interface](<../zh-cn/Systemd-networkd.html#Bridge_interface> "Systemd-networkd") for details. 

#### Network Manager

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Network_bridge#With_NetworkManager](<../zh-cn/Network_bridge.html#With_NetworkManager> "Network bridge")。**

**附注：** Duplicates the main page.（在 [Talk:Xen](<../zh-cn/Talk:Xen.html>) 中讨论）

Gnome's Network Manager can sometime be troublesome. If following the bridge creation section outlined in the [bridges](<../zh-cn/Network_bridge.html> "Network bridge") section of the wiki are unclear or do not work, then the following steps may work. 

Open the Network Settings and disable the interface you wish to use in your bridge (ex enp5s0). Edit the setting to off and uncheck "connect automatically." 

Create a new bridge connection profile by clicking on the "+" symbol in the bottom left of the network settings. Optionally, run: 
    
    # nm-connection-editor
    
to bring up the window immediately. Once the window opens, select Bridge. 

Click "Add" next to the "Bridged Connections" and select the interface you wished to use in your bridge (ex. Ethernet). Select the device mac address that corresponds to the interface you intend to use and save the settings 

If your bridge is going to receive an IP address via DHCP, leave the IPv4/IPv6 sections as they are. If DHCP is not running for this particular connection, make sure to give your bridge an IP address. Needless to say, all connections will fail if an IP address is not assigned to the bridge. If you forget to add the IP address when you first create the bridge, it can always be edited later. 

Now, as root, run: 
    
    # nmcli con show
    
You should see a connection that matches the name of the bridge you just created. Highlight and copy the UUID on that connection, and then run (again as root): 
    
    # nmcli con up <UUID OF CONNECTION>
    
A new connection should appear under the network settings. It may take 30 seconds to a minute. To confirm that it is up and running, run: 
    
    # brctl show
    
to show a list of active bridges. 

Reboot. If everything works properly after a reboot (ie. bridge starts automatically), then you are all set. 

<optional> In your network settings, remove the connection profile on your bridge interface that does NOT connect to the bridge. This just keeps things from being confusing later on. 

### Installation of Xen systemd services

The Xen _dom0_ requires the `xenstored.service`, `xenconsoled.service`, `xendomains.service` and `xen-init-dom0.service` to be [started](</wzh/index.php?title=Started&action=edit&redlink=1> "Started（页面不存在）") and possibly [enabled](</wzh/index.php?title=Enabled&action=edit&redlink=1> "Enabled（页面不存在）"). 

### Confirming successful installation

Reboot your _dom0_ host and ensure that the Xen kernel boots correctly and that all settings survive a reboot. A properly set up _dom0_ should report the following when you run `xl list` as root: 
    
    # xl list
    
    Name                                        ID   Mem VCPUs	State	Time(s)
    Domain-0                                     0   511     2     r-----   41652.9
    
Of course, the Mem, VCPUs and Time columns will be different depending on machine configuration and uptime. The important thing is that _dom0_ is listed. 

In addition to the required steps above, see [best practices for running Xen](<https://wiki.xen.org/wiki/Xen_Best_Practices>) which includes information on allocating a fixed amount of memory and how to dedicate (pin) a CPU core for _dom0_ use. It also may be beneficial to create a xenfs filesystem mount point by including in `/etc/fstab`
    
    none /proc/xen xenfs defaults 0 0
    
### Configure Best Practices

Review [Xen Project Best Practices](<https://wiki.xen.org/wiki/Xen_Project_Best_Practices>) before using Xen. 

## Using Xen

Xen supports both paravirtualized (PV) and hardware virtualized (HVM) _domU_. In the following sections the steps for creating HVM and PV _domU_ running Arch Linux are described. In general, the steps for creating an HVM _domU_ are independent of the _domU_ OS and HVM _domU_ support a wide range of operating systems including Microsoft Windows. To use HVM _domU_ the _dom0_ hardware must have virtualization support. Paravirtualized _domU_ do not require virtualization support, but instead require modifications to the guest operating system making the installation procedure different for each operating system (see the [Guest Install](<https://wiki.xen.org/wiki/Category:Guest_Install>) page of the Xen wiki for links to instructions). Some operating systems (e.g., Microsoft Windows) cannot be installed as a PV _domU_. In general, HVM _domU_ often run slower than PV _domU_ since HVMs run on emulated hardware. While there are some common steps involved in setting up PV and HVM _domU_ , the processes are substantially different. In both cases, for each _domU_ , a "hard disk" will need to be created and a configuration file needs to be written. Additionally, for installation each _domU_ will need access to a copy of the installation ISO stored on the _dom0_ (see the [Download Page](<https://archlinux.org/download/>) to obtain the Arch Linux ISO). 

###  Create a domU "hard disk"

Xen supports a number of different types of "hard disks" including [Logical Volumes](<../zh-cn/LVM.html> "LVM"), [raw partitions](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning"), and image files. To create a [sparse file](<https://en.wikipedia.org/wiki/Sparse_file> "wikipedia:Sparse file"), that will grow to a maximum of 10GiB, called `domU.img`, use: 
    
    $ truncate -s 10G domU.img
    
If file IO speed is of greater importance than domain portability, using [Logical Volumes](<../zh-cn/LVM.html> "LVM") or [raw partitions](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning") may be a better choice. 

Xen may present any partition / disk available to the host machine to a domain as either a partition or disk. This means that, for example, an LVM partition on the host can appear as a hard drive (and hold multiple partitions) to a domain. Note that making sub-partitons on a partition will make accessing those partitions on the host machine more difficult. See [kpartx(8)](<https://man.archlinux.org/man/kpartx.8>) for information on how to map out partitions within a partition. 

### Create a domU configuration

Each _domU_ requires a separate configuration file that is used to create the virtual machine. Full details about the configuration files can be found at the [Xen Wiki](<https://wiki.xenproject.org/wiki/XenConfigurationFileOptions>) or the [xl.cfg(5)](<https://xenbits.xen.org/docs/unstable/man/xl.cfg.5.html>) man page. Both HVM and PV _domU_ share some components of the configuration file. These include 
    
    name = "domU"
    memory = 512
    disk = [ "file:/path/to/ISO,sdb,r", "phy:/path/to/partition,sda1,w" ]
    vif = [ 'mac=00:16:3e:XX:XX:XX,bridge=xenbr0' ]
    
The `name=` is the name by which the xl tools manage the _domU_ and needs to be unique across all _domU_. The `disk=` includes information about both the installation media (`file:`) and the partition created for the _domU_ `phy`. If an image file is being used instead of a physical partition, the `phy:` needs to be changed to `file:`. The `vif=` defines a network controller. The `00:16:3e` MAC block is reserved for Xen domains, so the last three digits of the `mac=` must be randomly filled in (hex values 0-9 and a-f only). 

### Managing a domU

If a _domU_ should be started on boot, create a symlink to the configuration file in `/etc/xen/auto` and ensure the `xendomains` service is set up correctly. Some useful commands for managing _domU_ are: 
    
    # xl top
    # xl list
    # xl console domUname
    # xl shutdown domUname
    # xl destroy domUname
    
##  Configuring a hardware virtualized (HVM) Arch domU

In order to use HVM _domU_ install the [mesa](<https://archlinux.org/packages/?name=mesa>)包, [numactl](<https://archlinux.org/packages/?name=numactl>)包 and [bluez-libs](<https://archlinux.org/packages/?name=bluez-libs>)包 packages. 

A minimal configuration file for a HVM Arch _domU_ is: 
    
    name = 'HVM_domU'
    builder = 'hvm'
    memory = 512
    vcpus = 2
    disk = [ 'phy:/dev/vg0/hvm_arch,xvda,w', 'file:/path/to/ISO,hdc:cdrom,r' ]
    vif = [ 'mac=00:16:3e:00:00:00,bridge=xenbr0' ]
    vnc = 1
    vnclisten = '0.0.0.0'
    vncdisplay = 1
    
Since HVM machines do not have a console, they can only be connected to via a [vncviewer](</wzh/index.php?title=Vncserver&action=edit&redlink=1> "Vncserver（页面不存在）"). The configuration file allows for unauthenticated remote access of the _domU_ vncserver and is not suitable for unsecured networks. The vncserver will be available on port `590X`, where X is the value of `vncdisplay`, of the _dom0_. The _domU_ can be created with: 
    
    # xl create /path/to/config/file
    
and its status can be checked with 
    
    # xl list
    
Once the _domU_ is created, connect to it via the vncserver and install Arch Linux as described in the [Installation guide](<../zh-cn/Installation_guide.html> "Installation guide"). 

##  Configuring a paravirtualized (PV) Arch domU

A minimal configuration file for a PV Arch _domU_ is: 
    
    name = "PV_domU"
    kernel = "/mnt/arch/boot/x86_64/vmlinuz-linux"
    ramdisk = "/mnt/arch/boot/x86_64/initramfs-linux.img"
    extra = "archisobasedir=arch archisodevice=UUID=_YYYY-mm-dd-HH-MM-SS_ -00"
    memory = 512
    disk = [ "phy:/path/to/partition,sda1,w", "file:/path/to/ISO,sdb,r" ]
    vif = [ 'mac=00:16:3e:XX:XX:XX,bridge=xenbr0' ]
    
This file needs to tweaked for your specific use. Most importantly, the `archisodevice=UUID=_YYYY-mm-dd-HH-MM-SS_ -00` line must be edited to use the creation date and time of the ISO being used. 

Before creating the _domU_ , the installation ISO must be loop-mounted. To do this, ensure the directory `/mnt` exists and is empty, then run the following command (being sure to fill in the correct ISO path): 
    
    # mount -o loop /path/to/iso /mnt
    
Once the ISO is mounted, the _domU_ can be created with: 
    
    # xl create -c /path/to/config/file
    
The "-c" option will enter the _domU'_ s console when successfully created. Then you can install Arch Linux as described in the [Installation guide](<../zh-cn/Installation_guide.html> "Installation guide"), but with the following deviations. The block devices listed in the disks line of the cfg file will show up as `/dev/xvd*`. Use these devices when partitioning the _domU_. After installation and before the _domU_ is rebooted, the `xen-blkfront`, `xen-fbfront`, `xen-netfront`, `xen-kbdfront` modules must be added to [Mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio"). Without these modules, the _domU_ will not boot correctly. For booting, it is not necessary to install Grub. Xen has a Python-based grub emulator, so all that is needed to boot is a `grub.cfg` file: (It may be necessary to create the `/boot/grub` directory) 
    
    /boot/grub/grub.cfg
    
    menuentry 'Arch GNU/Linux, with Linux core repo kernel' --class arch --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-core repo kernel-true-__UUID__' {
            insmod gzio
            insmod part_msdos
            insmod ext2
            set root='hd0,msdos1'
            if [ x$feature_platform_search_hint = xy ]; then
              search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1  __UUID__
            else
              search --no-floppy --fs-uuid --set=root __UUID__
            fi
            echo    'Loading Linux core repo kernel ...'
            linux   /boot/vmlinuz-linux root=UUID=__UUID__ ro
            echo    'Loading initial ramdisk ...'
            initrd  /boot/initramfs-linux.img
    }
    
This file must be edited to match the UUID of the root partition. From within the _domU_ , run the following command: 
    
    # blkid
    
Replace all instances of `__UUID__` with the real UUID of the root partition (the one that mounts as `/`).: 
    
    # sed -i 's/__UUID__/12345678-1234-1234-1234-123456789abcd/g' /boot/grub/grub.cfg
    
Shutdown the _domU_ with the `poweroff` command. The console will be returned to the hypervisor when the domain is fully shut down, and the domain will no longer appear in the xl domains list. Now the ISO file may be unmounted: 
    
    # umount /mnt
    
The _domU_ cfg file should now be edited. Delete the `kernel =`, `ramdisk =`, and `extra =` lines and replace them with the following line: 
    
    bootloader = "pygrub"
    
Also remove the ISO disk from the `disk =` line. 

The Arch _domU_ is now set up. It may be started with the same line as before: 
    
    # xl create -c /etc/xen/archdomu.cfg
    
##  常见错误

###  "xl list" complains about libxl

Either you have not booted into the Xen system, or xen modules listed in `xencommons` script are not installed. 

###  "xl create" fails

Check the guest's kernel is located correctly, check the `pv-xxx.cfg` file for spelling mistakes (like using `initrd` instead of `ramdisk`). 

### Creating HVM fails

If creating HVM fails with: 
    
    libxl: error: libxl_dm.c:3131:device_model_spawn_outcome: Domain 33:domain 33 device model: spawn failed (rc=-3)
    libxl: error: libxl_dm.c:3351:device_model_postconfig_done: Domain 33:Post DM startup configs failed, rc=-3
    libxl: error: libxl_create.c:1837:domcreate_devmodel_started: Domain 33:device model did not start: -3
    libxl: error: libxl_aoutils.c:646:libxl__kill_xs_path: Device Model already exited
    
You have missed to install [numactl](<https://archlinux.org/packages/?name=numactl>)包. 

### Arch Linux guest hangs with a ctrl-d message

Press `ctrl-d` until you get back to a prompt, rebuild its initramfs described. 

###  failed to execute '/usr/lib/udev/socket:/org/xen/xend/udev_event' 'socket:/org/xen/xend/udev_event': No such file or directory

This is caused by `/etc/udev/rules.d/xend.rules`. Xend is deprecated and not used, so it is safe to remove that file. 

## See also

  * [The homepage at xen.org](<https://www.xenproject.org/>)
  * [The wiki at xen.org ](<https://wiki.xenproject.org/wiki/Main_Page>)
