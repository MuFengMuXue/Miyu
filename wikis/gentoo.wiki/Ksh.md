**Resources**

[[]][Home](http://www.kornshell.com)

[[]][Official documentation](http://www.kornshell.com/doc/)

[[]][GitHub](https://github.com/ksh93/ksh)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/ksh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/KornShell "wikipedia:KornShell")

**ksh** (**K**orn **sh**ell) is a [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell") developed by David Korn. Gentoo provides ksh93u+m, forked from the original ATT ksh.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [User shell]](#User_shell)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

`root `[`#`]`emerge --ask app-shells/ksh`

## [Configuration]

ksh can be configured via the file [\~/.kshrc], which is executed for interactive shells when `ENV` is not set. Refer to the [man page](https://manpages.debian.org/unstable/ksh93u+m/ksh93.1.en.html) for details.

### [User shell]

Users can make ksh their default shell by using [[[chsh(1)]](https://man.archlinux.org/man/chsh.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

`user `[`$`]`chsh -s /usr/bin/ksh`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-shells/ksh`

## [See also]

-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Dash](https://wiki.gentoo.org/wiki/Dash "Dash") --- a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell").
-   [Dsh](https://wiki.gentoo.org/wiki/Dsh "Dsh") --- a shell that allows parallel execution of remote commands across large numbers of servers
-   [mksh](https://wiki.gentoo.org/wiki/Mksh "Mksh") --- an actively developed free implementation of the Korn Shell programming language and a successor to the Public Domain Korn Shell
-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") --- an interactive login shell that can also be used as a powerful scripting language interpreter.

## [External resources]

-   [Ksh command](https://www.ibm.com/docs/en/aix/7.1?topic=k-ksh-command)