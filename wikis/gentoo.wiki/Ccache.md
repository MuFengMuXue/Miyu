This page contains [[changes](https://wiki.gentoo.org/index.php?title=Ccache&diff=1404557)] which are not marked for translation.

\

**Resources**

[[]][Home](https://ccache.dev/)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/ccache)

[[]][GitHub](https://github.com/ccache/ccache)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ccache "wikipedia:Ccache")

[ccache] helps avoid repeated recompilation for the same C and C++ object files by fetching the result from a cache directory.

A compiler cache is can be useful for:

-   Developers who rebuild the same/similar codebase multiple times and use [[/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches")] to test patches.
-   Users who frequently play with USE-flag changes and end up rebuilding the same packages multiple times.
-   Users who use [live ebuilds](https://wiki.gentoo.org/wiki/Ebuild#Live_ebuilds "Ebuild") extensively.
-   Installing very big ebuilds, such as [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") or [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice"), without fear of losing multiple hours of code compilation due to a failure.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Initial setup]](#Initial_setup)
    -   [[2.2] [Enabling ccache for certain packages]](#Enabling_ccache_for_certain_packages)
    -   [[2.3] [ccache.conf]](#ccache.conf)
    -   [[2.4] [Compression]](#Compression)
-   [[3] [Man page]](#Man_page)
-   [[4] [General notes]](#General_notes)
-   [[5] [Useful variables and commands]](#Useful_variables_and_commands)
-   [[6] [Gentoo specifics/gotchas]](#Gentoo_specifics.2Fgotchas)
    -   [[6.1] [gcc is a wrapper]](#gcc_is_a_wrapper)
-   [[7] [Caveats]](#Caveats)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/ccache](https://packages.gentoo.org/packages/dev-util/ccache) [[]] [Fast compiler cache]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+static-c++`](https://packages.gentoo.org/useflags/+static-c++)   Avoid dynamic dependency on gcc\'s libstdc++.
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`http`](https://packages.gentoo.org/useflags/http)                 Enable HTTP backend for storage via dev-cpp/cpp-httplib
  [`redis`](https://packages.gentoo.org/useflags/redis)               Enable Redis backend for storage via dev-libs/hiredis
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-29 05:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[dev-util/ccache]](https://packages.gentoo.org/packages/dev-util/ccache)[]]:

`root `[`#`]`emerge --ask dev-util/ccache`

## [Configuration]

### [Initial setup]

** Warning**\
Using ccache globally is not recommended as it will saturate the cache and have few cache hits! Enable it instead for specific packages.

Simply enable [ccache] support in [make.conf]:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="ccache"

    # Portage defaults to $/ccache unless CCACHE_DIR is
    # set in make.conf or in /etc/portage/env (or similar).
    #CCACHE_DIR="/var/cache/ccache"
    # If using a directory that Portage doesn't control, e.g. /var/cache/ccache,
    # this may be needed in some cases, but has some security implications.
    # See https://bugs.gentoo.org/492910.
    #CCACHE_UMASK="0002"

Done! From now on, all builds will try to reuse object files from the cache.

### [Enabling ccache for certain packages]

See [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")].

### [ccache.conf]

ccache will search [/etc/ccache.conf] as well as [\$/ccache.conf] for its configuration file.

Example config:

[FILE] **`/etc/ccache.conf`**

    # Maximum cache size to maintain
    max_size = 100.0G

    # Allow others to run 'ebuild' and share the cache.
    umask = 002

    # Don't include the current directory when calculating
    # hashes for the cache. This allows re-use of the cache
    # across different package versions, at the cost of
    # slightly incorrect paths in debugging info.
    # https://ccache.dev/manual/4.4.html#_performance
    hash_dir = false

    # Preserve cache across GCC rebuilds and
    # introspect GCC changes through GCC wrapper.
    #
    # We use -dumpversion here instead of -v,
    # see https://bugs.gentoo.org/872971.
    compiler_check = %compiler% -dumpversion

    # Logging setup is optional
    # Portage runs various phases as different users
    # so beware of setting a log_file path here: the file
    # should already exist and be writable by at least
    # root and portage. If a log_file path is set, don't
    # forget to set up log rotation!
    # log_file = /var/log/ccache.log
    # Alternatively, log to syslog
    # log_file = syslog

### [Compression]

ccache can compress its content. To enable and set the [zstd](https://wiki.gentoo.org/wiki/Zstd "Zstd") compression level^[\[1\]](#cite_note-1)^, edit [ccache.conf]:

[FILE] **`/etc/ccache.conf`**

    compression = true
    compression_level = 1

## [Man page]

The manual page for [[[dev-util/ccache]](https://packages.gentoo.org/packages/dev-util/ccache)[]] (see [man ccache]) is a great source of various knobs to make caching more robust and aggressive.

## [General notes]

** Note**\
This section is for using ccache outside of Portage and ebuilds.

[ccache] works by prepending [/usr/lib/ccache/bin] to `PATH` variable:

`user `[`$`]`ls -l /usr/lib/ccache/bin`

    ...
    c++ -> /usr/bin/ccache
    c99 -> /usr/bin/ccache
    x86_64-pc-linux-gnu-c++ -> /usr/bin/ccache
    ...

`FEATURES="ccache"` triggers the same behavior in Portage.

[ccache] may also be enabled for the current user and reuse the same cache directory:

[FILE] **`~/.bashrc`**

    export PATH="/usr/lib/ccache/bin$$"
    export CCACHE_DIR="/var/tmp/ccache"

## [Useful variables and commands]

Some variables:

-   Variable `CCACHE_DIR` points to cache root directory.
-   Variable `CCACHE_RECACHE` allows evicting old cache entries with new entries:

`root `[`#`]`CCACHE_RECACHE=yes emerge --oneshot cat/pkg`

See [man ccache] for many more variables.

Some commands:

-   To show cache hit statistics:

`user `[`$`]`CCACHE_DIR=/var/tmp/ccache ccache -s`

    Cacheable calls:   3188 /  3412 (93.43%)
      Hits:            1642 /  3188 (51.51%)
        Direct:        1642 /  1642 (100.0%)
        Preprocessed:     0 /  1642 ( 0.00%)
      Misses:          1546 /  3188 (48.49%)
    Uncacheable calls:  224 /  3412 ( 6.57%)
    Local storage:
      Cache size (GB):  0.1 / 100.0 ( 0.05%)
      Hits:            1642 /  3188 (51.51%)
      Misses:          1546 /  3188 (48.49%)

-   To drop all caches:

`user `[`$`]`CCACHE_DIR=/var/tmp/ccache/ ccache -C`

See [man ccache] for many more commands.

## [][Gentoo specifics/gotchas]

### [[gcc] is a wrapper]

To pass through a binary, the following entry is suggested for [ccache.conf]:

[FILE] **`ccache.conf`**

    compiler_check = %compiler% -v

Also, `-v` has a nice side-effect of not invalidating the cache if compiler itself was rebuilt without version changes.

## [Caveats]

Before using advanced [ccache] options, make sure it\'s understood what is being used as a cache key by [ccache]. By default these are:

-   Timestamp and size of a compiler binary (beware of shell and binary wrappers)
-   Compiler options used
-   Contents of a source file
-   Contents of all include files used for compilation

For more detailed information about caveats to ccache usage, refer to [the ccache manual](https://ccache.dev/manual/4.8.1.html#_caveats).

## [See also]

-   [Handbook:AMD64/Working/Features#Caching_compilation_objects](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features#Caching_compilation_objects "Handbook:AMD64/Working/Features") --- about ccache in Handbook
-   [Sccache](https://wiki.gentoo.org/wiki/Sccache "Sccache") --- helps avoid repeated recompilation for the same C, C++, and [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") object files by fetching result from a cache directory.

## [External resources]

-   [Optimizing ccache using per-package caches](https://blogs.gentoo.org/mgorny/2017/07/23/optimizing-ccache-using-per-package-caches/)

## [References]

1.  [[[↑](#cite_ref-1)] [[CCACHE(1)](https://ccache.dev/manual/4.2.html#_cache_compression), ccache.dev. Retrieved on December 21, 2024]]