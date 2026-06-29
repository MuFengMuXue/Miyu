  
ZIM 是一个存储维基内容以离线阅读的开放文件格式。 

##  安装

  * [zim](<https://archlinux.org/packages/?name=zim>)包: 图形界面编辑器。
  * [zim-git](<https://aur.archlinux.org/packages/zim-git/>)AUR: 最新的开发中的 git 版本。
  * [Kiwix](<https://en.wikipedia.org/wiki/Kiwix> "wikipedia:Kiwix"): 离线的 ZIM 阅读器，可以通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kiwix-desktop](<https://archlinux.org/packages/?name=kiwix-desktop>)包 包获取。这个项目包括了移动端的版本，以及一个 ZIM 文件的[在线图书馆](<https://library.kiwix.org/>)。
  * [网页存档](<https://github.com/birros/web-archives>)
  * [goldendict-ng](<https://aur.archlinux.org/packages/goldendict-ng/>)AUR: 支持 ZIM 格式的电子辞典。

终端工具： 

  * [zim-tools](<https://archlinux.org/packages/?name=zim-tools>)包
  * [kiwix-tools](<https://archlinux.org/packages/?name=kiwix-tools>)包: 通过服务器请求的命令行界面阅读，而不是下载整个 ZIM 数据库。

##  用途

Zim 可以用于： 

  * 保存笔记存档
  * 在会议或演讲时记笔记
  * 记录任务列表
  * 头脑风暴

[这段录屏](<https://www.youtube.com/watch?v=yBZpWgzO9Ps>)展示了它的基本功能。 

##  配置

Zim 使用 [XDG 基本目录规范](<../zh-cn/XDG_Base_Directory.html> "XDG Base Directory")。 

当新的维基创建的时候，在这个配置目录下会创建一个目录。这些目录使用富文本格式存储了所有的维基页面。 

##  技巧

一些可以用来完成任务的特别技巧。 

###  插件

Zim 提供了许多有用但没有默认开启的插件。它们可以在 _编辑 >首选项>插件_中找到。它们都提供一个托盘图标。 

#### Spell checker

The requirements for the Spell Checker plugin are as follows: [gtkspell3](<https://archlinux.org/packages/?name=gtkspell3>)包 and [aspell-en](<https://archlinux.org/packages/?name=aspell-en>)包. 

Change `aspell-en` to your desired language support. Now you can configure the Spell Checker and define the default language, in my case `en_GB`. If you do not want Zim to spell-check based on your system default language, go to _File > Properties > Spell Checker_ and enter a language code such as `en_US` or `en_GB`. 

#### Source View

The requirements for Source View are as follows: [gtksourceview3](<https://archlinux.org/packages/?name=gtksourceview3>)包

##  排障

### Problems at launch

A common error is at start up resulting in a error message like the following [this thread](<https://bbs.archlinux.org/viewtopic.php?id=120139>): 
    
    UnboundLocalError: local variable 'i' referenced before assignment
    
It is often related to a problem with the file path of the wikis stored in `~/.config/zim/notebooks.list`. Try to delete or move this file and restart Zim. 

### Error: Unable to find or create trash directory

This error message indicates that Zim is not able to find the trash directory as in [this thread](<https://bbs.archlinux.org/viewtopic.php?id=126413>). This occurs when the wiki is stored on a partition that does not have any trash directory under `/partition/.local/share/Trash`. Due to that one is not able to delete pages as Zim tries to move them to the trash. Solutions are either the creation of a trash directory or the installation of the developer snapshot instead of the stable version which permanently deletes a page if no trash directory can be found. Thus, the user does not receive this error message anymore. 

## See also

  * [Zim homepage](<https://www.zim-wiki.org/>)
  * [Zim official manual](<https://zim-wiki.org/manual/Start.html>)
  * [A short screencast](<https://www.youtube.com/watch?v=yBZpWgzO9Ps>)
  * [Zim community documentation](<https://github.com/jaap-karssenberg/zim-wiki/wiki>)
  * [Getting work done in Zim](<https://www.glump.net/content/getting-work-done-in-zim/getting-work-done-in-zim.html>)
  * [Zim content pulled from various Wikis](<https://wiki.kiwix.org/wiki/Content_in_all_languages>)
