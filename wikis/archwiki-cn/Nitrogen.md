**翻译状态：**

  * 本文（或部分内容）译自 [Nitrogen](<https://wiki.archlinux.org/title/Nitrogen> "arch:Nitrogen")，最近一次同步于 2025-02-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nitrogen?diff=0&oldid=705863>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nitrogen_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Feh](<../zh-cn/Feh.html> "Feh")

[Nitrogen](<https://github.com/l3ib/nitrogen/>) 是一种快速且轻量级 (基于GTK2) 的 X Window 桌面背景浏览器和设置器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nitrogen](<https://archlinux.org/packages/?name=nitrogen>)包 包。 

##  用法

运行 `nitrogen --help` 以获取完整详细信息。 以下示例将帮助您入门： 

###  设置壁纸

要从特定目录递归查看和设置所需的壁纸，请运行： 
    
    $ nitrogen /path/to/image/directory/
    
要以非递归方式查看和设置特定目录中的所需壁纸，请运行： 
    
    $ nitrogen --no-recurse /path/to/image/directory/
    
###  恢复壁纸

要在后续会话中还原所选的墙纸，请[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")以下命令： 
    
    $ nitrogen --restore &
    
##  故障排除

###  双显示器冻结

删除当前的 nitrogen 配置：[[1]](<https://bbs.archlinux.org/viewtopic.php?id=46245>)
    
    $ rm -r ~/.config/nitrogen/
    