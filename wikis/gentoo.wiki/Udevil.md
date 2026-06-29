Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Udevil/hu "Udevil (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Udevil/pl "Udevil/pl (6% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Udevil/ja "udevil (100% translated)")

**Resources**

[[]][Home](http://ignorantguru.github.io/udevil/)

[[]][GitHub](https://github.com/IgnorantGuru/udevil)

**udevil** is a small auto-mount utility created to be a \"a hassle-free replacement for [udisks](https://wiki.gentoo.org/wiki/Udisks "Udisks").\"^[\[1\]](#cite_note-1)^ It can be used *with* or *without* [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), ConsoleKit, policykit, [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus"), udisks, [GVfs](https://wiki.gentoo.org/wiki/GVfs "GVfs"), and [FUSE](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace "Filesystem in Userspace").

** Note**\
It is important to know [udevil] does not play nicely with encrypted filesystems. If an encrypted filesystem is being used consider looking for an alternate auto-mount utility, such as [[[sys-fs/udiskie]](https://packages.gentoo.org/packages/sys-fs/udiskie)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Global]](#Global)
    -   [[2.2] [Local]](#Local)
    -   [[2.3] [devmon]](#devmon)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Daemon mode]](#Daemon_mode)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [Systemd]](#Systemd)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

Kernel eventpolling may need to be enabled for device media to be properly detected by the kernel:

[KERNEL] **Enable eventpolling (CONFIG_EPOLL)**

    General setup  --->
       [*] Configure standard kernel features (expert users)  --->
          [*]   Enable eventpoll support

After enabling eventpolling confirm operation by running:

`root `[`#`]`cat /sys/module/block/parameters/events_dfl_poll_msecs `

`root `[`#`]`cat /sys/block/sr0/events_poll_msecs `

If either command returns 0 or -1 then there will be issues detecting device media. Create a small script in [[/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d")] that will force event polling for each device:

[FILE] **`/etc/local.d/eventpolling.start`Enable event polling**

    #!/bin/bash
    source /etc/profile
    echo 2000 > /sys/module/block/parameters/events_dfl_poll_msecs
    echo 2000 > /sys/block/sr0/events_poll_msecs

Be sure to make the script executable:

`root `[`#`]`chmod +x /etc/local.d/eventpolling.start`

### [Emerge]

Install [udevil]:

`root `[`#`]`emerge --ask sys-apps/udevil`

## [Configuration]

### [Global]

[udevil]\'s operation can be configured using the global configuration file:

-   [/etc/udevil/udevil.conf]

### [Local]

According to official documentation^[\[2\]](#cite_note-2)^ it is possible to configure auto-mount permissions on an individual basis by creating an [/etc/udevil/] configuration file in this following format:

-   [/etc/udevil/udevil-user-larry.conf]

Where `larry` is replaced by the desired user name.

### [devmon]

A configuration file called [devmon] is also installed in the [/etc].

-   [/etc/conf.d/devmon]

## [Usage]

### [Daemon mode]

#### [OpenRC]

[udevil] can be configured to operate as a daemon by calling the [devmon] command. It is possible to run this command in the background by calling it as a job using the ampersand (`&`). Users who belong to the `plugdev` group can add the following line to their [\~/.bashrc] file, which will start [devmon] as a daemon each time the system boots:

[FILE] **`~/.bashrc`Starting devmon in daemon mode**

    devmon 2>&1 > /dev/null &

#### [Systemd]

To start [devmon] as a [systemd user service](https://wiki.gentoo.org/wiki/Systemd#User_services "Systemd"):

`root `[`#`]`systemctl start devmon@larry`

Replace `larry` with the appropriate user name.

### [Invocation]

`user `[`$`]`udevil mount <device>`

`user `[`$`]`udevil unmount <device>`

## [Troubleshooting]

To avoid a permission denied error while trying to invoke [udevil], ensure the user belongs to the setuid executable\'s group, which is most likely `plugdev`.

## [See also]

-   [Udev](https://wiki.gentoo.org/wiki/Udev "Udev") --- [systemd\'s](https://wiki.gentoo.org/wiki/Systemd "Systemd") device manager for the Linux kernel.
-   [[[sys-fs/udiskie]](https://packages.gentoo.org/packages/sys-fs/udiskie)[]]

## [External resources]

-   [https://igurublog.wordpress.com/downloads/script-devmon/](https://igurublog.wordpress.com/downloads/script-devmon/) - A page describing [devmon], an auto-mounting daemon that is now distributed with [udevil]. This link may be helpful for reference purposes.

## [References]

1.  [[[↑](#cite_ref-1)] [[http://ignorantguru.github.io/udevil/](http://ignorantguru.github.io/udevil/)]]
2.  [[[↑](#cite_ref-2)] [[http://ignorantguru.github.io/udevil/udevil.conf.txt](http://ignorantguru.github.io/udevil/udevil.conf.txt)]]