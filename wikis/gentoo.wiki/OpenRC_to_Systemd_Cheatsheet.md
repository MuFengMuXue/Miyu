This page contains [[changes](https://wiki.gentoo.org/index.php?title=OpenRC_to_systemd_Cheatsheet&oldid=1264895&diff=1305757)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet/es "Cheatsheet de OpenRC a systemd (50% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet/it "Cheatsheet da OpenRC a systemd (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet/hu "OpenRC to systemd Cheatsheet (100% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet/ta "OpenRC இல் இருந்த systemd க்கான ஏமாற்றுத்தாள் (50% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/OpenRC_to_systemd_Cheatsheet/ja "OpenRC から systemd へのチートシート (100% translated)")

This article is for users that have recently converted from [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") to [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). It contains a list of commands commonly used in OpenRC and its equivalent systemd command.

** Note**\
The following table is not an exhaustive list and is not intended to replace reading [[man] pages](https://wiki.gentoo.org/wiki/Man_page "Man page").

  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------
  Command                       OpenRC                                                                                                                                systemd                                                                                                                                  Comments

  Start a service               [/etc/init.d/\<service\> start]\           [systemctl start \<service\>]
                                [rc-service \<service\> start]

  Stop a service                [/etc/init.d/\<service\> stop]\            [systemctl stop \<service\>]
                                [rc-service \<service\> stop]

  Restart a service             [/etc/init.d/\<service\> restart]\         [systemctl restart \<service\>]
                                [rc-service \<service\> restart]

  Get service status            [/etc/init.d/\<service\> status]\          [systemctl status \<service\>]
                                [rc-service \<service\> status]

  Show known startup scripts    [rc-status]\                               [systemctl list-units]                        Shows scripts that exist in runlevels
                                [rc-update show]

  Show all startup scripts      [ls /etc/init.d/]\                         [systemctl list-unit-files \--type=service]   Shows all installed scripts
                                [rc-update -v show]

  Enable service at startup     [rc-update add \<service\> \<runlevel\>]   [systemctl enable \<service\>]

  Disable service at startup    [rc-update del \<service\> \<runlevel\>]   [systemctl disable \<service\>]

  Disable service altogether    chmod 444 /etc/init.d/\<service\>                                                                                                     [systemctl mask \<service\>]                  The service cannot be run until *unmasked*.

  Cancels \'masking\' service   chmod 555 /etc/init.d/\<service\>                                                                                                     [systemctl unmask \<service\>]
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------

The following table is a list of useful systemd commands that have no OpenRC equivalent:

  ---------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------- ----------
  Command                                                          Syntax                                                                                                                                       Comments
  To be run after creating or modifying services                   [systemctl daemon-reload]
  Kill all processes related to service                            [systemctl kill \<service\>]
  Show logs events that happened today, most recent events first   [journalctl -r \--since=today]
  Show log events for a specific service                           [journalctl \_SYSTEMD_UNIT=\<service\>.service]
  ---------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------- ----------

## [Runlevels]

In systemd, what correpsponds to runlevels are called \"targets\", but the latter is more general. Services can be set to run before and after targets. In particular, `runlevel<N>.target` (N = 0\...6) roughly mimicks runlevels.

See [Systemd#Targets](https://wiki.archlinux.org/title/Systemd#Targets) in Arch Wiki for introduction. All pre-defined targets are found in the man page [systemd.special (7)](https://www.man7.org/linux/man-pages/man7/systemd.special.7.html).

## [][/etc/local.d]

In OpenRC, scripts [`/etc/local.d/*start`](https://wiki.gentoo.org/index.php?title=OpenRC_to_systemd_Cheatsheet/etc/local.d&action=edit&redlink=1 "OpenRC to systemd Cheatsheet/etc/local.d (page does not exist)") are started at system startup and `*stop` are run at shutdown. To port them to systemd with minimal changes, one can create the service `local.d.start`:

[FILE] **`/etc/systemd/system/local.d.start.service`**

    [Unit]
    Description=Run /etc/local.d scripts at start
    Before=runlevel3.target

    [Service]
    Type=simple
    ExecStart=/foo/bar/baz

    [Install]
    WantedBy=runlevel3.target

Here we chose runlevel3 as the target, but one can change this. This service will run the script `/for/bar/baz`, which should look like:

[FILE] **`/foo/bar/baz`**

    #!/bin/bash

    for i in /etc/local.d/*start; do
        if [[ -x "$i" ]]; then
            "$i" &
        fi
    done

The path of /foo/bar/baz is not standardized. Some suggest `/usr/local/bin`. /usr/local is [for sysadmin installing something locally](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s09.html), according to FHS. (The contributor of this section personally thinks it is too general, and would like to suggest something like `/usr/local/libexec/systemd/` for example.)

Similarly one can create a \*stop service. They have to be enabled to take effect.

## [[] See also]

-   [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") --- a dependency-based [init system](https://en.wikipedia.org/wiki/Init "wikipedia:Init") for Unix-like systems that maintains compatibility with the system-provided [init system](https://wiki.gentoo.org/wiki/Init_system "Init system")
-   [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") --- a modern SysV-style init and [[rc](https://wiki.gentoo.org/wiki/Rc "Rc")] replacement for Linux systems.