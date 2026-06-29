**翻译状态：**

  * 本文（或部分内容）译自 [Linux Containers/Using VPNs](<https://wiki.archlinux.org/title/Linux_Containers/Using_VPNs> "arch:Linux Containers/Using VPNs")，最近一次同步于 2024-4-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Linux_Containers/Using_VPNs?diff=0&oldid=806283>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Linux_Containers_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Using_VPNs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [OpenVPN](<../../zh-cn/OpenVPN.html> "OpenVPN")
  * [PeerGuardian_Linux](</wzh/index.php?title=PeerGuardian_Linux&action=edit&redlink=1> "PeerGuardian Linux（页面不存在）")
  * [ufw](<../../zh-cn/Uncomplicated_Firewall.html> "Ufw")
  * [WireGuard](<../../zh-cn/WireGuard.html> "WireGuard")

本文介绍如何设置 [Linux_容器](<../../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "Linux 容器")来运行多个带有“终止开关”的 VPN 协议，以实现安全/隐私的互联网使用。 与使用 [VirtualBox](<../../zh-cn/VirtualBox.html> "VirtualBox") 或者 [QEMU](<../../zh-cn/QEMU.html> "QEMU") 等全套的虚拟化相比， 这样做提供了更小的资源开销和在低功耗设备上运行等明显优势。 

##  配置容器

需要对 [Linux_容器](<../../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "Linux 容器")进行基本配置和了解。 本文假设读者已经设置了可运行的基本LXC。 

##  服务器模式的OpenVPN

本小节详细介绍了在容器中提供 OpenVPN 服务所需的一些额外设置。 想要使用给出的 OpenVPN 配置文件的用户无需阅读本小节。 

###  主机设置

  1. 主机操作系统需要网桥设置才能允许容器运行。请参考 [Linux_容器#宿主机网络配置](<../../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html#%E5%AE%BF%E4%B8%BB%E6%9C%BA%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE> "Linux 容器")。
  2. 需要启用数据包转发。请参考[网络分享#启用包转发](<../../zh-cn/%E7%BD%91%E7%BB%9C%E5%88%86%E4%BA%AB.html#%E5%90%AF%E7%94%A8%E5%8C%85%E8%BD%AC%E5%8F%91> "网络分享")。
  3. 尽管不是必须的，但强烈建议使用防火墙。

##  客户端模式的 OpenVPN

需要修改容器的配置才能使用 OpenVPN，如下所示： 
    
    /var/lib/lxc/playtime/config
    
    ...
    
    ## for OpenVPN
    lxc.mount.entry = /dev/net dev/net none bind,create=dir
    lxc.cgroup2.devices.allow = c 10:200 rwm
    
安装 [openvpn](<https://archlinux.org/packages/?name=openvpn>)包. 如果使用容器连接到第三方 VPN 提供商，只需将配置文件 `foo.conf` 放在 `/etc/openvpn/client/foo.conf` 即可。 To v要验证容器内的 OpenVPN 功能，请[启动](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `openvpn-client@foo.service` 来开启OpenVPN。一旦对当前配置感到满意，[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")服务来实现系统启动后自动开启。 

有关其他用例和设置，请参阅 [OpenVPN](<../../zh-cn/OpenVPN.html> "OpenVPN")。 

**注意：** 在“非特权”容器中运行 OpenVPN 的用户需要创建一个自定义 systemd 单元才能在容器中启动它。在[替换单元文件](<../../zh-cn/Systemd.html#%E6%9B%BF%E6%8D%A2%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")中注释掉以下开头的行：`LimitNPROC...`

## WireGuard

安装[wireguard-tools](<https://archlinux.org/packages/?name=wireguard-tools>)包。用户将拥有由第三方 VPN 服务提供的 WireGuard 配置，或者自己设置好的WireGuard 对应的配置。 如果使用容器连接到 VPN 提供商， 只需将配置文件 `foo.conf` 放入 `/etc/wireguard/` 。 

要验证容器内的 WireGuard 功能，请通过[启动](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `wg-quick@foo.service` 来开启WireGuard。一旦对当前配置感到满意，[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")服务来实现系统启动后自动开启。 

有关其他用例和设置，请参阅 [WireGuard](<../../zh-cn/WireGuard.html> "WireGuard")。 

##  容器内的防火墙配置

_强烈_ 建议在容器内运行正确配置的[防火墙](<../../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Firewalls")。容器内防火墙的作用有两个： 

  1. 提供“终止开关”，以便在 VPN 连接失败时维护隐私。
  2. 把不想要东西拒之门外。

本指南使用易于配置的 [ufw](<https://archlinux.org/packages/?name=ufw>)包，当然也可以使用其他防火墙。 

**提示：** 要完全重置 ufw 的配置文件，使用reset: `ufw reset`.

设置“终止开关”的方法是通过设置一个拒绝政策然后只允许VPN设备上的特定服务和流量。这样，如果该设备的连接中断时不会出现本地政策回退。 

**注意：** 下面显示的方法的一个限制是 VPN 配置文件不得使用 www.myvpn.com 等域名，它们需要使用相应的 IP 地址。如上所述，当 VPN 未连接时，容器 DNS 解析将被禁用。因此，为了连接，必须提供数字 IP。

编辑 `/etc/default/ufw` 并将 DEFAULT_OUTPUT_POLICY 从 "ACCEPT" 更改为 "DROP": 
    
    /etc/default/ufw
    
    DEFAULT_OUTPUT_POLICY="DROP"

**注意：** 以下命令调用 `ufw` 需要以root用户执行； 按照 wiki 标准命令的前缀“#”符号已被省略，以允许干净地复制/粘贴到终端中。

设置拒绝政策： 
    
    ufw default deny outgoing
    ufw default deny incoming
    
（可选）添加例如`/etc/ufw/applications.d/custom`等文件中定义的任何预定义或自定义规则： 
    
    ufw allow ssh
    ufw allow from my-custom-app1
    ufw allow from my-custom-app2
    
（可选）进一步限制来自内部 LAN IP 范围甚至单个 IP 地址的访问： 
    
    ufw allow from 192.168.1.0/24
    
WireGuard 用户将拥有一个与相应配置文件，比如`/etc/wireguard/foo.conf`，同名的接口，而 OpenVPN 用户很可能使用`tun0`. 在下面的命令中，将“foo”替换为 WireGuard 配置文件的名称（省略 .conf 后缀），或者如果使用 OpenVPN，则将“foo”替换为 tun0 或正在使用的任何设备： 
    
    ufw allow out on foo from any to any
    
最后，打开 VPN 提供商的 IP 地址和端口，并定义相对应的协议。在下面的行中，需要考虑三个变量： 

  * “xxx”代表 WireGuard 的 peer 或者 OpenVPN 的服务器的IP地址。它将在 VPN 提供商提供的相应配置文件中。
  * “yyy”代表要进行通信的端口。同样，这将位于配置文件中。
  * “zzz” 代表要使用的协议，可以从 udp 或 tcp 中选择。请注意，WireGuard 仅支持 udp，而 OpenVPN 两者都支持。

    ufw allow out to xxx port yyy proto zzz
    
**注意：** 如果预计使用多个服务器，请对 VPN 提供商定义的每个 IP 地址 (xxx) 重复此操作。

启动 ufw 并[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `ufw.service` 以实现开机启动。 

###  在配置文件中使用 VPN 域名的一个非正式方法

如果需要在 VPN 配置文件中使用域名，主机上的 shell 脚本可以将其预先解析为数字 IP，然后通过将该 IP 地址存储在写在容器中文件的一个变量来将该 IP 地址传递给容器。该文件又可以由修改后的 VPN systemd 服务读取。 它可以用, 但不正规。 

编辑两个变量以匹配相对应的容器名称和服务器名称： 

####  在主机上

安装 [bind](<https://archlinux.org/packages/?name=bind>)包 (dig 需要)并创建以下脚本： 
    
    /path/to/container-start.sh
    
    #!/bin/bash
    # this script should be called as root
    container=foo
    server=www.myvpnserver.org
     
    if ! systemctl is-active lxc@"$container" &>/dev/null; then
      ToUse=$(dig +short "$server")
      [[ -d /var/lib/lxc/$container/rootfs/etc/conf.d ]] || mkdir -p /var/lib/lxc/$container/rootfs/etc/conf.d
      echo "SERVER=$ToUse" > /var/lib/lxc/$container/rootfs/etc/conf.d/server.hack.txt
      systemctl start lxc@"$container"
    fi
    
从现在开始，调用该脚本来启动容器。它将使用 dig 从域名中获取 IP 地址，然后启动容器。 

####  从容器内部

修改启动 VPN 的 systemd 服务并创建一个框架配置文件，该配置文件可以使用我们刚刚创建的脚本创建的`/var/lib/lxc/$container/rootfs/etc/conf.d/server.hack.txt` 中定义的 IP 地址进行修改。 

要制作框架配置文件，只需将使用的配置文件重命名为另一个名称即可。 

例如使用 WireGuard： 
    
    mv /etc/wireguard/foo.conf /etc/wireguard/foo.skel
    
现在编辑 `/etc/wireguard/foo.skel` 以将 **Endpoint = www.myvpnserver.org** 替换为**@@@** ，例如： 
    
    Endpoint = @@@:51820
    
或者如果使用 OpenVPN： 
    
    mv /etc/openvpn/client/foo.conf /etc/openvpn/client/foo.skel
    
编辑 `/etc/openvpn/client/foo.skel` 以将远程**www.myvpnserver.org** 替换为**@@@** ，例如： 
    
    remote @@@
    
最后，创建一个[附加配置片段](<../../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd"), 以读取 IP 并将其替换为实际配置文件。 

使用 WireGuard 的示例： 
    
    /etc/systemd/system/wg-quick@foo.service.d/override.conf
    
    [Service]
    EnvironmentFile=-/etc/conf.d/server.hack.txt
    ExecStartPre=/bin/bash -ac "sed s/@@@/$SERVER/ </etc/wireguard/foo.skel >/etc/wireguard/foo.conf"

使用 OpenVPN 的示例： 
    
    /etc/systemd/system/openvpn-client@foo.service.d/override.conf
    
    [Service]
    EnvironmentFile=-/etc/conf.d/server.hack.txt
    ExecStartPre=/bin/bash -ac "sed s/@@@/$SERVER/ </etc/openvpn/client/foo.skel >/etc/openvpn/client/foo.conf"

##  测试服务

在正在运行的容器内 (通过 ssh 或者 `lxc-attach -n playtime`) 通过将浏览器导出到主机的计算机 X server 来测试设置: 
    
    $ DISPLAY=:0 firefox
    
**提示：** 通过 ssh 连接需要允许本地显示接受连接。执行此操作 `xhost +SI:localuser:yourusername` 然后通过 ssh 连接到容器。

结果应该是主机的 X server 中出现一个标题为"Mozilla Firefox (playtime)" 的 Firefox 窗口。许多网站可用于验证 IP 地址和 DNS 的状态，例如 [ipleak dot net](<https://ipleak.net>). 

此时，仅应显示与配置文件中定义的条目相对应的 DNS 条目。 
