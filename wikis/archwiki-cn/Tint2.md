**翻译状态：**

  * 本文（或部分内容）译自 [Tint2](<https://wiki.archlinux.org/title/Tint2> "arch:Tint2")，最近一次同步于 2024-06-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tint2?diff=0&oldid=221864>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tint2_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Tint2](<https://code.google.com/p/tint2/>) 是一个 Linux 下的面板程序，被开发者称为“简洁轻量的面板/任务栏”。虽然不依赖什么软件包，它也可以配置成系统托盘、任务列表、电源监视器甚至时钟；外观配置也很简单。因此，对于默认的 WM 没有面板（比如 [Openbox](<../zh-cn/Openbox.html> "Openbox") ）的用户来说， Tinit2 是个不错的选择。 

##  安装

tint2 可以通过[安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)")软件包[tint2](<https://archlinux.org/packages/?name=tint2>)包获得，软件包位于[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")。 

##  配置

tint2 有个配置文件在`~/.config/tint2/tint2rc`。一个结构化的具有默认设定的配置文件将在tint2第一次运行时被创建。你可以按你的偏好来修改这个文件。在[这里](<https://code.google.com/p/tint2/wiki/Configure>)能找到tint2的完整的配置文档。可以配置字体，颜色，外观，位置，以及配置文件中更多的其他条目。tint2包现在包含一个GUI的配置工具可以通过下列命令访问： 
    
    $ tint2conf
    
另外，你可以通过图形界面 tintwizard 编辑你的tint2rc配置文件。 

###  tint2-git(AUR)的面板启动程序

在[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")的[tint2-git](<https://aur.archlinux.org/packages/tint2-git/>)AUR的版本中，tint2-git已经可以在面板中添加启动项。你需要手动修改配置文件来实现这个功能，因为 tintwizard 不提供添加启动器支持。 

**注意：** 当你手动修改添加启动器后又使用tintwizard来编辑你的tint2的配置文件，tintwizard将删除一切它无法识别的选项。比方说你的启动器。

把如下配置添加到你的tint2配置文件： 找到# `Panel:`
    
    # Panel
    panel_items = LTSBC
    
找到新的一节# `Launchers:`
    
    # Launchers
    launcher_icon_theme = LinuxLex-8
    launcher_padding = 5 0 10
    launcher_background_id = 9
    launcher_icon_size = 85
    launcher_item_app = /some/where/application.desktop
    launcher_item_app = /some/where/anotherapplication.desktop
    
`panel_items`是一个新的配置选项，它定义了tint2用下面的方式以便显示： 

L
    显示启动器
T
    显示任务栏
S
    显示系统托盘
B
    显示电池状态
C
    显示时钟
F
    添加一个可扩展的空白间隙（freespace）。你可以指定多个。如果同时存在“T”则不会生效。（自从0.12版本起）
E
    添加一个执行器插件。你可以指定多个。（自0.12.4版本起）
P
    添加一个推按钮。你可以指定多个。（自0.14版本起）
:
    添加一个分割符。你可以指定多个。（自0.13.0版本起）

###  OpenBox3的应用菜单

如果运行AUR里的[tint2-git](<https://aur.archlinux.org/packages/tint2-git/>)AUR，你可以在tint2面板上创建程序启动器。然而tint2还不支持嵌套菜单，所以没法原生使用程序启动菜单。接下来介绍如何为OpenBox3创建这样一个菜单。 

首先，你需要安装[openbox](<https://archlinux.org/packages/?name=openbox>)包，[tint2-git](<https://aur.archlinux.org/packages/tint2-git/>)AUR和[xdotool](<https://archlinux.org/packages/?name=xdotool>)包。然后，为Openbox的右键菜单创建一个键绑定： 
    
    ~/.config/openbox/rc.xml
    
    <keyboard>
     <!-- Keybinding for opening OpenBox menu -->
     <keybind key="C-A-space">
       <action name="ShowMenu"><menu>root-menu</menu></action>
     </keybind>
    </keyboard>

这就设置了启动OpenBox右键菜单的快捷键`Ctrl+Alt+Space`。测试快捷键是否生效： 
    
    $ xdotool key ctrl+alt+space
    
如果右键菜单顺利弹出，说明生效了。现在，在`/usr/share/applications/`目录下创建一个`open-openbox-menu.desktop`文件。把这行添加到文件里`Exec=xdotool key ctrl+alt+space`,其中，ctrl+alt+space是你选择的组合键。然后从文件管理器重新打开你的新的`open-openbox-menu.desktop`文件，你将看到右键菜单弹出。最后，将这个文件作为启动器添加到tint2。这样就得到了tint2上的程序启动菜单。如果你需要将菜单固定到某个位置，你可以使用 `xdotool mousemove x y` 。你可以创建一个脚本在 `open-openbox-menu.desktop` 中引用它，因为它涉及两个命令。 

更多的帮助请参考[Openbox Menus](<http://openbox.org/wiki/Help:Menus>)来创建你的个性菜单，[menumaker](<https://wiki.archlinux.org/title/Menumaker> "en:Menumaker")可以为大多数（几乎所有）你安装的程序生成一个完满的menu.xml文件。 

从0.14版本起，你可以创建按钮。只需将上面实例中的字符串“xdotool key ctrl+alt+space”添加到你想成为开始菜单o操作的按钮动作即可。 

###  音量控制

tint2不附带音量控制小程序，请参见[应用程序列表/多媒体#音量控制l](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E9%9F%B3%E9%87%8F%E6%8E%A7%E5%88%B6> "应用程序列表/多媒体")

##  运行tint2

### Openbox

你可以简单的通过这条命令运行tint2: 
    
    $ tint2
    
如果你想在[Openbox](<../zh-cn/Openbox.html> "Openbox")启动的时候启动tint2，修改~/.config/openbox/autostart添加如下: 
    
    tint2 &
    
注意：如果在~/.config/openbox没有autostart文件，你可以从/etc/xdg/openbox/autostart复制一份。 

OpenBox autostart选项的更多信息参见[Openbox help](<http://openbox.org/wiki/Help:Autostart>)。 

### Gnome

[Gnome](<../zh-cn/GNOME.html> "Gnome") 中，底部面板和任务栏被Activities视图所替代。要在原底部面板位置使用tint2，运行 
    
    # gnome-session-properties
    
并添加 
    
    # /usr/bin/tint2
    
使tint2作为gnome启动时运行的程序。gnome下次启动时，tint2将自动运行。 

### i3

在 [i3](<../zh-cn/I3.html> "I3") 中，要使用 tinit2 替代 i3status ，请在 i3 配置文件的末尾添加以下行： 
    
    ~/.config/i3/config
    
    exec --no-startup-id tint2

并注释或删除同一文件中的任何类似 `bar{status_command i3status}` 的部分。 

###  多个面板

通过使用不同的配置文件执行tint2,可以同时运行多个tint2面板： 
    
    tint2 -c _path/to/first/config/file_
    tint2 -c _path/to/second/config/file_
    
##  启用透明度

tint2支持假透明和真透明。使用哪种透明度由`tint2rc`配置文件中的`disable_transparency`选项控制。 

如果您想完全禁用透明度，需要使用`disable_transparency = 1`并将面板背景不透明度设置为100。例如： 
    
    background_color = #000000 100
    
###  假透明

对于假透明，您需要设置`disable_transparency = 1`。 

假透明会捕获桌面背景的一部分，并将其用作面板背景。因此，在激活tint2之前设置背景图像是很重要的。一个用于[Openbox](<../zh-cn/Openbox.html> "Openbox")的启动脚本示例可能是（使用[Feh](<../zh-cn/Feh.html> "Feh")设置背景）： 
    
    ...
    feh --randomize --no-fehbg --bg-fill ~/Pictures/wallpapers/
    (sleep 1 && tint2) &
    ...
    
###  真透明

对于真透明，您需要先激活像[picom](<../zh-cn/Picom.html> "Picom")这样的合成器，并设置`disable_transparency = 0`。 

不透明度由tint2配置文件中`background_color`属性的第二个参数控制[configuration file](<https://gitlab.com/o9000/tint2/blob/master/doc/tint2.md#backgrounds-and-borders>)。 

如果您在运行中进行更改，可能需要重启tint2以使透明度生效。 

##  全屏/覆盖

要强制tint2保持在应用程序（覆盖层）之上，您需要适当地设置panel_layer选项。当您使用 `Alt+Tab` 从全屏窗口切换到普通应用程序时，这可能会很有帮助。在 [Crunchbang论坛](<https://crunchbang.org/forums/viewtopic.php?pid=70048>)上有关于此的讨论。 
    
    #Panel
    panel_layer = top
    strut_policy = follow_size
    
##  第三方扩展

也可以通过其他应用程序扩展tint2。要添加第三方扩展，请检查官方Wiki的[Applets](<https://gitlab.com/o9000/tint2/wikis/ThirdPartyApplets>)部分。 

##  另请参阅

  * [Tint2 upstream wiki](<https://gitlab.com/o9000/tint2/wikis/home>)
