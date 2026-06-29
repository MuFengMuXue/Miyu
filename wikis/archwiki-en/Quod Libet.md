# Quod Libet

Quod Libet is a music player written in Python and based on GTK, extendable using native or user plugins, and supporting a lot of audio formats using GStreamer as backend. It supports ReplayGain, reading and writing tags, displaying album arts and lyrics, filtering library based on regular expressions, and more.

The Quod Libet project provides 3 commands:
; : The player and library manager, supporting a CLI.
; : The graphical tag manager.
; : The command-line tag manager.

## Installation
Install the  package.

## Extending decoding capabilities
Quod Libet can benefit from Libav-based codecs through GStreamer (e.g. to decode Monkey's Audio (APE) files). To enable this, install the  package and restart the audio player.

## Extending plugins list
Quod Libet can benefit from some GStreamer's plugins (e.g. to compute ReplayGain information). To make them available in the Quod Libet's plugins list, install the  package and restart the audio player.

## Configuration
## Configuring the player core
In the menu, go to File and then Preferences. From here, you can configure the library path, enable ReplayGain, and configure the player layout.

## Enabling plugins
The default preferences of the player are not exhaustive. A more advanced configuration is done via
plugins. To enable them, in the menu, go to File > Plugins, and enable the desired plugins.

Here is a list of interesting plugins:

; Alternative progress bar: Display a progress bar at the top of the window.
; Waveform search bar: Display a waveform progress bar instead of a simple bar.
; Change theme: Configure the interface theme.
; ReplayGain: Add a button in contextual menu to compute ReplayGain information for selected files.
; Information overlay: Add an OSD during title change.
; D-BUS MPRIS support: Add MPRIS support through D-BUS allowing to control the media player using keyboard multimedia keys.
; Display lyrics: Add a panel at the right of the display to show embedded lyrics.

## Plugins
## ReplayGain
ReplayGain is disabled by default on Quod Libet. You must enable it in the preferences so that the volume of tracks will be adjusted at runtime based on ReplayGain tags.

Quod Libet is able to compute ReplayGain information and store it in the tags of audio files. It relies on the GStreamer's rganalysis plugin. To do so:
* Ensure GStreamer's plugins are installed through the  package.
* Enable the ReplayGain plugin, right click on a file, go to Plugins and click on ReplayGain.

## External control
Quod Libet can be controlled programmatically using MPRIS through D-Bus. To do so, enable the D-BUS MPRIS support plugin. It allows control using multimedia keys and terminal.

The following demonstrate some examples of player control using the terminal.

; Set the playback volume to 50%:

 $ dbus-send --dest=org.mpris.MediaPlayer2.quodlibet --print-reply /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Set string:org.mpris.MediaPlayer2.Player string:Volume variant:double:0.5

; Control playback action:
 $ dbus-send --dest=org.mpris.MediaPlayer2.quodlibet --print-reply /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next

Instead of Next, you can use one of the following actions: Pause, Play, Previous, Stop.

## Media server
Quod Libet can act as a media server using Music Player Daemon or Rygel as backends. To select and use one of them, enable the correspond plugins in the preferences.

## Troubleshooting
## Multimedia keys do not work
Multimedia keys work using the MPRIS interface. This interface has to be enabled in the plugins of Quod Libet to make them work.

## Interface freeze when title changes
Enabling a buggy plugin or too many sane plugins can sometimes leads to poor performance. Disable plugins until the freeze disappear, such that you can identify the faulty plugin. For instance, the Waveform search bar is known to cause some lags for low-end systems.
