# Rofi

Rofi is a window switcher, run dialog, ssh-launcher and dmenu replacement that started as a clone of simpleswitcher, written by Sean Pringle and later expanded by Dave Davenport.

## Installation
Install the  package.

## Configuration
To know more about rofi and its usage read the  man page.

There are two methods of setting configuration options:

* Local configuration. Normally, depending on XDG, in .
* Command line options:

 $ rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi

can be expressed in a configuration file like this:

 configuration {
  modi: "window,drun,ssh,combi";
  font: "hack 10";
  combi-modi: "window,drun,ssh";
  }
 @theme "solarized"

To get a full list of options for  file run . You can write the output of the command directly to your configuration file while running

## Icons
It is possible to use icons to display with their corresponding entries. Assuming you have  installed, with  and defining the icon theme with , you can have rofi display icons and do the following:

 $ rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi -icon-theme "Papirus" -show-icons

## Custom themes
You can preview and apply themes for rofi with

 $ rofi-theme-selector

The  man page contains extensive instructions on how to theme rofi, using a custom, CSS-like language. This page contains additional informations on the layout system used by rofi, the precise syntax used to theme rofi, as well as additional instructions to theme most of rofi's properties. Rofi's theme system can be simple (the default dmenu theme is around 30 lines of CSS) but is flexible enough to create various interactive, widget-like applets and menus, like rofi-advanced.

## Contributed themes
Rofi comes with several official themes stored in , and more user themes can be found at the rofi-themes repository.

Load up an official theme, or download a .rasi user theme and place it in  on the command line:

 $ rofi options -theme example

Alternatively, in your configuration file outside of the {{ic|configuration { }}} block:

 @theme "example"

## Tips and tricks
## Rofi as dmenu replacement
If called as dmenu (via a symlink), rofi acts like dmenu. Then, programs that call dmenu from a script (like passmenu from pass) will use rofi instead of dmenu. The exact behavior of  in dmenu mode is described in .

To approximate the look of dmenu, copy the file  shipped by default in the  package to the rofi configuration directory (usually ) and enable it by appending  at the end of  or with the  option on the command line.

## Execute shell commands from rofi
If you want the ability to run shell commands or use your own scripts directly from rofi with seeing the output, then ensure following:

Define {{ic|-run-shell-command '{terminal} -e SHELL -ic "{cmd} && read"}} where  is your shell (e.g. bash, zsh). This allows you to enter the command on the inputbar followed by . The terminal stays open until the next keypress.

This is an example with the recommended escaping sequence for i3:

 bindsym $mod+d exec --no-startup-id rofi -show drun -run-shell-command '{terminal} -e zsh -ic "{cmd} && read"'

## Unicode selection integration
Install  for a Unicode emoji/character picker integrated with rofi. See the project's README for usage and configuration.

## Emoji selection menu
Install  for an emoji picker integrated with rofi. See the project's README for the usage.

If you encounter rendering issues regarding emojis (rendering as rectangles for example), you should install , , and/or .

## Rofi as a power management menu
Rofi can be used to perform power management operation with systemd. Install . The AUR package will insert the rofi-power-menu script into $PATH by default so all that is needed to use it is:

 $ rofi -show p -modi p:rofi-power-menu

If you decide to not use the AUR package and clone it manually then you will have to tell rofi where to find rofi-power-menu executable. For example, if the executable is in :

 $ rofi -show p -modi p:$HOME/.rofi-power-menu

You can also put the executable in the PATH, and pass only its name.

To show default symbols, you may need to install .

For more information, read the README file in the repository.

## Rofi as a Clipboard Manager
Rofi can be used as a X11 clipboard manager using Greenclip or . For Greenclip install the  package. For Wayland,  is a good alternative.

## Rofi as a calculator
Rofi can be used as a calculator with natural language input, unit conversions, and currency conversions using the  package.
