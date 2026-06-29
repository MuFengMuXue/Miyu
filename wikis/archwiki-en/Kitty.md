# Kitty

kitty is a scriptable OpenGL based terminal emulator with TrueColor, ligatures support, protocol extensions for keyboard input and image rendering. It also offers tiling capabilities, like GNU Screen or tmux.

## Installation
Install the  package.

## Usage
New tabs and windows can be created and resized through various  shortcuts. Layouts are switchable through  and can be saved/restored.

A full keyboard mode provides distinction between ambiguous keys like  vs . Moreover, new text effects like curly-underline are also available for applications that support it.

## Kittens
kitty has a framework for creating subprograms called kittens. The commands for all kittens are prefixed with , so it is convenient to use them as shell aliases.

## icat
This kitten is based on the kitty graphics protocol. It needs ImageMagick to be installed. To show an image in the terminal:

 $ kitty +kitten icat image.jpg

It can also display animated gifs in the terminal. Instead of an image file, you can pass a directory or an image url. This also works over ssh to display images from a remote server. Several applications such as ranger and  use this protocol for displaying images in the terminal. For more information, see the official documentation

## diff
This kitten requires either git or  to be installed. Optionally, install  for syntax highlighting. To show a diff of two files:

 $ kitty +kitten diff file1 file2

It displays diffs for images as well as text files. This kitten can also be used over ssh. You can pass directories instead of files for a recursive diff. For more information, see the official documentation.

## clipboard
This kitten is used to read and write to the system clipboard and can be used to work with a clipboard even over ssh. To copy stdin to the system clipboard:

 $ echo "Hello" | kitty +kitten clipboard

To output the current clipboard contents to stdout:

 $ kitty +kitten clipboard --get-clipboard

This command will show a permission popup by default. To disable this, edit the clipboard_control option in the configuration file:

For more information, see the official documentation.

## Configuration
kitty stores its configuration in  and the default configuration can be found at . Fonts, colors, cursors and scrollback behaviors can be adjusted. You can see all available options in the official documentation or .

## Tips and tricks
## Single instance mode
This works similar to a daemon mode. When kitty is launched with the  or  option, only one instance of kitty will run. Launching kitty subsequently with the same option will create a new window of the existing kitty instance. This will lower memory usage because of a shared GPU cache and also reduces startup time. You can have multiple groups of kitty instances with  option. See  for more information.

## Troubleshooting
## Terminal issues with SSH
When kitty is used to ssh into a remote that does not have its terminfo, various issues can occur. The solution is normally to copy over the terminfo. Kitty has an ssh kitten to automate exactly this.

 $ kitty +kitten ssh user@host

You may want to set it as an alias for . One way to do that is to detect if the user is using Kitty, and if so, alias the ssh command. To do that, you would append the following line to your  or  file:

If for whatever reason you are unable to install the terminfo on the remote, you can try setting  to something that is more likely to be present. Note that this might disable some of the terminal's features. See OpenSSH#Connecting to a remote without the appropriate terminfo entry.

## Disappearing background color in vim
When using a color scheme with a background color in vim, the background may disappear or flicker while scrolling. To fix this, make sure the environment variable  is still set to , then add this line to your  file:

Related bug reports: Github issue #108, kitty FAQ

## Bitmap fonts not recognized
kitty does not provide support for bitmap fonts, due to its fundamental feature of being able to display fonts at arbitrary font sizes, which bitmap fonts are not suited for; see Github issue #97.
