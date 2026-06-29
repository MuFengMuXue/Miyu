**翻译状态：**

  * 本文（或部分内容）译自 [Virtual reality](<https://wiki.archlinux.org/title/Virtual_reality> "arch:Virtual reality")，最近一次同步于 2020-09-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Virtual_reality?diff=0&oldid=634309>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Virtual_reality_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[虚拟现实](<https://en.wikipedia.org/wiki/%E8%99%9A%E6%8B%9F%E7%8E%B0%E5%AE%9E> "wikipedia:虚拟现实")是使用各种外围设备，头戴式显示器或[CAVEs](<https://en.wikipedia.org/wiki/Cave_automatic_virtual_environment> "wikipedia:Cave automatic virtual environment")和跟踪器为用户模拟环境的一系列过程。虚拟显示技术不会从屏幕上向您显示静态视点，而是将您的视点相对于您站立的位置（在贴头或投影的表面上）进行渲染，以提供与您自己的眼睛观看视角相同的效果。 

许多虚拟现实的设备已经发布或即将发布，这为人们带来了不是那么昂贵，身临其境的虚拟现实环境。这些设备大多数都具有全部或部分Linux支持，并且许多具有[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")软件包。 

##  环境兼容列表

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Use [Template:Yes](<../zh-cn/Template:%E6%98%AF.html> "Template:Yes") and question marks.（在[Talk:虚拟现实(VR)](<../zh-cn/Talk:%E8%99%9A%E6%8B%9F%E7%8E%B0%E5%AE%9E\(VR\).html>)讨论）

**Legend:**

  * 绿色: 原生支持
  * 黄色: 通过工具集支持或部分支持
  * 红色: 不完整支持
  * 无色: 未知/未完成/计划支持

| Oculus Rift  | OSVR  | OpenVR  | Leap Motion  | Razer Hydra   
---|---|---|---|---|---  
Dolphin (从源仓库 fork 的 VR 版本)  |  |  | 部分完成  |  |   
Dolphin (官方 OSVR 支持)  | 通过 OSVR  |  |  | 通过 OSVR  | 通过 OSVR   
Minecrift (Minecraft VR)  |  | (计划) 通过 OSVR-SteamVR  | (计划)  | (计划) 通过 OSVR  |   
Janus VR  |  |  |  |  | 通过 OSVR   
Team Fortress 2  | 通过 OpenVR  | 通过 OSVR-SteamVR  | 不完整支持，随机修复状态  | 通过 OSVR  | 通过 OSVR   
Half Life 2  | 显示处于一只眼黑，一只眼无色的状态  | 通过 OSVR-SteamVR  | 显示处于一只眼黑，一只眼无色的状态  | 通过 OSVR  | 通过 OSVR   
VRUI VR 工具集和演示  |  |  |  |  |   
4089: The Ghost Within  | 通过 OpenVR  | 通过 OSVR-SteamVR  | 直到V社修复问题之前都不完善  | 通过 OSVR  | 通过 OSVR   
Games/Programs in Wine  | 在 OVRSDK 版本 <=0.5.0.0, 且 [oculus-wine-wrapper-git](<https://aur.archlinux.org/packages/oculus-wine-wrapper-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 和 [wine-unity3d-git](<https://aur.archlinux.org/packages/wine-unity3d-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]上支持  | 跟踪器工作完美。 但是在Unity演示没有Render Manager的工作时有问题，使用Render Manager的Unity演示会出现白屏或者黑屏。  |  |  |   
  
##  支持的设备和工具集

### OpenXR

OpenXR是一种开放的，不收费用的标准，用于访问虚拟现实以及增强现实的平台和设备。它由Khronos集团维护，并被大多数行业所采用，大多数运行时都支持OpenXR。 

### Monado

Monado是由Collabora开发的开源OpenXR运行时。它正在开发中，旨在提供支持大多数耳机的通用运行时。你可以在 <https://monado.freedesktop.org/> 上查看进度 

###  OpenVR / SteamVR

Valve致力于通过OpenVR创建用于VR开发的开放API。不幸的是，当API开放时，实际的默认实现（SteamVR）却没有进行开放。它提供了一个OpenXR标准的运行时。 

####  配置

安装 [Steam](<../zh-cn/Steam.html> "Steam"), 通过Steam里的下载按钮下载SteamVR。 

####  故障排除

#####  配置和启动错误

SteamVR / OpenVR创建一个配置目录〜/.openvr，该目录可能在不同的版本上出现配置错误。删除该目录，然后完全卸载/重新安装SteamVR可以解决。 

在某些配置下，访问Rift显然也很麻烦。一种替代方法是使用OSVR-SteamVR驱动程序和OSVR-Oculus-Rift插件。 

### OpenHMD

[OpenHMD](<http://www.openhmd.net/>) 目标是为沉浸式技术提供免费和开源的API和驱动程序，例如具有内置头部跟踪功能的头戴式显示器。目标是在便携式跨平台封装中实现尽可能多设备的支持。 

OpenHMD支持多种设备，例如Oculus Rift，HTC Vive，Sony PSVR，Deepoon E2等。 

可以从第三方获得 .NET，Java，Perl，Python和Rust的编程语言绑定。 

####  安装

安装 [openhmd-git](<https://aur.archlinux.org/packages/openhmd-git/>)AUR. 

####  SteamVR 支持

可以将OpenHMD与SteamVR一起使用。为此，您需要安装 [steamvr-openhmd-git](<https://aur.archlinux.org/packages/steamvr-openhmd-git/>)AUR 并创建符号链接，该链接指向SteamVR驱动程序目录中的OpenHMD SteamVR驱动程序，例如： 
    
     ln -s /usr/lib/steamvr/openhmd ~/.steam/steam/steamapps/common/SteamVR/drivers/openhmd
    
##  过时的设备和工具集

### OSVR

OSVR是由Sensics，Inc（一家历史悠久的VR公司）和Razer共同努力创建的VR的完全或几乎完全开放的软件API，最终开发人员只需要将各自的头戴式耳机挂接一些功能即可获得一流的支持。它支持最广泛的外围设备，并通过JSON配置文件具有极其灵活的配置。 

它还提供了一个插件，使其可以用作OpenVR实施，使您可以使用它与支持的任何设备一起玩OpenVR / SteamVR游戏。 

####  配置

安装 [osvr-core-git](<https://aur.archlinux.org/packages/osvr-core-git/>)AUR, 还有一些其他需要支持的独立设备，现在支持的插件有： [osvr-oculus-rift-git](<https://aur.archlinux.org/packages/osvr-oculus-rift-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

[osvr-leap-motion-git](<https://aur.archlinux.org/packages/osvr-leap-motion-git/>)AUR

如果希望将OSVR与SteamVR / OpenVR游戏和应用程序一起使用，安装 [osvr-steamvr-git](<https://aur.archlinux.org/packages/osvr-steamvr-git/>)AUR链接驱动到SteamVR， 运行OSVR服务器，并通过以下命令使其在后台运行: 
    
       osvr_server /usr/share/osvrcore/sample-configs/your_device_config.json
    
您可能希望自定义配置以适合您的个人需求。 

要测试您的安装是否正常并且跟踪器可用，请安装[osvr-tracker-viewer-git](<https://aur.archlinux.org/packages/osvr-tracker-viewer-git/>)AUR 和执行 `OSVRTrackerView`. 您应该看到OSVR可以拾取的每个跟踪器的一组轴。如果不这样做，请运行 `osvr_print_tree` 以查看可用的跟踪器或是否存在配置问题。 

### Oculus Rift

Oculus Rift 已经停止支持Linux了，更多请见 

[Oculus Rift](</wzh/index.php?title=Oculus_Rift&action=edit&redlink=1> "Oculus Rift（页面不存在）"). 

### Leap Motion

Leap Motion是一款价格实惠的手持跟踪器，可以轻松地安装在HMD的面板上，以允许您与虚拟对象进行交互。不幸的是，最新的Orion软件不适用于Linux，因此当前可用的跟踪功能正常但存在很多错误，它仅真正适用于Linux上的社交互动。但由于它的成本不到HMD或等效跟踪系统的1/10，因此它仍然是相当有用的设备。 

####  配置

安装 [leap-motion-driver](<https://aur.archlinux.org/packages/leap-motion-driver/>)AUR, [osvr-leap-motion-git](<https://aur.archlinux.org/packages/osvr-leap-motion-git/>)AUR 可选择安装 [leap-motion-sdk](<https://aur.archlinux.org/packages/leap-motion-sdk/>)AUR. 

要配置，启用 `leapd.service` 需执行 `LeapControlPanel`. 要测试跟踪是否有效，请运行安装随附的 `Playground`。 

##  支持的软件

当前，有一些应用程序可以在Rift和Linux上正常运行，其中一些应用程序位于AUR中。 

###  Dolphin (VR fork 版本)

[dolphin-emu-vr-git](<https://aur.archlinux.org/packages/dolphin-emu-vr-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 是Gamecube的仿真器，具有一些修补程序，可使其具有完整的头部追踪立体渲染效果，并带有许多自定义功能，使游戏在VR中开箱即用（例如，禁用剔除功能，让您查看整个世界）。 

鉴于Dolphin项目已开始正式支持上游OSVR，因此大部分支持已停止。 

**注意：** 当将此应用程序与Rift一起使用时，它可以在纵向（直接）模式下正常工作，并且应在不旋转Rift的情况下运行，这样可以最小化延迟。

###  Dolphin (官方 OSVR 支持)

olphin项目已开始致力于使用OSVR正式增加对VR的支持，可通过 [dolphin-emu-osvr-git](<https://aur.archlinux.org/packages/dolphin-emu-osvr-git/>)AUR获得支持。 它甚至可以使用OSVR的路径树输入作为控制器输入，这样您就可以使用收缩或六轴控制器输入作为Wiimote输入。但是，在某些地方支持有限，因为和原始的Oculus-only 的fork版本差别较大。 

###  wine中的游戏和程序

使用Wine时，许多应用程序具有一定程度的兼容性问题，但通常需要进行一些程度的调整才能使其按预期运行。 

[oculus-wine-wrapper-git](<https://aur.archlinux.org/packages/oculus-wine-wrapper-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 是一个实用工具，用于在运行Wine时修补Oculus SDK的Linux和Windows版本之间的差异。它为Wine应用程序创建要使用的共享内存上下文，从而允许该应用程序访问本机Oculus SDK。但似乎没有必要将SDK安装到wineprefix。 

####  Unity 游戏

为了在基于Unity的游戏中获得最佳性能，理想情况下，您应使用`-force-opengl`使其强制为opengl模式。 但是，对于未打补丁的Wine上，目前尚不可能做到这一点，因为它试图强制执行的WGL上下文与典型的GLX上下文有一些差异[有相关描述](<https://wiki.unity3d.com/index.php/Running_Unity_on_Linux_through_Wine#.22-force-opengl.22_option_crashing_Unity_.28Experimental_fix.29>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-19 ⓘ]。 使用 [wine-unity3d-git](<https://aur.archlinux.org/packages/wine-unity3d-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 包 将使您可以使用本机OpenGL运行这些游戏，从而可以在计算机上以不错的性能进行游戏。但是，玩家尝试更改视频模式或将设置弄乱，因此需要提供默认的视频设置。此外，由于它使用的是本机OpenGL，因此nvidia的__GL_THREADED_OPTIMIZATIONS可以显着提高性能。总体而言，该命令应如下所示： 
    
       env __GL_THREADED_OPTIMIZATIONS=1 wine UnityGame.exe -screen-height 1080 -screen-width 1920 -popupwindow -force-opengl
    
或者使用 [oculus-wine-wrapper-git](<https://aur.archlinux.org/packages/oculus-wine-wrapper-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]: 
    
       env __GL_THREADED_OPTIMIZATIONS=1 oculus-wine-wrapper UnityGame.exe -screen-height 1080 -screen-width 1920 -popupwindow -force-opengl
    
###  Minecrift (Minecraft VR)

可在[这里](<https://www.reddit.com/r/oculus_linux/comments/2shnbk/minecrift_linuxmac_support_coming_soon_steps_to/>)找到使用最新的JRift（本机Java rift运行时）版本运行现有Minecrift版本的指南。 您可能会希望在使用Rift时安装较旧的版本，因为JRift已不断更新以匹配Oculus SDK。 

另外，许多用户报告说使用JRE8的性能要好于JRE7。 

**注意：** 使用Rift时，此应用程序可在纵向（直接）模式下正常工作，并且应在不旋转Rift的情况下运行。但是，从15年5月12日开始，游戏中的GUI将显示为拉长的16：9矩形，而不是停留在屏幕比例上。这虽然是可用的，但是表现不理想。

### JanusVR

“janusVR：一个沉浸式，协作的多维互联网。” JanusVR是一款应用程序，可让您在多人游戏体验中浏览3D网站。janusvr的AUR包可以使用: [janusvr](<https://aur.archlinux.org/packages/janusvr/>)AUR

当JanusVR升级时，AUR软件包不会自动更新，但是当有新版本可用时，应用程序会告诉您，发生这种情况时，只需重新构建新软件包即可。 

**注意：** 此应用程序可在纵向（直接）模式下正常使用（从42.3开始），并且应在不旋转Rift的情况下运行。

####  Leap Motion 支持

Leap Motion使您可以通过手势输入，并且上世界上的其他人看到。您将需要将Leap安装到HMD的前面，并确保使用的是默认的头像。 

##  其他注意事项

###  启用OpenAL双耳模式支持

请查看 [Gaming#Binaural audio with OpenAL](<../zh-cn/%E6%B8%B8%E6%88%8F.html#Binaural_audio_with_OpenAL> "Gaming"). 
