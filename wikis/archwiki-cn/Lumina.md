**翻译状态：**

  * 本文（或部分内容）译自 [Lumina](<https://wiki.archlinux.org/title/Lumina> "arch:Lumina")，最近一次同步于 2020-05-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lumina?diff=0&oldid=615203>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lumina_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [ZFS](<../zh-cn/ZFS.html> "ZFS")
  * [Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox")
  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")

**警告：** Lumina DE 主要针对 FreeBSD，而不是 Linux。

[Lumina Desktop Environment](<https://lumina-desktop.org/>)（简称 Lumina）是一种轻型，符合 XDG，BSD 许可的桌面环境，其重点在于简化完成工作的能力，同时最大程度地减少系统开销。 从版本 0.8.0+ 开始，它需要 Qt 5，Fluxbox 窗口管理器，并使用少量 X 实用程序来执行各种任务，例如 numlockx 和 xscreensaver。 

Lumina 的功能包括： 

  * 很少的系统开销。
  * 智能的“favorites”系统，用于创建应用程序，文件和目录的快捷方式。
  * 通过“ Insight”文件管理器进行 [ZFS](<../zh-cn/ZFS.html> "ZFS") 文件还原功能。
  * 桌面系统是基于插件的，类似于 Android 或其他现代操作系统。
  * 可以轻松访问特定于操作系统的功能，例如屏幕亮度，音量和电池状态。

##  安装

从 AUR 安装 [lumina-desktop](<https://aur.archlinux.org/packages/lumina-desktop/>)AUR 或 [lumina-desktop-git](<https://aur.archlinux.org/packages/lumina-desktop-git/>)AUR。 

##  启动 Lumina 桌面环境

###  通过 .xinitrc 启动
    
     ~/.xinitrc
    
    exec start-lumina-desktop
    
有关信息，请访问 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") wiki 页面。 

##  报告错误

错误应报告到 [GitHub](<https://github.com/pcbsd/lumina>) 上的 Lumina 存储库。 
