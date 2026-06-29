[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Dnscrypt-proxy](<../zh-cn/Talk:Dnscrypt-proxy.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [DNSCrypt](<https://wiki.archlinux.org/title/DNSCrypt> "arch:DNSCrypt")，最近一次同步于 2018-06-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/DNSCrypt?diff=0&oldid=525116>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DNSCrypt_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[dnscrypt-proxy](<https://github.com/jedisct1/dnscrypt-proxy>) 可以加密和认证用户和 DNS 解析服务器之间的数据传输，支持 [DNS over HTTPS](<https://en.wikipedia.org/wiki/DNS_over_HTTPS> "wikipedia:DNS over HTTPS") 和 [DNSCrypt](<https://dnscrypt.info/>)，可以避免中间人攻击和窃听。 _dnscrypt-proxy_ 兼容 [DNSSEC](</wzh/index.php?title=DNSSEC&action=edit&redlink=1> "DNSSEC（页面不存在）")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [dnscrypt-proxy](<https://archlinux.org/packages/?name=dnscrypt-proxy>)包。 

##  配置

配置文件位于 `/etc/dnscrypt-proxy/dnscrypt-proxy.toml`。 

###  启动

服务有两种启动方式，但是只能二选一： 

  * 启用 `.service`

**注意：** 必须指定 `listen_addresses` (即在配置文件中写好 `listen_addresses = ['127.0.0.1:53', '[::1]:53']`)

  * 启用 `.socket`

**注意：** 必须留空 `listen_addresses` (即 `listen_addresses = [ ]`)，systemd 会自己配置好 socket

###  选择解析服务器

如果留空配置文件 `/etc/dnscrypt-proxy/dnscrypt-proxy.toml` 内的 `server_names`, _dnscrypt-proxy_ 将会自动从 `[sources]` 下选择最快的服务器 [[1]](<https://github.com/jedisct1/dnscrypt-proxy/wiki/Configuration#an-example-static-server-entry>)。服务器列表会自动下载、更新和验证 [[2]](<https://github.com/jedisct1/dnscrypt-proxy/wiki/Configuration-Sources#what-is-the-point-of-these-lists>)，因此无须指定服务器即可使用。 

如果要指定 DNS 服务器，编辑 `/etc/dnscrypt-proxy/dnscrypt-proxy.toml` 然后取消注释里面的 `server_names`，填写一个服务器名。使用 Cloudflare 服务器的配置如下： 
    
    server_names = ['cloudflare', 'cloudflare-ipv6']
    
[upstream page](<https://download.dnscrypt.info/resolvers-list/v2/public-resolvers.md>) 和 [Github](<https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/public-resolvers.md>) 有所有 DNS 服务器的列表。如果 _dnscrypt-proxy_ 之前成功运行过，`/var/cache/dnscrypt-proxy/public-resolvers.md` 文件里也会有一个服务器列表。最好找支持 DNSSEC、无记录且无审查的服务器。使用 `require_dnssec`, `require_nolog`, `require_nofilter` 选项可以强制使用 DNSSEC、禁止记录及禁止审查。 

###  禁用其他占用53端口的服务

**提示：** 如果使用 [#Unbound](<#Unbound>) 提供本地 DNS 缓存，请跳过这一节，因为 _unbound_ 默认监听 53。

查看占用 53 端口的服务： 
    
     $ ss -lp 'sport = :domain'
    
如果输出除了表头还有其他内容，你就需要禁用占用53端口的那些服务，比如 `systemd-resolved.service` 和其他网络管理器包含的类似服务。把它们全部干掉，直到上面的命令的输出只剩这个样子： 
    
     Netid               State                 Recv-Q                Send-Q                     Local Address:Port                                   Peer Address:Port
    
###  修改 resolv.conf

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Explain what the options mean. (在 [Talk:Dnscrypt-proxy](<../zh-cn/Talk:Dnscrypt-proxy.html>) 中讨论)

修改 [resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf")，把现有的`nameserver`全部清掉，添一行指向 _localhost_ 的地址（一般是 127.0.0.1）的`nameserver`；并增添一行 _options_ [[3]](<https://github.com/jedisct1/dnscrypt-proxy/wiki/Installation-linux#step-4-change-the-system-dns-settings>)。示例如下： 
    
    nameserver ::1
    nameserver 127.0.0.1
    options edns0 single-request-reopen
    
其他程序可能会修改 resolv.conf，详见：[resolv.conf#Overwriting of /etc/resolv.conf](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html#Overwriting_of_/etc/resolv.conf> "Resolv.conf")。 

###  启动 systemd 服务

根据上面你选择的[配置](<#%E5%90%AF%E5%8A%A8>)来 [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `dnscrypt-proxy.service` 或者 `dnscrypt-proxy.socket`

##  技巧

###  本地 DNS 缓存配置

**提示：** _dnscrypt_ can cache entries without relying on another program. This feature is enabled by default with the line `cache = true` in your dnscrypt configuration file

It is recommended to run DNSCrypt as a forwarder for a local DNS cache if not using _dnscrypt's_ cache feature; otherwise, every single query will make a round-trip to the upstream resolver. Any local DNS caching program should work. In addition to setting up _dnscrypt-proxy_ , you must setup your local DNS cache program. 

####  修改端口

In order to forward queries from a local DNS cache, _dnscrypt-proxy_ should listen on a port different from the default `53`, since the DNS cache itself needs to listen on `53` and query _dnscrypt-proxy_ on a different port. Port number `53000` is used as an example in this section. In this example, the port number is larger than 1024 so _dnscrypt-proxy_ is not required to be run by root. 

There are two methods for changing the default port: 

**Socket method**

[Edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `dnscrypt-proxy.socket` with the following contents: 
    
    [Socket]
    ListenStream=
    ListenDatagram=
    ListenStream=127.0.0.1:53000
    ListenDatagram=127.0.0.1:53000
    
When queries are forwarded from the local DNS cache to `53000`, `dnscrypt-proxy.socket` will start `dnscrypt-proxy.service`. 

**Service method**

Edit the `listen_addresses` option in `/etc/dnscrypt-proxy/dnscrypt-proxy.toml` with the following: 
    
    listen_addresses = ['127.0.0.1:53000', '[::1]:53000']
    
####  本地 DNS 缓存配置举例

The following configurations should work with _dnscrypt-proxy_ and assume that it is listening on port `53000`. 

##### Unbound

Configure [Unbound](<../zh-cn/Unbound.html> "Unbound") to your liking (in particular, see [Unbound#Local DNS server](<../zh-cn/Unbound.html#Local_DNS_server> "Unbound")) and add the following lines to the end of the `server` section in `/etc/unbound/unbound.conf`: 
    
      do-not-query-localhost: no
    forward-zone:
      name: "."
      forward-addr: 127.0.0.1@53000
    
**提示：** If you are setting up a server, add `interface: 0.0.0.0@53` and `access-control: _your-network_ /_subnet-mask_ allow` inside the `server:` section so that the other computers can connect to the server. A client must be configured with `nameserver _address-of-your-server_` in `/etc/resolv.conf`.

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `unbound.service` to apply the changes. 

##### dnsmasq

Configure dnsmasq as a [local DNS cache](<../zh-cn/Dnsmasq.html#DNS_server> "Dnsmasq"). The basic configuration to work with DNSCrypt: 
    
    /etc/dnsmasq.conf
    
    no-resolv
    server=127.0.0.1#53000
    listen-address=127.0.0.1

If you configured DNSCrypt to use a resolver with enabled DNSSEC validation, make sure to enable it also in dnsmasq: 
    
    /etc/dnsmasq.conf
    
    proxy-dnssec

Restart `dnsmasq.service` to apply the changes. 

##### pdnsd

Install [pdnsd](</wzh/index.php?title=Pdnsd&action=edit&redlink=1> "Pdnsd（页面不存在）"). A basic configuration to work with DNSCrypt is: 
    
    /etc/pdnsd.conf
    
    global {
        perm_cache = 1024;
        cache_dir = "/var/cache/pdnsd";
        run_as = "pdnsd";
        server_ip = 127.0.0.1;
        status_ctl = on;
        query_method = udp_tcp;
        min_ttl = 15m;       # Retain cached entries at least 15 minutes.
        max_ttl = 1w;        # One week.
        timeout = 10;        # Global timeout option (10 seconds).
        neg_domain_pol = on;
        udpbufsize = 1024;   # Upper limit on the size of UDP messages.
    }
    
    server {
        label = "dnscrypt-proxy";
        ip = 127.0.0.1;
        port = 53000;
        timeout = 4;
        proxy_only = on;
    }
    
    source {
        owner = localhost;
        file = "/etc/hosts";
    }

Restart `pdnsd.service` to apply the changes. 

###  沙盒隔离

[Edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `dnscrypt-proxy.service` to include the following lines: 
    
    [Service]
    CapabilityBoundingSet=CAP_IPC_LOCK CAP_SETGID CAP_SETUID CAP_NET_BIND_SERVICE
    ProtectSystem=strict
    ProtectHome=true
    ProtectKernelTunables=true
    ProtectKernelModules=true
    ProtectControlGroups=true
    PrivateTmp=true
    PrivateDevices=true
    MemoryDenyWriteExecute=true
    NoNewPrivileges=true
    RestrictRealtime=true
    RestrictAddressFamilies=AF_INET AF_INET6
    SystemCallArchitectures=native
    SystemCallFilter=~@clock @cpu-emulation @debug @keyring @ipc @module @mount @obsolete @raw-io
    
See [systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>) and [Systemd#Sandboxing application environments](<../zh-cn/Systemd.html#Sandboxing_application_environments> "Systemd") for more information. Additionally see [upstream comments](<https://github.com/DNSCrypt/dnscrypt-proxy/issues/601#issuecomment-426675917>). 

###  启用 EDNS0

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Name the advantages/motivation for enabling this. (在 [Talk:Dnscrypt-proxy](<../zh-cn/Talk:Dnscrypt-proxy.html>) 中讨论)

[Extension Mechanisms for DNS](<https://en.wikipedia.org/wiki/Extension_mechanisms_for_DNS> "wikipedia:Extension mechanisms for DNS") that, among other things, allows a client to specify how large a reply over UDP can be. 

Add the following line to your `/etc/resolv.conf`: 
    
    options edns0
    
[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** dnscrypt-proxy2 uses different config file. (在[Talk:Dnscrypt-proxy](<../zh-cn/Talk:Dnscrypt-proxy.html>)讨论)

You may also wish to append the following to `/etc/dnscrypt-proxy.conf`: 
    
    EDNSPayloadSize _< bytes>_
    
Where _< bytes>_ is a number, the default size being **1252** , with values up to **4096** bytes being purportedly safe. A value below or equal to **512** bytes will disable this mechanism, unless a client sends a packet with an OPT section providing a payload size. 

####  测试 EDNS0

Make use of the [DNS Reply Size Test Server](<https://www.dns-oarc.net/oarc/services/replysizetest>), use the _drill_ command line tool to issue a TXT query for the name _rs.dns-oarc.net_ : 
    
    $ drill rs.dns-oarc.net TXT
    
With **EDNS0** supported, the "answer section" of the output should look similar to this: 
    
    rst.x3827.rs.dns-oarc.net.
    rst.x4049.x3827.rs.dns-oarc.net.
    rst.x4055.x4049.x3827.rs.dns-oarc.net.
    "2a00:d880:3:1::a6c1:2e89 DNS reply size limit is at least 4055 bytes"
    "2a00:d880:3:1::a6c1:2e89 sent EDNS buffer size 4096"
    