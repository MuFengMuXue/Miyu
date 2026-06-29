**Resources**

[[]][Home](https://valgrind.org/)

[[]][Official documentation](https://valgrind.org/docs/manual/index.html)

[[]][Package information](https://packages.gentoo.org/packages/dev-debug/valgrind)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Valgrind "wikipedia:Valgrind")

[[]][GitWeb](https://sourceware.org/git/valgrind.git)

[[]][Bugs (upstream)](https://valgrind.org/support/bug_reports.html)

[[]][[#valgrind-dev](ircs://irc.libera.chat/#valgrind-dev)] ([[webchat](https://web.libera.chat/#valgrind-dev)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/valgrind)

**Valgrind** is a dynamic analysis tool which detects memory errors and memory leaks. It is spiritually the predecessor of modern debugging tools like [AddressSanitizer](https://wiki.gentoo.org/wiki/AddressSanitizer "AddressSanitizer") and LeakSanitizer, but remains relevant for debugging applications today because of its thoroughness and ease of setup (no need to recompile applications). They cover similar but not identical usecases ^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Examples]](#Examples)
    -   [[4.1] [Memory Leak]](#Memory_Leak)
    -   [[4.2] [Uninitialized Value]](#Uninitialized_Value)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Refuses to launch with strlen error]](#Refuses_to_launch_with_strlen_error)
    -   [[5.2] [Unhandled instruction bytes]](#Unhandled_instruction_bytes)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Installation]

For better support for Valgrind in system applications, consider enabling [[[valgrind]](https://packages.gentoo.org/useflags/valgrind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]. For example, this will make [[[dev-lang/python]](https://packages.gentoo.org/packages/dev-lang/python)[]] detect when Valgrind is in use and switch allocators from its internal pymalloc to valgrind\'s, giving far better output.

### [USE flags]

### [USE flags for] [dev-debug/valgrind](https://packages.gentoo.org/packages/dev-debug/valgrind) [[]] [An open-source memory debugger for GNU/Linux]

  ----------------------------------------------------------------- -----------------------------------------------------------------------
  [`mpi`](https://packages.gentoo.org/useflags/mpi)                 Add MPI (Message Passing Interface) layer to the apps that support it
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 17:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-debug/valgrind`

## [Configuration]

### [Environment variables]

-   `VALGRIND_OPTS`

### [Files]

-   [\~/.valgrindrc] - Local (per user) configuration file.
-   [./.valgrindrc] - Local (per project/directory) configuration file.

## [Usage]

Valgrind is actually a *suite* of tools, but for many people, \"Valgrind\" is synonymous with the default tool **memcheck**. The following tools are available, which can be selected with [valgrind \--tool=name]:

-   [cachegrind](https://valgrind.org/docs/manual/cg-manual.html) (cache and branch-prediction profiler)
-   [callgrind](https://valgrind.org/docs/manual/cl-manual.html) (call-graph generating cache and branch prediction profiler)
-   [dhat](https://valgrind.org/docs/manual/dh-manual.html) (dynamic heap analysis tool)
-   [drd](https://valgrind.org/docs/manual/drd-manual.html) (thread safety analysis)
-   [helgrind](https://valgrind.org/docs/manual/hg-manual.html) (thread error detector)
-   [lackey](https://valgrind.org/docs/manual/lk-manual.html) (example tool, can be used to analyze a specific function)
-   [massif](https://valgrind.org/docs/manual/ms-manual.html) (heap memory profiler)
-   [memcheck](https://valgrind.org/docs/manual/mc-manual.html) (memory error detector)

Using Valgrind with applications is easy, simply run [valgrind /path/to/application]. No recompilation is needed!

For example, to run Valgrind on [uptime]:

`user `[`$`]`valgrind uptime`

    ==3064010== Memcheck, a memory error detector
    ==3064010== Copyright (C) 2002-2022, and GNU GPL'd, by Julian Seward et al.
    ==3064010== Using Valgrind-3.20.0 and LibVEX; rerun with -h for copyright info
    ==3064010== Command: uptime
    ==3064010==
     03:35:26 up 4 days,  6:58,  1 user,  load average: 0.15, 2.26, 10.93
    ==3064010==
    ==3064010== HEAP SUMMARY:
    ==3064010==     in use at exit: 0 bytes in 0 blocks
    ==3064010==   total heap usage: 57 allocs, 57 frees, 31,824 bytes allocated
    ==3064010==
    ==3064010== All heap blocks were freed -- no leaks are possible
    ==3064010==
    ==3064010== For lists of detected and suppressed errors, rerun with: -s
    ==3064010== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)

The output states that [uptime] ran successfully with no detected memory leaks and no memory safety issues (no out-of-bounds access, etc).

### [Invocation]

`user `[`$`]`valgrind --help`

    usage: valgrind [options] prog-and-args

      tool-selection option, with default in [ ]:
        --tool=<name>             use the Valgrind tool named <name> [memcheck]

      basic user options for all Valgrind tools, with defaults in [ ]:
        -h --help                 show this message
        --help-debug              show this message, plus debugging options
        --help-dyn-options        show the dynamically changeable options
        --version                 show version
        -q --quiet                run silently; only print error msgs
        -v --verbose              be more verbose -- show misc extra info
        --trace-children=no|yes   Valgrind-ise child processes (follow execve)? [no]
        --trace-children-skip=patt1,patt2,...    specifies a list of executables
                                  that --trace-children=yes should not trace into
        --trace-children-skip-by-arg=patt1,patt2,...   same as --trace-children-skip=
                                  but check the argv[] entries for children, rather
                                  than the exe name, to make a follow/no-follow decision
        --child-silent-after-fork=no|yes omit child output between fork & exec? [no]
        --vgdb=no|yes|full        activate gdbserver? [yes]
                                  full is slower but provides precise watchpoint/step
        --vgdb-error=<number>     invoke gdbserver after <number> errors [999999999]
                                  to get started quickly, use --vgdb-error=0
                                  and follow the on-screen directions
        --vgdb-stop-at=event1,event2,... invoke gdbserver for given events [none]
             where event is one of:
               startup exit abexit valgrindabexit all none
        --track-fds=no|yes|all    track open file descriptors? [no]
                                  all includes reporting stdin, stdout and stderr
        --time-stamp=no|yes       add timestamps to log messages? [no]
        --log-fd=<number>         log messages to file descriptor [2=stderr]
        --log-file=<file>         log messages to <file>
        --log-socket=ipaddr:port  log messages to socket ipaddr:port
        --enable-debuginfod=no|yes query debuginfod servers for missing
                                  debuginfo [yes]

      user options for Valgrind tools that report errors:
        --xml=yes                 emit error output in XML (some tools only)
        --xml-fd=<number>         XML output to file descriptor
        --xml-file=<file>         XML output to <file>
        --xml-socket=ipaddr:port  XML output to socket ipaddr:port
        --xml-user-comment=STR    copy STR verbatim into XML output
        --demangle=no|yes         automatically demangle C++ names? [yes]
        --num-callers=<number>    show <number> callers in stack traces [12]
        --error-limit=no|yes      stop showing new errors if too many? [yes]
        --exit-on-first-error=no|yes exit code on the first error found? [no]
        --error-exitcode=<number> exit code to return if errors found [0=disable]
        --error-markers=<begin>,<end> add lines with begin/end markers before/after
                                  each error output in plain text mode [none]
        --show-error-list=no|yes  show detected errors list and
                                  suppression counts at exit [no]
        -s                        same as --show-error-list=yes
        --keep-debuginfo=no|yes   Keep symbols etc for unloaded code [no]
                                  This allows saved stack traces (e.g. memory leaks)
                                  to include file/line info for code that has been
                                  dlclose'd (or similar)
        --show-below-main=no|yes  continue stack traces below main() [no]
        --default-suppressions=yes|no
                                  load default suppressions [yes]
        --suppressions=<filename> suppress errors described in <filename>
        --gen-suppressions=no|yes|all    print suppressions for errors? [no]
        --input-fd=<number>       file descriptor for input [0=stdin]
        --dsymutil=no|yes         run dsymutil on Mac OS X when helpful? [yes]
        --max-stackframe=<number> assume stack switch for SP changes larger
                                  than <number> bytes [2000000]
        --main-stacksize=<number> set size of main thread's stack (in bytes)
                                  [min(max(current 'ulimit' value,1MB),16MB)]

      user options for Valgrind tools that replace malloc:
        --alignment=<number>      set minimum alignment of heap allocations [16]
        --redzone-size=<number>   set minimum size of redzones added before/after
                                  heap blocks (in bytes). [16]
        --xtree-memory=none|allocs|full   profile heap memory in an xtree [none]
                                  and produces a report at the end of the execution
                                  none: no profiling, allocs: current allocated
                                  size/blocks, full: profile current and cumulative
                                  allocated size/blocks and freed size/blocks.
        --xtree-memory-file=<file>   xtree memory report file [xtmemory.kcg.%p]

      uncommon user options for all Valgrind tools:
        --fullpath-after=         (with nothing after the '=')
                                  show full source paths in call stacks
        --fullpath-after=string   like --fullpath-after=, but only show the
                                  part of the path after 'string'.  Allows removal
                                  of path prefixes.  Use this flag multiple times
                                  to specify a set of prefixes to remove.
        --extra-debuginfo-path=path    absolute path to search for additional
                                  debug symbols, in addition to existing default
                                  well known search paths.
        --debuginfo-server=ipaddr:port    also query this server
                                  (valgrind-di-server) for debug symbols
        --allow-mismatched-debuginfo=no|yes  [no]
                                  for the above two flags only, accept debuginfo
                                  objects that don't "match" the main object
        --smc-check=none|stack|all|all-non-file [all-non-file]
                                  checks for self-modifying code: none, only for
                                  code found in stacks, for all code, or for all
                                  code except that from file-backed mappings
        --read-inline-info=yes|no read debug info about inlined function calls
                                  and use it to do better stack traces.
                                  [yes] on Linux/Android/Solaris for the tools
                                  Memcheck/Massif/Helgrind/DRD only.
                                  [no] for all other tools and platforms.
        --read-var-info=yes|no    read debug info on stack and global variables
                                  and use it to print better error messages in
                                  tools that make use of it (Memcheck, Helgrind,
                                  DRD) [no]
        --vgdb-poll=<number>      gdbserver poll max every <number> basic blocks [5000]
        --vgdb-shadow-registers=no|yes   let gdb see the shadow registers [no]
        --vgdb-prefix=    prefix for vgdb FIFOs [/tmp/vgdb-pipe]
        --run-libc-freeres=no|yes free up glibc memory at exit on Linux? [yes]
        --run-cxx-freeres=no|yes  free up libstdc++ memory at exit on Linux
                                  and Solaris? [yes]
        --sim-hints=hint1,hint2,...  activate unusual sim behaviours [none]
             where hint is one of:
               lax-ioctls lax-doors fuse-compatible enable-outer
               no-inner-prefix no-nptl-pthread-stackcache fallback-llsc none
        --fair-sched=no|yes|try   schedule threads fairly on multicore systems [no]
        --kernel-variant=variant1,variant2,...
             handle non-standard kernel variants [none]
             where variant is one of:
               bproc android-no-hw-tls
               android-gpu-sgx5xx android-gpu-adreno3xx none
        --merge-recursive-frames=<number>  merge frames between identical
               program counters in max <number> frames) [0]
        --num-transtab-sectors=<number> size of translated code cache [32]
               more sectors may increase performance, but use more memory.
        --avg-transtab-entry-size=<number> avg size in bytes of a translated
               basic block [0, meaning use tool provided default]
        --aspace-minaddr=0xPP     avoid mapping memory below 0xPP [guessed]
        --valgrind-stacksize=<number> size of valgrind (host) thread's stack
                                   (in bytes) [1048576]
        --show-emwarns=no|yes     show warnings about emulation limits? [no]
        --require-text-symbol=:sonamepattern:symbolpattern    abort run if the
                                  stated shared object doesn't have the stated
                                  text symbol.  Patterns can contain ? and *.
        --soname-synonyms=syn1=pattern1,syn2=pattern2,... synonym soname
                  specify patterns for function wrapping or replacement.
                  To use a non-libc malloc library that is
                      in the main exe:  --soname-synonyms=somalloc=NONE
                      in libxyzzy.so:   --soname-synonyms=somalloc=libxyzzy.so
        --sigill-diagnostics=yes|no  warn about illegal instructions? [yes]
        --unw-stack-scan-thresh=<number>   Enable stack-scan unwind if fewer
                      than <number> good frames found  [0, meaning "disabled"]
                      NOTE: stack scanning is only available on arm-linux.
        --unw-stack-scan-frames=<number>   Max number of frames that can be
                      recovered by stack scanning [5]
        --resync-filter=no|yes|verbose [yes on MacOS, no on other OSes]
                  attempt to avoid expensive address-space-resync operations
        --max-threads=<number>    maximum number of threads that valgrind can
                                  handle [500]

      user options for Memcheck:
        --leak-check=no|summary|full     search for memory leaks at exit?  [summary]
        --leak-resolution=low|med|high   differentiation of leak stack traces [high]
        --show-leak-kinds=kind1,kind2,.. which leak kinds to show?
                                                [definite,possible]
        --errors-for-leak-kinds=kind1,kind2,..  which leak kinds are errors?
                                                [definite,possible]
            where kind is one of:
              definite indirect possible reachable all none
        --leak-check-heuristics=heur1,heur2,... which heuristics to use for
            improving leak search false positive [all]
            where heur is one of:
              stdstring length64 newarray multipleinheritance all none
        --show-reachable=yes             same as --show-leak-kinds=all
        --show-reachable=no --show-possibly-lost=yes
                                         same as --show-leak-kinds=definite,possible
        --show-reachable=no --show-possibly-lost=no
                                         same as --show-leak-kinds=definite
        --xtree-leak=no|yes              output leak result in xtree format? [no]
        --xtree-leak-file=<file>         xtree leak report file [xtleak.kcg.%p]
        --undef-value-errors=no|yes      check for undefined value errors [yes]
        --track-origins=no|yes           show origins of undefined values? [no]
        --partial-loads-ok=no|yes        too hard to explain here; see manual [yes]
        --expensive-definedness-checks=no|auto|yes
                                         Use extra-precise definedness tracking [auto]
        --freelist-vol=<number>          volume of freed blocks queue     [20000000]
        --freelist-big-blocks=<number>   releases first blocks with size>= [1000000]
        --workaround-gcc296-bugs=no|yes  self explanatory [no].  Deprecated.
                                         Use --ignore-range-below-sp instead.
        --ignore-ranges=0xPP-0xQQ[,0xRR-0xSS]   assume given addresses are OK
        --ignore-range-below-sp=<number>-<number>  do not report errors for
                                         accesses at the given offsets below SP
        --malloc-fill=<hexnumber>        fill malloc'd areas with given value
        --free-fill=<hexnumber>          fill free'd areas with given value
        --keep-stacktraces=alloc|free|alloc-and-free|alloc-then-free|none
            stack trace(s) to keep for malloc'd/free'd areas       [alloc-and-free]
        --show-mismatched-frees=no|yes   show frees that don't match the allocator? [yes]

      Extra options read from ~/.valgrindrc, $VALGRIND_OPTS, ./.valgrindrc

      Memcheck is Copyright (C) 2002-2022, and GNU GPL'd, by Julian Seward et al.
      Valgrind is Copyright (C) 2000-2017, and GNU GPL'd, by Julian Seward et al.
      LibVEX is Copyright (C) 2004-2017, and GNU GPL'd, by OpenWorks LLP et al.

      Bug reports, feedback, admiration, abuse, etc, to: www.valgrind.org.

## [Examples]

### [Memory Leak]

[CODE] **memleak.c**

    #include <stdlib.h>

    int main()

`user `[`$`]`gcc -g memleak.c -o memleak`

`user `[`$`]`valgrind --leak-check=full ./memleak`

    ==3577== Memcheck, a memory error detector
    ==3577== Copyright (C) 2002-2024, and GNU GPL'd, by Julian Seward et al.
    ==3577== Using Valgrind-3.24.1.GIT and LibVEX; rerun with -h for copyright info
    ==3577== Command: ./memleak
    ==3577==
    10
    ==3577==
    ==3577== HEAP SUMMARY:
    ==3577==     in use at exit: 40 bytes in 1 blocks
    ==3577==   total heap usage: 2 allocs, 1 frees, 1,064 bytes allocated
    ==3577==
    ==3577== 40 bytes in 1 blocks are definitely lost in loss record 1 of 1
    ==3577==    at 0x4849968: malloc (vg_replace_malloc.c:446)
    ==3577==    by 0x1091AE: main (memleak.c:4)
    ==3577==
    ==3577== LEAK SUMMARY:
    ==3577==    definitely lost: 40 bytes in 1 blocks
    ==3577==    indirectly lost: 0 bytes in 0 blocks
    ==3577==      possibly lost: 0 bytes in 0 blocks
    ==3577==    still reachable: 0 bytes in 0 blocks
    ==3577==         suppressed: 0 bytes in 0 blocks
    ==3577==
    ==3577== For lists of detected and suppressed errors, rerun with: -s
    ==3577== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)

### [Uninitialized Value]

[CODE] **memleak.c**

    int main()

`user `[`$`]`gcc -g uninitialized.c -o uninitialized`

`user `[`$`]`valgrind --track-origins=yes ./uninitialized`

    ==3903== Memcheck, a memory error detector
    ==3903== Copyright (C) 2002-2024, and GNU GPL'd, by Julian Seward et al.
    ==3903== Using Valgrind-3.24.1.GIT and LibVEX; rerun with -h for copyright info
    ==3903== Command: ./uninitialized
    ==3903==
    ==3903== Use of uninitialised value of size 8
    ==3903==    at 0x109189: main (uninitialized.c:3)
    ==3903==  Uninitialised value was created by a stack allocation
    ==3903==    at 0x109179: main (uninitialized.c:1)
    ==3903==
    1179403647
    ==3903==
    ==3903== HEAP SUMMARY:
    ==3903==     in use at exit: 0 bytes in 0 blocks
    ==3903==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
    ==3903==
    ==3903== All heap blocks were freed -- no leaks are possible
    ==3903==
    ==3903== For lists of detected and suppressed errors, rerun with: -s
    ==3903== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)

## [Troubleshooting]

Valgrind often needs debug information of the C library to perform function redirection. For this, [create the package debug environment described above](https://wiki.gentoo.org/wiki/Debugging#Per-package "Debugging") and apply it for [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] (or [[[sys-libs/musl]](https://packages.gentoo.org/packages/sys-libs/musl)[]] as needed).

First, [debugedit] should be installed:

`root `[`#`]`emerge --ask dev-util/debugedit`

Configure Portage to build selected packages with (enhanced) debugging symbols (`-ggdb3`) and not to strip them:

[FILE] **[`/etc/portage/env/debugsyms`](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")**

    CFLAGS="$ -ggdb3"
    CXXFLAGS="$ -ggdb3"
    FEATURES="$ splitdebug compressdebug -nostrip"

[FILE] **[`/etc/portage/env/installsources`](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")**

    FEATURES="$ installsources"

Enable these settings for the required software:

[FILE] **[`/etc/portage/package.env`](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")**

    sys-libs/glibc debugsyms installsources

Remember to re-emerge the libc after setting the needed [package.env] variables:

`root `[`#`]`emerge --ask --oneshot sys-libs/glibc`

To get meaningful backtraces, users may need to build more packages (such as dependencies of the software being debugged) with the above environment. For local projects, programs should be built with `-Og -ggdb3`.

### [Refuses to launch with strlen error]

It is possible that Valgrind refuses to launch with an error like so:

    valgrind:  A must-be-redirected function
    valgrind:  whose name matches the pattern:      strlen
    valgrind:  in an object with soname matching:   ld-linux-x86-64.so.2

In this case, add `-fno-builtin-strlen` to `CFLAGS` for [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]]:

[FILE] **[`/etc/portage/env/glibc-no-strlen`](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")**

    # Needed for Valgrind
    CFLAGS="$ -fno-builtin-strlen"

[FILE] **[`/etc/portage/package.env`](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage")**

    sys-libs/glibc glibc-no-strlen

### [Unhandled instruction bytes]

This could be a few different errors and Valgrind\'s own [FAQ covers it](https://valgrind.org/docs/manual/faq.html#faq.msgdeath). The most common reason for seeing this however is that Valgrind does not [currently support AVX512](https://bugs.kde.org/show_bug.cgi?id=383010). Users should try building glibc with -march=x86-64-v3 or similar.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-debug/valgrind`

## [See also]

-   [GDB](https://wiki.gentoo.org/wiki/GDB "GDB") --- used to investigate runtime errors that normally involve memory corruption
-   [AddressSanitizer](https://wiki.gentoo.org/wiki/AddressSanitizer "AddressSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect several memory access errors.
-   [UndefinedBehaviorSanitizer](https://wiki.gentoo.org/wiki/UndefinedBehaviorSanitizer "UndefinedBehaviorSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect various forms of undefined behaviour (UB).

## [External resources]

-   [Debug memory errors with Valgrind and GDB](https://developers.redhat.com/articles/2021/11/01/debug-memory-errors-valgrind-and-gdb)
-   [Valgrind Memcheck: Different ways to lose your memory](https://developers.redhat.com/blog/2021/04/23/valgrind-memcheck-different-ways-to-lose-your-memory)
-   [Twenty years of Valgrind](https://nnethercote.github.io/2022/07/27/twenty-years-of-valgrind.html)
-   [GDB valgrind integration](https://sasshkas.blogspot.com/2021/07/gdb-valgrind-integration.html)
-   [Valgrind and GDB in close cooperation](https://www.redhat.com/en/blog/valgrind-and-gdb-close-cooperation)

## [References]

1.  [[[↑](#cite_ref-1)] [ Jan Kratochvil. [Memory error checking in C and C++: Comparing Sanitizers and Valgrind](https://developers.redhat.com/blog/2021/05/05/memory-error-checking-in-c-and-c-comparing-sanitizers-and-valgrind), [Red Hat Developer Blog](https://developers.redhat.com/blog), May 5th, 2021. Retrieved on January 26th, 2023.]]