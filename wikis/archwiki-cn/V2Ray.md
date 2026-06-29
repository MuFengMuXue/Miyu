**翻译状态：**

  * 本文（或部分内容）译自 [V2Ray](<https://wiki.archlinux.org/title/V2Ray> "arch:V2Ray")，最近一次同步于 2023-03-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/V2Ray?diff=0&oldid=765575>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/V2Ray_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[V2Ray](<https://github.com/v2fly/v2ray-core>) 是 Project V 的核心工具，其主要负责网络协议和功能的实现，与其它 Project V 通信。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [v2ray](<https://archlinux.org/packages/?name=v2ray>)包，如果需要最新开发版本请安装 [v2ray-git](<https://aur.archlinux.org/packages/v2ray-git/>)AUR。 

如果需要图形化管理 v2ray，可安装使用 WebUI 管理的 [v2raya](<https://aur.archlinux.org/packages/v2raya/>)AUR (或 [v2raya-bin](<https://aur.archlinux.org/packages/v2raya-bin/>)AUR)。 

[Qv2ray](<../zh-cn/Qv2ray.html> "Qv2ray") 与 Nekoray 已经停止维护，不再推荐安装。 

##  配置

V2Ray 使用 Json 配置， 请参考[配置文件格式](<https://www.v2fly.org/en_US/config/overview.html>)和[配置](<https://www.v2ray.com/en/configuration/index.html>)。 

##  使用

###  命令行

在命令行中使用 `v2ray` 命令启动，参考 [Commandline](<https://www.v2ray.com/en/welcome/command.html>). 

###  服务

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `v2ray.service`。 

###  多文件配置

要使用多文件配置，请编辑 `/etc/systemd/system/v2ray.service`，加入以下内容： 
    
    /etc/systemd/system/v2ray.service
    
    [Unit]
    Description=V2Ray Service
    After=network.target nss-lookup.target
    
    [Service]
    User=nobody
    AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
    CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
    ExecStart=/usr/bin/v2ray -confdir /etc/v2ray/
    
    [Install]
    WantedBy=multi-user.target
    
###  配置方式

V2Ray 有多种配置方式，目前较为有效的是 WebSocket+TLS。 

**提示：** 将 TLS 交由 [Nginx](<../zh-cn/Nginx.html> "Nginx") 配置，是一种更合理，也更易于管理的方式。

##  提示与技巧

###  路由规则

参见[路由](<https://www.v2ray.com/en/configuration/routing.html>)和 [V2Ray 路由](<https://guide.v2fly.org/en_US/basics/routing/basics_routing.html>)。 

预设的路由规则文件是 `geosite.dat` 和 `geoip.dat`，位于 `/usr/share/v2ray`。这两个文件分别由软件包 [v2ray-domain-list-community](<https://archlinux.org/packages/?name=v2ray-domain-list-community>)包 和 [v2ray-geoip](<https://archlinux.org/packages/?name=v2ray-geoip>)包 提供。这两个软件包将被作为 [v2ray](<https://archlinux.org/packages/?name=v2ray>)包 的依赖项安装。 

####  替换预设的路由规则文件

有些路由规则文件有现成的软件包。比如对 [@Loyalsoldier/v2ray-rules-dat](<https://github.com/Loyalsoldier/v2ray-rules-dat>) 来说，可以安装 [v2ray-rules-dat-git](<https://aur.archlinux.org/packages/v2ray-rules-dat-git/>)AUR 软件包。 

对于没有现成软件包的路由规则文件，可以[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")并安装，或者[在不移除依赖包的前提下](<../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")移除 [v2ray-domain-list-community](<https://archlinux.org/packages/?name=v2ray-domain-list-community>)包 和 [v2ray-geoip](<https://archlinux.org/packages/?name=v2ray-geoip>)包 然后将路由规则文件放在 `/usr/share/v2ray` 目录下。 

**警告：** 直接替换 `geosite.dat` 和 `geoip.dat` 可能导致[文件冲突](<../zh-cn/Pacman.html#"Failed_to_commit_transaction_\(conflicting_files\)"_%E9%94%99%E8%AF%AF> "Pacman")。

##  故障排除

###  Failed with result 'exit-code'

如果您在日志里看到了此错误：`Failed with result 'exit-code'`，这是因为 V2Ray 对目录 /var/log/v2ray/access.log 没有写入权限。使用以下命令可解决此问题。 
    
    chown -R nobody /var/log/v2ray
    
##  另请参阅

  * [V2Fly 官方网站和文档](<https://www.v2fly.org/>)
  * [V2Ray 新手指南](<https://guide.v2fly.org/>)
  * [v2rayA 官方网站和文档](<https://v2raya.org/>)
  * [Nekoray 官方网站和文档](<https://matsuridayo.github.io/>)
  * 不再推荐使用 [Qv2ray](<../zh-cn/Qv2ray.html> "Qv2ray") (项目已经停止维护) 。
