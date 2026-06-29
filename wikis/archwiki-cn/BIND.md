**翻译状态：**

  * 本文（或部分内容）译自 [BIND](<https://wiki.archlinux.org/title/BIND> "arch:BIND")，最近一次同步于 2017-08-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/BIND?diff=0&oldid=474888>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/BIND_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [DNSCrypt](<../zh-cn/Dnscrypt-proxy.html> "DNSCrypt")
  * [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq")
  * [Pdnsd](</wzh/index.php?title=Pdnsd&action=edit&redlink=1> "Pdnsd（页面不存在）")
  * [Unbound](<../zh-cn/Unbound.html> "Unbound")
  * [PowerDNS](</wzh/index.php?title=PowerDNS&action=edit&redlink=1> "PowerDNS（页面不存在）")

伯克利互联网名称服务 (Berkeley Internet Name Daemon，简称 [BIND](<https://www.isc.org/downloads/bind/>)) 是 DNS 协议的一个参考实现。 

**注意：** 开发 BIND 的组织在发现安全漏洞之后，会先通知付费客户，四天以后才会通知 Linux 发行版和大众。[[1]](<https://kb.isc.org/article/AA-00861/0/ISC-Software-Defect-and-Security-Vulnerability-Disclosure-Policy.html>)

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [bind](<https://archlinux.org/packages/?name=bind>)包。 

要使用 BIND 提供系统 DNS 服务，修改 [resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf")，将`nameserver 127.0.0.1`放到最前面。 

[开始/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `named.service` 服务。 

##  配置

BIND 的配置文件是 `/etc/named.conf`. `named.conf` man 手册页介绍了所有选项。 

[Reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") the `named.service` unit 以应用配置变更. 

###  只允许本地访问

如果希望只允许本地网络访问，编辑 `/etc/named.conf` 并将这行配置加入到 **options** 区域。 
    
    listen-on { 127.0.0.1; };
    
###  DNS 转发

要将 DNS 请求请求转发到上游 DNS 服务器（例如说您的 ISP 的服务器，或者 Google、OpenNIC 等知名的服务）。将下面字段加入配置文件的 options 中。. 
    
     forwarders { 8.8.8.8; 8.8.4.4; };
    
不要忘记重启 `named.service` 服务。 

##  权威 DNS 服务器

以下为一个设置权威域的简单教程。在这个示例中，我们的权威域名为 "domain.tld"。 

更详尽的教程参见 [Two-in-one DNS server with BIND9](<https://www.howtoforge.com/two_in_one_dns_bind9_views>). 

###  1\. 创建一个 zonefile
    
    # nano /var/named/domain.tld.zone
    
    $TTL 7200
    ; domain.tld
    @       IN      SOA     ns01.domain.tld. postmaster.domain.tld. (
                                            2007011601 ; Serial
                                            28800      ; Refresh
                                            1800       ; Retry
                                            604800     ; Expire - 1 week
                                            86400 )    ; Minimum
                    IN      NS      ns01
                    IN      NS      ns02
    ns01            IN      A       0.0.0.0
    ns02            IN      A       0.0.0.0
    localhost       IN      A       127.0.0.1
    @               IN      MX 10   mail
    imap            IN      CNAME   mail
    smtp            IN      CNAME   mail
    @               IN      A       0.0.0.0
    www             IN      A       0.0.0.0
    mail            IN      A       0.0.0.0
    @               IN      TXT     "v=spf1 mx"
    
$TTL 定义了默认的 TTL (time-to-live), 单位为秒。在这个例子中，默认 TTL 为 2 小时。 

每次修改 zonefile 的时候，都需要将 Serial (序列号) 加一再重启 **named** 。只有当新的 Serial 比最后传输的域的序列号大的时候，从服务器才会请求传输新的域。 

###  2\. 配置主服务器

将您的 zone 文件加到 `/etc/named.conf`: 
    
    zone "domain.tld" IN {
            type master;
            file "domain.tld.zone";
            allow-update { none; };
            notify no;
    };
    
[重新加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") `named.service` 服务。 

###  3\. 将其设置为默认 DNS 服务器

如果您自己已经在运行 DNS 服务器的话，可以考虑同时将其用来处理 DNS 查询请求。服务器必须支持 **recursive** (递归) 查询。为了防止 [DNS 放大攻击](<https://www.us-cert.gov/ncas/alerts/TA13-088A>)，许多 DNS 解析程序都默认禁用了递归功能。Arch 的默认 `/etc/named.conf` 配置只允许本机地址使用递归： 
    
    allow-recursion { 127.0.0.1; };
    
[resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf") 配置文件必须包含 127.0.0.1 地址以使用您的 DNS 服务器。 参见 [Domain name resolution#Overwriting of /etc/resolv.conf](<../zh-cn/Domain_name_resolution.html#Overwriting_of_/etc/resolv.conf> "Domain name resolution") 以了解确保这个文件不会被覆盖的方法。 

如果您想为您的局域网提供 DNS 服务的话（例如 192.168.0 IP 段），您必须将对应的 IP 段加入到 `/etc/named.conf` 中： 
    
    allow-recursion { 192.168.0.0/24; 127.0.0.1; };
    
##  配置 DNSSEC

  * <https://www.dnssec.net/practical-documents>
    * <https://www.cymru.com/Documents/secure-bind-template.html> **(configuration template!)**
    * <https://www.bind9.net/manuals>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-07 ⓘ]
    * <https://www.bind9.net/BIND-FAQ>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-07 ⓘ]
  * <https://web.archive.org/web/20100528023716/http://blog.techscrawl.com:80/2009/01/13/enabling-dnssec-on-bind/>
  * Or use an external mechanisms such as OpenDNSSEC (fully-automatic key rollover)

##  自动监听新的网络接口

BIND 会每个每隔几个小时扫描新的网络接口并停止在已经不再不存在的上监听。如果您想修改这个时间的话，可以在 `/etc/named.conf` 中增加这个项： 
    
    interface-interval <扫描间隔>;
    
最大间隔为 28 天 (40230 分钟)。 

如果需要禁用这个功能的话，可以将时间值设置为 **0** 。 

最后，请重启服务。 

##  在 chroot 环境运行 BIND

在 [chroot] 环境运行可以提高安全性。 

###  创建 Jail House

首先，我们需要创建一个 jail。我们可以使用 `/srv/named`, 并将相关文件都放到里面去。 
    
     mkdir -p /srv/named/{dev,etc,usr/lib/engines,var/{run,log,named}}
     # Copy over required system files
     cp -av /etc/{localtime,named.conf} /srv/named/etc/
     cp -av /usr/lib/engines-1.1/* /srv/named/usr/lib/engines/
     cp -dfprv /var/named /srv/named/var/
     # Set up required dev nodes
     mknod /srv/named/dev/null c 1 3
     mknod /srv/named/dev/random c 1 8
     # Set Ownership of the files
     chown -R named:named /srv/named
    
这些步骤可以配置 jail 的文件系统。 

###  服务文件

接下来我们需要创建服务文件 (service file)，以强制 BIND 在 chroot 环境中启动。 
    
     cp -av /usr/lib/systemd/system/named.service /etc/systemd/system/named-chroot.service
    
我们需要修改 service 启动 BIND 的方法。 
    
    /etc/systemd/system/named-chroot.service
    
      ExecStart=/usr/bin/named -4 -f -u named -t "/srv/named"
    
} 

最后，重新加载 systemd `systemctl daemon-reload`。然后，启动 `named-chroot.service`。 

##  参见

  * [BIND 9 Administrator Reference Manual](<https://www.isc.org/downloads/bind/doc/>)
  * [BIND 9 DNS Administration Reference Book](<http://www.reedmedia.net/books/bind-dns/>)
  * [DNS and BIND by Cricket Liu and Paul Albitz](<https://www.oreilly.com/library/view/dns-and-bind/0596100574>)
  * [Pro DNS and BIND](<http://www.netwidget.net/books/apress/dns/intro.html>)
  * [Internet Systems Consortium, Inc. (ISC)](<https://www.isc.org/>)
  * [DNS Glossary](<http://www.menandmice.com/knowledgehub/dnsglossary>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-07 ⓘ]
  * [Archived mailing list discussion on BIND's future](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/RR3TKD5ZWTYKQHQBFPHTHDLN3JKUOOWV/>)
