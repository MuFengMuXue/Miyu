**翻译状态：**

  * 本文（或部分内容）译自 [Quod Libet](<https://wiki.archlinux.org/title/Quod_Libet> "arch:Quod Libet")，最近一次同步于 2024-4-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Quod_Libet?diff=0&oldid=806262>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Quod_Libet_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Quod Libet](<https://quodlibet.readthedocs.io/>)是一款用 [Python](<../zh-cn/Python.html> "Python") 编写并基于 [GTK](<../zh-cn/GTK.html> "GTK") 的音乐播放器，可使用本机或用户插件进行扩展，并支持使用 [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") 作为后端的多种音频格式。它支持 [ReplayGain](<https://en.wikipedia.org/wiki/ReplayGain> "wikipedia:ReplayGain")、读写标签、显示专辑封面和歌词、基于正则表达式过滤库等。 

Quod Libet 项目提供 3 个命令： 

[quodlibet(1)](<https://man.archlinux.org/man/quodlibet.1>)
    The player and library manager, supporting a CLI.
[exfalso(1)](<https://man.archlinux.org/man/exfalso.1>)
    The graphical tag manager.
[operon(1)](<https://man.archlinux.org/man/operon.1>)
    The command-line tag manager.

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[quodlibet](<https://archlinux.org/packages/?name=quodlibet>)包软件包。 

###  扩展解码功能

Quod Libet 可以通过 [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") 从基于 [Libav-based](<../zh-cn/FFmpeg.html> "FFmpeg") 的编解码器中受益（ _例如_ ，解码 [Monkey 的音频 （APE）](<https://en.wikipedia.org/wiki/Monkey%27s_Audio> "wikipedia:Monkey's Audio")文件。要启用此功能，请安装 [gst-libav](<https://archlinux.org/packages/?name=gst-libav>)包 软件包并重新启动音频播放器。 

###  扩展插件列表

Quod Libet 可以从一些 [GStreamer的插件](<https://gstreamer.freedesktop.org/documentation/plugins_doc.html?gi-language=c>)中受益（ _例如_ ，用于计算 [ReplayGain](<https://en.wikipedia.org/wiki/ReplayGain> "wikipedia:ReplayGain") 信息）。要使它们在 Quod Libet 的插件列表中可用，请安装 [gst-plugins-good](<https://archlinux.org/packages/?name=gst-plugins-good>)包软件包并重新启动音频播放器。 

##  配置

###  配置播放器核心

在菜单中，转到 _文件_ ，然后转到 _首选项_ 。在这里，您可以配置库路径、启用 ReplayGain 并配置播放器布局。 

###  启用插件

播放器的默认首选项并非详尽无遗。更高级的配置是通过插件完成的。要启用它们，请在菜单中转到 _文件 >插件_，然后启用所需的插件。 

以下是有趣的插件列表： 

Alternative progress bar
    在窗口顶部显示进度条。
Waveform search bar
    显示波形进度条，而不是简单的条形。
Change theme
    配置界面主题。
ReplayGain
    在上下文菜单中添加一个按钮，以计算所选文件的 ReplayGain 信息。
Information overlay
    在标题更改期间添加 OSD。
D-BUS MPRIS support
    通过D-BUS添加MPRIS支持，允许使用键盘多媒体键控制媒体播放器。
Display lyrics
    在显示屏右侧添加一个面板以显示嵌入的歌词。

##  插件

### ReplayGain

默认情况下，[ReplayGain](<https://en.wikipedia.org/wiki/ReplayGain> "wikipedia:ReplayGain") 在 Quod Libet 上处于禁用状态。您必须在首选项中启用它，以便在运行时根据 ReplayGain 标签调整曲目的音量。 

Quod Libet 能够计算 ReplayGain 信息并将其存储在音频文件的标签中。它依赖于 [GStreamer 的 rganalysis](<https://gstreamer.freedesktop.org/documentation/replaygain/rganalysis.html?gi-language=c>) 插件。为此，请执行以下操作： 

  * 确保 GStreamer 的插件是通过 [gst-plugins-good](<https://archlinux.org/packages/?name=gst-plugins-good>)包 软件包安装的。
  * 启用 ReplayGain 插件，右键单击文件，转到 _Plugins_ 并单击 _ReplayGain_ 。

###  外部控制

Quod Libet 可以通过 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 使用 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") 以编程方式进行控制。为此，请启用 _D-BUS MPRIS support_ 插件。它允许使用多媒体键和终端进行控制。 

下面演示了使用终端进行播放器控制的一些示例。 

将播放音量设置为 50%
    
    $ dbus-send --dest=org.mpris.MediaPlayer2.quodlibet --print-reply /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Set string:org.mpris.MediaPlayer2.Player string:Volume variant:double:0.5
    
控制播放操作：
    
    $ dbus-send --dest=org.mpris.MediaPlayer2.quodlibet --print-reply /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next
    
您可以使用以下操作之一，而不是 _Next_ ： _Pause_ 、 _Play'、_ Previous _、_ Stop _。_

###  媒体服务器

Quod Libet 可以使用 [Music Player Daemon](<../zh-cn/Music_Player_Daemon.html> "Music Player Daemon") 或 [Rygel](</wzh/index.php?title=Rygel&action=edit&redlink=1> "Rygel（页面不存在）") 作为后端充当媒体服务器。要选择和使用其中之一，请在首选项中启用相应的插件。 

##  疑难解答

###  多媒体键不起作用

多媒体键使用 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") 接口工作。必须在 Quod Libet 的插件中启用此接口才能使它们正常工作。 

###  标题更改时界面冻结

启用有问题的插件或太多正常的插件有时会导致性能不佳。禁用插件，直到冻结消失，以便您可以识别有故障的插件。例如，众所周知， _波形搜索栏_ 会导致低端系统出现一些滞后。 

##  参见

  * [Wikipedia 页面](<https://en.wikipedia.org/wiki/Quod_Libet_\(software\)> "wikipedia:Quod Libet \(software\)")
  * [GitHub 存储库](<https://github.com/quodlibet/quodlibet/>)
  * [官方网站](<https://quodlibet.readthedocs.io/>)
