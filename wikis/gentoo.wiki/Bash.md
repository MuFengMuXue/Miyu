**Resources**

[[]][Home](https://www.gnu.org/software/bash/)

[[]][Home](https://tiswww.case.edu/php/chet/bash/bashtop.html)

[[]][Official documentation](https://www.gnu.org/software/bash/manual/bash.html)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/bash)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Bash_(Unix_shell) "wikipedia:Bash (Unix shell)")

[[]][[#bash](ircs://irc.libera.chat/#bash)] ([[webchat](https://web.libera.chat/#bash)])

**GNU Bash** (**B**ourne-**a**gain **sh**ell) is the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.

See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#General_usage "Terminal emulator") article for some general usage pointers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Shell completion]](#Shell_completion)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Login shell]](#Login_shell)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [.bashrc]](#.bashrc)
    -   [[2.3] [Shell completion integrations]](#Shell_completion_integrations)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Environment variables]](#Environment_variables)
        -   [[3.1.1] [PS1]](#PS1)
    -   [[3.2] [Built-ins]](#Built-ins)
        -   [[3.2.1] [set]](#set)
        -   [[3.2.2] [alias]](#alias)
            -   [[3.2.2.1] [Listing]](#Listing)
        -   [[3.2.3] [history]](#history)
    -   [[3.3] [Keyboard shortcuts]](#Keyboard_shortcuts)
        -   [[3.3.1] [vi mode]](#vi_mode)
        -   [[3.3.2] [emacs mode]](#emacs_mode)
            -   [[3.3.2.1] [Navigation]](#Navigation)
            -   [[3.3.2.2] [Screen control]](#Screen_control)
            -   [[3.3.2.3] [Text manipulation]](#Text_manipulation)
            -   [[3.3.2.4] [Command history]](#Command_history)
-   [[4] [Scripts]](#Scripts)
    -   [[4.1] [Script execution]](#Script_execution)
    -   [[4.2] [Redirection]](#Redirection)
    -   [[4.3] [Logical operators]](#Logical_operators)
    -   [[4.4] [Jobs]](#Jobs)
    -   [[4.5] [Command substitution]](#Command_substitution)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Garbled display]](#Garbled_display)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
    -   [[7.1] [Learning Modern Bash]](#Learning_Modern_Bash)
        -   [[7.1.1] [Debugging and Testing]](#Debugging_and_Testing)
        -   [[7.1.2] [Code Style and Documentation]](#Code_Style_and_Documentation)
        -   [[7.1.3] [Cheat Sheets]](#Cheat_Sheets)
    -   [[7.2] [Bash Reference Guides]](#Bash_Reference_Guides)
-   [[8] [References]](#References)

## [Installation]

[bash] is part of the [*\@system* set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") and comes installed on every Gentoo system. It is used internally by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s default package manager, and other Gentoo system components. It is therefore *highly recommended to not uninstall bash* (which is usual for a package in the \@system set), this would undoubtedly break the system. Do not uninstall bash just because another shell is installed, used, or set as a [login shell](https://wiki.gentoo.org/wiki/Login_shell "Login shell").

### [USE flags]

It is possible to [change USE flags](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE") for the bash package:

### [USE flags for] [app-shells/bash](https://packages.gentoo.org/packages/app-shells/bash) [[]] [The standard GNU Bourne again shell]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`+net`](https://packages.gentoo.org/useflags/+net)                   Enable /dev/tcp/host/port redirection
  [`+readline`](https://packages.gentoo.org/useflags/+readline)         Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`afs`](https://packages.gentoo.org/useflags/afs)                     Add OpenAFS support (distributed file system)
  [`bashlogger`](https://packages.gentoo.org/useflags/bashlogger)       Log ALL commands typed into bash; should ONLY be used in restricted environments such as honeypots
  [`examples`](https://packages.gentoo.org/useflags/examples)           Install examples, usually source code
  [`mem-scramble`](https://packages.gentoo.org/useflags/mem-scramble)   Build with custom malloc/free overwriting allocated/freed memory
  [`nls`](https://packages.gentoo.org/useflags/nls)                     Add Native Language Support (using gettext - GNU locale utilities)
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                     Optimize the build using Profile Guided Optimization (PGO)
  [`plugins`](https://packages.gentoo.org/useflags/plugins)             Add support for loading builtins at runtime via \'enable\'
  [`static`](https://packages.gentoo.org/useflags/static)               !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)       Verify upstream signatures on distfiles
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 12:21] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After making USE modifications, ask Portage to update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [[] Shell completion]

Shell completion programming, sometimes called tab completion, is available to many programs and their parameters on Gentoo. To enable shell completion for bash, install the [[[app-shells/bash-completion]](https://packages.gentoo.org/packages/app-shells/bash-completion)[]] package. No special USE flags for packages, which support completion, are required on individual packages. Post-installation, completion functionality can be managed through [[eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")].

`root `[`#`]`emerge --ask app-shells/bash-completion`

The [[[app-shells/gentoo-bashcomp]](https://packages.gentoo.org/packages/app-shells/gentoo-bashcomp)[]] package, which is installed by [[[app-shells/bash-completion]](https://packages.gentoo.org/packages/app-shells/bash-completion)[]], adds Gentoo-specific completions for e.g. [emerge].

Shell completion is enabled by default for all supported programs^[\[1\]](#cite_note-1)^.

## [Configuration]

### [Login shell]

Bash is the default shell on Gentoo, after installation. The default login shell for a user is defined in the [/etc/passwd] file.

The login shell can be changed using the [chsh] utility, to use another POSIX compatible shell ([chsh] is from [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]], which is part of the base profile). See the articles on [login](https://wiki.gentoo.org/wiki/Login "Login") and on [shell configuration](https://wiki.gentoo.org/wiki/Shell#Configuration "Shell") for more info.

### [Files]

There are many settings to consider when determining how to modify the shell\'s behavior. Configuration changes can be defined via variables, functions, or shell built-ins. These settings are defined in several different configuration files, where the settings in the last file parsed will overwrite entries in previously defined files.

-   [/etc/profile] - Initial (global) settings for all users.
-   [/etc/bash/bashrc.d] - Initial (global) settings for all users; here multiple files may be stored. Not a standard directory, but a few Linux distributions support it.
-   [\~/.bash_profile] - Local bash profile settings for the current user.
-   [\~/.bash_login] - Local settings for the current user, if [\~/.bash_profile] does not exist.
-   [\~/.profile] - Settings for the current user, if [\~/.bash_profile] and/or [\~/.bash_login] do not exist.

If the shell is started without login (e.g. in a terminal on a desktop), the following files are used:

-   [/etc/bash/bashrc] - Initial (global) settings for all users.
-   [\~/.bashrc] - Local settings on a per-user basis.

#### [.bashrc]

** Note**\
Do not confuse the commonly-used [.bashrc] bash configuration file with [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc"), a [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") file which is only ever used for very specific adjustments during package installation.

In Gentoo, and many other Linux distributions, [/etc/bashrc] is parsed from [/etc/profile] to ensure [/etc/bashrc] and [\~/.bashrc] are always checked when a user executes a new (non-login) shell. Local existing [\~/.bashrc] file settings always override global [/etc/bashrc] settings.

[FILE] **`~/.bashrc`**

    # This file contains suggested settings for a user's ~/.bashrc file.

    # Modify the PS1 variable to adjust command prompt
    # /u the username of the current user
    # /h the hostname up to the first `.'
    # /w the  current  working  directory, with $HOME abbreviated with a tilde (uses the value of the PROMPT_DIRTRIM variable)
    # /$ if the effective UID is 0, a #, otherwise a $
    # For more PS1 options see the PROMPTING section of `man 1 bash`
    PS1='\u@\h \w \$ '

    # No double entries in the shell history.
    export HISTCONTROL="$HISTCONTROL erasedups:ignoreboth"

    # Do not overwrite files when redirecting output by default.
    set -o noclobber

    # Wrap the following commands for interactive use to avoid accidental file overwrites.
    rm() "; }
    cp() "; }
    mv() "; }

### [[] Shell completion integrations]

List available completions via:

`user `[`$`]`eselect bashcomp list`

Disable specific completions using

`user `[`$`]`eselect bashcomp disable <command-name>`

To disable *all* bash shell completion integration for a particular user, create an [.inputrc] file with the following content in the user\'s home directory, then open a new bash shell:

[FILE] **`~/.inputrc`**

    # Disable bash completion
    set disable-completion on

It\'s considered good practice to store configs under [Git](https://wiki.gentoo.org/wiki/Git "Git").

## [Usage]

### [Environment variables]

See all variables for the current shell process which have the export attribute set:

`user `[`$`]`export`

Of course, users can export their own variables, which are available to the current process and inherited by child processes:

`user `[`$`]`export MYSTUFF=Hello`

Environment variables can also be localized to an individual child process by prepending an assignment list to a simple command. The resulting environment passed to `execve()` will be the union of the assignment list with the environment of the calling shell process:

`user `[`$`]`USE=kde emerge -pv libreoffice`

To check the value of a variable:

`user `[`$`]`typeset -p MYSTUFF`

#### [PS1]

The special shell variable named `PS1` defines what the terminal prompt looks like:

[CODE] **Example prompt**

    larry@gentoo: ~ $

** Note**\
In the above example, *larry* is the user name, *gentoo* is the system hostname, and the `~` (tilde) symbol represents the current user\'s home directory (also represented by the `HOME` environment variable in bash).

This prompt would be the following value for the `PS1` variable:

[CODE] **`PS1` definition**

    PS1="\u@\h \w $ "

The following table lists the possible placeholders that can be used in the `PS1` variable:

  ------ -----------------------------------------------------------------
  Code   Effect
  `\u`   Username.
  `\h`   Hostname.
  `\w`   Current directory.
  `\d`   Current date.
  `\t`   Current time.
  `\$`   Indicate the root user with \'#\' and normal users with \'\$\'.
  `\j`   Number of currently running tasks (jobs).
  ------ -----------------------------------------------------------------

Complete commands can be put into prompt using a command substitution. The following will execute the `cut -d\ -f1 /proc/loadavg` command to show the one-minute load average at the beginning of the prompt:

[CODE] **`PS1` definition**

    PS1="\$(cut -d\  -f1 /proc/loadavg) $ "

Looks like:

[CODE] **Prompt**

    0.10 $

Having colors in the prompt:

[CODE] **`PS1` definition**

    PS1="\e[0;32m\]\u@\h \w >\e[0m\] "

The `\e[0;32m\]` changes the color for every next output, put `\e[0m\]` at the end of the variable to reset the color, otherwise the whole prompt will be in green.

Color codes:

  -------------- --------------------------
  Code           Color
  `\e[0;30m\]`   Black
  `\e[0;31m\]`   Red
  `\e[0;32m\]`   Green
  `\e[0;33m\]`   Yellow
  `\e[0;34m\]`   Blue
  `\e[0;35m\]`   Magenta
  `\e[0;36m\]`   Cyan
  `\e[0;37m\]`   White
  `\e[0m\]`      Reset to standard colors
  -------------- --------------------------

The `0;` in `\e[0;31m\]` means foreground. If desired, other values like `1;` for foreground bold and `4;` for foreground underlined can be defined. Omit this number to refer to the background, e.g. `\e[31m\]`.

This script prints out all 256 color codes available in the Bash terminal that can be used in PS1 prompts. It prints color swatches in groups of 8 and demonstrates how to set text color using escape sequences. To reset the color back to the default after using an escape sequence, end the print out with `\e[0m`

[FILE] **`colors.sh`Bash Terminal Color Script**

    #!/bin/bash

    for color in ; do
      printf "\\e[38;5;%sm%3s\\e[0m " $color "\\e[38;5;$m"
      if ! ((($color + 1) % 8)); then
        echo
      fi
    done

The *tput* command in terminal provides an abstraction to control the appearance of the shell prompt. Instead of hard-coding escape sequences, *tput* uses terminal capabilities from the *terminfo* database. Here\'s an example that can be used for *tput* to change the color properties of your PS1 prompt:

[CODE] **`PS1` with tput for green text**

    PS1="\[$(tput setaf 2)\]\u@\h \w \$ \[$(tput sgr0)\]"

This sets the text color to green for the prompt. The tput setaf 2 command sets the foreground color using ANSI color codes, with *2* representing green. The `tput sgr0` command then resets the text formatting back to the terminal\'s default.

The prompt can be made visually informative about the Git repository status by coloring the branch name according to the repository state. Below is a *PS1* definition that color-codes the current branch as red for uncommitted changes, green for a clean directory, and yellow for stashed changes:

[CODE] **`PS1` with Colored Git Branch Status**

    git_branch() m$\\e[0m"
      fi
    }

    PS1="\u@\h \w \$(git_branch)\$ "

This prompt function checks the current Git branch and repository status, setting colors accordingly. Insert the function *git_branch* in your [\~/.bashrc] or [\~/.bash_profile] file, followed by the *PS1* assignment for this functionality to take effect.

### [Built-ins]

#### [set]

The set command is a shell built-in used to display and change settings in the bash shell.

Show all current settings:

`user `[`$`]`set -o`

Disable the shell history:

`user `[`$`]`set +o history`

Enable the shell history:

`user `[`$`]`set -o history`

#### [alias]

The [alias] builtin can be used to define a new command or redefine an existing command:

`user `[`$`]`alias ll='ls -l'`

Now whenever [ll] (two lowercase Ls) is send to the shell, it will actually execute [ls -l].

To remove an alias:

`user `[`$`]`unalias ll`

** Note**\
No harm is done to the actual command being redefined.

To temporarily bypass an alias escape the first letter of the command with a backslash character:

`user `[`$`]`\ls`

##### [Listing]

Run [alias] without any arguments to display a list of currently defined aliases:

`user `[`$`]`alias`

#### [history]

The history of used commands in a session is written to a file in the user\'s home directory. The easiest way to access the commands in the history is using the [Up] and [Down] keys.

To show all commands in the current history:

`user `[`$`]`history`

To search for commands in the history, by piping the output through [grep] and filter for words:

`user `[`$`]`history | grep echo`

The commands are numbered and can be executed using their index:

`user `[`$`]`!2`

To execute the last command used:

`user `[`$`]`!!`

Delete every command in the history:

`user `[`$`]`history -c`

Show the current settings for history:

`user `[`$`]`echo $HISTCONTROL`

### [Keyboard shortcuts]

bash includes two different keyboard shortcuts modes to make editing input on the command-line easier: emacs mode and vi mode. bash defaults to emacs mode.

#### [vi mode]

vi mode requires an [Esc] key press to prefix very movement or edit, so it can be a bit awkward to learn this mode. To change the mode to vi mode, execute the following command:

`user `[`$`]`set -o vi`

Review this bash [vi editing mode cheat sheet](https://www.catonmat.net/download/bash-vi-editing-mode-cheat-sheet.pdf) document by Peteris Krumins for more details on key bindings in vim mode.

#### [emacs mode]

To switch to emacs mode (which is the default mode):

`user `[`$`]`set -o emacs`

##### [Navigation]

The following sections are select excerpts from the bash man page. They can be retrieved locally by reading [man 1 bash]. They contain useful command-line navigation shortcuts and bash built-ins.

Search for `Commands for Moving` for the beginning of the section.

**Line movement:**

[ctrl]+[a]

[ctrl]+[e]

[ctrl]+[f]

[ctrl]+[b]

[alt]+[f]

[alt]+[b]

[ctrl]+[xx]

[ctrl]+[\]]-[\<char\>]

[ctrl]+[alt]-[\]]-[\<char\>]

**Directory movement:**

[cd /path]

[cd -]

[cd]

##### [Screen control]

[ctrl]+[s]

[ctrl]+[q]

[ctrl]+[l]

##### [Text manipulation]

**Deletion:**

[ctrl]+[u]

[ctrl]+[k]

[alt]+[d]

[alt]+[k]

[ctrl]+[w]

[ctrl]+[y]

##### [Command history]

[ctrl]+[p]

[ctrl]+[n]

[ctrl]+[r]

## [Scripts]

Shell scripts are text files which contain programs written in a certain shell scripting language. Which shell is used to interpret the commands in a script is defined by the first line of the script. This consists of two special characters `#!` (called the shebang), then a direct path to the shell. For example:

[FILE] **`myscript`**

    #!/bin/bash
    echo 'Hello World!'

If no shell is defined the default shell for the user who executes the script is used. Often [/bin/sh] is used, which is the father of all shells and has very limited functionalities. Nearly all shells available understand commands used when running [/bin/sh], so those scripts are highly portable.

** Note**\
On many distributions [/bin/sh] is a symbolic link to [/bin/bash]. But on other distributions (like Debian) it can be a symbolic link to [/bin/dash], which is a POSIX compliant variant of [sh]. In order to ensure good portability, be sure to test any script using the same shell as the one in its shebang.

### [Script execution]

To run scripts directly from the command-line, they need to be executable. To make a shell script executable:

`user `[`$`]`chmod +x myscript`

Now the script can be executed by using the [./] prefix, where either the shell defined by the shebang in the script or the default shell of the user is used:

`user `[`$`]`./myscript`

### [Redirection]

In Bash it is possible to redirect the output of one program into the input of another program using a pipe, indicated by the `|` symbol. This enables users to create command chains. Here is an example to redirect the output of [ls -l] into the program [/usr/bin/less]:

`user `[`$`]`ls -l | less`

To redirect output into a file:

`user `[`$`]`ls -l > ls_l.txt`

The `>` operator will erase any previous content before adding new one. If this is not desired, use the `>>` (append) operator instead.

### [Logical operators]

Logical operators are very useful to chain commands together. This is helpful when checking if the previous command finished successfully or not.

`&&` (AND) - The following command prints \'Success\' only if our test script is successful:

`user `[`$`]`./myscript && echo 'Success'`

`||` (OR) - The following command prints \'Failure\' only if our test script is unsuccessful:

`user `[`$`]`./myscript || echo 'Failure'`

### [Jobs]

Usually when script or command has been executed shell input is blocked until after execution has completed. To start a program directly in the background, append the ampersand character ([&]) to the end of the command:

`user `[`$`]`./myscript &`

This will execute the script as **job** number 1 and the prompt expects the next input.

When a program is already running, but the shell is needed for another task, it is possible to move programs from *foreground* to *background* and vice versa. To get a command prompt when a command is running on the shell, put it into *sleep* using [Ctrl]+[z], then move it to the background:

`user `[`$`]`bg %1`

To list all jobs running in the background:

`user `[`$`]`jobs`

To move a job back to foreground:

`user `[`$`]`fg %1`

** Note**\
Programs running as jobs usually do not terminate once they finish execution, there will be a message if a job finished and bringing it to foreground will then terminate the program.

### [Command substitution]

Using a command substitution, it is possible to run programs as parameters of other commands like here:

`user `[`$`]`emerge --ask --oneshot $(qlist -CI x11-drivers)`

This will first execute the command in the brackets and append the output as parameter of emerge.

** Note**\
This command is quite useful in Gentoo to quickly rebuild all X11 drivers.

More substitutions can be performed in one command like this:

`user `[`$`]`emerge --ask --oneshot $(qlist -CI x11-drivers) $(qlist -CI modules)`

## [Troubleshooting]

### [Garbled display]

The output of a shell can, in some conditions, become corrupt. See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator") article for instructions to help fix this.

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") --- a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell").
-   [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") --- an interactive login shell that can also be used as a powerful scripting language interpreter.
-   [Fish](https://wiki.gentoo.org/wiki/Fish "Fish") --- a smart and user-friendly command line [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and the rest of the family.
-   [Nushell](https://wiki.gentoo.org/wiki/Nushell "Nushell") --- a new kind of [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and Windows.
-   [bc](https://wiki.gentoo.org/wiki/Bc "Bc") --- arbitrary-precision fixed-point mathematical scripting language
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.

## [External resources]

### [Learning Modern Bash]

-   [Wikibooks Bash Scripting Guide](https://en.wikibooks.org/wiki/Bash_Shell_Scripting) --- an easy introduction to Bash scripting.
-   [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/) --- a slightly older but still useful Bash scripting guide.
-   [New Bash Features](https://mywiki.wooledge.org/BashFAQ/061) --- a list of features added to Bash over time.
-   [Bash Traps](https://web.archive.org/web/20230330234404/https://wiki.bash-hackers.org/scripting/newbie_traps) --- a collection of common mistakes and how to avoid them.
-   [Pure Bash Bible](https://github.com/dylanaraps/pure-bash-bible) --- a collection of pure Bash alternatives to external processes.
-   [Awesome Bash](https://github.com/awesome-lists/awesome-bash) --- A curated list of Bash scripts and resources.
-   [Exercism: Bash Track](https://exercism.org/tracks/bash) --- an interactive Bash tutorial.

#### [Debugging and Testing]

-   [Defensive Bash Programming](https://web.archive.org/web/20180917174959/http://www.kfirlavi.com/blog/2012/11/14/defensive-bash-programming) --- how not to shoot yourself in the foot with Bash.
-   [Unofficial Strict Mode](https://gist.github.com/robin-a-meade/58d60124b88b60816e8349d1e3938615) --- a \"strict mode\" inspired by the `use strict` pragma in [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") and a [detailed explanation](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425) of how this works.
-   [Unit Testing in Bash](https://github.com/dodie/testing-in-bash) --- a collection of Unit testing tools.
-   [shellcheck](https://github.com/koalaman/shellcheck) --- a static analysis tool for shell scripts.

#### [Code Style and Documentation]

-   [Shell Script Style Guide](https://google.github.io/styleguide/shellguide.html) --- Google\'s style guide for shell scripts.
-   [bash-doxygen](https://github.com/Anvil/bash-doxygen) --- A doxygen filter for bash scripts; great for developer documentation.
-   [Plain Old Documentation](https://charlotte-ngs.github.io/2015/01/BashScriptPOD.html) --- Perl-style POD documentation in Bash scripts; great for `man` page generation with `pod2man`.

#### [Cheat Sheets]

-   [Bash Scripting Cheat Sheet](https://devhints.io/bash).

### [Bash Reference Guides]

-   [Bash reference](https://devmanual.gentoo.org/tools-reference/bash/index.html) from the Gentoo Developer\'s Handbook.
-   [Chet\'s Bash page](https://tiswww.case.edu/php/chet/bash/bashtop.html).
-   The [Bash FAQ](https://mywiki.wooledge.org/BashFAQ) and [Bash guide](https://mywiki.wooledge.org/BashGuide) on Greg Wooledge\'s wiki.
-   [POSIX sh](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) specification.
-   [mksh](https://www.mirbsd.org/man/mksh.1), [ksh93](http://www2.research.att.com/sw/download/man/man1/ksh.html), and [ksh88](http://www2.research.att.com/sw/download/man/man1/ksh88.html) manuals for cross-reference.

## [References]

1.  [[[↑](#cite_ref-1)] [[News Items - bash-completion-2.1-r90](https://www.gentoo.org/support/news-items/2014-11-25-bash-completion-2_1-r90.html), November 25th, 2014. Retrieved on May 13th, 2017.]]