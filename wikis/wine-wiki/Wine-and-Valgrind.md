[Valgrind](https://www.valgrind.org/) is a set of tools aimed at finding
bugs and performance problems in programs. By default, it catches reads
of uninitialized memory, accesses to inaccessible memory, and memory
leaks. It's useful for debugging wine itself, as well as windows apps
running on Wine.

- To get the full power of Valgrind while debugging Wine, you need to
  build Wine from source **after** installing Valgrind. You'll also want
  to switch off certain compiler optimizations; the [Developer
  Tools](Building-Wine#developer-tools) section of the
  [Building Wine](Building-Wine) page has more details.

- Valgrind will work on [macOS](MacOS) (starting with partial
  support in macOS v10.8 "Mountain Lion"). If you want line numbers with
  Valgrind on Mac, don't forget to tell Xcode to generate a .dSYM file,
  though you can also use gdb after the fact to look up line numbers.

- In applications built with the debug version of the MS Visual C/C++
  runtime, memory allocated via malloc() is always initialized. This
  obscures any uninitialized memory accesses that would normally
  appear from Valgrind (see *[Memory Management and the Debug
  Heap](https://web.archive.org/web/20100929150511/http://msdn.microsoft.com/en-us/library/bebs9zyz(VS.80).aspx)*
  at MSDN for the full story).

## Running Wine under Valgrind

To analyze a program running on Wine with Valgrind, just call valgrind
with the appropriate options in front of the normal wine command. For
example:

```sh
$ valgrind --trace-children=yes --vex-iropt-register-updates=allregs-at-mem-access wine foo.exe
```

Note that this command will also trace the \["wineserver"\] if *foo.exe*
is the first Wine application running. Unless you're specifically
looking to debug wineserver (usually you'll be more interested in
specific dlls), this is a waste of resources. Valgrind can be pretty
intensive on the CPU so you can speed things up quite a bit by not
starting the wineserver under Valgrind.

To do that, just start a dummy program under Wine **first** (e.g.
notepad or winemine), then without closing that program, start your
desired program through wine and valgrind as you normally would.

### Valgrind Options Relevant for Wine

Over the years, several Valgrind options have turned out to be
necessary, or at least very helpful, when analyzing Wine. Two in
particular are necessary for Wine to function well under Valgrind:

- *[--trace-children=yes](https://valgrind.org/docs/manual/manual-core.html#opt.trace-children)*
  is necessary because wine starts new processes for individual programs
- *[--vex-iropt-register-updates=allregs-at-mem-access](https://valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver-limitations)*
  ensures that bitmap-related code, such as
  `GetBitmapBits()` works under Valgrind

Several more are useful for suppressing known bugs or exceptions in
Wine:

- *[--suppressions=path/to/suppression-file](https://valgrind.org/docs/manual/manual-core.html#manual-core.suppress)*
  lets you pass a file with custom suppression rules to Valgrind.
  [Austin English](@austin987) maintains a collection of
  suppression files for Wine at his [github
  repo](https://github.com/austin987/wine_misc/tree/master/valgrind)

This option can be repeated with multiple files

- *[--partial-loads-ok=yes](https://valgrind.org/docs/manual/mc-manual.html#opt.partial-loads-ok)*
  silences warnings for when bit-alignments overlap both addressable and
  illegal ranges. In particular, try this if the last three bytes of
  allocations throw a lot of "Invalid Read of Size N" warnings.
- *WINELOADERNOEXEC=1*
  works around a crash in `wld_mmap` if Valgrind puts things too early in the address space

There's a good chance these are false positives from vectorized string
operations ([Valgrind Bug Report
\#264936](https://bugs.kde.org/show_bug.cgi?id=264936) has more info).
In the Valgrind bug report, someone also mentions using GCC with the
*-fno-builtin-strdup* compiler option to make the warnings
disappear. It hasn't been tested with Wine, but the [Compiler
Optimizations](Building-Wine#compiler-optimizations--call-stacks)
section of [Building Wine](Building-Wine) has more details about
changing compiler flags while building Wine.

### Controlling Memory Leak Reports

There are a few more Valgrind options that let you fine-tune how much it
reports about memory leaks. By default, Valgrind only gives a count of
memory leaks detected at the end of execution.

To get more info, you want to pass the
*[--leak-check=full](https://valgrind.org/docs/manual/mc-manual.html#opt.leak-check)*
flag when running Valgrind. This will give you individual reports about
certain types of memory leaks (but not all). Once this option is set,
you can use several other options to specify which kinds of memory leaks
you want detailed reports for:

- *[--show-leak-kinds=definite,possible](https://valgrind.org/docs/manual/mc-manual.html#opt.show-leak-kinds)*
  only reports unfreed blocks with no pointers or that depend on
  interior pointers (the default)
- *[--show-possibly-lost=no](https://valgrind.org/docs/manual/mc-manual.html#opt.show-reachable)*
  or
  *[--show-leak-kinds=definite](https://valgrind.org/docs/manual/mc-manual.html#opt.show-leak-kinds)*
  only reports unfreed blocks with no pointers
- *[--show-reachable=yes](https://valgrind.org/docs/manual/mc-manual.html#opt.show-reachable)*
  or
  *[--show-leak-kinds=all](https://valgrind.org/docs/manual/mc-manual.html#opt.show-leak-kinds)*
  reports all forms of unfreed blocks, even trivial ones with clear
  pointers

Finally, by passing the
*[--track-origins=yes](https://valgrind.org/docs/manual/mc-manual.html#opt.track-origins)*
option, you can ask Valgrind to give you stack backtraces to the point
where a leaky memory block was allocated. This is terrifically helpful
for debugging, but it has the downside of making valgrind run even
slower.

## Conformance Tests under Valgrind

To run Wine's ConformanceTests under Valgrind, you mainly need to set
the *WINETEST_WRAPPER* and *VALGRIND_OPTS* variables, e.g...

```sh
$ export VALGRIND_OPTS="--trace-children=yes --track-origins=yes --gen-suppressions=all --suppressions=$HOME/valgrind-suppressions-ignore --suppressions=$HOME/valgrind-suppressions-external --num-callers=20 --vex-iropt-register-updates=allregs-at-mem-access"
$ WINETEST_WRAPPER=valgrind make -k test > test.log 2>&1
```

Along with suppression files, [Austin English's](@austin987) [github
repo](https://github.com/austin987/wine_misc/tree/master/valgrind)
also has some scripts to help run the tests under Valgrind.

## Changes to Wine Source

There are also some tweaks you can make to the Wine source code itself
that might help you uncover other problems. First, the Wine source
defines two constants that can be quickly changed and might reveal more
bugs:

- `MAX_FREE_PENDING` controls how long freed blocks are kept out of
  circulation and is set to 1024 by default. If you think your app is
  hanging on to freed pointers longer than it should, increasing it and
  recompiling wine might help Valgrind detect use-after-free errors.
- `HEAP_TAIL_EXTRA_SIZE` gives the size of the redzone at the end of
  each block. If your app nests really big structs within another struct
  or array, you might need to increase this to catch overrun errors.
  Watch out though because increasing it beyond 32 or so bytes can cause
  strange false positives sometimes.

## Valgrind Bugs / Feature Requests

There are several open bugs/feature requests in Valgrind that affect /
would benefit Wine (roughly descending priority):

- [valgrind doesn't show symbols for programs compiled with mingw's
  gcc](https://bugs.kde.org/show_bug.cgi?id=211031)
- [vex x86-\>IR: unhandled instruction bytes: 0x66 0x60 0xB8
  0x1](https://bugs.kde.org/show_bug.cgi?id=126245)
- [vex amd64-\>IR: unhandled instruction bytes: 0x65 0x4C 0x8B 0x1C (mov
  %gs:0x10,%r11)](https://bugs.kde.org/show_bug.cgi?id=148363)
- [want more contiguous user space for 32-bit process on 64-bit
  hardware](https://bugs.kde.org/show_bug.cgi?id=204536)
- [wine's crypt32 message tests crash under valgrind, because of a jump
  to NULL](https://bugs.kde.org/show_bug.cgi?id=264785)
- [wine's kernel32/thread test fails under
  valgrind](https://bugs.kde.org/show_bug.cgi?id=335563)
- [Memcheck has high false error rates on MSVC2013 compiled, optimised,
  code](https://bugs.kde.org/show_bug.cgi?id=344382) Note: Wine can't
  deal with MSVC2013 pdb's anyway, see:
  - [Wine builtin dbghelp fails to process stream name table of PDBs
    created with recent Visual Studio 2010-2013
    (mfc120.pdb)](#37746)
  - [dbghelp_msc:pe_load_debug_directory Got a page fault while loading
    symbols (Visual C++ 2013
    .pdb's)](#38594)
  - [winedbg: internal crash/hangs when running ieframe/tests/ie.c with
    pdb debug symbols](#38604)
- [(meta) Valgrind 3.10 cannot load wine on OS
  X](https://bugs.kde.org/show_bug.cgi?id=339017)
- [wine/osx: mmap-FIXED(0x1000, 1073741824) failed in UME
  (load_segment2)](https://bugs.kde.org/show_bug.cgi?id=349804)

## Alternatives to Valgrind

At least on Unix and among free, open-source tools, Valgrind is arguably
the gold standard for dynamic analysis suites. It offers many features
that most other execution-analysis tools don't (not least of which that
it's free, it's fast and it can handle Mac and Linux apps too). In fact,
if you're a Windows developer, you might want to consider testing your
program on Wine just to get Valgrind.

If for whatever reason you don't want to use Valgrind though, or you
want to run a tool natively on Windows, there are several free and
commercial ones.

### Open-Source Tools

- [Dr. Memory](https://www.drmemory.org/) (memory checker based on the
  [DynamoRIO framework](https://dynamorio.org/))
  - Supported on all platforms
- [gperftools](https://github.com/gperftools/gperftools) (Google
  Performance Tools for Unix)
  - Includes an efficient malloc implementation, plus heap & call-graph
    profilers
- [FastMM](https://sourceforge.net/projects/fastmm/) (fast
  memory-manager for C++ & Delphi programs)
  - Also includes memory checking tools
  - Only for Windows
- [DUMA](https://duma.sourceforge.net/) (memory checker based on Bruce
  Perens' older Electric Fence library)
  - Supported on Unix and Windows
  - Should still work but hasn't been updated since 2009
- [Visual Leak Detector](https://kinddragon.github.io/vld/) (memory leak
  detector for Microsoft Visual C++)
  - Only on Windows

### Freeware Tools

- [AMD CodeXL](https://gpuopen.com/archived/legacy-codexl/) (profiling
  for both the CPU and GPU)
  - Only for AMD processors...
  - Consequently not available for Mac
- [MS Application
  Verifier](https://msdn.microsoft.com/en-us/library/windows/hardware/ff538115%28v=vs.85%29.aspx)
  (Windows runtime test-suite)
  - Runs several tests, including memory checking, on Windows
    applications
  - Part of the Windows SDK and only available on Windows
- [Debugging Tools for
  Windows](https://msdn.microsoft.com/en-us/library/windows/hardware/ff551063%28v=vs.85%29.aspx)
  (set of debuggers from Microsoft)
  - Only for Windows naturally

### Commercial Tools

- [Unicom
  PurifyPlus](https://www.teamblue.unicomsi.com/products/purifyplus/)
  (originally IBM Rational Purify)
  - There are Linux & Mac versions too
- [Parasoft
  Insure++](https://www.parasoft.com/products/parasoft-insure/)
  (memory-error checking suite)
  - Also has Linux & Mac versions
- [Deleaker](https://www.deleaker.com/) (memory profiler and leak
  detector for Microsoft Visual C++)
  - Only for Windows
- [Software Verify C++ Suite](https://www.softwareverify.com/products/)
  (several different testing tools)
  - Only for Windows
- [Intel Inspector
  XE](https://www.intel.com/content/www/us/en/developer/tools/oneapi/inspector.html#gs.tmgpje)
  (memory checking and thread debugging)
  - Only for Intel processors
  - But otherwise supported on Windows, macOS, and Linux
- [Glowcode](https://www.glowcode.com/) (memory checking, profiling, and
  tracing)
  - Only for Windows

### Ad-Hoc Patches

Most separate profiling tools will significantly affect Wine's
performance. If this is a problem, you may be able to take a different
approach: patch the wine DLL so it can detect errors itself.

This should give you much lower overhead but at the price of much more
work for you, the developer. Also note that this will **only** work on
DLLs that never share allocated memory outside the scope of the DLL.

- Old example for
  [msi](https://www.winehq.org/pipermail/wine-patches/2006-October/031567.html)
- Old example for
  [richedit](https://www.winehq.org/pipermail/wine-patches/2006-October/032143.html)

## See Also

- [Debugging Mozilla with
  Valgrind](https://developer.mozilla.org/en-US/docs/Debugging_Mozilla_with_Valgrind)
  has a good case-study showing how to use Valgrind
- [Wine bugs](https://bugs.winehq.org/buglist.cgi?quicksearch=valgrind)
  involving or detected by Valgrind
- [Valgrind
  bugs](https://bugs.kde.org/buglist.cgi?product=valgrind&long_desc_type=substring&long_desc=wine&bug_status=UNCONFIRMED&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDSINFO)
  with Wine mentioned in the comments
- [Performance](Performance)
- [Static Analysis](Static-Analysis)
- [Code Coverage](Code-Coverage)
