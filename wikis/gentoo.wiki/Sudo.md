This page contains [[changes](https://wiki.gentoo.org/index.php?title=Sudo&oldid=1422032&diff=1441739)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Sudo/es "Sudo (60% translated)")
-   [français](https://wiki.gentoo.org/wiki/Sudo/fr "sudo (64% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Sudo/it "Sudo (78% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Sudo/hu "sudo (99% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Sudo/sv "sudo (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Sudo/ru "sudo (99% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Sudo/zh-cn "Sudo (40% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Sudo/ja "sudo (99% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Sudo/ko "Sudo (34% translated)")

**Resources**

[[]][Home](https://www.sudo.ws/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/sudo "wikipedia:sudo")

[[]][Package information](https://packages.gentoo.org/packages/app-admin/sudo)

[[]][GitWeb](https://www.sudo.ws/repos/sudo)

The [sudo] command provides a simple and secure way to configure privilege escalation --- i.e., letting normal users execute certain (or even all) commands as [root] or as another user, either with or without giving a password.

To allow some users to perform certain administrative steps on a system without granting them total [root access](https://en.wikipedia.org/wiki/Superuser "wikipedia:Superuser"), using [sudo] is the best option. Using [sudo] allows control over who can do what.

This article is meant as a quick introduction - the [[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]] package is a lot more powerful than what is described here. It has special features for editing files as a different user ([sudoedit]), running from within a script (so it can background, read the password from standard input instead of the keyboard, etc.), etc.

Please read the [sudo] and [sudoers] manual pages for more information.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Logging activity]](#Logging_activity)
    -   [[2.2] [Granting permissions]](#Granting_permissions)
    -   [[2.3] [Basic syntax]](#Basic_syntax)
    -   [[2.4] [Basic syntax with LDAP]](#Basic_syntax_with_LDAP)
    -   [[2.5] [Using aliases]](#Using_aliases)
    -   [[2.6] [Non-root execution]](#Non-root_execution)
    -   [[2.7] [Passwords and default settings]](#Passwords_and_default_settings)
    -   [[2.8] [Bash completion]](#Bash_completion)
    -   [[2.9] [zsh completion]](#zsh_completion)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Listing privileges]](#Listing_privileges)
    -   [[3.2] [Prolonging password timeout]](#Prolonging_password_timeout)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

** Note**\
sudo is not part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so it must be installed manually, if it is needed.

** Tip**\
The [su](https://wiki.gentoo.org/wiki/Su "Su") command should always be available, in case sudo is not installed.

### [USE flags]

### [USE flags for] [app-admin/sudo](https://packages.gentoo.org/packages/app-admin/sudo) [[]] [Allows users or groups to run commands as other users]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+secure-path`](https://packages.gentoo.org/useflags/+secure-path)   Replace PATH variable with compile time secure paths
  [`+sendmail`](https://packages.gentoo.org/useflags/+sendmail)         Allow sudo to send emails with sendmail
  [`gcrypt`](https://packages.gentoo.org/useflags/gcrypt)               Use message digest functions from dev-libs/libgcrypt instead of sudo\'s
  [`ldap`](https://packages.gentoo.org/useflags/ldap)                   Add LDAP support (Lightweight Directory Access Protocol)
  [`nls`](https://packages.gentoo.org/useflags/nls)                     Add Native Language Support (using gettext - GNU locale utilities)
  [`offensive`](https://packages.gentoo.org/useflags/offensive)         Let sudo print insults when the user types the wrong password
  [`pam`](https://packages.gentoo.org/useflags/pam)                     Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                   Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`skey`](https://packages.gentoo.org/useflags/skey)                   Enable S/Key (Single use password) authentication support
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                     Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`sssd`](https://packages.gentoo.org/useflags/sssd)                   Add System Security Services Daemon support
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)       Verify upstream signatures on distfiles
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-03 22:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/sudo`

## [Configuration]

### [Logging activity]

One additional advantage of [sudo] is that it can [log](https://wiki.gentoo.org/wiki/Logging "Logging") any attempt (successful or not) to run an application. This is very useful when tracking who made that one fatal mistake that took 10 hours to fix :)

** Tip**\
Sudo logs are to be found in [/var/log/auth.log] file.

### [Granting permissions]

The [[[app-admin/sudo]](https://packages.gentoo.org/packages/app-admin/sudo)[]] package allows the system administrator to grant permission to other users to execute one or more applications they would normally have no right to. Unlike using the `setuid` bit on these applications [sudo] gives a more fine-grained control on *who* can execute a certain command and *when*.

With [sudo] a clear list can be made of *who* can execute a certain application. If the [setuid](https://en.wikipedia.org/wiki/setuid "wikipedia:setuid") bit is set on an executable, any user would be able to run the application (or any user of a certain group, depending on the permissions used). With [sudo] the user can (and probably should) be required to provide a password in order to execute the application.

The [sudo] configuration is managed by the [/etc/sudoers] file.

** Warning**\
Only ever use the [visudo] command to edit [/etc/sudoers]. Never edit this file manually with a [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), [shell redirection](https://wiki.gentoo.org/wiki/Bash#Redirection "Bash"), or similar means. In other words, **never** use [nano /etc/sudoers], [vim /etc/sudoers], etc. **Always use *visudo*** - this tool makes sure that no two system administrators are editing this file at the same time, preserves the permissions on the file, and performs some syntax checking to make sure no fatal mistakes can occur in the file.

### [Basic syntax]

The most difficult part of [sudo] is the [/etc/sudoers] syntax. The basic syntax is as follows:

[CODE] **Basic /etc/sudoers syntax**

    user  host = command

This line tells [sudo] that the user, identified by `user` and logged in on the system `host`, can execute the command `command` (which can also be a comma-separated list of allowed commands).

A more real-life example might make this more clear: To allow the user [larry] to execute [emerge] when he is logged in on [localhost]:

[CODE] **Real /etc/sudoers example**

    larry  localhost = /usr/bin/emerge

** Note**\
The hostname must match the name that the [hostname] command returns.

** Note**\
In the simplest case, commands must be fully qualified paths to executables: hence `/usr/bin/emerge` not just `emerge`. Paths can also contain wildcards and may refer to entire directories. See the manpage for details.

** Warning**\
Do not allow a normal user to run an application that can enable them to elevate privileges. For instance, allowing users to execute [[emerge](https://wiki.gentoo.org/wiki/Portage#emerge "Portage")] as root can grant them full root access to the system because [emerge] can be manipulated to change the live file system to the user\'s advantage. If the [sudo] users are not trusted, don\'t grant them any additional rights.

The user name can also be substituted with a group name, in which case the name is prefaced by a `%` sign. For instance, to allow any one in the [wheel] group to execute [emerge]:

[CODE] **Allowing any [wheel] group member to execute [emerge]**

    %wheel  localhost = /usr/bin/emerge

To enable more than one command for a given user on a given machine, multiple commands can be listed on the same line. For instance, to allow [larry] to not only run [emerge] but also [ebuild] and [emerge-webrsync] as root:

[CODE] **Multiple commands**

    larry  localhost = /usr/bin/emerge, /usr/bin/ebuild, /usr/sbin/emerge-webrsync

The precise command line can also be specified (including parameters and arguments) not just the name of the executable. This is useful to restrict the use of a certain tool to a specified set of command options. The [sudo] tool allows [shell](https://wiki.gentoo.org/wiki/Shell "Shell")-style [wildcards](https://en.wikipedia.org/wiki/Wildcard_character "wikipedia:Wildcard character") (AKA meta or glob characters) to be used in path names as well as command-line arguments in the sudoers file. Note that these are *not* regular expressions.

Here is an example of [sudo] from the perspective of a first-time user of the tool who has been granted access to the full power of [emerge]:

`user `[`$`]`sudo emerge -uDN world`

    We trust you have received the usual lecture from the local System
    Administrator. It usually boils down to these three things:

        #1) Respect the privacy of others.
        #2) Think before you type.
        #3) With great power comes great responsibility.

    Password: ## (Enter the user password, not root!)

The password that [sudo] requires is the user\'s own password. This is to make sure that no terminal that is accidentally left open to others is abused for malicious purposes.

** Important**\
[sudo] does not alter the `$` variable: any command placed after [sudo] is executed within *the user\'s own environment*. Thus if a user wants to run a tool in [/sbin], for instance, the user must provide [sudo] with the full path of the command, like so:

`user `[`$`]`sudo /usr/sbin/emerge-webrsync`

### [Basic syntax with LDAP]

The `ldap` and `pam` USE flags are needed for the LDAP support.

When using sudo with LDAP, sudo will read configuration from LDAP Server as well. So two files will need to edited.

[FILE] **`/etc/ldap.conf.sudo`Please chmod 400 when done**

    # See ldap.conf(5) and README.LDAP for details
    # This file should only be readable by root

    # supported directives: host, port, ssl, ldap_version
    # uri, binddn, bindpw, sudoers_base, sudoers_debug
    # tls_

    host ldap.example.com
    port 389

    base dc=example,dc=com

    uri ldap://ldap.example.com/
    #uri ldapi://%2fvar%2frun%2fopenldap%2fslapd.sock

    ldap_version 3
    #ssl start_tls

    sudoers_base ou=SUDOers,dc=example,dc=com
    #sudoers_debug 2

    bind_policy soft

[FILE] **`/etc/nsswitch.conf`Please add the sudoers line**

    sudoers:     ldap files

The following LDAP entry will need to added for sudo.

** Note**\
It was design so that the sudoers branch are on top of the tree for security reason. This allows a different access right from LDAP to read/write to this branch

[CODE] **LDAP entry for sudo**

    version: 1
    DN: ou=SUDOers,dc=example,dc=com
    objectClass: organizationalUnit
    objectClass: top
    objectClass: domainRelatedObject
    associatedDomain: example.com
    ou: SUDOers

    DN: cn=defaults,ou=SUDOers,dc=example,dc=com
    objectClass: top
    objectClass: sudoRole
    cn: defaults
    description: Default sudoOption's go here
    sudoOption: env_reset

    DN: cn=root,ou=SUDOers,dc=example,dc=com
    objectClass: top
    objectClass: sudoRole
    cn: root
    sudoCommand: ALL
    sudoHost: ALL
    sudoUser: root

    DN: cn=%wheel,ou=SUDOers,dc=example,dc=com
    objectClass: top
    objectClass: sudoRole
    cn: %wheel
    sudoCommand: ALL
    sudoHost: ALL
    sudoOption: !authenticate
    sudoUser: %wheel

[CODE] **LDAP entry for wheel group**

    version: 1
    DN: cn=wheel,ou=Group,dc=example,dc=com
    objectClass: top
    objectClass: posixGroup
    cn: wheel
    description: Wheel Group
    gidNumber: 10
    memberUid: useradmin1
    memberUid: root

The configuration on the sudoer on LDAP are similar to files with some different. Please read more about sudo with LDAP on the link below.^[\[1\]](#cite_note-1)^

### [Using aliases]

In larger environments having to enter all users over and over again (or hosts, or commands) can be a daunting task. To ease the administration of [/etc/sudoers] *aliases* can be defined. The format to declare aliases is quite simple:

[CODE] **Declaring aliases in /etc/sudoers**

    Host_Alias hostalias = hostname1, hostname2, ...
    User_Alias useralias = user1, user2, ...
    Cmnd_Alias cmndalias = command1, command2, ...

One alias that always works, for any position, is the `ALL` alias (to make a good distinction between aliases and non-aliases it is recommended to use capital letters for aliases). The `ALL` alias is an alias to all possible settings.

A sample use of the `ALL` alias to allow *any* user to execute the [shutdown] command if he is logged on locally is:

[CODE] **Allowing any user to execute shutdown**

    ALL  localhost = /sbin/shutdown

Another example is to allow the user [larry] to execute the [emerge] command as root, regardless of where he is logged in from:

[CODE] **Allowing a user to run an application regardless of his location**

    larry   ALL = /usr/bin/emerge

More interesting is to define a set of users who can run software administrative applications (such as [emerge] and [ebuild]) on the system and a group of administrators who can change the password of any user, except root!

[CODE] **Using aliases for users and commands**

    User_Alias  SOFTWAREMAINTAINERS = larry, john, danny
    User_Alias  PASSWORDMAINTAINERS = larry, sysop
    Cmnd_Alias  SOFTWARECOMMANDS    = /usr/bin/emerge, /usr/bin/ebuild
    Cmnd_Alias  PASSWORDCOMMANDS    = /usr/bin/passwd [a-zA-Z0-9_-]*, !/usr/bin/passwd root

    SOFTWAREMAINTAINERS  localhost = SOFTWARECOMMANDS
    PASSWORDMAINTAINERS  localhost = PASSWORDCOMMANDS

### [Non-root execution]

It is also possible to have a user run an application as a different, non-root user. This can be very interesting when running applications as a different user (for instance [apache] for the web server) and want to allow certain users to perform administrative steps as that user (like killing zombie processes).

Inside [/etc/sudoers] list the user(s) in between `(` and `)` before the command listing:

[CODE] **Non-root execution syntax**

    users  hosts = (run-as) commands

For instance, to allow [larry] to run the [kill] tool as the [apache] or [gorg] user:

[CODE] **Non-root execution example**

    Cmnd_Alias KILL = /bin/kill, /usr/bin/pkill

    larry   ALL = (apache, gorg) KILL

With this set, the user can run [sudo -u] to select the user he wants to run the application as:

`user `[`$`]`sudo -u apache pkill apache`

An alias can be set for the user to run an application as using the `Runas_Alias` directive. Its use is identical to the other `_Alias` directives we have seen before.

### [Passwords and default settings]

By default, [sudo] asks the user to identify himself using his own password. Once a password is entered, [sudo] remembers it for 5 minutes, allowing the user to focus on his tasks and not repeatedly re-entering his password.

Of course, this behavior can be changed: set the `Defaults:` directive in [/etc/sudoers] to change the default behavior for a user.

For instance, to change the default 5 minutes to 0 (never remember):

[CODE] **Changing the timeout value**

    Defaults:larry  timestamp_timeout=0

A setting of `-1` would remember the password indefinitely (until the system reboots).

A different setting would be to require the password of the user that the command should be run as and not the users\' personal password. This is accomplished using `runaspw`. In the following example we also set the number of retries (how many times the user can re-enter a password before [sudo] fails) to `2` instead of the default 3:

[CODE] **Requiring the root password instead of the user\'s password**

    Defaults:john   runaspw, passwd_tries=2

Another interesting feature is to keep the `DISPLAY` variable set so that graphical tools can be executed:

[CODE] **Keeping the DISPLAY variable alive**

    Defaults:john env_keep=DISPLAY

Dozens of default settings can changed using the `Defaults:` directive. Fire up the [sudoers] manual page and search for `Defaults`.

To allow a user to run a certain set of commands without providing any password whatsoever, start the commands with `NOPASSWD:`, like so:

[CODE] **Allowing emerge to be run as root without asking for a password**

    larry     localhost = NOPASSWD: /usr/bin/emerge

### [Bash completion]

Users that want bash completion with sudo should ensure that the [[[app-shells/bash-completion]](https://packages.gentoo.org/packages/app-shells/bash-completion)[]] package is installed.

`root `[`#`]`emerge --ask app-shells/bash-completion`

### [zsh completion]

Users that want zsh completion with sudo should install the [[[app-shells/zsh-completions]](https://packages.gentoo.org/packages/app-shells/zsh-completions)[]] package.

`root `[`#`]`emerge --ask app-shells/zsh-completions`

## [Usage]

### [Listing privileges]

To list the current user\'s capabilities, run [sudo -l] :

`user `[`$`]`sudo -l`

    User larry may run the following commands on this host:
        (root)   /usr/libexec/xfsm-shutdown-helper
        (root)   /usr/bin/emerge
        (root)   /usr/bin/passwd [a-zA-Z0-9_-]*
        (root)   !/usr/bin/passwd root
        (apache) /usr/bin/pkill
        (apache) /bin/kill

Any command in [/etc/sudoers] that does not require a password to be entered, a password will not be required to list the entries either. Otherwise sudo will ask for a password if it isn\'t remembered.

### [Prolonging password timeout]

By default, if a user has entered their password to authenticate their self to [sudo], it is remembered for 5 minutes. If the user wants to prolong this period, he can run [sudo -v] to reset the time stamp so that it will take another 5 minutes before [sudo] asks for the password again.

`user `[`$`]`sudo -v`

The inverse is to kill the time stamp using [sudo -k].

## [See also]

-   [doas](https://wiki.gentoo.org/wiki/Doas "Doas") --- provides a way to perform commands as another user.
-   [su](https://wiki.gentoo.org/wiki/Su "Su") --- used to adopt the privileges of other users from the system

## [References]

1.  [[[↑](#cite_ref-1)] [[Sudoers LDAP Manual](https://www.sudo.ws/man/sudoers.ldap.man.html)]]