**Resources**

[[]][Home](https://www.sourceware.org/gdb/)

[[]][Official documentation](https://www.sourceware.org/gdb/documentation/)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/gdb)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Debugger "wikipedia:GNU Debugger")

[[]][GitWeb](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git)

[[]][Official project wiki](https://sourceware.org/gdb/wiki/)

[[]][Bugs (upstream)](https://www.sourceware.org/gdb/bugs/)

[[]][[#gdb](ircs://irc.libera.chat/#gdb)] ([[webchat](https://web.libera.chat/#gdb)])

The **GNU debugger (GDB)**, is used to investigate runtime errors that normally involve memory corruption.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Alternative interfaces]](#Alternative_interfaces)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Tweaks]](#Tweaks)
        -   [[2.2.1] [Silent startup]](#Silent_startup)
        -   [[2.2.2] [Persistent history]](#Persistent_history)
    -   [[2.3] [Retain debug symbols]](#Retain_debug_symbols)
    -   [[2.4] [Caching]](#Caching)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Enabling core dumps]](#Enabling_core_dumps)
    -   [[3.2] [Running the program with GDB]](#Running_the_program_with_GDB)
    -   [[3.3] [Enabling ASLR]](#Enabling_ASLR)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-debug/gdb](https://packages.gentoo.org/packages/dev-debug/gdb) [[]] [GNU debugger]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  [`+debuginfod`](https://packages.gentoo.org/useflags/+debuginfod)             Enable debuginfod support via dev-libs/elfutils libdebuginfod
  [`+python`](https://packages.gentoo.org/useflags/+python)                     Enable support for the new internal scripting language, as well as extended pretty printers
  [`+server`](https://packages.gentoo.org/useflags/+server)                     Install the \"gdbserver\" program (useful for embedded/remote targets)
  [`+xml`](https://packages.gentoo.org/useflags/+xml)                           Support parsing XML data files needed (at least) for cpu features, memory maps, and syscall tracing
  [`babeltrace`](https://packages.gentoo.org/useflags/babeltrace)               Enable dev-util/babeltrace support
  [`cet`](https://packages.gentoo.org/useflags/cet)                             Enable Intel Control-flow Enforcement Technology.
  [`guile`](https://packages.gentoo.org/useflags/guile)                         Add support for the guile Scheme interpreter
  [`lzma`](https://packages.gentoo.org/useflags/lzma)                           Support lzma compression in ELF debug info
  [`multitarget`](https://packages.gentoo.org/useflags/multitarget)             Support all known targets in one gdb binary
  [`nls`](https://packages.gentoo.org/useflags/nls)                             Add Native Language Support (using gettext - GNU locale utilities)
  [`rocm`](https://packages.gentoo.org/useflags/rocm)                           Enable support for AMD GPU debugging via dev-libs/rocdbgapi
  [`sim`](https://packages.gentoo.org/useflags/sim)                             Build gdb\'s simulators for various hardware platforms. See https://sourceware.org/gdb/wiki/Sim.
  [`source-highlight`](https://packages.gentoo.org/useflags/source-highlight)   Enable listing highlighting via dev-util/source-highlight
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)                     Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`xxhash`](https://packages.gentoo.org/useflags/xxhash)                       Use dev-libs/xxhash to speed up internal hashing.
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                           Enable support for ZSTD compression
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-11 11:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-debug/gdb`

### [Alternative interfaces]

gdb is a complex program with many alternative interfaces, some optimized for different use cases:

-   gdb command - \"gdb tui enable\" - GDB TUI mode (GDB Text User Interface) included, requires the [[[dev-util/debugedit]](https://packages.gentoo.org/packages/dev-util/debugedit)[]] for extra info
-   [[[dev-debug/cgdb]](https://packages.gentoo.org/packages/dev-debug/cgdb)[]] - terminal UI, ncurses, bit older
-   [[[dev-debug/gef]](https://packages.gentoo.org/packages/dev-debug/gef)[]] - terminal UI, just run [gef] instead
-   [[[dev-debug/pwndbg]](https://packages.gentoo.org/packages/dev-debug/pwndbg)[]] - terminal UI, just run [pwndbg] instead
-   [[[dev-util/seer]](https://packages.gentoo.org/packages/dev-util/seer)[]] - GUI, quite new
-   Emacs with gud-gdb - The Grand Unified Debugger (or GUD for short, is an Emacs major mode for debugging)

## [Configuration]

### [Files]

[gdb] can be configured via the following files:

-   [\~/.config/gdb/gdbearlyinit] which is checked before any other configuration file
-   [\~/.config/gdb/gdbinit] which is the primary configuration file

### [Tweaks]

#### [Silent startup]

By default, gdb is quite noisy at startup:

`user `[`$`]`gdb`

    GNU gdb (Gentoo 13.0.90_p20230110 vanilla) 13.0.90.20230110-git
    Copyright (C) 2023 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    Type "show copying" and "show warranty" for details.
    This GDB was configured as "x86_64-pc-linux-gnu".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <https://bugs.gentoo.org/>.
    Find the GDB manual and other documentation resources online at:
        <http://www.gnu.org/software/gdb/documentation/>.

    For help, type "help".
    Type "apropos word" to search for commands related to "word".
    (gdb)

To change this, enable `startup-quietly` in [\~/.config/gdb/gdbearlyinit]:

[FILE] **`~/.config/gdb/gdbearlyinit`**

    set startup-quietly on

Then afterwards, gdb is far quieter:

`user `[`$`]`gdb`

    (gdb)

#### [Persistent history]

By default, gdb does not retain command history or scrollback between runs. This can be changed via the various `history` toggles in [\~/.config/gdb/gdbinit].

[FILE] **`~/.config/gdb/gdbinit`**

    set history filename ~/.gdb_history
    set history save on
    set history size unlimited
    set history remove-duplicates unlimited

### [Retain debug symbols]

See [Installing debugging information for packages](https://wiki.gentoo.org/wiki/Debugging#Installing_debugging_information_for_packages "Debugging").

In order to debug a program, [emerge] the program either with `FEATURES="nostrip"` to prevent the stripping of debug symbols, or with the needed [package.env] settings.

Once debug symbols are set, it is time to begin debugging the program.

If more assistance is needed, such as being able to see the code within GDB TUI (GDB Text User Interface), install the [[[dev-util/debugedit]](https://packages.gentoo.org/packages/dev-util/debugedit)[]] package and include `FEATURES="installsources"`.

Although not really needed for meaningful [backtraces](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces "Project:Quality Assurance/Backtraces"), this significantly helps when actively coding.

### [Caching]

gdb can create and maintain a cache when it reads debug information, but only when build IDs are available. Gentoo enabled build IDs by default in 2025/02 ([[[bug #953869]](https://bugs.gentoo.org/show_bug.cgi?id=953869)[]]).

[FILE] **`~/.config/gdb/gdbinit`**

    # https://sourceware.org/gdb/current/onlinedocs/gdb.html/Index-Files.html
    set index-cache enabled on

## [Usage]

### [Enabling core dumps]

Core dumps can also be used for debugging. These core files (named for when RAM was called \"core\" memory) contain the same information that the program would produce when run with [gdb]. Here, [bad_code] is the program that will be debugged with [gdb]. In order to debug with a core file with bad_code, run [gdb ./bad_code core] where [core] is the name of the core file.

Sometimes a program crashes without an easy way to run it manually under gdb. A solution to this can be obtaining a coredump.

If the program\'s output is as follows, there was no coredump created:

`user `[`$`]`./foo`

    Segmentation fault

Note that it doesn\'t say \"(core dumped)\". If coredumps are already enabled, the following output will appear:

`user `[`$`]`./foo`

    Segmentation fault (core dumped)

To enable core dumps, run the following in a shell:

`root `[`#`]`sysctl kernel.yama.ptrace_scope=0 fs.suid_dumpable=2 # Allows running as a normal user`

`root `[`#`]`ulimit -c unlimited # Allow any size for coredumps (re-run this as the user running the broken program if needed)`

Then running the program again, a corefile should be created:

`user `[`$`]`./foo`

    Segmentation fault (core dumped)

`user `[`$`]`gdb foo foo.core`

    Reading symbols from foo...
    Core was generated by `./foo'.
    #0  0x00007f4fc7b37ae0 in gets () from /usr/lib64/libc.so.6
    (gdb) bt
    #0  0x00007f4fc7b37ae0 in gets () from /usr/lib64/libc.so.6
    #1  0x000055d73f62e08f in main () at /tmp/foo.c:10
    (gdb)

Note that [Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") users can utilize [coredumpctl] as well, while OpenRC users may wish to try [[[sys-process/minicoredumper]](https://packages.gentoo.org/packages/sys-process/minicoredumper)[]].

### [Running the program with GDB]

** Tip**\
Consider building the program with additional warnings. `-Wall -Wextra` enables most useful compiler warnings. See [GCC Warning Options](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#Options-to-Request-or-Suppress-Warnings) for details.

Suppose there is a program which needs to be debugged called [bad_code]. Some person claims that the program crashes and provides an example. Go ahead and test it out:

`user `[`$`]`` ./bad_code `perl -e 'print "A"x100'` ``

    Segmentation fault

It seems this person was right. Since the program is obviously broken, there is now a bug at hand. Now, it is time to use [gdb] to help solve this matter. First, run [gdb] with the `--args` option, then give it the full program with arguments:

`user `[`$`]`` gdb --args ./bad_code `perl -e 'print "A"x100'` ``

    GNU gdb 6.3
    Copyright 2004 Free Software Foundation, Inc.
    GDB is free software, covered by the GNU General Public License, and you are
    welcome to change it and/or distribute copies of it under certain conditions.
    Type "show copying" to see the conditions.
    There is absolutely no warranty for GDB. Type "show warranty" for details.
    This GDB was configured as "i686-pc-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".

A prompt that says \"(gdb)\" should display and wait for input. First, run the program with [run]:

`(gdb)``run`

    Starting program: /home/chris/bad_code

    Program received signal SIGSEGV, Segmentation fault.
    0xb7ec6dc0 in strcpy () from /lib/libc.so.6

The program should start, and show a notification of SIGSEGV, or Segmentation Fault. This is GDB telling us that the program has crashed. It also gives the last run function it could trace when the program crashes. However, this is not too useful, as there could be multiple strcpy\'s in the program, making it hard for developers to find which one is causing the issue. In order to help them out, a backtrace can be performed.

A backtrace runs backwards through all the functions that occurred upon program execution, to the function at fault. Functions that return (without causing a crash) will not show up on the backtrace. To get a backtrace at the (gdb) prompt type in [bt]. Something similar to the following message should be returned:

`(gdb)``bt`

    #0  0xb7ec6dc0 in strcpy () from /lib/libc.so.6
    #1  0x0804838c in run_it ()
    #2  0x080483ba in main ()

The trace pattern should be clearly visible. `main()` is called first, followed by `run_it()`, and somewhere in `run_it()` lies the `strcpy()` at fault. Things such as this help developers narrow down problems. There are a few exceptions to the output. First off is forgetting to enable debug symbols with `FEATURES="nostrip"`. With debug symbols stripped, the output looks something like this:

`(gdb)``bt`

    #0  0xb7e2cdc0 in strcpy () from /lib/libc.so.6
    #1  0x0804838c in ?? ()
    #2  0xbfd19510 in ?? ()
    #3  0x00000000 in ?? ()
    #4  0x00000000 in ?? ()
    #5  0xb7eef148 in libgcc_s_personality () from /lib/libc.so.6
    #6  0x080482ed in ?? ()
    #7  0x080495b0 in ?? ()
    #8  0xbfd19528 in ?? ()
    #9  0xb7dd73b8 in __guard_setup () from /lib/libc.so.6
    #10 0xb7dd742d in __guard_setup () from /lib/libc.so.6
    #11 0x00000006 in ?? ()
    #12 0xbfd19548 in ?? ()
    #13 0x080483ba in ?? ()
    #14 0x00000000 in ?? ()
    #15 0x00000000 in ?? ()
    #16 0xb7deebcc in __new_exitfn () from /lib/libc.so.6
    #17 0x00000000 in ?? ()
    #18 0xbfd19560 in ?? ()
    #19 0xb7ef017c in nullserv () from /lib/libc.so.6
    #20 0xb7dd6f37 in __libc_start_main () from /lib/libc.so.6
    #21 0x00000001 in ?? ()
    #22 0xbfd195d4 in ?? ()
    #23 0xbfd195dc in ?? ()
    #24 0x08048201 in ?? ()

This backtrace contains a large number of `??` (question) marks. This is because without debug symbols, [gdb] does not know how the program was run. Hence, it is crucial that debug symbols are *not* stripped.

Here is what the output looks like with `-ggdb3` flag enabled:

`(gdb)``bt`

    #0  0xb7e4bdc0 in strcpy () from /lib/libc.so.6
    #1  0x0804838c in run_it (input=0x0) at bad_code.c:7
    #2  0x080483ba in main (argc=1, argv=0xbfd3a434) at bad_code.c:12

Here, a lot more information is available for developers. Not only is function information displayed, but even the exact line numbers of the source files. This method is the most preferred, as long as the extra space can be spared.

The backtrace can be saved to a file by copying and pasting from the terminal. Once [gdb] tasks are over, quit.

`(gdb)``quit`

    The program is running. Exit anyway? (y or n) y

This ends the walk-through of [gdb]. However, there are other types of errors such as **improper file access** that can cause a program to fail during runtime. Find those using [strace].

### [Enabling ASLR]

gdb disables ASLR by default to make addresses more predictable, but this can affect how reproducible a bug is. It can mean a bug doesn\'t occur within gdb in some rare circumstances.

If this happens, try [set disable-randomization off] within gdb before running the program with [r].

## [See also]

-   [Debugging](https://wiki.gentoo.org/wiki/Debugging "Debugging") --- general advice on how to enable **debugging** symbols and information
-   [Stack smashing debugging guide](https://wiki.gentoo.org/wiki/Stack_smashing_debugging_guide "Stack smashing debugging guide") --- a step-by-step guide to debug stack smashing violations
-   [rr](https://wiki.gentoo.org/wiki/Rr "Rr") --- a C/C++ debugging tool for Linux that extends [GDB] with \'time-travel debugging\'.