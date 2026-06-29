**翻译状态：**

  * 本文（或部分内容）译自 [Rkhunter](<https://wiki.archlinux.org/title/Rkhunter> "arch:Rkhunter")，最近一次同步于 2025-11-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rkhunter?diff=0&oldid=846435>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rkhunter_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [安全](<../zh-cn/%E5%AE%89%E5%85%A8.html> "安全")
  * [应用程序列表/安全](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%AE%89%E5%85%A8.html> "应用程序列表/安全")
  * [AIDE](</wzh/index.php?title=AIDE&action=edit&redlink=1> "AIDE（页面不存在）")

**rkhunter** (Rootkit Hunter) 是一款用于POSIX兼容系统的安全监控工具。它通过搜索（rootkit的）默认目录、权限配置错误、隐藏文件、包含可疑字符串的内核模块，以及将重要文件的哈希值与已知正常文件哈希值进行比较，来检查rootkit和其他可能的漏洞。 

其使用 [Bash](<../zh-cn/Bash.html> "Bash") 编写，具有良好的可移植性，可在大多数基于UNIX的系统上运行。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") 软件包 [rkhunter](<https://archlinux.org/packages/?name=rkhunter>)包。 

##  配置

###  初始化

首次运行rkhunter前，请更新 _文件属性数据库_ : 
    
    # rkhunter --propupd
    
###  相关文件

主配置文件位于 `/etc/rkhunter.conf`。 

默认情况下，最近一次系统检查的日志将存放在 `/var/log/rkhunter.log`。 

##  使用

详细请参见 [rkhunter(8)](<https://man.archlinux.org/man/rkhunter.8>)。 

###  基本命令

更新文件属性数据库： 
    
    # rkhunter --propupd
    
在扫描前，务必运行以下命令以确保rkhunter数据文件保持最新： 
    
    # rkhunter --update
    
执行系统检查： 
    
    # rkhunter --check --sk
    
校验配置文件： 
    
    # rkhunter --config-check
    
##  故障排除

###  误报

默认情况下，Rootkit Hunter在文件属性检查期间会产生一些误报警告。这是因为部分核心程序已被脚本替代，您可通过白名单机制消除这些警告： 
    
    /etc/rkhunter.conf
    
    SCRIPTWHITELIST=/usr/bin/egrep
    SCRIPTWHITELIST=/usr/bin/fgrep
    SCRIPTWHITELIST=/usr/bin/ldd
    SCRIPTWHITELIST=/usr/bin/vendor_perl/GET

##  附录

###  额外文档

  * [Rootkit Hunter Homepage](<https://rkhunter.sourceforge.net/>)
  * [Rootkit Hunter README](<https://sourceforge.net/p/rkhunter/rkh_code/ci/master/tree/files/README>)
  * [Rootkit Hunter FAQ](<https://sourceforge.net/p/rkhunter/rkh_code/ci/master/tree/files/FAQ>)

###  相关维基页面

  * [rkhunter](<https://en.wikipedia.org/wiki/rkhunter> "wikipedia:rkhunter")
  * [Host-based intrusion detection system (HIDS)](<https://en.wikipedia.org/wiki/Host-based_intrusion_detection_system> "wikipedia:Host-based intrusion detection system")
  * [Intrusion detection system (IDS)](<https://en.wikipedia.org/wiki/Intrusion_detection_system> "wikipedia:Intrusion detection system")
