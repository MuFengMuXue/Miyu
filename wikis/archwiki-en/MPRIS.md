# MPRIS

MPRIS (Media Player Remote Interfacing Specification) is a standard D-Bus interface which aims to provide a common programmatic API for controlling media players.

It provides a mechanism for discovery, querying and basic playback control of compliant media players, as well as a track list interface which is used to add context to the active media item.

## Supported clients
* Audacious
*
*
* Chromium
*
* cmus
*
*
*
*
* Firefox
*
*
* KDE#KDE Connect
* mpv#mpv-mpris
* Music Player Daemon/Tips and tricks#MPRIS support
*
* Plasma Browser Integration
* N Music
*  (enable in Plugins > Shortcuts (MPRIS))
*
*  (enable in Settings > Plugins)
* Quod Libet
*
*
*
* Spotify#MPRIS
*
*
*
*
* Telegram
*
*
* Vermilion
* VLC

## Control utilities
## Playerctl
The  utility provides a command line tool to send commands to MPRIS clients. The most common commands are , ,  and :

 $ playerctl play-pause
 $ playerctl next
 $ playerctl previous
 $ playerctl stop

playerctl will send the command to the first player it finds. To select a player manually, use the  option, e.g. . For better automation playerctl comes with a daemon that keeps track of media player activity and directs commands to the one with most recent activity. You can spawn it into the background with:

 $ playerctld daemon

In order to start playerctld when you log in, you may create the following systemd/User service:

You should then do a daemon-reload before enabling the service with the  flag.

Additionally, playerctld has the ability to change an "active" player, which can be useful when you have multiple simultaneous media streams:

To switch to the next player, use:

 $ playerctld shift

To switch to the previous player, use:

 $ playerctld unshift

## mpris-player-control
The mpris_player_control is a shell script which integrates  and  to control MPRIS clients. It supports the Play, Pause, PlayPause and Stop actions and sink volume control (mute/unmute/up/down) for Spotify.

Run  to show basic script usage.

## D-Bus
An alternative to the above is to manually use D-Bus, which should be available by default as it is a dependency of systemd.

For example, the following commands can be used to control Spotify with the supported Methods:

 $ dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Method

Similarly using :

 $ busctl --user call org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player Method

## Bluetooth
Media control from Bluetooth headsets and similar devices may be forwarded to MPRIS.

Install the  package and run . In order to start up mpris-proxy in the background and/or when your system starts, start/enable  with the  flag.
