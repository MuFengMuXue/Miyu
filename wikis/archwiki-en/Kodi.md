# Kodi

Kodi (formerly known as XBMC) is an award-winning free and open source (GPL) software media player and entertainment hub that can be installed on Linux, OSX, Windows, iOS and Android, featuring a 10-foot user interface for use with televisions and remote controls. These can all be played directly from a CD/DVD, or from the hard-drive. Kodi can also play multimedia from a computer over a local network (LAN), or play media streams directly from the Internet. It can also be used to play and record live TV using a tuner, a backend server and a PVR plugin; more information about this can be found on the Kodi wiki.

## Installation
Install the  package. Users wanting HDR support should instead install the  package. Be sure to review/install optional dependencies listed by pacman to enable additional functionality.

## Setup
Both packages support several composers, with varying levels of functionality:

; GBM: currently the most feature rich. It is the only one of the three options able to display HDR content, may be a good choice for standalone operations since it runs directly on the GPU without the need for the added X11 layer. A complete list of features lacking compared to other back-ends can be found in Kodi issue 14876.
; Xorg: should be considered on-par with GBM.
; Wayland: a known limitation is having the resolution and frame rate set in the compositor rather than in Kodi's GUI; also currently does not support VT switching.

All of the official addons in the  group are disabled by default and need to be enabled in Kodi's addon menu after installation.

## Hardware video acceleration
Enable and configure hardware video acceleration to speed up playback performance. Once installed, the hardware backend(s) are presented under Settings > Player > Videos.

## Running
There are two general use cases:

#  is meant to be run by any user on an on-demand basis. Use it like any other program on the system.
#  is meant to be run as the only graphical application, for example on a HTPC. See #Running standalone for more information.

## Running standalone
Using standalone mode is advantageous for several reasons:

# One can define an unprivileged user to run kodi and have no access to a shell.
# When paired with a systemd unit (or equivalent, see below), this setup makes the box on which Kodi is running more like an appliance.

## kodi-standalone service
 provides three services and automatically creates and provisions the unprivileged user to run Kodi in standalone mode.
*
*
*

## Recommended methods to reboot/shutdown using kodi-standalone service
In principal this is no different than data loss occurring from a user doing work when a sysadmin issues a reboot command without prior warning. While it is possible to run Kodi in systemd's user.slice instead, doing so makes it difficult to use USB mounts within Kodi and to use PulseAudio for Kodi sessions.

* Kodi GUI: Selecting the corresponding option under power menu in the Kodi GUI.
* Mobile device: The official Android/iOS apps can also perform these actions (assuming the corresponding options are enabled in Kodi).
* CLI: Use  provided by  to send the  or the  command. The syntax is:
 $ kodi-send -a "Reboot"
 $ kodi-send -a "ShutDown()"

## Xsession with LightDM
To use LightDM with automatic login, see LightDM#Enabling autologin and LightDM#Enabling interactive passwordless login. Kodi includes  as xsession.

## Xsession with NoDM
Nodm is an automatic display manager which automatically starts an X session at system boot.

By creating a user for kodi (e.g. ) and installing  we simply have to specify the kodi user inside:

Make sure to execute  inside the xinitrc file.

## Socket activation
Socket activation can be used to start Kodi when the user issues a Wakeup command from a remote control app like Kore, or makes a connection to Kodi's html control port. Start listening by starting  (replace user with the user running Kodi to be started as).

There are no packaged  and  files, one must create them manually. Depending on the setup, one can optionally change the ports in .

## Start from remote control with LIRC / irexec
Kodi can be configured to start via a key press. Users will need  and . This can be useful on setups running 24/7 and having kodi up on demand.

See the corresponding LIRC article and create a functional setup with a remote. Also, the package  has to be installed.

Generate the file  with the following content:

Adopt  to whatever button on the remote is to start Kodi. One can use irw (see LIRC#Testing) to find out the correct values for  and .

Create a drop-in for :

Start  and enable it to run at boot time.

## Using a remote control
As Kodi is geared toward being a remote-controlled media center via an official app, physical remote control, or USB/bluetooth keyboard/mouse.

## Using the Android or iOS app
Both Android and iOS users can use the official app (currently free of charge) to control kodi once it is correctly setup to do so. Steps to configure both Kodi and the app are detailed on the Official Kodi Remote and Kore Manual page.

## Using a physical remote control
Any PC with a supported IR receiver/remote, can use LIRC or even kernel supported modules to drive it. Configuring specific remotes with lirc is covered on the LIRC article.

To work properly with Kodi, a file that maps the lirc events to Kodi keypresses is needed. Create an XML file at  (note the capital 'L').

 format is as follows:

* Device Name is whatever LIRC calls the remote. This is set using the Name directive in lircd.conf and can be viewed by running  and pressing a few buttons on the remote. IRW will report the name of the button pressed and the name of the remote will appear on the end of the line.
* XBMC_button is the name of the button as defined in keymap.xml.
* LIRC_button is the name as defined in . If  was autogenerated using , these are the names selected for the buttons. Refer back to LIRC for more information.
* A very thorough LIRC page hosted on the Kodi Wiki should be consulted for more help and information on this subject as this is out of scope of this article.

## HDMI-CEC
With a supported USB-CEC adapter, Kodi can be used to automatically turn on and off the TV and other home theater equipment. Volume control from Kodi can be sent to a supported amplifier, one can manage DVD or Blu-Ray players from inside Kodi, and redirect the active source on the TV to whichever equipment needs it, all from one remote control. For more information see the official Kodi wiki page on CEC and libCEC FAQ.

Install .

When connected, the USB-CEC's  entry (usually ) will default to being owned by the  group, so in order to use the device the user running Kodi needs to belong to that group. See Users and groups#Group management for instructions on how to add users to groups.

* Add all users that will use Kodi to the  user group.

## Using a gamepad
Install .

First, confirm that the gamepad is detected by the OS, navigate to Kodi Settings > Input > Peripherals and confirm your device is listed. Then, enter the Configure attached controllers submenu. Kodi will prompt to press buttons on the controller one at a time. Once the mapping is finished, the gamepad should be able to control the UI.

## Sharing media and a centralized database across multiple nodes
If multiple PCs on the same network are running Kodi, they can be configured to share a single media library (video and music). The advantage of this is media and key metadata are stored in one place, and are shared/updated by all nodes on the network. For example, users of this setup can:

* Stop watching a movie or show in one room then finish watching it in another room automatically.
* Share watched and unwatched status for media on all nodes.
* Simplify the setup with only a single library to maintain.

As well, the media itself can be located in one space thus allowing a lighter footprint of client systems (ie no need for large HDD space).

Several things are needed for this to work:

* Network exposed media (via protocols that Kodi can read, e.g. NFS or Samba).
* A MariaDB server.

These assumptions are used for the guide, substitute as needed:

* The media is located under following mount points:   .
* The network addresses of all nodes are within the 192.168.0.* subnet range.
* The IP address of the machine running both the NFS exports and the MariaDB database is 192.168.0.105.
* Each Kodi box is referred to as a node.
* The Linux user running Kodi is 'kodi' on all nodes.

For additional info, refer to the official Kodi wiki.

## NFS server export example
This section provides an example using exports, see NFS for install and usage. Nexus v20.0 of Kodi contains initial support for NFSv4 exports. A limitation is that users of NFSv4 exports will have to manually add the exports/browsing the NFS network is not currently supported. Users will also need to restart Kodi after the sources have been added. Using a NFSv3 export does not have these caveats.

Users wanting a pure NFSv4 setup should see NFS#Starting the server in order to keep things clean. Of course, this only applies to the box running the NFSv4 exports.

Create an empty directory in NFS root for each media directory to be shared. E.g.:

 # mkdir -p /srv/nfs/{shows,movies,music}

Bind mount the media directories to the empty directories in .

The following example is for a NFSv3 exports:

The following example is for a NFSv4 exports:

## Install and set up the MariaDB server
See MariaDB for installation and configuration instructions.

To create a database for Kodi, use the following commands:

 $ mysql -u root -p
    >
 MariaDB CREATE USER 'kodi' IDENTIFIED BY 'kodi';
 MariaDB [(none)> GRANT ALL ON *.* TO 'kodi';
 MariaDB flush privileges;
 MariaDB [(none)> \q

## Set up Kodi to use the MariaDB library and the NFS exports
## Set up Kodi to use the common SQL database
To tell Kodi to use the common database, insure that Kodi is not running, then create the following file:

## Set up network shares
For NFSv3 shares, load Kodi and define the network shares that correspond to the exports by browsing to the following within the interface Video > Files > Add Videos > Browse > Network Filesystem(NFS).

After a few seconds, the IP address corresponding to the NFS server should appear.

Select  from the list of share and then OK from the menu on the right. Assign this share the category of TV Shows to setup the appropriate scraper and to populate the SQL database with the correct metadata.

Repeat this browsing process for the "movies" and "music" and then exit Kodi once properly configured. At this point, the SQL tables should have been created.

For NFSv4 shares, user cannot browse the network but will have to manually define them under Video > Files > Add Videos > Browse > Add network location...  For there, change the Protocol to "Network File System (NFS)" and then define the server address (numerical IP or hostname) and then define the share under the Remote path section. Repeat for each export.

## Cloning the configuration to other nodes on the network
To set up another Kodi node on the network to use this library, simply copy  to that box and restart Kodi. There is NO need to copy any other files or to do any other setup steps on the new kodi node. The nfs exports, the metadata for the programming, any stop/start times, view status, etc. are all stored in the SQL tables.

## Tips and tricks
## Keep a log of what is watched
Keep track of every video watched on kodi with .

## Speedup video playback (synchronized audio and video) up to 1.5x
To enable speed-up and slow-down with audio/video sync (0.8x - 1.5x) do the following:
* Create the following file that will map the  and  keys to the  and  actions, respectively:

* Restart kodi which will read in these changes.
* Navigate to System > Player > Videos > Playback and enable "Sync playback to display" option.

## Modify default values for watch and resume points
Some users may wish to make the thresholds Kodi uses to create a resume point/consider a video "watched" entirely. Do so by editing  inserting the following three xml fields:

; ignoresecondsatstart:  the number of seconds to wait before keeping track of the start point. If users watch a value below the one defined, no start point is recorded. Default is 180.
; playcountminimumpercent:  the percentage of total play time to consider something watched. If users watch more of the video that this number but not the entire video, it is considered watched and any previously recorded resume point is deleted upon stopping and finally, the video is flagged as watched. Default is 90.
; ignorepercentatend: the percentage of total play time at the end of a video to ignore making a resume point. This is related to the previous setting except it considers the last x percent of the video. If users watch enough content to enter this space of the file, no resume point is saved and the video is flagged as watched. Default is 8.

## CLI for kodi
*  package provides  which can send valid kodi action or kodi function to kodi from the shell.

*  can handle many aspects of library management, from clean-up of unused images, to searching, to querying what is currently playing.

## Use Kodi to view security camera streams (rtsp or rtmp)
Since Kodi uses ffmpeg for video playback, it is able to play streams such as rtsp and rtmp can be viewed. To do so, simply create a txt file in the filesystem exposed to the kodi user containing the stream. For example:

Optionally meta-data, such as cover art and summaries can also be associated to the .strm file just like normal entries in a library by using an NFO file.

## UPnP and DLNA
Go to Settings > Services > UPnP/DLNA and toggle Enable UPnP support.

## Adjusting CD/DVD drive speed
The eject program from the  package does a nice job for this, but its setting is cleared as soon as the media is changed.

This udev-rule reduces the speed permanently:

{{hc|/etc/udev/rules.d/dvd-speed.rules|2=
KERNEL=="sr0", ACTION=="change", ENV{DISK_MEDIA_CHANGE}=="1", RUN+="/usr/bin/eject -x 2 /dev/sr0"
}}

Replace  with the device name of the optical drive. Replace  with  if the preference is 4x-speed instead of 2x-speed.

After creating the file, reload the udev rules with

 # udevadm control --reload

## Use port 80 for webserver
Kodi has a webservice that allows interaction through a web-interface. By default, it uses port  as  requires root privileges. Use the following to permit it to use low port numbers:

 # setcap 'cap_net_bind_service=+ep' /usr/lib/kodi/kodi.bin

Restart Kodi and set port  in the configuration menu (Services > Webserver > Port).

## Set Wireplumber HDMI audio volume from command line
The Kodi interface gives volume control in Settings -> System -> Audio as well as during playback, but there is also a volume level on digital sinks on Wireplumber/Pipewire level. On headless systems you can adjust many audio volume levels in alsamixer, but HDMI or digital sinks often have on/off switches and no levels.

To set the audio volume for your HDMI interface via shell on a standalone mediacenter setup you can follow these steps:

# Give user kodi a valid shell if it is assigned to nologin, which should be the case in a standalone mediacenter setup.
# Start playing video through HDMI to make the right sink appear in .
# Shell into the box and su to user kodi.
# Set the XDG_RUNTIME_DIR env var: {{ic|export XDG_RUNTIME_DIR"/run/user/${UID}"}}
# Check the sinks, their numbers and volume level using .
# Set the volume of the right sink to 100%:
# Reset  back as shell to the  user.

## Using ALSA
If PulseAudio or PipeWire do not work properly, try forcing ALSA by launching Kodi with the  flag.

One method to set the audio backend permanently is to create a custom systemd unit, or, alternatively, edit one from .

## Audio passthrough output device list in Kodi 21+
One can allow an external receiver or sound bar to decode audio by enabling passthrough. This is useful for files encoded in TrueHD or Atmos. If using PulseAudio, follow the instructions at https://kodi.wiki/view/PulseAudio to first enable passthrough in PulseAudio. Once complete, the corresponding passthrough options should appear in Kodi. When forcing ALSA by launching Kodi with ,  the passthrough options will appear in Kodi automatically.

Another way of getting TrueHD and DTS-MA passthrough without disabling PulseAudio or  is to use an external player like MPV, first create the file  then paste the following into it:

       /usr/bin/mpv
       --fs=yes "{1}"
       true

MPV should now be the default media player for Kodi. To set the correct audio output device for MPV, use the following command to show a list of available audio devices:

 $ mpv --audio-device=help

For example:

 alsa/hdmi:CARD=NVidia,DEV=1

Now edit  and add the following lines:

 audio-spdif=ac3,eac3,dts-hd,truehd
 audio-device=alsa/hdmi:CARD=NVidia,DEV=1

To have auto switching of refresh rates create the following folder  then download and place mpv-plugin-xrandr/xrandr.lua into that folder.

## Kodi JSON-RPC API to alter settings from external tools
Users can interact directly with Kodi on the CLI or from a python script etc. by making use of the JSON-RPC API.

For example, using :
 $ curl -v -H "Content-type: application/json" -d \
   '{"jsonrpc":"2.0","id":1,"method":"Settings.GetSettingValue","params":{"setting":"audiooutput.audiodevice"}}' \
   http://localhost:8080/jsonrpc -u xbmc:xbmc

Another example is this python script which simply toggles between two groups of settings, in this case, toggling the audio source back-and-forth between HDMI and optical out.

## Fix for delayed startup on Wi-Fi
If running with Wi-Fi only (wired network unplugged) while #Sharing media and a centralized database across multiple nodes, kodi will likely start before the wireless network is up, which will result in failure to connect to the shares and to the SQL server. Assuming the network is managed by systemd-networkd, this can be fixed by using a drop-in file:

## Run kodi in a window manager
Users running kodi in a window manager may see a black screen at exit. To fix this, try switching to another tty. A possible solution is to run kodi with this script (running as the root user):

To make sure that sudo does not ask for password for  create the following drop-in file using the  command as root:

## USB DAC not working
Users of USB DAC/sound cards may experience distorted sound/clicks/pops or no sound at all when selecting it from Audio settings. A possible fix:

Open  (it should be under  if using the supplied ) and change

 101

to

 100

## Virtual file system support
Kodi provides addons for accessing various virtual file systems from within Kodi. RAR archives can be accessed using . SFTP shares can be accessed using . Super Audio CD ISO files can be access using . Each of these addons must be enabled within Kodi's addon manager in order to be utilized.

## Inhibit KDE automatic sleep during playback
Using the add-on ossscreensavermanager in combination with commands using kwriteconfig6 it is possible to inhibit KDE's power saving functions during playback. Install the add-on, then under its advanced settings write under "Command to suspend screen saver":

 kwriteconfig6 --file powermanagementprofilesrc --group AC --group SuspendSession --key idleTime 1800000

Under "Command to resume screen saver", write:

 kwriteconfig6 --file powermanagementprofilesrc --group AC --group SuspendSession --key idleTime 86400000

In this example, the system suspends after 360 minutes during playback, and after 30 minutes without playback.

## Troubleshooting
## Accessing Kodi logs
In case of an error the first point to start investigation can be .

## Fullscreen mode stretches Kodi across multiple displays
For a multi-monitor setup, Kodi may default to stretching across all screens. One can restrict the fullscreen mode to one display by setting the environment variable  to the number of the desired target display. For example, having Kodi show up on display 0, add the following line to the Kodi user's  configuration:

 SDL_VIDEO_FULLSCREEN_HEAD=0

## H.264 playback is using only a single core
If the hardware does not or cannot make use of acceleration, disable it and explicitly set video decoding to software.
This is because H.264 decoding is only multithreaded when video decoding is set to software.

To achieve this, go to System Settings > Video. Set the  to  or . Then go to Acceleration and set  to .

## Kodi hangs on exit, fully occupying one CPU core, UI unresponsive
This problem can arise with third-party plugins installed, there is some issue with their terminationWorkaround: find proper UI description file () and tweak exit button type from internal Kodi's  function call to sending signal from outside system to Kodi. Here is one-liner that makes modifications to any skin from the default Kodi package:

 # find /usr/share/kodi/addons/skin.* -name DialogButtonMenu.xml -exec sed -i 's%Quit()%System.Exec ("killall --signal SIGHUP kodi.bin")%' {} \;

## kodi-standalone will not play DVDs
If kodi-standalone will not play DVDs, it may help to install udisks.
