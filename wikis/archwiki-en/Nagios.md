# Nagios

Nagios is an open source host, service and network monitoring program. It monitors specified hosts and services, alerting you to any developing issues, errors or improvements. This article describes the installation and configuration of Nagios.

## Features
Some of Nagios' features include:

* Monitoring of network services (SMTP, POP3, HTTP, NNTP, PING, etc.)
* Monitoring of host resources (processor load, disk usage, etc.)
* Simple plugin design that allows users to easily develop their own service checks
* Parallelized service checks
* Ability to define network host hierarchy using "parent" hosts, allowing detection of and distinction between hosts that are down and those that are unreachable
* Contact notifications when service or host problems occur and get resolved (via email, pager, or user-defined method)
* Ability to define event handlers to be run during service or host events for proactive problem resolution
* Automatic log file rotation
* Support for implementing redundant monitoring hosts
* Optional web interface for viewing current network status, notification and problem history, log file, etc.

The following installation and configuration were tested using nagios 3.2.0-1, Apache web server 2.2.14-2, and PHP5 5.3.1-3 by awayand.

## Webserver
According to the official documentation a webserver is not required, but if you wish to use any of the CGI features then a webserver (apache preferred), PHP (php-apache) for it and the gd library are required. This is assumed for this installation.

## Installation
Before installation, it is a good idea to make sure you have prerequisites installed, e.g. if you are using nginx then: nginx, php, php-fpm, fcgiwrap might be a good start.

Install  package.

Users may also want to install . When you do, make sure to edit  later to reflect the new paths:

 #$USER1$=/usr/share/nagios/libexec
 $USER1$=/usr/lib/monitoring-plugins

## Nagios configuration
Copy the sample configuration files:

 # for samples in /etc/nagios/{cgi.cfg.sample,resource.cfg.sample,nagios.cfg.sample,objects/commands.cfg.sample,objects/contacts.cfg.sample,objects/localhost.cfg.sample,objects/templates.cfg.sample,objects/timeperiods.cfg.sample} ; do cp $samples ${samples%.*} ; done

Make owner/group for all the files you just copied and belong to root equal to nagios/nagios:

 # chown -R nagios:nagios /etc/nagios

If you have installed apache-tools, then create htpasswd.users file with a username (e.g. nagiosadmin). You will be prompted to add a password.

 # htpasswd -c /etc/nagios/htpasswd.users nagiosadmin

Instead, if you do not want to install apache-tools, you can run the following command

 # echo -e "nagiosadmin:`perl -le 'print crypt("your_password","salt")'`" > /etc/nagios/htpasswd.users

You can also add a different user, but before you can do anything with it in Nagios, you will need to edit . You can replace 'nagiosadmin' with the desired user, or, you can append it with comma: nagiosadmin,yourusername,yournextusername etc.

If the owner/group of the nagios-plugins you installed are root:root, the following needs to be done:

 # chown -R nagios:nagios /usr/share/nagios

Once Nagios is configured, it is time to configure the webserver.

## Apache configuration
If using Apache HTTP Server as webserver, edit  and add the following to the end of the file:

If planning to use Nagios CGI scripts, you will need to uncomment the following:

Copy configure file:

 # cp /etc/webapps/nagios/apache.example.conf /etc/httpd/conf/extra/nagios.conf

Add the apache user http to the group nagios, otherwise you will get the following error when using nagios: "Could not open command file '/var/nagios/rw/nagios.cmd' for update!"

 # usermod -G nagios -a http

If you are still getting this error, you might need to change the rights on the file:

 # chmod 666 /var/nagios/rw/nagios.cmd

## Nginx configuration
Apart from php and php-fpm, You should have fcgiwrap installed or else CGI scripts will not run.

You will also need to ensure php-fm and fcgiwrap services/sockets are started when using nginx
# Start, or restart,  for php-fpm
# Start, or restart,  for fcgiwrap

Example configuration:

{{bc|
1=server {
    server_name     nagios.yourdomain.tld;
    root            /usr/share/nagios/share;
    listen          80;
    index           index.php index.html index.htm;
    access_log      nagios.access.log;
    error_log       nagios.error.log;

    auth_basic            "Nagios Access";
    auth_basic_user_file  /etc/nagios/htpasswd.users;

    # Fixes frames not working
    add_header X-Frame-Options "ALLOW";

    location ~ \.php$ {
        try_files       $uri = 404;
        fastcgi_index   index.php;
        fastcgi_pass    unix:/run/php-fpm/php-fpm.sock;
        include         fastcgi.conf;
    }

    location ~ \.cgi$ {
        root            /usr/share/nagios/sbin;
        rewrite         ^/nagios/cgi-bin/(.*)\.cgi /$1.cgi break;
        fastcgi_param   AUTH_USER $remote_user;
        fastcgi_param   REMOTE_USER $remote_user;
        include         fastcgi.conf;
        fastcgi_pass    unix:/run/fcgiwrap.sock;
    }

    # Fixes the fact some links are expected to resolve to /nagios, see here.
    location /nagios {
        alias /usr/share/nagios/share;
    }

}
}}

## Lighttpd configuration
Example for lighttpd:

{{bc|
1=$HTTP=~ "^/nagios" {
        alias.url = (
                "/nagios/cgi-bin" => "/usr/share/nagios/sbin",
                "/nagios" => "/usr/share/nagios/share"
        )

        $HTTP["url" =~ "^/nagios/cgi-bin" {
                cgi.assign = ( "" => "" )
        }

        auth.backend = "htpasswd"
        auth.backend.htpasswd.userfile = "/etc/nagios/htpasswd.users"
        auth.require = ( "" => (
                "method" => "basic",
                "realm" => "nagios",
                "require" => "user=nagiosadmin"
                )
        )
}
}}

Note that mod_setenv, mod_cgi, mod_alias and mod_auth must be allowed.

## PHP configuration
Edit  to include  in the open_basedir directive.

Example configuration:

## Final steps
# Start, or restart,  for Nagios
# Start, or restart, your webserver:  for Apache,  for Nginx, and  for lightttpd.

Now you should be able to access nagios through your webbrowser using the username and password you have created above using htpasswd:

 http://localhost/nagios

## Monitor an Arch Linux host
You will need  and either  or use check_by_ssh along with passwordless ssh to monitor your host.

## nrpe
The nrpe configuration is done in  and the interesting files to monitor will be in . Do not forget to edit  as it is mostly empty after install.

## check_by_ssh
On the monitoring system, su to the user account that Nagios/Icinga/whatever runs as, run .  Create a user on the Arch system to be monitored with the same name and a temporary password, e.g:

 # useradd -m -d /home/icinga -s /bin/bash -p icinga icinga.

From the monitoring system run this (where  is the IP of the client):

 $ ssh-copy-id client_ipaddess

Back on the client, clear the temporary password:

 # passwd -d icinga.

Verify you can login from the server with:

 $ ssh icinga@client_ipaddres

Many non Arch systems install the monitoring plugins to  but Arch installs them to .  It may be helpful to create  and symlink  to  from that directory.

Here is an example of a command invocation run from the command line as the monitoring system's user:

 $ /usr/lib/nagios/plugins/check_by_ssh -E -H 192.168.100.11 -C "/usr/lib/nagios/plugins/check_disk -w 10 -c 5 --path=/ --units=GB"
