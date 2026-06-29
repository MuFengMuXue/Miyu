**翻译状态：**

  * 本文（或部分内容）译自 [Nouveau](<https://wiki.archlinux.org/title/Nouveau> "arch:Nouveau")，最近一次同步于 2024-11-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nouveau?diff=0&oldid=820640>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nouveau_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")

本文包含安装和配置NVIDIA显卡开源驱动 [Nouveau](<https://nouveau.freedesktop.org/>) 的内容. 有关官方闭源驱动的信息请查看[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA"). 

查找硬件的[代号](<https://nouveau.freedesktop.org/wiki/CodeNames>) ([Wikipedia 包含更详细的列表](<https://en.wikipedia.org/wiki/Comparison_of_Nvidia_Graphics_Processing_Units> "wikipedia:Comparison of Nvidia Graphics Processing Units")), 然后和[功能矩阵](<https://nouveau.freedesktop.org/wiki/FeatureMatrix/>)进行比较，以查看支持的功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mesa](<https://archlinux.org/packages/?name=mesa>)包 包，它提供了用于 3D 加速的 DRI 驱动程序。 

  * 为x86_32 提供支持，另外安装 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 源中的的 [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包 包。
  * 对于 DDX 驱动程序（提供 [Xorg](<../zh-cn/Xorg.html> "Xorg") 中的 2D 加速），[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包 包。

**注意：** 有建议指出不安装 [xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包 驱动，而是使用 modesetting 驱动来支持 [NV50 (G80)](<https://nouveau.freedesktop.org/CodeNames.html#NV50>) 及更新版本的硬件，可能会更有利。可以参考一篇来自 2021 年的 [用户报告](<https://bbs.archlinux.org/viewtopic.php?id=263498>)。

详见[硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")

###  使用 Mesa NVK Vulkan 驱动程序

**警告：** 这个驱动仍在开发中，因此可能会出现性能问题。一些在开源和专有驱动上正常运行的内容（主要是游戏）可能在使用 NVK 上表现不佳（甚至完全无法运行）。如果玩游戏是一个重要的使用场景，那么在 NVK 成熟之前，您应该避免使用它。

使用 NVK 需要[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")版本在6.7及以上， mesa版本在24.1及以上。 

在启用 NVK 之前，必须[卸载](<../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "卸载")以下所有包（以及它们的 `lib32` 和 [DKMS](<../zh-cn/DKMS.html> "DKMS") 版本）： 

  * [nvidia](<https://archlinux.org/packages/?name=nvidia>)包, [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包, [nvidia-lts](<https://archlinux.org/packages/?name=nvidia-lts>)包, [nvidia-beta](<https://aur.archlinux.org/packages/nvidia-beta/>)AUR
  * [nvidia-settings](<https://archlinux.org/packages/?name=nvidia-settings>)包, [nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包
  * [egl-wayland](<https://archlinux.org/packages/?name=egl-wayland>)包

如果你使用的是多 GPU 设备，请确保没有在` /etc/modprobe.d` 中将 Nouveau 列入黑名单。 

**注意：** 您可能需要卸载系统上的所有 GPU 管理器，它们大多数会将模块列入黑名单，这可能会干扰 NVK

然后[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vulkan-nouveau](<https://archlinux.org/packages/?name=vulkan-nouveau>)包（如果需要，则安装 [lib32-vulkan-nouveau](<https://archlinux.org/packages/?name=lib32-vulkan-nouveau>)包）。 

使用 `nouveau.config=NvGspRm=1` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")

最后重启系统 

可以使用 [vulkan-tools](<https://archlinux.org/packages/?name=vulkan-tools>)包 中的 ` vulkaninfo` 来验证,它会显示系统中的 NVIDIA GPU 正在使用 NVK 驱动程序。 
    
    $ vulkaninfo
    
    ...
    GPU id : 0 (NVIDIA GeForce RTX 3050 Ti Laptop GPU (**NVK GA107**)):
           Surface type = VK_KHR_wayland_surface
           Formats: count = 8
    ...

##  加载

Nouveau的内核模块应该在系统启动时就已自动加载，如果没有的话： 

  * 确保你的[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")中没有`nomodeset` 或者 `vga=`， 因为Nouveau需要内核模式设置。
  * 另外，确保你没有在 modprobe 配置文件 `/etc/modprobe.d/` 或 `/usr/lib/modprobe.d/` 中屏蔽 Nouveau。
  * 检查 [dmesg](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Dmesg") 中有没有 opcode 错误，如果有的话，将 `nouveau.config=NvBios=PRAMIN` 加入[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")禁止模块卸载[[1]](<https://nouveau.freedesktop.org/wiki/TroubleShooting/#index10h3>)
  * 检查 `/etc/X11/xorg.conf` 和 `/etc/X11/xorg.conf.d/` 中是否存在任何文件，并且该文件是否引用了 [Template:Nvidia](</wzh/index.php?title=Template:Nvidia&action=edit&redlink=1> "Template:Nvidia（页面不存在）") 驱动程序。最好将该文件重命名。

###  尽早启动 KMS

**提示：** 如果你对这个问题的解决有问题的话，请访问[这个页面](<../zh-cn/Kernel_mode_setting.html#Forcing_modes_and_EDID> "Kernel mode setting").

Nouveau 驱动依赖[Kernel mode setting](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting") (KMS)。当系统启动时，KMS 模块会在其它模块之后启用，所以显示的分辨率发生改变。查看[Nouveau KernelModeSetting 页面](<https://nouveau.freedesktop.org/wiki/KernelModeSetting>)获取更多细节。 

可以设置将 KMS 尽早启动，在 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 加载时就接管功能。 

将 `nouveau` 加入 `/etc/mkinitcpio.conf` 的 `MODULES` 数组: 
    
    MODULES="... nouveau ..."
    
如果你使用了一个自定义的EDID文件，你应该像这样把它加入到initramfs 中： 
    
    /etc/mkinitcpio.conf
    
    FILES="/lib/firmware/edid/your_edid.bin"

重新生成初始ramdisk映像： 
    
    # mkinitcpio -p <kernel preset; e.g. _linux_ >
    
如果 Nouneau 出问题了，不得不多次重建 nouveau-drm 进行测试，请不要在 initramfs 中添加`nouveau`。因为这样会容易忘记重建 initramfs 而使测试更加困难。先使用“延迟启动”，直到系统已经稳定。如果需要自定义固件，使用 initrams 可能会有更多问题（一般不建议） 

##  提示与技巧

###  保留已安装的Nvidia驱动

如果你想保留已经安装的官方驱动但又想要使用Nouveau驱动，像下面注释掉`/etc/modprobe.d/nouveau_blacklist.conf` 或 ` /usr/lib/modprobe.d/nvidia-utils.conf`中的内容 
    
    #blacklist nouveau
    
你可能还需要注释掉其他优先使用专有驱动的配置文件，例如 [systemd-modules-load](<https://man.archlinux.org/man/systemd-modules-load.service.8.en>) 的 `/usr/lib/modules-load.d/nvidia-utils.conf` 和 [Udev](<../zh-cn/Udev.html> "Udev") 的 `/usr/lib/udev/rules.d/60-nvidia.rules`。可以使用以下命令检查驱动程序安装了哪些文件： 
    
    # pacman -Ql nvidia-utils | grep conf
    
    然后，确保禁用所有以 nvidia- 为前缀的服务，这些服务可能会调用 nvidia-modprobe 在启动时加载模块。例如：
    
     $ systemctl status nvidia-persistenced.service
    
如果你使用的是 [Xorg](<../zh-cn/Xorg.html> "Xorg")，可以通过创建文件 `/etc/X11/xorg.conf.d/20-nouveau.conf` 并添加以下内容，告诉 Xorg 加载 nouveau 驱动，而不是 NVIDIA 驱动： 
    
    Section "Device"
        Identifier "Nvidia card"
        Driver "nouveau"
    EndSection
    
重启以使更改生效。然后通过查看内核消息检查是否加载成功： 
    
    # dmesg
    
###  安装最新的开发包

你可以通过AUR安装最新的git包： 

  * 你可以通过[mesa-git](<https://aur.archlinux.org/packages/mesa-git/>)AUR安装最新的Mesa（包含最新的DRI驱动）。
  * 你可以通过[xf86-video-nouveau-git](<https://aur.archlinux.org/packages/xf86-video-nouveau-git/>)AUR 安装最新的DDX驱动。
  * 你也可以尝试安装像 [linux-mainline](<https://aur.archlinux.org/packages/linux-mainline/>)AUR 这样比较新的内核版本，这可能会带来更好的性能。
  * 要获得Nouveau最新的更新, 你应该使用AUR中的[linux-git](<https://aur.archlinux.org/packages/linux-git/>)AUR 包，并且编辑PKGBUILD 以使用Nouveau自己的内核库，目前它位于： <git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau>.
  * [libdrm-git](<https://aur.archlinux.org/packages/libdrm-git/>)AUR
  * [lib32-libdrm-git](<https://aur.archlinux.org/packages/lib32-libdrm-git/>)AUR
  * [lib32-mesa-git](<https://aur.archlinux.org/packages/lib32-mesa-git/>)AUR

你可以在 [Nouveau Source page](<https://nouveau.freedesktop.org/wiki/Source>)找到上游驱动源. 

**注意：** 在 [#安装](<#%E5%AE%89%E8%A3%85>)中提到, xf86-video-nouveau不再是必需的，也不推荐安装，在大多数情况下，未安装该驱动时，您的 GPU 将表现得更好。

###  双输出

Nouveau 支持xrandr拓展和多显示器，教程详见[RandR12](</wzh/index.php?title=RandR12&action=edit&redlink=1> "RandR12（页面不存在）")

这是一个完整的例子 `/etc/X11/xorg.conf.d/20-nouveau.conf` 用来演示在双输出模式下运行两个显示器。当然，你可能更喜欢像GNOME显示控制中心 (`gnome-control-center display`)这样的图形化配置工具. 
    
    # the right one
    Section "Monitor"
              Identifier   "NEC"
              Option "PreferredMode" "1280x1024_60.00"
    EndSection
    
    # the left one
    Section "Monitor"
              Identifier   "FUS"
              Option "PreferredMode" "1280x1024_60.00"
              Option "LeftOf" "NEC"
    EndSection
    
    Section "Device"
        Identifier "nvidia card"
        Driver "nouveau"
        Option  "Monitor-DVI-I-1" "NEC"
        Option  "Monitor-DVI-I-2" "FUS"
    EndSection
    
    Section "Screen"
        Identifier "screen1"
       Monitor "NEC"
        DefaultDepth 24
          SubSection "Display"
           Depth      24
           Virtual 2560 2048
          EndSubSection
        Device "nvidia card"
    EndSection
    
    Section "ServerLayout"
        Identifier "layout1"
        Screen "screen1"
    EndSection

###  设置控制台分辨率

使用[fbset](<https://archlinux.org/packages/?name=fbset>)包工具调整控制台分辨率. 你也可以通过 video= kernel 这样的选项来调整控制台分辨率 (详见 [KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS")). 

###  电源管理

Nouveau 驱动中缺乏合适的电源管理，大多数显卡在使用过程中会保持在较低的功率状态，频率也较低。对于某些显卡，已有实验性支持的 GPU 重新调频（详见 [Nouveau PowerManagement page](<https://nouveau.freedesktop.org/wiki/PowerManagement>)），并且从内核 4.5 开始，可以通过位于 /sys/kernel/debug/dri/*/pstate 的 debugfs 接口进行控制。 

正如 [upstream suggested](<https://gitlab.freedesktop.org/mesa/mesa/-/issues/10933#note_2357592>) 的那样，这个 debugfs 接口在 Turing 及更新版本的显卡上不可用，仅适用于 Kepler 及更早版本的显卡。 

例如，要检查系统中第一块显卡的可用电源状态和当前设置，可以运行： 
    
     # cat /sys/kernel/debug/dri/0/pstate
    
也可以通过向该接口写入来手动设置/强制某个电源状态： 
    
    # echo _pstate_ > /sys/kernel/debug/dri/0/pstate
    
**警告：** 重新调频仍处于高度实验阶段。手动设置电源状态可能会导致系统挂起、数据损坏或显卡过热。

###  风扇控制

如果硬件支持，可以通过 `/sys` 控制风扇转速。 
    
    $ find /sys -name pwm1_enable
    /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/hwmon/hwmon1/pwm1_enable
    $ readlink /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/driver
    ../../../../bus/pci/drivers/nouveau
    
`pwm1_enable` 可以设置为 0, 1 或 2，意思是 NONE, MANUAL 和 AUTO 风扇控制。设置为手动时，可以手动设置 `pwm1`，例如设置为 40 表示 40% 的转速. 

**警告：** 风险自担，不要太热烧了显卡!

可以通过 udev 规则设置: 
    
    $ cat /etc/udev/rules.d/50-nouveau-hwmon.rules
    ACTION=="add", SUBSYSTEM=="hwmon", DRIVERS=="nouveau", ATTR{pwm1_enable}="2"
    
参考: 

  * <https://floppym.blogspot.de/2013/07/fan-control-with-nouveau.html>
  * <https://web.archive.org/web/20141031191559/https://kalgan.cc/blog/posts/Controlling_nVidia_cards_fans_with_nouveau_in_Debian/>

### Optimus

要在笔记本上使用 [Optimus](<../zh-cn/NVIDIA_Optimus.html> "Optimus")(使用两个 GPUs)，请阅读 [bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee") 和 [PRIME](<../zh-cn/PRIME.html> "PRIME")

###  垂直同步

Xorg 合成器在使用 Nouveau 时容易出现问题。与大多数合成器不同，[Picom](<../zh-cn/Picom.html> "Picom") 提供了许多选项，可以进行调整以获得更流畅、无撕裂的效果。预计能够提供良好效果的配置如下： 
    
    $ picom -b --unredir-if-possible --backend xr_glx_hybrid --vsync --use-damage --glx-no-stencil
    
**提示：** 使用其他合成器时，别忘了关闭窗口管理器（如 KWin）的合成功能。

##  故障排除

将 `drm.debug=14` 和 `log_buf_len=16M` 添加到您的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中，以启用视频调试： 

建立详细的Xorg日志： 
    
    startx -- -logverbose 9 -verbose 9
    
查看加载的视频模块的参数和值： 
    
    modinfo -p video
    
###  禁用 MSI

如果出现模块加载错误或 X 服务器无法启用，请尝试将 `nouveau.config=NvMSI=0` 加入[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters"). 

Source: <https://bugs.freedesktop.org/show_bug.cgi?id=78441>

###  虚拟输出问题

Nouveau 驱动可能会检测到“虚拟”输出。例如，VGA-1 和 LVDS-1 都显示为连接状态，但实际上只有 LVDS-1 存在。 

这会导致显示问题和/或在关闭笔记本盖时无法进入挂起状态。 

####  内核参数

可以通过在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中禁用虚拟输出（如上述示例中的 VGA-1）来解决此问题： 
    
    video=VGA-1:d
    
此处 **d** 表示禁用(disable) 

Nouveau 内核模块还有一个选项，可以禁用 TV 输出检测 [[2]](<https://nouveau.freedesktop.org/wiki/KernelModuleParameters/#tv_disable>)： 
    
     tv_disable=1
     
####  Xorg 配置

可以通过将以下内容添加到 `/etc/X11/xorg.conf.d/20-nouveau.conf` 来在 [Xorg](<../zh-cn/Xorg.html> "Xorg") 中禁用虚拟输出： 
    
    Section "Monitor"
    Identifier "VGA-1"
    Option "Ignore" "1"
    EndSection
    
Source: <http://gentoo-en.vfose.ru/wiki/Nouveau#Phantom_and_unpopulated_output_connector_issues>

#### Xrandr

[Xrandr](<../zh-cn/Xrandr.html> "Xrandr") can disable the output: 
    
     $ xrandr --output VGA-1 --off
    
This can be added to the [xinit](<../zh-cn/Xinit.html> "Xinit") configuration. 

### Random lockups with kernel error messages

Specific Nvidia chips with Nouveau may give random system lockups and more commonly throw many kernel messages, seen with _dmesg_. Try adding the `nouveau.noaccel=1` [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter"). See [Fedora:Common kernel problems#Systems with nVidia adapters using the nouveau driver lock up randomly](<https://fedoraproject.org/wiki/Common_kernel_problems#Systems_with_nVidia_adapters_using_the_nouveau_driver_lock_up_randomly> "fedora:Common kernel problems") for more information. 

Note that using `nouveau.noaccel=1` kernel parameter might cause [~%100 CPU usage on Wayland](<https://bugs.kde.org/show_bug.cgi?id=485429>) when there is no iGPU or [disabled iGPU by factory](<https://h30434.www3.hp.com/t5/Notebook-Video-Display-and-Touch/Integrated-Intel-Graphics-GPU-disabled-by-factory/td-p/7178220>). You can switch to X11 session or prefer adding `LIBGL_ALWAYS_SOFTWARE=1` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") for wayland to disable OpenGL hardware acceleration completely. 

As an alternative, you can also use the `QT_XCB_FORCE_SOFTWARE_OPENGL=1` [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") to disable OpenGL acceleration in Qt applications. 

### Flat Panel Table Invalid

NVIDIA graphics cards with recent chipsets can cause startup issues - this includes X11 being unable to start and lspci freezing indefinitely[[3]](<https://bugzilla.redhat.com/show_bug.cgi?id=1425253>)[[4]](<https://bbs.archlinux.org/viewtopic.php?id=192532>)[[5]](<https://stackoverflow.com/questions/28062458/nouveau-error-while-booting-arch>)[[6]](<https://bbs.archlinux.org/viewtopic.php?id=207602>)[[7]](<https://unix.stackexchange.com/questions/207895/how-do-i-install-antergos-with-a-gtx-970>). 

This can break live distributions/installation media. This can be detected either by running lspci, or checking the systemd journal for the error: 
    
    nouveau E[     DRM]Pointer to flat panel table invalid
    
The system may start if the Nouveau driver is disabled by passing the following [kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters"): 
    
    modprobe.blacklist=nouveau
    
The Nouveau driver can then be loaded using 
    
    # modprobe nouveau
    
The system should then function correctly. If you have another Nvidia graphics card, or just want to be safe, you can disable the offending card using: 
    
    $ echo 1 > /sys/bus/pci/devices/_[card device id]_ /remove
    