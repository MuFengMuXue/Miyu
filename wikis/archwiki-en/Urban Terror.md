# Urban Terror

Urban Terror™ is a free multiplayer first person shooter developed by FrozenSand, that will run on any Quake III Arena compatible engine. It is available for Windows, Linux and Macintosh.

Urban Terror can be described as a Hollywood tactical shooter; somewhat realism based, but the motto is "fun over realism". This results in a very unique, enjoyable and addictive game.

## Installation
## Client
Urban Terror has been dropped to AUR (see ) : install .

## Mapping
A quick introduction on how to create your own maps.

## Install a map editor
Install .

## Prepare the game files
There are two ways use the second one if you are low on disk space.

## Extract your pk3s (recommended, ~1GB free disk space required)
To get something to work with, you need to extract Urban Terror's pk3 files to a new folder:
 $ install -d ~/urtmapping/q3ut4
 $ cd ~/urtmapping/q3ut4
 $ bsdtar -x -f /opt/urbanterror/q3ut4/zpak000_assets.pk3 --exclude maps
 $ bsdtar -x -f /opt/urbanterror/q3ut4/zpak000.pk3

## Give GTKRadiant write access to the game folder (for single user machines)
GTKradiant creates a few own files inside game directory on creating a game profile. This means that you can own to the Urban Terror folder temporarily until these are created:
 # chown yourusername -R /opt/urbanterror

Then start GTKRadiant and configure the game profile, just use  as path). Close it afterwards and restrict access again with:

 # chown root -R /opt/urbanterror

Please note, that your user will own the newly created files until they get deleted (which is just what we want in this case).

## Test your map
Copy your compiled .bsp mapfile to  and run:
 $ urbanterror +set fs_game iourtmap +set sv_pure 0 +map ut4_yourmap

## Tips and tricks
## Running Urban Terror without a window manager
See xinit#Starting applications without a window manager.

## Troubleshooting
## Fix urbanterror_ui.shader
Edit  and delete lines 29-55 (from /* to */), because gtkradiant will not recognize this part as a comment and would try to parse it.

## Problems with libcurl
UrbanTerror may complain that it cannot autodownload missing files because the cURL library could not be loaded, even though the cURL package is installed.  UrbanTerror expects the shared library file to be called libcurl.so.3, but Arch Linux currently uses libcurl.so.4.

To remedy this, start UrbanTerror with an additional parameter from a terminal emulator:
 $ urbanterror +cl_curllib libcurl.so.4
