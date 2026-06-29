**翻译状态：**

  * 本文（或部分内容）译自 [PulseAudio](<https://wiki.archlinux.org/title/PulseAudio> "arch:PulseAudio")，最近一次同步于 2022-06-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/PulseAudio?diff=0&oldid=734615>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PulseAudio_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [PulseAudio/Examples](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）")
  * [PulseAudio/疑难解答](<../zh-cn/PulseAudio/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "PulseAudio/疑难解答")
  * [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")

[PulseAudio](<https://en.wikipedia.org/wiki/PulseAudio> "wikipedia:PulseAudio") 是一种通用的声音服务器，旨在使用 [ALSA](<../zh-cn/ALSA.html> "ALSA") 或 [OSS](<../zh-cn/Open_Sound_System.html> "OSS") 作为应用程序和硬件设备之间的中间件运行。如果启用，它还使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 在本地设备之间提供轻松的网络流。虽然其主要目的是简化音频配置，但其模块化设计允许更高级的用户精确地配置守护进程以最适合他们的需求。 

**注意：**[ALSA](<../zh-cn/ALSA.html> "ALSA") 与 PulseAudio之间可能会出现一些混淆。 ALSA 包括一个带有声卡驱动程序的 Linux 内核组件，以及一个用户空间组件 `libasound`。[[1]](<https://www.alsa-project.org/main/index.php/Download>) PulseAudio 仅构建在内核组件上，但提供 `libasound` 与 [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包的兼容性。[[2]](<https://www.freedesktop.org/wiki/Software/PulseAudio/FAQ/#index14h3>)

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pulseaudio](<https://archlinux.org/packages/?name=pulseaudio>)包 软件包。 

某些 PulseAudio 模块不包括在主封装中，如果需要，必须单独安装： 

  * [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包 用于 PulseAudio管理 [ALSA](<../zh-cn/ALSA.html> "ALSA")，请参阅 [#ALSA](<#ALSA>)
  * [pulseaudio-bluetooth](<https://archlinux.org/packages/?name=pulseaudio-bluetooth>)包 用于[蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "蓝牙")支持 (Bluez),请参阅[蓝牙耳机](<../zh-cn/%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA.html> "蓝牙耳机")
  * [pulseaudio-equalizer](<https://archlinux.org/packages/?name=pulseaudio-equalizer>)包 用于均衡器接收器 (qpaeq)
  * [pulseaudio-jack](<https://archlinux.org/packages/?name=pulseaudio-jack>)包 用于 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）") sink、source 和 jackdbus 检测
  * [pulseaudio-lirc](<https://archlinux.org/packages/?name=pulseaudio-lirc>)包 使用 [LIRC](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）") 进行红外音量控制
  * [pulseaudio-zeroconf](<https://archlinux.org/packages/?name=pulseaudio-zeroconf>)包 用于 Zeroconf ([Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")/DNS-SD) 支持

###  前端

有许多前端可用于控制 PulseAudio 守护程序： 

####  控制台

  * **ncpamixer** — 脉冲音频的Ncurses混音器，灵感来自pavucontrol。

     <https://github.com/fulhax/ncpamixer> || [ncpamixer](<https://aur.archlinux.org/packages/ncpamixer/>)AUR

  * **pacmixer** — Alsamixer 同样用于 PulseAudio。

     <https://github.com/KenjiTakahashi/pacmixer> || [pacmixer](<https://aur.archlinux.org/packages/pacmixer/>)AUR

  * **PAmix** — Ncurses PulseAudio mixer，类似于 pavucontrol。

     <https://github.com/patroclos/PAmix> || [pamix-git](<https://aur.archlinux.org/packages/pamix-git/>)AUR

  * **pamixer** — PulseAudio 命令行混音器。

     <https://github.com/cdemoulins/pamixer> || [pamixer](<https://archlinux.org/packages/?name=pamixer>)包

  * **pavolume** — PulseAudio 的简单命令行音量控制，带有 libnotify 消息。

     <https://github.com/sseemayer/pavolume> || [pavolume-git](<https://aur.archlinux.org/packages/pavolume-git/>)AUR

  * **Ponymix** — PulseAudio 命令行混音器。

     <https://github.com/falconindy/ponymix> || [ponymix](<https://aur.archlinux.org/packages/ponymix/>)AUR

  * **pulseaudio-ctl** — 从 shell 控制 PulseAudio 音量或映射到键盘快捷键。

     <https://github.com/graysky2/pulseaudio-ctl> || [pulseaudio-ctl](<https://aur.archlinux.org/packages/pulseaudio-ctl/>)AUR

  * **pulsemixer** — PulseAudio 的 CLI 和 curses 混音器

     <https://github.com/GeorgeFilipkin/pulsemixer> || [pulsemixer](<https://archlinux.org/packages/?name=pulsemixer>)包

####  图形界面

  * **KMix** — [KDE](<../zh-cn/KDE.html> "KDE") 音量控制应用程序支持多个平台，包括PulseAudio，系统托盘小程序可配置。

     <https://apps.kde.org/kmix/> || [kmix](<https://archlinux.org/packages/?name=kmix>)包

  * **MicTray** — 轻量级系统托盘应用程序，可让您使用 PulseAudio 控制麦克风状态和音量。

     <https://github.com/Junker/MicTray> || [mictray](<https://aur.archlinux.org/packages/mictray/>)AUR

  * **pa-applet** — PulseAudio 的系统托盘小程序，带音量条。

     <https://github.com/fernandotcl/pa-applet> || [pa-applet-git](<https://aur.archlinux.org/packages/pa-applet-git/>)AUR

  * **pasystray** — PulseAudio 的系统托盘小程序。

     <https://github.com/christophgysin/pasystray> || [pasystray](<https://archlinux.org/packages/?name=pasystray>)包

  * **plasma-pa** — [KDE](<../zh-cn/KDE.html> "KDE") Plasma 小程序，用于使用 PulseAudio 进行音量管理

     <https://invent.kde.org/plasma/plasma-pa> || [plasma-pa](<https://archlinux.org/packages/?name=plasma-pa>)包

  * **PulseAudio Equalizer** — 基于LADSPA的多频段均衡器，用于PulseAudio。

     <https://github.com/pulseaudio-equalizer-ladspa/equalizer> || [pulseaudio-equalizer-ladspa](<https://archlinux.org/packages/?name=pulseaudio-equalizer-ladspa>)包

  * **PulseAudio Graph Control** — PulseAudio 基于 Electron的音量和图形控制

     <https://github.com/futpib/pagraphcontrol#readme> || [pagraphcontrol-git](<https://aur.archlinux.org/packages/pagraphcontrol-git/>)AUR

  * **PulseAudio Manager** — PulseAudio 的简单 GTK 前端。已停止开发。

     <http://0pointer.de/lennart/projects/paman/> || [paman](<https://aur.archlinux.org/packages/paman/>)AUR

  * **PulseAudio Preferences** — PulseAudio 的简单 GTK 配置对话框。

     <https://freedesktop.org/software/pulseaudio/paprefs/> || [paprefs](<https://archlinux.org/packages/?name=paprefs>)包

  * **PulseAudio Volume Control** — PulseAudio的简单GTK音量控制工具（“混音器”）。

     <https://freedesktop.org/software/pulseaudio/pavucontrol/> || [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包

  * **PulseAudio Volume Control (Qt)** — Mixer for PulseAudio (Qt port of pavucontrol).

     <https://github.com/lxqt/pavucontrol-qt> || [pavucontrol-qt](<https://archlinux.org/packages/?name=pavucontrol-qt>)包

  * **PulseAudio Volume Control (Sandsmark)** — Lightweight fork of the LXQt's pavucontrol, with missing features from pavucontrol implemented, bug fixes and unnecessary dependencies removed.

     <https://github.com/sandsmark/pavucontrol-qt> || [pavucontrol-qt-sandsmark-git](<https://aur.archlinux.org/packages/pavucontrol-qt-sandsmark-git/>)AUR

  * **PulseAudio Volume Meter** — Simple GTK volume meter for PulseAudio. Discontinued development.

     <http://0pointer.de/lennart/projects/pavumeter/> || [pavumeter](<https://aur.archlinux.org/packages/pavumeter/>)AUR

  * **PulseEffects** — Audio effects for PulseAudio applications.

     <https://github.com/wwmm/easyeffects/tree/pulseaudio-legacy> || [pulseeffects-legacy](<https://aur.archlinux.org/packages/pulseeffects-legacy/>)AUR

  * **Volctl** — Per-application system tray applet volume control for PulseAudio.

     <https://buzz.github.io/volctl/> || [volctl](<https://aur.archlinux.org/packages/volctl/>)AUR

  * **Xfce PulseAudio Panel Plugin** — PulseAudio plugin for [Xfce](<../zh-cn/Xfce.html> "Xfce")4 panel.

     <https://goodies.xfce.org/projects/panel-plugins/xfce4-pulseaudio-plugin> || [xfce4-pulseaudio-plugin](<https://archlinux.org/packages/?name=xfce4-pulseaudio-plugin>)包

  * **pa-notify** — PulseAudio or PipeWire volume notification daemon.

     <https://github.com/ikrivosheev/pa-notify> || [pa-notify](<https://aur.archlinux.org/packages/pa-notify/>)AUR

## Configuration

默认情况下，PulseAudio 配置为自动检测所有声卡并对其进行管理。它控制所有检测到的ALSA设备，并将所有音频流重定向到自身，使PulseAudio守护程序成为中央配置点。守护程序应该基本上是开箱即用的，只需要一些小的调整。 

虽然PulseAudio通常开箱即用，只需要最少的配置，但高级用户可以通过更改默认配置文件以禁用模块或从头开始编写自己的模块来更改守护程序的几乎每个方面。 

PulseAudio作为服务器守护程序运行，可以使用客户端/服务器体系结构在系统范围内运行或基于每个用户运行。守护程序本身除了提供 API 和主机动态加载的模块之外，没有模块，什么都不做。音频路由和处理任务都由各种模块处理，包括PulseAudio的原生协议本身（由[module-native-protocol-unix](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#index22h3>)提供）。客户端通过许多协议模块之一到达服务器，这些模块将接受来自外部源的音频，通过PulseAudio路由它，并最终让它通过最后的其他模块出去。输出模块不必是实际的声音输出：它可以将流转储到文件中，将其流式传输到[Icecast](</wzh/index.php?title=Icecast&action=edit&redlink=1> "Icecast（页面不存在）")等广播服务器，甚至只是丢弃它。 

您可以在[Pulseaudio Loadable Modules](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/>)模块上找到所有可用模块的详细列表。要启用它们，您只需向 `~/.config/pulse/default.pa` 中添加一行 `load-module _module-name-from-list_` 即可。 

###  配置文件

PulseAudio 将首先在 home 目录中 `~/.config/pulse/`查找配置文件，如果找不到它们，则将应用来自系统 `/etc/pulse/` 的配置。 

**提示：**

  * 强烈建议不要编辑系统范围的配置文件，而是编辑用户配置文件。创建`~/.config/pulse` 目录，然后将系统配置文件复制到其中并根据需要进行编辑。
  * 确保使用户配置与 `/etc/pulse/`中打包文件的更改保持同步。否则，PulseAudio可能会因配置错误而拒绝启动。
  * 通常不需要将您的用户添加到 `audio` 组中，因为PulseAudio使用 [udev](<../zh-cn/Udev.html> "Udev") 和 _logind_ 来动态地向当前 "active" 用户授予访问权限。例外情况包括无外设运行计算机，以便当前没有 "active" 用户。

#### daemon.conf

这是配置守护程序本身的主配置文件。它定义了基本设置，如模块使用的默认采样率、重采样方法、实时调度以及与服务器进程相关的各种其他设置。如果不重新启动 PulseAudio 守护程序，则无法在运行时更改这些内容。对于大多数用户来说，缺省值是明智的， 有关其他信息，请参阅 [pulse-daemon.conf(5)](<https://man.archlinux.org/man/pulse-daemon.conf.5>) [man page](<../zh-cn/Man_page.html> "Man page") 。 Boolean 选项接受以下任一选项： `true`, `yes`, `on` and `1` 以及 `false`, `no`, `off` and `0`. 

**注意：** PulseAudio 不在此文件中的路径上执行波形符扩展。对任何文件使用绝对路径。

选项 | 描述   
---|---  
daemonize | 控制服务器是否将守护自身并返回。设置为 `no` 调试时，以便您可以在终端上看到调试信息。   
resample-method | 当需要在模块之间传递采样率不兼容的音频时（例如，在仅支持48kHz的硬件上播放96kHz音频），可以使用 的重采样器可以与 `pulseaudio --dump-resample-methods`一起列出。 为当前用例选择 CPU 使用率和音频质量之间的最佳权衡。 **提示：** 在某些情况下，PulseAudio将产生高CPU负载。当（单独）对多个流进行重新采样时，可能会发生这种情况。如果这是工作流程中的常见用例，则应考虑以匹配的采样率创建一个额外的接收器，然后将其馈入主接收器，仅重新采样一次。  
avoid-resampling | 使用 `avoid-resampling = yes`, PulseAudio会自动将硬件配置为应用程序使用的采样率（如果硬件支持此采样率）(需要 [PulseAudio 11+](<https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/11.0/>))  **警告：** 启用此功能可能会导致音频失真，因此默认情况下处于禁用状态，有关详细信息，请参阅 [release notes](<https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/11.0/>)  
enable-remixing | 当输入和输出具有不同的通道数（例如，将6通道电影输出到立体声接收器中）时，pulse可以重新混合所有通道（默认 `yes`），或者当`no`时只是按名称简单映射通道（左到左，从右到右，所有其他通道被忽略）   
system-instance | If set to `yes`, run the daemon as a [system-wide](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SystemWide/>) instance. [Highly discouraged](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/WhatIsWrongWithSystemWide/>) as it can introduce security issues. Useful on [Multiseat](</wzh/index.php?title=Xorg_multiseat&action=edit&redlink=1> "Xorg multiseat（页面不存在）") systems, or headless systems that have no real local users. Defaults to `no`.   
flat-volumes |  `flat-volumes` scales the device-volume with the volume of the "loudest" application. For example, raising the VoIP call volume will raise the hardware volume and adjust the music-player volume so it stays where it was, without having to lower the volume of the music-player manually. Defaults to `yes` upstream, but to `no` within Arch.  **注意：** The default behavior upstream can sometimes be confusing and some applications, unaware of this feature, can set their volume to 100% at startup, potentially blowing your speakers or your ears. This is why Arch defaults to the classic (ALSA) behavior by setting this to `no`.  
realtime-scheduling | If your [kernel](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel") supports realtime scheduling (for instance, [Realtime kernel](</wzh/index.php?title=Realtime_kernel&action=edit&redlink=1> "Realtime kernel（页面不存在）") or [Linux-ck](<../zh-cn/Linux-ck.html> "Linux-ck")), set this to `yes` to ensure PulseAudio can deliver low-latency glitch-free playback. You can adjust `realtime-priority` as well to have it use the correct priority, especially when [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）") is also running on the system.   
nice-level | Since PulseAudio runs in userspace and involves inter-process communication, audio can be subject to dropouts if the daemon does not have enough CPU time to process the audio. The default usually is enough, but can be tweaked to give pulse the wanted priority over (or below) other applications.   
exit-idle-time | If you want to run PulseAudio only when needed and use ALSA otherwise, you can set a delay in seconds after which the daemon will automatically shutdown after all clients are disconnected. Set it to -1 to disable this feature.   
log-level | When debugging, you may want to increase the logging level of the daemon to see exactly why a specific module fails to load. High logging levels will sometimes print useful information such as detected minimum latency for the system, which can then be used to tweak `default-fragments` and `default-fragment-size-msec`.   
default-sample-format | This usually does not need to be changed, but if your sound card's native format is different, performance and quality can be improved by setting the right format here.   
default-sample-rate | The default sample rate user by pulse unless overriden at module level. Change this if your sound card does not support 44100Hz or if you wish to upsample all audio. See previous note about CPU usage.   
alternate-sample-rate | To fix a common limitation where movies at 48000Hz were needlessly downsampled to 44100Hz, some modules support changing their sample rate dynamically to avoid resampling when possible. See manual for more in-depth information. This usually does not need to be changed.   
default-channels | The default number of channels when not specified. Usually do not need any change as you can configure more channels on per-module basis.   
default-fragments | Audio samples are split into multiple fragments of `default-fragment-size-msec` each. The larger the buffer is, the less likely audio will skip when the system is overloaded. On the downside this will increase the overall latency. Increase this value if you have issues.   
default-fragment-size-msec | The size in milliseconds of each fragment. This is the amount of data that will be processed at once by the daemon.   
  
#### default.pa

This file is a startup script and is used to configure modules. It is actually parsed and read after the daemon has finished initializing and additional commands can be sent at runtime using [pactl(1)](<https://man.archlinux.org/man/pactl.1>) or [pacmd(1)](<https://man.archlinux.org/man/pacmd.1>). The startup script can also be provided on the command line by starting PulseAudio in a terminal using `pulseaudio -nC`. This will make the daemon load the CLI module and will accept the configuration directly from the command line, and output resulting information or error messages on the same terminal. This can be useful when debugging the daemon or just to test various modules before setting them permanently on disk. The manual page is quite self-explanatory, consult [pulse-cli-syntax(5)](<https://man.archlinux.org/man/pulse-cli-syntax.5>) for the details of the syntax. 

**提示：**

  * Rather than being a complete copy, `~/.config/pulse/default.pa` can start with the line `.include /etc/pulse/default.pa` and then just override the defaults.
  * Run `pacmd list-sinks | grep -Ei 'index:|name:'` to list available sinks. The present default sink is marked with an asterisk.
  * Edit `~/.config/pulse/default.pa` to insert/alter the set-default-sink command using the sink's name as the numbering cannot be guaranteed repeatable.

#### client.conf

This is the configuration file read by every PulseAudio client application. It is used to configure runtime options for individual clients. It can be used to set and configure the default sink and source statically as well as allowing (or disallowing) clients to automatically start the server if not currently running. If autospawn is enabled, clients will automatically start PulseAudio if it is not already running when a client attempts to connect to it. This can be useful if you do not want PulseAudio to always be running to conserve system resources. Otherwise, you really should have it start with your X11 session. 

###  配置命令

The main command to configure a server during runtime is `pacmd`. Run `pacmd --help` for a list options, or just run `pacmd` to enter the shell interactive mode and `Ctrl+d` to exit. All modifications will immediately be applied. 

Once your new settings have been tested and meet your needs, edit the `default.pa` accordingly to make the change persistent. See [PulseAudio/Examples](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）") for some basic settings. 

**提示：** Leave the `load-module module-default-device-restore` line in the `default.pa` file untouched. It will allow you to restart the server in its default state, thus dismissing any wrong setting.

It is important to understand that the "sources" (processes, capture devices) and "sinks" (sound cards, servers, other processes) accessible and selectable through PulseAudio depend upon the current hardware "Profile" selected. These "Profiles" are those ALSA "pcms" listed by the command `aplay -L`, and more specifically by the command `pacmd list-cards`, which will include a line "index:", a list beginning "profiles:", and a line "active profile: <...>" in the output, among other things. "Profiles" correspond to different card input/output configurations, notably the number of available input/output channels. 

The "active profile" can be set with the command `pacmd set-card-profile INDEX PROFILE`, with _no_ comma separating INDEX and PROFILE, where INDEX is just the number on the line "index:" and a PROFILE name is everything shown from the beginning of any line under "profile:" to just _before_ the colon and first space, as shown by the command `pacmd list-cards`. For instance, `pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo`. 

It may be easier to select a "Profile" with a graphical tool like `pavucontrol`, under the "Configuration" tab, or KDE System Settings, "Multimedia/Audio and Video Settings", under the "Audio Hardware Setup" tab. Each audio "Card", which are those devices listed by the command `aplay -l`, or again by the command `pacmd list-cards`, will have its own selectable "Profile". When a "Profile" has been selected, the then available "sources" and "sinks" can be seen by using the commands `pacmd list-sources` and `pacmd list-sinks`. Note that the "index" of the available sources and sinks will change each time a card profile is changed. 

The selected "Profile" can be an issue for some applications, especially the Adobe Flash players, typically `/usr/lib/mozilla/plugins/libflashplayer.so` and `/usr/lib/PepperFlash/libpepflashplayer.so`. Often, these Flash players will only work when one of the Stereo profiles is selected, and otherwise, will play video with no sound, or will simply "crash". When all else fails, you might try selecting a different profile. 

Of course, when configuring some variation of Surround Sound in PulseAudio, the appropriate Surround profile will have to be selected, before Surround Sound will work, or in order to do things like remap the speaker channels. 

###  连接和认证

Since PulseAudio runs as a daemon as the current user, clients needs to know where to find the daemon socket to connect to it as well as a shared random cookie file clients use to authenticate with it. By default, clients should be able to locate the daemon without problem using environment variables, X11 root window properties and finally by trying the default location (`unix:/run/user/$ID/pulse/native`). However, if you have clients that needs to access PulseAudio outside of your X11 session like [mpd](<../zh-cn/MPD.html> "Mpd") running as a different user, you will need to tell it how to connect to your PulseAudio instance. See [PulseAudio/Examples#Allowing multiple users to share a PulseAudio daemon](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）") for a complete example. An authentication cookie containing random bytes is enabled by default to ensure audio does not leak from one user to another on a multi-user system. If you already control who can access the server using user/group permissions, you can disable the cookie by passing `auth-cookie-enabled=0` to `module-native-protocol-unix`. 

####  环境变量

These two variables are the important ones in order for libpulse clients to locate PulseAudio if you moved its socket to somewhere else. See [pulseaudio(1)](<https://man.archlinux.org/man/pulseaudio.1>) for more details and other useful environment variables clients will read. 

Variable | Definition   
---|---  
`PULSE_SERVER` | Defines where the server is. It takes a protocol prefix like `unix:` or `tcp` followed by the path or IP of the server. Example: `unix:/home/pulse/native-sock`.   
`PULSE_COOKIE` | Point this to the location of a file that contains the random cookie generated by PulseAudio. This file will be read by clients and its content sent to the server, thus the file has to be readable by all audio clients. It does not need to be the same file, as long as its content matches the one the daemon uses.   
  
####  X11 属性

PulseAudio also uses window properties on the root window of the X11 server to help find the daemon. Since environment variables cannot be modified after child processes are started, X11 properties are more flexible because they are more easily changed because they are globally shared. As long as applications receive a `DISPLAY=` environment variable, it can read the most up-to-date values. X11 properties can be queried using `xprop -root`, or with `pax11publish -d` to read pulse-specific properties. `pax11publish` can also be used to update the properties from environment variables (`pax11publish -e`, or `pax11publish -r` to remove them entirely). If possible, it is recommended to let PulseAudio do it by itself using the module-x11-publish module or the `start-pulseaudio-x11` command. The following table is there only for completeness, you should not ever need to manually set these variables by hand. 

Variable | Definition   
---|---  
`PULSE_SERVER` | String value (`xprop -root -f PULSE_SERVER 8s -set PULSE_SERVER "unix:/tmp/pulse-sock"`), works the same as the environment variable of the same name.   
`PULSE_COOKIE` | String value that contains the hexadecimal representation of the authentication cookie.   
  
##  运行

PulseAudio on Arch has `pulseaudio.socket` enabled by default for the [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户") instance. This means that PulseAudio will automatically start when needed. 

**注意：**

  * To disable `pulseaudio.socket`, make sure that `$XDG_CONFIG_HOME/systemd/user/` exists and [mask](</wzh/index.php?title=Mask&action=edit&redlink=1> "Mask（页面不存在）") the `pulseaudio.socket` [user unit](<../zh-cn/User_unit.html> "User unit").
  * Many [desktop environments](</wzh/index.php?title=Desktop_environments&action=edit&redlink=1> "Desktop environments（页面不存在）") support [XDG Autostart](<../zh-cn/XDG_Autostart.html> "XDG Autostart"). In those desktop environments, PulseAudio will be launched automatically regardless of the socket activation status.

For more information, see [PulseAudio: Running](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Running/>). 

##  停用

[Stop](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop") the `pulseaudio.socket` and `pulseaudio.service` [user unit](<../zh-cn/User_unit.html> "User unit")s. 

##  后端配置

### ALSA

**警告：** Do **not** attempt to change the ALSA configuration files while using the default PulseAudio configuration. The default configuration grabs the hardware devices directly in order to allow all the on-the-fly configurations using the GUIs. Changes to the ALSA configurations will very likely be ignored by PulseAudio and ALSA applications will break randomly while trying to access an ALSA device already used by PulseAudio. If you intend to change the ALSA configurations, also configure PulseAudio manually to output to your own ALSA device and play nice with your configuration.

If you have applications that do not support PulseAudio explicitly but rely on ALSA, these applications will try to access the sound card directly via ALSA and will therefore bypass PulseAudio. PulseAudio will thus not have access to the sound card any more. As a result, all applications relying on PulseAudio will not be working any more, leading to [this issue](</wzh/index.php?title=PulseAudio/Troubleshooting&action=edit&redlink=1> "PulseAudio/Troubleshooting（页面不存在）"). To prevent this, you will need to install the [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包 package. It contains the necessary `/etc/alsa/conf.d/99-pulseaudio-default.conf` for configuring ALSA to use PulseAudio. Also make sure that `~/.asoundrc` does not exist, as it would override the `/etc/asound.conf` file. 

Also install [lib32-libpulse](<https://archlinux.org/packages/?name=lib32-libpulse>)包 and [lib32-alsa-plugins](<https://archlinux.org/packages/?name=lib32-alsa-plugins>)包 if you run a x86_64 system and want to have sound for 32-bit [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") programs like [Wine](<../zh-cn/Wine.html> "Wine") and [Steam](<../zh-cn/Steam.html> "Steam"). 

To prevent applications from using ALSA's OSS emulation and bypassing PulseAudio (thereby preventing other applications from playing sound), make sure the module `snd_pcm_oss` is not being loaded at boot. If it is currently loaded (`lsmod | grep oss`), disable it by executing: 
    
    # rmmod snd_pcm_oss
    
####  通过 ALSA 启用 DTS

To enable PulseAudio DTS (Digital Theater System) via ALSA install [dcaenc](<https://aur.archlinux.org/packages/dcaenc/>)AUR package and enable it: 
    
    /etc/asound.conf
    
    <confdir:pcm/dca.conf>

Finally restart PulseAudio. If experience volume issues with your DTS device and/or PulseAudio, you may fix it by looking for more setting option at [dcaenc's Github](<https://github.com/darealshinji/dcaenc>). 

####  将 PulseAudio sources, sinks and mixers 暴露于 ALSA

Although [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包 contains the necessary configuration file to allow ALSA applications to use PulseAudio's default device, ALSA's `pulse` plugin is more versatile than that: 
    
    ~/.asoundrc (or /etc/asound.conf)
    
    # Create an alsa input/output using specific PulseAudio sources/sinks
    pcm.pulse-example1 {
        type pulse
        device "my-combined-sink" # name of a source or sink
        fallback "pulse-example2" # if combined not available
    }
    
    pcm.pulse-example2 {
        type pulse
        device "other-sound-card" # name of a source or sink
        # example: device "alsa_output.pci-0000_00_1b.0.analog-stereo"
    }
    
    # Create an alsa mixer using specific PulseAudio sources/sinks
    # these can be tested with "alsamixer -D pulse-example3"
    ctl.pulse-example3 {
        type pulse
        device "my-output" # name of source or sink to control
    
        # example: always control the laptop speakers:
        # device "alsa_output.pci-0000_00_1b.0.analog-stereo"
        fallback "pulse-example4" # supports fallback too
    }
    
    # Mixers also can control a specific source and sink, separately:
    ctl.pulse-example4 {
        type pulse
        sink "my-usb-headphones"
        source "my-internal-mic"
        
        # example: output to HDMI, record using internal
        sink "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1"
        source "alsa_input.pci-0000_00_1b.0.analog-stereo"
    }
    
    # These can override the default mixer (example: for pnmixer integration)
    ctl.!default {
        type pulse
        sink "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra1"
        source "alsa_input.pci-0000_00_1b.0.analog-stereo"
    }

The [source code](<https://git.alsa-project.org/?p=alsa-plugins.git;a=tree;f=pulse;hb=HEAD>) can be read to know all available options. 

####  ALSA/dmix 无需获取硬件设备

**注意：** This section describes alternative configuration, which is generally **not** recommended.

You may want to use ALSA directly in most of your applications while still being able to use applications which require PulseAudio at the same time. The following steps allow you to make PulseAudio use dmix instead of grabbing ALSA hardware device. 

  * Remove package [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包, which provides compatibility layer between ALSA applications and PulseAudio. After this your ALSA applications will use ALSA directly without being hooked by Pulse.

  * Create a configuration file in `/etc/pulse/default.pa.d/` to unload the autodetection modules and load back-end drivers statically. Add **device** parameters as follows:

    /etc/pulse/default.pa.d/load-audio-drivers-statically.pa
    
    unload-module module-udev-detect
    unload-module module-detect
    load-module module-alsa-sink **device=dmix**
    load-module module-alsa-source **device=dsnoop**

  * _Optional:_ If you use [kmix](<https://archlinux.org/packages/?name=kmix>)包 you may want to control ALSA volume instead of PulseAudio volume: set `KMIX_PULSEAUDIO_DISABLE=1` as an [environment variable](<../zh-cn/Environment_variable.html> "Environment variable").

  * Now, reboot your computer and try running ALSA and PulseAudio applications at the same time. They both should produce sound simultaneously.

    Use [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包 to control PulseAudio volume if needed.

### OSS

There are multiple ways of making OSS-only programs output to PulseAudio: 

#### ossp

Install [ossp](<https://archlinux.org/packages/?name=ossp>)包 package and start `osspd.service`. 

#### padsp wrapper

使用OSS的程序可以通过使用padsp（包含在PulseAudio中）来与PulseAudio一起使用： 
    
    $ padsp OSSprogram
    
举几个例子： 
    
    $ padsp aumix
    $ padsp sox foo.wav -t ossdsp /dev/dsp
    
您还可以添加自定义包装器脚本，如下所示： 
    
    /usr/local/bin/OSSProgram
    
    #!/bin/sh
    exec padsp /usr/bin/OSSprogram "$@"
    
Make sure `/usr/local/bin` comes before `/usr/bin` in your `PATH`. 

**注意：** This does not work when the module-udev-detect has the option `tsched=0`.

### GStreamer

Install [gst-plugins-good](<https://archlinux.org/packages/?name=gst-plugins-good>)包, or [gstreamer0.10-good-plugins](<https://aur.archlinux.org/packages/gstreamer0.10-good-plugins/>)AUR if your intended program has a legacy [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") implementation. 

### OpenAL

OpenAL Soft 应默认使用 PulseAudio，但可以显式配置为这样做： 
    
    /etc/openal/alsoft.conf
    
    drivers=pulse,alsa

默认情况下，OpenAL 不允许 pulseaudio 将音频流移动到其他设备。要更改此设置，请添加允许移动选项： 
    
    /etc/openal/alsoft.conf
    
    [pulse]
    allow-moves=true

### libao

编辑 libao 配置文件： 
    
    /etc/libao.conf
    
    default_driver=pulse

请务必删除 alsa 驱动程序的 `dev=default` 选项或调整它以指定特定的 Pulse sink 名称或编号。 

**注意：** You could possibly also keep the libao standard of outputting to the _alsa_ driver and its default device if you install [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包 since the ALSA default device then **is** PulseAudio.

##  Audio 后期处理

### PulseEffects

[PulseEffects](<https://github.com/wwmm/easyeffects/tree/pulseaudio-legacy>) is a GTK advanced utility for applying several audio effects (e.g. Noise reduction, Equalizer etc.) to audio input and output. 

**注意：** PulseEffects new version ([EasyEffects](<../zh-cn/PipeWire.html#EasyEffects> "PipeWire")) only supports Pipewire. You need to install the legacy version ([pulseeffects-legacy](<https://aur.archlinux.org/packages/pulseeffects-legacy/>)AUR or [pulseeffects-legacy-git](<https://aur.archlinux.org/packages/pulseeffects-legacy-git/>)AUR) to use it with PulseAudio.

You may need to also install its optional dependency [lsp-plugins](<https://archlinux.org/packages/?name=lsp-plugins>)包 in order to get plugins to work. If PulseEffects plugins are greyed out after installing plugins, trying to start the daemon produces an error, or no devices are shown in the _Settings > PulseAudio_ tab, consider clearing the cache as shown in [[3]](<https://github.com/wwmm/easyeffects/issues/488#issuecomment-484101349>). 

A collection of PulseEffects presets can be found in [community presets](<https://github.com/wwmm/easyeffects/wiki/Community-presets>). 

###  均衡

If you want to use a different equalizer rather that the one integrated in [#PulseEffects](<#PulseEffects>), there are the following options. 

####  LADSPA 模块

Install [pulseaudio-equalizer-ladspa](<https://archlinux.org/packages/?name=pulseaudio-equalizer-ladspa>)包, an equalizer based on LADSPA [swh-plugins](<https://archlinux.org/packages/?name=swh-plugins>)包. Launch `pulseaudio-equalizer-gtk` GUI and tweak the parameters to match your expectations. 

####  集成模块

PulseAudio has an integrated 10-band equalizer system. In order to use it, install [pulseaudio-equalizer](<https://archlinux.org/packages/?name=pulseaudio-equalizer>)包 and read the following instructions. 

**警告：** PulseAudio equalizer module is considered [unstable and might be removed from PulseAudio](<https://lists.freedesktop.org/archives/pulseaudio-discuss/2014-March/020174.html>).

Load the equalizer sink and dbus-protocol module 
    
    $ pactl load-module module-equalizer-sink
    $ pactl load-module module-dbus-protocol
    
To start the GUI, run `qpaeq`. 

**注意：** If qpaeq has no effect, install [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包 and change "ALSA Playback on" to "FFT based equalizer on ..." while the media player is running.

To load the equalizer and dbus module on every boot, create a _.pa_ file in `/etc/pulse/default.pa.d/` or edit `~/.config/pulse/default.pa` and add the following lines: 
    
    ### Load the integrated PulseAudio equalizer and D-Bus module
    load-module module-equalizer-sink
    load-module module-dbus-protocol
    
**注意：** The equalizer sink needs to be loaded after the master sink is already available.

###  动态范围压缩

[Dynamic range compression](<https://en.wikipedia.org/wiki/Dynamic_range_compression> "wikipedia:Dynamic range compression") can be done with [#PulseEffects](<#PulseEffects>). Anyway PulseEffects might introduce much overhead and latency to audio stream, so if you only need a compression effect and a minor load on the system, other options are available using a [module-ladspa-sink](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#module-ladspa-sink>). 

####  Steve Harris 插件

Steve Harris LADSPA is a set of plugins containing various compression modules. Install [swh-plugins](<https://archlinux.org/packages/?name=swh-plugins>)包 and edit the configuration as the following 
    
    ~/.config/pulse/default.pa
    
    .include /etc/pulse/default.pa
    
    set-default-sink your_card_sink_name
    
    load-module module-ladspa-sink sink_name=shw_sc4 sink_master=your_card_sink_name plugin=sc4_1882 label=sc4 control=,,,,,,,,
    set-default-sink shw_sc4

You have to specify your card sink name, get it from `pacmd list-sinks`. In order to apply the changes, stop and restart Pulseaudio. The above configuration has empty control options using the default values. 

To tweak the module with custom control parameters, fill them respecting the right order. 

Control option | Description   
---|---  
RMS/peak (0/1) | The blanace between the RMS and peak envelope followers. RMS is generally better for subtle, musical compression and peak is better for heavier, fast compression and percussion.   
Attack time (ms) | The attack time in milliseconds.   
Release time (ms) | The release time in milliseconds.   
Threshold level (dB) | The point at which the compressor will start to kick in.   
Ratio (1:n) | The gain reduction ratio used when the signal level exceeds the threshold. 1 means no compression; higher values stronger compression.   
Knee radius (dB) | The distance from the threshold where the knee curve starts.   
Makeup gain (dB) | Controls the gain of the makeup input signal in decibels.   
Amplitude (dB) | The level of the input signal, in decibels.   
Gain reduction (dB) | The degree of gain reduction applied to the input signal, in decibels.   
  
Other plugins can be found in [Steve Harris' LADSPA Plugin Documentation](<http://plugin.org.uk/ladspa-swh/docs/ladspa-swh.html>). 

####  Calf 插件

For a more professional compressor, you can use the one developed by [Calf Studio Gear](<https://calf-studio-gear.org/>). Install [calf-ladspa](<https://aur.archlinux.org/packages/calf-ladspa/>)AUR and edit the configuration as the following 
    
    ~/.config/pulse/default.pa
    
    .include /etc/pulse/default.pa
    
    set-default-sink your_card_sink_name
    
    load-module module-ladspa-sink sink_name=calf_comp_x2 sink_master=your_card_sink_name plugin=veal label=Compressor control=,,,,,,,,,,
    set-default-sink calf_comp_x2

The plugin has 11 control options. If you want to insert custom values, read the following table and do not forget to specify them in the right order. 

Control option | Default | Min | Max | Type | Info   
---|---|---|---|---|---  
Bypass | 0 | 0 | 1 | Bool |   
Level in | 1 | 0.015625 | 64 | Float db |   
Threshold | 0.125 | 0.000976563 | 1 | Float dbFs | For example, to set -18 db, the right value is 10^(-18/20) = 0.158   
Ratio | 2 | 1 | 20 | Float |   
Attack | 20 | 0.01 | 2000 | Float ms |   
Release | 250 | 0.01 | 2000 | Float ms |   
Makeup | 1 | 1 | 64 | Float db |   
Knee | 2.828427125 | 1 | 8 | Float db |   
RMS/Peak | 0 | 0 | 1 | Bool | 0 = RMS; 1 = Peak   
Stereo Link | 0 | 0 | 1 | Bool | 0 = Average; 1 = Max   
Mix | 1 | 0 | 1 | Float | Percentage   
To understand the meaning of every single option, read the [Calf Compressor Documentation](<https://calf-studio-gear.org/doc/Compressor.html>).   
  
###  麦克风回声/噪音消除

Arch 默认不会加载 PulseAudio 的回声消除模块，因此，我们需要在`/etc/pulse/default.pa.d/`中添加它。首先，你可以使用 `pacmd` 并输入`list-modules`。如果你无法找到 `name: <module-echo-cancel>`，你就需要创建一个。 
    
    /etc/pulse/default.pa.d/noise-cancellation.pa
    
    ### 启用回声消除
    load-module module-echo-cancel use_master_format=1 aec_method=webrtc aec_args="analog_gain_control=0\ digital_gain_control=1" source_name=echoCancel_source sink_name=echoCancel_sink
    set-default-source echoCancel_source
    set-default-sink echoCancel_sink

然后重启 Pulseaudio 
    
    $ pulseaudio -k
    $ pulseaudio --start
    
然后可以使用 `pavucontrol` 来查看模块是否被启用了。在 `输入设备` 一栏下，应该已经出现了一个 `Echo-Cancel Source Stream from`

Turning on `beamforming=1` in the aec_args can also significantly reduce background noise if you have more than one microphone (which is common on many new laptops). However, beamforming requires specifying your `mic_geometry` (see below). 

If you want existing streams to be automatically moved to the new sink and source, you have to load the [module-switch-on-connect](<../zh-cn/%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA.html#%E8%AE%BE%E7%BD%AE%E8%87%AA%E5%8A%A8%E8%BF%9E%E6%8E%A5> "蓝牙耳机") with `ignore_virtual=no` before. 

**注意：** If you plug in a USB sound card or headset, or you have for example a 5.1 Speaker configuration and plug in a headset on your front audio connectors after you have loaded the `module-echo-cancel`, you have to manually unload and load the `module-echo-cancel` again, because unfortunately there is no way to tell the module that it should automatically switch to the new default 'source_master' and 'source_sink'. See [[4]](<https://gitlab.freedesktop.org/pulseaudio/pulseaudio/issues/196>).

####  Possible 'aec_args' for 'aec_method=webrtc'

Here is a list of possible 'aec_args' for 'aec_method=webrtc' with their default values [[5]](<https://github.com/pulseaudio/pulseaudio/blob/master/src/modules/echo-cancel/webrtc.cc>)[[6]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#index45h3>): 

  * `analog_gain_control=1` \- Analog AGC - 'Automatic Gain Control' done over changing the volume directly - Will most likely lead to [distortions](</wzh/index.php?title=PulseAudio/Troubleshooting&action=edit&redlink=1> "PulseAudio/Troubleshooting（页面不存在）").
  * `digital_gain_control=0` \- Digital AGC - 'Automatic Gain Control' done in post processing (higher CPU load).
  * `experimental_agc=0` \- Allow enabling of the webrtc experimental AGC mechanism.
  * `agc_start_volume=85` \- Initial volume when using AGC - Possible values 0-255 - A too low initial volume may prevent the AGC algorithm from ever raising the volume high enough [[7]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/9.0/>).
  * `high_pass_filter=1` \- ?
  * `noise_suppression=1` \- Noise suppression.
  * `voice_detection=1` \- VAD - Voice activity detection.
  * `extended_filter=0` \- The extended filter is more complex and less sensitive to incorrect delay reporting from the hardware than the regular filter. The extended filter mode is disabled by default, because it seemed produce worse results during double-talk [[8]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/9.0/>). Enable this option if your microphone or speaker has a larger latency, for example, if you use a wireless microphone or some HDMI TVs as speaker.
  * `intelligibility_enhancer=0` \- Some bits for webrtc intelligibility enhancer.
  * `drift_compensation=0` \- Drift compensation to allow echo cancellation between different devices (such as speakers on your laptop and the microphone on your USB webcam). - only possible with "mobile=0".
  * `beamforming=0` \- This can significantly reduce background noise. See [[9]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Modules/#index45h3>)[[10]](<https://arunraghavan.net/2016/06/beamforming-in-pulseaudio/>)
    * `mic_geometry=x1,y1,z1,x2,y2,z2` \- Only with "beamforming=1".
    * `target_direction=a,e,r` \- Only with "beamforming=1". Note: If the module does not want to load with this argument, set azimuth (a) to the desired value, but set elevation (e) and radius (r) to 0.
  * `mobile=0` \- ? 
    * `routing_mode=speakerphone` \- Possible Values "quiet-earpiece-or-headset,earpiece,loud-earpiece,speakerphone,loud-speakerphone" - only valid with "mobile=1".
    * `comfort_noise=1` \- ? - only valid with "mobile=1".

####  在某些应用程序中禁用音频后处理

If you are using the [module-echo-cancel](<#Microphone_echo/noise_cancellation>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节], you probably do not want other applications to do additional audio post processing. Here is a list for disabling audio post processing in following applications: 

  * Mumble: 
    1. Configure -> Settings -> Check 'Advanced' check box -> Audio Input
    2. Echo: Select 'Disabled'
    3. Noise Suppression: Set slider to 'Off'
    4. Max. Aplification: Set slider to '1.0'
  * TeamSpeak: 
    1. Tools -> Options -> Capture
    2. Uncheck: 'Typing attenuation', 'Remove background noise', 'Echo cancellation' and 'Echo reduction (Ducking)'
  * Firefox: see [Firefox tweaks#Disable WebRTC audio post processing](</wzh/index.php?title=Firefox_tweaks&action=edit&redlink=1> "Firefox tweaks（页面不存在）")
  * Steam: 
    1. In window "Friends List" -> Manage friends list settings (gear symbol) -> VOICE -> Show Advanced Settings
    2. Set the following sliders to "OFF": "Echo cancellation", "Noise cancellation", "Automatic volume/gain control"
  * Skype: 
    1. Tools -> Settings... -> Audio & Video -> Microphone -> Automatically adjust microphone settings -> off

####  用于重新加载回声消除模块的脚本

Since the module-echo-cancel is not always needed, or must be reloaded if the source_master or sink_master has changed, it is nice to have a easy way to load or reload the module-echo-cancel. 

[Create](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Create") the following script and make it [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"): 
    
    echoCancelEnable.sh
    
    #!/bin/sh
    aecArgs="$*"
    # If no "aec_args" are passed on to the script, use this "aec_args" as default:
    [ -z "$aecArgs" ] && aecArgs="analog_gain_control=0 digital_gain_control=1"
    newSourceName="echoCancelSource"
    newSinkName="echoCancelSink"
    
    # "module-switch-on-connect" with "ignore_virtual=no" (needs PulseAudio 12 or higher) is needed to automatically move existing streams to a new (virtual) default source and sink.
    if ! pactl list modules short | grep "module-switch-on-connect.*ignore_virtual=no" >/dev/null 2>&1; then
    	echo Load module \"module-switch-on-connect\" with \"ignore_virtual=no\"
    	pactl unload-module module-switch-on-connect 2>/dev/null
    	pactl load-module module-switch-on-connect ignore_virtual=no
    fi
    
    # Reload "module-echo-cancel"
    echo Reload \"module-echo-cancel\" with \"aec_args=$aecArgs\"
    pactl unload-module module-echo-cancel 2>/dev/null
    if pactl load-module module-echo-cancel use_master_format=1 aec_method=webrtc aec_args=\"$aecArgs\" source_name=$newSourceName sink_name=$newSinkName; then
    	# Set a new default source and sink, if module-echo-cancel has loaded successfully.
    	pacmd set-default-source $newSourceName
    	pacmd set-default-sink $newSinkName
    fi
    
To run the script easily from the graphical environment, you can create a [desktop launcher](</wzh/index.php?title=Desktop_launcher&action=edit&redlink=1> "Desktop launcher（页面不存在）") for it. 

###  递归神经网络噪声抑制 (RNNoise)

Installing the package [noise-suppression-for-voice](<https://archlinux.org/packages/?name=noise-suppression-for-voice>)包 will allow real-time noise suppression based on RNNoise: Learning Noise Suppression [[11]](<https://jmvalin.ca/demo/rnnoise/>). Configuration details can be found on the projects Github site [[12]](<https://github.com/werman/noise-suppression-for-voice>). One can install Cadmus ([cadmus-deb](<https://aur.archlinux.org/packages/cadmus-deb/>)AUR or [cadmus-appimage](<https://aur.archlinux.org/packages/cadmus-appimage/>)AUR) which is a GUI frontend for @werman's Pulse Audio real-time noise suppression plugin. 

Another alternative is [noisetorch](<https://aur.archlinux.org/packages/noisetorch/>)AUR which is also build on top of RNNoise. There is not only input noise cancellation but also an output. 

##  应用

### QEMU

Refer to [QEMU#Host](<../zh-cn/QEMU.html#Host> "QEMU")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] for a detailed guide on how to configure pulseaudio within [QEMU](<../zh-cn/QEMU.html> "QEMU"). 

### AlsaMixer.app

Make [alsamixer.app](<https://aur.archlinux.org/packages/alsamixer.app/>)AUR dockapp for the [windowmaker](<https://aur.archlinux.org/packages/windowmaker/>)AUR use pulseaudio, e.g.: 
    
    $ AlsaMixer.app --device pulse
    
Here is a two examples where the first one is for ALSA and the other one is for pulseaudio. You can run multiple instances of it. Use the `-w` option to choose which of the control buttons to bind to the mouse wheel. 
    
    # AlsaMixer.app -3 Mic -1 Master -2 PCM --card 0 -w 1
    # AlsaMixer.app --device pulse -1 Capture -2 Master -w 2
    
**注意：** It can use only those output sinks that set as default.

### XMMS2

Make it switch to pulseaudio output: 
    
    $ nyxmms2 server config output.plugin pulse
    
and to alsa: 
    
    $ nyxmms2 server config output.plugin alsa
    
To make xmms2 use a different output sink, e.g.: 
    
    $ nyxmms2 server config pulse.sink alsa_output.pci-0000_04_01.0.analog-stereo.monitor
    
See also the official guide [[13]](<https://xmms2.org/wiki/Using_the_application>). 

### KDE Plasma Workspaces and Qt4

PulseAudio will automatically be used by KDE/Qt4 applications. It is supported by default in the KDE sound mixer. For more information see the [KDE page in the PulseAudio wiki](<https://www.freedesktop.org/wiki/Software/PulseAudio/Desktops/KDE/>). 

One useful tidbit from that page is that `load-module module-device-manager` should be loaded. This usually happens automatically at login through the script `/usr/bin/start-pulseaudio-x11`; if you find that the module is not loaded automatically you can consider adding it manually to a configuration file in `/etc/pulse/default.pa.d/`. See [#Switch on connect](<#Switch_on_connect>) for possible conflicts with the `module-switch-on-connect`. 

If the phonon-gstreamer backend is used for [Phonon](</wzh/index.php?title=Phonon&action=edit&redlink=1> "Phonon（页面不存在）"), GStreamer should also be configured as described in [#GStreamer](<#GStreamer>). 

### Audacious

In order to use PulseAudio, set Edit → Preferences… → Devices → Playback → Device in Audacious to “default” or “pulse”. These devices are added to the drop-down list by [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包. 

###  Music Player Daemon (MPD)

[Configure](<https://mpd.wikia.com/wiki/PulseAudio>) [MPD](<../zh-cn/MPD.html> "MPD") to use PulseAudio. See also [MPD/Tips and Tricks#PulseAudio](</wzh/index.php?title=MPD/Tips_and_Tricks&action=edit&redlink=1> "MPD/Tips and Tricks（页面不存在）"). 

### MPlayer

[MPlayer](<../zh-cn/MPlayer.html> "MPlayer") natively supports PulseAudio output with the `-ao pulse` option. It can also be configured to default to PulseAudio output, in `~/.mplayer/config` for per-user, or `/etc/mplayer/mplayer.conf` for system-wide: 
    
    /etc/mplayer/mplayer.conf
    
    ao=pulse

### mpv

[mpv](<../zh-cn/Mpv.html> "Mpv") supports PulseAudio same as written for [#MPlayer](<#MPlayer>). Configuration in `~/.config/mpv/mpv.conf` per-user, or `/etc/mpv/mpv.conf` system-wide. 

### guvcview

[guvcview](<https://archlinux.org/packages/?name=guvcview>)包 when using the PulseAudio input from a [Webcam](</wzh/index.php?title=Webcam&action=edit&redlink=1> "Webcam（页面不存在）") may have the audio input suspended resulting in no audio being recorded. You can check this by executing: 
    
    $ pactl list sources
    
If the audio source is "suspended" then create the folowing _.pa_ file: 

`/etc/pulse/default.pa.d/no-module-suspend-on-idle.pa`

And then either restarting PulseAudio or your computer will only idle the input source instead of suspending it. guvcview will then correctly record audio from the device. 

##  网络 audio

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[PulseAudio/Examples#PulseAudio over network](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）")。**

**附注：** No need for two separate sections.（在 [Talk:PulseAudio](<../zh-cn/Talk:PulseAudio.html>) 中讨论）

One of PulseAudio's unique features is its ability to stream audio from clients over TCP to a server running the PulseAudio daemon reliably within a LAN. Ensure that client and server systems agree on the time (i.e., use NTP), or audio streams may be choppy or may not work at all. For a more detailed guide visit the [Official PulseAudio Documentation](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/>)

Enable the TCP module on the server(the computer that actually outputs sound), create the folowing _.pa_ file: 
    
    /etc/pulse/default.pa.d/tcp.pa
    
    load-module module-native-protocol-tcp
    
Or you can use the `paprefs` gui application (root is not required). Go to _Network Server > Enable network access to local sound devices_. 

To make sure module-native-protocol-tcp is loaded on the server, you can use: 
    
    $ pacmd list-modules | grep module-native-protocol-tcp
    
It is a requirement that both the client and server share the same cookie. Ensure that the clients and server share the same cookie file found under `~/.config/pulse/cookie`. It does not matter whose cookie file you use (the server or a client's), just that the server and client(s) share the same one. 

If it is undesirable to copy the cookie file from clients, anonymous clients can access the server by passing `auth-anonymous` to `module-native-protocol-tcp` on the server (again in `/etc/pulse/default.pa.d/`): 
    
    load-module module-native-protocol-tcp auth-anonymous=1
    
It is also possible to authenticate based on client IP address: 
    
    load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1;192.168.0.0/24
    
Change the LAN IP subnet to match that of those clients you wish to have access to the server. 

### Starting system-wide on boot

The PulseAudio daemon normally starts as a user service when a user logs in and attempts to play some sort of audio. For running a dedicated PulseAudio server accepting client connections over TCP, the daemon must be started on boot as a system service. Note [that in most desktop use cases, system mode likely is not the right choice](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/WhatIsWrongWithSystemWide/>). 

To run PulseAudio in a system mode, first we need to set up users and groups needed by system-wide PulseAudio server instance [[14]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/SystemWide/>): 

  1. Add user pulse. PulseAudio daemon switches to this user after starting. 
         
         # useradd -d /var/run/pulse -s /usr/bin/nologin -G audio pulse

  2. Optionally add user pulse to the bluetooth group, if you have it (bluez) and want PulseAudio to use bluetooth. 
         
         # usermod -aG bluetooth pulse

  3. Add group pulse-access. This group is used by PulseAudio server for access control. 
         
         # groupadd pulse-access

  4. Add users to pulse-access group, if you want them to have access to the system-wide PulseAudio instance. 
         
         # usermod -aG pulse-access root

Create the service `pulseaudio.service` in `/etc/systemd/system` containing the following: 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** The service runs as `root`, not as the `pulse` user.（在 [Talk:PulseAudio](<../zh-cn/Talk:PulseAudio.html>) 中讨论）

    /etc/systemd/system/pulseaudio.service
    
    [Unit]
    Description=Sound Service
     
    [Service]
    # Note that notify will only work if --daemonize=no
    Type=notify
    ExecStart=/usr/bin/pulseaudio --daemonize=no --exit-idle-time=-1 --disallow-exit=true --system --disallow-module-loading
    Restart=always
     
    [Install]
    WantedBy=default.target

Then [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `pulseaudio.service` at the system level. You will also need to disable the user-level PulseAudio service across the whole system: 
    
    # systemctl --global mask pulseaudio.socket
    
This is necessary even if you are accessing the system over SSH, to make sure the user-level PulseAudio service will never start. 

###  选择服务器

For a single shell or command you can set the environment variable `$PULSE_SERVER` to the host name or IP address of the desired PulseAudio server. 
    
    $ env PULSE_SERVER=_server-hostname-or-ip_ mplayer test.mp3
    
Alternatively you can create or modify `~/.pulse/client.conf` or `/etc/pulse/client.conf` to set a default-server persistently. 
    
    default-server = _server-hostname-or-ip_
    
It is also possible to specify multiple servers separated by spaces which are subsequently tried by PulseAudio[[15]](<https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/ServerStrings/>): 
    
    default-server = _server1_ _backup_
    
##  提示和技巧

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[PulseAudio/Examples](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）")。**

**附注：** Same topic.（在 [Talk:PulseAudio](<../zh-cn/Talk:PulseAudio.html>) 中讨论）

###  键盘控制音量

See [Keyboard shortcuts#Xorg](<../zh-cn/Keyboard_shortcuts.html#Xorg> "Keyboard shortcuts") to bind the following commands to your volume keys: `XF86AudioRaiseVolume`, `XF86AudioLowerVolume` and `XF86AudioMute`. 

First find out which sink corresponds to the audio output you would like to control. To list available sinks: 
    
    $ pactl list sinks short
    
Suppose sink 0 is to be used, to raise the volume: 
    
    $ sh -c "pactl set-sink-mute 0 false ; pactl set-sink-volume 0 +5%"
    
To lower the volume: 
    
    $ sh -c "pactl set-sink-mute 0 false ; pactl set-sink-volume 0 -5%"
    
To mute/unmute the volume: 
    
    $ pactl set-sink-mute 0 toggle
    
To mute/unmute the microphone: 
    
    $ pactl set-source-mute 1 toggle
    
**提示：**

  * To have keyboard shortcuts operate always on the default sink, specify `@DEFAULT_SINK@` as the sink number, for example `pactl set-sink-mute @DEFAULT_SINK@ toggle`.
  * For more advanced control, such as limiting the maximum volume, consider using one of the [console front-ends](<#Console>)[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节].

###  从非交互式 shell 播放音频 (systemd service, cron)

Set `XDG_RUNTIME_DIR` before the command (replace `_user_id_` with the ID of the user running PulseAudio): 
    
    $ XDG_RUNTIME_DIR=/run/user/_user_id_ paplay /usr/share/sounds/freedesktop/stereo/complete.oga
    
Or use `machinectl`: 
    
    # machinectl shell .host --uid=_user_id_ /usr/bin/paplay /usr/share/sounds/freedesktop/stereo/complete.oga
    
###  X11 Bell 事件

To get pulseaudio to handle X11 bell events, run the following commands after the X11 session has been started: 
    
    $ pactl upload-sample /usr/share/sounds/freedesktop/stereo/bell.oga bell-window-system
    $ pactl load-module module-x11-bell display=$DISPLAY
    
Or use configuration files `/etc/pulse/default.pa.d/` or `~/.config/pulse/default.pa`: 
    
    ~/.config/pulse/default.pa
    
    .include /etc/pulse/default.pa
    
    # audible bell
    load-sample-lazy bell-window-system /usr/share/sounds/freedesktop/stereo/bell.oga
    load-module module-x11-bell

To adjust the volume of the X11 bell, run the following command: 
    
    $ xset b 100
    
100 is a percentage. This requires the [xorg-xset](<https://archlinux.org/packages/?name=xorg-xset>)包 package. See [Autostarting](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting") for a way to run these commands automatically when the X11 session is started. 

### Switch on connect

This is a default enabled module used to switch the output sound to the newly connected device. For example, if you plug in a USB headset, the output will be switched to that. If you unplug it, the output will be set back to the last device. This used to be quite buggy but got a lot of attention in PulseAudio 8.0 and should work quite well now. 

**注意：** It does not work with some devices, see [PulseAudio/Troubleshooting#ALSA channels mute when headphones are plugged/unplugged improperly](</wzh/index.php?title=PulseAudio/Troubleshooting&action=edit&redlink=1> "PulseAudio/Troubleshooting（页面不存在）").

###  用于切换模拟输出的脚本

Some sound cards present the option of multiple analog outputs, being switchable through using Pulseaudio profiles. But switching manually can become a chore, so you can use the following commands to switch it: 
    
    $ pactl set-sink-port 'number of the card' 'port'
    
This will set the default output to whatever port you chose. Example: 
    
    $ pactl set-sink-port 0 "analog-output;output-speaker" 
    
The values can be easily obtained using: 
    
    $ pactl list
    
Current output can be obtained through: 
    
    $ pactl list sinks | grep "active profile"| cut -d ' ' -f 3-
    
This process can be automated through a simple script. This script then can be given a shortcut by the user: 
    
    ~/pa.sh (or anything the user wants)
    
    #!/bin/sh
    # This script uses kdialog notification to warn the user of the currently swapped to profile. User could adapt it to their needs or change it.
    
    CURRENT_PROFILE=$(pactl list sinks | grep "active profile"| cut -d ' ' -f 3-)
    
    if [ "$CURRENT_PROFILE" = "analog-output;output-speaker" ] ; then
            pactl set-sink-port 0 "analog-output;output-headphones-1"
            kdialog --title "Pulseaudio" --passivepopup "Headphone" 2 & 
    else 
            pactl set-sink-port 0 "analog-output;output-speaker"      
            kdialog --title "Pulseaudio" --passivepopup  "Speaker" 2 &
    fi
    
This script is intended to swap between two profiles. First checking the current profile then swapping it. Users are required to change the field 'active profile' according to the language pactl reports. Users might need to change the number of the card and the output to fit their machine. 

###  禁止媒体进入语音呼叫时静音 (module-role-cork)

When entering a voice call (e.g. in Microsoft Teams, maybe others too) any media applications might be muted. To disable this behaviour you can simply disable this module in PulseAudio configuration: 
    
    /etc/pulse/default.pa.d/no-cork.pa
    
    unload-module module-role-cork
    
##  高级配置和使用案例

See [PulseAudio/Examples](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）"). 

##  疑难解答

参阅 [PulseAudio/疑难解答](<../zh-cn/PulseAudio/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "PulseAudio/疑难解答"). 

##  参考文件

  * [PulseAudio official website](<https://www.freedesktop.org/wiki/Software/PulseAudio/>), including documentation
  * [Pulseaudio under the hood](<https://gavv.github.io/articles/pulseaudio-under-the-hood/>)
