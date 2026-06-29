Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/de "Gentoo Spickzettel (31% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/es "Chuleta de Gentoo (21% translated)")
-   [français](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/fr "Aide-mémoire (des commandes) de Gentoo (93% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/it "Gentoo Cheat Sheet (88% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/hu "Gentoo Cheat Sheet (100% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/cs "Gentoo Cheat Sheet/cs (2% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/ru "Gentoo Cheat Sheet/ru (42% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/zh-cn "Gentoo Cheat Sheet/zh-cn (25% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet/ja "Gentoo チートシート (100% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet] --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

This is a reference card of useful commands and tips for administrating Gentoo systems. Newcomers and greybeards alike are encouraged to add their helpful tips below.

** See also**\
See also the [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ") and the [Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ").

## Contents

-   [[1] [Package management]](#Package_management)
    -   [[1.1] [Sync methods]](#Sync_methods)
        -   [[1.1.1] [Portage]](#Portage)
        -   [[1.1.2] [eix]](#eix)
    -   [[1.2] [Package listings]](#Package_listings)
        -   [[1.2.1] [qlist]](#qlist)
        -   [[1.2.2] [eix]](#eix_2)
        -   [[1.2.3] [Portage]](#Portage_2)
    -   [[1.3] [Package installation]](#Package_installation)
        -   [[1.3.1] [Install a specific version]](#Install_a_specific_version)
        -   [[1.3.2] [Install only some packages in a group]](#Install_only_some_packages_in_a_group)
        -   [[1.3.3] [Add an already installed package to the world]](#Add_an_already_installed_package_to_the_world)
        -   [[1.3.4] [Install without adding to the world file]](#Install_without_adding_to_the_world_file)
    -   [[1.4] [Package removal]](#Package_removal)
        -   [[1.4.1] [\--deselect]](#--deselect)
        -   [[1.4.2] [\--depclean]](#--depclean)
    -   [[1.5] [Package upgrades]](#Package_upgrades)
    -   [[1.6] [Package troubleshooting]](#Package_troubleshooting)
        -   [[1.6.1] [Rebuilds]](#Rebuilds)
    -   [[1.7] [Portage enhancements]](#Portage_enhancements)
    -   [[1.8] [After installations or updates]](#After_installations_or_updates)
-   [[2] [USE flags]](#USE_flags)
    -   [[2.1] [Important Portage files]](#Important_Portage_files)
-   [[3] [Log management]](#Log_management)
    -   [[3.1] [genlop]](#genlop)
-   [[4] [Overlays]](#Overlays)
    -   [[4.1] [eselect repository]](#eselect_repository)
-   [[5] [Services]](#Services)
    -   [[5.1] [OpenRC]](#OpenRC)
    -   [[5.2] [systemd]](#systemd)
-   [[6] [Tips]](#Tips)
    -   [[6.1] [Generate metadata caches]](#Generate_metadata_caches)
    -   [[6.2] [Search packages in Portage by regular expressions]](#Search_packages_in_Portage_by_regular_expressions)
    -   [[6.3] [qcheck]](#qcheck)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Package management]

### [Sync methods]

** Important**\
It is important to read and follow any and all [news items](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base") that may be listed after performing a repository sync. See detailed instructions about [upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Updating_packages "Upgrading Gentoo").

#### [Portage]

Sync all repositories that are set to auto-sync including the Gentoo ebuild repository:

`root `[`#`]`emaint --auto sync`

Or, for short:

`root `[`#`]`emaint -a sync`

Sync the Gentoo ebuild repository using the mirrors by obtaining a snapshot that is (at most) a day old:

`root `[`#`]`emerge-webrsync`

[emerge \--sync] now runs the emaint sync module with the `--auto` option. See [Portage\'s sync operation](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Operation "Project:Portage/Sync").

#### [eix]

Sync [configured package repositories](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") and the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") using [eix](https://wiki.gentoo.org/wiki/Eix "Eix"):

`root `[`#`]`eix-sync`

This not only syncs the repositories, it also updates the cache used by eix to perform queries. It may be preferable to [configure portage to update the cache](https://wiki.gentoo.org/wiki/Eix#Updating_the_cache_with_each_sync "Eix") automatically.

### [Package listings]

#### [qlist]

List installed packages with version number and name of overlay used:

`root `[`#`]`qlist -IRv`

[qlist](https://wiki.gentoo.org/wiki/Q_applets "Q applets") is provided by [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]].

#### [eix]

To view the list of packages in the world set, along with their available versions, it is possible to use [eix](https://wiki.gentoo.org/wiki/Eix "Eix"):

`root `[`#`]`eix --world | less`

To keep color in the output, use the `--color` switch:

`root `[`#`]`eix --color -c --world | less -R`

#### [Portage]

The [Gentoo Linux Security Advisories check tool](https://wiki.gentoo.org/wiki/Security_Handbook/Staying_up-to-date "Security Handbook/Staying up-to-date") can test systems against some security vulnerabilities:

`user `[`$`]`glsa-check --test all`

Referring to [Package sets](https://wiki.gentoo.org/wiki/Package_sets#Portage "Package sets"), the selected set packages are listed by issuing:

`user `[`$`]`emerge --pretend --quiet --emptytree --nodeps @selected`

List all (\*), or specific named, packages using multiple slots:

`user `[`$`]`equery list --duplicates '*'`

List the available synchronized versions and keywords of a package.

`user `[`$`]`equery y firefox`

### [Package installation]

In the following examples the [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] package will be used, but users should replace it with the package they want to install.

List what packages would be installed, without installing them:

`user `[`$`]`emerge --pretend --verbose www-client/firefox`

Or, for short:

`user `[`$`]`emerge -pv www-client/firefox`

List what packages would be installed, ask for confirmation before installing them:

`root `[`#`]`emerge --ask --verbose www-client/firefox`

Or, for short:

`root `[`#`]`emerge -av www-client/firefox`

#### [Install a specific version]

Install a specific version of a package (use \"\\=\" (*backslash* and *equal sign*) for shells that attach special meaning to the \"=\" character). For example:

`root `[`#`]`emerge --ask =www-client/firefox-96.0.1`

** Warning**\
This will work temporarily, until the system is updated. During an update Portage will try to install the latest stable version of the package no matter which version is currently installed; whether the package was originally emerged via a preceding = operator or not.

To prevent Portage from automatically updating a package, add a line into a the [/etc/portage/package.mask/package.mask] file (create the file if it does not exist). Specify using the greater than operator (`>`) prefix if it is an older package than latest stable or lesser than operator (`<`) as a prefix if it is a newer one:

[FILE] **`/etc/portage/package.mask`**

    <www-client/firefox-96.0.1

See [/etc/portage/package.mask](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask") for more details on package masking.

#### [Install only some packages in a group]

To exclude packages and their dependencies when updating:

`root `[`#`]`emerge --update @world --exclude="firefox libreoffice"`

#### [Add an already installed package to the world]

Update the world file without reinstalling a package:

`root `[`#`]`emerge --noreplace firefox`

#### [Install without adding to the world file]

Install a package without adding it to the world file:

`root `[`#`]`emerge --ask --oneshot www-client/firefox`

Or, for short:

`root `[`#`]`emerge -a1 www-client/firefox`

### [Package removal]

** See also**\
See the emerge documentation on [removing packages](https://wiki.gentoo.org/wiki/Emerge#Remove_.28uninstall.29_packages "Emerge") for full information.

#### [\--deselect]

Use [emerge \--deselect] (or `-W` option for short) to remove the specified package from the [\@world set](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)"), indicating that the package is no longer wanted:

`root `[`#`]`emerge --deselect www-client/firefox`

Now run [emerge \--depclean] (or `-c` option for short). The `--pretend` (`-p`) option will have [emerge] display what actions would be taken, this must be reviewed to make sure no required packages would be removed:

`user `[`$`]`emerge --pretend --depclean`

If [emerge \--depclean] has not been run in a while, it may try to remove many packages - caution is advised. Once it has been assured that [emerge \--depclean] will only remove unneeded packages, run:

`root `[`#`]`emerge --ask --depclean`

The `--ask` option is not really needed after a check via `--pretend`, but is included in the previous example to help avoid \"copy paste\" mishaps.

** Tip**\
Do not confuse the lower case `-c` switch, which is short for `--depclean` (and is safe), with the upper case `-C` switch which risks damaging the system and should only be used when absolutely required (see warning in following section).

#### [\--depclean]

To directly remove a package that no other packages depend on:

`root `[`#`]`emerge --ask --verbose --depclean www-client/firefox`

    Calculating dependencies... done!
    >>> Calculating removal order...

    >>> These are the packages that would be unmerged:

     www-client/firefox
        selected: 68.5.0
       protected: none
         omitted: none

    All selected packages: =www-client/firefox-68.5.0

    >>> 'Selected' packages are slated for removal.
    >>> 'Protected' and 'omitted' packages will not be removed.

    Would you like to unmerge these packages? [Yes/No]

As a safety measure, depclean will not remove any packages unless **all** required dependencies have been resolved. As a consequence of this, it is sometimes necessary to first run:

`root `[`#`]`emerge --ask --verbose --update --newuse --deep @world`

Use `--changed-use` (`-U`) in place of `--newuse` (`-N`) to avoid rebuilds when the only changes are USE flags added to or dropped from the repository. Use the `--quiet` (`-q`) flag for more succinct execution:

`root `[`#`]`emerge --ask --quiet --update --changed-use --deep @world`

** Warning**\
There is an `--unmerge` option (`-C`), but this is not recommended and can break the system if not used with caution. This should only ever be used ***if necessary***, and once properly informed of what it does. This *will* **break the system**, or other software, if used on some packages. The correct way to remove packages in Gentoo is virtually always with the `--depclean` option, as described above. This may sometimes be useful to temporarily remove a hard block though.

### [Package upgrades]

Upgrade all packages in the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"), their dependencies (`--deep`), and packages that have USE flag changes (avoiding unnecessary rebuilds when USE changes have no impact):

`root `[`#`]`emerge --ask --verbose --update --deep --changed-use @world`

The `--newuse` may be used in place of`--changed-use` to make sure that all package use flags reflect the current state of those in the Gentoo repository, though this will entail more rebuilds. The `--with-bdeps=y` can be used to update build time dependencies also.

** See also**\
See [upgrading Gentoo](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") for more in depth information.

### [Package troubleshooting]

Check for and rebuild missing libraries (not normally needed):

`root `[`#`]`revdep-rebuild -v`

[equery] is part of [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]]. Install it by issuing this command:

`root `[`#`]`emerge -a gentoolkit`

Tell which installed package provides a command using [equery](https://wiki.gentoo.org/wiki/Equery "Equery"):

`user `[`$`]`` equery b `which vim` ``

** Tip**\
[qfile](https://wiki.gentoo.org/wiki/Qfile "Qfile") can provide a faster alternative to equery, if needed.

Tell which (not) installed package provides a command using [e-file](https://wiki.gentoo.org/wiki/Pfl "Pfl"):

`user `[`$`]`e-file vim`

Install e-file with:

`root `[`#`]`emerge -a app-portage/pfl`

Tell which packages depend on a specific package (cat/pkg in the example) using [equery](https://wiki.gentoo.org/wiki/Equery "Equery"):

`user `[`$`]`equery d www-client/firefox`

Get information about a package using [eix](https://wiki.gentoo.org/wiki/Eix "Eix"):

`root `[`#`]`eix www-client/firefox`

** Warning**\
Do not unemerge [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]]. It is needed by nearly every other package. If it gets inadvertently removed, a rescue stick/disk may be required.

#### [Rebuilds]

Sometimes it\'s necessary to rebuild some packages for them to work properly, here are some examples of rebuild commands.

After installing a new kernel:

`root `[`#`]`emerge @module-rebuild`

For [using new libraries](https://wiki.gentoo.org/wiki/Preserved-rebuild "Preserved-rebuild"):

`root `[`#`]`emerge @preserved-rebuild`

### [Portage enhancements]

Manage configuration changes after an emerge completes:

`root `[`#`]`dispatch-conf`

### [After installations or updates]

After updating [perl](https://wiki.gentoo.org/wiki/Perl "Perl")-core packages:

`root `[`#`]`perl-cleaner --all`

Or if previous didn\'t help:

`root `[`#`]`perl-cleaner --reallyall -- -av`

For [haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell") packages:

`root `[`#`]`haskell-updater`

## [USE flags]

Obtain descriptions and usage of the USE flag `X` using [euse](https://wiki.gentoo.org/wiki/Gentoolkit#euse "Gentoolkit"):

`user `[`$`]`euse -i X`

Gather more information on [euse] by reading its manual page:

`user `[`$`]`man euse`

Show what packages have the `mysql` USE flag:

`user `[`$`]`equery hasuse mysql`

Show what packages are currently built with the `mysql` USE flag:

`user `[`$`]`eix --installed-with-use mysql`

Show what USE flags are available for a specific package:

`user `[`$`]`equery uses `

Quickly add a required USE flag for a package install:

`root `[`#`]`echo 'dev-util/cmake -qt5' >> /etc/portage/package.use`

### [Important Portage files]

-   [[/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage")] - primary configuration directory for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage").
-   [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] - Global settings (USE flags, compiler options).
-   [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] - USE flags of individual packages. Can also be a folder containing multiple files.
-   [[/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords")] - Keyword individual packages; e.g. **[\~amd64]**, **[\~x86]**, or **[∼arm]**.
-   [[/etc/portage/package.license](https://wiki.gentoo.org/wiki//etc/portage/package.license "/etc/portage/package.license")] - Accepted licenses
-   [[/etc/portage/profile/use.mask](https://wiki.gentoo.org/wiki//etc/portage/profile/use.mask "/etc/portage/profile/use.mask")] - for masking/unmasking locked use flags.
-   [[/var/lib/portage/world](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)")] - List of explicitly installed package atoms.
-   [/var/db/pkg] - Contains information for every installed package a set of files about the installation.

## [Log management]

### [genlop]

[genlop](https://wiki.gentoo.org/wiki/Genlop "Genlop") is a Portage log processor, also estimating build times when emerging packages.

Install [[[app-portage/genlop]](https://packages.gentoo.org/packages/app-portage/genlop)[]] by issuing:

`root `[`#`]`emerge -a app-portage/genlop`

Gather more information on [genlop] by reading its manual page:

`root `[`#`]`man genlop`

View the last 10 emerges (installs):

`root `[`#`]`genlop -l | tail -n 10`

View how long emerging LibreOffice took:

`root `[`#`]`genlop -t libreoffice`

Estimate how long [emerge -uND \--with-bdeps=y \@world] will take:

`root `[`#`]`emerge -pU @world | genlop --pretend`

Watch the latest merging ebuild during system upgrades:

`root `[`#`]`watch genlop -unc`

## [Overlays]

### [eselect repository]

[[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] can be installed by issuing:

`root `[`#`]`emerge -a app-eselect/eselect-repository`

List all existing overlays:

`user `[`$`]`eselect repository list`

List all installed overlays:

`user `[`$`]`eselect repository list -i`

** See also**\
See [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") for more information.

## [Services]

Obtain root shell (if the current user is listed in the sudoers list):

`user `[`$`]`sudo -i`

### [OpenRC]

Start the ssh daemon in the default runlevel at boot:

`root `[`#`]`rc-update add sshd default`

Start the sshd service now:

`root `[`#`]`rc-service sshd start`

Check if the sshd service is running:

`root `[`#`]`rc-service sshd status`

Restart the sshd service:

`root `[`#`]`rc-service sshd restart`

Stop the sshd service:

`root `[`#`]`rc-service sshd stop`

List services, their status, and the runlevels they belong to:

`root `[`#`]`rc-status --all`

Show enabled services and the runlevels they belong to (not whether they are running or not, just if they are enabled):

`root `[`#`]`rc-update show`

### [systemd]

Start the ssh daemon at boot:

`root `[`#`]`systemctl enable sshd`

Start the sshd service now:

`root `[`#`]`systemctl start sshd`

Check if the sshd service is running:

`root `[`#`]`systemctl status sshd`

## [Tips]

### [Generate metadata caches]

Ebuild repositories vary from very small to very large in size. As a result they slow down the majority of Portage operations. That happens because overlays do not contain metadata caches. The cache is used to speed up searches and the building of dependency trees. A neat trick is to generate local metadata cache after syncing overlays.

`root `[`#`]`emerge --regen`

This trick also works in conjunction with eix. [eix-update] can use metadata cache generated by [emerge \--regen] to speed up things. To enable this, add the following variable to [/etc/eixrc/00-eixrc]:

[FILE] **`/etc/eixrc/00-eixrc`**

    OVERLAY_CACHE_METHOD="assign"

### [Search packages in Portage by regular expressions]

To search packages in Portage, along with installed version, by regular expressions:

`root `[`#`]`emerge -s "%^python$"`

or

`root `[`#`]`emerge --search "%^python$"`

### [qcheck]

Use [qcheck] to verify installed packages:

`root `[`#`]`qcheck vim-core`

[qcheck] comes with [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]] and can be installed by running this command:

`root `[`#`]`emerge -a app-portage/portage-utils`

Learn more about [qcheck] by reading its manual page:

`user `[`$`]`man qcheck`

## [See also]

-   [Package_sets](https://wiki.gentoo.org/wiki/Package_sets#Portage "Package sets")

## [External resources]

-   [Original gentoo-cheat repository](https://github.com/jonasstein/gentoo-cheat)
-   [Forum post about gentoo-cheat](https://forums.gentoo.org/viewtopic-p-7370146.html)
-   [Another Gentoo cheat sheet](http://bradleymacomber.com/ref/Gentoo/)
-   [Collection of Gentoo tips](https://forums.gentoo.org/viewtopic-t-529919.html)
-   [Newbie cheat sheet](https://web.archive.org/web/20151001093213/http://www.gentoo-wiki.info/Newbie_cheat_sheet)