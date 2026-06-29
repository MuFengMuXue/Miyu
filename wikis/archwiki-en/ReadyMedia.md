# ReadyMedia

ReadyMedia (previously MiniDLNA) is server software with the aim of being fully compliant with DLNA/UPnP clients.  The MiniDLNA daemon serves media files (music, pictures, and video) to clients on a network.  Example clients include applications such as  and Kodi, and devices such as portable media players, smartphones, televisions, and gaming consoles.

ReadyMedia is a simple, lightweight alternative to Gerbera, but has fewer features. It does not have a web interface for administration and must be configured by editing a text file.

## Installation
Install the  package.

If you want to use an unofficial branch which supports transcoding, install the  package.

## Configuration and starting
By default, minidlna runs as a system service (alternatively, you can run it manually). It can be configured in . Set the following necessary settings:

The minidlna service can be managed by  using systemd.

Access to the /home directories is protected by default. To allow access the parameter  needs to be overwritten in

MiniDLNA runs as the minidlna user by default. To change the user it runs as, see #Running minidlna as your own user below.

## Automatic Media_DB Update
ReadyMedia asks the kernel for one inotify watch per folder/subfolder in the Media_Collection Directories set in  to monitor changes, and thus update Media_DB in real time. When MiniDLNA is run as a regular user, it does not have the ability to change the kernel's inotify limits. If default number of inotify watches is non-sufficient to have MiniDLNA monitor all your media folders, increase inotify watches through  (100,000 should be enough for most uses):

 # sysctl fs.inotify.max_user_watches=100000

To have it permanently changed, add to

 # Increase inotify max watchs per user for local minidlna
 fs.inotify.max_user_watches = 100000

inotify performance may depend on device type. Some do not rescan media drives on a consistent basis or at all.  If files are added/deleted to monitored media directories, they may not be noticed until the device DLNA client is restarted.

Check inotify updates via MiniDLNA presentation_url by comparing files count. If it does not change, make sure the user running MiniDLNA has rw access to the DB folder. If the issue persists, copy or download new files first to a non-watched by inotify Downloads folder on the same drive, and then move them to appropriate media folders, since lengthy media files copying or downloading may confuse inotify.

You can also clean or rebuild MiniDLNA DB manually after stopping MiniDLNA daemon, or analyze its debug output (Ctrl+C to exit):

Stop the MiniDLNA daemon.

To rebuild Media_DB forcibly:
 # minidlnad -R
Stop the daemon after rebuilding Media_DB e.g. .

To run in debug mode:
 # minidlnad -d
 to exit it.

## Troubleshooting service autostart
Sometimes the minidlna daemon fails to start while booting. NetworkManager#NetworkManager-wait-online solves this issue. See .

## Running minidlna as your own user
Change  line in , and change the  and  options to directories that are writeable by that user. If you are running without systemd, this is all you need.

If you are using the systemd service, edit  as it will by default run as the  user. To do so, create a  drop-in file:

Copy the  file to  and replace root with your own user and group:

## Running minidlnad without systemd
Alternatively to a system service, you can run minidlna manually. This can be useful if you want to share media but do not have administrator access to the machine.

Create the necessary files and directories locally and edit the configuration:

 $ install -Dm644 /etc/minidlna.conf ~/.config/minidlna/minidlna.conf
 $ $EDITOR minidlna.conf

Configuring should be as above, specifically:

 media_dir=/home/$USER/dir
 db_dir=/home/$USER/.cache/minidlna
 log_dir=/home/$USER/.config/minidlna

You can now start minidlna with the following command:

 $ minidlnad -f /home/$USER/.config/minidlna/minidlna.conf -P /home/$USER/.config/minidlna/minidlna.pid

To autostart it at login, add the previous line to .

## Other aspects
Other aspects and MiniDLNA limitations may need to be considered beforehand to ensure satisfaction from its performance.

## Firewall
If using a firewall the ssdp (1900/udp) and trivnet1 (8200/tcp) ports will need to be opened. For example, this can be done with arno's iptables firewall by editing  and opening the ports by doing:

## iptables
In addition to 1900/udp and 8200/tcp, minidlna may also require allowing muliticasts. An overall configuration for iptables may therefore look like the following snippet, assuming there are separate chains which handle TCP, UDP and IGMP.

  -A TCP -m tcp --dport 8200 -m comment --comment minidlna -j ACCEPT
  -A UDP -d 239.255.255.250/32 -m udp --dport 1900 -m comment --comment "upnp dlna" -j ACCEPT
  -A IGMP -d 224.0.0.1/32 -m comment --comment "igmp membership queries, upnp/dlna" -j ACCEPT
  -A IGMP -d 239.0.0.0/8 -m comment --comment "igmp multicast, upnp/dlna" -j ACCEPT

## File System and Localization
When keeping MiniDLNA Media_DB on an external drive accessible in both Linux and Windows, choose proper file system for it. NTFS preserves in Windows its Linux defaults: rw access for root user and UTF8 font encoding for file names, so media titles in your language are readable when browsing Media_DB in terminal and media players, since most support UTF8. If you prefer Vfat (FAT32) for better USB drive compatibility with older players when hooked directly, or your Media_Collection drive is Vfat and has folder & file names in your local language, MiniDLNA can transcode them to UTF8 charset while scanning folders to Media_DB. Add to Media_Collection and Media_DB drives' mount options your FS language codepage for transcoding to short DOS file names, and iocharset for converting long file names to your terminal's locale, i.g. codepage=cp866,iocharset=utf8 (or ISO-8859-5). Set rw permissions for all users, since Vfat does not preserve Linux access permissions:

While your iocharset would be present in the system with a matching locale, if your terminal or player supports only short file names, check if the set codepage is also present and enabled (like ru_RU.CP866), i.e. was included in system configuration when Arch Linux release was compiled, or consider recompiling the release to add it:

 ls /usr/share/fonts/encodings

MiniDLNA lists Movies and Photos by file name in its DB, and Music entries by ID3 tags instead of file names. If Music collection was not tagged in UTF8 but in a local charset, MiniDLNA might not identify and transcode it correctly to UTF8 for display in media players, or the original tags codepage(s) may be absent in your system, so the tags will not be readable even when media file names are. In this case consider re-tagging your collection to UTF-16BE or UTF-8 encoding with an ID3 Tag Converter.

Picking the "right" file system for your Media_Collection is a trade-off: XFS and EXT4 show fast read/write for HDs and lower CPU load critical for slow computers with attached storage. NTFS is most compatible with Windows when plugging a drive directly for faster copy, while network file systems like Samba, NFS or iSCSI allow import to Windows any Linux FS with slower data copy. As file fragmentation affects playback, store your Movies on a non-system drive formatted in XFS (prevents fragments), NTFS (fragment resistant and easy to defrag), or EXT4 (uses large file extents), and avoid EXT3 or less resistant FAT32. For smaller Flash drives with seldom fragmented Music and Photo files, VFAT (FAT32) and EXT4 show faster writes with less CPU load, but EXT4 may affect memory wear due to journaling, and less compatible with media players. Proper drive partitioning, block alignment and mount options (i.e. async,noatime...- choice depends on file system and memory type) can greatly accelerate flash and HD drive speed among other advantages.

## Media Handling
MiniDLNA is aimed for small devices, so does not generate movie thumbnails to lower CPU load and DB built time. It uses either thumbs in the same folder with movie if any, or extracts them where present from media containers like MP4 or MKV with embedded Album Art tags, but not AVI. One can add thumbs (JPG 160x160 pxl or less) to media folders with a Thumbnail Maker, and miniDLNA will link them to media files after rescan. Larger thumbs will be resized and stored in Media_DB that slows scan. At one movie per folder, follow thumb naming rules in minidlna.conf. For multiple show episodes per folder, each thumb name should match its episode name without ext. (.cover.jpg or .jpg). To handle MS Album Art thumb names with GUID, add * to the end "AlbumArt_{*".jpg . MiniDLNA will list on screen only chosen media type (i.e. Movies), but will not other files in the same folder.

When viewing photos, progressive and/or lossless compression JPG may not be supported by your player via DLNA. Also resize photos to "suggested photo size" by the player's docs for problem free image slideshow. DLNA spec restricts image type to JPG or PNG, and max size to 4096 x 4096 pixels - and that is if the DLNA server implementation supports the LARGE format. The next size limit down (MEDIUM) is 1024 x 768, so resizing may help to show photos correctly.

To decrease system load, MiniDLNA does not transcode on the fly unsupported media files into supported by your player formats. When building Media_DB, it might not correctly identify whether certain formats are supported by your player, which may play via UPnP a broader formats choice. DLNA standard is quite limiting UPnP subset in media containers and codec profiles allowed. If you do not see on TV screen or cannot play some media files listed in Media_DB, check if your HD started spinning or try connecting to your media player via USB for their playback. MiniDLNA might not support choosing audio tracks, subtitles, disk chapters, list sorting, and other advanced playback features for your player model.

## Building a media server
Media served could be based on lightweight and cheap system like development board (Raspberry Pi, CubeBoard, etc.). You do not even need to put X Server on this board.

## Automount external drives
This is very useful if you want to automate the server. See udisks#Mount helpers for more information.

## Issues
Media server based on MiniDLNA could face the drive re-scan issue. Ex.: external HDD you have plugged will be scanned each time again and again. This happens due to MiniDLNA removes DB records for unplugged drive. If your drive plugged all the time it is not a problem, but if you have "pluggable" media library on large external drives this could take a big while till you start watching your video.

One can resolve the rescan issue by using this minidlna fork. It creates a metadata file next to each video file. This can significantly decrease the scan time for large media.

## Troubleshooting
## Server not visible in wireless network
Multicast requests restricted if server connected wirelessly.

* If multicast disabled, minidlna will not see SSDP M-SEARCH client's request  and will not respond.
* Server vanishes after 4:20 because IGMP not enabled.

To solve this, disable "Multicast Isolation" and/or "Multicast to Unicast" on the router. Examples:

* On ADB / Pirelli P.RG EA4202N router, connect to the configuration page, then Settings->Bridge and VLAN->Bridge List->click edit on Bridge Ethernet WiFi->set Multicast Isolation to No->Apply
* Upvel routers: Wireless > Advanced Settings > Multicast to Unicast > Disabled, Multicast rate "Auto"
* D-link: create new static IPoE (IPv4) connection with dummy IP/netmask, go to Advanced > IGMP > Enable and choose created interface.

## Media directory not accessible
Please note that the default systemd service file enforces the parameter . If you intend to share files that reside within the  file system you may want to lessen that restriction.
You can achieve this by updating the systemd unit override file.

## DLNA server stops being visible after some time when being shared on a bridge device
If you are using ReadyMedia to "broadcast" on a bridged device (such as an OpenVPN device bridged to an Ethernet device), the server may stop being seen by the clients after some time (which may vary from a few seconds to half a day).
In order to solve this you need to disable 'multicast snooping'. You can do it instantly with the following command:

 # echo 0 >> /sys/devices/virtual/net/br0/bridge/multicast_snooping

This should make the server visible to the clients *immediately*, but the change will be lost on reboot.
If this works, you can make it a permanent change by using a systemd service file. Edit the file  with the following content:

 Description=Set multicast snoop to off
 After=network-online.target

 [Service
 Type=oneshot
 ExecStart=/usr/bin/bash -c "echo 0 >> /sys/devices/virtual/net/br0/bridge/multicast_snooping"
 RemainAfterExit=true
 ExecStop=/usr/bin/bash -c "echo 1 >> /sys/devices/virtual/net/br0/bridge/multicast_snooping"
 StandardOutput=journal

 Install
 WantedBy=multi-user.target

Now all you have to do is enable .

This approach should disable multicast_snooping on every boot.
