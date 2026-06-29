# Fish

fish, the ''friendly interactive shell'', is a commandline shell intended to be interactive and user-friendly.

fish is intentionally not fully POSIX compliant, it aims at addressing POSIX inconsistencies (as perceived by the creators) with a simplified or a different syntax. This means that even simple POSIX compliant scripts may require some significant adaptation or even full rewriting to run with fish.

## Installation
Install the  package.

Once installed, simply type  to drop into the fish shell.

Documentation can be found by typing  from fish; it will be opened in a web browser. It is recommended to read at least the "Syntax overview" section, since fish's syntax is different from many other shells.

## System integration
One must decide whether fish is going to be the default user's shell, which means that the user falls directly in fish at login, or whether it is used in interactive terminal mode as a child process of the current default shell, here we will assume the latter is Bash. To elaborate on these two setups:

* fish used as the default shell: this mode requires some basic understanding of the fish functioning and its scripting language. The user's current initialization scripts and environment variables need to be migrated to the new fish environment. To configure the system in this mode, follow #Setting fish as default shell.
* fish used as an interactive shell only: this is the less disruptive mode, all the Bash initialization scripts are run as usual and fish runs on top of Bash in interactive mode connected to a terminal. To setup fish in this mode, follow #Setting fish as interactive shell only.

## Setting fish as default shell
If you decide to set fish as the default user shell, the first step is to set the shell of this particular user to . This can be done by following the instructions in Command-line shell#Changing your default shell.

The next step is to port the current needed actions and configuration performed in the various Bash initialization scripts, namely , ,  and , into the fish framework.

In particular, the content of the  environment variable, once directly logged under fish, should be checked and adjusted to one's need. In fish,  is defined as a global environment variable: it has a global scope across all functions, it is lost upon reboot and it is an environment variable which means it is exported to child processes. The recommended way of adding additional locations to the path is by calling the fish_add_path command from . For example:

 $ fish_add_path -p /first/path /second/path /third/one

These three locations will be prepended to the path.

## Setting fish as interactive shell only
Not setting fish as system wide or user default allows the current Bash scripts to run on startup. It ensures the current user's environment variables are unchanged and are exported to fish which then runs as a Bash child. Below are several ways of running fish in interactive mode without setting it as the default shell.

## Modify .bashrc to drop into fish
Keep Bash as the default shell and simply add the line  to the appropriate Bash#Configuration files, such as . This will allow Bash to properly source  and all files in . Because fish replaces the Bash process, exiting fish will also exit the terminal. Compared to the following options, this is the most universal solution, since it works both on a local machine and on a SSH server.
{{Tip|
* In this setup, use  to manually enter Bash without executing the commands from  which would run  and drop back into fish.
* Alternatively, you can add checks to drop into fish only if the parent process is not fish. This way you can quickly enter into bash by invoking  command without losing  configuration.
* You might also want to check the  variable before dropping into fish. It will prevent unwanted "bash-fish alternation" when nesting shells (useful if you use programs like ). Note that, depending on how you start your GUI session (e.g. from display manager or  from tty, with or without ),  might equal to  rather than .
* In order to let fish know whether it is a login shell, you can detect login shell status in  and pass on the  option to fish. The fish shell command  can be used to show the status.

To add this logic to your , you can use the following:

{{bc|if grep -qv 'fish' /proc/$PPID/comm && ${SHLVL} == [1,2 ]]
then
	shopt -q login_shell && LOGIN_OPTION='--login' || LOGIN_OPTION=''
	exec fish $LOGIN_OPTION
fi}}
}}

## Use terminal emulator options
Another option is to open your terminal emulator with a command line option that executes fish. For most terminals this is the  switch, so for example, to open gnome-terminal using fish, change your shortcut to use:

 gnome-terminal -e fish

With terminal emulators that do not support setting the shell, for example , it would look like this:

 SHELL=/usr/bin/fish lilyterm

Also, depending on the terminal, you may be able to set fish as the default shell in either the terminal configuration or the terminal profile.

## Use terminal multiplexer options
To set fish as the shell started in tmux, put this into your :

 set-option -g default-shell "/usr/bin/fish"

Whenever you run tmux, you will be dropped into fish.

## Configuration
The configuration file runs at every login and is located at . Adding commands or functions to the file will execute/define them when opening a terminal, similar to . Note that whenever a variable needs to be preserved, it should be set as universal rather than defined in the aforementioned configuration file.

The user's functions are located in the directory  under the filenames .

## Web interface
The fish terminal colors, prompt, functions, variables, history, bindings and abbreviations can be set with the interactive web interface:

 fish_config

It may fail to start if IPv6 has been disabled. See and IPv6#Disable IPv6.

## Command completion
fish can generate autocompletions from man pages. Completions are written to  (controlled by XDG_CACHE_HOME environment variable) and can be generated by calling:

 fish_update_completions

You can also define your own completions in . See  for a few examples.

Context-aware completions for Arch Linux-specific commands like pacman, pacman-key, makepkg, pbget, pacmatic are built into fish, since the policy of the fish development is to include all the existent completions in the upstream tarball. The memory management is clever enough to avoid any negative impact on resources.

## Tips and tricks
## Command substitution
fish does not implement Bash style history substitution (e.g. ), and the developers recommend in the [https://fishshell.com/docs/current/faq.html#why-doesn-t-history-substitution-etc-work fish faq to use the interactive history recall interface instead: the  arrow recalls whole past lines and  (or ) recalls individual arguments, while  prepends  to the existing line.

However some workarounds are described in the fish wiki: while not providing complete history substitution, some functions replace  with the previous command or  with the previous last argument.

## Disable greeting
By default, fish prints a greeting message at startup. To disable it, run once:

 $ set -U fish_greeting

This clears the universal  variable, shared with all fish instances and which is preserved upon restart of the shell.

## Make su launch fish
If su starts with Bash because Bash is the target user's (root if no username is provided) default shell, one can define a function to redirect it to fish whatever the user's shell:

## Start X at login
Add the following to the bottom of your .

For those running fish in interactive mode, replace  with  in the above code.

## Put git status in prompt
If you would like fish to display the branch and dirty status when you are in a git directory, you can define the following  function:

## Color the hostname in the prompt in SSH
To color the hostname in the prompt dynamically whenever connected through SSH, add the following lines in either the  function or the fish configuration file, here using the red color:

Note that the default fish prompt colors the hostname yellow when connected through SSH; additional modification to the prompt is not required for this functionality.
## Evaluate ssh-agent
In fish,  generate errors due to how variables are set. To work around this, use the csh-style option :

 $ eval (ssh-agent -c)

## Evaluate keychain
Because  uses the  environment variable to format output, it should work with fish as the default shell. However, if using fish as an interactive shell only, this variable must be set:

 $   SHELL=/bin/fish keychain --eval --quiet -Q id_ed25519 | source

## The "command not found" hook
Fish includes a "command not found" hook that will automatically search the official repositories, when entering an unrecognized command. This hook will be run using , falling back to  if it is not installed.

Since 3.2.2, "command not found" will not fallback to  by default due to its bad performance.

If the delay this behavior introduces is undesirable, this hook can be overridden by redefining  so that it only prints an error message:

 $ function fish_command_not_found
       __fish_default_command_not_found_handler $argvend

To make this change permanent, the  built-in can be used:

 $ funcsave fish_command_not_found

## Remove a process from the list of jobs
fish terminates any jobs put into the background when fish terminates. To keep a job running after fish terminates, first use the  builtin. For example, the following starts  in the background and then disowns it:

 $ firefox &
 $ disown

This means firefox will not be closed when the fish process is closed. See  in fish for more details.

## Set a persistent alias
To quickly make a persistent alias, one can simply use the method showed in this example:

 $ alias lsl "ls -l"
 $ funcsave lsl

alias supports the / option since fish version 3.0:

 $ alias -s lsl "ls -l"

This will create the function:

 function lsl
     ls -l $argv
 end

and will set the alias as a persistent shell function. To see all functions and/or edit them, one can simply use  and look into the Function tab in the web configuration page.

For more detailed information, see [https://fishshell.com/docs/current/cmds/alias.html alias - create a function — fish-shell.

## Source /etc/profile on login
Unlike ,  does not source  on a tty login. If you need to source this file for
the environment variables appended and declared in the  directory, you can add the following to your config:

This allows you to run  as your login shell, while still having all the environment variables you would typically
have in a  login session.
