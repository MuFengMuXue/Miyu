[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:YEd](<../zh-cn/Talk:YEd.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [YEd](<https://wiki.archlinux.org/title/YEd> "arch:YEd")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/YEd?diff=0&oldid=610293>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/YEd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[yEd](<http://www.yworks.com/en/products_yed_about.html>) 是用 Java 编写的功能强大的图形编辑器，可用于生成图。可以手动创建图，也可以从外部数据导入图以进行分析。如果需要，自动布局算法会安排数据集。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [yed](<https://aur.archlinux.org/packages/yed/>)AUR，它在 [AUR](<../zh-cn/AUR_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "AUR \(简体中文\)") 中可用。它需要一个已安装的 Java 运行时环境，例如 [jre7-openjdk](<https://archlinux.org/packages/?name=jre7-openjdk>)包 或 [jre](<https://aur.archlinux.org/packages/jre/>)AUR。 

安装后，可以使用 `yed` 命令运行 yEd。 

##  技巧与窍门

###  字体问题

如果遇到字体问题（例如[故障字体](<http://i.imgur.com/mcvU014.png>)），请尝试使用专有的 [jre](<https://aur.archlinux.org/packages/jre/>)AUR 而不是 OpenJDK，并将以下行添加到 shell 的 rc 文件： 
    
    export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=lcd_hrgb'
    