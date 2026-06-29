# Valheim

Valheim is a survival and sandbox game made by Swedish developers at Iron Gate Studio. It is currently in early access since 2nd February 2021 with no full release date announced so far.

This guide is related to the Steam version of the game, which has a native Linux build since it is built with Unity3D engine.

## Installation
## Without mods
If you buy the game on Steam you will also have the Valheim Dedicated Server tool, but you can install  and edit  to change the name, port, password, and world name of the server.

Start/enable . The server will log into the journal.

If you want to import the world you played previously, you should find your data in  or  when using Proton.

This server uses its own configuration directory at

The default port is 2456.

## With mods, BepInEx client and server
BepInEx is a plugin/modding framework for Unity games.

Due to an issue with stripped DLLs, the release from the BepInEx page cannot be used.

Denikson's pack contains the fixed DLLs. Download the zip manually, as using the Windows only Thunderstore Mod manager will not be covered here.
This will work only with the native version, not when launching via Proton.

In the zip, there is folder BexInPack_Valheim, unpack its contents to the root folder of Valheim, so you have BenInEx folder and  in the same folder as .

Make the  executable and in Steam go to the game's properties and set the game's launch arguments to:

 ./start_game_bepinex.sh %command%

And start the game, you should see in the top left corner that one plugin is loaded and the bottom right corner should have information that Valheim is modded.

Now you can download mods and unpack the .dlls to .

* BepInEx ConfigurationManager - allows Open Config Menu button in the bottom left to check which mods loaded and edit their configs.

## Server
For the server, you will need to have Valheim Dedicated Server tool installed (available in Steam), unpack the same Denikson's pack to the root of a dedicated server. Edit the  and edit the name, password, etc... parameters.

Run the script and the server should create .

Some mods will require the .dll to be in the plugin folder on both the client and server.
