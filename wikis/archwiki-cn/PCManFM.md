**翻译状态：**

  * 本文（或部分内容）译自 [PCManFM](<https://wiki.archlinux.org/title/PCManFM> "arch:PCManFM")，最近一次同步于 2024-10-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/PCManFM?diff=0&oldid=809082>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PCManFM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LXDE](<../zh-cn/LXDE.html> "LXDE")
  * [Openbox](<../zh-cn/Openbox.html> "Openbox")
  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [SpaceFM](<../zh-cn/SpaceFM.html> "SpaceFM")
  * [Thunar](<../zh-cn/Thunar.html> "Thunar")
  * [GNOME Files](<../zh-cn/GNOME_Files.html> "GNOME Files")
  * [Nemo](</wzh/index.php?title=Nemo&action=edit&redlink=1> "Nemo（页面不存在）")

[PCManFM](<https://en.wikipedia.org/wiki/PCManFM> "wikipedia:PCManFM") 是一个非常快速和轻量级的文件管理器，也是 [LXDE](<../zh-cn/LXDE.html> "LXDE") 的标准文件管理器。它使用 [GTK](<../zh-cn/GTK.html> "GTK") 作为其 UI，并使用 [GVFS](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS") （在 GNOME 的 [GIO](<https://en.wikipedia.org/wiki/GIO_\(Software\)> "wikipedia:GIO \(Software\)") 库）提供虚拟文件系统功能，例如文件回收站功能和挂载远程文件系统的功能。 

[PCManFM-Qt](<https://github.com/lxqt/pcmanfm-qt>)是使用[Qt](<../zh-cn/Qt.html> "Qt")的版本，是[LXQt]] 的标准文件管理器。尽管使用 Qt作为UI工具包，但PCManFM-Qt保留了[GVFS](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS")，而非使用KDE的 [KIO](<https://en.wikipedia.org/wiki/KIO> "wikipedia:KIO") [[1]](<https://blog.lxde.org/2013/02/19/pcmanfm-file-manager-is-ported-to-qt/>)。从本质上讲，这两个文件管理器都与桌面环境无关。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")下列软件包之一： 

  * [GTK 2](<../zh-cn/GTK.html> "GTK"): [pcmanfm](<https://archlinux.org/packages/?name=pcmanfm>)包
  * [GTK 3](<../zh-cn/GTK.html> "GTK"): [pcmanfm-gtk3](<https://archlinux.org/packages/?name=pcmanfm-gtk3>)包
  * [Qt6](<../zh-cn/Qt.html> "Qt"): [pcmanfm-qt](<https://archlinux.org/packages/?name=pcmanfm-qt>)包

可选组件： 

  * [gvfs](<https://archlinux.org/packages/?name=gvfs>)包：提供回收站功能
  * [udisks](<../zh-cn/Udisks.html> "Udisks")：远程文件系统的挂载支持
  * [gvfs-smb](<https://archlinux.org/packages/?name=gvfs-smb>)包 支持SMB/CIFS

###  开发版本

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中提供开发版本: 

  * GTK 2: [pcmanfm-git](<https://aur.archlinux.org/packages/pcmanfm-git/>)AUR
  * Qt6: [pcmanfm-qt-git](<https://aur.archlinux.org/packages/pcmanfm-qt-git/>)AUR

##  桌面管理

如果要用PCManFM进行桌面管理，比如设置壁纸和显示桌面图标，使用这个命令： 
    
    $ pcmanfm --desktop
    
窗口管理器提供的桌面菜单会被PCManFM提供的桌面菜单所替换。如果要还原，在桌面首选项的高级选项卡中勾选`点击桌面时显示窗口管理器提供的菜单`选项。 

###  桌面首选项

如果使用窗口管理器提供的桌面菜单，请输入以下命令以随时设置或修改桌面首选项： 
    
    $ pcmanfm --desktop-pref
    
可以考虑给这条命令绑定快捷键或添加到原生桌面菜单中以方便使用。 

###  新建图标

文件可以直接拖放到桌面上。至于应用程序快捷方式，需要把它们的`.desktop`文件**复制** 到`~/Desktop`文件夹；不能拖放`.desktop`文件，否则就会是移动而不是复制，这会导致这个应用从应用启动器中消失。如果用命令行就应该是这样： 
    
    $ cp /usr/share/applications/name-of-application.desktop ~/Desktop
    
例如，下面的命令为 [lxterminal](<https://archlinux.org/packages/?name=lxterminal>)包 创建了一个桌面快捷方式： 
    
    $ cp /usr/share/applications/lxterminal.desktop ~/Desktop
    
使用 [XDG user directories](<../zh-cn/XDG_user_directories.html> "XDG user directories") 程序能创建自己的目录，无需再配置`$HOME` 环境变量。 

##  守护进程模式

如果你想在后台运行PCManFM ( 比如说要自动挂载移动硬盘等可移动介质)，使用： 
    
    $ pcmanfm --daemon-mode
    
一次只能有一个 PCManFM 实例作为守护进程运行。 

如果自动挂载失败，请参见 [udisks](<../zh-cn/Udisks.html> "Udisks"). 

##  开机自启

PCManFM 可以被[自启](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#On_Xorg_startup> "Autostarting")为一个[守护进程](<../zh-cn/Systemd.html> "Daemon")或用于管理桌面。 

##  其他特性和功能

经验不足的用户应该意识到，单独的文件管理器 ，尤其是当安装一个独立窗口管理器（如 [Openbox](<../zh-cn/Openbox.html> "Openbox")）将无法提供完整桌面环境（如 [Xfce](<../zh-cn/Xfce.html> "Xfce")和[KDE](<../zh-cn/KDE.html> "KDE") ）的用户所习惯的特性和功能。有关详细信息，请查看[文件管理器功能](<../zh-cn/File_manager_functionality.html> "File manager functionality")一文。 

##  提示与技巧

###  获取其他文件类型缩略图

查看[文件管理功能# PCManFM获取其他文件类型缩略图](<../zh-cn/File_manager_functionality.html#Use_PCManFM_to_get_thumbnails_for_other_file_types> "File manager functionality"). 

###  设置终端模拟器

在 _Edit > Preferences > Advanced_ 里面的 _Tools > Open Current Folder in Terminal_，你可以配置 PCManFM 调用的终端模拟器。 

###  集成压缩包管理器

可以在 _Edit > Preferences > Advanced_ 中设置集成的压缩包管理器。目前 PCManFM和PCManFM-Qt都支持 [file-roller](<https://archlinux.org/packages/?name=file-roller>)包, [xarchiver](<https://archlinux.org/packages/?name=xarchiver>)包 (或者 [xarchiver-gtk2](<https://archlinux.org/packages/?name=xarchiver-gtk2>)包), [engrampa](<https://archlinux.org/packages/?name=engrampa>)包, [ark](<https://archlinux.org/packages/?name=ark>)包 [[2]](<https://github.com/lxde/libfm/blob/5346a5390a0881d5713a71e15f371132680056ee/data/archivers.list>) [[3]](<https://github.com/lxqt/libfm-qt/blob/d5c15390917f55a0d8ee3283234addf4f8bf5a40/data/archivers.list>). PCManFM-Qt 还支持 [lxqt-archiver](<https://archlinux.org/packages/?name=lxqt-archiver>)包，这是 LXQt 的默认选择。 

###  将自定义项目添加到上下文菜单

PCManFM 支持[桌面文件规范扩展](<https://web.archive.org/web/20180627170128/http://www.nautilus-actions.org/?q=node/377>) (DES-EMA)，它允许您将任意项目添加到文件和目录的上下文菜单中。要添加你自己的项目，请创建（如果不存在）`~/.local/share/file-manager/actions/`文件夹并向其中添加`.desktop` 文件： 
    
    ~/.local/share/file-manager/actions/_action_.desktop
    
    [Desktop Entry]
    Type=Action
    Profiles=_profile_id_
    Name=_Action name in English_
    Name[_cc_]=_Action name in Language_
    Icon=_Icon name_
    # Example: Icon=text-editor
     
    [X-Action-Profile _profile_id_]
    MimeTypes=_MIME-types (semicolon separated)_
    Exec=_command and arguments_
    # Example: Exec=gedit %f

你可以通过列出其id（以分号分隔），将一个或多个配置文件绑定到单个操作。配置文件允许你指定要为哪些文件类型执行哪些命令，因此同一操作可以根据所选文件类型运行不同的命令。除了特定的 MIME 类型（例如：`text/plain`文本文件），你可以使用以下常规类型： 

  * `all/allfiles` \--文件；
  * `inode/directory` \-- 文件夹
  * `all/all` \-- 文件和文件夹。

**注意：** 可以使用 pkexec 以 root 身份运行命令，但直接调用它不起作用，您需要创建一个中间脚本，如 [LXDE 的 wiki](<https://web.archive.org/web/20220428194115/https://wiki.lxde.org/en/PCManFM#pkexec_method>)中所述。

###  “创建新的...”模板

模板文件保存在 `~/Templates` ，点击 _文件 >新建..._可以选择相应的模板。默认的模板是“创建文件夹”和“创建空白文件”。 

###  缩略图

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 使用现代 SSD 时，PCManFM 可以毫无问题地呈现包含数千个媒体文件的目录的缩略图。（在 [Talk:PCManFM](<../zh-cn/Talk:PCManFM.html>) 中讨论）

和其他一些文件管理器（例如 Nautilus）一样，PCManFM 将加载文件夹中所有图像的预览。为了不滥用 HDD，请将文件夹中的图像数量保持在 100 个之内。 

##  故障排除

###  “打开方式”对话框窗口为空

如果您在打开方式对话框中没有看到任何可供选择的应用程序，那么你可以试着卸载 [gnome-menus](<https://archlinux.org/packages/?name=gnome-menus>)包 然后安装 [lxmenu-data](<https://archlinux.org/packages/?name=lxmenu-data>)包。此外，设置如下环境变量： 

  * `XDG_MENU_PREFIX=lxde-`
  * `XDG_CURRENT_DESKTOP=LXDE`

###  列表中没有 "应用"

删掉 `$HOME/.cache/menus` 文件夹里的东西，然后重新运行 PCManFM。 

PCManFM 需要设置`XDG_MENU_PREFIX`环境变量。变量的值应与`/etc/xdg/menus/`文件夹中文件的开头部分匹配。 

参考 [#“打开方式”对话框窗口为空](<#%E2%80%9C%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F%E2%80%9D%E5%AF%B9%E8%AF%9D%E6%A1%86%E7%AA%97%E5%8F%A3%E4%B8%BA%E7%A9%BA>). 

参考获取更多信息[[4]](<https://bbs.archlinux.org/viewtopic.php?pid=1110903>) 以及Linux Mint论坛的[[5]](<https://forums.linuxmint.com/viewtopic.php?f=175&t=53986#p501920>)（特别推荐） 

###  无图标

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 当建议编辑配置文件时使用[Template:hc](<../zh-cn/Template:Hc.html> "Template:Hc")（在[Talk:PCManFM](<../zh-cn/Talk:PCManFM.html>)讨论）

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 我们是否应该建议编辑文件管理器的全局 gtk 配置?（在 [Talk:PCManFM](<../zh-cn/Talk:PCManFM.html>) 中讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 软件也支持 gtk3，尽管这里只引用了 gtk2 (在 [Talk:PCManFM](<../zh-cn/Talk:PCManFM.html>) 中讨论)

如果你用的是[窗口管理器](<../zh-cn/Window_manager.html> "Window manager")而不是[桌面环境](<../zh-cn/Desktop_environment.html> "Desktop environment")，而文件夹和文件没有图标，你需要指定 GTK 图标主题。 

例如，你安装了 [oxygen-icons](<https://archlinux.org/packages/?name=oxygen-icons>)包，在 `~/.gtkrc-2.0` **或者** `/etc/gtk-2.0/gtkrc` 里添加这一行： 
    
    gtk-icon-theme-name = "oxygen"
    
**注意：** 重启 PCManFM 才能生效。

或者，用一个不同的主题（gnome，hicolor和 locolor 三个主题除外）。用下面这个命令查看安装了的图标主题： 
    
    $ ls ~/.icons/ /usr/share/icons/
    
如果看着都不爽，那就用这个命令查看所有可以安装的图标主题，选一个来安装： 
    
    $ pacman -Ss icon-theme
    
**提示：** 如果想要有个图形界面，安装 [lxappearance](<https://archlinux.org/packages/?name=lxappearance>)包 并用它来设置图标主题。

###  鼠标按钮不能触发 "上一/下一 文件夹" 功能

用 [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") 来修复这个功能。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xbindkeys](<https://archlinux.org/packages/?name=xbindkeys>)包、[xvkbd](<https://aur.archlinux.org/packages/xvkbd/>)AUR，在 `~/.xbindkeysrc` 里添加以下内容： 
    
    ~/.xbindkeysrc
    
    # Sample .xbindkeysrc for a G9x mouse.
    "/usr/bin/xvkbd -text '\[Alt_L]\[Left]'"
     b:8
    "/usr/bin/xvkbd -text '\[Alt_L]\[Right]'"
     b:9

按键代码可以通过 [xorg-xev](<https://archlinux.org/packages/?name=xorg-xev>)包 获取。 

最后在 `~/.xinitrc` 里添加以下内容来在登录时触发 _xbindkeys_ 。 
    
    xbindkeys &
    
###  \--desktop 参数不生效或使X-server崩溃

确保你有 `~/.config/pcmanfm` 文件夹的所有权和写权限。 

通过使用 `--desktop-pref` 参数或者修改 `~/.config/pcmanfm/default/pcmanfm.config` 来设置桌面壁纸来解决问题。 

###  终端模拟器的高级配置没有保存

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 为什么 libfm 的配置文件默认没有权限（在 [Talk:PCManFM](<../zh-cn/Talk:PCManFM.html>) 中讨论）

请设置 libfm 配置文件的权限： 
    
    $ chmod -R 755 ~/.config/libfm
    $ chmod 644 ~/.config/libfm/libfm.conf
    
###  记住文件排序设置

在 _View > Sort Files_ 里可以设置文件排序，但是如果要让 PCManFM 记住这个设置，需要打开 _Edit > Preferences_ 然后再关掉，这样会让当前的sort_type 和 sort_by 的值写入 `~/.config/pcmanfm/LXDE/pcmanfm.conf` 文件。 

###  挂载设备时候提醒 "Not authorized"

在 `/etc/polkit-1/rules.d/00-mount-internal.rules` 文件里添加这个 [polkit](<../zh-cn/Polkit.html> "Polkit") 规则： 
    
    /etc/polkit-1/rules.d/00-mount-internal.rules
    
    polkit.addRule(function(action, subject) {
        if ((action.id == "org.freedesktop.udisks2.filesystem-mount-system" &&
           subject.local && subject.active && subject.isInGroup("storage")))
           {
              return polkit.Result.YES;
           }
     });

并且把你的用户添加到 `storage` [用户组](<../zh-cn/User_group.html> "User group")里： 
    
    # usermod -aG storage _username_
    
###  不支持操作

如果您忘记安装可选的依赖项 [gvfs](<https://archlinux.org/packages/?name=gvfs>)包，请先检查，否则请参阅[会话权限](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E4%BC%9A%E8%AF%9D%E6%9D%83%E9%99%90> "常规故障排除")一文。 

###  系统重新启动时忘记密码

如果合适，安装一个 keyring 应用程序，比如 [GNOME/Keyring](<../zh-cn/GNOME/Keyring.html> "GNOME/Keyring")，[KDE Wallet](<../zh-cn/KDE_Wallet.html> "KDE Wallet") 或者 [lxqt_wallet](<https://aur.archlinux.org/packages/lxqt_wallet/>)AUR 用于 网络共享或[SSH agent](<../zh-cn/SSH_%E5%AF%86%E9%92%A5.html#SSH_agent> "SSH 密钥")。 
