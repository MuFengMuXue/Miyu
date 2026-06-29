摘自 [LXDE.org | LXDE官方主页](<https://lxde.org/>): 

    _"Lightweight X11 Desktop Environment" 是一种极快且节能的桌面环境。由一个国际开发者社区维护，它拥有漂亮的界面、多语言支持、标准键盘快捷键，以及诸如选项卡式文件浏览等额外功能。LXDE比其他环境使用更少的CPU和RAM。它专为具有低硬件规格的云计算机而设计，例如网书、移动设备（如MIDs）或老旧计算机。_

##  安装

使用LXDE最少需要安装 [lxde-common](<https://archlinux.org/packages/?name=lxde-common>)包, [lxsession](<https://archlinux.org/packages/?name=lxsession>)包, [openbox](<https://archlinux.org/packages/?name=openbox>)包(或者其他窗口管理器）。[lxde](<https://archlinux.org/groups/x86_64/lxde/>)包组包含完整的桌面。 

###  GTK+ 3 版本

你可以安装 [lxde-gtk3](<https://archlinux.org/groups/x86_64/lxde-gtk3/>)包组 软件包组来试用这个尚在实验阶段的版本. 

它几乎可以正常工作，但是可能会有一些问题，包括： [gpicview](<https://sourceforge.net/p/lxde/bugs/769/>), [lxappearance-obconf](<https://sourceforge.net/p/lxde/bugs/768/>), [lxlauncher](<https://sourceforge.net/p/lxde/bugs/803/>) 和 [lxpanel](<https://sourceforge.net/p/lxde/bugs/773/>). 

##  运行 LXDE

###  显示管理器

[LXDM](<../zh-cn/LXDM.html> "LXDM")是LXDE的默认显示管理器，并作为[lxde](<https://archlinux.org/groups/x86_64/lxde/>)包组组的一部分。另请参见[Display manager](<../zh-cn/Display_manager.html> "Display manager")。 

###  命令行

使用 "startx"，你需要在你的[xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")文件最后添加 
    
    ~/.xinitrc
    
    exec startlxde

另见[Start X at login](</wzh/index.php?title=Start_X_at_login&action=edit&redlink=1> "Start X at login（页面不存在）")

##  小提示

###  应用程序配置项

应用程序菜单是通过解析放在`/usr/share/applications/`和`~/.local/share/applications/`中的`.desktop`文件实现的。要添加或编辑菜单中的项，请见[desktop entries](<../zh-cn/Desktop_entries.html> "Desktop entries")。可在[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中找到第三方的菜单编辑器（如[lxmed](<https://aur.archlinux.org/packages/lxmed/>)AUR）。同时也有官方的菜单编辑器，如[alacarte](<https://archlinux.org/packages/?name=alacarte>)包（gnome）和[mozo](<https://archlinux.org/packages/?name=mozo>)包（mate）等。 

###  程序自动开启

应用程序可以用以下方式设置自动打开： 

  * 使用`.desktop`文件

LXDE 工具 [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart")

  * 使用LXsession

` ~/.config/lxsession/LXDE/autostart`中的每一行表示要执行的命令。如果一行以`@`开头，并且其后的命令崩溃，则该命令将自动重新执行。例如： 
    
    ~/.config/lxsession/LXDE/autostart
    
    @lxterminal
    @leafpad
    
**注意：** 这些命令 _不_ 以"&"结尾。

也有一个全局自启动文件，位于`/etc/xdg/lxsession/LXDE/autostart`。 

**注意：** 如果两个文件都存在，LXsession只执行v0.4.9之后的本地文件

###  鼠标键盘动作

鼠标和键绑定（即键盘快捷键）是使用Openbox实现的。LXDE用户应该参考 [Openbox 维基](<http://openbox.org/wiki/Help:Bindings>)来编辑 `~/.config/openbox/lxde-rc.xml`. 

[obkey](<https://aur.archlinux.org/packages/obkey/>)AUR 包提供了一个可选的图形用户界面，用于编辑键位绑定。默认情况下，它编辑 `rc.xml`，但您可以按照以下方式将其定向到LXDE配置文件中： 
    
    $ obkey ~/.config/openbox/lxde-rc.xml
    
请参见 [[1]](<https://code.google.com/p/obkey/>) 来获取更多信息 

###  光标

[lxappearance](<https://archlinux.org/packages/?name=lxappearance>)包 包是一个图形化工具，用于设置 [GTK](<../zh-cn/GTK.html> "GTK") 的外观和感觉，包括光标主题。使用LXAppearance配置的设置将被写入到 `~/.gtkrc-2.0`, `~/.config/gtk-3.0/settings.ini` 和 `~/.icons/default/index.theme` 文件中。请参见 [Cursor themes](<../zh-cn/Cursor_themes.html> "Cursor themes")。 

###  任务栏时间

您可以右键单击面板上的数字时钟小插件，并使用strftime格式设置它显示当前时间的方式。请参见 [strftime(3)](<https://man.archlinux.org/man/strftime.3>)。 

###  字体设置

[lxappearance-obconf](<https://archlinux.org/packages/?name=lxappearance-obconf>)包 用于配置 [Openbox](<../zh-cn/Openbox.html> "Openbox") 设置。此外，还可以参考 [Font configuration](<../zh-cn/Font_configuration.html> "Font configuration")。 

###  键盘布局

[lxpanel](<https://archlinux.org/packages/?name=lxpanel>)包 包括一个键盘布局小程序。 请参阅 [Keyboard configuration in Xorg](</wzh/index.php?title=Keyboard_configuration_in_Xorg&action=edit&redlink=1> "Keyboard configuration in Xorg（页面不存在）") 以获得通用指令，以及 [#程序自动开启](<#%E7%A8%8B%E5%BA%8F%E8%87%AA%E5%8A%A8%E5%BC%80%E5%90%AF>)以在LXDE中自动启动 _setxkbmap_ 。 

###  锁屏

LXDE本身不提供屏幕锁的功能。请参见 [List of applications/Security#Screen lockers](<../zh-cn/List_of_applications/Security.html#Screen_lockers> "List of applications/Security") 和 [#程序自动开启](<#%E7%A8%8B%E5%BA%8F%E8%87%AA%E5%8A%A8%E5%BC%80%E5%90%AF>)相关说明来启动它们。 

_Screen Lock_ 图标执行的脚本（位于 `/usr/bin/lxlock`）会搜索一些众所周知的屏幕锁定程序，并使用找到的第一个程序锁定屏幕。请参见 GitHub 上的 [lxlock](<https://github.com/lxde/lxsession/blob/master/lxlock/lxlock>)。 

`/etc/xdg/lxsession/LXDE/autostart` 文件（位于 [lxde-common](<https://archlinux.org/packages/?name=lxde-common>)包 包中）列出了 [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver")，它将自动启动。 

请参阅 [DPMS](<../zh-cn/Display_Power_Management_Signaling.html> "DPMS")，了解如何在没有外部程序的情况下控制屏幕保护。 

###  LXPanel中的图标

LXpanel 使用的默认图标存储在 `/usr/share/pixmaps/` 中，任何自定义图标也应该保存在这里。 

要更改应用程序的默认图标，请参考 [Desktop entries#Icons](<../zh-cn/Desktop_entries.html#Icons> "Desktop entries")。 

###  LXPanel中的菜单

面板的菜单可以在 `/etc/xdg/menus/lxde-applications.menu` 中进行配置，遵循 [xdg-menu](<../zh-cn/Xdg-menu.html> "Xdg-menu") 格式，以便与其他会话（特别是 [MATE](<../zh-cn/MATE.html> "MATE")）中的应用程序配合使用，以增加 LXDE 缺乏的某些功能。 

###  使用不同的窗口管理器

LXsession 使用 `~/.config/lxsession/LXDE/desktop.conf` 文件中定义的 [window manager](<../zh-cn/Window_manager.html> "Window manager") （默认为 [Openbox](<../zh-cn/Openbox.html> "Openbox")）。 如果该文件不存在，则会在 `/etc/xdg/lxsession/LXDE/desktop.conf` 中进行搜索。 

将文件中的 `openbox-lxde` 替换为您选择的窗口管理器： 

对于 metacity： 
    
    window_manager=metacity
    
对于 compiz： 
    
    window_manager=compiz
    
对于 [EXWM](<../zh-cn/EXWM.html#%E5%B5%8C%E5%85%A5_LXDE> "EXWM")： 
    
    window_manager=emacs
    
或者按照 [#程序自动开启](<#%E7%A8%8B%E5%BA%8F%E8%87%AA%E5%8A%A8%E5%BC%80%E5%90%AF>)部分中定义的方法使用 `_WM_ --replace`，其中 _WM_ 是要启动的窗口管理器可执行文件的名称。 这意味着每次登录时都会首先启动 _openbox_ ，然后立即被替换。 请注意，Openbox和LXDE不共享相同的 `rc.xml` 此键盘快捷键可能会有所不同。请参见 [xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）")。 

###  使用多个窗口管理器

LXDE默认情况下不启用混合，这会导致屏幕撕裂问题。如果您对此不满意，您可以牺牲更多的资源来启用窗口混合，要么安装混合管理器，要么将lxde替换为其他支持混合的窗口管理器。 

##  故障排除

###  一些程序不能运行

最近LXDE转向gtk3引入了一些错误，可能导致分段错误并阻止应用程序启动（尤其是自定义外观设置，也就是lxappearance）。在此问题完全修复之前，您可以尝试使用JWM来绕过gtk3的分段错误： 

  * 安装 JWM

    $ sudo pacman -S jwm
    
  * 将LXDE替换为jwm, 打开终端并运行：

    $ jwm
    
  * 这可能会导致一些小问题，但现在您应该能够正常打开segfault应用程序了
  * 完成后，请重新登录以刷新LXDE桌面

###  带有中文字符的NTFS

对于具有NTFS文件系统的存储设备，您需要安装 [NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G") 软件包。通常情况下，PCManFM与NTFS文件系统兼容良好，但是，对于使用NTFS的用户来说，存在一个问题，即如果您在NTFS文件系统上有包含非拉丁字符 （例如中文字符）的文件或目录， 当打开（或自动挂载）NTFS卷时，这些文件或目录的名称可能会消失。这是因为 lxsession mount-helper 未能正确解析策略和区域设置选项。对此有一个解决方法： 

创建一个新的 Bash 脚本，将其命名为 `/usr/local/bin/mount.ntfs-3g` 并包含以下内容： 
    
    #!/bin/bash
    /usr/bin/ntfs-3g $1 $2 -o locale=en_US.UTF-8
    
然后将其设置为可执行： 
    
    # chmod +x /usr/local/bin/mount.ntfs-3g
    
###  LXPanel崩溃问题解决方法

使用某些 [GTK](<../zh-cn/GTK.html> "GTK") 主题时，启动 _lxpanel_ 可能会导致以下错误： 
    
    lxpanel: cairo-scaled-font.c:459: _cairo_scaled_glyph_page_destroy: Assertion `!scaled_font->cache_frozen' failed.
    
在这种情况下，安装 [ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包。 

如果在浏览特定的Unicode网页时，lxpanel崩溃，请安装 [ttf-droid](<https://archlinux.org/packages/?name=ttf-droid>)包。 

###  LXPanel任务栏图标大小设置

正在运行的应用程序的图标与 _Panel Settings_ > _Geometry_ 设置的 _Icon size_ 不匹配，而是小4px， 这会导致其中一些图标模糊。为了在任务栏中显示清晰的32px图标，需要将 _Icon size_ 设置为36px，但这样做会使其他活动面板小工具的图标变模糊。为了解决这个问题，可以创建额外的面板，并通过在 _Panel Settings_ > _Geometry_ 中调整对齐和边距，使它们共同形成一个连续的面板。 

###  在LXTerminal中实现虚拟透明效果

最新版本的 [VTE terminal widget library](<https://wiki.gnome.org/Apps/Terminal/VTE>) 要求使用一个合成窗口管理器才能实现背景透明效果。而未维护的、遗留的 GTK 2 版本的 VTE 则采用伪透明技术，终端将显示桌面背景图像。如果你更喜欢伪透明效果，可以使用 [lxterminal-gtk2](<https://aur.archlinux.org/packages/lxterminal-gtk2/>)AUR 软件包安装 GTK 2 版本的 LXTerminal。 

###  光标太小

高分辨率屏显示光标过小，可以在[Gnome-look](<https://www.gnome-look.org/>)里找有36px或48px的光标主题文件并下载，之后在自定义外观里的光标下安装并选择使用。 

##  相关资源

  * [LXDE项目](<http://lxde.sourceforge.net>)
  * [最新组件](<https://sourceforge.net/project/showfiles.php?group_id=180858>)
  * [PCMan文件管理器](<https://sourceforge.net/project/showfiles.php?group_id=156956>)
