# Mattermost

From Mattermost's homepage:

:Mattermost is an open source, self-hosted Slack-alternative. As an alternative to proprietary SaaS messaging, Mattermost brings all your team communication into one place, making it searchable and accessible anywhere.

This article describes how to install and configure the Mattermost server.

## Installation
The Mattermost server can be installed in two ways:

* Using Docker by following the steps described in #With Docker;
* Using a package, by following the steps described in #With package.

An Electron-based desktop client is provided by the  package.

## With Docker
By using Docker, you do not need to manually install a database server and configure Mattermost dependencies. Since the docker image comes with all the dependencies automatically bundled, this is less work for you.

However, the tradeoff is that you cannot choose the database back-end or web server you want, but only those provided in the docker images, unless you make your own.

* Install Docker (including ).
* Download the source:
:
* Edit the  file
** Uncomment the  line.
** For Team edition, remove the comments on the line: .
** Adopt the UID/GID in the section to those of the owner of your  folders.
** Add the port forwarding statements as a child of  section (e.g. between  and )
:
* Build and start the docker container:
:

* Open  in your browser.

Please refer to the official guide for how to configure TLS, email, enable Enterprise features and use several server nodes using Docker Compose.

There are also some Docker images provided on the official Mattermost Docker Hub page. Please also refer to the repository of the Mattermost Docker images.

## With package
Install the  package.

* The installation will create the  user and group.
* The configuration happens in  where  and  are both owned by .
* In  recursively owned by , we can find:
** , a folder where all user files posted via messages, profile pictures and team pictures are stored;
** , a folder related to the webapp client which contains files rewritten by the webapp during runtime and, in the  subfolder, the web plugins installed via the webui;
** , a folder related to the plugins (server part).
* In , a folder created on the fly during the install process (cf. tmpfiles.d) which stores the server logs as json.  and  are both owned by .
* The rest of the immutable Mattermost directory is located at  and is recursively owned by .

Continue with #Database setup.

## Database setup
Mattermost requires a database back-end. If you plan to run it on the same machine, first install either MySQL or PostgreSQL as database.

Follow one of the following sections and then proceed with #Configuring Mattermost.

## MySQL/MariaDB
## PostgreSQL
1. Install and configure PostgreSQL.

2. Choose between TCP or UNIX Socket, and jump to the corresponding section.

## With TCP socket
3. Create the new user while connecting to the server as  user (you will be prompted for a password for the new user):

:

4. Create the Mattermost database, owned by  user:

:

5. PostgreSQL#Configure PostgreSQL to be accessible from remote hosts

6. Verify it works:

:

## With Unix socket
3. Create the new user while connecting to the server as  user:

:

4. Create the Mattermost database, owned by  user:

:

5. Setup the Unix socket by adding the following line to :

:

6. Restart .

7. Verify it works:

:

## Configuring Mattermost
Mattermost is configured in . Strings need to be quoted.

There are two settings you need to adapt to your database.

The  setting:  for MySQL and  for PostgreSQL.

The :
* For MySQL, set it to .
* For PostgreSQL
** TCP socket:
** Unix socket:  ; make sure there are 3 slashes after ,  is the name of the database and  is the directory containing the Unix socket

Start/enable  and open http://localhost:8065/.

## Setting up Mattermost
# Navigate to your Mattermost install and create a team and user.
# The first user in the system is automatically granted the  role, which gives you access to the System Console.
# Click on the menu button in the top left corner and choose the System Console option.
# Update Environment > SMTP settings to setup an SMTP email service. The example below assumes AmazonSES.
#* Set SMTP Server to
#* Set SMTP Server Port to
#* Set Enable SMTP Authentication to true
#* Set SMTP Server Username to
#* Set SMTP Server Password to
#* Set Connection Security to TLS
#* Save the Settings
# Update Site configuration > Notifications:
#* Set Send Email Notifications to true
#* Set Notification Display Name to
#* Set Notification From Address to
#* Set Support Email Address to some real address that can receive emails
#* Save the Settings
# Update Authentication > Email by changing Require Email Verification to true.
# Update Environment > Logging settings by setting Output logs to console to false.
# Feel free to modify other settings.
# Restart .

## Plugins
Plugins are enabled by default, but require access to the plugins directory which needs to be created with the correct owner:

## Tips and tricks
## Valid HTTPS via reverse web-proxy
To securely access your Mattermost server from the Android and iOS apps, which do not support self-signed TLS certificates, you can setup a reverse web proxy.

The main benefits of a proxy are:

* SSL termination
* HTTP to HTTPS redirect
* Port mapping 80 to 8065
* Standard request logs

Proxying can be achieved with most web servers.

## nginx
# Install and run nginx, preferably .
# Point your domain name eg.  to the server.
# Configure nginx to proxy connections from the internet to the Mattermost Server. Create and edit the nginx configuration file . {{bc|
upstream backend {
    server 127.0.0.1:8065;
    keepalive 32;
}

proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

server {
    listen 80;
    server_name    mattermost.example.com;

    location ~ /api/v{
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        client_max_body_size 50M;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Frame-Options SAMEORIGIN;
        proxy_buffers 256 16k;
        proxy_buffer_size 16k;
        client_body_timeout 60;
        send_timeout 300;
        lingering_timeout 5;
        proxy_connect_timeout 90;
        proxy_send_timeout 300;
        proxy_read_timeout 90s;
        proxy_pass http://backend;
    }

    location / {
        client_max_body_size 50M;
        proxy_set_header Connection "";
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Frame-Options SAMEORIGIN;
        proxy_buffers 256 16k;
        proxy_buffer_size 16k;
        proxy_read_timeout 600s;
        proxy_cache mattermost_cache;
        proxy_cache_revalidate on;
        proxy_cache_min_uses 2;
        proxy_cache_use_stale timeout;
        proxy_cache_lock on;
        proxy_pass http://backend;
    }
}
}}
# Enable the mattermost server:
# Restart .
# Verify you can access Mattermost through the proxy:  You should see a page titled .
# Set up Let’s Encrypt.

## Lighttpd2
A configuration sample for  to act as a proxy for Mattermost, assuming you have a certificate at .

See [https://doc.lighttpd.net/lighttpd2/mod_vhost.html mod_vhost if you want to transfer the proxy into a virtual host.

{{hc|/etc/lighttpd2/lighttpd.conf|
setup {

    module_load [
        "mod_accesslog",
        "mod_proxy",
        "mod_openssl"
    ];

    openssl [
        "listen" => "0.0.0.0:443",
        "listen" => ""pemfile" => "/etc/lighttpd2/certs/lighttpd2.pem",
        "options" => ["ALL", "NO_TICKET",
        "verify" => true,
        "verify-any" => true,
        "verify-depth" => 9
    ];

    listen "0.0.0.0:80";
    listen "log ["debug" => "", default => "/var/log/lighttpd2/error.log";
    accesslog "/var/log/lighttpd2/access.log";
    accesslog.format "%h %V %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}\"";

    static.exlude_extensions [ ".php", ".pl", ".fcgi", "~", ".inc" ];

}

openssl.setenv "client-cert";
keepalive.timeout 360;

docroot "/srv/http";
index [ "index.php", "index.html", "index.htm" ];

include "/etc/lighttpd2/mimetypes.conf";

proxy "127.0.0.1:8065";
}}

## Testing translations and pull requests
You can use the unofficial script mattermost-prepare-pkgbuild to test languages and pull requests.
