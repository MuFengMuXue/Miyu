# Archinstall

archinstall (upstream repository) is a helper library which automates the installation of Arch Linux. It is packaged with different pre-configured installers, such as a "guided" installer.

This document does not discuss use of archinstall as a Python library; see the official documentation for that.

## Running the installer
First, acquire and boot the live medium as described in Installation guide#Pre-installation.

The  package is part of the live medium and can be run directly:

 # archinstall

The guided installer will perform or ask user input for multiple steps, described in the official documentation.

Additional packages can be installed by specifying them after the Write additional packages to install prompt.

Once the installation is complete, green text should appear saying that it is safe to reboot, which is also the command you use to reboot.

## Profiles
archinstall includes profiles, or sets of packages and pre-configured options which can be installed next to the base system.
