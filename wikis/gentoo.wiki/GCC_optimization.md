This page contains [[changes](https://wiki.gentoo.org/index.php?title=GCC_optimization&oldid=1412756&diff=1436535)] which are not marked for translation.

Other languages:

-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/GCC_optimization/tr "GCC Optimizasyonu (15% translated)")
-   [español](https://wiki.gentoo.org/wiki/GCC_optimization/es "Optimización de GCC (39% translated)")
-   [français](https://wiki.gentoo.org/wiki/GCC_optimization/fr "Optimisation de GCC (52% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/GCC_optimization/it "Ottimizzazione di GCC (26% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GCC_optimization/hu "GCC optimalizálás (97% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/GCC_optimization/pt-br "Otimização do GCC (24% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/GCC_optimization/sv "GCC-optimering (4% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GCC_optimization/ru "Оптимизации GCC (75% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/GCC_optimization/zh-cn "GCC 优化 (52% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GCC_optimization/ja "GCCの最適化 (93% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GCC_optimization/ko "GCC optimization (23% translated)")

This guide provides an introduction to optimizing compiled code using safe, sane [`CFLAGS` and `CXXFLAGS`](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS"). It also describes the theory behind optimizing in general.

Default CFLAGS can be [set in make.conf](https://wiki.gentoo.org/wiki/Make.conf#CFLAGS_and_CXXFLAGS "Make.conf") for Gentoo systems. CFLAGS can also be [specified per-package](https://wiki.gentoo.org/wiki/Knowledge_Base:Overriding_environment_variables_per_package "Knowledge Base:Overriding environment variables per package").

** See also**\
For more information see [CFLAGS and CXXFLAGS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#CFLAGS_and_CXXFLAGS "Handbook:AMD64/Installation/Stage") in the Gentoo Handbook, and the [safe CFLAGS](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS") article. See also the [FAQ](https://wiki.gentoo.org/wiki/FAQ#Things_are_really_unstable_when_using_.27-O9_-ffast-math_-fomit-frame-pointer.27_optimizations._What_gives.3F "FAQ").

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [What are CFLAGS and CXXFLAGS?]](#What_are_CFLAGS_and_CXXFLAGS.3F)
    -   [[1.2] [How are they used?]](#How_are_they_used.3F)
    -   [[1.3] [Misconceptions]](#Misconceptions)
    -   [[1.4] [Ready?]](#Ready.3F)
-   [[2] [Optimizing]](#Optimizing)
    -   [[2.1] [The basics]](#The_basics)
    -   [[2.2] [-march]](#-march)
    -   [[2.3] [cpu-type]](#cpu-type)
    -   [[2.4] [-O]](#-O)
    -   [[2.5] [-pipe]](#-pipe)
    -   [[2.6] [-ftree-vectorize]](#-ftree-vectorize)
    -   [[2.7] [-fomit-frame-pointer]](#-fomit-frame-pointer)
    -   [[2.8] [-fno-semantic-interposition]](#-fno-semantic-interposition)
    -   [[2.9] [-msse, -msse2, -msse3, -mmmx, -m3dnow]](#-msse.2C_-msse2.2C_-msse3.2C_-mmmx.2C_-m3dnow)
    -   [[2.10] [Graphite]](#Graphite)
    -   [[2.11] [-fopenmp]](#-fopenmp)
    -   [[2.12] [Link Time Optimization (LTO)]](#Link_Time_Optimization_.28LTO.29)
    -   [[2.13] [Profile Guided Optimization (PGO)]](#Profile_Guided_Optimization_.28PGO.29)
-   [[3] [Hardening optimizations]](#Hardening_optimizations)
-   [[4] [Optimization FAQs]](#Optimization_FAQs)
    -   [[4.1] [Higher version of GCC should mean better optimizations?]](#Higher_version_of_GCC_should_mean_better_optimizations.3F)
    -   [[4.2] [Is there a perfect optimizer/CFLAGS?]](#Is_there_a_perfect_optimizer.2FCFLAGS.3F)
    -   [[4.3] [What about optimizing GCC itself?]](#What_about_optimizing_GCC_itself.3F)
    -   [[4.4] [But I get better performance with -funroll-loops -fomg-optimize!]](#But_I_get_better_performance_with_-funroll-loops_-fomg-optimize.21)
    -   [[4.5] [What about -O levels higher than 3?]](#What_about_-O_levels_higher_than_3.3F)
    -   [[4.6] [What about compiling outside the target machine?]](#What_about_compiling_outside_the_target_machine.3F)
    -   [[4.7] [What about redundant flags?]](#What_about_redundant_flags.3F)
    -   [[4.8] [What about LDFLAGS?]](#What_about_LDFLAGS.3F)
    -   [[4.9] [Can I use per-package flags?]](#Can_I_use_per-package_flags.3F)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [[] Introduction]

### [][[] What are CFLAGS and CXXFLAGS?]

`CFLAGS` and `CXXFLAGS` are among the environment variables conventionally used to specify compiler options to a build system when compiling C and C++ code. While these variables are not standardized, their use is essentially ubiquitous and any correctly written build should understand these for passing extra or custom options when it invokes the compiler. See the [GNU make](https://www.gnu.org/software/make/manual/make.html#Implicit-Variables) info page for a list of some of the commonly used variables in this category.

Because such a large proportion of the packages that make up most Gentoo systems are written in C and C++, these are two variables administrators will definitely want to set correctly as they will greatly influence the way much of the system is built.

They can be used to decrease the amount of debug messages for a program, increase error warning levels and, of course, to optimize the code produced. The [GCC manual](https://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html#Invoking-GCC) maintains a complete list of available options and their purposes.

### [][[] How are they used?]

Normally, `CFLAGS` and `CXXFLAGS` would be set in the environment when invoking a configure script or with makefiles generated by the [automake] program. In Gentoo-based systems, set the `CFLAGS` and `CXXFLAGS` variables in [/etc/portage/make.conf]. Variables set in this file will be exported to the environment of programs invoked by portage such that all packages will be compiled using these options as a base.

[CODE] **Setting CFLAGS in /etc/portage/make.conf**

    CFLAGS="-march=skylake -O2 -pipe"
    CXXFLAGS="$"

** Important**\
While it is possible to have multiple lines in **USE** flags, having multiple lines in `CFLAGS` can and *will* result in problems with programs such as [cmake]. Make sure the `CFLAGS` declaration is on a single line, with as little whitespace as possible to avoid issues. See [[[bug #500034]](https://bugs.gentoo.org/show_bug.cgi?id=500034)[]] as an example.

As seen in the example above, the `CXXFLAGS` variable is set to use all the options present in `CFLAGS`. Almost every system should be configured in this manner. Additional options for `CXXFLAGS` are less common and don\'t usually apply generally enough to deserve setting them globally.

** Tip**\
[Safe CFLAGS](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS") article might help beginners start optimizing their systems.

### [[] Misconceptions]

While compiler optimizations enabled by various `CFLAGS` can be an effective means of producing smaller and/or faster binaries, they can also impair the function of the code, bloat its size, slow down its execution time, or simply cause a build failure. The point of diminishing performance returns is reached rather quickly when dealing with `CFLAGS`. Don\'t set them arbitrarily.

Remember, the global `CFLAGS` configured in [/etc/portage/make.conf] will be applied to every package on the system so administrators typically only set general, widely-applicable options. Individual packages further modify these options either in the ebuild or the build system itself to generate the final set of flags used when invoking the compiler.

### [][[] Ready?]

Being aware of the risks involved, take a look at some sane, safe optimizations. These will hold in good stead and will be endearing to developers the next time a problem is reported on [Bugzilla](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide"). (Developers will usually request the user to recompile a package with minimal `CFLAGS` to see if the problem persists. Remember: aggressive flags can ruin code!)

## [[] Optimizing]

### [[] The basics]

The goal behind `CFLAGS` and `CXXFLAGS` is to create code tailor-made to the system; it should function perfectly while being lean and fast, if possible. Sometimes these conditions are mutually exclusive, so this guide will stick to combinations known to work well. Ideally, they are the best available for any CPU architecture. For informational purposes, aggressive flag use will be covered later. Not every option listed on the GCC manual (there are hundreds) will be discussed, but basic, most common flags will be reviewed.

** Note**\
When unaware of what a flag does, refer to the relevant chapter of the [GCC manual](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options). If still stumped after viewing the manual, try a search engine or check out the [GCC mailing lists](https://gcc.gnu.org/lists.html).

### [[] -march]

The first and most important option is `-march`. This tells the compiler what code it should produce for the system\'s [processor architecture](https://en.wikipedia.org/wiki/Microarchitecture "wikipedia:Microarchitecture") (or *arch*); it tells GCC that it should produce code for a certain kind of CPU. Different CPUs have different capabilities, support different instruction sets, and have different ways of executing code. The `-march` flag will instruct the compiler to produce specific code for the system\'s CPU, with all its capabilities, features, instruction sets, quirks, and so on provided the source code is prepared to use them. For instance, to take benefit from [AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions "wikipedia:Advanced Vector Extensions") instructions, the source code needs to be adapted to support it.

`-march=` is an [ISA](https://en.wikipedia.org/wiki/Instruction_set_architecture "wikipedia:Instruction set architecture") selection option; it tells the compiler that it may use the instructions from the ISA. On an Intel/AMD64 platform with `-march=native -O2` or lower optimization level, the code will likely end up with AVX instructions used but using shorter SSE XMM registers. When using a compiler version prior to GCC 12, in order to take full advantage of AVX YMM registers, the `-ftree-vectorize` or `-O3` options should be used as well^[\[1\]](#cite_note-1)^.

Even though the `CHOST` variable in [/etc/portage/make.conf] specifies the general architecture used, `-march` should still be used so that programs can be optimized for the system specific processor. x86 and x86-64 CPUs (among others) should make use of the `-march` flag.

What kind of CPU does the system have? To find out, run the following command:

`user `[`$`]`cat /proc/cpuinfo`

or even install [[[app-portage/cpuid2cpuflags]](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)[]] and add the available CPU-specific options to the [/etc/portage/package.use/00cpuflags] file, which the tool does through e.g. the [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *") variable:

`user `[`$`]`cpuid2cpuflags`

    CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

`root `[`#`]`echo "*/* $(cpuid2cpuflags)" > /etc/portage/package.use/00cpu-flags`

To get more details, including `march` and `mtune` values, two commands can be used.

-   The first command tells the compiler not to do any linking (`-c`), and instead of interpreting the `--help` option for clarifying command line options, it now shows if certain options are enabled or disabled (`-Q`). In this case, the options shown are those enabled for the selected target:

    :::: cmd-box


    `user `[`$`]`gcc -c -Q -march=native --help=target`


    ::::

<!-- -->

-   The second command will show the compiler directives for building the header file, but without actually performing the steps and instead showing them on the screen (`-###`). The final output line is the command that holds all the optimization options and architecture selection:

    :::: cmd-box


    `user `[`$`]`gcc -### -march=native /usr/include/stdlib.h`


    ::::

** Note**\
The `l2-cache-size` option represents processor\'s last level cache (L2 or higher if present).^[\[2\]](#cite_note-2)^

### [[] cpu-type]

-   The glibc-hwcaps feature (\>=sys-libs/glibc-2.33) can be used to define `-march` for a more general processor architecture (for \>=sys-devel/gcc-11):

`user `[`$`]`/lib64/ld-linux-x86-64.so.2 --help`

    ...
    Subdirectories of glibc-hwcaps directories, in priority order:
     x86-64-v4
     x86-64-v3 (supported, searched)
     x86-64-v2 (supported, searched)
     x86_64 (supported, searched)

In this example, the cpu supports x86-64-v3 psABI x86_64 which can be used for `-march=x86-64-v3`.

** Note**\
For `-mtune`, the [-msse, -msse2, -msse3, -mmmx, -m3dnow](https://wiki.gentoo.org/wiki/GCC_optimization#-msse.2C_-msse2.2C_-msse3.2C_-mmmx.2C_-m3dnow "GCC optimization") reference lists `cpu-type` models.

Now lets see `-march` in action. This example is for an older AMD Athlon 64 chip:

[FILE] **`/etc/portage/make.conf`AMD64 example**

    CFLAGS="-march=athlon64"
    CXXFLAGS="$"

Here\'s another one for a common Intel processor:

[FILE] **`/etc/portage/make.conf`Intel Core example**

    CFLAGS="-march=skylake"
    CXXFLAGS="$"

If the type of CPU is undetermined, or if the user does not know what setting to choose, it is possible use the `-march=native` setting. When this flag is used, GCC will attempt to detect the processor and automatically set appropriate flags for it. **However, this should not be used when intending to compile packages for different CPUs!**

If compiling packages on one computer in order to run them on a different computer (such as when using a fast computer to build for an older, slower machine), then *do not* use `-march=native`. \"Native\" means that the code produced will run *only* on that type of CPU. The applications built with `-march=native` on an Intel Core CPU will **not** be able to run on an old Intel Atom CPU.

Also available are the `-mtune` and `-mcpu` flags. These flags are normally only used when there is no available `-march` option; certain processor architectures may require `-mtune` or even `-mcpu`. Unfortunately, GCC\'s behavior isn\'t very consistent with how each flag behaves from one architecture to the next.

On x86 and x86-64 CPUs, `-march` will generate code specifically for that CPU using its available instruction sets and the correct ABI; it will have no backwards compatibility for older/different CPUs. Consider using `-mtune` when generating code for older CPUs such as i386 and i486. `-mtune` produces more generic code than `-march`; though it will tune code for a certain CPU, it does not take into account available instruction sets and ABI. Do not use `-mcpu` on x86 or x86-64 systems, as it is deprecated for those architectures.

Only non-x86/x86-64 CPUs (such as ARM, SPARC, Alpha, and PowerPC) may require `-mtune` or `-mcpu` instead of `-march`. On these architectures, `-mtune` / `-mcpu` will sometimes behave just like `-march` (on x86/x86-64) but with a different flag name. Again, GCC\'s behavior and flag naming is not consistent across architectures, so be sure to check the GCC [manual](https://gcc.gnu.org/onlinedocs/gcc/Submodel-Options.html#Submodel-Options) to determine which one should be used.

** Note**\
For more suggested `-march` / `-mtune` / `-mcpu` settings, please read chapter 5 of the appropriate [Gentoo Installation Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") for the architecture. Also, read the GCC manual\'s list of [architecture-specific options](https://gcc.gnu.org/onlinedocs/gcc/Submodel-Options.html#Submodel-Options), as well as more detailed explanations about the differences between `-march`, `-mcpu`, and `-mtune`.

** Warning**\
Do **not** use `-march=native` or `-mtune=native` in the `CFLAGS` or `CXXFLAGS` variables of [make.conf] when compiling with [distcc](https://wiki.gentoo.org/wiki/Distcc#-march.3Dnative "Distcc").

### [[] -O]

** Warning**\
Using `-O3` may cause some packages to break either during the compilation or misbehave at runtime, although `-O3` retains standard conformance, hence any breakage is either undefined behaviour in the application, or (very rarely) a compiler bug.

** Note**\
To print all packages that were built with specified `CFLAGS`/`CXXFLAGS` it\'s possible to use the following command: `grep O3 /var/db/pkg/*/*/CFLAGS`

Next up is the `-O` variable. This variable controls the overall level of optimization. Changing this value will make the code compilation take more time and will use much more memory, especially as the level of optimization is increased.

There are seven `-O` settings: `-O0`, `-O1`, `-O2`, `-O3`, `-Os`, `-Oz`, and `-Og`. Only use one of them in [/etc/portage/make.conf]. There is an eighth option which must not be used system-wide: `-Ofast` - despite its name, it breaks standards conformance and is dangerous.

With the exception of `-O0`, the `-O` settings each activate several additional flags, so be sure to read the GCC manual\'s chapter on [optimization options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options) to learn which flags are activated at each `-O` level, as well as some explanations as to what they do.

Let us examine each optimization level:

-   `-O0`: This level (that is the letter \"O\" followed by a zero) turns off optimization entirely and is the default if no `-O` level is specified in `CFLAGS` or `CXXFLAGS`. This reduces compilation time and can improve debugging info, but some applications will not work properly without optimization enabled. This option is not recommended except for debugging purposes.

<!-- -->

-   `-O1`: the most basic optimization level. The compiler will try to produce faster, smaller code without taking much compilation time. It is basic, but it should get the job done all the time.

<!-- -->

-   `-O2`: A step up from `-O1`. The *recommended* level of optimization unless the system has special needs. `-O2` will activate a few more flags in addition to the ones activated by `-O1`. With `-O2`, the compiler will attempt to increase code performance without compromising on size, and without taking too much compilation time.

<!-- -->

-   `-O3`: enables `-O2` as well as optimizations that are expensive in terms of compile time and memory usage. Compiling with `-O3` is likely to improve performance (although not guaranteed). While historically `-O3` could expose compiler bugs, nowadays issues with `-O3` are almost always instances of undefined behavior (UB) and the code is at fault and should be fixed. Some packages are still known-broken with `-O3`. Using `-O3` is not recommended unless running test suites for packages.

<!-- -->

-   `-Ofast`: New in GCC 4.7, consists of `-O3` plus `-ffast-math`, `-fno-protect-parens`, `-fallow-store-data-races`, `-fstack-arrays` and `-fno-semantic-interposition`. This option breaks strict standards compliance, and is not recommended for use. Do not use this system-wide ever, and only use it per-package if the software has been audited for use with the option.

<!-- -->

-   `-Os`: optimizes code for size. It activates all `-O2` options that do not increase the size of the generated code. It can be useful for machines that have extremely limited disk storage space and/or CPUs with small cache sizes.

<!-- -->

-   `-Oz`: Introduced in GCC 12.1, more aggressively optimize for size than `-Os`. Note this will heavily degrade runtime performance than `-O2`, due to increasing the number of instructions executed if those instructions require fewer bytes to encode.

<!-- -->

-   `-Og`: In GCC 4.8, a new general optimization level, `-Og`, has been introduced. It addresses the need for fast compilation and a superior debugging experience while providing a reasonable level of runtime performance. Overall experience for development should be better than the default optimization level `-O0`. Note that `-Og` does not imply `-g`, it simply disables optimizations that may interfere with debugging.

As previously mentioned, `-O2` is the recommended optimization level. If package compilation fails and while not using `-O2`, try rebuilding with that option. As a fallback option, try setting the `CFLAGS` and `CXXFLAGS` to a lower optimization level, such as `-O1` or even `-O0 -g2 -ggdb` (for error reporting and checking for possible problems).

### [[] -pipe]

A common flag is `-pipe`. This flag has no effect on the generated code, but it makes the compilation process *faster*. It tells the compiler to use pipes instead of temporary files during the different stages of compilation, which uses more memory. On systems with low memory, GCC might get killed. In those cases do not use this flag.

### [[] -ftree-vectorize]

`-ftree-vectorize` is an optimization option (default at `-O2` and up), which attempts to vectorize loops using the selected ISA if possible. The reason it previously wasn\'t enabled at `-O2` is that it doesn\'t always improve code, it can make code slower as well, and usually makes the code larger; it really depends on the loop etc. As of GCC 12, it is enabled by default at `-O2` with a low cost model (`-fvect-cost-model=very-cheap`) to strike a balance between code size and speed benefits. The cost model can be specified with `-fvect-cost-model`. Alternative vectorization cost models include: `cheap`, `dynamic`, and `unlimited`. The `dynamic` cost model (default at `-O3`) is going to estimate the cost of the loop using scalar instructions and vector instructions and will be able to decide whether vectorization is profitable using either compile time or runtime checks. The `cheap` cost model is similar to `dynamic`, although slighty more conservative, it will not take effect if the runtime checks for data dependencies or alignment exceed the parameters. The `unlimited` cost model assumes that vectorization is always profitable, making it switch from auto-vectorization to explicit vectorization, but it should never be used system-wide as it will cause *severe* code bloat.

### [[] -fomit-frame-pointer]

This is a very common flag designed to reduce generated code size. It is turned on at all levels of `-O` (except `-O0`) on architectures where doing so does not interfere with debugging (such as x86-64), but it may need to be activated. In that case add it to the flags. Though the GCC manual does not specify all architectures, it is turned on by using the `-O` option. It\'s still necessary to explicitly enable the `-fomit-frame-pointer` option to activate it on x86-32 with GCC up to version 4.6, or when using `-Os` on x86-32 with any version of GCC. However, using `-fomit-frame-pointer` will make debugging hard or impossible. It is worth noting that this option is not enabled by default when using Clang. It is also worth noting that keeping frame pointers is actually beneficial when profiling a code base, and in this case users may want to disable this through `-fno-omit-frame-pointer`.

** Important**\
Do *not* combine `-fomit-frame-pointer` with the similar flag `-momit-leaf-frame-pointer`. Using the latter flag is discouraged, as `-fomit-frame-pointer` already does the job properly. Furthermore, `-momit-leaf-frame-pointer` has been shown to negatively impact code performance.

### [[] -fno-semantic-interposition]

This flag is meant to improve code generation quality and can provide greater performance (default at `-Ofast`). The default behavior (`-fsemantic-interposition`) follows the ELF standard, which allows interposing of symbols by the dynamic linker. While this might sound useful in certain cases it prevents the compiler from doing extensive code analyses and optimizations (in particular the compiler will not attempt inlining unless the functions have been specifically declared as inlined). Contrary to popular belief, enabling this flag globally is safe (unless interposing symbols is required, for example when using different allocators on system libraries), but the reason for it not being enabled by default is to comply with the ELF standard. In contrast, this flag is part of the default when using Clang.

### [][[] -msse, -msse2, -msse3, -mmmx, -m3dnow]

** Note**\
The GCC [list of x86 and x86-64-specific flags](https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html) matches these instruction sets to their `cpu-type`.

The x86 and x86-64 architectures can have [Streaming SIMD Extensions](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions "wikipedia:Streaming SIMD Extensions") (SSE), [SSE2](https://en.wikipedia.org/wiki/SSE2 "wikipedia:SSE2"), [SSE3](https://en.wikipedia.org/wiki/SSSE3 "wikipedia:SSSE3"), [MMX](https://en.wikipedia.org/wiki/MMX_(instruction_set) "wikipedia:MMX (instruction set)"), and [3DNow!](https://en.wikipedia.org/wiki/3DNow! "wikipedia:3DNow!") instruction sets. These are useful primarily in multimedia, gaming, and other floating point-intensive computing tasks, though they also contain several other mathematical enhancements. These instruction sets are found in more modern CPUs.

** Important**\
Be sure to see if the CPU supports these instruction sets by running [cat /proc/cpuinfo]. The output will include any supported additional instruction sets. Note that **pni** is just a different name for SSE3.

Normally none of these flags need to be added to [/etc/portage/make.conf], as long as the system is using the correct `-march` (for example, `-march=nocona` implies `-msse3`). Some notable exceptions are newer VIA and AMD64 CPUs that support instructions not implied by `-march` (such as SSE3). For CPUs like these additional flags will need to be enabled where appropriate after checking [/proc/cpuinfo].

### [[] Graphite]

Graphite analyzes loop costs for `graphite` GCC when `COMMON_FLAGS` has `-floop-block -fgraphite-identity -floop-parallelize-all`. Refer to the Optimize Options for more.

### [[] -fopenmp]

Open Multi-Processing may generate instructions across multiple threads and registers from sequences using `-fopenmp`. Programs may execute in less time and are more likely to fail to compile. Use options like `-fno-openmp` and `-fopenmp-simd` when compiling the same program at least one more time. Refer to GCC\'s [Option Summary](https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html) for more.

### [][[] Link Time Optimization (LTO)]

** Note**\
LTO heavily increases compile times. Even changing one object file can cause a complete rebuild. GCC 15 supports *incremental LTO*, but this is not very relevant to Portage\'s clean builds.

Link Time Optimization (LTO) is a relatively modern method that optimizes the linking phase of compilation. Packages that have been built with LTO tend to execute faster (not guaranteed) and create smaller binaries. Although LTO can be used with many packages, LTO is still not considered ready for daily use and many packages are still being ported to support LTO. LTO may need to be disabled before reporting bugs because it is a common source of problems. The `-flto` flag may be used, with the optional `auto` argument (detects how many jobs to use) or an integer argument (an integer number of jobs to execute parallel).

** See also**\
The [LTO](https://wiki.gentoo.org/wiki/LTO "LTO") article for more information on LTO on Gentoo.

### [][[] Profile Guided Optimization (PGO)]

*Not to be confused with [the packages.gentoo.org tool and website](https://wiki.gentoo.org/wiki/Packages.gentoo.org "Packages.gentoo.org").*

Profile guided optimization (PGO) consists of compiling and profiling a program to assess hot paths in the code. The data gathered from profiling represents real world applications better than GCC\'s own internal optimizations and cost models. By using gathered profiling data GCC can apply beneficial optimizations while evading optimizations that hurt performance. With extensive profiling PGO can provide significant performance boosts. However, PGO is still considered an experimental optimization technique, it is known to break compilation in certain situations.

In PGO, first the code is compiled with `-fprofile-generate`, which instruments the code. Second, the code is run with applications to collect profile information. Finally, using the profiled data, the code is compiled with `-fprofile-use`. See [man gcc] for more information. To manually enable PGO for packages, see this [forum post](https://forums.gentoo.org/viewtopic-t-938468.html).

Due to its nature, PGO has to be applied on every update or every iteration of an application. This means that all the PGO steps must be executed for each update. Profiling-enabled packages should be run in real world situations, otherwise PGO\'s performance benefits will be less effective. These caveats can make PGO impractical: its possible benefits and caveats should weighted cautiously.

Some Gentoo ebuilds provide PGO optimization on their own, they can be enabled with the [[[pgo]](https://packages.gentoo.org/useflags/pgo)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag. Such ebuilds provide their own unique profiling scripts, with [[[pgo]](https://packages.gentoo.org/useflags/pgo)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] enabled it collects profiling data by running packages or test suites for gathering profiling data. [[[pgo]](https://packages.gentoo.org/useflags/pgo)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] enabled ebuilds benefit from (mostly) better performance with more convenience than running PGO manually. Still, enable [[[pgo]](https://packages.gentoo.org/useflags/pgo)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] cautiously for it is still not ready for daily use.

## [[] Hardening optimizations]

** Note**\
While it is possible to use a [hardened](https://wiki.gentoo.org/wiki/Hardened "Hardened") [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), it certainly isn\'t necessary for adding some hardening flags to [/etc/portage/make.conf] on a different profile. Especially on a desktop system, the use of position independent code (PIC) and position independent executables (PIE) on a system-wide level may cause compilation failures.

** Note**\
Reading section [Do I need to pass any flags to LDFLAGS/CFLAGS in order to turn on hardened building?](https://wiki.gentoo.org/wiki/Hardened/FAQ#Do_I_need_to_pass_any_flags_to_LDFLAGS.2FCFLAGS_in_order_to_turn_on_hardened_building.3F "Hardened/FAQ") in the [Hardened/FAQ](https://wiki.gentoo.org/wiki/Hardened/FAQ "Hardened/FAQ") is recommended for retrieving some basic hardened CFLAGS/CXXFLAGS.

** Warning**\
Changing the CFLAGS/CXXFLAGS can cause problems and in some cases may even render a system unusable. Rebuilding the whole system with [emerge -e \@world] may resolve the situation.

Hardening an otherwise unhardened system, like when using a desktop [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), can be considered a GCC optimization as well, especially in the light of security vulnerabilities such as [Meltdown](https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability) "wikipedia:Meltdown (security vulnerability)") and [Spectre](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability) "wikipedia:Spectre (security vulnerability)").

Some packages feature an individual [`hardened`](https://packages.gentoo.org/useflags/hardened) `USE` flag, enabling tested security enhancements (like CFLAGS/CXXFLAGS). It may be a good idea to set this system-wide in [/etc/portage/make.conf].

Optimizing CFLAGS/CXXFLAGS for overflow protection can be a good idea if security concerns outweigh speed optimization. This may be the case on a daily-use desktop system, while e.g. on an optimized gaming PC it will be considered counterproductive.

Another measure is [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization "wikipedia:Address space layout randomization") (ASLR) which can increase security by randomly placing each function and buffer in memory. This makes it harder for attack vectors to succeed.

PIE is enabled by default when it is safe to do so on in 17.0 profiles and newer^[\[3\]](#cite_note-3)^. PIC may also be enabled by default on executables for architectures that require it (like AMD64). There is no need to set PIE or PIC manually in CFLAGS.

** Note**\
A lot of these flags are now applied internally through the GCC toolchain automatically under the hardened profile, and some even under the regular profile. See table at [Hardened/Toolchain](https://wiki.gentoo.org/wiki/Hardened/Toolchain#Changes "Hardened/Toolchain").

The table below is provided to document flags rather than to serve as a list to use, as defaults are handled elsewhere in Gentoo, and specifying these system-wide may not work correctly:

  -------------------------------------------------- ---------------- ---------------------------------------------------------
  CFLAGS/CXXFLAGS                                    LDFLAGS          function
  `-D_FORTIFY_SOURCE=2` (or `-D_FORTIFY_SOURCE=3`)                    run-time buffer overflow detection
  `-D_GLIBCXX_ASSERTIONS`                                             run-time bounds checking for C++ strings and containers
  `-fstack-protector-strong`                                          stack smashing protector
  `-fstack-clash-protection`                                          increased reliability of stack overflow detection
  `-fcf-protection`                                                   control flow integrity protection
                                                     `-Wl,-z,now`     disable lazy binding
                                                     `-Wl,-z,relro`   read-only segments after relocation
  `-fpie`                                            `-Wl,-pie`       full ASLR for executables
  `-fpic -shared`                                                     no text relocations for shared libraries
  -------------------------------------------------- ---------------- ---------------------------------------------------------

## [[] Optimization FAQs]

### [][[] Higher version of GCC should mean better optimizations?]

Not always because of [software regression](https://en.wikipedia.org/wiki/Software_regression "wikipedia:Software regression"), where an optimization with an earlier version of GCC no longer optimizes. A full list of regressions can be found at this [link](https://gcc.gnu.org/bugzilla/buglist.cgi?quicksearch=regression). Should this happen, please file a bug to [Gentoo\'s bugzilla](https://bugs.gentoo.org) and/or [GCC\'s bugzilla](https://gcc.gnu.org/bugzilla).

### [][[] Is there a perfect optimizer/CFLAGS?]

No, because it would solve the [halting problem](https://en.wikipedia.org/wiki/Halting_problem "wikipedia:Halting problem"), where it can tell if any program stops or runs forever ^[\[4\]](#cite_note-4)^. This means that there is no *perfect* *CFLAGS* for every package. Even if such *CFLAGS* were found, packages change over time.

### [][[] What about optimizing GCC itself?]

[gcc] has `pgo` and `lto` use flags that enables Profile Guided Optimization and Link Time Optimization respectively. To enable for building [gcc] itself with PGO and LTO:

[FILE] **`/etc/portage/package.use/gcc`**

    sys-devel/gcc pgo lto

In Gentoo, a 3-stage bootstrap of [gcc] is done, meaning it compiles itself three times ^[\[5\]](#cite_note-5)^. In stage1, [gcc] is complied using an older [gcc]. In stage2, [gcc] is compiled using stage1 [gcc]. In stage3, [gcc] is compiled using stage2 [gcc] and is used to verify that stage2 [gcc] and stage3 [gcc] are the same. This is done because it is tested more completely and has better performance. The `lto` use flag adds `-flto` to `BOOT_CFLAGS`. The `pgo` use flag adds `-fprofile-generate` to stage2 [gcc] and adds `-fprofile-use -fprofile-reproducible=parallel-runs` to stage4 [gcc].

[gcc] performance may improve via PGO, although it may as much as double the compile times.

### [][[] But I get better performance with -funroll-loops -fomg-optimize!]

No, people only *think* they do because someone has convinced them that more flags are better. Aggressive flags will only hurt applications when used system-wide. Even the GCC [manual](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options) says that using `-funroll-loops` and `-funroll-all-loops` will make code larger and may run more slowly. Yet for some reason, these two flags, along with `-ffast-math`, `-fforce-mem`, `-fforce-addr`, and similar flags, continue to be very popular among ricers who want the biggest bragging rights. Supposing that these flags *are* advantageous for a single application, generalizing this to the whole system is unwise.

The truth of the matter is that they are dangerously aggressive flags. Take a good look around the [Gentoo Forums](https://forums.gentoo.org/) and [Bugzilla](https://bugs.gentoo.org/) to see what those flags do: nothing good!

These flags are not needed globally in `CFLAGS` or `CXXFLAGS`. They will only hurt performance. They might bring on the idea of having a high-performance system running on the bleeding edge, but they don\'t do anything but bloat the code and get bugs marked INVALID or WONTFIX.

Dangerous flags like these are not needed. **Don\'t use them**. Stick to the basics: `-march`, `-O`, and `-pipe`.

### [][[] What about -O levels higher than 3?]

Some users boast about even better performance obtained by using `-O4`, `-O9`, and so on, but the reality is that `-O` levels higher than 3 have no effect. The compiler may accept `CFLAGS` like `-O4`, but it actually doesn\'t do anything with them. It only performs the optimizations for `-O3`, nothing more.

Need more proof? Examine the [source code](https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/opts.cc#l519):

[CODE] **-O source code**

    case OPT_LEVELS_3_PLUS:
        enabled = (level >= 3);
        break;

    case OPT_LEVELS_3_PLUS_AND_SIZE:
        enabled = (level >= 3 || size);
        break;

As can be seen, any value higher than 3 is treated as just `-O3`.

### [][[] What about compiling outside the target machine?]

Some readers might wonder if compiling outside the target machine with a strictly inferior CPU or GCC sub-architecture will result in inferior optimization results (compared to a native compilation). The answer is simple: **No**. Regardless of the actual hardware on which the compilation takes place and the `CHOST` for which GCC was built, as long as the same arguments are used (except for `-march=native`) and the same version of GCC is used (although minor version might be different), the resulting optimizations are strictly the same.

To exemplify, if Gentoo is installed on a machine whose GCC\'s `CHOST` is *i686-pc-linux-gnu*, and a [Distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") server is setup on another computer whose GCC\'s `CHOST` is *i486-linux-gnu*, then there is no need to be afraid that the results would be less optimal because of the strictly inferior sub-architecture of the remote compiler and/or hardware. The result would be as optimized as a native build, as long as the same options are passed to both compilers (and the `-march` parameter doesn\'t get a `native` argument). In this particular case the target architecture needs to be specified explicitly as explained in [Distcc](https://wiki.gentoo.org/wiki/Distcc#-march.3Dnative "Distcc").

The only difference in behavior between two GCC versions built targeting different sub-architectures is the implicit default argument for the `-march` parameter, which is derived from the GCC\'s `CHOST` when not explicitly provided in the command line.

### [][[] What about redundant flags?]

Oftentimes `CFLAGS` and `CXXFLAGS` that are turned on at various `-O` levels are specified redundantly in [/etc/portage/make.conf]. Sometimes this is done out of ignorance, but it is also done to avoid flag filtering or flag replacing.

Flag filtering/replacing is done in many of the ebuilds in the Portage tree. It is usually done because packages fail to compile at certain `-O` levels, or when the source code is too sensitive for any additional flags to be used. The ebuild will either filter out some or all `CFLAGS` and `CXXFLAGS`, or it may replace `-O` with a different level.

The [Gentoo Developer Manual](https://devmanual.gentoo.org/ebuild-writing/functions/src_compile/build-environment/index.html) outlines where and how flag filtering/replacing works.

It\'s possible to circumvent `-O` filtering by redundantly listing the flags for a certain level, such as `-O3`, by doing things like:

[CODE] **Specifying redundant CFLAGS**

    CFLAGS="-O3 -finline-functions -funswitch-loops"

However, **this is not a smart thing to do**. `CFLAGS` are filtered for a reason! When flags are filtered, it means that it is unsafe to build a package with those flags. Clearly, it is *not* safe to compile the whole system with `-O3` if some of the flags turned on by that level will cause problems with certain packages. Therefore, don\'t try to \"outsmart\" the developers who maintain those packages. *Trust the developers*. Flag filtering and replacing is done to ensure stability of the system and application! If an ebuild specifies alternative flags, then don\'t try to get around it.

Building packages with unacceptable flags will most likely lead to problems. When reporting problems on Bugzilla, the flags that are used in [/etc/portage/make.conf] will be readily visible and developers will ask to recompile without those flags. Save the trouble of recompiling by not using redundant flags in the first place! Don\'t just automatically assume to be more knowledgeable than the developers.

### [][[] What about LDFLAGS?]

The Gentoo developers have already set basic, safe `LDFLAGS` in the base profiles, so they do not need to be changed.

### [][[] Can I use per-package flags?]

** Warning**\
Using per-package flags complicates debugging and support. Make sure to mention the use of this feature in the bug reports together with the changes made.

Information on how to use per-package environment variables (including `CFLAGS`) is described in the [Gentoo Handbook, \"Per-Package Environment Variables\"](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced#Per-package_environment_variables "Handbook:AMD64/Portage/Advanced").

## [[] See also]

-   [Configuring compile options](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Configuring_compile_options "Handbook:AMD64/Installation/Stage") (AMD64 Handbook)
-   [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *") --- a [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") variable containing instruction set and other CPU-specific features.
-   [Safe CFLAGS](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS") --- a summary of \"safe\" settings for [CFLAGS](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS") on Gentoo Linux.
-   [RUSTFLAGS](https://wiki.gentoo.org/wiki/Rust#Environment_variables "Rust")

## [[] External resources]

The following resources are of some help in further understanding optimization:

-   [GCC online documentation](https://gcc.gnu.org/onlinedocs/)

## [[] References]

1.  [[[↑](#cite_ref-1)] [GNU GCC Bugzilla, [AVX/AVX2 no ymm registers used in a trivial reduction](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=57952#c8). Retrieved on 2017/07/18.]]
2.  [[[↑](#cite_ref-2)] [GNU GCC Bugzilla, [\'gcc -march=native\' sets L2 cache size equal to L3 cache size on i7 and i5 CPU](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=87444#c3). Retrieved on 2022/08/14.]]
3.  [[[↑](#cite_ref-3)] [ [New 17.0 profiles in the Gentoo repository](https://www.gentoo.org/support/news-items/2017-11-30-new-17-profiles.html)]]
4.  [[[↑](#cite_ref-4)] [[https://en.wikipedia.org/wiki/Full-employment_theorem](https://en.wikipedia.org/wiki/Full-employment_theorem)]]
5.  [[[↑](#cite_ref-5)] [[https://gcc.gnu.org/install/build.html](https://gcc.gnu.org/install/build.html)]]

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: ****\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*