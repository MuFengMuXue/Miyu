# Dwarf Fortress

Dwarf Fortress is a single-player fantasy game. You can control a dwarven outpost or a party of adventurers in a randomly generated, persistent world. It is renowned for its highly customizable, complex in-depth game play.

The game is played mostly with mouse and the version of the game installed by the package is displayed in a terminal-like window with images of ASCII characters (screenshots). There is also a graphical version available on Steam or itch.io.

## Installation
Install the  package.

Alternatively, the AUR has packages of old versions that bundle or add graphics tilesets and/or utilities.

Other bundles, starter packs, tilesets, and mods can be found at the Dwarf Fortress File Depot.

See also the Installation page on the Dwarf Fortress wiki.

## Configuration Files
When first run, Dwarf Fortress that was installed via Pacman creates a folder in the user's home tree, at , to store configuration files, save files, etc.

Some of the directories in  are symlinks to directories in , so changes in  - either directly or through the link - will affect games for all users.

To make changes to Dwarf Fortress files that only affect one user, either delete the links and copy the linked directories from  to , or manually install a copy of Dwarf Fortress to a directory in the user's home directory and make the changes - and run the game from - there (see Manual or multiple installations on the Dwarf Fortress wiki).

## Tools
## DFHack
DFHack is a Dwarf Fortress memory access utility, with many useful scripts and plugins.

There are multiple dfhack packages available in the AUR.

To start Dwarf Fortress with DFHack, execute  instead of , or create a custom desktop entry.

Similarly to the Dwarf Fortress packages, the DFHack packages add files and symlinks to , including  which contains files that can be edited to configure DFHack.

## Manipulator
Manipulator is an in-game alternative to Dwarf Therapist with much of the same functionality, but does not require extra permissions. This plugin is enabled by default in the DFHack, accessible from the units screen.

## quickfort
Quickfort is a DFHack plugin that helps you build fortresses from "blueprint" .CSV, .XLS, and .XLSX files.

## StoneSense
StoneSense is an isometric Dwarf Fortress visualizer, as a plugin included with DFHack.

## Dwarf Therapist
Dwarf Therapist ( or ) is a utility to tune dwarvish behavior (makes micro-management a lot easier). For it to work on current kernels you will need to disable a kernel security feature, since it directly accesses and modifies the memory of a running Dwarf Fortress instance. This setting is called  and is active by default.

Permission to use  can be given to the  executable with:

 # setcap cap_sys_ptrace=eip /usr/bin/dwarftherapist

## SoundSense
SoundSense () adds various sound effects and music by monitoring the gamelog.txt (which for v50+ versions of Dwarf Fortress does not currently contain the information SoundSense needs).
