**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

In this guide provides instructions on setting up a basic virtual server using the OpenVZ Technology.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Host environment]](#Host_environment)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Creating a guest template]](#Creating_a_guest_template)
        -   [[2.1.1] [Template tarball]](#Template_tarball)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Test the virtual server]](#Test_the_virtual_server)

## [Installation]

### [Emerge]

Install the [[[sys-kernel/openvz-sources]](https://packages.gentoo.org/packages/sys-kernel/openvz-sources)[]] package:

`root `[`#`]`emerge --ask sys-kernel/openvz-sources`

### [Kernel]

[KERNEL] **Configure openvz-sources**

    Processor type and features  --->
      [*] Fair CPU scheduler
      [*]   VCPU scheduler support
    File Systems  --->
      [*] Quota support
      <M> VPS filesystem
      <M> Virtuozzo Disk Quota support
      [ ]   Unloadable Virtuozzo Disk Quota module
      [*]   Per-user and per-group quota in Virtuozzo quota partitions
    OpenVZ  --->
      [*] Virtual Environment support
      <M>   VE calls interface
      [ ]   Enable sysfs support in Virtual Environments
      <M>   VE networking
      [*]     VE netfiltering
      <M>   VE watchdog module

After you\'ve built and installed the kernel (steps not covered in this article), update the boot loader and reboot to see if the kernel boots correctly.

### [Host environment]

To maintain your virtual servers you need the [[[sys-cluster/vzctl]](https://packages.gentoo.org/packages/sys-cluster/vzctl)[]] package which contains all necessary programs and many useful features:

`root `[`#`]`emerge --ask sys-cluster/vzctl`

## [Configuration]

The vzctl packages has installed an init script called [vz]. It will help you to start/stop virtual servers on boot/shutdown:

`root `[`#`]`rc-update add vz default `

`root `[`#`]`/etc/init.d/vz start `

### [Creating a guest template]

#### [Template tarball]

Since many hardware related commands are not available inside a virtual server, there has been a patched version of baselayout known as baselayout-vserver. However all required changes have been integrated into normal baselayout-2, eliminating the need for seperate vserver stages, profiles and baselayout. The only (temporary) drawback is that baselayout-2 is still considered to be in alpha stage and there are no stages with baselayout-2 available on the mirrors yet.

As soon as baselayout-2 is stable you can use a precompiled stage3/4 from one of our mirrors. In the meantime please download a stage3/4 from here.

** Note**\
Unfortunately `vzctl` does not understand bzip2 (yet?) and needs a different filename to recognize Gentoo as the distribution, so you have to convert the stage tarball.

Convert the stage tarball:

`root `[`#`]`cd /vz/template/cache `

`root `[`#`]`bunzip2 stage4-<arch>-<version>.tar.bz2 `

`root `[`#`]`mv stage4-tarball.tar gentoo-<arch>-<version>.tar `

`root `[`#`]`gzip gentoo-<arch>-<version>.tar `

`root `[`#`]`cd - `

Create VPS

`root `[`#`]`vzctl create <vpsid> --ostemplate gentoo-<arch>-<version>`

** Note**\
Do not use vpsids \<=100, they are reserved.

## [Usage]

### [Test the virtual server]

You should be able to start and enter the vserver by using the commands below:

`root `[`#`]`vzctl start <vpsid> `

`root `[`#`]`vzctl enter <vpsid> `

`root `[`#`]`ps ax`

    PID   TTY      STAT   TIME COMMAND
        1 ?        S      0:00 init [3]
    20496 pts/0    S      0:00 /bin/bash -i
    20508 pts/0    R+     0:00 ps ax

`root `[`#`]`logout`

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Benedikt Boehm (author) on March 22, 2007**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*