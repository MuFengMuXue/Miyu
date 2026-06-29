**翻译状态：**

  * 本文（或部分内容）译自 [FluidSynth](<https://wiki.archlinux.org/title/FluidSynth> "arch:FluidSynth")，最近一次同步于 2024-8-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/FluidSynth?diff=0&oldid=816168>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FluidSynth_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 英文页面的更改不少。 (在[Talk:FluidSynth](<../zh-cn/Talk:FluidSynth.html>)讨论)

[FluidSynth](<https://www.fluidsynth.org/>) 是一款基于 SoundFont 2 规范的实时软件合成器。[gst-plugins-bad](<https://archlinux.org/packages/?name=gst-plugins-bad>)包 可选择使用它。 

[OpenTTD](<../zh-cn/OpenTTD.html> "OpenTTD") 与 [MPD](<../zh-cn/MPD.html> "MPD") 默认依赖于 FluidSynth。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [fluidsynth](<https://archlinux.org/packages/?name=fluidsynth>)包 软件包。 

还需要一个 [SoundFont](<https://en.wikipedia.org/wiki/SoundFont> "wikipedia:SoundFont")。参见 [MIDI#SoundFont 列表](<../zh-cn/MIDI.html#SoundFont_%E5%88%97%E8%A1%A8> "MIDI")以获取 SoundFonts 列表。 

##  用法

使用 FluidSynth 有两种方式。要么作为 [MIDI](<../zh-cn/MIDI.html> "MIDI") 播放器，要么作为向 [ALSA](<../zh-cn/ALSA.html> "ALSA") 添加 MIDI 支持的守护进程。 

###  独立模式

您可以简单地使用 fluidsynth 播放 MIDI 文件： 
    
    $ fluidsynth -a alsa -m alsa_seq -l -i /usr/share/soundfonts/FluidR3_GM.sf2 example.mid
    
假设你安装了 [soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包。 

FluidSynth 还有许多其他选项，请参见 [fluidsynth(1)](<https://man.archlinux.org/man/fluidsynth.1>) 或使用 `-h` 获取帮助。 

用户可能希望使用 `pipewire` 或 `pulseaudio` 代替 `alsa` 作为 -a 选项的参数。 

**提示：** 如果为默认 SoundFont 创建了符号链接（例如 
    
    ln -s FluidR3_GM.sf2 /usr/share/soundfonts/default.sf2

），则无需每次都指定 SoundFont。

###  ALSA 守护进程模式

如果希望 fluidsynth 作为 ALSA 音序器客户端运行，请编辑 `/etc/conf.d/fluidsynth` 并添加 SoundFont 和其他修改。例如，Fluid： 
    
    SOUND_FONT=/usr/share/soundfonts/FluidR3_GM.sf2
    OTHER_OPTS='-a alsa -m alsa_seq -r 48000'
    
然后，您就可以[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `fluidsynth.service`。 

**注意：** 如果使用 pulseaudio 驱动程序，则不能使用 root 启动 fluidsynth 服务。Pulseaudio 不允许 root 连接，因为 Pulseaudio 服务器通常由用户（而非 root）启动。因此，该服务是作为[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")提供的。

下面将提供一个软件 MIDI 输出端口（除了系统上的硬件 MIDI 端口（如果有的话））： 
    
    $ aconnect -o
    
    client 128: 'FLUID Synth (5117)' [type=user]
       0 'Synth input port (5117:0)'

aplaymidi 就是一个用法例子： 
    
    $ aplaymidi -p128:0 example.mid
    
**注意：** 要在实时设置中实现低延迟，必须设置 [FluidSynth wiki](<https://github.com/FluidSynth/fluidsynth/wiki/LowLatency>) 中描述的 RATE/NUM/SIZE 参数。这些参数的常用值和其他提示也在[专业音频#JACK 参数](<../zh-cn/%E4%B8%93%E4%B8%9A%E9%9F%B3%E9%A2%91.html#JACK_%E5%8F%82%E6%95%B0> "专业音频")中列出。

### SDL_Mixer

要在使用 SDL_Mixer 的程序中使用 fluidsynth，需要指定 soundfont： 
    
     $ SDL_SOUNDFONTS=/usr/share/soundfonts/FluidR3_GM.sf2 ./program
    
##  提示与技巧

###  将 MIDI 转换为 MP3/OGG

需要 [soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包 或其他任意 SoundFont。 

`/usr/share/soundfonts` is the default location of FluidR3_GM 

用简单的命令行将 midi 转为 mp3： 
    
    $ fluidsynth -l -T raw -F - /usr/share/soundfonts/FluidR3_GM.sf2 example.mid | twolame -b 256 -r - example.mp3 
    
需要 [twolame](<https://archlinux.org/packages/?name=twolame>)包。 

用简单的命令行将 midi 转为 ogg： 
    
    $ fluidsynth -nli -r 48000 -o synth.cpu-cores=2 -T oga -F example.ogg /usr/share/soundfonts/FluidR3_GM.sf2 example.MID
    
这是一个将多个 midi 文件并行转换为 ogg 的小脚本： 
    
    #!/bin/bash
    maxjobs=$(grep processor /proc/cpuinfo | wc -l)
    midi2ogg() {
    	name=$(echo $@ | sed -r s/[.][mM][iI][dD][iI]?$//g | sed s/^[.][/]//g)
    	for arg; do 
    	fluidsynth -nli -r 48000 -o synth.cpu-cores=$maxjobs -F "/dev/shm/$name.raw" /usr/share/soundfonts/FluidR3_GM.sf2 "$@"
    	oggenc -r -B 16 -C 2 -R 48000 "/dev/shm/$name.raw" -o "$name.ogg"
    	rm "/dev/shm/$name.raw"
    	## Uncomment for replaygain tagging
    	#vorbisgain -f "$name.ogg" 
    	done
    }
    export -f midi2ogg
    find . -regex '.*[.][mM][iI][dD][iI]?$' -print0 | xargs -0 -n 1 -P $maxjobs bash -c 'midi2ogg "$@"' --
    
##  问题解决

###  与 PulseAudio 冲突

如果 _fluidsynth_ 应用程序被设置为使用 `alsa` 作为驱动程序，声卡将被直接访问，PulseAudio 和使用 PulseAudio 的应用程序将无法正常工作。您可以修改配置文件 `/etc/conf.d/fluidsynth`，将驱动程序更改为 `pulseaudio`，然后重启 _fluidsynth_ 和 PulseAudio： 
    
    /etc/conf.d/fluidsynth
    
    OTHER_OPTS='-a pulseaudio -m alsa_seq -r 48000'
