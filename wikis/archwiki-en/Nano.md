# Nano

GNU nano (or nano) is a text editor which aims to introduce a simple interface and intuitive command options to console based text editing. nano supports features including colorized syntax highlighting, DOS/Mac file type conversions, spellchecking and UTF-8 encoding. nano opened with an empty buffer typically occupies a few MiB of resident memory.

## Installation
Install the  package.

## Configuration
The look, feel, and function of nano is typically controlled by way of either command-line arguments, or configuration commands within the file .

A sample configuration file is installed upon program installation and is located at . To customize your nano configuration, first create a local copy at :

 $ mkdir ~/.config/nano
 $ cp /etc/nanorc ~/.config/nano/nanorc

Proceed to establish the nano console environment by setting and/or unsetting commands within  file.

## Syntax highlighting
Nano ships with predefined syntax highlighting rules, defined in  and . To enable them, add the following line to your  or to :

 include "/usr/share/nano/*.nanorc"
 include "/usr/share/nano/extra/*.nanorc"

For syntax highlighting enhancements which replace and expand the defaults, install  or  and, additionally to the above setting, also add:

 include "/usr/share/nano-syntax-highlighting/*.nanorc"

## Forth
See https://paste.xinu.at/wc17YG/ for Forth highlighting.

## PKGBUILD
Save https://paste.xinu.at/4ss/ (similar to Arch's old svntogit server) to  and include it:

 include "/etc/nano/pkgbuild.nanorc"

## Suspension
Suspending (i.e. sending nano to the background) is enabled by default, however the default keybind is changed from  to   and it must be changed if the old behavior is desired. This can be done by checking the  section.

## Usage
Shortcuts can be viewed from inside nano. See the nano online help files via  within nano and the nano Command Manual for complete descriptions and additional support.

See also the cheatsheet for nano.

## Special functions
Keyboard shortcuts representing commonly used functions are listed along the bottom two lines of the nano screen.

They can be toggled by:

*  for  based shortcuts
* '''' (typically ) or  for  based shortcuts

## Tips and tricks
## Replacing vi with nano
To replace vi with nano as the default text editor for commands such as visudo, set the  and  environment variables, for example:

 export VISUAL=nano
 export EDITOR=nano

## Troubleshooting
## Hijacked keybindings
Some window managers have keybindings that conflict with nano, for example . Remove or remap them to e.g  (with  for ,  and ) and restart the window manager.
