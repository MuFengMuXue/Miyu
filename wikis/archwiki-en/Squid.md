# Squid

Squid is a caching proxy for HTTP, HTTPS and FTP, providing extensive access controls.

## Installation
Install the  package.

## Configuration
By default, the cache directories will be created in , and the appropriate permissions set up for those directories. However, for greater control, we need to delve into .

The following options might be of some use to you. If you do not have the option present in your configuration file, add it!

*  - Sets the port that Squid binds to on your local machine. You can have Squid bind to multiple ports by specifying multiple  lines. By default, Squid binds to port 3128.
 http_port 3128
 http_port 3129
*  - This is an access control list for who is allowed to use the proxy. By default only localhost is allowed to access the proxy. For testing purposes, you may want to change the option  to , which will allow anyone to connect to your proxy. If you wanted to just allow access to your subnet, you can do:
 acl ip_acl src 192.168.1.0/24
 http_access allow ip_acl
 http_access deny all
* - This is the email address of the cache manager.
 cache_mgr squid.admin@example.com
* - Specifies how long Squid should wait when its service is asked to stop. If you are running squid on your desktop PC, you may want to set this to something short.
 shutdown_lifetime 10 seconds
* - This is how much memory you want Squid to use to keep objects in memory rather than writing them to disk. Squid's total memory usage will exceed this! By default this is 8MB, so you might want to increase it if you have lots of RAM available.
 cache_mem 64 MB
* - hostname that will be shown in status/error messages
 visible_hostname cerberus
* - If you want your Squid to go through another proxy server, rather than directly out to the Internet, you need to specify it here.
* - Use this option if the parent proxy requires authentication.
* - Tells the cache to never go direct to the internet to retrieve a page. You will want this if you have set the option above.
 cache_peer 10.1.1.100 parent 8080 0 no-query default login=user:password
 never_direct allow all
* - The largest size of a cached object. By default this is 4 MB, so if you have a lot of disk space you will want to increase the size of it to something reasonable.
 maximum_object_size 10 MB

* - This is your cache directory, where all the cached files are stored. There are many options here, but the format should generally go like:
 cache_dir    16 256
So, in the case of a school's internet proxy:
 cache_dir diskd /cache0 200000 16 256
If you change the cache directory from defaults, you must set the correct permissions on the cache directory before starting Squid, else it will not be able to create its cache directories and will fail to start.

## Accessing services on local hostnames
If you plan to access web servers on the LAN using hostnames that are not fully-defined (e.g. http://mywebapp), you may need to enable the  option.  Without this option, Squid will make a DNS request for the hostname verbatim (), which may fail, depending on your LAN's DNS setup.  With the option enabled, Squid will append any domain configured in  when making the request (e.g. ).

## Starting
Once you have finished your configuration, you should check that your configuration file is correct:
 # squid -k check
Then create your cache directories:
 # squid -z
Then you can start/enable .

## Content Filtering
If you are looking for a content filtering solution, see Privoxy.

## Frontend
If you would like a web-based frontend for managing Squid, Webmin is your best bet.

## Squid 4.x not supported in Webmin
If you receive an error indicating your version of webmin is unsupported:

 Your version of Squid is not supported by Webmin. Only versions from 1.1 to 3.4 are supported by this module.

you will need to modify the file  (see issue #952)

## Ad blocking with adzapper
Adzapper is a plugin for Squid. It catches ads of all sorts (even Flash animations) and replaces them with an image of your choice, so the layout of the page is not altered very much.

## Installation
AdZapper is not presently in the official repositories or the AUR. The script itself, and detailed information on configuration and usage, can be found at https://adzapper.sourceforge.net.

## Configuration
 echo "redirect_program /usr/bin/adzapper.wrapper" >> /etc/squid/squid.conf

(squid 2.6.STABLE13-1)

 echo "url_rewrite_program /usr/bin/adzapper.wrapper" >> /etc/squid/squid.conf
 echo "url_rewrite_children 10" >> /etc/squid/squid.conf

If you want, you can edit  to configure adzapper to your liking. The configuration out of the box works wonderfully well though.

## Transparent web proxy
Transparency happens by redirecting all www requests eth0 picks up, to Squid. You will need to add a port with an  (for squid 3.2) parameter.  Note that at least one port must be available without the intercept parameter:

  http_port 3128
  http_port 3129 intercept

And for TLS:

  https_port 3130 intercept ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=4MB cert=/etc/squid/squidCA.pem
  acl step1 at_step SslBump1
  ssl_bump peek step1
  ssl_bump splice all
  # workaround for some sites
  client_persistent_connections off
  server_persistent_connections off

## iptables
From a terminal with root privileges, run:
 # gid=`id -g proxy`
 # iptables -t nat -A OUTPUT -p tcp --dport 80 -m owner --gid-owner $gid -j ACCEPT
 # iptables -t nat -A OUTPUT -p tcp --dport 80 -j DNAT --to-destination SQUIDIP:3129
 # iptables -t nat -A OUTPUT -p tcp --dport 443 -j DNAT --to-destination SQUIDIP:3130
 # iptables-save > /etc/iptables/iptables.rules

Then start the  systemd unit.

Replace SQUIDIP with the public IP(s) which squid may use for its listening port and outbound connections.

## Shorewall
Edit  and add
 REDIRECT	loc	3129	tcp	www # redirect to Squid on port 3128
 ACCEPT		$FW	net	tcp	www # allow Squid to fetch the www content

Restart the  systemd unit.

## HTTP Authentication
Squid can be configured to require a user and password in order to use it. We will use digest http auth

First create a users file with . Enter a password when prompted.

Then add these lines to your :

    auth_param digest program /usr/lib/squid/digest_file_auth -c /etc/squid/users
    auth_param digest children 5
    auth_param digest realm MyRealm

    acl users proxy_auth REQUIRED
    http_access allow users

And restart squid. Now you will be prompted to enter a username and password when accessing the proxy.

You can add more users with . You probably would like to install Apache package, which contains  tool.

## NTLM
Set up samba and winbindd and test it with
  ntlm_auth --username=DOMAIN\\user

Grant r-x access to /var/cache/samba/winbindd_privileged/ directory for squid user/group

Then add something like this to squid.conf:

  auth_param ntlm program /usr/bin/ntlm_auth --helper-protocol=squid-2.5-ntlmssp
  auth_param ntlm children 5
  auth_param ntlm max_challenge_reuses 0
  auth_param ntlm max_challenge_lifetime 2 minutes
  auth_param ntlm keep_alive off

  acl ntlm_users proxy_auth REQUIRED
  http_access allow ntlm_users
  http_access deny all

## Hide Browser’s Real IP Address
Reference: Squid Proxy Hide System’s Real IP Address

## SSL Bumping
Reference: Intercept HTTPS CONNECT messages with SSL-Bump

## Create Self-Signed Root CA Certificate
## Create a DER-encoded certificate to import into users' browsers
The result file (myCA.der) should be imported into the 'Authorities' section of users' browsers.
For example, in FireFox:
    Open 'Preferences'
    Go to the 'Privacy and Security' section
    Press the 'View Certificates' button and go to the 'Authorities' tab
    Press the 'Import' button, select the .der file that was created previously and pres 'OK'

## Modify Squid Configuration File
## Create and initialize TLS certificates cache directory
## Finally, Restart Squid then SSL Bump will work
Restart .

## Troubleshooting
## Squid needs to be restarted after boot
If you are using both squid and NetworkManager, the following error means that squid is launched before the Wi-Fi connection is enabled by NetworkManager ( is empty).

You can:
* Enable NetworkManager-wait-online.service systemd unit.
* Using NetworkManager dispatcher instead of systemd to start squid

Disable the  systemd unit with the following script:

Make sure it is executable

## Additional Resources
* Elite Proxy Config Example (archive.org)
