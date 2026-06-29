This script is run instead of init during the boot process after the kernel is loaded and measures the time during this process. With the aid of a script in the project\'s Git repository, it generates nice charts which show when each daemon started and stopped.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Kernel]](#Kernel)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Bootloader]](#Bootloader)
    -   [[2.2] [Analyzing the output]](#Analyzing_the_output)
-   [[3] [External resources]](#External_resources)

## [Installation]

You can install [[[app-benchmarks/bootchart2]](https://packages.gentoo.org/packages/app-benchmarks/bootchart2)[]] with the following command:

`root `[`#`]`emerge --ask app-benchmarks/bootchart2`

Then add the daemon to the default runlevel. This is needed to stop the bootchart process and generate the image:

`root `[`#`]`rc-update add bootchart2 default`

### [USE flags]

### [USE flags for] [app-benchmarks/bootchart2](https://packages.gentoo.org/packages/app-benchmarks/bootchart2) [[]] [Performance analysis and visualization of the system boot process]

  --------------------------------------------------------- -----------------------------------------------
  [`+cairo`](https://packages.gentoo.org/useflags/+cairo)   Enable support for the cairo graphics library
  --------------------------------------------------------- -----------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-12 03:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Kernel]

To get more verbose information:

[KERNEL] **enable proc events**

    General setup  --->
        CPU/Task time and stats accounting -->
            -*- Export task/process statistics through netlink (EXPERIMENTAL)
    Device Drivers --->
        <*> Connector - unified userspace <-> kernelspace linker  --->
            [*]   Report process events to userspace

## [Usage]

How to enable bootchart2 during boot and access the generated charts.

### [Bootloader]

-   For any GRUB based bootloader, the kernel commandline can be changed during boot by pressing [e] in the boot menu, then edit the kernel commandline and press [F10] to boot with changed parameters. The following options should be added:

\'initcall_debug\' - append timing data to each initcall

\'printk.time=y\' - append timing data to each message during initialization

\'init=/sbin/bootchartd\' - replace the default command for initialization with [/sbin/bootchartd] to start our benchmark

** Note**\
to use genkernel, replace *init=* with *real_init=*

-   To change the entry static for GRUB (bootchart on every boot):

In [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") the parameters can be added to the variable `GRUB_CMDLINE_LINUX_DEFAULT` in [/etc/default/grub].

[CODE] **Kernel command-line**

    linux initcall_debug printk.time=y init=/sbin/bootchartd

Then run:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

### [Analyzing the output]

The values are stored in [/var/log/bootchart.tgz] as a compressed tarball.

[CODE] **tar tf /var/log/bootchart.tgz**

    header
    dmesg
    cmdline2.log
    paternity.log
    proc_cpuinfo.log
    proc_diskstats.log
    proc_meminfo.log
    proc_stat.log
    taskstats.log

A script that generates an easier-to-analyze PDF or PNG from this tarball can be found on the project\'s homepage, by cloning the git repository, and then running `make pybootchartgui/main.py` and `./pybootchartgui.py`. The script requires [[[dev-python/pycairo]](https://packages.gentoo.org/packages/dev-python/pycairo)[]].

## [External resources]

-   [homepage](https://github.com/mmeeks/bootchart/)