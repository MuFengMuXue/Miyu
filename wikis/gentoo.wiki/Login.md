This article covers logging in to a shell, and setting up the default environment. See [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") for graphical logins.

Login consists of several steps:

1.  Authentication - See [Category:Authentication](https://wiki.gentoo.org/wiki/Category:Authentication "Category:Authentication")
2.  Provision of services with privilege - [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") organizes services, and also works in several other cases.
3.  Login shell invocation

On effective [shell](https://wiki.gentoo.org/wiki/Shell "Shell") invocation, the UID is set to that of the logged in user, then any shell initialization scripts are invoked, as described below.

## Contents

-   [[1] [Login shell startup scripts and environment variables]](#Login_shell_startup_scripts_and_environment_variables)
-   [[2] [Bash and variants - default]](#Bash_and_variants_-_default)
    -   [[2.1] [System wide config files for Bash]](#System_wide_config_files_for_Bash)
-   [[3] [Tcsh]](#Tcsh)
    -   [[3.1] [System wide config files for tcsh]](#System_wide_config_files_for_tcsh)
-   [[4] [Fish]](#Fish)
-   [[5] [See also]](#See_also)
-   [[6] [External links]](#External_links)
-   [[7] [References]](#References)

## [Login shell startup scripts and environment variables]

One important job of a login shell is to set system-wide environment variables. In Gentoo this is done:

-   for [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") and variants, by reading [/etc/profile.env] file
-   for csh/tcsh, by reading [/etc/csh.env] file.

The following sections concentrate on Gentoo login shells. For general information about login shells in Unix, see the [#external links](#external_links).

## [Bash and variants - default]

For Bash and variants, starting a login shell sources (executes in current process, conserving environment) configuration scripts, e.g. [/etc/profile], among others. These configuration files set environment variables, and perform some setup. These settings will be inherited by other shells, say opened in [terminal emulators](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator").

A bash login shell reads, in order:

-   [/etc/profile]
-   [/etc/profile.env]
-   Any files under the [/etc/profile.d/] directory with a [.sh] suffix.

[/etc/bash/bashrc] is also sourced - this does *not* configure Gentoo itself, but provides the Gentoo-default bash look-and-feel.

### [System wide config files for Bash]

[/etc/profile]

<!-- -->

[/etc/profile.env]

<!-- -->

[/etc/profile.d/\*.sh]

** Tip**\
When these files are updated (often after updating [/etc/profile.env], then running [env-update]), they must be sourced again from currently running shell(s), for the shell instances to continue functioning correctly - for example by running [source /etc/profile].

## [Tcsh]

When tcsh is run as the login shell, it reads one system-wide configuration file, [/etc/csh.login], which then sources other system-wide configuration files. These configuration files set environment variables, and do some other setup. These settings will be inherited by other shells, say opened in [terminal emulators](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator").

A tcsh login shell also reads [/etc/csh.cshrc], which provides some tcsh-specific default behavior, but does *not* configure Gentoo itself.

A tcsh login shell reads files in the following order:

-   [/etc/csh.login]
-   [/etc/csh.env]
-   Any files under the [/etc/profile.d/] directory with a [.csh] suffix.

### [System wide config files for tcsh]

[/etc/csh.login]

<!-- -->

[/etc/csh.env]

<!-- -->

[/etc/profile.d/\*.csh]

** Tip**\
When these files are updated, typically [/etc/csh.env], they must be sourced again from currently running shell(s), for the shell instances to continue functioning correctly.

## [Fish]

As stated in the article [fish](https://wiki.gentoo.org/wiki/Fish "Fish"), fish can\'t load system-wide configuration files mentioned above. To use fish as a user\'s default shell, there is a good workaround detailed in the fish article.

## [See also]

-   [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") --- presents the user with a graphical login screen to start a GUI session, either [X](https://wiki.gentoo.org/wiki/Xorg "Xorg") or [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland").
-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).

## [External links]

-   [login shell](https://wiki.archlinux.org/index.php/Login_shell) - ArchLinux Wiki article, for more general aspects of Unix login shells.

## [References]

1.  [[[↑](#cite_ref-1)] [More precisely, if there\'s any change in the directory [/etc/env.d], `emerge` will re-generate [/etc/profile.env]. (*Any* change will be caught; it is not limited to changes done by ebuild-helper-commands `doenvd` or `newenvd`.) Same can be expected for Gentoo official tools like eselect.]]
2.  [[[↑](#cite_ref-2)] [See [Linux Standard Base Core Specification, Generic Part, 5.0 Edition](https://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/book1.html)]]