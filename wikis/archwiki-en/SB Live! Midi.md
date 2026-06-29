# SB Live! Midi

SB Live! uses a wavetable synthesizer for its MIDI output. Therefore, in order to get MIDI output you need to load the SoundFont banks into the card.

## Installation
Install the  package.

Copy the SoundFont files from your SB Live driver CD somewhere on your disk. On the SB Live! Value CD, they are named: ,  and .

Load the bank by executing . See  for more advanced options. Some users have reported that  needs to be preloaded in order for this to work.

## Configuration
## Which bank to load?
The bank names (at least for SB Live! Value) correspond to their respective sizes (2 Mb, 4 Mb, 8 Mb). The bigger the bank is, the better the quality, although more RAM is also used, since SB Live Value does not have its own memory banks.

## Automating
Create a systemd service file to start  as a .
