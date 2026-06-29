**翻译状态：**

  * 本文（或部分内容）译自 [Ktorrent](<https://wiki.archlinux.org/title/Ktorrent> "arch:Ktorrent")，最近一次同步于 2024-8-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ktorrent?diff=0&oldid=813295>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ktorrent_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[KTorrent](<https://www.kde.org/applications/internet/ktorrent/>) 是 [KDE](<../zh-cn/KDE.html> "KDE") 的 [BitTorrent](<../zh-cn/Category:BitTorrent.html> "BitTorrent") 客户端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ktorrent](<https://archlinux.org/packages/?name=ktorrent>)包 软件包。 

##  问题解决

###  无法看到底部面板的某些工具

要显示 files、seeders、leechers 和 current trackers 的任何信息，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")可选依赖 [geoip](<https://archlinux.org/packages/?name=geoip>)包。建议在设置中启用 DHT，以避免速度过慢和 seeders 数量过少。 

##  在命令行中用脚本管理

虽然 KTorrent 仅是一个 GUI 应用程序，但是幸好它有一个 DBUS 接口，因此您可以使用脚本在命令行（即从 SSH）中对其进行管理。详情请参见 [linuxquestions 论坛回答](<https://www.linuxquestions.org/questions/linux-software-2/terminal-commands-for-ktorrent-4175441715/#post4851070>)。 
