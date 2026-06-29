  
**翻译状态：**

  * 本文（或部分内容）译自 [DNS-over-HTTPS](<https://wiki.archlinux.org/title/DNS-over-HTTPS> "arch:DNS-over-HTTPS")，最近一次同步于 2024-01-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/DNS-over-HTTPS?diff=0&oldid={{{3}}}>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DNS-over-HTTPS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")
  * [域名解析](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "域名解析")

[DNS-over-HTTPS](<https://github.com/m13253/dns-over-https>)是 [DNS over HTTPS](<../zh-cn/DNS_over_HTTPS.html> "DNS over HTTPS") 的一个实现。它可以作为一个本地解析器。 

##  安装

安装[dns-over-https](<https://archlinux.org/packages/?name=dns-over-https>)包包。 

##  客户端启动

###  禁用任何绑定到53端口的服务

为了查看是否有程序在使用53端口，运行： 
    
    $ ss -lp 'sport = :domain'
    
如果输出超过了一行，你需要禁用任何使用53端口的服务。一旦以上命令只输出以下内容，您就可以继续操作了： 
    
    Netid State   Recv-Q  Send-Q   Local Address:Port     Peer Address:Port Process
    
###  更改系统DNS服务器

将系统的DNS服务器更改为配置文件`listen = `中的地址。如果你不知道自己在做什么，建议使用`127.0.0.1`。 

这可以通过[Network Manager](<../zh-cn/Network_configuration.html#Network_managers> "Network configuration")或编辑[/etc/resolv.conf](</wzh/index.php?title=/etc/resolv.conf&action=edit&redlink=1> "/etc/resolv.conf（页面不存在）")来完成。 

###  启动

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")或[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `doh-client.service`。 

###  测试配置

要测试你系统的DNS是否有效，请在命令行输入`nslookup www.baidu.com`。假定您在安装之前有配置好DNS，这会在配置好DNS over HTTPS之前成功执行。 

##  客户端配置

客户端配置文件默认是`/etc/dns-over-https/doh-client.conf`。 

###  选择首选的上游DNS服务器

要选择首选[DNS服务器](<https://wiki.archlinux.org/title/DNS_server>)，请取消注释其中一个配置文件。 

如果你使用的DNS服务器未列出，你可以在`[upstream]` 部分使用此模板： 
    
    /etc/dns-over-https/doh-client.conf
    
    [[upstream.upstream_ietf]]
        url = "https://[IP or web address]/dns-query"
        weight = 20

##  故障排除

###  服务在有线连接中无法正常启动

正如[开发者所说](<https://github.com/m13253/dns-over-https/issues/150#issuecomment-1709965957>): 

    ArchLinux没有默认的网络管理器，因此systemd没有预先配置的在线检测。
    如果你用Wi-Fi,我建议确保systemd的在线检测能正常运行。我相信你的系统已经安装网络管理器，例如NetworkManager。以帮助你管理Wi-Fi密码。
    或者，如果你用有线网络，简单地修改.service文件以禁用在线检测将是最简单的解决方案。为非移动机器安装NetworkManager可能违反K.I.S.S.原则，我们不希望这样做。

上游[建议](<https://github.com/m13253/dns-over-https/issues/150#issuecomment-1706261425>)对服务文件使用[附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "附加配置片段")： 
    
    /etc/systemd/system/doh-client.service.d/override.conf
    
    [Unit]
    After=multi-user.target
    
    [Service]
    Type=idle
