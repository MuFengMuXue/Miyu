**翻译状态：**

  * 本文（或部分内容）译自 [DaVinci Resolve](<https://wiki.archlinux.org/title/DaVinci_Resolve> "arch:DaVinci Resolve")，最近一次同步于 2025-03-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/DaVinci_Resolve?diff=0&oldid=829772>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DaVinci_Resolve_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:DaVinci Resolve#](<../zh-cn/Talk:DaVinci_Resolve.html>) 中讨论）

相关文章

  * [OpenCL](<../zh-cn/GPGPU.html#OpenCL> "OpenCL")

[达芬奇专业剪辑工具](<https://www.blackmagicdesign.com/products/davinciresolve/>)是一个专有的视频编辑软件，包括调色、色彩校正、视觉特效、动态图形和音频后期制作的生产工具。 

##  安装

有受限的免费版本和付费(Studio)版本。 

对于免费版，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [davinci-resolve](<https://aur.archlinux.org/packages/davinci-resolve/>)AUR 或 [davinci-resolve-beta](<https://aur.archlinux.org/packages/davinci-resolve-beta/>)AUR 。 

若要获取付费版本，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [davinci-resolve-studio](<https://aur.archlinux.org/packages/davinci-resolve-studio/>)AUR 或 [davinci-resolve-studio-beta](<https://aur.archlinux.org/packages/davinci-resolve-studio-beta/>)AUR。 

**注意：** 自 19.1.3-2 版本后，你必须手动从 [Blackmagic Design 的官方网站](<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>) 中下载安装器，并在编译包之前将其放在与 PKGBUILD 同目录中 [[1]](<https://aur.archlinux.org/packages/davinci-resolve#comment-1008736>) 。安装后如遇问题请参见文末。

需要使用合适的 OpenGL 和 OpenCLC 驱动来运行 DaVinci Resolve。对于AMD和Intel显卡可以通过 Mesa ([Rusticl](<https://docs.mesa3d.org/rusticl.html>)) 使用OpenCL 开源驱动。 [NixOS Wiki 提供了一份 DaVinci Resolve 支持的 AMD 显卡兼容性表格](<https://wiki.nixos.org/wiki/DaVinci%20Resolve>)。 

OpenGL 驱动表格  GPU 制造商 | OpenGL 驱动 | 是否开源 | 文档 | 已测试的驱动版本 | 是否能够运行DaVinci Resolve | 测试的DaVinci Resolve版本 | 注释   
---|---|---|---|---|---|---|---  
AMD  | [mesa](<https://archlinux.org/packages/?name=mesa>)包 | 是 | [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") | 23.0.2-2 | 是 | 18.1.4-1 | 在Vega之前的GPU上，如果使用 opencl-amd 和 mesa, DR会崩溃，详见 [这篇](<https://gitlab.freedesktop.org/mesa/mesa/-/issues/6256>) bug 报告。你可以用rocm 和 `ROC_ENABLE_PRE_VEGA=1` 或使用 opencl-amd 和 progl 来代替。 已在 Radeon RX 580 测试过。 已在 Radeon PRO W6600测试过。   
Intel  | [mesa](<https://archlinux.org/packages/?name=mesa>)包 | 是 | [Intel graphics](<../zh-cn/Intel_graphics.html> "Intel graphics") | 23.1.6 | 是 | 19.1.3 | 正常工作。 已在 Intel Iris Xe 显卡（Alder Lake Mobile）测试过。   
NVIDIA  | [mesa](<https://archlinux.org/packages/?name=mesa>)包 | 是 | [Nouveau](<../zh-cn/Nouveau.html> "Nouveau") |  | 否 |  |   
[nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 | 否 | [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") | 575.64.05-2 | 是 | 19.1.3 | 此前在 Optimus 笔记本上用 nvidia-xrun 测试过。 用 RTX 3060 测试过，运行无误。   
测试过的[OpenCL](<../zh-cn/GPGPU.html#OpenCL> "OpenCL")驱动表  GPU 制造商 | OpenCL 驱动 | 是否开源 | 测试的驱动版本 | 是否能够运行DaVinci Resolve | 测试的DaVinci Resolve版本 | 评价   
---|---|---|---|---|---|---  
Neutral  | [opencl-rusticl-mesa](<https://archlinux.org/packages/?name=opencl-rusticl-mesa>)包 | 是 | 1:23.3.2-2 | 是 | 18.6.4-1 | 这只有在未安装[opencl-clover-mesa](<https://archlinux.org/packages/?name=opencl-clover-mesa>)包 的情况下才有效, 否则 DR 会用 Clover 而不是 rusticl。部分内核版本存在[ROCm问题](<https://github.com/ROCm/ROCm/issues/2596>), 但 6.1 LTS 和 6.10.2 工作正常。 已在RX 6800M测试过。   
mesa-tkg-git | 是 | 24.0.0_devel.180705.fdbb5d58983-1 | 是 | 18.6 | DR 现在与 Rusticl 合作，因为[MR 21305](<https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/21305>) 已合并 (commit [0a072bb3](<https://gitlab.freedesktop.org/mesa/mesa/-/commit/0a072bb31c0aa99ba6f8348e0e601053b643a584>))。 已在RX 7600 使用 `RUSTICL_ENABLE=radeonsi`测试过。   
AMD  | [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR | Pro和开源组件混合使用 | 1:5.6.0-2 | 是 | 18.5b | 目前没有仅包含 Ubuntu 重新打包 rocm 驱动的 AUR 包（[opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR同时打包了 rocm 和 orca）。在 GFX8（RX 580 等）上，默认使用 ORCA 遗留驱动，而该驱动本身目前需要 AMDGPU-PRO OpenGL 驱动才能工作（见上文）。 已在 Radeon Pro W6600测试过 (正常，甚至用mesa也行)。 已在 Radeon RX 580 测试过(正常，目前只支持 Progl)。 已在 Radeon RX 5700 XT、6700XT测试过(使用mesa) 当尝试在颜色页面上进行颜色校正时，地址崩溃 (和 rocm-opencl-runtime包冲突) 已在 Radeon 7900XT测试过。   
[rocm-opencl-runtime](<https://archlinux.org/packages/?name=rocm-opencl-runtime>)包 | 是 | 5.4.3-1 | 是 | 18.1.4-1 | 对于比 GFX9/Vega老的GPU， 使用变量`ROC_ENABLE_PRE_VEGA=1`; 在OpenGL Mesa中生效。 已在Radeon Pro W6600测试过。 已在AMD RX580测试过。色彩校正可能会导致崩溃（Radeon 7900XT 曾发生过），建议使用 [opencl-amd 5.6.0-2](<https://aur.archlinux.org/cgit/aur.git/commit/?h=opencl-amd&id=b2ca61a9c89de4a6569fcfacef98ee156f1d5196>)。   
[opencl-legacy-amdgpu-pro](<https://aur.archlinux.org/packages/opencl-legacy-amdgpu-pro/>)AUR | 否 | 22.10.1_1401426-1 | 是, 对于比Vega老的GPU | 17.4.6-2 | 请注意，这只是没有 ROCm 驱动的[opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR包 需要 AMDGPU-PRO OpenGL 驱动才能正常工作。 已在Radeon RX580测试过。   
Intel  | [intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包 | 是 | 25.27.34303.5-1 | 是 | 19.1.3 | 运行顺利。 已在Intel Itis Xe（Alder Lake Mobile）测试过。   
mesa [with the cl-gl sharing MR applied](<https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/21305>) | 是 | 23.3.0 with MR applied | 是 | 18.6 | 可支持导出为环境变量的`RUSTICL_ENABLE=iris`。   
[beignet](<https://aur.archlinux.org/packages/beignet/>)AUR | 是 | 1.3.2+12+gfc5f430c-2 | 否 |  | Core dumped   
[intel-opencl](<https://aur.archlinux.org/packages/intel-opencl/>)AUR | 否 | 5.0.r63503-2 | 否 |  | Core dumped   
[intel-opencl-runtime](<https://aur.archlinux.org/packages/intel-opencl-runtime/>)AUR | 否 | 1:18.1.0.013-2 | 否 |  | Core dumped   
Nvidia  | [opencl-nvidia](<https://archlinux.org/packages/?name=opencl-nvidia>)包 | 否 | 460.32.03-1 | 是 |  | 合适, 但改为在CUDA上运行？   
  
###  DaVinci Resolve检查器

可以通过运行 [davinci-resolve-checker](<https://github.com/Ashark/davinci-resolve-checker>) 脚本以确认自己的配置是否能够正常运行Davinci Resolve。(不要给Intel GPU那么做 - OpenCL驱动不支持, 尽管现在能用).。如果配置良好，它将会输出以下内容： 
    
    All seems good. You should be able to run DaVinci Resolve successfully.
    
###  BlackMagic采集卡

如果使用DeckLink、UltraStudio或Intensity卡进行视频采集和播放，请使用[decklink](<https://aur.archlinux.org/packages/decklink/>)AUR包安装Blackmagic Desktop Video Software。 

###  手动安装

自 19.1.3-2 版本起，开箱即用 AUR 包已无法正常工作。相反，可以克隆该软件包（把 davinci-resolve 改成你想要的版本，比如 davinci-resolve-studio）。 
    
    git clone <https://aur.archlinux.org/davinci-resolve.git>
    
从[BlackMagic的支持网站](<http://www.blackmagicdesign.com/support/>)下载你需要的Linux软件包。把压缩包放进克隆仓库里，放在其他文件（比如 PKGBUILD）旁边，并在文件末尾记下版本（比如 20.0.1）。另外，在下载的压缩包上运行`sha256sum`，记下输出。接下来编辑PKGBUILD：把pkgver 改成你的版本，把第一个 sha256sum 改成你的版本，另一个保持原样。执行`makepkg -i`，你就可以开始了。 

##  提示与技巧

###  使用ffmpeg编码插件

安装[davinci-ffmpeg-encoder-plugin](<https://aur.archlinux.org/packages/davinci-ffmpeg-encoder-plugin/>)AUR包。新的 ffmpeg 编码器适用于 AV1、HEVC 和 AVC（硬件使用 SVT-AV1、x265、x264 软件和 NVAPI）将通过“交付”标签页中的选项提供。请注意，编码器插件仅在Studio版本中提供。 

###  减少安装时间

由于二进制数据相当大，Davinci Resolve 包的压缩需要相当长的时间。你可以指示 makepkg 使用[另一种压缩算法](<https://wiki.archlinux.org/title/Makepkg#Use_other_compression_algorithms>)，在这种情况下完全禁用压缩，极大加快了整个过程。 
    
    PKGEXT='.pkg.tar'
    
###  使用便携版软件

如果因为软件包太大、需要切换多个版本等原因不想在系统中安装Davinci Resolve，可以把需要版本的安装包解压到想要解压的目录，然后直接在目录里运行opt/resolve/bin/resolve。 

###  使用自动化脚本

Davinci Resolve支持脚本。免费版只支持从软件内部启动脚本，而Studio版本可以从外部调用脚本。在 首选项->系统->常规->使用外部脚本 中可以选择三个选项：无（只能从软件内部调用）、本地（允许从本地主机调用）和网络（允许从远程主机调用）。 

可以在 帮助 -> 文档 -> 开发者 中找到相关文档。 

###  重新映射键盘和鼠标滚轮以滚动和缩放

软件本身滚动和缩放的快捷键很奇怪： 

  * Shift + 滚轮 = 调整轨道高度
  * Ctrl + 滚轮 = 滚动时间线
  * Alt + 滚轮 = 缩放时间线
  * 滚轮 = 垂直滚动

在软件中无法重新映射这些快捷键，见[[2]](<https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=74515>)。 

一个代替方法 (在 X11 和 Wayland里) 是使用[evsieve](<https://wiki.archlinux.org/title/Input_remap_utilities#evsieve>)。 用以下命令将 `/dev/input/event3` 和 `/dev/input/event5` 替换为你的键盘和鼠标事件： 
    
    # evsieve --input /dev/input/event3 grab --input /dev/input/event5 grab \
        --hook   key:leftalt:1 toggle=alt:2 \
        --hook   key:leftalt:0 toggle=alt:1 \
        --hook   key:leftctrl:1 toggle=ctrl:2 \
        --hook   key:leftctrl:0 toggle=ctrl:1 \
        --toggle rel:wheel @alt-up @alt-down id=alt \
        --map    yield rel:wheel@alt-down key:leftalt:0 key:leftctrl:1 key:leftctrl:2 rel:wheel key:leftctrl:0 key:leftalt:1 \
        --toggle rel:wheel @ctrl-up @ctrl-down id=ctrl \
        --map    yield rel:wheel@ctrl-down key:leftctrl:0 key:leftalt:1 key:leftalt:2 rel:wheel key:leftalt:0 key:leftctrl:1 \
        --block  rel:wheel_hi_res \
        --print  @alt-down @alt-up @ctrl-down @ctrl-up \
        --output create-link=/dev/input/by-id/merged-virtual-KM name="merged virtual KM"
    
另一个替代方法 (在 X11 (和 Xwayland)里运行更糟，有时会跳过事件)对于此问题, 你可以使用[IMWheel](<https://wiki.archlinux.org/title/IMWheel>)工具。它只能为正则表达式描述的应用重新映射修饰符。 

使用以下配置: 
    
    ~/.imwheelrc
    
    "^resolve"
    
        # 用滚轮滚动
        None, Up, Control_L|Button4
        None, Down, Control_L|Button5
    
        # 用Ctrl+滚轮实现缩放
        Control_L, Up,   Alt_L|Button4
        Control_L, Down, Alt_L|Button5
    
        # 用Alt+滚轮实现调节轨道高度
        Alt_L, Up,   Shift_L|Button4
        Alt_L, Down, Shift_L|Button5

或使用以下配置： 
    
    ~/.imwheelrc
    
    "^resolve"
    
         # 用滚轮缩放
         None, Up,   Alt_L|Button4
         None, Down, Alt_L|Button5
    
         # Shitf+滚轮实现滚动
         Shift_L, Up, Control_L|Button4
         Shift_L, Down, Control_L|Button5

###  在完全退出前防止提示返回

当你退出应用程序时，终端提示会返回给你，但终端突然被“套接字断开”的消息污染。为防止这种情况，主进程的输出通过 `cat`管道。参见[此处](<https://unix.stackexchange.com/a/698155>)的解释 

##  疑难解答

###  日志

DaVinci Resolve每次启动时都会在`~/.local/share/DaVinciResolve/logs/ResolveDebug.txt`创建日志文件。如果出现问题，可以检查此日志以获取相关信息。 

###  窗口没有标题栏

KDE可以用窗口规则强制开启标题栏，见[[3]](<https://forum.blackmagicdesign.com/viewtopic.php?=21&t=56878&p=456990#p456990>)。 

你可以手动创建描述所需窗口规则的文件： 
    
    DaVinci_Resolve_main_window_always_with_titlebar_and_frame.kwinrule
    
    [DaVinci Resolve main window always with titlebar and frame]
    Description=DaVinci Resolve main window always with titlebar and frame
    clientmachinematch=0
    noborder=false
    noborderrule=2
    titlematch=0
    types=1
    wmclass=resolve
    wmclasscomplete=false
    wmclassmatch=1

然后在 _系统设置 > 窗口管理 > 窗口规则_中导入此文件。 

###  MP4, H.264, H.265 and AAC 支持

DaVinci Resolve 免费版不支持 MP4 容器类型其实是个误解。更准确地说，DaVinci Resolve 免费版不支持解码或编码 H.264 和 H.265 视频，无论容器类型如何。 

例如，包含 AV1 视频流和 MP3 或 PCM 音频流的 MP4，可以被DaVinci Resolve 免费版解码。 

DaVinci Resolve 免费版和 Studio 版本均不支持 AAC 音频流的解码或编码。 

MP4 H.264 H.265 及 AAC 支持表  版本 | MP4 | H.264 | H.265 | AAC | 测试版 | 注释   
---|---|---|---|---|---|---  
免费版  | 是 | 否 | 否 | 否 | 18.6.6-2 | MP4 只要使用支持的编解码器（例如：AV1 和 PCM），就支持 MP4。   
Studio  | 是 | 是 | 是 | 否 | 18.6.6-2 |   
  
####  DaVinci Resolve 免费版解决方案

如果你的 MP4 视频是 H.264 或 H.265，音频是 AAC，你需要把视频和音频都转码成支持的编码。 
    
    $ ffmpeg -i input.mp4 -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a copy output.mov
    
如果你的 MP4 视频是 AV1，但音频是 AAC，只需将音频转码成支持的编解码器： 
    
    $ ffmpeg -i input.mp4 -c:v dnxhd -profile:v dnxhr_hq -pix_fmt yuv422p -c:a alac output.mov
    
If your MP4's video is AV1, but the audio is AAC, transcode just the audio to a supported codec: 
    
    $ ffmpeg -i input.mp4 -c:v copy -c:a pcm_s32le output.mp4
    
如果你的空间有限，你可以用这个选项（仍然会增加4.5%的文件体积）──但请记住，这是一种有损格式，所以你在后续阶段可能会出现压缩伪影——比如由于色彩校正——**从而丢失你的作品** ： 
    
    $ ffmpeg -i input.mp4 -c:v mpeg4 -q:v 2 -c:a alac output.mp4
    
你也可以用 alac 编解码器在 OBS 里做初次录音，然后用"-c：a copy"作为 ffmpeg 参数复制音频，避免再次编码。 

可以使用[incron](</wzh/index.php?title=Incron&action=edit&redlink=1> "Incron（页面不存在）")自动转换指定文件夹里出现的文件，见[此文章](<https://passthroughpo.st/painless-linux-video-production-part-3-organization-and-workflow/#:~:text=Auto%2DTranscode%20Your%20Footage>)中的设置案例。也可以编写脚本以实现此效果，更多信息见[另见部分](<#%E5%8F%A6%E8%A7%81>)。 

####  DR Studio的解决方案

尽管Studio 支持 H.264 和 H.265 视频，但不支持 AAC 音频。你可以将不支持的 AAC 格式音频转码成支持的无损格式，而无需破坏性地重新压缩视频，也不必将音频与视频分离。 

In [#另见](<#%E5%8F%A6%E8%A7%81>) 部分, 注意一个链接指向一个包含官方支持的编码格式列表的 PDF 文件。 

将音频转码为 **苹果无损音频编解码器** (`-c:a alac`). 如果你喜欢用 MOV 容器，这是个不错的选择。 
    
    $ ffmpeg -i input.mp4 -c:v copy -c:a alac output.mov
    
FLAC 相比 ALAC 在压缩上仅有小优势。要转码成 FLAC，你需要使用 MKV 容器。 
    
    $ ffmpeg -i input.mp4 -c:v copy -c:a flac -compression_level 12 output.mkv
    
用 PCM 可能没什么真正的优势，除了 MP4、MOV 和 MKV 容器都支持 PCM，如果你在意的话。 
    
    $ ffmpeg -i input.mp4 -c:v copy -c:a pcm_s32le output.mov
    
###  高分辨率支持

为了实现与高分辨率显示器的兼容性，请相应设置以下 [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")：[[4]](<https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=84614&p=469009&hilit=hidpi#wrapper>)
    
     QT_DEVICE_PIXEL_RATIO=2
    
     QT_AUTO_SCREEN_SCALE_FACTOR=true
    
你可以在设置中更改 UI 缩放：偏好设置（ctrl + ，）>用户标签>UI 设置>UI 显示缩放。 

###  关于Wine版本

因为有些插件能用于Windows而无法用于Linux版DR，而且Linux有MP4格式问题，所以可能有人想用Wine运行DR。但尽管Wine 6.5[支持了](<https://www.phoronix.com/scan.php?page=news_item&px=Wine-6.5-Released>)DR[所需](<https://www.newsshooter.com/2020/11/13/blackmagic-design-davinci-resolve-17-1-released/>)的OpenCL 1.2，还是无法用Wine启动DR。 

测试结果[在此](<https://appdb.winehq.org/objectManager.php?sClass=application&iId=17141>)。在DR 17.4.1中，DR无法看到可用的GPU列表（wine 6.21）。可能需要一些技巧让 Wine 能为应用程序展示 GPU。在 dr 18.5b1 和 wine 的 8.7-1 中，我会在[这里](<https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/158#issuecomment-1529782323>)提交 rocm 错误（5.4.3-1）。 

###  OpenCL版本错误

如果应用程序根本无法启动，即使显示安装程序并成功“巡回”(tour)，你的 OpenCL 版本可能与 NVIDIA 驱动不匹配。如果你安装了 nvidia-440xx，记得也安装 opencl-nvidia-440xx。错误信息可能如下： 
    
    ~/.local/share/DaVinciResolve/logs/LogArchive/ResolveDebug_C1.txt
    
    ...
    OpenCL error -1001: 'Unspecified Error', GPUPropertiesUtilUnix.cpp:338
    ...

###  再次显示初始界面

在尝试安装驱动时，可能需要从能检查系统和显卡的初始界面开始，你可以在备份后使用以下命令删除配置文件： 
    
    rm -r $HOME/.local/share/DaVinciResolve/configs
    
###  找不到全屏预览功能

仅Studio版有此功能，可以在菜单的 _Workspace > Video Clean Feed_ 中找到。 

###  视频预览时没有声音

达芬奇直接与 ALSA 进行连接， 所以如果你用 [pulseaudio](<https://wiki.archlinux.org/title/PulseAudio>) 你需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pulseaudio-alsa](<https://archlinux.org/packages/?name=pulseaudio-alsa>)包 或[pipewire-alsa](<https://archlinux.org/packages/?name=pipewire-alsa>)包. 或者你可以在`/etc/` 创建`asound.conf` 内容如下: 
    
    /etc/asound.conf
    
    pcm.!default pulse
    ctl.!default pulse

###  在intel/nvidia混合显卡上出现Error Code: 999

“GPU 因错误未能进行图像处理。错误代码：999。” 

如果 NVIDIA GPU 在按需模式下使用，你必须明确启用以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量"): 
    
    __NV_PRIME_RENDER_OFFLOAD=1
     __GLX_VENDOR_LIBRARY_NAME=nvidia
    
###  与libcrypto.so.1.0.0有关的静默崩溃

达芬奇 Resolve 无法以图形模式启动。在控制台中，会抛出以下错误： 
    
    $ /opt/resolve/bin/resolve 
    
    bin/resolve: error while loading shared libraries: libcrypt.so.1: cannot open shared object file: No such file or directory
    
你需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [libxcrypt-compat](<https://archlinux.org/packages/?name=libxcrypt-compat>)包. 

###  缺少工作流程集成菜单

在 Windows 和 Mac OS 的 DR Studio 中，有一个 Workspace -> 工作流集成菜单。工作流集成插件用 JavaScript（电子应用）编写。正如文档中所述（你可以在帮助 -> 文档 -> 开发者中找到），Linux 目前不被支持（在 17.4.3 中已确认）。他们说 Linux 支持集成脚本，这很可能是个错误，因为他们没有提供放置脚本的路径，菜单依然缺失（还是那个工作区->工作流集成）。 

###  找不到Python 3.6

前往 Workspace -> Console -> Py3 ，可能会弹出错误窗口 "Python 3.6 not found"。 

以下提供一种解决方案（来自[此问题](<https://video.stackexchange.com/questions/32458/davinci-resolve-python-3-6-not-found>)）： 
    
    env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.11
    sudo ln -s $HOME/.pyenv/versions/3.6.11/lib/python3.6 /usr/local/lib/python3.6
    sudo ln -s $HOME/.pyenv/versions/3.6.11/lib/libpython3.so /usr/local/lib/libpython3.6.so
    
在 DR 18 他们 [说](<https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=158557#:~:text=support%20for%20all%20modern%20and%20future%20python%203%20versions%20for%20scripting>)所有Python3版本都支持。 

###  杀死挂起进程

如果 DR 卡住了，按 ctrl + c（发送信号）时无法释放终端，且窗口不显示且无法再次打开 DR（显示已有其他实例运行），你仍然可以修复。 打开任务管理器（KDE的快捷键是ctrl + esc）, 然后搜索名为"GUI"的进程, 然后杀死它 (发送信号9)。现在可以正常打开DR了。 

###  用 Dolphin 代替 Qt File Picker

遗憾的是，DR 目前还不支持 XDG 桌面门户。功能请求请参见[[5]](<https://forum.blackmagicdesign.com/viewtopic.php?f=33&t=149142>) 。作为替代方法，你可以使用 Andrew Shark 的脚本[Import Media via Dolphin](<https://gitlab.com/AndrewShark/davinci-resolve-scripts/-/blob/main/import%20media%20via%20dolphin.py>). 

###  无法启动(onetbb/log4cxx)

切换到[onetbb](<https://archlinux.org/packages/?name=onetbb>)包 导致了死机，提示如下： 
    
    /opt/resolve/bin/resolve
    
    ...
    
    ActCCMessage Already in Table: Code= c005, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    
    ActCCMessage Already in Table: Code= c006, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    
    ActCCMessage Already in Table: Code= c007, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    
    ActCCMessage Already in Table: Code= 2282, Mode=  0, Level=  0, CmdKey= 8, Option= 0
    
    PnlMsgActionStringAdapter Already in Table: Code= 615e, Mode=  0, Level=  0, CmdKey= -1, Option= 0
    
    log4cxx: No appender could be found for logger (BtCommon).
    
    log4cxx: Please initialize the log4cxx system properly.
    
    ...

一个建议的替代方法是暂时把 `/opt/intel/oneapi/compiler/2023.0.0/linux/lib/libOpenCL.so`改到别的名字。 

参见[tbb 被onetbb 取代，resolve无法在Linux上启动](<https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=177985>) 的论坛帖子。 

###  无法启动(libpango/glib)

由于[Resolve处理库的方式](<https://unix.stackexchange.com/questions/743572/fedora-38-davinci-resolve-no-longer-opens-after-updating-from-fedora-37-to-38>)，如果系统库与 Resolve 发布的库差异过大，可能无法启动软件。 
    
    /opt/resolve/bin/resolve: symbol lookup error: /usr/lib64/libpango-1.0.so.0: undefined symbol: g_string_free_and_steal
    
为了绕过它，你可以强制 Resolve 使用系统版本： 
    
    $ LD_PRELOAD="/usr/lib64/libglib-2.0.so" /opt/resolve/bin/resolve
    
Resolve 第一次尝试可能无法启动，但后续尝试时会正常。 

这可能导致新的错误： 
    
    /opt/resolve/bin/resolve: symbol lookup error: /usr/lib/libgdk_pixbuf-2.0.so.0: undefined symbol: g_task_set_static_name
    
截至 2024-05-23，该“g_task_set_static_name”错误的修复方法如下([Arch论坛里的解决方案](<https://bbs.archlinux.org/viewtopic.php?id=295687>)): 
    
    $ LD_PRELOAD="/usr/lib/libgio-2.0.so /usr/lib/libgmodule-2.0.so" /opt/resolve/bin/resolve
    
另一个替代方法是从 Resolve 目录中移除几个库。这样 Resolve 就会被迫使用系统库，而不是随它打包的那些。另请参见 AUR 关于包和 PKGBUILD 本身的评以了解更多关于此技巧的信息。 
    
    /opt/resolve/libs/libglib-2.0.so*
    /opt/resolve/libs/libgio-2.0.so*
    /opt/resolve/libs/libgmodule-2.0.so*
    
###  无法启动(Wayland)

在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 会话中，环境变量 QT_QPA_PLATFORM=wayland 可能已经设置为允许其他 QT 程序启动支持 Wayland 的程序。然而，达芬奇 Resolve 将因以下错误无法启动： 
    
    qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
    
DaVinci Resolve 在启动时可以强制使用 [X11](<../zh-cn/Xorg.html> "X11")： 
    
    QT_QPA_PLATFORM=xcb /opt/resolve/bin/resolve
    
###  启动时“成功退出”

达芬奇 Resolve 可能无法启动，但又从未异常退出（退出代码 0），且无法生成日志文件。`/opt/resolve/bin/resolve` 的标准输出大致如下： 
    
    ActCCMessage Already in Table: Code= c005, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    ActCCMessage Already in Table: Code= c006, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    ActCCMessage Already in Table: Code= c007, Mode= 13, Level=  1, CmdKey= -1, Option= 0
    ActCCMessage Already in Table: Code= 2282, Mode=  0, Level=  0, CmdKey= 8, Option= 0
    log4cxx: No appender could be found for logger (BtCommon).
    log4cxx: Please initialize the log4cxx system properly.
    
这种状态通常与锁文件有关。Resolve 使用锁文件中的 `/tmp` 来检查正在运行的实例。出于各种原因，如果上次 Resolve 没有正确退出，这个锁文件会一直存在，阻止任何新的 Resolve 实例启动。 

锁文件的命名方案是 `qtsingleapp-DaVinc-xxx-lockfile` xxx 是某种十六进制 ID。你可以手动移除这个锁文件，Resolve 应该会重新启动。 

###  无法下载额外内容

使用**额外内容下载管理器** 下载 AI 语音训练数据或其他添加内容时，所有下载都会立即失败，状态下载失败 。这是因为 Resolve 中[TLS 证书路径](<https://forum.blackmagicdesign.com/viewtopic.php?f=40&t=218788#p1141546%E7%A1%AC%E7%BC%96%E7%A0%81%E7%9A%84>) 。你可以手动添加符号链接，让内部下载器正常工作。 
    
    mkdir -p /etc/pki/
    ln -s /etc/ssl /etc/pki/tls
    
额外内容存储在 /opt/resolve/Extras/ 中，确保空间足够，且启动 Resolve 的账户拥有写入权限。 

###  无法激活许可证，请稍后再试

这个错误有时在全新安装或更新后首次激活达芬奇 Resolve Studio 时出现。通常可以通过执行: 
    
    sudo chmod -R 7777 /opt/resolve/.license/
    
否则如果你还保留着之前安装的.license 文件夹，复制过去也可以解决这个问题。 

###  已安装的字体在达芬奇 Resolve 中不会显示

DaVinci Resolve 的“Text”对象仅尝试加载安装在系统范围的 `/usr/share/fonts` 或 `/usr/local/share/fonts` 文件夹中的[字体](<../zh-cn/%E5%AD%97%E4%BD%93.html> "字体") 。然而，“Text+”对象（在 Fusion 中也用于文本）只加载来自 `/usr/share/fonts` 的字体。 

如果你找不到安装的字体，可以检查它是否安装在 `/usr/share/fonts`（系统范围字体），而不是 `/usr/local/share/fonts/`（系统范围字体）或 `~/.local/share/fonts`（用户字体）。可以在 `/usr/share/fonts` 内创建一个指向 `/usr/local/share/fonts` 的符号链接。但不建议这样做 ，因为该目录由 [pacman](<../zh-cn/Pacman.html> "Pacman")管理，可能导致与字体包冲突。 

###  在 Fusion 标签页点击按键时会崩溃

Fusion 似乎需要美国本地配置，添加它们并生成本地区域 [Locale#生成 locales](<../zh-cn/Locale.html#%E7%94%9F%E6%88%90_locales> "Locale")： 
    
    /etc/locale.gen
    
    ...
    en_US.UTF-8 UTF-8
    ...

###  仅支持在Fairlight播放

DaVinci Resolve 搭配 Radeon 6700 XT（可能也类似的显卡）似乎需要 [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR，且不支持 [rocm-opencl-runtime](<https://archlinux.org/packages/?name=rocm-opencl-runtime>)。 

###  使用 OpenCL-AMD 7.2 时，达芬奇 Resolve 无法启动（分离故障）

恢复到最后一个可用版本的 [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR
    
    git clone <https://aur.archlinux.org/opencl-amd.git>
    cd opencl-amd
    git checkout 42c9eb7
    makepkg -si
    
此外，你可以通过编辑你的 /etc/pacman.conf 文件来阻止该软件包更新： 
    
    IgnorePkg = opencl-amd
    
##  另见

  * 已通过测试的配置见Davinci Resolve论坛的[这条帖子](<https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=56878&p=456990#p456924>)。
  * Davinci Resolve 19编解码器的[支持列表PDF](<https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_19_Supported_Codec_List.pdf>)。
  * 

在[此处](<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>) 你可以查看 BMD 是否发布了新版本的文档,详见最新支持说明栏。此外，它列出了每个版本的新注释。 

  * [ResolveDevDoc](<https://resolvedevdoc.readthedocs.io/en/latest/>) ──非官方的脚本文档

。用 readthedocs 格式化，比原始 txt 文件更美观、更易搜索 

  * [pydavinci](<https://github.com/pedrolabonia/pydavinci>) ──一个重新设计的 Resolve 脚本 API
