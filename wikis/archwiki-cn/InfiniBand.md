**翻译状态：**

  * 本文（或部分内容）译自 [InfiniBand](<https://wiki.archlinux.org/title/InfiniBand> "arch:InfiniBand")，最近一次同步于 2025-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/InfiniBand?diff=0&oldid=833274>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/InfiniBand_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本页介绍了如何设置、诊断和测试 [InfiniBand](<https://en.wikipedia.org/wiki/InfiniBand> "wikipedia:InfiniBand") 网络。 

##  简介

###  概述

InfiniBand（简称 IB）是以太网和光纤通道的替代方案。IB 提供高带宽和低延迟。IB 可以将数据直接从一台机器上的存储设备传输到另一台机器的用户空间，从而绕过并避免系统调用的开销。IB 适配器可以处理的网络协议与在 CPU 上运行的以太网协议不同，它允许操作系统和 CPU 在进行高带宽传输时保持低占用。这在10Gb+以太网中是个重要问题。 

IB 硬件由迈络思（Mellanox，与 Voltaire 合并，并得到 Oracle 的大力支持）和英特尔（2012 年收购了 QLogic 的 IB 部门）制造。迈络思于 2019 年被英伟达收购。IB 最常用于超算、集群和数据中心。IBM、惠普和 Cray 也是 InfiniBand 委员会的成员。Facebook、Twitter、eBay、YouTube 和 PayPal 都是 IB 用户。 

IB 软件的开发基于 [OpenFabrics Open Source Alliance](<https://www.openfabrics.org/>)。 

###  实惠的二手设备

由于大型企业从使用更新的设备中获益，无源 IB 线缆的最大长度限制，有源 IB 线缆的高成本，以及比以太网更复杂的技术设置，二手 IB 市场已经严重供大于求。因此，在家庭或小型企业的内部网络中使用二手 IB 设备性价比很高。 

###  带宽

####  信号传输速率

IB 传输速率一开始与 PCI Express（简称 PCIe）支持的最大速率一致。后来随着 PCIe 的发展，传输速率与其他 I/O 技术一样，每个端口的 PCIe 通道数也随之增加。IB 推出的 SDR（单数据速率）每通道信号传输速率为 2.5Gb/s（与 PCIe v1.0 相对应），后来又增加了：5Gb/s 的 DDR（双数据速率，PCIe 2.0）；10Gb/s 的 QDR（四数据速率，与 PCIe 3.0 的吞吐量相匹配，改进了 PCIe 3.0 的编码而非信号传输速率）；以及 14.0625 Gbps 的 FDR（十四数据速率，与 16G FC 光纤通道相匹配）。IB 目前正在提供 25Gb/s 的 EDR（增强数据速率，与 25Gb 以太网相匹配）。计划在 2017 年左右推出 50Gb/s 的 HDR（高数据速率）。 

####  有效吞吐量

由于 SDR、DDR 和 QDR 版本使用 8/10 编码（8 位数据需要 10 位信令），这些版本的有效吞吐量降低到 80% 。 SDR 为 2Gb/s/link；DDR 为 4Gb/s/link；QDR 为 8Gb/s/link。从 FDR 开始，IB 使用 64/66 编码，使有效吞吐量与信令速率的比率提高到 96.97% 。 FDR 为 13.64Gb/s/link；EDR 为 24.24Gb/s/lane；HDR 为 48.48Gb/s/link。 

IB 设备能够通过多个链路发送数据，不过商用标准是每条线缆大约 4 个链路。 

使用普通 4X 链路设备时，总有效吞吐量可达 SDR 为 8Gb/s；DDR 为 16Gb/s；QDR 为 32Gb/s；FDR 为 54.54Gb/s；EDR 为 96.97Gb/s；HDR 为 193.94Gb/s。 

###  延迟

IB 的延迟小得令人难以置信：SDR（5us）；DDR（2.5us）；QDR（1.3us）；FDR（0.7us）；EDR（0.5us）；HDR（< 0.5us）。相比之下，10Gb 以太网的延迟为 7.22us，是 FDR 延迟的 10 倍。 

###  向后兼容性

IB 设备几乎总是向后兼容的。连接应建立在最小带宽上。用于 PCIe 8x 插槽的 DDR 适配器应能在 PCIe 4x 插槽中使用（带宽减半）。 

###  线缆

IB 无源铜缆使用 QDR 时最长可达 7 米，使用 FDR 时最长可达 3 米。 

IB 有源光纤（光）电缆使用 FDR 时最长可达 300 米（FDR10 仅为 100 米）。 

Mellanox MetroX 设备可提供长达 80 公里的连接。延迟每公里增加约 5us。 

IB 线缆可用于直接连接两台计算机，无需交换机；不存在 IB 交叉线缆。 

##  术语解释

###  硬件

适配器、交换机、路由器和网桥/网关必须专为 IB 而设计。 

HCA (主机通道适配器)
    类似以太网 NIC（网络接口卡）。它将 IB 电缆连接到 PCIe 总线上，如果使用的是适当型号的 HCA，则可达到总线的全速。IB 网络的终端节点，执行传输级功能，并支持 IB verbs接口。
交换机
    与以太网网卡类似。在同一 IB 子网中将数据包从一个链路传送到另一个链路。
路由器
    类似以太网路由器。在不同 IB 子网之间传输数据包。
网桥/网关
    一个独立的硬件或执行此功能的计算机。桥接 IB 和以太网网络。

### GUID

与以太网 MAC 地址类似，但一个设备有多个 GUID。由硬件制造商分配，重启后保持不变。64 位地址（24 位制造商前缀和 40 位设备标识符）。分配给适配器、交换机、路由器和网桥/网关。 

Node GUID
    标识 HCA、交换机或路由器
Port GUID
    标识 HCA、交换机或路由器上的端口（即使一个 HCA 通常也有多个端口）
System GUID
    允许将多个 GUID 视为一个实体
LID（本地标识符）
    子网管理器接收时分配的 16 位地址。用于路由数据包。重启后不能持久使用。

###  网络管理

SM（子网管理器）
    主动管理 IB 子网。可以作为连接到 IB 网络的计算机上的一个软件程序、内置到 IB 交换机中或作为专门的 IB 设备来实现。初始化和配置子网中的其他一切，包括分配 LID（本地标识符）。建立通过子网的流量路径。隔离故障。防止其他未经授权的子网管理器。一个子网管理器下可以有多个交换机。一个子网中可以有多个子网管理器，但同时只能有一个处于活动状态。
MAD（管理数据报）
    子网管理器与 IB 设备之间通信的标准信息格式，由 UD（不可靠数据报）承载。
UD（不可靠数据报）
    
##  安装

首先安装 [rdma-core](<https://archlinux.org/packages/?name=rdma-core>)包 其中包含所有核心库和守护进程。 

###  更新固件

使用最新固件可显著提高性能，并修复连接问题。 

**警告：** 请小心操作，设备可能会损坏！

####  适用于 Mellanox

  * 安装 [mstflint](<https://aur.archlinux.org/packages/mstflint/>)AUR
  * 确定适配器的 PCI device ID (在这个例子中, "05:00.0" 就是适配器的 PCI device ID)

    $ lspci | grep Mellanox
    
    **05:00.0** InfiniBand: Mellanox Technologies MT25418 [ConnectX VPI PCIe 2.0 2.5GT/s - IB DDR / 10GigE] (rev a0)

  * 确定适配器的固件版本，以及适配器的 PSID（比型号更加具体 - 用于区分不同修订版本的兼容性设置）

    # mstflint -d <adapter PCI device ID> query
    
    ...
    FW Version:      **2.7.1000**
    ...
    PSID:            **MT_04A0110002**

  * 检查最新固件版本 
    * 访问 [Mellanox's firmware download page](<https://www.mellanox.com/page/firmware_download>)（本指南采用了该链接的 "固件刻录说明" ，使用的是 mstflint 选项）
    * 选择您的设备类别
    * 在 mstflint 给您的列表中找到设备的 PSID
    * 检查固件映像文件名是否比适配器的 FW 版本更新，比如 `fw-25408-2_9_1000-MHGH28-XTC_A1.bin.zip` 的版本就是 `2.9.1000`
  * 如果有最新版本，请下载新固件并将其刻录到适配器中。

    $ unzip <_firmware .bin.zip file name_ >
    # mstflint -d <_adapter PCI device ID_ > -i <_firmware .bin file name_ > burn
    
####  适用于 Intel/QLogic

在 [Intel Download Center](<https://downloadcenter.intel.com/>) 上搜索型号（或子串），然后按说明操作。下载的软件可能需要在 RHEL/CentOS 或 SUSE/OpenSUSE 中运行。 

###  内核模块

按照自己的喜好编辑 `/etc/rdma/modules/rdma.conf` 和 `/etc/rdma/modules/infiniband.conf` 。 然后加载这些文件中记录的内核模块，如 `ib_ipoib`, 或直接重启系统。 

**提示：** 尽管通常不需要这样操作，但如果内核模块未正确加载，请[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `rdma-load-modules@rdma.service` 和 `rdma-load-modules@infiniband.service`，然后重启系统。

**注意：**[由于内核堆栈的处理方式](<https://bugzilla.redhat.com/show_bug.cgi?id=965829>)，对 `/etc/rdma/modules/rdma.conf` 的修改只能在每次启动时生效一次， 即首次启动 `rdma-load-modules@*.service` 时， 重启 `rdma-load-modules@*.service` 没有任何作用。

###  子网管理器

每个 IB 网络至少需要一个子网管理器。如果没有子网管理器，设备可能会显示有链接，但状态永远不会从 `Initializing` 变为 `Active`。子网管理器会经常（通常为每 5 或 30 秒）检查网络中是否有新适配器，并将其添加到路由表中。如果 IB 交换机内嵌子网管理器，则可以使用该管理器，或者将其禁用，改用软件子网管理器。也有专用的 IB 子网管理器设备。 

###  启用端口

如果端口处于物理状态 `Sleep`（可通过 `ibstat` 验证）则首先需要运行 `ibportstate --Direct 0 1 enable` 来启用端口。如果链路两端的端口都处于睡眠状态，可能需要在启动时自动执行此操作。 

####  软件子网管理器

在一个系统上: 

  * 安装 [opensm](<https://aur.archlinux.org/packages/opensm/>)AUR
  * 修改 systemd 文件 `/usr/lib/systemd/system/opensm.service` 为如下所示。
  * [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `opensm.service`

当前的 opensm 配置与 RDMA 的 systemd 配置不兼容。即编辑 `/usr/lib/systemd/system/opensm.service` 中的两行（注释为原始内容）。 
    
    # /usr/lib/systemd/system/opensm.service
    
    Requires=rdma-load-modules@rdma.service # Requires=rdma.service
    After=rdma-load-modules@rdma.service # After=rdma.service

现在，所有连接的 IB 端口都应处于 `Active` 状态，物理状态应为 `LinkUp`。您可以通过运行 [ibstat](<#ibstat_-_%E6%9F%A5%E7%9C%8B%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%9A%84_IB_GUID>) 来检查。 
    
    $ ibstat
    
    ... (look at the ports shown you expect to be connected)
    State: Active
    Physical state: LinkUp
    ...

或通过检查 `/sys` 文件系统: 
    
    $ cat /sys/class/infiniband/_kernel_module_ /ports/_port_number_ /phys_state
    
    5: LinkUp
    
    $ cat /sys/class/infiniband/_kernel_module_ /ports/_port_number_ /state
    
    4: ACTIVE

##  TCP/IP (IPoIB)

您可以创建一个在 HCA 上运行的虚拟以太网适配器。这样，设计用于 TCP/IP 但不用于 IB 的程序就可以（间接）使用 IB 网络。由于通过正常的 TCP 协议栈发送所有流量，需要在 CPU 而不是 HCA 上运行系统调用、内存拷贝和网络协议，因此性能会受到负面影响。 

IB 接口将在加载模块 `ib_ipoib` 时出现。 使其出现的简单配置是在 `/etc/rdma/modules/infiniband.conf` 添加 `ib_ipoib` 行，然后重启系统。模块 `ib_ipoib` 随系统启动后，应使用命令 `ip link` 确认名称为 `ibp16s0` 的链接。 

还可对 IB 接口进行详细配置 (例如，将其重命名为 `ib0` 并分配 IP 地址[就像传统的以太网适配器一样](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")). 

###  连接模式

IPoIB 可在 datagram（默认）或 connected 模式下运行。Connected 模式[允许您设置更高的 MTU](<#%E8%B0%83%E4%BC%98_connection_%E6%A8%A1%E5%BC%8F_%E5%92%8C_MTU>)，但短报文的 TCP 延迟会比 datagram 模式增加5%. 

查看当前使用的模式： 
    
    $ cat /sys/class/net/_interface_ /mode
    
**注意：** ConnectX-6（或更新版本）的 Mellanox 卡不再支持 Connected 模式。

### MTU

在 datagram 模式下，使用 UD（不可靠数据报）传输，这通常会强制 MTU 为 2044 字节。从技术上讲，IB L2 MTU 将 4 字节用于 IPoIB 封装头，2044 字节传输数据。 

在 connected 模式下，使用 RC（可靠连接）传输，允许 MTU 达到最大 IP 数据包大小（65520 字节）。 

查看您的 MTU： 
    
    $ ip link show _interface_
    
###  调优 connection 模式和 MTU

只有更改默认 connection 模式 和/或 MTU 时，才需要 `ipoibmodemtu`。 

  * [安装并设置 TCP/IP over IB (IPoIB)](<#TCP/IP_\(IPoIB\)>)
  * 安装 [ipoibmodemtu](<https://aur.archlinux.org/packages/ipoibmodemtu/>)AUR
  * 通过 `/etc/ipoibmodemtu.conf` 配置 `ipoibmodemtu`，其中包含相关说明。 
    * 默认情况下，它将单个 IB 端口 `ib0` 设置为 `connected` 模式和 MTU `65520` 。
  * [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `ipoibmodemtu.service`

不同的设置会产生不同的结果。有些人通过使用 `connected` 模式和 MTU `65520` 看到了速度的大幅提升（双倍以上），而有些人看到的速度则与之差不多，甚至更差。请使用 [qperf](<#qperf_-_%E9%80%9A%E8%BF%87_RDMA_%E6%88%96_TCP/IP_%E6%B5%8B%E8%AF%95%E6%80%A7%E8%83%BD>) 和 [iperf](<#iperf_-_%E9%80%9A%E8%BF%87_TCP/IP_%E6%B5%8B%E8%AF%95%E6%80%A7%E8%83%BD>) 对系统进行微调。 

使用本文给出的 [qperf](<#qperf_-_%E9%80%9A%E8%BF%87_RDMA_%E6%88%96_TCP/IP_%E6%B5%8B%E8%AF%95%E6%80%A7%E8%83%BD>) 示例，下面是一个 SDR 网络（理论速度为 8 Gb/s）的示例结果，其中包含各种微调: 

Mode | MTU | MB/s | us latency   
---|---|---|---  
datagram | 2044 | 707 | 19.4   
connected | 2044 | 353 | 18.9   
connected | 65520 | 726 | 19.6   
  
**提示：** 整个子网使用相同的 connection 模式和 MTU 设置。混用和匹配无法达到最佳效果。

##  Soft RoCE (RXE)

Soft ROCE 是 RoCE 的软件实现，可通过任何以太网适配器使用 Infiniband。 

  * 安装 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包
  * 运行 `rdma link add rxe_eth0 type rxe netdev ethN` 以在以太网设备 ethN 上配置 RXE 实例。

现在应该有一个 rxe0 设备了: 
    
    # rdma link
    
    link rxe_eth0/1 state ACTIVE physical_state LINK_UP netdev enp1s0

##  远程数据存储

您可以使用 iSCSI、带有 iSER 的 iSCSI 或 SRP，通过 IB 网络将物理或虚拟设备从target（主机/服务器）共享到initiator（访客/客户端）系统。 这些方法与传统的文件共享（[Samba](<../zh-cn/Samba.html> "Samba") 或 [NFS](<../zh-cn/NFS.html> "NFS")）不同，因为启动程序系统会将共享设备视为自己的块级设备，而不是传统的挂载网络共享文件夹。 例如 `fdisk /dev/_block_device_id_`, `mkfs.btrfs /dev/_block_device_id_with_partition_number_`

缺点是每个共享设备一次只能有一个系统使用；试图在目标系统（target system）或其他发起系统（initiator system）上挂载共享设备会失败（最初的发起系统当然可以在上面运行传统的文件共享）。 

这样做的好处是带宽更快、控制能力更强，甚至可以远程物理定位发起系统的根文件系统（远程启动）。 

### targetcli

`targetcli`是一个命令，将其复杂的（不值得手动创建的）`/etc/target/saveconfig.json` 作为虚拟文件系统的配置文件。 

####  安装和使用

在目标系统上: 

  * 安装 [targetcli-fb](<https://aur.archlinux.org/packages/targetcli-fb/>)AUR
  * [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `target.service`

在 `targetcli` 中： 

  * 在任意虚拟目录中，运行 `help` 可查看“‘’该伪目录中可用的命令‘’”或 `help _command_`（如 `help create`）以获得更详细的帮助。
  * 许多命令还提供Tab补全
  * 运行 `ls` 查看当前虚拟目录及其下的整个虚拟文件系统

####  创建后端存储

输入配置命令: 
    
    # targetcli
    
在 `targetcli` 中，为每个要共享的设备或虚拟设备设置一个后端存储: 

  * 要共享真实的块设备，请运行 `cd /backstores/block` 和 `create _name_ _dev_`
  * 要将文件作为虚拟块设备共享，请运行 `cd /backstores/fileio` 和 `create _name_ _file_`
  * 要以直通方式共享物理 SCSI 设备，请运行 `cd /backstores/pscsi` 和 `create _name_ _dev_`
  * 要共享内存盘，请运行 `cd /backstores/ramdisk` 和 `create _name_ _size_`
  * 其中 _name_ 表示后端存储的名称
  * 其中 _dev_ 是要共享的块设备（如 `/dev/sda`、`/dev/sda4`、`/dev/disk/by-id/_XXX_` 或一个 LVM 逻辑卷 `/dev/vg0/lv1`）
  * 其中 _file_ 是要共享的文件（如 `/path/to/file`）
  * 其中 _size_ 是要创建的内存盘的大小（如 512MB 或 20GB）

### iSCSI

iSCSI 允许通过网络使用存储设备和虚拟存储设备。对于 IB 网络，存储设备可以通过 IPoIB 或 iSER 运行。 

与 [iSCSI Target](<../zh-cn/ISCSI_Target.html> "ISCSI Target")、[iSCSI Initiator](<../zh-cn/Open-iSCSI.html> "Open-iSCSI") 和 [iSCSI Boot](</wzh/index.php?title=ISCSI_Boot&action=edit&redlink=1> "ISCSI Boot（页面不存在）") 文章有很多重叠之处，但由于很多内容需要根据 IB 的使用情况进行定制，因此将讨论必要的内容。 

#### Over IPoIB

首先执行模板系统指令，这将指导您何时临时切换到发起系统指令。 

  * 在目标系统和发起系统上，[安装 TCP/IP over IB](<#TCP/IP_\(IPoIB\)>)

  * 在目标系统上，对于要共享的每个设备或虚拟设备，使用 `targetcli`： 
    * [创建后端存储](<#%E5%88%9B%E5%BB%BA%E5%90%8E%E7%AB%AF%E5%AD%98%E5%82%A8>)
    * 为每个后备存储创建一个 IQN（iSCSI 限定名称）（其他系统配置将看到的存储名称） 
      * 运行 `cd /iscsi` 和 `create`. 它将为您提供一个 _randomly_generated_target_name_ , 例如 `iqn.2003-01.org.linux-iscsi.hostname.x8664:sn.3d74b8d4020a`
      * 设置 TPG（目标门户组），在上一步中自动创建为 tpg1 
        * 创建 lun（逻辑单元编号） 
          * 运行 `cd _randomly_generated_target_name_ /tpg1/luns` 和 `create _storage_object_`。其中 `_storage_object_` 是指向现有存储对象的完整路径，例如 `/backstores/block/_name_`
        * 创建 acl （访问控制列表） 
          * 运行: `cd ../acls`; 和 `create _wwn_`, 此处 `_wwn_` 是initiator系统的 IQN（iSCSI 合格名称），又称其（全局名称）。 
            * 在发起系统（'**不是** 目标系统）上运行 `_wwn_` 获取（在其上安装 [open-iscsi](<https://archlinux.org/packages/?name=open-iscsi>)包 之后）`cat /etc/iscsi/initiatorname.iscsi`
    * 通过运行 `cd /`；`saveconfig`；`exit` 来保存并退出。

  * 在发起系统上： 
    * 安装 [open-iscsi](<https://archlinux.org/packages/?name=open-iscsi>)包
    * 此时，您可以获取发起系统的 IQN（iSCSI 合格名称），又称 wwn（全局名称），用于设置目标系统的 `lun`： 
      * `pacman` 应显示 `>>> Setting Initiatorname _wwn_`
      * 否则，请运行 `cat /etc/iscsi/initiatorname.iscsi` 查看 `InitiatorName=_wwn_`
    * [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `iscsid.service`
    * 要在启动时自动登录已发现的目标系统 ，请在发现目标系统前编辑 `/etc/iscsi/iscsid.conf` 设置 `node.startup = automatic`。
    * 要寻找在线的目标系统。请以 root 身份运行 `iscsiadm -m discovery -t sendtargets -p _portal_` 其中 _portal_ 是 IPv4/IPv6 地址或主机名 
      * 如果使用主机名，请确保它路由到 IB IP 地址而不是以太网 - 只使用 IB IP 地址可能更佳。
    * 要在启动时自动登录已发现的目标系统，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `iscsi.service`
    * 要手动登录已发现的目标，请以 root 身份运行 `iscsiadm -m node -L all`。
    * 查看每个登录目标的块设备 ID。以 root 身份运行 `iscsiadm -m session -P 3 | grep Attached` 块设备 ID 将出现在每个目标树中的最后一行（`-P` 是打印命令，其选项是冗余级别，只有第 3 级才会列出块设备 ID）

#### Over iSER

iSER（iSCSI Extensions for RDMA）利用 IB 的 RDMA 协议，而不是使用 TCP/IP。它消除了 TCP/IP 的开销，提供了更高的带宽、零拷贝时间、更低的延迟和更低的 CPU 利用率。 

根据 [iSCSI Over IPoIB](<#Over_IPoIB>) 介绍， 并做出以下更改: 

  * 如果您愿意，可以直接[安装 RDMA 以加载内核模块](<#%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97>)，而不是[安装 IPoIB](<#TCP/IP_\(IPoIB\)>)。
  * 在目标系统上，完成其他设置后，仍在 `targetcli` 中启用目标系统上的 iSER: 
    * 对于每一个您希望使用 iSER 而不是 IPoIB的 _iqn_ ，运行 `cd /iscsi/_iqn_ /tpg1/portals/0.0.0.0:3260`
      * 其中 _iqn_ 是随机生成的目标名称，例如 `iqn.2003-01.org.linux-iscsi.hostname.x8664:sn.3d74b8d4020a`
    * 运行 `enable_iser true`
    * 保存并退出: `cd /`; `saveconfig`; 和 `exit`
  * 在 initiator 系统上，运行 `iscsiadm` 寻早在线 target 时，使用附加参数 `-Iiser`，登录 target 时，应该会看到: `Logging in to [iface: iser...`

####  添加到 /etc/fstab

您上次寻找目标系统时，自动登录一定是打开的。 

就像添加本地块设备一样在 `/etc/fstab` 中添加挂载项，只是需要添加 `_netdev` 选项，以避免在网络初始化前尝试挂载。 

##  网络划分

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 用示例解释更多细节 (在 [Talk:InfiniBand](<../zh-cn/Talk:InfiniBand.html>) 中讨论)

一个 IB 子网可以为不同的客户或应用分区，从而提供安全性和服务质量保证。每个分区由 PKEY（分区密钥）标识。 

##  SDP (Sockets Direct Protocol)

使用 `librdmacm` 和 `LD_PRELOAD` (rsockets和libspd的后续版本）和`LD_PRELOAD`来拦截非IB程序的套接字调用，并通过RDMA以透明方式（对程序而言）将其发送到IB上。这大大加快了为 TCP/IP 构建的程序的运行速度，远远超过使用 IPoIB 所能达到的速度。它避免了为使用 IB 而修改程序源代码，甚至可用于闭源程序。它不适用于静态链接套接字库的程序。 

##  诊断和基准测试

所有 IB 专用工具都包含在 [rdma-core](<https://archlinux.org/packages/?name=rdma-core>)包 和 [ibutils](<https://aur.archlinux.org/packages/ibutils/>)AUR 中。 

###  ibstat - 查看计算机的 IB GUIDs

ibstat 会显示计算机上运行的每个 IB 适配器的详细信息，包括：型号；端口数；固件和硬件版本；节点，系统映像和端口 GUID；端口状态，物理状态，速率，base lid，lmc，SM lid，capability mask，和链路层。 
    
    $ ibstat
    
    CA 'mlx4_0'
            CA type: MT25418
            Number of ports: 2
            Firmware version: 2.9.1000
            Hardware version: a0
            Node GUID: 0x0002c90300002f78
            System image GUID: 0x0002c90300002f7b
            Port 1:
                    State: Active
                    Physical state: LinkUp
                    Rate: 20
                    Base lid: 3
                    LMC: 0
                    SM lid: 3
                    Capability mask: 0x0251086a
                    Port GUID: 0x0002c90300002f79
                    Link layer: InfiniBand
            Port 2:
                    State: Down
                    Physical state: Polling
                    Rate: 10
                    Base lid: 0
                    LMC: 0
                    SM lid: 0
                    Capability mask: 0x02510868
                    Port GUID: 0x0002c90300002f7a
                    Link layer: InfiniBand

本例显示的是 Mellanox Technologies (MT) 适配器。报告的是它的 PCI Device ID（25418），而不是产品型号。它显示的状态是 “Active”，这意味着它已正确连接到子网管理器。它显示的物理状态为 “LinkUp”，这意味着它通过线缆进行了电气连接，但不一定与子网管理器正确连接。它显示的总速率为 20 Gb/s（对该卡来说，它来自 5.0 Gb/s 信号速率和 4 个虚拟通道）。它显示子网管理器为该端口分配了 3 个 Base lid 。 

###  ibhosts - 查看 IB 网络上的所有主机

ibhosts 会显示 IB 网络上每台主机的节点 GUID、端口数量和设备名称。 
    
    # ibhosts
    
    Ca      : 0x0002c90300002778 ports 2 "MT25408 ConnectX Mellanox Technologies"
    Ca      : 0x0002c90300002f78 ports 2 "hostname mlx4_0"
    
###  ibswitches - 查看 IB 网络上的所有交换机

ibswitches 会显示 IB 网络上每个交换机的节点 GUID、端口数量和设备名称。如果只使用直接连接，则不会显示任何内容。 
    
    # ibswitches
    
###  iblinkinfo - 查看 IB 网络链接信息

iblinkinfo 将显示设备名称、端口 GUID、虚拟通道数、[信号传输速率](<#%E4%BF%A1%E5%8F%B7%E4%BC%A0%E8%BE%93%E9%80%9F%E7%8E%87>)、状态、物理状态以及所连接的设备。 
    
    # iblinkinfo
    
    CA: MT25408 ConnectX Mellanox Technologies:
          0x0002c90300002779      4    1[  ] ==( 4X           5.0 Gbps Active/  LinkUp)==>       3    1[  ] "kvm mlx4_0" ( )
    CA: hostname mlx4_0:
          0x0002c90300002f79      3    1[  ] ==( 4X           5.0 Gbps Active/  LinkUp)==>       4    1[  ] "MT25408 ConnectX Mellanox Technologies" ( )

该示例展示了不使用交换机直接连接的两个适配器，使用 5.0 Gb/s [信号传输速率](<#%E4%BF%A1%E5%8F%B7%E4%BC%A0%E8%BE%93%E9%80%9F%E7%8E%87>)和 4 个虚拟通道 (4X)。 

###  ibping - Ping 另一个 IB 设备

ibping 将尝试 ping 另一个 IB GUID。 ibping 必须在一台计算机上以服务器模式运行，在另一台计算机上以客户端模式运行。 

ibping 必须在一台计算机上以服务器模式运行。 
    
    # ibping -S
    
而在另一个端口上则是客户端模式。它正在 ping 一个特定端口，因此不能使用 CA 名称、节点或系统 GUID。它需要`-G`和端口 GUID，或`-L`和Lid。 
    
    # ibping -G 0x0002c90300002779
    -or-
    # ibping -L 1
    
    Pong from hostname.(none) (Lid 1): time 0.053 ms
    Pong from hostname.(none) (Lid 1): time 0.074 ms
    ^C
    --- hostname.(none) (Lid 4) ibping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1630 ms
    rtt min/avg/max = 0.053/0.063/0.074 ms

如果运行的是 IPoIB，则可以使用通过 TCP/IP 协议栈 ping 的常规 `ping`。 ibping 使用 IB 接口，不使用 TCP/IP 协议栈。 

###  ibdiagnet - 显示整个子网的诊断信息

ibdiagnet 会显示子网中的潜在问题。您可以在不带选项的情况下运行它。 `-lw <1x|4x|12x>` 指定适配器的预期链路宽度(虚拟通道数)，这样它就能检查是否按预期运行。 `-ls <2.5|5|10>` 指定计算机适配器的预期链接速度（信号传输速率），以便检查其是否按预期运行，但对于 FDR+ 设备，它还不支持速度超过 10 的选项。 `-c <count>` 覆盖默认发送 10 个数据包。 
    
    # ibdiagnet -lw 4x -ls 5 -c 1000
    
    Loading IBDIAGNET from: /usr/lib/ibdiagnet1.5.7
    -W- Topology file is not specified.
        Reports regarding cluster links will use direct routes.
    Loading IBDM from: /usr/lib/ibdm1.5.7
    -I- Using port 1 as the local port.
    -I- Discovering ... 2 nodes (0 Switches & 2 CA-s) discovered.
    
    -I---------------------------------------------------
    -I- Bad Guids/LIDs Info
    -I---------------------------------------------------
    -I- No bad Guids were found
    
    -I---------------------------------------------------
    -I- Links With Logical State = INIT
    -I---------------------------------------------------
    -I- No bad Links (with logical state = INIT) were found
    
    -I---------------------------------------------------
    -I- General Device Info
    -I---------------------------------------------------
    
    -I---------------------------------------------------
    -I- PM Counters Info
    -I---------------------------------------------------
    -I- No illegal PM counters values were found
    
    -I---------------------------------------------------
    -I- Links With links width != 4x (as set by -lw option)
    -I---------------------------------------------------
    -I- No unmatched Links (with width != 4x) were found
    
    -I---------------------------------------------------
    -I- Links With links speed != 5 (as set by -ls option)
    -I---------------------------------------------------
    -I- No unmatched Links (with speed != 5) were found
    
    -I---------------------------------------------------
    -I- Fabric Partitions Report (see ibdiagnet.pkey for a full hosts list)
    -I---------------------------------------------------
    -I-    PKey:0x7fff Hosts:2 full:2 limited:0
    
    -I---------------------------------------------------
    -I- IPoIB Subnets Check
    -I---------------------------------------------------
    -I- Subnet: IPv4 PKey:0x7fff QKey:0x00000b1b MTU:2048Byte rate:10Gbps SL:0x00
    -W- Suboptimal rate for group. Lowest member rate:20Gbps > group-rate:10Gbps
    
    -I---------------------------------------------------
    -I- Bad Links Info
    -I- No bad link were found
    -I---------------------------------------------------
    ----------------------------------------------------------------
    -I- Stages Status Report:
        STAGE                                    Errors Warnings
        Bad GUIDs/LIDs Check                     0      0     
        Link State Active Check                  0      0     
        General Devices Info Report              0      0     
        Performance Counters Report              0      0     
        Specific Link Width Check                0      0     
        Specific Link Speed Check                0      0     
        Partitions Check                         0      0     
        IPoIB Subnets Check                      0      1     
    
    Please see /tmp/ibdiagnet.log for complete log
    ----------------------------------------------------------------
     
    -I- Done. Run time was 0 seconds.
    
###  qperf - 通过 RDMA 或 TCP/IP 测试性能

qperf 可通过 RDMA（SDP、UDP、UD 和 UC）或 TCP/IP（包括 IPoIB）测量带宽和延迟 

qperf 必须在一台计算机上以服务器模式运行。 
    
    $ qperf
    
而在另一台上以客户端模式运行。SERVERNODE 可以是主机名，或者 IPoIB 的 TCP/IP 地址。其中有许多测试。下面是一些最有用的测试。 
    
    $ qperf SERVERNODE [OPTIONS] TESTS
    
####  TCP/IP over IPoIB
    
    $ qperf 192.168.2.2 tcp_bw tcp_lat
    
    tcp_bw:
        bw  =  701 MB/sec
    tcp_lat:
        latency  =  19.8 us

###  iperf - 通过 TCP/IP 测试性能

iperf 不是一个 IB 感知的程序，它的目的是通过 TCP/IP 或 UDP 进行测试。尽管[qperf](<#qperf_-_Measure_performance_over_RDMA_or_TCP/IP>) 可以使用 IPoIB 测试 IB TCP/IP 性能，但 iperf 仍是另一个可以使用的程序。 

iperf 必须在一台计算机上以服务器模式运行。 
    
    $ iperf3 -s
    
在另一台上使用客户端模式 
    
    $ iperf3 -c 192.168.2.2
    
    [  4] local 192.168.2.1 port 20139 connected to 192.168.2.2 port 5201
    [ ID] Interval           Transfer     Bandwidth
    [  4]   0.00-1.00   sec   639 MBytes  5.36 Gbits/sec                  
    ...
    [  4]   9.00-10.00  sec   638 MBytes  5.35 Gbits/sec                  
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth
    [  4]   0.00-10.00  sec  6.23 GBytes  5.35 Gbits/sec                  sender
    [  4]   0.00-10.00  sec  6.23 GBytes  5.35 Gbits/sec                  receiver
    
    iperf Done.

iperf 以 10 GB 为基准显示传输量，以 2 GB 为基准显示带宽。因此，本例显示 10 秒内传输 6.23GB（base 10）。也就是 10 秒内传输 6.69GB（base 2）。(6.23 * 2^30 / 10^9) 即 5.35 Gb/s（base 2），如 iperf 所示。 (6.23 * 2^30 / 10^9 * 8 / 10) 即 685 MB/s（base 2），与 qperf 报告的速度大致相同。(6.23 * 2^30 / 10^9 * 8 / 10 * 1024 / 8) 

##  常见问题 / FAQ

###  链接问题

####  链路、物理状态和端口状态

  * 查看系统是否能识别 IB 硬件模块。如果您有英特尔适配器，则必须在此处使用Intel，如果您有其他英特尔硬件，则需要查看几行内容:

    # dmesg | grep -Ei "Mellanox|InfiniBand|QLogic|Voltaire"
    
    [    6.287556] mlx4_core: Mellanox ConnectX core driver v2.2-1 (Feb, 2014)
    [    8.686257] <mlx4_ib> mlx4_ib_add: mlx4_ib: Mellanox ConnectX InfiniBand driver v2.2-1 (Feb 2014)
    
    $ ls -l /sys/class/infiniband
    
    mlx4_0 -> ../../devices/pci0000:00/0000:00:03.0/0000:05:00.0/infiniband/mlx4_0

如果没有任何显示，则说明内核无法识别适配器。本示例显示了使用 mlx4_0 内核模块的 Mellanox ConnectX 适配器的大致情况。 

  * 检查端口和物理状态。运行 [ibstat](<#ibstat_-_%E6%9F%A5%E7%9C%8B%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%9A%84_IB_GUIDs>) 或检查 `/sys`.

    $ ibstat
    
    (look at the port shown that you expect to be connected)

或 
    
    $ cat /sys/class/infiniband/<kernel module>/ports/<port number>/phys_state
    
     5: LinkUp
    
    $ cat /sys/class/infiniband/<kernel module>/ports/<port number>/state
    
     4: ACTIVE

物理状态应为 “LinkUp”。如果不是，则可能是线缆没有插好、没有连接到另一端的任何设备或线缆有缺陷。端口状态应为 "Active"。如果是 "Initializing" 或 "INIT" ，则说明[子网管理器](<#%E5%AD%90%E7%BD%91%E7%AE%A1%E7%90%86%E5%99%A8>)不存在、未运行或未将端口添加到网络路由表中。 

  * 您能否成功 [ibping](<#ibping_-_Ping_another_IB_device>) 其他直接使用 IB 的设备而不是 IPoIB？ 如果运行 IPoIB，能否成功 `ping`？

  * 考虑[更新固件](<#%E6%9B%B4%E6%96%B0%E5%9B%BA%E4%BB%B6>).

#### getaddrinfo failed: Name or service not known

  * 运行 [ibhosts](<#ibhosts_-_%E6%9F%A5%E7%9C%8B_IB_%E7%BD%91%E7%BB%9C%E4%B8%8A%E7%9A%84%E6%89%80%E6%9C%89%E4%B8%BB%E6%9C%BA>) ，查看每行末尾带引号的 CA 名称

###  速度问题

  * 首先要仔细检查您的期望值。

您是如何确定存在速度问题的？您使用的是[qperf](<#qperf_-_%E9%80%9A%E8%BF%87_RDMA_%E6%88%96_TCP/IP_%E6%B5%8B%E8%AF%95%E6%80%A7%E8%83%BD>)还是[iperf](<#iperf_-_%E9%80%9A%E8%BF%87_TCP/IP_%E8%A1%A1%E9%87%8F%E6%80%A7%E8%83%BD>)，它们都是从内存而不是硬盘传输数据。或者，您是在对实际文件传输进行基准测试吗？除非你运行 RAID 来提高速度，否则即使使用 2015 年中期可用的最快固态硬盘，单个硬盘（有时甚至是多个硬盘）也会对 IB 传输速度造成瓶颈。您是通过 IPoIB 使用 RDMA 还是 TCP/IP？如果是，[使用 IPoIB 而不使用 RDMA 会影响性能](<#TCP/IP_\(IPoIB\)>)。 

  * 检查您的链接速度，运行 [ibstat](<#ibstat_-_%E6%9F%A5%E7%9C%8B%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%9A%84_IB_GUIDs>), [iblinkinfo](<#iblinkinfo_-_%E6%9F%A5%E7%9C%8B_IB_%E7%BD%91%E7%BB%9C%E9%93%BE%E6%8E%A5%E4%BF%A1%E6%81%AF>), 或者检查 `/sys`.

    $ ibstat
    
    (look at the Rate shown on the port you are using)

或 
    
    # iblinkinfo
    
    (look at the middle part formatted like "4X     5.0 Gbps")

或 
    
    $ cat /sys/class/infiniband/<kernel module>/ports/<port number>/rate
    
    20 Gb/sec (4X DDR)

这是否符合您预期的[带宽和虚拟通道数](<#%E5%B8%A6%E5%AE%BD>)？ 

  * 检查整个子网的诊断信息。 运行 [#ibdiagnet - 显示整个子网的诊断信息](<#ibdiagnet_-_%E6%98%BE%E7%A4%BA%E6%95%B4%E4%B8%AA%E5%AD%90%E7%BD%91%E7%9A%84%E8%AF%8A%E6%96%AD%E4%BF%A1%E6%81%AF>). 确保使用 `-ls ` 和[适当的信号传输速率，这可能是您 IB 卡的宣传速度除以 4](<#%E5%B8%A6%E5%AE%BD>).

    # ibdiagnet -lw <expected number of virtual lanes -ls <expected signaling rate> -c 1000
    
  * 考虑[更新固件](<#%E6%9B%B4%E6%96%B0%E5%9B%BA%E4%BB%B6>).
