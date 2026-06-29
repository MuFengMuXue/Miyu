**Resources**

[[]][Bugs (upstream)](https://bugs.gentoo.org/buglist.cgi?quicksearch=%5BICE%2F7%5D)

A guide to debugging **GCC Internal Compiler Errors** (ICEs).

This page helps with diagnosing [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") crashes with `internal compiler error: Segmentation fault` when building a Gentoo package (or any software).

Extracting useful information from a crash to report a bug requires a few steps. This article lists the steps and provides a few real-world debugging sessions.

## Contents

-   [[1] [Quick guide]](#Quick_guide)
    -   [[1.1] [Tl;DR]](#Tl.3BDR)
-   [[2] [Detailed guide]](#Detailed_guide)
    -   [[2.1] [Steps to track an ICE (internal compiler errors) down]](#Steps_to_track_an_ICE_.28internal_compiler_errors.29_down)
        -   [[2.1.1] [Rebuilding GCC and glibc with debugging symbols (optional)]](#Rebuilding_GCC_and_glibc_with_debugging_symbols_.28optional.29)
        -   [[2.1.2] [Check if an ICE is reproducible]](#Check_if_an_ICE_is_reproducible)
        -   [[2.1.3] [Extract exact command]](#Extract_exact_command)
        -   [[2.1.4] [Extract self-contained source (use -save-temps)]](#Extract_self-contained_source_.28use_-save-temps.29)
        -   [[2.1.5] [Expand -march=native, exact gcc version and other system-specific options]](#Expand_-march.3Dnative.2C_exact_gcc_version_and_other_system-specific_options)
        -   [[2.1.6] [Report bug on bugs.gentoo.org]](#Report_bug_on_bugs.gentoo.org)
        -   [[2.1.7] [\[bonus\] minimize needed flags to reproduce failure]](#.5Bbonus.5D_minimize_needed_flags_to_reproduce_failure)
        -   [[2.1.8] [\[bonus\] minimize self-contained source using cvise]](#.5Bbonus.5D_minimize_self-contained_source_using_cvise)
        -   [[2.1.9] [\[bonus\] Check if bug still exists on vanilla gcc master]](#.5Bbonus.5D_Check_if_bug_still_exists_on_vanilla_gcc_master)
        -   [[2.1.10] [\[bonus\] Report bug on gcc.gnu.org/bugzilla]](#.5Bbonus.5D_Report_bug_on_gcc.gnu.org.2Fbugzilla)
        -   [[2.1.11] [\[bonus\] Extract gcc backtrace]](#.5Bbonus.5D_Extract_gcc_backtrace)
        -   [[2.1.12] [\[bonus\] Fix gcc bug]](#.5Bbonus.5D_Fix_gcc_bug)
-   [[3] [LTO example]](#LTO_example)
    -   [[3.1] [Summary]](#Summary)
    -   [[3.2] [Extract the exact compiler command]](#Extract_the_exact_compiler_command)
    -   [[3.3] [Minimize responsible objects]](#Minimize_responsible_objects)
        -   [[3.3.1] [Debugging the compiler]](#Debugging_the_compiler)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Quick guide]

### [][Tl;DR]

1.  Extract self-contained preprocessed file (extracted with `-save-temps`)
2.  Verify [gcc] still crashes when ran on preprocessed file
3.  Expand `-march=native` to flags not dependent on the local machine
4.  File a bug on [https://bugs.gentoo.org](https://bugs.gentoo.org) with the following details:
    1.  Provide a preprocessed file (or a minimized file)
    2.  Provide `gcc -v` output
    3.  Provide `emerge --info`
    4.  Provide `-march=native` expansion
5.  \[optional\] Minimize amount of flags needed to trigger the error
6.  \[optional\] Minimize self-contained example
7.  \[optional\] File a bug on [https://gcc.gnu.org/bugzilla](https://gcc.gnu.org/bugzilla)

This resume will probably not suffice for most readers, read on to the detailed guide below!

## [Detailed guide]

### [][Steps to track an ICE (internal compiler errors) down]

#### [][Rebuilding GCC and glibc with debugging symbols (optional)]

** Important**\
This consumes several gigabytes of disk space. Gentoo Wiki\'s [Debugging](https://wiki.gentoo.org/wiki/Debugging "Debugging") page contains more explanations on the topic.

** Warning**\
Using the `installsources` `FEATURE` requires [[[dev-util/debugedit]](https://packages.gentoo.org/packages/dev-util/debugedit)[]] to be installled prior to the following explanations.

To get more detailed [GCC] crash reports it is suggested to rebuild it with debugging symbols and keeping the full sources. As GCC and glibc are tightly coupled, it is also suggested to do the same for the latter to have more readable traces:

-   Create the following files in the directory [/etc/portage/env]:

[FILE] **`/etc/portage/env/debugsyms`**

    CFLAGS="$ -ggdb3"
    CXXFLAGS="$ -ggdb3"
    FEATURES="$ splitdebug compressdebug -nostrip"

[FILE] **`/etc/portage/env/installsources`**

    FEATURES="$ installsources"

[FILE] **`/etc/portage/env/no-builtin-strlen`**

    CFLAGS="$ -fno-builtin-strlen"

-   The next step is to activate those settings for [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]], create the following file in [/etc/portage/packages.env]:

[FILE] **`/etc/portage/package.env/gcc`**

    sys-devel/gcc debugsyms installsources

-   Do the same for [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]], however that latter case depends on if [Valgrind] is used or not. So create **one** of the following files according to the current use case:

[FILE] **`/etc/portage/package.env/glibc`(package.env settings for sys-libs/glibc for systems using Valgrind)**

    # Valgrind requires -fno-builtin-strlen for glibc
    sys-libs/glibc no-builtin-strlen debugsyms installsources

[FILE] **`/etc/portage/package.env/glibc`(package.env settings for sys-libs/glibc for systems without Valgrind)**

    sys-libs/glibc debugsyms installsources

-   Finally emerge [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] and [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] again:

`root `[`#`]`emerge --ask -1 sys-libs/glibc sys-devel/gcc`

** Tip**\
If the system has several slotted [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] installations, emerge again each of those.

#### [Check if an ICE is reproducible]

Sometimes GCC crashes due to external reasons not directly related to GCC:

-   Out-of-memory condition (check [dmesg])
-   Bad RAM modules ([[[sys-apps/memtest86+]](https://packages.gentoo.org/packages/sys-apps/memtest86+)[]])
-   Unstable overclock of CPU or RAM

Make sure to not be in any of the above cases!

Look at [build.log] with the ICE and try to resume the build to see if the same command causes the same ICE. Usually the command looks something like `make --jobs=8 --load-average=8 CPPFLAGS= CFLAGS= LDFLAGS=`.

Go to the `Working directory` (specified in [build.log] as well) and rerun the build command.

The exact command and the failure should be seen.

Our running example will be an ICE on `dev-lang/python-3.6.5`:

`user `[`$`]`cd '/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5'`

`user `[`$`]`LANG=C make`

    running build
    running build_ext
    INFO: Can't locate Tcl/Tk libs and/or headers
    building 'cmath' extension
    gcc-7.3.0 -pthread -fPIC -Wno-unused-result -Wsign-compare -DNDEBUG -march=prescott -mfpmath=sse -O2 -pipe -fomit-frame-pointer -fwrapv -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -I./Include -I. -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Include -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5 -c /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.c -o build/temp.linux-i686-3.6/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.o
    In file included from /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.c:11:0:
    /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/clinic/cmathmodule.c.h: In function 'cmath_acos':
    /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/clinic/cmathmodule.c.h:45:1: internal compiler error: Segmentation fault
     }
     ^
    Please submit a full bug report,
    with preprocessed source if appropriate.
    See <https://bugs.gentoo.org/> for instructions.

The build fails every time `LANG=C make` is rerun. Yay!

#### [Extract exact command]

If the build system already prints exact command, just re-execute it (make sure to be are in the correct directory). If the build system does not print the command, use other methods of getting the command like running `strace` or passing verbose flags manually.

In the case of Python, the command is printed as-is:

`user `[`$`]`LANG=C gcc-7.3.0 -pthread -fPIC -Wno-unused-result -Wsign-compare -DNDEBUG -march=prescott -mfpmath=sse -O2 -pipe -fomit-frame-pointer -fwrapv -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -I./Include -I. -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Include -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5 -c /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.c -o build/temp.linux-i686-3.6/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.o`

    In file included from /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.c:11:0:
    /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/clinic/cmathmodule.c.h: In function 'cmath_acos':
    /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/clinic/cmathmodule.c.h:45:1: internal compiler error: Segmentation fault
     }
     ^
    Please submit a full bug report,
    with preprocessed source if appropriate.
    See <https://bugs.gentoo.org/> for instructions.

#### [][Extract self-contained source (use -save-temps)]

Add `-save-temps` to the [gcc] command on the previous step to extract a preprocessed sample. `foo.c` will create `foo.i` (or `foo.ii` for `c++`).

Obligatory Python example:

`user `[`$`]`LANG=C gcc-7.3.0 -pthread -fPIC -Wno-unused-result -Wsign-compare -DNDEBUG -march=prescott -mfpmath=sse -O2 -pipe -fomit-frame-pointer -fwrapv -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -I./Include -I. -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Include -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5 -c /var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.c -o build/temp.linux-i686-3.6/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Modules/cmathmodule.o -save-temps`

    ... same failure ...

The preprocessed file is in `cmathmodule.i` now. Get more tips at [https://gcc.gnu.org/bugs/](https://gcc.gnu.org/bugs/).

#### [][Expand -march=native, exact gcc version and other system-specific options]

Some compiler options like `-march=native` are dependent on the environment. They must be resolved into exact options. One way to do it is to query [gcc] for expansion.

Comparing with the default -march gives:

`user `[`$`]`for t in param target optimize optimizer; do cmd="gcc -Q --help=$t"; diff -U0 <(LANG=C $cmd) <(LANG=C $cmd -march=native); done`

    --- /dev/fd/63    2020-06-10 22:26:45.832792880 +0100
    +++ /dev/fd/62  2020-06-10 22:26:45.832792880 +0100
    @@ -70,3 +70,3 @@
    -  --param=l1-cache-line-size=      32
    -  --param=l1-cache-size=           64
    -  --param=l2-cache-size=           512
    +  --param=l1-cache-line-size=      64
    +  --param=l1-cache-size=           32
    +  --param=l2-cache-size=           8192
    --- /dev/fd/61  2020-06-10 22:26:45.856792856 +0100
    +++ /dev/fd/60  2020-06-10 22:26:45.856792856 +0100
    @@ -16 +16 @@
    -  -maes                            [disabled]
    +  -maes                            [enabled]
    @@ -26 +26 @@
    -  -mavx                            [disabled]
    +  -mavx                            [enabled]
    ...

The diff can be minimized to reduce noise if a common arch baseline like x86-64-v2 is used:

`user `[`$`]`march=x86-64-v2; for t in param target optimize optimizer; do cmd="gcc -Q --help=$t"; diff -U0 <(LANG=C $cmd) <(LANG=C $cmd -march=native); done`

    --- /dev/fd/63  2023-12-18 23:10:40.048490713 +0000
    +++ /dev/fd/62  2023-12-18 23:10:40.049490723 +0000
    @@ -26 +26 @@
    -  --param=avoid-fma-max-bits=<0,512>           0
    +  --param=avoid-fma-max-bits=<0,512>           512
    @@ -241 +241 @@
    -  --param=simultaneous-prefetches=     6
    +  --param=simultaneous-prefetches=     100
    --- /dev/fd/63  2023-12-18 23:10:40.062490859 +0000
    +++ /dev/fd/62  2023-12-18 23:10:40.063490870 +0000
    @@ -13 +13 @@
    -  -mabm                                [disabled]
    +  -mabm                                [enabled]
    @@ -16,2 +16,2 @@
    -  -madx                                [disabled]
    -  -maes                                [disabled]
    +  -madx                                [enabled]
    +  -maes                                [enabled]
    @@ -33 +33 @@
    -  -march=                              x86-64-v4
    +  -march=                              znver2
    [...]

\
Here `-march=native` is substituted for `-march=x86-64-v2 --param=avoid-fma-max-bits=512 -mabm ...`.

Make sure bug is reproducible after substitution as well!

#### [Report bug on bugs.gentoo.org]

File a bug at [https://bugs.gentoo.org/](https://bugs.gentoo.org/) against toolchain@gentoo.org and provide a few details:

-   `gcc -v` output
-   Attach `.i` reproducer

#### [][\[bonus\] minimize needed flags to reproduce failure]

It is possible to do similar expansion for optimizer options as well: `LANG=C gcc -O2 -Q --help=optimizers`

To expand `-O3` into `-O2 + extra`, one option is to use `diff -U0 <(LANG=C gcc -O2 -Q --help=optimizers) <(LANG=C gcc -O3 -Q --help=optimizers)`

Try to find minimal set of flags needed to trigger the crash by removing some expanded options.

#### [][\[bonus\] minimize self-contained source using cvise]

Now to the fun part! Let\'s shrink `.i` down to a manageable size with help of [[[dev-util/cvise]](https://packages.gentoo.org/packages/dev-util/cvise)[]].

1.  :::: cmd-box


    `root `[`#`]`emerge --ask dev-util/cvise`


    ::::

2.  Write a [test.sh] tester:

    ::: box-caption
    [FILE] **`test.sh`**
    :::

    :::
        LANG=C gcc-7.3.0 -pthread -fPIC -Wno-unused-result -Wsign-compare -DNDEBUG -march=prescott -mfpmath=sse -O2 -pipe -fomit-frame-pointer -fwrapv -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -I./Include -I. -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Include -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5 -c cmathmodule.i -o cmathmodule.o \
        >gcc_out.txt 2>&1
        grep "internal compiler error" gcc_out.txt >/dev/null 2>&1
    :::

3.  Validate tester

    ::::: cmd-box


    `user `[`$`]`./test.sh`





    `user `[`$`]`echo $?`



        0
    :::::

4.  Reduce!

`user `[`$`]`cvise test.sh cmathmodule.i`

    ===< 2430 >===
    running 4 interestingness tests in parallel
    ===< pass_includes :: 0 >===
    ===< pass_unifdef :: 0 >===
    ===< pass_comments :: 0 >===
    ===< pass_blank :: 0 >===
    (1.2 %, 733906 bytes)
    (27.4 %, 539234 bytes)
    ===< pass_clang_binsrch :: replace-function-def-with-decl >===
    (29.5 %, 523834 bytes)
    (30.2 %, 518466 bytes)
    (32.0 %, 505350 bytes)
    ...
              ******** cmathmodule.i ********

    typedef struct  b;
    b c;
    d, e, f;
    g()

Done!

[cmathmodule.i] contains the same shrunk example.

The tester command may also be passed directly to [cvise] without creating a shell script, e.g.:

`user `[`$`]`LANG=C cvise --commands "gcc-7.3.0 -pthread -fPIC -Wno-unused-result -Wsign-compare -DNDEBUG -march=prescott -mfpmath=sse -O2 -pipe -fomit-frame-pointer -fwrapv -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -I./Include -I. -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5/Include -I/var/tmp/portage/dev-lang/python-3.6.5/work/Python-3.6.5 -c cmathmodule.i -o cmathmodule.o |& fgrep \"internal compiler error\"" cmathmodule.i`

#### [][\[bonus\] Check if bug still exists on vanilla gcc master]

Building [gcc] locally could look like:

`user `[`$`]`git clone git://gcc.gnu.org/git/gcc.git `

`user `[`$`]`mkdir -p gcc-build && cd gcc-build `

`user `[`$`]`../gcc/configure --enable-languages=c,c++ --disable-bootstrap --prefix="$(pwd)/../gcc-installed" --disable-nls CFLAGS="-O1 -ggdb" CXXFLAGS="-O1 -ggdb" `

`user `[`$`]`make && make install`

Look at configure options of Gentoo\'s [gcc -v] to get more options to add to defaults. Be careful: some configure options like `--enable-default-pie --enable-default-ssp` can change code generation enough to trigger or hide a bug.

#### [][\[bonus\] Report bug on gcc.gnu.org/bugzilla]

File the bug at [https://gcc.gnu.org/bugzilla/](https://gcc.gnu.org/bugzilla/) with attached minimal reproducer and `gcc -v` detals.

#### [][\[bonus\] Extract gcc backtrace]

Example session would be:

`user `[`$`]`gdb --quiet --args gcc-7.3.0 -fPIC -march=prescott -mfpmath=sse -O1 -c cmathmodule.c -o cmathmodule.o`

    (gdb) set follow-fork-mode child
    (gdb) break internal_error
    (gdb) run
    ...
    Thread 2.1 "cc1" received signal SIGSEGV, Segmentation fault.
    [Switching to process 17286]
    0x085375d4 in lra_eliminate_reg_if_possible(rtx_def**) ()
    (gdb) bt
    #0  0x085375d4 in lra_eliminate_reg_if_possible(rtx_def**) ()
    ...

#### [][\[bonus\] Fix gcc bug]

By now a source tree and a command for how to build it will be available!

A few starting points:

-   [https://gcc.gnu.org/contribute.html](https://gcc.gnu.org/contribute.html) for general notes on coding tips and guidelines
-   [https://gcc.gnu.org/onlinedocs/](https://gcc.gnu.org/onlinedocs/)

Good luck!

## [LTO example]

LTO bugs are harder to track down because there\'s an extra step (a few) between the compiler and the final binary.

GCC\'s [wiki](https://gcc.gnu.org/wiki/A_guide_to_testcase_reduction#Reducing_LTO_bugs) and [LinkTimeOptimization](https://gcc.gnu.org/wiki/LinkTimeOptimization) touches on this.

[PR105600](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105600) is an example of such a GCC bug.

Tip: experiment with `-flto-partition=1to1`, `-flto-partition=none`, and `-flto-partition=one`. They can help with reduction depending on the failure.

### [Summary]

The following example is based on a real case ([[[bug #903868]](https://bugs.gentoo.org/show_bug.cgi?id=903868)[]]). The first part is to narrow things down to have a minimal set of files then in a second movement, investigate why the error condition is triggered.

### [Extract the exact compiler command]

** Tip**\
[make VERBOSE=1 \...] may need to be run manually if CMake is used to get more details.

Whenever the compilation fails with an LTO error, the very first step is to look at what the file [build.log] contains and search inside for the string `FAILED:` (typically, it just precedes the compiler crash dump):

[FILE] **`/var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/build.log`**

    (...)
    FAILED: bin/xdg-desktop-portal-kde
    : && /usr/bin/x86_64-pc-linux-gnu-g++ -O3 -pipe -march=native -fomit-frame-pointer -fopt-info-vec -fcf-protection=return -flto=auto -ffat-lto-objects -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -fdiagnostics-color=always -Wl,--enable-new-dtags -flto=auto     -pthread src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/mocs_compilation.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/access.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/accessdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/account.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooser.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooserdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/background.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dbushelpers.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/desktopportal.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/email.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/filechooser.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/globalshortcuts.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/inhibit.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notification.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notificationinhibition.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/outputsmodel.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/print.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/quickdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktop.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktopdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/request.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencast.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencasting.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencastwidget.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenchooserdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshot.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshotdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/session.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/settings.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/userinfodialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/utils.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/waylandintegration.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/portalicon.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncher.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncherdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdgshortcut.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/background_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notificationinhibition_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/access_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/account_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/settings_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooser_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/desktopportal_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncher_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncherdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/email_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/filechooser_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/inhibit_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notification_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/print_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktop_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktopdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/request_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencast_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshot_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshotdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/session_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/waylandintegration_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/accessdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/kglobalaccel_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/kglobalaccel_component_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/wayland-zkde-screencast-unstable-v1-protocol.c.o src/CMakeFiles/xdg-desktop-portal-kde.dir/qwayland-zkde-screencast-unstable-v1.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/wayland-wayland-protocol.c.o src/CMakeFiles/xdg-desktop-portal-kde.dir/qwayland-wayland.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/user_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/documents_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/fuse_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/fdo_application_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/EWIEGA46WW/qrc_resources.cpp.o -o bin/xdg-desktop-portal-kde  /usr/lib64/libKF5Declarative.so.5.105.0  /usr/lib64/libKF5Notifications.so.5.105.0  /usr/lib64/libKF5WaylandClient.so.5.105.0  lib/libKirigamiFilepicker.a  /usr/lib64/libwayland-client.so  /usr/lib64/libQt5QuickWidgets.so.5.15.8  /usr/lib64/libKF5Package.so.5.105.0  /usr/lib64/libKF5KIOFileWidgets.so.5.105.0  /usr/lib64/libKF5KIOWidgets.so.5.105.0  /usr/lib64/libKF5KIOGui.so.5.105.0  /usr/lib64/libKF5WindowSystem.so.5.105.0  /usr/lib64/libX11.so  /usr/lib64/libKF5JobWidgets.so.5.105.0  /usr/lib64/libKF5Completion.so.5.105.0  /usr/lib64/libKF5Bookmarks.so.5.105.0  /usr/lib64/libKF5XmlGui.so.5.105.0  /usr/lib64/libKF5GlobalAccel.so.5.105.0  /usr/lib64/libKF5IconThemes.so.5.105.0  /usr/lib64/libQt5PrintSupport.so.5.15.8  /usr/lib64/libKF5ItemViews.so.5.105.0  /usr/lib64/libKF5ConfigWidgets.so.5.105.0  /usr/lib64/libKF5GuiAddons.so.5.105.0  /usr/lib64/libQt5WaylandClient.so.5.15.8  /usr/lib64/libKF5WidgetsAddons.so.5.105.0  /usr/lib64/libKF5ConfigGui.so.5.105.0  /usr/lib64/libKF5Codecs.so.5.105.0  /usr/lib64/libKF5Auth.so.5.105.0  /usr/lib64/libQt5Widgets.so.5.15.8  /usr/lib64/libKF5Solid.so.5.105.0  /usr/lib64/libQt5Quick.so.5.15.8  /usr/lib64/libQt5QmlModels.so.5.15.8  /usr/lib64/libQt5Qml.so.5.15.8  /usr/lib64/libKF5KIOCore.so.5.105.0  /usr/lib64/libKF5Service.so.5.105.0  /usr/lib64/libKF5ConfigCore.so.5.105.0  /usr/lib64/libKF5I18n.so.5.105.0  /usr/lib64/libQt5Concurrent.so.5.15.8  /usr/lib64/libQt5Network.so.5.15.8  /usr/lib64/libQt5Xml.so.5.15.8  /usr/lib64/libKF5AuthCore.so.5.105.0  /usr/lib64/libKF5CoreAddons.so.5.105.0  /usr/lib64/libQt5DBus.so.5.15.8  /usr/lib64/libQt5XkbCommonSupport.a  /usr/lib64//libQt5Gui.so  /usr/lib64//libQt5Core.so  /usr/lib64/libxkbcommon.so  /usr/lib64/libGL.so  /usr/lib64/libQt5Gui.so.5.15.8  /usr/lib64/libQt5Core.so.5.15.8 && :
    lto1: internal compiler error: Segmentation fault
    0xd75173 crash_signal
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/toplev.cc:314
    0x7f232bba75df ???
            /usr/src/debug/sys-libs/glibc-2.37-r1/glibc-2.37/signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c:0
    0x8bd220 bp_unpack_string(data_in*, bitpack_d*)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/data-streamer-in.cc:112
    0xc7c27f cl_optimization_stream_in(data_in*, bitpack_d*, cl_optimization*)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/build/gcc/options-save.cc:13501
    0xfeb513 streamer_read_tree_bitfields(lto_input_block*, data_in*, tree_node*)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/tree-streamer-in.cc:562
    0xbe071b lto_read_tree_1
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto-streamer-in.cc:1713
    0xbe0c20 lto_read_tree
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto-streamer-in.cc:1760
    0xbe0c20 lto_input_tree_1(lto_input_block*, data_in*, LTO_tags, unsigned int)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto-streamer-in.cc:1901
    0xbe0e6b lto_input_scc(lto_input_block*, data_in*, unsigned int*, unsigned int*, bool)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto-streamer-in.cc:1789
    0x83f9d4 lto_read_decls
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto-common.cc:1908
    0x83f9d4 lto_file_finalize
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto-common.cc:2288
    0x83f9d4 lto_create_files_from_ids
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto-common.cc:2298
    0x83f9d4 lto_file_read
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto-common.cc:2353
    0x83f9d4 read_cgraph_and_symbols(unsigned int, char const**)
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto-common.cc:2801
    0x80e5d6 lto_main()
            /usr/src/debug/sys-devel/gcc-13.0.1_pre20230409-r3/gcc-13-20230409/gcc/lto/lto.cc:654
    Please submit a full bug report, with preprocessed source (by using -freport-bug).
    Please include the complete backtrace with any bug report.
    See <https://bugs.gentoo.org/> for instructions.
    lto-wrapper: fatal error: /usr/bin/x86_64-pc-linux-gnu-g++ returned 1 exit status
    compilation terminated.
    /usr/lib/gcc/x86_64-pc-linux-gnu/13/../../../../x86_64-pc-linux-gnu/bin/ld: error: lto-wrapper failed
    collect2: error: ld returned 1 exit status

Pay attention to the two double ampersands (`&&`) that enclose the full command line. This is our point of interest, copy what is enclosed in-between and keep it somewhere - it will get used later in this section. For now, just change the working directory for the failed package\'s one somewhere under [/var/tmp/portage]. Here:

`root `[`#`]`cd /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1`

From this vantage point of view:

`root `[`#`]`ls -l work`

    total 22
    drwxr-xr-x 8 portage portage 17 Apr 13 12:42 xdg-desktop-portal-kde-5.27.4.1
    drwxr-xr-x 8 portage portage 19 Apr 13 12:42 xdg-desktop-portal-kde-5.27.4.1_build

Now there are two subdirectories:

-   [xdg-desktop-portal-kde-5.27.4.1] is where the package source files reside (notably)
-   [xdg-desktop-portal-kde-5.27.4.1_build] is where the object files resulting from the compilation process are put (plus some other things we ignore for the moment).

So from the above GCC command line perspective:

-   All [.cpp] files relative paths are relative to [xdg-desktop-portal-kde-5.27.4.1]
-   All [.cpp.o] files relative paths are relative to [xdg-desktop-portal-kde-5.27.4.1_build]
-   All [.a] files relative paths are relative to [xdg-desktop-portal-kde-5.27.4.1_build]

** Important**\
This classification is very important to keep in mind because a couple of operations hereafter depends on this directory tree structure.

On closer look at the above command line, it can be decomposed in three consecutive parts:

-   Part A =\> spans from `-O3` to `-lpthread` this is the various options that governs the GCC\'s behavior
-   Part B =\> spans from `src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/mocs_compilation.cpp.o` to `src/CMakeFiles/xdg-desktop-portal-kde.dir/fdo_application_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/EWIEGA46WW/qrc_resources.cpp.o` this big list is all of the object files previouly produced by GCC (we are at the final compilation stage\... optimize and link with all other needed objects files and librairies)
-   Part C =\> spans from `-o bin/xdg-desktop-portal-kde` to `/usr/lib64/libQt5Core.so.5.15.8` which is the list of the libraries/shared object files GCC will link against with.

Notice the presence of a relative path in the middle of part C which is [lib/libKirigamiFilepicker.a]. This file is produced by some previous building steps of the package [[[kde-plasma/xdg-desktop-portal-kde]](https://packages.gentoo.org/packages/kde-plasma/xdg-desktop-portal-kde)[]] itself, it will be taken care of a bit later.

### [Minimize responsible objects]

The failure is in [lto1] which by its nature is considering multiple objects. To narrow down the failure, the full command being passed must be considered.

Let\'s focus on part B (the big list of `.cpp.o` files) of the GCC command-line. The goal is to transform all of those relative paths of this list to their absolute path counterparts. Remember the directory structure mentioned in the previous section herebefore? All of those `.cpp.o` files are residing under [xdg-desktop-portal-kde-5.27.4.1_build], thus their path must be prepended with that latter one. As [xdg-desktop-portal-kde-5.27.4.1_build] resides itself under [/var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work], **the full path to prepend with is: [/var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build]**.

Now, create a file (here named [full_objects_list]) which contains the whole list of those `.cpp.o` files (*do not reformat it!* just copy/paste the whole list as is). The result should be like:

[FILE] **`'full_objects_list'`**

    src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/mocs_compilation.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/access.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/accessdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/account.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooser.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooserdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/background.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dbushelpers.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/desktopportal.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/email.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/filechooser.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/globalshortcuts.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/inhibit.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notification.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notificationinhibition.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/outputsmodel.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/print.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/quickdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktop.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktopdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/request.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencast.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencasting.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencastwidget.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenchooserdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshot.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshotdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/session.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/settings.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/userinfodialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/utils.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/waylandintegration.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/portalicon.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncher.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncherdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdgshortcut.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/background_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notificationinhibition_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/access_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/account_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/settings_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/appchooser_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/desktopportal_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncher_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/dynamiclauncherdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/email_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/filechooser_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/inhibit_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/notification_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/print_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktop_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/remotedesktopdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/request_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screencast_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshot_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/screenshotdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/session_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/waylandintegration_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/accessdialog_debug.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/kglobalaccel_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/kglobalaccel_component_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/wayland-zkde-screencast-unstable-v1-protocol.c.o src/CMakeFiles/xdg-desktop-portal-kde.dir/qwayland-zkde-screencast-unstable-v1.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/wayland-wayland-protocol.c.o src/CMakeFiles/xdg-desktop-portal-kde.dir/qwayland-wayland.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/user_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/documents_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/fuse_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/fdo_application_interface.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/EWIEGA46WW/qrc_resources.cpp.o

Now transform [full_objects_list] to not only convert relative paths to absolute paths but also put one item of the list per line. Here is [tr] comes at the rescue (don\'t forget the final slash in the [sed] directive!):

`root `[`#`]`cat full_objects_list | tr ' ' '\n' | sed -e "s:^:/var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/:" > full_objects_list_fixed `

The file [full_objects_list_fixed] should look like this (one file per line):

[FILE] **`'full_objects_list'`**

    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build//src/CMakeFiles/xdg-desktop-portal-kde.dir/xdg-desktop-portal-kde_autogen/mocs_compilation.cpp.o
    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/src/CMakeFiles/xdg-desktop-portal-kde.dir/access.cpp.o
    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/src/CMakeFiles/xdg-desktop-portal-kde.dir/accessdialog.cpp.o src/CMakeFiles/xdg-desktop-portal-kde.dir/account.cpp.o
    (...)

Now create a copy of the [full_objects_list_fixed] and name it [bad] (the original contents will be needed later):

`root `[`#`]`cp full_objects_list_fixed bad`

The crunchy part is to use [cvise-delta] (Package [[[dev-util/cvise]](https://packages.gentoo.org/packages/dev-util/cvise)[]]) to reduce the contents of the list stored in the file [bad] to the bare minimum. The only missing piece of that puzzle is to write a small shell-script (here named [check.sh]) that will be used by [cvise-delta] and this where the \"part A\" and the \"part B\" (respectively the set of options controlling the compiler\'s behaviour and the set of libraries to link with) as talked about in the previous section appears in the landscape.

While \"part A\" can be kept as is (after all the very same options set to reproduce the crash are wanted), however, \"part B\" needs to be changed a little bit. So this:

`-o bin/xdg-desktop-portal-kde /usr/lib64/libKF5Declarative.so.5.105.0 /usr/lib64/libKF5Notifications.so.5.105.0 /usr/lib64/libKF5WaylandClient.so.5.105.0 /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/lib/libKirigamiFilepicker.a /usr/lib64/libwayland-client.so /usr/lib64/libQt5QuickWidgets.so.5.15.8 /usr/lib64/libKF5Package.so.5.105.0 /usr/lib64/libKF5KIOFileWidgets.so.5.105.0 /usr/lib64/libKF5KIOWidgets.so.5.105.0 /usr/lib64/libKF5KIOGui.so.5.105.0 /usr/lib64/libKF5WindowSystem.so.5.105.0 /usr/lib64/libX11.so /usr/lib64/libKF5JobWidgets.so.5.105.0 /usr/lib64/libKF5Completion.so.5.105.0 /usr/lib64/libKF5Bookmarks.so.5.105.0 /usr/lib64/libKF5XmlGui.so.5.105.0 /usr/lib64/libKF5GlobalAccel.so.5.105.0 /usr/lib64/libKF5IconThemes.so.5.105.0 /usr/lib64/libQt5PrintSupport.so.5.15.8 /usr/lib64/libKF5ItemViews.so.5.105.0 /usr/lib64/libKF5ConfigWidgets.so.5.105.0 /usr/lib64/libKF5GuiAddons.so.5.105.0 /usr/lib64/libQt5WaylandClient.so.5.15.8 /usr/lib64/libKF5WidgetsAddons.so.5.105.0 /usr/lib64/libKF5ConfigGui.so.5.105.0 /usr/lib64/libKF5Codecs.so.5.105.0 /usr/lib64/libKF5Auth.so.5.105.0 /usr/lib64/libQt5Widgets.so.5.15.8 /usr/lib64/libKF5Solid.so.5.105.0 /usr/lib64/libQt5Quick.so.5.15.8 /usr/lib64/libQt5QmlModels.so.5.15.8 /usr/lib64/libQt5Qml.so.5.15.8 /usr/lib64/libKF5KIOCore.so.5.105.0 /usr/lib64/libKF5Service.so.5.105.0 /usr/lib64/libKF5ConfigCore.so.5.105.0 /usr/lib64/libKF5I18n.so.5.105.0 /usr/lib64/libQt5Concurrent.so.5.15.8 /usr/lib64/libQt5Network.so.5.15.8 /usr/lib64/libQt5Xml.so.5.15.8 /usr/lib64/libKF5AuthCore.so.5.105.0 /usr/lib64/libKF5CoreAddons.so.5.105.0 /usr/lib64/libQt5DBus.so.5.15.8 /usr/lib64/libQt5XkbCommonSupport.a /usr/lib64//libQt5Gui.so /usr/lib64//libQt5Core.so /usr/lib64/libxkbcommon.so /usr/lib64/libGL.so /usr/lib64/libQt5Gui.so.5.15.8 /usr/lib64/libQt5Core.so.5.15.8 `

Becomes that:

`@bad -o /dev/null /usr/lib64/libKF5Declarative.so.5.105.0 /usr/lib64/libKF5Notifications.so.5.105.0 /usr/lib64/libKF5WaylandClient.so.5.105.0 lib/libKirigamiFilepicker.a /usr/lib64/libwayland-client.so /usr/lib64/libQt5QuickWidgets.so.5.15.8 /usr/lib64/libKF5Package.so.5.105.0 /usr/lib64/libKF5KIOFileWidgets.so.5.105.0 /usr/lib64/libKF5KIOWidgets.so.5.105.0 /usr/lib64/libKF5KIOGui.so.5.105.0 /usr/lib64/libKF5WindowSystem.so.5.105.0 /usr/lib64/libX11.so /usr/lib64/libKF5JobWidgets.so.5.105.0 /usr/lib64/libKF5Completion.so.5.105.0 /usr/lib64/libKF5Bookmarks.so.5.105.0 /usr/lib64/libKF5XmlGui.so.5.105.0 /usr/lib64/libKF5GlobalAccel.so.5.105.0 /usr/lib64/libKF5IconThemes.so.5.105.0 /usr/lib64/libQt5PrintSupport.so.5.15.8 /usr/lib64/libKF5ItemViews.so.5.105.0 /usr/lib64/libKF5ConfigWidgets.so.5.105.0 /usr/lib64/libKF5GuiAddons.so.5.105.0 /usr/lib64/libQt5WaylandClient.so.5.15.8 /usr/lib64/libKF5WidgetsAddons.so.5.105.0 /usr/lib64/libKF5ConfigGui.so.5.105.0 /usr/lib64/libKF5Codecs.so.5.105.0 /usr/lib64/libKF5Auth.so.5.105.0 /usr/lib64/libQt5Widgets.so.5.15.8 /usr/lib64/libKF5Solid.so.5.105.0 /usr/lib64/libQt5Quick.so.5.15.8 /usr/lib64/libQt5QmlModels.so.5.15.8 /usr/lib64/libQt5Qml.so.5.15.8 /usr/lib64/libKF5KIOCore.so.5.105.0 /usr/lib64/libKF5Service.so.5.105.0 /usr/lib64/libKF5ConfigCore.so.5.105.0 /usr/lib64/libKF5I18n.so.5.105.0 /usr/lib64/libQt5Concurrent.so.5.15.8 /usr/lib64/libQt5Network.so.5.15.8 /usr/lib64/libQt5Xml.so.5.15.8 /usr/lib64/libKF5AuthCore.so.5.105.0 /usr/lib64/libKF5CoreAddons.so.5.105.0 /usr/lib64/libQt5DBus.so.5.15.8 /usr/lib64/libQt5XkbCommonSupport.a /usr/lib64//libQt5Gui.so /usr/lib64//libQt5Core.so /usr/lib64/libxkbcommon.so /usr/lib64/libGL.so /usr/lib64/libQt5Gui.so.5.15.8 /usr/lib64/libQt5Core.so.5.15.8 2>&1 | grep -q "internal compiler error" `

The three brought-in changes are:

-   Replacing the original `-o bin/xdg-desktop-portal-kde` by `@bad -o /dev/null` to make GCC consider the object list stored in the file [bad] (rather than the original full-fledged list) and make GCC output the result to [/dev/null].
-   Substituting the relative path of [libKirigamiFilepicker.a] for its absolute one counterpart (this is an archive produced by the package itself, not something external)
-   Appending `2>&1 | grep -q "internal compiler error"` at the very end

Putting all pieces together, the test script [check.sh] is this one:

[FILE] **`check.sh`**

    #!/bin/bash
    # Reproduces the ICE by calling g++ on object files (within @bad)
    /usr/bin/x86_64-pc-linux-gnu-g++ -O3 -pipe -march=native -fomit-frame-pointer -fopt-info-vec -fcf-protection=return -flto=auto -ffat-lto-objects -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -fdiagnostics-color=always -Wl,--enable-new-dtags -flto=auto -pthread @bad -o /dev/null /usr/lib64/libKF5Declarative.so.5.105.0  /usr/lib64/libKF5Notifications.so.5.105.0  /usr/lib64/libKF5WaylandClient.so.5.105.0 /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/lib/libKirigamiFilepicker.a  /usr/lib64/libwayland-client.so  /usr/lib64/libQt5QuickWidgets.so.5.15.8  /usr/lib64/libKF5Package.so.5.105.0  /usr/lib64/libKF5KIOFileWidgets.so.5.105.0  /usr/lib64/libKF5KIOWidgets.so.5.105.0  /usr/lib64/libKF5KIOGui.so.5.105.0  /usr/lib64/libKF5WindowSystem.so.5.105.0  /usr/lib64/libX11.so  /usr/lib64/libKF5JobWidgets.so.5.105.0  /usr/lib64/libKF5Completion.so.5.105.0  /usr/lib64/libKF5Bookmarks.so.5.105.0  /usr/lib64/libKF5XmlGui.so.5.105.0  /usr/lib64/libKF5GlobalAccel.so.5.105.0  /usr/lib64/libKF5IconThemes.so.5.105.0  /usr/lib64/libQt5PrintSupport.so.5.15.8  /usr/lib64/libKF5ItemViews.so.5.105.0  /usr/lib64/libKF5ConfigWidgets.so.5.105.0  /usr/lib64/libKF5GuiAddons.so.5.105.0  /usr/lib64/libQt5WaylandClient.so.5.15.8  /usr/lib64/libKF5WidgetsAddons.so.5.105.0  /usr/lib64/libKF5ConfigGui.so.5.105.0  /usr/lib64/libKF5Codecs.so.5.105.0  /usr/lib64/libKF5Auth.so.5.105.0  /usr/lib64/libQt5Widgets.so.5.15.8  /usr/lib64/libKF5Solid.so.5.105.0  /usr/lib64/libQt5Quick.so.5.15.8  /usr/lib64/libQt5QmlModels.so.5.15.8  /usr/lib64/libQt5Qml.so.5.15.8  /usr/lib64/libKF5KIOCore.so.5.105.0  /usr/lib64/libKF5Service.so.5.105.0  /usr/lib64/libKF5ConfigCore.so.5.105.0  /usr/lib64/libKF5I18n.so.5.105.0  /usr/lib64/libQt5Concurrent.so.5.15.8  /usr/lib64/libQt5Network.so.5.15.8  /usr/lib64/libQt5Xml.so.5.15.8  /usr/lib64/libKF5AuthCore.so.5.105.0  /usr/lib64/libKF5CoreAddons.so.5.105.0  /usr/lib64/libQt5DBus.so.5.15.8  /usr/lib64/libQt5XkbCommonSupport.a  /usr/lib64//libQt5Gui.so  /usr/lib64//libQt5Core.so  /usr/lib64/libxkbcommon.so  /usr/lib64/libGL.so  /usr/lib64/libQt5Gui.so.5.15.8  /usr/lib64/libQt5Core.so.5.15.8 2>&1 | grep -q 'internal compiler error'

Now unleash the power of [cvise-delta]:

`root `[`#`]`chmod +x check.sh`

`root `[`#`]`cvise-delta ./check.sh bad`

    00:00:01 INFO ===< 20595 >===
    00:00:01 INFO running 16 interestingness tests in parallel
    00:00:01 INFO INITIAL PASSES
    00:00:01 INFO ===< LinesPass::None >===
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO ===< LinesPass::None >===
    00:00:02 INFO cache hit for /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad
    00:00:02 INFO MAIN PASSES
    00:00:02 INFO Termination check: size was 166; now 166
    00:00:02 INFO CLEANUP PASSES
    00:00:02 INFO ===================== done ====================
    ===< PASS statistics >===
      pass name                                              time (s) time (%)   worked   failed  total executed
      LinesPass::None                                            0.34    12.15        0        0               1

    Runtime: 3 seconds
    Reduced test-cases:

    --- /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/temp/bad ---
    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/src/CMakeFiles/xdg-desktop-portal-kde.dir/xdgshortcut.cpp.o

Now the file [bad] should contain only a small number of problematic object files:

`root `[`#`]`cat bad`

    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/src/CMakeFiles/xdg-desktop-portal-kde.dir/xdgshortcut.cpp.o

Manually invoke the [g++] command as it is in [check.sh] from the command-line with that reduced subset should trigger a compiler crash :

`root `[`#`]`/usr/bin/x86_64-pc-linux-gnu-g++ -O3 -pipe -march=native -fomit-frame-pointer -fopt-info-vec -fcf-protection=return -flto=auto -ffat-lto-objects -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -fdiagnostics-color=always -Wl,--enable-new-dtags -flto=auto -pthread @bad -o /dev/null /usr/lib64/libKF5Declarative.so.5.105.0 /usr/lib64/libKF5Notifications.so.5.105.0 /usr/lib64/libKF5WaylandClient.so.5.105.0 /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/lib/libKirigamiFilepicker.a /usr/lib64/libwayland-client.so /usr/lib64/libQt5QuickWidgets.so.5.15.8 /usr/lib64/libKF5Package.so.5.105.0 /usr/lib64/libKF5KIOFileWidgets.so.5.105.0 /usr/lib64/libKF5KIOWidgets.so.5.105.0 /usr/lib64/libKF5KIOGui.so.5.105.0 /usr/lib64/libKF5WindowSystem.so.5.105.0 /usr/lib64/libX11.so /usr/lib64/libKF5JobWidgets.so.5.105.0 /usr/lib64/libKF5Completion.so.5.105.0 /usr/lib64/libKF5Bookmarks.so.5.105.0 /usr/lib64/libKF5XmlGui.so.5.105.0 /usr/lib64/libKF5GlobalAccel.so.5.105.0 /usr/lib64/libKF5IconThemes.so.5.105.0 /usr/lib64/libQt5PrintSupport.so.5.15.8 /usr/lib64/libKF5ItemViews.so.5.105.0 /usr/lib64/libKF5ConfigWidgets.so.5.105.0 /usr/lib64/libKF5GuiAddons.so.5.105.0 /usr/lib64/libQt5WaylandClient.so.5.15.8 /usr/lib64/libKF5WidgetsAddons.so.5.105.0 /usr/lib64/libKF5ConfigGui.so.5.105.0 /usr/lib64/libKF5Codecs.so.5.105.0 /usr/lib64/libKF5Auth.so.5.105.0 /usr/lib64/libQt5Widgets.so.5.15.8 /usr/lib64/libKF5Solid.so.5.105.0 /usr/lib64/libQt5Quick.so.5.15.8 /usr/lib64/libQt5QmlModels.so.5.15.8 /usr/lib64/libQt5Qml.so.5.15.8 /usr/lib64/libKF5KIOCore.so.5.105.0 /usr/lib64/libKF5Service.so.5.105.0 /usr/lib64/libKF5ConfigCore.so.5.105.0 /usr/lib64/libKF5I18n.so.5.105.0 /usr/lib64/libQt5Concurrent.so.5.15.8 /usr/lib64/libQt5Network.so.5.15.8 /usr/lib64/libQt5Xml.so.5.15.8 /usr/lib64/libKF5AuthCore.so.5.105.0 /usr/lib64/libKF5CoreAddons.so.5.105.0 /usr/lib64/libQt5DBus.so.5.15.8 /usr/lib64/libQt5XkbCommonSupport.a /usr/lib64//libQt5Gui.so /usr/lib64//libQt5Core.so /usr/lib64/libxkbcommon.so /usr/lib64/libGL.so /usr/lib64/libQt5Gui.so.5.15.8 /usr/lib64/libQt5Core.so.5.15.8`

    /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/src/CMakeFiles/xdg-desktop-portal-kde.dir/xdgshortcut.cpp.o

The point being: the same failure now occurs with far fewer arguments because [cvise-delta] reduced the list down to those responsible.

Now just keep aside:

-   The files [xdgshortcut.cpp.o] and [libKirigamiFilepicker.a]
-   the [g++] command-line to use

\
Perfect! There now is a lean work basis. Next step: debug the compiler.

#### [Debugging the compiler]

** Tip**\
it is highly suggested to rebuild GCC and glibc with debugging symbols. See the first section for detailed instruction on how to do this.

Invoke [GDB] by passing the whole problematic command-line after `--args`:

`root `[`#`]`gdb --quiet --args /usr/bin/x86_64-pc-linux-gnu-g++ -O3 -pipe -march=native -fomit-frame-pointer -fopt-info-vec -fcf-protection=return -flto=auto -ffat-lto-objects -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -fdiagnostics-color=always -Wl,--enable-new-dtags -flto=auto -pthread @bad -o /dev/null /usr/lib64/libKF5Declarative.so.5.105.0 /usr/lib64/libKF5Notifications.so.5.105.0 /usr/lib64/libKF5WaylandClient.so.5.105.0 /var/tmp/portage/kde-plasma/xdg-desktop-portal-kde-5.27.4.1-r1/work/xdg-desktop-portal-kde-5.27.4.1_build/lib/libKirigamiFilepicker.a /usr/lib64/libwayland-client.so /usr/lib64/libQt5QuickWidgets.so.5.15.8 /usr/lib64/libKF5Package.so.5.105.0 /usr/lib64/libKF5KIOFileWidgets.so.5.105.0 /usr/lib64/libKF5KIOWidgets.so.5.105.0 /usr/lib64/libKF5KIOGui.so.5.105.0 /usr/lib64/libKF5WindowSystem.so.5.105.0 /usr/lib64/libX11.so /usr/lib64/libKF5JobWidgets.so.5.105.0 /usr/lib64/libKF5Completion.so.5.105.0 /usr/lib64/libKF5Bookmarks.so.5.105.0 /usr/lib64/libKF5XmlGui.so.5.105.0 /usr/lib64/libKF5GlobalAccel.so.5.105.0 /usr/lib64/libKF5IconThemes.so.5.105.0 /usr/lib64/libQt5PrintSupport.so.5.15.8 /usr/lib64/libKF5ItemViews.so.5.105.0 /usr/lib64/libKF5ConfigWidgets.so.5.105.0 /usr/lib64/libKF5GuiAddons.so.5.105.0 /usr/lib64/libQt5WaylandClient.so.5.15.8 /usr/lib64/libKF5WidgetsAddons.so.5.105.0 /usr/lib64/libKF5ConfigGui.so.5.105.0 /usr/lib64/libKF5Codecs.so.5.105.0 /usr/lib64/libKF5Auth.so.5.105.0 /usr/lib64/libQt5Widgets.so.5.15.8 /usr/lib64/libKF5Solid.so.5.105.0 /usr/lib64/libQt5Quick.so.5.15.8 /usr/lib64/libQt5QmlModels.so.5.15.8 /usr/lib64/libQt5Qml.so.5.15.8 /usr/lib64/libKF5KIOCore.so.5.105.0 /usr/lib64/libKF5Service.so.5.105.0 /usr/lib64/libKF5ConfigCore.so.5.105.0 /usr/lib64/libKF5I18n.so.5.105.0 /usr/lib64/libQt5Concurrent.so.5.15.8 /usr/lib64/libQt5Network.so.5.15.8 /usr/lib64/libQt5Xml.so.5.15.8 /usr/lib64/libKF5AuthCore.so.5.105.0 /usr/lib64/libKF5CoreAddons.so.5.105.0 /usr/lib64/libQt5DBus.so.5.15.8 /usr/lib64/libQt5XkbCommonSupport.a /usr/lib64//libQt5Gui.so /usr/lib64//libQt5Core.so /usr/lib64/libxkbcommon.so /usr/lib64/libGL.so /usr/lib64/libQt5Gui.so.5.15.8 /usr/lib64/libQt5Core.so.5.15.8`

    Reading symbols from /usr/bin/x86_64-pc-linux-gnu-g++...
    Reading symbols from /usr/lib/debug//usr/x86_64-pc-linux-gnu/gcc-bin/13/x86_64-pc-linux-gnu-g++.debug...
    (gdb)

Set the variable `follow-fork-mode` to `child` ([set follow-fork-mode child]).

** Warning**\
To be continued

## [See also]

-   [C-Vise](https://wiki.gentoo.org/wiki/C-Vise "C-Vise") --- a super-parallel Python port of the C-Reduce. The port is fully compatible to the C-Reduce and uses the same efficient LLVM-based C/C++ reduction tool named clang_delta.
-   [Bisecting_with_live_ebuilds#GCC_example](https://wiki.gentoo.org/wiki/Bisecting_with_live_ebuilds#GCC_example "Bisecting with live ebuilds")
-   [Bugzilla/Bug_report_guide](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") --- explains how to report bugs using Gentoo\'s Bugzilla instance, which may be lightly customized to collect specific details for each Gentoo project area
-   [Bugzilla/Guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide") --- covers the recommended method of forensically reporting *specific details* of bugs within Gentoo.

## [External resources]

-   [GCC - How to Minimize Test Cases for Bugs](https://gcc.gnu.org/bugs/minimize.html)
-   [GCC wiki - A Guide to Testcase Reduction](https://gcc.gnu.org/wiki/A_guide_to_testcase_reduction)
-   [GCC wiki - Finding miscompilations on large testcases](https://gcc.gnu.org/wiki/Analysing_Large_Testcases)
-   [Reducing an LTO Linux kernel bug with cvise](https://nathanchance.dev/posts/cvise-lto-kernel-bug/)
-   [Bug with an example of needing timeouts and such in cvise script](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=109531)