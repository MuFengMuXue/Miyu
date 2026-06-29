**Resources**

[[]][Home](https://www.oracle.com/linux/downloads/linux-dtrace.html)

[[]][Official documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-guide/)

[[]][Official project wiki](https://github.com/oracle/dtrace/wiki)

[[]][Package information](https://packages.gentoo.org/packages/dev-debug/dtrace)

[[]][Wikipedia](https://en.wikipedia.org/wiki/DTrace "wikipedia:DTrace")

[[]][GitHub](https://github.com/oracle/dtrace)

**DTrace** is a dynamic tracing tool for analysing or debugging the whole system. It can analyse and inspect both the kernel (inc. modules) and userland applications. It might be used for both analysing performance issues, but also analysing unexpected or wrong behavior from either userland or the kernel.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel configuration]](#Kernel_configuration)
        -   [[1.1.1] [dist-kernel]](#dist-kernel)
    -   [[1.2] [Userland]](#Userland)
        -   [[1.2.1] [systemd]](#systemd)
        -   [[1.2.2] [OpenRC]](#OpenRC)
-   [[2] [Getting started]](#Getting_started)
    -   [[2.1] [Syntax]](#Syntax)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Investigating locks]](#Investigating_locks)
    -   [[3.2] [Probing a probe]](#Probing_a_probe)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Basic sanity checks]](#Basic_sanity_checks)
    -   [[4.2] [Faulting on a bad address]](#Faulting_on_a_bad_address)
    -   [[4.3] [Online examples not working]](#Online_examples_not_working)
        -   [[4.3.1] [execveat_common]](#execveat_common)
        -   [[4.3.2] [open]](#open)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel configuration]

** Warning**\
Kernel debug info is incompatible with `CONFIG_GCC_PLUGIN_RANDSTRUCT`, see [https://gcc.gnu.org/PR84052](https://gcc.gnu.org/PR84052). A workaround is disabling [[[hardened]](https://packages.gentoo.org/useflags/hardened)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] on dist-kernels if using them for now.

This modern DTrace implementation is based on *eBPF* and requires a suite of kernel configuration options which the ebuild checks for. In particular:

[KERNEL] **Debug Options**

    General Setup ->
     Compile-time checks and compiler options ->
       <*> Configure standard kernel features (expert users) ->
         <*> Load all symbols for debugging/ksymoops
         <*> Include all symbols in kallsyms Search for <code>CONFIG_KALLSYMS_ALL</code> to find this item.
    File systems ->
       <*> FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.
       <*> Character device in Userspace support Search for <code>CONFIG_CUSE</code> to find this item.
    Kernel Hacking  ->
       <*> Tracers -> Search for <code>CONFIG_FTRACE</code> to find this item.
        <*> Trace syscalls Search for <code>CONFIG_FTRACE_SYSCALLS</code> to find this item.
        <*> Enable uprobes-based dynamic events Search for <code>CONFIG_UPROBE_EVENTS</code> to find this item.
        <*> enable/disable function tracing dynamically Search for <code>CONFIG_DYNAMIC_FTRACE</code> to find this item.
        <*> Kernel Function Tracer Search for <code>CONFIG_FUNCTION_TRACER</code> to find this item.
       <*> Generate BTF typeinfo Search for <code>CONFIG_DEBUG_INFO_BTF</code> to find this item.

#### [dist-kernel]

When using a [Distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel"), enabling [[[debug]](https://packages.gentoo.org/useflags/debug)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] for the relevant \*-kernel package covers some of these.

If using gentoo-kernel\[hardened\], the following workaround config.d snippet can be used:

[FILE] **`/etc/kernel/config.d/50hardened.config`**

    # CONFIG_RANDSTRUCT_NONE is not set
    # CONFIG_RANDSTRUCT_FULL is not set
    # CONFIG_RANDSTRUCT_PERFORMANCE is not set
    # CONFIG_RANDSTRUCT is not set
    # CONFIG_GCC_PLUGIN_RANDSTRUCT is not set

\
A general snippet for DTrace is below:

[FILE] **`/etc/kernel/config.d/50dtrace.config`**

    CONFIG_CUSE=m
    CONFIG_FPROBE=y

    CONFIG_DEBUG_INFO=y
    # CONFIG_DEBUG_INFO_NONE is not set
    CONFIG_DEBUG_INFO_DWARF5=y
    # CONFIG_DEBUG_INFO_REDUCED is not set
    # CONFIG_DEBUG_INFO_COMPRESSED_NONE is not set
    CONFIG_DEBUG_INFO_COMPRESSED_ZLIB=y
    # CONFIG_DEBUG_INFO_COMPRESSED_ZSTD is not set
    # CONFIG_DEBUG_INFO_SPLIT is not set
    CONFIG_DEBUG_INFO_BTF=y
    CONFIG_PAHOLE_HAS_SPLIT_BTF=y
    CONFIG_PAHOLE_HAS_LANG_EXCLUDE=y
    CONFIG_DEBUG_INFO_BTF_MODULES=y
    # CONFIG_MODULE_ALLOW_BTF_MISMATCH is not set
    # CONFIG_GDB_SCRIPTS is not set
    CONFIG_PROBE_EVENTS_BTF_ARGS=y

** Note**\
Remember, the above only works with [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]]

### [Userland]

Modern versions of DTrace are Extended Berkeley Packet Filter ([eBPF](https://en.wikipedia.org/wiki/eBPF "wikipedia:eBPF"))-based, so there\'s no need for a separate kernel module, or any patches.

Simply install the userland tools:

`root `[`#`]`emerge --ask dev-debug/dtrace`

** Note**\
[[[sys-devel/bpf-toolchain]](https://packages.gentoo.org/packages/sys-devel/bpf-toolchain)[]] is used to avoid needing to manually build a cross-compiler with [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev").

#### [systemd]

`root `[`#`]`systemctl enable --now dtprobed`

#### [OpenRC]

`root `[`#`]`rc-update add dtprobed default && rc-service dtprobed start`

## [Getting started]

The DTrace framework is centred around two concepts:

-   *D scripts* (not to be confused with D programming language, also called [Dlang](https://wiki.gentoo.org/wiki/Dlang "Dlang")): these can be one-liners or whole scripts with a traditional shebang for convenience;
-   *probes* which attach to some system component of interest, like a part of a kernel module, or userland application

Other terminology:

-   *providers* publishes available *probes*
-   *modules* provide an implementation of a *probe*

For example, the *syscall* provider, via the *vmlinux* module, has various probes for each syscall at *entry* and *return*.

Following the [official D script tutorial](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-tutorial/) is strongly recommended.

### [Syntax]

D Script\'s syntax is roughly [Awk](https://wiki.gentoo.org/wiki/Awk "Awk")-like. Below is a basic skeleton:

[FILE]

    #!/usr/bin/env dtrace -s

    PROBE
    /optional predicate condition/


`BEGIN` and `END` blocks are special, like constructors/destructors:

[FILE]

    #!/usr/bin/env dtrace -s

    /* Sample script which starts up, prints a message, then exits and shows
       another message before terminating. */

    BEGIN


    END


A fully qualified probe name takes the form `provider:module:function:name`. Wildcards can be used to match multiple probes. To leave a field blank, use a colon-separator, e.g. `provider::function:name`. In general, DTrace tries to solve ambiguous names rather than bailing out.

For more information, see the [D Program Syntax Reference](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-v2-guide/d_program_syntax_reference.html#reference_h2t_nbw_kwb).

## [Usage]

DTrace shines in investigating emerging incidents where one-liners or small scripts can quickly be written to both gather information but also to prove or disprove a theory about root causes. As a result, the most important thing for using DTrace is being familiar with its primitives, rather than having a large corpus of pre-existing scripts ready to use.

### [Investigating locks]

Suppose a system has a mysterious lock file being rapidly created and then deleted.

Artificially create such a scenario with a loop:

`root `[`#`]`while true ; do flock -s $(mktemp) sleep 1 ; done`

This can be easily investigated:

[FILE]

    #!/usr/bin/env dtrace -s
    #pragma D option quiet

    syscall::openat:entry


    syscall::openat:return


    syscall::flock:entry


### [Probing a probe]

When writing a script, one might need to know the argument types (prototype) of a probe. For example, to investigate the parameters for *syscall::vmlinux::openat* and *syscall::vmlinux::openat2*:

`root `[`#`]`dtrace -l -n openat*:entry -v`

       ID   PROVIDER            MODULE                          FUNCTION NAME
    124115    syscall           vmlinux                            openat entry

    [...]

            Argument Types
                    args[0]: int
                    args[1]: char *
                    args[2]: int
                    args[3]: umode_t

    124113    syscall           vmlinux                           openat2 entry

    [...]

            Argument Types
                    args[0]: int
                    args[1]: char *
                    args[2]: struct open_how *
                    args[3]: size_t

## [Troubleshooting]

### [Basic sanity checks]

First, have DTrace enable a trivial probe and return once it is hit:

`root `[`#`]`dtrace -n 'BEGIN '`

    dtrace: description 'BEGIN ' matched 1 probe
    CPU     ID                    FUNCTION:NAME
     28      1                           :BEGIN

Check whether the syscall probe has very basic functionality:

`root `[`#`]`dtrace -n 'syscall:::entry '`

    dtrace: description 'syscall:::entry ' matched 344 probes
    CPU     ID                    FUNCTION:NAME
      3 124015                        bpf:entry

If either of these commands hang or don\'t produce a table as above, DTrace isn\'t working correctly. It may be caused by exotic optimization flags.

All the available probes can be listed with [dtrace -l]:

`root `[`#`]`dtrace -l`

       ID   PROVIDER            MODULE                          FUNCTION NAME
        1     dtrace                                                     BEGIN
        2     dtrace                                                     END
        3     dtrace                                                     ERROR
        4        cpc                                                     perf_count_hw_cpu_cycles-all-1000000000
        5        cpc                                                     cycles-all-1000000000
        6        cpc                                                     cpu_cycles-all-1000000000
        7        cpc                                                     perf_count_hw_instructions-all-1000000000
        8        cpc                                                     instructions-all-1000000000
    [...]

As of August 2024, on an **[\~amd64]** system with linux-6.6, around 125000 probes are registered. If the number is substantially **lower** than that, it\'s possible some required kernel config options are not enabled.

### [Faulting on a bad address]

Using a valid argument in an entry probe which the process hasn\'t yet accessed [might cause a fault](https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/dtrace-guide/avoiding-errors.html). To workaround this, store the argument in `this->foo` with *copyinstr*.

### [Online examples not working]

Some examples online may not work for a few reasons:

1.  Relying on unstable kernel ABI so \'function\' names or types may have changed
2.  The example relies on assumptions about libc and how it wraps syscalls
3.  Overly specific names

Below are a few examples of both a problem and analysis to fix it. The same methods can be applied to other bad examples on the internet.

#### [execveat_common]

For example, consider this script for tracing *execve*:

`root `[`#`]`dtrace -n 'proc::do_execveat_common:exec '`

    dtrace: invalid probe specifier proc::do_execveat_common:exec : probe description proc::do_execveat_common:exec does not match any probes

The specification *proc::do_execveat_common:exec* is prone to internal changes. BPF-based DTrace provides a tracepoint for *exec* elsewhere.

To fix it, use the more generic proc tracepoint:

`root `[`#`]`dtrace -n 'proc:::exec '`

    dtrace: description 'proc:::exec ' matched 1 probe
    CPU     ID                    FUNCTION:NAME
      2 123651                            :exec   /usr/sbin/utempter
      3 123651                            :exec   /usr/sbin/utempter
     10 123651                            :exec   /bin/bash
      1 123651                            :exec   /usr/bin/dircolors

#### [open]

For example, consider this script for tracing *open*:

`root `[`#`]`dtrace -n 'syscall::open:entry '`

    dtrace: description 'syscall::open:entry ' matched 1 probe
    [Likely to have no further output]

Most functions used to open files don\'t actually use the *open* syscall in glibc, but one of the other wrappers instead. Note that arg0 changes to arg1 here too as we see *openat* is being used which has different parameters:

`root `[`#`]`dtrace -n 'syscall::open*:entry '`

    dtrace: description 'syscall::open*:entry ' matched 5 probes
    CPU     ID                    FUNCTION:NAME
      5 128754                     openat:entry cc1plus          /usr/lib/gcc/x86_64-pc-linux-gnu/15/include/g++-v15/bits/stl_algobase.h

      2 128754                     openat:entry cc1plus          /usr/lib/gcc/x86_64-pc-linux-gnu/15/include/g++-v15/bits/stl_heap.h

      2 128754                     openat:entry cc1plus          /usr/lib/gcc/x86_64-pc-linux-gnu/15/include/g++-v15/bits/uniform_int_dist.h

      2 128754                     openat:entry cc1plus          /usr/lib/gcc/x86_64-pc-linux-gnu/15/include/g++-v15/bits/stl_construct.h

      2 128754                     openat:entry cc1plus          /usr/lib/gcc/x86_64-pc-linux-gnu/15/include/g++-v15/bits/stl_tempbuf.h

## [See also]

-   [SystemTap](https://wiki.gentoo.org/wiki/SystemTap "SystemTap") --- powerful tool that provides an infrastructure to simplify the gathering of information about the running Linux kernel or userspace programs

## [External resources]

-   [Linux Tracing Systems and How They Fit Together](https://jvns.ca/blog/2017/07/05/linux-tracing-systems/).
-   [Oracle Help Center - Introducing DTrace](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-tutorial/) (tutorial)
-   [Oracle Help Center - Using DTrace for System Tracing](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-v2-guide/)
-   [Oracle Help Center - DTrace Reference Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/dtrace-guide/) (older)
-   [Oracle Linux Training Station - DTrace](https://oracle-samples.github.io/oltrain/tracks/ol/dtrace/)