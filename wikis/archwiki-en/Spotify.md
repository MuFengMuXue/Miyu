# Spotify

Spotify is a digital music streaming service with a freemium business model. This article is mainly about the semi-official, proprietary Spotify for Linux client, which is developed by Spotify's engineers in their spare time and not actively supported by Spotify.Alternatively, there is an [https://open.spotify.com/ online player and a number of open source third-party clients.

## Installation
Install . This package manages a per-user installation in your home directory, allowing Spotify to update itself independently of pacman (similar to how Spotify self-updates on other operating systems).

If you prefer to manage Spotify updates with pacman, instead use  which repackages Spotify for Linux. If you need to add and play local files you need to additionally install  and .

## Third-party clients
*
*
*
*
*
*
*
*
*
*
*
*
*

## Tips and tricks
## Limit storage size
Spotify automatically manages a storage size for caching, however one may want to force the size limit preventing the filesystem from filling up.

Append  (measured in MB) to , e.g. a storage size of 3072 MB:

## Global media hotkeys
For environments in which controlling Spotify via the keyboard does not work automatically, the official Linux client has support for media keys like . We can use for example xbindkeys to catch the global media keypresses, and then forward them to Spotify using one of the methods below. If you use xbindkeys, ensure that Spotify is restarted after installation and key configuration otherwise the key events will not be properly caught.

## MPRIS
The Spotify client implements the MPRIS D-Bus interface which allows external control.

## Disable track notifications
After version 0.9.10, track change notifications were enabled by default. They can be quite intrusive. To disable them, launch Spotify with the  option or add:

Alternatively, you can disable track notifications via the client's settings: disable Show desktop notifications when the song changes.

## Show track notifications
 provides a library you can use with  and a notification daemon such as  to show the artist and title in a notification when the track changes.

 #!/usr/bin/env python3

 import gi
 gi.require_version('Playerctl', '2.0')
 from gi.repository import Playerctl, GLib
 from subprocess import Popen

 player = Playerctl.Player()

 def on_track_change(player, e):
     track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
     Popen(track_info)

 player.connect('metadata', on_track_change)

 GLib.MainLoop().run()

## Skip overplayed radio tracks
Another use of the  library is to skip tracks that are played too much on radio when you do not necessarily want to downvote these tracks because you may want to hear them again later on that station.

 #!/usr/bin/env python3

 from gi.repository import Playerctl, GLib

 player = Playerctl.Player()

 played_out = Fuss', 'Walk And Talk', 'Neuland'

 def on_track_change(player, e):
     if player.get_title() in played_out:
         player.next()

 player.on('metadata', on_track_change)

 GLib.MainLoop().run()

## Mute commercials
## spotblock
 is a resource-efficient ad blocker that runs as a systemd daemon.

## Spotify-AdKiller
 is another alternative to block Spotify ads.

## spotblock-rs
 is a fast and light program to mute Spotify ads. It also works with PipeWire.

## Hosts file
You may also add the following lines to your hosts file to block ads in Spotify:

## Remote Control
## Send commands via SSH
If you set up ssh on the server, you can send controls from a client to a remote Spotify instance with

 $ ssh user@host yourcommand

where yourcommand can be spotifycmd that you installed on the server, or a dbus script for the linux version, as described above.

## Grab the Spotify window via SSH
Aside from grabbing the whole desktop with TeamViewer or VNC to remotely control your server, you can also only grab the Spotify Window from the server to your client.

To do that, you need to configure sshd on your server and install x11vnc on both server and client as well as tigervnc on the client. Then you can use these scripts to grab either the complete dektop or only the Spotify window, which essentially gets you GUI client-like behavior as with MPD.

{{bc|
#!/bin/bash
# vncget.sh

if  $1 == all ;then
  ssh -f -t -L 5900:localhost:5900 user@host "x11vnc -q -display :0 -auth .Xauthority"
else
  ssh -f -t -L 5900:localhost:5900 user@host ".bin/vncgetspotify.sh"
fi

for i in {1..4}; do
  sleep 2
  if vncviewer localhost:0; then break; fi
done
}}

{{bc|
#!/bin/bash
# vncgetspotify.sh

export DISPLAY=:0

id=$(wmctrl -lx | awk '/spotify.exe.Wine/ {print $1}')
 -z $id  && id=$(wmctrl -lx | awk '/spotify.Spotify/ {print $1}')

x11vnc -sid $id -display :0 -auth .Xauthority
}}

You will need to copy the second script to ~/.bin/vncgetspotify.sh on the server and the first script to any place on your client.

Finally, to grab the spotify window, run on the client:

 $ sh vncget.sh

or, for the whole desktop:

 $ sh vncget.sh all

## HiDPI Mode
As the current Spotify build is not HiDPI aware, the amount to scale the interface by can be specified using the terminal command:
 $ spotify --force-device-scale-factor=X

where X is the amount to scale the interface by, e.g 2.

This change can be added to the  file in order to apply the scaling when launching from the desktop.

To make sure the file does not get overwritten when the package is updated, copy it to you local applications folder:
 $ cp /usr/share/applications/spotify.desktop ~/.local/share/applications/

Now edit  and add the  option:

You might need to relaunch your Desktop Manager, before these override changes will be effective.

## Running under Wayland
Running Spotify under Xwayland can cause some quirks such as blurry app, especially with mixed screen sizes and orientations and scaling. As of Spotify version 1.2.86.502.g8cd7fb22 wayland mode is detected automatically and no longer requires the :  flags. But due to some bug one has to unset the DISPLAY variable for it to work. To enable input method in Wayland, pass .

These change can be added to the  file in order to start in Wayland mode when launching from the desktop.

See the previous section #HiDPI Mode for details.

## Disable GPU
To prevent Spotify from using your GPU for hardware video acceleration and to reduce VRAM usage, launch Spotify with the  flag.

## Troubleshooting
## Desktop Environment alerts (beeps) mutes Spotify
Comment out "module-role-cork" in the PulseAudio configuration file so it does not get loaded anymore.

Or unload it temporarily with:

 $ pactl unload-module module-role-cork

## Blinking images and improper rendering while using Spotify Linux with DWM
Start spotify as a floating window.

You can add this rule to the rules array in your :
 { "Spotify",     NULL,       NULL,        2,         True,     -1 },

This will tell dwm to start spotify as a floating window associated with the tag "2" no matter what window mode you are in. Recompile and install dwm to apply your new settings.

## Broken search, browsing or radio
:Spotify bug report concerning non-english locales
If various tabs like browsing only show a blank screen, the search field does not seem to do anything or the radio page is broken (stuck when starting and unsresponsive to input) you might be using a custom locale.

Try setting the environment variable  to  before starting Spotify.

## Deadlock GUI Thread
Can occur under tiling window managers, such as Awesome, when double-clicking new song or playlist. Edit the file  to add or change the following:

 ui.track_notifications_enabled=false

Restart Spotify. This will try to disable song notifications which seem to be the cause of the issue (the lack of a notification daemon to receive them makes the UI thread hang). Note that several causes appear to exist for this problem, and this particular fix only applies to select versions of Spotify client, i3 and Awesome, and it may be that additional root causes exist for the Debian and Ubuntu users reporting this issue. Observed with Spotify 0.9.17.1.g9b85d436 and Awesome 3.4.15 and i3-gaps 4.13-2 and Spotify 1.0.64.407.g9bd02c2d.

Note: This issue has multiple causes, so keep track of what you change while researching this. Update this section with additional scenarios and fixes.

## Album art and images are missing, show up as squares
Quit Spotify, then open Spotify preferences

Change @https to @http:

 network.proxy.addr="your-proxy.com:80@http"
 network.proxy.mode=2

See original forum post here.

## Spotify does not detect other devices on local network
If a firewall is in place, open ports 57621 for UDP and TCP. If you use a variant of the iptables Simple stateful firewall, the following should do it:

 iptables -A TCP -p tcp --dport 57621 -j ACCEPT -m comment --comment spotify
 iptables -A UDP -p udp --dport 57621 -j ACCEPT -m comment --comment spotify

It is also possible to restrict the source and destination to the local network.

If you are using Spotify Connect to play music on a wireless speaker or AVR, your firewall needs to be configured for Spotify's mDNS lookup of those. Sadly, it uses a random unprivileged port which makes these firewall rules rather nasty. Fortunately, you can restrict the rules to source port 1900 or 5353.

 iptables -A UDP -p udp --sport 1900 --dport 1025:65535 -j ACCEPT -m comment --comment spotify
 iptables -A UDP -p udp --sport 5353 --dport 1025:65535 -j ACCEPT -m comment --comment spotify

If using MusicCast for streaming, you will also need to ensure that IGMP multicast packets are allowed to 224.0.0.22 (with IP options allowed) from the MusicCast speaker/AVR by all firewalls in place (including router firewall).

If you cannot detect other linux clients, this may be due to a bug in Spotify related to the user name launching the instance. Spotify will not detect other instances having the same  environment variable, even on different machines. To circumvent this, either create a dedicated user, or launch Spotify with a different . The following is a workaround to use your home directory and still be able to detect other devices:

 $ ln -s $HOME ~/.spotify_fakehome_$HOSTNAME
 $ HOME=$HOME/.spotify_fakehome_$HOSTNAME spotify &

## Search Bar text is invisible when using a dark theme
The text in the search bar appears to be hardcoded to be white, making it invisible when using a dark Qt theme. To fix this, you will need to make an override.

First create a css file somewhere your account has permission to read/write from (such as your home folder). Call it whatever you like (eg. spotify-override.css).

Open the newly created css file and add the following:

 QLineEdit { color: #000 }

Save the file and exit. Next, you need to add the following to the end of your Spotify launcher (substitute the path with the actual path of your css file):

 -stylesheet=/home/user/spotify-override.css

So your full launch path should look something like this:

 /usr/share/spotify/spotify-client/spotify -stylesheet=/home/user/spotify-override.css

## Not respecting window manager rules
Window manager that try to apply specific rules like starting it on a determined workspace or maximizing it on startup, has no effect, as Spotify does not set the WM_CLASS property before creating the window, violating the ICCCM specifications. One solution is to use .

## GUI hangs while the music plays
Also the previous and next track buttons act with a delay of 10-40 seconds. Spotify by default tries to send notification about next track, if you do not have a notification-daemon installed, Spotify's GUI hangs.

The solution is to either disable notifications in the settings or to install a notification daemon from Desktop notifications.

## Spotify occupies the whole screen over system panel and its borders are gone
If you have issue with window borders disappearing and the GUI going full-screen but you cannot drag the window or change its size, edit the preferences located by default in:

Close Spotify, remove both lines shown above, save and run Spotify again.

## Cannot open settings in Wayland
When using Wayland, clicking on the 'Settings' button does nothing. Using the keyboard instead will work (arrows and enter). See [https://community.spotify.com/t5/Desktop-Linux/Settings-don-t-open-on-Linux/td-p/1478736

## Crashes on startup
If you get a crash on startup with the following error message

 GPU process isn't usable. Goodbye

Try to run  with the  flag.

## Spotify has limited or no internet connectivity while using a VPN
More recent versions of Spotify (noticed after version ~1.1.10) use NetworkManager's detection of internet connectivity for determining if Spotify is able to play songs or even log in. When using a VPN service, Network Manager can fail to correctly identify internet connectivity, stating "Limited Connectivity". See NetworkManager#Checking connectivity for possible solutions.

## Slow or laggy client
If Spotify is being unusually slow, common culprits usually are corrupted cache files. Run the following command, after closing your Spotify client:

 $ rm -rf ~/.cache/spotify/Browser/* ~/.cache/spotify/Data/* ~/.cache/spotify/Storage/*

* Make sure you only delete the files inside the folders, and not the folders themselves.
* If that does not resolve the issue, try deleting  and reinstalling.

## /usr/lib/libcurl-gnutls.so.4 error
If you encounter the error:

 spotify: /usr/lib/libcurl-gnutls.so.4: no version information available (required by spotify)

Delete .
