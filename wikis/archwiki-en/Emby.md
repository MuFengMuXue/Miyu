# Emby

Emby is a personal media server, which has clients for many platforms.
It is used to organize personal home media, as well as playback on other devices.
There are a large amount of channels that are supported by the community, and can even be used with PVR and Tuner cards to provide TV streaming remotely.

## Installation
Install the  package.

## Usage
Enable and start .

Access Emby through the browser by navigating to http://localhost:8096/

## Write permissions
Emby runs under the user and user group  using systemd's DynamicUser feature. By default, Emby will have at most read permissions to your media files thanks to systemd's filesystem abstraction.

You might want to give emby write permissions and enable media deletion, local metadata saving, subtitle downloading and more.

You will need to create a dedicated group for your media files, or use one you already belong to, and give it access to your folders like so:

 # create the media group
 groupadd media

 # optionally add your_user to the media group
 usermod -aG media your_user

 # give ownership of your media files to the media group
 chgrp -R media /mnt/media_files

 # make the files writeable to the media group
 find /mnt/media_files -type f -exec chmod 664 {} +

 # make the directories writeable to the media group
 find /mnt/media_files -type d -exec chmod 775 {} +

 # add the sticky group bit so that newly created directories belong to the media group
 find /mnt/media_files -type d -exec chmod g+s {} +

Then extend the unit:

This will add the  user to the  group, and enable write permission to the  directory through systemd. Rinse and repeat for any additional media folders you might have.

## Hardware acceleration
Emby supports hardware accelerated transcoding using the GPU. This greatly reduces CPU usage when transcoding, and is for some systems the only option if the CPU itself is not powerful enough.

To check whether hardware acceleration is available, navigate to the transcoding settings in the Emby web interface, and select  under . A list of available hardware encoders and decoders will appear. If nothing is detected, see the following GPU-specific instructions.

## Intel
To enable hardware accelerated video transcoding/decoding for Intel GPUs, install the  package.

Confirm that hardware acceleration is detected with:

 $ ffdetect-emby qsvenc

The output should list detected encoding profiles along with other information.

## NVIDIA
To enable hardware accelerated video transcoding/decoding for NVIDIA GPUs, the NVIDIA drivers are required.

Confirm that hardware acceleration is detected with:

 $ ffdetect-emby nvenc

The output should list detected encoding profiles along with other information.

## Example nginx configuration
 # Based on example from https://emby.media/community/index.php?/topic/47508-how-to-nginx-reverse-proxy/
 server {
     listen 443 ssl;
     listen :::443 ssl;
     server_name emby.yourdomain.com;

     ssl_certificate /etc/letsencrypt/live/emby.yourdomain.com/fullchain.pem; # managed by Certbot
     ssl_certificate_key /etc/letsencrypt/live/emby.yourdomain.com/privkey.pem; # managed by Certbot
     include /etc/letsencrypt/options-ssl-nginx.conf;
     ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
     add_header Strict-Transport-Security "max-age=31536000" always;
     ssl_trusted_certificate /etc/letsencrypt/live/emby.yourdomain.com/chain.pem;
     ssl_stapling on;
     ssl_stapling_verify on;

     # Security / XSS Mitigation Headers
     add_header X-Frame-Options "SAMEORIGIN";
     add_header X-XSS-Protection "1; mode=block";
     add_header X-Content-Type-Options "nosniff";

     location = / {
         return 302 https://$host/web/;
     }

     location / {
         # Proxy main emby traffic
         proxy_pass http://127.0.0.1:8096;

         proxy_hide_header X-Powered-By;
         proxy_set_header Range $http_range;
         proxy_set_header If-Range $http_if_range;

         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
         proxy_set_header X-Forwarded-Protocol $scheme;
         proxy_set_header X-Forwarded-Host $http_host;

         # Disable buffering when the nginx proxy gets very resource heavy upon streaming
         proxy_buffering off;

         # Next three lines allow websockets
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "upgrade";
     }

 }

## Troubleshooting
## No such file or directory
Make sure directory referenced by  exists. If it does not exist  will fail to start with errors. For example if  does not exist systemd will try to use it as a mount:

 emby-server.service: Failed to set up mount namespacing: /run/systemd/unit-root/mnt/media_files: No such file or directory
 emby-server.service: Failed at step NAMESPACE spawning /usr/bin/emby-server: No such file or directory
