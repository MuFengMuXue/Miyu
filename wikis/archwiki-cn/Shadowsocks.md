[Shadowsocks](<https://shadowsocks.org>) 是一个轻量级 [SOCKS5](<https://en.wikipedia.org/wiki/SOCKS_\(protocol\)#SOCKS5> "wikipedia:SOCKS \(protocol\)") 代理。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [shadowsocks-rust](<https://archlinux.org/packages/?name=shadowsocks-rust>)包。 

###  其他可选项

  * [shadowsocks-go](<https://aur.archlinux.org/packages/shadowsocks-go/>)AUR—使用Go语言编写。
  * [shadowsocks-git](<https://aur.archlinux.org/packages/shadowsocks-git/>)AUR—使用Python语言编写。已不再开发。
  * [shadowsocks-libev-static](<https://aur.archlinux.org/packages/shadowsocks-libev-static/>)AUR—使用C语言编写。已不再开发。
  * [go-shadowsocks2](<https://aur.archlinux.org/packages/go-shadowsocks2/>)AUR—使用Go语言编写。已不再开发。

##  配置

Shadowsocks 以 [JSON](<https://en.wikipedia.org/wiki/JSON> "wikipedia:JSON") 为配置文件格式，以下是软件包中的样例： 
    
    /etc/shadowsocks/config.json
    
    {
        "server":"my_server_ip",
        "server_port":8388,
        "local_address": "127.0.0.1",
        "local_port":1080,
        "password":"mypassword",
        "timeout":300,
        "method":"chacha20-ietf-poly1305",
        "fast_open": false,
        "workers": 1,
        "prefer_ipv6": false
    }
    
**提示：**

  * 若需同时指定多个服务端地址，使用如下语法 `"server":["1.1.1.1", "2.2.2.2"]`.
  * 要找出在你的机器上运行最快的方式，可以运行[这个脚本](<https://github.com/shadowsocks/shadowsocks-libev/blob/master/scripts/iperf.sh>)。

名称 | 解释   
---|---  
server  | 服务端监听地址   
server_port  | 服务端端口   
local_address  | 本地监听地址   
local_port  | 本地端口   
password  | 用于加密的密码   
timeout  | 超时时间（秒）   
method  | 加密方式，默认为 `chacha20-ietf-poly1305`  
mode  | 是否启用 TCP / UDP 转发，参阅 [shadowsocks-libev(8)](<https://man.archlinux.org/man/shadowsocks-libev.8>)  
fast_open  | 是否启用 [TCP Fast Open](<https://github.com/shadowsocks/shadowsocks/wiki/TCP-Fast-Open>)  
workers  | worker 数量   
  
##  使用

###  客户端

**警告：**[udns](<https://archlinux.org/packages/?name=udns>)包 用作 DNS 的存根解析程序。为了防止客户端应用程序（如浏览器）的 DNS 请求泄漏，必须使用其他应用程序。例如客户端上的 [Privoxy](<../zh-cn/Privoxy.html> "Privoxy") 或完整的 DNS 解析程序。[[1]](<https://github.com/shadowsocks/shadowsocks-libev/issues/1542>) [[2]](<https://github.com/shadowsocks/shadowsocks-libev/issues/1641>)

####  通过命令行

使用 `ss-local`（shadowsocks-libev）或`sslocal` （shadowsocks-rust）命令启动客户端。 要使用 `/etc/shadowsocks/_config_.json` 配置文件启动客户端: 
    
    $ sslocal -c /etc/shadowsocks/_config_.json
    
或者，也可以直接在命令中指定配置： 
    
    $ sslocal -s _服务器地址_ -p _服务器端口_ -l _本地端口_ -k _密码_ -m _加密方式_
    
要输出详细日志，添加 `-v` 命令: 
    
    $ sslocal -s _服务器地址_ -p _服务器端口_ -l _本地端口_ -k _密码_ -m _加密方式_ -v
    
####  守护进程管理

Shadowsocks 客户端可以通过 [systemctl](<../zh-cn/Systemd.html> "Systemctl") 使用 `shadowsocks@.service` 或 `shadowsocks-libev@.service` 实例控制。 

要使用配置文件 `/etc/shadowsocks/_config_.json`，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `shadowsocks-libev-server@_config_.service` 或 `shadowsocks-server@_config_.service`. 

您可能也会对[在网络启动后](<../zh-cn/Systemd.html#Running_services_after_the_network_is_up> "Systemd")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]运行 `shadowsocks@` 或 `shadowsocks-libev@` 实例感兴趣。 

**提示：** 以 root 运行 `journalctl -u shadowsocks@_foo_` 来查看日志。

####  为其它程序配置代理

Shadowsocks 客户端启动后，其它程序并不会直接使用，可使用以下方法对其进行配置。 

#####  全局代理

使用 [iptables](<../zh-cn/Iptables.html> "Iptables") 等工具。 

**注意：** 使用全局代理会使所有的连接通过 Shadowsocks 服务器中转，一般不建议使用全局代理。

#####  程序设置

不少程序都能在其设置中添加代理。只需要在其设置中找到网络相关配置，添加 SOCKS5 代理，参照本地配置文件中的地址和端口填写即可（例如浏览器可参考下文 [#浏览器配置](<#%E6%B5%8F%E8%A7%88%E5%99%A8%E9%85%8D%E7%BD%AE>)）。 

#####  使用工具进行临时代理

例如 [proxychains-ng](<https://archlinux.org/packages/?name=proxychains-ng>)包 和 [tsocks](<https://archlinux.org/packages/?name=tsocks>)包. 参见 [Proxy server#Using a SOCKS proxy](<../zh-cn/Proxy_server.html#Using_a_SOCKS_proxy> "Proxy server"). 

#####  转换为 HTTP 代理

直接使用 SOCKS5 代理有时未必是用户的期望，可使用 [Privoxy](<../zh-cn/Privoxy.html> "Privoxy") 或 [Squid](<../zh-cn/Squid.html> "Squid") 等软件转换为 HTTP 代理。 

以 Privoxy 为例，编辑配置文件，添加 SOCKS5 转发： 
    
    forward-socks5 / 127.0.0.1:1080 .
    
默认监听的是本机的 8118 端口，即 `localhost:8118`，可更改为监听其他端口： 
    
    listen-address  127.0.0.1:8010
    
**提示：** 如果希望网络上其他主机也能使用该 Privoxy 配置，可以更改 `127.0.0.1` 为 `0.0.0.0` 或直接删除 `127.0.0.1`.

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `privoxy.service`. 

假设转换后的 HTTP 代理为 `127.0.0.1:8118`，则在终端中启动（以 Chromium 为例）： 
    
    $ chromium --proxy-server="http://127.0.0.1:8118"
    
#####  浏览器配置

**提示：** 浏览器直接使用 SOCKS 代理时，你可能需要使用 Privoxy 等辅助程序，因为一般浏览器会泄漏你的DNS请求，从而降低你的匿名性，参见 [#转换为 HTTP 代理](<#%E8%BD%AC%E6%8D%A2%E4%B8%BA_HTTP_%E4%BB%A3%E7%90%86>)

  * Firefox 
    * 使用如 [SwitchyOmega](<https://github.com/FelisCatus/SwitchyOmega>) 或 [FoxyProxy](<https://getfoxyproxy.org>) 等扩展。
    * 直接在 _首选项 > 常规 > 网络代理_中设置 _手动代理配置_ 或者 _自动代理配置的 URL（PAC）_ 。 
      * 使用 _手动代理配置_ ：在 _SOCKS 主机_ 栏填上 Shadowsocks 设置的本地地址和端口，点选 _SOCKS v5_ ，保存即可。
      * 使用 _自动代理配置的 URL（PAC）_ ：可使用 [genpac](<https://github.com/JinnLynn/genpac>) 工具生成。
  * Chrome/Chromium 
    * 使用 [SwitchyOmega](<https://github.com/FelisCatus/SwitchyOmega>) 等插件。

###  服务端

####  守护进程管理

[shadowsocks-libev-static](<https://aur.archlinux.org/packages/shadowsocks-libev-static/>)AUR: [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `shadowsocks-libev-server@_配置文件_.service`

[shadowsocks-rust](<https://archlinux.org/packages/?name=shadowsocks-rust>)包: [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `shadowsocks-rust-server@_配置文件_.service`

####  多端口运行

将配置文件中的 `"server_port"` 和 `"password"` 字段删去，添加 `"port_password"` 字段配置端口及其密码。 

参见 [Configure Multiple Users](<https://github.com/shadowsocks/shadowsocks/wiki/Configure-Multiple-Users>) 中的示例。 

###  性能优化

  * 使用常用端口如 `443` 等。[Great Firewall](<https://en.wikipedia.org/wiki/Great_Firewall> "wikipedia:Great Firewall") 为减轻压力，对常用端口检查相对较少。
  * [启用 TCP Fast Open](<../zh-cn/Sysctl.html#Enable_TCP_Fast_Open> "Sysctl").
  * [启用 BBR](<../zh-cn/Sysctl.html#Enable_BBR> "Sysctl").
  * 安装 [python-gevent](<https://archlinux.org/packages/?name=python-gevent>)包 提升 [shadowsocks](<https://archlinux.org/packages/?name=shadowsocks>)包 的速度。
  * 优化内核参数，参见 [Optimizing Shadowsocks](<https://github.com/shadowsocks/shadowsocks/wiki/Optimizing-Shadowsocks>).

###  加密

参见 [AEAD Ciphers](<https://shadowsocks.org/en/wiki/AEAD-Ciphers>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-23 ⓘ]. 

安装 [python-m2crypto](<https://archlinux.org/packages/?name=python-m2crypto>)包 包将会使加密更快一点。 

要使用 [Salsa20](<https://en.wikipedia.org/wiki/Salsa20> "wikipedia:Salsa20") 或 _ChaCha20_ 加密，安装 [libsodium](<https://archlinux.org/packages/?name=libsodium>)包 包。 

##  参阅

  * [shadowsocks-libev(8)](<https://man.archlinux.org/man/shadowsocks-libev.8>)
  * [Linux Kernel 4.9 中的 BBR 算法与之前的 TCP 拥塞控制相比有什么优势？](<https://www.zhihu.com/question/53559433>)
