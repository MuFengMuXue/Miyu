**翻译状态：**

  * 本文（或部分内容）译自 [Kodi](<https://wiki.archlinux.org/title/Kodi> "arch:Kodi")，最近一次同步于 2024-09-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kodi?diff=0&oldid=811998>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kodi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译（在 [Talk:Kodi#](<../zh-cn/Talk:Kodi.html>) 中讨论）

[Kodi](<https://kodi.tv/>) (formerly known as XBMC) is an award-winning free and open source (GPL) software media player and entertainment hub that can be installed on Linux, OSX, Windows, iOS and Android, featuring a 10-foot user interface for use with televisions and remote controls. These can all be played directly from a CD/DVD, or from the hard-drive. Kodi can also play multimedia from a computer over a local network (LAN), or play media streams directly from the Internet. It can also be used to play and record live TV using a tuner, a backend server and a PVR plugin; more information about this can be found on the [Kodi wiki](<https://kodi.wiki/view/PVR>). 

## Installation

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [kodi](<https://archlinux.org/packages/?name=kodi>)包 package. Users wanting HDR support should instead install the [kodi-gles](<https://archlinux.org/packages/?name=kodi-gles>)包 package. Be sure to review/install optional dependencies listed by pacman to enable additional functionality. 

### Setup

Both packages support several composers, with varying levels of functionality: 

[GBM](<https://en.wikipedia.org/wiki/Mesa_\(computer_graphics\)#Generic_Buffer_Management> "wikipedia:Mesa \(computer graphics\)")
    currently the most feature rich. It is the only one of the three options able to display HDR content, may be a good choice for standalone operations since it runs directly on the GPU without the need for the added X11 layer. A complete list of features lacking compared to other back-ends can be found in [Kodi issue 14876](<https://github.com/xbmc/xbmc/issues/14876>).
[Xorg](<../zh-cn/Xorg.html> "Xorg")
    should be considered on-par with GBM.
[Wayland](<../zh-cn/Wayland.html> "Wayland")
    a known limitation is having the resolution and frame rate set in the compositor rather than in Kodi's GUI; also currently does not support VT switching.

All of the official addons in the [kodi-addons](<https://archlinux.org/groups/x86_64/kodi-addons/>)包组 group are disabled by default and need to be enabled in Kodi's addon menu after installation. 

### Hardware video acceleration

Enable and configure [hardware video acceleration](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration") to speed up playback performance. Once installed, the hardware backend(s) are presented under _Settings > Player > Videos_. 

**注意：** A level of "Advanced" or "Expert" needs to be set in order to show all options.

## Running

There are two general use cases: 

  1. `/usr/bin/kodi` is meant to be run by any user on an on-demand basis. Use it like any other program on the system.
  2. `/usr/bin/kodi-standalone` is meant to be run as the only graphical application, for example on a [HTPC](<https://en.wikipedia.org/wiki/Home_theater_PC> "wikipedia:Home theater PC"). See [#Running standalone](<#Running_standalone>) for more information.

## Running standalone

Using standalone mode is advantageous for several reasons: 

  1. One can define an unprivileged user to run kodi and have no access to a shell.
  2. When paired with a systemd unit (or equivalent, see below), this setup makes the box on which kodi is running more like an appliance.

**警告：** Select **only one** of the methods listed below.

### kodi-standalone service

[kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR provides three services and automatically creates and provisions the unprivileged user to run Kodi in standalone mode. 

  * `kodi-x11.service`
  * `kodi-gbm.service`
  * `kodi-wayland.service`

**注意：**

  * The correct video driver and optionally [hardware video acceleration](<../zh-cn/Hardware_video_acceleration.html> "Hardware video acceleration") are assumed dependencies.
  * The home/userdata directory for the created `kodi` user is `/var/lib/kodi/`.
  * Certain use cases may require environment variables to be passed to the service. Define these variables in `/etc/conf.d/kodi-standalone` and they will be passed along to the service.
  * If `kodi-x11.service` fails to start, see [Xorg#Rootless Xorg](<../zh-cn/Xorg.html#Rootless_Xorg> "Xorg") for possible workarounds (this is uncommon).
  * `kodi-gbm.service` and `kodi-wayland.service` do not allow exiting to another virtual console.

####  Recommended methods to reboot/shutdown using kodi-standalone service

**警告：** Be aware that these services run Kodi in systemd's _system.slice_ , not _user.slice_. In order to have Kodi exit gracefully, initiate system reboot/shutdown with the respective Kodi actions **instead of** using _systemctl_. Failure to do so will result in an ungraceful exit of Kodi and the possible loss of GUI settings, Kodi uptime etc.

In principal this is no different than data loss occurring from a user doing work when a sysadmin issues a reboot command without prior warning. While it is possible to run Kodi in systemd's _user.slice_ instead, doing so makes it difficult to use USB mounts within Kodi and to use pulseaudio for Kodi sessions. 

  * **Kodi GUI** : Selecting the corresponding option under power menu in the Kodi GUI.
  * **Mobile device** : The official Android/iOS apps can also perform these actions (assuming the corresponding options are enabled in Kodi).
  * **CLI** : Use `kodi-send` provided by [kodi-eventclients](<https://archlinux.org/packages/?name=kodi-eventclients>)包 to send the `ShutDown()` or the `Reboot` command. The syntax is:

    $ kodi-send -a Reboot
    $ kodi-send -a ShutDown()
    
### Xsession with LightDM

**注意：** This assumes that a kodi user named `kodi` is on the system and that the following file is present as described.

To use LightDM with automatic login, see [LightDM#Enabling autologin](<../zh-cn/LightDM.html#Enabling_autologin> "LightDM") and [LightDM#Enabling interactive passwordless login](<../zh-cn/LightDM.html#Enabling_interactive_passwordless_login> "LightDM"). _Kodi_ includes `kodi.desktop` as [xsession](</wzh/index.php?title=Xsession&action=edit&redlink=1> "Xsession（页面不存在）"). 
    
    /etc/lightdm/lightdm.conf
    
    [Seat:seat0]
    pam-service=lightdm-autologin
    autologin-user=kodi
    autologin-user-timeout=0
    user-session=kodi

### Xsession with NoDM

[Nodm](</wzh/index.php?title=Nodm&action=edit&redlink=1> "Nodm（页面不存在）") is an automatic display manager which automatically starts an X session at system boot. 

By creating a [user](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "User") for kodi (e.g. `useradd -mU kodi`) and [install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install")ing [nodm](<https://archlinux.org/packages/?name=nodm>)包 we simply have to specify the kodi user inside: 
    
    /etc/nodm.conf
    
    NODM_USER=kodi
    NODM_XSESSION=/home/kodi/.xinitrc

Make sure to execute `kodi` inside the [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") file. 

**注意：** The `.xinitrc` file must be executable, so the `kodi` user's home must not be mounted with the `noexec` option.

### Socket activation

Socket activation can be used to start Kodi when the user issues a Wakeup command from a remote control app like Kore, or makes a connection to Kodi's html control port. Start listening by [starting](</wzh/index.php?title=Starting&action=edit&redlink=1> "Starting（页面不存在）") `kodi@_user_.socket` (replace _user_ with the user running Kodi to be started as). 

There are no packaged `kodi@.service` and `kodi@.socket` files, one must create them manually. Depending on the setup, one can optionally change the ports in `kodi@.socket`. 
    
    /etc/systemd/system/kodi@.service
    
    # This fails if the user does not have an X session.
    [Unit]
    Description=Launch Kodi on main display
    Conflicts=kodi.socket
    
    [Service]
    Type=simple
    Environment=DISPLAY=:0.0
    Nice=-1
    ExecStart=/usr/bin/su %i /usr/bin/kodi
    ExecStopPost=/usr/bin/systemctl --no-block start kodi@%i.socket
    
    [Install]
    WantedBy=multi-user.target
    
    /etc/systemd/system/kodi@.socket
    
    [Unit]
    Conflicts=kodi@%i.service
    
    [Socket]
    # Unset 
    ListenStream=
    # Start when receiving a TCP request on the http control port
    ListenStream=8080
    # start when receiving an UDP datagram (Wakeup/WOL)
    ListenDatagram=9
    
    [Install]
    WantedBy=sockets.target
    
###  Start from remote control with LIRC / irexec

Kodi can be configured to start via a key press. Users will need [kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR and [lirc](<https://archlinux.org/packages/?name=lirc>)包. This can be useful on setups running 24/7 and having kodi up on demand. 

See the corresponding [LIRC](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）") article and create a functional setup with a remote. Also, the package [kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR has to be installed. 

Generate the file `/var/lib/kodi/.lircrc` with the following content: 
    
    /var/lib/kodi/.lircrc
    
    begin
    prog = irexec
    remote = devinput
    button = KEY_MEDIA
    config = pgrep kodi-standalone || /usr/bin/kodi-standalone -l /run/lirc/lircd
    repeat = 0
    end
    
Adopt `button` to whatever button on the remote is to start Kodi. One can use _irw_ (see [LIRC#Testing](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）")) to find out the correct values for `remote` and `button`. 

Create a [drop-in](<../zh-cn/Systemd.html#Drop-in_files> "Systemd") for `kodi-xxx.service`: 
    
    /etc/systemd/system/kodi-xxx.service.d/lirc.conf
    
    [Service]
    ExecStart =
    ExecStart = /usr/bin/irexec

[Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `kodi-xxx.service` and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") it to run at boot time. 

## Using a remote control

As Kodi is geared toward being a remote-controlled media center via an official app, physical remote control, or USB/bluetooth keyboard/mouse. 

### Using the Android or iOS app

Both Android and iOS users can use the official app (currently free of charge) to control kodi once it is correctly setup to do so. Steps to configure both Kodi and the app are detailed on the [Official Kodi Remote](<https://kodi.wiki/view/Official_Kodi_Remote>) and [Kore Manual](<https://kodi.wiki/view/Kore_Manual>) page. 

**提示：** Kore provides [power management](<../zh-cn/Power_management.html> "Power management") actions to perform remotely [suspend](</wzh/index.php?title=Suspend&action=edit&redlink=1> "Suspend（页面不存在）")/[hibernation](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html> "Hibernation") and [Wake-on-LAN](<../zh-cn/Wake-on-LAN.html> "Wake-on-LAN") (WoL).

### Using a physical remote control

Any PC with a supported IR receiver/remote, can use [LIRC](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）") or even kernel supported modules to drive it. Configuring specific remotes with lirc is covered on the [LIRC](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）") article. 

To work properly with Kodi, a file that maps the lirc events to Kodi keypresses is needed. Create an [XML](<https://en.wikipedia.org/wiki/XML> "wikipedia:XML") file at `~/.kodi/userdata/Lircmap.xml` (note the capital 'L'). 

**注意：** Users running Kodi started with [kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR will find the `kodi` user's home (`~`) under `/var/lib/kodi/` and should substitute this in for the shortcut above. Also make sure that if creating this file as the root user, it gets proper [ownership](</wzh/index.php?title=Ownership&action=edit&redlink=1> "Ownership（页面不存在）") as `kodi:kodi` when finished.

`Lircmap.xml` format is as follows: 
    
    <lircmap>
      <remote device="devicename">
          <XBMC_button>LIRC_button</XBMC_button>
          ...
      </remote>
    </lircmap>

  * **Device Name** is whatever LIRC calls the remote. This is set using the **Name** directive in lircd.conf and can be viewed by running `irw` and pressing a few buttons on the remote. IRW will report the name of the button pressed and the name of the remote will appear on the end of the line.
  * **XBMC_button** is the name of the button as defined in [keymap.xml](<https://kodi.wiki/view/Keymap>).
  * **LIRC_button** is the name as defined in `lircd.conf`. If `lircd.conf` was autogenerated using `irrecord`, these are the names selected for the buttons. Refer back to [LIRC](</wzh/index.php?title=LIRC&action=edit&redlink=1> "LIRC（页面不存在）") for more information.
  * A very thorough [LIRC](<https://kodi.wiki/view/LIRC>) page hosted on the Kodi Wiki should be consulted for more help and information on this subject as this is out of scope of this article.

### HDMI-CEC

With a supported [USB-CEC adapter](<https://www.pulse-eight.com/p/104/usb-hdmi-cec-adapter>), Kodi can be used to automatically turn on and off the TV and other home theater equipment. Volume control from Kodi can be sent to a supported amplifier, one can manage DVD or Blu-Ray players from inside Kodi, and redirect the active source on the TV to whichever equipment needs it, all from one remote control. For more information see the [official Kodi wiki page on CEC](<https://kodi.wiki/view/CEC>) and [libCEC FAQ](<https://libcec.pulse-eight.com/faq>). 

Install [libcec](<https://archlinux.org/packages/?name=libcec>)包. 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Add reference for the need to add users to these groups. (在 [Talk:Kodi](<../zh-cn/Talk:Kodi.html>) 中讨论)

When connected, the USB-CEC's `/dev` entry (usually `/dev/ttyACM*`) will default to being owned by the `uucp` group, so in order to use the device the user running Kodi needs to belong to that group. See [Users and groups#Group management](<../zh-cn/Users_and_groups.html#Group_management> "Users and groups") for instructions on how to add users to groups. 

  * Add all users that will use Kodi to the `uucp` [user group](<../zh-cn/User_group.html> "User group").

**注意：** Trying to use the USB-CEC without belonging to above groups may lead to problems, including Kodi crashes, so make sure the correct user belongs to both groups.

### Using a gamepad

Install [kodi-addon-peripheral-joystick](<https://archlinux.org/packages/?name=kodi-addon-peripheral-joystick>)包. 

First, confirm that the [gamepad](<../zh-cn/%E6%B8%B8%E6%88%8F%E6%89%8B%E6%9F%84.html> "Gamepad") is detected by the OS, navigate to _Kodi Settings > Input > Peripherals_ and confirm your device is listed. Then, enter the _Configure attached controllers_ submenu. Kodi will prompt to press buttons on the controller one at a time. Once the mapping is finished, the gamepad should be able to control the UI. 

## Sharing media and a centralized database across multiple nodes

If multiple PCs on the same network are running Kodi, they can be configured to share a single media library (video and music). The advantage of this is media and key metadata are stored in one place, and are shared/updated by all nodes on the network. For example, users of this setup can: 

  * Stop watching a movie or show in one room then finish watching it in another room automatically.
  * Share watched and unwatched status for media on all nodes.
  * Simplify the setup with only a single library to maintain.

As well, the media itself can be located in one space thus allowing a lighter footprint of client systems (ie no need for large HDD space). 

Several things are needed for this to work: 

  * Network exposed media (via protocols that Kodi can read, e.g. NFS or Samba).
  * A [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") server.

**警告：** When sharing a database, ALL clients need to be on the same major version of Kodi due to versioned requirements of the database schema. Refer to [database version table](<https://kodi.wiki/view/Databases#Database_Versions>) for a list of database versions.

**注意：** The following guide is only an example of one configuration and is not meant to be limiting but illustrative. Key steps are shown but a detailed discussion is not offered.

These assumptions are used for the guide, substitute as needed: 

  * The media is located under following mount points: `/mnt/shows` `/mnt/movies` `/mnt/music`.
  * The network addresses of all nodes are within the 192.168.0.* subnet range.
  * The IP address of the machine running both the NFS exports and the MariaDB database is 192.168.0.105.
  * Each Kodi box is referred to as a node.
  * The Linux user running Kodi is 'kodi' on all nodes.

For additional info, refer to the [official Kodi wiki](<https://kodi.wiki/view/MySQL/Setting_up_MySQL#Arch_Linux>). 

### NFS server export example

This section provides an example using exports, see [NFS](<../zh-cn/NFS.html> "NFS") for install and usage. Nexus v20.0 of Kodi contains initial support for NFSv4 exports. A limitation is that users of NFSv4 exports will have to manually add the exports/browsing the NFS network is not currently supported. Users will also need to restart Kodi after the sources have been added. Using a NFSv3 export does not have these caveats. 

Users wanting a pure NFSv4 setup should see [NFS#Starting the server](<../zh-cn/NFS.html#Starting_the_server> "NFS") in order to keep things clean. Of course, this only applies to the box running the NFSv4 exports. 

**注意：** Users only need one box on the LAN to serve the content, therefore, do not repeat this for each node. The following example assumes the user is running Arch Linux, but any NFS server will work, be it Linux or BSD, etc.

Create an empty directory in NFS root for each media directory to be shared. E.g.: 
    
    # mkdir -p /srv/nfs/{shows,movies,music}
    
[Bind mount](<../zh-cn/NFS.html#Server> "NFS") the media directories to the empty directories in `/srv/nfs/`. 

The following example is for a NFSv3 [exports](<../zh-cn/NFS.html#Server> "NFS"): 
    
    /etc/exports.d/kodi.exports
    
    /srv/nfs          192.168.0.0/24(ro,fsid=0,no_subtree_check)
    /srv/nfs/shows    192.168.0.0/24(ro,no_subtree_check,insecure)
    /srv/nfs/movies   192.168.0.0/24(ro,no_subtree_check,insecure)
    /srv/nfs/music    192.168.0.0/24(ro,no_subtree_check,insecure)

The following example is for a NFSv4 [exports](<../zh-cn/NFS.html#Server> "NFS"): 
    
    /etc/exports.d/kodi.exports
    
    /srv/nfs          192.168.0.0/24(ro,fsid=0,no_subtree_check,insecure,async,all_squash,pnfs,anonuid=99,anongid=99)
    /srv/nfs/shows    192.168.0.0/24(ro,no_subtree_check,insecure,async,all_squash,pnfs,anonuid=99,anongid=99)
    /srv/nfs/movies   192.168.0.0/24(ro,no_subtree_check,insecure,async,all_squash,pnfs,anonuid=99,anongid=99)
    /srv/nfs/music    192.168.0.0/24(ro,no_subtree_check,insecure,async,all_squash,pnfs,anonuid=99,anongid=99)

### Install and set up the MariaDB server

See [MariaDB](<../zh-cn/MariaDB.html> "MariaDB") for installation and configuration instructions. 

To create a database for Kodi, use the following commands: 
    
    $ mysql -u root -p
       <<enter the mariadb root password assigned in the first step>>
    MariaDB [(none)]> CREATE USER 'kodi' IDENTIFIED BY 'kodi';
    MariaDB [(none)]> GRANT ALL ON *.* TO 'kodi';
    MariaDB [(none)]> flush privileges;
    MariaDB [(none)]> \q
    
### Set up Kodi to use the MariaDB library and the NFS exports

#### Set up Kodi to use the common SQL database

To tell Kodi to use the common database, insure that Kodi is not running, then create the following file: 
    
    ~/.kodi/userdata/advancedsettings.xml
    
    <advancedsettings>
      <videodatabase>
        <type>mysql</type>
        <host>192.168.0.105</host>
        <port>3306</port>
        <user>kodi</user>
        <pass>kodi</pass>
      </videodatabase>
    
      <musicdatabase>
        <type>mysql</type>
        <host>192.168.0.105</host>
        <port>3306</port>
        <user>kodi</user>
        <pass>kodi</pass>
      </musicdatabase>
    
      <videolibrary>
        <importwatchedstate>true</importwatchedstate>
        <importresumepoint>true</importresumepoint>
      </videolibrary>
    </advancedsettings>
    
**提示：** If using [kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR, the default for the profile is `/var/lib/kodi/.kodi` and be sure to chown the newly created file to the kodi user and group, i.e. `chown kodi:kodi /var/lib/kodi/.kodi/userdata/advancedsettings.xml`

#### Set up network shares

For NFSv3 shares, load Kodi and define the network shares that correspond to the exports by browsing to the following within the interface _Video > Files > Add Videos > Browse > Network Filesystem(NFS)_. 

After a few seconds, the IP address corresponding to the NFS server should appear. 

Select `/srv/nfs/shows` from the list of share and then _OK_ from the menu on the right. Assign this share the category of _TV Shows_ to setup the appropriate scraper and to populate the SQL database with the correct metadata. 

Repeat this browsing process for the "movies" and "music" and then exit Kodi once properly configured. At this point, the SQL tables should have been created. 

For NFSv4 shares, user cannot browse the network but will have to manually define them under _Video > Files > Add Videos > Browse > Add network location..._ For there, change the Protocol to "Network File System (NFS)" and then define the server address (numerical IP or hostname) and then define the share under the Remote path section. Repeat for each export. 

**注意：** Even if Kodi is running on the same box that is also running the NFS exports and SQL server, one **must** setup the media using the nfs shares only.

### Cloning the configuration to other nodes on the network

To set up another Kodi node on the network to use this library, simply copy `~/.kodi/userdata/advancedsettings.xml` to that box and restart Kodi. There is NO need to copy any other files or to do any other setup steps on the new kodi node. The nfs exports, the metadata for the programming, any stop/start times, view status, etc. are all stored in the SQL tables. 

**注意：** One can optionally define other media sources that are not managed by kodi database, but they will be specific to that particular node.

## Tips and tricks

### Keep a log of what is watched

Keep track of every video watched on kodi with [kodi-logger](<https://aur.archlinux.org/packages/kodi-logger/>)AUR. 

###  Speedup video playback (synchronized audio and video) up to 1.5x

To enable speed-up and slow-down with audio/video sync (0.8x - 1.5x) do the following: 

  * Create the following file that will map the `[` and `]` keys to the `tempo down` and `tempo up` actions, respectively:

    ~/.kodi/userdata/keymaps/custom.xml
    
    <keymap>
      <FullscreenVideo>
        <keyboard>
          <opensquarebracket>PlayerControl(tempodown)</opensquarebracket>
          <closesquarebracket>PlayerControl(tempoup)</closesquarebracket>
        </keyboard>
      </FullscreenVideo>
      <VideoMenu>
        <keyboard>
          <opensquarebracket>PlayerControl(tempodown)</opensquarebracket>
          <closesquarebracket>PlayerControl(tempoup)</closesquarebracket>
        </keyboard>
      </VideoMenu>
    </keymap>

  * Restart kodi which will read in these changes.
  * Navigate to _System > Player > Videos > Playback_ and enable "Sync playback to display" option.

**注意：** The following bug affecting GBM (but not affecting X11) is triggered by enabling this option. The bug manifests in sporadic A/V sync errors accompanied by entries in the `kodi.log` such as: `WARNING <general>: ActiveAE - large audio sync error: -89449.339487`, see [upstream bug #22625](<https://github.com/xbmc/xbmc/issues/22625>).

### Modify default values for watch and resume points

Some users may wish to make the thresholds Kodi uses to create a resume point/consider a video "watched" entirely. Do so by editing `~/.kodi/userdata/advancedsettings.xml` inserting the following three xml fields: 

ignoresecondsatstart
    the number of seconds to wait before keeping track of the start point. If users watch a value below the one defined, no start point is recorded. Default is 180.
playcountminimumpercent
    the percentage of total play time to consider something watched. If users watch more of the video that this number but not the entire video, it is considered watched and any previously recorded resume point is deleted upon stopping and finally, the video is flagged as watched. Default is 90.
ignorepercentatend
    the percentage of total play time at the end of a video to ignore making a resume point. This is related to the previous setting except it considers the last x percent of the video. If users watch enough content to enter this space of the file, no resume point is saved and the video is flagged as watched. Default is 8.
    
    ~/.kodi/userdata/advancedsettings.xml
    
    <advancedsettings>
      <video>
        <!-- see https://kodi.wiki/view/HOW-TO:Modify_automatic_watch_and_resume_points -->
        <ignoresecondsatstart>10</ignoresecondsatstart>
        <playcountminimumpercent>90</playcountminimumpercent>
        <ignorepercentatend>8</ignorepercentatend>
      </video>
    </advancedsettings>
    
### CLI for kodi

  * [kodi-eventclients](<https://archlinux.org/packages/?name=kodi-eventclients>)包 package provides `kodi-send` which can send valid [kodi action](<https://kodi.wiki/view/Action_IDs>) or [kodi function](<https://kodi.wiki/view/List_of_built-in_functions#List_of_functions>) to kodi from the shell.

  * [texturecache](<https://aur.archlinux.org/packages/texturecache/>)AUR can handle many aspects of library management, from clean-up of unused images, to searching, to querying what is currently playing.

###  Use Kodi to view security camera streams (rtsp or rtmp)

Since Kodi uses ffmpeg for video playback, it is able to play streams such as rtsp and rtmp can be viewed. To do so, simply create a txt file in the filesystem exposed to the kodi user containing the stream. For example: 
    
    $ cat front-door.strm
    
    rtsp://username:password@10.1.10.101

Optionally meta-data, such as cover art and summaries can also be associated to the _.strm_ file just like normal entries in a library by using an NFO file. 

### UPnP and DLNA

Go to _Settings > Services > UPnP/DLNA_ and toggle _Enable UPnP support_. 

###  Adjusting CD/DVD drive speed

The _eject_ program from the [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 package does a nice job for this, but its setting is cleared as soon as the media is changed. 

This udev-rule reduces the speed permanently: 
    
    /etc/udev/rules.d/dvd-speed.rules
    
    KERNEL=="sr0", ACTION=="change", ENV{DISK_MEDIA_CHANGE}=="1", RUN+="/usr/bin/eject -x 2 /dev/sr0"

Replace `sr0` with the device name of the optical drive. Replace `-x 2` with `-x 4` if the preference is 4x-speed instead of 2x-speed. 

After creating the file, reload the udev rules with 
    
    # udevadm control --reload
    
### Use port 80 for webserver

Kodi has a webservice that allows interaction through a web-interface. By default, it uses port `8080` as `80` requires root privileges. Use the following to permit it to use low port numbers: 
    
    # setcap 'cap_net_bind_service=+ep' /usr/lib/kodi/kodi.bin
    
Restart Kodi and set port `80` in the configuration menu (_Services > Webserver > Port_). 

### Using ALSA

If [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") or [PipeWire](<../zh-cn/PipeWire.html> "PipeWire") do not work properly, try forcing [ALSA](<../zh-cn/ALSA.html> "ALSA") by launching Kodi with the `--audio-backend=alsa` flag. 

One method to set the audio backend permanently is to [create a custom systemd unit](<../zh-cn/Systemd.html#Writing_unit_files> "Systemd"), or, alternatively, [edit](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") one from [kodi-standalone-service](<https://aur.archlinux.org/packages/kodi-standalone-service/>)AUR. 

###  Audio passthrough output device list in Kodi 21+

One can allow an external receiver or sound bar to decode audio by enabling passthrough. This is useful for files encoded in TrueHD or Atmos. If using PulseAudio, follow the instructions at <https://kodi.wiki/view/PulseAudio> to first enable passthrough in PulseAudio. Once complete, the corresponding passthrough options should appear in Kodi. When forcing ALSA by launching Kodi with `--audio-backend=alsa`, the passthrough options will appear in Kodi automatically. 

**注意：**

  * PulseAudio requires the output in Kodi to be set to 2 channel. Audio encoded in formats not passed through will only be sent as stereo audio. Use ALSA to support passthrough and passing decoded surround audio signals
  * PulseAudio does not support TrueHD, DTS-MA, or Atmos passthrough. Use ALSA to pass these to through the receiver.

Another way of getting TrueHD and DTS-MA passthrough without disabling Pulseaudio or Pipewire-Pulse is to use an external player like MPV, first create the file `~/.kodi/userdata/playercorefactory.xml` then paste the following into it: 
    
    <playercorefactory>
      <players>
        <player name="MPV" type="ExternalPlayer" audio="false" video="true">
          <filename>/usr/bin/mpv</filename>
          <args>--fs=yes "{1}"</args>
          <hidexbmc>true</hidexbmc>
        </player>
      </players>
      <rules action="prepend">
        <rule video="true" player="MPV"/>
      </rules>
    </playercorefactory>
    
[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[mpv](<../zh-cn/Mpv.html> "Mpv")。**

**附注：** Appears to partially duplicate [mpv#Specify an audio output](<../zh-cn/Mpv.html#Specify_an_audio_output> "Mpv") and [mpv#HD Audio passthrough](<../zh-cn/Mpv.html#HD_Audio_passthrough> "Mpv").（在 [Talk:Kodi](<../zh-cn/Talk:Kodi.html>) 中讨论）

MPV should now be the default media player for Kodi. To set the correct audio output device for MPV, use the following command to show a list of available audio devices: 
    
    $ mpv --audio-device=help
    
For example: 
    
    alsa/hdmi:CARD=NVidia,DEV=1
    
Now edit `~/.config/mpv/mpv.conf` and add the following lines: 
    
    audio-spdif=ac3,eac3,dts-hd,truehd
    audio-device=alsa/hdmi:CARD=NVidia,DEV=1
    
To have auto switching of refresh rates create the following folder `~/.config/mpv/scripts` then download and place [mpv-plugin-xrandr/xrandr.lua](<https://github.com/lvml/mpv-plugin-xrandr/blob/master/xrandr.lua>) into that folder. 

### Kodi JSON-RPC API to alter settings from external tools

Users can interact directly with Kodi on the CLI or from a python script etc. by making use of the [JSON-RPC API](<https://kodi.wiki/view/JSON-RPC_API/v12>). 

For example, using [curl](<https://archlinux.org/packages/?name=curl>)包: 
    
    $ curl -v -H "Content-type: application/json" -d \
      '{"jsonrpc":"2.0","id":1,"method":"Settings.GetSettingValue","params":{"setting":"audiooutput.audiodevice"}}' \
      <http://localhost:8080/jsonrpc> -u xbmc:xbmc
    
Another example is [this python script](<https://github.com/graysky2/streamzap/blob/master/kodi/audio_switch/audio_switch.py>) which simply toggles between two groups of settings, in this case, toggling the audio source back-and-forth between HDMI and optical out. 

### Fix for delayed startup on wifi

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** Duplicates [systemd-networkd#systemd-networkd-wait-online](<../zh-cn/Systemd-networkd.html#systemd-networkd-wait-online> "Systemd-networkd"). (在 [Talk:Kodi](<../zh-cn/Talk:Kodi.html>) 讨论)

If running with WiFi only (wired network unplugged) while [#Sharing media and a centralized database across multiple nodes](<#Sharing_media_and_a_centralized_database_across_multiple_nodes>), kodi will likely start before the wireless network is up, which will result in failure to connect to the shares and to the SQL server. Assuming the network is managed by [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd"), this can be fixed by using a [drop-in file](<../zh-cn/Drop-in_file.html> "Drop-in file"): 
    
    /etc/systemd/system/systemd-networkd-wait-online.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/lib/systemd/systemd-networkd-wait-online --ignore eth0

### Run kodi in a window manager

Users running kodi in a [Window manager](<../zh-cn/Window_manager.html> "Window manager") may see a black screen at exit. To fix this, try switching to another tty. A possible solution is to run kodi with this script (running as the root user): 
    
    kodi.sh
    
    #!/bin/sh
    kodi-standalone
    sudo chvt 2 
    sleep 1
    sudo chvt 1
    
To make sure that [sudo](<../zh-cn/Sudo.html> "Sudo") does not ask for password for `chvt` add this line to `sudoers` file: 
    
    /etc/sudoers
    
    _UserNameHere_ ALL=NOPASSWD: /usr/bin/chvt

### USB DAC not working

Users of USB DAC/sound cards may experience distorted sound/clicks/pops or no sound at all when selecting it from Audio settings. A possible fix: 

Open `guisettings.xml` (it should be under `/var/lib/kodi/.kodi/userdata/` if using the supplied `kodi-xxx.service`) and change 
    
    <processquality default="**true** ">**101** </processquality>
    
to 
    
    <processquality default="**false** ">**100** </processquality>
    
### Virtual file system support

Kodi provides addons for accessing various virtual file systems from within Kodi. RAR archives can be accessed using [kodi-addon-vfs-rar](<https://aur.archlinux.org/packages/kodi-addon-vfs-rar/>)AUR. SFTP shares can be accessed using [kodi-addon-vfs-sftp](<https://aur.archlinux.org/packages/kodi-addon-vfs-sftp/>)AUR. Super Audio CD ISO files can be access using [kodi-addon-vfs-sacd](<https://aur.archlinux.org/packages/kodi-addon-vfs-sacd/>)AUR. Each of these addons must be enabled within Kodi's addon manager in order to be utilized. 

### Inhibit KDE automatic sleep during playback

Using the add-on [ossscreensavermanager](<https://sourceforge.net/projects/osscreensavermanager/>) in combination with commands using _kwriteconfig6_ it is possible to inhibit KDE's power saving functions during playback. Install the add-on, then under its advanced settings write under "Command to suspend screen saver": 
    
    kwriteconfig6 --file powermanagementprofilesrc --group AC --group SuspendSession --key idleTime 1800000
    
Under "Command to resume screen saver", write: 
    
    kwriteconfig6 --file powermanagementprofilesrc --group AC --group SuspendSession --key idleTime 86400000
    
In this example, the system suspends after 360 minutes during playback, and after 30 minutes without playback. 

## Troubleshooting

### Accessing Kodi logs

In case of an error the first point to start investigation can be `~/.kodi/temp/kodi.log`. 

### Fullscreen mode stretches Kodi across multiple displays

For a multi-monitor setup, Kodi may default to stretching across all screens. One can restrict the fullscreen mode to one display by setting the [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") `SDL_VIDEO_FULLSCREEN_HEAD` to the number of the desired target display. For example, having Kodi show up on display 0, add the following line to the Kodi user's `~/.bashrc` configuration: 
    
    SDL_VIDEO_FULLSCREEN_HEAD=0
    
**注意：** Mouse cursor will be held inside screen with Kodi.

### H.264 playback is using only a single core

**提示：** By default, press `O` during playback to show codec information and CPU usage. More information about this overlay can be found at <https://kodi.wiki/view/Player_process_info>.

If the hardware does not or cannot make use of acceleration, disable it and explicitly set video decoding to software. This is because [H.264 decoding is only multithreaded when video decoding is set to software](<https://forum.kodi.tv/showthread.php?tid=170084&pid=1789661#pid1789661>). 

To achieve this, go to _System Settings > Video_. Set the `settings level` to `Advanced` or `Expert`. Then go to _Acceleration_ and set `Decoding method` to `software`. 

###  Kodi hangs on exit, fully occupying one CPU core, UI unresponsive

This problem can arise with third-party plugins installed, there is some issue with their termination[[1]](<https://www.linuxquestions.org/questions/linux-software-2/kodi-freezes-on-exit-kodi-bin-won't-die-4175588180/>),[[2]](<https://www.reddit.com/r/archlinux/comments/5029oo/kodi_freezes_on_exit_kodibin_wont_die/>). 

Workaround: find proper UI description file (`DialogButtonMenu.xml`) and tweak exit button type from internal Kodi's `Quit()` function call to sending signal from outside system to Kodi. Here is one-liner that makes modifications to any skin from the default Kodi package: 
    
    # find /usr/share/kodi/addons/skin.* -name DialogButtonMenu.xml -exec sed -i 's%<onclick>Quit()</onclick>%<onclick>System.Exec ("killall --signal SIGHUP kodi.bin")</onclick>%' {} \;
    
### kodi-standalone will not play DVDs

If kodi-standalone will not play DVDs, it may help to install [udisks](<../zh-cn/Udisks.html> "Udisks"). 

## See also

  * [Kodi Wiki](<https://kodi.wiki/view/Main_Page>) \- Excellent resource with much information about Arch Linux specifically
  * [Wikipedia:Kodi (software)](<https://en.wikipedia.org/wiki/Kodi_\(software\)> "wikipedia:Kodi \(software\)")
  * <http://www.hdpfans.com/thread-329076-1-1.html> \- Kodi/xbmc Chinese plug-in library installation method
  * <https://github.com/taxigps/xbmc-addons-chinese> \- xbmc-addons-chinese: Addon scripts, plugins, and skins for XBMC Media Center. Special for chinese laguage.
