[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Microsoft Surface Pro 3](<../zh-cn/Talk:Microsoft_Surface_Pro_3.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Microsoft_Surface_Pro_3](<https://wiki.archlinux.org/title/Microsoft_Surface_Pro_3> "arch:Microsoft Surface Pro 3")，最近一次同步于 2016-01-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Microsoft_Surface_Pro_3?diff=0&oldid=420251>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Microsoft_Surface_Pro_3_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：**[Help:Style#Language register](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html#Language_register> "Help:Style")（在[Talk:Microsoft Surface Pro 3](<../zh-cn/Talk:Microsoft_Surface_Pro_3.html>)讨论）

设备 | PCI/USB ID | 是否正常工作？   
---|---|---  
图形处理器 | `8086:0a16` | 是   
Wi-Fi | `11ab:2b38` | 是   
蓝牙 | `1286:204b` | 是   
网络摄像头 (前) | `045e:07be` | 是   
网络摄像头 (后) | `045e:07bf` | 是   
  
**警告：** 设备的保修仅在OEM版Windows仍然存在时有效,官方解释,双启动不会使保修失效.[这里](<https://answers.microsoft.com/en-us/surface/forum/surfpro-surfusingpro/would-dual-booting-the-surface-pro-void-its/da549e24-f986-4984-b081-25c029882163>).

本文记录了所有使Arch Linux在Surface Pro 3上工作的所有有效信息. 

##  启动进入安装

为了从USB启动,你需要做一些配置让平板从USB或者SD卡启动.另外,你可能需要暂时无视禁止[Secure Boot](<../zh-cn/Unified_Extensible_Firmware_Interface/Secure_Boot.html> "Unified Extensible Firmware Interface/Secure Boot")而导致启动时的一个丑陋的红色背景. 

Surface Pro 3有三种启动模式[详细看这里](<https://www.microsoft.com/surface/en-us/support/storage-files-and-folders/boot-surface-pro-from-usb-recovery-device>): 

  1. 普通模式 
     1. 按电源键。 你能从UEFI设置里的 "Alternate Boot order"改变启动顺序。
  2. 进入BIOS设置 
     1. 关闭电源 (或者重启如果你手速够快)
     2. 按住音量上
     3. 按电源键
     4. 等Surface的LOGO出现
     5. 放开音量上
  3. 从USB/SD卡启动 
     1. 关闭电源
     2. 按住音量下
     3. 按电源键
     4. 等Surface的LOGO出现
     5. 放开音量下

###  禁用Secure Boot

**注意：** 这会导致启动时有一个丑陋的红色背景

进入UEFI设置选择 _Secure Boot Control > Disable_.现在接着安装.[Microsoft 更多信息](<https://www.microsoft.com/surface/en-sg/support/warranty-service-and-recovery/how-to-use-the-bios-uefi>)

###  开启Secure Boot启动安装镜像

看这里[Secure Boot](<../zh-cn/Secure_Boot.html> "Secure Boot"). 

##  额外的步骤

虽然在最新的内核中已经支持了触摸屏,屏幕等等.但是它不支持摄像头,多点触控,Type Cover等.在Github上有为Surface Pro 3专制的内核:[[1]](<https://github.com/nuclearsandwich/surface3-archlinux>).改项目设法支持了这些设备.你可以直接在AUR[linux-surfacepro3](<https://aur.archlinux.org/packages/linux-surfacepro3/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]中安装或自行编译. 

###  编译内核

Ref: [Kernel/Traditional compilation#Kernel configuration](<../zh-cn/Kernel/Traditional_compilation.html#Kernel_configuration> "Kernel/Traditional compilation")

**注意：** 最新的内核补丁是[shvr's github repository](<https://github.com/shvr/fedora-surface-pro-3-kernel/>). 

  * Latest stable kernel release: [f23 branch](<https://github.com/shvr/fedora-surface-pro-3-kernel/commits/f23>)
  * Latest RC: [master branch](<https://github.com/shvr/fedora-surface-pro-3-kernel/commits/master>)

####  Surface Pro 3 Linux 其他内核补丁

  * [Camera patch](<https://github.com/lizalc/fedora-surface-pro-3-kernel/blob/b123951d60ef5c7d34a943af5f59989624978857/surface-pro-3-Add-support-driver-for-Surface-Pro-3-b.patch>)
  * [Hardware Buttons patch](<https://github.com/lizalc/fedora-surface-pro-3-kernel/blob/78354d93564831444a6c52ff0155e7cca0b12170/Add-Microsoft-Surface-Pro-3-camera-support.patch>)
  * [Type Cover patch](<https://github.com/shvr/fedora-surface-pro-3-kernel/blob/f23/Add-multitouch-support-for-Microsoft-Type-Cover-3.patch>)

**注意：** 使用`git-apply`可以自动添加这些.

###  启用触摸板

Ref: [Reddit](<https://www.reddit.com/r/SurfaceLinux/comments/3lbgs4/ubuntu_gnome_1510/>)

安装[xf86-input-synaptics](<https://archlinux.org/packages/?name=xf86-input-synaptics>)包并在`/usr/share/X11/xorg.conf.d/10-evdev.conf`添加: 
    
    Section "InputClass"··
        Identifier "Surface Pro 3 cover"
        MatchIsPointer "on"
        MatchDevicePath "/dev/input/event*"
        Driver "evdev"
        Option "vendor" "045e"
        Option "product" "07dc"
        Option "IgnoreAbsoluteAxes" "True"
    EndSection
    
###  重新启用Secure Boot

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[UEFI#Secure boot](<../zh-cn/UEFI.html#Secure_boot> "UEFI")。**

**附注：** Generic instructions（在 [Talk:Microsoft Surface Pro 3](<../zh-cn/Talk:Microsoft_Surface_Pro_3.html>) 中讨论）

## Troubleshooting

### Invalid signature detected check secure boot policy in setup

This happened to me after deleting the Secure Boot database and initializing it with Microsoft & CAs. I also had to do the recovery of the bitlocker partition, but I would follow these steps: 

  1. After the reset, switch off and try to boot from the sd/usb. If you do not succeed and get the message many times: 
     1. Leaving all TPM & SecureBoot enabled and SSD Only alternate system order
     2. Do another database reset
     3. Enroll the Microsoft and CAs again
     4. reboot into sd/usb with volume down
     5. It should work now
  2. Follow steps in the Secure Boot installation
  3. After the full installation of Arch Linux, when you have it working, do the BitLocker recovery

If after doing these steps does not still work. Flash the archiso image once more and try again, 

### Keyboard Cover not working

This can happen sometimes when you restart. The solution was to shutdown and reboot. (not restart) 
