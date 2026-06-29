**翻译状态：**

  * 本文（或部分内容）译自 [Xrdp](<https://wiki.archlinux.org/title/Xrdp> "arch:Xrdp")，最近一次同步于 2023-08-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xrdp?diff=0&oldid=783264>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xrdp_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**xrdp** 是一个守护程序，支持 Microsoft 的 [Remote Desktop Protocol](<https://en.wikipedia.org/wiki/Remote_Desktop_Protocol> "wikipedia:Remote Desktop Protocol") (RDP)。 它使用 Xvnc 或 xorgxrdp 作为其后端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xrdp](<https://aur.archlinux.org/packages/xrdp/>)AUR 软件包 (或是选择开发版本 [xrdp-git](<https://aur.archlinux.org/packages/xrdp-git/>)AUR)。这仅支持XVNC作为后端。 

###  Xorg 后端

要使用 xorgxrdp 代替后端，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorgxrdp](<https://aur.archlinux.org/packages/xorgxrdp/>)AUR 包。 

将 `allowed_users=anybody` 添加到 `/etc/X11/Xwrapper.config` 以允许任何人启动 X 服务器。 

##  使用说明

首先，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `xrdp` 服务。您应该能够将 RDP 客户端连接到默认 RDP 端口 (3389) 上的主机。如果成功，您将看到“xrdp”会话管理器窗口，该窗口允许您在“Xorg”或“Xvnc”会话之间进行选择，并为用户身份验证提供输入。通过修改 `/etc/xrdp/xrdp.ini` 可以高度自定义会话管理器 UI。 

用于启动 _Xorg_ 和 _Xvnc_ 显示服务器的参数可以在 `/etc/xrdp/sesman.ini` 中配置。 

成功启动显示服务器后， _xrdp_ 将默认执行 `/etc/xrdp/startwm.sh`。该脚本用于启动一个窗口管理器（类似于 [.xinitrc](</wzh/index.php?title=.xinitrc&action=edit&redlink=1> ".xinitrc（页面不存在）")），如果它们从 `~/.xinitrc` 或 `/etc/X11/xinit/xinitrc` 读取存在。建议编辑 `~/.xinitrc` 以启动您的桌面环境或窗口管理器，但您也可以编辑 `/etc/xrdp/startwm.sh`。 

如果您只是关闭会话窗口和 RDP 连接，您可以在下次连接 RDP 时再次访问同一会话。当您从会话窗口退出窗口管理器或桌面环境时，会话将关闭，下次将打开一个新会话。 

##  技巧和窍门

###  开机自动启动

[xrdp](<https://aur.archlinux.org/packages/xrdp/>)AUR 软件包包含 systemd 的服务文件。[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `xrdp.service`。 

###  图形加速

对于 Xorg 会话，您可以通过为 Intel 和 AMD GPU 安装 [xorgxrdp-glamor](<https://aur.archlinux.org/packages/xorgxrdp-glamor/>)AUR 和为 Nvidia GPU 安装 [xorgxrdp-nvidia](<https://aur.archlinux.org/packages/xorgxrdp-nvidia/>)AUR 来启用 [OpenGL](<../zh-cn/OpenGL.html> "OpenGL") 和 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 图形加速。 

###  声卡

安装必要的 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 与 [pulseaudio-module-xrdp](<https://aur.archlinux.org/packages/pulseaudio-module-xrdp/>)AUR 模块或者 [PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 与 [pipewire-module-xrdp](<https://aur.archlinux.org/packages/pipewire-module-xrdp/>)AUR。 

###  非 root 用户

在 `Xwrapper.config` 中添加如下内容: 
    
    /etc/X11/Xwrapper.config
    
    allowed_users=anybody
    needs_root_rights=no

如果没有上面的内容，从 [Remmina](<../zh-cn/Remmina.html> "Remmina") 等程序发起的远程连接将会出现空白屏幕。 

##  疑难解答

###  X server could not be started并且日志中有waitforx字样

由于 waitforx 的测试版本不稳定[[1]](<#cite_note-1>)，可以将 `/usr/lib/xrdp/waitforx`备份后，编辑新文件`waitforx`： 
    
    #!/bin/sh
    exit 0
    
保存后设置775权限。或者[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xrdp-git](<https://aur.archlinux.org/packages/xrdp-git/>)AUR 包。 

###  光标周围的黑框

如果您在鼠标指针周围遇到黑框，请使用 `Xcursor.core:1` 行创建 `~/.Xresources-xrdp` 并将其加载到 `~/.xinitrc` 中，例如 
    
    xrdb ~/.Xresources-xrdp
    exec startlxde
    
您可能需要安装 [xorg-xrdb](<https://archlinux.org/packages/?name=xorg-xrdb>)包。 

###  黑屏

如果您的 `~/.xinitrc` 在 `dbus_args` 中设置了 `--exit-with-session`，则登录会话管理器后可能会出现黑屏。 

尝试将 `~/.xinitrc` 复制到 `~/.xrdpinitrc`，删除 `--exit-with-session`，然后更新 `/etc/xrdp/startwm.sh` 调用 `~/.xrdpinitrc` 而不是 `~/.xinitrc`。您可能需要将您的桌面环境添加到对 .xrdpinitrc 的调用中，如 ~/.xinitrc 中所述；例如 `. ~/.xrdpinitrc xfce`。 

###  桌面环境的黑屏

如果使用桌面环境出现黑屏，则可能是 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 未正确初始化造成的。一些桌面环境(例如 KDE Plasma) 可能会从之前的会话中恢复应用程序和窗口，所以结果是只缺失了 "plasmashell"。 

尝试使用 `~/.xinitrc` 文件中的 `dbus-launch --exit-with-session` 运行桌面环境。对于 KDE Plasma，您可以使用命令 `/usr/lib/plasma-dbus-run-session-if-needed startplasma-x11` 或者 `dbus-launch --exit-with-session startplasma-x11`。 

###  loginctl 或 systemctl --user 不工作

尝试注释掉 `/etc/pam.d/system-auth` 中对 `systemd-home` 的所有引用。请参阅[这个问题](<https://github.com/neutrinolabs/xrdp/issues/1684>)。 

###  gnome-keyring 或 KDE Wallet 提示

如果在会话开始时提示您登录 gnome-keyring 或 [KDE Wallet]，请修改文件 `/etc/pam.d/xrdp-sesman` 如下： 
    
    /etc/pam.d/xrdp-sesman
    
    #%PAM-1.0
    
    auth            include         system-remote-login
    **-auth           optional        pam_gnome_keyring.so**
    **-auth   optional  pam_kwallet5.so**
    
    account         include         system-remote-login
    
    password        include         system-remote-login
    **-password       optional        pam_gnome_keyring.so use_authtok**
    
    **session         optional        pam_keyinit.so force revoke**
    session         include         system-remote-login
    **-session                optional        pam_gnome_keyring.so auto_start**
    **-session  optional  pam_kwallet5.so auto_start**

如果您只使用 gnome-keyring，则不需要包含 kwallet5 行，反之亦然。 

###  阻止自动启动项目启动

要阻止用户定义的 `~/.config/autostart` 项目启动，您可以在 `~/.xinitrc` 中的会话上设置自动启动目录参数以仅使用全局 ` /etc/xdg/autostart` 目录。 
    
    get_session(){
        local dbus_args=(--sh-syntax)
        case "$SESSION" in
            awesome) dbus_args+=(awesome) ;;
            bspwm) dbus_args+=(bspwm-session) ;;
            budgie) dbus_args+=(budgie-desktop) ;;
            cinnamon) dbus_args+=(cinnamon-session -a /etc/xdg/autostart) ;;
    
###  没有声音

这可能是 _loginctl_ 问题的征兆，因此请尝试以[以上内容](<#loginctl_%E6%88%96_systemctl_--user_%E4%B8%8D%E5%B7%A5%E4%BD%9C>)修复。系统[journal](<../zh-cn/Systemd/Journal.html> "Journal")可能会遇到以下错误： 
    
    Failed to load module "module-x11-publish" (argument: "display=:10.0 xauthority="): initialization failed.
    
这是 _systemd_ 不正确地启动 PulseAudio 的结果。一种解决方法是为您自己的用户或所有用户[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用") [user unit](<../zh-cn/User_unit.html> "User unit") 文件 `pulseaudio.service` 和 `pulseaudio.socket`，然后启动 PulseAudio需要时通过在 `/etc/pulse/client.conf` 中将 `autospawn` 设置为 `yes`。 

如果仍然没有声音，请尝试使用 `~/.xinitrc` 中的 `pulseaudio &` 手动启动 PulseAudio。 

###  两指滚动过快

使用 xorg 后端，确保 xorgxrdp 版本 0.9.19 或更新。然后添加 `XRDP_XORG_TOUCHPAD_SCROLL_HACK=yes` 到 `/etc/xrdp/sesman.ini` 中的 `[SessionVariables]` 段 。 

参见[此问题](<https://github.com/neutrinolabs/xorgxrdp/issues/150>)以获得详细信息。 

###  远程系统的功能限制

远程用户的权限可能会比直接登录用户的权限要低。需要额外的 [polkit](<../zh-cn/Polkit.html> "Polkit") 权限配置策略： 

####  挂载的设备

要远程访问挂载的设备，请参考 [udisks#Permissions](<../zh-cn/Udisks.html#Permissions> "Udisks"). 

#### NetworkManager

要远程访问网络管理器，请阅读 [NetworkManager#Set up PolicyKit permissions](<../zh-cn/NetworkManager.html#Set_up_PolicyKit_permissions> "NetworkManager")。 

##  参阅

  * [TigerVNC](<../zh-cn/TigerVNC.html> "TigerVNC") \- VNC，一个 RDP 的替代品，同时在此用作后端
  * [freerdp](<https://archlinux.org/packages/?name=freerdp>)包 一个支持 RDP 7.1 功能的 rdesktop 分支，包括网络级身份验证 (NLA)。它主要由 `xfreerdp` 客户端组成。此外，`freerdp-shadow-cli` 命令提供了一种快速简便的方法来启动 RDP 服务器。

  1. [↑](<#cite_ref-1>) <https://github.com/neutrinolabs/xrdp/issues/2788>
