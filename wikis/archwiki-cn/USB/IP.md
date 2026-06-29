**翻译状态：**

  * 本文（或部分内容）译自 [USB/IP](<https://wiki.archlinux.org/title/USB/IP> "arch:USB/IP")，最近一次同步于 2023-11-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/USB/IP?diff=0&oldid=793225>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/USB_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/IP_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

USB-IP 是一个将通用的USB设备通过IP网络进行共享的系统。为了在计算机之间共享具有全部功能的USB设备，USB-IP将“USB I/O消息”封装到 TCP/IP 中，并在计算机之间传输，以实现远程共享或访问USB设备。 

##  安装

[安装](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [usbip](<https://archlinux.org/packages/?name=usbip>)包 包。 

##  使用

###  服务端配置

服务端为提供USB设备映射端，所以请确保已连接上物理USB设备，并且加载 `usbip_host` USB-IP[内核模块](<../../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")，下面命令为加载模块： 
    
    # modprobe usbip_host
    
然后使用systemctl来启用 `usbipd.service` 服务，服务默认监听TCP 3240端口。 

**注意：** 默认情况下，USB-IP 需要监听端口 3240。如果防火墙正在运行，请确保允许这个端口访问。有关配置防火墙的详细说明，请转到 [Category:防火墙](<../../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Category:防火墙")。
    
    # systemctl enable --now usbipd.service
    
查看当前主机已连接的USB设备总线ID（busid）: 
    
    $ usbip list -l
    
下面命令将USB设备 _busid_ 为 1-1.5 绑定到服务中： 

**注意：** 系统在[休眠](<../../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86.html#%E4%BC%91%E7%9C%A0%E5%92%8C%E6%8C%82%E8%B5%B7> "电源管理")后需要重新进行绑定。
    
    # usbip bind --busid=1-1.5
    
解除绑定: 
    
    # usbip unbind --busid=1-1.5
    
解除绑定后，客户端将无法访问该USB设备 

####  使用systemd进行绑定

如果想让系统开机后自动挂载，可以使用systemd模块单元文件，添加下面配置文件到系统中： 
    
    /etc/systemd/system/usbip-bind@.service
    
    [Unit]
    Description=USB-IP Binding on bus id %I
    After=network-online.target usbipd.service
    Wants=network-online.target
    Requires=usbipd.service
    #DefaultInstance=1-1.5
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/usbip bind --busid=%i
    RemainAfterExit=yes
    ExecStop=/usr/bin/usbip unbind --busid=%i  
    Restart=on-failure
    
    [Install]
    WantedBy=multi-user.target

然后启用配置，如想将USB设备 _busid_ 为1-1.5 自动绑定到服务中,只需使用systemclt命令[启动/启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `usbip-bind@1-1.service`： 
    
    # systemctl enable --now usbip-bind@_1-1.5_.service
    
###  客户端配置

客户端为加载远程USB设备端，需要加载 `vhci-hcd` [内核模块](<../../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")命令如下： 
    
    # modprobe vhci-hcd
    
查看远程服务端可用的USB设备，如果一切顺利将列出远程服务已绑定服务的所有USB设备: 
    
    $ usbip list --remote=_服务端IP_
    
记录下需要连接USB设备，例如连接到 _busid_ 为 1-1.5 的USB设备: 
    
    $ usbip attach --remote=_服务端IP_ -b 1-1.5
    
**提示：** 如果服务器监听的不是默认端口:3240，可使用参数指定端口 `--tcp-port _端口号_`.

###  取消绑定设备

只有在客户端上断开设备后才能取消绑定 

在客户端上查看已映射的USB端口: 
    
    $ usbip port
    
在客户端上断开某个已连接的USB端口: 
    
    $ usbip detach --port=_端口号_
    
在服务端上取消绑定USB设备r: 
    
    $ usbip unbind --busid=_busid_
    
##  提示和技巧

###  通过厂商/设备ID进行绑定

如果总线ID(busid)在每次系统重启后都不一样，则可以使用 厂商/设备ID 进行绑定，在服务端将下面配置文件配置保存到系统中： 
    
    /etc/systemd/system/usbip-bind@.service
    
    [Unit]
    Description=USB-IP Binding device id %I
    After=network-online.target usbipd.service
    Wants=network-online.target
    Requires=usbipd.service
    
    [Service]
    Type=simple
    ExecStart=/bin/sh -c "/usr/sbin/usbip bind --$(/usr/sbin/usbip list -p -l | grep '#usbid=%i#' | cut '-d#' -f1)"
    RemainAfterExit=yes
    ExecStop=/bin/sh -c "/usr/sbin/usbip unbind --$(/usr/sbin/usbip list -p -l | grep '#usbid=%i#' | cut '-d#' -f1)"
    Restart=on-failure
     
    [Install]
    WantedBy=multi-user.target

下面示例是将配置是将厂商/设备ID为 _0924:3d68_ 设置开机自动绑定， 
    
    # systemctl start --now usbip-bind@_0924:3d68_.service
    
**注意：** 如果系统上存在多个同一个厂商同类型设备，即多个 `vendor:product` ID 重复的设备将无法正常工作。

在客户端的配置如下所示: 

  * Linux客户端

    $ usbip attach -r _服务端IP_ --$(usbip list -p -r _服务端IP_ | grep '#usbid=0924:3d68#' | cut -d# -f1)
    
**注意：** 如果上面命令执行失败, 使用 _-p_ 参数测试是否正常，如： `usbip list -p -r _服务端IP_`，如果不正常请改用下面命令: 
    
    $ usbip attach -r _服务端IP_ -b $(usbip list -p -r _服务端IP_ | grep '0924:3d68' | cut '-d:' -f1 | awk '{print $1}')
    
  * Windows客户端

    c:\> for /f "tokens=1 delims=:, " %a in ('usbip list -r _服务端IP_ ^| findstr /r /c:"0924:3d68"') do start usbip attach -r _服务端IP_ -b %a
    
###  将配置存放至 /etc/..

[usbip-systemd](<https://aur.archlinux.org/packages/usbip-systemd/>)AUR 提供 systemd 服务文件，用于按供应商/设备 ID 进行绑定，以及按主机名和供应商/设备 ID 进行连接。 

####  服务端配置

将USB设备的`vendor/product`ID按照下面格式编写配置文件，并存放在`/etc/usbip/bind-devices/` 目录下面。 
    
    /etc/usbip/bind-devices/example-device.conf
    
    USBIP_DEVICE=0924:3d68

之后使用下命令启用服务： 
    
    # systemctl enable --now usbip-bind@example-device.service
    
####  客户端配置

将服务端USB设备的`vendor/product`ID按照下面格式编写配置文件，并存放在`/etc/usbip/remote-devices/` 目录下面。 
    
    /etc/usbip/remote-devices/example-device.conf
    
    USBIP_HOST=_example-host_
    USBIP_DEVICE=0924:3d68

确保服务端守护进程正在运行并且配置的设备已绑定, 然后下面命令启用服务： 
    
    # systemctl enable --now usbip@_example-device_.service
    
##  参见

  * [USB-IP项目官方网站](<https://usbip.sourceforge.net/>)
  * [Linux Kernel中 "usbip-utils自述"](<https://www.kernel.org/doc/readme/tools-usb-usbip-README>)
  * ["如何使用USB/IP"](<https://developer.ridgerun.com/wiki/index.php?title=How_to_setup_and_use_USB/IP>)
  * ["Windows版本的USB/IP"](<https://github.com/cezanne/usbip-win>)
  * [usbip(8)](<https://man.archlinux.org/man/usbip.8>)
  * [usbipd(8)](<https://man.archlinux.org/man/usbipd.8>)
