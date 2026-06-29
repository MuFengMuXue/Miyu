**翻译状态：**

  * 本文（或部分内容）译自 [supergfxctl](<https://wiki.archlinux.org/title/supergfxctl> "arch:supergfxctl")，最近一次同步于 2024-07-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/supergfxctl?diff=0&oldid=809915>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/supergfxctl_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 本文需要更多针对非 NVIDIA 设备的混合图形笔记本的指导。 (在 [Talk:Supergfxctl](<../zh-cn/Talk:Supergfxctl.html>) 中讨论)

相关文章

  * [ASUS Linux](<../zh-cn/ASUS_Linux.html> "ASUS Linux")
  * [asusctl](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）")

[supergfxctl](<https://aur.archlinux.org/packages/supergfxctl/>)AUR 是由 [ASUS Linux](<../zh-cn/ASUS_Linux.html> "ASUS Linux") 提供的，用于在混合图形笔记本上管理显卡切换功能的实用工具。 

尽管 supergfxctl 最初是为华硕的 [Optimus](<../zh-cn/NVIDIA_Optimus.html> "Optimus") 笔记本设计的，它也逐渐成为了能在任何使用[混合图形技术](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")的笔记本上使用的独立工具。 

##  安装之前

对于使用 Optimus 的笔记本，请确保已安装 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 私有显卡驱动。请勿安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包。 如果安装了 [optimus-manager](<https://aur.archlinux.org/packages/optimus-manager/>)AUR 和 [bumblebee](<https://archlinux.org/packages/?name=bumblebee>)包 ，请卸载并确保在以下路径没有残余的 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")， [Intel](<../zh-cn/Intel_%E5%9B%BE%E5%BD%A2%E5%A4%84%E7%90%86%E5%99%A8.html> "Intel") 或其他 PRIME 管理器的配置文件： 

  * `/etc/X11/xorg.conf.d/`
  * `/etc/modprobe.d/`
  * `/etc/udev/rules.d/`

###  Initramfs 和内核参数

如果您的笔记本使用 NVIDIA 独立显卡， 您需要设置一些[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")，方法见 [NVIDIA#DRM 内核级显示模式设置](<../zh-cn/NVIDIA.html#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE> "NVIDIA")。 如果您的笔记本使用 AMD 独立显卡，您无需进行额外操作。 

##  安装

您可以使用由 ASUS Linux 提供的[软件仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#g14> "非官方用户仓库")来安装。您也可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [supergfxctl](<https://aur.archlinux.org/packages/supergfxctl/>)AUR 软件包，然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `supergfxd.service`。 

##  配置

配置文件保存在 `/etc/supergfxd.conf`。以下是一个样例配置文件： 
    
    supergfxd.conf
    
    {
      "mode": "Hybrid",
      "vfio_enable": false,
      "vfio_save": false,
      "always_reboot": false,
      "no_logind": false,
      "logout_timeout_s": 180,
      "hotplug_type": "None"
    }

##  用法

Supergfxctl 支持以下模式：`Integrated`，`Hybrid` 和 `VFIO`。它可以自行检测 MUX switch 是否处于 `AsusMuxDgpu` 模式。选项 `NvidiaNoModeSet` 会在重启系统时禁用 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") GPU [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 

若要使用 MUX switch，您必须确保 [asusctl](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）") 正在运行，详见 [asusctl#Using the MUX switch](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）")。 

###  显示支持的模式

以下命令可以显示您的笔记本支持的所有模式： 
    
    $ supergfxctl -s
    
###  获取当前模式

以下命令可以查询您显卡当前的模式： 
    
    $ supergfxctl -g
    
###  切换模式

以下命令可以将您显卡的模式切换为 `Hybrid`: 
    
    $ supergfxctl -m hybrid
    
##  预启动配置

###  使用 supergfxctl 配置显卡直通 (VFIO)

[VFIO](<../zh-cn/PCI_passthrough_via_OVMF.html> "PCI passthrough via OVMF") 显卡直通（GPU passthrough）可以通过编辑 `/etc/supergfxd.conf` 启用。在此配置文件中，[上游](<https://gitlab.com/asus-linux/supergfxctl>)建议将 `hotplug_type` 的值更改为 `Asus`，而不是 `None`。 
    
    /etc/supergfxd.conf
    
    {
    "vfio_enable": true,
    "hotplug_type": "Asus"
    }
    
详见 [ASUS Linux VFIO guide](<https://asus-linux.org/guides/vfio-guide/>)。 

###  使用 supergfxctl 与 MUX switch

当系统处于 `Hybrid` 模式时，[nvidia-prime](<https://archlinux.org/packages/?name=nvidia-prime>)包 提供的 `prime-run` 命令可以让程序运行在独立显卡上。只要 MUX switch 已经启用，应用就不会出错，所以很适合需要高图形性能的场景。 

###  在 Wayland 中使用 supergfxctl

自从 [Wayland](<../zh-cn/Wayland.html> "Wayland") 支持多显卡同步以来， 用户不再需要安装 supergfxctl，除非他们想使用 VFIO 或进一步限制耗电量。 可以使用 asusctl 切换到`AsusMuxDgpu` 模式，详见 [asusctl#Using the MUX switch](</wzh/index.php?title=Asusctl&action=edit&redlink=1> "Asusctl（页面不存在）")。 

##  图形化工具

如果您正在使用 [GNOME](<../zh-cn/GNOME.html> "GNOME") 或 [KDE](<../zh-cn/KDE.html> "KDE")，您可以使用桌面环境插件来管理 _supergfxctl_ 。下面列出了一些插件与其链接： 

名称 | 桌面环境 | 链接   
---|---|---  
supergfxctl-gex | Gnome |  <https://extensions.gnome.org/extension/5344/supergfxctl-gex/>  
GPU Supergfxctl Switch | Gnome (46) |  <https://extensions.gnome.org/extension/7018/gpu-supergfxctl-switch/>  
plasma6-applets-supergfxctl | KDE Plasma |  [plasma6-applets-supergfxctl](<https://aur.archlinux.org/packages/plasma6-applets-supergfxctl/>)AUR  
rog-control-center | Any |  [rog-control-center](<https://aur.archlinux.org/packages/rog-control-center/>)AUR
