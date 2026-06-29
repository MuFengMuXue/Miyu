**翻译状态：**

  * 本文（或部分内容）译自 [iwd](<https://wiki.archlinux.org/title/iwd> "arch:iwd")，最近一次同步于 2025-07-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/iwd?diff=0&oldid=838163>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/iwd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Network configuration](<../zh-cn/Network_configuration.html> "Network configuration")
  * [Wireless network configuration](<../zh-cn/Wireless_network_configuration.html> "Wireless network configuration")
  * [wpa_supplicant](<../zh-cn/Wpa_supplicant.html> "Wpa supplicant")

[iwd](<https://iwd.wiki.kernel.org/>) (iNet wireless daemon，iNet 无线守护程序) 是由英特尔（Intel）为 Linux 编写的一个无线网络守护程序。该项目的核心目标是不依赖任何外部库，而是最大程度地利用 Linux 内核提供的功能来优化资源利用。 

iwd 可以独立工作，也可以和 [ConnMan](<../zh-cn/ConnMan.html> "ConnMan")、[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 和 [NetworkManager](<../zh-cn/NetworkManager.html#%E5%B0%86_iwd_%E4%BD%9C%E4%B8%BA_Wi-Fi_%E5%90%8E%E7%AB%AF> "NetworkManager") 这样更完善的网络管理器结合使用。 

**注意：** 当通过 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 使用 iwd 时，除非 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 的文章中另有说明，否则请不要按照本页上的说明操作。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [iwd](<https://archlinux.org/packages/?name=iwd>)包 软件包。 

也可选择安装第三方包，其提供图形化与终端用户界面： 

  * **impala** — 一个用于 iwd 的终端用户界面（TUI）。

     <https://github.com/pythops/impala> || [impala](<https://archlinux.org/packages/?name=impala>)包

  * **iwdgui** — iwd 的图形界面前端。

     <https://gitlab.com/hfernh/iwdgui> || [iwdgui](<https://aur.archlinux.org/packages/iwdgui/>)AUR

  * **iwgtk** — iwd 的图形界面前端及指示器（托盘）图标。

     <https://github.com/J-Lentz/iwgtk> || [iwgtk](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/iwgtk>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")

  * **iwmenu** — iwd 的菜单驱动界面。

     <https://github.com/e-tho/iwmenu> || [iwmenu-git](<https://aur.archlinux.org/packages/iwmenu-git/>)AUR

##  使用方法

[iwd](<https://archlinux.org/packages/?name=iwd>)包 软件包提供了客户端程序 `iwctl`、守护程序 `iwd` 和 WiFi 监控工具 `iwmon`。 

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `iwd.service` 以便可以使用 `iwctl` 或 `iwgtk` 对其进行控制。 

**注意：** 仅允许root、`network` 或 `wheel` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组") 的成员与 _iwd_ 交互。为了使用 _iwctl_ 或 _iwgtk_ ，您需要 [ 将您的用户添加到其中一个组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户和用户组").

### iwctl

要进入交互式提示符（interactive prompt），执行： 
    
    $ iwctl
    
然后交互式提示符就会以 `[iwd]#` 前缀显示出来了。 

**提示：**

  * 在 `iwctl` 提示符中，可以通过 `Tab` 键自动补全命令和设备名称。
  * 要退出交互式提示，按下 `Ctrl+d` 发送 [EOF](<https://en.wikipedia.org/wiki/EOF_character> "wikipedia:EOF character") 信号。
  * 可以在不进入交互式提示符的情况下，将所有命令当作命令行参数使用。例如：`iwctl device wlan0 show`。

要列出所有可用的命令： 
    
    [iwd]# help
    
####  连接网络

首先，使用 [rfkill](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Rfkill_%E8%AF%B4%E6%98%8E> "Rfkill") 命令确认 Wi-Fi 设备未被屏蔽。 

如果不知道你的网络设备名称，请列出所有 WiFi 设备： 
    
    [iwd]# device list
    
如果设备或其相应的适配器已关闭，请将其打开。 
    
    [iwd]# device _name_ set-property Powered on
    
    [iwd]# adapter _adapter_ set-property Powered on
    
然后，要开始扫描网络（注意：这个命令不会输出任何内容），执行： 
    
    [iwd]# station _name_ scan
    
再然后，就可以列出所有可用的网络： 
    
    [iwd]# station _name_ get-networks
    
最后，要连接到一个网络： 
    
    [iwd]# station _name_ connect _SSID_
    
**注意：** * 对于通过 DHCP 的 IP 和 DNS 自动配置，您需要 [手动启用](<#%E5%90%AF%E7%94%A8%E5%86%85%E7%BD%AE%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE>) 内置 DHCP 客户端，或配置一个 [独立 DHCP 客户端](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%99%A8> "网络配置")。

**提示：** 用户界面支持自动补全，输入 `station ` 后按压 `Tab` `Tab`，将显示可用的设备，键入设备的首字母和 `Tab` 将自动补全。同样，输入 `connect ` 和 `Tab` `Tab` 以显示可用网络列表。然后，键入所选网络的首字母，后跟 `Tab`，以自动补全。

当网络密码尚未储存在 iwd 自动检查的任何设定档中时，系统会提示使用者输入密码，而连线操作也可以透过命令列参数的方式来指定： 
    
    $ iwctl --passphrase _passphrase_ station _name_ connect _SSID_
    
**注意：**

  * `iwd` 会自动将网络密码存储在 `/var/lib/iwd` 目录中，以后就可以使用其自动连接记住的网络。参见 [#网络配置](<#%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE>) 一节。
  * 要连接 SSID 里带空格的网络，连接时请用双引号将网络名称括起来。(或用转义符代替空格（"\ "）)
  * iwd 仅支持 8 到 63 位 ASCII 编码字符组成的 PSK 密码。如果没有满足要求，会出现下列错误信息：`PMK generation failed. Ensure Crypto Engine is properly configured`。

####  使用 WPS/WSC 连接网络

如果网络配置为可以通过按下一个按钮就能进行连接 ([Wikipedia:Wi-Fi Protected Setup](<https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup> "wikipedia:Wi-Fi Protected Setup")，WPS，WiFi 保护配置)，先检查设备是否能兼容以下配置步骤： 
    
    [iwd]# wsc list
    
然后，假设设备出现在了上面的列表中： 
    
    [iwd]# wsc _device_ push-button
    
接着按下路由器上的按钮。如果提前按下按钮，但只要少于两分钟前，以上步骤也是可以生效的。 

如果网络要求验证 PIN 码才能连接，请检查 `help` 命令的输出，了解如何为 `wsc` 命令提供正确的选项。 

####  断开网络连接

要断开网络连接： 
    
    [iwd]# station _device_ disconnect
    
####  显示设备和连接信息

要显示 WiFi 设备详细情况，比如 MAC 地址： 
    
    [iwd]# device _device_ show
    
要显示包括 WiFi 设备的连接网络在内的连接状态： 
    
    [iwd]# station _device_ show
    
####  管理已知网络

要列出以前连接过的网络： 
    
    [iwd]# known-networks list
    
要忘记已知的网络： 
    
    [iwd]# known-networks _SSID_ forget
    
### iwgtk

另外，[iwgtk](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/iwgtk>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 提供了一个 GUI 前端，也通过它可以控制 iwd。 

不加任何参数运行 `iwgtk` 将启动一个 iwd 的管理窗口，它能被用于切换适配器的开关、更改操作模式、查看或链接可用的无线网络、管理已保存的网络。 

####  托盘图标

要启动 iwgtk 的托盘图标请运行： 
    
    $ iwgtk -i
    
如果托盘中的图标没有出现，则你的系统托盘很可能不支持 StatusNotifierItem API，这种情况下你需要使用一个兼容层（例如[snixembed-git](<https://aur.archlinux.org/packages/snixembed-git/>)AUR）。 下面的系统托盘支持 StatusNotifierItem API，因此无需兼容层： 

  * KDE Plasma
  * swaybar
  * xfce4-panel

下面的托盘只支持 XEmbed 因此需要[snixembed-git](<https://aur.archlinux.org/packages/snixembed-git/>)AUR： 

  * AwesomeWM
  * i3bar

####  自启动

每次登录桌面时自启动 iwgtk 的托盘图标是常见的用法。如果你的桌面环境支持 [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart") 标准，则 iwgtk 托盘图标的自启动无需额外配置，因为 [iwgtk](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/iwgtk>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 将 `iwgtk-indicator.desktop` 文件放置在了 `/etc/xdg/autostart/`。 作为上面的方法的替代， [iwgtk](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/iwgtk>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")提供了一个用来自启动托盘进程的 systemd 单元文件.如果你的桌面环境支持 systemd 的 `graphical-session.target` 单元, 则 iwgtk 能在 [Systemd#使用单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")了 `iwgtk.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")后被 systemd 自动启动。 

##  网络配置

iwd 默认在 `/var/lib/iwd` 目录下储存网络配置。配置文件名形如 `_网络_._类别_`，其中网络是该网络的 SSID，类别是网络类别，是 _.open_ , _.psk_ , _.8021x 之一。_ 文件储存加密的 `PreSharedKey` 和可选的 cleartext `Passphrase`，可以不调用 `iwctl` 由用户创建。该文件亦可用作隶属该网络 SSID 的其他配置。参见 [iwd.network(5)](<https://man.archlinux.org/man/iwd.network.5>) 获得更详尽的设置。 

**注意：** 在字符串值中，包括身份和密码，特定字符被反斜杠转义。开头的空格，\n，\r 以及反斜杠必须转义表达。参见 [iwd.network(5)](<https://man.archlinux.org/man/iwd.network.5>)。

### WPA-PSK

一个连接到 WPA-PSK 或 WPA2-PSK 安全网络的最小示例文件，其 SSID "spaceship"，Passphrase "test1234"： 
    
    /var/lib/iwd/spaceship.psk
    
    [Security]
    PreSharedKey=aafb192ce2da24d8c7805c956136f45dd612103f086034c402ed266355297295

**注意：** 网络的 SSID 仅当其仅包含字母，数字或 `- _` 两字符之一时作为文件名。如果其包含其他字符，文件名将替代为`=`字符后SSID的十六进制编码（十六进制数使用小写字母）。

下列两种方法可以根据 passphrase 计算 pre-shared key： 

  * 在配置文件的 cleartext 输入 passphrase：

    /var/lib/iwd/spaceship.psk
    
    [Security]
    Passphrase=test1234

pre-shared key 会在第一次连接时自动追加到文件末尾：
    
    /var/lib/iwd/spaceship.psk
    
    [Security]
    Passphrase=test1234
    PreSharedKey=aafb192ce2da24d8c7805c956136f45dd612103f086034c402ed266355297295

  * 亦可使用 _wpa_passphrase_ （自[wpa_supplicant](<https://archlinux.org/packages/?name=wpa_supplicant>)包 或 [wpa-psk](<https://aur.archlinux.org/packages/wpa-psk/>)AUR），用 SSID 与 passphrase 计算 pre-shared key。
  * 参见 [wpa_supplicant#Connecting with wpa_passphrase](<../zh-cn/Wpa_supplicant.html#Connecting_with_wpa_passphrase> "Wpa supplicant") 获得更多细节。

### WPA Enterprise

#### EAP-PWD

为了连接到受 EAP-PWD 保护的企业（无线）访问接入点 (Access Point, AP)，需要在 `/var/lib/iwd` 文件夹中创建一个 `_essid_.8021x` 格式的文件，并包含以下内容： 
    
    /var/lib/iwd/_essid_.8021x
    
    [Security]
    EAP-Method=PWD
    EAP-Identity=_your_enterprise_email_
    EAP-Password=_your_password_
    
    [Settings]
    AutoConnect=true

如果不想自动连接到 AP，可以将相应选项设定为 False 并手动通过 `iwctl` 连接网络。密码同理，如果不想让密码以明文保存，则将相应选项从文件中删去，直接连接企业 AP。 

**注意：** 无法更改不同 SSID 的优先级，您可能需要设置 `AutoConnect=false` 作为变通方法。

#### EAP-PEAP

和 EAP-PWD 一样，同样需要在同一文件夹中创建一个 `_essid_.8021x` 格式的文件。在继续编写配置文件之前，不妨了解一下自己所属组织所使用的 CA 证书。下面是一个使用 MSCHAPv2 密码认证的示例配置文件： 
    
    /var/lib/iwd/_essid_.8021x
    
    [Security]
    EAP-Method=PEAP
    EAP-Identity=anonymous@realm.edu
    EAP-PEAP-CACert=/path/to/root.crt
    EAP-PEAP-ServerDomainMask=radius.realm.edu
    EAP-PEAP-Phase2-Method=MSCHAPV2
    EAP-PEAP-Phase2-Identity=johndoe@realm.edu
    EAP-PEAP-Phase2-Password=hunter2
    
    [Settings]
    AutoConnect=true

MsCHAPv2 密码亦可被存为一个加密的哈希值。正确的 md4 值可这样计算： 
    
    $ iconv -t utf16le | openssl md4 -provider legacy
    
在输完密码后，按下 `Ctrl+d`以输入 EOF，不要按 `Enter`。结果哈希值应储存在 `EAP-PEAP-Phase2-Password-Hash` 值。 

**注意：** 如果打算使用 _eduroam_ ，另请参见 [#Eduroam](<#Eduroam>)。

#### TTLS-PAP

和 EAP-PWD 一样，同样需要在同一文件夹中创建一个 `_essid_.8021x` 格式的文件。在继续编写配置文件之前，不妨了解一下自己所属组织所使用的 CA 证书。下面是一个使用 PAP 密码认证的示例配置文件： 
    
    /var/lib/iwd/_essid_.8021x
    
    [Security]
    EAP-Method=TTLS
    EAP-Identity=anonymous@uni-test.de
    EAP-TTLS-CACert=cert.pem
    EAP-TTLS-ServerDomainMask=*.uni-test.de
    EAP-TTLS-Phase2-Method=Tunneled-PAP
    EAP-TTLS-Phase2-Identity=user
    EAP-TTLS-Phase2-Password=password
    
    [Settings]
    AutoConnect=true

#### EAP-TLS

EAP-TLS 使用 x509 _客户端证书_ 来确认您的身份。和 ssh 密钥一样，这些证书使用公钥加密，因此永不需要向 wifi 验证服务器发送密钥，您也无需复制和重复使用密码。通常情况下，每台设备都会使用不同的证书。理论上，至少可以在不强迫你更改密码或中断其他设备的情况下撤销证书。 

与其他企业级方法一样，您需要知道贵组织使用的 CA 证书（`cacert.pem`），该证书可以向设备证明它连接到的目标是正确的。您还需要拥有在每次连接时上传的、代表您的客户端证书（`client-cert.pem`），以及证明您拥有客户端证书的配套的私钥（`client-key.pem`）。 

当您收集好凭证，将这个放到您的 `/var/lib/iwd/_essid_.8021x` 文件： 
    
    /var/lib/iwd/_essid_.8021x
    
    [Security]
    
    EAP-Method=TLS
    EAP-TLS-CACert=/path/to/cacert.pem
    EAP-Identity=_your_enterprise_email_
    EAP-TLS-ClientCert=/path/to/client-cert.pem
    EAP-TLS-ClientKey=/path/to/client-key.pem
    #EAP-TLS-ClientKeyPassphrase=key-passphrase  #如果 client-key.pem 是加密的，请提供其密码。
    
    [Settings]
    AutoConnect=true

#### Eduroam

通过 iwd 连接 eduroam 的方法详见以下文件，并填写必要的信息： 
    
    /var/lib/iwd/eduroam.8021x
    
    [Security]
    EAP-Method=PEAP
    EAP-Identity=anonymous@_university.domain_
    EAP-PEAP-Phase2-Method=MSCHAPV2
    EAP-PEAP-Phase2-Identity=_username@university.domain_
    EAP-PEAP-Phase2-Password=_password_
    
    [Settings]
    AutoConnect=true

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** CAT 中对 iwd 的支持不可用（在 [Talk:Iwd](<../zh-cn/Talk:Iwd.html>) 中讨论）

Eduroam 提供了一个[配置助手工具 (Configuration Assistant Tool，CAT)](<https://cat.eduroam.org/>), 遗憾的是它并不支持 iwd。但是，CAT 的安装程序只是一个 Python 脚本，可以通过点击下载按钮，然后选择你的大学来下载它。可以很轻易地提取出必要的配置选项，包括证书和服务域掩码。此外，一些机构正在升级到 EAP-TLS，并将 `client-cert.pem` 的生成外包给 [SecureW2](<https://www.securew2.com/>)。这种情况下，您也需要使用他们的工具来生成客户端证书。 

下列的表格包含了 iwd 配置选项到 Eduroam CAT 安装脚本变量的映射关系： 

Iwd 配置选项 | CAT 脚本变量   
---|---  
_essid_ | 某个 `Config.ssids` 文件   
`EAP-Method` |  `Config.eap_outer`  
`EAP-Identity` |  `Config.anonymous_identity`  
`EAP-_method_ -CACert` |  `Config.CA`的内容，或者包含`Config.CA`的 _.pem_ 文件的绝对路径   
`EAP-_method_ -ServerDomainMask` |  `Config.servers` 之一   
`EAP-_method_ -Phase2-Method` | 除非 `Config.eap_inner` 等于 `PAP`，否则请使用 `Tunneled-PAP`  
`EAP-_method_ -Phase2-Identity` |  `_username_ @Config.user_realm`  
  
其中 `_method_` 是 `EAP-Method` 的内容，应为 `TLS`、`TTLS` 或 `PEAP`。 提取所有必要信息，并转换、使之与 iwd 配置等价后，就可以按照前面的方法将其放入名为 `_essid_.8021x` 的配置文件中。 

**注意：**

  * Eduroam 提供方可能不要求使用 `EAP-Identity`，在这种情况下可以在选项字段里写上 `anonymous`。
  * 若您的 `EAP-_method_ -ServerDomainMask` 以 `DNS:`开始，只使用 `DNS:` 以后的部分。

####  其他情况

更多测试范例可在上游仓库的[测试案例中找到](<https://git.kernel.org/pub/scm/network/wireless/iwd.git/tree/autotests>)。 

####  内嵌证书

除了使用 PEM 文件的绝对路径（用于证书和密钥）之外，也可以将 PEM 文件本身直接包含在网络配置文件中。 

内嵌 PEM 可以在设置文件中的任意位置出现，格式如下： 
    
    [@pem@_my_ca_cert_]
    ----- BEGIN CERTIFICATE -----
    _PEM data_
    ----- END CERTIFICATE -----
    
其中， _my_ca_cert_ 是用来在配置文件中标识该证书的任意名称。 

然后，在设置文件中任何需要证书路径的地方，都可以通过在值前加上 `embed:` 来使用内嵌证书，例如： 
    
    EAP-TTLS-CACert=embed:_my_ca_cert_
    
这不仅限于 CA 证书。客户端证书、客户端密钥（无论是否加密）以及证书链都可以包含在内。 

##  可选配置

文件 `/etc/iwd/main.conf` 用于存储主要配置。参见 [iwd.config(5)](<https://man.archlinux.org/man/iwd.config.5>)。 

###  禁用特定网络的自动连接

创建或编辑 `/var/lib/iwd/_network_._type_` 文件。在其中添加如下部分： 
    
    /var/lib/iwd/spaceship.psk (for example)
    
    [Settings]
    AutoConnect=false

###  禁用定期扫描可用网络

默认情况下，当 `iwd` 处于未连接状态时，它会定期扫描可用网络。要禁用定期扫描（以便总是手动扫描网络），创建或编辑 `/etc/iwd/main.conf` 文件并添加以下部分： 
    
    /etc/iwd/main.conf
    
    [Scan]
    DisablePeriodicScan=true

###  启用内置网络配置

自 0.19 版本起，iwd 可使用内置的 DHCP 客户端或静态配置来分配（多个）IP 地址并设置路由。它是[独立 DHCP 客户端](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E7%AE%A1%E7%90%86%E5%99%A8> "网络配置")不错的替代品。 

要激活 iwd 的网络配置功能，创建或编辑 `/etc/iwd/main.conf` 并添加以下部分： 
    
    /etc/iwd/main.conf
    
    [General]
    EnableNetworkConfiguration=true

还可以用 `RoutePriorityOffset` 设置路由指标（route metric）： 
    
    /etc/iwd/main.conf
    
    [Network]
    RoutePriorityOffset=300

####  IPv6 支持

自从 1.10 版本，iwd 支持 IPv6，但在 2.0 版本以下默认禁用。2.0 版本后默认启用。 

欲禁用之，在配置文件下添加以下内容： 
    
    /etc/iwd/main.conf
    
    [Network]
    EnableIPv6=false

要在高于 1.10 低于 2.0 版本启用它： 
    
    /etc/iwd/main.conf
    
    [Network]
    EnableIPv6=true

无论您想用 DHCPv6 还是静态 IPv6 配置，您都需要启用该设置。它也可以设置在每个网络的基础上。 

####  在网络配置中设定静态 IP 地址

将下列部分添加到 `/var/lib/iwd/_network_._type_` 文件中。例如可以这样写： 
    
    /var/lib/iwd/spaceship.psk
    
    [IPv4]
    Address=192.168.1.10
    Netmask=255.255.255.0
    Gateway=192.168.1.1
    Broadcast=192.168.1.255
    DNS=192.168.1.1

####  选择 DNS 管理器

目前，iwd 支持两种 DNS 管理器——[systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 和 [resolvconf](</wzh/index.php?title=Resolvconf&action=edit&redlink=1> "Resolvconf（页面不存在）")。 

要使用 `systemd-resolved`，将下列部分添加到 `/etc/iwd/main.conf` 中： 
    
    /etc/iwd/main.conf
    
    [Network]
    NameResolvingService=systemd

而对于 `resolvconf`，添加的为: 
    
    /etc/iwd/main.conf
    
    [Network]
    NameResolvingService=resolvconf

**注意：** 若未指定，默认使用 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")，并推荐其用于[systemd](<https://lore.kernel.org/iwd/2249097a-97e0-175a-6b02-e5d6be484498%40gmail.com/>).

###  允许任何用户读取状态信息

如果想允许任何用户读取状态信息，但不允许修改设置，请按如下所示创建一个 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 配置： 
    
    /etc/dbus-1/system.d/iwd-allow-read.conf
    
    <!-- Allow any user to read iwd status information. Overrides some part
          of /usr/share/dbus-1/system.d/iwd-dbus.conf. -->
    
    <!DOCTYPE busconfig PUBLIC "-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
     "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
    <busconfig>
    
      <policy context="default">
        <deny send_destination="net.connman.iwd"/>
        <allow send_destination="net.connman.iwd" send_interface="org.freedesktop.DBus.Properties" send_member="GetAll" />
        <allow send_destination="net.connman.iwd" send_interface="org.freedesktop.DBus.Properties" send_member="Get" />
        <allow send_destination="net.connman.iwd" send_interface="org.freedesktop.DBus.ObjectManager" send_member="GetManagedObjects" />
        <allow send_destination="net.connman.iwd" send_interface="net.connman.iwd.Device" send_member="RegisterSignalLevelAgent" />
        <allow send_destination="net.connman.iwd" send_interface="net.connman.iwd.Device" send_member="UnregisterSignalLevelAgent" />
      </policy>
    
    </busconfig>
    
###  加密网络配置文件

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 加密网络配置文件在某些配置文件中可能无效。 (在 [Talk:Iwd](<../zh-cn/Talk:Iwd.html>) 中讨论)

默认情况下，iwd 会以未加密方式在系统中存储网络凭证。自 iwd 1.25 版起，iwd 提供了试验性支持，可为使用 systemd 的系统创建[加密配置文件](<https://iwd.wiki.kernel.org/profile_encryption>)。 

首先，创建一个加密凭证。下面的示例使用[systemd-creds](</wzh/index.php?title=Systemd-creds&action=edit&redlink=1> "Systemd-creds（页面不存在）")创建了一个名为 _iwd-secret_ 的加密凭据，该凭据与系统的[Trusted Platform Module](<../zh-cn/Trusted_Platform_Module.html> "Trusted Platform Module")绑定，将用于创建加密配置文件： 
    
    # systemd-ask-password -n | systemd-creds --tpm2-device=auto --name=iwd-secret encrypt - /etc/credstore.encrypted/iwd-secret.cred
    
接下来，为 iwd 服务创建一个 [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file")，添加 `LoadCredentialEncrypted` 选项。 
    
    /etc/systemd/system/iwd.service.d/use-creds.conf
    
    [Service]
    
    LoadCredentialEncrypted=iwd-secret:/etc/credstore.encrypted/iwd-secret.cred

最终，在 iwd 配置文件中添加 `SystemdEncrypt` 选项（值为该凭证），[重载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") systemd 管理器，并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") iwd 服务。 
    
    /etc/iwd/main.conf
    
    [General]
    
    ...
    
    SystemdEncrypt=iwd-secret

**注意：**

  * 当前系统中的任何配置文件都将自动加密。此时无需其他操作，今后的任何配置文件都将自动加密。

  * 在上例中，加密凭据隐式绑定到 TPM PCR 7。因此，如果安全启动状态或固件证书发生变化，该启动会话将无法连接网络。

##  故障排除

###  详细 TLS 调试

如果在配置 MSCHAPv2 或 TTLS 时遇到困难，这会很有用。可以通过一个[附加配置片段](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")来设定以下[环境变量](<../zh-cn/Environment_variables.html> "Environment variables")： 
    
    /etc/systemd/system/iwd.service.d/tls-debug.conf
    
    [Service]
    Environment=IWD_TLS_DEBUG=TRUE

之后通过以 root 身份运行 `journalctl -u iwd.service` 命令检查 iwd 日志。 

###  引导后重启 iwd.service

一些电脑上 `iwd.service` 需引导后重启才能正常工作。参见 [FS#63912](<https://bugs.archlinux.org/task/63912>) 和 [thread 251432](<https://bbs.archlinux.org/viewtopic.php?id=251432>)。这很可能是因为 _iwd_ 在无线网卡上电之前启动了。 

作为解决方法，使用命令 `systemctl list-units --type=device | grep _wlan0_` 找到需要等待的单元，并相应地[扩展该单元](</wzh/index.php?title=%E6%89%A9%E5%B1%95%E8%AF%A5%E5%8D%95%E5%85%83&action=edit&redlink=1> "扩展该单元（页面不存在）")： 
    
    /etc/systemd/system/iwd.service.d/override.conf
    
    [Unit]
    After=sys-_XXXX_ -net-_wlan0_.device
    Wants=sys-_XXXX_ -net-_wlan0_.device

然后[重新加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新加载") _systemd_ 管理器配置。 

如果仍然无效，可以尝试添加以下配置： 
    
    [Service]
    ExecStartPre=ip link set wlan0 up
    
或者 
    
    [Service]
    ExecStartPre=/usr/bin/sleep 2
    
### Wireless device is not renamed by udev

1.0 起，iwd 禁用了可预测的无线设备重命名。它设置了阻止 udev 重命名 `wlp#s#` 接口的以下 systemd 网络连接配置文件： 
    
    /usr/lib/systemd/network/80-iwd.link
    
    [Match]
    Type=wlan
    
    [Link]
    NamePolicy=keep kernel

结果是网络链接名 `wlan#` 在引导后保留。 这使得 _iwd_ 和 [udev](<../zh-cn/Udev.html> "Udev") 间存在接口重命名的竞争，如 [iwd udev interface renaming](<https://iwd.wiki.kernel.org/interface_lifecycle#udev_interface_renaming>) 所述。 

如果造成问题，尝试以此解决： 
    
    # ln -s /dev/null /etc/systemd/network/80-iwd.link
    
###  在 AP 模式下无 DHCP

当在 AP 模式下通过 DHCP连接到 _iwd_ 时，客户端可能收不到 IP 地址。这有必要用 _iwd_ 在管理好的接口上启用网络配置。 
    
    /etc/iwd/main.conf
    
    [General]
    EnableNetworkConfiguration=True

提及文件若不存在则创建。 

###  因 iwd 崩溃无法连接 WiFi

一些用户经历 WiFi 断开的情况，通过不断重连，最终使之稳定并成功连接。 

用户通过 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 报告 `iwd.service` 崩溃 ([[1]](<https://bbs.archlinux.org/viewtopic.php?id=273965>)) 。 

核心问题 是多个网络连接服务冲突。要解决，请检查您是否同时[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")多个服务。 

###  客户端密钥加载错误

要加载密钥文件， _iwd_ 需要 `pkcs8_key_parser` [内核参数](<../zh-cn/Kernel_module.html> "Kernel module")。引导时，它由 [systemd-modules-load.service(8)](<https://man.archlinux.org/man/systemd-modules-load.service.8>) 使用 `/usr/lib/modules-load.d/pkcs8.conf` 加载，如果才安装 iwd，就不会出现这种情况。 

当尝试连接到 WPA 企业网络时，如在 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 有例如 `Error loading client private key _/path/to/key_` 的消息，请手动加载内核： 
    
    # modprobe pkcs8_key_parser
    
###  iwd 始终漫游

如果连接太差，iwd 会漫游到其他已知 AP。 

出现此问题，系统日志会报：`wlan0: deauthenticating from xx:xx:xx:xx:xx:xx by local choice (Reason: 3=DEAUTH_LEAVING)`

您可通过以下方法查看信号强度： 
    
    iwctl station wlan0 show | grep RSSI
    
您可调整阈值以允许更差的连接。RoamThreshold 默认值为 -70，RoamThreshold5G 默认值为 -76。
    
    /etc/iwd/main.conf
    
    [General]
    
    RoamThreshold=-75
    
    RoamThreshold5G=-80

###  DHCP 请求中未发送主机名

请在网络的配置文件中设置 `SendHostname`，而不是在 `/etc/iwd/main.conf` 中设置。 
    
    /var/lib/iwd/SomeNetwork.psk
    
    ...
    [IPv4]
    SendHostname=true

###  /etc/resolv.conf：只读文件系统

当使用 **resolvconf** 作为 DNS 解析方法时，可能会出现无法写入 `/etc/resolv.conf` 的问题，报错为只读文件系统： 
    
    $ journalctl -u iwd.service
    
    Jun 14 14:08:12 host iwd[1170270]: event: state, old: disconnected, new: autoconnect_quick
    Jun 14 14:08:12 host iwd[1170270]: udev interface=wlan0 ifindex=6
    Jun 14 14:08:13 host iwd[1170270]: event: connect-info, ssid: <redacted>, bss: <redacted>, signal: -63, load: 0/255
    Jun 14 14:08:13 host iwd[1170270]: event: state, old: autoconnect_quick, new: connecting (auto)
    Jun 14 14:08:13 host iwd[1170270]: event: state, old: connecting (auto), new: connecting (netconfig)
    Jun 14 14:08:14 host iwd[1170315]: cp: cannot create regular file '/etc/resolv.conf.bak': Read-only file system
    Jun 14 14:08:14 host iwd[1170316]: /usr/lib/resolvconf/libc: line 257: /etc/resolv.conf: Read-only file system
    Jun 14 14:08:16 host iwd[1170366]: cp: cannot create regular file '/etc/resolv.conf.bak': Read-only file system
    Jun 14 14:08:16 host iwd[1170367]: /usr/lib/resolvconf/libc: line 257: /etc/resolv.conf: Read-only file system
    Jun 14 14:08:16 host iwd[1170270]: event: state, old: connecting (netconfig), new: connected

解决此问题的方法是，通过添加 [drop-in](<https://wiki.archlinux.org/title/Systemd#Drop-in_files>) 扩展 `iwd.service` systemd 单元的配置： 
    
    /etc/systemd/system/iwd.service.d/50-resolvconf.conf
    
    [Service]
    RuntimeDirectory=resolvconf
    ReadWritePaths=/etc/resolv.conf

这将允许 `iwd.service` 系统单元更新 `/etc/resolv.conf`。[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `iwd.service` 以使更改生效。 

**注意：** 关于此问题的讨论请参见上游邮件列表：[Re: iwd doesn't work with openresolv](<https://lore.kernel.org/iwd/2249097a-97e0-175a-6b02-e5d6be484498%40gmail.com/>)

##  另请参阅

  * [开始使用 iwd（英文）](<https://iwd.wiki.kernel.org/gettingstarted>)
  * [网络配置设置（英文）](<https://iwd.wiki.kernel.org/networkconfigurationsettings>)
  * [WPA Enterprise 的更多示例（英文）](<https://git.kernel.org/pub/scm/network/wireless/iwd.git/tree/autotests>)
  * [Arch Linux 论坛上的 IWD 帖子（英文）](<https://bbs.archlinux.org/viewtopic.php?id=237074>)
  * [2017 Update on new WiFi daemon for Linux by Marcel Holtmann - YouTube](<https://www.youtube.com/watch?v=F2Q86cphKDo>)
  * [The New Wi-Fi Experience for Linux - Marcel Holtmann, Intel - YouTube](<https://www.youtube.com/watch?v=QIqT2obSPDk>)
  * [How to set up a simple access point with iwd](<https://iwd.wiki.kernel.org/ap_mode>)
