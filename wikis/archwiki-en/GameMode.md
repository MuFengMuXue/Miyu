# GameMode

GameMode is a daemon and library combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.

## Installation
Install the  package. Since many old games are 32-bit-only, enable the multilib repository and install the  package as well.

Add yourself to the  user group. Without it, the GameMode user daemon will not have rights to change CPU governor or the niceness of processes.

## Configuration
GameMode is configured via the following files, which are read and then merged in the following order:

#  for system-wide configuration;
#  for user-local configuration;
#  for directory-local configuration.

## Renicing
GameMode can optionally adjust the priority of game processes (see ) beyond the regular user lower limit of .

This is controlled by the following configuration option:

Unlike renicing a process with the  command, GameMode uses a positive value then negates it before applying it to the process. For example, a value of  will renice the game process to .

## Overclocking
GameMode can optionally overclock your GPU when it is running, but requires special configuration on part of the user.

Independently of the used GPU, the  and  configuration options must be set appropriately.

## AMD
To alter the performance level of AMD GPUs, overclocking must be manually enabled, and the  configuration option must be set.

## NVIDIA
To alter the performance level of NVIDIA GPUs, overclocking must be manually enabled, and the , , and the  configuration options must be set.

## Usage
## Test configuration
Verify if the settings in the configuration file are working:

 $ gamemoded -t

## Run a single game
To run a game with GameMode start it like this:

 $ gamemoderun ./game

## Use with MangoHud
See MangoHud#Use with GameMode

## Verify that GameMode is running
When you have started your game you can verify that GameMode is running with the command:

 $ gamemoded -s

## Run a single Steam game
To make Steam start a game with GameMode, set its launch command:

 gamemoderun %command% launch options

## Run Steam with GameMode
To avoid having to change launch options for all Steam games, you may launch Steam directly with GameMode:

 $ gamemoderun steam

The downside of this approach is that GameMode will be running for as long as the Steam process is open, instead of only when a game is opened.

## Troubleshooting
## Renicing fails when set to less than -10
By default, GameMode provides PAM limits that allow changing the scheduling priority up to a maximum of . If the  setting in the configuration file is set to an unsupported value, renicing of the process will fail entirely.

You can adjust the requested value or adjust the maximum scheduling priority GameMode can set by editing . The example below configures  as the maximum scheduling priority GameMode can set:
