[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Thinkpad Fan Control](<../zh-cn/Talk:Thinkpad_Fan_Control.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Thinkpad Fan Control](<https://wiki.archlinux.org/title/Thinkpad_Fan_Control> "arch:Thinkpad Fan Control")，最近一次同步于 2017-03-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Thinkpad_Fan_Control?diff=0&oldid=471075>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Thinkpad_Fan_Control_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

在默认情况下由内嵌控制器控制风扇转速。如果您认为风扇转速过低或过大，您可能需要一个守护进程接管控制权。但这是有风险的：您需要负责控制温度。过高的温度会损坏或者缩短笔记本组件的使用寿命。 

来自 [http://www.thinkwiki.org/wiki/How_to_control_fan_speed：](<http://www.thinkwiki.org/wiki/How_to_control_fan_speed%EF%BC%9A>)

    _出于安全考虑，默认禁止用户控制风扇。若想启用风扇控制，必须在加载内核模块 thinkpad-acpi 时传递参数 fan_control=1_

当前可用于控制风扇的守护进程存在于 [Arch 用户软件仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "Arch 用户软件仓库")中， 分别是 [simpfand-git](<https://aur.archlinux.org/packages/simpfand-git/>)AUR 和 [thinkfan](<https://aur.archlinux.org/packages/thinkfan/>)AUR。 

##  安装

安装 [thinkfan](<https://aur.archlinux.org/packages/thinkfan/>)AUR。然后查看其文件列表： 
    
    # pacman -Ql thinkfan
    
请注意 thinkfan 包安装了文件 /usr/lib/modprobe.d/thinkpad_acpi.conf，该文件包含： 
    
    options thinkpad_acpi fan_control=1
    
因此，默认启用了风扇控制。 
    
    $ su
    # modprobe thinkpad_acpi
    # cat /proc/acpi/ibm/fan
    
您应该会看到风扇运行级别默认为 “auto”，您可以向这个文件写入运行级别的方式手动控制风扇转速。thinkfan 守护进程将会自动控制风扇转速。 

您需要复制一份默认配置文件（例如 /usr/share/doc/thinkfan/examples/thinkfan.conf.simple) 到 /etc/thinkfan.conf，并尝试修改它。需要在这个配置文件中指定读取哪些传感器，并且也需要指定用户控制风扇转速的接口。一些操作系统提供了 /proc/acpi/ibm/fan，对于其他操作系统，you will need to specify something like 
    
    hwmon /sys/devices/virtual/thermal/thermal_zone0/temp
    
to use generic hwmon sensors instead of thinkpad-specific ones. 

##  运行

您可以通过手动运行 thinkfan 命令测试配置（root用户）： 
    
    # thinkfan -n
    
and see how it reacts to the load level of whatever other programs you have running. 

当您的配置正确时，可通过如下命令启动 thinkfan 守护进程（root 用户）： 
    
    # systemctl start thinkfan
    
或者在系统启动时自动加载它： 
    
    # systemctl enable thinkfan
    
## Old packages which have gone missing

[tpfand](<https://aur.archlinux.org/packages/tpfand/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] and a version that doesn't require [HAL](<../zh-cn/Udev.html> "HAL") [tpfand-no-hal](<https://aur.archlinux.org/packages/tpfand-no-hal/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] are not actively developed anymore, and no longer available. An additional GTK+ frontend was provided in the [tpfan-admin](<https://aur.archlinux.org/packages/tpfan-admin/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] package in the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") which enables the monitoring of temperatures as well as the graphical adjustment of trigger points. 

Due to tpfand not beeing actively developed anymore, there was a fork called tpfanco (which in fact uses the same names for the executables as tpfand): [tpfanco-svn](<https://aur.archlinux.org/packages/tpfanco-svn/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 

The configuration file for tpfand (same for tpfanco) was `/etc/tpfand.conf`. 

Additionally, the [tpfand-profiles](<https://aur.archlinux.org/packages/tpfand-profiles/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] package in the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") provided the latest fan profiles for various thinkpad models. 
