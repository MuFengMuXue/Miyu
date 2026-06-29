**翻译状态：**

  * 本文（或部分内容）译自 [Uncomplicated Firewall](<https://wiki.archlinux.org/title/Uncomplicated_Firewall> "arch:Uncomplicated Firewall")，最近一次同步于 2025-08-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Uncomplicated_Firewall?diff=0&oldid=841350>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Uncomplicated_Firewall_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [iptables](<../zh-cn/Iptables.html> "Iptables")
  * [sshguard](<../zh-cn/Sshguard.html> "Sshguard")

来自项目[主页](<https://launchpad.net/ufw>)： 

    Ufw（即 Uncomplicated Firewall 的缩写）是一个管理网络[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")的程序。它提供了一个命令行界面，并旨在简单（uncomplicated）易用。

**注意：** 注意 UFW 可以使用 [iptables](<https://archlinux.org/packages/?name=iptables>)包 或 [nftables](<https://archlinux.org/packages/?name=nftables>)包 作为防火墙后端。此外，由于 `nft` 接受 iptables 语法（例如在 `/etc/ufw/before.rules` 中），因此使用 UFW 管理规则的用户无需学习怎么对 iptables 或者 nftables 进行底层调用。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [ufw](<https://archlinux.org/packages/?name=ufw>)包。 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `ufw.service` 使其开机自启。注意，如果 `iptables.service`（或者其 ipv6 部分）也被启用了，`ufw.service` 将不会生效。 

##  基本配置

以下是一个非常简单的配置示例，它将会默认拒绝所有连接，允许来自 192.168.0.1-192.168.0.255 局域网内的所有连接，允许所有目标为 [Deluge](</wzh/index.php?title=Deluge&action=edit&redlink=1> "Deluge（页面不存在）")（英语：[Deluge](<https://wiki.archlinux.org/title/Deluge> "en:Deluge")）（一个 BitTorrent 客户端）的连接，并启用了来自 _任何地方_ 的 SSH [连接速率限制](<#%E8%BF%9E%E6%8E%A5%E9%80%9F%E7%8E%87%E9%99%90%E5%88%B6>)： 
    
    # ufw default deny
    # ufw allow from 192.168.0.0/24
    # ufw allow Deluge
    # ufw limit ssh
    
要想允许一个端口而不是 _任何地方_ 进行连接，请参考下面的例子。这三条命令分别允许端口 51312 的 UDP 和 TCP 连接，允许端口 51313 的 UDP 连接，和允许范围从 51312 到 51314 端口的连接： 
    
    # ufw allow 51312
    # ufw allow 51312/udp
    # ufw allow 51312:51314
    
仅当首次安装后 _第一次使用_ UFW 时需要执行: 
    
    # ufw enable
    
**注意：** 请确保 `ufw.service` 已经被[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。

最后,使用以下命令确认更改已被应用: 
    
    # ufw status
    
    Status: active
    To                         Action      From
    --                         ------      ----
    Anywhere                   ALLOW       192.168.0.0/24
    Deluge                     ALLOW       Anywhere
    SSH                        LIMIT       Anywhere
    
**注意：** 状态报告仅限于用户添加的规则。在大多数情况下不会有什么问题，但最好还是了解一下内置规则是否存在。这些规则包括允许 UPNP、AVAHI 和 DHCP 回复的过滤器。具体信息请参考 [ufw README](<https://git.launchpad.net/ufw/tree/README>) 的“Default ruleset”一节。

使用以下命令来查看额外信息（包括默认策略）： 
    
    # ufw status verbose
    
但这依然限制于用户指定的规则。为了查看所有设置的规则，可以使用： 
    
    # ufw show raw
    
或者手册中列出的其他报告。由于这些报告也总结了流量情况，其输出有些难以阅读，为了方便阅读，你可以使用另一种检查传入流量的方法： 
    
    # iptables -S | grep ACCEPT
    # ip6tables -S | grep ACCEPT
    
请注意，只要你还在使用 `ufw` 来管理 `iptables`，就不要将后者[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。 

**注意：** 如果你在 `/etc/sysctl.d/*` 中设置了特殊的网络环境变量，请相应更新 `/etc/ufw/sysctl.conf` 中的内容（因为此配置会覆盖默认配置）。

##  转发策略

如果你需要使用 [VPN](<../zh-cn/Category:VPN.html> "VPN")（例如 [OpenVPN](<../zh-cn/OpenVPN.html> "OpenVPN") 或 [WireGuard](<../zh-cn/WireGuard.html> "WireGuard")），可以将 `/etc/default/ufw` 中的 **DEFAULT_FORWARD_POLICY** 变量从 **"DROP"** 调整到 **"ACCEPT"** ，以便无论用户如何设置如何都能转发所有数据包。要针对特定接口（例如 **wg0** ）进行转发，用户可以在 ***filter** 块中添加以下行： 
    
    /etc/ufw/before.rules
    
    # End required lines 
    
    -A ufw-before-forward -i wg0 -j ACCEPT
    -A ufw-before-forward -o wg0 -j ACCEPT
    
你可能还需要取消以下行的注释： 
    
    /etc/ufw/sysctl.conf
    
    net/ipv4/ip_forward=1
    net/ipv6/conf/default/forwarding=1
    net/ipv6/conf/all/forwarding=1

##  添加其他应用

软件包还提供了一些常见守护进程和程序的默认端口配置。可以通过查看 `/etc/ufw/applications.d` 目录下的文件或使用如下指令查看： 
    
    # ufw app list
    
如果用户正在使用非标准端口运行任何应用程序，建议创建 `/etc/ufw/applications.d/custom` 文件，并按照默认配置做模板添加所需的数据。 

**警告：** 如果用户修改了任何由软件包提供的规则集，这些修改将在第一次更新 ufw 软件包时被覆盖。这就是为什么建议将自定义应用程序规则放在外面的原因！

例如，使用自定义的 TCP 端口范围 20202-20205 进行 deluge 下载： 
    
    [Deluge-my]
    title=Deluge
    description=Deluge BitTorrent client
    ports=20202:20205/tcp

如果需要为同一应用程序定义 TCP 和 UDP 端口，只需使用竖线进行分隔，如下所示：该应用程序打开 TCP 端口 10000-10002 和 UDP 端口 10003： 
    
    ports=10000:10002/tcp|10003/udp
    
还可以使用逗号来定义端口。此示例打开 TCP 端口 10000-10002（包括端口 10000 和 10002）以及 UDP 端口 10003 和 10009： 
    
    ports=10000:10002/tcp|10003,10009/udp
    
##  删除应用

根据上面的 Deluge/Deluge-my 示例，以下操作将删除标准的 Deluge 规则，并用上面示例中的 Deluge-my 规则替换它们： 
    
    # ufw delete allow Deluge
    # ufw allow Deluge-my
    
通过 status 指令查询结果： 
    
    # ufw status
    
    Status: active
    To                         Action      From
    --                         ------      ----
    Anywhere                   ALLOW       192.168.0.0/24
    SSH                        ALLOW       Anywhere
    Deluge-my                  ALLOW       Anywhere
    
##  IP地址黑名单

将 IP 地址添加到黑名单可能是一个可取的做法，可以简单地编辑 `/etc/ufw/before.rules` 文件，在文件底部在 "COMMIT" 的上方插入一个 iptables DROP 行来轻松实现。 
    
    /etc/ufw/before.rules
    
    ...
    ## blacklist section
    # block just 199.115.117.99
    -A ufw-before-input -s 199.115.117.99 -j DROP
    # block 184.105.*.*
    -A ufw-before-input -s 184.105.0.0/16 -j DROP
    
    # don't delete the 'COMMIT' line or these rules won't be processed
    COMMIT
    
##  连接速率限制

ufw 有能力拒绝来自在过去 30 秒内尝试建立 6 次或更多连接的 IP 地址的连接。用户应该考虑在 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 之类的服务中使用这个选项。 

利用上述基本配置，要启用速率限制，我们只需用 limit 参数替换 allow 参数。然后新规则将取代先前的规则。 
    
    # ufw limit SSH
    
    Rule updated
    
    # ufw status
    
    Status: active
    To                         Action      From
    --                         ------      ----
    Anywhere                   ALLOW       192.168.0.0/24
    SSH                        LIMIT       Anywhere
    Deluge-my                  ALLOW       Anywhere
    
##  用户规则

所有的用户规则都储存在 `etc/ufw/user.rules` 和 `etc/ufw/user6.rules` 中，分别用于 IPv4 与 IPv6。 

##  技巧和窍门

###  禁用远程 ping

在以下文件中将 `ACCEPT` 改为 `DROP`： 
    
    /etc/ufw/before.rules
    
    # ok icmp codes
    ...
    -A ufw-before-input -p icmp --icmp-type echo-request -j ACCEPT
    
如果你正在使用 IPv6, 请一同更改 `/etc/ufw/before6.rules` 中的规则。 

###  禁用 IPv6 处理

将 `/etc/default/ufw` 中的 `IPV6=yes` 改为 `IPV6=no`，然后重新加载规则（`ufw reload`）。这样会移除原有 IPv6 规则，并且不再生成新的 IPv6 规则。 

###  禁用 UFW 日志

禁用 UFW 日志可以让 UFW 停止填充内核（[dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg")）和消息日志： 
    
    # ufw logging off
    
###  UFW 与 Docker

Docker 在默认状态下会编写 iptables 规则并忽视 ufw 规则，这可能会造成一些安全隐患。一种解决方案是使用 <https://github.com/chaifeng/ufw-docker> 。 

**提示：** 你可以安装 [ufw-docker](<https://aur.archlinux.org/packages/ufw-docker/>)AUR，并通过执行 `ufw-docker install` 来自动修复 iptables 规则。这个脚本也能帮你管理 Docker 相关的 ufw 规则，详细参见 `ufw-docker help`。 

##  GUI 前端

如果你在使用 [KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma")，可以安装 [plasma-firewall](<https://archlinux.org/packages/?name=plasma-firewall>)包，然后直接在 _Wi-Fi & Networking > Firewall_ 中调整防火墙配置。 

### Gufw

[gufw](<https://archlinux.org/packages/?name=gufw>)包 是一个用于 Ufw 的 GTK 前端，旨在使 Linux 防火墙的管理尽可能简单易用。它具有常见端口和 p2p 应用程序的预设设置。其依赖于软件包 [python](<https://archlinux.org/packages/?name=python>)包，[ufw](<https://archlinux.org/packages/?name=ufw>)包 以及 GTK 支持。 

##  参考

  * [Ubuntu UFW 文档](<https://help.ubuntu.com/community/UFW>)
  * [ufw(8)](<https://man.archlinux.org/man/ufw.8>)
  * 使用 ipsets 为 ufw 添加屏蔽列表：<https://github.com/poddmo/ufw-blocklist>
