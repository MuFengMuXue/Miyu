# Command-line shell

From Wikipedia:

:A Unix shell is a command-line interpreter or shell that provides a traditional user interface for the Unix operating system and for Unix-like systems. Users direct the operation of the computer by entering commands as text for a command line interpreter to execute or by creating text scripts of one or more such commands.

## List of shells
Shells that are more or less POSIX compliant are listed under #POSIX compliant, while shells that have a different syntax are under #Alternative shells.

## POSIX compliant
These shells can all be linked from . When Bash,  and zsh are invoked with the  name, they automatically become more POSIX compliant.

*
*
*
*
*
*
*

## Alternative shells
*
*
*
*
*
*
*
*
*
*
*

## Changing your default shell
After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

 $ chsh -l

And to set one as default for your user do:

 $ chsh -s /full/path/to/shell

If you are using systemd-homed, run:

 $ homectl update --shell=/full/path/to/shell user

where  is the full path as given by .

If you now log out and log in again, you will be greeted by the other shell.

## Uninstalling shell
Change the default shell before removing the package of the shell.

Alternatively, modify the user database.

Use it for every user with a shell other than bash set as their login shell (including root if needed). When completed, the package can be removed.

## Login shell
A login shell is an invocation mode, in which the shell reads files intended for one-time initialization, such as system-wide  or the user's  or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via SSH, changes the user with sudo or su using the  parameter, or when the user manually invokes a login shell (e.g. by ).

See #Configuration files and the links therein for an overview of the various initialization files. For more information about login shell, see also Difference between Login Shell and Non-Login Shell? and Why a "login" shell over a "non-login" shell? on Stack Exchange.

## Configuration files
To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g. Bash#Configuration files or Zsh#Startup/Shutdown files.

See also Wikipedia:Unix shell#Configuration files for a comparison of various configuration files of various shells.

## /etc/profile
Upon login, all Bourne-compatible shells source , which in turn sources any readable  files in : these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

## Standardisation
It is possible to make (some) shells configuration files follow the same naming convention, as well as supporting some common configuration between the shells.

See the article about this and the related repository. See also xsh.

## Input and output
See also GregsWiki and I/O Redirection.

* Redirections truncate files before commands are executed:  will therefore not work as expected. While some commands (sed for example) provide an option to edit files in-place, many do not. In such cases you can use the  command from the  package.
* Because cat is not built into the shell, on many occasions you may find it more convenient to use a redirection, for example in scripts, or if you care a lot about performance. In fact  or, for Bash 4, .
* Remember that many GNU core utilities accept files as arguments, so for example  is replaceable with .
