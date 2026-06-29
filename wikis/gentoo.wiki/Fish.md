This page contains [[changes](https://wiki.gentoo.org/index.php?title=Fish&diff=1428178)] which are not marked for translation.

**Resources**

[[]][Home](https://fishshell.com)

[[]][Official documentation](https://fishshell.com/docs/current/index.html)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/fish)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Friendly_interactive_shell "wikipedia:Friendly interactive shell")

[[]][GitHub](https://github.com/fish-shell/fish-shell)

**fish** - the **f**riendly **i**nteractive **sh**ell - is a smart and user-friendly command line [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and the rest of the family. [fish] includes features like syntax highlighting, autosuggest-as-you-type, and fancy tab completions that just work, with no configuration required.

Refer to the \"[terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#General_usage "Terminal emulator")\" article for some general usage pointers.

** Important**\
[fish] is not a POSIX-compatible shell. It could cause issues if improperly set as a user\'s login shell. Refer to the \"[Caveats](#Caveats)\" section for how to safely set [fish] as a user\'s default shell.

** Warning**\
[fish] should not be set as the system shell by making it the target of the [/bin/sh] symlink; this could result in an inoperable system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Caveats]](#Caveats)
    -   [[2.1] [fish as a default shell with Bash as the login shell]](#fish_as_a_default_shell_with_Bash_as_the_login_shell)
    -   [[2.2] [fish as shell with bass to create and import environment]](#fish_as_shell_with_bass_to_create_and_import_environment)
    -   [[2.3] [Setting the fish shell as the login shell]](#Setting_the_fish_shell_as_the_login_shell)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Completions]](#Completions)
    -   [[3.2] [Environment variables]](#Environment_variables)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Autocomplete for Portage Packages]](#Autocomplete_for_Portage_Packages)
    -   [[4.2] [Using fish with Nix]](#Using_fish_with_Nix)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Garbled display]](#Garbled_display)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/fish](https://packages.gentoo.org/packages/app-shells/fish) [[]] [Friendly Interactive SHell]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`nls`](https://packages.gentoo.org/useflags/nls)       Add Native Language Support (using gettext - GNU locale utilities)
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 21:21] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-shells/fish]](https://packages.gentoo.org/packages/app-shells/fish)[]]:

`root `[`#`]`emerge --ask app-shells/fish`

## [Caveats]

In Gentoo, the login shell (the shell started after a user logs in, as defined in [/etc/passwd]) sources [/etc/profile], which in turn sources [/etc/profile.env]. This is needed to set up a functioning Gentoo environment, so a working POSIX shell is essential (refer to \"[Login shell in Gentoo](https://wiki.gentoo.org/wiki/Login#Login_shell_in_Gentoo "Login")\" for details).

[fish] can *not* read these files, as it is not POSIX-compatible. Thus it is *strongly advised not to set [fish] as the login shell for any user*.

There is no reliable way to avoid this (see [[[bug #545830]](https://bugs.gentoo.org/show_bug.cgi?id=545830)[]]). However, there is a way to use [fish] by default, as explained in the next section.

Those who nevertheless want to set [fish] as a login shell in [/etc/passwd] can jump down to \"[setting the [fish] shell as the login shell](#Setting_the_fish_shell_as_the_login_shell)\", though this is highly discouraged and can result in difficult issues.

### [[] fish as a default shell with Bash as the login shell]

The following allows the use of [fish] by default, upon login or on starting a terminal emulator. This solution uses [\~/.bashrc] as a wrapper to have [fish] inherit the environment from the login shell, which is left as [Bash](https://wiki.gentoo.org/wiki/Bash "Bash").

Add the following to the user\'s [\~/.bashrc], making sure it\'s placed below the test for an interactive shell, e.g. at the end of the file:

[FILE] **`~/.bashrc`**

    [...]
    # Use fish in place of bash
    # keep this line at the bottom of ~/.bashrc
    [ -x /bin/fish ] && SHELL=/bin/fish exec fish
    # your fish path may also be /usr/bin/fish
    # doublecheck with 'which fish'.

When [bash] is started as an interactive shell, this will automatically launch [fish] for the user, once [bash] has fully initialized the correct system environment. It will also set the `SHELL` environment variable to `/bin/fish` in [fish].

Log into a new [virtual console](https://wiki.gentoo.org/wiki/Terminal_emulator#Virtual_consoles_and_switching "Terminal emulator") to test. Keeping open the current terminal may permit troubleshooting in case of any issue with the new configuration.

** Note**\
When set up this way, launching an interactive [bash] prompt will drop to [fish] because of the line added to [\~/.bashrc]. To launch [bash], ignore [\~/.bashrc] (beware that any commands in [\~/.bashrc] will not be executed):

`user `[`$`]`bash --rcfile /etc/profile`

This solution was suggested [by one of the [fish] developers](https://github.com/fish-shell/fish-shell/issues/3665#issuecomment-268527236), the [Arch wiki](https://wiki.archlinux.org/index.php/Fish#Not_setting_fish_as_default_shell) and Gentoo devs [\[1\]](https://bugs.gentoo.org/545830).

### [fish as shell with bass to create and import environment]

** Note**\
After a long and thorough discussion on [[[bug #545830]](https://bugs.gentoo.org/show_bug.cgi?id=545830)[]] and associated bugs, it was decided to use the [above instructions](#fish_as_default_with_bash) to set fish as the default shell on Gentoo. This solution is potentially less robust, though it may still work.

Once [fish] is installed, install [[bass]](https://github.com/edc/bass), which will permit [fish] to source [/etc/profile] on startup. [bass] is a utility to execute commands in [bash] and relay the environment variable changes to [fish]. The [bass] site has instructions for different [installation methods](https://github.com/edc/bass#installation), such as with the [fisher](https://github.com/jorgebucaran/fisher) plugin manager or [OMF](https://github.com/oh-my-fish/oh-my-fish). We will explain here how to install [bass] manually, as this is the most basic method, however a plugin manager is arguably preferable.

Move into or create a base directory for the [bass] repository, for example:

`user `[`$`]`cd ~/.local/opt`

Clone the [bass] repository (requires [Git](https://wiki.gentoo.org/wiki/Git "Git")), and move into the repository directory:

`user ~/.local/opt $``git clone `[`https://github.com/edc/bass`](https://github.com/edc/bass)`; cd bass`

Install [bass]:

`user ~/.local/opt/bass $``make install`

With [bass], one can now have [fish] inherit the system-wide environment variables on startup, from [bash].

Add the following line to [\~/.config/fish/config.fish], above any other commands that would need the environment to be set up ([config.fish] may need to be created):

[FILE] **`~/.config/fish/config.fish`**

    bass source /etc/profile

Finally, restart [fish] if it is already running.

This solution was suggested [by one of the [fish] developers](https://github.com/fish-shell/fish-shell/issues/3665#issuecomment-268527236) and the [Arch wiki](https://wiki.archlinux.org/index.php/Fish#Not_setting_fish_as_default_shell).

### [Setting the fish shell as the login shell]

** Warning**\
After setting [fish] as the login shell there probably will be entries missing in the `PATH` variable and some packages that rely on [/etc/profile.d] will be broken.

Those who really wish to make [fish] their login shell can still technically do so. This is not recommended and can result in a broken system:

`user `[`$`]`chsh -s /bin/fish`

## [Configuration]

[fish] starts by executing commands in [\~/.config/fish/config.fish]. The file can be created if it does not exist.

Since version 2.0, it is possible to configure [fish] from a Web browser session by running:

`user `[`$`]`fish_config`

### [Completions]

[fish] can generate completions from man pages. To generate completions run:

`user `[`$`]`fish_update_completions`

### [Environment variables]

The [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") explains how to set environment variables globally, for all users, and for the default shell (Bash).

Fish shell sets environment variables in a different way:

[FILE] **`~/.config/fish/config.fish`Append the PATH variable for fish shell**

    set -gx PATH "$PATH:$HOME/.local/bin:"

## [Tips]

### [Autocomplete for Portage Packages]

The autocomplete code for finding Portage packages ([source](https://github.com/fish-shell/fish-shell/blob/master/share/functions/__fish_print_portage_packages.fish)) works best if [Eix](https://wiki.gentoo.org/wiki/Eix "Eix") is installed.

### [Using fish with Nix]

The [\~/.bashrc] method from the \"fish as a default shell with bash as the login shell\" section above prevents [nix-shell] from applying its environment variable configuration. [Nix](https://nixos.org/) users can use the following variant to work around this problem by disabling fish execution within a nix-shell:

[FILE] **`~/.bashrc`**

    [...]
    # Use fish in place of bash
    # keep this line at the bottom of ~/.bashrc
    [ -x /bin/fish ] && [ -z "$IN_NIX_SHELL" ] && SHELL=/bin/fish exec fish

With this configuration in place, running [nix-shell] will result in a Bash shell. To start a nix-shell with [fish], use [nix-shell \--command fish], which will correctly apply the Nix environment before launching [fish].

## [Troubleshooting]

### [Garbled display]

The output of a shell can, in some conditions, become corrupt. Refer to the \"[terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator")\" article for instructions to help fix this.

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") --- a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell").
-   [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") --- an interactive login shell that can also be used as a powerful scripting language interpreter.
-   [Nushell](https://wiki.gentoo.org/wiki/Nushell "Nushell") --- a new kind of [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and Windows.

## [External resources]

-   [fish first steps tutorial](https://fishshell.com/docs/current/tutorial.html)
-   [fish related question on stackoverflow](https://stackoverflow.com/questions/tagged/fish)
-   [arch-wiki fish entry](https://wiki.archlinux.org/index.php/Fish)
-   [fish faq](https://fishshell.com/docs/current/faq.html)