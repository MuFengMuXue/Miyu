**翻译状态：**

  * 本文（或部分内容）译自 [Pkgstats](<https://wiki.archlinux.org/title/Pkgstats> "arch:Pkgstats")，最近一次同步于 2023-03-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/Pkgstats?diff=0&oldid=768755>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Pkgstats_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

pkgstats 将所有已安装软件包，您正在使用的体系结构和镜像的列表发送到 Arch Linux 项目。该信息是匿名的，不能用于识别用户，但是它将帮助 Arch 开发人员确定其工作的优先级（[源代码](<https://github.com/archlinux/svntogit-packages/blob/packages/pkgstats/trunk>)）。另请参阅该项目的[隐私权政策](<https://pkgstats.archlinux.de/privacy-policy>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [pkgstats](<https://archlinux.org/packages/?name=pkgstats>)包 软件包。 

##  用法

_pkgstats_ 设置为使用 [systemd/Timers](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers") 每周自动运行。一旦安装，它将在下次重启后被激活。 

如果不想等待重新启动周期，则可以手动[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `pkgstats.timer`。 

_pkgstats_ 也可以手动运行：有关用法的信息，请参见 `pkgstats -h`。 

##  结果和参考

从 <https://pkgstats.archlinux.de/> 上可以找到统计信息和文档，<https://pkgstats.archlinux.de/fun> 上包含相关的比较。 

通过以下公开的 API 可以获取 JSON 格式的统计数据：[API 文档](<https://pkgstats.archlinux.de/api/doc>)。 
