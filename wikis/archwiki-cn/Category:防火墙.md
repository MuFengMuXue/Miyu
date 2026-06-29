**翻译状态：**

  * 本文（或部分内容）译自 [Category:Firewalls](<https://wiki.archlinux.org/title/Category:Firewalls> "arch:Category:Firewalls")，最近一次同步于 2018-09-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/Category:Firewalls?diff=0&oldid=495629>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Category:Firewalls_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Arch Linux 提供了两种管理[防火墙](<https://en.wikipedia.org/wiki/Firewall_\(computing\)> "wikipedia:Firewall \(computing\)")的选项，两个方式默认都没有启用。Linux [内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")包含了 [netfilter](<https://netfilter.org>) 包过滤框架，可以通过下面两个工具进行管理： 

  * [iptables](<../zh-cn/Iptables.html> "Iptables") 是传统的防火墙管理用户空间工具。可以用命令行或图形工具进行配置。
  * [nftables](<../zh-cn/Nftables.html> "Nftables") 是为了替换 _iptables_ 的新框架，语法更简洁，功能完善而且提供了性能优化。

名称  | 用户空间软件包  | 用户空间程序  | Systemd 服务  | 配置文件   
---|---|---|---|---  
[iptables](<../zh-cn/Iptables.html> "Iptables") |  [iptables](<https://archlinux.org/packages/?name=iptables>)包 |  [iptables(8)](<https://man.archlinux.org/man/iptables.8>) |  `iptables.service` |  `/etc/iptables/iptables.rules`  
[nftables](<../zh-cn/Nftables.html> "Nftables") |  [nftables](<https://archlinux.org/packages/?name=nftables>)包 |  [nft(8)](<https://man.archlinux.org/man/nft.8>) |  `nftables.service` |  `/etc/nftables.conf`  
  
## 分类“防火墙”中的页面

本分类共含有11个页面，以下显示其中11个。 

### F

  * [Fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban")
  * [Firewalld](<../zh-cn/Firewalld.html> "Firewalld")

### I

  * [Ipset](<../zh-cn/Ipset.html> "Ipset")
  * [Iptables](<../zh-cn/Iptables.html> "Iptables")

### L

  * [路由器](<../zh-cn/%E8%B7%AF%E7%94%B1%E5%99%A8.html> "路由器")

### N

  * [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")
  * [Nftables](<../zh-cn/Nftables.html> "Nftables")

### S

  * [Shorewall](<../zh-cn/Shorewall.html> "Shorewall")
  * [Simple stateful firewall](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall")
  * [Sshguard](<../zh-cn/Sshguard.html> "Sshguard")

### U

  * [Uncomplicated Firewall](<../zh-cn/Uncomplicated_Firewall.html> "Uncomplicated Firewall")
