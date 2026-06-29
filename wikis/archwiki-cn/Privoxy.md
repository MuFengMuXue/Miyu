[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** A section is still untranslated, no content updates since 2017（在 [Talk:Privoxy#](<../zh-cn/Talk:Privoxy.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [Privoxy](<https://wiki.archlinux.org/title/Privoxy> "arch:Privoxy")，最近一次同步于 2017-10-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Privoxy?diff=0&oldid=491654>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Privoxy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Tor](<../zh-cn/Tor.html> "Tor")

[Privoxy](<https://www.privoxy.org/>) 是一个 HTTP 协议过滤代理，常结合 Tor 使用。Privoxy 是有着先进的过滤能力和保护隐私的代理工具，它可以过滤网页内容，管理cookies，控制访问，除广告、横幅、弹出窗口等等，它同时支持单系统和多用户网络。 

当用户直接使用 [SOCKS](<https://en.wikipedia.org/wiki/SOCKS> "wikipedia:SOCKS") 代理访问网络时，浏览器会泄漏 DNS 请求，降低匿名性，这时应该使用 Privoxy。 

##  安装

安装 [privoxy](<https://archlinux.org/packages/?name=privoxy>)包。 

##  配置

使用Privoxy必须指定转发规则，Privoxy的主配置文件在`/etc/privoxy/config`。 

###  监听地址

Privoxy默认只提供给本机使用（即localhost或者127.0.0.1），如果需要将Privoxy提供给网络中的其他计算机使用，需要`/etc/privoxy/config`在添加监听信息，格式： 
    
    listen-address [SERVER-IP]:[PORT]
    
例如提供给192.168.1.1的8118端口使用: 
    
    listen-address 192.168.1.1:8118
    
###  转发协议

编辑 `/etc/privoxy/config`文件添加相关转发规则： 

  * 转发socks5

示例（注意9050后面有一个空格和点号）： 
    
     forward-socks5 / localhost:9050 .
    
  * 转发.i2p

通过[I2P](<../zh-cn/I2P.html> "I2P")路由转发.i2p，示例： 
    
     forward .i2p localhost:4444
    
  * 转发onion

示例（注意9050后面有一个空格和点号）： 
    
    forward-socks4a .onion localhost:9050 .
    
###  广告屏蔽

**警告：** Blocking advertisements can reduce anonymity, since it creates a unique browser signature. This should not be done when using tor or another proxy for anonymity.

Using an ad blocking extension in a web browser can increase page load time. Additionally, extensions like AdBlock Plus are not supported by all browsers. A useful alternative is to install system-wide ad blocking by setting a proxy address in your preferred browser. 

You can use adblock plus filters. The [privoxy blocklist](<https://github.com/Andrwe/privoxy-blocklist>) script automatically downloads adblock plus filters, converts them to a privoxy friendly format, and edits privoxy's config file to include those filters: 

  1. Run the script once to create `/etc/conf.d/privoxy-blacklist`
  2. Edit `/etc/conf.d/privoxy-blacklist` to uncomment the line `PRIVOXY_USER=` and the two lines below it.
  3. Run the script again to download and install the blocklists.
  4. Restart privoxy.

To block tracking via embedded Facebook "Like" button, Twitter "follow", and Google Plus "+1", edit `/etc/privoxy/user.action` and add these lines to the end: 
    
    {+block-as-image{Facebook "like" and similar tracking URLs.}}
    www.facebook.com/(extern|plugins)/(login_status|like(box)?|activity|fan)\.php
    platform.twitter.com/widgets/follow_button?
    plusone.google.com
    
##  使用

使用[Systemd (简体中文)](</wzh/index.php?title=Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Systemd \(简体中文\)（页面不存在）") 启用privoxy服务。 

对程序进行代理设置，默认的地址是: 
    
    localhost:8118
    
Firefox浏览器:进入 首选项 > 高级 > 网络 > 设置，添加http代理。 

Chromium 
    
    $ chromium --proxy-server="localhost:8118"
    
你也可以添加`http_proxy`环境变量，例如添加到`~/.bashrc`中: 
    
    http_proxy="http://localhost:8118"
    
参看[Proxy settings](<../zh-cn/Proxy_settings.html> "Proxy settings")

##  参阅

  * [Privoxy 官方网站](<https://www.privoxy.org/>)
  * [Tor 官方网站](<https://www.torproject.org/>)
