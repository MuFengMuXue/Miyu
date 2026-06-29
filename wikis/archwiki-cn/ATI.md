**翻译状态：**

  * 本文（或部分内容）译自 [ATI](<https://wiki.archlinux.org/title/ATI> "arch:ATI")，最近一次同步于 2023-01-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/ATI?diff=0&oldid=764421>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ATI_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU")
  * [Vulkan](<../zh-cn/Vulkan.html> "Vulkan")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")

本文主要介绍较旧的显卡使用的开源的 **ATI** /[Radeon](<https://wiki.freedesktop.org/xorg/radeon/>) 驱动. 

##  选择正确的驱动

要选择正确的驱动，请参考[Xorg#AMD](<../zh-cn/Xorg.html#AMD> "Xorg")。本文主要介绍 **ATI** 。 

如果你不确定该用哪种，请先试一试开源版的。开源驱动能满足大多数的需要，而且，一般来说遇到的麻烦也更少些。查看现在功能开发进展情况可访问[功能矩阵](<https://www.x.org/wiki/RadeonFeature>)。 

[这个页面](<https://www.x.org/wiki/RadeonFeature/#index5h2>)可以将市场名(例如 Radeon HD4330) 映射到芯片组名(例如 R700). 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [mesa](<https://archlinux.org/packages/?name=mesa>)包，它提供 DRI 和 3D 加速。 

  * 若需要x86_64下的32位支持,可以从 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 安装 [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包.
  * 要使用 [Xorg](<../zh-cn/Xorg.html> "Xorg") 2D 加速 DDX 驱动，请安装软件包 [xf86-video-ati](<https://archlinux.org/packages/?name=xf86-video-ati>)包.

[加速视频解码](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html#ATI/AMD> "硬件视频加速")方面，[libva-mesa-driver](<https://archlinux.org/packages/?name=libva-mesa-driver>)包 和 [lib32-libva-mesa-driver](<https://archlinux.org/packages/?name=lib32-libva-mesa-driver>)包提供了VA-API, [mesa-vdpau](<https://archlinux.org/packages/?name=mesa-vdpau>)包 和 [lib32-mesa-vdpau](<https://archlinux.org/packages/?name=lib32-mesa-vdpau>)包 提供 VDPAU。 

##  载入

参考 [Kernel mode setting#Early KMS start](<../zh-cn/Kernel_mode_setting.html#Early_KMS_start> "Kernel mode setting")。 

radeon模块应该在启动时被正常载入. 

要是没有的话... 

  * 确保[内核参数](</wzh/index.php?title=%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "内核参数 \(简体中文\)（页面不存在）")中**没有** `nomodeset` 或 `vga=`,因为现在 radeon 需要[内核级显示模式设置](<../zh-cn/Kernel_mode_setting.html> "Kernel mode setting")。
  * 另外，确保 radeon 模块不在内核模块[黑名单](<../zh-cn/Kernel_modules.html#Blacklisting> "Kernel modules")中。

###  KMS早启动

参考 [Kernel mode setting#KMS 早启动](<../zh-cn/Kernel_mode_setting.html#KMS_%E6%97%A9%E5%90%AF%E5%8A%A8> "Kernel mode setting")

##  配置

Xorg 会自动装入驱动并通过 EDID 获得显示器分辨率，只有性能优化时才需要额外配置。 

如果要手动配置，请添加文件 `/etc/X11/xorg.conf.d/20-radeon.conf`, 并加入： 
    
    Section "OutputClass"
        Identifier "Radeon"
        MatchDriver "radeon"
        Driver "radeon"
    EndSection
    
通过此段可以调整显卡的设置。 

##  性能调整

###  启动视频加速

参见[Hardware video acceleration](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration")。 

###  图形工具

  * **radeon-profile** — 显示 Radeon 显卡的 Qt 应用程序。

     <https://github.com/marazmista/radeon-profile> || [radeon-profile-git](<https://aur.archlinux.org/packages/radeon-profile-git/>)AUR

  * **CoreCtrl** — 流行的通用 GPU/CPU 控制器，高级用法请参考 [设置](<https://gitlab.com/corectrl/corectrl/-/wikis/Setup>) 页面。

     <https://gitlab.com/corectrl/corectrl> || [corectrl](<https://archlinux.org/packages/?name=corectrl>)包

###  驱动配置

下面这些选项属于`/etc/X11/xorg.conf.d/**20-radeon.conf**`. 

请在应用驱动选项之前先阅读 [radeon(4)](<https://man.archlinux.org/man/radeon.4>) 和 [RadeonFeature](<https://www.x.org/wiki/RadeonFeature/#index4h2>)。 

**Acceleration architecture** ; Glamor是一种使用OpenGL的 2D加速方式，适用于R300及以上显卡驱动。 自xf86-video-ati版本1:7.2.0-1后, 在radeonsi(南方群岛系列 和 superior GFX 显卡)上glamor默认启用; 在其他显卡默认使用 EXA. 
    
    Option "AccelMethod" "glamor"
    
使用 Glamor 加速方式时可以启用 **ShadowPrimary** 选项，它将启用一个被称为 "shadow primary" 的缓冲区来供CPU快速存取像素信息，并给每个显示控制器 (CRTC) 分离出单独的 scanout 缓冲区。这将提升某些 2D 工作的性能，但可能会降低其他（比如3D）工作的性能。 
    
    Option "ShadowPrimary" "on"
    
**ColorTiling** 和 **ColorTiling2D** 是绝对安全的,并且默认被启用. 大多数用户能注意到性能的提升,但是这个功能R200及更早的显卡不支持. 早的显卡虽可以启用,但是工作负担转移到了cpu上 
    
    Option "ColorTiling" "on"
    Option "ColorTiling2D" "on"
    
**DRI3** 默认是启用的，老卡默认使用 DRI2， 要切换到 DRI3： 
    
    Option "DRI" "3"
    
**TearFree** 使用硬件的 flipping mechanism 机制来防止撕裂。当前启用这个选项会禁用 "EnablePageFlip" 选项。 
    
    Option "TearFree" "on"
    
**EXAVSync** 选项仅在使用 EXA 加速方式时有效，它通过stalling the engine until the display controller has passed the destination region来避免撕裂。这将导致性能下降，并已知在某些芯片上导致不稳定。 
    
    Option "EXAVSync" "yes"
    
下面是一个简单的 `/etc/X11/xorg.conf.d/**20-radeon.conf**` 配置文件示例： 
    
    Section "OutputClass"
            Identifier  "Radeon"
            Driver "radeon"
            MatchDriver "radeon"
            Option "AccelMethod" "glamor"
            Option "DRI" "3"
            Option "TearFree" "on"
            Option "ColorTiling" "on"
            Option "ColorTiling2D" "on"
    EndSection
    
**提示：**[driconf](<https://aur.archlinux.org/packages/driconf/>)AUR 是一个可以修改诸多设置的小工具，如 vsync, anisotropic filtering, texture compression 等。它还有一些程序（比如Goole Earth）需要的"disable Low Impact fallback"功能。

###  内核参数

**提示：** 你也许想用 `systool` 来调试新的参数，参见[这里](<../zh-cn/Kernel_module.html#%E8%8E%B7%E5%8F%96%E4%BF%A1%E6%81%AF> "Kernel module")。

如果 **gartsize** 没有被自动检测到，请添加 `radeon.gartsize=32` 到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")来手动定义它。 

**注意：** 对于新的AMD显卡不再需要设置这个参数： 
    
    [drm] Detected VRAM RAM=2048M, BAR=256M
    [drm] radeon: 2048M of VRAM memory ready
    [drm] radeon: 2048M of GTT memory ready.
    
重启后生效。 

####  关闭 PCIE 2.0

从3.6版内核开始，radeon里PCIE 2.0选项默认启用。 

对一些主板可能不稳定，可以向[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")添加 `radeon.pcie_gen2=0` 来关闭。 

参考 [Phoronix 文章](<https://www.phoronix.com/scan.php?page=article&item=amd_pcie_gen2&num=1>)

### Gallium HUD

radeon 驱动支持激活一个HUD，来显示透明的图像及文字于正在渲染的程序（如游戏）之上。可以显示当前帧率，每个CPU核心负载或者CPU负载平均值。这个HUD受 GALLIUM_HUD 环境变量控制，可以添加一些参数如： 

  * "fps" - 显示当前帧率
  * "cpu" - 显示平均CPU负载
  * "cpu0" - 显示第一个CPU核心负载
  * "cpu0+cpu1" - 显示前两个CPU核心负载
  * "draw-calls" - 显示一个物体的每个材质被显示到屏幕上多少次(displays how many times each material in an object is drawn to the screen）
  * "requested-VRAM" - 显示GPU的VRAM使用量
  * "pixels-rendered" - 显示正在显示的像素计数

关于参数的完整列表以及操作GALLIUM_HUD的一些注意事项，你可以添加"help"参数运行一个简单程序（如glxgears）来查看相应的终端输出。 
    
    # GALLIUM_HUD="help" glxgears
    
更多信息参见[邮件列表页面](<https://lists.freedesktop.org/archives/mesa-dev/2013-March/036586.html>)或[这篇博客](<https://kparal.wordpress.com/2014/03/03/fraps-like-fps-overlay-for-linux/>). 

##  混合交火

这是一项通常在配备了双显卡——一块比较节能（比如Intel的核芯显卡），另一块为高性能、高能耗（Radeon或NVIDIA）的笔记本上启用的特性。有两种方法可以启用它： 

  * 如果不需要运行很吃GPU的程序，可以禁用独立显卡（参见[Ubuntu wiki](<https://help.ubuntu.com/community/HybridGraphics#Using_vga_switcheroo>) ）： 
        
        # echo OFF > /sys/kernel/debug/vgaswitcheroo/switch

。
  * [PRIME](<../zh-cn/PRIME.html> "PRIME")是在Linux系统中使用双显卡切换的正确方式，但仍然需要用户进行大量手动设置。

##  节能

**注意：** 所有vbios中包含有适当电源状态表的显卡芯片（R1xx 及更新的）都支持电源管理。"dpm"仅在 R6xx 以及更新的芯片上被支持。

开源驱动的节电功能默认关闭,需要可手动启用. 

三种方法可供选择: 

  1. [dpm](<#%E5%8A%A8%E6%80%81%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86>)(3.13内核后默认启用)
  2. [dynpm](<#%E5%8A%A8%E6%80%81%E9%A2%91%E7%8E%87%E8%B0%83%E6%95%B4>)
  3. [profile](<#%E5%9F%BA%E4%BA%8E%E8%AE%A1%E5%88%92%E7%9A%84%E9%A2%91%E7%8E%87%E8%B0%83%E6%95%B4>)

详见 <https://www.x.org/wiki/RadeonFeature/#index3h2> . 

###  动态电源管理

从3.13内核开始,在[很多 AMD Radeon 设备](<https://kernelnewbies.org/Linux_3.13#head-f95c198f6fdc7defe36f470dc8369cf0e16898df>)上 DPM 默认启用。如果要禁用可加入参数 `radeon.dpm=0` 到[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

**提示：** DPM 可以支持 R6xx，但是在内核里默认没有启用，仅 R7xx 及之后的显卡才默认启用. 在内核参数中加入 `radeon.dpm=1` 可以启用 dpm.

不像[dynpm](<#%E5%8A%A8%E6%80%81%E9%A2%91%E7%8E%87%E8%B0%83%E6%95%B4>)，“dpm"方式根据GPU负载情况动态调整时钟频率和电压，同时它会启用频率和电压门控. 

dpm有3种模式可选: 

  * `battery` 最节能
  * `balanced` 默认
  * `performance` 最佳性能

可以通过sysfs来更改dpm的模式,如下: 
    
    # echo battery > /sys/class/drm/card0/device/power_dpm_state
    
你也许想要强制显卡工作在某一性能等级下: 

  * `auto` 默认; 使用当前dpm模式限定的所有性能等级
  * `low` 强制在最低性能
  * `high` 强制在最高性能

    # echo low > /sys/class/drm/card0/device/power_dpm_force_performance_level
    
####  命令行工具

  * [radcard](<https://github.com/superjamie/snippets/blob/master/radcard>) \- 一个获取/调整 DPM 电源状态与级别的脚本。

###  老方法

####  动态频率调整

此方法根据GPU负载自动改变时钟频率，所以GPU忙碌时显示性能提高，空闲时降低。自动变频试图在垂直消隐期间进行，但由于变频函数可能在周期内无法完成，这种方法可能导致显示闪烁。因此，动态调整只能在单显示器下正常工作。 

可以通过以下命令启用： 
    
    # echo dynpm > /sys/class/drm/card0/device/power_method
    
####  基于计划的频率调整

该方法允许你选择5种不同的计划。主要来说,不同的计划最终都改变GPU时钟频率和电压。这种方式不同于积极方式,但更稳定,少闪屏,而且可用于多显示器环境 

要激活此方法，可运行以下命令： 
    
    # echo profile > /sys/class/drm/card0/device/power_method
    
可选的计划： 

  * `default` 使用默认时钟频率，不改变电源状态。这是默认启用的计划。
  * `auto` 根据系统是否使用电池，在电源状态 `mid` 和 `high` 间自动切换
  * `low` 强制GPU运行于`low`电源状态.注意`low`在某些笔记本上可能导致显示问题, 如`auto` 计划在显示器关闭时只选中`low`.(Note that `low` can cause display problems on some laptops, which is why `auto` only uses `low` when monitors are off. ) 在其他计划中,当显示器进入节能状态时,将自动切换为 `low` 计划
  * `mid` 强制GPU运行于`mid`电源状态.
  * `high` 强制GPU运行于`high`电源状态.

例如，我们可以激活`low` 计划(你可以根据需要替换为上述其他计划): 
    
    # echo low > /sys/class/drm/card0/device/power_profile
    
####  永久配置

上述方法不是永久性的，系统重启后将丢失。为了让它一直有效，可以使用[udev](<../zh-cn/Udev.html> "Udev")规则, 例如设置基于计划的频率调整 : 
    
    /etc/udev/rules.d/30-radeon-pm.rules
    
    KERNEL=="dri/card0", SUBSYSTEM=="drm", DRIVERS=="radeon", ATTR{device/power_method}="profile", ATTR{device/power_profile}="low"
    
**注意：** 如果上述规则失效，你可以试试删除 `dri/` 前辍.

KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="radeon", ATTR{device/power_method}="profile", 

As another example, [dynamic power management](<#Dynamic_power_management>) can be permanently forced to a certain performance level: 
    
    /etc/udev/rules.d/30-radeon-pm.rules
    
    KERNEL=="dri/card0", SUBSYSTEM=="drm", DRIVERS=="radeon", ATTR{device/power_dpm_force_performance_level}="high"

To determine the `KERNEL` name, execute: 
    
    $ udevadm info --attribute-walk /sys/class/drm/card0 | grep "KERNEL="
    
###  其它

要查看当前GPU频率，可以运行如下命令，你可以看到类似如下输出： 
    
    # cat /sys/kernel/debug/dri/0/radeon_pm_info
    
      state: PM_STATE_ENABLED
      default engine clock: 300000 kHz
      current engine clock: 300720 kHz
      default memory clock: 200000 kHz
    
It depends on which GPU line yours is, however. Along with the radeon driver versions, kernel versions, etc. So it may not have much/any voltage regulation at all. 

Thermal sensors are implemented via external i2c chips or via the internal thermal sensor (rv6xx-evergreen only). To get the temperature on asics that use i2c chips, you need to load the appropriate hwmon driver for the sensor used on your board (lm63, lm64, etc.). The drm will attempt to load the appropriate hwmon driver. On boards that use the internal thermal sensor, the drm will set up the hwmon interface automatically. When the appropriate driver is loaded, the temperatures can be accessed via [lm_sensors](<../zh-cn/Lm_sensors.html> "Lm sensors") tools or via sysfs in `/sys/class/hwmon`. 

##  风扇速度

即使上述省电功能应该能很好调整风扇速度，一些显卡在空闲状态时仍然太吵了。这时，如果你的风扇支持的话，你可以尝试手动改变风扇速度。 

**注意：**

  * 请谨记以下方法会将风扇速度设置为固定值，它不会随着 gpu 的压力而调整，所以在高负荷工作时这有可能导致过热。
  * 设置低于标准的数值时最好检查你的 gpu 温度。

要控制风扇速度，请参考 [Fan speed control#AMDGPU sysfs fan control](<../zh-cn/Fan_speed_control.html#AMDGPU_sysfs_fan_control> "Fan speed control") (amdgpu 和 radeon 使用相同的控制方式)。 

如果要让此成为永久设置，使用 [#永久配置](<#%E6%B0%B8%E4%B9%85%E9%85%8D%E7%BD%AE>)。 

如果固定值不符合你的期望，还可以自定义为按一个温度/风扇速度曲线来调整，比如写一个脚本，来根据当前温度 (/sys/class/drm/card0/device/hwmon/hwmon0/temp1_input) 设置风扇速度，最好还能设置为温度变化后延迟调整。这里有一个图形界面的工具：[radeon-profile-git](<https://aur.archlinux.org/packages/radeon-profile-git/>)AUR。 

##  TV输出

首先，检查你有S-video输出：`xrandr`应该会给你类似如下的结果： 
    
    Screen 0: minimum 320x200, current 1024x768, maximum 1280x1200
    ...
    S-video disconnected (normal left inverted right x axis y axis)
    
现在我们应该告诉Xorg它已经接上了 (本来就是,对吧) 
    
    xrandr --output S-video --set "load detection" 1
    
设定TV制式标准 
    
    xrandr --output S-video --set "tv standard" ntsc
    
为它添加一个分辨率（目前只支持800x600） 
    
    xrandr --addmode S-video 800x600
    
复制模式（clone mode) 
    
    xrandr --output S-video --same-as VGA-0
    
好了，让我们来看看效果吧 
    
    xrandr --output S-video --mode 800x600
    
这时，在电视上你应该能看到你的桌面，分辨率是800x600。 

要关掉这一输出： 
    
    xrandr --output S-video --off
    
###  在KMS中强制TV输出

内核可识别下列格式的 `video=` 参数 （参见[KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS")）： 
    
    video=<conn>:<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][m][eDd]
    
例如： 
    
    video=DVI-I-1:1280x1024-24@60e
    
带有空格的参数必须用引号括起： 
    
    "video=9-pin DIN-1:1024x768-24@60e"
    
Current mkinitcpio implementation also requires `#` in front. For example: 
    
    root=/dev/disk/by-uuid/d950a14f-fc0c-451d-b0d4-f95c2adefee3 ro quiet radeon.modeset=1 security=none # video=DVI-I-1:1280x1024-24@60e "video=9-pin DIN-1:1024x768-24@60e"
    
  * [GRUB Legacy](<../zh-cn/GRUB_Legacy.html> "GRUB Legacy") 可直接接受如上参数。
  * [LILO](</wzh/index.php?title=LILO&action=edit&redlink=1> "LILO（页面不存在）") 需要在双引号前使用“\”转义 (例如 `# \"video=9-pin DIN-1:1024x768-24@60e\"`)

You can get list of your video outputs with following command: 
    
    $ ls -1 /sys/class/drm/ | grep -E '^card[[:digit:]]+-' | cut -d- -f2-

##  HDMI 音频输出

HDMI 音频输出在 [xf86-video-ati](<https://archlinux.org/packages/?name=xf86-video-ati>)包 软件包中提供支持。要启禁用，在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中添加 `radeon.audio=0`。 

如果启动后没有视频输出，则请禁用这个参数。 

**注意：**

  * 如果在安装驱动后 HDMI 音频没有工作，请使用[这里](<../zh-cn/Advanced_Linux_Sound_Architecture/Troubleshooting.html#HDMI_%E8%BE%93%E5%87%BA%E4%B8%8D%E5%B7%A5%E4%BD%9C> "Advanced Linux Sound Architecture/Troubleshooting")提供的方法进行检测。
  * 如果在 PulseAudio 中声音出现问题，尝试设置 `tsched=0`（参见 [PulseAudio/Troubleshooting#Glitches, skips or crackling](</wzh/index.php?title=PulseAudio/Troubleshooting&action=edit&redlink=1> "PulseAudio/Troubleshooting（页面不存在）")）并确保 `rtkit` 守护进程正在运行。
  * 因为 HDA 兼容硬件的相似性，你的声卡可能使用相同的模块。请使用推荐的方式[改变默认声卡](<../zh-cn/Advanced_Linux_Sound_Architecture.html#%E8%AE%BE%E7%BD%AE%E9%BB%98%E8%AE%A4%E5%A3%B0%E5%8D%A1> "Advanced Linux Sound Architecture")，比如修改 alsa 配置文件的 `defaults` 节点。

##  多显设置

###  使用 RandR 扩展

参见 [Multihead#RandR](<../zh-cn/%E5%A4%9A%E6%98%BE%E7%A4%BA%E5%99%A8.html#RandR> "Multihead")。 

###  独立的 X screen

独立的双显示器可以按正常方式配置，radeon 驱动有一个 `"ZaphodHeads"` 选项可以把显示的区域绑定到固定的设备，例如： 
    
    /etc/X11/xorg.conf.d/20-radeon.conf
    
    Section "Device"
      Identifier "Device0"
      Driver "radeon"
      Option "ZaphodHeads" "VGA-0"
      VendorName "ATI"
      BusID "PCI:1:0:0"
      Screen 0
    EndSection
    
有些显卡有多个输出（HDMI，DVI 和 VGA），而双屏显示的时候它只使用 HDMI+DVI，这时你可以通过 `"ZaphodHeads" "VGA-0"` 来更改输出。这在使用多输出显卡时很方便。 

##  关闭垂直同步刷新

radeon驱动默认启用垂直同步刷新，除了跑分外各种情况下工作良好。要关闭它，可以设置 `vblank_mode=0` [环境变量](<../zh-cn/Environment_variable.html> "Environment variable")或创建 `~/.drirc` （如果已存在请修改），加入以下部分 : 
    
    ~/.drirc
    
    <driconf>
        <device screen="0" driver="dri2">
            <application name="Default">
                <option name="vblank_mode" value="0" />
            </application>
        </device>
    </driconf>
    
请确保是 **dri2** , 而不是你的显卡型号（如 r600 ）。 

如果 vsync 还是启用状态，可以通过禁用`/etc/X11/xorg.conf.d/20-radeon.conf`. See [#Driver options](<#Driver_options>). 

##  故障排除

###  使用 EXA 时性能低

**注意：** 仅适用于使用 EXA 的老显卡(R600 或更老).新卡应该使用 Glamor 。

如果2D性能(比如在终端或浏览器的滚动滑块)有问题, 你可以将 `Option "MigrationHeuristic" "greedy"` 添加到你的 `xorg.conf` 文件的 `**Device**` 部分. 禁用 `EXAPixmaps` 也可能避免一些问题，但是可能带来别的问题，所以不建议使用。 

这是一个样例 `/etc/X11/xorg.conf.d/**20-radeon.conf**`: 
    
    Section "OutputClass"
            Identifier  "My Graphics Card"
            MatchDriver "radeon"
            Option "AccelMethod" "exa"
            Option  "MigrationHeuristic"  "greedy"
            #Option "EXAPixmaps" "off"
    EndSection
    
###  添加没有被侦测到的分辨率

参见[Xrandr的文章](<../zh-cn/Xrandr.html#Adding_undetected_resolutions> "Xrandr"). 

###  电视屏幕显示黑边

我的Radeon HD 5770用HDMI连接到电视时, 电视显示图像模糊,周围有2-3cm黑边,用催化剂时不是这样. 这是对付过扫描(Overscan)的(参见[Wikipedia:Overscan](<https://en.wikipedia.org/wiki/Overscan> "wikipedia:Overscan")),使用xrandr关闭它: 
    
    xrandr --output HDMI-0 --set underscan off
    
###  KMS启用时,黑幕,没有控制台,但是 X 能够工作

当在同一台PC使用两张或以上的ATI显卡时可能会遇到此问题. 例如 Fujitsu Siemens Amilo PA 3553 笔记本就有这个问题. 这是因为fbcon控制台驱动程序将自己映射到错误显卡的错误 framebuffer 设备上. 在内核参数添加: 
    
    fbcon=map:1
    
这将告诉fbcon映射自己到 `/dev/fb1` 而不是 `/dev/fb0`.如果这并未解决你的问题，尝试如下配置启动: 
    
    fbcon=map:0
    
###  显示器旋转对光标起效却对窗口/内容不起效

启用EXA代替glamor的新显卡用户可能会发现,用xrandr旋转显示器将导致光标和显示器尺寸旋转了,但窗口与里面内容却保持原来方向. 另外移动鼠标时光标按照原来的方向移动.若有此问题,在你的 `/var/log/Xorg.0.log` 中查找下面这一行: 
    
    (EE) RADEON(0): Rotation requires acceleration!
    
新显卡上使用EXA时加速将被禁用(来源: [这里](<https://bugs.freedesktop.org/show_bug.cgi?id=73420#c17>)). 你必须从启用EXA ([参见这里](<#%E9%A9%B1%E5%8A%A8%E8%AE%BE%E7%BD%AE>)) 和旋转中二选一. 

###  在ATI X1600 (RV530 series)上3D应用程序显示黑窗口

这三种方法可能有效: 

  * 将 `pci=nomsi` 添加到你的启动器的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数").
  * 如果没用的话,试试用`noapic`代替`pci=nomsi`.
  * 如果还是没用,你可以试试`vblank_mode=0 glxgears` 或者 `vblank_mode=1 glxgears`,看看哪个对你有用. 然后安装[driconf](<https://aur.archlinux.org/packages/driconf/>)AUR , 在`~/.drirc`里设置此参数.

###  从休眠中唤醒后光标崩溃

如果显示器唤醒后光标垂直方向重复刷新，可以在配置文件 `20-radeon.conf` 中的 `"Device"` 部分里设置 `"SWCursor" "True"`。 

###  多显示器模式下DisplayPort黑屏

尝试以[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `radeon.audio=0` 启动。 

###  R9-390 Poor Performance and/or Instability

Firmware issues with R9-390 series cards include poor performance and crashes (frequently caused by gaming or using Google Maps) possibly related DPM. Comment 115 of this bug [report](<https://bugs.freedesktop.org/show_bug.cgi?id=91880>) includes instructions for a fix. 

###  QHD / UHD / 4k support over HDMI for older Radeon cards

Older cards have their pixel clock limited to 165MHz for HDMI. Hence, they do not support QHD or 4k only via dual-link DVI but not over HDMI. 

One possibility to work around this is to use [custom modes with lower refresh rate](<https://www.elstel.org/software/hunt-for-4K-UHD-2160p.html.en>), e.g. 30Hz. 

Another one is a kernel patch removing the pixel clock limit, but this may damage the card! 

Official kernel bug ticket with patch for 4.8: <https://bugzilla.kernel.org/show_bug.cgi?id=172421>

The patch introduces a new kernel parameter `radeon.hdmimhz` which alters the pixel clock limit. 

Be sure to use a high speed HDMI cable for this. 

### Horizontal flickering occasionally when using 4k DP output on 390X

If you use 390X (or perhaps similar models) and the 4k output from DP, you may experiencing occasional horizontal artifacts / flickering (i.e. every half an hour or so, a horizontal strip of pixels with a height of ~100 pixels across the whole screen's width shaking up and down for a few seconds). This might be a bug of the radeon driver. Changing to [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") seems to fix it. 

## See also

[Benchmark](<https://www.phoronix.com/scan.php?page=article&item=radeonsi-cat-wow&num=1>) showing the open source driver is on par performance-wise with the proprietary driver for many cards. 
