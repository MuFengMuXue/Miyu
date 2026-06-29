**翻译状态：**

  * 本文（或部分内容）译自 [VnStat](<https://wiki.archlinux.org/title/VnStat> "arch:VnStat")，最近一次同步于 2020-07-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/VnStat?diff=0&oldid=627334>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/VnStat_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[vnStat](<https://humdi.net/vnstat/>) 是一个轻量级（命令行）网络流量监视器。它监视可选接口，并将网络流量日志存储在数据库中，以供以后分析。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vnstat](<https://archlinux.org/packages/?name=vnstat>)包 软件包。 

##  配置

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `vnstat.service` 守护程序。 

选择一个首选的网络接口，并相应地在 `/etc/vnstat.conf` 中编辑 `Interface` 变量。 要列出 vnstat 可用的所有接口，请使用 `vnstat --iflist`。 

要开始监视启动守护程序时配置文件中未引用的特定接口，必须首先初始化数据库。每个接口都需要自己的数据库。初始化 `eth0` 接口的命令是： 
    
    # vnstat --add -i eth0
    
添加新接口后，请记得[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `vnstat.service` 守护程序。 

##  用法

查询网络流量： 
    
    # vnstat --query
    
查看实时网络流量使用情况： 
    
    # vnstat --live
    
要查找更多选项，请使用： 
    
    # vnstat --help
    
或查看所有选项，使用： 
    
    # vnstat --longhelp
    
数据的直观呈现也可以通过 [vnstati(1)](<https://man.archlinux.org/man/vnstati.1>)（它是 [vnstat](<https://archlinux.org/packages/?name=vnstat>)包 软件包的一部分）来实现。 
