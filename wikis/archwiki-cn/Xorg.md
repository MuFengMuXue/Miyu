**翻译状态：**

  * 本文（或部分内容）译自 [Xorg](<https://wiki.archlinux.org/title/Xorg> "arch:Xorg")，最近一次同步于 2025-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xorg?diff=0&oldid=831592>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xorg_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Autostarting](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting")
  * [光标主题](<../zh-cn/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98.html> "光标主题")
  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [字体配置](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html> "字体配置")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [XDMCP](</wzh/index.php?title=XDMCP&action=edit&redlink=1> "XDMCP（页面不存在）")
  * [xinit](<../zh-cn/Xinit.html> "Xinit")
  * [xrandr](<../zh-cn/Xrandr.html> "Xrandr")

[X.Org 服务器](<https://en.wikipedia.org/wiki/X.Org_Server> "wikipedia:X.Org Server")——通常简称为 **X** ——是 [X.Org 基金会](<https://en.wikipedia.org/wiki/X.Org_Foundation> "wikipedia:X.Org Foundation")实现的 [X 窗口系统](<https://en.wikipedia.org/wiki/X_Window_System> "wikipedia:X Window System") (**X11**) 显示服务器，它是 Linux 用户中最流行的显示服务器。它的普及使其成为图形用户界面应用程序的必备条件，因此大多数发行版都广泛采用了它。 

有关替代和潜在继任者，参见 [Wayland](<../zh-cn/Wayland.html> "Wayland")。 

##  安装

Xorg 可以通过安装 [xorg-server](<https://archlinux.org/packages/?name=xorg-server>)包 包来安装。 

此外，[xorg-apps](<https://archlinux.org/groups/x86_64/xorg-apps/>)包组 组中的一些软件包对于某些特定的配置任务是必要的。它们会在相关部分中指出。 

软件包组 [xorg](<https://archlinux.org/groups/x86_64/xorg/>)包组 包含了 Xorg 服务器、[xorg-apps](<https://archlinux.org/groups/x86_64/xorg-apps/>)包组 中的软件包以及字体。 

###  驱动安装

Linux 内核包含了开源的视频驱动，支持硬件加速。然而，[OpenGL](<../zh-cn/OpenGL.html> "OpenGL")、[Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 和 X11 的 2D 加速还需要用户空间工具。 

首先，识别显卡（ _Subsystem_ 输出显示具体型号）： 
    
    $ lspci -v -nn -d ::03xx
    
**提示：**`::03` 在这里表示 "[显示控制器](<https://admin.pci-ids.ucw.cz/read/PD/03>) PCI 设备类"，而 `xx` 代表 "该类的任何子类"。

然后，安装适当的驱动。您可以在包数据库中搜索完整的开源 [Device Dependent X (DDX)](<https://dri.freedesktop.org/wiki/DDX/>) 驱动列表： 
    
    $ pacman -Ss xf86-video
    
然而，特定硬件的 DDX 如今可以看作是遗留方案。[xorg-server](<https://archlinux.org/packages/?name=xorg-server>)包 中有一个通用的 [modesetting(4)](<https://man.archlinux.org/man/modesetting.4>) DDX 驱动，它使用[内核级显示模式设置（KMS）](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")并且在现代硬件上工作得很好。这个 modesetting DDX 驱动使用 [Glamor](<https://www.freedesktop.org/wiki/Software/Glamor/>)[[1]](<https://gitlab.freedesktop.org/xorg/xserver/-/tree/server-21.1-branch/glamor>) 来提供 2D 加速，而 Glamor 需要使用 OpenGL。 

如果您想要安装另一个 DDX 驱动，请注意 Xorg 会自动搜索已安装的驱动： 

  * 如果无法找到设备在下表中列出的驱动，会首先检查是否安装了不支持 2D 和 3D 加速的 _fbdev_ ([xf86-video-fbdev](<https://archlinux.org/packages/?name=xf86-video-fbdev>)包).
  * 如果依然没有找到，会搜索 _vesa_ ([xf86-video-vesa](<https://archlinux.org/packages/?name=xf86-video-vesa>)包)，这是一个支持大部分显卡的通用驱动，不提供任何 2D 和 3D 加速功能。
  * 如果没有找到 _vesa_ ，Xorg 会回退到 [modesetting(4)](<https://man.archlinux.org/man/modesetting.4>) DDX 驱动.

为了充分发挥显卡性能，请按下表安装驱动程序。推荐先使用开源驱动，这些驱动出问题的可能性较小。 

厂商  | 类型  | 文档  | DRM 驱动  | OpenGL  | OpenGL ([multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib"))  | Vulkan  | Vulkan ([multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib"))  | DDX 驱动   
---|---|---|---|---|---|---|---|---  
AMD (原 ATI)  | 开源  |  [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") | 包含在 [Linux](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核") 当中  |  [mesa](<https://archlinux.org/packages/?name=mesa>)包[[1]](<#cite_note-mesa-1>) |  [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包[[1]](<#cite_note-mesa-1>) |  [vulkan-radeon](<https://archlinux.org/packages/?name=vulkan-radeon>)包 |  [lib32-vulkan-radeon](<https://archlinux.org/packages/?name=lib32-vulkan-radeon>)包 |  [xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包  
[ATI](<../zh-cn/ATI.html> "ATI") | 无  |  [xf86-video-ati](<https://archlinux.org/packages/?name=xf86-video-ati>)包  
闭源  |  [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO") |  [amdgpu-pro-oglp](<https://aur.archlinux.org/packages/amdgpu-pro-oglp/>)AUR[[2]](<#cite_note-amdgpu-pro-2>) |  [lib32-amdgpu-pro-oglp](<https://aur.archlinux.org/packages/lib32-amdgpu-pro-oglp/>)AUR[[2]](<#cite_note-amdgpu-pro-2>) |  [vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/vulkan-amdgpu-pro/>)AUR[[2]](<#cite_note-amdgpu-pro-2>) |  [lib32-vulkan-amdgpu-pro](<https://aur.archlinux.org/packages/lib32-vulkan-amdgpu-pro/>)AUR[[2]](<#cite_note-amdgpu-pro-2>) |  [xf86-video-amdgpu](<https://archlinux.org/packages/?name=xf86-video-amdgpu>)包  
Intel  | 开源  |  [Intel graphics](<../zh-cn/Intel_graphics.html> "Intel graphics") |  [mesa](<https://archlinux.org/packages/?name=mesa>)包[[1]](<#cite_note-mesa-1>) |  [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包[[1]](<#cite_note-mesa-1>) |  [vulkan-intel](<https://archlinux.org/packages/?name=vulkan-intel>)包 |  [lib32-vulkan-intel](<https://archlinux.org/packages/?name=lib32-vulkan-intel>)包 |  [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包[[3]](<#cite_note-intel-3>)  
NVIDIA  | 开源  |  [Nouveau](<../zh-cn/Nouveau.html> "Nouveau")[[4]](<#cite_note-nvidia-4>) |  [mesa](<https://archlinux.org/packages/?name=mesa>)包[[1]](<#cite_note-mesa-1>) |  [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包[[1]](<#cite_note-mesa-1>) |  [vulkan-nouveau](<https://archlinux.org/packages/?name=vulkan-nouveau>)包 |  [lib32-vulkan-nouveau](<https://archlinux.org/packages/?name=lib32-vulkan-nouveau>)包 |  [xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包  
闭源  |  [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")[[4]](<#cite_note-nvidia-4>) |  [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 |  [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 |  [lib32-nvidia-utils](<https://archlinux.org/packages/?name=lib32-nvidia-utils>)包 |  [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 |  [lib32-nvidia-utils](<https://archlinux.org/packages/?name=lib32-nvidia-utils>)包 |  [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包  
[nvidia-580xx-dkms](<https://aur.archlinux.org/packages/nvidia-580xx-dkms/>)AUR |  [nvidia-580xx-utils](<https://aur.archlinux.org/packages/nvidia-580xx-utils/>)AUR |  [lib32-nvidia-580xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-580xx-utils/>)AUR |  [nvidia-580xx-utils](<https://aur.archlinux.org/packages/nvidia-580xx-utils/>)AUR |  [lib32-nvidia-580xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-580xx-utils/>)AUR |  [nvidia-580xx-utils](<https://aur.archlinux.org/packages/nvidia-580xx-utils/>)AUR  
[nvidia-535xx-dkms](<https://aur.archlinux.org/packages/nvidia-535xx-dkms/>)AUR |  [nvidia-535xx-utils](<https://aur.archlinux.org/packages/nvidia-535xx-utils/>)AUR |  [lib32-nvidia-535xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-535xx-utils/>)AUR |  [nvidia-535xx-utils](<https://aur.archlinux.org/packages/nvidia-535xx-utils/>)AUR |  [lib32-nvidia-535xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-535xx-utils/>)AUR |  [nvidia-535xx-utils](<https://aur.archlinux.org/packages/nvidia-535xx-utils/>)AUR  
[nvidia-470xx-dkms](<https://aur.archlinux.org/packages/nvidia-470xx-dkms/>)AUR |  [nvidia-470xx-utils](<https://aur.archlinux.org/packages/nvidia-470xx-utils/>)AUR |  [lib32-nvidia-470xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-470xx-utils/>)AUR |  [nvidia-470xx-utils](<https://aur.archlinux.org/packages/nvidia-470xx-utils/>)AUR |  [lib32-nvidia-470xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-470xx-utils/>)AUR |  [nvidia-470xx-utils](<https://aur.archlinux.org/packages/nvidia-470xx-utils/>)AUR  
[nvidia-390xx-dkms](<https://aur.archlinux.org/packages/nvidia-390xx-dkms/>)AUR |  [nvidia-390xx-utils](<https://aur.archlinux.org/packages/nvidia-390xx-utils/>)AUR |  [lib32-nvidia-390xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-390xx-utils/>)AUR |  [nvidia-390xx-utils](<https://aur.archlinux.org/packages/nvidia-390xx-utils/>)AUR |  [lib32-nvidia-390xx-utils](<https://aur.archlinux.org/packages/lib32-nvidia-390xx-utils/>)AUR |  [nvidia-390xx-utils](<https://aur.archlinux.org/packages/nvidia-390xx-utils/>)AUR  
  
  1. ↑ [1.0](<#cite_ref-mesa_1-0>) [1.1](<#cite_ref-mesa_1-1>) [1.2](<#cite_ref-mesa_1-2>) [1.3](<#cite_ref-mesa_1-3>) [1.4](<#cite_ref-mesa_1-4>) [1.5](<#cite_ref-mesa_1-5>) 对旧硬件来说，[mesa-amber](<https://archlinux.org/packages/?name=mesa-amber>)包 / [lib32-mesa-amber](<https://archlinux.org/packages/?name=lib32-mesa-amber>)包 当中的经典 OpenGL 驱动（非 Gallium3D 驱动）也许会有用（Mesa 22.0 及更高版本不再支持经典非 Gallium3D 驱动），参阅 [OpenGL#安装](<../zh-cn/OpenGL.html#%E5%AE%89%E8%A3%85> "OpenGL")。
  2. ↑ [2.0](<#cite_ref-amdgpu-pro_2-0>) [2.1](<#cite_ref-amdgpu-pro_2-1>) [2.2](<#cite_ref-amdgpu-pro_2-2>) [2.3](<#cite_ref-amdgpu-pro_2-3>) 由于新版 AMDGPU PRO 驱动做出了非常大的更改，这些包已经进入停止维护阶段。因此我们不再建议您使用这些包。
  3. [↑](<#cite_ref-intel_3-0>) 对于第四代及更新的 Intel 显卡，推荐使用 _modesetting_ DDX 驱动。参阅：[Intel 图形处理器#安装](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html#%E5%AE%89%E8%A3%85> "Intel 图形处理器")。
  4. ↑ [4.0](<#cite_ref-nvidia_4-0>) [4.1](<#cite_ref-nvidia_4-1>) 对于使用集成显卡和独立显卡的 NVIDIA Optimus 笔记本，请参考 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus")。

其它 DDX 驱动也都位于 [xorg-drivers](<https://archlinux.org/groups/x86_64/xorg-drivers/>)包组 软件包组中。 

没有闭源驱动，Xorg 也应正常工作。闭源驱动的典型用途是某些高级图形功能例如为游戏提供 3D 渲染加速。 

#### AMD

GPU 架构  | 开源驱动  | 非开源驱动   
---|---|---  
RDNA 及之后  |  [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") |  [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO")  
GCN 3 及之后   
GCN 1和2  |  [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU")[[1]](<#cite_note-amdgpu-5>) / [ATI](<../zh-cn/ATI.html> "ATI") | 不支持   
TeraScale 及之前  |  [ATI](<../zh-cn/ATI.html> "ATI") | 不支持   
  
  1. [↑](<#cite_ref-amdgpu_5-0>) AMD GPU 实验支持

##  运行

[Xorg(1)](<https://man.archlinux.org/man/Xorg.1>) 命令通常不直接运行。而是使用[显示管理器](<../zh-cn/Display_manager.html> "Display manager")或者[xinit](<../zh-cn/Xinit.html> "Xinit")来启动 X server。 

**提示：** 用户通常需要选择安装[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")或[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")以配合使用 X。

##  配置

**注意：** Arch 提供了位于 `/usr/share/X11/xorg.conf.d` 的默认配置文件。通常情况下，用户无需进行额外的配置与修改即可正常使用。

Xorg 使用名为 `xorg.conf` 的配置文件和后缀为 `.conf` 的文件作为它的初始设置。这些文件的位置的完整列表可以在[xorg.conf(5)](<https://man.archlinux.org/man/xorg.conf.5>)中找到，其中还附有全部可用选项的详尽解释。 

###  使用 .conf 文件

`/etc/X11/xorg.conf.d/` 目录保存主机特有设置，你可以创建自己的配置文件，需要以 `XX-` 开头(两个数字和一个连接符)并以 `.conf` 结尾。X 服务器启动时会解析这些文件，将其视为 `xorg.conf` 的一部分进行处理。如果配置之间有冲突，将会使用 _最后_ 被处理的文件。所以通用的设置应该放到前面。最后会解析 `xorg.conf` 文件。 

有关配置选项请参考 [Fedora wiki](<https://fedoraproject.org/wiki/Input_device_configuration#xorg.conf.d>)。 

###  使用 xorg.conf

可以通过 `/etc/X11/xorg.conf` 或 `/etc/xorg.conf` 配置 Xorg，用下面命令可以生成 `xorg.conf` 模板： 
    
    # Xorg :0 -configure
    
执行后会在 `/root/` 生成 `xorg.conf.new` 文件，然后你可以将它复制到 `/etc/X11/xorg.conf`。 

**提示：** 如果已经运行了 X 服务器，请使用不同的 display，例如 `Xorg :2 -configure`。

或者，显卡的专有驱动可能也提供了自动配置 Xorg 的工具，详情请参考 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 或 [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO")。 

**注意：** 配置文件关键字是大小写敏感的，"_" 字符会被忽略。配置，包括选项名也是大小写敏感的，会自动忽略空白和 "_"。

##  输入设备

对于输入设备，X 服务器默认使用 libinput 驱动 ([xf86-input-libinput](<https://archlinux.org/packages/?name=xf86-input-libinput>)包)，但 [xf86-input-evdev](<https://archlinux.org/packages/?name=xf86-input-evdev>)包 和相关驱动也可作为替代方案。[[2]](<https://archlinux.org/news/xorg-server-1191-is-now-in-extra/>)

[Udev](<../zh-cn/Udev.html> "Udev")，作为 systemd 的依赖项被提供，将会检测硬件。这两个驱动程序将作为几乎所有设备的热插拔输入驱动，它们的行为定义在位于 `/usr/share/X11/xorg.conf.d/` 的默认配置文件 `10-quirks.conf` 和 `40-libinput.conf` 中。 

在启动 X server 后，日志文件将会为每个设备显示发生了什么热插拔（注意最近的日志名称可能有所不同）： 
    
    $ grep -e "Using input driver " Xorg.0.log
    
如果两个驱动都不支持您的设备, 请从 [xorg-drivers](<https://archlinux.org/groups/x86_64/xorg-drivers/>)包组 组安装需要的驱动程序。如果你想要使用其他驱动，也可以这样做。 

想要干预热插拔，请参考 [#配置](<#%E9%85%8D%E7%BD%AE>)。 

更详细的信息，请参考 [libinput](<../zh-cn/Libinput.html> "Libinput") 文后的链接和 [Fedora wiki](<https://fedoraproject.org/wiki/Input_device_configuration>)。 

###  输入映射

参考[键盘按键#映射按键码](</wzh/index.php?title=Keyboard_input&action=edit&redlink=1> "Keyboard input（页面不存在）")。 

###  鼠标加速

[鼠标加速](<../zh-cn/Mouse_acceleration.html> "Mouse acceleration")。 

###  扩展鼠标按键

[鼠标按键](<../zh-cn/Mouse_buttons.html> "Mouse buttons")。 

###  触摸板

参考 [Libinput](<../zh-cn/Libinput.html> "Libinput") 或 [Touchpad_Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics")。 

###  触摸屏

[触摸屏](<../zh-cn/%E8%A7%A6%E6%91%B8%E5%B1%8F.html> "Touchscreen")。 

###  键盘设置

参考 [Xorg/键盘设置](</wzh/index.php?title=Xorg/%E9%94%AE%E7%9B%98%E8%AE%BE%E7%BD%AE&action=edit&redlink=1> "Xorg/键盘设置（页面不存在）")（英语：[Xorg/Keyboard_configuration](<https://wiki.archlinux.org/title/Xorg/Keyboard_configuration> "en:Xorg/Keyboard configuration")）。 

##  显示器设置

###  手动配置

**注意：**

  * 新的 Xorg 版本会自动配置显示器，无需额外配置。
  * 如果 Xorg 无法检测到任何显示器，或者没有自动配置，则可使用配置文件。一个常见的情况是使用无头系统时，系统在没有显示器的情况下启动并自动运行了 Xorg，要么是在[登录](<../zh-cn/Xinit.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X> "Xinit") 时从 [虚拟控制台](<../zh-cn/Getty.html#%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95%E5%88%B0%E8%99%9A%E6%8B%9F%E6%8E%A7%E5%88%B6%E5%8F%B0> "Getty")，或者是从一个[显示管理器](<../zh-cn/Display_manager.html> "Display manager")。

无头配置需要 [xf86-video-dummy](<https://archlinux.org/packages/?name=xf86-video-dummy>)包 驱动； 安装然后创建一个配置文件，例如： 
    
    /etc/X11/xorg.conf.d/10-headless.conf
    
    Section "Monitor"
            Identifier "dummy_monitor"
            HorizSync 28.0-80.0
            VertRefresh 48.0-75.0
            Modeline "1920x1080" 172.80 1920 2040 2248 2576 1080 1081 1084 1118
    EndSection
    
    Section "Device"
            Identifier "dummy_card"
            VideoRam 256000
            Driver "dummy"
    EndSection
    
    Section "Screen"
            Identifier "dummy_screen"
            Device "dummy_card"
            Monitor "dummy_monitor"
            SubSection "Display"
            EndSubSection
    EndSection
    
###  多显示器

参考主要文章[多显示器](<../zh-cn/%E5%A4%9A%E6%98%BE%E7%A4%BA%E5%99%A8.html> "多显示器")了解通用信息。 

####  多于一个显卡

你必须指定正确的驱动，输入你的显卡的 BusID（以十进制表示）。 
    
    Section "Device"
        Identifier             "Screen0"
        Driver                 "intel"
        BusID                  "PCI:0:2:0"
    EndSection
    
    Section "Device"
        Identifier             "Screen1"
        Driver                 "nouveau"
        BusID                  "PCI:1:0:0"
    EndSection
    
为了获取 BusID （十六进制）： 
    
    $ lspci -d ::03xx
    
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 630 (rev 04)
    01:00.0 3D controller: NVIDIA Corporation GP107M [GeForce GTX 1050 Mobile] (rev a1)
    
这个示例的BusID是 `0:2:0` 和 `1:0:0`。 

###  显示大小和 DPI

默认情况下，Xorg 自 [2009-01-30](<https://gitlab.freedesktop.org/xorg/xserver/-/commit/fff00df94d7ebd18a8e24537ec96073717375a3f>) 起始终将 DPI 设置为 96。版本 21.1 时有一个自动侦测的修改，但是被[回退](<https://gitlab.freedesktop.org/xorg/xserver/-/commit/35af1299e73483eaf93d913a960e1d1738bc7de6>)了。 

通过 `-dpi` 命令行选项可以设置 X 服务器的DPI。 

在需要精细细节（如字体渲染）的情况下，拥有正确的DPI尤其必要。此前，制造商试图为96 DPI（10.3英寸对角线显示器为800x600，13.2英寸显示器为1024x768）创建一个标准。如今，屏幕 DPI 各不相同，在水平和垂直方向上可能不相等。例如，1440x900的19英寸宽屏LCD的DPI可能为89x87。 

要查看您的显示大小和 DPI 是否正确： 
    
    $ xdpyinfo | grep -B2 resolution
    
如果明确知道显示器的物理尺寸规格，可以在Xorg配置文件中设置，这样就可以计算出合适的DPI。 
    
    Section "Monitor"
        Identifier             "Monitor0"
        DisplaySize             286 179    # 单位：毫米
    EndSection
    
如果你只想设置显示器的物理尺寸的规格，**不用** 从头到尾创建新的完整 xorg.conf 配置文件的话，可以在 `/etc/X11/xorg.conf.d/90-monitor.conf` 中设置屏幕的规格： 
    
    Section "Monitor"
        Identifier             "<default monitor>"
        DisplaySize            286 179    # In millimeters
    EndSection
    
**注意：** 如果你使用的是专有 NVIDIA 驱动程序，你可能需要把 `Option "UseEdidDpi" "FALSE"` 放在 `Device` 或 `Screen` 部分下才能生效。

如果你没有屏幕的物理宽度和高度的规格（现在大多数规格只按对角线尺寸列出）的话，可以使用显示器的原始分辨率（或长宽比）和对角线长度来计算水平和垂直的物理尺寸。 

用[勾股定理（毕达哥拉斯定理）](<https://en.wikipedia.org/wiki/Pythagorean_theorem> "wikipedia:Pythagorean theorem")计算一个对角线长度为13.3英寸、原始分辨率为1280x800（或长宽比为16:10）的屏幕： 
    
    $ echo 'scale=5;sqrt(1280^2+800^2)' | bc  # 1509.43698
    
这将给出像素的对角线长度，有了这个值，你就可以获得水平和垂直的物理长度（并将其转换成毫米）： 
    
    $ echo 'scale=5;(13.3/1509)*1280*25.4' | bc  # 286.43072
    $ echo 'scale=5;(13.3/1509)*800*25.4'  | bc  # 179.01920
    
**注意：** 这种计算适用于正方形的显示器。然而，很少有显示器可以压缩纵横比（例如16:10的纵横比分辨率为16:9的显示器）。如果是这种情况，您应该手动测量屏幕大小。

####  手动设置DPI

**注意：** 虽然你可以设置任何你喜欢的DPI，并且使用Qt和GTK的应用程序将相应地进行缩放，但还是建议将其设置为 **96** (100%, 无缩放), **120** (高出25%), **144** (高出50%), **168** (高出75%), **192** (高出100%) 等，以减少使用位图的GUI的缩放瑕疵。把它降低到96 dpi以下可能不会减少GUI的图形元素的大小，因为通常图标的最低dpi是96。

对于兼容RandR的驱动程序（比如开源的ATI驱动程序），你可以通过以下方式设置。 
    
    $ xrandr --dpi 144
    
**注意：** 更改并不会即时生效，你需要重新启动它们。

参阅 [Autostarting#Xorg](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#Xorg> "Autostarting") 使其永久化保存. 

#####  专有的 NVIDIA 驱动程序

您可以通过在`Device`或`Screen`部分下添加选项来手动设置DPI： 
    
    Option              "DPI" "96 x 96"
    
#####  手动DPI设置的注意事项

GTK 经常通过可选的 [X resource](</wzh/index.php?title=X_resource&action=edit&redlink=1> "X resource（页面不存在）") `Xft.dpi` 覆盖X服务器的DPI。 可以通过这个来检查当前的DPI： 
    
    $ xrdb -query | grep dpi
    
对于 3.16 版本之后的 GTK 库，当此变量未明确设置时，GTK 会将其设置为 96。要让 GTK 应用程序遵守X服务器 DPI设置，你可能需要将 Xft.dpi 显式设置为与服务器相同的值。 Xresource `Xft.dpi`是一些桌面环境在个人设置中强制设置DPI到一个特定值的方法。 其中包括 [KDE](<../zh-cn/KDE.html> "KDE") 和 [TDE](</wzh/index.php?title=TDE&action=edit&redlink=1> "TDE（页面不存在）")。 

### DPMS

[DPMS](<../zh-cn/Display_Power_Management_Signaling.html> "Display Power Management Signaling") (显示器电源管理信号) 是一种技术，可以在计算机不使用时，可以使用显示器的省电行为. 这将允许您的显示器在预定时间段后自动进入待机。 

##  合成

X 的合成扩展使窗口层次结构的整个子树呈现到屏幕外的缓冲区。应用程序可以获取缓冲区的内容并执行它们喜欢的任何操作。屏幕外的缓冲区可以自动合并到父窗口中，也可以被称为合成管理器的外部程序合并。要了解更多信息，参考[compositing window manager](<https://en.wikipedia.org/wiki/Compositing_window_manager> "wikipedia:Compositing window manager")。 

某些窗口管理器（例如 [Compiz](<../zh-cn/Compiz.html> "Compiz"), [Enlightenment](<../zh-cn/Enlightenment.html> "Enlightenment"), KWin, Marco, Metacity, Muffin, Mutter, [Xfwm](<../zh-cn/Xfwm.html> "Xfwm")）自己完成这些合成。对于其他窗口管理器，可以使用一个独立的合成管理器。 

###  合成管理器列举

  * **[Picom](<../zh-cn/Picom.html> "Picom")** — 支持阴影、高级模糊和渐变的轻量级合成管理器。

     <https://github.com/yshui/picom> || [picom](<https://archlinux.org/packages/?name=picom>)包

  * **[Xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr")** — 复合窗口效果管理器

     <https://gitlab.freedesktop.org/xorg/app/xcompmgr/> || [xcompmgr](<https://archlinux.org/packages/?name=xcompmgr>)包

  * **[Gamescope](<../zh-cn/Gamescope.html> "Gamescope")** — Valve 的微合成器，具有面向游戏的功能，如 FSR 上采样。从 steamos-compositor 分叉而来。

     <https://github.com/ValveSoftware/gamescope> || [gamescope](<https://archlinux.org/packages/?name=gamescope>)包

  * **steamos-compositor-plus** — Valve 的合成器，带有一些额外的调整和修复。

     <https://github.com/chimeraos/steamos-compositor-plus> || [steamos-compositor-plus](<https://aur.archlinux.org/packages/steamos-compositor-plus/>)AUR

##  技巧和技巧

###  自动化

这一节列出用于键盘、鼠标输入和窗口操作自动化的实用程序（例如移动、调整大小和层级）。 

工具 | 软件包 | 手册 | [keyboard input](</wzh/index.php?title=Keyboard_input&action=edit&redlink=1> "Keyboard input（页面不存在）") | 窗口操作 | 注   
---|---|---|---|---|---  
xautomation  | [xautomation](<https://archlinux.org/packages/?name=xautomation>)包 | [xte(1)](<https://man.archlinux.org/man/xte.1>) | 是 | 否 | 也包含 screen scraping tools。无法模拟 F13+.   
xdo  | [xdo](<https://archlinux.org/packages/?name=xdo>)包 | [xdo(1)](<https://man.archlinux.org/man/xdo.1>) | 否 | 是 | 用于执行基本窗口操作的轻量级X实用工具   
xdotool  | [xdotool](<https://archlinux.org/packages/?name=xdotool>)包 | [xdotool(1)](<https://man.archlinux.org/man/xdotool.1>) | 是 | 是 |  [充满 Bug](<https://github.com/jordansissel/xdotool/issues>) 且开发不活跃，比如说CLI解析错误。[[3]](<https://github.com/jordansissel/xdotool/issues/14#issuecomment-327968132>)[[4]](<https://github.com/jordansissel/xdotool/issues/71>)  
xvkbd  | [xvkbd](<https://aur.archlinux.org/packages/xvkbd/>)AUR | [xvkbd(1)](<http://t-sato.in.coocan.jp/xvkbd/#option>) | 是 | 否 | 面向 Xorg 的虚拟键盘，在发送字母时也有 `-text` 选项。   
AutoKey  |  [autokey-qt](<https://aur.archlinux.org/packages/autokey-qt/>)AUR [autokey-gtk](<https://aur.archlinux.org/packages/autokey-gtk/>)AUR | [文档](<https://github.com/autokey/autokey#documentation>) | 是 | 是 | 强大的宏和脚本工具，有Qt和GTK两种前端。   
  
也可以参考 [Clipboard#Tools](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html#Tools> "Clipboard") and [an overview of X automation tools](<https://venam.nixers.net/blog/unix/2019/01/07/win-automation.html>). 

###  嵌套 X 会话

在嵌套的 X 的会话中启动其他桌面环境： 
    
    $ /usr/bin/Xnest :1 -geometry 1024x768+0+0 -ac -name Windowmaker & wmaker -display :1
    
这会在你当前的 X 会话中启动一个1024 × 768大小的 Window Maker 会话。 

需要安装[xorg-server-xnest](<https://archlinux.org/packages/?name=xorg-server-xnest>)包。 

[Xephyr](<../zh-cn/Xephyr.html> "Xephyr") 是一个更新的方法。 

###  远程启动 GUI 程序

查看主条目：[X11转发](<../zh-cn/OpenSSH.html#X11_forwarding> "OpenSSH")。 

###  按需禁用和启用输入源

利用 _xinput_ 你可以您可以暂时禁用或启用输入源。这可能很有用，例如，在具有多个鼠标的系统上（如ThinkPad），可以只使用一个鼠标以避免不必要的点击。 

从[official repositories](<../zh-cn/Official_repositories.html> "Official repositories")[安装](<../zh-cn/Pacman.html> "Pacman") [xorg-xinput](<https://archlinux.org/packages/?name=xorg-xinput>)包。 

找到要禁用的设备的ID： 
    
    $ xinput
    
例如在Lenovo ThinkPad T500中，输出如下所示： 
    
    $ xinput
    
    ⎡ Virtual core pointer                          id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ TPPS/2 IBM TrackPoint                     id=11   [slave  pointer  (2)]
    ⎜   ↳ SynPS/2 Synaptics TouchPad                id=10   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                         id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Video Bus                                 id=7    [slave  keyboard (3)]
        ↳ Sleep Button                              id=8    [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=9    [slave  keyboard (3)]
        ↳ ThinkPad Extra Buttons                    id=12   [slave  keyboard (3)]
    
使用`xinput --disable _device_id_`禁用设备， _device_id_ 是你要禁用的设备的ID。在此示例中，我们将禁用ID为10的Synaptics触摸板： 
    
    $ xinput --disable 10
    
要重新启用该设备，只需发出相反的命令： 
    
    $ xinput --enable 10
    
###  持久禁用输入源

你可以使用配置片段来禁用特定的输入源： 
    
    /etc/X11/xorg.conf.d/30-disable-_device_.conf
    
    Section "InputClass"
           Identifier   "disable-_device_ "
           Driver       "_driver_name_ "
           MatchProduct "_device_name_ "
           Option       "Ignore" "True"
    EndSection
    
`_device_` 是一个任意名称，` _driver_name_` 是输入驱动程序的名称，例如 `libinput`。` _device_name_` 是实际用于匹配正确设备的内容。对于其他方法（例如 [libinput](<../zh-cn/Libinput.html> "Libinput") 的 `MatchIsTouchscreen`），请参阅输入驱动程序的文档。虽然此示例使用 libinput，但这是一个与驱动程序无关的方法，它只是阻止设备传播到驱动程序。 

###  使用热键结束应用程序

在热键上运行脚本： 
    
    #!/bin/sh
    windowFocus=$(xdotool getwindowfocus);
    pid=$(xprop -id "$windowFocus" | grep PID);
    kill -9 "$pid"
    
依赖：[xorg-xprop](<https://archlinux.org/packages/?name=xorg-xprop>)包，[xdotool](<https://archlinux.org/packages/?name=xdotool>)包

###  阻止 TTY 访问

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 为什么需要这么做呢？ (在 [Talk:Xorg](<../zh-cn/Talk:Xorg.html>) 中讨论)

要在X中阻止tty访问，请将以下内容添加到[xorg.conf](<#%E9%85%8D%E7%BD%AE>)： 
    
    Section "ServerFlags"
        Option "DontVTSwitch" "True"
    EndSection

###  防止用户结束 X

要防止用户在运行时被结束，请将以下内容添加到[xorg.conf](<#%E9%85%8D%E7%BD%AE>)： 
    
    Section "ServerFlags"
        Option "DontZap"      "True"
    EndSection

**注意：** The `Ctrl+Alt+Backspace` shortcut is not directly what triggers killing the X server, but the `Terminate_Server` action from the keyboard map. This is usually not set by default, see [Xorg/Keyboard configuration#Terminating Xorg with Ctrl+Alt+Backspace](</wzh/index.php?title=Xorg/Keyboard_configuration&action=edit&redlink=1> "Xorg/Keyboard configuration（页面不存在）").

###  可视化结束应用程序

当应用程序行为异常或卡住时，与其从终端使用 `kill` 或 `killall` 并查找进程 ID 或名称，不如使用 [xorg-xkill](<https://archlinux.org/packages/?name=xorg-xkill>)包 点击该应用程序以关闭其与 X 服务器的连接。许多现有应用程序确实会在与 X 服务器的连接关闭时中止，但有些应用程序可能会选择继续运行。 

###  没有 root 权限的 Xorg

Xorg 可以使用标准用户权限而不是 root 来运行（所谓的“rootless” Xorg）。这对于用 root 权限运行是很大的安全性提升。注意大多数显示管理器都不支持 rootless Xorg。 

你可以用 `ps -o user $(pgrep Xorg)` 来验证 Xorg 在以什么用户的身份运行。 

也可参考[Xorg.wrap(1)](<https://man.archlinux.org/man/Xorg.wrap.1>), [systemd-logind(8)](<https://man.archlinux.org/man/systemd-logind.8>), [Systemd/用户#Xorg_as_a_systemd_user_service](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#Xorg_as_a_systemd_user_service> "Systemd/用户"), [[5]](<https://fedoraproject.org/wiki/Changes/XorgWithoutRootRights>) 和 [FS#41257](<https://bugs.archlinux.org/task/41257>)。 

####  使用 xinitrc

要配置“rootless”的Xorg [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc"): 

  * 将startx作为当前登录shell的子进程运行；直接运行{ic | startx}}，不要使用{ic | exec startx}}
  * 确保 Xorg 使用已设置权限的虚拟终端，即通过 logind 通过 [.xserverrc](<../zh-cn/Xinit.html#xserverrc> "Xinit") 在 `$XDG_VTNR` 中传递。
  * 如果使用某些专有的驱动程序, [kernel mode setting](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting") [自动检测](<https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/hw/xfree86/xorg-wrapper.c#L222>)将失效. 在这种情况下, 必须在 `/etc/X11/Xwrapper.config` 中设置`needs_root_rights = no`。

####  使用 GDM

在使用[kernel mode setting](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting")时，Xorg将在没有root权限的情况下运行[GDM](<../zh-cn/GDM.html> "GDM")。 

####  重定向Xorg会话日志

当Xorg在没有root权限的情况下运行时，Xorg的日志将保存到`~/.local/share/xorg/Xorg.log`。但是，Xorg会话的stdout和stderr的输出并不会重定向到此日志文件，要重新启动重定向，请使用命令行选项`-keeptty`来启动Xorg,并将stdout和stderr输出重定向到一个文件： 
    
    startx -- -keeptty >~/.xorg.log 2>&1
    
或者，将`/etc/X11/xinit/xserverrc`复到`~/.xserverrc`并使用命令行选项`-keeptty`来启动Xorg。参阅[[6]](<https://bbs.archlinux.org/viewtopic.php?pid=1446402#p1446402>)。 

### Xorg as Root

如上所述，某些情况下系统会默认启用无root权限的Xorg。若您的配置属于此类情况，且需要以root身份运行Xorg，可通过配置Xorg.wrap(1[Xorg.warp(1)](<https://man.archlinux.org/man/Xorg.warp.1>))强制要求root权限： 

**警告：** 在 root下运行 Xorg 可能会引起安全问题。更多讨论参见 [#Rootless Xorg](<#Rootless_Xorg>) 。
    
    /etc/X11/Xwrapper.config
    
    needs_root_rights = yes

##  故障和修复

###  一般问题

如果你在使用Xorg中遇到问题，请查看位于 `/var/log/` 的日志，或者对于从 v1.16 起的没有 `root` 权限的 Xorg，日志文件位于 `~/.local/share/xorg/`。 [GDM](<../zh-cn/GDM.html> "GDM") 用户应当检查 [systemd journal](</wzh/index.php?title=Systemd_journal&action=edit&redlink=1> "Systemd journal（页面不存在）"). [[7]](<https://bbs.archlinux.org/viewtopic.php?id=184639>)

日志文件的格式为 `Xorg.n.log`， 其中 `n` 表示显示器编号。对于单用户、使用默认配置文件的机器，日志文件常常是 `Xorg.0.log`，其它情形可能会有区别。 想要找到正确的文件，可以考虑检查 X 服务器会话启动的时间戳以及它是从哪个控制台启动的。例如： 
    
    $ grep -e Log -e tty Xorg.0.log
    
    [    40.623] (==) Log file: "/home/archuser/.local/share/xorg/Xorg.0.log", Time: Thu Aug 28 12:36:44 2014
    [    40.704] (--) controlling tty is VT number 1, auto-enabling KeepTty

**提示：** 要使用人类可读的时间戳监控日志，可以将 [tail(1)](<https://man.archlinux.org/man/tail.1>) 的输出通过管道传递给 [ts(1)](<https://man.archlinux.org/man/ts.1>)（由 [moreutils](<https://archlinux.org/packages/?name=moreutils>)包 包提供）。这将仅在命令运行时为添加到日志中的行提供正确的时间戳。例如： 
    
    $ tail -f ~/.local/share/xorg/Xorg.0.log | ts
    
  * 在日志文件中寻找以 `(EE)` 开头的行，它代表错误，以及 `(WW)`，代表警告（也可能暗示着其他问题）。
  * 如果在你的`$HOME`目录下有一个 _空的_ `.xinitrc` 文件，删除或修改它以使 X 正确启动。如果你不这样做，X 会显示黑屏并不会在 `Xorg.0.log` 中输出任何错误。简单地删除它就可以使 X 以默认配置运行。
  * 如果你遇到黑屏，你仍可以尝试切换到不同的虚拟控制台 （例如 `Ctrl+Alt+F6`），然后不假思索地以 root 登录。你可以通过输入 `root` （然后按下 `Enter` ） 然后输入密码（同样地，输入后按下 `Enter` ）。

    你也可以尝试使用以下命令杀死 X server：
    
    # pkill -x X

    如果不行的话，直接重启：
    
    # reboot

  * 如果你有关于键盘，鼠标，触摸板等等的问题，参考 [Category:Input devices](<../zh-cn/Category:Input_devices.html> "Category:Input devices") 中具体的文章。
  * 最后，在[AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU"), [Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel")和[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")等文章中搜索常见问题。

###  黑屏，没有指定协议..，资源暂时不可用等问题

X在当前用户的主目录中创建配置和临时文件。确保主目录所在的分区上有可用的可用磁盘空间。然而，在这种情况下，X服务器不提供有关磁盘空间不足的更明显信息。 

###  Matrox显卡的DRI功能失效

如果你使用的是Matrox显卡，在升级到Xorg7后它的DRI功能失效，试着在xorg.conf的显卡设备设置段Device section中加入下面一行： 
    
    Option "OldDmaInit" "On"
    
###  无法运行在frambuffer模式下

如果X启动失败，日志中有以下信息： 
    
     (WW) Falling back to old probe method for fbdev
     (II) Loading sub module "fbdevhw"
     (II) LoadModule: "fbdevhw"
     (II) Loading /usr/lib/xorg/modules/linux//libfbdevhw.so
     (II) Module fbdevhw: vendor="X.Org Foundation"
            compiled for 1.6.1, module version = 0.0.2
            ABI class: X.Org Video Driver, version 5.0
     (II) FBDEV(1): using default device
      
     Fatal server error:
     Cannot run in framebuffer mode. Please specify busIDs        for all framebuffer devices
    
只需要卸载[xf86-video-fbdev](<https://archlinux.org/packages/?name=xf86-video-fbdev>)包就可以了。 

###  无法加载'(null)'字体

  * 一些程序无法运行，提示无法加载`(null)'字体.****

这些软件包可能需要一些额外的字体。某些程序只能使用位图字体。 目前有两种主要的位图字体包：[xorg-fonts-75dpi](<https://archlinux.org/packages/?name=xorg-fonts-75dpi>)包、[xorg-fonts-100dpi](<https://archlinux.org/packages/?name=xorg-fonts-100dpi>)包。选择其中一个就可以了。通过下面这个命令查看显示设置： 
    
    $ xdpyinfo | grep resolution
    
根据显示信息选择合适dpi的字体即可(用75 或 100 代替XX)： 
    
    # pacman -S xorg-fonts-XXdpi
    
###  修复：在出现GUI登录界面之前，不启动Xorg

如果Xorg设置为自动启动并且出于某些原因你不想让它出现在 登录/显示 管理器之前，有两种办法: 

  * 将启动目标修改为 rescue.target. 参阅 [systemd#Change default target to boot into](<../zh-cn/Systemd.html#Change_default_target_to_boot_into> "Systemd").
  * 如果 X 无法启动，而且 GRUB 超时时间设置成了 0,无法进 Grub 禁止 Xorg boot. 可以使用 Arch CD 启动，然后挂载配置文件所在分区，

    可以以root用户使用命令
    
    # fdisk -l
    
    来查看你的全部分区。通常你所要的那个是形如 `/dev/sda1` 这样的东东。然后，使用命令
    
    # mount /dev/sda1 /mnt
    
挂载该分区至 `/mnt`。 这样你的文件系统就挂载在了 `/mnt` 下。例如，可以删除 `gdm` 来阻止Xorg正常启动，或者做其他一些必需的改动。 

###  无法用"su"以root身份启动X客户端

如果你遇到"Client is not authorized to connect to server"，尝试将以下内容 
    
     session        optional        pam_xauth.so
    
加入到`/etc/pam.d/su`文件中。`pam_xauth` 就可以正常设置环境变量以及处理 `xauth` 密钥了。 

###  X 启动失败：键盘初始化失败

遇到“X failed to start : Keyboard initialization failed”。 如果您的硬盘已满，startx将失败。 `/var/log/Xorg.0.log` 的末尾会是： 
    
     (EE) Error compiling keymap (server-0)
     (EE) XKB: Could not compile keymap
     (EE) XKB: Failed to load keymap. Loading default keymap instead.
     (EE) Error compiling keymap (server-0)
     (EE) XKB: Could not compile keymap
     XKB: Failed to compile keymap
     Keyboard initialization failed. This could be a missing or incorrect setup of xkeyboard-config.
     Fatal server error:
     Failed to activate core devices.
     ...
    
在/分区上腾出一些可用空间，X才能启动。 

###  想看视频时屏幕总是绿色

你的颜色深度设置错误。例如它可能需要设置为24位却被设置成了16位。 

### SocketCreateListener error

如果 X 结束，伴随着错误信息 "SocketCreateListener() failed"，你可能需要删除位于 `/tmp/.X11-unix` 的 socket 文件。这有可能在你先前以 root 身份运行 Xorg （例如想要生成 `xorg.conf`）后发生。 

###  想要以 root 权限运行程序时出现 无效的 MIT-MAGIC-COOKIE-1 密钥

这个错误意味着只有当前用户有权访问 X server。解决办法是将访问权授予 root： 
    
    $ xhost +si:localuser:root
    
这条命令也可以将 X server 访问权授予其他用户。 

##  另请参阅

  * [Xplain](<https://magcius.github.io/xplain/article/>) \- X Window 系统的深入讲解
  * [Xorg(1)](<https://man.archlinux.org/man/Xorg.1>)
  * [Prepare for LPIC-1 exam 2 - topic 106.1: X11](<https://developer.ibm.com/tutorials/l-lpic1-106-1/>) \- briefly covers architecture, [#Configuration](<#Configuration>), [desktop environments](</wzh/index.php?title=Desktop_environments&action=edit&redlink=1> "Desktop environments（页面不存在）"), remote usage, [Wayland](<../zh-cn/Wayland.html> "Wayland").
  * [xorg.conf(5)](<https://man.archlinux.org/man/xorg.conf.5>)
  * [Gentoo:Xorg/Guide#Configuration](<https://wiki.gentoo.org/wiki/Xorg/Guide#Configuration> "gentoo:Xorg/Guide")
