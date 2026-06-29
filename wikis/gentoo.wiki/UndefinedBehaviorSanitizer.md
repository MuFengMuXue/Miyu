[[]][Official documentation](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/UndefinedBehaviorSanitizer "wikipedia:UndefinedBehaviorSanitizer")

[[]][Official project wiki](https://github.com/google/sanitizers/wiki)

**Undefined Behavior Sanitizer** or UBSAN is a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect various forms of undefined behaviour (UB). It helps to both identify why an application is misbehaving and to help prevent future issues. Undefined Behavior Sanitizer is enabled with the compiler flag `-fsanitize=undefined`.

## Contents

-   [[1] [Configuration]](#Configuration)
-   [[2] [Use]](#Use)
    -   [[2.1] [Example]](#Example)
    -   [[2.2] [Per-package]](#Per-package)
-   [[3] [Caveats]](#Caveats)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Configuration]

UBsan can only be configured via two methods:

1.  additional flags passed to the compiler at build time (see the relevant compiler\'s documentation for examples)
2.  `UBSAN_OPTIONS` if not using the minimal runtime, options are delimited by colon (:)

It may be useful to run the following when debugging to enable both stacktraces and immediate abort on error:

`user `[`$`]`export UBSAN_OPTIONS="print_stacktrace=1:halt_on_error=1"`

## [Use]

The compiler must be built with sanitizer support:

1.  For GCC, [[[sanitize]](https://packages.gentoo.org/useflags/sanitize)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] must be enabled on [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]
2.  For Clang, [[[ubsan]](https://packages.gentoo.org/useflags/ubsan)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] must be enabled on [[[sys-libs/compiler-rt-sanitizers]](https://packages.gentoo.org/packages/sys-libs/compiler-rt-sanitizers)[]]

### [Example]

First, create the following incorrect C program:

[CODE] **/tmp/overflow.c**

    #include <stdio.h>

    int main()

Compile it:

`user `[`$`]`cc -O2 -g -fsanitize=undefined /tmp/overflow.c -o /tmp/overflow`

Run it:

`user `[`$`]`UBSAN_OPTIONS="print_stacktrace=1:halt_on_error=1" /tmp/overflow`

    /tmp/overflow.c:4:21: runtime error: shift exponent 32 is too large for 32-bit type 'unsigned int'
        #0 0x5612d124209a in main /tmp/overflow.c:4
        #1 0x7fae8909fd4f  (/usr/lib64/libc.so.6+0x23d4f)
        #2 0x7fae8909fe08 in __libc_start_main (/usr/lib64/libc.so.6+0x23e08)
        #3 0x5612d12420e4 in _start (/tmp/foo+0x10e4)

UBsan has instrumented the shift operation and trapped the overflow at runtime, identifying the type of UB and where it occurred.

### [Per-package]

The most sensible use of Undefined Behavior Sanitizer (or other sanitizers) is temporary and per-package using [/etc/portage/package.env].

Create a file in [/etc/portage/env] as follows:

[FILE] **`/etc/portage/env/ubsan.conf`**

    CFLAGS="$ -fsanitize=undefined"
    CXXFLAGS="$ -fsanitize=undefined"
    LDFLAGS="$ -fsanitize=undefined"

    # Only relevant if package uses Meson
    # For Meson packages, it might be necessary to comment out the *FLAGS lines above
    # and only set MYMESONARGS.
    MYMESONARGS="-Db_sanitize=undefined"

Next, add an entry to [package.env] followed by the name of the file created in the previous step:

[FILE] **`/etc/portage/package.env`**

    app-misc/hello ubsan.conf

Then re-emerge the relevant package(s):

`root `[`#`]`emerge --oneshot --usepkg=n app-misc/hello`

## [Caveats]

Sometimes enabling UBSAN makes compiler fail to do constexpr stuff. Check this bug: [gcc bugzilla: error: '((& x) != 0u)' is not a constant expression with fsanitize=undefined](https://gcc.gnu.org/PR71962). You can try using Clang to compile for debugging if this happens.

## [See also]

-   [AddressSanitizer](https://wiki.gentoo.org/wiki/AddressSanitizer "AddressSanitizer") --- a compiler feature in [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") that is able to detect several memory access errors.
-   [Valgrind](https://wiki.gentoo.org/wiki/Valgrind "Valgrind") --- dynamic analysis tool which detects memory errors and memory leaks.

## [External resources]

-   [All about UndefinedBehaviorSanitizer](https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer)
-   [Improving Application Security with UndefinedBehaviorSanitizer (UBSan) and GCC](https://blogs.oracle.com/linux/post/improving-application-security-with-undefinedbehaviorsanitizer-ubsan-and-gcc)