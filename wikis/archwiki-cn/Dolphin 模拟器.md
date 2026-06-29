**翻译状态：**

  * 本文（或部分内容）译自 [Dolphin emulator](<https://wiki.archlinux.org/title/Dolphin_emulator> "arch:Dolphin emulator")，最近一次同步于 2024-5-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dolphin_emulator?diff=0&oldid=814796>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dolphin_emulator_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Dolphin](<https://dolphin-emu.org/>) 是任天堂 GameCube 和 Wii 模拟器，目前支持 x86_64 和 AArch64 架构。Dolphin 适用于 Linux、macOS、Windows 和 Android。这是一个自由开源的社区开发项目。Dolphin 是第一个 GameCube 和 Wii 模拟器，也是目前唯一能够玩商业游戏的模拟器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[dolphin-emu](<https://archlinux.org/packages/?name=dolphin-emu>)包软件包。 

##  配置

**提示：** 运行 `dolphin-emu -h` 查找 Dolphin 的帮助选项。

**注意：** Dolphin 可能会根据每个游戏覆盖这些设置，例如当已知某个设置会破坏某个游戏时。如果绝对确定特定设置不会使游戏崩溃，则可以通过右键单击游戏并选择 _属性_ 来禁用或更改这些覆盖。同样，您可以使用此方法设置每个游戏的设置。

虽然模拟器运行不需要其他配置（它已预配置了默认设置），但更改设置可以提高性能和图形。设置分为三个主要部分： _配置_ 、 _图形_ 和 _DSP_ 。 

###  配置部分

**提示：** 最新版本的 Dolphin 删除了 _音频_ 跳帧选项，因此现在建议使用 _自动_ 。

在常规选项卡上，选中 _启用双核_ 和 _启用空闲跳过_ 。帧限制应设置为 _自动_ ，以便它适用于所有地区的游戏。CPU 仿真引擎应保留为 JIT Recompiler。如果打算播放导入的日本光盘，请仅选中“强制控制台为 NTSC-J”。 

_界面_ 选项卡上的所有选项都是个人选择。 

音频选项卡是 DSP 部分的屏幕;现在设置它意味着以后无需进行设置。请参阅下面的 [DSP 设置段落](<#DSP_section>)。 

接下来的两个选项卡不是很重要;Gamecube 选项卡具有有关连接配件（例如存储卡）的设置，唯一值得注意的 Wii 选项卡选项是“纵横比”下拉列表。将其设置为 16：9 或 4：3，具体取决于显示器的[纵横比](<https://en.wikipedia.org/wiki/Aspect_ratio> "wikipedia:Aspect ratio")。 

在最后一个选项卡“路径”上，可以设置 ISO 目录。游戏 ISO 的目录也可以通过单击主屏幕上的浏览来设置，但这里有更多选项可用，例如 _搜索子文件夹_ 。 

###  图形部分

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 提供新的 3D 选项。 (在 [Talk:Dolphin 模拟器](<../zh-cn/Talk:Dolphin_%E6%A8%A1%E6%8B%9F%E5%99%A8.html>) 中讨论)

在“常规”选项卡上，从当前最兼容的渲染器的后端下拉列表中选择 OpenGL。将“显示”和“其他”设置设置为所需的配置。垂直同步很有用，但它可能会导致速度变慢。“渲染到主窗口”选项在美学上改善了体验。 

如果您的显卡支持 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")，则使用 Vulkan 后端可能会为您提供比 OpenGL 更高的性能。请注意，Vulkan 后端可能与某些游戏不兼容，因此如果您在游戏中遇到问题，请尝试在放弃之前切换回 OpenGL。官方[兼容性列表](<https://dolphin-emu.org/compat/>)通常包含有关每个渲染器如何处理标题的提示。 

在“增强功能”选项卡上是可以改进图形的选项。虽然它们会产生出色的输出，但它们可能会减慢仿真速度，使游戏无法玩。选择最佳设置，只要速度保持 100%。 下表翻译质量不高，请参考英文原文。 

选项比较  选项 | 性能 | 质量   
---|---|---  
**内部分辨率** | 1x Native | 自动 (窗口大小)   
**反锯齿** | 无 | 至少 2x   
**各向异性滤波** | 1x | 至少 2x   
**后处理效果** | (关) | 你的选择  
(参见下面的提示)   
**缩放的 EFB 副本** | 取消选中 | 选中   
**单独像素光源** | 取消选中 | 选中   
**强制纹理过滤,  
宽屏黑客,  
禁用雾** | 关 | 你的选项  
(推荐: 关)   
  
**提示：** Dolphin 能够在立体 3D 中渲染为 2D 开发的游戏。要启用此功能，请将 _后处理效果_ 设置为 _立体_ （默认，对于红青色模式）或 _立体 2_ （蓝黄色）。还 _必须_ 取消选中 _黑客_ 选项卡上的 _快速深度计算_ （ _见下文_ ）。

**注意：** 使用滤镜和其他方法来改进图形可能会破坏一些游戏或导致任何级别的图形故障。

除非确定，否则最好保持 _黑客_ 选项卡不变。 

默认  选项 | 值   
---|---  
跳过从 CPU 访问 EFB | 取消选中   
忽略格式更改 | 选中   
EFB 副本 | 纹理   
纹理缓存/精度 | 快   
外部帧缓冲器 | 不启用   
缓存显示列表 | 取消选中   
禁用目标 Alpha | 取消选中   
OpenCL 纹理解码器 | 取消选中   
OpenMP 纹理解码器 | 取消选中   
快速深度计算 | 选中  
(应取消选中浮雕 3D)   
Vertex streaming hack | unchecked   
  
同样，除非确定，否则请取消选中 _高级_ 选项卡中的 _所有内容_ 。 

###  DSP 部分

将 DSP 仿真引擎设置为 

  * DSP HLE用于速度胜于精度，
  * DSP LLE 重新编译器以一定的速度为代价获得更好的准确性，
  * DSP LLE解释器;准确，但使 _一切_ 都无法播放。太慢了。

_单独线程上的 DSP LLE_ 可提高具有多核 CPU 的计算机的速度，但可能会导致音频故障，并且已知会破坏[塞尔达 ucode games](<https://wiki.dolphin-emu.org/index.php?title=Category:Zelda_ucode_games>)。音频后端最好设置为 [ALSA](<../zh-cn/ALSA.html> "ALSA")。对于 `pulseaudio` ，需要安装 Dolphin 的可选依赖项 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")。 

**注意：** 如果您从[配置部分的](<#%E9%85%8D%E7%BD%AE%E9%83%A8%E5%88%86>)链接来到这里，您现在应该返回。

##  游玩

**注意：** Dolphin 是一个资源密集型应用程序，因此并非所有游戏都能正常运行。请在[此处](<https://dolphin-emu.org/docs/faq/#why-do-i-need-such-powerful-computer-emulate-old-c>)查看原因。

**警告：** 确保您 _仅_ 将 Dolphin 用于合法购买的游戏的合法获得的自制光盘转储。Dolphin 不是为非法使用而开发的。按照适用法律的规定合法行事。您应对您对模拟器的任何使用负责。本维基上不会提供获取非法内容的链接、说明或提示。无意侵犯版权。

单击“浏览”以设置 ISO 目录，以便它们在 Dolphin 的默认屏幕上显示为库。否则，只需单击 _打开_ 并选择文件即可。 

###  Dolphin的 Wiki

每当游戏无法正常工作时，请尝试阅读 [Dolphin的wiki](<https://wiki.dolphin-emu.org>)上的页面。列出了有关为每个游戏设置模拟器的提示、版本兼容性图表、测试条目、故障排除和视频预览。欢迎贡献，例如测试条目和解决方法，并帮助其他用户。 

下面是一个 [xfce4-whiskermenu-plugin](<https://archlinux.org/packages/?name=xfce4-whiskermenu-plugin>)包 搜索操作命令，用于在 Dolphin 的 wiki 上进行搜索： 
    
    exo-open --launch WebBrowser <https://wiki.dolphin-emu.org/index.php?search=%u>
    
**提示：** 建议设置键盘映射。更喜欢具有模拟功能的游戏手柄，而不是键盘和鼠标。请参阅[GameCube游戏手柄的地图](<https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/GCController_Layout.svg/1000px-GCController_Layout.svg.png>)。还建议在玩耍时玩得开心。

##  主题

要更改 Dolphin 的主题，请在目录中 `~/.local/share/dolphin-emu/Styles` 放置一个 css 文件。然后转到 _选项_ 中的 _界面_ 选项卡并选中 使用 _自定义用户样式_ 框。单击 _用户样式_ 选项卡以更改主题。 

##  故障排除

###  与 Wayland 不兼容

Dolphin 5.0 与 Wayland 不兼容。通过以下命令强制它作为 X11 应用程序运行： 
    
    QT_QPA_PLATFORM=xcb dolphin-emu
    
###  游戏太快

确保将帧限制设置为游戏区域的正确值;NTSC 游戏为 60 个，PAL 游戏为 50 个。建议使用 _自动_ 。避免使用 Dolphin 同时播放其他媒体。 

###  模拟器太慢了

仔细检查 [CPU调速器](<../zh-cn/CPU_%E8%B0%83%E9%A2%91.html#%E8%B0%83%E9%80%9F%E5%99%A8> "CPU 调频")。如果使用 NVidia 显卡，则在 nvidia-settings 上将 powermizer 设置更改为“首选最高性能”;不过，请检查其温度以确保卡不会过热。更改 Dolphin 的优先级使用 _nice_ 。终止不必要的进程和禁用合成也有帮助。如上所述，正确配置 Dolphin 是最重要的部分。 

许多系统都有多个 GPU，例如英特尔的集成低性能 GPU 和专用显卡。请参阅 [PRIME](<../zh-cn/PRIME.html> "PRIME")，了解如何在专用 GPU 上执行 Dolphin。 

###  游戏在第一次通关时经常卡顿，但后续运行很流畅

这种卡顿可能是因为着色器编译导致图形渲染必须暂停。Dolphin 已经获得了将这种口吃降至最低的先进技术，称为 Ubershaders。它们需要强大的 GPU 才能发挥最佳作用，因此默认情况下不启用。在图形配置对话框的 _着色器编译_ 下，尝试 _同步（Ubershaders）_ 或 _异步（Ubershaders）_ 选项之一。将鼠标悬停在单选按钮上可查看对话框中更详细的说明文本。使用 _在开始之前编译着色器_ 选项也可以减少卡顿，但代价是游戏开始前的延迟时间更长。 

参见: [性能优化](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html> "性能优化")——大多数建议应该会有帮助。 

##  参见

  * [Wikipedia:Dolphin (emulator)](<https://en.wikipedia.org/wiki/Dolphin_\(emulator\)> "wikipedia:Dolphin \(emulator\)")
  * [Dolphin的性能指南。](<https://dolphin-emu.org/docs/guides/performance-guide/>)
  * [Dolphin的 FAQ](<https://dolphin-emu.org/docs/faq/>)
  * [Dolphin 的 wiki 条目，用于合法获取游戏转储](<https://wiki.dolphin-emu.org/index.php?title=Ripping_Game_Discs>)
