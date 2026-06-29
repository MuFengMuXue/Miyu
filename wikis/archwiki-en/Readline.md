# Readline

Readline is a library by the GNU Project, used by Bash and other CLI programs to edit and interact with the command line. See  for more information.

## Installation
The  package is most likely already installed as a dependency of Bash.

## Editing mode
By default Readline uses Emacs style shortcuts for interacting with command line. However, vi style editing interface is also supported by adding the following to :

Alternatively, to set it only for Bash by adding the following line to :

## Mode indicator in prompt
Vi-style editing has two modes: command and insert. You can display which one is currently active by adding the following option:

This will print a string in your prompt (/ by default) that can be customized with the  and  variables.

## Different cursor shapes for each mode
You can set a different cursor shape for each mode by using "\1 .. \2" escapes:

This will set a block shaped cursor when in command mode and a pipe cursor when in insert mode. Note that you must have the mode indicator enabled for this to work (see #Mode indicator in prompt).

The Virtual Console uses different escape codes, so you should check first which term is being used:

See software cursor for VGA for further details.

## Fast word movement
Xterm supports moving between words with  and  by default. To achieve this effect with other terminal emulators, find the correct terminal codes, and bind them to  and  in .

For example, for urxvt:

Another example for macOS style ( and ) word moving:

## History
The history configuration is split into:

* controlling its operation, which is configured shell-specific, for example see Bash#History customization and
* influencing the interaction, which may be configured via a shell-specific configuration, or its native  configuration applicable for all shells, as explained in the following examples.

Usually, pressing the up arrow key will cause the last command to be shown regardless of the command that has been typed so far. However, users may find it more practical to list only past commands that match the current input.

For example, if the user has typed the following commands:

*
*
*
*

In this situation, when typing  and pressing the up arrow key, current input will be replaced with , the last performed command. If the history search has been enabled, only past commands beginning with  (the current input) will be shown, in this case .

You can enable the history search mode by adding the following lines to  or :

 "\ehistory-search-backward
 "\e[B": history-search-forward

If you are using vi mode, you can add the following lines to the readline configuration file (from [https://bbs.archlinux.org/viewtopic.php?pid=428760#p428760 BBS#54972):

If you chose to add these lines to , it is recommended that you also add the following line at the beginning of this file to avoid strange things like BBS#112537:

 $include /etc/inputrc

Alternatively, one can use reverse-search-history (incremental search) by pressing , which does not search based on previous input but instead jumps backwards in the history buffer as commands are typed in a search term. Pressing  again during this mode will display the previous line in the buffer that matches the current search term, while pressing  (abort) will cancel the search and restore the current input line. So in order to search through all previous  commands, press , type 'mount' and keep pressing  until the desired line is found.

The forward equivalent to this mode is called forward-search-history and is bound to  by default. Beware that most terminals override  to pause, seemingly freeze, the output until  is entered. (This is called XON/XOFF flow control). For activating forward-search-history, either disable flow control by issuing:

 $ stty -ixon

or use a different key in . For example, to use  which is not bound by default:

 "\es": forward-search-history

## Faster completion
When performing tab completion, a single tab attempts to partially complete the current word. If no partial completions are possible, a double tab shows all possible completions.

The double tab can be changed to a single tab by setting:

Or you can set it such that a single tab will perform both steps: partially complete the word and show all possible completions if it is still ambiguous:

## Colorized completion
You can enable coloring of completion of filenames with the  option. You can also color the identical prefix of completion-lists with . For example:

## Macros
Readline also supports binding keys to keyboard macros, for example:

 $ bind '"\ew": "\C-e # macro"'

To keep it permanently, add the part within single quotes to readline's configuration file:

Now type a line and press . Readline will act as though  (end-of-line) had been pressed, appended with ''.

Use any of the existing keybindings within a readline macro, which can be quite useful to automate frequently used idioms. For example, this one makes  append  to the line and run it ( is equivalent to ):

 "\e\C-l": "\C-e | less\C-m"

The next one prefixes the line with  when pressing , confirming any yes/no question the command might ask:

 "\e\C-y": "\C-ayes | \C-m"

This example wraps the line in  and runs it, if  is pressed:

 "\es": "\C-a su -c '\C-e'\C-m"

This example prefixes the line with , if  is pressed. It lets you review the result and will not input the  key.

 "\es": "\C-asudo \C-e"

As a last example, quickly send a command in the background with , discarding all of its output:

 "\e\C-b": "\C-e > /dev/null 2>&1 &\C-m"

Similar to history vi-command macros can also be introduced to vi-command for values without a corresponding command or other macro purposes.

 $if mode=vi
 #vi mode settings
    set keymap vi-command
    # char search has a vi command so f could be defined
    "f": vi-char-search

    # char forward(next) and back(prev) does not have a vi-* command
    # so it can be accessed with a macro
    "zn": ";"
    "zp": ","

 # end vi mode settingss
 $endif

## Disabling control echo
Readline causes the terminal to echo  after  is pressed. For users who wish to disable this, simply add the following to :

 set echo-control-characters off

## Bracketed paste
By default, bracketed paste mode is on. It can be set manually in :

 set enable-bracketed-paste on

This ensures that pasting into Readline inserts the clipboard as single string of characters, instead of inserting characters as if they were entered from the keyboard. This is a safety measure to prevent Readline from automatically modifying and running pasted commands.
