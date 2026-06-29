**翻译状态：**

  * 本文（或部分内容）译自 [PipeWire](<https://wiki.archlinux.org/title/PipeWire> "arch:PipeWire")，最近一次同步于 2024-02-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/PipeWire?diff=0&oldid=795568>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PipeWire_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:PipeWire#](<../zh-cn/Talk:PipeWire.html>) 中讨论）

相关文章

  * [PipeWire/Examples](</wzh/index.php?title=PipeWire/Examples&action=edit&redlink=1> "PipeWire/Examples（页面不存在）")
  * [WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber")

[PipeWire](<https://pipewire.org>) 是一个新的底层多媒体框架。 它旨在以最低的延迟为音频和视频提供录制和播放功能，并支持基于 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")、[JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）")、[ALSA](<../zh-cn/ALSA.html> "ALSA") 和 [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") 的应用程序。 

基于该框架的守护进程可以配置为音频服务器(具有 PulseAudio 和 JACK 特性)和视频录制服务器。 

PipeWire 还支持像 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 这样的容器，不依赖于 `audio` 和 `video` [用户组](<../zh-cn/User_group.html> "User group")。 相反，它采用了类似于 [Polkit](<../zh-cn/Polkit.html> "Polkit")的安全模式，向 Flatpak 或 Wayland 请求许可以录制屏幕或音频。 

##  安装

可以从官方软件库[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pipewire](<https://archlinux.org/packages/?name=pipewire>)包 程序。 也有[lib32-pipewire](<https://archlinux.org/packages/?name=lib32-pipewire>)包 的32位库对于 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 进行支持 

Pipewire 使用 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")管理服务器并自动激活socket。 

可以选择安装 [pipewire-docs](<https://archlinux.org/packages/?name=pipewire-docs>)包 来查看文档。 

Pipewire 可以作为其他音频服务器的直接替代品。更多详细信息请参见[#声音](<#%E5%A3%B0%E9%9F%B3>)。 

###  会话（Session）管理

像 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）")一样，PipeWire 内部没有实现连接逻辑。 监视新 streams 并将其连接到适当的输出设备或应用程序的负担留给称为会话管理器的外部组件。 

#### WirePlumber

[WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber") 是推荐的会话管理器，采用模块化设计，通过 Lua 插件实现实际管理功能。 

默认配置文件位于 `/usr/share/wireplumber`。推荐通过在 `/etc/wireplumber` 或 `~/.config/wireplumber` 中添加片段配置来覆盖特定设置。[[1]](<https://pipewire.pages.freedesktop.org/wireplumber/daemon/locations.html#config-locations>)

WirePlumber 在 0.5 版本中将配置格式从 `.lua` 改为 `.conf`。迁移指南参见：<https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/migration.html#config-migration>

#### PipeWire Media Session

[pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 已弃用且不再推荐使用，该组件主要作为测试用例和会话管理器开发参考。 

###  GUI图形界面

  * **coppwr** — PipeWire 底层控制与诊断工具

     <https://github.com/dimtpap/coppwr> || [coppwr](<https://aur.archlinux.org/packages/coppwr/>)AUR

  * **Helvum** — 基于 GTK 的 PipeWire 接插板工具，灵感源自 JACK 的 _catia_ 。不支持连线保存

     <https://gitlab.freedesktop.org/pipewire/helvum> || [helvum](<https://archlinux.org/packages/?name=helvum>)包

  * **qpwgraph** — 基于 Qt 的 PipeWire 路由接插板，灵感源自 JACK 的 QjackCtl。支持连线保存

     <https://gitlab.freedesktop.org/rncbc/qpwgraph> || [qpwgraph](<https://archlinux.org/packages/?name=qpwgraph>)包

  * **pwvucontrol** — PipeWire 音量控制工具，可作为 pavucontrol 替代品

     <https://github.com/saivert/pwvucontrol> || [pwvucontrol](<https://aur.archlinux.org/packages/pwvucontrol/>)AUR

  * **sonusmix** — PipeWire 音频路由工具

     <https://codeberg.org/sonusmix/sonusmix> || [sonusmix](<https://aur.archlinux.org/packages/sonusmix/>)AUR

##  配置

PipeWire 软件包在 `/usr/share/pipewire` 中提供了一组初始配置文件。不应直接编辑这些文件，因为包更新将覆盖所做的更改。要配置 PipeWire，可以将文件从 `/usr/share/pipewire` 复制到备用系统配置目录位置 `/etc/pipewire`或用户目录 `~/.config/pipewire`。具有较高优先级的目录中的同名文件会使类似文件被忽略。 [[2]](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config-PipeWire#configuration-file-pipewireconf>)

### Profiles

Pipewire 带来了一个PulseAudio 配置以外的自定义的 "Pro Audio" 配置文件, 可通过 pavucontrol进行选择。其效果如下所述：<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/FAQ#what-is-the-pro-audio-profile>

##  用法

###  声音

PipeWire 可以用作音频服务器，类似于 PulseAudio 和 JACK，它旨在通过为JACK客户端提供PulseAudio兼容的服务器实现和ABI兼容库来取代PulseAudio和JACK。有关详细信息，请参阅博客文章[PipeWire Late Summer Update 2020](<https://blogs.gnome.org/uraeus/2020/09/04/pipewire-late-summer-update-2020/>)。 

首先，安装 [pipewire-audio](<https://archlinux.org/packages/?name=pipewire-audio>)包。然后根据音频客户端的类型，可能还需要执行一些额外的步骤。 

####  ALSA 客户端

安装 [pipewire-alsa](<https://archlinux.org/packages/?name=pipewire-alsa>)包 (如果安装了[pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包需要删掉它) 以使用 ALSA API 通过 PipeWire 路由所有应用程序。 

####  PulseAudio 客户端

安装 [pipewire-pulse](<https://archlinux.org/packages/?name=pipewire-pulse>)包。它将代替 [pulseaudio](<https://archlinux.org/packages/?name=pulseaudio>)包 和 [pulseaudio-bluetooth](<https://archlinux.org/packages/?name=pulseaudio-bluetooth>)包。重新启动、重新登录或 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `pipewire-pulse.service` [user unit](<../zh-cn/User_unit.html> "User unit") 以查看效果。 

通常，不需要进一步的操作，应用应作为用户服务自动启用`pipewire-pulse.socket`。要检查替换是否正常工作，请运行以下命令并查看输出： 
    
    $ pactl info
    
    ...
    Server Name: PulseAudio (on PipeWire 0.3.32)
    ...

[pactl(1)](<https://man.archlinux.org/man/pactl.1>) 命令由 PulseAudio 客户端库（[libpulse](<https://archlinux.org/packages/?name=libpulse>)包）提供，该库会作为依赖项随 _pipewire-pulse_ 自动安装。 

#####  调节全局或独立声道音量

调节输出声道音量时，需通过 `pactl get-sink-volume {sink`} 指定目标设备，可使用： \- 上文 _Default Sink:_ 或下文 _Name:_ 的值 \- 默认设备占位符 _@DEFAULT_SINK@_ \- 设备编号 _Sink #_ （如下例中的 _1_ ） 
    
    $ pactl list sinks | grep -B1 -A9 State:
    
    Sink #1
            State: RUNNING
            Name: alsa_output.pci-0000_2d_00.4.analog-surround-51
    ...
            Driver: PipeWire
    ...
            Mute: no
            Volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB,   rear-left: 65536 / 100% / 0.00 dB,   rear-right: 65536 / 100% / 0.00 dB,   front-center: 65536 / 100% / 0.00 dB,   lfe: 65536 / 100% / 0.00 dB
                    balance 0.00

提示：若当前有音频播放，可通过 [grep(1)](<https://man.archlinux.org/man/grep.1>) 筛选 _RUNNING_ （运行中）状态设备，其他设备通常显示为 _SUSPENDED_ （已挂起）。 

_balance_ （声道平衡）数值会自动计算。设置默认设备的整体音量： 
    
    pactl set-sink-volume @DEFAULT_SINK@ 75%

独立设置各声道音量（需提供每个声道的百分比）： 
    
    pactl set-sink-volume @DEFAULT_SINK@ 100% 75% 100% 75% 100% 100%

_Source_ （输入设备）的操作方式类似。更多配置（如模块加载）请参考上游维基： [Migration from PulseAudio](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Migrate-PulseAudio>) [Pipewire-Pulse Configuration](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config-PulseAudio>). 

####  JACK 客户端

安装 [pipewire-jack](<https://archlinux.org/packages/?name=pipewire-jack>)包 以获取 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）") 支持。还有 [lib32-pipewire-jack](<https://archlinux.org/packages/?name=lib32-pipewire-jack>)包 用于 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 支持。 

[pw-jack(1)](<https://man.archlinux.org/man/pw-jack.1>) 可以用来启动 JACK 客户端， 但从技术上讲它不是必需的， 因为它只用作 `PIPEWIRE_REMOTE`、`PIPEWIRE_DEBUG` 和 `PIPEWIRE_LATENCY` 环境变量的包装器。 

可以通过设置 缓冲区大小/采样率 的商（等于以秒为单位的块延迟）来请求自定义缓冲区大小： 
    
    PIPEWIRE_LATENCY="128/48000" _application_
    
####  蓝牙设备

如果安装了 [pipewire-pulse](<https://archlinux.org/packages/?name=pipewire-pulse>)包 软件包，PipeWire 将自动处理蓝牙音频设备。 

#####  自动化 profile 切换

[pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 和 [WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber") 都可以在检测到输入流时自动在 HSP/HFP 和 A2DP 配置文件之间切换。 

[WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber") 默认启用了配置文件自动切换。每当检测到输入流时，它可以自动在 HSP/HFP 和 A2DP 配置文件之间切换。可以使用以下命令禁用它： 
    
    $ wpctl settings --save bluetooth.autoswitch-to-headset-profile false
    
[pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 默认禁用，可以设置 `bluez5.autoswitch-profile` 属性为 `true` 以启用他： 
    
    /etc/pipewire/media-session.d/bluez-monitor.conf (or ~/.config/pipewire/media-session.d/bluez-monitor.conf)
    
    ...
    rules = [
        {
            ...
            actions = {
                update-props = {
                    ...
                    bluez5.autoswitch-profile = true
    ...

####  用于命令行的 PipeWire 补丁集

[qpwgraph](<https://archlinux.org/packages/?name=qpwgraph>)包 可用于可视化和创建连接，以及保存和加载补丁集。 对于非 GUI 需求，以下是用于保存线集、加载线集和解除所有连接的 bash 脚本。 要保存和加载，请使用命令行参数作为文件名。 
    
    pw-savewires
    
    #!/bin/bash
    
    if [[ "$#" -ne 1 ]]; then
    	echo
    	echo 'usage: pw-savewires filename'
    	echo
    	exit 0
    fi
    
    rm $1 &> /dev/null
    while IFS= read -r line; do
    	link_on=`echo $line | cut -f 4 -d '"'`
    	link_op=`echo $line | cut -f 6 -d '"'`
    	link_in=`echo $line | cut -f 8 -d '"'`
    	link_ip=`echo $line | cut -f 10 -d '"'`
    	echo "Saving: " "'"$link_on:$link_op"','"$link_in:$link_ip"'"
    	echo "'"$link_on:$link_op"','"$link_in:$link_ip"'" >> $1
    done < <(pw-cli dump short link)
    
    pw-loadwires
    
    #!/bin/python
    
    import sys
    import csv
    import os
    
    if len(sys.argv) < 2:
    	print('\n usage: pw-loadwires filename\n')
    	quit()
    
    with open(sys.argv[1], newline='') as csvfile:
    	pwwreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    	for row in pwwreader:
    		print('Loading:  ' + row[0] + ' --> ' + row[1])
    		process = os.popen('pw-link ' + row[0] + ' ' + row[1])
    
    pw-dewire
    
    #!/bin/bash
    while read -r line; do
    	echo 'Dewiring: ' $line '...'
    	pw-link -d $line
    done < <(pw-cli dump short link {{!}} grep -Eo '^[0-9]+')
    
####  与网络上的计算机共享音频设备

虽然 PipeWire 本身不是网络透明的，但其pulse实现支持[网络串流](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config-PulseAudio#network-support>)。在网络上的计算机之间共享音频的一种简单方法是使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 守护程序进行发现。要启用此功能，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pipewire-zeroconf](<https://archlinux.org/packages/?name=pipewire-zeroconf>)包 软件包。 

确保所有要共享声音的计算机上的 `avahi-daemon.service` 正在运行（如果使用 [firewall](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）")，则要保证 UDP 端口 `5353` 已打开）。 

**注意：** 某些 GUI 卷管理器默认隐藏网卡。（例如：在 Plasma 中，必须“配置音频音量...”并选中“显示虚拟设备”。

要共享本地音频设备，在主机上加载适当的模块（确保使用本地 IP 地址）： 
    
    $ pactl load-module module-native-protocol-tcp listen=_192.168.1.10_
    $ pactl load-module module-zeroconf-publish
    
然后在客户端上加载发现模块： 
    
    $ pactl load-module module-zeroconf-discover
    
还可以通过创建专用配置文件自动加载模块： 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 使用`context.modules` 而不是像下面这样的 `context.exec`。（在[Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>)讨论）
    
    /etc/pipewire/pipewire-pulse.conf.d/50-network-party.conf
    
    context.exec = [
        { path = "pactl" args = "load-module module-native-protocol-tcp" }
        { path = "pactl" args = "load-module module-zeroconf-discover" }
        { path = "pactl" args = "load-module module-zeroconf-publish" }
    ]

#####  将音频串流到 AirPlay 接收器

可以将音频串流到冒充 [AirPlay 接收器](<https://en.wikipedia.org/wiki/AirPlay#Receivers> "wikipedia:AirPlay")的设备。 要启用此功能，请加载 [RAOP Discover 模块](<https://docs.pipewire.org/page_module_raop_discover.html>)： 
    
    $ pactl load-module module-raop-discover
    
还可以通过创建专用配置文件自动加载此模块： 
    
    /etc/pipewire/pipewire.conf.d/raop-discover.conf (or ~/.config/pipewire/pipewire.conf.d/raop-discover.conf)
    
    context.modules = [
       {
           name = libpipewire-module-raop-discover
           args = { }
       }
    ]

某些扬声器的 AirPlay 实现（例如 Sonos AirPlay 2 扬声器）可能需要为源设备上的传入 UDP 流量打开端口 6001 和 6002。 

####  在本地 JACK 上运行 PipeWire

如果需要，PipeWire 也可以作为 JACK 客户端在本机 JACK 守护程序之上运行。 

请参阅 [JACK 和 PipeWire (PipeWire wiki)](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/JACK>) 和 [-JACK#jack-bridge JACK 桥(PipeWire wiki)](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config>) 了解更多信息和附加配置（例如可用通道）。 

要使用它，请安装 [pipewire-jack-client](<https://archlinux.org/packages/?name=pipewire-jack-client>)包 并启动 JACK。Pipewire 应该会被自动桥接。 

**注意：** 自从 pipewire [0.3.81版本](<https://gitlab.freedesktop.org/pipewire/pipewire/-/releases/0.3.81>) 加载 jackdbus 模块是自动完成的，而且不再是必须的。 

它可以在启动 jack 之前像 PulseAudio 模块一样手动加载（在[pactl(1)](<https://man.archlinux.org/man/pactl.1>)解释）：`pactl load-module module-jackdbus-detect`。 

####  使用 ALSA dmix 设备作为 PipeWire 接收器

可以通过 [ALSA dmix devices](<../zh-cn/Advanced_Linux_Sound_Architecture.html#Dmix> "Advanced Linux Sound Architecture") 将 PipeWire 服务器（或每个用户多个）输出到 ALSA。这允许您使用 ALSA 作为主要音频输出系统，同时能够使用非 ALSA 设备，例如蓝牙耳机。 

#####  ALSA dmix 设置

假设您有两张卡：`PCH` 和 `HDMI`： 
    
    /proc/asound/cards
    
     0 [PCH            ]: HDA-Intel - HDA Intel PCH
                          HDA Intel PCH at 0xdff40000 irq 146
     1 [HDMI           ]: HDA-Intel - HDA ATI HDMI
                          HDA ATI HDMI at 0xdfe60000 irq 147
    
你的 PCM 看起来长这样： 
    
    /proc/asound/pcm
    
    00-00: ALC1220 Analog : ALC1220 Analog : playback 1 : capture 1
    00-02: ALC1220 Alt Analog : ALC1220 Alt Analog : capture 1
    01-03: HDMI 0 : HDMI 0 : playback 1
    01-07: HDMI 1 : HDMI 1 : playback 1
    01-08: HDMI 2 : HDMI 2 : playback 1
    01-09: HDMI 3 : HDMI 3 : playback 1
    01-10: HDMI 4 : HDMI 4 : playback 1
    01-11: HDMI 5 : HDMI 5 : playback 1
    
假设您的 ALSA 配置如下所示： 
    
    /etc/asound.conf
    
    ctl.!default {
      type hw
      card PCH
    }
    
    pcm.!default {
      type plug
      slave.pcm "**dmix:PCH,0** "
    }
    
    pcm.dhdmi {
      type plug
      slave.pcm "**dmix:HDMI,9** "
    }
    
在此特定示例中，dmix 设备为 `dmix:PCH,0` 和 `dmix:HDMI,9`。 

#####  PipeWire dmix 设置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 添加[pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 指南。 (在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论)

首先，通过注释掉 `alsa_monitor.enable()` 来阻止 `wireplumber` 监控和添加硬件 ALSA 设备： 
    
    /etc/wireplumber/main.lua.d/90-enable-all.lua (or ~/.config/wireplumber/main.lua.d/90-enable-all.lua)
    
    ...
    -- Load devices
    **-- alsa_monitor.enable()**
    v4l2_monitor.enable()
    libcamera_monitor.enable()
    ...
    
现在，配置 `pipewire` 以使用 dmix 设备。 默认配置文件（`/usr/share/pipewire/pipewire.conf`）包含一个[注释掉了的示例](<https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/0.3.59/src/daemon/pipewire.conf.in#L219-239>)，您可以将其用作模板。 

将您自己的元素添加到 `context.objects` 数组中： 
    
    /etc/pipewire/pipewire.conf.d/alsa-dmix.conf (or ~/.config/pipewire/pipewire.conf.d/alsa-dmix.conf)
    
    context.objects = [
        # We do not start with dmix, but with an input device.
        # Do not forget to add an input device.
        # On a friend's Laptop, I saw Zoom having a nervous
        # breakdown and endlessly crying because no input device
        # was configured! You have been warned.
        { factory = adapter
            args = {
                factory.name           = api.alsa.pcm.source
                node.name              = "alsa-mic-internal" # name of pulse device (mpv)
                node.description       = "Mic Internal" # name of pulse device (pavucontrol)
                media.class            = "Audio/Source"
                api.alsa.path          = "**hw:PCH,0** "
            }
        }
        # Okay, now we add our dmix PCMs
        { factory = adapter
            args = {
                factory.name           = api.alsa.pcm.sink # sink for dmix
                node.name              = "alsa-dmix-internal" # name of pulse device (mpv)
                node.description       = "PCM Internal" # name of pulse device (pavucontrol)
                media.class            = "Audio/Sink" # Sink for dmix
                api.alsa.path          = "**dmix:PCH,0** "
            }
        }
    
        { factory = adapter
            args = {
                factory.name           = api.alsa.pcm.sink # sink for dmix
                node.name              = "alsa-dmix-hdmi" # name of pulse device (mpv)
                node.description       = "PCM HDMI" # name of pulse device (pavucontrol)
                media.class            = "Audio/Sink" # Sink for dmix
                # remember this is a non-default dmix from /etc/asound.conf
                api.alsa.path          = "**dmix:HDMI,9** "
            }
        }
    ]

作为用户（非 root），检查 `wpctl status` 的输出，并使用`wpctl set-default _ID_`根据您的喜好设置默认输入（源）和输出（接收器）设备。` _ID_` 是接收器/源名称之前的数字。 

现在，您可以全面测试您的配置。 

####  在设备配置之间切换

某些硬件音频设备（例如 `snd_hda_intel`）的功能会有所不同，具体取决于设备运行的配置文件。对于 `snd_hda_intel`，HDMI 和模拟输出有单独的配置文件。 

使用 WirePlumber 切换到 HDMI： 
    
    $ wpctl set-profile <device-ID> 3
    $ wpctl status
    
    ...
    ├─ Sinks:
    │  *   53. Built-in Audio Digital Stereo (HDMI) [vol: 1.00]
    ...

使用 WirePlumber 切换到模拟： 
    
    $ wpctl set-profile <device-ID> 1
    $ wpctl status
    
    ...
    ├─ Sinks:
    │  *   51. Built-in Audio Analog Stereo        [vol: 0.60]
    ...

###  WebRTC 屏幕共享

大多数应用程序过去依赖 X11 来捕获桌面（或单个应用程序），例如在网络浏览器中使用 WebRTC 时（例如在 Google Hangouts 上）。在 Wayland 上，出于安全原因，共享机制的处理方式有所不同。PipeWire 可以通过细粒度的访问控制在 Wayland 下共享内容。 

**提示：** 使用以下命令测试 WebRTC 屏幕共享是否正常工作[Mozilla 的 GetUserMedia WebRTC 测试页面](<https://mozilla.github.io/webrtc-landing/gum_test.html>).

**注意：**[xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 1.10.0 修复了 D-Bus 接口的规范和实现之间的不匹配问题。[[3]](<https://github.com/flatpak/xdg-desktop-portal/pull/609>) 因此，某些客户端可能无法使用 xdg-desktop-portal 1.10.0 或更高版本。

这需要 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 及其后端之一[被安装](<https://jgrulich.cz/2018/07/04/how-to-enable-and-use-screen-sharing-on-wayland>)。可用的后端有： 

  * [xdg-desktop-portal-gnome](<https://archlinux.org/packages/?name=xdg-desktop-portal-gnome>)包 对应 GNOME。
  * [xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包 对应 KDE。
  * [xdg-desktop-portal-wlr](<https://archlinux.org/packages/?name=xdg-desktop-portal-wlr>)包 对应 基于 wlroots 的 Wayland 合成器 (例如 [Sway](<../zh-cn/Sway.html> "Sway"), [dwl](<https://github.com/djpohly/dwl>))

Firefox (84+) 默认支持此方法，而在 Chromium (73+) 上，需要通过设置启用 [WebRTC PipeWire 支持](<https://bugs.chromium.org/p/chromium/issues/detail?id=682122>) URL `chrome://flags/#enable-webrtc-pipewire-capturer` 处的相应（实验）标志。 

[obs-studio](<https://archlinux.org/packages/?name=obs-studio>)包 (27+) 通过使用新的 PipeWire 捕获源支持此方法。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 自从 [该pull request](<https://github.com/flatpak/xdg-desktop-portal-gtk/pull/225>) 被合并后，以下有关特定应用程序/窗口共享的注释在[xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包上可能不再正确。另请参阅跟踪此讨论的情况：[[4]](<https://github.com/flatpak/xdg-desktop-portal-gtk/issues/204>).（在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论）

请注意，唯一支持的功能是共享整个桌面，而不是特定的应用程序/窗口 [-individual-windows](<https://github.com/emersion/xdg-desktop-portal-wlr/wiki/FAQ#will-this-let-me-share>)[[5]](<https://github.com/KDE/xdg-desktop-portal-kde/blob/master/TODO>)。 

#### xdg-desktop-portal-wlr

为了使 `xdg-desktop-portal-wlr` 正常工作，必须在 [systemd用户会话](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F> "Systemd/用户") 中设置 `XDG_CURRENT_DESKTOP` 和 `WAYLAND_DISPLAY` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。`XDG_CURRENT_DESKTOP` 必须设置为您的合成器的名称，例如 `XDG_CURRENT_DESKTOP=sway`。`WAYLAND_DISPLAY` 由合成器自动设置。将这些环境变量引入 systemd 用户会话的推荐方法是在启动合成器后运行 `systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP`，例如使用合成器配置文件。有关更多详细信息，请参阅 [[6]](<https://github.com/emersion/xdg-desktop-portal-wlr#running>) 和 [[7]](<https://github.com/emersion/xdg-desktop-portal-wlr/wiki>)。 

**提示：** 如果您有多个监视器，要选择与 `xdg-desktop-portal-wlr` 共享监视器，请安装 [slurp](<https://archlinux.org/packages/?name=slurp>)包 并添加以下配置（请参阅 [xdg-desktop-portal-wlr(5) § 屏幕播放选项](<https://man.archlinux.org/man/xdg-desktop-portal-wlr.5#%E5%B1%8F%E5%B9%95%E6%92%AD%E6%94%BE%E9%80%89%E9%A1%B9>)): 
    
    ~/.config/xdg-desktop-portal-wlr/config
    
    chooser_type = simple
    chooser_cmd = slurp -f %o -ro

当请求共享屏幕时，`slurp` 会向您显示十字光标，您需要单击要共享的屏幕。选择后，`xdg-desktop-portal-wlr` 将允许共享该屏幕。 

###  视频

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：**[pipewire-v4l2](<https://archlinux.org/packages/?name=pipewire-v4l2>)包 (在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论)

尽管该软件尚未准备好投入生产，但可以安全地使用。大多数依赖 [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") 处理视频流的应用程序应该使用 PipeWire GStreamer 插件开箱即用，请参阅 [GStreamer#PipeWire](<../zh-cn/GStreamer.html#PipeWire> "GStreamer")。因此，像 [cheese](<https://archlinux.org/packages/?name=cheese>)包 这样的应用程序已经能够使用它来共享视频输入。 

使用 [pipewire-v4l2](<https://archlinux.org/packages/?name=pipewire-v4l2>)包，还应该可以使用 `pw-v4l2` 脚本来预加载库 (`/lib/pipewire-0.3/v4l2/libpw-v4l2 .so`）拦截 v4l2 调用并通过管道路由视频。 

##  音频后期处理

###  Pipewire 模块过滤链（module-filter-chain）

Pipewire 有一个名为[过滤链（filter-chain）](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Filter-Chain>)的内部模块，可以创建节点来处理音频输入和输出。有关均衡、虚拟环绕声、LADSPA 插件和通道混合的示例，请参阅 `/usr/share/pipewire/filter-chain/`。 

####  全系统参数均衡

将配置文件复制到您的 `.config` 文件夹： 
    
    $ mkdir -p ~/.config/pipewire/pipewire.conf.d
    $ cp /usr/share/pipewire/filter-chain/sink-eq6.conf ~/.config/pipewire/pipewire.conf.d/
    
然后编辑 `sink-eq6.conf` 以合并所需的参数。对于耳机，可以从 [Oratory1990 的数据库](<https://old.reddit.com/r/oratory1990/wiki/index>)获取，或者，如果没有列出，则参考 [AutoEQ 项目](<https://github.com/jaakkopasanen/AutoEq/tree/master/results/>)。 

如果您需要前置放大器，请修改 `eq_band_1` 以在频率 0Hz 处应用具有负增益的 `bq_highshelf` 滤波器（支持 -120 至 +20dB 的增益）： 
    
    label = bq_highshelf
    control = { "Freq" = 0 "Q" = 1.0 "Gain" = -7.5 }
    
对于超过 6 个频段，请向 `nodes` 列表和相应的 `links` 添加更多条目，将一个过滤器“:Out”连接到下一个过滤器“:In”，例如增加到 11频段（前置放大器 + 10）： 
    
                        { output = "eq_band_6:Out" input = "eq_band_7:In" }
                        { output = "eq_band_7:Out" input = "eq_band_8:In" }
                        { output = "eq_band_8:Out" input = "eq_band_9:In" }
                        { output = "eq_band_9:Out" input = "eq_band_10:In" }
                        { output = "eq_band_10:Out" input = "eq_band_11:In" }
    
重新启动Pipewire，选择“Equalizer Sink”作为默认声音输出设备； 这应该适用于所有应用程序。 

### EasyEffects

EasyEffects（以前的 PulseEffects）是一个 GTK 实用程序，它为各个应用程序输出流和麦克风输入流提供大量音频效果和滤波器。值得注意的效果包括输入/​​输出均衡器、输出响度均衡和低音增强、输入嘶声消除器和降噪插件。有关效果的完整列表，请参阅 [GitHub 页面](<https://github.com/wwmm/easyeffects>)。 

为了使用 EasyEffects，请安装 [easyeffects](<https://archlinux.org/packages/?name=easyeffects>)包。有关预设配置的集合，请参阅[社区预设](<https://github.com/wwmm/easyeffects/wiki/Community-presets>)。对于算法生成的耳机 EQ 预设的集合，请参阅 [AutoEq](<https://github.com/jaakkopasanen/AutoEq>)。 

**注意：** 对于 PulseEffects 旧版本，请参阅 [PulseAudio#PulseEffects](<../zh-cn/PulseAudio.html#PulseEffects> "PulseAudio").

### NoiseTorch

NoiseTorch 是一种噪声抑制的替代方法，与 [noisetorch](<https://aur.archlinux.org/packages/noisetorch/>)AUR 打包在一起。另外还有-git版本[noisetorch-git](<https://aur.archlinux.org/packages/noisetorch-git/>)AUR。 

启动后，可以为所选麦克风加载模块。可以调整语音激活阈值，应将其设置为最高级别，而不是过滤掉任何实际语音。 

您可以使用 systemd 自动启动音频处理，请参阅 [[8]](<https://github.com/noisetorch/NoiseTorch/wiki/Start-automatically-with-Systemd>)。请注意，如果从 AUR 安装，noisetorch 二进制路径会有所不同。 

###  语音噪声抑制

安装 [noise-suppression-for-voice](<https://archlinux.org/packages/?name=noise-suppression-for-voice>)包 并进行下列操作之一： 

  * 在 `context.exec` 添加以下内容：

    /etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)
    
    ...
    context.exec = [
        ...
        { path = "/usr/bin/pipewire" args = "-c /usr/share/pipewire/filter-chain/source-rnnoise.conf" }
        ...

  * 参照 <https://github.com/werman/noise-suppression-for-voice#pipewire>.

然后将降噪后的音频源作为音频的默认选项。您可能需要先重启应用才能使用新的音频源。 

### JamesDSP

[JamesDSP for Linux](<https://github.com/Audio4Linux/JDSP4Linux#readme>) ([jamesdsp](<https://aur.archlinux.org/packages/jamesdsp/>)AUR) 为 PipeWire 和 PulseAudio 提供开源的音效实现。JamesDSP 使用自己的效果引擎，不依赖 LADSPA 或是 Calf 之类的东西。起初它被用于安卓设备的音效处理。 

###  LADSPA, LV2 和 VST 插件

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Does this section relate to using the pulseaudio daemon or the pipewire's interface for pulseaudio clients?（在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论）

您可以创建将 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 连接到 Carla 音频插件的输入/输出目标位置。 

如果您想在所有可用的 LADSPA、LV2 和 VST 中选择的话，可以使用自定义的 Pulseaudio null sink 和 Carla Jack 来应用这些插件。安装 [pipewire-pulse](<https://archlinux.org/packages/?name=pipewire-pulse>)包、[pipewire-jack](<https://archlinux.org/packages/?name=pipewire-jack>)包 和 [carla](<https://archlinux.org/packages/?name=carla>)包。首先，创建一个名为 `default_null_sink` 的 PulseAudio null sink。 . 
    
    pactl load-module module-null-sink object.linger=1 media.class=Audio/Sink sink_name=default_null_sink channel_map=FL,FR
    
从 Pipewire 启动 Carla：`pw-jack carla-rack`。在 _Rack(机架)_ 页面添加您想使用的插件，确保它们的类型都是 _stereo(立体声)_ 。您可以改变插件间的顺序，处理顺序由上至下（最上面的会最先接收到音频流），就跟 EasyEffects 一样。随后，在 _Patchbay(跳线槽)_ 页面将 `default_null_sink` 的左右监听(L/R monitor)连接到 Carla 的输入，然后将 Carla 的输出连接到回放设备(音响、耳机、HDMI...)。将配置文件保存到一个本地位置，比如 `~/Documents/carla_sink_effects.carxp`。 

您可以在多媒体应用发声的时候测试这些效果，比如用 Firefox 看视频。有两种测试方式。第一种：在 Carla 的 _Patchbay_ ，断开 Firefox 的所有连线，然后把它的左右声道输出连接到 `default_null_sink` 的 playback。第二种：使用 [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包 找到 Firefox 的音频流，然后将其重定向到 `default_null_sink`（这应该会记住连接方式，在下次启动的时候自动重定向）。 

若想在启动时应用这些设置，创建两个 systemd 用户服务： 
    
    ~/.config/systemd/user/jack-carla-rack.service
    
    [Unit]
    Description=Load Carla Rack JACK host
    
    [Service]
    PassEnvironment="PIPEWIRE_LINK_PASSIVE=true"
    Type=exec
    ExecStart=/usr/bin/pw-jack carla-rack -n
    
    [Install]
    WantedBy=default.target
    
    ~/.config/systemd/user/pulseaudio-null-sink@.service
    
    [Unit]
    Description=Load %i Pulseaudio null sink
    Before=jack-carla-rack.service
    After=pipewire-pulse.service
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/pactl load-module module-null-sink object.linger=1 media.class=Audio/Sink sink_name=%i channel_map=FL,FR
    ExecStop=/usr/bin/pactl unload-module module-null-sink
    RemainAfterExit=yes
    
    [Install]
    WantedBy=default.target

然后覆盖 _jack-carla-rack_ 服务，并在 _Environment_ 部分写明 Carla 配置的完整路径。 
    
    ~/.config/systemd/user/jack-carla-rack.service.d/override.conf
    
    [Service]
    Environment="CARLA_CONFIG_FILE=/home/username/Documents/carla_sink_effects.carxp"
    ExecStart=
    ExecStart=/usr/bin/pw-jack carla-rack -n $CARLA_CONFIG_FILE

最后，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `pulseaudio-null-sink@default_null_sink.service` 和 `jack-carla-rack.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

注意，如果你将 `default_null_sink` 设置为了系统默认设备，所有的应用声音都会被重定向至它，并且音量键也会改变它的音量而不是回放设备的。如果想控制回放设备的音量，需要把回放设备设成默认设备，然后将所需应用在 pavucontrol 里重定向到 `default_null_sink`（PipeWire兼容层应该会记住应用的连接关系）。 

##  故障排除

###  音频

####  PipeWire 检测不到麦克风

PipeWire 的 `alsa-monitor` 模块默认使用 [alsa-card-profiles](<https://archlinux.org/packages/?name=alsa-card-profiles>)包 检测设备。若失效，可尝试在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 中关闭 `api.alsa.use-acp` 或启用 `api.alsa.use-ucm`： 
    
    /etc/wireplumber/wireplumber.conf.d/50-alsa-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/50-alsa-config.conf)
    
    monitor.alsa.properties = {
      # 使用ALSA卡配置文件设备。它们通过UCM或配置集。
      # 来配置设备和混音器设置。
      **# alsa.use-acp = true**
      # 优先使用UCM配置（若可用）。可禁用此项。
      # 以跳过尝试使用UCM配置。
      **alsa.use-ucm = true**
    }

如果使用的是 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包: 
    
    /etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)
    
    ...
    rules = [
        {
            ...
            actions = {
            update-props = {
                ...
                **api.alsa.use-acp = false**
    ...

然后重启 WirePlumber 并检查可用设备： 

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** `--list-targets` 选项在新版的 `pw-record` 中已不可用，若想列出项目请使用 `wpctl status`、`pw-cli ls` 或是 `pw-dump`。 (在[Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>)讨论)
    
    $ pw-record --list-targets
    
    Available targets ("*" denotes default): 62
    	58: description="Built-in Audio" prio=1872
    	60: description="Built-in Audio" prio=2000
    *	62: description="Built-in Audio (Loopback PCM)" prio=1984

在[这个 issue](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/2332>) 中提到的另一种解决方案是手动添加麦克风。首先，确保麦克风能被 ALSA 检测到。 
    
    $ arecord -l
    
    **** List of CAPTURE Hardware Devices ****
    card _card_number_ : _card_name_ , device _device_number_ : _device_name_
      ...
    
从列表里选择你的麦克风，运行以下命令以测试麦克风。 
    
    $ arecord --duration=5 --format=dat --device=hw:_card_number_ ,_device_number_ test-mic.wav # record from the mic
    $ aplay test-mic.wav # play it

如果 arecode 测试麦克风工作正常但是却没被 PipeWire 检测到，试着通过配置文件手动添加这一设备。 
    
    /etc/pipewire/pipewire.conf.d/microphone.conf (or ~/.config/pipewire/pipewire.conf.d/microphone.conf)
    
    context.objects = [
        { factory = adapter
            args = {
                factory.name           = api.alsa.pcm.source
                node.name              = "microphone"
                node.description       = "Undetected Microphone"
                media.class            = "Audio/Source"
                api.alsa.path          = "hw:_card_number_ ,_device_number_ "
            }
        }
    ]

重启 PipeWire 来重载配置。 

####  连接新设备时声音不会自动切换

要实现自动切换到新连接的设备，请创建以下文件： 
    
    /etc/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf (或 ~/.config/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf)
    
    pulse.cmd = [
        { cmd = "load-module" args = "module-switch-on-connect" }
    ]

然后使用 [systemctl --user](<../zh-cn/Systemctl_--user.html> "Systemctl --user") [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `pipewire-pulse.service` 服务，并检查 `module-switch-on-connect` 模块是否已加载。 

####  连接到蓝牙设备后没有声音

截至 2020-12-07，如果连接上蓝牙设备却没有声音，您可能需要切换默认输出设备(sink)与/或是将 sink 输入移动到正确的 sink 位置。使用 `pactl list sinks` 列出所有可用的 sink 并通过 `pactl set-default-sink` 将默认 sink 切换为蓝牙设备。这可以使用类似[这样的脚本](<https://gist.github.com/tinywrkb/04e7fd644afa9b92d33a3a99ab07ee9e>)通过 [udev](<../zh-cn/Udev.html> "Udev") 自动化。 

参见这个 [Reddit 讨论串](<https://www.reddit.com/r/archlinux/comments/jydd02/pipewirepulse_03164_in_testing_now_replaces/gd3m7fu/?context=3>)关于这一问题的探讨。根据脚本作者所言，耳机配置(the headset profile，HSP)可能仍有问题。 

####  mpv/vlc/totem 无声音但浏览器和GNOME扬声器测试正常

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 当前行文风格不符合Wiki规范，更类似博客文章。需要重新措辞并精简内容。子章节划分过度，且问题原因未经证实仅为推测。（在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论）

#####  问题现象描述

验证此问题的最佳方式是使用 `mpv` 测试已安装编解码器支持的视频文件： 
    
    $ mpv --ao=alsa _测试文件.mpv_
    $ mpv --ao=pcm _测试文件.mpv_
    $ mpv --ao=jack _测试文件.mpv_
    $ mpv --ao=pulse _测试文件.mpv_
    $ mpv --ao=openal _测试文件.mpv_
    
若上述部分或全部测试能正常发声，但使用 `pipewire` 选项时无声： 
    
    $ mpv --ao=pipewire _测试文件.mpv_
    
则适用本解决方案。GNOME 桌面扬声器测试和浏览器播放 YouTube 能正常发声。 

在 GNOME 中切换输入、静音/取消静音、调节音量均无法解决问题。 

`pactl list sinks` 显示为 'SUSPENDED' 可忽略，因浏览器播放视频时状态会正常变化。 

使用 `pactl info` 未发现明显问题。 

检查相关 `systemd` 单元日志也未发现明显异常。 

#####  问题原因

疑似 PipeWire 到硬件的音频路径被静音，原作者无法通过命令行工具具体定位该问题。 

#####  解决方案

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pavucontrol](<https://archlinux.org/packages/?name=pavucontrol>)包 软件包。运行 `pavucontrol`，选择相应音源，在 `mpv --ao=pipewire test.mp4` 播放时切换静音按钮状态。 

####  音量过低

将 PulseAudio 替换为 PipeWire 后，声音可能正常工作，但重启后音量会变得异常低。 

打开 `alsamixer`，使用 `F6` 选择正确的声卡，并确保 ALSA 音量设置为 100%。`alsactl` 会在重启后保持此设置。 

####  提升 RLIMIT_MEMLOCK
    
    Dec 13 11:11:11 HOST pipewire-pulse[99999]: Failed to mlock memory 0x7f4f659d8000 32832: This is not a problem but for best performance, consider increasing RLIMIT_MEMLOCK
    
安装 [realtime-privileges](<https://archlinux.org/packages/?name=realtime-privileges>)包 并且将您的用户加入 `realtime` 组。 

此外，将 memlock 从 64kB 提升至 128kB 似乎足以解决问题。如果你是在 [systemd/User](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/User") 下使用 `pipewire-pulse`，向 `/etc/security/limits.d/username.conf` 添加： 
    
    username	soft	memlock	64
    username	hard	memlock	128
    
####  修改默认采样率

默认 PipeWire 使用 48kHz 的全局采样率。如果您想更改此值（比如您有个支持更高采样率的 DAC），则可以设置一个更高的默认值： 
    
    /etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)
    
    ...
    context.properties = {
        ...
        **default.clock.rate          =_sample_rate_**
        ...

####  修改允许的采样率

只要 DAC 支持，PipeWire 可以动态更改采样率。所选的采样率会跟随当前正在播放的音频流。 
    
    /etc/pipewire/pipewire.conf (or ~/.config/pipewire/pipewire.conf)
    
    ...
    context.properties = {
        ...
        **default.clock.allowed-rates = [_sample_rate_1_ _sample_rate_2_ _sample_rate_3_ ... ]**
        ...

举个例子： `[ 44100 48000 88200 96000 ]`. 

据[开发者所言](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1523>)，“PipeWire 支持至多 16 种不同的采样率，并且会在允许的时候进行切换”。也就是说，在受支持的设备按照以上内容配置**不会发生重采样** 。在 PipeWire [0.3.61](<https://gitlab.freedesktop.org/pipewire/pipewire/-/releases/0.3.61#pipewire>) 之后，最多可以配置 32 种不同的采样率。 

#####  获取支持的采样率

请参照您 DAC 的硬件手册来查看受支持的采样率。内核驱动编码器支持的采样率可以通过以下命令查看： 
    
    $ grep -E 'Codec|Audio Output|rates' /proc/asound/card*/codec#*
    
如果您的DAC没有报告编解码器信息，可以尝试这样获取支持的采样率： 
    
    $ grep -m1 -Hn "" /proc/asound/card?/stream? | tee /dev/tty | awk -F':' '{print $1}' | xargs grep 'Rates'
    
**注意：** 虽然您的DAC芯片可能报告比规格书更高的采样率，但其中一些是为特殊模式(如USB转I2S)设计的

#####  检查当前使用的采样率

要想查看当前某声卡配置的采样率，请运行： 
    
    $ grep rate: /proc/asound/card?/pcm??/sub?/hw_params
    
    /proc/asound/card1/pcm0p/sub0/hw_params:rate: 96000 (96000/1)
    
在 `pcm0p` 和 `pcm0c` 中，`c` 指的是"录制设备（capture）"而 `p`指的是"回放设备（playback）"。 

命令： 
    
    $ pw-top
    
也可以显示每个声卡和音频流当前使用的采样率。 

**提示：** 如果在设置default.clock.allowed-rates后DAC仍无法切换到更高采样率，可能意味着系统无法读取DAC支持的采样率。这种情况下您仍可以尝试设置default.clock.rate

####  音质 (重采样质量)

如果之前使用 PulseAudio 时用了 `resample-method = speex-float-10` 或是 `soxr-vhq`，可考虑将 `resample.quality` 设为 `10` 或最大值 `14`： 
    
    /etc/pipewire/client.conf.d/resample.conf (或 ~/.config/pipewire/client.conf.d/resample.conf)
    
    stream.properties = {
        resample.quality = 10
    }

不要忘记[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `pipewire.service` 和 `pipewire-pulse.socket` 这两个[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")(如果想要应用配置千万不能把后者忘了)。 

在 `10` 与 `14` 之间音质差距很小，但是 CPU 负载会差两到三倍。同时，`4`、`10` 与 `14` 对延迟影响的差距还有待探索。在Ryzen 2600上使用 `resample.quality = 14` 进行44100→48000Hz重采样时，`pipewire` 或 `pipewire-pulse` 进程会占用单核4%的CPU资源。 

您可以在 <https://src.infinitewave.ca/> 比较重采样器(不要关注任何超过 18KHz，超过 120dB 的内容)。speex 被列为 "Xiph.org Speex"。 

PipeWire 使用它自己的被称为 Spa 的重采样算法。与 SoX 的 `sox` 和 Speex 的 `speexenc` 一样，PipeWire 同样有这个重采样器的单独版本 `spa-resample`。使用方法如下： 
    
    $ spa-resample -q 14 -f s24 -r 48000 输入文件16bit44100或其他格式.wav 输出文件24bit48000hz.wav
    
通过创建自己的 sink 并且使用其他重采样器应该是可能的。或者你也可以使用音乐播放器的插件，比如 Qmmp 就有个 SoX 插件。 

####  外部声卡在重连后不会激活

检查 `~/.config/pipewire/media-session.d/default-profile` 看看有没有默认配置是 "off" 的条目并将其移除。如果不管用，移除 `~/.config/pipewire/media-session.d/` 中的所有文件并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `pipewire.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

####  没有声音或 pactl info shows 执行失败：Connection refused

这意味着应用程序无法连接到 PipeWire-Pulse 服务，请检查 `pipewire-pulse.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")是否正在运行。 

如果问题仍未解决，请运行 `strace -f -o /tmp/pipe.txt pactl info`，然后在 IRC（OFTC 网络的 [#pipewire](<ircs://irc.oftc.net/pipewire>) 频道）或邮件列表寻求帮助时附上 `/tmp/pipe.txt` 文件内容。 

####  蓝牙音质低

若蓝牙播放出现卡顿，检查 `pipewire.service` 的 [unit status](</wzh/index.php?title=Unit_status&action=edit&redlink=1> "Unit status（页面不存在）")，看看有没有类似以下的错误： 
    
    Feb 17 18:23:01 HOST pipewire[249297]: (bluez_input.18:54:CF:04:00:56.a2dp-sink-60) client too slow! rate:512/48000 pos:370688 status:triggered
    
如果出现此类错误，使用 `pactl list sinks` 检查当前所选编码器，试着把 `bluez5.codecs` 修改为 `sbc aac ldac aptx aptx_hd` 其中之一。你也可以尝试 mSBC 支持（修复了 Sony 1000XM3 系列，比如 WH-1000XM3 和 WF-1000XM3 的麦克风）以及 SBC-XQ 编码： 

**注意：** 像 WH-1000XM3 这样的耳机，如果在配套应用中设置"音质模式"为"稳定连接优先"而非"音质优先"，将仅会通告 SBC/SBC-XQ 编解码器。

在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 下： 
    
    /etc/wireplumber/wireplumber.conf.d/51-bluez-config.conf (or ~/.config/wireplumber/wireplumber.conf.d/51-bluez-config.conf)
    
    monitor.bluez.properties = {
      bluez5.enable-sbc-xq = true
      bluez5.enable-msbc = true
      bluez5.codecs = [ sbc sbc_xq ]
    }

使用 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 时： 
    
    /etc/pipewire/media-session.d/bluez-monitor.conf (or ~/.config/pipewire/media-session.d/bluez-monitor.conf)
    
    ...
    properties = {
      ...
      **bluez5.enable-msbc = true**
      **bluez5.enable-sbc-xq = true**
      **bluez5.codecs = [sbc sbc_xq]**
    ...

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `pipewire.service` 用户单元来使修改生效。 

####  在播放时有可觉察的音频延迟或是爆裂声

这是由不活跃时的节点暂停（node suspension）造成的。 

在 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 下: 

创建以下配置文件覆盖默认设置： 
    
    /etc/wireplumber/wireplumber.conf.d/51-disable-suspension.conf (或 ~/.config/wireplumber/wireplumber.conf.d/51-disable-suspension.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            # 匹配所有输入设备
            node.name = "~alsa_input.*"
          },
          {
            # 匹配所有输出设备
            node.name = "~alsa_output.*"
          }
        ]
        actions = {
          update-props = {
            session.suspend-timeout-seconds = 0
          }
        }
      }
    ]
    
    # 对于蓝牙设备
    monitor.bluez.rules = [
      {
        matches = [
          {
            # 匹配所有蓝牙输入
            node.name = "~bluez_input.*"
          },
          {
            # 匹配所有蓝牙输出
            node.name = "~bluez_output.*"
          }
        ]
        actions = {
          update-props = {
            session.suspend-timeout-seconds = 0
          }
        }
      }
    ]

重启 `pipewire.service` 和 `wireplumber.service` 以应用更改。 

除了完全禁用节点暂停，您也可以设置挂起超时时间（单位为秒）。 

部分设备会自行检测静音状态并挂起。对此类设备仅禁用节点暂停可能无效，可通过添加微量噪声使设备永不静音： 
    
    .../51-disable-suspension.conf
    
    ...
        session.suspend-timeout-seconds = 0,  # 0表示禁用挂起
        dither.method = "wannamaker3", # 添加指定类型的抖动
        dither.noise = 2, # 添加额外噪声位
    ...

可能需要调整 `dither.noise` 和 `dither.method` 参数，使噪声既足够微弱又能防止静音检测。详见 [PipeWire documentation](<https://docs.pipewire.org/page_man_pipewire-client_conf_5.html#client_conf__dither_noise>)。 

在 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 下： 

编辑 `/etc/pipewire/media-session.d/*-monitor.conf` 文件（根据延迟出现的设备类型），将 `session.suspend-timeout-seconds` 属性设为 0 禁用暂停，或尝试其他值。 

或者注释掉 `/etc/pipewire/media-session.d/media-session.conf` 中的 `suspend-node` 行。 

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `pipewire.service` 和 `pipewire-pulse.service` 以应用更改，或直接重启系统。 

####  多个流同时播放时音频被切断

此问题通常可以通过阅读 `pipewire-pulse.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")的 [journal](<../zh-cn/Systemd/Journal.html> "Journal") 检测出来。您会看到类似以下内容： 
    
    pipewire-pulse[21740]: pulse-server 0x56009b9d5de0: [Nightly] UNDERFLOW channel:0 offset:370676 underrun:940
    
根据[官方 PipeWire 除错指南](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Troubleshooting#underrununderflow-and-broken-pipe-errors>)，在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 下的解决方案： 
    
    /etc/wireplumber/wireplumber.conf.d/50-alsa-config.conf (或 ~/.config/wireplumber/wireplumber.conf.d/50-alsa-config.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            node.name = "~alsa_output.*"
          }
        ]
        actions = {
          update-props = {
            api.alsa.period-size   = 1024    # 周期缓冲区大小
            api.alsa.headroom      = 8192    # 预留缓冲空间
          }
        }
      }
    ]

在 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 下： 
    
    /etc/pipewire/media-session.d/alsa-monitor.conf (或 ~/.config/pipewire/media-session.d/alsa-monitor.conf
    
    api.alsa.headroom = 1024    # 缓冲空间设置

如果您经历了由内核页锁定（page locking）与延迟调度（late scheduling）导致的音频卡顿，请参考[游戏#调整内核参数以实现响应时间一致性](<../zh-cn/%E6%B8%B8%E6%88%8F.html#%E8%B0%83%E6%95%B4%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0%E4%BB%A5%E5%AE%9E%E7%8E%B0%E5%93%8D%E5%BA%94%E6%97%B6%E9%97%B4%E4%B8%80%E8%87%B4%E6%80%A7> "游戏")。 

####  音频失真

  * 对于麦克风，试着运行 `alsamixer` 并切换到有问题的声卡，然后使用方向键降低所有 "Mic Boost" 与 "Internal Mic Boost" 选项，For microphones,
  * 参照[#修改默认采样率](<#%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E9%87%87%E6%A0%B7%E7%8E%87>)将采样率降至 `44100` (44.1 kHz)。

####  在待机后出现音频问题

如果将机器从睡眠中唤醒后音频出现缺失或是其他状况，重新初始化 ALSA 可能有帮助： 
    
    # alsactl init
    
####  USB DAC 延迟高 (比如 Schiit DACs)

修改采样率可能有助于某些 DAC 的延迟，例如 Schiit Hel 2。[[9]](<https://www.reddit.com/r/osugame/comments/msifdd/usb_dacamp_and_audio_lag/>) 使用 _pipewire-media-session_ 的匹配规则，我们可以为设备设置属性。[[10]](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Config-pipewire-media-session#matching-rules>)

将默认的配置文件 `/usr/share/pipewire/media-session.d/alsa-monitor.conf` 复制到 `/etc/pipewire/media-session.d/` 或是 `~/.config/pipewire/media-session.d/`。 随后添加一各新的规则块，类似下面这个： 
    
    /etc/pipewire/media-session.d/alsa-monitor.conf (or ~/.config/pipewire/media-session.d/alsa-monitor.conf)
    
    ...
    rules = {
        ...
        {
            matches = [
                {
                    node.name = "alsa_output._name-of-node_ "
                }
            ]
            actions = {
                update-props = {
                    audio.format = "S24_3LE"
                    audio.rate = 96000
                    # Following value should be doubled until audio does not cut out or other issues stop occurring
                    api.alsa.period-size = 128
    ...

在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 上： 
    
    /etc/wireplumber/wireplumber.conf.d/52-update-rate-and-format.conf (或 ~/.config/wireplumber/wireplumber.conf.d/52-update-rate-and-format.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            node.name = "alsa_output._设备节点名称_ "
          }
        ]
        actions = {
          update-props = {
            audio.format = "S24_3LE"          # 24位小端格式
            audio.rate = 96000                # 96kHz采样率
            # 此数值应逐步加倍直至解决断音问题
            api.alsa.period-size = 128        # 周期缓冲区大小
          }
        }
      }
    ]

`alsa_output._name-of-node_` 中的 node 可以使用 `pw-top` 获得。 

你的 DAC 可能支持不同的格式或是采样率，通过查询 [ALSA](<../zh-cn/ALSA.html> "ALSA") 您可以得知 DAC 支持什么： 

首先获取 DAC 的声卡号： 
    
    $ aplay -l
    
    ...
    card 3: S2 [Schiit Hel 2], device 0: USB Audio [USB Audio]
      Subdevices: 0/1
      Subdevice #0: subdevice #0
    ...
    
在这个例子中是 card 3。 然后获取所有受支持的采样率与格式： 
    
    $ cat /proc/asound/card _X_ /stream _X_
    
    ...
    Playback:
      ...
      Interface 1
        Altset 1
        Format: S16_LE
        Channels: 2
        Endpoint: 0x05 (5 OUT) (ASYNC)
        Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
        Data packet interval: 125 us
        Bits: 16
        ...
      Interface 1
        Altset 2
        Format: S24_3LE
        Channels: 2
        Endpoint: 0x05 (5 OUT) (ASYNC)
        Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
        Data packet interval: 125 us
        Bits: 24
        ...
      Interface 1
        Altset 3
        Format: S32_LE
        Channels: 2
        Endpoint: 0x05 (5 OUT) (ASYNC)
        Rates: 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
        Data packet interval: 125 us
        Bits: 32
        ...
    ...
    
上述输出表明 `S16_LE, S24_3LE, S32_LE` 是受支持的格式，`44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000` 是所有格式都支持的采样率。 

####  将音量升至 30% USB DAC 才出声

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 添加 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 相关指示 (在 [Talk:PipeWire](<../zh-cn/Talk:PipeWire.html>) 中讨论)

某些 USB DAC 在音量达到一定值前不会有输出 [[11]](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1117>)。通常这个值是 25% - 30%，而此时多半声音已经过响，还没法调小。解决方法是忽略硬件混音器的音量控制：将 `["api.alsa.soft-mixer"]` 设为 `true`。 

在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 下： 
    
    /etc/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf (或 ~/.config/wireplumber/wireplumber.conf.d/alsa-soft-mixer.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            device.name = "~alsa_card.*"  # 匹配所有ALSA声卡
          }
        ]
        actions = {
          update-props = {
            # 禁用硬件混音器音量控制，仅使用软件音量调节。
            # 混音器仍会根据所选端口静音未使用通路。
            api.alsa.soft-mixer = true
          }
        }
      }
    ]

然后重启 pipewire。将 `alsamixer` 的主音量设定好，随后使用root权限运行 `# alsactl store` 保存设置。您现在应该可以正常使用音量调节了。 

####  实时音频不起作用

如果 `pipewire.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")的 [status](</wzh/index.php?title=Unit_status&action=edit&redlink=1> "Unit status（页面不存在）") 出现了 `RTKit error: org.freedesktop.DBus.Error.AccessDenied`，这意味着 pipewire 守护进程的优先级不是实时。对于此问题，参见 [[12]](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1069>)。 

####  同时输出到同一声卡的多个 sink

复制一份 `/usr/share/alsa-card-profile/mixer/profile-sets/default.conf` 便于更改跨版本更新持久化。以下是一个将模拟输出和 HDMI 默认映射结合到一起的配置： 
    
    /usr/share/alsa-card-profile/mixer/profile-sets/multiple.conf
    
    [General]
    auto-profiles = no
    
    [Mapping analog-stereo]
    device-strings = front:%f
    channel-map = left,right
    paths-output = analog-output analog-output-lineout analog-output-speaker analog-output-headphones analog-output-headphones-2
    paths-input = analog-input-front-mic analog-input-rear-mic analog-input-internal-mic analog-input-dock-mic analog-input analog-input-mic analog-input-linein analog-input-aux analog-input-video analog-input-tvtuner analog-input-fm analog-input-mic-line analog-input-headphone-mic analog-input-headset-mic
    priority = 15
    
    [Mapping hdmi-stereo]
    description = Digital Stereo (HDMI)
    device-strings = hdmi:%f
    paths-output = hdmi-output-0
    channel-map = left,right
    priority = 9
    direction = output
    
    [Profile multiple]
    description = Analog Stereo Duplex + Digital Stereo (HDMI) Output
    output-mappings = analog-stereo hdmi-stereo
    input-mappings = analog-stereo

接着，配置 PipeWire 的 media-session，对匹配设备使用新的声卡配置。识别声卡信息可以使用 `$ pw-cli dump device`。 

在 [wireplumber](<https://archlinux.org/packages/?name=wireplumber>)包 上： 
    
    /etc/wireplumber/wireplumber.conf.d/51-alsa-custom.conf (或 ~/.config/wireplumber/wireplumber.conf.d/51-alsa-custom.conf)
    
    monitor.alsa.rules = [
      {
        matches = [
          {
            device.nick = "HDA Intel PCH"  # 匹配Intel板载声卡
          }
        ]
        actions = {
          update-props = {
            api.alsa.use-acp = true        # 启用ALSA卡配置文件
            api.acp.auto-profile = false   # 禁用自动配置集切换
            api.acp.auto-port = false      # 禁用自动端口切换
            device.profile-set = "multiple.conf"  # 指定配置集文件
            device.profile = "multiple"    # 使用多路输出配置
          }
        }
      }
    ]

在 [pipewire-media-session](<https://archlinux.org/packages/?name=pipewire-media-session>)包 上： 
    
    /etc/pipewire/media-session.d/alsa-monitor.conf (或 ~/.config/pipewire/media-session.d/alsa-monitor.conf)
    
    rules = [
        {
            matches = [ { alsa.card_name = "HDA Intel PCH" } ]  # 匹配Intel板载声卡
            actions = {
                update-props = {
                    api.alsa.use-acp = true
                    device.profile-set = "multiple.conf"
                    device.profile = "multiple"
                    api.acp.auto-profile = false
                    api.acp.auto-port = false
                }
            }
        }
    ]

####  Discord 没有提示音

这可能是由于 min.quantum 设置得过低，尝试将其修改到 700 以上。您可以为 Discord 专门写一个覆盖用的配置，只需在 pipewire-pulse.conf 的 pulse.rules 部分添加如下规则： 
    
    /etc/pipewire/pipewire-pulse.conf (or ~/.config/pipewire/pipewire-pulse.conf)
    
    ...
    pulse.rules = [
      ...
        {
            # Discord notification sounds fix
            matches = [ { application.process.binary = "Discord" } ]
            actions = {
                update-props = {
                    pulse.min.quantum      = 1024/48000     # 21ms
                }
            }
        }
    ...

####  FMOD 游戏在 PipeWire 下崩溃

某些使用旧版 [FMOD 音频引擎](<https://en.wikipedia.org/wiki/FMOD> "wikipedia:FMOD")的游戏（譬如 [Pillars of Eternity](<https://en.wikipedia.org/wiki/Pillars_of_Eternity> "wikipedia:Pillars of Eternity")）会运行 `pulseaudio --check` 并且在 PulseAudio 的二进制文件不存在的情形下崩溃。可以通过将 `/bin/pulseaudio` 链接至 `/bin/true` 来绕过这个问题。[[13]](<https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/1514>)
    
    # ln -s /bin/true /bin/pulseaudio
    
注意：重新安装 PulseAudio 需要移除此符号链接。 

####  自动切换不起作用

自动切换不起作用可能是由于 [WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber") 状态有问题。[这条评论](<https://gitlab.freedesktop.org/pipewire/wireplumber/-/issues/191#note_1252549>)指出可以删除 [WirePlumber](<../zh-cn/WirePlumber.html> "WirePlumber") 的本地状态并重启守护进程看看有没有用： 
    
    $ rm -r ~/.local/state/wireplumber/
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `wireplumber.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

####  从待机状态恢复时失去实时优先级/负载下音频爆裂

由于 rtkit [2011 年的一个 bug](<https://github.com/heftig/rtkit/issues/13>)，待机事件会取消 PipeWire 的实时优先级并且不会恢复。若想禁用造成问题的保护措施，[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `rtkit-daemon.service`： 
    
    /etc/systemd/system/rtkit-daemon.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/lib/rtkit-daemon --no-canary

然后重启 `rtkit-daemon.service` 和 `pipewire.service`，以及 media session 服务。 

####  在向 RAOP 设备推流时没有声音 (例如 Sonos)

使用 [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）") 或 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 设置 mDNS 域名解析。 

####  KDE Plasma 中未显示音频设备

PipeWire 客户端（包括桌面环境）可能依赖 [XDG_RUNTIME_DIR](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") [[14]](<https://specifications.freedesktop.org/basedir-spec/latest/#variables>) 来连接 PipeWire 守护进程。[[15]](<https://docs.pipewire.org/page_daemon.html>) 若登录后立即出现无声问题，可能是由于该变量被手动设置为错误路径。 

虽然手动重启 PipeWire 可暂时解决，但仍可能导致其他问题（如 Chromium 无法屏幕共享并报错 `pipewire context failed`）。`XDG_RUNTIME_DIR` 应由 [pam_systemd(8)](<https://man.archlinux.org/man/pam_systemd.8>) 自动设置，请检查并移除所有初始化文件中的手动设置。 

####  SDDM/LightDM 用户登录后设备音量未恢复

若使用 [SDDM](<../zh-cn/SDDM.html> "SDDM") 或 [LightDM](<../zh-cn/LightDM.html> "LightDM") 时发现登录后音量设置未保留，需为显示管理器的用户屏蔽 PipeWire，因其运行的 WirePlumber 会干扰用户会话： 
    
    # systemctl --user -M _user_ @ mask pipewire.socket
    
将 `_user_` 替换为 `sddm`（在SDDM上）或 `lightdm`（在LightDM上）。详见 [Debian Wiki article](<https://wiki.debian.org/PipeWire#Device_volume_for_SDDM_users_is_not_restored_on_login>)。 

####  终端铃声失效

从 PipeWire 角度，需加载 x11.bell 模块（默认配置已包含，可见上述配置文件）。请确认已安装 [pipewire-x11-bell](<https://archlinux.org/packages/?name=pipewire-x11-bell>)包 包。窗口管理器也可能影响终端铃声，例如 xfwm 需在终端设置中启用"声音提示"。重启服务测试： 
    
    $ systemctl --user restart pipewire
    
可通过以下命令测试铃声： 
    
    $ echo $'\a'
    
###  视频

####  OBS 等程序即使请求了窗口/屏幕却仍旧什么都不显示

如果您确定自己已经安装了 [xdg-desktop-portal](<https://archlinux.org/packages/?name=xdg-desktop-portal>)包 以及 [xdg-desktop-portal-gtk](<https://archlinux.org/packages/?name=xdg-desktop-portal-gtk>)包 和 [xdg-desktop-portal-kde](<https://archlinux.org/packages/?name=xdg-desktop-portal-kde>)包 两者之一，请检查守护程序的运行状态。 

在 OBS 中，如果一切工作正常，您应该会在 `stdout` 看到如下输出： 
    
    ...
    info: [pipewire] desktop selected, setting up screencast
    info: [pipewire] created stream 0x5632d7456850
    info: [pipewire] playing stream…
    
对于多显示器配置，[slurp](<https://archlinux.org/packages/?name=slurp>)包 可以用于捕获所有屏幕。 

##  参阅

  * [Wiki](<https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/home>)——Freedesktop GitLab 上的 PipeWire Wiki
  * [Pipewire Update Blog Post](<https://blogs.gnome.org/uraeus/2018/01/26/an-update-on-pipewire-the-multimedia-revolution-an-update/>)——一篇 2018 年 1 月的描述当时 PipeWire 状态的博文
  * [PipeWire Late Summer Update 2020](<https://blogs.gnome.org/uraeus/2020/09/04/pipewire-late-summer-update-2020/>)——2020 年 9 月的一篇博文
