**翻译状态：**

  * 本文（或部分内容）译自 [Telegram](<https://wiki.archlinux.org/title/Telegram> "arch:Telegram")，最近一次同步于 2023-01-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Telegram?diff=0&oldid=759988>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Telegram_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Telegram](<https://en.wikipedia.org/wiki/Telegram_\(software\)> "wikipedia:Telegram \(software\)") 是一种基于云的跨平台即时消息服务，具有可选的端到端加密。创建帐户需要手机号。 

官方客户端是开源的，但最新版本的代码并不总是立即发布。服务器端代码是专有的。 

##  安装

在 Arch Linux 上，你可以这样使用 Telegram: 

###  聊天软件的插件

  * [telegram-tdlib-purple-git](<https://aur.archlinux.org/packages/telegram-tdlib-purple-git/>)AUR 为基于 [libpurple](<https://archlinux.org/packages/?name=libpurple>)包 的聊天软件 （例如 [Pidgin](<../zh-cn/Pidgin.html> "Pidgin") ） 提供了支持。
  * 基于 [Telepathy](<https://en.wikipedia.org/wiki/Telepathy_\(software\)> "wikipedia:Telepathy \(software\)") （例如 GNOME 的 [empathy](<https://aur.archlinux.org/packages/empathy/>)AUR）的软件可以使用 [telepathy-haze](<https://archlinux.org/packages/?name=telepathy-haze>)包，它也支持[libpurple](<https://archlinux.org/packages/?name=libpurple>)包，所以也可以用 [telegram-tdlib-purple-git](<https://aur.archlinux.org/packages/telegram-tdlib-purple-git/>)AUR 提供支持。
  * [KDE](<../zh-cn/KDE.html> "KDE") 用户可以使用 [telepathy-morse](<https://archlinux.org/packages/?name=telepathy-morse>)包 将默认聊天程序设置为 Telegram。

###  图形界面

[telegram-desktop](<https://archlinux.org/packages/?name=telegram-desktop>)包 提供了[官方桌面版客户端](<https://desktop.telegram.org/%7C>)。 

三方客户端: 

  * **Kotatogram Desktop** — Kotatogram Desktop 基于 Telegram Desktop，具有 Telegram Desktop 的所有功能，但也有一些更实用、更美观的功能。

     <https://kotatogram.github.io/> || [kotatogram-desktop](<https://aur.archlinux.org/packages/kotatogram-desktop/>)AUR 或者 [kotatogram-desktop-bin](<https://aur.archlinux.org/packages/kotatogram-desktop-bin/>)AUR

###  终端客户端

  * **Telegram messenger CLI** — Telegram 的命令行界面，使用 readline 界面。

     <https://github.com/vysheng/tg> || [telegram-cli-git](<https://aur.archlinux.org/packages/telegram-cli-git/>)AUR

  * **ncTelegram** — 用 Python 和 urwid 库开发的 [Ncurses](<https://en.wikipedia.org/wiki/Ncurses> "wikipedia:Ncurses") Telegram 客户端，依赖于 [telegram-cli-git](<https://aur.archlinux.org/packages/telegram-cli-git/>)AUR。

     <https://github.com/Nanoseb/ncTelegram> || [nctelegram-git](<https://aur.archlinux.org/packages/nctelegram-git/>)AUR

  * **tg** — Telegram 终端客户端。

     <https://github.com/paul-nameless/tg> || [telegram-tg](<https://aur.archlinux.org/packages/telegram-tg/>)AUR

  * **telegram-send** — Telegram-send 不是完整的客户端,是一款命令行工具，用于通过 Telegram 向账户、群组或频道发送消息和文件。 它提供了一个简单的界面，可以方便地从其他程序中调用。

     <https://github.com/rahiel/telegram-send> || [python-telegram-send](<https://aur.archlinux.org/packages/python-telegram-send/>)AUR

  * **nchat** — nchat 是一款基于终端的聊天客户端，适用于 Linux 和 macOS，支持 Telegram 和 WhatsApp。

     <https://github.com/d99kris/nchat> || [nchat-git](<https://aur.archlinux.org/packages/nchat-git/>)AUR

  * **telega.el** — GNU Emacs Telegram 平台的全功能非官方客户端。

     <https://github.com/zevlg/telega.el> || 此软件并不在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中

  * **TelegramTUI** — 基于 Python 的 TUI telegram

     <https://github.com/vtr0n/TelegramTUI> || 此软件并不在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中，你可以通过 `pipx install telegramtui` 安装

###  基于网页的客户端

  * 官方的 [Telegram WebK](<https://web.telegram.org/k/>)。
  * [官方网页应用 Telegram Web](<https://web.telegram.org>)。
  * [franz](<https://aur.archlinux.org/packages/franz/>)AUR 是[开源](<https://github.com/meetfranz/franz>)的 Web 客户端，可以作为 [Telegram](<https://en.wikipedia.org/wiki/Telegram_\(software\)> "wikipedia:Telegram \(software\)"), [WhatsApp](<https://en.wikipedia.org/wiki/WhatsApp> "wikipedia:WhatsApp"), [Facebook](<https://en.wikipedia.org/wiki/Facebook> "wikipedia:Facebook") 等应用的客户端。
  * [rambox-bin](<https://aur.archlinux.org/packages/rambox-bin/>)AUR 是 Franz 的备选之一，也是开源的，提供了各个功能的对标组件。
  * [Telegram Web 的 Chrome app](<https://telegram.org/dl/webogram/chromeapp>)。

##  提示和技巧

###  在 Telegram 中使用 GTK 对话框

如果你想要使用 [GTK](<../zh-cn/GTK.html> "GTK") 对话框来代替 [Qt](<../zh-cn/Qt.html> "Qt") 对话框，请将[环境变量](<../zh-cn/Environment_variable.html> "Environment variable")`QT_QPA_PLATFORMTHEME` 设置为 `gtk3`。 

###  Telegram 桌面中的 KDE 对话框

如果想使用 [KDE](<../zh-cn/KDE.html> "KDE") 文件对话框来代替 [Qt](<../zh-cn/Qt.html> "Qt") 对话框，请将[环境变量](<../zh-cn/Environment_variable.html> "Environment variable") `QT_QPA_PLATFORMTHEME` 设置为 `xdgdesktopportal`。 

###  使用 SVG 图标主题

如果您想使用基于 SVG 图像的图标主题 (e.g. [papirus-icon-theme](<https://archlinux.org/packages/?name=papirus-icon-theme>)包)，请安装 [qt5-svg](<https://archlinux.org/packages/?name=qt5-svg>)包。参见 [Qt#Icon theme is not applied](<../zh-cn/Qt.html#Icon_theme_is_not_applied> "Qt")。 

###  Wayland 支持

参见 [Wayland#Qt](<../zh-cn/Wayland.html#Qt> "Wayland")。 

###  Telegram Desktop 中的 xdg-open

如果你想在 t.me 链接上使用 xdg-open 并收到一个错误，找不到 tg 的处理程序： 
    
    xdg-mime default telegramdesktop.desktop application/x-xdg-protocol-tg
    xdg-mime default telegramdesktop.desktop x-scheme-handler/tg

### Failed to set real-time priority for thread: Operation not permitted

如果获得以下错误信息： 
    
    $ telegram-desktop
    
    [ALSOFT] (EE) Failed to set real-time priority for thread: Operation not permitted (1)
    
安装 [realtime-privileges](<https://archlinux.org/packages/?name=realtime-privileges>)包，并[添加](<../zh-cn/Users_and_groups.html#Group_management> "Users and groups")您自己到 `realtime` 用户组并重启。参见[Realtime process management#Configuring PAM](</wzh/index.php?title=Realtime_process_management&action=edit&redlink=1> "Realtime process management（页面不存在）")。 

###  HiDPI 缩放

如果系统启用了 Qt 缩放，且缩放比例不是整数，你可能遇到[图片和图标出现马赛克](<https://github.com/telegramdesktop/tdesktop/issues/23953>)的问题。此时可能需要单独针对 Telegram 关闭[高 DPI 缩放](<https://doc.qt.io/qt-5/highdpi.html#high-dpi-support-in-qt>)。 

将 `/usr/share/applications/telegramdesktop.desktop` 复制到[用户特定应用程序目录](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%A1%B9> "桌面项")下，并像这样编辑： 
    
    $HOME/.local/share/applications/telegramdesktop-no-scaling.desktop
    
    ...
    Exec=env -u QT_SCREEN_SCALE_FACTORS telegram-desktop -- %u
    ...

您可能需要[更新桌面项目数据库](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E5%88%B7%E6%96%B0%E6%A1%8C%E9%9D%A2%E9%A1%B9%E6%95%B0%E6%8D%AE%E5%BA%93> "桌面项")。 

###  音频后端

Telegram 使用 [OpenAL](<https://github.com/kcat/openal-soft>)，可以通过编辑此[配置文件](<https://github.com/kcat/openal-soft/blob/master/alsoftrc.sample>)（`~/.config/alsoft.conf`）或者通过[此处](<https://github.com/kcat/openal-soft/blob/master/docs/env-vars.txt>)列出的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")进行修改。 

如果使用了无效的音频后端导致声音故障，可以通过修改[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `ALSOFT_DRIVERS` 或者修改 OpenAL 配置文件 `[general]` 部分中的属性 `drivers` 来覆盖设置。比如 drivers 值为 `"pulse"` 时，系统将优先使用 pulseaudio, 失败则回滚到默认驱动程序。 

###  选择正确的摄像头

Telegram 版本 3.7.1 不允许切换用于视频会议的摄像头。如果要强制 telegram 使用其他摄像头, 可以禁用不需要的摄像头，参见 <https://askubuntu.com/a/166819> 。 

### Fcitx support for Qt 6 Telegram

Telegram-desktop 自 3.4.2-2 版本起已迁移至基于 Qt 6 构建。从旧版本升级的用户可能会发现 [Fcitx](<../zh-cn/Fcitx.html> "Fcitx") 输入法在此应用中停止工作。要恢复功能，请安装 [fcitx-qt6](<https://archlinux.org/packages/?name=fcitx-qt6>)包 软件包或 [fcitx-im](<https://archlinux.org/groups/x86_64/fcitx-im/>)包组 软件包组。若使用[Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5")输入框架，则应安装 [fcitx5-im](<https://archlinux.org/groups/x86_64/fcitx5-im/>)包组 软件包组。 

### Changing the default file browser

在未设置 `XDG_CURRENT_DESKTOP` 环境变量的环境中（如不运行桌面环境，即仅运行窗口管理器时），telegram-desktop 会退回到非常基本的文件浏览器。 使用上述变量，用户可以将默认浏览器更改为自己喜欢的、属于特定桌面环境的浏览器。 该变量的有效值可以在[这里](<../zh-cn/Xdg-utils.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "Xdg-utils")找到。 例如，使用 XFCE 项目中的[Thunar](<../zh-cn/Thunar.html> "Thunar")： 
    
    XDG_CURRENT_DESKTOP=XFCE telegram-desktop

###  Arch Linux 中文社区的 Telegram 群组和频道

  * [Arch Linux CN News](<https://t.me/archlinuxcn>) \- 翻译 Arch Linux 官方网站的最新消息，和社区内大家遇到的踩坑预警。
  * [#archlinux-cn](<https://t.me/archlinuxcn_group>) \- 同步到 IRC #archlinux-cn 的中文讨论。
  * [#archlinux-cn-offtopic](<https://t.me/archlinuxcn_offtopic>) \- 同步到 IRC #archlinux-cn-offtopic ，中文水群。

##  参见

  * [Arch Linux](<https://t.me/archlinuxgroup>) \- 讨论有关 Arch Linux 的一切内容的非官方群组。
  * [ArchWikiBot](<https://t.me/archewikibot>) \- Arch Linux Wiki 搜索机器人。
  * [Planet Arch Linux & News](<https://t.me/planetarch>) \- Channel with recent Planet Arch updates and Latest News in one place.
  * [Arch Linux: Recent package updates](<https://t.me/archlinux_updates>) \- Arch Linux 软件包更新通知频道。
  * [Arch Linux News](<https://t.me/archlinuxnews>) \- Arch 网站的新闻频道 _(2018 年起不再更新)_ 。
  * [Planet Arch](<https://t.me/archplanet>) \- Planet Arch 网站的文章频道 _(2018 年起不再更新)_ 。
