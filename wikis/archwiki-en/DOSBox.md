# DOSBox

DOSBox is an x86 PC DOS-emulator for running old DOS games or programs.

## Installation
Install the  package. DOSBox has not seen a new release since 2019, you may want to try the  development version. Alternatively, two forks can be installed:

*  aims to modernize the codebase (and some distributions ship it as the default)
*  tries to emulate hardware much more accurately

## Configuration
No initial configuration is needed, however the official DOSBox manual refers to a configuration file named . By default that file exists in your  folder.

You can also make a new configuration file on a per-application basis by copying  from  to the directory where your DOS app resides and modifying the settings accordingly. You can also create a configuration file automatically: simply run  without any parameters inside your desired application's folder:

 $ dosbox

Then at the DOS prompt, type:

 Z:\> config -wc dosbox.conf

The configuration file  will then be saved in the current directory. Go in a change whatever settings you need.

The configuration options are described in the official DOSBox wiki.

## Usage
A simple way to run DOSBox is to place your DOS game (or its setup files) into a directory and then run  with the directory path appended. For example:

 $ dosbox ./game-folder/

You should now have a DOS prompt whose working directory is the one specified above. From there, you can execute the desired programs:

 C:\> SETUP.EXE

## Tips and tricks
## Free DOSBox focus
If DOSBox traps your focus, use  to free it.

## Play music in DOS games
To play music, some DOS games require a MIDI synthesizer which DOSBox does not emulate. However, DOSBox can use one if it is available. A software synthesizer such as FluidSynth or Timidity can be used if your computer does not have a hardware synthesizer.
