**翻译状态：**

  * 本文（或部分内容）译自 [Advanced_Linux_Sound_Architecture](<https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture> "arch:Advanced Linux Sound Architecture")，最近一次同步于 2025-07-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture?diff=0&oldid=841827>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 本文疑似机翻，许多用词不自然、不准确。（在 [Talk:ALSA#](<../zh-cn/Talk:ALSA.html>) 中讨论）

相关文章

  * [/配置范例](</wzh/index.php?title=ALSA/%E9%85%8D%E7%BD%AE%E8%8C%83%E4%BE%8B&action=edit&redlink=1> "ALSA/配置范例（页面不存在）")
  * [/疑难解答](<../zh-cn/ALSA/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "ALSA/疑难解答")
  * [PC 扬声器](<../zh-cn/PC_%E6%89%AC%E5%A3%B0%E5%99%A8.html> "PC 扬声器")
  * [PipeWire](<../zh-cn/PipeWire.html> "PipeWire")
  * [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")
  * [音频系统](<../zh-cn/%E9%9F%B3%E9%A2%91%E7%B3%BB%E7%BB%9F.html> "音频系统")
  * [应用程序列表/多媒体#音量控制](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E9%9F%B3%E9%87%8F%E6%8E%A7%E5%88%B6> "应用程序列表/多媒体")

[高级 Linux 声音体系](<https://zh.wikipedia.org/wiki/ALSA> "zhwp:ALSA")（Advanced Linux Sound Architecture，(ALSA) ）提供声卡的[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")驱动，代替了原来的[Open Sound System](<../zh-cn/Open_Sound_System.html> "Open Sound System") (OSS)。 

除了声音设备驱动，ALSA还捆绑了一个用户空间驱动的库用于应用开发。开发者可以使用这些 ALSA 驱动进行高级 API 开发，可以通过 ALSA 库达成与声音设备的内核（直接）交互。 

**提示：** ALSA 相关术语的解释—— _interface_ , _card_ , _device_ (一个 _card_ 不是一个 _device_), _subdevice_ , 以及更多 - 可以在 [Wikipedia:Advanced Linux Sound Architecture#Concepts](<https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture#Concepts> "wikipedia:Advanced Linux Sound Architecture")找到

##  安装

ALSA 驱动是内核的一部分，ALSA 库([alsa-lib](<https://archlinux.org/packages/?name=alsa-lib>)包)通常作为[依赖](<../zh-cn/PKGBUILD.html#%E4%BE%9D%E8%B5%96%E5%85%B3%E7%B3%BB> "PKGBUILD")安装，故无需手动安装。 

[udev](<../zh-cn/Udev.html> "Udev")会在系统启动时自动检测硬件并选择所需的驱动，并加载相应的声音设备驱动模块。所以你的声卡应当已经可以工作了. 

然而在一开始声音可能被静音了。这种情况下见[#解除频道静音](<#%E8%A7%A3%E9%99%A4%E9%A2%91%E9%81%93%E9%9D%99%E9%9F%B3>)。 

###  固件

笔记本电脑通常需要[Sound Open Firmware](<https://www.sofproject.org/>) (SOF) ([sof-firmware](<https://archlinux.org/packages/?name=sof-firmware>)包)——他们倾向于使用 Cadence Tensilica Xtensa 架构[DSP](<https://en.wikipedia.org/wiki/Digital_signal_processor> "wikipedia:Digital signal processor")s，请参阅[支持的平台](<https://thesofproject.github.io/latest/platforms/>)列表。如果固件丢失，[日志](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")将提供以下消息： 
    
    error: sof firmware file is missing
    
    error: failed to load DSP firmware -2
    
    error: sof_probe_work failed err: -2
    
有关更多 SOF 故障排除信息，请参阅[英特尔硬件平台概述](<https://thesofproject.github.io/latest/getting_started/intel_debug/introduction.html>). 

装有Cirrus Logic[智能放大器](<https://www.cirrus.com/products/audio/boosted-amplifiers/laptop-audio>)的笔记本电脑需要[linux-firmware-cirrus](<https://archlinux.org/packages/?name=linux-firmware-cirrus>)包包。参考： 

  * [Audio drivers for Cirrus Logic CS35L54/56/57/63 Boosted Smart Amplifiers](<https://docs.kernel.org/sound/codecs/cs35l56.html>),

  * [archlinux/packaging/packages/linux-firmware#19](<https://gitlab.archlinux.org/archlinux/packaging/packages/linux-firmware/-/issues/19>).

某些英特尔音频设备需要[linux-firmware-intel](<https://archlinux.org/packages/?name=linux-firmware-intel>)包包。 

[alsa-firmware](<https://archlinux.org/packages/?name=alsa-firmware>)包包含[一些声卡](<https://github.com/alsa-project/alsa-firmware>)可能需要的固件。 

See also [#Cards and modules](<#Cards_and_modules>) and [Linux firmware](<../zh-cn/Linux_firmware.html> "Linux firmware"). 

###  ALSA 实用程序

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading")软件包 [alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包。其包含 `alsamixer` 、 `amixer` 等实用程序。 _amixer_ 是一个用于更改音频设置的shell命令，而 _alsamixer_ 则提供了一个较为直观的，基于[ncurses](<https://en.wikipedia.org/wiki/Ncurses> "wikipedia:Ncurses")的界面，用于配置声音设备。 

###  ALSA 和 Systemd

[alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包 软件包默认包含了 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元配置文件 `alsa-restore.service` 和 `alsa-state.service`。 

在安装时它们会自动安装并激活（通过软件包提供的指向[sound.target](<../zh-cn/Systemd.html#%E7%9B%AE%E6%A0%87%EF%BC%88target%EF%BC%89> "Systemd")的符号链接）。选项如下所述： 

  * `alsa-restore.service`默认在启动时读取`/var/lib/alsa/asound.state`，并在关机时写入更新值。由于 `/etc/alsa/state-daemon.conf`不存在，除非用户有意识的创建。

  * `alsa-state.service`在守护进程模式下（重新）启动alsactl 以持续跟踪并保持音量改变,前提是用户有意识的创建了`/etc/alsa/state-daemon.conf`。

显然，这两种方法是互斥的,您可以根据自己的要求决定选择两种方法之一。要编辑这些单位，参考[systemd#修改现存单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd"). 您可以用[systemctl](<../zh-cn/Systemd.html> "Systemctl")查看他们的状态。 

了解更多信息，参考[alsactl(1)](<https://man.archlinux.org/man/alsactl.1>). 

###  用户权限

本地用户有权限播放音频和更改混音器水平。要允许远程用户使用 ALSA，您需要将这些用户[添加](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户和用户组")到`audio`组。 

**注意：** 将用户添加到`audio`组允许直接访问设备。请记住，这允许应用程序专门保留输出设备。这可能会破坏多座系统上的软件混合或快速用户切换。因此，默认情况下不建议将用户添加到`audio`组，除非您有特殊[需求](<https://wiki.ubuntu.com/Audio/TheAudioGroup>)。

###  OSS 模拟

[OSS 模拟](<https://docs.kernel.org/sound/designs/oss-emulation.html>)有拦截[OSS](<../zh-cn/Open_Sound_System.html> "OSS")呼叫并通过 ALSA 重新路由它们的能力。此模拟层非常有用，例如，对于尝试打开`/dev/dsp` 并直接向它们写入声音数据的老旧应用程序，如果没有 OSS 或模拟库，将会缺少`/dev/dsp`，应用程序将不会产生任何声音。 

如果您希望 OSS 应用程序与[dmix](<#Software_mixing>)一起使用，请同时安装[alsa-oss](<https://archlinux.org/packages/?name=alsa-oss>)包包。 

[加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9D%97> "内核模块") `snd_pcm_oss`和`snd_seq_oss`内核模块。将它们配置为在[启动时加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#systemd> "内核模块")。 

##  解除频道静音

ALSA 默认静音所有声道，必须手动解除。 

###  使用amixer解除静音

可以使用 `amixer` 解除声卡的主音量静音： 
    
    $ amixer sset Master unmute
    $ amixer sset Speaker unmute
    $ amixer sset Headphone unmute
    
###  使用alsamixer解除静音

使用 `alsamixer` 可以解除声卡的静音： 
    
    $ alsamixer
    
声道下方标有 `MM` 表示其已经静音，而标有 `00` 表示已经启用。 

使用 `←` 和 `→` 键滚动到 `Master` 和 `PCM` 声道，按下 `m` 键解除静音。 

使用 `↑` 键增加音量，获得`0`dB的增益。增益值可在左上方 `Item:` 字段旁边看到。 

**注意：** 若增益高于0 dB，可能会听到失真。

###  解除5.1/7.1声音的静音

要想得到完整的 [5.1](<https://en.wikipedia.org/wiki/5.1_surround_sound> "wikipedia:5.1 surround sound") 或[7.1 环绕声](<https://en.wikipedia.org/wiki/7.1_surround_sound> "wikipedia:7.1 surround sound")，可能需要解除 `Front`、 `Surround`、 `Center`、 `LFE` （低音炮）以及 `Side` 等其他声道的静音（这些声道名称是[Intel HD Audio](<https://en.wikipedia.org/wiki/Intel_High_Definition_Audio> "wikipedia:Intel High Definition Audio")声卡使用的，可能因设备不同而有所差异）。 

**注意：** 请注意这样并不会自动上混立体声源（如多数音乐）。要实现这一功能，见[#上混](<#%E4%B8%8A%E6%B7%B7>)。

###  启用麦克风

要启用麦克风，按 `F4` 切换至 Capture （捕获）选项卡，然后按 `空格` 启用一个声道即可。如果麦克风不工作，参考[Advanced Linux Sound Architecture/Troubleshooting#没有麦克风输入](<../zh-cn/Advanced_Linux_Sound_Architecture/Troubleshooting.html#%E6%B2%A1%E6%9C%89%E9%BA%A6%E5%85%8B%E9%A3%8E%E8%BE%93%E5%85%A5> "Advanced Linux Sound Architecture/Troubleshooting")。 

按下 `Esc` 键退出 alsamixer。 

###  测试你的更改

接下来，测试声卡是否工作： 
    
    $ speaker-test -c 2
    
根据扬声器的配置，调整 `-c` 。对于 7.1 声道，使用 `-c 8`： 
    
    $ speaker-test -c 8
    
如果声音输出到了错误的设备，可以试试用 `-D` 参数手动指定。 
    
    $ speaker-test -D default:PCH -c 8
    
`-D` 的值是 PCM 通道的名字，运行以下命令即可获取： 
    
    $ aplay -L | grep :CARD
    
    default:CARD=PCH  # 'default:PCH' is the PCM channel name for -D
    sysdefault:CARD=PCH
    front:CARD=PCH,DEV=0
    surround21:CARD=PCH,DEV=0
    surround40:CARD=PCH,DEV=0
    surround41:CARD=PCH,DEV=0
    surround50:CARD=PCH,DEV=0
    surround51:CARD=PCH,DEV=0
    surround71:CARD=PCH,DEV=0

###  附加注释

  * 如果你的系统有多个声卡，则可以按`F6`切换声卡。

  * 有些声卡需要静音或禁用数字输出，才能听到模拟声音。反之亦然

  * 有些机器，如Thinkpad T61，有`Speaker`声道，也需要解除静音并调整。

  * 有些机器，如Dell E6400，可能也需要解除`Front` 和 `Headphone` 通道的静音并调整它们。

  * 如果重启以后，你的声音调整似乎丢失了，尝试以root运行alsamixer。

##  驱动配置

更多信息，参考[驱动程序配置指南](<https://docs.kernel.org/sound/alsa-configuration.html>). 

要重新加载 ALSA 驱动程序配置，您必须重新加载相应的模块。在执行此作之前，使用相应 ALSA 驱动程序的所有进程（如[PipeWire](<../zh-cn/PipeWire.html> "PipeWire")）必须停止。要使用声音[设备文件](<https://en.wikipedia.org/wiki/Device_file#Character_devices> "wikipedia:Device file")识别进程，请使用[fuser(1)](<https://man.archlinux.org/man/fuser.1>)： 
    
    # fuser --all --verbose /dev/snd/*
    
参考： 

  * [ALSA SoundCard Matrix](<https://www.alsa-project.org/main/index.php/Matrix:Main>)

  * [alsactl(1)](<https://man.archlinux.org/man/alsactl.1>)

  * [Kernel modules#Manual module handling](<../zh-cn/Kernel_modules.html#Manual_module_handling> "Kernel modules")

###  卡和模块

运行 `lspci -k -nn -d ::0403`确定PCI设备的模块。 

**提示：**

  * `::0403`这里表示 _多媒体控制器_ PCI 设备类的[音频设备](<https://admin.pci-ids.ucw.cz/read/PD/04/03>) 子类。
  * _lspci_ 输出中的 _Kernel driver in use_ 是加载的模块。 _Kernel modules_ 能够处理设备，参考[lspci(8) § k](<https://man.archlinux.org/man/lspci.8#k>)。

USB设备运行`lsusb --verbose --tree | grep --after-context=1 'Class=Audio'`。 

运行`lsmod | grep '^snd'` 以获取已加载声音模块的完整列表。 

运行 `cat /proc/asound/cards` 以获取声卡列表及其相应的 _索引_ （ _卡号_ ）。 

**提示：**

  * 有关`/proc/asound/cards`的格式，请参阅 ALSA 库 API [控制接口](<https://www.alsa-project.org/alsa-doc/alsa-lib/control.html>)的 _常规概述_ 部分。
  * 有关 `/proc/asound` [procfs](</wzh/index.php?title=Procfs&action=edit&redlink=1> "Procfs（页面不存在）") 树的一般信息，请参阅[ALSA 驱动程序的 Proc 文件](<https://docs.kernel.org/sound/designs/procfile.html>).

运行`cat /proc/asound/modules`获取卡片索引及其相应的模块名称。 

###  声卡索引

如果要更改声卡顺序（或你的声卡顺序在启动时发生更改，你想要让它保持不变），使用`snd` 模块的`slots`选项为给定驱动程序[保留](<https://docs.kernel.org/sound/alsa-configuration.html#module-snd>)索引,参考[内核模块#S配置模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#S%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")。 

**提示：** _slot_ 名称源自OSS，相当于ALSA中的术语 _索引_ 。

以下示例假设你希望 USB 声卡始终是第一个（即索引为`0`），无论何时加载模块（例如，此卡可以在启动时拔出）： 

    /etc/modprobe.d/alsa-base.conf
    
    options snd slots=snd_usb_audio

当模块名称前面加上感叹号（`!`）时，将为除该名称之外的任何模块提供相应的索引。例如，将索引（`0`）留给除了`snd_usb_audio`外的任何模块，以避免 USB 声卡获取它： 
    
    options snd slots=!snd_usb_audio
    
您还可以提供`-2`的索引，以指示 ALSA 永远不要使用此卡作为主卡：负值被解释为[允许索引的位掩码](<https://docs.kernel.org/sound/alsa-configuration.html#common-parameters-for-top-sound-card-modules>)。使用特定模块的`index`选项，和上面例子作用相同： 
    
    options snd_usb_audio index=-2
    
如果多张声卡使用相同的模块，并且它们的顺序始终相同，则只需使用`index`选项即可更改顺序。以下示例假设有两个使用 HD 音频模块的音频卡（例如，集成音频卡和非集成视频卡的 HDMI 输出），并且你想交换它们的索引： 
    
    options snd_hda_intel index=1,0
    
**提示：**

  * 上面的示例解读为“使用`snd_hda_intel`的第一张声卡给出索引 `1`，第二个给出索引`0`”。哪张卡是第一张，哪张卡是第二张由[udev](<../zh-cn/Udev.html> "Udev")决定的。

  * ALSA 模块选项通常不会采用单个值，而是采用一个值数组，选项设置的每个值，仅适用于给定模块正在处理的声卡之一。在以下输出中查找概念数组的存在：

    $ modinfo --field=parm _module_name_ | column --separator=':' --table --table-columns-limit=2

`slots`选项可以与 `index` 选项组合，[只要它们不冲突](<https://docs.kernel.org/sound/alsa-configuration.html#module-autoloading-support>): 

    options snd slots=,snd_hda_intel,snd_hda_intel,snd_usb_audio,snd_usb_audio,snd_usb_audio
    
    options snd_hda_intel index=2,1
    
    options snd_usb_audio index=3,4,5 vid=0x _VID_3_ ,0x _VID_4_ ,0x _VID_5_ pid=0x _PID_3_ ,0x _PID_4_ ,0x _PID_5_
    
**提示：**

  * `slots=,`意思是“不保留索引零”，因此例如，一些 USB 卡（在`snd-usb-audio`选项中未提及）在启动后插入，可能是第一个。

  * `snd_usb_audio`模块允许使用`vid`和`pid`选项来指定卡，因此您不依赖于 _udev_ 的顺序。

参考： 

  * [MultipleCards](<https://alsa.opensrc.org/MultipleCards>)

  * [MultipleUSBAudioDevices](<https://alsa.opensrc.org/MultipleUSBAudioDevices>)

###  禁用卡

要禁用由给定内核模块控制的所有卡，使用[安装](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E5%AE%89%E8%A3%85> "内核模块")或[模块黑名单](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E4%BD%BF%E7%94%A8%E5%86%85%E6%A0%B8%E5%91%BD%E4%BB%A4%E8%A1%8C> "内核模块")方法[阻止模块加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "内核模块")。 

**注意：** 在 _modprobe.d_ 配置文件中使用[blacklist](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "内核模块")关键字将不起作用。 

要选择应禁用的卡，请使用内核模块的`enable`[选项](<https://docs.kernel.org/sound/alsa-configuration.html#common-parameters-for-top-sound-card-modules>)。例如，禁用一个模块所操作的第二张卡： 
    
    /etc/modprobe.d/alsa-base.conf
    
    options _module_name_ enable=1,0

另请参阅[/疑难解答#编解码器探测](<../zh-cn/ALSA/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#%E7%BC%96%E8%A7%A3%E7%A0%81%E5%99%A8%E6%8E%A2%E6%B5%8B> "ALSA/疑难解答")以禁用 HD Audio 卡编解码器。 

##  库配置

系统配置文件是`/etc/asound.conf`，每个用户配置文件是 `~/.asoundrc`。 

[配置文件](<https://www.alsa-project.org/alsa-doc/alsa-lib/conf.html>)中解释了库配置的语法，例如空格、行延续、注释，包括配置文件、标点符号（分隔符）、赋值、复合赋值、操作模式等。 

ALSA 库配置是为库的每个实例加载的，因此要重新加载它，您所要做的就是重新启动正在使用它的程序。 

更多信息，参考: 

  * [Configuring ALSA](<https://www.volkerschatz.com/noise/alsa.html#config>)

  * ALSA非官方wiki上的[.asoundrc 文章](<https://alsa.opensrc.org/Asoundrc>)。

  * ALSA项目wiki上的[.asoundrc文章](<https://www.alsa-project.org/main/index.php/Asoundrc>)。

###  基本语法

####  操作模式

解析节点有不同的操作模式，默认模式为“合并/创建”（merge/create）。如果操作模式为“合并/创建”或“合并”（merge），会进行类型检查。只有同样类型的赋值能够被合并，因此字符串不能与整形数合并。在默认操作模式中尝试对复合键值定义一个简单赋值是没有作用的，反之亦然。 

操作模式前缀符号： 

  * "+" -- 合并/创建
  * "-" -- 合并
  * "?" -- 不覆盖（do not override）
  * "!" -- 覆盖（override）

    # 合并/创建 - 如果不存在节点则创建之。
    # 如果其存在且类型匹配，则合并subkeyN到键值中。
    key.subkeyN valueN;
    
    # 合并/创建 - 与上面等同
    key.+subkeyN valueN;
    
    # 合并 - 节点 key.subkeyN 必须已经存在且拥有相同类型
    key.-subkeyN valueN;
    
    # 不覆盖 - 如果 key.subkeyN 节点已经存在，则忽略新的赋值
    key.?subkeyN valueN;
    
    # 覆盖 - 移除 subkeyN 及其下所有键值, 然后创建节点 key.subkeyN
    key.!subkeyN valueN;
    
在操作正确的情况下，使用覆盖操作模式通常来说是安全的。但是切记，在一个节点中可能会有其他对于正确动作来说必要的键值。 

**警告：** 覆盖 pcm 节点大致必然会使 alsa 无法使用，因为所有插件定义都会被删除。 因此除非要从头开始创建配置，否则 **不要使用 !pcm.key** 。

####  嵌套

有时，在配置中使用嵌套可能很有用，甚至更容易阅读。 
    
    Nesting PCM plugins
    
    pcm.azalia {	type hw; card 0	}
    pcm.!default {	type plug; slave.pcm "azalia"	}
    
    # 相当于
    
    pcm.!default {	type plug; slave.pcm {	type hw; card 0;	}	}
    
    # 也相当于
    
    pcm.!default.type plug;
    pcm.default.slave.pcm.type hw;
    pcm.default.slave.pcm.card 0;

###  设置默认声卡

####  使用“defaults”节点设置默认设备的示例

假设“默认”（default）节点在 `/usr/share/alsa/alsa.conf` 设定，其中“defaults.pcm.card”及其对应的“ctl”（控制）项都赋值为整型数“0”， 而用户想要将默认PCM与控制设备设定为声卡“2”（第三个声卡），或对于Azalia声卡设定为“SB”。 
    
    defaults.ctl.card 2; # 将默认设备与控制设定为第三个声卡（计数从0开始）。
    defaults.pcm.card 2; # 寻址类型不会更改。
    
    defaults.ctl.+card 2; # 与上面相同。
    defaults.pcm.+card 2;
    
    defaults.ctl.-card 2; # 对于默认设置来说效果相同，但如果默认节点被去除
    defaults.pcm.-card 2; # 或类型被更改，则合并操作不会带来更改。
    
    defaults.pcm.?card 2; # 没有效果，因为该赋值已经存在。
    defaults.ctl.?card 2;
    
    defaults.pcm.!card "SB"; # 此处有必要使用覆盖操作模式，
    defaults.ctl.!card "SB"; # 因为数值类型有所不同。
    
这里使用双引号会自动将值的数据类型设为字符串，因此在上例中设置 `defaults.pcm.!card "2"` 的结果就是保持之前的默认设备不变，此例中为声卡0。只要不使用特殊字符（理想状态下也不应该会使用），双引号就不是强制性的。这可能与其他作业无关。 

**注意：** 从配置的角度来看，这些并不等同于设置复合的“default”PCM 设备，因为大多数用户也在其中指定寻址类型，这实际上可能是相同的，但分配本身仍然不同。 此外，`defaults.pcm.card`在 ALSA 配置文件中被多次引用，通常作为回退分配，其中不同的环境变量优先。

####  通过默认节点设置默认声卡

关于 `defaults.pcm.card` 和 `defaults.pcm.device`，要实际运用[上面的例子](<#%E4%BD%BF%E7%94%A8%E2%80%9C%E9%BB%98%E8%AE%A4%E2%80%9D%E8%8A%82%E7%82%B9%E7%9A%84%E9%BB%98%E8%AE%A4%E8%AE%BE%E5%A4%87%E8%AE%BE%E5%AE%9A%E7%A4%BA%E4%BE%8B>)，假定有2块声卡分别编号为0和1，想要默认使用编号1的声卡，在 `/etc/asound.conf` 或用户对应的 `~/.asoundrc` 使用以下配置即可更改回放与混音控制声卡。 
    
    defaults.pcm.card 1
    defaults.ctl.card 1

####  使用环境变量选择默认PCM设备

把ALSA_CARD设为设备的名字也许就可以了。首先用 `aplay -l` 获取名称，然后将ALSA_CARD设为冒号之后、方括号之前的名称：例如，如果有 

`card 1: HDMI [HDA ATI HDMI], device 3: HDMI 0 [HDMI 0]`

那就设置`ALSA_CARD=HDMI`。 

其他变量也在默认全局配置 `/usr/share/alsa/alsa.conf `中检查。通过在那里查找形式为 `vars [ ... ]` 的构造，出现了下表： 

| Variable name | Used by   
---|---|---  
1 | ALSA_CARD | pcm.default , pcm.hw , pcm.plughw , ctl.sysdefault , ctl.hw , rawmidi.default , rawmidi.hw , hwdep.hw   
2 | ALSA_CTL_CARD | ctl.sysdefault , ctl.hw   
3 | ALSA_HWDEP_CARD | hwdep.default , hwdep.hw   
4 | ALSA_HWDEP_DEVICE | hwdep.default , hwdep.hw   
5 | ALSA_PCM_CARD | pcm.default , pcm.hw , pcm.plughw   
6 | ALSA_PCM_DEVICE | pcm.hw , pcm.plughw   
7 | ALSA_RAWMIDI_CARD | rawmidi.default , rawmidi.hw   
8 | ALSA_RAWMIDI_DEVICE | rawmidi.default , rawmidi.hw   
  
或者也可以在你自己的配置文件（最好是全局的`/etc/asound.conf`）中对行为进行覆盖。添加： 
    
    pcm.!default {
      type plug
      slave.pcm {
        @func getenv
        vars [ ALSAPCM ]
        default "hw:Audigy2"
      }
    }

同样把本例中的 `Audigy2` 替换成你的设备名字。你可以使用`aplay -l`获取名字，或者也可以使用**surround51** 等PCM。不过，如果你需要使用麦克风的话，选择全双工PCM声卡为默认设备是个不错的选择。 

现在只需改变环境变量 `ALSAPCM`，就可以在启动程序时选择声卡。对于所有不允许选择声卡的程序此法效果良好，而对于其他的程序请确保保持默认声卡选择。 

举例来说，假设你写了一个缩混PCM命名为 `mix51to20` ，用以下命令即可将之用于[mplayer](<https://archlinux.org/packages/?name=mplayer>)包： `ALSAPCM=mix51to20 mplayer example_6_channel.wav`

**注意：** 请注意默认寻址类型。

####  直接寻址硬件

**警告：** 此设置使设备无法对其他应用程序使用。仅当它是更复杂的设置 `~/.asoundrc` 的一部分或用户有意的想要直接寻址声卡（例如通过`IEC958` 或专用音乐服务器进行数字输出）时，才建议使用此方法。某些应用程序（例如[Chromium](<../zh-cn/Chromium.html> "Chromium")）不支持此没有声音服务器或[#软件混音](<#%E8%BD%AF%E4%BB%B6%E6%B7%B7%E9%9F%B3>)的设置。

首先确认你想设为默认的声卡和设备ID： 
    
    $ aplay -l
    
    **** List of PLAYBACK Hardware Devices ****
    card 0: Intel [HDA Intel], device 0: CONEXANT Analog [CONEXANT Analog]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 0: Intel [HDA Intel], device 1: Conexant Digital [Conexant Digital]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 1: JamLab [JamLab], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 2: Audio [Altec Lansing XT1 - USB Audio], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    
例如，此列表中的最后一个条目具有卡索引（卡号）`2`、卡 ID 字符串 `Audio` 和设备 ID `0`。要把这块声卡设为默认，可以使用系统级的 `/etc/asound.conf` 或用户级的 `~/.asoundrc` 文件。如果文件不存在，需要手动创建。然后针对相应的声卡加入以下内容： 
    
    pcm.!default {
       type hw
       card Audio #or card 2
       hint {
        show on # for some applications
       }
    }
    
    ctl.!default {
       type hw
       card Audio
    }
    
    pcm.dmixer {
    	type dmix
    	ipc_key 2048
    	slave {
    		pcm "hw:Audio" #or "hw:2"
    	}
    }
    
    pcm.dsnooper {
    	type dsnoop
    	ipc_key 2048
    	slave {
    		pcm "hw:Audio"
    	}
    }
    
建议使用声卡 ID 字符串而代替数字引用来克服启动顺序问题。 

**注意：** T这种方法可能会有问题 ，如果您的系统有多个相同 ID 字符串的卡(追加 `_1`, `_2`, … 后缀).有关详细信息，请参阅 [识别两个相同的音频设备](<https://alsa.opensrc.org/Udev#Identify_two_identical_audio_devices>)。

`pcm.dmixer`和`pcm.dsnooper` 是不支持不[混音](<#%E8%BD%AF%E4%BB%B6%E6%B7%B7%E9%9F%B3>)的应用程序的备用。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 应引入选择ALSA设备的一般方法，例如环境值。（在 [Talk:ALSA](<../zh-cn/Talk:ALSA.html>) 中讨论）

例如，`chromium -alsa-output-device=pcm.dmixer -alsa-input-device=pcm.dsnooper` 使得Chromium临时混音。 

`pcm`选项会影响将用于音频播放的卡和设备，而 `ctl`选项会影响 _alsamixer_ 等控制实用程序使用哪张卡。 

更改应在您（重新）启动应用程序后立即生效(例如，Player)。您还可以使用类似 _aplay_ 的命令进行测试： 
    
    $ aplay -D default:PCH _your_favourite_sound.wav_
    
如果您收到有关 asound 配置的错误，请检查[上游文档](<https://www.alsa-project.org/main/index.php/Asoundrc#The_default_plugin>)，了解配置文件格式可能发生的更改。 

##  插件

如果需要启用[#上混](<#%E4%B8%8A%E6%B7%B7>)，[#缩混](<#%E7%BC%A9%E6%B7%B7>)，[#高质量重采样](<#%E9%AB%98%E8%B4%A8%E9%87%8F%E9%87%8D%E9%87%87%E6%A0%B7>)和其他高级功能，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")插件[alsa-plugins](<https://archlinux.org/packages/?name=alsa-plugins>)包， 

有关更多信息，请参阅[PCM（数字音频）插件](<https://www.alsa-project.org/alsa-doc/alsa-lib/pcm_plugins.html>)。 

###  软件混音

混音使多个应用程序能够同时输出声音。大多数独立声卡都支持硬件混合，如果可用，默认情况下会启用。集成主板声卡（如英特尔高清音频），通常不支持硬件混音。在此类卡上，软件混音由名为`dmix`的 ALSA 插件完成。如果硬件混音不可用，则会自动启用此功能。 

**注意：** 默认情况下，对于不支持硬件混音的声卡，软件混音是启用。默认情况下，`dmix`未为数字输出 （S/PDIF） 启用，需要以下配置片段启用。

要手动启用`dmix`，请将以下内容添加到 ALSA 配置文件中： 

    /etc/asound.conf
    
    pcm.dsp {
    	
        type plug
    	
        slave.pcm "dmix"
    	
    }

###  上混

播放双声道立体声音源（如音乐）时，需要利用上混才能充分利用 5.1 或 7.1 环绕立体声系统。以前，上混很麻烦，还经常出错；但如今有了插件可以轻松地打理好这一任务。我们使用由 [alsa-plugins](<https://archlinux.org/packages/?name=alsa-plugins>)包 软件包提供的 `upmix` 插件。 

然后在ALSA配置文件（`/etc/asound.conf` 或 `~/.asoundrc`）中添加如下内容： 
    
    pcm.upmix71 {
        type upmix
        slave.pcm "surround71"
        delay 15
        channels 8
    }
    
该范例适用于7.1声道上混。类比该范例，同样能设置5.1或4.0声道上混。 

该设置添加了一个新的用于上混的pcm通道。如果希望所有音频源都通过该 pcm 输出，在上述设置后添加如下配置即可： 
    
    pcm.!default "plug:upmix71"
    
插件自动允许多个音频源同时通过它输出，所以将其设为默认实际上是个安全的选择。如果不行，就得像下面这样为上混配置 dmixer： 
    
    pcm.dmix6 {
        type asym
        playback.pcm {
            type dmix
            ipc_key 567829
            slave {
                pcm "hw:0,0"
                channels 6
            }
        }
    }
    
并使用 dmix6 而非 surround71。如果遇到声音卡顿或混乱，考虑增加 buffer_size（比如增加到 32768），或使用[高质量重采样](<#%E9%AB%98%E8%B4%A8%E9%87%8F%E9%87%8D%E9%87%87%E6%A0%B7>)。 

###  缩混

如果您想将源缩混为立体声，比如您想在立体声系统上观看具有 5.1 声音的电影，请使用 [alsa-plugins](<https://archlinux.org/packages/?name=alsa-plugins>)包中包含的 vdownmix 插件。 

在配置文件中添加如下内容： 
    
    pcm.!surround51 {
        type vdownmix
        slave.pcm "default"
    }
    pcm.!surround40 {
        type vdownmix
        slave.pcm "default"
    }
    
**注意：** 这可能还不足以让缩混工作，见 [[1]](<https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=541786>) 。因此可能需要添加 `pcm.!default "plug:surround51"` 或 `pcm.!default "plug:surround40"`。只能使用一个 `vdownmix` 插件；如果你有7.1声道音响，需要使用 `surround71` 来代替上面所述的配置文件。一个让 `vdownmix` 和 `dmix` 同时工作的配置文件的示例见 [[2]](<https://bbs.archlinux.org/viewtopic.php?id=167275>) 。

###  多频段均衡器

[多频段均衡器](<https://web.archive.org/web/20191211120217/http://plugin.org.uk/ladspa-swh/docs/ladspa-swh.html#id1197>) **(mbeq)** 是一个相当典型的多频段图形均衡器。它是使用[快速傅里叶变换](<https://en.wikipedia.org/wiki/Fast_Fourier_transform> "wikipedia:Fast Fourier transform")（FFT）实现的，因此它需要相当多的 CPU 功率，但相位效应应该比等效滤波器实现更少。如果输入信号的采样率太低，则顶部频段将被忽略 - 最高有用频段将始终是高架。 

_mbeq_ 是 Steve Harris 的[LADSPA](<https://en.wikipedia.org/wiki/LADSPA> "wikipedia:LADSPA") [插件套件](<https://github.com/swh/ladspa>)的一部分。 

如果还没有的话，安装 [alsa-plugins](<https://archlinux.org/packages/?name=alsa-plugins>)包、[ladspa](<https://archlinux.org/packages/?name=ladspa>)包 和 [swh-plugins](<https://archlinux.org/packages/?name=swh-plugins>)包 软件包。 

  * 在 `~/.asoundrc` 或 `/etc/asound.conf` 中添加如下内容：

    /etc/asound.conf
    
    pcm.eq {
      type ladspa
    
      # The output from the EQ can either go direct to a hardware device
      # (if you have a hardware mixer, e.g. SBLive/Audigy) or it can go
      # to the software mixer shown here.
      #slave.pcm "plughw:0,0"
      slave.pcm "plug:dmix"
    
      # Sometimes you may need to specify the path to the plugins,
      # especially if you have just installed them.  Once you have logged
      # out/restarted this should not be necessary, but if you get errors
      # about being unable to find plugins, try uncommenting this.
      #path "/usr/lib/ladspa"
    
      plugins [
        {
          label mbeq
          id 1197
          input {
            #this setting is here by example, edit to your own taste
            #bands: 
            50hz, 100hz, 156hz, 220hz, 311hz, 440hz, 622hz, 880hz, 1250hz, 1750hz, 25000hz, #50000hz, 10000hz, 20000hz
            controls [ -5 -5 -5 -5 -5 -10 -20 -15 -10 -10 -10 -10 -10 -3 -2 ]
          }
        }
      ]
     }
    
     # Redirect the default device to go via the EQ - you may want to do
     # this last, once you are sure everything is working.  Otherwise all
     # your audio programs will break/crash if something has gone wrong.
    
     pcm.!default {
      type plug
      slave.pcm "eq"
     }
    
     # Redirect the OSS emulation through the EQ too (when programs are running through "aoss")
    
     pcm.dsp0 {
      type plug
      slave.pcm "eq"
     }
    
### AlsaEqual

#### System-wide

安装 [alsaequal](<https://aur.archlinux.org/packages/alsaequal/>)AUR包。 

安装包后，将以下内容添加到 ALSA 配置文件中： 

    /etc/asound.conf
    
    ctl.equal {
    	
        type equal;
    	
    }
    	
    pcm.plugequal {
    	
        type equal;
    	
        # Normally, the equalizer feeds into dmix so that audio
    	
        # from multiple applications can be played simultaneously:
    	
        slave.pcm "plug:dmix";
    	
        # If you want to feed directly into a device, specify it instead of dmix:
    	
        #slave.pcm "plughw:0,0";
    	
    }
    	
    # Configuring pcm.!default will make the equalizer your default sink
    	
    pcm.!default {
    	
    # If you do not want the equalizer to be your default,
    	
    # give it a different name, like pcm.equal commented below
    	
    # Then you can choose it as the output device by addressing
    	
    # it in individual apps, for example mpg123 -a equal 06.Back_In_Black.mp3
    	
    # pcm.equal {
    	
        type plug;
    	
        slave.pcm plugequal;
    	
    }

要更改均衡器设置，请运行 
    
    $ alsamixer -D equal
    
请注意，每个用户的均衡器配置都不同（除非未指定其他内容）。 保存在 `~/.alsaequal.bin`中。 

因此，如果您想将ALSAEqual与[mpd](<../zh-cn/MPD.html> "Mpd") 或在不同用户下运行的其他软件一起使用，您可以使用以下命令进行配置。 
    
    $ su mpd -c 'alsamixer -D equal'
    
或者，例如，您可以在他们的主目录中创建指向您的`.alsaequal.bin`的符号链接。 

####  仅特定输出

如果您只想将均衡器应用于特定的输出设备（例如，您的扬声器连接到 S/PDIF 输出，而不是耳机连接到耳机插孔），但又希望能够从多个应用程序和同时输出到两个输出设备，您需要创建两个直接馈送到各自设备（`slave.pcm`）的 {ic|dmix}} 设备。以下内容适用于立体声输出，并保持常规立体声输入，仅将均衡器应用于 S/PDIF 输出。 
    
    /etc/asound.conf
    
    #
    	
    #  (capture.pcm)  <-- dnsoop
    	
    #        |
    	
    # !default                               --> dmixa
    	
    #        |                               |
    	
    #  (playback.pcm) --> stereo2quad ==> quad
    	
    #                                        |
    	
    #                                        --> softvol --> plugequal --> dmixd
    	
    #
    	
    # dmix for analog output
    	
    pcm.dmixa {
    	
      type dmix
    	
      ipc_key 1024
    	
      ipc_perm 0666
    	
      slave.pcm "hw:PCH,0"
    	
      slave {
    	
         period_time 0
    	
        period_size 1024
    	
        buffer_size 4096
    	
         channels 2
    	
      }
    	
      bindings {
    	
        0 0
    	
        1 1
    	
      }
    	
    }
    	
    # dmix for digital output
    	
    pcm.dmixd {
    	
      type dmix
    	
      ipc_key 2048
    	
      ipc_perm 0666
    	
      slave.pcm "hw:PCH,1"
    	
      slave {
    	
        period_time 0
    	
        period_size 1024
    	
        buffer_size 4096
    	
        channels 2
    	
      }
    	
      bindings {
    	
        0 0
    	
        1 1
    	
      }
    	
    }
    	
    # equalizer with controls
    	
    pcm.plugequal {
    	
      type equal
    	
      slave {
    	
        pcm "plug:dmixd"
    	
      }
    	
    }
    	
    ctl.equal {
    	
     type equal
    	
    }
    	
    # Volume control for S/PDIF
    	
    pcm.softvol {
    	
        type softvol
    	
        slave.pcm "plug:plugequal"
    	
        control {
    	
            name "S/PDIF"
    	
        }
    	
    }
    	
    # multi:
    	
    # "a" (analog)  -> dmix,
    	
    # "d" (digital) -> softvol -> plugequal -> dmix
    	
    pcm.quad {
    	
         type multi
    	
         slaves {
    	
          a.pcm "dmixa"
    	
          a.channels 2
    	
          d.pcm "plug:softvol" # detour via softvol and equalizer
    	
          d.channels 2
    	
        }
    	
        bindings {
    	
          0 { slave a; channel 0; }
    	
          1 { slave a; channel 1; }
    	
          2 { slave d; channel 0; }
    	
          3 { slave d; channel 1; }
    	
         }
    	
    }
    	
    # stereo to quad
    	
    pcm.stereo2quad {
    	
      type route
    	
      slave.pcm "quad"
    	
      ttable [
    	
        [ 1 0 1 0 ]
    	
        [ 0 1 0 1 ]
    	
      ]
    	
    }
    	
    # playback to stereo to quad, capture as usual
    	
    pcm.!default {
    	
      type asym
    	
      playback.pcm "plug:stereo2quad"
    	
      capture.pcm "plug:dnsoop"
    	
    }

####  管理状态

安装[alsaequal-mgr](<https://aur.archlinux.org/packages/alsaequal-mgr/>)AUR 包。 

像往常一样配置均衡器 
    
    $ alsamixer -D equal
    
当您对状态感到满意时，您可以给它起一个名字（在本例中为 _foo_ ）并保存它： 
    
    $ alsaequal-mgr save _foo_
    
状态 "foo"可以在以后用一下方式恢复 
    
    $ alsaequal-mgr load _foo_
    
但是，这只能恢复`~/.alsaequal.bin`然后，您必须通过 `alsamixer -D equal`更新均衡器。 

因此，您可以为游戏、电影、音乐流派、VoIP 应用程序等创建不同的均衡器状态，并根据需要重新加载它们。 

有关更多选项，请参阅[项目页面](<https://xyne.dev/projects/alsaequal-mgr/>)和帮助消息。 

##  提示和技巧

###  高质量重采样

启用[#软件混音](<#%E8%BD%AF%E4%BB%B6%E6%B7%B7%E9%9F%B3>)混音后，ALSA 会强制将所有内容重新采样到相同的频率（支持时默认为 48 kHz）。默认情况下，它将[尝试使用](<https://git.alsa-project.org/?p=alsa-lib.git;a=blob;f=src/pcm/pcm_rate.c;h=2eb4b1b33933dec878d0f25ad118869adac95767;hb=HEAD#l1278>) _speexrate_ 转换器来执行此作，如果不可用，则回退到低质量的线性插值。因此，如果您由于重采样不良而获得较差的音质，只需安装[alsa-plugins](<https://archlinux.org/packages/?name=alsa-plugins>)包包即可解决问题。 

要获得更高质量的重采样，您可以将默认速率转换器更改为 `speexrate_medium`或`speexrate_best`。两者都表现得足够好，在实践中您选择哪一个并不重要，因此使用最好的转换器通常不值得它所需的额外 CPU 周期。 

要更改默认转换器，请将以下内容放在 `~/.asoundrc`或 `/etc/asound.conf`中： 
    
    defaults.pcm.rate_converter "speexrate_medium"
    
**注意：**

  * 也可以使用 [libsamplerate](<https://archlinux.org/packages/?name=libsamplerate>)包包转换器，其速度仅为 _speexrate_ 转换器的一半左右，但质量不会提高多少。

  * 也可以使用 [Rate 使用 libavresample 的转换器插件](<https://github.com/alsa-project/alsa-plugins/blob/master/doc/lavrate.txt>) ，此插件使用[FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg")。`lavcrate_high`和`lavcrate_higher`分别等于 [Kodi](<../zh-cn/Kodi.html> "Kodi")低质量和中质量重采样器。

  * 某些应用程序（如 MPlayer 及其分支）默认执行自己的重采样，因为某些 ALSA 驱动程序在启用重采样时具有不正确的延迟报告（因此导致 AV 不同步），因此更改此设置不会产生任何影响，除非您将它们配置为使用 ALSA 重采样。

###  在启动时禁用自动静音

_自动静音模式_ 可以在使用 _amixer_ 启动时配置。例如，要禁用它： 
    
     # amixer -c 0 sset "Auto-Mute Mode" Disabled
    
或者，可以通过 _alsamixer_ 使用基于 ncurses 的接口。为了保存任何修改，请使用： 

     # alsactl store
    
或 

     # alsactl daemon
    
参考 [#ALSA和systemd](<#ALSA%E5%92%8Csystemd>). 

###  热插拔 USB 声卡

请看[为 ALSA 编写 Udev 规则](<https://alsa.opensrc.org/Udev>). 

###  同时输出

您可能希望通过通过迷你插孔连接的外部扬声器和内部扬声器同时播放音乐。这可以通过使用`alsamixer`或{ic|amixer}}取消静音**自动静音** 项目来完成： 
    
    $ amixer sset "Auto-Mute" unmute
    
然后取消静音其他必需项目，例如**耳机** 、**扬声器** 、**低音扬声器**...... 

**注意：** 如果耳机连接器（迷你插孔）发出噼啪声，参考 [/疑难解答#通过耳机插孔有爆裂声](<../zh-cn/ALSA/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#%E9%80%9A%E8%BF%87%E8%80%B3%E6%9C%BA%E6%8F%92%E5%AD%94%E6%9C%89%E7%88%86%E8%A3%82%E5%A3%B0> "ALSA/疑难解答")。

###  键盘控制音量

将以下命令[映射](<../zh-cn/%E9%94%AE%E7%9B%98%E8%BE%93%E5%85%A5.html> "键盘输入")到音量键： `XF86AudioRaiseVolume`, `XF86AudioLowerVolume`, `XF86AudioMute`. 

提高音量： 
    
    amixer set Master 5%+
    
降低音量： 
    
    amixer set Master 5%-
    
切换音量的静音/取消静音： 
    
    amixer set Master toggle
    
###  使用snd_aloop的虚拟声音设备

您可能需要一个插孔替代方案来创建虚拟录音或播放设备，以便使用{{ic|snd_aloop}模块混合不同的源： 
    
    modprobe snd_aloop
    
使用以下方法列出您的新虚拟设备 
    
    aplay -l
    
现在你可以使用 ffmpeg： 
    
    ffmpeg -f alsa -i hw:1,1,0 -f alsa -i hw:1,1,1 -filter_complex amerge output.mp3
    
在 hw：R，W，N 短语中，R 是您的虚拟卡设备号。录制设备应将 W 设置为 1，播放设备应设置为 0。N 是您的子设备。您可以使用所有可用的虚拟设备并使用 mplayer 等应用程序播放/停止： 
    
    mplayer -ao alsa:device=hw=1,0,0 fileA
    mplayer -ao alsa:device=hw=1,0,1 fileB
    
您还可以用这种方法，就是使用下面的脚本来使用[festival](</wzh/index.php?title=Festival&action=edit&redlink=1> "Festival（页面不存在）")将语音生成到录音流中。 
    
    #!/bin/sh
    echo "$1" | iconv -f utf-8 -t iso-8859-1 | text2wave  > "_tmp_.wav"
    mplayer -ao alsa:device=hw=2,0,0 "_tmp.wav"
    rm "_tmp.wav"
    
###  重新配置输入/输出端口

[alsa-tools](<https://archlinux.org/packages/?name=alsa-tools>)包包含 _hdajackretask_ 工具，该工具可用于（在Intel HDA卡上）重新配置声卡输入/输出端口；例如，将麦克风插孔变成耳机插孔。 

### apulse

[apulse](<https://aur.archlinux.org/packages/apulse/>)AUR 提供了[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") API 的[替代部分实现](<https://github.com/i-rinat/apulse?tab=readme-ov-file#about>)。它允许您将 ALSA 用于仅支持 PulseAudio 声音的应用程序。用法很简单： 
    
    $ apulse _application_
    
##  相关阅读

  * [ALSA 项目维基](<https://www.alsa-project.org/>)

  * [ALSA 非官方 wiki](<https://alsa.opensrc.org/>)

  * [ALSA 的近距离观察](<https://www.volkerschatz.com/noise/alsa.html>)

  * [Linux ALSA声音笔记](<http://www.sabi.co.uk/Notes/linuxSoundALSA.html>)

  * [Pulse-code 调制(PCM)](<https://en.wikipedia.org/wiki/Pulse-code_modulation> "wikipedia:Pulse-code modulation")
