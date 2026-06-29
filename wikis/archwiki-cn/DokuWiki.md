**翻译状态：**

  * 本文（或部分内容）译自 [DokuWiki](<https://wiki.archlinux.org/title/DokuWiki> "arch:DokuWiki")，最近一次同步于 2024-9-2，若英文版本有所[更改](<https://wiki.archlinux.org/title/DokuWiki?diff=0&oldid=815765>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/DokuWiki_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自其[网站](<https://www.dokuwiki.org/zh:dokuwiki>): 

    DokuWiki 是一个简单易用、用途多样并且不依赖数据库的开源维基软件。它因简洁易读的语法受到用户的喜爱。而容易维护、备份方便和易于整合则使它成为管理员的最爱。内置的访问控制和认证管理使 DokuWiki 在企业环境下特别适合，而由充满活力的社区贡献的众多插件对其功能的扩充则令它拥有了比传统维基更广阔的应用。

See upstream for the detailed list of [features](<https://www.dokuwiki.org/features>). 

DokuWiki should work on any web server which supports PHP. As the requirements may change over time, you should consult the [requirements page](<https://www.dokuwiki.org/requirements>) for DokuWiki for additional details. 

It is strongly recommend to read through the appropriate sections of [DokuWiki's security page](<https://www.dokuwiki.org/security>) for your web server. Most popular web servers are covered but there are generic instructions as well. 

## Installation

The package in the [official repositories](<../zh-cn/Official_repositories.html> "Official repositories") unpacks DokuWiki at `/usr/share/webapps/dokuwiki` with the configuration files in `/etc/webapps/dokuwiki` and the data files in `/var/lib/dokuwiki/data`. It also changes the ownership of the relevant files to the "http" user. This should work fine for most popular web servers as packaged for Arch. 

  1. Install your web server of choice (e.g. [Apache HTTP Server](<../zh-cn/Apache_HTTP_Server.html> "Apache HTTP Server"), [nginx](<../zh-cn/Nginx.html> "Nginx") or [lighttpd](<../zh-cn/Lighttpd.html> "Lighttpd")) and configure it for [PHP](<../zh-cn/PHP.html> "PHP"). As mentioned above, DokuWiki has no need for a database server so you may be able to skip those steps when setting up your web server.
  2. [Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [dokuwiki](<https://archlinux.org/packages/?name=dokuwiki>)包 package.
  3. Configure web server for dokuwiki (see section below)
  4. With your web browser of choice, open http://<your-server>/dokuwiki/install.php and continue the installation from there. For nginx the URL is http://<your-server>/install.php.

Alternatively, if you would like to install from tarball, you can read from <https://www.dokuwiki.org/Install>. Generally the procedure is the same as above. Instead of using pacman, you will need to [download the tarball](<https://www.splitbrain.org/projects/dokuwiki>), unpack it to your server's document root (e.g. `/srv/http/dokuwiki`), and chown to the appropriate user (e.g. "http"). 

## Configuration

If you use [PHP's open_basedir](<../zh-cn/PHP.html#Configuration> "PHP"), you need to include the dokuwiki directories `/etc/webapps/dokuwiki/` and `/var/lib/dokuwiki/`. For example: 
    
    /etc/php/php.ini
    
    open_basedir = _< other paths>_:/etc/webapps/dokuwiki/:/var/lib/dokuwiki/

Also uncomment the following line. 
    
    /etc/php/php.ini
    
    extension=gd
    
Dokuwiki needs this library for resizing images. 

Then check that you have [php-gd](<https://archlinux.org/packages/?name=php-gd>)包 installed and restart `php-fpm.service`. 

### Apache

The package should add the file `/etc/httpd/conf/extra/dokuwiki.conf` with the following contents: 
    
    /etc/httpd/conf/extra/dokuwiki.conf
    
    Alias /dokuwiki /usr/share/webapps/dokuwiki
    <Directory /usr/share/webapps/dokuwiki/>
        Options +FollowSymLinks
        AllowOverride All
        order allow,deny
        allow from all
        php_admin_value open_basedir "/tmp/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps/dokuwiki/:/var/lib/dokuwiki/"
    </Directory>
    
If you are running [Apache 2.4 or newer](<https://httpd.apache.org/docs/2.4/upgrading.html>), you will have to change the following lines: 
    
    /etc/httpd/conf/extra/dokuwiki.conf
    
        order allow,deny
        allow from all
    
to read: 
    
    /etc/httpd/conf/extra/dokuwiki.conf
    
        Require all granted
    
Include the newly created file in the Apache configuration by placing the following line at the end of `/etc/httpd/conf/httpd.conf`: 
    
    /etc/httpd/conf/httpd.conf
    
    Include conf/extra/dokuwiki.conf
    
Make sure the folders `/etc/webapps/dokuwiki` and `/var/lib/dokuwiki` are owned by user and group "http". You may relocate these directories if you like as long as you update the references in `/etc/httpd/conf/extra/dokuwiki.conf` respectively. You should keep the reference to `/var/lib/dokuwiki/` for DokuWiki to find the plugins and tpl folder. 

Afterwards [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") Apache. 

Then finish the installation by running the _dokuwiki/install.php_ script in your browser. 

### lighttpd

Edit the `/etc/lighttpd/lighttpd.conf` file as per the [dokuwiki instructions](<https://www.dokuwiki.org/install:lighttpd>) (might contain updated information). 

Make sure the modules `mod_access` and `mod_alias` are loaded. If not, load them by adding the following to `/etc/lighttpd/lighttpd.conf`: 
    
    server.modules += ("mod_access")
    server.modules += ("mod_alias")

`mod_access` provides the `url.access-deny` command, which we are using from this point. 

Under the line: 
    
    $HTTP["url"] =~ "\.pdf$" {
      server.range-requests = "disable"
    }

add this: 
    
    # subdir of dokuwiki
    # comprised of the subdir of the root dir where dokuwiki is installed
    # in this case the root dir is the basedir plus /htdocs/
    # Note: be careful with trailing slashes when uniting strings.
    # all content on this example server is served from htdocs/ up.
    #var.dokudir = var.basedir + "/dokuwiki"
    var.dokudir = server.document-root + "/dokuwiki"
    
    # make sure those are always served through fastcgi and never as static files
    # deny access completly to these
    $HTTP["url"] =~ "/(\.|_)ht" { url.access-deny = ( "" ) }
    $HTTP["url"] =~ "^" + var.dokudir + "/(bin|data|inc|conf)/"  { url.access-deny = ( "" ) }

_These entries give some basic security to DokuWiki._ lighttpd does not use .htaccess files like Apache. You CAN install with out this, but I would NEVER recommend it. 

Add alias somewhere in lighttpd or fastcgi conf file: 
    
    alias.url += ("/dokuwiki" => "/usr/share/webapps/dokuwiki/")

[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") lighttpd. 

### nginx

Ensure that [php-fpm](<https://archlinux.org/packages/?name=php-fpm>)包 is installed and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")ed. 

Add the following server block, but change the server name to your own and comment out the install.php block until you are done installing DokuWiki. This block assumes you use TLS. [[1]](<https://www.dokuwiki.org/install:nginx>)
    
    /etc/nginx/nginx.conf
    
        server {
            listen 443 ssl http2;
            listen [::]:443 ssl http2;
            server_name wiki.example.com;
             
            root /usr/share/webapps/dokuwiki;
            index doku.php;
    
            #Remember to comment the below out when you are installing DokuWiki, and uncomment it when you are done.
            location ~ /(data/|conf/|bin/|inc/|install.php) { deny all; } # secure Dokuwiki
    
            location ~^/\.ht { deny all; } # also secure the Apache .htaccess files
            location @dokuwiki {
                #rewrites "doku.php/" out of the URLs if you set the userewrite setting to .htaccess in dokuwiki config page
                rewrite ^/_media/(.*) /lib/exe/fetch.php?media=$1 last;
                rewrite ^/_detail/(.*) /lib/exe/detail.php?media=$1 last;
                rewrite ^/_export/([^/]+)/(.*) /doku.php?do=export_$1&id=$2 last;
                rewrite ^/(.*) /doku.php?id=$1&$args last;
            }
    
            location / { try_files $uri $uri/ @dokuwiki; }
            location ~ \.php$ {
                try_files $uri =404;
                fastcgi_pass unix:/run/php-fpm7/php-fpm.sock;
                fastcgi_index index.php;
                include fastcgi.conf;
            }
    
        }
    
[Restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") nginx. 

### Enable upload and displaying of SVG files

DokuWiki supports SVG files but has them disabled by default. 

If you wish to enable them, create the following file: 
    
    /etc/webapps/dokuwiki/mime.local.conf
    
    svg image/svg+xml
    
This has security implications - [see here](<https://github.com/splitbrain/dokuwiki/issues/1045#issuecomment-90226230>)

## Post installation

### Cleaning up

**After configuring the server either remove the install.php file or make sure it is made inaccessible in your webserver configuration!**
    
     # rm /usr/share/webapps/dokuwiki/install.php
    
### Installing plugins

Many community created plugins can be found [here](<https://www.dokuwiki.org/plugins>)

They can be added through the web interface (as well as updated) through the Admin menu. Some plugins cannot be downloaded, if they go over ssl (e.g. git). 

### Backing up

It is very trivial to backup DokuWiki, since there is no database. All pages are in plain text, and require only a simple tar, or [rsync](<../zh-cn/Rsync.html> "Rsync"). 

A quick breakdown of the directories of interest in the current (20180422_a-1) version: 
    
     /usr/share/webapps/dokuwiki/data/  =>  All User Created Data
     /usr/share/webapps/dokuwiki/conf/  =>  Configuration settings
    
This may change in future releases, please consult the [DokuWiki Backup FAQ](<https://www.dokuwiki.org/faq:backup>) for verification. 

## Further reading

The [DokuWiki main site](<https://www.dokuwiki.org/>) has all of the information and help that you could possibly need. 
