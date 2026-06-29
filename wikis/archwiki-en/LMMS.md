# LMMS

LMMS is a free cross-platform software which allows you to produce music with your computer. This covers creating melodies and beats, synthesizing and mixing sounds and arranging samples. You can have fun with your MIDI keyboard and much more – all in a user-friendly and modern interface. Furthermore LMMS comes with many ready-to-use instrument and effect plugins, presets and samples.

## Installation
Install , or  for the development version. See https://github.com/LMMS/lmms/releases for release notes.

As always, if you want to use multiple audio applications simultaneously but your hardware does not natively support this, you will need either a usermode sound server, or to configure ALSA dmix.

## MIDI and soundfonts
Depending on your setup and the installation method, you might need to manually setup a soundfont and Timidity.

Then, you will need to edit the FluidSynth configuration file: . For the audio driver, choose the sound server that you installed.

Start the user service .

When LMMS starts, it will prompt you with the settings. Go to the audio settings, choose the same interface that you set for FluidSynth, and restart LMMS if you made a switch.

## Troubleshooting
Some users are having troubles with drag-and-drop support on Wayland. To restore this functionality, you can try setting the environment variable  to let LMMS start in Xwayland.
