# RTorrent

rTorrent is a quick and efficient BitTorrent client that uses, and is in development alongside, the libTorrent (not to be confused with ) library. It is written in C++ and provides a terminal-based user interface via the ncurses programming library. When combined with a terminal multiplexer (e.g. GNU Screen or Tmux) and Secure Shell, it becomes a convenient remote BitTorrent client.

## Installation
Install the  package.

## Configuration
Before running rTorrent, copy the example configuration file  to , and check out the related rTorrent wiki page that has a modern basic configuration file.

## Performance
The values for the following options are dependent on the system's hardware and Internet connection speed.

The  option executes a hash check when rTorrent is started. It checks for errors in your completed files.
 pieces.hash.on_completion.set = yes

## Create and manage files
The  option will determine where your torrent data will be saved (could be a relative path):
 directory.default.set = ~/downloaded

The  option allows rTorrent to save the progress of your torrents. It is recommended to create a directory in home directory (e.g. ).
 session.path.set = ~/.rtorrent.session

The  option has rTorrent watch a particular directory for new torrent files.  Saving a torrent file to this directory will automatically start the download. Remember to create the directory that will be watched (e.g. ). Also, be careful when using this option as rTorrent will move the torrent file to your session folder and rename it to its hash value.
 schedule2 = watch_directory,5,5,load.start=/home/user/watch/*.torrent
 schedule2 = untied_directory,5,5,stop_untied=
 schedule2 = tied_directory,5,5,start_tied=

The following  option is intended to stop rTorrent from downloading data when disk space is low.
 schedule2 = low_diskspace,5,60,((close_low_diskspace,100M))

## Port configuration
The  option sets which port(s) to use for listening. It is recommended to use a port that is higher than 49152 (see: List of port numbers). Although, rTorrent allows a range of ports, a single port is recommended.
 network.port_range.set = 49164-49164

Additionally, make sure port forwarding is enabled for the proper port(s) (see: Port Forward guides).

## Additional settings
The  option enables or disables encryption. It is very important to enable this option, not only for yourself, but also for your peers in the torrent swarm. Some users need to obscure their bandwidth usage from their ISP. And it does not hurt to enable it even if you do not need the added security.
 protocol.encryption.set = allow_incoming,try_outgoing,enable_retry
It is also possible to force all connections to use encryption. However, be aware that this stricter rule will reduce your client's availability:
 protocol.encryption.set = require,require_RC4,allow_incoming,try_outgoing

See also Wikipedia:BitTorrent Protocol Encryption.

This final  option enables DHT support. DHT is common among public trackers and will allow the client to acquire more peers.

## Key bindings
rTorrent relies exclusively on keyboard shortcuts for user input. A quick reference is available in the table below. A complete guide is available on the rTorrent wiki (see: rTorrent User Guide).

{| class="wikitable"
|-
!width="75" |Cmd
!Action
|-
|Ctrl-q
|Quit application
|-
|Ctrl-s
|Start download. Runs hash first unless already done.
|-
|Ctrl-d
|Stop an active download or remove a stopped download
|-
|Ctrl-k
|Stop and close the files of an active download.
|-
|Ctrl-r
|Initiate hash check of torrent. Starts downloading if file is not available.
|-
|Ctrl-o
|Specify the download directory for a added, but not started torrent.
|-
|Left
|Returns to the previous screen
|-
|Right
|Goes to the next screen
|-
|Backspace
|Adds and starts the specified *.torrent
|-
|Return
|Adds and does not start the specified *.torrent
|-
|a|s|d
|Increase global upload throttle about 1|5|50 KB/s
|-
|A|S|D
|Increase global download throttle about 1|5|50 KB/s
|-
|z|x|c
|Decrease global upload throttle about 1|5|50 KB/s
|-
|Z|X|C
|Decrease global download throttle about 1|5|50 KB/s
|}

## Redundant mapping
 is often used for terminal control to stop screen output while  is used to start it. These mappings may interfere with rTorrent. Check to see if these terminal options are bound to a mapping:

To remove the mappings, change the terminal characteristics to undefine the aforementioned special characters (i.e.  and ):
 # stty stop undef
 # stty start undef

To remove these mappings automatically at startup you may add the two preceding commands to your  file.

## Additional tips
## systemd service for a headless server
This unit file relies on running a single user named rtorrent and configuring rtorrent to run as a daemon.

Create the following file:

## systemd service as a daemon for a user
This unit will allow multiple users, or a single user to run rtorrent as a daemon.

To start rtorrent at boot time, enable  (where  is the user who will run rtorrent).

Create the following file:

## systemd services using tmux or screen
Usage of the following services depends on type of service unit.

For system services (in /etc/systemd/system/):

To start at boot time:
 # systemctl enable rtorrent
Start manually:
 # systemctl start rtorrent
Stop:
 # systemctl stop rtorrent

Make sure 'rtorrent' user is created with the appropriate home directory with your rtorrent.rc placed in.

For user services (in /etc/systemd/user/):
 $ systemctl --user enable rtorrent
Start manually:
 $ systemctl --user start rtorrent
Stop:
 $ systemctl --user stop rtorrent

## With screen
*As system service unit

*As user service unit

Attach to rtorrent's session:
 screen -D -r rtorrent

Detach:
 Ctrl-a d

## with tmux
*With independent tmux server (restart rtorrent if crashed)

*With tmux running as user rtorrent (restart rtorrent if crashed)

Attach to rtorrent's session:
 tmux -L rt attach -t rt
 tmux attach -t rt

Detach:
 Ctrl-b d

## systemd service file with dtach
When running dtach from systemd unit, the  environment variable has to be set explicitly for rtorrent to work.

This service file has no restart because the author occasionally takes the drive in question offline, and rtorrent fails, shall we say, "suboptimally" when started in this scenario and loses many torrent specific settings such as the specific directories each torrent is stored in.  In fact the symlinks that kick off rtorrent live on the relevant drive; if it is unmounted rtorrent cannot start.  This use case of blocking rtorrent from starting is relevant to users who put the downloaded files on removable media such as NAS, USB or eSATA drives.

Note some other issues exposed in this service file other than just dtach:

 is a symlink to

This lets us run several instances and kill each one independently with a different version of the ExecStop, to wit:

These are each in a different service file, each of which controls one instance.

Without this step, when running multiple instances a killall solution would kill all the running rtorrent instances.

If multiple rtorrent instances are not needed and the rtorrent rc file is in the default location the above service file may be simplified.  The entire file is included but only the ExecStart and
ExecStop lines change.

Note the hyphen in `ExecStart=-/usr/bin/dtach` part, which allows failure exit code also to denote successfull termination. This is likely because of a current issueAn alternative is to use `SuccessExitStatus=1` in the service section.

The service can be controlled as a user unit. When it is started, you can attach to the session:

 $ dtach -a  /home/sam/run/dtach_fifos/fifo -e "^T"

## Pre-allocation
rTorrent has the ability to pre-allocate  space for a torrent. The major benefit is that it limits and avoids fragmentation of the filesystem. However, this introduces a delay during the pre-allocation if the filesystem does not support the fallocate syscall natively.

Therefore this switch is recommended for xfs, ext4, btrfs and ocfs2 filesystems, which have native fallocate syscall support. They will see no delay during preallocation and no fragmented filesystem. Pre-allocation on others filesystems will cause a delay but will not fragment the files.

To enable it, add the following to your :

To make pre-allocation available on filesystems other than the above - albeit at a delay - you can recompile libTorrent from the ABS tree with the following new switch:
  $ ./configure --prefix=/usr --disable-debug --with-posix-fallocate

See [https://github.com/rakshasa/rtorrent/wiki/Performance-Tuning#disk-allocation the upstream documentation for further information

## Manage completed files
## With watch folders
It is possible to have rtorrent organize completed torrent data to specific folders based on which 'watch' folder you drop the *.torrent into while continuing to seed.

As a solution, use the following example in your .
Make sure to change the paths.

You can add additional watch directories and corresponding completion directories like so:

You can also specify incomplete directories per watch directory:

Also see completion moving via a bash script, and via pyrocore's rtcontrol (there is an AUR package).

## Without watch folders
If you prefer rtorrent to manage completed folder locations automatically, per label, add the below to your rtorrent.rc configuration and amend the paths to suit your environment:

{{bc|1=
# Check if destination dir is not Null
method.set_key = event.download.inserted_new,check_dest_dir, \
"branch=d.custom=storagedir,,\
 \"d.custom.set=storagedir,/path/to/download/directory\""

# Modify destination dir according to tv label
method.set_key = event.download.inserted_new,update_dest_dir_tv, \
"branch=\"equal={d.custom1=, cat=TV}\",\
 \"d.custom.set=storagedir,/path/to/tv/dir\""

# Modify destination dir according to movies label
method.set_key = event.download.inserted_new,update_dest_dir_movies, \
"branch=\"equal={d.custom1=, cat=Movies}\",\
  \"d.custom.set=storagedir,/path/to/movie/dir\""

# Move files of completed torrents
method.set_key = event.download.finished,move_completed, \
"d.directory.set=$d.custom=storagedir; \
     execute2={mv,-u,$d.base_path=,$d.custom=storagedir}"}}

An example use-case for this is if you are using ZFS and need to have the source material on the same filesystem. rTorrent will download to a temporary NVMe/SSD and then move the content to a ZFS filesystem where the *arrs can then process the media and hardlink to a separate folder that your media server will scrape.

## Notification with Google mail
Cell phone providers allow you to "email" your phone:

*Install mailx which is provided by the  package.

*Clear the  file and enter:

Now to send the text, we must pipe a message to the mailx program.
*Make a Bash script:

Where the $@ is a variable holding all the arguments passed to our script.

*And finally, add the important  line:
 method.set_key = event.download.finished,notify_me,"execute2=/path/to/mail.sh,$d.name="

Breaking it down:

 is the command id, which may be used by other commands, it can be just about anything you like, so long as it is unique.

 is the rtorrent command, in this case to execute a shell command.

 is the name of our script (or whatever command you want to execute) followed by a comma separated list of all the switches/arguments to be passed.

 'd' is an alias to whatever download triggered the command, get_name is a function which returns the name of our download, and the '$' tells rTorrent to replace the command with its output before it calls execute.

The end result? When that torrent, 'All Live Nudibranches', that we started before leaving for work finishes, we will be texted:
 All Live Nudibranches: Done

## UI tricks
rTorrent does not list the active tab properly by default, add this line to your  to show only active torrents
 schedule2 = filter_active,30,30,"view.filter = active,\"or={d.up.rate=,d.down.rate=}\""

Then press  in your rTorrent client to see the changes in action.

To sort the seeding view by the upload rate and only show torrents with peers:

 # Sort the seeding view by the upload rate and only show torrents with peers
 view.sort_current = seeding,greater=d.up.rate=
 view.filter = seeding,"and=d.complete=,d.peers_connected="
 view.sort_new = seeding,less=d.up.rate=
 view.sort = seeding

To sort the complete view by the upload rate:

 # Sort the complete view by the upload rate
 view.sort_current = complete,greater=d.up.rate=
 view.filter = seeding,"and=d.complete="
 view.sort_new = seeding,less=d.up.rate=
 view.sort = seeding

## Manually adding trackers to torrents
# Select torrent to edit from rTorrent console view.
# Hit .
# If you had four trackers type following lines one at a time (always press  first) to add four more for example:

 d.tracker.insert="5","udp://tracker.publicbt.com:80"
 d.tracker.insert="6","udp://tracker.openbittorrent.com:80"
 d.tracker.insert="7","udp://tracker.istole.it:80"
 d.tracker.insert="8","udp://tracker.ccc.de:80"

## Schedule torrent to start at a specific time
If you do not want to download a torrent immediately, and would prefer it to begin at a later time (to accomodate a data plan, for example), you can add the torrent to a specific directory and tell rtorrent to check that directory periodically, if a torrent file is present, rtorrent will start downloading at the appointed time:

 # Start torrents at 1am in this directory
 schedule2 = watch_start,01:00:00,24:00:00, "load.start=/home/user/torrents/offpeak/*.torrent"

rtorrent will check the directory  every 24 hours, and if a torrent file is present will start it at 01:00 am.

## Troubleshooting
## CA certificates
By default rTorrent will work with trackers that use HTTPS with valid certificates. If an HTTPS tracker is being rejected because it has a custom or unusual certificate you may need to download it and validate it separately.

Once you have done that you can inform rTorrent of the new certificate via

 $ rtorrent -o http_capath=/etc/ssl/certs/www.your-tracker.com.pem

For more information see:
* rTorrent + SSL guide Full instructions for downloading and validating a new HTTPS certificate.
* rTorrent Error & CA Certificate
* rTorrent Certificates Problem
* rtorrent setup

In rTorrent 0.8.9 and up you can disable HTTPS checking completely by setting  and , source.

## Locked directories
rTorrent can sometimes lock up after a crash or incorrect shutdown, and will complain about a lock file.

Per the error message, the file called "rtorrent.lock" can be found within the hidden folder  for your download directory and manually removed.

## Event failed: bad return code
This is most often caused by there being spaces in your system.method.* lines, or by event handlers that call out to external scripts which are either simply not installed, or return a non-zero exit code.

For the first, remove any spurious spaces, or else quote path etc. where they are intentional, and it will work.

## Web interface
There are numerous web-based front ends for rTorrent; the most active include the following:
* ruTorrent - Has an interface very similar to μTorrent and supports many plugins and advanced features (see also: RTorrent/RuTorrent and guide on forum).
* Flood - Modern interface, written in Node.js using XMLRPC.

## XMLRPC interface
In order to use rTorrent with web interfaces, you can configure rTorrent to create a Unix socket and then allow the web server user access to the socket, typically . This can be applied on start-up by adding the following to the .rtorrent.rc configuration file:
 network.scgi.open_local = /home/user/rpc.socket
 schedule = socket_facl,5,0,"execute=setfacl,-m,u:http:rwx\\,g:http:rwx,/home/user/rpc.socket"

Ensure user is changed to the user running rTorrent. The  command will run 5 seconds after rTorrent has finished initialising to allow the socket to be created.

For more information see: Using XMLRPC with rTorrent.

## Saving magnet links as torrent files in watch folder
If you wish to have magnet links automatically added to your watch folder, here is a script that will do the trick:

 #!/bin/bash
 watch_folder=~/.rtorrent/watch
 cd $watch_folder
 "$1" =~ xt=urn:btih:([^&/+) ]] || exit;
 echo "d10:magnet-uri${#1}:${1}e" > "meta-${BASH_REMATCH(adapted from https://blog.gonzih.me/blog/2012/02/17/how-to-use-magnet-links-with-rtorrent/).

Save it, for instance as rtorrent-magnet, give it execution permission, and place it somewhere under your $PATH. Then in Firefox:
# Type  into the Location Bar (address bar) and press .
# Right-click: New > Boolean > Name: network.protocol-handler.expose.magnet > Value > false.
# Next time you click a magnet link you will be asked which application to open it with. Select the script we just created and you will be done.

If you want xdg-open to handle this, which you need if you are using chrome instead of Firefox, (though gnome and other DE might have their own programs overriding xdg-open) you need to create the desktop entry for the rtorrent-magnet script in  with the following content:

 [Desktop Entry
 Type=Application
 Name=rtorrent-magnet
 Exec=rtorrent-magnet %U
 MimeType=x-scheme-handler/magnet;
 NoDisplay=true

Then all you need to do is to register the mimetype using
 $ xdg-mime default rtorrent-magnet.desktop x-scheme-handler/magnet

## Magnet to torrent
You could also use the  package which downloads the metadata and creates a torrent file.

How to use:
 $ magnet2torrent -m  -o file

Or use  and , to process magnet links from clipboard:

 $ d=$(xdg-user-dir DOWNLOAD)
 $ c=$(xclip -o -selection clipboard | grep ^magnet)
 $ aria2c -d "$d" --input-file <( echo "$c" ) --bt-metadata-only=true --bt-save-metadata=true

## rtorrent-ps
rTorrent-PS is an rTorrent distribution in form of a patchset with UI enhancements, colorization, and some added features.

## Installation
Install .

## Configuration
Set "pyro.extended" to 1 in your rTorrent configuration file to activate rTorrent-PS features.

See rtorrent-ps templates of the pimp-my-box repository for additional configuration examples. Be aware they may require PyroScope command line utilities to work.

## PyroScope command line utilities
PyroScope command line utilities are a collection of tools for the rTorrent client that work well together with the #rtorrent-ps patchset.
Amongst other things, they provide automation for common tasks and a queue manager for rTorrent.

Follow the official documentation for installation and configuration. See rtorrent-ps templates of the pimp-my-box repository for additional configuration examples.
