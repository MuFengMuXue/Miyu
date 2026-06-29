**翻译状态：**

  * 本文（或部分内容）译自 [Matomo](<https://wiki.archlinux.org/title/Matomo> "arch:Matomo")，最近一次同步于 2022-09-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Matomo?diff=0&oldid=744762>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Matomo_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Matomo，前身为 Piwik，是一个开源网络分析工具，在 GNU 通用公共许可证 3 下获得许可。该软件是用 php 编写的，可以通过网络浏览器访问。该项目的核心理念是隐私，因为当使用第三方网站分析提供商时，网站所有者会将用户的数据泄露给他们，以便他们将其出售给广告商。 

通过在目标网站上加载一些JavaScript，可以用一个运行实例分析多个网站。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [matomo](<https://aur.archlinux.org/packages/matomo/>)AUR 或 [matomo-git](<https://aur.archlinux.org/packages/matomo-git/>)AUR 包。git 包已经为你配置了 php-fpm 守护程序。此外，它还为你下载并安装了最新的 GeoIP 数据库。默认情况下，Matomo 通过访客设定的浏览器语言来猜测他们的位置，这不是可靠的地理位置信息。 

##  配置

###  php 配置

需要正确配置 php 才能使 Matomo 工作。 

首先，启用 MySQL 支持，如 [PHP#MySQL/MariaDB](<../zh-cn/PHP.html#MySQL/MariaDB> "PHP") 中所述。通过编辑 `/etc/php/php.ini` 来做到这一点。通过删除前面的分号取消注释 `;extension=pdo_mysql` 和 `;extension=mysqli`。 

通常，注释由前面的分号表示。 

`;extension=iconv` 需要启用，并且 `;extension=gd` 对于 Matomo 是可选的。至少取消注释 iconv。 

####  允许 Matomo 访问需要的文件

**注意：** 此处的更改仅适用于 [matomo](<https://aur.archlinux.org/packages/matomo/>)AUR 包而不是 [matomo-git](<https://aur.archlinux.org/packages/matomo-git/>)AUR 包，因为后者已经包含此文件。

由于7.4版以来对 `php-fpm.service` 的新限制，其中 `ProtectSystem` 被设置为阻止 Matomo 正常运行（无法安装插件、更改配置等），因此需要手动设置访问某些文件的权限。 

下面的文件 `/etc/systemd/system/php-fpm.service.d/override_matomo.conf` 修复了这个问题，同时没有展示出更多非必要的内容，如果不希望这样做，仍然允许用户按照安装清单中的描述修改 ACL。 
    
    [Service]
    ReadWritePaths = /usr/share/webapps/matomo/config
    ReadWritePaths = /usr/share/webapps/matomo/matomo.js
    ReadWritePaths = /usr/share/webapps/matomo/misc/user/
    ReadWritePaths = /usr/share/webapps/matomo/plugins/

###  服务器设置 (nginx)

要启用 php 网站，请安装 [php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包 包和 [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `php-fpm.service`（参见 [Nginx#PHP implementation](<../zh-cn/Nginx.html#PHP_implementation> "Nginx")）。 

通过修改`/etc/nginx/nginx.conf`创建服务器。在 "http "上下文中添加以下模板。或者，看看 [matomo的GitHub](<https://github.com/matomo-org/matomo-nginx>) 说明。 
    
    include /etc/nginx/mime.types;
    
    server
    {
        index index.php;
        listen 443 ssl;
        listen [::]:443 ssl;
        root /usr/share/webapps/matomo/;
        server_name matomo.example.com;
    
        location ~ ^/(\.git/|config/|core/|lang/|tmp/)
        {
            return 403;
        }
    
        location ~ \.php$
        {
            try_files $uri =404;
    
            # FastCGI
            include fastcgi.conf;
            fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
            fastcgi_index index.php;
        }
    
        location ~ \.(avi|css|eot|gif|htm|html|ico|jpg|js|json|mp3|mp4|ogg|png|svg|ttf|wav|woff|woff2)$
        {
            try_files $uri =404;
        }
    
        location ~ ^/(libs/|misc/|node_modules/|plugins/|vendor/)
        {
            return 403;
        }
    }

要使用加密，您可以从 [letsencrypt](</wzh/index.php?title=Letsencrypt&action=edit&redlink=1> "Letsencrypt（页面不存在）") 获取免费证书。请求并安装证书后，通过将以下代码添加到 "http" 或 "server" 上下文以使用它们： 
    
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    ssl_certificate_key /etc/letsencrypt/live/subdomain.domain.me/privkey.pem;
    ssl_certificate /etc/letsencrypt/live/subdomain.domain.me/fullchain.pem;
    
通过[启动/启用](</wzh/index.php?title=Starting/enabling&action=edit&redlink=1> "Starting/enabling（页面不存在）") `nginx.service` 运行 nginx 服务器。 

**注意：**`mariadb.service` 以及 `php-fpm.service` 是必须的。

###  最后步骤

所有主要设置都完成了。在你的浏览器中调用你的 Matomo 网站，并完成次要安装指南——不外乎是检查所需的一切是否可用，并设置和编写你的配置文件。 
