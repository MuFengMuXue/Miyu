**翻译状态：**

  * 本文（或部分内容）译自 [Xiaomi Mi Notebook Air 13.3 (2016)](<https://wiki.archlinux.org/title/Xiaomi_Mi_Notebook_Air_13.3_\(2016\)> "arch:Xiaomi Mi Notebook Air 13.3 \(2016\)")，最近一次同步于 2020-03-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xiaomi_Mi_Notebook_Air_13.3_\(2016\)?diff=0&oldid=590955>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xiaomi_Mi_Notebook_Air_13.3_\(2016\)_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**设备** | **状态** |  **内核模块**  
---|---|---  
视频 | 工作 | i915   
无线网络 | 工作 | iwlwifi   
蓝牙 | 工作 | btusb   
音频 | 工作 | snd_hda_intel   
触摸板 | 工作 | ?   
网络摄像头 | 工作 | uvcvideo   
USB-C / Thunderbolt 3 | 工作 | ?   
功能/多媒体键 | 工作 | ?   
  
小米笔记本 Air 13.3 是一款铝合金的超极本，由小米公司生产。目前只能在中国或者通过跨境电商网站购买。第一代小米 Air 使用运行在 2.3 Ghz 的 Intel Core i5 6200U 和 NVIDIA GeForce 940MX 显卡，以较低的价格提供了不错的性能。 

如果按照以下步骤安装，应该不会出现任何问题。 

##  安装前的系统设置

正确启动 Arch 安装媒介实际上很简单。启动 Arch 安装 ISO 之前，在引导过程中按 `F2`，进入 UEFI 设置。 

  * 安全 -> 设置密码
  * 安全 -> 关闭安全启动（Secure Boot）
  * 再次设置密码，但在"新密码"一栏留空，从而重置密码

Arch的安装就可以正常进行了。请参考[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")获取更多信息。 

**注意：** 切记，你的固态硬盘名称为 `nvme0n1` 而非 `sda`。

##  显卡设置

小米笔记本同时配有 Intel 的集成显卡和 Nvidia 的独立显卡。 

###  只使用集显

如果你想完全禁用Nvidia GPU以提高续航，操作如下： 

  * 安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包
  * 屏蔽内核模块 [nvidia](<https://archlinux.org/packages/?name=nvidia>)包 和 [xf86-video-nouveau](<https://archlinux.org/packages/?name=xf86-video-nouveau>)包，参见 [Kernel module#黑名单](<../zh-cn/Kernel_module.html#%E9%BB%91%E5%90%8D%E5%8D%95> "Kernel module")

    /etc/modprobe.d/nouveau.conf
    
    blacklist nouveau
    blacklist nvidia

  * 安装[bbswitch](<https://archlinux.org/packages/?name=bbswitch>)包以[关闭独立显卡](<../zh-cn/Bumblebee.html#%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "Bumblebee")

    /etc/modprobe.d/bbswitch
    
    options bbswitch load_state=0 unload_state=0

###  Intel/Nvidia 混合配置

使用 [Bumblebee](<../zh-cn/Bumblebee.html> "Bumblebee") 或 [NVIDIA Optimus](<../zh-cn/NVIDIA_Optimus.html> "NVIDIA Optimus") 都可以启用混合 GPU。Bumblebee 一般续航和兼容性更好，但没有 NVIDIA 的官方支持。 

请参阅相应文章。 

##  输入

###  触摸板

想要正常使用触摸板，必须使用 [xf86-input-libinput](<https://archlinux.org/packages/?name=xf86-input-libinput>)包。如果使用 [xf86-input-evdev](<https://archlinux.org/packages/?name=xf86-input-evdev>)包，则触摸板会像触摸屏一样工作（也就是说，它直接把你在触摸板上的操作映射到屏幕上）。而如果使用 [xf86-input-synaptics](<https://archlinux.org/packages/?name=xf86-input-synaptics>)包（尽管强烈不建议这样，因为它已经被废弃了（参见 [Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics")）），触摸板只会偶尔正常工作。通过XOrg配置文件对 [libinput](<https://archlinux.org/packages/?name=libinput>)包 作如下配置，即可启用双指手势、轻触点击、双指/三指点击（分别对应于按下鼠标右键和中键）。 
    
    /etc/X11/xorg.conf.d/20-touchpad.conf
    
    Section "InputClass"
            Identifier "libinput touchpad"
            Driver "libinput"
            MatchIsTouchpad "on"
            MatchDevicePath "/dev/input/event*"
            Option "Tapping" "on"
            Option "ClickMethod" "clickfinger"
            Option "NaturalScrolling" "true"
    EndSection

###  Fn 键

在该笔记本上默认Fn键是启用的（如按F1可以静音）。如果按这些Fn功能键没有反应，那么你很可能使用的是[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")而不是[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。使用相应的配置文件将按键与功能绑定，比如利用 [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") 或 [i3](<../zh-cn/I3.html> "I3") 的 `bindsym`。 

大多数 Fn 键返回正确的键码。以下表格包含了这些信息： 

Fn-F-Key  | Keycode   
---|---  
`F1` |  `XF86AudioMute`  
`F2` |  `XF86AudioLowerVolume`  
`F3` |  `XF86AudioRaiseVolume`  
`F4` |  `XF86MonBrightnessDown`  
`F5` |  `XF86MonBrightnessUp`  
`F6` |  `Super_L + P`  
`F7` |  `无`  
`F8` |  `Super_L + Tab`  
`F9` |  `无`  
`F10` |  `Turns Keyboard backlight on/off`  
`F11` |  `Print`  
`F12` |  `Insert`  
  
##  显示校准

出厂显示校准很差。作为对校色仪的替代，试试这里的[ICC 配置文件](</wzh/index.php?title=ICC_profiles&action=edit&redlink=1> "ICC profiles（页面不存在）")：[tlvince/xiaomi-mi-notebook-air-13](<https://github.com/tlvince/xiaomi-mi-notebook-air-13/tree/master/display-calibration>). 

##  硬件信息

_lspci_ 输出： 
    
    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 520 (rev 07)
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
    00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point-LP LPC Controller (rev 21)
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
    01:00.0 3D controller: NVIDIA Corporation GM108M [GeForce 940MX] (rev ff)
    02:00.0 Network controller: Intel Corporation Wireless 8260 (rev 3a)
    03:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM951/PM951 (rev 01)
    
_lsusb_ 输出： 
    
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 8087:0a2b Intel Corp.
    Bus 001 Device 002: ID 05c8:03a2 Cheng Uei Precision Industry Co., Ltd (Foxlink)
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
##  故障排除

###  背光灯

以默认配置使用 [xorg-xbacklight](<https://archlinux.org/packages/?name=xorg-xbacklight>)包 之类的工具是无效的，因为背光灯路径不符合标准。为了解决此问题，需要使用 X-Org 配置文件： 
    
    /etc/X11/xorg.conf.d/10-backlight.conf
    
    Section "Device" 
            Identifier "Card0" 
            Driver     "intel" 
            Option     "Backlight"  "intel_backlight" 
            BusID      "PCI:0:2:0" 
    EndSection

### WiFi

如果自动检测的 WiFi 驱动出现问题，可能是因为两个驱动存在冲突，如 `rfkill list` 的输出所示。屏蔽有问题的驱动以解决此问题： 
    
    /etc/modprobe.d/blacklist.conf
    
    blacklist acer-wmi

注：此问题在 Linux 内核 4.9 以上版本中已经解决。 

###  音频插孔

如果想使用插入音频组合插孔中的耳机上的麦克风，请将这一行加入 alsa 配置文件： 
    
    /etc/modprobe.d/alsa-base.conf
    
    options snd-hda-intel model=dell-headset-multi

然后重启机器。 
