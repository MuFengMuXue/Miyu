# Zsh

Zsh is a powerful shell that operates as both an interactive shell and as a scripting language interpreter. While being compatible with the POSIX sh (not by default, only if issuing ), it offers advantages such as improved tab completion and globbing.

The Zsh FAQ offers more reasons to use Zsh.

## Installation
Before starting, users may want to see what shell is currently being used:

 $ echo $SHELL

Install the  package. For additional completion definitions, install the  package as well.

## Initial configuration
Make sure that Zsh has been installed correctly by running the following in a terminal:

 $ zsh

You should now see zsh-newuser-install, which will walk you through some basic configuration. If you want to skip this, press . If you did not see it, you can invoke it manually with:

 $ autoload -Uz zsh-newuser-install
 $ zsh-newuser-install -f

## Making Zsh your default shell
Change your shell to . See Command-line shell#Changing your default shell.

## Startup/Shutdown files
When starting, Zsh will read commands from the following files in this order by default, provided they exist.

*  Used for setting environment variables for all users; it should not contain commands that produce output or assume the shell is attached to a TTY. When this file exists it will ''always'' be read, this cannot be overridden.
*  Used for setting user's environment variables; it should not contain commands that produce output or assume the shell is attached to a TTY. When this file exists it will ''always'' be read.
*  Used for executing commands at start for all users, will be read when starting as a ''login shell''. Please note that on Arch Linux, by default it contains one line which sources . See warning below before wanting to remove that!
**  This file should be sourced by all POSIX sh-compatible shells upon login: it sets up  and other environment variables and application-specific () settings upon login.
*  Used for executing user's commands at start, will be read when starting as a ''login shell''. Typically used to autostart graphical sessions and to set session-wide environment variables.
*  Used for setting interactive shell configuration and executing commands for all users, will be read when starting as an ''interactive shell''.
*  Used for setting user's interactive shell configuration and executing commands, will be read when starting as an ''interactive shell''.
*  Used for executing commands for all users at ending of initial progress, will be read when starting as a ''login shell''.
*  Used for executing user's commands at ending of initial progress, will be read when starting as a ''login shell''. Typically used to autostart command line utilities. Should not be used to autostart graphical sessions, as at this point the session might contain configuration meant only for an interactive shell.
*  Used for executing commands when a ''login shell exits'''.
*  Used for executing commands for all users when a ''login shell exits'''.

See the graphic representation.

## Configure Zsh
Although Zsh is usable out of the box, it is almost certainly not set up the way most users would like to use it. But due to the sheer amount of customization available in Zsh, configuring Zsh can be a daunting and time-consuming experience. For automatic configuration, see #Third-party extensions.

## Simple .zshrc
Included below is a sample configuration file. It provides a decent set of default options as well as giving examples of many ways that Zsh can be customized. In order to use this configuration save it as a file named .

Here is a simple :

See #Prompt themes for more details about the prompt theme system.

## Configuring $PATH
Zsh ties the  variable to a  array. This allows you to manipulate  by simply modifying the  array. See A User's Guide to the Z-Shell for details.

To add  to the :

## Command completion
Perhaps the most compelling feature of Zsh is its advanced autocompletion abilities. At the very least, enable autocompletion in . To enable autocompletion, add the following to your :

The above configuration includes ssh/scp/sftp hostnames completion but in order for this feature to work, users must not enable ssh's hostname hashing (i.e. option  in ssh client configuration).

For autocompletion with an arrow-key driven interface, add the following to:

To activate the menu, press  twice.

For enabling autocompletion of privileged environments in privileged commands (e.g. if you complete a command starting with sudo, completion scripts will also try to determine your completions with sudo), include:

## Custom completion
You can write custom completions on your own. Should you do so, you can refer to the  man page.

Note that the official documentation can be hard to read. You can consider trying the simpler zsh-completion-howto tutorial for an easy start.

## Key bindings
Zsh does not use readline, instead it uses its own and more powerful Zsh Line Editor (ZLE). It does not read  or . Read A closer look at the zsh line editor and creating custom widgets for an introduction to ZLE configuration.

ZLE has an Emacs mode and a vi mode. If one of the  or  environment variables contain the string  then vi mode will be used; otherwise, it will default to Emacs mode. Set the mode explicitly with  or  respectively for Emacs mode or vi mode. The delay of pressing Esc key in vi mode is 0.4s by default, and you can make it shorter (0.05s) with .

Key bindings are assigned by mapping an escape sequence matching a keypress to a ZLE widget. The available widgets, with descriptions of their actions and their default keybindings, are listed in  and .

The recommended way to set key bindings in Zsh is by using string capabilities from . For example{{hc|~/.zshrc|2=
# create a zkbd compatible hash;
# to add other keys to this hash, see: man 5 terminfo
typeset -g -A key

key[Home="${terminfokey[End="${terminfokey[Insert="${terminfokey[Backspace="${terminfokey[Delete="${terminfokey[Up="${terminfokey[Down="${terminfokey[Left="${terminfokey[Right="${terminfokey[PageUp="${terminfokey[PageDown="${terminfokey[Shift-Tab="${terminfo# setup key accordingly
[[ -n "${key[Home}"      ]] && bindkey -- "${keybeginning-of-line
[[ -n "${key[End}"       ]] && bindkey -- "${keyend-of-line
[[ -n "${key[Insert}"    ]] && bindkey -- "${keyoverwrite-mode
[[ -n "${key[Backspace}" ]] && bindkey -- "${keybackward-delete-char
[[ -n "${key[Delete}"    ]] && bindkey -- "${keydelete-char
[[ -n "${key[Up}"        ]] && bindkey -- "${keyup-line-or-history
[[ -n "${key[Down}"      ]] && bindkey -- "${keydown-line-or-history
[[ -n "${key[Left}"      ]] && bindkey -- "${keybackward-char
[[ -n "${key[Right}"     ]] && bindkey -- "${keyforward-char
[[ -n "${key[PageUp}"    ]] && bindkey -- "${keybeginning-of-buffer-or-history
[[ -n "${key[PageDown}"  ]] && bindkey -- "${keyend-of-buffer-or-history
[[ -n "${key[Shift-Tab}" ]] && bindkey -- "${keyreverse-menu-complete

# Finally, make sure the terminal is in application mode, when zle is
# active. Only then are the values from $terminfo valid.
if (( ${+terminfo[smkx} && ${+terminfo)); then
    autoload -Uz add-zle-hook-widget
    function zle_application_mode_start { echoti smkx }
    function zle_application_mode_stop { echoti rmkx }
    add-zle-hook-widget -Uz zle-line-init zle_application_mode_start
    add-zle-hook-widget -Uz zle-line-finish zle_application_mode_stop
fi
}}

## Shift, Alt, Ctrl and Meta modifiers
xterm-compatible terminals can use extended key-definitions from . Those are combinations of , ,  and  together with , , , , , , ,  or . Refer to the [https://sourceforge.net/p/zsh/code/ci/master/tree/Functions/Misc/zkbd zkbd source for a list of recommended names for the modifier keys and key combinations.

For example, for  to move to the beginning of the previous word and  to move to the beginning of the next word:

{{hc|~/.zshrc|2=
keykey[Control-Right="${terminfo[[ -n "${key[Control-Left}"  ]] && bindkey -- "${keybackward-word
[[ -n "${key[Control-Right}" ]] && bindkey -- "${keyforward-word
}}

## History
To have the history list ignore commands that start with a blank space, issue , either in the command prompt, or in . Though even with , the last command can be repeated, for example by pressing the  key, until another command takes its place as the last command.  to undo a  command.

By default, history will be with  of 30, separate for each terminal, without the ability to delete entries from the list, and not saved between sessions. One of the consequences of setting  is to have the history list saved between sessions.

## History search
You need to set up the  array and make sure that ZLE enters application mode to use the following instructions; see #Key bindings.

To enable history search add these lines to  file:

{{hc|~/.zshrc|
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

[[ -n "${key[Up}"   ]] && bindkey -- "${keyup-line-or-beginning-search
[[ -n "${key[Down}" ]] && bindkey -- "${keydown-line-or-beginning-search
}}

By doing this, only the past commands matching the current line up to the current cursor position will be shown when  or  keys are pressed.

## Prompts
Zsh offers the options of using a prompt theme or, for users who are dissatisfied with the themes (or want to expand their usefulness), the possibility to build a custom prompt.

## Prompt themes
Prompt themes are a quick and easy way to set up a colored prompt in Zsh. See  for information about prompt themes and how to write your own theme.

To use a theme, make sure that prompt theme system is set to autoload in . This can be done by adding these lines to:

Available prompt themes are listed by running the command:

 $ prompt -l

For example, to use the  theme, enter:

 $ prompt walters

To preview all available themes, use this command:

 $ prompt -p

## Manually installing prompt themes
It is possible to install themes manually, without external configuration manager tools. For a local installation, first create a folder and add it to the  array, eg:

 $ mkdir ~/.zprompts
 $ fpath=("$HOME/.zprompts" "$fpath[@")

Now create a symbolic link of your theme file in this folder:

 $ ln -s mytheme.zsh ~/.zprompts/prompt_mytheme_setup

If instead you wish to install a theme globally, do:

 # ln -s mytheme.zsh /usr/share/zsh/functions/Prompts/prompt_mytheme_setup

Now you should be able to activate it using:

 $ prompt mytheme

If everything works, you can edit your  accordingly.

## Adding prompt themes without a separate file for each one
In addition to adding a prompt theme through its own file, it is possible to add themes from within another file (like your ), eg:

{{hc|~/.zshrc|2=
# Load promptinit
autoload -Uz promptinit && promptinit

# Define the theme
prompt_mytheme_setup() {
    PS1="%~%# "
}

# Add the theme to promptsys
prompt_themes+=( mytheme )

# Load the theme
prompt mytheme
}}

## Customized prompt
Additionally to a primary left-sided prompt  (, ) that is common to all shells, Zsh also supports a right-sided prompt  (). These two variables are the ones you will want to set to a custom value.

Other special purpose prompts, such as  (),  (),  (),  (),  () and , are explained in .

All prompts can be customized with prompt escapes. The available prompt escapes are listed in .

## Colors
Zsh sets colors differently than Bash; You do not need to use profuse ANSI escape sequences or terminal capabilities from . Zsh provides convenient prompt escapes to set the foreground color, background color and other visual effects; see  for a list of them and their descriptions.

Colors can be specified using a decimal integer, the name of one of the eight most widely-supported colors or as a # followed by an RGB triplet in hexadecimal format. See the description of fg=colour in  for more details.

Most terminals support the following colors by name:

{| class="wikitable"
|-
! Name !! Number
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|}

Color numbers 0–255 for terminal emulators compatible with xterm 256 colors can be found in the xterm-256color chart.

With a correctly set TERM environment variable, the terminal's supported maximum number of colors can be found from the  database using . In the case of 24-bit colors, also check the COLORTERM environment variable with . If it returns  or  then your terminal supports 16777216 (224) colors even if terminfo shows a smaller number.

{{Tip|
* Prompt escapes can be tested with command , for example: {{bc|$ print -P '%B%F{red}co%F{green}lo%F{blue}rs%f%b'}}
* If you use 24-bit colors, you might want to load the  module in terminals that do not support them. E.g.: {{bc|"$COLORTERM" == (24bit|truecolor) || "${terminfo[colors}" -eq '16777216' ]] || zmodload zsh/nearcolor}} See  for details about the  module.
}}

## Example
An example of a simple colorless prompt:

 PROMPT='%n@%m %~ %# '

How it will be displayed:

username@host ~ %

This is an example of a two-sided prompt with color:

 PROMPT='%F{green}%n%f@%F{magenta}%m%f %F{blue}%B%~%b%f %# '
 RPROMPT='And here is how it will be displayed:

username@host ~ % [0

To use colors from the 16-255 range and 24-bit true color, you can use the number from 0 to 255 assigned to the wanted color and its hexadecimal color code, respectively:

 PROMPT='%F{2}%n%f@%F{5}%m%f %F{4}%B%~%b%f %# '
 RPROMPT='PROMPT='%F{#c0c0c0}%n%f@%F{#008000}%m%f %F{#800080}%B%~%b%f %# '
 RPROMPT='[%F{#0000ff}%?%f'

## Sample .zshrc files
* To get the same setup as the monthly ISO releases (which use Zsh by default), install . It includes the many tweaks and advanced optimizations from grml.
* https://github.com/MrElendig/dotfiles-alice/blob/master/.zshrc - basic setup, with dynamic prompt and window title/hardinfo.

See dotfiles#User repositories for more.

## Tips and tricks
## Autostart X at login
See xinit#Autostart X at login.

## Restore terminal settings after a program exits abnormally
Many programs change the terminal state, and often do not restore terminal settings on exiting abnormally (e.g. when crashing or encountering SIGINT).

This can typically be solved by executing :

 $ reset

The following sections describe ways to avoid the need to manually reset the terminal.

## The ttyctl command
The ttyctl command can be used to "freeze/unfreeze" the terminal. To freeze the interactive shell on launch, use the following:

## Resetting the terminal with escape sequences
Alternate linedrawing character set can screw up the terminal in a way which ttyctl cannot prevent.

A simple solution is to output the escape sequences that reset the terminal from the  hook function, so that they are executed every time before the prompt is drawn. For example, using the escape sequence :

{{hc|~/.zshrc|2=

autoload -Uz add-zsh-hook

function reset_broken_terminal () {
    printf '%b' '\e}

add-zsh-hook -Uz precmd reset_broken_terminal
}}

To test if it works, run:

 $ print '\e(0\e)B'

## Remembering recent directories
## Dirstack
Zsh can be configured to remember the DIRSTACKSIZE last visited folders. This can then be used to cd them very quickly. You need to add some lines to your configuration file:

{{hc|~/.zshrc|
autoload -Uz add-zsh-hook

DIRSTACKFILE="${XDG_CACHE_HOME:-$HOME/.cache}/zsh/dirs"
if  -f "$DIRSTACKFILE"  && (( ${#dirstack} == 0 )); then
    dirstack=("${(@f)"$( "$DIRSTACKFILE"
}
add-zsh-hook -Uz chpwd chpwd_dirstack

DIRSTACKSIZE='20'

setopt AUTO_PUSHD PUSHD_SILENT PUSHD_TO_HOME

## Remove duplicate entries
setopt PUSHD_IGNORE_DUPS

## This reverts the +/- operators.
setopt PUSHD_MINUS
}}

Now use

 $ dirs -v

to print the dirstack. Use  to go back to a visited folder. Use autocompletion after the dash. This proves very handy if using the autocompletion menu.

## cdr
cdr allows you to change the working directory to a previous working directory from an automatically maintained list. It stores all entries in files that are maintained across sessions and (by default) between terminal emulators in the current session.

See  for setup instructions.

## zoxide
 is a smarter cd command that lets you navigate anywhere in just a few keystrokes. It remembers your frequently used directories and uses a scoring mechanism to guess where you want to go.

See [https://github.com/ajeetdsouza/zoxide or  for more details.

## Help command
Unlike Bash, Zsh does not enable a built in  command, instead it provides . By default  is an alias to , it can be either executed manually by prepending it to a command or it can be invoked for the currently typed command with the keyboard shortcuts  or  .

Since by default it is just an alias to man, it will only work on external commands. To improve its functionality, so that it works on shell builtins and other shell features, you need to use the  function. See  for more information on the  and its assistant functions.

First load the  function and then remove the existing  alias. For convenience  can be aliased to . For example, add following to your :

 autoload -Uz run-help
 (( ${+aliases)) && unalias run-help
 alias help=run-help

Assistant functions have to be enabled separately:

 autoload -Uz run-help-git run-help-ip run-help-openssl run-help-p4 run-help-sudo run-help-svk run-help-svn

For example,  command will now open the man page  instead of .

## Persistent rehash
Typically,  from  will not automatically find new executables in the . For example, after you install a new package, the files in  would not be immediately or automatically included in the completion. Thus, to have these new executables included, one would run:

 $ rehash

This 'rehash' can be set to happen automatically.[https://github.com/robbyrussell/oh-my-zsh/issues/3440 Simply include the following in your :

## On-demand rehash
As above, however pacman can be configured with hooks to automatically request a , which does not incur the performance penalty of constant rehashing as above. To enable this, create the  directory, and a  directory, then create a hook file:

This keeps the modification date of the file  consistent with the last time a package was installed, upgraded or removed. Then,  must be coaxed into rehashing its own command cache when it goes out of date, by adding to your :

{{hc|~/.zshrc|
zshcache_time="$(date +%s%N)"

autoload -Uz add-zsh-hook

rehash_precmd() {
    if  -a /var/cache/zsh/pacman ; then
        local paccache_time="$(date -r /var/cache/zsh/pacman +%s%N)"
        if (( zshcache_time < paccache_time )); then
            rehash
            zshcache_time="$paccache_time"
        fi
    fi
}

add-zsh-hook -Uz precmd rehash_precmd
}}

If the  hook is triggered before  is updated, completion may not work until a new prompt is initiated. Running an empty command, e.g. pressing , should be sufficient.

## Alternative on-demand rehash using SIGUSR1
As above, however the hook file looks like this:

{{hc|~/.zshrc|
TRAPUSR1() { rehash }
}}

The function trap above can be replaced with a list trap . See  for differences between types of traps.

This method will instantly  all  instances, removing the need to press enter to trigger .

## Bind key to ncurses application
Bind a ncurses application to a keystroke, but it will not accept interaction. Use  variable to make it work. The following example lets users open ncmpcpp using :

{{hc|~/.zshrc|2=
ncmpcppShow() {
    BUFFER="ncmpcpp"
    zle accept-line
}
zle -N ncmpcppShow
bindkey '^ncmpcppShow
}}

An alternate method, that will keep everything you entered in the line before calling application:

{{hc|~/.zshrc|2=
ncmpcppShow() {
    ncmpcpp <$TTY
    zle redisplay
}
zle -N ncmpcppShow
bindkey '^[\' ncmpcppShow
}}

## File manager key binds
Key binds like those used in graphic file managers may come handy. The first comes back in directory history (), the second let the user go to the parent directory (). They also display the directory content.

{{hc|~/.zshrc|
cdUndoKey() {
    popd
    zle       reset-prompt
    print
    ls
    zle       reset-prompt
}

cdParentKey() {
    pushd ..
    zle      reset-prompt
    print
    ls
    zle       reset-prompt
}

zle -N                 cdParentKey
zle -N                 cdUndoKey
bindkey '^[[1;3A'      cdParentKey
bindkey '^[[1;3D'      cdUndoKey
}}

## xterm title
If your terminal emulator supports it, you can set its title from Zsh. This allows dynamically changing the title to display relevant information about the shell state, for example showing the user name and current directory or the currently executing command.

The xterm title is set with the [https://www.tldp.org/HOWTO/Xterm-Title-3.html#ss3.1 xterm control sequence operating system command  or . For example:

 $ print -n '\e]2;My xterm title\a'

will set the title to

 My xterm title

A simple way to have a dynamic title is to set the title in the  and  hook functions. See  for a list of available hook functions and their descriptions.

By using  you can additionally take advantage of Zsh's prompt escapes.

{{hc|~/.zshrc|
autoload -Uz add-zsh-hook

function xterm_title_precmd () {
    print -Pn -- '\e]2;%n@%m %~\a'
     "$TERM" == 'screen'*  && print -Pn -- '\e_\005{2}%n\005{-}@\005{5}%m\005{-} \005{+b 4}%~\005{-}\e\\'
}

function xterm_title_preexec () {
    print -Pn -- '\e]2;%n@%m %~ %# ' && print -n -- "${(q)1}\a"
     "$TERM" == 'screen'*  && { print -Pn -- '\e_\005{2}%n\005{-}@\005{5}%m\005{-} \005{+b 4}%~\005{-} %# ' && print -n -- "${(q)1}\e\\"; }
}

if alacritty*|aterm*|foot*|gnome*|konsole*|kterm*|putty*|rxvt*|screen*|wezterm*|tmux*|xterm*) ; then
    add-zsh-hook -Uz precmd xterm_title_precmd
    add-zsh-hook -Uz preexec xterm_title_preexec
fi
}}

## Terminal emulator tab title
Some terminal emulators and multiplexers support setting the title of the tab. The escape sequences depend on the terminal:

{| class="wikitable sortable"
! Terminal
! Escape sequences
! Description
|-
! GNU Screen
|
| Screen's window title ().
|-
! Konsole
|
| Konsole's tab title.
|}

## Shell environment detection
See Environment variables#Shell environment detection.

## /dev/tcp equivalent: ztcp
Use the  module:

 $ zmodload zsh/net/tcp

You can now establish TCP connections:

 $ ztcp example.com 80

More details are available in  and .

## Shortcut to exit shell on partial command line
By default,  will not close your shell if the command line is filled, this fixes it:

{{hc|.zshrc|
exit_zsh() { exit }
zle -N exit_zsh
bindkey '^D' exit_zsh
}}

## pacman -F "command not found" handler
pacman includes functionality to search for packages containing a file. The following command-not-found handler will use pacman directly to search for matching packages when an unknown command is executed.

{{hc|1=~/.zshrc|2=
...
function command_not_found_handler {
    local purple='\ebright='\e[0;1m' green='\e[1;32m' reset='\e[0m'
    printf 'zsh: command not found: %s\n' "$1"
    local entries=(
        ${(f)"$(/usr/bin/pacman -F --machinereadable -- "/usr/bin/$1")"}
    )
    if (( ${#entries[@} ))
    then
        printf "${bright}$1${reset} may be found in the following packages:\n"
        local pkg
        for entry in "${entriesdo
            # (repo package version file)
            local fields=(
                ${(0)entry}
            )
            if [[ "$pkg" != "${fields[2}" ]]
            then
                printf "${purple}%s/${bright}%s ${green}%s${reset}\n" "${fields"${fields[2}" "${fieldsfi
            printf '    /%s\n' "${fields[4}"
            pkg="${fieldsdone
    fi
    return 127
}
...
}}

For an alternative using pkgfile, see #pkgfile "command not found" handler.

## Clear the backbuffer using a key binding
By default, the clear screen keybinding will not clear the backbuffer (the part you need to scroll up for to see it) on most terminal emulators. A possible solution to this problem is the following.

{{hc|~/.zshrc|2=
...
function clear-screen-and-scrollback() {
    printf '\x1Bc'
    zle clear-screen
}

zle -N clear-screen-and-scrollback
bindkey '^L' clear-screen-and-scrollback
...
}}

## Third-party extensions
## Configuration frameworks
*
*
*
*

## Plugin managers
*
*
*
*
*
*
*

## Fish-like syntax highlighting and autosuggestions
Fish provides very powerful shell syntax highlighting and autosuggestions. To use both in Zsh, you can install , , and finally source one or both of the provided scripts from the end of your zshrc, ensuring that  is sourced after  [https://github.com/zsh-users/zsh-syntax-highlighting#why-must-zsh-syntax-highlightingzsh-be-sourced-at-the-end-of-the-zshrc-file:

## pkgfile "command not found" handler
pkgfile includes a Zsh script file that provides a  function that will automatically search the pkgfile database when entering an unrecognized command.

You need to source the script to enable it. For example:

For an alternative using pacman's native functionality, see #pacman -F "command not found" handler.

## Troubleshooting
## IOT instruction
 message just means that an application exited with signal 6 (SIGABRT, Signal Abort). The patch is already in upstream (i.e. you can use ) and it will be applied in 5.10. For more information, see [https://zsh.org/workers/51601 and .
