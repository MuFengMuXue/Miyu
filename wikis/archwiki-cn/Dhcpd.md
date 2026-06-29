**翻译状态：**

  * 本文（或部分内容）译自 [dhcpd](<https://wiki.archlinux.org/title/dhcpd> "arch:dhcpd")，最近一次同步于 2023-01-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/dhcpd?diff=0&oldid=761344>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/dhcpd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd")

dhcpd 是老版本的 [**互联网系统协会 (ISC)**](<https://www.isc.org/dhcp>) DHCP 服务器。它可在局域网中管理路由。需要注意，ISC 推荐以 [Kea](<https://www.isc.org/kea/>) 作为替代。 

**注意：** _dhcpd_ (DHCP **(服务器)** 守护进程) 不是 [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") (DHCP **客户端** 守护进程).

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dhcp](<https://archlinux.org/packages/?name=dhcp>)包 包。 

##  使用

_dhcpd_ 包括两个单元文件：`dhcpd4.service` 和 `dhcpd6.service`，可用于[控制](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")守护进程。它们分别在 IPv4 和 IPv6 的 _所有_ [网络接口](</wzh/index.php?title=Network_interfaces&action=edit&redlink=1> "Network interfaces（页面不存在）")上启动守护进程。可查看 [#只侦听单一网口](<#%E5%8F%AA%E4%BE%A6%E5%90%AC%E5%8D%95%E4%B8%80%E7%BD%91%E5%8F%A3>)了解单一网口配置。 

##  配置

为你想使用的接口分配静态 IPv4 地址（在实例中我们将使用 `eth0`）。指定的子网不应与其他接口的子网重叠。 
    
    # ip link set up dev eth0
    # ip addr add 139.96.30.100/24 dev eth0 # arbitrary address
    
**提示：** 通常有三个预留的网段用于私有网络，它们不会与任何互联网中的主机发生冲突： 

  * `192.168/16` (subnet `192.168.0.0`, netmask `255.255.0.0`)
  * `172.16/12` (subnet `172.16.0.0`, netmask `255.240.0.0`)
  * `10/8` (for large networks; subnet `10.0.0.0`, netmask `255.0.0.0`)

另请参阅 [RFC 1918](<https://tools.ietf.org/html/rfc1918> "rfc:1918")。

要在启动时分配静态 IP 地址，查看[网络配置#静态 IP 地址](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E9%9D%99%E6%80%81_IP_%E5%9C%B0%E5%9D%80> "网络配置")。 

默认的 `dhcpd.conf` 文件包含许多注释的例子，复制一份该文件： 
    
    # mv /etc/dhcpd.conf /etc/dhcpd.conf.example
    
欲仅监听子网 `139.96.30.0/24`，您可以创建以下最精简的配置文件： 
    
    /etc/dhcpd.conf
    
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    option subnet-mask 255.255.255.0;
    option routers 139.96.30.100;
    subnet 139.96.30.0 netmask 255.255.255.0 {
      range 139.96.30.150 139.96.30.250;
    }
    
注意： 

  * 如果 `eth0` 是子网 `139.96.30.0/24`的仅有接口（往往如此），那么 `dhcpd` 只监听 `eth0`

  * 如果您想 `dhcpd` 监听其他接口，通过指定使用其他接口的子网修改配置文件以监听。

如果你要为一台特定的设备提供一个固定的 IP 地址，你可以定义主机块： 
    
    /etc/dhcpd.conf
    
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    option subnet-mask 255.255.255.0;
    option routers 139.96.30.100;
    subnet 139.96.30.0 netmask 255.255.255.0 {
      range 139.96.30.150 139.96.30.250;
    }
    host macbookpro{
      hardware ethernet 70:56:81:22:33:44;
      fixed-address 139.96.30.199;
    }
    
`domain-name-servers` 选项包含提供给客户的 DNS 服务器地址，这个例子中使用了谷歌的公共 DNS 服务器。如果你知道一个本地的DNS服务器（例如，由你的服务商提供的），那么你应该使用这个 DNS。如果 DNS 服务器部署在本地设备上，应该使用子网络中的地址（如 `139.96.30.100`）。 

`subnet-mask` 和 `routers` 定义子网掩码和子网上可用路由器的列表。在大多数情况下，对于小型网络，您可以使用 `255.255.255.0` 作为掩码，并指定将 DHCP 服务器配置为路由器的机器的 IP 地址。 

`subnet` 块定义了单独子网的选项，这些子网映射到运行“dhcpd”的网络接口。在我们的示例中，这是一个用于单个接口 `eth0` 的子网 `139.96.30.0/24`，我们为其定义了可用 IP 地址的范围。此范围内的地址将分配给连接的客户端。 

###  只侦听单一网口

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 虽然手册界面 [dhcpd(8)](<https://man.archlinux.org/man/dhcpd.8>) 建议以下描述的行为，但实践中，`dhcpd` 仅监听在其配置文件中被声明的子网接口。 (在[Talk:Dhcpd](<../zh-cn/Talk:Dhcpd.html>)讨论)

如果你的计算机已经是一个或多个网络中的一部分，那在你的计算机给其他网络的计算机分配 IP 地址时可能会有问题。这可以通过配置 dhcpd 或使用 [systemctl](<../zh-cn/Systemd.html#Using_units> "Systemd") 以守护进程的形式启动。 

####  配置 dhcpd

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** `dhcpd` 不监听子网不在配置文件中声明的接口。（在 [Talk:Dhcpd](<../zh-cn/Talk:Dhcpd.html>) 中讨论）

为了排除接口，您必须为将在该接口上配置的子网创建一个空声明。 

这是通过编辑配置文件来完成的（例如）： 
    
    /etc/dhcpd.conf
    
    # No DHCP service in DMZ network (192.168.2.0/24)
    subnet 192.168.2.0 netmask 255.255.255.0 {
    }
    
####  服务文件

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 使用 systemd 251 测试时无效。（在 [Talk:Dhcpd](<../zh-cn/Talk:Dhcpd.html>) 中讨论）

_dhcpd_ 提供的默认服务文件没有指定接口。为 `dhcpd4.service` 使用 [drop-in unit file](</wzh/index.php?title=Drop-in_unit_file&action=edit&redlink=1> "Drop-in unit file（页面不存在）")，如下所示： 
    
    /etc/systemd/system/dhcpd4.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dhcpd -4 -q -cf /etc/dhcpd.conf -pf /run/dhcpd4/dhcpd.pid %I

这允许使用 `dhcpd4.service` 作为模板单元，将“dhcpd”绑定到特定接口；例如 `dhcpd4@_eth0_.service`，其中 _eth0_ 是[第一个枚举到的以太网设备](<https://freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames>)。 

###  用于 PXE

PXE 配置通过以下两个选项完成： 
    
    /etc/dhcpd.conf
    
    next-server 192.168.0.2;
    filename "/pxelinux.0";

此部分可以在整个 `subnet` 中或仅在 `host` 定义中。 `next-server` 是 TFTP 服务器的 IP，`filename` 是要引导的映像的文件名。有关详细信息，请参阅 [PXE](<../zh-cn/PXE.html> "PXE")。 

##  参阅

  * [ISC DHCP 文档](<https://kb.isc.org/docs/aa-00333>)
