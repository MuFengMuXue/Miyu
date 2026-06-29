本文涵盖了在 Lenovo ThinkPad T14P Gen2 (2024) 笔记本（仅中国大陆特供）上安装和配置 Arch Linux 的信息。 

##  安装

使用最新的 [Archiso](<https://archlinux.org/download/>) 完成基本的系统安装。 

其余安装过程请参考[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")。 

常用笔记本设置可参考：[笔记本电脑](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html> "笔记本电脑")。 

##  硬件

需要额外安装的硬件驱动有： 

###  视频驱动

安装以下几个包： 

[mesa](<https://archlinux.org/packages/?name=mesa>)包 [lib32-mesa](<https://archlinux.org/packages/?name=lib32-mesa>)包 [vulkan-intel](<https://archlinux.org/packages/?name=vulkan-intel>)包 [lib32-vulkan-intel](<https://archlinux.org/packages/?name=lib32-vulkan-intel>)包

请勿安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包，该包是为了旧显卡准备的，本型号设备安装后 SDDM 显示管理器会出现黑屏现象。 

###  指纹扫描器

指纹扫描器可以在 [fprintd](<https://archlinux.org/packages/?name=fprintd>)包 和 PAM 配合下完美工作，如果是在非 Gnome / KDE 桌面环境下使用，建议安装 [fingerprint-gui](<https://aur.archlinux.org/packages/fingerprint-gui/>)AUR。 

可以参阅 [Fprint](<../zh-cn/Fprint.html> "Fprint") 进一步设置指纹登录解锁和 sudo 解锁等（注意：目前 指纹解锁并不支持自动解锁密钥环，故指纹登录目前并不实用）。 

####  指纹解锁 sudo

编辑 `/etc/pam.d/sudo`，在最顶部增加一行 `auth sufficient pam_fprintd.so` 即可。 

解释：该行表示使用 frprintd 进行 pam 认证解锁，并且如果失败继续下面的认证方式。 

####  指纹解锁 polkit

polkit 用于给某些程序提权。 

复制文件 `/usr/lib/pam.d/polkit-1` 到 `/etc/pam.d/polkit-1`，然后在最顶部增加一行 `auth sufficient pam_fprintd.so` 即可。 

###  NPU 驱动

目前 Intel 已经开源其 NPU 驱动，并且 AUR 已有打包：[intel-npu-driver-bin](<https://aur.archlinux.org/packages/intel-npu-driver-bin/>)AUR。 

##  笔记本设置

### ACPI

[ACPI](<../zh-cn/ACPI_modules.html> "ACPI modules") 支持完善，没有明显问题。 

注意：电源按钮在 linux 下行为和在 windows 下行为不同，如果需要触发电源按钮的 ACPI 事件，需要按住按钮约 1 秒时间等待生效！ 

###  风扇调节

无需额外设置，开箱即用。 

###  键盘

键盘开箱即用，默认支持 windows下的所有快捷键，但 Copilot 按键需要额外配置。 

Fn + 快捷键正常（包括背光支持） 

###  指点杆

请使用 [xf86-input-libinput](<https://archlinux.org/packages/?name=xf86-input-libinput>)包 ，默认开箱即用（但默认不支持指点杆的双击功能）。 

###  视频硬件解码

安装 [intel-media-driver](<https://archlinux.org/packages/?name=intel-media-driver>)包 即可，firefox 可自动识别，chromium 系需要做额外设置，传递参数： 
    
    ~/.config/chromium-flags.conf
    
    --enable-features=VaapiVideoDecodeLinuxGL

chrome 则需要编辑文件 `~/.config/chrome-flags.conf`。 

##  省电优化方案

建议以下两款工具均安装 

  1. [thermald](<https://archlinux.org/packages/?name=thermald>)包 可以防止 Intel 平台过热，但目前并不完全支持所有的 CPU 型号，可以通过 `sudo systemctl status thermald` 来查看thermald 是否支持当前 CPU。

  1. [TLP](<../zh-cn/TLP.html> "TLP") 是一款专业的省电优化工具，可以安装 [tlp](<https://archlinux.org/packages/?name=tlp>)包, [tlpui](<https://archlinux.org/packages/?name=tlpui>)包，[tlp-rdw](<https://archlinux.org/packages/?name=tlp-rdw>)包。

安装并开启 TLP： 
    
     sudo pacman -S tlp tlp-rdw
    
建议额外安装 [tlpui](<https://aur.archlinux.org/packages/tlpui/>)AUR，作为 GUI 控制。 
    
     sudo systemctl enable tlp.service
     # 无线电设备向导需要额外的服务支持
     sudo systemctl enable NetworkManager-dispatcher.service
     # 屏蔽以下服务以避免冲突
     sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket
    
TLP 默认已经配置了绝大多数功能保证可以开箱即用，但并不保证实现更好的省电策略，故需要手动进行调节： 

注意：以下设置是为了让电脑在流畅的情况下尽可能的低功耗，如果想要满血运行，可以参考 TLP 的官方文档，调整 CPU 为主动模式。 

###  处理器设置

  * `CPU_DRIVER_OPMODE_ON_AC` 设置为 `passive`
  * `CPU_DRIVER_OPMODE_ON_BAT` 设置为 `passive`

这会指示 CPU 启动被动模式，允许我们选择更加智能的调度模式。 

  * `CPU_SCALING_GOVERNOR_ON_AC` 设置为 `schedutil`
  * `CPU_SCALING_GOVERNOR_ON_BAT` 设置为 `schedutil`

设置 CPU 自动调频策略，`schedutil` 策略由较新内核支持，可以提供更好的调频策略。 

  * `CPU_ENERGY_PERF_POLICY_ON_AC` 设置为 `balance_performance`
  * `CPU_ENERGY_PERF_POLICY_ON_BAT` 设置为 `balance_power`

设置 CPU 能耗策略为平衡模式。 

###  充电阈值设置

充电阈值旨在通过减少持续运行导致的磨损和容量损失来延长电池的使用寿命。 

设置主电池： 
    
    START_CHARGE_THRESH_BAT0=75
    STOP_CHARGE_THRESH_BAT0=80
    
设置辅电池： 
    
    START_CHARGE_THRESH_BAT1=75
    STOP_CHARGE_THRESH_BAT1=80
    
###  音频省电超时

TLP 默认开启音频省电超时，当前会导致出现噪音干扰，可选择禁用省电或者延长超时时间： 
    
    # 禁用
    SOUND_POWER_SAVE_ON_BAT=0
    # 延长至10
    SOUND_POWER_SAVE_ON_BAT=10
    
注意：目前的 TLP 开启音频相关设置后会导致 pipewire 的开机自动切换失效（表现为耳机播放无声音，手动在 DE 中切换设备到扬声器后再切换回来后正常工作），可以考虑关闭音频省电的相关设置。 

###  WIFI 省电

默认 TLP 在使用电池时开启省电策略，但会略微影响 WIFI 的连接稳定性，可考虑是否关闭来获得更好的网络连接！ 
