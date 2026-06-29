# Powerline

Powerline is a statusline plugin for Vim, and provides statuslines and prompts for several other applications, including zsh, bash, fish, tmux, IPython, Awesome, i3 and Qtile.

## Installation
Install  and .

## Usage
## Bash
Add the following to your bashrc:

Close and reopen your terminal and it should be working. If not, check the Powerline bash prompt usage instructions to ensure that it has not changed.

## Zsh
Add the following to your zshrc:

## Fish
Add the following to your config.fish:

This will activate the next time you enter Fish.

## Tmux
Add the following to your tmux.conf:

## Vim
Install .

## Detailed usage
For detailed usage instructions, such as configuring your system to use Powerline with other shells, window manager widgets, etc., please refer to the Usage section of the Powerline documentation.

## Customizing
The official Powerline documentation refers to , which for Arch Linux is the following:

 /usr/lib/python3.x/site-packages/powerline

To customize Powerline, copy a default configuration to . Then edit the file to your liking.

Example to customize Powerline for tmux:

 $ mkdir -p ~/.config/powerline/themes/tmux/
 $ cp /usr/lib/python3.x/site-packages/powerline/config_files/themes/tmux/default.json ~/.config/powerline/themes/tmux/default.json

## Tips and tricks
## Alternative installation
## Using python-pip
* Install
* Please refer to the Powerline installation guide for additional python-pip instructions

## Using a vim plugin manager
There are many vim plugin managers available which are able to install and update Powerline, assuming you are using a version of vim with Python support or you install . For example, using , add the following to your  file:

Substitute  with the actual directory, such as , and run the vim-plug command  within vim. This will download Powerline from the Powerline GitHub page to the specified plugin directory and add it to vim.

## Alternative fonts
A reduced set of fonts for the text console are available in .

## Alternative package
There is currently one known alternative to Powerline — Vim-airline. It is a part of  and can be installed separately as . Optionally, install .

## Troubleshooting
## Fonts: glyphs missing
If you installed  but you notice missing glyphs, make sure your locale is set. Restart your session to see the changes.
