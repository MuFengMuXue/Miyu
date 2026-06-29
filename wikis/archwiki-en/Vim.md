# Vim

Vim is a vi-style terminal text editor. It is an extended version of vi with additional features, including syntax highlighting, a comprehensive help system, native scripting (Vim script), a visual mode for text selection, comparison of files (), and tools with restricted capabilities such as  and .

## Installation
Install one of the following packages:

*  — with Python, Lua, Ruby and Perl interpreters support but without GTK/X support.
*  — which also provides the same as the above vim package with GTK/X support.

## Usage
For a basic overview on how to use Vim, follow the Vim tutorial by running either vimtutor (for the terminal version) or gvimtutor (for the graphical version).

Vim includes a broad help system that can be accessed with the  command. Subjects include commands, configuration options, key bindings, plugins etc. Use the  command (without any subject) for information about the help system and jumping between subjects.

## Configuration
Vims user-specific configuration file is located in the home directory: , and Vim files of current user are located inside . The global configuration file is located at . Global Vim files such as  and  are located inside .

From version 9.1.0327 Vim adopts freedesktop XDG Base Directory Specification: that means, you can now place your configuration files under  so Vim will stop littering your home directory.

For gVim, the user-specific configuration file is located at  and the global configuration file is located at .

## Clipboard
Vim commands such as  or  normally operate with the unnamed register . If the  feature is available and its value includes , then Vim yank, delete, change and put operations which would normally go to the unnamed register will use the clipboard register  instead, which is the  buffer in X.

To change the default register, you can  to use the  register instead. The  clipboard register corresponds to the  buffer in X. It should be noted that the  option can be set to a comma-delimited value. If you , then yank operations will also copy the yanked text to the  register in addition to the  register (however, delete, change and put operations will still only operate on the  register).

For more information, see . There are other values which can be set for the  feature. You can use  to take you to the help topic for the first valid value which can be set for this feature, followed by help for all other valid values.

## Syntax highlighting
To enable syntax highlighting for many programming languages:

 :filetype plugin on
 :syntax on

## Indentation
The indent file for specific file types can be loaded with:

 :filetype indent on

## Visual wrapping
The  option is on by default, which instructs Vim to wrap lines longer than the width of the window, so that the rest of the line is displayed on the next line. The  option only affects how text is displayed, the text itself is not modified.

The wrapping normally occurs after the last character that fits the window, even when it is in the middle of a word. More intelligent wrapping can be controlled with the  option. When it is enabled with , the wrapping occurs after characters listed in the  string option, which by default contains a space and some punctuation marks (see ).

Wrapped lines are normally displayed at the beginning of the next line, regardless of any indentation. The breakindent option instructs Vim to take indentation into account when wrapping long lines, so that the wrapped lines keep the same indentation of the previously displayed line. The behaviour of  can be fine-tuned with the  option, for example to shift the wrapped line another four spaces to the right for Python files (see  for details):

 autocmd FileType python set breakindentopt=shift:4

## Using the mouse
Vim has the ability to make use of the mouse, but it only works for certain terminals:

* xterm/urxvt-based terminal emulators
* Linux console with  (see Console mouse support for details)
* PuTTY

To enable this feature, add this line into :

 set mouse=a

The  option is set in .

## Traverse line breaks with arrow keys
By default, pressing  at the beginning of a line, or pressing  at the end of a line, will not let the cursor traverse to the previous, or following, line.

The default behavior can be changed by adding  to your  file.

## Merging files
Vim includes a diff editor (a program that shows differences between two or more files and aids to conveniently merge them). Use vimdiff to run the diff editor — just specify some couple of files to it: . Here is the list of vimdiff-specific commands.

{| class="wikitable"
! Action          !! Shortcut
|-
| next change     ||
|-
| previous change ||
|-
| diff obtain     ||
|-
| diff put        ||
|-
| fold open       ||
|-
| fold close      ||
|-
| rescan files    ||
|}

## Tips and tricks
## Line numbers
To show the line number column, use . By default absolute line numbers are shown, relative numbers can be enabled with . Setting both enables hybrid line numbers—the current line is absolute, while the others are relative.

Jumping to a specific line is possible with  or . Jumps are remembered in a jump list, see  for details.

## Spell checking
Vim has the ability to do spell checking, enable by entering:

 set spell

By default, only English language dictionaries are installed (in ). More dictionaries can be found in the official repositories by searching for . Additional dictionaries can be put in the folder  and enabled with the command:  (replacing the  with the name of the needed dictionary).

{| class="wikitable"
! Action                      !! Shortcut
|-
| next spelling               ||
|-
| previous spelling           ||
|-
| spelling suggestions        ||
|-
| spelling good, add          ||
|-
| spelling good, session      ||
|-
| spelling wrong, add         ||
|-
| spelling wrong, session     ||
|-
| spelling repeat all in file ||
|}

## Saving runtime state
Normally, exiting  discards all unessential information such as opened files, command line history, yanked text etc. Preserving this information can be configured in the following ways.

## viminfo files
The  file may also be used to store command line history, search string history, input-line history, registers' content, marks for files, location marks within files, last search/substitute pattern (to be used in search mode with  and  within the session), buffer list, and any global variables you may have defined. For the  modality to be available, the version of  you installed must have been compiled with the  feature.

Configure what is kept in your  file, by adding (for example) the following to your  file:

 set viminfo='10, cscope.files

Create database files that cscope will read:

 $ cscope -bq

Default keyboard shortcuts:

  Ctrl-\ and
       c: Find functions calling this function
       d: Find functions called by this function
       e: Find this egrep pattern
       f: Find this file
       g: Find this definition
       i: Find files #including this file
       s: Find this C symbol
       t: Find assignments to

Feel free to change the shortcuts.

 #Maps ctrl-c to find functions calling the function
 nnoremap  :cs find c =expand("")

## Taglist
Taglist provides an overview of the structure of source code files and allows you to efficiently browse through source code files in different programming languages.

Install the  package.

Useful options to be put in :

 let Tlist_Compact_Format = 1
 let Tlist_GainFocus_On_ToggleOpen = 1
 let Tlist_Close_On_Select = 1
 nnoremap  :TlistToggle

## Troubleshooting
## gVim is slow
Vims GTK 3 GUI may be slower than the GTK 2 version (see ).  can be installed as a workaround.

## gVim does not launch under Wayland
By default, gVim will try to search for an X11 display and resort to terminal if unable to find one. To use it under Wayland-only environments, add the  environment variable.

## Bidirectional support
Vim still lacks full bidirectional support, and this varies depending on the terminal.

Use  to force text alignment using. It can be assigned to a keybind using:

 inoremap  :silent if &rl  set rl!  else  set rl  endif

Vim has its own letter shaping functionality. Despite some rendering issues, this works on terminals with no letter shaping support like alacritty and st. The shaping depends on Arabic Presentation Forms-B (U+FE70–FEFF), so make sure your font includes support for these characters. As there is no known monospace font with full support for these characters, you need to have an additional fallback font (e.g:  with fallback to ). See St#Arabic shaping support for example terminal fonts setup.

However, if the terminal supports letter shaping like gnome-terminal and other libvte-based terminals, then Vim and the terminal letter shaping could conflict, resulting in mangled Arabic text. Currently, Vim doesn't detect if the terminal has letter-shaping capabilities or not. So the workaround is to manually tell Vim to leave letter-shaping up to the terminal by . Note that will cause reversed text when  because of a limitation. See :set arabic for more info.

## Official
* Homepage
* Documentation
* Vim Wiki
* Vim Scripts

## Tutorials
* vim Tutorial and Primer
* vi Tutorial and Reference Guide
* Graphical vi-Vim Cheat Sheet and Tutorial
* Vim Introduction and Tutorial
* Open Vim — collection of Vim learning tools
* Learn Vim Progressively
* Learning Vim in 2014
* Seven habits of effective text editing

## Videos
* Vimcasts — screencasts in .ogg format.
* Vim Tutorial Videos — covering the basics up to advanced topics.

## Cheat sheets
* https://devhints.io/vim
* https://vim.rtorr.com/ - A mobile friendly Vim cheat sheet - Sources

## Games
* Vim Adventures
* VimGolf

## Configuration
* nion's
* A detailed configuration from Amir Salihefendic
* Bart Trojanowski
* Steve Francia's Vim Distribution
* Vim Awesome - Vim Plugins
* W4RH4WK's Vim configuration
* Fast vimrc/colorscheme from askapache
* Basic vimrc

## Colors
* Vivify
* Vim colorscheme customization
