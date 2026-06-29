**Resources**

[[]][Home](https://www.zsh.org/)

[[]][Official documentation](https://zsh.sourceforge.io/Doc/Release/zsh_toc.html)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/zsh)

[[]][Guide](https://wiki.gentoo.org/wiki/Zsh/Guide "Zsh/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zsh "wikipedia:Zsh")

[[]][GitWeb](http://sourceforge.net/p/zsh/code/ci/master/tree/)

[[]][[#zsh](ircs://irc.libera.chat/#zsh)] ([[webchat](https://web.libera.chat/#zsh)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/zsh)

[zsh] (**Z sh**ell) is an interactive login shell that can also be used as a powerful scripting language interpreter. It is similar to [bash](https://wiki.gentoo.org/wiki/Bash "Bash") and the Korn shell, but offers extensive configurability, powerful command-line completion, file globbing, and spelling correction.

See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#General_usage "Terminal emulator") article for some general usage pointers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Add-ons]](#Add-ons)
        -   [[1.3.1] [app-shells/zsh-completions]](#app-shells.2Fzsh-completions)
        -   [[1.3.2] [app-shells/gentoo-zsh-completions]](#app-shells.2Fgentoo-zsh-completions)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Setting zsh as the default shell]](#Setting_zsh_as_the_default_shell)
    -   [[2.3] [File]](#File)
    -   [[2.4] [Scripting]](#Scripting)
    -   [[2.5] [oh-my-zsh]](#oh-my-zsh)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Inactive keys]](#Inactive_keys)
-   [[5] [Troubleshooting]](#Troubleshooting_2)
    -   [[5.1] [Garbled display]](#Garbled_display)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/zsh](https://packages.gentoo.org/packages/app-shells/zsh) [[]] [UNIX Shell similar to the Korn shell]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`caps`](https://packages.gentoo.org/useflags/caps)           Use Linux capabilities library to control privilege
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`examples`](https://packages.gentoo.org/useflags/examples)   Install examples, usually source code
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)           Add support for sys-libs/gdbm (GNU database libraries)
  [`maildir`](https://packages.gentoo.org/useflags/maildir)     Add support for maildir (\~/.maildir) style mail spools
  [`pcre`](https://packages.gentoo.org/useflags/pcre)           Add support for Perl Compatible Regular Expressions
  [`static`](https://packages.gentoo.org/useflags/static)       !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)   Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-shells/zsh]](https://packages.gentoo.org/packages/app-shells/zsh)[]]:

`root `[`#`]`emerge --ask app-shells/zsh`

### [Add-ons]

#### [][app-shells/zsh-completions]

Emerging [[[app-shells/zsh-completions]](https://packages.gentoo.org/packages/app-shells/zsh-completions)[]] enables auto-completion for arguments of commands, which is one of the advantages [zsh] has over other shells:

`root `[`#`]`emerge --ask app-shells/zsh-completions`

** Note**\
To enable auto-completion globally (for most programs), add \'zsh-completion\' to the `USE` variable in [/etc/portage/make.conf]

#### [][app-shells/gentoo-zsh-completions]

Emerging [[[app-shells/gentoo-zsh-completions]](https://packages.gentoo.org/packages/app-shells/gentoo-zsh-completions)[]] enables Gentoo specific auto-completion for arguments of Portage and other Gentoo commands:

`root `[`#`]`emerge --ask app-shells/gentoo-zsh-completions`

When installing this package be sure to add the following to the respective [\~/.zshrc] files:

[FILE] **`~/.zshrc`Enabling Portage completions and Gentoo prompt for [zsh]**

    autoload -U compinit promptinit
    compinit
    promptinit; prompt gentoo

To enable a cache for the completions add:

[FILE] **`~/.zshrc`Enabling cache for the completions for [zsh]**

    zstyle ':completion::complete:*' use-cache 1

## [Configuration]

### [Invocation]

`user `[`$`]`zsh`

Upon running [zsh] for the first time as a new user, you will be greeted by a basic configuration dialog. The setup process can be skipped by pressing [q]. If the setup process is skipped [zsh] can be setup manually.

### [Setting [zsh] as the default shell]

To make [zsh] the default shell for a user, run:

`user `[`$`]`chsh -s /bin/zsh`

Note that this method is fine, but trying to use [zsh] as [/bin/sh] is strongly discouraged as it has issues in POSIX emulation mode. For example, glibc may fail to build: [[[bug #804645]](https://bugs.gentoo.org/show_bug.cgi?id=804645)[]]. If trying to minimise use of Bash on the system, consider [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") for [/bin/sh].

### [File]

[zsh]\'s main configuration file is located in each user\'s home directory at [\~/.zshrc]. Reload this file in running shells for the changes to take effect:

`user `[`$`]`source ~/.zshrc`

** Note**\
Reloading via the [source] command is only necessary when instances of [zsh] are already in memory *after* changes are made to the shell\'s configuration file.

### [Scripting]

Launch scripts can be made in each user\'s home directory at [\~/.zprofile]. This file is executed when Zsh starts as a login shell. The [\~/.zprofile] file may need to be created:

`user `[`$`]`touch ~/.zprofile`

### [oh-my-zsh]

The zsh community created numerous tweaks, the easiest way to acquire them is to install [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) framework. It contains handy plugins and eye [candy themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes), and makes their configuration very easy. However you should always consider the security risk involving running code outside of Gentoo developers jurisdiction.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-shells/zsh`

## [Troubleshooting]

### [Inactive keys]

If the [Home] or [End] or [Del] key does not work, try entering keybindings into the user\'s \`\~/.zshrc\` such as examples in [ArchWiki](https://wiki.archlinux.org/index.php/Zsh#Key_bindings).

## [Troubleshooting]

### [Garbled display]

The output of a shell can, in some conditions, become corrupt. See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator") article for instructions to help fix this.

## [See also]

-   [Zsh/Guide](https://wiki.gentoo.org/wiki/Zsh/Guide "Zsh/Guide") --- details installation, configuration, and light usage functionality for zsh.
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") --- a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell").
-   [Fish](https://wiki.gentoo.org/wiki/Fish "Fish") --- a smart and user-friendly command line [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and the rest of the family.
-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Nushell](https://wiki.gentoo.org/wiki/Nushell "Nushell") --- a new kind of [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and Windows.

## [External resources]

-   [Official [zsh] introduction](http://zsh.sourceforge.net/Intro/intro_toc.html)
-   [Official User\'s Guide](http://zsh.sourceforge.net/Guide/zshguide.html)
-   [[zsh] Documentation in various formats](http://zsh.sourceforge.net/Doc/)
-   [[zsh] FAQ](http://zsh.sourceforge.net/FAQ/zshfaq.html)
-   [[zsh] Wiki](http://zshwiki.org/home/start)
-   [[zsh] Lovers](http://grml.org/zsh/zsh-lovers.html)
-   [GRML [zsh] Configuration](http://grml.org/zsh/)
-   [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/wiki)
-   [Sorin Ionescu maintained oh-my-zsh fork now called prezto - The configuration framework for [zsh]](https://github.com/sorin-ionescu/prezto)
-   [ArchWiki [zsh] page](https://wiki.archlinux.org/index.php/Zsh)