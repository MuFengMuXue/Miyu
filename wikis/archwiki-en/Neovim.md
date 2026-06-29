# Neovim

Neovim is a fork of Vim aiming to improve the codebase, allowing for easier implementation of APIs, improved user experience and plugin implementation. Neovim inspired editors like Helix.

## Installation
Install the  package, or  for the latest development version, which strongly encourages the use of Lua as its main configuration language. To make the system clipboard work with Neovim, you may need to install  (X11) or  (Wayland).

It is also possible to install one of many GUIs and other related projects:

*
*
*
*
*
*
*

## Configuration
Nvim stores configuration, data, and logs in standard locations conforming with the XDG Base Directory specification. Plugins are encouraged but not required to follow this convention.

Nvim's user-level configuration file is named  or . Only one can be used and must be located in the  directory. See the Lua guide for an introduction to the use of Lua in Nvim. When the system-wide configuration file does not exist, Nvim checks for , which is not intended to be edited by users.By default, the former global configuration file does not exist. If you create the former file, you may wish to have it source the latter if you still want the functionality it provides, which is allowing pacman-installed vim packages to work with Nvim.

Nvim is compatible with most of Vim's options. Options specific to Nvim can be found in Nvim's documentation, either [https://neovim.io/doc/user/options/ online or by running  in Nvim.

## Migrating from Vim
If you wish to migrate your existing Vim configuration to Nvim, simply copy your  to . If applicable, copy the contents of  to .

## Shared configuration between Vim and Nvim
Neovim uses  instead of  as its main configuration directory and  instead of  as its main configuration file.

If you wish to continue using Vim and wish to source your existing Vim configuration in Nvim, see nvim-from-vim or the  neovim command.

## Loading plugins
Vim/Nvim plugins installed from official repositories or AUR get automatically sourced by , so there is no need to take any extra steps. A vast amount of plugins can be found on both places, but the most recommended way to add plugins is by using a plugin manager, most commonly used are  which works for both Vim and Nvim, and lazy.nvim which only works on Nvim and is written in Lua. Both of them allow for expressive configurations, ranging from github branch to runtime commands.

Most plugins written for vim work without much effort on Nvim, but not every plugin written for Nvim works for Vim, so if your intention is to ensure a compatible configuration, stick to a traditional  or

## Tips and tricks
## Replacing vi and vim with neovim
Setting  and  environment variables should be sufficient in most cases.

Some applications may hardcode vi or vim as default editor; to use neovim in their place, install .

## Symlinking init.vim to .vimrc
As neovim is mostly compatible with standard vim, you can symlink  to your old  to keep old configuration options:

 $ ln -s ~/.vimrc ~/.config/nvim/init.vim

If you want some lines to be specific to each version, you can use an  block:

## True color support
The  of this project explain how to add 24-bits "True Color" support to your syntax highlighting and how to use a color picker to see how it looks in real-time. Comes with the syntax highlighting of the author (if installed) for C++.

## Lastplace cursor support
If you like to keep your last position of cursor to be saved, lastplace.lua is quite useful. It just needs to be placed in  or in the system-wide directory .

## Language Server Protocol
Neovim contains a built-in Language Server Protocol client and the nvim-lspconfig plugin provides common configurations for it.

See Language Server Protocol for a list of Arch packages.

## Use as a pager
You can use the  command to open manual pages. To open all manual pages with neovim set the  environment variable to .

For other pager support install either the  or the  package and set the  environment variable to .

You can also try page, packaged in .

## Multiple isolated nvim configurations
Several nvim flavors can be installed side by side using the NVIM_APPNAME environment variable. Create a directory in your , e.g.  and put your new nvim configuration into it.

To run nvim using a specified configuration:

* Set the  variable directly in your shell or configuration file with . Now the  command will automatically invoke the foo flavor. To restore the default behavior unset the environment variable with .
* Define an alias, e.g.

## Install LazyVim beside your native nvim configuration
If you would like to install the popular LazyVim flavor beside your native nvim configuration, follow the install instructions. But keep in mind that you do not have to delete or move the following directories of your actual nvim configuration:  , ,  and .

Hence, clone the starter repository to a directory name of your choice in your  path. The commands below are using  as target directory:

 $ git clone https://github.com/LazyVim/starter ~/.config/nvimLazyvim

Do not forget to remove the  directory:

 $ rm -rf ~/.config/nvimLazyvim/.git

To invoke the new flavor use the following command:

 $ NVIM_APPNAME=nvimLazyvim nvim

An alias to shorten typing can be made in your shell startup file by appending following line:

 alias v=' NVIM_APPNAMEnvimLazyvim nvim'

## Troubleshooting
## Cursor is not restored to previous state after exit
If the cursor keeps blinking after exiting neovim, see the solution in the neovim FAQ.

## Tree-sitter parser error after system upgrade
After updating the system, it is advised to sync neovim's packages, e.g , then manually force update parsers by . Removing neovim's cache files in  may fix issues.

## Tree-sitter executable not found
The  package provides only the library. If the tree-sitter executable is needed, install .
