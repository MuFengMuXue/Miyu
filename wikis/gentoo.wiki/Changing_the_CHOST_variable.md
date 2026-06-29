Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/de "Changing the CHOST variable/de (8% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/es "Cambiar la variable CHOST (25% translated)")
-   [français](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/fr "Changer la variable CHOST (17% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/hu "A CHOST változó megváltoztatása (86% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/ru "Изменение переменной CHOST (83% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/zh-cn "改变CHOST变量 (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/ja "CHOSTの変更 (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable/ko "Changing the CHOST variable (19% translated)")

This document explains how to change the [`CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST") variable of an existing system.

Changing the `CHOST` is a big issue that can seriously screw up a system - so why is there a guide for that if it can cause that much havoc?

There are certain situations where changing the `CHOST` variable is inevitable. Most of them should never be necessary in normal operations (e.g., because they involve bootstrapping for a new architecture). Sometimes however\... As an example, switching profile may involve a change of `CHOST`, e.g., in the case of the upgrade of MIPS machines from the 17.0 to the 23.0 profiles, because we are adapting our settings to common standards.

Even after following the instructions here, problems may arise, so please make sure to read and execute them very carefully. In this example the `CHOST` variable will be changed from mips64-unknown-linux-gnu to mips64-unknown-linux-gnuabin32. Please change the commands according to the specific situation.

## Contents

-   [[1] [Updating make.conf]](#Updating_make.conf)
-   [[2] [Building the packages]](#Building_the_packages)
    -   [[2.1] [The Toolchain]](#The_Toolchain)
    -   [[2.2] [The C Standard Library]](#The_C_Standard_Library)
-   [[3] [Verifying things work]](#Verifying_things_work)
-   [[4] [Finishing the change]](#Finishing_the_change)
-   [[5] [Common problems]](#Common_problems)
-   [[6] [Feedback]](#Feedback)

## [[] Updating make.conf]

To start out with the `CHOST` variable change, edit the [/etc/portage/make.conf] file and add/change the `CHOST` value to suit the requirements.

[FILE] **`/etc/portage/make.conf`**

    CHOST="mips64-unknown-linux-gnuabin32"

Note that profiles provide a default setting for `CHOST`; depending on the situation, it may be necessary to override it in [/etc/portage/make.conf] or remove an override in [/etc/portage/make.conf]. In any case, the important point is that the effective value changes.

Please note that if planning to use another value of CHOST than the profile default, the *CHOST\_\$* variable may need updating as well. It is possible to query the value of this variable of the currently set profile with the *portageq* tool:

`user `[`$`]`portageq envvar ABI`

    n32

`user `[`$`]`portageq envvar CHOST_n32`

    mips64-unknown-linux-gnuabin32

If this value is equal to CHOST, it\'s good. Otherwise, override it as well, e.g.:

[FILE] **`/etc/portage/make.conf`**

    CHOST_n32="mips64-unknown-linux-gnuabin32"

## [[] Building the packages]

** Important**\
It is generally a good idea to rebuild the packages **to the same versions** as before the CHOST switch, i.e. avoiding combining upgrades with it. If multiple slots are installed, either uninstall extraneous slots or rebuild all of them. If that is not possible, please upgrade the packages first (with old CHOST). While it may not be impossible to do so, it is hard to predict which potential problems may arise and almost impossible to document them in this guide.

** Important**\
If the CHOST switch takes place together with other changes, e.g. in the course of a profile upgrade, please read the documentation there as well to make sure the different steps do not interfere.

Rebuild the following packages in this order:

### [The Toolchain]

For GCC-based systems:

`root `[`#`]`emerge --ask --oneshot sys-devel/binutils`

** Note**\
It may be necessary to run [binutils-config] before compiling gcc.

`root `[`#`]`emerge --ask --oneshot sys-devel/gcc`

For LLVM-based systems:

** Note**\
This is for systems which use LLVM/Clang as a system compiler and have no GCC at all, which is an unsupported configuration for advanced users only. If you are not absolutely certain you fit into this category, follow the GCC-based systems path above instead.

`root `[`#`]`emerge --ask --oneshot llvm-core/llvm`

`root `[`#`]`emerge --ask --oneshot llvm-core/clang`

`root `[`#`]`emerge --ask --oneshot llvm-core/clang-common`

Install the rest of the toolchain as in [Clang/Bootstrapping](https://wiki.gentoo.org/wiki/Clang/Bootstrapping "Clang/Bootstrapping").

### [The C Standard Library]

For glibc based systems:

`root `[`#`]`emerge --ask --oneshot sys-libs/glibc`

For musl based systems:

`root `[`#`]`emerge --ask --oneshot sys-libs/musl`

## [[] Verifying things work]

Now it is time to make sure that the [gcc-config] and [binutils-config] settings are sane and that there are no leftovers in [/etc/env.d/].

The output of [gcc-config] and [binutils-config] should look like the following:

** Note**\
The output may, or even will differ according to the gcc version and `CHOST` settings. The example below uses gcc 12 on mips.

`root `[`#`]`gcc-config -l`

     [1] mips64-unknown-linux-gnuabin32-12 *

`root `[`#`]`gcc-config -c`

    mips64-unknown-linux-gnuabin32-12

`root `[`#`]`binutils-config -l`

     [1] mips64-unknown-linux-gnuabin32-2.39 *
    # binutils-config -c
    mips64-unknown-linux-gnuabin32-2.39

Next, check to see if there are references to the old `CHOST` variable in [/etc/env.d/]:

`root `[`#`]`cd /etc/env.d/ `

`root `[`#`]`grep linux-gnu *`

    04gcc-mips64-unknown-linux-gnu:MANPATH="/usr/share/gcc-data/mips64-unknown-linux-gnu/12/man"
    04gcc-mips64-unknown-linux-gnu:INFOPATH="/usr/share/gcc-data/mips64-unknown-linux-gnu/12/info"
    04gcc-mips64-unknown-linux-gnuabin32:MANPATH="/usr/share/gcc-data/mips64-unknown-linux-gnuabin32/12/man"
    04gcc-mips64-unknown-linux-gnuabin32:INFOPATH="/usr/share/gcc-data/mips64-unknown-linux-gnuabin32/12/info"
    05binutils:MANPATH=/usr/share/binutils-data/mips64-unknown-linux-gnuabin32/2.39/man
    05binutils:INFOPATH=/usr/share/binutils-data/mips64-unknown-linux-gnuabin32/2.39/info

Here, binutils is fine - there is one file, and it only contains references to the new `CHOST`. For gcc, there is a file for both the new and the old `CHOST` value, so delete the old stale one:

`root `[`#`]`rm 04gcc-mips64-unknown-linux-gnu`

The same also applies to [binutils] - if there\'s an extra one, see which is the outdated one and delete it. Next, check the contents of [/etc/env.d/binutils/]:

`root `[`#`]`cd /etc/env.d/binutils/ `

`root `[`#`]`ls -l`

    total 12
    -rw-r--r-- 1 root root  13 Dec  9 22:16 config-mips64-unknown-linux-gnu
    -rw-r--r-- 1 root root  13 Dec 31 17:00 config-mips64-unknown-linux-gnuabin32
    -rw-r--r-- 1 root root 117 Dec 31 16:59 mips64-unknown-linux-gnuabin32-2.39

`root `[`#`]`cat config-mips64-unknown-linux-gnuabin32`

    CURRENT=2.39

`root `[`#`]`cat mips64-unknown-linux-gnuabin32-2.39`

    TARGET="mips64-unknown-linux-gnuabin32"
    VER="2.39"
    LIBPATH="/usr/lib32/binutils/mips64-unknown-linux-gnuabin32/2.39"

There\'s one stale file with the old CHOST, config-mips64-unknown-linux-gnu, so delete this one.

`root `[`#`]`rm config-mips64-unknown-linux-gnu`

Time to move on to the [gcc/] directory.

`root `[`#`]`cd /etc/env.d/gcc`

    # ls -l
    total 12
    -rw-r--r-- 1 root root  36 Dec 30 11:31 config-mips64-unknown-linux-gnu
    -rw-r--r-- 1 root root  42 Dec 31 23:54 config-mips64-unknown-linux-gnuabin32
    -rw-r--r-- 1 root root 353 Dec 31 23:52 mips64-unknown-linux-gnuabin32-12

`root `[`#`]`cat config-mips64-unknown-linux-gnuabin32`

    CURRENT=mips64-unknown-linux-gnuabin32-12

`root `[`#`]`cat config-mips64-unknown-linux-gnu`

    CURRENT=mips64-unknown-linux-gnu-12

`root `[`#`]`cat mips64-unknown-linux-gnuabin32-12`

    GCC_PATH="/usr/mips64-unknown-linux-gnuabin32/gcc-bin/12"
    LDPATH="/usr/lib/gcc/mips64-unknown-linux-gnuabin32/12"
    MANPATH="/usr/share/gcc-data/mips64-unknown-linux-gnuabin32/12/man"
    INFOPATH="/usr/share/gcc-data/mips64-unknown-linux-gnuabin32/12/info"
    STDCXX_INCDIR="g++-v12"
    CTARGET="mips64-unknown-linux-gnuabin32"
    GCC_SPECS=""
    MULTIOSDIRS="../lib32"

[config-mips64-unknown-linux-gnuabin32] and [mips64-unknown-linux-gnuabin32-12] are fine, but [config-mips64-unknown-linux-gnu] is another leftover that needs removal.

** Note**\
Again, the name of the file containing references to an outdated gcc version may have a different name. It is important to identify the file on its content, not only the name.

`root `[`#`]`rm config-mips64-unknown-linux-gnu`

Now run the following commands to update the environment:

`root `[`#`]`env-update && source /etc/profile`

Next, verify everything is fixed in /etc/env.d. If there are still files found, try to track it down before going on.

If you\'re also using clang to build certain packages on a GCC system, you also need to edit /etc/clang/gentoo-gcc-install.cfg

`root `[`#`]`cat /etc/clang/gentoo-gcc-install.cfg`

    # This file is maintained by gcc-config.
    # It is used to specify the selected GCC installation.
    --gcc-install-dir="/usr/lib/gcc/mips64-unknown-linux-gnu/14"
    --gcc-install-dir="/usr/lib/gcc/mips64-unknown-linux-gnu/14"

And replace mips64-unknown-linux-gnu with mips64-unknown-linux-gnuabin32.

## [[] Finishing the change]

Now it is necessary to re-emerge [[[sys-devel/libtool]](https://packages.gentoo.org/packages/sys-devel/libtool)[]]:

`root `[`#`]`emerge --ask --oneshot libtool`

It is now possible to rebuild all the packages:

`root `[`#`]`emerge --ask --emptytree @world`

In theory, it should not be necessary to do so, but it cannot be 100% guaranteed that this is actually the case. Alternatively, it is possible to manually rebuild all the known problematic packages:

-   multilib packages using CHOST prefixing or header wrapping,
-   Perl, Python and other tools that store configured compiler path.

`root `[`#`]`emerge --ask --oneshot /usr/bin/mips64-unknown-linux-gnu-* /usr/include/mips64-unknown-linux-gnu /usr/lib/llvm/*/bin/mips64-unknown-linux-gnu-* dev-lang/perl dev-lang/python`

Note that paths that do not apply to the current system may need removing from the above invocation.

When encountering other packages that need recompiling, please let us know through the [discussion page](https://wiki.gentoo.org/wiki/Talk:Changing_the_CHOST_variable "Talk:Changing the CHOST variable") of this guide.

## [[] Common problems]

Not so many anymore. Usually this just works, as long as no really exotic change is done. Make sure to not combine the CHOST change with other steps though. Some of the notes below are really old\...

When upgrading from gcc 3.3 to 4.1 at the same time as changing the `CHOST` variable (please don\'t do that anyway), a couple of users reported broken packages that need recompiling, such as [[[sys-apps/groff]](https://packages.gentoo.org/packages/sys-apps/groff)[]] and [[[mail-mta/courier]](https://packages.gentoo.org/packages/mail-mta/courier)[]]:

[CODE] **Error message**

    error while loading shared libraries: libstdc++.so.5: cannot open shared object file: No such file or directory

This happens because during the upgrade, the `CHOST` variable doesn\'t exactly match the `CTARGET` variable value, making the compiler assume that the system is using cross-compiling. As a consequence, `LDPATH` isn\'t inserted into [ld.so.conf], resulting in this error.

Please see the [GCC upgrade guide](https://wiki.gentoo.org/wiki/Upgrading_GCC "Upgrading GCC") for what needs to be rebuilt after a GCC upgrade.

In some rare cases, this can break old versions of python, too. This may be fixed by adding [/usr/lib/gcc-lib/i386-pc-linux-gnu/3.3.6] (change accordingly to the old `CHOST` and gcc version) to [/etc/ld.so.conf], running [ldconfig] and then [emerge libstdc++-v3]. However, as can be seen, this situation needs to be avoided - don\'t change `CHOST` and gcc at the same time.

## [[] Feedback]

That should be all, feedback (both if it worked, failed or other problems were encountered) is welcome, please use the [discussion page](https://wiki.gentoo.org/wiki/Talk:Changing_the_CHOST_variable "Talk:Changing the CHOST variable") or post to [this forum thread](https://forums.gentoo.org/viewtopic-t-494147.html). Much in this guide comes from vapier, thanks for the help!

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Wernfried Haas, [Mike Frysinger (vapier)](https://wiki.gentoo.org/wiki/User:Vapier "User:Vapier") , Chris White**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*