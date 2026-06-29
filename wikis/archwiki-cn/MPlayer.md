**翻译状态：**

  * 本文（或部分内容）译自 [MPlayer](<https://wiki.archlinux.org/title/MPlayer> "arch:MPlayer")，最近一次同步于 2021-03-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/MPlayer?diff=0&oldid=654962>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MPlayer_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [mpv](<../zh-cn/Mpv.html> "Mpv")

[MPlayer](<https://mplayerhq.hu>) 是 GNU/Linux 下非常流行的影音播放器，支持绝大多数视频/音频文件格式，非常通用。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [mplayer](<https://archlinux.org/packages/?name=mplayer>)包 或它的开发版本 [mplayer-svn](<https://aur.archlinux.org/packages/mplayer-svn/>)AUR 。 

定制版： 

  * **MPlayer-VAAPI** — 支持 VAAPI 的版本

     <http://gitorious.org/vaapi/mplayer>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-21 ⓘ] || [mplayer-vaapi](<https://aur.archlinux.org/packages/mplayer-vaapi/>)AUR

  * **MPlayer2** — MPlayer 的分支

     <https://github.com/nezumisama/mplayer2> || [mplayer2](<https://aur.archlinux.org/packages/mplayer2/>)AUR

**注意：** _mplayer2_ 的开发已经停止，推荐使用 [mpv](<../zh-cn/Mpv.html> "Mpv")，mpv 更注重速度和开发质量，尽管它对老旧设备兼容性差。使用前请注意一下它们的 [差异](<https://github.com/mpv-player/mpv/blob/master/DOCS/mplayer-changes.rst>)。

###  图形前端

参考 [List of applications/Multimedia#MPlayer-based](<../zh-cn/List_of_applications/Multimedia.html#MPlayer-based> "List of applications/Multimedia"). 

##  配置

系统全局配置文件位于 `/etc/mplayer/`，用户配置文件位于 `~/.mplayer/`。 

`/etc/mplayer/` 下默认包含： 

  * `codecs.conf` \- 解码器配置文件。
  * `example.conf` \- mplayer.conf 不会在安装时自动创建，这是其示例文件。
  * `input.conf` \- 快捷键配置文件。

`~/.mplayer/` 下默认包含一个 _config_ 文件。 

参考 [MPlayer 配置示例](<https://mplayerhq.hu/DOCS/man/en/mplayer.1.html#CONFIGURATION%20FILES>)和 [mplayer(1)](<https://man.archlinux.org/man/mplayer.1>)。 

###  按键绑定

系统按键绑定通过 `/etc/mplayer/input.conf` 配置，个人按键绑定通过 `~/.mplayer/input.conf` 配置。完整的键盘快捷键列表请阅读 [mplayer(1)](<https://man.archlinux.org/man/mplayer.1>)。 

参阅：[XF86 键盘符号](<https://wiki.linuxquestions.org/wiki/XF86_keyboard_symbols>)

##  提示与技巧

###  硬件加速

参考[硬件视频加速](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration")。 

####  启用 VDPAU

将下列内容加入前面提到过的配置文件（全局或用户配置文件均可）： 
    
    vo=vdpau,
    vc=ffmpeg12vdpau,ffwmv3vdpau,ffvc1vdpau,ffh264vdpau,ffodivxvdpau,
    
**注意：**

  * 最后面的逗号很重要！如果找不到指定的驱动程序和编解码器，它们会告诉 MPlayer 使用其他驱动程序和编解码器。
  * `-vo` 选项选择 VDPAU 视频输出驱动, `-vc` 选项选择 VDPAU 视频解码器。

**警告：** 只有最新型号的显卡支持 ffodivxvdpau。如果你的不支持，可以删除。详情请查阅 [Hardware video acceleration#NVIDIA](<../zh-cn/Hardware_video_acceleration.html#NVIDIA> "Hardware video acceleration")。

####  启用 VA-API

这需要 AUR 中的 [mplayer-vaapi](<https://aur.archlinux.org/packages/mplayer-vaapi/>)AUR。 
    
    $ mplayer -vo vaapi -va vaapi _foobar.mpeg_

  * **-vo** \- Select vaapi video output driver
  * **-va** \- Select vaapi video decoder driver

基于 MPlayer 的播放器： 

  * [gnome-mplayer](<https://archlinux.org/packages/?name=gnome-mplayer>)包: 要启用硬件加速: _Edit > Preferences > Player_, 然后设置 Video Output 为 `vaapi`。
  * [smplayer](<https://archlinux.org/packages/?name=smplayer>)包: 要启用硬件加速: _Options > Preferences > General > Video_, 然后设置 Output driver 为 `vaapi`。

###  Radeon 显卡启用半透明视频混合显示

为了在 X 中获得半透明视频效果，你需要在 MPlayer 中启用视频纹理: 
    
    $ mplayer -vo xv:adaptor=1 _file_
    
或者在 `~/.mplayer/config` 中添加一行: 
    
    vo=xv:adaptor=1
    
你可以使用 `xvinfo` 命令检查你的显卡支持哪种视频模式。 

###  播放流媒体文件

要播放流媒体（如 ASX 链接)，使用以下命令： 
    
    $ mplayer -playlist link-to-stream.asx 
    
必须使用 `-playlist` 参数，因为这些文件是流媒体列表，而非影音文件。 

###  播放 DVD

要使用 MPlayer 播放 DVD： 
    
    $ mplayer dvd://_N_
    
其中 _N_ 想要播放的标题号。 如果不确定就从 1 开始。 要从特定的一章开始请使用 '-chapter' 标志。 例如，添加 '-chapter 5' 到命令会从标题的第 5 章开始播放。 

Mplayer 默认检查 `/dev/dvd`。 在命令行中添加 `dvd-device` 选项或者在 `~/.mplayer/config` 中使用 `dvd-device` 变量可以告诉它使用 `/dev/sr0`。 

要播放一个 DVD 镜像文件： 
    
    $ mplayer -dvd-device movie.iso dvd://_N_
    
启用 DVD 菜单请使用: 
    
    $ mplayer dvdnav://
    
**注意：** 使用方向键导航， `Enter` 键选择。

启用鼠标支持请使用： 
    
    $ mplayer -mouse-movements dvdnav://
    
要找到音频语言，以 `-v` 启动 MPlayer 可以切换到音频输出 ID。用 `-aid _audio_id_` 来选择一个音频 ID。通过编辑 `~/.mplayer/config` 并添加 `alang=en` 这一行可以将英语设为默认音频。 

用 MPlayer 时，DVD 音量可能会被设置得比较低。要提高最大音量到 400%，请使用 `softvol=yes` 和 `softvol-max=400`。初始音量默认为软件音量的 100%，全局混合水平保持不变。使用 `9` 和 `0` 可以在 0 和 400% 之间调节音量。 
    
    alang=en
    softvol=yes
    softvol-max=400
    
#### DVB-T Streaming

更多信息参见 [DVB-T](</wzh/index.php?title=DVB-T&action=edit&redlink=1> "DVB-T（页面不存在）")。 

###  JACK 支持

要使 MPlayer 将其音频直接输出到 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）") 作为默认行为，编辑 `~/.mplayer/config` 并添加： 
    
    ao=jack
    
如果你现在没有运行 JACK, 你可以通过从命令行唤起 MPlayer，来让 MPlayer 根据需要输出到 JACK, 如： 
    
    $ mplayer -ao jack _path/to/file_
    
###  高级字幕

要让 ass 或者 ssa 格式字幕正常展示，你需要修改 `~/.mplayer/config` 添加： 
    
    ass=true
    
或者添加 `-ass` 到命令行: 
    
    $ mplayer -ass _path/to/subtitledVideo.mkv_
    
需要启用此标志的一个可能指示是：您的字幕中是否出现数字。这是由被解释为要显示的东西的定位信息引起的。Mplayer 也会抱怨字幕太长或太多行。 

启用 `ass` 也会同时启用任何嵌入字体。 根据 MPlayer 的手册，如果 [fontconfig](<https://archlinux.org/packages/?name=fontconfig>)包 的版本号大于等于 2.4.2，不需添加 `embeddedfonts=true`。 当没有嵌入字体的时候，fontconfig 也会被用来选择使用哪个字体。这可能会导致使用的字体与 OSD 字幕渲染器的不同。 

###  网络电台

下面是一个脚本示例，用于轻松启动/停止播放预定义电台。 [[1]](<https://web.archive.org/web/20170130092907/http://www.linuxforums.org/forum/miscellaneous/199396-mplayer-flash.html#post941062>)
    
    #!/bin/bash
    XX="X"$1;
    PLAYIT='mplayer  -loop 0 -playlist http://*.*.*.*:8000/listen.pls';
    
    if [ "$XX" == "Xstop" ]; then
      killall mplayer;
    else
      if [ 'EX' == 'EX'"$(pidof mplayer)" ]; then
        if [ "$UID" -ne 0 ]; then 
          nohup $PLAYIT &> /dev/null & disown;
        else 
          echo The "root" user is not allowed to run this script.
        fi
      else
        echo mplayer is already running by user: $(ps -eo user,comm | grep -i "mplayer"$ | sed 's/ mplayer/,/m') | sed "s/ ,$/./m";
      fi
    fi
    
有关正在运行的 MPlayer 实例的更详细信息： 
    
    $ ps -eo pcpu,pid,user,comm | grep -i "mplayer"$ | sed  "s/ mplayer$//m"
    
###  额外的二进制解码器

如果你需要播放使用 cook、drvc 或 sipr 编解码器编码的媒体，可以安装带有必要的二进制编解码器包 [codecs64](<https://aur.archlinux.org/packages/codecs64/>)AUR。更多信息参见 [[2]](<http://www.mplayerhq.hu/design7/dload.html>)。 

##  问题处理

###  无法打开名称含空格的文件

打开名称含空格的文件时，如果报类似于“无法打开 `file:///_The%20Movie_`”的错误（空格被替换成 `%20` 了），可以通过下面的方法解决： 

打开 `/usr/share/applications/mplayer.desktop`，修改下面的内容： 
    
    Exec=mplayer %U
    
为： 
    
    Exec=mplayer "%F"
    
如果要使用图形前端，修改为 `Exec=gui_name "%F"` 即可。 

###  OSD 和字幕有黑色或奇怪颜色的字体

当使用 MPlayer 可能默认使用的 `vdpau` 输出时，似乎 OSD 和字体颜色会有问题。你可以使用 `xv` 而不是 `vdpau` 来绕过这一问题。 

作为一个命令行选项： 
    
    mplayer -vo xv
    
添加如下一行到你的 `~/.mplayer/config` 文件： 
    
    vo=xv
    
详细信息参见[原帖](<https://bbs.archlinux.org/viewtopic.php?pid=1379141>)。 

###  Smplayer无图像

打开 `mp4` 和 `flv` 文件时，SMPlayer 可能出现无图像问题。解决方法如下： 

打开 `~/.mplayer/config` 添加： 
    
     [extension.mp4]
     demuxer=mov
    
如果还有问题，可能是由 SMPlayer 原有设置导致的。删除设置文件即可： 
    
     $ rm -rf ~/.config/smplayer/file_settings
    
###  Gnome中启用复合的透明 SMPlayer

在使用 compiz 和 cairo dock 时，你注意到 SMPlayer 的透明屏幕了吗？当你用 SMPlayer 打开视频时，你只能听到音频而没有视频，这是很可笑的！下面是解决方法：[复制粘贴到终端] 
    
       sudo bash -c "cat > /usr/bin/smplayer.helper" <<EOF
       export XLIB_SKIP_ARGB_VISUALS=1
       exec smplayer.real "$@"
       EOF
       sudo chmod 755 /usr/bin/smplayer.helper
       sudo mv /usr/bin/smplayer{,.real}
       sudo ln -sf smplayer.helper /usr/bin/smplayer
    
如果你不使用 `sudo`, 请直接使用 `su` 以 root 登录并执行上述命令！ 

###  SMPlayer: OSD font too big / subtitle text too small

自 SMPlayer 0.8.2.1 (with MPlayer2 20121128-1)起, 字幕字体与OSD字体的比例非常奇怪。这可能会导致 OSD 文字占满整个屏幕而字体太小以至于无法阅读。这个问题可以通过添加如下选项解决： 
    
    -subfont-osd-scale 2
    
或者添加到由 SMPlayer 传输到 MPlayer 的额外选项解决。这些选项可在 _Options > Preferences > Advanced > Options for MPlayer_ 找到。也可以通过添加如下的行到 `~/.mplayer/config` 解决： 
    
    subfont-osd-scale=2
    
###  Mplayer 字幕中某些字符显示为问号

如果字幕的编码方式是 utf8，请尝试使用： 
    
    -subcp utf8
    
你可以使用如下命令查看字幕的编码方式： 
    
    file subtitles.srt
    
参考 [mplayer-shows-question-marks-for-some-characters-on-subtitle](<https://www.linuxquestions.org/questions/slackware-14/mplayer-shows-question-marks-for-some-characters-on-subtitle-works-fine-on-xine-906077/>). 

###  断断续续的音频 CD 播放

当 CDROM 向下旋转 CD 时，CDDA 播放可能每隔几秒钟中断一次。要解决这个问题，你需要使用 `-cache` 选项提前缓存或缓冲： 
    
    mplayer cdda://:1 -cache 1024
    
`:1` 是为了降低 CDROM 的速度，以获得恒定的自旋和较少的噪声。 

##  参阅

  * [MPlayer FAQ](<https://wiki.multimedia.cx/index.php?title=MPlayer_FAQ>)
  * [MPlayer tips](<https://help.ubuntu.com/community/MPlayerTips>)
  * [How to configure MPlayer](<https://how-to.wikia.com/wiki/How_to_configure_MPlayer>)
  * [playerctl](<https://github.com/acrisci/playerctl>): A command-line utility and library for controlling media players
