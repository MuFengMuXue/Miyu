# spa-acp-tool

The PipeWire ALSA profile debugging utility

# SYNOPSIS

*spa-acp-tool** \[*OPTIONS*\] \[*COMMAND*\]

# DESCRIPTION

Debug tool for exercising the ALSA card profile probing code, without
running PipeWire.

May be used to debug problems where PipeWire has incorrectly
functioning ALSA card profiles.

# OPTIONS

 -h | \--help
Show help

 -v | \--verbose
Increase verbosity by one level

 -c NUMBER | \--card NUMBER
Select which card to probe

 -p | \--properties
Additional properties to pass to ACP, e.g. `key=value ...`.

# COMMANDS

 help | h
Show available commands

 quit | q
Quit

 card ID | c ID
Probe card

 info | i
List card info

 list | l
List all objects

 list-verbose | lv
List all data

 list-profiles [ID] | lpr [ID]
List profiles

 set-profile ID | spr ID
Activate a profile

 list-ports [ID] | lp [ID]
List ports

 set-port ID | sp ID
Activate a port

 list-devices [ID] | ld [ID]
List available devices

 get-volume ID | gv ID
Get volume from device

 set-volume ID VOL | v ID VOL
Set volume on device

 inc-volume ID | v+ ID
Increase volume on device

 dec-volume ID | v- ID
Decrease volume on device

 get-mute ID | gm ID
Get mute state from device

 set-mute ID VAL | sm ID VAL
Set mute on device

 toggle-mute ID  | m ID
Toggle mute on device

# AUTHORS

The PipeWire Developers <$(PACKAGE_BUGREPORT)>;
PipeWire is available from <$(PACKAGE_URL)>

# SEE ALSO

pipewire(1)
