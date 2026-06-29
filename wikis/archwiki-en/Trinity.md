# Trinity

From the Trinity Desktop Environment (TDE) project page:

:TDE is a complete software desktop environment designed for Unix-like operating systems, intended for computer users preferring a traditional desktop model, and is free/libre software. Born as a fork of KDE 3.5 back in 2010, TDE is now a fully independent project with its own personality and development team, available for various Linux distributions, BSD and DilOS.

TDE depends on End of Life libraries like Qt 3, which they maintain themselves.

The Trinity applications and applets should also work with other desktop environments.

## Installation
## Binary packages
Install either the tde-tdebase package from the trinity repository for a base Trinity environment, or tde-meta for a more complete one.

If you have any errors during an upgrade, add the  key by following pacman/Package signing#Adding unofficial keys.

## Build from source
Trinity Packaging repository contains  files for most Trinity packages in the  folder.

The sources are in a git repository. More info on cloning it is at their GIT information page.

The suggested build order is specified in the How to Build TDE page.

See also DeveloperWiki:Building in a clean chroot.

## Starting
## Manually
To start Trinity from the Linux console:

 $ startx /opt/trinity/bin/starttde

See xinit for more.

## Graphically
tde-tdebase comes with TDE Display Manager. To start it at boot, enable the .

## Tips and tricks
## Trinity "Kicker" panel with other desktop environments
To use the Trinity "kicker" Desktop Panel and Applets with another desktop environment, create this script and make it executable. For Plasma5, use System Settings > Startup and Shutdown > Autostart > Add Script.

 #!/bin/bash
 /opt/trinity/bin/tdeinit
 /opt/trinity/bin/kicker
 /opt/trinity/bin/tdebuildsycoca --noincremental

## Troubleshooting
## TDE Display Manager
If you encounter any issues, the  may have to be manually configured. See Display manager#Loading the display manager for resolution.
