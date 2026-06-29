**翻译状态：**

  * 本文（或部分内容）译自 [ConnMan](<https://wiki.archlinux.org/title/ConnMan> "arch:ConnMan")，最近一次同步于 2021-03-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/ConnMan?diff=0&oldid=722527>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ConnMan_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Network configuration](<../zh-cn/Network_configuration.html> "Network configuration")
  * [Wireless network configuration](<../zh-cn/Wireless_network_configuration.html> "Wireless network configuration")

[ConnMan](<https://web.archive.org/web/20210224075615/https://01.org/connman>) 是一个命令行网络管理器，为嵌入式设备和快速响应设计。ConnMan 通过[插件](<https://git.kernel.org/cgit/network/connman/connman.git/tree/plugins>)扩展，但内置了 [DHCP](<https://en.wikipedia.org/wiki/DHCP> "wikipedia:DHCP") 与 [NTP](<../zh-cn/Category:NTP.html> "NTP") 支持。[[1]](<https://git.kernel.org/cgit/network/connman/connman.git/tree/src/>)

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [connman](<https://archlinux.org/packages/?name=connman>)包 软件包。 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包、[bluez](<https://archlinux.org/packages/?name=bluez>)包 与 [openvpn](<https://archlinux.org/packages/?name=openvpn>)包 是对应 Wi-Fi、蓝牙与 VPN 功能的可选依赖。 

在[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enabling") `connman.service` 之前，确保禁用所有已安装的[网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")。 

ConnMan 自带 [connmanctl(1)](<https://man.archlinux.org/man/connmanctl.1>) 命令行界面。各种 [#前端](<#%E5%89%8D%E7%AB%AF>)也可以使用。 

###  前端

  * **cmst** — ConnMan 的 QT GUI。

     <https://github.com/andrew-bibb/cmst> || [cmst](<https://aur.archlinux.org/packages/cmst/>)AUR

  * **connman-ncurses** — ConnMan 的简单 ncurses UI；没有实现 ConnMan 的全部功能，但是可以用（有没有 X 都可以运行），参考 [wiki](<https://github.com/eurogiciel-oss/connman-json-client/wiki>)。

     <https://github.com/eurogiciel-oss/connman-json-client> || [connman-ncurses-git](<https://aur.archlinux.org/packages/connman-ncurses-git/>)AUR

  * **ConnMan-UI** — GTK3 客户端托盘程序。

     <https://github.com/tbursztyka/connman-ui> || [connman-ui-git](<https://aur.archlinux.org/packages/connman-ui-git/>)AUR

  * **connman_dmenu** — dmenu 客户端/前端。

     <https://github.com/taylorchu/connman_dmenu> || [connman_dmenu-git](<https://aur.archlinux.org/packages/connman_dmenu-git/>)AUR

  * **Econnman** — Enlightenment 桌面托盘程序。

     <https://www.enlightenment.org> || [econnman](<https://aur.archlinux.org/packages/econnman/>)AUR

  * **LXQt-Connman-Applet** — LXQt 桌面托盘程序。

     <https://github.com/lxqt/lxqt-connman-applet> || [lxqt-connman-applet](<https://aur.archlinux.org/packages/lxqt-connman-applet/>)AUR

  * **connman-gtk** — GTK 客户端。

     <https://github.com/jgke/connman-gtk> || [connman-gtk](<https://aur.archlinux.org/packages/connman-gtk/>)AUR

  * **gnome-extension-connman** — ConnMan 的 Gnome3 扩展；如果不安装 connman-gtk，提供的功能很少。

     <https://github.com/jgke/gnome-extension-connman> || <https://extensions.gnome.org/extension/981/connman-extension/>

##  用法

ConnMan 自带 `connmanctl` 命令行界面，参考 [connmanctl(1)](<https://man.archlinux.org/man/connmanctl.1>)。 如果你不提供任何命令，直接运行 `connmanctl`，将会启动一个交互式终端。 

_ConnMan_ 会自动处理有线连接。 

### Wi-Fi

####  启用与禁用 wifi

执行 `connmanctl technologies` 来检查 wifi 是否开启，查看类似 `Powered: True/False` 的输出。 执行 `connmanctl enable wifi` 来开启 wifi，或者执行 `connmanctl disable wifi` 来禁用 wifi。 其他启用 wifi 的方法包括使用笔记本电脑上的 `Fn` 键，或者执行 `ip link set <interface> up`。 

####  连接到公开的接入点

`connmanctl` 接受简单的 _technologies_ 名称来扫描网络，要扫描附近的 Wi-Fi 网络： 
    
    $ connmanctl scan wifi
    
在扫描之后，列出可用的网络（示例输出）： 
    
    $ connmanctl services
    
    *AO MyNetwork               wifi_dc85de828967_68756773616d_managed_psk
        OtherNET                wifi_dc85de828967_38303944616e69656c73_managed_psk 
        AnotherOne              wifi_dc85de828967_3257495245363836_managed_wep
        FourthNetwork           wifi_dc85de828967_4d7572706879_managed_wep
        AnOpenNetwork           wifi_dc85de828967_4d6568657272696e_managed_none
    
要连接到公开的网络，使用以 `wifi_` 开头的第二个参数: 
    
    $ connmanctl connect wifi_dc85de828967_4d6568657272696e_managed_none
    
**提示：** 网络名称可以用 tab 补全。

你现在应该已经连上网络了，使用 `connmanctl state` 或 `ip addr` 来检查。 

####  连接到受保护的接入点

你需要提供更多的信息，起码是密码或者密码短语，给 ConnMan 守护程序来连接受保护的接入点。 

这一节的命令展示了如何在交互模式执行 `connmanctl`，只有交互模式下才能使用 `agent` 命令。要开启交互模式，只需要输入： 
    
    $ connmanctl
    
接下来的操作和之前的类似，首先扫描所有的 Wi-Fi _technologies_ ： 
    
    connmanctl> scan wifi
    
列出服务： 
    
    connmanctl> services
    
现在你需要注册一个 agent 来处理用户请求，命令是： 
    
    connmanctl> agent on
    
现在连接到受收保护的服务，使用 tab 补全来输入 wifi_ 服务，比如要连接到上面例子中的 OtherNET， 输入： 
    
    connmanctl> connect wifi_dc85de828967_38303944616e69656c73_managed_psk
    
Agent 会向你询问守护进程连接到网路需要的一切信息，这些信息会依据与你要连接的网络类型的不同而变化。 Agent 也会像下面一样显示有关信息的额外数据： 
    
    Agent RequestInput wifi_dc85de828967_38303944616e69656c73_managed_psk
      Passphrase = [ Type=psk, Requirement=mandatory ]
      Passphrase?  
    
提供要求的信息，在这个例子里是密码短语，然后输入： 
    
    connmanctl> quit
    
如果你提供的信息正确，那么你应该已经连接到受保护的接入点了。 

####  使用 iwd 代替 wpa_supplicant

ConnMan 可以使用 [iwd](<https://archlinux.org/packages/?name=iwd>)包 连接无线网络。Community 中提供的的软件包已经支持使用 [iwd](<https://archlinux.org/packages/?name=iwd>)包 来连接无线网络。因为只要 [connman](<https://archlinux.org/packages/?name=connman>)包 找到 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 就会启动它，这里建议卸载 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包。 

目前 [iwd](<https://archlinux.org/packages/?name=iwd>)包 的 `-i` 选项似乎会导致 [connman](<https://archlinux.org/packages/?name=connman>)包 无法找到 Wi-Fi 接口。 

创建下面两个服务文件，可以让 [connman](<https://archlinux.org/packages/?name=connman>)包 无论是否安装了[wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包，都一律使用 [iwd](<https://archlinux.org/packages/?name=iwd>)包 来连接无线网络。 
    
    /etc/systemd/system/iwd.service
    
    [Unit]
    Description=Internet Wireless Daemon (IWD)
    Before=network.target
    Wants=network.target
    
    [Service]
    ExecStart=/usr/lib/iwd/iwd
    
    [Install]
    Alias=multi-user.target.wants/iwd.service
    
    /etc/systemd/system/connman_iwd.service
    
    [Unit]
    Description=Connection service
    DefaultDependencies=false
    Conflicts=shutdown.target
    RequiresMountsFor=/var/lib/connman
    After=dbus.service network-pre.target systemd-sysusers.service iwd.service
    Before=network.target multi-user.target shutdown.target
    Wants=network.target
    Requires=iwd.service
    
    [Service]
    Type=dbus
    BusName=net.connman
    Restart=on-failure
    ExecStart=/usr/bin/connmand --wifi=iwd_agent -n 
    StandardOutput=null
    CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE CAP_NET_RAW CAP_SYS_TIME CAP_SYS_MODULE
    ProtectHome=true
    ProtectSystem=true
    
    [Install]
    WantedBy=multi-user.target

然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")/[开始](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `connman_iwd` 服务。 

使用 [iwd](<https://archlinux.org/packages/?name=iwd>)包 代替 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 的好处是：ping 时间似乎会更加一致，并且连接会更加可靠。 

###  设置

对于用户经常连接的网络，ConnMan 会自动创建设置与配置文件。这些文件包括了密码短语、essid 和其他信息。配置文件存放在 `/var/lib/connman/` 内，以服务为名的文件夹下。要查看所有的网络配置文件，在 [root shell](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Regular_user_or_root> "Help:Reading") 内执行： 
    
    # cat /var/lib/connman/*/settings
    
**注意：** VPN 设置存放在 `/var/lib/connman-vpn/`。

### Technologies

ConnMan 将各种硬件接口称为 _Technologies_ 。 

要列出所有可用的 _Technologies_ ，执行： 
    
    $ connmanctl technologies
    
只列出 _Technologies_ 类型的名字，可以使用这一行命令： 
    
    $ connmanctl technologies | awk '/Type/ { print $NF }'
    
**注意：** 字段 `Type = tech_name` 里的“tech_name”，就是 `connmanctl` 命令所使用的 technology 类型

要与这些接口交互，必须使用 technology 的类型。要开启或关闭 _Technologies_ 可以用： 
    
    $ connmanctl enable _technology_type_
    
与： 
    
    $ connmanctl disable _technology_type_
    
比如要关闭 wifi： 
    
    $ connmanctl disable wifi
    
**警告：** connman 会监听 rfkill 事件。使用 connman 时，尽管硬件锁可能可以正常工作，但基本无法使用 `rfkill` 或 `bluetoothctl` 来开关设备。 [[2]](<https://git.kernel.org/cgit/network/connman/connman.git/tree/doc/overview-api.txt#n406>) 请使用 `connmanctl enable|disable`

##  提示与技巧

###  避免改变 hostname

ConnMan 默认会更改临时 hostname。与 X authority 一起使用时会有问题：如果用旧的 hostname 生成了 xauth magic coookie 之后，ConnMan 改变了你的 hostname，那么将无法创建新的窗口，会显示诸如 `No protocol specified` 和 `Can't open display: :0.0` 的错误。手动重置 hostname 可以解决这个问题，但根本的解决办法是从一开始就防止 ConnMan 改变你的 hostname。把下面的配置加入 `/etc/connman/main.conf` 即可： 
    
    [General]
    AllowHostnameUpdates=false
    
改变这个文件后记得[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `connman.service`。 

要测试的话，建议一边观察 [systemd 日志](</wzh/index.php?title=Systemd_journal&action=edit&redlink=1> "Systemd journal（页面不存在）")，一边插拔几次网线接口。 

###  有线网络与无线网络共存时，优先使用有线网络

ConnMan 默认不会优先使用有线网络，这会导致 ConnMan 即使在可以使用有线网络时，也只使用慢速的无线网络。你可以将下面的配置加入 `/etc/connman/main.conf`，让 ConnMan 优先使用有线网络。 
    
    [General]
    PreferredTechnologies=ethernet,wifi
    
###  互斥连接

ConnMan 允许你同时连接有线与无线网络。这样允许程序在通过 wifi 建立了连接后，再连接到有线网络，通过 wifi 建立的连接也不会中断。但有些人更喜欢同一时间只使用一种网络，将下面的配置加入 `/etc/connman/main.conf` 可以实现这一点： 
    
    [General]
    SingleConnectedTechnology=true
    
###  连接到 eduroam (802.1X)

在[连接](<#Wi-Fi>)到诸如 eduroam 的 [WPA2 企业模式](</wzh/index.php?title=WPA2_Enterprise&action=edit&redlink=1> "WPA2 Enterprise（页面不存在）")网络之前，需要建立单独的配置文件。 比如，创建 `/var/lib/connman/eduroam.config`： 
    
    eduroam.config
    
    [service_eduroam]
    Type=wifi
    Name=eduroam
    EAP=peap
    CACertFile=/etc/ssl/certs/_certificate.cer_
    Phase2=_MSCHAPV2_
    Identity=_user@foo.edu_
    AnonymousIdentity=_anonymous@foo.edu_
    Passphrase=_password_

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `wpa_supplicant.service` 和 `connman.service` 来连接到新网络上。 

**注意：**

  * 选项是大小写敏感的，比如应该用 `EAP = ttls` 而不是 `EAP = TTLS`。[[3]](<https://together.jolla.com/question/55969/connman-fails-due-to-case-sensitive-settings/>)
  * 请向提供 eduroam 网络的机构咨询各种设置，比如用户名、密码、`EAP`、`Phase2output`和需要的凭证。

更多信息请参考 [connman-service.config(5)](<https://man.archlinux.org/man/connman-service.config.5>) 和 [Wireless network configuration#eduroam](<../zh-cn/Wireless_network_configuration.html#eduroam> "Wireless network configuration"). 

###  避免与本地 DNS 服务冲突

如果你在运行本地的 DNS 服务，在安装了 ConnMan 之后，你很可能会遇到 53 端口（TCP 和/或 UDP）被占用的问题。这是因为 ConnMan 内置的 DNS 代理也会尝试绑定 53 端口。如果你看到了来自 [BIND](<../zh-cn/BIND.html> "BIND") 或 [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq") 的日志诸如： 
    
    named[529]: could not listen on UDP socket: address in use
    
就是这个问题引起的。要确认是哪个应用占用了 53 端口，可以以 root 身份执行 `ss -tulpn`。 

要修复这个问题，可以[修改](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd") systemd 服务文件，以 `-r` 或 `--nodnsproxy` 选项启动 connmand。 创建文件夹 `/etc/systemd/system/connman.service.d/` 并新增文件 `disable_dns_proxy.conf`： 
    
    /etc/systemd/system/connman.service.d/disable_dns_proxy.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/connmand -n --nodnsproxy

确保在新增此文件后 [reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") systemd 守护程序，并 [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `connman.service` 和你的 DNS 代理。 

###  /etc/resolv.conf

如果你既想知道从 DHCP 获得的 DNS 服务器地址，同时又想保留自定义的 `/etc/resolv.conf`，那么就在上面的文件里追加 `RuntimeDirectory=connman`（如果不需要 `ExecStart` ，就去掉 ExecStart 行）。这样 connman 就会把从 DHCP 获得的 DNS 服务器地址写入 `/var/run/connman/resolv.conf`。 

记得在增加这个文件之后[重载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") systemd 守护程序，并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `connman.service`和你的 DNS 代理。 

###  屏蔽接口

如果有 [Docker](<../zh-cn/Docker.html> "Docker") 之类的的程序创建了虚拟接口，当网络连接中断时，ConnMan 可能会尝试连接这些虚拟接口，而不是真实的硬件接口。简单的解决办法是将你不想要 ConnMan 连接的接口加入黑名单。 ConnMan 默认会屏蔽以 `vmnet`、`vboxnet`、`virbr` 与 `ifb` 开头的接口，所以配置新的黑名单时也要加入这些接口。 

屏蔽接口还可以避免竞态条件：在 systemd/udev 改变接口名称到形如 `enp4s0` 的[可预测的网络接口名称](<https://systemd.io/PREDICTABLE_INTERFACE_NAMES/>)之前，connman 可能就会去连接接口。屏蔽惯用（且不可预测）的接口前缀可以让 connman 在接口重命名之后再连接。 

把下面的配置加入 `/etc/connman/main.conf`（如果不存在就创建这个文件）： 
    
    [General]
    NetworkInterfaceBlacklist=vmnet,vboxnet,virbr,ifb,docker,veth,eth,wlan
    
[重启](<../zh-cn/Systemd.html#Using_units> "Systemd") `connman.service` 之后，在 Econnman 这样的 GUI 工具中，所有形如 `veth#######` 的接口也都会被隐藏。 

##  疑难杂症

###  Error /net/connman/technology/wifi: Not supported

目前，connman 不支持用 [iwd](<https://archlinux.org/packages/?name=iwd>)包 扫描 Wi-Fi 网络，这个功能暂时只能由 `wpa_supplicant` 提供（参考 [[4]](<https://lists.01.org/pipermail/connman/2018-August/022915.html>)）。要用 iwd连接 wifi，[enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 并 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `iwd.service`，然后参考 [Iwd](<../zh-cn/Iwd.html> "Iwd") 中的指示，或者使用[#前端](<#%E5%89%8D%E7%AB%AF>)的其中之一。为了让 connman 能扫描 Wi-Fi，安装 [wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 软件包，并在停用 `iwd.service` 之后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")`connman.service`。 

###  Error /net/connman/technology/wifi: No carrier

在你使用这条命令启用 wifi 后： 
    
    $ connmanctl enable wifi
    
如果扫描无线网络时产生了这条错误，这可能是因为一个未解决的 Bug。[[5]](<https://01.org/jira/browse/CM-670>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] 如果在满足了[这些条件](<https://lists.01.org/pipermail/connman/2014-December/019203.html>)后还未解决，请在禁用其他网络管理器，并重启系统之后再尝试。 

也可能仅仅是因为无线接口被 [rfkill](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Rfkill_%E8%AF%B4%E6%98%8E> "Rfkill") 关闭了，重启 wpa_supplicant 时有可能会这样。使用 `rfkill list` 来检查。 

###  "Not registered", or "Method "Connect" with signature ... doesn't exist"

在执行命令时你可能会看到这样的错误： 

来自 `connmanctl` 提示符： 
    
    connmanctl> connect _service_id_
    
    Error /net/connman/service/_SSID_ : Method "Connect" with signature "" on interface "net.connman.Service" doesn't exist
    
来自终端： 
    
    # connmanctl connect _service_id_
    
    Error /net/connman/service/_service_id_ : Not registered
    
这些错误是由于没有运行 agent。在 `connmanctl` 提示符里执行 `agent on` 来启动 agent，然后再试一试。 

###  Error Failed to set hostname/domainname

Connman 可能会因没有 `CAP_SYS_ADMIN` 而无法设置 hostanme 或 domainname。 

你需要[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `connman.service`（以及其他类似的文件，如 `connman-vpn.service`）来修改 `CapabilityBoundingSet` 行，增加 `CAP_SYS_ADMIN`。 

更多细节请参考 `EPERM` 下的 [sethostname(2) § ERRORS](<https://man.archlinux.org/man/sethostname.2#ERRORS>) 或 [setdomainname(2) § ERRORS](<https://man.archlinux.org/man/setdomainname.2#ERRORS>)。 

###  连接时出现未知路由

每次连接完成后，日志中可能出现未知的路由，比如： 
    
    ...
    connmand[473]: wlp2s0 {add} route 82.165.8.211 gw 10.20.30.4 scope 0 <UNIVERSE>
    connmand[473]: wlp2s0 {del} route 82.165.8.211 gw 10.20.30.4 scope 0 <UNIVERSE>
    ...
    
这可能是由于 ConnMan 在通过检查与 ipv4.connman.net 的连接，来测试网络（在本例里，`82.165.8.211` 就是 ipv4.connman.net 被解析后的 IP地址）。[[6]](<https://01.org/jira/browse/CM-657>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ] 详细信息，包括 ConnMan 为什么要这么做，以及 ConnMan 除了连接 IP 还传递了什么信息，请参考 [ConnMan README](<https://git.kernel.org/pub/scm/network/connman/connman.git/tree/README#n388>)。 

该行为可以通过在 `/etc/connman/main.conf` 中增加下面的配置来阻止： 
    
    [General]
    EnableOnlineCheck=false
    
这项配置也会导致默认设备状态不会从 READY 切换到 ONLINE。[connman.conf(5)](<https://man.archlinux.org/man/connman.conf.5>) 但网络连接是正常的。 

也可以用防火墙规则阻止连接检查，这不会影响正常的网络连接（除非有 captive portal）： 
    
    # ip6tables -A OUTPUT -d ipv6.connman.net -j REJECT
    # iptables -A OUTPUT -d ipv4.connman.net,ipv6.connman.net -j REJECT
    
###  File /proc/net/pnp doesn't exist

如果你在错误日志中看到了这个，这是由 connman 的 bug 引起的 [[7]](<https://bbs.archlinux.org/viewtopic.php?id=227689#p1766928>)，可以无视。[Bug Report](<https://01.org/jira/browse/CM-690>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]

##  另请参见

  * [Git 仓库文档](<https://git.kernel.org/cgit/network/connman/connman.git/tree/doc>)——更多细节文档
