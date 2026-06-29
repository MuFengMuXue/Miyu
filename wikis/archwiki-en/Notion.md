# Notion

Notion is a tiling, tabbed window manager for X.

## Installation
Install .

## Starting
Run  with xinit.

## With a display manager
To start/select Notion with a display manager, a standard .desktop file can be created in the  directory. An example  file can be found below:

 Entry
 Name=Notion
 Comment=This session logs you into Notion
 Exec=/usr/bin/notion
 TryExec=/usr/bin/notion
 Icon=
 Type=XSession

See the display manager article for more details.

## Usage
You can view Notion's man page during use with the F1 key and pressing the return key, this will tell you the default key bindings for Notion. You can also access the man page for other programs this way by pressing F1, typing in the program's name and pressing return. Besides the manual there is also a getting started tour available for a quick overview of Notion.

## Configuration
Notion can be configured using Lua. To get started, copy  to . For more information, read Configuring and Extending Notion using Lua.
