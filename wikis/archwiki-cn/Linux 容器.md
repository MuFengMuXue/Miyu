  
**翻译状态：**

  * 本文（或部分内容）译自 [Linux Containers](<https://wiki.archlinux.org/title/Linux_Containers> "arch:Linux Containers")，最近一次同步于 2025-02-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Linux_Containers?diff=0&oldid=824982>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Linux_Containers_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [/使用 VPN](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8/%E4%BD%BF%E7%94%A8_VPN.html> "Linux 容器/使用 VPN")
  * [Cgroups](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html> "Cgroups")
  * [Docker](<../zh-cn/Docker.html> "Docker")
  * [Incus](<../zh-cn/Incus.html> "Incus")
  * [LXD](</wzh/index.php?title=LXD&action=edit&redlink=1> "LXD（页面不存在）")
  * [Podman](<../zh-cn/Podman.html> "Podman")
  * [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")

[Linux 容器](<https://linuxcontainers.org/>) (LXC) 是一种在单个宿主机（LXC host）运行多个隔离的 Linux 系统（容器）的操作系统级虚拟化方法。它并不提供虚拟机，而是提供了一个具有独立 CPU、内存、块 I/O、网络等空间和资源控制环境的虚拟环境。这是通过 LXC 宿主机上 Linux 内核的 [namespaces](<https://en.wikipedia.org/wiki/Linux_namespaces> "wikipedia:Linux namespaces") 和 [cgroups](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html> "Cgroups") 特性实现的。它类似于 chroot ，但是具有更好的隔离性。 

[LXD](</wzh/index.php?title=LXD&action=edit&redlink=1> "LXD（页面不存在）") 可以被用做 LXC 的管理器，本页面则涉及直接使用 LXC 。 

使用容器的替代方法包括 [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") 和 [Docker](<../zh-cn/Docker.html> "Docker") 。 

##  特权容器或非特权容器

LXC 支持两种类型的容器： _特权_ 和 _非特权_ 。 

一般来说， _特权_ 容器被认为是**不安全** 的[[1]](<https://linuxcontainers.org/lxc/security/>)。 

运行 _非特权_ 容器比运行 _特权_ 容器[更安全](<https://www.stgraber.org/2014/01/17/lxc-1-0-unprivileged-containers>)，因为 _非特权_ 容器在设计上具有更高程度的隔离性。其中的关键在于容器内的 root UID 被映射为宿主机上的非 root UID ，这使得容器内部的攻击更难以对宿主机系统施加影响。换句话说，如果攻击者设法逃离容器，它们会发现自己在宿主机上被限制或没有权限。 

Arch 的 [linux](<https://archlinux.org/packages/?name=linux>)包 、 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 和 [linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 内核软件包现在提供了 _非特权_ 容器的开箱即用支持。 类似的，对于 [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 软件包， _非特权_ 容器仅适用于系统管理员；对于普通用户，默认情况下禁用了 namespace ，因此需要进行额外的内核配置更改。 

本文包含了用户运行任何类型容器所需的信息，但是为了运行 _非特权_ 容器可能需要[额外的操作](<#%E5%90%AF%E7%94%A8%E9%9D%9E%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8%E6%94%AF%E6%8C%81%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89>)。 

###  一个例子说明非特权容器

为了说明 UID 映射的作用，考虑以下来自运行中的 _非特权_ 容器的输出。在 `ps` 命令的输出中，我们可以看到容器化的进程由容器化的 root 用户所有： 
    
    [root@unprivileged_container /]# ps -ef | head -n 5
    
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 17:49 ?        00:00:00 /sbin/init
    root        14     1  0 17:49 ?        00:00:00 /usr/lib/systemd/systemd-journald
    dbus        25     1  0 17:49 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
    systemd+    26     1  0 17:49 ?        00:00:00 /usr/lib/systemd/systemd-networkd

然而在宿主机中，可以看到这些容器化的 root 进程事实上显示为以映射用户（ID>99999）的身份运行，而不是宿主机上真实的 root 用户： 
    
    [root@host /]# lxc-info -Ssip --name sandbox
    
    State:          RUNNING
    PID:            26204
    CPU use:        10.51 seconds
    BlkIO use:      244.00 KiB
    Memory use:     13.09 MiB
    KMem use:       7.21 MiB
    
    [root@host /]# ps -ef | grep 26204 | head -n 5
    
    UID        PID  PPID  C STIME TTY          TIME CMD
    100000   26204 26200  0 12:49 ?        00:00:00 /sbin/init
    100000   26256 26204  0 12:49 ?        00:00:00 /usr/lib/systemd/systemd-journald
    100081   26282 26204  0 12:49 ?        00:00:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
    100000   26284 26204  0 12:49 ?        00:00:00 /usr/lib/systemd/systemd-logind

##  安装

###  需要的软件

安装 [lxc](<https://archlinux.org/packages/?name=lxc>)包 和 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 使宿主机系统能够运行特权 lxc 容器。 

####  启用非特权容器支持（可选）

更改 `/etc/lxc/default.conf` 使其包含下面的配置行： 
    
    lxc.idmap = u 0 100000 65536
    lxc.idmap = g 0 100000 65536
    
创建 `/etc/subuid` 和 `/etc/subgid` 为每个可以运行容器的用户配置容器化 UID/GID 对的映射。下面的示例仅针对 root 用户（和 [systemd](<../zh-cn/Systemd.html> "Systemd") 系统单元）： 
    
    /etc/subuid
    
    root:100000:65536
    
    /etc/subgid
    
    root:100000:65536
    
此外，只有在提前委派一个 [cgroup](</wzh/index.php?title=Cgroup&action=edit&redlink=1> "Cgroup（页面不存在）") 时，以非 root 用户运行非特权容器才有效（ cgroup2 委派模型强制执行此限制，而不是 liblxc ）。使用以下 _systemd_ 命令来委派 cgroup （根据 [LXC - Getting started: Creating unprivileged containers as a user](<https://linuxcontainers.org/lxc/getting-started/#creating-unprivileged-containers-as-a-user>)）： 
    
    $ systemd-run --unit=_myshell_ --user --scope -p "Delegate=yes" lxc-start _container_name_
    
同样的方式也适用于其他 lxc 命令。 

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[cgroups#User delegation](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html#User_delegation> "Cgroups")。**

**附注：** 这不是 Linux 容器特有的问题，避免重复。（在 [Talk:Linux 容器](<../zh-cn/Talk:Linux_%E5%AE%B9%E5%99%A8.html>) 中讨论）

或者，您可以通过创建一个 _systemd_ 单元来委派 _非特权_ [cgroup](</wzh/index.php?title=Cgroup&action=edit&redlink=1> "Cgroup（页面不存在）") （根据 [Rootless Containers: Enabling CPU, CPUSET, and I/O delegation](<https://rootlesscontaine.rs/getting-started/common/cgroup2/#enabling-cpu-cpuset-and-io-delegation>) ）： 
    
    /etc/systemd/system/user@.service.d/delegate.conf
    
    [Service]
    Delegate=cpu cpuset io memory pids

#####  linux-hardened 和自定义内核上的非特权容器

希望在 [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 或自定义内核上运行 _非特权_ 容器的用户需要完成几个额外的配置步骤。 

首先，内核需要支持用户命名空间（具有 `CONFIG_USER_NS` 配置）。所有 Arch Linux 内核都有 `CONFIG_USER_NS` 的支持。然而，基于更一般的安全考虑， [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 内核仅为 _root_ 用户启用了用户命名空间。这里有两个建立 _非特权_ 容器的选项： 

  * 只以 _root_ 用户的身份建立非特权容器。同样为 _sysctl_ 的 `user.max_user_namespaces` 配置设置一个正值来满足你的环境要求，如果当前值为 `0` （这将解决运行 `lxc info --show-log _container_name_` 时产生的 `Failed to clone process in new user namespace` 错误）。
  * 在 [linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 & `lxd 5.0.0` 下，你可能需要配置 `/etc/subuid` & `/etc/subgid` 为使用 `root:1000000:65536` 。你还可能需要以特权模式启用**第一个** 容器。这会解决错误 `newuidmap failed to write mapping "newuidmap: uid range [0-1000000000) -> [1000000-1001000000) not allowed"` 。
  * 启用 _sysctl_ 的 `kernel.unprivileged_userns_clone` 配置来允许普通用户运行非特权容器。可以以 root 身份运行 `sysctl kernel.unprivileged_userns_clone=1` 来为当前会话生效或阅读 [sysctl.d(5)](<https://man.archlinux.org/man/sysctl.d.5>) 使其永久生效。

###  宿主机网络配置

LXC 支持多种不同的虚拟网络类型和设备（见 [lxc.container.conf(5) § NETWORK](<https://man.archlinux.org/man/lxc.container.conf.5#NETWORK>)）。本节所介绍的虚拟网络类型中，大部分都需要一个宿主机上的网桥设备。 

这里主要有几个可供参考的配置： 

  1. 主机网桥
  2. NAT 网桥

主机网桥需要宿主机上的网络设置工具来配置一个共享网桥接口。宿主机和所有 LXC 容器将在同一个网络中被指派 IP 地址（如 192.168.1.x）。当你的目标是将一些暴露在网络上的服务如 web 服务器或 VPN 服务器容器化时，这可能更加便捷。用户可以将 LXC 当作物理 LAN 上的其他 PC，并在路由器上为其配置相应的端口转发。增加的便捷也可以认为是增加的威胁向量，同样的，如果 WAN 流量被转发给 LXC，将其运行在不同的网络范围上将显现更小的威胁面。 

NAT 网桥不需要宿主机的网络设置工具来配置网桥。[lxc](<https://archlinux.org/packages/?name=lxc>)包 自带的 `lxc-net` 将建立一个叫 `lxcbr0` 的 NAT 网桥。这个 NAT 网桥是一个独立的网桥，具有不与以太网设备或物理网络桥接的私有网络。它以宿主机的一个子网的形式存在。 

####  使用主机网桥

见 [Network bridge](<../zh-cn/Network_bridge.html> "Network bridge")。 

####  使用 NAT 网桥

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包，它是 `lxc-net` 的依赖，并在网桥启动前，先为其建立配置文件： 
    
    /etc/default/lxc-net
    
    # Leave USE_LXC_BRIDGE as "true" if you want to use lxcbr0 for your
    # containers.  Set to "false" if you'll use virbr0 or another existing
    # bridge, or mavlan to your host's NIC.
    USE_LXC_BRIDGE="true"
    
    # If you change the LXC_BRIDGE to something other than lxcbr0, then
    # you will also need to update your /etc/lxc/default.conf as well as the
    # configuration (/var/lib/lxc/<container>/config) for any containers
    # already created using the default config to reflect the new bridge
    # name.
    # If you have the dnsmasq daemon installed, you'll also have to update
    # /etc/dnsmasq.d/lxc and restart the system wide dnsmasq daemon.
    LXC_BRIDGE="lxcbr0"
    LXC_ADDR="10.0.3.1"
    LXC_NETMASK="255.255.255.0"
    LXC_NETWORK="10.0.3.0/24"
    LXC_DHCP_RANGE="10.0.3.2,10.0.3.254"
    LXC_DHCP_MAX="253"
    # Uncomment the next line if you'd like to use a conf-file for the lxcbr0
    # dnsmasq.  For instance, you can use 'dhcp-host=mail1,10.0.3.100' to have
    # container 'mail1' always get ip address 10.0.3.100.
    #LXC_DHCP_CONFILE=/etc/lxc/dnsmasq.conf
    
    # Uncomment the next line if you want lxcbr0's dnsmasq to resolve the .lxc
    # domain.  You can then add "server=/lxc/10.0.3.1' (or your actual $LXC_ADDR)
    # to your system dnsmasq configuration file (normally /etc/dnsmasq.conf,
    # or /etc/NetworkManager/dnsmasq.d/lxc.conf on systems that use NetworkManager).
    # Once these changes are made, restart the lxc-net and network-manager services.
    # 'container1.lxc' will then resolve on your host.
    #LXC_DOMAIN="lxc"

**提示：** 确保网桥的 IP 网段不会和本地网络冲突。一种选择可用 IP 地址的方法是使用已经动态分配给容器的地址之一。可以使用 `lxc-ls -f` 命令进行检查。

然后我们需要修改 LXC 容器模板使我们的容器使用我们的网桥： 
    
    /etc/lxc/default.conf
    
    lxc.net.0.type = veth
    lxc.net.0.link = lxcbr0
    lxc.net.0.flags = up
    lxc.net.0.hwaddr = 00:16:3e:xx:xx:xx

作为一个可选配置，创建一个配置文件来手动为任意一个容器指定 IP 地址： 
    
    /etc/lxc/dnsmasq.conf
    
    dhcp-host=playtime,10.0.3.100

#####  防火墙相关

基于宿主机运行的防火墙类型，可能需要允许 `lxcbr0` 的入口流量进入宿主机，以及 `lxcbr0` 的出口流量穿过宿主机进入其他网络。为了测试这是否可以实现，尝试启动一个容器并使用 DHCP 自动获取 IP 地址，检查 `lxc-net` 是否能够为容器注册一个 IP 地址。（如果 IP 地址并没有被成功分配，可以用 `lxc-ls -f` 检查，宿主机有必要更改的策略。 

[ufw](<https://archlinux.org/packages/?name=ufw>)包 用户可以简单运行[下面两行命令](<https://discuss.linuxcontainers.org/t/lxd-bridge-doesnt-work-with-ipv4-and-ufw-with-nftables/10034/17>)来放行入口和出口流量: 
    
    # ufw allow in on lxcbr0
    # ufw route allow in on lxcbr0
    
或者，[nftables](<https://archlinux.org/packages/?name=nftables>)包 用户可以编辑 `/etc/nftables.conf` （并运行 `nft -f /etc/nftables.conf` 重载该配置；运行 `nft -cf /etc/nftables.conf` 来检查格式是否正确）使容器能够具有互联网访问权限（将 `"eth0"` 替换成系统中具有互联网连接的设备；运行 `ip link` 列出所有设备： 
    
    /etc/nftables.conf
    
    table inet filter {
      chain input {
        ...
        iifname "lxcbr0" accept comment "Allow lxc containers"
        
        pkttype host limit rate 5/second counter reject with icmpx type admin-prohibited
        counter
      }
      chain forward {
        ...
        iifname "lxcbr0" oifname "eth0" accept comment "Allow forwarding from lxcbr0 to eth0"
        iifname "eth0" oifname "lxcbr0" accept comment "Allow forwarding from eth0 to lxcbr0"
      }
    }
    
另外，由于 LXC 运行在 10.0.3.x 子网上，需要将对诸如 ssh、httpd 等服务的访问主动转发到 LXC。原则上，主机上的防火墙需要对容器上预期端口的入口流量进行转发。 

######  iptables 规则示例

这个示例规则的功能是允许 ssh 流量转发到 LXC： 
    
    # iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 2221 -j DNAT --to-destination 10.0.3.100:22
    
这个规则将 2221 端口的 tcp 流量转发到 LXC 的 22 端口上。 

**注意：** 确保允许宿主机上 2221/tcp 的流量和 LXC 上 22/tcp 的流量。

为了从 LAN 上的另一台 PC 通过 ssh 连接到容器，需要 ssh 到宿主机的 2221 端口。宿主机将会把流量转发给容器。 
    
    $ ssh -p 2221 host.lan
    
######  ufw 规则示例

如果使用 [ufw](<https://archlinux.org/packages/?name=ufw>)包，将下面的内容添加到 `/etc/ufw/before.rules` 中： 
    
    /etc/ufw/before.rules
    
    *nat
    :PREROUTING ACCEPT [0:0]
    -A PREROUTING -i eth0 -p tcp --dport 2221 -j DNAT --to-destination 10.0.3.100:22
    COMMIT
    
#####  以非 root 用户运行容器

为了使用非 root 用户创建并启动容器，需要进行额外的配置。 

建立 usernet 文件名为 `/etc/lxc/lxc-usernet`。根据 [lxc-usernet(5)](<https://man.archlinux.org/man/lxc-usernet.5>)，每一行配置格式为： 
    
    user type bridge number
    
为每个需要建立容器的用户添加配置。bridge 需要和 `/etc/default/lxc-net` 中定义的一样。 

在非 root 用户的家目录还需要一份 `/etc/lxc/default.conf` 配置文件的拷贝，如 `~/.config/lxc/default.conf` （如果有必要的话请建立该目录）。 

以非 root 用户运行容器需要 `~/.local/share/` 具有 `+x` 权限。在启动容器前使用 [chmod](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%9D%83%E9%99%90> "Chmod") 命令应用该更改。 

###  创建容器

使用 [lxc-create(1)](<https://man.archlinux.org/man/lxc-create.1>) 命令创建容器。在 lxc-3.0.0-1 版本中，上游移除了本地存储的容器模板。 

使用像下面这样的调用，来建立一个 Arch 容器： 
    
    # lxc-create --name _playtime_ --template download -- --dist archlinux --release current --arch amd64
    
使用像下面这样的调用并从支持的列表中选择，来建立其他发行版的容器： 
    
    # lxc-create --name _playtime_ --template download
    
要查看 _download_ 模板的选项列表： 
    
    # lxc-create -t download --help
    
**提示：**

  * 用户可以选择安装 [haveged](<https://archlinux.org/packages/?name=haveged>)包 包并 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `haveged.service` ，来避免在设置过程中，等待系统熵种子生成时出现类似挂起的情况。否则 private/GPG 密钥的生成过程可能使整个过程变得更长。
  * [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 用户可以应用 `-B btrfs` 来建立一个 Btrfs 子卷以存储容器化的根目录。这在使用 `lxc-clone` 命令进行容器克隆时十分有用。 [ZFS](<../zh-cn/ZFS.html> "ZFS") 用户可以相应地应用 `-B zfs`。

**注意：** 想要使用传统模板的用户可以在 [lxc-templates](<https://aur.archlinux.org/packages/lxc-templates/>)AUR 找到它们，或者用户也可以用 [distrobuilder](<https://archlinux.org/packages/?name=distrobuilder>)包 建立自己的模板。

###  配置容器

下面的例子同时适用于 _特权_ 和 _非特权_ 容器。主要对于非特权容器，默认会出现例子中没有出现的额外配置，包括 `lxc.idmap = u 0 100000 65536` 和 `lxc.idmap = g 0 100000 65536` 这些在[启用非特权容器支持（可选）](</wzh/index.php?title=%E5%90%AF%E7%94%A8%E9%9D%9E%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8%E6%94%AF%E6%8C%81%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89&action=edit&redlink=1> "启用非特权容器支持（可选）（页面不存在）")中作为可选配置添加的值。 

####  具有网络支持的基本配置

**注意：** 在 lxc-1:2.1.0-1 版本中，许多配置选项改变了。已有的容器需要被更新；用户需要参考 [v2.1 发布注记](<https://discuss.linuxcontainers.org/t/lxc-2-1-has-been-released/487>) 中包含这些变化的表格。

当一个进程使用 `/var/lib/lxc/CONTAINER_NAME/config` 中定义的容器时，系统资源将被虚拟化/隔离。在默认情况下，创建容器的进程将应用一个没有网络支持的最小化配置。下面是一个具有 `lxc-net.service` 提供网络支持的示例： 
    
    /var/lib/lxc/playtime/config
    
    # Template used to create this container: /usr/share/lxc/templates/lxc-archlinux
    # Parameters passed to the template:
    # For additional config options, please look at lxc.container.conf(5)
    
    # Distribution configuration
    lxc.include = /usr/share/lxc/config/common.conf
    lxc.arch = x86_64
    
    # Container specific configuration
    lxc.rootfs.path = dir:/var/lib/lxc/playtime/rootfs
    lxc.uts.name = playtime
    
    # Network configuration
    lxc.net.0.type = veth
    lxc.net.0.link = lxcbr0
    lxc.net.0.flags = up
    lxc.net.0.hwaddr = ee:ec:fa:e9:56:7d
    
####  容器中的挂载点

对于 _特权_ 容器，用户可以选择宿主机上的目录并以 bind 方式挂载在容器中。这在容器化相同架构并希望在容器和宿主机之间分享 pacman 软件包时非常有用。另一个例子是共享文件夹。配置的格式是： 
    
    lxc.mount.entry = /var/cache/pacman/pkg var/cache/pacman/pkg none bind 0 0
    
**注意：** 若不对文件系统权限进行更改，这在 _非特权_ 容器上将无法使用。

####  图形化程序相关（可选）

为了在宿主机上显示容器中的程序窗口，需要定义一些挂载点，使容器化的程序可以获取宿主机上的资源。向 `/var/lib/lxc/playtime/config` 添加下面的段落： 
    
    ## for xorg
    lxc.mount.entry = /dev/dri dev/dri none bind,optional,create=dir
    lxc.mount.entry = /dev/snd dev/snd none bind,optional,create=dir
    lxc.mount.entry = /tmp/.X11-unix tmp/.X11-unix none bind,optional,create=dir,ro
    lxc.mount.entry = /dev/video0 dev/video0 none bind,optional,create=file
    
[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 设置 `xhost +` 是非常不安全的，参考 [cookie-based authentication](<../zh-cn/Systemd-nspawn.html#%E9%81%BF%E5%85%8D_xhost> "Systemd-nspawn") 作为替代。（在 [Talk:Linux 容器](<../zh-cn/Talk:Linux_%E5%AE%B9%E5%99%A8.html>) 中讨论）

如果 LXC 客户机依然出现 _permission denied_ 的报错，在宿主机调用 `xhost +` 来允许客户机连接宿主机的显示服务器。注意这种完全放开显示适配器权限可能带来的安全风险。 另外，在上面的挂载点**之前** 添加下面的配置。 
    
    lxc.mount.entry = tmpfs tmp tmpfs defaults
    
####  VPN 相关

运行容器化的 [OpenVPN](<../zh-cn/OpenVPN.html> "OpenVPN") 或 [WireGuard](<../zh-cn/WireGuard.html> "WireGuard"), 见 [Linux 容器/使用 VPN](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8/%E4%BD%BF%E7%94%A8_VPN.html> "Linux 容器/使用 VPN") 。 

##  管理容器

###  基本使用方法

列出所有已安装的LXC容器： 
    
    # lxc-ls -f
    
可以使用Systemd的`lxc@CONTAINER_NAME.service`来[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")或[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop")LXC。[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `lxc@CONTAINER_NAME.service`可以在宿主系统启动时连带启动LXC。 

也可以不使用Systemd来启动或停止LXC。启动一个LXC容器： 
    
    # lxc-start -n _CONTAINER_NAME_
    
停止容器： 
    
    # lxc-stop -n _CONTAINER_NAME_
    
登录容器： 
    
    # lxc-console -n _CONTAINER_NAME_
    
登录容器后，它就像普通的Linux系统一样，可以进行设置root账户密码、创建用户、下载软件包等操作。 

执行容器内命令： 
    
    # lxc-attach -n _CONTAINER_NAME_ --clear-env
    
它和lxc-console相似，用于以root权限在容器内执行一条命令。若不使用` --clear-env`选项，容器将携带宿主机的环境变量值（例如`$PATH`，容器使用其他发行版的环境变量可能无法执行某些指令）。 

###  高级使用方法

####  LXC容器克隆

通过快照运行多个容器可以减少管理容器权限的负担（如用户管理和系统更新等）。该策略是以一个最新版本的容器为基础，需要使用容器时，克隆一个基础容器并在这个克隆的基础容器上构建应用。容器使用overlayfs挂载，overlayfs只会存储和基本容器有差异的数据，故这种策略能尽可能减少对系统和磁盘的占用。基本容器是只读的，但是通过overlayfs，由基本容器衍生的其他容器可以进行修改。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** The note needs a reference. (在 [Talk:Linux 容器](<../zh-cn/Talk:Linux_%E5%AE%B9%E5%99%A8.html>) 中讨论)

**注意：** 因为安全原因，目前的主线Arch Linux内核不支持非特权容器使用overlayfs

例如，设置一个基础容器，并通过以下命令以基础容器为基础创建两个快照（snapshot）容器，称之为“snap1”和“snap2”. 
    
    # lxc-copy -n base -N snap1 -B overlayfs -s
    # lxc-copy -n base -N snap2 -B overlayfs -s
    
**注意：** 如果在基础容器上设定了静态IP，在启动快照容器前应为它手动设定IP。如果涉及到自动化流程，可以在自动化脚本内使用sed对快照容器进行IP设置。

这些快照可以像其他容器一样被启动和关闭。用户可以通过以下命令选择性的删除某些快照和其中的数据。该删除指令不会影响基础容器。 
    
    # lxc-destroy -n snap1 -f
    
在[pi-hole](</wzh/index.php?title=Pi-hole&action=edit&redlink=1> "Pi-hole（页面不存在）")和[OpenVPN](<../zh-cn/OpenVPN.html> "OpenVPN")管理快照的脚本及系统组件可在[lxc-service-snapshots](<https://github.com/graysky2/lxc-service-snapshots>)获得。 

###  将一个特权容器转换为非特权容器

当一个系统被设置为使用非特权容器时（见 [#Enable support to run unprivileged containers (optional)](<#Enable_support_to_run_unprivileged_containers_\(optional\)>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]），[nsexec-bzr](<https://aur.archlinux.org/packages/nsexec-bzr/>)AUR包含一个被称为`uidmapshift`的工具将某个已经存在的特权容器转换为非特权容器从而避免重新构建新容器。 

**警告：**

  * 强烈建议在使用这个工具前备份容器！！！
  * 这个工具不会更改[ACL](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "ACL")内的的UID和GID，请手动变更。

可以使用以下命令来进行转换： 
    
    # uidmapshift -b /var/lib/lxc/foo 0 100000 65536
    
直接运行`uidmapshift`可查看使用帮助。 

##  运行Xorg程序

使用lxc-attach或[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")调用目标容器，并在需要使用的程序前加上X程序的DISPLAY ID。对于大多数简单的设置，显示编号通常为0。 

一个简单的例子，在容器内运行Firefox并在主机屏幕上显示： 
    
    $ DISPLAY=:0 firefox
    
或者为避免直接连接容器，以下命令可以在宿主容器使这个过程自动化： 
    
    # lxc-attach -n playtime --clear-env -- sudo -u YOURUSER env DISPLAY=:0 firefox
    
##  提示与技巧

###  在非特权容器中 ping 无法工作

在非特权容器中，如果没有额外的配置步骤，ping 很可能无法工作。示例错误： 
    
    % ping www.google.com
    ping: socktype: SOCK_RAW
    ping: socket: Operation not permitted
    ping: -> missing cap_net_raw+p capability or setuid?
    
要在主机上修复容器 foo 中的此问题： 
    
    # lxc-attach -n foo -- chmod u+s /usr/bin/ping

##  故障排除

###  Root用户登录失败

如果在使用lxc-console登录时显示以下错误： 
    
    login: root
    Login incorrect
    
以及容器的 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 显示: 
    
    pam_securetty(login:auth): access denied: tty 'pts/0' is not secure !
    
删除容器内文件系统的 `/etc/securetty`[[2]](<https://unix.stackexchange.com/questions/41840/effect-of-entries-in-etc-securetty/41939#41939>) 和 `/usr/share/factory/etc/securetty`。或者将它们加入`/etc/pacman.conf`的[NoExtract](<../zh-cn/Pacman.html#%E5%9C%A8%E5%AE%89%E8%A3%85%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "NoExtract")中以阻止它们被重新下载，见 **[FS#45903](<https://bugs.archlinux.org/task/45903>)** 。 

或者使用lxc-attach创建一个新用户并用它来登陆系统，在登录后切换为root账户。 
    
    # lxc-attach -n playtime
    [root@playtime]# useradd -m -Gwheel newuser
    [root@playtime]# passwd newuser
    [root@playtime]# passwd root
    [root@playtime]# exit
    # lxc-console -n playtime
    [newuser@playtime]$ su
    
###  容器配置中使用 veth 时无网络连接

如果你通过`/etc/lxc/_containername_ /config`将网络接口设定为**veth** 后无法访问局域网或广域网，请检查这个虚拟网口是否获得ip地址并正确连接到网络。 
    
    ip addr show veth0 
    inet 192.168.1.111/24
    
你可以关闭所有有关的静态ip集，并像平常一样通过已启动的容器设置这些ip 

例如 `_container_ /config`
    
    ...
    lxc.net.0.type = veth
    lxc.net.0.name = veth0
    lxc.net.0.flags = up
    lxc.net.0.link = bridge
    ...
    
然后通过容器的首选方法分配 IP，见[网络配置#Network management](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Network_management> "网络配置"). 

###  无法找到命令

当在相对于宿主机系统使用不同Linux发行版的容器中（例如在Arch Linux宿主机系统中运行Debian容器）执行基本命令（如 _ls_ 、 _cat_ 等）时，可能会出现此错误。在附加容器时，请使用参数`--clear-env`： 
    
    # lxc-attach -n _container_name_ --clear-env
    
### Failed at step KEYRING spawning...

在非特权容器内执行的服务可能会出现以下错误： 
    
    some.service: Failed to change ownership of session keyring: Permission denied
    some.service: Failed to set up kernel keyring: Permission denied
    some.service: Failed at step KEYRING spawning ....: Permission denied
    
在容器内添加文件`/etc/lxc/unpriv.seccomp`，并写入以下配置： 
    
    /etc/lxc/unpriv.seccomp
    
    2
    blacklist
    [all]
    keyctl errno 38

并在容器配置文件的lxc.idmap属性后添加： 
    
    lxc.seccomp.profile = /etc/lxc/unpriv.seccomp
    
##  已知的问题

###  缺失lxc.init.static会导致lxc-execute执行失败

`lxc-execute` 指令运行失败并显示以下错误：`Unable to open lxc.init.static`。参见 [FS#63814](<https://bugs.archlinux.org/task/63814>) 了解详情。 

使用 `lxc-start` 命令重启即可。 

##  参见

  * [官方网站](<https://linuxcontainers.org/lxc/introduction/>)
  * [入门指南](<https://linuxcontainers.org/lxc/getting-started/>)
  * [文档](<https://linuxcontainers.org/lxc/documentation/>)
  * [论坛](<https://discuss.linuxcontainers.org/>)
  * [官方 GitHub 仓库](<https://github.com/lxc/lxc>)
