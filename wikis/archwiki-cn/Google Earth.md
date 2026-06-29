[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Google Earth](<../zh-cn/Talk:Google_Earth.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Google_Earth](<https://wiki.archlinux.org/title/Google_Earth> "arch:Google Earth")，最近一次同步于 2015-2-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Google_Earth?diff=0&oldid=355374>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Google_Earth_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated 2015（在 [Talk:Google Earth#](<../zh-cn/Talk:Google_Earth.html>) 中讨论）

来自[项目网站](<https://support.google.com/earth/bin/answer.py?hl=en&answer=176145>)：: 

_"Google Earth可以让您在一个虚拟的地球上随意的旅行并观看卫星影像,地形,地图,3D建筑等元素. 随着Google earth中地理内容的丰富, 您将能探索更真实的世界，并能够飞到您最喜欢的地方, 搜索商户或者只是用于导航。"_

##  安装

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")中已提供了Google earth 的安装包: 

  * 最新版本 - [google-earth](<https://aur.archlinux.org/packages/google-earth/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]
  * 之前的版本 - [google-earth6](<https://aur.archlinux.org/packages/google-earth6/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

##  故障处理

**提示：** 参见 [官方支持社区](<https://productforums.google.com/forum/#!categories/earth/linux>) 来查阅本段中未包括的内容。

###  启动时出现错误

Google Earth可能会因多种错误而不能启动，下面列出了几个常见错误和错误的处理方法。 

####  Startup tips 被启用

即使startup tips非常有用，但是它被人所更为了解的原因是startup tip容易造成软件的崩溃，所以请使它无效化，把以下字段加入 `~/.config/Google/GoogleEarthPlus.conf`中: 
    
    [General]
    enableTips=false
    
####  `~/.drirc`文件的结尾没有换行
    
    $ echo >> ~/.drirc
    
####  缓存文件损坏

如果缓存文件已损坏并需要重建,请移除它: 
    
    $ rm -r ~/.googleearth/Cache/
    
####  Another crash happened while handling crash!

您可以尝试移除以下文件: 
    
    $ rm -f ~/.googleearth/Cache/cookies ~/.googleearth/instance-running-lock
    
###  占用的内存过多

您可以在 _Tools > Options > Cache_中调整最大缓存限制来控制内存的使用大小，或者您可以在 _3D View_ 页面中通过降低画面质量来降低内存负荷。 

###  Panoramio上的照片无法使用

在[Google Earth forums](<https://productforums.google.com/forum/#!categories/earth/linux>)中有几个针对不同原因所给出的不同解决方案 [[1]](<https://productforums.google.com/d/msg/earth/548PQIT8bKI/rbpVsbMawwIJ>) [[2]](<https://productforums.google.com/forum/#!msg/earth/_h4t6SpY_II/6O_DTry49pgJ>) [[3]](<https://productforums.google.com/d/msg/earth/tZfKSs2AaZc/r_rBDl5djIMJ>)。 如果在[google-earth](<https://aur.archlinux.org/packages/google-earth/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]中的[PKGBUILD](<https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=google-earth>)设置`_attempt_fix` 变量仍不起作用，回滚到旧版的[google-earth6](<https://aur.archlinux.org/packages/google-earth6/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] 可能会解决这个问题. 

###  地球除了黄色的边框以外什么都不显示

根据更新日志[7.0.3](<https://support.google.com/earth/bin/answer.py?hl=en&answer=40901>)这个问题已得到大幅改善，但是这个错误仍然会存在: 
    
    这个问题可能会出现在使用Intel系列GPU的Linux用户中
    
解决方法同样适用于 [google-earth6](<https://aur.archlinux.org/packages/google-earth6/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]。 
