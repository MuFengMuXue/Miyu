# Terminator

Terminator is a terminal emulator which supports tabs and multiple resizable terminal panels in one window. It is based on GNOME Terminal.

## Installation
Install the  package.

## Configuration
See  or right click Terminator then click Preferences.

User-specific configurations can be found in .

## GTK customization
Terminator supports tabs. If their size is considered too big, GTK styling can be used in  on 'notebook tab' and 'notebook tab button' to achieve the desired height and/or width.

## Key commands
 Toggle fullscreen

 Split terminals horizontally

 Split terminals vertically

 Close current Panel

 Open new tab

 Move to the terminal above the current one

 Move to the terminal below the current one

 Move to the terminal left of the current one

 Move to the terminal right of the current one

## Managing profiles
It is possible to start terminator with a random profile every time. To avoid unexpected behavior, you should start with a clean  section. You can copy the one from this file. It contains many well-known color schemes. Copy its contents to your  file, which is located in . Then,  your list of profiles to a destination of your choice.

 $ sed -n -e '/background_color/{x;1!s/.*\-e h $HOME/.config/terminator/config > $HOME/.config/terminator/profiles

When you add more profiles in the future and would like to have them included in the startup pool, you will have to reissue the command above. You can create an alias.

You must now modify Terminator's desktop file so that it selects a random profile from this list at startup.

 $ cp /usr/share/applications/terminator.desktop ~/.local/share/applications

Find the  line and comment it out with . Add your own  line as follows.

Save the file and restart your desktop environment.
