# PCSX-Reloaded

PCSX-Reloaded, also known as PCSXR, PCSXr or PCSX-r, is a plugin based console emulator built on top of the PSEmu Pro plugin interface, which allows playing Play Station 1 games on a PC.

Being a plugin based emulator allows more configurability, including setting screen resolutions and texture qualities higher than those supported by the original console.

## Installation
The last stable version was released 2015-09-25 and can be installed with the  package. The  package allows the installation of the development version, the latest commit having taken place in 2017.

Notice, however, that if you have a 64 bit machine and you choose to grab one of these versions, PCSXR will be compiled to 64 bit architecture, rendering it incompatible with the vast majority of the plugins, which are 32 bit only. If you intend to use any plugins other than the ones that come with the emulator, you should install the 32 bit package .

Alternatively, an actively developed fork is available with the  package.

## Usage
Upon the first launch PCSXR will create a hidden directory named  into your home directory, where all the configurations, plugins, savedata and the console bios will be stored. Deleting this directory will reset PCSXR's configuration to its original state.

## BIOS
The bios dump must be put into the  directory. PCSXR can also emulate an internal bios, but it is not compatible with all games and presents issues. PCSXR provides an incomplete compatibility list.

## Plugins
PCSXR already comes with a set of plugins that allows to play out-of-the-box, however, if you wish to install plugins for extra video/sound/joystick/configurability you will need to put the respective plugins and their configuration files at the  directory.
Most of the Linux compatible plugins can be found at Pete's Domain.

Be aware that some of the plugins will require  to show their configuration interface.

## Configuration
Configure your Video, Sound, Controllers, CDROM and BIOS by going to Configuration > Plugins & Bios.

## Playing
Run a game from CDROM by clicking File > Run CD or by pressing .

Run a game from an ISO or BIN file by clicking File > Run ISO or by pressing .

Run the Play Station BIOS and manage your memory cards and savedata by clicking File > Run BIOS or by pressing .

## Save states
PCSXR supports save states, which allows you to save your game progress in any moment, regardless of you being in a savepoint or not and without the need of attaching a new memory card.

There are 9 slots available for save states, meaning that for each different game you can have up to nine different states saved.

Save a state by clicking Emulator > Save States and selecting a slot or by pressing   eg.  for slot 1.

Load a state by clicking Emulator > Load States and selecting a state previously saved to a slot or by pressing  eg.  for slot 1.

## Troubleshooting
## wrong ELF class: ELFCLASS32
You installed a 64 bit version of the emulator and is trying to run a 32 bit plugin.
Install the  package.

## cfgPeteXGL2, cfgPeteMesaGL or cfgPeopsOSS not found
This issue happens because the latest Linux version of Pete's plugins do not provide the configuration files with them. To solve the problem go to Pete's GPU Plugins page and find the Linux GPU Configs section, download the configuration files - they will come all together in a .tar.gz file. Fetch the missing ones from the Gzip file and put them on the  folder and the problem will be solved.

## PE.Op.S OSS Audio Driver outputs no sound
OSS is dated, use the SDL Sound 1.1.0 plugin that comes included with the emulator.

## Audio crackling
Disable the system type (NTFS/PAL) auto-detection and manually set it to PAL in Configuration > CPU ... > System Type.

## PCSXR segfaults when launching a game or the BIOS
Segfaults are confirmed to happen in computers that have an Intel HD Graphics 965 installed on them, but the bug is reportedly happening on AMD and NVIDIA powered PC's as well.

Open the file  and change the  property's value from  to  to fix it.

You may also want to investigate the cause of the segfault by examining the Core dump with coredumpctl.

## error while loading shared libraries: libgtk-1.2.so.0
Install .
