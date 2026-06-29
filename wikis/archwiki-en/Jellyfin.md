# Jellyfin

Jellyfin is a free and open-source multimedia application suite designed to organize, manage, and share digital media files to networked devices.

## Installation
There are a few options for installation:

*  — main server backend
*  — required to host the web frontend. Alternatively, add  to your configuration.
*  — compile from latest commit

Start/enable the  systemd unit. Upon starting for the first time, Jellyfin will create configuration and data directories at  by default.

To begin configuring Jellyfin, browse to http://localhost:8096/ and complete the initial wizard. This is only possible if  was installed.

## Configuration
## Nginx reverse proxy
The below configuration describes a Nginx reverse proxy with a sample certificate. Be sure to modify the template to suit your own circumstances. See upstream documentation for more reverse proxy configuration examples.

{{hc|/etc/nginx/sites-available/domain.com.conf|
server {
    http2 on;
    listen 443 ssl;
    listen ssl;
    server_name DOMAIN_NAME;

    # use a variable to store the upstream proxy
    # in this example we are using a hostname which is resolved via DNS
    # (if you are not using DNS remove the resolver line and change the variable to point to an IP address e.g `set $jellyfin 127.0.0.1`)
    set $jellyfin jellyfin;
    resolver 127.0.0.1 valid=30;

    ssl_certificate /etc/letsencrypt/live/DOMAIN_NAME/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/DOMAIN_NAME/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    add_header Strict-Transport-Security "max-age=31536000" always;

    # Security / XSS Mitigation Headers
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";

    # Content Security Policy
    # See: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
    # Enforces https content and restricts JS/CSS to origin
    # External Javascript (such as cast_sender.js for Chromecast) must be whitelisted.
    #add_header Content-Security-Policy "default-src https: data: blob: http://image.tmdb.org; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' https://www.gstatic.com/cv/js/sender/v1/cast_sender.js https://www.youtube.com blob:; worker-src 'self' blob:; connect-src 'self'; object-src 'none'; frame-ancestors 'self'";

    location = / {
        return 302 https://$host/web/;
    }

    location / {
        # Proxy main Jellyfin traffic
        proxy_pass http://$jellyfin:8096;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Protocol $scheme;
        proxy_set_header X-Forwarded-Host $http_host;

        # Disable buffering when the nginx proxy gets very resource heavy upon streaming
        proxy_buffering off;
    }

    # location block for /web - This is purely for aesthetics so /web/#!/ works instead of having to go to /web/index.html/#!/
    location = /web/ {
        # Proxy main Jellyfin traffic
        proxy_pass http://$jellyfin:8096/web/index.html;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Protocol $scheme;
        proxy_set_header X-Forwarded-Host $http_host;
    }

    location /socket {
        # Proxy Jellyfin Websockets traffic
        proxy_pass http://$jellyfin:8096;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Protocol $scheme;
        proxy_set_header X-Forwarded-Host $http_host;
    }
}
}}

## CSS customization
Server administrators can modify Jellyfin's appearance via the custom CSS field on the web dashboard. Many sources offer portable blocks of CSS to change server typography, colors, and layout. Some examples include [https://github.com/CTalvio/Ultrachromic Ultrachromic and upstream documentation.

## Plugins
Jellyfin features many community-developed plugins that can be installed from the web dashboard. By default, plugins will automatically update.

## File permission
Jellyfin runs as user , which has no permission for your home directory. If you add a directory inside your home directory to a library, Jellyfin fails to access it. You can create a dedicated directory for Jellyfin.

 # mkdir /media

You may want to change the owner of the directory to your current user for easier management.

 # chown $USER: /media

## Intel Quick Sync Video (QSV) accelerated hardware transcoding
The optional dependency  or  must be installed for this to work with the custom  binary.

See the official guide for more details.

## Clients
In addition to the web interface, there are alternative desktop clients available.

*
*
*
*
*

## Troubleshooting
## Jellyfin does not detect folder or external drive
In order for Jellyfin to see folders, it needs to be given read and execute permissions. This is due to Jellyfin being run as the user "jellyfin" instead of your user. As such, it will not have access to your /home/ folder by default. The best practice is to put the media into a folder in the root folder (e.g. ) or on an external drive. Then you have to give it read and execute permissions via the code below or by setting it via a file explorer.

If not set already, set the owner/group to your username.

## External drives
If you have not explicitly set up a mounting configuration for your drives, your desktop environment (e.g. GNOME or KDE) might automatically mount it when you try accessing it via their file explorers. Jellyfin will not be able to access the drive. This is because the desktop environment mounts it to your user (via FUSE), while Jellyfin uses by default the "Jellyfin" user.

You will need to manually mount the drives for Jellyfin to see them by setting the mount point. See Fstab for more details. You can also use a program such as KDE Partition Manager or GNOME Disks to set the partition's mount point. Be sure to give the external drive the correct user permissions.

## Playback issues
Jellyfin sometimes fails to play back specific media files. Most media files should be compatible with Jellyfin as it automatically detects the media format and transcodes (using ) to a format the client can handle. However, this is a complicated process that can fail in various ways. This is made more complicated by the fact that specific Jellyfin plugins use different methods for handling the transcoding process. Hence, the troubleshooting tips are provided below with reference to specific plugins / clients. However, these issues may show up in different Jellyfin clients or with different Jellyfin plugins.

* When using the TVHeadend Jellyfin plugin, recording playback works fine, but viewing live TV fails with an unsupported format error on the client. Check the Dashboard > Playback > Transcode Path configuration. Be sure that there is no trailing slash in the path. For example  is fine, but  is not. This might be fixed in the future. See the issue: https://github.com/jellyfin/jellyfin/issues/10299
* When using the Jellyfin web client, playback of some media files fails randomly. Check that User > Settings > Playback > Maximum Allowed Audio Channels is set to "Stereo". Some browsers do not support 6-channel audio and sometimes some recorded TV broadcasts contain 6-channel audio, causing the web client to fail to playback otherwise valid recordings. Forcing stereo audio should fix this. See this related bug report with some tools shown on how to check the number of audio channels in a video: https://github.com/Dash-Industry-Forum/dash.js/issues/2864.
:

## Web interface redirects to setup wizard after update
Some users report that after an update, the web UI does not allow them to log in, and instead shows them the initial setup wizard. To fix this, ensure that in  the value of  is set to .

## Transcoding is extremely slow with Intel DG2 hardware decode/encode
If transcoding has become extremely slow (less than 5 frames/second) and you are using an Intel DG2/Alchemist GPU for hardware decoding/encoding, ensure you are using the  kernel driver and not the  kernel driver.

See this ticket on the  module issue tracker for more information: https://gitlab.freedesktop.org/drm/xe/kernel/-/issues/234

To disable the  driver, create a file in :

You will need to reboot after creating the file.

## Hardening
Just like any other service, Jellyfin can be hardened by modifying its systemd unit.
Hardening is also called sandboxing in the literature.
The following sandboxing options are an effective way to limit the exposure of the system towards the unit's processes.

Create the following drop-in file:

This will allow Jellyfin to only write to , , ,  and restrict writing to the rest of the file system. It will also deny access to the entire  and limit access to .
This also restrict any access to . Multiple paths can be specified for this option.

More details on the systemd sandboxing options can be found at .
