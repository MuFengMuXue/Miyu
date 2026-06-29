相关文章

  * [IPv6 tunnel broker setup](</wzh/index.php?title=IPv6_tunnel_broker_setup&action=edit&redlink=1> "IPv6 tunnel broker setup（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [IPv6](<https://wiki.archlinux.org/title/IPv6> "arch:IPv6")，最近一次同步于 2022-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/IPv6?diff=0&oldid=757072>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/IPv6_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

在 Arch Linux 中，[IPv6](<https://en.wikipedia.org/wiki/IPv6> "wikipedia:IPv6") 是默认开启的。 

[tldp Linux+IPv6-HOWTO](<https://tldp.org/HOWTO/Linux+IPv6-HOWTO/index.html>) 这篇文章比较旧， 且缺乏维护。不过其涵盖了本文所提及的许多主题，从基础的东西讲起并且循序渐进到高级配置。而且还有很多命令的例子。初学者可以先读一读这篇文章再接着阅读本文。 

##  邻居发现（Neighbor discovery，ND）

使用 Ping 命令来 ping `ff02::1` 这个多播地址，会得到本地链路层的所有主机的响应。需要手动指定接口（`%eth0`） 
    
    $ ping ff02::1%eth0
    
Ping 完之后，您可以用如下命令来获取本地子网中的所有主机。 
    
    $ ip -6 neigh
    
如果您 Ping 的是 `ff02::2` 这个多播地址，则只有网络中的路由器会响应。 

如果您添加一个 `-I _your-global-ipv6_` 选项，本地链路上的主机会以他们的本地链路地址来响应。这种情况下可以省略接口。 
    
    $ ping -I 2001:4f8:fff6::21 ff02::1
    
用下面这个脚本可以 Ping 所有接口上的所有其他主机，并且把你的地址告诉所有人。 
    
    #!/usr/bin/bash
    declare -a l_ifs
    readarray l_ifs < <(/sbin/ip -6 -j address | jq -r '.[] | .ifname ')
    for l_if in ${l_ifs[@]} ; do
     echo $l_if
     declare -a l_addrs
     readarray l_addrs < <(/sbin/ip -6 -j address show dev "$l_if" | \
                            jq -r  '.[0].addr_info[].local')
     for l_addr in ${l_addrs[@]} ; do
       echo $l_addr
       ping -c 4 -6 -I "$l_addr" ff02::1%"$l_if"
     done
    done
    
##  无状态地址自动配置 (SLAAC)

想要获得一个IPv6地址，最简单的办法就是用SLAAC。只要您的网络配置好了“无状态地址自动配置”（Stateless address autoconfiguration，简称SLAAC），您的设备就会自动根据路由器广播（Router Advertisement，RA）的前缀为自己配置一个地址。既不需要进一步配置，也不需要专门的软件（如DHCP客户端） 

###  客户端配置

如果您正在使用 [netctl](<../zh-cn/Netctl.html> "Netctl")，您要做的只是往接口配置文件里加上这么一行： 
    
    IP6=stateless
    
如果您使用的是 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")，那么只要网络内有路由器广播，它就会自动配置上 IPv6 地址。 

不过需要注意的是，SLAAC只有在网络允许 IPv6 ICMP 包通过的时候才能工作。所以你需要在客户端防火墙上允许 `ipv6-icmp` 类型的数据包传入。如果您用的是 [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")/[iptables](<../zh-cn/Iptables.html> "Iptables")，加上下面这行就可以了： 
    
    -A INPUT -p ipv6-icmp -j ACCEPT
    
如果您用的是其他防火墙，请参考对应的文档来放行 `ipv6-icmp` 数据包。 

如果你选择的网络管理方案不支持通过SLAAC配置DNS（比如netctl），那么你可以考虑用[ndisc6](<https://archlinux.org/packages/?name=ndisc6>)包包里的[rdnssd(8)](<https://man.archlinux.org/man/rdnssd.8>)命令来配置DNS。 

###  路由器（网关）配置

要正确给网络内的客户端分配 IPv6，我们要用到一个广播守护进程，一般是[radvd](<https://archlinux.org/packages/?name=radvd>)包。其配置过程其实相当简单。参考下面的配置来编辑 `/etc/radvd.conf`文件。 
    
    # 把LAN替换为你实际的局域网接口
    interface LAN {
      AdvSendAdvert on;
      MinRtrAdvInterval 3;
      MaxRtrAdvInterval 10;
      prefix ::/64 {
        AdvOnLink on;
        AdvAutonomous on;
        AdvRouterAddr on;
      };
    };
    
以上配置会让客户端自己从 /64 地址段中选择地址来使用。请注意如果配置了 `prefix ::/64`，RADVD会向局域网广播那个接口上的 _所有_ 可用的前缀。如果您想要广播指定的前缀，请手动指定，比如 `prefix 2001:DB8::/64`。`prefix` 节可以根据需要多次重复来广播多个不同前缀。 

您可以通过 RDNSS 功能向客户端广播 DNS，以 Google DNS 为例，配置如下： 
    
    RDNSS 2001:4860:4860::8888 2001:4860:4860::8844 {
    };
    
网关必须在所有链上允许 `ipv6-icmp` 类型数据包通过。以 [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")/[iptables](<../zh-cn/Iptables.html> "Iptables") 为例： 
    
    -A INPUT -p ipv6-icmp -j ACCEPT
    -A OUTPUT -p ipv6-icmp -j ACCEPT
    -A FORWARD -p ipv6-icmp -j ACCEPT
    
根据其他防火墙前端进行相应的调整，最后别忘了激活 `radvd.service` 服务。 

##  隐私拓展

当一个客户端通过 SLAAC 获得一个地址时，其 IPv6 地址是经过客户端网络接口广播的前缀和 MAC 地址计算而得出的。这可能会引起隐私问题，因为别人可以轻易通过 IPv6 SLAAC 地址反推客户端 MAC。为了解决这个问题，[RFC 4941](<https://tools.ietf.org/html/rfc4941> "rfc:4941") 中提出了 _IPv6 隐私拓展_ 标准。启用隐私扩展后，内核会生成一个 _临时_ 地址，这个地址是原来的 SLAAC 地址经过二次计算得出的随机地址。当主动连接到远程服务器时，会优先选择使用私有地址，从而帮助隐藏原始的 SLAAC地址。启用隐私扩展的步骤如下: 

向 `/etc/sysctl.d/40-ipv6.conf` 中添加如下内容： 
    
    # Enable IPv6 Privacy Extensions
    net.ipv6.conf.all.use_tempaddr = 2
    net.ipv6.conf.default.use_tempaddr = 2
    net.ipv6.conf._nic0_.use_tempaddr = 2
    ...
    net.ipv6.conf._nicN_.use_tempaddr = 2
    
上面的 `nic0` 到 `nicN` 是你的网络接口。你可以参考[网络配置#Listing network interfaces](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Listing_network_interfaces> "网络配置") 来列出你的设备上的接口。 `all.use_tempaddr` 或者 `default.use_tempaddr` 参数对于执行 sysctl 设置时已经存在的接口无效，也就是说不会即时生效。 

不过当您重启设备之后，隐私拓展应该就会生效了。 

### dhcpcd

[dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") 的默认配置已经包括了 `slaac private`，这会启用 [RFC 7217](<https://tools.ietf.org/html/rfc7217> "rfc:7217") 中定义的“稳定的私有IPv6地址而不是基于硬件的地址”功能。因此，您无需修改任何设置，除非您希望更频繁地获得新的随机地址，而不仅在连接到新网络的时候改变IPv6地址。您还可以设置 `slaac hwaddr` 来使用普通的基于 MAC 生成的固定 IPv6 后缀。 

### NetworkManager

您可以修改 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 的全局配置文件 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>) 或连接配置中的 `ipv6.ip6-privacy` 选项，来决定是否启用 IPv6 隐私拓展。如果全局配置和连接配置都没有设置该选项，NetworkManager 会根据 `/proc/sys/net/ipv6/conf/default/use_tempaddr` 内核参数来决定。 

如果您想明确默认启用 IPv6 隐私拓展，请在 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>) 中添加以下内容： 
    
    /etc/NetworkManager/conf.d/ip6-privacy.conf
    
    [connection]
    ipv6.ip6-privacy=2

然后[应用配置](<../zh-cn/NetworkManager.html#Configuration> "NetworkManager")并重新连接所有活动接口。 

想要为每一个使用 NetworkManager 管理的接口单独设置 IPv6 隐私拓展功能，请编辑其对应的 `/etc/NetworkManager/system-connections/` 目录下的 keyfile，并把 `ip6-privacy=2` 添加到 `[ipv6]` 一节下方，示例如下： 
    
    /etc/NetworkManager/system-connections/_example_connection_.nmconnection
    
    ...
    [ipv6]
    method=auto
    **ip6-privacy=2**
    ...

最后，重新加载连接配置并再次连接。 

**注意：** 尽管隐私拓展生成的 `scope global temporary` IPv6 地址看上去永远不会被更新（在其 `valid_lft` 所显示的生命周期内，该地址永远不会变为 `deprecated` 状态），但经过较长时间的验证，这个地址 **确实** 会发生变化。

### systemd-networkd

_systemd-networkd_ 同样不遵守 `/etc/sysctl.d/40-ipv6.conf` 中配置的 `net.ipv6.conf.xxx.use_tempaddr` 内核参数，除非您在 _.network_ 文件中指定 `IPv6PrivacyExtensions` 选项的值为 `kernel`。 

不过 systemd-networkd 遵守其他 IPv6 隐私拓展的内核参数，比如： 
    
    net.ipv6.conf.xxx.temp_prefered_lft
    net.ipv6.conf.xxx.temp_valid_lft
    
**注意：**`temp_prefered_lft` 才是正确的变量名，“preferred”应该是拼错了

请参考 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 和 [systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>) 以了解更多信息。 

### ConnMan

在服务文件（比如 `/var/lib/connman/_service_ /settings`）中设置： 
    
    IPv6.privacy=preferred
    
请参考 [ConnMan](<../zh-cn/ConnMan.html> "ConnMan") 以了解更多信息。 

##  稳定的隐私地址

另外一个选择，是使用 [RFC 7217](<https://tools.ietf.org/html/rfc7217> "rfc:7217") 中定义的稳定隐私地址。它可以在不暴露 MAC 地址的情况下固定住网络中的 IPv6 地址。 

Another option is a stable private IP address ([RFC 7217](<https://tools.ietf.org/html/rfc7217> "rfc:7217")). This allows for IPs that are stable within a network without exposing the MAC address of the interface. 

以 `wlan0` 接口为例，使用以下命令来让内核为其生成一个密钥： 
    
    # sysctl net.ipv6.conf.wlan0.addr_gen_mode=3
    
把接口关闭再启用，然后运行 `ip addr show dev wlan0`，您应该会看到每个 IPv6 地址旁边会有 `stable-privacy` 标志。内核已经为该接口生成了一个 128 位的密钥用于产生稳定 IPv6 地址，您可以运行 `sysctl net.ipv6.conf.wlan0.stable_secret` 来查看这一密钥。我们需要固定这个密钥以让他每次重启后都获得同样的地址，所以请在 `/etc/sysctl.d/40-ipv6.conf` 中进行如下配置： 
    
    # Enable IPv6 stable privacy mode
    net.ipv6.conf.wlan0.stable_secret = _刚才查看的密钥_
    net.ipv6.conf.wlan0.addr_gen_mode = 2
    
**注意：**`stable-privacy` 标志 **不会** 被应用到由 [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") 获得的 IPv6 地址上

### NetworkManager

NetworkManager 不遵守以上设置，但是它默认已经启用了稳定隐私地址。[[1]](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-12/NEWS#L367-369>)[[2]](<https://bugzilla.redhat.com/show_bug.cgi?id=1279242#c15>)

##  静态地址

有些情况下使用静态地址可以增强安全性。使用SLAAC分配动态地址时，你的计算机的地址会由其网卡MAC推算出，这不利于安全，因为即使地址的网络号改变，你的电脑依然可以被追踪到。 

要想用[netctl](<../zh-cn/Netctl.html> "Netctl")分配一个静态地址，可以参照`/etc/netctl/examples/ethernet-static`。如下的部分尤其重要： 
    
    ...
    # For IPv6 static address configuration
    IP6=static
    Address6=('1234:5678:9abc:def::1/64' '1234:3456::123/96')
    Routes6=('abcd::1234')
    Gateway6='1234:0:123::abcd'
    
**注意：** 如果你只有IPv6连接，那么你要给出IPv6的DNS服务器，例如： 
    
    DNS=('6666:6666::1' '6666:6666::2')
    
如果你的ISP没有告诉你IPv6的DNS服务器地址，并且你也没有自己的服务器，你可以从[resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf")这篇文章中选一个。

##  IPv6与PPPoE

PPPoE的软件包`pppd`提供了对PPPoE之上的IPv6的支持（前提是你的ISP和调制解调器支持）。只需要将如下内容加入`/etc/ppp/pppoe.conf`： 
    
     +ipv6
    
如果你使用[netctl](<../zh-cn/Netctl.html> "Netctl")，那么就向你的netctl配置文件加入如下内容： 
    
     PPPoEIP6=yes
    
##  地址委派 (DHCPv6-PD)

**注意：** 这个部分是针对自行使用配置网关的内容，不是客户端。如果你使用从市场购得的路由器，请查阅其附带的文档以开启地址委派。

地址委派是一种常见的 IPv6 部署方式，被许多 ISP 所采用。具体的做法是将一个地址前缀分配给用户（局域网），即路由器配置为将不同的前缀分配给不同的子网；ISP 通过 DHCPv6 将地址前缀（通常是`/56`或`/64`）分发出去，DHCP 客户端再将前缀分配给局域网。对于一个拥有两个网卡的简单网关来说，它的工作就是将从 WAN 口（或虚拟接口，比如ppp）获取的前缀分配给局域网。 

DHCPv6 客户端需要在 UDP 546 接口上接受传入的连接。对于基于 [nftables](<../zh-cn/Nftables.html> "Nftables") 的防火墙，可以编辑 `/etc/nftables.conf`： 
    
    table inet filter {
      chain input {
        udp dport dhcpv6-client accept
        ...
      }
    ...
    }
    
###  使用dhcpcd

[Dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd")在 IPv4 之外也提供了一个完整的支持 DHCPv6-PD 的客户端。如果你使用 `dhcpcd`，需要修改 `/etc/dhcpcd.conf`。你可能已经在用dhcpcd来配置 IPv4,，所以只需要对现有的配置进行小幅修改： 
    
    duid
    noipv6rs
    waitip 6
    # Uncomment this line if you are running dhcpcd for IPv6 only.
    #ipv6only
    
    # use the interface connected to WAN
    interface WAN
    ipv6rs
    iaid 1
    # use the interface connected to your LAN
    ia_pd 1 LAN
    #ia_pd 1/::/64 LAN/0/64
    
这种配置下，客户端会从`WAN`接口获取一个前缀，分配给`LAN`接口。 如果ISP分配的是`/64`的地址，你需要用第二个`ia_pd`选项。 这也会禁用除`WAN`接口之外的所有路由器请求。 

**提示：** 查阅手册页**`dhcpcd(8)`** 与**`dhcpcd.conf(5)`** 获得更多信息。

###  使用WIDE-DHCPv6

[WIDE-DHCPv6](<http://wide-dhcpv6.sourceforge.net/>)是原本由KAME计划开发的DHCPv6开源实现。它在[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中：[wide-dhcpv6](<https://aur.archlinux.org/packages/wide-dhcpv6/>)AUR。 

如果你使用`wide-dhcpv6`，修改`/etc/wide-dhcpv6/dhcp6c.conf`： 
    
    # use the interface connected to your WAN
    interface WAN {
      send ia-pd 0;
    };
    
    id-assoc pd 0 {
      # use the interface connected to your LAN
      prefix-interface LAN {
        sla-id 1;
        sla-len 8;
      };
    };
    
**注意：**`sla-len`应设置为满足`(WAN-prefix) + (sla-len) = 64`的值。这里示范的情况是针对一个长度`/56`的前缀，56+8=64。对于前缀长度`/64`的网络，`sla-len`应为`0`。

要启用或运行wide-dhcpv6，使用如下命令。把`WAN`改为连接到ISP的网卡: 
    
    # systemctl enable/start dhcp6c@WAN.service
    
**提示：** 查阅手册页**`dhcp6c(8)`** 与**`dhcp6c.conf(5)`** 获取更多信息。

### systemd-networkd

配置您的上游(wan)和下游(lan)接口。这将在运行 DHCPv6 客户端的接口上启用 DHCPv6-PD，并通过 IPv6 路由广播在下游网络中分发委派的地址前缀。 
    
    /etc/systemd/network/wan.network
    
    [Network]
    # Use 'yes' instead of 'ipv6' for both ipv4 and ipv6.
    DHCP=ipv6
    
    /etc/systemd/network/lan.network
    
    [Network]
    IPv6SendRA=yes
    DHCPv6PrefixDelegation=yes

###  其他客户端

[dhclient](</wzh/index.php?title=Dhclient&action=edit&redlink=1> "Dhclient（页面不存在）") 也可以请求前缀；但想要把整个或者部分前缀分配到接口上则需要使用 _dhclient_ 退出脚本来完成。请参考 <https://github.com/jaymzh/v6-gw-scripts/blob/master/dhclient-ipv6> 中的例子。 

## NAT64

[Wikipedia:NAT64](<https://en.wikipedia.org/wiki/NAT64> "wikipedia:NAT64") 是让只有 IPv6 地址的主机通过使用 NAT 来和 IPv4 主机通信的过渡机制。 

Linux 内核并不原生支持 NAT64，但您可以使用以下这些软件包来添加 NAT64 支持： 

  * **Jool** — SIIT and NAT64 for Linux

     <https://nicmx.github.io/Jool/> || [jool-dkms](<https://aur.archlinux.org/packages/jool-dkms/>)AUR, [jool-tools](<https://aur.archlinux.org/packages/jool-tools/>)AUR

  * **TAYGA** — NAT64 daemon (unmaintained)

     <http://www.litech.org/tayga/> || [tayga](<https://aur.archlinux.org/packages/tayga/>)AUR

##  禁用 IPv6

**注意：** Arch直接将IPv6支持编译进内核，因此不能禁用对应的内核模块。

###  关闭 IPv6 功能

如果您遇到一些问题，可以试着向内核参数加入 `ipv6.disable=1` ，来完全关闭 IPv6 功能， 参考[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")来了解更多信息. 

此外，只加入`ipv6.disable_ipv6=1`内核参数可以保留IPv6功能，但不会向网卡分配IPv6地址。 

也可以通过向`/etc/sysctl.d/40-ipv6.conf`加入如下配置来避免系统给网卡分配IPv6地址： 
    
    # Disable IPv6
    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf._nic0_.disable_ipv6 = 1
    ...
    net.ipv6.conf._nicN_.disable_ipv6 = 1
    
重启 `systemd-sysctl.service` 单元来应用上述设置。 

注意你必须在这里清楚地列出所有不需要分配IPv6地址的网卡，仅仅设置`all.disable_ipv6`并不会立刻对已经连接的网卡起作用。 

**注意：** 如果通过 _sysctl_ 禁用IPv6， 你应该在`/etc/hosts`中删除所有的IPv6主机，否则当你使用主机名连接它们的时候会解析到不通的IPv6地址

###  其他应用程序

在内核中关闭 IPv6 功能不会阻止应用程序尝试使用 IPv6。多数情况下，这样不会有问题，但如果你发现程序无法正常运行，你应该查阅该应用程序的手册页，以找到关闭 IPv6 的合适方法。 

#### dhcpcd

_dhcpcd_ 会依然尝试发送 IPv6 路由器请求。要禁用这种行为，可以依照其手册页`dhcpcd.conf (5)`，向`/etc/dhcpcd.conf`加入如下内容： 
    
    noipv6rs
    noipv6
    
#### NetworkManager

如果要禁用 NetworkManager 的 IPv6 功能，右键点击网络状态图标，然后选择 _配置网络连接 > 有线以太网 > _网络连接名称 _ > 编辑 > IPv6 > 方法 > 忽略/已禁用_然后点击应用。 

你也可以通过命令行来设置，先输入： 
    
    # nmcli connection modify _ConnectionName_ ipv6.method "disabled"
    
然后再重启连接： 
    
    # nmcli connection up _ConnectionName_
    
要确认设置是否被应用，使用 `ip address show` 看看还有没有显示 IPv6 地址（inet6）。或者检查 `/proc/sys/net/ipv6/conf/_interface_ /disable_ipv6` 这个内核参数，其值应该为 1。 

#### ntpd

依照[Systemd#Drop-in files](<../zh-cn/Systemd.html#Drop-in_files> "Systemd")，修改`ntpd.service`的启动方式。 
    
    # systemctl edit ntpd.service
    
这样会产生一个drop-in snippet，替代原有的`ntpd.service`来加载ntpd。参数`-4`关闭了ntpd的IPv6支持。向drop-in snippet中加入如下内容： 
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/ntpd -4 -g -u ntp:ntp
    
第一行清除了之前的`ExecStart`配置，接下来的一行将该配置设置为带有`-4`参数的ntpd。 

#### GnuPG

在 _dirmngr_ 配置文件中设置如下参数： 
    
    ~/.gnupg/dirmngr.conf
    
    disable-ipv6
    
然后重启 `dirmngr.service` 服务. 

#### sshd

修改 `sshd_config` 来让 sshd 只使用 IPv4： 
    
    /etc/ssh/sshd_config
    
    AddressFamily inet
    
然后重启 `sshd.service` 服务 

#### systemd-timesyncd

有时 [Systemd-timesyncd](<../zh-cn/Systemd-timesyncd.html> "Systemd-timesyncd") 会尝试查询IPv6时间服务器，即使IPv6已被禁用。这可能导致系统时钟未更新，日志显示类似以下错误： 
    
    systemd-timesyncd[336]: Failed to set up connection socket: Address family not supported by protocol
    
`systemd timesyncd` 在其“状态”中会显示尝试连接 IPv6 地址的记录，类似于： 
    
    Status: "Connecting to time server [2001:19f0:8001:afd:5400:1ff:fe9d:cba]:123 (2.pool.ntp.org)"
    
根据 [FS#59806](<https://bugs.archlinux.org/task/59806>), 只有 2.ntp.org 池支持 IPv6。所以将 `2.arch.pool.ntp.org` 和 `2.pool.ntp.org` 从配置文件 `/etc/systemd/timesyncd.conf` 的 NTP 和 FallbackNTP 部分中删去即可避免这一现象。 

### systemd-networkd

_networkd_ 支持按接口禁用IPv6。当网络单元的 `[Network]` 部分的 `LinkLocalAddressing=ipv4` 或 `LinkLocalAddressing=no` 时，networkd不会尝试在匹配的接口上配置IPv6。 

然而，请注意，即使在使用上述选项时，如果 IPv6 未被全局禁用， _networkd_ 仍会收到路由器通告。如果接口未接收到IPv6流量（例如，由于 sysctl 或 ip6tables 设置），它将保持在配置状态，并可能导致等待网络完全配置的服务超时。为了避免这种情况，还应在 `[Network]` 部分设置 `IPv6AcceptRA=no` 选项。 

##  参见

  * [IPv6](<https://docs.kernel.org/networking/ipv6.html>) — kernel.org documentation
  * [IPv6 temporary addresses](<https://www.ipsidixit.net/2012/08/09/ipv6-temporary-addresses-and-privacy-extensions/>) — a summary about temporary addresses and privacy extensions
  * [IPv6 prefixes](<https://mirrors.deepspace6.net/howtos/Linux+IPv6-HOWTO.html#AEN520>) — a summary of prefix types
  * [net.ipv6 options](<https://tldp.org/HOWTO/Linux+IPv6-HOWTO/ch11s02.html>) — documentation of kernel parameters
