**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo ThinkPad X13 Gen 1 (AMD)](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X13_Gen_1_\(AMD\)> "arch:Lenovo ThinkPad X13 Gen 1 \(AMD\)")，最近一次同步于 2021-03-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X13_Gen_1_\(AMD\)?diff=0&oldid=656130>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X13_Gen_1_\(AMD\)_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

硬件 | PCI/USB ID | 是否正常工作   
---|---|---  
触摸板 |  | 是   
触摸板按键 |  | 是   
键盘 |  | 是   
显卡 | `8086:2723` | 是   
摄像头 | `04f2:b6d0` | 是   
有线局域网 | `10ec:8168` | 是   
蓝牙 | `8086:2723` | 是   
电源管理 |  | 是   
USB接口 | `10ec:816d` | 是   
SD读卡器 | `` | 是   
HDMI接口 |  | 是   
声卡 | `1022:15e3` | 是   
无线局域网 | `8086:2723` | 是   
指纹传感器 | `06cb:00bd` | 是   
可信平台模块（TPM） |  | 未测试   
  
##  安装

安装过程中无任何特殊步骤。 

### BIOS

建议将BIOS更新至最新版本，本条目撰写时所使用的最新版本为1.30 

BIOS更新文件可以从[X13支持页面](<https://pcsupport.lenovo.com/mx/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x13-type-20uf-20ug/downloads/ds544980-bios-update-utility-bootable-cd-for-windows-10-64-bit-thinkpad-t14s-x13>)以[ISO镜像文件](<https://download.lenovo.com/pccbbs/mobiles/r1cuj60wd.iso>)的形式下载并复制到一个优盘中。 

BIOS中有一个可自定义的电源配置默认是为`Windows 10`设定的。建议将其改成为`Linux`设定，可以减少[#电源管理](<#%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86>)方面的问题。 

##  辅助功能

BIOS提供两种操作模式，**图形模式** 和**纯文本模式** 。 

在图形模式下，可以使用键盘选择各种选项。**左** 和**右** 两个方向键用来选择选项，**空格** 用来激活选项。 

如果像更流畅的使用键盘设定BIOS，推荐使用纯文本模式。 

以下步骤可以将BIOS设置为纯文本模式： 

  * 在**Setup** 选项卡下的左侧栏里选择**Config**
  * 用**右方向键** 定位至右侧栏里的**Setup UI**
  * 选择**Simple Text** 模式
  * 按下**F10** 保存BIOS选项并重启。

**注意：** 视力障碍用户可能需要一个视力正常的人来帮助更改BIOS设定

##  硬件

###  显示

#### Lightdm

Lightdm会因为amdgpu显卡驱动加载过晚而发生问题，使用KMS将显卡驱动加载至initramfs 
    
    /etc/mkinitcpio.conf
    
    MODULES=(amdgpu)

之后重新生成initramfs 
    
    # mkinitcpio -P
    
####  亮度控制

在内核版本5.9下使用原生亮度控制 
    
    /etc/default/grub
    
    GRUB_CMDLINE_LINUX_DEFAULT=".... acpi_backlight=native ...."

之后重建GRUB配置 
    
    # grub-mkconfig -o /boot/grub/grub.cfg
    
###  声卡

PulseAudio无需任何设定就可以正常工作，但是其默认选择的ALSA音频设备可能不正确。可能需要通过如下文件更改默认设别： 
    
    /etc/asound.conf
    
    defaults.pcm.card 2
    defaults.ctl.card 2
    
记得使用alsamixer应用取消静音： 
    
    $ alsamixer
    
使用alsactl应用永久保留设置： 
    
    # alsactl store
    
##  固件

[fwupd](<../zh-cn/Fwupd.html> "Fwupd") 暂不支持此设备。 

##  电源管理

此设备从休眠中恢复存在很多问题，为了解决这些问题，请参考[#BIOS](<#BIOS>)章节中的方法。 

如果系统使用sd-encrypt进行了全盘加密，建议切换至使用`encrypt`的mkinitcpio钩子。 

##  功能键

按键  | 可见？1 | 图标？2 | 效果   
---|---|---|---  
`Fn` | 是 | 否 |  `XF86WakeUp`  
`Fn+Esc` | 否 | 是 | 开启Fn锁   
`Fn+F1` | 是 | 是 |  `XF86AudioMute`  
`Fn+F2` | 是 | 是 |  `XF86AudioLowerVolume`  
`Fn+F3` | 是 | 是 |  `XF86AudioRaiseVolume`  
`Fn+F4` | 是 | 是 |  `XF86AudioMicMute`  
`Fn+F5` | 否 | 是 | 降低显示器亮度   
`Fn+F6` | 否 | 是 | 提高显示器亮度   
`Fn+F7` | 是 | 是 |  `XF86Display`  
`Fn+F8` | 是 | 是 |  `XF86WLAN`3  
`Fn+F9` | 否 | 是 |   
`Fn+F10` | 否 | 是 |   
`Fn+F11` | 否 | 是 |   
`Fn+F12` | 是 | 是 |  `XF86Favorites`  
`Fn+Space` | 否 | 是 | 开启/关闭键盘灯   
`Fn+4` | 是 | 否 |  `XF86Sleep`3  
`Fn+B` | 是 | 否 |  `Ctrl_L + Break`  
`Fn+P` | 是 | 否 |  `Pause`  
`Fn+K` | 是 | 否 |  `Scroll Lock`  
`Fn+Left` | 是 | 否 |  `Home`  
`Fn+Right` | 是 | 否 |  `End`  
`Fn+S` | 是 | 否 |  `Alt_L + SysRq `  
`Fn+End` | 是 | 否 |  `Ins`  
  
  1. 按键可以通过`xev`或类似工具被探测到。
  2. 物理按键上有显示其功能的图标
  3. 默认由systemd-logind管理

##  参考

  * 产品配置: <https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_x13_Gen_1_AMD/ThinkPad_x13_Gen_1_AMD_Spec.PDF>
  * 官方维护手册: <https://download.lenovo.com/pccbbs/mobiles_pdf/t14s_gen1_x13_gen1_hmm_en.pdf>
  * <https://certification.ubuntu.com/hardware/202006-27979>
