**翻译状态：**

  * 本文（或部分内容）译自 [Cmus](<https://wiki.archlinux.org/title/Cmus> "arch:Cmus")，最近一次同步于 2024-4-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cmus?diff=0&oldid=806158>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cmus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[cmus](<https://cmus.github.io/>) _(C* MUsic Player)_ 是一款小巧、快速且功能强大的控制台音频播放器，支持大多数主要音频格式。各种功能包括无缝播放、ReplayGain 支持、MP3 和 Ogg 流媒体、实时过滤、即时启动、可自定义的按键绑定和 vi 样式的默认按键绑定。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cmus](<https://archlinux.org/packages/?name=cmus>)包 软件包，或开发版的 [cmus-git](<https://aur.archlinux.org/packages/cmus-git/>)AUR 。 

有关可用的[编解码器](<../zh-cn/%E7%BC%96%E8%A7%A3%E7%A0%81%E5%99%A8%E4%B8%8E%E5%AE%B9%E5%99%A8.html> "Codecs")和输出插件，参见可选依赖项（可使用 `cmus --plugins` 列出已安装的插件）。 

###  将 cmus 与 ALSA 结合使用

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [alsa-lib](<https://archlinux.org/packages/?name=alsa-lib>)包 软件包。 

当用 [ALSA](<../zh-cn/ALSA.html> "ALSA") 使用 cmus 时，默认配置不允许播放音乐。在尝试启动 cmus 时，你可能会看到终端行一片空白，没有任何输出。要解决这个问题，请创建一个新的配置文件并设置以下变量： 
    
    ~/.config/cmus/rc
    
    set output_plugin=alsa
    set dsp.alsa.device=default
    set mixer.alsa.device=default
    set mixer.alsa.channel=Master

##  用法

参见[cmus(1)](<https://man.archlinux.org/man/cmus.1>), [cmus-tutorial(7)](<https://man.archlinux.org/man/cmus-tutorial.7>) 与 [cmus-remote(1)](<https://man.archlinux.org/man/cmus-remote.1>). 

##  配置

要配置 cmus，请参见[cmus(1)](<https://man.archlinux.org/man/cmus.1>)。 

###  遥控

cmus可以通过带有`cmus-remote`的unix套接字进行外部控制。这样就可以轻松地通过外部应用程序或键绑定来控制播放。 

此功能的一种用法是使用 XF86 键盘事件控制 CMUS 中的播放。如果 Cmus 未运行，则运行时以下脚本将在 xterm 终端中启动 Cmus，否则将切换播放/暂停： 
    
    #!/bin/sh
    
    if ! pgrep -x cmus ; then
      xterm -e cmus
    else
      cmus-remote -u
    fi

将上面的代码复制到文件中 `~/bin/cplay` 并使其[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。 

要在 [Openbox](<../zh-cn/Openbox.html> "Openbox") 中使用 cmus-remote，请参阅[Openbox#rc.xml](<../zh-cn/Openbox.html#rc.xml> "Openbox")。 

### JACK

要使 cmus 与 JACK 服务器一起工作，请在 cmus 中运行上述命令： 
    
    :set output_plugin=jack

##  音频记录

Cmus本身不支持音频记录，但有[第三方解决方案](<https://github.com/cmus/cmus/wiki/status-display-programs#audio-scrobbling-to-eg-lastfm-or-librefm>)。安装 [cmusfm](<https://aur.archlinux.org/packages/cmusfm/>)AUR 进行 Last.fm 或 Libre.fm 音频记录。对于初始配置，请运行 `cmusfm init` 并点击链接以执行身份验证。 

默认情况下，cmusfm 会拼凑到 Last.fm 服务。但是，可以通过修改配置文件 (`~/.config/cmus/cmusfm.conf`) 中的 **service-api-url** 和 **service-auth-url** 选项来更改此行为。之后，应该重新初始化 `cmusfm init` 以便使用新的 scrobbling 服务进行身份验证。为了将 Libre.fm 用作 音频记录 服务，应使用如下配置： 
    
    ~/.config/cmus/cmusfm.conf
    
    service-api-url = "https://libre.fm/2.0/"
    service-auth-url = "https://libre.fm/api/auth"
    
下一步是将 cmusfm 设置为 CMUS 的 _状态程序_ 。在主 cmus 窗口中执行命令 `:set status_display_program=cmusfm`

##  故障排除

###  添加后看不到曲目

如果您看不到刚刚添加的曲目，那可能是因为您没有安装 [ffmpeg](<https://archlinux.org/packages/?name=ffmpeg>)包 包。您可以看到可用的文件扩展名，用： 
    
    $ cmus --plugins
    
##  另请参阅

  * [Git存储库](<https://github.com/cmus/cmus>)
  * [网站](<https://cmus.github.io/>)
  * [用户提交的脚本](<https://github.com/cmus/cmus/wiki>)
