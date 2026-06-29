# Fzf

fzf is a general-purpose command-line fuzzy finder.

## Installation
Install the  package.

## Configuration
## Shells
Optional fzf keybindings and completion are available for various shells:

*  list files+folders in current directory (e.g., type , press , select a few files using , finally )
*  search history of shell commands
*  fuzzy change directory

## Bash
Source the desired files from your .bashrc:

*
*

From version 0.48 onwards, this can be accomplished with a single line:

*

The original syntax is still supported and useful for user-customized versions of the scripts.

## Zsh
Source the desired files from your .zshrc (after vi-mode, if using that, too):

*
*

From version 0.48 onwards, this can be accomplished with a single line:

*

## fish
For fish, keybindings are in:

*

fish will source this by default but the bindings have to be enabled manually:

fzf completion in fish can be enabled with custom functions:
https://github.com/junegunn/fzf/wiki/Examples-(fish)

## Vim
The basic Vim plugin is already included within the package and installed to Vim's global plugin directory. Thus, you do not need to add anything to your  to be able to use it. It only provides the FZF command, though. There is an additional Vim plugin made by the author of fzf that defines some convenience functions, see https://github.com/junegunn/fzf.vim.

## Arch specific fzf uses
## Pacman
Try this to fuzzy-search through all available packages, with package info shown in a preview window, and then install selected packages:

 $ pacman -Slq | fzf --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S

List all your installed packages, and then remove selected packages:

 $ pacman -Qq | fzf --multi --preview 'pacman -Qi {1}' | xargs -ro sudo pacman -Rns

If you want to add package file list in preview – may be a bit slower updating preview window (make sure you run  with root privileges at least once before invocation to sync the pacman file database):

 $ pacman -Slq | fzf --multi --preview 'cat <(pacman -Si {1}) <(pacman -Fl {1} | awk "{print \$2}")' | xargs -ro sudo pacman -S

## Alternatives
*  – fuzzy finder written in Rust
*   – fuzzy finder/selector
