`MAKEOPTS` is a variable that defines and limits how many parallel make jobs can be launched from Portage. It can be set in the [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#MAKEOPTS "/etc/portage/make.conf")] configuration file.

** Tip**\
As a rule of thumb, MAKEOPTS jobs should be limited to less than or equal to the minimum of the size of RAM/2GB or CPU thread count.

The parallel jobs entry ensures that, when [make] is invoked, it knows how many parallel sessions it is allowed to trigger (when parallel sessions are possible of course). This is completely within the scope of that make command and has no influence on parallel installations (which is triggered through [emerge] with [\--jobs=X] option). The recommended value is the number of logical processors in the CPU.

On a system with one Intel Core i7 CPU the following command shows the numbering of the available logical CPUs.

`root `[`#`]`lscpu`

    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    CPU(s):              8
    On-line CPU(s) list: 0-8
    Thread(s) per core:  2
    Core(s) per socket:  4
    Socket(s):           1

The [make] program creates parallel tasks based on the system\'s current load average and the [\--load-average] limit. Since the load average is a damped value, the load-average jobs limitation can be sensibly set slightly above the number of available CPUs. For 4 physical cores with 2 threads per core, or 8 logical cores, the `MAKEOPTS` variable *could* be set to:

[FILE] **`/etc/portage/make.conf`**

    MAKEOPTS="--jobs 8 --load-average 9"

Also, since Portage 3.0.31^[\[1\]](#cite_note-1)^ and 3.0.53^[\[2\]](#cite_note-2)^, [\--jobs] and [\--load-average] respectively default to the number of threads returned by [nproc] if `MAKEOPTS` is unset.

Jobs should also be limited by RAM. Recent [gcc] versions can take 1.5 GB to 2 GB of RAM per job for large C++ codebases. For systems with 8 logical CPUs and only 4 GB RAM, `MAKEOPTS` should be lowered to `-j2` so that the system can run the basics and also compile without hitting [swap](https://wiki.gentoo.org/wiki/Swap "Swap") very often slowing things down. To measure the time needed to compile the [[[app-misc/mc]](https://packages.gentoo.org/packages/app-misc/mc)[]] package with 4 jobs:

`root `[`#`]`time MAKEOPTS="-j4" emerge app-misc/mc`

## Contents

-   [[1] [MAKEOPTS on a per-package basis]](#MAKEOPTS_on_a_per-package_basis)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)
-   [[4] [References]](#References)

## [MAKEOPTS on a per-package basis]

Packages can be emerged with different `MAKEOPTS` values on a per-package basis. See [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")] for details.

## [See also]

-   [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS") --- a variable for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") that defines entries to be appended to the [emerge] command line.
-   [Knowledge Base:Emerge out of memory](https://wiki.gentoo.org/wiki/Knowledge_Base:Emerge_out_of_memory "Knowledge Base:Emerge out of memory")
-   [Portage niceness](https://wiki.gentoo.org/wiki/Portage_niceness "Portage niceness") --- describes some configuration options available for system administrators to help manage [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")\'s resource usage.
-   [steve](https://wiki.gentoo.org/wiki/Steve "Steve") --- a jobserver implementation for Gentoo

## [External resources]

-   [MAKEOPTS="-j\$ +1″ is NOT the best optimization](https://blogs.gentoo.org/ago/2013/01/14/makeopts-jcore-1-is-not-the-best-optimization/)
-   [Parallel Builds With Gentoo's Emerge](https://www.preney.ca/paul/archives/341)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitweb.gentoo.org/proj/portage.git/commit/?id=5d2af567772bb12b073f1671daea6263055cbdc2](https://gitweb.gentoo.org/proj/portage.git/commit/?id=5d2af567772bb12b073f1671daea6263055cbdc2)]]
2.  [[[↑](#cite_ref-2)] [[https://gitweb.gentoo.org/proj/portage.git/commit/?id=de7be7f45ee54e3f789def46542919550687d15e](https://gitweb.gentoo.org/proj/portage.git/commit/?id=de7be7f45ee54e3f789def46542919550687d15e)]]