**翻译状态：**

  * 本文（或部分内容）译自 [Rosegarden](<https://wiki.archlinux.org/title/Rosegarden> "arch:Rosegarden")，最近一次同步于 2024-10-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rosegarden?diff=0&oldid=817741>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rosegarden_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[Rosegarden](<https://www.rosegardenmusic.com/>)** 是一个用 Qt 编写的数字音频工作站程序。它可用作音频和 MIDI 音序器、乐谱编写器以及音乐创作和编辑工具。它旨在成为 Cubase 等应用程序的自由替代品。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rosegarden](<https://archlinux.org/packages/?name=rosegarden>)包 软件包。 请务必先安装 [MIDI](<../zh-cn/MIDI.html> "MIDI") 设置。 

##  配置

###  自定义键盘快捷键

通过编辑一组 XML 配置文件，可以自定义 rosegarden 中的键盘快捷键。第一步是下载与源代码打包在一起的默认配置文件，并将其放置在 `~/.local/share/rosegarden/rc` 中。一种简单的方法是运行 
    
    $ cd ~/.local/share/rosegarden
    $ svn co <http://svn.code.sf.net/p/rosegarden/code/trunk/rosegarden/data/rc>
    
将从源代码的开发分支获取配置文件。 

**注意：** 上述步骤是从 Rosegarden 的开发分支获取配置文件，开发分支可能与稳定版不兼容。如有需要，可在稳定版源代码压缩包中的 `data/rc` 目录下找到 `rc`。

然后，可以通过编辑 `~/.local/share/rosegarden/rc` 中的相应文件来设置或修改键盘快捷键。例如，要将 `Space` 键映射到播放/暂停，请编辑 `rosegardenmainwindow.rc` 中的以下几行代码 
    
    ~/.local/share/rosegarden/rc/rosegardenmainwindow.rc
    
    <Action name="play" text="&Play" icon="transport-play" shortcut="Ctrl+Enter, Enter, Media Play, Ctrl+Return, Space" shortcut-context="application" />
    <Action name="recordtoggle" text="P&unch in Record" icon="transport-record" shortcut="" shortcut-context="application" />

##  用法

###  与 Timidity 和 Pulseaudio 一起使用

在启动 Rosegarden 之前，以[守护进程](<../zh-cn/Timidity++.html#%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E6%A8%A1%E5%BC%8F> "Timidity++")模式启动 [Timidity++](<../zh-cn/Timidity++.html> "Timidity++")： 
    
    $ timidity -iA
    
这样，Rosegarden 就不会启动 [jackd](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）")，你仍然可以听到其他正在运行的应用程序发出的声音。 

##  参见

  * [专业音频](<../zh-cn/%E4%B8%93%E4%B8%9A%E9%9F%B3%E9%A2%91.html> "专业音频")
