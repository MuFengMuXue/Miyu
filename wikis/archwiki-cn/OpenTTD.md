**注意：** 本页面**不是** 英文页面的翻译。请勿不加选择地将英文页面同步至本页面。

[OpenTTD](<https://www.openttd.org/>) 是对受欢迎的 DOS 游戏 [Transport Tycoon Deluxe](<https://en.wikipedia.org/wiki/Transport_Tycoon_Deluxe> "wikipedia:Transport Tycoon Deluxe") 的自由重新实现。在此游戏里，您是一家运输公司的所有者，您必须长年累月地管理公司以获取利润。 

[![](../File:550px-OpenTTD.webp.png)](<../File:OpenTTD.webp>)OpenTTD 主窗口，版本：14.1，字体：Noto Sans CJK SC。

##  安装

###  官方版 OpenTTD

####  游戏本体

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [openttd](<https://archlinux.org/packages/?name=openttd>)包 包。 

也可以安装最新 Git 构建：[openttd-git](<https://aur.archlinux.org/packages/openttd-git/>)AUR。 

####  基础图形与音效

如果您没有原版游戏，[openttd-opengfx](<https://archlinux.org/packages/?name=openttd-opengfx>)包 和 [openttd-opensfx](<https://archlinux.org/packages/?name=openttd-opensfx>)包 包含自由的图形和声音。 

####  基础音乐

您可以安装自由的 [OpenMSX](<https://wiki.openttd.org/en/Basesets/OpenMSX>) 音乐包，它可以在游戏中下载，也可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [openttd-openmsx](<https://aur.archlinux.org/packages/openttd-openmsx/>)AUR（查看 [AUR 上的讨论](<https://aur.archlinux.org/packages/openttd-openmsx>)获取有关打包信息）。您需要确保 [Fluidsynth](<../zh-cn/FluidSynth.html#%E7%8B%AC%E7%AB%8B%E6%A8%A1%E5%BC%8F> "Fluidsynth") 可用。安装一个 [Soundfont](<../zh-cn/MIDI.html#SoundFont_%E5%88%97%E8%A1%A8> "MIDI") 以确保音乐正常播放，参见[#音乐不播放](<#%E9%9F%B3%E4%B9%90%E4%B8%8D%E6%92%AD%E6%94%BE>)。 

####  社交插件

OpenTTD 可以加载插件，与 [Steam](<../zh-cn/Steam.html> "Steam")、[Discord](<../zh-cn/Discord.html> "Discord") 等社交平台集成。 

要实现这种集成，必须下载特定平台的插件并将其存储在 `social_integration` 文件夹中。 

请参阅 [OpenTTD 网站](<https://www.openttd.org/downloads/openttd-releases/latest>)，查看可用插件。 

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 上已有 Discord 插件的打包：[openttd-discord-social-bin](<https://aur.archlinux.org/packages/openttd-discord-social-bin/>)AUR。 

####  Transport Tycoon Deluxe 原始数据（可选）

OpenTTD 可以使用原始 Windows/DOS 版本的 Transport Tycoon Deluxe 的非自由图形和声音数据。 

**注意：** 虽然您可以从 DOS 或 Windows 版本的游戏中转存文件，但只有 Windows 版本才提供原始音乐。

您可以从游戏光盘、现有安装文件中获取这些文件，也可以从 [Abandonia](<http://www.abandonia.com/en/games/240>) 免费提供的游戏安装存档中获取。 

要使用原始图形和音效，请将以下文件复制到 `/usr/share/openttd/data/` 或 `~/.local/share/openttd/baseset` ： 

  * Windows : trg1r.grf, trgcr.grf, trghr.grf, trgir.grf, trgtr.grf
  * DOS : TRG1.GRF, TRGC.GRF, TRGH.GRF, TRGI.GRF, TRGT.GRF
  * 来自任意版本的 sample.cat

如果是原始配乐，请将原始 TTD 游戏目录下 gm 文件夹中的文件复制到 `~/.local/share/openttd/gm` 中。 

[openttd-ttdwin](<https://aur.archlinux.org/packages/openttd-ttdwin/>)AUR 大致实现了安装原始游戏文件的**过程** 。 

**注意：** TTD 数据文件受版权保护，不包括在 [openttd-ttdwin](<https://aur.archlinux.org/packages/openttd-ttdwin/>)AUR 内。

###  含补丁的 OpenTTD

**注意：** 以下补丁都不是官方维护的。它们的游戏体验与[#官方版 OpenTTD](<#%E5%AE%98%E6%96%B9%E7%89%88_OpenTTD>) 不完全一致（如缺少翻译、存在程序缺陷等）。

#### JGRPP

关于 JGRPP 的详细信息，参见 [OpenTTD JGRPP 中文百科](<https://ottdzh.readthedocs.io/projects/jgrpp/latest/>)（[英文原版](<https://github.com/jgrennison/openttd-patches/wiki>)）。 

OpenTTD 最有名的补丁莫过于 JGRPP 了，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [openttd-jgrpp](<https://aur.archlinux.org/packages/openttd-jgrpp/>)AUR 软件包。 

#### n-ice

citymania 客户端的分支版，针对 n-ice 和 btpro 社区进行了修改。 

要安装此补丁，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [openttd-n-ice](<https://aur.archlinux.org/packages/openttd-n-ice/>)AUR。 

**注意：** 截止到本文最后一次修订，此 AUR 包仍严重过时且维护不积极，建议自行[编译](<https://github.com/n-ice-community/openttd-cmclient>)。

##  教程

游戏一开始可能会让人一头雾水。[中文维基](<https://wiki.openttd.org/zh/Manual/>)和[英文维基](<https://wiki.openttd.org/en/Manual/>)上有很好的[教程](<https://wiki.openttd.org/zh/Manual/Tutorial/%E6%95%99%E7%A8%8B>)。 

对于游戏内的教程，我们已经实现了一个游戏脚本。 只需使用游戏内的 _在线查找拓展包_ 中下载 _Beginner Tutorial -Game Script_ ，然后加载 _Beginner Tutorial_ 场景即可。 

还有中文社区维护的 [OpenTTD 社区文档](<https://ottdzh.readthedocs.io/>)（[Github 仓库](<https://github.com/OpenTTD-China-Set/OpenTTD-documents>)）。 

##  配置

关于 OpenTTD 目录结构，参见 [Github 上的说明文档](<https://github.com/OpenTTD/OpenTTD/blob/master/docs/directory_structure.md>)。 

###  游戏配置

OpenTTD 主配置文件位于 `~/.openttd/openttd.cfg` 或 `~/.config/openttd/openttd.cfg`，首次启动时会自动创建。每次退出 OpenTTD 时，它都会将游戏中任何更改写入配置文件。 

配置文件中的各种设置可通过主菜单上的按钮进行编辑。有以下按钮： 

  * 游戏选项
  * 设置
  * AI 设置
  * NewGRF 设置
  * 游戏脚本设置

###  Wayland 支持

[SDL3](<../zh-cn/SDL.html> "SDL3") 已默认启用 [Wayland](<../zh-cn/Wayland.html> "Wayland")，但 OpenTTD 仍未迁移至 SDL3。欲为 OpenTTD 启用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 支持，设置 `SDL_VIDEODRIVER=wayland` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。JGRPP 等补丁版设置方法同上。 

参见 [Wayland#SDL](<../zh-cn/Wayland.html#SDL> "Wayland")。 

##  多人游戏

###  客户端

玩家可以使用多人游戏菜单加入服务器。在多人游戏中，禁用快进、玩家暂停和作弊功能。 

服务器的所有问题都应由服务器管理员来解决，通常不是程序缺陷，只是服务器配置错误。 

###  服务器

您可以通过 `-D ` 参数启动服务器，例如 
    
    # openttd -D 0.0.0.0:3979
    
这将启动服务器并接受[附加命令](<https://wiki.openttd.org/en/Manual/Console%20Commands>)。配置会生成并存储在 `~/.config/openttd/openttd.cfg` 中，每次服务器启动时都会读取。在服务器运行时，可以通过直接向服务器发送命令来覆盖配置。某些设置无法在游戏中更改。 

您可以创建 [Systemd 服务](<../zh-cn/Systemd.html> "Systemd")在后台运行，或者使用 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 之类的软件。 

要公开您的服务器，您需要一个面向公众的服务器，并正确设置所有端口转发。默认端口为 3979。 

##  提示与技巧

###  高度图

OpenTTD 允许使用灰度图像作为[高度图](<https://wiki.openttd.org/en/Manual/Heightmap>)来生成地形图。[terrain.party](<https://terrain.party/>) 上有一个基于真实地球地形的出色的高度图生成器。此外，您也可以使用 [bother](<https://aur.archlinux.org/packages/bother/>)AUR 应用程序，该程序可以下载更大的区域，并包含许多用于微调生成的高度图的选项（使用注意事项请参见 [README](<https://github.com/bunburya/bother/blob/master/README.md>)）。您还可以使用 [GIMP](<../zh-cn/GIMP.html> "GIMP") 对高度图进行微调，其中的“色阶”和“高斯模糊”工具尤为实用。 

###  沙盒选项

在当前游戏按下 `Ctrl+Alt+C`，即可显示 _沙盒选项_ （旧“作弊菜单”）。 

有关沙盒选项的详细信息，请访问[官方 Wiki 页面（英文）](<https://wiki.openttd.org/en/Manual/Sandbox%20options>)。 

###  多人游戏

一定要为自己的公司设置一个密码，以免被他人接管。有些服务器会在闲置一段时间后重置你的密码。 

如果轨道建造菜单未打开，则可使用 `t` 字母调出聊天。 

您可以通过购买股票（如果服务器已启用）投资其他公司。随后，您可以出售股票以获取利润，或亏损。 

##  问题解决

###  无法使用 Fcitx5

设置 `SDL_IM_MODULE=fcitx` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。 

参见 [Fcitx5#X11](<../zh-cn/Fcitx_5.html#X11> "Fcitx5")。 

###  XWayland 下开启垂直同步后卡死

使 OpenTTD [在 Wayland 下运行](<#Wayland_%E6%94%AF%E6%8C%81>)可能会解决问题。 

参见 [Wayland#SDL](<../zh-cn/Wayland.html#SDL> "Wayland")。 

###  音乐不播放

游戏的配乐由 [MIDI](<../zh-cn/MIDI.html> "MIDI") 文件组成。因此，您需要使用 [MIDI 合成器](<../zh-cn/MIDI.html#%E5%90%88%E6%88%90%E5%99%A8> "MIDI")来播放它们。 

游戏会自动尝试使用 [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth")（[openttd](<https://archlinux.org/packages/?name=openttd>)包 的依赖），无需额外参数。如果出于某种原因您需要/想要使用其他合成器，OpenTTD 提供了 “extmidi” 音乐驱动程序，您可以通过配置命令来播放音乐。 

**警告：**

  * 使用 extmidi 驱动程序时，游戏内的音量控制滑块将被禁用，无法用来更改音量。
  * 如果要运行的命令未包含在 `$PATH` 中，则必须指定绝对路径。

**提示：** 一般情况下，如果您是首次使用 MIDI 合成器，您只需再安装一个 [Soundfont](<../zh-cn/MIDI.html#SoundFont_%E5%88%97%E8%A1%A8> "MIDI") 即可播放音乐，因为 [fluidsynth](<https://archlinux.org/packages/?name=fluidsynth>)包 已作为依赖而被安装。

[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `openttd.cfg` 以配置 extmidi ： 
    
    ~/.config/openttd/openttd.cfg
    
    [misc]
    musicdriver = "extmidi:cmd=<command>"

**注意：** 您还可以在启动游戏时配置 extmidi： `openttd -m extmidi:cmd=<command>`

但是，extmidi 不允许在命令中添加参数。解决办法是使用封装脚本： 
    
    ~/.config/openttd/playmidi
    
    #!/bin/bash
    
    # 在这里，我们假定要使用 [FluidSynth](<../zh-cn/FluidSynth.html> "FluidSynth") 合成器和Soundfont  [soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包
    # 在 [soundfont-fluid](<https://archlinux.org/packages/?name=soundfont-fluid>)包 和 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 中提供。
    
    trap "pkill fluidsynth" EXIT
    fluidsynth -a pulseaudio -i /usr/share/soundfonts/FluidR3_GM2-2.sf2 $*
    
令之[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。 

然后，您可以指定脚本的完整路径，作为与 extmidi 一起使用的命令： 
    
    ~/.config/openttd/openttd.cfg
    
    [misc]
    musicdriver = "extmidi:cmd=/home/<user>/.config/openttd/playmidi"

##  参见

  * [OpenTTD](<https://www.openttd.org>)
  * [OpenTTD FAQ](<https://wiki.openttd.org/en/Archive/Community/FAQ%20troubleshooting>)
  * [OpenTTD Wiki](<https://wiki.openttd.org/zh/>)
  * [OpenTTD 官方社区](<https://forum.openttd.org/>)
  * [openttd 吧](<https://tieba.baidu.com/f?kw=openttd>)
