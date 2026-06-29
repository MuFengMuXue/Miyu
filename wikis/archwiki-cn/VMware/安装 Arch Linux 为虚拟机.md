**翻译状态：**

  * 本文（或部分内容）译自 [VMware/Installing Arch as a guest](<https://wiki.archlinux.org/title/VMware/Installing_Arch_as_a_guest> "arch:VMware/Installing Arch as a guest")，最近一次同步于 2025-01-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/VMware/Installing_Arch_as_a_guest?diff=0&oldid=824810>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/VMware_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Installing_Arch_as_a_guest_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [VMware](<../../zh-cn/VMware.html> "VMware")
  * [VMWare vCLI](</wzh/index.php?title=VMWare_vCLI&action=edit&redlink=1> "VMWare vCLI（页面不存在）")

这篇文章是关于如何在 [VMware](<../../zh-cn/VMware.html> "VMware") 产品，比如 [Workstation Player](<https://www.vmware.com/products/workstation-player.html>)，[Fusion](<https://www.vmware.com/products/fusion.html>) 或 [Workstation Pro](<https://www.vmware.com/products/workstation-pro.html>) 中安装Arch Linux。 

##  编译进内核的驱动程序（模块）

**注意：** 下列模块只有部分会被 Arch 的 [Udev](<../../zh-cn/Udev.html> "Udev") 自动检测并启用。如果某些需要的模块没有被自动检测到（可通过 `lsmod | grep _modulename_` 进行确认），可以将其添加到 [mkinitcpio](<../../zh-cn/Mkinitcpio.html> "Mkinitcpio") 的 `MODULES` 列表。例如： 
    
    /etc/mkinitcpio.conf
    
    ...
    	
    MODULES=(... vmw_balloon vmw_pvscsi vsock vmw_vsock_vmci_transport ...)

确保 [重新生成 initramfs](<../../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

  * `vmw_balloon` \- 物理内存管理驱动。它可以像一个气球一样被“吹大”，在客户机上申请内存，并通过监视器释放掉这部分内存，使得这部分物理内存可以被分配给其它客户机使用；也可以"放气"，以允许虚拟机使用更多物理内存。还支持将反分配状态（deallocated）的虚拟机原本所占的内存释放回主机，而无需彻底停用虚拟机。
  * `vmw_pvscsi` \- VMware 平行虚拟化 SCSI（PVSCSI）的主机总线适配器（HBA）。
  * `vmw_vmci` \- 虚拟机通信接口（VMCI）。VMCI 虚拟设备的作用是实现虚拟环境中的主机-客机间高速通信。
  * `vmwgfx` \- 这是 VMware SVGA2 虚拟显卡的 DRM 驱动，作用是 3D 加速。支持 [KMS](<../../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS")。
  * `vmxnet3` \- VMware 的 vmxnet3 虚拟网卡所需模块。
  * [open-vm-tools](<https://archlinux.org/packages/?name=open-vm-tools>)包 10.0 以上版本包含了一个基于 [FUSE](<../../zh-cn/FUSE.html> "FUSE") 实现的 HGFS 文件系统，支持 Linux 4.0 及以上版本内核，用于主机-客机间共享目录。

如果你在某种监视器（比如 [VMware vSphere Hypervisor](<https://www.vmware.com/products/vsphere-hypervisor>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]）上运行 Arch Linux，那么同时需要安装下面这些模块。当虚拟机间通信时，客户机-服务器类型的应用可以通过 VMCI 虚拟设备向 VMCI 套接字（vsock）接口进行写入： 

  * `vsock` \- 虚拟套接字协议。其作用是允许虚拟机，主机或监视器间像 TCP/IP 协议一样通信。
  * `vmw_vsock_vmci_transport` \- 基于 VMCI 实现的虚拟套接字。

某些模块，例如旧的 `vmhgfs` 目录共享模块，还需要额外地手工编译，并手工从 systemd 启用服务，才能正常运转。 

##  VMware Tools 与 Open-VM-Tools 方案对比

2007 年，VMware 将 [VMware Tools](<https://kb.vmware.com/kb/340>) 中的大部分代码以 LGPL 协议发布，这就是 [Open-VM-Tools](<https://sourceforge.net/projects/open-vm-tools/>)。官方的 VMware Tools 不再[单独](<https://packages.vmware.com/tools/esx/latest/repos/index.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]向 Arch Linux 提供。 

以往，VMware Tools 方案所提供的网络与储存驱动是最好的，而且还带有时间同步等功能。然而网络与 SCSI 驱动这部分代码现已合并入 Linux 内核了。 

VMware Tools 曾经有使用 Unity mode 功能的优势，但由于使用的人不多且维护困难，于是从 VMWare Workstation 12 开始移除了 Linux 客户机的 Unity mode 支持。详情请阅[此跟帖](<https://communities.vmware.com/thread/518735>)的答案。 

## Open-VM-Tools

###  实用工具

[open-vm-tools](<https://archlinux.org/packages/?name=open-vm-tools>)包 软件包里包括如下工具： 

  * `vmtoolsd` \- 负责汇报虚拟机状态的服务。
  * `vmware-checkvm` \- 用于检测虚拟机中是否在运行着某程序的工具。
  * `vmware-toolbox-cmd` \- 用于收集宿主系统信息的工具。
  * `vmware-user` \- 用来在宿主机和虚拟机之间共享剪切板（复制/粘贴）的工具。
  * `vmware-vmblock-fuse` \- 文件系统工具。基于 [FUSE](<https://en.wikipedia.org/wiki/Filesystem_in_Userspace> "wikipedia:Filesystem in Userspace")（Filesystem in Userspace）实现了宿主/客机之间拖拽文件的功能。
  * `vmware-xferlogs` \- 向虚拟机的日志文件输出日志与调试信息。
  * `vmhgfs-fuse` \- 挂载 HGFS 共享目录的工具。

###  安装

[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [open-vm-tools](<https://archlinux.org/packages/?name=open-vm-tools>)包。然后[启动](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vmtoolsd.service` 和 `vmware-vmblock-fuse.service`。 

如果主机和客户机间复制粘贴功能无法正常工作，请尝试手动安装 [gtkmm3](<https://archlinux.org/packages/?name=gtkmm3>)包。 

##  官方的 VMware Tools

###  模块

  * `vmblock` \- 文件系统驱动。支持在主机-客机间拖拽文件。已被 `vmware-vmblock-fuse` [取代](<https://www.mail-archive.com/open-vm-tools-devel@lists.sourceforge.net/msg00213.html>)。
  * `vmci` \- 主机-客户机间的高性能通信接口。
  * `vmmon` \- 虚拟机监视器。
  * `vmnet` \- 网络驱动。
  * `vsock` \- VMCI 套接字。

**注意：**`vmware-vmblock-fuse` 这一组件不是以 内核 模块的形式实现的；且除非你禁用了 `fuse`，`vmblock` 已被从内核中移除。如果需要启用这些功能，需要手动启用 systemd 服务，具体操作见下文。 

###  在客户机安装

安装依赖项：[base-devel](<https://archlinux.org/groups/x86_64/base-devel/>)包组（用于编译模块），[net-tools](<https://archlinux.org/packages/?name=net-tools>)包（提供 `ifconfig` 供安装程序调用）和 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包 (提供内核头文件)。另外需要 [devtools](<https://archlinux.org/packages/?name=devtools>)包 包中的 `pkgctl` 来签出 `open-vm-tools`。 

然后为安装程序创建假 init 目录： 
    
    # for x in {0..6}; do mkdir -p /etc/init.d/rc${x}.d; done
    
挂载安装程序： 
    
    # mount /dev/cdrom /mnt
    
解压（以解压到 `/root` 为例）： 
    
    # tar xf /mnt/VMwareTools*.tar.gz -C /root
    
开始安装： 
    
    # perl /root/vmware-tools-distrib/vmware-install.pl
    
若安装时出现如下的错误，都可以安全忽略： 

  * VMXNET 3 虚拟网卡
  * "Warning: This script could not find mkinitrd or update-initramfs and cannot remake the initrd file!"
  * 在系统中找不到 Fuse 组件

启用 `vmware-vmblock-fuse` systemd 服务（请确保你手动安装了依赖或使用了 `-s` 参数）。`open-vm-tools` 源代码应当被 [Arch 构建系统](<../../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")签出。 
    
     $ pkgctl repo clone open-vm-tools
     $ cd open-vm-tools
     $ makepkg -s --asdeps
     # cp vm* /usr/lib/systemd/system
    
[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vmware-vmblock-fuse.service` 和 `vmtoolsd.service`。 

接下来重新启动虚拟机。 

登录并启动 VMware Tools: 
    
    # /etc/init.d/rc6.d/K99vmware-tools start
    
另外，可以通过创建 `/etc/systemd/system/vmwaretools.service` 文件来在启动时自动启动 `vmware-tools`： 
    
    /etc/systemd/system/vmwaretools.service
    
    [Unit]
    Description=VMWare Tools daemon
    
    [Service]
    ExecStart=/etc/init.d/vmware-tools start
    ExecStop=/etc/init.d/vmware-tools stop
    PIDFile=/var/lock/subsys/vmware
    TimeoutSec=0
    RemainAfterExit=yes
     
    [Install]
    WantedBy=multi-user.target

然后[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vmwaretools.service`。 

**提示：** 在 GitHub 上有个项目 [[1]](<https://github.com/rasa/vmware-tools-patches>) 尝试将这些步骤全自动处理。

##  Xorg 配置

**注意：** 要在虚拟机中使用 Xorg，至少需要为其分配 32MB 的显存。

需要安装以下依赖：[xf86-input-vmmouse](<https://archlinux.org/packages/?name=xf86-input-vmmouse>)包，[xf86-video-vmware](<https://archlinux.org/packages/?name=xf86-video-vmware>)包，以及 [mesa](<https://archlinux.org/packages/?name=mesa>)包。 

应该只需要这几个包就可以启动至 `graphical target` 了。接下来 `/etc/xdg/autostart/vmware-user.desktop` 会自动启动，并负责完成在虚拟机里运行的相关必要配置。 

然而如果你先启动至了 `multi-user.target`，或者你的环境不太常规（比如用了多个显示器），那么你需要手动[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vmtoolsd.service` 服务，并且还需要让 [Xorg 以根权限运行](<../../zh-cn/Xorg.html#Xorg_as_Root> "Xorg")以加载相关驱动。 

##  提示与技巧

###  通过 `vmhgfs-fuse` 共享目录

**注意：** 这一功能需要的最低软件版本是 `open-vm-tools` v.10.x 与 Linux 内核 4.x,同时需要 VMware Workstation / Fusion。

在菜单中选择 _Edit virtual machine settings > Options > Shared Folders > Always enabled_，即可建立共享目录。 

在客机里运行如下命令可以列出共享目录： 
    
    $ vmware-hgfsclient
    
然后以如下方式挂载： 
    
    # mkdir <shared folders root directory>
    # vmhgfs-fuse -o allow_other -o auto_unmount .host:/_< shared_folder>_ _< shared folders root directory>_
    
如果碰到了如下报错：`fusermount: option allow_other only allowed if 'user_allow_other' is set in /etc/fuse.conf`，需将 `/etc/fuse.conf` 中的这一行取消注释： 
    
    user_allow_other
    
欲了解 `vmhgfs-fuse` 的其他挂载参数，可以用 `-h` 参数调用： 
    
    # vmhgfs-fuse -h
    
**注意：** In case I/O operations (such as `cp`, `mv` or `cat`) result in an "Input/output error" when accessing the shared folder then setting the mount option `max_write` can serve as a workaround (observed with `open-vm-tools` version 11.1.0 and higher; see this bug report: <https://github.com/vmware/open-vm-tools/issues/437>)).

#### fstab

每个共享目录的挂载都需要写如下的一行配置： 
    
    /etc/fstab
    
    .host:/_< shared_folder>_ _< shared folders root directory>_ fuse.vmhgfs-fuse nofail,allow_other 0 0
    
然后创建并挂载目录： 
    
    # mkdir _< shared folders root directory>_
    # mount _< shared folders root directory>_
    
#### Systemd

创建如下 `.service` 文件： 
    
    /etc/systemd/system/_< shared folders root directory>_-_< shared_folder>_.service
    
    [Unit]
    Description=Load VMware shared folders
    Requires=vmware-vmblock-fuse.service
    After=vmware-vmblock-fuse.service
    ConditionPathExists=.host:/_< shared_folder>_
    ConditionVirtualization=vmware
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/bin/vmhgfs-fuse -o allow_other -o auto_unmount .host:/_< shared_folder>_ _< shared folders root directory>_
    
    [Install]
    WantedBy=multi-user.target

如果客机里的 `_< shared folders root directory>_` 目录还不存在，你需要手动提前创建： 
    
    # mkdir -p _< shared folders root directory>_
    
然后[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `<shared folders root directory>-<shared_folder>.service` 挂载目标。 

删掉 _< shared_folder>_ 的部分可以一次性挂载所有共享目录。 

###  使用 vmhgfs 模块的旧式目录共享

**注意：** 该功能只在 VMware Workstation 和 Fusion 中可用

在菜单中选择 _Edit virtual machine settings > Options > Shared Folders > Always enabled_，即可建立共享目录。 

确保已加载 `vmhgfs` 驱动： 
    
    # modprobe vmhgfs
    
可以通过以下命令查看共享目录清单： 
    
    $ vmware-hgfsclient
    
然后可以通过如下命令挂载目录： 
    
    # mkdir /home/user1/shares
    # mount -n -t vmhgfs .host:/_< shared_folder>_ /home/user1/shares
    
####  在启动时启用

按照如下编辑 `mkinitcpio.conf` 文件： 
    
    /etc/mkinitcpio.conf
    
    ...
    MODULES=(... vmhgfs)
    ...

然后[重新生成 initramfs](<../../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

##### fstab

每个共享目录的挂载都需要写如下的一行配置： 
    
    /etc/fstab
    
    .host:/_< shared_folder>_ _/home/user1/shares_ vmhgfs defaults 0 0
    
然后创建并挂载目录： 
    
    # mkdir /home/user1/shares
    # mount /home/user1/shares
    
##### Systemd

共享目录需用到 `vmhgfs` 驱动。参考如下案例创建 `.service` 文件： 
    
    /etc/systemd/system/_< shared folders root directory>_-_< shared_folder>_.mount
    
    [Unit]
    Description=Load VMware shared folders
    ConditionPathExists=.host:/_< shared_folder>_
    ConditionVirtualization=vmware
    
    [Mount]
    What=.host:/_< shared_folder>_
    Where=_< shared folders root directory>_/_< shared_folder>_
    Type=vmhgfs
    Options=defaults,noatime
    
    [Install]
    WantedBy=multi-user.target
    
    /etc/systemd/system/_< shared folders root directory>_-_< shared_folder>_.automount
    
    [Unit]
    Description=Load VMware shared folders
    ConditionPathExists=.host:/_< shared_folder>_
    ConditionVirtualization=vmware
    
    [Automount]
    Where=_< shared folders root directory>_/_< shared_folder>_
    
    [Install]
    WantedBy=multi-user.target

如果客户机内还没有 `_< shared folders root directory>_` 目录，你需要手动提前创建： 
    
    # mkdir -p _< shared folders root directory>_
    
然后[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `mnt-hgfs.automount` 挂载目标。 

删掉 _< shared_folder>_ 的部分可以一次性挂载所有共享目录。 

####  清理 locate DB

在使用 [locate](<../../zh-cn/Locate.html> "Locate") 时，不需要在 `locate DB` 中为共享目录进行索引。因此，可以将共享目录添加到 `/etc/updatedb.conf` 中的 `PRUNEPATHS`。 

###  3D 加速

如果在创建客户机时没有选择 3D 加速功能，可以勾选: _编辑虚拟机设置 > 硬件 > 显示器 > 加速 3D 图形_。 

**注意：** 启用 3D 加速之后，Xorg 的性能可能会很差。有些时候通过 llvmpipe 来实现软件渲染的性能可能更好。

####  OpenGL 与 GLSL 支持

用户可以自行更新实现 OpenGL 的 GLSL 内核模块，覆盖 Arch 自带的版本。 

本文成文时，OpenGL 3.3 和 GLSL 3.30 都得到了支持。参阅 <https://bbs.archlinux.org/viewtopic.php?id=202713> 可以了解更多细节。 

###  时间同步

为虚拟机配置时间同步很重要，因为虚拟机比物理机更容易出现时间波动现象。主要原因就在于 CPU 是被共用的。 

有两种方案可以实现同步：与宿主机同步，或是通过外部服务器同步。 

####  与宿主机同步时间

先确保 `vmtoolsd.service` 服务已[启动](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")，然后用如下命令启用时间同步功能： 
    
    # vmware-toolbox-cmd timesync enable
    
宿主系统休眠后，用如下的命令来使客机间同步时间： 
    
    # hwclock --hctosys --localtime
    
####  与外部服务器同步时间

参阅 [NTP](<../../zh-cn/Category:NTP.html> "NTP")。 

##  故障排除

###  客户机网络速度减慢

Arch Linux 和其它 Linux 客户机一样，当使用 NAT 模式的时候也许会碰到网络速度减慢的问题。为了解决这个问题，请在宿主机下把对应的客户机的网络模式切换为**桥接模式** ，在必要时修改客户机网络的配置文件。有关配置的详细信息请参阅[网络配置](<../../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")。如果在 Windows 宿主机下，使用正确的客户机网络配置仍然无法正确连接网络, 可使用**管理员** 运行**虚拟网络编辑器** 并点击左下方的**还原默认设置** 按钮。 

###  声音问题

如果虚拟机发出了恼人的巨响，那有可能是 [PC 扬声器](<../../zh-cn/PC_%E6%89%AC%E5%A3%B0%E5%99%A8.html> "PC 扬声器")的原因。在客户机系统里[禁用 PC 扬声器](<../../zh-cn/PC_%E6%89%AC%E5%A3%B0%E5%99%A8.html#%E7%A6%81%E7%94%A8PC%E5%96%87%E5%8F%AD> "PC 扬声器")即可解决。 

###  音/视频卡顿

在虚拟机环境下，在软件（如火狐和系统通知等）中回放音/视频时可能会出现卡顿、噪声和延迟。这些问题通常和 PipeWire 音频后端及模拟驱动有关，调整 ALSA 的 ringbuffer 设置或 PipeWire 的配置有助于解决这些问题。 

具体的排障和修复步骤请参考论坛帖子：[Audio and Video stuttering/crackling](<https://bbs.archlinux.org/viewtopic.php?id=280654>)。 

###  鼠标问题

虚拟机可能会出现下列鼠标问题： 

  * 自动获取/失去焦点的功能可能会在鼠标箭头移入窗口时失效
  * 按键无响应
  * 卡顿、延迟
  * 在个别软件中点击无响应
  * 箭头在移入/移出虚拟机时跳跃
  * 箭头会跳跃到从虚拟机移出的位置

可以先尝试[卸载](<../../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "卸载") [xf86-input-vmmouse](<https://archlinux.org/packages/?name=xf86-input-vmmouse>)包 包，[xf86-input-vmmouse](<https://archlinux.org/packages/?name=xf86-input-vmmouse>)包 和 [xf86-input-libinput](<https://archlinux.org/packages/?name=xf86-input-libinput>)包 应足以处理鼠标和键盘输入。 

为解决[鼠标箭头跳跃到从虚拟机移出的位置](<https://forums.mageia.org/en/viewtopic.php?f=7&t=7977>)的问题，可以试试在 `.vmx` 配置文件里添加如下配置： 
    
    ~/vmware/_< Virtual Machine name>_/_< Virtual Machine name>_.vmx
    
    mouse.vusb.enable = "TRUE"
    mouse.vusb.useBasicMouse = "FALSE"

VMware 还会为游戏做自动的鼠标优化。如果这一优化产生了问题，可以在这里将其禁用： _Edit > Preferences > Input > Optimize mouse for games: Never_

再者，尝试在 `60-libinput.conf` 里[禁用](<https://www.spinics.net/lists/xorg/msg53932.html>) `catchall` 事件也可能有用： 
    
    /usr/share/X11/xorg.conf.d/60-libinput.conf
    
    #Section "InputClass"
    #        Identifier "libinput pointer catchall"
    #        MatchIsPointer "on"
    #        MatchDevicePath "/dev/input/event*"
    #        Driver "libinput"
    #EndSection
    
###  启动故障

####  启动速度慢

如果 VMware 开启了内存热扩容功能，那么有可能会出现如下错误： 

  * add_memory failed
  * acpi_memory_enable_device() error

可以在 `.vmx` 配置文件里写入 `mem.hotadd = "FALSE"` 来禁用内存热扩容功能。 
    
    ~/vmware/_< Virtual Machine name>_/_< Virtual Machine name>_.vmx
    
    mem.hotadd = "FALSE"

####  关机/重启时卡住不动

试着降低 vmtoolsd 服务的超时阈值（默认是 90 秒）： 
    
    /etc/systemd/system/vmtoolsd.service.d/timeout.conf
    
    [Service]
    TimeoutStopSec=1

###  窗口分辨率自动适配

自动适配的意思是，当你在宿主机里缩放 VMware 窗口之后，Arch 作为客户机系统，应该自动根据主系统窗口的新尺寸来调整分辨率。 

####  方案 1

确保在设置里开启了自动适配。 

VMware Worksation 的这一设置位于： _View - > Autosize -> Autofit Guest_

####  方案 2

出于某些原因，分辨率自动适配的功能依赖于 [gtkmm](<https://archlinux.org/packages/?name=gtkmm>)包 和 [gtk2](<https://archlinux.org/packages/?name=gtk2>)包 软件包，所以需确保客户机上已安装这两个包。如果客户机没有安装 X windows 或使用的桌面环境不依赖于 GTK（例如 KDE），那么你需要手动安装这两个包。 

####  方案 3

可能需要向 mkinitcpio.conf 添加相关模块： 
    
    /etc/mkinitcpio.conf
    
    MODULES=(vsock vmw_vsock_vmci_transport vmw_balloon vmw_vmci vmwgfx)

不要忘了[重新生成 initramfs](<../../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

####  方案 4

[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `vmtoolsd.service`。 

如果不起效，需确保 `vmtoolsd.service` 已正常[重启](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")。 

####  方案 5

If [GNOME](<../../zh-cn/GNOME.html> "GNOME") is running on [Wayland](<../../zh-cn/Wayland.html> "Wayland"), [install](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [xf86-video-vmware](<https://archlinux.org/packages/?name=xf86-video-vmware>)包 ([FS#57473](<https://bugs.archlinux.org/task/57473>)). 

See [[2]](<https://github.com/vmware/open-vm-tools/issues/22#issuecomment-362705505>). 

####  方案 6

Make sure that Stretch Mode is disabled. Follow _VM > Settings > Display > Display Scaling_ and untick the option _Stretch mode_. 

####  潜在的方案 7

通过[内核命令行参数](<../../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")的 `video=` 选项[手动设置分辨率](<../../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#Forcing_modes> "内核级显示模式设置")。 

###  拖拽与复制粘贴

**提示：** 这些功能与 _gtkmm3_ 有着未指明的依赖关系，并会导致这些功能静默失败。此问题在 [FS#43159](<https://bugs.archlinux.org/task/43159>)有详述。

为了确保拖拽与复制粘贴功能正常工作，需要安装 [open-vm-tools](<https://archlinux.org/packages/?name=open-vm-tools>)包 和 [gtkmm3](<https://archlinux.org/packages/?name=gtkmm3>)包 这两个包。 

使 `vmware-user` 在 [X11](<../../zh-cn/Xorg.html> "X11") 之后运行： 

  * 确保 `/etc/xdg/autostart/vmware-user.desktop` 存在，如果文件不存在，请运行：

    # cp /etc/vmware-tools/vmware-user.desktop /etc/xdg/autostart/vmware-user.desktop
    
或 

  * 添加 `vmware-user` 到 [Xinitrc](<../../zh-cn/Xinit.html#xinitrc> "Xinitrc")

[Wayland 暂不支持](<https://github.com/vmware/open-vm-tools/issues/443>)复制粘贴功能，但使用 [Xwayland](<../../zh-cn/Wayland.html#Xwayland> "Xwayland") 的应用可以正常使用该功能。 

###  在 VMware Workstation 11 版上运行共享 VM

Workstation 11 有个 bug：当 Arch 客户机以共享 VM 模式运行，且启动了 vmtoolsd 服务时，vmware-hostd 会崩溃。open-vm-tools 有个补丁来[绕过](<https://github.com/vmware/open-vm-tools/issues/31>)这一问题。 

## Virtual Network Editor Wayland

[Running GUI applications as root](</wzh/index.php?title=Running_GUI_applications_as_root&action=edit&redlink=1> "Running GUI applications as root（页面不存在）") \-- some of the following is copied from 

  * When running VMWare workstation on a wayland host the Virtual Network Editor will not launch under Wayland this because

Trying to run a graphical application as root via [su](<../../zh-cn/Su.html> "Su"), [sudo](<../../zh-cn/Sudo.html> "Sudo") or [pkexec](<../../zh-cn/Polkit.html> "Polkit") in a Wayland session (e.g. [GParted](<../../zh-cn/Parted.html> "GParted") or [Gedit](</wzh/index.php?title=Gedit&action=edit&redlink=1> "Gedit（页面不存在）")), will fail with an error similar to this: 
    
    $ sudo vmware-netcfg
    No protocol specified
    Unable to init server: Could not connect: Connection refused
    
    (gedit:2349): Gtk-WARNING **: cannot open display: :0
    
This is a security feature of Wayland they reason GUI applications should not be run as root. This can be achieved using the following in the terminal 

### Using xhost

A more versatile —though much less secure— workaround is to use [xhost](<../../zh-cn/Xhost.html> "Xhost") to temporarily allow the root user to access the local user's X session[[3]](<https://bugzilla.redhat.com/show_bug.cgi?id=1274451#c64>). To do so, execute the following command as the current (unprivileged) user: 
    
    $ xhost si:localuser:root
    
To remove this access after the application has been closed: 
    
    $ xhost -si:localuser:root
    
### Using sudo -E

Launch vmware-netcfg with: 
    
    $ sudo -E vmware-netcfg
    