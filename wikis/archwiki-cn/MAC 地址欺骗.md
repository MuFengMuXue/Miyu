**翻译状态：**

  * 本文（或部分内容）译自 [MAC address spoofing](<https://wiki.archlinux.org/title/MAC_address_spoofing> "arch:MAC address spoofing")，最近一次同步于 2018-05-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/MAC_address_spoofing?diff=0&oldid=520883>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MAC_address_spoofing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

这篇文章文章将会介绍几个修改 MAC 地址的方法。 

##  手动更改

有两种方法可以修改 MAC 地址：[安装](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")并配置 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包 或 [macchanger](<https://archlinux.org/packages/?name=macchanger>)包。下面来说明一下这两种方法。 

### iproute2

首先，你可以用下面的命令来检查当前的 MAC 地址 
    
    # ip link show _interface_
    
`_interface_` 是你的[网卡](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")的名字 

我们现在要关注的是跟在“link/ether”后面的那一串带冒号的十六进制字节。它看起来可能是这样： 
    
    link/ether 00:1d:98:5a:d1:3a
    
修改 MAC 地址的第一步是禁用网卡，它可以通过下面的命令来完成： 
    
    # ip link set dev _interface_ down
    
接下来，我们要开始修改我们的 MAC 地址。只要每个字节都是十六进制值就可以，但有的网络运营商可能会拒绝为不正确的 MAC 分配 IP 地址。所以，除非你是你连接的网络的管理员，否则你应该使用真实的 MAC 地址前缀（一般是前三个字节），剩下三个字节可以随便设置（只要是十六进制值）。如果想了解更多内容，请访问 [Wikipedia:Organizationally unique identifier](<https://en.wikipedia.org/wiki/Organizationally_unique_identifier> "wikipedia:Organizationally unique identifier"). 

要更改 MAC 地址，我们要运行这个命令： 
    
    # ip link set dev _interface_ address _XX:XX:XX:XX:XX:XX_
    
这6位 `_XX:XX:XX:XX:XX:XX_` 就是你要设置的 MAC 地址。 

最后一步是重新启用网卡，输入这行命令： 
    
    # ip link set dev _interface_ up
    
如果你想验证你的 MAC 地址是否成功修改，只需要再次运行 `ip link show _interface_` ，然后检查“link/ether”后面的值。如果成功修改，“link/ether”后面应该跟着你刚刚设置的 MAC 地址。 

### macchanger

另一个方法是通过 [macchanger](<https://archlinux.org/packages/?name=macchanger>)包 (a.k.a., the GNU MAC Changer)。它有一些方便的功能，比如改变 MAC 地址以匹配某个运营商，或者完全随机化地址。 

从[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")里[安装](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")这个包 [macchanger](<https://archlinux.org/packages/?name=macchanger>)包 . 

由于更改 MAC 地址基于网卡，我们需要用[网卡名](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")来替换每行命令中的 `_interface_` 。 

用这行命令我们可以将 MAC 地址完全随机化： 
    
    # macchanger -r _interface_
    
要随机化当前 MAC 地址的后三位字节 (这样运营商会认为这个 MAC 地址是注册过的 MAC 地址，就可以避免被断网的风险)，你可以运行这个命令 
    
    # macchanger -e _interface_
    
要把 MAC 地址改成指定的值，请运行： 
    
    # macchanger --mac=_XX:XX:XX:XX:XX:XX_ _interface_
    
把 `_XX:XX:XX:XX:XX:XX_` 改成你想要的 MAC 地址。 

最后，如果想把 MAC 地址恢复成出厂值，运行这个： 
    
    # macchanger -p _interface_
    
**注意：** 在更改 MAC 地址的时候，设备将无法使用（无论是以任何方式连接，或是试图启用这个设备）

##  自动更改

### systemd-networkd

[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 支持通过 [link files](<../zh-cn/Systemd-networkd.html#link_files> "Systemd-networkd") 设置 MAC 地址（细节请查看 [systemd.link(5)](<https://man.archlinux.org/man/systemd.link.5>)）. 

要设置一个静态 MAC 地址，修改这个文件为： 
    
    /etc/systemd/network/00-default.link
    
    [Match]
    MACAddress=_原始 MAC_
    
    [Link]
    MACAddress=_更改后的 MAC_
    NamePolicy=kernel database onboard slot path

如要在每次启动时随机化 MAC 地址，把 `MACAddress=_更改后的 MAC_` 改成 `MACAddressPolicy=random`。 

### systemd-udevd

[udev](<../zh-cn/Udev.html> "Udev") 允许你创建 udev 规则 来更改 MAC 地址。使用 `address` 参数来用原始 MAC 地址来匹配设备，然后用 _ip_ 命令来更改 MAC 地址: 
    
    /etc/udev/rules.d/75-mac-spoof.rules
    
    ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="XX:XX:XX:XX:XX:XX", RUN+="/usr/bin/ip link set dev %k address YY:YY:YY:YY:YY:YY"

其中，`XX:XX:XX:XX:XX:XX` 是原始 MAC 地址，`YY:YY:YY:YY:YY:YY` 是目标 MAC 地址 

###  systemd 单元

####  创建单元

下面写了两个用 [Systemd](<../zh-cn/Systemd.html> "Systemd") 来在启动时更改 MAC 地址的例子，其中一个用 _ip_ 来设置静态 MAC，另一个用 _macchanger_ 来设置随机 MAC。systemd 的 `network-pre.target` 可以确保 MAC 地址在网络管理器如 [netctl](<../zh-cn/Netctl.html> "Netctl")、[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")、[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 或 [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") 启动之前就已经更改好。 

##### iproute2

设置静态 MAC 地址的 [Systemd](<../zh-cn/Systemd.html> "Systemd") 单元: 
    
    /etc/systemd/system/macspoof@.service
    
    [Unit]
    Description=MAC Address Change %I
    Wants=network-pre.target
    Before=network-pre.target
    BindsTo=sys-subsystem-net-devices-%i.device
    After=sys-subsystem-net-devices-%i.device
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/ip link set dev %i address 36:aa:88:c8:75:3a
    ExecStart=/usr/bin/ip link set dev %i up
    
    [Install]
    WantedBy=multi-user.target
    
##### macchanger

设置随机 MAC 地址的 [Systemd](<../zh-cn/Systemd.html> "Systemd") 单元，同时保留原始的运营商字节。请确保您已[安装](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")了 [macchanger](<https://archlinux.org/packages/?name=macchanger>)包: 
    
    /etc/systemd/system/macspoof@.service
    
    [Unit]
    Description=macchanger on %I
    Wants=network-pre.target
    Before=network-pre.target
    BindsTo=sys-subsystem-net-devices-%i.device
    After=sys-subsystem-net-devices-%i.device
    
    [Service]
    ExecStart=/usr/bin/macchanger -e %I
    Type=oneshot
    
    [Install]
    WantedBy=multi-user.target
    
或者用 `-r` 选项来使 MAC 地址完全随机化，参见 [#macchanger](<#macchanger>)。 

####  启用服务

将所需的网络接口 (如：`eth0`) 附加到服务名称后面 (如`macspoof@eth0.service`)，然后[启用](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")服务. 

重启，或者按照适当的顺序重启依赖的服务。如果你是局域网管理员，请通过路由器检查其中的静态或 DHCP 地址表，验证 MAC 是否已成功修改。 

###  netctl 接口

你可以使用 [netctl hook](<../zh-cn/Netctl.html#Using_hooks> "Netctl") 来在每次启动或重启网卡的时候运行特定命令。把 `_interface_` 替换为你的[网络接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置"): 
    
    /etc/netctl/interfaces/_interface_
    
    #!/usr/bin/env sh
    /usr/bin/macchanger -r _interface_

使脚本可执行： 
    
    chmod +x /etc/netctl/interfaces/_interface_
    
来源: [akendo.eu](<https://blog.akendo.eu/archlinuxrandom-mac-address-for-new-wireless-connections/>)

### NetworkManager

参见 [NetworkManager#Configuring MAC address randomization](<../zh-cn/NetworkManager.html#Configuring_MAC_address_randomization> "NetworkManager"). 

##  故障排除

###  连接到 DHCPv4 网络失败

如果您无法连接到 DHCPv4网络，而且您使用的是 NetworkManager 默认的 dhcpcd，你可能需要[修改 dhcpd 配置](<../zh-cn/Dhcpcd.html#Client_ID> "Dhcpcd")来续租。 

##  另见

  * [Wikipedia:MAC spoofing](<https://en.wikipedia.org/wiki/MAC_spoofing> "wikipedia:MAC spoofing")
  * [Macchanger GitHub page](<https://github.com/alobbs/macchanger>)
  * [DebianAdmin 上的文章](<https://www.debianadmin.com/change-your-network-card-mac-media-access-control-address.html>) with more _macchanger_ options
