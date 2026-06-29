# TerraTec Aureon 7.1

The Terratec Aureon 7.1 USB is an affordable external sound card which supports optical and digital output through S/PDIF with full 5.1/7.1 surround sound.

## Installation
ALSA drivers are part of the kernel and have support for this sound card.

## Configuration
## Set the card as the default device
If you have multiple sound cards, you need to set the Terratec card as a default. Create the following file:

Rebooting may be required for the changes to take effect.

## Enable volume control
This card does not have hardware volume control, so you need to create software Master control.
Create the following file in your home folder:

{{hc|.asoundrc|
pcm.softvol {
        type softvol
        slave {
                pcm "dmix"
        }
        control {
                name "Master"
                card 0
        }
}

pcm.!default {
        type plug
        slave.pcm "softvol"
}
}}

Run  and check as you should have a Master volume control.

## Hotkeys
The sound card has external hotkeys for volume change and mute. You can capture the button presses by installing Xbindkeys and using the following config:

As you can see,  does not handle mute for this mixer, which is why you can use a simple mute.sh script, which stores the volume level in . Be sure to change the file path to mute.sh accordingly.

 #!/bin/bash
 var=$(amixer get Master | grep "Front Left:")
 var=$(echo "$var" | sed -ne 's/^if [ $var == "0%"
 then
         volume=$(cat volume.txt)
         amixer set 'Master' $volume
 else
         rm volume.txt
         echo $var > volume.txt
         amixer set 'Master' 0%
 fi

## Configure mplayer for surround sound (optional)
Add the following codec settings for mplayer:

Kodi can be used for media playback too, as most receivers do no support the AAC codec. Kodi will re-encode AAC to a common codec (AC3 probably) in realtime, so you can watch most surround sound media files. It also has a self-explanatory configuration system using a GUI.
