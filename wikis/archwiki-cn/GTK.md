**翻译状态：**

  * 本文（或部分内容）译自 [GTK](<https://wiki.archlinux.org/title/GTK> "arch:GTK")，最近一次同步于 2022-04-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/GTK?diff=0&oldid=726334>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GTK_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [统一 Qt 和 GTK 应用程序的外观](<../zh-cn/%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html> "统一 Qt 和 GTK 应用程序的外观")
  * [Qt](<../zh-cn/Qt.html> "Qt")
  * [GNU](<../zh-cn/GNU.html> "GNU")
  * [GTK/开发](</wzh/index.php?title=GTK/%E5%BC%80%E5%8F%91&action=edit&redlink=1> "GTK/开发（页面不存在）")

摘自 [GTK 官方网站](<https://www.gtk.org>)： 

    GTK，或称 GIMP Toolkit，是一个跨平台的图形界面开发库。该库提供一套完整的窗口部件，从一次性工具到大型应用都可使用。

GTK，即 GIMP Toolkit，最初由 [GNU 项目](<../zh-cn/GNU.html> "GNU")为 [GIMP](<../zh-cn/GIMP.html> "GIMP") 开发，但现在它已经是一个非常流行的工具包，绑定了很多语言。本文将探讨 GTK 主题、风格、图标、字体和字号的配置工具，也会详细介绍手动配置。 

##  安装

目前在[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")中有三个版本的 GTK。它们可以通过以下软件包来[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")： 

  * **GTK 4.x** 可以通过 [gtk4](<https://archlinux.org/packages/?name=gtk4>)包 包获得。
  * **GTK 3.x** 可以通过 [gtk3](<https://archlinux.org/packages/?name=gtk3>)包 包获得。
  * **GTK 2.x** 可以通过 [gtk2](<https://archlinux.org/packages/?name=gtk2>)包 包获得。

**GTK 1.x** 可以通过 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 上的 [gtk](<https://aur.archlinux.org/packages/gtk/>)AUR 包获得。 

##  主题

###  GTK 3 和 GTK 4

GTK 3 和 GTK 4 的默认主题是 Adwaita，但也包含了 HighContrast 和 HighContrastInverse 主题。 

要设置特定主题，请通过 [dconf](<../zh-cn/GNOME.html#%E9%85%8D%E7%BD%AE>) 编辑器设置 `org.gnome.desktop.interface` 命名空间下的 `gtk-theme` 属性: 
    
    $ gsettings set org.gnome.desktop.interface gtk-theme Adwaita
    
**注意：** 对基于 libadwaita 的 GTK 4 应用程序，需要选择具有 [特殊支持](<https://github.com/jnsh/arc-theme/issues/61#issuecomment-922380704>) 的主题，且需要设置 `GTK_THEME` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") 以强行应用，或者使用打过补丁的libadwaita版本：[libadwaita-without-adwaita-git](<https://aur.archlinux.org/packages/libadwaita-without-adwaita-git/>)AUR。

若不使用 dconf 属性，则可以使用 `GTK_THEME` 设置 GTK 3 和 GTK 4 主题。例如将 GNOME 计算器的主题设为 Adwaita 的暗色变体： 
    
    $ GTK_THEME=Adwaita:dark gnome-calculator
    
**提示：** 要将上述更改应用于桌面快捷方式（或启动器），请参阅 [桌面项#编辑环境变量](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E7%BC%96%E8%BE%91%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "桌面项")。

**注意：** 如果不使用对应的 [XDG_桌面门户](<../zh-cn/XDG_%E6%A1%8C%E9%9D%A2%E9%97%A8%E6%88%B7.html> "XDG 桌面门户") ，则可能需要设置 [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `ADW_DISABLE_PORTAL=1` 方可正确载入通过 GSettings 设置的主题。参见 <https://gitlab.gnome.org/GNOME/libadwaita/-/commit/e715fae6a509db006a805af816f9d163f81011ef>

### GTK 2

GTK 2 的默认主题是 Raleigh，但 Arch Linux 位于 `/usr/share/gtk-2.0/gtkrc` 的自定义配置文件将默认主题设为了 Adwaita。不过，这需要安装 [gnome-themes-extra-gtk2](<https://aur.archlinux.org/packages/gnome-themes-extra-gtk2/>)AUR 包才能正常工作，否则 GTK 2 应用程序将继续显示 Raleigh 主题。 

若要修改 GTK 2 的主题，可以通过配置环境变量 `GTK2_RC_FILES` 来实现。例如将 [GIMP](<../zh-cn/GIMP.html> "GIMP") 的主题设为 Raleigh： 
    
    $ GTK2_RC_FILES=/usr/share/themes/Raleigh/gtk-2.0/gtkrc gimp
    
**提示：**`gtkrc` 也可以是由 [#配置工具](<#%E9%85%8D%E7%BD%AE%E5%B7%A5%E5%85%B7>) 在家目录 (/home) 下创建的自定义文件。参见 [#示例](<#%E7%A4%BA%E4%BE%8B>)。

在官方软件仓库或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 可以安装更多主题。可以在 `~/.themes/` 或 `~/.local/share/themes/` 目录中手动提取主题。 

###  GTK 2 与 GTK 3 的主题支持：

  * **Adapta** — 基于 Material Design 准则的自适应 GTK 主题。包括: Adapta, Adapta-Eta, Adapta-Nokto, Adapta-Nokto-Eta

     <https://github.com/tista500/Adapta> || [adapta-gtk-theme](<https://archlinux.org/packages/?name=adapta-gtk-theme>)包

  * **Arc** — 具有现代外观和透明元素的平面主题。包括: Arc, Arc-Dark, Arc-Darker

     <https://github.com/jnsh/arc-theme> || 透明: [arc-gtk-theme](<https://aur.archlinux.org/packages/arc-gtk-theme/>)AUR, 不透明: [arc-solid-gtk-theme](<https://aur.archlinux.org/packages/arc-solid-gtk-theme/>)AUR

  * **Bluebird** — Xfce 的蓝色桌面套件。

     <https://github.com/shimmerproject/Bluebird> || [xfce-theme-bluebird](<https://aur.archlinux.org/packages/xfce-theme-bluebird/>)AUR

  * **Breeze** — KDE 默认小部件主题的 GTK 版本。包括: Breeze, Breeze-Dark

     <https://invent.kde.org/plasma/breeze-gtk> || [breeze-gtk](<https://archlinux.org/packages/?name=breeze-gtk>)包

  * **Deepin** — 深度桌面的默认主题。包括: deepin, deepin-dark

     <https://github.com/linuxdeepin/deepin-gtk-theme> || [deepin-gtk-theme](<https://archlinux.org/packages/?name=deepin-gtk-theme>)包

  * **GNOME Extra Themes** — GNOME 桌面的附加主题。包括: Adwaita, Adwaita-dark, HighContrast

     <https://gitlab.gnome.org/GNOME/gnome-themes-extra> || [gnome-themes-extra](<https://archlinux.org/packages/?name=gnome-themes-extra>)包

  * **Greybird** — 灰色和蓝色的 Xfce 主题，在 Xubuntu 12.04 中默认使用。

     <https://github.com/shimmerproject/Greybird> || [xfce-theme-greybird](<https://aur.archlinux.org/packages/xfce-theme-greybird/>)AUR

  * **Materia** — GTK3、GTK2 和 GNOME Shell 的类 Material Design 平面主题。

     <https://github.com/nana-4/materia-theme> || [materia-gtk-theme](<https://archlinux.org/packages/?name=materia-gtk-theme>)包

  * **MATE Themes** — MATE 桌面的默认主题。包括: BlackMATE, Blue-Submarine, BlueMenta, ContrastHighInverse, Green-Submarine, GreenLaguna, Menta, TraditionalGreen, TraditionalOk

     <https://github.com/mate-desktop/mate-themes> || [mate-themes](<https://archlinux.org/packages/?name=mate-themes>)包

  * **Numix** — 具有现代外观的简约轻盈的主题 (GNOME, Openbox, Unity, Xfce)。包括：Numix

     <https://github.com/numixproject/numix-gtk-theme> || [numix-gtk-theme-git](<https://aur.archlinux.org/packages/numix-gtk-theme-git/>)AUR

  * **Vertex** — GTK 3、GTK 2、Gnome-Shell 以及 Cinnamon 的主题。

     <https://github.com/horst3180/vertex-theme> || [vertex-themes](<https://aur.archlinux.org/packages/vertex-themes/>)AUR

  * **Zuki** — GTK、gnome-shell 等的主题。

     <https://github.com/lassekongo83/zuki-themes> || [zuki-themes](<https://aur.archlinux.org/packages/zuki-themes/>)AUR

AUR 中还有很多 GTK 主题，例如：[搜索 gtk-theme](<https://aur.archlinux.org/packages?K=gtk-theme>)。 

###  GTK 与 QT

同时在系统上安装 GTK 和 QT（通常是 [KDE](<../zh-cn/KDE.html> "KDE") 组件）程序的人都知道，两者的外观并不怎么协调。关于两者外观统一的问题，参见：[统一 Qt 和 GTK 应用程序的外观](<../zh-cn/%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html> "统一 Qt 和 GTK 应用程序的外观")。 

##  配置工具

大部分主流[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")都提供配置 GTK 主题、图标、字体和字体尺寸的工具，并使用 [XSettings](<https://specifications.freedesktop.org/xsettings-spec/>) 管理这些设置： 

  * 如果使用 [Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon")，使用主题工具 (_cinnamon-settings themes_): 前往 _系统设置 > 主题_.
  * 如果使用 [Enlightenment](<../zh-cn/Enlightenment.html> "Enlightenment")：前往 _设置 > 全部 > 外观 > 应用程序主题_.
  * 如果使用 [GNOME](<../zh-cn/GNOME.html> "GNOME")，使用 GNOME Tweaks (_gnome-tweaks_): 安装 [gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包.
  * 如果使用 [MATE](<../zh-cn/MATE.html> "MATE")，使用“外观首选项”工具 (_mate-appearance-properties_): 前往 _系统 > 设置 > 外观_.
  * 如果使用 [Xfce](<../zh-cn/Xfce.html> "Xfce")，使用“外观”工具: 前往 _设置 > 外观_.

其他 GUI 工具通常会覆写[配置文件](<#%E9%85%8D%E7%BD%AE>)。 

**同时支持 GTK 2 与 GTK 3 的：**

  * **KDE GTK Configurator** — 允许您更改 GTK 2 和 GTK 3 应用程序样式和字体的应用程序。

     <https://invent.kde.org/plasma/kde-gtk-config> || [kde-gtk-config](<https://archlinux.org/packages/?name=kde-gtk-config>)包
    安装完成后, 在 _系统设置 > 外观 > Application Style > Configure GNOME/GTK Application Style_ 中能找到 `kde-gtk-config`。

  * **LXAppearance** — LXDE 项目中独立于桌面的 GTK 2 和 GTK 3 风格配置工具（不需要 LXDE 桌面的其他部分）。

     <https://wiki.lxde.org/en/LXAppearance>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-18 ⓘ] || [lxappearance-gtk3](<https://archlinux.org/packages/?name=lxappearance-gtk3>)包

  * **Oo-mox** — 一款图形应用程序，用于生成 Numix 和 Flat Plat 主题（GTK 2 和 3）、Archdroid 和 Gnome 颜色图标主题的不同颜色变体，也能为 HiDPI 显示生成预缩放的 GTK 2 主题。

     <https://github.com/actionless/oomox> || [themix-full-git](<https://aur.archlinux.org/packages/themix-full-git/>)AUR

**只支持 GTK 2 的：**

  * **GTK Change Theme** — 能改变 GTK 2.0 主题的小程序（被认为是 _switch2_ 之外的更好选择）。

     <http://plasmasturm.org/code/gtk-chtheme/> || [gtk-chtheme](<https://archlinux.org/packages/?name=gtk-chtheme>)包

  * **GTK Preference Tool** — GTK 主题选择器和字体切换器。

     <https://gtk-win.sourceforge.io/home/index.php/Main/GTKPreferenceTool> || [gtk2_prefs](<https://aur.archlinux.org/packages/gtk2_prefs/>)AUR

  * **GTK Theme Switch** — 简易 GTK 主题切换器。

     <http://muhri.net/nav.php3?node=gts> || [gtk-theme-switch2](<https://aur.archlinux.org/packages/gtk-theme-switch2/>)AUR

##  配置

GTK 设置可以在配置文件中手动指定，但桌面环境和应用程序可以覆盖这些设置。根据 GTK 版本，这些文件位于： 

  * GTK 2 用户特定设置: `~/.gtkrc-2.0`
  * GTK 2 系统全局设置: `/etc/gtk-2.0/gtkrc`
  * GTK 3 用户特定设置: `$XDG_CONFIG_HOME/gtk-3.0/settings.ini` (如果 `$XDG_CONFIG_HOME` 未设置，则为 `$HOME/.config/gtk-3.0/settings.ini`)
  * GTK 3 系统全局设置: `/etc/gtk-3.0/settings.ini`

**注意：**

  * 有关当前支持的 GTK 配置选项的完整列表，请参阅 GTK 编程参考手册中的 [GTK4](<https://docs.gtk.org/gtk4/class.Settings.html#properties>) 和 [GTK3](<https://docs.gtk.org/gtk3/class.Settings.html#properties>) _GtkSettings_ 属性（以及 [GTK 2 属性](<https://ghostarchive.org/archive/p2BmM>)）。

  * 自 GTK 3.10 以来，以下描述的一些设置 (例如 `gtk-icon-sizes`) 已弃用并被忽略。
  * 如果编辑 GTK 配置文件，只有新启动的应用程序才会显示更改。

###  基本主题配置

要手动改变 GTK 主题、图标、字体和字体大小，请在配置文件中添加以下内容： 

  * GTK 2:

    ~/.gtkrc-2.0
    
    gtk-icon-theme-name = "Adwaita"
    gtk-theme-name = "Adwaita"
    gtk-font-name = "DejaVu Sans 11"

  * GTK 3:

    $XDG_CONFIG_HOME/gtk-3.0/settings.ini
    
    [Settings]
    gtk-icon-theme-name = Adwaita
    gtk-theme-name = Adwaita
    gtk-font-name = DejaVu Sans 11

如果主题没有应用于 GTK 3，请使用 `gsettings`: 
    
    $ gsettings set org.gnome.desktop.interface gtk-theme Pop
    
**注意：** 图标主题名称是其目录的名称，而不是其 index.theme 中的 name 属性。

###  深色版主题

有些 GTK 3 的主题包含深色版本, 但只有应用程序明确要求时才会使用. 要在所有 GTK 3 程序中应用深色模式, 请使用以下配置: 
    
    gtk-application-prefer-dark-theme = true
    
对于 GTK 4，请使用以下命令： 
    
    $ gsettings set org.gnome.desktop.interface color-scheme prefer-dark
    
###  键盘快捷键

把鼠标放在某个菜单项，然后按下某个按键组合，即可修改该项目的快捷键。不过，该功能默认是关闭的。启用方法是使用以下配置： 
    
    gtk-can-change-accels = 1
    
####  Emacs 按键绑定

要在 GTK 应用程序中拥有类似 Emacs 的键绑定，请添加以下内容： 
    
    ~/.gtkrc-2.0
    
    gtk-key-theme-name = "Emacs"
    
    ~/.config/gtk-3.0/settings.ini
    
    [Settings]
    gtk-key-theme-name = Emacs

对于 GTK3 还需要运行： 
    
    $ gsettings set org.gnome.desktop.interface gtk-key-theme "Emacs"
    
Xfce 也需要类似的设置： 
    
    $ xfconf-query -c xsettings -p /Gtk/KeyThemeName -s Emacs
    
`/usr/share/themes/Emacs/` 中的配置文件决定了 Emacs 的键位绑定，并且可以更改。您也可以把其中的内容复制到用户目录下的 `~/.gtkrc-2.0` 文件中来为个别用户进行自定义。 

###  GNOME 菜单延迟

鼠标指向菜单与菜单显示之间有一定延迟，通过以下设置调整延迟时间（以毫秒为单位）： 
    
    gtk-menu-popup-delay = 0
    
###  缩小窗口部件

如果屏幕很小，不喜欢过大的图标和窗口部件，可以调整其尺寸。 

若要让工具栏仅显示图标而不显示文字（[valid values](<https://developer.gnome.org/gtk3/stable/gtk3-Standard-Enumerations.html#GtkToolbarStyle>)）： 
    
    gtk-toolbar-style = GTK_TOOLBAR_ICONS
    
若要显示小图标： 
    
    gtk-icon-sizes = "panel-menu=16,16:panel=16,16:gtk-menu=16,16:gtk-large-toolbar=16,16\
    :gtk-small-toolbar=16,16:gtk-button=16,16"
    
若要移除按钮上的图标： 
    
    gtk-button-images = 0
    
若要移除菜单上的图标： 
    
    gtk-menu-images = 0
    
另见 [[1]](<https://martin.ankerl.com/2008/10/11/how-to-make-a-compact-gnome-theme/>) 和 [[2]](<https://www.gnome-look.org/p/1079374>). 

###  隐藏 CSD 按钮

若要删除 _gtk3_ 窗口的客户端装饰 (CSD)[[3]](<https://blogs.gnome.org/tbernard/2018/01/26/csd-initiative/>) 最小化和最大化按钮： 
    
    gtk-decoration-layout=menu:close
    
参见 [GTK 文档](<https://docs.gtk.org/gtk3/property.Settings.gtk-decoration-layout.html>)。 

###  禁用鼠标中键粘贴

若要关闭鼠标中键（主键）粘贴： 
    
    gtk-enable-primary-paste=false
    
###  文件选择器启动时的初始位置

在**当前工作目录** 而不是**最近** 位置内打开文件选择器。通常来说，**当前工作目录** 是 _家 (home)_ 目录。 

**GTK 3**

通过如下命令，更改[设置](<../zh-cn/GNOME.html#%E9%85%8D%E7%BD%AE> "GNOME")： 
    
    $ gsettings set org.gtk.Settings.FileChooser startup-mode cwd
    
**GTK 2**

将下面内容加入 `~/.config/gtk-2.0/gtkfilechooser.ini`： 
    
    StartupMode=cwd
    
###  传统滚动操作

**注意：** 并非所有的 GTK 应用程序都遵从这个设置。

**提示：** 只需要用右键代替左键，就能可靠地实现传统的滚动操作。

在 GTK 3.6 之前，点击滚动条中滑块的任何一边都会使滚动条向点击的方向滚动大约一页。从 GTK 3.6 开始，滑块会直接移动到点击的位置。通过创建包含以下内容的文件，可以在一些应用程序中恢复这种操作： 
    
    ~/.config/gtk-3.0/settings.ini
    
    [Settings]
    gtk-primary-button-warps-slider = false
    
### Disable overlay scrollbars

Since GTK 3.15, overlay scrollbars are enabled by default, meaning that scrollbars will be shown only on mouseover in GTK 3 applications. This behavior can be reverted by setting the following environment variable: `GTK_OVERLAY_SCROLLING=0`. See [Environment variables#Graphical environment](<../zh-cn/Environment_variables.html#Graphical_environment> "Environment variables"). 

Alternatively, overlay scrollbars can be disabled in the GTK 3 settings since GTK 3.24.9. To do so, the value of gtk-overlay-scrolling has to be set to false in the [Settings] section of the settings file: 
    
    ~/.config/gtk-3.0/settings.ini
    
    [Settings]
    gtk-overlay-scrolling = false

GTK 4 will no longer support `GTK_OVERLAY_SCROLLING`. It has already been [dropped](<https://github.com/GNOME/gtk/commit/e49615184a9d85bb0bb4e289b3ee8252adee3813#diff-3cf94c6e1eb009e20985034bc2210bfd>) from master. As of GTK 4, the overlay nature of the scrollbars is part of the toolkit. The blanket toggle has been removed to prevent developers from breaking applications that have not been tested with both combinations. To allow application developers to decide what their applications should look like, the toolkit instead provides a mechanism to opt-out or add a setting for users. The function [gtk_scrolled_window_set_overlay_scrolling()](<https://developer.gnome.org/gtk3/stable/GtkScrolledWindow.html#gtk-scrolled-window-set-overlay-scrolling>) can be used to enable/disable overlay scrolling on a _per-application_ basis. Application developers can optionally use [GSettings](<https://blog.gtk.org/2017/05/01/first-steps-with-gsettings/>) to have a user setting bound to the property. 

#### Remove overlay scroll indicators

The positions of the overlay scrollbars are indicated by thin dashed lines in the application window. These dashed lines will be present even when overlay scrolling is disabled using the environment variable discussed in the section above. To remove the indicator lines, create the following file: 
    
    ~/.config/gtk-3.0/gtk.css
    
    /* Remove dotted lines from GTK 3 applications */
    undershoot.top, undershoot.right, undershoot.bottom, undershoot.left { background-image: none; }
    
###  示例

GTK example configurations: 

**注意：** May be ignored by some [desktop environments](</wzh/index.php?title=Desktop_environments&action=edit&redlink=1> "Desktop environments（页面不存在）") (e.g. [GNOME](<../zh-cn/GNOME.html> "GNOME")).
    
    ~/.gtkrc-2.0
    
    gtk-theme-name="Arc-Dark"
    gtk-icon-theme-name="breeze-dark"
    gtk-font-name="Sans 11"
    gtk-cursor-theme-name="Breeze_Amber"
    gtk-cursor-theme-size=0
    gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
    gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
    gtk-button-images=0
    gtk-menu-images=0
    gtk-enable-event-sounds=0
    gtk-enable-input-feedback-sounds=0
    gtk-xft-antialias=1
    gtk-xft-hinting=1
    gtk-xft-hintstyle="hintslight"
    gtk-xft-rgba="rgb"
    
    ~/.config/gtk-3.0/settings.ini
    
    [Settings]
    gtk-theme-name=Arc-Dark
    gtk-icon-theme-name=breeze-dark
    gtk-font-name=Sans 11
    gtk-cursor-theme-name=Breeze_Amber
    gtk-cursor-theme-size=0
    gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
    gtk-toolbar-icon-size=GTK_ICON_SIZE_SMALL_TOOLBAR
    gtk-button-images=0
    gtk-menu-images=0
    gtk-enable-event-sounds=0
    gtk-enable-input-feedback-sounds=0
    gtk-xft-antialias=1
    gtk-xft-hinting=1
    gtk-xft-hintstyle=hintslight
    gtk-xft-rgba=rgb
    # gtk-decoration-layout=menu:close
    # gtk-application-prefer-dark-theme=1

##  GDK 后端

GDK（GTK 的底层抽象层）支持多个后端显示 GTK 应用。 

###  Wayland 后端

GDK [Wayland](<../zh-cn/Wayland.html> "Wayland") 后端仅由 [gtk3](<https://archlinux.org/packages/?name=gtk3>)包 支持，并且是使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 显示服务器时的默认后端。 

使用 [gtk3](<https://archlinux.org/packages/?name=gtk3>)包 之前的 GTK 版本的应用程序不支持 Wayland，并且需要通过 Xwayland 才能使用 _X11_ 后端在 Wayland 会话上运行。 

使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 后端时，一些变量不会从 `settings.ini` 读取。 Any key that is present in the GSettings schema `org.gnome.desktop.interface` are read from there instead of `settings.ini`. 

An example of such variables are `gtk-color-scheme` and `icon-theme`, which must have their keys set with GSettings in order to theme GTK Applications under [Wayland](<../zh-cn/Wayland.html> "Wayland"). 或者，如果只需要自定义主题，可以设置环境变量 `GTK_THEME`。 

###  Xorg 后端

如果正在使用 [Xorg](<../zh-cn/Xorg.html> "Xorg") 显示服务器，则后端自动默认为 _x11_ 。 

通过设置环境变量 `GDK_BACKEND=x11`，可以强制 Wayland 会话的 GTK3 应用程序通过 Xwayland 使用 _X11_ 后端。 

###  Broadway 后端

The GDK Broadway backend provides support for displaying GTK applications in a web browser, using HTML5 and web sockets. [[4]](<https://developer.gnome.org/gtk3/3.8/gtk-broadway.html>)

When using _broadwayd_ , specify the display number to use, prefixed with a colon, similar to X. The default display number is 0 (zero). 
    
    $ display_number=:5
    
Start it. 
    
    $ broadwayd $display_number 
    
Port used by default 
    
    port = 8080 + $display_number
    
Point your browser to <http://127.0.0.1:port>

To Start applications 
    
    $ GDK_BACKEND=broadway BROADWAY_DISPLAY=$display_number _< <application>>_
    
Alternatively can set address and port 
    
    $ broadwayd --port $port_number --address $address $display_number
    
##  疑难解答

### Different themes between GTK 2 and GTK 3 applications

In general, if a selected theme has support for both GTK 2 and GTK 3, the theme will be applied to all GTK 2 and GTK 3 applications. If a selected theme has support for only GTK 2, it will be used for GTK 2 applications and the default GTK theme will be used for GTK 3 applications. If the selected theme has support for only GTK 3, it will be used for GTK 3 applications and the default GTK theme will be used for GTK 2 applications. Thus for application theme consistency, it is best to use a theme which has support for both GTK 2 and GTK 3. 

You could find what themes installed on your system have both an GTK 2 and GTK 3 version by using this command (does not work with names containing spaces): 
    
    find $(find ~/.themes /usr/share/themes/ -wholename "*/gtk-3.0" | sed -e "s/^\(.*\)\/gtk-3.0$/\1/") -wholename "*/gtk-2.0" | sed -e "s/.*\/\(.*\)\/gtk-2.0/\1"/
    
### Theme not applied to root applications

As user theme files (`$XDG_CONFIG_HOME/gtk-3.0/settings.ini`, `~/.gtkrc-2.0`) are not read by other accounts, the selected theme will not apply to [X applications run as root](</wzh/index.php?title=Running_X_apps_as_root&action=edit&redlink=1> "Running X apps as root（页面不存在）"). Possible solutions include: 

  * Create symlinks, e.g

    # ln -s /home/[username]/.gtkrc-2.0 /etc/gtk-2.0/gtkrc
    # ln -s /home/[username]/.config/gtk-3.0/settings.ini /etc/gtk-3.0/settings.ini
    
  * Configure system-wide theme files: `/etc/gtk-3.0/settings.ini` (GTK 3) or `/etc/gtk-2.0/gtkrc` (GTK 2)
  * Adjust the theme as root

    # lxappearance
    
  * Use a settings daemon (this is what most desktop environments do). A desktop-agnostic variant using [XSettings](<https://specifications.freedesktop.org/xsettings-spec/>) is available in the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") under [xsettingsd-git](<https://aur.archlinux.org/packages/xsettingsd-git/>)AUR.

### Client-side decorations

GTK 3.12 introduced [client-side decorations](<https://blogs.gnome.org/mclasen/2013/12/05/client-side-decorations-in-themes/>), which move the title-bar away from the window manager. This may present issues such as [double title-bars](<https://redmine.audacious-media-player.org/boards/1/topics/1135>), no title-bar at all, [double shadows](<https://github.com/chjj/compton/issues/189>) with compositing enabled, or being unable to move a frozen application. 

To remove the shadow and gap around windows (for example in combination with a tiling window manager), create the following file: 
    
    ~/.config/gtk-3.0/gtk.css
    
    .window-frame, .window-frame:backdrop {
     box-shadow: 0 0 0 black;
     border-style: none;
     margin: 0;
     border-radius: 0;
    }
    
    .titlebar {
     border-radius: 0;
    }
    
    .window-frame.csd.popup {
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(0, 0, 0, 0.13);
    }
    
    .header-bar {
      background-image: none;
      background-color: #ededed;
      box-shadow: none;
    }
    /* You may want to use this if you don't like the double title.
    GtkLabel.title {
        opacity: 0;
    }*/
    
Note that if visual problems persist, you may want to use the GTK Inspector to find the offending elements as explained here [[5]](<https://github.com/numixproject/numix-gtk-theme/issues/206#issuecomment-817660426>). 

To adjust the buttons in the header bar, use the `gtk-decoration-layout` setting. [[6]](<https://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings--gtk-decoration-layout>) The below examples removes all buttons: 
    
    ~/.config/gtk-3.0/settings.ini
    
    gtk-decoration-layout=menu:

To remove client-side decorations altogether, it's possible to use a patched library like [gtk3-classic](<https://aur.archlinux.org/packages/gtk3-classic/>)AUR or [gtk3-nocsd-git](<https://aur.archlinux.org/packages/gtk3-nocsd-git/>)AUR. 

###  cedilla ç/Ç instead of ć/Ć

See [[7]](<https://bugs.launchpad.net/ubuntu/+source/ibus/+bug/518056>), and [[8]](<https://bugs.launchpad.net/ubuntu/+source/ibus/+bug/518056/comments/37>) for a workaround using Xcompose (US international layout). 

### Suppress warning about accessibility bus

If you do not use any [Gnome Accessibility](<https://wiki.gnome.org/Accessibility>) features, you may receive warnings like: 
    
    WARNING **: Couldn't connect to accessibility bus:
    
To suppress these warnings, execute programs with `NO_AT_BRIDGE=1` or set that as a global [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"). 

### Titlebar background color mismatch

If you are using a [window manager](<../zh-cn/Window_manager.html> "Window manager") which uses a window decoration theme that mimics the GTK theme background color, you may find that the titlebar color no longer completely matches the application color in some GTK 3 applications. As a workaround, create the following file: 
    
    ~/.config/gtk-3.0/gtk.css
    
    /* Always use background color */
    GtkWindow {
        background-color: @theme_bg_color;
    }
    
    /* Fix tooltip background override */
    .tooltip {
        background-color: rgba(0, 0, 0, 0.8);
    }
    
    .tooltip * {
        background-color: transparent;
    }
    
    /* Fix Nautilus desktop window background override */
    NautilusWindow {
         background-color: transparent; 
    }
    
### Wrong focus events with tiling window managers

**注意：** This disables smooth scrolling and touchscreen support for GTK3 applications. [[9]](<https://bugzilla.gnome.org/show_bug.cgi?id=677329#c14>)

[Define](</wzh/index.php?title=Define&action=edit&redlink=1> "Define（页面不存在）") `GDK_CORE_DEVICE_EVENTS=1` to use GTK2 style input, instead of xinput2. [[10]](<https://bugzilla.gnome.org/show_bug.cgi?id=677329#c10>)

### Thumbnail support for GTK file dialog

Install [gtk2-patched-filechooser-icon-view](<https://aur.archlinux.org/packages/gtk2-patched-filechooser-icon-view/>)AUR and [gtk3-patched-filechooser-icon-view](<https://aur.archlinux.org/packages/gtk3-patched-filechooser-icon-view/>)AUR to have the option to view files as thumbnails instead of list in the GTK file chooser. 

### Button and menu icons

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Explain what the issue is. GNOME ignores `settings.ini` if GDM is used.（在 [Talk:GTK](<../zh-cn/Talk:GTK.html>) 中讨论）

For some applications in GNOME's Wayland session. Your `~/.config/gtk-3.0/settings.ini` file is misconfigured. This can happen if you try other GTK based desktop environments. These are the offending values: 
    
    ~/.config/gtk-3.0/settings.ini
    
    [Settings]
    gtk-button-images=1
    gtk-menu-images=1

Simply set them to 0 or remove the whole file to use GNOME defaults. 

### GTK 3 without polkit

GTK3 depends on polkit through colord, which is required for printing. However printing works fine without polkit installed; at least with a monochrome printer and package versions gtk3-print-backends=3.22.19-2 and colord=1.4.1-1. 

### Some GTK 2 themes only change the UI color palette

Depending on the theme of choice's support for GTK 2, UI controls may still have the default Raleigh appearance, possibly with a different color palette. This is due to these themes requiring the GTK 2 Murrine engine, which is missing (GTK 2 programs should complain about it on their standard error output). Install the [gtk-engine-murrine](<https://archlinux.org/packages/?name=gtk-engine-murrine>)包 package. 

### Patching GTK file chooser to use regular type ahead

GTK file chooser uses the same type-ahead-find feature as [GNOME/Files](<../zh-cn/GNOME/%E6%96%87%E4%BB%B6.html> "GNOME/Files"). This can be very jarring and does not fit in very well with other desktop enviroments. 

Some applications support XDG-desktop-portal which allows application to use the native file chooser. If that does not work you can restore type-ahead functionality by using a patched GTK, for example [gtk3-classic](<https://aur.archlinux.org/packages/gtk3-classic/>)AUR. 

### Text in GTK 4 applications is blurry or renders incorrectly

GTK 4 switched to grayscale antialiasing without hinting when rendering fonts. A setting is available that will restore some of the GTK 3 behavior [[11]](<https://gitlab.gnome.org/GNOME/gtk/-/issues/3787#note_1260756>). Subpixel antialiasing is not available. 
    
    ~/.config/gtk-4.0/settings.ini
    
    [Settings]
    gtk-hint-font-metrics=1

##  参见

  * [GTK 官方网站](<https://www.gtk.org/>)
  * [维基百科对 GTK 的介绍](<https://en.wikipedia.org/wiki/GTK> "wikipedia:GTK")
