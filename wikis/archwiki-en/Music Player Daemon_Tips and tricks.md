# Music Player Daemon/Tips and tricks

Go back to Music Player Daemon.

## Organizing library
MPD does not manage your library. Check out  or .

## Last.fm/Libre.fm scrobbling
To scrobble your songs to Last.fm or Libre.fm when using MPD, there are several possibilities.

## mpdas
mpdas is an AudioScrobbler client for MPD written in C++. It uses  and . mpdas supports the latest AudioScrobbler protocol (2.0) and will also cache unscrobbled plays in  if there is no network connectivity.

The  package is available.

Configuration of mpdas is very simple, see the official README. A very basic example of  is also available as .

To autostart mpdas along with mpd, add an entry for it into the file in which you start mpd (e.g. xinitrc):

When mpd is started as a systemd user service, it is better to start mpdas as a user unit too.

## mpdscribble
 is a daemon that is arguably the best alternative, because it is the semi-official MPD scrobbler and uses the new "idle" feature in MPD for more accurate scrobbling. Also, you do not need root access to configure it, because it does not need any changes to  at all. Visit the official website for more information.

A sample configuration is included: , copy it to  and edit to suit.

Your password can also be in the form of an md5hash:

 echo -n "password" | md5sum | cut -f 1 -d " "

To autostart mpdscribble you can use the  under systemd user instance. See systemd/User for details.

Alternatively you can autostart mpdscribble along with mpd, add an entry for it into the file in which you start mpd (e.g. ):

## Sonata
Sonata has built-in support for scrobbling, although that requires the program to run the whole time. Additionally, Sonata does not cache the songs if they cannot be forwarded to Last.fm at the time of playing, meaning they will not be added to the statistics.

## YAMS
YAMS is a Last.FM scrobbling daemon for MPD written in Python.

As it is written for v2.0 of Last.FM's scrobbling API, YAMS does not store your username or password locally, but opts to use a cookie instead. Similar to other scrobblers, YAMS can save failed scrobbles and upload them at a later date. It also offers a decent amount of configuration options for when/how a scrobble should be made (including ignoring duplicate scrobbles when a track is played multiple times in a row).

The  package is available.

In order to authenticate, the user must run the  command in an interactive terminal, at least once, and follow the printed instructions.

Afterwards, YAMS can be started with its binary:

 runs as a daemon by default ( will run it in the foreground).

 will kill the current running instance.

 will attach to the current running instance's log file, allowing you to watch the daemon's output.

 will print all command line options.

YAMS also comes with a systemd service file that can be started with the  user unit after authentication is complete.

## Disable resume playback on startup
This feature is present in mpd after version 0.16.2. When this feature is enabled, mpd will always start in the "paused" state, even if a song was playing when mpd was stopped. Add the line below to enable this feature.

## Example configuration: Output with 44.1 KHz at e. g. 16 bit depth, multiple programs at once
Why these formats? Because they are the standard format for CD audio, because ALSA on its own allows more than one program "to sound" only with dmix — which uses an inferior resampling algorithm by default — and because dmix by default resamples anything lower to 48 KHz (or whatever higher format is playing at the time). Also, some get clicking sounds if at least  is not changed this way.

What is the downside? These settings cause everything (if necessary) to be resampled to this format, such as material from DVD or TV which usually is at 48 KHz. But there is no known way to have ALSA dynamically change the format, and particularly if you listen to far more CDs than anything else the occasional 48 to 44.1 is not too great a loss.

The following assumes that there are not already other settings which conflict resp. overwrite it. This applies especially to the current user's potential  — which MPD as its own user ignores, therefore the following should go to :

{{hc|/etc/mpd.conf|2=
audio_output {
        type                    "alsa" # Use the ALSA output plugin.
	name			"your_custom_name" # Must be present and does not have to match the actual card name , e.g. what you have in /etc/asound.conf
        options                 "dev=dmixer"
        device                  "plug:dmix" # Both lines cause MPD to output to dmix
	format	        	"44100:16:2" # the actual format
	auto_resample		"no" # This bypasses ALSA's own algorithms, which generally are inferior. See below how to choose a different one.
}
}}

If one wants to leave the bit depth decision to ALSA resp. MPD, comment out resp. omit the dmix.format line and change the one for mpd with format to "44100:*:2".

## Control MPD with lirc
There are already some clients designed for communications between lircd and MPD, however, as far as the practical use, they are not very useful since their functions are limited.

It is recommended to use mpc with irexec. mpc is a command line player which only sends the command to MPD and exits immediately, which is perfect for irexec, the command runner included in lirc. What irexec does is that it runs a specified command once received a remote control button.

First of all, please setup your remotes as referred to the LIRC article.

Edit your favored lirc startup configuration file, default location is .

Fill the file with the following pattern:

 begin
      prog = irexec
      button =
      config =
      repeat =
 end

An example:

 ## irexec
 begin
      prog = irexec
      button = play_pause
      config = mpc toggle
      repeat = 0
 end

 begin
      prog = irexec
      button = stop
      config = mpc stop
      repeat = 0
 end
 begin
      prog = irexec
      button = previous
      config = mpc prev
      repeat = 0
 end
 begin
      prog = irexec
      button = next
      config = mpc next
      repeat = 0
 end
 begin
      prog = irexec
      button = volup
      config = mpc volume +2
      repeat = 1
 end
 begin
      prog = irexec
      button = voldown
      config = mpc volume -2
      repeat = 1
 end
 begin
      prog = irexec
      button = pbc
      config = mpc random
      repeat = 0
 end
 begin
      prog = irexec
      button = pdvd
      config = mpc update
      repeat = 0
 end
 begin
      prog = irexec
      button = right
      config = mpc seek +00:00:05
      repeat = 0
 end
 begin
      prog = irexec
      button = left
      config = mpc seek -00:00:05
      repeat = 0
 end
 begin
      prog = irexec
      button = up
      config = mpc seek +1%
      repeat = 0
 end
 begin
      prog = irexec
      button = down
      config = mpc seek -1%
      repeat = 0
 end

There are more functions for mpc, run  for more info.

## PulseAudio
## Local (as your own user)
No special options are required; just add a pulse output as described in the comments of mpd's configuration file.

## Local (with separate mpd user)
When run as its own user as per the wiki instructions, mpd will be unable to send sound to another user's pulseaudio server. Rather than setting up pulseaudio as a system-wide daemon, a practice strongly discouraged by upstream, you can instead configure mpd to use pulseaudio's TCP module to send sound to localhost:

First, edit the PulseAudio configuration - either the user configuration in  (typically ) if it exists, otherwise the system-wide configuration file in  and uncomment the TCP module and set 127.0.0.1 as an allowed IP address like this:

 ### Network access (may be configured with paprefs, so leave this commented
 ### here if you plan to use paprefs)
 #load-module module-esound-protocol-tcp
 load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1
 #load-module module-zeroconf-publish

Additional IP ranges in cidr notation may be added using  as the separator. Once this is complete, restart pulseaudio:

 $ pulseaudio --kill
 $ pulseaudio --start -or- start-pulseaudio-x11/kde

Next, edit  and add a new pulse output pointing to 127.0.0.1 as a "remote" server:

 audio_output {
        type		"pulse"
        name		"Local Music Player Daemon"
        server		"127.0.0.1"
 }

Once this is added, restart mpd.

You should now have a working local mpd, usable by all users whose pulseaudio servers allow sound from 127.0.0.1.

## Remote
As with any PulseAudio-enabled program, mpd can send sound over the network. The complete PulseAudio system is not required on the server running mpd;  is the only requirement to act as a source and is already a dependency of mpd.

In order to send audio from mpd to another computer follow the directions above, editing  on the server running mpd using the IP address of the target computer and  or  (typically ) on the target computer using the IP address of the server.

Once this is done, the server's mpd source should show up on the target computer while playing or paused as a normal source able to be rerouted and controlled as usual; there will be no visible source on the target while mpd is stopped.

## Cue files
No additional steps are needed for cue support in mpd since 0.17. MPD has its own integrated parser which works with both external and embedded cue sheets.
For example, the command  loads the file  as playlist; or in the case of an CUESHEET tag, .

Client support of cue files is a bit limited. Two available programs that do support CUE files are  and ncmpcpp.

## HTTP streaming
Since version 0.15 there is a built-in HTTP streaming daemon/server that comes with MPD. This allows MPD to broadcast its music to HTTP clients.

This is not meant to be used as a streaming solution (e.g. replacement of Spotify, Deezer, etc.). First, it only allows one stream to be played, so multiple users cannot listen at the same time to different music. Second, MPD buffers audio a lot so that it plays reliably even when the client drops the connection for a while, therefore it introduces a non-negligeable latency when changing songs. To use MPD as a streaming solution, see #Music streaming with the satellite setup.

## Configuration
To activate this server simply set it as output device in mpd.conf:

 audio_output {
 	type		"httpd"
 	name		"My HTTP Stream"
 	encoder		"opus"		# optional
 	port		"8000"
 #	quality		"5.0"			# do not define if bitrate is defined
 	bitrate		"128000"			# do not define if quality is defined
 	format		"48000:16:1"
 	always_on       "yes"			# prevent MPD from disconnecting all listeners when playback is stopped.
 	tags            "yes"			# httpd supports sending tags to listening streams.
 }

## Format
MPD supports several encoding formats. See what your MPD supports with:

 $ mpd --version

## Use
Then to listen to this stream simply open the URL of your mpd server (along with the specified port) in your favorite music player. Note: You may have to specify the file format of the stream using an appropriate file extension in the URL. For example, using Winamp 5.5, You would use http://192.168.1.2:8000/mpd.ogg rather than http://192.168.1.2:8000/.

To use mpd to connect to the stream from another computer:

 mpc add http://192.168.1.2:8000

## Music streaming with the satellite setup
While #HTTP streaming allows the user to broadcast its music over HTTP, the satellite setup allows multiple users to listen to different songs at the same time, on separate machines.

## Topology
The satellite setup involves two or more machines: a server and multiple clients. The server is typically the machine that has the music files. It runs an MPD instance that will browse these files and build a database. The clients are the machines that will actually play the music (e.g. your phone or your laptop). They will also run MPD instances, though these ones will fetch the database from the server MPD and play the music. You might notice that MPD on the server is not necessary, however it greatly increases the speed to list all songs, as the client's MPD will not have to browse all the files remotely.

Besides, you will need a way for the server to make the music files available to the clients. MPD supports multiple storage plugins to fetch the music with. For example, if you choose the curl plugin, you will need a WebDAV server on the server.

Finally, you will need a secure communication tunnel between the server and each client. This is because the protocol used to control MPD is not encrypted and does not provide authentication. A VPN or a SSH tunnel will be useful here.

## Configuration
On the server, write the configuration file for the MPD instance that will build the database:

{{hc|/etc/mpd.conf|
pid_file            "/run/mpd/mpd.pid"
playlist_directory  "/var/lib/mpd/playlists"
music_directory     "/path/to/your/music/"

database {
    plugin           "simple"
    path             "/var/lib/mpd/mpd.db"
    cache_directory  "/var/lib/mpd/cache"
}

audio_output {
    type  "null"
    name  "This server does not need to play music, but it can"
}
}}

Then, setup either the WebDAV server, the NFS server or the Samba share.

On each client, write the configuration file for the MPD instance that will play the music:

{{hc|/etc/mpd.conf|
pid_file            "/run/mpd/mpd.pid"
playlist_directory  "/var/lib/mpd/playlists"

# WebDAV setup
music_directory     "https://optional_user:optional_password@example.com/path/to/your/music/"

# NFS setup
music_directory     "nfs://example.com/path/to/your/music/"

# Samba setup
music_directory     "smb://example.com/path/to/your/music/"

# Note the proxy here
database {
    plugin  "proxy"
    host    "example.com"
    port    "6600"
}

audio_output {
    type  "alsa"
    name  "Some output name"
}
}}

{{Note|1=
* libsmbclient has a serious bug which causes MPD to crash, and therefore this plugin is disabled by default and should not be used until the bug is fixed * On Android the configuration file needs to be at the root of the user storage, alongside the  folder. Also, files MPD writes to need to lie in the application folder, generally in . For example:

{{hc|/storage/emulated/0/mpd.conf|
music_directory  "http://example.com/Music"
log_file         "/data/user/0/org.musicpd/cache/log"
state_file       "/data/user/0/org.musicpd/cache/state"

audio_output {
    type  "sles"
    name  "Android only supports OpenSL ES"
}
}}

}}

## MPRIS support
See also MPRIS.

## mpDris2
Install the  package. It runs in the user session and monitors the mpd server.

Copy the default configuration file from  to . Edit it as needed.

After installation, you can start/enable the  user unit.

## mpd-mpris
Install the  package.

After installation, you can start/enable the  user unit.

By default mpd-mpris connects to  (which is the default host/port of mpd). To change this settings copy  to  then edit run parameters as needed.

## Notifications
The  package optionally supports displaying graphical notifications.
If you do not want [https://specifications.freedesktop.org/mpris-spec/latest/ mpris support and are looking for a more lightweight or specific option, here are some alternatives:

## musnify-mpd
musnify-mpd is a simple python script that provides notification support for Music Player Daemon using .
It can also display the album covers loaded from last fm or load it from the user-local music library.

The  package is available.

After installation you may want to configure your mpd host and port. To do this copy the ".example" file into

 $ mkdir ~/.config/musnify-mpd
 $ cp /usr/share/doc/musnify-mpd/musnify-mpdconfig.example ~/.config/musnify-mpd/musnify-mpd.config

Example configuration:

To enable artworks from last.fm, you will need to edit  and provide a apiKey. You can create your apiKey here

## mpd-notification
Notify about tracks played by . This runs in the background and produces notifications whenever mpd produces an event (e.g. new track is played, playback paused or stopped). This also supports local or  album artworks.

The  package is available.

After installation, just run  to run it once. The  user unit can be enabled to start it automatically.

## Adding a separate volume control (ALSA)
While MPD does not allow you to adjust its own volume by default ( affects global volume), you can easily make a MPD-specific volume slider using the softvol ALSA module.  Just add this to :

{{bc|
pcm.mpd {
    type softvol
    slave.pcm "default"
    control.name "MPD Playback Volume"
    control.card 0
}
}}

And link it to MPD:

{{hc|mpd.conf|
audio_output {
    type "alsa"
    name "ALSA"
    device "mpd"
    mixer_control "MPD"
}
}}

Afterwards you should be able to adjust song volume both through  and .  (You may need to reboot for the control to work properly.)

## Control the remote mpd server
To control the remote mpd server, if you have an ssh server on the same machine, you can login and use ncmpcpp to control it.

Or, if your mpd server is listening on an accessible interface/port ( on the mpd machine will show mpd listening on 0.0.0.0, for example) then you can set the MPD_HOST variable which directs a local client like mpc to the remote server.

 $ export MPD_HOST=ip.of.server
 $ export MPD_PORT=6600      # optional
 $ mpc play
