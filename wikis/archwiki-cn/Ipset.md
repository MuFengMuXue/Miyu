**翻译状态：**

  * 本文（或部分内容）译自 [Ipset](<https://wiki.archlinux.org/title/Ipset> "arch:Ipset")，最近一次同步于 2016-06-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ipset?diff=0&oldid=438095>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ipset_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Firewalls](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Firewalls")
  * [Iptables](<../zh-cn/Iptables.html> "Iptables")

[ipset](<https://ipset.netfilter.org/>)是 Linux [防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "Firewalls") [iptables](<../zh-cn/Iptables.html> "Iptables") 的一个协助工具。 通过这个工具可以轻松愉快地屏蔽一组IP地址。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [ipset](<https://archlinux.org/packages/?name=ipset>)包。 

##  配置

###  屏蔽一组地址

先创建一个新的网络地址的"集合"。下面的命令创建了一个新的叫做"myset"的"net"网络地址的"hash"集合。 
    
    # ipset create myset hash:net
    
或 
    
    # ipset -N myset nethash
    
把希望屏蔽的IP地址添加到集合中。 
    
    # ipset add myset 14.144.0.0/12
    # ipset add myset 27.8.0.0/13
    # ipset add myset 58.16.0.0/15
    
最后，配置 [iptables](<../zh-cn/Iptables.html> "Iptables")，屏蔽这个集合中的所有地址。这个命令将会向"INPUT"链顶端添加一个规则来从 ipset 中 "-m" 匹配名为 "myset" 的集合，当匹配到的包是一个"src"包时，"DROP"屏蔽掉它。 
    
    # iptables -I INPUT -m set --match-set myset src -j DROP
    
###  屏蔽多个 IP 地址

先创建一个 IP 地址"集合"，下面命令创建一个 "myset-ip" 散列集合。 
    
    # ipset create myset-ip hash:ip
    
或 
    
    # ipset -N myset-ip iphash
    
将要屏蔽的地址加入此集合： 
    
    # ipset add myset-ip 1.1.1.1
    # ipset -A myset-ip 2.2.2.2
    
最后，用 [iptables](<../zh-cn/Iptables.html> "Iptables") 屏蔽集合中的所有地址. 
    
    # iptables -I INPUT -m set --match-set myset-ip src -j DROP
    
###  使ipset持久化

上面创建的 ipset 存在于内存中，重启后将会消失。要使ipset持久化，你要这样做： 

首先把 ipset 保存到 /etc/ipset.conf: 
    
    # ipset save > /etc/ipset.conf
    
然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `ipset.service`, 与 `iptables.service`相似，这个服务用于恢复[iptables 规则](<../zh-cn/Iptables.html#Configuration_and_usage> "Iptables")。 

###  使用PeerGuardian和其它列表屏蔽

maeyanie.com所作的[pg2ipset-git](<https://aur.archlinux.org/packages/pg2ipset-git/>)AUR与[ipset-update.sh](<https://github.com/ilikenwf/pg2ipset/blob/master/ipset-update.sh>) 脚本配合可以用cron来自动更新多个屏蔽列表。 当前实现了按默认国家屏蔽，tor退出节点屏蔽，和来自Bluetack的pg2列表屏蔽。 

##  其他命令

查看集合。 
    
    # ipset list
    
删除名为"myset"的集合。 
    
    # ipset destroy myset
    
删除所有集合。 
    
    # ipset destroy
    
更多信息请参考ipset的man手册页。 

##  优化

[iprange](<https://aur.archlinux.org/packages/iprange/>)AUR工具可以通过合并相邻范围或消除重复范围来帮助减少ipset.conf中的项目。 在表的大小很大时，这有助于改善路由/防火墙的性能。这个工具也可以把一个主机名的列表转换成IP列表。 

虽然 ipset 设计上可以支持非常大的屏蔽，但并不是无限的。有些国家的 IP 地址空间非常庞大，所以按区域屏蔽的效果并不理想。 
