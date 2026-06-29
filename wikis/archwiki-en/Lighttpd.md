# Lighttpd

"lighttpd (pronounced /lighty/) is a secure, fast, standards compliant, and very flexible web server that has been optimized for high-performance environments. lighttpd supports a wide variety of features while using memory and CPU efficiently, making lighttpd an ideal web server for all systems, small and large."

## Installation
Install the  package.

## Configuration
## Basic setup
The lighttpd configuration file is: . By default it should produce a working test page.

To check your  for bugs you can use this command (helps finding misconfigurations very quickly):

 $ lighttpd -tt -f /etc/lighttpd/lighttpd.conf

The default configuration file specifies  as the document directory served. To test the installation, create a dummy file:

Then start/enable the  and point your browser to , where you should see the test page.

Example configuration files are available in .

## Basic logging
lighttpd can write out both errors and access to log files. The error log is enabled by default (controlled by the  option). To enable the access log, edit  as follows:

 server.modules += (
    "mod_accesslog",
 )

 accesslog.filename = "/var/log/lighttpd/access.log"

## Enabling https via SSL
## Self-signed
Self-signed SSL Certificates can be generated assuming  is installed on the system as follows:
 # mkdir /etc/lighttpd/certs
 # openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -sha256 -keyout /etc/lighttpd/certs/server.pem -out /etc/lighttpd/certs/server.pem
 # chmod 600 /etc/lighttpd/certs/server.pem

Modify  adding the following lines to enable https:

 server.modules += ( "mod_openssl" )

 $SERVER== ":443" {
    ssl.engine                  = "enable"
    ssl.pemfile                 = "/etc/lighttpd/certs/server.pem"
 }

See [https://redmine.lighttpd.net/projects/lighttpd/wiki/Docs_SSL lighttpd TLS configuration for details.

## Let's Encrypt
Alternatively, generate a certificate signed by Let's Encrypt.

Edit  by adding the following lines:

 $SERVER== ":443" {
     ssl.engine                  = "enable"
     ssl.privkey                 = "/etc/letsencrypt/live/domain/privkey.pem"
     ssl.pemfile                 = "/etc/letsencrypt/live/domain/fullchain.pem"
 }

See [https://redmine.lighttpd.net/projects/lighttpd/wiki/HowToSimpleSSL bootstrap Let's Encrypt in the lighttpd documentation for details.

## Redirect http requests to https
You should add  in server.modules array in :

{{bc|
server.modules += ( "mod_redirect" )

$HTTP== "http" {
  url.redirect = ("" => "https://${url.authority}${url.path}${qsa}")
}

$SERVER["socket" == ":443" {
  ssl.engine = "enable"
  ssl.pemfile = "/etc/lighttpd/certs/server.pem"
  server.document-root = "..."
}
}}

To redirect all hosts for part of the site (e.g. secure or phpmyadmin):

{{bc|
$HTTP=~ "^/secure" {
  $HTTP["scheme" == "http" {
    url.redirect = ("" => "https://${url.authority}${url.path}${qsa}")
  }
}
}}

## Password protecting a directory
A passwd file which is lighttpd's equivalent to the system's  is needed for user authentication.  The setup requires a specific format and md5sum hashed password but users can quickly and easily create an entry using the following as an example:

 $ user=foo
 $ password=b@R102
 $ realm='Password Required'
 $ hash=`echo -n "$user:$realm:$password" | md5sum | cut -b -32`

 # echo "$user:$realm:$hash" >> /etc/lighttpd/lighttpd.user

Modify  adding the following lines to enable the directory protection:

 server.modules += ( "mod_auth", "mod_authn_file" )

 auth.backend = "htdigest"
 auth.backend.htdigest.userfile = "/etc/lighttpd/lighttpd.user"

 # note this entry is relative to the server.document-root
 auth.require = ( "/secret" =>
    (
     "method" => "basic",
     "realm" => "Password Required",
     "require" => "valid-user"
    )
 )

## Block AI crawlers
Insert this into your configuration, ideally after retrieving an up-to-date match for known AI crawlers from the ai.robots.txt project. This will filter out some old browsers (likely bots) and any useragent claiming to be a browser but not supporting modern browser HTTP headers. Non-browser useragents like curl/wget are allowed.

 # Regex for URLs that are always allowed
 var.allowURLs = "^(/robots\.txt|/favicon\.ico|/\.well-known/)"
 # Allow bots that declare themselves as such
 var.allowBotUA = "(?i)bot|spider|crawl"
 # Block old browsers (Chrome/Firefox  "/blocked.html" ) }}. Your custom error page could include an option to set a cookie if the user is human, and disable the block by appending:

 $HTTP=~ "human=true" {
   url.access-deny = ()
   url.rewrite-once = ()
 }

## CGI
Common Gateway Interface (CGI) scripts just need to enable the CGI module; include the configuration file and make sure your chosen programming language interpreter is installed. (i.e. for python you would install )

Create the file  and add the following to it:

 server.modules += ( "mod_cgi" )

 cgi.assign                 = ( ".pl"  => "/usr/bin/perl",
                                ".cgi" => "/usr/bin/perl",
                                ".rb"  => "/usr/bin/ruby",
                                ".erb" => "/usr/bin/eruby",
                                ".py"  => "/usr/bin/python",
                                ".php" => "/usr/bin/php-cgi" )

 index-file.names           +=( "index.pl",   "default.pl",
                                "index.rb",   "default.rb",
                                "index.erb",  "default.erb",
                                "index.py",   "default.py",
                                "index.php",  "default.php" )

For PHP scripts, you will need to make sure the following is set in
 cgi.fix_pathinfo = 1

In your lighttpd configuration file,  add:
 include "conf.d/cgi.conf"

## FastCGI
Install .
Now you have lighttpd with fcgi support. If that was what you wanted, you are all set. People that want Ruby on Rails, PHP or Python should continue.

First, copy the example configuration file from  to

The following needs adding to the configuration file,
 server.modules += ( "mod_fastcgi" )

 index-file.names += ( "dispatch.fcgi" ) #dispatch.fcgi if rails specified

 server.error-handler-404   = "/dispatch.fcgi" #too
 fastcgi.server = (
     ".fcgi" => (
       "localhost" => (
         "socket" => "/run/lighttpd/rails-fastcgi.sock",
         "bin-path" => "/path/to/rails/application/public/dispatch.fcgi"
       )
     )
 )

Then in :
 include "conf.d/fastcgi.conf"

For PHP or Ruby on Rails, see the next sections.

## PHP
## Using php-cgi
Install  and  (see also PHP and LAMP).

Check that php-cgi is working

 PHP 5.4.3 (cgi-fcgi) (built: May  8 2012 17:10:17)
 Copyright (c) 1997-2012 The PHP Group
 Zend Engine v2.4.0, Copyright (c) 1998-2012 Zend Technologies

If you get a similar output, php is installed correctly.

Create a new configuration file:

Make lighttpd use the new configuration file by appending the following line to your lighttpd configuration file:

Reload lighttpd.

## Using php-fpm
For dynamic management of PHP processes, you can install  and then start and enable .

In  add:
 server.modules += ( "mod_fastcgi" )

 index-file.names += ( "index.php" )

 fastcgi.server = (
     ".php" => (
       "localhost" => (
         "socket" => "/run/php-fpm/php-fpm.sock",
         "broken-scriptfilename" => "enable"
       ))
 )

## uWSGI
In  add
{{bc|1=
server.modules += ("mod_scgi")

$HTTP["url" =~ "^/uwsgi/" {
    scgi.protocol = "uwsgi"
    scgi.server   = (
        "/uwsgi/foo" => ((
            "socket"            => "/path/to/socket",
            "check-local"       => "disable"
        )),
        "/uwsgi/bar" => ((
            "host"              => "127.0.0.1",
            "port"              => "8080",
            "check-local"       => "disable"
        ))
    )
}
}}
You can than start the uwsgi application either as a systemd unit or direct.
Here is a neat guide from digitalocean on how to setup a flask application from the scratch.

## Output compression
Copy example configuration file:

 # mkdir /etc/lighttpd/conf.d
 # cp /usr/share/doc/lighttpd/config/conf.d/deflate.conf /etc/lighttpd/conf.d/

Add following in :

 include "conf.d/deflate.conf"

Finally, reload , and it will dynamically compress plain text and html content.

It is also possible to select the type of content that should be compressed. Modify  on the parameter :

 deflate.mimetypes = ("text/plain", "text/html", "text/javascript", "text/css", "text/xml")

You can also create a cache directory to store compressed files:

 # mkdir /var/cache/lighttpd/compress
 # chown http:http /var/cache/lighttpd/compress

Then uncomment and modify the  option in :

 deflate.cache-dir = "/var/cache/lighttpd/compress"
