**翻译状态：**

  * 本文（或部分内容）译自 [MIDI](<https://wiki.archlinux.org/title/MIDI> "arch:MIDI")，最近一次同步于 2025-01-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/MIDI?diff=0&oldid=824537>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MIDI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MIDI](<https://en.wikipedia.org/wiki/MIDI> "wikipedia:MIDI") 本身是"乐器数字接口"（Musical Instrument Digital Interface）的缩写，是乐器与任何能理解这种语言的设备之间的通信协议和标准。它可以用来控制一系列合成器，让铁罐发出鼓的声音，甚至操作工业设备。 

不过，本文的讨论范围主要集中在计算机系统中使用 MIDI 播放包含 MIDI 数据的文件。这些文件的扩展名通常为 `.mid`，在多媒体计算机共享音乐的黄金时代大受欢迎。在专业音乐创作/编曲中，它仍然发挥着重要作用。 

##  MIDI 文件

在此不赘述该格式的具体内容，只需了解 MIDI 文件（如 `foobar.mid` ）不包含任何数字音频数据，因此没有 "PCM 流"。一个常见的误解是，MIDI 是一种声音文件格式，因此人们通常会抱怨音乐播放器应用程序无法播放该文件。下面是一个非常适合初学者的 MIDI/MID 文件概述： 
    
    **# FOOBAR.MID**
    Note ON
      _Use Instrument #1_
      _Play Note C1_
      _Set Volume at 100_
      _Set Pitch at 50_
    
为了让这样的文件发挥作用，需要有一个"引擎"能将数据转化为音乐。这个引擎有一个"音色发生器"，也就是我们所说的"合成器"。因此，任何可以在没有 MIDI 功能硬件（计算机的声音设备）的情况下播放 MIDI 文件的播放器都内置或使用外置合成器。一个典型的键盘（不是你正在打字的键盘）实际上由两部分组成——一个 MIDI "控制器"（琴键）和一个合成器（音调发生器/模块；发出声音的东西）。 

所以，到此为止，您应该能够理解： 

  * 需要有一个合成器来播放 MIDI 文件。
  * 合成器可以是硬件，也可以是软件。
  * 大多数计算机声卡/芯片组都没有合成器。
  * 您需要一台拥有适当"音色库"（音色集合）的合成器，才能尽享 MIDI 文件的魅力。
  * 如果音色库中没有某种乐器，那么合成器将不会使用该乐器演奏任何音符。
  * 如果文件中的某一乐器与音色库中的另一乐器相对应，合成器就会发出不同的声音（显而易见）。

##  General MIDI 音色库

[General MIDI](<https://en.wikipedia.org/wiki/General_MIDI> "wikipedia:General MIDI")（GM）是对许多 MIDI 相关事项进行标准化的规范，特别是声音集合中的乐器布局。与General MIDI 兼容的"音色库"意味着它符合 General MIDI 的标准，只要 MIDI 文件也与 General MIDI 兼容（没有特别的规定，如引入新的乐器或将乐器放在音色库的不同位置），重放就会按预期进行，因为音色库为 MIDI 信息/事件提供了正确的乐器/处理程序。最流行的音色库格式之一是 [SoundFont](<https://en.wikipedia.org/wiki/SoundFont> "wikipedia:SoundFont")，尤其是 _SF2_ 。另一种流行格式是 [Gravis UltraSound](<https://en.wikipedia.org/wiki/Gravis_UltraSound> "wikipedia:Gravis UltraSound")（GUS）补丁文件。 

  * 如果您的声卡可以使用 SoundFont，您可以将 **.sf2** 文件加载到声卡上。
  * 如果没有可以使用音色的声卡（基本上没有硬件合成器），可以使用软件合成器并加载 SF2 文件。反过来，您也可以想办法在全局范围内使用该合成器。

###  SoundFont 列表

  * **FatBoy** — 用于经典视频游戏 MIDI、模拟和一般用途的免费 GM/GS SoundFont。

     <https://web.archive.org/web/20220124174052/https://fatboy.site/> || [soundfont-fatboy](<https://aur.archlinux.org/packages/soundfont-fatboy/>)AUR

  * **Fluid** — Frank Wen 的专业级 GM/GS soundfont。

     <https://web.archive.org/web/20020804030405/http://www.jazzybee.com/fluid/> || [soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包

  * **FreePats** — 自由开放的通用 MIDI 声音集。

     <https://web.archive.org/web/20240925205657/https://freepats.zenvoid.org/SoundSets/general-midi.html> || [freepats-general-midi](<https://archlinux.org/packages/?name=freepats-general-midi>)包

  * **GeneralUser GS** — S. Christian Collins 制作的与 GM 和 GS 兼容的 SoundFont 库，用于作曲、播放 MIDI 文件和复古游戏。

     <https://www.schristiancollins.com/generaluser.php> || [soundfont-generaluser](<https://aur.archlinux.org/packages/soundfont-generaluser/>)AUR（此包已过时）

AUR 中还有许多其他 SoundFonts，例如：[search for soundfont-](<https://aur.archlinux.org/packages?K=soundfont->)。另请参阅 [FluidSynth Wiki](<https://github.com/FluidSynth/fluidsynth/wiki/SoundFont>)。 

###  Gravis UltraSound patch 列表

  * **FreePats (legacy)** — FreePats 通用 MIDI 音效集的旧版本，最初由 Eric A. Welsh 制作。

     <https://web.archive.org/web/20240925205657/https://freepats.zenvoid.org/SoundSets/general-midi.html#OldFreePatsGM> || [freepats-legacy](<https://aur.archlinux.org/packages/freepats-legacy/>)AUR

SoundFonts 可通过 [unsf-git](<https://aur.archlinux.org/packages/unsf-git/>)AUR 软件包中的命令行工具 _unsf_ 转换为 Gravis UltraSound 补丁集。 

##  硬件播放

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** More details on soundcards and MIDI, possibly links to SBLive MIDI here... (在 [Talk:MIDI](<../zh-cn/Talk:MIDI.html>) 中讨论)

If you simply need to play a MIDI file on a MIDI-capable hardware device (e.g. a hardware synthesizer), you can use the `aplaymidi` command from [alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包. 

To get the list of the available MIDI ports, use the command 
    
    $ aplaymidi -l
    
Then to play a MIDI file, specify it along with an available port of the preferred MIDI device that you got from the output of the previous command. For example like this: 
    
    $ aplaymidi -p 24:0 midi_file.mid
    
### SB Audigy 1 - Emu10k1 WaveTable

First, make sure that the **Synth** mixer control is not muted and that **Audigy Analog/Digital output Jack** is set to **[Off]**. 

To check and adjust them, use `alsamixer` or your mixer of choice. 

Next, build and install the [awesfx](<https://aur.archlinux.org/packages/awesfx/>)AUR package from the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"). Then, load a SoundFont file on the Emux WaveTable, like so: 
    
    $ asfxload /path/to/any/file.sf2
    
The .SF2 file can be any SoundFont. If you have access to _2GMGSMT.SF2_ on Windows, you can use that one. 

You should be all set now. To play your .mid files with `aplaymidi`, you will have to do as follows: 

Get a list of the available MIDI ports by running 
    
    $ aplaymidi -l
    
    Port    Client name                      Port name
    14:0    Midi Through                     Midi Through Port-0
    28:0    SB Live! 5.1 [SB0060]            EMU10K1 MPU-401 (UART)
    29:0    Emu10k1 WaveTable                Emu10k1 Port 0
    29:1    Emu10k1 WaveTable                Emu10k1 Port 1
    29:2    Emu10k1 WaveTable                Emu10k1 Port 2
    29:3    Emu10k1 WaveTable                Emu10k1 Port 3
    
Then, pick an available "Emu10k1 WaveTable" MIDI port, in this case 29:0, and specify it as such: 
    
    $ aplaymidi -p 29:0 midi_file.mid
    
##  软件播放

"那为什么我可以用 Windows Media Player 播放 MIDI？" 

这是因为 Windows 有一个默认的全局软件合成器。即便如此，它也无法达到现代电脑应有的质量。如果有办法在 Linux 上做到这一点，你也可以从任何播放器回放 MIDI。也许可以在声音服务器中安装一个 MIDI 服务器（可容纳所选的合成器），如 Phonon 或 PulseAudio。不过，目前还没有实现这类功能，你只能用带有合成器源插件或合成器本身的播放器或声音服务器播放 MIDI。 

###  合成器

#### FluidSynth

为 ALSA 添加 MIDI 支持的 MIDI 播放器和守护进程。它只支持 SoundFonts。请参阅 [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth")。 

####  TiMidity++

MIDI 转 WAVE 转换器和播放器。它支持 SoundFonts 和 Gravis UltraSound 补丁文件。请参阅 [Timidity++](<../zh-cn/Timidity++.html> "Timidity++")。 

#### WildMIDI

[WildMIDI](<https://github.com/Mindwerks/wildmidi>) 是一款简单的 MIDI 播放器软件。它使用 Gravis UltraSound 补丁文件将 MIDI 文件转换为音频。目前还不支持 SoundFonts。[[1]](<https://github.com/Mindwerks/wildmidi/issues/8>) 要使用它，需要一个指向 GUS 补丁的配置文件 [wildmidi.cfg(5)](<https://man.archlinux.org/man/wildmidi.cfg.5>)： 
    
    /etc/wildmidi/wildmidi.cfg
    
    dir _/path/to/any_
    source _/path/to/any_ /timidity.cfg

配置文件格式大多与 TiMidity++ 兼容。 

您可以简单地使用 WildMIDI 播放 MIDI 文件： 
    
    $ wildmidi example.mid
    
将 MIDI 文件转换为 WAV 格式： 
    
    $ wildmidi example.mid -o example.wav
    
更多选项请参见 [wildmidi(1)](<https://man.archlinux.org/man/wildmidi.1>) 。 

### Players

#### GStreamer-based players

MIDI files can be played in GNOME Videos and all other players using [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") as backend after having installed [gst-plugins-bad](<https://archlinux.org/packages/?name=gst-plugins-bad>)包 and a SoundFont ([soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包 for example). It uses [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") as synthesizer and picks up the first usable SoundFont from the `/usr/share/soundfonts/` directory. 

#### VLC

The FluidSynth plugin provides MIDI playback support for [VLC](<../zh-cn/VLC_%E5%AA%92%E4%BD%93%E6%92%AD%E6%94%BE%E5%99%A8.html> "VLC") using [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") as synthesizer. A SoundFont needs to be installed, and VLC will detect it automatically. If multiple SoundFonts are installed, you can choose one in VLC preferences (_Tools > Preferences_): you have to show all settings. Then, go to _Input/Codecs > Audio codecs > FluidSynth_. 

And, if you installed e.g. Fluid, set the location to: 
    
    /usr/share/soundfonts/FluidR3_GM.sf2
    
#### Audacious

The AMIDI-Plug from the [audacious-plugins](<https://archlinux.org/packages/?name=audacious-plugins>)包 package provides MIDI playback support for [Audacious](<../zh-cn/Audacious.html> "Audacious") using [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") as synthesizer. You can specify the SoundFont to use for playback in the settings of its MIDI output plugin (_File > Preferences > Plugins > Input > AMIDI-Plug > Preferences_). 

#### DeaDBeeF

[deadbeef](<https://aur.archlinux.org/packages/deadbeef/>)AUR player is able to play MIDI files via its WildMidi player plugin. It does not support SoundFonts, just Gravis UltraSound patch files. You can specify the configuration file location in DeaDBeeF by going to _Edit > Preferences > Plugins > WildMidi Player > Configure_. 

#### Drumstick

Drumstick MIDI File Player is able to play MIDI files using [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") as synthesizer. Install [dmidiplayer](<https://aur.archlinux.org/packages/dmidiplayer/>)AUR. 
