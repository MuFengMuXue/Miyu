**翻译状态：**

  * 本文（或部分内容）译自 [Hardware probe](<https://wiki.archlinux.org/title/Hardware_probe> "arch:Hardware probe")，最近一次同步于 2022-04-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Hardware_probe?diff=0&oldid=692419>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Hardware_probe_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Hardware probe](<https://github.com/linuxhw/hw-probe>) 是一种用于检查硬件设备的可操作性，收集系统日志并有助于[硬件数据库](<https://linux-hardware.org/?distro=Arch>)和[用户统计信息](<https://github.com/linuxhw/Trends/tree/master/Dist/Arch>)的工具。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hw-probe](<https://aur.archlinux.org/packages/hw-probe/>)AUR 包。 

##  用法

进行探查： 
    
    # hw-probe -all -upload
    
解码 ACPI 表（需要 [acpica](<https://archlinux.org/packages/?name=acpica>)包 包）： 
    
    # hw-probe -all -upload -decode-acpi
    
执行简单的图形，硬盘，cpu 和内存测试（需要 [mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包 包）： 
    
    # hw-probe -all -upload -check
    
##  参见

  * [lspci 和其他硬件检测相关的工具](<https://en.wikipedia.org/wiki/Lspci> "wikipedia:Lspci")
