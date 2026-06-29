# RTorrent/RuTorrent

ruTorrent is a PHP frontend/web interface to rTorrent (a console based BitTorrent client). It uses rTorrent's built-in XML-RPC server to communicate with it.

It is lightweight, highly extensible, and is designed to look similar to uTorrent.

## Installation
Install the  package.

## Configuration
See upstream wiki here. By default the configuration files are symlinked to  .

## Web server configuration
## Apache 2.4
Install and configure Apache with PHP according to the LAMP page.

* Edit the open_basedir value in /etc/php/php.ini to include:
 /etc/webapps/rutorrent/conf/:/usr/share/webapps/rutorrent/php/:/usr/share/webapps/rutorrent/

* Enable the rTorrent XMLRPC interface on UNIX socket : rTorrent#XMLRPC interface

* Enable SCGI on the socket you chose for rTorrent by adding this to :
 ProxyPass /RPC2 scgi:///path/to/rpc.socket

* Lastly, add the ruTorrent folder to
As a directory alias

   Alias /rutorrent /usr/share/webapps/rutorrent

     Require all granted

As a VirtualHost

   ServerName torrent.yourwebsite.com
   DocumentRoot /usr/share/webapps/rutorrent

      Options -Indexes -MultiViews
      Require all granted
      AllowOverride all

## Nginx
* Create a link from your web root to rutorrent
 ln -s /usr/share/webapps/rutorrent/ /usr/share/nginx/html/rutorrent

* Edit the open_basedir value in /etc/php/php.ini to include:
 /etc/webapps/rutorrent/conf/:/usr/share/webapps/rutorrent/php/:/usr/share/webapps/rutorrent/

* Enable the rTorrent XMLRPC interface: rTorrent#XMLRPC interface

* Edit the following location to your rutorrent configuration at  where rtorrentuser is the user running rutorrent:
 $scgi_port = 0;
 $scgi_host = "unix:///home/rtorrentuser/rpc.socket";

Note: A multi-user setup will need user specific configuration files under  for each user's socket location. Create a folder with the user's name, then create a config.php, for example:
 /usr/share/webapps/rutorrent/conf/users/rtorrentuser/config.php
 /usr/share/webapps/rutorrent/conf/users/anotheruser/config.php

* Restart .

* You can now access ruTorrent at http://127.0.0.1/rutorrent

## Lighttpd
 should be compiled with XML-RPC support.

Add the following line to your rtorrent configuration file, usually .

 scgi_port = 127.0.0.1:5050

Instead of using a tcp port, it may also be possible to use a socket using the scgi_local option instead, however lighttpd may complain about permissions regardless of permissions / location of socket file.

You can choose a port other than 5050 if you like.

## lighttpd
Install Lighttpd and PHP:    .

After starting lighttpd as per the wiki, you should be able to access the test page at http://localhost:80.

By default the pages are served from , this is where we will be putting rutorrent.

## lighttpd.conf
Create the  drop-in folder and .

Add following lines for lighttpd to load the fastcgi and simple-cgi modules. Fastcgi is needed for rutorrent itself, and scgi for rutorrent to communicate with rtorrent:

Next we add the configuration for scgi to connect to rtorrent. Make sure to use the same socket location when configuring rtorrent:

And finally the fastcgi settings so lighttpd knows how to deal with php:

Edit  to include the configuration drop-in location:

Finally, restart .

## php.ini
We need to make a small change to the open_basedir line in , to allow rutorrent to access the binaries it needs to run.

    open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/usr/bin

The binaries are stat, id, php, curl, gzip. If these are installed somewhere other than , then you may need to append that to the line also.

## rutorrent
Create a link from your web root to rutorrent
 ln -s /usr/share/webapps/rutorrent/ /srv/http/rutorrent

We need to edit , and configure the socket previously configured for rtorrent and lighttpd above.

You can now access ruTorrent at http://127.0.0.1/rutorrent

## Plugins
To install plugins for rutorrent, download the archive of the plugin you want and extract to rutorrent's plugin directory.
 /srv/http/rutorrent/plugins

Plugins can be found on the rutorrent website: https://code.google.com/p/rutorrent/wiki/Plugins

## SSL and authentication
## User authentication
Detailed information on the different authentication methods can be found here: https://redmine.lighttpd.net/projects/1/wiki/Docs_ModAuth

In this example we will digest authentication with htdigest method.

In your lighttpd directory, we will create a file called  or some other filename of your choice to hold the passwords.

For htdigest, the format of the lines is:

 username:Realm:hash

Username is your desired username, Realm is a name you chose to give to the access level. Hash is an md5sum of a string that looks like:

 username:Realm:password

So your actual password is not stored in the file, it just contributes to the md5sum.

So using username: 'tom', Realm: 'rtorrent' and password: 'secret_pass', we can obtain the hash by running:

    $ echo -n "tom:rtorrent:secret_pass" | md5sum | cut -b -32
    6a4aaa1091eb2d1d025bbd692dee3f0c

-n tells echo not to print a newline, the cut command takes just the first 32 bytes so we do not get the dash at the end.

So now save the hash in a variable by running:

    $ hash=$(echo -n "tom:rtorrent:secret_pass" | md5sum | cut -b -32)
    $ echo $hash
    6a4aaa1091eb2d1d025bbd692dee3f0c

Now save it to our password file:

 # echo "tom:rtorrent:$hash" > /etc/lighttpd/lighttpd-htdigest.user

You can use any file name you like, just add the same file to .

If root as owner of this file does not work, try http:

 # chown http /etc/lighttpd/lighttpd-htdigest.user
 # chmod 400 /etc/lighttpd/lighttpd-htdigest.user

Now we will change  to tell it to use this password file for anytime rutorrent is accessed.

Add the following lines:

    server.modules += ( "mod_auth" )
    auth.debug = 0
    auth.backend = "htdigest"
    auth.backend.htdigest.userfile = "/etc/lighttpd/lighttpd-htdigest.user"

    auth.require = ( "/rutorrent/" => (
                     "method"  => "digest",
                     "realm"   => "rtorrent",
                     "require" => "valid-user"
                   ))

Restart lighttpd, and it should now require you to enter your username and password when you reload rutorrent.

Restart .

## SSL
See Lighttpd#Enabling https via SSL. The following resources can help you add ssl to lighttpd If you just want to get it working, the following commands should work.

Create pem file:

 # mkdir /etc/lighttpd/certs
 # openssl req -new -x509 -newkey rsa:2048 -keyout /etc/lighttpd/certs/lighttpd.pem -out /etc/lighttpd/certs/lighttpd.pem -days 730 -nodes

Then add the following lines to  (remove '#' comments if you still want plain http enabled:

    #$SERVER["socket" == ":443" {
         ssl.engine = "enable"
         ssl.pemfile = "/etc/lighttpd/certs/lighttpd.pem"
    #}

And change this line from 80 to 443 (if you only want ssl enabled):

    server.port     = 443

Then https should work, and depending on what you changed, http may not work anymore.

Note: This cert is not signed by a Certificate Authority, so you will have to add an exception in Firefox.

## Troubleshooting
For problems with rutorrent or lighttpd, the best place to check first is probably the lighttpd log files, in , particularly .

 $ tail /var/log/lighttpd/error.log
