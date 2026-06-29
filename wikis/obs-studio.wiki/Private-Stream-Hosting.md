# Private Stream Hosting Guide

This guide outlines the high level steps to setup your own private streaming server that can receive a stream from OBS Studio and relay that stream to connected clients. Several guides exist on the steps to achieve this, but, over the years they have not been updated. By remaining high-level this guide should change less often than other guides.


# Software:

    Debian 10
    nginx (build from source)
    nginx-rtmp-module (build from source)


# Prerequisites:

    Have a dedicated server with Debian 10 installed

# Steps:
## Install Necessary Software
    https://github.com/sergey-dryabzhinsky/nginx-rtmp-module/wiki/Building-and-installing-on-Ubuntu-and-Debian
    https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/

Install software packages to be able to compile the nginx source code:

    apt-get install build-essential libpcre3 libpcre3-dev libssl-dev

Download the nginx source code from the nginx website:

    https://nginx.org/en/download.html

Download the nginx-rtmp-module source code from github:

    https://github.com/sergey-dryabzhinsky/nginx-rtmp-module

Configure the nginx source code to compile the nginx-rtmp-module

    ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-dev

Compile nginx

Install nginx to the system

Enable and Start nginx as a service

## Configure NGINX for RTMP Module
    https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/
    https://github.com/arut/nginx-rtmp-module/wiki/Directives

Configure the nginx conf file to include the rtmp configuration settings.


Remember the [NAME] you choose in the application for later.

Whitelist your OBS computer [IP_ADDRESS] for publishing and deny everyone else.

    rtmp {
      server {
        (See nginx configuration for more parameters)
    
        application [NAME] {
          (See nginx-rtmp-module configuration for more parameters)
    
          allow publish [IP_ADDRESS];
          deny publish all;
    
          live on;
          record off;
         }
       }
     }


  Restart the nginx service

## Configure OBS Studio
    https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmp-server-using-nginx.50/

In the OBS Settings, configure the streaming settings.

    Streaming Service: Custom
    Server: rtmp://[SERVER]/[NAME]
    Play Path/Stream Key: [STREAMKEY]

*Note the stream key is not private. This means that the server is relying on the whitelist in step 2 to prevent others using your server to create their own streams.

DO NOT FORGET TO SET THE WHITELIST IN STEP 2!

Clients can play the video in VLC media player using the following url:

    rtmp://[SERVER]/[NAME]/[STREAMKEY]
