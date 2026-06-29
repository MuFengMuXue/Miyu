# Cutefish

Cutefish is a Desktop Environment written originally for the CutefishOS project that has a focus on simplicity, beauty, and practicality. It is written using the Qt5 framework to provide a simple, universal look and feel.

## Installation
Cutefish can be installed with .

## Starting
Cutefish can either be started with a display manager or manually from the console. The display manager included with Cutefish is SDDM.

## Graphically
Enable .

## Manually
The  can be called from your xinitrc or directly on the startx command line.

## Configuration
Cutefish configuration can be done mainly in the settings application pinned on the dock.

## Keybindings
Cutefish does not natively support keybindings, but using the sxhkd daemon we can add custom keybindings.

It can be started through a custom session:

## Terminal colorscheme
Cutefish Terminal does not natively have a built-in color scheme switcher. We can however edit the source code
to include our own colorscheme.

Start with retrieving the PKGBUILD for  with the ABS.

Edit the theme, either in the building step or manually, which is either  or  in .

To avoid repeating this step at every update, it would be prudent to create a patch to reuse it afterwards.
