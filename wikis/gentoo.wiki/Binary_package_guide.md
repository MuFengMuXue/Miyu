This page contains [[changes](https://wiki.gentoo.org/index.php?title=Binary_package_guide&oldid=1430358&diff=1435751)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Binary_package_guide/de "Leitfaden zur Nutzung von Binärpaketen (21% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Binary_package_guide/es "Guía de los paquetes binarios (18% translated)")
-   [français](https://wiki.gentoo.org/wiki/Binary_package_guide/fr "Guide sur les paquets binaires (22% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Binary_package_guide/it "Guida ai pacchetti binari (8% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Binary_package_guide/hu "Bináris szoftvercsomagok útmutatója (85% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Binary_package_guide/cs "Binary package guide/cs (2% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Binary_package_guide/ru "Руководство по бинарным пакетам (52% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Binary_package_guide/zh-cn "二进制包指南 (20% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Binary_package_guide/ja "バイナリーパッケージガイド (98% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Binary_package_guide/ko "바이너리 꾸러미 안내서 (15% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

** See also**\
See the [Gentoo Binary Host Quickstart](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") article for information on **using pre-built binary packages from the *Gentoo binary package host***. That article should cover everything needed to easily use the binary packages from the public Gentoo binhost.

This guide covers in-depth **binary package** creation, distribution, use, and maintenance, and a few more advanced topics near the end. This page focuses on self-built binary packages rather than the official Gentoo binhost, though it covers that a bit too.

[Portage](https://wiki.gentoo.org/wiki/Portage "Portage") fully supports binary packages in addition to its well-known support for source-based [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild"). Portage may be used to create binary packages, to install them, or to update packages already on the system from binary packages. Portage has support for fetching binary packages from *binary package hosts*.

** Note**\
All tools used in this guide are part of [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]], unless otherwise stated.

## Contents

-   [[1] [Why use binary packages on Gentoo?]](#Why_use_binary_packages_on_Gentoo.3F)
-   [[2] [Binary package formats]](#Binary_package_formats)
-   [[3] [Using binary packages]](#Using_binary_packages)
    -   [[3.1] [General prerequisites]](#General_prerequisites)
    -   [[3.2] [Handling \*FLAGS in detail]](#Handling_.2AFLAGS_in_detail)
    -   [[3.3] [Installing binary packages]](#Installing_binary_packages)
    -   [[3.4] [Verify binary package OpenPGP signatures]](#Verify_binary_package_OpenPGP_signatures)
    -   [[3.5] [Pulling packages from a binary package host]](#Pulling_packages_from_a_binary_package_host)
    -   [[3.6] [Reinstalling modified binary packages]](#Reinstalling_modified_binary_packages)
    -   [[3.7] [Additional client settings]](#Additional_client_settings)
    -   [[3.8] [Updating packages on the binary package host]](#Updating_packages_on_the_binary_package_host)
-   [[4] [Creating binary packages]](#Creating_binary_packages)
    -   [[4.1] [Using \--buildpkg as an emerge option]](#Using_--buildpkg_as_an_emerge_option)
    -   [[4.2] [Implementing buildpkg as a Portage feature]](#Implementing_buildpkg_as_a_Portage_feature)
    -   [[4.3] [Excluding creation of some packages]](#Excluding_creation_of_some_packages)
    -   [[4.4] [Binary package compression formats]](#Binary_package_compression_formats)
    -   [[4.5] [Binary package OpenPGP signing]](#Binary_package_OpenPGP_signing)
    -   [[4.6] [Using quickpkg]](#Using_quickpkg)
-   [[5] [Setting up a binary package host]](#Setting_up_a_binary_package_host)
    -   [[5.1] [Web based binary package host]](#Web_based_binary_package_host)
        -   [[5.1.1] [HTTPD]](#HTTPD)
        -   [[5.1.2] [Caddy]](#Caddy)
        -   [[5.1.3] [nginx]](#nginx)
        -   [[5.1.4] [http.server]](#http.server)
    -   [[5.2] [SSH binary package host]](#SSH_binary_package_host)
    -   [[5.3] [NFS exported]](#NFS_exported)
        -   [[5.3.1] [Setting file permissions]](#Setting_file_permissions)
-   [[6] [Maintaining binary packages]](#Maintaining_binary_packages)
    -   [[6.1] [Removing outdated binary packages]](#Removing_outdated_binary_packages)
    -   [[6.2] [Maintaining the Packages file]](#Maintaining_the_Packages_file)
-   [[7] [Advanced topics]](#Advanced_topics)
    -   [[7.1] [Chrooting]](#Chrooting)
        -   [[7.1.1] [Creating the directories]](#Creating_the_directories)
        -   [[7.1.2] [Deploying the build environment]](#Deploying_the_build_environment)
        -   [[7.1.3] [Configuring the build environment]](#Configuring_the_build_environment)
        -   [[7.1.4] [Configuring the chroot]](#Configuring_the_chroot)
        -   [[7.1.5] [Entering the chroot]](#Entering_the_chroot)
            -   [[7.1.5.1] [Performing an initial build]](#Performing_an_initial_build)
    -   [[7.2] [Building for other architectures]](#Building_for_other_architectures)
        -   [[7.2.1] [crossdev]](#crossdev)
            -   [[7.2.1.1] [Build a cross compiler]](#Build_a_cross_compiler)
            -   [[7.2.1.2] [Basic setup]](#Basic_setup)
            -   [[7.2.1.3] [Profiles]](#Profiles)
            -   [[7.2.1.4] [Build a single package]](#Build_a_single_package)
            -   [[7.2.1.5] [Build world file]](#Build_world_file)
            -   [[7.2.1.6] [Binary location]](#Binary_location)
        -   [[7.2.2] [QEMU chroot compiling]](#QEMU_chroot_compiling)
    -   [[7.3] [Creating snapshots of the packages directory]](#Creating_snapshots_of_the_packages_directory)
    -   [[7.4] [Understanding the binary package format]](#Understanding_the_binary_package_format)
        -   [[7.4.1] [XPAK format]](#XPAK_format)
        -   [[7.4.2] [GPKG format]](#GPKG_format)
    -   [[7.5] [The PKGDIR layout]](#The_PKGDIR_layout)
    -   [[7.6] [Unpacking with quickunpkg]](#Unpacking_with_quickunpkg)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Undefined Reference Compiler Errors]](#Undefined_Reference_Compiler_Errors)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [][Why use binary packages on Gentoo?]

There are many reasons why some system administrators like installing binary packages on Gentoo:

-   *Save time when keeping similar systems updated*. Building from source can take more time than installing from binaries. When maintaining several similar systems, possibly some of them with older hardware, it can be easier if only one system has to compile everything from source and the other systems use the resultant binary packages.
-   *Do safe updates*. For mission-critical systems in production it is important to stay *usable* as much as possible. This can be done by a staging server that performs all updates first to itself. Once the staging server is in a good state the updates can then be applied to the critical systems via binary packages. A variant of this approach is to do the updates in a chroot on the same system and use the binaries created there to update the real system.
-   *As a backup*. Often, binary packages are the only way of recovering a broken system (i.e. broken compiler). Having pre-compiled binaries around, either on a binary package server or locally, can be of great help in case of a broken toolchain.
-   It can aid in *updating very old systems*. The task of updating very old systems can be eased by using binary packages. It is usually helpful to install binary packages on old systems because they do not require build-time dependencies to be installed/updated. Binaries packages also avoid failures in build processes.

## [[] Binary package formats]

Two binary package formats for use in Gentoo exist, XPAK and GPKG. Starting with [v3.0.31](https://gitweb.gentoo.org/proj/portage.git/tag/?h=portage-3.0.31), Portage supports the new binary package format GPKG. The GPKG format solves issues with the legacy XPAK format and offers the benefit of [new features](https://wiki.gentoo.org/wiki/Binary_package_guide#Binary_package_OpenPGP_signing "Binary package guide"), however it is *not* backward compatible with the legacy XPAK format.

System administrators using older versions of Portage (\<=v3.0.30) should continue to use the legacy XPAK format, which is Portage\'s default setting on those versions.

Motivation for the newer GPKG format design can be found in [GLEP 78: Gentoo binary package container format](https://www.gentoo.org/glep/glep-0078.html#motivation). Bugs [[[bug #672672]](https://bugs.gentoo.org/show_bug.cgi?id=672672)[]] and [[[bug #820578]](https://bugs.gentoo.org/show_bug.cgi?id=820578)[]] also provide helpful details.

To instruct Portage to use the GPKG format, change the `BINPKG_FORMAT` value in [/etc/portage/make.conf]. Note that current versions of Portage use gpkg by default.

[FILE] **`/etc/portage/make.conf`Specify GPKG binary package format**

    BINPKG_FORMAT="gpkg"

This guide mostly applies to both formats; where this is not the case it will be noted. See the [Understanding the binary package format](https://wiki.gentoo.org/wiki/Binary_package_guide#Understanding_the_binary_package_format "Binary package guide") section for technical details on the binary package formats themselves.

## [[] Using binary packages]

### [General prerequisites]

For binary packages made on one system to be usable on other systems they must fulfill some requirements:

-   The builder and client architecture and [`CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST") must match.
-   The `CFLAGS` and `CXXFLAGS` variables used to build the binary packages must be compatible with all clients.
-   USE flags for processor specific instruction set features (like MMX, SSE, etc.) must be carefully selected; all clients must support them.

** Note**\
[Binary packages](https://wiki.gentoo.org/wiki/Binary_package_quickstart "Binary package quickstart") that are distributed as part of Gentoo\'s official [Binhost project](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost") use a minimum instruction set and conservative compiler settings in order to be as widely usable as possible. By way of example, **[amd64]** keyworded packages are built with `-march=x86-64 -mtune=generic`, which works for *any* machine which runs the x86-64 (**[amd64]**) instruction set.

** Important**\
Portage can not validate if these requirements match. In case of doubt, it is the responsibility of the system administrator to guard these settings.

### [][Handling \*FLAGS in detail]

The [[[app-misc/resolve-march-native]](https://packages.gentoo.org/packages/app-misc/resolve-march-native)[]] utility can be used to find a subset of `CFLAGS` that is supported by both the server and client(s). For example, the host might return:

`user `[`$`]`resolve-march-native`

     -march=skylake -mabm -mrtm --param=l1-cache-line-size=64 --param=l1-cache-size=32 --param=l2-cache-size=12288

While the client might return:

`user `[`$`]`resolve-march-native`

     -march=ivybridge -mno-rdrnd --param=l1-cache-line-size=64 --param=l1-cache-size=32 --param=l2-cache-size=3072

In this example `CFLAGS` could be set to `-march=ivybridge -mno-rdrnd` since `-march=ivybridge` is a full subset of `-march=skylake`. `-mabm` and `-mrtm` are not included as these are not supported by the client. However, `-mno-rdrnd` is included as the client does not support `-mrdrnd`. To find which `-march`\'s are subsets of others, check the [gcc manual](//gcc.gnu.org/onlinedocs/gcc/x86-Options.html), if there is no suitable subset set e.g. `-march=x86-64`.

Optionally, it is also possible to set `-mtune=`*`some-arch`* or `-mtune=native` to tell gcc to tune code to a specific arch. In contrast to `-march`, the `-mtune` argument does not prevent code from being executed on other processors. For example, to compile code which is compatible with *ivybridge* and up but is tuned to run best on *skylake* set `CFLAGS` to `-march=ivybridge -mtune=skylake`. When `-mtune` is not set it defaults to whatever `-march` is set to.

When changing `-march` to a lower subset for using binary packages on a client, a full recompilation is required to make sure that all binaries are compatible with the client\'s processor, to save time packages that are not compiled with e.g. gcc/clang can be excluded:

`user `[`$`]`emerge -e @world --exclude="acct-group/* acct-user/* virtual/* app-eselect/* sys-kernel/* sys-firmware/* dev-python/* dev-java/* dev-ruby/* dev-perl/* dev-lua/* dev-php/* dev-tex/* dev-texlive/* x11-themes/* */*-bin"`

Similarly, [[[app-portage/cpuid2cpuflags]](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)[]] can be used to find a suitable subset of processor specific instruction set USE flags. For example, the host might return:

`user `[`$`]`cpuid2cpuflags`

     CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sse sse2 sse3 sse4_1 sse4_2 ssse3

While the client might return:

`user `[`$`]`cpuid2cpuflags`

     CPU_FLAGS_X86: avx f16c mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

In this example `CPU_FLAGS_X86` can be set to `avx f16c mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3` in [/etc/portage/make.conf] because these flags are supported by both the client and the host

Next to these, Portage can check if the binary package is built using the same USE flags as expected on the client. Unless using `--usepkgonly` (`-K`) or `--getbinpkgonly` (`-G`), if a package is built with a different USE flag combination, Portage will either ignore the binary package (and use source-based build) or fail, depending on the options passed to the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") command upon invocation (see [Installing binary packages](https://wiki.gentoo.org/wiki/Binary_package_guide#Installing_binary_packages "Binary package guide")).

On clients, a few configuration changes are needed in order for the binary packages to be used.

### [[] Installing binary packages]

There are a few options that can be passed on to the [emerge] command that inform Portage about using binary packages:

  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Option                     Description
  `--usepkg` (`-k`)          Tries to use the binary package(s) in the locally available [packages] directory. Useful when using [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") or [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") mounted binary package hosts. If the binary packages are not found, a regular (source-based) installation will be performed.
  `--usepkgonly` (`-K`)      Similar to `--usepkg` (`-k`) but fail if the binary package cannot be found. This option is useful if *only pre-built* binary packages are to be used.
  `--getbinpkg` (`-g`)       Download the binary package(s) from a remote binary package host. If the binary packages are not found, a regular (source-based) installation will be performed.
  `--getbinpkgonly` (`-G`)   Similar to `--getbinpkg` (`-g`) but will fail if the binary package(s) cannot be downloaded. This option is useful if *only pre-built* binary packages are to be used.
  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to automatically use binary package installations, the appropriate option can be added to the `EMERGE_DEFAULT_OPTS` variable:

[FILE] **`/etc/portage/make.conf`Automatically fetch binary packages and build from source if not available**

    EMERGE_DEFAULT_OPTS="$ --getbinpkg"

There is a Portage feature that forces emerge to always try to fetch files from the binary package host:

[FILE] **`/etc/portage/make.conf`Enabling getbinpkg in the `FEATURES` variable**

    FEATURES="getbinpkg"

Note that this is *not* equivalent to `--getbinpkg` (`-g`) in the `EMERGE_DEFAULT_OPTS` variable. Especially, `--getbinpkg=n` on the command line won\'t override the feature.

** Warning**\
Currently, if a package with [user patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") is installed, it will be fetched from the binary package host anyway, and the user patches themselves won\'t be applied. [[[bug #917047]](https://bugs.gentoo.org/show_bug.cgi?id=917047)[]]

This can be fixed by excluding any packages with user patches from using the binhost:

[FILE] **`/etc/portage/make.conf`Exclude package ATOM from using the binhost**

    EMERGE_DEFAULT_OPTS="$ --usepkg-exclude ATOM"

### [[] Verify binary package OpenPGP signatures]

** Important**\
OpenPGP signing and verification is only available for the GPKG binpkg format.

Portage will try to verify the binary package\'s signature whenever possible, but users must first set up trusted local keys. [[[app-portage/getuto]](https://packages.gentoo.org/packages/app-portage/getuto)[]] can be used to set up a local trust anchor and update the keys in [/etc/portage/gnupg]. Portage calls [getuto] automatically with *\--getbinpkg* or *\--getbinpkgonly*.

This configures portage such that it trusts the [Gentoo Release Engineering keys](https://www.gentoo.org/downloads/signatures/) as also contained in the package [[[sec-keys/openpgp-keys-gentoo-release]](https://packages.gentoo.org/packages/sec-keys/openpgp-keys-gentoo-release)[]] for binary installation purposes.

Changes to the configuration can be done as root using `gpg` with the parameter `--homedir=/etc/portage/gnupg`. This way allows importing additional signing keys (e.g. for non-standard installation sources) and declare them as trusted.

To add a custom signing key:

1.  Generate (or use an existing) key with signing abilities, and export the public key to a file. **This is distinct from the key and keyring that getuto will generate**. The signing key should reside in [/root/.gnupg] by default (`BINPKG_GPG_SIGNING_GPG_HOME` controls this).
2.  Set `BINPKG_GPG_SIGNING_KEY` to be the fingerprint for the public key of the signing key just-created.
3.  Run `getuto` if it has never run (for the verification keyring in [/etc/portage/gnupg]:

    :::: cmd-box


    `root `[`#`]`getuto`


    ::::
4.  Use `gpg --homedir=/etc/portage/gnupg --import public.key` to import the public key of the signing key in Portage\'s verification keyring.
5.  Trust and sign the signing key created in Step 1 using the verification key created by `getuto`. In order to do this, first get the password to unlock the key at [/etc/portage/gnupg/pass], then use:

    :::: cmd-box


    `root `[`#`]`gpg --homedir=/etc/portage/gnupg --edit-key YOURKEYID`


    ::::

    Type `sign`, `yes`, paste (or type) the password. The key is now signed. To trust it, type `trust`, then `4` to trust it fully. Finally, type `save`.
6.  Update the trustdb so that GPG considers the key valid:

    :::: cmd-box


    `root `[`#`]`gpg --homedir=/etc/portage/gnupg --check-trustdb`


    ::::

If you hit any issues, check if a pre-existing [/etc/portage/gnupg] existed. If it did, move it away and then repeat the above steps.

Congratulations, Portage now has a working keyring!

** Important**\
Trusting the key marginally or less will not work.

By default, Portage will only verify GPG signatures when a signature file is found in a package, which allows the user to mix signed and unsigned GPKG binary packages from different sources, and allows to use old XPAK format binary packages.

If the user wishes to force signature verification, the `binpkg-request-signature` feature needs to be enabled. This feature assumes that all packages should be signed and rejects any unsigned package. Note that this feature does not support per-binhost configuration.

[FILE] **`/etc/portage/make.conf`Enabling Portage\'s binpkg-request-signature feature**

    # Require that all binpkgs be signed and reject them if they are not (or have an invalid sig)
    FEATURES="binpkg-request-signature"

### [[] Pulling packages from a binary package host]

** Warning**\
\"The `PORTAGE_BINHOST` variable is deprecated in favor of the [/etc/portage/binrepos.conf] configuration file\" - [[[make.conf(5)]](https://man.archlinux.org/man/make.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]

When using a binary package host, clients need to have the `sync-uri` variable in [/etc/portage/binrepos.conf] (preferred) **or** the `PORTAGE_BINHOST` variable set in [/etc/portage/make.conf]. Without this configuration, the client will not know where the binary packages are stored which results in Portage being unable to retrieve them.

[FILE] **`/etc/portage/binrepos.conf`Setting binhost sync-uri**

    [mybinhost]
    sync-uri = https://example.com/binhost
    priority = 10

    # Introduced in portage-3.0.74 for per-repo verification choices
    #verify-signature = true
    # Defaults to /var/cache/binhost/$NAME with >=portage-3.0.77
    #location = /var/cache/binhost/mybinhost

For each binhost, a name can be configured in the brackets. `sync-uri` must point to the directory in which the [Packages] file resides. Optionally, `priority` can be set. When a package exists in multiple binary package repositories, the package is pulled from the binary package host with the highest priority. This way, a preferred binary package host can be set up.

Many Gentoo stages already come with a preinstalled [/etc/portage/binrepos.conf] file, which points to the corresponding binary packages generated during the stage builds.

** Note**\
The support for multiple binary package servers is somewhat incomplete. If several servers serve a binary package for the same package version, then only the first one will be considered. This can be problematic when these binary packages differ in their USE variable configuration and the USE variable configuration of a later binary package would match the systems configuration.

### [[] Reinstalling modified binary packages]

Passing the `--rebuilt-binaries` option to [emerge] will reinstall every binary that has been rebuilt since the package was installed. This is useful in case rebuilding tools like [revdep-rebuild] are run on the binary package server.

A related option is `--rebuilt-binaries-timestamp`. It causes emerge not to consider binary packages for a re-install if those binary packages have been built before the given time stamp. This is useful to avoid re-installing all packages, if the binary package server had to be rebuild from scratch but `--rebuilt-binaries` is used otherwise.

### [[] Additional client settings]

Next to the `getbinpkg` feature, Portage also listens to the `binpkg-logs` feature. It controls if log files for successful binary package installations should be kept. It is only relevant if the `PORT_LOGDIR` variable has been set and is enabled by default.

Similar to excluding binary packages for a certain set of packages or categories, clients can be configured to exclude binary package installations for a certain set of packages or categories.

To accomplish this, use the `--usepkg-exclude` option:

`root `[`#`]`emerge -uDNg @world --usepkg-exclude "sys-kernel/gentoo-sources virtual/* sys-kernel/gentoo-kernel"`

To enable such additional settings for each emerge command, add the options to the `EMERGE_DEFAULT_OPTS` variable in the [make.conf] file:

[FILE] **`/etc/portage/make.conf`Enabling emerge settings on every invocation**

    EMERGE_DEFAULT_OPTS="$ --usepkg-exclude 'sys-kernel/gentoo-sources virtual/*'"

### [Updating packages on the binary package host]

** Important**\
Do not use `--changed-use`(`-U`) when updating packages on the binary package host, doing so will cause packages with added or removed USE flags to be skipped, which will cause their installation from binary package on the client to fail due to non-matching USE between the source ebuild and binary package (if the client\'s `--binpkg-respect-use=y`, the default). Use `--newuse`(`-N`), which will always rebuild packages even for added or removed USE flags, ensuring the binary package stays in sync with the source ebuild.

## [[] Creating binary packages]

There are three main methods for creating binary packages:

1.  After a regular installation, using the [quickpkg] application.
2.  Explicitly during an [emerge] operation by using the `--buildpkg` (`-b`) option.
3.  Automatically through the use of the `buildpkg` (build binary packages for all packages) or `buildsyspkg` (build binary packages only for the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)")) values in Portage\'s `FEATURES` variable.

All three methods will create a binary package in the directory pointed to by the `PKGDIR` variable (which defaults to [/var/cache/binpkgs]).

### [[] Using \--buildpkg as an emerge option]

When installing software using [emerge], Portage can be asked to create binary packages by using `--buildpkg` (`-b`) option:

`root `[`#`]`emerge --ask --buildpkg sys-devel/gcc`

It is also possible to ask Portage to *only* create a binary package but *not* to install the software on the live system. For this, the `--buildpkgonly` (`-B`) option can be used:

`root `[`#`]`emerge --ask --buildpkgonly sys-devel/gcc`

The latter approach however requires all build time dependencies to be previously installed.

### [[] Implementing buildpkg as a Portage feature]

The most common way to automatically create binary packages whenever a package is installed by Portage is to use the `buildpkg` feature, which can be set in [/etc/portage/make.conf] like so:

[FILE] **`/etc/portage/make.conf`Enabling Portage\'s buildpkg feature**

    FEATURES="buildpkg"

With this feature enabled, every time Portage installs software, it will create a binary package as well.

### [[] Excluding creation of some packages]

It is possible to tell Portage not to create binary packages for a select few packages or categories. This is done by passing the `--buildpkg-exclude` option to emerge:

`root `[`#`]`emerge -uDN @world --buildpkg --buildpkg-exclude "acct-*/* sys-kernel/*-sources virtual/*"`

This could be used for packages that have little to no benefit in having a binary package available. Examples would be the Linux kernel source packages or upstream binary packages (those ending with *-bin* like [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]]).

### [[] Binary package compression formats]

It is possible to use a specific compression type on binary packages. Currently, the following formats are supported: `bzip2`, `gzip`, `lz4`, `lzip`, `lzop`, `xz`, and `zstd`. Defaults to `zstd`. Review [man make.conf] and search for `BINPKG_COMPRESS` for the most up-to-date information.

The compression format can be specified via [make.conf].

[FILE] **`/etc/portage/make.conf`Specify binary package compression format**

    BINPKG_COMPRESS="lz4"

Note that the compression type used might require extra dependencies to be installed, for example, in this case [[[app-arch/lz4]](https://packages.gentoo.org/packages/app-arch/lz4)[]].

### [[] Binary package OpenPGP signing]

** Important**\
OpenPGP signing and verification is only available for the GPKG binpkg format.

A PGP signature enables Portage to check the creator and integrity of a binary package, and to perform trust management based on PGP keys. The binary package signing feature is **disabled** by default. To use it, enable the `binpkg-signing` feature. Note that whether this feature is enabled does not affect the signature verification feature.

[FILE] **`/etc/portage/make.conf`Enabling Portage\'s binpkg-signing feature**

    FEATURES="binpkg-signing"

Users also need to set the `BINPKG_GPG_SIGNING_GPG_HOME` and `BINPKG_GPG_SIGNING_KEY` variables for Portage to find the signing key.

[FILE] **`/etc/portage/make.conf`Configuring Portage\'s signing key**

    BINPKG_GPG_SIGNING_GPG_HOME="/root/.gnupg"
    BINPKG_GPG_SIGNING_KEY="0x1234567890ABCDEF"

Portage will only try to unlock the PGP private key at the beginning. If the user\'s key will expire over time, then consider enabling `gpg-keepalive` to prevent signing failures.

[FILE] **`/etc/portage/make.conf`Enabling Portage\'s gpg-keepalive feature**

    FEATURES="gpg-keepalive"

** Tip**\
gpg-agent by default expires cache entries after 2 hours. This means that, by default, if an emerge session lasts longer than 2 hours, signing of binpkgs will eventually fail regardless of [FEATURES=\"gpg-keepalive\"]. To prevent this problem, set `max-cache-ttl` to some large value (e.g. `34560000`) in [\$BINPKG_GPG_SIGNING_GPG_HOME/gpg-agent.conf].

### [[] Using quickpkg]

The [quickpkg] application (included in Portage) takes one or more dependency atoms (or package sets) and creates binary packages for all *installed* packages that match that atom.

** Warning**\
There is a caveat with this method: it relies on the installed files, which can be a problem in case of configuration files. Administrators often change configuration files after installing software. Because this could leak out important (perhaps even confidential) data into the packages, [quickpkg] by default does *not* include configuration files that are protected through the `CONFIG_PROTECT` method. To force inclusion of configuration files, use the `--include-config` or `--include-unmodified-config` options.

For instance, to create binary packages of all *installed* GCC versions:

`root `[`#`]`quickpkg sys-devel/gcc`

To create binary packages for the system set:

`root `[`#`]`quickpkg @system`

To create binary packages of all installed packages on the system, use the `*` glob:

`root `[`#`]`quickpkg "*/*"`

## [[] Setting up a binary package host]

Portage supports a number of protocols for downloading binary packages: FTP, FTPS, HTTP, HTTPS, and SSH/SFTP. This leaves room for many possible binary package host implementations.

There is, however, no \"out-of-the-box\" method provided by Portage for distributing binary packages. Depending on the desired setup additional software will need to be installed.

### [[] Web based binary package host]

A common approach for distributing binary packages is to create a web-based binary package host.

#### [HTTPD]

Install [[[www-servers/lighttpd]](https://packages.gentoo.org/packages/www-servers/lighttpd)[]] and configure it to provide read access to [/etc/portage/make.conf]\'s `PKGDIR` location.

[FILE] **`/etc/lighttpd/lighttpd.conf`lighttpd configuration example**

    # add this to the end of the standard configuration
    server.dir-listing = "enable"
    server.modules += ( "mod_alias" )
    alias.url = ( "/packages" => "/var/cache/binpkgs/" )
    dir-listing.activate = "enable" # optional: keep it, if you want to have a nice listing at web page at the /packages path.

#### [Caddy]

To set up the [Caddy](https://wiki.gentoo.org/wiki/Caddy "Caddy") HTTP server to provide a web-based binary package host, create a `Caddyfile` containing:

[FILE] **`Caddyfile`**

    x.x.x.x:80

Once that is created, run Caddy with:

`root `[`#`]`caddy run --config /path/to/Caddyfile`

Then, on the client systems, configure [/etc/portage/binrepos.conf] accordingly:

[FILE] **`/etc/portage/binrepos.conf/caddy.conf`Using a web-based binary package host**

    [caddy]
    priority = 1
    sync-uri = http://binhost.example.com/packages

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/caddy

#### [nginx]

To setup a web-based binhost utilizing [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx"), the default configuration `nginx.conf` will suffice, with a little tweaking. A full example of such looks like the following:

[FILE] **`/etc/nginx/nginx.conf`**

    user nginx nginx;
    worker_processes auto;

    events

    http
    }

#### [http.server]

** Warning**\
It is not recommended to use this for hosting in production, as it only implements basic security checks. For more information, read the official documentation [here](https://docs.python.org/3/library/http.server.html).

Python includes a barebones HTTP server by default and is very simple to use. To setup a binhost with this, [cd] into the `PKGDIR` directory and run:

`user `[`$`]`python http.server 8000`

    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

### [[] SSH binary package host]

To provide an authenticated approach for binary package mirrors, Portage can be configured to use the SSH protocol to access binary packages.

When using SSH, it is possible to use the root Linux user\'s SSH key (without passphrase as the installations need to happen in the background) to connect to a remote binary package host.

To accomplish this, make sure that the root user\'s SSH key is allowed on the server. This will need to happen for each machine that will connect to the SSH capable binary host:

`root `[`#`]`cat root.id_rsa.pub >> /home/binpkguser/.ssh/authorized_keys`

The [/etc/portage/binrepos.conf] configuration could then look like so:

[FILE] **`/etc/portage/binrepos.conf/ssh.conf`Setting binrepos.conf up for SSH access**

    [ssh]
    priority = 1
    sync-uri = ssh://binpkguser@binhostserver/var/cache/binpkgs

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/ssh

If the SSH server is listening to a different port (e.g 25), then it must be specified after the address, like so:

[FILE] **`/etc/portage/binrepos.conf/ssh.conf`Setting up binrepos.conf for SSH access on port 25**

    [ssh]
    priority = 1
    sync-uri = ssh://binpkguser@binhostserver:25/var/cache/binpkgs

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/ssh

Portage ignores [\~/.ssh/config] by default, however you can setup your make.conf to use a custom ssh config like so:

[FILE] **`/etc/portage/make.conf`Setting up make.conf for custom SSH config**

    PORTAGE_SSH_OPTS='-F /home/larry/.ssh/config'

### [[] NFS exported]

When using binary packages on an internal network, it might be easier to export the packages through [NFS](https://wiki.gentoo.org/wiki/Nfs-utils "Nfs-utils") and mount it on the clients.

There are two ways of doing this:

1.  Making it a \'remote\' via [/etc/portage/binrepos.conf] which is the modern way (and uses *\--getbinpkg*), or
2.  Mounting the exported tree at [/var/cache/binpkgs] where Portage thinks it is \'local\'

The modern way allows per-repo PGP verification and also \'re-serving\' without mixing up binaries from different sources.

The [/etc/exports] file could look like so:

[FILE] **`/etc/exports`Exporting the packages directory**

    /var/cache/binpkgs   2001:db8:81::/48(ro,no_subtree_check,root_squash) 192.168.100.0/24(ro,no_subtree_check,root_squash)

On the clients, the location can then be mounted **at a separate location**. An example [/etc/fstab] entry would look like so:

[FILE] **`/etc/fstab`Entry for mounting the packages folder**

    binhost:/var/cache/binpkgs      /opt/nfs-binpkgs    nfs    defaults    0 0

Then configure Portage to know about this:

[FILE] **`/etc/portage/binrepos.conf/nfs.conf`**

    [nfs]
    priority = 1
    sync-uri = file:///opt/nfs-binpkgs

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/nfs

That is, there are three locations involved in total:

-   server/binhost: [/var/cache/binpkgs]
-   client: [/opt/nfs-binpkgs] is the mount location for NFS with the full set of binpkgs
-   client: [/var/cache/binhost/nfs] is the local cached copy of any binaries used

#### [[] Setting file permissions]

Using the above exports, the client may not discover new binary packages or may fail to emerge them if the file permissions are insufficient. To fix this, change ownership of the exported PKGDIR from the host:

`root `[`#`]`chown -v nobody:nobody /var/cache/binpkgs`

Set also the [setgid] bit so that new packages will inherit the group ownership:

`root `[`#`]`chmod -v g+s /var/cache/binpkgs`

The ownership will also have to be changed individually (or recursively) for any packages that have already been created at this point.

## [[] Maintaining binary packages]

Exporting and distributing the binary packages will lead to useless storage consumption if the binary package list is not actively maintained.

### [[] Removing outdated binary packages]

In the [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") package an application called [eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean") is provided. It allows for maintaining Portage-related variable files, such as downloaded source code files, but also binary packages.

The following command will remove all binary packages that have no corresponding ebuild in the installed ebuild repositories:

`root `[`#`]`eclean packages`

For more details please read the [eclean](https://wiki.gentoo.org/wiki/Eclean "Eclean") article.

Another tool that can be used is the [qpkg](https://wiki.gentoo.org/wiki/Q_applets#Create_or_manipulate_binary_package_.28qpkg.29 "Q applets") tool from the [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]] package. However, this tool is a bit less configurable.

To clean up *unused* binary packages (in the sense of used by the server on which the binary packages are stored):

`root `[`#`]`qpkg -c`

### [[] Maintaining the Packages file]

** Tip**\
As of portage-3.0.52, Portage defaults to `FEATURES=pkgdir-index-trusted` for performance, which requires an accurate [Packages] index. This can be disabled if it is an inconvenience to regularly fix up the index with [emaint] after manual changes.

Inside the packages directory exists a [manifest file](https://en.wikipedia.org/wiki/Manifest_file "wikipedia:Manifest file") called [Packages]. This file acts as a cache for the metadata of all binary packages in the packages directory. The file is updated whenever Portage adds a binary package to the directory. Similarly, [eclean] updates it when it removes binary packages.

If for some reason binary packages are simply deleted or copied into the packages directory, or the [Packages] file gets corrupted or deleted, then it must be recreated. This is done using [emaint] command:

`root `[`#`]`emaint binhost --fix`

To clear the cache of *all* binary packages:

`root `[`#`]`rm -r /var/cache/binpkgs/*`

## [[] Advanced topics]

### [Chrooting]

If creating packages for a different [Portage profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles") or system with different USE flags, a [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") can be created.

** Note**\
This example uses [/var/chroot/buildenv] as the chroot path, but any path can be used.

#### [Creating the directories]

First, the directories for this chroot must be created:

`root `[`#`]`mkdir --parents /var/chroot/buildenv`

#### [Deploying the build environment]

Next, the appropriate *stage 3 tarball* must be downloaded and extracted, here the *desktop profile \| openrc* tarball is being used:

`/var/chroot/buildenv/ #``wget `[`https://bouncer.gentoo.org/fetch/root/all/releases/amd64/autobuilds/20230528T163158Z/stage3-amd64-desktop-openrc-20230528T163158Z.tar.xz`](https://bouncer.gentoo.org/fetch/root/all/releases/amd64/autobuilds/20230528T163158Z/stage3-amd64-desktop-openrc-20230528T163158Z.tar.xz)

This can be extracted with the following command:

`/var/chroot/buildenv/ #``tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner`

#### [Configuring the build environment]

** Important**\
If the target host uses multilib, and the build system does not, the kernel must be rebuilt to support it.

[KERNEL] **Enabling 32bit Emulation mode**

    Binary Emulations --->
      [*] IA32 Emulation
    General architecture-dependent options --->
      [*] Provide system calls for 32-bit time_t

[CODE] **Equivalent .config**

    CONFIG_IA32_EMULATION=y
    CONFIG_COMPAT_32BIT_TIME=y

The build environment should be configured to match that of the system it is building for. The simplest way to do this is to copy the [/etc/portage] and [/var/lib/portage/world] files. This can be done with **rsync**:

** Note**\
This command should be executed on the build target machine, where the remote host has the chroot.

`user `[`$`]`rsync --archive --whole-file --verbose /etc/portage/* larry@remote_host:/var/chroot/buildenv/etc/portage`

`user `[`$`]`rsync --archive --whole-file --verbose /var/db/repos/* larry@remote_host:/var/chroot/buildenv/var/db/repos`

** Note**\
This requires that *larry* has write privileges in this chroot, if using this method, it may make sense to clear the target directory, and give *larry* ownership of this directory, where it can later be changed to be owned by *root*. These permissions should be changed recursively:

`root `[`#`]`chown --recursive root:root /var/chroot/buildenv/etc/portage`

This process should be repeated for the world file:

`user `[`$`]`rsync --archive --whole-file --verbose /var/lib/portage/world larry@remote_host:/var/chroot/buildenv/var/lib/portage/world`

** Note**\
[/var/lib/portage] and [/var/lib/portage/world] should have the `root:portage` permissions.

#### [Configuring the chroot]

Once created, mounts must be bound for the chroot to work:

`/var/chroot/buildenv #``mount --types proc /proc proc`

`/var/chroot/buildenv #``mount --rbind /dev dev`

`/var/chroot/buildenv #``cp --dereference /etc/resolv.conf etc`

** Note**\
If a [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") is being used for [portage\'s temp dir](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs#fstab "Portage TMPDIR on tmpfs"), ensure that is mounted.

#### [Entering the chroot]

To enter this chroot, the following command can be used:

`/var/chroot/buildenv #``chroot . /bin/bash`

Optionally, the prompt can be set to reflect the fact that the chroot is active:

`/ #``export PS1="(chroot) $PS1"`

##### [Performing an initial build]

** Note**\
This step assumes this configuration has been completed: [Setting portage to use buildpkg](https://wiki.gentoo.org/wiki/Binary_package_guide#Implementing_buildpkg_as_a_Portage_feature "Binary package guide").

This step is optional, but rebuilds all packages in the new *world*:

`(chroot) #``emerge --emptytree @world`

### [[] Building for other architectures]

#### [crossdev]

** Note**\
This is a brief overview of how the process works, more information can be found at [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev")

[crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") is a tool to easily build cross-compile toolchains. This is useful to create binary packages for installation on a system whose [architecture](https://packages.gentoo.org/arches) differs from that of the system used to build the packages. A common example would be building binary packages for a device like an **[arm64]** [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") from a more powerful **[amd64]** desktop PC.

An installation guide for [[[sys-devel/crossdev]](https://packages.gentoo.org/packages/sys-devel/crossdev)[]] can be found at the [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") page.

##### [[] Build a cross compiler]

Using crossdev with the following command can build a toolchain for the desired system:

`root `[`#`]`crossdev --stable -t <arch-vendor-os-libc>`

For the rest of this section, the example target will be for a Raspberry Pi 4:

`root `[`#`]`crossdev --stable -t aarch64-unknown-linux-gnu`

After this has built, a toolchain will have been created in [/usr/aarch64-unknown-linux-gnu], and will look like a bare-bones Gentoo install where it is possible to edit [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") settings as normal.

** Tip**\
Replacing `aarch64-unknown-linux-gnu` with `aarch64-unknown-linux-musl` would build a system with the Musl libc rather than Glibc.

##### [[] Basic setup]

Removing the `-pam` flag from the `USE` line in [/usr/aarch64-unknown-linux-gnu/etc/portage/make.conf] is generally recommended in a setup like this:

[FILE] **`/usr/aarch64-unknown-linux-gnu/etc/portage/make.conf`Disable the pam USE flag**

    CHOST=aarch64-unknown-linux-gnu
    CBUILD=x86_64-pc-linux-gnu

    ROOT=/usr/$/

    ACCEPT_KEYWORDS="$"

    USE="$"

    CFLAGS="-O2 -pipe -fomit-frame-pointer"
    CXXFLAGS="$"

    FEATURES="-collision-protect sandbox buildpkg noman noinfo nodoc"
    # Ensure pkgs from another repository are not overwritten
    PKGDIR=$var/cache/binpkgs/

    #If you want to redefine PORTAGE_TMPDIR uncomment (and/or change the directory location) the following line
    PORTAGE_TMPDIR=$var/tmp/

    PKG_CONFIG_PATH="$usr/lib/pkgconfig/"
    #PORTDIR_OVERLAY="/var/db/repos/local/"

##### [[] Profiles]

List available profiles for the device by running:

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/aarch64-unknown-linux-gnu eselect profile list`

Next, select the profile that best suits:

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/aarch64-unknown-linux-gnu eselect profile set `

##### [[] Build a single package]

To build a single binary package for use on the device, use the following:

`root `[`#`]`emerge-aarch64-unknown-linux-gnu --ask foo`

##### [[] Build world file]

To build every package in the world file, then the following command is needed:

`root `[`#`]`emerge-aarch64-unknown-linux-gnu --emptytree @world`

##### [[] Binary location]

By default, all binary packages will be stored in [/usr/aarch64-unknown-linux-gnu/var/cache/binpkgs], so this is the location needed to be selected when [setting up a binary package host](https://wiki.gentoo.org/wiki/Binary_package_guide#Setting_up_a_binary_package_host "Binary package guide").

#### [QEMU chroot compiling]

Another method is to emulate the CPU of the other architecture using [QEMU virtualization software](https://en.wikipedia.org/wiki/QEMU) as if it was a normal chroot on the host system.

The pros of this method is that is simple to work with and are far less likely to run into cross compiling bugs which can save a lot of time. The downside is qemu can be around 10 times slower to compile and some of the more niches architectures, like HPPA are less used so there is a chance the user could be the first to discover a new QEMU bug.

** Tip**\
It is possible to merge both crossdev and qemu methods to cover all needs, however this is outside the scope of the guide to setup.

\
To setup QEMU cross compiling, just follow the excellent guide at [Embedded Handbook/General/Compiling with QEMU user chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_QEMU_user_chroot "Embedded Handbook/General/Compiling with QEMU user chroot") and then use native chroot guide from [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide#Configuring_the_chroot "Binary package guide")

### [[] Creating snapshots of the packages directory]

When deploying binary packages for a large number of client systems it might become worthwhile to create snapshots of the packages directory. The client systems then do not use the packages directory directly but use binary packages from the snapshot.

Snapshots can be created using the [/usr/lib/portage/python3.11/binhost-snapshot] tool that comes with Portage (note that the path to that tool may need to be adjusted to match the [python](https://wiki.gentoo.org/wiki/Python "Python") version with which Portage is installed). It takes four arguments:

1.  A source directory (the path to the packages directory).
2.  A target directory (that must not exist).
3.  A URI.
4.  A binary package server directory.

The files from the package directory are copied to the target directory. A [Packages] file is then created inside the binary package server directory (fourth argument) with the provided URI.

Client systems need to use an URI that points to the binary package server directory. From there they will be redirected to the URI that was given to [binhost-snapshot]. This URI has to refer to the target directory.

### [[] Understanding the binary package format]

#### [[] XPAK format]

XPAK format binary packages created by Portage have the file name ending with [.tbz2]. These files consist of two parts:

1.  A [.tar.bz2] archive containing the files that will be installed on the system.
2.  A [xpak] archive containing package metadata, the ebuild, and the environment file.

See [man xpak] for a description of the format.

In [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]] some tools exists that are able to split or create [tbz2] and [xpak] files.

The following command will split the [tbz2] into a [.tar.bz2] and an [.xpak] file:

`user `[`$`]`qtbz2 -s .tbz2`

The [.xpak] file can be examined using the [qxpak] utility.

To list the contents:

`user `[`$`]`qxpak -l .xpak`

The next command will extract a file called [USE] which contains the enabled USE flags for this package:

`user `[`$`]`qxpak -x package-manager-0.xpak USE`

#### [[] GPKG format]

GPKG format binary packages created by Portage have the file name ending with [.gpkg.tar]. These files consist of four parts at least:

1.  A [gpkg-1] empty file used to identify the format.
2.  A [C/PV/metadata.tar] archive containing package metadata, the ebuild, and the environment file.
3.  A [C/PV/image.tar] archive containing the files that will be installed on the system.
4.  A [Manifest] file containing checksums to protect against file corruption.
5.  Multiple optional [.sig] files containing OpenPGP signature are used for integrity checking and verification of trust.

The format can be extracted by [tar] without the need for additional tools.

### [[] The PKGDIR layout]

The currently used format version 2 has the following layout:

[CODE] **Packages directory layout (version 2)**

    PKGDIR
    `+- Packages
     +- app-accessibility/
     |  +- pkg1-version.tbz2
     |  `- pkgN-version.tbz2
     +- app-admin/
     |  `- ...
     `- ...

The [Packages] file is the major improvement (and also the trigger for Portage to know that the binary package directory uses version 2) over the first binary package directory layout (version 1). In version 1, all binary packages were also hosted inside a single directory (called [All/]) and the category directories only had symbolic links to the binary packages inside the [All/] directory.

In portage-3.0.15 and later, `FEATURES=binpkg-multi-instance` is enabled by default:

[CODE] **Packages directory layout (version 2 + FEATURES=binpkg-multi-instance)**

    PKGDIR
    `+- Packages
     +- app-accessibility/
     |  +- pkg1/
     |    +- pkg1-version-build_id.xpak
     |    `- pkgN-version-build_id.xpak
     +- app-admin/
     |  `- ...
     `- ...

### [[] Unpacking with quickunpkg]

Zoobab wrote a simple shell tool named [quickunpkg](https://github.com/zoobab/quickunpkg) to quickly unpack [tbz2] files.

## [Troubleshooting]

### [Undefined Reference Compiler Errors]

When using binary packages built on a different host, it\'s important to ensure the build host is using the same, or a lower version of [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] or [[[llvm-core/clang]](https://packages.gentoo.org/packages/llvm-core/clang)[]].

In other words, the system using the binary packages must have a compiler version greater than or equal to the binary host.

Failure to use appropriate versions can result in errors similar to:

[CODE]

    /usr/libexec/gcc/x86_64-pc-linux-gnu/ld: /usr/lib/gcc/x86_64-pc-linux-gnu/12/../../../../lib64/libSPIRV-Tools-opt.so: undefined reference to `std::ios_base_library_init()@GLIBCXX_3.4.32

** Note**\
The official Gentoo binary host delays changing the default compiler to a new stable GCC version to avoid this problem. Binary packages built on the official binhost have a lengthy window where they are still compatible with systems that have not *yet* upgraded GCC.

** Tip**\
Doing an *oneshot* update of the system compiler is generally sufficient to ensure remotely obtained binary packages function.

## [See also]

-   [Binary package quickstart](https://wiki.gentoo.org/wiki/Binary_package_quickstart "Binary package quickstart") --- how to install packages from the Gentoo binary package host, how to set up Portage to do this by default, and associated information on Gentoo binhost usage
-   [Emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- the main command-line interface to [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Project:Binhost](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost") --- aims to provide readily installable, precompiled packages for a subset of configurations, via central binary package hosting

## [External resources]

[quickpkg](https://dev.gentoo.org/~zmedico/portage/doc/man/quickpkg.1.html) man page.