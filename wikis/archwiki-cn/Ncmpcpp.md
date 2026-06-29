**翻译状态：**

  * 本文（或部分内容）译自 [Ncmpcpp](<https://wiki.archlinux.org/title/Ncmpcpp> "arch:Ncmpcpp")，最近一次同步于 2025-10-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ncmpcpp?diff=0&oldid=844104>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ncmpcpp_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [MPD](<../zh-cn/MPD.html> "MPD")

[Ncmpcpp](<https://rybczak.net/ncmpcpp>) 是一个 [mpd](<../zh-cn/MPD.html> "Mpd") 客户端（与 [mopidy](<https://mopidy.com/>) 兼容），其 UI 与 _ncmpc_ 非常相似，但它提供了新的实用功能，例如：支持对音乐库的正则表达式搜索、对扩展的音频格式的支持、项目过滤、播放列表排序以及在本地音乐库上的文件系统浏览器。 

ncmpcpp/mpd 以客户端/服务器关系工作，因此您需要能在系统上运行 mpd 才能使用 ncmppp 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ncmpcpp](<https://archlinux.org/packages/?name=ncmpcpp>)包 软件包，或者开发版本 [ncmpcpp-git](<https://aur.archlinux.org/packages/ncmpcpp-git/>)AUR。 

##  基本配置

ncmpcpp 的 shell“GUI”是高度可定制的，可以根据自己的喜好编辑 `$XDG_CONFIG_HOME/ncmpcpp/config` 来定制。如果在安装后尚未创建 `$XDG_CONFIG_HOME/ncmpcpp/config`，只需复制示例配置，[修改所有者](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "文件权限与属性")并至少编辑以下三个配置选项： 

  * **mpd_host** \- 应指向 _mpd_ 所在的主机，如果在同一台计算机上，可以是“localhost”、“127.0.0.1”或“::1”。要使用密码连接，请设置为“ _password_ @_host_ ”
  * **mpd_port** \- _mpd_ 的默认值应为 “6600”
  * **mpd_music_dir** \- 应与 `mpd.conf` 中的“music_directory”中指定的路径值相同

如需灵感，可以参阅以下资源： 

  * `/usr/share/doc/ncmpcpp/config` 中的示例配置文件。
  * [分享您的 .ncmpcpp/config 与屏幕截图的论坛线程](<https://bbs.archlinux.org/viewtopic.php?id=66488>)

##  启用音频可视化

对于音频可视化，请在 `/etc/mpd.conf` 或 `~/.config/mpd/mpd.conf` 中添加以下几行来生成用于可视化的[快速傅里叶变换](<https://en.wikipedia.org/wiki/Fast_Fourier_transform> "wikipedia:Fast Fourier transform")数据： 
    
    audio_output {
        type                    "fifo"
        name                    "my_fifo"
        path                    "/tmp/mpd.fifo"
        format                  "44100:16:2"
    }
    
**注意：** 对于正常的音频输出，可能需要额外添加一个 `audio_output` 片段。具体细节请见[Music Player Daemon#配置音频](<../zh-cn/Music_Player_Daemon.html#%E9%85%8D%E7%BD%AE%E9%9F%B3%E9%A2%91> "Music Player Daemon")

下面的几行也需要被添加到 `$XDG_CONFIG_HOME/ncmpcpp/config` 中 
    
    visualizer_data_source = "/tmp/mpd.fifo"
    visualizer_output_name = "my_fifo"
    visualizer_in_stereo = "yes"
    visualizer_type = "spectrum"
    visualizer_look = "+|"
    
  * **visualizer_type** \- 将可视化设置为 `spectrum`/`ellipse`/`wave_filled` 分析仪或 `wave` 形式。
  * **visualizer_look** \- 设置可视化工具的外观（字符串长度必须恰好是 2 个字符：第一个用于 `wave`，第二个用于`spectrum`/`ellipse`/`wave_filled`）

**注意：** 如果遇到了同步问题，将 `mpd` 配置中 `buffer_time` 的值修改为 [100000 或更低](<https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/config>).

如果使用 [mopidy](<https://docs.mopidy.com/en/latest/installation/arch/>), 则可视化是由 [gstreamer 的 udpsink](<https://github.com/ncmpcpp/ncmpcpp/commit/fb886f687014e22b2fe1477da855be5201063ea8>) 来处理。修改 `mopidy.conf` 中的 `[audio]` 块中的 `output` 为： 
    
    output = tee name=t ! queue ! autoaudiosink t. ! queue ! audio/x-raw,rate=44100,channels=2,format=S16LE ! udpsink host=localhost port=5555
    
这会将音频数据转发到端口 `5555`。要使 `ncmpcpp` 从此端口读取数据，请相应地更改其 `visualizer_data_source`： 
    
    visualizer_data_source = "localhost:5555"
    
##  提示和技巧

###  重新映射快捷键

可以通过在 npmpcpp 中按 `F1` 来获得快捷键和其绑定的功能列表。只需将 `/usr/share/doc/ncmpcpp/bindings` 复制到 `$XDG_CONFIG_HOME/ncmpcpp/` 并对该文件进行编辑，即可重新映射任何默认快捷键。 

###  从文件名自动设置标签，反之亦然

在标签编辑器中可以选择一个包含音乐的目录，然后选择中间部分的 `Filename` 选项。这将打开一个小窗口，其中包含两个选项：`Get Tags from Filename` 和 `Rename files`。 如果选择`Get Tags From Filename`，则会显示一个包含两个窗格的弹出窗口。在左侧的窗格中可以输入如何从文件名中提取所选信息的模式，还可以选择 `Preview` 来预览结果。而在右侧的窗格中可以看到包含所有可能用于提取信息的关键字的图例。 

一个简单的示例是模式：`%a - %t`。如果音乐文件是根据（艺术家 - 标题）的格式命名的，则此模式将提取对应信息并为文件设置标签。 

另一个选项 `Rename Files` 则完全相反。它从音频文件中获取标签并根据标签创建文件名。 

###  歌曲更改时通知

可以在 `execute_on_song_change` 命令中使用 _notify-send_ 来在歌曲更改时（以及 ncmpcpp 启动时）发出通知。这取决于是否安装并配置了[桌面通知程序](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html> "桌面通知程序")。例如： 
    
    execute_on_song_change = notify-send "Now Playing" "$(mpc --format '%title% \n%artist% - %album%' current)"
    
####  带专辑封面的通知

可以使用此脚本使得歌曲更改的通知能带有当前播放歌曲的专辑封面。默认情况下，专辑封面的预览文件将存储在 `$XDG_CONFIG_HOME/ncmpcpp/previews` 中并缩放到 128x128。预览文件名是以 base64 编码的专辑名称，因此不应保存重复的预览。 

假设 `~/.local/bin` 在 `$PATH` 中，请[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:阅读")（并使其[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:阅读")） 
    
    ~/.local/bin/songinfo
    
    #!/bin/sh
    
    music_dir="$HOME/Music"
    previewdir="$XDG_CONFIG_HOME/ncmpcpp/previews"
    filename="$(mpc --format "$music_dir"/%file% current)"
    previewname="$previewdir/$(mpc --format %album% current | base64).png"
    
    [ -e "$previewname" ] || ffmpeg -y -i "$filename" -an -vf scale=128:128 "$previewname" > /dev/null 2>&1
    
    notify-send -r 27072 "Now Playing" "$(mpc --format '%title% \n%artist% - %album%' current)" -i "$previewname"
    
并将下内容添加到 ncmpcpp 配置中： 
    
    execute_on_song_change = songinfo
    
##  另见

[dotshare.it 配置](<http://dotshare.it/category/mpd/ncmpcpp/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2025-08-16 ⓘ]
