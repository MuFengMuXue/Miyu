**翻译状态：**

  * 本文（或部分内容）译自 [Adminer](<https://wiki.archlinux.org/title/Adminer> "arch:Adminer")，最近一次同步于 2024-8-4，若英文版本有所[更改](<https://wiki.archlinux.org/title/Adminer?diff=0&oldid=813746>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Adminer_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Adminer](<https://www.adminer.org/>) 是一个用 PHP 编写的基于网络的数据库管理工具。它可以管理 [MySQL](<../zh-cn/MySQL.html> "MySQL")、[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")、[Sqlite3](<../zh-cn/SQLite.html> "Sqlite3")、MS SQL、Oracle 数据库和 [Elasticsearch](<../zh-cn/Elasticsearch.html> "Elasticsearch")。 

它是 [PhpMyAdmin](<../zh-cn/PhpMyAdmin.html> "PhpMyAdmin") 的一个更简单的替代方案。你可以在[官方网站页](<https://www.adminer.org/en/>)或 [Wikipedia](<https://en.wikipedia.org/wiki/Adminer> "wikipedia:Adminer") 找到更多关于这个项目的信息。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [adminer](<https://aur.archlinux.org/packages/adminer/>)AUR 软件包或[下载 Adminer](<https://www.adminer.org/#download>)，然后将其手动放置在 document-root 中。 

使用 [adminer](<https://aur.archlinux.org/packages/adminer/>)AUR 软件包时，Adminer 将安装为 `/usr/share/webapps/adminer/index.php`。 

确保未注释 `/etc/php/php.ini` 中的正确扩展，例如，`extension=pdo_mysql` 会提供 [MySQL](<../zh-cn/MySQL.html> "MySQL") 数据库管理。 

##  配置

### Apache

**注意：** 确保[Apache 的 PHP 扩展](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html#PHP> "Apache HTTP 服务器")已正确配置

在 ` /etc/httpd/conf/httpd.conf` 中添加以下一行： 
    
    Include conf/extra/httpd-adminer.conf
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")你的 [Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")守护进程。 

现在可以通过浏览 <http://localhost/adminer> 访问 Adminer。 

### Nginx

**注意：** 确保已正确配置[PHP FastCGI 接口](<../zh-cn/Nginx.html#FastCGI> "Nginx")。

以 `root` 权限使用`/usr/share/webapps/adminer` 创建 [server entry](<../zh-cn/Nginx.html#Managing_server_entries> "Nginx")： 
    
    /etc/nginx/sites-available/adminer.conf
    
    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
    
        server_name adminer.domain;
        root /usr/share/webapps/adminer;
    
        # Only allow certain IPs 
        #allow 192.168.1.0/24;
        #deny all;
    
        index index.php;
    
        location / {
            try_files $uri $uri/ =404;
        }
    
        error_page 404 /index.php;
    
        # PHP configuration
        location ~ \.php$ {
          ...
        }
    }
    
将 `adminer.conf` 符号链接到 `sites-enabled` 并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") [nginx](<../zh-cn/Nginx.html> "Nginx")。 

### Hiawatha

确保正确配置[PHP FastCGI 接口](</wzh/index.php?title=Hiawatha&action=edit&redlink=1> "Hiawatha（页面不存在）")。 

然后在 `/etc/hiawatha/hiawatha.conf` 中添加以下 `VirtualHost` 块。 
    
    /etc/hiawatha/hiawatha.conf
    
    VirtualHost {
    
        # If you set WebsiteRoot to /usr/share/webapps/adminer you do not need followsymlinks
        # I symlinked the adminer folder to '/srv/http/adminer' so that I can easily remember where it's located but
        # still set 'WebsiteRoot' to the real source directory. You could point WebsiteRoot to the
        # symlinked directory, but you will have to set 'FollowSymlinks = yes' for that to function properly
    
        Hostname = db.domainname.dom
        #FollowSymlinks = yes
        #WebsiteRoot = /srv/http/adminer
        WebsiteRoot = /usr/share/webapps/adminer
        AccessLogfile = /var/log/hiawatha/adminer/access.log
        ErrorLogfile = /var/log/hiawatha/adminer/error.log
        StartFile = index.php
        UseFastCGI = PHP7
    
    }

然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `hiawatha.service`。 

##  参见

  * [Official Adminer 网页](<https://www.adminer.org/en/>)
  * [Author's weblog](<https://php.vrana.cz/>)
