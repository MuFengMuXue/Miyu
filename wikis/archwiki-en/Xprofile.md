# Xprofile

An xprofile file,  and , allows you to execute commands at the beginning of the X user session - before the window manager is started.

The xprofile file is similar in style to xinitrc.

## Compatibility
The xprofile files are natively sourced by the following display managers:
* GDM -
* LightDM -
* LXDM -
* SDDM -

## Sourcing xprofile from a session started with xinit
It is possible to source xprofile from a session started with one of the following programs:

*
*
* XDM
* Any other Display manager which uses  or

All of these execute, directly or indirectly,  or  if it does not exist. That is why xprofile has to be sourced from these files.

## Configuration
Firstly, create the file  if it does not exist already. Then, simply add the commands for the programs you wish to start with the session. See below:
