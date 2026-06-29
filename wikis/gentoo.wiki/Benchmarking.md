This article describes various methods of system benchmarking on Linux. It covers CPUs, power usage, RAM, and graphics.

## Contents

-   [[1] [Power usage]](#Power_usage)
-   [[2] [CPU]](#CPU)
    -   [[2.1] [time]](#time)
-   [[3] [RAM]](#RAM)
    -   [[3.1] [ramspeed]](#ramspeed)
-   [[4] [I/O]](#I.2FO)
    -   [[4.1] [hdparm]](#hdparm)
    -   [[4.2] [time]](#time_2)
-   [[5] [OpenGL]](#OpenGL)
    -   [[5.1] [Nexuiz]](#Nexuiz)
        -   [[5.1.1] [Install]](#Install)
        -   [[5.1.2] [Reset default options]](#Reset_default_options)
        -   [[5.1.3] [Benchmark]](#Benchmark)
    -   [[5.2] [Xonotic]](#Xonotic)
        -   [[5.2.1] [Install]](#Install_2)
        -   [[5.2.2] [Reset]](#Reset)
        -   [[5.2.3] [Benchmark]](#Benchmark_2)
    -   [[5.3] [glxgears]](#glxgears)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Power usage]

[[[sys-power/powertop]](https://packages.gentoo.org/packages/sys-power/powertop)[]] can guess the computer\'s current power usage in watts.

`root `[`#`]`powertop -d | grep usage`

    Power usage (ACPI estimate): 15.7W (0.5 hours)

## [CPU]

Some examples with different cryptographic commands. OpenSSL tries many different combinations of ciphers, key lengths and modes:

`user `[`$`]`openssl speed`

This could be bound to a single core (as root):

`root `[`#`]`taskset -c 1 openssl speed`

[[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] instead has less algorithms but includes kernel\'s cryptographic API if available:

`user `[`$`]`cryptsetup benchmark`

### [time]

Command [time] measures execution time of a sub command. Use a reproducible command to measure CPU performance:

`root `[`#`]`time emerge -1 coreutils`

    real   2m33.483s
    user    2m6.310s
    sys 0m55.257s

Using [emerge] is not very reliable since the task is very complex and also requires I/O time and does not run parallel in all stages. Instead with [[[sys-devel/bc]](https://packages.gentoo.org/packages/sys-devel/bc)[]] calculation of PI burns CPU time for a single core only:

`user `[`$`]`time echo "scale=5000; 4*a(1)" | bc -l`

## [RAM]

### [ramspeed]

[[[app-benchmarks/ramspeed]](https://packages.gentoo.org/packages/app-benchmarks/ramspeed)[]] can measure the computer\'s ram speed.

** Warning**\
ramspeed is incompatible with ACCEPT_LICENSE=\"@FREE\". It is a proprietary program.

`user `[`$`]`ramspeed -b1 -m4 | grep 4096 && ramspeed -b2 -m4 | grep 4096`

    INTEGER & WRITING      4096 Kb block: 1948.94 MB/s
    INTEGER & READING      4096 Kb block: 5208.66 MB/s

## [][I/O]

Some of the available packages to measure input-output-performance in general:

-   [[[app-benchmarks/iozone]](https://packages.gentoo.org/packages/app-benchmarks/iozone)[]]
-   [[[sys-block/fio]](https://packages.gentoo.org/packages/sys-block/fio)[]] -- be careful with tests writing to devices to not interfere with valuable data

### [hdparm]

Historically used to measure hard disk performance:

`root `[`#`]`hdparm -tT /dev/sda`

    /dev/sda:
     Timing cached reads:   1076 MB in  2.00 seconds = 538.08 MB/sec
     Timing buffered disk reads: 242 MB in  3.01 seconds =  80.32 MB/sec

### [time]

Using [time] to examine time spent in user and system space:

`user `[`$`]`time bzip2 -c patch-3.3 > patch-3.3.bz2`

    real 0m13.272s
    user    0m7.606s
    sys 0m0.054s

`user `[`$`]`time eix search`

    <snip>

    real    0m0.363s
    user    0m0.066s
    sys 0m0.008s

## [OpenGL]

### [Nexuiz]

#### [Install]

`root `[`#`]`emerge --ask games-fps/nexuiz`

#### [Reset default options]

If you have played nexuiz you should reset to default options for canonical benchmark results.

`user `[`$`]`rm -r ~/.nexuiz/`

#### [Benchmark]

`user `[`$`]`nexuiz-glx -benchmark demos/demo1 -nosound 2>&1 | egrep -e '[0-9]+ frames'`

    1910 frames 42.0330749 seconds 45.4404063 fps, one-second fps min/avg/max: 35 46 63 (90 seconds)

### [Xonotic]

#### [Install]

`root `[`#`]`emerge --ask games-fps/xonotic`

#### [Reset]

If you have played Xonotic you should reset to default options for canonical benchmark results.

`user `[`$`]`rm -r ~/.xonotic/`

#### [Benchmark]

`user `[`$`]`xonotic-glx -benchmark demos/the-big-keybench 2>&1 | egrep -e '[0-9]+ frames' `

    12568 frames 556.0637400 seconds 22.6017255 fps, one-second fps min/avg/max: 19 23 27 (207 seconds)

### [glxgears]

** Note**\
glxgears is a very basic OpenGL support test, it is not a real benchmark tool!

Obtain [glxgears] by emerging [[[x11-apps/mesa-progs]](https://packages.gentoo.org/packages/x11-apps/mesa-progs)[]].

`user `[`$`]`vblank_mode=0 glxgears & sleep 15 ; killall glxgears`

    5762 frames in 5.0 seconds = 1152.369 FPS
    5806 frames in 5.0 seconds = 1161.017 FPS

## [See also]

-   [PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") --- a Linux utility that can monitor and display a system\'s electrical power usage.

## [External resources]

-   [http://lbs.sourceforge.net/](http://lbs.sourceforge.net/) - A SourceForge site dedicated to listing benchmark utilities for Linux.