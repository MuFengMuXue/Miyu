# Adminer

Adminer is a web-based database management tool written in PHP. It is possible to manage MySQL, PostgreSQL, Sqlite3, MS SQL, Oracle database and Elasticsearch.

It is a simpler alternative to PhpMyAdmin. You can find more pieces of information about this project at the official page or at Wikipedia.

## Installation
Install the  package or download Adminer and place it manually in the document-root instead.

When using the  package, Adminer will be installed as .

Ensure the correct extensions in  are uncommented, e.g.  should provide MySQL database management.

## Configuration
## Apache
Add the following line to :

 Include conf/extra/httpd-adminer.conf

Then restart your Apache HTTP Server daemon.

Adminer can now be accessed by browsing to http://localhost/adminer.

## Nginx
Create a server entry using  as :
{{hc|/etc/nginx/sites-available/adminer.conf|
server {
    listen 443 ssl http2;
    listen ssl http2;

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
}}

Symlink  to  and restart nginx.

## Hiawatha
Ensure that the PHP FastCGI interface is configured correctly.

Then add the following  block to your .
{{hc|head=/etc/hiawatha/hiawatha.conf|output=
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
}}

Then restart the .
