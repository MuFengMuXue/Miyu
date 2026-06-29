**翻译状态：**

  * 本文（或部分内容）译自 [Irssi](<https://wiki.archlinux.org/title/Irssi> "arch:Irssi")，最近一次同步于 2023-01-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Irssi?diff=0&oldid=664570>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Irssi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [IRC channels](<../zh-cn/IRC_channels.html> "IRC channels")
  * [IRC](<../zh-cn/Arch_%E7%9A%84_IRC_%E9%A2%91%E9%81%93.html> "IRC")
  * [WeeChat](</wzh/index.php?title=WeeChat&action=edit&redlink=1> "WeeChat（页面不存在）")
  * [HexChat](</wzh/index.php?title=HexChat&action=edit&redlink=1> "HexChat（页面不存在）")

[Irssi](<https://irssi.org/>) 是一个基于 [ncurses](<https://invisible-island.net/ncurses/announce.html>)、模块化的 [IRC](<https://en.wikipedia.org/wiki/Internet_Relay_Chat> "wikipedia:Internet Relay Chat") (互联网中继聊天 Internet Relay Chat) 客户端。 

得益于健壮的社区以及官方插件的支持，使得 Irssi 客户端能够支持 [SILC](<https://en.wikipedia.org/wiki/SILC_\(protocol\)> "wikipedia:SILC \(protocol\)")和 [ICB](<http://www.icb.net/_jrudd/icb/protocol.html>) 协议。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [irssi](<https://archlinux.org/packages/?name=irssi>)包 。 

在 AUR 的 [irssi-script](<https://aur.archlinux.org/packages/?O=0&K=irssi-script>) 下和 [Irssi's Script Repository](<https://scripts.irssi.org/>) 有一些脚本。 

##  使用

更详细的介绍请阅读[官方文档](<https://irssi.org/documentation>)。 

**注意：** 这部分假定您了解 IRC 的基本知识并过去用过其他客户端。

推荐使用[终端复用器](</wzh/index.php?title=%E7%BB%88%E7%AB%AF%E5%A4%8D%E7%94%A8%E5%99%A8&action=edit&redlink=1> "终端复用器（页面不存在）")，例如 [tmux](<../zh-cn/Tmux.html> "Tmux") 或者 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 等。它能让用户轻松地断开和重新连接一个会话，并且能够运行如 [nicklist.pl](<http://wouter.coekaerts.be/site/irssi/nicklist>) 这类依赖次要窗口的脚本。要运行 irssi ，执行： 
    
    $ irssi
    
参见 [irssi(1)](<https://man.archlinux.org/man/irssi.1>)。 

###  命令

Irssi 的命令以反斜杠为开始，并且大小写不敏感。您可以输入 `/help` 来获得内建的命令列表。这份列表也能[在线查阅](<https://irssi.org/documentation/help/>)。 

命令  | 说明   
---|---  
[/help](<https://irssi.org/documentation/help/help/>) | 列出所有命令或者解释给定的命令。   
[/network](<https://irssi.org/documentation/help/network/>) | 管理您的 IRC 网络。   
[/server](<https://irssi.org/documentation/help/server/>) | 管理您的 IRC 服务器。   
[/connect](<https://irssi.org/documentation/help/connect/>) | 连接一个服务器或者网络。   
[/disconnect](<https://irssi.org/documentation/help/disconnect/>) | 断开目前的服务器连接。   
`ALT+(1-0,q-p,etc)` | 切换活动窗口。`Ctrl+n` 循环到下一个窗口，`Ctrl+p` 循环到前一个。   
[/window](<https://irssi.org/documentation/help/window/>) | 管理 irssi 窗口。   
[/layout](<https://irssi.org/documentation/help/layout/>) | 保存或者关闭窗口配置。   
[/statusbar](<https://irssi.org/documentation/help/statusbar/>) | 管理状态栏。   
[/set](<https://irssi.org/documentation/help/set/>) | 查看或者变更设置。   
[/alias](<https://irssi.org/documentation/help/alias/>) | 管理您的别名。   
  
##  设置

个人设置文件应当位于 `~/.irssi/config`。在 `/etc/irssi.conf` 有一份模板。使用 `--config` 参数也能使用代替的配置文件启动 irssi。 

  * 您可以使用 `/save` 来把当前的配置保存到配置文件中。
  * 您可以使用 `/layout save` 来保存当前打开的窗口的位置。

###  使用SASL进行身份验证

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Is `-ssl_capath` actually needed?（在[Talk:Irssi](<../zh-cn/Talk:Irssi.html>)讨论）

Irssi 是支持 [Simple Authentication and Security Layer](<https://en.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer> "wikipedia:Simple Authentication and Security Layer") (SASL)进行登录的。 

你可以进行如下设置，实现以SASL的身份认证机制添加IRC聊天服务器（如LiberaChat） 
    
    /SERVER ADD -ssl -ssl_verify -ssl_capath /etc/ssl/certs -network liberachat -port 6697 irc.libera.chat
    /NETWORK ADD -sasl_mechanism plain -sasl_username _username_ -sasl_password _password_ liberachat
    
**注意：**

  * IRC聊天服务器的名字是区分大小写的，请确保服务器的名字输入正确
  * 如上的第一条命令，是用于添加允许 [#TLS Connection](<#TLS_Connection>)的聊天服务器
  * 如果你之前已经添加了聊天服务器，只需输入第二条命令即可
  * 如果你的IRC账户的密码中含有 `$`, 你必须额外再加一个 `$` 作为前缀，使得Irssi将`$`作为正常字符进行读取。如将密码设置为`1234$$56`

如果上述操作没问题的话，Irssi在重启之后，你就能看到在所加入的IRC聊天服务器的频道内输出SASL认证成功的信息。 

###  启动时自动连接到 #archlinux

启动 irssi 并输入以下命令： 
    
    /server add -auto -network liberachat irc.libera.chat
    
`liberachat` 可以用任何喜欢的词代替，例如常用缩写 `fn`。 

保证 [SASL](<#Authenticating_with_SASL>) 设置正确。也可以配合 `-autosendcmd` 命令使用 NickServ 代替 SASL，但是这可能会与您设置的自动加入频道的设置发生冲突。如果愿意的话，可以使用 SSL 证书代替给 NickServ 发送密码认证。 
    
    /channel add -auto #archlinux liberachat
    /channel add -auto #archlinux-offtopic liberachat
    
###  TLS 连接

LiberaChat 是使用 6697 端口进行 SSL/TLS 连接的。 若想通过TLS连接LiberaChat IRC网络，可以进行以下设置： 
    
    /server add -auto -tls -tls_verify -network liberachat -port 6697 irc.libera.chat
    
保存更改： 
    
    /save
    
如果配置成功，那么你将会看到“Z”模组的设置。你应该会看到以下输出："Mode change (+Zi) for user `你的用户名`

#### Client certificates

LiberaChat 和 [OFTC](<Https://www.oftc.net/>) 都支持使用SSL证书进行身份认证并为其提供了相应的明文密码的替代方案。 欲知详情，请看LiberaChat的‘[使用CertFP](<https://libera.chat/guides/certfp>)’的指导。 

要创建有效期为730天的无密码证书（当被要求输入详细信息，如状态或甚至通用名称（CN）时，您可以填写任何您想要的内容）： 
    
    $ openssl req -newkey rsa:4096 -days 730 -x509 -keyout irssi.key -out irssi.crt -nodes 
    $ cat irssi.crt irssi.key > ~/.irssi/irssi.pem
    $ chmod 600 ~/.irssi/irssi.pem
    $ rm irssi.crt irssi.key
    
接下来，找出相应的指纹： 
    
    $ openssl x509 -sha512 -fingerprint -noout -in ~/.irssi/irssi.pem | sed -e 's/^.*=//;s/://g;y/ABCDEF/abcdef/'
    
这将把SHA512指纹写入至标准输出(stdout)。 如果需要SHA1指纹, 将参数 `-sha512` 改为 `-sha1`。sed命令可用于通过删除不需要的文本和字符来正确格式化指纹。 

赋值其指纹字符串，稍后将会使用它。 

在irssi中，断开与网络的连接并为其添加客户端证书和密钥。如果您的证书是在没有密码的情况下生成的，请省略-ssl_pass选项： 
    
    /disconnect liberachat
    /server add -ssl_cert ~/.irssi/irssi.pem  -ssl_pass _irssi.pem_password_ -network liberachat irc.libera.chat 6697
    
现在，您可以进行连接(不是`重新连接`哦！)以及注册指纹了 
    
    /connect liberachat
    /msg NickServ identify _YOUR_PASSWORD_
    /msg NickServ cert add _YOUR_FINGERPRINT_
    
此时，您可以从配置文件中删除密码了(如果您将其保存在其中)，并使用以下命令来保存配置 
    
    /save
    
###  启用自动日志记录功能
    
    /SET autolog ON
    /save
    
###  隐藏频道内其他用户的状态

为了忽略所有频道用户的加入、离开和退出显示，请在Irssi中输入以下内容： 
    
    /ignore * joins parts quits
    
查阅 [smartfilter](<https://github.com/lifeforms/irssi-smartfilter>) 来限制活跃用户的上线提醒 

###  鼠标滚动

为了能在Irssi下启动鼠标滚动功能, 输入以下命令: 
    
     /run scriptassist
     /script install mouse.pl
    
欲将其在Irssi运行开始时启用鼠标滚动功能，请输入以下命令： 
    
     /script autorun mouse.pl
    
如果以上命令不起作用, 你可以手动将[mouse.pl](<https://github.com/irssi/scripts.irssi.org/blob/master/scripts/mouse.pl>)脚本放入`~/.irssi/scripts` 或者 `~/.irssi/scripts/autorun`，操作如下: 
    
     /script load mouse.pl
    
##  技巧

###  HTTP 代理

要在Irssi下使用HTTP代理，需要以下命令： 
    
    /SET use_proxy ON
    /SET proxy_address <Proxy host address>
    /SET proxy_port <Proxy port>
    /SET -clear proxy_string
    /SET proxy_string_after conn %s %d
    /EVAL SET proxy_string CONNECT %s:%d HTTP/1.0\n\n
    
然后irssi应该相应地修改其配置文件；如果不需要代理，只需将use_proxy设置为OFF。 

如果代理需要密码，请尝试： 
    
    /SET proxy_password your_pass
    
否则： 
    
    /SET -clear proxy_password
    
**注意：** 如果设置了HTTP代理，那么SSL认证将失效！

###  在Irssi中使用tmux来显示频道内的用户昵称列表

Irssi 插件 [nicklist](<https://scripts.irssi.org/scripts/nicklist.pl>) 提供了一个可显示昵称列表的小窗口，有两种方法能够实现哦： 

  * **屏幕 ,** 它只是将列表添加到irssi的右侧，但带来的缺点是每次irssi打印一行时都会重新绘制整个窗口。

  * **FIFO ,** 顾名思义，它将列表写入FIFO，然后可以用例如cat~/.irssi/nicklistfifo连续读取。利用FIFO来实现昵称列表的表现效果会更好：

    /NICKLIST FIFO
    
This fifo can be used in a [tmux](<../zh-cn/Tmux.html> "Tmux") window split vertically with _irssi_ in its left pane and the _cat_ from above in a small one in its right. Since the pane is dependent on its creating tmux session's geometry, a subsequent session with a different one needs to recreate it (which also implies a switch in _irssi_ windows to refill the fifo). 

E.g., the following script first checks for a running _irssi_ , presumed to have been run by a previous execution of itself. Unless found it creates a new tmux session, a window named after and running _irssi_ and then the pane with _cat_. If however _irssi_ was found it merely attaches to the session and recreates the _cat_ pane. 
    
    #!/bin/sh
    
    T3=$(pgrep -u "$USER" -x irssi)
    
    irssi_nickpane() {
        tmux setw main-pane-width $(( $(tput cols) - 21));
        tmux splitw -v "cat ~/.irssi/nicklistfifo";
        tmux selectl main-vertical;
        tmux selectw -t irssi;
        tmux selectp -t 0;
    }
    
    irssi_repair() {
        tmux selectw -t irssi
        [ "$(tmux lsp | wc -l)" -gt 1 ] && tmux killp -a -t 0
        irssi_nickpane
    }
    
    if [ -z "$T3" ]; then
        tmux new-session -d -s main;
        tmux new-window -t main -n irssi irssi;
        irssi_nickpane ;
    fi
        tmux attach-session -d -t main;
        irssi_repair ;
    exit 0

**提示：** Instead of doing all this work, [this plugin](<http://anti.teamidiot.de/static/nei/*/Code/Irssi/tmux-nicklist-portable.pl>) does all the work needed for a nice nicklist inside tmux.

###  Virtual hostname (vhost)

A vhost can be used to change your hostname when connected to an IRC-server, commonly viewed when joining/parting or doing a whois. This is most commonly done on a server that has a static IP address. Without a vhost it would commonly look like so when doing a 'whois': 
    
    nick@123.456.78.90.isp.com
    
The result of a successful vhost could be like so if you have the domain example.com available: 
    
    nick@example.com
    
Keep in mind that not every IRC-server supports the use of vhost. This might be individually set between the servers and not the network, so if you are experiencing issues with one server try another on the same network. 

#### Required preconfigurations

Irssi supports using a vhost as long as the required configurations has been set. This includes especially that your host supports [Recursive DNS Lookup (rDNS)](<https://en.wikipedia.org/wiki/Reverse_DNS_lookup> "wikipedia:Reverse DNS lookup") using [Pointer record (PTR)](<https://en.wikipedia.org/wiki/List_of_DNS_record_types> "wikipedia:List of DNS record types"). Additionally you should add an appropriate line to your `/etc/hosts` file. 

To see if this is working, test with the 'host' DNS lookup utility included in [bind](<https://archlinux.org/packages/?name=bind>)包 like so (where _ip_ is a normal IPv4 address): 
    
    host _ip_
    
If this returns something in the lines of this then you know that your rDNS is working. 
    
    _ip_.in-addr.arpa domain name pointer example.com
    
#### Enabling the vhost

There are a couple of ways to connect to a server with a given hostname. One is using the 'server' command with a -host argument like so: 
    
    /server -host example.com irc.libera.chat
    
Another way would be to set your hostname (vhost) with the 'set' command which will save your hostname to `~/.irssi/config`: 
    
    /set hostname example.com
    /save
    /server irc.libera.chat
    
##  更多内容

  * [Official website](<https://irssi.org/>)
  * [Official Irssi script repository](<https://scripts.irssi.org/>)
  * [Setting up Irssi](<https://linuxtidbits.wordpress.com/2008/01/09/setting-up-irssi/>)
  * [Guide to efficiently using Irssi and screen](<https://quadpoint.org/articles/irssi/>) by Matt Sparks
  * [IRC notifications with dzen2](<http://jasonwryan.com/blog/2011/11/07/irc-dzen/>) by Jason Ryan
  * [Irssi’s /channel, /network, /server and /connect – What it means](<https://pthree.org/2010/02/02/irssis-channel-network-server-and-connect-what-it-means/>) by Aaron Toponce
  * [awesome Wiki Irssi tips](<https://web.archive.org/web/20160227121906/http://awesome.naquadah.org/wiki/Irssi_tips>) (Wayback Machine)
  * [irssi systemd unit GitHub gist](<https://gist.github.com/drye/5520101>)
