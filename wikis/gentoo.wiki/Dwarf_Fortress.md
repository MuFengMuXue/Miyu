**Resources**

[[]][Home](http://www.bay12games.com/dwarves/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dwarf_Fortress "wikipedia:Dwarf Fortress")

Copied from the [Wikipedia](https://en.wikipedia.org/wiki/Dwarf_Fortress) page on Dwarf Fortress:

\"Dwarf Fortress (officially called Slaves to Armok: God of Blood Chapter II: Dwarf Fortress) is a part construction and management simulation, part roguelike, indie video game created by Tarn and Zach Adams. Freeware and in development since 2002, its first alpha version was released in 2006 and it received attention for being a two-member project surviving solely on donations. The primary game mode is set in a procedurally generated fantasy world in which the player indirectly controls a group of dwarves, and attempts to construct a successful and wealthy underground fortress. Critics praised its complex, emergent gameplay but had mixed reactions to its difficulty. The game influenced Minecraft and was selected among other games to be featured in the Museum of Modern Art to show the history of video gaming in 2012.

The game has text-based graphics and is open-ended with no main objectives. Before being played, the player has to generate worlds with continents, oceans and histories documenting civilizations. The main game mode, Fortress Mode, consists of selecting a suitable site from the generated-world, establishing a successful colony or fortress, combating threats like goblin invasions, generating wealth and taking care of the dwarves. Each dwarf is modeled down to its individual personality, has likes or dislikes and specific trainable skills in various labors. The second main game mode, Adventure Mode, is a turn-based, open-ended roguelike where the player starts off as an adventurer in the world and is free to explore, complete quests, or even visit old abandoned fortresses. The combat system is anatomically detailed with combat logs describing organs getting pierced, fat getting bruised and limbs getting severed.\"

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)

## [Installation]

While Dwarf Fortress can be run directly from the binary on [Bay 12\'s Website](http://www.bay12games.com/dwarves/), it is recommended to install the package using Portage, as this ensures all 32-bit libraries are built and brings the added benefit of a shortcut installed alongside the other programs installed on the system. Using Portage does have a trade-off as the binary on the Gentoo servers tend to be a few versions behind what has been released upstream.

### [Emerge]

To install using Portage, run the command:

`root `[`#`]`emerge --ask games-roguelike/dwarf-fortress`

After the installation has finished before sure add the desired users to the games group:

`root `[`#`]`gpasswd -a <user> games`

### [Additional software]

For Audio output, install OpenAL:

`root `[`#`]`emerge --ask --noreplace media-libs/openal`

## [Configuration]

All configuration files exist in [\~/.dwarf-fortress]