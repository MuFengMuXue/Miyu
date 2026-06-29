# Audacious

Audacious is a free and advanced audio player. It is focused on audio quality and supports a wide variety of audio codecs, and is easily extensible through third-party plugins.

## Installation
Install the  package.

## Configuration
## Plugins
## AMIDI-Plug (MIDI Player)
To play MIDI and RMI files, it is required to install the  package, and also install the sound font files, both  and . No further configuration is required on the fluidsynth package, but for additional functionality check the FluidSynth instructions.

Afterwards, the plugin will be enabled, and in the plugin configuration panel (File, Settings ..., Plugins pane, Input tab, select AMIDI-Plug (MIDI Player)) add the installed sound font files one at a time (Extension ) to the SoundFont dialog, they are located at .

## Tips and tricks
## Audtool
Audacious is shipped with a powerful management tool called Audtool which could be used to retrieve information or to control the player.

For example, to retrieve the current song's title or artist, issue the following commands:

 $ audtool current-song
 $ audtool current-song-tuple-data artist

There are also functions to control playback, manipulate the playlist, equalizer and main window. See  for the whole list of options.

## Winamp
To add classic Winamp skins to Audacious, just copy them to either  (user only) or  (system wide), then select them from the Skinned Interface tab in Preferences. Alternatively drag the skin file directly into the list view of available skins.

## Troubleshooting
## Audacious starts instead of file manager
See File manager functionality#Directories are not opened in the file manager.
