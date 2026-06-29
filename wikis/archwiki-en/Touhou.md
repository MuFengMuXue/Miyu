# Touhou

Touhou Project is the name of a series of danmaku games, also known as bullet-hell shooters.

Bullet-hell shooters is a genre of 2D shooters based on really complex patterns, which are beautiful and interesting to look at, and implies great difficulty, memorizing patterns and fast player reaction.

Touhou Project games are one of the most popular of this genre because—among other things—the in-game world is a giant universe, the music (at least the WAVs in the full version) is spectacular, and—if you have been on the internet for a while—you might stumble upon its curious fanbase, which has produced videos, music, manga (Japanese comics) and even unofficial games.

## Installation
PC-98 games can be played using Linux-native X Neko Project II emulator—install the  package.

The following packages only depend on Wine to run, and Timidity++ to play MIDI music. They install the free trial versions. You can easily replace the trials with the full game if you have it.

These games have been packaged for your convenience:

* Touhou 6: Embodiment of Scarlet Devil —  or
* Touhou 7: Perfect Cherry Blossom —
* Touhou 8: Imperishable Night —

We need help packaging more Touhou games for the Arch User Repository. This is a list of games that have free, downloadable trial editions to build off of:

* Touhou 7.5: Immaterial and Missing Power
* Touhou 9: Phantasmagoria of Flower View
* Touhou 10: Mountain of Faith
* Touhou 10.5: Scarlet Weather Rhapsody
* Touhou 11: Subterranean Animism
* Touhou 12: Undefined Fantastic Object
* Touhou 13: Ten Desires
* Touhou 13.5: Hopeless Masquerade.
* Touhou 14: Double Dealing Character
* Touhou 14.5: Urban Legend in Limbo
* Touhou 15: Legacy of Lunatic Kingdom
* Touhou 15.5: Antinomy of Common Flowers
* Touhou 16: Hidden Star in Four Seasons
* Touhou 17: Wily Beast and Weakest Creature
* Touhou 18: Unconnected Marketeers

## Python engine
Linkmauve has made an experimental Python engine to make the games more portable. See the  and  packages.

## Extra information
## Installing the full version
If you have the full version of either Imperishable Night or Perfect Cherry Blossom, you can place them in your home folder, or you can place them in the overlay so that they will work in the liveCD and also get installed to disk.

# Find the folder with the Touhou game files.
# Set your file manager to see hidden files/folders.
::
# Go to your "Home" folder and find the folders  and/or .
# Paste your game files right over the shortcuts in either  or
# Start your games normally. They will use the full version.

## MIDI Music
If you are using the trial edition, they only include MIDI files. To play them, you will also need to install  along with some soundfonts ().

Now add the following lines to the Timidity++ configuration file:

Remember to start the  user unit before playing.

## Audio in Windows-era games
If you find that you have no audio in any of the Windows era or later games (Touhou 6 and later), make sure to install  and , and recheck your configuration in winecfg. In addition, set the audio in-game to "WAV" mode.

## Steam version
You can find games available on Steam from this list.

## thcrap
The Touhou Community Reliant Automatic Patcher (thcrap) is mainly developed to facilitate self-updating, multilingual translation of the Touhou Project games on Touhou Patch Center, but can theoretically be used for just about any other patch for these games, without going through that site.

The simplest way to launch Touhou games with thcrap is to use thcrap-steam-proton-wrapper script.

* Download your purchased game from Steam.

* Install . For Flatpak version of Steam install  from Flathub instead.
* Change your Touhou game launch options. Right click your Touhou games in your Steam library, then click Properties. Under the General tab, change LAUNCH OPTIONS to
 thcrap_proton -c en.js -- %command%
Checkout the manual to launch Touhou games with other languages.
* First time launching the game, it will ask you to install thcrap.
* After that, it will update thcrap and launch the game. When thcrap window show up, it's recommended you uncheck the Keep the updater running in background in the setting, so Steam could properly shutdown the game when you quit.

## thprac
thprac is a tool for practicing. Add  option will install and launch Touhou game with thprac.
 thcrap_proton -p -c en.js -- %command%

## vpatch
Vsync patch reduces input delay (game responds more quickly when a button is pressed).

* Download the patch from touhouwiki.

* Copy ,  and  to your game directory  (or  for Flatpak version of Steam).

* Open  in the game directory with your favorite text editor. We are going to change windows size. For TH10 the default window is very small. First, set  under  section. If using 4K display, set Width = 2667 and Height = 2000. If using 1080p display set Width = 1280 and Height = 960. Based on this tutorial. To fix the Th10 Marisa B 3.xx power bug, add  to  section.

* Make a backup of original Steam executable . This is for convenience, you can always recover it using verify local data in Steam.

* Replace the  with the one you legally obtained from original disk.

* Change the Steam game launch option to

 thcrap_proton -v -c en.js -- %command%

: the  flag let Steam runs .
