相关文章

  * [KDE](<../zh-cn/KDE.html> "KDE")
  * [Yakuake](<../zh-cn/Yakuake.html> "Yakuake")

**翻译状态：**

  * 本文（或部分内容）译自 [Konsole](<https://wiki.archlinux.org/title/Konsole> "arch:Konsole")，最近一次同步于 2023-05-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Konsole?diff=0&oldid=734990>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Konsole_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Konsole](<https://apps.kde.org/en/konsole>) 是 KDE 桌面的一个终端模拟器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [konsole](<https://archlinux.org/packages/?name=konsole>)包 软件包。 

##  问题解决

###  真彩程序无法正确显示

这是因为默认情况下， _konsole_ 不会正确设置 `TERM` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。要设置它，编辑 _konsole_ 配置或新建一个配置： 
    
    ~/.local/share/konsole/konsole.profile
    
    [General]
    Name=konsole
    Environment=TERM=konsole-direct,COLORTERM=truecolor

**注意：** 在将 `TERM` 设置为 `konsole-direct` 后，一些程序可能无法正常工作。这时，使用 `konsole-256color`。

##  参见

  * [KDE UserBase Wiki 上的 Konsole](<https://userbase.kde.org/Konsole>)
