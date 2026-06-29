# Rhythmbox

Rhythmbox is an audio player that plays and helps organize digital music. It is designed to work well under the GNOME desktop using the GStreamer media framework.

## Installation
Install the  package.

## Tips and tricks
## Playing remote media from Internet sources (blip.tv, Jamendo, SHOUTcast)
Rhythmbox takes advantage of the Grilo framework to browse external sources such as SHOUTcast webradios and more.

You need to install the  and  packages. Then, be sure to enable the Grilo Media Browser plugin into Rhythmbox ("Edit" > "Plugins").

## How to activate the Cover Art plugin
If you want to use the cover art plugin, but are unable to do so, you need to install .

After you do that, restart Rhythmbox.

This requirement also affects the Song Lyrics and Magnitune plugins, as well as several others.

## What to do when the little red icon shows when you try to play radio stations
First thing to do when the stop sign icon shows is to right-click the name of the station you are trying to listen to and open the Properties dialog box. Rhythmbox should give a bit more explanation about why it was unable to start playing the audio stream.

## Using the DAAP Music Sharing plugin
Install the optional dependency for DAAP sharing, , and set up hostname resolution with Avahi.

## Troubleshooting
## "Unknown Playback Error" when streaming or playing from regular files
Rhythmbox may display this error when it does not have the correct codec to play that stream. You will need to identify what format the stream is (by looking at the command line error messages that Rhythmbox displays) and then install the correct GStreamer codec for that particular audio stream: see GStreamer#Installation.

## "Error, impossible to activate plugin 'Audio CD Recorder'" shows up every time I start Rhythmbox
You have two options:
#install
#disable the cd recording plugin: Run , navigate to  and remove cd-recorder from active-plugins.

## Slow start and "Unable to start mDNS browsing: MDNS service is not running" output
You have two options:
#activate the DAAP Music Sharing (see #Using the DAAP Music Sharing plugin above)
#disable the DAAP plugin: Run , navigate to  and remove DAAP from active-plugins.

## Rhythmbox Startup is Slow
This can be easily fixed by disabling some of the plugins. For example, if you do not use a mediaplayer gnome-shell extension you do not need the MRPIS and D-bus plugins enabled.

## No cover are shown in the dedicated box
Creating a lastFM account and login in with the rhythmbox plugin can solve the problem.

## Cannot enable MTP device support
Install .

## Cannot enable iPod support
Install .

## Music files within the music library are not found
Sometimes it helps to remove the Rhythmbox library in order to rebuild it properly. Quit Rhythmbox, move  to an other directory. Restart Rhythmbox and rescan your music library.

## uPnP/DLNA Client does not work out of the box
Install  and . Then enable Grilo media browser plugin. DLNA server should appear under shared sources.

## Certain files return "Additional GStreamer plugins required"
Install . However, these plugins may pose distribution problems.
