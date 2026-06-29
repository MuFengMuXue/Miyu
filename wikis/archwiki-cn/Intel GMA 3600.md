**翻译状态：**

  * 本文（或部分内容）译自 [Intel_GMA3600](<https://wiki.archlinux.org/title/Intel_GMA3600> "arch:Intel GMA3600")，最近一次同步于 2017-10-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Intel_GMA3600?diff=0&oldid=361396>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Intel_GMA3600_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** No updates since 2017, changes have occurred on the English page since. （在 [Talk:Intel GMA 3600#](<../zh-cn/Talk:Intel_GMA_3600.html>) 中讨论）

Intel GMA3600 是基于 PowerVR SGX 545 显示核心的集成显卡，搭载于 Atom N2600,N2800,D2550 中。 

Linux 内核从 3.5 版本开始支持此设备。 

##  Xorg 驱动

目前没有单独的 Xorg 驱动，请使用 [xorg-server](<https://archlinux.org/packages/?name=xorg-server>)包 提供的 modesetting 驱动: 
    
    /etc/X11/xorg.conf.d/20-gpudriver.conf
    
    Section "Device"
        Identifier "Intel GMA3600"
        Driver     "modesetting"
    EndSection
    
modesetting 驱动可以使用 xrandr 禁用/启用 LVDS, VGA 等端口，修改分辨率. 

下面设置可以禁用 LVDS 并强制启用 VGA： 
    
    /etc/X11/xorg.conf.d/20-gpudriver.conf
    
    Section "Device"
        Identifier "Intel GMA3600"
        Driver     "modesetting"
        Option     "Monitor-LVDS-0" "Ignore"
        Option     "Monitor-VGA-0" "Monitor"
    EndSection
    
    Section "Monitor"
        Identifier "Ignore"
        Option     "Ignore"
    EndSection
    
    Section "Monitor"
        Identifier "Monitor"
        Option     "Enable"
    EndSection
    
##  问题解决

###  恢复后黑屏

如果恢复系统后黑屏，请执行： 
    
    # touch /etc/pm/sleep.d/99video
    
###  播放视频

目前没有办法使用视频加速，可以用 Atom CPU 用多线程解码: 
    
    mplayer -lavdopts threads=4 -fs myvideo.avi
    
##  参阅

  * <https://www.change.org/en-GB/petitions/intel-listen-to-the-community-and-develop-gma3600-drivers-for-linux>
  * <https://ubuntuforums.org/showthread.php?t=1953734>
  * <https://communities.intel.com/message/158477>
