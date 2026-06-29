\

**Resources**

[[]][Home](https://www.mingw-w64.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MinGW "wikipedia:MinGW")

[[]][Official documentation](http://mingw.org/wiki)

[[]][GitWeb](https://sourceforge.net/p/mingw/_list/git?)

[[]][[#mingw-w64](ircs://irc.libera.chat/#mingw-w64)] ([[webchat](https://web.libera.chat/#mingw-w64)])

**MinGW** (historically *MinGW32*) is a toolchain that provides a native GCC-based environment for compiling Windows binaries. It can also be used in cross-compilation setups to build binaries on other operating systems. [MinGW-w64](https://mingw-w64.org) is a fork of MinGW that adds support for 64-bit Windows executables. This article assumes the use of MinGW-w64 for both 32-bit and 64-bit target support.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [Quickstart]](#Quickstart)
    -   [[1.3] [Emerge]](#Emerge)
        -   [[1.3.1] [Preparation]](#Preparation)
        -   [[1.3.2] [Toolchain installation]](#Toolchain_installation)
        -   [[1.3.3] [Notes]](#Notes)
        -   [[1.3.4] [Compiling other parts of the runtime]](#Compiling_other_parts_of_the_runtime)
    -   [[1.4] [libssp]](#libssp)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Portage]](#Portage)
        -   [[2.1.1] [Settings]](#Settings)
            -   [[2.1.1.1] [Profile settings]](#Profile_settings)
            -   [[2.1.1.2] [make.conf tweaks]](#make.conf_tweaks)
        -   [[2.1.2] [Emerging packages]](#Emerging_packages)
            -   [[2.1.2.1] [Overriding USE flags, keywords and configuration options]](#Overriding_USE_flags.2C_keywords_and_configuration_options)
            -   [[2.1.2.2] [User patching]](#User_patching)
            -   [[2.1.2.3] [Overlaying]](#Overlaying)
        -   [[2.1.3] [Notes on specific packages]](#Notes_on_specific_packages)
            -   [[2.1.3.1] [app-admin/eselect]](#app-admin.2Feselect)
            -   [[2.1.3.2] [sys-apps/gentoo-functions]](#sys-apps.2Fgentoo-functions)
            -   [[2.1.3.3] [dev-util/gtk-update-icon-cache]](#dev-util.2Fgtk-update-icon-cache)
            -   [[2.1.3.4] [OpenSSL]](#OpenSSL)
            -   [[2.1.3.5] [sys-libs/ncurses]](#sys-libs.2Fncurses)
            -   [[2.1.3.6] [sys-libs/readline]](#sys-libs.2Freadline)
            -   [[2.1.3.7] [x11-libs/cairo]](#x11-libs.2Fcairo)
            -   [[2.1.3.8] [x11-libs/gdk-pixbuf]](#x11-libs.2Fgdk-pixbuf)
            -   [[2.1.3.9] [x11-libs/gtk+]](#x11-libs.2Fgtk.2B)
            -   [[2.1.3.10] [GDBM]](#GDBM)
    -   [[2.2] [SDL tutorial example]](#SDL_tutorial_example)
    -   [[2.3] [Hello World Example]](#Hello_World_Example)
    -   [[2.4] [POSIX threads for Windows]](#POSIX_threads_for_Windows)
        -   [[2.4.1] [Compile GCC/G++ with POSIX thread model]](#Compile_GCC.2FG.2B.2B_with_POSIX_thread_model)
            -   [[2.4.1.1] [x86_64 toolchain]](#x86_64_toolchain)
            -   [[2.4.1.2] [i686 toolchain]](#i686_toolchain)
            -   [[2.4.1.3] [How to link with cross-compiler toolchain]](#How_to_link_with_cross-compiler_toolchain)
        -   [[2.4.2] [Porting POSIX threads to Windows]](#Porting_POSIX_threads_to_Windows)
    -   [[2.5] [Wine and %PATH%]](#Wine_and_.25PATH.25)
    -   [[2.6] [No need for -lm]](#No_need_for_-lm)
    -   [[2.7] [DirectX]](#DirectX)
-   [[3] [Removal]](#Removal)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Emerging a toolchain failed with error: Missing digest for \*.ebuild]](#Emerging_a_toolchain_failed_with_error:_Missing_digest_for_.2A.ebuild)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

** Note**\
The use of target\'s host-part-name mingw64 is strongly discouraged. Most checks in binutils, gdb, gcc, etc (and all their testsuites) are still using mingw32^[\[1\]](#cite_note-gcc55886-1)^.

### [Prerequisites]

To install the MinGW toolchain, prepare the system with a [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") environment:

`root `[`#`]`emerge --ask app-eselect/eselect-repository sys-devel/crossdev`

`root `[`#`]`eselect repository create crossdev`

We use a target descriptor to tell [crossdev] what to build: `$outputarch-$runtime-mingw32`.

Throughout this article, the 32-bit toolchain has `$outputarch == i686`, the 64-bit toolchain has `$outputarch == x86_64`. Since only MinGW-w64 is used as the runtime, it is assumed `$runtime == w64`. (Don\'t get confused by `mingw32`, this is merely a legacy name^[\[1\]](#cite_note-gcc55886-1)^.)

### [Quickstart]

After crossdev is installed, the following command will install the 64-bit MinGW cross-toolchain:

`root `[`#`]`crossdev --target x86_64-w64-mingw32`

To install the 32-bit toolchain (which also uses the MinGW-w64 runtime), use:

`root `[`#`]`crossdev --target i686-w64-mingw32`

Either use the cross-compiler directly, or use the cross-emerge wrapper symlink. For example:

`root `[`#`]`x86_64-w64-mingw32-emerge app-arch/lzop`

The resulting executable can be found in `/usr/x86_64-w64-mingw32/usr/bin/lzop.exe`.

It\'s possible to configure the cross environment in `/usr/x86_64-w64-mingw32/etc/portage`.

### [Emerge]

#### [Preparation]

crossdev will automatically create [/etc/portage/package.keywords/cross-x86_64-w64-mingw32] and [/etc/portage/package.use/cross-x86_64-w64-mingw32] (or their 32-bit counterparts). Since by default some critical USE flags like `sanitize`, `fortran` or `vtv` are left enabled, it might be necessary to override the automatically-created USE flags with

`root `[`#`]`echo "cross-x86_64-w64-mingw32/gcc -fortran -vtv -sanitize" >> /etc/portage/package.use/cross-x86_64-w64-mingw32 `

** Note**\
Users with [hardened profiles](https://wiki.gentoo.org/wiki/Project:Hardened "Project:Hardened") have to (at least for x86_64-w64-mingw32-gcc) disable `hardened` and `pie`:^[\[2\]](#cite_note-2)^

`root `[`#`]`echo "cross-x86_64-w64-mingw32/gcc -fortran -vtv -sanitize -pie -hardened" >> /etc/portage/package.use/cross-x86_64-w64-mingw32-gcc `

With [crossdev] installed, emerge the MinGW toolchain:

#### [Toolchain installation]

To build a 64-bit Windows toolchain:

`root `[`#`]`crossdev --target x86_64-w64-mingw32`

To build a 32-bit Windows toolchain:

`root `[`#`]`crossdev --target i686-w64-mingw32`

** Note**\
The `CHOST` recommendation has recently changed in this document as a number of packages (ie [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]]) require the newer API available in mingw64-runtime. To use the old mingw-runtime for 32-bit, use the target `CHOST` value of `i686-pc-mingw32`.

** Note**\
If `sys-libs/binutils` is already installed from `stable`, please note that `binutils` and `binutils-libs` should be the same version. In case of a conflict, consider using `crossdev -S`.

Adding the `--ex-insight` or `--ex-gcc` options may cause issues; they have been known to not build. `--ex-gdb` will enable GDB and likely will work, but it is not very useful on Linux because MinGW GCC by default makes PEs (EXE files), not ELF files, and [gdb] has no way of running PEs on Linux. A remote debugger (with a Windows target machine) is a possibility, but an unlikely one.

#### [Notes]

-   the GCJ sources will not compile due to missing makespec files that do not get installed (copying from MinGW from Windows does not work either).
-   `sanitize` may cause compilation failures on gcc-4.9 or later.
-   `openmp` was force-disabled in the ebuild, but now respects the USE flag setting. However, it may still cause compilation issues when enabled.

#### [Compiling other parts of the runtime]

The MinGW-w64 runtime supplies some development tools and libraries, in particular a `pthreads` implementation which has features the one below does not. Before taking this step, make sure to backup the contents of [/etc/portage/package.use/cross-x86_64-w64-mingw32], as this next step will overwrite it with a new line for the runtime. If this file isn\'t edited to add in the old contents back into this file, when doing an update looking for changes in USE flags, emerge will try to re-emerge the compilers with the `multilib` flag on.

[CODE] **[/etc/portage/package.use/cross-x86_64-w64-mingw32]**

    cross-x86_64-w64-mingw32/mingw64-runtime libraries idl tools -selinux -multilib

To install:

`root `[`#`]`USE="libraries idl tools" crossdev --ex-only --ex-pkg cross-x86_64-w64-mingw32/mingw64-runtime -t x86_64-w64-mingw32`

### [libssp]

The GCC USE flag [sys-devel/gcc\[libssp\]](https://packages.gentoo.org/useflags/libssp) has been masked, since it is usually provided by libc. Apparently `msvcrt` does not provide `libssp`, so it is recommended to re-enable this USE flag for cross-compilation (see [package.use.mask](https://wiki.gentoo.org/wiki//etc/portage/profile/package.use.mask "/etc/portage/profile/package.use.mask")):

[FILE] **`/etc/portage/profile/package.use.mask/mingw-libssp`**

    cross-i686-w64-mingw32/gcc -libssp
    cross-x86_64-w64-mingw32/gcc -libssp

[FILE] **`/etc/portage/profile/package.use.force/mingw-libssp`**

    cross-i686-w64-mingw32/gcc libssp
    cross-x86_64-w64-mingw32/gcc libssp

## [Usage]

### [Portage]

The crossdev environment is a completely independent Portage instance, configured in [/usr/x86_64-w64-mingw32/etc/portage].

Emerging packages might work. If it doesn\'t, disabling all USE flags after a failed build, then selectively adding them back, might work. If it doesn\'t, it\'s probably not possible to build the package. However, as with any other bug, one may report, diagnose and/or fix it.

#### [Settings]

It\'s possible to adjust some cross-portage defaults like the temporary build directory:

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/profile/make.conf`**

    PORTAGE_TMPDIR=/tmp/portage/$

\

##### [Profile settings]

** Note**\
If [crossdev] hasn\'t created the [/usr/x86_64-w64-mingw32/etc/portage/profile/] directory, then the [emerge-wrapper] command may be needed to initialize it:

`root `[`#`]`emerge-wrapper --target x86_64-w64-mingw32 --init`

Various ebuilds support MinGW or Win32 targets, but different build systems often need different indicators. Ensuring the following is set in [/usr/x86_64-w64-mingw32/etc/portage/profile/make.defaults] should allow most build systems to detect the proper target. Note that some of these variables may have already been set by [crossdev]:

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/profile/make.defaults`Profile-level variables for x86_64**

    ARCH="amd64"
    KERNEL="-linux Winnt"
    ELIBC="mingw"

[FILE] **`/usr/i686-w64-mingw32/etc/portage/profile/make.defaults`Profile-level variables for i686**

    ARCH="x86"
    KERNEL="-linux Winnt"
    ELIBC="mingw"

##### [make.conf tweaks]

The MinGW-w64 runtime and the cross-toolchain do not provide any [libgcc_s\_\*.dll] files, and without an external source for these files, there may be issues executing whatever is built by the cross-toolchain. Fortunately, there\'s a workaround in the form of `LDFLAGS` `-static-libgcc` and `-static-libstdc++`, however, due to the fact that these non-standard flags tend to get stripped out of builds, some trickery is needed. Add the following to [make.conf]:

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/profile/make.conf`**

    # Workaround missing libgcc_s_*.dll files by statically linking libc and libstdc++
    CC="$-gcc -static-libgcc"
    CXX="$-g++ -static-libgcc -static-libstdc++"

USE flags can be set globally in [make.conf] or per-package in [package.use]; as the builds are for Win32 it likely makes sense to globally disable some flags, such as `USE="-X"` and globally enable `USE="win32"` in case any packages support it.

Finally, it is a good idea to make sure that the code compiled will actually run on the targets it is to be executed on. This means setting appropriate `-march` and `-mtune` values in the `CFLAGS` variable for the target platform:

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/profile/make.conf`**

    CFLAGS="-march=x86_64 -mtune=generic -O2 -pipe"
    CXXFLAGS="$"

[FILE] **`/usr/i686-w64-mingw32/etc/portage/profile/make.conf`**

    CFLAGS="-march=i686 -mtune=generic -O2 -pipe"
    CXXFLAGS="$"

#### [Emerging packages]

Cross emerging is done by `x86_64-w64-mingw32-emerge`. For example, to emerge the [[[sys-libs/zlib]](https://packages.gentoo.org/packages/sys-libs/zlib)[]] package, use:

`root `[`#`]`x86_64-w64-mingw32-emerge sys-libs/zlib`

Alternatively:

`root `[`#`]`emerge-wrapper --target x86_64-w64-mingw32 -av sys-libs/zlib`

** Note**\
It\'s possible to get rid of emerge\'s news messages by disabling the news feature

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/make.conf`Disabling the news feature**

    FEATURES="-news"

Alternatively, deleting the contents of [/usr/x86_64-w64-mingw32/var/lib/gentoo/news/news-gentoo] may help:

`root `[`#`]`echo "" > /usr/x86_64-w64-mingw32/var/lib/gentoo/news/news-gentoo.unread`

Using Portage, the following issues can occur:

-   The application wants GDBM (see below).
-   The application wants to link with ALSA, OSS, Mesa or other libraries only applicable to X or Linux.
-   The application\'s ebuild doesn\'t contain the necessary configuration options to support a MinGW or Win32 target.
-   The application is an unnecessary utility script such as gentoo-functions or [eselect].
-   An ebuild inherits multilib and specifies `MULTILIB_CHOST_TOOLS` without adding `$(get_exeext)`.

In the multilib case, emerge wants to move the executables specified in `MULTILIB_CHOST_TOOLS`. But when cross compiling with mingw32, the executables receive an extension `.exe` and emerge cannot find the file without the extension and fails. If this sort of error is encountered, please mention the package in [[[bug #588330]](https://bugs.gentoo.org/show_bug.cgi?id=588330)[]]. In the meantime, fix the issue by overlaying (see [below](#Overlaying)) a custom ebuild, appending the extension `$(get_exeext)` to all files in `MULTILIB_CHOST_TOOLS`.

The main techniques to tweak ebuilds to make them work are

##### [][Overriding USE flags, keywords and configuration options]

To override USE flags and keywords, simply use [/etc/portage/package.use/] and [/etc/portage/package.keywords/] respectively. For configuration options, we can tell emerge to use a package specific file defining environment variables (see [package.env](https://wiki.gentoo.org/wiki/Package.env "Package.env")). For example, if we want to configure [[[x11-libs/cairo]](https://packages.gentoo.org/packages/x11-libs/cairo)[]] with `--with-target=win32`, we create

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/env/econf-target-win32`Environment overrides for configure options**

    EXTRA_ECONF="--with-target=win32"

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/package.env/cairo`Specifying *cairo.conf* as package specific file defining overrides for cairo**

    x11-libs/cairo econf-target-win32

##### [User patching]

Most ebuilds call `epatch_user` which searches for user-provided patches in [\$/etc/portage/patches/]. See [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") for more details.

Place patches to be applied in cross-compilation only in [/usr/x86_64-w64-mingw32/etc/portage/patches/\$category/\$package].

##### [Overlaying]

If an issue cannot be fixed by simply overriding configure options, then we may have to override certain ebuilds by creating a [new ebuild repository](https://wiki.gentoo.org/wiki/Crossdev#Crossdev_overlay "Crossdev") that\'s only active for the cross environment. We\'ll use [/usr/x86_64-w64-mingw32/usr/portage] since it\'s empty.

Create the following files:

[FILE] **`/usr/x86_64-w64-mingw32/usr/portage/metadata/layout.conf`**

    masters = gentoo

[FILE] **`/usr/x86_64-w64-mingw32/usr/portage/profiles/repo_name`**

    cross-x86_64-w64-mingw32

[FILE] **`/usr/x86_64-w64-mingw32/etc/portage/repos.conf`**

    [DEFAULT]
    main-repo = gentoo

    [cross-x86_64-w64-mingw32]
    location = /usr/x86_64-w64-mingw32/usr/portage/
    masters = gentoo
    auto-sync = no

Portage will then use our custom ebuilds in the [/usr/x86_64-w64-mingw32/usr/portage/] folder when we\'re building for Windows.

#### [Notes on specific packages]

##### [][app-admin/eselect]

This package brings in a number of system dependencies that are just plain not needed to build win32 software, and at the time of writing many of them (like python) fail to emerge. However, as the binary is called during phase functions of other ebuilds that are needed, a simple [package.provided] entry does not suffice to get rid of it. Instead, it can be recommend to [overlay](#Overlaying) a custom [[[app-admin/eselect]](https://packages.gentoo.org/packages/app-admin/eselect)[]] ebuild that installs a dummy [eselect] binary, something that will do nothing yet always return success. This is a dirty hack that certainly has drawbacks, but it at least allows the meat of slotted packages to be emerged.

The ebuild could look for example like this:

[FILE] **`/usr/i686-w64-mingw32/usr/portage/app-admin/eselect/eselect-1.4.6.ebuild`**

    EAPI=5

    DESCRIPTION="Dummy binary"

    SLOT="0"
    KEYWORDS="~alpha ~amd64 ~arm ~arm64 ~hppa ~ia64 ~m68k ~mips ~ppc ~ppc64 ~s390 ~sh ~sparc ~x86 ~ppc-aix ~amd64-fbsd ~sparc-fbsd ~x86-fbsd ~x64-freebsd ~x86-freebsd ~hppa-hpux ~ia64-hpux ~x86-interix ~amd64-linux ~arm-linux ~ia64-linux ~x86-linux ~ppc-macos ~x64-macos ~x86-macos ~m68k-mint ~sparc-solaris ~sparc64-solaris ~x64-solaris ~x86-solaris"

    src_unpack() /$
    }

    src_install() /usr/bin/
        echo ":" > $/usr/bin/$
        chmod +x $/usr/bin/$
    }

##### [][sys-apps/gentoo-functions]

This is another one of those necessary tool dependencies that isn\'t really needed in a mingw cross-build environment. Although mostly implemented in shell, there is a single compiled binary that fails due to missing POSIX API stuff, [/sbin/consoletype]. This package may be something that can be [package.provided] away, but to be on the safe side one can also overlay this ebuild and install a dummy script that echo\'s \'serial\' and exists with code 1, in place of compiling consoletype.

##### [][dev-util/gtk-update-icon-cache]

[gtk-update-icon-cache] is a tool that various packages inheriting the gnome eclasses will call in their `pkg_postinst` phase functions. Although it may be a good idea to install it for use within the win32 target environment, the resulting binary cannot be run in phase functions and so failures will often occur. Another dummy-script-installing overlay package can get around this issue.

##### [OpenSSL]

Follow this guide: [\[3\]](https://github.com/tatsh/cross-pc-mingw32-openssl)

##### [][sys-libs/ncurses]

Ncurses is a very finicky package, mostly due to the fact that it\'s build system was generated using a custom-forked version of autotools. At this time of writing, *sys-libs/ncurses-5.9-r5* is stable and a static-only installation will emerge with `EXTRA_ECONF="--enable-term-driver --enable-sp-funcs --without-shared"` and `USE="static-libs"`, but ncurses-6.0 will not compile.

##### [][sys-libs/readline]

[[[sys-libs/readline]](https://packages.gentoo.org/packages/sys-libs/readline)[]] is another finicky package, in part because it depends on ncurses. Only `~sys-libs/readline-6.2_p5` will build successfully, newer versions need a lot of patching. Further, due to ncurses being limited to a static-only installation, readline must also be built static-only using `EXTRA_ECONF="--disable-shared"` and `USE="static-libs"`.

##### [][x11-libs/cairo]

Cairo is well supported, but the ebuilds currently do not provide a USE flag for the Win32 target. Specifying `EXTRA_ECONF="--with-target=win32"` and ensuring `USE="-X -aqua -xcb -x11-xcb"` can address that for now.

If the plan is to emerge [[[x11-libs/gtk+]](https://packages.gentoo.org/packages/x11-libs/gtk+)[]], then we abuse the `aqua` USE flag (both packages do not provide a `win32` USE flag) in order to avoid forced X11 dependencies ans set `USE="aqua"` for both packages. This will enable quartz support via configure options which we have to suppress by specifying `EXTRA_ECONF="--enable-quartz=no --enable-quartz-image=no"`.

** Note**\
Support for Win32 in the form of a USE flag may be added to Cairo in the future.

##### [][x11-libs/gdk-pixbuf]

This package builds as-is without any modifications, however, there are two minor issues related to using the package:

-   the pkg_postinst phase is unable to run \'gdk-pixbuf-query-loaders\' to generate the [loaders.cache] file, which means that this will need to be done by hand using Wine, via something like

`root `[`#`]`wine /usr/i686-w64-mingw32/usr/bin/gdk-pixbuf-query-loaders.exe >/usr/i686-w64-mingw32/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders.cache`

-   the paths used by gdk-pixbuf at runtime to find the various loader DLLs are absolute, meaning that they will need to be installed on the target Win32 systems at `[drive]:\usr\lib\gdk-pixbuf-2.0\2.10.0\loaders`.

It\'s possible to circumvent both of these issues by building `gdk-pixbuf` with `EXTRA_ECONF="--with-included-loaders=yes"`, as this will include the loader code directly in the main `gdk-pixbuf` DLL.

##### [][x11-libs/gtk+]

As touched on in the section about cairo above, in order to avoid a lot of X11 deps, gtk+ needs to be built with `USE="aqua"` and `EXTRA_ECONF="--with-gdktarget=win32"` for gtk+:2 or `EXTRA_ECONF="--enable-win32-backend --disable-quartz-backend"` for gtk+:3.

If build failures related to missing symbols are seen in the libraries at installation time, this may be related to a need to clear the [gtk.def] file so that it can be regenerated properly by the build system. An easy way to do this without overlaying the ebuilds is to use the following script snippet in [/usr/i686-w64-mingw32/etc/portage/bashrc]:

[FILE] **`/usr/i686-w64-mingw32/etc/portage/bashrc`**

    case "$/$" in
    x11-libs/gtk+)
            case "$" in
            prepare)
                    einfo "Cleaning out gtk/gtk.def to aid in mingw out-of-source builds"
                    rm -f "$"/gtk/gtk.def
                    ;;
            esac
            ;;
    esac

** Note**\
x11-libs/gtk+-3.18 and newer needs the function `cairo_win32_surface_create_with_format`, which reportedly will not be available until `x11-libs/cairo-1.15.2` or newer.

** Note**\
There are currently collisions between `gtk+:2` and `gtk+:3` on the file `$/usr/bin/gailutil.def`; this needs to be resolved by hand if both slots are desired at the same time.

** Note**\
Support for a win32 use flag may soon be added to cairo in the gentoo repo.

##### [GDBM]

These are \"Standard GNU database libraries\" according to Portage. Many libraries and applications depend on this. The package reportedly compiled successfully compiled in the past, but the current versions in Portage do not compile due to the package requiring a POSIX environment (which mingw is not). Patching is very much needed.

[FILE] **`build.log`excerpt**

    i686-w64-mingw32-gcc -c -I. -I. -march=k8 -msse3 -O2 -pipe gdbmfetch.c  -DDLL_EXPORT -DPIC -o .libs/gdbmfetch.lo
    gdbmopen.c: In function 'gdbm_open':
    gdbmopen.c:171: error: storage size of 'flock' isn't known
    gdbmopen.c:171: error: 'F_RDLCK' undeclared (first use in this function)
    gdbmopen.c:171: error: (Each undeclared identifier is reported only once
    gdbmopen.c:171: error: for each function it appears in.)
    gdbmopen.c:171: error: 'F_SETLK' undeclared (first use in this function)
    gdbmopen.c:177: error: storage size of 'flock' isn't known
    gdbmopen.c:177: error: 'F_WRLCK' undeclared (first use in this function)

To get around this problem for the moment, try building with `USE="-*"`.

### [SDL tutorial example]

Emerge SDL:

`root `[`#`]`i686-w64-mingw32-emerge media-libs/libsdl`

Try compiling this source code (save to `test.c`).

[FILE] **`test.c`**

    #include <SDL/SDL.h>
    #include <windows.h>

    void cool_wrapper(SDL_Surface **s, int flags)

    int main(int argc, char *argv[])

Use the following command to build:

`user `[`$`]`` i686-w64-mingw32-gcc -o test.exe test.c `/usr/i686-w64-mingw32/usr/bin/sdl-config --libs` ``

Test with Wine (requires SDL.dll to be somewhere in Wine\'s `%PATH%`, which includes the same directory as the EXE):

`user `[`$`]`cp /usr/i686-w64-mingw32/usr/bin/SDL.dll . `

`user `[`$`]`wine test.exe `

If it shows a window named SDL_app, then it worked. The window will automatically exit after about 5 seconds (the Windows `Sleep()` function halts execution for 5000 milliseconds).

### [Hello World Example]

Simple Win32 C program to test installation and function.^[\[3\]](#cite_note-3)^

[FILE] **`hello.c`**

    #include <windows.h>

    int WINAPI

    WinMain (HINSTANCE hInstance, HINSTANCE hPrevInst, LPTSTR lpCmdLine, int nShowCmd)

To build GUI, `-mwindows` is added (default is `-mconsole`)

`user `[`$`]`i686-w64-mingw32-gcc hello.c -o hello.exe -mwindows`

Verify with file.

`user `[`$`]`file hello.exe `

hello.exe: PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows

### [POSIX threads for Windows]

At least two alternatives exist to port applications with POSIX threads to windows. One option is to compile `gcc` with the `posix` thread model, described in the next sub-section. The other option is to use a wrapper library that provides a POSIX-compatible API on top of the `win32` thread functions, described in the second next sub-section.

#### [][Compile GCC/G++ with POSIX thread model]

If a cross-compiler is needed with support for `std::thread` (for example to compile DXVK^[\[4\]](#cite_note-4)^ and Wine with the `+mingw` flag, to be able to run Windows games), then the following procedure is needed.

##### [x86_64 toolchain]

It is needed to emerge first the default toolchain, with the unwanted `win32` threading model:

`root `[`#`]`crossdev --target cross-x86_64-w64-mingw32`

Next, the following command changes the environment variables for the toolchain in [/etc/portage/env] and [/etc/portage/package.env] so that the configure step for `gcc` receives the `--enable-threads=posix` parameter:

`root `[`#`]`crossdev --genv 'EXTRA_ECONF="--enable-threads=posix"' --init-target --target cross-x86_64-w64-mingw32`

The `libraries idl tools` USE flags are required for `cross-x86_64-w64-mingw32/mingw64-runtime` to be able to get the `pthread` libraries^[\[5\]](#cite_note-5)^, needed to build `gcc` with the `posix` thread model (see [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")):

`root `[`#`]`echo "cross-x86_64-w64-mingw32/mingw64-runtime libraries idl tools" > /etc/portage/package.use/cross-x86_64-w64-mingw32`

Then we re-emerge it:

`root `[`#`]`emerge --oneshot cross-x86_64-w64-mingw32/mingw64-runtime`

And finally re-emerge `gcc` so it will finally have the `posix` threading model

`root `[`#`]`emerge --oneshot cross-x86_64-w64-mingw32/gcc`

Future updates of `cross-x86_64-w64-mingw32/gcc` will remain posix, and `cross-x86_64-w64-mingw32/mingw64-runtime` will keep the needed `libraries idl tools` use flag toggles, since we updated properly the environment variables in [/etc/portage/env], [/etc/portage/package.env], and [/etc/portage/package.use].

After the compilation, check that the thread model is posix by calling the cross-compiler binary with the -v flag.

`user `[`$`]`x86_64-w64-mingw32-gcc -v`

    [..]
    Thread model: posix
    [..]

##### [i686 toolchain]

For `i686` a small performance improvement can be made to exception handling^[\[6\]](#cite_note-6)^, the compiled list of the commands being the following

[CODE]

    crossdev --target cross-i686-w64-mingw32
    crossdev --genv 'EXTRA_ECONF="--enable-threads=posix --disable-sjlj-exceptions --with-dwarf2"' \
    --init-target --target cross-i686-w64-mingw32
    echo "cross-i686-w64-mingw32/mingw64-runtime libraries idl tools" > /etc/portage/package.use/cross-i686-w64-mingw32
    emerge --oneshot cross-i686-w64-mingw32/mingw64-runtime
    emerge --oneshot cross-i686-w64-mingw32/gcc

##### [How to link with cross-compiler toolchain]

I cross-compiled a C++ program that used sqlite, fftw and glfw. The first two packages can be generated using emerged. I define the following USE flags in /usr/x86_64-w64-mingw32/etc/portage/package.use

[CODE]

    dev-db/sqlite -readline -debug -doc -icu -secure-delete static-libs -tcl -test -tools
    sci-libs/fftw -altivec -doc -fortran -mpi -neon -openmp -quad static-libs -test -threads -zbus

For ease of installation I prefer to statically linked cross-compiles binaries. Otherwise the binaries must be packaged with additional dll files.

The sqlite and fftw library can be cross compiled like this:

`root `[`#`]`cat /usr/x86_64-w64-mingw32/etc/portage/package.use|cut -d " " -f 1|grep -v "#" |xargs x86_64-w64-mingw32-emerge`

Unfortunately, Gentoo\'s portage system does not allow to cross-compile glfw without X11 dependencies. I therefore compiled this library from source:

`user `[`$`]`cmake -DCMAKE_TOOLCHAIN_FILE=CMake/x86_64-w64-mingw32.cmake -DCMAKE_BUILD_TYPE=Release -DGLFW_BUILD_DOCS=OFF -DGLFW_BUILD_EXAMPLES=OFF -DGLFW_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=/usr/x86_64-w64-mingw32/usr ..`

The flags for linking the mostly static binary are:

[CODE]

    LDFLAGS=-L/usr/x86_64-w64-mingw32/usr/lib \
    -l:libglfw3.a \
    -l:libfftw3f.a \
    -l:libsqlite3.a \
    -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 \
    -lopengl32 \
    -lws2_32 \
    -static-libgcc \
    -static-libstdc++

Note that the colon in -l:libsqlite3.a instructs the linker to use the static library file.

I didn\'t find a way to statically link with libwinpthread. I have to deliver the binary together with /usr/x86_64-w64-mingw32/usr/bin/libwinpthread-1.dll

#### [Porting POSIX threads to Windows]

Windows thread functions seem to work fine with MinGW. The following example code will compile without error:

[FILE] **`win32_threads.c`**

    #include <windows.h>
    #include <stdio.h>
    #include <stdlib.h>

    #define NUM_THREADS 5

    DWORD print_hello(LPVOID lpdwThreadParam);

    int main(int argc, char *argv[])
        else
      }

      exit(EXIT_SUCCESS);
    }

    /* Thread routine */
    DWORD print_hello(LPVOID lpdwThreadParam)

Compile with:

`user `[`$`]`i686-w64-mingw32-gcc -o win32_threads.exe win32_threads.c`

(The call to `Sleep()` will make the thread creation a little more closer to POSIX, more in order, and there will not be duplicate runs.)

However, many applications rely upon POSIX threads and do not have code for Windows thread functionality. The [POSIX Threads for Win32](http://sourceware.org/pthreads-win32/) project provides a library for using POSIX thread-like features on Windows (rather than relying upon Cygwin). It basically wraps POSIX thread functions to Win32 threading functions (`pthread_create()`-\>`CreateThread()` for example). Be aware that not [everything](http://msdn.microsoft.com/en-us/library/ms684847%28VS.85%29.aspx) is implemented on either end (however do note that Chrome uses this library for threading on Windows). Regardless, many ported applications to Windows end up using POSIX Threads for Win32 because of convenience. This library can provide the best of both worlds as Windows thread functions work fine as show above.

To get Pthreads for Win32:

1.  Go to the [Sourceware FTP](ftp://sourceware.org/pub/pthreads-win32/dll-latest/include/) and download the header files to the includes directory for MinGW (for me this is `/usr/i686-w64-mingw32/usr/include`).
2.  Go to the [Sourceware FTP](ftp://sourceware.org/pub/pthreads-win32/dll-latest/lib/) and download only the .a files to the lib directory for MinGW (for me this is `/usr/i686-w64-mingw32/usr/lib`).\'
3.  At the same directory, get the DLL files (only **pthreadGC2.dll** and **pthreadGCE2.dll**; others are for Visual Studio) and place them in the bin directory of the MinGW root (for me this is `/usr/i686-w64-mingw32/usr/bin`).

Example POSIX threads code:

[FILE] **`win32_posix_threads.c`**

    #include
    #include <stdio.h>
    #include <stdlib.h>

    #define NUM_THREADS 5

    void *print_hello(void *thread_id)

    int main(int argc, char *argv[])
      }

      pthread_attr_destroy(&attr);
      for (i = 0; i < NUM_THREADS; i++)
        printf("Completed join with thread %d, status = %d\n", i, status);
      }
      pthread_exit(NULL);

      exit(EXIT_SUCCESS);
    }

Compile with:

`user `[`$`]`i686-w64-mingw32-gcc -o posix_threads.exe -mthreads posix_threads.c -lpthreadGC2`

** Warning**\
It\'s very important that `-lpthreadGC2` or `-lpthreadGCE2` is at the **end** of the command.

With `i686-w64-mingw32-objdump -p posix_threads.exe` we can see that we need [pthreadGC2.dll]. If linked with -lpthreadGCE2 (exception handling POSIX threads), [mingwm10.dll], [pthreadGCE2.dll], and possibly [libgcc_s_sjlj-1.dll] will be required (last one only not compiled with `CFLAG` `-static-libgcc` with [g++]).

Copy the DLL file(s) required to the directory and test with Wine. For example:

`user `[`$`]`cp /usr/i686-w64-mingw32/usr/bin/pthreadGC2.dll . `

`user `[`$`]`wine posix_threads.exe `

If all goes well, the output should be similar to the following:

    In main: creating thread 0
    In main: creating thread 1
    Thread #0 responding.
    In main: creating thread 2
    Thread #1 responding.
    In main: creating thread 3
    Thread #2 responding.
    In main: creating thread 4
    Thread #3 responding.
    Thread #4 responding.
    Completed join with thread 0, status = 0
    Completed join with thread 1, status = 0
    Completed join with thread 2, status = 0
    Completed join with thread 3, status = 0
    Completed join with thread 4, status = 0

** Note**\
Is is probably a good idea to include `-mthreads` as a `CFLAGS` value for any code that relies on thread-safe exception handling. From the man page:

-   `-mthreads` - Support thread-safe exception handling on MinGW 32. Code that relies on thread-safe exception handling must compile and link all code with the -mthreads option. When compiling, -mthreads defines:
-   `-D_MT`; when linking, it links in a special thread helper library
-   `-lmingwthrd` which cleans up per thread exception handling data.

### [][Wine and %PATH%]

Like Windows, Wine supports environment variables. It is possible to specify the path of DLLs (for example, the MinGW bin directory) in the registry at `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment` (for me this value would be `Z:\usr\i686-w64-mingw32\usr\bin`). This isn\'t particularly recommend as it could be omitted to distribute DLLs with the application binaries.

### [No need for -lm]

If `#include <math.h>` is coded, and any of its functions are used, there is no need to link with the standard C math library using the `-lm` switch with [gcc] or [].

### [DirectX]

DirectX 9 headers and libs are included. Link with `-ldx9`. For the math functions (such as `MatrixMult`, unlike Windows, it is needed to dynamically link with `-ld3dx9d` and then include [d3dx9d.dll] (this file SHOULD be got from Microsoft\'s SDK). This is the same for DirectX 8.

There is no support for DirectX 10 or 11 yet. Minimal support for Direct2D has been implemented via a patch (search the official mailing list of MinGW).

## [Removal]

`root `[`#`]`crossdev -C i686-w64-mingw32`

If files are left over (such as libraries and things that have been added), a prompt will occur to remove the [/usr/i686-w64-mingw32] directory recursively.

## [Troubleshooting]

### [][Emerging a toolchain failed with error: Missing digest for \*.ebuild]

Add the following to the crossdev overlay metadata:

[FILE] **`layout.conf`**

    thin-manifests = true

## [External resources]

-   [Compile for Windows on Linux \[BLOGCOMPILER](https://web.archive.org/web/20181218213125/http://www.blogcompiler.com/2010/07/11/compile-for-windows-on-linux/)\] - Generic introduction to cross-compiling windows binaries.
-   [MinGW Hello World \[mingw-cross.sourceforge\]](http://mingw-cross.sourceforge.net/hello_win32api.html) - \"Hello World\" binary guide.
-   [GCC and Make Compiling, Linking and Building C/C++ Applications \[ntu.edu\]](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html) - C/C++ based GCC overview.
-   [MinGW/MSYS development environment](http://ingar.satgnu.net/devenv/mingw32/base.html) - Setting up a MinGW/MSYS base system.

## [References]

1.  [[↑ ^[1.0](#cite_ref-gcc55886_1-0)^ ^[1.1](#cite_ref-gcc55886_1-1)^] [[https://gcc.gnu.org/bugzilla/show_bug.cgi?id=55886](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=55886)]]
2.  [[[↑](#cite_ref-2)] [[[[Bug 620464]](https://bugs.gentoo.org/show_bug.cgi?id=620464#c7)[]]Crossdev of Mingw (both i686-w64-mingw32 and x86_64-w64-mingw32) fail in stage2 because ld does not recognize -z]]
3.  [[[↑](#cite_ref-3)] [[MinGW Hello World](http://mingw-cross.sourceforge.net/hello_win32api.html), \"Hello World\" binary guide]]
4.  [[[↑](#cite_ref-4)] [[\[1\]](https://github.com/doitsujin/dxvk)]]
5.  [[[↑](#cite_ref-5)] [[Bug report giving out the information](https://bugs.gentoo.org/631460)]]
6.  [[[↑](#cite_ref-6)] [[\[2\]](https://github.com/brechtsanders/winlibs_mingw/issues/20#issuecomment-650259935)]]