Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Portage/es "Portage/es (85% translated)")
-   [français](https://wiki.gentoo.org/wiki/Portage/fr "Portage/fr (83% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Portage/hu "Portage/hu (94% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Portage/zh-cn "Portage/zh-cn (1% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Portage/ja "Portage/ja (99% translated)")

**[Portage - the heart of Gentoo]**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/portage)

[[]][Official documentation](https://dev.gentoo.org/~zmedico/portage/doc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Portage_(software) "wikipedia:Portage (software)")

[[]][GitWeb](https://gitweb.gentoo.org/proj/portage.git)

[[]][GitHub](https://github.com/gentoo/portage)

[[]][Bugs (upstream)](https://bugs.gentoo.org)

** See also**\
Portage is a very advanced package manager that will treat the user\'s wishes with the highest respect. Sometimes too much trust is put into the user, so you may be looking for [Portage Help](https://wiki.gentoo.org/wiki/Portage/Help "Portage/Help") rather than this article.

**Portage** is the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo. It functions as the heart of Gentoo-based operating systems, providing advanced dependency resolution, flexible building and installation of software from source or from [binary packages](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart"), and most other core distribution functionality.

Portage will provision software from the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), any [additional ebuild repositories](https://wiki.gentoo.org/wiki/Portage#Ebuild_repositories "Portage"), or binhost. Portage includes many [commands](https://wiki.gentoo.org/wiki/Portage#Usage "Portage") for repository and package management, the primary of which is the [[emerge]](https://wiki.gentoo.org/wiki/Portage#emerge "Portage") command.

Some common questions about portage and the [emerge] command are answered in the [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ") and the [Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ").

** Tip**\
For day to day usage, the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge"), [emaint](https://wiki.gentoo.org/wiki/Portage#emaint "Portage"), and [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") will be the most used Portage commands. Refer to relevant documentation.

** See also**\
See [man portage] for complete user documentation. See the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") article for information on installing and maintaining packages with Portage.

This article describes Portage from a user\'s perspective. Those looking to contribute to Portage development should visit the [Portage project page](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Updating Portage]](#Updating_Portage)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
    -   [[3.2] [Environment variables]](#Environment_variables)
    -   [[3.3] [Ebuild repositories]](#Ebuild_repositories)
    -   [[3.4] [Binary hosts]](#Binary_hosts)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [archive-conf]](#archive-conf)
    -   [[4.2] [dispatch-conf]](#dispatch-conf)
    -   [[4.3] [ebuild]](#ebuild)
    -   [[4.4] [egencache]](#egencache)
    -   [[4.5] [emaint]](#emaint)
    -   [[4.6] [emerge]](#emerge)
    -   [[4.7] [emerge-webrsync]](#emerge-webrsync)
    -   [[4.8] [emirrordist]](#emirrordist)
    -   [[4.9] [env-update]](#env-update)
    -   [[4.10] [fixpackages]](#fixpackages)
    -   [[4.11] [glsa-check]](#glsa-check)
    -   [[4.12] [gpkg-sign]](#gpkg-sign)
    -   [[4.13] [portageq]](#portageq)
    -   [[4.14] [quickpkg]](#quickpkg)
    -   [[4.15] [regenworld]](#regenworld)
-   [[5] [Tips]](#Tips)
    -   [[5.1] [Common portage issues and resolutions]](#Common_portage_issues_and_resolutions)
    -   [[5.2] [Main (Gentoo) ebuild repository sync time]](#Main_.28Gentoo.29_ebuild_repository_sync_time)
    -   [[5.3] [Listing package sets]](#Listing_package_sets)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [Corrupt or absent Portage]](#Corrupt_or_absent_Portage)
    -   [[6.2] [Default Gentoo ebuild repository location change]](#Default_Gentoo_ebuild_repository_location_change)
        -   [[6.2.1] [Old location]](#Old_location)
        -   [[6.2.2] [New location]](#New_location)
-   [[7] [See also]](#See_also)
    -   [[7.1] [Related to Portage]](#Related_to_Portage)
    -   [[7.2] [Portage in the Gentoo AMD64 Handbook]](#Portage_in_the_Gentoo_AMD64_Handbook)
    -   [[7.3] [Portage tools]](#Portage_tools)
    -   [[7.4] [Alternate package managers and GUIs]](#Alternate_package_managers_and_GUIs)
    -   [[7.5] [Ebuild or package related]](#Ebuild_or_package_related)
-   [[8] [External resources]](#External_resources)
    -   [[8.1] [Portage man pages]](#Portage_man_pages)
-   [[9] [References]](#References)

## [[] Installation]

All Gentoo installations come with Portage, so ***there is no need to install it!***.

In the rare eventuality of a corrupt or missing Portage, see the [Corrupt or absent Portage](https://wiki.gentoo.org/wiki/Portage#Corrupt_or_absent_Portage "Portage") section.

### [[] USE flags]

### [USE flags for] [sys-apps/portage](https://packages.gentoo.org/packages/sys-apps/portage) [[]] [The package management and distribution system for Gentoo]

  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+ipc`](https://packages.gentoo.org/useflags/+ipc)                               Use inter-process communication between portage and running ebuilds.
  [`+native-extensions`](https://packages.gentoo.org/useflags/+native-extensions)   Compiles native \"C\" extensions (speedups, instead of using python backup code). Currently includes libc-locales. This should only be temporarily disabled for some bootstrapping operations. Cross-compilation is not supported.
  [`+rsync-verify`](https://packages.gentoo.org/useflags/+rsync-verify)             Enable full-tree cryptographic verification of Gentoo repository git or rsync checkouts using app-portage/gemato.
  [`apidoc`](https://packages.gentoo.org/useflags/apidoc)                           Build html API documentation with sphinx-apidoc.
  [`build`](https://packages.gentoo.org/useflags/build)                             !!internal use only!! DO NOT SET THIS FLAG YOURSELF!, used for creating build images and the first half of bootstrapping \[make stage1\]
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gentoo-dev`](https://packages.gentoo.org/useflags/gentoo-dev)                   Enable features required for Gentoo ebuild development.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xattr`](https://packages.gentoo.org/useflags/xattr)                             Preserve extended attributes (filesystem-stored metadata) when installing files. Usually only required for hardened systems.
  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 21:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [[] Updating Portage]

In order for Gentoo to stay up to date, Portage must stay up to date. Generally the usual, regular [updating of Gentoo](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Updating_packages "Upgrading Gentoo"), will automatically update Portage without issue.

On occasion, updates to Portage can make it advisable to update Portage before the rest of the system. After [synchronizing Portage](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository"), a message requesting this may be displayed:

    * An update to portage is available. It is _highly_ recommended
    * that you update portage now, before any other packages are updated.

    * To update portage, run 'emerge --oneshot sys-apps/portage' now.

Emerge Portage as advised (adapt the command if the message differs from this example). **The `--oneshot` option is important**, to avoid adding [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]] to the [world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)"):

`root `[`#`]`emerge --ask --oneshot sys-apps/portage`

If there is an issue with updating Portage, [User:Sam/Portage_help/Upgrading_Portage](https://wiki.gentoo.org/wiki/User:Sam/Portage_help/Upgrading_Portage "User:Sam/Portage help/Upgrading Portage") may help.

## [[] Configuration]

### [[] Files]

The main Portage configuration is in [make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf"), though there are many files used to configure Portage, mainly in the [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") directory.

See [man make.conf] for comprehensive documentation, notably a list of variables that can be set in this file.

The [[/usr/share/portage/config/make.globals](https://gitweb.gentoo.org/proj/portage.git/tree/cnf/make.globals)] file contains many default configuration values sourced by Portage. These values can be overwritten by specifying the same variable names in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")].

### [[] Environment variables]

Portage can be configured to a vast extent through environment variables.

See [man make.conf] for information on available environment variables. Refer also to the [Handbook section for working with environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") in Gentoo.

To view all presently set environment variables, run:

`user `[`$`]`emerge --info --verbose`

** Tip**\
Environment variables can be set on a per-package basis via [/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env") entries.

### [[] Ebuild repositories]

In addition to the **[Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")**, from which Portage will pull packages by default, additional [ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") are available, for example:

-   [repos.gentoo.org](https://repos.gentoo.org/) - list of repositories contributed by the community, some by Gentoo developers
-   [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") - official ebuild repository maintained collaboratively by Gentoo users, with a little support from a few Gentoo developers
-   [gpo.zugaina.org](https://gpo.zugaina.org/) - third-party list of ebuild repositories

The ebuild repository article has a section on [configuring ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_management "Ebuild repository") to be used by Portage.

Search for available ebuilds on the command line with [emerge \--search] or [eix](https://wiki.gentoo.org/wiki/Eix "Eix").

** Warning**\
While the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") is either written or [reviewed](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") by Gentoo developers, and the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository has some developer oversight, that is not always the case for other ebuild repositories. It is possible that some ebuilds repositories might contain vulnerable, badly broken or, theoretically, even malicious software.

### [[] Binary hosts]

Binary hosts are configured in [/etc/portage/binrepos.conf] and allow fast installation of binary packages, as long as there is a package available for the requested [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for the package being installed or updated.

There is an [official Gentoo binary host](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") that contains many binary packages for the **[amd64]** and **[arm64]** architectures - see the guide at that link for further setup and usage instructions.

To configure alternative binary hosts, and for more information on using binary packages with Portage, see the [binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide").

## [[] Usage]

Portage includes many different tools and utilities to help with system administration and maintenance. The following sections list these in alphabetical order.

** Tip**\
The main commands users will need on a day to day basis are [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge"), [emaint](https://wiki.gentoo.org/wiki/Portage#emaint "Portage"), and [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf").

### [[] archive-conf]

The purpose of [archive-conf] is to save off a config file in the dispatch-conf archive directory. Most users should not *ever* need to run this command:

`root `[`#`]`archive-conf`

    Usage: archive-conf /CONFIG/FILE [/CONFIG/FILE...]

### [[] dispatch-conf]

The [dispatch-conf] utility is used to manage configuration file updates. See the [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") article.

### [[] ebuild]

** See also**\
This section covers the [ebuild] command. For information on *ebuild files*, see the [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") article.

** Note**\
As a user, **do not use the [ebuild] command to install packages**. The [ebuild] command is provided mainly for package development, use the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") command to install packages.

\

If in possession of an [ebuild file](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") to be installed, first place it in an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") that is available to Portage, then install with the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") command.

[ebuild] is Portage\'s command for running the various [ebuild functions](https://devmanual.gentoo.org/ebuild-writing/functions/).

For a brief summary of usage and command-line options:

`root `[`#`]`ebuild --help`

    usage: Usage: ebuild <ebuild file> <command> [command] ...

    See the ebuild(1) man page for more info

    options:
      -h, --help            show this help message and exit
      --force               When used together with the digest or manifest command, this option forces regeneration of digests for all distfiles associated
                            with the current ebuild. Any distfiles that do not already exist in $ will be automatically fetched.
      --color          enable or disable color output
      --debug               show debug output
      --version             show version and exit
      --ignore-default-opts
                            do not use the EBUILD_DEFAULT_OPTS environment variable
      --skip-manifest       skip all manifest checks

For more information on the [ebuild] command, view it\'s man page:

`user `[`$`]`man 1 ebuild`

### [[] egencache]

The [egencache] tool rebuilds the cache of metadata information for the ebuild repositories. See the [egencache](https://wiki.gentoo.org/wiki/Egencache "Egencache") article for additional information.

### [[] emaint]

Performs package management related system health checks and maintenance.

See [repository synchronization](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") about how to use [emaint] to synchronize repositories. See [man 1 emaint] for detailed information.

** Note**\
The [emerge \--sync] command is now implemented with [[emaint]](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository").

`user `[`$`]`emaint --help`

    usage: usage: emaint [options] COMMAND

    The emaint program provides an interface to system health checks
    and maintenance. See the emaint(1) man page for additional
    information about the following commands:

    Commands:
      all            Perform all supported commands
      binhost        Scan and generate metadata indexes for binary packages.
      cleanconfmem   Check and clean the config tracker list for uninstalled packages.
      cleanresume    Discard emerge --resume merge lists
      logs           Check and clean old logs in the PORTAGE_LOGDIR.
      merges         Scan for failed merges and fix them.
      movebin        Perform package move updates for binary packages
      moveinst       Perform package move updates for installed and binary packages.
      sync           Check repos.conf settings and sync repositories.
      world          Check and fix problems in the world file.

    optional arguments:
      -h, --help            show this help message and exit
      -c, --check           Check for problems (a default option for most modules)
      -f, --fix             Attempt to fix problems (a default option for most modules)
      --version             show program's version number and exit
      -C, --clean           Cleans out logs more than 7 days old (cleanlogs only) module-options: -t, -p
      -t NUM, --time NUM    (cleanlogs only): -t, --time Delete logs older than NUM of days
      -p, --pretend         (cleanlogs only): -p, --pretend Output logs that would be deleted
      -P, --purge           Removes the list of previously failed merges. WARNING: Only use this option if you plan on manually fixing them or do not want them re-installed.
      -y, --yes             (merges submodule only): Do not prompt for emerge invocations
      -r REPO, --repo REPO  (sync module only): -r, --repo Sync the specified repo
      -A, --allrepos        (sync module only): -A, --allrepos Sync all repos that have a sync-url defined
      -a, --auto            (sync module only): -a, --auto Sync auto-sync enabled repos only
      --sync-submodule
                            (sync module only): Restrict sync to the specified submodule(s)

### [[] emerge]

[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") is the command-line interface to Portage and is how most users will interact with Portage.

See the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") article for more information on the wiki.

### [[] emerge-webrsync]

Install a Gentoo ebuild repository snapshot from the web. See [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Installing_a_Gentoo_ebuild_repository_snapshot_from_the_web "Handbook:AMD64/Installation/Base").

`root #``emerge-webrsync -h`

    Usage: /usr/bin/emerge-webrsync [options]

    Options:
      --revert=yyyymmdd   Revert to snapshot
      -k, --keep          Keep snapshots in DISTDIR (don't delete)
      -q, --quiet         Only output errors
      -v, --verbose       Enable verbose output
      -x, --debug         Enable debug output
      -h, --help          This help screen (duh!)

[emerge-webrsync] is called internally by [[eix-sync](https://wiki.gentoo.org/wiki/Ebuild_repository#eix "Ebuild repository")] when `sync-type` in [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf") is set to [`webrsync`](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features#Validated_Gentoo_repository_snapshots "Handbook:AMD64/Working/Features").

### [[] emirrordist]

Tool for mirroring of package distfiles.

`root #``emirrordist -h`

    usage: emirrordist [options] <action>

    emirrordist - a fetch tool for mirroring of package distfiles

    optional arguments:
      -h, --help            show this help message and exit

    Actions:
      --version             display portage version and exit
      --mirror              mirror distfiles for the selected repository

    Common options:
      --dry-run             perform a trial run with no changes made (usually
                            combined with --verbose)
      --verbose, -v         display extra information on stderr (multiple
                            occurences increase verbosity)
      --ignore-default-opts
                            do not use the EMIRRORDIST_DEFAULT_OPTS environment
                            variable
      --distfiles DIR       distfiles directory to use (required)
      --jobs JOBS, -j JOBS  number of concurrent jobs to run
      --load-average LOAD, -l LOAD
                            load average limit for spawning of new concurrent jobs
      --tries TRIES         maximum number of tries per file, 0 means unlimited
                            (default is 10)
      --repo REPO           name of repo to operate on
      --config-root DIR     location of portage config files
      --repositories-configuration REPOSITORIES_CONFIGURATION
                            override configuration of repositories (in format of
                            repos.conf)
      --strict-manifests <y|n>
                            manually override "strict" FEATURES setting
      --failure-log FILE    log file for fetch failures, with tab-delimited
                            output, for reporting purposes
      --success-log FILE    log file for fetch successes, with tab-delimited
                            output, for reporting purposes
      --scheduled-deletion-log FILE
                            log file for scheduled deletions, with tab-delimited
                            output, for reporting purposes
      --delete              enable deletion of unused distfiles
      --deletion-db FILE    database file used to track lifetime of files
                            scheduled for delayed deletion
      --deletion-delay SECONDS
                            delay time for deletion, measured in seconds
      --temp-dir DIR        temporary directory for downloads
      --mirror-overrides FILE
                            file holding a list of mirror overrides
      --mirror-skip MIRROR_SKIP
                            comma delimited list of mirror targets to skip when
                            fetching
      --restrict-mirror-exemptions RESTRICT_MIRROR_EXEMPTIONS
                            comma delimited list of mirror targets for which to
                            ignore RESTRICT="mirror"
      --verify-existing-digest
                            use digest as a verification of whether existing
                            distfiles are valid
      --distfiles-local DIR
                            distfiles-local directory to use
      --distfiles-db FILE   database file used to track which ebuilds a distfile
                            belongs to
      --recycle-dir DIR     directory for extended retention of files that are
                            removed from distdir with the --delete option
      --recycle-db FILE     database file used to track lifetime of files in
                            recycle dir
      --recycle-deletion-delay SECONDS
                            delay time for deletion of unused files from recycle
                            dir, measured in seconds (defaults to the equivalent
                            of 60 days)
      --fetch-log-dir DIR   directory for individual fetch logs
      --whitelist-from FILE
                            specifies a file containing a list of files to
                            whitelist, one per line, # prefixed lines ignored

See also [man emirrordist].

### [[] env-update]

Updates environment settings automatically.

`root #``env-update -h`

    Usage: env-update [--no-ldconfig]

    See the env-update(1) man page for more info

See also [man env-update]. See the [login](https://wiki.gentoo.org/wiki/Login "Login") article for some information on how the environment is set up in Gentoo.

### [[] fixpackages]

Perform package move updates for all packages.

`root #``fixpackages -h`

    usage: fixpackages [-h]

    The fixpackages program performs package move updates on configuration files,
    installed packages, and binary packages.

    optional arguments:
      -h, --help  show this help message and exit

See also [man fixpackages].

### [[] glsa-check]

[Gentoo Linux Security Announcements](https://wiki.gentoo.org/wiki/GLSA "GLSA"), or [GLSAs](https://www.gentoo.org/support/security/), are notifications sent out to the community to inform of security vulnerabilities related broadly to Gentoo Linux or specifically to packages contained in the ::gentoo ebuild repository.

[glsa-check] is a tool to keep track of the various [GLSAs](https://security.gentoo.org/glsa/). It can be used to view GLSAs, but more importantly to test if the system is vulnerable to known GLSAs.

See [man glsa-check] and [glsa-check \--help] for more information:

`user `[`$`]`glsa-check --help`

    usage: glsa-check <option> [glsa-id | all | new | affected]

    optional arguments:
      -h, --help        show this help message and exit
      -V, --version     Show information about glsa-check
      -q, --quiet       Be less verbose and do not send empty mail
      -v, --verbose     Print more messages
      -n, --nocolor     Removes color from output
      -e, --emergelike  Upgrade to latest version (not least-change)
      -c, --cve         Show CVE IDs in listing mode
      -r, --reverse     List GLSAs in reverse order

    Modes:
      -l, --list        List a summary for the given GLSA(s) or set and whether they affect the system
      -d, --dump        Show all information about the GLSA(s) or set
      --print           Alias for --dump
      -t, --test        Test if this system is affected by the GLSA(s) or set and output the GLSA ID(s)
      -p, --pretend     Show the necessary steps to remediate the system
      -f, --fix         (experimental) Attempt to remediate the system based on the instructions given in the GLSA(s) or set. This will only upgrade (when an upgrade path exists) or remove packages
      -i, --inject      Inject the given GLSA(s) into the glsa_injected file
      -m, --mail        Send a mail with the given GLSAs to the administrator

    glsa-list can contain an arbitrary number of GLSA ids, filenames containing GLSAs or the special identifiers 'all' and 'affected'

### [[] gpkg-sign]

[ **Todo:**]

-   This section needs an explanation on the use of this command.

\

`user `[`$`]`gpkg-sign --help`

    usage: gpkg-sign [options] <gpkg package file>

    options:
      -h, --help            show this help message and exit
      --keep-current-signature
                            Keep existing signature when updating signature (default: false)
      --allow-unsigned      Allow signing from unsigned packages when binpkg-request-signature is enabled (default: false)
      --skip-signed         Skip signing if a package is already signed (default: false)

### [[] portageq]

For details see [portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq").

### [[] quickpkg]

** Warning**\
This command **uses the current state of files present on the system** (for example, this might include passwords or other secrets stored under [/etc]), which is often undesirable when creating binary packages. See the [quickpkg section of the Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide#Using_quickpkg "Binary package guide") for more information.

Creates binary packages **using the current state of files present on the system**. See the [quickpkg section of the Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide#Using_quickpkg "Binary package guide") for more information.

`user `[`$`]`quickpkg --help`

    usage: quickpkg [options] <list of package atoms or package sets>

    optional arguments:
      -h, --help            show this help message and exit
      --umask UMASK         umask used during package creation (default is 0077)
      --ignore-default-opts
                            do not use the QUICKPKG_DEFAULT_OPTS environment variable
      --include-config <y|n>
                            include all files protected by CONFIG_PROTECT (as a security precaution, default is 'n')
      --include-unmodified-config <y|n>
                            include files protected by CONFIG_PROTECT that have not been modified since installation (as a
                            security precaution, default is 'n')

See also [man quickpkg].

### [[] regenworld]

See the [regenworld](https://wiki.gentoo.org/wiki/Regenworld "Regenworld") article.

## [[] Tips]

### [[] Common portage issues and resolutions]

Gentoo has many more configuration options than most distributions allow. This leads to terminology which can be confusing at first, such as **blockers**, **circular dependencies**, **REQUIRED_USE**, etc.

[Portage/Help](https://wiki.gentoo.org/wiki/Portage/Help "Portage/Help") will help a user understand how they come about and how to resolve them.

### [][[] Main (Gentoo) ebuild repository sync time]

To see when the Gentoo ebuild repository was last updated (synced), run the following command:

`user `[`$`]`cat /var/db/repos/gentoo/metadata/timestamp.chk`

### [[] Listing package sets]

Need to determine what packages are inside each set? See [Package sets](https://wiki.gentoo.org/wiki/Package_sets#Listing "Package sets").

## [[] Troubleshooting]

### [[] Corrupt or absent Portage]

Although it should be very rare, as with all data, there remains a possibility that Portage could become corrupt or even uninstalled, which would be *very* bad for the functioning of the whole system. If ever this were to occur, there *are* ways Portage can be recovered, however, because Portage is so central, re-installation is a rather involved operation, requiring manual intervention to, in effect, install a package manager without having a functioning package manager.

See [Fix my Gentoo](https://wiki.gentoo.org/wiki/Fix_my_Gentoo "Fix my Gentoo") for details on emergency installation via binary packages. See also [Fixing broken Portage](https://wiki.gentoo.org/wiki/Project:Portage/Fixing_broken_portage "Project:Portage/Fixing broken portage").

### [[] Default Gentoo ebuild repository location change]

As of portage v2.3.66^[\[1\]](#cite_note-1)^, which was released on 2019-04-29^[\[2\]](#cite_note-2)^, the default locations changed for the `portdir`, `distdir`, `repo_name`, `repo_basedir` directories.

For more information see bug [[[bug #662982]](https://bugs.gentoo.org/show_bug.cgi?id=662982)[]].

#### [[] Old location]

[CODE] **Location before 2019-04-29**

    repo_basedir="/usr"
    repo_name="portage"
    distdir="/usr/portage/distfiles"
    portdir="/usr/portage"
    target_distdir="/usr/portage/distfiles"
    target_pkgdir="/usr/portage/packages"

#### [[] New location]

[CODE] **Location as of 2019-04-29 and later**

    repo_basedir="/var/db/repos"
    repo_name="gentoo"
    distdir="/var/cache/distfiles"
    portdir="/var/db/repos/gentoo"
    target_distdir="/var/cache/distfiles"
    target_pkgdir="/var/cache/binpkgs"

## [[] See also]

-   [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") --- the primary configuration directory for [Portage], Gentoo\'s package manager.
-   [/etc/portage/bashrc](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") --- a global [bashrc] file referenced by Portage.
-   [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- the main configuration file used to customize the [Portage] environment on a global level., the location [Portage] keeps binary packages.
-   [/etc/portage/color.map](https://wiki.gentoo.org/wiki//etc/portage/color.map "/etc/portage/color.map") --- a file containing variables that define color classes used by Portage.
-   [prefix](https://wiki.gentoo.org/wiki/Prefix "Prefix") --- enables the power of Gentoo and [Portage] on other distributions and/or operating systems (Microsoft Windows via Cygwin, Android via Termux, etc.).

### [[] Related to Portage]

-   [Upgrading Gentoo](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- explains how to **upgrade (update)** Gentoo, as well as how to proceed for a well maintained system.
-   [Catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") --- a tool to build [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file") and [live-images](https://wiki.gentoo.org/wiki/Live_image "Live image") for Gentoo
-   [Creating an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") --- basics of creating an ebuild repository and maintaining ebuilds in it.
-   [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") --- an introduction to optimizing compiled code using safe, sane [`CFLAGS` and `CXXFLAGS`](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS").
-   [Portage tips](https://wiki.gentoo.org/wiki/Portage_tips "Portage tips") --- the main command-line interface to [Portage]
-   [Repository format](https://wiki.gentoo.org/wiki/Repository_format "Repository format") --- A quick reference to Gentoo ebuild repository (overlay) format.
-   [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification") --- a standardization effort to ensure that the [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") file format, the ebuild repository format (of which the Gentoo ebuild repository is the main incarnation), as well as behavior of the package managers interacting with these ebuilds is properly agreed upon and documented.
-   [Ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- a file-structure that can provide packages for installation on a Gentoo system.
-   [Category:Portage](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")
-   [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- a suite of tools to ease the administration of a Gentoo system, and [Portage] in particular.
-   [Portage Multi Stage Dockerfile](https://wiki.gentoo.org/wiki/Portage_Multi_Stage_Dockerfile "Portage Multi Stage Dockerfile") --- The [emerge \--quickpkg-direct] and related [emerge \--quickpkg-direct-root] options are useful inside Dockerfiles
-   [Portage Security](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") --- aims to answer the question *\"How can I dispel doubts regarding the security of the Gentoo ebuild repository on a system?\"*
-   [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") --- It is unlikely that tmpfs will provide any performance gain for modern systems

### [[] Portage in the Gentoo AMD64 Handbook]

-   [A Portage introduction](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage "Handbook:AMD64/Working/Portage")
-   [USE flags](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE "Handbook:AMD64/Working/USE")
-   [Portage features](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features "Handbook:AMD64/Working/Features")
-   [Files and directories](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Files "Handbook:AMD64/Portage/Files")
-   [Configuring through variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Variables "Handbook:AMD64/Portage/Variables")
-   [Mixing software branches](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Branches "Handbook:AMD64/Portage/Branches")
-   [Additional Portage tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Tools "Handbook:AMD64/Portage/Tools")
-   [Custom Portage tree](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree "Handbook:AMD64/Portage/CustomTree")
-   [Advanced Portage features](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced "Handbook:AMD64/Portage/Advanced")

### [[] Portage tools]

-   [Useful Portage tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage], available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").
-   [Cfg-update](https://wiki.gentoo.org/wiki/Cfg-update "Cfg-update") --- a utility used on Gentoo to manage configuration file updates.

### [[] Alternate package managers and GUIs]

-   [Pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore") --- an alternative package manager for Gentoo that aims for high performance, extensibility, and a clean design.
-   [[[app-portage/kuroo]](https://packages.gentoo.org/packages/app-portage/kuroo)[]] - Graphical Portage frontend based on KF5/Qt5.
-   [App Swipe](https://github.com/k9spud/appswipe) - Qt GUI for browsing local Portage repositories.

### [[] Ebuild or package related]

-   [Package sets](https://wiki.gentoo.org/wiki/Package_sets "Package sets") --- describes package sets in high detail and includes a list of all typically available sets on a Gentoo system.

## [[] External resources]

-   [Official Portage documentation](https://dev.gentoo.org/~zmedico/portage/doc) - Built by Portage developer [Zac Medico (zmedico)](https://wiki.gentoo.org/wiki/User:Zmedico "User:Zmedico") .
-   [packages.gentoo.org](https://packages.gentoo.org/) - online searchable database of packages from the Gentoo package repository.

### [[] Portage man pages]

The man pages contain complete technical documentation for Portage. Type [man \<subject\>] in a shell on a Gentoo system to read the local man page. Note that man pages have a *see also* section for further information.

-   [emerge - command-line interface to the Portage system](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html) - emerge man page.
-   [Portage configuration files](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html) - Portage man page.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitweb.gentoo.org/proj/catalyst.git/commit/?id=91eb3317ee581f7d1eeacc68ebe88de5a1cdfd1a](https://gitweb.gentoo.org/proj/catalyst.git/commit/?id=91eb3317ee581f7d1eeacc68ebe88de5a1cdfd1a)]]
2.  [[[↑](#cite_ref-2)] [[https://gitweb.gentoo.org/proj/portage.git/tag/?h=portage-2.3.66](https://gitweb.gentoo.org/proj/portage.git/tag/?h=portage-2.3.66)]]