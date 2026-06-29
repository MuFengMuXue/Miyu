**翻译状态：**

  * 本文（或部分内容）译自 [Notion](<https://wiki.archlinux.org/title/Notion> "arch:Notion")，最近一次同步于 2020-05-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Notion?diff=0&oldid=615719>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Notion_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")

[Notion](<https://notionwm.net/>) 是 X 的平铺，选项卡式的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [notion](<https://archlinux.org/packages/?name=notion>)包。 

##  启动

使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 运行 `notion`。 

###  使用显示管理器

要使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动/选择 Notion，可以在 `/usr/share/xsessions/` 目录中创建一个标准的 .desktop 文件。 以下是一个示例 `notion.desktop` 文件： 
    
    [Desktop Entry]
    Name=Notion
    Comment=This session logs you into Notion
    Exec=/usr/bin/notion
    TryExec=/usr/bin/notion
    Icon=
    Type=XSession
    
有关更多详细信息，请参见[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")文章。 

##  用法

您可以在使用过程中使用 F1 键并按 return 键来查看 Notion 的手册页，这将告诉您 Notion 的默认键绑定。您也可以通过按 F1 键，输入程序名称并按 return 键来访问其他程序的手册页。除了手册之外，还有一个快速[入门指南](<https://notionwm.net/tour.html>)，快速概述了 Notion。 

##  配置

可以使用 Lua 配置 Notion。首先，将 `/etc/notion/cfg_notion.lua` 复制到 `~/.notion`。有关更多信息，请阅读[使用 Lua 配置和扩展 Notion](<https://raboof.github.io/notion-doc/notionconf/>)。 

##  参见

  * <https://notionwm.net/> \- Notion 网站
  * <https://raboof.github.io/notion-doc/notionconf/> \- 使用 Lua 配置和扩展 Notion
  * <https://github.com/raboof/notion/> \- Notion GitHub
