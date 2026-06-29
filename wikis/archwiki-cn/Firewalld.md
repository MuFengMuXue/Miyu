**翻译状态：**

  * 本文（或部分内容）译自 [Firewalld](<https://wiki.archlinux.org/title/Firewalld> "arch:Firewalld")，最近一次同步于 2024-01-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Firewalld?diff=0&oldid=784096>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Firewalld_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [nftables](<../zh-cn/Nftables.html> "Nftables")

[firewalld](<https://firewalld.org/>) 是由红帽开发的防火墙守护进程。 默认使用 [nftables](<../zh-cn/Nftables.html> "Nftables") 。据项目主页： 

    Firewalld 提供了一个动态管理的防火墙，支持使用区域来标识网络连接/接口的可信等级。支持 IPv4、IPv6 防火墙设置、以太网桥接和 IP sets。使用分离的运行时配置和永久设置。也提供了一个接口用来直接为服务或应用添加防火墙规则。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [firewalld](<https://archlinux.org/packages/?name=firewalld>)包。 

##  使用

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `firewalld.service`. 

你可以使用控制台工具 `firewall-cmd` 来控制防火墙规则。 

`firewall-offline-cmd` 可在 firewalld 未运行时进行配置，与 `firewall-cmd` 类似。 

随 [firewalld](<https://archlinux.org/packages/?name=firewalld>)包 带的 `firewall-config` 命令提供了一个图形界面。 

##  配置

使用 `firewall-cmd` 可用于运行时更改配置 

**注意：** 大部分命令只会改变运行时配置而其将会在重启后丢失，要想进行永久配置有两种方式： 

  * 使用 `--permanent` 参数。这 **不会** 更改运行时配置直至防火墙服务重启，或使用 `--reload` 重载规则。
  * 持久化规则可见：[#将运行时配置设为永久](<#%E5%B0%86%E8%BF%90%E8%A1%8C%E6%97%B6%E9%85%8D%E7%BD%AE%E8%AE%BE%E4%B8%BA%E6%B0%B8%E4%B9%85>)

###  区域

区域是一系列可用于指定接口的规则。 

要查看当前区域及其应用的接口，使用： 
    
    # firewall-cmd --get-active-zones
    
一些命令（例如 add/remove port/service） 需要指定区域/ 

区域可以通过 `--zone=_zone_name_` 参数传递。 

若未指定一个确切的区域，则使用默认区域。 

####  区域信息

你可以列出所有区域的配置： 
    
    # firewall-cmd --list-all-zones
    
或指定一个区域 
    
    # firewall-cmd --info-zone=_zone_name_
    
####  更改接口区域
    
    # firewall-cmd --zone=_zone_ --change-interface=_interface_name_
    
此处 `_zone_` 是你想分配给接口的区域。 

#####  使用 NetworkManager 管理区域

[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 能够为不同的连接分配不同的区域。例如：将一个家庭 WiFi 分配到 "home" 区域， 将工作室 WiFi 分配到 "work" 区域，并将剩余 WiFi 分配到 "public" 区域。 

列出连接配置： 
    
    $ nmcli connection show
    
将 "myssid" 设置为 "home" 区域： 
    
    $ nmcli connection modify _myssid_ connection.zone _home_
    
####  默认区域

默认区域将会被自动应用到新的接口上，查询默认区域使用： 
    
    # firewall-cmd --get-default-zone
    
更改默认区域使用： 
    
    # firewall-cmd --set-default-zone=_zone_
    
**注意：** 此改变是临时的

###  服务

服务是为特定守护程序预配置的规则。例如匹配 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 的 服务 {{ic|ssh} 在被分配到一个区域后会开放 22 端口。 

使用下面的命令列出所有可用的服务： 
    
    # firewall-cmd --get-services
    
查询特定服务的信息： 
    
    # firewall-cmd --info-service _service_name_
    
####  从区域中添加或移除服务

添加一个服务到区域： 
    
    # firewall-cmd --zone=_zone_name_ --add-service _service_name_
    
移除服务： 
    
    # firewall-cmd --zone=_zone_name_ --remove-service _service_name_
    
###  端口

可以直接在指定区域上开放端口： 
    
    # firewall-cmd --zone=_zone_name_ --add-port _port_num_ /_protocol_
    
此处 `_protocol_` 应为 `tcp` 或 `udp` 之一。 

关闭端口使用带有相同的端口号和协议的 `--remove-port` 选项。 

###  NAT 地址伪装

此命令与 `iptables -t nat -A POSTROUTING -j MASQUERADE` 具有相同的效果： 
    
    # firewall-cmd --zone=public --add-masquerade
    
从版本 1.0.0 开始，如果想要 NAT 地址伪装在不同的防火墙区域之间工作，您必须创建一个新的策略对象，用于过滤它们之间的流量： 
    
    # firewall-cmd --new-policy NAT_int_to_ext --permanent
    # firewall-cmd --permanent --policy NAT_int_to_ext --add-ingress-zone internal
    # firewall-cmd --permanent --policy NAT_int_to_ext --add-egress-zone public
    # firewall-cmd --permanent --policy NAT_int_to_ext --set-target ACCEPT
    
###  端口转发

如果你在路由器上配置了 firewalld，而且还如上开启了 NAT 地址伪装，则通过 firewalld 设置端口转发很简单： 
    
    # firewall-cmd --zone=public --add-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40
    
这会将外部端口上的 12345/tcp 端口转发到内部网络 10.20.30.40 的 22 （标准 SSH） 端口。移除此端口转发： 
    
    # firewall-cmd --zone=public --remove-forward-port=port=12345:proto=tcp:toport=22:toaddr=10.20.30.40
    
不幸的是你必须键入完整的转发声明以移除它，只指定端口和协议是不行的。 

###  Rich 规则

通过使用 Rich 规则，可以以一种易于理解的方式创建更复杂的防火墙规则。 

要添加 Rich 规则： 
    
    # firewall-cmd [--zone=_zone_name_] [--permanent] --add-rich-rule='_rich_rule_ '
    
其中 `_rich_rule_` 是一条丰富语言规则。 

如果要允许来所有的连接自网络 `192.168.1.0/24` 到 [NFS](<../zh-cn/NFS.html> "NFS") [service](<#Services>)： 
    
    # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="nfs" accept'
    
要允许来自 `192.168.2.3` 到端口 `1234/tcp` 的连接： 
    
    # firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.2.3" port port="1234" protocol="tcp" accept'
    
有关更多 Rich 规则语法，请参阅 [firewalld.richlanguage(5)](<https://man.archlinux.org/man/firewalld.richlanguage.5>)。 

要删除 Rich 规则： 
    
    # firewall-cmd  [--zone=_zone_name_] [--permanent] --remove-rich-rule='_rich_rule_ '
    
##  提示和技巧

###  端口或服务有效时间

使用 `--timeout=_value_` 可以设置服务或端口的有效时间。时间默认为秒，`m` 后缀代表分钟， `h` 后缀代表小时。 例如：为 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 开放三小时的使用时间： 
    
    # firewall-cmd --add-service ssh --timeout=3h
    
**注意：** 超时选项与 --permanent 互斥。也就是说，超时只能是运行时配置，不可能持久化。

###  将运行时配置设为永久

你可以将运行时配置持久化（这意味着重启后也会保留配置） 
    
    # firewall-cmd --runtime-to-permanent
    
###  检查服务配置

`/usr/lib/firewalld/services/` 存储了默认支持的服务的配置文件，`/etc/firewalld/services/` 存储了用户创建的服务文件。 

###  移除程序/托盘图标

托盘图标与 [firewalld](<https://archlinux.org/packages/?name=firewalld>)包 一起打包。其自启动脚本位于 `/etc/xdg/autostart/firewall-applet.desktop` 可以被隐藏，参见 [XDG Autostart#目录](<../zh-cn/XDG_Autostart.html#%E7%9B%AE%E5%BD%95> "XDG Autostart")。另一种方法是，通过将其添加到 `/etc/pacman.conf` 中的 [NoExtract](<../zh-cn/Pacman.html#%E5%9C%A8%E5%AE%89%E8%A3%85%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "Pacman") 来阻止该文件的安装。 

##  参阅

  * [firewall-cmd(1)](<https://man.archlinux.org/man/firewall-cmd.1>)
  * [Official documentation](<https://firewalld.org/documentation>)
  * [Fedora:Firewalld](<https://fedoraproject.org/wiki/Firewalld> "fedora:Firewalld")
  * [Fedora:Features/FirewalldRichLanguage](<https://fedoraproject.org/wiki/Features/FirewalldRichLanguage> "fedora:Features/FirewalldRichLanguage")
