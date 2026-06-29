# Nginx

nginx (pronounced "engine X"), is a free, open-source, high-performance HTTP web server and reverse proxy, as well as an IMAP/POP3 proxy server, written by Igor Sysoev in 2005. nginx is well known for its stability, rich feature set, simple configuration, and low resource consumption.

This article describes how to set up nginx and how to optionally integrate it with PHP via #FastCGI.

## Installation
Install  or .

Using the mainline branch is recommended. The main reason to use the stable branch is that you are concerned about possible impacts of new features, such as incompatibility with third-party modules or the inadvertent introduction of bugs in new features.

For a chroot-based installation for additional security, see #Installation in a chroot.

## Running
Start/enable  or  if you use Angie.

The default page served at http://127.0.0.1 is .

## Configuration
First steps with nginx are described in the Beginner’s Guide. You can modify the configuration by editing the files in  The main configuration file is located at .

More details and examples can be found in the official documentation.

The examples below cover the most common use cases. It is assumed that you use the default location for documents (). If that is not the case, substitute your path instead.

## Configuration example
{{hc|/etc/nginx/nginx.conf|
user http;
worker_processes auto;
worker_cpu_affinity auto;

events {
    worker_connections 1024;
}

http {
    charset utf-8;
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    server_tokens off;
    log_not_found off;
    types_hash_max_size 4096;
    client_max_body_size 16M;

    # MIME
    include mime.types;
    default_type application/octet-stream;

    # logging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log warn;

    # load configs
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
}}

## General configuration
## Processes and connections
You should choose a fitting value for . This setting ultimately defines how many connections nginx will accept and how many processors it will be able to make use of. Generally, making it the number of hardware threads in your system is a good start. Alternatively,  accepts the  value since versions 1.3.8 and 1.2.5, which will try to autodetect the optimal value (source).

The maximum connections nginx will accept is given by .

## Running under different user
By default,  runs the master process as  and worker processes as user . To run worker processes as another user, change the  directive in :

If the group is omitted, a group whose name equals that of user is used.

## Server blocks
It is possible to serve multiple domains using  blocks. These are comparable to "VirtualHosts" in Apache HTTP Server. Also see the upstream examples.

In the example below the server listens for incoming connections on IPv4 and IPv6 ports 80 for two domains,  and :

{{hc|/etc/nginx/nginx.conf|
...
server {
    listen 80;
    listen server_name domainname1.tld;
    root /usr/share/nginx/domainname1.tld/html;
    location / {
        index index.php index.html index.htm;
    }
}

server {
    listen 80;
    listen [:::80;
    server_name domainname2.tld;
    root /usr/share/nginx/domainname2.tld/html;
    ...
}
}}

Restart  to apply any changes.

## Managing server entries
It is possible to put different  blocks in different files. This allows you to easily enable or disable certain sites.

For using the  and  approach, create the following directories:

 # mkdir /etc/nginx/sites-available
 # mkdir /etc/nginx/sites-enabled

Create a file inside the  directory that contains one or more server blocks:

{{hc|/etc/nginx/sites-available/example.conf|
server {
    listen 443 ssl;
    listen ssl;
    http2 on;

    ...
}
}}

Append  to the end of the  block:

{{hc|/etc/nginx/nginx.conf|
http {
    ...
    include sites-enabled/*;
}
}}

To enable a site, simply create a symlink:

 # ln -s /etc/nginx/sites-available/example.conf /etc/nginx/sites-enabled/example.conf

To disable a site, unlink the active symlink:

 # unlink /etc/nginx/sites-enabled/example.conf

Reload/restart  to enable changes to the site's configuration.

## TLS
OpenSSL provides TLS support and is installed by default on Arch installations.

Create a private key and self-signed certificate. This is adequate for most installations that do not require a CSR:

 # mkdir /etc/nginx/ssl
 # cd /etc/nginx/ssl
 # openssl req -new -x509 -nodes -newkey rsa:4096 -keyout server.key -out server.crt -days 1095
 # chmod 400 server.key
 # chmod 444 server.crt

If you need to create a CSR, follow these instructions instead of the above:

 # mkdir /etc/nginx/ssl
 # cd /etc/nginx/ssl
 # openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out server.key
 # chmod 400 server.key
 # openssl req -new -sha256 -key server.key -out server.csr
 # openssl x509 -req -days 1095 -in server.csr -signkey server.key -out server.crt

A starting point for a  with TLS is [https://ssl-config.mozilla.org/#server=nginx Mozilla's SSL Configuration Generator.

Restart  to apply any changes.

## Per-user directories
To replicate Apache-style  URLs to users'  directories, try the following. (Note: if both rules are used, below, the more-specific PHP rule must come first.)

{{hc|/etc/nginx/nginx.conf|
...
server {
    ...
    # PHP in user directories, e.g. http://example.com/~user/test.php
    location ~ ^/~(.+?)(/.+\.php)$ {
        alias          /home/$1/public_html$2;
        fastcgi_pass   unix:/run/php-fpm/php-fpm.sock;
        fastcgi_index  index.php;
        include        fastcgi.conf;
    }

    # User directories, e.g. http://example.com/~user/
    location ~ ^/~(.+?)(/.*)?$ {
        alias     /home/$1/public_html$2;
        index     index.html index.htm;
        autoindex on;
    }
    ...
}
...
}}

See #PHP implementation for more information on PHP configuration with .

Restart  to enable the new configuration.

## FastCGI
FastCGI, also FCGI, is a protocol for interfacing interactive programs with a web server. FastCGI is a variation on the earlier Common Gateway Interface (CGI); FastCGI's main aim is to reduce the overhead associated with interfacing the web server and CGI programs, allowing servers to handle more web page requests at once.

FastCGI technology is introduced into nginx to work with many external tools, e.g. Perl, PHP and Python.

## PHP implementation
PHP-FPM is the recommended solution to run as FastCGI server for PHP.

Install  and make sure PHP has been installed and configured correctly. The main configuration file of PHP-FPM is . For basic usage the default configuration should be sufficient.

Finally, start/enable .

You can also use  instead, see #Using php-legacy.

## nginx configuration
When serving a PHP web-application, a  for PHP-FPM should to be included in each server block e.g.:

{{hc|/etc/nginx/sites-available/example.conf|2=
server {
    root /usr/share/nginx/html;

    location / {
        index index.html index.htm index.php;
    }

    location ~ \.php$ {
        # 404
        try_files $fastcgi_script_name =404;

        # default fastcgi_params
        include fastcgi_params;

        # fastcgi settings
        fastcgi_pass			unix:/run/php-fpm/php-fpm.sock;
        fastcgi_index			index.php;
        fastcgi_buffers			8 16k;
        fastcgi_buffer_size		32k;

        # fastcgi params
        fastcgi_param DOCUMENT_ROOT	$realpath_root;
        fastcgi_param SCRIPT_FILENAME	$realpath_root$fastcgi_script_name;
        #fastcgi_param PHP_ADMIN_VALUE	"open_basedir=$base/:/usr/lib/php/:/tmp/";
    }
}
}}

If it is needed to process other extensions with PHP (e.g. .html and .htm):

 location ~ [^/\.(php|html|htm)(/|$) {
     ...
 }

Non .php extension processing in PHP-FPM should also be explicitly added in :

 security.limit_extensions = .php .html .htm

{{Tip|To allow multiple  blocks using the same PHP-FPM configuration, a  configuration file may be used to ease management:

{{hc|/etc/nginx/php_fastcgi.conf|2=
location ~ \.php$ {
    # 404
    try_files $fastcgi_script_name =404;

    # default fastcgi_params
    include fastcgi_params;

    # fastcgi settings
    ...
}
}}

To enable PHP support for a particular server, simply include the  configuration file:

{{hc|/etc/nginx/sites-available/example.conf|
server {
    server_name example.com;
    ...

    include /etc/nginx/php_fastcgi.conf;
}
}}

}}

## Test configuration
You need to restart the  and  units if the configuration has been changed in order to apply changes.

To test the FastCGI implementation, create a new PHP file inside the  folder containing:

Navigate this file inside a browser and you should see the informational page with the current PHP configuration.

## CGI implementation
This implementation is needed for CGI applications.

## fcgiwrap
Install . The configuration is done by editing . Enable and start .

## Multiple worker threads
If you want to spawn multiple worker threads, it is recommended that you use , which will take care of restarting crashed children. You will need to use  to create the Unix socket, as multiwatch seems unable to handle the systemd-created socket, even though fcgiwrap itself does not have any trouble if invoked directly in the unit file.

Override the unit  (and the  unit, if present), and modify the  line to suit your needs. Here is a unit file that uses . Make sure  is not started or enabled, because it will conflict with this unit:

Tweak  to change the number of children that are spawned.

## nginx configuration
In , copy the file  to . In , comment or delete the lines which set  and .

Inside each  block serving a CGI web application should appear a  block similar to:

 location ~ \.cgi$ {
      include       fcgiwrap_params;
      fastcgi_param DOCUMENT_ROOT /srv/www/cgi-bin/;
      fastcgi_param SCRIPT_NAME   myscript.cgi;
      fastcgi_pass  unix:/run/fcgiwrap.sock;
 }

The default socket file for  is .

Using  is a shortcut alternative to setting  and . If you use , you also will not need to copy  to  and comment out the  and  lines.

If you keep getting a  error, you should check if your CGI-application first announces the mime-type of the following content. For HTML this needs to be .

If you get 403 errors, make sure that the CGI executable is readable and executable by the  user and that every parent folder is readable by the  user.

## Installation in a chroot
Installing nginx in a chroot adds an additional layer of security. For maximum security the chroot should include only the files needed to run the nginx server and all files should have the most restrictive permissions possible, e.g., as much as possible should be owned by root, directories such as  should be unreadable and unwritable, etc.

Arch comes with an  user and group by default which will run the server. The chroot will be in .

A Perl script to create this jail is available at jail.pl gist. You can either use that or follow the instructions in this article. It expects to be run as root. You will need to uncomment a line before it makes any changes.

## Create necessary devices
nginx needs , , and . To install these in the chroot create the  directory and add the devices with mknod. Avoid mounting all of  to ensure that, even if the chroot is compromised, an attacker must break out of the chroot to access important devices like .

{{Tip|
* Be sure that  is mounted without the nodev option
* See  and {{ic|ls -l /dev/{null,random,urandom}}} to better understand the mknod options.
}}

 # export JAIL=/srv/http
 # mkdir $JAIL/dev
 # mknod -m 0666 $JAIL/dev/null c 1 3
 # mknod -m 0666 $JAIL/dev/random c 1 8
 # mknod -m 0444 $JAIL/dev/urandom c 1 9

## Create necessary directories
nginx requires a bunch of files to run properly. Before copying them over, create the folders to store them. This assumes your nginx document root will be .

 # mkdir -p $JAIL/etc/nginx/logs
 # mkdir -p $JAIL/usr/{lib,bin}
 # mkdir -p $JAIL/usr/share/nginx
 # mkdir -p $JAIL/var/{log,lib}/nginx
 # mkdir -p $JAIL/www/cgi-bin
 # mkdir -p $JAIL/{run,tmp}
 # cd $JAIL; ln -s usr/lib lib
 # cd $JAIL; ln -s usr/lib lib64
 # cd $JAIL/usr; ln -s lib lib64

Then mount  and  as tmpfs's. The size should be limited to ensure an attacker cannot eat all the RAM.

 # mount -t tmpfs none $JAIL/run -o 'noexec,size=1M'
 # mount -t tmpfs none $JAIL/tmp -o 'noexec,size=100M'

In order to preserve the mounts across reboots, the following entries should be added to :

## Populate the chroot
First copy over the easy files.

 # cp -r /usr/share/nginx/* $JAIL/usr/share/nginx
 # cp -r /usr/share/nginx/html/* $JAIL/www
 # cp /usr/bin/nginx $JAIL/usr/bin/
 # cp -r /var/lib/nginx $JAIL/var/lib/nginx

Now copy over required libraries. Use ldd to list them and then copy them all to the correct location. Copying is preferred over hardlinks to ensure that even if an attacker gains write access to the files they cannot destroy or alter the true system files.

For files residing in  you may try the following one-liner:

 # cp $(ldd /usr/bin/nginx | grep /usr/lib/ | sed -sre 's/(.+)(\/usr\/lib\/\S+).+/\2/g') $JAIL/usr/lib

And the following for :

 # cp /lib64/ld-linux-x86-64.so.2 $JAIL/lib

Copy over some miscellaneous but necessary libraries and system files.

 # cp /usr/lib/libnss_* $JAIL/usr/lib
 # cp -rfvL /etc/{services,localtime,nsswitch.conf,nscd.conf,protocols,hosts,ld.so.cache,ld.so.conf,resolv.conf,host.conf,nginx} $JAIL/etc

Create restricted user/group files for the chroot. This way only the users needed for the chroot to function exist as far as the chroot knows, and none of the system users/groups are leaked to attackers should they gain access to the chroot.

 # touch $JAIL/etc/shells
 # touch $JAIL/run/nginx.pid

Finally, make set very restrictive permissions. As much as possible should be owned by root and set unwritable.

 # chown -R root:root $JAIL/

 # chown -R http:http $JAIL/www
 # chown -R http:http $JAIL/etc/nginx
 # chown -R http:http $JAIL/var/{log,lib}/nginx
 # chown http:http $JAIL/run/nginx.pid

 # find $JAIL/ -gid 0 -uid 0 -type d -print | xargs chmod -rw
 # find $JAIL/ -gid 0 -uid 0 -type d -print | xargs chmod +x
 # find $JAIL/etc -gid 0 -uid 0 -type f -print | xargs chmod -x
 # find $JAIL/usr/bin -type f -print | xargs chmod ug+rx
 # find $JAIL/ -group http -user http -print | xargs chmod o-rwx
 # chmod +rw $JAIL/tmp
 # chmod +rw $JAIL/run

If your server will bind port 80 (or any other port in range give the chrooted executable permission to bind these ports without root.

 # setcap 'cap_net_bind_service=+ep' $JAIL/usr/bin/nginx

## Modify nginx.service to start chroot
Override the unit . Upgrading nginx will not modify your custom .service file.

The systemd unit must be changed to start up nginx in the chroot, as the http user, and store the PID file in the chroot.

You can now safely get rid of the non-chrooted nginx installation.

 # pacman -Rsc nginx

If you do not remove the non-chrooted nginx installation, you may want to make sure that the running nginx process is in fact the chrooted one. You can do so by checking where  symlinks to. It should link to  instead of .

 # ps -C nginx | awk '{print $1}' | sed 1d | while read -r PID; do ls -l /proc/$PID/root; done

## Tips and tricks
## Running unprivileged using systemd
Use a drop-in unit file for  and set the  and optionally  options under :

We can harden the service against ever elevating privileges:

Then we need to ensure that  has access to everything it needs. Follow the subsections below and then start nginx.

## Port
Linux does not permit non- processes to bind to ports below 1024 by default. A port above 1024 can be used:

{{hc|/etc/nginx/nginx.conf|
server {
        listen 8080;
}
}}

Or you may grant the nginx process the CAP_NET_BIND_SERVICE capability which allows it to bind to ports below 1024:

Alternatively, you can use systemd socket activation. In this case, systemd will listen on the ports and, when a connection is made, spawn nginx passing the socket as a file descriptor. This means nginx requires no special capabilities as the socket already exists when it is started. This relies on an internal environment variable that nginx uses for passing sockets [https://trac.nginx.org/nginx/ticket/237 and is therefore not officially supported. Instead of setting  and , edit the service override to set the  environment variable to tell nginx which file descriptors the sockets will be passed as:

There will be one socket per listening port starting at file descriptor 3, so in this example we are telling nginx to expect two sockets. Now create an  unit specifying what ports to listen on:

The sockets will be passed in the order defined in this unit, so port 80 will be file descriptor 3 and port 443 will be file descriptor 4. If you previously enabled or started the service, you should now stop it, and enable  instead. When your system starts, nginx will not be running, but will be started when you access the website in a browser. With this you can harden the service further; for example, in many cases you can now set  in the service file, blocking nginx from the external network, since the socket created by systemd is sufficient to serve the website over. Note that this will print a warning in the logs of the nginx service:

## PID file
 is compiled to use  by default, which user cannot write to. We can create a directory that user can write to and place the PID file there. This can for example be done with  ().

Edit  to configure the PID file:

## /var/lib/nginx
 is compiled to store temp files in  by default.

You can give user write access to this directory by for example using  ():

## /var/log/nginx
 is compiled to store access logs in  by default.

You can give user write access to this directory by for example using  ():

## Running user service using systemd
If you want to run a server instance fully controlled and configurable by unprivileged user, here is an example of a systemd user service.

It reads config from  and uses  as a working directory.

## Alternative script for systemd
On pure systemd you can get advantages of chroot + systemd. Based on set [https://nginx.org/en/docs/ngx_core_module.html#user user group and pid with:

the absolute path of the file is .

It is not necessary to set the default location, nginx loads at default , but it is a good idea.

Alternatively you can run only  as chroot with parameter  set as  (see ) or start it before mount point as effective or a systemd path (see ) is available.

Enable the created  and change the  to  in .

The  in unit file allows systemd to monitor process (absolute path required). If it is undesired, you can change to default one-shot type, and delete the reference from the unit file.

## Nginx beautifier
 is a commandline tool used to beautify and format nginx configuration files.

## Gixy static config analyzer
 is a fork of stale Yandex Gixy — security and performance issues analyzer of Nginx configuration. By default it reads  only. Full config can be obtained and analyzed with following commands:

 # nginx -T > nginx_full.conf
 $ gixy nginx_full.conf

## Better headers management
Nginx has a rather unintuitive header management system where headers can only be defined in one context, any other headers are ignored. To remedy this we can install the headers-more-nginx module.

Install the package  package. This will install the module to  directory.

To load the module add the following to the top of your main nginx configuration file.

## Basic Authentication
Basic authentication requires creation of a password file. The password file can be managed using  program provided by the  package or using  which provides  - details available on GitHub source

## Using php-legacy
Install  instead of  and make sure PHP has been installed and configured correctly.

The main configuration file of PHP-LEGACY-FPM is . For basic usage the default configuration should be sufficient.

The Unix socket for the  argument also needs to be adjusted, usually it is:

 fastcgi_pass unix:/run/php-fpm-legacy/php-fpm.sock;

Then start/enable .

## Troubleshooting
## Configuration validation
## Error: The page you are looking for is temporarily unavailable. Please try again later. (502 Bad Gateway)
This is because the FastCGI server has not been started, or the socket used has wrong permissions.

Try out this answer to fix the 502 error.

In Arch Linux, the configuration file mentioned in above link is .

## Error: No input file specified
1. Verify that variable  in  contains the correct path specified as  argument in  (usually ). When using PHP-FPM as FastCGI server for PHP, you may add  in the  block which aims for processing PHP file in .

2. Another occasion is that, wrong  argument in the  section in . Make sure the  points to the same directory as it in  in the same server. Or you may just set root as global, do not define it in any location section.

3. Check permissions: e.g.  for user/group,  for directories and  for files. Remember the entire path to the  directory should have the correct permissions. See File permissions and attributes#Bulk chmod to bulk modify a directory tree.

4. You do not have the  containing the full path to your scripts. If the configuration of nginx () is correct, this kind of error means PHP failed to load the requested script. Usually it is simply a permissions issue, you can just run php-cgi as root:

 # spawn-fcgi -a 127.0.0.1 -p 9000 -f /usr/bin/php-cgi

or you should create a group and user to start the php-cgi:

 # groupadd www
 # useradd -g www www
 # chmod +w /srv/www/nginx/html
 # chown -R www:www /srv/www/nginx/html
 # spawn-fcgi -a 127.0.0.1 -p 9000 -u www -g www -f /usr/bin/php-cgi

5. If you are running php-fpm with chrooted nginx ensure  is set correctly within  (or  if working on older version)

## Warning: Could not build optimal types_hash
When starting the , the process might log the message:

 18872#18872: could not build optimal types_hash, you should increase either types_hash_max_size: 1024 or types_hash_bucket_size: 64; ignoring types_hash_bucket_size

To fix this warning, increase the values for these keys inside the  block [https://nginx.org/en/docs/http/ngx_http_core_module.html#types_hash_max_size {{hc|/etc/nginx/nginx.conf|
http {
    types_hash_max_size 4096;
    server_names_hash_bucket_size 128;
    ...
}
}}

## Cannot assign requested address
The full error from  unit status is

 [emerg 460#460: bind() to A.B.C.D:443 failed (99: Cannot assign requested address)

Even if your nginx unit-file is configured to run after  with systemd, nginx may attempt to listen at an address that is configured but not added to any interface yet. Verify that this the case by manually running start for nginx (thereby showing the IP address is configured properly). Configuring nginx to listen to any address will resolve this issue. Now if your use case requires listening to a specific address, one possible solution is to reconfigure systemd.

To start nginx after all configured network devices are up and assigned an IP address, append  to  within  and start/enable .
