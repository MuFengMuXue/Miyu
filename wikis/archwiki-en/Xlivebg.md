# Xlivebg

Xlivebg is a live wallpaper framework, and collection of live wallpapers, for the X window system. It provides all the groundwork necessary for displaying animated graphics with OpenGL on the root window, so that a variety of live wallpapers can be written without having to deal with how to tie everything to the X window system, how to create the OpenGL context itself, or how to present any configurable parameters of the live wallpaper to the user.

## Installation
Install the  package.

## Configuration
The preferred user configuration is at , while a system configuration lives at .

A graphical configuration tool is provided as xlivebg-gui.

## Usage
See Autostarting#On Xorg startup for the details on starting a xlivebg instance automatically.

## Known issues
## Output corrupted or absent when using a compositor
When using a compositor such as xcompmgr, use the  flag to instruct xlivebg to draw to its own desktop window and not the root window.
