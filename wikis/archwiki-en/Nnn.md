# Nnn

nnn (also stylized as n³) is a portable terminal file manager written in C. It is easily extensible via its flat text plugin system where you can add your own language-agnostic scripts alongside already available plugins, including a (neo)vim plugin.

nnn features native archiving/decompression to and from commonly installed formats such as xz, disk usage analysis and a fuzzy app launcher, a batch file renamer and a file picker through its plugin architecture. nnn supports instant search-as-you-type with regex (or simple string) filters and a navigate-as-you-type mode for continuous navigation in filter mode with directory auto-select. Also supported are contexts, bookmarks, multiple sorting options, SSHFS, batch operations on selections (a group of selected files) and a lot more.

Despite its capabilities, nnn is designed to be easy to use and is configured by way of environment variables without the use of a configuration file.

## Installation
Install the  package.

## Usage
nnn can be controlled with the vi-like keys  or the . Do not memorize keys: arrows,  and  suffice. Press  for help on keyboard shortcuts anytime.

## Configuration
nnn is configured via environment variables. For detailed information on these settings, see  as well as the nnn wiki.

One of the more useful settings is the  variable which lets you choose shortcuts to quickly jump to your bookmarked directories. They are reached with  followed by one of the letters that you have specified. In the example configuration hitting the keys  would result in nnn jumping into . But all of these are optional, nnn will consistently behave the same on all of your machines.

## Get selected files in terminal
To get a list of the files you have selected in nnn one could create the following alias:

{{hc|head=~/.bashrc|output=
alias ncp="cat ${NNN_SEL:-${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.selection} | tr '\0' '\n'"
}}

which later could be used to pipe the selected files to other tools.

## Indicate depth level within nnn shells
If you use  to spawn a shell in the current directory, it could be nice to add:

To have your prompt indicate that you are within a shell that will return you to nnn when you are done.

This together with #cd on quit (Ctrl-G) becomes a powerful combination.

## cd on quit (Ctrl-G)
Add the following to your /

And run the  command instead of  (more precisely the n bash function).

Also see the nnn wiki.

## Add your own plugins
You can run your own plugins by putting them in {{ic|${XDG_CONFIG_HOME:-$HOME/.config}/nnn/plugins}}. For example you could create a executable shell script

{{hc|head=${XDG_CONFIG_HOME:-$HOME/.config}/nnn/plugins/git-changes|output=
#!/usr/bin/env sh
git log -p -- "$@"
}}

Set the environment variable  and then trigger it by pressing  and selecting  which will conveniently show the git log of changes to the particular file along with the code for a quick and easy review.
