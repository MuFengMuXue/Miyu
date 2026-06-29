**翻译状态：**

  * 本文（或部分内容）译自 [Sshguard](<https://wiki.archlinux.org/title/Sshguard> "arch:Sshguard")，最近一次同步于 2022-11-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sshguard?diff=0&oldid=756857>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sshguard_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban")
  * [Secure Shell](<../zh-cn/Secure_Shell.html> "Secure Shell")

**警告：** 使用 IP 黑名单将会阻挡普通的攻击，但它依赖于一个额外的守护进程以及成功的日志记录（包含 /var 的分区可能会被占满，尤其是当攻击者正在攻击服务器时）。另外，由于知道您的 IP 地址，攻击者可以发送伪装源头的包，并将您阻挡在服务器之外。[SSH 密钥](<../zh-cn/SSH_keys.html> "SSH keys") 为防止暴力破解提供了一个优雅的解决方案，而没有上述问题。

[sshguard](<https://www.sshguard.net>) 是一个用于保护 [SSH](<../zh-cn/Secure_Shell.html> "Secure Shell") 以及其他服务免受暴力破解攻击的守护进程，类似于 [fail2ban](<../zh-cn/Fail2ban.html> "Fail2ban")。 

sshguard 与后者的不同之处在于，它是使用 C 编写的，使用起来更轻量、简单，功能更少，但同时也能出色地执行核心功能。 

sshguard 不会受到大多数（或任何）日志分析[漏洞](<https://web.archive.org/web/20120625102244/http://www.ossec.net/main/attacking-log-analysis-tools>)的影响，而这些漏洞曾导致同类型工具出现问题。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sshguard](<https://archlinux.org/packages/?name=sshguard>)包 软件包. 

##  设置

sshguard 通过监控 `/var/log/auth.log`，[syslog-ng](</wzh/index.php?title=Syslog-ng&action=edit&redlink=1> "Syslog-ng（页面不存在）") 或 systemd 日志来获得失败的登录尝试。对于每次失败的尝试，违规的主机都会在有限时间内被禁止，无法进行通信。对于违规主机，被禁止的默认时间长度从 120 秒开始，之后每次登录失败都会增加 1.5 倍。sshguard 可以被配置为永久禁止一个失败尝试次数过多的主机。 

临时和永久禁止都是通过在 iptables 的 "sshguard" 链中添加条目完成的，该条目会删除来自违规主机的所有数据包。随后该封禁会被记录到 syslog 并保存到 `/var/log/auth.log`，如果使用 systemd 日志，则会保存到 systemd 日志中。 

您必须配置下列防火墙之一来让 sshguard 的屏蔽发挥作用。 

### firewalld

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** ipset 已在 firewalld 中被弃用。下列操作将会破坏 firewalld。 (在[Talk:Sshguard](<../zh-cn/Talk:Sshguard.html>)讨论)

sshguard 可以与 [firewalld](<../zh-cn/Firewalld.html> "Firewalld") 一同工作。确保您已安装、配置并启用 firewalld。为了让 sshguard 写入设置区域，请执行以下命令： 
    
    # firewall-cmd --permanent --zone=public --add-rich-rule="rule source ipset=sshguard4 drop"
    
如果您使用 ipv6，您可以执行相同的命令，但需要把 sshguard4 替换为 sshguard6。完成后，执行以下命令： 
    
    # firewall-cmd --reload
    
您可以通过以下命令确认上述内容： 
    
    # firewall-cmd --info-ipset=sshguard4
    
最后，在 /etc/sshguard.conf 中，找到 BACKEND 行并变更如下： 
    
    BACKEND="/usr/lib/sshguard/sshg-fw-firewalld"
    
### UFW

如果安装并启用了 UFW，则必须赋予它将 DROP 控制传递给 sshguard 的能力。可以通过在 `/etc/ufw/before.rules` 中包含以下行来实现。这些行应该被插入到回环设备部分之后。

**注意：** 在非标准端口上运行 sshd 的用户需要修改最后一行中的端口号（标准端口为 22）。
    
    /etc/ufw/before.rules
    
    # 允许全部回环
    -A ufw-before-input -i lo -j ACCEPT
    -A ufw-before-output -o lo -j ACCEPT
    
    # 将 sshd 的控制权交给 sshguard
    :sshguard - [0:0]
    -A ufw-before-input -p tcp --dport 22 -j sshguard
    
在进行上述变更后需要[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") ufw。 

### iptables

**注意：** 请先参阅 [iptables](<../zh-cn/Iptables.html> "Iptables") 和 [简单的有状态防火墙](<../zh-cn/Simple_stateful_firewall.html> "Simple stateful firewall") 来设置防火墙。

必要的设置是在 iptables 上创建一个名为 `sshguard` 的链。sshguard 将会在这个链上自动插入规则以丢弃来自坏主机的数据包： 
    
    # iptables -N sshguard
    
接下来添加一条从 `INPUT` 链跳转到 `sshguard` 链的规则。这条规则必须被添加在任何其他处理 sshguard 保护端口的规则**之前** 。使用下列行来保护 FTP 和 SSH，或查看 [[1]](<https://web.archive.org/web/20180902011955/https://www.sshguard.net/docs/setup/#netfilter-iptables>) 了解更多实例。 
    
    # iptables -A INPUT -m multiport -p tcp --destination-ports 21,22 -j sshguard
    
若要保存这些规则： 
    
    # iptables-save > /etc/iptables/iptables.rules
    
**注意：** For IPv6, repeat the same steps with _ip6tables_ and save the rules with _ip6tables-save_ to `/etc/iptables/ip6tables.rules`.

### nftables

编辑 `/etc/sshguard.conf` 并将 `BACKEND` 的值更改如下： 
    
    /etc/sshguard.conf
    
    BACKEND="/usr/lib/sshguard/sshg-fw-nft-sets"

When you [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") the `sshguard.service`, two new tables named `sshguard` in the `ip` and `ip6` address families are added which filter incoming traffic through sshguard's list of IP addresses. The chains in the `sshguard` table have a priority of -10 and will be processed before other rules of lower priority. See [sshguard-setup(7)](<https://man.archlinux.org/man/sshguard-setup.7>) and [nftables](<../zh-cn/Nftables.html> "Nftables") for more information. 

##  用法

### systemd

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `sshguard.service`。 

### syslog-ng

如果您安装了 [syslog-ng](<https://archlinux.org/packages/?name=syslog-ng>)包，您可以直接从命令行启动 sshguard。 
    
    /usr/sbin/sshguard -l /var/log/auth.log -b /var/db/sshguard/blacklist.db
    
##  配置文件

Configuration is done in `/etc/sshguard.conf` which is required for _sshguard_ to start. A commented example is located at `/usr/share/doc/sshguard/sshguard.conf.sample` or can also be found on [Bitbucket sshguard.conf.sample](<https://bitbucket.org/sshguard/sshguard/src/master/examples/sshguard.conf.sample>). 

**注意：** Piped commands and runtime flags in _sshguard's_ systemd units [are not supported](<https://sourceforge.net/p/sshguard/mailman/message/35709860/>). Such flags can be modified in the configuration file.

### Blacklisting threshold

By default in the Arch-provided configuration file, offenders become permanently banned once they reach a "danger" level of 120 (or 12 failed logins; see [attack dangerousness](<https://web.archive.org/web/20160908055836/http://www.sshguard.net/docs/terminology/#attack-dangerousness>) for more details). This behavior can be modified by prepending a danger level to the blacklist file. 
    
    BLACKLIST_FILE=200:/var/db/sshguard/blacklist.db
    
The `200:` in this example tells sshguard to permanently ban a host after achieving a danger level of 200. 

Finally [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshguard.service`

### Moderate banning example

A slightly more aggressive banning rule than the default one is proposed here to illustrate various options: 

  * It monitors [sshd](<../zh-cn/OpenSSH.html> "Sshd") and [vsftpd](</wzh/index.php?title=Vsftpd&action=edit&redlink=1> "Vsftpd（页面不存在）") via logs from the [systemd/日志](<../zh-cn/Systemd/Journal.html> "Systemd/日志")
  * It blocks attackers after 2 attempts (each having a cost of 10, explaining the `20` value of the `THRESHOLD` parameter) for 180 seconds with subsequent block time longer by a factor of 1.5. Note that this 1.5 multiplicative delay is internal and not controlled in the settings
  * Attackers are permanently blacklisted after 10 attempts (10 attempts having each a cost of 10, explaining the `100` value in the `BLACKLIST_FILE` parameter)
  * It blocks not only the attacker's IP but all the IPv4 subnet 24 ([CIDR](<https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing> "wikipedia:Classless Inter-Domain Routing") notation)

    /etc/sshguard.conf
    
    # Full path to backend executable (required, no default)
    BACKEND="/usr/lib/sshguard/sshg-fw-iptables"
    
    # Log reader command (optional, no default)
    LOGREADER="LANG=C.UTF-8 /usr/bin/journalctl -afb -p info -n1 -t sshd -t vsftpd -o cat"
    
    # How many problematic attempts trigger a block
    THRESHOLD=20
    # Blocks last at least 180 seconds
    BLOCK_TIME=180
    # The attackers are remembered for up to 3600 seconds
    DETECTION_TIME=3600
    
    # Blacklist threshold and file name
    BLACKLIST_FILE=100:/var/db/sshguard/blacklist.db
    
    # IPv6 subnet size to block. Defaults to a single address, CIDR notation. (optional, default to 128)
    IPV6_SUBNET=64
    # IPv4 subnet size to block. Defaults to a single address, CIDR notation. (optional, default to 32)
    IPV4_SUBNET=24

### Aggressive banning

For some users under constant attack, a more aggressive banning policy can be adopted. If you are confident that accidental failed logins are unlikely, you can instruct SSHGuard to permanently ban hosts after a single failed login. Modify the parameters in the configuration file in the following way: 
    
    THRESHOLD=10
    BLACKLIST_FILE=10:/var/db/sshguard/blacklist.db
    
最后[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `sshguard.service`。 

另外，为了防止在单个连接期间进行多次身份验证尝试，您需要在 `/etc/ssh/sshd_config` 中定义如下： 
    
    MaxAuthTries 1
    
[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `sshd.service` 来使此更改生效。 

##  提示与技巧

###  解除封禁

如果您封禁了自己，你可以等待自动解封，或者使用 iptables 或 nftables 来解除封禁。 

要永久解除您的封禁，您还需要从 `/var/db/sshguard/blacklist.db` 移除您的 IP 地址。 

#### iptables

首先检查您的 IP 是否被 sshguard 阻止： 
    
    # iptables --list sshguard --line-numbers --numeric
    
然后使用下列命令来解禁，使用前一个命令中标识的行号： 
    
    # iptables --delete sshguard _line-number_
    
#### nftables

从 `attackers` 中移除您的 IP 地址： 
    
    # nft delete element _family_ sshguard attackers { _ip_address_ }
    
其中 `_family_` 可以为 `ip` 或 `ip6`。 

###  日志记录

要查看传递给 sshguard 的内容，请检查 `/usr/lib/systemd/scripts/sshguard-journalctl` 中的脚本和 systemd 服务 `sshguard.service`。一个在终端中查看日志的等效命令： 
    
    # journalctl -afb -p info SYSLOG_FACILITY=4 SYSLOG_FACILITY=10
    