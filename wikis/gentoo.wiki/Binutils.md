**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain")][Project](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain")

[[]][Home](https://www.gnu.org/software/binutils/)

[[]][Official documentation](https://sourceware.org/binutils/docs/)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/binutils)

[[]][Wikipedia](https://en.wikipedia.org/wiki/binutils "wikipedia:binutils")

[[]][GitWeb](https://sourceware.org/git/binutils-gdb.git)

[[]][Sourcehut](https://sr.ht/~sourceware/binutils-gdb)

[[]][Official project wiki](https://sourceware.org/binutils/wiki/)

[[]][Bugs (upstream)](https://sourceware.org/bugzilla/)

**Binutils** is a set of tools for creating and manipulating certain types of [binary files](https://en.wikipedia.org/wiki/binary_files "wikipedia:binary files"). They can work on [executable files](https://en.wikipedia.org/wiki/executable_files "wikipedia:executable files"), [libraries](https://en.wikipedia.org/wiki/Library_(computing) "wikipedia:Library (computing)"), [object files](https://en.wikipedia.org/wiki/object_files "wikipedia:object files"), [assembly code](https://en.wikipedia.org/wiki/assembly_code "wikipedia:assembly code"), etc.

Binutils contains commands such as the [ld] linker, [as] assembler, or the [strip] tool for removing debug symbols.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Select a newer version]](#Select_a_newer_version)
        -   [[2.1.1] [eselect module]](#eselect_module)
        -   [[2.1.2] [Built-in binutils-config utility]](#Built-in_binutils-config_utility)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [ld]](#ld)
    -   [[3.2] [as]](#as)
    -   [[3.3] [addr2line]](#addr2line)
    -   [[3.4] [ar]](#ar)
        -   [[3.4.1] [Creating an archive]](#Creating_an_archive)
        -   [[3.4.2] [Printing contents of an archive]](#Printing_contents_of_an_archive)
        -   [[3.4.3] [Extracting an archive]](#Extracting_an_archive)
        -   [[3.4.4] [Delete a file from an archive]](#Delete_a_file_from_an_archive)
    -   [[3.5] [c++filt]](#c.2B.2Bfilt)
    -   [[3.6] [elfedit]](#elfedit)
    -   [[3.7] [gprof]](#gprof)
    -   [[3.8] [gprofng]](#gprofng)
    -   [[3.9] [nm]](#nm)
    -   [[3.10] [objcopy]](#objcopy)
    -   [[3.11] [objdump]](#objdump)
    -   [[3.12] [ranlib]](#ranlib)
    -   [[3.13] [readelf]](#readelf)
    -   [[3.14] [size]](#size)
    -   [[3.15] [strings]](#strings)
    -   [[3.16] [strip]](#strip)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Preserved-rebuild loop]](#Preserved-rebuild_loop)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-devel/binutils](https://packages.gentoo.org/packages/sys-devel/binutils) [[]] [Tools necessary to build programs]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  [`+debuginfod`](https://packages.gentoo.org/useflags/+debuginfod)     Enable debuginfod support via dev-libs/elfutils libdebuginfod
  [`+gold`](https://packages.gentoo.org/useflags/+gold)                 Build ld.gold linker
  [`+nls`](https://packages.gentoo.org/useflags/+nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`+plugins`](https://packages.gentoo.org/useflags/+plugins)           Enable plugin support in tools
  [`cet`](https://packages.gentoo.org/useflags/cet)                     Enable Intel Control-flow Enforcement Technology.
  [`default-gold`](https://packages.gentoo.org/useflags/default-gold)   Set ld to point to ld.gold instead of ld.bfd
  [`doc`](https://packages.gentoo.org/useflags/doc)                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gprofng`](https://packages.gentoo.org/useflags/gprofng)             Enable the next-generation gprofng profiler
  [`hardened`](https://packages.gentoo.org/useflags/hardened)           Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`multitarget`](https://packages.gentoo.org/useflags/multitarget)     Adds support to binutils for cross compiling (does not work with gas)
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                     Build binutils with Profile Guided Optimization (PGO) and LTO
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)     Build static versions of dynamic libraries as well
  [`test`](https://packages.gentoo.org/useflags/test)                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)             Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`xxhash`](https://packages.gentoo.org/useflags/xxhash)               Use dev-libs/xxhash for \--build-id=xx support
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                   Enable support for ZSTD compression
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-15 22:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Binutils is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so it should always be installed.

In case needed, such as after changing [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"):

`root `[`#`]`emerge --ask --oneshot sys-devel/binutils`

## [Configuration]

### [Select a newer version]

#### [eselect module]

System administrators can use the [eselect binutils] command to select an alternate version of binutils. This is not normally necessary, since more than one version of the binutils is not installed by default, however it may be necessitated by packages upgrades.

#### [Built-in binutils-config utility]

Selecting an alternate version of binutils can be done using the [binutils-config] command. First list known (installed) versions:

`root `[`#`]`binutils-config --list-profiles`

     [1] x86_64-pc-linux-gnu-2.25.1 *
     [2] x86_64-pc-linux-gnu-2.26.1

Select the newest profile. Either the integer number or the full profile name can be used to select the profile; below the profile name is used:

`root `[`#`]`binutils-config x86_64-pc-linux-gnu-2.26.1`

     * Switching to x86_64-pc-linux-gnu-2.26.1 ...                                                                                   [ ok ]

     * Please remember to run:

     *   # . /etc/profile

## [Usage]

See the [upstream documentation](https://sourceware.org/binutils/docs/) for the appropriate man page for more detailed documentation on each utility.

** Note**\
The following C file will be referenced throughout the article.

[FILE] **`example.c`**

    #include <stdio.h>

    int main(void)

### [ld]

The default linker provided by binutils which is also commonly referred to as \"BFD\", or \"Binary File Descriptor.\" Most users will never need to directly interact with [ld], as [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") invokes it during the compilation process. An example can be seen below.

The `-c` flag here tells GCC to only compile and assemble, and to not proceed with the linking process.

`user `[`$`]`gcc -c example.c`

This command can be broken down as:

-   `-o example` - the output file name
-   `/lib64/crt1.o` - provides the `_start` entry point and various other preparations before executing [main()]
-   `example.o` - the object file provided by GCC earlier
-   `-lc` - tells the linker to link to libc
-   `--dynamic-linker /lib64/ld-linux-x86-64.so.2` - informs [ld] of which dynamic linker to use

`user `[`$`]`ld -o example /lib64/crt1.o example.o -lc --dynamic-linker /lib64/ld-linux-x86-64.so.2`

`user `[`$`]`./example`

    Hello, World!

### [as]

** Note**\
This section will re-use the example C file from the [ld](https://wiki.gentoo.org/wiki/Binutils#ld "Binutils") section.

First, generate the assembly file from the example C file:

`user `[`$`]`gcc -S example.c`

Next, generate the object file with [as]:

`user `[`$`]`as -o example.o example.s`

### [addr2line]

[addr2line] is a debugging tool that can be utilized to inform a developer how a memory address in an executable file correlates to a line number in the original C file.

Firstly, compile the example C file with the flag, `-g` to embed debugging information.

Next, utilize [objdump] to find the memory address that [main()] starts at:

`user `[`$`]`objdump -d a.out | grep -A10 "<main>:"`

    0000000000001179 <main>:
        1179:   f3 0f 1e fa             endbr64
        117d:   55                      push   %rbp
        117e:   48 89 e5                mov    %rsp,%rbp
        1181:   48 8d 05 7c 0e 00 00    lea    0xe7c(%rip),%rax        # 2004 <_IO_stdin_used+0x4>
        1188:   48 89 c7                mov    %rax,%rdi
        118b:   e8 c0 fe ff ff          call   1050
        1190:   b8 00 00 00 00          mov    $0x0,%eax
        1195:   5d                      pop    %rbp
        1196:   c3                      ret

Next, use [addr2line] to find where the address `1179` starts in the example file:

`user `[`$`]`addr2line -e a.out 1179`

    /home/larry/example.c:3

### [ar]

[ar] is an archive manipulation program.

#### [Creating an archive]

This section will create some test files:

`user `[`$`]`for x in ; do touch $x; echo "some random data for $x" > $x; done`

To create an archive:

`user `[`$`]`ar r example.a 1 2 3 4`

    ar: creating example.a

-   `r` means to replace or insert new files into the archive

#### [Printing contents of an archive]

To print the contents of an archive, use `p`:

`user `[`$`]`ar p example.a`

    some random data for 1
    some random data for 2
    some random data for 3
    some random data for 4

To see the filename associated with the contents, add the `v` flag:

`user `[`$`]`ar pv example.a`

    <1>

    some random data for 1

    <2>

    some random data for 2

    <3>

    some random data for 3

    <4>

    some random data for 4

#### [Extracting an archive]

To extract an archive\'s contents, use `x`:

`user `[`$`]`ar x example.a`

#### [Delete a file from an archive]

To delete a file from an archive, use `d`:

`user `[`$`]`ar d example.a 3`

`user `[`$`]`ar p example.a`

    some random data for 1
    some random data for 2
    some random data for 4

### [][c++filt]

[c++filt] allows for developers to de-mangle C++ function names. The following example demangles a main function:

`user `[`$`]`c++filt _Z4mainiPPc`

    main(int, char**)

### [elfedit]

**elfedit** updates ELF header and properties.

To remove the x86 feature `shstk` from an ELF and verify with [readelf]:

`user `[`$`]`elfedit --disable-x86-feature=shstk a.out`

`user `[`$`]`readelf -n a.out`

    Displaying notes found in: .note.gnu.property
      Owner                Data size    Description
      GNU                  0x00000040   NT_GNU_PROPERTY_TYPE_0
          Properties: x86 feature: IBT
        x86 ISA needed: x86-64-baseline, x86-64-v2, x86-64-v3, x86-64-v4
        x86 feature used: x86
        x86 ISA used: x86-64-baseline

    ...

### [gprof]

`user `[`$`]`gprof --help`

    Usage: gprof [-[abcDhilLrsTvwxyz]] [-[ABCeEfFJnNOpPqQRStZ][name]] [-I dirs]
        [-d[num]] [-k from/to] [-m min-count] [-t table-length]
        [--[no-]annotated-source[=name]] [--[no-]exec-counts[=name]]
        [--[no-]flat-profile[=name]] [--[no-]graph[=name]]
        [--[no-]time=name] [--all-lines] [--brief] [--debug[=level]]
        [--function-ordering] [--file-ordering] [--inline-file-names]
        [--directory-path=dirs] [--display-unused-functions]
        [--file-format=name] [--file-info] [--help] [--line] [--min-count=n]
        [--no-static] [--print-path] [--separate-files]
        [--static-call-graph] [--sum] [--table-length=len] [--traditional]
        [--version] [--width=n] [--ignore-non-functions]
        [--demangle[=STYLE]] [--no-demangle] [--external-symbol-table=name] [@FILE]
        [image-file] [profile-file...]
    Report bugs to <https://bugs.gentoo.org/>

### [gprofng]

`user `[`$`]`gprofng --help`

    Usage: gprofng [OPTION(S)] COMMAND [KEYWORD] [ARGUMENTS]

    This is the driver for the GPROFNG tools suite to gather and analyze performance data.

    Options:

     --version           print the version number and exit.
     --help              print usage information and exit.
     --check             verify if the hardware and software environment is supported.
     --verbose   enable (on) or disable (off) verbose mode; the default is "off".

    Commands:

    The driver supports various commands. These are listed below.

    It is also possible to invoke the lower level commands directly, but since these
    are subject to change, in particular the options, we recommend to use the driver.

    The man pages for the commands below can be viewed using the command name with
    "gprofng" replaced by "gp" and the spaces replaced by a dash ("-"). For
    example the man page name for "gprofng collect app" is "gprofng-collect-app".

    The following combination of commands and keywords are supported:

    Collect performance data

     gprofng collect app     collect application performance data.

    Display the performance results

     gprofng display text    display the performance data in ASCII format.
     gprofng display html    generate an HTML file from one or more experiments.
     gprofng display src     display source or disassembly with compiler annotations.

    Miscellaneous commands

     gprofng archive         include binaries and source code in an experiment directory.

    Environment:

    The following environment variables are supported:

     GPROFNG_MAX_CALL_STACK_DEPTH  set the depth of the call stack (default is 256).

     GPROFNG_USE_JAVA_OPTIONS      may be set when profiling a C/C++ application
                                   that uses dlopen() to execute Java code.

     GPROFNG_SSH_REMOTE_DISPLAY    use this variable to define the ssh command
                                   executed by the remote display tool.

     GPROFNG_SKIP_VALIDATION       set this variable to disable checking hardware,
                                   system, and Java versions.

     GPROFNG_ALLOW_CORE_DUMP       set this variable to allow a core file to be
                                   generated; otherwise an error report is created on /tmp.

     GPROFNG_ARCHIVE               use this variable to define the settings for automatic
                                   archiving upon experiment recording completion.

     GPROFNG_ARCHIVE_COMMON_DIR    set this variable to the location of the common archive.

     GPROFNG_JAVA_MAX_CALL_STACK_DEPTH  set the depth of the Java call stack; the default
                                        is 256; set to 0 to disable capturing of call stacks.

     GPROFNG_JAVA_NATIVE_MAX_CALL_STACK_DEPTH  set the depth of the Java native call stack;
                                               the default is 256; set to 0 to disable capturing
                                               of call stacks (JNI and assembly call stacks
                                               are not captured).

    Documentation:

    A getting started guide for gprofng is maintained as a Texinfo manual. If the info and
    gprofng programs are properly installed at your site, the command "info gprofng"
    should give you access to this document.

    See also:

    gprofng-archive(1), gprofng-collect-app(1), gprofng-display-html(1), gprofng-display-src(1), gprofng-display-text(1)

    Report bugs to <https://sourceware.org/bugzilla/>

### [nm]

`user `[`$`]`nm --help`

    Usage: nm [option(s)] [file(s)]
     List symbols in [file(s)] (a.out by default).
     The options are:
      -a, --debug-syms       Display debugger-only symbols
      -A, --print-file-name  Print name of the input file before every symbol
      -B                     Same as --format=bsd
      -C, --demangle[=STYLE] Decode mangled/processed symbol names
                               STYLE can be "none", "auto", "gnu-v3", "java",
                               "gnat", "dlang", "rust"
          --no-demangle      Do not demangle low-level symbol names
          --recurse-limit    Enable a demangling recursion limit.  (default)
          --no-recurse-limit Disable a demangling recursion limit.
      -D, --dynamic          Display dynamic symbols instead of normal symbols
      -e                     (ignored)
      -f, --format=FORMAT    Use the output format FORMAT.  FORMAT can be `bsd',
                               `sysv', `posix' or 'just-symbols'.
                               The default is `bsd'
      -g, --extern-only      Display only external symbols
        --ifunc-chars=CHARS  Characters to use when displaying ifunc symbols
      -j, --just-symbols     Same as --format=just-symbols
      -l, --line-numbers     Use debugging information to find a filename and
                               line number for each symbol
      -n, --numeric-sort     Sort symbols numerically by address
      -o                     Same as -A
      -p, --no-sort          Do not sort the symbols
      -P, --portability      Same as --format=posix
      -r, --reverse-sort     Reverse the sense of the sort
          --plugin NAME      Load the specified plugin
      -S, --print-size       Print size of defined symbols
      -s, --print-armap      Include index for symbols from archive members
          --quiet            Suppress "no symbols" diagnostic
          --size-sort        Sort symbols by size
          --special-syms     Include special symbols in the output
          --synthetic        Display synthetic symbols as well
      -t, --radix=RADIX      Use RADIX for printing symbol values
          --target=BFDNAME   Specify the target object format as BFDNAME
      -u, --undefined-only   Display only undefined symbols
      -U, --defined-only     Display only defined symbols
          --unicode=
                             Specify how to treat UTF-8 encoded unicode characters
      -W, --no-weak          Ignore weak symbols
          --without-symbol-versions  Do not display version strings after symbol names
      -X 32_64               (ignored)
      @FILE                  Read options from FILE
      -h, --help             Display this information
      -V, --version          Display this program's version number
    nm: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex plugin
    Report bugs to <https://bugs.gentoo.org/>.

### [objcopy]

`user `[`$`]`objcopy --help`

    Usage: objcopy [option(s)] in-file [out-file]
     Copies a binary file, possibly transforming it in the process
     The options are:
      -I --input-target <bfdname>      Assume input file is in format <bfdname>
      -O --output-target <bfdname>     Create an output file in format <bfdname>
      -B --binary-architecture <arch>  Set output arch, when input is arch-less
      -F --target <bfdname>            Set both input and output format to <bfdname>
         --debugging                   Convert debugging information, if possible
      -p --preserve-dates              Copy modified/access timestamps to the output
      -D --enable-deterministic-archives
                                       Produce deterministic output when stripping archives
      -U --disable-deterministic-archives
                                       Disable -D behavior (default)
      -j --only-section <name>         Only copy section <name> into the output
         --add-gnu-debuglink=<file>    Add section .gnu_debuglink linking to <file>
      -R --remove-section <name>       Remove section <name> from the output
         --remove-relocations <name>   Remove relocations from section <name>
         --strip-section-headers              Strip section header from the output
      -S --strip-all                   Remove all symbol and relocation information
      -g --strip-debug                 Remove all debugging symbols & sections
         --strip-dwo                   Remove all DWO sections
         --strip-unneeded              Remove all symbols not needed by relocations
      -N --strip-symbol <name>         Do not copy symbol <name>
         --strip-unneeded-symbol <name>
                                       Do not copy symbol <name> unless needed by
                                         relocations
         --only-keep-debug             Strip everything but the debug information
         --extract-dwo                 Copy only DWO sections
         --extract-symbol              Remove section contents but keep symbols
         --keep-section <name>         Do not strip section <name>
      -K --keep-symbol <name>          Do not strip symbol <name>
         --keep-section-symbols        Do not strip section symbols
         --keep-file-symbols           Do not strip file symbol(s)
         --localize-hidden             Turn all ELF hidden symbols into locals
      -L --localize-symbol <name>      Force symbol <name> to be marked as a local
         --globalize-symbol <name>     Force symbol <name> to be marked as a global
      -G --keep-global-symbol <name>   Localize all symbols except <name>
      -W --weaken-symbol <name>        Force symbol <name> to be marked as a weak
         --weaken                      Force all global symbols to be marked as weak
      -w --wildcard                    Permit wildcard in symbol comparison
      -x --discard-all                 Remove all non-global symbols
      -X --discard-locals              Remove any compiler-generated symbols
      -i --interleave[=<number>]       Only copy N out of every <number> bytes
         --interleave-width <number>   Set N for --interleave
      -b --byte <num>                  Select byte <num> in every interleaved block
         --gap-fill <val>              Fill gaps between sections with <val>
         --pad-to <addr>               Pad the last section up to address <addr>
         --set-start <addr>            Set the start address to <addr>
         <incr>
                                       Add <incr> to the start address
         <incr>
                                       Add <incr> to LMA, VMA and start addresses
         <name><val>
                                       Change LMA and VMA of section <name> by <val>
         --change-section-lma <name><val>
                                       Change the LMA of section <name> by <val>
         --change-section-vma <name><val>
                                       Change the VMA of section <name> by <val>

                                       Warn if a named section does not exist
         --set-section-flags <name>=<flags>
                                       Set section <name>'s properties to <flags>
         --set-section-alignment <name>=<align>
                                       Set section <name>'s alignment to <align> bytes
         --add-section <name>=<file>   Add section <name> found in <file> to output
         --update-section <name>=<file>
                                       Update contents of section <name> with
                                       contents found in <file>
         --dump-section <name>=<file>  Dump the contents of section <name> into <file>
         --rename-section <old>=<new>[,<flags>] Rename section <old> to <new>
         --long-section-names
                                       Handle long section names in Coff objects.
         --change-leading-char         Force output format's leading character style
         --remove-leading-char         Remove leading character from global symbols
         --reverse-bytes=<num>         Reverse <num> bytes at a time, in output sections with content
         --redefine-sym <old>=<new>    Redefine symbol name <old> to <new>
         --redefine-syms <file>        --redefine-sym for all symbol pairs
                                         listed in <file>
         --srec-len <number>           Restrict the length of generated Srecords
         --srec-forceS3                Restrict the type of generated Srecords to S3
         --strip-symbols <file>        -N for all symbols listed in <file>
         --strip-unneeded-symbols <file>
                                       --strip-unneeded-symbol for all symbols listed
                                         in <file>
         --keep-symbols <file>         -K for all symbols listed in <file>
         --localize-symbols <file>     -L for all symbols listed in <file>
         --globalize-symbols <file>    --globalize-symbol for all in <file>
         --keep-global-symbols <file>  -G for all symbols listed in <file>
         --weaken-symbols <file>       -W for all symbols listed in <file>
         --add-symbol <name>=[<section>:]<value>[,<flags>]  Add a symbol
         --alt-machine-code <index>    Use the target's <index>'th alternative machine
         --writable-text               Mark the output text as writable
         --readonly-text               Make the output text write protected
         --pure                        Mark the output file as demand paged
         --impure                      Mark the output file as impure
         --prefix-symbols      Add  to start of every symbol name
         --prefix-sections     Add  to start of every section name
         --prefix-alloc-sections
                                       Add  to start of every allocatable
                                         section name
         --file-alignment <num>        Set PE file alignment to <num>
         --heap <reserve>[,<commit>]   Set PE reserve/commit heap to <reserve>/
                                       <commit>
         --image-base <address>        Set PE image base to <address>
         --section-alignment <num>     Set PE section alignment to <num>
         --stack <reserve>[,<commit>]  Set PE reserve/commit stack to <reserve>/
                                       <commit>
         --subsystem <name>[:<version>]
                                       Set PE subsystem to <name> [& <version>]
         --compress-debug-sections[=]
                       Compress DWARF debug sections
         --decompress-debug-sections   Decompress DWARF debug sections using zlib
         --elf-stt-common=[yes|no]     Generate ELF common symbols with STT_COMMON
                                         type
         --verilog-data-width <number> Specifies data width, in bytes, for verilog output
      -M  --merge-notes                Remove redundant entries in note sections
          --no-merge-notes             Do not attempt to remove redundant notes (default)
      -v --verbose                     List all object files modified
      @<file>                          Read options from <file>
      -V --version                     Display this program's version number
      -h --help                        Display this output
         --info                        List object formats & architectures supported
    objcopy: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex plugin
    Report bugs to <https://bugs.gentoo.org/>

### [objdump]

`user `[`$`]`objdump --help`

    Usage: objdump <option(s)> <file(s)>
     Display information from object <file(s)>.
     At least one of the following switches must be given:
      -a, --archive-headers    Display archive header information
      -f, --file-headers       Display the contents of the overall file header
      -p, --private-headers    Display object format specific file header contents
      -P, --private=OPT,OPT... Display object format specific contents
      -h, --[section-]headers  Display the contents of the section headers
      -x, --all-headers        Display the contents of all headers
      -d, --disassemble        Display assembler contents of executable sections
      -D, --disassemble-all    Display assembler contents of all sections
          --disassemble=<sym>  Display assembler contents from <sym>
      -S, --source             Intermix source code with disassembly
          --source-comment[=<txt>] Prefix lines of source code with <txt>
      -s, --full-contents      Display the full contents of all sections requested
      -Z, --decompress         Decompress section(s) before displaying their contents
      -g, --debugging          Display debug information in object file
      -e, --debugging-tags     Display debug information using ctags style
      -G, --stabs              Display (in raw form) any STABS info in the file
      -W, --dwarf[a/=abbrev, A/=addr, r/=aranges, c/=cu_index, L/=decodedline,
                  f/=frames, F/=frames-interp, g/=gdb_index, i/=info, o/=loc,
                  m/=macro, p/=pubnames, t/=pubtypes, R/=Ranges, l/=rawline,
                  s/=str, O/=str-offsets, u/=trace_abbrev, T/=trace_aranges,
                  U/=trace_info]
                               Display the contents of DWARF debug sections
      -Wk,--dwarf=links        Display the contents of sections that link to
                                separate debuginfo files
      -WK,--dwarf=follow-links
                               Follow links to separate debug info files (default)
      -WN,--dwarf=no-follow-links
                               Do not follow links to separate debug info files
      -L, --process-links      Display the contents of non-debug sections in
                                separate debuginfo files.  (Implies -WK)
          --ctf[=SECTION]      Display CTF info from SECTION, (default `.ctf')
          --sframe[=SECTION]   Display SFrame info from SECTION, (default '.sframe')
      -t, --syms               Display the contents of the symbol table(s)
      -T, --dynamic-syms       Display the contents of the dynamic symbol table
      -r, --reloc              Display the relocation entries in the file
      -R, --dynamic-reloc      Display the dynamic relocation entries in the file
      @<file>                  Read options from <file>
      -v, --version            Display this program's version number
      -i, --info               List object formats and architectures supported
      -H, --help               Display this information

     The following switches are optional:
      -b, --target=BFDNAME           Specify the target object format as BFDNAME
      -m, --architecture=MACHINE     Specify the target architecture as MACHINE
      -j, --section=NAME             Only display information for section NAME
      -M, --disassembler-options=OPT Pass text OPT on to the disassembler
      -EB --endian=big               Assume big endian format when disassembling
      -EL --endian=little            Assume little endian format when disassembling
          --file-start-context       Include context from start of file (with -S)
      -I, --include=DIR              Add DIR to search list for source files
      -l, --line-numbers             Include line numbers and filenames in output
      -F, --file-offsets             Include file offsets when displaying information
      -C, --demangle[=STYLE]         Decode mangled/processed symbol names
                                       STYLE can be "none", "auto", "gnu-v3",
                                       "java", "gnat", "dlang", "rust"
          --recurse-limit            Enable a limit on recursion whilst demangling
                                      (default)
          --no-recurse-limit         Disable a limit on recursion whilst demangling
      -w, --wide                     Format output for more than 80 columns
      -U[d|l|i|x|e|h]                Controls the display of UTF-8 unicode characters
      --unicode=[default|locale|invalid|hex|escape|highlight]
      -z, --disassemble-zeroes       Do not skip blocks of zeroes when disassembling
          --start-address=ADDR       Only process data whose address is >= ADDR
          --stop-address=ADDR        Only process data whose address is < ADDR
          --no-addresses             Do not print address alongside disassembly
          --prefix-addresses         Print complete address alongside disassembly
          --[no-]show-raw-insn       Display hex alongside symbolic disassembly
          --insn-width=WIDTH         Display WIDTH bytes on a single line for -d
          --adjust-vma=OFFSET        Add OFFSET to all displayed section addresses
          --show-all-symbols         When disassembling, display all symbols at a given address
          --special-syms             Include special symbols in symbol dumps
          --inlines                  Print all inlines for source line (with -l)
          --prefix=PREFIX            Add PREFIX to absolute paths for -S
          --prefix-strip=LEVEL       Strip initial directory names for -S
          --dwarf-depth=N            Do not display DIEs at depth N or greater
          --dwarf-start=N            Display DIEs starting at offset N
          --dwarf-check              Make additional dwarf consistency checks.
          --ctf-parent=NAME          Use CTF archive member NAME as the CTF parent
          --visualize-jumps          Visualize jumps by drawing ASCII art lines
          --visualize-jumps=color    Use colors in the ASCII art
          --visualize-jumps=extended-color
                                     Use extended 8-bit color codes
          --visualize-jumps=off      Disable jump visualization
          --disassembler-color=off       Disable disassembler color output.
          --disassembler-color=terminal  Enable disassembler color output if displaying on a terminal. (default)
          --disassembler-color=on        Enable disassembler color output.
          --disassembler-color=extended  Use 8-bit colors in disassembler output.

    objdump: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex plugin
    objdump: supported architectures: i386 i386:x86-64 i386:x64-32 i8086 i386:intel i386:x86-64:intel i386:x64-32:intel iamcu iamcu:intel

    The following i386/x86-64 specific disassembler options are supported for use
    with the -M switch (multiple options should be separated by commas):
      x86-64      Disassemble in 64bit mode
      i386        Disassemble in 32bit mode
      i8086       Disassemble in 16bit mode
      att         Display instruction in AT&T syntax
      intel       Display instruction in Intel syntax
      att-mnemonic  (AT&T syntax only)
                  Display instruction with AT&T mnemonic
      intel-mnemonic  (AT&T syntax only)
                  Display instruction with Intel mnemonic
      addr64      Assume 64bit address size
      addr32      Assume 32bit address size
      addr16      Assume 16bit address size
      data32      Assume 32bit data size
      data16      Assume 16bit data size
      suffix      Always display instruction suffix in AT&T syntax
      amd64       Display instruction in AMD64 ISA
      intel64     Display instruction in Intel64 ISA
    Report bugs to <https://bugs.gentoo.org/>.

### [ranlib]

`user `[`$`]`ranlib --help`

    Usage: ranlib [options] archive
     Generate an index to speed access to archives
     The options are:
      @<file>                      Read options from <file>
      --plugin <name>              Load the specified plugin
      -D                           Use zero for symbol map timestamp
      -U                           Use actual symbol map timestamp (default)
      -t                           Update the archive's symbol map timestamp
      -h --help                    Print this help message
      -v --version                 Print version information
    ranlib: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex plugin
    Report bugs to <https://bugs.gentoo.org/>

### [readelf]

[readelf] is a powerful command that reads information contained within ELF files. For example, to read the ELF header from `example.c`:

`user `[`$`]`readelf -h a.out`

    ELF Header:
      Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
      Class:                             ELF64
      Data:                              2's complement, little endian
      Version:                           1 (current)
      OS/ABI:                            UNIX - System V
      ABI Version:                       0
      Type:                              DYN (Position-Independent Executable file)
      Machine:                           Advanced Micro Devices X86-64
      Version:                           0x1
      Entry point address:               0x1060
      Start of program headers:          64 (bytes into file)
      Start of section headers:          42232 (bytes into file)
      Flags:                             0x0
      Size of this header:               64 (bytes)
      Size of program headers:           56 (bytes)
      Number of program headers:         14
      Size of section headers:           64 (bytes)
      Number of section headers:         38
      Section header string table index: 37

### [size]

[size] displays the sizes of sections within binary files. For example, using `example.c`:

`user `[`$`]`size a.out`

       text     data     bss     dec     hex filename
       1456     600       8    2064     810 a.out

### [strings]

[strings] allows for users to view the printable characters contained within an executable file. This has a variety of uses that will not be outlined here. From the example C file, it is possible to find the string within the ELF:

`user `[`$`]`strings a.out | grep "Hello, World!"`

    Hello, World!

### [strip]

[strip] can remove all symbols and other data from a variety of file types. For example, using the output of `gcc example.c`:

`user `[`$`]`strip a.out`

## [Troubleshooting]

### [Preserved-rebuild loop]

When Portage is caught in a `@preserved-rebuild` loop and the only culprit failing is binutils, use the following steps to resolve the issue. First use the [binutils-config] command to select the latest emerged version. See [Select a new version](#Select_a_newer_version) section above. After executing this step, return here and perform a `--depclean`:

`root `[`#`]`emerge --ask --depclean`

Finally perform a `@preserved-rebuild` a final time:

`root `[`#`]`emerge --ask @preserved-rebuild`

## [Removal]

### [Unmerge]

This package is part of the [system set](https://wiki.gentoo.org/wiki/@system "@system") and should not be removed from systems. *Older* versions of the package can be safely removed by passing the `--depclean` option to [emerge]:

`root `[`#`]`emerge --ask --depclean --verbose sys-devel/binutils`

## [See also]

-   [GDB](https://wiki.gentoo.org/wiki/GDB "GDB") --- used to investigate runtime errors that normally involve memory corruption