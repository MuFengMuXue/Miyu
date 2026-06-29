[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Isatapd](<../zh-cn/Talk:Isatapd.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Isatapd](<https://wiki.archlinux.org/title/Isatapd> "arch:Isatapd")，最近一次同步于 2020-04-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Isatapd?diff=0&oldid=608836>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Isatapd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[isatapd](<http://www.saschahlusiak.de/linux/isatap.htm>) 是一个 [ISATAP](<https://en.wikipedia.org/wiki/ISATAP> "wikipedia:ISATAP") 客户端。它是一个守护程序，用于在 Linux 中创建和维护 ISATAP 隧道 RFC 5214。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [isatapd](<https://archlinux.org/packages/?name=isatapd>)包 包。 

##  用法

该软件包提供了 `isatapd@.service` 系统服务。[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")时，将所选路由器（例如isatap.tsinghua.edu.cn）作为参数传递给服务。 

如果要修改其他选项而不是使用默认值，请查看[项目主页](<http://www.saschahlusiak.de/linux/isatap.htm>)以供进一步参考。 
