# Doom

From Wikipedia:

:Doom is a first-person shooter game developed and published by id Software. Released on December 10, 1993, for DOS.

Following Doom's success, the source code for the Doom engine was released under GNU GPLv2 in 1997 by John Carmack (the original source code can be found at https://github.com/id-Software/DOOM). It now lives on in multiple ports, though you will still need to have a copy of the original game's data to play it and Doom 2 (also called the "IWAD").

## Installation
## Games/WADs
Also see List of games#Shooters (FPS, third person) for more Doom-related packages.
You can find WADs created by the community in the IDGames archive and other sites.

## Freedoom
Freedoom aims to be a completely free and open source reimagining of Doom. Its WADs are intended to function as drop-in replacements for the commercial files compatible with the entire back catalog of Doom mods, thus enabling users to access them without the need to purchase non-free software. Install .

## Doom Shareware
The  package supplies the original Doom shareware IWAD.

## Engines
A source port is a game engine that can be used to play Doom.
Most Doom source ports support common command-line options. Below is a table that describes the most commonly used ones.

{| class="wikitable"
|-
! Command-line option !! Description
|-
| -iwad doom2.wad || Use doom2.wad as the IWAD (Internal WAD) data-file.
|-
| -file scythe.wad  || Load scythe.wad as the PWAD (Patch WAD). Use this option to load maps and mods created by the community.
|-
| -skill 4 || Set the difficulty setting to Ultra-violence.
|-
| -playdemo demo1.lmp || Load user demo. Note that you need to have matching versions of WAD(s). You also need to set the correct game engine compatibility level setting.
|}

The most widely used source ports include the following.

## GZDoom
An updated version of ZDoom, GZDoom is the go-to standard for compatibility with the most mods and games based on the Doom engine. Install the  package to install it.

## UZDoom
UZDoom is a GZDoom fork with similar goals as GZDoom. Install .

## Chocolate Doom
Chocolate Doom is a port that tries to be as historically-accurate to the original games as possible.
Install .

## DOOM Retro
DOOM Retro is based off of Chocolate Doom, but tailored to the project author's taste. Install .

## DSDA-Doom
DSDA-Doom is a modern successor of PrBoom family of source ports. It is named after the Doom Speed Demo Archive and it includes features facilitating Doom speedrunning, among other improvements.
Install .

## Zandronum
Zandronum is a source port in the ZDoom family.
Like its predecessor Skulltag, its main area of focus is on delivering great multiplayer support.
It's packaged on the AUR as  package.

You can also install the Doomseeker tool to conveniently find multiplayer servers.
It's packaged as  on the AUR.

## Editors
There exist a number of editors to manipulate the data in Doom WADs in order to create maps, weapons, and even whole games using the Doom engine.

## SLADE
SLADE is a WAD inspector, allowing users to see and modify the data lumps within, such as textures, sprites, scripts and info lumps. It also comes with a built-in map editor.
Install the  package to install SLADE3.

## Ultimate Doom Builder
Specifically a map editor, Ultimate Doom Builder is written in .NET, and is the de-facto standard for creating Doom maps. Install .

## DoomTools
DoomTools is a suite of utilities written in Java that assist in creating modifications for Doom engine games. Most notable are DoomMake, which allows building mods in CMake-like fashion, and DECOHack, which simplifies creating DeHackEd patches by using domain-specific language. DoomTools are available by installing

## Eureka
Eureka is another map editor for Doom.
It's available from the AUR as .

## Node builders
The original vanilla Doom engine as well as certain source ports require that custom WADs include a section (also known as a lump) that contains nodes.
However, ZDoom-based source ports (including GZDoom) can build them on demand and they don't require that a WAD comes with them pre-generated.
More information on nodes can be read at Doom Wiki and ZDoom Wiki.

As an example of a node builder is , and it's available from the AUR.
However, several others exists as well.

## Configuration
Most Doom maps and mods will require a Doom or Doom 2 IWAD to work. Many modern source ports will look for WAD files in . You may override this path by setting  environment variable.

## GZDoom
The base GZDoom config file is located under .

To add the directory containing your IWADs so that GZDoom can see it, add the following to the config file underneath :

,

where  is the path to where your IWADs are.

## Troubleshooting
A good resource for troubleshooting GZDoom is the ZDoom Wiki. It also has good resources on mapping, scripting, and other information when creating for Doom. You can find a lot of information on Doom games at the community Doom Wiki. You can also ask questions on the Doom World forums.
