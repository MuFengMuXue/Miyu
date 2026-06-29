# Cagebreak

Cagebreak is a manually tiling compositor for Wayland, based on  and inspired by ratpoison, which is easily controlled through the keyboard and a UNIX domain socket.

## Installation
Install  or .
Alternatively, download the release tarball or clone the repository.

## Optional dependencies
*  for copy/paste capabilities
*  for allowing Xorg applications to run under cagebreak

## Configuration
The general configuration for cagebreak is located in . This defaults to .

Read  for detailed information. Note that you can also add configuration by using #Interaction through socket.

An example configuration file may be found on GitHub.

## Usage
Start cagebreak like any other binary.

## Getting started
The following is an example of how to install and use cagebreak with the configuration file provided on GitHub.

# Follow #Installation.
# Copy the example configuration from GitHub to . Documentation is provided in .
# Install  or replace  with your preferred terminal emulator in the configuration file.
# Run  or autostart it to run cagebreak on login (see #Keyboard layout for details).
# Cagebreak should start up and display the terminal emulator you specified above. Press   to open a new terminal or   to split the screen. You can also use  to switch to the workspace . For a full list of available keybindings, read the configuration file and .
# If you wish, you may also interact with cagebreak using the UNIX domain socket. See #Interaction through socket for further information.
# Also, please file any bugs you may find:
#* GitHub issue tracker or via email as per the SECURITY.md for cagebreak
#* AUR comments for the  and  PKGBUILDs

## Keyboard layout
Set the environment variable  to the desired keyboard layout. See  for further information.

## Interaction through socket
If cagebreak is invoked with the -e option, cagebreak opens a UNIX domain socket through which interaction with the compositor is possible
at run-time. The path to this socket is stored in the  environment variable.
For example,  may be invoked with:

 $ nc -U $CAGEBREAK_SOCKET

to send cagebreak any configuration while it is running. The syntax is identical to the syntax of the configuration file.

Add the --bs (bad security) option, if you want to see the names of views over the socket (please consider the security implications on your local system).
