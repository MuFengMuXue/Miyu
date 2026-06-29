**翻译状态：**

  * 本文（或部分内容）译自 [LMMS](<https://wiki.archlinux.org/title/LMMS> "arch:LMMS")，最近一次同步于 2025-02-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/LMMS?diff=0&oldid=826711>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/LMMS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Rosegarden](<../zh-cn/Rosegarden.html> "Rosegarden")

[LMMS](<https://lmms.io/>) 是一个开源、跨平台的数字音频工作站（DAW），您可以用它在您的计算机上创作音乐。包括创作旋律和节拍、合成/混合声音以及排列样本。使用你的 MIDI 键盘和其他工具可以更富乐趣——尽在一个友好且现代化的界面中。此外， LMMS 自带许多开箱即用的乐器、效果插件、预设和样本。 

##  安装

安装 [lmms](<https://archlinux.org/packages/?name=lmms>)包 或 [lmms-git](<https://aur.archlinux.org/packages/lmms-git/>)AUR （开发版本）。发行注记参见 [[1]](<https://github.com/LMMS/lmms/releases>)。 

如同大部分时候，您若想同时运行多个音频应用，但您的硬件不支持这样，您会需要一个[用户模式的音频服务器](<../zh-cn/%E9%9F%B3%E9%A2%91%E7%B3%BB%E7%BB%9F.html#%E9%9F%B3%E9%A2%91%E6%9C%8D%E5%8A%A1%E5%99%A8> "音频系统")，或者配置 [ALSA dmix](<../zh-cn/ALSA.html#Dmix> "ALSA"). 

##  MIDI 与 soundfont

根据您的设置和安装方法，您可能需要手动设置 [soundfont](<../zh-cn/MIDI.html#SoundFont_%E5%88%97%E8%A1%A8> "MIDI") 和 [Timidity++](<../zh-cn/Timidity++.html> "Timidity++")。 

然后，您需要编辑 FluidSynth 配置文件： `/etc/conf.d/fluidsynth`。对于音频驱动程序，请选择已安装的声音服务器。 

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") [user 服务](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户") `fluidsynth.service`。 

LMMS 启动时，会提示您进行设置。转到音频设置，选择与为 FluidSynth 设置的相同接口，如果进行了切换，则需重启 LMMS。 

##  疑难解答

一些用户在 Wayland 上遇到了拖放支持问题。要恢复这一功能，可以尝试设置环境变量 `QT_QPA_PLATFORM=xcb` 以让 LMMS 在 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 中启动。 
