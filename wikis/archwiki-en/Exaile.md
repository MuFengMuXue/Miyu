# Exaile

Exaile is a music manager and player for GTK written in Python. It incorporates automatic fetching of album art, lyrics fetching, Last.fm scrobbling, support for many portable media players, internet radio such as shoutcast, and tabbed playlists.

## Installation
Install the  package.

If you use ALSA and want to use alsasink instead of the default one, install . This may solve problem if no sound is heard after installation and also when trying to play several sources simultaneously.

## Playing audio CDs
Exaile requires  to play audio CDs. The correct package for this is .

## Enabling multimedia keys irrespective of DE/WM
First, run  and retrieve the keycodes for the Previous, Next, Play, Stop, and Mute keys. Then create a textfile and add lines in the following format: . Replace the keycode (173) with your own keycode for the Previous key. Repeat the process for the other keys, substituting 'Prev' for 'Next', 'Play', 'Stop', and 'Mute'.

Then edit  and add the line  prior to the 'exec' command (if there is one) for the DE/WM, where  is the path to the text file created above.

Finally, in Exaile, go to Edit > Preferences > Plugins, and enable the XKeys plugin. After a restart, multimedia keys should work.

## Troubleshooting
## Progress bar stuck at 0:00
First, make sure there are no problems with your sound architecture (ALSA, OSS, etc.). And your playback sink in Exaile is set correctly. Try setting it to automatic first.

If you are trying to listen to an MP3 file, try playing an audio file encoded in a different format, such as .ogg or .flac.

## "Playback error encountered! Configured audiosink bin0 is not working"
If you are getting a message like this, or "Configured audiosink bin1 is not working" (or with another number after 'bin'), it may be because Flash is blocking the use of ALSA by Exaile. You can fix this by running

 $ killall npviewer.bin

In certain cases (such as if a YouTube video has finished playing), Flash may be blocking the use of ALSA even if an 'npviewer.bin' process is not running. In that case, refreshing the offending page while using a Flash blocking browser extension should fix the problem.

## "Last.fm Loved Tracks" plugin not working
When launched from console, Exaile emits a warning in the command line:

 WARNING : Error while connecting to Last.fm network: 'module' object has no attribute 'LastFMNetwork'

You need to install the .

## "Playback error encountered! No suitable plugins found"
Install all plugin packages listed in the GStreamer article and try again.

## Known issues
## Playing from SMB share
Unfortunately, Exaile does not support smb protocol.
