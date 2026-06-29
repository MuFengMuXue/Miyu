**Resources**

[[]][Home](https://sourceware.org/systemtap/)

[[]][Official documentation](https://sourceware.org/systemtap/documentation.html)

[[]][Official project wiki](https://sourceware.org/systemtap/wiki)

[[]][Package information](https://packages.gentoo.org/packages/dev-debug/systemtap)

[[]][GitWeb](https://sourceware.org/git/systemtap.git)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SystemTap "wikipedia:SystemTap")

**SystemTap** ([stap]) is a powerful tool that provides an infrastructure to simplify the gathering of information about the running Linux kernel or userspace programs^[\[1\]](#cite_note-SystemTap_-_Debian_Wiki-1)^. It allows users to write and reuse simple scripts to deeply examine the activities of a running Linux system. These scripts can be designed to extract data, filter it, and summarize it quickly (and safely), enabling the diagnosis of complex performance (or even functional) problems.^[\[2\]](#cite_note-SystemTap_Beginners_Guide-2)^

## Contents

-   [[1] [How it Works]](#How_it_Works)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Installation]](#Installation)
    -   [[2.3] [Basic Usage]](#Basic_Usage)
-   [[3] [Viewing Kernel Information]](#Viewing_Kernel_Information)
    -   [[3.1] [Real-world Usage]](#Real-world_Usage)
-   [[4] [See Also]](#See_Also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [How it Works]

SystemTap scripts are written in the SystemTap scripting language, are then compiled to C-code kernel modules and inserted into the kernel. This allows the scripts to instrument the execution of functions or statements in the kernel or user-space.

## [Usage]

SystemTap provides a command line interface and a scripting language to examine the activities of a running Linux system, particularly the kernel, in fine detail.

### [Kernel]

As SystemTap taps into the kernel at a low level, it requires that debug symbols be enabled (DWARF5, specifically) - for Gentoo this means reconfiguring the kernel^[\[3\]](#cite_note-3)^.

For [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]:

[KERNEL] **debug symbol generation**

    -> Kernel hacking
              -> Compile-time checks and compiler options
                   -> Debug information (Generate DWARF Version 5 debuginfo)

For [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]]:

[FILE] **`FILE /etc/kernel/config.d/99-debugsyms.config`**

    CONFIG_DEBUG_INFO=y
    CONFIG_DEBUG_INFO_DWARF5=y

Additional options that are probably already enabled: `CONFIG_KPROBES`, `CONFIG_RELAY`, `CONFIG_DEBUG_FS`, `CONFIG_MODULES`, `CONFIG_MODULE_UNLOAD`, `CONFIG_UPROBES`.

Users should try to reduce the number of modules / enabled options for an instrumented kernel where possible---`CONFIG_DEBUG_INFO` can multiply disk space usage. Be sure to leave `CONFIG_DEBUG_INFO_SPLIT` disabled; SystemTap doesn\'t handle split debuginfo yet.

### [Installation]

`root `[`#`]`emerge --ask dev-util/systemtap`

### [Basic Usage]

After installation, a basic probe to read the VFS can be performed to validate SystemTap functionality:

`root `[`#`]`stap -v -e 'probe vfs.read ' `

    Pass 1: parsed user script and 45 library script(s) in 340usr/0sys/358real ms.
    Pass 2: analyzed script: 1 probe(s), 1 function(s), 0 embed(s), 0 global(s) in 290usr/260sys/568real ms.
    Pass 3: translated to C into "/tmp/stapiArgLX/stap_e5886fa50499994e6a87aacdc43cd392_399.c" in 490usr/430sys/938real ms.
    Pass 4: compiled C into "stap_e5886fa50499994e6a87aacdc43cd392_399.ko" in 3310usr/430sys/3714real ms.
    Pass 5: starting run.
    read performed
    Pass 5: run completed in 10usr/40sys/73real ms.

This command instructs SystemTap to print read performed and then exit properly once a virtual file system read is detected. If the SystemTap deployment was successful, it prints output similar to the above; the last three lines of the output (beginning with Pass 5) indicate that SystemTap was able to successfully create the instrumentation to probe the kernel, run the instrumentation, detect the event being probed (in this case, a virtual file system read), and execute a valid handler (print text then close it with no errors)^[\[4\]](#cite_note-stap-validation-4)^.

## [Viewing Kernel Information]

SystemTap can be used to view information about the kernel in various ways. For example, it can be used to identify the top system calls used by the system. It can also be used to determine which processes are performing the highest volume of system calls, providing more data in investigating systems for polling processes and other resource hogs.

### [Real-world Usage]

This example describes using SystemTap to view the \`inet_getname\` function which was identified as the source of the following [nfsd] errors: `nfsd: peername failed (err 107)!`

** Note**\
`inet6_getname` may cause failures if ipv6 is not enabled or loaded as a module. In that case just remove the line.

[FILE] **`nfsd_peername.stp`**

    probe kernel.function("inet_getname").call,
          module("ipv6").function("inet6_getname").call

    }

    probe kernel.function("inet_getname").return,
          module("ipv6").function("inet6_getname").return

    }

When run, the above script will log calls made to `inet_gentame` from binaries named [nfsd], as well as the return value:

`root `[`#`]`vim nfsd_peername.stp`

`root `[`#`]`stap -v nfsd_peername.stp`

    Pass 1: parsed user script and 114 library scripts using 57340virt/40276res/5700shr/35220data kb, in 120usr/10sys/130real ms.
    Pass 2: analyzed script: 6 probes, 24 functions, 9 embeds, 3 globals using 228712virt/213276res/7376shr/206592data kb, in 2270usr/570sys/2737real ms.
    Pass 3: translated to C into "/tmp/stapkilbvn/stap_aaaa6994e39808fec232416d081ab400_33413_src.c" using 228712virt/213468res/7568shr/206592data kb, in 10usr/20sys/32real ms.
    Pass 4: compiled C into "stap_aaaa6994e39808fec232416d081ab400_33413.ko" in 7670usr/1440sys/8936real ms.
    Pass 5: starting run.
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.84 port: 750 state: TCP_CLOSE_WAIT
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: 0
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.76 port: 940 state: TCP_CLOSE
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: -107
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.72 port: 671 state: TCP_CLOSE
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: -107
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.82 port: 742 state: TCP_CLOSE
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: -107
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.79 port: 749 state: TCP_CLOSE
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: -107
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.62 port: 886 state: TCP_ESTABLISHED
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: 0
    Thu Dec  7 15:19:49 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.93 port: 861 state: TCP_ESTABLISHED
    Thu Dec  7 15:19:49 2023 AEST nfsd <- inet_getname ret: 0
    Thu Dec  7 15:19:50 2023 AEST nfsd -> inet_getname addr: 10.xxx.xxx.76 port: 940 state: TCP_ESTABLISHED
    Thu Dec  7 15:19:50 2023 AEST nfsd <- inet_getname ret: 0

## [See Also]

-   [DTrace](https://wiki.gentoo.org/wiki/DTrace "DTrace") --- dynamic tracing tool for analysing or debugging the whole system

## [External resources]

-   [SUSE Documentation](https://documentation.suse.com/sles/15-SP1/html/SLES-all/cha-tuning-systemtap.html)

## [References]

1.  [[[↑](#cite_ref-SystemTap_-_Debian_Wiki_1-0)] [[https://wiki.debian.org/SystemTap](https://wiki.debian.org/SystemTap)]]
2.  [[[↑](#cite_ref-SystemTap_Beginners_Guide_2-0)] [[https://sourceware.org/systemtap/SystemTap_Beginners_Guide/](https://sourceware.org/systemtap/SystemTap_Beginners_Guide/)]]
3.  [[[↑](#cite_ref-3)] [[https://sourceware.org/systemtap/wiki/SystemTapWithSelfBuiltKernel](https://sourceware.org/systemtap/wiki/SystemTapWithSelfBuiltKernel)]]
4.  [[[↑](#cite_ref-stap-validation_4-0)] [[https://sourceware.org/systemtap/SystemTap_Beginners_Guide/using-systemtap.html#installproper](https://sourceware.org/systemtap/SystemTap_Beginners_Guide/using-systemtap.html#installproper)]]