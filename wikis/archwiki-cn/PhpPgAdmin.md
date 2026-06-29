相关文章

  * [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")

**翻译状态：**

  * 本文（或部分内容）译自 [PhpPgAdmin](<https://wiki.archlinux.org/title/PhpPgAdmin> "arch:PhpPgAdmin")，最近一次同步于 2024-7-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/PhpPgAdmin?diff=0&oldid=817614>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PhpPgAdmin_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[phpPgAdmin](<https://github.com/phppgadmin/phppgadmin>) 是一个基于网络的工具，可帮助使用 PHP 前端管理 PostgreSQL 数据库。 

##  安装

PhpPgAdmin 需要一个带 PHP 的网络服务器，如 Apache。要设置它，请参阅[Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")和[Apache HTTP 服务器#PHP](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html#PHP> "Apache HTTP 服务器")。 

安装 [phppgadmin](<https://aur.archlinux.org/packages/phppgadmin/>)AUR 软件包。 

##  配置

### PHP

您需要编辑 `/etc/php/php.ini`，取消注释以下一行，以启用 PHP 中的 `pgsql` 扩展： 
    
    extension=pgsql
    
您需要确保 PHP 可以访问 `/etc/webapps`。如有必要，请将其添加到 `/etc/php/php.ini` 中的 `open_basedir`： 
    
    open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps
    
###  网络服务器

#### Apache

创建 Apache 配置文件： 
    
    /etc/httpd/conf/extra/phppgadmin.conf
    
    Alias /phppgadmin "/usr/share/webapps/phppgadmin"
    <Directory "/usr/share/webapps/phppgadmin">
        DirectoryIndex index.php
        AllowOverride All
        Options FollowSymlinks
        Require all granted
    
        # phppgadmin raises deprecated warnings that lead
        # to parsing errors in JS
        #php_flag display_startup_errors off
        #php_flag display_errors off
        #php_flag html_errors off
    </Directory>
    
并将其包含在 `/etc/httpd/conf/httpd.conf` 中： 
    
    # phpPgAdmin configuration
    Include conf/extra/phppgadmin.conf
    
您还需要连接 php7： 
    
    Include conf/extra/php7_module.conf
    LoadModule php7_module modules/libphp7.so
    
默认情况下，每个人都能看到 phpPgAdmin 页面，若要更改，请编辑 `/etc/httpd/conf/extra/phppgadmin.conf` 以满足您的需求。例如，如果只希望在同一台机器上访问，请将 `Require all granted` 替换为 `Require local`。 

#### Lighttpd

lighttpd 的 php 设置与 apache 完全相同。 在 lighttpd 配置中为 phppgadmin 设置一个别名。 
    
     alias.url = ( "/phppgadmin" => "/usr/share/webapps/phppgadmin/")
    
然后在配置（server.modules 部分）中启用 mod_alias、mod_fastcgi 和 mod_cgi。 

确保 lighttpd 已设置为服务 php 文件，[Lighttpd#FastCGI](<../zh-cn/Lighttpd.html#FastCGI> "Lighttpd")。 

重启 lighttpd 并浏览 <http://localhost/phppgadmin/index.php> 。 

#### nginx

请确保按照 [nginx#nginx 配置](<../zh-cn/Nginx.html#nginx_%E9%85%8D%E7%BD%AE> "Nginx")中的说明，为 PHP 设置 [nginx#FastCGI](<../zh-cn/Nginx.html#FastCGI> "Nginx") 和单独的配置文件。 

使用此方法，您将以 `phppgadmin.<domain>` 的身份访问 PhpPgAdmin。 

您可以使用服务器块设置子域（或域），如 
    
    server {
        server_name     phppgadmin.<domain.tld>;
        root    /usr/share/webapps/phppgadmin;
        index   index.php;
        include php.conf;
    }
    
###  phpPgAdmin 配置

phpPgAdmin 的配置文件位于 `/etc/webapps/phppgadmin/config.inc.php`。 

如果 PostgreSQL 服务器位于 `localhost`，则可能需要编辑以下一行： 
    
    $conf['servers'][0]['host'] = _;_
    
到： 
    
    $conf['servers'][0]['host'] = 'localhost';
    
##  访问 phpPgAdmin 安装

phpPgAdmin 安装完成。在开始使用之前，您需要通过[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `httpd.service` 以重启 apache 服务器。 

您可以通过 <http://localhost/phppgadmin/> 访问 phpPgAdmin 安装。 

##  问题解决

###  由于安全原因，登录被禁止

如果 extra_login_security 设置为 "true"，那么通过 phpPgAdmin 进行的无密码登录或特定用户名（ _psql_ 、 _postgres_ 、 _root_ 、 _administrator_ ）登录将被拒绝。只有在阅读了常见问题并了解如何修改 PostgreSQL 的 `pg_hba.conf` 以启用带密码的本地连接之后，才能将此设置为 `false`。 

编辑 `/etc/webapps/phppgadmin/config.inc.php` 并更改以下行： 
    
    $conf['extra_login_security'] = true;
    
到： 
    
    $conf['extra_login_security'] = false;
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `postgresql.service`。 
