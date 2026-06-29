**翻译状态：**

  * 本文（或部分内容）译自 [Matrix](<https://wiki.archlinux.org/title/Matrix> "arch:Matrix")，最近一次同步于 2025-03-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Matrix?diff=0&oldid=828383>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Matrix_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Matrix](<https://matrix.org/>) 是一个新的开放式联邦化的即时通信和 VoIP 生态系统。其包含服务端、[客户端](<https://matrix.org/clients/>)和[桥接工具](<https://matrix.org/bridges/>)，可以连接到已有的通信解决方案如[IRC](<https://en.wikipedia.org/wiki/Internet_Relay_Chat> "wikipedia:Internet Relay Chat")。 

Arch Linux 的官方 Matrix 频道位于[#archlinux:archlinux.org](<https://matrix.to/#/#archlinux:archlinux.org>)，一些国际社区有其自己的 Matrix 房间，请参阅[国际社区](<../zh-cn/%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA.html> "国际社区")以了解详细信息。 

对于客户端，请参阅[应用程序列表/互联网#Matrix 客户端](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#Matrix_%E5%AE%A2%E6%88%B7%E7%AB%AF> "应用程序列表/互联网")。 

您可以使用已有的 Matrix 服务器如 <https://matrix.org> 或按照下文创建您自己的 Synapse 服务器。 

##  安装

Matrix 的服务端实现 **Synapse** 由 [matrix-synapse](<https://archlinux.org/packages/?name=matrix-synapse>)包 提供，其会创建一个 _synapse_ 用户。 

##  配置

安装完成后需要生成一个配置文件， _synapse_ 用户应当能够读取该文件： 
    
    # generate_config --server-name _my.domain.name_ \
                      --config-dir /etc/synapse \
                      --data-dir /var/lib/synapse \
                      --report-stats yes \
                      --generate-secrets \
                      --output-file /etc/synapse/homeserver.yaml
    
    # generate_log_config -o /etc/synapse/_my.domain.name_.log.config \
                          -f /var/log/synapse/homeserver.log
                          
    # generate_signing_key --output_file /etc/synapse/_my.domain.name_.signing.key
    
    # chown -R synapse:synapse /etc/synapse \
                               /var/log/synapse

请注意这会为指定的服务器名称生成相应的 SSL 和自签名证书，若您更改了服务器名称，则应重新生成。 

若您的 Synapse 服务器可通过互联网访问，那么非常建议您为其设置[反向代理](<https://github.com/element-hq/synapse/blob/develop/docs/reverse_proxy.md>)。 

##  数据库

Synapse 仅用 SQLite 测试服务器，操作时使用 Postgres。 

要使用 Postgres，请安装 [python-psycopg2](<https://archlinux.org/packages/?name=python-psycopg2>)包。 

您可在官方网站上读到更多有关安装和配置的信息：[Using Postgres](<https://github.com/element-hq/synapse/blob/develop/docs/postgres.md>)

##  服务

[matrix-synapse](<https://archlinux.org/packages/?name=matrix-synapse>)包 包含 systemd 服务 `synapse.service`，其会按照配置文件 `/etc/synapse/homeserver.yaml` 以用户 _synapse_ 启动 Synapse 服务端。 

##  用户管理

您的新 synapse 服务器需要至少一个用户，可以执行以下命令创建您的默认非 root 用户： 
    
    [synapse]$ register_new_matrix_user -c /etc/synapse/homeserver.yaml <http://127.0.0.1:8008>
    
也可以使用一个 [matrix 客户端](<https://matrix.org/ecosystem/clients/>)，例如 [element-desktop](<https://archlinux.org/packages/?name=element-desktop>)包，或 [libpurple](<https://archlinux.org/packages/?name=libpurple>)包 的 [purple-matrix-git](<https://aur.archlinux.org/packages/purple-matrix-git/>)AUR 插件。 

##  蜘蛛爬虫

如需为链接预览等功能启用蜘蛛爬虫，请安装 [python-lxml](<https://archlinux.org/packages/?name=python-lxml>)包 和 [python-netaddr](<https://archlinux.org/packages/?name=python-netaddr>)包。之后在 `homeserver.yaml` 中设定 `url_preview_enabled: True`。欲使 synapse 服务器拒绝指向内部服务器的 GET 请求，请设定 `url_preview_ip_range_blacklist:`。 

**警告：** 黑名单默认空白：不配置的话synapse 服务器可以爬取您所有的内部主机。

There are some examples that can be uncommented. Add your local IP ranges to that list to prevent the synapse server from trying to crawl them. After changing the `homeserver.yaml`, the service has to be restarted. 

## Interesting channels

KDE community has a wide variety of matrix rooms for specific applications, languages, events and etc. See <https://community.kde.org/Matrix> for details. 

The GNOME Community also has a Matrix instance for its instant communications with a wide variety of matrix rooms. See <https://wiki.gnome.org/GettingInTouch/Matrix> for details. 

## Troubleshooting

### Read-only file system

By default, synapse can only write to the working-directory (`/var/lib/synapse`) set in its service file. A write-error may occur if synapse writes to a different path (e.g. your media-store is in `/var/lib/matrix-synapse/media`). 

You can allow access to other directories by creating a [replacement unit file](</wzh/index.php?title=Replacement_unit_file&action=edit&redlink=1> "Replacement unit file（页面不存在）") for `synapse.service` and by adding `ReadWritePaths=_your_paths_` to the `[Service]` section. 

### High memory consumption

The memory consumption of Synapse can be significantly reduced[[1]](<https://element-hq.github.io/synapse/latest/usage/administration/admin_faq.html#help-synapse-is-slow-and-eats-all-my-ramcpu>) by installing [jemalloc](<https://archlinux.org/packages/?name=jemalloc>)包. To enable it, the [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") `LD_PRELOAD` must be set accordingly. This can be done by creating `/etc/default/synapse`, which will be applied by the systemd unit file.[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/matrix-synapse/-/blob/main/synapse.service?ref_type=heads#L18>)
    
    /etc/default/synapse
    
    LD_PRELOAD=/usr/lib/libjemalloc.so
    
After enabling _jemalloc_ , the memory footprint can be reduced further by tuning cache settings: [[3]](<https://element-hq.github.io/synapse/latest/usage/configuration/config_documentation.html#caches-and-associated-values>)
    
    /etc/synapse/homeserver.yaml
    
    caches:
      cache_autotuning:
        max_cache_memory_usage: 1024M
        target_cache_memory_usage: 758M
        min_cache_ttl: 5m
    
The configuration options under `cache_autotuning` will not work unless _jemalloc_ is enabled. 
