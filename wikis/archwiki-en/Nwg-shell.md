# Nwg-shell

The nwg-shell project aims to create a consistent, GTK based user interface for the Sway Wayland Compositor.

It also supports Hyprland since version 0.5.0 https://github.com/nwg-piotr/nwg-shell/releases/tag/v0.5.0.

## Installation
The  components can be installed with the  (meta) package.

The  script (see #Configuration) also expects a web browser, a file manager and a text editor to be installed before being run in order to setup keybindings properly. The suggested ones are ,  and  but other ones can be installed instead.

## Configuration
The  package provides the  script which can be run to interactively generate a default configuration for every  components as well as a custom configuration for .

For Sway, run:

 $ nwg-shell-installer -a

For Sway and Hyprland:

 $ nwg-shell-installer -a -hypr

Alternatively, one can modify each components' configurations and style sheets graphically or by modifying the related files under .

Finally, one can enable the  (so greetd will be started at boot) and set up the  greeter.

## Shell components
The  package provides the following  components:

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
