**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-admin/doas)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Doas "wikipedia:Doas")

[[]][GitHub](https://github.com/Duncaen/OpenDoas)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/OpenDoas)

[[]][doas(1)](https://man.openbsd.org/doas)

[[]][doas.conf(5)](https://man.openbsd.org/doas.conf)

The **doas** command provides a way to perform commands as another user. It aims to be a a simplified and lightweight replacement for [[sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo")]. The [doas] tool was originally written for [OpenBSD](https://www.openbsd.org/) by Ted Unangst. *OpenDoas* is a port of [doas] for Linux, which is available as the [[[app-admin/doas]](https://packages.gentoo.org/packages/app-admin/doas)[]] package.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [Basic configuration]](#Basic_configuration)
    -   [[2.3] [Authentication]](#Authentication)
        -   [[2.3.1] [Persist]](#Persist)
    -   [[2.4] [Commands]](#Commands)
    -   [[2.5] [Environment variables]](#Environment_variables)
    -   [[2.6] [Testing]](#Testing)
    -   [[2.7] [Targets]](#Targets)
    -   [[2.8] [Bash tab completion]](#Bash_tab_completion)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/doas](https://packages.gentoo.org/packages/app-admin/doas) [[]] [Run commands as super/another user (alt sudo) (unofficial port from OpenBSD)]

  ----------------------------------------------------------- ----------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`persist`](https://packages.gentoo.org/useflags/persist)   Adds support for \"persist\" feature (experimental)
  ----------------------------------------------------------- ----------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-03-12 18:14] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/doas`

## [Configuration]

The [doas] tool is configured by the ruleset specified in [/etc/doas.conf]. By using an empty configuration file the default ruleset will be applied which denies all actions.

### [Permissions]

Create a empty [/etc/doas.conf] file:

`root `[`#`]`touch /etc/doas.conf`

Set the recommended ownership and permissions for the [/etc/doas.conf] file:

`root `[`#`]`chown -c root:root /etc/doas.conf`

`root `[`#`]`chmod -c 0400 /etc/doas.conf`

### [Basic configuration]

A simple skeleton configuration could be to specify a rule which allows all users in the [wheel] group to perform any action as root.

[FILE] **`/etc/doas.conf`Allow all users in the [wheel] group to execute any command as root**

    permit :wheel

It\'s also possible to deny certain actions to specified users. The ruleset is evaluated in a hierarchical manner, thus adding a new rule can override the previous one:

[FILE] **`/etc/doas.conf`Deny a user to execute a command**

    permit :wheel
    deny larry cmd fdisk

The user [larry] is part of the [wheel] group and therefore may perform actions available to root, but the second rule denies this user access to the [fdisk] command.

### [Authentication]

The [nopass] keyword provides the ability for users in a certain group to perform elevated actions without having to enter a password:

[FILE] **`/etc/doas.conf`Allow all users in the [wheel] group to perform actions as root without authentication**

    permit nopass :wheel

#### [Persist]

** Note**\
Due to OpenBSD-specific kernel API required by [doas] to set and clear timeouts, the persist feature is disabled by default in the *OpenDoas* port.

Using the [persist] keyword [doas] can remember an authenticated user and will not require confirmation by password for a time period of five minutes after the last [doas] command was entered in the terminal window:

[FILE] **`/etc/doas.conf`Do not require passwords for five minutes for all users in the [wheel] group**

    permit persist :wheel

Note: Persist support is enabled via the `persist` USE flag on [[[app-admin/doas]](https://packages.gentoo.org/packages/app-admin/doas)[]]

### [Commands]

The [doas] tool allows the creation of rules which only apply to certain commands.

A rule can be specified to allow a certain user to use a command only available to root:

[FILE] **`/etc/doas.conf`Allow a user to use the [reboot] command without a password**

    permit nopass larry cmd /sbin/reboot

** Tip**\
For security reasons, *OpenDoas* recommends specifying absolute paths like shown above. However, [doas] can use the target user\'s [PATH](https://wiki.gentoo.org/wiki/Handbook:X86/Working/EnvVar "Handbook:X86/Working/EnvVar") in execution. When configuring `permit nopass larry cmd reboot` instead, [larry] does not need to specify the directory path.

This allows the user [larry] to execute [doas /sbin/reboot] without having to enter a password. This may allow users to use restricted commands without providing complete root access.

### [Environment variables]

By default, [doas] creates a new environment for the program. This behavior may be overridden with the [setenv] and [keepenv] keywords:

[FILE] **`/etc/doas.conf`Preserve [LANG], [LC_ALL], and [PATH]**

    permit setenv  :wheel

[FILE] **`/etc/doas.conf`Override [PATH]**

    permit setenv  :wheel

[FILE] **`/etc/doas.conf`Preserve all environment variables**

    permit keepenv :wheel

### [Testing]

A configuration file can be tested as follows:

`user `[`$`]`doas -C /etc/doas.conf`

Specifying a command to test if the currently running user has permissions to perform a specific command:

`user `[`$`]`doas -C /etc/doas.conf cat`

This test will output [deny] if the currently running user does not have the permissions to execute the [cat] command.

Permissions can be checked for a specified user via:

`user `[`$`]`doas -C /etc/doas.conf cat -u larry`

If the user [larry] has permissions to access [cat] it may output [permit].

### [Targets]

The [doas] can not only be used to perform actions with root privileges, it also allows to target certain users.

[FILE] **`/etc/doas.conf`Allow a user to perform actions as another user**

    permit nopass larry as postgres

By adding this rule, the user [larry] is allowed to perform actions as the [postgres] user without having to enter a password.

### [Bash tab completion]

By default [bash] will only tab complete files and directories within the current or referenced directory. To tell bash to complete arguments as if they were separate commands (also leveraging the tab completion settings of other commands) the following can be added to either the users [.bashrc], or the global [/etc/bashrc].

[FILE] **`~/.bashrc`Configure tab completion**

    #     Complete arguments as if they were commands
    #     (eg: `doas emer<tab>` -> `doas emerge`)
    #     (eg: `doas dd status=p<tab>` -> `doas dd status=progress`)
    #    Complete arguments as if they were directory names (default behavior)
    #     (eg: `doas /bi<tab>` -> `doas /bin/`)
    # If you have app-shells/bash-completion installed
    complete -F _root_command doas
    # Alternative that doesn't require app-shells/bash-completion
    # However this doesn't complete arguments, among other things
    complete -cf doas

## [Usage]

The [doas] command can be used like [sudo]:

`user `[`$`]`doas emerge -uDN @world`

See [doas(1)](https://man.openbsd.org/doas) for more information.

## [See also]

-   [su](https://wiki.gentoo.org/wiki/Su "Su") --- used to adopt the privileges of other users from the system
-   [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo") --- provides a simple and secure way to configure privilege escalation

## [External resources]

-   [doas configuration file man page](https://man.openbsd.org/doas.conf.5)