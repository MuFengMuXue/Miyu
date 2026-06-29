[sysctl] is provided by [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]], and can be used to configure kernel parameters at system runtime.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Service]](#Service)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [Systemd]](#Systemd)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Viewing current values]](#Viewing_current_values)
    -   [[4.2] [Setting values]](#Setting_values)
    -   [[4.3] [Reloading values]](#Reloading_values)
    -   [[4.4] [Filtering values]](#Filtering_values)

## [Introduction]

[sysctl] can be used to manage the system\'s kernel configuration, available through [/proc/sys/].

** Note**\
[sysctl] parameter names can be found using file paths under [/proc/sys/], replacing the \"*/*\" with \"*.*\".

## [Installation]

### [Kernel]

[KERNEL] **Enable procfs support**

    File systems  --->
       Pseudo filesystems  --->
          <*>  /proc file system support

### [Emerge]

`root `[`#`]`emerge --ask sys-process/procps`

** Note**\
This package is typically installed by default.

## [Configuration]

Kernel parameters can be configured by editing *.conf* files under [/etc/sysctl.d].

For example setting a custom value of `net.ipv4.tcp_retries2` can be achieved with file:

[FILE] **`/etc/sysctl.d/99-tcp-retransmission.conf`**

    net.ipv4.tcp_retries2=3

** Tip**\
Multiple files can be used, but they will be processed in lexicographical order, and values defined multiple times will take the last value. [/etc/sysctl.conf] is typically loaded last.

### [Service]

#### [OpenRC]

The OpenRC [sysctl] init script is enabled by default, it simply executes [sysctl \--system].

#### [Systemd]

The Systemd *systemd-sysctl* service is enabled by default.

## [Usage]

### [Viewing current values]

Current kernel configuration values can be printed with:

`root `[`#`]`sysctl --all`

### [Setting values]

Values can be updated using:

`root `[`#`]`sysctl --write = `

** Important**\
Setting values this way does not persist across reboots.

### [Reloading values]

Configuration values can be reloaded as they would be read on boot with:

`root `[`#`]`sysctl --system`

### [Filtering values]

**\--pattern** can be used to filter to parameters which match the supplied extended regex. This can be used for both printing and setting values.

To reload all system net values:

`root `[`#`]`sysctl --system --pattern 'net.*'`