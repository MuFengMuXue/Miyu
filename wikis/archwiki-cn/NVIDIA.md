相关文章

  * [NVIDIA/提示和技巧](<../zh-cn/NVIDIA/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html> "NVIDIA/提示和技巧")
  * [NVIDIA/故障排除](<../zh-cn/NVIDIA/%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html> "NVIDIA/故障排除")
  * [Nouveau](<../zh-cn/Nouveau.html> "Nouveau")
  * [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus")
  * [PRIME](<../zh-cn/PRIME.html> "PRIME")
  * [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee")
  * [nvidia-xrun](<../zh-cn/Nvidia-xrun.html> "Nvidia-xrun")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")

**翻译状态：**

  * 本文（或部分内容）译自 [NVIDIA](<https://wiki.archlinux.org/title/NVIDIA> "arch:NVIDIA")，最近一次同步于 2025-11-2，若英文版本有所[更改](<https://wiki.archlinux.org/title/NVIDIA?diff=0&oldid=849580>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NVIDIA_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文包含安装和配置 [NVIDIA](<https://www.nvidia.com>) 官方显卡驱动的信息。想要了解社区开源驱动的信息，参见 [Nouveau](<../zh-cn/Nouveau.html> "Nouveau")。如果您使用的是有混合显卡的笔记本（如Intel核显+NVIDIA显卡）, 请额外参阅 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") 页面。 

##  安装

**警告：** 请避免从 NVIDIA 官网下载驱动包进行安装。建议使用 Arch Linux 的 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装驱动程序，这样驱动程序能够在更新系统时与其他组件一同更新。

**注意：** 在具有[混合图形技术](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")的机型上双重启动时，启用Windows或第三方应用中的 _集显模式/节能模式_ 可能会完全禁用NVIDIA独立显卡(例如[ASUS节能模式](<https://www.asus.com/support/faq/1043747/#a14>))，导致其无法被检测到。

首先，从 [nouveau NVIDIA代号查询页](<https://nouveau.freedesktop.org/CodeNames.html>) 中查找您的显卡系列代号(例如：NV110, NVC0)。您也可以运行以下命令获知显卡型号/名称： 
    
    $ lspci -k -d ::03xx
    
随后为您的显卡安装合适的驱动： 

**注意：**

  * 使用 [dkms](<https://archlinux.org/packages/?name=dkms>)包 安装时, 请参阅 [DKMS#安装](<../zh-cn/DKMS.html#%E5%AE%89%E8%A3%85> "DKMS") 部分
  * 使用[DKMS](<../zh-cn/DKMS.html> "DKMS")方式安装的驱动并不与特定内核绑定，其会为安装了头文件的每个内核重新编译NVIDIA内核模块。

GPU 家族  | 驱动  | 支持状态   
---|---|---  
[Blackwell (GBXXX)](<https://en.wikipedia.org/wiki/Blackwell_\(microarchitecture\)> "w:Blackwell \(microarchitecture\)")系列或更新版本  |  [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 适用于 [linux](<https://archlinux.org/packages/?name=linux>)包   
[nvidia-open-lts](<https://archlinux.org/packages/?name=nvidia-open-lts>)包 适用于 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包   
[nvidia-open-dkms](<https://archlinux.org/packages/?name=nvidia-open-dkms>)包 适用于任意内核  |  [上游推荐使用](<https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/>)  
支持中1  
[Turing (NV160/TUXXX)](<https://nouveau.freedesktop.org/CodeNames.html#NV160>)系列到 [Ada Lovelace (NV190/ADXXX)](<https://nouveau.freedesktop.org/CodeNames.html#NV190>)系列  | 同时被以下包支持： 

  * [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 在 Turing 架构上可能存在电源管理问题2,   
可能会在 Turing 架构的笔记本上崩溃2
  * [nvidia-580xx-dkms](<https://aur.archlinux.org/packages/nvidia-580xx-dkms/>)AUR

[Maxwell (NV110/GMXXX)](<https://nouveau.freedesktop.org/CodeNames.html#NV110>)系列到   
[Volta (NV140/GVXXX)](<https://nouveau.freedesktop.org/CodeNames.html#NV140>)系列  |  [nvidia-580xx-dkms](<https://aur.archlinux.org/packages/nvidia-580xx-dkms/>)AUR | 旧版，支持中   
[Kepler (NVE0/GKXXX)](<https://nouveau.freedesktop.org/CodeNames.html#NVE0>)系列  |  [nvidia-470xx-dkms](<https://aur.archlinux.org/packages/nvidia-470xx-dkms/>)AUR | 过时，不再支持3,4  
[Fermi (NVC0/GF1XX)](<https://nouveau.freedesktop.org/CodeNames.html#NVC0>)系列  |  [nvidia-390xx-dkms](<https://aur.archlinux.org/packages/nvidia-390xx-dkms/>)AUR  
[Tesla (NV50/G80-90-GT2XX)](<https://nouveau.freedesktop.org/CodeNames.html#NV50>)系列  |  [nvidia-340xx-dkms](<https://aur.archlinux.org/packages/nvidia-340xx-dkms/>)AUR  
[Curie (NV40/G70)](<https://nouveau.freedesktop.org/CodeNames.html#NV40>) 以及更老的系列  | Arch Linux没有相应的驱动包   
  
  1. 如果以上驱动安装后都不能正常工作，您也许需要使用 [nvidia-open-beta](<https://aur.archlinux.org/packages/nvidia-open-beta/>)AUR 以获得更新版本的驱动。
  2. NVIDIA 的开源内核模块无法在 Turing 架构的显卡上启用 [D3 电源管理](<../zh-cn/PRIME.html#PCI-Express_Runtime_D3_\(RTD3\)_%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "PRIME")。这会降低搭载Turing 架构显卡且使用 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") 配置的笔记本电脑的续航时间。建议改用专有驱动模块（例如 [nvidia-580xx-dkms](<https://aur.archlinux.org/packages/nvidia-580xx-dkms/>)AUR），并在 [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") 中设置`NVreg_EnableGpuFirmware=0`。[有关此问题的更多信息](<https://github.com/NVIDIA/open-gpu-kernel-modules/issues/640#issuecomment-2188114679>)。
  3. 在安装了 [Intel CPU 11 代或更新版本的处理器](<https://www.intel.com/content/www/us/en/newsroom/opinion/intel-cet-answers-call-protect-common-malware-threats.html>)以及Linux 5.18 (或更高版本)的系统上可能无法正常工作，原因是与其与 [Indirect Branch Tracking](<https://edc.intel.com/content/www/us/en/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/007/indirect-branch-tracking/>) 这个安全功能不兼容。您可以在 [Arch_的启动流程](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html> "Arch 的启动流程")中设置 `ibt=off` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")来禁用它。请注意，这项安全功能负责[缓解一些攻击技术的影响](<https://lwn.net/Articles/889475/>)。
  4. NVIDIA不再积极为这些显卡提供驱动。这意味着这些驱动[不正式支持现在的Xorg版本](<https://nvidia.custhelp.com/app/answers/detail/a_id/3142/>)。因此使用 [Nouveau](<../zh-cn/Nouveau.html> "Nouveau") 驱动可能会更方便，因为它依然为这些老显卡提供对当前Xorg的支持。但是，NVIDIA 提供的 legacy 驱动依旧可用，并且或许拥有更好的 3D 性能（稳定性）。

对于 32 位应用程序支持，请安装 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库中对应的 _lib32_ nvidia 软件包（例如 [lib32-nvidia-utils](<https://archlinux.org/packages/?name=lib32-nvidia-utils>)包）。 

[nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 软件包包含一个文件，其将会在重启后屏蔽 _nouveau_ 内核模块。另外，您还可以将`kms` 从 `/etc/mkinitcpio.conf` 里的`HOOKS` 数组中移除，并[重新生成 initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 这将防止 initramfs 包含 `nouveau` 模块，以确保内核在早启动阶段不会加载它。 

**注意：** 如果您正在使用 [Wayland](<#Wayland>) ，您需要首先配置 [#DRM 内核级显示模式设置](<#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE>) 后重启，否则您可能会遇到黑屏。

一旦驱动安装完毕，就可以进入下一步了：[#Xorg配置](<#Xorg%E9%85%8D%E7%BD%AE>)或[#Wayland配置](<#Wayland%E9%85%8D%E7%BD%AE>)

###  定制内核

安装 [nvidia-open-dkms](<https://archlinux.org/packages/?name=nvidia-open-dkms>)包 软件包以及你内核对应的头文件。 

确保您的内核设置了 `CONFIG_DRM_SIMPLEDRM=y` 选项，如果使用 `CONFIG_DEBUG_INFO_BTF`，则 PKGBUILD 中需要以下选项（从内核 5.16 开始）： 
    
    install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids
    
[linux](<https://archlinux.org/packages/?name=linux>)包 6.15 引入了新的 NVIDIA GPU驱动 [Nova](<https://docs.kernel.org/gpu/nova/index.html>)。[nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 默认会将其加入黑名单。您可以[运行systemd-analyze](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E4%BD%BF%E7%94%A8_/etc/modprobe.d/%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6> "内核模块")来验证这一点。 如果您还安装了其他版本的驱动程序，可能还需要手动将`nova_core`和`nova_drm`模块加入[黑名单](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%BB%91%E5%90%8D%E5%8D%95> "内核模块")。 

###  DRM 内核级显示模式设置

由于NVIDIA不支持[自动 KMS 晚加载](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#KMS_%E6%99%9A%E5%90%AF%E5%8A%A8> "内核级显示模式设置"), 要正常运行Wayland 合成器或[没有 root 权限的 Xorg](<../zh-cn/Xorg.html#%E6%B2%A1%E6%9C%89_root_%E6%9D%83%E9%99%90%E7%9A%84_Xorg> "Xorg")，您必须启用 DRM ([直接渲染管理器](<https://en.wikipedia.org/wiki/Direct_Rendering_Manager> "wikipedia:Direct Rendering Manager"))[内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")。 

[nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包 560.35.03-5 版本后默认启用 DRM ([Direct Rendering Manager](<https://en.wikipedia.org/wiki/Direct_Rendering_Manager> "wikipedia:Direct Rendering Manager")) [内核级显示模式设置](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "内核级显示模式设置")，如您使用更旧的驱动版本，请为`nvidia_drm`模块设置以下[内核模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")：`modeset=1`。 

您可以使用以下命令验证DRM是否自动启用： 
    
    # cat /sys/module/nvidia_drm/parameters/modeset
    
其应当返回 `Y`。 

**警告：**[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E5%AE%98%E6%96%B9%E6%94%AF%E6%8C%81%E7%9A%84%E5%86%85%E6%A0%B8> "Kernel") 默认启用 `simpledrm`, 如您使用545或更旧版本的NVIDIA驱动，您需要设置内核模块参数 `nvidia_drm.fbdev`。因为当其不被启用时，NVIDIA 驱动程序尝试使用 `efifb` 或 `vesafb` 进行帧缓冲(其无法在`simpledrm`下工作)。

**注意：** 版本 470 之前的 NVIDIA 驱动程序 ( 例如 [nvidia-390xx-dkms](<https://aur.archlinux.org/packages/nvidia-390xx-dkms/>)AUR) 不支持对 XWayland 进行硬件加速，导致非 Wayland 原生应用程序在 Wayland 会话中性能不佳。

####  早启动

对于基本功能，只需添加内核参数就足够了。如果您希望确保驱动能被最早加载，或者遇到了启动问题（例如 `nvidia` 内核模块在[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动后才被加载），可以将 `nvidia`、`nvidia_modeset`、`nvidia_uvm` 和 `nvidia_drm` 添加到 initramfs 中。请参阅[内核模块#早期模块加载](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E6%97%A9%E6%9C%9F%E6%A8%A1%E5%9D%97%E5%8A%A0%E8%BD%BD> "内核模块")以了解如何配置您的 initramfs 生成器。[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")用户可能还需要在每次 [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 驱动程序更新时[重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")映像。请参阅[#Pacman 钩子](<#Pacman_%E9%92%A9%E5%AD%90>)以自动化这些步骤 

##### mkinitcpio

如果使用 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") initramfs，请按照 [mkinitcpio#MODULES](<../zh-cn/Mkinitcpio.html#%E6%A8%A1%E5%9D%97%EF%BC%88MODULES%EF%BC%89> "Mkinitcpio") 添加模块。 

如果你将驱动添加到了 initramfs 中，记得每次更新 [nvidia-open](<https://archlinux.org/packages/?name=nvidia-open>)包 驱动程序后都要运行 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")。请参见 [#pacman hook](<#pacman_hook>) 来自动执行这些步骤。 

##### Booster

如果您使用的是 [Booster](<../zh-cn/Booster.html> "Booster")，请参阅 [Booster#早期加载内核模块](<../zh-cn/Booster.html#%E6%97%A9%E6%9C%9F%E5%8A%A0%E8%BD%BD%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97> "Booster")。 

##### dracut

如果您使用的是 [dracut](<../zh-cn/Dracut.html> "Dracut")，请参阅 [dracut#早期内核模块加载](<../zh-cn/Dracut.html#%E6%97%A9%E6%9C%9F%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E5%8A%A0%E8%BD%BD> "Dracut")。 

####  Pacman 钩子

为了避免更新 NVIDIA 驱动之后忘了更新 [initramfs](<../zh-cn/Arch_boot_process.html#initramfs> "Arch boot process")，你可以使用 [Pacman Hooks](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")： 
    
    /etc/pacman.d/hooks/nvidia.hook
    
    [Trigger]
    Operation=Install
    Operation=Upgrade
    Operation=Remove
    Type=Package
    Target=nvidia-open
    Target=linux
    # Change the linux part above and in the Exec line if a different kernel is used
    # 如果使用不同的内核，请更改上面的 linux 部分和 Exec 行中的内容
    [Action]
    Description=Updating NVIDIA module in initcpio
    Depends=mkinitcpio
    When=PostTransaction
    NeedsTargets
    Exec=/bin/sh -c 'while read -r trg; do case $trg in linux) exit 0; esac; done; /usr/bin/mkinitcpio -P'

务必保证 `Target` 项所设置的软件包与你在前面的安装过程中所使用的相符（例如`nvidia-open-dkms` 或 `nvidia-open-lts` 等）。 

**注意：**`Exec` 那一行看起来非常复杂，是为了避免在 `nvidia-open` 和 `linux` 软件包都发生更新的时候重复运行 `mkinitcpio`。如果你觉得无所谓，可以删掉 `Target=linux` 以及 `NeedsTargets`，然后 `Exec` 就可以简化为 `Exec=/usr/bin/mkinitcpio -P`.

###  硬件加速视频解码

GeForce 8 系列及更新的显卡通过 VDPAU 进行视频硬件解码。Fermi 架构（400、500系列）及更新的显卡支持通过 NVDEC 进行硬件加速解码。参见[硬件视频加速](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration")。 

###  基于 NVENC 的硬件加速视频编码

想要使用 NVENC，则需要安装 `nvidia_uvm` 模块，并在 `/dev` 下创建相关设备节点。 

最新的驱动程序包提供了一个 [udev规则](</wzh/index.php?title=Udev_rule&action=edit&redlink=1> "Udev rule（页面不存在）")，它可以自动创建设备节点，因此不需要进一步的操作。 

如果您使用旧的驱动程序 ( 例如 [nvidia-340xx-dkms](<https://aur.archlinux.org/packages/nvidia-340xx-dkms/>)AUR) ，则需要另外创建设备节点。调用 `nvidia-modprobe` 实用程序会自动创建它们。您可以自己创建 `/etc/udev/rules.d/70-nvidia.rules` 规则来自动运行它 : 
    
    /etc/udev/rules.d/70-nvidia.rules
    
    ACTION=="add", DEVPATH=="/bus/pci/drivers/nvidia", RUN+="/usr/bin/nvidia-modprobe -c 0 -u"

##  Xorg 配置

NVIDIA专有驱动不需要任何 Xorg 服务器配置文件。您可以[启动 X](<../zh-cn/Xorg.html#Running> "Xorg") 来检验没有配置文件的 Xorg 能否正确运行。但是，您可能需要创建配置文件（优先创建`/etc/X11/xorg.conf.d/20-nvidia.conf`而不是`/etc/X11/xorg.conf`）来调整 Xorg 运行时的一些设置。您可以用NVIDIA Xorg 配置工具来生成配置，也可以手动创建它。假如是手动创建的话，它可以是一个最小配置文件(也就是意味着它仅仅把一些基础的选项传给 [Xorg](<../zh-cn/Xorg.html> "Xorg") 服务器)，也可以是包含大量的绕开Xorg 自动发现与预配置选项的设置的文件。 

**提示：** 更多配置项相关内容参见 [NVIDIA/故障排除](<../zh-cn/NVIDIA/%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html> "NVIDIA/故障排除")。

###  自动配置

NVIDIA的软件包已经包含一个自动配置的工具来帮助您创建Xorg服务器配置文件(`xorg.conf`)。您可以通过运行下面的命令来实现自动配置： 
    
    # nvidia-xconfig
    
该命令会自动检测并根据现有硬件的情况创建（或修改）`/etc/X11/xorg.conf`。 

再一次检查您的配置文件`/etc/X11/xorg.conf`中的默认色深、水平同步、垂直刷新和分辨率是否正确。 

### nvidia-settings

[nvidia-settings](<https://archlinux.org/packages/?name=nvidia-settings>)包可以让你通过 CLI 或者图形界面配置很多选项。无参数运行`nvidia-settings`会启动图形界面版本的配置工具，而 CLI 选项参见[nvidia-settings(1)](<https://man.archlinux.org/man/nvidia-settings.1>)。 

你可以以非 root 用户身份使用 CLI/图形界面配置工具，并把设置保存到`~/.nvidia-settings-rc`或使用 _Save to X configuration File_ 按钮来保存到[xorg.conf](<../zh-cn/Xorg.html#Using_xorg.conf> "Xorg")（用于多用户环境）。 

通过以下命令来为当前用户加载 `~/.nvidia-settings-rc`： 
    
    $ nvidia-settings --load-config-only
    
参见 [Autostarting](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting") 来在每次开机的时候自动执行此命令。 

{{注意| 

  * 在保存了`nvidia-settings`的设置变更之后，[Xorg](<../zh-cn/Xorg.html> "Xorg") 可能会无法启动或者启动时崩溃。修改或者删掉生成的`~/.nvidia-settings-rc`及（或）[Xorg](<../zh-cn/Xorg.html> "Xorg") 文件可能能够恢复正常启动。

###  手动配置

有些调整项无法通过 [#自动配置](<#%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AE>) 或 [#nvidia-settings](<#nvidia-settings>) 自动启用，但可以通过修改你的配置文件来进行配置。Xorg服务器需要重新启动以应用这些配置。 

参见 [NVIDIA Accelerated Linux Graphics Driver README and Installation Guide](<https://download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/>) 来了解更多细节及选项。 

####  最简配置

用 root 用户创建一个配置文件`20-nvidia.conf`(或 `/etc/X11/xorg.conf`)： 
    
    /etc/X11/xorg.conf.d/20-nvidia.conf
    
    Section "Device"
       Identifier     "Device0"
       Driver         "nvidia"
       VendorName     "NVIDIA Corporation"
    EndSection
    
####  关闭启动时的 Logo

如果您使用的是旧版驱动( [nvidia-340xx-dkms](<https://aur.archlinux.org/packages/nvidia-340xx-dkms/>)AUR )，您可能希望禁用在 X 启动时显示的 NVIDIA 徽标启动画面。添加`"NoLogo"`选项到`Device`节里： 
    
    Option "NoLogo" "1"
    
####  覆盖显示器侦测

`Device`节下面的`"ConnectedMonitor"`选项允许您覆盖X服务器在启动时的显示器侦测过程，这可能有助于在启动时节约大量时间。可用的选项包括：`"CRT"`用于模拟信号连接，`"DFP"`用于数字显示器，`"TV"`用于电视。 

下面的例子是强制NVIDIA的驱动绕开启动检测并且强制把显示器识别为DFP： 
    
    Option "ConnectedMonitor" "DFP"
    
**注意：** "CRT"适用于所有传输模拟信号的15 pin VGA连接器，包括平板显示器上的VGA接口。"DFP"仅适用于DVI、HDMI和DisplayPort等数字信号连接器。

####  启用亮度控制

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 可能已过时[[1]](<https://lists.archlinux.org/archives/list/aur-requests@lists.archlinux.org/thread/GXJG7D3ALUQKOE2DT4XCL4UXQUFDDSEC/>), 上游软件包看起来也很久没更新了 (在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论)

添加内核参数： 
    
    nvidia.NVreg_RegistryDwords=EnableBrightnessControl=1
    
或者，在`Device`节下添加: 
    
    Option "RegistryDwords" "EnableBrightnessControl=1"
    
如果亮度控制依旧无法生效，请尝试安装[nvidia-bl-dkms](<https://aur.archlinux.org/packages/nvidia-bl-dkms/>)AUR。 

**注意：** 安装 [nvidia-bl-dkms](<https://aur.archlinux.org/packages/nvidia-bl-dkms/>)AUR 会提供 `/sys/class/backlight/nvidia_backlight/` 接口以用于背光亮度控制，但是你的系统可能会继续发送亮度调整信号到 `/sys/class/backlight/acpi_video0/`。 解决方案之一是监视文件变化，例如为 `acpi_video0/brightness` 添加 _inotifywait_ 并将变化翻译并写入 `nvidia_backlight/brightness`。 参见 [Backlight#sysfs modified but no brightness change](<../zh-cn/%E8%83%8C%E5%85%89.html#sysfs_modified_but_no_brightness_change> "Backlight").

####  启用 SLI

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 从版本 455.23.04 开始，某些 SLI 模式不再受支持。 (在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论)

**警告：** 自 GTX 10xx系列（1080、1070、1060等等）开始，仅 2 路 SLI 是受支持的。3 路或 4 路 SLI 或许能够在 CUDA/OpenCL 应用上使用，但是会让几乎所有 OpenGL 应用崩溃。

根据NVIDIA驱动的 [README](<https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/xconfigoptions.html#SLI>) 附录 B: _这个选项可以在支持的配置中控制 SLI 渲染的相关配置。_ 一个 _支持的配置_ 是指有一块 SLI 认证的主板以及 2 或者 3 个 SLI认 证的 GeForce GPU 的计算机。 

您可以用`lspci`查找第一个 GPU 的 PCI 总线 ID： 
    
    # lspci -d ::03xx
    
    00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor Graphics Controller (rev 09)
    03:00.0 VGA compatible controller: NVIDIA Corporation GK107 [GeForce GTX 650] (rev a1)
    04:00.0 VGA compatible controller: NVIDIA Corporation GK107 [GeForce GTX 650] (rev a1)
    08:00.0 3D controller: NVIDIA Corporation GM108GLM [Quadro K620M / Quadro M500M] (rev a2)
    
在`Device`节下添加 BusID（例如前面例子里的那 3 个）： 
    
    BusID "PCI:3:0:0"
    
**注意：** 这个格式很重要。BusID的值必须指定为`"PCI:<BusID>:0:0"`的格式。

根据需要的 SLI 渲染模式来添加值到`Screen`节下面： 
    
    Option "SLI" "AA"
    
下表列出了可用的渲染模式。 

Value | Behavior   
---|---  
0, no, off, false, Single | 渲染时仅使用单GPU。   
1, yes, on, true, Auto | 启用SLI并让驱动自动选择合适的渲染模式。   
AFR | 启用SLI并使用交替帧渲染模式。   
SFR | 启用SLI并使用分割帧渲染模式。   
AA | 启用SLI和使用SLI抗锯齿。与全场景反锯齿结合使用以改善视觉效果。   
  
另外，您可以使用 `nvidia-xconfig` 实用工具来将这些变动写入`xorg.conf`： 
    
    # nvidia-xconfig --busid=PCI:3:0:0 --sli=AA
    
从shell来验证一下SLI是否被启用： 
    
    $ nvidia-settings -q all | grep SLIMode
    
       Attribute 'SLIMode' (arch:0.0): AA
        'SLIMode' is a string attribute.
        'SLIMode' is a read-only attribute.
        'SLIMode' can use the following target types: X Screen.
    
**警告：** 启用 SLI 之后，你的系统可能会在启动 xorg 的时候假死、没有反应。建议你在重启之前禁用你的显示管理器。

如果这个配置没有效果，你可能需要使用 `nvidia-settings` 提供的PCI总线ID： 
    
    $ nvidia-settings -q all | grep -i pcibus
    
    Attribute 'PCIBus' (host:0[gpu:0]): 101.
      'PCIBus' is an integer attribute.
      'PCIBus' is a read-only attribute.
      'PCIBus' can use the following target types: GPU, SDI Input Device.
    Attribute 'PCIBus' (host:0[gpu:1]): 23.
      'PCIBus' is an integer attribute.
      'PCIBus' is a read-only attribute.
      'PCIBus' can use the following target types: GPU, SDI Input Device.
    
并将 xorg.d 配置中的 PrimaryGPU 选项注释掉： 
    
    /usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
    
    ...
    
    Section "OutputClass"
    ...
        # Option "PrimaryGPU" "yes"
    ...
    
使用后面这个配置或许会顺便解决任何图形界面启动问题。 

###  多台显示器

参见[Multihead](<../zh-cn/%E5%A4%9A%E6%98%BE%E7%A4%BA%E5%99%A8.html> "Multihead")以获取更多信息。 

####  使用 nvidia-settings

[nvidia-settings](<#nvidia-settings>) 工具可以配置多个监视器。 

对于 CLI 配置，首先运行以下命令获取 `CurrentMetaMode`: 
    
    $ nvidia-settings -q CurrentMetaMode
    
    Attribute 'CurrentMetaMode' (hostnmae:0.0): id=50, switchable=no, source=nv-control :: DPY-1: 2880x1620 @2880x1620 +0+0 {ViewPortIn=2880x1620, ViewPortOut=2880x1620+0+0}

将 `::` 之后的所有内容保存到属性末尾（在本例中为：`DPY-1: 2880x1620 @2880x1620 +0+0 {ViewPortIn=2880x1620, ViewPortOut=2880x1620+0+0}`），并使用 `nvidia-settings --assign "CurrentMetaMode=_your_meta_mode_ "` 重新配置显示器。 

**提示：** 您可以为所使用的不同监视器和分辨率配置创建 shell alias。

#### ConnectedMonitor

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** `"TwinView"选项`已在 302.07 版本移除，且TwinView 功能现已默认启用 (在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论)

如果驱动程序没有正确检测到第二个监视器，则可以使用 ConnectedMonitor 强制设置。 
    
    /etc/X11/xorg.conf
    
    Section "Monitor"
        Identifier     "Monitor1"
        VendorName     "Panasonic"
        ModelName      "Panasonic MICRON 2100Ex"
        HorizSync       30.0 - 121.0 # this monitor has incorrect EDID, hence Option "UseEDIDFreqs" "false"
        VertRefresh     50.0 - 160.0
        Option         "DPMS"
    EndSection
    
    Section "Monitor"
        Identifier     "Monitor2"
        VendorName     "Gateway"
        ModelName      "GatewayVX1120"
        HorizSync       30.0 - 121.0
        VertRefresh     50.0 - 160.0
        Option         "DPMS"
    EndSection
    
    Section "Device"
        Identifier     "Device1"
        Driver         "nvidia"
        Option         "NoLogo"
        Option         "UseEDIDFreqs" "false"
        Option         "ConnectedMonitor" "CRT,CRT"
        VendorName     "NVIDIA Corporation"
        BoardName      "GeForce 6200 LE"
        BusID          "PCI:3:0:0"
        Screen          0
    EndSection
    
    Section "Device"
        Identifier     "Device2"
        Driver         "nvidia"
        Option         "NoLogo"
        Option         "UseEDIDFreqs" "false"
        Option         "ConnectedMonitor" "CRT,CRT"
        VendorName     "NVIDIA Corporation"
        BoardName      "GeForce 6200 LE"
        BusID          "PCI:3:0:0"
        Screen          1
    EndSection
    
通过添加带有 `Screen` 选项的重复设备配置，能让 X 在一张显卡上使用两台显示器而不需要 `TwinView`。注意，`nvidia-settings` 将去掉您添加的任何 `ConnectedMonitor` 选项。 

#### TwinView

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** `"TwinView"选项`已在 302.07 版本移除，且双屏支持现已默认启用 (在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论)

若你想用一个大屏幕,而不是两个屏幕.将`TwinView`设为`1`。只有所有显示器都接到同一张显卡上时，TwinView 才能工作。 
    
    Option "TwinView" "1"
    
示例配置： 
    
    /etc/X11/xorg.conf.d/10-monitor.conf
    
    Section "ServerLayout"
        Identifier     "TwinLayout"
        Screen         0 "metaScreen" 0 0
    EndSection
    
    Section "Monitor"
        Identifier     "Monitor0"
        Option         "Enable" "true"
    EndSection
    
    Section "Monitor"
        Identifier     "Monitor1"
        Option         "Enable" "true"
    EndSection
    
    Section "Device"
        Identifier     "Card0"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
    
        #refer to the link below for more information on each of the following options.
        Option         "HorizSync"          "DFP-0: 28-33; DFP-1: 28-33"
        Option         "VertRefresh"        "DFP-0: 43-73; DFP-1: 43-73"
        Option         "MetaModes"          "1920x1080, 1920x1080"
        Option         "ConnectedMonitor"   "DFP-0, DFP-1"
        Option         "MetaModeOrientation" "DFP-1 LeftOf DFP-0"
    EndSection
    
    Section "Screen"
        Identifier     "metaScreen"
        Device         "Card0"
        Monitor        "Monitor0"
        DefaultDepth    24
        Option         "TwinView" "True"
        SubSection "Display"
            Modes          "1920x1080"
        EndSubSection
    EndSection
    
另请参考[设备选项信息](<https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/configtwinview.html>)

如果您有多个支持 SLI 的显卡，则可以把多个显示器接到不同的显卡上。“MetaModes”选项与 SLI Mosaic 模式配合使用可实现此功能。下面是一个适用于上述情况的配置，它可以完美运行 [GNOME](<../zh-cn/GNOME.html> "GNOME")。 

    /etc/X11/xorg.conf.d/10-monitor.conf
    
    Section "Device"
            Identifier      "Card A"
            Driver          "nvidia"
            BusID           "PCI:1:00:0"
    EndSection
    
    Section "Device"
            Identifier      "Card B"
            Driver          "nvidia"
            BusID           "PCI:2:00:0"
    EndSection
    
    Section "Monitor"
            Identifier      "Right Monitor"
    EndSection
    
    Section "Monitor"
            Identifier      "Left Monitor"
    EndSection
    
    Section "Screen"
            Identifier      "Right Screen"
            Device          "Card A"
            Monitor         "Right Monitor"
            DefaultDepth    24
            Option          "SLI" "Mosaic"
            Option          "Stereo" "0"
            Option          "BaseMosaic" "True"
            Option          "MetaModes" "GPU-0.DFP-0: 1920x1200+4480+0, GPU-1.DFP-0:1920x1200+0+0"
            SubSection      "Display"
                            Depth           24
            EndSubSection
    EndSection
    
    Section "Screen"
            Identifier      "Left Screen"
            Device          "Card B"
            Monitor         "Left Monitor"
            DefaultDepth    24
            Option          "SLI" "Mosaic"
            Option          "Stereo" "0"
            Option          "BaseMosaic" "True"
            Option          "MetaModes" "GPU-0.DFP-0: 1920x1200+4480+0, GPU-1.DFP-0:1920x1200+0+0"
            SubSection      "Display"
                            Depth           24
            EndSubSection
    EndSection
    
    Section "ServerLayout"
            Identifier      "Default"
            Screen 0        "Right Screen" 0 0
            Option          "Xinerama" "0"
    EndSection
    
####  对于同时拥有AMD核显和NVIDIA独立显卡的用户

由于NVIDIA自动生成的xorg.conf配置默认不包含AMDGPU这会导致双屏用户其中一个屏幕不能显示 需要先进行[自动配置](<#%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AE>)，然后在`/etc/X11/xorg.conf.d/`下新建`20-amdgpu.conf`： 
    
    Section "Device"
         Identifier "AMD"
         Driver "amdgpu"
    EndSection 
    
#####  TwinView 和垂直同步

如果您正在使用 TwinView 和垂直同步 (**nvidia-settings** 中的 _Sync to VBlank_ 选项 ) ，您将注意到只有一个屏幕能正常同步，除非您有两个相同的显示器。虽然 **nvidia-settings** 确实提供了一个选项来更改垂直同步的屏幕 (**Sync to this display device** 选项 ) ，但这并不总是有效。一个解决方案是在启动时添加以下环境变量，例如在 `/etc/profile` 中附加 : 
    
    export __GL_SYNC_TO_VBLANK=1
    export __GL_SYNC_DISPLAY_DEVICE=DFP-0
    export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-0
    
你可以把 `DFP-0` 改为你首选要同步的屏幕 (`DFP-0` 是DVI接口， `CRT-0` 是VGA接口). 您可以从 "X Server XVideoSettings" 部分的 **nvidia-settings** 中找到显示器的标识符。 

#####  用 TwinView 玩游戏

如果你想在使用 TwinView 时玩全屏游戏，你会注意到游戏将两个屏幕识别为一个大屏幕。虽然这理论上没问题（因为虚拟 X 屏幕实际上是屏幕大小的总和），但您可能不希望同时在两个屏幕上显示。 

要纠正 SDL 的这种行为，请尝试 : 
    
    export SDL_VIDEO_FULLSCREEN_HEAD=1
    
对于 OpenGL，向 xorg.conf 中添加适当的 Metamode 并重新启动 X: 
    
    Option "Metamodes" "1680x1050,1680x1050; 1280x1024,1280x1024; 1680x1050,NULL; 1280x1024,NULL;"
    
另一种可以单独使用或与上述方法结合使用的方法是[在单独的 X 服务器中启动游戏](<../zh-cn/%E6%B8%B8%E6%88%8F.html#Starting_games_in_a_separate_X_server> "Gaming")。 

####  马赛克拼接模式

马赛克模式是使用多个显示器进行跨显卡合成的唯一方式。您的窗口管理器不一定能区分不同的显示器。马赛克模式需要一个有效的 SLI 配置。即使使用基本模式而不使用 SLI，GPU 仍然必须支持 / 兼容 SLI。 

#####  基本马赛克拼接模式

Base Mosaic 模式适用于任何 Geforce 8000 系列或更高版本的 GPU。无法从 nvidia-setting GUI 中启用它。您必须使用 _nvidia-xconfig_ 命令行程序或手动编辑 `xorg.conf`。必须指定元模式。以下是 2x2 配置中四个 DFP 的示例，每个 DFP 以 1920x1024 运行，两个 DFP 连接到两个显卡： 
    
    # nvidia-xconfig --base-mosaic --metamodes="GPU-0.DFP-0: 1920x1024+0+0, GPU-0.DFP-1: 1920x1024+1920+0, GPU-1.DFP-0: 1920x1024+0+1024, GPU-1.DFP-1: 1920x1024+1920+1024"
    
**注意：** 虽然文档列出了 2x2 的监视器配置，在基础马赛克模式下 [GeForce 显卡被人为限制了只能使用3个显示器](<https://forums.developer.nvidia.com/t/basemosaic-v295-vs-v310-vs-v325-only-up-to-three-screens/30583#3954733>)。Quadro 卡支持 3 个以上的显示器。截至 2014 年 9 月，Windows 驱动程序已取消了这一人为限制，但仍保留在 Linux 驱动程序中。

#####  SLI 马赛克拼接模式

如果您有 SLI 配置，并且每个 GPU 都是 Quadro FX 5800、Quadro Fermi 或更新型号，那么您可以使用 SLI 马赛克模式。可以从 nvidia-settings GUI 内或从命令行通过以下方式启用： 
    
    # nvidia-xconfig --sli=Mosaic --metamodes="GPU-0.DFP-0: 1920x1024+0+0, GPU-0.DFP-1: 1920x1024+1920+0, GPU-1.DFP-0: 1920x1024+0+1024, GPU-1.DFP-1: 1920x1024+1920+1024"
    
##  Wayland配置

关于 XWayland，请参阅 [Wayland#Xwayland](<../zh-cn/Wayland.html#Xwayland> "Wayland")。 

有关进一步的配置选项，请查看相应[混成器](<../zh-cn/Wayland.html#%E6%B7%B7%E6%88%90%E5%99%A8> "Wayland")的 wiki 页面或文档。 

**注意：** 在驱动程序版本 555.xx 之前，或者在使用不支持通过`linux-drm-syncobj-v1`协议进行显式同步的混成器时，NVIDIA 驱动程序可能会出现严重问题，表现为闪烁、帧顺序错乱等，这在原生 Wayland 或 Xwayland 应用程序中均会发生。

###  配置

`nvidia_drm` 模块有如下两个可选的内核参数。在使用560.35.03-5或更高版本的[nvidia-utils](<https://archlinux.org/packages/?name=nvidia-utils>)包时，这两个参数默认已[启用](<https://gitlab.archlinux.org/archlinux/packaging/packages/nvidia-utils/-/blob/3b439109/PKGBUILD#L60>)

#### modeset

使用Wayland时，`modeset`必须被启用。560.35.03-5或更高版本的驱动已经默认启用了这一设置。 

如您使用的是较旧的驱动，您可能需手动启用 `modeset`，请参阅 [#DRM 内核级显示模式设置](<#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE>)和 [Wayland系统需求](<../zh-cn/Wayland.html#%E7%B3%BB%E7%BB%9F%E9%9C%80%E6%B1%82> "Wayland")进行配置。 

#### fbdev

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 截至[linux](<https://archlinux.org/packages/?name=linux>)包 6.14.2 和570.133.07 版本专有驱动，禁用 fbdev 后 Wayland 运行良好，且`cat`命令可能返回`N`，因此本节内容仅适用于较旧版本的驱动程序 (在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论)

启用`fbdev`对于某些 Wayland 配置是必要的。 

在Linux 6.11以及更高版本上这是一个硬性需求，但目前尚不清楚这是预期行为还是一个错误[[2]](<https://forums.developer.nvidia.com/t/drm-fbdev-wayland-presentation-support-with-linux-kernel-6-11-and-above/307920>)

您可以参考 [#DRM 内核级显示模式设置](<#DRM_%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE>)中的方法进行设置。其区别在于验证其是否打开时，您需要执行： 
    
    # cat /sys/module/nvidia_drm/parameters/fbdev
    
如果没有成功设置，其将返回缺少文件错误，而不是`N`。 

###  休眠支持

Wayland 的休眠可能比 X 更容易受到默认设置的影响，详细信息请参见 [Tips and tricks#Preserve video memory after suspend](</wzh/index.php?title=Tips_and_tricks&action=edit&redlink=1> "Tips and tricks（页面不存在）")。 

如您使用 GDM，请参考 [GDM#Wayland 与 NVIDIA 专有驱动](<../zh-cn/GDM.html#Wayland_%E4%B8%8E_NVIDIA_%E4%B8%93%E6%9C%89%E9%A9%B1%E5%8A%A8> "GDM")。 

### nvidia-application-profiles-rc.d

某些 Wayland 合成器在默认情况下会占用大量的 VRAM，您可以通过对它们的进程名称应用 [GLVidHeapReuseRatio](<https://www.nvidia.com/en-us/drivers/details/237587/>) 应用程序配置键来解决这个问题。例如，[niri](<../zh-cn/Niri.html> "Niri") 用户可通过以下方式释放 ~2.5GiB 的显存占用： 
    
    /etc/nvidia/nvidia-application-profiles-rc.d/50-limit-free-buffer-pool-in-wayland-compositors.json
    
    {
        "rules": [
            {
                "pattern": {
                    "feature": "procname",
                    "matches": "niri"
                },
                "profile": "Limit free buffer pool on Wayland compositors"
            }
        ],
        "profiles": [
            {
                "name": "Limit free buffer pool on Wayland compositors",
                "settings": [
                    {
                        "key": "GLVidHeapReuseRatio",
                        "value": 0
                    }
                ]
            }
        ]
    }

## NVswitch

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 需要多个语法改进，以及关于 fabric manager 的部分应当制作为一个 AUR 包。（在[Talk:NVIDIA](<../zh-cn/Talk:NVIDIA.html>)讨论）

对于具有 NVswitch 的系统，例如 AWS 上的 H100x8： 

  * 安装 nvidia-fabricmanager

  * 安装所有fabric manager所需要的内核模块

使用 fabricmanager 时，pytorch 会报告未找到 GPU。 

安装 fabric manager: 

  1. 从[此处](<https://developer.download.nvidia.com/compute/cuda/redist/fabricmanager/linux-x86_64/>)下载tarball。

  1. 版本 555.42.02 运作良好

  1. 修改 sbin/fm_run_package_installer.sh 中的安装脚本以修复安装文件路径

要获取匹配的内核驱动程序： 

  1. 克隆 nvidia-beta-dkms 和 nvidia-utils-beta 的 AUR

  1. 将 PKGBUILD 更改为使用版本 555.42.02

  1. 构建安装并重启

随后运行 `systemctl enable nvidia-fabricmanager` 以及 `systemctl start nvidia-fabricmanager`，现在 pytorch 应当能正确识别到GPU。 

##  提示和技巧

参考 [NVIDIA/提示和技巧](<../zh-cn/NVIDIA/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html> "NVIDIA/提示和技巧"). 

##  故障排除

参考 [NVIDIA/故障排除](<../zh-cn/NVIDIA/%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html> "NVIDIA/故障排除"). 

##  另请参见

  * [Current graphics driver releases in official NVIDIA Forum](<https://forums.developer.nvidia.com/t/current-graphics-driver-releases/28500>)
  * [NVIDIA Developers Forum - Linux Subforum](<https://forums.developer.nvidia.com/c/gpu-graphics/linux/148>)
