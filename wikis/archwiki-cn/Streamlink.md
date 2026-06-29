**翻译状态：**

  * 本文（或部分内容）译自 [Streamlink](<https://wiki.archlinux.org/title/Streamlink> "arch:Streamlink")，最近一次同步于 2025-08-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Streamlink?diff=0&oldid=842618>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Streamlink_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Streamlink](<https://github.com/streamlink/streamlink>) 是一个用 [Python](<../zh-cn/Python.html> "Python") 编写的命令行工具，可将各类服务的视频流传输至常见的视频播放器（如 [VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC")、[MPlayer](<../zh-cn/MPlayer.html> "MPlayer")、[mpv](<../zh-cn/Mpv.html> "Mpv")）。完整的播放器支持列表请参阅[播放器兼容性](<https://streamlink.github.io/players.html#player-compatibility>)。 

该项目是从已不再维护的 [Livestreamer](<https://github.com/chrippa/livestreamer>) 分支而来。 

Streamlink 基于插件系统构建，可轻松添加对新流媒体服务的支持。绝大多数主流流媒体平台均已兼容，包括 Dailymotion、Livestream、Twitch、UStream、YouTube Live、哔哩哔哩等。完整的插件列表请参阅[插件](<https://streamlink.github.io/plugins.html>)页面。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [streamlink](<https://archlinux.org/packages/?name=streamlink>)包 或其开发版本 [streamlink-git](<https://aur.archlinux.org/packages/streamlink-git/>)AUR。 

##  使用

该软件包提供了 `streamlink` 命令行工具，使用起来非常简单： 
    
    $ streamlink -p _播放器_ _url_ _stream_
    
  * `_播放器_`——所使用的媒体播放器的可执行文件名，例如 `vlc`。也可以指定完整路径，例如 `/usr/bin/vlc`。如果安装，默认使用 VLC。
  * `_url_`——流媒体的 URL 地址，HTTP(S) 的协议前缀（`http://`、`https://`）通常可以省略，具体取决于所用插件的实现方式。
  * `_stream_`——要播放的具体流，主要用于选择视频画质：`best` 表示最高画质，`worst` 表示最低画质，某些插件可能还支持其他画质选项。如果不提供此参数，则会输出所有当前可用流的列表。

例如： 
    
    $ streamlink -p mpv dailymotion.com/embed/video/x1b1h6o worst
    
有关可用选项的完整列表，请参阅 [streamlink(1)](<https://man.archlinux.org/man/streamlink.1>)。 

若要将视频流保存到本地硬盘： 
    
    $ streamlink -o ~/$current_time.m2t _url_ best,high
    
### Twitch

使用以下命令播放 Twitch 直播： 
    
    $ streamlink -p _播放器_ twitch.tv/_频道名_ _画质_
    
例如： 
    
    $ streamlink -p vlc twitch.tv/archlinux best
    
可用的画质选项可能（视原画质而定）包括：`audio_only`、`160p`（`worst`）、`360p`、`480p`、`720p60`、`1080p60`（`best`）。 

###  哔哩哔哩

使用以下命令播放哔哩哔哩直播： 
    
    $ streamlink -p _播放器_ live.bilibili.com/_房间号_ _画质_
    
例如： 
    
    $ streamlink -p vlc live.bilibili.com/22102223 best
    
可用的画质选项包括：`hls_alt`（`worst`）、`hls_alt2`、`hls`、`httpstream_alt` 和 `httpstream`（`best`）。 

##  另请参阅

  * [Streamlink 的 GitHub 仓库](<https://github.com/streamlink/streamlink>)
  * [Streamlink 官方文档](<https://streamlink.github.io/>)（英文）
