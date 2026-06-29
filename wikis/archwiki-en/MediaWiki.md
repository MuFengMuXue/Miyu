# MediaWiki

MediaWiki is a free and open source wiki software written in PHP, originally developed for Wikipedia. MediaWiki also powers this wiki—see also the archwiki repository.

## Installation
To run MediaWiki you need three things:

* the  package, which pulls in PHP,
* a web server—such as Apache HTTP Server, lighttpd or nginx,
* a database system—one of MariaDB, MySQL, PostgreSQL, or SQLite.

To install MediaWiki on XAMPP, see .

## Configuration
The steps to achieve a working MediaWiki configuration involve editing the PHP settings and adding the MediaWiki configuration snippets.

## PHP
MediaWiki requires the  and the  extensions, so you need to uncomment  and  in .

Optional dependencies:

* For thumbnail rendering, install either ImageMagick or . If you choose the latter, you also need to uncomment .

Enable the API for your DBMS:

* If you use MariaDB, uncomment .
* If you use PostgreSQL, install  and uncomment .
* If you use SQLite, install  and uncomment .

Second, tweak the session handling or you might get a fatal error () by finding the  path. A good choice can be  or .

You will need to create the directory if it does not exist and then restrict its permissions:

 # mkdir -p /var/lib/php/sessions/
 # chown http:http /var/lib/php/sessions
 # chmod go-rwx /var/lib/php/sessions

If you use PHP's open_basedir and want to , you need to include  ( symlinks  to ).

## Web server
## Apache
Follow Apache HTTP Server#PHP.

Copy  to  and edit it as needed.

Add the following line to :

 Include conf/extra/mediawiki.conf

Restart the  daemon.

## Nginx
To get MediaWiki working with Nginx, create the following file:

{{hc|/etc/nginx/mediawiki.conf|
location / {
   index index.php;
   try_files $uri $uri/ @mediawiki;
}
location @mediawiki {
   rewrite ^/(.*)$ /index.php;
}
location ~ \.php$ {
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
}}

Ensure that  is installed and  is started.

Include a server directive, similar to this

{{hc|/etc/nginx/nginx.conf|
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
}}

Finally, restart  and  daemons.

## Lighttpd
You should have Lighttpd installed and configured. "mod_alias" and "mod_rewrite" in server.modules array of lighttpd is required. Append to the lighttpd configuration file the following lines

Restart the  daemon.

## Database
Set up a database server as explained in the article of your DBMS: MariaDB, PostgreSQL, SQLite or MySQL.

If you have set a non-empty root password for the database server, MediaWiki can automatically create the database during the next step. (See MariaDB#Reset the root password for how to set this password retrospectively for MariaDB.)  Otherwise the database needs to be created manually - see .

## Wiki setup
Now you need to set up your wiki by creating its database tables and configuration file, . There are two methods: from command line and from browser, the former being safer because it doesn't require you to expose the installer.

This file defines the specific settings of your wiki. Whenever you upgrade the  package, it will not be replaced.

## From command line
The install script has a lot of parameters, refer to  for full details. Here is a basic example:

 # cd /etc/webapps/mediawiki/
 # php maintenance/run.php install \
     --dbname=wikidb \
     --dbserver="localhost" \
     --installdbuser=root \
     --installdbpass=rootpassword \
     --dbuser=dbusername \
     --dbpass=dbuserpassword \
     --server="http://wiki.example.com/" \
     --scriptpath=/w \
     --lang=en \
     --pass=Adminpassword "Wiki Name" "Admin account name"

## From browser
Open the wiki URL (usually ) in a browser and do the initial configuration. Follow .

The generated  file is offered for download, save it to .

Since 1.38.0 it has a symbolic link included in .

## LDAP Auth
Use  and . Pay attention to "Compatibility Matrix" section. Currently LDAP works only with PluggableAuth-5.7.

You need to install and add to config ldap stack extensions and PluggableAuth:

*
*
*
*
*
*

Then set up at least 3 variables:

*  - whole ldap config (can be in json file)
*  - list of auth plugins
 $wgPluggableAuth_Config = array(
        array('plugin' => 'LDAPAuthentication2'),
        array('plugin' => 'LDAPAuthorization'),
 );
* and

Do not forget to run  after configuration.

## Short URL
Short URL feature allows the wiki articles to be accessed in SEO-friendly structure (like ).

Below assumes that the URL structure used will be , where  is the article name.

## Apache
Add rewrite rules to :

{{bc|
RewriteEngine On

# Short URL for wiki pages
RewriteRule ^/?wiki(/.*)?$ %{DOCUMENT_ROOT}/w/index.php # Redirect / to Main Page
RewriteRule ^/*$ %{DOCUMENT_ROOT}/w/index.php [L
}}

Restart .

## Nginx
Add rewrite rules to :

{{bc|
# Handling for Mediawiki REST API, see
location /rest.php/ {
	try_files $uri $uri/ /w/rest.php?$query_string;
}

# Handling for the article path (pretty URLs)
location /wiki/ {
	rewrite ^/wiki/(?.*)$ /index.php;
}

# Explicit access to the root website, redirect to main page (adapt as needed)
location  / {
	return 301 /wiki/Main_Page;
}
}}

Restart .

## LocalSettings.php
Append to :

You may also want to rewrite the article's page action URLs. To do so, append below instead:

{{bc|
## Use "/wiki/$action/$1" for page actions
$actions  [
	'view',
	'edit',
	'watch',
	'unwatch',
	'delete',
	'revert',
	'rollback',
	'protect',
	'unprotect',
	'markpatrolled',
	'render',
	'submit',
	'history',
	'purge',
	'info',
];

foreach ( $actions as $action ) {
  $wgActionPaths"/wiki/$action/$1";
}

# Keep "/wiki/$1" for viewing articles
$wgActionPaths['view'  "/wiki/$1";
$wgArticlePath  $wgActionPaths'view';
$wgUsePathInfo  true;
}}

## Upgrading
See , and do not forget to run:

 # cd /usr/share/webapps/mediawiki
 # php maintenance/run.php update

## Tips and tricks
## Unicode
Check that PHP, Apache HTTP Server and MariaDB all use UTF-8. Otherwise you may face strange bugs because of encoding mismatch.

## VisualEditor
The VisualEditor MediaWiki extension provides a rich-text editor for MediaWiki. Follow  to install it.
