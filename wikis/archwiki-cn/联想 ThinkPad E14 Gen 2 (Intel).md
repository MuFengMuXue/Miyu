**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo_ThinkPad_E14_Gen_2_(Intel)](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_E14_Gen_2_\(Intel\)> "arch:Lenovo ThinkPad E14 Gen 2 \(Intel\)")，最近一次同步于 2024/07/13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_E14_Gen_2_\(Intel\)?diff=0&oldid=809003>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_E14_Gen_2_\(Intel\)_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

硬件 | PCI/USB ID | 可用?   
---|---|---  
TrackPoint |  | 是   
触摸板 |  | 是   
显卡 (Intel) | `8086:9a49` | 是   
显卡 (NVIDIA) | `10de:1f97` | 是   
摄像头 | `04f2:b6c2` | 是   
以太网 | `10ec:8168` | 是   
蓝牙 | `8087:0026` | 是   
声卡 | `8086:a0c8` | 是   
无线局域网 | `8086:a0f0` | 是   
TPM 2.0 |  | 是   
  
##  安装

在安装时，禁用 [Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot")，并请为 [microcode](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [intel-ucode](<https://archlinux.org/packages/?name=intel-ucode>)包 并为 [Intel graphics](<../zh-cn/Intel_graphics.html> "Intel graphics") 安装 [xf86-video-intel](<https://archlinux.org/packages/?name=xf86-video-intel>)包 . 

若您想使用 [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA") 显卡, 尝试 [nouveau](<../zh-cn/Nouveau.html> "Nouveau"). 

##  可访问性

BIOS 系统有两种模式，**Quick** 和 **Diagnostics** 。两者都可以正确安装和启动 Arch Linux。 

### Quick

BIOS 的外观简洁，色彩不是很丰富，但更现代、更流畅，因此可以很好地与 OCR 软件配合使用。但是，它需要用户使用鼠标。另外，在启动系统前，中间显示[Lenovo](</wzh/index.php?title=Lenovo&action=edit&redlink=1> "Lenovo（页面不存在）")的标志。 

**注意：** 盲人用户应请求有视力的人帮助更改 BIOS 设置

### Diagnostics

外观将是传统的蓝色和白色，使用带有锯齿的字体，但你不需要鼠标，只需要键盘。 此外，在启动系统之前，它会使用黑白锯齿字体显示计算机信息。 

服务手册还包含触发某些功能所需的快捷方式，例如启动菜单和设置 (`Enter`)。 

使用 `F1` 进入 BIOS，使用 `F12` 进入启动菜单。 

##  固件

**注意：**

  * 此设备没有 BIOS 扬声器，而是使用内置扬声器。哔声可能比预期的要响亮。
  * 要禁用此功能，请在启动前快速关闭 FnLock 并按 `F1`。

您可以使用 TPM 2.0 `BIOS>Security>Secure Chip`. 

###  安全启动

在 Arch Linux 安装后，您可以配置 
    
    BIOS>Security>Secure boot
    
###  固件数据路径

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 未测试 (在 [Talk:联想 ThinkPad E14 Gen 2 (Intel)](<../zh-cn/Talk:%E8%81%94%E6%83%B3_ThinkPad_E14_Gen_2_\(Intel\).html>) 中讨论)

####  日志

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 未测试 (在 [Talk:联想 ThinkPad E14 Gen 2 (Intel)](<../zh-cn/Talk:%E8%81%94%E6%83%B3_ThinkPad_E14_Gen_2_\(Intel\).html>) 中讨论)

##  声卡

安装 extra 仓库的 [sof-firmware](<https://archlinux.org/packages/?name=sof-firmware>)包。 

跟进 [ALSA](<../zh-cn/ALSA.html> "ALSA") 以了解更多细节。 

##  蓝牙

安装后，参见[蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "蓝牙")。 

##  电源管理

没有已知问题。 

###  电源按钮

此设备有检测到一个电源按钮和一个睡眠按钮。 
    
    $ loginctl seat-status
    
    seat0
            Sessions: *3
             Devices:
                      ├─/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
                      │ input:input9 "Video Bus"
                      ├─/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:45/LNXVIDEO:01/input/input10
                      │ input:input10 "Video Bus"
                      ├─/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
                      │ input:input0 "Power Button"
                      ├─/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0D:00/input/input2
                      │ input:input2 "Lid Switch"
                      ├─/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input1
                      │ input:input1 "Sleep Button"
                      ├─/sys/devices/pci0000:00/0000:00:02.0/drm/card0
                      [...]

在这种情况下，`PNP0C0C:00` (`/dev/input/event0`) **是** 一个物理存在的电源按钮。您可以通过抑制电源按钮操作来验证这一点。 
    
    # systemd-inhibit --what=handle-power-key sleep 1h
    
[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 测试的桌面环境列表需要扩展 (在 [Talk:联想 ThinkPad E14 Gen 2 (Intel)](<../zh-cn/Talk:%E8%81%94%E6%83%B3_ThinkPad_E14_Gen_2_\(Intel\).html>) 中讨论)

**注意：**

  * 如果您使用桌面环境，此命令可能对您无效。
  * 已测试无效的桌面环境列表: KDE Plasma, Gnome.
  * 这是因为桌面环境接管了 **handle-power-key** 事件。
  * 要更改此设置，请在对应桌面环境的设置中找到电源管理，然后将按下电源键的反应设为**无** 。

然后追踪事件： 
    
    # stdbuf -o0 evemu-record /dev/input/event0
    
如果提示不存在 `evemu-record`，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [evemu](<https://archlinux.org/packages/?name=evemu>)包. 

按下电源按钮应该会记录一个按下事件。 

固件将发送多次按下电源按钮的事件，因此您的机器很可能只需要几秒钟即可关闭电源。这是因为 systemd 在按下电源按钮时会终止它正在等待的进程/单元。 

有关处理特定密钥的更多信息，请参阅 [logind.conf(5)](<https://man.archlinux.org/man/logind.conf.5>)。 

###  睡眠和唤醒

您可以使用带有睡眠按钮的 USB 键盘。 

还有一个睡眠按钮/暂停键。它是一个由固件处理的虚拟键，在使用 #Unmarked 键绑定之一时会被触发，这会挂起您的设备。使用以下命令来禁止处理挂起键： 
    
    # systemd-inhibit --what=sleep sleep 1h
    
**注意：**

  * **handle-suspend-key** 也被桌面环境接管，请查看 [#电源按钮](<#%E7%94%B5%E6%BA%90%E6%8C%89%E9%92%AE>)。
  * 但 **sleep** 不是。

根据`xev`测试，每个按键都有`XF86WakeUp`的功能。 

所以在使设备睡眠后，您可以按任意键恢复。 

##  功能键

按键  | 可见？1 | 标记？2 | 效果   
---|---|---|---  
`Fn+Esc` | 否 | 是 | 启用 FnLock   
`Fn+F1` | 是 | 是 |  `XF86AudioMute`  
`Fn+F2` | 是 | 是 |  `XF86AudioLowerVolume`  
`Fn+F3` | 是 | 是 |  `XF86AudioRaiseVolume`  
`Fn+F4` | 是 | 是 |  `XF86AudioMicMute`  
`Fn+F5` | 是 | 是 |  `XF86MonBrightnessDown`  
`Fn+F6` | 是 | 是 |  `XF86MonBrightnessUp`  
`Fn+F7` | 是 | 是 |  `XF86Display`  
`Fn+F8` | 是 | 是 |  `XF86WLAN`  
`Fn+F9` | 否 | 是 | 通知中心（仅限 Windows）   
`Fn+F10` | 否 | 是 | 接听（仅限 Windows）   
`Fn+F11` | 否 | 是 | 挂断（仅限 Windows）   
`Fn+F12` | 是 | 是 |  `XF86Favorites`  
`Fn+Print` | 否 | 是 | 选择屏幕截图区域（仅限 Windows）   
  
  1. 按键对 `xev` 和类似工具可见
  2. 物理键上有一个符号，描述了它的功能

###  未标记的键绑定

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 未完成 (在 [Talk:联想 ThinkPad E14 Gen 2 (Intel)](<../zh-cn/Talk:%E8%81%94%E6%83%B3_ThinkPad_E14_Gen_2_\(Intel\).html>) 中讨论)

## Intel Wi-Fi 6 AX201

对于配备英特尔 AX201 Wi-Fi 适配器的型号，该接口在使用电池运行时可以进行节电，这会增加网络延迟。 

为避免此问题，您可以按照 [Power management#Network interfaces](<../zh-cn/Power_management.html#Network_interfaces> "Power management") 中的说明禁用节电。 
