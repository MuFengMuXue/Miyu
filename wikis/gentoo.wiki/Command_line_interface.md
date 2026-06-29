Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Shell/hu "Shell (78% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Shell/ta "செயற்றளம் (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Shell/ja "シェル (63% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Shell_(computing)#Command-line_shells "wikipedia:Shell (computing)")

A **shell** is a command-line interpreter that provides a text-based interface to users, usually accessed in a [virtual console](https://en.wikipedia.org/wiki/Virtual_console "wikipedia:Virtual console") or a [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator").

Most shells can interpret [shell scripts](https://en.wikipedia.org/wiki/Shell_script "wikipedia:Shell script"): text files that contain prewritten commands targeting a specific shell or set of compatible shells.

Shells can often be accessed remotely, over [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") for example, or over a serial connection, etc.

Typically, a shell is the first program started after a user logs in at a virtual console or opens a terminal emulator. The [/etc/passwd] file contains information defining the [login shell](https://wiki.gentoo.org/wiki/Login "Login") for each user on the system.

A user can switch their current session to any other available shell simply by typing the command to run the alternative shell. It is usually possible to set the choice of login shell, in case of specific requirements or user preference (see \"User\'s login shell\" section below). Certain terminal emulators allow defining a specific shell for use in that emulator.

In Gentoo, the [/bin/sh] file is a symlink to the default system shell, which can be set to link to one of a choice POSIX shells. The default system shell and user shell on Gentoo after [installation](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") is [Bash](https://wiki.gentoo.org/wiki/Bash "Bash").

For information about scripting in the context of POSIX and different shell implementations, refer to the [Shell/Scripting](https://wiki.gentoo.org/wiki/Shell/Scripting "Shell/Scripting") page.

** See also**\
See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#General_usage "Terminal emulator") article for some general usage pointers.

** Note**\
When writing scripts, care should be taken to reference the correct interpreter on the first line by using a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix) "wikipedia:Shebang (Unix)"). A script beginning with `#!/bin/sh` should only use POSIX constructs without any bash specific code, for example.

## Contents

-   [[1] [The Command Line Interface]](#The_Command_Line_Interface)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [POSIX Shells]](#POSIX_Shells)
    -   [[2.2] [Non-POSIX Shells]](#Non-POSIX_Shells)
        -   [[2.2.1] [Generic System Shells]](#Generic_System_Shells)
        -   [[2.2.2] [Application Compatibility Shells]](#Application_Compatibility_Shells)
        -   [[2.2.3] [Bootloader Shells]](#Bootloader_Shells)
        -   [[2.2.4] [Firmware Shells]](#Firmware_Shells)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [System shell]](#System_shell)
    -   [[3.2] [User\'s login shell]](#User.27s_login_shell)
        -   [[3.2.1] [Creating a user with a specific login shell]](#Creating_a_user_with_a_specific_login_shell)
        -   [[3.2.2] [Setting an existing user\'s login shell]](#Setting_an_existing_user.27s_login_shell)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Garbled display]](#Garbled_display)
-   [[5] [See also]](#See_also)

## [The Command Line Interface]

The [Unix-like](https://en.wikipedia.org/wiki/Unix-like "wikipedia:Unix-like") **command line interface (CLI)** is a powerful, mature paradigm to interact with modern computers. The CLI maintains some notable advantages over graphically-based models, which makes it the tool of choice for many professionals.

The CLI provides a standardized text-based interface generally accessed through a shell running in a [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") (or [virtual console](https://wiki.gentoo.org/wiki/Terminal_emulator#Virtual_consoles_and_switching "Terminal emulator")).

The CLI has a rich history that predates even [CRT](https://en.wikipedia.org/wiki/Cathode-ray_tube "wikipedia:Cathode-ray tube") screen technology, beginning on [teleprinters](https://en.wikipedia.org/wiki/Teleprinter "wikipedia:Teleprinter"). This long history has resulted in a sophisticated system, which has developed many of its characteristics along with the [UNIX OS](https://en.wikipedia.org/wiki/UNIX "wikipedia:UNIX"). Today, text is almost always entered with a keyboard, and output presented on a screen.

Though the learning curve may be steeper than for GUIs, once minimal skill is acquired the CLI provides all the commands available on a system right under the user\'s fingertips, without having to read and navigate menus.

CLI tools tend to provide simple, easily memorizable interfaces whose options can be combined to achieve desired functionality. The CLI generally follows a standard interface to allow tight interaction between tools. It also allows for accessing the manuals of tools via [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page"), or more quickly and simply via `--help`.

Modern shells allow for powerful constructs such as [pipes](https://en.wikipedia.org/wiki/Pipeline_(Unix) "wikipedia:Pipeline (Unix)") by which various tools can interact seamlessly, and for the filtering and sorting of output via several CLI [utilities](https://wiki.gentoo.org/wiki/Category:Command_line_tools "Category:Command line tools").

Some CLI utilities may be interactive, either by asking for basic input after execution or by opening a command-specific subshell. Most utilities take input from the command line, [standard input](https://en.wikipedia.org/wiki/Standard_streams "wikipedia:Standard streams"), files, devices, or a network. Then they output either to the command line, or else have their output redirected to a file or piped to other commands.

## [Available software]

Gentoo provides a choice of shells:

### [POSIX Shells]

  -------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                                                     Package                                                                                                                                                                                                                                                                                                                                                                  Homepage                                                                                                                                   Description
  [ash]                                                         [[[sys-apps/busybox]](https://packages.gentoo.org/packages/sys-apps/busybox)[]]   [https://www.busybox.net/](https://www.busybox.net/)                                                       BusyBox\'s uses the minimalist Almquist shell.
  [[bash](https://wiki.gentoo.org/wiki/Bash "Bash")]            [[[app-shells/bash]](https://packages.gentoo.org/packages/app-shells/bash)[]]      [https://tiswww.case.edu/php/chet/bash/bashtop.html](https://tiswww.case.edu/php/chet/bash/bashtop.html)   The **B**ourne **A**gain **Sh**ell is the default shell on Gentoo. It is used by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s default package manager.
  [[dash](https://wiki.gentoo.org/wiki/Dash "Dash")]            [[[app-shells/dash]](https://packages.gentoo.org/packages/app-shells/dash)[]]      [http://gondor.apana.org.au/\~herbert/dash/](http://gondor.apana.org.au/~herbert/dash/)                    The **D**ebian **A**lmquist **Sh**ell. A small, fast, posix-compliant shell suited for startup scripts (as [/bin/sh] replacement).
  [[dsh](https://wiki.gentoo.org/wiki/Dsh "Dsh")]               [[[app-shells/dsh]](https://packages.gentoo.org/packages/app-shells/dsh)[]]         [https://www.netfort.gr.jp/](https://www.netfort.gr.jp/)                                                   A shell distributed shell that enables parallel execution of commands across large numbers of servers.
  [[fbc](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC")]   [[dev-lang/fbc](https://gitweb.gentoo.org/repo/proj/guru.git/tree/dev-lang/fbc)]                                                                                                                                                                      [https://www.freebasic.net/](https://www.freebasic.net/)                                                   FreeBASIC, a [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") compiler, [can be adapted](https://www.freebasic.net/forum/viewtopic.php?t=7483) to function as an interactive BASIC interpreter and POSIX shell.
  [[ksh](https://wiki.gentoo.org/wiki/Ksh "Ksh")]               [[[app-shells/ksh]](https://packages.gentoo.org/packages/app-shells/ksh)[]]         [http://www.kornshell.com/](http://www.kornshell.com/)                                                     The Original Korn Shell, 1993 revision (ksh93).
  [[mksh](https://wiki.gentoo.org/wiki/Mksh "Mksh")]            [[[app-shells/mksh]](https://packages.gentoo.org/packages/app-shells/mksh)[]]      [https://www.mirbsd.org/mksh.htm](https://www.mirbsd.org/mksh.htm)                                         An actively developed free implementation of the Korn Shell, well suited for scripting.
  [pwsh]                                                        [[[app-shells/pwsh]](https://packages.gentoo.org/packages/app-shells/pwsh)[]]      [https://learn.microsoft.com/powershell/](https://learn.microsoft.com/powershell/)                         Most shells assume \"everything is a file\". PowerShell is an object-oriented shell where \"everything is an object\". Now MIT-licensed and available on Linux.
  [tcsh]                                                        [[[app-shells/tcsh]](https://packages.gentoo.org/packages/app-shells/tcsh)[]]      [http://www.tcsh.org/](http://www.tcsh.org/)                                                               An enhanced version of the Berkeley **C** **Sh**ell ([csh]).
  [yash]                                                        [[[app-shells/yash]](https://packages.gentoo.org/packages/app-shells/yash)[]]      [https://yash.osdn.jp/](https://yash.osdn.jp/)                                                             **Y**et **A**nother **SH**ell is a POSIX-compliant command line shell written in C99 (ISO/IEC 9899:1999).
  [[zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh")]               [[[app-shells/zsh]](https://packages.gentoo.org/packages/app-shells/zsh)[]]         [http://www.zsh.org/](http://www.zsh.org/)                                                                 An advanced shell that is the chosen interactive shell for many users.
  -------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Non-POSIX Shells]

#### [Generic System Shells]

  -------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------- ---------------------------------------------
  Name                                                                                                                                                     Package                                                                                                                                                                                                                                                                                                                                                                        Homepage                                                                           Description
  [[fish](https://wiki.gentoo.org/wiki/Fish "Fish")]            [[[app-shells/fish]](https://packages.gentoo.org/packages/app-shells/fish)[]]            [https://fishshell.com/](https://fishshell.com/)   The **F**riendly **I**nteractive **SH**ell.
  [[nushell](https://wiki.gentoo.org/wiki/Nushell "Nushell")]   [[[app-shells/nushell]](https://packages.gentoo.org/packages/app-shells/nushell)[]]   [https://nushell.sh/](https://nushell.sh/)         A new type of shell, written in Rust
  -------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------- ---------------------------------------------

#### [Application Compatibility Shells]

  ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                       Package                                                                                                                                                                                                                                                                                                                                                                              Homepage                                                                             Description
  AmigaShell                                                                                                 [[[app-emulation/fs-uae]](https://packages.gentoo.org/packages/app-emulation/fs-uae)[]]   [https://fs-uae.net/](https://fs-uae.net/)           FS-UAE, an [Amiga](https://en.wikipedia.org/wiki/Amiga "wikipedia:Amiga") emulator, [can be configured](https://www.exxosforum.co.uk/forum/viewtopic.php?t=2372&start=10) to allow shell access from the terminal. The requisite AmigaOS components have open source implementations via [AROS](http://www.aros.org/).
  [cmd.exe]       [[[virtual/wine]](https://packages.gentoo.org/packages/virtual/wine)[]]                           [https://www.winehq.org/](https://www.winehq.org/)   A shell that reproduces the [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "wikipedia:Microsoft Windows") execution environment; part of [Wine](https://wiki.gentoo.org/wiki/Wine "Wine").
  [command.com]   [[[app-emulation/dosemu]](https://packages.gentoo.org/packages/app-emulation/dosemu)[]]   [http://www.dosemu.org/](http://www.dosemu.org/)     A shell that reproduces the [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS "wikipedia:MS-DOS") execution environment; part of [DOSEMU](https://wiki.gentoo.org/wiki/DOSEMU "DOSEMU").
  ---------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### [Bootloader Shells]

  -------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------- -------------------------------------
  Name                                               Package                                                                                                                                                                                                                                                                                                                                                         Homepage                                                                                                   Description
  [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")   [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]]   [https://www.gnu.org/software/grub/](https://www.gnu.org/software/grub/)   A minimalist pre-boot rescue shell.
  -------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------- -------------------------------------

#### [Firmware Shells]

  ----------------------------------------------------------------------------- --------- -------------------------------------------------------------------------------------------------- --------------------------------------------------------------------
  Name                                                                          Package   Homepage                                                                                           Description
  [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware")   ---       [https://www.openfirmware.info/](https://www.openfirmware.info/)   A [Forth](https://wiki.gentoo.org/wiki/Forth "Forth")-based shell.
  [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI")                              ---       [https://uefi.org/](https://uefi.org/)                             A minimalist firmware shell for EFI firmware.
  ----------------------------------------------------------------------------- --------- -------------------------------------------------------------------------------------------------- --------------------------------------------------------------------

For more shell options, see the [app-shells](https://packages.gentoo.org/categories/app-shells) package category or the output of the following command ([eix](https://wiki.gentoo.org/wiki/Eix "Eix") required):

`user `[`$`]`eix -cC app-shells`

## [Configuration]

** See also**\
See the [login](https://wiki.gentoo.org/wiki/Login "Login") article for how the environment is set up.

### [System shell]

** Important**\
Changing [/bin/sh] to something other than [bash] can cause rare issues with badly written scripts, e.g. scripts starting with `#!/bin/sh` but using bash-specific code. See [[[bug #526268]](https://bugs.gentoo.org/show_bug.cgi?id=526268)[]]. It may be safer to leave the system shell as the default bash, and set user login shells when creating users, or using the [chsh] command for existing users - see [next section](#changing_user_shell).

** Note**\
It\'s normal that only a handful of POSIX compatible shells will be available to be used with this method. See the [next section](#changing_user_shell) on how to set user login shells, which allows setting more shells as default. Also note the above warning, and consider preferentially using the method from the next section to set any shell as default.

The \"system shell\" is used when executed from [/bin/sh], such as by scripts that start with `#! /bin/sh`. Changing the \"system shell\" will not change what shell users login to, and will not change what shell is set for new users either.

System administrators can change the system shell using USE flags on [[[app-alternatives/sh]](https://packages.gentoo.org/packages/app-alternatives/sh)[]]. This utility changes the system shell by replacing [/bin/sh] with a symlink to a different POSIX compatible shell.

### [USE flags for] [app-alternatives/sh](https://packages.gentoo.org/packages/app-alternatives/sh) [[]] [/bin/sh (POSIX shell) symlink]

  ----------------------------------------------------------- --------------------------------------
  [`+bash`](https://packages.gentoo.org/useflags/+bash)       Symlink to app-shells/bash
  [`busybox`](https://packages.gentoo.org/useflags/busybox)   Symlink to sys-apps/busybox
  [`dash`](https://packages.gentoo.org/useflags/dash)         Symlink to app-shells/dash
  [`ksh`](https://packages.gentoo.org/useflags/ksh)           Symlink to app-shells/ksh
  [`lksh`](https://packages.gentoo.org/useflags/lksh)         Symlink to lksh from app-shells/mksh
  [`mksh`](https://packages.gentoo.org/useflags/mksh)         Symlink to mksh from app-shells/mksh
  ----------------------------------------------------------- --------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

To set a particular choice for [/bin/sh] use [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use`**

    # Make /bin/sh a symlink to dash from app-shells/dash
    app-alternatives/sh -bash dash

### [][[] User\'s login shell]

** Important**\
Some shells such as [fish](https://wiki.gentoo.org/wiki/Fish "Fish") can cause issues if directly set as the login shell. See the [caveats section of the fish article](https://wiki.gentoo.org/wiki/Fish#Caveats "Fish") to see how to set it as a default shell safely.

Login-shell settings are stored in [/etc/passwd].

#### [Creating a user with a specific login shell]

Login shells can be set when creating a new user with the [useradd] command (from [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]]).

To create a user and specify their login shell:

`user `[`$`]`useradd -s /bin/ksh -m larry`

The `-s` option indicates the path to the shell, the `-m` option instructs the [useradd] command to create the new user\'s home directory if it does not already exist.

#### [][Setting an existing user\'s login shell]

A user\'s login shell can be changed using the [chsh] command. To change the login shell for the current user, type [chsh] and enter the path to the new shell. In the example below, a user named *larry* is changing their login shell from [/bin/ksh] to [/bin/zsh]:

`user `[`$`]`chsh`

    Changing the login shell for larry
    Enter the new value, or press ENTER for the default
        Login Shell [/bin/ksh]: /bin/zsh

[chsh] can be used to change the login shell for any user from the super user account (root).

The [chsh] command only allows shells listed in [/etc/shells].

## [Troubleshooting]

### [Garbled display]

The output of a shell can, in some conditions, become corrupt. See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator") article for instructions to help fix this.

## [See also]

-   [GNU Coreutils](https://wiki.gentoo.org/wiki/GNU_Coreutils "GNU Coreutils") --- basic file, shell and text manipulation utilities of the GNU operating system; a superset of the utilities specified by the [POSIX \"Shell and Utilities\" volume](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html).
-   [Login](https://wiki.gentoo.org/wiki/Login "Login") --- logging in to a shell, and setting up the default environment.
-   [Recommended tools](https://wiki.gentoo.org/wiki/Recommended_tools "Recommended tools") --- lists system-administration related tools recommended for use in a **[shell] environment** ([terminal/console](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator"))
    -   [Pagers](https://wiki.gentoo.org/wiki/Recommended_tools#Pagers "Recommended tools")
    -   [Shell environment tools](https://wiki.gentoo.org/wiki/Recommended_tools#Shell_environment "Recommended tools")
    -   [Terminal multiplexers](https://wiki.gentoo.org/wiki/Recommended_tools#Terminal_multiplexers "Recommended tools")
-   [Shell/Scripting](https://wiki.gentoo.org/wiki/Shell/Scripting "Shell/Scripting") --- a reference guide to **scripting-related differences** between [shells]
-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).
-   [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux") --- userspace utilities for Linux-specific system management, including device control, terminal logins, process management, and tty messaging.