相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [KDE](<../zh-cn/KDE.html> "KDE")
  * [udisks](<../zh-cn/Udisks.html> "Udisks")

**翻译状态：**

  * 本文（或部分内容）译自 [Dolphin](<https://wiki.archlinux.org/title/Dolphin> "arch:Dolphin")，最近一次同步于 2025-07-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dolphin?diff=0&oldid=840405>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dolphin_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Dolphin](<https://www.kde.org/applications/system/dolphin/>) 是 KDE 的默认文件管理器。请参阅 [Dolphin 模拟器](<../zh-cn/Dolphin_%E6%A8%A1%E6%8B%9F%E5%99%A8.html> "Dolphin 模拟器")来了解与之重名的[游戏机模拟器](<../zh-cn/%E6%B8%B8%E6%88%8F%E6%9C%BA%E6%A8%A1%E6%8B%9F%E5%99%A8.html> "游戏机模拟器")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dolphin](<https://archlinux.org/packages/?name=dolphin>)包 软件包. 

###  插件

  * [audiocd-kio](<https://archlinux.org/packages/?name=audiocd-kio>)包: 添加音频CD支持
  * [baloo](<https://archlinux.org/packages/?name=baloo>)包: 添加标签支持 (查看 [#文件标签](<#%E6%96%87%E4%BB%B6%E6%A0%87%E7%AD%BE>))
  * [dolphin-plugins](<https://archlinux.org/packages/?name=dolphin-plugins>)包: 添加 [Git](<../zh-cn/Git.html> "Git"), [Mercurial](</wzh/index.php?title=Mercurial&action=edit&redlink=1> "Mercurial（页面不存在）") 和 [Dropbox](<../zh-cn/Dropbox.html> "Dropbox") 支持
  * [kio-admin](<https://archlinux.org/packages/?name=kio-admin>)包 作为管理员来管理文件
  * [kompare](<https://archlinux.org/packages/?name=kompare>)包: 对比文件(或者选择两个文件 _，{右键} > 使用……打开 > {你的对比工具}_.)
  * [konsole](<https://archlinux.org/packages/?name=konsole>)包: 聚合的终端面板

**注意：** 一些插件可能仍需要通过以下步骤启用： _配置 > 配置 Dolphin... > 右键菜单_

###  文件预览

  * [ffmpegthumbs](<https://archlinux.org/packages/?name=ffmpegthumbs>)包: 预览视频文件 (基于ffmpeg)
  * [icoutils](<https://archlinux.org/packages/?name=icoutils>)包 : 预览 _*.ico_ , _*.cur_ 文件和嵌入了图标的 _*.exe_
  * [kde-thumbnailer-apk](<https://aur.archlinux.org/packages/kde-thumbnailer-apk/>)AUR: 预览 _*.apk_ 文件
  * [kdegraphics-thumbnailers](<https://archlinux.org/packages/?name=kdegraphics-thumbnailers>)包: 图像文件、PDF 与 Blender _*.blend_ 文件
  * [kimageformats](<https://archlinux.org/packages/?name=kimageformats>)包: Gimp _.xcf_ 、 _.heic_ 文件（用[libheif](<https://archlinux.org/packages/?name=libheif>)包）
  * [qt6-imageformats](<https://archlinux.org/packages/?name=qt6-imageformats>)包 : _.webp_ 、 _.tiff_ 、 _.tga_ 、 _.jp2_ 文件
  * [libappimage](<https://archlinux.org/packages/?name=libappimage>)包 : 预览嵌入了图标的 _*.AppImage_ 中的图标
  * [resvg](<https://aur.archlinux.org/packages/resvg/>)AUR: 快速准确地预览SVG图像缩略图
  * [kdesdk-thumbnailers](<https://archlinux.org/packages/?name=kdesdk-thumbnailers>)包: 缩略图系统的插件
  * [raw-thumbnailer](<https://aur.archlinux.org/packages/raw-thumbnailer/>)AUR: 预览 _*.raw_ 文件
  * [taglib](<https://archlinux.org/packages/?name=taglib>)包 : 音频文件

**注意：** 预览一些特殊的文件类型必须在 Previews for specific file-types must be enabled in _配置 > 配置 Dolphin... > 界面 > 预览_.

**注意：** 要启用 resvgAUR 代替内置的 SVG 缩略图编辑器，请关闭 SVG 图像。

##  配置

###  单击打开文件夹/文件

配置单击打开文件，你需要安装[qt6ct](<https://archlinux.org/packages/?name=qt6ct>)包并在终端运行它，然后它会在‘界面’标签处为你提供单击打开文件、更改主题等的选项。 

如果你使用Kvantum主题引擎——打开 _kvantum manager > 配置当前主题 > 杂项 > 点击行为。_

###  更改默认终端模拟器

Dolphin和其他KDE软件默认使用[konsole](<https://archlinux.org/packages/?name=konsole>)包。你可以运行`kcmshell6 componentchooser`并且在 _其它..._ 弹窗中选择你的终端模拟器或者在弹窗选择区域输入运行命令以更改默认终端模拟器。（第二个选项将会为这个命令创建一个新的本地桌面快捷方式） 

例如，为了能让Dolphin在 [alacritty](<../zh-cn/Alacritty.html> "Alacritty") 中打开 [tmux](<../zh-cn/Tmux.html> "Tmux") ，在选择`Other...` 后输入 `alacritty -e tmux` 。 

这个设置也可以通过修改`~/.config/kdeglobals`的配置文件来更改。例如，在`[General]`区域添加 alacritty 来使用alacritty： 
    
    TerminalApplication=alacritty
    TerminalService=Alacritty.desktop

在 `TerminalApplication` 输入一个命令，在 `TerminalService` 输入一个桌面快捷方式（`TerminalService`应该是可选的） 

**注意：** 这不会影响在Dolphin窗口中的终端（使用F4打开的）

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** This does (only) work in KDE and might not be dolphin related and might not work in many other WMs.（在 [Talk:Dolphin](<../zh-cn/Talk:Dolphin.html>) 中讨论）

你可以通过 _键盘 > 快捷键_来选择你喜欢的终端并且为其设置一个 _运行_ 快捷键为`Ctrl+Alt+T` 以覆写Konsole的快捷键。请注意，以这种方式打开的终端可能不会遵循你在终端配置文件中设置的终端背景颜色，但否则它应该与在窗口中运行的实例一样。 

### KIO slaves

Dolphin 使用 _KIO slaves_ 进行网络访问、垃圾箱和其他功能，这与使用 [GVFS](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS") 的 [GTK](<../zh-cn/GTK.html> "GTK") 文件管理器不同。可用协议显示在位置栏（可编辑模式）[[1]](<https://docs.kde.org/stable5/en/dolphin/dolphin/location-bar.html#location-bar-editable>)。要快速将它们添加为书签，请在工作区中单击鼠标右键，然后选择“添加到常用位置”。 

您可以手动安装 KIO slaves。例如，要在 Dolphin 中浏览您的 Google 云端硬盘，请安装 [kio-gdrive](<https://archlinux.org/packages/?name=kio-gdrive>)包。 

## Tips and Tricks

###  文件标签

Dolphin 为文件标签提供了广泛的支持。您可以通过右键单击文件并选择 _分配标签_ 来向文件添加标签。您可以在“属性”菜单或“信息”面板查看文件上的标签。 

Dolphin 使用 `user.xdg.tags` [extended attribute](</wzh/index.php?title=Extended_attributes&action=edit&redlink=1> "Extended attributes（页面不存在）")直接将标签与每个文件一起存储。Baloo 将这些标签索引到自己的数据库中，以便快速搜索，并维护所有已知标签的列表。 

激活[Baloo](<../zh-cn/Baloo.html> "Baloo") 来在位置面板中展示所有被索引的标签并且可以通过搜索文件标签来搜索文件。 

###  隐藏自定义文件/目录

文件/目录 可以通过创建`.hidden`文件，并在里面写入文件/目录的名字（一行一个）来隐藏 

###  创建自定义服务菜单

你可以通过在以下路径中添加`*.desktop`来为dolphin添加自定义服务菜单入口（见 [[2]](<https://develop.kde.org/docs/apps/dolphin/service-menus/>)） 

  * `~/.local/share/kio/servicemenus/`
  * `/usr/share/kio/servicemenus/`

**注意：** Desktop 入口 **必须** 是可执行的以在dolphin中展出
    
    gamemode.desktop
    
    [Desktop Entry]
    Type=Service
    MimeType=application/*;
    Actions=runWithGamemode
    
    [Desktop Action runWithGamemode]
    Name=Run with Gamemode
    Name[de]=Mit Gamemode ausführen
    Icon=input-gaming
    Exec=gamemoderun %u

这个添加`Run with Gamemode`菜单项在所有 _应用程序_ [mime types](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "XDG MIME 应用程序")

**提示：** To create a servicemenu for all file-types, use the `application/octet-stream` mimetype.

##  故障排除

###  设备名称显示为“X GiB Harddrive”

创建一个文件系统标签或分区标签，Dolphin 会在设备列表中显示此标签，而不是大小。请参见[块设备持久化命名#by-label](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#by-label> "块设备持久化命名"). 

###  在外部驱动器上将文件移动到废纸篓需要很长时间

若要将文件移入废纸篓，用户必须具有对废纸篓的独占访问权限。理由是您不希望其他人看到您删除的内容。为此，在外部驱动器上创建了一个文件夹 `.Trash-1000/` ，具有权限模式`700`。 

如果无法设置正确的访问权限，dolphin 会（与 GNOME 不同）将文件移动到主目录中的垃圾箱中，这需要时间。 

要安装 U 盘/外部 HDD，Dolphin 使用 [Udisks](<../zh-cn/Udisks.html> "Udisks")。FAT32 / EXFAT / NTFS 不支持 UNIX 文件权限，udisk 默认以模式 755 挂载它们。要配置 udisk 以使用模式 700 挂载这些驱动器，请查看文件 `/etc/udisks2/mount_options.conf.example` 。复制文件（名称应以 .conf 结尾），取消对相关部分的注释，并将三个文件系统添加到带有 xyz_defaults 选项 `fmask=177,dmask=077` 的行中。 

(背景信息：[[3]](<https://bugs.kde.org/show_bug.cgi?id=76380#c62>), [[4]](<https://invent.kde.org/frameworks/kio/-/merge_requests/125>)) 

###  透明字体

使用 [GTK Qt 样式](<../zh-cn/%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html#QGtkStyle> "统一 Qt 和 GTK 应用程序的外观")时，选择框中的字体可能会变得透明。原生 Qt 样式（如 _Cleanlook_ s 和 _Oxygen_ ）不受影响。 

###  已安装SMB共享上的崩溃

参见 [Samba#无法覆盖文件。](<../zh-cn/Samba.html#Unable_to_overwrite_files,_permissions_errors> "Samba"). 

###  图标不显示

如果 Dolphin 没有显示图标，安装并运行 [qt6ct](<https://archlinux.org/packages/?name=qt6ct>)包，在图标主题选项卡中选择一个 _图标主题_ ，然后 _应用_ 。 

如果图标仍未在 Dolphin 中显示，请在你的[xprofile](<../zh-cn/Xprofile.html> "Xprofile")中将 `QT_QPA_PLATFORMTHEME` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")设置为 `qt6ct` 。或者，使用`platformtheme`标志启动 Dolphin： 
    
    $ dolphin --platformtheme qt6ct
    
此外，当您使用不常见、不完整的图标主题时，请确保安装并继承备份图标主题，例如 _hicolor_ 或 _Adwaita_ 。 

###  图标太大

如果在 KDE 环境之外的 Dolphin 上图标过大，请用以下方法启动它： 
    
    XDG_CURRENT_DESKTOP=KDE KDE_SESSION_VERSION=6 **QT_AUTO_SCREEN_SCALE_FACTOR=0** dolphin
    
###  不匹配的文件夹视图背景颜色

在 Plasma 以外的其他位置运行 Dolphin 时，文件夹视图窗格中的背景颜色可能与系统 Qt 主题不匹配。这是因为 Dolphin 从 `[Colors:View]` 中 `~/.config/kdeglobals`
    
    ~/.config/kdeglobals
    
    ...
    [Colors:View]
    BackgroundNormal=#2E2E2E
    ...

如果您在文件夹视图窗格周围看到蓝色边框（如果您处于拆分视图中，则只会在焦点窗格周围），您可以通过 qt6ct 应用程序应用 `fusion-fixes.qss` 样式表来摆脱它。这个[答案](<https://unix.stackexchange.com/a/683366>)描述了如何让 adwaita 黑暗主题在 Gnome 下为 dolphin 工作。 

或者，使用 [kvantum](<https://archlinux.org/packages/?name=kvantum>)包 来管理您的 Qt6 主题。有关使用说明，请参阅[Kvantum](<https://github.com/tsujan/Kvantum/blob/master/Kvantum/README.md>)项目主页。 

###  Zsh 配置文件未加载集成终端（Zsh profile not loading in integrated terminal）

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 这个 _issue_ 不仅限于 Zsh;默认情况下，Konsole （以及 Konsolepart） 不会启动登录 shell。 `zprofile` 应该在启动会话时由[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")加载（就像由 [SDDM](<../zh-cn/SDDM.html> "SDDM")[[5]](<https://github.com/sddm/sddm/blob/develop/data/scripts/Xsession>)[[6]](<https://github.com/sddm/sddm/blob/develop/data/scripts/wayland-session>) 完成的那样），而不是由终端模拟器加载。（在 [Talk:Dolphin](<../zh-cn/Talk:Dolphin.html>) 中讨论）

如果您的 zsh 配置文件未加载，请尝试编辑您当前的配置文件。右键单击集成终端，然后单击 _编辑当前配置文件..._ 并将启动命令编辑为 `/bin/zsh --login`

###  GTK 应用程序未使用Dolphin

参见[统一 Qt 和 GTK 应用程序的外观#一致的文件对话框](<../zh-cn/%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html#%E4%B8%80%E8%87%B4%E7%9A%84%E6%96%87%E4%BB%B6%E5%AF%B9%E8%AF%9D%E6%A1%86> "统一 Qt 和 GTK 应用程序的外观"). 

###  无法安装任何右键菜单插件

当您转到Dolphin菜单 _配置 >配置 Dolphin>右键菜单>下载新服务_并尝试安装任何服务时，您会收到以下错误消息： 
    
    /usr/bin/servicemenuinstaller: error while loading shared libraries: libpackagekitqt6.so.1: cannot open shared object file: No such file or directory
    
这可以通过安装 [packagekit-qt6](<https://archlinux.org/packages/?name=packagekit-qt6>)包 来解决。然后重新启动 Dolphin。 

###  在其他[Window manager](<../zh-cn/Window_manager.html> "Window manager")运行[tong chang de](<../zh-cn/Window_manager.html> "Window manager")，Dolphin无法找到应用

你可以通过安装 [archlinux-xdg-menu](<https://archlinux.org/packages/?name=archlinux-xdg-menu>)包 软件包，并且运行： 
    
    $ XDG_MENU_PREFIX=arch- kbuildsycoca6 --noincremental
    
这更新KService 桌面文件系统配置文件缓存（见[kbuildsycoca6(8)](<https://man.archlinux.org/man/kbuildsycoca6.8>)），很多KDE软件依赖它来选择桌面入口。`--noincremental`参数是可选的。由于[archlinux-xdg-menu](<https://archlinux.org/packages/?name=archlinux-xdg-menu>)包会创建一个带有`arch-`的 [XDG桌面菜单](<https://specifications.freedesktop.org/menu-spec/latest/>)（见[xdg-menu](<../zh-cn/Xdg-menu.html> "Xdg-menu")），因此 `XDG_MENU_PREFIX`是必需的。 

这个XDG 桌面菜单文件可以在`/etc/xdg/menus/*-applications.menu` 找到。 

通常你不需要安装`kbuildsycoca6`，因为这是dolphin依赖的包[kservice](<https://archlinux.org/packages/?name=kservice>)包的一部分 

**注意：** 这个解决方案仅仅是重新构建缓存并且不会使它更新

##  参见

  * [Wikipedia:Dolphin (file manager)](<https://en.wikipedia.org/wiki/Dolphin_\(file_manager\)> "wikipedia:Dolphin \(file manager\)")
  * [KDE 用户群: Dolphin](<https://userbase.kde.org/Dolphin>)
  * [Dolphin 手册](<https://docs.kde.org/stable5/en/dolphin/dolphin/index.html>)
