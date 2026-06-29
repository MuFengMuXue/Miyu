相关文章

  * [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg")

**翻译状态：**

  * 本文（或部分内容）译自 [Open Broadcaster Software](<https://wiki.archlinux.org/title/Open_Broadcaster_Software> "arch:Open Broadcaster Software")，最近一次同步于 2022-11-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Open_Broadcaster_Software?diff=0&oldid=758095>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Open_Broadcaster_Software_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Open Broadcaster Software](<https://obsproject.com/>)（OBS）是一款开源的跨平台视频录制和直播应用程序。它提供一项容易上手和可扩展的工作流程，具有可定制的场景、音量混合器、转场、过滤器等功能。 

##  安装

可选择 [obs-studio](<https://archlinux.org/packages/?name=obs-studio>)包 或 [obs-studio-git](<https://aur.archlinux.org/packages/obs-studio-git/>)AUR 开发版本安装。 

提供其他功能的客户端也可以使用。 

  * [obs-studio-tytan652](<https://aur.archlinux.org/packages/obs-studio-tytan652/>)AUR
  * [obs-studio-browser](<https://aur.archlinux.org/packages/obs-studio-browser/>)AUR
  * [obs-vaapi](<https://aur.archlinux.org/packages/obs-vaapi/>)AUR

##  配置

为方便配置， _工具 > 自动配置向导_可以快速设置录制和直播功能。该向导根据你的硬件（如果设置流媒体，还包括网络连接）自动选择比特率、分辨率和编码器。 

###  硬件加速

硬件加速的编码和解码在性能、CPU/GPU 使用和质量方面是最好的。编码器可以在 _设置 > 输出 > 流媒体 > 编码器_中改变（可能要先将 _设置 > 输出 > 输出模式_为 _高级_ ）。如果没有检测到硬件编码器，请参阅[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")。 

###  录制输出

OBS 默认在用户的家目录中输出录像，视频文件名中带有空格，并选择相同的编码器用于流媒体。输出路径、文件大小、文件格式、文件名样式等可以在 _设置 > 输出 > 录制_中改变。 

###  热键

OBS 默认没有指定热键。所有的热键对在选择时以红色显示，可以使用相同的键来切换热键对的功能。 

###  虚拟摄像机输出

从26.1版开始，OBS 支持 Linux 虚拟摄像机输出。要使用它，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [v4l2loopback](</wzh/index.php?title=V4l2loopback&action=edit&redlink=1> "V4l2loopback（页面不存在）")，然后 OBS 中会出现 _启动虚拟摄像机_ 按钮。如果`v4l2loopback`包中的[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")尚未加载，OBS 会自动尝试加载它，并要求获得管理权限（使用 [pkexec(1)](<https://man.archlinux.org/man/pkexec.1>)）。 

### Wayland

由于 OBS 是一款 Qt 应用程序，请参见 [Wayland#Qt](<../zh-cn/Wayland.html#Qt> "Wayland") 以使其在 Wayland 下工作。OBS 从版本 28 开始[从 Qt5 更新到了 Qt6](<https://github.com/obsproject/obs-studio/discussions/6481>)，因此更新的版本需要安装 [qt6-wayland](<https://archlinux.org/packages/?name=qt6-wayland>)包。参见 [PipeWire#WebRTC_屏幕共享](<../zh-cn/PipeWire.html#WebRTC_%E5%B1%8F%E5%B9%95%E5%85%B1%E4%BA%AB> "PipeWire")以启用 Wayland 屏幕捕获。 

####  KDE中全局快捷键无法使用

在OBS中设置的全局快捷键只有在OBS处于焦点状态时才有效。作为解决方法，您可以通过OBS的WebSocket接口来控制它，该接口可以在OBS中启用，方法是转到 _工具 > WebSocket服务器设置_，然后选择 _启用WebSocket服务器_ 。 

**注意：**`obs-studio`仍然缺少WebSocket支持 [FS#76710](<https://bugs.archlinux.org/task/76710>)，但[Flatpak](<../zh-cn/Flatpak.html> "Flatpak")和一些AUR软件包具有此支持（例如[obs-studio-git](<https://aur.archlinux.org/packages/obs-studio-git/>)AUR）。

然后可以使用`[obsws-python](<https://github.com/aatikturk/obsws-python>)`或`[obs-websocket-py](<https://github.com/Elektordi/obs-websocket-py>)`（版本>=1.0）来控制WebSocket。可以使用[pip](</wzh/index.php?title=Pip&action=edit&redlink=1> "Pip（页面不存在）")安装其中任何一个。然后在 _系统设置 > 快捷键_中，您可以为`obsws-python`添加以下命令，以设置自定义快捷键以切换录制： 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 避免复杂的一行命令。（在[Talk:Open Broadcaster Software](<../zh-cn/Talk:Open_Broadcaster_Software.html>)讨论）
    
    python -c "import obsws_python;obsws_python.ReqClient(host='localhost',port=4455,password=**yourwebsocketpassword**).toggle_record()"
    
或者，如果您使用`obs-websocket-py`，则使用以下命令： 
    
    python -c "from obswebsocket import obsws,requests;c=obsws('localhost',4455,**yourwebsocketpassword**);c.connect();c.call(requests.ToggleRecord());c.disconnect()"
    
WebSocket密码和端口可以在 _WebSocket服务器设置 > 显示连接信息_中找到。 

如果您希望避免复杂的一行命令，请使用[recording-toggle.py](<https://gitlab.com/AndrewShark/obs-scripts/-/tree/main/obs-wayland-shortcuts>)脚本。 

##  提示和技巧

###  浏览器来源

[obs-browser](<https://github.com/obsproject/obs-browser>) 插件提供在画布中使用网页的功能，通常用于基于网络的覆盖。该网页可以交互，并像其他源类型一样工作。 

默认的 [obs-studio](<https://archlinux.org/packages/?name=obs-studio>)包 [不提供这个插件](<https://bugs.archlinux.org/task/66008>)，但可以通过其他客户端或插件包添加。 

  * [obs-studio-git](<https://aur.archlinux.org/packages/obs-studio-git/>)AUR 使用浏览器插件进行编译。

  * [obs-studio-tytan652](<https://aur.archlinux.org/packages/obs-studio-tytan652/>)AUR 是一款定制的客户端，提供浏览器插件以及浏览器停靠栏，还有其他改进。

###  通过 Vulkan/OpenGL 捕获

[obs-vkcapture](<https://github.com/nowrep/obs-vkcapture>) 插件增加通过直接连接到 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 或 [OpenGL](<../zh-cn/OpenGL.html> "OpenGL") 的功能，而不是使用通用的 [Xorg](<../zh-cn/Xorg.html> "Xorg") 或 [Wayland](<../zh-cn/Wayland.html> "Wayland") 窗口捕获 API。要使用它，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [obs-vkcapture](<https://aur.archlinux.org/packages/obs-vkcapture/>)AUR，以及 [lib32-obs-vkcapture](<https://aur.archlinux.org/packages/lib32-obs-vkcapture/>)AUR（如果捕获32位应用程序）。按照 GitHub 仓库中的说明，使用该插件设置 _游戏捕获_ 。 

###  使用 GStreamer 进行编码

[obs-gstreamer](<https://github.com/fzwoch/obs-gstreamer>) 项目提供： 

  * 使用 GStreamer 进行编码的编码器插件。
  * 使用 [GStreamer pipeline](<https://gstreamer.freedesktop.org/documentation/tutorials/basic/dynamic-pipelines.html>) 作为源、视频过滤器或音频过滤器的插件。这是个高级功能，提供给熟悉使用 GStreamer 的用户。

AMD GPU 用户报告说，通过 GStreamer 的 [VA-API](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "VA-API") 胜过 OBS 默认的 VA-API 视频编码能力。要使用 obs-gstreamer 进行编码，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [obs-gstreamer](<https://aur.archlinux.org/packages/obs-gstreamer/>)AUR 并将 OBS 的编码器改为 _GStreamer 编码器_ 。如果 OBS 在编码器方面出现错误，你可能需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gstreamer-vaapi](<https://archlinux.org/packages/?name=gstreamer-vaapi>)包。 

###  手动插件安装

可以将插件手动安装到 `~/.config/obs-studio/plugins/`. 目录结构如下: 
    
    ~/.config/obs-studio/plugins/plugin_name/bin/64-bit/plugin_name.so
    ~/.config/obs-studio/plugins/plugin_name/data/locale/en-US.ini
    
###  录制矩形区域

在 KDE 上，您可以用 [obs-rectangle-area-selector](<https://gitlab.com/AndrewShark/obs-scripts/-/tree/main/obs-rectangle-area-selector>) 脚本选择并录制一块矩形区域。 

##  疑难解答

###  QuickSync 提示 "Error creating a MFX session"

该错误会在没有安装正确的英特尔 QuickSync 驱动时发生。 
    
    [AVHWDeviceContext @ 0x6111a37c1040] Error creating a MFX session: -9.
    Device creation failed: -1313558101.
    
要使用 QuickSync，请为 Iron Lake (Gen5) 到 [Ice Lake (Gen10)](<https://en.wikipedia.org/wiki/Ice_Lake_\(microprocessor\)> "wikipedia:Ice Lake \(microprocessor\)") 的GPU 安装 [intel-media-sdk](<https://archlinux.org/packages/?name=intel-media-sdk>)包，对于 [Tiger Lake (Gen11)](<https://en.wikipedia.org/wiki/Tiger_Lake> "wikipedia:Tiger Lake") 及更新的 GPU，请安装 [vpl-gpu-rt](<https://archlinux.org/packages/?name=vpl-gpu-rt>)包。 

关于更多信息，请参阅 [FFmpeg#Intel QuickSync (QSV)](<../zh-cn/FFmpeg.html#Intel_QuickSync_\(QSV\)> "FFmpeg")。 

##  参见

  * [OBS Wiki](<https://obsproject.com/wiki/Home>)
  * [修复 Arch Linux 缺失的 OBS 功能](<https://www.youtube.com/watch?v=IZjTXVKYm2Q>)
