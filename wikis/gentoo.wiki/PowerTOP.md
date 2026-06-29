**Resources**

[[]][Home](https://01.org/powertop/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PowerTOP "wikipedia:PowerTOP")

[[]][Package information](https://packages.gentoo.org/packages/sys-power/powertop)

**PowerTOP** is a Linux utility that can monitor and display a system\'s electrical power usage. It is useful as a hardware monitoring and diagnostic tool. It is among the most powerful battery stretching utilities for notebook computers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Calibration]](#Calibration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Could not find a Makefile in the kernel source directory]](#Could_not_find_a_Makefile_in_the_kernel_source_directory)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Several kernel options must be enabled in the kernel for PowerTOP to work properly. These include: `CONFIG_DEBUG_FS`, `CONFIG_TRACING`, `CONFIG_BLK_DEV_IO_TRACE`, `CONFIG_TIMER_STATS` (was removed in kernel 4.11), `CONFIG_CPU_FREQ_STAT`, and `CONFIG_CPU_FREQ_STAT_DETAILS` (removed in 4.11, and rolled into `CONFIG_CPU_FREQ_STAT`).

** Note**\
`CONFIG_TIMER_STATS` has been removed from kernel, see [https://patchwork.kernel.org/patch/9561519/](https://patchwork.kernel.org/patch/9561519/)

For newer Intel Core series of processors (based on the Sandy Bridge microarchitecture or newer) enable the [powercap sysfs driver](https://wiki.gentoo.org/wiki/Power_management/Guide#powercap_sysfs_driver "Power management/Guide") via `CONFIG_POWERCAP` and `CONFIG_INTEL_RAPL`.

Optionally, for wireless power saving enable: `CONFIG_TRACEPOINTS`.

[KERNEL] **Enable support for PowerTOP in the kernel**

    Power management and ACPI options  --->
       CPU Frequency scaling  --->
          [*] CPU Frequency scaling
          <*>   CPU frequency transition statistics
          [*]     CPU frequency transition statistics details
       -*- Device power management core functionality
       [*]   Power Management Debug Support
       [*]      Extra PM attributes in sysfs for low-level debugging/testing

    Kernel hacking  --->
       [*] Kernel debugging

       Generic Kernel Debugging Instruments  --->
          [*] Debug Filesystem

       [*] Collect kernel timers statistics
       [*] Tracers  --->
          [*] Support for tracing block IO actions

[KERNEL] **Generic powercap sysfs driver**

    Processor type and features --->
      <M> /dev/cpu/*/msr - Model-specific register support Search for <code>CONFIG_X86_MSR</code> to find this item.
    Device Drivers --->
      <*> Generic powercap sysfs driver ---> Search for <code>CONFIG_POWERCAP</code> to find this item.
        <M> Intel RAPL Support via MSR Interface Search for <code>CONFIG_INTEL_RAPL</code> to find this item.

If the above options have not properly been enabled [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") will display warning messages at the end of the emerge. If help is required for upgrading the kernel while enabling the above options, be sure to see the [kernel upgrade article](https://wiki.gentoo.org/wiki/Kernel/Upgrade "Kernel/Upgrade")!

### [USE flags]

### [USE flags for] [sys-power/powertop](https://packages.gentoo.org/packages/sys-power/powertop) [[]] [tool to diagnose issues with power consumption and power management]

  ----------------------------------------------------------- --------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Add support for X11
  [`nls`](https://packages.gentoo.org/useflags/nls)           Add Native Language Support (using gettext - GNU locale utilities)
  [`unicode`](https://packages.gentoo.org/useflags/unicode)   Add support for Unicode
  ----------------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting USE flags, [emerge] PowerTOP:

`root `[`#`]`emerge --ask sys-power/powertop`

## [Configuration]

PowerTOP does not have any configuration other than passing options via the command-line.

### [Calibration]

Calibration can be performed in order for PowerTOP to gain an understanding of the system:

`root `[`#`]`powertop --calibrate`

** Note**\
During the calibrating process the attached screen and network adapters are turned off and on again.

## [Usage]

### [Invocation]

`user `[`$`]`/usr/sbin/powertop --help`

    Usage: powertop [OPTIONS]

         --auto-tune         sets all tunable options to their GOOD setting
     -c, --calibrate         runs powertop in calibration mode
     -C, --csv[=filename]    generate a csv report
         --debug             run in "debug" mode
         --extech[=devnode]  uses an Extech Power Analyzer for measurements
     -r, --html[=filename]   generate a html report
     -i, --iteration[=iterations] number of times to run each test
     -q, --quiet             suppress stderr output
     -t, --time[=seconds]    generate a report for 'x' seconds
     -w, --workload[=workload] file to execute for workload
     -V, --version           print version information
     -h, --help              print this help menu

    For more help please refer to the 'man 8 powertop'

## [Troubleshooting]

### [Could not find a Makefile in the kernel source directory]

After an emerge a message similar to the following message may be displayed:

[CODE] **Post emerge warning message**

    * Could not find a Makefile in the kernel source directory.
     * Please ensure that /usr/src/linux points to a complete set of Linux sources
     * Unable to calculate Linux Kernel version for build, attempting to use running version
     *   CONFIG_DEBUG_FS:    is not set when it should be.
     *   CONFIG_TRACEPOINTS:         is not set when it should be.
     *   CONFIG_BLK_DEV_IO_TRACE:    is not set when it should be.
     *   CONFIG_TIMER_STATS:         is not set when it should be.
     *   CONFIG_TRACING:     is not set when it should be.
     * Please check to make sure these options are set correctly.
     * Failure to do so may cause unexpected problems.

This warning indicates the PowerTOP ebuild has attempted to verify a successful operating environment for the PowerTOP software package. In order to be sure PowerTOP will work as intended, at the end of the [emerge] process, a check is ran against the current kernel source configuration. In the case of the above message two warnings were provided:

1.  No kernel sources have been detected. This can happen as a result of running an [emerge \--depclean] or failed to have a specific kernel set using the [eselect kernel] command.
2.  Since no kernel sources have been detected Portage was not able to scan the kernel\'s [.config] file to determine if the correct features have been enabled in the kernel. According to the error message above, five features are not set. The features may or may not be set in the current running kernel. Portage is simply making the user aware there is no way to verify these features have been set without a [.config] file. If PowerTOP can perform some functions but not others, be sure all the kernel features listed have been enabled. For more information on how to do so consult the [kernel configuration article](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration").

## [See also]

-   [Power management](https://wiki.gentoo.org/wiki/Power_management "Power management") --- describes methods to save energy for longer battery runtimes, a quieter computer, lower power bills, and an environmentally friendly impact.

## [External resources]

-   [https://www.linux.com/learn/powertop-finds-power-hogs-your-linux-pc](https://www.linux.com/learn/powertop-finds-power-hogs-your-linux-pc) - A Linux.com article on using PowerTOP to measure large power consumers.
-   [https://01.org/sites/default/files/page/powertop_users_guide_201406.pdf](https://01.org/sites/default/files/page/powertop_users_guide_201406.pdf) - A PowerTOP user guide writen by two Intel employees (PDF).