# Ganglia

Ganglia is a scalable distributed system monitor tool for high-performance computing systems such as clusters and grids. It allows the user to remotely view live or historical statistics (such as CPU load averages or network utilization) for all machines that are being monitored.

The Ganglia Wiki contains all the information you need to get started with Ganglia.

## Installation
Ganglia can be installed with the  package, along with the web frontend . There is also a reduced-dependency version named  for headless systems.

## Ganglia Web Interface
The ganglia web frontend is available as the  package on the AUR.

You will also need a web server with a working PHP setup. The following sections include some example setups.

Make sure that the  setting in your  includes ,  and .

## Nginx with php-fpm
Firstly, install the  and  packages.

Secondly, read the nginx article. Note its nginx#FastCGI and subsequent php-fpm sections. nginx#nginx configuration details a minimum  to use.

An older minimal configuration for nginx would be something like this:
{{hc|/etc/nginx/nginx.conf|
events {
  worker_connections  1024;
}

http {
  include mime.types;
  default_type application/octet-stream;

  upstream php {
    server unix:/run/php-fpm/php-fpm.sock;
  }

  server {
    listen 80 default_server;

    root /usr/share/webapps;
    index index.php;

    location ~ \.php$ {
      fastcgi_pass php;
      include fastcgi.conf;
    }
  }
}
}}

Then start , ,  and .

Go to http://localhost/ganglia and check that your setup is working.

## Troubleshooting
## Issues with IP-address binding or undesirable hostnames
If  in the  section of , the  daemon will determine which IP to bind to (and report in the XML data) by determining the IP address of the default hostname.  You should be able to replicate this behaviour with one of these commands:

The hostname to report is determined by asking the system to look up a hostname for the chosen IP address, in order to ensure the hostname is that by which other machines on the network identify the monitored machine:

The hostname listed at the top of the list is the one that will be reported by , and will appear in the web UI.  You can influence the returned hostname by modifying your  or  files.  In particular, watch out for placing  before  on the  line in .  This will cause  to attempt to bind to a UDP port on 127.0.0.1, and it will fail to load.

If you are not able to achieve the desired behaviour, the hostname can be overridden in the  file by adding the following lines to the  section:

{{bc|1=
globals {
  ...
  override_hostname = myhostname.mydomain
  override_ip = 127.0.0.2
}
}}
