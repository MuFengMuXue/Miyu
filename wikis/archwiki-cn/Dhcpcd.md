**翻译状态：**

  * 本文（或部分内容）译自 [Dhcpcd](<https://wiki.archlinux.org/title/Dhcpcd> "arch:Dhcpcd")，最近一次同步于 2024-08-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dhcpcd?diff=0&oldid=806181>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dhcpcd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")
  * [无线网络配置](</wzh/index.php?title=%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE&action=edit&redlink=1> "无线网络配置（页面不存在）")
  * [dhcpd](<../zh-cn/Dhcpd.html> "Dhcpd")

_dhcpcd_ 是 DHCP 和 DHCPv6 客户端，是目前功能最丰富的开源 DHCP 客户端。[项目主页](<https://roy.marples.name/projects/dhcpcd>)包含了完整的功能列表。 

**注意：** Roy Marple 的 _dhcpcd_ （DHCP **client** daemon）和 Internet Systems Consortium 的 [dhcpd](<../zh-cn/Dhcpd.html> "Dhcpd")（DHCP **(server)** daemon）是不同的软件。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [dhcpcd](<https://archlinux.org/packages/?name=dhcpcd>)包。 

[dhcpcd-ui](<https://aur.archlinux.org/packages/dhcpcd-ui/>)AUR 是 dhcpcd 和 [GTK](<../zh-cn/GTK.html> "GTK") 前端，提供了对 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant") 的可选支持。功能包括配置对话框、输入无线网络的密码等。 

##  运行

要为 _所有的_ 网络接口启动守护进程，[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `dhcpcd.service`。 

要单独为指定的网络接口启动守护进程，[启动或启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")模板单元 `dhcpcd@_interface_.service`，其中的 _interface_ 名可从[这里](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Listing_network_interfaces> "网络配置")查询。 

建议使用模板单元方式，详情请参阅 [#dhcpcd 和 systemd 网络接口](<#dhcpcd_%E5%92%8C_systemd_%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3>)。无论哪种方式都会分配一个动态 IP 地址。要分配静态 IP 地址，请参阅 [#静态配置](<#%E9%9D%99%E6%80%81%E9%85%8D%E7%BD%AE>)。 

##  配置

主配置文件是 `/etc/dhcpcd.conf`，详情请参考 [dhcpcd.conf(5)](<https://man.archlinux.org/man/dhcpcd.conf.5>)，下面会介绍一些常用选项。 

###  DHCP 静态路由

如果要在客户端设置静态路由，请使用 `/etc/dhcpcd.exit-hook`。下面的例子中添加了一个 VPN 子网 `10.11.12.0/24` 到网关 `192.168.192.5` 的静态路由： 
    
    /etc/dhcpcd.exit-hook
    
    ip route add 10.11.12.0/24 via 192.168.192.5
    
可以在文件中配置多个路由。 

###  DHCP 客户端标识

服务器可以通过下列方式不同的 DHCP 客户端： 

  1. 主机名（或客户端发送的主机名），
  2. 所用网卡的 MAC 地址，
  3. Identity Association ID（身份关联 ID IAID），区分不同使用场景或接口的标识，
  4. DHCP 唯一标识（DUID）。

详情请参考 [RFC 3315](<https://tools.ietf.org/html/rfc3315#section-4.2> "rfc:3315")。 

DHCP 服务器通过配置决定申请 DHCP IP 租约时，哪些是必须的，哪些是可选的。 

**注意：** _dhcpcd_ 默认配置的是最常用的方式。服务器会自动确认上述标识，只有在出现问题时才需要额外配置。

如果无法通过 _dhcpcd_ 默认配置获取 IP 地址，可以在 `dhcpcd.conf` 中尝试如下配置： 

  * `hostname` 发送 `/etc/hostname` 中配置的主机名
  * `clientid` 发送 MAC 地址作为标识
  * `iaid <interface>` 生成并发送 IAID,可以在接口块（`interface <interface>`）中使用，参考：[[1]](<https://bbs.archlinux.org/viewtopic.php?pid=1388376#p1388376>))，下面的选项更常用：
  * `duid` 将联合使用 DUID 和 IAID 作为标识。

DUID 的数值配置在 `/var/lib/dhcpcd/duid` 中，为了保证 DHCP 租约的有效性，需要保证 DUID 在整个网络中是唯一的，而 IAID 需要能区分每一个接口（[RFC 4361](<https://tools.ietf.org/html/rfc4361#section-6.1> "rfc:4361")）。 

如果运行的是[动态 DNS](<https://en.wikipedia.org/wiki/Dynamic_DNS> "wikipedia:Dynamic DNS")，请确保三个都是唯一的。如果网络中出现重复的 DUID，例如克隆的虚拟机中，有不同的主机名和 MAC 地址，但是没有修改 DUID 时，最新获取IP地址的客户端会清除之前 DUID 获取的地址。 

###  静态配置

需要的配置在[网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")中均有说明，通常包含[网络接口](</wzh/index.php?title=Network_interface&action=edit&redlink=1> "Network interface（页面不存在）")名称、IP 地址、路由地址和域名服务器。 

在 `/etc/dhcpcd.conf` 中为 _dhcpcd_ 配置静态地址： 
    
    /etc/dhcpcd.conf
    
    interface eth0
    static ip_address=192.168.0.10/24	
    static routers=192.168.0.1
    static domain_name_servers=192.168.0.1 8.8.8.8

还可以进行更复杂的配置，比如 `arping` 选项，详情请参考 [dhcpcd.conf(5)](<https://man.archlinux.org/man/dhcpcd.conf.5>)。 

####  备用配置

可以为 _dhcpcd_ 添加备用设置，当 DHCP 续租失败时使用。这对于[无显示设备机器](<https://en.wikipedia.org/wiki/Headless_computer> "wikipedia:Headless computer")特别有用，动态地址无法获取时，使用静态地址作为备用，确保机器有可用的网络连接。 

下面示例为 `static_eth0` 配置了 `192.168.1.23` 静态地址，`192.168.1.1` 网关，并将此配置设置为 `eth0` 的备用配置。 
    
    /etc/dhcpcd.conf
    
    # define static profile
    profile static_eth0
    static ip_address=192.168.1.23/24
    static routers=192.168.1.1
    static domain_name_servers=192.168.1.1
    
    # fallback to static profile on eth0
    interface _eth0_
    fallback static_eth0

##  钩子

_dhcpcd_ 会按字母顺序执行 `/usr/lib/dhcpcd/dhcpcd-hooks/` 中配置的钩子，详情请参考 [dhcpcd.conf(5)](<https://man.archlinux.org/man/dhcpcd.conf.5>) 和 [dhcpcd-run-hooks(8)](<https://man.archlinux.org/man/dhcpcd-run-hooks.8>)。 

**注意：**

  * 可以在 `dhcpcd.conf` 中使用 `nohook` 禁用钩子。
  * 可以用 `env` 选项为所有钩子设置环境变量。例如要强制设置主机名，请使用 `env force_hostname=YES`。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** describe (at least some) provided hooks. (在 [Talk:Dhcpcd](<../zh-cn/Talk:Dhcpcd.html>) 中讨论)

### 10-wpa_supplicant

通过创建一个符号链接启用这个钩子，不仅可以在当版本中使用，后期程序更新时也可使用： 
    
    # ln -s /usr/share/dhcpcd/hooks/10-wpa_supplicant /usr/lib/dhcpcd/dhcpcd-hooks/
    
如果启用了 `10-wpa_supplicant` 钩子，将会在无线接口上自动加载 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant")，它仅在以下情况开启： 

  * 不存在已在接口上监听的 _wpa_supplicant_ 进程。
  * 至少存在一个 _wpa_supplicant_ 配置文件。默认情况下， _dhcpcd_ 将会按顺序检查以下配置文件：

    /etc/wpa_supplicant/wpa_supplicant-_interface_.conf
    /etc/wpa_supplicant/wpa_supplicant.conf
    /etc/wpa_supplicant-_interface_.conf
    /etc/wpa_supplicant.conf
    
但也可通过设置 `env wpa_supplicant_conf=_configuration_file_path_` 在 `/etc/dhcpcd.conf` 中添加自定义配置文件路径。 

**注意：** 钩子会在找到第一个配置文件时停止执行，因此，如果您有多个 _wpa_supplient_ 配置文件，则应该考虑到这一点，否则“dhcpcd”可能会使用错误的配置文件。

如果您通过 _wpa_supplicant_ 管理您的无线连接，钩子可能会创建一些不必要的连接事件。例如，如果您关闭了 _wpa_supplicant_ ，钩子可能会使无线接口再次打开。此外，如果您正在使用 [netctl-auto](<../zh-cn/Netctl.html#Special_systemd_units> "Netctl")， _wpa_supplicant_ 将会根据 `/run/network/wpa_supplicant__interface_.conf` 配置文件自动启动。因此，从钩子重新启动接口是不必要的，并且可能会导致 `/etc/wpa_supplicant/wpa_supplicant.conf` 文件在启动时解析错误，因为该文件在默认打包的版本中只包含虚拟的预设值。通过移出添加钩子的符号链接以禁用钩子，或者向 `dhcpcd.conf` 中添加 `nohook wpa_supplicant` 参数以解决这个问题。 

##  小技巧

###  禁用 ARP 探测加速 DHCP 响应

dhcpcd 在内部实现了 DHCP 标准提议（[RFC 2131](<https://tools.ietf.org/html/rfc2131#section-2.2> "rfc:2131")），以通过 ARP 探测验证指定 IP 地址是否已被其他设备使用，在家庭网络环境下这通常是不必要的，因此，可以通过禁用 ARP 探测在每次连接时节约 5 秒左右的时间： 
    
    /etc/dhcpcd.conf
    
    noarp
    
相当于将 `--noarp` 参数传递给 `dhcpcd`，并禁用 ARP 探测，从而加快使用 DHCP 连接到网络的速度。 

###  移除旧的 DHCP 租约

在文件 `/var/lib/dhcpcd/_interface_.lease` 中，` _interface_` 是获得租约的接口名称，包含 DHCP 服务器发送的实际可用的 DHCP 租约响应。对一个无线接口来说，文件名则为 `/var/lib/dhcpcd/_interface_ -_ssid_.lease`，其中 `_ssid_` 是无线网络名称。这些文件用于确定服务器分配的最近一个租约，文件的 `mtime` 属性用于确定租约的公告时间。如果最近的租约信息可用，则该租约信息将用于请求先前在网络上使用的相同 IP 地址，如果您不想要这样做，只需删除这些文件即可。 

如果 DHCP 服务器仍然分配相同的 IP 地址，可能是因为服务器被配置为保持固定分配并且识别出了客户端发送的客户端 id（client id）或者是 DUID（详见 [#DHCP 客户端标识](<#DHCP_%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%A0%87%E8%AF%86>)），您可以通过停止 _dhcpcd_ 并移除或重命名 `/var/lib/dhcpcd/duid` 文件来进行测试， _dhcpcd_ 会在下次运行时重新生成这个文件。 

请注意，DUID 旨在作为重启后和不同接口之间的持久化的机器标识符。如果要将系统迁移到新计算机上，则不应该留存这个文件。 

###  多重引导获取不同 IP 地址

如果您使用双引导 Arch 和 macOS 或者是 Windows，并且每个系统想要获得不同的 IP 地址，您可以通过在每个操作系统指定不同的 DUID 来控制获得的 IP 地址。 

在 Windows 下 DUID 应该保存在以下注册键下： 
    
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters\Dhcpv6DUID
    
macOS 中可以在 `Network\adapter\dhcp preferences panel` 中直接访问修改。 

如果您使用 [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq") 作为 DHCP 服务器，可以在其配置文件中通过恰当指定 `dhcp-host=` 规则来使用不同的 DUID。 

###  /etc/resolv.conf

如果系统上 [resolvconf](</wzh/index.php?title=Resolvconf&action=edit&redlink=1> "Resolvconf（页面不存在）")（英语：[resolvconf](<https://wiki.archlinux.org/title/resolvconf> "en:resolvconf")） 可用，DNS 信息将会发送给它处理，否则， _dhcpcd_ 将会自行将 DNS 信息写入 _`/etc/resolv.conf`_ 。可以通过禁用 `/usr/lib/dhcpcd/dhcpcd-hooks/20-resolv.conf` 钩子防止 _dhcpcd_ 重写 `/etc/resolv.conf` 文件，只需在 `/etc/dhcpcd.conf` 最后一段中添加以下内容即可： 
    
    nohook resolv.conf
    
注意，一般来说，禁用此钩子也会使 dhcpcd 禁用 resolvconf。 

或者，您可以创建一个名为 `/etc/resolv.conf.head` 的文件，其中包含您的 DNS 服务器信息。dhcpcd 将把这个文件的内容放在 `/etc/resolv.conf` 的开头。 

或者，您可以将 dhcpcd 配置为每次使用相同的 DNS 服务器。想要这么做，请在 `/etc/dhcpcd.conf` 的末尾添加以下行，其中 `_dns-server-ip-addressses_` 是一个以空格分隔的 DNS IP 地址列表。 
    
    static domain_name_servers=_dns-server-ip-addresses_
    
例如，要设置 Google DNS 服务器： 
    
    static domain_name_servers=8.8.8.8 8.8.4.4
    
**提示：** 当使用 [openresolv](</wzh/index.php?title=Openresolv&action=edit&redlink=1> "Openresolv（页面不存在）")（英语：[openresolv](<https://wiki.archlinux.org/title/openresolv> "en:openresolv")） 时，可以在 `/etc/resolvconf.conf` 中设置 DNS 服务器地址，这样，它们就不会被任何支持 _resolvcconf_ 的软件覆盖。

##  问题解决

###  客户端 ID

如果您处在根据 MAC 地址过滤客户端 ID 的 DHCPv4 的网络中，则可能需要更改以下行： 
    
    /etc/dhcpcd.conf
    
    # 根据 RFC4361，DHCPv4 使用和 DHCPv6 相同的 DUID+IAID 作为客户端 ID。
    duid
    
改为： 
    
    /etc/dhcpcd.conf
    
    # 使用接口的硬件地址作为客户端 ID（DHCPv4）。
    clientid
    
否则，您可能无法获得租约，因为 DHCP 服务器可能无法正确读取 [DHCPv6-风格](<https://en.wikipedia.org/wiki/DHCPv6> "wikipedia:DHCPv6")的客户端 ID。有关更多信息，请参阅 [RFC 4361](<https://tools.ietf.org/html/rfc4361> "rfc:4361")。 

###  通过先释放 IP 地址检查 DHCP 问题

此问题可能在 DHCP 获得错误的 IP 分配时发生，例如当两个路由器通过 VPN 相连时。路由器通过 VPN 连接分配到了地址。要修复该问题，请以 root 身份释放该 IP 地址： 
    
    # dhcpcd -k
    
然后请求一个新地址： 
    
    # dhcpcd
    
您可能需要多次运行这两个命令。 

###  路由器不兼容导致的问题

对于某些（不兼容的）路由器，除非您注释掉 `/etc/dhcpcd.conf` 中的以下行，否则无法正确连接。 
    
    require dhcp_server_identifier
    
除非您的网络上有多个 DHCP 服务器（非典型），否则这不会导致问题，详情请见[这个页面](<https://technet.microsoft.com/en-us/library/cc977442.aspx>)。 

###  dhcpcd 和 systemd 网络接口

可以在不指定接口的情况下[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `dhcpcd.service`。但系统启动时，该单元可能会在 _systemd-udevd_ 尝试应用一个可预测的网络接口名称时与其产生竞争状态： 
    
    error changing net interface name wlan0 to wlp4s0: Device or resource busy" 
    
要避免该问题，请根据 [dhcpcd.conf(5)](<https://man.archlinux.org/man/dhcpcd.conf.5>)，使用 `denyinterfaces` 或 `allowinterfaces` 以阻止 dhcpcd 绑定至内核名称，例如： 
    
    denyinterfaces wlan* eth*
    
也可如 [#运行](<#%E8%BF%90%E8%A1%8C>)中所述，为每个接口启用 _dhcpcd_ 。但是，模板单元也有缺点，它不支持有线连接的热插拔，且如果没有连接网线就会失败。为解决这个问题，请参见 [#超时延迟](<#%E8%B6%85%E6%97%B6%E5%BB%B6%E8%BF%9F>)。 

###  超时延迟

如果 dhcpcd 在单个接口上运行，且在 30 秒后未能获得租约（例如，当服务器未准备好或网线未插入时），它将退出并返回错误。 

要让 _dhcpcd_ 无限期等待一次，请[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")单元并将`timeout` 设置为 `0`： 
    
    /etc/systemd/system/dhcpcd@.service.d/timeout.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dhcpcd -w -q **-t 0** %I

令单元在退出后重启以使其无限期等待： 
    
    /etc/systemd/system/dhcpcd@.service.d/dhcpcdrestart.conf
    
    [Service]
    Restart=always

##  已知问题

###  dhcpcd@.service 降低启动速度

在默认配置中， _dhcpcd_ 的标识 `-w` 会使 `dhcpcd@.service` 在进入后台守护进程前等待 IP 地址的获取。如果启用了该单元，可能会导致启动时暂停并等待 IP 地址分配以继续启动流程。要修复该问题，请为该单元创建如下的[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")： 
    
    /etc/systemd/system/dhcpcd@.service.d/no-wait.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dhcpcd -b -q %I

另请参阅 [FS#49685](<https://bugs.archlinux.org/task/49685>)。 

##  参阅

  * [dhcpcd(8)](<https://man.archlinux.org/man/dhcpcd.8>)
  * [dhcpcd.conf(5)](<https://man.archlinux.org/man/dhcpcd.conf.5>)
