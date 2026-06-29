**翻译状态：**

  * 本文（或部分内容）译自 [Ly](<https://wiki.archlinux.org/title/Ly> "arch:Ly")，最近一次同步于 2026-04-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ly?diff=0&oldid=869455>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ly_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")

[Ly](<https://codeberg.org/fairyglade/ly>) 是一个轻量级的 TUI (类似ncurses) 显示管理器，适用于 Linux 和 BSD，设计时考虑了可移植性（例如，它不需要 systemd 即可运行）。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ly](<https://archlinux.org/packages/?name=ly>)包。对于 X server 支持，安装 [xorg-xauth](<https://archlinux.org/packages/?name=xorg-xauth>)包。 

###  依赖

为了获得完整的 _Ly_ 体验，建议[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [brightnessctl](<https://archlinux.org/packages/?name=brightnessctl>)包 和 [durdraw](<https://aur.archlinux.org/packages/durdraw/>)AUR，用于管理屏幕亮度设置和设置自定义动画。 

##  用法

要使 _Ly_ 在启动时运行，需要执行两个步骤。首先，确保[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `ly@tty _X_.service`，然后[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用") `getty@tty _X_.service`，其中 _X_ 代表 1 到 6 的数字。 

##  配置

系统配置文件在 `/etc/ly/config.ini`，用户配置文件在 `~/.config/ly`。 

##  参见

  * [Ly on Github](<https://github.com/fairyglade/ly>)
  * [emptty Display Manager](<https://github.com/tvrzna/emptty/>)
  * [Lemurs Display Manager](<https://github.com/coastalwhite/lemurs>)
