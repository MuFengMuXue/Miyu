**翻译状态：**

  * 本文（或部分内容）译自 [Timidity++](<https://wiki.archlinux.org/title/Timidity%2B%2B> "arch:Timidity++")，最近一次同步于 2024-05-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Timidity%2B%2B?diff=0&oldid=808987>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Timidity%2B%2B_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[TiMidity++](<https://timidity.sourceforge.net/>) 是用于在不使用硬件合成器的情况下播放 MIDI 文件的[软件合成器](<../zh-cn/MIDI.html#%E5%90%88%E6%88%90%E5%99%A8> "MIDI")。它可以实时将 MIDI 翻译给声卡，或是将成果存储到文件中，比如存储到 [PCM](<https://en.wikipedia.org/wiki/PCM> "wikipedia:PCM")[ _.wav_](<https://en.wikipedia.org/wiki/WAV> "wikipedia:WAV") 文件格式。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [timidity++](<https://archlinux.org/packages/?name=timidity%2B%2B>)包 包。 

你还应当安装[音色库（SoundFont）](<https://en.wikipedia.org/wiki/SoundFont> "wikipedia:SoundFont")或 [Gravis UltraSound](<https://en.wikipedia.org/wiki/Gravis_UltraSound> "wikipedia:Gravis UltraSound")（GUS） 补丁文件来获得产生音频的能力。参见 [MIDI#SoundFont 列表](<../zh-cn/MIDI.html#SoundFont_%E5%88%97%E8%A1%A8> "MIDI")

如果你使用 [pipewire](<https://archlinux.org/packages/?name=pipewire>)包，由于 TiMidity++ 有时依赖 [ALSA](<../zh-cn/ALSA.html> "ALSA") 工作，你需要安装 [pipewire-alsa](<https://archlinux.org/packages/?name=pipewire-alsa>)包。 

##  配置

将下面的配置加入到 [timidity.cfg(5)](<https://man.archlinux.org/man/timidity.cfg.5>) 来选用你想用的音色库。 

FreePats： 
    
    /etc/timidity/timidity.cfg
    
    soundfont /usr/share/soundfonts/freepats-general-midi.sf2
    
Fluid： 
    
    /etc/timidity/timidity.cfg
    
    soundfont /usr/share/soundfonts/FluidR3_GM.sf2
    
###  守护进程

如果你希望将 TiMidity++ 用作 ALSA 的音序器，你应当将用户加入到 `audio` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。就像大部分用户组更改一样，你可能需要重启会话（比如登出后再登入），来使新加入的组可以通过 `groups` 指令显示出来。 

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `timidity.service` 用户单元。注意，当你没有在加入 `audio` 组后没有重启会话时，你可能无法正常启动这个服务。 

使用 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 的环境下，这个服务可能无法启动。你可能需要在你的桌面环境中将下列指令设为[自启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")项。如果你只想以守护进程模式运行 TiMidity++ 一次，你也可以直接使用这串指令来获得相对更易读的终端输出。 
    
    $ timidity -iA
    
##  用例

###  播放文件

TiMidity++ 有两种用法：将它用作一个 MIDI 播放器，或是为 [ALSA](<../zh-cn/ALSA.html> "ALSA") 添加 MIDI 支持的守护进程。 

####  独立模式

你可以用 TiMidity++ 播放 MIDI 文件： 
    
    $ timidity _example.mid_
    
`-in` 选项会唤出一个基于文本的界面。TiMidyty++ 还有很多其他选项。详见 [timidity(1)](<https://man.archlinux.org/man/timidity.1>) 或使用 `-h` 选项。 

####  守护进程模式

如果你选择将 TiMidity++ 用作[守护进程](<#%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B>)，它将为 [rosegarden](<../zh-cn/Rosegarden.html> "Rosegarden")、aplaymidi、vkeybd 之类的程序提供 MIDI 输出支持。 

Timidity++ 会提供软 MIDI 接口（如果你的系统有硬件 MIDI 接口的话，就会另外创建一些）： 
    
    $  aconnect -o
    
    client 128: 'TiMidity' [type=user]
        0 'TiMidity port 0 '
        1 'TiMidity port 1 '
        2 'TiMidity port 2 '
        3 'TiMidity port 3 '

你现在可以如此播放 MIDI 文件： 
    
    $ aplaymidi _filename.mid_ --port 128:0
    
另一个典型例子是 **vkeybd** ，一个 X 下的虚拟 MIDI 键盘。 

你可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vkeybd](<https://aur.archlinux.org/packages/vkeybd/>)AUR，然后如此使用： 
    
    $ vkeybd --addr 128:0
    
选项 `--addr 128:0` 将软件 MIDI 输入接口（本例是由 vkeybd 提供的）连接到第一个 ALSA 输出接口（本例中是由 Timidity++ 提供的）。另外，你也可以使用 aconnect，[patchage](<https://aur.archlinux.org/packages/patchage/>)AUR 或是 kaconnect。最终，当你使用 vkeybd 提供的按键弹奏时，TiMidity++ 将演奏出恰当的乐声。 

####  连接到虚拟 MIDI 设备

如果你有一个 Timidyty++ 守护进程和 aplaymidi 一起运行，你可以将这个守护进程与虚拟 MIDI 设备连接，来使 rosegarden 或 scala 之类的程序运行。 

加载 `snd-virmidi` 内核模块。如果你愿意，也可以让系统[启动时加载模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E8%87%AA%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9D%97> "内核模块")。 

用 acconnect 来确认接口数： 
    
    $ aconnect -o
    
    client 14: 'Midi Through' [type=kernel]
         0 'Midi Through Port-0'
     client 20: 'Virtual Raw MIDI 1-0' [type=kernel]
         0 'VirMIDI 1-0     '
     client 21: 'Virtual Raw MIDI 1-1' [type=kernel]
         0 'VirMIDI 1-1     '
     client 22: 'Virtual Raw MIDI 1-2' [type=kernel]
         0 'VirMIDI 1-2     '
     client 23: 'Virtual Raw MIDI 1-3' [type=kernel]
         0 'VirMIDI 1-3     '
     client 128: 'TiMidity' [type=user]
         0 'TiMidity port 0 '
         1 'TiMidity port 1 '
         2 'TiMidity port 2 '
         3 'TiMidity port 3 '

然后创建连接： 
    
    $ aconnect 20:0 128:0
    
现在，系统中的 `/dev/snd/midiC1D0` MIDI 虚拟输出设备应该可以使用了。 

##  小技巧

###  转换文件

Timidity++ 可以将 MIDI 文件转为其他格式。下列指令将结果输出到 WAV 文件中： 
    
    $ timidity _input.mid_ -Ow -o _out.wav_
    
用 [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") 可以转为其他模式。此例转为 mp3： 
    
    $ timidity _input.mid_ -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 256k _out.mp3_
    
###  如何使 DOSBox 使用 TIMIdity++

**注意：** 下列方法测试于 [DOSBox](<../zh-cn/DOSBox.html> "DOSBox") 0.72 版本。

首先，你需要写配置。在 [DOSBox](<../zh-cn/DOSBox.html> "DOSBox") 中输入下列指令创建配置文件： 
    
    config -writeconf dosbox.conf
    
你可以将 [[ic|dosbox.conf}} 替换成任何你想要的名字。如果你想要隐藏文件，在文件名前加点。 

在执行下列指令前，使用 _aconnect_ 指令以确保 Timidity++ 已经作为守护进程启动。 

使用任何编辑器编辑配置，你需要直接跳转到此节： 
    
    dosbox.conf
    
    [midi]
    mpu401=intelligent
    device=default
    config=

把 ALSA 连接端口写到 _config=_ 后，默认是： 
    
    config=128:0
    
在终端中重启 DOSBox 以阅读调错信息。情况下，你应该看见 128:0 接口已成功初始化。 

##  疑难解惑

###  TiMidity++ 并不能播放 MIDI 文件

可能是你的声音文件没有正确配置。运行： 
    
    $ timidity _example.mid_
    
如果终端输出如下，那么你的声音文件可能没有正确配置。 
    
    No instrument mapped to tone bank 0, program XX - \
    this instrument will not be heard
    
确保你已经安装了声音文件，并且你的声音文件已经列入 `/etc/timidity/timidyty.cfg`。详见[#配置](<#%E9%85%8D%E7%BD%AE>)。 

###  守护进程模式下，播放声音速度过快

TiMidity++ 的默认 ALSA 输出模块可能在 ALSA 服务模式下导致这个问题。尝试其他输出选项，例如 **libao** ： 
    
    $ timidity -iA -OO
    
然后用 aplaymidi 测试。如果不起效，你可能需要配置 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）") 然后将 Timidity++ 的输出改到 JACK 上。 

##  参见

  * [USB MIDI 键盘](</wzh/index.php?title=USB_MIDI_%E9%94%AE%E7%9B%98&action=edit&redlink=1> "USB MIDI 键盘（页面不存在）")
