# MOC

Music On Console is a lightweight music player similar to MPD, but unlike it, MOC comes with an interface and its server does not support remote access.

## Installation
Install . To use the pulseaudio driver, go to #Using PulseAudio.

## Front-ends
*
*

## Configuration
On mocp first run, the  directory is created.  MOC reads its configuration from the file .

Sample configuration files can be found in .  To configure, copy the examples to  and edit accordingly.

To use MOC with v4.1 OSS, see OSS#MOC.

To change the default key bindings, see .

## Using PulseAudio
Locate the variable  and add  to the front.

 SoundDriver = PULSEAUDIO:JACK:ALSA:OSS

This ensures that PulseAudio gets loaded with first priority. Listing other sound drivers after this are fallbacks when the previous ones are not available.

## Navigation
To change directories with the arrow keys uncomment in :

 Keymap = keymap

Edit the following in :

 go    = ENTER RIGHT
 go_up = U LEFT
 #seek_forward  = RIGHT
 #seek_backward = LEFT

To speed up navigation and detach, set the following in :

 ReadTags = no
 ShowTime = no
 TagsCacheSize = 0

## systemd service
Enable this service for the respective user:

## Themes
Several themes for the player GUI are available. To list the available themes and set one, use hotkey .
To set one to permanent use the configuration file .

 Theme = laras_theme

A selection of example themes can be found in , the installation of  adds more of them.

Since themes are just text files, it is easy to create new ones. User defined themes are expected in .

Example theme file:

 background                     = white black
 frame                          = white black
 window_title                   = white black
 directory                      = white black
 selected_directory             = white black reverse
 playlist                       = white black
 selected_playlist              = white black reverse
 file                           = white black
 selected_file                  = white black reverse
 selected_info                  = white black reverse
 marked_file                    = white black bold
 marked_selected_file           = white black reverse
 info                           = white black
 marked_info                    = white black bold
 marked_selected_info           = white black reverse
 status                         = white black
 title                          = white black bold
 state                          = white black
 current_time                   = white black bold
 time_left                      = white black bold
 total_time                     = white black bold
 time_total_frames              = white black
 sound_parameters               = white black bold
 legend                         = white black
 disabled                       = white black
 enabled                        = white black bold
 empty_mixer_bar                = white black
 filled_mixer_bar               = white black reverse
 empty_time_bar                 = white black
 filled_time_bar                = white black reverse
 entry                          = white black
 entry_title                    = white black
 error                          = white black bold
 message                        = white black
 plist_time                     = white black

## Usage
Run mocp to start the server and interface. Some useful default shortcuts (press  for more):

{| class="wikitable"
|-
| Start playing at this file or go to this directory
|
|-
| Pause
|  or
|-
| Play next file
|
|-
| Play previous file
|
|-
| Silent seek forward by 5s
|
|-
| Silent seek backward by 5s
|
|-
| Switch between playlist and file list
|
|-
| Add a file/directory to the playlist
|
|-
| Add a directory recursively to the playlist
|
|-
| Delete an item from the playlist
|
|-
| Clear the playlist
|
|-
| Increase volume by 1%
|
|-
| Decrease volume by 1%
| {{ic|?@or a space. This is known to cause an authentication error with mocpscrob configurations which specify passwords not conforming to these new specifications. Changing one's password and updating the  password accordingly resolves this issue.

## Troubleshooting
## MOC fails to start
If MOC fails to start, it is most probably because of something wrong in . You can try to fix it, or simply delete the whole folder.

## Strange characters
If you see strange-like characters displayed instead of the normal lines (vertical lines to separate space, etc.), you may have a font set incompatible to MOC. Either change the respective font, or edit  to use ASCII for drawing lines:

 ASCIILines = no

## FATAL_ERROR: Layout1 is malformed
If MOC crashes with this error, try adding either line to :
 Layout1 = directory(0,0,50%,100%): playlist(50%,0,100%,100%)
or
 Layout1 = directory(0,0,50%,100%): playlist(50%,0,FILL,100%)

See [https://moc.daper.net/node/262 original report and Debian bugs.

## Bluetooth not working unless it is connected before MOC is started
When using pipewire, MOC defaults to JACK which appears to be the cause of this issue. Simply changing from jack to ALSA solves this issue through changing the following value within the configuration file:

Default value:

New value:

MOC picks the first working audio driver, thus ALSA will be picked first. This should fix the bluetooth issues.
