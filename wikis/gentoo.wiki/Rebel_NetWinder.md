Little-endian ARMv4 based network server from Rebel.

## Contents

-   [[1] [Rebel NetWinder]](#Rebel_NetWinder)
-   [[2] [/proc/cpuinfo]](#.2Fproc.2Fcpuinfo)
-   [[3] [Cross compile preparation]](#Cross_compile_preparation)
-   [[4] [External resources]](#External_resources)

## [Rebel NetWinder]

Board specifications:

[CODE]

    # DEC/Intel StrongARM 110 processor, ~233MHz
    # DEC/Intel 21285 FootBridge chipset
    # 32/64/128MB RAM
    # Intergraphics Systems CyberPro 2000A graphics chip with 2MB RAM, VGA output
    # WinBond 553 IDE controller
    # RockWell WaveArtist audio chip
    # Philips 7111 video capture/WinBond 9660 TV Encoder
    # 1x WinBond 940 10BaseT Ethernet controller
    # 1x Digital 21143(Tulip) 10/100BaseT Ethernet controller

## [][/proc/cpuinfo]

CPU info:

[FILE] **`/proc/cpuinfo`**

    Code Listing 2.1: CPU Info
    Processor       : StrongARM-110 rev 4 (v4l)
    BogoMIPS        : 185.54
    Features        : swp half 26bit fastmult
    CPU implementer : 0x44
    CPU architecture: 4
    CPU variant     : 0x0
    CPU part        : 0xa10
    CPU revision    : 4

    Hardware        : Rebel-NetWinder
    Revision        : 59ff
    Serial          : 0000000000000000

## [Cross compile preparation]

Setup:

`root `[`#`]`emerge --ask crossdev`

`root `[`#`]`crossdev armv4l-unknown-linux-gnu`

Emerge wrapper:

[FILE] **`netwinder-merge`**

    #!/bin/sh

    CHOST=armv4l-unknown-linux-gnu

    #export CBUILD=$(portageq envvar CBUILD)
    export SYSROOT="/usr/$"
    export PORTAGE_CONFIGROOT="/usr/$"

    # optional exports
    export enable_malloc0returnsnull=yes \
            ac_cv_file__usr_share_sgml_X11_defs_ent=1 \
            ac_cv_func_setpgrp_void=yes ac_cv_func_setgrent_void=yes \
            ac_cv_func_calloc_0_nonnull=yes ac_cv_func_malloc_0_nonnull=yes \
            gl_cv_func_malloc_0_nonnull=yes ac_cv_func_realloc_0_nonnull=yes \
            ac_cv_func_memcmp_working=yes ac_cv_func_strnlen_working=yes

    # optional export for glib:2
    export glib_cv_uscore=no glib_cv_stack_grows=no \
            glib_cv_stack_grows=no  glib_cv_has__inline=yes \
            glib_cv_has__inline__=yes glib_cv_hasinline=yes \
            glib_cv_sane_realloc=yes glib_cv_va_copy=yes \
            glib_cv___va_copy=yes glib_cv_va_val_copy=no \
            glib_cv_rtldglobal_broken=no glib_cv_uscore=no \
            ac_cv_func_posix_getpwuid_r=yes \
            ac_cv_func_posix_getgrgid_r=yes \
            ac_cv_header_pwd_h=yes \
            ac_cv_func_getpwuid_r=yes \
            glib_cv_sizeof_gmutex=40

    FAKEROOT=
    if [[ $(id -u) != 0 ]]; then
        if [[ $(type -p fakeroot) != "" ]]; then
            FAKEROOT=fakeroot
        fi
    fi

    $ emerge -q "$@"

[FILE] **`/usr/armv4l-unknown-linux-gnu/etc/make.conf`**

    CHOST=armv4l-unknown-linux-gnu
    CBUILD=x86_64-pc-linux-gnu
    ARCH="arm"
    ROOT=/usr/$/
    ACCEPT_KEYWORDS="arm ~arm"
    USE="$ zlib bindist make-symlinks minimal \
            input_devices_keyboard input_devices_evdev \
            video_cards_fbdev video_cards_dummy"

    VIDEO_CARDS="fbdev dummy"

    INPUT_DEVICES="evdev keyboard mouse touchscreen"
    USE_EXPAND="video_cards input_devices"
    MARCH_TUNE="-mcpu=strongarm110"
    CFLAGS="-Os -pipe $ -fomit-frame-pointer -I$/usr/include/ -I$/include/"

    CXXFLAGS="$"
    LDFLAGS="-L$/usr/lib -L$/lib"

    PKG_CONFIG_PATH="$/usr/lib/pkgconfig/"
    MAKEOPTS="-j8"
    FEATURES="-collision-protect sandbox buildpkg noman noinfo nodoc"

    PORTDIR_OVERLAY="/usr/portage/local/"
    PKGDIR=$/packages/
    PORTAGE_TMPDIR=$/tmp/
    PORTAGE_WORKDIR_MODE=2775
    PORTAGE_ECLASS_WARNING_ENABLE=0

    CLEAN_DELAY=0
    EPAUSE_IGNORE=1
    EBEEP_IGNORE=1

## [External resources]

-   [NetWinder.org](http://www.netwinder.org/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Mike Frysinger, Ned Ludd, Robin H. Johnson, Alex Tarkovsky, Alexey Shvetsov, Raúl Porcel, Joshua Saddler on April 28, 2013.**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*