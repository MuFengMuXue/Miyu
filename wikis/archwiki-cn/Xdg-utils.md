**翻译状态：**

  * 本文（或部分内容）译自 [xdg-utils](<https://wiki.archlinux.org/title/xdg-utils> "arch:xdg-utils")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/xdg-utils?diff=0&oldid=820778>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/xdg-utils_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[xdg-utils](<https://www.freedesktop.org/wiki/Software/xdg-utils/>) 提供了官方工具，用于管理 [XDG MIME 应用程序](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "XDG MIME 应用程序")。 

  * [xdg-desktop-menu(1)](<https://man.archlinux.org/man/xdg-desktop-menu.1>) \- 安装桌面菜单项
  * [xdg-desktop-icon(1)](<https://man.archlinux.org/man/xdg-desktop-icon.1>) \- 将[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")复制到用户的桌面
  * [xdg-email(1)](<https://man.archlinux.org/man/xdg-email.1>) \- 在用户首选的邮件客户端中编写新电子邮件，可能会预填入主题和其他信息
  * [xdg-icon-resource(1)](<https://man.archlinux.org/man/xdg-icon-resource.1>) \- 安装图标资源
  * [xdg-mime(1)](<https://man.archlinux.org/man/xdg-mime.1>) \- 查询和安装 MIME 类型和关联
  * [xdg-open(1)](<https://man.archlinux.org/man/xdg-open.1>) \- 在用户首选应用程序中打开文件或 URI
  * [xdg-screensaver(1)](<https://man.archlinux.org/man/xdg-screensaver.1>) \- 启用、禁用或暂停屏幕保护程序
  * [xdg-settings(1)](<https://man.archlinux.org/man/xdg-settings.1>) \- 获取或设置默认的 Web 浏览器和 URL 处理程序

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xdg-utils](<https://archlinux.org/packages/?name=xdg-utils>)包 包。 

##  使用

###  环境变量

**注意：** 正常运行的桌面环境应该会自动设置这些变量。本节仅在理解 _xdg-utils_ 的工作原理时需要，即用于故障排除。

_xdg-utils_ 尝试通过调用其提供的专用程序来与您的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")集成，在适用的情况下。当前环境的评估如下[[1]](<https://gitlab.freedesktop.org/xdg/xdg-utils/-/blob/d11b33ec7f24cfb1546f6b459611d440013bdc72/scripts/xdg-utils-common.in#L270-L364>)： 

  * 如果设置了标准化的 [XDG_CURRENT_DESKTOP](<../zh-cn/XDG_CURRENT_DESKTOP.html> "XDG CURRENT DESKTOP") 环境变量，并且该值属于已识别的桌面环境，则使用相应的值。
  * 如果存在任何经典回退或特定环境变量，例如 KDE 的 `KDE_FULL_SESSION`，则使用相应的值。
  * 如果设置了遗留的 [DESKTOP_SESSION](<../zh-cn/Environment_variables.html#Examples> "Environment variables") 环境变量，并且该值属于已识别的桌面环境，则使用相应的值。

在此过程中，如果找到任何匹配项，则 [DE](<../zh-cn/Environment_variables.html#Examples> "Environment variables") 变量会被内部覆盖为检测到的桌面环境的标准化值。因此，`DE` 既是一个遗留的环境变量，也是 _xdg-utils_ 的内部状态变量。例如，如果 `XDG_CURRENT_DESKTOP` 是 `KDE`， _xdg-utils_ 会将 `DE` 设置为 `kde`。如果没有找到匹配项，则会使用任何已存在的 `DE` 值， 这样 `XDG_CURRENT_DESKTOP=KDE` 就等于 `XDG_CURRENT_DESKTOP` 未设置并且 `DE=kde`。此实现细节值得注意，因为它导致**如果桌面环境已被检测到，预设的`DE` 会被忽略**。 

_xdg-utils_ 识别的环境变量值如下： 

桌面环境 | `XDG_CURRENT_DESKTOP` | `DE` |  `DESKTOP_SESSION`  
---|---|---|---  
– |  `X-Generic`1 | `generic` | –   
[Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") |  `Cinnamon`, `X-Cinnamon` | `cinnamon` | –   
[Deepin](<../zh-cn/%E6%B7%B1%E5%BA%A6%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "Deepin") |  `Deepin`, `DEEPIN`, `deepin`1 | `deepin` | –   
[Enlightenment](<../zh-cn/Enlightenment.html> "Enlightenment") |  `ENLIGHTENMENT`1 | `enlightenment` | –   
[GNOME](<../zh-cn/GNOME.html> "GNOME") |  `GNOME`2 | `gnome` |  `gnome`  
[GNOME Flashback](<../zh-cn/GNOME_Flashback.html> "GNOME Flashback") |  `GNOME-Flashback`, `GNOME-Flashback:GNOME`2 | `gnome` |  `gnome`  
[KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") | `KDE` | `kde` | –   
[LXDE](<../zh-cn/LXDE.html> "LXDE") | `LXDE` | `lxde` |  `LXDE`  
[LXQt](<../zh-cn/LXQt.html> "LXQt") | `LXQt` | `lxqt` | –   
[MATE](<../zh-cn/MATE.html> "MATE") | `MATE` | `mate` |  `mate`  
[Xfce](<../zh-cn/Xfce.html> "Xfce") | `XFCE` | `xfce` |  `xfce`, `xfce4`, `Xfce Session`  
  
  1. 这不是一个已在 freedesktop.org 上[注册](<https://specifications.freedesktop.org/menu-spec/latest/onlyshowin-registry.html>)的环境。
  2. GNOME 变体，包括 _GNOME Classic_ 模式，都被 _xdg-utils_ 视为相同的。

请注意，这仅仅是 _xdg-utils_ 提供的脚本能够 _检测_ 的列表。脚本仍会在以下条件下执行通用的、与环境无关的操作： 

  * 请求了通用例程，使用 `XDG_CURRENT_DESKTOP=X-Generic` 或 `DE=generic`。
  * 环境检测失败。所有相关的环境变量都无法识别或未设置，而经典回退也没有揭示任何信息。
  * 执行了特定环境的操作，但失败了，例如由于缺少程序。

### xdg-mime

[xdg-mime(1)](<https://man.archlinux.org/man/xdg-mime.1>) 是一个用于直接查询和修改默认 MIME 应用程序的脚本。它在其他脚本中使用，例如 _xdg-open_ ，并且还是一个有用的故障排除工具。 

确定文件的 MIME 类型： 
    
    $ xdg-mime query filetype photo.jpeg
    image/jpeg
    
确定 MIME 类型的默认应用程序： 
    
    $ xdg-mime query default image/jpeg
    gimp.desktop
    
更改 MIME 类型的默认应用程序： 
    
    $ xdg-mime default feh.desktop image/jpeg
    
将文件管理器设置为默认文件管理器（例如 -Thunar）： 
    
    $ xdg-mime default thunar.desktop inode/directory
    
调试 MIME 类型的默认应用程序： 
    
    $ env XDG_UTILS_DEBUG_LEVEL=10  xdg-mime query default text/html
    Checking /home/user/.config/mimeapps.list
    Checking /home/user/.local/share/applications/defaults.list and /home/user/.local/share/applications/mimeinfo.cache
    Checking /usr/local/share/applications/defaults.list and /usr/local/share/applications/mimeinfo.cache
    Checking /usr/share/applications/defaults.list and /usr/share/applications/mimeinfo.cache
    qutebrowser.desktop
    
当需要确定文件的 MIME 类型时， _xdg-mime_ 会尝试使用适合桌面环境的程序： 

桌面环境 | 程序 | 包   
---|---|---  
[Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") |  `gio` |  [glib2](<https://archlinux.org/packages/?name=glib2>)包  
[GNOME](<../zh-cn/GNOME.html> "GNOME")  
[GNOME Flashback](<../zh-cn/GNOME_Flashback.html> "GNOME Flashback")  
[LXDE](<../zh-cn/LXDE.html> "LXDE")  
[MATE](<../zh-cn/MATE.html> "MATE")  
[Xfce](<../zh-cn/Xfce.html> "Xfce")  
[Deepin](<../zh-cn/%E6%B7%B1%E5%BA%A6%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "Deepin") | –  | –   
[Enlightenment](<../zh-cn/Enlightenment.html> "Enlightenment")  
[LXQt](<../zh-cn/LXQt.html> "LXQt")  
[KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") | `kmimetypefinder` |  [kde-cli-tools](<https://archlinux.org/packages/?name=kde-cli-tools>)包  
  
在通用情况下， _xdg-mime_ 将： 

  * 如果存在，委托给 [mimetype](<../zh-cn/Default_applications.html#perl-file-mimeinfo> "Default applications")。需要安装 [perl-file-mimeinfo](<https://archlinux.org/packages/?name=perl-file-mimeinfo>)包 包。
  * 如果存在，委托给 [file](<https://archlinux.org/packages/?name=file>)包。

### xdg-open

[xdg-open(1)](<https://man.archlinux.org/man/xdg-open.1>) 是一个[资源打开器](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html#%E8%B5%84%E6%BA%90%E6%89%93%E5%BC%80%E5%99%A8> "资源打开器")，被许多应用程序使用，遵循 XDG MIME 应用程序标准，并尽可能与系统的桌面环境集成。 

如果检测到桌面环境，将调用其提供的处理程序 [[2]](<https://gitlab.freedesktop.org/xdg/xdg-utils/-/blob/master/scripts/xdg-open.in>): 

桌面环境 | 程序 | 包   
---|---|---  
[Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") |  `gio` |  [glib2](<https://archlinux.org/packages/?name=glib2>)包  
[GNOME](<../zh-cn/GNOME.html> "GNOME")  
[GNOME Flashback](<../zh-cn/GNOME_Flashback.html> "GNOME Flashback")  
[MATE](<../zh-cn/MATE.html> "MATE")  
[Deepin](<../zh-cn/%E6%B7%B1%E5%BA%A6%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "Deepin") | `dde-open` |  [deepin-api](<https://archlinux.org/packages/?name=deepin-api>)包  
[Enlightenment](<../zh-cn/Enlightenment.html> "Enlightenment") |  `enlightenment_open` |  [enlightenment](<https://archlinux.org/packages/?name=enlightenment>)包  
[KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") |  `kde-open`1 |  [kde-cli-tools](<https://archlinux.org/packages/?name=kde-cli-tools>)包  
[LXDE](<../zh-cn/LXDE.html> "LXDE") | `pcmanfm` |  [pcmanfm](<https://archlinux.org/packages/?name=pcmanfm>)包  
[LXQt](<../zh-cn/LXQt.html> "LXQt") | – | –   
[Xfce](<../zh-cn/Xfce.html> "Xfce") |  `exo-open`2 |  [exo](<https://archlinux.org/packages/?name=exo>)包  
  
  1. 如果 `KDE_SESSION_VERSION` 未设置，则会使用 `kfmclient` 来自 [konqueror](<https://archlinux.org/packages/?name=konqueror>)包。不过，KDE Plasma 应该始终设置此变量。
  2. 还会尝试使用来自 [glib2](<https://archlinux.org/packages/?name=glib2>)包 的 `gio`。

在通用情况下， _xdg-open_ 将： 

  * 查询 [#xdg-mime](<#xdg-mime>) 以获取与资源关联的默认桌面条目，解析桌面条目，并执行其命令。
  * 如果存在，委托给 [run-mailcap](<../zh-cn/Default_applications.html#run-mailcap> "Default applications")。需要安装 [run-mailcap](<https://aur.archlinux.org/packages/run-mailcap/>)AUR 包。
  * 如果存在，委托给 [mimeopen](<../zh-cn/Default_applications.html#perl-file-mimeinfo> "Default applications")。需要安装 [perl-file-mimeinfo](<https://archlinux.org/packages/?name=perl-file-mimeinfo>)包 包。

**提示：** 要查看 _xdg-open_ 将使用哪个后端，请设置 `XDG_UTILS_DEBUG_LEVEL=3`。

由于 _xdg-mime_ 依赖于 [perl-file-mimeinfo](<https://archlinux.org/packages/?name=perl-file-mimeinfo>)包 包来实现 [XDG MIME 应用程序](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "XDG MIME 应用程序")标准，如果您没有使用桌面环境，应该安装 [perl-file-mimeinfo](<https://archlinux.org/packages/?name=perl-file-mimeinfo>)包，或考虑使用其他[资源打开器](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html#%E8%B5%84%E6%BA%90%E6%89%93%E5%BC%80%E5%99%A8> "资源打开器")。 

### xdg-settings

请参见 [xdg-settings(1)](<https://man.archlinux.org/man/xdg-settings.1>)。 

设置所有 Web MIME 类型使用单个应用程序的快捷方式： 
    
    $ xdg-settings set default-web-browser firefox.desktop
    
设置 URL 方案的默认应用程序的快捷方式： 
    
    $ xdg-settings set default-url-scheme-handler irc xchat.desktop
    
##  提示与技巧

###  URL 方案处理程序

要设置 URL 方案的默认应用程序，您可能还需要更改 `x-scheme-handler/*` MIME 类型的默认应用程序： 
    
    $ xdg-mime default firefox.desktop x-scheme-handler/https x-scheme-handler/http
    