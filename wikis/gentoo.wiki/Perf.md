[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Perf&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Official project wiki](https://perfwiki.github.io)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/perf)

**perf** is a tool for profiling Linux with performance counters. It can instrument CPU performance counters, tracepoints, kprobes, and uprobes (dynamic tracing). It is also capable of lightweight profiling.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [System-wide profiling]](#System-wide_profiling)
    -   [[3.2] [Performance counters]](#Performance_counters)
        -   [[3.2.1] [Per-command]](#Per-command)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Compiler flags]](#Compiler_flags)
    -   [[4.2] [Missing source code annotations]](#Missing_source_code_annotations)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/perf](https://packages.gentoo.org/packages/dev-util/perf) [[]] [Userland tools for Linux Performance Counters]

  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+doc`](https://packages.gentoo.org/useflags/+doc)                       Build documentation and man pages. With this USE flag disabled, the \--help parameter for perf and its sub-tools will not be available. This is optional because it depends on a few documentation handling tools that are not always welcome on user systems.
  [`+libtraceevent`](https://packages.gentoo.org/useflags/+libtraceevent)   Enable dev-libs/libtraceevent support
  [`+libtracefs`](https://packages.gentoo.org/useflags/+libtracefs)         Enable dev-libs/libtracefs support
  [`+python`](https://packages.gentoo.org/useflags/+python)                 Add optional support/bindings for the Python language
  [`+slang`](https://packages.gentoo.org/useflags/+slang)                   Add support for the slang text display library (it\'s like ncurses, but different)
  [`babeltrace`](https://packages.gentoo.org/useflags/babeltrace)           Enable dev-util/babeltrace support
  [`big-endian`](https://packages.gentoo.org/useflags/big-endian)           Big-endian toolchain support
  [`bpf`](https://packages.gentoo.org/useflags/bpf)                         Enable support for eBPF features with dev-libs/libbpf
  [`caps`](https://packages.gentoo.org/useflags/caps)                       Use Linux capabilities library to control privilege
  [`capstone`](https://packages.gentoo.org/useflags/capstone)               Use dev-libs/capstone for disassembly support
  [`crypt`](https://packages.gentoo.org/useflags/crypt)                     Add support for encryption \-- using mcrypt or gpg where applicable
  [`debug`](https://packages.gentoo.org/useflags/debug)                     Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                         Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`java`](https://packages.gentoo.org/useflags/java)                       Add support for Java
  [`libpfm`](https://packages.gentoo.org/useflags/libpfm)                   Enable dev-libs/libpfm support
  [`lzma`](https://packages.gentoo.org/useflags/lzma)                       Support for LZMA compression algorithm
  [`numa`](https://packages.gentoo.org/useflags/numa)                       Enable NUMA support using sys-process/numactl (NUMA kernel support is also required)
  [`perl`](https://packages.gentoo.org/useflags/perl)                       Add support for Perl as a scripting language for perf tools.
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)             Add support to define SDT event in perf tools.
  [`tcmalloc`](https://packages.gentoo.org/useflags/tcmalloc)               Use the dev-util/google-perftools libraries to replace the malloc() implementation with a possibly faster one
  [`unwind`](https://packages.gentoo.org/useflags/unwind)                   Use sys-libs/libunwind for frame unwinding support.
  ------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-22 14:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/perf`

## [Configuration]

perf can be configured via [\~/.perfconfig] or the system-wide file [/etc/perfconfig].

A suggested config to start with is:

[FILE] **`~/.perfconfig`**

    [annotate]
            # Other disassemblers can't handle splitdebug
            disassemblers = objdump
    [buildid]
            # The default is ~/.debug
            dir = ~/.config/debug

## [Usage]

### [System-wide profiling]

One can monitor the whole system in a (h)top-like format using `perf top`. While (h)top shows CPU usage at a *program* level, *perf top* shows usage down to a symbol (function) level. It allows further drilling down to see exactly which lines are the most expensive at any given time.

### [Performance counters]

To monitor performance counters system-wide, one can simply run `perf stat`, in the following example, it profiles the system for 5 seconds.

** Note**\
The argument, `-s 2`, is the SIGINT signal (the same one that C-c sends). Using timeout without this signal will result in no output being displayed upon exit.

`user `[`$`]`timeout -s 2 5s perf stat`

     Performance counter stats for 'system wide':

            119,873.70 msec cpu-clock                        #   23.996 CPUs utilized
               608,052      context-switches                 #    5.072 K/sec
                52,088      cpu-migrations                   #  434.524 /sec
                54,966      page-faults                      #  458.533 /sec
       149,286,631,432      instructions                     #    1.63  insn per cycle
                                                      #    0.08  stalled cycles per insn
        91,639,578,301      cycles                           #    0.764 GHz
        12,251,888,547      stalled-cycles-frontend          #   13.37% frontend cycles idle
        19,086,150,804      branches                         #  159.219 M/sec
           493,116,174      branch-misses                    #    2.58% of all branches

           4.995528985 seconds time elapsed

#### [Per-command]

To see the performance counters (like branch misses) for a specific command, simply add the command after the [perf stat] argument. In this example, the command `emerge -ep @world` will be used.

`user `[`$`]`perf stat emerge -ep @world`

     Performance counter stats for 'emerge -ep @world':

             16,518.88 msec task-clock                       #    0.970 CPUs utilized
                18,177      context-switches                 #    1.100 K/sec
                15,651      cpu-migrations                   #  947.462 /sec
               324,994      page-faults                      #   19.674 K/sec
        94,669,490,050      instructions                     #    1.37  insn per cycle
                                                      #    0.14  stalled cycles per insn
        68,918,358,065      cycles                           #    4.172 GHz
        13,046,547,573      stalled-cycles-frontend          #   18.93% frontend cycles idle
        18,809,738,679      branches                         #    1.139 G/sec
           544,326,478      branch-misses                    #    2.89% of all branches

          17.034427384 seconds time elapsed

          14.761382000 seconds user
           1.708188000 seconds sys

## [Troubleshooting]

### [Compiler flags]

For common perf functionality, it needs a way to trace the stack for an application. There are two ways perf currently supports:

-   Frame pointers
-   DWARF-based

Frame pointers require building packages with *-fno-omit-frame-pointer* and has a small runtime penalty accordingly, while using DWARF-based unwinding is [slow and requires huge amounts](https://rwmj.wordpress.com/2023/02/14/frame-pointers-vs-dwarf-my-verdict/) of disk space.

This will change in future with [SFrames](https://wiki.gentoo.org/wiki/Project:Toolchain/SFrame "Project:Toolchain/SFrame") which facilitates fast stack tracing, has no runtime cost, and is compact.

### [Missing source code annotations]

perf has an [s] hotkey to enable source code details when annotating a symbol. This [depends on the disassembler](https://lore.kernel.org/all/Z_S_JB_L_t9viciV@google.com/) used by perf. As of 2025-07-02, this only works with GNU Binutils\' [objdump]. To configure perf to always use [objdump], run:

`user `[`$`]`perf config annotate.disassemblers=objdump`

## [External resources]

-   [perf and DWARF and fork()](https://trofi.github.io/posts/215-perf-and-dwarf-and-fork.html)
-   [perf top: an awesome way to spy on CPU usage](https://jvns.ca/blog/2016/02/24/perf-top-my-new-best-friend/)