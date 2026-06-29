**翻译状态：**

  * 本文（或部分内容）译自 [lighttpd](<https://wiki.archlinux.org/title/lighttpd> "arch:lighttpd")，最近一次同步于 2022-12-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/lighttpd?diff=0&oldid=753629>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/lighttpd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[lighttpd](<https://www.lighttpd.net/>)是一个安全，快速，标准，且非常灵活的[网页服务器](<https://en.wikipedia.org/wiki/Web_server> "wikipedia:Web server")，并对高性能环境做了最佳化。相较于其他网页服务器,它占用的内存很少，且注重CPU负载量。它的进阶功能集 （[FastCGI](<https://en.wikipedia.org/wiki/FastCGI> "wikipedia:FastCGI")，[CGI](<https://en.wikipedia.org/wiki/Common_Gateway_Interface> "wikipedia:Common Gateway Interface")，验证，输出压缩，网址重定向等等）让Lighttpd成为每个试图摆脱瓶颈的服务器的完美网页服务器软件。 

##  安装

Lighttpd可以从[extra]仓库获得: 
    
    # pacman -S lighttpd
    
##  设置

###  基本设置

lighttpd配置文件： `/etc/lighttpd/lighttpd.conf`。在安装完成后它会自动生成一个用于测试的测试页面。 

想要检查 `lighttpd.conf` 中的语法错误，可以使用以下命令来快速查找错误： 
    
    $ lighttpd -t -f /etc/lighttpd/lighttpd.conf
    
预设配置文件会把 `/srv/http/` 指定为提供HTTP服务的文件目录。 

测试安装结果： 
    
    # chmod 755 /srv/http/index.html
    # echo 'TestMe!' >> /srv/http/index.html
    
修改日志目录权限: 
    
    # chown -R http:http /var/log/lighttpd
    
启动服务: 
    
    # systemctl start lighttpd
    
然后就可以使用浏览器打开网址 `localhost` ，你应该能见到测试页面。 

开机自动启动: 
    
    # systemctl enable lighttpd
    
示例配置文件在 `/usr/share/doc/lighttpd/`。 

####  基本日志

lighttpd 能够输出错误与访问记录到日志文件中。错误日志默认启用(`server.errorlog` 选项). 如下编辑`/etc/lighttpd/lighttpd.conf`启用访问日志： 
    
    server.modules += (
       "mod_accesslog",
    )
    
    accesslog.filename = "/var/log/lighttpd/access.log"
    
####  通过SSL启动HTTPS

**警告：** 计划独立实现SSL/TLS的用户应当注意，SSL/TLS的一些变种和实现难以抵抗攻击。参阅[OpenSSL](<../zh-cn/OpenSSL.html> "OpenSSL")

**提示：**

  * Mozilla 有一个能用于lighttpd的SSL [配置生成器](<https://ssl-config.mozilla.org/#server=lighttpd>)。
  * 设置SSL后, 你可以用 Qualys SSL Labs' [SSL服务器检验](<https://www.ssllabs.com/ssltest/index.html>)来检查你的配置

#####  自签名证书

安装[openssl](<https://archlinux.org/packages/?name=openssl>)包后，自签名SSL证书用以下方式生成： 
    
    # mkdir /etc/lighttpd/certs
    # openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -sha256 -keyout /etc/lighttpd/certs/server.pem -out /etc/lighttpd/certs/server.pem
    # chmod 600 /etc/lighttpd/certs/server.pem
    
修改`/etc/lighttpd/lighttpd.conf`，增加以下内容来启用HTTPS。 
    
    server.modules += ( "mod_openssl" )
    
    $SERVER["socket"] == ":443" {
        ssl.engine                  = "enable" 
        ssl.pemfile                 = "/etc/lighttpd/certs/server.pem" 
     }
    
详情请参阅 [lighttpd TLS 配置](<https://redmine.lighttpd.net/projects/lighttpd/wiki/Docs_SSL>)。 

#####  Let's Encrypt

你也可以生成被[Let's Encrypt](</wzh/index.php?title=Let%27s_Encrypt&action=edit&redlink=1> "Let's Encrypt（页面不存在）")签名的证书。 

在`/etc/lighttpd/lighttpd.conf`增加： 
    
    $SERVER["socket"] == ":443" {
        ssl.engine                  = "enable" 
        ssl.privkey                 = "/etc/letsencrypt/live/_domain_ /privkey.pem"
        ssl.pemfile                 = "/etc/letsencrypt/live/_domain_ /fullchain.pem"
    }
    
详情请参阅 lighttpd 文档中的[启用 Let's Encrypt](<https://redmine.lighttpd.net/projects/lighttpd/wiki/HowToSimpleSSL>)。 

####  重定向HTTP请求到HTTPS

你需要在`/etc/lighttpd/lighttpd.conf`中的server.modules数组中增加`"mod_redirect"`: 
    
    server.modules += ( "mod_redirect" )
    
    $SERVER["socket"] == ":80" {
      $HTTP["host"] == "example.org" {
        url.redirect = ( "^/(.*)" => "https://example.org/$1" )
        server.name                 = "example.org" 
      }
    }
    
    $SERVER["socket"] == ":443" {
      ssl.engine = "enable" 
      ssl.pemfile = "/etc/lighttpd/certs/server.pem" 
      server.document-root = "..." 
    }
    
为了重定向所有网络主机到它们的HTTPS安全访问方式，用以下内容取代之前的socket 80端口配置： 
    
    $SERVER["socket"] == ":80" {
      $HTTP["host"] =~ ".*" {
        url.redirect = (".*" => "https://%0$0")
      }
    }
    
如仅需重定向所有网络主机的一部分 (例如，“secure” or ”phpmyadmin“): 
    
    $SERVER["socket"] == ":80" {
      $HTTP["url"] =~ "^/secure" {
        url.redirect = ( "^/(.*)" => "https://example.com/$1" )
      }
    }
    
####  用密码保护目录

注意：此模块需要[mariadb-libs](<https://archlinux.org/packages/?name=mariadb-libs>)包。一个近似于系统的`/etc/passwd`的密码文件需要被用于用户的认证。安装需要特定的格式和经md5sum散列的密码，但用户可以用下列命令轻松创建： 
    
    $ user=foo
    $ password=b@R102
    $ realm='Password Required'
    $ hash=`echo -n "$user:$realm:$password" | md5sum | cut -b -32`
    
    # echo "$user:$realm:$hash" >> /etc/lighttpd/lighttpd.user
    
修改`/etc/lighttpd/lighttpd.conf`，增加下列内容以启用目录保护: 
    
    server.modules += ( "mod_auth", "mod_authn_file" )
    
    auth.backend                = "htdigest"
    auth.backend.htdigest.userfile = "/etc/lighttpd/lighttpd.user"
    
    # 注意：这里的路径是相对于server.document-root变量的
    auth.require = ( "/secret" =>
       (
        "method" => "basic",
        "realm" => "Password Required",
        "require" => "valid-user"
       )
    )
    
**注意：** 写入`/etc/lighttpd/lighttpd.conf`的”user“和”realm“项必须与`/etc/lighttpd/lighttpd.user`中相符，以使认证正常运作。

### CGI

[Common Gateway Interface](<https://en.wikipedia.org/wiki/Common_Gateway_Interface> "wikipedia:Common Gateway Interface") (CGI) 脚本对于lighttpd可以开箱即用, 你只需要开启CGI模块, 指定配置文件，并确保指定语言的解释器已经安装。 (如：使用python需要安装 [python](<https://archlinux.org/packages/?name=python>)包) 

创建 `/etc/lighttpd/conf.d/cgi.conf` ，添加以下内容: 
    
    server.modules += ( "mod_cgi" )
    
    cgi.assign                 = ( ".pl"  => "/usr/bin/perl",
                                   ".cgi" => "/usr/bin/perl",
                                   ".rb"  => "/usr/bin/ruby",
                                   ".erb" => "/usr/bin/eruby",
                                   ".py"  => "/usr/bin/python",
                                   ".php" => "/usr/bin/php-cgi" )
    
    index-file.names           += ( "index.pl",   "default.pl",
                                   "index.rb",   "default.rb",
                                   "index.erb",  "default.erb",
                                   "index.py",   "default.py",
                                   "index.php",  "default.php" )
    
对于PHP脚本，请确认在 `/etc/php/php.ini`添加了下列配置： 
    
    cgi.fix_pathinfo = 1
    
在你的lighttpd配置文件中`/etc/lighttpd/lighttpd.conf`添加： 
    
    include "conf.d/cgi.conf"
    
### FastCGI

安装 [fcgi](<https://archlinux.org/packages/?name=fcgi>)包，之后你的lighttpd就有了fcgi支持， 以下内容是给需要使用Ruby，PHP或者Python的人的指导。 

**注意：** lighttpd现在默认以用户 `http` 运行。

首先复制一份默认配置，从 `/usr/share/doc/lighttpd/config/conf.d/fastcgi.conf` 复制到 `/etc/lighttpd/conf.d`

将以下内容添加到 `/etc/lighttpd/conf.d/fastcgi.conf`
    
    server.modules += ( "mod_fastcgi" )
    
    #server.indexfiles += ( "dispatch.fcgi" ) #这是强烈不建议的
    index-file.names += ( "dispatch.fcgi" ) # 如果选用rails，增加dispatch.fcgi
    
    server.error-handler-404   = "/dispatch.fcgi" #同上
    fastcgi.server = (
        ".fcgi" => (
          "localhost" => ( 
            "socket" => "/run/lighttpd/rails-fastcgi.sock",
            "bin-path" => "/path/to/rails/application/public/dispatch.fcgi"
          )
        )
    )
    
然后在 `/etc/lighttpd/lighttpd.conf`中添加: 
    
    include "conf.d/fastcgi.conf"
    
下面是关于PHP的指导。 

#### PHP

安装 [php](<https://archlinux.org/packages/?name=php>)包 和 [php-cgi](<https://archlinux.org/packages/?name=php-cgi>)包 (可以参阅 [PHP](<../zh-cn/PHP.html> "PHP") 、 [LAMP](<../zh-cn/Category:%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8.html> "LAMP")). 

确认php-cgi可以工作： `php-cgi --version`
    
    PHP 5.4.3 (cgi-fcgi) (built: May  8 2012 17:10:17)
    Copyright (c) 1997-2012 The PHP Group
    Zend Engine v2.4.0, Copyright (c) 1998-2012 Zend Technologies
    
如果输出内容与上面相仿则php已经正确安装。 

创建一份新的配置文件: 
    
    /etc/lighttpd/conf.d/fastcgi.conf
    
    # 请确保php和php-cgi已正确安装。参阅:                                                             
    # https://wiki.archlinux.org/index.php/Fastcgi_and_lighttpd#PHP
    
    server.modules += ("mod_fastcgi")
    
    # FCGI server
    # ===========
    #
    # 配置一个处理PHP请求的FastCGI服务器
    #
    index-file.names += ("index.php")
    fastcgi.server = ( 
        ".php" => (
            # 下列FastCGI服务器中的负载均衡配置。
            # 服务器的命名仅用作日志中服务器的标识名。
            "localhost" => ( 
                "bin-path" => "/usr/bin/php-cgi",
                "socket" => "/tmp/php-fastcgi.sock",
                # 分解SCRIPT_FILENAME 以让PHP能够从中解析出PATH_INFO
                "broken-scriptfilename" => "enable",
                # 启动 (max-procs + (max-procs * PHP_FCGI_CHILDREN)) 个进程, 其中
                # max-procs 个是“watcher”进程，其余是“worker”进程。参阅：
                # https://redmine.lighttpd.net/projects/1/wiki/frequentlyaskedquestions#How-many-php-CGI-processes-will-lighttpd-spawn 
                "max-procs" => 4, # 默认值
                "bin-environment" => (
                    "PHP_FCGI_CHILDREN" => "1" # 默认值
                )
            )
        )   
    )
    
在/etc/lighttpd/lighttpd.conf中添加以下内容使新配置能够应用: 
    
    /etc/lighttpd/lighttpd.conf
    
    include "conf.d/fastcgi.conf"
    
**注意：** 模块顺序十分重要, 正确地模块加载顺序位于 `/usr/share/doc/lighttpd/config/modules.conf`. 任何错误配置都可能导致 _lighttpd_ 崩溃。

重新加载 lighttpd： 

  1. systemctl restart lighttpd

**注意：**

  * 如果你在访问php文件时遇到诸如 _No input file found_ 的错误, 有很多原因可以导致这个错误，请参阅 [this FAQ](<https://redmine.lighttpd.net/projects/1/wiki/frequentlyaskedquestions#I-get-the-error-No-input-file-specified-when-trying-to-use-PHP>) 。
  * 确认没有其他模块 (如 `mod_cgi`) 负责处理php文件。

#####  使用php-fpm

为了动态管理PHP进程，你可以安装[php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包，启动`php-fpm.service`。 

**注意：** 你可以编辑`/etc/php/php-fpm.conf`以调整池中的服务器数量，以及其他配置项。更多关于php-fpm的细节可在[php-fpm 网站](<https://php-fpm.org/>)上找到。注意：你对`/etc/php/php.ini`做出改动后需要重启`php-fpm.service`。

在 `/etc/lighttpd/conf.d/fastcgi.conf` 添加: 
    
    server.modules += ( "mod_fastcgi" )
    
    index-file.names += ( "index.php" ) 
    
    fastcgi.server = (
        ".php" => (
          "localhost" => ( 
            "socket" => "/run/php-fpm/php-fpm.sock",
            "broken-scriptfilename" => "enable"
          ))
    )
    
### uWSGI

在 `/etc/lighttpd/lighttpd.conf`中加入 
    
    server.modules += ("mod_scgi")
    
    $HTTP["url"] =~ "^/uwsgi/" {
        scgi.protocol = "uwsgi"
        scgi.server   = (
            "/uwsgi/foo" => ((
                "socket"            => "/path/to/socket",
                "check-local"       => "disable"
            )),
            "/uwsgi/bar" =>
                "host"              => "127.0.0.1",
                "port"              => "8080",
                "check-local"       => "disable"
            ))
        )
    }

可以采用[systemd unit](<https://uwsgi-docs.readthedocs.io/en/latest/Systemd.html>)]或[[direct](<https://redmine.lighttpd.net/projects/lighttpd/wiki/HowToPythonWSGI>)的方式启动ywsgi应用。 [此处](<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04>)是一个来自 [digitalocean](<https://www.digitalocean.com>)的小巧的教程，指出如何从零开始创建一个Flask框架应用程序。 

###  输出压缩

复制示例配置文件： 
    
    # mkdir /etc/lighttpd/conf.d
    # cp /usr/share/doc/lighttpd/config/conf.d/deflate.conf /etc/lighttpd/conf.d/
    
在`/etc/lighttpd/lighttpd.conf`中增加如下内容： 
    
    include "conf.d/deflate.conf"
    
Finally, [reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") `lighttpd.service`, 后续将会自动压缩纯文本和 html 内容。 

**注意：** 不能通过在`/etc/lighttpd/lighttpd.conf`增加内容代替复制`deflate.conf`的作用

`/etc/lighttpd/conf.d/deflate.conf`中的`deflate.mimetypes`参数配置何种类型的内容应该被压缩： 
    
    deflate.mimetypes           = ("text/plain", "text/html", "text/javascript", "text/css", "text/xml")
    
可以创建缓存目录保存压缩后的文件: 
    
    # mkdir /var/cache/lighttpd/compress
    # chown http:http /var/cache/lighttpd/compress
    
取消 `/etc/lighttpd/conf.d/deflate.conf` 中 `deflate.cache-dir` 选项的注释并修改为： 
    
    deflate.cache-dir = "/var/cache/lighttpd/compress"
    
##  参见

  * [Lighttpd wiki](<https://redmine.lighttpd.net/projects/lighttpd/wiki>)
