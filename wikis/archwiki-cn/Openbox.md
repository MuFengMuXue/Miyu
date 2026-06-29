**翻译状态：**

  * 本文（或部分内容）译自 [Openbox](<https://wiki.archlinux.org/title/Openbox> "arch:Openbox")，最近一次同步于 2021-07-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Openbox?diff=0&oldid=685513>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Openbox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 原文已同步更新翻译未完成. Unfinished translation started 2021-07-23.（在 [Talk:Openbox#](<../zh-cn/Talk:Openbox.html>) 中讨论）

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [File manager functionality](<../zh-cn/File_manager_functionality.html> "File manager functionality")
  * [Xdg-menu](<../zh-cn/Xdg-menu.html> "Xdg-menu")
  * [Oblogout](</wzh/index.php?title=Oblogout&action=edit&redlink=1> "Oblogout（页面不存在）")

Openbox 是一个轻量、强大且高度可定制的堆叠式[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")，它支持大量扩展标准。它可以单独作为某个[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")的一个基础组件独立构建和运行，也可以集成于其它桌面环境如[KDE](<../zh-cn/KDE.html> "KDE")或[Xfce](<../zh-cn/Xfce.html> "Xfce")中，作为备选窗口管理器。[LXDE](<../zh-cn/LXDE.html> "LXDE")和[LXQt](<../zh-cn/LXQt.html> "LXQt")桌面环境则是基于Openbox构建而成。 

##  安装

只需[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[openbox](<https://archlinux.org/packages/?name=openbox>)包软件包。也可以安装TTF字体，如[ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包和[ttf-liberation](<https://archlinux.org/packages/?name=ttf-liberation>)包。 

##  启动

###  单独运行

通过 [xinit](<../zh-cn/Xinit.html> "Xinit") 运行 `openbox` 或者 `openbox-session` 。 注意只有 `openbox-session` 支持 [#自动启动](<#%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8>). 

**注意：** 执行openbox-session后,屏幕上只会出现灰色的空白界面。 尝试移动你的鼠标并**右键单击** ，如果显示一个Openbox菜单，说明它真的在工作了。

###  其它桌面环境

**注意：**

  * 如果你把一个 [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境") 的原有窗口管理器替换为 Openbox，请记住 Openbox 不会提供任何的混成特效 (比如透明度)。 请参阅 [#混成特效](<#%E6%B7%B7%E6%88%90%E7%89%B9%E6%95%88>).
  * Openbox可以与GNOME应用程序一起工作(见[GTK#Client-side decorations](<../zh-cn/GTK.html#Client-side_decorations> "GTK")). [[1]](<https://icculus.org/pipermail/openbox/2014-April/008497.html>)

请参阅[桌面环境#使用其它窗口管理器](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html#%E4%BD%BF%E7%94%A8%E5%85%B6%E5%AE%83%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8> "桌面环境")。 

##  配置

**注意：** 本地配置文件总是会覆盖全局配置。

四个关键文件构成了 [openbox配置](<http://openbox.org/wiki/Configuration>)的基础，每个文件都有其独特的作用。它们分别是： `rc.xml`, `menu.xml`, `autostart`, 和 `environment`。 尽管这些文件将在下面进行更详细的讨论，但要开始配置Openbox，首先需要基于它们创建一个**本地** Openbox 配置文件 (即针对您特定的用户帐户) 。 这可以通过从**全局的** `/etc/xdg/openbox` 配置文件中复制它们作为模板来完成 (适用于任何和所有用户): 
    
    $ mkdir -p ~/.config/openbox
    $ cp -a /etc/xdg/openbox/ ~/.config/
    
### rc.xml

**提示：** 自定义键盘快捷键 (键绑定) 必须添加到此文件的 `<keyboard>` 部分， 并在 `<!-- Keybindings for running aplications -->` 标题下方添加。

`~/.config/openbox/rc.xml` 是主要的配置文件，负责确定整个会话的行为和设置，其中包括： 

  * 键盘快捷键 (e.g. starting applications; controlling the volume)
  * 主题
  * 桌面和虚拟桌面设置
  * 应用程序窗口设置

该文件也是预配置的，这意味着只需要修改现有内容就可以根据个人喜好自定义行为。 

**注意：** 仅当定义了 x 和 y 位置时，与每个监视器上的应用程序固定放置相关的每个应用程序的特定设置才能生效。

### menu.xml

`~/.config/openbox/menu.xml` 定义了桌面菜单的类型和行为，可以通过右键单击背景访问。 尽管提供的默认菜单是一个**静态菜单** (即在安装新应用程序时不会自动更新), 但也有可能使用**动态菜单** ，它们将自动更新。 

在 [#菜单](<#%E8%8F%9C%E5%8D%95>)部分下面详细讨论了可用的选项。 

###  自动启动

`openbox-session` 提供了两种自动启动机制： [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart") (仅在安装了 [python-pyxdg](<https://archlinux.org/packages/?name=python-pyxdg>)包 时可用) 和 [Openbox's own autostart mechanism](<http://openbox.org/wiki/Help:Autostart>). 

Openbox 自己的自动启动机制： 

  * 来源 `/etc/xdg/openbox/environment`
  * 来源 `~/.config/openbox/environment`
  * 运行 `/etc/xdg/openbox/autostart`
  * 运行 `~/.config/openbox/autostart`

解决`~/.config/openbox/autostart` 中命令顺序执行错误（或者被跳过）的问题通常可以通过增加小的延迟来解决。例如： 
    
    xset -b
    (sleep 3s && nm-applet) &
    (sleep 3s && conky) &
    
###  环境

`~/.config/openbox/environment` 可以用于导出和设置相关的环境变量，例如： 

  * 定义新的路径（例如执行需要将整个路径列出的命令）
  * 更改语言设置
  * 定义其他要使用的变量（例如，可以在此处列出对于GTK主题的修复）

###  主题 

安装 [obconf](<https://archlinux.org/packages/?name=obconf>)包 和/或 [lxappearance-obconf](<https://archlinux.org/packages/?name=lxappearance-obconf>)包 ，用于配置视觉设置和主题的图形界面。 

可以在 [openbox-themes](<https://aur.archlinux.org/packages/openbox-themes/>)AUR 软件包或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中找到大量精选的主题。一些 [GTK#Themes](<../zh-cn/GTK.html#Themes> "GTK") 也附带了Openbox主题。 安装时，Openbox特定和兼容的主题将被安装到 `/usr/share/themes` 目录，并且可以立即选择使用。 

[box-look.org](<https://www.box-look.org/browse/ord/latest/>) 是一个优秀且历史悠久的主题资源网站。 

[deviantART.com](<https://www.deviantart.com/>) 是另一个优秀的资源网站。在网上还可以找到更多的资源。 

####  编辑或创建

**提示：** 对于主题，最好将其复制到您的主目录而不是编辑在 `/usr/share/themes/`中找到的主题。这样做可以在出现任何问题时保留原始文件，并确保在更新时不会被覆盖您所做的更改。

在官方的 [openbox.org](<http://openbox.org/wiki/Help:Themes>) 网站上有详细介绍创建新主题或修改现有主题的过程。[obtheme](<https://aur.archlinux.org/packages/obtheme/>)AUR 是一个用户友好的图形界面工具，用于进行这些操作。 

###  图形界面配置

有几个图形界面应用程序可供选择，可以快速简便地配置您的Openbox桌面环境。 

  * **ObConf** — 一个基于GTK3的配置工具，用于Openbox窗口管理器。

     <http://openbox.org/wiki/ObConf:About> || [obconf](<https://archlinux.org/packages/?name=obconf>)包

  * **LXAppearance ObConf** — 这是一个用于配置Openbox的LXAppearance插件。请注意，该插件并不提供所有用于配置Openbox的选项，因此您可能仍然需要安装obconf来完成配置。

     <https://lxde.org> || [lxappearance-obconf](<https://archlinux.org/packages/?name=lxappearance-obconf>)包

  * **LXInput** — LXDE键盘和鼠标配置。

     <https://lxde.org> || [lxinput](<https://archlinux.org/packages/?name=lxinput>)包

  * **LXRandR** — LXDE显示器配置。

     <https://wiki.lxde.org/en/LXRandR>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-22 ⓘ] || [lxrandr](<https://archlinux.org/packages/?name=lxrandr>)包

  * **obkey** — 配置Openbox的键盘快捷键。

     <https://code.google.com/p/obkey/> || [obkey](<https://aur.archlinux.org/packages/obkey/>)AUR

  * **obapps** — Openbox中用于配置应用程序设置的图形化工具。

     <https://sourceforge.net/projects/obapps/> || [obapps](<https://aur.archlinux.org/packages/obapps/>)AUR

在 [#菜单](<#%E8%8F%9C%E5%8D%95>)部分讨论与配置Openbox桌面菜单相关的程序和应用程序。 

##  重新配置Openbox

**提示：** 如果还没有，为了方便起见，值得将此命令添加到菜单和/或键绑定中。

Openbox并不总是会在会话中自动反映对其配置文件所做的更改。因此，在编辑完配置文件之后，需要手动重新加载这些文件。要执行此操作，请输入以下命令： 
    
    $ openbox --reconfigure
    
打算将此命令作为键绑定添加到 `~/.config/openbox/rc.xml` ， 将命令列为 `reconfigure` 即可。 以下是一个示例，使用 `Super`+`F11` 键绑定： 
    
    <keybind key="W-F11">
      <action name="Reconfigure"/>
    </keybind>
    
##  键绑定

所有键绑定都必须添加到 `~/.config/openbox/rc.xml` 文件中，并放置在 `<!-- Keybindings for running aplications -->` 标题下方。然在这里提供了简要概述，但更详细的键绑定说明可以在[openbox.org](<http://openbox.org/wiki/Help:Bindings>) 网站上找到。 

键绑定可以使用以下语法添加到配置文件中： 
    
    <keybind key="**my-key-combination** ">
      <action name="**my-action** ">
        **...**
      </action>
    </keybind>
    
执行外部命令的操作名称是Execute。使用以下语法来定义要执行的外部命令： 
    
    <action name="Execute">
      <command>**my-command** </command>
    </action>
    
请参阅 [the Openbox wiki](<http://openbox.org/wiki/Help:Actions>) 以获取所有可用操作的列表。 

**提示：**[obkey](<https://aur.archlinux.org/packages/obkey/>)AUR 实用程序提供了一个图形界面来配置按键绑定。在使用 _obkey_ 之前，您应该使用 _obconf_ 来创建 `~/.config/openbox/rc.xml` 文件。

对于键位绑定，使用标准的字母数字键是很直观的，但其他类型的键，如 `modifiers`， `multimedia` 和 `navigation`，会分配特殊的名称。 

###  组合键 

`Modifier` 键在键绑定中起着重要作用（例如，按住。`shift` 键 或 `CTRL / control` 与其他键组合以执行某项操作）。使用修饰键有助于防止冲突的键绑定，即将两个或多个操作链接到同一个键或键组合。使用修饰键与其他键结合的语法是： 
    
    "<modifier>-<key>"
    
修饰符代码如下： 

  * `S`: Shift
  * `C`: Control / CTRL
  * `A`: Alt
  * `W`: Super / Windows
  * `M`: Meta
  * `H`: Hyper (如果它绑定到某个东西上)

###  多媒体键

在可用的情况下，可以设置适当的 `multimedia` 键来执行其预期的功能，例如控制音量和/或屏幕亮度。 这些通常会集成到 `function` 中，并通过相应的符号进行标识。请参见 [Extra keyboard keys](<../zh-cn/Extra_keyboard_keys.html> "Extra keyboard keys") 获取更多信息。 

音量和亮度的多媒体代码如下（请注意，命令仍然需要分配给它们才能实际发挥作用）: 

  * `XF86AudioRaiseVolume`: 增加音量
  * `XF86AudioLowerVolume`: 减小音量
  * `XF86AudioMute`: 静音/取消静音
  * `XF86MonBrightnessUp`: 增加屏幕亮度
  * `XF86MonBrightnessDown`: 降低屏幕亮度

要查看完整的XF86多媒体键列表，请参阅 [LQWiki:XF86 keyboard symbols](<https://wiki.linuxquestions.org/wiki/XF86_keyboard_symbols> "lqwiki:XF86 keyboard symbols")。 

####  音量控制

控制音量所使用的命令取决于音频播放系统是使用 [ALSA](<../zh-cn/ALSA.html> "ALSA")，[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")，还是 [OSS](<../zh-cn/Open_Sound_System.html> "OSS")。 

  * ALSA: 请参阅 [Advanced Linux Sound Architecture#Keyboard volume control](<../zh-cn/Advanced_Linux_Sound_Architecture.html#Keyboard_volume_control> "Advanced Linux Sound Architecture").
  * PulseAudio: 请参阅 [PulseAudio#Keyboard volume control](<../zh-cn/PulseAudio.html#Keyboard_volume_control> "PulseAudio")
  * OSS: 请参阅 [Open Sound System#Keyboard volume control](<../zh-cn/Open_Sound_System.html#Keyboard_volume_control> "Open Sound System").

###  导航键

这些是方向/箭头键，通常用于将光标向上、向下、向左或向右移动。以下是（自说明的）导航代码： 

  * `Up`: 上
  * `Down`: 下
  * `Left`: 左
  * `Right`: 右

##  菜单 

在Openbox中，有三种类型的菜单可供选择使用： `static`，`pipes` (动态) 和 `generators` (静态或动态). 这些菜单可以单独使用，也可以组合使用。 

###  静态菜单

As the name would suggest, this default type of menu does not change in any way, and may be manually edited and/or (re)generated automatically through the use on an appropriate software package. 

Fast and efficient, while this type of menu can be used to select applications, it can also be useful to access specific functions and/or perform specific tasks (e.g. desktop configuration), leaving the access of applications to another process (e.g. the [synapse](<https://archlinux.org/packages/?name=synapse>)包 or [xfce4-appfinder](<https://archlinux.org/packages/?name=xfce4-appfinder>)包 applications). 

The `~/.config/openbox/menu.xml` file will be the sole source of static desktop menu content. 

####  菜单生成器

[menumaker](<https://archlinux.org/packages/?name=menumaker>)包 automatically generates `xml` menus for several window managers, including Openbox, [Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox"), [IceWM](<../zh-cn/IceWM.html> "IceWM") and [Xfce](<../zh-cn/Xfce.html> "Xfce"). It will search for all installed executable programs and consequently create a menu file for them. It is also possible to configure MenuMaker to exclude certain application types (e.g. relating to [GNOME](<../zh-cn/GNOME.html> "GNOME") or [KDE](<../zh-cn/KDE.html> "KDE")), if desired. 

Once installed and executed, it will automatically generate a new `~/.config/openbox/menu.xml` file. To avoid overwriting an existing file, enter: 
    
    $ mmaker -v OpenBox3
    
Otherwise, to overwrite an existing file, add the `force` argument (`f`): 
    
    $ mmaker -vf OpenBox3
    
Once a new `~/.config/openbox/menu.xml` file has been generated it may then be manually edited, or configured using a GUI menu editor, such as [obmenu](<https://aur.archlinux.org/packages/obmenu/>)AUR. 

#### obmenu

**警告：**`obm-xdg` \- a pipe menu to generate a list of [GTK](<../zh-cn/GTK.html> "GTK") and [GNOME](<../zh-cn/GNOME.html> "GNOME") applications - is also provided with obmenu. However, it has long-running bugs whereby it may produce an invalid output, or even not function at all. Consequently it has been omitted from discussion.

[obmenu](<https://aur.archlinux.org/packages/obmenu/>)AUR is a "user-friendly" GUI application to edit `~/.config/openbox/menu.xml`, without the need to code in `xml`. 

#### xdg-menu

[archlinux-xdg-menu](<https://archlinux.org/packages/?name=archlinux-xdg-menu>)包 will automatically generate a menu based on `xdg` files contained within the `/etc/xdg/` directory for numerous Window Managers, including Openbox. Review the [Xdg-menu#OpenBox](<../zh-cn/Xdg-menu.html#OpenBox> "Xdg-menu") article for further information. 

####  登出菜单选项

**提示：** The commands provided can also be attached to [#键绑定](<#%E9%94%AE%E7%BB%91%E5%AE%9A>)

The `~/.config/openbox/menu.xml` file can be edited in order to provide a sub-menu with the same options as provided by [oblogout](<#oblogout>). The sample script below will provide all of these options, with the exception of the ability to lock the screen: 
    
    <menu id="exit-menu" label="Exit">
    	<item label="Log Out">
    		<action name="Execute">
    			<command>openbox --exit</command>
    		</action>
    	</item>
    	<item label="Shutdown">
    		<action name="Execute">
    			<command>systemctl poweroff</command>
    		</action>
    	</item>
    	<item label="Restart">
    		<action name="Execute">
    		        <command>systemctl reboot</command>
    		</action>
    	</item>
    	<item label="Suspend">
    		<action name="Execute">
    		        <command>systemctl suspend</command>
    		</action>
    	</item>
    	<item label="Hibernate">
    		<action name="Execute">
    		        <command>systemctl hibernate</command>
    		</action>
    	</item>
    </menu>
    
Once the entries have been composed, add the following line to present the sub-menu where desired within the main desktop menu (usually as the last entry): 
    
    <menu id="exit-menu"/>
    
###  管道菜单

**提示：** It is entirely feasible for a static menu to contain one or more pipe sub-menus. The functionality of some pipe menus may also rely on the installation of relevant software packages.

This type of menu is in essence a script that provides dynamic, refreshed lists on-the-fly as and when run. These lists may be used for multiple purposes, including to list applications, to provide information, and to provide control functions. Pre-configured pipe menus can be installed, although not from the [official repositories](<../zh-cn/Official_repositories.html> "Official repositories"). More experienced users can also modify and/or create their own custom scripts. Again, `~/.config/openbox/menu.xml` may and commonly will contain several pipe menus. 

####  范例 

  * [openbox-xdgmenu](<https://aur.archlinux.org/packages/openbox-xdgmenu/>)AUR: 快速将xdg菜单转换为xml管道菜单的转换器。
  * [obfilebrowser](<https://aur.archlinux.org/packages/obfilebrowser/>)AUR: 应用程序和文件浏览器
  * [obdevicemenu](<https://aur.archlinux.org/packages/obdevicemenu/>)AUR: 使用 [Udisks](<../zh-cn/Udisks.html> "Udisks") 管理可移动介质
  * [wifi pipe menu](<https://bbs.archlinux.org/viewtopic.php?pid=1345031>): 使用 [Netctl](<../zh-cn/Netctl.html> "Netctl") 进行无线网络连接

[Openbox.org](<http://openbox.org/wiki/Openbox:Pipemenus>) 还提供了更多的管道菜单列表。 

###  生成器

This type of menu is akin to those provided by the taskbars of desktop environments such as [Xfce](<../zh-cn/Xfce.html> "Xfce") or [LXDE](<../zh-cn/LXDE.html> "LXDE"). Automatically updating on-the-fly, this type of menu can be powerful and very convenient. It may also be possible to add custom categories and menu entries; read the documentation for your intended dynamic menu to determine if and how this can be done. 

A menu generator will have to be executed from the `~/.config/openbox/menu.xml` file. 

#### obmenu-generator

**提示：** icons can still be disabled in [obmenu-generator](<https://aur.archlinux.org/packages/obmenu-generator/>)AUR, even where enabled in `~/.config/openbox/rc.xml`.

[obmenu-generator](<https://aur.archlinux.org/packages/obmenu-generator/>)AUR is highly recommended despite being an unofficial package. With the ability to be used as a static or dynamic menu, it is highly configurable, powerful, and versatile. Menu categories and individual entries may also be easily hidden, customised, and/or added with ease. The [official homepage](<https://trizenx.blogspot.co.uk/2012/02/obmenu-generator.html>) provides further information and screenshots. 

Below is an example of how obmenu-generator would be dynamically executed without icons in `~/.config/openbox/menu.xml`: 
    
    <?xml version="1.0" encoding="utf-8"?>
    <openbox_menu>
        <menu id="root-menu" label="OpenBox 3" execute="/usr/bin/obmenu-generator">
        </menu>
    </openbox_menu>
    
To automatically iconify entries, the `-i` option would be added: 
    
    <menu id="root-menu" label="OpenBox 3" execute="/usr/bin/obmenu-generator -i">
    
#### openbox-menu

**提示：** If this menu produces an error, it may be solved by enabling icons in `~/.config/openbox/rc.xml`.

[openbox-menu](<https://aur.archlinux.org/packages/openbox-menu/>)AUR uses the [LXDE](<../zh-cn/LXDE.html> "LXDE") [menu-cache](<https://sourceforge.net/projects/lxde/files/menu-cache/>) to create dynamic menus. The [official homepage](<http://fabrice.thiroux.free.fr/openbox-menu_en.html>) provides further information and screenshots. 

###  菜单图标

To show icons next to menu entries, it will be necessary to ensure they are enabled in the `<menu>` section of the `~/.config/openbox/rc.xml` file: 
    
    <showIcons>yes</showIcons>
    
Where using a static menu, it will then be necessary to edit the `~/.config/openbox/menu.xml` file to provide both the `icon =` command, along with the full path and icon name for each entry. An example of the syntax used to provide an icon for a category is: 
    
    <menu id="apps-menu" label="[label name]" icon="[pathway to icon]/[icon name]">
    
###  将桌面菜单作为面板菜单

**提示：** XDoTool can simulate any keybind for any action, and as such, it may therefore be used for many other purposes...

[xdotool](</wzh/index.php?title=Xdotool&action=edit&redlink=1> "Xdotool（页面不存在）") is a package that can issue commands to simulate key presses / keybinds, meaning that it is possible to use it to invoke keybind-related actions without having to actually press their assigned keys. As this includes the ability to invoke an assigned keybind for the Openbox desktop menu, it is therefore possible to use XDoTool to turn the Openbox desktop menu into a panel menu. Especially where the desktop menu is heavily customised and feature-rich, this may prove very useful to: 

  * Replace an existing panel menu
  * Implement a panel menu where otherwise not provided or possible (e.g. for [Tint2](<../zh-cn/Tint2.html> "Tint2"))
  * Compensate where losing access to the desktop menu due to the use of an application like [xfdesktop](<https://archlinux.org/packages/?name=xfdesktop>)包 to manage the [desktop](<#%E6%A1%8C%E9%9D%A2%E5%9B%BE%E6%A0%87%E4%B8%8E%E5%A3%81%E7%BA%B8>).

Once XDoTool has been installed - if not already present - it will be necessary to create a keybind to access the root menu in `~/.config/openbox/rc.xml`, and again below the `<!-- Keybindings for running aplications -->` heading. For example, the following code will bring up the menu by pressing `CTRL` \+ `m`: 
    
    <keybind key="C-m">
        <action name="ShowMenu">
           <menu>root-menu</menu>
        </action>
    </keybind>
    
Openbox must then be [reconfigured](<#%E9%87%8D%E6%96%B0%E9%85%8D%E7%BD%AEOpenbox>). In this instance, XDoTool will be used to simulate the `CTRL` \+ `m` keypress to access the desktop menu with the following command (note the use of `+` in place of `-`): 
    
    xdotool key control+m
    
How this command may be used as a panel launcher / icon is largely dependent on the features of panel used. While some panels will allow the above command to be executed directly in the process of creating a new launcher, others may require the use of an executable script. As an example, a custom executable script called `obpanelmenu.sh` will be created in the `~/.config` folder: 
    
    $ _text editor_ ~/.config/obpanelmenu.sh
    
Once the empty file has been opened, the appropriate XDoTool command must be added to the empty file (i.e. to simulate the `CTRL` \+ `m` keypress for this example): 
    
    xdotool key control+m
    
After the file has been saved and closed, it may then be made into an executable script with the following command: 
    
    $ chmod +x ~/.config/obpanelmenu.sh
    
Executing it will bring up the Openbox desktop menu. Consequently, where using a panel that supports drag-and-drop functionality to add new launchers, simply drag the executable script onto it before changing the icon to suit personal taste. 

###  XDG 兼容菜单

一个符合xdg标准的菜单是基于freedesktop.org标准的。菜单的定义位于/etc/xdg/menus目录中的菜单文件中。新的应用程序将自动出现在菜单中。 

####  范例

  * [californium](<https://github.com/mlde/californium>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-15 ⓘ]: 基于LXQt主菜单的xdg菜单，易于主题化。

##  提示与技巧

###  光标与图标主题

详情参阅[光标主题](<../zh-cn/Cursor_themes.html> "Cursor themes")和[图标](</wzh/index.php?title=Icons&action=edit&redlink=1> "Icons（页面不存在）")。 

###  桌面图标与壁纸

Openbox本身不支持使用桌面图标或壁纸。 

请参阅 [PCManFM](<../zh-cn/PCManFM.html#Desktop_management> "PCManFM"), [SpaceFM](<../zh-cn/SpaceFM.html#Desktop_management> "SpaceFM") 和 [Idesk](<../zh-cn/Idesk.html> "Idesk"). 

**注意：** 您可能需要编辑 `~/.conkyrc` 并将 `own_window_type` 设置成 `normal`.

请参阅 [List of applications#Wallpaper setters](<../zh-cn/List_of_applications.html#Wallpaper_setters> "List of applications"). 

###  混成特效

Openbox对[混成](<https://en.wikipedia.org/wiki/Compositing_window_manager> "wikipedia:Compositing window manager")不提供原生支持，因此需要外部混成器。 

虽然合成不是必需的组件， 但它可以特别避免 [oblogout](<#oblogout>) 导致的屏幕失真问题，以及终端窗口透明度引起的视觉故障等问题。请参见 [Xorg#Composite](<../zh-cn/Xorg.html#Composite> "Xorg") 获取常见的选择。 

### oblogout

请参阅 [Oblogout](</wzh/index.php?title=Oblogout&action=edit&redlink=1> "Oblogout（页面不存在）") 文章，了解如何使用这个实用的图形化注销脚本的概述。 

###  Openbox多显示器用户

While Openbox provides better than average multihead support on its own, [openbox-multihead-git](<https://aur.archlinux.org/packages/openbox-multihead-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] provides a development branch called **Openbox Multihead** that gives multihead users per-monitor desktops. This model is not commonly found in floating window managers, but exists mainly in [tiling window managers](<../zh-cn/Window_manager.html#Types> "Window manager"). It is explained well on the [Xmonad web site](<https://xmonad.org/tour.html#workspace>). Also, please see [README.MULTIHEAD](<https://github.com/BurntSushi/openbox-multihead/blob/multihead/README.MULTIHEAD>) for a more comprehensive description of the new features and configuration options found in Openbox Multihead. 

Openbox Multihead会在只有一个屏幕时像普通的Openbox一样工作。 

###  热键执行复合命令

如果您需要执行复杂的命令，请使用Shell功能。 

特殊字符的替换如下： 

  * `&`: &amp;
  * `<`: &lt;
  * `>`: &gt;

这个示例将立即关闭显示器并使用[slock](<https://archlinux.org/packages/?name=slock>)包 锁定屏幕。它是从[这个帖子](<https://bbs.archlinux.org/viewtopic.php?pid=903057>)中获取的. 
    
     <keybind key="W-l">
       <action name="Execute">
         <command>sh -c 'slock &amp; (sleep .5 &amp;&amp; xset dpms force off)'</command>
       </action>
     </keybind>
    
有时候需要为应用程序指定环境变量： 
    
     <keybind key="A-F7">
       <action name="Execute">
         <command>sh -c "LC_ALL=C obconf"</command>
       </action>
     </keybind>
    
另一个示例将启动应用程序，并将所有stdout和stderr输出保存到文件中： 
    
     <keybind key="A-f">
       <action name="Execute">
         <command>sh -c sh -c "exec gimp &gt;/tmp/gimp.out 2&gt;&amp;1"</command>
       </action>
     </keybind>
    
启用屏幕截图功能： 
    
     <keybind key="Print">
       <action name="Execute">
         <command>gnome-screenshot -c</command>
       </action>
     </keybind>
     <keybind key="A-Print">
       <action name="Execute">
         <command>gnome-screenshot -c -w</command>
       </action>
     </keybind>
     <keybind key="W-Print">
       <action name="Execute">
         <command>gnome-screenshot -i</command>
       </action>
     </keybind>
    
###  应用程序启动器

Given the lack of a desktop environment with a plain Openbox install, it can be useful to install one or more application launchers as supplements to the Openbox menu system and the hotkeys. Lists of such launchers can be found at [Category:Application launchers](<../zh-cn/Category:Application_launchers.html> "Category:Application launchers") and [List of applications/Other#Application launchers](<../zh-cn/List_of_applications/Other.html#Application_launchers> "List of applications/Other"); popular examples are [Gmrun](<../zh-cn/Gmrun.html> "Gmrun") and [dmenu](<../zh-cn/Dmenu.html> "Dmenu"). 

###  鼠标切换桌面

It is possible to switch desktop by moving the mouse cursor to the edges of the screen. First install [xdotool](<https://archlinux.org/packages/?name=xdotool>)包 and add the following two lines to your `~/.xinitrc`: 
    
    xdotool behave_screen_edge --delay 500 left set_desktop --relative -- -1 &
    xdotool behave_screen_edge --delay 500 right set_desktop --relative -- +1 &
    
###  设置默认应用及文件关联

请参见[默认应用程序](<../zh-cn/Default_applications.html> "Default applications")文章. 

###  Ad-hoc窗口透明

**警告：** 这可能在行动组中定义了其他动作时无法工作。

The program [transset-df](<https://aur.archlinux.org/packages/transset-df/>)AUR can enable window transparency on-the-fly. 

For example, using the following code in the `<mouse>` section of the `~/.config/openbox/rc.xml` file will enable control of application window transparency by hovering the mouse-pointer over the title bar and scrolling with the middle button: 
    
    <context name="Titlebar">
        ...
        <mousebind button="Up" action="Click">
            <action name= "Execute" >
            <execute>transset-df -p .2 --inc  </execute>
            </action>
        </mousebind>
        <mousebind button="Down" action="Click">
            <action name= "Execute" >
            <execute>transset-df -p .2 --dec </execute>
            </action>
        </mousebind>
        ...
    </context>
    
###  使用 obxprop 进行更快的配置

The [openbox](<https://archlinux.org/packages/?name=openbox>)包 package provides a `obxprop` binary that can parse relevant values for applications settings in `rc.xml`. Officially `obxprop | grep "^_OB_APP"` is recommended for this task. Start the process by running the command shown, then click a window to see its properties in the terminal. 

###  应用程序的 Xprop 值

[xorg-xprop](<https://archlinux.org/packages/?name=xorg-xprop>)包 can be used to relay property values for selected applications. Where frequently using per-application settings, the following [Bash Alias](<../zh-cn/Bash.html#Aliases> "Bash") may be useful: 
    
    alias xp='xprop | grep "WM_WINDOW_ROLE\|WM_CLASS" && echo "WM_CLASS(STRING) = \"NAME\", \"CLASS\""'
    
To use Xorg-XProp, run using the alias given `xp`, and click on the active program desired to define with per-application settings. The results displayed will only be the information that Openbox itself requires, namely the `WM_WINDOW_ROLE` and `WM_CLASS` (name and class) values: 
    
    WM_WINDOW_ROLE(STRING) = "roster"
    WM_CLASS(STRING) = "gajim.py", "Gajim.py"
    WM_CLASS(STRING) = "NAME", "CLASS"
    
###  切换键盘布局

请参考文章[在键盘布局之间切换的方法](</wzh/index.php?title=Keyboard_configuration_in_Xorg&action=edit&redlink=1> "Keyboard configuration in Xorg（页面不存在）")中的说明。 

###  设置虚拟桌面网格

安装 [obsetlayout](<https://aur.archlinux.org/packages/obsetlayout/>)AUR。例如，要设置一个 2x2 的网格： 
    
    obsetlayout 0 2 2 0
    
在不带参数的情况下运行它，以了解参数的含义。 

###  启用敏感边角

[lead-git](<https://aur.archlinux.org/packages/lead-git/>)AUR 为openbox和其他轻量级窗口管理器提供了热角功能。在自动启动文件中添加一个条目以启动该应用程序： 
    
    lead &
    
命令可以在配置文件中进行编辑`~/.config/mlde/lead.conf`: 
    
    [eDP1]
    bottom=
    bottomLeft=chromium
    bottomRight=thunar
    left=
    right=
    top=
    topLeft=mlde.californium toggle
    topRight=skippy-xd
    
###  窗口吸附

Many desktop environments and window managers support _window snapping_ (e.g. Windows 7 Aero snap), whereby they will automatically snap into place when moved to the edge of the screen. This effect can also be simulated in Openbox through the use of [keybinds](<#%E9%94%AE%E7%BB%91%E5%AE%9A>) on focused windows. 

As illustrated in the example below, percentages must be used to determine window sizes (see [openbox.org](<http://openbox.org/wiki/Help:Actions>) for further information). In this instance, The `super` key is used in conjunction with the `navigation` keys: 
    
    <keybind key="W-Left">
        <action name="UnmaximizeFull"/>
        <action name="MaximizeVert"/>
        <action name="MoveResizeTo">
            <width>50%</width>
        </action>
        <action name="MoveToEdge"><direction>west</direction></action>
    </keybind>
    <keybind key="W-Right">
        <action name="UnmaximizeFull"/>
        <action name="MaximizeVert"/>
        <action name="MoveResizeTo">
            <width>50%</width>
        </action>
        <action name="MoveToEdge"><direction>east</direction></action>
    </keybind>
    
However, it should be noted that once a window has been 'snapped' to an edge, it will remain vertically maximised unless subsequently maximised and then restored. The solution is to implement additional keybinds - in this instance using the `down` and `up` keys - to do so. This will also make pulling 'snapped' windows from screen edges faster as well: 
    
    <keybind key="W-Down">
       <action name="Unmaximize"/>
    </keybind>
    <keybind key="W-Up">
       <action name="Maximize"/>
    </keybind>
    
This [Ubuntu forum thread](<https://ubuntuforums.org/showthread.php?t=1796793>) provides more information. Applications such as [opensnap](<https://aur.archlinux.org/packages/opensnap/>)AUR are also available to automatically simulate window snapping behaviour without the use of keybinds. Another option is to use [bunsen-utilities-git](<https://aur.archlinux.org/packages/bunsen-utilities-git/>)AUR which provides `bl-aerosnap --left` and `bl-aerosnap --right` commands which will snap active window on left or right edge respectively if it's not snapped and restore it to original size and position otherwise. Just bind these commands to the key combination of your choosing. 

###  平滑的显示管理器过渡

**注意：** 这已经确定可以在 [LightDM](<../zh-cn/LightDM.html> "LightDM") 上工作。

Users of display managers might experience a flickering during the transition between the display manager and the Openbox desktop. The flickering comes from Openbox setting the root window's color during startup. Therefore there is a brief moment when the display flashes in a grey color, between the display manager's background and the desktop's wallpaper. 

Setting the root window's background color can be disabled by editing the Openbox startup script found in `/usr/lib/openbox/openbox-autostart`. Simply comment out (or delete) the block starting with `# Set a background color`. 

**注意：** Users who do not specifically set their wallpaper will "inherit" the display manager's background automatically if they disable the root window color adjustment.

###  窗口渲染

To remove window decorations for all or particular applications, use the _< decor>_ option in the _< applications>_ section of _rc.xml_ (user: _~/.config/openbox/_ or system: _/etc/xdg/openbox/_).  
Example for Firefox, including variants like Firefox-Beta and Firefox-Nightly: 
    
     <application class="Firefox*">
       <decor>no</decor>
     </application>
    
One could also disable decorations for all applications (using class **"*"**), then enable them (using **yes**) for individual ones. To apply the changes, restart your desktop session, and thus Openbox. Reference: [Openbox FAQ](<http://openbox.org/wiki/Help:FAQ#How_do_I_remove_the_decorations_from_all_my_windows.3F>)

##  排错

### Firefox

基于Mozilla的浏览器可能会忽略应用程序规则 (例如 `<desktop>`) 除非使用 `class="Firefox"` 。请参阅 [#应用程序的 Xprop 值](<#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84_Xprop_%E5%80%BC>). 

###  主题丢失

If for any reason the newly extracted theme cannot be selected, open the theme directory to first ensure that it is compatible with Openbox - there should be an `openbox-3` directory and a `themerc` file within it. An `.obt` (**O** pen**B** ox **T** heme) file may also be present in some instances, which can then be manually loaded in [obconf](<https://archlinux.org/packages/?name=obconf>)包. 

A theme may also be not accessible due to wrong permissions. See [File permissions and attributes](<../zh-cn/File_permissions_and_attributes.html> "File permissions and attributes") for more. 

###  连续切换桌面时停顿

By default Openbox switches from the last desktop back to the first desktop on mouse wheel scroll. Use `<wrap>no</wrap>` in the `mousebind` section to disable this behaviour. 
    
       <context name="Desktop">
         <mousebind button="Up" action="Click">
           <action name="GoToDesktop">
             <to>previous</to>
             <wrap>no</wrap>
           </action>
         </mousebind>
         <mousebind button="Down" action="Click">
           <action name="GoToDesktop">
             <to>next</to>
             <wrap>no</wrap>
           </action>
         </mousebind>
       </context>
    
###  新窗口隐藏在活动窗口后面

Some application windows (such as Firefox windows) may load behind the currently active window, causing you to need to switch to the window you just created to focus it. To fix this behavior add this to your `~/.config/openbox/rc.xml` file, inbetween the `<openbox_config>` and `</openbox_config>` tags: 
    
    <applications>
      <application class="*">
        <focus>yes</focus>
      </application>
    </applications>

##  参阅 

  * [Openbox Website](<http://openbox.org/>) \- 官方网站
  * [Box-Look.org](<https://www.box-look.org/>) \- 一个关于主题和相关艺术作品的资源网站
  * [Openbox Hacks and Configs Thread](<https://bbs.archlinux.org/viewtopic.php?id=93126>) @ Arch Linux 论坛
  * [Openbox Screenshots Thread](<https://bbs.archlinux.org/viewtopic.php?id=45692>) @ Arch Linux 论坛
  * [An Openbox guide](<https://urukrama.wordpress.com/openbox-guide/>)
