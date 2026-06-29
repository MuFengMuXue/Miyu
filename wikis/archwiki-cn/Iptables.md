**翻译状态：**

  * 本文（或部分内容）译自 [Iptables](<https://wiki.archlinux.org/title/Iptables> "arch:Iptables")，最近一次同步于 2021-11-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Iptables?diff=0&oldid=701860>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Iptables_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [nftables](<../zh-cn/Nftables.html> "Nftables")
  * [Fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban")
  * [sshguard](<../zh-cn/Sshguard.html> "Sshguard")
  * [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")
  * [Sysctl#TCP/IP stack hardening](<../zh-cn/Sysctl.html#TCP/IP_stack_hardening> "Sysctl")
  * [Uncomplicated Firewall](<../zh-cn/Uncomplicated_Firewall.html> "Uncomplicated Firewall")

_iptables_ 是一个配置 Linux 内核[防火墙](</wzh/index.php?title=Firewall&action=edit&redlink=1> "Firewall（页面不存在）")的命令行工具，是 [Netfilter](<https://en.wikipedia.org/wiki/Netfilter> "wikipedia:Netfilter") 项目的一部分。术语 _iptables_ 也经常代指该内核级防火墙。iptables 可以直接配置，也可以通过许多[控制台](<#%E6%8E%A7%E5%88%B6%E5%8F%B0>)和[图形化](<#%E5%9B%BE%E5%BD%A2%E5%8C%96>)前端配置。iptables 用于 [ipv4](<https://en.wikipedia.org/wiki/Ipv4> "wikipedia:Ipv4")， _ip6tables_ 用于 [IPv6](<../zh-cn/IPv6.html> "IPv6")。 _iptables_ 和 _ip6tables_ 拥有相同的语法，但是有些特别的选项，对 IPv4 和 IPv6 有些不同的。 

**注意：** _iptables_ 是一个遗留的框架，[nftables](<../zh-cn/Nftables.html> "Nftables") 致力于提供一个现代化的替代产品，包括一个兼容层。

##  安装

Arch Linux 内核已经编译了 iptables 支持。只需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")用户层工具 [iptables](<https://archlinux.org/packages/?name=iptables>)包 包即可。[iptables](<https://archlinux.org/packages/?name=iptables>)包是[base](<https://archlinux.org/packages/?name=base>)包[meta package](<../zh-cn/Meta_package.html> "Meta package")的间接依赖，因此系统中已经默认安装了 iptables 包。 

###  前端

####  控制台

  * **Arno's firewall** — 可用于单机器和多连接机器的安全防火墙。配置简单，管理方便，高度定制化。支持：NAT和SNAT, 端口转发，拥有静态和动态IP分配的ADSL网络调制解调器，MAC地址过滤，隐身端口扫描检测，DMZ和DMZ-2-LAN转发，保护免SYN/ICMP洪范攻击，使用限速的可自定义的用户日志防御日志洪范攻击，所有IP协议和VPN(如IPsec)，插件支持额外添加功能。

     <https://rocky.eld.leidenuniv.nl/> || [arno-iptables-firewall](<https://aur.archlinux.org/packages/arno-iptables-firewall/>)AUR

  * **ferm** — 维护复杂防火墙的工具，无需一遍遍的向防火墙写入复杂的规则。它允许将整个防火墙规则储存在一个单独的文件中，之后使用一个单独的命令进行加载。 防火墙配置类似于结构变成语言，可以包含levels和lists。

     <http://ferm.foo-projects.org/> || [ferm](<https://archlinux.org/packages/?name=ferm>)包

  * **[FireHOL](<https://en.wikipedia.org/wiki/FireHOL> "wikipedia:FireHOL")** — 用来表达防火墙规则的语言，不仅仅是生成某种防火墙的脚本。它可以以一种你想要的方式，使构建一个很复杂的防火墙变得简单。

     <http://firehol.sourceforge.net/> || [firehol](<https://aur.archlinux.org/packages/firehol/>)AUR

  * **Firetable** — 维护IPtables防火墙的工具。每个接口可以通过其自己的配置文件单独配置，配置文件是以一种简单且人类可读的语法书写的。

     <https://gitlab.com/hsleisink/firetable> || [firetable](<https://aur.archlinux.org/packages/firetable/>)AUR

  * **[firewalld](<../zh-cn/Firewalld.html> "Firewalld") (firewall-cmd)** — 守护进程和控制台接口，以用来配置网络和防火墙保护区域，和设置与配置防火墙规则一样。

     <https://firewalld.org/> || [firewalld](<https://archlinux.org/packages/?name=firewalld>)包

  * **[Shorewall](<../zh-cn/Shorewall.html> "Shorewall")** — 配置Netfilter的高级工具。您可以使用一组配置文件中的条目描述防火墙/网关的需求。

     <http://www.shorewall.net/> || [shorewall](<https://aur.archlinux.org/packages/shorewall/>)AUR

  * **[Uncomplicated Firewall](<../zh-cn/Uncomplicated_Firewall.html> "Uncomplicated Firewall")** — iptables的简单前端。

     <https://launchpad.net/ufw> || [ufw](<https://archlinux.org/packages/?name=ufw>)包

  * **[PeerGuardian](</wzh/index.php?title=PeerGuardian_Linux&action=edit&redlink=1> "PeerGuardian Linux（页面不存在）") (pglcmd)** — 面向隐私的防火墙应用。它使用一个指定的巨大的阻塞链表（包含数千或数百万的IP的范围）来阻止主机的出站和入站连接。

     <https://sourceforge.net/projects/peerguardian/> || [pgl](<https://aur.archlinux.org/packages/pgl/>)AUR

  * **Vuurmuur** — 强大的防火墙管理器。它拥有一个简单易学配置方式，并且支持简单或复杂的配置。配置完全可以使用[ncurses](<https://archlinux.org/packages/?name=ncurses>)包GUI进行，并且该GUI支持通过SSH或控制台进行的安全远程管理。Vuurmuur支持流量整形，拥有一个强大的监控功能，它允许管理员实时查看日志，链接和带宽使用。

     <https://www.vuurmuur.org/> || [vuurmuur](<https://aur.archlinux.org/packages/vuurmuur/>)AUR

  * **Servicewall** — 简单的自定义的iptables前端，使你可以定义在连接到特定领域时允许的服务，并且在需要时自动的切换配置文件。它的服务定义通过[jhansonxi](<https://www.blogger.com/profile/02954133518928245196>)提供，通过[ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw")使用。它依赖于[ulogd](<https://www.netfilter.org/projects/ulogd/index.html>)来向日志文件提供丢弃的包的日志，并且提供了一个注重日志访问限制的日志检查框架。

     <https://github.com/lafleurdeboum/servicewall> || [servicewall-git](<https://aur.archlinux.org/packages/servicewall-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

####  图形化

  * **Firewall Builder** — GUI防火墙配置管理工具，支持iptables (netfilter), ipfilter, pf, ipfw, 思科 PIX (FWSM, ASA) 和思科路由拓展访问链表。程序可以运行在Linux，FreeBSD，OpenBSD，Windows和macOS上，并且可以管理本地和远程的防火墙。

     <https://fwbuilder.sourceforge.net/> || [fwbuilder](<https://archlinux.org/packages/?name=fwbuilder>)包

  * **[firewalld](<https://en.wikipedia.org/wiki/firewalld> "wikipedia:firewalld") (firewall-config)** — 用于配置网络和防火墙区域，以及设置和配置防火墙规则的守护进程和图形界面。

     <https://firewalld.org/> || [firewalld](<https://archlinux.org/packages/?name=firewalld>)包

  * **[Gufw](<../zh-cn/Uncomplicated_Firewall.html#Gufw> "Uncomplicated Firewall")** — 用于[ufw](<https://archlinux.org/packages/?name=ufw>)包的基于GTK的前端，这正好是一个十分简单好用的对于iptables(gufw->ufw->iptables)的用户前端。

     <https://gufw.org/> || [gufw](<https://archlinux.org/packages/?name=gufw>)包

  * **[PeerGuardian](</wzh/index.php?title=PeerGuardian_Linux&action=edit&redlink=1> "PeerGuardian Linux（页面不存在）") GUI (pglgui)** — 面向隐私的防火墙应用。它使用一个指定的巨大的阻塞链表（包含数千或数百万的IP的范围）来阻止主机的出站和入站连接。

     <https://sourceforge.net/projects/peerguardian/> || [pgl](<https://aur.archlinux.org/packages/pgl/>)AUR

##  基本概念

iptables 可以检测、修改、转发、重定向和丢弃 IPv4 数据包。过滤 IPv4 数据包的代码已经内置于内核中，并且按照不同的目的被组织成**表** 的集合。**表** 由一组预先定义的**链** 组成，**链** 包含遍历顺序规则。每一条规则包含一个谓词的潜在匹配和相应的动作（称为**目标** ），如果谓词为真，该动作会被执行。也就是说条件匹配。iptables 是用户工具，允许用户使用**链** 和**规则** 。很多新手面对复杂的 linux IP 路由时总是感到气馁，但是，实际上最常用的一些应用案例（NAT 或者基本的网络防火墙）并不是很复杂。 

理解 iptables 如何工作的关键是这张[图](<https://www.frozentux.net/iptables-tutorial/images/tables_traverse.jpg>)。图中在上面的小写字母代表**表** ，在下面的大写字母代表**链** 。**从任何网络端口** 进来的每一个 IP 数据包都要从上到下的穿过这张图。一种常见的错误认知是认为 iptables 对从内部端口进入的数据包和从面向互联网端口进入的数据包采取不同的处理方式，相反，iptables 对从任何端口进入的数据包都会采取相同的处理方式。可以定义规则使 iptables 采取不同的方式对待从不同端口进入的数据包。当然一些数据包是用于本地进程的，因此在图中表现为从顶端进入，到 <Local Process> 停止，而另一些数据包是由本地进程生成的，因此在图中表现为从 <Local Process> 发出，一直向下穿过该流程图。一份关于该流程图如何工作的详细解释请参考[这里](<https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html#TRAVERSINGOFTABLES>)。 

在大多数使用情况下都不会用到 **raw** ，**mangle** 和 **security** 表。下图简要描述了网络数据包通过 **iptables** 的过程： 
    
                                   XXXXXXXXXXXXXXXXXX
                                 XXX     Network    XXX
                                   XXXXXXXXXXXXXXXXXX
                                           +
                                           |
                                           v
     +-------------+              +------------------+
     |table: filter| <---+        | table: nat       |
     |chain: INPUT |     |        | chain: PREROUTING|
     +-----+-------+     |        +--------+---------+
           |             |                 |
           v             |                 v
     [local process]     |           ****************          +--------------+
           |             +---------+ Routing decision +------> |table: filter |
           v                         ****************          |chain: FORWARD|
    ****************                                           +------+-------+
    Routing decision                                                  |
    ****************                                                  |
           |                                                          |
           v                        ****************                  |
    +-------------+       +------>  Routing decision  <---------------+
    |table: nat   |       |         ****************
    |chain: OUTPUT|       |               +
    +-----+-------+       |               |
          |               |               v
          v               |      +-------------------+
    +--------------+      |      | table: nat        |
    |table: filter | +----+      | chain: POSTROUTING|
    |chain: OUTPUT |             +--------+----------+
    +--------------+                      |
                                          v
                                   XXXXXXXXXXXXXXXXXX
                                 XXX    Network     XXX
                                   XXXXXXXXXXXXXXXXXX
    
###  表（Tables）

iptables 包含 5 张表（tables）: 

  1. `raw` 用于配置数据包，`raw` 中的数据包不会被系统跟踪。
  2. `filter` 是用于存放所有与防火墙相关操作的默认表。
  3. `nat` 用于[网络地址转换](<https://en.wikipedia.org/wiki/Network_address_translation> "wikipedia:Network address translation")（例如：端口转发）。
  4. `mangle` 用于对特定数据包的修改（参考[损坏数据包](<https://en.wikipedia.org/wiki/Mangled_packet> "wikipedia:Mangled packet")）。
  5. `security` 用于[强制访问控制](<../zh-cn/%E5%AE%89%E5%85%A8.html#Mandatory_access_control> "Security")网络规则（例如： SELinux -- 详细信息参考[该文章](<https://lwn.net/Articles/267140/>)）。

大部分情况仅需要使用 **filter** 和 **nat** 。其他表用于更复杂的情况——包括多路由和路由判定——已经超出了本文介绍的范围。 

###  链 （Chains）

表由链组成，链是一些按顺序排列的规则的列表。默认的 `filter` 表包含 `INPUT`， `OUTPUT` 和 `FORWARD` 3条内建的链，这3条链作用于数据包过滤过程中的不同时间点，如该[流程图](<https://www.frozentux.net/iptables-tutorial/chunkyhtml/images/tables_traverse.jpg>)所示。`nat` 表包含`PREROUTING`， `POSTROUTING` 和 `OUTPUT` 链。 

使用 [iptables(8)](<https://man.archlinux.org/man/iptables.8>) 查看其他表中内建链的描述。 

默认情况下，任何链中都没有规则。可以向链中添加自己想用的规则。链的默认规则通常设置为 `ACCEPT`，如果想确保任何包都不能通过规则集，那么可以重置为 `DROP`。默认的规则总是在一条链的最后生效，所以在默认规则生效前数据包需要通过所有存在的规则。 

用户可以加入自己定义的链，从而使规则集更有效并且易于修改。如何使用自定义链请参考 [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")。 

###  规则 （Rules）

数据包的过滤基于**规则** 。**规则** 由一个 _目标_ （数据包匹配所有条件后的动作）和很多 _匹配_ （导致该规则可以应用的数据包所满足的条件）指定。一个规则的典型匹配事项是数据包进入的端口（例如：eth0 或者 eth1）、数据包的类型（ICMP, TCP, 或者 UDP）和数据包的目的端口。 

目标使用 `-j` 或者 `--jump` 选项指定。目标可以是用户定义的链（例如，如果条件匹配，跳转到之后的用户定义的链，继续处理）、一个内置的特定目标或者是一个目标扩展。内置目标是 `ACCEPT`， `DROP`， `QUEUE` 和 `RETURN`，目标扩展是 `REJECT` and `LOG`。如果目标是内置目标，数据包的命运会立刻被决定并且在当前表的数据包的处理过程会停止。如果目标是用户定义的链，并且数据包成功穿过第二条链，目标将移动到原始链中的下一个规则。目标扩展可以被 _终止_ （像内置目标一样）或者 _不终止_ （像用户定义链一样）。详细信息参阅 [iptables-extensions(8)](<https://man.archlinux.org/man/iptables-extensions.8>)。 

###  遍历链 （Traversing Chains）

该[流程图](<https://www.frozentux.net/iptables-tutorial/chunkyhtml/images/tables_traverse.jpg>)描述了链在任何接口上收到的网络数据包是按照怎样的顺序穿过表的交通管制链。第一个路由策略包括决定数据包的目的地是本地主机（这种情况下，数据包穿过 `INPUT` 链），还是其他主机（数据包穿过 `FORWARD` 链）；中间的路由策略包括决定给传出的数据包使用哪个源地址、分配哪个接口；最后一个路由策略存在是因为先前的 mangle 与 nat 链可能会改变数据包的路由信息。数据包通过路径上的每一条链时，链中的每一条规则按顺序匹配；无论何时匹配了一条规则，相应的 target/jump 动作将会执行。最常用的3个 target 是 `ACCEPT`, `DROP` ,或者 jump 到用户自定义的链。内置的链有默认的策略，但是用户自定义的链没有默认的策略。在 jump 到的链中，若每一条规则都不能提供完全匹配，那么数据包像[这张图片](<https://www.frozentux.net/iptables-tutorial/images/table_subtraverse.jpg>)描述的一样返回到调用链。在任何时候，若 `DROP` target 的规则实现完全匹配，那么被匹配的数据包会被丢弃，不会进行进一步处理。如果一个数据包在链中被 `ACCEPT`，那么它也会被所有的父链 `ACCEPT`，并且不再遍历其他父链。然而，要注意的是，数据包还会以正常的方式继续遍历其他表中的其他链。 

###  模块 （Modules）

有许多模块可以用来扩展 iptables，例如 connlimit, conntrack, limit 和 recent。这些模块增添了功能，可以进行更复杂的过滤。 

##  配置并运行 iptables

iptables 是一个 [Systemd](<../zh-cn/Systemd.html> "Systemd") 服务，因此可以这样启动： 
    
    # systemctl start iptables
    
但是，除非有 `/etc/iptables/iptables.rules` 文件，否则服务不会启动，Arch [iptables](<https://archlinux.org/packages/?name=iptables>)包 包不包含默认的 `iptables.rules` 文件。因此，第一次启动服务时使用以下命令： 
    
    # touch /etc/iptables/iptables.rules
    # systemctl start iptables
    
或者 
    
    # cp /etc/iptables/empty.rules /etc/iptables/iptables.rules
    # systemctl start iptables
    
和其他服务一样，如果希望启动时自动加载 iptables，必须启用该服务： 
    
    # systemctl enable iptables
    
###  从命令行

####  显示当前规则

使用以下命令查看当前规则和匹配数： 
    
    # iptables -nvL
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination   
         
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination    
        
    Chain OUTPUT (policy ACCEPT 0K packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination

上面的结果表明还没有配置规则。没有数据包被阻止。 

在输入中添加 `--line-numbers` 选项，可以在列出规则的时候显示行号。这在添加单独的规则的时候很有用。 

####  重置规则

使用这些命令刷新和重置 iptables 到默认状态： 
    
    # iptables -F
    # iptables -X
    # iptables -t nat -F
    # iptables -t nat -X
    # iptables -t mangle -F
    # iptables -t mangle -X
    # iptables -t raw -F
    # iptables -t raw -X
    # iptables -t security -F
    # iptables -t security -X
    # iptables -P INPUT ACCEPT
    # iptables -P FORWARD ACCEPT
    # iptables -P OUTPUT ACCEPT
    
没有任何参数的 `-F` 命令在当前表中刷新所有链。同样的， `-X` 命令删除表中所有非默认链。 

用下面的带 `[chain]` 参数的 `-F` 和 `-X` 命令刷新或删除单独的链。 

####  编辑规则

有两种方式添加规则，一种是在链上附加规则，另一种是将规则插入到链上某个特定位置。这里将讲解这两种方式。 

首先，由于电脑不是路由器(unless, of course, it [is a router](<../zh-cn/%E8%B7%AF%E7%94%B1%E5%99%A8.html> "Router"))，因此将 `FORWARD` 链默认的规则由 `ACCEPT` 改成 `DROP`。 
    
    # iptables -P FORWARD DROP
    
**警告：** 本章节其余部分主要讲解 iptables 规则的语法和其背后的思想，而不是作为一种保护服务器的手段，如果想要提高系统的安全性，参考 [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall") 来获得一个最低限度的 iptables 安全配置，参考 [Security](<../zh-cn/%E5%AE%89%E5%85%A8.html> "Security") 来提高 Arch Linux 的安全性。

[Dropbox](<https://en.wikipedia.org/wiki/Dropbox_\(service\)> "wikipedia:Dropbox \(service\)") 的局域网同步特性——[每30秒广播数据包](<https://isc.sans.edu/port.html?port=17500>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ]到所有可视的计算机，如果我们碰巧在一个拥有 Dropbox 客户端的局域网中，但是我们不想使用这个特性，那么我们希望拒绝这些数据包。 
    
    # iptables -A INPUT -p tcp --dport 17500 -j REJECT --reject-with icmp-port-unreachable
    
    # iptables -nvL --line-numbers
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    1        0     0 REJECT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:17500 reject-with icmp-port-unreachable
    
    Chain FORWARD (policy DROP 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
    Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
**注意：** 这里使用 `REJECT` 而不是 `DROP`，因为 [RFC 1122 3.3.8](<https://tools.ietf.org/html/rfc1122#page-69>) 要求主机尽可能返回 ICMP 错误而不是丢弃数据包。[这里](<https://www.chiark.greenend.org.uk/~peterb/network/drop-vs-reject>) 介绍了为什么倾向于 REJECT 而不是 DROP 数据包。

现在，我们改变对 Dropbox 的看法，并且决定安装其到我们的计算机，我们也希望局域网同步，但是我们的网络只有一个特定的 IP 地址，因此需要使用 `-R` 参数来替换旧规则，`10.0.0.85` 是我们的另一个 IP 地址。 
    
    # iptables -R INPUT 1 -p tcp --dport 17500 ! -s 10.0.0.85 -j REJECT --reject-with icmp-port-unreachable
    
    # iptables -nvL --line-numbers
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    1        0     0 REJECT     tcp  --  *      *      !10.0.0.85            0.0.0.0/0            tcp dpt:17500 reject-with icmp-port-unreachable
    
    Chain FORWARD (policy DROP 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
    Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
现在我们替换了原来的规则，使 `10.0.0.85` 可以访问计算机 `17500` 端口。但是我们意识到这条规则是不可升级的。如果友好的 Dropbox 用户想要访问设备上的 `17500` 端口。我们应该马上允许，而不是在测试过所有防火墙规则后再允许。 

因此我们写一条新规则来立即允许受信任的用户。使用 `-I` 参数来在旧规则前插入一条新规则： 
    
    # iptables -I INPUT -p tcp --dport 17500 -s 10.0.0.85 -j ACCEPT -m comment --comment "Friendly Dropbox"
    
    # iptables -nvL --line-numbers
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    1        0     0 ACCEPT     tcp  --  *      *       10.0.0.85            0.0.0.0/0            tcp dpt:17500 /* Friendly Dropbox */
    2        0     0 REJECT     tcp  --  *      *      !10.0.0.85            0.0.0.0/0            tcp dpt:17500 reject-with icmp-port-unreachable
    
    Chain FORWARD (policy DROP 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
    Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
更改第二条规则，使其拒绝 `17500` 端口的任何数据包： 
    
    # iptables -R INPUT 2 -p tcp --dport 17500 -j REJECT --reject-with icmp-port-unreachable
    
我们的最终规则如下： 
    
    # iptables -nvL --line-numbers
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    1        0     0 ACCEPT     tcp  --  *      *       10.0.0.85            0.0.0.0/0            tcp dpt:17500 /* Friendly Dropbox */
    2        0     0 REJECT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:17500 reject-with icmp-port-unreachable
    
    Chain FORWARD (policy DROP 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
    Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    num   pkts bytes target     prot opt in     out     source               destination
    
###  配置文件

在 Arch Linux 中， Iptables 规则默认存放在 `/etc/iptables/iptables.rules` 文件中，它们不会被自动加载，因此需要启用 `iptables.service`，服务会在启动时读取文件并且加载规则，或者直接启动服务： 
    
    # systemctl enable iptables.service
    # systemctl start iptables.service
    
ipv6 规则默认保存在 `/etc/iptables/ip6tables.rules`,`ip6tables.service` 服务会使用这个规则，可以用类似的方式启动服务。 

**注意：** iptables 1.4.21-1 包中的 `iptables.service` 和 `ip6tables.service` 文件已经过期了。因为安全原因，自 systemd 214 起推荐防火墙在 `network-pre.target` 目标之前启动，这样防火墙就可以在任何网络配置之前运行。等待 iptables 数据包更新，创建深层目录 `/etc/systemd/system/iptables.service.d`，创建 `00-pre-network.conf` 文件，添加如下片段： 
    
    [Unit]
    Before=network-pre.target
    [Install]
    RequiredBy=network-pre.target
    
如果系统使用 `ip6tables.service`，那么在 `/etc/systemd/system/ip6tables.service.d` 目录中做同样的配置。更多细节参考 [systemd bug report](<https://bugs.freedesktop.org/show_bug.cgi?id=79600>)，[systemd release announcement](<https://lists.freedesktop.org/archives/systemd-devel/2014-June/019925.html>) 和 [FS#33478](<https://bugs.archlinux.org/task/33478>)

通过命令行添加规则，配置文件不会自动改变，所以必须手动保存： 
    
    # iptables-save > /etc/iptables/iptables.rules
    
修改配置文件后，需要重新加载服务： 
    
    # systemctl reload iptables
    
或者通过 iptables 直接加载： 
    
    # iptables-restore < /etc/iptables/iptables.rules
    
###  指南

  * [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")
  * [Router](<../zh-cn/%E8%B7%AF%E7%94%B1%E5%99%A8.html> "Router")

##  日志

LOG 目标可以用来记录匹配某个规则的数据包。和 ACCEPT 或 DROP 规则不同，进入 LOG 目标之后数据包会继续沿着链向下走。所以要记录所有丢弃的数据包，只需要在 DROP 规则前加上相应的 LOG 规则。但是这样会比较复杂，影响效率，所以应该创建一个`logdrop`链。 

创建 logdrop 链： 
    
    # iptables -N logdrop
    
定义规则： 
    
    # iptables -A logdrop -m limit --limit 5/m --limit-burst 10 -j LOG
    # iptables -A logdrop -j DROP
    
[下文](<#%E9%99%90%E5%88%B6%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB>)会给出 `limit` 和 `limit-burst` 选项的解释。 

现在任何时候想要丢弃数据包并且记录该事件，只要跳转到 `logdrop` 链，例如： 
    
    # iptables -A INPUT -m conntrack --ctstate INVALID -j logdrop
    
###  限制日志级别

上述 `logdrop` 链使用限制（limit）模式来防止 _iptables_ 日志来过大或者造成不必要的硬盘读写。没有限制的话，一个试图链接的错误配置服务、或者一个攻击者，都会使 iptables 日志写满整个硬盘（或者至少是 `/var` 分区）。 

限制模式使用 `-m limit`，可以使用 `--limit` 来设置平均速率或者使用 `--limit-burst` 来设置起始触发速率。在上述 `logdrop` 例子中： 
    
    iptables -A logdrop -m limit --limit 5/m --limit-burst 10 -j LOG
    
appends a rule which will log all packets that pass through it. The first 10 consecutive packets will be logged, and from then on only 5 packets per minute will be logged. The "limit burst" count is reset every time the "limit rate" is not broken, i.e. logging activity returns to normal automatically. 

添加一条记录所有通过其的数据包的规则。开始的连续10个数据包将会被记录，之后每分钟只会记录5个数据包。The "limit burst" count is reset every time the "limit rate" is not broken，例如，日志记录活动自动恢复到正常。 

###  查看记录的数据包

记录的数据包作为内核信息，可以在 [systemd journal](<../zh-cn/Systemd/Journal.html> "Systemd/日志") 看到。 

使用以下命令查看所有最近一次启动后所记录的数据包： 
    
    # journalctl -k | grep "IN=.*OUT=.*" | less
    
###  使用 syslog-ng

使用 Arch 默认的 [syslog-ng](</wzh/index.php?title=Syslog-ng&action=edit&redlink=1> "Syslog-ng（页面不存在）") 可以控制 iptables 日志的输出文件： 
    
    filter f_everything { level(debug..emerg) and not facility(auth, authpriv); };
    
修改为 
    
    filter f_everything { level(debug..emerg) and not facility(auth, authpriv) and not filter(f_iptables); };
    
iptables 的日志就不会输出到 `/var/log/everything.log`。 

iptables 也可以不输出到 `/var/log/iptables.log`，只需设置`syslog-ng.conf` 中的 d_iptables 为需要的日志文件。 
    
    destination d_iptables { file("/var/log/iptables.log"); };
    
###  使用 ulogd

[ulogd](<https://www.netfilter.org/projects/ulogd/index.html>) 是专门用于 netfilter 的日志工具，可以代替默认的 LOG 目标。软件包 [ulogd](<https://archlinux.org/packages/?name=ulogd>)包 位于 `[community]` 源。 

##  参见

[Wikipedia:iptables](<https://en.wikipedia.org/wiki/iptables> "wikipedia:iptables")

  * [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")
  * [官方网站](<https://www.netfilter.org/projects/iptables/index.html>)
  * [Iptables 教程 1.2.2](<https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html>)
