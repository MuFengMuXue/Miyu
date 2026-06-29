**翻译状态：**

  * 本文（或部分内容）译自 [MPRIS](<https://wiki.archlinux.org/title/MPRIS> "arch:MPRIS")，最近一次同步于 2024-4-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/MPRIS?diff=0&oldid=805916>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MPRIS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MPRIS](<https://specifications.freedesktop.org/mpris-spec/latest/>) (媒体播放器远程接口规范) 是一个标准的 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 接口，旨在提供用于控制媒体播放器的通用编程API。 

它为兼容媒体播放器的发现、查询和基本播放控制提供了一种机制，还提供了一个曲目列表界面，用于为活动媒体项目添加上下文。 

##  支持的客户端

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 您可以查看[您选择的播放器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html> "应用程序列表/多媒体")并检查它是否支持带有 playerctl 工具的 MPRIS。如果是这样，请将其添加到以下列表中。 (在 [Talk:MPRIS](<../zh-cn/Talk:MPRIS.html>) 中讨论)

  * [Audacious](<../zh-cn/Audacious.html> "Audacious")
  * [celluloid](<https://archlinux.org/packages/?name=celluloid>)包
  * [Chromium](<../zh-cn/Chromium.html> "Chromium")
  * [clementine](<https://aur.archlinux.org/packages/clementine/>)AUR
  * [cmus](<../zh-cn/Cmus.html> "Cmus")
  * [deadbeef](<https://aur.archlinux.org/packages/deadbeef/>)AUR (using [deadbeef-mpris2-plugin](<https://aur.archlinux.org/packages/deadbeef-mpris2-plugin/>)AUR)
  * [dragon](<https://archlinux.org/packages/?name=dragon>)包
  * [Firefox](<../zh-cn/Firefox.html> "Firefox")
  * [gmusicbrowser](<https://aur.archlinux.org/packages/gmusicbrowser/>)AUR
  * [guayadeque](<https://aur.archlinux.org/packages/guayadeque/>)AUR
  * [KDE#KDE Connect](<../zh-cn/KDE.html#KDE_Connect> "KDE")
  * [mpv#mpv-mpris](<../zh-cn/Mpv.html#mpv-mpris> "Mpv")
  * [MPD/提示与技巧#MPRIS 支持](<../zh-cn/MPD/%E6%8F%90%E7%A4%BA%E4%B8%8E%E6%8A%80%E5%B7%A7.html#MPRIS_%E6%94%AF%E6%8C%81> "MPD/提示与技巧")
  * [ncspot](<https://archlinux.org/packages/?name=ncspot>)包
  * [Quod Libet](<../zh-cn/Quod_Libet.html> "Quod Libet")
  * [rage](<https://archlinux.org/packages/?name=rage>)包
  * [resonance](<https://aur.archlinux.org/packages/resonance/>)AUR
  * [smf-dsp-git](<https://aur.archlinux.org/packages/smf-dsp-git/>)AUR
  * [Spotify#MPRIS](</wzh/index.php?title=Spotify&action=edit&redlink=1> "Spotify（页面不存在）")
  * [spotube-bin](<https://aur.archlinux.org/packages/spotube-bin/>)AUR
  * [Telegram](<../zh-cn/Telegram.html> "Telegram")
  * [tidal-hifi-bin](<https://aur.archlinux.org/packages/tidal-hifi-bin/>)AUR
  * [VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC")
  * [brave-nightly-bin](<https://aur.archlinux.org/packages/brave-nightly-bin/>)AUR

##  控制工具

**提示：** 为常用控制命令和多媒体键，（如`XF86AudioPlay`, `XF86AudioStop`, `XF86AudioPrev` 与 `XF86AudioNext`）创建[键绑定](<../zh-cn/%E5%BF%AB%E6%8D%B7%E9%94%AE.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%BF%AB%E6%8D%B7%E9%94%AE> "键绑定")

### Playerctl

[playerctl](<https://archlinux.org/packages/?name=playerctl>)包 工具提供了一个命令行工具，用于将命令发送到 MPRIS 客户端。最常见的命令是 `play-pause`, `next` 与 `previous`: 
    
    $ playerctl play-pause
    $ playerctl next
    $ playerctl previous
    
_playerctl_ 会向它找到的第一个播放器发送命令。要手动选择播放器，请使用 `--player` 选项，例如 `--player=vlc` 。为了更好地实现自动化，playerctl 附带了一个守护进程，它能跟踪媒体播放器的活动，并将命令发送给最近有活动的播放器。你可以使用以下命令将它转入后台： 
    
    $ playerctld daemon
    
为了在登录时启动 _playerctld_ ，您可以创建以下 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")服务 
    
    ~/.config/systemd/user/playerctld.service
    
    [Unit]
    Description=Keep track of media player activity
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/playerctld daemon
    
    [Install]
    WantedBy=default.target

然后，您应该在[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")带有`--user`标志的服务之前执行[daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") 。 

**提示：** 可以安装 [playerctld-systemd-unit](<https://aur.archlinux.org/packages/playerctld-systemd-unit/>)AUR 软件包，而不是手动创建服务。

此外， _playerctld_ 还能够更改 _活动_ 播放器，这在您同时拥有多个媒体流时非常有用： 

要切换到下一个播放器，请使用： 
    
    $ playerctld shift
    
要切换到上一个播放器，请使用： 
    
    $ playerctld unshift
    
### mpris-player-control

[mpris_player_control](<https://gitlab.com/axdsop/nix-dotfiles/tree/master/Configs/polybar/scripts/mpris_player>) 是一个 shell 脚本，它集成了 `dbus-send` 和 `pactl` 以控制 MPRIS 客户端。它支持播放、暂停、暂停播放和停止操作，以及 [Spotify](</wzh/index.php?title=Spotify&action=edit&redlink=1> "Spotify（页面不存在）") 的音量控制（静音/静音/上/下）。 

运行 `mpris_player_control -h` 以显示基本脚本用法。 

### D-Bus

上述方法的替代方法是手动使用 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus")，默认情况下它应该可用，因为它是 [systemd](<../zh-cn/Systemd.html> "Systemd") 的依赖项。 

例如，可以使用以下命令通过支持的 [Methods](<https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html#methods>) 来控制 [Spotify](</wzh/index.php?title=Spotify&action=edit&redlink=1> "Spotify（页面不存在）")： 
    
    $ dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player._Method_
    
类似地，使用 [busctl(1)](<https://man.archlinux.org/man/busctl.1>): 
    
    $ busctl --user call org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player _Method_
    
##  蓝牙

来自蓝牙耳机和类似设备的媒体控制可能会转发到 MPRIS。 

**注意：** 某些耳机（例如索尼 WH-1000XM3）提供 AVRCP 接口。对于这些类型，不需要 _mpris-proxy_ 。只需确保已为媒体键设置了[键绑定](<../zh-cn/%E5%BF%AB%E6%8D%B7%E9%94%AE.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%BF%AB%E6%8D%B7%E9%94%AE> "键绑定")即可。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [bluez-utils](<https://archlinux.org/packages/?name=bluez-utils>)包 软件包并运行 `mpris-proxy`。为了在后台和/或系统启动时启动 _mpris-proxy_ ，您可以创建一个 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")服务： 
    
    ~/.config/systemd/user/mpris-proxy.service
    
    [Unit]
    Description=Forward bluetooth media controls to MPRIS
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/mpris-proxy
    
    [Install]
    WantedBy=default.target

然后，在[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")带有`--user` 标志的服务之前执行[daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")。 

**提示：** 可以安装 [mpris-proxy-service](<https://aur.archlinux.org/packages/mpris-proxy-service/>)AUR 软件包，而不是手动创建服务。
