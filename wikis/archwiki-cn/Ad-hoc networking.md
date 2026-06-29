**翻译状态：**

  * 本文（或部分内容）译自 [Ad-hoc_networking](<https://wiki.archlinux.org/title/Ad-hoc_networking> "arch:Ad-hoc networking")，最近一次同步于 2022-08-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ad-hoc_networking?diff=0&oldid=743231>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ad-hoc_networking_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络配置](<../zh-cn/Network_configuration.html> "Network configuration")
  * [无线设置](<../zh-cn/Wireless_Setup.html> "Wireless Setup")
  * [软AP](</wzh/index.php?title=%E8%BD%AFAP&action=edit&redlink=1> "软AP（页面不存在）")
  * [Internet sharing](<../zh-cn/Internet_sharing.html> "Internet sharing")

Independent Basic Service Set(独立基本服务集)，缩写是 IBSS，也被称为自组网络，是一种不使用中心控制节点，就能让一组设备相互通讯的方法。是点对点网络的一种，网络中的设备直接通讯，不需要中转。自组网络可以用来进行[网络共享](<../zh-cn/Internet_sharing.html> "Internet sharing")。 

##  要求

所有要连接到网络的设备都具有兼容 [[1]](<https://wireless.wiki.kernel.org/en/users/drivers%7Cnl80211>) 的无线网卡。 

##  Wifi 链路层

因为 IBSS 网络是点对点网络，所有设备都应该使用相同的 wifi 连接设置。 

**提示：** 可以设置更复杂的网络拓扑，[Linux 无线文档](<https://wireless.wiki.kernel.org/en/users/documentation/iw/vif>) 包含更高级的示例。

###  手动设置

**警告：** 此方法创建的是 **非加密** 自组网络，要创建加密网络，请参考 [#wpa_supplicant](<#wpa_supplicant>).

详细信息请参考[网络配置/Wireless#iw](</wzh/index.php?title=%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/Wireless&action=edit&redlink=1> "网络配置/Wireless（页面不存在）")。请先[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [iw](<https://archlinux.org/packages/?name=iw>)包。 

设置操作模式为 ibss: 
    
    # iw _interface_ set type ibss
    
启动接口(可能需要额外的 `rfkill unblock wifi`): 
    
    # ip link set _interface_ up
    
现在可以创建自组网络了，将 _your_ssid_ 替换为实际的网络， _frequency_ 替换为以 MHz 为单位的频率。频道和频率的对应关系，请参考, [这里](<https://en.wikipedia.org/wiki/List_of_WLAN_channels#Interference_Concerns> "wikipedia:List of WLAN channels")。 
    
    # iw _interface_ ibss join _your_ssid_ _frequency_
    
### wpa_supplicant

确保已经[安装](<../zh-cn/Pacman.html> "Pacman")了 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包，并进行了配置(参考 [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant")). 
    
    /etc/wpa_supplicant-adhoc.conf
    
    ctrl_interface=DIR=/run/wpa_supplicant GROUP=wheel
    
    # use 'ap_scan=2' on all devices connected to the network
    # this is unnecessary if you only want the network to be created when no other networks are available
    ap_scan=2
    
    network={
        ssid="MySSID"
        mode=1
        frequency=2432
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        group=CCMP
        psk="secret passphrase"
    }
    
所有连接到网络的设备运行下面 _wpa_supplicant_ 命令: 
    
    # wpa_supplicant -B -i _interface_ -c /etc/wpa_supplicant-adhoc.conf -D nl80211,wext
    
##  网络配置

最后一步是给网络中的所有设备分配 IP 地址，有多种方法： 

  * 分配静态 IP 地址，参考：[网络配置#Static IP address](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Static_IP_address> "网络配置").
  * 在一个设备上运行 DHCP，参考 [dhcpd](<../zh-cn/Dhcpd.html> "Dhcpd") 或 [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq").
  * 运行 _avahi-autoipd_. 参考 [Avahi#Obtaining IPv4LL IP address](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）").

要向自组网络共享外网连接，请参考 [Internet sharing](<../zh-cn/Internet_sharing.html> "Internet sharing"). 

##  技巧

###  使用 NetworkManager

如果使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")，可以使用 _nm-applet_ 进行自组网络配置，不用使用手动方法。详情参考 [NetworkManager#Sharing internet connection over Wi-Fi](<../zh-cn/NetworkManager.html#Sharing_internet_connection_over_Wi-Fi> "NetworkManager")。 

###  自定义 systemd 服务(使用 wpa_supplicant 和静态 IP)

可以使用下面模板启用无线自组网络： 
    
    /etc/conf.d/network-wireless-adhoc@_interface_
    
    addr=192.168.0.2
    mask=24
    
    /etc/systemd/system/network-wireless-adhoc@.service
    
    [Unit]
    Description=Ad-hoc wireless network connectivity (%i)
    Wants=network.target
    Before=network.target
    BindsTo=sys-subsystem-net-devices-%i.device
    After=sys-subsystem-net-devices-%i.device
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    EnvironmentFile=/etc/conf.d/network-wireless-adhoc@%i
    
    # perhaps rfkill is not needed for you
    ExecStart=/usr/bin/rfkill unblock wifi
    ExecStart=/usr/bin/ip link set %i up
    ExecStart=/usr/bin/wpa_supplicant -B -i %i -D nl80211,wext -c /etc/wpa_supplicant-adhoc.conf
    ExecStart=/usr/bin/ip addr add ${addr}/${mask} dev %i
    
    ExecStop=/usr/bin/ip addr flush dev %i
    ExecStop=/usr/bin/ip link set %i down
    
    [Install]
    WantedBy=multi-user.target

## See also

  * [Ubuntu community wiki WifiDocs/Adhoc](<https://help.ubuntu.com/community/WifiDocs/Adhoc>)
  * [Manual about creating an Ad-Hoc network on UbuntuGeek](<https://www.ubuntugeek.com/creating-an-adhoc-host-with-ubuntu.html>)
  * [Share your 3G Internet connection over wifi](<https://web.archive.org/web/20200225211430/http://go2linux.garron.me/linux/2011/03/share-your-3g-internet-connection-over-wifi-linux-ipod-touch-925/>)
