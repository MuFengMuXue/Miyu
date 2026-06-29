Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Monit/hu "monit (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Monit/ru "Monit (44% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Monit/zh-cn "Monit (91% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Monit/ja "Monit (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Monit/ko "Monit/ko (69% translated)")

**Resources**

[[]][Home](https://mmonit.com/monit/)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/monit)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Monit "wikipedia:Monit")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/monit)

**monit** is a utility for managing and monitoring processes, programs, files, directories and filesystems on a UNIX system.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Installing monit]](#Installing_monit)
    -   [[1.2] [Monit configuration files]](#Monit_configuration_files)
    -   [[1.3] [Automatically starting monit at boot]](#Automatically_starting_monit_at_boot)
    -   [[1.4] [User management]](#User_management)
    -   [[1.5] [Monit web interface]](#Monit_web_interface)
-   [[2] [Monitoring applications through monit]](#Monitoring_applications_through_monit)
-   [[3] [Debugging monit]](#Debugging_monit)
    -   [[3.1] [Running monit in the foreground]](#Running_monit_in_the_foreground)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Configuration]

### [Installing monit]

The [[[app-admin/monit]](https://packages.gentoo.org/packages/app-admin/monit)[]] application has the following USE flags:

### [USE flags for] [app-admin/monit](https://packages.gentoo.org/packages/app-admin/monit) [[]] [Monitoring and managing daemons or similar programs running on a Unix system]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)           Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 21:56] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Once the USE flags are properly determined, install [[[app-admin/monit]](https://packages.gentoo.org/packages/app-admin/monit)[]] through [emerge]:

`root `[`#`]`emerge --ask app-admin/monit`

### [Monit configuration files]

The Monit application uses [/etc/monitrc] as its configuration file.

To make adding and removing monitoring definitions easy, [monit] supports including files inside a specified directory (usually [/etc/monit.d]. To enable this, edit [/etc/monitrc] like so:

[FILE] **`/etc/monitrc`Allowing flexible configuration entries**

    ## It is possible to include additional configuration parts from other files or
    ## directories.
    include /etc/monit.d/*

When a Monit related configuration file is altered, tell [monit] to reread its configuration settings:

`root `[`#`]`monit reload`

### [Automatically starting monit at boot]

It is recommended to start [monit] through the [/etc/inittab] so that [init] itself launches the [monit] application, and will automatically relaunch it when [monit] would suddenly die. Starting [monit] through an init script would not provide this functionality.

[FILE] **`/etc/inittab`Auto restart monit in case of failure**

    # Run monit in standard runlevels
    mo:2345:respawn:/usr/bin/monit -Ic /etc/monitrc

After updating [/etc/inittab], [monit] can be immediately started through [telinit q].

### [User management]

Users added to the [monit] or [users] group will be able to manipulate [monit] through its web interface.

To add users to one of these groups, use [gpasswd] (note, replace `$` by the user\'s actual login name):

`root `[`#`]`gpasswd -a $ monit `

`root `[`#`]`gpasswd -a $ users`

Inside the [/etc/monitrc] file, the `allow` statement should refer to these groups, like so:

[FILE] **`/etc/monitrc`Granting groups access to the web interface**

    set httpd port 2812
      allow @monit
      allow @users

It is also possible to hard-code usernames and passwords in the [monitrc] file, but this is not recommended. Check the [monitrc] file for default passwords and remove those, or alter them to use a strong, unique password. The syntax used then is `allow <username>:`.

### [Monit web interface]

The default location of the web interface is at [localhost:2812](http://localhost:2812), with `admin` as admin username and `monit` as default password. Make sure to change this!

## [Monitoring applications through monit]

The Monit application uses PID file checks to see if an application is still running or not. That implies that a PID file *must* be available for an application, otherwise [monit] cannot guard it. If a daemon does not create a PID file, use a [wrapper](https://mmonit.com/wiki/Monit/FAQ#pidfile) to create one.

** Note**\
The use of PID files (and validating PIDs from tools like [ps]) for monitoring is often said to be broken^[\[1\]](#cite_note-1)^. Monit does try to overcome this weakness by checking the PID file frequently enough to be reliable.

Through using the [/etc/monit.d/] location, it is easy to add in additional monitoring rules.

For instance, to automatically restart [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") when it would die:

[FILE] **`/etc/monit.d/mysql`Auto restart mysql**

    check process mysql with pidfile /var/run/mysqld/mysqld.pid
        start program = "/bin/bash -c 'rc-service mysql start'"
        stop program  = "/bin/bash -c 'rc-service mysql stop'"

Another example is to manage the memory usage of a process and create an alert when it grows beyond a certain threshold:

[FILE] **`/etc/monit.d/squid`Check squid and alert on memory consumption bigger than 512 MByte**

    check process squid with pidfile /run/squid.pid
       start program = "/bin/bash -c 'rc-service squid start'"
       stop  program = "/bin/bash -c 'rc-service squid stop'"
       if totalmem > 512 MB then alert

## [Debugging monit]

### [Running monit in the foreground]

To run [monit] in the foreground and provide feedback on everything it is detecting, use the `-Ivv` option:

`root `[`#`]`monit -Ivv`

    ...
    'squid' total mem amount of 525748kB matches resource limit [total mem amount>524288kB]

## [External resources]

For more information about Monit, the following resources can help out.

-   [Monit official documentation](https://mmonit.com/monit/documentation/monit.html)
-   [Monit Wiki](https://mmonit.com/wiki/Main/HomePage)
-   [Configuring Monit for Avahi](https://wiki.amahi.org/index.php/Monit)

## [References]

1.  [[[↑](#cite_ref-1)] [Greg Wooledge. [Process management](http://mywiki.wooledge.org/ProcessManagement), Retrieved on January 1st, 2015]]