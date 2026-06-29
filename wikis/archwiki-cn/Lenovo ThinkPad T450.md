[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Lenovo ThinkPad T450](<../zh-cn/Talk:Lenovo_ThinkPad_T450.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo ThinkPad T450](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T450> "arch:Lenovo ThinkPad T450")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T450?diff=0&oldid=610285>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_T450_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文介绍了有关在 Lenovo Thinkpad T450 笔记本电脑上安装和配置 Arch 的详细信息。 

##  安装

同时支持 UEFI 和 MBR 样式的 BIOS。使用最新版本的 [Archiso](<https://archlinux.org/download/>) 安装 Arch Linux 不会有任何问题。该[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")可以正常工作，除了音响。 

查看 T450s wiki，几乎所有在那里的内容都可以在 T450 上使用：[Lenovo ThinkPad T450s](</wzh/index.php?title=Lenovo_ThinkPad_T450s&action=edit&redlink=1> "Lenovo ThinkPad T450s（页面不存在）")

###  音响

请参阅 [ALSA (简体中文)#设置默认声卡](</wzh/index.php?title=ALSA_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "ALSA \(简体中文\)（页面不存在）")以将默认声卡设置为Intel PCH（扬声器和耳机）。 
    
    /etc/modprobe.d/thinkpad-t450s.conf
    
    options snd_hda_intel index=1,0

重新启动以设置更改。 

###  重新绑定前进和后退键

见 [T420](</wzh/index.php?title=Lenovo_ThinkPad_T420_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Lenovo ThinkPad T420 \(简体中文\)（页面不存在）")
