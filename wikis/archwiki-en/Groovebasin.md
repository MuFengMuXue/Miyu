# Groovebasin

Groovebasin is a music player server with a web-based user interface.

Run it on a server connected to some speakers in your home or office. Guests can control the music player by connecting with a laptop, tablet, or smart phone. Further, you can stream your music library remotely.

Groove Basin works with your personal music library; not an external music service. Groove Basin will never support DRM content.

## Installation
Install the  package from the Arch User Repository.

## Configuration
A configuration file is located in  you need to provide groovebasin with a configuration file or it will create a new one in the current directory named .

## Start the Server
To start groovebasin as a regular user run
 $ groovebasin --start
A unit file is also available to start .

## Web Interface
Open on your browser https://localhost:16242/.

## NGINX Proxy
NGINX can be used to redirect traffic from port 16242 to 80 with the following configuration.

{{hc|/etc/nginx/nginx.conf|
location /groove/ {
        proxy_set_header    X-Real-IP  $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    Host $http_host;
        proxy_redirect      off;
        proxy_http_version  1.1;
        proxy_set_header    Upgrade $http_upgrade;
        proxy_set_header    Connection "upgrade";
        proxy_pass          http://127.0.0.1:16242/;
}
}}
