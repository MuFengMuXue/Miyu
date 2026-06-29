# Alacritty

Alacritty is a simple, GPU-accelerated terminal emulator written in Rust. It supports scrollback, 24-bit colors, copy/paste, clicking on URLs, and custom key bindings.

## Installation
Install the  package.

## Configuration
Alacritty searches for a configuration file at the following places in this order:

*
*
*
*
*

Versions before 0.13.0 used a YAML configuration file. Old YAML config files can be converted to TOML by running . However, automatic migration drops all comments.

Alacritty does not provide a configuration file by default. Configuration options can be found at the project's homepage. If the  option is enabled (default), most settings will take effect as soon as you save the configuration file.

## Colors
See the alacritty-theme repository for a list of available color schemes. If your preferred color scheme is on the list, you can either:

# paste the theme configuration into your configuration file, or
# install , then add the path to your preferred theme configuration to the  table:

 import = ["/usr/share/alacritty/themes/your_theme.toml"

## Font
If you do not want to use your system’s default font, you can specify a different font by changing the following lines:

Substitute  with a font name from the output of

 $ fc-list : family style

Note that some fonts do not provide an  style but an  style instead.

## Tips and tricks
## Spawn new instance in same directory
Add the following lines to your configuration file to spawn a new instance of Alacritty in the current working directory by pressing :

 bindings = [
    { key = "Return", mods = "Control|Shift", action = "SpawnNewInstance" }

## Vi mode and copy/paste
The vi mode allows moving around Alacritty's viewport and scrollback using the keyboard. By default, you can toggle it using . To copy, you can either use a mouse to select and press , or enter Vi mode, start a selection using , move around with  like in vim, and copy the selection with . To paste, press . To copy/paste to/from X clipboard, you can use a mouse selection to copy and a middle mouse click to paste.

## Hints
Terminal hints can be used to find text or hyperlinks in the visible part of the terminal and pipe it to other applications. By default, Alacritty provides hinting URLs via the  shortcut and opens them with xdg-open. See the  section of Alacritty TOML configuration manual for details.

For example, to make  file hints (e.g. ) clickable and open in Visual Studio Code, one can add the following section to Alacritty's TOML config:

{{hc|alacritty.toml|output=
hints.enabled
regex = "+\\.rs:\\d+:\\d+"
command = { program = "code", args = [ "--goto" ] }
mouse = { enabled = true }
}}

Multiple types of regex-based hints can be added by adding multiple  sections.

## Switch themes on the fly
If you want to switch the theme, for example when connecting to a server over ssh. The following command can be used:
 $ alacritty msg config "$(cat ~/path/to/theme.toml)"

## Troubleshooting
## Mouse not working properly in Vim
Add  and  to your  or switch to Neovim. Also see this issue.

## Transparent border in dwm
With dwm, alacritty's borders become transparent. Adding this line to  in the dwm source directory and recompiling fixes the issue:

 if (!XftColorAllocName(...))
     die("error, cannot allocate color '%s'", clrname); /* Find this line */
 '''dest->pixel |= 0xff  alacritty.terminfo  # export Alacritty's Terminfo
 $ scp alacritty.terminfo user@remote-host:~/  # or any other method to copy to the remote host

On the remote host, in the directory where you copied :

 $ tic -x alacritty.terminfo  # import Terminfo for current user
 $ rm alacritty.terminfo  # optional: remove Terminfo file

Here is a one-liner version of the process above:

 $ infocmp | ssh "$user@$host" 'tic -x /dev/stdin'

Alternatively, one can set the value of  in the configuration to  instead of the default :

## No title bar on Wayland GNOME
When using Wayland GNOME, the title bar is empty and has strange icons. See https://github.com/alacritty/alacritty/issues/4739 for details.

One workaround is to launch Alacritty with Xwayland instead of native Wayland by setting an empty  environment variable.

## Different font size on multiple monitors
By default, Alacritty attempts to scale fonts to the appropriate point size on each monitor based on the . On some setups with multiple displays, this behavior can result in vastly different physical sizes [https://github.com/alacritty/alacritty/issues/1339.

To view the existing device pixel ratio values for each monitor, run , move the child window to each monitor, and pay attention to the reported  in the parent window.

Forcing a constant device pixel ratio using the  environment variable may be sufficient to fix the different font size issue:

 $ WINIT_X11_SCALE_FACTOR=1.66 alacritty

This can also be achieved by setting the value of  in the configuration file:

## Color scheme not recovering what was previously set with pywal
You can add the following code to your shell's run commands ().

 if command -v wal > /dev/null 2>&1 && [ "$TERM" = "alacritty" ]; then
     wal -Rqe
 fi

This is better than simply adding  because

# You only need this to happen in your terminal emulator window.
#  is pretty slow and you don't need to run that in every subshell.
# You don't need to see StdOut, we use the  option.
# We don't need to cause other parts of our desktop to reload colors again as well (i.e. gtk, xrdb, polybar, i3). This is done with the  flag.
