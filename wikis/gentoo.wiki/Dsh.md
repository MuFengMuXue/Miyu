[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dsh&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.netfort.gr.jp/~dancer/software/dsh.html.en)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/dsh)

**[dsh]** is a shell that allows parallel execution of remote commands across large numbers of servers. Generally called \"distributed shell\" [dsh] was often leveraged as an orchestration tool prior to the rise of modern alternatives. Even to this day, [dsh] is still used by some system administrators where heavyweight tools such as [Ansible](https://wiki.gentoo.org/wiki/Ansible "Ansible") are impractical or inefficient.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [Global Configuration Files]](#Global_Configuration_Files)
        -   [[2.2.2] [User Specific Configuration Files]](#User_Specific_Configuration_Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/dsh](https://packages.gentoo.org/packages/app-shells/dsh) [[]] [Distributed Shell]

  --------------------------------------------------- --------------------------------------------------------------------
  [`nls`](https://packages.gentoo.org/useflags/nls)   Add Native Language Support (using gettext - GNU locale utilities)
  --------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-shells/dsh`

## [Configuration]

### [Environment variables]

-   `$DSH_FANOUT` - the maximum number of concurrent remote shell commands
-   `$DSH_REMOTE_CMD` - used to specify a remote shell other than the default [[rsh](https://wiki.gentoo.org/index.php?title=Rsh&action=edit&redlink=1 "Rsh (page does not exist)")], typically [[ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh")].
-   `$DSH_NODE_LIST` - the location of the host list.
-   `$WCOLL` - (deprecated) the location of the host list.
-   `$DSH_PATH` - the default path for remote command execution, `$PATH` by default.

### [Files]

#### [Global Configuration Files]

-   [/etc/dsh/machines.list] - the list of machine names to be used for when `-a` command-line option is specified.
-   [/etc/dsh/group/\<group_name\>] - the list of machine names to be used for when `-g` group name command-line option is specified.
-   [/etc/dsh/dsh.conf] - the configuration file containing the day-to-day default.

#### [User Specific Configuration Files]

-   [\$HOME/.dsh/machines.list] - the list of machine names to be used for when `-a` command-line option is specified.
-   [\$HOME/.dsh/group/\<group_name\>] - the list of machine names to be used for when `-g` group name command-line option is specified.
-   [\$HOME/.dsh/dsh.conf] - the configuration file containing the day-to-day default.

## [Usage]

First, tell [dsh] where to find the server list:

`user `[`$`]`DSH_NODE_LIST=~/<server.list>`

Second, tell [dsh] what command to run:

`user `[`$`]`dsh -v '<remote_command>'`

** Note**\
Without the `-v` (verbose) flag remote commands will be executed but no output will be visible to the user.

### [Invocation]

`user `[`$`]`dsh --help`

    Distributed Shell / Dancer's shell version 0.25.10
    Copyright 2001-2005 Junichi Uekawa,
    distributed under the terms and conditions of GPL version 2

    -v --verbose                   Verbose output
    -q --quiet                     Quiet
    -M --show-machine-names        Prepend the host name on output
    -H --hide-machine-names        Do not prepend host name on output
    -i --duplicate-input           Duplicate input given to dsh
    -b --bufsize                   Change buffer size used in input duplication
    -m --machine [machinename]     Execute on machine
    -n --num-topology              How to divide the machines
    -a --all                       Execute on all machines
    -g --group [groupname]         Execute on group member
    -f --file [file]               Use the file as list of machines
    -r --remoteshell [shellname]   Execute using shell (rsh/ssh)
    -o --remoteshellopt [option]   Option to give to shell
    -h --help                      Give out this message
    -w --wait-shell                Sequentially execute shell
    -c --concurrent-shell          Execute shell concurrently
    -F --forklimit [fork limit]    Concurrent with limit on number
    -V --version                   Give out version information

## [See also]

-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Ansible](https://wiki.gentoo.org/wiki/Ansible "Ansible") --- an agentless automation system written in [Python](https://wiki.gentoo.org/wiki/Python "Python").
-   [Rex](https://wiki.gentoo.org/wiki/Rex "Rex") --- a configuration automation framework written in [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") known for its shallow learning curve and ease of extensibility
-   [Sparrow](https://wiki.gentoo.org/index.php?title=Sparrow&action=edit&redlink=1 "Sparrow (page does not exist)")