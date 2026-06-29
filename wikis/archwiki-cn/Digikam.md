**翻译状态：**

  * 本文（或部分内容）译自 [Digikam](<https://wiki.archlinux.org/title/Digikam> "arch:Digikam")，最近一次同步于 2024-7-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Digikam?diff=0&oldid=815918>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Digikam_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Digikam](<https://en.wikipedia.org/wiki/Digikam> "wikipedia:Digikam") 是一款基于 KDE 的图像整理工具，通过插件架构内置了编辑功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [digikam](<https://archlinux.org/packages/?name=digikam>)包。 

###  非 KDE 安装

为了在不运行 KDE 桌面环境时正确显示图标（不丢失图标），您必须安装 KDE 图标主题，并在 Digikam 的设置中激活它。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [breeze-icons](<https://archlinux.org/packages/?name=breeze-icons>)包。 

安装完成后，您应配置 Digikam 以使用图标： 

  1. 导航至 _设置 > 配置 digiKam > 其他_
  2. 现在，在 _外观_ 中选择 _Breeze_ 或 _Breeze Dark_ 作为 _图标主题_

重新启动 Digikam ，即可享受应用程序内一致的图标。 

##  问题解决

###  工具提示无法阅读

DigiKam 有自己的窗口小部件风格设置。如果工具提示是空白（空矩形），或由于前景和背景组合不佳而无法阅读，请选择不同的 widget 风格： 

  1. 导航至 _设置 > 配置 digiKam > 其他_
  2. 现在，在 _外观_ 中选择 _Breeze_ 作为 _小部件样式_

摘自 Digikam [文档](<https://docs.digikam.org/en/setup_application/miscs_settings.html#appearance-settings>)： 

    Breeze 风格是所有桌面下的最佳选择。
