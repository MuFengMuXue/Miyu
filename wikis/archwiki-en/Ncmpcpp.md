# Ncmpcpp

Ncmpcpp is an mpd client (compatible with mopidy) with a UI very similar to ncmpc, but it provides new useful features such as support for regular expressions for library searches, extended song format, items filtering, the ability to sort playlists, and a local filesystem browser.

To use it, a functional mpd must be present on the system since ncmpcpp/mpd work together in a client/server relationship.

## Installation
Install the  package.

## Basic configuration
The shell "GUI" for ncmpcpp is highly customizable. Edit  to your liking. If, after installation,  has not been created, simply copy the sample config, change owner and edit at the very least the following three configuration options:

* mpd_host - Should point to the host on which mpd resides, can be "localhost", "127.0.0.1" or "::1" if on the same machine. To connect with a password, write "password@host"
* mpd_port - The default of mpd should be "6600"
* mpd_music_dir - The same directory value as specified in "music_directory" in

For inspiration, see the following resources:
* Sample configuration file in .
* Show your .ncmpcpp/config with screenshot forum thread

## Enabling visualization
For visualization, add a few lines to  or  to enable the generation of the fast Fourier transform data for the visualization:

 audio_output {
     type                    "fifo"
     name                    "my_fifo"
     path                    "/tmp/mpd.fifo"
     format                  "44100:16:2"
 }

Additional lines need to be added to

 visualizer_data_source = "/tmp/mpd.fifo"
 visualizer_output_name = "my_fifo"
 visualizer_in_stereo = "yes"
 visualizer_type = "spectrum"
 visualizer_look = "+|"

* visualizer_type - Set the visualization to either a // analyzer or  form.
* visualizer_look - Set the visualizer's look (string has to be exactly 2 characters long: first one is for wave and whereas second for frequency spectrum, wave_filled and ellipse).

If you use mopidy, visualization is handled via gstreamer's udpsink. Edit the  in the  block of your :

 output = tee name=t ! queue ! autoaudiosink t. ! queue ! audio/x-raw,rate=44100,channels=2,format=S16LE ! udpsink host=localhost port=5555

This forwards the audio data to port . For  to read from this port, change its  accordingly:

 visualizer_data_source = "localhost:5555"

## Tips and tricks
## Remapping keys
A listing of key bindings and their respective functions is available from within npmpcpp itself via hitting . Users may remap any of the default keys simply by copying  to  and editing it.

## Autoset Tags from Filename and vice versa
In the Tag Editor you can select a directory with music and then select the  option in the middle section. This opens a little window with two options:  and .
If you choose , a popup with two windows is shown. On the left side you can enter a pattern that extracts the selected information from the filenames. You can also hit  to see what the result would look like. On the right side you can see the legend containing all the possible keywords to be used for extraction.

A simple Example would be the pattern: . If your files are named according to this pattern (Artist - Title) then this pattern would extract this information and set the Tags for the File.

The other option  does the exact opposite. It takes the Tags from the audio files and creates a Filename from them.

## Notification on song change
notify-send can be used in the  command to generate notifications whenever the song changes (and upon application launch). This is contingent upon having a desktop notification server installed and configured. As an example:

 execute_on_song_change = notify-send "Now Playing" "$(mpc --format '%title% \n%artist% - %album%' current)"

## With album art
If you want song change notifications to have the album art of the currently playing song, you can use this script. Album art previews will be stored in  by default, scaled to 128x128. Preview filenames are the album names encoded in base64, so no duplicate previews should be saved.

Assuming  is in your , create (and make executable):

and add this to your ncmpcpp config:

 execute_on_song_change = songinfo
