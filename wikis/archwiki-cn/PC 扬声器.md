**翻译状态：**

  * 本文（或部分内容）译自 [PC speaker](<https://wiki.archlinux.org/title/PC_speaker> "arch:PC speaker")，最近一次同步于 2024-09-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/PC_speaker?diff=0&oldid=814184>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PC_speaker_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")
  * [ALSA](<../zh-cn/ALSA.html> "ALSA")

从第一台 IBM PC 开始，大多数电脑都配备了内置**扬声器** （或是 _蜂鸣器_ ），其可以发出蜂鸣声。该扬声器并不具备高保真回放功能，仅能以蜂鸣形式发出音频反馈信息。某些软件（如浏览器，编辑器或终端）也可能会产生蜂鸣声，该特征不一定符合用户需要。本文提供了配置或完全禁用蜂鸣器的一系列指南。 

对于没有声卡或扬声器，但需要简单音频提示的情况，请参考 [#Beep](<#Beep>)。 

##  机制

电脑扬声器通常是连接在主板前面板接头上的一个物理装置。有些厂商的主板根本不带扬声器，而有些主板可能会直接将扬声器焊在主板上。笔记本电脑通常没有物理 PC 扬声器，但会将蜂鸣器连接到笔记本电脑的内部扬声器。在某些情况下，蜂鸣器会通过声卡的常规输出（如扬声器、耳机）发出声音，其音量往往会出乎意料地大。 

传统上，开机时 BIOS 会在[加电自检](<https://zh.wikipedia.org/wiki/%E5%8A%A0%E7%94%B5%E8%87%AA%E6%A3%80> "zhwp:加电自检")过程中发出蜂鸣声。较新的主板型号省略了开机自检蜂鸣，转而立即启动到操作系统。通常 BIOS 允许切换开机自检蜂鸣，但无法配置完全关闭电脑扬声器。 

一旦系统启动进入 Linux 并加载了 `pcspkr` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")后，就可以在环境中使用电脑扬声器，由用户手动调用并在一定程度上进行配置。由于 PC 扬声器由 CPU 直接控制，而且只能发出嘟嘟声，因此 PC 扬声器不能被用于播放音频文件。如果确实需要，卸载 `pcspkr` 并[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [snd-pcsp-dkms](<https://aur.archlinux.org/packages/snd-pcsp-dkms/>)AUR 可提供基本的音频输出。 

##  禁用 PC 喇叭

当且仅当你能够识别出某个声音是由环境的哪一部分生成的，就有可能关掉特定的一类声音，而让其他声音继续动作。这样就可以自定义对声音的选择。欢迎将可能对其他用户有用的配置与设置加入此wiki页面。 

###  物理禁用

将 PC 扬声器移除后，系统就无法发出蜂鸣声了。可能的话，将蜂鸣器物理上从主板移除可以达成该目的。有些厂商会提供跳线来禁用蜂鸣器。 

**警告：** 不建议移除 PC 扬声器，它在系统启动异常时会发出特定规律的声音，在主板说明书上可查到相应故障并解决。建议方式为在 BIOS 中禁用上电蜂鸣，并按照下文操作将蜂鸣器加入黑名单。如果你确定要物理移除扬声器，强烈建议将其保留以防万一。

###  全局设置

可以通过[移除](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%97%B6%E8%AE%BE%E7%BD%AE> "内核模块") `pcspkr` 和 `snd_pcsp` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")来完全禁用 PC 喇叭： 

**注意：** 该操作不会禁用整个音频系统，只会禁用 [PC 扬声器](<https://en.wikipedia.org/wiki/PC_speaker> "wikipedia:PC speaker")。
    
    # rmmod pcspkr
    # rmmod snd_pcsp
    
将 `pcspkr` 和 `snd_pcsp` 模块加入[黑名单](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "黑名单")的方法可以阻止 [udev](<../zh-cn/Udev.html> "Udev") 在启动时加载它。[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")文件： 
    
    /etc/modprobe.d/nobeep.conf
    
    blacklist pcspkr
    blacklist snd_pcsp
    
还有一种方法是[将其加入内核命令行黑名单](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E4%BD%BF%E7%94%A8%E5%86%85%E6%A0%B8%E5%91%BD%E4%BB%A4%E8%A1%8C_2> "内核模块")。只需把 `module_blacklist=pcspkr,snd_pcsp` 加入引导加载器的内核行即可。 

###  控制台

可将以下命令添加到 `/etc/profile` 或 `/etc/profile.d/disable-beep.sh` 之类的单独文件： 
    
    setterm -blength 0
    
另一种方法是在 `~/.inputrc` 或 `/etc/inputrc` 中添加或取消注释以下命令： 
    
    set bell-style none
    
####  Less 分页器

要想在 [less](<https://archlinux.org/packages/?name=less>)包 分页器中禁用 PC 喇叭，可以通过 `less -q`（在到达行尾时静音 PC 喇叭）或 `less -Q`（全部静音）启动它。对于[手册页](<../zh-cn/Man_page.html> "Man page")，运行 `man -P "less -Q"` 或设置 `$MANPAGER` 或 `$PAGER` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。 

或者也可以将以下行加入你的 `~/[.bashrc](<../zh-cn/Bash.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Bash")`: 
    
    alias less='less -Q'
    alias man='man -P "less -Q"'
    
### Xorg
    
    $ xset -b
    
将这条命令加入 `/etc/xprofile` 等启动文件即可固化设置。更多信息参见 [xprofile](<../zh-cn/Xprofile.html> "Xprofile")。 

### ALSA

大部分声卡中 PC 喇叭都被列为一个 [ALSA](<../zh-cn/ALSA.html> "ALSA") 通道，名称为 _PC Speaker_ 、 _PC Beep_ 或 _Beep_ 。使用 `alsamixer` 或 `amixer` 即可将喇叭静音，例如： 
    
    $ amixer set 'PC Speaker' 0% mute
    
要想取消静音，参见 [ALSA#解除各声道的静音](<../zh-cn/ALSA.html#%E8%A7%A3%E9%99%A4%E5%90%84%E5%A3%B0%E9%81%93%E7%9A%84%E9%9D%99%E9%9F%B3> "ALSA")。 

**提示：** 如果你在使用 PulseAudio，而默认 ALSA 设备没有列出 PC 喇叭，请尝试选择声卡对应的设备——PulseAudio 代理控制可能不会列出 PC 喇叭。

### GNOME

使用 [GSettings](<../zh-cn/GNOME.html#%E9%85%8D%E7%BD%AE> "GNOME"): 
    
    $ gsettings set org.gnome.desktop.wm.preferences audible-bell false
    
### KDE Plasma

响铃通知设置可在“系统设置”→“辅助功能”→“响铃”更改。 

### Cinnamon

[Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") 似乎会播放水滴声。要禁用它，设置 [gsettings(1)](<https://man.archlinux.org/man/gsettings.1>)： 
    
    $ gsettings set org.cinnamon.desktop.wm.preferences audible-bell false
    
### GTK

将以下行加入 `.gtkrc-2.0`： 
    
    gtk-error-bell = 0
    
以及 `$XDG_CONFIG_HOME/gtk-3.0/settings.ini` 的 [Settings] 部分： 
    
    [Settings]
    gtk-error-bell = 0
    
这在 [Gnome 开发者手册](<https://developer.gnome.org/gtk3/stable/GtkSettings.html>)中有记载。 

### PulseAudio

[使用 PulseAudio](<../zh-cn/PulseAudio.html#X11_Bell_Events> "PulseAudio") 以播放声音取代 PC 喇叭蜂鸣。 

### Arch Linux ISO

如果你想禁用 Arch Linux ISO 的初始化声音，需要重新打包 ISO。首先，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libisoburn](<https://archlinux.org/packages/?name=libisoburn>)包 和 [mtools](<https://archlinux.org/packages/?name=mtools>)包。 

从 ISO 中提取 El Torito 启动映像和 systemd-boot 配置文件（`loader.conf`）： 
    
    $ osirrox -indev archlinux-_YYYY.MM.DD_ -x86_64.iso -extract_boot_images ./ -extract /loader/loader.conf loader.conf
    
将 `loader.conf` 设为可读写，并移除 `beep` 选项： 
    
    $ chmod +w loader.conf
    $ sed '/^beep on/d' -i loader.conf
    
将修改后的 `loader.conf` 添加到 El Torito UEFI 启动映像： 
    
    $ mcopy -D oO -i eltorito_img2_uefi.img loader.conf ::/loader/
    
最后，使用修改后的启动映像和 `loader.conf` 重新打包 ISO： 
    
    $ xorriso -indev archlinux-_YYYY.MM.DD_ -x86_64.iso \
    	-outdev archlinux-_YYYY.MM.DD_ -x86_64-silent.iso \
    	-map loader.conf /loader/loader.conf \
    	-boot_image any replay \
    	-append_partition 2 0xef eltorito_img2_uefi.img
    
**注意：** 该操作只会禁用初始化声音，启动后还是有可能会发出蜂鸣声。要在启动后禁用 PC 扬声器，请参考[#全局设置](<#%E5%85%A8%E5%B1%80%E8%AE%BE%E7%BD%AE>)。

## Beep

用户可以在登录到[虚拟控制台](<../zh-cn/Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0.html#%E8%99%9A%E6%8B%9F%E6%8E%A7%E5%88%B6%E5%8F%B0> "Linux 控制台")时发出短促的声音。详见 [Wikipedia:bell character#usage](<https://en.wikipedia.org/wiki/bell_character#usage> "wikipedia:bell character")。 

Beep 是一个高级 PC 喇叭蜂鸣程序。它可以用于没有声卡和/或扬声器可用，同时希望有简单音频通知的情况。 

###  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [beep](<https://archlinux.org/packages/?name=beep>)包 软件包。 

可能也需要在[ALSA](<../zh-cn/ALSA.html> "ALSA")中[解除](<#ALSA>)对 PC 喇叭的静音。 

###  作为非 root 用户运行

`beep` 使用 `/dev/input/by-path/platform-pcspkr-event-spkr` 来控制 PC 喇叭。要作为非 root 用户访问它，必须设置适当的权限。创建 `/etc/udev/rules.d/70-pcspkr-beep.rules` 并添加以下规则： 
    
    ACTION=="add", SUBSYSTEM=="input", ATTRS{name}=="PC Speaker", ENV{DEVNAME}!="", TAG+="uaccess"
    
这会允许任何登录到当前活动虚拟控制台会话的用户使用 PC 喇叭。 

或者可以设置一个新的用户组（如 `beep`）并设置相应规则，以对设备文件设置正确的权限： 
    
    ACTION=="add", SUBSYSTEM=="input", ATTRS{name}=="PC Speaker", ENV{DEVNAME}!="", GROUP="beep", MODE="0620"
    
使用这种方式， `beep` 组中的任何用户都能够控制喇叭。 

执行以下命令强制重新载入规则与设备文件，从而无需重启即可应用新的用户权限： 
    
    # udevadm control --reload && rmmod pcspkr && modprobe pcspkr
    
###  提示与技巧

很多人可能喜欢传统蜂鸣声，也有些人可能想要改变一下它的属性。下面的例子可以播放音调稍高，长度稍短的声音并重复两遍。 
    
    # beep -f 5000 -l 50 -r 2
    
##  相关阅读

  * [xset(1)](<https://man.archlinux.org/man/xset.1>)，[setterm(1)](<https://man.archlinux.org/man/setterm.1>)，[bash(1)](<https://man.archlinux.org/man/bash.1>)
  * <https://github.com/NaWer/beep> 和 <https://github.com/ShaneMcC/beeps> \- 使用 beep 播放各种音乐的 bash 脚本代码库
