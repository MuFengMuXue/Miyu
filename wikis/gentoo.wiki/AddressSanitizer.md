[[]][Official documentation](https://clang.llvm.org/docs/AddressSanitizer.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/AddressSanitizer "wikipedia:AddressSanitizer")

[[]][Official project wiki](https://github.com/google/sanitizers/wiki)

**Address Sanitizer** or ASAN is a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect several memory access errors. It thereby adds a certain level of memory safety to C/C++ code. Address Sanitizer is enabled with the compiler flag `-fsanitize=address`.

## Contents

-   [[1] [Why use AddressSanitizer?]](#Why_use_AddressSanitizer.3F)
-   [[2] [Disadvantages and limitations]](#Disadvantages_and_limitations)
-   [[3] [Configuration]](#Configuration)
-   [[4] [Use]](#Use)
    -   [[4.1] [Example]](#Example)
    -   [[4.2] [Per-package]](#Per-package)
    -   [[4.3] [System-wide use]](#System-wide_use)
        -   [[4.3.1] [Asantoo stage tarball]](#Asantoo_stage_tarball)
        -   [[4.3.2] [Booting]](#Booting)
-   [[5] [Bugs]](#Bugs)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [][Why use AddressSanitizer?]

Address Sanitizer is a very powerful *debugging* feature. It is not a hardening feature.

It provides two related benefits:

1.  Discovery of memory safety issues which weren\'t visible before
2.  Reducing the impact of a memory safety issue to denial of service (because the program will abort)

It is much faster than Valgrind and works fine with newer instruction sets like AVX512.

## [Disadvantages and limitations]

Address Sanitizer has significant performance and memory costs. Expect a system that is 50-100% slower and needs a lot of RAM.

It is incompatible with Valgrind, but it can\'t detect everything Valgrind can (like uninitialized memory use).

It is not possible to use an application that is not using Address Sanitizer with a library that has been compiled with Address Sanitizer. Therefore it is often not possible to exclude single applications from Address Sanitizer usage - you also have to avoid using Address Sanitizer for all dependencies.

It is unsafe to use in production with suid binaries especially because the libsanitizer runtime uses environment variables that may [allow privilege escalation](https://www.openwall.com/lists/oss-security/2016/02/17/9).

## [Configuration]

ASan can only be configured via two methods:

1.  additional flags passed to the compiler at build time (see the relevant compiler\'s documentation for examples)
2.  `ASAN_OPTIONS` if not using the minimal runtime, options are delimited by colon (:)

It may be useful to run the following to *disable* LeakSanitizer which reports memory leaks:

`user `[`$`]`export ASAN_OPTIONS="detect_leaks=0"`

## [Use]

** Note**\
Sanitizers are [not yet compatible](https://github.com/google/sanitizers/issues/247) with FORTIFY_SOURCE and may prevent some issues being found. On balance, sanitizers may be better for debugging, while `_FORTIFY_SOURCE` (which Gentoo enables by default) is better for production use: this default is suppressed with sanitizers are used on Gentoo, but may not be on all distributions. If ASan misses a result unexpectedly, try compiling with `-U_FORTIFY_SOURCE`.

The compiler must be built with sanitizer support:

1.  For GCC, the [[[sanitize]](https://packages.gentoo.org/useflags/sanitize)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") must be enabled on [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]
2.  For Clang, [[[asan]](https://packages.gentoo.org/useflags/asan)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] must be enabled on [[[llvm-runtimes/compiler-rt-sanitizers]](https://packages.gentoo.org/packages/llvm-runtimes/compiler-rt-sanitizers)[]]

### [Example]

First, create the following incorrect C program:

[CODE] **/tmp/outofbounds.c**

    #include <stdio.h>

    /* Contains 3 elements:
      - numbers[0] = 1
      - numbers[1] = 2
      - numbers[2] = 3
    */
    int numbers[] = ;

    int main()

Compile it:

`user `[`$`]`cc -O2 -g -fsanitize=address /tmp/outofbounds.c -o /tmp/outofbounds`

Run it:

`user `[`$`]`/tmp/outofbounds`

    ==705829==ERROR: AddressSanitizer: global-buffer-overflow on address 0x5618b592d030 at pc 0x5618b592a16a bp 0x7ffc395483d0 sp 0x7ffc395483c0
    READ of size 4 at 0x5618b592d030 thread T0
        #0 0x5618b592a169 in main /tmp/outofbounds.c:14
        #1 0x7f5f02009d4f  (/usr/lib64/libc.so.6+0x23d4f)
        #2 0x7f5f02009e08 in __libc_start_main (/usr/lib64/libc.so.6+0x23e08)
        #3 0x5618b592a1c4 in _start (/tmp/outofbounds+0x11c4)

    0x5618b592d030 is located 4 bytes after global variable 'numbers' defined in '/tmp/outofbounds.c' (0x5618b592d020) of size 12
    SUMMARY: AddressSanitizer: global-buffer-overflow /tmp/outofbounds.c:14 in main
    Shadow bytes around the buggy address:
      0x5618b592cd80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592ce00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592ce80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592cf00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592cf80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    =>0x5618b592d000: 00 00 00 00 00 04[f9]f9 f9 f9 f9 f9 00 00 00 00
      0x5618b592d080: f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9 f9
      0x5618b592d100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592d180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592d200: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
      0x5618b592d280: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    Shadow byte legend (one shadow byte represents 8 application bytes):
      Addressable:           00
      Partially addressable: 01 02 03 04 05 06 07
      Heap left redzone:       fa
      Freed heap region:       fd
      Stack left redzone:      f1
      Stack mid redzone:       f2
      Stack right redzone:     f3
      Stack after return:      f5
      Stack use after scope:   f8
      Global redzone:          f9
      Global init order:       f6
      Poisoned by user:        f7
      Container overflow:      fc
      Array cookie:            ac
      Intra object redzone:    bb
      ASan internal:           fe
      Left alloca redzone:     ca
      Right alloca redzone:    cb
    ==705829==ABORTING

ASan has intercepted the allocator and trapped the out-of-bounds access at runtime.

### [Per-package]

The most sensible use of Address Sanitizer (or other sanitizers) is temporary and per-package using [/etc/portage/package.env].

Create a file in [/etc/portage/env] as follows:

[FILE] **`/etc/portage/env/asan.conf`**

    CFLAGS="$ -fsanitize=address"
    CXXFLAGS="$ -fsanitize=address"
    LDFLAGS="$ -fsanitize=address"

    # Only relevant if package uses Meson
    # For Meson packages, it might be necessary to comment out the *FLAGS lines above
    # and only set MYMESONARGS.
    MYMESONARGS="-Db_sanitize=address"

    # Needed because ASAN uses interposition (LD_PRELOAD)
    # Other sanitizers don't need this.
    FEATURES="$ -sandbox -usersandbox"

Next, add an entry to [package.env] followed by the name of the file created in the previous step:

[FILE] **`/etc/portage/package.env`**

    app-misc/hello asan.conf

Then re-emerge the relevant package(s):

`root `[`#`]`emerge --oneshot --usepkg=n app-misc/hello`

### [System-wide use]

** Warning**\
Using Gentoo with Address Sanitizer is highly experimental. You will almost certainly face problems. If you want to try this you should be willing to play around with things and help fixing bugs. You probably don\'t want to use this for any production systems. It also [introduces security risks like local root exploits](https://www.openwall.com/lists/oss-security/2016/02/17/9) and is not suitable for production use.

It is possible to compile a Gentoo system with Address Sanitizer for experimentation, but not advised for production environments. Just trying to do this will automatically uncover many bugs in upstream applications. This project helps to improve the general quality of the upstream software Gentoo uses.

#### [Asantoo stage tarball]

The easiest way to test Gentoo with Address Sanitizer is using a prepared [asantoo stage 3 tarball](https://dev.gentoo.org/~hanno/asantoo/). With this tarball, a normal Gentoo installation can be started.

Differences between the \"normal\" Gentoo stage 3 tarball and the asantoo tarball:

-   It includes the [asantoo overlay](https://github.com/hannob/asantoo). The overlay contains several packages with fixes or workarounds needed to let them compile with Address Sanitizer
-   It has git installed (to sync the overlay).
-   Address Sanitizer CFLAGS/CXXFLAGS/LDFLAGS have been added to [make.conf].
-   Some core packages (gcc, glibc, their dependencies and some other problematic packages) have been excluded from the compilation with Address Sanitizer through [package.env].
-   Some quirks workaround existing problems, these include a Portage hook that fixes libtool scripts and a workaround for pthread detection for some packages.
-   An env file causes Address Sanitizer errors to be logged to [/var/log/asan].

#### [Booting]

The easiest way to play around with this is to just use it in a chroot environment. Booting such a system poses some challenges.

Address Sanitizer only works if [/proc] is mounted. However as you will compile everything with Address Sanitizer the init system can\'t work that way. You will need an initramfs. This can be created with [[genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")], however please note that you need to create the initramfs on a normal Gentoo system.

## [Bugs]

You will almost certainly run into various compilation and runtime issues with many software packages. Some common issues are described on the [Problems](https://wiki.gentoo.org/wiki/AddressSanitizer/Problems "AddressSanitizer/Problems") page.

## [See also]

-   [UndefinedBehaviorSanitizer](https://wiki.gentoo.org/wiki/UndefinedBehaviorSanitizer "UndefinedBehaviorSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect various forms of undefined behaviour (UB).
-   [Valgrind](https://wiki.gentoo.org/wiki/Valgrind "Valgrind") --- dynamic analysis tool which detects memory errors and memory leaks.

## [External resources]

-   [Memory error checking in C and C++: Comparing Sanitizers and Valgrind](https://developers.redhat.com/blog/2021/05/05/memory-error-checking-in-c-and-c-comparing-sanitizers-and-valgrind)
-   [Understanding AddressSanitizer: Better memory safety for your code](https://blog.trailofbits.com/2024/05/16/understanding-addresssanitizer-better-memory-safety-for-your-code/)