**翻译状态：**

  * 本文（或部分内容）译自 [sdcv](<https://wiki.archlinux.org/title/sdcv> "arch:sdcv")，最近一次同步于 2024-07-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/sdcv?diff=0&oldid=813154>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/sdcv_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[sdcv](<https://dushistov.github.io/sdcv>) 是一个命令行字典。它提供对 [StarDict](<https://en.wikipedia.org/wiki/StarDict> "wikipedia:StarDict") 格式的字典的访问。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sdcv](<https://archlinux.org/packages/?name=sdcv>)包 软件包。 

##  用法

[sdcv](<https://archlinux.org/packages/?name=sdcv>)包 可以从命令行启动： 
    
    $ sdcv
    
这为您提供了一个“类 shell”的命令行，您可以从中查询数据库。 

##  添加字典

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Mention [AUR 软件包](<https://aur.archlinux.org/packages?O=0&SeB=nd&K=stardict-&outdated=&SB=p&SO=d&PP=50&submit=Go>). (在 [Talk:Sdcv](<../zh-cn/Talk:Sdcv.html>) 中讨论)

网上有很多地方可以下载 StarDict 词典（例如 [[1]](<https://web.archive.org/web/20200702000038/>) [[2]](<http://download.huzheng.org/>)）。 

一旦你有了合适的文件，你就可以将它们解压到 `/usr/share/stardict/dic`。 

如果您没有 root 权限，您可以设置 `STARDICT_DATA_DIR` [环境变量](<../zh-cn/Environment_variable.html> "Environment variable")： 
    
    STARDICT_DATA_DIR=$XDG_DATA_HOME
    
sdcv 将在 `dic` 子目录中查找，因此请确保已创建它，然后将您的字典文件放入其中。 

如果一切都正确完成，sdcv 应该能够输出传递给它的单词的定义。 

##  技巧提示

###  输出格式

您可以使用 sdcv 的包装器来方便地格式化其输出（[Source](<https://owenh.net/stardict>)）： 
    
    function def() {
    	sdcv -n --utf8-output --color "$@" 2>&1 | \
    	fold --width=$(tput cols) | \
    	less --quit-if-one-screen -RX
    }
    
一个[环境变量](<../zh-cn/Environment_variable.html> "Environment variable")可以实现类似的格式化功能，而不需要包装器，影响 `sdcv` 的所有正常调： 
    
    SDCV_PAGER='less --quit-if-one-screen -RX'
    
管道也有效： 
    
    SDCV_PAGER='lolcat -f | less --quit-if-one-screen -RX'
    
##  另见

  * [官方网站](<https://sdcv.sourceforge.net/>)
  * [owenh.net - StarDict 词典](<https://owenh.net/stardict>)
  * [在 askubuntu.com 上发帖](<https://askubuntu.com/a/191268>)
