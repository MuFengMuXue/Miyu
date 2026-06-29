相关文章

  * [Gogs](</wzh/index.php?title=Gogs&action=edit&redlink=1> "Gogs（页面不存在）")
  * [Git](<../zh-cn/Git.html> "Git")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:Gitea#](<../zh-cn/Talk:Gitea.html>) 中讨论）

**翻译状态：**

  * 本文（或部分内容）译自 [Gitea](<https://wiki.archlinux.org/title/Gitea> "arch:Gitea")，最近一次同步于 2024-04-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gitea?diff=0&oldid=808158>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gitea_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Gitea](<https://gitea.io/>) 是 [Gogs](</wzh/index.php?title=Gogs&action=edit&redlink=1> "Gogs（页面不存在）") 的社区管理分支，Gogs 是用 Go 编写并在 MIT 许可下发布的轻量级代码托管解决方案。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gitea](<https://archlinux.org/packages/?name=gitea>)包 或 [gitea-git](<https://aur.archlinux.org/packages/gitea-git/>)AUR 软件包。还有一个 gitea fork [forgejo](<https://archlinux.org/packages/?name=forgejo>)包 软件包。 

Gitea 需要使用数据库后端，支持以下数据库： 

  * [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")/[MySQL](<../zh-cn/MySQL.html> "MySQL")
  * [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")
  * [SQLite](<../zh-cn/SQLite.html> "SQLite")
  * MSSQL

##  配置

用户配置文件位于 `/etc/gitea/app.ini`。 

有关更多配置示例，参见 [Gitea 文档](<https://docs.gitea.io/en-us/customizing-gitea/>)。 

### PostgreSQL

[安装](<../zh-cn/PostgreSQL.html#Installation> "PostgreSQL")并[配置](<../zh-cn/PostgreSQL.html#Initial_configuration> "PostgreSQL") [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL"). 

在 TCP 或 UNIX 套接字之间进行选择，然后跳转到相应的部分。 

**注意：** 当 Gitea 和 PostgreSQL 在同一台机器上时，您应该使用 Unix 套接字，因为它更快、更安全。

####  用 TCP socket

以 `postgres` 用户身份连接服务器时创建新用户（系统会提示输入新用户的密码）： 
    
    [postgres]$ createuser -P gitea
    
创建用户 `gitea` 拥有的 Gitea 数据库： 
    
    [postgres]$ createdb -O gitea gitea
    
[PostgreSQL#Configure PostgreSQL to be accessible from remote hosts](<../zh-cn/PostgreSQL.html#Configure_PostgreSQL_to_be_accessible_from_remote_hosts> "PostgreSQL")

验证它是否有效： 
    
    $ psql --host=_ip_address_ --dbname=gitea --username=gitea --password
    
通过首次运行安装程序或更新 `app.ini` 配置 Gitea： 
    
    /etc/gitea/app.ini
    
    DB_TYPE             = postgres
    HOST                = _hostadress:port_
    NAME                = gitea
    USER                = gitea
    ; Use PASSWD = `your password` for quoting if you use special characters in the password.
    PASSWD              = **password**

####  用 Unix socket

以 `postgres` 用户身份连接服务器时创建新用户（系统会提示输入新用户的密码）： 
    
    [postgres]$ createuser gitea
    
创建用户 `gitea` 拥有的 Gitea 数据库： 
    
    [postgres]$ createdb -O gitea gitea
    
通过将以下行添加到 `/var/lib/postgres/data/pg_hba.conf` 来设置 Unix 套接字： 
    
    /var/lib/postgres/data/pg_hba.conf
    
    local    gitea           gitea           peer
    
[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `postgresql.service`. 

验证它是否有效： 
    
    [gitea]$ psql --dbname=gitea --username=gitea
    
通过首次运行安装程序或更新 `app.ini` 配置 Gitea： 
    
    /etc/gitea/app.ini
    
    DB_TYPE             = postgres
    HOST                = /run/postgresql/
    NAME                = gitea
    USER                = gitea
    PASSWD              =

###  MariaDB/MySQL

**注意：** 使用`/var/run/mysqld/mysqld.sock` 作为监听参数，即可启用 MySQL 套接字支持。

以下是设置[MariaDB](<../zh-cn/MariaDB.html> "MariaDB")的示例，设置所需的密码： 
    
    $ mysql -u root -p
    
    mysql> CREATE DATABASE `gitea` DEFAULT CHARACTER SET `utf8mb4` COLLATE `utf8mb4_unicode_ci`;
    mysql> CREATE USER `gitea`@'localhost' IDENTIFIED BY '**password'** ;
    mysql> GRANT ALL PRIVILEGES ON `gitea`.* TO `gitea`@`localhost`;
    mysql> FLUSH PRIVILEGES;
    mysql> \q

尝试使用新用户连接到新数据库： 
    
    $ mysql -u **gitea** -p -D gitea
    
通过首次运行安装程序或更新 `app.ini` 配置MariaDB： 
    
    /etc/gitea/app.ini
    
    DB_TYPE  = mysql
    HOST     = 127.0.0.1:3306 ; or /var/run/mysqld/mysqld.sock
    NAME     = gitea
    USER     = _gitea_
    PASSWD   = **password**

##  用法

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `gitea.service`, 网络接口应在 `http://localhost:3000` 上监听。 

首次运行 Gitea 时，应该会重定向到 `http://localhost:3000/install`。 

**注意：**

  * 您可能希望配置反向代理以进行远程访问，例如 [nginx](<#nginx>).
  * 如果希望 Gitea 监听所有接口，请在 `/etc/gitea/app.ini` 中设置 `HTTP_ADDR = 0.0.0.0`。

##  技巧和窍门

###  本地 shell 客户端 (tea)

通过 [tea](<https://archlinux.org/packages/?name=tea>)包，您可以使用 gitea 的官方客户端。更多信息请访问 <https://gitea.com/gitea/tea> 。 

###  启用 SSH 支持

确保 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 已正确配置并运行。 

####  设置域名

您可能希望设置`SSH_DOMAIN`, 例如 
    
    /etc/gitea/app.ini
    
    SSH_DOMAIN                 = git.domain.tld

**注意：** 如果将 `PROTOCOL` 设置为 `unix` ，则需要取消设置 `LOCAL_ROOT_URL` 或将其设置为 `http://unix/`。参见 [comment](<https://github.com/go-gitea/gitea/issues/3741#issuecomment-377334757>)。

####  配置 SSH

默认情况下，Gitea 将以用户 `gitea` 的身份运行；该账户也将用于 ssh 版本库访问。要使 ssh 访问正常，必须启用 PAM。或者，也可以解锁服务账户。 
    
    /etc/ssh/sshd_config
    
    ...
    UsePAM yes
    ...

如果在 [SSH 配置](<../zh-cn/OpenSSH.html#Configuration_2> "OpenSSH")中使用 `AllowUsers`，请在其中添加 `AllowUsers gitea`，例如： 
    
    /etc/ssh/sshd_config
    
    ...
    AllowUsers archie **gitea**
    ...

如果使用 `sshd.service`，请[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动")该服务（如果使用 `sshd.socket`，则无需重启）。 

###  禁用 HTTP 协议

默认情况下，已启用通过 HTTP 协议与版本库交互的功能。 如果使用[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")，可以将 `DISABLE_HTTP_GIT` 设置为 `true`，禁用 HTTP 支持。 

###  绑定受限端口

如果使用内置 SSH 服务器并希望 Gitea 将其绑定到 22 端口，或希望直接将 Gitea 网络服务器绑定到 80/443 端口（即在不使用代理的设置中），则需要添加 [drop-in systemd unit override](<../zh-cn/Systemd.html#Drop-in_files> "Systemd")： 
    
    /etc/systemd/system/gitea.service.d/override.conf
    
    [Service]
    AmbientCapabilities=CAP_NET_BIND_SERVICE
    CapabilityBoundingSet=CAP_NET_BIND_SERVICE
    PrivateUsers=false

###  启用 Dark 主题

在 _ui_ 部分，可以将 `DEFAULT_THEME` 设置为 `arc-green`，使网页界面使用深色背景。 

###  自定义 Gitea 的外观

更多详情，请参阅 Gitea 文档[[1]](<https://docs.gitea.io/en-us/administration/customizing-gitea/>)。 

gitea 的外观可使用[Go](<../zh-cn/Go.html> "Go")模板进行高度定制。 首先，创建 `/var/lib/gitea/custom` 目录。 可通过编辑 `/var/lib/gitea/custom/templates` 中的文件覆盖模板。 默认模板可在 `templates` 目录下的 [Gitea 源代码](<https://github.com/go-gitea/gitea>)中找到。例如，要自定义主页，可将源代码中的 `templates/home.tmpl` 复制到 `/var/lib/gitea/custom/templates/home.tmpl` 并根据需要编辑模板。 

此外，还可以通过创建以下文件更改徽标和图标： `/var/lib/gitea/custom/public/img/logo.svg`和 `/var/lib/gitea/custom/public/img/favicon.svg`

更改这些文件后，需要重新启动 Gitea。 

###  配置反向代理

有关更多信息和示例，请参阅 Gitea 文档网站 [[2]](<https://docs.gitea.io/en-us/reverse-proxies/>) 上的反向代理部分。 

#### nginx

The following is an example of using [nginx](<../zh-cn/Nginx.html#Managing_server_entries> "Nginx") as reverse proxy for Gitea over unix socket (you need to [provide the SSL certificate](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）")): 
    
    /etc/nginx/servers-available/gitea.conf
    
    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        server_name git.domain.tld;
    
        ssl_certificate /path/to/fullchain.pem;
        ssl_certificate_key /path/to/privkey.pem;
    
        location / {
            client_max_body_size 512M;
            proxy_pass <http://unix:/run/gitea/gitea.socket>;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

Update the `[server]` and `[session]` section of `app.ini`: 
    
    /etc/gitea/app.ini
    
    [server]
    PROTOCOL                   = unix
    DOMAIN                     = git.domain.tld
    ROOT_URL                   = https://git.domain.tld
    HTTP_ADDR                  = /run/gitea/gitea.socket
    LOCAL_ROOT_URL             =
    
    [session]
    COOKIE_SECURE              = true 
    
**注意：** You do not need to activate any SSL certificate options in `/etc/gitea/app.ini`.

#### Apache HTTP Server

The following is an example of using the [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") as reverse proxy for Gitea over unix socket. To forward `domain.tld` to the gitea server, use 
    
    /etc/httpd/conf/httpd.conf
    
    ProxyPreserveHost On
    ProxyRequests off
    AllowEncodedSlashes NoDecode
    Proxypass / unix:/run/gitea/gitea.socket|http://domain.tld nocanon
    ProxypassReverse / unix:/run/gitea/gitea.socket|http://domain.tld nocanon
    
where `domain.tld` should be replaced by your domain name (this entry is only passed as a header to the proxy, and does not seem to matter for this setup). 
    
    /etc/gitea/app.ini
    
    [server]
    PROTOCOL                   = unix
    DOMAIN                     = domain.tld
    ROOT_URL                   = https://domain.tld
    HTTP_ADDR                  = /run/gitea/gitea.socket
    LOCAL_ROOT_URL             =
    
To forward a subpath such as `domain.tld/git` to the gitea server, use 
    
    /etc/httpd/conf/httpd.conf
    
    <Proxy *>
      Order allow,deny
      Allow from all
    </Proxy>
    AllowEncodedSlashes NoDecode
    Proxypass /git unix:/run/gitea/gitea.socket|http://domain.tld nocanon
    ProxypassReverse /git unix:/run/gitea/gitea.socket|http://domain.tld nocanon
    
    /etc/gitea/app.ini
    
    [server]
    PROTOCOL                   = unix
    DOMAIN                     = domain.tld
    ROOT_URL                   = https://git.domain.tld
    HTTP_ADDR                  = /run/gitea/gitea.socket
    LOCAL_ROOT_URL             =
    
### Setup for custom data directory

As of now, you cannot use a custom path like `/srv/gitea` as your server home, since the shipped `gitea.service` unit file marks everything read-only. 

To enable these custom paths, create a [drop-in snippet](<../zh-cn/Drop-in_snippet.html> "Drop-in snippet") with your server home directory as a new `ReadWriteDirectories` directive: 
    
    /etc/systemd/system/gitea.service.d/data-directory.conf
    
    [Service]
    ReadWriteDirectories=/srv/gitea

Then do a [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") and [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `gitea.service` for the changes to take effect. 

##  问题解决

###  升级到 1.5.0 后启动数据库时出现错误

升级到 1.5.0 后可能会出现问题。服务无法启动，日志中出现以下错误： 
    
    /var/log/gitea/gitea.log
    
    2018/08/21 16:11:12 [...itea/routers/init.go:60 GlobalInit()] [E] Failed to initialize ORM engine: migrate: do migrate: Sync2: Error 1071: Specified key was too long; max key length is 767 bytes

要解决这个问题，请在 MySQL/MariaDB 服务器上以 `root` 用户身份运行以下命令 
    
    $ mysql -u root -p
    
    MariaDB> set global innodb_large_prefix = `ON`;

gitea should stop complaining about key size and startup properly. 

### Service failing with permission denied

如果手动创建 `gitea` 用户，并将其主页文件夹设置为 `/home/gitea`，gitea 服务将无法启动，并输出类似于 ： 
    
    Sep 04 04:44:32 systemd[1]: gitea.service: Failed with result 'exit-code'.
    Sep 04 04:44:32 systemd[1]: gitea.service: Main process exited, code=exited, status=200/CHDIR
    Sep 04 04:44:32 (gitea)[30727]: gitea.service: Failed at step CHDIR spawning /usr/bin/gitea: Permission denied
    Sep 04 04:44:32 (gitea)[30727]: gitea.service: Changing to the requested working directory failed: Permission denied
    
该服务需要将用户的主文件夹作为 gitea 的主文件夹，默认文件夹为 `/var/lib/gitea` ： 
    
    $ usermod -d /var/lib/gitea gitea
    
##  参见

  * [Gitea Documentation](<https://docs.gitea.io/>)
