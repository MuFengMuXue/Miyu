Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/de "EMERGE DEFAULT OPTS (6% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/es "EMERGE_DEFAULT_OPTS (44% translated)")
-   [français](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/fr "EMERGE DEFAULT OPTS (44% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/it "EMERGE DEFAULT OPTS (44% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/hu "EMERGE_DEFAULT_OPTS (100% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/pt-br "EMERGE DEFAULT OPTS/pt-br (25% translated)")
-   [русский](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/ru "EMERGE_DEFAULT_OPTS (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/zh-cn "EMERGE DEFAULT OPTS (44% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS/ja "EMERGE_DEFAULT_OPTS (100% translated)")

**EMERGE_DEFAULT_OPTS** is a variable for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") that defines entries to be appended to the [emerge] command line.

`EMERGE_DEFAULT_OPTS` allows for parallel [emerge] operations through the `--jobs ``N` and `--load-average ``X.Y` options. `EMERGE_DEFAULT_OPTS` is used by Portage to reference system load, or load average, and limit how many packages are built at a time.

## Contents

-   [[1] [Common use cases]](#Common_use_cases)
    -   [[1.1] [Parallel builds]](#Parallel_builds)
-   [[2] [See also]](#See_also)

## [Common use cases]

### [Parallel builds]

The `--jobs ``N` argument (short form: `-j``N`) will [emerge] `N` jobs at a time. Providing no arguments to `-j` floods the processor with as many jobs as possible. This is not recommended. Values for `N` should be no more than 2GB of ram per processor core. Packages can reach this constraint.

To run up to three build jobs simultaneously:

[FILE] **`/etc/portage/make.conf`Enabling 3 parallel package builds**

    EMERGE_DEFAULT_OPTS="--jobs 3"

When used with `--load-average ``X.Y` (short form: `-l``X.Y`), [emerge] tries to limit the load average of the system below the floating point number `X.Y`. The running jobs are again limited by the `--jobs` parameter.

The load average value is the same as displayed by [top] or [uptime], and for an `N`-core system, a load average of `N``.0` would be a 100% load. Setting `X.Y``=``N``*0.9` to limit the load to 90% maintains system responsiveness.

** Note**\
When `MAKEOPTS="-jN"` is used with `EMERGE_DEFAULT_OPTS="--jobs K --load-average X.Y"` the number of possible tasks created would be up to `N*K`. Therefore, both variables need to be set with each other in mind as they create up to K jobs each with up to N tasks.

`MAKEOPTS` and `EMERGE_DEFAULT_OPTS` are suited for long emerges including multiple source code files and make the most of the `--jobs` parameter. They should be used with caution and be commented out when they cause [emerge] errors.

## [See also]

-   [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS") --- a variable that defines and limits how many parallel make jobs can be launched from Portage.
-   [Knowledge Base:Emerge out of memory](https://wiki.gentoo.org/wiki/Knowledge_Base:Emerge_out_of_memory "Knowledge Base:Emerge out of memory")
-   [Portage niceness](https://wiki.gentoo.org/wiki/Portage_niceness "Portage niceness") --- describes some configuration options available for system administrators to help manage [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")\'s resource usage.