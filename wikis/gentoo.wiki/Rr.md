[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Rr&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://rr-project.org/)

[[]][GitHub](https://github.com/rr-debugger/rr)

**rr**, **R**ecord and **R**eplay Framework, is a C/C++ debugging tool for Linux that extends [GDB](https://wiki.gentoo.org/wiki/GDB "GDB") with \'time-travel debugging\'. It provides an efficient reverse execution under GDB, allowing for the replaying of recorded instructions.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Debugging a segmentation fault]](#Debugging_a_segmentation_fault)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [AMD Zen CPUs]](#AMD_Zen_CPUs)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-debug/rr](https://packages.gentoo.org/packages/dev-debug/rr) [[]] [Record and Replay Framework]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`multilib`](https://packages.gentoo.org/useflags/multilib)   On 64bit systems, if you want to be able to compile 32bit and 64bit binaries
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-20 19:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-debug/rr`

## [Usage]

The important thing to understand is that *rr* allows hitting a crash, then going backwards to inspect state *before the crash happens*. Suppose a function *foo* gets called many (at least 20) times and it crashes the last time: setting a breapkoint on *foo* will hit many useless instances. To debug it, one needs the last one.

Using [rr record \...] to record the crash, then [rr replay] to open an rr-infused gdb session, then *b foo* to set a breakpoint on *foo*, finally by using *reverse-continue*, the session will land on the penultimate *foo* call which crashed.

### [Debugging a segmentation fault]

Take the following C file for example:

[CODE]

    #include <stdio.h>

    volatile int cookie = 1;

    int main()

Compile the file with the `-g` flag:

`user `[`$`]`gcc -ggdb3 main.c`

Upon running this file after compilation, the following is output:

`user `[`$`]`./a.out`

    Hello world!
    Upgrading cookie to a new number...
    Time to crash!
    Aborted                    (core dumped) ./a.out

To investigate the problem with rr, use `rr record`:

`user `[`$`]`rr record ./a.out`

    rr: Saving execution to trace directory `/home/larry/.local/share/rr/a.out-1'.
    On Zen CPUs, rr will not work reliably unless you disable the hardware SpecLockMap optimization.
    For instructions on how to do this, see https://github.com/rr-debugger/rr/wiki/Zen
    Hello world!
    Upgrading cookie to a new number...
    Time to crash!
    Aborted                    rr record ./a.out

Now replay the file using `rr replay`:

`user `[`$`]`rr replay`

    On Zen CPUs, rr will not work reliably unless you disable the hardware SpecLockMap optimization.
    For instructions on how to do this, see https://github.com/rr-debugger/rr/wiki/Zen
    Reading symbols from /home/larry/.local/share/rr/a.out-1/mmap_copy_4_a.out...
    Remote debugging using 127.0.0.1:35159
    Reading symbols from /lib64/ld-linux-x86-64.so.2...
    warning: BFD: warning: system-supplied DSO at 0x6fffd000 has a section extending past end of file
    warning: Discarding section .replay.text which has an invalid size (27) [in module system-supplied DSO at 0x6fffd000]
    0x00007f5269447d40 in _start () from /lib64/ld-linux-x86-64.so.2
    (rr)

Let it crash:

`(rr)``continue`

    Continuing.
    Hello world!
    Upgrading cookie to a new number...
    Time to crash!

    Program received signal SIGABRT, Aborted.
    __pthread_kill_implementation (threadid=<optimized out>, signo=6, no_tid=0) at pthread_kill.c:44
    44            return INTERNAL_SYSCALL_ERROR_P (ret) ? INTERNAL_SYSCALL_ERRNO (ret) : 0;

Look at the backtrace:

`(rr)``bt`

    #0  __pthread_kill_implementation (threadid=<optimized out>, signo=6, no_tid=0) at pthread_kill.c:44
    #1  __pthread_kill_internal (threadid=<optimized out>, signo=6) at pthread_kill.c:89
    #2  __GI___pthread_kill (threadid=<optimized out>, signo=signo@entry=6) at pthread_kill.c:100
    #3  0x00007f5269021042 in __GI_raise (sig=sig@entry=6) at ../sysdeps/posix/raise.c:26
    #4  0x00007f52690013a1 in __GI_abort () at abort.c:73
    #5  0x000055cea0a1e509 in main () at main.c:14

Look at the code around the failure, by first entering the right frame:

`(rr)``frame 5`

    #5  0x000055cea0a1e509 in main () at main.c:14
    14              __builtin_abort();

Then list surrounding code:

`(rr)``list`

    9               printf("Upgrading cookie to a new number...\n");
    10              cookie = 3;
    11
    12              printf("Time to crash!\n");
    13              cookie = 0;
    14              __builtin_abort();
    15      }

Set a watchpoint on `cookie`:

`(rr)``watch cookie`

    Hardware watchpoint 1: cookie

Reverse continue (rewind) until the breakpoint is hit:

`(rr)``reverse-continue`

    Continuing.

    Program received signal SIGABRT, Aborted.
    __pthread_kill_implementation (threadid=<optimized out>, signo=6, no_tid=0) at pthread_kill.c:44
    44            return INTERNAL_SYSCALL_ERROR_P (ret) ? INTERNAL_SYSCALL_ERRNO (ret) : 0;

Do it again:

`(rr)``reverse-continue`

    Continuing.

    Hardware watchpoint 1: cookie

    Old value = 0
    New value = 3
    main () at main.c:13
    13              cookie = 0;

The value of *cookie* can now be seen just before the \"Time to crash\" message was \'3\'.

## [Troubleshooting]

### [AMD Zen CPUs]

Owners of AMD Zen CPUs may need to activate a [workaround](https://github.com/rr-debugger/rr/wiki/Zen).

systemd users can run:

`root `[`#`]`systemctl start rr-zen_workaround.service`

There isn\'t an OpenRC service available at present, but [/usr/bin/rr-zen_workaround.py] can be invoked directly.

## [See also]

-   [GDB](https://wiki.gentoo.org/wiki/GDB "GDB") --- used to investigate runtime errors that normally involve memory corruption