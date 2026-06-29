[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:GitLab](<../zh-cn/Talk:GitLab.html>)讨论)

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** No updates since 2018（在 [Talk:GitLab#](<../zh-cn/Talk:GitLab.html>) 中讨论）

相关文章

  * [Gitolite](</wzh/index.php?title=Gitolite&action=edit&redlink=1> "Gitolite（页面不存在）")
  * [Ruby on Rails](<../zh-cn/Ruby_on_Rails.html> "Ruby on Rails")

**翻译状态：**

  * 本文（或部分内容）译自 [Gitlab](<https://wiki.archlinux.org/title/Gitlab> "arch:Gitlab")，最近一次同步于 2024-2-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gitlab?diff=0&oldid=800947>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gitlab_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

这是来自 [Gitlab的主页](<https://about.gitlab.com/>): 

    GitLab 提供 git 仓储管理、代码查阅、问题追踪、动态监控和维基. 企业在本地安装Gitlab并用LDAP和活动目录服务器连接以进行安全的身份验证和授权。单个GitLab服务器可以处理超过25,000个用户，但也可以使用多个活动服务器创建高可用性设置。

你可以在 [GitLab.com](<https://gitlab.com/>)找到实时版本的例子. 

##  安装

**注意：** 这篇文章优先覆盖非https安装和配置Gitlab. 如果需要，查阅[#更多配置](<#%E6%9B%B4%E5%A4%9A%E9%85%8D%E7%BD%AE>) 来设置SSL.

Gitlab需要 [Redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）") 和数据库后端. 如果你计划在同一个机器运行的话, 首先得安装 [PostgreSQL (简体中文)](</wzh/index.php?title=PostgreSQL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "PostgreSQL \(简体中文\)（页面不存在）"). 

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [gitlab](<https://archlinux.org/packages/?name=gitlab>)包 包. 

为了接受邮件通知, 一个邮件服务器必须被安装和配置. 查阅 [Category:Mail server](<../zh-cn/Category:Mail_server.html> "Category:Mail server") 获取更多细节. 

##  配置

###  初步说明

Gitlab包括多种组件, 可查阅[架构概览页](<https://docs.gitlab.com/ce/development/architecture.html>). 

[gitlab](<https://archlinux.org/packages/?name=gitlab>)包 包会以更接近标准Linux公约的方式安装Gitlab: 

描述  |  [GitLab's Official](<https://github.com/gitlabhq/gitlabhq/blob/master/doc/install/installation.md>) |  [gitlab](<https://archlinux.org/packages/?name=gitlab>)包  
---|---|---  
配置文件 GitShell  |  `/home/git/gitlab-shell/config.yml` |  `/etc/webapps/gitlab-shell/config.yml`  
配置文件 GitLab  |  `/home/git/gitlab/config/gitlab.yml` |  `/etc/webapps/gitlab/gitlab.yml`  
用户 (家目录)  |  `git` (`/home/git`)  |  `gitlab` (`/var/lib/gitlab`)   
  
**提示：** 如果你熟悉 [Arch Build System](<../zh-cn/Arch_Build_System.html> "Arch Build System") 你可以编辑PKGBUILD和相关文件来改变gitlab的家目录到你喜欢的位置.

### GitLab

编辑 `/etc/webapps/gitlab/gitlab.yml` 并至少设置下面的参数: 

**注意：** `hostname` 和 `port` 被用于 `git clone <http://hostname:port>` 的例子中.

**Hostname:** 在 `gitlab:` 区里设置 `host:` \- 把 `localhost` 换成 `yourdomain.com` (**注意:** 不要加 '<http://'> 或者后面的斜线) - 到你的完全合格的域名. 

**Port:** `port:` 可能会让你很困扰. 这不是Gitlab服务器运行的端口(unicorn) ; 这是用户通过浏览器初次连接的端口. 基本上, 如果你有意让用户通过他们的浏览器访问 'yourdomain.com' , 而且不用附加端口号, 把 `port:` 设成 `80`. 如果你想让用户输入比如 'yourdomain.com:3425' 这样的东西到浏览器, 那么你就得设置 `port:` 成 `3425`. 你也会得**设置你的网络服务器** 来监听那个端口. 

**Timezone (时区，可选):** `time_zone:` 参数是可选的, 但是它可能对强制Gitlab应用的区域有用. 

最后设置正确的 [permissions](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "Permissions") 到 _uploads_ （上传） 目录: 
    
    # chmod 700 /var/lib/gitlab/uploads
    
###  为Puma自定义端口

GitLab Puma 是处理大多数用户请求的主要组件. 默认的, Unix套接字 /run/gitlab/gitlab.socket，可以通过 `/etc/webapps/gitlab/puma.rb` 文件来改变: 
    
    /etc/webapps/gitlab/puma.rb
    
    bind 'unix:///run/gitlab/gitlab.socket'
    bind 'tcp://127.0.0.1:8080'

如果 Puma 地址被改变, 其它与Puma交流的组件的配置也需要被更新: 

  * 对于 GitLab Shell, 在 `/etc/webapps/gitlab-shell/config.yml`更新 `gitlab_url` 变量.

**提示：** 根据注释里的配置文件, UNIX 套接字能通过 URL转义斜杠(/) (即. `http+unix://%2Frun%2Fgitlab%2Fgitlab.socket` 对应默认的 `/run/gitlab/gitlab.socket`). 额外的, 未转义斜杠能用来指定 [相关URL根路径](<https://docs.gitlab.com/ce/install/relative_url.html>) (例如. `/gitlab`).

  * 对于 GitLab Workhorse, [edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `gitlab-workhorse.service` 并更新 `-authBackend` 选项.

###  机密字符串

确定 `/etc/webapps/gitlab/secret` 和 `/etc/webapps/gitlab-shell/secret` 文件包含了些什么. 它们的内容应该被保密因为它们会被用作生成认证令牌等. 

比如, 能够通过下面的命令生成随机字符串: 
    
    # hexdump -v -n 64 -e '1/1 "%02x"' /dev/urandom > /etc/webapps/gitlab/secret
    # chmod 640 /etc/webapps/gitlab/secret
    
    # hexdump -v -n 64 -e '1/1 "%02x"' /dev/urandom > /etc/webapps/gitlab-shell/secret
    # chmod 640 /etc/webapps/gitlab-shell/secret
    
同时需要填写以下新的机密字符串 
    
    /etc/webapps/gitlab/secrets.yml
    
    production:
      secret_key_base: secret
      db_key_base: secret
      otp_key_base: secret
      openid_connect_signing_key: secret
    
### Redis

为了提供足够的性能，你可能需要一个缓存数据库. [安装](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）")并[配置](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）")一个redis实例, 注意专用于通过套接字监听的部分. 

  * 添加 `gitlab` 用户到 `redis` [user group](<../zh-cn/User_group.html> "User group").

  * 更新配置文件:

    /etc/webapps/gitlab/resque.yml
    
    development:
      url: unix:/run/redis/redis.sock
    test:
      url: unix:/run/redis/redis.sock
    production:
      url: unix:/run/redis/redis.sock
    
    /etc/webapps/gitlab-shell/config.yml
    
    # Redis settings used for pushing commit notices to gitlab
    redis:
      bin: /usr/bin/redis-cli
      host: 127.0.0.1
      port: 6379
      # pass: redispass # Allows you to specify the password for Redis
      database: 5 # Use different database, default up to 16
      socket: /run/redis/redis.sock # **uncomment** this line
      namespace: resque:gitlab

###  数据库后端

在Gitlab运行之前需要一个[PostgreSQL]数据库. 

#### PostgreSQL

登录 PostgreSQL 并创造 `gitlabhq_production` 数据库和它的用户一起. 记得改变 `your_username_here` 和 `your_password_here` 到你的真正的值: 
    
    # psql -d template1
    
    template1=# CREATE USER your_username_here WITH PASSWORD 'your_password_here';
    template1=# ALTER USER your_username_here SUPERUSER;
    template1=# CREATE DATABASE gitlabhq_production OWNER your_username_here;
    template1=# \q

**注意：** 创建超级用户的目的是Gitlab在视图变得"智能"并安装扩展(并不仅仅在它的命名区间创建).并且它只被Postgresql的超级用户允许.

用新用户连接到新数据库来确定它有用: 
    
    # psql -d gitlabhq_production
    
打开新的 `/etc/webapps/gitlab/database.yml` 并设置 `username:` 和 `password:`的值. 比如: 
    
    /etc/webapps/gitlab/database.yml
    
    #
    # PRODUCTION
    #
    production:
      main:
        adapter: postgresql
        encoding: unicode
        database: gitlabhq_production
        username: your_username_here
        password: "your_password_here"
        # host: localhost
        # port: 5432
        socket: /run/postgresql/.s.PGSQL.5432
      ci:
        adapter: postgresql
        encoding: unicode
        database: gitlabhq_production
        database_tasks: false
        username: your_username_here
        password: "your_password_here"
        # host: localhost
        # port: 5432
        socket: /run/postgresql/.s.PGSQL.5432
    ...
    
对于我们的目的 (除非你知道你在干什么),你不必担心配置列在 `/etc/webapps/gitlab/database.yml`的其它数据库. 我们只需要设置生产的数据库来让Gitlab工作. 

**注意：** 注意：自 GitLab 15.9 起，数据库.yml 中只有 main: 部分的做法已被淘汰。在 GitLab 17.0 及更高版本中，你必须在 database.yml 中包含两个部分：main: 和 ci:. ci:必须与 main: 连接到同一个数据库。

###  防火墙

如果你想通过[Iptables (简体中文)](<../zh-cn/Iptables_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Iptables \(简体中文\)") 防火墙给予Gitlab安装过程直接权限, 你可能需要调整端口和网络地址: 
    
    # iptables -A tcp_inbound -p TCP -s **192.168.1.0/24** --destination-port **80** -j ACCEPT
    
启用 API-access: 
    
    # iptables -A tcp_inbound -p TCP -s **192.168.1.0/24** --destination-port **8080** -j ACCEPT
    
如果你在一个路由器后面, 别忘了转发这个端口到Gitlab服务器端口, 如果你想运行 WAN-access的话. 

###  初始化Gitlab数据库

在初始化数据库之前开启 [Redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）") 服务器和 `gitlab-gitaly.service` . 

初始化数据库并激活更多特性: 
    
    $ cd /usr/share/webapps/gitlab
    $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:setup GITLAB_ROOT_PASSWORD=_yourpassword_ GITLAB_ROOT_EMAIL=_youremail_ GITLAB_LICENSE_FILE=_/path/to/license_
    
最后运行下面的命令来检查你的安装: 
    
    $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:env:info
    $ sudo -u gitlab $(cat environment | xargs) bundle exec rake gitlab:check
    
**注意：**

  * _gitlab:env:info_ 和 _gitlab:check_ 命令会显示一个和Git相关的严重的错误. 这是正常的.
  * _gitlab:check_ 会显示缺少初始化脚本. 这也没什么好担心的, 因为 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务文件会被相应使用 (而这Gitlab无法识别).

###  调整修改位

(如果用户和组所有权没有正确配置的话Gitlab检查不会通过) 
    
    # chmod -R ug+rwX,o-rwx /var/lib/gitlab/repositories/
    # chmod -R ug-s /var/lib/gitlab/repositories
    # find /var/lib/gitlab/repositories/ -type d -print0 | xargs -0 chmod g+s
    
##  开始并测试Gitlab

确定 [PostgreSQL (简体中文)](</wzh/index.php?title=PostgreSQL_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "PostgreSQL \(简体中文\)（页面不存在）") 和 [Redis](</wzh/index.php?title=Redis&action=edit&redlink=1> "Redis（页面不存在）") 运行和设置正确. 

然后 [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")/[enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `gitlab.target`. 

现在你可以通过访问 <http://localhost:8080> 或者 http://yourdomain.com来测试你的Gitlab[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-02 ⓘ], 你可能会被提示创建密码: 
    
    username: root
    password: You'll be prompted to create one on your first visit.
    
查阅[#故障排除](<#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4>)和在 `/usr/share/webapps/gitlab/log/` 目录下的日志文件来 排除故障. 

##  每次更新时升级数据库

###  手动操作

在更新 [gitlab](<https://archlinux.org/packages/?name=gitlab>)包 包后, 需要升级数据库: 
    
    $ cd /usr/share/webapps/gitlab
    $ sudo -u gitlab $(cat environment | xargs) bundle exec rake db:migrate
    
之后, 之后重载并重启Gitlab相关服务: `gitlab-sidekiq.service`, `gitlab-puma.service`, `gitlab-workhorse.service` 和 `gitlab-gitaly.service`

###  自动操作

你可以创建 pacman 钩子来自动升级 GitLab 软件包更新的数据库。创建以下三个文件，不要忘记使 shell 脚本可执行： 
    
    /etc/pacman.d/hooks/05-gitlab-pre.hook
    
    [Trigger]
    Operation = Upgrade
    Type = Package
    Target = gitlab
    
    [Action]
    Description = Stopping gitlab services
    When = PreTransaction
    Exec = /usr/bin/systemctl stop gitlab-gitaly.service gitlab-mailroom.service gitlab-puma.service gitlab-sidekiq.service gitlab-workhorse.service
    
    /etc/pacman.d/hooks/99-gitlab-post.hook
    
    [Trigger]
    Operation = Upgrade
    Type = Package
    Target = gitlab
    
    [Action]
    Description = Migrating GitLab database and starting services
    When = PostTransaction
    Exec = /etc/pacman.d/scripts/gitlab-migrate-database.sh
    
    /etc/pacman.d/scripts/gitlab-migrate-database.sh
    
    #!/bin/sh
    
    cd "/usr/share/webapps/gitlab"
    sudo -u gitlab $(cat environment | xargs) bundle exec rake db:migrate
    
    # The hook runs after 30-systemd-daemon-reload.hook so another systemctl daemon-reload is not necessary.
    systemctl start gitlab.target

##  更多配置

###  基本的 SSH

在完成了基本安装后, 为用户设置ssh权限. [安全外壳协议](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "安全外壳协议")的配置会在下面描述. [其它SSH客户端和服务器](<../zh-cn/Secure_Shell.html#Implementations> "Secure Shell")需要不同的调整. 

获取添加用户SSH秘钥的建议，过程在[GitLab](<https://docs.gitlab.com/ee/ssh/>) 网站里描述的很好了. 你可以在 `/var/lib/gitlab/log/gitlab-shell.log`检查管理员日志来确认用户SSH秘钥被正确提交了. 在这些事件之后, GitLab 添加这些秘钥到 _authorized_keys_ 文件里，它在 `/var/lib/gitlab/.ssh/authorized_keys`. 

测试秘钥的常见方法 (比如: `$ ssh -T git@_YOUR_SERVER_`) 需要一点额外配置才能正常工作. 在 `/etc/webapps/gitlab/gitlab.yml` (默认用户: `gitlab`)里配置的用户必须添加到服务器的sshd配置文件,除此之外还有几个其它改变 : 
    
    /etc/ssh/sshd_config
    
    PubkeyAuthentication   yes
    AuthorizedKeysFile     %h/.ssh/authorized_keys
    
更新配置文件之后, 重启ssh守护进程: 
    
    # systemctl restart sshd
    
测试用户SSH米哟啊 (可选添加 -v 来查看额外信息): 
    
    $ ssh -T **gitlab** @_YOUR_SERVER_
    
###  自定义SSH连接

如果你在一个非标准端口运行SSH，你必须改变Gitlab用户的SSH配置: 
    
    /var/lib/gitlab/.ssh/config
    
    host localhost      # Give your setup a name (here: override localhost)
    user gitlab         # Your remote git user
    port 2222           # Your port number
    hostname 127.0.0.1; # Your server name or IP

你还必须在 `/etc/webapps/gitlab/gitlab.yml` 文件里改变相应的选项 (比如. ssh_user, ssh_host, admin_uri) . 

###  HTTPS/SSL

####  改变Gitlab配置

修改 `/etc/webapps/gitlab/shell.yml` 那样到你的Gitlab站点的URL就会以 `https://`开头. 修改 `/etc/webapps/gitlab/gitlab.yml` 那样 `https:` 设置就会被设为 `true`. 

查阅 [Apache HTTP Server#TLS](<../zh-cn/Apache_HTTP_Server.html#TLS> "Apache HTTP Server") 和 [Let’s Encrypt](</wzh/index.php?title=Let%E2%80%99s_Encrypt&action=edit&redlink=1> "Let’s Encrypt（页面不存在）"). 

####  Let's Encrypt(让我们加密吧)

验证你的URL, Let's Encrypt的过程会试图用像 `https://gitlab._YOUR_SERVER_FQDN_ /.well-known/acme-challenge/_A_LONG_ID_`的东西连接你的Gitlab服务器. 但是, 因为Gitlab配置, 每个到 `gitlab._YOUR_SERVER_FQDN_` 的请求会被重定向到一个代理 (gitlab-workhorse) 而它无法处理这个URL. 

为了绕过这个问题, 你可以使用 Let's Encrypt的webroot配置, 在 `/srv/http/letsencrypt/`设置webroot. 

除此之外, 强迫到Gitlab的Let's Encrypt请求重定向到这个webroot可通过添加下面的: 
    
    /etc/http/conf/extra/gitlab.conf
    
    Alias "/.well-known"  "/srv/http/letsencrypt/.well-known"
    RewriteCond   %{REQUEST_URI}  !/\.well-known/.*
    
###  Web服务器配置

如果你想把Gitlab集成进一个运行的服务器而不是用它的内置http服务器Unicorn，那么按照这些说明操作. 

#### Node.js

你可以轻松在443端口设置http代理来代理到8080端口的Gitlab程序的流量，通过为Node.js使用http-master. 在你创建你的域名的 OpenSSL 秘钥并获取你的CA 证书 (或自己设置的)后, 然后去 <https://github.com/CodeCharmLtd/http-master> 来学习使用https代理到Gitlab的请求多容易. http-master 建立在 [node-http-proxy](<https://github.com/nodejitsu/node-http-proxy>)之上. 

#### Nginx

查阅 [Nginx#Configuration](<../zh-cn/Nginx.html#Configuration> "Nginx") 获取基本的 _nginx_ 配置信息和 [Nginx#TLS](<../zh-cn/Nginx.html#TLS> "Nginx") 来启用 HTTPS. 在这个部分的例子假设服务器区块是用 [Nginx#Managing server entries](<../zh-cn/Nginx.html#Managing_server_entries> "Nginx")管理的. 

创建和编辑基于下面代码的配置. 查阅 [upstream GitLab repository](<https://gitlab.com/gitlab-org/gitlab-ce/tree/master/lib/support/nginx>)获取更多例子. 
    
    /etc/nginx/servers-available/gitlab
    
    upstream gitlab-workhorse {
      server unix:/run/gitlab/gitlab-workhorse.socket fail_timeout=0;
    }
    
    server {
      listen 80;
      #listen 443 ssl; # uncomment to enable ssl
      server_name example.com
    
      #ssl_certificate ssl/example.com.crt;
      #ssl_certificate_key ssl/example.com.key;
    
      location / {
          # unlimited upload size in nginx (so the setting in GitLab applies)
          client_max_body_size 0;
    
          # proxy timeout should match the timeout value set in /etc/webapps/gitlab/unicorn.rb
          proxy_read_timeout 60;
          proxy_connect_timeout 60;
          proxy_redirect off;
    
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-Ssl on;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
    
          proxy_pass http://gitlab-workhorse;
      }
    
      error_page 404 /404.html;
      error_page 422 /422.html;
      error_page 500 /500.html;
      error_page 502 /502.html;
      error_page 503 /503.html;
      location ~ ^/(404|422|500|502|503)\.html$ {
        root /usr/share/webapps/gitlab/public;
        internal;
      }
    }
    
#### Apache

安装并配置 [Apache HTTP Server (简体中文)](</wzh/index.php?title=Apache_HTTP_Server_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Apache HTTP Server \(简体中文\)（页面不存在）"). 你可以使用这些 [upstream recipes](<https://gitlab.com/gitlab-org/gitlab-recipes/tree/master/web-server/apache>) 来开始Gitlab虚拟主机的配置文件. 

对于SSL配置查阅 [Apache HTTP Server#TLS](<../zh-cn/Apache_HTTP_Server.html#TLS> "Apache HTTP Server"). 如果你不需要它, 移除它. 注意到SSL虚拟主机需要特定IP而不是通用IP. 同样如果你为Unicorn设置了自定义端口, 不要忘了在 `BalanceMember` 行也设置它. 

### Gitlab-workhorse

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** [gitlab-workhorse](<https://archlinux.org/packages/?name=gitlab-workhorse>)包 组件现在是有必要的. 默认设置能应对普遍的情况所以这个部分能被移除. (在 [Talk:GitLab](<../zh-cn/Talk:GitLab.html>) 讨论)

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 这个部分还需要配置指导. (在 [Talk:GitLab](<../zh-cn/Talk:GitLab.html>) 中讨论)

Gitlab8.0以后使用分开的http服务器[gitlab-workhorse](<https://archlinux.org/packages/?name=gitlab-workhorse>)包来应对大量的http请求比如 Git 推送/拉取. 如果你想使用这个而不是 SSH, 安装 [gitlab-workhorse](<https://archlinux.org/packages/?name=gitlab-workhorse>)包 包, 启用 `gitlab-workhorse.service` 并为它配置web服务器. [gitlab-workhorse](<https://archlinux.org/packages/?name=gitlab-workhorse>)包 优先级应高于 `gitlab-unicorn` 根据 GitLab 的建议: <https://gitlab.com/gitlab-org/gitlab-ce/issues/22528#note_16036216>

**注意：** Unicorn还是需要所以不要disable或者stop它 `gitlab-unicorn.service`.

默认 [gitlab-workhorse](<https://archlinux.org/packages/?name=gitlab-workhorse>)包 监听 `/run/gitlab/gitlab-workhorse.socket`. 你可以 [edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") `gitlab-workhorse.service` 并改变参数 `-listenAddr` 来让它监听一个地址, 例如 `-listenAddr 127.0.0.1:8181`. 如果你监听一个地址的话你也要把网络类型设置为 `-listenNetwork tcp`

当你使用nginx时记得修改你的nginx配置文件. 从gitlab-unicorn 转换到 gitlab-workhorse 相应的编辑以下两个设置 
    
    /etc/nginx/servers-available/gitlab
    
    upstream gitlab {
       server unix:/run/gitlab/gitlab-workhorse.socket fail_timeout=0;
    }
    
    ...
          
          proxy_pass <http://unix:/run/gitlab/gitlab-workhorse.socket>;
      }  
    }

##  有用的建议

###  隐藏选项

到Gitlab的家目录: 
    
    # cd /usr/share/webapps/gitlab
    
并运行: 
    
    # rake -T | grep gitlab
    
    rake gitlab:app:check                         # GITLAB | Check the configuration of the GitLab Rails app
    rake gitlab:backup:create                     # GITLAB | Create a backup of the GitLab system
    rake gitlab:backup:restore                    # GITLAB | Restore a previously created backup
    rake gitlab:check                             # GITLAB | Check the configuration of GitLab and its environment
    rake gitlab:cleanup:block_removed_ldap_users  # GITLAB | Cleanup | Block users that have been removed in LDAP
    rake gitlab:cleanup:dirs                      # GITLAB | Cleanup | Clean namespaces
    rake gitlab:cleanup:repos                     # GITLAB | Cleanup | Clean repositories
    rake gitlab:env:check                         # GITLAB | Check the configuration of the environment
    rake gitlab:env:info                          # GITLAB | Show information about GitLab and its environment
    rake gitlab:generate_docs                     # GITLAB | Generate sdocs for project
    rake gitlab:gitlab_shell:check                # GITLAB | Check the configuration of GitLab Shell
    rake gitlab:import:all_users_to_all_groups    # GITLAB | Add all users to all groups (admin users are added as owners)
    rake gitlab:import:all_users_to_all_projects  # GITLAB | Add all users to all projects (admin users are added as masters)
    rake gitlab:import:repos                      # GITLAB | Import bare repositories from gitlab_shell -> repos_path into GitLab project instance
    rake gitlab:import:user_to_groups[email]      # GITLAB | Add a specific user to all groups (as a developer)
    rake gitlab:import:user_to_projects[email]    # GITLAB | Add a specific user to all projects (as a developer)
    rake gitlab:satellites:create                 # GITLAB | Create satellite repos
    rake gitlab:setup                             # GITLAB | Setup production application
    rake gitlab:shell:build_missing_projects      # GITLAB | Build missing projects
    rake gitlab:shell:install[tag,repo]           # GITLAB | Install or upgrade gitlab-shell
    rake gitlab:shell:setup                       # GITLAB | Setup gitlab-shell
    rake gitlab:sidekiq:check                     # GITLAB | Check the configuration of Sidekiq
    rake gitlab:test                              # GITLAB | Run all tests
    rake gitlab:web_hook:add                      # GITLAB | Adds a web hook to the projects
    rake gitlab:web_hook:list                     # GITLAB | List web hooks
    rake gitlab:web_hook:rm                       # GITLAB | Remove a web hook from the projects
    rake setup                                    # GITLAB | Setup gitlab db
    
###  备份和恢复

创建Gitlab系统的备份: 
    
    # sudo -u gitlab -H rake RAILS_ENV=production gitlab:backup:create
    
从之前创建的备份文件恢复 `/home/gitlab/gitlab/tmp/backups/20130125_11h35_1359131740_gitlab_backup.tar`: 
    
    # sudo -u gitlab -H rake RAILS_ENV=production gitlab:backup:restore BACKUP=/home/gitlab/gitlab/tmp/backups/20130125_11h35_1359131740
    
**注意：** 备份文件夹在 `config/gitlab.yml`设置. GitLab 备份和恢复记录在 [这里](<https://github.com/gitlabhq/gitlabhq/blob/master/doc/raketasks/backup_restore.md>).

###  通过SMTP从Gitlab发送邮件

你可能想用 gmail (或者其它邮件服务) 从你的Gitlab寄邮件. 这能避免在Gitlab服务器上安装邮件守护进程的需要. 

根据你的邮件服务器设置调整 `smtp_settings.rb` : 
    
    /usr/share/webapps/gitlab/config/initializers/smtp_settings.rb
    
    if Rails.env.production?
      Gitlab::Application.config.action_mailer.delivery_method = :smtp
    
      ActionMailer::Base.delivery_method = :smtp
      ActionMailer::Base.smtp_settings = {
        address:              'smtp.gmail.com',
        port:                 587,
        domain:               'gmail.com',
        user_name:            'username@gmail.com',
        password:             'application password',
        authentication:       'plain',
        enable_starttls_auto: true
      }
    end

Gmail 会拒绝这样接受的邮件 (并会邮寄给你一个邮件它拒绝了). 你需要关闭安全认证 (按照拒绝邮件中的链接) 来解决这个问题. 更安全的办法是为username@gmail.com开启双因素认证并为这个配置文件设置应用密码. 

##  故障排除

###  HTTPS不是绿色 (gravatar不使用 https)

Redis 缓存了 gravatar 图像, 如果你用http拜访 GitLab, 那么启用 https, gravatar 会加载不安全的图像. 你可以清楚这些缓存通过执行以下命令 
    
    cd /usr/share/webapps/gitlab
    RAILS_ENV=production bundle-2.3 exec rake cache:clear
    
以Gitlab用户的身份. 

###  更新后的错误

从AUR更新安装包后, 数据库迁移和资源更新有时候会失败. 这些步骤可以解决这些问题, 如果简单的开关机不行的话. 

首先, 移动到Gitlab安装目录. 
    
    # cd /usr/share/webapps/gitlab
    
如果每个Gitlab页面都给了一个500页面, 那么数据库迁移和资源可能太陈旧了. 如果不是的话, 跳过这步. 
    
    # su - gitlab -s /bin/sh -c "cd '/usr/share/webapps/gitlab'; bundle-2.3 exec rake db:migrate RAILS_ENV=production"
    
如果Gitlab一直在等待布置完成的话, 那么资源可能没有被重新编译. 
    
    # su - gitlab -s /bin/sh -c "cd '/usr/share/webapps/gitlab'; bundle-2.3 exec rake gitlab:assets:clean gitlab:assets:compile cache:clear RAILS_ENV=production"
    
最后, 重启Gitlab服务再测试你的网站. 
    
    # systemctl restart gitlab-unicorn gitlab-sidekiq gitlab-workhorse
    
###  Gitlab-Unicorn 无法访问非默认的从库目录

如果自定义的仓库存储目录被设置在 `/home`, 在`gitlab-unicorn.service`禁用 `ProtectHome=true` 参数 (查阅 [Systemd#Drop-in files](<../zh-cn/Systemd.html#Drop-in_files> "Systemd") 和 [github.com上的相关论坛帖子](<https://forum.gitlab.com/t/cannot-change-repositores-location/9634/2>)). 

###  无法连接到 Gitaly

有时候, Gitaly服务无法开始, 让gitlab无法连接到gitlay. 解决办法很简单: 
    
    # systemctl start gitlab-gitaly
    
##  也可查阅

  * [Official installation documentation](<https://docs.gitlab.com/ce/install/installation.html>)
  * [GitLab recipes with further documentation on running it with several web servers](<https://gitlab.com/gitlab-org/gitlab-recipes>)
  * [GitLab source code](<https://gitlab.com/gitlab-org/gitlab-ce>)
