**翻译状态：**

  * 本文（或部分内容）译自 [Wake-on-LAN](<https://wiki.archlinux.org/title/Wake-on-LAN> "arch:Wake-on-LAN")，最近一次同步于 2024-01-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/Wake-on-LAN?diff=0&oldid=798980>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Wake-on-LAN_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [电源管理/唤醒触发器](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E5%94%A4%E9%86%92%E8%A7%A6%E5%8F%91%E5%99%A8.html> "电源管理/唤醒触发器")

网络唤醒（Wake-on-LAN,WoL）是一个通过网络来打开计算机的功能。 

##  硬件设置

网络唤醒只在满足以下前提条件时有效： 

  1. 目标计算机的主板和网卡支持网络唤醒。

  1. 目标计算机必须 _物理地_ 连接（使用线缆）到一台路由器或者源计算机才能让网络唤醒正常工作，除非你的无线网卡支持无线唤醒（WoWLAN或WoW）。

你需要在你的BIOS或UEFI中准备： 

  1. 启用网络唤醒功能。不同的主板制造商使用稍微不同的语言来描述这项功能。查找像是“PCI Power up”“Allow PCI wake up event”或“Boot from PCI/PCI-E”的术语。

  1. 如果在BIOS/UEFI中可用，确保[ErP](<https://www.cgdirector.com/what-is-erp-mode-erp-ready-in-bios>)是**禁用** 的，否则你的网卡将不会有电并且将不会从其他设备受到任何网络唤醒包。

**注意：**

  * 有些主板在关机状态下支持网络唤醒，但有的主板只在睡眠或挂起状态下支持网络唤醒。
  * 一些主板受到一个Bug的影响，导致当BIOS的网络唤醒功能启用时立刻或随机在关机后唤醒。

##  软件设置

###  在网卡上启用网络唤醒

根据硬件的不同，网卡驱动可能默认关闭网络唤醒。 

要查询或更改这项设置，安装[ethtool](<https://archlinux.org/packages/?name=ethtool>)包，确定[网络配置#网络接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")的名字，并用以下命令来查询： 
    
    # ethtool _interface_ | grep Wake-on
    
    Supports Wake-on: pumbag
    Wake-on: d
    
值 _Wake-on_ 定义了触发唤醒的活动：`d`（禁用）、`p`（PHY活动）、`u`（单播活动）、`m`（多播活动）、`b`（广播活动）、`a`（ARP活动）和`g`（魔术包活动）。 网络唤醒工作需要值为`g`，如果不是，使用以下命令启用网卡驱动的网络唤醒功能： 
    
    # ethtool -s _interface_ wol g
    
**注意：** 为了启用该功能，可能还需要设置`u`、`m`和`b`中的一个以及`g`。

此命令的操作在下一次重启之后可能不会保留，在这种情况下，必须通过某种机制来重复执行。下面列出了常见的解决方案。 

###  让其持久

#### systemd.link

可以通过[systemd-networkd#link文件](<../zh-cn/Systemd-networkd.html#link%E6%96%87%E4%BB%B6> "Systemd-networkd")进行link-level配置。实际配置由udev`net_setup_link`内置程序执行。向网络link文件中添加`WakeOnLan`： 
    
    /etc/systemd/network/50-wired.link
    
    [Match]
    MACAddress=_aa:bb:cc:dd:ee:ff_
    
    [Link]
    NamePolicy=kernel database onboard slot path
    MACAddressPolicy=persistent
    **WakeOnLan=magic**

另请参阅[systemd.link(5)](<https://man.archlinux.org/man/systemd.link.5>)以获取更多信息。 

**注意：**

  * 仅应用第一个匹配的文件。必须包括systemd附带的链接文件`/usr/lib/systemd/network/99-default.link`的内容，否则接口可能配置错误。
  * 需要考虑的是，文件名应该按顺序放在默认的`99-default.link`之前，例如`50-wired.link`就可以。
  * 此配置仅适用于link级别，并且独立于像是[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")和[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")这样的network级别守护程序。
  * 在`Match`部分，`OriginalName=`也可以用于识别接口。

#### systemd service

这相当于前面的`systemd.link`选项，但使用独立的systemd服务。 
    
    /etc/systemd/system/wol@.service
    
    [Unit]
    Description=Wake-on-LAN for %i
    Requires=network.target
    After=network.target
    
    [Service]
    ExecStart=/usr/bin/ethtool -s %i wol g
    Type=oneshot
    
    [Install]
    WantedBy=multi-user.target

或者安装[wol-systemd](<https://aur.archlinux.org/packages/wol-systemd/>)AUR，然后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")激活这个新服务`wol@_接口_.service`。 

#### udev

[udev](<../zh-cn/Udev.html> "Udev")能够在设备可见时立即运行任何命令。以下规则将在名称与`en*`匹配的所有网络接口上打开网络唤醒。文件名很重要，它必须以81到99之间的数字开头，这样它才能在`80-net-setup-link.rules`之后运行，后者用可预测的名称重命名接口，否则`NAME`将未定义，规则将不会运行。 
    
    /etc/udev/rules.d/**81** -wol.rules
    
    ACTION=="add", SUBSYSTEM=="net", NAME=="en*", RUN+="/usr/bin/ethtool -s $name wol g"

`$name`占位符将替换为匹配设备的`NAME`变量的值。 

#### cron

每次使用crontab中的"@reboot"重启计算机时，都可以运行一个命令。首先,确保启用[cron](<../zh-cn/Cron.html> "Cron")，然后为root用户编辑含以下行的crontab： 
    
    @reboot /usr/bin/ethtool -s _interface_ wol g
    
#### netctl

如果使用[netctl](<../zh-cn/Netctl.html> "Netctl")，可以通过添加以下netctl配置文件使此设置永久化： 
    
    /etc/netctl/_profile_
    
    ExecUpPost='/usr/bin/ethtool -s _interface_ wol g'

#### NetworkManager

NetworkManager提供[网络唤醒支持](<https://www.phoronix.com/scan.php?page=news_item&px=NetworkManager-WoL-Control>)。通过魔术包启用网络唤醒的一种方式是通过 _nmcli_ 。 

首先，搜索有线连接的名称： 
    
    # nmcli con show
    
    NAME    UUID                                  TYPE            DEVICE
    wired1  612e300a-c047-4adb-91e2-12ea7bfe214e  802-3-ethernet  enp0s25

通过以下操作可以查看网络唤醒设置的当前状态： 
    
    # nmcli c show "wired1" | grep 802-3-ethernet.wake-on-lan
    
    802-3-ethernet.wake-on-lan:             default
    802-3-ethernet.wake-on-lan-password:    --

在连接上启用魔术包网络唤醒： 
    
    # nmcli c modify "wired1" 802-3-ethernet.wake-on-lan magic
    
然后重启，可能是两次。要禁用网络唤醒，使用`ignore`替换`magic`。 

使用[nm-connection-editor](<https://archlinux.org/packages/?name=nm-connection-editor>)包GUI也可以更改网络唤醒设置。 

你可以通过添加一个专用的配置文件来为所有连接永久禁用网络唤醒： 
    
    /etc/NetworkManager/conf.d/_wake-on-lan.conf_
    
    [connection]
    ethernet.wake-on-lan = ignore
    wifi.wake-on-wlan = ignore

###  在TLP启用网络唤醒

当使用[TLP](<../zh-cn/TLP.html> "TLP")进行挂起或休眠时，`/etc/tlp.conf`中的`WOL_DISABLE`设置必须设置为`N`来允许使用网络唤醒来恢复电脑。 

##  触发唤醒

要触发目标设备的网络唤醒，必须知道它的**MAC地址** 。要获取它，在设备商执行下面的命令： 
    
    $ ip link
    
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp1s0: <BROADCAST,MULTICAST,PROMISC,UP,LOWER_UP> mtu 1500 qdisc fq_codel master br0 state UP group default qlen 1000
        link/ether **48:05:ca:09:0e:6a** brd ff:ff:ff:ff:ff:ff
    
这里的MAC地址是`48:05:ca:09:0e:6a`。 

在最简单的形式中，网络唤醒将魔术包作为以太网帧进行广播，其中包含当前网络子网中IP协议层下方的MAC地址。不需要了解IP地址，因为它在第二层（数据链路层）上运行。 

如果用于通过互联网或其它子网唤醒计算机，通常依赖路由器中继数据包并进行广播。在这种情况下，路由器的外部IP地址必须是已知的。请记住，作为安全措施，大部分路由器默认情况下不会中继子网定向广播，需要明确告知这样做。 

能够为网络唤醒发送魔术包的应用程序： 

  * **gWakeOnLAN** — 通过网络唤醒功能来唤醒关闭的电脑的GTK程序。

     <https://www.muflone.com/gwakeonlan/english/> || [gwakeonlan](<https://archlinux.org/packages/?name=gwakeonlan>)包

  * **wol** — 在一个小的程序中实现局域网唤醒功能。它唤醒服从魔术包的硬件。注意：此应用程序需要需要使用-p参数将端口默认值（40000）改为9。

     <https://sourceforge.net/projects/wake-on-lan/> || [wol](<https://archlinux.org/packages/?name=wol>)包

  * **wol_qt** — 具有集成ARP扫描的Qt程序，用于查找MAC地址和批量发送局域网唤醒数据包。

     <https://github.com/stefmitropoulos/wol_qt> || [wol_qt](<https://aur.archlinux.org/packages/wol_qt/>)AUR

###  在同一局域网中

如果你通过网络线缆直接连接到另一台电脑，或者局域网内的通信没有防火墙，那么使用网络唤醒会很简单，因为无需担心端口重定向。 

在最简单的情况下，使用默认广播地址`225.225.225.225`： 
    
    $ wol _目标的MAC地址_
    
要仅将魔术包广播到特定的子网或主机，请使用`-i`： 
    
    $ wol -i _target_IP_ _target_MAC_address_
    
###  通过因特网

当源计算机和目标计算机被NAT路由器分隔时，可以设想不同的解决方案： 

  * 如果路由器支持网络唤醒，则可以通过它将数据包正确广播到本地网络。

否则可以通过端口转发实现局域网唤醒。路由器需要使用以下两个选项之一进行配置： 

  * 将不同的端口转发到目标计算机。这需要每台目标计算机在它的局域网有一个静态的IP。

  * 将单个端口转发到广播地址。大多数路由器不允许转发到广播，但是你可以通过telnet、SSH、串口（console）或其它方式获得访问路由器的shell的权限，并运行下面的命令：

    $ ip neighbor add 192.168.1.254 lladdr FF:FF:FF:FF:FF:FF dev net0

此示例假设网络为192.168.1.0/24，并使用net0作为网络接口。现在，将UDP端口9转发到192.168.1.254。该解决方案已在运行[Tomato](<https://en.wikipedia.org/wiki/Tomato_\(firmware\)> "wikipedia:Tomato \(firmware\)")的Linksys WRT54G和Verizon FIOS ActionTec路由器上成功测试。有关如何在具有[DD-WRT](<https://en.wikipedia.org/wiki/DD-WRT> "wikipedia:DD-WRT")固件上的路由器执行此操作的说明，请参见[这个教程](<https://www.dd-wrt.com/wiki/index.php/WOL#Remote_Wake_On_LAN_via_Port_Forwarding>)；对于具有OpenWrt固件的路由器，请参阅[这个教程](<https://openwrt.org/docs/guide-user/services/w_o_l/wol>)。 

在任何情况下，从源计算机运行以下命令以触发唤醒： 
    
    $ wol -p _forwarded_port_ -i _router_IP_ _target_MAC_address_
    
##  杂项

###  检查魔术包的接受情况

为了确保网络唤醒数据包到达目标计算机，可以监听UDP端口，通常是端口9，以获取魔术包。魔术包的帧预计会包含6字节的FF，之后是目标计算机的16个重复（每个6字节），总共102字节。 

####  使用netcat

这可以通过在目标计算机上安装[gnu-netcat](<https://archlinux.org/packages/?name=gnu-netcat>)包并使用以下命令来执行： 
    
    # nc --udp --listen --local-port=9 --hexdump
    
然后等待传入流量出现在`nc`终端里。 

**注意：** 电脑本身的防火墙不需要打开即可网络唤醒（接口的处理发生在NIC中，在防火墙之前）。但是，为了使用netcat进行调试，你仍然需要临时打开该端口。

####  使用ngrep

在目标设备上安装[ngrep](<https://archlinux.org/packages/?name=ngrep>)包并执行下面的命令： 
    
    # ngrep '\xff{6}(.{6})\1{15}' -x port 9
    
###  网络唤醒脚本示例

下面是一个说明了在不同的机器上使用网络唤醒的示例： 
    
    #!/bin/bash
    
    # definition of MAC addresses
    monster=01:12:46:82:ab:4f
    ghost=01:1a:d2:56:6b:e6
    
    echo "Which PC to wake?"
    echo "m) monster"
    echo "g) ghost"
    echo "q) quit"
    read input1
    case $input1 in
      m)
        /usr/bin/wol $monster
        ;;
      g)
        # uses wol over the internet provided that port 9 is forwarded to ghost on ghost's router
        /usr/bin/wol --port=9 --host=ghost.mydomain.org $ghost
        ;;
      Q|q)
        break
        ;;
    esac
    
##  故障排除

### NetworkManager

####  网络适配器在关机时处于断电状态

如果通过 _nmcli_ 配置了网络唤醒，并且网络适配器在关机时处于断电状态，则将自动协商设置为`yes`可能会有所帮助。设置使用它： 

    # nmcli c modify "wired1" 802-3-ethernet.auto-negotiate yes
    
###  在关机后唤醒

众所周知,一些主板会受到一个Bug的影响，无论何时启用BIOS的网络唤醒功能（例如[这里](<https://bbs.archlinux.org/viewtopic.php?id=173648>)所讨论的），该错误都会导致关机后立即或随即唤醒。 

####  使用BIOS修复

BIOS首选项中的以下操作可以解决某些主板的问题： 

  1. 禁用USB设置中所有对 _xHCI_ 的引用（注意，这也会在启动时禁用USB3.0）。

  1. 如果 _EuP 2013‘’是一个明确的选项，禁用它。_

  1. 可选地启用键盘唤醒操作。

**注意：** 对于上面第三条的值，有各种各样的意见，它可能取决于主板。

####  通过内核修复

这个问题也可以通过添加`xhci_hcd.quirks=270336`内核参数来解决。这会激活： 

  * `XHCI_SPURIOUS_REBOOT`
  * `XHCI_SPURIOUS_WAKEUP`

###  电池排空的问题

一些笔记本电脑在关机后会出现电池耗尽的问题[[1]](<https://ubuntuforums.org/archive/index.php/t-1729782.html>)。这可能由启用网络唤醒导致。要解决这个问题，像上面提到的一样禁用网络唤醒： 
    
    # ethtool -s net0 wol d
    
###  瑞昱

使用基于瑞昱8168 8169 8101 8111（C）的NIC（网卡和板载网卡）时,可能会注意到NIC在启动时似乎被禁用，并且没有指示灯。请参阅[网络配置/以太网#Realtek_没有连接/网络唤醒故障](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E4%BB%A5%E5%A4%AA%E7%BD%91.html#Realtek_%E6%B2%A1%E6%9C%89%E8%BF%9E%E6%8E%A5/%E7%BD%91%E7%BB%9C%E5%94%A4%E9%86%92%E6%95%85%E9%9A%9C> "网络配置/以太网")。 

如果网络交换机上的链路指示灯在计算机关闭但网络唤醒仍不工作时启用，则至少使用r8168内核模块引导系统一次，然后切换回内核中包含r8169的内核模块似乎至少可以在以下配置中解决该问题： 

  * MSI B85M-E45主板, BIOS版本V10.9, 板载Realtek 8111G 芯片组

对于r8168模块，你可能需要设置 `s5wol=1`[内核模块#配置模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")来启用网络唤醒功能。 

###  alx驱动支持

对于一些较新的基于Atheros的NIC（如Atheros AR8161和Killer E2500），由于一个导致意外唤醒的Bug,主线alx模块中的网络唤醒支持已被禁用（请参阅[该讨论](<https://lore.kernel.org/netdev/1372880891-12320-1-git-send-email-johannes@sipsolutions.net/>)）。可以使用补丁（使用[alx-wol-dkms](<https://aur.archlinux.org/packages/alx-wol-dkms/>)AUR包安装一个[dkms](</wzh/index.php?title=Dkms&action=edit&redlink=1> "Dkms（页面不存在）")模块），该补丁不仅恢复了网络唤醒支持，还修复了潜在的错误，如[这里](<https://bugzilla.kernel.org/show_bug.cgi?id=61651>)所述。 

另请参阅预修复补丁的源代码[[2]](<https://github.com/Snugface/alx>)。 
