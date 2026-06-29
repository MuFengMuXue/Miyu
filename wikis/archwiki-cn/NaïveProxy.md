相关文章

  * [Trojan](</wzh/index.php?title=Trojan&action=edit&redlink=1> "Trojan（页面不存在）")
  * [Shadowsocks](<../zh-cn/Shadowsocks.html> "Shadowsocks")
  * [V2Ray](<../zh-cn/V2Ray.html> "V2Ray")
  * [WireGuard](<../zh-cn/WireGuard.html> "WireGuard")

**翻译状态：**

  * 本文（或部分内容）译自 [NaïveProxy](<https://wiki.archlinux.org/title/Na%C3%AFveProxy> "arch:NaïveProxy")，最近一次同步于 2024-07-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Na%C3%AFveProxy?diff=0&oldid=812751>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Na%C3%AFveProxy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[NaïveProxy](<https://github.com/klzgrad/naiveproxy>) 是一个跨平台的代理工具，使用了 Chromium 的网络栈来伪装流量，并在绕过[中国国家防火墙](<https://zh.wikipedia.org/wiki/Great_Firewall> "wiki-zh:Great Firewall")时提供了强大的反审查能力和低可检测性。它可以减轻由 TLS 指纹特征造成的被识别问题，并在[中国大规模封锁基于 TLS 的审查规避工具](<https://github.com/net4people/bbs/issues/129>)时成功存活。它需要一个 `naiveproxy` 客户端和一个带有 `forwardproxy` 模块的 [Caddy](<../zh-cn/Caddy.html> "Caddy") 服务器来工作。 

##  安装

安装 [naiveproxy](<https://aur.archlinux.org/packages/naiveproxy/>)AUR 或 [naiveproxy-git](<https://aur.archlinux.org/packages/naiveproxy-git/>)AUR 来获取最新的开发版本，并执行 `naiveproxy config.json`。下面是一个配置文件示例： 
    
    config.json
    
    {
      "listen": "socks://127.0.0.1:1080",
      "proxy": "https://myUsername:myStrongPassword@my.domain"
    }
    
##  配置

如果没有一个带有 forwardproxy 模块的 caddy 服务器，Naiveproxy 将无法工作。你可以用 `xcaddy` 来构建它： 
    
    $ go install github.com/caddyserver/xcaddy/cmd/xcaddy@latest
    $ ~/go/bin/xcaddy build --with github.com/caddyserver/forwardproxy@caddy2=github.com/klzgrad/forwardproxy@naive
    
接着，配置 caddy： 
    
    /etc/caddy/Caddyfile
    
    {
      order forward_proxy before file_server
    }
    :443, my.domain:443 {
      tls /etc/caddy/ssl.cer /etc/caddy/ssl.key
      forward_proxy {
        basic_auth myUsername myStrongPassword
        hide_ip
        hide_via
        probe_resistance
      }
      file_server {
        root /var/www/html
      }
    }
    
注意，为了让这个 Caddyfile 能正常工作，`:443` 必须放在最前面。有关如何配置 TLS 证书的说明，请参阅 [Caddyfile 文档](<https://caddyserver.com/docs/caddyfile/directives/tls>)。 

然后，启动 caddy 服务器： 
    
    # setcap cap_net_bind_service=+ep ./caddy && ./caddy start
    
您可能也想要[把 caddy 作为一个守护进程运行](<https://github.com/klzgrad/naiveproxy/wiki/Run-Caddy-as-a-daemon>)。 
