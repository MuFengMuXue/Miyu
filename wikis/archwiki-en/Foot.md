# Foot

foot is a fast, lightweight and minimalistic Wayland terminal emulator.

## Installation
Install the  package.

Additionally, install the  package for improved terminfo.

## Configuration
foot loads configuration file at  (defaulting to ). A template for the configuration file can be found in ; copy the template to  and uncomment the setting you want to change. Restart foot to apply the new settings.

Manual page  provides detailed information on how to configure foot.

## Colors
You can customize colors by modifying  section.

Themes can be found in . To apply a theme, add an  key under .

## Server (daemon) mode
When run normally, foot starts a new foot process for each window.

foot can  also be run in a server mode. In this mode, one process hosts multiple windows. All Wayland communication, VT parsing and rendering is done in the server process.

New windows are opened by running footclient, which remains running until the terminal window is closed, at which point it exits with the exit value of the client process (typically the shell).

Enable/start the user unit  or the corresponding  for socket activation to start the foot server automatically on login.

## Tips and tricks
## GNOME
## Show borders
Currently, GNOME does not support server side decoration on Wayland. foot running on GNOME will show a plain and flat window. You can configure foot to show borders so that different foot windows can be distinguished more easily.

## terminfo
The standard  package uses ncurses . Installing  allows you to use foots upstream terminfo, which contains additional features primarily beneficial for use with tmux, like application synchronized updates and 24-bit color support.

See foot's wiki entry for more details.

## Troubleshooting
## foot-server is not started after login
The  and  units require , but Sway does not set it automatically. So create a  unit and start it whenever Sway started by following the steps in Sway#Manage Sway-specific daemons with systemd.
