[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 翻译已经过期，请阅读英文页面中的内容。（在 [Talk:WireGuard#](<../zh-cn/Talk:WireGuard.html>) 中讨论）

相关文章

  * [Linux Containers/Using VPNs](</wzh/index.php?title=Linux_Containers/Using_VPNs&action=edit&redlink=1> "Linux Containers/Using VPNs（页面不存在）")

引用自 [WireGuard](<https://www.wireguard.com/>) 项目主页： 

    WireGuard 是一种极其简单但快速且现代的 VPN，它利用了最先进的加密技术。它的目标是比 IPsec 更快、更简单、更精简和更有用，同时避免令人头疼的问题。其旨在提供比 OpenVPN 更高的性能。WireGuard 被设计为在嵌入式接口和超级计算机等上运行的通用 VPN，适用于许多不同的环境。虽然最初仅支持 Linux，但现在可以跨平台（Windows、macOS、BSD、iOS、Android）广泛部署。

本文中的主要概念在 [WireGuard](<https://www.wireguard.com/>) 项目主页上有粗略的介绍。2019 年底以后，[Linux 内核](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e7096c131e5161fa3b8e52a650d7719d2857adfd>)中包含 WireGuard。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wireguard-tools](<https://archlinux.org/packages/?name=wireguard-tools>)包，其提供了用户空间实用程序。 

另外，如果 Peer 公钥可用，也可以借助其他网络管理器的 WireGuard 支持。详见[#持久化配置](<#%E6%8C%81%E4%B9%85%E5%8C%96%E9%85%8D%E7%BD%AE>)。 

###  图形客户端

  * **wireguird** — 一个运行在Linux上的GTK GUI WireGuard客户端

     <https://github.com/UnnoTed/wireguird> || [wireguird](<https://aur.archlinux.org/packages/wireguird/>)AUR

  * **wireguard-gui** — 一个使用nextauri制作的Wireguard Linux图形化客户端

     <https://github.com/0xle0ne/wireguard-gui> || [wireguard-gui-bin](<https://aur.archlinux.org/packages/wireguard-gui-bin/>)AUR

###  命令行工具

  * **wg_tool** — 用于管理服务器和用户 wireguard 配置的工具。

     <https://github.com/gene-git/wg_tool> || [wg_tool](<https://aur.archlinux.org/packages/wg_tool/>)AUR

  * **wg-client** — 一个同时具有图形化界面和命令行的Linux客户端

     <https://github.com/gene-git/wg-client> || [wg-client](<https://aur.archlinux.org/packages/wg-client/>)AUR

  * **wg2nd** — 将 WireGuard 配置从 [wg-quick(8)](<https://man.archlinux.org/man/wg-quick.8>) 格式转换为 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 兼容的配置的工具。

     <https://git.flu0r1ne.net/wg2nd/about> || [wg2nd](<https://aur.archlinux.org/packages/wg2nd/>)AUR

##  使用

以下命令展示了如何在两个对等节点之间建立一条使用以下设置的基本的隧道： 

| 外部（公共）地址  | 内部 IP 地址  | 端口   
---|---|---|---  
域名  | IPv4 地址  | IPv6 地址  | IPv4 地址  | IPv6 地址   
对等节点 A  |  | 198.51.100.101  | 2001:db8:a85b:70a:ffd4:ec1b:4650:a001  | 10.0.0.1/24  | fdc9:281f:04d7:9ee9::1/64  | UDP/51871   
对等节点 B  | peer-b.example  | 203.0.113.102  | 2001:db8:40f0:147a:80ad:3e88:f8e9:b002  | 10.0.0.2/24  | fdc9:281f:04d7:9ee9::2/64  | UDP/51902   
对等节点 C  |  |  _动态（不固定）_ |  _动态（不固定）_ | 10.0.0.3/24  | fdc9:281f:04d7:9ee9::3/64  | UDP/51993   
  
**提示：** 对等节点可使用相同的 UDP 端口。

外部地址应该已经存在。例如，如果 ICMP 回显请求未被阻止，则对等节点 A 应该能够通过 [ping](</wzh/index.php?title=Ping&action=edit&redlink=1> "Ping（页面不存在）") 通对等点 B 的公共 IP 地址，反之亦然。 

内部地址将是使用 [ip(8)](<https://man.archlinux.org/man/ip.8>) 实用程序手动创建或通过网络管理软件创建的新地址，这些地址将在新的 WireGuard 网络内部使用。以下示例使用 10.0.0.0/24 和 fdc9:281f:04d7:9ee9::/64 作为内部网络。 IP 地址中的 `/24` 和 `/64` 是 [CIDR](<https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation> "wikipedia:Classless Inter-Domain Routing")。 

###  生成密钥

为每个对等节点创建公钥和私钥。如果要连接很多节点，可以考虑 vanity keypair 个性化 Base64 编码的公钥字符串，参见[#Vanity keys](<#Vanity_keys>)。 

生成私钥： 
    
    $ (umask 0077; wg genkey > peer_A.key)
    
**注意：** 建议仅允许所有者读写。以上命令使用子 shell 临时改变 [umask](<../zh-cn/Umask.html> "Umask")，从而确保只有所有者可访问（有读写权限）。

生成公钥： 
    
    $ wg pubkey < peer_A.key > peer_A.pub
    
或者，一次性生成公钥和私钥： 
    
    $ wg genkey | (umask 0077 && tee peer_A.key) | wg pubkey > peer_A.pub
    
还可以生成预共享密钥，以添加一层额外的对称密钥加密技术，将其混合到现有的公钥加密技术中，以实现后量子抵抗。应为每个对等节点对生成预共享密钥，且不应重复使用。例如，三个互连的对等节点 A、B 和 C 将需要三个单独的预共享密钥，每个对等节点对一个。 

使用以下命令为每个对等节点对生成预共享密钥（确保也使用 `umask 0077`）： 
    
    $ wg genpsk > peer_A-peer_B.psk
    $ wg genpsk > peer_A-peer_C.psk
    $ wg genpsk > peer_B-peer_C.psk
    
#### Vanity keys

Currently, WireGuard does not support comments or attaching human-memorable names to keys. This makes identifying the key's owner difficult particularly when multiple keys are in use. One solution is to generate a public key that contains some familiar characters (perhaps the first few letters of the owner's name or of the hostname etc.), [wireguard-vanity-address](<https://aur.archlinux.org/packages/wireguard-vanity-address/>)AUR does this. 

For example: 
    
    $ wireguard-vanity-address --in 8 leslie
    
    searching for 'leslie' in pubkey[0..10], one of every 214748364 keys should match
    one core runs at 2.69e6 keys/s, CPU cores available: 16
    est yield: 5.0 seconds per key, 200.10e-3 keys/s
    hit Ctrl-C to stop
    private wEoVMj92P+E3fQXVf9IixWJqpCqcnP/4OfvrB1g3zmY=  public LEsliEny+aMcWcRbh8Qf414XsQHSBOAFk3TaEk/aSD0=
    private EAOwlGGqpHVbZ9ehaCspdBJt+lkMcCfkwiA5T5a4JFs=  public VlesLiEB5BFd//OD2ILKXviolfz+hodG6uZ+XjoalC8=
    private UDWG4VWI+RzAGzNSnlC+0X4d3nk9goWPs/NRC5tX524=  public 9lESlieIFOlJFV6dG7Omao2WS+amWgshDdBYn8ahRjo=

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 以下翻译已经过期，请阅读英文页面中的内容。（在 [Talk:WireGuard#](<../zh-cn/Talk:WireGuard.html>) 中讨论）

在 peer 上生成公钥和私钥： 
    
    $ wg genkey | tee privatekey | wg pubkey > publickey
    
下面的指令会演示如何以表中的配置建立一条两个 peer 之间的隧道 

| Peer A  | Peer B   
---|---|---  
公网地址  | 10.10.10.1/24  | 10.10.10.2/24   
内网地址  | 10.0.0.1/24  | 10.0.0.2/24   
wireguard 监听端口  | UDP/4857  | UDP/3981   
  
Peer 应当已经拥有公网地址。例如，peer A 应当能够通过 `ping 10.10.10.2` ping 通 peer B，反之亦然。内部地址是由下文 `ip` 命令创建的新地址，并且将在 WireGuard 网络中共享。IP地址中 `/24` 的含义详见 [CIDR](<https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation> "wikipedia:Classless Inter-Domain Routing")

###  Peer A 配置

这个 peer 将监听 UDP 端口 48574，通过将 peer B 的公钥与其内部和外部 IP 地址关联，接受来自 peer B 的连接。 
    
    # ip link add dev wg0 type wireguard
    # ip link set dev wg0 mtu 1420
    # ip addr add 10.0.0.1/24 dev wg0
    # wg set wg0 listen-port 4857 private-key ./privatekey
    # wg set wg0 peer [Peer B public key] persistent-keepalive 25 allowed-ips 10.0.0.2/32 endpoint 10.10.10.2:3981
    # ip link set wg0 up
    
`[Peer B public key]` 的格式应当如同 `EsnHH9m6RthHSs+sd9uM6eCHe/mMVFaRh93GYadDDnM=`。`allowed-ips` 是 peer A 能够向之发送流量的地址列表。`allowed-ips 0.0.0.0/0` 将允许向任意地址发送流量。 

###  Peer B 配置

如同 Peer A，只不过 wireguard 守护监听 UDP 端口 39814 并且只接受 peer A 的连接 
    
    # ip link add dev wg0 type wireguard
    # ip link set dev wg0 mtu 1420
    # ip addr add 10.0.0.2/24 dev wg0
    # wg set wg0 listen-port 3981 private-key ./privatekey
    # wg set wg0 peer [Peer A public key] persistent-keepalive 25 allowed-ips 10.0.0.1/32 endpoint 10.10.10.1:4857
    # ip link set wg0 up
    
###  基本检查

不带任何参数使用 wg 命令可以快速查看当前的配置。 

例如，当 peer A 配置好之后，我们可以看见它的身份和与之关联的 peers。 
    
     peer-a$ wg
     interface: wg0
       public key: UguPyBThx/+xMXeTbRYkKlP0Wh/QZT3vTLPOVaaXTD8=
       private key: (hidden)
       listening port: 4857
     
     peer: 9jalV3EEBnVXahro0pRMQ+cHlmjE33Slo9tddzCVtCw=
       endpoint: 10.10.10.2:3981
       allowed ips: 10.0.0.2/32
    
此时我们可以 ping 通隧道的另一端： 
    
     peer-a$ ping 10.0.0.2
    
###  配置持久化

配置可以通过 `showconf` 来保存 
    
    # wg showconf wg0 > /etc/wireguard/wg0.conf
    # wg setconf wg0 /etc/wireguard/wg0.conf
    
###  示例 peer 配置
    
    /etc/wireguard/wg0.conf
    
    [Interface]
    PrivateKey = [CLIENT PRIVATE KEY]
    MTU = 1420
    
    [Peer]
    PublicKey = [SERVER PUBLICKEY]
    AllowedIPs = 10.0.0.0/24, 10.123.45.0/24, 1234:4567:89ab::/48
    Endpoint = [SERVER ENDPOINT]:5182
    PersistentKeepalive = 25

##  配置一个 VPN 服务器

WireGuard 自带一个快速创建和销毁 VPN 服务器的工具，`wg-quick`。注意这里使用的配置文件不是一个能被 `wg setconf` 有效的配置文件，并且你可能至少要把 `eth0` 改成你实际使用的。 

###  服务器
    
    /etc/wireguard/wg0server.conf
    
    [Interface]
    Address = 10.0.0.1/24  # This is the virtual IP address, with the subnet mask we will use for the VPN
    PostUp   = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
    ListenPort = 5182
    PrivateKey = [SERVER PRIVATE KEY]
    MTU = 1420
    
    [Peer]
    PublicKey = [CLIENT PUBLIC KEY]
    AllowedIPs = 10.0.0.2/32  # 这表示客户端只有一个 IP。

要使 iptables 规则生效，启用 IPv4 转发： 
    
    # sysctl net.ipv4.ip_forward=1
    
永久保留这项改变，向 `/etc/sysctl.d/99-sysctl.conf` 添加 `net.ipv4.ip_forward = 1`。 

使用 `wg-quick up wg0server` 启用 Interface，`wg-quick down wg0server` 用以关闭 

###  客户端 (转发所有流量)
    
    /etc/wireguard/wg0.conf
    
    [Interface]
    Address = 10.0.0.2/24  # The client IP from wg0server.conf with the same subnet mask
    PrivateKey = [CLIENT PRIVATE KEY]
    DNS = 10.0.0.1
    MTU = 1420
    
    [Peer]
    PublicKey = [SERVER PUBLICKEY]
    AllowedIPs = 0.0.0.0/0, ::0/0
    Endpoint = [SERVER ENDPOINT]:5182
    PersistentKeepalive = 25

使用 `wg-quick up wg0` 来启用 Interface, 使用 `wg-quick down wg0` 来关闭。 

使用 `systemctl enable wg-quick@wg0` 来自动启动。 

如果你使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager"), 可能有必要启用 NetworkManager-wait-online.service `systemctl enable NetworkManager-wait-online.service`

或者你使用的是 systemd-networkd, 启用 systemd-networkd-wait-online.service `systemctl enable systemd-networkd-wait-online.service`

等待所有设备就绪再尝试 WireGuard 连接 

##  使用技巧

###  以加密的形式存储私钥

以加密的形式存储私钥可能是可以实现的，例如通过使用 [pass](<https://archlinux.org/packages/?name=pass>)包。只需将配置文件中[Interface]下的 PrivateKey 一行替换为。 
    
     PostUp = wg set %i private-key <(su user -c "export PASSWORD_STORE_DIR=/path/to/your/store/; pass WireGuard/private-keys/%i")
    
where user is your username. See the `wg-quick(8)` man page for more details. 

将其中的user替换成你的用户名。更多细节请参见 `wg-quick(8)` man 页面。 

##  疑难解答

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:WireGuard#](<../zh-cn/Talk:WireGuard.html>) 中讨论）

###  路由定期被重置

[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 用户应确保其[未管理](<../zh-cn/NetworkManager.html#%E5%BF%BD%E7%95%A5%E7%89%B9%E5%AE%9A%E8%AE%BE%E5%A4%87> "NetworkManager") WireGuard 接口。例如，创建以下配置文件： 
    
    /etc/NetworkManager/conf.d/unmanaged.conf
    
    [keyfile]
    unmanaged-devices=type:wireguard

###  DNS 无法解析

When tunneling all traffic through a WireGuard interface, the connection can become seemingly lost after a while or upon new connection. This could be caused by a [network manager](<../zh-cn/Network_manager.html> "Network manager") or [DHCP](</wzh/index.php?title=DHCP&action=edit&redlink=1> "DHCP（页面不存在）") client overwriting `/etc/resolv.conf`. 

By default _wg-quick_ uses _resolvconf_ to register new [DNS](</wzh/index.php?title=DNS&action=edit&redlink=1> "DNS（页面不存在）") entries (from the `DNS` keyword in the configuration file). This will cause issues with [network manager](<../zh-cn/Network_manager.html> "Network manager")s and [DHCP](</wzh/index.php?title=DHCP&action=edit&redlink=1> "DHCP（页面不存在）") clients that do not use _resolvconf_ , as they will overwrite `/etc/resolv.conf` thus removing the DNS servers added by wg-quick. 

The solution is to use networking software that supports [resolvconf](</wzh/index.php?title=Resolvconf&action=edit&redlink=1> "Resolvconf（页面不存在）"). 

**注意：** Users of [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") should make sure that [systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包 is [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")ed.

Users of [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") should know that it does not use resolvconf by default. It is recommended to use [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved"). If this is undesirable, [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [openresolv](<https://archlinux.org/packages/?name=openresolv>)包 and configure NetworkManager to use it: [NetworkManager#Use openresolv](<../zh-cn/NetworkManager.html#Use_openresolv> "NetworkManager"). 

###  MTU 过低

Due to too low MTU (lower than 1280), wg-quick may have failed to create the WireGuard interface. This can be solved by setting the MTU value in WireGuard configuration in Interface section on client. 
    
    foo.config
    
    [Interface]
    Address = 10.200.200.2/24
    MTU = 1420
    PrivateKey = _PEER_FOO_PRIVATE_KEY_
    DNS = 10.200.200.1

###  密钥长度或格式错误

To avoid the following error, put the key value in the configuration file and not the path to the key file. 
    
    # wg-quick up wg0
    
    [#] ip link add wg0 type wireguard
    [#] wg setconf wg0 /dev/fd/63
    Key is not the correct length or format: `_/path/example.key'_
    Configuration parsing error
    [#] ip link delete dev wg0
    
###  无法在 NAT 或防火墙后建立持久连接

By default, WireGuard peers remain silent while they do not need to communicate, so peers located behind a NAT and/or [firewall](</wzh/index.php?title=Firewall&action=edit&redlink=1> "Firewall（页面不存在）") may be unreachable from other peers until they reach out to other peers themselves (or the connection may time out). Adding `PersistentKeepalive = 25` to the `[Peer]` settings of a peer located behind a NAT and/or firewall can ensure that the connection remains open. 

To temporarily set the persistent-keepalive setting via command line, run the following command: 
    
    # wg set wg0 peer _public_key_ persistent-keepalive 25
    
###  循环路由

Adding the endpoint IP to the allowed IPs list, the kernel will attempt to send handshakes to said device binding, rather than using the original route. This results in failed handshake attempts. 

As a workaround, the correct route to the endpoint needs to be manually added using 
    
    # ip route add _endpoint_ip_ via _gateway_ dev _network_interface_
    
E.g. for peer B from above in a standard LAN setup: 
    
    # ip route add 203.0.113.102 via 192.168.0.1 dev eth0
    
To make this route persistent, the command can be added as `PostUp = ip route ...` to the `[Interface]` section of `wg0.conf`. However, on certain setups (e.g. using `wg-quick@.service` in combination with NetworkManager) this might fail on resume. Furthermore, this only works for a static network setup and fails if gateways or devices change (e.g. using Ethernet or Wi-Fi on a laptop). 

Using NetworkManager, a more flexible solution is to start WireGuard using a dispatcher script. As root, create 
    
    /etc/NetworkManager/dispatcher.d/50-wg0.sh
    
    #!/bin/sh
    case $2 in
      up)
        wg-quick up wg0
        ip route add <endpoint ip> via $IP4_GATEWAY dev $DEVICE_IP_IFACE
        ;;
      pre-down)
        wg-quick down wg0
        ;;
    esac

If not already running, start and enable `NetworkManager-dispatcher.service`. Also make sure that NetworkManager is not managing routes for `wg0`, see [#Routes are periodically reset](<#Routes_are_periodically_reset>). 

###  使用 systemd-networkd 时睡眠导致连接丢失

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")。**

**附注：** Might reach more people on the dedicated page.（在 [Talk:WireGuard#Merge proposal of Connection lost after sleep using systemd-networkd](<../zh-cn/Talk:WireGuard.html#Merge_proposal_of_Connection_lost_after_sleep_using_systemd-networkd> "Talk:WireGuard") 中讨论）

[systemd](<../zh-cn/Systemd.html> "Systemd") version 253 introduced a change in how network interfaces are reconfigured when resuming from a suspended state[[1]](<https://github.com/systemd/systemd/commit/a39a9ac8065c29330207838b70fe388bde2bc254>). In doing so, network connections managed by [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") will lose connection to the wireguard interface. Unless a kill switch is configured, this risks exposing the public IP address after resuming from suspend. To fix this, uncomment and change the value to `no` for `ManageForeignRoutingPolicyRules` in `/etc/systemd/networkd.conf`. [[2]](<https://github.com/systemd/systemd/issues/26665#issuecomment-1454353725>)

##  参见

  * [Wikipedia:WireGuard](<https://en.wikipedia.org/wiki/WireGuard> "wikipedia:WireGuard")
  * [Jason Donenfeld 的演讲](<https://www.wireguard.com/presentations/>)
  * [邮件列表](<https://lists.zx2c4.com/mailman/listinfo/wireguard>)
  * [非官方 WireGuard 文档](<https://docs.sweeting.me/s/wireguard>)
  * [Debian:Wireguard](<https://wiki.debian.org/Wireguard> "debian:Wireguard")
