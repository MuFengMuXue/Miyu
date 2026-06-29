# Icecast

Icecast is a program for streaming media such as audio and video across a network.
Different types of clients connect to the IceCast server, either to provide a "mount point", control the server, or listen to the audio being cast.

Icecast has support for streaming many audio streams simultaneously - each stream has a "mount point" which a client can access, with a network URI such as  (this refers to a mount point called "example").

## Installation
Install .

## Configuration
All configuration is done in .

By default icecast listens on port . It can listen on more than one port - this behavior can be changed by modifying one or more  sections.

Icecast binds to all interfaces (i.e. ) by default. To change this behavior, modify a  section below a respective  section.

To set defaults for all mounts that do not specify their type (e.g. ) the  section can be modified:

## Running
Enable and start .

To verify that icecast is running go to http://localhost:8000/ or check the status of .

## Streaming
Several programs are able to stream to icecast based on a  set in the  section of the configuration.

## MPD
Make sure to setup MPD and a client to control it.

Configure MPD (as system or user service) to be an icecast source:

{{hc|mpd.conf|
audio_output {
    type        "shout"
    encoding    "ogg"
    name        "my cool stream"
    host        "localhost"
    port        "8000"
    mount       "/example.ogg"
    user        "source"
    password    ""

# Set either quality or bit rate
#   quality     "5.0"
    bitrate     "64"
    format      "44100:16:1"
# Optional Parameters
#   description "here is my long description"
#   genre       "jazz"
}

# Need this so that mpd still works if icecast is not running
audio_output {
    type "null"
    name "fake out"
}
}}

Start .

The icecast web interface should now list this new stream and the playlist should be available as http://localhost:8000/example.ogg.m3u

## ezstream
 is a native source client for icecast. It uses XML files for configurations, like icecast

Several examples can be found in /usr/share/examples/ezstream/.
It supports mp3, Ogg Vorbis, Ogg Theora, for streaming video ffmpeg2theora can be used to reencode into Ogg Theora.

After configuring, stream can be started by

Multiple media can streamed by creating a m3u playlist and defining it under  in configuration file

## XMMS2
 is a minimal music player which can be controled with several clients, setting this up is fairly simple compared to MPD and media can be added to stream on fly unlike ezstream.

Icecast configuration can be displayed with:

These can be changed as follows,

Change the output as ices so XMMS2 can mount the stream on icecast server.

Upon starting, the stream should be working and files can be added with the command "add".

Alternatively, XMMS2 can be controlled with  which provides a simple GUI.

## VLC
 is a full-featured media player and transcoder with built-in support for Icecast streaming. It can be controlled via GUI or command line, and can act as an Icecast source for  media files or real-time audio captured from JACK output ports and other sources. For example, this command connects VLC to the first JACK audio output ports it finds, encodes the audio as Ogg Vorbis, and streams it to an Icecast mount point at :

{{bc|
$ cvlc 'jack://channels=2:ports=.*' ':sout=#transcode{vcodec=none,acodec=vorb,ab=192,channels=2,samplerate=44100,scodec=none}:std{access=shout,mux=ogg,dst=//source:hackme@localhost:8000/stream.ogg}' :no-sout-all :sout-keep
}}

Alternatively, VLC offers a guided GUI to stream to an Icecast server. When opening any media source, choose Stream and then add Icecast as a destination. You will be prompted for the network Address, Port, Mount Point, and Login:pass. Use  as the format for the latter. Select the desired transcoding options on the next screen and you are ready to go.

## Playback
Streams can be listened to via a web browser when visiting http://localhost:8000.

Additionally, there are several clients that can make direct use of a provided playlist file (e.g. http://localhost:8000/example.ogg.m3u)

## MPD
Icecast streams can be played back using MPD.

Use an MPD client such as  to add the URL of an icecast playlist file to the playlist of a (local) MPD instance:
 $ mpc add http://localhost:8000/example.ogg.m3u

The added item behaves like any other track in the MPD playlist.

## MPlayer
Install the  package.

Start the program and provide it with the icecast playlist:
 $ mplayer -playlist http://localhost:8000/example.ogg.m3u

## Mpv
Install the  package.

Start the program and point it at the icecast playlist:
 $ mpv http://localhost:8000/example.ogg.m3u

## Sonata
* Install the  package.
* Start it up and you should be greeted by Sonata's preferences.
* Set 'Name' to the name of your server.
* Set 'Host' to the IP address of your server.
* Set 'Port' to '6600'.
* Click the '+' and repeat the previous steps but instead about your local computer (i.e. its name and IP).
* Right-click->'Connections' and select your server. Then click on the 'Library' tab, if all is well, you should see your entire music selection that is on your server. Find a folder, right-click and click 'Add'. Clicking on the 'Current' tab will show you your current playlist, which should have the contents of whatever folder you just chose from the library. Double-click on a song. You should see the text get bold and the progress bar show up, just like it is playing, but you will not hear anything. Fear not.
* Right-click->'Connections' and select your local computer. Then click the 'Streams' tab. Right-click and click 'New'. Make 'Stream Name' the name from your servers /etc/mpd.conf file's audio_output { } section and make the URL IP.of.server:8000/example.ogg.m3u. Double-click on this stream.
* Click on the 'Current' tab and you will see the URL of the stream as your only item. Double-click on it and after a delay you should hear whatever song you had chosen on the server.

## VLC
In addition to acting as an Icecast source,  can play back streams from Icecast and other network audio sources. Choose Open Network Stream... and provide the URL when prompted.

## Tips and tricks
## Running Icecast in a chroot environment
Change following settings in :

Edit the  section of :

Now change this entries in :

Create a log directory under  and set the permissions:

## Local user
Note that if you are running icecast under a local user (i.e. one that does not use /etc/icecast.xml) then you will need to copy the icecast web xml files from /usr/share otherwise you will get errors about XSLT and the web interface will not work.

Also, make sure that the  section in the icecast configuration file is commented out, as changing the owner of a process requires root privileges.
