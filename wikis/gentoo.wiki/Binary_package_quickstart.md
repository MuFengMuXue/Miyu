This page contains [[changes](https://wiki.gentoo.org/index.php?title=Gentoo_Binary_Host_Quickstart&diff=1440214)] which are not marked for translation.

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost]\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost")][Project](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost")

[[]][GitWeb](https://gitweb.gentoo.org/proj/binhost.git)

[[]][Bugs (upstream)](https://bugs.gentoo.org/buglist.cgi?component=Binary+packages+support)

[[]][[#gentoo-binhost](ircs://irc.libera.chat/#gentoo-binhost)] ([[webchat](https://web.libera.chat/#gentoo-binhost)])

Gentoo offers prebuilt binary packages through the **Gentoo binary package host**, for quicker and easier package [installation](https://wiki.gentoo.org/wiki/Emerge#Install_a_package "Emerge") and [updates](https://wiki.gentoo.org/wiki/Update "Update"). Also called the **Gentoo binhost** for short, it provides thousands of packages that can be installed without the need to compile code locally, or to install build-time dependencies, giving Gentoo users even more choice and convenience!

The Gentoo binhost leverages [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")\'s longstanding [support for binary packages](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") to systematically provide a huge array of prebuilt packages. It hosts commonly used packages, for a range of common [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") configurations, for several system architectures, and with optional optimizations for more recent hardware.

The Gentoo binhost delivers resource-light package installation, for the common case where building with very specific, custom compiler flags is not required. It is important to highlight that using binary packages from the Gentoo binhost in no way diminishes the power, choice, or freedom afforded to Gentoo users; on the contrary, it provides one more useful option for many common use-cases, for an even smoother Gentoo experience. Of course, users who require packages built with specific CFLAGS not available from the Gentoo binhost will not usually use it\'s packages.

A common way to use the Gentoo binhost is to have Portage default to installing using binary packages whenever such a package is available for the requested USE flag configuration, but to transparently build packages locally to the user\'s specification when there is no appropriate binary package available. Gentoo deployments configured this way still allow the usual full control over the system, with all USE flags still available to be customized, just with the added benefit of faster package installation whenever possible.

The **[amd64]** (x86-64) and **[arm64]** (aarch64) architectures are currently much more widely supported than other architectures - see the [available packages](#Available_packages_and_update_schedule) section. The [available packages and configurations](https://wiki.gentoo.org/wiki/Gentoo_binhost/Available_packages_and_configurations "Gentoo binhost/Available packages and configurations") subpage gives details of what USE flags packages are available for, and wish CFLAGS they use.

This article explains how to install packages from the Gentoo binary package host, how to set up Portage to do this by default, and associated information on Gentoo binhost usage.

** See also**\
The [binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") has more general information on binary packages and binary package hosts on Gentoo. The [binhost project](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost") page has information about the development of the Gentoo binhost.

\

The [news item announcing the Gentoo Binhost\'s official launch](https://www.gentoo.org/news/2023/12/29/Gentoo-binary.html) has some interesting details, so does the [news item from when x86-64-v3 binary packages became available](https://www.gentoo.org/news/2024/02/04/x86-64-v3.html).

## Contents

-   [[1] [The Gentoo binhost]](#The_Gentoo_binhost)
    -   [[1.1] [Appropriate use-cases]](#Appropriate_use-cases)
    -   [[1.2] [Unsuitable use-cases]](#Unsuitable_use-cases)
    -   [[1.3] [Available packages and update schedule]](#Available_packages_and_update_schedule)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Make the Gentoo binhost available to Portage (binrepos.conf)]](#Make_the_Gentoo_binhost_available_to_Portage_.28binrepos.conf.29)
    -   [[2.2] [Configure Portage to use binary packages by default]](#Configure_Portage_to_use_binary_packages_by_default)
    -   [[2.3] [Package signature verification]](#Package_signature_verification)
    -   [[2.4] [Emerge options and EMERGE_DEFAULT_OPTS]](#Emerge_options_and_EMERGE_DEFAULT_OPTS)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Emerging a single binary package]](#Emerging_a_single_binary_package)
    -   [[3.2] [Update the system using binary packages]](#Update_the_system_using_binary_packages)
-   [[4] [Frequently asked questions]](#Frequently_asked_questions)
    -   [[4.1] [I used to have a binary package but not anymore, what happened?]](#I_used_to_have_a_binary_package_but_not_anymore.2C_what_happened.3F)
    -   [[4.2] [Portage still tries to compile from source]](#Portage_still_tries_to_compile_from_source)
    -   [[4.3] [Preferring binary to source for particular packages]](#Preferring_binary_to_source_for_particular_packages)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Emerge complains with \"there are no binary packages to satisfy \\"]](#Emerge_complains_with_.22there_are_no_binary_packages_to_satisfy_.3Cpackage.3E.22)
    -   [[5.2] [keyblock resource: \'/etc/portage/gnupg/pubring.kbx\': No such file or directory]](#keyblock_resource:_.27.2Fetc.2Fportage.2Fgnupg.2Fpubring.kbx.27:_No_such_file_or_directory)
    -   [[5.3] [Preexisting /etc/portage/gnupg directory]](#Preexisting_.2Fetc.2Fportage.2Fgnupg_directory)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [The Gentoo binhost]

### [Appropriate use-cases]

The Gentoo binhost brings some key benefits that will help determine when it suits individual use-cases:

-   Faster package installation and upgrades, up to orders of magnitude quicker depending on the package and hardware
-   Limited storage and RAM requirements when installing larger packages (i.e., some packages need X GB of RAM during compilation)
-   Older systems can be set up rapidly and maintained without waiting longer than needed for packages to build (compile)
-   Fast updates and fast set-up time for cloud instances

The Gentoo binhost can be invaluable when installing Gentoo Linux, making for easier and potentially much faster installations.

### [Unsuitable use-cases]

The binary packages from the Gentoo binhost are built with preset compiler options. If there is the need to set options such as `-march` to a value not available for packages in the Gentoo binhost, then of course it will not be useful. Some `-march` settings can reportedly give up to a 5% boost on x86-64 processors for some cases. Of course if these optimizations are required, packages can always be built locally, even when mixing binary packages into the installation.

The Gentoo binhost can only provide binary packages if the locally-requested [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") combination is not changed from the default setting(s) used for the creation of the binary packages. If the user requests non-default USE flags for a package, then the package will need to be compiled locally. Portage can automatically either install from a binary package by default, or build a package locally when needed.

### [Available packages and update schedule]

The Gentoo binhost currently has strong support for the **[amd64]** (x86-64) and **[arm64]** (aarch64) architectures, for which it supplies packages that are known to be commonly installed on desktop systems. Such packages include the [KDE Plasma](https://wiki.gentoo.org/wiki/KDE "KDE") and [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"), and productivity packages such as [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") or [TeX Live](https://wiki.gentoo.org/wiki/TeX_Live "TeX Live"), for example. For these architectures, the binary packages are updated *daily*.

Other [architectures and system types](https://packages.gentoo.org/arches) have more basic support on the Gentoo binhost, and are furnished with core packages only. The binary packages for these architectures are updated approximately once a week.

See the [available packages and configurations](https://wiki.gentoo.org/wiki/Gentoo_binhost/Available_packages_and_configurations "Gentoo binhost/Available packages and configurations") subpage for more details.

## [Configuration]

### [][Make the Gentoo binhost available to Portage (binrepos.conf)]

To be able to use packages from the Gentoo binhost, Portage must be configured to be able to find it. Older installations will have to configure this manually, but more recent installations use new [Stage3](https://www.gentoo.org/downloads/) files which come with the Gentoo binhost preconfigured and ready to use, and the handbook explains during installation how to [set it to be used by default](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Optional:_Adding_a_binary_package_host "Handbook:AMD64/Installation/Base").

Follow this section to customize the Gentoo binhost configuration, or on systems that were installed before Gentoo binhost configuration was provided by default in Stage3 installation tarballs.

Using a [local Gentoo mirror](https://www.gentoo.org/downloads/mirrors/) is highly recommend to reduce server load and to speed up downloads on the local end. Portage uses files in the directory [/etc/portage/binrepos.conf] to find binary package hosts, and here are some example configuration files for different mirrors and architectures:

[FILE] **`/etc/portage/binrepos.conf/gentoobinhost.conf`CDN Mirror Example, amd64**

    [gentoo]
    priority = 9999
    sync-uri = https://distfiles.gentoo.org/releases/amd64/binpackages/23.0/x86-64/

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/gentoo

[FILE] **`/etc/portage/binrepos.conf/gentoobinhost.conf`UK Mirror Example, amd64**

    [gentoo]
    priority = 9999
    sync-uri = https://www.mirrorservice.org/sites/distfiles.gentoo.org/releases/amd64/binpackages/23.0/x86-64/

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/gentoo

[FILE] **`/etc/portage/binrepos.conf/gentoobinhost.conf`CN Mirror Example, arm64**

    [gentoo]
    priority = 9999
    sync-uri = https://mirrors.aliyun.com/gentoo/releases/arm64/binpackages/23.0/arm64

    # Introduced in portage-3.0.74 for per-repo verification choices
    verify-signature = true
    # Default value with >=portage-3.0.77
    location = /var/cache/binhost/gentoo

The `sync-uri` in [binrepos.conf] contains at its end the local system architecture and type of installation. The examples above are given for normal amd64 or arm64 installations. .

** Note**\
An x86-64-v3 directory exists, which is strongly recommended *if* your CPU supports that microarchitecture level. For more details, see [the news article](https://www.gentoo.org/news/2024/02/04/x86-64-v3.html).

** Note**\
When using a hardened, musl, llvm [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), x32, or even an entirely different architecture, these paths are not correct. Corresponding directories exist, but have only the package set found within the stage3.

### [Configure Portage to use binary packages by default]

To automatically download and use a binary package when a suitable one is available on the servers, enable the [getbinpkg] Portage feature:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="getbinpkg"

If no suitable binary package can be found, the package will be compiled from source as usual.

** Warning**\
Currently, if a package with [user patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches") is installed, it will be fetched from the binary package host anyway, and the user patches themselves won\'t be applied. [[[bug #917047]](https://bugs.gentoo.org/show_bug.cgi?id=917047)[]]

This can be fixed by excluding any packages with user patches from using the binhost:

[FILE] **`/etc/portage/make.conf`Exclude package ATOM from using the binhost**

    EMERGE_DEFAULT_OPTS="$ --usepkg-exclude ATOM"

### [Package signature verification]

Now, enable the `binpkg-request-signature` Portage feature to require verification of GPG signatures:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="binpkg-request-signature"

Once binary packages have to be downloaded, [emerge] will automatically run the Gentoo Trust Tool known as [getuto] to set up a ring of GPG keys that are trusted for binary package installation.

If hitting issues, the [preexisting /etc/portage/gnupg directory](#Preexisting_.2Fetc.2Fportage.2Fgnupg_directory) may help.

### [Emerge options and EMERGE_DEFAULT_OPTS]

Below are some useful settings that can be applied via `EMERGE_DEFAULT_OPTS` in [make.conf] or on the [emerge] command line to improve the experience of working with Gentoo binary packages.

\--getbinpkg (-g)

** Note**\
This option should still be supplied when using the other options in this section.

Adding `--getbinpkg` will automatically download and use a binary package when a suitable one is available on the servers. If no suitable binary package can be found, the package will be compiled from source as usual.

\--usepkgonly (-K)

Using `--usepkgonly` will tell Portage to only use binary packages and exit if no suitable one can be found locally or (with -g) for download.

\--with-bdeps=y

This can be set to y(es) or n(o) and controls whether build dependencies of packages are downloaded and/or installed.

For binary package installation, it defaults to no. For source-based installation, the build dependencies are required and are accordingly also installed.

\--binpkg-respect-use=y

** Warning**\
Do not set `--binpkg-respect-use=n` lightly, in `EMERGE_DEFAULT_OPTS` or otherwise. It will break the system.

\* By default, Portage will accept binary packages only if use flags match the precise requirements and compile the package from source otherwise. It will also log a warning: \"The following binary packages have been ignored due to non matching USE\"

\* When the option is explicitly set to y(es), the warning is disabled.

\* When the option is explicitly set to n(o), the differences between a user\'s configuration and the configuration used to make the binary package are ignored, and the binary package is installed anyway. [** Warning:** Dangerous.]

In some cases, it is desirable to sacrifice choice of USE flags in order to expand the number of binary packages that can be installed. Leaving the option unset is therefore useful, because portage will print possible package.use lines which can be used to opt in to those binaries. Otherwise, it is best to set the option to y(es).

## [Usage]

If Portage is not configured to use binary packages from the Gentoo binhost by default in the `EMERGE_DEFAULT_OPTS`, binary packages can still be used selectively when emerging packages.

### [Emerging a single binary package]

To install a single package using the binhost, add the `--getbinpkg` (`-g`) switch as in the example below:

`root `[`#`]`emerge --ask --verbose --getbinpkg app-editors/nano`

Or the shorthand:

`root `[`#`]`emerge -avg app-editors/nano`

### [Update the system using binary packages]

To perform a full system update using the binhost use:

`root `[`#`]`emerge --ask --verbose --update --deep --changed-use --getbinpkg @world`

Or shorthand:

`root `[`#`]`emerge -avuDUg @world`

## [Frequently asked questions]

Various questions are covered in the Gentoo news *[Gentoo goes Binary!](https://www.gentoo.org/news/2023/12/29/Gentoo-binary.html)*.

Review the frequently asked questions before [asking for help](https://wiki.gentoo.org/wiki/Support "Support") when using the Gentoo binhost.

### [][I used to have a binary package but not anymore, what happened?]

Builds are scheduled around 5am EST and may take a couple hours to finish building (except when dev-libs/icu has a major version bump, in which case you will have to wait all day because there is just SO MUCH to rebuild. Sorry about that!) Try waiting a bit. Getting in the habit of doing your daily updates later in the day might help too. You may also wish to keep an eye on [[[bug #924772]](https://bugs.gentoo.org/show_bug.cgi?id=924772)[]].

Note that some additional packages are also built by lottery every day. Winning that lottery one day doesn\'t guarantee it will be built the next time that package gets a version bump.

### [Portage still tries to compile from source]

If there is a binary package available on a binhost but Portage is not using it, it may well be because of a mismatch between the [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") that were requested to install the package with, and the USE flags that were applied to build the binary package.

The USE flags that were used to build the available binary package may be listed by using the following command:

`user `[`$`]`emerge --pretend --verbose --getbinpkg --usepkgonly --binpkg-respect-use=n `

To allow Portage to install from the available binary package, adjust the requested USE flags accordingly, in [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") or [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use").

### [Preferring binary to source for particular packages]

There is currently no way to specify that the binary version of a particular package should be preferred to the source version. The functionality is planned, but there is no specific timeline for implementation at this stage.^[\[1\]](#cite_note-1)^ Refer to [bug 463964](https://bugs.gentoo.org/463964) and [bug 924772](https://bugs.gentoo.org/924772).

## [Troubleshooting]

### [][Emerge complains with \"there are no binary packages to satisfy \\"]

If `--getbinpkg` (`-g`) isn\'t supplied, Portage won\'t search the binhost for binary packages, even if `--usepkgonly` (`-K`) is supplied.

If `--getbinpkg` is being supplied to portage, users should make sure the package exists on the binhost by visiting the URL in [/etc/portage/binhost.conf] in a web browser.

### [][keyblock resource: \'/etc/portage/gnupg/pubring.kbx\': No such file or directory]

The keyring in [/etc/portage/gnupg/] needs to be generated. If [/etc/portage/gnupg/] does not exist, run [getuto].

If that directory does exist, follow the instructions in the [next section](#Preexisting_.2Fetc.2Fportage.2Fgnupg_directory).

### [][Preexisting /etc/portage/gnupg directory]

In the past, [/etc/portage/gnupg] may have been used for older methods of verifying the Gentoo repository. If it exists, *getuto* won\'t override it, but the correct settings may be missing. If hitting issues, move away the old directory, then run [getuto] again:

`root `[`#`]`mv /etc/portage/gnupg /etc/portage/gnupg.bak ; getuto`

## [See also]

-   [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") --- in-depth **binary package** creation, distribution, use, and maintenance
-   [Emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- the main command-line interface to [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.
-   [Project:Binhost](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost") --- aims to provide readily installable, precompiled packages for a subset of configurations, via central binary package hosting

## [References]

1.  [[[↑](#cite_ref-1)] [[Gentoo forums post](https://forums.gentoo.org/viewtopic-p-8819825.html#8819825). Accessed on 2024-03-17.]]