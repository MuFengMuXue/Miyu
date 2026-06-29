**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo ThinkPad X1 Carbon (Gen 8)](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_\(Gen_8\)> "arch:Lenovo ThinkPad X1 Carbon \(Gen 8\)")，最近一次同步于 2021-03-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_\(Gen_8\)?diff=0&oldid=657019>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_\(Gen_8\)_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**This article or section does not follow the[Laptop page guidelines](</wzh/index.php?title=Help:Laptop_page_guidelines&action=edit&redlink=1> "Help:Laptop page guidelines（页面不存在）").**

**Reason:** Stub (Discuss in [Talk:联想 ThinkPad X1 Carbon (Gen 8)](<../zh-cn/Talk:%E8%81%94%E6%83%B3_ThinkPad_X1_Carbon_\(Gen_8\).html>))

相关文章

  * [Lenovo ThinkPad X1 Carbon](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 2)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_2\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 2\)（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 3)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_3\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 3\)（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 4)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_4\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 4\)（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 5)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_5\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 5\)（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 6)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_6\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 6\)（页面不存在）")
  * [Lenovo ThinkPad X1 Carbon (Gen 7)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_7\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 7\)（页面不存在）")
  * [Lenovo ThinkPad X1 Yoga (Gen 3)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Yoga_\(Gen_3\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Yoga \(Gen 3\)（页面不存在）")
  * [Lenovo ThinkPad X1 Yoga (Gen 4)](</wzh/index.php?title=Lenovo_ThinkPad_X1_Yoga_\(Gen_4\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Yoga \(Gen 4\)（页面不存在）")

第八代Lenovo ThinkPad X1 Carrbon发布于2020年初，是一款配备了14寸屏幕、第十代英特尔酷睿处理器并集成[Intel UHD 620](<../zh-cn/Intel_graphics.html> "Intel graphics")显卡的超极本。 

为了确保电脑型号正确，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading")[dmidecode](<https://archlinux.org/packages/?name=dmidecode>)包并运行: 
    
    # dmidecode -s system-version
    ThinkPad X1 Carbon  Gen 8
    
**提示：**<https://www.thinkwiki.org/wiki/ThinkWiki> 含有大量与ThinkPad相关的资源

**硬件** | **是否正常工作** |  **使用模组**  
---|---|---  
[英特尔核显](<../zh-cn/Intel_graphics.html> "Intel graphics") | 是 | i915, (intel_agp)   
[无线局域网卡](<../zh-cn/Network_configuration/Wireless.html#iwlwifi> "Network configuration/Wireless") | 是 | iwlmvm   
[有线网卡转接器](<https://www.lenovo.com/us/en/accessories-and-monitors/cables-and-adapters/adapters/CABLE-BO-Ethernet-Extension-Adapter-2/p/4X90Q84427>) | 是 | ？   
Fibocom移动宽带 | 是¹ | ？   
声卡 | 是 | snd_hda_intel   
麦克风 | 是⁴ | snd_sof   
[触摸板](<../zh-cn/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91.html#%E8%A7%A6%E6%91%B8%E6%9D%BF> "Laptop") | 是 | psmouse, rmi_smbus, i2c_i801   
[指点杆](<../zh-cn/%E6%8C%87%E7%82%B9%E6%9D%86.html> "TrackPoint") | 是 | psmouse, rmi_smbus, i2c_i801   
摄像头 | 是 | uvcvideo   
[指纹传感器](<../zh-cn/Fprint.html> "Fprint") | 是² | ？   
[电源管理](<../zh-cn/Power_management.html> "Power management") | 是³ | ？   
[蓝牙](<../zh-cn/%E8%93%9D%E7%89%99.html> "Bluetooth") | 是 | btusb   
键盘背光灯 | 是 | thinkpad_acpi   
NFC | 否⁵ | ?   
Fn键/多媒体控制键 | 是 | ？   
  
  1. Fibcom LTE移动宽带模块需要使用USB模式以工作在Linux环境下，具体参考[[1]](<https://forums.lenovo.com/t5/Other-Linux-Discussions/How-To-Configure-X1-Carbon-Gen-7-on-Debian-FingerPrint-4G-Modem/td-p/4550327>)和[[2]](<https://github.com/abrasive/xmm7360>)的相关内容
  2. 已有官方[fwupd](<../zh-cn/Fwupd.html> "Fwupd")发布
  3. S3级别的休眠需要更改BIOS设置，详情键[#待机/休眠](<#%E5%BE%85%E6%9C%BA/%E4%BC%91%E7%9C%A0>)。
  4. 使用5.3之前版本的[linux](<https://archlinux.org/packages/?name=linux>)包内核时，内置麦克风不工作。使用5.3或之后版本的内核时，可开启SOF固件,详见see [Talk#Microphone](</wzh/index.php?title=Talk:Lenovo_ThinkPad_X1_Carbon_\(Gen_7\)&action=edit&redlink=1> "Talk:Lenovo ThinkPad X1 Carbon \(Gen 7\)（页面不存在）")。
  5. 联想开发者认为此功能无关紧要（2020年8月）[论坛](<https://forums.lenovo.com/t5/Redhat-Fedora-CentOS/X1-Carbon-Gen8-and-other-models-too-coming-with-Fedora-Linux/m-p/5011378?page=1#5042158>)

##  升级

###  自动 (Linux供应商固件服务)

[联想已于2018年8月宣布加入](<https://blogs.gnome.org/hughsie/2018/08/06/please-welcome-lenovo-to-the-lvfs/>)[Linux供应商固件服务(LVFS)](<https://fwupd.org/>)计划。该计划允许在操作系统内升级固件。BIOS升级文件（可能也包括其他固件，如雷电控制器固件）可以通过[fwupd](<../zh-cn/Fwupd.html> "Fwupd")获取和安装。 

###  手动 (fwupdmgr)

未来联想可能提供能直接通过fwupdmgr安装的固件升级程序。具体可以在[Lenovo ThinkPad X1 Carbon (Gen 8) 驱动](<https://pcsupport.lenovo.com/de/de/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-8th-gen-type-20u9-20ua/20u9/parts/display/compatible>)页面查找Linux相关的.cab文件。 

  1. 确保电源适配器已经稳定连接
  2. 打开终端
  3. 定位到.cab文件所在的路径
  4. 运行`fwupdmgr install xxxxxxxx.cab`升级固件
  5. 重启系统
  6. 系统重启后UEFI固件会被升级

##  待机/休眠

BIOS有两个“睡眠状态”选项：Windows和Linux，可以在 _Config > Power > Sleep State_找到。Linux选项提供传统的S3级电源状态——除了内存外的所有硬件组件全部断电，这个选项可以使休眠正常运作。Windows选项则提供较新的基于软件的待机状态，这一选项在Linux上应该能正常工作。使用Windows选项可能会更快地从休眠中恢复，但也可能会增加电量消耗。 

##  声卡

参考 [Lenovo ThinkPad X1 Carbon (Gen 7)#Audio](</wzh/index.php?title=Lenovo_ThinkPad_X1_Carbon_\(Gen_7\)&action=edit&redlink=1> "Lenovo ThinkPad X1 Carbon \(Gen 7\)（页面不存在）")
