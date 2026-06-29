Like all healthy software projects, developing Gentoo requires *lots* of testing. This article provides information for ebuild developers on **testing ebuilds**.

It is preferred that arch-specific ebuild testing takes place on a real system, inside a [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot"), or within another type of non-virtualized container. Virtualization may be acceptable in situations where it is not possible or practical to test on real hardware.

Testing can be separated to generic \"version bump\" tests, stabilization work and keywording work. For stabilization it\'s important that the [test environment](https://wiki.gentoo.org/wiki/Test_environment "Test environment") only has stable packages installed, with no unstable ebuilds present (keyworded or unmasked). In any case, the test environment should be up-to-date, and it is recommended to have as few packages installed as possible. This will aid in finding missing dependencies. You should always aim to test each version bump as thoroughly as possible.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [make.conf and test.conf files]](#make.conf_and_test.conf_files)
-   [[2] [Testing]](#Testing)
    -   [[2.1] [General]](#General)
        -   [[2.1.1] [USE flags]](#USE_flags)
        -   [[2.1.2] [Runtime testing]](#Runtime_testing)
        -   [[2.1.3] [Emerge testing dependencies]](#Emerge_testing_dependencies)
    -   [[2.2] [Libraries]](#Libraries)
    -   [[2.3] [Kernel]](#Kernel)
    -   [[2.4] [Toolchain]](#Toolchain)
    -   [[2.5] [Emacs packages]](#Emacs_packages)
-   [[3] [Tools]](#Tools)
    -   [[3.1] [pkg-testing-tools]](#pkg-testing-tools)
    -   [[3.2] [pkgdev tatt]](#pkgdev_tatt)
        -   [[3.2.1] [Local package testing]](#Local_package_testing)
        -   [[3.2.2] [Bugzilla package testing using Nattka]](#Bugzilla_package_testing_using_Nattka)
    -   [[3.3] [tatt]](#tatt)
        -   [[3.3.1] [Configuration]](#Configuration_2)
        -   [[3.3.2] [Sample workflow]](#Sample_workflow)
-   [[4] [QA violations]](#QA_violations)
-   [[5] [Architecture-specific notes]](#Architecture-specific_notes)
    -   [[5.1] [amd64]](#amd64)
    -   [[5.2] [arm]](#arm)
    -   [[5.3] [x86]](#x86)
-   [[6] [See also]](#See_also)

## [Configuration]

### [make.conf and test.conf files]

This setup has a basic [/etc/portage/make.conf] with a more sophisticated [/etc/portage/env/test.conf] for use with packages that need testing. The [[make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] file should have settings similar to the following:

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-march=native -O2 -pipe -frecord-gcc-switches"
    CXXFLAGS="$"
    FFLAGS="$"
    FCFLAGS="$"
    LDFLAGS="$ -Wl,--defsym=__gentoo_check_ldflags__=0"

    ACCEPT_LICENSE="*"

    GENTOO_MIRRORS="https://distfiles.gentoo.org"

    PORTAGE_TMPDIR="/var/tmp"

    PORTAGE_ELOG_CLASSES="log warn error qa"

    # Add settings specific to your environment
    MAKEOPTS="-j16"

    EMERGE_DEFAULT_OPTS="--nospinner --jobs=8"
    FEATURES="parallel-fetch parallel-install"

    # These checks are from app-portage/iwdevtools, enable per-package separately.
    QA_CMP=n
    QA_SED=n
    QA_VDB=n

This is easily achievable with some arch-testing tools, such as [[[app-portage/pkg-testing-tools]](https://packages.gentoo.org/packages/app-portage/pkg-testing-tools)[]], but even by editing [/etc/portage/package.env] manually with little effort.

** Warning**\
The MAKEOPTS value should be modified accordingly to the host system.

Then the [env/test.conf] file:

[FILE] **`/etc/portage/env/test.conf`**

    # -frecord-gcc-switches (if present in all of CFLAGS, CXXFLAGS, FFLAGS, FCFLAGS) detects missing CFLAGS usage
    COMMON_FLAGS="-march=native -O2 -pipe -frecord-gcc-switches"

    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"

    # You can use $ here, but please remember to include as-needed manually then.
    # Enables a Portage QA check to report when LDFLAGS is not respected
    LDFLAGS="$ -Wl,--defsym=__gentoo_check_ldflags__=0"

    # ipc-sandbox - prevent host IPC access (requires Linux and namespace support in kernel)
    # network-sandbox - prevent network access during merge (requires Linux and network namespace support in kernel)
    # protect-owned - prevent a package from overwriting files it does not own
    # sandbox - ensure package does not write directly to live system
    # split-log - store logs created by PORTAGE_ELOG_SYSTEM="save" in category subdirectories
    # split-elog - store build logs in category subdirectories
    # strict - have portage react strongly to conditions that have the potential to be dangerous
    # test - run package tests, or alternatively test-fail-continue
    # userfetch - drop privileges during fetching
    # userpriv - drop privileges during merge
    # usersandbox - enable sandbox when userpriv is enabled
    FEATURES="ipc-sandbox network-sandbox protect-owned sandbox split-log split-elog strict test userfetch userpriv usersandbox"

    # Note: FEATURES="parallel-install" may result in not seeing some QA warnings for e.g.
    # xdg db/cache updates.
    FEATURES="$ -parallel-install"

    # Display selected types of messages again when emerge exits, and save them to disk
    PORTAGE_ELOG_CLASSES="log warn error qa"
    PORTAGE_ELOG_SYSTEM="echo save"

    # Attempts to detect correct setuptools usage with setup.py python packages.
    DISTUTILS_STRICT_ENTRY_POINTS=1

    # Disables network-sandboxing from test phase if PROPERTIES="test_network" is set in the ebuild.
    # See https://mgorny.pl/articles/the-ultimate-guide-to-eapi-8.html#properties-test-network-to-ease-reenabling-tests-requiring-internet.
    ALLOW_TEST="network"

    # Used to control what additional QA checks app-portage/iwdevtools provides for us.
    # Please refer to upstream for documentation. Still highly experimental!
    IWDT_ALL=y
    QA_CMP=y
    QA_CMP_ARGS="-xS"
    QA_SED=y
    QA_VDB=y

The `QA_`\* variable define checks included with the [[[app-portage/iwdevtools]](https://packages.gentoo.org/packages/app-portage/iwdevtools)[]] package. All flags and features can be found on [make.conf.5](https://dev.gentoo.org/~zmedico/portage/doc/man/make.conf.5.html) (or [man 5 make.conf]) where they are explained.

** Important**\
If `QA_`\* checks are enabled from iwdevtools, the [/etc/portage/bashrc] will need to include the following:

[FILE] **`/etc/portage/bashrc`**

    # Import the whole set
    source /usr/share/iwdevtools/bashrc
    # Alternatively, source the files individually
    #source /usr/share/iwdevtools/qa-cmp.bashrc
    #source /usr/share/iwdevtools/qa-sed.bashrc
    #source /usr/share/iwdevtools/qa-vdb.bashrc

    #post_pkg_preinst()

    #post_pkg_postinst()

Note that iwdevtools can be used separately with provided scripts, it doesn\'t need to be integrated with Portage hooks to be effective.

## [Testing]

Each ebuild in Gentoo is different and therefore requires a slightly different approach to stabilization. Consider the following guidelines for each class of package. Use common sense when in doubt.

### [General]

#### [USE flags]

While it is preferable to test every [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") combination, this is not always possible or appropriate. The ebuild may have a large number of USE flags, a long compile time, or the stabilization in question may just not call for it.

In cases where all USE flags combinations are not being tested, it is still recommended to test:

-   With all USE flags enabled.
-   With all USE flags disabled.
-   The default USE flag settings.

Note that arch-testing tools, such as tatt and pkg-testing-tools, provide functionality to test random combinations of USE flags.

#### [Runtime testing]

Consider the level of runtime testing that is required for the target package. Remember, the focus of stabilization is to integrate a testing ebuild into stable and not to identify routine upstream bugs or regressions - that is the purpose of the ebuild\'s 30 day wait time in while it\'s marked as unstable (\~ARCH).

The level of runtime testing required will vary wildly based on a variety of factors. Consider the following examples:

-   Multiple days of \"normal use\" testing may be appropriate for a new version of [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]].
-   Basic functionality testing, such as browsing some web pages, may make sense for a new version of [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]].
-   Passing tests might be enough for [[[dev-python/yenc]](https://packages.gentoo.org/packages/dev-python/yenc)[]].
-   A leaf package such as [[[kde-apps/kcalc]](https://packages.gentoo.org/packages/kde-apps/kcalc)[]] may not require any runtime testing at all.

#### [Emerge testing dependencies]

[portage] has a feature to compile all the testing dependencies before running tests which can be called with the flag `--with-test-deps`, this is useful to stop the system pulling and running tests on packages that don\'t require testing in the depgraph.

An example of this would be:

`root `[`#`]`emerge --ask --verbose --oneshot --with-test-deps dev-lang/perl`

### [Libraries]

A new library version may introduce incompatibles with reverse dependencies. Where there is a risk of such breakage, each stable reverse dependency must be rebuilt. Beware of reverse dependencies that only use the library conditionally (eg. `USE="png"`).

### [Kernel]

Kernel ebuilds referenced in the Handbook have certain exemptions from the usual stabilization policy, so stabilization requests are normally only filed for the first version in a long term stable branch (subsequent versions can be stabilized at the discretion of the maintainer).

First, test all available kernel options:

`user `[`$`]`cd /usr/src/example-sources-1.2.3 `

`user `[`$`]`make allyesconfig `

`user `[`$`]`make # add '-j' as appropriate for the hardware `

If that succeeds, build with a normal kernel configuration:

`user `[`$`]`make distclean `

`user `[`$`]`make menuconfig `

`user `[`$`]`make `

`user `[`$`]`make modules_install # if you use modules `

After reboot, check [dmesg] for anything strange and use the system as normal, trying to get a bit of uptime.

If stabilizing a special feature variant such as [[[sys-kernel/hardened-sources]](https://packages.gentoo.org/packages/sys-kernel/hardened-sources)[]], try to test relevant features.

### [Toolchain]

New versions of toolchain packages can often introduce major changes and widespread breakage into the Gentoo ebuild repository. The purpose of a stabilization request for a toolchain package is to test the package itself on each architecture - not to detect build failures in miscellaneous packages. It is expected that such failures are managed and resolved by the maintainer (normally through tracker bugs and tinderboxing) prior to filing a stabilization request.

See the Toolchain Project\'s [notes](https://wiki.gentoo.org/wiki/Project:Toolchain#Packaging_notes "Project:Toolchain") for more.

Once the normal testing is successful, rebuild [`@system`](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") (or [`@world`](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") if the hardware permits) and once successful, observe the system in normal operation for abnormalities.

### [Emacs packages]

Some Emacs packages need testing when being keyworded or stabilised, so a detailed [test plan](https://wiki.gentoo.org/wiki/Project:Emacs/Test_plans "Project:Emacs/Test plans") was created for them.

## [Tools]

### [pkg-testing-tools]

Install the tool.

`root `[`#`]`emerge --ask app-portage/pkg-testing-tools`

[[[app-portage/pkg-testing-tools]](https://packages.gentoo.org/packages/app-portage/pkg-testing-tools)[]] is an alternative to tatt. Its strengths are ease-of-use and JSON format reports. Please refer to [upstream](https://github.com/APN-Pucky/pkg-testing-tools) for documentation, or use [pkg-testing-tool \--help].

[pkg-testing-tools] doesn\'t require any configuration to be usable. It\'s very simple and therefore has a shallow learning curve. Integrating it to daily ebuild dev work is strongly encouraged.

At minimum you should have a [/etc/portage/env/test.conf] file with some test-specific settings defined. Please see [#make.conf\_.26_test.conf](#make.conf_.26_test.conf).

By default [pkg-testing-tools] disables some USE flags. Such as `debug`, `doc`, etc, that aren\'t too important when making sure the source code compiles. However when using the tool on version bumps, to make sure everything in the ebuild works, it may be a good idea to expand the USE flag pool that is being tested. It is easy to edit the source afterwards, but there are also [example patches](https://github.com/juippis/my-gentoo-lxd-scripts/tree/master/pkg-testing-tool-patches) available, that can be dropped into [/etc/portage/patches]. By default the tool also disables `--autounmask` feature, which makes sense on stabilizing work since it can accidentally autounmask \~unstable packages, but when the tool is used along with version bumps, you may want autounmasking feature to solve different USE flag combinations automatically.

One downside compared to [tatt] is that [pkg-testing-tools] does not have a way to test *reverse* dependencies. [tatt] has a built-in feature for that. You can always find reverse dependencies of a package from [https://qa-reports.gentoo.org/](https://qa-reports.gentoo.org/) or simply from [https://packages.gentoo.org/](https://packages.gentoo.org/). There is a [simple](https://github.com/juippis/my-gentoo-lxd-scripts/blob/master/container/bin/rdeptester.sh) script to pair [pkg-testing-tools] with [https://qa-reports.gentoo.org/](https://qa-reports.gentoo.org/) but it is not suitable for stabilization workflow. [eix] can be further paired with the two to find stable reverse dependencies of an atom.

  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Tool argument             Description
  -p                        Specify the package atom we\'re testing via *-p \'=cat/pn-ver\'*
  \--append-emerge          Give extra emerge arguments (`EMERGE_DEFAULT_OPTS`).
  \--append-required-use    Enable/disable certain USE flags. Can also be used by exporting USE flag before calling the tool.
  \--binpkg                 Append \--usepkg to emerge command and add buildpkg to FEATURES. Also controllable via [make.conf].
  \--max-use-combinations   Specify the amount runs per package.
  \--test-feature-scope     When to enable *FEATURES=\"test\"*: never, once per whole run, or always.
  \--report                 Specify optional report path, and filename.
  \--extra-env-file         Specify optional [env/\*] file to be used.
  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Example commands:

`user `[`$`]`pkg-testing-tool --append-emerge '--autounmask=y' --extra-env-file 'test.conf' --test-feature-scope once --max-use-combinations 6 -p '=app-emulation/lxd-4.0.7'`

Uses [env/test.conf] specific settings only for the testable atom, does a run with *FEATURES=\"test\"* once, and does 6 different use-combination runs at max while also enabling autounmask features.

`user `[`$`]`pkg-testing-tool --append-emerge '--autounmask=y' --extra-env-file 'test.conf' --test-feature-scope never --max-use-combinations 12 --append-required-use '!profile' --report /var/tmp/portage/logs/efl-1.25.1-r11-report.json -p '=dev-libs/efl-1.25.1-r11'`

Uses [env/test.conf] specific settings only for the testable atom, never does a run with *FEATURES=\"test*, does 12 runs with different USE flag combinations, enables autounmasking features, appends *USE=\"-profile\"* globally and writes a report into [/var/tmp/portage/logs/].

### [pkgdev tatt]

[[[dev-util/pkgdev]](https://packages.gentoo.org/packages/dev-util/pkgdev)[]] has a **tatt** module that can be used to test packages.

Run [pkgdev tatt -h] for an overview. **pkgdev tatt** reads configuration from [\~/.config/pkgdev/pkgdev.conf]

\

#### [Local package testing]

Examples:

Run one compile-test with default use flags, by using [env/test.conf] on the specified atom:

`user `[`$`]`pkgdev tatt --use-default --extra-env-file test.conf -p =www-client/firefox-122.0.1 -j tatt-firefox `

`user `[`$`]`./tatt-firefox.sh`

Run compile-test with default use flags and run once with `FEATURES="test"`, include settings from [env/test.conf]:

`user `[`$`]`pkgdev tatt --use-default --extra-env-file test.conf -t -p =media-video/yle-dl-20240130 -j tatt-yle-dl `

`user `[`$`]`./tatt-yle-dl.sh`

Run compile-tests with 6 different use flag combinations, do one run with `FEATURES="test"`, enable autounmasking via `--emerge-opts` and include settings from [env/test.conf]:

`user `[`$`]`pkgdev tatt --emerge-opts="--autounmask=y --verbose" --use-combos 6 --extra-env-file test.conf -t -p =category/package-version -j tatt-package `

`user `[`$`]`./tatt-package.sh`

**pkgdev tatt** will output a [./tatt-package.report] report about successful and failed builds.

If you need to test a package without KEYWORDS, add `-k` flag to **pkgdev tatt** command.

#### [Bugzilla package testing using Nattka]

TODO

### [tatt]

[[[app-portage/tatt]](https://packages.gentoo.org/packages/app-portage/tatt)[]] is a tool designed to automate some of the repetitive tasks involved in arch testing. Currently only version 9999 supports working with a git ebuild repository and the Bugzilla atom field.

For each job, tatt produces a series of scripts allowing the user to control exactly what is performed:

  ------------- -----------------------------------------------------------------------------------------------------
  Script name   Function
  cleanup       Removes generated scripts and atoms from the keyword file
  commit        Commits the keyword changes to the repository
  rdeps         Compiles a selection of stable reverse dependencies
  success       Reports a successful stabilization to the bug, removing the arch from CC and closing if appropriate
  useflags      Builds the atoms with various USE flag combinations
  ------------- -----------------------------------------------------------------------------------------------------

#### [Configuration]

tatt has a variety of configuration options (see [man 5 tatt]), but there is a few that must be set to ensure useful operation of all functions.

[FILE] **`~/.tatt`**

    # architecture to use for keyword changes and bug updates
    arch=amd64

    # success message to print on bugs
    successmessage=@@ARCH@@ stable

    # repository to work in when committing keyword changes
    repodir=/home/dev/gentoo

    # API key to authenticate with bugzilla for updating/closing bugs
    # generate at https://bugs.gentoo.org/userprefs.cgi?tab=apikey
    bugzilla-key=XXX

#### [Sample workflow]

First, start a new job:

`user `[`$`]`tatt -b 590118`

    Bugnumber:  590118
    Stabilization bug detected.
    Jobname: writerperfect
    Found the following package atom : =app-text/writerperfect-0.9.5
    =app-text/writerperfect-0.9.5 already in /etc/portage/package.keywords/archtest
    No stable rdeps for writerperfect
    Success Report script written to writerperfect-success.s
    Commit script written to writerperfect-commit.sh

Now the various scripts are available for use:

`user `[`$`]`ls`

    writerperfect-cleanup.sh  writerperfect-commit.sh  writerperfect-success.sh  writerperfect-useflags.sh

Next, build the package and perform whatever testing is necessary:

`root `[`#`]`./writerperfect-useflags.sh`

`user `[`$`]`writerperfect`

A report is also produced summarizing the build status of each USE flag combination:

`user `[`$`]`cat writerperfect.report`

    USE='-abiword -cdr -ebook -freehand -gsf -keynote -mspub -mwaw -pagemaker -visio -wpd -wpg -wps' : REQUIRED_USE not satisfied (probably)
    USE='abiword cdr ebook -freehand gsf -keynote mspub mwaw pagemaker visio -wpd -wpg -wps'  succeeded for =app-text/writerperfect-0.9.5
    USE='abiword cdr ebook freehand gsf keynote mspub mwaw pagemaker visio wpd wpg wps'  succeeded for =app-text/writerperfect-0.9.5
     FEATURES= test succeeded for =app-text/writerperfect-0.9.5

Once everything looks good, commit the keyword change:

`user `[`$`]`./writerperfect-commit.sh`

    writerperfect-0.9.5: amd64 ~x86 ~x86-linux ~x86-solaris

    RepoMan scours the neighborhood...
    RepoMan sez: "If everyone were like you, I'd be out of business!"

    RepoMan scours the neighborhood...
    >>> Creating Manifest for /home/michael/dev/gentoo/gentoo/app-text/writerperfect

    Note: use --include-dev (-d) to check dependencies for 'dev' profiles

    * 1 files being committed...
    [master fe834f9] app-text/writerperfect: amd64 stable
     1 file changed, 1 insertion(+), 1 deletion(-)

    Commit complete.
    RepoMan sez: "If everyone were like you, I'd be out of business!"

Finally, update the bug and cleanup the job:

`user `[`$`]`./writerperfect-success.sh`

`user `[`$`]`./writerperfect-cleanup.sh`

## [QA violations]

Most of these violations will be detected automatically using the testing tool, but are also described here for completeness.

-   Does not respect the `CC` variable (see [Removing native symlinks](https://wiki.gentoo.org/wiki/Project:Toolchain/use_native_symlinks#Removing_native_symlinks "Project:Toolchain/use native symlinks"), [[[bug #243502]](https://bugs.gentoo.org/show_bug.cgi?id=243502)[]]).
-   Does not respect `CFLAGS` variable (see [[[bug #59506]](https://bugs.gentoo.org/show_bug.cgi?id=59506)[]]).
-   Does not respect `LDFLAGS` variable (see [[[bug #331933]](https://bugs.gentoo.org/show_bug.cgi?id=331933)[]]).
-   Bundled symbols (see [Why not bundle dependencies](https://wiki.gentoo.org/wiki/Why_not_bundle_dependencies "Why not bundle dependencies"), [[[bug #251464]](https://bugs.gentoo.org/show_bug.cgi?id=251464)[]]).
-   Insecure symbols.
-   Installs documentation outside of the [/usr/share/doc/\$ directory.
-   ELF files found in the [/usr/share] directory.

## [Architecture-specific notes]

A number of items described in earlier sections, such as checking of reverse dependencies and miscellaneous QA checks, are architecture-neutral. At a stabilization level, the primary responsibility for carrying out these checks rests on the first architecture to stabilize an ebuild. Subsequent architectures may assume that these checks have been completed and skip them if they wish.

The devmanual also covers this [topic](https://devmanual.gentoo.org/keywording/index.html#stabilization-rules).

### [amd64]

-   Any developer may perform **[amd64]** stabilization - it is not necessary to be on the arch team.
-   `multilib-strict` must be added to the `FEATURES` variable in the [make.conf] file.

### [arm]

The [ARM project](https://wiki.gentoo.org/wiki/Project:ARM "Project:ARM") supports four **[arm]** variants - armv4, armv5, armv6, and armv7. Where possible for fragile packages, trying `CFLAGS="-march=$arch"` for each variant is encouraged.

### [x86]

-   Any developer may perform **[x86]** stabilization - it is not necessary to be on the arch team.
-   It is acceptable to stabilize in an **[x86]** [chroot](https://wiki.gentoo.org/wiki/Project:AMD64/32-bit_Chroot_Guide "Project:AMD64/32-bit Chroot Guide") on **[amd64]**.
-   It is generally acceptable to stabilize a package with only a build test on **[x86]** if it is already stable on **[amd64]**.

## [See also]

-   [Stable request](https://wiki.gentoo.org/wiki/Stable_request "Stable request") --- the procedure for moving an ebuild from testing to stable.
-   [Chroot_for_package_testing](https://wiki.gentoo.org/wiki/Chroot_for_package_testing "Chroot for package testing") --- reusable [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") environment can be prepared using a snapshot of a [btrfs file system](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"), a subdirectory, or a container, with [[[sys-apps/bubblewrap]](https://packages.gentoo.org/packages/sys-apps/bubblewrap)[]]

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **[Agostino Sarubbo (ago)](https://wiki.gentoo.org/wiki/User:Ago "User:Ago") , various arch testing teams**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*