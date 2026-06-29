** Warning**\
This article is *not* about running Linux on [ARM](https://en.wikipedia.org/wiki/ARM_architecture "wikipedia:ARM architecture"), it is about building toolchains for embedded use!

This article is about compiling code for an ARM processor, taking advantage of its [FPU](https://en.wikipedia.org/wiki/Floating-point_unit "wikipedia:Floating-point unit").

** See also**\
For more information on building crossdev toolchains for system and kernel builds: [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev")

## Contents

-   [[1] [Prepare the toolchain]](#Prepare_the_toolchain)
    -   [[1.1] [Building with crossdev]](#Building_with_crossdev)
        -   [[1.1.1] [Building]](#Building)
        -   [[1.1.2] [Enable C++ support]](#Enable_C.2B.2B_support)
        -   [[1.1.3] [Enable nanolib support]](#Enable_nanolib_support)
        -   [[1.1.4] [Create a ARM gdb]](#Create_a_ARM_gdb)
        -   [[1.1.5] [Build for specific CPUs]](#Build_for_specific_CPUs)
    -   [[1.2] [Using the pre-built toolchain]](#Using_the_pre-built_toolchain)
-   [[2] [Writing code]](#Writing_code)
    -   [[2.1] [Error message: \.... uses VFP register arguments \... does not]](#Error_message:_...._uses_VFP_register_arguments_..._does_not)
    -   [[2.2] [Error message: undefined reference to \`\_\_stack_chk_guard\']](#Error_message:_undefined_reference_to_.60_stack_chk_guard.27)
    -   [[2.3] [Using Mbed]](#Using_Mbed)
        -   [[2.3.1] [Missing mbed_config.h]](#Missing_mbed_config.h)
    -   [[2.4] [Using STM32CubeMX]](#Using_STM32CubeMX)
    -   [[2.5] [Using pre-built toolchain\'s samples]](#Using_pre-built_toolchain.27s_samples)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [Referencies]](#Referencies)

## [Prepare the toolchain]

### [Building with crossdev]

If *nanolib*, *hardfloat* and *C++* support are not important, you may proceed to [building](#Building).

\

#### [Building]

** Warning**\
These instructions are specifically for embedded use, not Linux systems. Information for `-linux` toolchains is located at: [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev")

We use [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") to create a local [ebuild repo](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") with symlinks to your \"regular\" Gentoo ebuild repository. The ebuilds are thus the same as for your [x86_64] system, but are now used for cross-compiling to ARM.

The simplest command to build a toolchain with gcc\'s the default target configuration:

`root `[`#`]`crossdev --target arm-none-eabi `

Depending on your CPU, this may not be enough though:

** Important**\
Since there\'s many differences between the ARM CPU families, your `gcc` needs to support them.

To see currently available targets:

`user `[`$`]`arm-none-eabi-gcc --print-multi-lib`

This output is also used by [newlib] at buildtime to create suitable [libc] binaries! For example, if you use a Thumb-only Cortex-M CPU and no thumb-only [libc] (or [libc_nano]) archives available - you may encounter illegal instructions on your CPU since it tries to execute non-thumb instructions!

You can use `with-multilib-list` to support more target CPUs.

There are several profiles to enable ARM CPU targets in the gcc source code. This feature is documented in `gccsource/INSTALL/configure.html` or `info gccinstall -n Configuration` searching for `with-multilib-list`:

  ---------------- ---------------------------- ----------------------------
  `profile_name`   CPU family                   `gcc` source file
  aprofile         Cortex-A CPUs                gcc/config/arm/t-aprofile
  rmprofile        Cortex-R and Cortex-M CPUs   gcc/config/arm/t-rmprofile
  ---------------- ---------------------------- ----------------------------

  : ARM GCC CPU profiles

These can be set (also multiple profiles with **comma separation**) when installing gcc with `--with-multilib-list`

`root `[`#`]`crossdev --target arm-none-eabi --genv 'EXTRA_ECONF="--with-multilib-list=$profile_name"' `

#### [][Enable C++ support]

Just enable the `cxx` `USE` flag in your cross *compiler* package [[[cross-arm-none-eabi/gcc]](https://packages.gentoo.org/packages/cross-arm-none-eabi/gcc)[]].

After you set the flag, rebuild the package.

\

#### [Enable nanolib support]

To enable the nano C library, [[[cross-arm-none-eabi/newlib]](https://packages.gentoo.org/packages/cross-arm-none-eabi/newlib)[]] needs the `nano` `USE` flag.

\

#### [Create a ARM gdb]

Either build [[[dev-debug/gdb]](https://packages.gentoo.org/packages/dev-debug/gdb)[]] with `multitarget` `USE` flag, or emerge the dedicated [[[cross-arm-none-eabi/gdb]](https://packages.gentoo.org/packages/cross-arm-none-eabi/gdb)[]].

\

#### [Build for specific CPUs]

You probably don\'t need this when you installed the toolchain with [gcc] `rmprofile` (see [above](#Building)). Using it, your toolchain supports all various sub-architectures and flavors with floating point units and without.

To build toolchains for specific CPUs:

Quoting Embedded Artistry^[\[1\]](#cite_note-Embedded_Artistry-1)^:

** Note**\
**SOFT**

The soft option enables full software floating-point support. The compiler will not generate FPU instructions in soft mode. Instead, the compiler generates library calls to handle floating point operations. The compiler also generates prologue and epilogue functions to pass floating-point arguments (float, double) into integer registers (one for float, two for double).

**SOFTFP**

The softfp option is a hybrid between hard and soft. The compiler is allowed to generate hardware floating-point instructions, but it still uses the soft-float ABI. Like with soft, the compiler generates functions to pass floating-point arguments to integer registers. Depending on the chosen FPU (-mfpu), the compiler can choose when to use emulated or hardware floating-point instructions.

**HARD**

The hard option enables full hardware floating-point support. The compiler generates floating-point instructions and uses the floating-point ABI. Floating-point function arguments are passed directly into FPU registers. Since there are no function prologue or epilogue requirements, no pipeline stalls are incurred with floating-point arguments. The hard float option will provide you with the highest performance, but does limit your compiled binary to the selected FPU.

When using the hard option, you must define an FPU using -mfpu.

It\'s a bit tricky to enable *hard floating point* targets. One way to enable it, supposing the target processor has an [FPU](https://en.wikipedia.org/wiki/Floating-point_unit "wikipedia:Floating-point unit"), is the following:

`root `[`#`]`crossdev --target arm-hardfloat-eabi --env \ `

               'EXTRA_ECONF="--with-cpu=cortex-m4
                             --with-float-abi=hard
                             --with-mode=thumb"'

Analyzing the above command, we replaced [-none-] with [-hardfloat-] in the cross-compile target speficier.

As for the `EXTRA_ECONF` flags, they were copied from a [readme.txt] file found in the ARM toolchain [source](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm)\'s root or the following path for the pre-built version: [share/doc/gcc-arm-none-eabi/]. Here are the contents of the [readme.txt] for convenience:

`user `[`$`]`cat readme.txt`

    --------------------------------------------------------------------------
    | Arm core   | Command Line Options                       | multilib     |
    |------------|--------------------------------------------|--------------|
    | Cortex-M0+ | -mthumb -mcpu=cortex-m0plus                | thumb        |
    | Cortex-M0  | -mthumb -mcpu=cortex-m0                    | /v6-m        |
    | Cortex-M1  | -mthumb -mcpu=cortex-m1                    |              |
    |------------|--------------------------------------------|--------------|
    | Cortex-M3  | -mthumb -mcpu=cortex-m3                    | thumb        |
    |            |                                            | /v7-m        |
    |------------|--------------------------------------------|--------------|
    | Cortex-M4  | -mthumb -mcpu=cortex-m4                    | thumb        |
    | (No FP)    |                                            | /v7e-m       |
    |------------|--------------------------------------------|--------------|
    | Cortex-M4  | -mthumb -mcpu=cortex-m4 -mfloat-abi=softfp | thumb        |
    | (Soft FP)  |                                            | /v7e-m+fp    |
    |            |                                            | /softfp      |
    |------------|--------------------------------------------|--------------|
    | Cortex-M4  | -mthumb -mcpu=cortex-m4 -mfloat-abi=hard   | thumb        |
    | (Hard FP)  |                                            | /v7e-m+fp    |
    |            |                                            | /hard        |
    |------------|--------------------------------------------|--------------|
    | Cortex-M7  | -mthumb -mcpu=cortex-m7                    | thumb        |
    | (No FP)    |                                            | /v7e-m       |
    |            |                                            | /nofp        |
    |------------|--------------------------------------------|--------------|
    | Cortex-M7  | -mthumb -mcpu=cortex-m7 -mfloat-abi=softfp | thumb        |
    | (Soft FP)  |                                            | /v7e-m+dp    |
    |            |                                            | /softfp      |
    |------------|--------------------------------------------|--------------|
    | Cortex-M7  | -mthumb -mcpu=cortex-m7 -mfloat-abi=hard   | thumb        |
    | (Hard FP)  | -mfpu=fpv5-sp-d16                          | /v7e-m+dp    |
    |            |                                            | /hard        |
    |------------|--------------------------------------------|--------------|
    | Cortex-M23 | -mthumb -mcpu=cortex-m23                   | thumb        |
    |            |                                            | /v8-m.base   |
    |------------|--------------------------------------------|--------------|
    | Cortex-M33 | -mthumb -mcpu=cortex-m33                   | thumb        |
    |  (No FP)   |                                            | /v8-m.main   |
    |            |                                            | /nofp        |
    |------------|--------------------------------------------|--------------|
    | Cortex-M33 | -mthumb -mcpu-cortex-m33                   | thumb        |
    | (Soft FP)  | -mfloat-abi=softfp                         | /v8-m.main+fp|
    |            |                                            | /softfp      |
    |------------|--------------------------------------------|--------------|
    | Cortex-M33 | -mthumb -mcpu=cortex-m33                   | thumb        |
    | (Hard FP)  | -mfloat-abi=hard                           | /v8-m.main+fp|
    |            |                                            | /hard        |
    |------------|--------------------------------------------|--------------|
    | Cortex-R4  | [-mthumb] -mcpu=cortex-r?                  | thumb        |
    | Cortex-R5  |                                            | /v7          |
    | Cortex-R7  |                                            | /nofp        |
    | Cortex-R8  |                                            |              |
    | (No FP)    |                                            |              |
    |------------|--------------------------------------------|--------------|
    | Cortex-R5  | [-mthumb] -mcpu=cortex-r?                  | thumb        |
    | Cortex-R7  | -mfloat-abi=softfp                         | /v7+fp       |
    | Cortex-R8  |                                            | /softfp      |
    | (Soft FP)  |                                            |              |
    |------------|--------------------------------------------|--------------|
    | Cortex-R5  | [-mthumb] -mcpu=cortex-r?                  | thumb        |
    | Cortex-R7  | -mfloat-abi=hard                           | /v7+fp       |
    | Cortex-R8  |                                            | /hard        |
    | (Hard FP)  |                                            |              |
    |------------|--------------------------------------------|--------------|
    | Cortex-R52 | [-mthumb] -mcpu=cortex-r52                 | thumb        |
    | (No FP)    |                                            | /v7          |
    |            |                                            | /nofp        |
    |------------|--------------------------------------------|--------------|
    | Cortex-R52 | [-mthumb] -mcpu=cortex-r52                 | thumb        |
    | (Soft FP)  | -mfloat-abi=softfp                         | /v7+fp       |
    |            |                                            | /softfp      |
    |------------|--------------------------------------------|--------------|
    | Cortex-R52 | [-mthumb] -mcpu=cortex-r52                 | thumb        |
    | (Soft FP)  | -mfloat-abi=hard                           | /v7+fp       |
    |            |                                            | /hard        |
    |------------|--------------------------------------------|--------------|
    | Cortex-A*  | [-mthumb] -mcpu=cortex-a*                  | thumb        |
    | (No FP)    |                                            | /v7          |
    |            |                                            | /nofp        |
    |------------|--------------------------------------------|--------------|
    | Cortex-A*  | [-mthumb] -mcpu=cortex-a*                  | thumb        |
    | (Soft FP)  | -mfloat-abi=softfp                         | /v7+fp       |
    |            |                                            | /softfp      |
    |------------|--------------------------------------------|--------------|
    | Cortex-A*  | [-mthumb] -mcpu=cortex-a*                  | thumb        |
    | (Hard FP)  | -mfloat-abi=hard                           | /v7+fp       |
    |            |                                            | /hard        |
    --------------------------------------------------------------------------

### [Using the pre-built toolchain]

A pre-built toolchain is the [GNU Arm Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm). Remember to update your `PATH` by prepending the location of the toolchain\'s bin folder:

`user `[`$`]`export PATH="/path/to/toolchain/bin:$PATH" `

## [Writing code]

#### [Error message: \.... uses VFP register arguments \... does not]

This probably means that some of the libraries being linked, were compiled with `hardfloat` (`-mfloat=hardfloat`) while others with `floatfp` or `float`. This can also happen when the compiler was compiled in an opposite to the code manner.

#### [][Error message: undefined reference to \`\_\_stack_chk_guard\']

The `__stack_chk*` symbols are defined by [libc.a] and are used for [stack smashing protection](https://en.wikipedia.org/wiki/Buffer_overflow_protection).

In the case of compilation errors like `` undefined reference to `__stack_chk_guard' ``, you can disable stack smashing guards by disabling the `ssp` `USE` for [cross-arm\*/gcc].

\

### [Using Mbed]

[Mbed](https://www.mbed.com) is an online platform for writing and compiling code for various boards. It has an *export* function that enables retrieving the said code including a [Makefile] and the imported libraries.

** Note**\
If [arm-hardfloat-eabi] or [-mfloat=hard] is used, the [Makefile] must be adapted since it uses [arm-none-eabi] and [-march=floatfp].

** Important**\
If instead of the `mbed-os` library, the `mbed` one is included, being precompiled, it might not link against hardfloatly compiled code.

#### [Missing mbed_config.h]

If compilation fails with a missing [mbed_config.h] file, [Makefile] needs to be adapted with a point to the root folder\'s [mbed_config.h] file.

### [Using STM32CubeMX]

[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) can be used to initialize code. In provides a graphical user interface to choose pin modes and clocks.

### [][Using pre-built toolchain\'s samples]

The pre-built [GNU Arm Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm), comes with code samples and [Makefile]s.

## [See also]

## [External resources]

1.  [Embedded Artistry](https://embeddedartistry.com/blog/2017/10/9/r1q7pksku2q3gww9rpqef0dnskphtc) explains the difference between `hard`, `softfp` and `soft` (the three ARM floating point compiler options).
2.  [Discussion](http://gentoo.2317880.n4.nabble.com/Building-a-bare-metal-ARM-hard-float-compiler-what-ABI-td300828.html) on the problems enabling *hardfloat*.
3.  Another similar [discussion](https://forums.gentoo.org/viewtopic-t-1067608-start-0.html) in the Gentoo forums.

## [Referencies]

1.  [[[↑](#cite_ref-Embedded_Artistry_1-0)] [Phillip Johnston. [\"Demystifying ARM Floating Point Compiler Options\"](https://embeddedartistry.com/blog/2017/10/9/r1q7pksku2q3gww9rpqef0dnskphtc), October 11, 2017. Retrieved on 2019-09-30]]