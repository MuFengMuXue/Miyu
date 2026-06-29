**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

This document guides users through the process of upgrading GCC up to version 4.1.x.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [GCC Upgrading]](#GCC_Upgrading)
-   [[2] [General Upgrade Instructions]](#General_Upgrade_Instructions)
    -   [[2.1] [Introduction]](#Introduction_2)
-   [[3] [Upgrading from GCC-3.3 to 3.4]](#Upgrading_from_GCC-3.3_to_3.4)
    -   [[3.1] [Introduction]](#Introduction_3)
    -   [[3.2] [The Choices]](#The_Choices)
    -   [[3.3] [Using revdep-rebuild]](#Using_revdep-rebuild)
    -   [[3.4] [Using emerge -e]](#Using_emerge_-e)
-   [[4] [Upgrading to GCC on a First Install]](#Upgrading_to_GCC_on_a_First_Install)
    -   [[4.1] [Introduction]](#Introduction_4)
    -   [[4.2] [Using revdep-rebuild]](#Using_revdep-rebuild_2)
    -   [[4.3] [Using emerge -e]](#Using_emerge_-e_2)
    -   [[4.4] [Cleaning up]](#Cleaning_up)
-   [[5] [Common Pitfalls]](#Common_Pitfalls)
    -   [[5.1] [Frequent Error Messages]](#Frequent_Error_Messages)
-   [[6] [See also]](#See_also)

## [Introduction]

### [GCC Upgrading]

Why should you upgrade? Well, GCC is quite similar to any other package on your system, just a bit more critical. You should upgrade GCC whenever a new version fixes some bug that annoys you, new functionality you need is introduced, or if you want to keep your system up-to-date. If none of the previous cases apply to you, you can safely postpone upgrade as long as your GCC version is supported by Gentoo developers.

If you install a new major version of GCC (such as 3.3.6 to 3.4.5), the system will not switch over to use it automatically. You\'ll have to explicitly request the change because the migration process might require some additional steps. If you decide not to switch, Portage will continue to use older version of your compiler until you change your mind, or remove the old compiler from the system. Non-major GCC upgrades are switched automatically for you (such as 3.4.5 to 3.4.6).

This guide will document the necessary steps required to perform a seamless upgrade of the compiler used by your Gentoo box. A specific section is dedicated to the [#Upgrading_from_GCC-3.3_to_3.4](#Upgrading_from_GCC-3.3_to_3.4) and issues with `libstdc++` . A second specific section is [#Upgrading_to_GCC_on_a_First_Install](#Upgrading_to_GCC_on_a_First_Install) Gentoo using a stage3 tarball, after a new GCC major/minor version has been released.

** Warning**\
It should be noted that upgrading from GCC-3.4 (or 3.3) to GCC-4.1 or greater still requires you to follow these instructions, as GCC-3.4 and GCC-4.1 use slightly different ABIs.

## [General Upgrade Instructions]

### [Introduction]

** Important**\
If you\'re looking for instructions specific to upgrades from GCC-3.3 to GCC-3.4, please consult the section called [#Upgrading_from_GCC-3.3_to_3.4](#Upgrading_from_GCC-3.3_to_3.4) .

** Important**\
If you\'re looking for instructions specific to upgrades in GCC for new installs, please consult the section called [#Upgrading_to_GCC_on_a_First_Install](#Upgrading_to_GCC_on_a_First_Install) .

Generally speaking, upgrades to *bug fix releases* , like from 3.3.5 to 3.3.6, should be quite safe \-- just emerge new version, switch your system to use it and rebuild the only affected package, `libtool` . However, some GCC upgrades break binary compatibility; in such cases a rebuild of the affected packages (or even whole toolchain and system) might be required.

When we spoke about the need to switch your compiler to the newer version by hand, we said it won\'t happen automatically. However, there is one exception \-- upgrades to bug fix releases, like from 3.3.5 to 3.3.6 in case you don\'t use the \"multislot\" feature allowing them to coexist on one system. Multislot is disabled by default as the majority of users won\'t benefit from it.

`root `[`#`]`emerge --ask gcc`

Please substitute \"i686-pc-linux-gnu-4.1.1\" with the GCC version and CHOST settings you\'ve upgraded to:

`root `[`#`]`gcc-config i686-pc-linux-gnu-4.1.1 `

`root `[`#`]`env-update && source /etc/profile`

If you upgraded from GCC 3 to 4 (e.g. from 3.4.6 to 4.1.1 in this example) you will have to run fix_libtool_files.sh manually. Replace \$CHOST with your actual CHOST, found in /etc/portage/make.conf. Replace \<gcc-version\> with your new, updated GCC version.

`root `[`#`]`/usr/share/gcc-data/$CHOST/<gcc-version>/fix_libtool_files.sh 3.4.6`

Now rebuild libtool.

`root `[`#`]`emerge --oneshot -av libtool`

To be completely safe that your system is in a sane state, you *must* rebuild the toolchain and then world to make use of the new compiler.

`root `[`#`]`emerge -eav system `

`root `[`#`]`emerge -eav world`

It is safe to remove the older GCC version at this time. If you feel the need, please issue the following command (as usual, substitute `=sys-devel/gcc-3.4*` with the version you want to uninstall):

`root `[`#`]`emerge -aC =sys-devel/gcc-3.4*`

** Important**\
Please note that the GCC 4.1 and newer can compile only kernels newer than 2.4.34. Don\'t remove your old GCC version if you want to use an older kernel.

** Important**\
In case you\'re upgrading from GCC-3.3, you should run`emerge --oneshot sys-libs/libstdc++-v3` to provide compatibility with older binary C++ applications.

## [Upgrading from GCC-3.3 to 3.4]

### [Introduction]

The upgrade from GCC-3.3 to 3.4 is not seamless as the C++ ABI changed between these two versions. There is an issue with the `libstdc++` library which must be taken care of, as well.

### [The Choices]

** Important**\
If you upgrade from gcc 3.4 to 4.1, please consult the [#General_Upgrade_Instructions](#General_Upgrade_Instructions) .

** Important**\
If you\'re upgrading on a SPARC machine, you will have to take the way of the complete system rebuild due to some internal [ABI changes](http://gcc.gnu.org/gcc-3.4/sparc-abi.html) in GCC\'s parameter passing.

If you upgrade from gcc 3.3 to 3.4, you have two possibilities on how to upgrade your system. The revdep-rebuild method is faster and requires use of the `revdep-rebuild` tool from package `gentoolkit` while the other option rebuilds the entire system from scratch so it will make use of new GCC features. It\'s up to you to decide which of these two ways you will choose. In most cases, the first method is sufficient.

If you upgrade from gcc 3.3 to 4.1, do not use the method based on revdep-rebuild, but rebuild the entire system.

### [Using revdep-rebuild]

This method requires that you first install `gentoolkit` if you have not already done so. Then we will upgrade GCC and switch to the new compiler. We will also rebuild the `libtool` package to ensure that toolchain is in healthy state.

`root `[`#`]`emerge --ask gentoolkit`

`root `[`#`]`emerge --ask gcc`

Please substitute \"i686-pc-linux-gnu-3.4.5\" with the GCC version and CHOST settings you\'ve upgraded to:

`root `[`#`]`gcc-config i686-pc-linux-gnu-3.4.5 `

`root `[`#`]`source /etc/profile`

Now rebuild libtool.

`root `[`#`]`emerge --oneshot -av libtool`

Now, we want to see which packages that revdep-rebuild will want to rebuild. Then we will tell revdep-rebuild to actually rebuild the packages. This may take some time, so have some patience.

`root `[`#`]`revdep-rebuild --library libstdc\+\+.so.5 -- -p -v `

`root `[`#`]`revdep-rebuild --library libstdc\+\+.so.5`

** Note**\
It is possible that you might have problems with non-existing package versions due to them being outdated or masked. If this is the case, you will want to use the `--package-names` option to `revdep-rebuild` . This causes packages to be recompiled based on the package name, rather than the exact name and version.

To provide compatibility with older binary C++ applications and any packages that revdep-rebuild might have missed, `sys-libs/libstdc++-v3` needs to be merged before you unmerge GCC 3.3 from your system.

`root `[`#`]`emerge --oneshot sys-libs/libstdc++-v3 `

`root `[`#`]`emerge -aC =sys-devel/gcc-3.3*`

### [Using emerge -e]

This method, while much slower, will rebuild your whole system to ensure that everything has been rebuilt with your new compiler, and therefore safer. At first, you will upgrade GCC and libtool and switch to your new compiler.

`root `[`#`]`emerge --ask gcc`

Please substitute \"i686-pc-linux-gnu-3.4.5\" with the GCC version and CHOST settings you\'ve upgraded to:

`root `[`#`]`gcc-config i686-pc-linux-gnu-3.4.5 `

`root `[`#`]`source /etc/profile`

If you upgraded from gcc 3 to 4 (e.g. from 3.3.6 to 4.1.1 in this example) you will have to run fix_libtool_files.sh manually. Replace \$CHOST with your actual CHOST, found in /etc/portage/make.conf. Replace \<gcc-version\> with your new, updated GCC version.

`root `[`#`]`/usr/share/gcc-data/$CHOST/<gcc-version>/fix_libtool_files.sh 3.3.6`

`root `[`#`]`emerge --ask libtool`

To provide compatibility with older binary C++ applications, `sys-libs/libstdc++-v3` needs to be merged onto your system.

`root `[`#`]`emerge --oneshot sys-libs/libstdc++-v3`

Now we will go about first rebuilding the system target, then the world target. This will take a very long time, depending on the number of packages that you have installed, as it will rebuild your entire toolchain and supporting system files, followed by every package on your system, including the toolchain. This is necessary to ensure that all packages have been compiled with the new toolchain, including the toolchain itself.

`root `[`#`]`emerge -e system `

`root `[`#`]`emerge -e world`

It is also safe to remove older GCC versions at this time:

`root `[`#`]`emerge -aC =sys-devel/gcc-3.3*`

## [Upgrading to GCC on a First Install]

### [Introduction]

A GCC upgrade on a system after installation from a stage3 tarball is a simple affair. One advantage users of new installations have is they do not have a plethora of software installed that links against the older version of GCC. The following example is for a GCC-3.3 to 3.4 upgrade. Certain parts will be different if upgrading from other versions of GCC. For example, the library names used for `revdep-rebuild` below are GCC 3.3 specific, as well as the need to install `libstdc++-v3` .

If a user has not made any customizations to their system yet, then there are very few steps to get their system upgraded to a new GCC version. As with the GCC-3.3 to 3.4 upgrade, the user has a couple options. However, unlike the GCC-3.3 to 3.4 upgrade, this one is less complicated as there are fewer differences between the methods. The [#first-install-revdep-rebuild](#first-install-revdep-rebuild) is faster and makes use of the `revdep-rebuild` tool from `gentoolkit` , similar to the above procedure. Using revdep-rebuild causes only packages which actually link against GCC libraries to be rebuilt, while the [#first-install-emerge-e](#first-install-emerge-e) causes your entire new install to be recompiled with the new GCC version and takes much longer. This second method is never required and only documented for completeness.

These first steps are common between both methods, and should be completed by everyone.

`root `[`#`]`emerge --ask gcc`

Please substitute \"i686-pc-linux-gnu-3.4.5\" with the GCC version and CHOST settings you\'ve upgraded to:

`root `[`#`]`gcc-config i686-pc-linux-gnu-3.4.5 `

`root `[`#`]`source /etc/profile`

Now rebuild libtool.

`root `[`#`]`emerge --oneshot -av libtool`

To provide compatibility with older binary C++ applications, `sys-libs/libstdc++-v3` needs to be merged onto your system.

`root `[`#`]`emerge --oneshot sys-libs/libstdc++-v3`

### [Using revdep-rebuild]

This method requires that you first install `gentoolkit` if you have not already done so. We will then run `revdep-rebuild` to actually scan the installed packages for ones we need to rebuild, then rebuild them.

`root `[`#`]`emerge --ask gentoolkit`

`root `[`#`]`revdep-rebuild --library libstdc++.so.5 -- -p -v `

`root `[`#`]`revdep-rebuild --library libstdc++.so.5`

** Note**\
It is possible that you might have problems with non-existing package versions due to them being outdated or masked. If this is the case, you will want to use the `--package-names` option to `revdep-rebuild` . This causes packages to be recompiled based on the package name, rather than the exact name and version.

### [Using emerge -e]

This method, while much slower, will rebuild the system target to ensure that everything has been rebuilt with your new compiler. This is not necessary, but is valid if you are also making changes to CFLAGS or other make.conf variables that will affect the system compile.

Since we are performing these actions after an initial installation, we do not need to recompile the `world` target as we would when doing an upgrade on an already installed system. However, you may choose to perform a world update in place of the system update, to ensure that all packages are updated.

`root `[`#`]`emerge -e system`

### [Cleaning up]

It is also safe to remove older GCC versions at this time. Please substitute `YOUR-NEW-GCC-VERSION` with the actual version you\'ve upgraded to:

`root `[`#`]`emerge -aC "<sys-devel/gcc-YOUR-NEW-GCC-VERSION"`

## [Common Pitfalls]

It\'s important to disable `distcc` during upgrade. Mixing compiler versions on your nodes *will* cause build issues. This is not required for ccache, as the cache objects will be invalidated anyway.

Always use same GCC version for your kernel and additional kernel modules. Once you rebuild your world with new GCC, external modules (like `app-emulation/qemu-softmmu` ) will fail to load. Please rebuild your kernel with the new GCC to fix that.

If you\'re upgrading on a SPARC machine, make sure to rerun `silo -f` after re-emerging world to avoid possible issues.

### [Frequent Error Messages]

If your system complains about something like *libtool: link: \`/usr/lib/gcc-lib/i686-pc-linux-gnu/3.3.6/libstdc++.la\' is not a valid libtool archive* , please run `/usr/share/gcc-data/$CHOST/<gcc-version>/fix_libtool_files.sh 3.3.6` (substitute \"3.3.6\" with the version numbers from the error message, and \$CHOST and \<gcc-version\> with your actual CHOST and GCC version).

If you see *error: /usr/bin/gcc-config: line 632: /etc/env.d/gcc/i686-pc-linux-gnu-3.3.5: No such file or directory* , then try deleting [/etc/env.d/gcc/config-i686-pc-linux-gnu] and running `gcc-config` again, followed by `source /etc/profile` . Only do this if you do not have any cross-compilers set up, though.

If a package fails during `emerge -e system` or `emerge -e world` , you can resume operation with `emerge --resume` . If a package fails repeatedly, skip it with `emerge --resume --skipfirst` . Don\'t run any other instances of emerge in between or you will lose the resume information.

If you get an error message *spec failure: unrecognized spec option* while upgrading your compiler, try to switch back to your default compiler, unset the `GCC_SPECS` variable and upgrade GCC again:

`root `[`#`]`gcc-config 1 `

`root `[`#`]`source /etc/profile `

`root `[`#`]`unset GCC_SPECS `

`root `[`#`]`emerge -uav gcc`

## [See also]

-   [Upgrading GCC](https://wiki.gentoo.org/wiki/Upgrading_GCC "Upgrading GCC")

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Wernfried Haas, Jan Kundrat, halcy0n, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*