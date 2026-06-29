**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo Thinkpad T14 (AMD) Gen 1](<https://wiki.archlinux.org/title/Lenovo_Thinkpad_T14_\(AMD\)_Gen_1> "arch:Lenovo Thinkpad T14 \(AMD\) Gen 1")，最近一次同步于 2021-04-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_Thinkpad_T14_\(AMD\)_Gen_1?diff=0&oldid=663795>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_Thinkpad_T14_\(AMD\)_Gen_1_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**This article or section does not follow the[Laptop page guidelines](</wzh/index.php?title=Help:Laptop_page_guidelines&action=edit&redlink=1> "Help:Laptop page guidelines（页面不存在）").**

**Reason:** 硬件列表需要调整；`lspci`/`lsusb` 的返回值不应列在笔记本页面中 (Discuss in [Talk:Lenovo Thinkpad T14 (AMD) Gen 1](<../zh-cn/Talk:Lenovo_Thinkpad_T14_\(AMD\)_Gen_1.html>))

相关文章

  * [Lenovo Thinkpad T14s (AMD) Gen 1](</wzh/index.php?title=Lenovo_Thinkpad_T14s_\(AMD\)_Gen_1&action=edit&redlink=1> "Lenovo Thinkpad T14s \(AMD\) Gen 1（页面不存在）")
  * [Lenovo ThinkPad T495s](</wzh/index.php?title=Lenovo_ThinkPad_T495s&action=edit&redlink=1> "Lenovo ThinkPad T495s（页面不存在）")
  * [Lenovo ThinkPad T495](</wzh/index.php?title=Lenovo_ThinkPad_T495&action=edit&redlink=1> "Lenovo ThinkPad T495（页面不存在）")

硬件设备 | 是否正常工作？   
---|---  
[AMD显卡](<../zh-cn/AMDGPU.html> "AMDGPU") | 是   
[无线局域网](<../zh-cn/Network_configuration/Wireless.html> "Network configuration/Wireless") | 是   
[摄像头](</wzh/index.php?title=%E7%BD%91%E7%BB%9C%E6%91%84%E5%83%8F%E6%9C%BA&action=edit&redlink=1> "网络摄像机（页面不存在）") | 是   
[小红点](<../zh-cn/%E6%8C%87%E7%82%B9%E6%9D%86.html> "TrackPoint") | 是   
[触摸板](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html#%E8%A7%A6%E6%91%B8%E6%9D%BF> "Laptop") | 是   
[指纹识别](<../zh-cn/Fprint.html> "Fprint") | 是   
[移动宽带](</wzh/index.php?title=ThinkPad_mobile_Internet&action=edit&redlink=1> "ThinkPad mobile Internet（页面不存在）") |  [Xmm7360-pci](</wzh/index.php?title=Xmm7360-pci&action=edit&redlink=1> "Xmm7360-pci（页面不存在）")  
  
本文主要叙述在Lenovo Thinkpad T14 (AMD) Gen 1笔记本电脑上安装和配置[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")。当使用内核版本>=5.9.0时，所有硬件基本上是开箱即用的状态。目前尚未测试的硬件有：移动宽带、智能卡读卡器、蓝牙。 

与笔记本电脑安装Arch Linux相关的通用事项及建议，参见[Laptop](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html> "Laptop")。 

##  硬件

AMD 锐龙 7 PRO 4750U 处理器 

使用内核版本5.9.14。 
    
    产品名称：Thinkpad T14 (AMD) Gen 1
    配置代码: 20UE / 20UD
    BIOS版本: 1.27 (R1BET58W)
    
`lspci` 返回如下内容： 
    
    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.4 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.6 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:02.7 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 7
    01:00.0 Non-Volatile memory controller: SK hynix Device 1639
    02:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 0e)
    02:00.1 Serial controller: Realtek Semiconductor Co., Ltd. Device 816a (rev 0e)
    02:00.2 Serial controller: Realtek Semiconductor Co., Ltd. Device 816b (rev 0e)
    02:00.3 IPMI Interface: Realtek Semiconductor Co., Ltd. Device 816c (rev 0e)
    02:00.4 USB controller: Realtek Semiconductor Co., Ltd. Device 816d (rev 0e)
    03:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
    04:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)
    05:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 15)
    06:00.0 USB controller: Renesas Technology Corp. uPD720202 USB 3.0 Host Controller (rev 02)
    07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev d1)
    07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device 1637
    07:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    07:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1
    07:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1
    07:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor (rev 01)
    07:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller 
    
`lsusb` 返回如下内容： 
    
    Bus 007 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 006 Device 003: ID 8087:0029 Intel Corp. AX200 Bluetooth
    Bus 006 Device 002: ID 06cb:00bd Synaptics, Inc. Prometheus MIS Touch Fingerprint Reader
    Bus 006 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 005 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 004 Device 002: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 004 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 002 Device 002: ID 04f2:b6d0 Chicony Electronics Co., Ltd Integrated Camera
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    
##  固件

###  安全启动

2021年1月之后，删除系统自带的安全启动秘钥并安装用户自己的秘钥（如使用[KeyTool](<../zh-cn/Unified_Extensible_Firmware_Interface/Secure_Boot.html#Using_KeyTool> "Unified Extensible Firmware Interface/Secure Boot")）将会使设备变砖。这个问题与[其他联想笔记本上出现的问题](<https://forums.lenovo.com/t5/ThinkPad-X-Series-Laptops/BIOS-BUG-X1C7-quot-Configuration-changed-restart-system-quot-loop-after-enrolled-my-own-secureboot-key/m-p/4607484>)相似，可能是由于固件中的错误导致的。如果在更换安全启动秘钥后设备陷入无限循环的重启中，惟一的修复方法就是更换主板。希望这个问题能够在未来的固件升级中得到修复。 

###  电池问题

在一个持续更新的[论坛帖子](<https://forums.lenovo.com/t5/Other-Linux-Discussions/T14-AMD-battery-drain-in-standby-Linux/m-p/5037674?page=1>)中，出现了关于待机/关机状态下电池消耗过快的讨论。目前估计使用AMD雷诺阿架构CPU及其相关硬件的笔记本都会受到影响。由于1.30版本的BIOS可能会导致关机状态下电池电量在2-3天内减少50%，目前建议使用1.29版本的BIOS。 

另外有意见指出，升级内核应该可以解决这个问题。联想和Canonical正在着手解决这个问题。 

##  AMD显卡

开源的[AMD显卡](<../zh-cn/AMDGPU.html> "AMDGPU")驱动无需任何特别修改即可正常工作。 

如果想在[Chromium](<../zh-cn/Chromium.html> "Chromium")浏览器中开启硬件加速视频解码功能，安装[libva-mesa-driver](<https://archlinux.org/packages/?name=libva-mesa-driver>)包、[vulkan-radeon](<https://archlinux.org/packages/?name=vulkan-radeon>)包及[mesa-vdpau](<https://archlinux.org/packages/?name=mesa-vdpau>)包软件包，创建文件`~/.config/chromium-flags.conf`，将下列内容粘贴至创建的文件中： 
    
    --ignore-gpu-blocklist
    --use-gl=desktop
    --enable-gpu-rasterization
    --enable-zero-copy
    --ignore-gpu-blacklist
    --disable-gpu-driver-bug-workarounds
    --enable-accelerated-video-decode
    
重新启动[Chromium](<../zh-cn/Chromium.html> "Chromium")浏览器，并确认`chrome://gpu`的输出内容与下列内容一致： 
    
    Canvas: Hardware accelerated
    Compositing: Hardware accelerated
    Multiple Raster Threads: Enabled
    Out-of-process Rasterization: Disabled
    OpenGL: Enabled
    Hardware Protected Video Decode: Hardware accelerated
    Rasterization: Hardware accelerated on all pages
    Skia Renderer: Enabled
    Video Decode: Hardware accelerated
    Vulkan: Disabled
    WebGL: Hardware accelerated
    WebGL2: Hardware accelerated
    
向下滚动很多行后应该会看到以下内容： 
    
    Video Acceleration Information
    Decode h264 baseline	16x16 to 4096x4096 pixels
    Decode h264 main	16x16 to 4096x4096 pixels
    Decode h264 high	16x16 to 4096x4096 pixels
    Decode vp9 profile0	16x16 to 8192x4352 pixels
    
更多内容请参考[Chromium#Force GPU acceleration](<../zh-cn/Chromium.html#Force_GPU_acceleration> "Chromium")及[vaapi on linux](<https://chromium.googlesource.com/chromium/src/+/master/docs/gpu/vaapi.md#vaapi-on-linux>)。 

##  指纹传感器

指纹传感器在近期更新的固件及近期升级的软件支持下工作正常。 

  1. 使用[fwupd](<../zh-cn/Fwupd.html> "Fwupd")安装“Synaptics Prometheus Fingerprint Reader”的最新固件。相关固件为[Prometheus Fingerprint Reader](<https://fwupd.org/lvfs/devices/com.synaptics.prometheus.firmware>)和[Prometheus Fingerprint Reader Configuration](<https://fwupd.org/lvfs/devices/com.synaptics.prometheus.config>)。
  2. 需要[fprintd](<https://archlinux.org/packages/?name=fprintd>)包版本≥1.90.1且[libfprint](<https://archlinux.org/packages/?name=libfprint>)包版本≥1.90.1。也可以安装[fprintd-libfprint2](<https://aur.archlinux.org/packages/fprintd-libfprint2/>)AUR和[libfprint-git](<https://aur.archlinux.org/packages/libfprint-git/>)AUR使用最新的开发版本。

[fprint](<../zh-cn/Fprint.html> "Fprint")页面包含安装指纹传感器的更多细节，如以[PAM](<../zh-cn/PAM.html> "PAM")为基础的身份验证。 

如果[fwupd](<../zh-cn/Fwupd.html> "Fwupd")未能检测到指纹传感器，但是`lsusb`可以检测到，你需要在BIOS中重置指纹传感器。 

##  背光

通过修改`/sys/class/backlight/amdgpu_bl0/brightness`文件中的值（范围0-255），背光可以正常工作。也可以通过背光调节软件控制背光。 

如果使用比内核版本5.8.6更早的内核，需要[禁用](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")`systemd-backlight@backlight:acpi_video0.service`，因为该单元会启动失败。 

##  休眠

S3级别的休眠需要在BIOS中设定Config -> Power -> Sleep to Linux。 

##  智能卡读卡器

似乎可以正常工作，能够读取卡片。具体用法可参考[smartcards](</wzh/index.php?title=Smartcards&action=edit&redlink=1> "Smartcards（页面不存在）")

##  移动宽带

[xmm7360-pci](<https://github.com/xmm7360/xmm7360-pci>)经测试可正常使用，具体参考[Xmm7360-pci](</wzh/index.php?title=Xmm7360-pci&action=edit&redlink=1> "Xmm7360-pci（页面不存在）")。 
    
    $ lspci | grep XMM
    05:00.0 Wireless controller [0d40]: Intel Corporation XMM7360 LTE Advanced Modem (rev 01)
    
##  无线局域网

板载无线局域网卡型号为Intel AX200，直接使用可能会存在[处理器微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")方面的问题。对于WiFi断连的一个可能的解决方案是打开iwlwifi天线聚合，具体方法为创建一个[modprobe](<../zh-cn/Kernel_module.html> "Kernel module")配置： 
    
    /etc/modprobe.d/iwlwifi.conf
    
    options iwlwifi 11n_disable=8

之后重启。详情参照[Network configuration/Wireless#iwlwifi](<../zh-cn/Network_configuration/Wireless.html#iwlwifi> "Network configuration/Wireless")。 
