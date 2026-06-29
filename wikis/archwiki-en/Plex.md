# Plex

Plex is a media player system and software suite consisting of many player applications for 10-foot user interfaces and an associated media server that organizes personal media stored on local devices. Integrated Plex Channels provide users with access to a growing number of online content providers such as YouTube, Vimeo, TEDTalks, and CNN among others. Plex also provides integration for cloud services including Dropbox, Box, Google Drive, or Copy.

Plex for Linux is split into a closed-source server Plex Media Server, and an open-source client Plex Home Theater, a fork of the popular Kodi project.

## Plex Media Server (PMS)
## Installation
Install  (stable update channel) or  (beta update channel). The latter is only available to Plex Pass subscribers and can provide early access to improvements and/or new functionalities, but also early access to potential bugs. Even though the beta update channel is typically quite stable, it is recommended to install the stable release unless you require specific early access content (release notes).

## Configuration
Start/enable the  systemd unit.

To begin configuring the Plex Media Server, browse to http://localhost:32400/web/.

To configure Plex Media Server remotely, you can first create an SSH tunnel (setup can only be done from )

and then browse to .

or if you are running apache, with a reverse proxy, by adding this configuration in httpd-vhosts.conf

## Custom domain
## Nginx reverse proxy
Below an example server configuration is given for a reverse proxy using Nginx, including certificate configuration.

{{hc|/etc/nginx/sites-available/domain.com.conf|
server {
    listen                  443 ssl http2;
    listen                  ssl http2;
    server_name             media.domain.com;

    # SSL
    ssl_certificate         /etc/letsencrypt/live/media.domain.com/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/media.domain.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/media.domain.com/chain.pem;

    # logging
    access_log              /var/log/nginx/media.domain.com.access.log;
    error_log               /var/log/nginx/media.domain.com.error.log warn;

    # reverse proxy
    location / {
        proxy_pass https://localhost:32400;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# HTTP redirect
server {
    listen      80;
    listen      [:::80;
    server_name media.domain.com;
    include     nginxconfig.io/letsencrypt.conf;

    location / {
        return 301 https://media.domain.com$request_uri;
    }
}
}}

## Plugins
PMS can be expanded with additional plugins. For example, PMS can be used as an IPTV client with the IPTV plugin.

Plugins can be installed inside .

## Plex Live TV and DVR
Plex live TV requires a plexpass.

To enable live TV viewing and DVR support with plex, you must have one of the supported tuners listed on the support page. PMS will automatically recognize any connected tuners.

The plex user needs to be part of the video group in order to access local tuners. This can be done by running

To enable IPTV support via m3u playlist install .

## Hauppauge
The drivers for all Hauppauge tuners have been included in the Linux kernel for some time now (e.g. ~v4.7 for WinTV-DualHD), however the firmware isn’t loaded by default. Look for a kernel message:  by e.g. starting a tail with  and enable/insert the (USB) tuner device. If missing, download the respective firmware file and copy it file to .

## Security
It is recommended to store your media files outside of your home directory, as making it accessible to PMS would mean lowering its security. Having a separate  or  partition is a good setup for use with PMS.

You can further increase security via systemd, by editing  as follows:

## Resource management
Originally, PMS used ulimit to limit its allocated resources, however this is not compatible with running as a regular user. Instead, you can now set a maximum amount of memory via, again, systemd. For example, you can add:

 MemoryMax=4G

to the file mentioned above.

## Network
PMS and its DLNA server require several ports to be open:

*Plex Media Server: TCP 32400
*Plex DLNA Server: TCP 32469, UDP 1900
*Network Discovery: UDP 32410, 32412, 32413, 32414
*Bonjour/Avahi Network Discovery (legacy): UDP 5353

A short example with iptables:

 # iptables -A INPUT -p tcp -m multiport --dports 32400,32469 -j ACCEPT
 # iptables -A INPUT -p udp -m multiport --dports 1900,32410,32412,32413,32414 -j ACCEPT

In order to connect to Plex through on a standard http port, this command can be used (for port 8080):

 # iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 32400

Then you can connect directly to http://yourplexaddress:8080 on this port

## UFW Rule
If you use UFW and would like to create an App List entry for Plex, create/edit  and ensure it contains the following content:

Once you have saved the file, reload the UFW application definitions with:

 # ufw app update plexmediaserver

And then finally allow the Plex app with:

 # ufw allow plexmediaserver-all

## Library Updates
Plex Media Server has a setting "Update my library automatically" which can detect new media files as they are downloaded to your library. But as your library grows, these updates might stop working reliably. To fix, you need to increase the number of files non-root users are allowed to subscribe to via inotify. Create the file

and run  to apply without rebooting. Now plex should see any new files.

## Troubleshooting
Logs are located in .

In case there are no logs or they are not helpful, you might want to launch PMS manually to get some terminal output:

 source /etc/conf.d/plexmediaserver
 [plex$ export LD_LIBRARY_PATH=/usr/lib/plexmediaserver
 /usr/lib/plexmediaserver/Plex\ Media\ Server

## Plex's WebUI returns 404
There may be a situation when updating Plex's WebUI will return 404 Not Found. To fix this you just need to restart .

## Long-running stop job
When logging out, shutting down, or stopping  manually, it may take a long time to finish the systemd stop job. This is possibly due to a bug in the Plex Tuner Service.[https://www.linuxquestions.org/questions/linux-general-1/a-stop-job-is-running-for-plex-4175553076/#post6279191

If you do not use Plex's DVR feature, you can prevent Plex Tuner Service from running. First, stop , then rename  the relevant executable:

 # mv '/usr/lib/plexmediaserver/Plex Tuner Service' '/usr/lib/plexmediaserver/Plex Tuner Service.disabled'

Finally, start  again.

To avoid having to repeat these steps manually after each update, use the NoExtract array in  to block the installation of this file.

## Plex does not detect folder or external drive
In order for Plex to see folders, it needs to be given read and execute permissions. This is due to Plex being run as the user "plex" instead of your user. As such, it will not have access to your /home/ folder by default. The best practice is to put the media into a folder in the root folder (e.g. ) or on an external drive. Then you have to give it read and execute permissions via the code below or by setting it via a file explorer.

If not set already, set the owner/group to your username.

## External drives
If you haven't explicitly set up a mounting configuration for your drives, your desktop environment (e.g. GNOME or KDE) might automatically mount it when you try accessing it via their file explorers. Plex won't be able to access the drive. This is because the desktop environment mounts it to your user (via FUSE), while Plex uses by default the "plex" user.

You will need to manually mount the drives for Plex to see them by setting the mount point. See Fstab for more details. You can also use a program such as KDE Partition Manager or GNOME Disks to set the partition's mount point. Be sure to give the external drive the correct user permissions.

## Plex for Desktop
Plex Desktop is the current release of Plex's desktop media client. It has officially replaced Plex Home Theater (PHT) and Plex Media Player (PMP), and includes downloads for Plex Pass users. PMP reached its EOL in 2020, though it still retains a "TV Mode" (replaced by Plex HTPC). Keep in mind, Plex's desktop app is closed-source.

## Installation
The plex-desktop package can be installed from Snap or the  package.

## Kodi and PleXBMC
With the PleXBMC add-on, Kodi can be used as a replacement for PHT.

## Installation
Install the  package, then follow the instructions at https://kodi.wiki/view/Add-on:PleXBMC.
