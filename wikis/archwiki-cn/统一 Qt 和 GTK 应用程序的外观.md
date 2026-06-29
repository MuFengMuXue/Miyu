**翻译状态：**

  * 本文（或部分内容）译自 [Uniform look for Qt and GTK applications](<https://wiki.archlinux.org/title/Uniform_look_for_Qt_and_GTK_applications> "arch:Uniform look for Qt and GTK applications")，最近一次同步于 2021年3月4日，若英文版本有所[更改](<https://wiki.archlinux.org/title/Uniform_look_for_Qt_and_GTK_applications?diff=0&oldid=651850>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Uniform_look_for_Qt_and_GTK_applications_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GTK](<../zh-cn/GTK.html> "GTK")
  * [Qt](<../zh-cn/Qt.html> "Qt")

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 此文许多内容已过时。 (在[Talk:统一 Qt 和 GTK 应用程序的外观](<../zh-cn/Talk:%E7%BB%9F%E4%B8%80_Qt_%E5%92%8C_GTK_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A4%96%E8%A7%82.html>)讨论)

基于 [Qt](<../zh-cn/Qt.html> "Qt") 和 [GTK](<../zh-cn/GTK.html> "GTK") 的程序使用不同的图形库来渲染图形化用户界面，各自具有不同的主题、风格和图标，所以观感明显有所不同。这篇文章将使你的 Qt 和 GTK 程序看起来更相似，以此获得更加现代化、集成化的桌面体验。 

##  介绍

要想在不同的图形库之间获得相似的外观，你通常需要修改以下内容： 

  * **主题** ——应用程序和组件等元素的自定义外观。通常包含一套风格、图标主题和颜色主题。
  * **风格** ——组件的布局和样式。
  * **图标主题** ——全局图标。
  * **颜色主题** ——与风格相适应的全局颜色样式。

你可以选择下面的不同方法： 

  * 使用下面列出的，适用于各个图形库的工具分别修改 [Qt 和 GTK 的主题](<#Qt_%E5%92%8C_GTK_%E9%80%9A%E7%94%A8%E7%9A%84%E4%B8%BB%E9%A2%98>)，以选择外观相似的主题（样式，颜色，图标，光标，字体）。
  * 使用特殊的[主题引擎](<#%E4%B8%BB%E9%A2%98%E5%BC%95%E6%93%8E>)，该引擎作为中间人修改其他图形库的主题，以匹配您的主要图形库。

##  Qt 和 GTK 通用的主题

下面列出了几种主题，Qt 和 GTK 都可使用，并且风格统一。这些主题适配了 Qt 和 GTK 的主要版本。有了这些主题，你就可以在使用不同的图形库构建的应用程序之间得到相同的外观了。 

**提示：** 如果希望将用户定义的主题应用于 root 用户的应用, 参考[GTK#主题没有应用到 root 用户的应用程序上](<../zh-cn/GTK.html#%E4%B8%BB%E9%A2%98%E6%B2%A1%E6%9C%89%E5%BA%94%E7%94%A8%E5%88%B0_root_%E7%94%A8%E6%88%B7%E7%9A%84%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E4%B8%8A> "GTK")和[Qt#主题没有应用到 root 用户的应用程序上](<../zh-cn/Qt.html#%E4%B8%BB%E9%A2%98%E6%B2%A1%E6%9C%89%E5%BA%94%E7%94%A8%E5%88%B0_root_%E7%94%A8%E6%88%B7%E7%9A%84%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E4%B8%8A> "Qt")。

**注意：** GTK 3 从 3.16 版本开始[不再支持](<https://bbs.archlinux.org/viewtopic.php?pid=1518404#p1518404>)非 CSS 主题，因此，以前的解决方案，例如 Oxygen-Gtk，[已经不再可用](<https://bugs.kde.org/show_bug.cgi?id=340288>)。

### Breeze

Breeze 是 KDE Plasma 的默认 Qt 主题。它可以通过适用于 Qt 5 的 [breeze](<https://archlinux.org/packages/?name=breeze>)包，适用于 Qt 4 的 [breeze-kde4](<https://aur.archlinux.org/packages/breeze-kde4/>)AUR 以及适用于 GTK 2 和 GTK 3 的 [breeze-gtk](<https://archlinux.org/packages/?name=breeze-gtk>)包 软件包安装。 

安装后，您可以使用[GTK 配置工具](<../zh-cn/GTK.html#%E9%85%8D%E7%BD%AE%E5%B7%A5%E5%85%B7> "GTK")更改 GTK 主题。 

如果当前运行的是 KDE Plasma，请安装 [kde-gtk-config](<https://archlinux.org/packages/?name=kde-gtk-config>)包，然后从命令行运行之；或者注销后重新登录，接着转到 _系统设置 > 外观 > 应用程序风格 > 配置 GNOME/GTK 应用程序风格…_来配置 GTK 程序的主题。“系统设置”中设置的字体、图标主题、光标和组件样式将自动应用至 GTK，仅 GTK 主题需要用前面提到的 GTK 配置工具手动更改。 

### Adwaita

Adwaita是 GNOME 默认的主题。GTK 3 版本包含在 [gtk3](<https://archlinux.org/packages/?name=gtk3>)包 软件包中，而 GTK 2 版本包含在 [gnome-themes-extra](<https://archlinux.org/packages/?name=gnome-themes-extra>)包 中。[adwaita-qt](<https://github.com/MartinBriza/adwaita-qt>)是 Adwaita 主题的 Qt 移植版本。与模仿 GTK 2 主题的 [#QGtkStyle](<#QGtkStyle>) 不同，它提供了与 GTK 3 Adwaita 相似的原生 Qt 样式。可以通过适用于 Qt 4 的 [adwaita-qt4](<https://aur.archlinux.org/packages/adwaita-qt4/>)AUR、适用于 Qt 5 的 [adwaita-qt5](<https://archlinux.org/packages/?name=adwaita-qt5>)包 和适用于 Qt 6 的 [adwaita-qt6](<https://archlinux.org/packages/?name=adwaita-qt6>)包 软件包来安装此主题。 

要将 Qt 样式设置为默认值： 

  * 对于 Qt 4，可以使用 _Qt 配置_ （`qtconfig-qt4`）启用它，在 _外观 > GUI 样式_中选择 _adwaita_ 。或者，编辑 `/etc/xdg/Trolltech.conf`（系统范围）或 `~/.config/Trolltech.conf`（用户范围）文件：

    ~/.config/Trolltech.conf
    
    ...
    [Qt]
    style=adwaita
    ...

  * 对于 Qt 5，可以通过以下环境变量来启用主题：`QT_STYLE_OVERRIDE=adwaita`。或者，使用 [qt5ct](<https://archlinux.org/packages/?name=qt5ct>)包 软件包。更多详细说明，参考 [Qt#在KDE Plasma以外的环境下配置Qt5应用程序](<../zh-cn/Qt.html#%E5%9C%A8KDE_Plasma%E4%BB%A5%E5%A4%96%E7%9A%84%E7%8E%AF%E5%A2%83%E4%B8%8B%E9%85%8D%E7%BD%AEQt5%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F> "Qt")。

##  主题引擎

主题引擎可以认为是一个简单的 API，用于从一个或多个图形库转译主题（图标除外）。这些引擎为进程添加额外的代码，这种解决方案不如使用原生主题那样优雅可行。 

### Kvantum

Kvantum（[kvantum](<https://archlinux.org/packages/?name=kvantum>)包）是一个用于 Qt 5 的，基于 SVG 的可定制主题引擎，具有多种内置样式，包含一些版本的流行 GTK 主题，例如 Adapta、Arc、Ambiance 和 Materia。 

Kvantum 被视为一种风格而不是主题。要通过环境变量的方式为所有 Qt 应用设置 Kvantum，使用`QT_STYLE_OVERRIDE=kvantum`

####  主题配置

要为 Kvantum [设置一个主题变体](<https://github.com/tsujan/Kvantum/blob/master/Kvantum/doc/Theme-Config.pdf>)，如 [KvLibadwaita](<https://github.com/GabePoel/KvLibadwaita>)，像这样编辑配置文件： 
    
    /etc/xdg/Kvantum/kvantum.kvconfig（或 ~/.config/Kvantum/kvantum.kvconfig）
    
    ...
    theme=KvLibadwaita
    ...

### QGtkStyle

**注意：** QGtkStyle 已从 [qt5-base](<https://archlinux.org/packages/?name=qt5-base>)包 5.7.0 中移除[[1]](<https://github.com/qtproject/qtbase/commit/899a815414e95da8d9429a4a4f4d7094e49cfc55>)并添加到 [qt5-styleplugins](<https://aur.archlinux.org/packages/qt5-styleplugins/>)AUR 中[[2]](<https://github.com/qtproject/qtstyleplugins/commit/102da7d50231fc5723dba6e72340bef3d29471aa>)。

**警告：** 取决于 GTK 2 的主题，此样式可能会导致显示问题，例如透明的字体或不一致的部件。

此 Qt 样式使用 GTK 2 渲染所有组件以便于与 [GNOME](<../zh-cn/GNOME.html> "GNOME") 和类似基于 GTK 的环境相协调。从 Qt 4.5 开始，此样式包含在 Qt 中。它要求安装 [gtk2](<https://archlinux.org/packages/?name=gtk2>)包 并进行配置。 

这是 Cinnamon、GNOME 和 Xfce 中的默认 Qt 4 样式，也是 Cinnamon、GNOME、MATE、LXDE 和 Xfce 中的默认 Qt 5 样式。至于其他环境： 

  * 对于Qt4，可以使用 _Qt 配置_ （`qtconfig-qt4`）启用它，在 _外观 > GUI 样式_下选择 _GTK_ 。或者，编辑 `/etc/xdg/Trolltech.conf`（系统范围）或 `~/.config/Trolltech.conf`（用户范围）：

    ~/.config/Trolltech.conf
    
    ...
    [Qt]
    style=GTK+
    ...

  * 对于 Qt 5，可以通过安装 [qt5-styleplugins](<https://aur.archlinux.org/packages/qt5-styleplugins/>)AUR 并设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html#%E5%9B%BE%E5%BD%A2%E7%8E%AF%E5%A2%83> "环境变量")来启用它：`QT_QPA_PLATFORMTHEME=gtk2`

  * 对于 Qt 6，可以通过安装 [qt6gtk2](<https://aur.archlinux.org/packages/qt6gtk2/>)AUR 并在 [qt6ct](<https://archlinux.org/packages/?name=qt6ct>)包 中选择 _qt6gtk2_ 样式，或设置以下环境变量：`QT_QPA_PLATFORMTHEME=gtk2`。

为了完全统一，请确保配置的 [GTK 主题](<../zh-cn/GTK.html#%E4%B8%BB%E9%A2%98> "GTK")同时支持 GTK 2 和 GTK 3。如果你的首选主题在将 Qt 配置为使用 GTK 2 后出现了不一致的渲染效果，请安装 [gtk-theme-switch2](<https://aur.archlinux.org/packages/gtk-theme-switch2/>)AUR，然后选择一个主题。 

### QAdwaitaDecorations

Qt 装饰插件实现类似 GNOME Adwaita 的客户端装饰，适用于Qt 6 和 QT 5 平台。 

安装 [qadwaitadecorations-qt5](<https://aur.archlinux.org/packages/qadwaitadecorations-qt5/>)AUR 和 [qadwaitadecorations-qt6](<https://archlinux.org/packages/?name=qadwaitadecorations-qt6>)包 软件包。 

可以通过设置环境变量 `QT_WAYLAND_DECORATION=adwaita` 开启。 

### QWhiteSurGtkDecorations

QWhiteSurGtkDecorations是一个 Qt 装饰插件，可以在Gnome wayland上实现类似 GNOME WhiteSur-gtk 主题风格的客户端装饰，适用于Qt 6 和 QT 5 平台。 

需要安装 [qwhitesurgtkdecorations-qt5](<https://aur.archlinux.org/packages/qwhitesurgtkdecorations-qt5/>)AUR 和 [qwhitesurgtkdecorations-qt6](<https://archlinux.org/packages/?name=qwhitesurgtkdecorations-qt6>)包 软件包。 

可以通过设置环境变量 `QT_WAYLAND_DECORATION=whitesur-gtk` 启用它。 

## Tips and tricks

###  在Qt应用程序中使用GTK图标主题

如果您正在运行Plasma，请安装[kde-gtk-config](<https://archlinux.org/packages/?name=kde-gtk-config>)包，然后在 _系统设置 > 应用程序风格 > 应用样式 > 配置GNOME/GTK应用样式_下选择图标主题。 

如果您使用的是[GNOME](<../zh-cn/GNOME.html> "GNOME")，请首先检查是否安装了[dconf-editor](<https://archlinux.org/packages/?name=dconf-editor>)包。 

然后，运行`dconf-editor`，然后在 _org > gnome > desktop > interface_ 下查找`icon-theme`键，并将其更改为您的首选图标主题。 

如果您使用的不是[GNOME](<../zh-cn/GNOME.html> "GNOME")，例如，如果您使用的是[i3-wm](<https://archlinux.org/packages/?name=i3-wm>)包，请首先安装[dconf-editor](<https://archlinux.org/packages/?name=dconf-editor>)包。 

然后，运行`dconf-editor`，然后在 _org > gnome > desktop> interface_下查找`icon-theme`键，并将其更改为您的图标主题。 

由于您使用的不是[GNOME](<../zh-cn/GNOME.html> "GNOME")，因此可能需要在个人的配置文件中设置`DESKTOP_SESSION`的值。 为此，请在终端中执行以下代码，然后重新启动系统。 
    
    $ echo 'export DESKTOP_SESSION=gnome' >> /etc/profile
    
**或者**

将`export DESKTOP_SESSION=gnome`设置在`~/.xinitrc`中的某个位置，或者在[Xprofile](<../zh-cn/Xprofile.html> "Xprofile")中使用一个[Display manager](<../zh-cn/Display_manager.html> "Display manager")。 

**注意：** 如果未应用图标主题，则可能要检查您输入的首选主题名称是否格式正确。例如，如果要将当前活动的图标主题应用于QT应用程序，则可以使用以下命令找到其名称的正确格式： 
    
    $ awk -F= '/icon-theme/ {print $2}' ~/.gtkrc-2.0

###  添加标题栏和框架到KDE Plasma下的GTK3应用程序

要使Gnome/GTK应用程序显示KDE/Plasma的标题栏和框架，请安装[gtk3-nocsd-git](<https://aur.archlinux.org/packages/gtk3-nocsd-git/>)AUR并重新启动窗口管理器以加载更新的库路径。 

您还可以使用它运行Gtk应用程序： 
    
    $ gtk3-nocsd gedit
    
###  在KDE Plasma下改善GTK应用程序的亚像素渲染

See [Font configuration#LCD filter](<../zh-cn/Font_configuration.html#LCD_filter> "Font configuration"). 

###  一致的文件对话框

为了具有相同的文件对话框，可以使用XDG Portal。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包和[xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包，并在环境变量[environment variable](<../zh-cn/Environment_variable.html> "Environment variable")中设置`GTK_USE_PORTAL=1`。 

##  故障排查

###  主题对GTK程序无效

如果你安装的风格或主题引擎在某些GTK程序不能显示，很可能你的GTK设置文件因某些原因不能被加载。你可以检查你的系统找到那些文件作如下设置： 
    
    export | grep gtk
    
通常那些文件设置在 ~/.gtkrc （GTK1）, ~/.gtkrc2.0 或 ~/.gtkrc2.0-kde （GTK2） 

新版gtk-qt-engine 使用 ~/.gtkrc2.0-kde 和 ~/.kde/env/gtk-qt-engine.rc.sh 设置输出变量 如果你最近移除了gtk-qt-engine然后试图设置GTK主题，你必有要移除 ~/.kde/env/gtk-qt-engine.rc.sh 然后重启。这样做会使GTK外观使用标准的设置 ~/.gtkrc2.0来代替 ~/.gtkrc2.0-kde 

###  系统升级后GTK应用程序不使用svg（breeze）图标

尝试运行下面命令来解决问题： 
    
    # gdk-pixbuf-query-loaders --update-cache
    
###  Flatpak Qt应用程序不使用Gnome Adwaita黑暗主题

如果将主题切换为Adwaita-dark后，Flatpak Qt应用程序仍使用精简版，请安装所需的KStyle： 
    
    # flatpak install flathub org.kde.KStyle.Adwaita
    
###  即使在设置Qt主题后，在GNOME Wayland上运行的Qt应用也有不匹配的窗口装饰外观

安装 [qadwaitadecorations-qt5](<https://aur.archlinux.org/packages/qadwaitadecorations-qt5/>)AUR 和 [qadwaitadecorations-qt6](<https://aur.archlinux.org/packages/qadwaitadecorations-qt6/>)AUR，并设置以下环境变量[environment variable](<../zh-cn/Environment_variables.html#Graphical_environment> "Environment variables"):`export QT_WAYLAND_DECORATION=adwaita`。 

###  GTK 应用程序不能完全使用 KDE 系统设置

为了进一步整合 GTK 应用程序上的 [Plasma](<../zh-cn/KDE.html> "Plasma") 设置，可能需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gnome-settings-daemon](<https://archlinux.org/packages/?name=gnome-settings-daemon>)包、[gsettings-desktop-schemas](<https://archlinux.org/packages/?name=gsettings-desktop-schemas>)包 和 [gsettings-qt](<https://archlinux.org/packages/?name=gsettings-qt>)包，这将为 GTK 提供适当的 Qt 绑定。 

###  安装kde-gtk-config后，没有“系统设置>应用程序样式> GTK”菜单

使用[kde-gtk-config](<https://archlinux.org/packages/?name=kde-gtk-config>)包时，可以选择[lxappearance](<https://archlinux.org/packages/?name=lxappearance>)包之类的[GTK configuration tools](<../zh-cn/GTK.html#Configuration_tools> "GTK")来配置GTK 2和GTK 3样式。 

即使它来自LXDE项目，它也是与桌面无关的（它不需要LXDE桌面的其他部分） 

###  Dolphin主题与Nautilus匹配效果不佳

参考 [arch:Dolphin#Mismatched_folder_view_background_colors](<https://wiki.archlinux.org/title/Dolphin#Mismatched_folder_view_background_colors> "arch:Dolphin") 小节以解决颜色奇怪的问题 
