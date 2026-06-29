[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:OpenVPN](<../zh-cn/Talk:OpenVPN.html>)讨论)

相关文章

  * [OpenVPN in Linux containers](</wzh/index.php?title=OpenVPN_in_Linux_containers&action=edit&redlink=1> "OpenVPN in Linux containers（页面不存在）")

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Still out of date, even after the 2021-12-01 update, e.g. this page still references `rc.conf`（在 [Talk:OpenVPN#](<../zh-cn/Talk:OpenVPN.html>) 中讨论）

本文介绍了 [OpenVPN](<https://openvpn.net>) 的基本的安装与配置过程，适用于个人使用与小型商业使用。要了解更多信息，请访问官方网站 [HOWTO](<https://openvpn.net/index.php/open-source/documentation/howto.html>)、[OpenVPN 2.4 手册页](<https://community.openvpn.net/openvpn/wiki/Openvpn24ManPage>)以及 [Manual](<https://openvpn.net/index.php/open-source/documentation/manuals.html>)。OpenVPN 是一个健壮的、高度灵活的 [VPN](<https://en.wikipedia.org/wiki/VPN> "wikipedia:VPN") 守护进程。它支持 [SSL/TLS](<https://en.wikipedia.org/wiki/SSL/TLS> "wikipedia:SSL/TLS") 安全、[以太网桥接](<https://en.wikipedia.org/wiki/Bridging_\(networking\)> "wikipedia:Bridging \(networking\)")、经由[代理](<https://en.wikipedia.org/wiki/Proxy_server> "wikipedia:Proxy server")的 [TCP](<https://en.wikipedia.org/wiki/Transmission_Control_Protocol> "wikipedia:Transmission Control Protocol") 或 [UDP](<https://en.wikipedia.org/wiki/User_Datagram_Protocol> "wikipedia:User Datagram Protocol") [隧道](<https://en.wikipedia.org/wiki/Tunneling_protocol> "wikipedia:Tunneling protocol")和 [NAT](<https://en.wikipedia.org/wiki/Network_address_translation> "wikipedia:Network address translation")。另外，它也支持动态 IP 地址以及 [DHCP](<https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol> "wikipedia:Dynamic Host Configuration Protocol")，可伸缩性足以支持数百或数千用户的使用场景，同时可移植至大多数主流操作系统平台上。 

OpenVPN 与 [OpenSSL](<https://www.openssl.org>) 库紧密相关，并由此获得许多加密功能。它除了支持使用[预共享密钥](<https://en.wikipedia.org/wiki/Pre-shared_key> "wikipedia:Pre-shared key")（静态密钥模式）或使用非对称加密的[公钥](<https://en.wikipedia.org/wiki/Public_key> "wikipedia:Public key")（[SSL/TLS](<https://en.wikipedia.org/wiki/SSL/TLS> "wikipedia:SSL/TLS") 模式）这两种传统加密方式之外。还支持不加密的 TCP/UDP 隧道。 

OpenVPN 配合大多数平台上都有的 [TUN/TAP](<https://en.wikipedia.org/wiki/TUN/TAP> "wikipedia:TUN/TAP") 虚拟网络接口一起使用。总体而言，它旨在提供 [IPSec](<https://en.wikipedia.org/wiki/IpSec> "wikipedia:IpSec") 的许多关键功能，但占用空间相对较小。OpenVPN 由 James Yonan 编写，并在 [GNU 通用公共许可证 (GPL)](<https://en.wikipedia.org/wiki/GNU_General_Public_License> "wikipedia:GNU General Public License") 下发布。 

##  安装

[安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)") [openvpn](<https://archlinux.org/packages/?name=openvpn>)包，它同时支持服务器和客户端模式。 

可用的前端： 

  * **NetworkManager OpenVPN** — OpenVPN 的 NetworkManager VPN 插件。

     <https://wiki.gnome.org/Projects/NetworkManager/VPN> || [networkmanager-openvpn](<https://archlinux.org/packages/?name=networkmanager-openvpn>)包

  * **QOpenVPN** — 用 PyQt 为基于 systemd 的发行版编写的简单 OpenVPN GUI。

     <https://github.com/xmikos/qopenvpn> || [qopenvpn](<https://archlinux.org/packages/?name=qopenvpn>)包

  * **eOVPN** — 用于连接、管理和更新 OpenVPN 配置的应用程序。

     <https://github.com/jkotra/eOVPN> || [eovpn](<https://aur.archlinux.org/packages/eovpn/>)AUR

##  内核配置

OpenVPN 需要 TUN/TAP 的支持，默认内核已经进行了正确的配置。自定义的内核需要启用 `tun` 模块。 
    
    Kernel config file
    
     Device Drivers
      --> Network device support
        [M] Universal TUN/TAP device driver support

详情参阅 [Kernel modules](<../zh-cn/Kernel_modules.html> "Kernel modules")

##  连接到第三方提供的 VPN

要连接到第三方提供的 VPN 服务，可以忽略以下大部分内容，尤其是在服务器设置方面。 从 [#客户端配置文件](<#%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)开始，然后跳到 [#启动 OpenVPN](<#%E5%90%AF%E5%8A%A8_OpenVPN>)。 应使用提供商证书和说明，请参阅 [Category:VPN providers](</wzh/index.php?title=Category:VPN_providers&action=edit&redlink=1> "Category:VPN providers（页面不存在）") 以获取可适用于其他提供商的示例。 [Linux Containers 中的 OpenVPN 客户端](</wzh/index.php?title=OpenVPN_client_in_Linux_Containers&action=edit&redlink=1> "OpenVPN client in Linux Containers（页面不存在）")也有一般适用的说明，同时它更进一步，将 OpenVPN 客户端进程隔离到容器中。 

**注意：** 大多数免费的 VPN 提供商会（通常只）提供 [PPTP](<../zh-cn/PPTP_server.html> "PPTP server"), 它更容易设置和配置，但 [不安全](<http://poptop.sourceforge.net/dox/protocol-security.phtml>)。

##  从头开始创建公钥基础设施 (PKI)

在设置 OpenVPN 服务器时，用户需要创建一个[公开密钥基础建设 (PKI)](<https://en.wikipedia.org/wiki/Public_Key_Infrastructure> "wikipedia:Public Key Infrastructure")，这在 [Easy-RSA](</wzh/index.php?title=Easy-RSA&action=edit&redlink=1> "Easy-RSA（页面不存在）") 文章中有详细说明。 按照单独文章中的步骤创建所需的证书、私钥和相关文件后，此时 `/etc/openvpn/server` 中应该有 5 个文件： 
    
    ca.crt
    dh.pem
    servername.crt
    servername.key
    ta.key
    
或者，从 OpenVPN 2.4 开始，可以使用 Easy-RSA 使用椭圆曲线生成证书和密钥。 有关详细信息，请参阅 OpenVPN 文档。 

##  一个基本的三层 IP 路由配置

**注意：** 除非另有明确说明，本文的其余部分均假设基本的第 3 层 IP 路由配置。

OpenVPN 是一个非常通用的软件，可以进行多种配置，实际上机器既可以是服务器，也可以是客户端。 

随着 v2.4 的发布，服务器配置存储在 `/etc/openvpn/server` 中，客户端配置存储在 `/etc/openvpn/client` 中，每种模式都有自己的systemd 单元，即 `openvpn-client@.service` 和 `openvpn-server@.service`。 

###  示例配置

OpenVPN 软件包附带了一系列用于不同目的的示例配置文件。示例服务器和客户端配置文件是基本 OpenVPN 设置的理想起点，具有以下功能： 

  * 使用 [Public Key Infrastructure (PKI)](<https://en.wikipedia.org/wiki/Public_key_infrastructure> "wikipedia:Public key infrastructure") 进行身份验证。
  * 使用虚拟 TUN 网络接口（OSI 第 3 层 IP 路由）创建 VPN。
  * 监听 UDP 端口 1194 上的客户端连接（OpenVPN 的官方 IANA 端口号[[1]](<https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=openvpn>) ）。
  * 将虚拟地址分配给来自 10.8.0.0/24 子网的连接客户端。

有关更高级的配置，请参阅 [openvpn(8)](<https://man.archlinux.org/man/openvpn.8>) 手册页和 [OpenVPN 文档](<https://openvpn.net/index.php/open-source/documentation>)。 

###  服务器配置文件

**注意：** 请注意，如果服务器位于防火墙或 NAT 转换路由器后面，则必须将 OpenVPN 端口转发到服务器。

将示例服务器配置文件 `/usr/share/openvpn/examples/server.conf` 复制到 `/etc/openvpn/server/server.conf`。 

编辑文件，至少进行以下更改： 
    
    /etc/openvpn/server/server.conf
    
    ca ca.crt
    cert servername.crt
    key servername.key
    dh dh.pem
    
    tls-crypt ta.key # Replaces _tls-auth ta.key 0_
    
    user nobody
    group nobody
    
如果使用带有椭圆曲线的 TLS，请指定 `dh none` 和 `ecdh-curve secp521r1`。使用椭圆曲线时不使用 DH 参数文件。从 OpenVPN 2.4.8 开始，需要在服务器配置中指定椭圆曲线的类型。否则服务器将无法识别曲线类型并可能使用不兼容的曲线类型，从而导致身份验证错误。 

####  强化服务器

如果优先考虑安全性，则建议进行其他配置，包括：限制服务器使用强密码/身份验证方法和（可选）将启用的 TLS 密码集限制为较新的密码。从 OpenVPN 2.4 开始，服务器和客户端将在 TLS 模式下自动协商 **AES-256-GCM** 。 

将以下内容添加到 `/etc/openvpn/server/server.conf`： 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 使用说明属于维基文本，不属于代码块。避免诸如“边缘安全性”之类的主观术语。（在[Talk:OpenVPN](<../zh-cn/Talk:OpenVPN.html>)讨论）

最安全 
    
    /etc/openvpn/server/server.conf
    
    cipher AES-256-GCM
    auth SHA512
    tls-version-min 1.3
    #Uncomment  tls-cipher to limit possible negotiation options to the strongest ciphers, doing so it's no longer possible to generate certs with current easyrsa, [more information](<https://wiki.openssl.org/index.php/TLS1.3>)
    #tls-cipher TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
    
[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 兼容性选项不适合强化部分。（在[Talk:OpenVPN](<../zh-cn/Talk:OpenVPN.html>)讨论）

与大多数设备的兼容性 
    
    /etc/openvpn/server/server.conf
    
    cipher AES-256-GCM
    auth SHA512
    tls-version-min 1.2
    tls-cipher TLS-DHE-RSA-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-128-GCM-SHA256:TLS-DHE-RSA-WITH-AES-256-CBC-SHA:TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA:TLS-DHE-RSA-WITH-AES-128-CBC-SHA:TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA
    
**注意：**

  * .ovpn 客户端配置文件“必须”包含匹配的密码和身份验证行才能正常工作（至少对于 iOS 和 Android 客户端）。
  * 错误地使用 `tls-cipher` 可能会导致调试连接困难，并且可能没有必要。有关更多信息，请参阅 [OpenVPN 的社区维基](<https://community.openvpn.net/openvpn/wiki/Hardening#Useof--tls-cipher>)。

####  启用压缩

上游不建议启用压缩；这样做会向服务器打开所谓的 VORACLE 攻击向量。请参阅[这篇](<https://community.openvpn.net/openvpn/wiki/VORACLE>)文章。 

####  非标准端口和/或协议

一般建议使用 OpenVPN over UDP，因为 [TCP over TCP 不是一个好主意](<http://sites.inka.de/bigred/devel/tcp-tcp.html>)[[2]](<https://adsabs.harvard.edu/abs/2005SPIE.6011..138H>)。 

某些网络可能不允许默认端口和/或协议上的 OpenVPN 连接。规避这一点的一种策略是模拟 HTTPS 流量，这很可能是畅通无阻的。 

为此，请将 `/etc/openvpn/server/server.conf` 配置为： 
    
    /etc/openvpn/server/server.conf
    
    port 443
    proto tcp
    
**注意：**.ovpn 客户端配置文件 **必须** 包含匹配的端口和原型线才能正常工作！

####  在物理机的不同端口上运行多个 OpenVPN 实例

可以在同一台机器上运行多个并发的 OpenVPN 实例。每个服务器都需要在 `/etc/openvpn/server/` 中定义为单独的 .conf 文件。至少，并行服务器需要在不同的端口上运行。一个简单的设置将流量连接到一个单独的 IP 池。更高级的设置超出了本指南的范围。 

考虑这个例子，运行 2 个并发服务器，一个端口 443/udp，另一个端口 80/tcp。 

首先修改创建的 `/etc/openvpn/server/server.conf` 如下： 
    
    /etc/openvpn/server/server.conf
    
    port 443
    proto udp
    server 10.8.0.0 255.255.255.0
    
现在复制它并修改副本以在 80/tcp 上运行： 
    
    /etc/openvpn/server/server2.conf
    
    port 80
    proto tcp
    server 10.8.1.0 255.255.255.0
    
请务必在防火墙中设置相应的条目，请参阅[#防火墙配置](<#%E9%98%B2%E7%81%AB%E5%A2%99%E9%85%8D%E7%BD%AE>)中的相关部分。 

###  客户端配置文件

将示例客户端配置文件 `/usr/share/openvpn/examples/client.conf` 复制到 `/etc/openvpn/client/`。 

编辑以下内容： 

  * `remote` 指令反映服务器的 [Fully Qualified Domain Name](<https://en.wikipedia.org/wiki/Fully_qualified_domain_name> "wikipedia:Fully qualified domain name")、主机名（客户端已知）或其 IP 地址。
  * 取消注释 `user` 和 `group` 指令以删除权限。
  * `ca`、`cert` 和 `key` 参数反映密钥和证书的路径和名称。
  * 启用 TLS HMAC 握手保护（`--tls-crypt` 或 `--tls-auth`）。

    /etc/openvpn/client/client.conf
    
    client
    remote elmer.acmecorp.org 1194
    
    user nobody
    group nobody
    ca ca.crt
    cert client.crt
    key client.key
    
    tls-crypt ta.key # Replaces _tls-auth ta.key 1_
    
####  以非特权用户身份运行

在配置文件中使用选项 `user nobody` 和 `group nobody` 会使 _OpenVPN_ 在建立连接后放弃其 `root` 权限。缺点是在 VPN 断开连接后，守护进程无法再次删除其设置的网络路由。如果想要在没有 VPN 连接的情况下限制传输流量，那么延迟路由可能被认为是有益的。但是，也可能发生 OpenVPN 服务器在隧道运行时向路由推送更新的情况。具有删除权限的客户端将无法执行更新并退出并出现错误。 

由于似乎需要手动操作来管理路由，因此选项 `user nobody` 和 `group nobody` 可能看起来不受欢迎。然而，根据设置，有不同的方法来处理这些情况： 

  * 对于单元的错误，一个简单的方法是[edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit")它并在`[Service]`部分添加一个`Restart=on-failure`。但是，仅此一项不会删除任何过时的路由，因此可能会发生重新启动的隧道未正确路由的情况。
  * 包中包含`/usr/lib/openvpn/plugins/openvpn-plugin-down-root.so`，可以用来让 _openvpn_ fork一个只有root权限的进程从主进程接收到关闭信号时执行自定义脚本的任务，该进程正在处理具有删除权限的隧道（另请参阅其 [README](<https://community.openvpn.net/openvpn/browser/plugin/down-root/README?rev=d02a86d37bed69ee3fb63d08913623a86c88da15>)）。

下面链接的 OpenVPN HowTo 更进一步，创建了一个专用的非特权用户/组，而不是现有的 `nobody`。这样做的好处是避免了在守护进程之间共享用户时的潜在风险： 

  * [OpenVPN HowTo](<https://openvpn.net/index.php/open-source/documentation/howto.html#security>) 解释了如何创建非特权用户模式和包装脚本以自动恢复路由的另一种方法。
  * 可以让 OpenVPN 首先以非特权用户身份启动，而无需以 root 身份运行，请参阅[这个 OpenVPN wiki](<https://community.openvpn.net/openvpn/wiki/UnprivilegedUser>)（howto）。 howto 假设存在 System V init，而不是 [Systemd](<../zh-cn/Systemd.html> "Systemd") 并且不包括 `--up`/`--down` 脚本的处理 - 那些应该被处理与 _ip_ 命令相同的方式，额外注意访问权限。
  * 也可以从无特权的 podman 容器中运行 OpenVPN，请参阅[这部分 OpenVPN HowTo](<https://community.openvpn.net/openvpn/wiki/UnprivilegedUser#RunOpenVPNwithinunprivilegedpodmancontainer>)

**提示：**[#openvpn-unroot](<#openvpn-unroot>) 描述了一种自动化上述设置的工具。

###  将证书转换为加密的 .p12 格式

某些软件只会读取存储在密码加密的 .p12 文件中的 VPN 证书。这些可以使用以下命令生成： 
    
    # openssl pkcs12 -export -inkey keys/bugs.key -in keys/bugs.crt -certfile keys/ca.crt -out keys/bugs.p12

###  测试 OpenVPN 配置

在服务器上（以 root 用户）运行 `openvpn /etc/openvpn/server/server.conf`，在客户端（以 root 用户）运行 `openvpn /etc/openvpn/client/client.conf`。示例输出应类似于以下内容： 
    
    # openvpn /etc/openvpn/server/server.conf
    
    Wed Dec 28 14:41:26 2011 OpenVPN 2.2.1 x86_64-unknown-linux-gnu [SSL] [LZO2] [EPOLL] [eurephia] built on Aug 13 2011
    Wed Dec 28 14:41:26 2011 NOTE: OpenVPN 2.1 requires '--script-security 2' or higher to call user-defined scripts or executables
    Wed Dec 28 14:41:26 2011 Diffie-Hellman initialized with 2048 bit key
    ...
    Wed Dec 28 14:41:54 2011 bugs/95.126.136.73:48904 MULTI: primary virtual IP for bugs/95.126.136.73:48904: 10.8.0.6
    Wed Dec 28 14:41:57 2011 bugs/95.126.136.73:48904 PUSH: Received control message: 'PUSH_REQUEST'
    Wed Dec 28 14:41:57 2011 bugs/95.126.136.73:48904 SENT CONTROL [bugs]: 'PUSH_REPLY,route 10.8.0.1,topology net30,ping 10,ping-restart 120,ifconfig 10.8.0.6 10.8.0.5' (status=1)
    
    # openvpn /etc/openvpn/client/client.conf
    
    Wed Dec 28 14:41:50 2011 OpenVPN 2.2.1 i686-pc-linux-gnu [SSL] [LZO2] [EPOLL] [eurephia] built on Aug 13 2011
    Wed Dec 28 14:41:50 2011 NOTE: OpenVPN 2.1 requires '--script-security 2' or higher to call user-defined scripts or executables
    ...
    Wed Dec 28 14:41:57 2011 GID set to nobody
    Wed Dec 28 14:41:57 2011 UID set to nobody
    Wed Dec 28 14:41:57 2011 Initialization Sequence Completed

[查找IP地址](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#IP_%E5%9C%B0%E5%9D%80> "网络配置")分配给服务器上的tunX接口，从客户端[ping](</wzh/index.php?title=Ping&action=edit&redlink=1> "Ping（页面不存在）")。 

[查找IP地址](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#IP_%E5%9C%B0%E5%9D%80> "网络配置")分配给客户端的tunX接口，从服务器[ping](</wzh/index.php?title=Ping&action=edit&redlink=1> "Ping（页面不存在）")。 

**注意：** 如果使用防火墙，请确保 TUN 设备上的 IP 数据包没有被阻止。

###  使用 Fragment 和 MSS 配置 MTU

如果在通过 OpenVPN 使用（远程）服务时遇到问题（例如网页浏览、[DNS](</wzh/index.php?title=DNS&action=edit&redlink=1> "DNS（页面不存在）")、[NFS](<../zh-cn/NFS.html> "NFS")），则可能需要手动设置 MTU 值。 

以下消息可能指示应调整 MTU 值： 
    
    read UDPv4 [EMSGSIZE Path-MTU=1407]: Message too long (code=90)
    
为了获得最大段大小 (MSS)，客户端需要沿着到服务器的路径发现最小的 MTU。为了做到这一点 ping 服务器并禁用碎片，然后指定最大数据包大小 [[3]](<https://www.sonassi.com/help/troubleshooting/setting-correct-mtu-for-openvpn>)： 
    
    # ping -M do -s 1500 -c 1 example.com
    
每次将 1500 值减 10，直到 ping 成功。 

**注意：** 不支持“片段”指令的客户端（例如 OpenELEC，[应用程序](<https://docs.openvpn.net/connecting/connecting-to-access-server-with-apple-ios/faq-regarding-openvpn-connect-ios/>)) 无法连接到使用 `fragment` 指令的服务器。请参阅 `mtu-test` 作为替代解决方案。

更新客户端配置以使用成功的 MTU 值，例如： 
    
    /etc/openvpn/client/client.conf
    
    remote example.com 1194
    
    tun-mtu 1400 
    mssfix 1360
    
可能会指示 OpenVPN 每次在客户端连接时测试 MTU。请耐心等待，因为客户端可能不会通知正在运行的测试，并且连接在完成之前可能会显示为无效。以下将增加大约 3 分钟的 OpenVPN 启动时间。建议配置片段大小，除非客户端将通过许多不同的网络进行连接并且瓶颈不在服务器端： 
    
    /etc/openvpn/client/client.conf
    
    remote example.com 1194
    
    mtu-test
    
### IPv6

####  通过 IPv6 连接到服务器

从 OpenVPN 2.4 开始，当仅使用 `proto udp` 或 `proto tcp` 时，OpenVPN 将使用操作系统定义的 `AF_INET`，在大多数情况下，这将仅是 IPv4。要同时使用 IPv4 和 IPv6，请使用 `proto udp6` 或 `proto tcp6`。要仅强制执行 IPv4，请使用 `proto udp4` 或 `proto tcp4`。在较旧的 OpenVPN 版本上，一个服务器实例只能支持 IPv4 或 IPv6。 

####  在隧道内提供 IPv6

为了在隧道内提供 IPv6，请将 IPv6 前缀路由到 OpenVPN 服务器。要么在网关上设置静态路由（如果分配了静态块），要么使用 DHCPv6 客户端通过 DHCPv6 前缀委派获取前缀（详情请参阅[IPv6 Prefix delegation](<../zh-cn/IPv6.html#Prefix_delegation_\(DHCPv6-PD\)> "IPv6")）。还可以考虑使用来自地址块 fc00::/7 的唯一本地地址。这两种方法各有优缺点： 

  * 许多 ISP 仅提供动态更改的 IPv6 前缀。 OpenVPN 不支持前缀更改，因此每次更改前缀时都要更改 server.conf（也许可以通过脚本自动实现）。
  * ULA 地址不会路由到 Internet，并且设置 NAT 不像使用 IPv4 那样简单。这意味着不能通过隧道路由整个流量。那些希望通过 IPv6 连接两个站点而不需要通过隧道连接到 Internet 的人可能希望使用 ULA 地址来轻松。

或者，NDP 代理应该可以工作。请参阅[这个 StackExchange 帖子](<https://unix.stackexchange.com/questions/136211/routing-public-ipv6-traffic-through-openvpn-tunnel>)。 

收到前缀（建议使用 /64）后，将以下内容附加到 server.conf： 
    
    server-ipv6 2001:db8:0:123::/64
    
这是相当于 OpenVPN 的默认 10.8.0.0/24 网络的 IPv6，需要从 DHCPv6 客户端获取。或者使用例如 fd00:1234::/64。 

那些想要将路由推送到家庭网络（192.168.1.0/24 等效）的人，还需要附加： 
    
    push "route-ipv6 2001:db8:0:abc::/64"
    
OpenVPN 尚不包括 DHCPv6，因此没有方法例如通过 IPv6 推送 DNS 服务器。这需要通过 IPv4 来完成。 [OpenVPN Wiki](<https://community.openvpn.net/openvpn/wiki/IPv6>) 提供了一些其他配置选项。 

##  启动 OpenVPN

###  手动启动

###  systemd 服务配置

###  让 NetworkManager 开始连接

###  NetworkManager-native VPN 配置

####  图形界面配置

####  CLI 配置

####  与连接同步状态

####  故障排除

######  没有证书密码

##  通过服务器路由客户端流量

###  防火墙配置

####  防火墙

#### ufw

#### iptables

###  如果 VPN 出现故障，防止泄漏

#### ufw

#### vpnfailsafe

##  第 3 层 IPv4 路由

###  路由 LAN 的先决条件

####  路由表

###  将服务器 LAN 连接到客户端

###  将客户端 LAN 连接到服务器

###  连接客户端和服务器 LANs

###  连接客户端和客户端局域网

##  域名解析

###  pull-resolv-conf 自定义脚本

###  update-resolv-conf 自定义脚本

###  update-systemd-resolved 自定义脚本

###  使用 NetworkManager 覆盖 DNS 服务器

##  第 2 层以太网桥接

##  配置生成器

### ovpngen

### openvpn-unroot

##  故障排除

###  客户端守护进程在挂起后没有重新连接

###  一段时间不活动后连接断开

###  PID 文件不存在

###  路由配置失败， systemd-networkd

###  tls-crypt 解包错误：数据包太短

##  另见

##  准备证书和密钥数据

现在要创建所需的证书和密钥，可以在任何机器上完成，即使没有联网也可以进行。 设置证书和密钥生成脚本的默认值。编辑 `/etc/openvpn/easy-rsa/vars`，设置 KEY_COUNTRY, KEY_PROVINCE, KEY_CITY, KEY_ORG 和 KEY_EMAIL 参数(不要留空任何参数)，然后导出环境变量。 
    
    # source ./vars
    
清理之前的密钥： 
    
    # ./clean-all
    
build-ca 脚本创建了 certificate authority (CA) ca.key，密钥认证机器需要这个密钥。服务器和客户端需要 ca.crt 证书。 
    
    # ./build-ca
    
`build-key-server` 为服务器创建一个证书和密钥对。使用中不要输入简单的密码或公司名。 
    
    # ./build-key-server <server-name>
    
`build-dh` 脚本创建服务器需要的 Diffie-Hellman pem 文件。 
    
    # ./build-dh
    
`build-key` 脚本创建客户端证书和密钥对。可以生成任意多个以给不同的客户端使用。只要保证客户端名 <client> 是唯一的。如果要用密码认证客户端，请使用 `build-key-pass` 脚本。 
    
    # ./build-key <client1>
    # ./build-key <client2>
    
生成的文件都保存在 `/etc/openvpn/easy-rsa/keys`。如果有错误，可以通过运行 `clean-all` 脚本，然后从头开始。注意这将删除之前生成的证书和密钥。 
    
    # ./clean-all
    
最后一步是将所有需要的文件通过安全通道放到正确的机器上。`ca.crt` 需要放到所有服务器和客户端。`server.crt`, `server.key` 和 `dh{n}.pem` 文件放到服务器， `client.crt` 和 `client.key` 文件放到客户端。 

##  配置服务器

###  复制默认服务器配置文件
    
    # cp /usr/share/openvpn/examples/server.conf /etc/openvpn/openvpn.conf
    
###  使用 PAM 和密码认证
    
    port 1194
    proto udp
    dev tap
    ca /etc/openvpn/easy-rsa/keys/ca.crt
    cert /etc/openvpn/easy-rsa/keys/<MYSERVER>.crt
    key /etc/openvpn/easy-rsa/keys/<MYSERVER>.key
    dh /etc/openvpn/easy-rsa/keys/dh1024.pem
    server 192.168.56.0 255.255.255.0
    ifconfig-pool-persist ipp.txt
    ;learn-address ./script
    client-to-client
    ;duplicate-cn
    keepalive 10 120
    ;tls-auth ta.key 0
    comp-lzo
    ;max-clients 100
    ;user nobody
    ;group nobody
    persist-key
    persist-tun
    status /var/log/openvpn-status.log
    verb 3
    client-cert-not-required
    username-as-common-name
    plugin /usr/lib/openvpn/openvpn-auth-pam.so login
    
###  使用证书认证
    
    port 1194
    proto tcp
    dev tun0
    
    ca /etc/openvpn/easy-rsa/keys/ca.crt
    cert /etc/openvpn/easy-rsa/keys/<MYSERVER>.crt
    key /etc/openvpn/easy-rsa/keys/<MYSERVER>.key
    dh /etc/openvpn/easy-rsa/keys/dh1024.pem
    
    server 10.8.0.0 255.255.255.0
    ifconfig-pool-persist ipp.txt
    keepalive 10 120
    comp-lzo
    user nobody
    group nobody
    persist-key
    persist-tun
    status /var/log/openvpn-status.log
    verb 3
    
    log-append /var/log/openvpn
    status /tmp/vpn.status 10
    
###  通过服务器路由

将下面内容写入服务器的 `openvpn.conf` 配置文件，"192.168.1.1" 修改为外部 DNS IP 地址。 
    
    push "dhcp-option DNS 192.168.1.1"
    push "redirect-gateway def1"
    
使用 iptable 进行 NAT 转发： 
    
    echo 1 > /proc/sys/net/ipv4/ip_forward
    iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
    
如果运行在 OpenVZ VPS 环境，参见 [[4]](<https://web.archive.org/web/20120625100339/http://thecodeninja.net/linux/openvpn-archlinux-openvz-vps/>): 
    
    iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o venet0 -j SNAT --to (venet0 ip)
    
如果一切正常，保存修改，编辑 `/etc/conf.d/iptables` 设置 IPTABLES_FORWARD=1 
    
    /etc/rc.d/iptables save
    
##  客户端配置

配置客户端的 .conf 文件 

###  使用密码认证
    
    client
    dev tap
    proto udp
    remote <address> 1194
    resolv-retry infinite
    nobind
    persist-tun
    comp-lzo
    verb 3
    auth-user-pass passwd
    ca ca.crt
    
被 `auth-user-pass` 引用的 `passwd` 文件必须包含如下两行: 

  * 第一行 - username
  * 第二行 - password

###  证书验证
    
    client
    remote <MYSERVER> 1194
    dev tun0
    proto tcp
    resolv-retry infinite
    nobind
    persist-key
    persist-tun
    verb 2
    ca ca.crt
    cert client1.crt
    key client1.key
    comp-lzo
    
将`ca.crt`, `client1.crt` 和 `client1.key`复制到远程计算机： 

安装隧道模块: 
    
     # sudo modprobe tun
    
要让 **tun** 模块自动启动，请将其加入 `/etc/rc.conf` 的 Modules 行。 

### DNS

系统使用的 DNS 服务器定义在`/etc/resolv.conf`。通常此文件由控制系统网络的模块(Wicd, NetworkManager 等)维护。然而，如果希望通过远程服务器解析地址，OpenVPN 需要修改这个文件。 

安装 **openresolv** 软件包，它可以实现多个程序互不影响的修改 `resolv.conf`。安装后通过重启网络连接，保证 resolv.conf 是由 "resolvconf" 创建而且 DNS 解析工作正常。openresolv 不需要配置，它会自动检测和使用网络系统。 

然后将如下脚本保存到`/usr/share/openvpn/update-resolv-conf`: 
    
    #!/bin/bash
    #
    # Parses DHCP options from openvpn to update resolv.conf
    # To use set as 'up' and 'down' script in your openvpn *.conf:
    # up /etc/openvpn/update-resolv-conf
    # down /etc/openvpn/update-resolv-conf
    #
    # Used snippets of resolvconf script by Thomas Hood <jdthood@yahoo.co.uk>
    # and Chris Hanson
    # Licensed under the GNU GPL.  See /usr/share/common-licenses/GPL.
    #
    # 05/2006 chlauber@bnc.ch
    #
    # Example envs set from openvpn:
    # foreign_option_1='dhcp-option DNS 193.43.27.132'
    # foreign_option_2='dhcp-option DNS 193.43.27.133'
    # foreign_option_3='dhcp-option DOMAIN be.bnc.ch'
    
    [ -x /usr/sbin/resolvconf ] || exit 0
    
    case $script_type in
    
    up)
       for optionname in ${!foreign_option_*} ; do
          option="${!optionname}"
          echo $option
          part1=$(echo "$option" | cut -d " " -f 1)
          if [ "$part1" == "dhcp-option" ] ; then
             part2=$(echo "$option" | cut -d " " -f 2)
             part3=$(echo "$option" | cut -d " " -f 3)
             if [ "$part2" == "DNS" ] ; then
                IF_DNS_NAMESERVERS="$IF_DNS_NAMESERVERS $part3"
             fi
             if [ "$part2" == "DOMAIN" ] ; then
                IF_DNS_SEARCH="$part3"
             fi
          fi
       done
       R=""
       if [ "$IF_DNS_SEARCH" ] ; then
               R="${R}search $IF_DNS_SEARCH
    "
       fi
       for NS in $IF_DNS_NAMESERVERS ; do
               R="${R}nameserver $NS
    "
       done
       echo -n "$R" | /usr/sbin/resolvconf -a "${dev}.inet"
       ;;
    down)
       /usr/sbin/resolvconf -d "${dev}.inet"
       ;;
    esac
    
设置脚本可执行属性： 
    
    $ chmod +x /usr/share/openvpn/update-resolv-conf
    
然后将下面内容加入 OpenVPN 客户端的配置文件： 
    
    script-security 2
    up /usr/share/openvpn/update-resolv-conf
    down /usr/share/openvpn/update-resolv-conf
    
现在再启动 OpenVPN 连接，就能发现 `resolv.conf` 文件已经更新，关闭连接后恢复正常。 

##  启动 OpenVPN

###  手动启动

如需对 VPN 连接进行调试，可以以 root 身份手动运行 `openvpn /etc/openvpn/client.conf` 以启动客户端守护程序。服务器端同样可以如此启动，只需替换为服务器端的配置文件（例，`openvpn /etc/openvpn/server.conf`）。 

###  systemd 服务配置

若需在系统启动时自动启动 OpenVPN，对服务器端与客户端，都可以采用在对应机器上[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `openvpn@_< configuration>_.service` 的方式配置。 

例如，如果客户端配置文件是 `/etc/openvpn/client.conf`，则服务名称应为 `openvpn@client.service`。或者，如果服务器端配置文件是 `/etc/openvpn/server.conf`，则服务名称应为 `openvpn@server.service`。 

###  让 NetworkManager 启动连接

在客户端，您可能并不需要一直运行 VPN 隧道，或者您仅仅想要为特定的 NetworkManager 连接建立隧道。要实现这一点，您可以向 `/etc/NetworkManager/dispatcher.d/` 添加脚本。在下列示例中，"Provider" 是 NetworkManager 连接的名称： 
    
    /etc/NetworkManager/dispatcher.d/10-openvpn
    
    #!/bin/sh
    case "$2" in
      up)
        if [ "$CONNECTION_ID" = "Provider" ]; then
          systemctl start openvpn@client
        fi
      ;;
      down)
        systemctl stop openvpn@client
      ;;
    esac

请查看 [NetworkManager#Network services with NetworkManager dispatcher](<../zh-cn/NetworkManager.html#Network_services_with_NetworkManager_dispatcher> "NetworkManager") 以了解详情。 

###  Gnome 配置

如果您想要经由 Gnome 内置的网络配置来连接到一个 OpenVPN 服务器，请按照如下步骤进行配置： 首先，安装 `networkmanager-openvpn`。 然后，在设置菜单选中网络设置，在VPN点击+新建连接。从这里你可以选择OpenVPN并手动输入设置，或者您也可以选择导入[配置文件](<#%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%85%8D%E7%BD%AE>)，如果您已经有一个的话。如果您按照上述说明，配置文件会在`/etc/openvpn/client.conf`。打开开关就可以连接VPN。 

##  参见

  * [OpenVPN 官方站点](<https://openvpn.net/index.php/open-source.html>)
