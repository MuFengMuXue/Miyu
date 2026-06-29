**翻译状态：**

  * 本文（或部分内容）译自 [MediaWiki](<https://wiki.archlinux.org/title/MediaWiki> "arch:MediaWiki")，最近一次同步于 2024-08-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/MediaWiki?diff=0&oldid=794459>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MediaWiki_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MediaWiki](<https://www.mediawiki.org/wiki/MediaWiki> "mw:MediaWiki") 是一个自由、开源的维基软件，用 [PHP](<../zh-cn/PHP.html> "PHP") 写成；原本是为维基百科开发的。它也给 ArchWiki 和本维基提供了帮助。（详情查看 [Special:版本](<../Special:%E7%89%88%E6%9C%AC.html> "Special:版本")和 [GitHub 仓库](<https://github.com/archlinux/archwiki>)）。 

##  安装

为了运行 MediaWiki 你需要三个组件： 

  * [mediawiki](<https://archlinux.org/packages/?name=mediawiki>)包 包，[PHP](<../zh-cn/PHP.html> "PHP") 会作为它的依赖安装
  * 一个[网络服务器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1%E5%99%A8> "网络服务器")――例如 [Apache HTTP 服务器](<../zh-cn/Apache_HTTP_%E6%9C%8D%E5%8A%A1%E5%99%A8.html> "Apache HTTP 服务器")、[Nginx](<../zh-cn/Nginx.html> "Nginx") 和 [lighttpd](<../zh-cn/Lighttpd.html> "Lighttpd")
  * 一个数据库系统―― [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")、[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")、[SQLite](<../zh-cn/SQLite.html> "SQLite") 或 [MySQL](<../zh-cn/MySQL.html> "MySQL")

如果要在 [XAMPP](</wzh/index.php?title=XAMPP&action=edit&redlink=1> "XAMPP（页面不存在）") 上安装 MediaWiki，参见 [mw:Manual:Installing MediaWiki on XAMPP](<https://www.mediawiki.org/wiki/Manual:Installing_MediaWiki_on_XAMPP> "mw:Manual:Installing MediaWiki on XAMPP")

##  配置

实现一个可用的 MediaWiki 配置的步骤包括编辑 PHP 设置和添加 MediaWiki 配置片段。 

### PHP

MediaWiki 需要 `iconv` 和 `intl` 插件，所以需要把 `/etc/php/php.ini` 里面的 `extension=iconv` 和 `extension=intl` 取消注释。 

可选插件： 

  * 为了渲染缩略图，安装 [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick") 或者 [php-gd](<https://archlinux.org/packages/?name=php-gd>)包（二选一）。如果安装的是后者，需要取消注释 `extension=gd`。

启用你的数据库管理系统的 API： 

  * 如果是 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")，取消注释`extension=mysqli`。
  * 如果是 [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")，安装 [php-pgsql](<https://archlinux.org/packages/?name=php-pgsql>)包 并取消注释 `extension=pgsql`。
  * 如果是 [SQLite](<../zh-cn/SQLite.html> "SQLite")，安装 [php-sqlite](<https://archlinux.org/packages/?name=php-sqlite>)包 并取消注释 `extension=pdo_sqlite`。

其次，调整会话处理方式，否则可能会在寻找 `session.save_path` 路径时遇到严重错误（`PHP Fatal error: session_start(): Failed to initialize storage module[...]`）。`/var/lib/php/sessions` 或 `/tmp/` 路径是个不错的选择。 
    
    /etc/php/php.ini
    
    session.save_path = "/var/lib/php/sessions"

如果那个目录不存在，你要手动创建它，并更改权限： 
    
    # mkdir -p /var/lib/php/sessions/
    # chown http:http /var/lib/php/sessions
    # chmod go-rwx /var/lib/php/sessions
    
如果你使用了 [PHP's open_basedir](<../zh-cn/PHP.html#Configuration> "PHP") 并想[允许文件上传](<https://www.mediawiki.org/wiki/Manual:Configuring_file_uploads> "mw:Manual:Configuring file uploads")，你需要把 `/var/lib/mediawiki/` 添加到里面去 ([mediawiki](<https://archlinux.org/packages/?name=mediawiki>)包 为 `images/` 创建了指向 `/var/lib/mediawiki/` 的符号链接)。 

###  网站服务器

#### Apache

按照 [Apache HTTP Server#PHP](<../zh-cn/Apache_HTTP_Server.html#PHP> "Apache HTTP Server") 配置 PHP。 

复制 `/etc/webapps/mediawiki/apache.example.conf` 到 `/etc/httpd/conf/extra/mediawiki.conf` 并按需要修改它。 添加下面这一行到 `/etc/httpd/conf/httpd.conf`: 
    
    Include conf/extra/mediawiki.conf
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `httpd.service`。 

**注意：** 默认示例文件 `/etc/webapps/mediawiki/apache.example.conf` 会覆盖 PHP 的 open_basedir 设置，可能会和其他页面产生冲突。 可以通过把以 `php_admin_value` 开头的行移到 `<Directory>` 标签之间来避免这个问题。而如果你运行了多个依赖同一个 server 的应用，你可以把这个值添加到 `/etc/php/php.ini` 里的 open_basedir 里，而不仅仅是放在 `/etc/httpd/conf/extra/mediawiki.conf` 里。

#### Nginx

对于 [Nginx](<../zh-cn/Nginx.html> "Nginx")，请创建这样的一个文件： 
    
    /etc/nginx/mediawiki.conf
    
    location / {
       index index.php;
       try_files $uri $uri/ @mediawiki;
    }
    location @mediawiki {
       rewrite ^/(.*)$ /index.php;
    }
    location ~ \.php?$ {
       include /etc/nginx/fastcgi_params;
       fastcgi_pass unix:/var/run/php-fpm/php-fpm.sock;
       fastcgi_index index.php;
       fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
       try_files $uri @mediawiki;
    }
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
       try_files $uri /index.php;
       expires max;
       log_not_found off;
    }
    # Restrictions based on the .htaccess files
    location ~ ^/(cache|includes|maintenance|languages|serialized|tests|images/deleted)/ {
       deny all;
    }
    location ~ ^/(bin|docs|extensions|includes|maintenance|mw-config|resources|serialized|tests)/ {
       internal;
    }
    location ^~ /images/ {
       try_files $uri /index.php;
    }
    location ~ /\. {
       access_log off;
       log_not_found off; 
       deny all;
    }
    location /rest.php {
       try_files $uri $uri/ /rest.php?$args;
    }
    
请确保已经安装了 [php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包 并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")了 `php-fpm.service`。 

在`/etc/nginx/nginx.conf`添加一个 server 块，类似这样的： 
    
    /etc/nginx/nginx.conf
    
    server {
      listen 80;
      server_name mediawiki;
      root /usr/share/webapps/mediawiki;
      index index.php;
      charset utf-8;
    # For correct file uploads
      client_max_body_size    100m; # Equal or more than upload_max_filesize in /etc/php/php.ini
      client_body_timeout     60;
      include mediawiki.conf;
    
    }
    
最后，[restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `nginx.service` 和 `php-fpm.service`。 

#### Lighttpd

应当先安装并配置好 [Lighttpd](<../zh-cn/Lighttpd.html> "Lighttpd")。lighttpd 的 server.modules array 中需要“mod_alias“和“mod_rewrite“。将以下内容添加至 lighttpd 的配置文件： 
    
    /etc/lighttpd/lighttpd.conf
    
    alias.url += ("/mediawiki" => "/usr/share/webapps/mediawiki/")
    url.rewrite-once += (
                    "^/mediawiki/wiki/upload/(.+)" => "/mediawiki/wiki/upload/$1",
                    "^/mediawiki/wiki/$" => "/mediawiki/index.php",
                    "^/mediawiki/wiki/([^?]*)(?:\?(.*))?" => "/mediawiki/index.php?title=$1&$2"
    )
    
然后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `lighttpd.service` 守护进程。 

###  数据库

按照你所需要的数据库管理系统（DBMS）的文章配置数据库服务器：[MariaDB](<../zh-cn/MariaDB.html> "MariaDB")、[PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL")、[SQLite](<../zh-cn/SQLite.html> "SQLite") 或 [MySQL](<../zh-cn/MySQL.html> "MySQL")。 

如果数据库密码不为空，MediaWiki会自动创建数据库(设置 MariaDB 密码的方法在 [MariaDB#Reset the root password](<../zh-cn/MariaDB.html#Reset_the_root_password> "MariaDB")) 。否则你就需要手动创建数据库，详情参考： [upstream instructions](<https://www.mediawiki.org/wiki/Manual:Installing_MediaWiki#Create_a_database> "mw:Manual:Installing MediaWiki")。 

### LocalSettings.php

在浏览器里打开 wiki 的 URL (通常是 `http://_your_server_ /mediawiki/index.php`) 并进行初始化配置。参考[upstream instructions](<https://www.mediawiki.org/wiki/Manual:Config_script> "mw:Manual:Config script")的步骤。 

生成的 `LocalSettings.php` 文件是用来下载的，保存它到 `/usr/share/webapps/mediawiki/LocalSettings.php`。 

自 1.38.0 版本起，`/usr/share/webapps/mediawiki/LocalSettings.php` 内已包含一个符号链接。 

**警告：**[LocalSettings.php](<https://www.mediawiki.org/wiki/LocalSettings.php> "mw:LocalSettings.php") 包含了数据库连接设置（例如用户名和密码）和网络更新密码。请确保仅 root 和 http 用户可以访问 `/etc/webapps/mediawiki/LocalSettings.php` 文件： 
    
    # chown root:http /etc/webapps/mediawiki/LocalSettings.php
    # chmod 640 /etc/webapps/mediawiki/LocalSettings.php
    
该文件定义了所部署维基的特定设置。升级 [mediawiki](<https://archlinux.org/packages/?name=mediawiki>)包 软件包不会替换此文件。 

#### LDAP Auth

使用 [PluggableAuth](<https://www.mediawiki.org/wiki/Extension:PluggableAuth> "mw:Extension:PluggableAuth") 和 [LDAP Stack](<https://www.mediawiki.org/wiki/LDAP_Stack> "mw:LDAP Stack")。请留意“Compatibility Matrix”章节。目前 LDAP 仅能与 PluggableAuth-5.7 一同使用。 

请安装并在配置中添加 ldap stack 扩展和 PluggableAuth： 

  * [Extension:PluggableAuth](<https://www.mediawiki.org/wiki/Extension:PluggableAuth> "mw:Extension:PluggableAuth")
  * [Extension:LDAPProvider](<https://www.mediawiki.org/wiki/Extension:LDAPProvider> "mw:Extension:LDAPProvider")
  * [Extension:LDAPAuthentication2](<https://www.mediawiki.org/wiki/Extension:LDAPAuthentication2> "mw:Extension:LDAPAuthentication2")
  * [Extension:LDAPAuthorization](<https://www.mediawiki.org/wiki/Extension:LDAPAuthorization> "mw:Extension:LDAPAuthorization")
  * [Extension:LDAPUserInfo](<https://www.mediawiki.org/wiki/Extension:LDAPUserInfo> "mw:Extension:LDAPUserInfo")
  * [Extension:LDAPGroups](<https://www.mediawiki.org/wiki/Extension:LDAPGroups> "mw:Extension:LDAPGroups")

接下来请设置至少 3 个变量： 

  * `$LDAPProviderDomainConfigProvider`——整个 ldap 配置（可以是 json 文件）
  * `$wgPluggableAuth_Config`——auth 插件列表

    $wgPluggableAuth_Config = array(
           array('plugin' => 'LDAPAuthentication2'),
           array('plugin' => 'LDAPAuthorization'),
    );
    
  * 以及 `$LDAPProviderDefaultDomain`

配置完成后请运行 `php maintenance/update.php`。 

##  升级

参考 [mw:Manual:Upgrading](<https://www.mediawiki.org/wiki/Manual:Upgrading> "mw:Manual:Upgrading"), 不要忘记运行: 
    
    # cd /usr/share/webapps/mediawiki
    # php maintenance/update.php
    
##  提示和技巧

### Unicode

请确保[PHP](<../zh-cn/PHP.html> "PHP"), [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server") 和 [MariaDB](<../zh-cn/MariaDB.html> "MariaDB")都用的是 UTF-8 编码。否则可能遇到因为编码不匹配导致的奇怪bug。 

###  可视化编辑器

VisualEditor（可视化编辑器）扩展为 MediaWiki 提供了一个富文本编辑器。请参照 [mw:Extension:VisualEditor](<https://www.mediawiki.org/wiki/Extension:VisualEditor> "mw:Extension:VisualEditor") 安装。 
