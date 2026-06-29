**翻译状态：**

  * 本文（或部分内容）译自 [Libvirt](<https://wiki.archlinux.org/title/Libvirt> "arch:Libvirt")，最近一次同步于 2025-3-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Libvirt?diff=0&oldid=828554>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Libvirt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [PCI passthrough via OVMF](<../zh-cn/PCI_passthrough_via_OVMF.html> "PCI passthrough via OVMF")
  * [Category:Hypervisors](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:Hypervisors")

Libvirt 是一组软件的汇集，提供了管理虚拟机和其它虚拟化功能（如：存储和网络接口等）的便利途径。这些软件包括：一个长期稳定的 C 语言 API、一个守护进程（libvirtd）和一个命令行工具（virsh）。Libvirt 的主要目标是提供一个单一途径以管理多种不同虚拟化方案以及虚拟化主机，包括：[KVM/QEMU](<../zh-cn/QEMU.html> "QEMU")，[Xen](<../zh-cn/Xen.html> "Xen")，[LXC](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "LXC")，[OpenVZ](<https://openvz.org>) 或 [VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") [hypervisors](<../zh-cn/Category:%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%AE%A1%E7%90%86.html> "Category:Hypervisors") （[详见这里](<https://libvirt.org/drivers.html>)）。 

Libvirt 的一些主要功能如下： 

  * **VM management（虚拟机管理）** ：各种虚拟机生命周期的操作，如：启动、停止、暂停、保存、恢复和迁移等；多种不同类型设备的热插拔操作，包括磁盘、网络接口、内存、CPU等。
  * **Remote machine support（支持远程连接）** ：Libvirt 的所有功能都可以在运行着 libvirt 守护进程的机器上执行，包括远程机器。可以使用最简便且无需额外配置的 SSH 协议，也可以使用受支持的多种网络连接方式。
  * **Storage management（存储管理）** ：任何运行 libvirt 守护进程的主机都可以用于管理多种类型的存储：创建多种类型的文件镜像（qcow2，vmdk，raw，...），挂载 NFS 共享，枚举现有 LVM 卷组，创建新的 LVM 卷组和逻辑卷，对裸磁盘设备分区，挂载 iSCSI 共享，以及更多......
  * **Network interface management（网络接口管理）** ：任何运行 libvirt 守护进程的主机都可以用于管理物理的和逻辑的网络接口，枚举现有接口，配置（和创建）接口、桥接、VLAN、端口绑定。
  * **Virtual NAT and Route based networking（虚拟 NAT 和基于路由的网络）** ：任何运行 libvirt 守护进程的主机都可以管理和创建虚拟网络。Libvirt 虚拟网络使用防火墙规则实现一个路由器，为虚拟机提供到主机网络的透明访问。

##  安装

基于守护进程/客户端的架构的 libvirt 只需要安装在需要要实现虚拟化的机器上。注意，服务器和客户端可以是相同的物理机器。 

###  服务端

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libvirt](<https://archlinux.org/packages/?name=libvirt>)包 以及至少一个虚拟运行环境（hypervisor）： 

  * [libvirt 的 KVM/QEMU 驱动](<https://libvirt.org/drvqemu.html>)是 _libvirt_ 的首选驱动，如果 KVM 功能已[启用](<../zh-cn/QEMU.html#%E5%90%AF%E7%94%A8_KVM> "QEMU")，则支持全虚拟化和硬件加速的客户机。详见 [QEMU](<../zh-cn/QEMU.html> "QEMU")。

  * 其他[受支持的虚拟运行环境](<https://libvirt.org/drivers.html>)包括 [LXC](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "LXC")、[VirtualBox](<../zh-cn/VirtualBox.html> "VirtualBox") 和 [Xen](<../zh-cn/Xen.html> "Xen")。请参见它们各自的安装说明。有关 `libvirtd` 的安装备注： 
    * [Libvirt 的 LXC 驱动](<https://libvirt.org/drvlxc.html>)并不依赖 [lxc](<https://archlinux.org/packages/?name=lxc>)包 提供的 [LXC](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "LXC") 用户空间工具。因此，无需安装该工具也能使用这个驱动。需要 `libvirtd` 处于运行状态才能使用 `libvirt-lxc` 连接。
    * Libvirt 能支持 [Xen](<../zh-cn/Xen.html> "Xen")，但默认未内建支持（[FS#27356](<https://bugs.archlinux.org/task/27356>)）。需要用 [ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS") 编辑 [libvirt](<https://archlinux.org/packages/?name=libvirt>)包 的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") ，去掉 `-Ddriver_libxl=disabled` 选项后重新构建（built）libvirt。

对于网络连接，需要安装这些包： 

  * [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包 用于[默认的](<https://wiki.libvirt.org/VirtualNetworking.html#the-default-configuration>) NAT/DHCP 网络
  * [openbsd-netcat](<https://archlinux.org/packages/?name=openbsd-netcat>)包 用于 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 远程管理

其他可选依赖项可能提供所需或扩展功能，例如 [dmidecode](<https://archlinux.org/packages/?name=dmidecode>)包 用于支持 DMI 系统信息。建议在阅读 [libvirt](<https://archlinux.org/packages/?name=libvirt>)包 的 pacman 输出后，将所需组件[作为依赖项](<../zh-cn/Pacman.html#Installation_reason> "Pacman")安装。 

**注意：** 若正在使用 [firewalld](<../zh-cn/Firewalld.html> "Firewalld")，从 `libvirt` 5.1.0 和 [firewalld](<../zh-cn/Firewalld.html> "Firewalld") 0.7.0 开始，不再需要将防火墙后端改为 [iptables](<../zh-cn/Iptables.html> "Iptables")。`libvirt` 现在会在 [firewalld](<../zh-cn/Firewalld.html> "Firewalld") 中自动创建名为 'libvirt' 的区域，并在该区域管理其所需的网络规则。详见 [Firewall and network filtering in libvirt](<https://libvirt.org/firewall.html>).

###  客户端

客户端是用于管理和访问虚拟机的用户界面。 

  * **virsh** — 用于管理和配置域（虚拟机）的命令行程序。

     <https://libvirt.org/> || [libvirt](<https://archlinux.org/packages/?name=libvirt>)包

  * **[Boxes](<https://en.wikipedia.org/wiki/GNOME_Boxes> "wikipedia:GNOME Boxes")** — 简单的 GNOME 3 程序，可以访问远程虚拟系统。是 [gnome-extra](<https://archlinux.org/groups/x86_64/gnome-extra/>)包组的一部分。

     <https://apps.gnome.org/Boxes> || [gnome-boxes](<https://archlinux.org/packages/?name=gnome-boxes>)包

  * **Libvirt Sandbox** — 应用程序沙箱工具包。

     <https://sandbox.libvirt.org/> || [libvirt-sandbox](<https://aur.archlinux.org/packages/libvirt-sandbox/>)AUR

  * **Virt Viewer** — 简单的远程显示客户端。

     <https://gitlab.com/virt-viewer/virt-viewer> || [virt-viewer](<https://archlinux.org/packages/?name=virt-viewer>)包

  * **[Virt-manager](</wzh/index.php?title=Virt-manager&action=edit&redlink=1> "Virt-manager（页面不存在）") （英语：[Virt-manager](<https://wiki.archlinux.org/title/Virt-manager> "en:Virt-manager")）** — 用于图形化使用 libvirt 管理 KVM，Xen 或是 LXC。

     <https://virt-manager.org/> || [virt-manager](<https://archlinux.org/packages/?name=virt-manager>)包

  * **[Cockpit](</wzh/index.php?title=Cockpit&action=edit&redlink=1> "Cockpit（页面不存在）") （英语：[Cockpit](<https://wiki.archlinux.org/title/Cockpit> "en:Cockpit")）** — 基于网页的系统管理工具，可通过插件管理虚拟机。

     <https://cockpit-project.org/> || [cockpit-machines](<https://archlinux.org/packages/?name=cockpit-machines>)包

兼容 libvirt 的软件列表见[这里](<https://libvirt.org/apps.html>)。 

##  配置

Libvirt 可通过两种模式管理 QEMU 虚拟机：system（系统模式）和 session（会话模式）[[1]](<https://libvirt.org/drvqemu.html#connections-to-qemu-driver>)[[2]](<https://wiki.libvirt.org/FAQ.html#what-is-the-difference-between-qemu-system-and-qemu-session-which-one-should-i-use>)： 

  * **system** URI 连接到以 root 身份运行的 libvirtd daemon（该进程在系统启动时加载）。使用 'system' 模式创建和运行的虚拟机默认以 root 身份启动，除非另行配置（例如通过 `/etc/libvirt/qemu.conf`）。
  * **session** URI 会以当前本地用户身份启动 libvirtd 实例，所有虚拟机均以该用户权限运行。

**模式对比分析** ： 

  * 仅 'system' 模式支持虚拟机随宿主机启动自动运行，且 root 权限的 libvirtd 实例拥有通过 bridge 或虚拟网络配置完整网络连接的权限。`qemu:///system` 通常是 virt-manager 等工具的默认选项。 
    * `qemu:///session` 存在显著缺陷：由于 libvirtd 实例权限不足，仅支持 qemu 的 usermode networking（用户模式网络），该模式存在隐性限制，因此不建议使用（[详见qemu 网络配置](<https://web.archive.org/web/20210426155203/https://people.gnome.org/~markmc/qemu-networking.html>)）。

`qemu:///session` 的优势在于权限简化：用户可直接在 $HOME 存储磁盘镜像、串行 PTY 设备归属用户自身等。 

对于 _**系统**_ 级别的管理任务（如：全局配置和镜像 _卷_ 位置），libvirt 要求至少要[设置授权](<#%E8%AE%BE%E7%BD%AE%E6%8E%88%E6%9D%83>)和[启动守护进程](<#%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B>)。 

对于用户 _**会话**_ 级别的管理任务，守护进程的安装和设置 _不是_ 必须的。授权总是仅限本地，前台程序将启动一个 **libvirtd** 守护进程的本地实例。 

###  设置授权

来自 [libvirt：连接授权](<https://libvirt.org/auth.html#ACL_server_config>)： 

    Libvirt 守护进程允许管理员分别为客户端连接的每个网络 socket 选择不同授权机制。这主要是通过 libvirt 守护进程的主配置文件 `/etc/libvirt/libvirtd.conf` 来实现的。每个 libvirt socket 可以有独立的授权机制配置。目前的可选项有 `none`、`polkit` 和 `sasl`。

#### Using libvirt group

把用户加到 `libvirt` [user group 用户组](</wzh/index.php?title=User_group_%E7%94%A8%E6%88%B7%E7%BB%84&action=edit&redlink=1> "User group 用户组（页面不存在）")是确保该用户可以访问libvirt daemon的最简单方法。 

默认情况下，`libvirt` 组的成员对 RW 守护程序套接字具有免密访问权限。 

####  使用 polkit

Because [libvirt](<https://archlinux.org/packages/?name=libvirt>)包 pulls [polkit](<https://archlinux.org/packages/?name=polkit>)包 as a dependency during installation, [polkit](<../zh-cn/Polkit.html> "Polkit") is used as the default value for the `unix_sock_auth` parameter ([source](<https://libvirt.org/auth.html#ACL_server_polkit>)). [File-based permissions](<#Authenticate_with_file-based_permissions>) remain nevertheless available. 

**注意：** 为使 `polkit` 认证工作正常，应该重启一次系统。

_libvirt_ 守护进程在 polkit 策略配置文件（`/usr/share/polkit-1/actions/org.libvirt.unix.policy`）中提供了两种 [polkit 操作](<../zh-cn/Polkit.html#Actions> "Polkit")： 

  * `org.libvirt.unix.manage` 面向完全的管理访问（读写模式后台 socket），以及
  * `org.libvirt.unix.monitor` 面向仅监视察看访问（只读 socket）。

默认的面向读写模式后台 socket 的策略需要认证为管理员。这点类似于 [sudo](<../zh-cn/Sudo.html> "Sudo") 认证，但它并不要求客户应用最终以 root 身份运行。默认策略下也仍然允许任何应用连接到只读 socket。 

Arch Linux 默认 `wheel` 组的所有用户都是管理员身份：定义于 `/etc/polkit-1/rules.d/50-default.rules`（参阅：[Polkit#管理员身份认证](<../zh-cn/Polkit.html#%E7%AE%A1%E7%90%86%E5%91%98%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81> "Polkit")）。所以**如果用户是`wheel` 组的成员**，就不必新建组和规则文件：只要连接到了读写模式 socket（例如通过 [virt-manager](<https://archlinux.org/packages/?name=virt-manager>)包）就会被提示输入该用户的口令。 

**注意：** 口令提示依赖于系统上的[身份认证组件](<../zh-cn/Polkit.html#%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81%E7%BB%84%E4%BB%B6> "Polkit")。文本控制台默认的认证代理是 `pkttyagent`，它可能因工作不正常而导致各种问题。

**提示：** 如果要配置无口令认证，参阅 [Polkit#跳过口令提示](<../zh-cn/Polkit.html#%E8%B7%B3%E8%BF%87%E5%8F%A3%E4%BB%A4%E6%8F%90%E7%A4%BA> "Polkit")。

你可能想要修改授权以读写模式访问 socket 的组。例如，你想授权 `mykvm` 组，可创建下面的文件： 
    
    /etc/polkit-1/rules.d/50-libvirt.rules
    
    /* Allow users in mykvm group to manage the libvirt
    daemon without authentication */
    polkit.addRule(function(action, subject) {
        if (action.id == "org.libvirt.unix.manage" &&
            subject.isInGroup("mykvm")) {
                return polkit.Result.YES;
        }
    });
    
然后[添加自己](<../zh-cn/Users_and_groups.html#%E5%85%B6%E4%BB%96%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86%E7%A4%BA%E4%BE%8B> "Users and groups")到 `mykvm` 组并重新登录。可以将 _mykvm_ 替换为你想要的任意组，只需确保该组存在，且用户是该组的成员（详情可参考[用户和用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")）。 

修改组之后不要忘记重新登录才能生效。 

####  基于文件的权限授权

为了给 _libvirt_ 组用户定义基于文件的权限以管理虚拟机，取消下列行的注释： 
    
    /etc/libvirt/libvirtd.conf
    
    #unix_sock_group = "libvirt"
    #unix_sock_ro_perms = "0777"  # set to 0770 to deny non-group libvirt users
    #unix_sock_rw_perms = "0770"
    #auth_unix_ro = "none"
    #auth_unix_rw = "none"
    
有些资料提到可以通过改变某些特定 libvirt 目录的权限以简化管理。需要记住的是：包更新时，这些变更会丢失。如要修改这些系统目录的权限，需要 root 用户权限。 

###  守护进程

**注意：** Libvirt 正在从单个整体守护进程转变为单独的模块化守护进程，目的是在将来删除整体守护进程。参见 [Libvirt daemons](<https://libvirt.org/daemons.html#modular-driver-daemons>) 获取更多信息。

`libvirtd.service` 和 `virtlogd.service`这两个服务单元都要[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")。可以把 `libvirtd.service` 设置为[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")，这时系统将同时启用 `virtlogd.service` 和 `virtlockd.socket` 两个服务[单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")，因此后二者不必再设置为**启用** 。 

另一种方案是仅[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `libvirtd.socket` 与 `virtlogd.socket`，以实现按需 socket 激活。 

###  非加密的 TCP/IP sockets

**警告：** 这种方法常用于在可信网络中快速连接远程域做协助。这是 _**最不安全**_ 的连接方式，应当 _仅仅_ 用于测试或用于安全、私密和可信的网络环境。这时 SASL 没有启用，所以所有的 TCP 通讯都是 _明文_ 传输。在正式的应用场合应当 _始终_ 启用 SASL。

编辑 `/etc/libvirt/libvirtd.conf`： 
    
    /etc/libvirt/libvirtd.conf
    
    listen_tls = 0
    listen_tcp = 1
    auth_tcp="none"
    
同时需要编辑 `/etc/conf.d/libvirtd` 以在监听模式下启动服务： 
    
    /etc/conf.d/libvirtd
    
    LIBVIRTD_ARGS="--listen"

###  用主机名访问虚拟机

在非隔离的、桥接的网络中从宿主机访问客户机，可以通过启用 [libvirt](<https://archlinux.org/packages/?name=libvirt>)包 提供的 `libvirt` 和/或 `libvirt_guest` NSS 模块来实现。For the comparison of the two modules and technical details, see [libvirt documentation](<https://libvirt.org/nss.html>). 

在 [nsswitch.conf(5)](<https://man.archlinux.org/man/nsswitch.conf.5>) 中添加需要的模块： 
    
    /etc/nsswitch.conf
    
    hosts: files **libvirt libvirt_guest** dns myhostname
    
**注意：** `ping` 和 `ssh` 这类命令使用虚拟机主机名可以正常工作，但 `host` 和 `nslookup` 这类命令可能会失败或产生非预期结果，因后者依赖 DNS 。应改用 `getent hosts <vm-hostname>` 命令。

##  测试

测试 libvirt 在 _系统_ 级工作是否正常： 
    
    $ virsh -c qemu:///system
    
测试 libvirt 在用户 _会话_ 级工作是否正常： 
    
    $ virsh -c qemu:///session
    
##  管理

绝大部分的 libvirt 管理可以通过三个工具实现：[virt-manager](<https://archlinux.org/packages/?name=virt-manager>)包（图形界面）、`virsh` 和 `guestfish`（它是 [libguestfs](<https://archlinux.org/packages/?name=libguestfs>)包 的一部分）。 

### virsh

Visrsh 用于管理客户 _域_ （虚拟机），适用于脚本及虚拟环境管理工作。受限于与虚拟化环境通信的通道，绝大部分 virsh 命令需要管理员权限。尽管如此，一些典型的管理操作如域的创建、运行等也可以像 VirtualBox 那样以普通用户身份执行。 

Virsh 允许带命令行选项执行。如果不带则进入其内置的交互式终端：`virsh`。交互式终端支持 tab 键命令补全。 

从命令行执行： 
    
    $ virsh [可选项] <命令> [参数]...
    
在交互式终端里运行： 
    
    virsh # <命令> [参数]...
    
帮助也是可用的： 
    
    $ virsh help [option*] or [group-keyword*]
    
###  存储池

存储池是指保存 _卷_ 的位置。Libvirt 中 _卷_ 的定义相当于其他系统中 _虚拟磁盘_ 或 _虚拟机镜像_ 的概念。存储池应该是一个目录、一个网络文件系统或一个分区（这也包括 [LVM](<../zh-cn/LVM.html> "LVM")）。存储池可以在活动与不活动之间切换，可以为其分配存储空间。 

在 _系统_ 级别，默认被激活的存储池是 `/var/lib/libvirt/images/`；在用户 _会话_ 级别，`virt-manager` 将存储池创建在 `$XDG_DATA_HOME/images` 目录。 

列出活动和不活动的存储池的命令： 
    
    $ virsh pool-list --all
    
####  用 virsh 新建存储池

以下示例为 _添加_ 存储池、目录和 LVM 卷的方法： 
    
    $ virsh pool-define-as name type [source-host] [source-path] [source-dev] [source-name] [<target>] [--source-format format]
    $ virsh pool-define-as _poolname_ dir - - - - /home/_username_ /.local/libvirt/images
    $ virsh pool-define-as _poolname_ fs - -  _/dev/vg0/images_ - _mntpoint_
    
上述示例仅仅定义了存储池的信息，下面创建它： 
    
    $ virsh pool-build     _poolname_
    $ virsh pool-start     _poolname_
    $ virsh pool-autostart _poolname_
    
删除它的命令： 
    
    $ virsh pool-undefine  _poolname_
    
**提示：** 对于 LVM 存储池而言： 

  * 最佳实践是仅把一个卷组分配给一个存储池。
  * 请为存储池选择一个与 LVM 卷组不同的名字。否则当存储池被删除时，该卷组也将被删除。

####  用 virt-manager 新建存储池

首先，连接到虚拟运行环境（例如 QEMU/KVM 的系统/用户会话）。然后，右键点击一个**连接** ，选择**详情** ；切换到**存储** 选项卡，点击左下角的**+** ，按照向导操作。 

###  存储卷

存储池被创建之后，就可以在存储池中创建存储卷。 _如果你想新建一个域（虚拟机），那么这一步可以跳过，因为这一步可以在创建域的过程中完成。_

####  用 virsh 新建卷

新建卷，列出卷，变更卷大小，删除卷： 
    
    $ virsh vol-create-as      _poolname_ _volumename_ 10GiB --format aw|bochs|raw|qcow|qcow2|vmdk
    $ virsh vol-upload  --pool _poolname_ _volumename_ _volumepath_
    $ virsh vol-list           _poolname_
    $ virsh vol-resize  --pool _poolname_ _volumename_ 12GiB
    $ virsh vol-delete  --pool _poolname_ _volumename_
    $ virsh vol-dumpxml --pool _poolname_ _volumename_  # for details.
    
###  域

虚拟机被称作**“域”** 。如果你想在命令行下操作，使用 `virsh` 列出，创建，暂停，关闭……域。`virt-viewer` 可以用来查看使用 `virsh` 启动的域。域的创建通常以图形化的 `virt-manager` 或者命令行下的 `virt-install`（一个命令行工具，是 [virt-install](<https://archlinux.org/packages/?name=virt-install>)包 包的一部分）完成。 

创建新域通常需要安装媒介，例如存储池中的 `.iso` 文件或是直接从光驱安装。 

列出活动的和不活动的域： 
    
    # virsh list --all
    
**注意：**[SELinux](<../zh-cn/SELinux.html> "SELinux") 有内置策略使在 `/var/lib/libvirt/images/` 中的卷可以被访问。如果你使用 SELinux 并且在卷方面有问题，确保卷位于该目录，或是其它存储池的标记正常。

####  用 virt-install 新建域

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** `/usr/share/libosinfo` is not provided by any official packages, including [libosinfo](<https://archlinux.org/packages/?name=libosinfo>)包.（在 [Talk:Libvirt#Where_is_'/usr/share/libosinfo/db/oses/os.xml'？](</wzh/index.php?title=Talk:Libvirt&action=edit&redlink=1> "Talk:Libvirt（页面不存在）") 中讨论）

对于很详细的域（虚拟机）配置，可以[#用 virt-manager 新建域](<#%E7%94%A8_virt-manager_%E6%96%B0%E5%BB%BA%E5%9F%9F>)更简单地完成。但是，基础配置同样可以用 `virt-install` 完成并且同样顺利运行。最小配置包括 `--name`，`--memory`，存储（`--disk`，`--filesystem` 或 `--nodisks`）和安装介质（通常来说是 `.iso` 文件或 CD）。查看 [virt-install(1)](<https://man.archlinux.org/man/virt-install.1>) 得到未列出的选项和更多的详情。 

安装 Arch Linux（创建了 2 GiB qcow2 格式卷；用户网络）： 
    
    $ virt-install  \
      --name arch-linux_testing \
      --memory 1024             \
      --vcpus=2,maxvcpus=4      \
      --cpu host                \
      --cdrom $HOME/Downloads/arch-linux_install.iso \
      --disk size=2,format=qcow2  \
      --network user            \
      --virt-type kvm
    
Fedora testing (Xen, 非默认池,无默认控制台): 
    
    $ virt-install  \
      --connect xen:///     \
      --name fedora-testing \
      --memory 2048         \
      --vcpus=2             \
      --cpu=host            \
      --cdrom /tmp/fedora20_x84-64.iso      \
      --os-type=linux --os-variant=fedora20 \
      --disk pool=testing,size=4            \
      --network bridge=br0                  \
      --graphics=vnc                        \
      --noautoconsole
    $ virt-viewer --connect xen:/// fedora-testing
    
Windows: 
    
    $ virt-install \
      --name=windows7           \
      --memory 2048             \
      --cdrom /dev/sr0          \
      --os-variant=win7         \
      --disk /mnt/storage/domains/windows7.qcow2,size=20GiB \
      --network network=vm-net  \
      --graphics spice
    
**提示：** 运行 `osinfo-query --fields=name,short-id,version os` 来获得 `--os-variant` 的参数，这可以帮助定制域的一些规格。然而 `--memory` 和 `--disk` 是必须被输入的。如果需要查看这些规格，可以看看 `/usr/share/libosinfo/db/oses/_os_.xml`（译注：此处可能已过时）。在安装后，推荐安装 [Spice Guest Tools](<https://www.spice-space.org/download.html>)，其中包括 [VirtIO 驱动](<https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Virtualization_Host_Configuration_and_Guest_Installation_Guide/form-Virtualization_Host_Configuration_and_Guest_Installation_Guide-Para_virtualized_drivers-Mounting_the_image_with_virt_manager.html>)。Windows 的 VirtIO 网络驱动可通过 [virtio-win](<https://aur.archlinux.org/packages/virtio-win/>)AUR 获得。要使用 VirtIO，需要在虚拟机 `.xml` 配置中使用 `<model type='virtio' />`。更多的信息可以参考 [QEMU](<../zh-cn/QEMU.html#Preparing_a_Windows_guest> "QEMU") 页面.

导入现有的卷： 
    
    $ virt-install  \
      --name demo  \
      --memory 512 \
      --disk /home/user/VMs/mydisk.img \
      --import
    
####  用 virt-manager 新建域

首先，连接到虚拟运行环境（例如 QEMU/KVM _system_ 或用户 _session_ ，在连接上右击并选择 _新建_ ，然后跟随向导完成。 

  * 在**第四步** 中取消选中**立即分配全部虚拟磁盘空间** 会加快创建过程并节省实际虚拟磁盘空间占用；**然而** ，这将导致将来花费额外的磁盘整理时间。
  * 在**第五步** 中打开**高级选项** 并确认**虚拟化类型** 设为 **kvm** （这通常是首选模式）。如果要求附加的硬件配置，选中**安装前定制** 选项。

####  管理域

启动域： 
    
    $ virsh start _domain_
    $ virt-viewer --connect qemu:///session _domain_
    
正常关闭域；强制关闭域: 
    
    $ virsh shutdown _domain_
    $ virsh destroy  _domain_
    
在 libvirtd 启动时自动启动域: 
    
    $ virsh autostart _domain_
    $ virsh autostart _domain_ --disable
    
在宿主机关闭时自动关闭域: 

    通过使用 `libvirt-guests.service` Systemd 服务，运行中的域可以在宿主机关闭时自动挂起/关闭。同时这个服务还可以让挂起/休眠的域在宿主机启动的时候自动恢复。可查看 [libvirt-guests(8)](<https://man.archlinux.org/man/libvirt-guests.8>) 了解相关选项。

编辑一个域的 XML 配置： 
    
    $ virsh edit _domain_
    
参考 libvirt 维基的 [XML 格式](<https://libvirt.org/format.html>)一节了解关于 XML 配置文件的信息。 

**注意：** 直接被 QEMU 启动的虚拟机不被 libvirt 管理。

###  网络

[这里](<https://jamielinux.com/docs/libvirt-networking-handbook/>)是有关 libvirt 网络的的概述。 

可将以下四种网络连接到域： 

  * bridge——这是一个虚拟设备，它通过一个物理接口直接共享数据。使用场景为：宿主机有 _静态_ 网络、不需与其它域连接、要占用全部进出流量，并且域运行于 _系统_ 层级。网桥必须要在 libvirt 外配置，详细操作可参考[网桥](<../zh-cn/Network_bridge.html> "Network bridge")。网桥创建后，需要将它指定到相应客户机的 `.xml` 配置文件中。
  * network——这是一个虚拟网络，它可以与其它虚拟机共用。Libvirt 提供多种虚拟网络模式，例如 NAT（Network address translation，网络地址转换）模式，路由模式和隔离模式。使用场景为：宿主机有 _动态_ 网络（例如：NetworkManager）或使用无线网络。
  * macvtap——直接连接到宿主机的一个物理网络接口。相较 _桥接_ 更加简单，代价是宿主机无法通过该接口与域通信。Libvirt 可以很方便地配置该类网络。
  * user——本地网络，仅用于用户 _会话_ 。

绝大多数用户都可以通过 `virsh` 的各种可选项创建具有各种功能的网络，一般来说通过 GUI 程序（像 `virt-manager` 之类）更方便，也可以按 [#用 virt-install 新建域](<#%E7%94%A8_virt-install_%E6%96%B0%E5%BB%BA%E5%9F%9F>)所述实现。 

**注意：**

  * libvirt 通过 [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包 处理 DHCP 和 DNS 请求，为每个虚拟网络创建一个实例。它也会为特定的路由添加 iptables 规则并启用 `ip_forward` 内核参数。这也意味着宿主机上无需预先运行 dnsmasq（并可能干扰到 libvirt 的 dnsmasq 实例）。
  * 如果无法启动默认网络，请确保已安装 [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包 和 [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包，并在 [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `libvirtd.service` 前先 [启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `iptables.service`。

**注意：**

如果你用了 [iptables](<https://archlinux.org/packages/?name=iptables>)包 而不是 [nftables](<https://archlinux.org/packages/?name=nftables>)包, 那么有必要在配置文件`/etc/libvirt/network.conf`中相应地指定它。 

**示例** : 

  1. default: #firewall_backend = "nftables"

firewall_backend = "iptables" 

通过以下命令获取虚拟机的 IP（假设它连接到 `_default_` 网络并通过 DHCP 获取 IP）： 
    
    $ virsh net-dhcp-leases default
    
如果 VM 上运行有 `_qemu-guest-agent_`： 
    
    $ virsh domifaddr --source agent $vm
    
将 `_$vm_` 替换为实际的虚拟机名称（或域 ID）。 

####  管理并修改网络

修改网络前建议先阅读 libvirt 维基的[用于虚拟网络的基本命令行用法](<https://wiki.libvirt.org/VirtualNetworking.html#basic-command-line-usage-for-virtual-networks>)一节。另外也建议通过 [libvirt 网络维基](<https://wiki.libvirt.org/page/VirtualNetworking>)了解用法。 

#### IPv6

当通过任何配置工具试图添加 IPv6 地址时，你可能会遇到这样的错误： 
    
    Check the host setup: enabling IPv6 forwarding with RA routes without accept_ra set to 2 is likely to cause routes loss. Interfaces to look at: _eth0_
    
要修复这个问题，运行如下命令（将 `eth0` 改为你的物理接口的名称），并重新启动系统。 
    
    # sysctl net.ipv6.conf.eth0.accept_ra=2
    
#### Macvtap

要创建 macvtap 网络，先创建该文件： 
    
    macvtap.xml
    
    <network>
      <name>macvtap-net</name>
      <forward mode='bridge'>
        <interface dev='eth0'/>
      </forward>
    </network>

然后定义并启用网络： 
    
    $ virsh net-define macvtap.xml
    $ virsh net-autostart macvtap-net
    $ virsh net-start macvtap-net
    
现在已创建好 `macvtap-net` 网络并已持久化，它通过 `eth0` 桥接到外部网络。 

**警告：** 宿主机无法通过该网络与域通信。宿主机的网络不受影响，域也可以与该网络的其它机子通信，但不能与宿主机本身通信。可参考 [libvirt 维基](<https://wiki.libvirt.org/TroubleshootMacvtapHostFail.html>)绕过该限制。

####  nftables 防火墙

当使用 NAT 类型网络配合简单的限制性 nftables 防火墙（例如默认配置）时，可能需要允许以下流量： 

虚拟网络接口（默认配置在此丢弃数据包）的转发流量 

来自虚拟网络接口的 DNS/DHCP 请求（供 DHCP 客户端与宿主机通信） 

以 `virbr0` 作为 libvirt 桥接接口的简化配置示例： 
    
    /etc/nftables.conf
    
    # ...
    table inet filter {
      chain input {
        type filter hook input priority filter
        policy drop
        # ...
        iifname virbr0 udp dport {53, 67} accept comment "allow VM dhcp/dns requests to host"
        # ...
      }
    
      chain forward {
        type filter hook forward priority filter
        policy drop
        
        iifname virbr0 accept
        oifname virbr0 accept
      }
    }
    
###  快照

快照保存某一时刻域的磁盘、内存和设备状态以供将来使用。快照有很多用处，例如在进行可能的破坏性操作时保存一份干净的域状态。快照使用唯一名称进行标识。 

快照保存在卷之中，卷必须为 qcow2 或 raw 格式。快照使用增量存储，所以并不会占用很多空间。 

####  创建快照

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** Some of this data appears to be dated. (在[Talk:Libvirt](<../zh-cn/Talk:Libvirt.html>)讨论)

Once a snapshot is taken it is saved as a new block device and the original snapshot is taken offline. Snapshots can be chosen from and also merged into another (even without shutting down the domain). 

Print a running domain's volumes (running domains can be printed with `virsh list`): 
    
    # virsh domblklist _domain_
    
     Target     Source
     ------------------------------------------------
     vda        /vms/domain.img
    
To see a volume's physical properties: 
    
    # qemu-img info /vms/domain.img
    
     image: /vms/domain.img
     file format: qcow2
     virtual size: 50G (53687091200 bytes)
     disk size: 2.1G
     cluster_size: 65536
    
Create a disk-only snapshot (the option `--atomic` will prevent the volume from being modified if snapshot creation fails): 
    
    # virsh snapshot-create-as _domain_ snapshot1 --disk-only --atomic
    
List snapshots: 
    
    # virsh snapshot-list _domain_
    
     Name                 Creation Time             State
     ------------------------------------------------------------
     snapshot1           2012-10-21 17:12:57 -0700 disk-snapshot
    
One can then copy the original image with `cp --sparse=true` or `rsync -S` and then merge the original back into snapshot: 
    
    # virsh blockpull --domain _domain_ --path /vms/_domain_.snapshot1
    
`domain.snapshot1` becomes a new volume. After this is done the original volume (`domain.img` and snapshot metadata can be deleted. The `virsh blockcommit` would work opposite to `blockpull` but it seems to be currently under development (including `snapshot-revert feature`, scheduled to be released sometime next year. 

###  其它管理操作

连接到非默认的虚拟运行环境： 
    
    $ virsh --connect xen:///
    virsh # uri
    xen:///
    
通过 SSH 连接到 QEMU 虚拟运行环境，并且以相同方式登录： 
    
    $ virsh --connect qemu+ssh://_username_ @_host_ /system
    $ LIBVIRT_DEBUG=1 virsh --connect qemu+ssh://_username_ @_host_ /system
    
通过 SSH 连接到一个图形控制台： 
    
    $ virt-viewer  --connect qemu+ssh://_username_ @_host_ /system _domain_
    $ virt-manager --connect qemu+ssh://_username_ @_host_ /system _domain_
    
**注意：** 如果你在连接 RHEL 服务器（或其他不是 Arch 的服务器）时出现问题，可尝试这里提到的两个方案：[FS#30748](<https://bugs.archlinux.org/task/30748>) 和 [FS#22068](<https://bugs.archlinux.org/task/22068>)。

连接到 VirtualBox（ _libvirt 对 VirtualBox 的支持尚不稳定，可能会导致 libvirtd 崩溃_ ）: 
    
    $ virsh --connect vbox:///system
    
网络配置: 
    
    $ virsh -c qemu:///system net-list --all
    $ virsh -c qemu:///system net-dumpxml default
    
## Hooks

钩子 (Hooks) 是指在启动和运行 libvirt 守护进程时，由不同事件触发的脚本。 它们可以用来执行启动访客机所需的准备命令，例如设置网络或预留内存。 

libvirt 提供以下类型的钩子： 

  * daemon - 触发时机：启动、关闭、重新加载
  * qemu - 触发时机：准备、启动、已启动、已停止、释放、迁移、恢复、重新连接、附加
  * lxc - 触发时机：准备、启动、已启动、已停止、释放、重新连接
  * libxl - 触发时机：准备、启动、已启动、已停止、释放、迁移、重新连接
  * network - 触发时机：启动、已启动、已停止、端口创建、更新、端口删除

有关每个钩子和触发器的详细信息，请参见 [libvirt 文档](<https://www.libvirt.org/hooks.html>)。 

###  新建一个 hook

钩子由位于 `/etc/libvirt/hooks` 的脚本表示。如果该文件夹不存在，则需要创建它。 

每个钩子由该文件夹中同名的脚本（例如 `/etc/libvirt/hooks/qemu`）或子文件夹（例如 `/etc/libvirt/hooks/qemu.d/`）表示。后者可以包含不同的脚本，这些脚本在触发点都会运行。脚本像其他任何脚本一样运行，因此需要以要使用的命令解释器的声明开头（例如 `#!/bin/bash`）并[可由 libvirt 用户执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。 

每当碰到触发点时，脚本就会运行。例如，daemon 脚本在系统的启动/停止周期中至少运行两次，一次在启动时，一次在关闭时。要仅在给定点运行命令，必须在脚本中实现条件。为此，libvirt 传递可用于识别当前触发条件的参数。 

根据 libvirt 文档，这些参数定义如下： 

  * 参数 1：操作涉及的对象的名称
  * 参数 2：正在执行的操作的名称
  * 参数 3：如果要命名子操作则使用
  * 参数 4：如有需要，则为额外参数 如果其中一个参数不适用，则传递一个连字符。

**注意：** 如果创建脚本后钩子不起作用，请尝试重启 libvirt 守护进程。根据新的模块化 daemon 架构，需重启的具体 daemon 取决于对应的 hook（例如针对 `qemu` hook 需操作 `virtqemud`）。

####  示例

To run an command every time you start an qemu guest, before any resources are allocated, you can use the qemu hook. At this point, libvirt runs the hooks like this: `/etc/libvirt/hooks/qemu <guest_name> prepare begin -` The script for this could like this: 
    
    /etc/libvirt/hooks/qemu
    
    #!/bin/bash
    guest_name="$1"
    libvirt_task="$2"
    if [ "$libvirt_task" = "prepare" ]; then
    	<run some important code here>
    fi

If the guest is stopped, the same script would be run, but this time the daemon would start the command like this: `/etc/libvirt/hooks/qemu <guest_name> stopped end -`

##  宿主机与虚拟机间共享数据

### Virtio-FS

**注意：** Virtio-FS is not supported in QEMU/KVM user sessions.

The description here will use hugepages to enable the usage of shared folders. [Sharing files with Virtio-FS](<https://libvirt.org/kbase/virtiofs.html>) lists an overview of the supported options to enable filesharing with the guest. 

First you need to [enable hugepages](<../zh-cn/KVM.html#Enabling_huge_pages> "KVM") which are used by the virtual machine: 
    
    /etc/sysctl.d/40-hugepage.conf
    
    vm.nr_hugepages = _nr_hugepages_

To determine the number of hugepages needed check the size of the hugepages: 
    
    $ grep Hugepagesize /proc/meminfo
    
The number of hugepages is _memory size of virtual machine / Hugepagesize_. Add to this value some additional pages. You have to reboot after this step, so that the hugepages are allocated. 

Now you have to prepare the configuration of the virtual machine: 
    
    # virsh edit _name_of_virtual_machine_
    
    <domain>
    ...
      <memoryBacking>
        <hugepages/>
      </memoryBacking>
    ...
      <cpu ...>
        <numa>
          <cell memory='memory size of virtual machine' unit='KiB' memAccess='shared'/>
        </numa>
      </cpu>
    ...
      <devices>
        ...
        <filesystem type='mount' accessmode='passthrough'>
          <driver type='virtiofs'/>
          <source dir='path to source folder on host'/>
          <target dir='mount_tag'/>
        </filesystem>
        ...
      </devices>
    </domain>
    
It is necessary to add the NUMA definition so that the memory access can be declared as shared. id and cpus values for NUMA will be inserted by virsh. 

It should now be possible to mount the folder in the shared machine: 
    
    # mount -t virtiofs _mount_tag_ /mnt/mount/path
    
Add the following [fstab](<../zh-cn/Fstab.html> "Fstab") entry to mount the folder automatically at boot: 
    
    /etc/fstab
    
    ...
    _mount_tag_ /mnt/mount/path virtiofs rw,noatime,_netdev 0 0

### 9p

File system directories can be shared using the [9P protocol](<https://en.wikipedia.org/wiki/9P_\(protocol\)> "wikipedia:9P \(protocol\)"). Details are available in [QEMU's documentation of 9psetup](<https://wiki.qemu.org/Documentation/9psetup>). 

Configure the virtual machine as follows: 
    
    <domain>
    ...
      <devices>
        ...
        <filesystem type="mount" accessmode="mapped">
          
          <target dir="_mount_tag_ "/>
        </filesystem>
      </devices>
    </domain>

Boot the guest and [mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") the shared directory from it using: 
    
    # mount -t 9p -o trans=virtio,version=9p2000.L _mount_tag_ _/path/to/mount_point/on/guest_
    
See <https://docs.kernel.org/filesystems/9p.html> for more mount options. 

To mount it at boot, add it to the guest's [fstab](<../zh-cn/Fstab.html> "Fstab"): 
    
    /etc/fstab
    
    ...
    _mount_tag_	_/path/to/mount_point/on/guest_	9p	trans=virtio,version=9p2000.L	0 0

The module for the 9p transport (i.e. `9pnet_virtio` for `trans=virtio`) will not be automatically loaded, so mounting the file system from `/etc/fstab` will fail and you will encounter an error like `9pnet: Could not find request transport: virtio`. The solution is to [preload the module during boot](<../zh-cn/Kernel_module.html#Automatic_module_loading> "Kernel module"): 
    
    /etc/modules-load.d/9pnet_virtio.conf
    
    9pnet_virtio
    
###  Samba / SMB

An other easy way to share data between guest and host is to use the smb protocol. While performance and latency may not be as good as in the other described ways, its sufficient for simple tasks like transfering simple files like images or documents from and to the guest. 

The smb server can be set up directly on either the host, or the guest, for example using [Samba](<../zh-cn/Samba.html#Server> "Samba"), eliminating the need for a dedicated file server. Windows guests have the ability to create smb shares included right after installation ([Microsoft Supportpage](<https://support.microsoft.com/en-us/windows/file-sharing-over-a-network-in-windows-10-b58704b2-f53a-4b82-7bc1-80f9994725bf>)). 

One possible way to access the share under linux (either from the host, or from the guest, depending, where you have installed your server) is to create an entry in your fstab. The [samba](<https://archlinux.org/packages/?name=samba>)包 package is required. 
    
    /etc/fstab
    
    #Accessing a samba share on my vm from the host
    //my_vm/my_share /home/archuser/my_vm cifs _netdev,noauto,nofail,user,credentials=/home/archuser/.config/my_vm.key,gid=1000,uid=984 0 0

`_netdev,noauto,nofail` ensures that the share is only mounted when needed without causing issues if the vm is not booted. `user,credentials=/home/user/.config/my_vm.key,gid=1000,uid=984` gives you the ability to mount the share on the fly while first accessing it, [without needing a password](<../zh-cn/Samba.html#Storing_share_passwords> "Samba"). 

##  UEFI 支持

Libvirt 可以通过 QEMU 和 [OVMF](<https://github.com/tianocore/edk2>) 来支持 UEFI 虚拟机。 

安装 [edk2-ovmf](<https://archlinux.org/packages/?name=edk2-ovmf>)包。 

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `libvirtd`。 

你现在就可以创建 UEFI 虚拟机了。通过 [virt-manager](<https://archlinux.org/packages/?name=virt-manager>)包 创建一台虚拟机，在到达 _新建虚拟机_ 向导的最后一页时，进行如下操作： 

  * 勾选**在安装前自定义配置** ，之后点击**完成** 。
  * 在**概况** 屏幕, 将固件改为：

  1.      * _UEFI x86_64: /usr/share/edk2/x64/OVMF_CODE.4m.fd_ ：无安全启动支持的 x64 UEFI，
     * _UEFI x86_64: /usr/share/edk2/x64/OVMF_CODE.secboot.4m.fd_ ：带安全启动支持的 x64 UEFI（无预置证书）。
  2. 点击 _应用_ 。

  * 点击**开始安装**

参考 [Fedora:Using UEFI with QEMU](<https://fedoraproject.org/wiki/Using_UEFI_with_QEMU> "fedora:Using UEFI with QEMU") 获得更多信息。 

##  小技巧

###  在虚拟机中使用整个物理磁盘设备

若宿主机存在包含其他操作系统（如 Windows）的独立物理磁盘，可将其配置为虚拟机中的虚拟磁盘进行启动。由于采用原始磁盘访问，虚拟机内磁盘性能接近原生。 

####  Windows 虚拟机启动前提条件

在尝试启动前，**必须** 在该磁盘的 Windows 系统中安装 [virtio 驱动](<https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/>)： 

  * **Windows 7** ：使用版本 [0.1.173-4](<https://askubuntu.com/questions/1310440/using-virtio-win-drivers-with-win7-sp1-x64>)。新版 virtio 中的部分驱动可通过设备管理器手动安装
  * **Windows 10** ：支持最新 virtio 版本

#####  配置 Windows 磁盘接口驱动

若启动时遭遇 `0x0000007B` 蓝屏错误，表示 Windows 在早期启动阶段无法访问磁盘（因相关接口驱动未加载或设置为手动启动）。需[修改注册表强制驱动随系统启动](<https://superuser.com/a/1032769>)： 

  1. 打开注册表编辑器，定位至 `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services`
  2. 对以下键值（如存在）执行操作： `aliide, amdide, atapi, cmdide, iastor, iastorV, intelide, LSI_SAS, msahci, pciide, viaide`
  3. 将每个键中的 **Start** 值改为 **0**
  4. 若使用 PCIe NVMe 磁盘，需同样启用对应驱动

####  获取磁盘唯一标识路径

执行 `ls /dev/disk/by-id/` 查看磁盘 ID（例如，得到 `ata-TS512GMTS930L_C199211383`则 `/dev/disk/by-id/ata-TS512GMTS930L_C199211383` 为磁盘唯一标识） 

####  通过 QEMU CLI 添加磁盘

在 QEMU 命令行中添加参数：`-drive file=/dev/disk/by-id/ata-TS512GMTS930L_C199211383,format=raw,media=disk`

（替换 `file=` 后的路径为实际磁盘路径） 

####  通过 libvirt XML 添加磁盘

在 QEMU 命令行中添加参数： 
    
    $ virsh edit _vmname_
    
    ...
        <disk type="block" device="disk">
          <driver name="qemu" type="raw" cache="none" io="native"/>
          <source dev="/dev/disk/by-id/ata-TS512GMTS930L_C199211383"/>
          <target dev="sda" bus="sata"/>
          <address type="drive" controller="0" bus="0" target="0" unit="0"/>
        </disk>
    ...
    
替换 `file=` 后的路径为实际磁盘路径 

####  通过 virt-manager 添加磁盘

  * **新建虚拟机** ：选择 "导入现有磁盘"，粘贴磁盘唯一路径
  * **已有虚拟机** ：添加设备 → 存储 → 选择/创建自定义存储 → 粘贴磁盘路径

###  Python 连接代码

[libvirt-python](<https://archlinux.org/packages/?name=libvirt-python>)包 在 `/usr/lib/python3.x/site-packages/libvirt.py` 提供了一个 Python API。 

常用例子在 `/usr/share/doc/libvirt-python-_your_libvirt_version_ /examples/` 给出。 

一个使用 [qemu-desktop](<https://archlinux.org/packages/?name=qemu-desktop>)包 和 [openssh](<https://archlinux.org/packages/?name=openssh>)包 的例子（非官方）: 
    
    #! /usr/bin/env python3
    import socket
    import sys
    import libvirt
    
    conn = libvirt.open("qemu+ssh://xxx/system")
    print("Trying to find node on xxx")
    domains = conn.listDomainsID()
    for domainID in domains:
        domConnect = conn.lookupByID(domainID)
        if domConnect.name() == 'xxx-node':
            print("Found shared node on xxx with ID {}".format(domainID))
            domServ = domConnect
            break
    
###  先进格式化 4K 原生硬盘

To turn a disk into an [Advanced Format](<../zh-cn/Advanced_Format.html> "Advanced Format") 4Kn disk, both its physical and logical sector size needs to be set to 4 KiB. For virtio-blk and virtio-scsi this can be done by setting the `logical_block_size` and `physical_block_size` options with the [<blockio> element](<https://libvirt.org/formatdomain.html#hard-drives-floppy-disks-cdroms>). For example: 
    
    # virsh edit _name_of_virtual_machine_
    
    <domain>
      ...
      <devices>
        ...
        <disk type='file' device='disk'>
          ..
          **< blockio logical_block_size='4096' physical_block_size='4096'/>**
        </disk>
        ...
      </devices>
    </domain>

###  控制 QEMU

Libvirt is capable of passing on QEMU command line arguments to the underlying QEMU instance running the VM. This functionality is highly useful when libvirt does not provide [QEMU features](<../zh-cn/QEMU.html> "QEMU") (yet). For examples, see the entire [Intel GVT-g](<../zh-cn/Intel_GVT-g.html> "Intel GVT-g") article. 

#### modify VM XML schema for QEMU

This serves to enable QEMU-specific elements. Change 
    
    $ virsh edit _vmname_
    
    <domain type='kvm'>
    
to 
    
    $ virsh edit _vmname_
    
    <domain xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0' type='kvm'>
    
####  QEMU 命令行参数

In libvirt, QEMU command line arguments separated by whitespaces need to be provided separately. 

The correct location to insert them is at the end of the `<domain>` element, i. e. right above the closing `</domain>` tag. 
    
    -display gtk,gl=es,zoom-to-fit=off
    
Becomes 
    
    $ virsh edit _vmname_
    
    ...
      </devices>
      <qemu:commandline>
        <qemu:arg value="-display"/>
        <qemu:arg value="gtk,gl=es,zoom-to-fit=off"/>
      </qemu:commandline>
    </domain>
    
##  排障

###  系统实例下的 PulseAudio

PulseAudio 守护进程通常在你的普通用户下运行，并且只接受来自相同用户的连接。然而 libvirt 默认使用 root 运行 QEMU。为了让 QEMU 在普通用户下运行，编辑 `/etc/libvirt/qemu.conf` 并将 `user` 设置为你的用户名。 
    
    user = "dave"
    
你同样需要告诉 QEMU 使用 PulseAudio 后端并识别要连接的服务器。使用 `virsh edit` 将如下内容添加到你的域配置中： 
    
      <audio id="1" type="pulseaudio" serverName="/run/user/1000/pulse/native">
        <input latency="20000"/>
        <output latency="20000"/>
      </audio>
    
`1000` 是你的用户 ID，如有必要可修改。 

可省略延迟参数（单位：微秒），但使用默认值可能导致音频出现 crackling（爆音）。 

####  Hypervisor CPU 使用率过高

virt-manager 生成的默认虚拟机配置可能导致 QEMU 进程占用较高 CPU（10-20%）。若以无界面模式运行虚拟机，建议移除非必要设备 

### Virtual machine cannot be un-paused on virt-manager

If you are using a disk image format such as [qcow2](<../zh-cn/QEMU.html#Creating_a_hard_disk_image> "QEMU") which has a specified virtual capacity, but only stores what is needed, then you need to have space on the host partition for the image to grow. If you see I/O related errors when attempting to start the VM, it's possible that the host partition holding the virtual disk image is full. You can run `df -h` on the host to verify how much free space is available. 

If this is the case, see [System maintenance#Clean the filesystem](<../zh-cn/System_maintenance.html#Clean_the_filesystem> "System maintenance") for ways to free up space. 

### Redirect USB Device is greyed out in virt-manager

If the _Redirect USB Device_ menu item is greyed out, check that the following hardware is configured for the VM: 

  * A USB Controller.
  * One or more USB Redirectors.

### Error starting domain: Requested operation is not valid

When you try to open a virtual machine this error may pop up. This is because when you try to open a existing virtual machine libvirt tries to search for the default network which is not available. To make it available you have to autostart your network interface so that whenever your restart your computer your network interface is always active. See [libvirt networking page](<https://wiki.libvirt.org/page/Networking>). 

Look at the name of your network interface with the following command: 
    
    # virsh net-list --all
    
To autostart your network interface: 
    
    # virsh net-autostart _name_of_the_network_
    
To start your network interface: 
    
    # virsh net-start _name_of_the_network_
    
###  Virt Manager Error 'Virt Manager doesn't have search permissions'

Ensure the folder containing your virtual machine files and installation ISO are owned by the `libvirt-qemu` group 
    
    $ sudo chown -R $USER:libvirt-qemu /path/to/virtual/machine
    
###  启动域时错误：请求的操作无效：网络 'default' 未激活

若默认网络因故处于未激活状态，所有配置使用该网络的虚拟机将无法启动。初步解决措施可尝试通过 virsh 手动启动网络： 

`# virsh net-start default`

若问题仍未解决，请参考[网络故障排查指南](<https://www.xmodulo.com/network-default-is-not-active.html>)

##  参阅

  * [libvirt 网站](<https://libvirt.org/drvqemu.html>)
  * [Red Hat 虚拟化部署和管理指南](<https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Virtualization_Deployment_and_Administration_Guide/index.html>)
  * [Red Hat 虚拟化调优指南](<https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Virtualization_Tuning_and_Optimization_Guide/index.html>)
  * [Slackware KVM and libvirt](<https://docs.slackware.com/howtos:general_admin:kvm_libvirt>)
  * [IBM KVM](<https://www-01.ibm.com/support/knowledgecenter/linuxonibm/liaat/liaatkvm.htm>)
  * [libvirt 网络手册](<https://jamielinux.com/docs/libvirt-networking-handbook/>)
