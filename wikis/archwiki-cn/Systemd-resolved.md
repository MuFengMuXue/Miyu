相关文章

  * [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")
  * [域名解析](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "域名解析")

**翻译状态：**

  * 本文（或部分内容）译自 [Systemd-resolved](<https://wiki.archlinux.org/title/Systemd-resolved> "arch:Systemd-resolved")，最近一次同步于 2025-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd-resolved?diff=0&oldid=823402>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd-resolved_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

_systemd-resolved_ 是一个通过[D-Bus](<../zh-cn/D-Bus.html> "D-Bus")接口、[NSS](</wzh/index.php?title=Name_Service_Switch&action=edit&redlink=1> "Name Service Switch（页面不存在）")([nss-resolve(8)](<https://man.archlinux.org/man/nss-resolve.8>))解析服务和一个监听`127.0.0.53`的本地DNS解析器为本地应用提供网络名称解析的[systemd](<../zh-cn/Systemd.html> "Systemd")服务。 

##  安装

_systemd-resolved_ 是默认安装的[systemd](<https://archlinux.org/packages/?name=systemd>)包包的一部分。 

##  配置

_systemd-resolved_ 为DNS（包括DNSSEC和Dns over TLS）、多播DNS（mDNS）和链路本地多播名称解析（LLMNR）提供解析服务。 

可以通过编辑`/etc/systemd/resolved.conf`或 `/etc/systemd/resolved.conf.d/`中的[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")文件来配置解析器。请参阅[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)。 

要使用 _systemd-resolved_ ，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")`systemd-resolved.service`。 

**提示：** 要了解有关选项和开关的上下文，可以如[Systemd#诊断一个服务](<../zh-cn/Systemd.html#%E8%AF%8A%E6%96%AD%E4%B8%80%E4%B8%AA%E6%9C%8D%E5%8A%A1> "Systemd")中所述打开 _systemd-resolved_ 的详细调试信息。

### DNS

依赖 glibc [getaddrinfo(3)](<https://man.archlinux.org/man/getaddrinfo.3>)（或类似API）的软件直接就能使用。如果存在[nss-resolve(8)](<https://man.archlinux.org/man/nss-resolve.8>)，`/etc/nsswitch.conf`的默认配置将使用它进行主机名解析。 

有些软件会直接读取`/etc/resolv.conf`进行域名解析，例如网络浏览器、Go 和 GnuPG 等，为了支持这些软件， _systemd-resolved_ 提供了四种不同的文件处理模式：本地、静态、上联和外部（file-stub, static, uplink和foreign），[systemd-resolved(8) § /ETC/RESOLV.CONF](<https://man.archlinux.org/man/systemd-resolved.8#/ETC/RESOLV.CONF>)中对这些方式进行了详细说明。 

`/run/systemd/resolve/stub-resolv.conf`包含作为唯一DNS服务器和搜索域名的本地存根`127.0.0.53`。这是将 _systemd-resolved_ 托管配置传播到所有客户端的推荐操作模式。要使用它，将`/etc/resolv.conf`替换为指向它的符号链接： 
    
    # ln -sf ../run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
    
**注意：**

  * 以`../`开头的目标路径是 _相对于链接位置的_ ，而不是当前目录。
  * 未正确配置`/etc/resolv.conf`将会导致DNS解析中断。
  * 在 _arch-chroot_ 内部时将无法创建`/etc/resolv.conf`符号链接，因为该文件从外部系统绑定安装。应该在chroot外创建符号链接。例如： 
        
        # ln -sf ../run/systemd/resolve/stub-resolv.conf _/mnt_ /etc/resolv.conf

####  设置DNS服务器

**提示：** 要检查 _systemd-resolved_ 当前正在使用的DNS, 请运行`resolvectl status`.

#####  自动配置

对于使用`/etc/resolv.conf`的网络管理器， _systemd-resolved_ 将开箱即用，不需要特定的配置，因为 _systemd-resolved_ 将通过`/etc/resolv.conf`符号链接探测，[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")、[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")和[iwd](<../zh-cn/Iwd.html> "Iwd")就是这样。 

但是，如果DHCP和VPN客户端使用[resolvconf](<https://en.wikipedia.org/wiki/resolvconf> "wikipedia:resolvconf")程序来设置名称服务器和搜索域名（请参阅[[1]](<https://wiki.archlinux.org/title/Openresolv#Users>)来获得使用 _resolvconf_ 程序的软件的列表）则需要额外的软件包[systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包来提供`/usr/bin/resolvconf`符号链接。 

**注意：**

  * _systemd-resolved_ 有一个受限的 _resolvconf_ 接口，可能与所有客户端一起工作，请参阅 [resolvectl(1) § COMPATIBILITY WITH RESOLVCONF(8)](<https://man.archlinux.org/man/resolvectl.1#COMPATIBILITY_WITH_RESOLVCONF\(8\)>)来获得更多信息。
  * [systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包只在`systemd-resolved.service`运行时才工作。 如果你没有使用 _systemd-resolved_ 确保[systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包包已经删除，否则会导致需要使用`/usr/bin/resolvconf`二进制文件的网络软件出问题。

#####  手动配置

在本地（stub）和静态（static）模式中，自定义DNS服务器可以在[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)文件中设置： 
    
    /etc/systemd/resolved.conf.d/dns_servers.conf
    
    [Resolve]
    DNS=192.168.35.1 fd7b:d0bd:7a6e::1
    Domains=~.

**注意：**

  * 在[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)中没有`Domains=~.`选项时，如果在per-link的配置中，其中任何一个设置了`Domains=~.`， _systemd-resolved_ 可能使用每per-link的DNS服务器。
  * 此选项不会影响任何在per-link配置中指定了更具体的搜索域名的域名解析.

要获得更多关于per-link配置的信息，请参阅[Systemd-networkd#network_文件](<../zh-cn/Systemd-networkd.html#network_%E6%96%87%E4%BB%B6> "Systemd-networkd")。 

#####  备用

如果 _systemd-resolved_ 没有从网络管理器收到任何DNS服务器地址并且没有DNS服务器在[Systemd-resolved#手动配置](<#%E6%89%8B%E5%8A%A8%E9%85%8D%E7%BD%AE>)中配置了， _systemd-resolved_ 会回退到备用DNS地址来确保DNS解析始终工作。 

**注意：** 备用DNS依次为：Cloudflare、Quad9和Google。请参阅定义DNS服务器的[systemd PKGBUILD](<https://gitlab.archlinux.org/archlinux/packaging/packages/systemd/-/blob/6a2bc5773a560688e6c12ab4bcfec87df6092ec1/PKGBUILD#L124-133>)。

地址可以通过编辑[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)中的`FallbackDNS`来更改，例如： 

    /etc/systemd/resolved.conf.d/fallback_dns.conf
    
    [Resolve]
    FallbackDNS=127.0.0.1 ::1

要禁用备用DNS功能，请在不指定任何地址的情况下设置`FallbackDNS`： 
    
    /etc/systemd/resolved.conf.d/fallback_dns.conf
    
    [Resolve]
    FallbackDNS=

#### DNSSEC

**警告：** 截至2023年6月， _systemd-resolved_ 中的DNSSEC支持被认为是实验性和不完整的。[[2]](<https://github.com/systemd/systemd/issues/25676#issuecomment-1634810897>) 因此，[systemd](<https://archlinux.org/packages/?name=systemd>)包默认禁用DNSSEC验证。

可以通过更改[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)中的`DNSSEC`设置来启用DNSSEC验证。 

  * 设置`DNSSEC=allow-downgrade`以仅在上游DNS服务器支持DNSSEC的情况下验证DNSSEC。

  * 设置`DNSSEC=true`以始终验证DNSSEC，因此停止不支持它的名称服务器的DNS解析。例如：

    /etc/systemd/resolved.conf.d/dnssec.conf
    
    [Resolve]
    DNSSEC=true

通过查询一个具有无效签名的域名来测试DNSSEC验证： 
    
    $ resolvectl query badsig.go.dnscheck.tools
    
    badsig.go.dnscheck.tools: resolve call failed: DNSSEC validation failed: invalid
    
现在来测试一个具有有效签名的域名： 
    
    $ resolvectl query go.dnscheck.tools
    
    go.dnscheck.tools: 2604:a880:400:d0::256e:b001 -- link: enp2s0
                       142.93.10.179               -- link: enp2s0
    
    -- Information acquired via protocol DNS in 122.2ms.
    -- **Data is authenticated: yes** ; Data was acquired via local or encrypted transport: no
    -- Data from: network
    
#### DNS over TLS

DNS over TLS默认禁用。要启用它，请更改[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)中`[Resolve]`部分的`DNSOverTLS`设置。要启用对你的DNS提供商服务器证书的验证，请在DNS设置中以` _ip_address_ #_hostname_`的格式包含它们的主机名。例如： 
    
    /etc/systemd/resolved.conf.d/dns_over_tls.conf
    
    [Resolve]
    DNS=9.9.9.9#dns.quad9.net
    DNSOverTLS=yes

**注意：**

  * 如果`DNSOverTLS=yes`，使用的DNS服务器必须支持DNS over TLS，否则所有DNS请求都将失败。
  * 或者，只有当服务器支持`DNSOverTLS=opportunistic`时，才可以使用DNS over TLS。如果使用的DNS服务器不支持DNS over TLS， _systemd-resolved_ 将回退到常规的未加密DNS。

[ngrep](<https://archlinux.org/packages/?name=ngrep>)包可用于测试DNS over TLS是否工作，因为DNS over TLS始终使用853端口而且从不使用53端口。当通过DNS over TLS解析主机名时，ngrep命令53端口应该不产生输出，并且853端口应该产生加密输出。 

使用[Wireshark](<../zh-cn/Wireshark.html> "Wireshark")可以检查 TLS DNS 的详细数据包内容。 

####  额外的监听接口

默认情况下， _systemd-resolved_ 通过环回接口响应本地应用程序的DNS请求。要使 _systemd-resolved_ 在默认接口之外的额外接口或地址上响应DNS请求，请在[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)中为每个额外接口设置`DNSStubListenerExtra`选项。例如： 
    
    /etc/systemd/resolved.conf.d/additional-listening-interfaces.conf
    
    [Resolve]
    DNSStubListenerExtra=192.168.10.10
    DNSStubListenerExtra=2001:db8:0:f102::10
    DNSStubListenerExtra=192.168.10.11:9953

**提示：** 这在将 _systemd-resolved_ 用作[路由器](<../zh-cn/%E8%B7%AF%E7%94%B1%E5%99%A8.html> "路由器")的DNS服务器时非常有用。

### mDNS

_systemd-resolved_ 可以作为mDNS的解析程序和响应程序工作。 

解析器使用"_主机名_.local"命名方案提供主机名（[网络配置#设置计算机名]）解析。 

只有同时启用systemd-resolved的mDNS支持并且当前活动的网络管理器为网络连接启用了mDNS支持，mDNS才会被激活。 

_systemd-resolved_ 的mDNS支持默认启用，可以通过它的`MulticastDNS`设置禁用（请参阅[resolved.conf(5) § OPTIONS](<https://man.archlinux.org/man/resolved.conf.5#OPTIONS>)）。 

启用每个连接的mDNS支持依赖网络管理器： 

  * 对于[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，设置每个连接的设置文件的`[Network]`部分中的`MulticastDNS`选项。你可能也需要在`[Link]`部分中设置`Multicast=yes`。请参阅[systemd.network(5)](<https://man.archlinux.org/man/systemd.network.5>)。

  * 对于[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")，在网络连接的配置文件的`[connection]`部分中设置`mdns`，可以运行`nmcli connection modify _interface_name_ connection.mdns _{yes|no|resolve}_`来设置。请参阅[nm-settings(5)](<https://man.archlinux.org/man/nm-settings.5>)。

**注意：**

  * 如果安装了Avahi，请考虑禁用或屏蔽`avahi-daemon.service`和`avahi-daemon.socket`以防止和 _systemd-resolved_ 发生冲突。
  * 如果你计划使用mDNS和[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")确保打开UDP端口 `5353`。

**提示：** 可以通过在`/etc/NetworkManager/conf.d/`中创建配置文件并在`[connection]`部分设置`connection.mdns=2`来设置所有[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")连接的默认值。请参阅[NetworkManager.conf(5) § CONNECTION SECTION](<https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTION_SECTION>)和[[3]](<https://bbs.archlinux.org/viewtopic.php?pid=1965078#p1965078>)。

### LLMNR

[Link-Local Multicast Name Resolution](<https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution> "wikipedia:Link-Local Multicast Name Resolution")是由微软创造的主机名解析服务。 

LLMNR将只会在systemd-resolved的全局设置（[resolved.conf(5) § OPTIONS](<https://man.archlinux.org/man/resolved.conf.5#OPTIONS>)中的`LLMNR`）和网络管理器的每个连接的设置都启用时才会活动。默认情况下， _systemd-resolved_ 启用LLMNR响应程序，[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")和[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")[[4]](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/301>)为连接启用它。 

  * 对于[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，选项是`[Network]`部分中的`LLMNR`。请参阅[systemd.network(5) § [NETWORK] SECTION OPTIONS](<https://man.archlinux.org/man/systemd.network.5#%5BNETWORK%5D_SECTION_OPTIONS>)。

  * 对于[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")，选项是`[connection]`部分中的`llmnr`。请参阅[nm-settings(5) § connection setting](<https://man.archlinux.org/man/nm-settings.5#connection_setting>)。

**提示：** 所有[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")连接的默认值可以通过在`/etc/NetworkManager/conf.d/`中创建配置文件并在`[connection]`部分中设置`connection.llmnr`来进行设置。请参阅[NetworkManager.conf(5) § CONNECTION SECTION](<https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTION_SECTION>)。

如果你计划使用LLMNR和[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")，确保打开UDP和TCP端口`5355`。 

##  查找

要解析DNS记录、mDNS或LLMNR主机，你可以使用 _resolvectl_ 组件。 

例如，要解析一个DNS记录： 
    
    $ resolvectl query archlinux.org
    
    archlinux.org: 2a01:4f8:172:1d86::1
                   138.201.81.199
    
    -- Information acquired via protocol DNS in 48.4ms.
    -- Data is authenticated: no
    
##  故障排除

###  systemd-resolved不搜索本地域名

当只给定主机名时，即使`UseDomains=yes`和`Domains=[domain-list]`存在于相应的[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")的 _.network_ 文件中，并且该文件在`resolv.conf`中生成预期的`search [domain-list]`， _systemd-resolved_ 也可能不会搜索本地域名。你可以运行`networkctl status`或`resolvectl status`来检查域名搜索是否真的被选中了。 

可能的解决方法： 

  * 禁用LLMNR以使systemd-resolved立刻继续附加DNS后缀。

  * 修改`/etc/nsswitch.conf`的`hosts`数据库（例如在`resolve`服务后删除`[!UNAVAIL=return]`选项。）

  * 切换到使用完全限定域名（fully-qualified domain names）。

  * 使用`/etc/hosts`来解析主机名。

  * 回退到使用glibc的`dns`以代替systemd的`resolve`。

###  systemd-resolved不解析没有后缀的主机名

为了使systemd-resolved解析不完全限定域名的主机名，请向`/etc/systemd/resolved.conf`中添加`ResolveUnicastSingleLabel=yes`。 

**警告：** 这将把single-label names转发到可能不在你控制之下的全局DNS服务器。这种行为不符合标准，且可能导致隐私和安全风险。请参阅[resolved.conf(5)](<https://man.archlinux.org/man/resolved.conf.5>)来获得详细信息。

这似乎只在禁用LLMNR的情况下工作（`LLMNR=no`）。 

如果你在使用[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，你可能希望DHCP服务器或IPv6路由器提供的域名用作搜索域名，这在默认情况下是禁用的，将它添加到接口的 _.network_ 文件中来启用： 
    
    [Network]
    UseDomains=true

你可以使用以下工具检查每个接口的systemd-resolved结果： 
    
    $ resolvectl domain
    
##  另请参阅

  * [我们通过Francisco Ros在外面发现的systmed-resolved的名称解析问题](<https://moss.sh/name-resolution-issue-systemd-resolved>)
  * 查看[resolvectl(1) § EXAMPLES](<https://man.archlinux.org/man/resolvectl.1#EXAMPLES>)以获取更多示例。
