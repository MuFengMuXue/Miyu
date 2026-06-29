# Termite

Termite is a minimal VTE-based terminal emulator. It is a modal application, similar to Vim, with an insert mode and selection mode where keybindings have different functions.

The configuration file allows changing colors and setting options. Termite supports transparency along with both the 256 color and true color (16 million colors) palettes. It has a similar look and feel to urxvt.

## Installation
Install the  package.

## Usage
Termite starts in insert mode by default. Text may be selected using the mouse, or by using selection-mode keys. In insert mode,  is used to copy selected text to the X clipboard,  to paste.  starts scrollback completion, and  /  scroll the screen up or down.

 enters selection-mode, similar to vim's normal-mode. Many commands are borrowed from Vim, for example  for visual mode,  for visual line mode,  for visual block mode,  to copy ("yank") selected text,  and  for searching, , , ,  for movement, and  to go back to insert mode.

## Configuration
Termite looks for configuration files in  , ,  and . The configuration file is used to change options such as font, colors, window hints, etc. The configuration file syntax is inspired by XDG Desktop Entry Specification .desktop files (inspired by Microsoft Windows .ini files), with three sections: options, colors, and hints.

To start customizing termite copy the base example file to your home dir first:

 $ cp /etc/xdg/termite/config ~/.config/termite/config

## Font
Fonts are specified in the format  under the options section.  is specified according to fontconfig, not Xft. Use  to see which fonts are available on the system (see also Font configuration#Font paths).

## Colors
Colors consist of either a 24-bit hex value (e.g. ), or an rgba vector (e.g. ). Valid properties for colors are , , , , , , and  (where N is an integer from zero through 254; used to assign a 24-bit color value to terminal colorN).

An amazing collection of termite color schemes can be found here: https://github.com/khamer/base16-termite/tree/master/themes

## Reload configuration without exiting
You can reload Termite's configuration file without exiting by pressing  from within Termite.

Alternatively, you can send a  signal to all Termite instances:

 $ killall -USR1 termite

## Transparency
As of version 9, Termite supports true transparency via color definitions that specify an alpha channel value This requires a compositor to be running, such as picom or . Most compositors do not require special configuration for Termite to use transparency.

## Troubleshooting
## Ctrl+Shift+t
If opening a new tab through  fails with , source . See GNOME/Tips and tricks#New terminals adopt current directory.

If it continues to fail, ensure your hostname is valid. See .

## Remote SSH error
When Termite is using remote SSH connection sometimes the error occurs: Error opening terminal: xterm-termite. or Open terminal failed: missing or unsuitable terminal: xterm-termite.

This error can occur when trying to edit file with vim or nano. To fix this issue you should execute this command on the remote system:

 $ export TERM=xterm-color

Alternatively, follow the instructions on Termite's [https://github.com/aperezdc/termite GitHub. This will allow you to use all of Termite's features when using SSH, whereas the above may not. === Terminal issues with SSH ===

When Termite is used for SSH connections to a remote system which does not have its Terminfo, various issues (such as non-working backspace and weird cursor behaviour) could happen. The solution is to send your Terminfo to the remote host.

On the local host, using Termite:

 $ infocmp > termite.terminfo  # export Termite's Terminfo
 $ scp termite.terminfo user@remote-host:~/  # or any other method to copy to the remote host

On the remote host, in the directory where you copied :

 $ tic -x termite.terminfo  # import Terminfo for current user
 $ rm termite.terminfo  # optional: remove Terminfo file
