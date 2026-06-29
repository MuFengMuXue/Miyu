**翻译状态：**

  * 本文（或部分内容）译自 [PhpMyAdmin](<https://wiki.archlinux.org/title/PhpMyAdmin> "arch:PhpMyAdmin")，最近一次同步于 2021-03-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/PhpMyAdmin?diff=0&oldid=655234>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PhpMyAdmin_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[phpMyAdmin](<https://www.phpmyadmin.net/>)是一个基于网页的，帮助管理MySQL数据库的Apache/PHP前端。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [phpmyadmin](<https://archlinux.org/packages/?name=phpmyadmin>)包。 

##  运行

### PHP

确保PHP的[MySQL](<../zh-cn/PHP.html#MySQL/MariaDB> "PHP")扩展已经被启用。 

你也可以启用 `extension=bz2` 和 `extension=zip` 扩展以支持压缩。 

**注意：** 如果设置了`open_basedir`，`/usr/share/webapps` 和 `/etc/weppapps/` 必须加入到`/etc/php/php.ini` 中的`open_basedir`。参考 [PHP#配置](<../zh-cn/PHP.html#%E9%85%8D%E7%BD%AE> "PHP")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]。

### Apache

按照[Apache HTTP Server#PHP](<../zh-cn/Apache_HTTP_Server.html#PHP> "Apache HTTP Server")设置PHP。 创建Apache配置文件： 
    
    /etc/httpd/conf/extra/phpmyadmin.conf
    
    Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
    <Directory "/usr/share/webapps/phpMyAdmin">
        DirectoryIndex index.php
        AllowOverride All
        Options FollowSymlinks
        Require all granted
    </Directory>

在`/etc/httpd/conf/httpd.conf`加入配置文件： 
    
    # phpMyAdmin configuration
    Include conf/extra/phpmyadmin.conf
    
**注意：** 默认情况下，每个可以访问Web服务器的人都可以通过这个URL访问phpMyAdmin登录页面。要改变此设置，编辑`/etc/httpd/conf/extra/phpmyadmin.conf`。例如，你只想从本地访问phpMyAdmin，将`Require all granted`改为`Require local`。注意，这将禁止远程访问phpMyAdmin，如果你想安全地远程访问phpMyAdmin，你可以设置一个[加密的SOCKS通道](<../zh-cn/OpenSSH.html#Encrypted_SOCKS_tunnel> "OpenSSH")。

修改了 Apache 配置文件之后，[restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `httpd.service`。 

### Lighttpd

配置[Lighttpd](<../zh-cn/Lighttpd.html> "Lighttpd")，确保能正常使用PHP，并且启用`mod_alias`。 

在配置文件中为phpmyadmin加入下列alias： 
    
     alias.url = ( "/phpmyadmin" => "/usr/share/webapps/phpMyAdmin/")
    
### Nginx

确保正确配置[FastCGI](<../zh-cn/Nginx.html#FastCGI> "Nginx")，并使用 [nginx#Server blocks](<../zh-cn/Nginx.html#Server_blocks> "Nginx") 来使得管理更简单。 

####  子域名

根据个人喜好，通过子域名访问 phpMyAdmin, 如 `https://_pma.domain.tld_`： 
    
    /etc/nginx/sites-available/_pma.domain.tld_
    
    server {
        server_name _pma.domain.tld_ ;
        ; listen 80; # also listen on http
        ; listen [::]:80;
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        index index.php;
        access_log /var/log/nginx/pma.access.log;
        error_log /var/log/nginx/pma.error.log;
    
        # Allows limiting access to certain client addresses.
        ; allow 192.168.1.0/24;
        ; allow _my-ip_ ;
        ; deny all;
    
        root /usr/share/webapps/phpMyAdmin;
        location / {
            try_files $uri $uri/ =404;
        }
    
        error_page 404 /index.php;
    
        location ~ \.php$ {
            try_files $uri $document_root$fastcgi_script_name =404;
    
            fastcgi_split_path_info ^(.+\.php)(/.*)$;
            fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            include fastcgi_params;
    
            fastcgi_param HTTP_PROXY "";
            fastcgi_param HTTPS on;
            fastcgi_request_buffering off;
       }
    }

####  子目录

或者使用子目录，如 `https://_domain.tld_ /phpMyAdmin`： 
    
    /etc/nginx/sites-available/_domain.tld_
    
    server {
        server_name _domain.tld_ ;
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
        index index.php;
        access_log /var/log/nginx/domain.tld.access.log;
        error_log /var/log/nginx/domain.tld.error.log;
    
        root /srv/http/domain.tld;
        location / {
            try_files $uri $uri/ =404;
        }
    
        location /phpMyAdmin {
            root /usr/share/webapps/phpMyAdmin;
        }
    
        # Deny static files
        location ~ ^/phpMyAdmin/(README|LICENSE|ChangeLog|DCO)$ {
           deny all;
        }
    
        # Deny .md files
        location ~ ^/phpMyAdmin/(.+\.md)$ {
          deny all;
       }
    
       # Deny setup directories
       location ~ ^/phpMyAdmin/(doc|sql|setup)/ {
          deny all;
       }
    
       #FastCGI config for phpMyAdmin
       location ~ /phpMyAdmin/(.+\.php)$ {
          try_files $uri $document_root$fastcgi_script_name =404;
    
          fastcgi_split_path_info ^(.+\.php)(/.*)$;
          fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
          fastcgi_index index.php;
          fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
          include fastcgi_params;
    
          fastcgi_param HTTP_PROXY "";
          fastcgi_param HTTPS on;
          fastcgi_request_buffering off;
       }
    }
    
##  配置

主配置文件位于 `/usr/share/webapps/phpMyAdmin/config.inc.php`。 

###  定义远程 MySQL 服务器

如果[MySQL](<../zh-cn/MySQL.html> "MySQL")服务器不在本机上，添加如下行到配置文件: 
    
    $cfg['Servers'][$i]['host'] =  'example.com';
    
###  使用安装脚本

要使用phpMyAdmin安装脚本（例如 <http://localhost/phpmyadmin/setup> ），确保`http`用户可以写入`/usr/share/webapps/phpMyAdmin`。 
    
    # mkdir /usr/share/webapps/phpMyAdmin/config
    # chown http:http /usr/share/webapps/phpMyAdmin/config
    # chmod 750 /usr/share/webapps/phpMyAdmin/config
    
###  添加blowfish_secret passphrase

需要设置一个唯一的32位的字符串从而充分地使用blowfish算法，从而避免……（配置文件现在需要一个短语密码）的错误。 

(blowfish_secret)_:_
    
    /usr/share/webapps/phpMyAdmin/config.inc.php
    
    $cfg['blowfish_secret'] = '...';

###  启用配置存储

例如table linking,change tracking,PDF creation,bookmarking queries的附加功能默认是被禁用的，并且会提示The phpMyAdmin configuration storage is not completely configured, some extended features have been deactivated. 

**注意：** 下面的例子将`controluser`假设为**pma** ，`controlpass` 假设为**pmapass** 。

在`/usr/share/webapps/phpMyAdmin/config.inc.php`取消注释(移除开头的//)，并按需更改为所需的凭据： 
    
    /usr/share/webapps/phpMyAdmin/config.inc.php
    
    /* User used to manipulate with storage */
    // $cfg['Servers'][$i]['controlhost'] = 'my-host';
    // $cfg['Servers'][$i]['controlport'] = '3306';
    $cfg['Servers'][$i]['controluser'] = 'pma';
    $cfg['Servers'][$i]['controlpass'] = 'pmapass';
    
    /* Storage database and tables */
    $cfg['Servers'][$i]['pmadb'] = 'phpmyadmin';
    $cfg['Servers'][$i]['bookmarktable'] = 'pma__bookmark';
    $cfg['Servers'][$i]['relation'] = 'pma__relation';
    $cfg['Servers'][$i]['table_info'] = 'pma__table_info';
    $cfg['Servers'][$i]['table_coords'] = 'pma__table_coords';
    $cfg['Servers'][$i]['pdf_pages'] = 'pma__pdf_pages';
    $cfg['Servers'][$i]['column_info'] = 'pma__column_info';
    $cfg['Servers'][$i]['history'] = 'pma__history';
    $cfg['Servers'][$i]['table_uiprefs'] = 'pma__table_uiprefs';
    $cfg['Servers'][$i]['tracking'] = 'pma__tracking';
    $cfg['Servers'][$i]['userconfig'] = 'pma__userconfig';
    $cfg['Servers'][$i]['recent'] = 'pma__recent';
    $cfg['Servers'][$i]['favorite'] = 'pma__favorite';
    $cfg['Servers'][$i]['users'] = 'pma__users';
    $cfg['Servers'][$i]['usergroups'] = 'pma__usergroups';
    $cfg['Servers'][$i]['navigationhiding'] = 'pma__navigationhiding';
    $cfg['Servers'][$i]['savedsearches'] = 'pma__savedsearches';
    $cfg['Servers'][$i]['central_columns'] = 'pma__central_columns';
    $cfg['Servers'][$i]['designer_settings'] = 'pma__designer_settings';
    $cfg['Servers'][$i]['export_templates'] = 'pma__export_templates';

####  创建数据库

有两种方法来创建需要的表： 

  * 使用phpMyAdmin导入 `/usr/share/webapps/phpMyAdmin/sql/create_tables.sql`。
  * 在命令行中执行`mysql -u root -p < /usr/share/webapps/phpMyAdmin/sql/create_tables.sql`。

####  创建数据库用户

要赋予`controluser`所需的权限，执行如下的查询： 

**注意：** 确保将所有的`pma`和`pmapass`替换为在`config.inc.php`设置的值。如果正在为远程数据库配置，还需将`localhost`改为适当的主机。
    
    GRANT USAGE ON mysql.* TO 'pma'@'localhost' IDENTIFIED BY 'pmapass';
    GRANT SELECT (
        Host, User, Select_priv, Insert_priv, Update_priv, Delete_priv,
        Create_priv, Drop_priv, Reload_priv, Shutdown_priv, Process_priv,
        File_priv, Grant_priv, References_priv, Index_priv, Alter_priv,
        Show_db_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv,
        Execute_priv, Repl_slave_priv, Repl_client_priv
        ) ON mysql.user TO 'pma'@'localhost';
    GRANT SELECT ON mysql.db TO 'pma'@'localhost';
    GRANT SELECT ON mysql.host TO 'pma'@'localhost';
    GRANT SELECT (Host, Db, User, Table_name, Table_priv, Column_priv)
        ON mysql.tables_priv TO 'pma'@'localhost';
    
为了使用书签和关系特性，设置如下的权限： 
    
    GRANT SELECT, INSERT, UPDATE, DELETE ON phpmyadmin.* TO 'pma'@'localhost';
    
重新登录以启用新特性。 

###  启用templates catching

在`/usr/share/webapps/phpMyAdmin/config.inc.php`添加如下行： 
    
     $cfg['TempDir'] = '/tmp/phpmyadmin'
    
###  移除配置目录

当配置完成之后，可以移除临时配置目录，这也会抑制来自网页交互的警告： 
    
    # rm -r /usr/share/webapps/phpMyAdmin/config
    
###  安装主题

主题的位置在 `/usr/share/webapps/phpMyAdmin/themes`。你可以在 <https://www.phpmyadmin.net/themes/> 找到新主题。 

直接下载并将主题提取到相应位置，在 phpmyadmin 刷新之后它将正常工作。然而，你下载的主题必须与 phpmyadmin 的版本相对应，适用于老版本的主题无法使用。 

##  参见

  * [Wikipedia](<https://en.wikipedia.org/wiki/phpMyAdmin> "wikipedia:phpMyAdmin")
  * [Official website](<https://www.phpmyadmin.net/>)
