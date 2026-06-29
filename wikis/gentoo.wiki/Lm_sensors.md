**Resources**

[[]][lm_sensors](https://github.com/groeck/lm-sensors)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lm_sensors "wikipedia:Lm sensors")

[[]][lm_sensors](https://github.com/groeck/lm-sensors)

[lm_sensors] is a set of hardware monitoring user space utilities. They are helpful for tracking temperature, fan, and voltage data. This article deals with the sensors aspect to lm_sensors, but the package also contains software to control fan speed: see the page for [fan speed control](https://wiki.gentoo.org/wiki/Fan_speed_control#Fancontrol "Fan speed control") for details.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Modules]](#Modules)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Testing]](#Testing)
-   [[4] [Troubleshooting]](#Troubleshooting)

## [Installation]

Before [lm_sensors] will work as intended, the currently running Linux kernel must have the proper modules available to or built-in to the binary in order to give lm_sensors the sensor-related data needed for correct operation. There is a chance these modules have been previously built as modules or are currently included the Kernel\'s binary (built-in). It is also possible the Kernel is lacking the modules or features. If something is missing then the user will have to take the actions necessary to correct the absence.

In any case a simple hardware detection should be performed using the [sensors-detect] tool to scan the hardware on the motherboard. Once the hardware has been determined the program will display the output on what is or is not included in the kernel configuration. This step will be performed after installation during the configuration section below.

Another option is to check the [Supported Device List](https://web.archive.org/web/20150901174206/http://www.lm-sensors.org:80/wiki/Devices) on archive.org. Finally, [sensors-detect] detects the supported drivers if all drivers in kernel section *Hardware Monitoring support* are enabled.

### [Kernel]

[I2C](https://wiki.gentoo.org/wiki/I2C "I2C") support is needed along with the following kernel options:

[KERNEL] **Enable I2C_CHARDEV and hardware Monitoring support in the kernel**

    Device Drivers  --->
        -*- I2C support  --->
            <*>   I2C device interface
        <*> Hardware Monitoring support  --->

            Select a driver, e.g.:
            [*] Intel Core/Core2/Atom temperature sensor (coretemp)

### [USE flags]

Portage knows the global USE flag [`lm-sensors`](https://packages.gentoo.org/useflags/lm-sensors) for enabling support for [lm-sensors] in other packages.

Local USE flags include:

### [USE flags for] [sys-apps/lm-sensors](https://packages.gentoo.org/packages/sys-apps/lm-sensors) [[]] [Hardware Monitoring user-space utilities]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`contrib`](https://packages.gentoo.org/useflags/contrib)           Installs user contributed configuration files so you don\'t need to find settings on your own for your system if somebody else has already created such a configuration for sensors/mainboards you are using.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sensord`](https://packages.gentoo.org/useflags/sensord)           Enable sensord - a daemon that can be used to periodically log sensor readings from hardware health-monitoring chips
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

In case any of the packages having the `lm-sensors` USE flag is installed, set the flag per package in [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] or globally in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE "/etc/portage/make.conf")] and update \@world so that [[[sys-apps/lm-sensors]](https://packages.gentoo.org/packages/sys-apps/lm-sensors)[]] will be pulled in as dependency:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Otherwise install it directly:

`root `[`#`]`emerge --ask sys-apps/lm-sensors`

## [Configuration]

If all drivers were built into the kernel, skip to the next section and proceed with [testing](#Testing). Otherwise configure the modules as needed.

### [Modules]

** Warning**\
Be aware using [sensors-detect] to probe the hardware in the system may result in a frozen system. Take some *special caution* by reading [the official documentation](https://web.archive.org/web/20150823034732/http://www.lm-sensors.org:80/wiki/Documentation) before running [lm_sensors] on **IBM Thinkpads**.

The [sensors-detect] ([/usr/sbin/sensors-detect]) tool can be used to find available sensors and associated kernel modules:

`root `[`#`]`sensors-detect`

Follow the instructions, it will probe which sensors are available and load the relevant kernel modules. The final question will allow you to write a config file in [/etc/modules-load.d] that contains the kernel modules that need to be loaded. This will only work if the `modules-load` runscript is started, add it to the `default` runlevel if necessary.

If you use `/etc/conf.d/modules` to declare which kernel modules to load simply add the necessary kernel modules as shown by `sensors-detect` to it.

### [Services]

#### [OpenRC]

Start the sensors daemon now:

`root `[`#`]`rc-service lm_sensors start`

To start [lm_sensors] on system boot add it the default runlevel:

`root `[`#`]`rc-update add lm_sensors default`

#### [systemd]

Start the sensors daemons now:

`root `[`#`]`systemctl start lm_sensors`

Enable the sensors daemon for future boots:

`root `[`#`]`systemctl enable lm_sensors`

## [Usage]

### [Invocation]

`user `[`$`]`sensors --help`

    Usage: sensors [OPTION]... [CHIP]...
      -c, --config-file     Specify a config file
      -h, --help            Display this help text
      -s, --set             Execute `set' statements (root only)
      -f, --fahrenheit      Show temperatures in degrees fahrenheit
      -A, --no-adapter      Do not show adapter for each chip
          --bus-list        Generate bus statements for sensors.conf
      -u                    Raw output
      -v, --version         Display the program version

    Use `-' after `-c' to read the config file from stdin.
    If no chips are specified, all chip info will be printed.
    Example chip names:
        lm78-i2c-0-2d   *-i2c-0-2d
        lm78-i2c-0-*    *-i2c-0-*
        lm78-i2c-*-2d   *-i2c-*-2d
        lm78-i2c-*-*    *-i2c-*-*
        lm78-isa-0290   *-isa-0290
        lm78-isa-*  *-isa-*
        lm78-*

### [Testing]

Now test if everything works:

`user `[`$`]`sensors`

    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +48.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:       +48.0°C  (high = +100.0°C, crit = +100.0°C)

## [Troubleshooting]

See the [lm_sensors FAQ](https://hwmon.wiki.kernel.org/faq?s%5b%5d=lm_sensors).