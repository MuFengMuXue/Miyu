**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Debugging "wikipedia:Debugging")

This article provides general advice on how to enable **debugging** symbols and information.

** Note**\
Debugging symbols are unrelated to `USE=debug`! This USE flag is usually for enabling assertions and other debug code paths within packages, it\'s very possible that they will result in failures even when everything works fine.

## Contents

-   [[1] [Installing debugging information for packages]](#Installing_debugging_information_for_packages)
    -   [[1.1] [Per-package]](#Per-package)
        -   [[1.1.1] [Setup]](#Setup)
        -   [[1.1.2] [Example of it working]](#Example_of_it_working)
    -   [[1.2] [Don\'t strip symbols globally]](#Don.27t_strip_symbols_globally)
    -   [[1.3] [Troubleshooting]](#Troubleshooting)
-   [[2] [Compression]](#Compression)
-   [[3] [Valgrind]](#Valgrind)
-   [[4] [Eclass debugging]](#Eclass_debugging)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installing debugging information for packages]

Debug information is stripped by default to save space. This article explains how to enable it either selectively (preferred) or globally (expensive).

** Note**\
Files will be larger with debug symbols:

[CODE] **Comparison of Filesizes**

    ## (debug symbols stripped)
    3140 bytes
    ## (debug symbols enabled)
    6374 bytes
    ## (-ggdb flag enabled)
    19552 bytes

### [Per-package]

Portage has several related feature flags:

-   To install debugging information, use the `splitdebug` feature.
-   To install the source code, activate the `installsources` feature, which requires [[[dev-util/debugedit]](https://packages.gentoo.org/packages/dev-util/debugedit)[]].

These features are integrated to provide an environment where [[[dev-debug/gdb]](https://packages.gentoo.org/packages/dev-debug/gdb)[]] can find both the debugging information and the sources, allowing full use of its interactive debugging functionality.

If `nostrip` is in the default [FEATURES](https://wiki.gentoo.org/wiki/FEATURES "FEATURES"), `splitdebug` won\'t do anything, so disable it when using splitdebug.

#### [Setup]

Create two files in [/etc/portage/env]:

[FILE] **[`/etc/portage/env/debugsyms`](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")**

    CFLAGS="$ -ggdb3"
    CXXFLAGS="$ -ggdb3"
    LDFLAGS="$ -ggdb3"
    # nostrip is disabled here because it negates splitdebug
    FEATURES="$ splitdebug compressdebug -nostrip"

[FILE] **[`/etc/portage/env/installsources`](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")**

    FEATURES="$ installsources"

`root `[`#`]`emerge --ask dev-util/debugedit dev-debug/gdb`

Then configure packages as required to use the newly-created environment (env) snippets above, depending on whether the source code and/or debugging symbols are needed:

[FILE] **[`/etc/portage/package.env`](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")**

    # Example package where you only want debug symbols
    category/some-package debugsyms
    # Example package where you want debug symbols and nice source lines in the debugger
    # If in doubt, choose this one!
    category/some-library debugsyms installsources

Now rebuild the package(s) that were configured in [/etc/portage/package.env] to get debug symbols:

`root `[`#`]`emerge --ask --oneshot category/some-package category/some-library`

#### [Example of it working]

Now, when debugging a program with gdb, it will find the sources and debugging information.

[CODE] **Example gdb session for debugging [[[dev-util/radare2]](https://packages.gentoo.org/packages/dev-util/radare2)[]]**

    % gdb --args r2 /bin/ls
    Reading symbols from r2...Reading symbols from /usr/lib64/debug//usr/bin/radare2.debug...done.
    done.
    = gdb>> break main
    Breakpoint 1 at 0x2e70: file radare2.c, line 372.
    = gdb>> run
    Starting program: /usr/bin/r2 /bin/ls

    Breakpoint 1, main (argc=2, argv=0x7fffffffdd98, envp=0x7fffffffddb0) at radare2.c:372
    372    int main(int argc, char **argv, char **envp) Keep all ELF symbols in each binary**

    # Warning: if doing this system wide, a lower level of debug information like -g may be more appropriate
    # to save memory during builds and disk space.
    CFLAGS="$ -ggdb3"
    CXXFLAGS="$ -ggdb3"
    LDFLAGS="$ -ggdb3"
    FEATURES="nostrip"

### [Troubleshooting]

1.  If [/usr/src] doesn\'t appear, check for any errors in build log.

## [Compression]

`FEATURES="compressdebug"` enables compression of debug symbols in Portage. This may make loading debug info in gdb and such a bit slower but is worth it for most where the disk space saving is valuable. The default compression algorithm is zlib.

Newer versions of the toolchain can use [zstd if configured](https://wiki.gentoo.org/wiki/Zstd#Debug_symbols "Zstd") for a better compression ratio.

[[[sys-devel/dwz]](https://packages.gentoo.org/packages/sys-devel/dwz)[]] can also be used to optimize debugging info size with \>=sys-apps/portage-3.0.62 with `FEATURES="dedupdebug"`.

## [Valgrind]

See [Valgrind](https://wiki.gentoo.org/wiki/Valgrind "Valgrind"), a dynamic analysis tool which detects memory errors and memory leaks.

## [Eclass debugging]

To enable eclass debugging, set the following in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    ECLASS_DEBUG_OUTPUT=on

## [See also]

-   [GDB](https://wiki.gentoo.org/wiki/GDB "GDB") --- used to investigate runtime errors that normally involve memory corruption
-   [AddressSanitizer](https://wiki.gentoo.org/wiki/AddressSanitizer "AddressSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect several memory access errors.
-   [UndefinedBehaviorSanitizer](https://wiki.gentoo.org/wiki/UndefinedBehaviorSanitizer "UndefinedBehaviorSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect various forms of undefined behaviour (UB).
-   [Valgrind](https://wiki.gentoo.org/wiki/Valgrind "Valgrind") --- dynamic analysis tool which detects memory errors and memory leaks.
-   [Stack smashing debugging guide](https://wiki.gentoo.org/wiki/Stack_smashing_debugging_guide "Stack smashing debugging guide") --- a step-by-step guide to debug stack smashing violations
-   [Debuginfod](https://wiki.gentoo.org/wiki/Debuginfod "Debuginfod")
-   [Project:Quality Assurance/Backtraces 1.4 debug USE flag](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces#debug_USE_flag "Project:Quality Assurance/Backtraces")

## [External resources]

-   [Debugging binaries invoked from scripts with GDB](https://developers.redhat.com/articles/2022/12/27/debugging-binaries-invoked-scripts-gdb)
-   [libtool: Debugging executables](https://www.gnu.org/software/libtool/manual/html_node/Debugging-executables.html)