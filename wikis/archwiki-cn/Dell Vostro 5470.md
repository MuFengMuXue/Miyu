[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Dell Vostro 5470](<../zh-cn/Talk:Dell_Vostro_5470.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Dell Vostro 5470](<https://wiki.archlinux.org/title/Dell_Vostro_5470> "arch:Dell Vostro 5470")，最近一次同步于 2020-05-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dell_Vostro_5470?diff=0&oldid=609058>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dell_Vostro_5470_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

该页面涉及在 Dell Vostro 5470 笔记本电脑上配置 Arch Linux。 

## CPU

这台笔记本电脑有几种 CPU 配置，具体取决于购买的配置。此文档使用 Core i7-4500U CPU。 
    
    # uname -p
    
该 CPU 具有[频率缩放功能](<../zh-cn/CPU_frequency_scaling.html> "CPU frequency scaling"). 

##  触摸屏

开箱即用。 

## GPU

显卡：NVIDIA Corporation GK208M [GeForce GT 740M] 

###  Bumblebee 和 NVIDIA 专有驱动程序

安装 intel 视频驱动程序 

安装 Bumblebee 

将用户添加到 bumblebee 组 
    
    # systemctl enable bumblebeed
    
安装 NVIDIA 专有驱动程序 

[bbswitch](<https://archlinux.org/packages/?name=bbswitch>)包

[primus](<https://archlinux.org/packages/?name=primus>)包

##  网络

###  无线网络

开箱即用 
