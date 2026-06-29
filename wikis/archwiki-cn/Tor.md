[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Tor](<../zh-cn/Talk:Tor.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** No updates since 2020, still references `rc d`.（在 [Talk:Tor#](<../zh-cn/Talk:Tor.html>) 中讨论）

相关文章

  * [I2P](<../zh-cn/I2P.html> "I2P")
  * [Privoxy](<../zh-cn/Privoxy.html> "Privoxy")

**翻译状态：**

  * 本文（或部分内容）译自 [Tor](<https://wiki.archlinux.org/title/Tor> "arch:Tor")，最近一次同步于 2020-04-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tor?diff=0&oldid=489707>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tor_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**注意：** 本文正在一个[临时页面](<../User:Giteeajake/Tor.html> "User:Giteeajake/Tor")重译，请前往该临时页面查看进度。

[Tor](<https://www.torproject.org/download/download.html.en>) 是一个开源实现，第二代洋葱路由匿名代理网络，提供免费访问。其首要目标是通过对流量分析攻击保护，使网上的匿名性。 

##  介绍

使用Tor网络在他们的机器上运行洋葱代理。这个软件向外连接到Tor，定期的通过Tor网络连接一个虚拟的电子回路。Tor在一个分层方式采用加密(因此有了‘洋葱’的比喻),确保路由器之间的完全保密。 同时， 洋葱代理服务器软件，向客户端提出了SOCKS接口。SOCKS监听程序是Tor的特点，通过Tor的虚拟电路的流量，然后复。 

**警告：** 仅仅使用Tor不能保证匿名。这里可以看出几个主要的误导 (see: [[1]](<https://www.torproject.org/download/download.html.en#%E4%BB%80%E4%B9%88%E6%98%AFTor%E7%9C%9F%E6%AD%A3%E7%9A%84%E5%B7%A5%E4%BD%9C>))。

通过这个过程洋葱代理将会管理终端用户的匿名网络流量。它通过加密流量来保持用户的匿名， 通过Tor的其他节点来发送信息，在发送信息到你指定的服务器之前解密。虽然Tor相对的来说比一般的使用DNS目录连接安全(例如：没有使用代理), 由于大量的数据加密所以它相对来说比较慢。 此外，尽Tor阻止了流量分析但是Tor不能阻Tor网络边界流量的确认。(例如：例如流量进入或者退出网络)。 

[Wikipedia:Tor (anonymity network)](<https://en.wikipedia.org/wiki/Tor_\(anonymity_network\)> "wikipedia:Tor \(anonymity network\)")

##  安装

[安装](<../zh-cn/Pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Pacman \(简体中文\)")位于[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")的软件包 [tor](<https://archlinux.org/packages/?name=tor>)包。 

此外，还可以安装 [Qt](<../zh-cn/Qt.html> "Qt") 前端 [vidalia](<https://aur.archlinux.org/packages/vidalia/>)AUR。除了控制 Tor 进程外，Vidalia 可以查看 Tor 的配置和状态、监控带宽使用并查看、过滤和搜索日志信息。如果喜欢使用命令行，并能获得和 Vidalia 一样的效果，可以使用 [nyx](<https://archlinux.org/packages/?name=nyx>)包

##  配置

为了更好的理解Tor`/etc/tor/torrc`配置文件. 配置选项在 man tor[tor(1)](<https://man.archlinux.org/man/tor.1>)和[Tor website](<https://www.torproject.org/docs/tor-manual.html.en>)有介绍. 

默认配置应该能够很好的为大多数Tor用户服务除了哪些是用Vidalia的用户, Vidalia是一Tor的图形界面。 在[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")有可用包[vidalia](<https://aur.archlinux.org/packages/vidalia/>)AUR。除了控制过程中的Vidalia允许您查看Tor状态监视带宽使用情况，查看，过滤，搜索日志消息;和配置Tor的某些方面。 

使用`TOR_MAX_FD`变量，您可以设置自定义文件为Tor的描述ulimits`/etc/conf.d/tor`。 

默认情况下的Tor记录在日志级别的通知“STDOUT”。如果你能够记录在自己的文件`torrc`, 他们默认为 `/usr/local/var/log/tor/`. 

###  中继配置

中继 (relay) 是 Tor 网络中重要一环，负责数据传输和隐藏真实 ip 地址。如果没有配置 Tor 配置文件中的 `AccountingMax` 且没有布置 Web 服务器，应该考虑修改你的洋葱路由端口 (ORPort) 为 `443` ，因为防火墙会阻止 `tor` ，只能用于访问网页。修改后可以绕过防火墙，也可以考虑 `22` , `110` , `143` 和 `9001` 端口。由于低于1024端口属于特级端口，需要在 `tor.service` 中设置 `User=root` 和 `/etc/tor/torrc` 中设置 `User tor` 以 [root](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "Root") 权限运行。[realy setup](<https://community.torproject.org/relay/setup/>)

###  启用 Tor ControlPort

大多数用户是不需要这个功能的，但一些应用程序需要这个功能来实现对 Tor 节点的低级访问。 通过 ControlPort ，其他应用程序可以更改和查看 Tor Node ，在 Tor 运行时修改配置文件和查看 Tor 网络。 

添加到文件 
    
    ControlPort 9051

即可启用 

**警告：** 由于 ControlPort 会修改 Tor 配置文件，所以一般情况下不要启用，需要启用时应搭配 `cookie` 文件或控制密钥来使用，且只对受信任的程序或用户提供！

关于配置 Tor ControlPort ，请参考[设置 cookie 文件](<https://wiki.archlinux.org/title/Tor#Set_a_Tor_Control_cookie_file>)

##  用法

可以通过命令行或 **vidalia** 等图形程序启动 Tor. 

要永久连接，可以启动 **tor** [daemon](<../zh-cn/Systemd.html> "Daemon") 并将其加入 `DAEMONS` 数组。 

程序配置成实验 127.0.0.1 或 localhost 作为 SOCKS5 代理就可以使用 Tor，端口要设置成 9050 (Tor 标准设置) 或 9051 (用 **vidalia** 标准配置). 

访问 [Tor](<https://check.torproject.org/>)、[Harvard](<http://serifos.eecs.harvard.edu/cgi-bin/ipaddr.pl?tor=1>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-05-17 ⓘ] 或 [Xenobite.eu](<https://torcheck.xenobite.eu/>) 可以检查 Tor 是否正确运行。 

##  网页浏览

Tor主要支持Firefox，但是也支持Chromium。 

### Firefox

如果你使用Firefox, 你可以安装这个插件: [TorButton](<https://www.torproject.org/torbutton/>)。这将允许你很容易地在Tor的网络和正常网络切换。 

如果你正在使用多代理(例如：如果你想使用 TOR 和 "ssh -D") 也有一个插件叫作 "[FoxyProxy](<https://addons.mozilla.org/firefox/addon/foxyproxy-standard/>)" 他允许你对于不同网址或者全部网址指定多个代理。只需将它指向localhost上的端口8118（polipo运行中）。 

为了测试他, 在你的浏览器打开或者关闭Tor浏览这个网址[Tor check](<https://check.torproject.org/>)。 更多信息请查看这个网址[the official doc](<https://www.torproject.org/docs/tor-doc-unix.html.en>)。 

### Chromium

当你使用Tor和Chromium时不需要polipo。只需要简单的运行Tor daemon, 

然后运行： 
    
    $ chromium --proxy-server="socks://localhost:9050"
    
##  即时通信

要让即时通信程序使用 Tor，并不需要 [polipo](<../zh-cn/Polipo.html> "Polipo")/[privoxy](<../zh-cn/Privoxy.html> "Privoxy") 等 http 代理。直接使用 tor 守护进程监听的端口 9050 即可。 

### Pidgin

通过 preferences -> proxy 进入编辑，设置为： 
    
    Proxy type 	SOCKS5
    Host 	        127.0.0.1
    Port 	        9150
    
之后 [pidgin](<../zh-cn/Pidgin.html> "Pidgin") 会使用 Tor 进行通信。有时根据不同账号的 IM 服务配置，需要修改代理设置。在 Accounts -> Manage Accounts 中选择要修改的账号，在 Proxy 标签页中选择： 
    
    Proxy type 	Use Global Proxy Settings
    
## Irssi

Freenode 不推荐使用 [Irssi](<../zh-cn/Irssi.html> "Irssi") 和 Privoxy。他们推荐 `mapaddress` 方式，通过运行 `torify irssi` 启动。将下行加入 `/etc/tor/torrc`: 
    
    mapaddress  10.40.40.40 p4fsi4ockecnea7l.onion
    
Freenode 需要 charybdis 和 ircd-seven 的 SASL 机制在连接时进行 nickserv 确认。从 Freenode 网站(即 <https://web.archive.org/web/20150423190608/http://www.freenode.net/sasl/cap_sasl.pl>) 下载启用 SASL 的 `cap_sasl.pl`，保存到 `~/.irssi/scripts/cap_sasl.pl`

用 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装需要的 perl 模块和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中的 [perl-crypt-dh](<https://aur.archlinux.org/packages/perl-crypt-dh/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 
    
    $ pacman -S perl-crypt-openssl-bignum perl-crypt-blowfish
    
也可以通过 perl 直接安装: 
    
    $ perl -MCPAN -e 'install Crypt::OpenSSL::Bignum Crypt::DH Crypt::Blowfish'
    
启动 irssi 
    
    $ torify irssi
    
加载使用 SASL 机制的脚本： 
    
    /script load cap_sasl.pl
    
将身份设置到 nickserv，连接时会读取这个值，支持的机制是 PLAIN 和 DH-BLOWFISH。 
    
    /sasl set <network> <username> <password> <mechanism>
    
连接到 Freenode: 
    
    /connect -network <network> 10.40.40.40
    
如果遇到问题，请访问 Arch 论坛上的 [Cannot Connect to Freenode IRC using Irssi & Tor](<https://bbs.archlinux.org/viewtopic.php?pid=956467>)。 

###  外部链接

  * [Accessing freenode Via Tor](<https://web.archive.org/web/20160217155848/https://freenode.net/irc_servers.shtml#tor>)
  * [SASL README](<https://web.archive.org/web/20120618084030/http://freenode.net/sasl/README.txt>)
  * [IRC/SILC torproject.org 上的 Wiki](<https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO/IrcSilc>)

##  使用 HTTP 代理

如果你需要一个 HTTP 代理。 

**注意：** 现在 Tor 开发组推荐在 Privoxy 上使用 Polipo. [[2]](<https://trac.torproject.org/projects/tor/wiki/doc/TorFAQ#WhydoweneedPolipoorPrivoxywithTorWhichisbetter>)

### Privoxy

Privoxy 是一个 HTTP 代理，它使用 SOCKS4a 代理进行 html/cookie 过滤。可以安装 [Privoxy](<../zh-cn/Privoxy.html> "Privoxy") 文章安装。 

####  在Firefox使用Tor 和 Privoxy

最简单的方法就是使用[Torbutton](<https://2019.www.torproject.org/docs/torbutton/>) 扩展。 

或者, 你可以使用[Foxyproxy](<https://addons.mozilla.org/firefox/addon/foxyproxy-standard>)。然后重启Firefox你就会发现一个新的工具条。 点 _Add_ , 选 _Standard proxy type_. 选 你要的 _Proxy Label_ , 例如 _Tor_ 。进入“HTTP Proxy”和“SSL Proxy”区域： 
    
    Hostname: 127.0.0.1 Port: 8118
    
然后Firefox将会用代理连接。你也可以在 _No Proxy for_ 添加例外。 

现在,返回 <https://whatsmyip.net/> 检查你的ip地址是否和以前不同了。 

####  在其他程序使用Tor 和Privoxy

你可以在像即时通信, Jabber, IRC,等软件使用这个方法。 

你可以指定代理(127.0.0.1 port 8118)在那些支持HTTP代理的软件里面。 

如果使用SOCKS 代理，你可以指定你的程序到Tor (127.0.0.1 port 9050)。用这种方法的一个问题是，虽然自己做DNS解析的应用程序可能会泄漏信息。 

你可以考虑使用Socks4A (e.g. via privoxy)来取代他。 

##  运行Tor 服务

###  配置

你的带宽必须至少20kb/s: 
    
    Nickname <tornickname>
    ORPort 9001
    BandwidthRate 20 KB            # Throttle traffic to 20KB/s
    BandwidthBurst 50 KB           # But allow bursts up to 50KB/s
    ExitRelay 0                  # Disallow exits from your relay
    
允许 Irc 在 6660-6667 端口输出： 
    
    ExitPolicy accept *:6660-6667,reject *:* # Allow irc ports but no more
    
Tor 作为输出节点: 
    
    ExitPolicy accept *:119        # Accept nntp as well as default exit policy
    
Tor 作为中间人： 
    
    ExitPolicy reject *:*
    
##  运行 Tor 网桥

Tor 网桥是旨在 ISP 运营商或政府阻止访问中继 (relay) 时提供的连接方案，通过访问[bridges](<https://bridges.torproject.org/>)来了解网桥的工作原理。 

需要使用网桥时需在 `/etc/tor/torrc` 添加一下4行：
    
    /etc/tor/torrc
    
    SOCKSPort 0
    ORPort 443
    BridgeRelay 1
    ExitRelay 0

## TorDNS

Tor 0.2.x系列提供了一个内置的DNS转发器。在Tor配置文件添加如下文件来启动它。 
    
    /etc/tor/torrc
    
     DNSPort 9053
     AutomapHostsOnResolve 1
     AutomapHostsSuffixes .exit,.onion
    
然后重新启动 Tor 来加载更新过的配置文件： 
    
    /etc/rc.d/tor restart
    
这将让Tor接受DNS请求(在这个例子里面监听着9053端口)。并通过Tor网络域名。一个缺点是，它是仅能够解决一个记录的DNS查询； MX 和NS 请求没有回应。 

更多信息请查看 [Debian-based introduction](<https://techstdout.boum.org/TorDns/>)。 

DNS查询，也可以通过命令行`tor-resolve`来查询。例如： 
    
    $ tor-resolve archlinux.org
    66.211.214.131
    
## Torsocks

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:Tor#](<../zh-cn/Talk:Tor.html>) 中讨论）

[torsocks](<https://archlinux.org/packages/?name=torsocks>)包 will allow you use an application via the Tor network without the need to make configuration changes to the application involved. From the man page: 

_torsocks is a wrapper between the torsocks library and the application in order to make every Internet communication go through the Tor network._

Usage example: 
    
    $ torsocks elinks checkip.dyndns.org
    $ torsocks wget -qO- <https://check.torproject.org/> | grep -i congratulations
    
## Torify

`torify` 允许你的程序不需要更改配置来通过访问Tor网络。 

man page: 
    
     torify  is  a simple wrapper that calls tsocks with a tor specific configuration file.
    
     tsocks itself is a wrapper between the tsocks library and the  application  that
     you would like to run socksified
    
使用例子： 
    
    $ torify elinks checkip.dyndns.org
    $ torify wget -qO- https://check.torproject.org/ | grep -i congratulations
    
Torify **不会** 通过Tor网络来查询DNS。其中一种解决方法就是和`tor-resolve` 来解决(前文所述)。在这种情况下, 上面的例子程序将像这样 
    
    $ tor-resolve checkip.dyndns.org
    208.78.69.70
    $ torify elinks 208.78.69.70
    
##  问题解决

###  User value的问题

如果 _tor_ daemon启动失败，你可以在root环境下运行一下命令(或者使用sudo) 
    
    # tor
    
如果你收到以下 error 
    
    May 23 00:27:24.624 [warn] Error setting groups to gid 43: "Operation not permitted".
    May 23 00:27:24.624 [warn] If you set the "User" option, you must start Tor as root.
    May 23 00:27:24.624 [warn] Failed to parse/validate config: Problem with User value. See logs for details.
    May 23 00:27:24.624 [err] Reading config failed--see warnings above.
    
它意味着你的User value有问题。通过以下的步骤解决： 

运行以下命令检查`/var/lib/tor`目录的权限 
    
    # ls -l /var/lib/
    
如果`/var/lib/tor`权限显示如下 
    
    drwx------ 2 tor    tor    4096 May 12 21:03 tor
    
这意味着它被 _tor_ 用户和 _tor_ 组所拥有 

通过以下命令把拥有者和组改为 _root_ , _root_
    
    # chown -R root:root /var/lib/tor
    
如果你重新检查权限,他现在应该显示为 
    
    drwx------ 2 root   root   4096 May 12 21:03 tor
    
现在打开 `/etc/tor/torrc`找到以下文字 
    
    ## Uncomment this to start the process in the background... or use
    ## --runasdaemon 1 on the command line.
    RunAsDaemon 1
    User tor
    Group tor
    
注释掉 _User tor_ 和 _Group tor_ , 所以他应该显示为 
    
    ## Uncomment this to start the process in the background... or use
    ## --runasdaemon 1 on the command line.
    RunAsDaemon 1
    #User tor
    #Group tor
    
保存更改然后重启 _tor_ daemon, 他应该能够工作了 
    
    # /etc/rc.d/tor restart
    
##  外部链接

  * [Official Website](<https://www.torproject.org/>)
  * [“如何翻墙”系列：关于 Tor 的常见问题解答 @ 编程随想的博客](<https://program-think.blogspot.com/2013/11/tor-faq.html>)
  * [Unix-based Tor Articles](<https://trac.torproject.org/projects/tor/wiki#Unixish>)
  * [Software commonly integrated with Tor](<https://trac.torproject.org/projects/tor/wiki/doc/SupportPrograms>)
  * [How to set up a Tor _Hidden Service_](<https://www.torproject.org/docs/tor-hidden-service.html.en>)
  * [新中继的生命周期](<https://blog.torproject.org/lifecycle-new-relay/>)
  * [贡献服务器作为 Tor 节点](<https://www.ohyee.cc/post/note_tor_as_relay>)
  * [Running a bridge](<https://2019.www.torproject.org/docs/bridges#RunningABridge>)
