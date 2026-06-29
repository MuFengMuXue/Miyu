# Smokeping

Smokeping
allows you to probe a list of servers, store that data using
RRDtool, and generate statistical charts based on RRDtool's
output. Smokeping consists of two parts. A daemon runs in the
background pinging and collecting data at set intervals. A web
interface displays that data in the form of graphs.

This wiki page covers a basic setup of the smokeping daemon and the CGI webinterface.

## Installation
This section covers the installation of Smokeping using the  package. FastCGI on Apache will be setup as described in Apache and FastCGI.

The smokeping package consists of two parts:
* The smokeping daemon and configs in . This daemon performs the monitoring.
* The smokeping "htdocs" in . These will be used by the web interface.

In addition to the  package, you will need:
* A tool that smokeping can use for monitoring.  is the simplest and default method for simple ping probes.
*  and  for the web interface if you are using Apache.
*  and start and enable fcgiwrap.socket if you are using Nginx
* An image cache directory that the FastCGI script can write to, e.g.
* A data directory that the smokeping daemon can write to, and the FastCGI script can read, e.g.
* To ensure that the main configuration file is readable by the smokeping daemon.

## Optional Prerequisites
If you want to use other probes such as the DNS or http probe you will
need other packages as shown below. The configuration of these will is not covered by this wiki page.

{| class="wikitable"
! Probe !! Package Needed
|-
| Curl ||
|-
| DNS ||  (for the dig utility)
|-
| EchoPing ||
|-
| SSH ||
|-
| TelnetIOSPing ||
|-
| AnotherDNS ||
|-
| LDAP ||
|-
| LDAP (tls) ||
|-
| Authen ||
|}

## Configuration
Smokeping requires you to edit a few files. The unedited files end
with the  extension. Rename the
files in  to remove the suffix. The find command does this and
prints out each file that is being renamed and needs editing:

 # cd /etc/smokeping
 # find . -name '*.dist' -print -execdir sh -c 'mv {} $(basename {} .dist)' \;
 # mv /srv/http/smokeping/smokeping.fcgi.dist /srv/http/smokeping/smokeping.fcgi

## Editing the configuration file
Next, edit the  file; this is smokeping's main configuration file. A brief description of the sections is followed by a complete example.

Note: most paths need changing, potentially from  to , but confirm each one.
Paths for the various  files can be found with

The General section of the  file is the easiest to edit. Personalize the
top of the configuration file to match your information. The comments describe each field. Note that if you do not have the  program installed (ie from postfix or sendmail) then use something else instead like . The file you specify must exist or smokeping will error out.

The Alerts section does not require any changes for this example.

The Database section does not require any changes.

In the Presentation section the path to the template filename needs to be updated, (ie )

The Probes section specifies which probes are active. By default only the FPing probe is enabled. This section does not require any changes.

The Slaves section is not needed in this minimal example, so it can be either commented out or removed. Note that if you use the  setting in the Slaves section, you will have to make that file unreadable to the rest of the world, or else smokeping will error: .

The Targets section specifies which hosts will be probed (pinged in our example). Customize it so that it probes the host(s) you would like to collect statistics on, as shown in the example below.

You can learn more about the Smokeping configuration file with the examples at
https://oss.oetiker.ch/smokeping/doc/smokeping_examples.en.html

## Notes on the smokeping configuration file syntax
Each + character defines a section in the hierarchy. Spaces are not allowed in the section names. Period and forward slashes should probably also be avoided in section names. This is probably because the RRD files are stored under the data directory with the same exact names as the sections.

In the Targets section, you can define  as either a real host name or the path to another section to generate a multiple host chart, as shown in the  example above.

## Setup the rest of the system
Setup the extra directories referenced by the configuration file:
 # mkdir -p /srv/smokeping/data
 # mkdir -p /srv/smokeping/imgcache
 # chown -R smokeping:smokeping /srv/smokeping
 # chown -R http:http /srv/smokeping/imgcache
 # chmod a+rx /srv/smokeping
 # chmod -R a+rx /srv/smokeping/data

Since the smokeping configuration is read by both the smokeping daemon and the FastCGI scripts, so it needs to be readable:
 # chmod a+rx /etc/smokeping
 # chmod a+r /etc/smokeping/config

## Notes on Smokeping in Master Slave configuration
A master-slave has one additional wrinkle, though the principles are the same.
For slaves, smokeping IS NOT writing the data to the RRD files - they're getting pushed there by the web-server. So, in master-slave mode you need to be sure that the user your web-server is running as [ running as user ] also has WRITE permissions to the RRD files (under ).

When running Smokeping in Master / Slave mode, the master has effective permissions of the user the smokeping slave runs as. Do NOT run slaves as root. Read the security considerations first.

The Smokeping FAQ on their wiki details the complex permission requirements. If your master slave config is still not working, use  to provide the minimum required permissions:
 On the master, give both `http` and `smokeping` full access (rwx) to `/srv/smokeping/*`
 # setfacl -R -m u:http:rwx /srv/smokeping
 # setfacl -R -m u:smokeping:rwx /srv/smokeping

 Set specific read permissions for files inside `/etc/smokeping`
 # setfacl -m u:http:r /etc/smokeping/smokeping_secrets
 # setfacl -m u:smokeping:r /etc/smokeping/config /etc/smokeping/smokeping_secrets

Slaves require no config file, they pull their config from the master, and just need to read :
 # /usr/bin/smokeping --master-url=https://smokeping.site/smokeping.fcgi
 # setfacl -m u:http:r /etc/smokeping/smokeping_secrets
A sample slave's systemd unit:
 Description=Smokeping Slave: my.slave.net
 Documentation=man:smokeping_master_slave(7)

 [Service
 ExecStart=/usr/sbin/smokeping \
   --master-url=https://smokeping.site/smokeping.fcgi \
   --cache-dir=/var/lib/smokeping \
   --shared-secret=/etc/smokeping/smokeping_secrets \
   --pid-dir=/run/smokeping \
   --slave-name=my.slave.net
 # The --slave-name should be an exact match to both the master's config and smokeping_secrets

 ExecReload=/bin/kill -HUP $MAINPID

 Type=forking
 RuntimeDirectory=smokeping
 PIDFile=/run/smokeping/smokeping.pid
 User=smokeping
 Group=smokeping
 Restart=on-failure

## Start and enable daemon
Start and enable . Then check that it is running.

## Setup web frontend
## Apache
Edit  so that it includes:

 LoadModule fcgid_module modules/mod_fcgid.so

   AddHandler fcgid-script .fcgi

 Alias /smokeping/imgcache /srv/smokeping/imgcache
 Alias /smokeping /srv/http/smokeping

   AllowOverride all
   Require all granted

  Options FollowSymLinks ExecCGI
  AllowOverride all
  Require all granted

Start Apache via the .

Check that http://localhost/smokeping/smokeping.fcgi loads. The first data should appear after a couple of minutes.

If the fonts in the graphs are unreadable, you may need to install the  package.

## Caddy
Thanks to the [https://caddy.community/t/smokeping-caddyfile/3560/8 Caddy community and with this configuration file /etc/smokeping/config and with enable

{{hc|/etc/caddy/caddy.conf.d/smokeping.conf|
smokeping.example.com {

        log stdout
        errors

        tls john@example.com
        root /srv/http/smokeping

        fastcgi / unix:/var/run/fcgiwrap.sock {
                env SCRIPT_FILENAME /srv/http/smokeping/smokeping.fcgi.dist
        }
}

smokeping.example.com/js {
        root /srv/http/smokeping/js
}

smokeping.example.com/css {
        root /srv/http/smokeping/css
}

smokeping.example.com/cache {
        root /var/cache/smokeping
}
}}

An updated version of this Caddy configuration for smokeping - https://gist.github.com/Strykar/4df1eb8aebc4d5f7039f6045301352c7

## Caddy 2
Thanks to the francislavoie and Caddy community and to the Caddy docs.
Start and enable fcgiwrap.socket!

{{hc|/etc/caddy/caddy.conf.d/smokeping.conf|
smokeping.example.com {

    handle /js/* {
        root * /srv/http/smokeping/
        file_server
    }
    handle /css/* {
        root * /srv/http/smokeping/
        file_server
    }
    handle /imgcache/* {
        root * /srv/http/smokeping/
        file_server
    }
    handle /images/* {
        root * /srv/http/smokeping/
        file_server
    }

    handle {
        root * /srv/http/smokeping/
        reverse_proxy unix//var/run/fcgiwrap.sock {
            transport fastcgi {
                env SCRIPT_FILENAME /srv/http/smokeping/smokeping.fcgi
                split ""
            }
        }
    }
}
}}

## Lighttpd
First install  and .

Edit the Lighttpd configuration file and ensure you have at least all of the following configuration directives:

Start/enable the

Systemd should show  being managed by .

Finally, add a symbolic link to allow images to load:

## Nginx
Ensure that  and  are both running via systemctl.

Add a server block for smokeping to , following is an example for a TLS enabled block.

    server {
        server_name smokeping.example.com;
        listen 443 ssl http2;
        listen ssl http2;
        root /srv/http/smokeping/;
        index smokeping.fcgi;
        gzip off;
        access_log /var/log/nginx_smokeping.log combined;
        error_log /var/log/nginx_smokeping.log;
        location ~ \.fcgi$ {
            fastcgi_intercept_errors on;
            include /etc/nginx/fastcgi_params;
            fastcgi_param SCRIPT_FILENAME /srv/http/smokeping/smokeping.fcgi;
            fastcgi_pass unix:/var/run/fcgiwrap.sock;
        }
        location ^~ /imgcache {
            alias /srv/smokeping/imgcache;
            gzip off;
        }
    }

Verify that your configuration is fine via  as the root user and reload the configuration via  as the root user.

## Advanced Configuration
Smokeping is a powerful tool that can be configured in many ways. You can setup many different types of probes. You can setup slave smokeping servers that can send their statistics and show you probes from other servers.

You can also create your custom probes in perl, see some third-party probes [https://github.com/oetiker/SmokePing/wiki/Third-party-probes on their wiki. These options are currently not covered by this guide, please consult the documentation on the Smokeping website instead.

Also see - https://github.com/oetiker/SmokePing/wiki/FAQ

## Notes
## Smoketrace (Tr.cgi)
The SmokeTraceroute utility is gone since v2.5.0 according to the release notes.
