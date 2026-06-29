# Environment variables

An environment variable is a named object that contains data used by one or more applications. In simple terms, it is a variable with a name and a value. The value of an environmental variable can for example be the location of all executable files in the file system, the default editor that should be used, or the system locale settings. Users new to Linux may often find this way of managing settings a bit unmanageable. However, environment variables provide a simple way to share configuration settings between multiple applications and processes in Linux.

## Utilities
The  package contains the programs  and . List the current environment variable values with:

 $ printenv

The env utility can be used to run a command under a modified environment. The following example will launch xterm with the environment variable  set to . This will not affect the global environment variable .

 $ env EDITOR=vim xterm

The shell builtin  allows you to change the values of shell options, set the positional parameters and to display the names and values of shell variables.

Each process stores their environment in the  file. This file contains each key value pair delimited by a nul character (). A more human readable format can be obtained with sed, e.g. .

## Defining variables
To avoid needlessly polluting the environment, you should seek to restrict the scope of variables. In fact, graphical sessions and systemd services require you to set variables in certain locations for them to take effect. The scopes of environment variables are broken down into the contexts they affect:

* Global: All programs that any user runs, not including systemd services.
* By user: All programs that a particular user runs, not including user systemd services (see systemd/User#Environment variables) or graphical applications (see #Graphical environment).

## Globally
## Using shell initialization files
Most Linux distributions tell you to change or add environment variable definitions in  or other locations. Keep in mind that there are also package-specific configuration files containing variable settings such as . Be sure to maintain and manage the environment variables and pay attention to the numerous files that can contain environment variables. In principle, any shell script can be used for initializing environmental variables, but following traditional UNIX conventions, these statements should only be present in some particular files.

The following files can be used for defining global environment variables on your system, each with different limitations:

*  is used by the pam_env module and is shell agnostic so scripting or glob expansion cannot be used. The file only accepts  pairs.
*  initializes variables for login shells only. It does, however, run scripts (e.g. those in ) and can be used by all Bourne shell compatible shells.
* Shell specific configuration files - Global configuration files of your shell, initializes variables and runs scripts. For example Bash#Configuration files (e.g. ) or Zsh#Startup/Shutdown files (e.g. ).

The following Bash helper function can be used to append a number of directories to the  environment variable. Add the function at the top of the file where you define your environment (e.g. ). The function will only add directories that actually exist on the filesystem, and it will avoid creating duplicate entries.

{{bc|
add_paths() {
  for d in "$@"; do
    :)$d(:|$)  && PATH="$PATH:$d"
  done
}

add_paths ~/bin ~/scripts
}}

Most shells (including Bash, Zsh, and fish) allow adding variables to the environment using the  command. This allows defining environment variables in a common file such as :

This file can then be sourced from shell startup files:

## Using pam_env
The PAM module  loads the variables to be set in the environment from the following files in order:  and .

 must consist of simple  pairs on separate lines, for example:

 has the following format:

{{ic|@{HOME} }} and  {{ic|@{SHELL} }} are special variables that expand to what is defined in . The following example illustrates how to expand the  environment variable into another variable:

{{hc|/etc/security/pam_env.conf|2=
XDG_CONFIG_HOME   DEFAULT=@{HOME}/.config
}}

{{Note|The variables {{ic|${HOME} }} and {{ic|${SHELL} }} are not linked to the  and  environment variables, they are not set by default.}}

The format also allows to expand already defined variables in the values of other variables using {{ic|${VARIABLE} }}, like this:

{{hc|/etc/security/pam_env.conf|2=
GOPATH DEFAULT=${XDG_DATA_HOME}/go
}}

 pairs are also allowed, but variable expansion is not supported in those pairs. See  for more information.

## Per user
You do not always want to define an environment variable globally. For instance, you might want to add  to the  variable but do not want all other users on your system to have that in their  too. Local environment variables can be defined in many different files:

* User configuration files of your shell, for example Bash#Configuration files or Zsh#Startup/Shutdown files.
** Unless you are restricting the scope of the variables to terminals you open (e.g. command-line applications only), you are looking to modify the login shell.
* systemd user environment variables are read from .

To add a directory to the  for local usage, put following in :

 export PATH="${PATH}:/home/my_user/bin"

To update the variable, re-login or source the file: .

## Graphical environment
If an environment variable only affects graphical applications, you may want to restrict the scope of it by only setting it within the graphical session. In order of decreasing scope:

* #Per Xorg session and #Per Wayland session affect the whole graphical session, certainly including the DE.
* #Per desktop environment session affects the applications spawned within graphical session, potentially including the DE itself.
* #Per application affects just a particular graphical application.

## Per desktop environment session
Some graphical environments, (e.g. KDE Plasma) support executing shell scripts at login: they can be used to set environment variables. See KDE#Autostart for example.

## Per Xorg session
The procedure for modifying the environment of the Xorg session depends on how it is started:
* Most display managers source xprofile.
* startx and SLiM execute xinitrc.
* XDM executes ; see XDM#Defining the session.
* LightDMPlasma login manager[https://github.com/KDE/plasma-login-manager/blob/master/data/scripts/Xsession and SDDMadditionally source startup scripts for login shells, like  for bash or  and  for zsh.

Though the end of the script depends on which file it is, and any advanced syntax depends on the shell used, the basic usage is universal:

## Per Wayland session
Since Wayland does not initiate any Xorg related files, GDM and KDE Plasma source systemd user environment variables instead.

No other display managers supporting Wayland sessions (e.g. SDDM) provide direct support for this yet. However, LightDM, Plasma login manager and SDDM source startup scripts for login shells on Wayland sessions too.

greetd also sources  and  - this behavior is controlled by its  setting, enabled by default.

If your display manager sources startup scripts like  and you want to use , you can source it like so:

## Per application
To set environment variables only for a specific application instead of the whole session, edit the application's .desktop file. See Desktop entries#Modify environment variables for instructions.

For Steam games, you can configure a program's environment by editing its launch options; see Steam#Launch options.

## Per session or shell
Sometimes only temporary variables are required. One might wish to temporarily run executables from a specific directory without typing the absolute  each time, or use the  in a short temporary shell script.

For example, to add a session-specific directory to , use:

 $ export PATH="${PATH}:/home/my_user/tmp/usr/bin"

To add only a shell-specific directory to , use:

 $ PATH="${PATH}:/home/my_user/tmp/usr/bin"

In Bash,  is already exported by default, so both of the above will remain visible to subprocesses unless overwritten. To better illustrate the difference between exported and non-exported variables, consider the following:

 $ MYVAR="shell-only"
 $ bash -c 'echo $MYVAR'  # prints nothing

 $ export MYVAR="session-wide"
 $ bash -c 'echo $MYVAR'  # prints: session-wide

## Examples
The following section lists a number of common environment variables used by a Linux system and describes their values.

## Desktop environment detection
; XDG_CURRENT_DESKTOP:
A freedesktop.org variable containing a colon separated list of strings that the current desktop environment identifies as [https://specifications.freedesktop.org/mime-apps-spec/latest/file.html. Standardized values for actively developed environments are , , , , , , , , , , , , and  ; XDG_SESSION_DESKTOP:
Similar to , but only permits a single string. Despite its name, [https://gitlab.gnome.org/GNOME/gtk/-/issues/1224#note_270915 it is not standardized by freedesktop.org.
; DE:
A legacy variable indicating the desktop environment being used. There is no central documentation for what possible values are, but xdg-utils provides a reference for many desktop environments.
; DESKTOP_SESSION:
Another legacy variable, similar to  but less common. It may be a path to the session's desktop entry, in  ; WINDOW_MANAGER:
A variable sometimes used to choose the window manager to be used in a desktop environment, as opposed to the other variables here which are set by the already chosen display manager or desktop environment, for other programs to read.
; DISPLAY:
Used by the X Window System to specify the host, display and screen. The format is . A display refers to a collection of screens sharing a common set of input devices (keyboard, mouse, etc.). The host name was formerly used to specify the name of the machine to which the display is connected but it should be missing when the X server runs on the same computer than the X client. See  for more details.
; WAYLAND_DISPLAY:
The Wayland equivalent of , set by the compositor. If unset, applications will try .
; XAUTHORITY:
Path to the  file. This file contains credentials to access the X Window Server. These are often stored under the form of a cookie (arbitrary piece of data) sent to X server to authenticate (for example, ).

## System and session paths
; HOME:
Contains the path to the home directory of the current user. This variable can be used by applications to associate configuration files and such like with the user running it.
; PATH:
Contains a colon-separated list of directories in which your system looks for executable files. When a regular command (e.g. ls, systemctl or pacman) is interpreted by the shell (e.g. bash or zsh), the shell looks for an executable file with the same name as your command in the listed directories, and executes it. To run executables that are not listed in , a relative or absolute path to the executable must be given, e.g.  or .

; PWD:
Contains the path to the working directory.
; OLDPWD:
Contains the path to the previous working directory, that is, the value of  before last cd was executed.
; MAIL:
Contains the location of incoming email. The traditional setting is .

## Network proxies
; ftp_proxy:
Contains FTP proxy server
 ftp_proxy="ftp://192.168.0.1:21"
;http_proxy:
Contains HTTP proxy server
 http_proxy="http://192.168.0.1:80"

## Documentation paths
; MANPATH:
Contains a colon-separated list of directories in which man searches for the man pages.

; INFODIR:
Contains a colon-separated list of directories in which the info command searches for the info pages, e.g.,

## Default programs
; SHELL:
Contains the path to the user's [https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html#tag_08_03 preferred shell. Note that this is not necessarily the shell that is currently running. In the event that it has no value, Bash will automatically set this variable to the user's login shell as defined in  or to  if this cannot be determined.
; PAGER:
Contains command to run the program used to list the contents of files, e.g., .
; EDITOR:
Contains the command to run the lightweight program used for editing files, e.g., . For example, you can write an interactive switch between gedit under X or nano, in this example:
 [ -n "$DISPLAY" ] && export EDITOR=gedit || export EDITOR=nano
; VISUAL:
Contains command to run the full-fledged editor that is used for more demanding tasks, such as editing mail (e.g., , vim, emacs etc).
; TERMINAL:
Contains the command to run the user's preferred terminal emulator. This is not necessarily the currently running terminal ().
; BROWSER:
Contains the path to the web browser. Helpful to set in an interactive shell configuration file so that it may be dynamically altered depending on the availability of a graphic environment, such as X:
 [ -n "$DISPLAY" ] && export BROWSER=firefox || export BROWSER=links

## Miscellaneous
; TERM:
Contains the type of the running terminal, e.g. . It is used by programs running in the terminal that wish to use terminal-specific capabilities (see ). This variable should be set by the terminal emulator and overriding it from the shell is not advised.
; TZ:
Used to to set a time zone different to the system zone for a user. The zones listed in  can be used as reference, for example . When pointing the  variable to a zoneinfo file, it should start with a colon per the GNU manual.

## Shell environment detection
See a repository about shell environment detection for tests to detect the shell environment. This includes login/interactive shell, Xorg session, TTY and SSH session.
