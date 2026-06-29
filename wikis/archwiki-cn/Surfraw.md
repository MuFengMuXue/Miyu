**翻译状态：**

  * 本文（或部分内容）译自 [Surfraw](<https://wiki.archlinux.org/title/Surfraw> "arch:Surfraw")，最近一次同步于 2024-6-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Surfraw?diff=0&oldid=810958>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Surfraw_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Surfraw](<https://en.wikipedia.org/wiki/Surfraw> "wikipedia:Surfraw") 为各种流行的 WWW 搜索引擎提供了一个快速的 UNIX 命令行界面。Surfraw 最初是由 Julian Assange 创建的。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [surfraw](<https://archlinux.org/packages/?name=surfraw>)包 软件包。 

##  配置

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 译者未充分理解部分内容，如果您的翻译更佳，可以参与贡献。（在 [Talk:Surfraw#配置](<../zh-cn/Talk:Surfraw.html#%E9%85%8D%E7%BD%AE>) 中讨论）

Surfraw 使用默认浏览器打开成功的查询。如果没有安装任何标准浏览器，Surfraw 将调用 $BROWSER。如果该变量为空，您将收到一条错误信息，因为 Surfraw 无法打开查询。您可以通过 `~/.config/surfraw/conf` 配置浏览器和其他选项： 
    
    SURFRAW_graphical_browser=/usr/bin/chromium
    #SURFRAW_text_browser=/usr/bin/elinks
    SURFRAW_graphical=yes
    
默认配置文件安装在 `/etc/xdg/surfraw/conf` 中，其中包含所有可配置选项。 

##  用法

Surfraw 由一组称为 elvi 的 shell 脚本组成，每个脚本都能搜索特定网站。 

要查看 elvi 列表，请键入： 
    
    $ surfraw -elvi
    
您可以使用 surfraw 的全称，也可以使用 surfraw 的简称： 
    
    $ sr duckduckgo _topic_name_
    
你也可以将 `/usr/lib/surfraw` 添加到 `$PATH` 中，以直接调用 elvi。 

有 100 多种 elvi 可供在网上搜索，如亚马逊网站： 
    
    $ surfraw amazon -search=books -country=en -q Stanislaw Lem 
    
要搜索 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"): 
    
    $ sr aur _package_name_
    
要搜索 ArchWiki: 
    
    $ sr archwiki _article_name_
    
有关网站搜索脚本的完整列表，请参见 [Elvi 列表](<https://gitlab.com/surfraw/Surfraw/wikis/current-elvi>)
