# Badwolf

Badwolf is a minimal, privacy oriented, WebKitGTK browser for Linux and BSD on x86(-64) and arm7&8 running on X11 and Wayland. Badwolf features toggles for JavaScript and image loading, a tabbed browsing experience in a mouse-driven user interface. It has a low memory footprint and small binary size.

## Installation
Install .

## Video streaming
For video streaming to work make sure to install ,  and .

## Configuration
## Interface
The interface can be modified using css located at  for a per-user configuration or in  for a system-wide configuration.
For a list if configurable properties see the gtk manual.

## Extensions
Badwolf does not support JavaScript user extensions, but it does support WebKit extensions such as wyebadblock.

## Keybindings
The default keybings can be changed in the  file. Custom keybinds can also be added that run arbitrary C code.

## config.h
Certain properties can be changed in the  file. Further documentation can be found in the file itself.

## Homepage
The default homepage (for new tabs and fresh browser sessions) can be set in .
