**翻译状态：**

  * 本文（或部分内容）译自 [Cloudflared](<https://wiki.archlinux.org/title/Cloudflared> "arch:Cloudflared")，最近一次同步于 2025-04-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cloudflared?diff=0&oldid=830457>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cloudflared_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Cloudflared](<https://developers.cloudflare.com/1.1.1.1/dns-over-https/cloudflared-proxy/>) 可被用于运行本地 [DNS over HTTPS](<../zh-cn/DNS_over_HTTPS.html> "DNS over HTTPS")（DoH）服务器，也就是存根解析器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cloudflared](<https://archlinux.org/packages/?name=cloudflared>)包。 

##  用法

运行 `cloudflared proxy-dns` 来启动 DNS over HTTPS 代理服务器。 

使用 `--address` 和 `--port` 选项来指定 cloudflared 监听的地址和端口，它们的默认值分别为 `localhost` 和 `53`。详细的可用命令行选项清单可在[这里](<https://fig.io/manual/cloudflared/proxy-dns>)查看。 

你可以创建一个 systemd [单元文件](<../zh-cn/Systemd.html#%E7%BC%96%E5%86%99%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")，例如： 
    
    /etc/systemd/system/cloudflared.service
    
    [Unit]
    Description=DNS over HTTPS proxy client
    Wants=network-online.target nss-lookup.target
    Before=nss-lookup.target
    
    [Service]
    AmbientCapabilities=CAP_NET_BIND_SERVICE
    CapabilityBoundingSet=CAP_NET_BIND_SERVICE
    DynamicUser=yes
    ExecStart=/usr/bin/cloudflared proxy-dns --port 54
    
    [Install]
    WantedBy=multi-user.target

**注意：** Extra 包不提供服务单元文件。参见 [archlinux/packaging/packages/cloudflared#1](<https://gitlab.archlinux.org/archlinux/packaging/packages/cloudflared/-/issues/1>)。

启动服务后，你可以使用 [drill(1)](<https://man.archlinux.org/man/drill.1>)（由 [ldns](<https://archlinux.org/packages/?name=ldns>)包 提供）来确认它是否在正常工作。 
    
    $ drill archlinux.org @127.0.0.1 -p 54
    
##  检查

通过 [1.1.1.1/help](<https://1.1.1.1/help>) 来检查浏览器是否在使用 _Cloudflare DoH_ 。 

##  上游节点

默认情况下 cloudflared 会使用 `https://1.1.1.1/dns-query` 和 `https://1.0.0.1/dns-query`，即 [Cloudflare DoH 服务器](<https://en.wikipedia.org/wiki/1.1.1.1> "wikipedia:1.1.1.1")的地址作为上游 URL。 

你可以通过 `--upstream` 选项来指定不同的上游节点 URL。 

**注意：** 请使用你信任的 DNS 解析服务器，可参考[域名解析#第三方 DNS 服务](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html#%E7%AC%AC%E4%B8%89%E6%96%B9_DNS_%E6%9C%8D%E5%8A%A1> "域名解析").

##  参阅

  * [官方指引](<https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/>)
  * [命令行选项](<https://fig.io/manual/cloudflared/proxy-dns>)
  * [Running a DNS over HTTPS Client - Cloudflare Resolver](<https://developers.cloudflare.com/1.1.1.1/dns-over-https/cloudflared-proxy/>)
  * [隆重推出家庭版 1.1.1.1](<https://blog.cloudflare.com/zh-cn/introducing-1-1-1-1-for-families/>)
