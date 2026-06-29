# Pacman/Rosetta

This page uses a table to display the correspondence of package management commands among some of the most popular Linux distributions. The original inspiration was given by openSUSE's Software Management Command Line Comparison.

## Basic operations
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Search for package(s). What exact fields are being searched by default varies in each tool. Mostly options bring tools on par. ||  ||  ||  ||  or  ||  ()
or  ()
|-
| Install package(s) by name ||  ||  ||  ||  or  ||
|-
| Only print the targets instead of performing the actual operation ||  (or ) ||  ||  (or , , ) ||   ||  ()
|-
| Toggle the manual confirmations ||  or  ||  () or  ||  () ||  () or  () ||  ()
|-
| Refresh the local package repository ||  (see the warnings about partial updates) ||  or  or  (built-in auto function) ||  ||  or   ||
|-
| Upgrade Packages - Install packages which have an older version already installed ||  ||  ||  ||  or  ||
|-
| Upgrade Packages - Another form of the update command, which can perform more complex updates -- like distribution upgrades. When the usual update command will omit package updates, which include changes in dependencies, this command can perform those updates. ||  ||  ||  ||  ||
|-
| Remove a package(s) and all dependencies by name ||  ||  ||  ||  or  ||  ()
|-
| Remove a package(s) and its configuration files ||  || ? ||  || ? || n/a
|-
| Remove a package(s) and all dependencies and configuration files ||  || ? ||  || ? || n/a
|-
| Remove dependencies that are no longer needed (orphans), because e.g. the package which needed the dependencies was removed. ||  ( to also remove optional deps)||  ||  ||  (just for removing a package) or  (listing only) ||  ()
|-
| Remove packages no longer included in any repositories. ||  ||  ||  |||| ?
|-
| Mark a package previously installed as a dependency as explicitly required. ||  ||  ||  ||  (workaround which needs to reinstall the package) ||  ()
|-
| Install package(s) as dependency / without marking as explicitly required. ||  ||  and then  ||  || n/a (feature request + workaround) ||  ()
|-
| Only downloads the given package(s) without unpacking or installing them ||  ||  ||  (into the package cache) or  (bypass the package cache) ||  ||  ()
|-
| Clean up all local caches. Options might limit what is actually cleaned. ||  or  ||  ||  removes only unneeded, obsolete information or  ||  ||
|-
| Start a shell to enter multiple commands in one session ||||  || ||  ||
|-
| Show a log of actions taken by the software management. || read  ||  || read  || read  or  provided by an additional package || read
|-
| Get a dump of the whole system information - Prints, Saves or similar the current state of the package management system. Preferred output is text or XML. (Note: Why either-or here? No tool offers the option to choose the output format.) || see  || see  ||  ||||
|-
| e-mail delivery of package changes ||||||  ||||
|-
|}

## Querying specific packages
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Show all or most information about a package. The tools' verbosity for the default command vary. But with options, the tools are on par with each other. ||  or  ||  or  ||  or  ||  or  || ,  or
|-
| Display local package information: Name, version, description, etc. ||  ||  /  ||  or  ||  or  ||  or
|-
| Display remote package information: Name, version, description, etc.||  ||  ||  or  ||  ||  and  or
|-
| Display files provided by local package ||  ||  ||  ||  ||  or
|-
| Display files provided by a remote package ||  ||  or  (from package yum-utils) ||  ||||
|-
| Query the package which provides FILE ||  ||  (installed only) or  (everything) or  (from package yum-utils) ||  or  ||  (installed only) or  (everything) ||  or
|-
| List the files that the package holds. Again, this functionality can be mimicked by other more complex commands. ||  or  ||  ||  ||  ||  or
|-
| Displays packages which provide the given exp. aka reverse provides. Mainly a shortcut to search a specific field. Other tools might offer this functionality through the search command. ||  ||  ||  ||  or  (exact match) or  (fuzzy match) ||  (only installed packages) or
|-
| Search all packages to find the one which holds the specified file. ||  ||  ||  or  is using this functionality. ||  ||  or
|-
| Show the changelog of a package||  ||  ||  ||  ||
|-
|}

## Querying package lists
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Search for package(s) by searching the expression in name, description, short description. What exact fields are being searched by default varies in each tool. Mostly options bring tools on par. ||  ||  ||  ||  or  ||  or
|-
| Lists packages which have an update available. Note: Some provide special commands to limit the output to certain installation sources, others use options. ||  ||  or  ||  ||  or  (just for patches) ||
|-
| Display a list of all packages in all installation sources that are handled by the packages management. Some tools provide options or additional commands to limit the output to a specific installation source. ||  ||  ||  or  (Cache only) or  ||  ||
|-
| Generates a list of installed packages ||  ||  ||  ||  ||
|-
| List packages that are installed but are not available in any installation source (anymore). ||  ||  ||  ||  ||
|-
| List packages that were recently added to one of the installation sources, i.e. which are new to it. || ||  ||  or  || ||
|-
| List installed local packages along with version ||  ||  ||  or  ||  or  ||
|-
| Search locally installed package for names or descriptions ||  ||  ||  ||  ||
|-
| List packages not required by any other package ||  ||  or  ||  ||  ||
|-
| List packages installed explicitly (not as dependencies) ||  ||  ||  ||   ||  or
|-
| List packages installed automatically (as dependencies) ||  ||  ||  ||  ||
|-
|}

## Querying package dependencies
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Display packages which require X to be installed, aka show reverse dependencies. ||  or  ||  or  ||  or  ||  ||
|-
| Display packages which conflict with given expression (often package). Search can be used as well to mimic this function. ||  or  ||  ||  ||  ||
|-
| List all packages which are required for the given package, aka show dependencies. ||  or  ||  or  ||  or  ||  ||
|-
| List what the current package provides ||  or   ||  ||  or  ||  ||  or
|-
| List all packages that require a particular package ||  ||  || {{ic|aptitude search ~D{depends,recommends,suggests}:$pattern}} or  or  ||  ||
|-
| Display all packages that the specified packages obsoletes. ||  or  ||  ||  ||  ||
|-
| Generates an output suitable for processing with dotty for the given package(s). || || ||  || ||
|-
|}

## Installation sources management
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Installation sources management ||edit  || edit {{ic|/etc/yum.repos.d/${REPO}.repo}}|| edit  || edit {{ic|/etc/zypp/repos.d/${REPO}.repo}} ||  or
|-
| Add an installation source to the system. Some tools provide additional commands for certain sources, others allow all types of source URI for the add command. Again others, like apt force editing a sources list. apt-cdrom is a special command, which offers special options design for CDs/DVDs as source. || edit  ||  ||  ||  ||  or
|-
| Refresh the information about the specified installation source(s) or all installation sources. ||  (always upgrade the whole system afterwards) ||  and then  ||  ||  or   ||  or
|-
| Prints a list of all installation sources including important information like URI, alias etc. ||  ||  ||  ||  or   ||  or
|-
| List all packages from a certain repo||  || || ||  or  ||
|-
| Disable an installation source for an operation || || || || ||
|-
| Download packages from a different version of the distribution than the one installed. ||  ||  ||  or  (dependencies not covered) ||  ||  and then
|-
|}

## Overrides
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Add a package lock rule to keep its current state from being changed || edit  modifying IgnorePkg array || edit  adding/amending the  option ||  ||  or put package name in  ||
|-
| Delete a package lock rule || edit  removing package from IgnorePkg line || ||  ||  or remove package name from  ||  (or )
|-
| Show a listing of all lock rules ||  || ||  ||  or view  ||
|-
| Set the priority of the given package to avoid upgrade, force downgrade or to overwrite any default behavior. Can also be used to prefer a package version from a certain installation source. || edit  modifying HoldPkg and/or IgnorePkg arrays || || , ||  || edit  adding a line with
|-
| Remove a previously set priority || || ||  ||  || edit  removing offending line
|-
| Show a list of set priorities || || ||  or  ||  ||
|-
|}

## Verification and repair
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Verify single package ||  (can add another ) ||  ||  ||  ||
|-
| Verify all packages ||  (can add another ) ||  ||  ||  ||
|-
| Reinstall given package; this will reinstall the given package without dependency hassle ||  ||  ||  ||  ||
|-
| Verify dependencies of the complete system; used if installation process was forcefully killed ||  ||  ||  ||  ||
|-
| Use some magic to fix broken dependencies in a system || for pacman dependency level, use ; for shared library level, use  or  (from ) ||  ||   and then  ||  ||
|-
| Add a checkpoint to the package system for later rollback || || (unnecessary, it is done on every transaction) || || n/a ||
|-
| Remove a checkpoint from the system || n/a || n/a || || n/a ||
|-
| Provide a list of all system checkpoints || n/a ||  || || n/a ||
|-
| Rolls entire packages back to a certain date or checkpoint || n/a ||  || || n/a ||
|-
| Undo a single specified transaction || n/a ||  || || n/a ||
|-
|}

## Using package files and building packages
{| class="wikitable"
! Action !! Arch !! Red Hat/Fedora !! Debian/Ubuntu !! SLES/openSUSE !! Gentoo
|-
| Query a package supplied on the command line rather than an entry in the package management database ||  ||  ||  || ||
|-
| List the contents of a package file ||  ||  ||  ||  ||
|-
| Install local package file, e.g. app.rpm and uses the installation sources to resolve dependencies ||  ||  ||  ||  ||
|-
| Updates package(s) with local packages and uses the installation sources to resolve dependencies ||  ||  ||  || ||
|-
| Add a local package to the local package cache mostly for debugging purposes. ||  || ||  || n/a ||
|-
| Extract a package ||  ||  ||  ||  ||
|-
| Install/Remove packages to satisfy build-dependencies. Uses information in the source package || Use ABS and  ||  ||  ||  ||
|-
| Display the source package to the given package name(s) || ||  ||  || n/a ||
|-
| Download the corresponding source package(s) to the given package name(s) || Use ABS and  ||  ||  or  ||  ||
|-
| Build a package, checking and installing required dependencies first ||  ||  (normal) or mock (in chroot) ||  || , then build, and then  ||  or
|-
| Check for possible packaging issues || namcap(requires ) || rpmlint || lintian || rpmlint || repoman
|-
|}

## Log file rotation
By default, Arch Linux does not rotate . See, for example,  and . This is in contrast to the default policy of most other Linux distributions. Some distributions, notably Gentoo, hardly write log files by default.
