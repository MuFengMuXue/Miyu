**翻译状态：**

  * 本文（或部分内容）译自 [Mpv](<https://wiki.archlinux.org/title/Mpv> "arch:Mpv")，最近一次同步于 2024-09-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mpv?diff=0&oldid=828287>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mpv_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [MPlayer](<../zh-cn/MPlayer.html> "MPlayer")
  * [yt-dlp](<../zh-cn/Yt-dlp.html> "Yt-dlp")

[mpv](<https://mpv.io/>) 是一款基于 [MPlayer](<../zh-cn/MPlayer.html> "MPlayer") 和 _mplayer2_ 的多媒体播放器（ _mplayer2_ 现已不再维护）。它支持多种类型的视频文件格式、音视频编解码器和字幕。[这里](<https://github.com/mpv-player/mpv/blob/master/DOCS/mplayer-changes.rst>)有一份不太完整的关于 _mpv_ 与上述播放器之间差异的详细列表。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mpv](<https://archlinux.org/packages/?name=mpv>)包 软件包或开发者版本的 [mpv-git](<https://aur.archlinux.org/packages/mpv-git/>)AUR。 

###  前端

参见[应用程序列表/多媒体#基于_mpv](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E5%9F%BA%E4%BA%8E_mpv> "应用程序列表/多媒体")。 

##  配置

_mpv_ 拥有良好且全面的默认设置，即使电脑上的显卡老旧或性能较弱， _mpv_ 也能良好运行。然而，在配备有更新更现代的显卡的电脑上， _mpv_ 经过详尽配置，即可获得更好的视频品质（视频品质的高低取决于显卡性能）。要实现这一点，只需要创建一些配置文件（这些配置文件默认不存在）。 

**注意：** 系统级配置文件会从 `/etc/mpv/` 中读取，用户级配置文件在未设置 `XDG_CONFIG_HOME` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")的情况下将从 `~/.config/mpv/` 中读取，用户级配置会覆盖系统级配置，而在命令行使用的配置将覆盖上述所有配置。配置时可能需要反复试错，因此，建议使用用户级配置。

_mpv_ 提供了包含默认设置的配置文件示例，将这些文件复制一份然后开始配置： 
    
    $ cp -r /usr/share/doc/mpv/ ~/.config/
    
`mpv.conf` 是 _mpv_ 的主要配置文件，`input.conf` 包含了按键绑定的配置。通读这两个文件，了解它们的工作原理以及可用选项。 

###  通用设置

将以下设置写入 `~/.config/mpv/mpv.conf`。 

####  字幕配置

启用模糊搜索： 
    
    sub-auto=fuzzy
    
更改字体： 
    
    sub-font="fontName"
    
将字幕加粗以增加可读性： 
    
    sub-bold=yes
    
####  高品质配置

默认设置下，mpv 兼顾质量和性能。此外，它还提供了两个预定义的配置：代表最高性能的 `fast` 和代表卓越渲染质量的 `high-quality`。使用 `--profile=_name_` 选项以应用某个特定的配置，使用 `--show-profile=_name_` 查看该配置的内容。 
    
    profile=high-quality
    
_mpv_ 的实时性能统计数据可通过 `i` 键调出查看。此功能在确认硬件是否以当前配置运行，或用于对比不同配置下的运行情况时非常有用。 

最后两个选项稍微有些复杂。`video-sync=display-resample` 选项能够在音频与视频不同步时，通过保留视频帧，并对音频进行重新采样以保证音视频同步（相较于视频丢帧，音频音调的轻微改变通常难以分辨）。相关的深入探讨位于 mpv 维基上的[显示同步](<https://github.com/mpv-player/mpv/wiki/Display-synchronization>)。`interpolation` 选项通过改变视频帧的显示方式，让源视频帧更好地贴合显示器的刷新率，以此让画面上的移动显得更加平滑（不要与 SVP 的技术相混淆，后者实际上是将视频转换至 60 帧）。相关的深入探讨位于 mpv 维基上的 [Interpolation](<https://github.com/mpv-player/mpv/wiki/Interpolation>)（Interpolation 又常被称为 _smoothmotion_ ）。 
    
    profile=high-quality
    video-sync=display-resample
    interpolation
    
**注意：** 使用 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") 时，`video-sync=display-resample` 选项可能会导致视频加速。同时，在某些系统上，该选项会彻底扰乱帧速率，插值（interpolation）将完全失去作用。

你能做的远不止于此，但同时，随着配置深入，这些配置细节将更加复杂，对显卡的性能要求也更高。简而言之，可以加载那些实现了奇特的缩放和锐化技术的特殊着色器，这其中包括那些实际上使用了经过图像训练（真实世界和动画化的图像均有）的深度神经网络的着色器。要了解更多相关细节，请查阅 [mpv wiki](<https://github.com/mpv-player/mpv/wiki>)，尤其是 [user shader's section](<https://github.com/mpv-player/mpv/wiki/User-Scripts#user-shaders>) 这部分。 

更多其他配置项参见 [mpv(1)](<https://man.archlinux.org/man/mpv.1>)。在命令行运行 _mpv_ 检查配置的错误信息也能获取帮助。 

####  自定义配置

自定义配置可在 `mpv.conf` 中创建，这些“配置”实际上只是“选项组”，它们可用于： 

  * 在不同的配置之间快速切换，无需重写文件。
  * 为特殊内容创建特殊配置。
  * 嵌套多个配置，将简单的配置组合成更复杂的配置。

创建一个配置很简单。`mpv.conf` 文件的开头区域被称为“顶层”，写在此处的所有选项都会在 _mpv_ 启动后生效。要创建一个配置，首先写下一对中括号，然后在中括号内写下配置的名称。一旦创建了配置，接下来写的所有选项（直到下一个配置开始之前）都属于该配置。这是一份 `mpv.conf` 文件的示例： 
    
    profile=myprofile2        #“顶层”区域，加载 myprofile2
    ontop=yes                 #窗口置顶
    
    [myprofile1]              #一份简单的配置，“顶层”区域到此处结束
    profile-desc="a profile"  #可选的配置描述
    fs=yes                    #以全屏模式启动
    
    [myprofile2]              #另一份简单的配置
    profile=high-quality      #mpv 自带的一个配置
    log-file=~~/log           #设置日志文件的位置，~~/ 会被转换成 ~/.config/mpv
    
上述示例文件中，“顶层”区域仅有两行，区域下方定义了两个单独的配置。 _mpv_ 启动时，读取第一行的内容，加载 `myprofile2` 的选项，这相当于加载了 `high-quality` 中的选项以及 `log-file=~~/log` 选项，最终加载 `ontop=yes` 选项，至此启动完成。注意，由于没有在“顶层”区域调用 `myprofile1` 配置，该配置将不会被加载。 

又或者，直接从命令行调用 _mpv_ ： 
    
    $ mpv --profile=myprofile1 video.mkv
    
此时，除 `myprofile1` 这一配置内的选项，其余所有选项都会被忽略。 

#####  自动配置

mpv 会根据文件扩展名或是使用的协议，自动加载特定类型的配置。 

根据匹配的文件扩展名，分别为扩展名是 _.mkv_ 和 _.gif_ 的所有文件加载其对应的配置： 
    
    [extension.mkv]
    keep-open
    volume-max=150
    
    [extension.gif]
    osc=no
    loop-file

当播放任意的 http 或 https 流时加载下面的配置（例如 `mpv https://example.com/video.mp4`）： 
    
    [protocol.https]
    speed=2
    keep-open
    
    [protocol.http]
    profile=protocol.https

运行 `mpv --list-protocols` 以查看 mpv 支持的不同协议。 

###  按键绑定

根据 `/usr/share/doc/mpv/input.conf` 和 [mpv(1) § COMMAND INTERFACE](<https://man.archlinux.org/man/mpv.1#COMMAND_INTERFACE>) 中的示例，按键绑定简单明了。 

将下面的示例添加至 `~/.config/mpv/input.conf`： 
    
    shift+s         screenshot each-frame
    Shift+UP        seek  600
    Shift+DOWN      seek -600
    =               cycle video-unscaled
    -               cycle-values window-scale 2 3 1 .5
    WHEEL_UP        add volume 5
    WHEEL_DOWN      add volume -5
    WHEEL_LEFT      ignore
    WHEEL_RIGHT     ignore
    Alt+RIGHT       add video-rotate 90
    Alt+LEFT        add video-rotate -90
    Alt+-           add video-zoom -0.25
    Alt+=           add video-zoom 0.25
    Alt+j           add video-pan-x -0.05
    Alt+l           add video-pan-x 0.05
    Alt+i           add video-pan-y 0.05
    Alt+k           add video-pan-y -0.05
    Alt+BS          set video-zoom 0; set video-pan-x 0; set video-pan-y 0
    
有关在 mpv 中重现 MPC-HC 按键绑定的尝试，请参考[这个链接](<https://github.com/dragons4life/MPC-HC-config-for-MPV/blob/master/input.conf>)。 

###  额外配置文件

此外，还可以创建一些配置文件和目录，其中包括： 

  * `~/.config/mpv/script-opts/osc.conf` 负责管理屏幕控制器。更多信息请参阅 [mpv(1) § ON SCREEN CONTROLLER](<https://man.archlinux.org/man/mpv.1#ON_SCREEN_CONTROLLER>)。
  * `~/.config/mpv/scripts/_script-name_.lua` 表示 Lua 脚本。获取示例请参考[这个链接](<https://github.com/mpv-player/mpv/issues/3500#issuecomment-305646994>)。

要了解其他文件和目录的相关信息，请参阅 [mpv(1) § FILES](<https://man.archlinux.org/man/mpv.1#FILES>)。 

##  脚本

mpv 有大量可扩展播放器功能的脚本（参见[用户脚本](<https://github.com/mpv-player/mpv/wiki/User-Scripts>)）。为此，它为 Lua 和 JavaScript 提供了内部绑定。 

脚本的安装方式通常是将它们放在 `~/.config/mpv/scripts/` 目录内（可能需要先创建该目录）。之后，它们将在 mpv 启动时被自动加载（这个行为可以被其他 _mpv_ 选项修改）。有些脚本自带安装和配置说明，请务必查看。此外，有些脚本已经陈旧、损坏且不再维护。 

### JavaScript

JavaScript（ES5 via [MuJS](<https://mujs.com/>)）自 2014 年起作为 mpv 的脚本语言得到支持。目前仅有[少量脚本](<https://github.com/mpv-player/mpv/wiki/User-Scripts#javascript>)可用，如果想要自己制作脚本，[mpv(1) § JAVASCRIPT](<https://man.archlinux.org/man/mpv.1#JAVASCRIPT>) 有文档可供参考。 

在 mpv 的 `scripts` 目录下放入一个扩展名为 `.js` 的脚本以开始使用，例如： 
    
    ~/.config/mpv/scripts/fullscreen-off-on-pause.js
    
    function onPauseChange (prop, enabled) {
        if (enabled) {
            mp.set_property('fullscreen', 'no')
        }
    }
    
    mp.observe_property('pause', 'bool', onPauseChange)
    
想要了解更多细节，例如，关于使用 `require` 加载 CommonJS 模块，请参见 [mpv(1) § CommonJS modules and require(id)](<https://man.archlinux.org/man/mpv.1#CommonJS_modules_and_require\(id\)>)。 

[mpv](<https://archlinux.org/packages/?name=mpv>)包 软件包和 AUR 中的某些软件包（例如 [mpv-full](<https://aur.archlinux.org/packages/mpv-full/>)AUR 和 [mpv-full-git](<https://aur.archlinux.org/packages/mpv-full-git/>)AUR）已支持 JavaScript。 

### Lua

_mpv_ 的 Lua 脚本开发记录在 [mpv(1) § LUA SCRIPTING](<https://man.archlinux.org/man/mpv.1#LUA_SCRIPTING>) 和 [TOOLS/lua](<https://github.com/mpv-player/mpv/tree/master/TOOLS/lua>) 的示例中，这些脚本会被安装到 `/usr/share/mpv/scripts`。 

例如，启用内置脚本，自动裁剪带黑条的视频： 
    
    $ ln -s /usr/share/mpv/scripts/autocrop.lua ~/.config/mpv/scripts
    
#### mpv-ytdlAutoFormat

[mpv-ytdlautoformat](<https://github.com/Samillion/mpv-ytdlautoformat>) 是一个 Lua 脚本，能够将 Youtube 的 ytdl-format、Twitch 或者其他域的内容，自动转换成 480p 或是你需要的视频品质。 

#### mpv-webm

[mpv-webm](<https://github.com/ekisu/mpv-webm>)（或简称为 _webm_ ）是一个易于使用的 Lua 脚本， 允许在观看视频的同时创建 WebM 文件。它包含了若干特性，并且，它没有任何额外的依赖项（完全依赖于 mpv）。 

#### ytdl-preload

[ytdl-preload](<https://gist.github.com/bitingsock/17d90e3deeb35b5f75e55adb19098f58>) Lua 脚本能够预加载播放列表中的下一个 ytdl-link。 

**注意：** 该脚本仍处于积极开发的阶段。

### C

#### mpv-mpris

[mpv-mpris](<https://github.com/hoyon/mpv-mpris>) 插件由 C 语言开发，它允许其他应用程序通过 [MPRIS](<../zh-cn/MPRIS.html> "MPRIS") 协议与 _mpv_ 集成。例如，安装 _mpv-mpris_ 后，[kdeconnect](<https://archlinux.org/packages/?name=kdeconnect>)包 能够在电话来电时自动暂停 _mpv_ 中播放的视频。另一个例子是集成蓝牙音频设备上的播放或暂停等按钮。 

安装 [mpv-mpris](<https://archlinux.org/packages/?name=mpv-mpris>)包 以使用该插件。 

## Vapoursynth

Vapoursynth 是 AviSynth 的替代品，可用于 Linux，并允许通过 python 脚本进行视频操作。Vapoursynth 的 python 脚本可被用作 _mpv_ 的视频过滤器。 

[mpv](<https://archlinux.org/packages/?name=mpv>)包 软件包现已默认启用 Vapoursynth 支持。 

###  SVP 4 Linux (SmoothVideoProject)

[SmoothVideoProject SVP](<https://www.svp-team.com/wiki/Main_Page>) 是一个主要用于转换视频帧率至 60 帧的程序。它免费且功能齐全，适用于 64 位 Linux（Windows 和 OS X 版本是收费的，且不兼容 32 位 Linux）。 

它有三个主要功能，每个功能都可以任意禁用或启用（不会强制使用运动插补）。 

  1. [运动插补](<https://www.svp-team.com/wiki/Manual:FRC>)（[youtube 视频](<https://www.youtube.com/watch?v=Wjb6CSe4708>)）- 一种将视频帧率转换至 60 帧的算法。这会产生具有争议性的“肥皂剧效应”，有人喜欢，有人讨厌。遗憾的是，这种算法并不完美，还会产生许多奇怪的伪影。它可以根据性能或品质进行调整（通过滑块）。它也提供了一些减少伪影的设置，将实际帧与生成帧插补以减少伪影的明显程度。帧率检测可设置成自动或手动（手动似乎能解决某些用户的性能问题）。
  2. [黑条光照（Black bar lighting）](<https://www.svp-team.com/wiki/Manual:Outer_lighting>)（[youtube 视频](<https://www.youtube.com/watch?v=yTzTpW3kTBE>)）- 如果图像的宽高比在显示屏上产生黑条，SVP 将用屏幕内容生成的“光照”使黑条发光。可对它进行一些自定义设置，但默认设置非常接近最佳状态。
  3. [LED 环境光照控制](<https://www.svp-team.com/wiki/Manual:SVPlight>)([youtube 视频](<https://www.youtube.com/watch?v=UUM2n-8kIJ8>)）- 可控制电视机上的 LED 环境光照。

一旦编译了支持 Vapoursynth 的 _mpv_ ，让 SVP 与 _mpv_ 协同工作就非常简单。仅需安装 [svp-bin](<https://aur.archlinux.org/packages/svp-bin/>)AUR，打开 SVP 程序，让它评估系统性能（可能需要先关闭其他程序以获取准确的结果）,最后在 mpv.conf 中添加下面的 _mpv_ 配置 [[1]](<https://www.svp-team.com/wiki/SVP:mpv>)： 
    
    mpv.conf
    
    [svp]
    input-ipc-server=/tmp/mpvsocket     # 接收来自 SVP 的输入
    hr-seek-framedrop=no                # 修复音频不同步
    watch-later-options-remove=vf       # 不保留 SVP 的视频过滤器
    
    # 某些情况下可修复卡顿，其他情况下可能引起卡顿。如遇卡顿可以尝试。
    #opengl-early-flush=yes

然后，为了使用 SVP，在以该配置运行 _mpv_ 并打开文件之前，必须在后台运行 SVP 程序。要么像这样使用： 
    
    $ mpv --profile=svp video.mkv
    
要么在 _mpv_ [配置](<#%E8%87%AA%E5%AE%9A%E4%B9%89%E9%85%8D%E7%BD%AE>)的“顶层”部分设置 `profile=svp`。 

要使用硬件解码，必须使用回传解码器（copy-back decoder），因为普通解码器不兼容 Vapoursynth（请选择一个以 `-copy` 结尾的 `hwdec` 选项）。例如： 
    
    hwdec=auto-copy
    hwdec-codecs=all
    
_mpv_ 的开发人员无论如何都不鼓励使用硬件解码，而且硬件解码也不可能在性能上产生显著的差异。 

##  提示与技巧

###  图像

####  硬件视频加速

参见[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")。 

硬件加速视频解码可通过 `--hwdec=_API_` 选项启用。要获取所有受支持的接口和其他选项，请参见 [mpv(1) § hwdec](<https://man.archlinux.org/man/mpv.1#hwdec=_api1,api2,..._no_auto_auto>)。 

将该选项添加到配置文件以使其始终生效（例如在桌面环境播放视频）： 
    
    ~/.config/mpv/mpv.conf
    
    hwdec=auto

要允许 CPU 处理视频滤镜，请从 `*-copy` 中选择某个接口。 

视频播放时，可使用键盘快捷键 `Ctrl+h` 切换硬件解码。 

要排除硬件加速故障，可能需要调整日志记录级别（参见 [mpv(1) § msg-level](<https://man.archlinux.org/man/mpv.1#msg-level>)）。例如，`--msg-level=vd=v,vo=v,vo/gpu/vaapi-egl=trace` 将启用以下功能： 

  * 来自视频解码模块 (`vd`) 和视频输出模块 (`vo`) 的详细信息。
  * 负责视频解码模块的更详细的跟踪信息。根据经验，在没有调整任何日志记录级别的情况下运行 mpv 之后，相关模块应该是 `vo/gpu/vaapi-egl`。

####  在宽高比之间快速切换

使用 `Shift+a` 在宽高比之间切换。 

####  忽略宽高比

使用 `--keepaspect=_no_` 忽略宽高比。要使该选项始终生效，请在配置文件中添加 `keepaspect=_no_` 这一行。 

####  绘制至根窗口

使用 `--wid=0` 参数运行 _mpv_ 。 _mpv_ 将绘制到 ID 为 0 的窗口中。 

####  始终显示应用程序窗口

要让从命令行启动的 mpv（即使播放的是音频文件）显示应用程序窗口，请使用 `--force-window` 选项。要使该选项始终生效，请在配置文件中添加 `force-window=yes` 这一行。 

####  禁用视频输出

要在命令行启动时禁用视频输出，请使用 `--vid=no` 选项，或是其别名 `--no-video`。 

####  终端输出视频

  * `--vo=tct` “彩色 Unicode 艺术的视频输出驱动程序，可在文本控制台中运行。”
  * `--vo=caca` “彩色 ASCII 艺术的视频输出驱动程序，可在文本控制台中运行。”由于存在漏洞（参见 [FS#70962](<https://bugs.archlinux.org/task/70962>)），Arch Linux 禁用了 [libcaca](<https://archlinux.org/packages/?name=libcaca>)包 支持，并且由于其上游停止活动，此包尚未被重新加入：安装 [mpv-full](<https://aur.archlinux.org/packages/mpv-full/>)AUR。

###  音频

####  音量过低

为配置文件中的 `volume-max=_value_` 设置一个合适的值，例如 `volume-max=150`，这将使音量提高至 150%，也就是两倍多的音量。将音量调得过高会产生削波假象（clipping artefacts）。此外（或作为替代方法），还可以使用 `af=acompressor` [动态压缩范围](<https://en.wikipedia.org/wiki/Dynamic_range_compression> "wikipedia:Dynamic range compression")。 

####  指定音频输出

运行以下命令获取可用音频输出设备列表： 
    
    $ mpv --audio-device=help
    
然后将其中的某个设备添加至 `~/.config/mpv/mpv.conf`。例如： 
    
    audio-device=alsa/hdmi:CARD=NVidia,DEV=1
    
####  高清音频直通

要使 TrueHD 和 DTS-MA 等高清音频编解码器直通影音接收器，请将以下内容添加至 `~/.config/mpv/mpv.conf`。 
    
    audio-spdif=ac3,eac3,dts-hd,truehd
    
####  音量标准化

不同信号源的响度可能不同或不一致，因此 _mpv_ 用户可能需要配置自动音量标准化。例如： 
    
    ~/.config/mpv/input.conf
    
    n cycle_values af loudnorm=I=-30 loudnorm=I=-15 anull

这会绑定按键 `n`，使音频过滤器设置（`af`）在指定的值之间循环： 

  * `loudnorm=I=-30`：loudnorm 设置为 `I=-30`，音量小，可能适合背景音乐
  * `loudnorm=I=-15`：音量大一些，可能适合当前播放的视频
  * `anull`：音量过滤器重置为空（null），即禁用音频过滤器

**注意：** 绑定一个按键并不会改变默认的音频过滤器。要改变默认值，请将例如 `af=loudnorm=I=-30` 的配置项添加到主配置文件中。

_mpv_ 中的音频过滤功能由后端的 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 提供。参见 [Wikipedia:EBU R 128](<https://en.wikipedia.org/wiki/EBU_R_128> "wikipedia:EBU R 128") 和 [ffmpeg loudnorm filter](<https://ffmpeg.org/ffmpeg-filters.html#loudnorm>) 以获取细节信息。 

另请参见上游问题 [[2]](<https://github.com/mpv-player/mpv/issues/3979>) 和 [[3]](<https://github.com/mpv-player/mpv/issues/2883>)，其中提到了不同的选项。 

####  在 mpv 用作音乐播放器时使用 Lua 脚本增强其功能

[这篇博文](<https://web.archive.org/web/20160320001546/http://bamos.github.io/2014/07/05/mpv-lua-scripting/>)介绍了 [music.lua](<https://github.com/bamos/dotfiles/blob/master/.mpv/scripts.old/music.lua>) 脚本，该脚本展示了如何在 mpv 用作音乐播放器时，使用 Lua 脚本增强其功能。 

###  退出时保存播进度

默认情况下，按下快捷键 `Shift+q` 可保存播放进度并退出。可在按键绑定的配置文件中设置 `quit_watch_later` 以修改此快捷键。 

要在退出时自动保存当前播放位置，请以 `--save-position-on-quit` 启动 _mpv_ ，或将 `save-position-on-quit` 添加至配置文件。 

####  保存在播放列表中的位置以及在播放下一个文件时暂停播放

播放列表可以是一个文件列表，参见 [mpv(1) § playlist](<https://man.archlinux.org/man/mpv.1#playlist=_filename_>)。要播放一个列表并记住播放位置： 
    
    $ mpv --save-position-on-quit --pause --reset-on-next-file=pause --playlist=_/path/to/playlist_
    
以 `--pause` 选项启动时， _mpv_ 将处于暂停状态，当切换至下一个文件时，`--reset-on-next-file=pause` 将重置暂停模式。 

###  播放 DVD

mpv 不支持 DVD 菜单。要以视频 DVD 的最长标题启动主流，使用这个命令： 
    
    $ mpv dvd://
    
可选的标题指定符是一个数字（从 0 开始），可在 DVD 上单独的视频流之间进行选择： 
    
    $ mpv dvd://[title] 
    
已被复制到本地文件系统（例如使用了 [dvdbackup](</wzh/index.php?title=Dvdbackup&action=edit&redlink=1> "Dvdbackup（页面不存在）")（英语：[dvdbackup](<https://wiki.archlinux.org/title/dvdbackup> "en:dvdbackup")） 工具）的 DVD 可通过指定本地拷贝将其包含进来：`--dvd-device=_PATH_`。 

要从本地文件系统播放 DVD，请参考下面的[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")示例： 
    
    [Desktop Entry]
    Type=Application
    Name=mpv Media Player DVD 
    GenericName=Multimedia player
    Comment=Play movies and songs
    Icon=mpv
    Exec=mpv dvd:// --player-operation-mode=pseudo-gui --force-window --idle --dvd-device=%f
    Terminal=false
    Categories=AudioVideo;Audio;Video;Player;TV;
    #（MimeType 和 X-KDE-Protocols 已省略，参见原 mpv.desktop 文件）
    
将 Exec 这一行替换为： 
    
    Exec=mpv dvd://0 dvd://1 dvd://2 dvd://3 dvd://4 dvd://5 dvd://6 dvd://7 dvd://8 dvd://9  --player-operation-mode=pseudo-gui --force-window --idle --dvd-device=%f
    
mpv 播放器会将 DVD 标题以从 0 到 9 的顺序排列在播放列表内，这样用户就可以连续地播放或通过 mpv 用户界面在 DVD 标题之间前后跳转。 

安装 [libdvdcss](<https://archlinux.org/packages/?name=libdvdcss>)包 以解决以下问题： 
    
    [dvdnav] Error getting next block from DVD 1 (Error reading from DVD.)
    
###  恢复旧的屏幕控件

自 0.21.0 版本起， _mpv_ 已经将屏幕控件（on-screen controls）替换为底部栏（bottombar）。如果想要恢复屏幕控件，可以按照[此处的说明](<https://github.com/mpv-player/mpv/wiki/FAQ#i-want-the-old-osc-back>)编辑 _mpv_ 的配置。 

###  可重现的屏幕截图

屏幕截图的模板选项可以包含截屏帧的精确时间码（HH:MM:SS.mmm）。有意义的文件名更易于了解屏幕截图的来源。可以像这样设置它： 
    
    ~/.config/mpv/mpv.conf
    
    screenshot-template="%F - [%P] (%#01n)"

这将扩展至 `_filename_ - [HH:MM:SS.mmm] (_number_).jpg`。结果示例： 
    
    Gunsmith Cats/
    ├── Gunsmith Cats Ep. 01 - [00:00:50.217] (1).jpg
    ├── Gunsmith Cats Ep. 01 - [00:22:55.874] (1).jpg
    ├── Gunsmith Cats Ep. 01 - [00:22:55.874] (2).jpg
    └── Gunsmith Cats Ep. 02 - [00:15:05.778] (1).jpg
    
这样的一个好处是，文件排序得当，因为时间码在章节编号内部以字母顺序进行排列。 

参见 [mpv(1) § screenshot-template](<https://man.archlinux.org/man/mpv.1#screenshot-template>) 以获取更多信息。 

###  创建单张屏幕截图

这是使用开始时间（`HH:MM:SS`）创建单张屏幕截图的示例： 
    
    $ mpv --no-audio --start=00:01:30 --frames=1 /path/to/video/file --o=/path/to/screenshot.png
    
屏幕截图将被保存至 /path/to/screenshot.png。 

### Streaming

#### Twitch.tv streaming over mpv

安装好 [yt-dlp](<../zh-cn/Yt-dlp.html> "Yt-dlp") 或 [youtube-dl](<https://aur.archlinux.org/packages/youtube-dl/>)AUR 后， _mpv_ 能直接打开 Twitch 的直播流。 

或参见 [Streamlink#Twitch](<../zh-cn/Streamlink.html#Twitch> "Streamlink")。 

另一个选择是基于 Livestreamer 的 [Lua 脚本](<https://gist.github.com/ChrisK2/8701184fe3ea7701c9cc>)。 

####  youtube-dl 和格式选择

`--ytdl-format` 的默认值是 `bestvideo+bestaudio/best`。这可能意味着，对于那些有 4K 分辨率的 youtube 视频，即使连接着的显示器分辨率低得多，软件内解码 VP9 编码的 4K 视频对于设备而言依然十分困难。 

然而，设置正确的 youtube-dl 格式选择器能轻易地解决这个问题。下面的配置示例中，只有垂直分辨率小于等于 1080 像素的视频会被选择。 
    
    ytdl-format="bestvideo[height<=?1080]+bestaudio/best"
    
因无法硬件解码而希望完全禁用特定的编解码器，可以将其添加至格式选择器内。例如，可额外选择忽略 VP9，如下所示： 
    
    ytdl-format="bestvideo[height<=?1080][vcodec!~='vp0?9']+bestaudio/best"
    
若更倾向于开源编解码器（VP9 和 Opus），请使用： 
    
    ytdl-format="((bestvideo[vcodec^=vp9]/bestvideo)+(bestaudio[acodec=opus]/bestaudio[acodec=vorbis]/bestaudio[acodec=aac]/bestaudio))/best"
    
####  youtube-dl 音频搜索

要从终端模拟器中使用 `yta _search terms_` 寻找并串流音频，将下面的函数添加至 `.bashrc`： 
    
    function yta() {
        mpv --ytdl-format=bestaudio ytdl://ytsearch:"$*"
    }
    
###  系统集成

####  从 KDE 的剪切板中打开视频链接

如果已安装 [youtube-dl](<https://aur.archlinux.org/packages/youtube-dl/>)AUR 或 [yt-dlp](<https://archlinux.org/packages/?name=yt-dlp>)包，并且正在使用 [KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma")，可以在 KDE 的剪切板中创建一个自定义操作来方便快捷地播放来自视频分享站点的链接。 

  1. 打开剪切板配置菜单（典型的做法是右键它的系统托盘图标）然后前往 _Actions_ 标签页。
  2. 点击 _Add Action_ 然后输入用于探测想要从中播放视频的网站的正则表达式（例如，`^http.+(youtu|twitch)` 用于探测 YouTube 和 Twitch 的网站）。
  3. 点击 _Add Command_ ，在 _Command_ 下输入 `mpv %s` 并在 _Description_ 下输入 `mpv`。

此时，在剪切板内按下快捷键 `Ctrl+Alt+r` 并在上下文菜单中选择 _mpv_ 即可播放来自剪切板的视频链接。有可能需要前往 _Advanced Settings_ 并将火狐浏览器从 _Disable Actions for Windows of Type WM_CLASS_ 这一小节移除。 

##  故障排除

###  常规调试

若使用 _mpv_ 播放时遇到问题（或完全无法运行），首先需要做这三件事： 

  1. 从命令行启动 _mpv_ （-v 标识用于增加输出信息详细程度）。幸运的话，你会看到一条错误信息，告诉你什么地方出错了。  
`$ mpv -v video.mkv`
  2. 让 _mpv_ 输出日志文件。日志内容可能难以筛选，但如果有什么东西坏了，你应该能在日志里看到。  
`$ mpv -v --log-file=./log video.mkv`
  3. 无配置文件运行 _mpv_ 。如果运行正常，那么问题应该在配置文件的某处（或许是硬件无法跟上你的设置）。  
`$ mpv --no-config video.mkv`

如果 _mpv_ 能够运行但运行状态不佳，那么第四件值得一试的事就是查看实时统计数据（使用快捷键 `i`），确认其具体运行情况。 

###  修复播放卡顿和撕裂问题

在支持 OpenGL 的硬件上， _mpv_ 默认使用 OpenGL 视频输出设备设置。在尝试使用英特尔 HD4XXX 系列显卡或类似显卡在 4K 显示器上播放视频时，使用任何 OpenGL 输出设置都会出现播放卡顿（有时甚至完全停止）和严重的撕裂问题。如果遇到以上问题，使用 XV 视频输出（仅适用于 [Xorg](<../zh-cn/Xorg.html> "Xorg")）或许有用： 
    
    ~/.config/mpv/mpv.conf
    
    vo=xv

**注意：** 这是 X 上兼容性最佳的视频输出，但视频品质可能很低，在屏幕显示（OSD）和字幕显示方面也存在问题。

这有可能进一步提升播放性能（尤其在低性能硬件上），但大多数情况下，这会大幅降低视频品质。 

要提升视频播放性能，可以考虑以下[配置项](<#%E9%85%8D%E7%BD%AE>)： 
    
    ~/.config/mpv/mpv.conf
    
    vd-lavc-fast
    vd-lavc-skiploopfilter=_skipvalue_
    vd-lavc-skipframe=_skipvalue_
    vd-lavc-framedrop=_skipvalue_
    vd-lavc-threads=_threads_

###  窗口合成器相关问题

如 [mpv(1) § Window](<https://man.archlinux.org/man/mpv.1#Window>) 中所述，mpv 在全屏模式下默认禁用任何活动窗口[合成器](<../zh-cn/Xorg.html#%E5%90%88%E6%88%90> "Xorg")。这用于防止播放时可能出现的性能问题。 

对于 KWin 或 Mutter 等窗口合成器而言，即使在窗口化模式下，禁用窗口合成也是有好处的。这可以通过设置 `x11-bypass-compositor=yes` 选项实现。 

禁用合成有两个缺点： 

  * 重新启用合成可能会出现一段时间的卡顿，尤其在使用 KWin 合成时。
  * 由合成提供的任何效果都将暂时不可用（直至 mpv 重新启用合成），这在 [Plasma](<../zh-cn/KDE.html> "Plasma") 中会阻止默认的应用程序切换器工作。

为避免这些问题，可使用 `x11-bypass-compositor=no` 令合成器保持启用状态。 

###  没有音量条，无法调整音量

在音量图标上滚动鼠标滚轮。 

###  GNOME Blank screen (Wayland)

在 Wayland 下 _mpv_ 可能不会暂停 GNOME 的省电设置，导致屏幕保护程序在视频播放时关闭显示器。解决方法是在 `mpv.desktop` 中 `Exec=` 这一行开头添加 `gnome-session-inhibit`。 

要仅在播放时阻止屏保，请使用 [mpv_inhibit_gnome](<https://aur.archlinux.org/packages/mpv_inhibit_gnome/>)AUR。作为替代方案，可使用这个基于 `gnome-session-inhibit` 的 [mpv Lua 脚本](<https://gist.github.com/crazygolem/a7d3a2d3c0cee5d072c0cbbbdee69286>)。 

**提示：** flatpak 应用程序 `io.mpv.Mpv` 已包含 [mpv_inhibit_gnome](<https://github.com/Guldoman/mpv_inhibit_gnome>) 插件。

###  光标主题在 GNOME Wayland 下不受约束

参见 [GNOME/Troubleshooting#Cursor size or theme issues on Wayland](</wzh/index.php?title=GNOME/Troubleshooting&action=edit&redlink=1> "GNOME/Troubleshooting（页面不存在）")（英语：[GNOME/Troubleshooting#Cursor size or theme issues on Wayland](<https://wiki.archlinux.org/title/GNOME/Troubleshooting#Cursor_size_or_theme_issues_on_Wayland> "en:GNOME/Troubleshooting")）。 

###  关于 AMD GPU 上缺少 CUDA 库的错误信息

[v0.34.1](<https://github.com/mpv-player/mpv/releases/tag/v0.34.1>) 以及更早版本的 mpv 在 AMD GPU 上使用 VAAPI 硬件加速时，可能会遇到持续的错误信息：`Cannot load libcuda.so.1`。设置 `gpu-hwdec-interop=vaapi` 可阻止此错误信息。 

相关错误报告：[Github issue #9691](<https://github.com/mpv-player/mpv/issues/9691>)，[Github issue #8765](<https://github.com/mpv-player/mpv/issues/8765>)。 

上游已在 [pull request #9842](<https://github.com/mpv-player/mpv/pull/9842>) 中修复该问题。 

###  无法在 PipeWire 被屏蔽时播放音频

如果 _mpv_ 在[屏蔽](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") [PipeWire](<../zh-cn/PipeWire.html> "PipeWire") 的系统上崩溃或无法播放音频（报告无输出或管道破损），请设置 `--ao` 选项以匹配环境。在 `mpv.conf` 中设置该选项以使其始终生效。 

###  mpv 无法从文件播放 DVD

如果 mpv 无法从纯 VIDEO_TS/VOB 结构的文件播放 DVD，则可能是恢复播放进度的功能存在问题。请尝试清理 `.config/mpv/watch_later` 文件夹，或以 `no-resume-playback`（也可设置 `save-position-on-quit=no` 选项）启动 _mpv_ 。 

###  修复暂停后恢复播放时出现的卡顿问题

如果在使用 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 时出现视频卡顿，请尝试 [mpv(1) § --pulse-latency-hacks](<https://man.archlinux.org/man/mpv.1#pulse~4>) 中讨论的 `pulse-latency-hacks` 选项： 
    
    ~/.config/mpv/mpv.conf
    
    pulse-latency-hacks=yes
