# OpenTTD

OpenTTD is a free re-implementation of the popular DOS game Transport Tycoon Deluxe. You are a transport company owner, and you must manage it over the years in order to make profit.

## Installation
Install the  package.

If you do not own the original game,  and  contains the free graphics & sounds.

Additionally, you may install the free OpenMSX music pack either from openttd.org, from  or in-game from the main menu option Check Online Content. You can check FluidSynth#Standalone mode to make sure FluidSynth works properly.

## Original Transport Tycoon Deluxe data (optional)
OpenTTD can use the non-free graphics and sound data of the original Windows/DOS version of Transport Tycoon Deluxe.

You can get these files from the game CD-ROM, from an existing install or you get them from the freely available game installation archive available at Abandonia.

To use the original graphics & sound effects, copy the following files to  or  :

* Windows : trg1r.grf, trgcr.grf, trghr.grf, trgir.grf, trgtr.grf
* DOS : TRG1.GRF, TRGC.GRF, TRGH.GRF, TRGI.GRF, TRGT.GRF
* sample.cat from either version

For the original soundtrack, copy the files from the gm folder of the original TTD game directory to .

## Tutorial
The game can be quite confusing at first.  A good tutorial is available on the wiki here.

For an in-game tutorial, a game script has been implemented.  Just download 'Beginner Tutorial' with the in-game download manager and load the 'Beginner Tutorial' scenario.

## Configuration
The OpenTTD main configuration file is located at  and is automatically created upon first startup.

Various settings in the configuration file can be edited with buttons on the main menu.

## Multiplayer
## Client
Players can join a server using the Multiplayer menu. In multiplayer, fast forwarding, pausing by the player and cheats are disabled.

All problems with a server should resolve the administrator of the server and are usually not a bug, just a misconfiguration on the server.

## Server
You can start the server by passing the  argument, e.g.:

 # openttd -D 0.0.0.0:3979

This starts the server and accepts additional commands. Configuration is generated and stored in  and is read every time the server starts. It can be overriden with commands issued directly to the server while running. Some settings cannot be changed during a game.

## Tips and tricks
## Heightmaps
OpenTTD allows using a grayscale image as a heightmap for landscape generation. There is an excellent heightmap generator available at terrain.party, based on real Earth terrain. Alternatively, you can use the  application, which can download larger areas and contains a number of options for fine-tuning the resulting heightmap (see the README for some notes on usage). You may further use  for fine-tuning the heightmap, especially useful are the Levels and Gaussian Blur tools.

## Cheats
A cheat menu can be shown in a local game by pressing .

Detailed information about cheats are available for sandbox (single player) and multiplayer modes.

## Multiplayer
Always set a password for your own company to avoid others taking over. Some servers reset your password after some idle time.

Chat can be brought up with the  letter if the rail building menu is not open.

You can invest in other companies by buying shares (if enabled on server). You can later sell the shares for profit, or loss.

## Troubleshooting
## Music is not playing
The soundtrack of the game is made of MIDI files. Therefore, you need a MIDI synthesizer to play them.

The game will automatically try to use FluidSynth with no additional arguments. Make sure a soundfont is also installed. Usually, installing  should enable music playback.

If for some reason you need/want to use another synthesizer, OpenTTD provides the "extmidi" music driver, which allows you to configure a command to be ran to play music.

Edit your openttd.cfg to configure extmidi :

However, extmidi does not allow additionnal arguments in the command. The solution is to use a wrapper script:

Mark it as executable.

Then you can specify the full path to the script as the command to be used with extmidi :
