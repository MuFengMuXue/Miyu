[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 解释重复，结构松散（在[Talk:Systemd-networkd](<../zh-cn/Talk:Systemd-networkd.html>)讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [Systemd-networkd](<https://wiki.archlinux.org/title/Systemd-networkd> "arch:Systemd-networkd")，最近一次同步于 2025-07-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd-networkd?diff=0&oldid=838171>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd-networkd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd](<../zh-cn/Systemd.html> "Systemd")
  * [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")
  * [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")
  * [Network bridge](<../zh-cn/Network_bridge.html> "Network bridge")
  * [Network configuration](<../zh-cn/Network_configuration.html> "Network configuration")
  * [Wireless network configuration](<../zh-cn/Wireless_network_configuration.html> "Wireless network configuration")
  * [Category:Network configuration](<../zh-cn/Category:Network_configuration.html> "Category:Network configuration")

_systemd-networkd_ 是一个管理网络配置的系统守护进程。它会在网络设备出现时检测和配置它们；它还可以创建虚拟网络设备。这个服务非常适合于为 [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn") 管理的容器或者虚拟机创建复杂的网络配置。如果只是简单网络的配置，它也同样能胜任。 

##  基本用法

[systemd](<https://archlinux.org/packages/?name=systemd>)包 是默认 Arch 安装的一部分，包含操作有线网络所需的所有文件。无线适配器可以通过其他服务（比如 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant") 或者 [iwd](<../zh-cn/Iwd.html> "Iwd")）来配置，本文后面的部分也会介绍相关内容。 

###  必需的服务和设置

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `systemd-networkd.service` 以使用 _systemd-networkd_ 。 

**注意：** 必须确认没有其他服务正在管理网络。不同的网络管理服务会互相冲突。通过 `systemctl --type=service` 可以得到正在运行的服务的列表，请[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop")其他网络管理服务。

配置 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 是可选的，它为本地应用程序提供网络名称解析服务。是否使用它可以考虑下面几条： 

  * 如果 _.network_ 文件中指定了 DNS 条目，则 _systemd-resolved_ 服务是必需的
  * 想自动从DHCP服务器或IPv6路由器推荐获取 DNS 服务器地址（通过在`[Network]`中设置(`DHCP=`和/或`IPv6AcceptRA=`，并在对应的`[DHCPv4]`、`[DHCPv6]`、`[IPv6AcceptRA]`中设置`UseDNS=yes`（默认值）来实现，参见[systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>)）
  * 请搞明白 [resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf") 和 _systemd-resolved_ 如何互相影响，以便正确配置要使用的 DNS 服务器。更多相关信息可以参见 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")
  * 注意：即使没有启用 _systemd-networkd_ ， _systemd-resolved_ 也能够提供服务。

### systemd-networkd-wait-online

启用 `systemd-networkd.service` 的同时，也会启用 `systemd-networkd-wait-online.service`。这是一个一次性类型的 systemd 服务，用于等待网络完成配置。该服务具有 `WantedBy=network-online.target`，因此只有当 `network-online.target` 被启用或被其他单元拉入时才会启动。另请参阅[当网络启动后执行服务](<../zh-cn/Systemd.html#Running_services_after_the_network_is_up> "Systemd")。 

默认情况下，`systemd-networkd-wait-online.service` 会等待所有由 _systemd-networkd_ 管理的链路完成配置（或失败），并且至少有一个链路在线。 

详情请参阅 [systemd-networkd-wait-online(8)](<https://man.archlinux.org/man/systemd-networkd-wait-online.8>)。 

####  多个网络接口不一定会持续连接

若系统具有多个网络接口，但这些接口并不一定会时时保持连接（例如拥有双口以太网卡，但只插了一根线），启动 `systemd-networkd-wait-online.service` 时会在默认 2 分钟超时后失败，从而导致开机流程出现不必要的延迟。 

若希望更改为等待“任一”接口而不是“全部”接口上线，可以[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")该服务，并在 `ExecStart` 行加入 `--any` 参数： 
    
    /etc/systemd/system/systemd-networkd-wait-online.service.d/wait-for-only-one-interface.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/lib/systemd/systemd-networkd-wait-online --any

或者，也可以使用 `systemd-networkd-wait-online@.service` 来指定特定接口。例如，若只需等待 `enp1s0` 上线，请[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用") `systemd-networkd-wait-online.service`，并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `systemd-networkd-wait-online@enp1s0.service`。 

**提示：** 若已知某些接口可能不会随时上线，可在 `.network` 配置文件的 `[Link]` 区块中加入 `RequiredForOnline=no`。详情请参见 [systemd.network(5) § [LINK]_SECTION_OPTIONS](<https://man.archlinux.org/man/systemd.network.5#%5BLINK%5D_SECTION_OPTIONS>)。

####  等待直到网络接口取得可路由地址

根据 [systemd-networkd-wait-online.service(8)](<https://man.archlinux.org/man/systemd-networkd-wait-online.service.8>) 的说明，"online 表示链路的操作状态至少为 degraded"（关于 degraded 与其他操作状态的定义，请参阅 [networkctl(1)](<https://man.archlinux.org/man/networkctl.1>)）。 

若希望 `systemd-networkd-wait-online.service` 在网络接口取得可路由的 IP 地址后才结束（以避免依赖网络的其他服务启动过早），可在 _.network_ 配置文件中的 `[Link]` 区段加入： 
    
    [Link]
    RequiredForOnline=routable

###  配置样例

在本节中，所有配置都存储为在 `/etc/systemd/network/` 目录下 形如 `foo.network` 的文件。有关选项的完整列表和处理顺序可以参考 [#配置文件](<#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)和 [systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>)。 

Systemd/udev 会自动为所有本地以太网、WLAN 和 WWAN 接口分配可预测且稳定的网络接口名。使用 `networkctl list` 以列出系统上所有设备。 

在修改了配置文件之后，[restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `systemd-networkd.service` 以使得它们生效。 

**注意：**

  * 配置文件中指定的选项区分大小写。
  * 在下面的示例中，`enp1s0` 是有线适配器，`wlp2s0` 是无线适配器。他们的名字在不同系统上可能会有不同的名字。也可以使用通配符，例如，`Name=en*`。
  * 如果想要禁用 IPv6 的话，参考 [IPv6#systemd-networkd](<../zh-cn/IPv6.html#systemd-networkd_2> "IPv6")。
  * 在 `[Network]` 段设置 `DHCP=yes` 来同时接收 IPv4 **和** IPv6 DHCP 请求。

####  使用 DHCP 的有线适配器
    
    /etc/systemd/network/20-wired.network
    
    [Match]
    Name=enp1s0
    
    [Link]
    RequiredForOnline=routable
    
    [Network]
    DHCP=yes

####  使用静态 IP 的有线适配器
    
    /etc/systemd/network/20-wired.network
    
    [Match]
    Name=enp1s0
    
    [Network]
    Address=10.1.10.9/24
    Gateway=10.1.10.1
    DNS=10.1.10.1
    #DNS=8.8.8.8

`Address=` 能够被使用多次来指定多个 IPv4 或者 IPv6 地址。 参见 [#network 文件](<#network_%E6%96%87%E4%BB%B6>)或者 [systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>) 了解更多配置项。 

####  无线适配器

为了能够使用 _systemd-networkd_ 连接一个无线网络，需要一个被其他应用，比如 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant") 或 [iwd](<../zh-cn/Iwd.html> "Iwd")，配置好的无线适配器。 
    
    /etc/systemd/network/25-wireless.network
    
    [Match]
    Name=wlp2s0
    
    [Link]
    RequiredForOnline=routable
    
    [Network]
    DHCP=yes
    IgnoreCarrierLoss=3s
    
如果无线适配器有一个静态地址，它的配置（除了接口的名字）跟有线适配器是一样的。 

####  同一台机器上的有线和无线适配器

这些设置将为有线和无线连接自动获取 DHCP IP, 并使用 metric 让内核动态地决定使用的链接。这样，网络在有线连接断开时就不会有明显的中断。内核的 route metric (与 ip 配置一致) 会在具有多个设备时决定使用哪个传出数据包。如果某个连接断开，其他的接口就会自动接管，而不会出现网络中断（正在进行的传输可能会出现问题，不过那是另一层的问题了。） 

**注意：**`Metric` 选项用于静态路由，而 `RouteMetric` 选项则用于不使用静态路由的配置。详情请参见 [systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>)。
    
    /etc/systemd/network/20-wired.network
    
    [Match]
    Name=enp1s0
    
    [Network]
    DHCP=yes
    
    [DHCPv4]
    RouteMetric=100
    
    [IPv6AcceptRA]
    RouteMetric=100
    
    /etc/systemd/network/25-wireless.network
    
    [Match]
    Name=wlp2s0
    
    [Network]
    DHCP=yes
    
    [DHCPv4]
    RouteMetric=600
    
    [IPv6AcceptRA]
    RouteMetric=600

####  网络接口重命名

作为[更改设备名称](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E6%9B%B4%E6%94%B9%E6%8E%A5%E5%8F%A3%E5%90%8D%E7%A7%B0> "网络配置")的替代方案，systemd 使用 _.link_ 文件用于接口重命名。常见的例子是基于 MAC 地址给一个 USB 接口以太网适配器设置一个可预见的接口名称。这类设备依其连接到不同 USB 接口而具有不同的接口名称。 
    
    /etc/systemd/network/10-ethusb0.link
    
    [Match]
    MACAddress=12:34:56:78:90:ab
    
    [Link]
    Description=USB to Ethernet Adapter
    Name=ethusb0

**注意：** 任何由用户提供的 _.link_ 文件名**必须** 是依字典顺序先于默认配置文件名`99-default.link`才能生效。例如，必须是`10-ethusb0.link`而不能是 `ethusb0.link`。

##  配置文件

配置文件位于 `/usr/lib/systemd/network`，非持久化的运行时网络配置目录位于 `/run/systemd/network` ，本地管理网络配置位于 `/etc/systemd/network`。`/etc/systemd/network` 中的配置文件具有最高优先级。 

配置文件有三类。它们均使用类似于 [systemd 单元文件](<../zh-cn/Systemd.html#%E7%BC%96%E5%86%99%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")的格式。 

  * _**.network**_ 文件，为 _匹配_ 的设备提供一个网络配置
  * _**.netdev**_ 文件，为 _匹配_ 的环境创建一个 _虚拟网络设备_
  * _**.link**_ 文件，当网络设备出现时，[udev](<../zh-cn/Udev.html> "Udev") 将查找第一个 _匹配_ 的 _.link_ 文件

它们均遵循下列规则： 

  * 如果位于`[Match]`小节的**全部** 条件相匹配，配置项将被激活
  * 一个空的`[Match]`小节意味着配置项适用任何情况（相当于`*`通配符）
  * 所有配置文件将按字典顺序集中保存和处理，不管它们在目录中的实际顺序如何。
  * 同名文件将彼此替换

**提示：**

  * 要永久覆盖 `/usr/lib/systemd/network` 中系统提供的文件（即升级之后仍覆盖），请在 `/etc/systemd/network` 中放置一个具有相同名称的文件并将其符号链接到 `/dev/null`
  * 星号（`*`）通配符可以在 `VALUE` 中使用（例如 `en*` 将匹配任何以太网设备）， 布尔值可以简单地写为 `yes` 或 `no`。
  * 根据[这个线索](<https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/thread/PE53GCKRAMJC2A62KGEBBQAFPQK7GRND/>)的讨论，最佳实践是 to setup specific container network settings _inside the container_ with **networkd** configuration files.
  * Systemd 使用`1, true, yes, on`作为逻辑“真”值，`0, false, no, off`作为逻辑“假”值

###  network 文件

这类文件用于设置网络配置变量，尤其适用于服务器和容器。 

_.network_ 文件含有下列小节：`[Match]`、`[Link]`、`[Network]`、`[Address]`、`[Route]`以及`[DHCP]`。下列为每小节的通用配置。详情及范例请参阅[systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>)。 

####  [Match] 小节

参数 | 说明 | 可接受的值 | 默认值   
---|---|---|---  
`Name=` | 匹配设备名称，例如 `en*`。可使用 `!` 反向匹配。 | 以空格分隔的设备名称，支持通配符与逻辑否定（`!`） |   
`MACAddress=` | 匹配 MAC 地址，例如 `MACAddress=01:23:45:67:89:ab 00-11-22-33-44-55 AABB.CCDD.EEFF` | 使用冒号、连字符或点号分隔的十六进制 MAC 地址 |   
`Host=` | 匹配主机名称或 machine ID。 | 含通配符的主机名称字符串，[machine-id(5)](<https://man.archlinux.org/man/machine-id.5>) |   
`Virtualization=` | 检查是否运行于虚拟环境中。`Virtualization=false` 仅匹配实体机器；`Virtualization=true` 则匹配任何容器或虚拟机。亦可检查特定虚拟化类型或实现，或用户命名空间（`private-users`）。 | 布尔值、逻辑否定（`!`）、类型（`vm`, `container`）、实现（参见 [systemd-detect-virt(1)](<https://man.archlinux.org/man/systemd-detect-virt.1>)）、`private-users` |   
  
####  [Link] 小节

参数 | 说明 | 可接受的值 | 默认值   
---|---|---|---  
`MACAddress=` | 指定设备的硬件地址。可用于 [MAC 地址伪造](<../zh-cn/MAC_address_spoofing.html#systemd-udevd> "MAC address spoofing")。 | 使用冒号、连字符或点号分隔的十六进制 MAC 地址 |   
`MTUBytes=` | 指定设备的最大传输单元（MTU）大小（单位：字节）。若启用 IPv6 且设置值小于 1280（IPv6 最小 MTU），系统会自动调整为此值。设置较大的 MTU（例如使用 [jumbo frames](</wzh/index.php?title=Jumbo_frames&action=edit&redlink=1> "Jumbo frames（页面不存在）")）可大幅提升传输性能。 | 整数，可加上单位 K、M、G（以 1024 为底） |   
`Multicast=` | 是否允许使用 [多播](<https://en.wikipedia.org/wiki/Multicast_address> "wikipedia:Multicast address")。 | 布尔值 |   
  
####  [Network] 小节

参数 | 说明 | 可接受的值 | 默认值   
---|---|---|---  
`DHCP=` | 控制 DHCPv4 或 DHCPv6 客户端支持。 | 布尔值、`ipv4`, `ipv6` |  `no`  
`DHCPServer=` | 启用时将启动 DHCPv4 服务器。 | 布尔值 |  `no`  
`MulticastDNS=` | 启用 [多播 DNS](<https://tools.ietf.org/html/rfc6762> "rfc:6762") 支持。若设为 `resolve`，仅启用名称解析功能，不注册主机或广播服务。 | 布尔值、`resolve` |  `false`  
`DNSSEC=` | 控制是否启用 DNSSEC 验证支持。设为 `allow-downgrade` 时，在不支持 DNSSEC 的网络中将自动停用以提高兼容性。 | 布尔值、`allow-downgrade` |  `false`  
`DNS=` | 设置静态 [DNS](</wzh/index.php?title=DNS&action=edit&redlink=1> "DNS（页面不存在）") 地址。可指定多个值。 | [inet_pton(3)](<https://man.archlinux.org/man/inet_pton.3>) |   
`Domains=` | 指定此连接使用哪些域名解析，[systemd.network(5) § [NETWORK] SECTION OPTIONS](<https://man.archlinux.org/man/systemd.network.5#%5BNETWORK%5D_SECTION_OPTIONS>)。 | 域名，可加上波浪号（`~`）表示仅供解析使用 |   
`IPv4Forwarding=` 和 `IPv6Forwarding=` | 启用时，此接口接收的（IPv4 / IPv6）包可根据路由表转发至其他接口。对应内核的 `net.ipv4/6.conf.INTERFACE.forwarding` sysctl 选项。详见 [Internet sharing#Enable packet forwarding](<../zh-cn/Internet_sharing.html#Enable_packet_forwarding> "Internet sharing")。 | 布尔值 |  `no`  
`IPMasquerade=` | 启用时，此接口转发的包会被伪装为来自本机。此选项的设置可能会同时启用 `IPv4Forwarding` 或 `IPv6Forwarding`。 |  `ipv4`, `ipv6`, `both`, `no` |  `no`  
`IPv6PrivacyExtensions=` | 设置是否使用会定期变更的无状态临时地址（参见 [RFC:4941](<https://tools.ietf.org/html/rfc4941> "rfc:4941")）。`prefer-public` 表示启用临时地址，但偏好使用公开地址；`kernel` 则保留内核默认值。 | 布尔值、`prefer-public`, `kernel` |  `no`  
  
####  [Address] 小节

参数 | 说明 | 可接受的值 | 默认值   
---|---|---|---  
`Address=` | 可多次指定此键以设置多个 IP 地址。若未使用 DHCP，则此参数为必要项。若指定为 `0.0.0.0`（IPv4）或 `::`（IPv6），系统会自动从全局未使用段中分配一个适当大小的地址范围。 | 静态 IPv4 或 IPv6 地址及其前缀长度（见 [inet_pton(3)](<https://man.archlinux.org/man/inet_pton.3>)） |   
  
####  [Route] 小节

  * `Gateway=` 此选项为“必要项”，除非使用直接路由或 DHCP。
  * `Destination=` 路由的目的地前缀，可加上斜线与前缀长度。
  * `Metric=` 路由的优先权。
  * `Type=` 路由的类型。
  * `Table=` 路由所使用的路由表 ID。
  * `GatewayOnLink=` 若设为 `yes`，则内核不再检查网关是否可由本机直接连接（例如：是否连接至本地网络）。可用于解决部分路由问题。

若 `Destination` 未在 `[Route]` 区段中指定，则该区段将视为默认路由。 

**提示：** 将 `Address=` 与 `Gateway=` 直接写入 `[Network]` 区段，可作为简写方式，适用于 `[Address]` 仅包含 `Address`、`[Route]` 仅包含 `Gateway` 的情况。

####  [RoutingPolicyRule]

标准路由算法通常仅根据目标地址选择包应发送的网关。但在复杂网络中，这样的判断不一定足够。 

`[RoutingPolicyRule]` 区段允许你根据指定条件应用额外的路由规则，只应用至符合条件的包。 

以下是部分可用的匹配条件： 

  * `TypeOfService=`：匹配包的服务类型，值为 0 到 255 间的整数。
  * `From=`：源地址前缀。
  * `To=`：目的地地址前缀。
  * `FirewallMark=`：iptables 设置的防火墙标记值。
  * `IncomingInterface=`：包进入的接口。
  * `OutgoingInterface=`：包离开的接口。

其他可用选项： 

  * `Type=`：Routing Policy Database（路由策略数据库）的规则类型。
  * `Table=`：当包匹配此规则时要使用的路由表。
  * `Priority=`：此规则的优先级。规则会依优先级由小至大排序并应用。
  * `InvertRule=`：若设为 `true`，则此规则会反转，即应用于**不符合**任何匹配条件的包。
  * `SuppressPrefixLength=`：若包的前缀长度小于等于指定值，则此规则不应用。

####  [DHCPv4]

参数 | 说明 | 可接受的值 | 默认值   
---|---|---|---  
`UseDNS=` | 控制是否使用 DHCP 服务器广播的 DNS 服务器信息。 | 布尔值 |  `true`  
`Anonymize=` | 若设为 true，则根据 [RFC:7844](<https://tools.ietf.org/html/rfc7844> "rfc:7844")（DHCP 客户端匿名配置档）限制发送可识别用户的选项。 | 布尔值 |  `false`  
`UseDomains=` | 控制是否使用 DHCP 服务器提供的域名作为 DNS 搜索域。若设为 `route`，仅用于 DNS 路由查询，不用作搜索。可解决搭配 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 使用时的本地域名解析问题。 | 布尔值、`route` |  `false`  
`IPv6OnlyMode=` | 若设为 true，DHCP 客户端会通知服务器其支持仅 IPv6 运行（参见 [RFC:8925](<https://tools.ietf.org/html/rfc8925> "rfc:8925")）。若服务器响应该选项，则客户端会中止 DHCPv4 请求，不会获取 IPv4 地址，并改为设置为 IPv6-only 模式。 | 布尔值 |  `true`（若启用 IPv6 时）   
  
####  [DHCPServer]

这是一个 DHCP 服务器的示例配置，与 [hostapd](</wzh/index.php?title=Hostapd&action=edit&redlink=1> "Hostapd（页面不存在）") 搭配使用可建立无线热点。`IPMasquerade` 会新增 [NAT](<../zh-cn/Internet_sharing.html#Enable_NAT> "Internet sharing") 所需的防火墙规则，并隐含 `IPv4Forwarding=yes`，以启用[包转发](<../zh-cn/Internet_sharing.html#Enable_packet_forwarding> "Internet sharing")功能。 
    
    /etc/systemd/network/_wlan0_.network
    
    [Match]
    Name=wlan0
    
    [Network]
    Address=10.1.1.1/24
    DHCPServer=true
    IPMasquerade=ipv4
    
    [DHCPServer]
    PoolOffset=100
    PoolSize=20
    EmitDNS=yes
    DNS=9.9.9.9

###  netdev 文件

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** 与 [systemd.netdev(5)](<https://man.archlinux.org/man/systemd.netdev.5>) 手册页内容重复。 (在 [Talk:Systemd-networkd](<../zh-cn/Talk:Systemd-networkd.html>) 讨论)

这些文件用于创建虚拟网络设备。它们包含两个区段：`[Match]` 与 `[NetDev]`。以下列出每个区段常用的设置键值。更多信息与示例请参阅 [systemd.netdev(5)](<https://man.archlinux.org/man/systemd.netdev.5>)。 

这类文件将创建虚拟网络设备。包含两个小节：`[Match]` 和 `[NetDev]`。下列为每小节的通用配置。详情及范例请参阅[systemd.netdev(5)](<https://man.archlinux.org/man/systemd.netdev.5>)。 

####  [Match] 小节

  * `Host=` 主机名
  * `Virtualization=` 检查是否运行于虚拟机中

####  [NetDev] 小节

最通用的配置为： 

  * `Name=` 接口名称。**必须提供**
  * `Kind=` 例如： _bridge_ , _bond_ , _vlan_ , _veth_ , _sit_ ，等等。**必须提供**

###  link 文件

这些文件是自定义 udev 规则的替代方案，会在设备出现时由 [udev](<../zh-cn/Udev.html> "Udev") 自动应用。它们包含两个区段：`[Match]` 与 `[Link]`。以下列出各区段常用的设置键值。更多信息与示例请参阅 [systemd.link(5)](<https://man.archlinux.org/man/systemd.link.5>)。 

**提示：** 使用 `# udevadm test-builtin net_setup_link /sys/path/to/network/device` 来诊断 _.link_ 文件的问题。

####  [Match] 小节

  * `MACAddress=` MAC 地址
  * `Host=` 主机名
  * `Virtualization=`
  * `Type=` 设备类型，例如 vlan

####  [Link] 小节

  * `MACAddressPolicy=` 持久 (persistent) 或随机 (random) 地址，或
  * `MACAddress=` 指定的地址

**注意：** 系统内建的 `/usr/lib/systemd/network/99-default.link` 文件对大部分基本情况已足够使用。

##  容器下的应用

此服务由 [systemd](<https://archlinux.org/packages/?name=systemd>)包 提供。你会想要在主机及容器上 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 并 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `systemd-networkd.service`。 

为了方便调试，强烈建议安装 [bridge-utils](<https://archlinux.org/packages/?name=bridge-utils>)包、[net-tools](<https://archlinux.org/packages/?name=net-tools>)包 与 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包 软件包。 

如果你使用 [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")，可能需要修改 `systemd-nspawn@.service`，并在 `ExecStart` 行加入启动选项。请参考 [systemd-nspawn(1)](<https://man.archlinux.org/man/systemd-nspawn.1>) 了解所有可用选项。 

注意：若想利用 DHCP 自动配置 DNS，需要启用 `systemd-resolved`，并将 `/run/systemd/resolve/resolv.conf` 符号链接到 `/etc/resolv.conf`。详细信息请参考 [systemd-resolved.service(8)](<https://man.archlinux.org/man/systemd-resolved.service.8>)。 

在开始配置容器网络前，建议： 

  * 停用所有 [netctl](<../zh-cn/Netctl.html> "Netctl")（主机与容器）、[dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd")（主机与容器）、systemd-networkd（仅容器）、及 `systemd-nspawn@.service`（仅主机）服务，避免冲突并方便调试。
  * 若容器要访问互联网，确认已启用[数据包转发](<../zh-cn/Internet_sharing.html#Enable_packet_forwarding> "Internet sharing")。确保你的 _.network_ 文件中未意外关闭转发，因为如果没有设置 `IPForward=1`，`systemd-networkd` 会在该接口关闭转发，即使全局已启用。
  * 确认没有任何 [iptables](<../zh-cn/Iptables.html> "Iptables") 规则阻挡流量。
  * 启动 daemon 后，使用 systemd 的 `networkctl` 指令查看网络接口状态。

以下设定中， 

  * 我们将限制 `ip a` 指令只显示相关接口
  * 假设“主机”是你启动的主要操作系统，“容器”是你的来宾虚拟机
  * 所有接口名称及 IP 地址皆为示范用途

###  基本 DHCP 网络

此设定会为主机与容器启用 DHCP IP。两系统会共用相同 IP，因共用同一接口。 
    
    /etc/systemd/network/_MyDhcp_.network
    
    [Match]
    Name=en*
    
    [Network]
    DHCP=ipv4
    
接着在容器启用并启动 `systemd-networkd.service`。 

当然你可以用实际网卡名称替换 `en*`，可用 `ip link` 指令查询。 

  * 主机与容器上执行：

    $ ip a
    
    2: enp7s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 14:da:e9:b5:7a:88 brd ff:ff:ff:ff:ff:ff
        inet 192.168.1.72/24 brd 192.168.1.255 scope global enp7s0
           valid_lft forever preferred_lft forever
        inet6 fe80::16da:e9ff:feb5:7a88/64 scope link 
           valid_lft forever preferred_lft forever
    
默认会使用 DHCP 服务器返回的 hostname 作为临时主机名。 

若要更改，请在 `[DHCPv4]` 区段加入 `UseHostname=false`： 
    
    /etc/systemd/network/_MyDhcp_.network
    
    [DHCPv4]
    UseHostname=false
    
若不想自行设定 `/etc/resolv.conf` 的 DNS，想用 DHCP 配置，需 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `systemd-resolved.service` 并建立符号链接： 
    
    # ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf
    
详情参见 [systemd-resolved.service(8)](<https://man.archlinux.org/man/systemd-resolved.service.8>)。 

**注意：** 若透过 `/usr/bin/arch-chroot` 进入系统分区，需在 chroot 外的挂载分区上建立符号链接，因为 arch-chroot 会将文件链接到实际运行环境。

###  DHCP 用于两个独立 IP

####  桥接端口

先建立虚拟桥接接口，让 systemd 建立名为 _br0_ 的以太网桥接设备。 
    
    /etc/systemd/network/_MyBridge_.netdev
    
    [NetDev]
    Name=br0
    Kind=bridge

重新 [Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `systemd-networkd.service`，让 systemd 建立桥接。 

主机与容器上： 
    
    $ ip a
    
    3: br0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default 
        link/ether ae:bd:35:ea:0c:c9 brd ff:ff:ff:ff:ff:ff
    
此时 _br0_ 接口已显示但状态为 DOWN。 

####  绑定以太网卡到桥接端口

接着将符合名称 _en*_ 的接口加入桥接 _br0_ 。 
    
    /etc/systemd/network/_bind_.network
    
    [Match]
    Name=en*
    
    [Network]
    Bridge=br0

以太网卡本身不得配置 DHCP 或 IP，桥接需要无 IP 的接口，请修改原有 `/etc/systemd/network/_MyEth_.network` 移除 IP 配置。 

####  桥接网络

桥接建立且已绑定以太网卡后，需为桥接接口指定 IP 配置。以下范例为 DHCP。 
    
    /etc/systemd/network/_mybridge_.network
    
    [Match]
    Name=br0
    
    [Network]
    DHCP=ipv4

####  添加选项以引导容器

若要让主机和容器取得不同 IP，需要将容器网络与主机“断开”。加入启动参数 `--network-bridge=br0`： 
    
    # systemd-nspawn --network-bridge=br0 -bD /path_to/my_container
    
####  成果

  * 宿主机上

    $ ip a
    
    3: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
        link/ether 14:da:e9:b5:7a:88 brd ff:ff:ff:ff:ff:ff
        inet 192.168.1.87/24 brd 192.168.1.255 scope global br0
           valid_lft forever preferred_lft forever
        inet6 fe80::16da:e9ff:feb5:7a88/64 scope link 
           valid_lft forever preferred_lft forever
    6: vb-_MyContainer_ : <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br0 state UP group default qlen 1000
        link/ether d2:7c:97:97:37:25 brd ff:ff:ff:ff:ff:ff
        inet6 fe80::d07c:97ff:fe97:3725/64 scope link 
           valid_lft forever preferred_lft forever
    
  * 容器中

    $ ip a
    
    2: host0: <BROADCAST,MULTICAST,ALLMULTI,AUTOMEDIA,NOTRAILERS,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 5e:96:85:83:a8:5d brd ff:ff:ff:ff:ff:ff
        inet 192.168.1.73/24 brd 192.168.1.255 scope global host0
           valid_lft forever preferred_lft forever
        inet6 fe80::5c96:85ff:fe83:a85d/64 scope link 
           valid_lft forever preferred_lft forever
    
####  注意

  * 主机的 `br0` 与容器的 `host0` 现有各自的 IP
  * 新增两个接口：主机的 `vb-_MyContainer_` 及容器的 `host0`。这是因为使用了 `--network-bridge=br0`，该选项暗示了 `--network-veth`，在主机与容器间建立虚拟以太网桥接连接。
  * 容器的 DHCP IP 是由系统 `/usr/lib/systemd/network/80-container-host0.network` 提供。
  * 主机上执行：

    $ brctl show
    
    bridge name	bridge id		STP enabled	interfaces
    br0		8000.14dae9b57a88	no		enp7s0
    							vb-_MyContainer_
    
此输出证明桥接有两个绑定接口。 

  * 宿主机上的路由表：

    $ ip route
    
    default via 192.168.1.254 dev br0 
    192.168.1.0/24 dev br0  proto kernel  scope link  src 192.168.1.87
    
  * 容器中的路由表：

    $ ip route
    
    default via 192.168.1.254 dev host0 
    192.168.1.0/24 dev host0  proto kernel  scope link  src 192.168.1.73
    
以上显示 `br0` 与 `host0` 已启用并拥有 IP 与默认网关 192.168.1.254。网关地址由 systemd-networkd 自动获取。 
    
    $ cat /run/systemd/resolve/resolv.conf
    
    nameserver 192.168.1.254
    
###  静态 IP 网络

为每个设备设置静态 IP 有利于部署 FTP、HTTP、SSH 等服务。只要系统中的 `/usr/lib/systemd/network/99-default.link` 包含 `MACAddressPolicy=persistent`（默认启用），每台设备重启后都会保留相同的 MAC 地址，方便将服务路由到目标设备。 

配置步骤如下： 

主机端 

配置与 [#DHCP 用于两个独立 IP](<#DHCP_%E7%94%A8%E4%BA%8E%E4%B8%A4%E4%B8%AA%E7%8B%AC%E7%AB%8B_IP>) 类似。先创建虚拟桥接接口并绑定实体网卡，通过以下两个文件实现： 

/etc/systemd/network/_MyBridge_.netdev /etc/systemd/network/_MyEth_.network 

然后为虚拟桥接接口设置 IP 和 DNS，示例如下： 
    
    /etc/systemd/network/_MyBridge_.network
    
    [Match]
    Name=br0
    
    [Network]
    DNS=192.168.1.254
    Address=192.168.1.87/24
    Gateway=192.168.1.254
    
容器端 

先移除系统默认提供的 DHCP 配置文件 `/usr/lib/systemd/network/80-container-host0.network`，以永久方式（例如 [systemd](<https://archlinux.org/packages/?name=systemd>)包 更新后仍然生效）在容器中执行： 

  1. ln -sf /dev/null /etc/systemd/network/80-container-host0.network

若只想在主机端使用静态 IP，容器仍通过 DHCP 获取 IP，则可以保留此文件。 

然后为默认接口 `host0` 设置静态 IP，并在容器中 [enable and start](</wzh/index.php?title=Enable_and_start&action=edit&redlink=1> "Enable and start（页面不存在）") `systemd-networkd.service`，示例如下： 
    
    /etc/systemd/network/_MyVeth_.network
    
    [Match]
    Name=host0
    
    [Network]
    DNS=192.168.1.254
    Address=192.168.1.94/24
    Gateway=192.168.1.254
    
##  提示与技巧

###  交互界面及桌面集成

_systemd-networkd_ 并不提供图形交互式管理界面。但仍有一些工具可以用于显示或修改当前网络状态、接收通知或处理无线网络配置： 

  * _networkctl_ 提供了一个命令行接口，用于查询或修改网络接口状态。值得注意的是，若只想修改接口的某些行为，需要先[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Append,_add,_create,_edit> "Help:Reading")一项或多项位于 `/etc/systemd/network/` 中的配置文件。
  * 当 _networkd_ 配置了 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant") 时， _wpa_cli_ 和 _wpa_gui_ 可用于动态关联与配置 WLAN 接口。
  * [networkd-dispatcher](<https://aur.archlinux.org/packages/networkd-dispatcher/>)AUR 服务允许在网络接口状态变化时执行脚本，功能类似于 _NetworkManager-dispatcher_ 。
  * [networkd-notify-git](<https://aur.archlinux.org/packages/networkd-notify-git/>)AUR 会在接口状态发生变化时生成简单通知消息。
  * 作为 DNS 解析器， _systemd-resolved_ 可以通过 `resolvectl status` 命令可视化当前 DNS 服务器信息。

###  基于 SSID（位置）配置静态 IP 或 DHCP

常见场景中，家庭无线使用 DHCP，而公司无线则使用静态 IP。这种混合设置可通过如下方式配置： 

**注意：** 文件名中的数字决定了处理顺序。用户可以在 [Match] 区段按 SSID、BSSID 或两者同时匹配。
    
    /etc/systemd/network/24-wireless-office.network
    
    # 专门用于办公 Wi‑Fi 的配置
    [Match]
    Name=wlp2s0
    SSID=office_ap_name
    #BSSID=aa:bb:cc:dd:ee:ff
    
    [Network]
    Address=10.1.10.9/24
    Gateway=10.1.10.1
    DNS=10.1.10.1
    #DNS=8.8.8.8
    
    /etc/systemd/network/25-wireless-dhcp.network
    
    # 对其他任何 Wi‑Fi 网络使用 DHCP
    [Match]
    Name=wlp2s0
    
    [Link]
    RequiredForOnline=routable
    
    [Network]
    DHCP=yes

###  有线与无线接口绑定

参见 [Wireless bonding](<../zh-cn/Wireless_bonding.html> "Wireless bonding")。 

绑定（bonding）允许通过多个接口共享连接，例如当有线接口断开时，无线仍保持连接，网络不中断。 

创建一个 bond 接口，此处使用的模式为 _active‑backup_ ，即如果主接口断开，则切换到备份接口： 
    
    /etc/systemd/network/30-bond0.netdev
    
    [NetDev]
    Name=bond0
    Kind=bond
    
    [Bond]
    Mode=active-backup
    PrimaryReselectPolicy=always
    MIIMonitorSec=1s

将有线接口设为主接口： 
    
    /etc/systemd/network/30-ethernet-bond0.network
    
    [Match]
    Name=enp0s25
    
    [Network]
    Bond=bond0
    PrimarySlave=true

将无线接口设为备份接口： 
    
    /etc/systemd/network/30-wifi-bond0.network
    
    [Match]
    Name=wlan0
    
    [Network]
    Bond=bond0

**注意：** 在 `[Match]` 区段使用 MAC 地址时，建议使用 `PermanentMACAddress` 而非 `MACAddress`，详见 [upstream 讨论](<https://github.com/systemd/systemd/issues/27432>)。

像配置普通接口一样配置 bond 接口： 
    
    /etc/systemd/network/30-bond0.network
    
    [Match]
    Name=bond0
    
    [Link]
    RequiredForOnline=routable
    
    [Network]
    BindCarrier=enp0s25 wlan0
    DHCP=yes

现在，如果有线网络断开，系统将自动切换到无线连接，保持联网状态： 
    
    $ networkctl
    
    IDX LINK    TYPE     OPERATIONAL      SETUP     
      1 lo      loopback carrier          unmanaged 
      2 enp0s25 ether    no-carrier       configured
      3 bond0   bond     degraded-carrier configured
      5 wlan0   wlan     enslaved         configured
    
    4 links listed.
    
###  加快 TCP 慢启动过程

在带宽较高（如 >10 Mbit/s）且延迟中等的连接（如家庭宽带）上，TCP 默认的慢启动算法偏保守，会导致下载初期速度较慢，需要数秒才能达到满速。在使用 pacman 更新包时尤其明显，每个包下载都从较慢速率起步，常在加速完成前就结束。 

通过调整以下参数，可以让 TCP 连接以更大窗口启动，从而避免慢启动阶段造成的性能损失[[1]](<https://www.cdnplanet.com/blog/tune-tcp-initcwnd-for-optimum-performance/>)。虽然在低速连接或设置过高的情况下会因丢包而降低性能，但在带宽充足的环境下可显著提升体验。 

使用前后请务必进行基准测试，以确认网络实际获得提升；若下载已经没有慢启动问题，则无需调整。测试时，应对高低速服务器都做测试，避免提升高速连接却牺牲低速访问。 

编辑对应连接的 `.network` 文件以调整： 
    
    /etc/systemd/network/eth0.network
    
    [Match]
    Name=eth0
    
    #[Network]
    #Gateway=...  <-- 如果已存在，则删除并在下面 Route 中指定
    
    [Route]
    # 此选项适用于 DHCP 提供的网关，如手动指定网关，也应写在这里。
    Gateway=_dhcp4
    
    # 以下为默认值 10，单位为 MSS (1460 字节) 的倍数
    InitialCongestionWindow=10
    InitialAdvertisedReceiveWindow=10

默认值 `10` 适合 <10 Mbit/s；若你是 100 Mbit/s 连接，建议使用 `30`。手册 [systemd.network(5) § [ROUTE] SECTION OPTIONS](<https://man.archlinux.org/man/systemd.network.5#%5BROUTE%5D_SECTION_OPTIONS>) 表示 `100` 属于过高。 

若启用 sysctl 设置 `net.ipv4.tcp_slow_start_after_idle`，当连接空闲一段时间后，TCP 将回到上述初始值；若禁用，则保留协商后的更大窗口。无论设置如何，每个 **新 TCP 连接** 都从上述 Initial* 值开始。 

sysctl 参数 `net.ipv4.tcp_congestion_control` 决定拥塞期间窗口的动态调整，与 Initial* 设置无直接关系。Initial* 仅控制每条 TCP 新连接的初始窗口，后续仍由拥塞算法调整。提高初始值可以减少协商延迟，但若设置不当，会适得其反。 

###  防止多个默认路由冲突

_systemd-networkd_ [未按接口类型设置默认路由度量](<https://github.com/systemd/systemd/issues/17698>)，使用多个网络设备时，需手动设置度量值。例如，下列 `ip route` 输出显示多个默认路由： 
    
    ip route
    
    default via 10.30.1.1 dev eno2 proto dhcp src 10.30.1.15 metric 1024
    default via 192.168.1.254 dev eno1 proto dhcp src 172.18.105.104 metric 1024

由于度量值一致，系统会产生竞争条件。根据接口启用顺序选择默认路由，例如 eno2 先启用则被优先选中，可能导致 eno1 可用时却被忽略。 

为避免此问题，应为各接口设置不同的 `RouteMetric=` 值。参考 [#有线与无线接口绑定](<#%E6%9C%89%E7%BA%BF%E4%B8%8E%E6%97%A0%E7%BA%BF%E6%8E%A5%E5%8F%A3%E7%BB%91%E5%AE%9A>)区段的示例。 

如某设备不应成为默认路由源，可在其 .network 中使用 `UseRoutes=false` 选项，忽略 DHCP 提供的路由条目。该配置对于仅连接至另一台设备时特别有用。 

###  在已有接口上配置第二个静态 IP 及其独立 MAC

若希望系统在路由器中识别为两个不同设备，可为某接口创建拥有独立 IP 和 MAC 的虚拟接口。 

在物理接口上添加一个 macvlan 虚拟接口并指定唯一 MAC： 
    
    /etc/systemd/network/25-eth210.netdev
    
    [NetDev]
    Name=_eth210_
    Kind=macvlan
    MACAddress=_00:11:22:33:44:55_
    
    [MACVLAN]
    Mode=bridge

然后为该虚拟接口创建配置文件，使用相同子网和网关，但 IP 避开 DHCP 分配范围： 
    
    /etc/systemd/network/25-eth210.network
    
    [Match]
    Name=_eth210_
    
    [Network]
    Address=_192.168.132.210/24_
    Gateway=_192.168.132.1_
    
    [Route]
    Destination=_192.168.132.0/24_
    Metric=2

该虚拟 macvlan 接口的路由度量定为 2，因此除非特别指定，否则系统会优先通过主接口（度量值为默认 1）访问网络。 

最后，请在主接口的 `.network` 文件的 `[Network]` 段中添加 `MACVLAN=eth210`！ 

为了让路由器“认识”这个新 MAC 地址并接受它，可作为 root 运行 `arping -I eth210 192.168.132.1`。配置路由器后，你可以测试虚拟接口的互联网连通性，例如运行：`curl --interface 192.168.132.210 ifconfig.me`应会返回你的公网 IP。 

##  故障排查

###  启动时“挂载”服务失败

如果你运行的是 [Samba](<../zh-cn/Samba.html> "Samba") 或 [NFS](<../zh-cn/NFS.html> "NFS") 等服务，而它们在网络尚未启动时就尝试启动而失败，可以考虑 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `systemd-networkd-wait-online.service`。不过这通常不是必要的，因为大多数网络服务即使网络尚未完全配置，也能正常启动。 

###  systemd-resolve 不搜索本地域

[systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 在仅提供主机名时，可能不会自动搜索本地域，即使相应的 _.network_ 文件中设定了 `UseDomains=yes` 或 `Domains=[domain-list]`，并且在 `resolv.conf` 中正确生成了 `search [domain-list]`。 

你可以通过运行 `networkctl status` 或 `resolvectl status` 来确认搜索域是否被正确读取。 

可能的解决方案： 

禁用 [LLMNR](<../zh-cn/Systemd-resolved.html#LLMNR> "Systemd-resolved")，让 systemd-resolved 立即继续尝试 DNS 后缀。 

简化 `/etc/nsswitch.conf` 中 `hosts` 条目（例如移除 `[!UNAVAIL=return]`）。 

使用完整限定域名（FQDN）。 

使用 `/etc/hosts` 解析主机名。 

放弃使用 systemd 的 `resolve`，改用 glibc 的 DNS 解析方式。 

###  第二台电脑无法使用桥接网络

如果第一台电脑有两个 LAN 接口，第二台电脑只有一个 LAN 并连接到第一台电脑，那么为了让第二台电脑能够通过桥接接口访问所有网络，需要执行以下命令： 
    
    # sysctl net.bridge.bridge-nf-filter-pppoe-tagged=0
    # sysctl net.bridge.bridge-nf-filter-vlan-tagged=0
    # sysctl net.bridge.bridge-nf-call-ip6tables=0
    # sysctl net.bridge.bridge-nf-call-iptables=0
    # sysctl net.bridge.bridge-nf-call-arptables=0
    
##  参阅

  * [systemd.networkd man page](<https://www.freedesktop.org/software/systemd/man/systemd-networkd.service.html>)
  * [Tom Gundersen, main systemd-networkd developer, G+ home page](<https://plus.google.com/u/0/+TomGundersen/posts>)
  * [Tom Gundersen posts on Core OS blog](<https://coreos.com/blog/intro-to-systemd-networkd/>)
  * [How to set up systemd-networkd with wpa_supplicant](<https://bbs.archlinux.org/viewtopic.php?pid=1393759#p1393759>) (WonderWoofy's walkthrough on Arch forums)
