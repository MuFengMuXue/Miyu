**翻译状态：**

  * 本文（或部分内容）译自 [SDDM](<https://wiki.archlinux.org/title/SDDM> "arch:SDDM")，最近一次同步于 2025-02-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/SDDM?diff=0&oldid=826773>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SDDM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [KDE](<../zh-cn/KDE.html> "KDE")

[Simple Desktop Display Manager](<https://github.com/sddm/sddm/>) (SDDM) 是一个[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")。它是 [KDE](<../zh-cn/KDE.html> "KDE") Plasma 和 [LXQt](<../zh-cn/LXQt.html> "LXQt") 桌面环境推荐的显示管理器。 

[Wikipedia:Simple Desktop Display Manager](<https://en.wikipedia.org/wiki/Simple_Desktop_Display_Manager> "wikipedia:Simple Desktop Display Manager") 介绍： 

    Simple Desktop Display Manager (SDDM) 是用于 X11 和 Wayland 视窗系统的显示管理器（图形登录程序与会话管理器）。SDDM 使用 C++11 从头编写并支持通过 QML 改变主题。

[KDE](<../zh-cn/KDE.html> "KDE") 开发团队已接受了将 SDDM 项目整合到 Plasma 桌面项目中的 [issue](<https://invent.kde.org/plasma/plasma-desktop/-/issues/91>)。SDDM 将成为 Plasma 的官方组成部分，并且其更新可能会与 Plasma 桌面更新一起推出。 

**注意：** 截止至 SDDM 0.20 版本，[Wayland](<../zh-cn/Wayland.html> "Wayland") 会话能够被列出，并可从 SDDM 启动，但 SDDM 登录界面本身默认仍在 X11 模式下运行，不过[可以启用](<#Wayland>)试验性的 Wayland 登录界面。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sddm](<https://archlinux.org/packages/?name=sddm>)包。可选安装 [sddm-kcm](<https://archlinux.org/packages/?name=sddm-kcm>)包 或 [qt5-declarative](<https://archlinux.org/packages/?name=qt5-declarative>)包 以分别启用对 [KConfig Module](<../zh-cn/KDE.html#KCM> "KDE") 或 Qt5 的支持。 

然后根据[显示管理器#加载显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%8A%A0%E8%BD%BD%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8> "显示管理器")的说明配置 SDDM 在系统引导时启动。 

##  配置

SDDM 的默认配置文件为 `/usr/lib/sddm/sddm.conf.d/default.conf`。要修改配置，请在 `/etc/sddm.conf.d/` 目录下创建配置文件。详见 [sddm.conf(5)](<https://man.archlinux.org/man/sddm.conf.5>) 以获得所有配置选项。 

[sddm-kcm](<https://archlinux.org/packages/?name=sddm-kcm>)包 软件包 (包含在 [plasma](<https://archlinux.org/groups/x86_64/plasma/>)包组 用户组) 提供了一个图形用户界面以在 Plasma 系统设置中配置 SDDM。[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中也有基于 [Qt](<../zh-cn/Qt.html> "Qt") 的配置软件 [sddm-conf-git](<https://aur.archlinux.org/packages/sddm-conf-git/>)AUR。 

一切东西都应该开箱即用，自从 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 后，SDDM 默认使用 `systemd-logind` 以进行会话管理。 

###  自动登录

SDDM 通过它的配置文件来支持自动登录，例如： 
    
    /etc/sddm.conf.d/autologin.conf
    
    [Autologin]
    User=john
    Session=plasma

此配置使得在系统启动后自动以用户 `john` 开启一个 KDE Plasma 会话。X 的会话类型位于 `/usr/share/xsessions/`， wayland 的会话类型位于 `/usr/share/wayland-sessions/`。 

要在登录 KDE Plasma 的同时锁定会话，请参阅 [KDE#锁屏](<../zh-cn/KDE.html#%E9%94%81%E5%B1%8F> "KDE")。 

###  无密码登录

可以配置 SDDM 以允许在不需要密码的情况下登录到某些账户。与自动登录不同，用户仍需要选择要登录的账户，并且它与简单地将账户密码设置为空字符串不同，因为它只允许交互式用户登录（而不是，例如，通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 远程登录的用户）。 

SDDM 通过 [PAM](<../zh-cn/PAM.html> "PAM") 运行，因此您必须配置 PAM 的 SDDM 配置： 
    
    /etc/pam.d/sddm
    
    #%PAM-1.0
    
    **auth        sufficient  pam_succeed_if.so user ingroup nopasswdlogin**
    
    auth        include     system-login
    
    ...

也是为了能在没有密码的情况下解锁 KDE Plasma 锁屏，同样在`/etc/pam.d/kde`文件的顶部添加相同的行： 
    
    /etc/pam.d/kde
    
    #%PAM-1.0
    
    **auth        sufficient  pam_succeed_if.so user ingroup nopasswdlogin**
    
    auth        include     system-login
    
    ...

然后，只有`nopasswdlogin`组的成员，才能在不输入密码的情况下交互式登录： 
    
    # groupadd -r nopasswdlogin
    
    # gpasswd -a _username_ nopasswdlogin
    
###  登录后自动解锁 KDE Wallet

详见 [KDE Wallet#在登录时自动解锁 Kwallet](<../zh-cn/KDE_Wallet.html#%E5%9C%A8%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E8%A7%A3%E9%94%81_Kwallet> "KDE Wallet")。 

###  主题设置

在 `[Theme]` 小节更改主题设置。如果您使用 Plasma 的系统设置，主题可能会显示预览。 

设置 `breeze` 以获得 Plasma 默认主题。 

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 有一些可用的主题，例如 [archlinux-themes-sddm](<https://aur.archlinux.org/packages/archlinux-themes-sddm/>)AUR。 

####  当前主题

通过 `Current` 的值设置当前主题，例如 `Current=archlinux-simplyblack`。 

####  创建主题

默认 SDDM 主题目录为 `/usr/share/sddm/themes/`。你可以添加你的自制主题到该目录下一个单独的子目录中。注意 SDDM 要求这些子目录的名字要与主题的名字一致。可以通过研究已安装的文件来更改或创建属于你的主题。 

####  自定义主题

要覆盖 `theme.conf` 配置文件中的设置，在相同目录下创建一个自定义的 `theme.conf.user` 文件。例如，要更改主题的背景： 
    
    /usr/share/sddm/themes/_name_ /theme.conf.user
    
    [General]
    
    background=_/path/to/background.png_

####  测试（预览）主题

如果需要，你可以预览一个 SDDM 主题。如果你想知道一个主题看起来怎么样，或是想要编辑一个主题后在不必登出的情况下观察改动的效果，那么这将会非常有用。你可以运行下面的命令： 
    
    $ sddm-greeter-qt6 --test-mode --theme /usr/share/sddm/themes/breeze
    
这应该为所有已连接的显示器打开一个新窗口以显示主题的预览。 

**注意：** 这只是一个预览。在这个模式下，一些动作如关机、挂起或登录将不会执行。

####  鼠标光标

要设置鼠标光标的主题，将 `CursorTheme` 设置成您喜欢的光标主题。 

合法的 [Plasma](<../zh-cn/KDE.html> "Plasma") 鼠标光标主题有 `breeze_cursors`，`Breeze_Snow` 和 `breeze-dark`。 

####  用户图标（头像）

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** SDDM 现在无需配置即可检测到 `/var/lib/AccountsService/icons/` 中的图标，而 Plasma 不再在 `$HOME/` 中创建文件。 (在[Talk:SDDM](<../zh-cn/Talk:SDDM.html>)讨论)

SDDM 对于每个用户从相应的 `~/.face.icon` 目录下读取 PNG 图片格式的用户图标（即“头像”），或者从 SDDM 配置文件中由 `FacesDir` 为所有用户定义的共有位置。配置设置可以通过修改 `/etc/sddm.conf` 文件被直接替换，更好的方法是创建一个位于 `/etc/sddm.conf.d/` 下的文件来修改，例如 `/etc/sddm.conf.d/avatar.conf`。 

要使用 `FacesDir` 选项来确定头像位置，即在配置文件中 `FacesDir` 所确定的位置为每一个用户放置一个 PNG 图片，命名如 `_username_.face.icon`。`FacesDir` 默认的路径为 `/usr/share/sddm/faces/`。你可以更改默认 `FacesDir` 目录以合乎你的要求。下面是一个例子： 
    
    /etc/sddm.conf.d/avatar.conf
    
    [Theme]
    FacesDir=/var/lib/AccountsService/icons/

另一个选项是放置一个名为 `.face.icon` 的 PNG 图片到你的家目录下。在这种情况下，您不用对任何 SDDM 配置文件进行更改。不过，您仍需确定 `sddm` 用户可以读取这些 PNG 图片作为用户图标。 

**注意：** 在许多 KDE 的版本中，用户图标图像文件是 `~/.face` 而 `~/.face.icon` 是链接到图像文件的符号链接。如果用户的图标是符号链接，你需要为目标文件设置恰当的文件权限。

为了[设置合适权限](<../zh-cn/Access_Control_Lists.html#Set_ACL> "Access Control Lists")运行： 
    
    $ setfacl -m u:sddm:x ~/
    $ setfacl -m u:sddm:r ~/.face.icon
    
你可以通过运行下列命令[检查权限](<../zh-cn/Access_Control_Lists.html#Show_ACL> "Access Control Lists")： 
    
    $ getfacl ~/
    $ getfacl ~/.face.icon
    
详见 [SDDM README: No User Icon](<https://github.com/sddm/sddm#no-user-icon>)。 

###  数字锁

如果你想强制启用数字锁，在 `[General]` 小节设置 `Numlock=on`。 

如果 SDDM 在 Wayland 下运行，当前 NumLock 设置不起作用。您可能需要更改 KWin 设置以启用它，请参阅[此 issue](<https://github.com/sddm/sddm/issues/1830#issuecomment-1859339401>)

###  旋转显示

详见 [Xrandr#Configuration](<../zh-cn/Xrandr.html#Configuration> "Xrandr")。 

###  DPI 设置

有时位于“显示管理器”级别设置正确的显示器 DPI 是很有用的。[[1]](<https://github.com/sddm/sddm/blob/master/README.md#custom-dpi>) 你需要在 `ServerArguments` 字符串的末尾加上参数 `-dpi _your_dpi_` 例如： 
    
    /etc/sddm.conf.d/dpi.conf
    
    [X11]
    ServerArguments=-nolisten tcp -dpi 94

###  启用 HiDPI

**注意：** 自 SDDM 0.20.0 起，默认启用了 HiDPI 支持，以下步骤不再必要。

创建 [HiDPI](<../zh-cn/HiDPI.html> "HiDPI") 配置文件如下： 
    
    /etc/sddm.conf.d/hidpi.conf
    
    [Wayland]
    EnableHiDPI=true
    
    [X11]
    EnableHiDPI=true

当使用 Wayland 时，HiDPI 缩放取决于所使用的问候程序。[[2]](<https://github.com/sddm/sddm/issues/1704>) 例如，当使用基于 Qt 的问候程序（如 Breeze）时，请添加以下配置： 
    
    [General]
    
    GreeterEnvironment=QT_SCREEN_SCALE_FACTORS=2,QT_FONT_DPI=192

###  启用虚拟键盘

安装 [qt6-virtualkeyboard](<https://archlinux.org/packages/?name=qt6-virtualkeyboard>)包 或你希望的其他[虚拟键盘](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E5%B1%8F%E5%B9%95%E9%94%AE%E7%9B%98> "应用程序列表/工具")，创建如下文件： 
    
    /etc/sddm.conf.d/virtualkbd.conf
    
    [General]
    InputMethod=_您使用的虚拟键盘名称_

SDDM 在登录屏幕的左下角会显示一个虚拟键盘图标。 

###  使用指纹识别器

**提示：** 自 Plasma 6 发布以来，KDE 的锁屏应该已经支持使用指纹解锁，`kscreenlocker` 已经包含了所需的 `/etc/pam.d/kde-fingerprint`。 

然而，该配置不包括登录，只包括解锁现有会话。 

因为 KWallet 在登录时需要基于密码的认证（见下文），您可能仍然希望跳过 SDDM 的指纹设置。 

**注意：** 在改变设置前要确定你的指纹已经注册完成。指纹支持目前并不是完全工作正常，并且看起来在使用这种方法时仅使用密码登录将不再有效。

SDDM 使用 [fprint](<../zh-cn/Fprint.html> "Fprint") 以使用指纹识别。在安装了 fprint 和添加指纹签名后，在 `/etc/pam.d/sddm` 的顶部添加： 
    
    /etc/pam.d/sddm
    
    auth 			sufficient  	pam_fprintd.so

为了同时使用密码或指纹解锁，您可以在文件顶部添加以下内容： 
    
    /etc/pam.d/sddm
    
    auth 			[success=1 new_authtok_reqd=1 default=ignore]  	pam_unix.so try_first_pass likeauth nullok
    
    auth 			sufficient  	pam_fprintd.so

请注意，KWallet不能使用指纹读取器解锁（见 [KDE Wallet#在登录时自动解锁 Kwallet](<../zh-cn/KDE_Wallet.html#%E5%9C%A8%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E8%A7%A3%E9%94%81_Kwallet> "KDE Wallet")），但第一行确保了使用密码登录将自动解锁 KWallet。 

如果您现在在空密码字段中按回车，指纹读取器应该开始工作。 

###  无根模式

传统上，[Xorg](<../zh-cn/Xorg.html> "Xorg") 显示服务器默认以 root 权限运行。这种有根模式允许 Xorg 无限制地访问系统资源，这在直接硬件访问和管理常见的环境中是必要的。然而，随着现代计算环境中对安全性的日益重视，人们已经努力转向无根模式，这也是 [Wayland](<../zh-cn/Wayland.html> "Wayland") 默认以无根模式运行的原因。 

自 [sddm](<https://archlinux.org/packages/?name=sddm>)包 0.20.0 以来，支持启动非特权 X11（和 Wayland）会话。[[3]](<https://github.com/sddm/sddm/blob/v0.20.0/ChangeLog>)

要启用无根模式：在 `/etc/sddm.conf.d/` 下创建一个新的配置文件，给它一个有意义的名字，并添加以下内容，如果需要，将 `x11-user` 替换为 `wayland`。 
    
    /etc/sddm.conf.d/rootless-x11.conf
    
    [General]
    
    DisplayServer=x11-user

要确认您是否正在以无根模式运行，请检查哪个用户拥有compositor 进程的所有权（例如 `kwin_wayland`) 

**注意：**

  * SDDM 将其对 Wayland 的支持视为实验性的。
  * 默认情况下 `DisplayServer=wayland` 尝试使用 [weston](<../zh-cn/Weston.html> "Weston") 混成器，即便它没有安装，要使用不同的 Wayland 混成器，请按照 [#KDE Plasma / KWin](<#KDE_Plasma_/_KWin>) 中的描述将程序和相关参数输入到 `CompositorCommand` 选项中，也请参考 [sddm.conf(5)](<https://man.archlinux.org/man/sddm.conf.5>) 了解更多。

### Wayland

####  KDE Plasma / KWin

**警告：** KWin 启动时默认启用全局快捷键。这可能对登录屏幕很危险，因为使用默认的键绑定可以绕过登录提示。指定 `--no-global-shortcuts` 可以解决这个问题。[[4]](<https://invent.kde.org/plasma/plasma-workspace/-/commit/7e4159e46f816dc65ac62eae37b15c882f0c8064>)

将以下行添加到您的配置文件中，将 Wayland 混成器设置为 KWin 并启用 [wlr_layer_shell](<https://wayland.app/protocols/wlr-layer-shell-unstable-v1>) Wayland 协议扩展。使用 Qt5 和 Qt6 的 SDDM 主题分别需要 [layer-shell-qt](<https://archlinux.org/packages/?name=layer-shell-qt>)包 和 [layer-shell-qt5](<https://aur.archlinux.org/packages/layer-shell-qt5/>)AUR。 
    
    /etc/sddm.conf.d/10-wayland.conf
    
    [General]
    
    DisplayServer=wayland
    
    GreeterEnvironment=QT_WAYLAND_SHELL_INTEGRATION=layer-shell
    
    [Wayland]
    
    CompositorCommand=kwin_wayland --drm --no-lockscreen --no-global-shortcuts --locale1

#####  虚拟键盘

要启用虚拟键盘支持（例如使用 [qt6-virtualkeyboard](<https://archlinux.org/packages/?name=qt6-virtualkeyboard>)包 或 [plasma-keyboard](<https://archlinux.org/packages/?name=plasma-keyboard>)包），请在 `kwin_wayland` 命令中追加 `--inputmethod` 标志和适当的虚拟键盘，如下所示。不要在 `General` 部分设置 `InputMethod` 选项，因为这将导致虚拟键盘不再显示。 
    
    /etc/sddm.conf.d/10-wayland.conf
    
    [Wayland]
    
    CompositorCommand=kwin_wayland --drm --no-lockscreen --no-global-shortcuts --locale1 --inputmethod plasma-keyboard

#####  匹配 Plasma 显示配置

在 Plasma Wayland 会话中对显示配置所做的更改（例如监视器布局、分辨率等）将不会保留到 SDDM。要使它们保留，请打开 Plasma 的 _系统设置_ ，导航到**颜色和主题 >登录屏幕 (SDDM)** ，然后点击右上**应用 Plasma 设置...** 。您需要有执行此操作的权限。 

也可以手动完成同样的操作： 

要启用 SDDM 中正确的显示和监视器处理（缩放、监视器分辨率、刷新率等），您可以从您的主目录复制或修改适当的配置文件到 SDDM 的目录： 
    
    # cp ~/.config/kwinoutputconfig.json /var/lib/sddm/.config/
    
    # chown sddm:sddm /var/lib/sddm/.config/kwinoutputconfig.json
    
同时要启用 SDDM 中正确的输入处理（点击触控、触摸屏映射等），您可以从您的主目录复制适当的配置文件到 SDDM 的目录： 
    
    # cp ~/.config/kcminputrc /var/lib/sddm/.config/
    
    # chown sddm:sddm /var/lib/sddm/.config/kcminputrc
    
###  界面中文化

按照[安装指南#区域和本地化设置](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E5%8C%BA%E5%9F%9F%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%8C%96%E8%AE%BE%E7%BD%AE> "安装指南")设置完 LOCALE 后，SDDM 界面依然会显示为英文。欲显示中文，请修改 `sddm.service`，在 `[service]` 节中设置环境： 
    
    /usr/lib/systemd/system/sddm.service
    
    [Service]
    Environment=LANG=zh_CN.UTF-8

然后重启即可。 

##  故障排除

###  只有空白屏幕和光标，但没有欢迎界面

如果没有足够的空间，欢迎界面会崩溃。使用 `df -h` 命令检查您的磁盘空间。 

如果磁盘空间足够，那么这个问题可能源于此 [bug](<https://github.com/sddm/sddm/issues/1179>)。切换[到另一个 TTY](<../zh-cn/Getty.html#Installation> "Getty")，并尝试`loginctl unlock-session _session_id_`或[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") SDDM。 

###  登录后挂起

尝试移除 `~/.Xauthority` 文件后不重启再次登入。重启会再次创建该文件即该问题依旧存在。 

###  SDDM 在 tty1 启动而不是 tty7

SDDM 根据 [systemd 的规定](<http://0pointer.de/blog/projects/serial-console.html>)在 tty1 启动图形会话。 

请注意，配置文件仍然有 `MinimumVT` 选项，但自 SDDM 版本 0.20 起已被忽略：[sddm.conf(5) § MinimumVT=](<https://man.archlinux.org/man/sddm.conf.5#MinimumVT=>)。 

###  一个或多个用户没有出现在欢迎界面

**警告：** 根据 [UID 和 GID](<https://systemd.io/UIDS-GIDS/>)，通常不应将 UID 低于 1000 或高于 60513 的用户暴露给[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")。

默认情况下，SDDM 配置为仅显示 UID 在 1000 到 60513 范围内的用户。如果所需用户的 UID 在此范围之外，则需要修改该范围。 

例如，对于 UID 为 501 的用户，设置 `MinimumUid` 并隐藏那些使用系统用户 shell 的用户： 
    
    /etc/sddm.conf.d/uid.conf
    
    [Users]
    HideShells=/usr/bin/nologin,/sbin/nologin,/bin/false,/usr/bin/git-shell
    	
    MinimumUid=500

对于具有过大 UID 的用户，将 `MaximumUid` 设置为适当的值。 

###  用户头像未显示在欢迎界面上

如果用户数量超过 `DisableAvatarsThreshold` 参数设定的数量，或者 `EnableAvatars` 参数根本没有启用，那么在欢迎界面上将不会显示用户头像。要解决这个问题，请在您的 SDDM 配置中添加以下几行： 
    
    /etc/sddm.conf.d/avatars.conf
    
    [Theme]
    EnableAvatars=true # enable avatars	
    DisableAvatarsThreshold=7 # set the threshold for the number of users. Avatars are not shown if this threshold is exceeded.

###  SDDM 只加载 US 键盘布局

SDDM 加载的键盘布局被确定在 `/etc/X11/xorg.conf.d/00-keyboard.conf` 文件中。您可以通过 `localectl set-x11-keymap` 命令以生成此配置文件。详见 [Xorg/键盘设置](</wzh/index.php?title=Xorg/%E9%94%AE%E7%9B%98%E8%AE%BE%E7%BD%AE&action=edit&redlink=1> "Xorg/键盘设置（页面不存在）")（英语：[Xorg/Keyboard_configuration](<https://wiki.archlinux.org/title/Xorg/Keyboard_configuration> "en:Xorg/Keyboard configuration")）。 

设置仅在 SDDM 中设置而不在后续会话中设置的键盘布局的另一种方法是在 SDDM 的启动脚本（位于 `/usr/share/sddm/scripts/Xsetup`）中调用 _setxkbmap_ 命令。有关示例，请参见[Xorg/键盘设置#使用 setxkbmap](</wzh/index.php?title=Xorg/%E9%94%AE%E7%9B%98%E8%AE%BE%E7%BD%AE&action=edit&redlink=1> "Xorg/键盘设置（页面不存在）")（英语：[Xorg/Keyboard configuration#Using setxkbmap](<https://wiki.archlinux.org/title/Xorg/Keyboard_configuration#Using_setxkbmap> "en:Xorg/Keyboard configuration")）。 

SDDM 可能也会错误地显示为 US 布局，但在您开始输入您的密码时立即切换到正确的键盘布局 [[5]](<https://github.com/sddm/sddm/issues/202#issuecomment-76001543>)。此 bug 看起来不是来自 SDDM，而是 [Xorg](<../zh-cn/Xorg.html> "Xorg")。[[6]](<https://gitlab.freedesktop.org/xorg/xserver/-/issues/257>)

###  屏幕分辨率过低

此问题可能源于显示屏 HiDPI 的使用破坏了 [EDID](<https://en.wikipedia.org/wiki/Extended_Display_Identification_Data> "wikipedia:Extended Display Identification Data") [[7]](<https://github.com/sddm/sddm/issues/692>)。如果你[启动了 HiDPI](<#%E5%90%AF%E7%94%A8_HiDPI>)，尝试关掉它。 

如果上述方法失败了，您可以尝试在 Xorg 配置文件中设置您的显示尺寸： 
    
    /etc/X11/xorg.conf.d/90-monitor.conf
    
    Section "Monitor"
            Identifier      "<default monitor>"
            DisplaySize     345 194 # in millimeters
    EndSection

###  自动挂载家目录的加载时间过长

SDDM 默认会访问 `~/.face.icon` 文件以尝试显示用户头像。如果您的家目录采用自动挂载的文件系统（autofs），例如如果您使用 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")，这将会使之等待 60 秒，直到自动挂载的文件系统（autofs）返回此目录不能被挂载。 

您可以通过创建以下文件关闭头像功能： 
    
    /etc/sddm.conf.d/avatar.conf
    
    [Theme]
    EnableAvatars=false

###  X authority（也称为 MIT-MAGIC-COOKIE）文件

SDDM 使用一个随机的新鲜 UUID 作为认证文件，详情见 [[8]](<https://github.com/sddm/sddm/issues/622>)。因此，要找到该文件，可以使用一个脚本来查找： 
    
    # find /var/run/sddm/ -type f
     
如果需要在没有用户登录时启动 [x11vnc](<../zh-cn/X11vnc.html> "X11vnc")，可能需要这个文件。例如： 
    
    # x11vnc -display :0 -auth "$( find /var/run/sddm/ -type f )"
     
###  多屏幕设置上的重叠欢迎界面

在多屏幕设置上，X 监视器布局可能没有正确设置，导致欢迎界面重叠。要解决这个问题，添加以下几行来从左到右排序您的 SDDM 问候者布局： 
    
    /usr/share/sddm/scripts/Xsetup
    
    for next in $(xrandr --listmonitors | grep -E " *[0-9]+:.*" | cut -d" " -f6); do
      [ -z "$current" ] && current=$next && continue
      xrandr --output $current --auto --output $next --auto --right-of $current
      current=$next
    done

###  登录会话出现在意外的显示设备上

如果连接了多个显示设备，SDDM 登录会话可能会出现在与您的主显示设备不同的显示设备上。如果次要显示设备旋转了而主显示设备没有，这个问题可能会很烦人。一个简单的解决方法是在登录会话使用 `Xsetup` 脚本之前使用 `xrandr` 配置显示设备。例如，这里 `xrandr` 报告有两个已连接的显示设备，其中次要显示设备（DP-2）位于主显示设备（DP-4）的左侧。 
    
    # xrandr | grep -w connected
    
    DP-2 connected 2160x3840+0+0 left (normal left inverted right x axis y axis) 597mm x 336mm
    
    DP-4 connected primary 3840x2160+2160+0 (normal left inverted right x axis y axis) 697mm x 392mm
    
以下 `Xsetup` 重新创建了登录窗口的上述设置： 
    
    /usr/share/sddm/scripts/Xsetup
    
    #!/bin/sh
    
    # Xsetup - 在登录对话框出现之前作为 root 运行
    
    xrandr --output DP-4 --auto --primary
    
    xrandr --output DP-2 --left-of DP-4 --rotate left --noprimary

###  使用 NVIDIA 显卡注销后黑屏

用户注销后可能会遇到完全黑屏或只有光标/显示设备徽标显示在屏幕上。这是因为 `sddm.service` 比 NVIDIA 驱动程序启动得更快。考虑使用 [early KMS](<../zh-cn/NVIDIA.html#%E6%97%A9%E5%90%AF%E5%8A%A8> "NVIDIA")。 

###  在 Wayland 上使用混合图形时屏幕不同步

如果您设置 SDDM 使用 `kwin_wayland` 合成器，启动时可能会遇到屏幕不同步的问题。如果返回到 X11 工作正常，并且您正在使用 `mesa-amber` 驱动程序，那么通过用 `mesa` 替换当前的 `mesa-amber` 驱动程序，Wayland 很可能会正常工作。您可以在 [KDE Bug 483804](<https://bugs.kde.org/show_bug.cgi?id=483804>) 查看有关此问题的更多细节。 

###  部分主题崩溃

部分 SDDM 没有在 `metadata.desktop` 中指定 `QtVersion`， 导致 SDDM 以不兼容的欢迎界面启动（Qt5 而不是 Qt6）。 

若您设定了自定义主题，但重启后显示默认主题并报错 `Library import requires a version`，您需要将 `QtVersion=6` 添加到 `/usr/share/sddm/themes/_主题名称_ /metadata.desktop`。 
