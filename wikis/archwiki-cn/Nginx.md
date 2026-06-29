**翻译状态：**

  * 本文（或部分内容）译自 [Nginx](<https://wiki.archlinux.org/title/Nginx> "arch:Nginx")，最近一次同步于 2025-02-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nginx?diff=0&oldid=823885>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nginx_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**Nginx** (读作"engine X") 由Igor Sysoev(俄罗斯)于2005年编写，是一个免费、开源、高性能的HTTP [web服务器](</wzh/index.php?title=Web%E6%9C%8D%E5%8A%A1%E5%99%A8&action=edit&redlink=1> "Web服务器（页面不存在）")和反向代理，也可以作为一个IMAP/POP3代理服务器。Nginx因为稳定，丰富的功能集，配置简单，资源占用低而闻名世界。 

这篇文章描述了如何设置nginx并且如何通过[#FastCGI](<#FastCGI>)集成[PHP](<../zh-cn/PHP.html> "PHP"). 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")以下其中一个软件包： 

  * [nginx-mainline](<https://archlinux.org/packages/?name=nginx-mainline>)包 \- 主线分支：新功能、更新、错误修复。
  * [nginx](<https://archlinux.org/packages/?name=nginx>)包 \- 稳定分支：仅重大错误修复。
  * [angie](<https://aur.archlinux.org/packages/angie/>)AUR \- nginx 的分支和直接替代品，具有更多功能。
  * [freenginx-mainline](<https://aur.archlinux.org/packages/freenginx-mainline/>)AUR \- 保留 nginx 自由和开放开发的直接替代品（主线分支）。
  * [freenginx-libressl](<https://aur.archlinux.org/packages/freenginx-libressl/>)AUR \- 保留 nginx 自由和开放开发的直接替代品（主线分支，支持 [LibreSSL](</wzh/index.php?title=LibreSSL&action=edit&redlink=1> "LibreSSL（页面不存在）")）。
  * [freenginx](<https://aur.archlinux.org/packages/freenginx/>)AUR \- 保留 nginx 自由和开放开发的直接替代品（稳定分支）。

推荐使用主线分支。使用稳定分支的主要原因是担心新功能可能带来的不良影响，例如与第三方模块不兼容或开发者在引入[新功能](<https://nginx.org/en/download.html>)时疏忽导致的错误。 

**注意：** 所有在[official repositories](<../zh-cn/Official_repositories.html> "Official repositories")可用的模块都需要 _nginx_ （与 _nginx-mainline_ 相反）作为依赖。你可能需要在下决定选 _nginx_ 还是 _nginx-mainline_ 前，先查看下模块名单。 _nginx-mainline_ 的模块能在[Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository")找到。

对于在基于chroot环境下的额外安全性，可查阅[#在chroot环境下安装](<#%E5%9C%A8chroot%E7%8E%AF%E5%A2%83%E4%B8%8B%E5%AE%89%E8%A3%85>)。 

##  启动

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `nginx.service` 或 `angie.service`（如果你使用 Angie）。 

默认在 <http://127.0.0.1> 页面服务的页面是 `/usr/share/nginx/html/index.html`。 

##  配置

安装nginx后的第一步该干什么写在[用户手册](<https://nginx.org/en/docs/beginners_guide.html>)里了。你可以通过编辑在`/etc/nginx/`下的文件来修改配置。主配置文件在`/etc/nginx/nginx.conf`。 

更多细节和例子，你可以在[官方文档](<https://nginx.org/en/docs/>)找到。 

下面的例子包含了最常见的使用案例。我们假定你使用的是默认文件路径(`/usr/share/nginx/html`)。如果你改了路径，用你自己的路径替代。 

**提示：** DigitalOcean 提供了一个 [Nginx 配置工具](<https://www.digitalocean.com/community/tools/nginx/>)。

###  配置例子
    
    /etc/nginx/nginx.conf
    
    user http;
    worker_processes auto;
    worker_cpu_affinity auto;
    
    events {
        worker_connections 1024;
    }
    
    http {
        charset utf-8;
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        server_tokens off;
        log_not_found off;
        types_hash_max_size 4096;
        client_max_body_size 16M;
    
        # MIME
        include mime.types;
        default_type application/octet-stream;
    
        # logging
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log warn;
    
        # load configs
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }
    
###  通用配置

####  进程和连接

你应该为`worker_processes`选一个合适的值。这项设置最终决定了nginx接受多少连接和它会使用多少处理器。通常来说，把它设置成你系统里的硬件线程数就好了。可选的是，自从 1.3.8 和 1.2.5版本以后， `worker_processes` 接受 `auto` 作为值了，它会自动检测最优值 ([source](<https://nginx.org/en/docs/ngx_core_module.html#worker_processes>))。 

nginx的最大连接数有下面的公式给出`max_clients = worker_processes * worker_connections`。 

####  不同用户间的使用

默认的，[nginx](<https://archlinux.org/packages/?name=nginx>)包 用 `root` 身份运行主进程而用`http`用户运行worker进程。如果要用其它用户运行worker进程，改变`nginx.conf`里的`user`参数就好了： 
    
    /etc/nginx/nginx.conf
    
    user _user_ [_group_];
    
如果组（group）忽略不写的话，就会用和 _user_ 相同的名字来代替。 

**提示：** 其实也可以使用[systemd](<../zh-cn/Systemd.html> "Systemd")以`root`身份在没有任何东西运行的情况下运行nginx。可以看 [#使用 systemd无权限运行](<#%E4%BD%BF%E7%94%A8_systemd%E6%97%A0%E6%9D%83%E9%99%90%E8%BF%90%E8%A1%8C>) 和 [#使用 systemd 用户服务运行](<#%E4%BD%BF%E7%94%A8_systemd_%E7%94%A8%E6%88%B7%E6%9C%8D%E5%8A%A1%E8%BF%90%E8%A1%8C>)。

####  server代码块

通过使用 `server` 模块，可以实现服务多个域名。这些模块可以类比为[Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server")中的"VirtualHosts"。也可查阅[上游文献](<https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/>)。 

下面的例子，服务器监听IPv4和IPv6的80端口的进入流量的两个域名，分别是`domainname1.tld` 和`domainname2.tld`： 
    
    /etc/nginx/nginx.conf
    
    ...
    server {
        listen 80;
        listen [::]:80;
        server_name domainname1.tld;
        root /usr/share/nginx/domainname1.tld/html;
        location / {
            index index.php index.html index.htm;
        }
    }
    
    server {
        listen 80;
        listen [::]:80;
        server_name domainname2.tld;
        root /usr/share/nginx/domainname2.tld/html;
        ...
    }
    
[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")(重启) `nginx.service` 来让改变的配置生效。 

确保主机名是可以被设置好的DNS服务器比如[BIND](<../zh-cn/BIND.html> "BIND") 或者 [dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq")解析的，或者可以查看下[网络配置#Local network hostname resolution](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#Local_network_hostname_resolution> "网络配置")。 

#####  管理服务器入口

把不同的`server`模块放到不同的文件里是可能的。这样的话可以让你很轻易的开启和禁用特定的站点。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 有人认为使用 `sites-enabled` 和 `sites-available` 的方法已经不再有用，反而会带来更多问题，可以参考 [比较这两种方法](<https://serverfault.com/questions/527630/difference-in-sites-available-vs-sites-enabled-vs-conf-d-directories-nginx>) 和 [使用这种方法可能引发的问题](<https://stackoverflow.com/questions/45660042/nginx-proxy-pass-leads-to-404-not-found-page/45789055>)。 

相反，可以直接在 `/etc/nginx/conf.d/` 目录下创建文件，这种方式符合标准的配置文件放置方式。然后在主配置文件中加入 `include /etc/nginx/conf.d/*.conf`，类似于包含其他目录中的文件模式。这样，可以通过将文件重命名为 `original_name.conf.disabled` 来禁用站点，因为只有以 _.conf_ 结尾的文件才会被包含。 

（在 [Talk:Nginx](<../zh-cn/Talk:Nginx.html>) 中讨论）

如果仍然想使用 `sites-enabled` 和 `sites-available` 的方法，可以创建以下文件夹： 
    
    # mkdir /etc/nginx/sites-available
    # mkdir /etc/nginx/sites-enabled
    
在`sites-available`文件夹下创建一个文件包含一个或更多服务器模块： 
    
    /etc/nginx/sites-available/example.conf
    
    server {
        listen 443 ssl;
        listen [::]:443 ssl;
        http2 on;
    
        ...
    }
    
把` include sites-enabled/*;`放到`http` 模块的末尾： 
    
    /etc/nginx/nginx.conf
    
    http {
        ...
        include sites-enabled/*;
    }
    
如果要启用一个网站，只需要简单的创建一个符号链接： 
    
    # ln -s /etc/nginx/sites-available/example.conf /etc/nginx/sites-enabled/example.conf
    
如果要移除一个网站： 
    
    # unlink /etc/nginx/sites-enabled/example.conf
    
[Reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload")/[restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `nginx.service` 来让配置生效。 

#### TLS

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 不要仅仅把 [OpenSSL#Usage](<../zh-cn/OpenSSL.html#Usage> "OpenSSL") 的配置搬过来。（在[Talk:Nginx](<../zh-cn/Talk:Nginx.html>)讨论）

[OpenSSL](<../zh-cn/OpenSSL.html> "OpenSSL") 提供了TLS支持并且默认在Arch系统安装时安装了。 

**提示：**

  * 你可能需要在配置SSL之前阅读 [ngx_http_ssl_module](<https://nginx.org/en/docs/http/ngx_http_ssl_module.html>) 文档。
  * [Let’s Encrypt](</wzh/index.php?title=Let%E2%80%99s_Encrypt&action=edit&redlink=1> "Let’s Encrypt（页面不存在）") 是一个免费的、自动的、开放的证书颁发机构。有一个插件可以从命令行请求有效的证书并自动配置。
  * Mozilla有一篇有用的 [TLS文章](<https://wiki.mozilla.org/Security/Server_Side_TLS> "mozillawiki:Security/Server Side TLS")，也有一个[自动化工具](<https://mozilla.github.io/server-side-tls/ssl-config-generator/>)来创建一个更安全的配置。

**警告：** 如果你打算实现TLS，你必须知道一些变化和实现 [仍然被攻击时很脆弱](<https://en.wikipedia.org/wiki/Transport_Layer_Security#Attacks_against_TLS.2FSSL> "wikipedia:Transport Layer Security")[[1]](<https://weakdh.org/#affected>)。如果想知道TLS内现存的漏洞和怎样用合适的方法到nginx上，可访问 <https://weakdh.org/sysadmin.html>

创建一个私钥和自签名的证书，这对大多数不需要 [CSR](<../zh-cn/OpenSSL.html#Generate_a_certificate_signing_request> "OpenSSL")的安装来说足够了： 
    
    # mkdir /etc/nginx/ssl
    # cd /etc/nginx/ssl
    # openssl req -new -x509 -nodes -newkey rsa:4096 -keyout server.key -out server.crt -days 1095
    # chmod 400 server.key
    # chmod 444 server.crt
    
**注意：**`-days` 是可选的并且RSA键大小最低可到2048 (默认值)。

如果你需要创建一个CSR，用下面的教程而不是上面的： 
    
    # mkdir /etc/nginx/ssl
    # cd /etc/nginx/ssl
    # openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out server.key
    # chmod 400 server.key
    # openssl req -new -sha256 -key server.key -out server.csr
    # openssl x509 -req -days 1095 -in server.csr -signkey server.key -out server.crt
    
**注意：** 如果你需要更多的 _openssl_ 选项，可以阅读 [openssl(1ssl)](<https://man.archlinux.org/man/openssl.1ssl>) 或[扩展文档](<https://www.openssl.org/docs/>)。

使用TLS的 `/etc/nginx/nginx.conf` 的基本例子可以参考 [Mozilla的SSL配置生成器](<https://ssl-config.mozilla.org/#server=nginx>)。 

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `nginx.service` 来让配置生效。 

####  分用户目录

如果要复制Apache式的 `~user` URLs 到用户的 `~/public_html` 目录，可以尝试下面的。(注意：如果下面的两个规则都用了的话一定要把更清楚地PHP规则放在前面。) 
    
    /etc/nginx/nginx.conf
    
    ...
    server {
        ...
        # PHP in user directories, e.g. <http://example.com/~user/test.php>
        location ~ ^/~(.+?)(/.+\.php)$ {
            alias          /home/$1/public_html$2;
            fastcgi_pass   unix:/run/php-fpm/php-fpm.sock;
            fastcgi_index  index.php;
            include        fastcgi.conf;
        }
    
        # User directories, e.g. <http://example.com/~user/>
        location ~ ^/~(.+?)(/.*)?$ {
            alias     /home/$1/public_html$2;
            index     index.html index.htm;
            autoindex on;
        }
        ...
    }
    ...
    
查阅 [#PHP实现](<#PHP%E5%AE%9E%E7%8E%B0>)来阅读更多 `nginx`的PHP配置。 

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `nginx.service` 来启用新配置。 

### FastCGI

[FastCGI](<https://en.wikipedia.org/wiki/FastCGI> "wikipedia:FastCGI"), 也叫 FCGI, 是适用于web服务器和交互式程序的接口的协议. FastCGI 是早期的 [Common Gateway Interface](<https://en.wikipedia.org/wiki/Common_Gateway_Interface> "wikipedia:Common Gateway Interface") (CGI)的变种; FastCGI的主要目的是减少CGI程序和web服务器交互的开销,来允许服务器同时处理更多网页请求. 

FastCGI技术被引进nginx是为了与许多外部工具，比如. [Perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）"), [PHP](<../zh-cn/PHP.html> "PHP") 和 [Python](<../zh-cn/Python.html> "Python")

####  PHP实现

[PHP-FPM](<https://php-fpm.org/>) 是建议使用的用作[PHP](<../zh-cn/PHP.html> "PHP")的FastCGI服务器的解决方案. 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包 然后确保 [PHP](<../zh-cn/PHP.html> "PHP") 被安装配置正确. PHP-FPM的主要配置文件是 `/etc/php/php-fpm.conf`. 基础使用的话默认配置就足够了. 

最后, [启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `php-fpm.service`. 

你也可以使用 [php-legacy-fpm](<https://archlinux.org/packages/?name=php-legacy-fpm>)包 代替，参见 [#使用 php-legacy](<#%E4%BD%BF%E7%94%A8_php-legacy>). 

**注意：**

  * 如果你 [用不同的用户运行nginx](<#%E4%B8%8D%E5%90%8C%E7%94%A8%E6%88%B7%E9%97%B4%E7%9A%84%E4%BD%BF%E7%94%A8>), 确保PHP-FPM套接字文件能被这个用户访问，或者通过一个TCP套接字.
  * 如果你在chroot的环境下运行nginx (chroot 是 `/srv/nginx-jail`, web页面在 `/srv/nginx-jail/www`), 你必须修改文件 `/etc/php/php-fpm.conf` ，把 `chroot = /srv/nginx-jail` 和 `listen = /srv/nginx-jail/run/php-fpm/php-fpm.sock` 两行加入到指令部分 (默认是`[www]`). 如果缺少的话请为套接字文件创建目录。此外, 动态链接到依赖的模块，你需要将这些依赖复制到(比如. 对于php-imagick, 你需要复制ImageMagic的库复制到chroot, 而不是imagick.so他自己).

#####  nginx 配置

当服务一个PHP web程序时，一个PHP-FPM的`location`应该包括在 [#server代码块](<#server%E4%BB%A3%E7%A0%81%E5%9D%97>)里 [[2]](<https://www.nginx.com/resources/wiki/start/topics/examples/phpfcgi/>),比如.: 
    
    /etc/nginx/sites-available/example.conf
    
    server {
        root /usr/share/nginx/html;
    
        location / {
            index index.html index.htm index.php;
        }
    
        location ~ \.php$ {
            # 404
            try_files $fastcgi_script_name =404;
    
            # default fastcgi_params
            include fastcgi_params;
    
            # fastcgi settings
            fastcgi_pass			unix:/run/php-fpm/php-fpm.sock;
            fastcgi_index			index.php;
            fastcgi_buffers			8 16k;
            fastcgi_buffer_size		32k;
    
            # fastcgi params
            fastcgi_param DOCUMENT_ROOT	$realpath_root;
            fastcgi_param SCRIPT_FILENAME	$realpath_root$fastcgi_script_name;
            #fastcgi_param PHP_ADMIN_VALUE	"open_basedir=$base/:/usr/lib/php/:/tmp/";
        }
    }

如果需要用PHP处理其他文件扩展名 (比如. _.html_ and _.htm_): 
    
    location ~ [^/]\.(php|html|htm)(/|$) {
        ...
    }
    
非 _.php_ 的PHP-FPM扩展处理都需要被直接加入到 `/etc/php/php-fpm.d/www.conf`: 
    
    security.limit_extensions = .php .html .htm
    
**注意：** 需要注意下 `fastcgi_pass` 参数, 因为它被选定的FastCGI服务器在它的配置文件里定义TCP或Unix套接字. 对应`php-fpm`的**default** (Unix) 套接字是 是: 
    
    fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
    
你可能想要使用常见的 TCP 套接字, **not default** , 
    
    fastcgi_pass 127.0.0.1:9000;
    
Unix 的域名套接字应该会快一点.

**提示：** 如果你使用多个 `server` 块来启用PHP支持, 创建一个 `php_fastcgi.conf` 配置文件可能更简单: 
    
    /etc/nginx/php_fastcgi.conf
    
    location ~ \.php$ {
        # 404
        try_files $fastcgi_script_name =404;
        # default fastcgi_params
        include fastcgi_params;
        # fastcgi settings
        ...
    }

为特定的服务器启用PHP支持, 只需要简单的加入 `include php.conf`就好了: 
    
    /etc/nginx/sites-available/example.conf
    
    server {
        server_name example.com;
        ...
    
        include /etc/nginx/php_fastcgi.conf;
    }
    
#####  测试配置

你需要[restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `php-fpm.service` 和 `nginx.service` 服务单元来让配置生效，如果配置之前被改变过的话. 

测试FastCGI实现, 在`root`目录下创建一个新的PHP文件，内容是: 
    
    <?php phpinfo(); ?>
    
把这个文件用浏览器打开，你应该就可以看到现在的PHP配置的信息页了. 

####  CGI 实现

这个实现是CGI程序所需要的. 

##### fcgiwrap

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [fcgiwrap](<https://archlinux.org/packages/?name=fcgiwrap>)包. 配置文件是 `/usr/lib/systemd/system/fcgiwrap.socket`. [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并且[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `fcgiwrap.socket`. 

######  多个工人线程

如果你想生成多个工人线程建议你使用[multiwatch](<https://aur.archlinux.org/packages/multiwatch/>)AUR, 它会处理崩溃的子进程. 如果你需要使用`spawn-fcgi` 来创建Unix套接字,因为multiwatch无法处理systemd创建的套接字，尽管fcgiwarp它自己在单元文件中直接调用页没有任何问题. 

[覆盖](<../zh-cn/Systemd.html#%E6%9B%BF%E6%8D%A2%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "覆盖单元文件") `fcgiwrap.service` (和`fcgiwrap.socket` 单元, 如果存在的话), 修改`ExecStart`行到满足你需要的地方. 下面是使用[multiwatch](<https://aur.archlinux.org/packages/multiwatch/>)AUR的单元文件. 确保`fcgiwrap.socket` 没有被start（开始）或enable（启用）, 因为他会和这些单元冲突: 
    
    /etc/systemd/system/fcgiwrap.service
    
    [Unit]
    Description=Simple CGI Server
    After=nss-user-lookup.target
    
    [Service]
    ExecStartPre=/bin/rm -f /run/fcgiwrap.socket
    ExecStart=/usr/bin/spawn-fcgi -u http -g http -s /run/fcgiwrap.sock -n -- /usr/bin/multiwatch -f 10 -- /usr/sbin/fcgiwrap
    ExecStartPost=/usr/bin/chmod 660 /run/fcgiwrap.sock
    PrivateTmp=true
    Restart=on-failure
    
    [Install]
    WantedBy=multi-user.target

可以自定义 `-f 10` 来改变生成的子进程的数量. 

**警告：**`ExecStartPost`行是需要的，因为当为`spawn-fcgi`使用`-M 660`参数选项时会出现奇怪的情况.这有可能是一个Bug

#####  nginx配置

在每个服务了一个CGI程序的`server` 块内都应该有一个像下面的 `location` 块: 
    
    location ~ \.cgi$ {
         root           /path/to/server/cgi-bin;
         fastcgi_pass   unix:/run/fcgiwrap.sock;
         include        fastcgi.conf;
    }
    
    fcgiwrap 的默认套接字文件是 /run/fcgiwrap.sock.
    
**警告：** 如果使用了 SCRIPT_NAME 和 DOCUMENT_ROOT，fcgiwrap 会 _丢弃_ nginx 中设置的其他 fastcgi_params。你必须使用 SCRIPT_FILENAME 才能通过 Nginx 配置设置其他参数（如 PATH_INFO）。参见 [这个](<https://github.com/gnosek/fcgiwrap/issues/3>) GitHub 问题。

如果你一直出现 `502 - bad Gateway` 错误,你应该检查你的CGI程序是否宣告了下面内容的mime类型。如果是html，他应该是`Content-type: text/html`. 

如果你遇到 403 错误，请确保 CGI 可执行文件对 `http` 用户可读且可执行，并且每个父文件夹对 `http` 用户可读。 

##  在chroot环境下安装

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 本节内容来自2013年。自那时起，systemd已被引入，可以更高效且无需太多麻烦地替代此方法。（在 [Talk:Nginx](<../zh-cn/Talk:Nginx.html>) 中讨论）

在[chroot](<../zh-cn/Chroot.html> "Chroot")环境里运行nginx是有一个额外的安全层的。为了最大化安全性，chroot环境应该只包括nginx服务器需要的文件，并且所有的文件都应该尽可能有严格的权限，比如像`/usr/bin`这样的文件夹应该不可读和不可写。 

Arch默认有一个`http`用户和组来运行服务器，chroot将会在`/srv/http`。 

创建这个监狱（指chroot环境）的PERL脚本能在[jail.pl gist](<https://gist.github.com/4365696>)找到。你可以直接用那个脚本或者跟着这篇文章的指示继续阅读下去。它应该用root运行。你需要在它起作用之前取消一行注释。 

###  创建必要的设备

nginx需要 `/dev/null`, `/dev/random`, 和 `/dev/urandom`. 为了在chroot环境中安装这些设备，需要创建 `/dev/` 目录并使用 _mknod_ 添加设备。尽量避免挂载整个`/dev/`目录，以确保即使chroot被攻破，攻击者也必须突破chroot才能访问像`/dev/sda1`这样的重要设备。 

**提示：**

  * 确保 `/srv/http` 挂载时没有使用nodev选项
  * 查看 [mknod(1)](<https://man.archlinux.org/man/mknod.1>) 和 `ls -l /dev/{null,random,urandom}` 来更好地理解 _mknod_ 选项。

    # export JAIL=/srv/http
    # mkdir $JAIL/dev
    # mknod -m 0666 $JAIL/dev/null c 1 3
    # mknod -m 0666 $JAIL/dev/random c 1 8
    # mknod -m 0444 $JAIL/dev/urandom c 1 9
    
###  创建必要目录

nginx需要大量文件来运转正常。在把它们拷贝过去之前创建一个文件夹来存储它们。假设你的nginx文档目录在 `/srv/http/www`。 
    
    # mkdir -p $JAIL/etc/nginx/logs
    # mkdir -p $JAIL/usr/{lib,bin}
    # mkdir -p $JAIL/usr/share/nginx
    # mkdir -p $JAIL/var/{log,lib}/nginx
    # mkdir -p $JAIL/www/cgi-bin
    # mkdir -p $JAIL/{run,tmp}
    # cd $JAIL; ln -s usr/lib lib
    # cd $JAIL; ln -s usr/lib lib64
    # cd $JAIL/usr; ln -s lib lib64
    
然后挂载 `$JAIL/tmp` 和 `$JAIL/run` 作为tmpfs。大小应该限制确保攻击者无法吃掉所有的内存。 
    
    # mount -t tmpfs none $JAIL/run -o 'noexec,size=1M'
    # mount -t tmpfs none $JAIL/tmp -o 'noexec,size=100M'
    
为了在重启后保留挂载，下面的入口应该被添加到`/etc/fstab`: 
    
    /etc/fstab
    
    tmpfs   /srv/http/run   tmpfs   rw,noexec,relatime,size=1024k   0       0
    tmpfs   /srv/http/tmp   tmpfs   rw,noexec,relatime,size=102400k 0       0

###  填充chroot

首先复制简单的文件。 
    
    # cp -r /usr/share/nginx/* $JAIL/usr/share/nginx
    # cp -r /usr/share/nginx/html/* $JAIL/www
    # cp /usr/bin/nginx $JAIL/usr/bin/
    # cp -r /var/lib/nginx $JAIL/var/lib/nginx
    
然后复制必要的库。使用 _ldd_ 来列出它们并将它们复制到正确的位置。复制优于硬链接，以确保即使攻击者获得文件的写权限，也无法破坏或修改真实的系统文件。 
    
    $ ldd /usr/bin/nginx
    
    linux-vdso.so.1 (0x00007fffc41fe000)
    libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f57ec3e8000)
    libcrypt.so.1 => /usr/lib/libcrypt.so.1 (0x00007f57ec1b1000)
    libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x00007f57ebead000)
    libm.so.6 => /usr/lib/libm.so.6 (0x00007f57ebbaf000)
    libpcre.so.1 => /usr/lib/libpcre.so.1 (0x00007f57eb94c000)
    libssl.so.1.0.0 => /usr/lib/libssl.so.1.0.0 (0x00007f57eb6e0000)
    libcrypto.so.1.0.0 => /usr/lib/libcrypto.so.1.0.0 (0x00007f57eb2d6000)
    libdl.so.2 => /usr/lib/libdl.so.2 (0x00007f57eb0d2000)
    libz.so.1 => /usr/lib/libz.so.1 (0x00007f57eaebc000)
    libGeoIP.so.1 => /usr/lib/libGeoIP.so.1 (0x00007f57eac8d000)
    libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f57eaa77000)
    libc.so.6 => /usr/lib/libc.so.6 (0x00007f57ea6ca000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f57ec604000)

对于 `/usr/lib` 中的文件，你可以使用以下命令： 
    
    # cp $(ldd /usr/bin/nginx | grep /usr/lib/ | sed -sre 's/(.+)(\/usr\/lib\/\S+).+/\2/g') $JAIL/usr/lib
    
使用以下命令复制 `ld-linux-x86-64.so`： 
    
    # cp /lib64/ld-linux-x86-64.so.2 $JAIL/lib
    
**注意：** 不要尝试复制 `linux-vdso.so`：它不是真实存在的库，不在 `/usr/lib` 文件夹中。

复制一些复杂但必要的库和系统文件。 
    
    # cp /usr/lib/libnss_* $JAIL/usr/lib
    # cp -rfvL /etc/{services,localtime,nsswitch.conf,nscd.conf,protocols,hosts,ld.so.cache,ld.so.conf,resolv.conf,host.conf,nginx} $JAIL/etc
    
为chroot创建严格的用户/组文件。这样只有chroot正常工作所需的用户才会被chroot知道，其他用户/组不会泄露给攻击者，即使他们已经获取了chroot权限。 
    
    $JAIL/etc/group
    
    http:x:33:
    nobody:x:99:
    
    $JAIL/etc/passwd
    
    http:x:33:33:http:/:/bin/false
    nobody:x:99:99:nobody:/:/bin/false
    
    $JAIL/etc/shadow
    
    http:x:14871::::::
    nobody:x:14871::::::
    
    $JAIL/etc/gshadow
    
    http:::
    nobody:::
    
    # touch $JAIL/etc/shells
    # touch $JAIL/run/nginx.pid
    
最后，设置非常严格的权限。尽可能多的文件应归root所有并设置为不可写。 
    
    # chown -R root:root $JAIL/
    
    # chown -R http:http $JAIL/www
    # chown -R http:http $JAIL/etc/nginx
    # chown -R http:http $JAIL/var/{log,lib}/nginx
    # chown http:http $JAIL/run/nginx.pid
    
    # find $JAIL/ -gid 0 -uid 0 -type d -print | xargs chmod -rw
    # find $JAIL/ -gid 0 -uid 0 -type d -print | xargs chmod +x
    # find $JAIL/etc -gid 0 -uid 0 -type f -print | xargs chmod -x
    # find $JAIL/usr/bin -type f -print | xargs chmod ug+rx
    # find $JAIL/ -group http -user http -print | xargs chmod o-rwx
    # chmod +rw $JAIL/tmp
    # chmod +rw $JAIL/run
    
如果你的端口绑定为80（或其他在[1-1023]范围内的端口），给chroot无需root即可绑定的权限。 
    
    # setcap 'cap_net_bind_service=+ep' $JAIL/usr/bin/nginx
    
###  修改nginx.service来开启chroot

[覆盖单元文件](<../zh-cn/Systemd.html#%E6%9B%BF%E6%8D%A2%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "覆盖单元文件") `nginx.service`。升级nginx不会修改你自定义的 _.service_ 文件。 

systemd单元必须在开启chroot里的nginx之前修改，以http用户的身份，将pid文件放到chroot里。 

**注意：** 我不确定pid文件是否需要被放到chroot里.
    
    /etc/systemd/system/nginx.service
    
    [Unit]
    Description=A high performance web server and a reverse proxy server
    After=network.target
    
    [Service]
    Type=forking
    PIDFile=/srv/http/run/nginx.pid
    ExecStartPre=/usr/bin/chroot --userspec=http:http /srv/http /usr/bin/nginx -t -q -g 'pid /run/nginx.pid; daemon on; master_process on;'
    ExecStart=/usr/bin/chroot --userspec=http:http /srv/http /usr/bin/nginx -g 'pid /run/nginx.pid; daemon on; master_process on;'
    ExecReload=/usr/bin/chroot --userspec=http:http /srv/http /usr/bin/nginx -g 'pid /run/nginx.pid; daemon on; master_process on;' -s reload
    ExecStop=/usr/bin/chroot --userspec=http:http /srv/http /usr/bin/nginx -g 'pid /run/nginx.pid;' -s quit
    
    [Install]
    WantedBy=multi-user.target

**注意：** 用pacman升级nginx并不会升级chroot里的nginx。如果你要升级的话可能需要手动重复上面的步骤。不要忘记更新它链接的库.

你现在可以安全的写在非chroot环境下的nginx安装. 
    
    # pacman -Rsc nginx
    
如果你不移除非chroot环境的nginx安装，你可能想要确认运行的nginx是不是chroot环境里的, 你可以查询 `/proc/_PID_ /root` 链接到哪里. 如果链接到 `/srv/http` 而不是`/`那运行的就是chroot环境下的nginx. 
    
    # ps -C nginx | awk '{print $1}' | sed 1d | while read -r PID; do ls -l /proc/$PID/root; done
    
##  建议和技巧

###  使用 systemd 以非特权用户身份运行

使用 [drop-in unit file](</wzh/index.php?title=Drop-in_unit_file&action=edit&redlink=1> "Drop-in unit file（页面不存在）") 为 `nginx.service` 设置 `User` 和可选的 `Group` 选项，放在 `[Service]` 下： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    User=_user_
    Group=_group_

我们可以通过以下方式加固服务，防止其提升权限： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    NoNewPrivileges=yes

**提示：** 更多限制选项请参阅 [systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>)。

然后我们需要确保 `_user_` 拥有访问所需资源的权限。按照以下子章节进行配置，然后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") nginx。 

**提示：** 相同的设置可能也适用于你的 [FastCGI 服务器](<#FastCGI>)。

####  端口

默认情况下，Linux 不允许非 `root` 进程绑定到 1024 以下的端口。可以使用 1024 以上的端口： 
    
    /etc/nginx/nginx.conf
    
    server {
            listen 8080;
    }
    
**提示：** 如果你希望 nginx 在端口 80 或 443 上可访问，可以配置你的 [防火墙](</wzh/index.php?title=Firewall&action=edit&redlink=1> "Firewall（页面不存在）") 将请求从 80 或 443 重定向到 nginx 监听的端口。

或者你可以授予 nginx 进程 CAP_NET_BIND_SERVICE 能力，使其能够绑定到 1024 以下的端口： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    CapabilityBoundingSet=
    CapabilityBoundingSet=CAP_NET_BIND_SERVICE
    AmbientCapabilities=
    AmbientCapabilities=CAP_NET_BIND_SERVICE

另外，你可以使用 systemd 套接字激活。在这种情况下，systemd 将监听端口，并在建立连接时启动 nginx，并将套接字作为文件描述符传递。这意味着 nginx 不需要特殊权限，因为套接字在启动时已经存在。这依赖于 nginx 用于传递套接字的内部环境变量 [[3]](<https://trac.nginx.org/nginx/ticket/237>)，因此不受官方支持。与其设置 `CapabilityBoundingSet` 和 `AmbientCapabilities`，不如编辑服务覆盖文件，设置 `NGINX` 环境变量，告诉 nginx 套接字将作为哪些文件描述符传递： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    Environment=NGINX=3:4;

每个监听端口将有一个套接字，从文件描述符 3 开始，因此在此示例中，我们告诉 nginx 期望两个套接字。现在创建一个 `nginx.socket` 单元，指定要监听的端口： 
    
    /etc/systemd/system/nginx.socket
    
    [Socket]
    ListenStream=0.0.0.0:80
    ListenStream=0.0.0.0:443
    After=network.target
    Requires=network.target
    
    [Install]
    WantedBy=sockets.target

套接字将按照此单元中定义的顺序传递，因此端口 80 将是文件描述符 3，端口 443 将是文件描述符 4。如果你之前启用或启动了服务，现在应该[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop")它，并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `nginx.socket`。当系统启动时，nginx 将不会运行，但在你通过浏览器访问网站时启动。通过这种方式，你可以进一步加固服务；例如，在许多情况下，你现在可以在服务文件中设置 `PrivateNetwork=True`，阻止 nginx 访问外部网络，因为 systemd 创建的套接字足以通过它提供网站服务。请注意，这将在 nginx 服务的日志中打印一条警告：`2020/08/29 19:33:20 [notice] 254#254: using inherited sockets from "3:4;"`

####  PID 文件

[nginx](<https://archlinux.org/packages/?name=nginx>)包 默认编译为使用 `/run/nginx.pid`，而 _user_ 无法写入该文件。我们可以创建一个 _user_ 可以写入的目录，并将 PID 文件放在那里。例如，可以使用 `RuntimeDirectory` ([systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>))。 

[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `nginx.service` 以配置 PID 文件： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    RuntimeDirectory=nginx
    PIDFile=/run/nginx/nginx.pid
    ExecStart=
    ExecStart=/usr/bin/nginx -g 'pid /run/nginx/nginx.pid; error_log stderr;' 
    ExecReload=
    ExecReload=/usr/bin/nginx -s reload -g 'pid /run/nginx/nginx.pid; error_log stderr;'

####  /var/lib/nginx

[nginx](<https://archlinux.org/packages/?name=nginx>)包 默认编译为将临时文件存储在 `/var/lib/nginx` 中。 

**提示：** 通过运行 `$ nginx -V` 查看所有编译时选项。

你可以通过例如使用 `StateDirectory` ([systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>)) 来授予 _user_ 对该目录的写权限： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    StateDirectory=nginx

####  /var/log/nginx

[nginx](<https://archlinux.org/packages/?name=nginx>)包 默认编译为将访问日志存储在 `/var/log/nginx` 中。 

你可以通过例如使用 `LogsDirectory` ([systemd.exec(5)](<https://man.archlinux.org/man/systemd.exec.5>)) 来授予 _user_ 对该目录的写权限： 
    
    /etc/systemd/system/nginx.service.d/user.conf
    
    [Service]
    ...
    LogsDirectory=nginx

###  使用 systemd 运行用户服务

如果你想运行一个完全由非特权用户控制和配置的服务器实例，请考虑使用 [nginx-user-service](<https://aur.archlinux.org/packages/nginx-user-service/>)AUR。 

###  针对systemd的可选脚本

在纯systemd的情况下，你可以享受chroot + systemd的好处。 [[4]](<http://0pointer.de/blog/projects/changing-roots.html>) 基于设置[用户组](<https://nginx.org/en/docs/ngx_core_module.html#user>)和 pid： 
    
    /etc/nginx/nginx.conf
    
    user http;
    pid /run/nginx.pid;

文件的绝对路径是`/srv/http/etc/nginx/nginx.conf`。 
    
    /etc/systemd/system/nginx.service
    
    [Unit]
    Description=nginx (Chroot)
    After=network.target
    
    [Service]
    Type=forking
    PIDFile=/srv/http/run/nginx.pid
    RootDirectory=/srv/http
    ExecStartPre=/usr/bin/nginx -t -c /etc/nginx/nginx.conf
    ExecStart=/usr/bin/nginx -c /etc/nginx/nginx.conf
    ExecReload=/usr/bin/nginx -c /etc/nginx/nginx.conf -s reload
    ExecStop=/usr/bin/nginx -c /etc/nginx/nginx.conf -s stop
    
    [Install]
    WantedBy=multi-user.target

没必要设置默认路径，nginx默认加载` -c /etc/nginx/nginx.conf`，但这仍然是一个好主意。 

作为可选项，你可以在chroot环境下**仅仅** 运行 `ExecStart`，`RootDirectoryStartOnly`参数要设置为`yes`（参见 [systemd.service(5)](<https://man.archlinux.org/man/systemd.service.5>)），或者在挂载点生效前启用它，或者使用一个 [systemd路径](<https://www.freedesktop.org/software/systemd/man/systemd.path.html>)。 
    
    /etc/systemd/system/nginx.path
    
    [Unit]
    Description=nginx (Chroot) path
    [Path]
    PathExists=/srv/http/site/Public_html
    [Install]
    WantedBy=default.target

[Enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")（启用）创建的`nginx.path` 然后把 `/etc/systemd/system/nginx.service`里的`WantedBy=default.target` 变成 `WantedBy=nginx.path`。 

单元文件里的`PID文件`允许systemd监控进程（需要绝对路径）。如果这不是你想要的，你可以改变默认的“一击”类型，然后删除单元文件里的参照。 

###  Nginx Beautifier （nginx美化器）

[nginxbeautifier](<https://aur.archlinux.org/packages/nginxbeautifier/>)AUR 是一个命令行工具，用来美化和格式化nginx配置文件。 

###  更好的头文件管理

Nginx 有一个非常不直观的头文件管理系统，头文件只能在一个上下文中定义，任何其它的头文件都会被忽略。为了补救这个问题，我们可以安装 [headers-more-nginx](<https://github.com/openresty/headers-more-nginx-module#more_set_headers>) 模块。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nginx-mod-headers-more](<https://archlinux.org/packages/?name=nginx-mod-headers-more>)包 包。这样会把模块安装到 `/usr/lib/nginx/modules` 目录下。 

如果要加载模块，把下面这行加入到你的 nginx 配置文件的第一行。 
    
    /etc/nginx/nginx.conf
    
    load_module "/usr/lib/nginx/modules/ngx_http_headers_more_filter_module.so";
    ...

###  基本认证

基本认证需要创建一个密码文件。密码文件可以使用 [apache](<https://archlinux.org/packages/?name=apache>)包 包提供的 `htpasswd` 程序进行管理，或者使用 [nginx_passwd](<https://aur.archlinux.org/packages/nginx_passwd/>)AUR 提供的 `nginx-passwd` 进行管理 - 详细信息可在 [GitHub 源码](<https://github.com/gene-git/nginx_passwd>)上找到。 

###  使用 php-legacy

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [php-legacy-fpm](<https://archlinux.org/packages/?name=php-legacy-fpm>)包 而不是 [php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包，并确保 [PHP](<../zh-cn/PHP.html> "PHP") 已正确安装和配置。 

PHP-LEGACY-FPM 的主配置文件是 `/etc/php-legacy/php-fpm.conf`。对于基本使用，默认配置应该足够。 

`fastcgi_pass` 参数的 Unix 套接字也需要调整，通常为： 
    
    fastcgi_pass unix:/run/php-fpm-legacy/php-fpm.sock;
    
然后[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `php-legacy-fpm.service`。 

##  故障排除

###  配置验证
    
    # nginx -t
    
     nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
     nginx: configuration file /etc/nginx/nginx.conf test is successful
    
###  Error: The page you are looking for is temporarily unavailable. Please try again later. (502 Bad Gateway)

这是因为FastCGI服务器还没有开启，或者套接字有错误的权限。 

试一试[这个回答](<https://stackoverflow.com/questions/4252368/nginx-502-bad-gateway/16497957#16497957>)来解决502问题。 

在Arch Linux，上面提到的配置文件在 `/etc/php/php-fpm.conf`。 

### Error: No input file specified

1\. 确定`/etc/php/php.ini`里的 `open_basedir`变量包含正确的路径，要和 `nginx.conf` (通常在`/usr/share/nginx/`)里的`root`变量一致. 当使用[PHP-FPM](<https://php-fpm.org/>) 作为PHP的FastCGI服务器时, 你可以添加 `fastcgi_param PHP_ADMIN_VALUE "open_basedir=$document_root/:/tmp/:/proc/";` 到`nginx.conf`里的 `location` 代码块里，它能处理PHP文件. 

2\. 另一种情况是, `nginx.conf`文件里，`location ~ \.php$`代码块里的错误的 `root` 变量. 确保`root` 指向相同服务器里的`location /`的同样的目录. 或者你直接把root设为全局，不要把它定义到任何地方 

3\. 检查权限: 比如. `http` 是用户/组, `755` 是目录权限，`644` 是文件权限. 记住，到`html`目录的路径目录也必须有相同的权限. 可以查看 [File permissions and attributes#Bulk chmod](<../zh-cn/File_permissions_and_attributes.html#Bulk_chmod> "File permissions and attributes") 来批量修改大量文件夹的权限. 

4\. 你没有让 `SCRIPT_FILENAME` 包含你脚本的全部路径. 如果nginx的配置 (`fastcgi_param SCRIPT_FILENAME`) 是对的的话, 这种错误意味着PHP无法加载请求的脚本. 通常它知识简单的权限问题, 你可以用root运行php-cgi: 
    
    # spawn-fcgi -a 127.0.0.1 -p 9000 -f /usr/bin/php-cgi
    
或者你应该创建一个组和用户来开启php-cgi: 
    
    # groupadd www
    # useradd -g www www
    # chmod +w /srv/www/nginx/html
    # chown -R www:www /srv/www/nginx/html
    # spawn-fcgi -a 127.0.0.1 -p 9000 -u www -g www -f /usr/bin/php-cgi
    
5\. 如果你是在chroot的环境下的nginx运行php-fpm，确保`/etc/php-fpm/php-fpm.d/www.conf`里的`chroot` 设置正确(或者 `/etc/php-fpm/php-fpm.conf` 如果是旧版本的话) 

### Warning: Could not build optimal types_hash

当开启 `nginx.service`, 进程可能会有下面的日志信息: 
    
    [warn] 18872#18872: could not build optimal types_hash, you should increase either types_hash_max_size: 1024 or types_hash_bucket_size: 64; ignoring types_hash_bucket_size
    
解决这个警告, 提升`http`代码块的下面的键的值 [[5]](<https://nginx.org/en/docs/http/ngx_http_core_module.html#types_hash_max_size>) [[6]](<https://nginx.org/en/docs/http/server_names.html>): 
    
    /etc/nginx/nginx.conf
    
    http {
        types_hash_max_size 4096;
        server_names_hash_bucket_size 128;
        ...
    }
    
###  不能指定请求地址

来自`nginx.service` [单元状态](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "单元状态")的全部错误是 
    
    [emerg] 460#460: bind() to A.B.C.D:443 failed (99: Cannot assign requested address)
    
尽管，你的 nginx 单元文件配置为在 `network.target` 之后运行，nginx 可能仍然会尝试监听一个已配置但尚未添加到任何接口的地址。通过手动 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") （启动）nginx 来验证这种情况（从而确保 IP 地址配置正确）。配置 nginx 监听任何地址都会解决这个问题。如果你的使用场景需要监听特定地址，一个可能的解决方案是重新配置 systemd。 

在所有配置的网络设备启动并分配 IP 地址后启动 nginx，在 `nginx.service` 中将 `network-online.target` 附加到 `After=`，然后 [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `systemd-networkd-wait-online.service`。 

##  参见

  * [WebDAV with nginx](<../zh-cn/WebDAV.html#nginx> "WebDAV")
  * [nginx configuration pitfalls](<https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/>)
  * [Very good in-depth 2014 look at nginx security and Reverse Proxying](<https://calomel.org/nginx.html>)
  * [Installing LEMP (nginx, PHP, MySQL with MariaDB engine and PhpMyAdmin) in Arch Linux](<https://www.tecmint.com/install-nginx-php-mysql-with-mariadb-engine-and-phpmyadmin-in-arch-linux/>)
  * [Using SSL certificates generated with Let's Encrypt](</wzh/index.php?title=Let%E2%80%99s_Encrypt&action=edit&redlink=1> "Let’s Encrypt（页面不存在）")
