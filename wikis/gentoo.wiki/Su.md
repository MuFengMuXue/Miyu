Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Su/de "Su (26% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Su/hu "Su (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Su/ru "su (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Su/ja "su (100% translated)")

**Resources**

[[]][Home](http://pkg-shadow.alioth.debian.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Su_(Unix) "wikipedia:Su (Unix)")

[[]][Man page](http://man7.org/linux/man-pages/man1/su.1@@shadow-utils.html)

The **[su]** (**s**ubstitute **u**ser) command can be used to adopt the privileges of other users from the system.

The command is provided by the [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux") package, that has the [[[su]](https://packages.gentoo.org/useflags/su)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") enabled by default. The su command is also available with [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]], that also has a [[[su]](https://packages.gentoo.org/useflags/su)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag. Avoid installing both these commands simultaneously.

## Contents

-   [[1] [Caveats]](#Caveats)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Adopt root privileges]](#Adopt_root_privileges)
    -   [[2.2] [Adopt another user\'s privileges]](#Adopt_another_user.27s_privileges)
-   [[3] [See also]](#See_also)

## [Caveats]

The use of [su] to access the user [root] is only permitted when the calling user is a member of the user group [wheel].

In the next example the user *john* is added to the user group [wheel].

`root `[`#`]`usermod -aG wheel john`

## [Usage]

`user `[`$`]`su --help`

    Usage:
     su [options] [-] [<user> [<argument>...]]

    Change the effective user ID and group ID to that of <user>.
    A mere - implies -l.  If <user> is not given, root is assumed.

    Options:
     -m, -p, --preserve-environment      do not reset environment variables
     -w, --whitelist-environment <list>  don't reset specified variables

     -g, --group <group>             specify the primary group
     -G, --supp-group <group>        specify a supplemental group

     -, -l, --login                  make the shell a login shell
     -c, --command <command>         pass a single command to the shell with -c
     --session-command <command>     pass a single command to the shell with -c
                                       and do not create a new session
     -f, --fast                      pass -f to the shell (for csh or tcsh)
     -s, --shell <shell>             run <shell> if /etc/shells allows it
     -P, --pty                       create a new pseudo-terminal

     -h, --help                      display this help
     -V, --version                   display version

    For more details see su(1).

### [Adopt root privileges]

[su] will run commands as root by default. Since not specifying a username will cause [su] to ask for root privileges, the following command will run as root and halt the system:

`user `[`$`]`su -c 'shutdown -h now'`

** Tip**\
It is best practice to encapsulate the commands following the `-c` option with either single or double quotes.

### [][Adopt another user\'s privileges]

It is also possible to specify a user other than root to substitute commands. The following example will run the command [echo] as the user larry:

`user `[`$`]`su -c 'echo "Moo to the Gentoo Wiki reader out there!"' larry`

## [See also]

-   [doas](https://wiki.gentoo.org/wiki/Doas "Doas") --- provides a way to perform commands as another user.
-   [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo") --- provides a simple and secure way to configure privilege escalation