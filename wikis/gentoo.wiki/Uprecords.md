**Resources**

[[]][GitHub](https://github.com/rpodgorny/uptimed)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/uptimed)

**uptimed** is a daemon that keeps track of a system\'s \'uptime\' (how long a system has running between a reboot). It can be used to provide the statistical information necessary to boast about how long a system as gone between reboots. Huge nerds love this.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/uptimed](https://packages.gentoo.org/packages/app-misc/uptimed) [[]] [System uptime record daemon that keeps track of your highest uptimes]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/uptimed`

## [Configuration]

### [Files]

-   [/etc/uptimed.conf] - The global configuration file for [uptimed].

### [Services]

#### [OpenRC]

With OpenRC the uptimed daemon can be added to the default system runlevel with the following command:

`root `[`#`]`rc-update add uptimed default`

This will add the [uptimed] daemon to start as a service whenever the system performs a full boot.

To start using uptimed now:

`root `[`#`]`rc-service uptimed start`

#### [systemd]

When using systemd, issue the following command to start uptimed on the next boot:

`root `[`#`]`systemctl enable uptimed`

To start using uptimed now:

`root `[`#`]`systemctl start uptimed`

## [Usage]

### [Invocation]

`user `[`$`]`uprecords -?`

    usage: uprecords [OPTION]...

      -?             this help
      -a             do not print ansi codes
      -b             sort by boottime
      -B             reverse sort by boottime
      -k             sort by sysinfo
      -K             reverse sort by sysinfo
      -d             print downtime seen before every uptimes instead of system
      -c             do not show current entry if not in top entries
      -f             run continously in a loop
      -s             do not print extra statistics
      -w             wide output (more than 80 cols per line)
      -i INTERVAL    use INTERVAL seconds for loop instead of 5, implies -f
      -m COUNT       show a maximum of top COUNT entries instead of 10
      -M             show next milestone
      -v             version information

The [uprecords] command will print a table with system uptime information:

`user `[`$`]`uprecords`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/uptimed`

## [See also]

-   [[uptime](https://wiki.gentoo.org/index.php?title=Uptime&action=edit&redlink=1 "Uptime (page does not exist)")] - A command that displays the amount of time the system has been running.

## [External resources]

-   [https://archives.gentoo.org/gentoo-user/message/b6e85a7d66178464ec2188592bb3b2fe](https://archives.gentoo.org/gentoo-user/message/b6e85a7d66178464ec2188592bb3b2fe) - A Gentoo mailing list thread where [uptimed] was handy.