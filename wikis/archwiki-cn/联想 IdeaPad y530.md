**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo IdeaPad y530](<https://wiki.archlinux.org/title/Lenovo_IdeaPad_y530> "arch:Lenovo IdeaPad y530")，最近一次同步于 2020-05-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_IdeaPad_y530?diff=0&oldid=610393>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_IdeaPad_y530_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

##  使计算机可以工作

###  启用所有扬声器
    
    echo "options snd_hda_intel model=lenovo-sky" >> /etc/modprobe.d/modprobe.conf
    
###  亮度错误的解决方法

Lenovo Ideapad Y530 具有 ACPI 系统的非常规实现。正在开发内核补丁（2.6.29）。在其发布之前，以下解决方法应能帮助控制显示亮度，使其超出键盘快捷键的有限功能。 

要查看可用选项列表： 
    
    cat /proc/acpi/video/VGA/LCDD/brightness
    
将以下命令中的 XX 替换为所需的显示亮度。 
    
    echo XX > /proc/acpi/video/VGA/LCDD/brightness
    
显示最高亮度： 
    
    echo 65 > /proc/acpi/video/VGA/LCDD/brightness
    
###  工作期间打开/关闭 wifi

有任何想法吗？目前，您必须重新启动才能使其正常运行。 
