[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Quvi](<../zh-cn/Talk:Quvi.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Quvi](<https://wiki.archlinux.org/title/Quvi> "arch:Quvi")，最近一次同步于 2020-05-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Quvi?diff=0&oldid=611818>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Quvi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**quvi** 解析 Internet 应用程序的媒体流 URL，否则将不得不使用 Adobe Flash 多媒体平台访问媒体流。典型的例子是使用该“多媒体平台”来传递其内容的视频的不同媒体主机，例如 YouTube。 

来源：[项目主页](<http://quvi.sourceforge.net/>)

##  安装

安装 [quvi](<https://aur.archlinux.org/packages/quvi/>)AUR。 

##  用法

从 URL 播放视频的最简单方法是使用 
    
    $ quvi "<url>" --exec "mplayer %u"
    
可以通过创建将其配置为默认行为 
    
    ~/.quvirc
    
    exec = "mplayer %u"

##  相关链接

  * [Quvi 主页](<http://quvi.sourceforge.net/>)
