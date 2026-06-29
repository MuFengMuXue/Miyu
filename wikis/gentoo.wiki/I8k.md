**Resources**

[[]][Home](https://launchpad.net/i8kutils)

** Warning**\
The i8k module and its interface /proc/i8k has been deprecated and the dell-smm-hwmon module ^[\[1\]](#cite_note-1)^ should be used instead.

This article describes the setup of *i8k*, a kernel module to monitor cpu temperature and control fan speed on Dell laptops.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Software]](#Software)
        -   [[1.2.1] [Add-ons]](#Add-ons)
-   [[2] [External resources]](#External_resources)

## [Installation]

There is no need to install i8k kernel module as i8k kernel module comes ready in most recent (2014) kernels.

### [Kernel]

If compiling a customized kernel, the following options are required:

[KERNEL]

    Processor type and features  --->
        <M> Dell laptop support

When the module is loaded, there is a check. If the user\'s laptop is supported, ok. If not, the module will fail to load.

If the user want to load the module anyway, put the option `force=1` right after the command as shown below:

`root `[`#`]`modprobe i8k force=1`

** Warning**\
Loading the driver on an untested laptop can crash the system.

### [Software]

-   [[[app-laptop/i8kutils]](https://packages.gentoo.org/packages/app-laptop/i8kutils)[]] - Fan control for Dell laptops

i8kutils contains the user-space programs needed to handle the data provided by the i8k kernel module.

#### [Add-ons]

-   [[[x11-plugins/i8krellm]](https://packages.gentoo.org/packages/x11-plugins/i8krellm)[]] - [GKrellM](https://wiki.gentoo.org/wiki/GKrellM "GKrellM")2 plugin

## [External resources]

-   [i8kutils homepage at Debian](http://packages.qa.debian.org/i/i8kutils.html)

1.  [[[↑](#cite_ref-1)] [[Kernel driver dell-smm-hwmon¶](https://www.kernel.org/doc/html/latest/hwmon/dell-smm-hwmon.html)]]