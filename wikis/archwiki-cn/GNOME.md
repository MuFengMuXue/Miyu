**翻译状态：**

  * 本文（或部分内容）译自 [GNOME](<https://wiki.archlinux.org/title/GNOME> "arch:GNOME")，最近一次同步于 2025-12-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNOME?diff=0&oldid=856203>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNOME_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [GTK](<../zh-cn/GTK.html> "GTK")
  * [GDM](<../zh-cn/GDM.html> "GDM")
  * [GNOME/Files](<../zh-cn/GNOME/%E6%96%87%E4%BB%B6.html> "GNOME/Files")
  * [GNOME/Gedit](<../zh-cn/GNOME/Gedit.html> "GNOME/Gedit")
  * [GNOME/Web](<../zh-cn/GNOME/Web.html> "GNOME/Web")
  * [GNOME/Keyring](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring")
  * [Official repositories#gnome-unstable](<../zh-cn/Official_repositories.html#gnome-unstable> "Official repositories")

[GNOME](<https://www.gnome.org/>)（读音为/(ɡ)noʊm/）是一个追求简单易用的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。它由 [GNOME项目](<https://zh.wikipedia.org/wiki/GNOME%E8%A8%88%E5%8A%83> "zhwp:GNOME计划")设计，并且完全由自由开源的软件组成。GNOME默认使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 作为显示服务器，并同时提供多个对话可供选择： 

  * **GNOME** 是在[Wayland](<../zh-cn/Wayland.html> "Wayland")上运行GNOME Shell的默认选项。传统的X应用使用Xwayland运行。
  * **GNOME Classic** 通过[特定的扩展和数值](<https://web.archive.org/web/20190503163814/http://www.worldofgnome.org/welcome-to-gnome-3-8-flintstones-mode/>)，提供了“[传统的桌面体验](<https://help.gnome.org/users/gnome-help/stable/gnome-classic.html>)”（类似GNOME2的界面）。因此，它是GNOME Shell的定制样式，而非真正的不同模式。

##  安装

有两个软件组可用： 

  * [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 包含基本的桌面环境和一些集成良好的[应用](<https://wiki.gnome.org/Apps>)
  * [gnome-circle](<https://archlinux.org/groups/x86_64/gnome-circle/>)包组 包含多种[格外应用](<https://apps.gnome.org/#circle>)，极大的拓展了Gnome生态。
  * [gnome-extra](<https://archlinux.org/groups/x86_64/gnome-extra/>)包组 包含部分[开发工具](<https://apps.gnome.org/#development>)，以及其他适合Gnome的应用与游戏。

GNOME 的基础桌面环境由 [Mutter](<https://zh.wikipedia.org/wiki/Mutter_\(software\)> "zhwp:Mutter \(software\)") 窗口管理器的插件 [GNOME Shell](<https://zh.wikipedia.org/wiki/GNOME_Shell> "zhwp:GNOME Shell") 组成。可以用 [gnome-shell](<https://archlinux.org/packages/?name=gnome-shell>)包 单独安装它。 

**注意：** _mutter_ 是桌面的混成器。它利用硬件图形加速减少屏幕的混乱。GNOME 会话管理器会自动检测显卡驱动是否能够运行 GNOME Shell，如果不行则用 _llvmpipe_ 软件渲染。

也可以使用不稳定版本，见[官方软件仓库#gnome-unstable](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html#gnome-unstable> "官方软件仓库")。 

##  运行 GNOME

GNOME 可以使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")以图形方式启动，也可以从控制台手动启动（可能会缺少某些功能）。[gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组的显示管理器是[GDM](<../zh-cn/GDM.html> "GDM")。 

**注意：** GDM提供了GNOME的锁屏功能（及其它）支持。如果没有使用GDM启动GNOME，则需要使用其它屏幕锁定器。见[List of applications/Security#Screen lockers](<../zh-cn/List_of_applications/Security.html#Screen_lockers> "List of applications/Security")。

###  图形界面启动

如果安装了[gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组并希望GNOME在下次启动时自动启动, 请[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `gdm.service`，随后可以在显示管理器的会话菜单中选择想要使用的会话： _GNOME_ 、 _GNOME Classic_ （仅在[gnome-shell-extensions](<https://archlinux.org/packages/?name=gnome-shell-extensions>)包 已安装时显示）。 

如果想立即启动 GNOME 以避免重启，可以从一个没有被图形占用的 tty 上[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `gdm.service`。 

###  手动启动

**注意：** 仍然需要X服务器用于运行尚未移植到[Wayland](<../zh-cn/Wayland.html> "Wayland")的应用，详见[Wayland#XWayland](<../zh-cn/Wayland.html#XWayland> "Wayland")。使用Qt等特定图形库的应用，可以通过强制设置环境变量使用Wayland。详见[Wayland#GUI libraries](<../zh-cn/Wayland.html#GUI_libraries> "Wayland")。

####  会话类型

Gnome会话继承了systemd的会话类型。当会话开始时，systemd的会话类型在会话启动时由`XDG_SESSION_TYPE`环境变量决定，并在启动后只能由该会话上的控制器决定。详见 [Github](<https://github.com/systemd/systemd/issues/14489>)。 

因此仅仅在登录后设置`XDG_SESSION_TYPE` 并不起作用。因此应创建一个systemd drop-in 文件给getty设置环境变量： 
    
    /etc/systemd/system/getty@tty1.service.d/wayland.conf
    
    [Service]
    Environment=XDG_SESSION_TYPE=wayland

重新加载后检查会话类型： 
    
    $ loginctl session-status

####  启动会话

在正确设置会话类型后，可以通过以下命令手动启动会话： 
    
    $ gnome-session

由于直接运行`gnome-shell --wayland`缺乏会话管理，所以并不推荐。 

请注意，手动调用Gnome**不需要**`gdm`（因此也不需要附带的`gdm.service`），因此对于安装了Gnome最小安装的用户来说，可以根据个人喜好，选择一些包含在更广泛的`gnome`组中的软件包。 

若要在 tty1 登录时启动，将以下内容添加到 `.bash_profile` 中： 
    
    gnome-session --no-reexec

Firefox和Qt应用不遵守`XDG_SESSION_TYPE`，所以最好给它们加上变量： 
    
    if [-z $DISPLAY && $(tty) == /dev/tty1 && $XDG_SESSION_TYPE == wayland ](</wzh/index.php?title=-z_$DISPLAY_%26%26_$\(tty\)_%3D%3D_/dev/tty1_%26%26_$XDG_SESSION_TYPE_%3D%3D_wayland&action=edit&redlink=1> "-z $DISPLAY && $\(tty\) == /dev/tty1 && $XDG SESSION TYPE == wayland（页面不存在）"); then
      MOZ_ENABLE_WAYLAND=1 QT_QPA_PLATFORM=wayland exec gnome-session --no-reexec
    fi

###  Wayland中的GNOME应用

在使用 _GNOME_ 会话时，GNOME 应用将使用 Wayland 运行。出于调试需要, <https://docs.gtk.org/gtk3/running.html> 和 <https://docs.gtk.org/gtk4/running.html> 列出的选项和环境变量。 

##  导航

[GNOME Shell cheat sheet](<https://wiki.gnome.org/Projects/GnomeShell/CheatSheet>) 中解释了如何高效地使用 GNOME shell，它展示了 GNOME shell 的特色和快捷键，包括切换任务，使用键盘，窗口控制，面板，概览模式等等。以下是部分常用的快捷键： 

  * `Super+m`：显示消息列表
  * `Super+a`：显示应用菜单
  * `Alt+Tab`：切换当前使用的应用
  * `Alt+`` （美式键盘`Tab`上面的按键）：切换正在前台使用的应用的窗口
  * `Alt+F2`，然后输入 `r` 或 `restart`：在图形界面出问题时重启界面（仅用于X/传统模式，不适用于Wayland模式）。

如需改变默认配置，使其更类似Windows，见 [GNOME/提示与技巧#导航](<../zh-cn/GNOME/%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7.html#%E5%AF%BC%E8%88%AA> "GNOME/提示与技巧")。 

更多快捷键见[键盘导航](<https://help.gnome.org/users/gnome-help/stable/keyboard-nav.html>)。 

##  遗留名称

**注意：** 一些GNOME应用在文档和对话框中的名称已经更改，但执行文件名称却没有。下面表格列出了一些这样的应用。

**提示：** 在搜索栏中搜索应用的遗留名称将成功找到对应的应用，例如搜索 _nautilus_ 会出现 _文件_ 。

当前  | 遗留   
---|---  
[文件](<../zh-cn/GNOME/%E6%96%87%E4%BB%B6.html> "GNOME/Files") | Nautilus   
[Web](<../zh-cn/GNOME/Web.html> "GNOME/Web") | Epiphany   
视频  | Totem   
主菜单  | Alacarte   
[文档查看器](</wzh/index.php?title=GNOME/Document_viewer&action=edit&redlink=1> "GNOME/Document viewer（页面不存在）") | Evince   
磁盘使用情况分析器  | Baobab   
图像查看器  | EoG (Eye of GNOME)   
[密码和密钥](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring") | Seahorse   
翻译编辑器  | Gtranslator   
  
##  配置

GNOME系统设置面板（ _gnome-control-center_ ）和GNOME应用使用[dconf](<https://en.wikipedia.org/wiki/Dconf> "wikipedia:Dconf")配置系统存储设置。 

您可以使用[gsettings(1)](<https://man.archlinux.org/man/gsettings.1>)命令行工具直接访问 dconf 数据库。这也可以让您修改用户界面不公开的设置。命令行工具 [dconf(1)](<https://man.archlinux.org/man/dconf.1>) 可以直接修改底层数据库，跳过验证过程。 

直到GNOME 3.24，设置由GNOME设置进程应用（位于`/usr/lib/gnome-settings-daemon/gnome-settings-daemon`），其也可以在GNOME会话之外运行。 

然而GNOME 3.24用几个相互独立的设置插件（`/usr/lib/gnome-settings-daemon/gsd-*`，后来移动到`/usr/lib/gsd-*`）取代了 GNOME 设置进程。这些插件通过 `/etc/xdg/autostart` (匹配org.gnome.SettingsDaemon.*.desktop) 下的桌面文件进行控制。若要在 GNOME 会话之外运行这些插件，您需要复制或编辑相应的[桌面条目](<../zh-cn/Desktop_entries.html> "Desktop entries")到 `~/.config/autostart`。 

配置通常是用户特定的，本文将不介绍如何为多个用户创建配置模板。 

###  GNOME 系统设置

####  色彩

`colord` 守护进程会读取显示器的 EDID 信息并提取出合适的色彩配置内容。大多数情况下，色彩配置都是正确的，不需要额外设置；但是对于某些偏差情况或使用较旧的显示器时，可以把色彩配置文件放在 `~/.local/share/icc/` 下并被指向。 

####  夜间模式

GNOME 内置了类似于 [Redshift](<../zh-cn/Redshift.html> "Redshift") 的蓝光过滤功能。夜间模式可以在设置面板中启动及自定义启动时间。此外，夜间模式的色温可以使用以下[dconf](<https://archlinux.org/packages/?name=dconf>)包设置进行调整，5000是一个示例值： 
    
    $ gsettings set org.gnome.settings-daemon.plugins.color night-light-temperature 5000
    
**提示：** 若要在Wayland中调整白天的色温，请安装[Night Light Slider扩展](<https://extensions.gnome.org/extension/1276/night-light-slider/>)。

**注意：** 在NVIDIA显卡上，夜间颜色只工作在版本545.29.02及之后的驱动上

####  日期与时间

如果系统已有配置好的[网络时间协议 守护进程](<../zh-cn/Network_Time_Protocol_daemon.html> "Network Time Protocol daemon")，它同样会对 GNOME 起作用。如果需要，同步设置可以在菜单内设为手动控制。 

GNOME支持自动选择时区，可在系统设置里的 _日期和时间_ 选项中开启。前提是已开启定位服务 (见设置中的 _隐私_ 选项）。 

**注意：** 由于Mozilla定位服务的退役，自动选择时区可能不再工作。见[[1]](<https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/issues/841#note_2300635>) . 解决方案见 [[2]](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E5%9F%BA%E4%BA%8E%E5%9C%B0%E7%90%86%E4%BD%8D%E7%BD%AE%E8%AE%BE%E5%AE%9A>)

若要在顶栏内显示日期，请运行： 
    
    $ gsettings set org.gnome.desktop.interface clock-show-date true
    
另外，若要在顶栏的日历中显示周数，请运行： 
    
    $ gsettings set org.gnome.shell.calendar show-weekdate true
    
####  默认应用程序

首次安装 GNOME 时，您可能会发现某些格式由错误的应用处理，比如视频被 _totem_ 打开而不是以前使用的 [VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC")。某些格式关联可以使用系统设置中的 _默认应用程序_ 进行调整。 

有关其它协议和方法，请参阅[默认应用程序](<../zh-cn/Default_applications.html> "Default applications")进行配置。 

####  鼠标和触摸板

大多数触摸板设置可以使用系统设置中的 _鼠标和触摸板_ 进行调整。 

根据您的设备，其它配置可能可用，但不会显示在默认界面内，例如不同的触摸板点击方法： 
    
    $ gsettings range org.gnome.desktop.peripherals.touchpad click-method
    
    enum
    'default'
    'none'
    'areas'
    'fingers'
    
手动设置: 
    
    $ gsettings set org.gnome.desktop.peripherals.touchpad click-method 'fingers'
    
或使用[gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包设置。 

**注意：** GNOME 不支持 [synaptics](<../zh-cn/Touchpad_Synaptics.html> "Synaptics") 并默认使用 [libinput](<../zh-cn/Libinput.html> "Libinput")。参考 [这个缺陷报告](<https://bugzilla.gnome.org/show_bug.cgi?id=764257#c12>)。

#####  使用鼠标更改窗口大小

默认情况下，您可以使用鼠标移动窗口，方法是按住 Super，单击并按住鼠标左键并拖动鼠标。 

此外，您可以通过按住 Super、单击并按住鼠标右键并拖动鼠标来启用鼠标调整窗口大小： 
    
    $ gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true
    
如果您不喜欢 Super 键，还可以将修饰键更改为其他键，例如 Alt 或 Ctrl： 
    
    $ gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier "'<Alt>'"
    
####  网络

[NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 是GNOME项目中控制网络设置的工具。如果尚未安装，则[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包软件包并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")`NetworkManager.service` 。 

虽然可以使用任何其它[网络管理器](<../zh-cn/Network_manager.html> "Network manager")，但 NetworkManager 可以使用整合到桌面环境的网络设置和状态指示器（ [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包，不必要安装 ）。 

**注意：** 用[networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包的 _nmtui_ 设置隐藏的无线网络不会自动连接。您需要在GNOME设置中创建一个新配置文件，以恢复该网络的自动连接功能。

####  在线帐户

部分在线账户，比如 [ownCloud](</wzh/index.php?title=OwnCloud&action=edit&redlink=1> "OwnCloud（页面不存在）")，需要安装 [gvfs-goa](<https://archlinux.org/packages/?name=gvfs-goa>)包 和[gvfs-dnssd](<https://archlinux.org/packages/?name=gvfs-dnssd>)包以在 GNOME 应用比如 [GNOME 文件](<../zh-cn/GNOME_Files.html> "GNOME Files")以及 GNOME 文档中发挥全部功能[[3]](<https://wiki.gnome.org/ThreePointSeven/Features/Owncloud>)。 

详见[在线账户](<https://help.gnome.org/users/gnome-help/stable/accounts.html>)。 

####  搜索

GNOME shell在按下`Super`键并开始输入时会启动搜索。[localsearch](<https://archlinux.org/packages/?name=localsearch>)包作为[gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组中[nautilus](<https://archlinux.org/packages/?name=nautilus>)包的依赖被默认安装。它提供一个应用和数据的索引数据库。它可以被设置中“搜索”菜单项配置。它在用户登录时自动被gnome-session启动。 

localsearch 并不自动递归用户的家目录中所有的目录,所以你可能需要在 搜索 > 搜索位置 中添加自定义的路径。创建一个名为 `.nomedia` 的空文件以将某个目录从索引中排除。 

可通过 `localsearch status` 查看当前索引状态。搜索内容可以在命令行中被`localsearch searc``h`查看，被`localsearch tag`编辑，以及被重置。见 `localsearch help` 或在线寻求参考。 

tinysparql-sql被用作索引数据库。如果需要，数据库可以被直接查询。 

####  设备安全

GNOME 43 在设置中添加了一个新的设备安全面板。该功能依赖[fwupd](<../zh-cn/Fwupd.html> "Fwupd")工作。见 [[4]](<https://gitlab.gnome.org/GNOME/gnome-control-center/-/issues/2122>)

###  高级设置

如上文所述，改变[GTK](<../zh-cn/GTK.html> "GTK")主题或[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")主题等选项，并不会出现在GNOME设置（gnome-control-center）里。想要修改这些设置可以使用GNOME Tweaks （[gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包），这是一个展示了许多这类设置的图形化工具。 

（存储在 DConf 数据库中的）GNOME设置也可以使用[dconf-editor(1)](<https://man.archlinux.org/man/dconf-editor.1>)（一个图形化的DConf配置工具）或[gsettings](<https://developer.gnome.org/gio/stable/GSettings.html>)命令行工具进行配置。GNOME Tweaks 只能用于改变GUI。注意，你不一定总能看到下文描述的所有设置。 

####  拓展

拓展的目录位于 <https://extensions.gnome.org>。拓展可通过 [archlinux官方仓库](<https://archlinux.org/packages/?q=gnome-shell-extension>) (少数), [AUR](<https://aur.archlinux.org/packages?K=gnome-shell-extension>)或者[网页](<https://extensions.gnome.org>)安装。

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 下方的“注意”推荐手动管理用户文件，因为更“简单”，但并没有解释为什么。（在 [Talk:GNOME](<../zh-cn/Talk:GNOME.html>) 中讨论）

**注意：** * 通过浏览器安装拓展仅对当前用户生效，并需要用户手动管理升级。这是比较简单的方法。 

  *     * 此外，如果你想要从浏览器安装拓展，你需要安装 [gnome-browser-connector](<https://archlinux.org/packages/?name=gnome-browser-connector>)包。如果从官方仓库或者AUR安装，则不需要。
  * 从AUR（或者官方仓库）安装拓展是他们对整个系统生效（并且在使用 [AUR 助手](<../zh-cn/AUR_%E5%8A%A9%E6%89%8B.html> "AUR 助手")时自动更新）。

已安装的拓展可以通过 _gnome-extensions-app_ 在图形界面、在命令行使用[gnome-extensions(1)](<https://man.archlinux.org/man/gnome-extensions.1>)或在浏览器中通过网页配置、启用或禁用。在浏览器中，如需安装和激活拓展，请点击右上角的ON，然后点击弹出窗口的Install（如果该拓展并没有被安装）。已经安装的拓展可在 <https://extensions.gnome.org/local/>查看并检查更新。 

[gnome-shell-extensions](<https://archlinux.org/packages/?name=gnome-shell-extensions>)包 提供了一些GNOME官方维护的非常有用的拓展。 

[extension-manager](<https://archlinux.org/packages/?name=extension-manager>)包 是一个用于在操作系统或用户范围内安装、拆卸、启用、禁用拓展的图形工具。安装前请仔细确认[已知问题列表](<https://github.com/mjakeman/extension-manager/labels/bug>)。 

启用一个拓展（默认禁用）： 
    
    $ gsettings set org.gnome.shell disable-user-extensions false
    
列出当前启用的拓展： 
    
    $ gsettings get org.gnome.shell enabled-extensions
    
上述命令可能会列出已删除的扩展。要仅列出已启用和安装的扩展，请改用 gnome-extensions： 
    
    $ gnome-extensions list --enabled
    
关于 GNOME shell拓展的更多信息，详见 <https://extensions.gnome.org/about/>. 

####  外观

#####  主题

**注意：** 从[Gnome 42](<https://release.gnome.org/42/>)开始，许多默认的Gnome应用程序使用GTK 4和libadwaita。这些应用程序目前不支持通过gsettings或[gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包改变主题，只能通过系统设置的外观选项来调整配置。若要设置Adwaita或Adwaita-dark以外的GTK主题，见[GTK#Themes](<../zh-cn/GTK.html#Themes> "GTK")。

GNOME默认使用Adwaita。若要只将Adwaita-dark应用于GTK 2应用，请使用以下符号链接： 
    
    $ ln -s /usr/share/themes/Adwaita-dark ~/.themes/Adwaita
    
**注意：** Adwaita-dark主题由[gnome-themes-extra](<https://archlinux.org/packages/?name=gnome-themes-extra>)包提供，因此GNOME的最小安装可能不会包含此主题。

若要选择新的主题，（将它们移到适当的目录中，并）使用GNOME Tweaks或下面的GSettings命令。 

对于GTK主题： 
    
    $ gsettings set org.gnome.desktop.interface gtk-theme _theme-name_
    
对于图标主题： 
    
    $ gsettings set org.gnome.desktop.interface icon-theme _theme-name_
    
**注意：** 窗口管理器的主题会跟随GTK主题。使用`org.gnome.desktop.wm.preferences theme`的方法已被废弃和忽略。

见[GTK#Themes](<../zh-cn/GTK.html#Themes> "GTK")和[Icons#Manually](</wzh/index.php?title=Icons&action=edit&redlink=1> "Icons（页面不存在）"). 

######  标题栏按钮排序

设置 GNOME 窗口管理器顺序 (Mutter, Metacity): 
    
    $ gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'
    
**提示：** 冒号表示窗口标题栏按钮出现的方向

#####  GNOME Shell主题

GNOME Shell本身的主题是可配置的。首先确认您已安装[gnome-shell-extensions](<https://archlinux.org/packages/?name=gnome-shell-extensions>)包软件包以应用Shell主题。然后通过GNOME Tweaks或通过[GNOME Shell Extensions](<https://extensions.gnome.org>) 网站启用“User Themes”扩展。Shel主题可以通过使用GNOME Tweaks软件加载并选用。 

[AUR](<https://aur.archlinux.org/packages?O=0&K=gnome-shell-theme&do_Search=Go&PP=50&SB=v&SO=d>)里有大量可用的GNOME Shell主题。Shell主题也可在[gnome-look.org](<https://gnome-look.org/>)里下载。 

#####  AppIndicators/顶部菜单栏图标

AppIndicators 对于监控和控制后台程序很有用，其对应的软件包是 [gnome-shell-extension-appindicator](<https://archlinux.org/packages/?name=gnome-shell-extension-appindicator>)包 or [gnome-shell-extension-appindicator-git](<https://aur.archlinux.org/packages/gnome-shell-extension-appindicator-git/>)AUR。安装后重启 [GNOME Shell](<#Navigation>) ，然后在 GNOME 扩展程序中启用 AppIndicator 扩展，或者运行 `$ gnome-extensions enable $(gnome-extensions list | grep -m 1 appindicatorsupport)`来以命令行方式启用它。 

#####  Shell动画速度

GNOME shell 动画可以被提速、降速或禁用。见[GNOME/Tips and tricks#Change animation speed](<../zh-cn/GNOME/Tips_and_tricks.html#Change_animation_speed> "GNOME/Tips and tricks"). 

#####  Shell 模糊效果

Blur my Shell 是一个给概览模式页面、Shell本身和其他部分应用添加模效果的拓展。安装 [gnome-shell-extension-blur-my-shell](<https://aur.archlinux.org/packages/gnome-shell-extension-blur-my-shell/>)AUR ，或者[gnome-shell-extension-blur-my-shell-git](<https://aur.archlinux.org/packages/gnome-shell-extension-blur-my-shell-git/>)AUR 。该拓展具有高度可自定义性，并且你可以自由选择对哪些应用施加模糊效果。 

#####  更好的 Alt-Tab

GNOME中默认的 Alt-Tab功能非常简单，并不展示selected windows的概览。你可以在设置应用中将 Alt-Tab快捷键从 “切换应用” 改为 “切换窗口”以展示窗口概览。 

你也可以使用Coverflow Alt-Tab。这是一个拓展Alt-Tab行为的拓展，添加了一些特性使在应用程序之间切换更简单、更好看。 安装[gnome-shell-extension-coverflow-alt-tab-git](<https://aur.archlinux.org/packages/gnome-shell-extension-coverflow-alt-tab-git/>)AUR。你可以根据喜好配置该拓展。 

注意：`Super-``默认提供“切换窗口”功能。 

####  自启动

GNOME提供[XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart")。 

[gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包 程序可以用来管理自启动项。 

**提示：** 如果Tweaks中自启动应用选项下加号按钮为灰色不可用，尝试在终端下通过`gnome-tweaks`命令启动Tweaks。见[此贴](<https://bbs.archlinux.org/viewtopic.php?pid=1413631#p1413631>)。

####  桌面

##### Dash to Dock

To move the dash out of the overview and turn it into a dock to以便于启动和切换应用, 安装 [gnome-shell-extension-dash-to-dock](<https://aur.archlinux.org/packages/gnome-shell-extension-dash-to-dock/>)AUR. 

#####  启动到概览模式

从GNOME 40开始，桌面会直接启动到概览模式，而不是桌面（如以前的版本）。若要模仿经典的行为，可以安装[No overview at start-up](<https://extensions.gnome.org/extension/4099/no-overview/>)插件。 

如果你在使用[gnome-shell-extension-dash-to-dock](<https://aur.archlinux.org/packages/gnome-shell-extension-dash-to-dock/>)AUR，你也可以在gsettings中禁用该行为。 
    
    $ gsettings set org.gnome.shell.extensions.dash-to-dock disable-overview-on-startup true
    
详见[此讨论](<https://discourse.gnome.org/t/gnome-40-login-is-to-the-activities-overview-mode-how-do-you-disable-this/5783>)。 

####  剪贴板历史

不像其他桌面环境，GNOME 并没有内建的管理剪贴板历史的工具。你可以使用拓展。安装 [gnome-shell-extension-clipboard-indicator](<https://aur.archlinux.org/packages/gnome-shell-extension-clipboard-indicator/>)AUR。 

####  天气

以展示选定地点的天气，比如状态、风速、气压等信息，请安装 [gnome-shell-extension-openweather](<https://aur.archlinux.org/packages/gnome-shell-extension-openweather/>)AUR。天气信息实时更新。 

####  音频输入输出选择

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** 该软件目前最高只支持到Gnome 43。 (在 [Talk:GNOME](<../zh-cn/Talk:GNOME.html>) 讨论)

默认情况下，如果你想要选择音频输入输出设备或改变麦克风的音量，你需要打开GNOME控制中心进行配置。你可以安装[gnome-shell-extension-sound-output-device-chooser](<https://aur.archlinux.org/packages/gnome-shell-extension-sound-output-device-chooser/>)AUR 或者 [gnome-shell-extension-sound-output-device-chooser-git](<https://aur.archlinux.org/packages/gnome-shell-extension-sound-output-device-chooser-git/>)AUR以更方便地控制他们。你可以在安装后进行更多的配置。 

####  字体

**提示：** 如果您把"Scaling factor"调至1.00以上的某值，辅助功能菜单将自动启用

GNOME可以设置窗体标题，界面（应用），文档及等宽字体。查看Tweaks下的字体选项卡以获得相关选项。 

对于字体渲染来说，RGBA可能适合更多的显示器类型，如果字体看起来过分拥挤，可以将字体渲染调至“Slight”或“None”。 

####  输入法

GNOME集成了的通过[IBus](<../zh-cn/IBus.html> "IBus")的输入法, 只有[ibus](<https://archlinux.org/packages/?name=ibus>)包和添加想要的输入法引擎 (例如:[ibus-libpinyin](<https://archlinux.org/packages/?name=ibus-libpinyin>)包 for Intelligent Pinyin) 需要安装，安装后，输入法引擎可以加入GNOME的区域和语言设置键盘布局。 

####  非主流键盘布局

如果您使用的是像Neo2这样使用多层/修饰键的替代键盘布局，您可能需要转到 GNOME。设置 (_gnome-control-center_)中的 _Keyboard > Type Special Characters_ 将 _Alternate Characters Key_ 从 _右 Alt_ 改为其他键，以便它可以作为键盘布局的本地修饰键使用。将其设置为 _Left Alt_ 会阻止 _Alt+Tab_ 键盘快捷键，因此请小心您所更改的内容。 如果没有进行这个更改，您的左 _Mod3_ 键可能会起作用，但右侧的一个 (_AltGr_) 键可能不会起作用。（截至2021-05-18） 

####  电源

当您使用笔记本时，可能想修改以下设置，包括控制闲置、按下电源按钮和盖子关闭时的行为。 
    
    $ gsettings set org.gnome.settings-daemon.plugins.power button-power _hibernate_
    $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout _3600_
    $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type _hibernate_
    $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout _1800_
    $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type _hibernate_
    $ gsettings set org.gnome.desktop.lockdown disable-lock-screen _true_
    
如需在合上盖子后依然保持显示器开启： 
    
    $ gsettings set org.gnome.settings-daemon.plugins.xrandr default-monitors-setup do-nothing
    
GNOME 3.24中不建议使用以下设置： 
    
    org.gnome.settings-daemon.plugins.power button-hibernate
    org.gnome.settings-daemon.plugins.power button-power
    org.gnome.settings-daemon.plugins.power button-sleep
    org.gnome.settings-daemon.plugins.power button-suspend
    org.gnome.settings-daemon.plugins.power critical-battery-action
    
#####  笔记本合盖时不挂起

The settings panel of GNOME does not provide an option for the user to change the action triggered when the laptop lid is closed. To change the lid switch action system-wide, edit the systemd settings in `/etc/systemd/logind.conf`. To turn off suspend on lid close, set `HandleLidSwitch=ignore`, as described in [Power management#ACPI events](<../zh-cn/Power_management.html#ACPI_events> "Power management"). 

#####  修改电池电量严重不足时的行为

设置面板不提供对电池电量严重不足行为的设置。这些设置也从dconf中移除。不过它们现在由upower管理。按需编辑`/etc/UPower/Upower.conf`中upower设置。 
    
    /etc/UPower/UPower.conf
    
    PercentageLow=10
    PercentageCritical=3
    PercentageAction=2
    CriticalPowerAction=HybridSleep

#####  电源模式

安装 [gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 的可选依赖 [power-profiles-daemon](</wzh/index.php?title=Power-profiles-daemon&action=edit&redlink=1> "Power-profiles-daemon（页面不存在）") 以支持电源配置文件。 由于 _gnome-shell_ 和 GNOME 设置都请求在启动时激活 `power-profiles-daemon` 服务，所以不需要特意将其[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")。 

当服务激活时，可以通过 GNOME 设置的 _电源_ 选项和系统菜单管理电源配置文件。 

####  录屏

内建的截屏工具没有默认录屏选项。安装 [gnome-shell](<https://archlinux.org/packages/?name=gnome-shell>)包的可选依赖 [gst-plugin-pipewire](<https://archlinux.org/packages/?name=gst-plugin-pipewire>)包 以启用录屏功能。 

###  使用不同的窗口管理器

GNOME Shell 不支持更改[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器"), 但是 [GNOME Flashback](<../zh-cn/GNOME_Flashback.html> "GNOME Flashback") 提供使用 Metacity 和 [Compiz](<../zh-cn/Compiz.html> "Compiz") 的session。此外，可以通过[自定义 GNOME sessions](<../zh-cn/GNOME/Tips_and_tricks.html#Custom_GNOME_sessions> "GNOME/Tips and tricks") 来使用别的组件。 

将 GNOME Shell替换为不同的 [Wayland compositor](</wzh/index.php?title=Wayland_compositor&action=edit&redlink=1> "Wayland compositor（页面不存在）") 将会导致[gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 （GNOME 设置）的部分设置显示错误。 _gnome-control-center_ 依然可以正常工作，但因为 [mutter](<https://archlinux.org/packages/?name=mutter>)包 （GNOME Shell） 无法用于提供这些设置以填充这些区域，他们将不再奇效或无法准确反映你的设置。这些设置包括蓝牙，显示以及鼠标/触控板等。 

##  参见

  * [官方网站](<https://www.gnome.org/>)
  * [Contributing to GNOME, feature requests, bugs, code](<https://blogs.gnome.org/tbernard/2021/06/15/community-power-2/>)
  * [GNOME-shell 扩展](<https://extensions.gnome.org/>)
  * 主题、图标和壁纸： 
    * [GNOME Art](<https://art.gnome.org/>)
    * [GNOME 外观](<https://www.gnome-look.org/>)
  * GTK/GNOME 程序： 
    * [GNOME 文件管理](<https://www.gnomefiles.org/>)
    * [GNOME 项目列表](<https://www.gnome.org/projects/>)
  * [自定义 GNOME Shell](<https://blog.fpmurphy.com/2011/03/customizing-the-gnome-3-shell.html>)
  * GNOME 代码和镜像: 
    * [GNOME GitLab](<https://gitlab.gnome.org/>)
    * [GNOME Github 镜像](<https://github.com/GNOME>)
