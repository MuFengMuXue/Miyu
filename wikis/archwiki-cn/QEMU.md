相关文章

  * [Category:Hypervisors](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:Hypervisors")
  * [Libvirt](<../zh-cn/Libvirt.html> "Libvirt")
  * [QEMU/Guest graphics acceleration](</wzh/index.php?title=QEMU/Guest_graphics_acceleration&action=edit&redlink=1> "QEMU/Guest graphics acceleration（页面不存在）")
  * [PCI passthrough via OVMF](<../zh-cn/PCI_passthrough_via_OVMF.html> "PCI passthrough via OVMF")

**翻译状态：**

  * 本文（或部分内容）译自 [QEMU](<https://wiki.archlinux.org/title/QEMU> "arch:QEMU")，最近一次同步于 2024-11-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/QEMU?diff=0&oldid=820328>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/QEMU_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自 [QEMU 关于页面](<https://wiki.qemu.org/Main_Page>)：“QEMU”是一个广泛使用的开源计算机模拟器和虚拟机。" 

当作为架构模拟器时，可以在一种架构（如x86 PC）下运行另一种架构（如ARM）下的操作系统和程序。通过使用动态转换，它可以获得非常好的性能。 

作为虚拟机时，QEMU可以使用其他虚拟机管理程序（如 [Xen](<../zh-cn/Xen.html> "Xen") 或 [KVM](<../zh-cn/KVM.html> "KVM")）来使用 CPU 扩展（[HVM](<https://en.wikipedia.org/wiki/Hardware-assisted_virtualization> "wikipedia:Hardware-assisted virtualization")）进行虚拟化，通过在主机 CPU 上直接执行客户机代码来获得接近于宿主机的性能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [qemu-full](<https://archlinux.org/packages/?name=qemu-full>)包，(或 [qemu-base](<https://archlinux.org/packages/?name=qemu-base>)包，一个无GUI支持的基本版本；[qemu-desktop](<https://archlinux.org/packages/?name=qemu-desktop>)包，默认仅支持 x86_64 模拟） 

并根据需要安装下面的可选软件包： 

  * [qemu-block-gluster](<https://archlinux.org/packages/?name=qemu-block-gluster>)包 \- [Glusterfs](<../zh-cn/Glusterfs.html> "Glusterfs") 设备块支持
  * [qemu-block-iscsi](<https://archlinux.org/packages/?name=qemu-block-iscsi>)包 \- [iSCSI](<../zh-cn/ISCSI.html> "ISCSI") 设备块支持
  * [samba](<https://archlinux.org/packages/?name=samba>)包 \- [SMB/CIFS](<../zh-cn/Samba.html> "Samba") 服务器支持

除了这些之外, [qemu-user-static](<https://archlinux.org/packages/?name=qemu-user-static>)包 提供了 user-mode 下运行静态编译程序的支持。 

###  QEMU 变种

QEMU提供了多个变种以供用户在不同场景中使用。 

粗略地说，QEMU 有两种运行模式： 

全系统模拟模式（full-system emulation）
    在该模式下, QEMU 将会模拟一个完整的系统，包含一个或多个处理器以及各种外围设备。这种模式更加贴近真实的系统，且这种模式不要求被模拟的客户机系统是 Linux，但它的速度较慢。
    QEMU 中启用 full-system 模式的命令依照如下规则进行命名 `qemu-system-_目标机器架构_`，例如 `qemu-system-x86_64` 用于模拟 [x86_64](<https://en.wikipedia.org/wiki/x86_64> "wikipedia:x86 64") 架构 CPU, `qemu-system-i386` 模拟 Intel [32位 x86](<https://en.wikipedia.org/wiki/i386> "wikipedia:i386") 架构 CPU， `qemu-system-arm` 模拟 [32 位 ARM 架构](<https://en.wikipedia.org/wiki/ARM_architecture_family#32-bit_architecture> "wikipedia:ARM architecture family")，`qemu-system-aarch64` 模拟 [64 位 ARM 架构](<https://en.wikipedia.org/wiki/AArch64> "wikipedia:AArch64")，等等。
    如果模拟的 CPU 架构与宿主机的 CPU 架构相同, 那么即使在此模式下，QEMU 仍有可能使用 hypervisor（例如[KVM](<#%E5%90%AF%E7%94%A8_KVM>) 或者 Xen）的技术对模拟机进行加速。
[用户模式（Usermode emulation）](<https://www.qemu.org/docs/master/user/main.html>)
    
    在此模式下, QEMU 能够利用宿主机的系统资源来调用为其他架构编译的 Linux 可执行文件。当然，里面依旧存在一些小问题, 比如说一些功能特性没有被实现, 采用动态链接的可执行文件无法直接在上面使用（参阅[#从x86_64环境中 Chroot 至 arm/arm64 环境](<#%E4%BB%8Ex86_64%E7%8E%AF%E5%A2%83%E4%B8%AD_Chroot_%E8%87%B3_arm/arm64_%E7%8E%AF%E5%A2%83>)解决该问题）并且只支持 Linux 程序（尽管我们可以使用[wine](<https://gitlab.winehq.org/wine/wine/-/wikis/Emulation>)在 Linux 上运行 Windows 程序）。
    QEMU 中启用用户模式的命令依照如下规则进行命名 `qemu-_目标机器架构_`, 例如 `qemu-x86_64` 用于模拟 64 位的 CPU。

QEMU 拥有动态链接和静态链接两个变种： 

动态链接 (默认)
     `qemu-*` 命令依赖于宿主机上的库文件, 因此整个程序体积较小。
静态链接
     `qemu-*` 命令则可以在任何架构相同的 Linux 系统上使用。

在 Arch Linux 中，全系统模拟有两个变种： 

有界面（Non-Headless）（默认）：这个变种启用了一些 GUI 相关的特性，需要额外的依赖（例如 SDL 或 GTK）。
无界面（Headless）：这个变种不需要 GUI 相关的依赖（适用于服务器场景）。

需要注意的是，这两个版本安装的执行文件名称是一样的（例如 `qemu-system-x86_64`），因此系统上不能同时安装这两个版本。 

###  Arch Linux中相关安装包的详细信息

  * [qemu-desktop](<https://archlinux.org/packages/?name=qemu-desktop>)包 包提供了 `x86_64` 架构的模拟器， 可以进行全系统模拟 (`qemu-system-x86_64`)。 [qemu-emulators-full](<https://archlinux.org/packages/?name=qemu-emulators-full>)包包提供了 `x86_64` 用户模式的模拟 (`qemu-x86_64`)。 对于其他支持的架构，这个包都提供了全系统模拟和用户模拟两个变种 (比如说 `qemu-system-arm` 和 `qemu-arm`)。
  * 对应于这些包的无界面版本 (仅适用于全系统模拟模式) 分别是 [qemu-base](<https://archlinux.org/packages/?name=qemu-base>)包(仅`x86_64`) 和 [qemu-emulators-full](<https://archlinux.org/packages/?name=qemu-emulators-full>)包 (其余架构)。
  * 可以用如下独立的安装包中的 QEMU 模块扩展全系统模拟的功能: [qemu-block-gluster](<https://archlinux.org/packages/?name=qemu-block-gluster>)包, [qemu-block-iscsi](<https://archlinux.org/packages/?name=qemu-block-iscsi>)包, 和 [qemu-guest-agent](<https://archlinux.org/packages/?name=qemu-guest-agent>)包。
  * [qemu-user-static](<https://archlinux.org/packages/?name=qemu-user-static>)包 为所有 QEMU 支持的架构提供了一个带用户模式和静态链接模式的变种。 它的QEMU命令依照 `qemu-_target_architecture_ -static`的规则命名, 例如, `qemu-x86_64-static` 代表目标架构为intel 64位CPU。

**注意：** 目前为止，Arch Linux 无论是在官方仓库还是 AUR 仓库中都不提供全系统模式且使用静态链接的 QEMU 变种，原因是很少有人需要它们。

##  QEMU 的图形前端

与其他的虚拟化程序如 [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 和 [VMware](<../zh-cn/VMware.html> "VMware") 不同, QEMU不提供管理虚拟机的GUI（运行虚拟机时出现的窗口除外），也不提供创建具有已保存设置的持久虚拟机的方法。除非您已创建自定义脚本以启动虚拟机，否则必须在每次启动时在命令行上指定运行虚拟机的所有参数。 

[Libvirt](<../zh-cn/Libvirt.html> "Libvirt")提供了一种管理 QEMU 虚拟机的便捷方式。有关可用的前端，请参阅 [libvirt 客户端列表](<../zh-cn/Libvirt.html#%E5%AE%A2%E6%88%B7%E7%AB%AF> "Libvirt")。 

##  创建新虚拟系统

###  创建硬盘镜像

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 如果我没有理解错手册页的话，原始格式只有在文件系统不支持“空洞”或者明确指定了预分配的情况下才会分配全部大小。参见 [qemu-img(1) § NOTES](<https://man.archlinux.org/man/qemu-img.1#NOTES>)。（在 [[主站 Talk:QEMU](<https://wiki.archlinux.org/title/Talk:QEMU>)] 中讨论）

**提示：** 有关QEMU镜像的更多信息，请参阅 [QEMU Wikibook](<https://en.wikibooks.org/wiki/QEMU/Images>)。

除非直接从 CD-ROM 或网络引导（并且不安装系统到本地），运行 QEMU 时都需要硬盘镜像。硬盘镜像是一个文件，存储虚拟机硬盘上的内容。 

一个硬盘镜像可能是 _raw_ 镜像, 和客户机器上看到的内容一模一样，并且将始终使用主机上的来宾硬盘驱动器的全部容量。此方法提供的I / O开销最小，但可能会浪费大量空间，因为guest虚拟机上未使用的空间无法在主机上使用。 

另外一种方式是 _qcow2_ 格式，仅当客户系统实际写入内容的时候，才会分配镜像空间。对客户机器来说，硬盘大小表现为完整大小，即使它可能仅占用主机系统上的非常小的空间。此映像格式还支持QEMU快照功能（有关详细信息，请参阅 [#通过 monitor console 创建快照和管理快照](<#%E9%80%9A%E8%BF%87_monitor_console_%E5%88%9B%E5%BB%BA%E5%BF%AB%E7%85%A7%E5%92%8C%E7%AE%A1%E7%90%86%E5%BF%AB%E7%85%A7>)）。但是，使用此格式而不是 _raw_ 可能会影响性能。 

QEMU 提供 `qemu-img`命令创建硬盘镜像.例如创建一个 4 GiB _raw_ 格式的镜像: 
    
    $ qemu-img create -f raw _image_file_ 4G
    
您也可以用 `-f qcow2` 创建一个 _qcow2_ 镜像。 

用 `dd` 或 `fallocate` 也可以创建一个 _raw_ 镜像。 

**注意：** 您也可以通过 `dd` 或 `fallocate` 创建一个所需大小的 _raw_ 镜像。

**警告：** 如果硬盘镜像存储在 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 系统上，则应在创建任何映像之前考虑禁用该目录的 [写时复制](<../zh-cn/Btrfs.html#Copy-on-Write_\(CoW\)> "Btrfs") 功能。可以在创建镜像时为qcow2格式指定选项nocow：
    
    $ qemu-img create -f qcow2 _image_file_ -o nocow=on 4G

####  Overlay存储镜像

你可以创建一次存储镜像（backing镜像），然后让 QEMU 只保存对backing镜像的变更到一个overlay镜像中。这能让你恢复到这个存储镜像一开始的状态。你可以在想还原时创建一个新的overlay镜像，基于最初的backing镜像。 

要创建一个overlay镜像，执行下面的命令。 
    
    $ qemu-img create -o backing_file=_img1.raw_ ,backing_fmt=_raw_ -f _qcow2_ _img1.cow_
    
之后，你可以正常运行 QEMU 虚拟机（参阅 [#运行虚拟化的系统](<#%E8%BF%90%E8%A1%8C%E8%99%9A%E6%8B%9F%E5%8C%96%E7%9A%84%E7%B3%BB%E7%BB%9F>)）： 
    
    $ qemu-system-i386 _img1.cow_
    
基础镜像（指backing镜像）会保持完好，对存储内容的变更将被记录在overlay镜像文件中。 

当基础镜像的路径改变时，需要进行修复。 

**警告：** 基础镜像的绝对文件系统路径存储在（二进制的）覆写镜像文件中。若改变基础镜像的路径，可能需要做一些调整。

确保原来的基础镜像的路径仍然指向该镜像。如果有必要，在原路径上做一个符号链接到新路径上。然后执行如下命令： 
    
    $ qemu-img rebase -b _/new/img1.raw_ _/new/img1.cow_
    
你也可以选择执行一个 “不安全 ”的重定向，即不检查基础镜像的原路径。 
    
    $ qemu-img rebase -u -b _/new/img1.raw_ _/new/img1.cow_
    
####  调整镜像大小

**警告：** 调整包含NTFS引导文件系统的镜像将无法启动已安装的操作系统，推荐在操作之前进行备份

执行 `qemu-img` 带 `resize` 选项调整硬盘驱动镜像的大小.它适用于 _raw_ 和 _qcow2_. 例如, 增加镜像 10 GiB 大小, 运行: 
    
    $ qemu-img resize _disk_image_ +10G
    
在磁盘映像扩容后，必须使用虚拟机内部系统的分区工具对该镜像进行分区并格式化后才能真正开始使用新空间。 

#####  减小镜像大小

缩小磁盘映像时，必须首先在虚拟机中使用文件系统和分区工具减少分配的文件系统和分区大小，然后再减小磁盘镜像。对于 Windows 虚拟机，可以从“控制面板-创建并格式化硬盘分区”中执行此操作。 

**警告：** 缩小磁盘镜像而不减少虚拟机分区大小将导致数据丢失。

通过以下命令将磁盘镜像减小 10 GiB： 
    
    $ qemu-img resize --shrink _disk_image_ -10G
    
####  转换镜像格式

你可以使用 `qemu-img convert` 来调整镜像格式. 例如，你可以使用一下命令来将 _raw_ 格式的镜像转换成 _qcow2_ 格式的镜像: 
    
    $ qemu-img convert -f raw -O qcow2 _input_.img _output_.qcow2
    
这条命令不会删除 _input_.img 

###  准备安装介质

要将操作系统安装到您的磁盘镜像, 你需要操作系统的安装介质 (例如 光盘, USB设备, 或 ISO 镜像). 不要挂载安装介质，因为 QEMU 要直接访问媒体。 

**提示：** 如果使用光盘，最好先将媒体转储到文件中，因为这既可以提高性能，又不需要您直接访问设备（也就是说，您可以将QEMU作为普通用户，而无需更改对媒体设备文件的访问权限）。例如，如果CD-ROM设备节点名为`/dev/cdrom`，则可以使用以下命令将其转储到文件中：
    
    $ dd if=/dev/cdrom of=_cd_image.iso_

###  安装操作系统

这是你第一次需要去启动模拟器的步骤，为了在磁盘镜像上安装操作系统，你必须同时将磁盘镜像与安装介质装载到虚拟机上，从安装介质中启动操作系统。 

以i386的客户机为例，为了从CD-ROM内的把可用于启动的ISO文件安装到磁盘镜像上，你需要： 
    
    $ qemu-system-x86_64 -cdrom _iso_image_ -boot order=d -drive file=_disk_image_ ,format=raw
    
参阅 [qemu(1)](<https://man.archlinux.org/man/qemu.1>) 获得更多关于不同类型安装介质的信息 (例如floppy，磁盘镜像和物理驱动盘)，参阅 [#运行虚拟化的系统](<#%E8%BF%90%E8%A1%8C%E8%99%9A%E6%8B%9F%E5%8C%96%E7%9A%84%E7%B3%BB%E7%BB%9F>)了解更多有用的选项。 

在安装完操作系统后，就可以直接从QEMU镜像内启动了。（参阅 [#运行虚拟化的系统](<#%E8%BF%90%E8%A1%8C%E8%99%9A%E6%8B%9F%E5%8C%96%E7%9A%84%E7%B3%BB%E7%BB%9F>)） 

**注意：** 默认情况下仅分配给虚拟机128MiB的内存， 分配的内存大小可以通过 `-m` 调整， 比如 `-m 512M` 或 `-m 2G`。

**提示：**

  * 相较于指定 `-boot order=x` ，一部分用户感觉使用 `-boot menu=on` 启用boot菜单的体验更舒服些，至少在配置和实验时是这样的。
  * 当使用无界面（headless）模式时， 将会默认在本地5900端口启动一个VNC服务器， 可以用 [TigerVNC](<../zh-cn/TigerVNC.html> "TigerVNC") 连接到客户机的系统上: `vncviewer :5900`
  * 若你在安装过程中需要替换软盘或CD，可以使用QEMU机器监视器（在虚拟机窗口中按`Ctrl + Alt + 2`）来删除存储设备并将其连接到虚拟机。使用` info block`查看块设备，然后使用`change`命令换出设备。按下` Ctrl + Alt + 1`返回虚拟机。

##  运行虚拟化的系统

`qemu-system-*` 程序 (例如 `qemu-system-i386` 或 `qemu-system-x86_64`, 取决于客户机架构)用来运行虚拟化的客户机。用法是: 
    
    $ qemu-system-i386 _options_ _disk_image_
    
所有 `qemu-system-*`的选项是相同的,参见 [qemu(1)](<https://man.archlinux.org/man/qemu.1>) 查看文档和所有选项 

一般来说，如果一个选项有多个可能的值，你可以使用 
    
    $ qemu-system-x86_64 _option_ _help_
    
来列出所有可能的值。如果它支持属性，你可以使用 
    
    $ qemu-system-x86_64 _option_ _value,help_
    
来列出所有可能的属性。 

例如: 
    
    $ qemu-system-x86_64 -machine help
    $ qemu-system-x86_64 -machine q35,help
    $ qemu-system-x86_64 -device help
    $ qemu-system-x86_64 -device qxl,help
    
你可以使用这些方法和 [qemu(1)](<https://man.archlinux.org/man/qemu.1>) 的文档来理解接下来几个小节中的相关选项。 

默认 QEMU 会在窗口中显示虚拟机的视频输出.有一点要记住:当您单击QEMU窗口,鼠标指针被捕获。要放开，按 `Ctrl+Alt+g`. 

**警告：** QEMU 不应以 root 身份运行. 如果必须以 root 身份在某个脚本中运行 QEMU，那么你需要使用 `-runas` 选项让 QEMU 放弃root 权限

###  启用 KVM

KVM（基于内核的虚拟机）完全虚拟化必须要您的 Linux 内核和硬件支持，并且必须加载必要的[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。更多信息参见 [KVM](<../zh-cn/KVM.html> "KVM")。 

要在 KVM 模式中启动 QEMU, 追加 `-accel kvm` 到启动选项。检查运行中的虚拟机是否启用了 KVM，进入 [QEMU 监视器](<#QEMU_%E7%9B%91%E8%A7%86%E5%99%A8>)，输入 `info kvm`。 

**注意：**

  * `-machine` 选项中的 `accel=kvm` 参数与`-enable-kvm` 或 `-accel kvm` 选项是等价的。
  * CPU模型 `host` 需要 KVM。
  * 如果你使用 GUI 工具去启动 QEMU，但是性能体验极差，那么最好检查一下是否真的开启了 KVM 支持，因为 QEMU 可能选择了备用的软件级模拟。
  * 需要启用 KVM 才能正常启动 Windows 7 和 Windows8，否则会出现“蓝屏”.

###  启用 IOMMU （Intel VT-d/AMD-Vi）的支持

首先，启用 IOMMU。参阅 [PCI passthrough via OVMF#Setting up IOMMU](<../zh-cn/PCI_passthrough_via_OVMF.html#Setting_up_IOMMU> "PCI passthrough via OVMF"). 

添加 `-device intel-iommu` 选项创建 IOMMU 设备: 
    
    $ qemu-system-x86_64 **-enable-kvm -machine q35 -device intel-iommu** -cpu host ..
    
**注意：** 在基于 Intel CPU 的系统上，用 `-device intel-iommu` 创建 QEMU 内的 IOMMU 设备将会禁用 PCI 直通， 并返回一个像这样的错误报告： 
    
    Device at bus pcie.0 addr 09.0 requires iommu notifier which is currently not supported by intel-iommu emulation

虽然仍然需要添加内核参数 `intel_iommu=on` 来重新映射 IO（例如，[通过 vfio-pci 的 PCI 直通](<../zh-cn/PCI_passthrough_via_OVMF.html#Isolating_the_GPU> "PCI passthrough via OVMF")），但如果需要 PCI 直通，则不应设置 `-device intel-iommu`。

###  以 UEFI 模式启动

QEMU 使用的默认固件是 [SeaBIOS](<https://www.coreboot.org/SeaBIOS>)，一个传统 BIOS 的实现。QEMU 使用 `/usr/share/qemu/bios-256k.bin` (由 [seabios](<https://archlinux.org/packages/?name=seabios>)包 提供) 作为默认的只读 (ROM) 镜像。你可以使用参数 `-bios` 来选择另一个固件文件。然而， UEFI 需要可写的内存来正常工作，所以你需要模拟 [PC System Flash](<https://wiki.qemu.org/Features/PC_System_Flash>) 。 

[OVMF](<https://github.com/tianocore/tianocore.github.io/wiki/OVMF>) 是一个为虚拟机提供 UEFI 支持的 TianoCore 项目。它可以通过 [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包 来[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")。 

使用 OVMF 作为固件有两种方法。第一种是复制 `/usr/share/edk2/x64/OVMF.4m.fd` 文件，使其可写并用作 pflash 驱动器: 
    
    -drive if=pflash,format=raw,file=_/copy/of/OVMF.4m.fd_
    
所有对 UEFI 设置的更改将直接保存到此文件中。 

另一种更优选的方法是将 OVMF 分成两个文件。第一个文件将是只读的，并存储固件可执行文件，而第二个文件用作可写的变量存储区。这样做的好处是您可以直接使用固件文件，而无需复制，因此它会由 [pacman](<../zh-cn/Pacman.html> "Pacman") 自动更新。 

使用 `/usr/share/edk2/x64/OVMF_CODE.4m.fd` 作为第一个只读 pflash 驱动器。复制 `/usr/share/edk2/x64/OVMF_VARS.4m.fd` ，使其可写，并用作第二个可写 pflash 驱动器: 
    
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
    -drive if=pflash,format=raw,file=_/copy/of/OVMF_VARS.4m.fd_
    
如果需要启用安全启动，请使用q35机器类型，并将 `/usr/share/edk2/x64/OVMF_CODE.4m.fd` 替换为 `/usr/share/edk2/x64/OVMF_CODE.secboot.fd`。 

###  可信平台模块模拟

QEMU 可以模拟可信平台模块 ([Trusted Platform Module](<../zh-cn/Trusted_Platform_Module.html> "Trusted Platform Module")) ，这是某些系统（例如需要 TPM 2.0 的 Windows 11）所必需的。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [swtpm](<https://archlinux.org/packages/?name=swtpm>)包 ，来提供一个软件 TPM 实现。创建一个目录来存储 TPM 数据 (这里以 `_/path/to/mytpm_` 为例) 。 运行以下命令启动模拟器r: 
    
    $ swtpm socket --tpm2 --tpmstate dir=_/path/to/mytpm_ --ctrl type=unixio,path=_/path/to/mytpm/swtpm-sock_
    
`_/path/to/mytpm/swtpm-sock_` 将由 _swtpm_ 创建: 这是一个 UNIX 套接字，QEMU 将连接到此套接字。您可以将其放在任何目录中。 

默认情况下， _swtpm_ 启动一个 TPM 1.2 模拟器。 `--tpm2` 选项启用 TPM 2.0 模拟。 

最后，将以下选项添加到 QEMU: 
    
    -chardev socket,id=chrtpm,path=_/path/to/mytpm/swtpm-sock_ \
    -tpmdev emulator,id=tpm0,chardev=chrtpm \
    -device tpm-tis,tpmdev=tpm0
    
然后 TPM 将在虚拟机内可用。关闭虚拟机后， _swtpm_ 将自动终止。 

有关更多信息，请参见 [the QEMU documentation](<https://www.qemu.org/docs/master/specs/tpm.html>) 。 

如果虚拟机操作系统仍然无法识别 TPM 设备，请尝试调整可能会导致该问题的 _CPU 模型和拓扑_ 选项。 

##  宿主机和虚拟机数据交互

###  网络

我们可以利用任何支持文件传输的网络协议实现客户机和宿主机之间的数据交互, 例如 [NFS](<../zh-cn/NFS.html> "NFS"), [SMB](</wzh/index.php?title=SMB&action=edit&redlink=1> "SMB（页面不存在）"), [NBD](<https://en.wikipedia.org/wiki/Network_block_device> "wikipedia:Network block device"), HTTP, [FTP](<../zh-cn/Very_Secure_FTP_Daemon.html> "Very Secure FTP Daemon"), 或 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH"), 当然这么做的前提是你已经配置好二者之间的网络，且在系统上启动了相应的服务程序。 

在默认情况下，用户模式的客户机能够通过 10.0.2.2 这个IP访问到宿主机。任何运行于宿主机上的服务端程序都可以通过这个地址被访问到，比如说我们可以通过这个IP访问到宿主机上的 SSH 服务器或 SMB 服务器。因此在这种情况下，客户机能够挂载宿主机通过 [SMB](</wzh/index.php?title=SMB&action=edit&redlink=1> "SMB（页面不存在）") 或 [NFS](<../zh-cn/NFS.html> "NFS") 暴露出来的目录，也可以访问宿主机上的 HTTP 服务器等。通常情况下宿主机无法访问客户机上的服务，不过你也可以通过一些特殊的网络配置达到这个目的 (参阅[#Tap 网络](<#Tap_%E7%BD%91%E7%BB%9C>)) 

###  QEMU 端口转发

**注意：** QEMU's port forwarding is IPv4-only. IPv6 port forwarding is not implemented and the last patches were proposed in 2018.[[1]](<https://lore.kernel.org/qemu-devel/1540512223-21199-1-git-send-email-max7255@yandex-team.ru/T/#u>)

QEMU 能够将宿主机的端口转发到客户机上以实现一些功能，例如从宿主机上访问客户机的 SSH 端口。 

举个例子，将宿主机上的 60022 端口与客户机上的22 (SSH) 端口进行绑定，需通过如下命令启动 QEMU： 
    
    $ qemu-system-x86_64 _disk_image_ -nic user,hostfwd=tcp::60022-:22
    
确认你客户机上的 sshd 程序正在运行，然后可以通过如下命令连接到客户机的 SSH 端口： 
    
    $ ssh _guest-user_ @127.0.0.1 -p 60022
    
你可以用 [SSHFS](<../zh-cn/SSHFS.html> "SSHFS") 把客户机的整个文件系统都挂到宿主机上，这样就可以在宿主机上对客户机的文件系统进行读写了。 

想进行多端口转发的话, 只需要在 `-nic` 参数中指定多个 `hostfwd`, 以 VNC 端口为例: 
    
    $ qemu-system-x86_64 _disk_image_ -nic user,hostfwd=tcp::60022-:22,hostfwd=tcp::5900-:5900
    
###  QEMU 的内置SMB服务器

QEMU的文档中指出它有一个内置的 SMB 服务器，但实际上，它只是在宿主机上加载一个自动生成的 `smb.conf` 配置文件 (位于`/tmp/qemu-smb._random_string_`)，然后启动宿主机上的 [Samba](<../zh-cn/Samba.html> "Samba")，使得客户机能够通过一个IP地址进行访问 (默认的IP地址是10.0.2.4)。这个方法只适用于用户网络，在你不想在宿主机开启通常的 [Samba](<../zh-cn/Samba.html> "Samba") 服务 (客户机同样能访问这类Samba服务) 时这个方法还挺好用的。 

选项 `smb=` 仅可以设置共享一个目录，如果 QEMU 的 SMB 配置允许用户使用符号链接，那么即使在虚拟机运行时也很容易新加入更多的目录，只需要通过在共享目录里创建相应的软链接就行。然而就算并没有这么配置，我们可以依照如下进行配置 SMB 服务器 

宿主机上必须安装 _Samba_ 。通过如下QEMU命令启用这项特性: 
    
    $ qemu-system-x86_64 -nic user,id=nic0,smb=_shared_dir_path_ _disk_image_
    
`_shared_dir_path_` 就是你想要在宿主机和客户机之间共享的目录。 

接着，在客户机内，你应该能够通过 10.0.2.4 访问到名为 qemu 的共享文件夹，例如可以在 Windows 文件浏览器中前往 `\\10.0.2.4\qemu` 这个地址。 

**注意：**

  * 如果你像这样多次指定共享选项：`-net user,smb=_shared_dir_path1_ -net user,smb=_shared_dir_path2_` 或是 `-net user,smb=_shared_dir_path1_ ,smb=_shared_dir_path2_`，qemu 只会共享参数中最后的一个目录。
  * 如果你不能访问共享文件夹且客户机系统为 Windows, 请检查 [NetBIOS 协议是否被启用](<http://ecross.mvps.org/howto/enable-netbios-over-tcp-ip-with-windows.htm>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-05-06 ⓘ] 并确认防火墙没有屏蔽 NetBIOS 协议的 [端口](<https://technet.microsoft.com/en-us/library/cc940063.aspx>)
  * 如果你无法访问共享文件夹且客户机系统为 Windows 10 企业版/教育版或 Windows Server 2016, 请[启用游客访问](<https://support.microsoft.com/en-us/help/4046019>).

共享多个文件夹并在运行时增删文件夹的一个方法是：共享一个空目录，然后在其中创建指向其余共享目录的符号链接。可以用下面的脚本修改SMB服务器的配置，这个脚本还能使宿主机上不允许执行的文件在客户机内拥有执行权限。 
    
    #!/bin/sh
    eval $(ps h -C smbd -o pid,args | grep /tmp/qemu-smb | gawk '{print "pid="$1";conf="$6}')
    echo "[global]
    allow insecure wide links = yes
    [qemu]
    follow symlinks = yes
    wide links = yes
    acl allow execute always = yes" >> "$conf"
    # in case the change is not detected automatically:
    smbcontrol --configfile="$conf" "$pid" reload-config
    
仅当 qemu 启动的客户机第一次访问到网络磁盘后，才能应用该脚本。共享多文件夹的另一个方法是在配置文件里加入额外的共享路径，就像下面这样 
    
    echo "[_myshare_]
    path=_another_path_
    read only=no
    guest ok=yes
    force user=_username_ " >> $conf
    
这个共享文件夹可以在客户机内通过 `\\10.0.2.4\_myshare_` 访问。 

###  使用文件系统直通和 VirtFS

参阅 [QEMU 文档](<https://wiki.qemu.org/Documentation/9psetup>). 

### Host file sharing with virtiofsd

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** See [Help:Style/Formatting and punctuation](</wzh/index.php?title=Help:Style/Formatting_and_punctuation&action=edit&redlink=1> "Help:Style/Formatting and punctuation（页面不存在）").（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

[virtiofsd](<https://archlinux.org/packages/?name=virtiofsd>)包 提供了 virtiofsd 工具。有关可用选项的完整列表，请参阅[在线文档](<https://gitlab.com/virtio-fs/virtiofsd/-/blob/main/README.md?ref_type=heads#user-content-usage>)或 [qemu-docs](<https://archlinux.org/packages/?name=qemu-docs>)包 内置的 `/usr/share/doc/virtiofsd/README.md` 文件。 

由于 qemu 程序需要访问 virtiofsd 套接字，因此请将运行 qemu 的用户添加到 'kvm' [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。你可能需要重新登录才能使更改生效。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Running services as root is not secure. Also the process should be wrapped in a systemd service.（在 [Talk:QEMU](<../zh-cn/Talk:QEMU.html>) 中讨论）

Start as virtiofsd as root: 
    
    # /usr/lib/virtiofsd --socket-path=/var/run/qemu-vm-001.sock --shared-dir /tmp/vm-001 --cache always
    
where 

  * `/var/run/qemu-vm-001.sock` is a socket file,
  * `/tmp/vm-001` is a shared directory between the host and the guest virtual machine.

The created socket file has root only access permission. Give group kvm access to it with: 
    
    # chgrp kvm qemu-vm-001.sock; chmod g+rxw qemu-vm-001.sock
    
Add the following configuration options when starting the virtual machine: 
    
    -object memory-backend-memfd,id=mem,size=4G,share=on \
    -numa node,memdev=mem \
    -chardev socket,id=char0,path=/var/run/qemu-vm-001.sock \
    -device vhost-user-fs-pci,chardev=char0,tag=myfs
    
where 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Explain the remaining options (or remove them if they are not necessary). (在 [Talk:QEMU](<../zh-cn/Talk:QEMU.html>) 中讨论)

  * `size=4G` shall match size specified with `-m 4G` option,
  * `/var/run/qemu-vm-001.sock` points to socket file started earlier,

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** The section should not be specific to Windows.（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

Remember, that guest must be configured to enable sharing. For Windows there are [instructions](<https://virtio-fs.gitlab.io/howto-windows.html>). Once configured, Windows will have the `Z:` drive mapped automatically with shared directory content. 

Your Windows 10 guest system is properly configured if it has: 

  * VirtioFSSService windows service,
  * WinFsp.Launcher windows service,
  * VirtIO FS Device driver under "System devices" in Windows "Device Manager".

If the above installed and `Z:` drive is still not listed, try repairing "Virtio-win-guest-tools" in Windows _Add/Remove programs_. 

###  在宿主机上挂载客户机的分区

在主机系统上挂载驱动器镜像可能很有用，它可以作为在虚拟机和主机之间传输文件的一种方式。这应在虚拟机未运行时进行。 

挂载驱动器的过程取决于 qemu 镜像的类型 (_raw_ 或 _qcow2_) 。我们将在 [#挂载 raw 镜像内的分区](<#Mounting_a_partition_from_a_raw_image>)和 [#挂载 qcow2 镜像内的分区](<#Mounting_a_partition_from_a_qcow2_image>)中详细介绍两种格式的挂载步骤。完整文档请参见[Wikibooks:QEMU/Images#Mounting an image on the host](<https://en.wikibooks.org/wiki/QEMU/Images#Mounting_an_image_on_the_host> "wikibooks:QEMU/Images")。 

**警告：** 请确保重新运行虚拟机之前，所有挂载的分区都被卸载，否则很可能造成磁盘数据的损坏。

####  挂载 raw 镜像内的分区

可以通过将 raw 磁盘镜像文件内的分区设置为环回设备来挂载这些分区。 

#####  手动指出偏移量

挂载磁盘镜像中分区的一个方法是手动指定挂载的偏移量，你可以使用类似下面的命令完成这个操作： 
    
    # mount -o loop,offset=32256 _disk_image_ _mountpoint_
    
`offset=32256` 选项实际上会被传递给 `losetup` 程序，用于设置一个起始地址为 32256 字节处的 loop 设备。接着这个 loop 设备将会被挂载。 你也可以使用 `sizelimit` 选项指定这个分区的具体大小，通常不需要指定该选项。 

具体的偏移量取决于你的磁盘镜像，你所需要的分区可能并不以 32256 字节处作为起始地址。运行 `fdisk -l _disk_image_` 查看磁盘镜像中的分区，fdisk 会显示分区的起始地址和结束地址，地址以 512 字节的扇区为单位，因此需要将该地址乘以 512 获得可用于 `mount` 的字节偏移量。 

#####  loop模块自动检测分区

Linux 的 loop 驱动支持 loopback 设备的分区，不过默认情况下它是关闭的，可以通过下面的方法启用： 

  * 卸载所有 loopback 设备 (比如说卸载所有挂载的镜像)。
  * [卸下](<../zh-cn/Kernel_modules.html#Manual_module_handling> "Kernel modules") `loop` 内核模块, 接着以 `max_part=15` 参数重新加载该模块。 此外，你可以用 `max_loop` 参数设置 loop 设备的最大数量。

**提示：** 你可以在 `/etc/modprobe.d` 增加一个条目使得每次加载 loop 模块时带上 `max_part=15` 参数, 或者把 `loop.max_part=15` 加入内核命令行, 这得看你的内核是否带有 `loop.ko` 模块。

将镜像文件设置为 loopback 设备: 
    
    # losetup -f -P _disk_image_
    
接着，假设创建的loop设备名称为 `/dev/loop0` ，相应的 `/dev/loop0p _X_` 也会被自动创建， X 代表分区的编号，这些分区可以被直接挂载，例如： 
    
    # mount /dev/loop0p1 _mountpoint_
    
如要使用 _udisksctl_ 挂载磁盘镜像, 参阅 [Udisks#Mount loop devices](<../zh-cn/Udisks.html#Mount_loop_devices> "Udisks"). 

#####  使用 kpartx

[multipath-tools](<https://archlinux.org/packages/?name=multipath-tools>)包 包内的 _kpartx_ 可以读取设备的分区表，然后为每个分区创建一个新设备，举个例子： 
    
    # kpartx -a _disk_image_
    
这条命令将会为你设置 loopback 设备，并在 `/dev/mapper/` 下创建必要的分区设备。 

####  挂载 qcow2 镜像内的分区

我们将使用 `qemu-nbd` 完成这一功能, 同时它也能让我们使用 NBD (_network block device_) 协议共享该磁盘镜像。 

首先，我们需要加载 _nbd_ 模块： 
    
    # modprobe nbd max_part=16
    
接着，共享该磁盘并创建设备条目： 
    
    # qemu-nbd -c /dev/nbd0 _/path/to/image.qcow2_
    
进行分区发现检测： 
    
    # partprobe /dev/nbd0
    
_fdisk_ 可以获取 `_nbd0_` 内各分区的相关信息： 
    
    # fdisk -l /dev/nbd0
    
    Disk /dev/nbd0: 25.2 GiB, 27074281472 bytes, 52879456 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xa6a4d542
    
    Device      Boot   Start      End  Sectors  Size Id Type
    /dev/nbd0p1 *       2048  1026047  1024000  500M  7 HPFS/NTFS/exFAT
    /dev/nbd0p2      1026048 52877311 51851264 24.7G  7 HPFS/NTFS/exFAT

接下来可以挂载镜像的任意分区了，比如说我们要挂载分区2： 
    
    # mount /dev/nbd0**p2** _mountpoint_
    
完成任务后，切记卸载镜像文件，然后根据之前的操作一步步还原，即分区并断开与 nbd 设备的连接： 
    
    # umount _mountpoint_
    # qemu-nbd -d /dev/nbd0
    
###  将任意分区作为磁盘镜像唯一主分区

有时，你可能想在 QEMU 中使用物理机的一个系统分区。在虚拟机里使用原始分区可以改善读写性能，因为此时 QEMU 不需要经过宿主机的文件系统层完成读写操作，该分区同样可以用于在宿主机和客户机之间进行数据共享。 

在 Arch Linux 的默认设置中，代表原始分区的设备文件的所有者为 _root_ ， 隶属于 _disk_ 组。如果你希望使用一个非 root 用户能够对原始分区进行读写，那么请更改对应设备文件的所有者为该用户，将这个用户加入 _disk_ 组中，或者使用 [ACL](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "ACL") 完成更精细的权限管理。 

**警告：**

  * 不推荐让虚拟机修改宿主机系统上重要数据，比如说对 root 分区进行修改，尽管你拥有这么做的能力。
  * 不要同时挂载一块在宿主机和客户机内都可读写的分区，否则会造成数据的损坏。

在完成上述设置后，你可以将该分区作为一块虚拟磁盘添加到 QEMU 虚拟机内了。 

然而，如果你想使得 _整个_ 虚拟机都包含在单个分区中，事情就开始变得有些复杂了。在这个场景下，由于系统分区本身是作为文件系统完成格式化的，而非一个带有 MBR 的分区设备，我们便无法在这个分区上安装引导加载程序，进而也就没有办法启动虚拟机了。要启动这类虚拟机，你有如下几种选择：[#手动指定 kernel 和 initrd](<#%E6%89%8B%E5%8A%A8%E6%8C%87%E5%AE%9A_kernel_%E5%92%8C_initrd>)，[#模拟一块带 MBR 的磁盘](<#%E6%A8%A1%E6%8B%9F%E4%B8%80%E5%9D%97%E5%B8%A6_MBR_%E7%9A%84%E7%A3%81%E7%9B%98>)，[#使用设备映射器](<#%E4%BD%BF%E7%94%A8%E8%AE%BE%E5%A4%87%E6%98%A0%E5%B0%84%E5%99%A8>)，[#使用线性 RAID](<#%E4%BD%BF%E7%94%A8%E7%BA%BF%E6%80%A7_RAID>)或是[#使用网络块设备](<#%E4%BD%BF%E7%94%A8%E7%BD%91%E7%BB%9C%E5%9D%97%E8%AE%BE%E5%A4%87>)。 

####  手动指定 kernel 和 initrd

QEMU 支持直接加载 [Linux 内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernels")和 [init ramdisks](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")，从而绕过了类似 [GRUB](<../zh-cn/GRUB.html> "GRUB") 这类的引导加载程序。它会把包含根文件系统的物理分区作为虚拟机的虚拟磁盘，然后启动虚拟机。通过类似下面的命令可以完成这些操作： 

**注意：** 在示例中， 我们使用的是 **宿主机的** 镜像，而非客户机的。如果你希望使用客户机的镜像，请将 `/dev/sda3` 设置为只读（为了保护宿主机上的文件系统），并且指定 `/full/path/to/images` ，或者在客户机内使用一些 kexec 的技巧，重新加载客户机的内核（会延长启动时间）
    
    $ qemu-system-x86_64 -kernel /boot/vmlinuz-linux -initrd /boot/initramfs-linux.img -append root=/dev/sda /dev/sda3
    
在上面这个例子中，宿主机上的 `/dev/sda3` 物理分区被用于客户机的根文件系统，但是在虚拟机内部它的名字则是 `/dev/sda`

当然你可以指定任意一个 kernel 和 initrd，而不局限于Arch Linux提供的。 

`-append` 中可以传递许多[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")， 需要用单引号或双引号将他们包起来，比如： 
    
    ... -append 'root=/dev/sda1 console=ttyS0'
    
####  模拟一块带 MBR 的磁盘

当我们想要既保持物理分区遵循文件系统的格式，又作为客户机的虚拟磁盘包含客户机内的分区时，我们有一个比较复杂的方法，那就是模拟一块带 MBR 的磁盘，这样就使得它可以被类似 GRUB 的引导程序正常启动。 

假设你有一块普通的、未挂载的硬盘分区 `/dev/hda _N_` ，分区内有些文件系统，若想将其制作为QEMU硬盘镜像，需要在该物理分区内动态地预置一个主引导记录（MBR）。更宽泛地说，该分区可以是更大的模拟磁盘中的一部分，尤其是那种模拟了物理磁盘，但仅向虚拟机暴露 `/dev/hda _N_` 名称的块设备。 

这类虚拟磁盘可以用带引用的 VMDK 文件形容，VMDK内的引用指向 MBR 的副本以及实际的分区。 但 QEMU 并不支持这类VMDK格式，例如通过[如下命令创建](<https://www.virtualbox.org/manual/ch09.html#rawdisk>)的虚拟机： 
    
    $ VBoxManage internalcommands createrawvmdk -filename _/path/to/file.vmdk_ -rawdisk /dev/hda
    
将会被QEMU拒绝，并返回一个错误信息 
    
    Unsupported image type 'partitionedDevice'
    
注意 `VBoxManage` 会创建两个文件：` _file.vmdk_` 和 `_file-pt.vmdk_`, 后一个是 `file.vmdk` MBR 的副本。对目标分区外的数据或MBR本身的读操作将会返回0， 而写操作则会被丢弃。 

#####  使用设备映射器

与使用 VMDK 描述文件类似的方法就是使用[设备映射器](<https://docs.kernel.org/admin-guide/device-mapper/index.html>)，设备映射器会在目标分区内添加一份带有 loop 设备的 MBR 文件。在此种情况下，不要求虚拟磁盘与原始分区拥有同样的大小。首先创建一个包含 MBR 的文件： 
    
    $ dd if=/dev/zero of=_/path/to/mbr_ count=2048
    
在这里，我们通过这个命令，使用现代化的磁盘分区程序创建了一个符合分区对齐策略的文件，总共大小为 1MiB（2048 * 512 字节）。为了兼容老式的磁盘分区程序，可能要求其为 63 个扇区而非 2048 个扇区。MBR 表仅占一块512字节的块，剩余的空间可以用于创建一个 BIOS 启动分区，或者在创建一个在混合分区方案中需要用到的 GUID 分区表。接着我们将 loop 设备附加到 MBR 文件上： 
    
    # losetup --show -f _/path/to/mbr_
    
    /dev/loop0

在这个例子里，最终生成的设备为 `/dev/loop0`，设备映射器将会把 MBR 文件与分区结合起来： 
    
    # echo "0 2048 linear /dev/loop0 0
    2048 `blockdev --getsz /dev/hda _N_ ` linear /dev/hda _N_ 0" | dmsetup create qemu
    
生成的 `/dev/mapper/qemu` 可以被作为 QEMU 原生镜像使用了，在虚拟磁盘上创建一个分区表（可参阅关于线性 RAID 的部分），以及相应的引导加载器代码（代码会存放在 `_/path/to/mbr_`）需要额外的步骤。 

下面的步骤中，`/dev/hda _N_` 在虚拟磁盘和物理磁盘上的位置都相同，并且除了 MBR（副本）外磁盘的其余部分都是隐藏的： 
    
    # dd if=/dev/hda count=1 of=_/path/to/mbr_
    # loop=`losetup --show -f _/path/to/mbr_ `
    # start=`blockdev --report /dev/hda _N_ | tail -1 | awk '{print $5}'`
    # size=`blockdev --getsz /dev/hda _N_ `
    # disksize=`blockdev --getsz /dev/hda`
    # echo "0 1 linear $loop 0
    1 $((start-1)) zero
    $start $size linear /dev/hda _N_ 0
    $((start+size)) $((disksize-start-size)) zero" | dmsetup create qemu
    
通过管道传入作为 `dmsetup` 标准输入的是一张表，该表的格式与 `VBoxManage` 创建的VMDK描述文件中的表格式相同， 即我们同样能通过 `dmsetup create qemu --table _table_file_` 加载VMDK描述文件中的表。 对于虚拟机来说， 仅 `/dev/hda _N_` 能被访问， 而对其余部分， 除了第一个扇区外，对其他扇区的读操作都只会返回0， 写操作都会被丢弃。 可以用 `dmsetup table qemu` 显示 `/dev/mapper/qemu` 的表（用 `udevadm info -rq name /sys/dev/block/_major_ :_minor_` 将 `_major_ :_minor_` 转化为类似 `/dev/_blockdevice_` 的名字）。若要删除创建的设备，请使用 `dmsetup remove qemu` 和 `losetup -d $loop`。 

设备映射器方法一个可能的应用场景与Windows XP有关，比如说要在Windows XP安装中进行多引导配置，并且有可能要采用混合分区方案（从物理硬件上说，Windows XP可能是唯一使用MBR分区表的系统，更现代化的操作系统能使用GUID分区表）。Windows XP支持硬件配置文件，因此同样的安装可以选择不同的硬件配置完成（在本例中是裸机与虚拟机），而Windows仅需为每个配置文件安装一次新检测到的硬件的驱动即可。注意在这个例子里， 要更新MBR副本中bootloader代码的部分，使得它直接从 `/dev/hda _N_` 加载Windows XP而不是系统内自带的多引导bootloader（比如GRUB）。或者，将包含bootloader安装的启动分区之副本包含于虚拟磁盘中，同样也可起到类似MBR的作用。 

#####  使用线性 RAID

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** [CONFIG_MD_LINEAR Removal](<https://github.com/torvalds/linux/commit/849d18e27be9a1253f2318cb4549cc857219d991>) Linear RAID has been deprecated since 2021 and removed on Kernel Version 6.8. (在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论)

你同样能用 线性模式（需要 `linear.ko` 内核驱动）的[RAID](<../zh-cn/RAID.html> "RAID")以及一块loop设备完成这件事。 

首先创建一个用于容纳MBR的小文件： 
    
    $ dd if=/dev/zero of=_/path/to/mbr_ count=32
    
这样就创建了一个 16 KiB（32 * 512字节）的小文件。该文件最好不要太小（尽管 MBR 只需要一个512字节大小的块），过小的话将会限制软 RAID 设备的 chunk 大小，对于性能是有影响的。将 loop 设备设置到 MBR 文件上。 
    
    # losetup -f _/path/to/mbr_
    
因为我们尚无法使用其他 loop 设备， 因此就先假设产生的设备名为 `/dev/loop0`。下一步将创建合并式 MBR + 使用软件 RAID 的磁盘镜像 `/dev/hda _N_` ： 
    
    # modprobe linear
    # mdadm --build --verbose /dev/md0 --chunk=16 --level=linear --raid-devices=2 /dev/loop0 /dev/hda _N_
    
这一步产生的 `/dev/md0` 设备将在之后作为一个 QEMU 原始镜像（别忘了给模拟器相应的访问权限）。最后一步（也是比较取巧的一步）是设置磁盘配置，使得 MBR 内主分区的起始地址与 `/dev/md0` 中某一块 `/dev/hda _N_` 的起始地址（在这个例子中是 16 * 512 = 16384 字节的偏移处）。请在宿主机上用 `fdisk` 完成该操作，别在虚拟机里面这么做，因为默认的 QEMU 内的磁盘检测程序常给出无法进行千位舍入的偏移量（比如 31.5 KiB），软件RAID无法处理这样的情况。因此请在主机上进行下面的操作： 
    
    # fdisk /dev/md0
    
按下 `X` 进入专家选单， 设置每个磁道上 's'ectors 的数目，使得一个柱面的大小与MBR文件中相符。对于双磁头柱面，且每个扇区为 512 字节的情况， 每个磁道上的扇区数当为 16， 因此我们通过计算 2x16x512=16k 得到柱面的大小。 

按下 `R` 返回主界面。 

按下 `P` 并检查柱面大小为 16k。 

现在，来创建与 `/dev/hda _N_` 对应的主分区。 设置它的起始地址为柱面2， 结束地址在磁盘的末端（注意现在的柱面编号已经与进入 fdisk 时的编号不同了）。 

最后，把结果写入：完成～ 现在你拥有了一块可以直接从宿主机进行挂载的分区，该分区同样也是 QEMU 磁盘镜像的一部分。 
    
    $ qemu-system-x86_64 -hdc /dev/md0 _[...]_
    
现在，若原始的 `/dev/hda _N_` 分区中包含必要的一些工具，你就可以安全地用 QEMU 在磁盘镜像上设置任何一个引导加载程序。 

#####  使用网络块设备

With [Network Block Device](<https://docs.kernel.org/admin-guide/blockdev/nbd.html>), Linux can use a remote server as one of its block device. 你也可以用 `nbd-server`（在 [nbd](<https://archlinux.org/packages/?name=nbd>)包 包中）为 QEMU 创建一个 MBR 封装器。 

假设你已经用上面所说的方法创建了一个方法创建了一个MBR封装文件，将其重命名为 `wrapper.img.0`。然后在同一个目录下创建一个名为 `wrapper.img.1`的符号链接，指向你选择的分区。然后，还是在这个文件夹下，创建如下的脚本： 
    
    #!/bin/sh
    dir="$(realpath "$(dirname "$0")")"
    cat >wrapper.conf <<EOF
    [generic]
    allowlist = true
    listenaddr = 127.713705
    port = 10809
    
    [wrap]
    exportname = $dir/wrapper.img
    multifile = true
    EOF
    
    nbd-server \
        -C wrapper.conf \
        -p wrapper.pid \
        "$@"

`.0` and `.1` 这两个后缀名是关键，名字的其他其他部分都可以更改。在运行上面的脚本（有可能需要以root身份运行，保证nbd-server能够去访问该分区）后，你可以用如下命令启动QEMU： 
    
    qemu-system-x86_64 -drive file=nbd:127.713705:10809:exportname=wrap _[...]_
    
### Using an entire physical disk device inside the virtual machine

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Duplicates [#Using any real partition as the single primary partition of a hard disk image](<#Using_any_real_partition_as_the_single_primary_partition_of_a_hard_disk_image>), libvirt instructions do not belong to this page.（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

You may have a second disk with a different OS (like Windows) on it and may want to gain the ability to also boot it inside a virtual machine. Since the disk access is raw, the disk will perform quite well inside the virtual machine. 

#### Windows virtual machine boot prerequisites

Be sure to install the [virtio drivers](<https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/>) inside the OS on that disk before trying to boot it in the virtual machine. For Win 7 use version [0.1.173-4](<https://askubuntu.com/questions/1310440/using-virtio-win-drivers-with-win7-sp1-x64>). Some singular drivers from newer virtio builds may be used on Win 7 but you will have to install them manually via device manager. For Win 10 you can use the latest virtio build. 

##### Set up the windows disk interface drivers

You may get a `0x0000007B` bluescreen when trying to boot the virtual machine. This means Windows can not access the drive during the early boot stage because the disk interface driver it would need for that is not loaded / is set to start manually. 

The solution is to [enable these drivers to start at boot](<https://superuser.com/a/1032769>). 

In `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services`, find the folders `aliide, amdide, atapi, cmdide, iastor (may not exist), iastorV, intelide, LSI_SAS, msahci, pciide and viaide`. Inside each of those, set all their "start" values to 0 in order to enable them at boot. If your drive is a PCIe NVMe drive, also enable that driver (should it exist). 

#### Find the unique path of your disk

Run `ls /dev/disk/by-id/`: tere you pick out the ID of the drive you want to insert into the virtual machine, for example `ata-TS512GMTS930L_C199211383`. Now add that ID to `/dev/disk/by-id/` so you get `/dev/disk/by-id/ata-TS512GMTS930L_C199211383`. That is the unique path to that disk. 

#### Add the disk in QEMU CLI

In QEMU CLI that would probably be: 

`-drive file=/dev/disk/by-id/ata-TS512GMTS930L_C199211383,format=raw,media=disk`

Just modify `file=` to be the unique path of your drive. 

#### Add the disk in libvirt

In libvirt XML that translates to 
    
    $ virsh edit _vmname_
    
    ...
        <disk type="block" device="disk">
          <driver name="qemu" type="raw" cache="none" io="native"/>
          <source dev="/dev/disk/by-id/ata-TS512GMTS930L_C199211383"/>
          <target dev="sda" bus="sata"/>
          <address type="drive" controller="0" bus="0" target="0" unit="0"/>
        </disk>
    ...
    
Just modify "source dev" to be the unique path of your drive. 

#### Add the disk in virt-manager

When creating a virtual machine, select "import existing drive" and just paste that unique path. If you already have the virtual machine, add a device, storage, then select or create custom storage. Now paste the unique path. 

##  网络

**警告：** 本部分在翻译过程中，英文wiki产生style告警，这代表日后本节的内容将会有相应调整，暂停本节的翻译： 网络拓扑 ([#仅主机 网络](<#%E4%BB%85%E4%B8%BB%E6%9C%BA_%E7%BD%91%E7%BB%9C>), [#内部网络](<#%E5%86%85%E9%83%A8%E7%BD%91%E7%BB%9C>) 节中以及其他节中引用的部分) 不应当根据不同的虚拟网络接口实现进行划分和描述， 例如[#用户模式](<#%E7%94%A8%E6%88%B7%E6%A8%A1%E5%BC%8F>), [#Tap 网络](<#Tap_%E7%BD%91%E7%BB%9C>), [#通过 VDE2 配置网络](<#%E9%80%9A%E8%BF%87_VDE2_%E9%85%8D%E7%BD%AE%E7%BD%91%E7%BB%9C>)。

采用TAP设备和网桥的虚拟网络的性能应该会比使用用户模式网络或VDE要好，原因在于TAP设备和网桥是在内核中实现的。 

此外，虚拟网络的性能可以通过将 [virtio](<https://wiki.libvirt.org/page/Virtio>) 网络设备直接注册到虚拟机中改善，这比默认情况下模拟 e1000 NIC的性能表现要更好，参阅 [#安装 virtio 驱动](<#%E5%AE%89%E8%A3%85_virtio_%E9%A9%B1%E5%8A%A8>)获得更多相关信息。 

###  关于链路层地址的限制

若在QEMU启动中指定了 `-net nic` 参数，QEMU将会为虚拟机注册一块虚拟网卡，其链路层地址为 `52:54:00:12:34:56` 。然而，当在多台虚拟机之间搭建桥接网络时，每台虚拟机在tap设备的虚拟机端都需要拥有一个独一无二的链路层地址 (MAC)，否则网桥会因为收到多个不同源却拥有相同MAC地址的数据包而无法正常工作。即使你为多个tap设备配置了不同的MAC地址也依旧会出现这个问题，因为当数据包通过tap设备时，tap设备并不会改写包内的链路层地址。 

因此请确保每个虚拟机拥有自己独一无二的网卡地址, 并且它们都以 `52:54:` 开头。 可以通过如下命令手动设置虚拟机的MAC地址, 下面的'X'可以替换成任何16进制字符: 
    
    $ qemu-system-x86_64 -net nic,macaddr=52:54:_XX:XX:XX:XX_ -net vde _disk_image_
    
生成不同的链路层地址有很多方法: 

  * 手动为每个NIC设置独一无二的链路层地址，这么做的优点在于每次启动虚拟机时，DHCP服务器都会将相同的IP地址分配给对应的MAC地址，但是这个方法在需要大量虚拟机的情况下就不适用了。
  * 在每次启动虚拟机时随机生成链路层地址，实际情况下地址冲突的概率可视为0， 不过此方法的缺点在于DHCP服务器每次都会分配一个不同的IP地址。你可以用如下的这些脚本生成随机的链路层地址，并用于 `macaddr` 参数中。

    printf -v macaddr "52:54:%02x:%02x:%02x:%02x" $(( $RANDOM & 0xff)) $(( $RANDOM & 0xff )) $(( $RANDOM & 0xff)) $(( $RANDOM & 0xff ))
    qemu-system-x86_64 -net nic,macaddr="$macaddr" -net vde _disk_image_

  * 使用这个脚本 `qemu-mac-hasher.py` 可以根据虚拟机的名字进行Hash得到一个链路层地址。 只要每台虚拟机的名字是独一无二的, 这个方法就结合了上述两种方法的优点: 每次运行脚本生成的链路层地址都是相同的, 且冲突概率在实际应用中仍可视为0.

    qemu-mac-hasher.py
    
    #!/usr/bin/env python
    # usage: qemu-mac-hasher.py <VMName>
    
    import sys
    import zlib
    
    crc = str(hex(zlib.crc32(sys.argv[1].encode("utf-8")))).replace("x", "")[-8:]
    print("52:54:%s%s:%s%s:%s%s:%s%s" % tuple(crc))

如果要在脚本调用这个方法，你可以参照下面的例子: 
    
    vm_name="_VM Name_ "
    qemu-system-x86_64 -name "$vm_name" -net nic,macaddr=$(qemu-mac-hasher.py "$vm_name") -net vde _disk_image_
    
###  用户模式

默认情况下，没有任何`-netdev`参数，QEMU将使用带有内置DHCP服务器的用户模式网络。当您的虚拟机运行其DHCP客户端时，将为其分配IP地址，它们将能够通过QEMU伪装的IP来访问物理主机的网络。 

**注意：** ICMPv6 尚未完成实现，因此不会起效：`Slirp: external icmpv6 not supported yet`. [Ping](</wzh/index.php?title=Ping&action=edit&redlink=1> "Ping（页面不存在）")ing an IPv6 address will not work.

如果主机已连接Internet，则此默认配置可以使您的虚拟机轻松访问Internet。但是如果您同时启动多个虚拟机，则虚拟机将无法在外部网络上直接看到，虚拟机也将无法相互通信。 

QEMU的用户模式网络可以提供更多功能，例如内置TFTP或SMB服务器，将主机端口重定向到虚拟机（例如，允许SSH连接到虚拟机）或将虚拟机连接到VLAN，以便它们可以彼此通信。 有关更多详细信息，请参见`-net user`标志上的QEMU文档。 

但是，用户模式网络在效用和性能上都有局限性。更高级的网络配置需要使用TAP设备或其他方法。 

**注意：** 如果主机系统使用[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，请确保按照[systemd-networkd#Required services and setup](<../zh-cn/Systemd-networkd.html#Required_services_and_setup> "Systemd-networkd")中的描述对`/etc/resolv.conf`文件进行符号链接，否则虚拟机系统中的DNS查找将无法进行。

**提示：**

  * 使用此选项，虚拟机将使用 virtio 网络驱动程序来进行用户模式网络： `-nic user,model=virtio-net-pci`.
  * 使用此选项，用户模式网络将被隔离，与主机和外部网络隔离开来：`-net user,restrict=y`.

###  Tap 网络

[Tap devices](<https://en.wikipedia.org/wiki/TUN/TAP> "wikipedia:TUN/TAP")是一个Linux内核特性，允许您创建作为真实网络接口的虚拟网络接口。发送到tap接口的包将被传递到一个用户空间程序(如QEMU)，该程序将自己绑定到该接口。 

QEMU可以为虚拟机使用tap网络，因此发送到tap接口的包将被发送到虚拟机，并显示为来自虚拟机中的网络接口(通常是以太网接口)。相反，虚拟机通过其网络接口发送的所有内容都将出现在tap接口上。 

Linux桥接驱动程序支持Tap设备，因此可以将Tap设备彼此桥接在一起，也可以连接其他主机接口，如`eth0`。如果您希望您的虚拟机能够相互通信，或者希望LAN上的其他机器能够与虚拟机通信，那么这是非常理想的方案。 

**警告：** 如果您将tap设备和一些主机接口桥接在一起，例如`eth0`，您的虚拟机将直接出现在外部网络上，这将使它们遭受攻击的可能。根据您的虚拟机可以访问的资源，您可能需要采取所有[precautions](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Firewalls")来保护您的虚拟机。如果风险太大,虚拟机没有资源或您设置多个虚拟机,一个更好的解决方案可能是使用[host-only networking](<#%E4%BB%85%E4%B8%BB%E6%9C%BA_%E7%BD%91%E7%BB%9C>)建立NAT。在这种情况下，您只需要在主机上安装一个防火墙，而不是为每个虚拟机安装多个防火墙。

正如在用户模式网络部分中指出的，tap设备提供比用户模式具有更高的网络性能。如果虚拟机中的操作系统支持virtio网络驱动程序，那么网络性能也会显著提高。假设使用tap0设备，virtio驱动程序在客户端上使用，并且没有使用脚本来帮助启动/停止网络，使用下面的qemu命令： 
    
    -device virtio-net,netdev=network0 -netdev tap,id=network0,ifname=tap0,script=no,downscript=no
    
但是，如果已经使用带有virtio网络驱动程序的Tap设备，则甚至可以通过启用vhost来提高网络性能，例如： 
    
    -device virtio-net,netdev=network0 -netdev tap,id=network0,ifname=tap0,script=no,downscript=no,vhost=on
    
详情请参考：<https://web.archive.org/web/20160222161955/http://www.linux-kvm.com:80/content/how-maximize-virtio-net-performance-vhost-net>

####  仅主机 网络

如果为网桥提供了IP地址，并且使能发往该网桥的流量允许，但没有实际接口（例如`eth0`）连接到网桥，则虚拟机与虚拟机间，虚拟机与主机间能够相互通信。但是，如果您没有在物理主机上设置IP掩蔽，则他们将无法与外部网络进行通信。 此配置被其他虚拟化软件（例如[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox")）称为“仅主机网络模式”。 

**提示：**

  * 如果你想设置IP掩蔽，例如虚拟机的NAT，请查看[Internet sharing#Enable NAT](<../zh-cn/Internet_sharing.html#Enable_NAT> "Internet sharing")页面。
  * 您也许想在网桥接口上运行一个DHCP服务器来服务虚拟网络。例如，使用`172.20.0.1/16`子网，[dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq")作为DHCP服务器:

    # ip addr add 172.20.0.1/16 dev br0
    # ip link set br0 up
    # dnsmasq -C /dev/null --interface=br0 --bind-interfaces --dhcp-range=172.20.0.2,172.20.255.254

####  内部网络

如果您不为网桥提供IP地址并在[iptables](<../zh-cn/Iptables.html> "Iptables")添加INPUT规则链，将所有流向网桥中的数据丢弃，则虚拟机将能够彼此通信，但无法与物理主机或外部网络通信。此配置被其他虚拟化软件（例如[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox")）称为“内部网络”。您将需要为虚拟机分配静态IP地址，或在其中一个虚拟机上运行DHCP服务器。 

在默认情况下，iptables将丢弃桥接网络中的数据包。您可能需要使用这样的iptables规则来允许桥接网络中的数据包: 
    
    # iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
    
####  使用 qemu-bridge-helper 桥接网络

这种方法不需要启动脚本，并且很容易适应多个tap和多个桥。它使用`/usr/lib/qemu/qemu-bridge-helper`，允许在现有桥上创建tap设备。 

**提示：**

  * 参见 [Network bridge](<../zh-cn/Network_bridge.html> "Network bridge") 获取创建网桥的信息
  * See <https://wiki.qemu.org/Features/HelperNetworking> for more information on QEMU's network helper.

首先，创建一个配置文件，包含QEMU使用的所有网桥的名称: 
    
    /etc/qemu/bridge.conf
    
    allow _br0_
    allow _br1_
    ...

Make sure `/etc/qemu/` has `755` [permissions](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions"). [QEMU issues](<https://gitlab.com/qemu-project/qemu/-/issues/515>) and [GNS3 issues](<https://www.gns3.com/community/discussions/gns3-cannot-work-with-qemu>) may arise if this is not the case. 

Now start the virtual machine; the most basic usage to run QEMU with the default network helper and default bridge `br0`: 
    
    $ qemu-system-x86_64 -nic bridge _[...]_
    
Using the bridge `br1` and the virtio driver: 
    
    $ qemu-system-x86_64 -nic bridge,br=_br1_ ,model=virtio-net-pci _[...]_
    
####  手工创建网桥

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** This section needs serious cleanup and may contain out-of-date information.（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

**提示：** 自 QEMU 1.1 起，[network bridge helper](<https://wiki.qemu.org/Features/HelperNetworking>)可以为您设置 tun/tap，而无需其他脚本。 请参阅[#使用 qemu-bridge-helper 桥接网络](<#%E4%BD%BF%E7%94%A8_qemu-bridge-helper_%E6%A1%A5%E6%8E%A5%E7%BD%91%E7%BB%9C>)。

下面介绍如何将虚拟机连接到主机接口，如`eth0`，这可能是最常见的配置。这种配置使虚拟机看起来直接位于外部网络，与物理主机位于同一以太网段。 

我们将用桥适配器替换普通的以太网适配器，然后将普通的以太网适配器绑定到它。 

  * 安装 [bridge-utils](<https://archlinux.org/packages/?name=bridge-utils>)包，它提供 `brctl` 来操作网桥。

  * 启用 IPv4 转发:

    # sysctl -w net.ipv4.ip_forward=1
    
要使更改永久生效，请将 `/etc/sysctl.d/99-sysctl.conf` 中的 `net.ipv4.ip_forward = 0` 更改为 `net.ipv4.ip_forward = 1`。 

  * 加载 `tun` 模块，并将其配置为在引导时加载。详见[Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")。

  * 现在创建桥。有关详细信息，请参见[Bridge with netctl](</wzh/index.php?title=Bridge_with_netctl&action=edit&redlink=1> "Bridge with netctl（页面不存在）")。请记住网桥的命名，如 `br0`，或将以下脚本更改为网桥的名称。In the `run-qemu` script below, `br0` is set up if not listed, as it is assumed that by default the host is not accessing network via the bridge.

  * 创建 QEMU 用于打开 tap 适配器的脚本，该脚本具有 `root:kvm` 750权限:

    /etc/qemu-ifup
    
    #!/bin/sh
    
    echo "Executing /etc/qemu-ifup"
    echo "Bringing up $1 for bridged mode..."
    sudo /usr/bin/ip link set $1 up promisc on
    echo "Adding $1 to br0..."
    sudo /usr/bin/brctl addif br0 $1
    sleep 2
    
  * 创建QEMU用于在`/etc/qemu-ifdown`中关闭tap适配器的脚本，该脚本具有`root:kvm` 750权限:

    /etc/qemu-ifdown
    
    #!/bin/sh
    
    echo "Executing /etc/qemu-ifdown"
    sudo /usr/bin/ip link set $1 down
    sudo /usr/bin/brctl delif br0 $1
    sudo /usr/bin/ip link delete dev $1
    
  * 使用 `visudo` 将以下内容添加到 `sudoers` 文件中:

    Cmnd_Alias      QEMU=/usr/bin/ip,/usr/bin/modprobe,/usr/bin/brctl
    %kvm     ALL=NOPASSWD: QEMU
    
  * 您可以使用以下 `run-qemu` 脚本启动QEMU:

    run-qemu
    
    #!/bin/bash
    : '
    e.g. with img created via:
    qemu-img create -f qcow2 example.img 90G
    run-qemu -cdrom archlinux-x86_64.iso -boot order=d -drive file=example.img,format=qcow2 -m 4G -enable-kvm -cpu host -smp 4
    run-qemu -drive file=example.img,format=qcow2 -m 4G -enable-kvm -cpu host -smp 4
    '
    
    nicbr0() {
        sudo ip link set dev $1 promisc on up &> /dev/null
        sudo ip addr flush dev $1 scope host &>/dev/null
        sudo ip addr flush dev $1 scope site &>/dev/null
        sudo ip addr flush dev $1 scope global &>/dev/null
        sudo ip link set dev $1 master br0 &> /dev/null
    }
    _nicbr0() {
        sudo ip link set $1 promisc off down &> /dev/null
        sudo ip link set dev $1 nomaster &> /dev/null
    }
    
    HASBR0="$( ip link show | grep br0 )"
    if [ -z $HASBR0 ] ; then
        ROUTER="192.168.1.1"
        SUBNET="192.168.1."
        NIC=$(ip link show | grep en | grep 'state UP' | head -n 1 | cut -d":" -f 2 | xargs)
        IPADDR=$(ip addr show | grep -o "inet $SUBNET\([0-9]*\)" | cut -d ' ' -f2)
        sudo ip link add name br0 type bridge &> /dev/null
        sudo ip link set dev br0 up
        sudo ip addr add $IPADDR/24 brd + dev br0
        sudo ip route del default &> /dev/null
        sudo ip route add default via $ROUTER dev br0 onlink
        nicbr0 $NIC
        sudo iptables -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
    fi
    
    USERID=$(whoami)
    precreationg=$(ip tuntap list | cut -d: -f1 | sort)
    sudo ip tuntap add user $USERID mode tap
    postcreation=$(ip tuntap list | cut -d: -f1 | sort)
    TAP=$(comm -13 <(echo "$precreationg") <(echo "$postcreation"))
    nicbr0 $TAP
    
    printf -v MACADDR "52:54:%02x:%02x:%02x:%02x" $(( $RANDOM & 0xff)) $(( $RANDOM & 0xff )) $(( $RANDOM & 0xff)) $(( $RANDOM & 0xff ))
    qemu-system-x86_64 -net nic,macaddr=$MACADDR,model=virtio \
        -net tap,ifname=$TAP,script=no,downscript=no,vhost=on \
        $@
    
    _nicbr0 $TAP
    sudo ip link set dev $TAP down &> /dev/null
    sudo ip tuntap del $TAP mode tap
    
    if [ -z $HASBR0 ] ; then
        _nicbr0 $NIC
        sudo ip addr del dev br0 $IPADDR/24 &> /dev/null
        sudo ip link set dev br0 down
        sudo ip link delete br0 type bridge &> /dev/null
        sudo ip route del default &> /dev/null
        sudo ip link set dev $NIC up
        sudo ip route add default via $ROUTER dev $NIC onlink &> /dev/null
    fi
    
然后，要启动VM，可以这样做： 
    
    $ run-qemu -hda _myvm.img_ -m 512
    
  * 出于性能和安全原因，建议禁用[网桥上的防火墙](<https://ebtables.netfilter.org/documentation/bridge-nf.html>)：

    /etc/sysctl.d/10-disable-firewall-on-bridge.conf
    
    net.bridge.bridge-nf-call-ip6tables = 0
    net.bridge.bridge-nf-call-iptables = 0
    net.bridge.bridge-nf-call-arptables = 0
    
In order to apply the parameters described above on boot, you will also need to load the br-netfilter module on boot. Otherwise, the parameters will not exist when sysctl will try to modify them. 
    
    /etc/modules-load.d/br_netfilter.conf
    
    br_netfilter
    
运行 `sysctl -p /etc/sysctl.d/10-disable-firewall-on-bridge.conf` 立即应用更改。 

参见 [libvirt wiki](<https://wiki.libvirt.org/page/Networking#Creating_network_initscripts>) 和 [Fedora bug 512206](<https://bugzilla.redhat.com/show_bug.cgi?id=512206>)。如果在引导过程中 sysctl 报出关于不存在文件的错误，请在引导时加载 `bridge` 模块。参见[Kernel module#systemd](<../zh-cn/Kernel_module.html#systemd> "Kernel module")。 

或者，您可以配置 [iptables](<../zh-cn/Iptables.html> "Iptables")，通过添加类似这样的规则，允许所有流量通过桥进行转发: 
    
    -I FORWARD -m physdev --physdev-is-bridged -j ACCEPT
    
####  物理设备和 Tap 设备之间通过 iptables 进行网络共享

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Internet_sharing](<../zh-cn/Internet_sharing.html> "Internet sharing")。**

**附注：** Duplication, not specific to QEMU.（在 [Talk:QEMU](<../zh-cn/Talk:QEMU.html>) 中讨论）

桥接网络能在有线接口(例如eth0)之间工作，并且很容易设置。但是，如果主机通过无线设备连接到网络，则无法进行桥接。 

参见 [Network bridge#Wireless interface on a bridge](<../zh-cn/Network_bridge.html#Wireless_interface_on_a_bridge> "Network bridge")。 

解决这个问题的一种方法是，给tap设备设置一个静态IP，使linux自动处理它的路由，然后通过iptables规则转发tap接口和连接到网络的设备之间的通信。 

参见 [Internet sharing](<../zh-cn/Internet_sharing.html> "Internet sharing"). 

在那里你可以找到在设备之间共享网络所需要的东西，包括tap和tun。下面将进一步介绍所需的一些主机配置。如上所述，需要为静态IP配置客户机，使用分配给tap接口的IP作为网关。需要注意的是，如果客户机上的DNS服务器在从一个连接到网络的主机设备切换到另一个时发生了更改，那么它们可能需要手动编辑。 

要在每次启动时允许 IP 转发，需要在 `/etc/sysctl.d` 中，向 sysctl 配置文件添加以下信息: 
    
    net.ipv4.ip_forward = 1
    net.ipv6.conf.default.forwarding = 1
    net.ipv6.conf.all.forwarding = 1
    
iptables规则如下： 
    
    # Forwarding from/to outside
    iptables -A FORWARD -i ${INT} -o ${EXT_0} -j ACCEPT
    iptables -A FORWARD -i ${INT} -o ${EXT_1} -j ACCEPT
    iptables -A FORWARD -i ${INT} -o ${EXT_2} -j ACCEPT
    iptables -A FORWARD -i ${EXT_0} -o ${INT} -j ACCEPT
    iptables -A FORWARD -i ${EXT_1} -o ${INT} -j ACCEPT
    iptables -A FORWARD -i ${EXT_2} -o ${INT} -j ACCEPT
    # NAT/Masquerade (network address translation)
    iptables -t nat -A POSTROUTING -o ${EXT_0} -j MASQUERADE
    iptables -t nat -A POSTROUTING -o ${EXT_1} -j MASQUERADE
    iptables -t nat -A POSTROUTING -o ${EXT_2} -j MASQUERADE
    
假设有3个设备连接到一个内部设备的网络共享流量，例如: 
    
    INT=tap0
    EXT_0=eth0
    EXT_1=wlan0
    EXT_2=tun0
    
前面显示了一个转发，允许与tap设备共享有线和无线连接。 

所示的转发规则是无状态的，用于纯转发。可以考虑限制特定的流量，设置防火墙来保护来宾和其他人。然而，这些会降低网络性能，而简单的网桥不包括这些。 

好处:不管连接是有线还是无线，如果使用tun设备通过VPN连接到远程站点，假设为该连接打开的tun设备是tun0，并且应用了先前的iptables规则，那么远程连接也将与客户机共享。这避免了客户也需要打开VPN连接。同样，由于来宾网络需要是静态的，因此如果以这种方式远程连接主机，很可能需要编辑来宾网络上的DNS服务器。 

###  通过 VDE2 配置网络

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** This section needs serious cleanup and may contain out-of-date information.（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

####  何为VDE?

VDE 全称为 Virtual Distributed Ethernet，作为 [uml](<../zh-cn/User-mode_Linux.html> "User-mode Linux")_switch 的一个扩展，是一个用于管理虚拟网络的工具包 

其基本的思想是创建一个虚拟的开关，就如插座那样，允许虚拟机和物理机通过"插入"连接彼此。下面的配置非常简单，然而，VDE的功能远比展示的更强大，其能够接入虚拟开关，在不同的主机上运行它们并监听开关上的通信。恳请您阅读[该项目的文档](<https://wiki.virtualsquare.org/>)获取更多信息。 

本方法的优点在于无需sudo特权，普通用户一般没有运行modprobe的权限。 

####  基础操作

可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vde2](<https://archlinux.org/packages/?name=vde2>)包 包来获得 VDE 支持。 

在此处配置中，我们使用tun/tap在主机上创建一块虚拟网卡，用如下命令加载`tun`模块(参阅[Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")获取更多信息) 
    
    # modprobe tun
    
现在来创建一个虚拟开关： 
    
    # vde_switch -tap tap0 -daemon -mod 660 -group users
    
这条命令完成了开关创建，`tap0`创建并将其"插入"，然后允许 `users` 组内的用户使用之。 

该网卡已插入，然而还没有进行配置。需要用下面的命令进行配置： 
    
    # ip addr add 192.168.100.254/24 dev tap0
    
现在，只需要以普通用户的身份，指定`-net`参数启动KVM即可： 
    
    $ qemu-system-x86_64 -net nic -net vde -hda _[...]_
    
接下来只需同配置物理机网络一般，对客户机网络进行配置就行。 

**提示：** 你可能想在tap设备上设置NAT，实现在虚拟机内访问互联网，那就参考[Internet sharing#Enable NAT](<../zh-cn/Internet_sharing.html#Enable_NAT> "Internet sharing")获取更多的帮助吧

####  启动脚本

启动VDE的一个示例脚本： 
    
    /etc/systemd/scripts/qemu-network-env
    
    #!/bin/sh
    # QEMU/VDE network environment preparation script
    
    # The IP configuration for the tap device that will be used for
    # the virtual machine network:
    
    TAP_DEV=tap0
    TAP_IP=192.168.100.254
    TAP_MASK=24
    TAP_NETWORK=192.168.100.0
    
    # Host interface
    NIC=eth0
    
    case "$1" in
      start)
            echo -n "Starting VDE network for QEMU: "
    
            # If you want tun kernel module to be loaded by script uncomment here
    	#modprobe tun 2>/dev/null
    	## Wait for the module to be loaded
     	#while ! lsmod | grep -q "^tun"; do echo "Waiting for tun device"; sleep 1; done
    
            # Start tap switch
            vde_switch -tap "$TAP_DEV" -daemon -mod 660 -group users
    
            # Bring tap interface up
            ip address add "$TAP_IP"/"$TAP_MASK" dev "$TAP_DEV"
            ip link set "$TAP_DEV" up
    
            # Start IP Forwarding
            echo "1" > /proc/sys/net/ipv4/ip_forward
            iptables -t nat -A POSTROUTING -s "$TAP_NETWORK"/"$TAP_MASK" -o "$NIC" -j MASQUERADE
            ;;
      stop)
            echo -n "Stopping VDE network for QEMU: "
            # Delete the NAT rules
            iptables -t nat -D POSTROUTING -s "$TAP_NETWORK"/"$TAP_MASK" -o "$NIC" -j MASQUERADE
    
            # Bring tap interface down
            ip link set "$TAP_DEV" down
    
            # Kill VDE switch
            pgrep vde_switch | xargs kill -TERM
            ;;
      restart|reload)
            $0 stop
            sleep 1
            $0 start
            ;;
      *)
            echo "Usage: $0 {start|stop|restart|reload}"
            exit 1
    esac
    exit 0
    
使用上面的脚本作为 systemd 服务： 
    
    /etc/systemd/system/qemu-network-env.service
    
    [Unit]
    Description=Manage VDE Switch
    
    [Service]
    Type=oneshot
    ExecStart=/etc/systemd/scripts/qemu-network-env start
    ExecStop=/etc/systemd/scripts/qemu-network-env stop
    RemainAfterExit=yes
    
    [Install]
    WantedBy=multi-user.target
    
修改 `qemu-network-env` 权限至[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。 

现在可以像其他服务一样，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `qemu-network-env.service` 服务。 

####  备用方法

如果上面的方法不起作用，或者说不想折腾内核配置、TUN、dnsmasq 和 iptables，可以采用下面的方法，也可以获得同样的效果， 
    
    # vde_switch -daemon -mod 660 -group users
    # slirpvde --dhcp --daemon
    
然后，启动 VM 并连接至主机网络中： 
    
    $ qemu-system-x86_64 -net nic,macaddr=52:54:00:00:EE:03 -net vde _disk_image_
    
###  VDE2 网桥

根据 [quickhowto: qemu networking using vde, tun/tap, and bridge](<https://selamatpagicikgu.wordpress.com/2011/06/08/quickhowto-qemu-networking-using-vde-tuntap-and-bridge/>) 所描述的. 任何连接到 vde 上的虚拟机都会暴露给外部。举个例子，每台虚拟机都能直接从 ADSL 路由器那收到 DHCP 的配置信息。 

####  基础操作

首先，你需要有 `tun` 模块并安装了 [bridge-utils](<https://archlinux.org/packages/?name=bridge-utils>)包 包。 

创建一个 vde2/tap 设备： 
    
    # vde_switch -tap tap0 -daemon -mod 660 -group users
    # ip link set tap0 up
    
创建一个网桥: 
    
    # brctl addbr br0
    
添加设备: 
    
    # brctl addif br0 eth0
    # brctl addif br0 tap0
    
配置网桥接口: 
    
    # dhcpcd br0
    
####  启动脚本

所有设备应该都设置好了，且只有网桥拥有IP地址。对于网桥上的物理设备(比如`eth0`)，可以通过[netctl](<../zh-cn/Netctl.html> "Netctl")使用一个自定义的配置文件完成上面所述设置： 
    
    /etc/netctl/ethernet-noip
    
    Description='A more versatile static Ethernet connection'
    Interface=eth0
    Connection=ethernet
    IP=no

下面的systemd服务用于为`users`用户组内的成员创建和启动VDE2 tap网卡。 
    
    /etc/systemd/system/vde2@.service
    
    [Unit]
    Description=Network Connectivity for %i
    Wants=network.target
    Before=network.target
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/bin/vde_switch -tap %i -daemon -mod 660 -group users
    ExecStart=/usr/bin/ip link set dev %i up
    ExecStop=/usr/bin/ip addr flush dev %i
    ExecStop=/usr/bin/ip link set dev %i down
    
    [Install]
    WantedBy=multi-user.target

最后，通过 [netctl 创建网桥](</wzh/index.php?title=Bridge_with_netctl&action=edit&redlink=1> "Bridge with netctl（页面不存在）")。 

###  简化配置参数

如果你经常需要以不同的网络配置选项运行QEMU，就会发现时常得输入大量的 `-netdev` 和 `-device` 选项组合，这些需要大量重复性的劳动。可以用 `-nic` 选项将二者结合，就如下面这样： 
    
    -netdev tap,id=network0,ifname=tap0,script=no,downscript=no,vhost=on -device virtio-net-pci,netdev=network0
    
可简化为: 
    
    -nic tap,script=no,downscript=no,vhost=on,model=virtio-net-pci
    
要注意的是缺失了网络ID，因此将会以`model=`创建这些设备。{ic|-nic}}命令的前半部分参数正是`-netdev`的参数，而后半部分参数（`model=`之后的部分）则与设备有关，原本设备所提供的参数同样可以在此使用（例如，可以指定`smb=`）。若要完全禁用网络，可以用`-nic none`。 

参阅 [QEMU networking文档](<https://qemu.weilnetz.de/doc/6.0/system/net.html>)了解更多的相关参数。 

##  图形

使用 `-display curses` 命令行选项，QEMU 可以模拟一个标准显卡文本模式。这允许用户可以直接在文本终端中直接输入文本或看见文本输出。 `-nographic` 选项起到了类似的作用。 

QEMU 可以根据 `-vga _type_` 参数模拟多种不同的显卡，可用的选项为 `std`,`qxl`,`vmware`,`virtio`,`cirrus` 或 `none`。 

### std

使用 `-vga std` 你可以得到最高 2560 x 1600 像素的分辨率。从 QEMU 2.2 开始是默认选项。 

### qxl

QXL是一个支持 2D 的并行虚拟化图形驱动。需要在客户机中安装驱动并在启动 QEMU 时设置 `-vga qxl` 选项。你可能也会想使用 [#SPICE](<#SPICE>) 优化 QXL 的图形表现。 

在Linux客户机中，需要加载 `qxl` 和 `bochs_drm` 这两个内核模块，以获得一个比较好的效果。 

QXL 设备的默认 VGA 内存大小为 16M，这样的内存大小最高支持 QHD (2560x1440) 的分辨率，如果想要一个更高的分辨率，请[增加vga_memmb](<#%E5%A4%9A%E5%B1%8F%E6%94%AF%E6%8C%81>)。 

### vmware

尽管Bug有点多，但相比于std和cirrus它的表现会更好。对于Arch Linux客户机来说可以安装 [xf86-video-vmware](<https://archlinux.org/packages/?name=xf86-video-vmware>)包 和 [xf86-input-vmmouse](<https://archlinux.org/packages/?name=xf86-input-vmmouse>)包 获取VMware驱动。 

### virtio

`virtio-vga` / `virtio-gpu` 是一个基于[virgl](<https://virgil3d.github.io/>)的3D并行虚拟化图形驱动。目前它已经成熟；目前它仅支持Linux客户机，且需要以`gallium-drivers=virgl`选项编译[mesa](<https://archlinux.org/packages/?name=mesa>)包。 

若要在客户机上启用3D加速，那么需要用 `-device virtio-vga-gl` 选项选择此vga，并用 `-display sdl,gl=on` 或 `-display gtk,gl=on` 在显示设备上启用 OpenGL 上下文，这两个选项分别适用于 SDL 输出和 GTK 输出。如果配置成功了，那么在客户机的 kernel log 里可以看到： 
    
    # dmesg | grep drm 
    
    [drm] pci: virtio-vga detected
    [drm] virgl 3d acceleration enabled
    
### cirrus

cirrus 是[2.2之前](<https://wiki.qemu.org/ChangeLog/2.2#VGA>)默认的图形选项，[不应当](<https://www.kraxel.org/blog/2014/10/qemu-using-cirrus-considered-harmful/>)在现代操作系统中使用它。 

### none

这就像一台完全没有 VGA 卡的 PC，无法通过 `-vnc` 访问它。另外，这种情况与使用 `-nographic` 选项不同，`-nographic` 会让 QEMU 模拟 VGA 卡，只是关闭了 SDL 输出。 

## SPICE

[SPICE project](<https://www.spice-space.org/>) 旨在为用户提供一种完全开源的方式，无缝地对虚拟机进行远程访问。 

###  在宿主机上启用 SPICE 支持

下面是一个启用SPICE作为远程桌面协议的例子，并支持复制和粘贴操作： 
    
    $ qemu-system-x86_64 -vga qxl -device virtio-serial-pci -spice port=5930,disable-ticketing=on -device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0 -chardev spicevmc,id=spicechannel0,name=vdagent
    
这些参数的含义如下： 

  1. `-device virtio-serial-pci` 添加一块 virtio-serial 设备
  2. `-spice port=5930,disable-ticketing` 在 TCP `5930` 端口上进行 spice 频道的监听，允许客户端不经验证即可连接。

**提示：** 使用 [Unix 套接字](<https://en.wikipedia.org/wiki/Unix_socket> "wikipedia:Unix socket") 而非 TCP 端口不会涉及宿主机系统的网络栈，也不意味着可以对数据包进行封装和解封以使用网络和其它相关的协议。这些套接字仅通过硬盘上的 inode 进行表示，这么做是出于性能上的考虑。Unix 套接字可以使用 `-spice unix=on,addr=/tmp/vm_spice.socket,disable-ticketing=on` 代替上述参数。

  1. `-device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0` 在 virtio-serial 设备上为 spice vdagent 打开一个端口。
  2. `-chardev spicevmc,id=spicechannel0,name=vdagent` 为该端口添加一块 spicevmc 字符设备。`virtserialport` 的 `chardev=` 选项需要与 `chardev` 的 `id=` 相符，在本例中是 `spicechannel0`。将端口名字设置为 `com.redhat.spice.0` 也很重要，因为它就是 vdagent 在客户机上所搜索的命名空间。最后，指定 `name=vdagent` 选项使得 spice 知道该频道的服务对象。

###  通过 SPICE 客户端连接到客户机

若要连接到客户机上必须要有一个 SPICE 客户端。在 Arch 中，有如下可用的客户端： 

  * **virt-viewer** — 协议开发者所推荐的 SPICE 客户端，是 virt-manager 项目的子集。

     <https://virt-manager.org/> || [virt-viewer](<https://archlinux.org/packages/?name=virt-viewer>)包

  * **spice-gtk** — SPICE GTK 客户端，SPICE 项目的一个子集，作为小部件嵌入其它应用中。

     <https://www.spice-space.org/> || [spice-gtk](<https://archlinux.org/packages/?name=spice-gtk>)包

若需要能在智能手机上运行的客户端，或者其他平台的客户端，参照 [spice-space download](<https://www.spice-space.org/download.html>) 中的 _Other clients_ 章节。 

####  手动开启 SPICE 客户端

连接到一个监听在 Unix 套接字 `/tmp/vm_spice.socket` 上的客户机的方法是用 `$ remote-viewer spice+unix:///tmp/vm_spice.socket` 或 `$ spicy --uri="spice+unix:///tmp/vm_spice.socket"` 命令手动运行 SPICE 客户端，使用的客户端取决于你的喜好。SPICE 模式下的 QEMU 就如一个远程桌面服务器，可能使用 `-daemonize` 参数以daemon 模式运行 QEMU 会更方便一些。 

**提示：** 可以用下面的命令，通过 SSH 隧道连接到客户机：
    
    $ ssh -fL 5999:localhost:5930 _my.domain.org_ sleep 10; spicy -h 127.0.0.1 -p 5999

。这个例子中 _spicy_ 连接到了本地的 `5999` 端口，该端口通过 SSH 转发至 _my.domain.org_ 上的 SPICE 服务器端口 `5930`。要注意 `-f` 选项让 ssh 在后台执行了 `sleep 10` 命令。这种情况下，在客户端存活时 ssh 会话保持运行，在客户端结束运行时将自动关闭 ssh 会话。

####  QEMU 运行时启动SPICE

QEMU 可以自动地开启一个 SPICE 客户端并创建一个合适的套接字。如果通过 `-display spice-app` 参数将显示设置为SPICE，那么将会使用系统默认的 SPICE 客户端作为 viewer，默认的客户端取决于你的[mimeapps.list](<../zh-cn/XDG_MIME_Applications.html#mimeapps.list> "XDG MIME Applications")文件。 

###  在客户机上开启SPICE的支持

对于**Arch Linux客户机** ，如要支持多屏和共享剪贴板，需要安装以下的包： 

  * [spice-vdagent](<https://archlinux.org/packages/?name=spice-vdagent>)包: Spice的xorg客户端代理，使得用户能够在客户端和X-session之间进行复制和粘贴等。(Refer to this [issue](<https://github.com/systemd/systemd/issues/18791>), until fixed, for workarounds to get this to work on non-GNOME desktops.)
  * [xf86-video-qxl](<https://archlinux.org/packages/?name=xf86-video-qxl>)包: Xorg X11 qxl视频驱动
  * [x-resize](<https://aur.archlinux.org/packages/x-resize/>)AUR: 除 GNOME 之外的桌面环境在 SPICE 客户端窗口大小调整时不会自动反应。此软件包使用 [udev](<../zh-cn/Udev.html> "Udev") 规则和 [xrandr](<../zh-cn/Xrandr.html> "Xrandr") 为所有基于 X11 的桌面环境和窗口管理器实现自动调整大小。

对于**其它的操作系统** 客户机, 参照[spice-space download](<https://www.spice-space.org/download.html>)的 _Guest_ 章节。 

###  开启 SPICE 口令验证

若要启用 SPICE 的口令验证，需要从 `-spice` 的参数中移除 `disable-ticketing`，改为 `password=_yourpassword_`，例如： 
    
    $ qemu-system-x86_64 -vga qxl -spice port=5900,password=_yourpassword_ -device virtio-serial-pci -device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0 -chardev spicevmc,id=spicechannel0,name=vdagent
    
现在 SPICE 客户端在连接 SPICE 服务器的时候应该就会进行口令询问了。 

###  用 TLS 对与 SPICE 的通信进行加密

同样可以为客户端与 SPICE 服务器的通信配置 TLS 加密。首先，需要有一个包含如下文件的目录（文件名必须与下面保持一致）： 

  * `ca-cert.pem`: CA 主证书。
  * `server-cert.pem`: `ca-cert.pem` 签名后的服务器证书。
  * `server-key.pem`: 服务器的私钥。

[Spice User Manual](<https://www.spice-space.org/spice-user-manual.html#_generating_self_signed_certificates>)还展示了使用服务器自己生成的CA生成自签名证书的例子。 

这些完成后，你可以用前文描述的 `-spice` 的参数在 QEMU 启动时自动开启 SPICE：`-spice tls-port=5901,password=_yourpassword_ ,x509-dir=_/path/to/pki_certs_`，其中 `_/path/to/pki_certs_` 代表包含那三个文件的目录。 

现在可以用 [virt-viewer](<https://archlinux.org/packages/?name=virt-viewer>)包 连接到服务器了： 
    
    $ remote-viewer spice://_hostname_?tls-port=5901 --spice-ca-file=_/path/to/ca-cert.pem_ --spice-host-subject="C=_XX_ ,L=_city_ ,O=_organization_ ,CN=_hostname_ " --spice-secure-channels=all
    
要记住的是，`--spice-host-subject` 参数需要根据你的 `server-cert.pem` 中的子条目进行设置。此外还需要将 `ca-cert.pem` 复制到每个客户端上用于验证服务器证书。 

**提示：** 使用下面的命令，就可以获得服务器证书中的子条目格式，可用于 `--spice-host-subject` 参数中（以逗号进行分隔）： 
    
    $ openssl x509 -noout -subject -in server-cert.pem | cut -d' ' -f2- | sed 's/\///' | sed 's/\//,/g'

等效的 [spice-gtk](<https://archlinux.org/packages/?name=spice-gtk>)包 命令为: 
    
    $ spicy -h _hostname_ -s 5901 --spice-ca-file=ca-cert.pem --spice-host-subject="C=_XX_ ,L=_city_ ,O=_organization_ ,CN=_hostname_ " --spice-secure-channels=all
    
## VNC

可以用`-vnc :_X_`选项将QEMU的VGA输出重定向至VNC会话中。将` _X_`替换为输出目标的编号（0代表之后监听在5900，1代表监听在5901...）。 
    
    $ qemu-system-x86_64 -vnc :0
    
在[#开机时启动QEMU虚拟机](<#%E5%BC%80%E6%9C%BA%E6%97%B6%E5%90%AF%E5%8A%A8QEMU%E8%99%9A%E6%8B%9F%E6%9C%BA>)这一小节中同样提供了一个VNC的示例。 

**警告：** 默认的 VNC 服务器没有使用任何验证手段，用户可以从任何主机上连接到 VNC。

###  基本的口令验证

可以通过使用`password`选项很容易地设置访问口令。必须在QEMU Monitor中指定口令，仅当用户提供口令时才有可能连接到VNC。 
    
    $ qemu-system-x86_64 -vnc :0,password -monitor stdio
    
在QEMU Monitor中设置口令需使用 `change vnc password` 命令，然后指定一个口令。 

底下的命令将在启动 VNC 时直接为其设置口令： 
    
    $ printf "change vnc password\n%s\n" MYPASSWORD | qemu-system-x86_64 -vnc :0,password -monitor stdio
    
**注意：** 口令被限制在8个字符内，可以用暴力破解的方式猜到口令。因此在公网上推荐使用更细致的保护措施。

##  音频

###  创建音频后端

`-audiodev` 标识用于设定后端音频驱动及其相关选项。 

To list availabe audio backend drivers: 
    
    $ qemu-system-x86_64 -audiodev help
    
在 [qemu(1)](<https://man.archlinux.org/man/qemu.1>)man 页面中详细列出了可用的后端音频驱动以及可选的设置项。 

最简单的情况下，你需要选择一个驱动并设置一个 id。以 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 为例： 
    
    -audiodev pa,id=snd0
    
###  使用音频后端

#### Intel HD Audio

模拟 Intel HD Audio 需要添加控制器和编解码器设备。可以用如下命令列出可用的 Intel HDA Audio 设备： 
    
    $ qemu-system-x86_64 -device help | grep hda
    
添加音频控制器： 
    
    -device ich9-intel-hda
    
添加音频编解码器并将其映射到宿主机的音频后端 id 上。 
    
    -device hda-output,audiodev=snd0
    
#### Intel 82801AA AC97

模拟 AC97 需要添加声卡设备并将其映射到宿主机的一个音频后端 id 上。 
    
    -device AC97,audiodev=snd0
    
**注意：**

  * 如果没有提供 audiodev 后端，QEMU 会自动查找并添加它，这只适用于单个 audiodev。例如，`-device intel-hda -device hda-duplex` 将使用默认的 audiodev 后端在客户机上模拟 `intel-hda`。
  * 客户机的显卡模拟驱动也可能导致声音质量的问题，需要逐一测试以使其正常工作。你可以用 `qemu-system-x86_64 -h | grep vga` 列出可能的选项。

#### VirtIO sound

自 QEMU 8.2.0 版本开始，VirtIO 声卡也可用。使用方式如下： 
    
    -device virtio-sound-pci,audiodev=my_audiodev -audiodev alsa,id=my_audiodev
    
更多信息可以在 [QEMU 文档](<https://www.qemu.org/docs/master/system/devices/virtio-snd.html>)中找到。 

##  安装 virtio 驱动

QEMU 为用户提供并行虚拟化块设备和网络设备的能力，其是借助 [virtio](<https://wiki.libvirt.org/page/Virtio>) 驱动实现的，拥有更好的性能表现以及更低的开销。 

  * virtio块设备需要使用 `-drive` 指定一个 disk image 的参数，且需要带上`if=virtio`参数：

    $ qemu-system-x86_64 -drive file=_disk_image_ ,if=**virtio**
    
  * 网络配置也是类似的：

    $ qemu-system-x86_64 -nic user,model=**virtio-net-pci**
    
**注意：** 仅有当客户机有 virtio 设备对应的驱动时该方法才能起效，Linux 是有这方面支持的，而在 Arch Linux 中已经包含所需的驱动了，不过无法保证这些驱动能够兼容其他操作系统。

###  Arch Linux 客户机

要在Arch Linux客户机中使用virtio设备，必须在客户端加载以下模块：{`virtio`、`virtio_pci`、`virtio_blk`、`virtio_net`、`virtio_ring`。对于32位系统来说，不需要特定的“virtio”模块。 

如果希望从 virtio 磁盘引导，ramdisk 必须包含必要的模块。默认情况下，这是由 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 的 `autodetect` 钩子处理的。否则要在 `/etc/mkinitcpio.conf` 中使用 `MODULES` 数组包含必要的模块并重新构建 ramdisk。 
    
    /etc/mkinitcpio.conf
    
    MODULES=(virtio virtio_blk virtio_pci virtio_net)

Virtio 磁盘公认的前缀为 `**v**`（例如：`**v** da`，`**v** db`，等等）。因此，当从 virtio 磁盘启动时，需要在 `/etc/fstab` 和 `/boot/grub/grub.cfg` 中进行更改。 

**提示：** 当在 `/etc/fstab` 和引导加载程序中通过 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID") 引用磁盘时，不需要执行任何操作。

关于使用KVM进行半虚拟化的更多信息，可以参考[这里](<https://www.linux-kvm.org/page/Boot_from_virtio_block_device>)。 

您可以安装 [qemu-guest-agent](<https://archlinux.org/packages/?name=qemu-guest-agent>)包 来实现对 QMP 命令的支持，从而增强管理程序的管理能力。安装完成后，您需要启动`qemu-guest-agent.service`。 

###  Windows 客户机

####  Windows 的 Virtio 驱动

Windows 系统不自带 virtio 驱动程序。最新和稳定版本的驱动程序由 Fedora 定期构建，有关下载驱动程序的详细信息可以在 GitHub 上的 [virtio-win](<https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md>) 项目中找到。 在以下部分中，我们将主要使用由 [virtio-win.iso](<https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso>) 提供的稳定 ISO 文件。或者，可以使用 [virtio-win](<https://aur.archlinux.org/packages/virtio-win/>)AUR。 

####  块设备驱动

#####  安装一个新的Windows

需要在系统安装时通过 ISO 加载驱动，具体操作是在主磁盘设备和 Windows 安装盘外挂载一个额外的 cdrom 设备，将系统镜像与 virtio 驱动一同加载： 
    
    $ qemu-system-x86_64 ... \
    -drive file=_disk_image_ ,index=0,media=disk,if=virtio \
    -drive file=_windows.iso_ ,index=2,media=cdrom \
    -drive file=_virtio-win.iso_ ,index=3,media=cdrom \
    ...
    
在安装过程中，Windows Installer 会询问你“Where do you want to install Windows?”，其会返回一个警告表示没有找到任何磁盘设备。接下来跟着如下示例中的步骤进行操作（基于Windows Server 2012 R2 with Update）： 

  * 选择选项 _加载驱动_
  * 反选 _隐藏与这个计算机硬件不兼容的驱动_
  * 按 浏览 按钮并选择 virtio iso 的 CDROM ，一般命名为 "virtio-win-XX"
  * 然后浏览 `E:\viostor\[your-os]\amd64` ，选择它并确认

现在应该能看到 virtio 磁盘出现在列表中了，等待被选中、格式化并安装。 

#####  将现有的 Windows VM 转为使用 virtio

可将现有的 Windows 客户机改为从 virtio 磁盘中启动，前提是客户机中有 virtio 驱动，且该驱动在启动期间就被加载。 

然后我们需要让 Windows 在 Windows 能以 virtio 模式启动一个磁盘镜像之前，在启动时加载 virtio 驱动。 

先创建一个新的磁盘镜像，用于搜索 virtio 驱动： 
    
    $ qemu-img create -f qcow2 _fake.qcow2_ 1G
    
挂载 fake 磁盘（处于virtio模式下）和带有驱动的CD-ROM，运行原本的Windows客户机（启动盘依旧是处于IDE模式中）： 
    
    $ qemu-system-x86_64 -m 4G -drive file=_disk_image_ ,if=ide -drive file=_fake.qcow2_ ,if=virtio -cdrom virtio-win.iso
    
Windows会自动检测fake磁盘，并搜索适配的驱动。如果失败了，前往 _Device Manager_ ，找到SCSI驱动器（带有感叹号图标，应处于打开状态），点击 _Update driver_ 并选择虚拟的CD-ROM。不要定位到CD-ROM内的文件夹了，只选择CD-ROM设备就行，Windows会自动找到合适的驱动的。（已在Windows 7 SP1中完成测试）。 

可以让Windows从下一次起为以安全模式启动，可以用Windows上的 _msconfig.exe_ 工具完成该配置，在安全模式中所有的驱动都会在boot期间被加载，包括我们新装的virtio驱动。只要Windows知道boot期间需要加载virtio，在未来的boot过程中Windows都会记住该设置的。 

将客户机配置为安全模式启动后，可以关机并重新启动它，现在可以以 virtio 模式挂载 boot 磁盘： 
    
    $ qemu-system-x86_64 -m 4G -drive file=_disk_image_ ,if=virtio
    
现在应当能携带 virtio 驱动启动到安全模式中，你可以返回到 _msconfig.exe_ 中禁用安全模式并重启 Windows。 

**注意：** 如果使用`if=virtio`参数时碰上了蓝屏问题，这代表virtio磁盘驱动可能没有在boot期间被安装，以安全模式重启之，然后检查你的驱动配置。

####  网络驱动

安装virtio网络驱动程序要容易一些，只需如上所述添加`-net`参数即可。 
    
    $ qemu-system-i386 -m 4G -vga std -drive file=_windows_disk_image_ ,if=virtio -net nic,model=virtio -cdrom virtio-win-0.1-185.iso
    
Windows将检测网络适配器并尝试为其找到驱动程序。如果失败，请转到“设备管理器”，找到带有感叹号图标的网络适配器（双击打开），切换到驱动程序并单击“更新驱动程序”，然后选择虚拟CD-ROM。别忘了选中显示要递归搜索目录的复选框。 

####  Balloon 驱动

如果想要追踪客户机内存状态（比如通过`virsh`的`dommemstat`命令）或者在运行时改变客户机内存大小（尽管依然无法改变实际的内存大小，不过可以通过inflating balloon驱动限制内存的使用），那么请在客户机上安装balloon驱动吧。 

安装该驱动需要前往 _Device Manager_ ，其位于 _System devices_ 内的 _PCI standard RAM Controller_ 中（未识别的PCI控制设备则在 _Other devices_ 中）。选择 _Update driver_ ，在打开的窗口中选择 _Browse my computer..._ ，然后选择CD-ROM（记得勾上 _Include subdirectories_ 选项），安装完成后重启，驱动就安装成功了。现在可以如气球打气一般调整内存限制（例如通过hmp命令`balloon _memory_size_`，该命令会使balloon从客户机中尽可能地夺取内存，将客户机的内存大小限制至 _memory_size_ ）。然而，现在依然无法追踪内存的状态，我们还需要正确地安装 _Balloon_ 服务才行。以管理员身份启动命令行，前往CD-ROM中的 _Balloon_ 目录，然后在目录下找到对应系统和架构的地方。当深入至 _amd64_ (_x86_) 目录时，运行`blnsrv.exe -i`进行安装，安装之后`virsh`命令`dommemstat`就会输出命令所支持的各种数据。 

###  FreeBSD客户机

如果你使用的是FreeBSD 8.3之后10.0-CURRENT之间的版本， 那么无论内核中是否包含了virtio-kmod， 都需要安装`emulators/virtio-kmod`端口。安装之后请在`/boot/loader.conf`添加如下内容： 
    
    virtio_load="YES"
    virtio_pci_load="YES"
    virtio_blk_load="YES"
    if_vtnet_load="YES"
    virtio_balloon_load="YES"

按照下面修改 `/etc/fstab`： 
    
    # sed -ibak "s/ada/vtbd/g" /etc/fstab
    
注意确认 `/etc/fstab` 内容与该命令的预期效果相同，如果出错了就通过 rescue CD 启动，然后将 `/etc/fstab.bak` 复制到 `/etc/fstab`。 

##  QEMU 监视器

QEMU运行时会提供一个监视器 console 界面以方便用户同虚拟机进行交互。QEMU 监视器提供了许多有趣的功能，例如获取当前虚拟机的信息，热插拔设备，创建快照等。在 QEMU 监视器 console 中运行 `help` 或 `?` 命令，或者阅读[官方 QEMU 文档](<https://www.qemu.org/docs/master/system/monitor.html>)获得完整的命令列表。 

###  访问 QEMU 监视器 Console

####  图形化界面

当使用默认的 `std` 图形选项时，可以通过按下 `Ctrl+Alt+2` 组合键或从QEMU窗口上的 _View > compatmonitor0_ 访问到 QEMU 监视器。若要返回到虚拟机的图形界面，那么按下 `Ctrl+Alt+1` 或者 _View > VGA_ 就行。 

然而，这种标准的访问方式不够方便，而且并不是在QEMU的所有图形化输出方式中都适用。 

#### Telnet

启动 QEMU 时带上 `-monitor telnet:127.0.0.1:_port_ ,server,nowait` 参数可以启用 [telnet](<../zh-cn/Telnet.html> "Telnet")。虚拟机启动后可以通过 telnet 访问到监视器： 
    
    $ telnet 127.0.0.1 _port_
    
**注意：** 如果指定 `127.0.0.1` 作为监听地址，那么只能在运行 QEMU 的宿主机上连接到该监视器。如果想要远程访问，QEMU需要在 `0.0.0.0` 上进行监听：`-monitor telnet:0.0.0.0:_port_ ,server,nowait`。还要记住的是，最好对[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")进行配置，该连接是完全不进行认证和加密的，因此需要通过防火墙确保本地网络环境是可信的。

####  UNIX 套接字

通过 `-monitor unix:_socketfile_ ,server,nowait` 参数运行QEMU，之后就可以通过 [socat](<https://archlinux.org/packages/?name=socat>)包、[nmap](<https://archlinux.org/packages/?name=nmap>)包 或 [openbsd-netcat](<https://archlinux.org/packages/?name=openbsd-netcat>)包 连接到监视器上。 

例如，如果QEMU是通过如下命令启动： 
    
    $ qemu-system-x86_64 -monitor unix:/tmp/monitor.sock,server,nowait _[...]_
    
就可以像这样连接到监视器上： 
    
    $ socat - UNIX-CONNECT:/tmp/monitor.sock
    
或者通过这种方式: 
    
    $ nc -U /tmp/monitor.sock
    
也可以使用 [nmap](<https://archlinux.org/packages/?name=nmap>)包： 
    
    $ ncat -U /tmp/monitor.sock
    
#### TCP

可以使用 `-monitor tcp:127.0.0.1:_port_ ,server,nowait` 参数将监视器暴露于TCP端口上，然后用 netcat（[openbsd-netcat](<https://archlinux.org/packages/?name=openbsd-netcat>)包 或 [gnu-netcat](<https://archlinux.org/packages/?name=gnu-netcat>)包 都可以）进行连接： 
    
    $ nc 127.0.0.1 _port_
    
**注意：** 为了能够从其它设备上通过 TCP 套接字访问到监视器，而不仅仅从运行QEMU的主机上连接，需要像前面Telnet中描述的那样，在`0.0.0.0`地址上进行监听。

####  标准 I/O

如果以 `-monitor stdio` 参数运行QEMU，那么其实是可以在运行 QEMU 的终端下访问到监视器的。 

###  在 Monitor conosle 下向虚拟机发送按键行为

由于在某些配置下，宿主机可能会拦截一些按键组合另作他用，这导致要在虚拟机中触发一些特定按键组合变得有些困难（一个显然的例子就是`Ctrl+Alt+F*`组合，该组合用于改变当前的tty）。我们采用在monitor console下发送按键组合的方式解决该问题。只需切换到monitor console下，然后使用`sendkey`命令，即可将按键转发至虚拟机中，例如： 
    
    (qemu) sendkey ctrl-alt-f2
    
###  通过 monitor console 创建快照和管理快照

**注意：** 该特性**只** 支持 _qcow2_ 格式的虚拟机磁盘镜像，对于 _raw_ 是无效的。

有时候我们很需要将虚拟机的当前状态进行保存，或是将虚拟机重置到之前的快照状态，而且最好是随时能进行这些操作。QEMU monitor console为用户提供了必要的功能，进行快照创建，快照管理，以及快照恢复。 

  * Use `savevm _name_` 用于创建一个名为 _name_ 的快照。
  * Use `loadvm _name_` 用于将虚拟机状态恢复至快照 _name_ 。
  * Use `delvm _name_` 用于删除快照 _name_ 。
  * Use `info snapshots` 用于查看保存的快照列表，这些快照由一个自增长的ID和标签名（用户创建快照时赋予）进行标识。

###  以冻结模式运行虚拟机

QEMU支持以冻结态运行虚拟机（需使用`-snapshot`参数），换句话说，虚拟机关闭时，对于虚拟机的一切修改都会丢弃。当用户对磁盘镜像写入时，这些变动最终写入的位置是`/tmp`目录下的一个临时文件，QEMU关机时将会把他们丢弃。 

不过，即使虚拟机运行于冻结状态下，依旧可以通过monitor console将这些变化写入磁盘镜像（如果你想的话）。使用下面的命令： 
    
    (qemu) commit all
    
另外如果在冻结状态下创建快照，这些快照在QEMU退出时都会被丢弃，除非你显式地commit了他们。 

###  monitor console 中的开机和暂停命令

在QEMU monitor console下也可以模拟对物理机的一些操作： 

  * `system_powerdown` 会向虚拟机发送ACPI关机信号，效果就类似物理机上按下电源按钮。
  * `system_reset` 会重置虚拟机，类似物理机上的重置按钮。该操作可能导致数据丢失或文件系统的损坏，这是因为虚拟机并不是"干净地"重启的。
  * `stop` 会暂停虚拟机。
  * `cont` 使暂停的虚拟机恢复运行。

###  虚拟机截屏

可以在monitor console下运行该命令，获取PPM格式的截屏图片： 
    
    (qemu) screendump _file.ppm_
    
##  QEMU 机器协议

QEMU机器协议（QMP）是一个基于JSON格式的协议，使得其他应用程序可以通过该协议控制QEMU实例。类似[#QEMU 监视器](<#QEMU_%E7%9B%91%E8%A7%86%E5%99%A8>)，其提供了与运行中的虚拟机进行交互的能力，且能够编程进行控制。关于QMP各命令的描述可以在这个[qmp-commands](<https://raw.githubusercontent.com/coreos/qemu/master/qmp-commands.hx>)链接中找到。 

###  启动 QMP

使用QMP协议来控制虚拟机的通常做法是在启动QEMU时使用`-qmp`打开一个 TCP 套接字。底下是一个使用 TCP 4444 端口的例子： 
    
    $ qemu-system-x86_64 _[...]_ -qmp tcp:localhost:4444,server,nowait
    
而与QMP代理进行通信的一个选择是使用 [netcat](</wzh/index.php?title=Netcat&action=edit&redlink=1> "Netcat（页面不存在）"): 
    
    nc localhost 4444
    
    {"QMP": {"version": {"qemu": {"micro": 0, "minor": 1, "major": 3}, "package": ""}, "capabilities": []} } 

在目前这个阶段，其能识别的命令仅有`qmp_capabilities`，QMP将进入了命令模式。敲下： 
    
    {"execute": "qmp_capabilities"}
    
现在，QMP可以接收命令了。要查看QMP接受的命令列表，使用： 
    
    {"execute": "query-commands"}
    
###  即时将子镜像合并至父镜像中

通过发起一个`block-commit`可以将一个正处于运行态的快照合并到其父结点上。下面的例子是其最简单的一种形式，将把子镜像提交至父镜像中： 
    
    {"execute": "block-commit", "arguments": {"device": "_devicename_ "}}
    
QMP收到该命令后，处理程序将会寻找基镜像，把该镜像由只读转为可读写模式，然后完成commit的任务。 

一旦 _block-commit_ 操作完成，将会触发一个`BLOCK_JOB_READY`事件，发出同步完成的信号。当然也可以用一种更优雅的方式完成该操作，改为使用`block-job-complete`： 
    
    {"execute": "block-job-complete", "arguments": {"device": "_devicename_ "}}
    
在发出该命令之前， _commit_ 操作将会保持活动状态。 任务完成后，基镜像将会保持在可读写模式，并变为active层。另一方面，子镜像将变得不可使用，用户有责任将其清除。 

**提示：** 执行`query-block`命令并对输出进行解析可以获取设备列表和其对应名字。设备名在 `device` 字段中，例如本例中磁盘设备名就是 `ide0-hd0`：
    
    {"execute": "query-block"}
    
    {"return": [{"io-status": "ok", "device": "**ide0-hd0** ", "locked": false, "removable": false, "inserted": {"iops_rd": 0, "detect_zeroes": "off", "image": {"backing-image": {"virtual-size": 27074281472, "filename": "parent.qcow2", ... } 

###  即时创建一个新的快照

为运行中的镜像创建一个快照： 
    
    {"execute": "blockdev-snapshot-sync", "arguments": {"device": "_devicename_ ","snapshot-file": "_new_snapshot_name_.qcow2"}}
    
该命令将会创建一个名为 `_new_snapshot_name_.qcow2` 的堆叠文件，该快照也将成为新的活动层。 

##  技巧

###  改善虚拟机的性能表现

底下是一些可以改善虚拟机性能表现的技术，例如： 

  * 启用[#启用 KVM](<#%E5%90%AF%E7%94%A8_KVM>)：QEMU的启动命令加上 `-enable-kvm` 选项。
  * 通过 `-cpu host` 选项让 QEMU 模拟宿主机上的特定 CPU，如果没有该选项 QEMU 尝试模拟的是一个更为通用的 CPU。
  * 特别的，如果客户机是 Windows，启用[Hyper-V enlightenments](<https://blog.wikichoon.com/2014/07/enabling-hyper-v-enlightenments-with-kvm.html>)可以改善性能：`-cpu host,hv_relaxed,hv_spinlocks=0x1fff,hv_vapic,hv_time`.有关更多信息和标志，请参阅 [QEMU 文档](<https://www.qemu.org/docs/master/system/i386/hyperv.html>)。
  * 可以使用 `-smp cores=x,threads=y,sockets=1,maxcpus=z` 选项为虚拟机分配多个核心。threads 参数用于分配 [SMT 核心](<https://www.tomshardware.com/reviews/simultaneous-multithreading-definition,5762.html>)。为 QEMU、管理程序和主机系统保留一个物理核心不受干扰是非常有益的。
  * 检查是否为虚拟机分配的足够的内存。默认情况下，QEMU仅仅为每台虚拟机分配 128MiB 的内存，可以使用 `-m` 选项分配更多的内存。例如，`-m 1024` 代表启动一台内存为 1024MiB 的虚拟机，`-m 4G`则为4GiB的内存。
  * 如果客户机操作系统支持相关的驱动，可以使用[virtio](<https://wiki.libvirt.org/page/Virtio>)创建网络设备或块设备，详情可参考 [#Installing virtio drivers](<#Installing_virtio_drivers>)。
  * 使用 TAP 设备代替 user-mode 网络，参阅[#Tap 网络](<#Tap_%E7%BD%91%E7%BB%9C>)。
  * 如果客户机需要进行大量的磁盘写工作，在宿主机文件系统上设置合适的挂载选项可以优化该工作。例如，可以用`barrier=0`选项挂载一个 [Ext4 文件系统](<../zh-cn/Ext4.html> "Ext4")。在使用这些性能强化选项之前最好阅读相关文档，因为性能上的提升通常伴随着数据完整性下降的代价。
  * 如果有一块原始磁盘或分区，你可能会想要禁用缓存：
        
        $ qemu-system-x86_64 -drive file=/dev/_disk_ ,if=virtio,**cache=none**

  * 使用原生的Linux AIO：
        
        $ qemu-system-x86_64 -drive file=_disk_image_ ,if=virtio**,aio=native,cache.direct=on**

  * 如果正同时运行多台虚拟机，而它们拥有同样的操作系统，可以通过启用[内核页归并](<https://en.wikipedia.org/wiki/Kernel_SamePage_Merging_\(KSM\)> "wikipedia:Kernel SamePage Merging \(KSM\)")节省内存。参阅[#开启 KSM](<#%E5%BC%80%E5%90%AF_KSM>)。
  * 在一些情况下，可以在运行时从安装了 balloon 驱动的客户机上回收内存，这需要 QEMU 启动该客户机时使用`-device virtio-balloon`选项。
  * 尽管不是很稳定，可以使用 ICH-9 AHCI 控制器的仿真层。AHCI 的仿真模拟支持 [NCQ](<https://en.wikipedia.org/wiki/Native_Command_Queuing> "wikipedia:Native Command Queuing")，因此可以同时处理多个读写请求：
        
        $ qemu-system-x86_64 -drive id=disk,file=_disk_image_ ,if=none -device ich9-ahci,id=ahci -device ide-drive,drive=disk,bus=ahci.0

参阅 <https://www.linux-kvm.org/page/Tuning_KVM> 获取更多信息。 

###  开机时启动QEMU虚拟机

####  通过 libvirt 实现

如果虚拟机是通过 [libvirt](<../zh-cn/Libvirt.html> "Libvirt") 设置的，可以用 `virsh autostart` 将其配置为开机自启，或者通过 _virt-manager_ GUI 中虚拟机的 Boot Options，选择 "Start virtual machine on host boot up" 实现开机自启。 

####  通过 systemd 服务实现

可以用如下的 systemd unit 和 config 配置开机时启动 QEMU VM。 
    
    /etc/systemd/system/qemu@.service
    
    [Unit]
    Description=QEMU virtual machine
    
    [Service]
    Environment="haltcmd=kill -INT $MAINPID"
    EnvironmentFile=/etc/conf.d/qemu.d/%i
    ExecStart=/usr/bin/qemu-system-x86_64 -name %i -enable-kvm -m 512 -nographic $args
    ExecStop=/usr/bin/bash -c ${haltcmd}
    ExecStop=/usr/bin/bash -c 'while nc localhost 7100; do sleep 1; done'
    
    [Install]
    WantedBy=multi-user.target

**注意：** 为了方便地结束任务，该 service 会等待至 console 端口被释放（这意味着 VM 已被关闭）。

接着按单个 VM 创建配置文件，命名为 `/etc/conf.d/qemu.d/_VM 名称_`，在其中设置好 `args` 和 `haltcmd` 变量，配置示例： 
    
    /etc/conf.d/qemu.d/one
    
    args="-hda /dev/vg0/vm1 -serial telnet:localhost:7000,server,nowait,nodelay \
     -monitor telnet:localhost:7100,server,nowait,nodelay -vnc :0"
    
    haltcmd="echo 'system_powerdown' | nc localhost 7100" # or netcat/ncat
    
    /etc/conf.d/qemu.d/two
    
    args="-hda /srv/kvm/vm2 -serial telnet:localhost:7001,server,nowait,nodelay -vnc :1"
    
    haltcmd="ssh powermanager@vm2 sudo poweroff"

对该变量的描述如下： 

  * `args` \- 使用的 QEMU 命令行参数。
  * `haltcmd` \- 安全关闭虚拟机的命令，在第一个例子中，QEMU monitor 是通过 `-monitor telnet:..` 选项暴露至 telnet，因而关闭虚拟机是通过 `nc` 命令在 monitor console 中发送 `system_powerdown`，完成 ACPI 关机的工作。在另一个例子里，使用的则是 SSH。

若要设置启动时运行哪个虚拟机，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `qemu@_vm_name_.service` 这个 systemd 单元。 

###  鼠标整合

添加 `-usb -device usb-tablet` 选项以避免点击客户机系统的窗口时鼠标被捕获。该选项代表 QEMU 能够在不捕获鼠标的情况下，向系统报告鼠标的位置，该选项启用时还会覆盖 PS/2 鼠标模拟功能。例如： 
    
    $ qemu-system-x86_64 -hda _disk_image_ -m 512 -usb -device usb-tablet
    
如果该命令不起作用，试试 `-vga qxl` 参数，并看看[#鼠标指针抖动或者不稳定](<#%E9%BC%A0%E6%A0%87%E6%8C%87%E9%92%88%E6%8A%96%E5%8A%A8%E6%88%96%E8%80%85%E4%B8%8D%E7%A8%B3%E5%AE%9A>)的操作指导。 

###  宿主机的USB设备传递至虚拟机

从客户机访问连接到宿主机USB口的设备是可能的，首先需要识别设备连接的位置，可以用`lsusb`命令找到设备连接位置，例如： 
    
    $ lsusb
    
    ...
    Bus **003** Device **007** : ID **0781** :**5406** SanDisk Corp. Cruzer Micro U3
    
上面以粗体显示的数字分别用于标识“ host_bus”和“ host_addr”或者“ vendor_id”和“ product_id”。 

基本的思想是在 QEMU 中 `-device usb-ehci,id=ehci` 或 `-device qemu-xhci,id=xhci` 分别对 EHCI (USB 2) 或 XHCI (USB 1.1，USB 2，USB 3) 控制器进行模拟，然后将物理设备通过 `-device usb-host,..` 选项进行添加。在本节中的剩余部分， _controller_id_ 要么是 `ehci`，要么是 `xhci`。 

接着，这里有两种方法通过qemu连接到宿主机的USB： 

  1. 识别出该设备，并将其连接至任一总线以及宿主机上的地址，通用的语法如下：
         
         -device usb-host,bus=_controller_id_.0,vendorid=0x _vendor_id_ ,productid=0x _product_id_

。Applied to the device used in the example above, it becomes:
         
         -device usb-ehci,id=ehci -device usb-host,bus=ehci.0,vendorid=0x**0781** ,productid=0x**5406**

；此外也可以在上面的选项中添加`...,port=_port_number_` 设置，用于指定设备添加至虚拟机控制器上的哪个物理端口。该设置在为 VM 添加多个设备时比很有用。另一个方案是使用 QEMU 5.1.0 之后出现的 `usb-host` 的 `hostdevice`属性，语法为：
         
         -device qemu-xhci,id=xhci -device usb-host,hostdevice=/dev/bus/usb/003/007

  2. 若要添加一个已连接至特定USB总线和地址的设备，语法为：
         
         -device usb-host,bus=_controller_id_.0,hostbus=_host_bus_ ,host_addr=_host_addr_

，将其中的参数修改至该总线和地址即可，拿上面的例子来说，需修改为：
         
         -device usb-ehci,id=ehci -device usb-host,bus=ehci.0,hostbus=**3** ,hostaddr=**7**

**注意：** 如果运行 QEMU 时遇到了权限方面的错误，可以阅读 [udev#About udev rules](<../zh-cn/Udev.html#About_udev_rules> "Udev") 获取更多信息，以了解如何为设备设定合适的权限。

###  使用 SPICE 进行 USB 重定向

使用[#SPICE](<#SPICE>)时可以将USB设备从客户端重定向至虚拟机中，无需使用QEMU命令。还支持为配置USB重定向插槽数（插槽数将决定可同时重定向的最大设备数）。相比于前面那种使用`-usbdevice`进行重定向的方法，SPICE方法的优势在于可以在虚拟机启动后USB设备热插拔，移除或添加USB设备时无需停机。这个方法还允许通过网络将客户端的USB设备重定向至服务端。总之，其是在QEMU虚拟机中使用USB设备最灵活的方法。 

我们需要为每个所需的USB重定向插槽添加一个EHCI/UHCI控制器，以及每个插槽添加一个SPICE重定向通道。例如，将下面的选项加入到所使用的QEMU命令中，以SPICE模式启动虚拟机时将会添加三个用于重定向的USB插槽： 
    
    -device ich9-usb-ehci1,id=usb \
    -device ich9-usb-uhci1,masterbus=usb.0,firstport=0,multifunction=on \
    -device ich9-usb-uhci2,masterbus=usb.0,firstport=2 \
    -device ich9-usb-uhci3,masterbus=usb.0,firstport=4 \
    -chardev spicevmc,name=usbredir,id=usbredirchardev1 -device usb-redir,chardev=usbredirchardev1,id=usbredirdev1 \
    -chardev spicevmc,name=usbredir,id=usbredirchardev2 -device usb-redir,chardev=usbredirchardev2,id=usbredirdev2 \
    -chardev spicevmc,name=usbredir,id=usbredirchardev3 -device usb-redir,chardev=usbredirchardev3,id=usbredirdev3

参阅 [SPICE/usbredir](<https://www.spice-space.org/usbredir.html>) 获取更多信息。 

[spice-gtk](<https://archlinux.org/packages/?name=spice-gtk>)包中的`spicy`(_Input > Select USB Devices for redirection_)和[virt-viewer](<https://archlinux.org/packages/?name=virt-viewer>)包中的`remote-viewer`(_File > USB device selection_)都支持该特性。请确保你已在客户机上安装必要的SPICE Guest Tools，以使得该功能正常运作（参见[#SPICE](<#SPICE>)节获得更多信息）。 

**警告：** 需要牢记一点，当将USB设备从客户端重定向至服务端时，在客户端所在的操作系统上都无法使用该USB了，除非停止重定向。尤其重要的是千万不要将输入设备重定向（即不要将鼠标和键盘重定向），这么做会使得你难以访问到SPICE客户端的菜单而无法撤销该操作，因为在输入设备被重定向至虚拟机后，客户端无法响应它们的操作。

####  使用 udev 进行自动 USB 转发

通常，转发的设备必须在虚拟机启动时可用才能被转发。如果该设备断开连接，它将不再被转发。 

您可以使用 [udev rule](</wzh/index.php?title=Udev_rule&action=edit&redlink=1> "Udev rule（页面不存在）") 在设备上线时自动附加设备。在磁盘上的某个位置创建一个 `hostdev` 条目，并将其所有权 [chown](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "Chown") 为 root ，以防止其他用户修改它。
    
    /usr/local/hostdev-mydevice.xml
    
    <hostdev mode='subsystem' type='usb'>
      
        <vendor id='0x03f0'/>
        <product id='0x4217'/>

</hostdev>

然后创建一个用于附加或脱离设备的 _udev_ 规则: 
    
    /usr/lib/udev/rules.d/90-libvirt-mydevice
    
    ACTION=="add", \
        SUBSYSTEM=="usb", \
        ENV{ID_VENDOR_ID}=="03f0", \
        ENV{ID_MODEL_ID}=="4217", \
        RUN+="/usr/bin/virsh attach-device GUESTNAME /usr/local/hostdev-mydevice.xml"
    ACTION=="remove", \
        SUBSYSTEM=="usb", \
        ENV{ID_VENDOR_ID}=="03f0", \
        ENV{ID_MODEL_ID}=="4217", \
        RUN+="/usr/bin/virsh detach-device GUESTNAME /usr/local/hostdev-mydevice.xml"

详阅[这篇博客](<https://rolandtapken.de/blog/2011-04/how-auto-hotplug-usb-devices-libvirt-vms-update-1>)。 

###  开启KSM

Kernel Samepage Merging (KSM) 是Linux内核的一个特性，允许应用程序向内核申请同其他申请页归并的进程进行页归并，KSM机制允许客户虚拟机之间进行页共享。当许多客户机运行相似的操作系统时，这个机制可以节省客观的内存。 

**注意：** 尽管KSM可能减小内存占用量，其增加了CPU负担。此外要注意的是使用该机制可能产生一些安全问题，参见[Wikipedia:Kernel same-page merging](<https://en.wikipedia.org/wiki/Kernel_same-page_merging> "wikipedia:Kernel same-page merging")。

启用KSM: 
    
    # echo 1 > /sys/kernel/mm/ksm/run
    
使之常驻，使用 [systemd 的临时文件](<../zh-cn/Systemd.html#systemd-tmpfiles_-_temporary_files> "Systemd")
    
    /etc/tmpfiles.d/ksm.conf
    
    w /sys/kernel/mm/ksm/run - - - - 1
    
当 KSM 启用，而正好有准备进行归并的页，（比如，至少有两个相似的 VM 正在运行），那么 `/sys/kernel/mm/ksm/pages_shared` 应会是非零的。参阅 <https://www.kernel.org/doc/html/latest/admin-guide/mm/ksm.html> 了解更多信息。 

**提示：** 查看KSM性能的一种简单方法是列出此目录下的所有文件内容： 
    
    $ grep -r . /sys/kernel/mm/ksm/
    
###  多屏支持

Linux的QXL驱动支持默认支持四头（虚拟屏幕），可以通过`qxl.heads=N`这一内核参数进行变更。 

QXL设备的默认VGA内存大小为16M（VRAM大小为64M），在想使用两块1920x1200显示器时（需要2 × 1920 × 4 (色深) × 1200 = 17.6 MiB VGA内存）是不够用的。用`-vga none -device qxl-vga,vgamem_mb=32`选项代替`-vga qxl`可以对该属性进行变更。如果你将vgamem_mb增大至64M以上，则还需要增大`vram_size_mb`选项的值。 

###  自定义显示器分辨率

可以使用 `-device VGA,edid=on,xres=1280,yres=720` 来设置自定义显示器分辨率 (参见 [EDID](<https://en.wikipedia.org/wiki/Extended_Display_Identification_Data> "wikipedia:Extended Display Identification Data") 和 [display resolution](<https://en.wikipedia.org/wiki/Display_resolution> "wikipedia:Display resolution")) 。 

###  复制和粘贴

在宿主机和客户机之间共享剪贴板的方法之一是使用SPICE远程桌面协议，通过SPICE客户端访问客户机，你需要遵照[#SPICE](<#SPICE>)节中描述的步骤，通过该方式运行的客户机将支持与宿主机进行复制粘贴的操作。 

#### SPICE

在主机和虚拟机之间共享剪贴板的一种方法是启用 SPICE 远程桌面协议，并使用 SPICE 客户端访问客户端。 

请按照 [#SPICE](<#SPICE>) 中描述的步骤进行。以这种方式运行的虚拟机将支持与主机的复制粘贴功能。 

#### qemu-vdagent

QEMU 提供了其自己的 spice vdagent 字符设备实现，称为 `qemu-vdagent`。它与 spice-vdagent 客户端服务接口，可以实现虚拟机和主机之间的剪贴板共享。 

要使用 QEMU 的 GTK 显示器访问此共享剪贴板，你需要[从源码编译 QEMU](<../zh-cn/Arch_Build_System.html> "Arch Build System") ，并使用 `--enable-gtk-clipboard` 配置参数。这需要替换已安装的 `qemu-ui-gtk` 包。 

**注意：**

  * 已提交功能请求 [FS#79716](<https://bugs.archlinux.org/task/79716>) 以在官方包中启用此功能。
  * 由于 [在某些情况下会导致虚拟机冻结](<https://gitlab.com/qemu-project/qemu/-/issues/1150>) ， qemu-ui-gtk 中的共享剪贴板功能已推回到实验阶段。上游已提出解决此问题的修复方案。

添加以下的 QEMU 命令行参数: 
    
    -device virtio-serial,packed=on,ioeventfd=on
    -device virtserialport,name=com.redhat.spice.0,chardev=vdagent0
    -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off
    
这些参数如果转换为 [libvirt 格式](<../zh-cn/Libvirt.html#QEMU_command_line_arguments> "Libvirt")也是有效的。 

**注意：** 虽然 spicevmc 字符设备会自动启动虚拟机的 spice-vdagent 服务，但 qemu-vdagent 字符设备可能不会。

在 Linux 虚拟机上，你可以手动[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `spice-vdagent.service` [用户单元](<../zh-cn/User_unit.html> "User unit")。在 Windows 虚拟机上，请将 spice-agent 的启动类型设置为自动。 

###  Windows专用说明

QEMU可以运行从 Windows 95 至 Windows 11 的任何版本 Windows。 

在QEMU中也可以运行 [Windows PE](<../zh-cn/Windows_PE.html> "Windows PE")。 

####  快速启动设置

**注意：** 改变电源设置需要一个 Administrtor 账户

根据此[论坛帖子](<https://www.tenforums.com/tutorials/4189-turn-off-fast-startup-windows-10-a.html>)所解释的那样，对于Windows8及之后的客户机最好在Control Panel的Power Options中禁用"Turn on fast startup (recommended)"，该设置导致客户机在每次启动时卡死。 

为了正确应用对 `-smp` 选项进行的更改，可能也需要禁用快速启动。 

####  远程桌面协议

如果你使用一个 MS Windows 客户机，可能会想使用 RDP 连接到客户机 VM。若你正使用 VLAN 或与客户机处于同一个网络中，先使用： 
    
    $ qemu-system-x86_64 -nographic -nic user,hostfwd=tcp::5555-:3389
    
接着通过 [rdesktop](<https://archlinux.org/packages/?name=rdesktop>)包 或 [freerdp](<https://archlinux.org/packages/?name=freerdp>)包 连接到客户机。例如： 
    
    $ xfreerdp -g 2048x1152 localhost:5555 -z -x lan
    
###  在物理设备上克隆一个已安装的Linux系统

安装在物理设备上的Linux系统可以克隆至QEMU VM中运行，参阅[Clone Linux system from hardware for QEMU virtual machine](<https://coffeebirthday.wordpress.com/2018/09/14/clone-linux-system-for-qemu-virtual-machine/>)

###  从 x86_64 环境中 Chroot 至 arm/arm64 环境

有时候相比于在基于ARM架构的设备上工作，在磁盘镜像上进行工作更容易。可以通过挂载一个 _root_ 分区的SD卡/存储设备，然后chroot到该设备实现该目的。 

另一个使用 ARM chroot 的场景是在 x86_64 机器上构建 ARM 包。这种情况下，可以使用来自 [Arch Linux ARM](<https://archlinuxarm.org>) 的镜像包来创建 chroot 环境 - 具体操作可查阅 [[2]](<https://nerdstuff.org/posts/2020/2020-003_simplest_way_to_create_an_arm_chroot/>)。 

无论哪种方式，都应该可以从chroot运行pacman并安装更多软件包，编译大型库等。由于可执行文件是针对ARM体系结构的，因此需要QEMU转换为x86。 

在 x86_64 宿主机上安装 [qemu-user-static](<https://archlinux.org/packages/?name=qemu-user-static>)包 和 [qemu-user-static-binfmt](<https://archlinux.org/packages/?name=qemu-user-static-binfmt>)包，后者会将 qemu 二进制文件注册至 binfmt 服务。 

需要使用 _qemu-user-static_ 执行其他架构上的程序，这个包与 [qemu-emulators-full](<https://archlinux.org/packages/?name=qemu-emulators-full>)包 提供的程序很相似，只是对于 chroot 来说必须使用 "static" 变种。比如： 
    
    qemu-arm-static path_to_sdcard/usr/bin/ls
    qemu-aarch64-static path_to_sdcard/usr/bin/ls
    
这两个命令分别用于执行 32 位 ARM 和 64ARM 的 {{ic|ls} }命令。注意如果没有 chroot，这些都不会生效，因为那样的话它们将会试图寻找不存在宿主机系统上的一些二进制文件。 

[qemu-user-static](<https://archlinux.org/packages/?name=qemu-user-static>)包 允许自动地用为 ARM 可执行文件添加 `qemu-arm-static` 或 `qemu-aarch64-static` 前缀。 

检查一下 ARM 可执行的支持是否被开启了： 
    
    $ ls /proc/sys/fs/binfmt_misc
    
    qemu-aarch64  qemu-arm	  qemu-cris  qemu-microblaze  qemu-mipsel  qemu-ppc64	    qemu-riscv64  qemu-sh4    qemu-sparc	qemu-sparc64  status
    qemu-alpha    qemu-armeb  qemu-m68k  qemu-mips	      qemu-ppc	   qemu-ppc64abi32  qemu-s390x	  qemu-sh4eb  qemu-sparc32plus	register
    
每种可执行的文件都须在此处列出。 

如果未开启，请[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `systemd-binfmt.service`。 

将SD卡挂载至 `/mnt/sdcard`（设备名可能不同）： 
    
    # mount --mkdir /dev/mmcblk0p2 /mnt/sdcard
    
如有需要，挂载启动分区（同样，使用合适的设备名）： 
    
    # mount /dev/mmcblk0p1 /mnt/sdcard/boot
    
最后如[Change root#Using chroot](<../zh-cn/Change_root.html#Using_chroot> "Change root")所描述的那样， _chroot_ 到 SD 卡的 root 中： 
    
    # chroot /mnt/sdcard /bin/bash
    
此外，可以使用 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 提供的 _arch-chroot_ 替代 chroot，可以方便地获取网络支持： 
    
    # arch-chroot /mnt/sdcard /bin/bash
    
还可以用 [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") chroot 到 ARM 环境中： 
    
    # systemd-nspawn -D /mnt/sdcard -M myARMMachine --bind-ro=/etc/resolv.conf
    
`--bind-ro=/etc/resolv.conf` 是可选的，其在 chroot 中提供了一个可用的网络 DNS。 

###  在 chroot 环境中使用 sudo

如果您在 chroot 环境中安装了 [sudo](<../zh-cn/Sudo.html> "Sudo")，并在尝试使用它时收到以下错误： 
    
    sudo: effective uid is not 0, is /usr/bin/sudo on a file system with the 'nosuid' option set or an NFS file system without root privileges?
    
那么您可能需要修改 binfmt 标志，例如对于 aarch64： 
    
    # cp /usr/lib/binfmt.d/qemu-aarch64-static.conf /etc/binfmt.d/
    # vi /etc/binfmt.d/qemu-aarch64-static.conf
    
并在该文件末尾添加一个 `C`： 
    
    :qemu-aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-aarch64-static:FPC
    
然后[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") systemd-binfmt.service 并检查更改是否生效（注意标志行上的 C）： 
    
    # cat /proc/sys/fs/binfmt_misc/qemu-aarch64
    
    enabled
    interpreter /usr/bin/qemu-aarch64-static
    flags: POCF
    offset 0
    magic 7f454c460201010000000000000000000200b700
    mask ffffffffffffff00fffffffffffffffffeffffff

有关更多信息，请参阅[内核 binfmt 文档](<https://docs.kernel.org/admin-guide/binfmt-misc.html>)的“flags”部分。 

##  处理常见问题

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[QEMU/Troubleshooting](</wzh/index.php?title=QEMU/Troubleshooting&action=edit&redlink=1> "QEMU/Troubleshooting（页面不存在）")。**

**附注：** This section is long enough to be split into a dedicated subpage.（在 [Talk:QEMU](<../zh-cn/Talk:QEMU.html>) 中讨论）

### Not grabbing mouse input

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** It is not explained what the option actually does. Is it causing or avoiding the side effect?（在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论）

Tablet mode has side effect of not grabbing mouse input in QEMU window: 
    
    -usb -device usb-tablet
    
It works with several `-vga` backends one of which is virtio. 

###  鼠标指针抖动或者不稳定

如果QEMU中鼠标指针不受控制地跳来跳去，那么启动QEMU之前在命令进行如下设置或许能解决该问题： 
    
    $ export SDL_VIDEO_X11_DGAMOUSE=0
    
如果成功了，可以把这条命令加入到你的 `~/.bashrc` 文件中 

###  看不见鼠标指针

使用`-show-cursor`选项启动QEMU以显示指针。 

如果这么做不起作用的话，请确保你的显示设备被正确设置了。例如： `-vga qxl`。 

还可尝试 [#鼠标整合](<#%E9%BC%A0%E6%A0%87%E6%95%B4%E5%90%88>)中提到的 `-usb -device usb-tablet`。该选项会覆盖默认采用的PS/2鼠标仿真，将鼠标作为外设在宿主机和客户机之间同步指针位置。 

###  有两个不同的鼠标指针

遵循 [#鼠标整合](<#%E9%BC%A0%E6%A0%87%E6%95%B4%E5%90%88>)提到的方法。 

###  使用 VNC 时键盘出现问题

使用 VNC 时，您可能会遇到[这里](<https://www.berrange.com/posts/2010/07/04/more-than-you-or-i-ever-wanted-to-know-about-virtual-keyboard-handling/>)所描述的键盘问题。 解决的方法是不使用 QEMU 的 `-k` 选项, 并使用 [gtk-vnc](<https://archlinux.org/packages/?name=gtk-vnc>)包 的 `gvncviewer` 。另请参见在libvirt邮件列表中发布的[消息](<https://www.mail-archive.com/libvir-list@redhat.com/msg13340.html>)。 

###  键盘像坏了一样或者方向键不起作用

如果发现某些键不起作用或按下一个按键，触发的却是其他按键，那么你可能需要指定键盘布局选项。在 `/usr/share/qemu/keymaps` 中可以找到键盘布局选项。 
    
    $ qemu-system-x86_64 -k _keymap_ _disk_image_
    
###  无法读取键盘映射文件
    
    qemu-system-x86_64: -display vnc=0.0.0.0:0: could not read keymap file: 'en'
    
这类问题产生的原因是将非法的键盘映射名作为`-k`的参数传递给qemu。例如，`en`是错误的键盘映射名称，`en-us`才是正确的。相关信息参见`/usr/share/qemu/keymaps`。 

###  客户机在调整窗口大小时一起被拉伸了

按下 `Ctrl+Alt+u` 可以恢复到原来的大小。 

###  ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy

如果在以 `-enable-kvm` 选项启动QEMU时显示了这样一条错误信息： 
    
    ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy
    failed to initialize KVM: Device or resource busy
    
这意味着还有另一个 [hypervisor](</wzh/index.php?title=Hypervisor&action=edit&redlink=1> "Hypervisor（页面不存在）") 处于运行状态， 不推荐同时运行多个hypervisor。 

###  libgfapi 的错误信息

启动时若显示如下错误信息: 
    
    Failed to open module: libgfapi.so.0: cannot open shared object file: No such file or directory
    
[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [glusterfs](<https://archlinux.org/packages/?name=glusterfs>)包 或者直接忽略这个错误信息，GlusterFS 只是一个可选的依赖。 

###  LIVE-environments 上发生内核错误

如果你启动一个 live-environment（或者启动一个系统），可能会遭遇如下错误： 
    
    [ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown block(0,0)
    
或者其他阻碍启动过程的东西（比如无法解包initramfs， 无法启动foo服务之类的），试试启动VM的时候用 `-m VALUE` 分配合适的 RAM 大小，如果内存太小是很有可能遭遇上述的问题的。 

###  Windows 7 客户机的音频质量差

为Windows7使用 `hda` 音频驱动可能造成音频质量降低， 通过QEMU的 `-soundhw ac97` 参数选择 `ac97` 作为音频驱动， 并从[Realtek AC'97 Audio Codecs](<https://www.realtek.com/en/component/zoo/category/pc-audio-codecs-ac-97-audio-codecs-software>)下载AC97驱动，然后在客户机中安装该驱动可能会解决这个问题。参见[Red Hat Bugzilla – Bug 1176761](<https://bugzilla.redhat.com/show_bug.cgi?id=1176761#c16>)以获取更多信息。 

### Could not access KVM kernel module: Permission denied

如果遇见了如下的错误信息: 
    
    libvirtError: internal error: process exited while connecting to monitor: Could not access KVM kernel module: Permission denied failed to initialize KVM: Permission denied
    
这是因为 Systemd 234 为 `kvm` 组注册了一个动态ID （参见[FS#54943](<https://bugs.archlinux.org/task/54943>)）。可以编辑 `/etc/libvirt/qemu.conf` 将 `group = "78"` 改为 `group = "kvm"` 避免产生这个错误。 

###  启动 Windows VM 时产生 "System Thread Exception Not Handled"

Windows 8或Windows 10 guest虚拟机在启动时可能会引发通用兼容性异常，即“System Thread Exception Not Handled”，这通常是由实体机上旧版驱动程序的异常行为引起的。在KVM机器上，通常可以通过将CPU模型设置为` core2duo`来解决此问题。 

###  某些 Windows 游戏/程序导致蓝屏出现

有时，一些能在物理机上正常运行的程序在虚拟机中会意外地崩溃。如果在以 root 运行 ` dmesg -wH` 时发现有 ` MSR` 相关的错误，则导致这些崩溃的原因是 KVM 注入了 GPF（[General protection fault](<https://en.wikipedia.org/wiki/General_protection_fault> "wikipedia:General protection fault")），当客户机尝试访问不受支持的寄存器（MSR， [Model-specific registers](<https://en.wikipedia.org/wiki/Model-specific_register> "wikipedia:Model-specific register")）时会导致客户机上的应用程序崩溃。将 `ignore_msrs=1` 传给 KVM 模块可以使其忽略不支持的 MSR， 从而解决大部分的同类问题。 
    
    /etc/modprobe.d/kvm.conf
    
    ...
    options kvm ignore_msrs=1
    ...

一些添加该选项可能会起作用的场景： 

  * GeForce Experience 反映没有可支持的CPU。
  * 星际争霸2和黑色洛城使用 `KMODE_EXCEPTION_NOT_HANDLED` 对 Windows 10 的蓝屏做了一些处理，蓝屏信息中将无法识别驱动。

**警告：** 虽然通常这么做是安全的，对于某些应用程序也可能不起作用，但默默忽略未知的 MSR 仍可能破坏 VM 或其他 VM 中的其他软件。

###  VM 中的应用程序有很高的延迟，或是需要等待很长的时间才会启动

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** No longer true since kernel 5.6 (在[Talk:QEMU](<../zh-cn/Talk:QEMU.html>)讨论)

这可能是由于VM中的可用熵不足所致。考虑通过将 [VirtIO RNG 设备](<https://wiki.qemu.org/Features/VirtIORNG>)添加到 VM，或安装诸如 [Haveged](<../zh-cn/Haveged.html> "Haveged") 之类的熵生成守护程序。 

有趣的是，OpenSSH 需要一段时间才能在熵不足的情况下开始接受连接，而其日志却不会显示原因。 

###  中断时间过长以及运行不流畅

此问题表现为小停顿（断断续续），在图形密集型应用程序（例如游戏）中尤其明显。 

  * 原因之一是CPU的节能功能，该功能由[CPU frequency scaling](<../zh-cn/CPU_frequency_scaling.html> "CPU frequency scaling")控制。请对所有处理器核心进行修改，将其更改为`performance`。
  * 另一个可能的原因是PS/2输入。从PS/2切换到Virtio输入，请参阅[PCI passthrough via OVMF#Passing keyboard/mouse via Evdev](<../zh-cn/PCI_passthrough_via_OVMF.html#Passing_keyboard/mouse_via_Evdev> "PCI passthrough via OVMF")。

###  QXL 导致视频分辨率降低

QEMU 4.1.0版本带来了一个回退问题，当使用SPICE时，会将QXL视频降到低分辨率。 [[3]](<https://bugs.launchpad.net/qemu/+bug/1843151>)例如，当KMS启动时，文本分辨率可能会低至4x10个字符。尝试提高GUI分辨率时，它可能会达到最低的支持分辨率。 

解决方法是，以这种形式创建设备： 
    
    -device qxl-vga,max_outputs=1...
    
###  使用启用了安全启动的OVMF时，VM无法启动

[edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包 中的 `OVMF_CODE.secboot.4m.fd` 以及 `OVMF_CODE.secboot.fd` 文件是在 [SMM](<https://en.wikipedia.org/wiki/System_Management_Mode> "w:System Management Mode") 的支持下完成构建的，如果未在 VM 中禁用 S3 支持，则 VM 可能根本无法启动。 

在QEMU命令中添加 `-global ICH9-LPC.disable_s3=1` 以解决该问题。 

参见 [FS#59465](<https://bugs.archlinux.org/task/59465>) 以及 <https://github.com/tianocore/edk2/blob/master/OvmfPkg/README> 获取 QEMU 使用 Secure Boot 所需要的更多选项。 

### Virtual machine not booting into Arch ISO

When trying to boot the virtual machine for the first time from an Arch ISO image, the boot process hangs. Adding `console=ttyS0` to kernel boot options by pressing `e` in the boot menu you will get more boot messages and the following error: 
    
    :: Mounting '/dev/disk/by-label/ARCH_202204' to '/run/archiso/bootmnt'
    Waiting 30 seconds for device /dev/disk/by-label/ARCH_202204 ...
    ERROR: '/dev/disk/by-label/ARCH_202204' device did not show up after 30 seconds...
       Falling back to interactive prompt
       You can try to fix the problem manually, log out when you are finished
    sh: can't access tty; job control turned off
    
The error message does not give a good clue as to what the real issue is. The problem is with the default 128MB of RAM that QEMU allocates to the virtual machine. Increasing the limit to 1024MB with `-m 1024` solves the issue and lets the system boot. You can continue installing Arch Linux as usual after that. Once the installation is complete, the memory allocation for the virtual machine can be decreased. The need for 1024MB is due to RAM disk requirements and size of the installation media. See [this message on the arch-releng mailing list](<https://lists.archlinux.org/archives/list/arch-releng@lists.archlinux.org/message/D5HSGOFTPGYI6IZUEB3ZNAX4D3F3ID37/>) and [this forum thread](<https://bbs.archlinux.org/viewtopic.php?id=204023>). 

###  客户机上的CPU中断没有被触发

如果你是按照 [OSDev Wiki](<https://wiki.osdev.org/>) 来编写自己的操作系统，或者只是使用 QEMU 的 `gdb` 接口和 `-s` 标志，您需要知道的是，很多仿真器（包括QEMU）通常会实现一些CPU中断，同时还有许多硬件中断没有被实现。了解代码是否触发中断的一种方法是使用： 
    
    -d int
    
可以在输出中查看 interrupts/exceptions。 

如要查看QEMU还提供了什么客户机调试功能，使用如下命令： 
    
    qemu-system-x86_64 -d help
    
或者将 `x86_64` 替换为你选择的其他架构 

### KDE with sddm does not start spice-vdagent at login automatically

Remove or comment out `X-GNOME-Autostart-Phase=WindowManager` from `/etc/xdg/autostart/spice-vdagent.desktop`. [[4]](<https://github.com/systemd/systemd/issues/18791>)

###  Error starting domain: Requested operation is not valid: network 'default' is not active

If for any reason the default network is deactivated, you will not be able to start any guest virtual machines which are configured to use the network. Your first attempt can be simply trying to start the network with virsh. 
    
    # virsh net-start default
    
For additional troubleshooting steps, see [[5]](<https://www.xmodulo.com/network-default-is-not-active.html>). 

##  参阅

  * [Official QEMU website](<https://qemu.org>)
  * [Official KVM website](<https://www.linux-kvm.org>)
  * [QEMU Emulator User Documentation](<https://qemu.weilnetz.de/doc/6.0/>)
  * [QEMU Wikibook](<https://en.wikibooks.org/wiki/QEMU> "wikibooks:QEMU")
  * [Hardware virtualization with QEMU](<http://alien.slackbook.org/dokuwiki/doku.php?id=slackware:qemu>) by AlienBOB (last updated in 2008)
  * [Building a Virtual Army](<http://blog.falconindy.com/articles/build-a-virtual-army.html>) by Falconindy
  * [QEMU documentation](<https://www.qemu.org/documentation/>)
  * [QEMU on Windows](<https://qemu.weilnetz.de/>)
  * [Wikipedia](<https://en.wikipedia.org/wiki/Qemu> "wikipedia:Qemu")
  * [Debian Wiki - QEMU](<https://wiki.debian.org/QEMU> "debian:QEMU")
  * [QEMU Networking on gnome.org](<https://people.gnome.org/~markmc/qemu-networking.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-22 ⓘ]
  * [Networking QEMU Virtual BSD Systems](<http://bsdwiki.reedmedia.net/wiki/networking_qemu_virtual_bsd_systems.html>)
  * [QEMU on gnu.org](<https://www.gnu.org/software/hurd/hurd/running/qemu.html>)
  * [QEMU on FreeBSD as host](<https://wiki.freebsd.org/qemu>)
  * [Managing Virtual Machines with QEMU - openSUSE documentation](<https://wiki.mikejung.biz/KVM_/_Xen>)
  * [Managing Virtual Machines with QEMU - openSUSE documentation](<https://doc.opensuse.org/documentation/leap/virtualization/html/book-virt/part-virt-qemu.html>)
  * [KVM on IBM Knowledge Center](<https://www.ibm.com/support/knowledgecenter/en/linuxonibm/liaat/liaatkvm.htm>)
