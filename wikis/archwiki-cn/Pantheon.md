[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Pantheon](<../zh-cn/Talk:Pantheon.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Abandoned translation from 2016 ([447339](<../Special:%E5%B7%AE%E5%BC%82/447339.html> "Special:差异/447339"))（在 [Talk:Pantheon#](<../zh-cn/Talk:Pantheon.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [Pantheon](<https://wiki.archlinux.org/title/Pantheon> "arch:Pantheon")，最近一次同步于 2016-03-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pantheon?diff=0&oldid=423635>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pantheon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Pantheon](<https://elementaryos.org/>) 是linux发行版 elementary os 的默认桌面环境。由开发者使用vala语言和gtk3工具包编写完成，高效并且易于使用。用户界面上，与GNOME-shell和Mac OS X多有相似之处。 

##  安装

Pantheon桌面环境目前不由archlinux官方维护，要在archlinux安装使用Pantheon桌面环境可以向系统添加三方维护的软件源，并从该软件源安装相关软件包，将以下代码添加到软件源列表（需要管理员权限） `/etc/pacman.conf`:（每日构建版本） 
    
    [pantheon]
    SigLevel = Optional
    Server = http://pkgbuild.com/~alucryd/$repo/$arch
    
**提示：** 对这些软件包的编译脚本感兴趣的可以访问[Alucryd's GitHub repository](<https://github.com/alucryd/aur-alucryd/tree/master/pantheon>).

当然，如果喜欢也可以选择自己编译这些软件包，相关的软件包源码都可以直接从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 系统找到. 

如果只是向体验基础的Pantheon用户界面.可以安装[pantheon-session-bzr](<https://aur.archlinux.org/packages/pantheon-session-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]，这将自动安装以下软件包： 

  * [cerbere-bzr](<https://aur.archlinux.org/packages/cerbere-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 进程守护程序
  * [gala-bzr](<https://aur.archlinux.org/packages/gala-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 窗口管理器
  * [wingpanel-bzr](<https://aur.archlinux.org/packages/wingpanel-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 顶部面板组件
  * [slingshot-launcher-bzr](<https://aur.archlinux.org/packages/slingshot-launcher-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 顶部面板应用程序菜单
  * [plank-bzr](<https://aur.archlinux.org/packages/plank-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 地步Dock程序启动器

当然，要获取更完美的Pantheon桌面体验，还请同时安装以下软件包： 

**提示：** 请确保系统安装的以下程序包都是带-bzr的版本，已避免可能导致的错误。

  * [audience-bzr](<https://aur.archlinux.org/packages/audience-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Video player
  * [contractor-bzr](<https://aur.archlinux.org/packages/contractor-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Service for sharing data between apps
  * [dexter-contacts-bzr](<https://aur.archlinux.org/packages/dexter-contacts-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Contacts manager (does not build)
  * [eidete-bzr](<https://aur.archlinux.org/packages/eidete-bzr/>)AUR: Simple screencaster
  * [elementary-icon-theme-bzr](<https://aur.archlinux.org/packages/elementary-icon-theme-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: elementary icons
  * [elementary-scan-bzr](<https://aur.archlinux.org/packages/elementary-scan-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Simple scan utility (does not build)
  * [elementary-wallpapers-bzr](<https://aur.archlinux.org/packages/elementary-wallpapers-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: elementary wallpaper collection
  * [gtk-theme-elementary-bzr](<https://aur.archlinux.org/packages/gtk-theme-elementary-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: elementary GTK theme
  * [feedler-bzr](<https://aur.archlinux.org/packages/feedler-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: RSS feeds reader (does not build)
  * [footnote-bzr](<https://aur.archlinux.org/packages/footnote-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Note taking app
  * [geary](<https://archlinux.org/packages/?name=geary>)包: Email client
  * [indicator-pantheon-session-bzr](<https://aur.archlinux.org/packages/indicator-pantheon-session-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Session indicator
  * [lightdm-pantheon-greeter-bzr](<https://aur.archlinux.org/packages/lightdm-pantheon-greeter-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: LightDM greeter
  * [maya-calendar-bzr](<https://aur.archlinux.org/packages/maya-calendar-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Calendar
  * [midori-granite-bzr](<https://aur.archlinux.org/packages/midori-granite-bzr/>)AUR: Web browser
  * [noise-bzr](<https://aur.archlinux.org/packages/noise-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Audio player
  * [pantheon-backgrounds-bzr](<https://aur.archlinux.org/packages/pantheon-backgrounds-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Wallpaper collection
  * [pantheon-calculator-bzr](<https://aur.archlinux.org/packages/pantheon-calculator-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Calculator
  * [pantheon-default-settings-bzr](<https://aur.archlinux.org/packages/pantheon-default-settings-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Pantheon default's settings (appearance, etc.)
  * [pantheon-files-bzr](<https://aur.archlinux.org/packages/pantheon-files-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: File explorer
  * [pantheon-notify-bzr](<https://aur.archlinux.org/packages/pantheon-notify-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Notification daemon
  * [pantheon-print-bzr](<https://aur.archlinux.org/packages/pantheon-print-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Print settings
  * [pantheon-terminal-bzr](<https://aur.archlinux.org/packages/pantheon-terminal-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Terminal emulator
  * [plank-theme-pantheon-bzr](<https://aur.archlinux.org/packages/plank-theme-pantheon-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Pantheon theme for plank
  * [scratch-text-editor-bzr](<https://aur.archlinux.org/packages/scratch-text-editor-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Text editor
  * [snap-photobooth-bzr](<https://aur.archlinux.org/packages/snap-photobooth-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Webcam app
  * [switchboard-bzr](<https://aur.archlinux.org/packages/switchboard-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Settings manager

**注意：** You will also need to install plugs, look for "switchboard-plug-*" in the [AUR](<https://aur.archlinux.org/packages/?O=0&K=switchboard-plug>) or in [Alucryd's GitHub repository](<https://github.com/alucryd/aur-alucryd/tree/master/pantheon>).

推荐安装以下字体包来获取最佳桌面体验: 

  * [ttf-opensans](<https://archlinux.org/packages/?name=ttf-opensans>)包: Open Sans Fonts
  * [ttf-raleway-font-family](<https://aur.archlinux.org/packages/ttf-raleway-font-family/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: Raleway Font Family
  * [ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包: Font family based on the Bitstream Vera Fonts
  * [ttf-droid](<https://archlinux.org/packages/?name=ttf-droid>)包: General-purpose fonts released by Google as part of Android
  * [gnu-free-fonts](<https://archlinux.org/packages/?name=gnu-free-fonts>)包: Set of free outline fonts covering the Unicode character set
  * [ttf-liberation](<https://archlinux.org/packages/?name=ttf-liberation>)包: Red Hats Liberation fonts

###  补充信息

#### Packages based on older evolution-data-server

[dexter-contacts-bzr](<https://aur.archlinux.org/packages/dexter-contacts-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] and [feedler-bzr](<https://aur.archlinux.org/packages/feedler-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] do not build because they are based on evolution-data-server 3.2. Arch Linux provides version 3.10 which uses a different Vala API. 

##  启用Pantheon桌面

###  使用显示服务器启动

[pantheon-session-bzr](<https://aur.archlinux.org/packages/pantheon-session-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] provides a session entry for display managers such as [gdm](<https://archlinux.org/packages/?name=gdm>)包 or [lightdm](<https://archlinux.org/packages/?name=lightdm>)包. 

**注意：** Either use the bzr version of _cerbere_ or add 'gala' to the monitored processes for this to work.

###  通过 .xinitrc 启动

你也可以用 `~/.xinitrc` 启动Pantheon。这段代码将能够成功启动Pantheon: 
    
    #!/bin/sh
     
    if [ -d /etc/X11/xinit/xinitrc.d ]; then
      for f in /etc/X11/xinit/xinitrc.d/*; do
        [ -x "$f" ] && . "$f"
      done
      unset f
    fi
    
    gsettings-data-convert &
    xdg-user-dirs-gtk-update &
    /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
    /usr/lib/gnome-settings-daemon/gnome-settings-daemon &
    /usr/lib/gnome-user-share/gnome-user-share &
    eval $(gnome-keyring-daemon --start --components=pkcs11,secrets,ssh,gpg)
    export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID GPG_AGENT_INFO SSH_AUTH_SOCK
    exec cerbere
    
**注意：** Pantheon may refuse to start correctly, resulting in errors such as no visible mouse cursor and others. In this case you have to add the window manager 'gala' to the list of monitored processes of cebere. This can be done in `dconf-editor` and should look like [this](<https://web.archive.org/web/20140908032837/http://s0.uploads.im/AvOIT.png>). Remember do not run dconf-editor as root, use your local username.

### Autostart applications

Pantheon, when launched via `~/.xinitrc`, does not support XDG autostart. However, there are 3 other ways to achieve this for applications which do not provide a systemd unit: 

  * You may add any program to your `~/.xinitrc`, preferably right before the _exec cerbere_ line. This is the better choice for one-shot programs.
  * Or you may edit the `org.pantheon.cerbere.monitored-processes` key using _dconf-editor_ and add the programs of your choice. This method is best for applications which keep running in the background.
  * Or you may use a program like [dapper](<https://aur.archlinux.org/packages/dapper/>)AUR, [dex-git](<https://aur.archlinux.org/packages/dex-git/>)AUR, or [fbautostart](<https://aur.archlinux.org/packages/fbautostart/>)AUR to add support for XDG autostart in your `~/.xinitrc`.

**注意：** Keep in mind that applications started via _cerbere_ cannot be terminated, they will keep respawning.

## Configuration

Configuring Pantheon is done via [switchboard-bzr](<https://aur.archlinux.org/packages/switchboard-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] and its plugs, most are available in the AUR and the custom repo. All pantheon settings can also be altered via _dconf_ , they are located in the `org.pantheon` key. Use _dconf-editor_ for easy editing. 

Part of the configuration is handled by [gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 via a dedicated plug, which unfortunately only supports GNOME up to 3.6. Use [gnome-control-center](<https://archlinux.org/packages/?name=gnome-control-center>)包 itself and [gnome-tweak-tool](<https://archlinux.org/packages/?name=gnome-tweak-tool>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：replaced by [gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包] instead. 

### Pantheon Files

#### Enable context menu entries

If you want to enable context menu entries such as for [file-roller](<https://archlinux.org/packages/?name=file-roller>)包 to extract/compress archives, then you have to additionally install [contractor-bzr](<https://aur.archlinux.org/packages/contractor-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 

### Terminal

####  Opacity (transparency)

You can set a certain opacity to make Pantheon Terminal (semi-)transparent. Open `dconf-editor` and go to `org.pantheon.terminal.settings.opacity` to set your desired opacity. 

## Known Issues

### Indicators not working in wingpanel

Make sure the /etc/xdg/autostart/indicator-[name].desktop file contains Pantheon inside OnlyShowIn= 
    
    OnlyShowIn=Unity;XFCE;GNOME;Pantheon;
    
**注意：**

  * Indicator support itself is a complex issue, due to standards discrepancies between Ubuntu and Gnome's implementation of KDE's status notification indicators.
  * The pantheon devs are working on [a number of their own indicators](<https://launchpad.net/~wingpanel-devs>) for wingpanel.

### Indicator-session menus not working

  * [indicator-session-bzr](<https://aur.archlinux.org/packages/indicator-session-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

This version of indicator-session relies on dbus methods native to Unity for most of its functions; it can be made to work by patching out the use of Unity dialogs, such as in [indicator-session-pantheon-bzr](<https://github.com/quequotion/pantheon-bzr-qq/tree/master/REDUNDANT/indicator-session-pantheon-bzr>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-04 ⓘ]

  * [indicator-session](<https://aur.archlinux.org/packages/indicator-session/>)AUR

This version of indicator-session fails to interact with the session manager somehow; a (crudely hacked) version that uses systemd/logind instead is available [indicator-session-systemd](<https://aur.archlinux.org/packages/indicator-session-systemd/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

_About This Computer_ , _Lock_ and _Sound Settings_ ([indicator-sound](<https://aur.archlinux.org/packages/indicator-sound/>)AUR or [indicator-sound-pantheon-bzr](<https://github.com/quequotion/pantheon-bzr-qq/tree/master/REDUNDANT/indicator-session-pantheon-bzr>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-04 ⓘ]) rely on gnome components that may not be installed, such as gnome-control-center and gnome-screensaver. 

For _Lock_ functionality (including "Ctrl+L" hotkey), replace gnome-screensaver with [light-locker](</wzh/index.php?title=Light-locker&action=edit&redlink=1> "Light-locker（页面不存在）") or [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver") and [a script that emulates the gnome-screensaver dbus](<https://github.com/quequotion/pantheon-bzr-qq/tree/master/EXTRAS/xscreensaver-dbus-screenlock>). 

### No transparency in pantheon-terminal

Transparency in pantheon-terminal is not yet fully functional with GTK themes other than the elmentaryOS theme. Either use [gtk-theme-elementary](<https://archlinux.org/packages/?name=gtk-theme-elementary>)包 or add [this](<https://bazaar.launchpad.net/~elementary-design/egtk/4.x/revision/210>) code to your theme. 

### White icons in pantheon-files

Currently there seems to be a bug which displays the view icons in the top location in a white colour instead of black. This can be fixed by installing [gtk-theme-elementary-bzr](<https://aur.archlinux.org/packages/gtk-theme-elementary-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] or adding the following line to `gtk-widgets.css` or `gtk-widgets.css` of your [gtk-theme-elementary](<https://archlinux.org/packages/?name=gtk-theme-elementary>)包 theme: 
    
    GtkToolItem { color: @text_color; }
    
### Wingpanel is transparent

Wingpanel is transparent by design when using the elementary GTK theme. It becomes black when a maximized window occupies your screen. However, using other GTK themes will produce a solid panel most of the time. 

### Corrupted graphics in canonical indicators

Indicators behave incorrectly with every theme I have tried. They are very ancient, all of them date back to 2012 because the newer indicators depend on Ubuntu patches, and they should be killed with fire anyway. Wingpanel is doing just that and I hope the next major release will ship their new plugin system. 

### Cannot interact with the LightDM Pantheon greeter

You need to delete `/var/lib/lightdm/.pam_environment`. Do note however that this file is a workaround for the following LightDM bug: <https://bugs.launchpad.net/ubuntu/+source/unity-greeter/+bug/1024482>

## Troubleshooting

### Gala crashes on start

It appears that unconfigured gala tries to use default gnome wallpaper as a background. However, the corresponding file is absent unless you have [gnome-themes-standard](<https://archlinux.org/packages/?name=gnome-themes-standard>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] installed. Thus, install [gnome-themes-standard](<https://archlinux.org/packages/?name=gnome-themes-standard>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] to workaround the crash. It is safe to remove this package after you configure pantheon in a way you want. 

###  How can I add new applications to the dock?

Either drag and drop a desktop file on it, or right click on a running application and select "Keep in dock". You can then reorder icons by drag and drop. 

###  How can I change the default appearance such as GTK theme, font size, etc?

Use [gnome-tweak-tool](<https://archlinux.org/packages/?name=gnome-tweak-tool>)包[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：replaced by [gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包] or see [GTK+](<../zh-cn/GTK.html> "GTK+"). 

### I do not have any mouse cursor

The 'gala' window manager is most likely not running. [#通过 .xinitrc 启动](<#%E9%80%9A%E8%BF%87_.xinitrc_%E5%90%AF%E5%8A%A8>) Add 'gala' to the list of cerbere's monitored processes. 

### Wingpanel is empty except for Applications

The indicators that are displayed in the wingpanel are split into separate packages. [#安装](<#%E5%AE%89%E8%A3%85>) Install additional indicators such as [wingpanel-indicator-datetime-bzr](<https://aur.archlinux.org/packages/wingpanel-indicator-datetime-bzr/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found], [indicator-power](<https://aur.archlinux.org/packages/indicator-power/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] or [indicator-sound](<https://aur.archlinux.org/packages/indicator-sound/>)AUR. 
