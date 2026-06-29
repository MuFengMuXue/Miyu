[musl](https://wiki.gentoo.org/wiki/Musl "Musl") is very strict regarding standards-conformance compared to the widely used GNU C Library (glibc). This means that many of the GNU extensions, as well as much of the backwards compatibility provided by glibc is completely absent, and applications that use these will often fail to build. Here are some **pointers on getting software to compile with musl**.

** See also**\
For those looking to port Gentoo\'s Musl support to a new architecture then the [New Musl Stage Creation](https://wiki.gentoo.org/wiki/Catalyst/New_Musl_Stages_Creation "Catalyst/New Musl Stages Creation") article will show how to achieve this to apply for official support in Gentoo as the end result.

## Contents

-   [[1] [Macro errors]](#Macro_errors)
    -   [[1.1] [MAXNAMLEN not defined here]](#MAXNAMLEN_not_defined_here)
    -   [[1.2] [MSG_TRYHARD undeclared]](#MSG_TRYHARD_undeclared)
    -   [[1.3] [S_BLKSIZE undeclared]](#S_BLKSIZE_undeclared)
-   [[2] [Undefined references and missing functions]](#Undefined_references_and_missing_functions)
    -   [[2.1] [getopt was not declared in this scope]](#getopt_was_not_declared_in_this_scope)
    -   [[2.2] [undefined reference to getpt]](#undefined_reference_to_getpt)
    -   [[2.3] [undefined reference to fts\* (ex. fts_read)]](#undefined_reference_to_fts.2A_.28ex._fts_read.29)
    -   [[2.4] [undefined reference to \`libintl_dgettext\']](#undefined_reference_to_.60libintl_dgettext.27)
    -   [[2.5] [strtol_l not declared]](#strtol_l_not_declared)
    -   [[2.6] [error: LFS64 interfaces (\*64 undeclared here, ex. pread64)]](#error:_LFS64_interfaces_.28.2A64_undeclared_here.2C_ex._pread64.29)
-   [[3] [Missing headers]](#Missing_headers)
    -   [[3.1] [error.h: No such file or directory]](#error.h:_No_such_file_or_directory)
    -   [[3.2] [cdefs.h: No such file or directory]](#cdefs.h:_No_such_file_or_directory)
-   [[4] [Other build time errors]](#Other_build_time_errors)
    -   [[4.1] [error: assignment of read-only variable \'\[stdout\|stdin\|stderr\]\']](#error:_assignment_of_read-only_variable_.27.5Bstdout.7Cstdin.7Cstderr.5D.27)
    -   [[4.2] [Anyting wtmp/utmp related]](#Anyting_wtmp.2Futmp_related)
-   [[5] [Runtime issues]](#Runtime_issues)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
    -   [[7.1] [Standalone packages]](#Standalone_packages)
    -   [[7.2] [Porting tasks]](#Porting_tasks)
    -   [[7.3] [Patches from other distros]](#Patches_from_other_distros)
    -   [[7.4] [Other resources]](#Other_resources)

## [Macro errors]

Errors like these are usually the easiest, and thankfully the most common issues encountered when porting software to musl. Oftentimes it is possible to just copy the definition from glibc, and then conditionally define it. Sometimes these macros are only aliases in glibc, and if that\'s the case just replace the macro with the original one. The good way of dealing with this is to remove the usage of these macros, and submitting patches upstream.

### [MAXNAMLEN not defined here]

`MAXNAMLEN` is the BSD name for `NAME_MAX`. glibc aliases this as `NAME_MAX`, but not musl, so applications which tries to use this macro will fail to build.

To fix this:

1.  Include `<limits.h>`.
2.  Add a conditional \"ifdef\" for `NAME_MAX`, if it\'s defined then use it. If not, fall back to `MAXNAMLEN`. The reason to fall back to `MAXNAMELEN` is to make the BSD users and friends happy.

See also [glibc\'s documentation](https://www.gnu.org/software/libc/manual/html_node/Limits-for-Files.html).

### [MSG_TRYHARD undeclared]

`MSG_TRYHARD` is also one of these glibc aliases (`_GNU_SOURCE` set). Just use `MSG_DONTROUTE` instead.

### [S_BLKSIZE undeclared]

`S_BLKSIZE` is an alias for `DEV_BSIZE`. Just use `DEV_BSIZE` instead.

## [Undefined references and missing functions]

These errors are very similar to the macro errors above, but for functions instead of macros. The most common cause for undefined reference errors is that the program in question uses some GNU extension, or that musl has moved the function into a separate header that needs to be included first.

### [getopt was not declared in this scope]

musl moves this into its own header. To fix, include `<getopt.h>`.

### [undefined reference to getpt]

`getpt` is specific to glibc, instead use the portable `posix_openpt` function, for example.

** Note**\
`getpt` does not take an argument, but `posix_openpt` does. To get the same behavior, simply pass `O_RDWR`

Example: \"net-misc/vmnet-0.4: vmnet.c:(.text+\<snip\>): undefined reference to getpt\" [[[bug #712470]](https://bugs.gentoo.org/show_bug.cgi?id=712470)[]]

### [][undefined reference to fts\* (ex. fts_read)]

These functions are part fts, a set of functions in glibc that are not in musl libc. There is a standalone package for this here: [[[sys-libs/fts-standalone]](https://packages.gentoo.org/packages/sys-libs/fts-standalone)[]]. To fix this, simply add the standalone as a DEPEND for the affected package:

[FILE] **`package.ebuild`**

    DEPEND="
        ...
        elibc_musl? ( sys-libs/fts-standalone )
        ...
    "

### [][undefined reference to \`libintl_dgettext\']

See: [https://www.gnu.org/software/gettext/FAQ.html#integrating_undefined](https://www.gnu.org/software/gettext/FAQ.html#integrating_undefined)

Example: \"media-libs/fontconfig-2.13.0-r2: undefined reference to \`libintl_dgettext\' \[\...\] on amd64-fbsd\" [[[bug #652674]](https://bugs.gentoo.org/show_bug.cgi?id=652674)[]]

### [strtol_l not declared]

strtol is a function to convert a string to an integer type. The \'\_l\' counterpart takes an additional locale parameter to be used instead of the global locale. musl only uses \"C.UTF-8\", so passing a local locale does not make any sense.

Check for strtol_l in the build system and use strtol if it\'s not available to fix this. Platform macros can also be used, though configure checks are usually prefered.

### [][error: LFS64 interfaces (\*64 undeclared here, ex. pread64)]

The Gentoo tracker bug for these issues is [[[bug #903611]](https://bugs.gentoo.org/show_bug.cgi?id=903611)[]].

The legacy \"LFS64\" (\"large file support\") interfaces, which were provided by macros remapping them to their standard names (`#define stat64 stat` and similar) have been deprecated and are no longer provided under the \_GNU_SOURCE feature profile, only under explicit \_LARGEFILE64_SOURCE. The latter will also be removed in a future version. [https://musl.libc.org/releases.html](https://musl.libc.org/releases.html)

The correct fix is to adjust the code to use standard `off_t` types and then to cater for glibc by passing `-D_FILE_OFFSET_BITS=64` to avoid regressing glibc systems. In autoconf, this can be done with the `AC_SYS_LARGEFILE` macro (if using this, config.h **must** be consistently included before all standard headers everywhere, or corruption may occur).

As a temporary workaround, `-D_LARGEFILE64_SOURCE` can be appended to `CPPFLAGS` by doing

[FILE] **`borked.ebuild`**

    inherit flag-o-matic
    ...
    src_compile()

** Note**\
Report usage of these macros upstream.

See also: [musl release notes, see 1.2.4](https://musl.libc.org/releases.html)

## [Missing headers]

musl is relatively selective of what should go into the core musl libc codebase. The reasoning is obviously different on a case-to-case basis but usually it boils down to:

1.  GNU extensions.
2.  Often unused/error-prone functionality.
3.  Makes more sense as a separate library.

This can often be worked around with \*-standalone packages. Be aware that some standalones, like [[[sys-libs/cdefs-standalone]](https://packages.gentoo.org/packages/sys-libs/cdefs-standalone)[]], are only there for user convenience. Preferably usage of these should be reported upstream.

### [error.h: No such file or directory]

[error.h] just provides extra ways to report errors. This is a GNU extension and is not provided by musl. To fix this, either use the `perror` function, or combine `fprintf(stderr, ...)` with `exit(EXIT_FAILURE)`.

** Note**\
error.h includes a global `error_message_count` variable which \"counts the number of messages that have been output by `error()` and `error_at_line()`\". This sometimes needs to be accounted for, just check for `error_message_count` in the application.

[[[sys-libs/error-standalone]](https://packages.gentoo.org/packages/sys-libs/error-standalone)[]] is available for users\' comfort when compiling third-party software, but contributors and developers should fix these errors, and preferably fix this upstream.

Example: \"net-libs/iax-0.2.2-r3 : iax.c: fatal error: error.h: No such file or directory \" [[[bug #712510]](https://bugs.gentoo.org/show_bug.cgi?id=712510)[]]

### [cdefs.h: No such file or directory]

** Warning**\
cdefs.h is an internal glibc header that should NEVER be used by any application, see [musl faq](https://wiki.musl-libc.org/faq.html#Q:-When-compiling-something-against-musl,-I-get-error-messages-about-%3Ccode%3Esys/cdefs.h%3C/code%3E)

Developers like to wrongly include [sys/cdefs.h] to use the `_*_DECLS` macros. This is a bug and the correct way to do it is to use:

[FILE] **`bug.cpp`**

    #ifdef __cplusplus
    extern "C" **

    #ifdef __cplusplus
    }
    #endif

instead of `_END_DECLS`

## [Other build time errors]

Other build time errors that do not belong to any of the above sections.

### [][error: assignment of read-only variable \'\[stdout\|stdin\|stderr\]\']

In musl stdout, stdin and stderr are read-only and cannot be set like in glibc.

To fix this, use freopen like this:

[CODE]

    freopen("standard-output-file", "w", stdout);

Instead of:

[CODE]

    stdout = fopen ("standard-output-file", "w");

See: [glibc standard streams](https://www.gnu.org/software/libc/manual/html_node/Standard-Streams.html).

Example of this: [lvm2 fix](https://github.com/gentoo/gentoo/commit/2a99ca696dc1229ec4bbe7aa7dc4fb37533c839b#diff-049fb37dde861dc3a15ffcfe8af1ec9e0b2ff8ba4552ef6643b0739c0830bfe8)

### [][Anyting wtmp/utmp related]

This functionality is not implemented in musl mostly due to the \"usefulness/security-risk\"-ratio beeing far too low. It is however mandated by POSIX and therefore musl defines it as stubs instead of just not including it at all.

Because it\'s implemented with stubs instead of simply not being there it means that builds will not fail with a simple \"tmp.h\" not found error as expected. Builds can instead complain about things like undefined macros such as WTMPX_FILENAME and \_PATH_WTMPX, or not finding a valid path to utx.log. This should almost always be solved by making the functionality optional/conditionally removing it.

See: [musl faq about utmp/wtmp](https://wiki.musl-libc.org/faq.html#Q:-Why-is-the-utmp/wtmp-functionality-only-implemented-as-stubs?)

Example: [AccountsService: \"Do not know which filename to watch for wtmp changes\"](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/97)

## [Runtime issues]

** Note**\
musl, compared to other libc\'s, uses a tiny default stack size. That can cause runtime crashes for applications that allocate a lot of data on the stack. See [todo](#todo) below.

## [See also]

-   [Libc](https://wiki.gentoo.org/wiki/Libc "Libc") --- a software component that allows userspace applications to interact with operating system services.
-   [Musl](https://wiki.gentoo.org/wiki/Musl "Musl") --- a [standard C library](https://wiki.gentoo.org/wiki/Libc "Libc") implementation that strives to be lightweight and correct in the sense of standards
-   [Project:Musl](https://wiki.gentoo.org/wiki/Project:Musl "Project:Musl") - Gentoo\'s musl project

## [External resources]

### [Standalone packages]

glibc includes various extra functions which are not part of POSIX, so musl does not include them.

[User:blueness](https://wiki.gentoo.org/wiki/User:Blueness "User:Blueness") has ported and added the common ones to Gentoo:

-   [[[sys-libs/fts-standalone]](https://packages.gentoo.org/packages/sys-libs/fts-standalone)[]] (adds [fts](http://man7.org/linux/man-pages/man3/fts.3.html) - functions to traverse directories etc)
-   [[[sys-libs/obstack-standalone]](https://packages.gentoo.org/packages/sys-libs/obstack-standalone)[]] (obstack in [glibc](https://www.gnu.org/software/libc/manual/html_node/Obstacks.html))
-   [[[sys-libs/queue-standalone]](https://packages.gentoo.org/packages/sys-libs/queue-standalone)[]] (queue.h)
-   [[[sys-libs/rpmatch-standalone]](https://packages.gentoo.org/packages/sys-libs/rpmatch-standalone)[]] (used for \'yes/no\' [questions](http://man7.org/linux/man-pages/man3/rpmatch.3.html))
-   [[[sys-libs/argp-standalone]](https://packages.gentoo.org/packages/sys-libs/argp-standalone)[]] ([extends](https://www.gnu.org/software/libc/manual/html_node/Argp.html) getopt)

### [Porting tasks]

-   Tracker [bug](https://bugs.gentoo.org/713786) for missing includes/compile errors
-   Bugs with [possible patches](https://bugs.gentoo.org/buglist.cgi?f1=blocked&keywords=PATCH%2C%20&keywords_type=allwords&list_id=4532876&o1=equals&query_format=advanced&resolution=---&v1=713786) to test and commit

If a patch is discovered in another distro (or if a developer creates one themselves!), please add PATCH to the keywords (if the correct permissions are possessed) and comment with a link to the patch. File a new bug if one does not already exist.

### [Patches from other distros]

** Warning**\
As Alpine Linux is musl-only, compared to Gentoo and Void, it tends to make non-portable patches. In worst case scenario this will break glibc, oftentimes by symbol redefinition. If unsure, test on glibc.

** Note**\
These patches are often also poorly documented. Please try to figure out what they do and supply a nice message in the .patch/commit. If unsure, ask for help!

If stuck, it may be worth seeing what other musl-using distros have done to fix the problem.

Be aware that some distros, like Alpine, include compatibility packages by default (for now), so this will not always help.

-   [sabotage\'s patches](https://github.com/sabotage-linux/sabotage/tree/master/KEEP)
-   [dragora\'s patches](https://git.savannah.gnu.org/cgit/dragora.git/tree/patches)
-   netbsd\'s pkgsrc [patches](https://github.com/GregorR/musl-pkgsrc-patches)

By all means look at Alpine or Void Linux too, but they do not seem to have an easy listing of patches like the above.

-   Alpine Linux [search](https://pkgs.alpinelinux.org/) ([git](https://git.alpinelinux.org/aports/tree/main/))
-   Void Linux [search](https://voidlinux.org/packages/)
-   [OpenEmbedded](https://cgit.openembedded.org/meta-openembedded/)
-   [Buildroot](https://git.busybox.net/buildroot/)
-   [Adélie Linux](https://pkg.adelielinux.org/current/-/search)
-   Miscellaneous [projects](https://wiki.musl-libc.org/projects-using-musl.html#Linux-distributions-using-musl) using musl

### [Other resources]

-   [[#gentoo-hardened](ircs://irc.libera.chat/#gentoo-hardened)] ([[webchat](https://web.libera.chat/#gentoo-hardened)])
-   [[#musl](ircs://irc.libera.chat/#musl)] ([[webchat](https://web.libera.chat/#musl)])
-   musl\'s [FAQ](https://wiki.musl-libc.org/faq.html)
-   musl\'s POSIX [table](https://repo.or.cz/w/musl-tools.git/blob_plain/HEAD:/tab_posix.html); useful for seeing \'new\' header file names
-   musl\'s compatibility [page](https://wiki.musl-libc.org/compatibility.html)
-   Gentoo\'s [musl overlay](https://gitweb.gentoo.org/proj/musl.git/)