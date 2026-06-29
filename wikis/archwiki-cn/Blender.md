**翻译状态：**

  * 本文（或部分内容）译自 [Blender](<https://wiki.archlinux.org/title/Blender> "arch:Blender")，最近一次同步于 2024-08-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Blender?diff=0&oldid=813267>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Blender_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Blender](<https://www.blender.org>) 是最为知名的开源3D建模程序。 

##  安装

安装软件包 [blender](<https://archlinux.org/packages/?name=blender>)包 。 

##  GPU 渲染

Blender支持大多数硬件加速渲染。在根据你的硬件准备好系统（见下文）后，你可以在 _编辑 > 偏好设置... > 系统_中选择显卡作为渲染设备。 

###  NVIDIA显卡

Blender支持CUDA和OptiX两个渲染后端用于NVIDA显卡，大多数现代NVIDIA显卡都受支持。为了使用这些后端，需要安装[cuda](<https://archlinux.org/packages/?name=cuda>)包。之后系统选项中应该能够看到相关选项。 

###  Intel Arc显卡

如果你有一块现代Intel Arc显卡，你可以使用Blender内建的硬件支持，前提是已经安装了[intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包。 

在本文撰写之时，你可能需要为Blender指定一个额外的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    CYCLES_ONEAPI_ALL_DEVICES=1 blender
    
###  AMD 开源驱动上的 HIP

对于支持的GPU而言 (GFX9, CDNA, 以及 RDNA, 详情请参考[官方的硬件兼容列表](<https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html#hip-amd>))，安装[hip-runtime-amd](<https://archlinux.org/packages/?name=hip-runtime-amd>)包来通过HIP获得Blender的GPU加速功能，使用[Mesa](<../zh-cn/OpenGL.html> "Mesa")驱动。 

要在Blender中启用HIP,安装[hip-runtime-amd](<https://archlinux.org/packages/?name=hip-runtime-amd>)包并在Blender偏好设置中选择你的GPU。 

**注意：** ROCm HIP目前在3D视角中使用cycles渲染引擎存在[问题](<https://gitlab.freedesktop.org/drm/amd/-/issues/2145>)（参考"问题"中的内容来获得解决方法），但是通过 _渲染 > 渲染图像_ 或按下F12渲染图像工作正常

##  专业的渲染插件

Blender在专业领域以及工业上越来越知名。因此，目前已有不少EEVEE和Cycles渲染引擎的替代品，它们以插件的形式存在。以下列出了在Linux上发布或者即将发布的专业渲染插件列表。 

### BlendNet

[BlendNet](<https://github.com/state-of-the-art/BlendNet>) 是一个开源的插件，它能让多台机器上的CPU和GPU协作渲染。 

BlendNet内置了对主要云服务的支持，例如AWS, Azure 或者 GCP, 而且也支持您自己的渲染农场。 

####  集成云服务器

  1. 安装软件包 [blendnet](<https://aur.archlinux.org/packages/blendnet/>)AUR。
  2. 在 _偏好设置 - > 插件 -> Render: BlendNet_ 中启用BlendNet插件
  3. 按照官方[BlendNet wiki](<https://github.com/state-of-the-art/BlendNet/wiki>)的指引，配置好AWS、Azure或GCP上的渲染农场

####  自建服务器

[blendnet](<https://aur.archlinux.org/packages/blendnet/>)AUR 提供了systemd单元和配置，这让您能便利地部署您自己的CUDA GPU加速的Blendnet渲染农场。 

BlendNet渲染农场由一个“管理员”实例与多个代理机器组成。 blender插件连接到管理员，借此安排渲染作业。 参看 [BlendNet wiki](<https://github.com/state-of-the-art/BlendNet/wiki/How-BlendNet-is-working>) 以了解更多和BlendNet架构有关的内容。 

首先，请在管理员、代理和安装插件的机器上都安装好 [blendnet](<https://aur.archlinux.org/packages/blendnet/>)AUR，然后按照以下步骤执行。 

#####  设置: 管理员

  1. 复制`/etc/blendnet/server.key`和`/etc/blendnet/server.crt`到所有管理员、代理和安装插件的机器上的`/etc/blendnet/`目录.
  2. 编辑`/etc/blendnet/manager.json`，添加管理员用户名和密码。
  3. 编辑`/etc/blendnet/manager.json`，添加代理用户名和密码。
  4. 启动/启用`blendnet-manager.service`服务。

#####  设置: 代理

  1. 编辑`/etc/blendnet/agent.json`添加和管理员机器中相同的代理用户名和密码。
  2. 启动/启用`blendnet-agent.service`服务。

如果安装来[cuda](<https://archlinux.org/packages/?name=cuda>)包，[blendnet](<https://aur.archlinux.org/packages/blendnet/>)AUR会自动启用GPU+CPU加速：你可以通过查看代理机器的日志来检查GPU加速是否启用： 
    
    $ journalctl -xefu blendnet-agent.service
    
#####  设置: 插件

  1. 在 _偏好设置 - > 插件 -> Render: BlendNet_ 中启用BlendNet插件。
  2. 为插件配置管理员/代理的用户名和密码。
  3. 指定`/etc/blendnet/server.crt`中的CA证书。
  4. 关闭偏好设置，打开渲染属性并启用Cycles渲染引擎 （**不是** BlendNet！）
  5. 通过"BlendNet Render (local)"的Cycles面板中`+`添加所有代理。
  6. 根据[BlendNet 渲染说明](<https://github.com/state-of-the-art/BlendNet/wiki/HOWTO%3A-First-steps#run-the-first-render-task>)完成剩余步骤。

### LuxCoreRender

[LuxCoreRender](<https://luxcorerender.org/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]是一个使用OpenCL的开源渲染方法。安装[blender-plugin-luxcorerender](<https://aur.archlinux.org/packages/blender-plugin-luxcorerender/>)AUR并在用户偏好中启用LuxCoreRender插件以使用该渲染器。 

### RenderMan

RenderMan是一个兼容Linux的私有渲染插件，在非商业协议下可自由使用，参见[相关内容](<https://renderman.pixar.com/view/renderman4blender>)。 

### Pro-Render

[Pro-Render](<https://www.amd.com/en/technologies/radeon-prorender-blender>)是一个来源于AMD的开源插件，能够让兼容OpenCL 1.2的设备创建逼真的GPU渲染，与CPU渲染相比加速了渲染速度。 

### Blend4Web

[Blend4Web](<https://www.blend4web.com/>)是一个用于在网络浏览器中创建并显示3D图像的开源框架。包含一个Blender插件来直接创建并导出3D场景到网页。在插件设置中激活Blend4Web专有配置文件，当切换到这个配置后，Blender界面会改变为仅显示与Blender4Web相关的设置。参见[相关文档](<https://www.blend4web.com/doc/en/setup.html>)来安装Blender4Web SDK。 

### Verge3D

[Verge3D](<https://www.soft8soft.com/verge3d>)是一个实时渲染器，工具包来源于Blend4Web的原创团队。包含Puzzles视觉编辑器来允许不通过代码创作可交互网页应用。 

##  解决问题

###  Blender在选择对象时会很卡顿

当使用集成Intel显卡时，可能要5-10秒才能选择一个对象。在 _File > User Preferences > System_ 中将 _Selection_ 改为 _OpenGL Occlusion Queries_ 。 

###  Blender未把AMD显卡列在OpenCL渲染设备中

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 不用专有驱动也可以启用Blender OpenCL支持。Blender 3.0移除了OpenCL支持，考虑使用HIP (在[Talk:Blender](<../zh-cn/Talk:Blender.html>)讨论)

Blender（目前）仅支持AMD官方专有驱动来启用OpenCL，意味着你需要安装以下任意一个AMD OpenCL驱动： 

  * [AMDGPU PRO](<../zh-cn/AMDGPU_PRO.html> "AMDGPU PRO")
  * [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR驱动搭配开源AMDGPU驱动

安装后AMD GPU应该会出现在渲染设备中，通过 _File > User Preferences > System > Compute Device_ 选择。 

**注意：** Blender开发者决定转移到其他API([HIP](<https://github.com/ROCm-Developer-Tools/HIP>))并弃用OpenCL支持。该决定将会在Blender 3.0生效（2021年12月4日），参见[更多内容](<https://developer.blender.org/T91571>)。

###  Blender 在 i915 上崩溃

仅仅更改初始界面中的立方体大小，就会导致Blender无响应，dmesg显示关于GPU挂起的信息： 
    
    kernel: i915 0000:00:02.0: [drm] blender[90663] context reset due to GPU hang
    kernel: i915 0000:00:02.0: [drm] GPU HANG: ecode 9:1:85df9ebf, in blender [90663]
    
解决办法来源于[上游Bug](<https://gitlab.freedesktop.org/drm/intel/-/issues/2935>)和一个[AskUbuntu上的提问](<https://askubuntu.com/questions/1477715/blender-hangs-using-intel-integrated-graphics>): 

  * 设置`INTEL_DEBUG=reemit`环境变量后启动Blender,也就是说将Blender .desktop文件的Exec行内容改为`Exec=env INTEL_DEBUG=reemit blender %f`

  * 增加preemtion超时限制到 10 000 ms。要永久改变这个值，添加一个[udev](<../zh-cn/Udev.html> "Udev")规则：

    /etc/udev/rules.d/99-i915-increase-preemt-timeout.rules
    
    # Increase Intel preemt timeout to 10 000 ms
    #
    # This is needed for Blender not to crush, see
    # https://askubuntu.com/questions/1477715/blender-hangs-using-intel-integrated-graphics
     
    ACTION=="add|bind",SUBSYSTEM=="pci",DRIVER=="i915",RUN+="/bin/bash -c 'for i in /sys/$DEVPATH/drm/card?/engine/[rc]cs*/preempt_timeout_ms; do echo 10000 > $i; done'"
    
###  界面文字

如果自己过小或模糊，字体大小可以通过 _User Preferences > Themes > Text Style_增加（一或两磅）。在 _User Preferences > Themes > System_选择加粗字体作为界面字体可以明显降低模糊。 

##  参阅

  * [Blender manual](<https://docs.blender.org/manual/en/dev/>)
  * Reddit 上的 [Blender wiki](<https://www.reddit.com/r/blender/wiki/index>)
  * [Sheepit](</wzh/index.php?title=Sheepit&action=edit&redlink=1> "Sheepit（页面不存在）") 免费、分布式的Blender渲染农场
