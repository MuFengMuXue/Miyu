**[/etc/portage/env]** can contain files to be called during the installation of specific packages, or files used to set Portage\'s environment variables on a per-package basis.

To have a file called when emerging a specific package, it should be named following the pattern \"[/etc/portage/env/\<**category**\>/\<**package_name**\>]\" (versions can be included, see portage man page), the contents being as in [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc"); the contents will be parsed as a bash script. These files can hook into specific phases of the emerge process.

If all that is needed is to set environment variables, use a free-form file name directly in [/etc/portage/env], then add a line in **[/etc/portage/package.env]** with a package atom followed by the chosen file name, like in the following examples. This allows the same environment settings to be used for multiple packages, if needed, or settings to be \"mix and matched\". Variables can be set in same manner as in [[[make.conf(5)]](https://man.archlinux.org/man/make.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

> It supports simple shell-like expansion of the form var=\"\$\", the source keyword and variable substitution, but not some of the more advanced BASH features like arrays and special parameter expansions. For more details, see the Simple lexical analysis documentation: [https://docs.python.org/3/library/shlex.html](https://docs.python.org/3/library/shlex.html). Note that if you source files, they need to be in the same shlex syntax for portage to read them.

** See also**\
There are two separate sections in the portage man page that cover in detail the use of this directory.

[/etc/portage/package.env] can be a *file*, or can be created as a *directory* that can contain multiple files. Some packages, such as [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]], require [/etc/portage/package.env] to be a directory.

** Note**\
Be aware that certain variables in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] are [incremental variables](https://dev.gentoo.org/~ulm/pms/head/pms.html#section-5.3.1). For an incremental variable, if the variable is already specified in [/etc/portage/make.conf] then Portage will read the values set in [make.conf], and *then* read the values set in files beneath the [/etc/portage/env] directory. In other words if `FEATURES="ccache"` in [make.conf], and `FEATURES="-ccache"` in [package/env/disable-ccache.conf], then Portage will see `FEATURES` as set to `FEATURES="ccache -ccache"` at emerge time for any packages which [disable-ccache.conf] is applied. This ultimately results in ccache being *disabled* for packages referencing [disable-ccache.conf] in the [/etc/portage/package.env] file.

## Contents

-   [[1] [Usage examples]](#Usage_examples)
    -   [[1.1] [Use different MAKEOPTS for a specific package]](#Use_different_MAKEOPTS_for_a_specific_package)
    -   [[1.2] [Enable debug information for a specific package]](#Enable_debug_information_for_a_specific_package)
    -   [[1.3] [Build certain packages in a different location]](#Build_certain_packages_in_a_different_location)
    -   [[1.4] [Amend an ebuild function]](#Amend_an_ebuild_function)
-   [[2] [Caveats]](#Caveats)
    -   [[2.1] [emerge \--info does not show changes from package.env]](#emerge_--info_does_not_show_changes_from_package.env)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Usage examples]

### [Use different `MAKEOPTS` for a specific package]

As mentioned at [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS"), a good rule of thumb is to set the amount of [[[make(1)]](https://man.archlinux.org/man/make.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] jobs to the minimum of the size of RAM divided by 2GB and CPU thread count. For most packages, each job uses less than 2 GB of RAM, so this is fine. However, some packages may need more RAM when compiling, which necessitates a lower `--jobs` value. This can be set using [/etc/portage/package.env].

First, a file that appends the desired `--jobs` value to `MAKEOPTS` should be created:

[FILE] **`/etc/portage/env/makeopts-jobs-2.conf`**

    MAKEOPTS="$ --jobs=2"

If `MAKEOPTS` contains multiple values for `--jobs`, the last one will be used by make.

This file can then be applied to packages that fail to compile with higher job counts:

[FILE] **`/etc/portage/package.env`**

    dev-qt/qtwebengine makeopts-jobs-2.conf

But it is better to limit *EMERGE_DEFAULT_OPTS* for Chromium, QtWebEngine, Rust, LibreOffice rather than *MAKEOPTS*.

### [Enable debug information for a specific package]

Suppose a user would like to build GIMP with debug information because the user wants a development version and would like to report any crashes to GIMP upstream.

Create a file in [/etc/portage/env] that contains the desired changes:

** Important**\
In per-package environment files, variables like *CFLAGS* must be set explicitly. Portage does not automatically expand *COMMON_FLAGS*.

[FILE] **`/etc/portage/env/debug.conf`**

    CFLAGS="$ -g"
    CXXFLAGS="$ -g"
    FEATURES="splitdebug"

Next, add an entry to [package.env] followed by the name of the file created in the previous step:

[FILE] **`/etc/portage/package.env`**

    media-gfx/gimp  debug.conf

### [Build certain packages in a different location]

Suppose the Portage build directory is in [tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs"), but some packages are too large, and run out of space. The `PORTAGE_TMPDIR` can be modified to exclude the packages that are too large.

Create a file in [/etc/portage/env] that modifies `PORTAGE_TMPDIR` variable and sets it to an on-disk directory:

[FILE] **`/etc/portage/env/notmpfs.conf`**

    PORTAGE_TMPDIR="/var/tmp/notmpfs"

Add [large packages](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs#Considering_tmpfs.27_size "Portage TMPDIR on tmpfs") to [package.env]:

[FILE] **[`/etc/portage/package.env`]**

    app-emulation/qemu-kvm  notmpfs.conf
    app-office/libreoffice  notmpfs.conf debug.conf
    www-client/firefox      notmpfs.conf

Do not forget to create the [/var/tmp/notmpfs] directory and change the ownership to the portage user and group.

Notice that it is possible to reference several files in [/etc/portage/env] for each package. [(Tip originally blogged by [Jeremy Olexa](https://blog.jolexa.net/post/gentoo-per-package-portage_tmpdir-settings/))]

### [Amend an ebuild function]

A package-specific file in the [[/etc/portage/env](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env")] directory could help modifying an [ebuild function](https://devmanual.gentoo.org/ebuild-writing/functions/), without [creating a new ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository"). In this example, **epatch_user** [is added to an old EAPI 5 ebuild](https://forums.gentoo.org/viewtopic-t-1114198.html):

[FILE] **`/etc/portage/env/media-gfx/fbida-2.12`**

    src_prepare()

** Important**\
It is unwise to modify an ebuild function. It\'s better to use pre/post hook functions instead, see [/etc/portage/bashrc#Hook_functions](https://wiki.gentoo.org/wiki//etc/portage/bashrc#Hook_functions "/etc/portage/bashrc") for more details.

** See also**\
See [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") for more information on what can be done in these files.

## [Caveats]

### [emerge \--info does not show changes from package.env]

According to [[[bug #410069]](https://bugs.gentoo.org/show_bug.cgi?id=410069)[]], it is important to note that running [emerge \--info] does not show changes from the [package.env] file. This may be fixed in a future Portage release.

## [See also]

-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), Gentoo\'s package manager.
-   [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") --- a global [bashrc] file referenced by Portage.
-   [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") --- provide a way to apply patches to package source code when sources are extracted before installation
-   [Knowledge Base:Emerge out of memory](https://wiki.gentoo.org/wiki/Knowledge_Base:Emerge_out_of_memory "Knowledge Base:Emerge out of memory")
-   [Knowledge Base:Overriding environment variables per package](https://wiki.gentoo.org/wiki/Knowledge_Base:Overriding_environment_variables_per_package "Knowledge Base:Overriding environment variables per package")

## [External resources]

-   [Portage man page](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html)