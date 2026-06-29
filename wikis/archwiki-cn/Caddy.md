**翻译状态：**

  * 本文（或部分内容）译自 [Caddy](<https://wiki.archlinux.org/title/Caddy> "arch:Caddy")，最近一次同步于 2024-05-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Caddy?diff=0&oldid=804458>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Caddy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Caddy](<https://caddyserver.com/>) 是具有 HTTP/2 功能的[网页服务器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8> "应用程序列表/互联网")，具有自动 HTTPS 配置功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [caddy](<https://archlinux.org/packages/?name=caddy>)包 软件包。 

##  插件

如果你需要比默认 caddy 更多的功能，可以使用 [xcaddy-bin](<https://aur.archlinux.org/packages/xcaddy-bin/>)AUR 来自定义 caddy server 构建。这对于需要如 DNS challenge 插件等场景非常有用。 另外，在可用的情况下，你也可以直接从 [AUR](<https://aur.archlinux.org/packages/?O=0&K=caddy>) 挑选要要安装的带插件预构建版本，例如 [caddy-cloudflare](<https://aur.archlinux.org/packages/caddy-cloudflare/>)AUR。 

你可以使用 xcaddy 构建带特定插件的定制 caddy server： 
    
    $ xcaddy build [<caddy_version>]
       [--output <file>]
       [--with <module[@version][=replacement]>...]
    
更多信息可参考 [xcaddy 存储库](<https://github.com/caddyserver/xcaddy>)。 

##  配置

Caddy 2 支持多种配置格式，详情可参考[配置适配器](<https://caddyserver.com/docs/config-adapters>)（包括 caddyfile，[nginx](<../zh-cn/Nginx.html> "Nginx")，json，yaml，toml 等）。 

最常用的做法是使用被称为 [Caddyfile](<https://caddyserver.com/docs/caddyfile>) 的纯文本文件。`Caddyfile` 由（可选的[全局选项块](<https://caddyserver.com/docs/caddyfile/options>)及）要发布的网页地址开头，后接数个次级指令。 

一个简单的 `Caddyfile` 如下所示，在 `localhost:2020` 发布了一个网页： 
    
    {
      http_port 2020
    }
    
    localhost:2020
    file_server
    
##  用法
    
    $ caddy help
    $ caddy help run
    
Caddy 可以由页面目录中的任何用户运行，并且 `Caddyfile` 应该位于同一目录中： 
    
    $ caddy run
    
或者，您可以指定一个自定义的 `Caddyfile`： 
    
    $ caddy run --config ../path/to/Caddyfile
    
##  故障排除

###  证书错误

如果你遇到了任何 SSL 证书相关问题（特别是在非公开域名上），基本上都由 caddy 实例无将证书添加到系统信任存储位置的权限导致。在使用 `caddy.service` 自动启动 caddy 时似乎都由于该问题导致。 

要修复该问题，请使用 root 权限执行以下命令。你只需隔很长时间运行一次该命令（根证书的寿命周期）。 
    
    # XDG_DATA_HOME=/var/lib caddy trust
    
##  参见

  * [Caddy 官方网站](<https://caddyserver.com/>)
  * [Caddy 用户指南](<https://caddyserver.com/docs>)
  * [Caddyfile 文档](<https://caddyserver.com/docs/caddyfile>)
