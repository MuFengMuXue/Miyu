This page contains [[changes](https://wiki.gentoo.org/index.php?title=Nushell&oldid=1406478&diff=1428055)] which are not marked for translation.

Other languages:

-   [English]

**Resources**

[[]][Home](https://www.nushell.sh)

[[]][Official documentation](https://www.nushell.sh/book)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/nushell)

[[]][GitHub](https://github.com/nushell/nushell)

**Nushell** is a new kind of [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and Windows. Nushell uses structured data allowing for powerful but simple pipelines. It offers great error messages, completions and works with existing datatypes.

** Important**\
As with the [fish](https://wiki.gentoo.org/wiki/Fish "Fish") shell, Nushell is not a [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compatible shell. It could cause issues if improperly set as a user\'s login shell. Refer to the \"[Caveats](https://wiki.gentoo.org/wiki/Nushell#Caveats "Nushell")\" section for how to safely set [nushell] as a user\'s default shell.

** Warning**\
Nushell should not be set as the system shell by making it the target of the [/bin/sh] symlink; this could result in an inoperable system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Caveats]](#Caveats)
-   [[3] [Features]](#Features)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Environment variables]](#Environment_variables)
-   [[5] [Tips]](#Tips)
    -   [[5.1] [SSH agent]](#SSH_agent)
    -   [[5.2] [Using Nushell with Nix]](#Using_Nushell_with_Nix)
    -   [[5.3] [Sudo inside Doom Emacs]](#Sudo_inside_Doom_Emacs)
    -   [[5.4] [Signing Git commit messages with GPG]](#Signing_Git_commit_messages_with_GPG)
    -   [[5.5] [Interactive news item reading]](#Interactive_news_item_reading)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/nushell](https://packages.gentoo.org/packages/app-shells/nushell) [[]] [A new type of shell, written in Rust]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                                 Add support for X11
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`mcp`](https://packages.gentoo.org/useflags/mcp)                             Build MCP server
  [`plugins`](https://packages.gentoo.org/useflags/plugins)                     Build official plugins
  [`system-clipboard`](https://packages.gentoo.org/useflags/system-clipboard)   System clipboard support in \`reedline\`
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 23:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-shells/nushell]](https://packages.gentoo.org/packages/app-shells/nushell)[]]:

`root `[`#`]`emerge --ask app-shells/nushell`

## [Caveats]

Nushell is not [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compatible, thus it is *strongly advised not to set Nushell as the login shell for any user*. Refer to [the discussion for the fish shell](https://wiki.gentoo.org/wiki/Fish#Caveats "Fish") for more details.

A simple working solution is to start [nushell] from the terminal, as advised in [the official documentation](https://www.nushell.sh/book/default_shell.html#setting-nu-as-default-shell-on-your-terminal).

To use [nushell] as the default login shell, [\~/.bashrc] can be used to have [nushell] inherit the environment from the login shell, which is left as Bash. Add the following to the user\'s [\~/.bashrc], making sure it\'s placed below the test for an interactive shell, e.g. at the end of the file:

[FILE] **`~/.bashrc`**

    [...]
    # Use nushell in place of bash
    # keep this line at the bottom of ~/.bashrc
    [ -x /usr/bin/nu ] && SHELL=/usr/bin/nu exec nu

When [bash] is started as an interactive shell, this will automatically launch [nushell] for the user, once [bash] has fully initialized the correct system environment. It will also set the `SHELL` environment variable to `/usr/bin/nu` in [nushell].

## [Features]

In Nushell, data is structured as tables. This allows one to query, filter and sort easily. For example, a search for all Emacs processes can be done with:

`user `[`$`]`ps | name =~ emacs`

List files with older first:

`user `[`$`]`ls | sort-by modified`

Getting the basename of several files:

`user `[`$`]`ls *.png | get name | path parse | get stem`

Applying a command to each line in the table can done using a closure with [each]. Converting all Org-mode files in a directory to Markdown is a good illustration of a closure and string substitution:

`user `[`$`]`ls *.org | each  `

Thanks to string substitution, it allows for complex but natural commands that would have been rather awkward in Bash.

## [Configuration]

Nushell creates a default configuration file in [\~/.config/nushell/config.nu].

Disabling the welcome banner is done with:

[FILE] **`~/.config/nushell/config.nu`**

    $env.config =

Changing the theme requires defining and enabling a theme with:

[FILE] **`~/.config/nushell/config.nu`**

    $env.config =

Due to Nushell development, updates may break the configuration file.

### [Environment variables]

Environment variables can be set up in the current session with:

`user `[`$`]`$env.FOO = 'BAR'`

`PATH` is a list of strings so appending a new location can be done with:

`user `[`$`]`$env.PATH = ($env.PATH | prepend "/home/USER/.juliaup/bin")`

To define environment variables in all sessions, put them in [\~/.config/nushell/env.nu].

## [Tips]

### [SSH agent]

Since `eval` is not available in nushell, [several workarounds exist](https://www.nushell.sh/cookbook/ssh_agent.html#workarounds). One option is to run `ssh-agent` as a user service.

For example, with systemd create:

`~/.config/systemd/user/ssh-agent.service`

    [Unit]
    Description=SSH key agent

    [Service]
    Type=simple
    Environment=SSH_AUTH_SOCK=%t/ssh-agent.socket
    ExecStart=/usr/bin/ssh-agent -D -a $SSH_AUTH_SOCK

    [Install]
    WantedBy=default.target

Then add the following to `~/.bash_profile`:

    export SSH_AUTH_SOCK=/run/user/1000/ssh-agent.socket
    ssh-add "$HOME/.ssh/id_ed25519"

### [Using Nushell with Nix]

The modifications to [\~/.bashrc] described above prevent Nushell from applying its environment variable configuration. [Nix](https://nixos.org/) users can use the following variant to work around this problem by disabling Nushell execution within a nix-shell:

[FILE] **`~/.bashrc`**

    [...]
    # Use nushell in place of bash
    # keep this line at the bottom of ~/.bashrc
    [ -x /usr/bin/nu ] && [ -z "$IN_NIX_SHELL" ] && SHELL=/usr/bin/nu exec nu

With this configuration in place, running [nix-shell] will result in a Bash shell. To start a nix-shell with Nushell, use [nix-shell \--command nushell], which will correctly apply the Nix environment before launching Nushell.

### [Sudo inside Doom Emacs]

Accessing files with [sudo] inside Emacs fails as it cannot run the [/bin/sh -i] command. Setting Emacs\' `shell-file-name` variable to `/bin/bash` does not work. A simple way to get around it is to reconfigure the `SHELL` environment variable for Doom Emacs with:

`user `[`$`]`SHELL="/bin/bash" ~/.emacs.d/bin/doom env`

### [Signing Git commit messages with GPG]

If it fails with [gpg: signing failed: Inappropriate ioctl for device], set `GPG_TTY` to the output of [tty] with:

`user `[`$`]`$env.GPG_TTY = (tty)`

### [Interactive news item reading]

To read [eselect news](https://wiki.gentoo.org/wiki/Eselect#News "Eselect") in a more interactive manner, one could take advantage of Nushell\'s features such as parsing and fuzzy input:

[CODE] **Nushell script to read eselect news**

    eselect --brief news list all
    | parse --regex '\s*(?P<Unread>N)?\s*(?P<Date>\d-\d-\d)\s*(?P<Title>.+)'
    | update Unread  else  }
    | update Date
    | get Title
    | input list --fuzzy --index
    | sudo eselect news read $"($in + 1)"

This could be further customized to only read news from a certain period by adding an additional pipe like [\| where Date \> (date now) - 2wk] to only read items for the past two weeks.

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") --- a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell").
-   [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") --- an interactive login shell that can also be used as a powerful scripting language interpreter.
-   [Fish](https://wiki.gentoo.org/wiki/Fish "Fish") --- a smart and user-friendly command line [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and the rest of the family.

## [External resources]

-   [All Nushell commands](https://www.nushell.sh/commands/)
-   [Useful tips](https://www.nushell.sh/cookbook/)
-   [Nushell-related question on StackOverflow](https://stackoverflow.com/questions/tagged/nushell)
-   [Arch wiki Nushell entry](https://wiki.archlinux.org/index.php/Nushell)