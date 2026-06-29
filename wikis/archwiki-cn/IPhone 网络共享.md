**翻译状态：**

  * 本文（或部分内容）译自 [iPhone tethering](<https://wiki.archlinux.org/title/iPhone_tethering> "arch:iPhone tethering")，最近一次同步于 2025-01-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/iPhone_tethering?diff=0&oldid=822105>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/iPhone_tethering_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

您可以通过 **Wi-Fi** 、**USB** 或**蓝牙** 来在设备上共享您的 iPhone 的移动数据连接，除非您的服务提供商（运营商）禁用了此功能： 

  * 只要您的电脑能够连接无线网络，Wi-Fi 就不需要其他额外配置，
  * 下文提供使用 USB 与蓝牙的操作指南。

##  通过 USB 进行共享

通过原生的 USB 进行共享是最理想的方式，因为其可以提供更加稳定的连接，且较蓝牙和 Wi-Fi 共享消耗的电量较少。 

要使用 USB 进行 iPhone 网络共享，您需要安装 [libimobiledevice](<https://archlinux.org/packages/?name=libimobiledevice>)包 与 [usbmuxd](<https://archlinux.org/packages/?name=usbmuxd>)包。**usbmuxd** 依赖于 **libimobiledevice** ，其中 usbmuxd 负责系统与 iOS 设备间的底层连接。**usbmuxd** 包也包含了一条 udev 规则，使其能够在设备连接或断开连接时自动启动与停止该守护进程。相关内容详见 [iOS](<../zh-cn/IOS.html> "IOS")。 

连接 iOS 设备，并确保 `usbmuxd.service` 已经自动启动。 

下一步，在您的 iPhone 上启用 _个人热点_ （ _Personal Hotspot）_ ，并将其用数据线连接至您的电脑。这时您应该会多出一个可用的以太网连接，并能够使用任意[网络管理器](<../zh-cn/Network_manager.html> "Network manager")通过新加入的 iPhone 以太网设备连接到 Internet，与使用其他普通的以太网连接没有什么区别。 

如果您在使用 [MAC 地址伪装](<../zh-cn/MAC_address_spoofing.html> "MAC address spoofing")，您可能需要将不支持 MAC 复制的 `ipheth` 驱动程序列为例外。 
    
    /etc/NetworkManager/conf.d/your-file-here.conf
    
    [your-section]
    match-device=*,except:driver:ipheth

###  使用 systemd-networkd

如果您使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 进行网络管理，您能轻易将其配置为通过 iPhone 连接 Internet，与使用其他普通网络适配器时别无二致。 

假设 _enp0s26u1u2c4i2_ 是运行 `networkctl list` 命令时展示的 iPhone 创建的网络设备的名称，创建下面的 _.network_ 文件： 
    
    /etc/systemd/network/30-tethering.network
    
    [Match]
    Name=enp0s26u1u2c4i2
    
    [Network]
    DHCP=yes

###  故障排除

若设备列表中有 iPhone 但无法连接，您有可能需要在使用网络共享之前先将 iPhone 与您的电脑连接并进行配对。过程中，使用 PIN 的 iPhone 需要解锁。 
    
    # idevicepair pair
    
####  缺少驱动程序

如果您按照上面的步骤操作，但 `networkctl list` 命令仍无法检测到 iPhone，您可能缺少了[ipheth](<https://github.com/dgiagio/ipheth>) 驱动。您可以运行 `modprobe ipheth` 命令来检查您是否安装了该驱动程序。如果出现了错误消息，可能是您自行编译内核时发生的问题。请在编译内核时设置 `ipheth` flag。
    
    .config
    
    CONFIG_USB_IPHETH=y

##  通过蓝牙进行共享

使用蓝牙进行网络共享会相对较快地将电池耗尽。如果您同时连接了 USB 电源供应器，情况可能会稍好一些。 

###  硬件要求

  * 运行 iPhone OS 3.0 及以上的开启了网络共享的 iPhone。在 _设置 ＞ 通用 ＞ 网络_ 中开启网络共享选项。
  * 蓝牙控制器或类似的硬件设备，最好支持 EDR (_Enhanced Data Rate_) 以便获得相对较好的速度。在 _Belkin F8T016NE_ 上经过了测试。

###  设置

参考主文章[蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "Bluetooth")并设置好蓝牙守护程序。 

####  Gnome/XFCE

安装 [Blueman](</wzh/index.php?title=Blueman&action=edit&redlink=1> "Blueman（页面不存在）") GTK 蓝牙管理器。 

您的通知区域中应该会出现一个蓝牙图标（注意：如果在开机时未启用蓝牙，图标可能不会出现）。点击该图标，并搜索附近的设备，添加您的 iPhone。（注意，要使 iPhone 可以被发现，您可能需要在 iPhone 上打开设置中的蓝牙页面。） 

一旦 iPhone 被添加到了设备列表中，打开设备菜单并选择 配对 。通常这需要先在电脑后在 iPhone 上输入 PIN 码。连接好后，再次打开设备菜单，选择 _网络访问 ＞ 网络访问点_ 。如果一切正常的话，blueman 会报告成功，您的 iPhone 上的状态栏也会变为蓝色，表示成功建立了网络共享。 

Blueman 将会创建一个新的网络设备，一般为 bnep0。要连接到该设备，以 root 身份运行以下命令： 
    
    # dhcpcd bnep0
    
#### netcfg

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** _netcfg_ 已经被 [netctl](<../zh-cn/Netctl.html> "Netctl") 取代 (在[Talk:IPhone 网络共享](<../zh-cn/Talk:IPhone_%E7%BD%91%E7%BB%9C%E5%85%B1%E4%BA%AB.html>)讨论)

您也可以创建一个 [netcfg](<../zh-cn/Netctl.html> "Netcfg") 网络档案，以便在命令行界面中就可以轻松地进行网络共享而不需要使用 [Blueman](</wzh/index.php?title=Blueman&action=edit&redlink=1> "Blueman（页面不存在）") 或 Gnome。假设您有一部地址为 '00:00:DE:AD:BE:EF' 的已经配对好的 iPhone，只需要在 `/etc/network.d called` 中创建一个档案，例如 'tether' ： 
    
     CONNECTION="ethernet"
     DESCRIPTION="Ethernet via pand tethering to iPhone"
     INTERFACE="bnep0"
     IPHONE="00:00:DE:AD:BE:EF"
     PRE_UP="pand -E -S -c ${IPHONE} -e ${INTERFACE} -n 2>/dev/null"
     POST_DOWN="pand -k ${IPHONE}"
     IP="dhcp"
    
接下来执行： 
    
    # netcfg tether
    
要关闭网络连接并停止网络共享： 
    
    # netcfg down tether
    