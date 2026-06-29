This page contains [[changes](https://wiki.gentoo.org/index.php?title=Ebuild_repository&oldid=1397185&diff=1426100)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Ebuild_repository/de "Ebuild-Repositorien (12% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Ebuild_repository/es "Repositorio de ebuilds (57% translated)")
-   [français](https://wiki.gentoo.org/wiki/Ebuild_repository/fr "Dépôt ebuild (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Ebuild_repository/hu "Az ebuild szoftvercsomag-tároló (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Ebuild_repository/pl "Ebuild repository/pl (3% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Ebuild_repository/ru "Репозиторий ebuild-файлов (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Ebuild_repository/zh-cn "ebuild 仓库 (15% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Ebuild_repository/ja "ebuild リポジトリ (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Ebuild_repository/ko "Overlay (7% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository] --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Overlays "Project:Overlays")][Project](https://wiki.gentoo.org/wiki/Project:Overlays "Project:Overlays")

An **ebuild repository** is a file-structure that can provide packages for installation on a Gentoo system. Ebuild repositories contain [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild"), [eclasses](https://wiki.gentoo.org/wiki/Eclass "Eclass"), and other types of descriptive metadata files that supply [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") with packages, [news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base"), [profile targets](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles"), etc.

The **[Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")** is [Gentoo Linux\'s primary and official ebuild repository] - it contains all the information needed to build and install every package that makes up Gentoo. Additional ebuild repositories, such as [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"), can be configured with Portage, to provide even more packages.

Portage will install the latest available version of a package from any configured ebuild repository, by default. If the latest available version is provided by several ebuild repositories, it will be chosen according to a set order of priority - hence the colloquial name **overlay**.

Administrators of Gentoo systems can configure additional ebuild repositories with Portage by using the utilities and methods described below.

## Contents

-   [[1] [The Gentoo ebuild repository]](#The_Gentoo_ebuild_repository)
-   [[2] [Where do ebuild repositories come from?]](#Where_do_ebuild_repositories_come_from.3F)
-   [[3] [Repository management]](#Repository_management)
-   [[4] [Installing packages from other repositories]](#Installing_packages_from_other_repositories)
-   [[5] [Repository synchronization]](#Repository_synchronization)
-   [[6] [Best practices]](#Best_practices)
    -   [[6.1] [Cache generation]](#Cache_generation)
    -   [[6.2] [Masking enabled ebuild repositories]](#Masking_enabled_ebuild_repositories)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [[] The Gentoo ebuild repository]

The ***Gentoo ebuild repository*** is the main ebuild repository for a Gentoo Linux system, and is where all the packages come from by default. It is maintained on the [gitweb.gentoo.org server](https://gitweb.gentoo.org/repo/gentoo.git/tree), and gets [synchronized](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository") to local machines (in [/var/db/repos/gentoo](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo")), to be available to [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").

The Gentoo ebuild repository contains *[ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild")* files that tell Portage how to build and install each package. The ebuilds come with metadata, dependency information, and everything else needed to get a package in working order.

The [metadata](https://wiki.gentoo.org/wiki/Repository_format/package/metadata.xml "Repository format/package/metadata.xml") provides the package\'s name, version, where to get sources from, available [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), [license](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#Licenses "Handbook:AMD64/Working/Portage"), website etc. Dependency information in ebuilds allows Portage to pull in any other packages required to build and run a package that is to be installed - no more, no less. Dependencies are very granular in Gentoo, they will even vary depending on what USE flags are selected, for ultimate selectivity. Perhaps most importantly, *ebuilds* contain the information required to [configure](https://wiki.gentoo.org/wiki/Autotools "Autotools"), [build](https://wiki.gentoo.org/wiki/Build_automation "Build automation") (compile), [install](https://wiki.gentoo.org/wiki/Emerge "Emerge"), and [test](https://wiki.gentoo.org/wiki/Package_testing "Package testing") each package - usually from a project\'s own source code.

In addition to ebuilds, the Gentoo ebuild repository contains the official *[profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")*, which define the default state of [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), default values for most variables found in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")], the [set of system packages](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), etc.

The *Gentoo ebuild repository* is also the place where *[news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base")* are posted, which is why any new news items will be highlighted after a Gentoo ebuild repository [synchronization](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository").

The *Gentoo ebuild repository*, and its ebuilds, are maintained by the [Gentoo developers](https://devmanual.gentoo.org/general-concepts/package-maintainers/index.html) and other [members of the community](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers "Project:Proxy Maintainers").

** Note**\
The *Gentoo ebuild repository* will sometimes be called by shorter, or even colloquial, names, such as the ***Gentoo repository***, the ***Gentoo repo***, ***::gentoo***, ***gentoo.git***, or occasionally just the \"***repo***\". It is also historically and commonly known within the Gentoo community as the *Portage tree*, *rsync tree*, or sometimes just \"*the tree*\".

** Tip**\
**[GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU")** is an official ebuild repository maintained collaboratively by Gentoo users, with a little help from a few Gentoo developers. It is complementary to the *Gentoo ebuild repository*, and the maintainers strive to keep up a reasonable level of quality for the packages provided. There is also a list of public ebuild repositories [registered on repos.gentoo.org](https://repos.gentoo.org/).

## [][[] Where do ebuild repositories come from?]

Because an ebuild repository is simply a structure of files and directories, a new ebuild repository can be made available to Portage simply by copying those files and directories to a location known to Portage. The ebuild repositories and their files are usually under [/var/db/repos/], but the location of repositories configured for Portage is specified in [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf"). Ebuild repositories can be configured on any accessible filesystem however, even on an [nfs](https://wiki.gentoo.org/wiki/Nfs-utils "Nfs-utils") or [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") filesystem - allowing them to be stored on a network or Internet server.

As previously discussed, the Gentoo ebuild repository is hosted on [gitweb.gentoo.org](https://gitweb.gentoo.org/repo/gentoo.git/tree/). That server also hosts [other ebuild repositories](https://gitweb.gentoo.org/repo/).

In practice, any additional ebuild repositories usually aren\'t just copied to a directory by hand and configured for Portage (meaning added to [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")). Generally, new repositories are made available by third parties, and once configured for Portage, are **[synchronized](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_synchronization "Ebuild repository")** by Portage. Synchronization mirrors all the files from a remote location to a locally available filesystem, as configured.

Because ebuild repositories are just file-structures, many methods can be used to synchronize them, and Portage offers several possibilities. [Rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") is the default synchronization method, [git](https://wiki.gentoo.org/wiki/Git "Git") is also popular. The synchronization method is specified in [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf") when configuring a repository, along with the information needed to retrieve it.

## [[] Repository management]

Use the [[eselect repository]](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") tool to easily add, disable, or remove ebuild repositories configured with Portage. This tool also provides a handy way to list and add repositories available through being [registered on repos.gentoo.org](https://repos.gentoo.org/).

Ebuild repositories can always be configured manually, by editing [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")].

** Warning**\
While the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") is either written or [reviewed](https://wiki.gentoo.org/wiki/Portage_Security "Portage Security") by Gentoo developers, and the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository has some developer oversight, that is not always the case for other ebuild repositories. It is possible that some ebuild repositories might contain vulnerable, badly broken or, theoretically, even malicious software.

New ebuild repositories for use with Portage can also be [created by the user](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository").

The list of active ebuild repositories can be obtained through the output of one of the following commands:

`user `[`$`]`emerge --info`

`user `[`$`]`portageq repos_config /`

## [[] Installing packages from other repositories]

Packages from repositories other than the Gentoo ebuild repository can be installed with the [emerge] command, just as usual.

For example, once the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository is added, to install the *x11-misc/xbanish* package from that repository:

`root `[`#`]`emerge --ask x11-misc/xbanish`

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    Dependency resolution took 2.96 s.

    [ebuild   R   #] x11-misc/xbanish-1.7::guru  0 KiB

    Total: 1 package (1 reinstall), Size of downloads: 0 KiB

Note that the repository is not specified in the command. The \"::guru\" appended to the package atom in the output shows what repository the package will be installed from. This works because the *x11-misc/xbanish* package is present in the GURU repository, but *not* in the Gentoo repository.

If multiple versions of the same package are available from two or more different ebuild repositories, Portage will install the most recent version.

** Tip**\
Beware when performing [system updates](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Updating_packages "Upgrading Gentoo") that if a newly added ebuild repository is providing newer versions of currently installed packages, these packages will be replaced with the newer versions from the overlay. Consider if any updates are desired.\
\
See [masking enabled ebuild repositories](https://wiki.gentoo.org/wiki/Ebuild_repository#Masking_enabled_ebuild_repositories "Ebuild repository") to avoid an ebuild repository blanket-upgrading packages. Note that the GURU ebuild repository intentionally avoids providing versions that would replace packages from the Gentoo ebuild repository.

If the latest version of a package is available from more than one ebuild repository, the repository with the highest priority will be used. The priority can be set for an ebuild repository in [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf"). The Gentoo ebuild repository has a default priority set to `-1000`, and the default if a priority is not set for a repository is `0`. If several ebuild repositories have the same priority (such as two or more not having any priority set, so having priority `0`), the order is **undetermined** - a package to install will be selected arbitrarily.

It is possible to instruct [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") to install a package from a specific ebuild repository with the `::` [version specifier](https://wiki.gentoo.org/wiki/Version_specifier#By_ebuild_repository "Version specifier") (can be used for different emerge instructions, e.g. uninstalling a package through `--depclean`):

`root `[`#`]`emerge --ask category/atom::repository-name`

See the [repository management](https://wiki.gentoo.org/wiki/Ebuild_repository#Repository_management "Ebuild repository") section to see how to list repositories configured for portage with their respective priorities.

## [[] Repository synchronization]

Ebuild repositories should be **synchronized**, so that the local mirrors will reflect a recent state of the repositories. This is necessary to be able to [keep the system up to date](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo"), and [install](https://wiki.gentoo.org/wiki/Portage#emerge "Portage") current software.

** Note**\
Regularly synchronizing with the **Gentoo repository** and updating the system in this way is important, to ensure that all the latest security updates are installed, and that the local system does not get too out of sync with the **Gentoo repository**, as this can make upgrades complicated if things have moved too far on in the repository.

** Tip**\
Synchronize and [update](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") between daily or weekly to keep a Gentoo Linux installation running smoothly with the latest security updates. Waiting more than a few weeks to update may make things a little more complicated when the update is attempted. Please don\'t synchronize more than once daily, to avoid strain on the servers.

** Important**\
If local repositories are not very up to date, **synchronize the repositories and update the system, before installing packages**.

Repository synchronization is performed with the [emaint sync] command, and is configured through the files in [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")]:

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

To sync all repositories for which `auto-sync=true` is set, run [emaint sync] with the `--auto` switch (`-a` for short). This is usually the **command that should be run regularly**, before system updates and package installation (and is equivalent to using the old [emerge \--sync] command):

`root `[`#`]`emaint sync --auto`

To sync the *foo* repository (irrespective of the *foo* auto-sync setting):

`root `[`#`]`emaint sync --repo foo`

To sync all repositories with a valid sync-type and sync-url defined (ignoring auto-sync settings):

`root `[`#`]`emaint sync --allrepos`

** Warning**\
For any repositories that should ***not*** be synced when running [emaint sync \--auto], `auto-sync = no` **must** be set in the appropriate file in [/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf"), due to the default being `auto-sync = true`.

** Note**\
The [emerge \--sync] command is now only a compatibility command. Primary control of all sync operations has been moved from [emerge] to [emaint], and [emerge \--sync] now just calls the emaint sync module with the `--auto` option. This performs a sync on only those repositories with the auto-sync setting set to `yes` or `true`. If the auto-sync option is *not* set or is absent for the configured repositories, then [emerge \--sync] may sync no repositories at all.

** Tip**\
The [emerge-webrsync](https://wiki.gentoo.org/wiki/Portage#emerge-webrsync "Portage") tool can be used to download and install the daily Gentoo Repository rsync snapshot, to help with firewall restrictions, or to speed up the first synchronization, for example.

See [man emaint] for information on how to use the portage synchronization commands. See the [Portage project sync](https://wiki.gentoo.org/wiki/Project:Portage/Sync "Project:Portage/Sync") article about migrating to the new modular sync system from Portage version 2.2.16, it contains important information, notably for users of [eix-sync], [esync -l], and [emerge \--sync] .

## [[] Best practices]

### [[] Cache generation]

When large ebuild repositories are installed, Portage may take a long time to perform operations like dependency resolution. This is because ebuild repositories do not usually contain a metadata cache.

There are several available methods to generate such a cache. In order of speed:

1.  [Pkgcraft](https://wiki.gentoo.org/wiki/Pkgcraft "Pkgcraft")\'s [pk repo metadata] from [[[sys-apps/pkgcraft-tools]](https://packages.gentoo.org/packages/sys-apps/pkgcraft-tools)[]]
2.  [Pkgcore](https://wiki.gentoo.org/wiki/Pkgcore "Pkgcore")\'s [pmaint regen] from [[[sys-apps/pkgcore]](https://packages.gentoo.org/packages/sys-apps/pkgcore)[]]
3.  [Portage](https://wiki.gentoo.org/wiki/Portage "Portage")\'s [egencache] or [emerge \--regen] from [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]]

To do this using, for example, [emerge \--regen] after syncing the ebuild repositories:

`root `[`#`]`emaint sync --allrepos `

`root `[`#`]`( ulimit -n 4096 && emerge --regen )`

There is no need to (re)generate the cache if syncing ::gentoo via rsync as it is already there (most users of ::gentoo are rsync users). Ditto if using the \'metadata\' or \'sync\' repo for ::gentoo with git. Regeneration via any method is time-consuming. Using raw repositories with git however will require generation.

### [[] Masking enabled ebuild repositories]

When using *large* ebuild repositories or those with *unknown/low quality code*, it is best practice to hard mask the whole ebuild repository and only accept specific ebuilds on a case-by-case basis. For example, for an overlay named \"repository-foobar\":

[FILE] **`/etc/portage/package.mask`Mask all packages in an ebuild repository**

    */*::repository-foobar

Then add the specific package(s) from the repository-foobar overlay so that they will be available visible to Portage for installation:

[FILE] **`/etc/portage/package.unmask`Unmask a specific package in an ebuild repository**

    foo-category/bar::repository-foobar

After the above unmask, the package named \"foo-category/bar\" should be available and none of the other packages from the repository-foobar overlay will be available.

## [[] See also]

-   [Creating an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") --- basics of creating an ebuild repository and maintaining ebuilds in it.
-   [Creating a custom ebuild repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Creating_a_custom_ebuild_repository "Handbook:AMD64/Portage/CustomTree") - Section in the Gentoo Handbook
-   [Overlays guide (Overlay project)](https://wiki.gentoo.org/wiki/Project:Overlays/Overlays_guide "Project:Overlays/Overlays guide") - A user guide written by the Overlay project.
-   [Overlays project](https://wiki.gentoo.org/wiki/Project:Overlays "Project:Overlays") - The official Gentoo project for ebuild repositories\' support.

## [[] External resources]

-   [https://repos.gentoo.org](https://repos.gentoo.org) - Gentoo\'s official ebuild repository hosting location.
-   [https://github.com/gentoo/](https://github.com/gentoo/) - GitHub mirror of the Gentoo\'s ebuild repository.
-   [https://gpo.zugaina.org/Overlays](https://gpo.zugaina.org/Overlays) - A non-official very useful site for searching overlays.