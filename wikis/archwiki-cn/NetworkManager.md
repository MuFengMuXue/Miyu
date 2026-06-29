**翻译状态：**

  * 本文（或部分内容）译自 [NetworkManager](<https://wiki.archlinux.org/title/NetworkManager> "arch:NetworkManager")，最近一次同步于 2025-07-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/NetworkManager?diff=0&oldid=838657>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NetworkManager_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")
  * [网络配置/无线网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE/%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置/无线网络配置")

[NetworkManager](<https://networkmanager.dev/>) 是一个为系统提供检测和配置功能以便自动连接到网络的程序。NetworkManager 的功能对无线和有线网络都很有用。对于无线网络，NetworkManager 偏好已知的无线网络，并能切换到最可靠的网络。能感知 NetworkManager 的应用程序可以切换在线和离线模式。比起无线连接，NetworkManager 更偏好有线连接，且支持调制解调器连接和一些类型的 VPN。NetworkManager 最初由 Red Hat 开发，现在由 [GNOME](<../zh-cn/GNOME.html> "GNOME") 管理。 

**警告：** 默认情况下，文件系统中的 root 用户和通过 GUI（如 _nm-applet_ ）访问设置的用户可以访问机密信息（如 WiFi 密码）。参见[#加密的 Wi-Fi 密码](<#%E5%8A%A0%E5%AF%86%E7%9A%84_Wi-Fi_%E5%AF%86%E7%A0%81>)。

##  安装

可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包 软件包获取 NetworkManager。此软件包包含一个守护程序、一个命令行界面（`nmcli`）和一个基于 curses 的界面（`nmtui`）。 

###  启用 NetworkManager

安装完成后，[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `NetworkManager.service`。NetworkManager 守护进程启动后，会自动连接到已配置且可用的“系统连接”。“用户连接”和未配置的连接需要通过 _nmcli_ 或 applet 进行配置和连接。 

**注意：**

  * 请确保没运行其它网络配置服务；多个网络服务会发生冲突。可以用 `systemctl --type=service` 查看正在运行的服务列表，然后[停止](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")它们。参见[#配置](<#%E9%85%8D%E7%BD%AE>)以启用 NetworkManager 服务。
  * 如果 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 没有[启动](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")，错误消息将会淹没日志。详见后面的 Unit dbus-org.freedesktop.resolve1.service not found 部分。

###  额外的界面

  * [nm-connection-editor](<https://archlinux.org/packages/?name=nm-connection-editor>)包 提供图形界面；
  * [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 提供系统托盘图标（`nm-applet`）。

###  移动网络支持

NetworkManager 使用 [ModemManager](</wzh/index.php?title=ModemManager&action=edit&redlink=1> "ModemManager（页面不存在）") 提供移动宽带连接。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [modemmanager](<https://archlinux.org/packages/?name=modemmanager>)包 和 [usb_modeswitch](<https://archlinux.org/packages/?name=usb_modeswitch>)包。然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `ModemManager.service`。 

可能需要[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `NetworkManager.service` 才能使其检测 ModemManager。重新启动后，重新插入调制解调器应该就可以识别了。 

从前端界面(例如 [nm-connection-editor](<https://archlinux.org/packages/?name=nm-connection-editor>)包)添加连接并将连接类型选择为 broadband,选择 ISP 和套餐, [mobile-broadband-provider-info](<https://archlinux.org/packages/?name=mobile-broadband-provider-info>)包 会自动填入 [APN](<https://en.wikipedia.org/wiki/Access_Point_Name> "wikipedia:Access Point Name") 和其它设置。 

###  PPPoE / DSL 支持

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ppp](<https://archlinux.org/packages/?name=ppp>)包 以支持 PPPoE / DSL 连接。使用 `nm-connection-editor` 添加一个新的 DSL/PPPoE 连接。 

###  VPN 支持

从 1.16 版本开始 NetworkManager 原生支持 [WireGuard](<../zh-cn/WireGuard.html> "WireGuard")，它只需要 `wireguard` 内核模块。详见 [WireGuard in NetworkManager 博客文章](<https://blogs.gnome.org/thaller/2019/03/15/wireguard-in-networkmanager/>)。 

对其他类型 VPN 的支持基于一个插件系统。它们在以下软件包中提供： 

  * [networkmanager-openconnect](<https://archlinux.org/packages/?name=networkmanager-openconnect>)包 支持 [OpenConnect](</wzh/index.php?title=OpenConnect&action=edit&redlink=1> "OpenConnect（页面不存在）")
  * [networkmanager-openvpn](<https://archlinux.org/packages/?name=networkmanager-openvpn>)包支持 [OpenVPN](<../zh-cn/OpenVPN.html> "OpenVPN")
  * [networkmanager-pptp](<https://archlinux.org/packages/?name=networkmanager-pptp>)包 支持 [PPTP Client](<../zh-cn/PPTP_Client.html> "PPTP Client")
  * [networkmanager-strongswan](<https://archlinux.org/packages/?name=networkmanager-strongswan>)包 支持 [strongSwan](<../zh-cn/StrongSwan.html> "StrongSwan")
  * [networkmanager-vpnc](<https://archlinux.org/packages/?name=networkmanager-vpnc>)包
  * [networkmanager-fortisslvpn-git](<https://aur.archlinux.org/packages/networkmanager-fortisslvpn-git/>)AUR
  * [networkmanager-iodine-git](<https://aur.archlinux.org/packages/networkmanager-iodine-git/>)AUR
  * [networkmanager-libreswan](<https://aur.archlinux.org/packages/networkmanager-libreswan/>)AUR
  * [networkmanager-l2tp](<https://archlinux.org/packages/?name=networkmanager-l2tp>)包
  * [networkmanager-ssh](<https://aur.archlinux.org/packages/networkmanager-ssh/>)AUR
  * [network-manager-sstp](<https://archlinux.org/packages/?name=network-manager-sstp>)包

**警告：** 有很多与 VPN 支持有关的[错误](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues?search=VPN&state=opened>)。Check the daemon processes options set via the GUI correctly and double-check with each package release.

**注意：**

  * 要在使用 VPN 时获得完整的 DNS 解析，请设置[条件转发](<#DNS_%E7%BC%93%E5%AD%98%E5%92%8C%E6%9D%A1%E4%BB%B6%E8%BD%AC%E5%8F%91>)。
  * 这些插件可能没有文档化的命令行界面，或者在没有运行 applet 的情况下根本无法工作。如果您使用的是常规 DE，那么这不是问题；如果不是，那么您应该在配置或激活连接时运行 [#nm-applet](<#nm-applet>)，来显示必要的对话框。[[1]](<https://bbs.archlinux.org/viewtopic.php?id=246698>)

##  使用

NetworkManager 附带 [nmcli(1)](<https://man.archlinux.org/man/nmcli.1>) 和 [nmtui(1)](<https://man.archlinux.org/man/nmtui.1>)。 

###  nmcli 示例

显示附近的 Wi-Fi 网络： 
    
    $ nmcli device wifi list
    
连接到 Wi-Fi 网络： 
    
    $ nmcli device wifi connect _SSID_或_BSSID_ password _密码_
    
连接到隐藏的 Wi-Fi 网络： 
    
    $ nmcli device wifi connect _SSID_或_BSSID_ password _密码_ hidden yes
    
连接到 `wlan1` 网络接口上的 Wi-Fi： 
    
    $ nmcli device wifi connect _SSID_或_BSSID_ password _密码_ ifname wlan1 _profile_name_
    
断开网络接口上的连接： 
    
    $ nmcli device disconnect ifname eth0
    
显示连接列表及其名称、UUID、类型和支持设备： 
    
    $ nmcli connection show
    
激活连接（即使用现有配置文件连接到网络）： 
    
    $ nmcli connection up _name_或_uuid_
    
删除连接： 
    
    $ nmcli connection delete _name_或_uuid_
    
显示所有网络设备及其状态： 
    
    $ nmcli device
    
关闭 Wi-Fi： 
    
    $ nmcli radio wifi off
    
###  编辑连接

设置的完整列表参见 [nm-settings(5)](<https://man.archlinux.org/man/nm-settings.5>)。 

首先需要获取连接列表： 
    
    $ nmcli connection
    
    NAME                UUID                                  TYPE      DEVICE
    Wired connection 2  e7054040-a421-3bef-965d-bb7d60b7cecf  ethernet  enp5s0
    Wired connection 1  997f2782-f0fc-301d-bfba-15421a2735d8  ethernet  enp0s25
    MY-HOME-WIFI-5G     92a0f7b3-2eba-49ab-a899-24d83978f308  wifi       --
    
第一列可以作为连接 connection-id, 本示例中使用 `Wired connection 2`。 

创建后有三种方法可以配置 `Wired connection 2`： 

nmcli 交互式编辑器
     `nmcli connection edit 'Wired connection 2'`.  
Usage is well documented from the editor.

nmcli 命令行界面
     `nmcli connection modify 'Wired connection 2' _setting_._property_ _value_`. 用法参见 [nmcli(1)](<https://man.archlinux.org/man/nmcli.1>) 。 For example you can change its IPv4 route metric to 200 using `nmcli connection modify 'Wired connection 2' ipv4.route-metric 200` command.

To remove a setting pass an empty field ("") to it like this: 

    `nmcli connection modify 'Wired connection 2' _setting_._property_ ""`

连接文件
    在 `/etc/NetworkManager/system-connections/` 中修改对应的 `Wired connection 2.nmconnection` 文件。  
别忘了使用 `nmcli connection reload` 重新加载配置文件。

### nmtui

NetworkManager 提供了一个用于管理连接、系统主机名和无线开关的文本用户界面（TUI）。可以通过运行 `nmtui` 来启动。 

##  前端

为把 NetworkManager 与桌面环境集成，您可以安装一个 applet。这不仅便于您轻松访问网络选择和配置界面，更能提供一个安全存储网络密钥的代理程序。这种图形前端往往显示在系统托盘（或通知区域），从而允许用户选择网络或者配置 NetworkManager。各种桌面环境都有自己的 applet。你也可以使用 [#nm-applet](<#nm-applet>)。 

### GNOME

[GNOME](<../zh-cn/GNOME.html> "GNOME") 在 _网络设置_ 里有内置的配置工具。 

### KDE Plasma

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [plasma-nm](<https://archlinux.org/packages/?name=plasma-nm>)包 软件包。然后通过 _面板的选项 > 添加部件 > 网络_将其添加到 KDE 的任务栏上。 

### nm-applet

[network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 是一个工作在 Xorg 环境下的 GTK 3 前端，带有一个系统托盘。 

为了存储连接密码，您可以安装实现了 [Secret Service D-Bus API](<https://specifications.freedesktop.org/secret-service/latest/>) 的应用程序，如 [GNOME/Keyring](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring")、[KDE Wallet](<../zh-cn/KDE_Wallet.html> "KDE Wallet") 和 [KeePassXC](</wzh/index.php?title=KeePassXC&action=edit&redlink=1> "KeePassXC（页面不存在）")。 

请注意，如果对某个连接启用了 `对其他用户可用` 选项，NetworkManager 就会明文存储密码，不过相应的文件只能被 root 或者其他使用 `nm-applet` 的用户访问。参照 [#加密的 Wi-Fi 密码](<#%E5%8A%A0%E5%AF%86%E7%9A%84_Wi-Fi_%E5%AF%86%E7%A0%81>)。 

要在没有系统托盘的情况下运行 `nm-applet`，可以使用 [trayer](<https://archlinux.org/packages/?name=trayer>)包 或 [stalonetray](<https://archlinux.org/packages/?name=stalonetray>)包。例如，可以在自己的可执行文件路径中添加这样的脚本： 
    
    nmgui
    
    #!/bin/sh
    nm-applet    2>&1 > /dev/null &
    stalonetray  2>&1 > /dev/null
    killall nm-applet
    
当关闭 _stalonetray_ 窗口的时候，它也会关闭 `nm-applet`，所以当你完成网络配置后它就不会再占用内存。 

applet 可以显示一些事件的通知，比如连接或断开 WiFi。要显示这些消息，确保你已安装了一个通知服务器——请参见 [Desktop notifications](<../zh-cn/Desktop_notifications.html> "Desktop notifications")。如果在没有通知服务器的情况下使用，那么可能会在 stdout/stderr 中看到一些消息，并且 applet可能会挂起。请参见[[2]](<https://bugzilla.gnome.org/show_bug.cgi?id=788313>)。 

要在禁用通知的情况下使用 `nm-applet`，请使用以下命令运行 applet： 
    
    $ nm-applet --no-agent
    
**提示：**`nm-applet` 可能被[自启动桌面配置项](<../zh-cn/XDG_Autostart.html> "XDG Autostart")自动启动, 这种情况下请在那里的 Exec 一行添加 `--no-agent` 选项： 
    
    Exec=nm-applet --no-agent

**警告：** 在 [i3](<../zh-cn/I3.html> "I3") 中，如果以 `--no-agent` 选项启动 nm-applet，将无法通过点击列表中的项目来连接新的加密 Wi-Fi 网络，因为不会弹出密码输入对话框。[journal](<../zh-cn/Systemd/Journal.html> "Journal") 中会显示 `no secrets: No agents were available for this request`。

#### Appindicator

从 1.18.0 版本开始，官方软件包 [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 中[包含](<https://github.com/archlinux/svntogit-packages/commit/7640a2bd557fe84813207ef4d5e35bb5aece6c54>) Appindicator 支持。要在 Appindicator 环境中使用 nm-applet，请使用以下命令启动 applet： 
    
    $ nm-applet --indicator
    
### networkmanager-dmenu

[networkmanager-dmenu-git](<https://aur.archlinux.org/packages/networkmanager-dmenu-git/>)AUR 是一个通过 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 或 [rofi](<../zh-cn/Rofi.html> "Rofi") 而不是 `nm-applet` 管理 NetworkManager 连接的小脚本。它提供了所有必要的功能, 例如连接到已有的 NetworkManager wifi 或有线网络、连接到新的 wifi 网络、在需要的时候询问密码、连接到已有的 VPN、启用/停用网络连接、运行 _nm-connection-editor_ 图形界面、连接到蓝牙网络等等。 

### switchboard

Pantheon 的 [switchboard](<https://archlinux.org/packages/?name=switchboard>)包 搭配 [switchboard-plug-network](<https://archlinux.org/packages/?name=switchboard-plug-network>)包 和 [nm-connection-editor](<https://archlinux.org/packages/?name=nm-connection-editor>)包，提供了一种与桌面环境无关的方式来配置 NetworkManager。可以通过以下命令运行： 
    
    $ io.elementary.settings
    
##  配置

NetworkManager 需要一些额外的步骤才能正常运行。请确保已按照[网络配置#设置计算机名](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E8%AE%BE%E7%BD%AE%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%90%8D> "网络配置")一节的描述配置 `/etc/hosts`。 

NetworkManager 的全局配置文件位于 `/etc/NetworkManager/NetworkManager.conf`。额外的配置文件可以放在 `/etc/NetworkManager/conf.d/` 中。全局的默认配置通常不需要改动。 

编辑配置文件后，可以使用以下命令应用更改： 
    
    # nmcli general reload
    
### NetworkManager-wait-online

启用 `NetworkManager.service` 的同时也会启用 `NetworkManager-wait-online.service`，这是一个一次性（oneshot）系统服务，用于等待网络配置完成。后者包含 `WantedBy=network-online.target`，因此只有当 `network-online.target` 本身被启用或被其他单元拉取时才会完成。另见 [systemd#Running services after the network is up](<../zh-cn/Systemd.html#Running_services_after_the_network_is_up> "Systemd")。 

默认情况下，`NetworkManager-wait-online.service` 会等待 NetworkManager 启动完成，而不是特指等待网络连接可用（参见 [nm-online(1)](<https://man.archlinux.org/man/nm-online.1>)）。如果 `NetworkManager-wait-online.service` 在网络真正连通之前就结束，可能会导致启动时某些服务失败，可以通过[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")移除 `ExecStart` 行中的 `-s` 参数来解决： 
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/nm-online -q
    
注意这可能会导致[其他问题](<https://lists.fedoraproject.org/archives/list/users@lists.fedoraproject.org/thread/EGC324JD3HJCGVN7J55WYPRLFDA3TP7N/>)。 

在某些情况下，由于超时太短，服务仍然无法在启动时成功启动。[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")服务，将 `NM_ONLINE_TIMEOUT` 从 `60` 改为更大的值。 

###  设置 PolicyKit 权限

默认情况下，活动的本地会话中的所有用户都能在没有密码的情况下改变大多数网络设置。参照 [General troubleshooting#会话权限](<../zh-cn/General_troubleshooting.html#%E4%BC%9A%E8%AF%9D%E6%9D%83%E9%99%90> "General troubleshooting")检查会话类型。在大多数情况下，一切都应该开箱即用。 

一些操作（例如改变系统计算机名）需要管理员密码。这时，需要将自己[添加](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")到 `wheel` 用户组并运行一个 [polkit 身份认证组件](<../zh-cn/Polkit.html#%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81%E7%BB%84%E4%BB%B6> "Polkit")，它将提示输入密码。 

对于远程会话（例如 [headless VNC](<../zh-cn/TigerVNC.html#Running_vncserver_for_virtual_\(headless\)_sessions> "TigerVNC")），有几种方法获得使用 NetworkManager 所需的权限： 

  1. 将自己[添加](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")到 `wheel` 用户组。执行每个操作时都需要输入自己的密码。注意你的账户同时被赋予了此账户组的其他权限，例如使用 [sudo](<../zh-cn/Sudo.html> "Sudo") 命令时无需输入 root 密码。
  2. 将自己[添加](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "Users and groups")到 `network` 用户组，同时创建一个包含以下内容的 `/etc/polkit-1/rules.d/50-org.freedesktop.NetworkManager.rules` 文件：
         
         polkit.addRule(function(action, subject) {
           if (action.id.indexOf("org.freedesktop.NetworkManager.") == 0 && subject.isInGroup("network")) {
             return polkit.Result.YES;
           }
         });
         
`network` 用户组中的所有用户都将能免密码管理网络，这意味着不需要运行 polkit 身份认证组件，因此在 SSH 会话中也能工作。

###  代理设置

NetworkManager 支持一些代理设置。虽然这些设置无法直接通过 _nmtui_ 修改，但 _nm-applet_ 和 _nmcli_ 支持它们，也可以通过调度脚本运行自定义代理命令。 请参阅 [nm-settings-nmcli(5)](<https://man.archlinux.org/man/nm-settings-nmcli.5>) 中的代理设置与 [#Dispatcher examples](<#Dispatcher_examples>)。 

此外，如果你使用 [GNOME](<../zh-cn/GNOME.html> "GNOME") 或 [KDE](<../zh-cn/KDE.html> "KDE")，你可以使用 [proxydriver](<https://aur.archlinux.org/packages/proxydriver/>)AUR，它将使用 NetworkManager 的信息处理代理设置。 

要让 _proxydriver_ 能够改变代理设置，你需要执行下面的命令，来让NetworkManager作为GNOME启动过程的一部分。（参见 [GNOME#自启动](<../zh-cn/GNOME.html#%E8%87%AA%E5%90%AF%E5%8A%A8> "GNOME")）。 
    
    $ xhost +si:localuser:_username_
    
参见 [Proxy server](<../zh-cn/Proxy_server.html> "Proxy server")。 

###  检查互联网可连接性

NetworkManager 可以在连接到网络后尝试访问一个 Web 服务器，以确定该网络是否需要进行进一步认证（比如基于强制网络门户的网页认证）。 默认网址（在 `/usr/lib/NetworkManager/conf.d/20-connectivity.conf` 中配置）是 [ping.archlinux.org](<https://ping.archlinux.org>)。要使用其他 Web 服务器或禁用连接检查，请创建 `/etc/NetworkManager/conf.d/20-connectivity.conf`，请参见 [NetworkManager.conf(5) § CONNECTIVITY SECTION](<https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTIVITY_SECTION>)。如下配置文件示例使用了由 GNOME 提供的另一个 Web 服务器 (并不一定要使用 [GNOME](<../zh-cn/GNOME.html> "GNOME") 桌面环境): 
    
    /etc/NetworkManager/conf.d/20-connectivity.conf
    
    [connectivity]
    uri=http://nmcheck.gnome.org/check_network_status.txt
    
若要禁用 NetworkManager 的连接性检查（有时候一些 VPN 会阻止这类检查），请使用以下配置： 
    
    /etc/NetworkManager/conf.d/20-connectivity.conf
    
    [connectivity] 
    enabled=false
    
**注意：** 尽管自动连接检查理论上可能会泄露隐私，但 Arch Linux 默认设置的连接检查 Web 服务器承诺不会记录任何访问。 请参考 [[3]](<https://gitlab.archlinux.org/archlinux/infrastructure/-/commit/fabccd0f61e5dea3925e8a0c6a46d56d5750c121#a4f34381bbb18ea77bfb3dd11a8aeca707078fca_0_26>) [[4]](<https://gitlab.archlinux.org/archlinux/infrastructure/-/blob/master/roles/ping/templates/nginx.d.conf.j2>).

###  强制网络门户

如果您连接的网络提供了[强制门户](<https://en.wikipedia.org/wiki/zh:%E5%BC%BA%E5%88%B6%E9%97%A8%E6%88%B7> "w:zh:强制门户")（一般用于网页认证）, 桌面管理器会自动打开一个窗口并要求您输入凭据。如果您的桌面管理器没有这么做，则您可以安装 [capnet-assist](<https://archlinux.org/packages/?name=capnet-assist>)包 软件包 (然而其 NetworkManager 的 disapatcher 脚本目前是坏的)。或者您也可以参考以下内容创建一个自己的 dispatcher 脚本。 
    
    /etc/NetworkManager/dispatcher.d/90-open_captive_portal
    
    #!/bin/sh -e
    # Script to dispatch NetworkManager events
    #
    # Runs shows a login webpage on walled garden networks.
    # See NetworkManager(8) for further documentation of the dispatcher events.
    
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    
    if [ -x "/usr/bin/logger" ]; then
        logger="/usr/bin/logger -s -t captive-portal"
    else
        logger=":"
    fi
    
    wait_for_process() {
        PNAME=$1
        while [ -z "$(/usr/bin/pgrep $PNAME)" ]; do
            sleep 3;
        done
    }
    
    #launch the browser, but on boot we need to wait that nm-applet starts
    start_browser() {
        local user="$1"
        local display="$2"
    
        export DISPLAY="$display"
        wait_for_process nm-applet
    
        export XAUTHORITY="/home/$user/.Xauthority"
        export GTK_IM_MODULE=fcitx:ibus
    
        $logger "Running browser as '$user' with display '$display' to login in captive portal"
        sudo -u "$user" --preserve-env=DISPLAY,XAUTHORITY,GTK_IM_MODULE -H xdg-open http://capnet.elementary.io 2>&1 > /dev/null
    }
    
    # Run the right scripts
    case "$2" in
        connectivity-change)
        $logger -p user.debug "dispatcher script triggered on connectivity change: $CONNECTIVITY_STATE"
        if [ "$CONNECTIVITY_STATE" = "PORTAL" ]; then
            # Match last column of who's output with ' :[at least one digit] '
            who | awk '$NF ~ /\(:[0-9]+\)/ { print $1 " " substr($NF, 2, length($NF)-2) };' | \
            while read user display; do
                start_browser $user $display || $logger -p user.err "Failed for user: '$user' display: '$display'"
            done
        fi
        ;;
        *)
        # In a down phase
        exit 0
        ;;
    esac
    
请将该脚本设为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。但该脚本假设你使用的是 X，并且只是打开一个 HTTP 页面，可能并不适用于所有人。 

你需要[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `NetworkManager.service` 或重新启动系统，脚本才会开始生效。一旦启用，当检测到你处于强制门户（captive portal）环境中时，调度脚本应会自动打开登录窗口。 

一个简单的解决方案是 [captive-portal-sh](<https://github.com/Seme4eg/captive-portal-sh>)——一个用于获取强制门户 URL 并在默认浏览器中打开的 shell 脚本（仅适用于 Wayland 用户）。 

另一个方案是基于 Google Chrome 的 [captive-browser-git](<https://aur.archlinux.org/packages/captive-browser-git/>)AUR。 

####  旧硬件中通过 iwd 支持强制门户（captive portal）

一些较老的 Wi-Fi 芯片（例如 Broadcom BCM4360）需要使用专有的 `wl` 驱动，该驱动不支持许多强制门户热点在显示登录页面前所使用的 OWE/椭圆曲线握手（Elliptic-Curve handshake）。 通过将 NetworkManager 的 Wi-Fi 后端切换为 `iwd`（参见 [#Using iwd as the Wi-Fi backend](<#Using_iwd_as_the_Wi-Fi_backend>)），可以在现有驱动基础上由用户空间实现完整的 OWE 密钥交换，从而完成加密关联、获取 DHCP 租约，并触发门户的 “PORTAL” 状态。 完成这些步骤后，任何调度脚本或浏览器启动器都可以可靠地弹出登录页面，即使是原本无法完全连接的硬件也能正常访问网络。 

###  DHCP 客户端

NetworkManager 默认使用内置的 DHCP 客户端。内置的 DHCPv4 插件基于 [nettools 的 n-dhcp4](<https://nettools.github.io/n-dhcp4/>) 库，而内置的 DHCPv6 插件的代码基于 systemd-networkd。 

要使用不同的 DHCP 客户端，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下之一： 

  * [dhcpcd](<https://archlinux.org/packages/?name=dhcpcd>)包 \- [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd")。
  * [dhclient](<https://archlinux.org/packages/?name=dhclient>)包 \- [dhclient](</wzh/index.php?title=Dhclient&action=edit&redlink=1> "Dhclient（页面不存在）")。

要更改 DHCP 客户端后端，请在 `/etc/NetworkManager/conf.d/` 中的配置文件中设置选项 `main.dhcp=_dhcp 客户端名称_`。例如： 
    
    /etc/NetworkManager/conf.d/dhcp-client.conf
    
    [main]
    dhcp=dhclient

**注意：**

  * NetworkManager 不支持使用 dhcpcd 进行 IPv6 配置。 详见[NetworkManager issue #5](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/5>).如果将 dhcpcd 设置为 DHCP 客户端，NetworkManager 将为 DHCPv6 使用内置 DHCP 客户端。
  * 不要启用 [dhclient](<https://archlinux.org/packages/?name=dhclient>)包 和 [dhcpcd](<https://archlinux.org/packages/?name=dhcpcd>)包 软件包提供的 systemd 单元。它们会与 NetworkManager 冲突，详情请参见[#安装](<#%E5%AE%89%E8%A3%85>)中的注释。

###  DNS 管理

NetworkManager 的 DNS 管理在 GNOME 项目的 wiki 页面中进行了描述——[Projects/NetworkManager/DNS](<https://wiki.gnome.org/Projects/NetworkManager/DNS>)。 

####  DNS 缓存和条件转发

NetworkManager 有一个插件，用于启用 DNS 缓存和条件转发 ([以前](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/merge_requests/143>)在 NetworkManager 的文档中称为“拆分 DNS”）。此设置的优点是 DNS 查找将被缓存，缩短了解析时间，并且 VPN 主机的 DNS 查找将路由到相关 VPN 的 DNS 服务器。如果您连接到多个 VPN，这尤其有用。 

**注意：** 如果 `/etc/resolv.conf` 是指向 `/run/systemd/resolve/stub-resolv.conf`、`/run/systemd/resolve/resolv.conf`、`/lib/systemd/resolv.conf` 或 `/usr/lib/systemd/resolv.conf` 的符号链接，NetworkManager 将自动选择 systemd resolved。要使用 dnsmasq，必须首先删除该符号链接，然后重新启动 NetworkManager。

##### dnsmasq

确保已安装 [dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包。然后在 `/etc/NetworkManager/conf.d/` 中的配置文件中设置 `main.dns=dnsmasq`： 
    
    /etc/NetworkManager/conf.d/dns.conf
    
    [main]
    dns=dnsmasq

现在以 root 身份运行 `nmcli general reload`。NetworkManager 将自动启动 dnsmasq 并将 `127.0.0.1` 添加到 `/etc/resolv.conf`。原来的 DNS 服务器可以在 `/run/NetworkManager/no-stub-resolv.conf` 中找到。你可以通过使用 `drill example.com` 进行两次相同的 DNS 查询，来确认是否正在使用 dnsmasq，同时验证服务器和查询时间。 

**注意：**

  * 无需启动 `dnsmasq.service` 或编辑 `/etc/dnsmasq.conf`。NetworkManager 不通过 systemd 服务启动 dnsmasq，也不会读取 dnsmasq 的默认配置文件。
  * NetworkManager 启动的 dnsmasq 实例会绑定到 `127.0.0.1:53`，因此你不能在同一地址和端口上运行其他软件（包括 `dnsmasq.service`）。

######  自定义 dnsmasq 配置

可以通过在 `/etc/NetworkManager/dnsmasq.d/` 中创建配置文件为 _dnsmasq_ 创建自定义配置。例如，要更改 DNS 缓存（存储在 RAM 中）的大小： 
    
    /etc/NetworkManager/dnsmasq.d/cache.conf
    
    cache-size=1000

可以使用以下命令检查配置文件语法： 
    
    $ dnsmasq --test --conf-file=/dev/null --conf-dir=/etc/NetworkManager/dnsmasq.d
    
所有可用选项请参见 [dnsmasq(8)](<https://man.archlinux.org/man/dnsmasq.8>)。 

###### IPv6

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 这并不能解决问题，因为 NetworkManager 不会将 `::1` 添加到 `/etc/resolv.conf` 中。除非手动传递 `@::1` 给 drill，否则它仍然会因为 `Error: error sending query: No (valid) nameservers defined in the resolver` 而失败。（在 [Talk:NetworkManager](<../zh-cn/Talk:NetworkManager.html>) 中讨论）

在 NetworkManager 中启用 `dnsmasq` 可能会破坏本应正常工作的 IPv6-only DNS 查询（例如 `drill -6 [hostname]`）。为了解决这个问题，可以创建以下文件，配置 _dnsmasq_ 也监听 IPv6 回环地址： 
    
    /etc/NetworkManager/dnsmasq.d/ipv6-listen.conf
    
    listen-address=::1

此外，`dnsmasq` 也不优先考虑上游 IPv6 DNS。遗憾的是，NetworkManager 无法执行此操作 ([Ubuntu Bug](<https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/936712>)）。解决方法是在 NetworkManager 配置中禁用 IPv4 DNS（如果有）。 

###### DNSSEC

默认情况下，NetworkManager 启动的 dnsmasq 实例不会验证 [DNSSEC](</wzh/index.php?title=DNSSEC&action=edit&redlink=1> "DNSSEC（页面不存在）")，因为它是使用 `--proxy-dnssec` 选项启动的。它将信任从上游 DNS 服务器获得的任何 DNSSEC 信息。 

要让 dnsmasq 验证 DNSSEC（这会破坏不支持 DNSSEC 的 DNS 服务器的解析），请创建以下配置文件： 
    
    /etc/NetworkManager/dnsmasq.d/dnssec.conf
    
    conf-file=/usr/share/dnsmasq/trust-anchors.conf
    dnssec

##### systemd-resolved

NetworkManager 能把 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 作为DNS解析器和缓存。在使用它之前，确保你已正确配置 _systemd-resolved_ 并且 `systemd-resolved.service` 已经[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")。 

如果 `/etc/resolv.conf` 是一个指向 `/run/systemd/resolve/stub-resolv.conf`、`/run/systemd/resolve/resolv.conf` 或 `/usr/lib/systemd/resolv.conf` 的[符号链接](<../zh-cn/Systemd-resolved.html#DNS> "Systemd-resolved")，systemd-resolved会自动启用。 

你也可以通过编写 `/etc/NetworkManager/conf.d/` 下的配置文件，设置 `main.dns=systemd-resolved` 来显式启用它： 
    
    /etc/NetworkManager/conf.d/dns.conf
    
    [main]
    dns=systemd-resolved

#####  使用 openresolv 监听者的 DNS 解析器

如果 [openresolv](</wzh/index.php?title=Openresolv&action=edit&redlink=1> "Openresolv（页面不存在）") 有适用于你的本地 [DNS resolver](<../zh-cn/DNS_resolver.html> "DNS resolver") 的监听者，请设置该监听者并[配置 NetworkManager 使用 openresolv](<#Use_openresolv>)。 

由于 NetworkManager 向 _resolvconf_ 广播的是单一“接口”，因此无法在两个 NetworkManager 连接之间实现条件转发。详见 [NetworkManager issue 153](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/153>)。 

如果你在 `/etc/resolvconf.conf` 中设置了 `private_interfaces="*"`[[5]](<https://roy.marples.name/projects/openresolv/configuration/>)，可以部分缓解该问题。任何不在搜索域列表中的查询都不会被转发，而是根据本地解析器的配置处理，例如转发到其他 DNS 服务器或从 DNS 根递归解析。 

####  自定义 DNS 服务器

#####  设置自定义全局 DNS 服务器

要为所有连接设置 DNS 服务器，请在 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>) 中的 `[global-dns-domain-*]` 的部分下使用 `servers=_serveripaddress1_ ,_serveripaddress2_ ,_serveripaddress3_` 的格式指定它们。例如： 
    
    /etc/NetworkManager/conf.d/dns-servers.conf
    
    [global-dns-domain-*]
    servers=::1,127.0.0.1

**注意：**

  * 如果您使用 [NetworkManager's dnsmasq or systemd-resolved plugin](<#DNS_%E7%BC%93%E5%AD%98%E5%92%8C%E6%9D%A1%E4%BB%B6%E8%BD%AC%E5%8F%91>) 或 [openresolv subscribers](<#DNS_resolver_with_an_openresolv_subscriber>)，则不要使用 `servers=` 选项指定环回地址，因为这可能会破坏 DNS 解析。
  * 指定的服务器不会被发送到 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")，而是使用连接的 DNS 服务器。

#####  设置自定义连接 DNS 服务器

######  设置自定义连接 DNS 服务器（GUI）

设置方法取决于所使用的前端类型；通常流程是右键点击程序小工具，编辑（或创建）一个配置文件，然后选择 DHCP 类型为 _自动（指定地址）_ 。 需要输入 DNS 地址，格式通常为：`127.0.0.1, _DNS-server-one_ , ...`。 

######  设置自定义连接 DNS 服务器（nmcli / 连接文件）

要为每个连接设置 DNS 服务器，需要修改[连接设置](<#Edit_a_connection>)中的 `ipv4.dns` 和 `ipv6.dns`（以及对应的 `dns-search` 和 `dns-options`）参数。 

如果 `method` 设置为 `auto`（即使用 DHCP/RA），则需要将 `ignore-auto-dns` 设置为 `yes`。 

要使用 DNS over TLS（[需要 systemd-resolved](<#systemd-resolved>)），请使用语法 `dns=_ip.address_ #_servername_ ;` 指定 DNS 服务器，同时将 `connection.dns-over-tls` 设置为 `2`。例如，要使用 Quad9： 
    
    /etc/NetworkManager/system-connections/Example Wi-Fi.nmconnection
    
    ...
    [connection]
    ...
    dns-over-tls=2
    
    [ipv4]
    ...
    dns=9.9.9.9#dns.quad9.net;149.112.112.112#dns.quad9.net;
    ignore-auto-dns=true
    
    [ipv6]
    ...
    dns=2620:fe::fe#dns.quad9.net;2620:fe::9#dns.quad9.net;
    ignore-auto-dns=true

**注意：** 此示例使用 Quad9。请替换为你信任的 DNS 解析器。详见 [Domain name resolution#Third-party DNS services](<../zh-cn/Domain_name_resolution.html#Third-party_DNS_services> "Domain name resolution")。

####  /etc/resolv.conf

NetworkManager 对 `/etc/resolv.conf` 的管理方式可以通过 `main.rc-manager` 选项配置。 [networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包 会把它设置为 `symlink`，而不是上游默认的 `auto`。 具体设置及其值在 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>) 手册页中有说明。 

**提示：** 使用 openresolv 可以让 NetworkManager 和其他管理 _resolvconf_ 的软件共存。比如如果要运行一个本地 DNS 缓存和拆分 DNS 解析器，openresoly可以提供一个 [subscriber](</wzh/index.php?title=Openresolv&action=edit&redlink=1> "Openresolv（页面不存在）")。不过将 NetworkManager 与 openresolv 一起使用时，要注意条件转发[仍未得到完全支持](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/153>)

_NetworkManager_ 还通过调度程序脚本提供钩子，可用于在网络变化后修改 `/etc/resolv.conf`。有关更多信息，请参见 [#使用 NetworkManager 调度网络服务](<#%E4%BD%BF%E7%94%A8_NetworkManager_%E8%B0%83%E5%BA%A6%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1>)和[NetworkManager(8)](<https://man.archlinux.org/man/NetworkManager.8>)。 

**注意：**

  * 如果 NetworkManager 被配置为使用 [dnsmasq](<#dnsmasq>) 或 [systemd-resolved](<#systemd-resolved>)，则相应的环回地址将写入 `/etc/resolv.conf`。
  * NetworkManager （要）写入 `/etc/resolv.conf` 的 `resolv.conf` 文件位于 `/run/NetworkManager/resolv.conf`。
  * `/run/NetworkManager/no-stub-resolv.conf` 中包含 NetworkManager 获取到的 DNS 服务器和搜索域。

#####  不让 NetworkManager 管理 /etc/resolv.conf

要防止 NetworkManager 修改 `/etc/resolv.conf`，请在 `/etc/NetworkManager/conf.d/` 下的配置文件中设置 `main.dns=none` 选项： 
    
    /etc/NetworkManager/conf.d/dns.conf
    
    [main]
    dns=none

**提示：** 你可能还想设置 `main.systemd-resolved=false`，这样 NetworkManager 就不会将 DNS 配置发送给 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")。

**注意：** 请参见 DNS 缓存和条件转发，以配置 NetworkManager 使用其他 DNS 后端，如 [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq") 和 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")，而不是使用 `main.dns=none`。

之后 `/etc/resolv.conf` 可能是一个损坏的符号链接，你需要将其删除。然后，重新创建一个新的 `/etc/resolv.conf` 文件。 

#####  使用 openresolv

**注意：** NetworkManager 不支持使用由 [systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包 提供的 systemd-resolved 的 _resolvconf_ 接口 ([resolvectl(1) § COMPATIBILITY WITH RESOLVCONF(8)](<https://man.archlinux.org/man/resolvectl.1#COMPATIBILITY_WITH_RESOLVCONF\(8\)>)) 

  * 在使用 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 时，请不要设置 `main.rc-manager=resolvconf`；而应该[正确创建一个 /etc/resolv.conf 的 symlink](<../zh-cn/Systemd-resolved.html#DNS> "Systemd-resolved") 或者 [将 NetworkManager 显式配置为使用 systemd 解析](<#systemd-resolved>).
  * 如果您没有使用 systemd-resolved ，请勿安装 [systemd-resolvconf](<https://archlinux.org/packages/?name=systemd-resolvconf>)包 软件包。除非 `systemd-resolved.service` 启动，否则它将破坏所有使用 resolconf 的网络软件（不仅仅是 NetworkManager）。

要将 NetworkManager 配置为使用 [openresolv](</wzh/index.php?title=Openresolv&action=edit&redlink=1> "Openresolv（页面不存在）")，请在 `/etc/NetworkManager/conf.d/` 目录下的配置文件中设置 `main.rc-manager=resolvconf`: 
    
    /etc/NetworkManager/conf.d/rc-manager.conf
    
    [main]
    rc-manager=resolvconf

###  防火墙

可以根据当前的连接[分配 firewalld 区域](<../zh-cn/Firewalld.html#%E4%BD%BF%E7%94%A8_NetworkManager_%E7%AE%A1%E7%90%86%E5%8C%BA%E5%9F%9F> "Firewalld")。例如，在工作时限制较多，在家时限制较少。 

也可以通过 [NetworkManager 调度](<#%E4%BD%BF%E7%94%A8_NetworkManager_%E8%B0%83%E5%BA%A6%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1>)实现。 

##  使用 NetworkManager 调度网络服务

有些服务只有联网时才有意义，例如 [NFS](<../zh-cn/NFS.html> "NFS"), [ SMB](<../zh-cn/Samba.html> "Samba") 和 [NTPd](<../zh-cn/Network_Time_Protocol_daemon.html> "Network Time Protocol daemon")。NetworkManager 可以在连接网络后启动这些服务，并在网络关闭时停止它们。 

要使用这一功能, 需要 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 并 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `NetworkManager-dispatcher.service`。 

服务启动后，可以将脚本加到 `/etc/NetworkManager/dispatcher.d` 目录。 

这些脚本必须属于 root, 否则不会被执行。为了安全起见, [所属](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "文件权限与属性")用户组也设置为 root: 
    
    # chown root:root /etc/NetworkManager/dispatcher.d/_10-script.sh_
    
而且脚本必须是[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable")的。 
    
    # chmod 755 _scriptname_
    
脚本将在连接网络时按字母表顺序运行，并在网络停止时反向停止。要保证启动顺序，可以在前面加数字，例如 `10_portmap` 或 `30_netfs` 这样就能保证 portmapper 在 NFS 挂载之前启动。 

脚本将接收如下参数： 

  * **Interface name:** 例如 `eth0`
  * **Action:** _up_ , _down_ , _vpn-up_ , _vpn-down_ , ... (完整列表请参考 [NetworkManager(8)](<https://man.archlinux.org/man/NetworkManager.8>))

**警告：** 如果没有连接到外部网络，请注意启动的服务和需要它们的程序。如果连接公共网络时启动了错误的服务，可能导致安全问题。

###  避免超时

如果一切运行良好, 那么这一节就可以跳过了。然而，如果你要运行的 dispatcher 脚本需要花费更多时间来运行，则可能出现一些问题。一开始，默认的内部超时时间为 3 秒，如果脚本未在该时间内执行完毕，则会被终止。后来这一超时被延长到大约 20 秒（参见 [Bugtracker](<https://bugzilla.redhat.com/show_bug.cgi?id=982734>)）。如果 20 秒仍然不够，那么您可以通过修改 dispatcher 服务文件 `/usr/lib/systemd/system/NetworkManager-dispatcher.service` 来让它在退出后保持活动。 
    
    /etc/systemd/system/NetworkManager-dispatcher.service
    
    .include /usr/lib/systemd/system/NetworkManager-dispatcher.service
    [Service]
    RemainAfterExit=yes

运行修改后的 `NetworkManager-dispatcher` 服务并将其设置为开机启动。 

**警告：** 加入了 `RemainAfterExit` 那一行后会让 dispatcher 一直运行。不幸的是, dispatcher **必须** 在再次运行脚本前被关闭。这意味着脚本只能被运行一次。因此, 除非超时确实引起了问题, 否则不要修改服务文件。

###  Dispatcher 示例

####  自动设置时区

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[System time#Update timezone every time NetworkManager connects to a network](<../zh-cn/System_time.html#Update_timezone_every_time_NetworkManager_connects_to_a_network> "System time")。**

**附注：** system time 页面中的示例看起来更简单。（在 [Talk:NetworkManager](<../zh-cn/Talk:NetworkManager.html>) 中讨论）

安装 [tzupdate](<https://aur.archlinux.org/packages/tzupdate/>)AUR 并创建一个可执行脚本： 
    
    /etc/NetworkManager/dispatcher.d/update-timezone.sh
    
    #! /bin/bash
    # 网络连接时自动设置时区
    iface=$1
    action=$2
    
    if [[ $iface != lo && $action == up ]]; then
        tz=$(tzupdate -s 1 -p 2>/dev/null)
        if [[ -n $tz && -r /usr/share/zoneinfo/$tz ]]; then
    	timedatectl set-timezone $tz
        fi
    fi
    
如果需要，可以将条件 `$iface != lo` 修改为匹配特定接口。 

####  使用 sshfs 挂载远程目录

由于该脚本在一个非常受限制的环境中运行, 为了连接上SSH agent, 你必须 export `SSH_AUTH_SOCK`。 这里有几种不同方式, 参照 [here](<https://bbs.archlinux.org/viewtopic.php?pid=1042030#p1042030>) 获取更多详细信息. 以下示例需要 gnome-keyring , 如果 gnome-keyring 没解锁,将需要你输入密码. 如果 NetworkManager 设置为登录后自动连接, 很有可能因为 _gnome-keyring_ 还没启动导致失败(转入睡眠). 对应的 UUID 可以通过命令 `nmcli con status` 或 `nmcli con list` 查得。 
    
    #!/bin/sh
    USER='username'
    REMOTE='user@host:/remote/path'
    LOCAL='/local/path'
    
    interface=$1 status=$2
    if [ "$CONNECTION_UUID" = "_uuid_ " ]; then
      case $status in
        up)
          # sleep 10
          SSH_AUTH_SOCK=$(find /tmp -maxdepth 1 -type s -user "$USER" -name 'ssh')
          export SSH_AUTH_SOCK
          su "$USER" -c "sshfs $REMOTE $LOCAL"
          ;;
        down)
          fusermount -u "$LOCAL"
          ;;
      esac
    fi
    
####  挂载 SMB 共享

一些 [SMB](<../zh-cn/Samba.html> "Samba") 共享仅在某些网络或位置（例如在家中）可用。您可以使用 dispatcher 脚本来仅挂载当前位置中存在的 SMB 共享。 

下面的脚本将检查我们是否连接到一个特定的网络，并挂载共享 : 
    
    /etc/NetworkManager/dispatcher.d/30-mount-smb.sh
    
    #!/bin/sh
    
    # Find the connection UUID with "nmcli connection show" in terminal.
    # All NetworkManager connection types are supported: wireless, VPN, wired...
    if [ "$2" = "up" ]; then
      if [ "$CONNECTION_UUID" = "uuid" ]; then
        mount /your/mount/point & 
        # add more shares as needed
      fi
    fi
    
以下脚本将在正常断开与特定网络的连接之前卸载所有 SMB 共享： 
    
    /etc/NetworkManager/dispatcher.d/pre-down.d/30-umount-smb.sh
    
    #!/bin/sh
    
    if [ "$CONNECTION_UUID" = "uuid" ]; then
      umount -a -l -t cifs
    fi
    
**注意：** 如上所示，请确保该脚本位于 `pre-down.d` 子目录中，否则它将在任何连接状态更改时卸载所有共享。

下面的脚本将尝试在意外断开与特定网络的连接后卸载所有 SMB 共享 : 
    
    /etc/NetworkManager/dispatcher.d/40-umount-smb.sh
    
    #!/bin/sh
    
    if [ "$CONNECTION_UUID" = "uuid" ]; then
      if [ "$2" = "down" ]; then
        umount -a -l -t cifs
      fi
    fi
    
**注意：**

  * 自 NetworkManager 0.9.8 起，关闭或重启时不会执行 _pre-down_ 和 _down_ 事件，详见 [该错误报告](<https://bugzilla.gnome.org/show_bug.cgi?id=701242>) 获取更多信息。
  * 之前的 _umount_ 脚本仍然可能导致实际访问挂载点的应用程序“挂起”。

另一种方法是使用 [NFS#Using a NetworkManager dispatcher](<../zh-cn/NFS.html#Using_a_NetworkManager_dispatcher> "NFS") 中的脚本 : 
    
    /etc/NetworkManager/dispatcher.d/30-smb.sh
    
    #!/bin/sh
    
    # Find the connection UUID with "nmcli con show" in terminal.
    # All NetworkManager connection types are supported: wireless, VPN, wired...
    WANTED_CON_UUID="CHANGE-ME-NOW-9c7eff15-010a-4b1c-a786-9b4efa218ba9"
    
    if [ "$CONNECTION_UUID" = "$WANTED_CON_UUID" ]; then
        
        # Script parameter $1: network interface name, not used
        # Script parameter $2: dispatched event
        
        case "$2" in
            "up")
                mount -a -t cifs
                ;;
            "down"|"pre-down"|"vpn-pre-down")
                umount -l -a -t cifs >/dev/null
                ;;
        esac
    fi
    
**注意：** 此脚本会忽略带有 `noauto` 选项的挂载，删除此挂载选项或使用 `auto` 选项来允许 dispatcher 管理这些挂载。

在 `/etc/NetworkManager/dispatcher.d/pre-down/` 目录下创建一个符号链接来捕获 `pre-down` 事件 : 
    
    # ln -s ../30-smb.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-smb.sh
    
####  挂载 NFS 共享

参见 [NFS#Using a NetworkManager dispatcher](<../zh-cn/NFS.html#Using_a_NetworkManager_dispatcher> "NFS"). 

####  当插入网线时用 dispatcher 脚本自动关闭无线网络

其想法是，仅当 LAN 电缆拔下时（例如，从笔记本电脑底座上拔下时）才打开 Wi-Fi，一旦 LAN 电缆再次插入，Wi-Fi 将自动禁用。 

创建以下 dispatcher 脚本 [[6]](<https://superuser.com/questions/233448/disable-wlan-if-wired-cable-network-is-available>)，并将其中的 `_LAN_interface_` 替换为您自己的网络接口。 

**注意：** 你可以使用 [nmcli](<#nmcli_examples>)（`nmcli d | grep ethernet`）来获取接口列表。以太网接口通常以 `en` 或 `eth` 开头，例如 `enp0s5` 或 `eth0`。

记得将脚本设置为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。你可以通过[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `NetworkManager.service`，运行 `ip a`，并检查 `wlp3s0`（或你的 Wi-Fi 接口名）是否处于 `state DOWN` 来验证脚本是否生效。如果遇到异常情况，请查看 `NetworkManager-dispatcher.service` 的[日志](</wzh/index.php?title=%E6%97%A5%E5%BF%97&action=edit&redlink=1> "日志（页面不存在）")。 
    
    /etc/NetworkManager/dispatcher.d/wlan_auto_toggle.sh
    
    #!/bin/sh
    
    if [ "$1" = "_LAN_interface_ " ]; then
        case "$2" in
            up)
                nmcli radio wifi off
                ;;
            down)
                nmcli radio wifi on
                ;;
        esac
    elif [ "$(nmcli -g GENERAL.STATE device show LAN_interface)" = "20 (unavailable)" ]; then
        nmcli radio wifi on
    fi

**注意：** 当电脑上次开机时局域网接口已连接，但关机期间又断开连接时，有一个故障保护机制。否则电脑重启后无线设备仍会保持关闭状态，加上局域网接口断开，就会导致没有网络连接。

####  使用 dispatcher 在网络连接建立后连接 vpn

此部分示例演示如果自动连接到NetworkManager已定义的vpn-connection.首先创建调度脚本定义vpn连接之后的事务 

**注意：** 要使用 `iwgetid`，需要安装 [wireless_tools](<https://archlinux.org/packages/?name=wireless_tools>)包。
    
    /etc/NetworkManager/dispatcher.d/vpn-up
    
    #!/bin/sh
    VPN_NAME="name of VPN connection defined in NetworkManager"
    ESSID="Wi-Fi network ESSID (not connection name)"
    
    interface=$1 status=$2
    case $status in
      up|vpn-down)
        if iwgetid | grep -qs ":\"$ESSID\""; then
          nmcli connection up id "$VPN_NAME"
        fi
        ;;
      down)
        if iwgetid | grep -qs ":\"$ESSID\""; then
          if nmcli connection show --active | grep "$VPN_NAME"; then
            nmcli connection down id "$VPN_NAME"
          fi
        fi
        ;;
    esac
    
如果想在任意 Wi-Fi 网络都可以自动连接 VPN, 你可以用这样给 ESSID 赋值: `ESSID=$(iwgetid -r)`。记住要给脚本设置相应的权限, 参见[上文](<#%E4%BD%BF%E7%94%A8_NetworkManager_%E8%B0%83%E5%BA%A6%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1>)。 

由于 [VPN secrets 保管方式的原因](<https://developer.gnome.org/NetworkManager/0.9/secrets-flags.html>), 连接依然可能会失败并且 `NetworkManager-dispatcher.service` 会报错 'no valid VPN secrets'。这样就需要用下面方法让脚本可以获取 VPN 密码: 

或者直接在 VPN 配置文件中加入 `vpn-secrets` 并写入密码: 

1\. 可以选择编辑 VPN 连接的配置文件让 NetworkManager 自己储存 secrets 而不是把 secrets 保存在[不能被root访问的](<https://bugzilla.redhat.com/show_bug.cgi?id=710552>) keyring 中: 打开 `/etc/NetworkManager/system-connections/_name of your VPN connection_`, 把 `password-flags` 以及 `secret-flags` 从 `1` 改为 `0`。 

如果还不行，需要在安全位置创建 `passwd-file`，权限和 dispatcher 脚本一致，并添加如下内容： 
    
    /path/to/passwd-file
    
    vpn.secrets.password:YOUR_PASSWORD
    
脚本也需要做出相应修改： 
    
    /etc/NetworkManager/dispatcher.d/vpn-up
    
    #!/bin/sh
    VPN_NAME="name of VPN connection defined in NetworkManager"
    ESSID="Wi-Fi network ESSID (not connection name)"
    
    interface=$1 status=$2
    case $status in
      up|vpn-down)
        if iwgetid | grep -qs ":\"$ESSID\""; then
          nmcli connection up id "$VPN_NAME" passwd-file /path/to/passwd-file
        fi
        ;;
      down)
        if iwgetid | grep -qs ":\"$ESSID\""; then
          if nmcli connection show --active | grep "$VPN_NAME"; then
            nmcli connection down id "$VPN_NAME"
          fi
        fi
        ;;
    esac
    
2\. 修改 `password-flags`，将密码加入配置文件的 `vpn-secrets` 部分: 
    
     [vpn]
     ....
     password-flags=0
     
     [vpn-secrets]
     password=_your_password_
    
**注意：** 可能需要打开配置界面，重新设置 VPN 密码。

####  用 dispatcher 来禁用 VPN 上的 IPv6 连接

许多商业 VPN 供应商仅支持 IPv4。这意味着所有 IPv6 流量都会绕过 VPN，使 VPN 变得毫无用处。为了避免这种情况，可以使用 dispatcher 在 VPN 连接启动时禁用所有 IPv6 流量。 
    
    /etc/NetworkManager/dispatcher.d/10-vpn-ipv6
    
    #!/bin/sh
    
    case "$2" in
    	vpn-up)
    		echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
    		;;
    	vpn-down)
    		echo 0 > /proc/sys/net/ipv6/conf/all/disable_ipv6
    		;;
    esac
    
作为替代方案，可以使用调度器（dispatcher）临时将 VPN 连接所用设备的 IPv6 模式设置为 `link-local`。这样可以避免 NetworkManager 产生大量关于 IPv6 被禁用的日志。如果有多个设备或连接提供 IPv6 连接，该脚本将无法正常工作，但可以调整脚本以遍历多个设备。请注意，任何对连接的更改（通过 [nmcli(1)](<https://man.archlinux.org/man/nmcli.1>) 或[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")）都会重新应用整个连接到设备，并重新启用 IPv6（如果连接中启用了 IPv6）。 
    
    /etc/NetworkManager/dispatcher.d/10-vpn-ipv6
    
    #!/bin/sh
    
    case "$2" in
    	vpn-up)
    		nmcli device modify "${DEVICE_IFACE}" ipv6.method link-local
    		;;
    	vpn-down)
    		nmcli device reapply "${DEVICE_IFACE}"
    		;;
    esac
    
####  启动 OpenNTPD

安装 [networkmanager-dispatcher-openntpd](<https://aur.archlinux.org/packages/networkmanager-dispatcher-openntpd/>)AUR 软件包 

####  使用 systemd-timesyncd 动态设置通过 DHCP 获取到的 NTP 服务器

当你在不同的网络之间漫游时 ( 例如公司的局域网，家里的 WiFi，以及不时出现的其他 WiFi) ，你可能需要把 timesyncd 使用的 NTP 服务器设置为 DHCP 提供的服务器。但是，NetworkManager 本身不能与 systemd-timesyncd 通信来设置 NTP 服务器。 

dispatcher 可以解决这个问题。 

[Create](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Create") the overlay directory for your systemd-timesyncd configuration `/etc/systemd/timesyncd.conf.d` if it does not already exist. Inside `/etc/NetworkManager/dispatcher.d`, put the following: 
    
    /etc/NetworkManager/dispatcher.d/10-update-timesyncd
    
    #!/bin/sh
    
    [ -z "$CONNECTION_UUID" ] && exit 0
    INTERFACE="$1"
    ACTION="$2"
    
    case $ACTION in
    up | dhcp4-change | dhcp6-change)
        [ -n "$DHCP4_NTP_SERVERS" ] || exit
        mkdir -p /etc/systemd/timesyncd.conf.d
        cat <<-THE_END >"/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
            [Time]
            NTP=$DHCP4_NTP_SERVERS
        THE_END
        systemctl restart systemd-timesyncd.service
        ;;
    down)
        rm -f "/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
        systemctl restart systemd-timesyncd.service
        ;;
    esac
    
每次 NetworkManager 设置新的网络连接（`ACTION=up`）或获得现有连接的一些更新（`ACTION=dhcp4-change` 或 `ACTION=dhcp6-change`），并且提供的连接数据包含有关 NTP 服务器（`DHCP4_NTP_SERVERS`）的信息时，都会将特定于连接的覆盖配置文件写入 `/etc/systemd/timesyncd.conf.d`，其中包含获取到的 NTP 服务器。每当连接被断开（`ACTION=down`）时，特定于连接的覆盖文件就会被删除。每次更改 systemd-timesyncd 的配置后，都会重新启动此服务以获取更新的配置。为每个连接使用单独的配置文件是为了避免 NetworkManager 并行管理两个或多个连接时，配置中的不同 NTP 服务器名称被覆盖，因为 `up`、`dhcp4-change`、`dhcp6-change` 和 `down` 操作可能以任意顺序出现。 

##  测试

NetworkManager 托盘组件被设计成开机自动启动，所以对大部分用户来说，并不需要过多配置。但是如果你手动停用旧有的网络设置断网，你需要测试一下 NetworkManager 是否正常工作。首先[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `NetworkManager.service`. 

有些托盘组件会提供给你一个 .desktop 文件以便通过系统菜单运行。如果没有，那你就需要通过命令或者注销重登录系统来让托盘组件运行。 一旦托盘组件运行了，它会自动请求网络连接并通过 DHCP 服务器来进行网络配置。 

在一些 non-xdg-compliant 窗口系统，比如在 [awesome](<../zh-cn/Awesome.html> "Awesome") 中启动 GNOME applet： 
    
    nm-applet --sm-disable &
    
如果需要静态 IP，你需要配置 NetworkManager。一般来说，在托盘图标上面点击右键，选择“编辑连接”即可。 

##  提示与技巧

###  加密的 Wi-Fi 密码

NetworkManager 默认会在 `/etc/NetworkManager/system-connections/` 中的连接文件当中以明文形式存储密码。要显示存储的密码，使用以下命令： 
    
    # grep -r '^psk=' /etc/NetworkManager/system-connections/
    
密码可以被文件系统中的 root 用户和通过 GUI（如 `nm-applet`）访问设置的用户访问。 

最好将密码以加密形式保存在密钥环中，而不是明文。这样做的缺点是必须为每个用户设置连接。 

更好的做法是以加密形式将密码存储在密钥环中而不是以明文形式存储，使用密钥环的缺点是需要为每一个用户单独配置连接。 

为了对密钥环进行读写操作，必须有一个可用的机密代理，比如： 

  * `nmcli` with the `--ask` option
  * [#前端](<#%E5%89%8D%E7%AB%AF>)中提及的任一图形界面

如果这两者都不可用，那么身份验证将失败，并提示错误 `no secrets: No agents were available for this request.`

####  使用 GNOME 密钥环

需要启动密钥环守护程序并解锁密钥环才能让之后的东西工作。 

此外，需要将 NetworkManager 配置为不存储所有用户的密码。使用 GNOME 的 [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包，从终端运行 `nm-connection-editor`，选择一个网络连接，单击 _编辑_ ，选择 _Wi-Fi 安全性_ 选项卡，单击密码的右图标并选择 _只为此用户存储密码_ 。 

####  使用 KDE Wallet

若使用 KDE 的 [plasma-nm](<https://archlinux.org/packages/?name=plasma-nm>)包，请单击该小部件，然后单击右上角的 _设置_ 图标，再单击网络连接，在 _常规配置_ 选项卡中，取消选中 _允许所有用户连接到此网络_ 。如果勾选该选项，即使正在运行 keyring 守护程序，密码仍将以明文形式存储。 

如果之前选择了该选项又取消勾选了，则可能必须首先使用 `重置` 选项才能使密码从文件中消失。或者，首先删除连接并重新设置它。 

###  通过 Wi-Fi 共享网络连接（移动热点）

使用 NetworkManager，您只要点击几下就可以共享你的 Internet 连接（例如，3G或者有线）。请注意 可能会干扰该功能。 

您需要一个支持 AP 模式的 Wi-Fi 卡，请参阅[软件接入点#无线网卡必须支持AP模式](<../zh-cn/%E8%BD%AF%E4%BB%B6%E6%8E%A5%E5%85%A5%E7%82%B9.html#%E6%97%A0%E7%BA%BF%E7%BD%91%E5%8D%A1%E5%BF%85%E9%A1%BB%E6%94%AF%E6%8C%81AP%E6%A8%A1%E5%BC%8F> "软件接入点")了解详细信息。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包 软件包。请注意 NetworkManager 会启动自己的独立于`dnsmasq.service`的 _dnsmasq_ 实例，作为 DHCP 服务器。有关注意事项，请参见 [#dnsmasq](<#dnsmasq>)。 

创建共享连接： 

  * 点击小部件并选择 _创建新无线网络_.
  * 按照向导操作（选择 WPA2 或更高版本，请确保使用至少 8 个字符长的密码，密码太短会创建失败）。 
    * 选择 Hotspot（热点） 或 Ad-hoc 作为 Wi-Fi 模式。

该连接将被保存供下次使用。 

**注意：** Android 不支持连接到 Ad-hoc 网络。要与 Android 共享连接，请使用基础结构模式（即将 Wi-Fi 模式设置为“热点”）。

###  通过以太网共享连接（作为WISP路由器）

场景：您的设备能通过 Wi-Fi 上网，并且您希望通过以太网与其他设备共享互联网连接，这一般被称为 WISP。 

要求： 

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[dnsmasq](<https://archlinux.org/packages/?name=dnsmasq>)包 软件包。请注意 NetworkManager 会启动自己的独立于`dnsmasq.service`的 _dnsmasq_ 实例，作为 DHCP 服务器。有关注意事项，请参见 [#dnsmasq](<#dnsmasq>)。
  * 您的互联网连接设备和其他设备通过合适的以太网电缆连接（这通常意味着网线直连或两者接到同一个交换机上）。
  * 防火墙没有阻止网络连接共享。

步骤： 

  * 在终端里运行 `nm-connection-editor`。
  * 添加新的以太网连接
  * 为新的连接起一个合适的名字
  * 转到 “IPv4 设置” 选项
  * 在“方法”下选择“共享给其他计算机”
  * 保存

现在，您应该可以在 NetworkManager 的有线连接列表中看到您新创建的连接。 

###  在cron任务（jobs）或脚本中检查网络是否连接

有些 _cron_ 任务需要可用的网络连接才能成功。你可能希望在网络不可用时避免运行这些任务。为此，添加一个网络的**if** 测试，该测试询问NetworkManager的 _nm-tool_ 并检查网状态。下面展示的测试当任何接口可用时成功，当所有借口都不可用时失败。对于可能连接有线，无线或者关闭网络的笔记本来说这很方便。 
    
    if [ $(nm-tool|grep State|cut -f2 -d' ') == "connected" ]; then
        #Whatever you want to do if the network is online
    else
        #Whatever you want to do if the network is offline - note, this and the else above are optional
    fi
    
例如，这对于一个运行 _fpupdate_ 来更新F-Prot病毒扫描签名的`cron.hourly`脚本很有帮助。另外，经过小的修改，使用 _nm-tool_ 输出的不同部分可以区分不同的网络；例如，因为活跃的无线网络连接有一个星号（asterisk'*'）表示，你可以grep网络名，然后grep星号。 

###  登录后自动解锁秘钥环

NetworkManager 默认不会连接到需要密码的网络，仅在登录后才会连接，要不登录就连接网络，请使用下面方式配置： 

  1. 在面板中右键点击 `nm-applet` 图标，选择“编辑连接”，然后打开“无线”标签页
  2. 选择你想操作的连接，点击“编辑”按钮
  3. 勾选“自动连接”和“对所有用户可用”选项
  4. 此外，确保在“Wi-Fi 安全性”下选择了“为所有用户保存密码（不加密）”

登出并重新登录，完成。 

###  有密码认证的KDE and OpenConnect VPN

虽然可以在连接时直接输入，[plasma-nm](<https://archlinux.org/packages/?name=plasma-nm>)包 0.9.3.2-1及以上版本还支持从 [KWallet](<../zh-cn/KDE_Wallet.html> "KWallet") 中获取OpenConnect用户名和密码。 

打开"KDE Wallet Manager"在"Network Management|Maps"下面查找你的OpenConnect VPN连接。点击"Show values"并在这个表的键值"VpnSecrets"下输入你的凭据（相应替代'username'和'password'）: 
    
    form:main:username%SEP%_username_ %SEP%form:main:password%SEP%_password_
    
下次你连接时，用户名和密码会出现在"VPN secrets"对话框中。 

###  忽略特定设备

有时，可能希望Networkmanager忽略特定的设备，并且不为他们配置地址和路由。通过在`/etc/NetworkManager/NetworkManager.conf`中使用下述配置，你可以快速轻松地按照MAC或者接口名忽略设备。 
    
    [keyfile]
    unmanaged-devices=mac:00:22:68:1c:59:b1;mac:00:1E:65:30:D1:C4;interface-name:eth0
    
填入上述内容后，执行 `# nmcli general reload` 后，应该能在NetworkManager不改变已完成设置的情况下配置接口。 

###  配置 MAC 地址随机化

**注意：** 有时候可能需要禁用 MAC 地址随机化功能以获得（稳定的）链路连接（比如[[7]](<https://bbs.archlinux.org/viewtopic.php?id=220101>)）。也有些网络会基于 MAC 地址来限制设备接入或限速。

MAC 地址随机化可以通过不向网络公开真实的 MAC 地址来提高隐私。 

NetworkManager 支持两种类型的 MAC 地址随机化：扫描期间的随机化和网络连接时的随机化。这两种模式都可以通过修改 `/etc/NetworkManager/NetworkManager.conf` 或在 `/etc/NetworkManager/conf.d/` 中创建单独的配置文件来配置，推荐使用后者，因为 NetworkManager 可能会覆盖前者的配置文件。 

Wi-Fi 扫描期间的随机化默认情况下是启用的，但是可以通过在 `/etc/NetworkManager/NetworkManager.conf` 或 `/etc/NetworkManager/conf.d` 下的专用配置文件中添加以下行来禁用 ： 
    
    /etc/NetworkManager/conf.d/wifi_rand_mac.conf
    
    [device]
    wifi.scan-rand-mac-address=no

可以为无线和以太网接口设置不同的网络连接时的 MAC 地址随机化模式。有关不同模式的更多细节，请参见 [GNOME 博客文章](<https://blogs.GNOME.org/thaller/2016/08/26/mac-address-spoofing-in-networkmanager-1-4-0/>)。 

在 MAC 地址随机化方面，最重要的模式是 `stable` 和 `random`。当您连接到新网络时，`stable` 会生成一个随机 MAC 地址，并将两者永久关联。这意味着您每次连接到该网络时都将使用相同的 MAC 地址。相比之下，`random` 每次连接到新的或以前已知的网络时都会生成一个新的 MAC 地址。您可以通过在 `/etc/NetworkManager/conf.d` 下添加所需配置来配置 MAC 随机化： 
    
    /etc/NetworkManager/conf.d/wifi_rand_mac.conf
    
    [device-mac-randomization]
    # "yes" is already the default for scanning
    wifi.scan-rand-mac-address=yes
     
    [connection-mac-randomization]
    # Randomize MAC for every ethernet connection
    ethernet.cloned-mac-address=random
    # Generate a random MAC for each WiFi and associate the two permanently.
    wifi.cloned-mac-address=stable

要为特定连接配置 MAC 地址随机化（例如，当网络不支持随机 MAC 地址时），请[编辑该连接](<#Edit_a_connection>)，将 `802-11-wireless.cloned-mac-address` 设置为其中一种模式（例如 `stable` 或 `random`）。 

参考这篇 [GNOME 博客文章](<https://blogs.gnome.org/thaller/2016/08/26/mac-address-spoofing-in-networkmanager-1-4-0/>)了解更多详情。 

###  启用IPv6隐私扩展

参见 [IPv6#NetworkManager](<../zh-cn/IPv6.html#NetworkManager> "IPv6")

###  给每个网络连接配置单独的 DUID

DHCPv6 唯一标识符（DUID）是 DHCPv6 客户端用于向 DHCPv6 服务器标识自身的值。NetworkManager 支持 3 种类型的 DUID： 

  * DUID-UUID ([RFC 6355](<https://tools.ietf.org/html/rfc6355> "rfc:6355")): 从通用唯一标识符（UUID）生成。
  * DUID-LL ([RFC 3315](<https://tools.ietf.org/html/rfc3315> "rfc:3315")): 从链路层地址 ( 即 MAC 地址 ) 生成。
  * DUID-LLT ([RFC 3315](<https://tools.ietf.org/html/rfc3315> "rfc:3315")): 从链路层地址加上时间戳生成。

如果使用了 NetworkManager 内置的 DHCP 客户端（默认如此），则他会使用从机器 ID (`/etc/machine-id`) 生成的 DUID 来标识自身。这意味着机器上的所有网络连接都用的是同一个 DUID，这可能会造成隐私泄露。 

幸运的是，NetworkManager 能够为每个连接提供唯一的 DUID，这些 DUID 来自连接的 stable-id 和每个主机的唯一密钥。您可以通过在 `/etc/NetworkManager/conf.d` 下添加以下配置来启用它 : 
    
    /etc/NetworkManager/conf.d/duid.conf
    
    [connection]
    ipv6.dhcp-duid=stable-uuid

该选项同时还支持 `stable-ll` 和 `stable-llt` 等值。有关更多信息，请阅读 [nm-settings(5) § ipv6 setting](<https://man.archlinux.org/man/nm-settings.5#ipv6_setting>) 中 `dhcp-duid` 的说明。 

###  有线连接的使用

默认情况下，NetworkManager 会为它发现的每个有线以太网连接生成一个连接配置文件。在生成连接时，它无法确定是否还有更多的以太网适配器可用。因此，它将第一个有线连接命名为“Wired connection 1”。你可以通过配置 `no-auto-default`（参见 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>)）来避免自动生成此连接，或者直接删除它。之后，NetworkManager 会记住不再为该接口生成连接。 

你也可以编辑该连接（并保存到磁盘）或删除它。NetworkManager 不会重新生成新的连接。然后你可以将连接名称改为你想要的任何名字。可以使用类似 [nm-connection-editor](<https://archlinux.org/packages/?name=nm-connection-editor>)包 的工具来完成这项任务。 

###  将 iwd 作为 Wi-Fi 后端

**注意：**

  * 不要启用 `iwd.service` 或手动配置 [iwd](<../zh-cn/Iwd.html> "Iwd"). NetworkManager 会开启并自我管理。
  * 切换到 iwd 之前要考虑到[已存在的问题](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues?scope=all&utf8=%E2%9C%93&state=opened&search=iwd>)

为了启用 [experimental iwd backend](<https://iwd.wiki.kernel.org/networkmanager>), 要首先[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [iwd](<https://archlinux.org/packages/?name=iwd>)包 并创建如下配置文件: 
    
    /etc/NetworkManager/conf.d/wifi_backend.conf
    
    [device]
    wifi.backend=iwd

你也可以选择安装 [networkmanager-iwd](<https://aur.archlinux.org/packages/networkmanager-iwd/>)AUR, 一个修改过的 _NetworkManager 包_ ，专门用于和 _iwd_ 共同工作，主要区别在于 _iwd_ 是必须的 但是 _wpa_supplicant_ 在构建后可以卸载。 

**注意：** 切换到 _iwd_ 之后，你可能需要[转换现有的 NetworkManager 网络配置文件](<https://iwd.wiki.kernel.org/networkmanager.html#converting_network_profiles>)

###  在网络命名空间中运行

如果你想在网络命名空间中运行 NetworkManager（例如，管理应由特定应用程序使用的设备），请在将设备移入命名空间之前先将其关闭： 
    
    $ ip link set dev _MY_DEVICE_ down
    $ ip link set dev _MY_DEVICE_ netns _MY_NAMESPACE_
    $ ip netns exec _MY_NAMESPACE_ NetworkManager
    ...
    $ ip netns exec _MY_NAMESPACE_ killall NetworkManager
    
否则，NetworkManager 之后会因 `device is strictly unmanaged` 错误而无法建立连接。 

###  自动连接 VPN

NetworkManager 可以设置为在连接到互联网时自动连接 VPN，且可以针对每个网络单独配置。VPN 连接本身可以通过 GNOME 的 NetworkManager 前端添加，但要实现自动使用 VPN，必须使用 `nmcli`。其他前端可能没有此限制。 

首先，确保将 VPN 连接设置为对所有用户可用。在 GNOME 中，这只需在 `details` 标签页下勾选一个选项。在 `Identity` 标签页中，点击密码字段右侧的图标，将其设置为 `为所有用户保存密码`。 

然后找到该 VPN 连接的 UUID，并将其添加到互联网连接的 `connection.secondaries` 中： 
    
    # UUID=$(nmcli --get-values connection.uuid connection show _VPN-连接名称_)
    # nmcli connection modify _互联网连接名称_ connection.secondaries "$UUID"
    
现在，当 NetworkManager 重启后，并且你连接了已配置的互联网连接，就会自动连接到 VPN。 

##  排错

###  安全 Wi-Fi 网络不提示输入密码

尝试连接到安全的 Wi-Fi 网络时，既不提示输入密码，也不建立连接。如果没有安装密钥环软件包，这种情况就会发生。一个简单的解决方案是安装 [gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包。如果希望密码以加密的形式存储，按照 [GNOME/Keyring](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring") 来设置 _gnome-keyring-daemon_ 。 

### Network management disabled

当 NetworkManager 关闭但 pid（state）文件未删除时，就会看到 `Network management disabled` 提示。此时，请手动删除文件： 
    
    # rm /var/lib/NetworkManager/NetworkManager.state
    
###  内置 DHCP 客户端的问题

如果在使用内置 DHCP 客户端获取 IP 地址时遇到问题，请考虑换一个 DHCP 客户端，有关说明，请参阅 [#DHCP 客户端](<#DHCP_%E5%AE%A2%E6%88%B7%E7%AB%AF>)。这种解决方法可能会解决大型无线网络（如 eduroam）中的问题。 

###  使用 dhclient 时的 DHCP 问题

如果在通过 DHCP 获取 IP 地址时遇到问题，尝试在 `/etc/dhclient.conf` 中添加以下内容： 
    
     interface "eth0" {
       send dhcp-client-identifier 01:_aa:bb:cc:dd:ee:ff_ ;
     }
    
其中 `_aa:bb:cc:dd:ee:ff_` 是网卡的 MAC 地址。MAC 地址可以使用 [iproute2](<https://archlinux.org/packages/?name=iproute2>)包 包中的 `ip link show _接口_` 命令获得。 

###  未检测到 3G 调制解调器

参见 [Mobile broadband modem#NetworkManager](</wzh/index.php?title=Mobile_broadband_modem&action=edit&redlink=1> "Mobile broadband modem（页面不存在）")。 

###  在笔记本电脑上关闭 WLAN

有时候在使用笔记本上的开关禁用 Wi-Fi 然后重新启用后，NetworkManager 无法工作。这常常是 _rfkill_ 的问题。要检查驱动程序是否已告知 _rfkill_ 无线适配器的状态，请使用： 
    
    $ watch -n1 rfkill list all
    
如果开启适配器后其标识符仍然显示为 blocked，可尝试如下命令手动 unblock（其中 X 是上面输出的标识符编号）： 
    
    # rfkill event unblock X
    
###  静态 IP 地址设置恢复为 DHCP

由于未解决的错误，将默认连接更改为静态 IP 地址时，`nm-applet` 可能无法正确存储配置更改，并将恢复为自动 DHCP。 

要解决这个问题，必须在 `nm-applet` 中编辑默认连接（例如 "Auto eth0"）、改变连接名称（例如改成 "my eth0"）、取消勾选"对所有用户可用"复选框并根据需要改变静态 IP 地址设置，最后点击**应用** 。这将保存一个具有给定名称的新连接。 

接下来，要让默认连接不自动连接。要做到这一点，请以 _非_ root 身份运行 `nm-connection-editor`。在连接编辑器中，编辑默认连接（例如 "Auto eth0"），取消勾选"自动连接"。点击**应用** ，然后关闭连接编辑器。 

###  普通用户无法编辑连接

参见 [#设置 PolicyKit 权限](<#%E8%AE%BE%E7%BD%AE_PolicyKit_%E6%9D%83%E9%99%90>)。 

###  忘记隐藏无线网络

由于隐藏网络不会显示在无线视图的选择列表中，因此无法使用 GUI 忘记（删除）它们。可以使用以下命令删除： 
    
    # rm /etc/NetworkManager/system-connections/_SSID_
    
这也适用于任何其他连接。 

###  GNOME 中 VPN 不工作

使用 GNOME 时，在 NetworkManager 中设置 OpenConnect 或 vpnc 连接时，有时不会看到弹出对话框，并且 `/var/log/errors.log` 中会出现以下错误： 
    
    localhost NetworkManager[399]: <error> [1361719690.10506] [nm-vpn-connection.c:1405] get_secrets_cb(): Failed to request VPN secrets #3: (6) No agents were available for this request.
    
这是由于 GNOME NetworkManager Applet 期望对话框脚本位于 `/usr/lib/gnome-shell`，而 NetworkManager 的包将它们放入 `/usr/lib/networkmanager`。 作为"临时"修复（这个错误已经存在一段时间了），请创建以下符号链接： 

  * 对于 OpenConnect：`ln -s /usr/lib/networkmanager/nm-openconnect-auth-dialog /usr/lib/gnome-shell/`
  * 对于 VPNC（即 Cisco VPN）：`ln -s /usr/lib/networkmanager/nm-vpnc-auth-dialog /usr/lib/gnome-shell/`

对其他的 NetworkManager VPN 插件可能也需要做类似的事情，不过以上两个最常见。 

###  无法连接到可见的欧洲无线网络

WLAN 芯片附带默认的[监管区域](</wzh/index.php?title=%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE&action=edit&redlink=1> "无线网络配置（页面不存在）")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]。如果接入点不在这些限制范围内运行，就无法连接到网络。解决这个问题很容易： 

  1. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [wireless-regdb](<https://archlinux.org/packages/?name=wireless-regdb>)包。
  2. 取消注释 `/etc/conf.d/wireless-regdom` 中正确的国家代码。
  3. 重新启动系统，因为该设置仅在启动时读取。

###  启动时自动连接到 VPN 不工作

当系统（即以 root 用户运行的 NetworkManager）尝试建立一个 VPN 连接时问题就会发生，因为密码存储在某一个特定用户的 GNOME Keyring 中，所以无法获取密码。 

一个解决办法是用明文存储 VPN 密码，如[#使用 dispatcher 在网络连接建立后连接 vpn](<#%E4%BD%BF%E7%94%A8_dispatcher_%E5%9C%A8%E7%BD%91%E7%BB%9C%E8%BF%9E%E6%8E%A5%E5%BB%BA%E7%AB%8B%E5%90%8E%E8%BF%9E%E6%8E%A5_vpn>) 步骤 (2.) 中所描述。 

如果使用 `nm-applet` GUI 中的新的"自动连接 VPN"选项，就不再需要使用步骤 (1.) 所描述的 dispatcher 自动连接。 

###  systemd 瓶颈

随着时间的推移，日志文件（`/var/log/journal`）可能会变得非常庞大。使用 NetworkManager 时，这可对启动性能产生大的影响，参考：[systemd#启动的时间太长](<../zh-cn/Systemd.html#%E5%90%AF%E5%8A%A8%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%AA%E9%95%BF> "Systemd")。 

###  **使用archinstall脚本创建的系统关机慢（并且关机时kde右下角弹窗报错）**

使用命令（`journalctl -p5` 按斜杠输入`Killing`） 
    
    输出结果 NetworkManager[38]: <error> [1685410869.7713] platform-linux: sysctl: failed to open
    
可以尝试使用以下方法（基本可以解决） 

`sudo systemctl disable NetworkManager.service`

`reboot`

`sudo systemctl start NetworkManager.service`

`sudo systemctl enable NetworkManager.service`

###  有规律的网络断开、延迟和丢包（WiFi）

NetworkManager 每 2 分钟扫描一次。 

有些 WiFi 驱动在已连接/关联的同时扫描基站会有问题。症状包括 VPN 断开/重连和丢包，以及页面无法加载但之后刷新没有问题。 

以 root 身份运行 `journalctl -f` 可以表明这种情况是否正在发生，类似下面的信息会在日志文件中以有规律的间隔出现： 
    
    NetworkManager[410]: <info>  (wlp3s0): roamed from BSSID 00:14:48:11:20:CF (my-wifi-name) to (none) ((none))
    
如果漫游不重要，可以通过在 WiFi 连接配置文件中锁定接入点的 BSSID 来禁用定期扫描行为。 

###  联想笔记本（IdeaPad、Legion 等）无法开启 Wi-Fi

部分联想机型存在 `ideapad_laptop` 模块的问题，原因是 Wi-Fi 驱动错误地报告了软阻塞。尽管仍可以使用 `netctl` 操作无线网卡，但 NetworkManager 等管理工具则会失效。你可以通过切换硬件开关后运行 `rfkill list`，如果软阻塞依然存在，就可以确认是此问题导致。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 尝试使用 `rfkill.default_state` 和 `rfkill.master_switch_mode`（参见 [kernel-parameters.html](<https://docs.kernel.org/admin-guide/kernel-parameters.html>)）来修复 rfkill 问题。（在 [Talk:NetworkManager](<../zh-cn/Talk:NetworkManager.html>) 中讨论）

[卸载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块") `ideapad_laptop` 模块应能解决此问题。（**警告** : 这可能会导致笔记本键盘和触控板也被禁用！） 

###  不把主机名推送到DHCP服务器

NetworkManager 默认会将主机名发送给 DHCP 服务器。 

要全局禁用向 DHCP 服务器发送主机名，请在 `/etc/NetworkManager/conf.d/` 下创建配置文件，设置 `ipv4.dhcp-send-hostname=false` 和 `ipv6.dhcp-send-hostname=false` 选项。例如： 
    
    /etc/NetworkManager/conf.d/dhcp-send-hostname.conf
    
    [connection]
    ipv4.dhcp-send-hostname=false
    ipv6.dhcp-send-hostname=false

要为特定连接禁用向 DHCP 服务器发送主机名（或者在全局禁用时为某连接启用此功能），请在该网络连接文件中添加： 
    
    /etc/NetworkManager/system-connections/_your_connection_file_.nmconnection
    
    ...
    [ipv4]
    dhcp-send-hostname=false
    ...
    [ipv6]
    dhcp-send-hostname=false
    ...

**注意：** 这些选项仅被默认的[内部 DHCP 客户端](<#DHCP%E5%AE%A2%E6%88%B7%E7%AB%AF>)支持。若使用 NetworkManager 配合 dhcpcd，要禁止发送主机名，请编辑 `/etc/dhcpcd.conf` 并在最后一行添加 `anonymous`。

###  nm-applet 在 i3wm 中消失

如果你使用 `xfce4-notifyd.service` 作为通知服务，则必须[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")该单元文件并添加以下内容： 
    
    /etc/systemd/user/xfce4-notifyd.service.d/display_env.conf
    
    [Service]
    Environment="DISPLAY=:0.0"

重新加载守护进程后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `xfce4-notifyd.service`。退出 i3 并重新启动，托盘中的 applet 应该会显示。 

###  找不到单元 dbus-org.freedesktop.resolve1.service

如果 `systemd-resolved.service` 没有启动，NetworkManager 会尝试通过 D-Bus 启动它，但会失败： 
    
    dbus-daemon[991]: [system] Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")
    dbus-daemon[991]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.resolve1.service': Unit dbus-org.freedesktop.resolve1.service not found.
    dbus-daemon[991]: [system] Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")
    
这是因为 NetworkManager 会尝试将 DNS 信息发送给 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")，即使在 [NetworkManager.conf(5)](<https://man.archlinux.org/man/NetworkManager.conf.5>) 中设置了 `main.dns=`。[[8]](<https://gitlab.freedesktop.org/NetworkManager/NetworkManager/commit/d4eb4cb45f41b1751cacf71da558bf8f0988f383>)

可以通过在 `/etc/NetworkManager/conf.d/` 中添加配置文件来禁用此行为： 
    
    /etc/NetworkManager/conf.d/no-systemd-resolved.conf
    
    [main]
    systemd-resolved=false

参见 [FS#62138](<https://bugs.archlinux.org/task/62138>)。 

###  需要密钥但未提供

如果你在尝试连接到网络时收到以下错误： 
    
    $ nmcli device wifi connect _SSID_ password _password_
    
    Error: Connection activation failed: (7) Secrets were required, but not provided
    
此错误可能有多种原因，建议查看 [journal](<../zh-cn/Systemd/Journal.html> "Journal")（使用 `-u NetworkManager` 过滤）。例如，如果 NetworkManager 建立连接耗时过长，它可能会认为密码错误： 
    
    NetworkManager[1372]: <warn>  [1643991888.3808] device (wlan0): Activation: (wifi) association took too long
    NetworkManager[1372]: <info>  [1643991888.3809] device (wlan0): state change: config -> need-auth (reason 'none', sys-iface-state: 'managed')
    NetworkManager[1372]: <warn>  [1643991888.3838] device (wlan0): Activation: (wifi) asking for new secrets
    
你可以尝试删除该连接配置文件并重新创建一个： 
    
    $ nmcli connection delete _SSID_
    $ nmcli device wifi connect _SSID_ password _password_
    
也可以尝试禁用 MAC 地址随机化： 
    
    /etc/NetworkManager/conf.d/wifi_rand_mac.conf
    
    [device]
    wifi.scan-rand-mac-address=no

###  WPA Enterprise 连接（使用 iwd 后端）

如果你在使用 NetworkManager 的 [iwd 后端](<#Using_iwd_as_the_Wi-Fi_backend>)连接类似 'eduroam' 的 WPA Enterprise 网络，会出现以下错误： 
    
     Connection 'eduroam' is not avialable on device wlan0 because profile is not compatible with device (802.1x connections must have IWD provisioning files)
    
这是因为 NetworkManager 无法配置 WPA Enterprise 网络。你必须使用 iwd 的配置文件来配置它，例如放在 `/var/lib/iwd/_essid_.8021x`，详见 [iwd#WPA Enterprise](<../zh-cn/Iwd.html#WPA_Enterprise> "Iwd")。 

###  请求 VPN 密钥失败

如果你收到以下错误： 
    
    Failed to request VPN secrets #1: No agents were available for this request.
    
可能是因为密码为空，或你需要[配置 PolicyKit 权限](<#Set_up_PolicyKit_permissions>)。 

###  OpenVPN 连接失败并显示 “secrets: failed to request VPN secrets” 警告

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** 此段不适合作为排查问题章节。pacman 会指出可选依赖，如果还不清楚，应归入 [#VPN support](<#VPN_support>)。 (在 [Talk:NetworkManager#Remove unnecessary section 8.22](<../zh-cn/Talk:NetworkManager.html#Remove_unnecessary_section_8.22> "Talk:NetworkManager") 讨论)

包 [networkmanager-openvpn](<https://archlinux.org/packages/?name=networkmanager-openvpn>)包 在 GNOME-Shell 集成时需要依赖 [libnma-gtk4](<https://archlinux.org/packages/?name=libnma-gtk4>)包，并可选依赖 [libnma](<https://archlinux.org/packages/?name=libnma>)包（Gtk3）。如果系统缺少 [libnma](<https://archlinux.org/packages/?name=libnma>)包，系统日志会打印如下信息： 
    
    NetworkManager[642]: <warn>  [...] vpn[..."name_of_vpn_profile VPN"]: secrets: failed to request VPN secrets #3: No agents were available for this request.
    
### Failed to request VPN secrets

If you get this error: 
    
    Failed to request VPN secrets #1: No agents were available for this request.
    
It is either because the password is empty or you have to [set up PolicyKit permissions](<#Set_up_PolicyKit_permissions>). 

###  OpenVPN 连接失败报 OpenSSL “ca md too weak” 错误

自从 [openssl](<https://archlinux.org/packages/?name=openssl>)包 升级到版本 3 后，使用遗留加密算法生成的证书默认将被拒绝。通过 [networkmanager-openvpn](<https://archlinux.org/packages/?name=networkmanager-openvpn>)包 使用此类证书时，日志可能出现以下错误： 
    
    nm-openvpn[14359]: OpenSSL: error:0A00018E:SSL routines::ca md too weak
    nm-openvpn[14359]: Cannot load certificate file /home/archie/.local/share/networkmanagement/certificates/my_issued_cert.crt
    nm-openvpn[14359]: Exiting due to fatal error
    
正确的做法是让 OpenVPN 服务器管理员生成并重新签发更安全的证书。但作为临时解决方案，OpenVPN 需要指定： 

`

**模板错误：** 您在尝试使用 = 标志吗？ 有关解决方法，请访问 [Help:Template#Escape template-breaking characters](<../zh-cn/Help:%E6%A8%A1%E6%9D%BF.html#Escape_template-breaking_characters> "Help:Template")。

`

虽然 GUI 插件可能无法设置，但可以使用 nmcli 实现。此外，你还需要启用 OpenSSL 的 “legacy” 提供器。 

首先，通过以下命令获取有问题的 VPN 连接名称： 
    
    $ nmcli connection show
    
假设连接名为 _vpn.example.com_ ，使用 nmcli 格式如下： 
    
    $ nmcli connection modify vpn.example.com +vpn.data tls-cipher=DEFAULT:@SECLEVEL=0
    
此更改将立即反映在 `/etc/NetworkManager/system-connections/vpn.example.com.nmconnection` 文件中。 

接着，编辑 `/etc/ssl/openssl.cnf` 来启用 legacy provider（参见 OpenSSL wiki）： 

在文件末尾的 provider_sect 部分添加： 
    
    /etc/ssl/openssl.cnf
    
    openssl_conf = openssl_init
    
    [openssl_init]
    providers = provider_sect
    
    [provider_sect]
    default = default_sect
    legacy = legacy_sect
    
    [default_sect]
    activate = 1
    
    [legacy_sect]
    activate = 1

最后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `NetworkManager.service` 以使新的 OpenSSL 配置生效。 

###  WPA Enterprise 连接因 OpenSSL "unsupported protocol" 报错而验证失败

自 [openssl](<https://archlinux.org/packages/?name=openssl>)包 升级至版本 3 起，默认情况下 “SSL 3、TLS 1.0、TLS 1.1 和 DTLS 1.0 仅在安全等级 0 时可用”。[参见 OpenSSL 发布说明](<https://www.openssl.org/news/openssl-3.0-notes.html>)。尝试连接仅支持旧协议的 Wi-Fi 网络时，日志中可能会出现如下错误： 
    
    wpa_supplicant[3320]: SSL: SSL3 alert: write (local SSL3 detected an error):fatal:protocol version
    wpa_supplicant[3320]: OpenSSL: openssl_handshake - SSL_connect error:0A000102:SSL routines::unsupported protocol
    wpa_supplicant[3320]: wlp3s0: CTRL-EVENT-EAP-FAILURE EAP authentication failed
    
正确的做法是说服机构的管理员升级加密的网络隧道协议到 TLS 1.3，并可选择性地放弃对已弃用的安全标准（包括 TLS 1.0/1.1、DTLS 1.0 和 SSL 1-3）的支持。不过，作为临时解决方案，有多种方法可以默认启用 TLS 1.0 和/或 1.1。 

其中一种方法是手动打补丁或还原 OpenSSL 中导致此问题的更改（[[9]](<https://github.com/openssl/openssl/commit/7bf2e4d7f0c7ae19b7a8c416910886a7171e9820>)）。由于这也会降低所有使用 OpenSSL 安全级别 1 的程序的安全性，因此不推荐该方法。 

更好的方法是单独为 `wpa_supplicant` 设置使用的安全等级，如 [BBS#286417](<https://bbs.archlinux.org/viewtopic.php?id=286417#p2104492>) 所述。若仅修改受影响的连接，可以在连接的配置文件的 `[802-1x]` 部分设置 `phase1-auth-flags=32` 或 `phase1-auth-flags=64`。这可能无法通过图形界面完成，但可使用 `nmcli`。 

首先，使用以下命令获取出问题的连接名称： 
    
    $ nmcli connection show
    
假设该连接使用 TLS 1.0，名称为 _Example Wi-Fi_ ，则执行： 
    
    $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 32
    
若为 TLS 1.1，则执行： 
    
    $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 64
    
**注意：** 输入的数字是由 2 的 n 次方计算而得。这里，**n** 是从右到左计算的“网络验证字节”索引。设定第 5 个位元（2⁵ = 32）可启用 TLS 1.0，设定第 6 个位元（2⁶ = 64）可启用 TLS 1.1。

此更改将立即反映到 `/etc/NetworkManager/system-connections/Example Wi-Fi.nmconnection` 文件中。 

最后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `NetworkManager.service` 以使新的 OpenSSL 设置生效。 

##  参见

  * [NetworkManager for Administrators Part 1](<https://blogs.gnome.org/dcbw/2015/02/16/networkmanager-for-administrators-part-1/>)
  * [Wikipedia:NetworkManager](<https://en.wikipedia.org/wiki/NetworkManager> "wikipedia:NetworkManager")
  * [NetworkManager 官方网站](<https://networkmanager.dev/>)
