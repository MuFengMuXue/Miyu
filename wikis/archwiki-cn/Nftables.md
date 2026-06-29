相关文章

  * [iptables](<../zh-cn/Iptables.html> "Iptables")
  * [Firewalld](<../zh-cn/Firewalld.html> "Firewalld")

**翻译状态：**

  * 本文（或部分内容）译自 [nftables](<https://wiki.archlinux.org/title/nftables> "arch:nftables")，最近一次同步于 2023-2-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/nftables?diff=0&oldid=766949>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/nftables_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[nftables](<https://netfilter.org/projects/nftables/>) 是一个网络过滤器项目，旨在替换现有的 {ip,ip6,arp,eb}tables 框架。它提供了一个新的数据包过滤框架、一个新的用户空间实用程序（nft）和一个针对 {ip,ip6}tables 的兼容层。它使用了现有的钩子、连接跟踪系统、用户空间队列组件和网络过滤器的日志子系统。 

它由三个主要组件组成：内核实现、libnl [网络链接](<https://en.wikipedia.org/wiki/Netlink> "wikipedia:Netlink")通信和 nftables 用户空间前端。 内核提供了一个网络链接配置接口，以及运行时规则集计算，libnl 包含用于与内核通信的底层函数，nftables 前端供用户通过 nft 进行交互。 

你也可以访问[官方 nftables wiki 页](<https://wiki.nftables.org/wiki-nftables/index.php/Main_Page>)获取更多信息。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")用户空间实用程序包 [nftables](<https://archlinux.org/packages/?name=nftables>)包 或 git 版本 [nftables-git](<https://aur.archlinux.org/packages/nftables-git/>)AUR。 

或者，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包，它将 [nftables](<https://archlinux.org/packages/?name=nftables>)包 作为一个依赖项，将自动卸载 [iptables](<https://archlinux.org/packages/?name=iptables>)包（[base](<https://archlinux.org/packages/?name=base>)包[元包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包和软件包组")的间接依赖项），并在一起使用时防止 [iptables](<https://archlinux.org/packages/?name=iptables>)包 和 [nftables](<https://archlinux.org/packages/?name=nftables>)包 之间的冲突。 

**提示：** 大多数 [iptables 前端](<../zh-cn/Iptables.html#%E5%89%8D%E7%AB%AF> "Iptables")都不直接或间接支持 nftables，但可能会引入它。[[1]](<https://www.spinics.net/lists/netfilter/msg58215.html>) 一个同时支持 nftables 和 iptables 的图形前端是 [firewalld](<../zh-cn/Firewalld.html> "Firewalld")。[[2]](<https://firewalld.org/2018/07/nftables-backend>)

###  前端

  * **[firewalld](<../zh-cn/Firewalld.html> "Firewalld") (firewall-cmd)** — 用于配置网络和防火墙域以及建立和配置防火墙规则的守护进程和控制台界面。

     <https://firewalld.org/> || [firewalld](<https://archlinux.org/packages/?name=firewalld>)包

  * **nft-blackhole** — 脚本/守护进程可以按国家和黑名单阻止 nftables 中的 IP。

     <https://github.com/tomasz-c/nft-blackhole> || [nft-blackhole](<https://aur.archlinux.org/packages/nft-blackhole/>)AUR

  * **[ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw")** — Ufw（即 Uncomplicated Firewall 的缩写）是一个管理网络防火墙的程序。它提供了一个命令行界面，旨在简单（uncomplicated）易用。

     <https://launchpad.net/ufw> || [ufw](<https://archlinux.org/packages/?name=ufw>)包

##  用法

**提示：** 如果你已经拥有 iptables 规则，那么可以将 iptables 规则转换为 nftables 规则，参见[[3]](<https://wiki.nftables.org/wiki-nftables/index.php/Moving_from_iptables_to_nftables>)。

**nftables** **不** 区分命令行中制作的临时规则和从文件加载或保存到文件中的永久规则。 

所有规则都必须使用 `nft` 命令行工具创建或加载。 

请参考 [#配置](<#%E9%85%8D%E7%BD%AE>)章节了解如何使用。 

可以打印当前规则集： 
    
    # nft list ruleset
    
删除所有规则集，使系统没有防火墙： 
    
    # nft flush ruleset
    
通过[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `nftables.service` 从 `/etc/nftables.conf` 读取规则集。 

###  简单的防火墙

[nftables](<https://archlinux.org/packages/?name=nftables>)包 附带了一个简单而安全的防火墙配置，存储在 `/etc/nftables.conf` 文件中。 

`nftables.service` 将在[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")时从该文件加载规则。 

##  配置

nftables 的用户空间实用程序 `nft` 在将规则集传递给内核之前执行大多数规则集评估。规则存储在链中，而链又存储在表中。以下部分说明如何创建和修改这些构件。 

要从文件读取输入，请使用 `-f`/`--file` 选项： 
    
    # nft --file _文件名_
    
请注意，任何已加载的规则都**不会** 自动刷新。 

有关所有命令的完整列表，请参见 [nft(8)](<https://man.archlinux.org/man/nft.8>)。 

###  表

表包含[#链](<#%E9%93%BE>)。与 iptables 中的表不同，nftables 中没有内置表。表的数量及其名称由用户决定。不过，每个表只有一个地址族，并且仅适用于该族的数据包。表可以指定五个族之一： 

nftables 族 | iptables 实用程序   
---|---  
ip | iptables   
ip6 | ip6tables   
inet | iptables 和 ip6tables   
arp | arptables   
bridge | ebtables   
  
`ip`（即 IPv4）是默认族，如果未指定族，则将使用该族。 

要创建同时适用于 IPv4 和 IPv6 的规则，请使用 `inet`。`inet` 允许统一 `ip` 和 `ip6` 族，从而使同时定义两者的规则更加容易。 

参见 [nft(8) § ADDRESS FAMILIES](<https://man.archlinux.org/man/nft.8#ADDRESS_FAMILIES>) 获得关于地址族的完整描述。 

在以下所有示例中，` _族类型_` 是可选的，如果未指定，则设置为 `ip`。 

####  创建表

以下示例添加一个新表： 
    
    # nft add table _族类型_ _表名_
    
####  列出表

要列出所有表： 
    
    # nft list tables
    
####  列出表中的链和规则

要列出指定表的所有链和规则，请执行： 
    
    # nft list table _族类型_ _表名_
    
例如，要列出 `inet` 族的 `my_table` 表的所有规则： 
    
    # nft list table inet my_table
    
####  删除表

要删除一个表，请执行： 
    
    # nft delete table _族类型_ _表名_
    
这会销毁表中的所有链。 

####  刷新表

要刷新来自表的所有规则，请执行： 
    
    # nft flush table _族类型_ _表名_
    
###  链

链的用途是包含[#规则](<#%E8%A7%84%E5%88%99>)。与 iptables 中的链不同，nftables 中没有内置链。这意味着，如果没有链在网络过滤器框架中使用任何类型或钩子，则与 iptables 不同，nftables 将不会触及流经这些链的数据包。 

链有两种类型。 _基本_ 链是来自网络堆栈的数据包的入口点，其中指定了一个钩子值。为了更好地组织，可以使用 _常规_ 链作为跳转目标。 

在以下所有示例中 `_族类型_` 都是可选的，如果未指定则设为 `ip`。 

####  创建链

#####  基本链

要添加基本链，请指定钩子和优先级值： 
    
    # nft add chain _族类型_ _表名_ _链名_ '{ type _链类型_ hook _钩子类型_ priority _优先级值_ ; }'
    
`_链类型_` 可以是 `filter`, `route`, 或 `nat`。 

对于 IPv4/IPv6/Inet 地址族，` _钩子类型_` 可以是 `prerouting`, `input`, `forward`, `output`, 或 `postrouting`。见 [nft(8) § ADDRESS FAMILIES](<https://man.archlinux.org/man/nft.8#ADDRESS_FAMILIES>) 获取其他族的钩子列表。 

`_优先级值_` 采用优先级名称或整数值。见 [nft(8) § CHAINS](<https://man.archlinux.org/man/nft.8#CHAINS>) 获取标准优先级名称和值的列表。数字较低的链首先被处理，并且可以是负数。[[4]](<https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Base_chain_types>)

例如，要添加过滤输入数据包的基本链： 
    
    # nft add chain inet my_table my_chain '{ type filter hook input priority 0; }'
    
在上述任意情况中用 `create` 替换 `add` 以添加新链，但如果该链已经存在，则返回错误。 

#####  常规链

下面将常规链 `_链名_` 添加到表 `_表名_` 中： 
    
    # nft add chain _族类型_ _表名_ _链名_
    
例如，要将名为 `my_tcp_chain` 的常规链添加到 `inet` 地址族的 `my_table` 表，请执行： 
    
    # nft add chain inet my_table my_tcp_chain
    
####  列出规则

下面列出链的所有规则： 
    
    # nft list chain _族类型_ _表名_ _链名_
    
例如，下面列出名为 `my_table` 的 `inet` 表中名为 `my_output` 的链的规则： 
    
    # nft list chain inet my_table my_output
    
####  编辑链

要编辑链，只需按其名称调用它并定义要更改的规则。 
    
    # nft chain _族类型 表名 链名_ '{ [ type _链类型_ hook _钩子类型_ device _设备名_ priority _优先级值_ ; policy _策略类型_ ; ] }'
    
例如，要将 `my_table` 表的 `my_input` 链策略从 `accept` 更改为 `drop`
    
    # nft chain inet my_table my_input '{ policy drop ; }'
    
####  删除链

要删除一个链，请执行： 
    
    # nft delete chain _族类型_ _表名_ _链名_
    
链不能包含任何规则或是跳转目标。 

####  刷新来自链的规则

要刷新来自链的规则，请执行： 
    
    # nft flush chain _族类型_ _表名_ _链名_
    
###  规则

规则由表达式或语句构成，并包含在链中。 

####  添加规则

要向链添加规则，请执行： 
    
    # nft add rule _族类型_ _表名_ _链名_ handle _句柄值_ _语句_
    
规则附加在 `_句柄值_` 处，这是可选的。如果未指定，规则将附加到链的末端。 

应当用可以添加到任何有效列表命令的 `--handle` 开关确定规则句柄。此开关告诉 `nft` 在其输出中列出句柄。 `--numeric` 参数用于查看某些数值输出，如未解析的 IP 地址。 
    
    # nft --handle --numeric list chain inet my_table my_input
    
    table inet my_table {
         chain input {
              type filter hook input priority 0;
              ip saddr 127.0.0.1 accept # handle 10
         }
    }
    
要将规则添加到指定位置，请执行： 
    
    # nft insert rule _族类型_ _表名_ _链名_ handle _句柄值_ _语句_
    
如果未指定 `_句柄值_`，则规则将附加到链的开头。 

#####  表达式

通常，一个 `_语句_` 包括一些要匹配的表达式，然后是一个判断语句。判断语句包括 `accept`, `drop`, `queue`, `continue`, `return`, `jump _链名_`, 和 `goto _链名_`。存在判断语句以外的其他语句。有关详细信息，见 [nft(8)](<https://man.archlinux.org/man/nft.8>)。 

nftables 中有各种可用的表达式，并且在很大程度上与 iptables 对应的表达式一致。最明显的区别是没有通用或隐式匹配。通用匹配总是可用的，例如 `--protocol` 或 `--source`。隐式匹配是特定于协议的，例如，当数据包被确定为 TCP 时，即为 `--sport`。 

以下是可用匹配项的不完整列表： 

  * meta (元属性，例如 interfaces)
  * icmp (ICMP 协议)
  * icmpv6 (ICMPv6 协议)
  * ip (IP 协议)
  * ip6 (IPv6 协议)
  * tcp (TCP 协议)
  * udp (UDP 协议)
  * sctp (SCTP 协议)
  * ct (连接跟踪)

以下是匹配参数的不完整列表（有关更完整的列表，见 [nft(8)](<https://man.archlinux.org/man/nft.8>)）： 
    
    meta:
      oif <output interface INDEX>
      iif <input interface INDEX>
      oifname <output interface NAME>
      iifname <input interface NAME>
    
      （oif 和 iif 接受字符串参数并转换为接口索引）
      （oifname 和 iifname 更动态，但由于字符串匹配，速度较慢）
    
    icmp:
      type <icmp type>
    
    icmpv6:
      type <icmpv6 type>
    
    ip:
      protocol <protocol>
      daddr <destination address>
      saddr <source address>
    
    ip6:
      daddr <destination address>
      saddr <source address>
    
    tcp:
      dport <destination port>
      sport <source port>
    
    udp:
      dport <destination port>
      sport <source port>
    
    sctp:
      dport <destination port>
      sport <source port>
    
    ct:
      state <new | established | related | invalid>
    
####  删除

单个规则只能通过其句柄删除。获取句柄在[#添加规则](<#%E6%B7%BB%E5%8A%A0%E8%A7%84%E5%88%99>)中展示。假设 
    
    # nft --handle --numeric list chain inet my_table my_input
    
    table inet my_table {
         chain input {
              type filter hook input priority 0;
              ip saddr 127.0.0.1 accept # handle 10
         }
    }
    
    # nft delete rule inet my_table my_input handle 10
    
删去它。 

可以使用 `nft flush table` 命令刷新表中的所有链。使用 `nft flush chain` 或 `nft delete rule` 命令可以刷新单个链。 
    
    # nft flush table _表名_
    # nft flush chain _族类型_ _表名_ _链名_
    # nft delete rule _族类型_ _表名_ _链名_
    
第一个命令刷新 ip `_表名_` 表中的所有链。第二个刷新 `_族类型_` `_表名_` 表中的 `_链名_` 链。第三个删除 `_族类型_` `_表名_` 表中 `_链名_` 链中的所有规则。 

###  集

[集是命名的或匿名的](<https://wiki.nftables.org/wiki-nftables/index.php/Sets>)，由一个或多个元素组成，用逗号分隔，用大括号括起来。匿名集嵌入到规则中，无法更新，必须删除并重新添加规则。例如，下面您不能从 dports 的匿名集中只删除 “http”： 
    
    # nft add rule ip6 filter input tcp dport {telnet, http, https} accept
    
命名集可以被更新，并且可以被类型化和标记。 _sshguard_ 为被阻止主机的 IP 地址使用命名集。 
    
    table ip sshguard {
           set attackers {
                   type ipv4_addr
                   flags interval
                   elements = { 1.2.3.4 }
           }
    
要从该集 _添加（add）_ 或 _删除（delete）_ 元素（element），使用： 
    
    # nft add element ip sshguard attackers { 5.6.7.8/32 }
    # nft delete element ip sshguard attackers { 1.2.3.4/32 }
    
注意， _ipv4_addr_ 类型可以包含 CIDR 网络掩码（此处的 “/32” 不是必需的，但为了完整起见，包含了它）。此外请注意，这里由 “TABLE ip sshguard { SET attackers }” 定义的集被称为 `ip sshguard attackers`。 

###  原子重载

刷新当前规则集： 
    
    # echo "flush ruleset" > /tmp/nftables 
    
转储当前规则集： 
    
    # nft -s list ruleset >> /tmp/nftables
    
现在，您可以编辑 `/tmp/nftables` 并通过以下方式应用更改： 
    
    # nft -f /tmp/nftables
    
##  示例

###  工作站
    
    /etc/nftables.conf
    
    flush ruleset
    
    table inet my_table {
    	set LANv4 {
    		type ipv4_addr
    		flags interval
    
    		elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
    	}
    	set LANv6 {
    		type ipv6_addr
    		flags interval
    
    		elements = { fd00::/8, fe80::/10 }
    	}
    
    	chain my_input_lan {
    		udp sport 1900 udp dport >= 1024 meta pkttype unicast limit rate 4/second burst 20 packets accept comment "接受 UPnP IGD 端口映射回复"
    
    		udp sport netbios-ns udp dport >= 1024 meta pkttype unicast accept comment "接受 Samba Workgroup 浏览回复"
    
    	}
    
    	chain my_input {
    		type filter hook input priority filter; policy drop;
    
    		iif lo accept comment "接受所有本机流量"
    		ct state invalid drop comment "丢弃无效连接"
    		ct state established,related accept comment "接受来自我们（us）的流量"
    
    		meta l4proto ipv6-icmp accept comment "接受 ICMPv6"
    		meta l4proto icmp accept comment "接受 ICMP"
    		ip protocol igmp accept comment "接受 IGMP"
    
    		udp dport mdns ip6 daddr ff02::fb accept comment "接受 mDNS"
    		udp dport mdns ip daddr 224.0.0.251 accept comment "接受 mDNS"
    
    		ip6 saddr @LANv6 jump my_input_lan comment "来自专用 IP 地址范围的连接"
    		ip saddr @LANv4 jump my_input_lan comment "来自专用 IP 地址范围的连接"
    
    		counter comment "统计任何其他流量"
    	}
    
    	chain my_forward {
    		type filter hook forward priority filter; policy drop;
    		# 丢弃转发给我们的所有内容。我们不转发。这是路由器的工作。
    	}
    
    	chain my_output {
    		type filter hook output priority filter; policy accept;
    		# 接受每个出站连接
    	}
    
    }
    
###  服务器
    
    /etc/nftables.conf
    
    flush ruleset
    
    table inet my_table {
    	set LANv4 {
    		type ipv4_addr
    		flags interval
    
    		elements = { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16 }
    	}
    	set LANv6 {
    		type ipv6_addr
    		flags interval
    
    		elements = { fd00::/8, fe80::/10 }
    	}
    
    	chain my_input_lan {
    		meta l4proto { tcp, udp } th dport 2049 accept comment "接受 NFS"
    
    		udp dport netbios-ns accept comment "接受 NetBIOS 名称服务 (nmbd)"
    		udp dport netbios-dgm accept comment "接受 NetBIOS 数据报服务 (nmbd)"
    		tcp dport netbios-ssn accept comment "接受 NetBIOS 会话服务 (smbd)"
    		tcp dport microsoft-ds accept comment "接受 Microsoft 目录服务 (smbd)"
    
    		udp sport { bootpc, 4011 } udp dport { bootps, 4011 } accept comment "接受 PXE"
    		udp dport tftp accept comment "接受 TFTP"
    	}
    
    	chain my_input {
    		type filter hook input priority filter; policy drop;
    
    		iif lo accept comment "接受所有本机流量"
    		ct state invalid drop comment "丢弃无效链接"
    		ct state established,related accept comment "接受来自我们（us）的流量"
    
    		meta l4proto ipv6-icmp accept comment "接受 ICMPv6"
    		meta l4proto icmp accept comment "接受 ICMP"
    		ip protocol igmp accept comment "接受 IGMP"
    
    		udp dport mdns ip6 daddr ff02::fb accept comment "接受 mDNS"
    		udp dport mdns ip daddr 224.0.0.251 accept comment "接受 mDNS"
    
    		ip6 saddr @LANv6 jump my_input_lan comment "来自专用 IP 地址范围的连接"
    		ip saddr @LANv4 jump my_input_lan comment "来自专用 IP 地址范围的连接"
    
    		tcp dport ssh accept comment "在 端口 22 上接受 SSH"
    
    		tcp dport ipp accept comment "在端口 631 上接受 IPP/IPPS"
    
    		tcp dport { http, https, 8008, 8080 } accept comment "接受 HTTP (端口 80, 443, 8008, 8080)"
    
    		udp sport bootpc udp dport bootps ip saddr 0.0.0.0 ip daddr 255.255.255.255 accept comment "接受 DHCPDISCOVER (对于 DHCP-Proxy)"
    	}
    
    	chain my_forward {
    		type filter hook forward priority filter; policy drop;
    		# 丢弃转发给我们的所有内容。我们不转发。这是路由器的工作。
    	}
    
    	chain my_output {
    		type filter hook output priority filter; policy accept;
    		# 接受每个出站连接
    	}
    
    }
    
###  限速
    
    table inet my_table {
    	chain my_input {
    		type filter hook input priority filter; policy drop;
    
    		iif lo accept comment "接受所有本机流量"
    		ct state invalid drop comment "丢弃无效链接"
    
    		meta l4proto icmp icmp type echo-request limit rate over 10/second burst 4 packets drop comment "无 ping 洪流"
    		meta l4proto ipv6-icmp icmpv6 type echo-request limit rate over 10/second burst 4 packets drop comment "无 ping 洪流"
    
    		ct state established,related accept comment "接受来自我们（us）的流量"
    
    		meta l4proto ipv6-icmp icmpv6 type { destination-unreachable, packet-too-big, time-exceeded, echo-reply, parameter-problem, mld-listener-query, mld-listener-report, mld-listener-reduction, nd-router-solicit, nd-router-advert, nd-neighbor-solicit, nd-neighbor-advert, ind-neighbor-solicit, ind-neighbor-advert, mld2-listener-report } accept comment "接受 ICMPv6"
    		meta l4proto icmp icmp type { destination-unreachable, router-solicitation, router-advertisement, time-exceeded, parameter-problem } accept comment "接受 ICMP"
    		ip protocol igmp accept comment "接受 IGMP"
    
    		tcp dport ssh ct state new limit rate 15/minute accept comment "避免在 SSH 上使用暴力破解"
    
    	}
    
    }
    
###  跳转（Jump）

在配置文件中使用跳转时，必须首先定义目标链。否则可能会出现 `Error: Could not process rule: No such file or directory`。 
    
    table inet my_table {
        chain web {
            tcp dport http accept
            tcp dport 8080 accept
        }
        chain my_input {
            type filter hook input priority filter;
            ip saddr 10.0.2.0/24 jump web
            drop
        }
    }
    
###  不同接口的不同规则

如果您的机箱有多个网络接口，并且您希望对不同的接口使用不同的规则，那么您可能需要使用 “分派（dispatching）” 过滤器链，然后使用特定于接口的过滤器链。例如，假设您的机箱充当家庭路由器，您希望运行可通过 LAN 访问的网络服务器（接口 `enp3s0`），但不能从公共网络访问（接口 `enp2s0`）。您可能需要考虑这样的结构： 
    
    table inet my_table {
      chain my_input { # 该链充当分派器
        type filter hook input priority filter;
    
        iif lo accept comment "始终接受环回"
        iifname enp2s0 jump my_input_public
        iifname enp3s0 jump my_input_private
    
        reject with icmpx port-unreachable comment "拒绝来自所有其他接口的流量"
      }
      chain my_input_public { # 适用于公共接口界面的规则
        ct state {established,related} accept
        ct state invalid drop
        udp dport bootpc accept
        tcp dport bootpc accept
        reject with icmpx port-unreachable comment "所有其它流量"
      }
      chain my_input_private {
        ct state {established,related} accept
        ct state invalid drop
        udp dport bootpc accept
        tcp dport bootpc accept
        tcp port http accept
        tcp port https accept
        reject with icmpx port-unreachable comment "所有其它流量"
      }
      chain my_output { # 我们把一切都放出来
        type filter hook output priority filter;
        accept
      }
    }
    
或者，您可以只选择一个 `iifname` 语句，例如针对单个上游接口，并将所有其他接口的默认规则放在一个位置，而不是为每个接口分派。 

###  伪装（Masquerading）

nftables 有一个特别的关键字 `masquerade`“其中源地址被自动设为输出接口的地址”（[来源](<https://wiki.nftables.org/wiki-nftables/index.php/Performing_Network_Address_Translation_%28NAT%29#Masquerading>)）。这对于接口的 IP 地址不可预测或不稳定的情况尤其有用，例如连接到许多 ISP 的路由器的上游接口。如果没有它，每次接口的 IP 地址更改时都必须更新网络地址转换规则。 

要使用它： 

  * 确保在内核中启用伪装（如果使用默认内核，则已启用），否则请在内核配置期间，设置 `CONFIG_NFT_MASQ=m`。
  * `masquerade` 关键字只能在 `nat` 类型的链中使用。
  * 伪装是一种源网络地址转换（NAT），因此只在输出路径中工作。

具有两个接口的机器示例：LAN 连接到 `enp3s0`，公共网络连接到 `enp2s0`： 
    
    table inet my_nat {
      chain my_masquerade {
        type nat hook postrouting priority srcnat;
        oifname "enp2s0" masquerade
      }
    }
    
由于表类型为 `inet`，IPv4 和 IPv6 数据包都将被伪装。如果您只希望 ipv4 数据包被伪装（因为 IPv6 的额外地址空间不需要 NAT），可以在 `oifname "enp2s0"` 前面使用 `meta nfproto ipv4` 表达式，或者可以将表类型更改为 `ip`。 

###  带端口转发的 NAT

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** I think `my_postrouting` chain will cause the destination computer see that connections are made by router rather than from some global IP. Also this does not masquerade outbound traffic.（在 [Talk:Nftables](<../zh-cn/Talk:Nftables.html>) 中讨论）

此示例将端口22和80转发到 `_destination_ip_`。您需要通过 [sysctl](<../zh-cn/Sysctl.html> "Sysctl") 将 `net.ipv4.ip_forward` 和 `net.ipv4.conf._wan_interface_.forwarding` 设置为 `1`。 
    
    table ip my_nat {
      chain my_prerouting {
        type nat hook prerouting priority dstnat;
    
        tcp dport { ssh, http } dnat to _destination_ip_
      }
    
      chain my_postrouting {
        type nat hook postrouting priority srcnat;
    
        ip daddr _destination_ip_ masquerade
      }
    }
    
###  计算每个 IP 的新连接数

使用此代码段计算 HTTPS 连接数： 
    
    /etc/nftables.conf
    
    table inet filter {
        set https {
            type ipv4_addr;
            flags dynamic;
            size 65536;
            timeout 60m;
        }
    
        chain input {
            type filter hook input priority filter;
            ct state new tcp dport 443 update @https { ip saddr counter }
        }
    }
    
要打印计数器，请运行 `nft list set inet filter https`。 

###  动态黑洞

使用此代码段可以在1分钟内从超过 10/秒 限制的源 IP 断开所有 HTTPS 连接。 
    
    /etc/nftables.conf
    
    table inet dev {
        set blackhole {
            type ipv4_addr;
            flags dynamic, timeout;
            size 65536;
        }
    
        chain input {
            ct state new tcp dport 443 \
                    meter flood size 128000 { ip saddr timeout 10s limit rate over 10/second } \
                    add @blackhole { ip saddr timeout 1m }
    
            ip saddr @blackhole counter drop
        }
    }
    
要打印黑洞的 IP，请运行 `nft list set inet dev blackhole`。 

##  提示和技巧

###  保存当前规则集

`nft list ruleset` 命令的输出也是它的有效输入文件。当前规则集可以保存到文件中，稍后再加载回。 
    
    $ nft -s list ruleset | tee _filename_
    
**注意：**`nft list` 不输出变量定义，如果原始文件中有任何变量定义，它们将丢失。规则中使用的任何变量都将被其值替换。

###  简单的状态防火墙

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 这不是一个非常简单的防火墙。我认为 Arch Linux 在 /etc/nftables.conf 中提供的内容很简单。建议用该脚本替换此部分，并给出如何根据特定需要扩展该部分的一些指导。（在 [Talk:Nftables](<../zh-cn/Talk:Nftables.html>) 中讨论）

见 [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall") 获取更多信息。 

####  单机

刷新当前规则集： 
    
    # nft flush ruleset
    
添加一个表： 
    
    # nft add table inet my_table
    
添加输入（input）、转发（forward）和输出（output）基本链。输入和转发的策略将是丢弃。输出的策略是接受。 
    
    # nft add chain inet my_table my_input '{ type filter hook input priority 0 ; policy drop ; }'
    # nft add chain inet my_table my_forward '{ type filter hook forward priority 0 ; policy drop ; }'
    # nft add chain inet my_table my_output '{ type filter hook output priority 0 ; policy accept ; }'
    
添加两个将与 tcp 和 udp 关联的常规链： 
    
    # nft add chain inet my_table my_tcp_chain
    # nft add chain inet my_table my_udp_chain
    
将接受相关（related）和已建立（established）的流量： 
    
    # nft add rule inet my_table my_input ct state related,established accept
    
将接受所有环回接口流量： 
    
    # nft add rule inet my_table my_input iif lo accept
    
丢弃所有无效流量： 
    
    # nft add rule inet my_table my_input ct state invalid drop
    
接受 ICMP 和 IGMP： 
    
    # nft add rule inet my_table my_input meta l4proto ipv6-icmp accept
    # nft add rule inet my_table my_input meta l4proto icmp accept
    # nft add rule inet my_table my_input ip protocol igmp accept
    
新的 udp 流量将跳转到 UDP 链： 
    
    # nft add rule inet my_table my_input meta l4proto udp ct state new jump my_udp_chain
    
新的 tcp 流量将跳转到 TCP 链： 
    
    # nft add rule inet my_table my_input 'meta l4proto tcp tcp flags & (fin|syn|rst|ack) == syn ct state new jump my_tcp_chain'
    
拒绝其他规则未处理的所有流量： 
    
    # nft add rule inet my_table my_input meta l4proto udp reject
    # nft add rule inet my_table my_input meta l4proto tcp reject with tcp reset
    # nft add rule inet my_table my_input counter reject with icmpx port-unreachable
    
此时，您应该决定要向传入连接打开哪些端口，这些端口由 TCP 和 UDP 链处理。例如，要打开网络服务器的连接，请添加： 
    
    # nft add rule inet my_table my_tcp_chain tcp dport 80 accept
    
要接受网络服务器的 HTTPS 连接在端口 443： 
    
    # nft add rule inet my_table my_tcp_chain tcp dport 443 accept
    
要接受 SSH 流量在端口 22： 
    
    # nft add rule inet my_table my_tcp_chain tcp dport 22 accept
    
要接受传入的DNS请求： 
    
    # nft add rule inet my_table my_tcp_chain tcp dport 53 accept
    # nft add rule inet my_table my_udp_chain udp dport 53 accept
    
确保在满意后使您的更改永久化。 

###  防止暴力攻击

[Sshguard](<../zh-cn/Sshguard.html> "Sshguard") 是个程序，它可以检测暴力攻击，并根据临时列入黑名单的 IP 地址修改防火墙。见 [Sshguard#nftables](<../zh-cn/Sshguard.html#nftables> "Sshguard") 了解如何设置与之一起使用的 nftables。 

###  记录流量

你可以使用 `log` 操作记录数据包。记录所有传入流量的最简单规则是： 
    
    # nft add rule inet filter input log
    
见 [nftables wiki](<https://wiki.nftables.org/wiki-nftables/index.php/Logging_traffic>) 获取详情。 

##  故障排除

###  与 Docker 一起工作

**注意：**

  * 使用以下设置，即使具有 `--net host --privileged`，您也无法在容器内使用 `AF_BLUETOOTH` 等协议。
  * 无根 Docker 容器已经在单独的网络命名空间中运行。你可能不需要做任何事情。

使用 nftables 可能会干扰 [Docker](<../zh-cn/Docker.html> "Docker") 网络（以及其他容器运行时）。您可以在互联网上找到各种解决方案，其中包括修补 iptables 规则并确保定义的服务启动顺序，或者完全禁用 dockers iptables 管理，这使得使用 docker 非常受限（想想端口转发或 docker-compose）。 

一种可靠的方法是让 docker 在一个单独的网络命名空间中运行，在那里它可以为所欲为。最好**不要** 使用 [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包 来防止 docker 混合 nftables 和 iptables 规则。 

使用以下 docker 服务[放置文件](<../zh-cn/Systemd.html#%E6%94%BE%E7%BD%AE%E6%96%87%E4%BB%B6> "Systemd")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]： 
    
    /etc/systemd/system/docker.service.d/netns.conf
    
    [Service]
    PrivateNetwork=yes
    
    # 清理
    ExecStartPre=-nsenter -t 1 -n -- ip link delete docker0
    
    # 添加虚拟接口
    ExecStartPre=nsenter -t 1 -n -- ip link add docker0 type veth peer name docker0_ns
    ExecStartPre=sh -c 'nsenter -t 1 -n -- ip link set docker0_ns netns "$$BASHPID" && true'
    ExecStartPre=ip link set docker0_ns name eth0
    
    # 使主机联机
    ExecStartPre=nsenter -t 1 -n -- ip addr add 10.0.0.1/24 dev docker0
    ExecStartPre=nsenter -t 1 -n -- ip link set docker0 up
    
    # 使命名服务器联机
    ExecStartPre=ip addr add 10.0.0.100/24 dev eth0
    ExecStartPre=ip link set eth0 up
    ExecStartPre=ip route add default via 10.0.0.1 dev eth0

如果 `10.0.0.*` IP 地址不适合您的设置，请调整它们。 

使用以下后路由规则为 docker0 启用 IP 转发并设置 NAT： 
    
    iifname docker0 oifname eth0 masquerade
    
然后，确保已启用[内核 IP 转发](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%88%86%E4%BA%AB.html#%E5%90%AF%E7%94%A8%E5%8C%85%E8%BD%AC%E5%8F%91> "网络分享")。 

现在，您可以使用 nftables 为 `docker0` 接口设置防火墙和端口转发，而不受任何干扰。 

##  另见

  * [网络过滤器 nftables wiki](<https://wiki.nftables.org/>)
  * [debian:nftables](<https://wiki.debian.org/nftables> "debian:nftables")
  * [gentoo:nftables](<https://wiki.gentoo.org/wiki/nftables> "gentoo:nftables")
  * [First release of nftables](<https://lwn.net/Articles/324251/>)
  * [nftables quick howto](<https://home.regit.org/netfilter-en/nftables-quick-howto/>)
  * [The return of nftables](<https://lwn.net/Articles/564095/>)
  * [What comes after ‘iptables’? Its successor, of course: `nftables`](<https://developers.redhat.com/blog/2016/10/28/what-comes-after-iptables-its-successor-of-course-nftables/>)
