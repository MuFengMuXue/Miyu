# FrankenWM

From FrankenWM:

:FrankenWM is a dynamic tiling window manager (comparable to dwm or awesome), featuring the v-stack, b-stack, grid, fibonacci, dualstack, equal and monocle layouts out of the box. If you want to, you can add gaps between the windows as well.

## Installation
Install the  package. Due to the absence of releases since 2020, you may want to try the  package.

## Starting
## From tty
Run  with xinit

## Configuration
Configuration is done at compile time by editing . There are lots of comments in the default configuration () which explain what the settings are doing.

## Usage
The basic usage includes opening a terminal (), opening dmenu () and closing windows (). There is a complete, sorted list of the default keybinds and explanations of the tiling layouts in .

## Panels
FrankenWM does not come with a panel included, but gives you the possibility to leave space either at the top or bottom for one, like conky or dzen. There are a couple of settings in the configuration for this space.

If you want to use FrankenWM's status in your bar, you can pipe FrankenWM to a shell script to parse the output and pipe it to a bar. Sample scripts to accomplish this with a few different bar are located here.

## Troubleshooting
## I do not see anything
This is normal behaviour, as FrankenWM does not come with a bar included or a desktop background, so after running  without anything else, you will probably see a black screen. See Panels above for information on how to add a panel to your desktop. Wallpapers can be set by using software like xsetroot, feh or hsetroot.

## I cannot open a terminal/menu
Have a look at the  used to build your currently running version of FrankenWM, which is located in the build directory. Make sure that both the shortcut to run the / command and the / itself are set properly to start an installed terminal/menu.
