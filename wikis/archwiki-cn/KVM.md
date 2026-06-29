相关文章

  * [Category:Hypervisors](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:Hypervisors")
  * [Libvirt](<../zh-cn/Libvirt.html> "Libvirt")

**翻译状态：**

  * 本文（或部分内容）译自 [KVM](<https://wiki.archlinux.org/title/KVM> "arch:KVM")，最近一次同步于 2024-11-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/KVM?diff=0&oldid=801890>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KVM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**KVM** ，[基于内核的虚拟机](<https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine> "wikipedia:Kernel-based Virtual Machine")，是内置于 Linux 内核的 [hypervisor](<https://en.wikipedia.org/wiki/hypervisor> "wikipedia:hypervisor")。在功能上类似于 [Xen](<../zh-cn/Xen.html> "Xen")，但运行起来更简便。与使用模拟的原生 [QEMU](<../zh-cn/QEMU.html> "QEMU") 不同的是，KVM 是 QEMU 的一种特殊的运行模式，这种模式通过内核模块使用 CPU 扩展（[HVM](<https://en.wikipedia.org/wiki/Hardware-assisted_virtualization> "wikipedia:Hardware-assisted virtualization")）进行虚拟化。 

通过 KVM，可以运行多台未修改的 GNU/Linux、Windows 或任何其他操作系统的虚拟机（详情请参阅[客户机支持状态](<https://www.linux-kvm.org/page/Guest_Support_Status>)）。每台虚拟机都有独享的虚拟硬件：网卡、硬盘、显卡等。 

有关 KVM 与 [Xen](<../zh-cn/Xen.html> "Xen")、[VMware](<../zh-cn/VMware.html> "VMware") 和 QEMU 的区别，可查看 [KVM FAQ](<https://www.linux-kvm.org/page/FAQ#General_KVM_information>)。 

本页面不包含使用KVM作为后端的其他虚拟机的通用功能。对于这些信息，你应查看相关的文档。 

##  检查 KVM 支持

###  硬件支持

KVM 需要虚拟机宿主的处理器支持虚拟化（对于 Intel 处理器来说是 VT-x，对于 AMD 处理器来说是 AMD-V）。你可通过以下命令来检查你的处理器是否支持硬件虚拟化： 
    
    $ LC_ALL=C.UTF-8 lscpu | grep Virtualization
    
或者： 
    
    $ grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo
    
如果运行后没有显示，那么你的处理器**不** 支持硬件虚拟化，你**不能** 使用KVM。 

**注意：** 你可能需要在 BIOS 中启用虚拟化支持。10 年内所有由 AMD 和 Intel 生产的 x86_64 处理器都支持虚拟化。如果你的处理器看上去不支持虚拟化，几乎可以确定是因为这项功能在 BIOS 中未启用。

###  内核支持

Arch Linux 内核提供了相应的[内核模块](<../zh-cn/Kernel_modules.html> "Kernel modules")来支持KVM。 

  * 你可以通过以下命令来检查内核中是否已包含必要的模块（`kvm` 以及 `kvm_amd` 和 `kvm_intel` 中的一个）：

    $ zgrep CONFIG_KVM /proc/config.gz
    
只有当模块设置为 `y` 或 `m` 时才可用。 

  * 然后，确认这些内核模块已自动加载：

    $ lsmod | grep kvm
    
    kvm_intel             245760  0
    kvmgt                  28672  0
    mdev                   20480  2 kvmgt,vfio_mdev
    vfio                   32768  3 kvmgt,vfio_mdev,vfio_iommu_type1
    kvm                   737280  2 kvmgt,kvm_intel
    irqbypass              16384  1 kvm
    
如果运行后没有显示，那么需要[手动加载](<../zh-cn/Kernel_modules.html#%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%97%B6%E8%AE%BE%E7%BD%AE> "Kernel modules")这些模块。 

**提示：** 如果 modprobe `kvm_intel` 或 `kvm_amd` 失败，但 modprobe `kvm` 成功，并且 `lscpu` 声称支持硬件加速，检查 BIOS 设置。某些厂商，特别是笔记本电脑厂商，默认禁用这些处理器扩展。modprobe 失败后，[dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg") 的输出可以告诉你这些扩展是硬件不支持还是在 BIOS 中禁用。

##  Virtio 准虚拟化

准虚拟化为客户机提供了一种使用主机上设备的快速有效的通信方式。KVM 使用 **Virtio** API 作为虚拟机管理程序和客户机之间的连接层，为虚拟机提供准虚拟化设备。 

所有 Virtio 设备都包括两部分：主机设备和客户机驱动程序。 

###  内核支持

用以下命令检查**虚拟机中** 内核的 VIRTIO 模块是否可用： 
    
    $ zgrep VIRTIO /proc/config.gz
    
然后，检查这些内核模块是否已自动加载： 
    
    $ lsmod | grep virtio
    
如果运行后没有显示，那么需要[手动加载](<../zh-cn/Kernel_modules.html#%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%97%B6%E8%AE%BE%E7%BD%AE> "Kernel modules")这些模块。 

###  准虚拟化设备列表

  * 网络设备 (virtio-net)
  * 块设备 (virtio-blk)
  * 控制器设备 (virtio-scsi)
  * 串口设备 (virtio-serial)
  * 气球设备 (virtio-balloon)

##  如何使用 KVM

请参考[QEMU](<../zh-cn/QEMU.html> "QEMU")。 

##  小贴士与小技巧

**注意：** 请参考 [QEMU#Tips and tricks](<../zh-cn/QEMU.html#Tips_and_tricks> "QEMU") 和 [QEMU#Troubleshooting](<../zh-cn/QEMU.html#Troubleshooting> "QEMU") 获取通用技巧。

###  嵌套虚拟化

嵌套虚拟化使现有虚拟机能够在第三方虚拟机管理程序和其他虚拟化云平台上运行，而无需对原始虚拟机或其网络进行任何修改。 

在宿主机上，启用 `kvm_intel` 模块的嵌套虚拟化功能： 

**注意：** AMD 操作也类似，只需在必要时将 `intel` 替换为 `amd`
    
    # modprobe -r kvm_intel
    # modprobe kvm_intel nested=1
    
要使嵌套虚拟化永久生效（请参考 [Kernel modules#Setting module options](<../zh-cn/Kernel_modules.html#Setting_module_options> "Kernel modules")）： 
    
    /etc/modprobe.d/kvm_intel.conf
    
    options kvm_intel nested=1

确认嵌套虚拟化功能是否已激活： 
    
    $ cat /sys/module/kvm_intel/parameters/nested
    
    Y

启用主机直通模式以将CPU的所有功能转发给客户操作系统: 

  1. 如果正在使用[QEMU](<../zh-cn/QEMU.html> "QEMU"), 可以使用以下命令运行客户操作系统: `qemu-system-x86_64 -enable-kvm -cpu host`.
  2. 如果使用virt-manager，请将CPU模式更改为 `host-passthrough`。
  3. _如果使用virsh_ , 使用`virsh edit _vm-name_`命令并更改 CPU 行为 `<cpu mode='host-passthrough' check='partial'/>`

现在，启动虚拟机并检查VMX标志是否存在 
    
    $ grep -E --color=auto 'vmx|svm' /proc/cpuinfo
    
###  开启内存大页

可以启用大页 (Huge Pages) 以提高虚拟机的性能。如果您正在使用最新版本的 Arch Linux 并且正在运行 KVM，那么这基本是开箱即用的。请检查是否存在目录 `/dev/hugepages`。如果不存在，请先创建它。现在，我们需要配置正确的权限。默认目录权限是 root 的 uid 和 gid 及 0755，但我们希望 kvm 组中的任何人都可以访问 hugepages。 

在 `/etc/fstab`添加下列内容: 
    
    /etc/fstab
    
    hugetlbfs       /dev/hugepages  hugetlbfs       mode=01770,gid=kvm        0 0

相较于通过 `gid=kvm` 直接指定组名，你也可以使用数字作为 gid，但数字 ID 必须要与 `kvm` 组相一致。`1770` 模式允许所有组成员创建文件，但成员间无法互相取消链接或重命名文件。确保 `/dev/hugepages` 已正确挂载： 
    
    # umount /dev/hugepages
    # mount /dev/hugepages
    $ mount | grep huge
    
    hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,mode=1770,gid=78)

现在可以计算需要多少大页内存了。查看一个大页的大小： 
    
    $ grep Hugepagesize /proc/meminfo
    
通常会是 2048 kB ≙ 2 MB，加入虚拟机的内存是 1024 MB. 1024 / 2 = 512. 额外增加一点，就变成 550。将此数值写入设置： 
    
    # echo 550 > /proc/sys/vm/nr_hugepages
    
如果剩余内存足够: 
    
    $ grep HugePages_Total /proc/meminfo
    
    HugesPages_Total:  550
    
如果数值没有这么大，请关闭其他软件，或减少虚拟机的内存使用(number_of_pages x 2): 
    
    $ qemu-system-x86_64 -enable-kvm -m 1024 -mem-path /dev/hugepages -hda <disk_image> [...]
    
注意 `-mem-path` 参数，这将启用大页。 虚拟机运行时，通过下面命令查看使用了多少个页： 
    
    $ grep HugePages /proc/meminfo
    
    HugePages_Total:     550
    HugePages_Free:       48
    HugePages_Rsvd:        6
    HugePages_Surp:        0
    
如果一切正常，可以默认启动大页了，将下面内容加入 `/etc/sysctl.d/40-hugepage.conf`: 
    
    /etc/sysctl.d/40-hugepage.conf
    
    vm.nr_hugepages = 550

参阅： 

  * [Linux 内核大页支持情况](<https://docs.kernel.org/admin-guide/mm/hugetlbpage.html>)
  * [Debian Wiki - Hugepages](<https://wiki.debian.org/Hugepages> "debian:Hugepages")

###  安全启动

启用 KVM 安全启动前需要满足一下几点： 

  1. 必须使用编译了安全启动的 UEFI.
  2. UEFI 中必须包含加密密钥.

**注意：** Arch Linux 目前没有像 Fedora 等其他发行版一样提供安全启动密钥，如果要安全启动 Arch Linux,需要创建自己的签名密钥并在执行下面命令后用密钥签名内核。更多信息请参考 [Unified Extensible Firmware Interface/Secure Boot](<../zh-cn/Unified_Extensible_Firmware_Interface/Secure_Boot.html> "Unified Extensible Firmware Interface/Secure Boot")。

要启用 UEFI 安全启动支持，请安装 [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包 并将虚拟机设置为使用启用安全启动的 UEFI。如果是使用 [libvirt](<../zh-cn/Libvirt.html> "Libvirt")，可以将如下内容加入虚拟机 XML 配置文件： 
    
    <os firmware="efi">
      <loader readonly="yes" secure="yes" type="pflash">/usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd</loader>
    </os>

下一步需要加入一些密钥，这里我们使用 Microsoft 和 Redhat 的安全启动密钥。安装 [virt-firmware](<https://archlinux.org/packages/?name=virt-firmware>)包 并执行下面命令，将 `_vm_name_` 替换为虚拟机名称。 
    
    $ virt-fw-vars --input /var/lib/libvirt/qemu/nvram/_vm_name_ _VARS.fd --output /var/lib/libvirt/qemu/nvram/_vm_name_ _SECURE_VARS.fd --secure-boot --enroll-redhat
    
编辑 libvirt XML 配置，将其指向新的 VARS 文件。 
    
    <os firmware="efi">
      <loader readonly="yes" secure="yes" type="pflash">/usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd</loader>
      <nvram template="/usr/share/edk2/x64/OVMF_VARS.4m.fd">/var/lib/libvirt/qemu/nvram/**{vm-name}** _SECURE_VARS.fd</nvram>
    </os>

这样安全启动应该就会自动启用了，可以通过虚拟机 UEFI 启动时按 `F2` 按键进行确认。 

##  参阅

  * [KVM Howto](<https://www.linux-kvm.org/page/HOWTO>)
  * [KVM FAQ](<https://www.linux-kvm.org/page/FAQ#General_KVM_information>)
