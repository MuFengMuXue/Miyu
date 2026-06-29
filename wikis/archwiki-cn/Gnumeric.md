[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Gnumeric](<../zh-cn/Talk:Gnumeric.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Gnumeric](<https://wiki.archlinux.org/title/Gnumeric> "arch:Gnumeric")，最近一次同步于 2020-05-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gnumeric?diff=0&oldid=612426>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gnumeric_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Gnumeric](<https://en.wikipedia.org/wiki/Gnumeric> "wikipedia:Gnumeric") 是一个功能强大的电子表格应用程序，可以导入和导出各种格式，包括 .csv，HTML，LaTeX，Lotus 1-2-3，OpenDocument Spreadsheet 和 Microsoft Excel。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gnumeric](<https://archlinux.org/packages/?name=gnumeric>)包。 

可选的依赖项是 [psiconv](<https://archlinux.org/packages/?name=psiconv>)包（用于 Psion 5 文件支持），[python2-gobject2](<https://aur.archlinux.org/packages/python2-gobject2/>)AUR（用于 python 插件支持）和 [yelp](<https://archlinux.org/packages/?name=yelp>)包（用于查看帮助手册）。 

##  提示与技巧

Gnumeric 尊重数字小数分隔符的[区域](<../zh-cn/Locale.html> "区域")设置，并将其用于导出，（例如导出到 .csv 文件）。例如 

  * 对于德语区域设置 `de`，数字显示为 `0,5` _（逗号）_ ，
  * 对于英语区域设置 `en`，数字显示为 `0.5` _（点）_ 。

要使用其他语言环境启动 Gnumeric，请运行 
    
     LC_NUMERIC="en" gnumeric
    
##  参见

  * [Gnumeric 官方网站](<http://www.gnumeric.org/>)
