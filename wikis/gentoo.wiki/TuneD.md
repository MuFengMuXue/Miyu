**Resources**

[[]][Home](https://tuned-project.org/)

[[]][GitHub](https://github.com/redhat-performance/tuned)

[[]][Official documentation](https://github.com/redhat-performance/tuned/tree/master/doc/manual/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/tuned)

**TuneD** is a daemon for monitoring and adaptive tuning of system devices.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

** Important**\
TuneD is incompatible with [[[sys-power/power-profiles-daemon]](https://packages.gentoo.org/packages/sys-power/power-profiles-daemon)[]] and [[[sys-power/cpupower]](https://packages.gentoo.org/packages/sys-power/cpupower)[]]. Unmerge those tools before installing TuneD

`root `[`#`]`emerge --ask sys-apps/tuned`

## [Configuration]

View the man page for all configuration options.

`user `[`$`]`man 5 tuned-main.conf`

### [Service]

#### [OpenRC]

Start the daemon:

`root `[`#`]`rc-service tuned start`

Optionally, add the service to the default runlevel to start it on boot:

`root `[`#`]`rc-update add tuned default`

## [Usage]

After enabling the daemon, the current active profile can be viewed:

`root `[`#`]`tuned-adm active`

The list of available profiles can be viewed:

`root `[`#`]`tuned-adm list`

The `profile` subcommand can be used to switch to a different profile. For instance, one could use the following for aggressive power saving on laptops:

`root `[`#`]`tuned-adm profile laptop-battery-powersave`

## [See also]

-   [Power management](https://wiki.gentoo.org/wiki/Power_management "Power management") --- describes methods to save energy for longer battery runtimes, a quieter computer, lower power bills, and an environmentally friendly impact.
-   [PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") --- a Linux utility that can monitor and display a system\'s electrical power usage.