**翻译状态：**

  * 本文（或部分内容）译自 [Discord](<https://wiki.archlinux.org/title/Discord> "arch:Discord")，最近一次同步于 2020-09-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Discord?diff=0&oldid=635346>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Discord_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Discord 是一款专有的跨平台多合一语音和文本聊天应用程序。它是专门为游戏玩家量身定制的。但是，许多开源社区也有[官方的 Discord 服务器](<https://discord.com/open-source>)。可以通过 Web 浏览器或通过 [Electron](<https://github.com/electron/electron>) 制作的桌面应用程序使用 Discord。 

##  安装

您可以使用以下软件包之一来安装 Discord 的桌面应用程序： 

###  图形客户端

[官方应用](<https://discord.com/>)： 

  * 稳定版：[discord](<https://archlinux.org/packages/?name=discord>)包
  * 测试版：[discord-ptb](<https://aur.archlinux.org/packages/discord-ptb/>)AUR
  * 每夜构建版：[discord-canary](<https://aur.archlinux.org/packages/discord-canary/>)AUR

第三方客户端： 

  * [ripcord](<https://aur.archlinux.org/packages/ripcord/>)AUR，有关更多信息，请参阅 [Ripcord](</wzh/index.php?title=Ripcord&action=edit&redlink=1> "Ripcord（页面不存在）") 文章

###  命令行客户端

尽管目前只有少数几个打包在 AUR 上，但在 GitHub 之类的地方（例如 [Discline](<https://github.com/MitchWeaver/Discline>) 或 [terminal-discord](<https://github.com/xynxynxyn/terminal-discord>)）上托管着更多基于 CLI 的第三方客户端。 

###  聊天客户端插件

  * 通过使用 [purple-discord-git](<https://aur.archlinux.org/packages/purple-discord-git/>)AUR，您可以在基于 [libpurple](<https://archlinux.org/packages/?name=libpurple>)包 的图形或终端聊天软件（例如 [Pidgin](<../zh-cn/Pidgin.html> "Pidgin")）上使用 Discord。
  * 通过使用 [bitlbee-discord-git](<https://aur.archlinux.org/packages/bitlbee-discord-git/>)AUR，您可以通过 [Bitlbee](</wzh/index.php?title=Bitlbee&action=edit&redlink=1> "Bitlbee（页面不存在）") 使用 Discord。

###  自定义 CSS 和插件

通过 [betterdiscord-git](<https://aur.archlinux.org/packages/betterdiscord-git/>)AUR 软件包，可以将 Discord 修改为使用自定义 CSS 和插件。 

请注意，使用这些软件包或修改 Discord 客户端的任何软件包或应用程序均违反 Discord 的服务条款，并可能会封禁您的帐户。使用这些或类似软件包时，您将承担全部责任。 

##  故障排除

  * 如果您在进行语音聊天时遇到啪啪作响的声音，则应尝试执行此处概述的步骤：[PulseAudio/Troubleshooting](</wzh/index.php?title=PulseAudio/Troubleshooting&action=edit&redlink=1> "PulseAudio/Troubleshooting（页面不存在）")

  * 如果不能在多显示器设置上共享单个显示器，则应尝试使用 [mon2cam-git](<https://aur.archlinux.org/packages/mon2cam-git/>)AUR 作为此错误的解决方法：[Discord Trello](<https://trello.com/c/SJEH2Fsi/41-multiple-monitors-are-shown-as-one-in-screenshare>)

  * 当使用 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 版本的 Discord 时，Rich Presence 将无法开箱即用。要使其正常工作，必须创建从 `$XDG_RUNTIME_DIR/discord-ipc-0` 到 `$XDG_RUNTIME_DIR/app/com.discordapp.Discord/discord-ipc-0` 的符号链接。要为当前用户会话创建符号链接，请运行：
        
        $ ln -sf {app/com.discordapp.Discord,$XDG_RUNTIME_DIR}/discord-ipc-0

    要自动创建符号链接，可以通过在 `~/.config/user-tmpfiles.d/` 中的扩展名为 `.conf` 的文件中添加以下行来使用 [systemd-tmpfiles](<../zh-cn/Systemd.html#systemd-tmpfiles_-_%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd-tmpfiles")：
    
    L %t/discord-ipc-0 - - - - app/com.discordapp.Discord/discord-ipc-0

**提示：** 可以通过 `--start-minimized` 参数最小化 Discord。
