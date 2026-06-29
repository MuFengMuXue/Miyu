# DokuWiki

From its website:
: DokuWiki is a simple to use and highly versatile Open Source wiki software that doesn't require a database. It is loved by users for its clean and readable syntax. The ease of maintenance, backup and integration makes it an administrator's favorite. Built in access controls and authentication connectors make DokuWiki especially useful in the enterprise context and the large number of plugins contributed by its vibrant community allow for a broad range of use cases beyond a traditional wiki.

See upstream for the detailed list of features.

DokuWiki should work on any web server which supports PHP.  As the requirements may change over time, you should consult the requirements page for DokuWiki for additional details.

It is strongly recommend to read through the appropriate sections of DokuWiki's security page for your web server.  Most popular web servers are covered but there are generic instructions as well.

## Installation
The package in the official repositories unpacks DokuWiki at  with the configuration files in  and the data files in . It also changes the ownership of the relevant files to the "http" user. This should work fine for most popular web servers as packaged for Arch.

# Install your web server of choice (e.g. Apache HTTP Server, nginx or lighttpd) and configure it for PHP.  As mentioned above, DokuWiki has no need for a database server so you may be able to skip those steps when setting up your web server.
# Install the  package.
# Configure web server for dokuwiki (see section below)
# With your web browser of choice, open http://&lt;your-server&gt;/dokuwiki/install.php and continue the installation from there. For nginx the URL is http://&lt;your-server&gt;/install.php.

Alternatively, if you would like to install from tarball, you can read from https://www.dokuwiki.org/Install.  Generally the procedure is the same as above.  Instead of using pacman, you will need to download the tarball, unpack it to your server's document root (e.g. ), and chown to the appropriate user (e.g. "http").

## Configuration
If you use PHP's open_basedir, you need to include the dokuwiki directories  and . For example:

Also uncomment the following line.

Dokuwiki needs this library for resizing images.

Then check that you have  installed and restart .

## Apache
The package should add the file  with the following contents:

If you are running Apache 2.4 or newer, you will have to change the following lines:

to read:

Include the newly created file in the Apache configuration by placing the following line at the end of :

Make sure the folders  and  are owned by user and group "http". You may relocate these directories if you like as long as you update the references in  respectively. You should keep the reference to  for DokuWiki to find the plugins and tpl folder.

Afterwards restart Apache.

Then finish the installation by running the dokuwiki/install.php script in your browser.

## lighttpd
Edit the  file as per the dokuwiki instructions (might contain updated information).

Make sure the modules  and  are loaded. If not, load them by adding the following to :

 provides the  command, which we are using from this point.

Under the line:
{{bc|1=
$HTTP=~ "\.pdf$" {
  server.range-requests = "disable"
}
}}

add this:
{{bc|1=
# subdir of dokuwiki
# comprised of the subdir of the root dir where dokuwiki is installed
# in this case the root dir is the basedir plus /htdocs/
# Note: be careful with trailing slashes when uniting strings.
# all content on this example server is served from htdocs/ up.
#var.dokudir = var.basedir + "/dokuwiki"
var.dokudir = server.document-root + "/dokuwiki"

# make sure those are always served through fastcgi and never as static files
# deny access completly to these
$HTTP["url" =~ "/(\.|_)ht" { url.access-deny = ( "" ) }
$HTTP=~ "^" + var.dokudir + "/(bin|data|inc|conf)/"  { url.access-deny = ( "" ) }
}}

These entries give some basic security to DokuWiki. lighttpd does not use .htaccess files like Apache. You CAN install with out this, but I would NEVER recommend it.

Add alias somewhere in lighttpd or fastcgi conf file:

Restart lighttpd.

## nginx
Ensure that  is installed and started.

Add the following server block, but change the server name to your own and comment out the install.php block until you are done installing DokuWiki. This block assumes you use TLS. [https://www.dokuwiki.org/install:nginx
{{hc|/etc/nginx/nginx.conf|
    server {
        listen 443 ssl http2;
        listen ssl http2;
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
            rewrite ^/_export/([^/+)/(.*) /doku.php?do=export_$1&id=$2 last;
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
}}

Restart nginx.

## Enable upload and displaying of SVG files
DokuWiki supports SVG files but has them disabled by default.

If you wish to enable them, create the following file:

This has security implications - see here

## Post installation
## Cleaning up
After configuring the server either remove the install.php file or make sure it is made inaccessible in your webserver configuration!
  # rm /usr/share/webapps/dokuwiki/install.php

## Installing plugins
Many community created plugins can be found here

They can be added through the web interface (as well as updated) through the Admin menu. Some plugins cannot be downloaded, if they go over ssl (e.g. git).

## Backing up
It is very trivial to backup DokuWiki, since there is no database. All pages are in plain text, and require only a simple tar, or rsync.

A quick breakdown of the directories of interest in the current (20180422_a-1) version:
  /usr/share/webapps/dokuwiki/data/  =>  All User Created Data
  /usr/share/webapps/dokuwiki/conf/  =>  Configuration settings

This may change in future releases, please consult the DokuWiki Backup FAQ for verification.
