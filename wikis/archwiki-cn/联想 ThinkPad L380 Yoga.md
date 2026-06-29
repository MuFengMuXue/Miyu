**翻译状态：**

  * 本文（或部分内容）译自 [Lenovo ThinkPad L380 Yoga](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_L380_Yoga> "arch:Lenovo ThinkPad L380 Yoga")，最近一次同步于 2020-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_L380_Yoga?diff=0&oldid=605270>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lenovo_ThinkPad_L380_Yoga_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

为确保您拥有此笔记本，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [dmidecode](<https://archlinux.org/packages/?name=dmidecode>)包 然后运行: 
    
    # dmidecode -t system | grep Version
    
    Version: ThinkPad L380 Yoga
    
##  配置

###  SD 卡

开箱即用，只是不要忘记 exfat-utils。 

### Wacom

开箱即用。 

有关更多配置，请参见[Tablet PC](</wzh/index.php?title=Tablet_PC&action=edit&redlink=1> "Tablet PC（页面不存在）")。 

##  附加功能

安装 [iio-sensor-proxy](<https://archlinux.org/packages/?name=iio-sensor-proxy>)包 以便在GNOME下自动旋转屏幕和调节亮度。 

[thinkpad-yoga-scripts-git](<https://aur.archlinux.org/packages/thinkpad-yoga-scripts-git/>)AUR 不能很好的工作，因为触摸板和指点杆制造商改变。而是使用 <https://github.com/ffejery/thinkpad-l380-yoga-scripts> ，有关如何构建的信息，请参见[makepkg](<../zh-cn/Makepkg.html> "Makepkg")。还有一个AUR包: [thinkpad-l380-yoga-scripts-git](<https://aur.archlinux.org/packages/thinkpad-l380-yoga-scripts-git/>)AUR。请把`/opt/thinkpad-l380-yoga-scripts/rotate/thinkpad-rotate.py` 按照自述文件中的提示进行编辑，因为您可能希望触摸屏和笔与屏幕一起旋转。 
