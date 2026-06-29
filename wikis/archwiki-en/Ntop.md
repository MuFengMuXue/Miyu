# Ntop

ntop is a network traffic probe based on libpcap, that offers RMON-like network traffic statistics accessible via a web browser.

ntop's final release was in 2012 and is currently unmaintained. It has been succeeded by ntopng ().

## Installation and configuration
Install the  package.
The first run of ntop, you must set the admin password:
 # ntop

Next, you need to edit the configuration file () to adapt on your needs. Below is an example configuration, with the focus on the host to get as much as information from the hosts connections:

Before starting and possibly enabling the  service, you may have to edit its ntop command options:

## Tips and tricks
## Web interface
To access ntop's web interface, enter http://127.0.0.1:3000/ into your web browser. To make changes to the server, you will need to enter your username (default = admin) and password.

If ntop is not just used locally on your machine, but network wide by multiple users, you would be better off by allowing SSL connections (https) only.

 # ntop -W 4223

On firefox, the self-signed certificat should be a problem. Page will not be shown like that.

Additional paramethers are allowed. Now direct our browser to https://127.0.0.1:4223/.

You can also provide ntop with your own SSL certificate. Simply put it in ntop's configuration directory and name it

 # cd /usr/share/ntop
 # openssl req -x509 -nodes -days 365
   \-subj '/C=US/L=Portland/CN=swim'
   \-newkey rsa:1024 -keyout ntop-cert.pem -out ntop-cert.pem

Instead of make a self-signed certificat who will make your page unable to print on firefox, you should look at letsencrypt service. This service will make a free well recognized certificat for your domain. Then you will have to copy privkey.pem and fullchain.pem inside ntop-cert.pem:

 # cat /etc/letsencrypt/live//privkey.pem /etc/letsencrypt/live/>your domain>/fullchain.pem > /usr/share/ntop/ntop-cert.pem

you can also copy your private key in the same place.

## Group and user
In order for the -u parameter to work properly and to make your ntop setup a bit more secure, you should create your own group and user for it.

 # useradd -M -s /usr/bin/false ntop
 # passwd -l ntop

## Troubleshooting
## **ERROR** RRD: Disabled - unable to create base directory (err 13, /var/lib/ntop/rrd)
Directory  may not exist. Create it and make sure it belongs to user nobody.

## Please enable make sure that the ntop html/ directory is properly installed
If you receive this warning while trying to access the web interface, edit  to include your IP and restart the daemon. For example:

 NTOP_ARGS="-i enp1s0 -w 127.0.0.1:3000"

This is the IP you will use to access the web interface.
