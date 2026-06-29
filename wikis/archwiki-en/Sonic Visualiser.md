# Sonic Visualiser

From https://www.sonicvisualiser.org/:

:Sonic Visualiser is the first program you reach for when want to study a music recording closely. It's designed for musicologists, archivists, signal-processing researchers, and anyone else looking for a friendly way to look at what lies inside the audio file.

## Installation
Install the  package.

## Known issues
## Play button does not play the track (No audio)
Sonic visualiser requires PulseAudio to be set up to hear anything. For ALSA-only users, using  as described in Advanced Linux Sound Architecture#apulse gets the audio working.

 $ apulse sonic-visualiser

The terminal messages will still have , but can be ignored. Audio should play with no issues.
