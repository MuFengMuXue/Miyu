# Bash

Bash (Bourne-Again SHell) is a command-line shell/programming language by the GNU Project. Its name alludes to its predecessor, the long-deprecated Bourne shell. Bash can be run on most Unix-like operating systems, including GNU/Linux.

Bash is the default command-line shell on Arch Linux.

## Invocation
Bash behaviour can be altered depending on how it is invoked. Some descriptions of different modes follow.

If Bash is spawned by  in a TTY, by an SSH daemon, or similar means, it is considered a login shell. This mode can also be engaged using the / command line option.

Bash is considered an interactive shell when its standard input, output and error are connected to a terminal (for example, when run in a terminal emulator), and it is not started with the  option or  non-option arguments (for example, ). All interactive shells source  and , while interactive login shells also source  and .

## Configuration files
Bash will attempt to execute a set of startup files depending on how it was invoked. See the Bash Startup Files section of the GNU Bash manual for a complete description.

{| class="wikitable"
! File
! Description
! Login shells (see note)
! Interactive, non-login shells
|-
|
| Sources application settings in  and .
|
|
|-
|
| Per-user, after . If this file does not exist,  and  are checked in that order. The skeleton file  also sources .
|
|
|-
|
| Per-user, after exit of a login shell.
|
|
|-
|
| Depends on the  compilation flag. After exit of a login shell.
|
|
|-
|
| Depends on the  compilation flag. Sources .
|
|
|-
|
| Per-user, after .
|
|
|}

## Shell and environment variables
The behavior of Bash and programs run by it can be influenced by a number of environment variables. Environment variables are used to store useful values such as command search directories, or which browser to use. When a new shell or script is launched it inherits its parent's variables, thus starting with an internal set of shell variables.

These shell variables in Bash can be exported in order to become environment variables:

 VARIABLE=content
 export VARIABLE

or with a shortcut

 export VARIABLE=content

Environment variables are conventionally placed in  or  so that other Bourne-compatible shells can use them.

See Environment variables for more general information.

## Command line
Bash command line is managed by the separate library called Readline. Readline provides emacs and vi styles of shortcuts for interacting with the command line, i.e. moving back and forth on the word basis, deleting words etc. It is also Readline's responsibility to manage history of input commands. Last, but not least, it allows you to create macros.

## Tab completion
Tab completion is the option to auto-complete typed commands by pressing  (enabled by default).

## Single-tab
It may require up to three tab-presses to show all possible completions for a command. To reduce the needed number of tab-presses, see Readline#Faster completion.

## Common programs and options
By default, Bash only tab-completes commands, filenames, and variables.  The package  extends this by adding more specialized tab completions for common commands and their options, which can be enabled by sourcing  (which has been already sourced in Arch's ). With , normal completions (such as   ) will behave differently; however, they can be re-enabled with  (see and [https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html for more detail).

## Customize per-command
By default, Bash only tab-completes file names following a command. You can change it to complete command names using :

or complete command names and file names with :

 complete -cf sudo

See  for more completion options.

## History
## History completion
You can bind the up and down arrow keys to search through Bash's history (see: Readline#History and Readline Init File Syntax):

or to affect all readline programs:

## History customization
The  variable can prevent certain commands from being logged to the history.

To stop logging of consecutive identical commands:

To remove all but the last identical command:

To avoid saving commands that start with a space:

To avoid saving consecutive identical commands, and commands that start with a space:

To remove all but the last identical command, and commands that start with a space:

See  for details.

## Disable history
To disable the bash history only temporarily:

 $ set +o history

The commands entered now are not logged to the .

For example, now you can hash passwords with , or hide GPG usage like
and your secret is not written to disk.

To enable history:

 $ set -o history

To disable all bash history:

... and just to make sure, destroy your old histfile forever:

 $ wipe -i -l2 -x4 -p4 "$HISTFILE"
 $ ln -sv /dev/null "$HISTFILE"

## Mimic Zsh run-help ability
Zsh can invoke the manual for the command preceding the cursor by pressing .
A similar behaviour is obtained in Bash using this Readline bind:

{{hc|~/.bashrc|
run-help() { help "$READLINE_LINE" 2>/dev/null || man "$READLINE_LINE"; }
bind -m vi-insert -x '"\eh": run-help'
bind -m emacs -x     '"\eh": run-help'
}}

This assumes are you using the (default) Emacs editing mode.

## Share bash history across machines
 replaces your existing shell history with an SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronization of your history between machines, via an Atuin server.

Enable bash history timestamps () before syncing. Atuin works well with tools like  and cmd-wrapped to provide an enhanced terminal experience across machines.

## Aliases
alias is a command, which enables a replacement of a word with another string. It is often used for abbreviating a system command, or for adding default arguments to a regularly used command.

Personal aliases can be stored in  or any separate file sourced from . System-wide aliases (which affect all users) belong in . See for example aliases.

For functions, see Bash/Functions.

## Tips and tricks
## Prompt customization
See Bash/Prompt customization.

## Syntax highlighting and autosuggestions
[https://github.com/akinomyoga/ble.sh ble.sh (Bash Line Editor), packed as , is a command line editor written in pure Bash, which is an alternative to GNU Readline. It has many enhanced features like syntax highlighting, autosuggestions, menu-completion, abbreviations, Vim editing mode, and hook functions. Other interesting features include status line, history share, right prompt, transient prompt, and xterm title.

After installing it, source it in an interactive session.

Configurations are explained in depth in the ~/.blerc file and at the wiki. The stable  package is also available.

## Command not found
pkgfile includes a "command not found" hook that will automatically search the official repositories, when entering an unrecognized command.

You need to source the hook to enable it, for example:

Then attempting to run an unavailable command will show the following info:

## Disable Ctrl+z in terminal
You can disable the  feature (pauses/closes your application) by wrapping your command like this:

 #!/bin/bash
 trap "" 20
 adom

Now, when you accidentally press  in  instead of , nothing will happen because  will be ignored.

## Clear the screen after logging out
To clear the screen after logging out on a virtual terminal:

## Auto "cd" when entering just a path
Bash can automatically prepend  when entering just a path in the shell. For example:

But after adding one line into  file:

You get:
 ~$ /etc
 cd /etc
 etc$

## Autojump
 is a python script which allows navigating the file system by searching for strings in a database with the user's most-visited paths.

 is an alternative which has additional features and performance improvements compared to the original  and can serve as a drop-in replacement for autojump.

## Prevent overwrite of files
For the current session, to disallow existing regular files to be overwritten by redirection of shell output:

 $ set -o noclobber

This is identical to .

To make the changes persistent for your user:

To manually overwrite a file while  is set:

 $ echo "output" >| file.txt

## Use directory stack to navigate
 and  can be used to push or pop directories to a stack while switching to them. This can be useful for "replaying" your navigation history.

 ~ pushd /tmp/dir1
 /tmp/dir1 pushd /var/lib
 /var/lib popd
 /tmp/dir1 popd
 ~

See .

## Shell environment detection
See Environment variables#Shell environment detection.

## Troubleshooting
## Line wrap on window resize
When resizing a terminal emulator, Bash may not receive the resize signal. This will cause typed text to not wrap correctly and overlap the prompt. The  shell option checks the window size after each command and, if necessary, updates the values of  and .

## Shell exits even if ignoreeof set
If you have set the  option and you find that repeatedly hitting  causes the shell to exit, it is because this option only allows 10 consecutive invocations of this keybinding (or 10 consecutive EOF characters, to be precise), before exiting the shell.

To allow higher values, you have to use the IGNOREEOF variable.

For example:

 export IGNOREEOF=100

## Checking errors by analyzing scripts
The package  analyzes bash (and other shell) scripts, prints possible errors, and suggests better coding.

There is also the web site shellcheck.net of the same purpose, based on this program.

## Tutorials
* Greg's Wiki
* GregsWiki:BashGuide
* GregsWiki:BashFAQ
* Quote Tutorial

## Community
* An active and friendly IRC channel for Bash

## Examples
* How to change the title of an xterm
