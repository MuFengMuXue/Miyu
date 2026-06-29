# Pianobar

Pianobar is a free/open-source, console-based client for the personalized online radio Pandora (only available in the USA).

Features
* play and manage (create, add more music, delete, rename, ...) stations
* rate songs and explain why they have been selected
* upcoming songs/song history
* customize keybindings and text output
* remote control and eventcmd interface (send tracks to last.fm, for example)
* proxy support for listeners outside the USA

## Installation
Install the  package.

## Configuration
First, you need to create a configuration file for Pianobar. This should be located at  or

Here is an example configuration file. See  for more configuration options.

{{hc|~/.config/pianobar/config|2=
audio_quality = {high, medium, low}
autostart_station = stationid

password = plaintext_password
user = your@user.name
}}

## Troubleshooting
## Sound Quality Issues
If you are experiencing sound/quality issues when running pianobar, and you are currently using ALSA as your sound driver, the following fixes may be useful.

Install . See the ALSA page for more information.

Change the default libao driver from  to :

Now run pianobar:

 $ aoss pianobar

Alternatively, you can use PulseAudio:

## Network Error
If you are receiving the , try adding the following line:
