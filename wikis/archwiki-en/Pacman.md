# Pacman

The pacman package manager is one of the major distinguishing features of Arch Linux. It combines a simple binary package format with an easy-to-use Arch build system. The goal of pacman is to make it possible to easily manage packages, whether they are from the official repositories or the user's own builds.

pacman keeps the system up-to-date by synchronizing package lists with the master server. This server/client model also allows the user to download/install packages with a simple command, complete with all required dependencies.

pacman is written in the C programming language and uses the  tar format for packaging.

## Usage
What follows is just a small sample of the operations that pacman can perform. To read more examples, refer to .

## Installing packages
A package is an archive containing:

* all of the (compiled) files of an application
* metadata about the application, such as application name, version, dependencies, etc.
* installation files and directives for pacman

Arch's package manager pacman can install, update, and remove those packages. Using packages instead of compiling and installing programs yourself has various benefits:

* easily updatable: pacman will update existing packages as soon as updates are available
* dependency checks: pacman handles dependencies for you, you only need to specify the program and pacman installs it together with every other program it needs
* clean removal: pacman has a list of every file in a package; this way, no files are unintentionally left behind when you decide to remove a package.

## Installing specific packages
To install a single package or list of packages, including dependencies, issue the following command:

 # pacman -S package_name1 package_name2 ...

To install a list of packages with regex (see this forum thread):

 # pacman -S $(pacman -Ssq package_regex)

Sometimes there are multiple versions of a package in different repositories (e.g. extra and extra-testing). To install the version from the extra repository in this example, the repository needs to be defined in front of the package name:

 # pacman -S extra/package_name

To install a number of packages sharing similar patterns in their names, one can use curly brace expansion. For example:

 # pacman -S plasma-{desktop,mediacenter,nm}

This can be expanded to however many levels needed:

 # pacman -S plasma-{workspace{,-wallpapers},pa}

## Virtual packages
A virtual package is a special package which does not exist by itself, but is provided by one or more other packages. Virtual packages allow other packages to not name a specific package as a dependency, in case there are several candidates. Virtual packages cannot be installed by their name, instead they become installed in your system when you have installed a package providing the virtual package. An example is the dbus-units package.

## Installing package groups
Some packages belong to a group of packages that can all be installed simultaneously. For example, issuing the command:

 # pacman -S gnome

will prompt you to select the packages from the  group that you wish to install.

Sometimes a package group will contain a large amount of packages, and there may be only a few that you do or do not want to install. Instead of having to enter all the numbers except the ones you do not want, it is sometimes more convenient to select or exclude packages or ranges of packages with the following syntax:

 Enter a selection (default=all): 1-10 15

which will select packages 1 through 10 and 15 for installation, or:

 Enter a selection (default=all): ^5-8 ^2

which will select all packages except 5 through 8 and 2 for installation.

To see what packages belong to the gnome group, run:

 $ pacman -Sg gnome

Also visit https://archlinux.org/groups/ to see what package groups are available.

## Removing packages
To remove a single package, leaving all of its dependencies installed:

 # pacman -R package_name

To remove a package and its dependencies which are not required by any other installed package:

 # pacman -Rs package_name

The above may sometimes refuse to run when removing a group which contains otherwise needed packages. In this case try:

 # pacman -Rsu package_name

To remove a package, its dependencies and all the packages that depend on the target package:

 # pacman -Rsc package_name

To remove a package, which is required by another package, without removing the dependent package:

 # pacman -Rdd package_name

pacman saves important configuration files when removing certain applications and names them with the extension: .pacsave. To prevent the creation of these backup files use the  option:

 # pacman -Rn package_name

## Upgrading packages
pacman can update all packages on the system with just one command. This could take quite a while depending on how up-to-date the system is. The following command synchronizes the repository databases and updates the system's packages, excluding "local" packages that are not in the configured repositories:

 # pacman -Syu

## Querying package databases
pacman queries the local package database with the  flag, the sync database with the  flag and the files database with the  flag. See ,  and  for the respective suboptions of each flag.

pacman can search for packages in the database, searching both in packages' names and descriptions:

 $ pacman -Ss string1 string2 ...

Sometimes, 's builtin ERE (Extended Regular Expressions) can cause a lot of unwanted results, so it has to be limited to match the package name only; not the description nor any other field:

 $ pacman -Ss '^vim-'

To search for already installed packages:

 $ pacman -Qs string1 string2 ...

To search for package file names in remote packages:

 $ pacman -F string1 string2 ...

To display extensive information about a given package (e.g. its dependencies):

 $ pacman -Si package_name

For locally installed packages:

 $ pacman -Qi package_name

Passing two  flags will also display the list of backup files and their modification states:

 $ pacman -Qii package_name

To retrieve a list of the files installed by a package:

 $ pacman -Ql package_name

To retrieve a list of the files installed by a remote package:

 $ pacman -Fl package_name

To verify the presence of the files installed by a package:

 $ pacman -Qk package_name

Passing the  flag twice will perform a more thorough check.

To query the database to know which package a file in the file system belongs to:

 $ pacman -Qo /path/to/file_name

To query the database to know which remote package a file belongs to:

 $ pacman -F /path/to/file_name

To list all packages no longer required as dependencies (orphans):

 $ pacman -Qdt

To list all packages explicitly installed and not required as dependencies:

 $ pacman -Qet

See pacman/Tips and tricks for more examples.

For advanced functionality, install pkgfile, which uses a separate database with all files and their associated packages.

## Pactree
Install the  package to get .

To view the dependency tree of a package:

 $ pactree package_name

To view the dependent tree of a package, pass the reverse flag  to pactree.

## Database structure
The pacman databases are normally located at . For each repository specified in , there will be a corresponding database file located there. Database files are gzipped tar archives containing one directory for each package, for example for the  package:

The  file contains meta data such as the package description, dependencies, file size and MD5 hash.

## Cleaning the package cache
Pacman stores its downloaded packages in  and does not remove the old or uninstalled versions automatically. This has some advantages:

# It allows to downgrade a package without the need to retrieve the previous version through other means, such as the Arch Linux Archive.
# A package that has been uninstalled can easily be reinstalled directly from the cache directory, not requiring a new download from the repository.

However, it is necessary to deliberately clean up the cache periodically to prevent the directory to grow indefinitely in size.

The  script, provided within the  package, deletes all cached versions of installed and uninstalled packages, except for the most recent three, by default:

 # paccache -r

Enable and start  to discard unused packages weekly. You can configure the arguments for the service in , e.g with  or  for the two examples below.

You can also define how many recent versions you want to keep. To retain only one past version use:

 # paccache -rk1

Add the / switch to limit the action of paccache to uninstalled packages. For example to remove all cached versions of uninstalled packages, use the following:

 # paccache -ruk0

See  for more options.

pacman also has some built-in options to clean the cache and the leftover database files from repositories which are no longer listed in the configuration file . However pacman does not offer the possibility to keep a number of past versions and is therefore more aggressive than paccache default options.

To remove all the cached packages that are not currently installed, and the unused sync databases, execute:

 # pacman -Sc

To remove all files from the cache, use the clean switch twice, this is the most aggressive approach and will leave nothing in the cache directory:

 # pacman -Scc

 and  are two further alternatives to clean the cache.

## Additional commands
Download a package without installing it:

 # pacman -Sw package_name

Install a 'local' package that is not from a remote repository (e.g. the package is from the AUR):

 # pacman -U /path/to/package/package_name-version.pkg.tar.zst

To keep a copy of the local package in pacmans cache, use:

 # pacman -U file:///path/to/package/package_name-version.pkg.tar.zst

Install a 'remote' package (not from a repository stated in pacmans configuration files):

 # pacman -U http://www.example.com/repo/example.pkg.tar.zst

## Dry run
pacman always lists packages to be installed or removed, and asks for permission before taking any action.

To get a list in a processable format, and to prevent the actions of ,  and , you can use , short for .

 can be added to format this list in various ways.  will return a list without package versions.

## Installation reason
The pacman database organizes installed packages into two groups, according to installation reason:

* explicitly-installed: packages that were literally passed to a generic pacman  or  command;
* dependencies: packages that, despite never (in general) having been passed to a pacman installation command, were implicitly installed because they were  required by packages explicitly installed.

When installing a package, it is possible to force its installation reason to dependency with:

 # pacman -S --asdeps package_name

The command is normally used because explicitly-installed packages may offer optional packages, usually for non-essential features for which the user has discretion.

When reinstalling a package, though, the current installation reason is preserved by default.

The list of explicitly-installed packages can be shown with , while the complementary list of dependencies can be shown with .

To change the installation reason of an already installed package, execute:

 # pacman -D --asdeps package_name

Use  to do the opposite operation.

## What happens during package install/upgrade/removal
When successful, the workflow of a transaction follows five high-level steps plus pre/post transaction hooks:

# Initialize the transaction if there is not a database lock.
# Choose which packages will be added or removed in the transaction.
# Prepare the transaction, based on flags, by performing sanity checks on the sync databases, packages, and their dependencies.
# Commit the transaction:
## When applicable, download packages ().
## If pre-existing pacman  hooks apply, they are executed.
## Packages are removed that are to-be-replaced, conflicting, or explicitly targeted to be removed.
## If there are packages to add, then each package is committed:
### If the package has an install script, its  function is executed (or  or  in the case of an upgraded or removed package).
### pacman deletes all the files from a pre-existing version of the package (in the case of an upgraded or removed package). However, files that were marked as configuration files in the package are kept (see /Pacnew and Pacsave).
### pacman untars the package and dumps its files into the file system (in the case of an installed or upgraded package). Files that would overwrite kept, and manually modified, configuration files (see previous step), are stored with a new name (.pacnew).
### If the package has an install script, its  function is executed (or  or  in the case of an upgraded or removed package).
## If pacman  hooks that exist at the end of the transaction apply, they are executed.
# Release the transaction and transaction resource (i.e. database lock).

## Configuration
pacman settings are located in : this is the place where the user configures the program to work in the desired manner. In-depth information about the configuration file can be found in .

## General options
General options are in the  section. Read  or look in the default  for information on what can be done here.

## Comparing versions before updating
To see old and new versions of available packages, uncomment the "VerbosePkgLists" line in . The output of  will be like this:

 Package (6)             Old Version  New Version  Net Change  Download Size

 extra/libmariadbclient  10.1.9-4     10.1.10-1      0.03 MiB       4.35 MiB
 extra/libpng            1.6.19-1     1.6.20-1       0.00 MiB       0.23 MiB
 extra/mariadb           10.1.9-4     10.1.10-1      0.26 MiB      13.80 MiB

## Parallel downloads
The number of packages being downloaded in parallel (at the same time) are configured in  with the  option under . The  shipped with the  package sets it to . If the option is unset, packages will be downloaded sequentially.

## Skip package from being upgraded
To have a specific package skipped when upgrading the system, add this line in the  section:

 IgnorePkg=linux

For multiple packages use a space-separated list, or use additional  lines. Also, glob patterns can be used. If you want to skip packages just once, you can also use the  option on the command-line - this time with a comma-separated list.

It will still be possible to upgrade the ignored packages using : in this case pacman will remind you that the packages have been included in an  statement.

## Skip package group from being upgraded
As with packages, skipping a whole package group is also possible:

 IgnoreGroup=gnome

## Skip file from being upgraded
All files listed with a  directive will never be touched during a package install/upgrade, and the new files will be installed with a .pacnew extension.

 NoUpgrade=path/to/file

Multiple files can be specified like this:

 NoUpgrade=path/to/file1 path/to/file2

## Skip files from being installed to system
To always skip installation of specific files or directories list them under . For example, to avoid installing bash completion scripts, use:

 NoExtract=usr/share/bash-completion/completions/*

Later rules override previous ones, and you can negate a rule by prepending .

## Maintain several configuration files
If you have several configuration files (e.g. main configuration and configuration with testing repository enabled) and would have to share options between configurations you may use  option declared in the configuration files, e.g.:

 Include = /path/to/common/settings

where  file contains the same options for both configurations.

## Hooks
pacman can run pre- and post-transaction hooks from the  directory; more directories can be specified with the  option in , which defaults to . Hook file names must be suffixed with .hook. pacman hooks are not interactive.

pacman hooks are used, for example, in combination with  and  to automatically create system users and files during the installation of packages. For example,  specifies that it wants a system user called  and certain directories owned by this user. The pacman hooks  and  invoke  and  when pacman determines that  contains files specifying users and tmp files.

For more information on alpm hooks, see .

## Repositories and mirrors
Besides the special section, each other  in  defines a package repository to be used. A repository is a logical collection of packages, which are physically stored on one or more servers: for this reason each server is called a mirror for the repository.

Repositories are distinguished between official and unofficial. The order of repositories in the configuration file matters; repositories listed first will take precedence over those listed later in the file when packages in two repositories have identical names, regardless of version number. In order to use a repository after adding it, you will need to upgrade the whole system first.

Each repository section allows defining the list of its mirrors directly or in a dedicated external file through the  directive; for example, the mirrors for the official repositories are included from . See the Mirrors article for mirror configuration.

## Package cache directory
pacman stores downloaded package files in cache, in a directory denoted by  in [options section of  (defaults to  if not set).

Cache directory may grow over time, even if keeping just the freshest versions of installed packages.

If you want to move that directory to some more convenient place, do one of the following:

* Set the  option in  to new directory. Remember to retain the trailing slash. This is the recommended solution.
* Mount a dedicated partition or e.g. Btrfs subvolume in .
* Bind-mount selected directory in .

## Package security
pacman supports package signatures, which add an extra layer of security to the packages. The default configuration, , enables signature verification for all the packages on a global level. This can be overridden by per-repository  lines. For more details on package signing and signature verification, take a look at pacman-key.

## Troubleshooting
## "Failed to commit transaction (conflicting files)" error
If you see the following error: error: could not prepare transaction
 error: failed to commit transaction (conflicting files)
 package: /path/to/file exists in filesystem
 Errors occurred, no packages were upgraded.

This is happening because pacman has detected a file conflict, and by design, will not overwrite files for you. This is by design, not a flaw.

The problem is usually trivial to solve (although to be sure, you should try to find out how these files got there in the first place). A safe way is to first check if another package owns the file (). If the file is owned by another package, file a bug report. If the file is not owned by another package, rename the file which "exists in filesystem" and re-issue the update command. If all goes well, the file may then be removed.

If you had installed a program manually without using pacman, for example through , you have to remove/uninstall this program with all of its files. See also Pacman tips#Identify files not owned by any package.

Every installed package provides a  file that contains metadata about this package. If this file gets corrupted, is empty or goes missing, it results in  errors when trying to update the package. Such an error usually concerns only one package. Instead of manually renaming and later removing all the files that belong to the package in question, you may explicitly run  to force pacman to overwrite files that match .

## "Failed to commit transaction (invalid or corrupted package)" error
Look for .part files (partially downloaded packages) in  and remove them (often caused by usage of a custom  in ).

 # find /var/cache/pacman/pkg/ -iname "*.part" -delete

That same error may also appear if archlinux-keyring is out-of-date, preventing pacman from verifying signatures. See Pacman/Package signing#Upgrade system regularly for the fix and how to avoid it in the future.

## "Failed to init transaction (unable to lock database)" error
When pacman is about to alter the package database, for example installing a package, it creates a lock file at . This prevents another instance of pacman from trying to alter the package database at the same time.

If pacman is interrupted while changing the database, this stale lock file can remain. If you are certain that no instances of pacman are running then delete the lock file:

 # rm /var/lib/pacman/db.lck

## Packages cannot be retrieved on installation
This error manifests as ,  or .

Firstly, ensure the package actually exists. If certain the package exists, your package list may be out-of-date. Try running  to force a refresh of all package lists and upgrade. Also make sure the selected mirrors are up-to-date and repositories are correctly configured. You can also use Reflector to keep the mirrors up-to-date.

If pacman reports there is nothing to update, but the  error continues to be printed, consider forcing a database download with . This is never needed under normal circumstances, so inspect more closely the status and consistency of the mirror.

It could also be that the repository containing the package is not enabled on your system, e.g. the package could be in the multilib repository, but multilib is not enabled in your .

See also FAQ#Why is there only a single version of each shared library in the official repositories?.

## Fixing an unbootable system caused by an interrupted upgrade
Whether due to power loss, kernel panic or hardware failure an update may be interrupted. In most cases, there will not be much damage but the system will likely be unbootable.

# Ready a USB flash installation medium and boot it.
# Mount the root filesystem as well as your ESP.
#  into the mounted root filesystem.
# Check  and replicate the exact update by supplying the entire list of packages that was upgraded during the failed transaction to , allowing it to reinstall while resuming the original update:

 # pacman -Syu $(grep "\[2025-07-27T22.*\ \upgraded" /var/log/pacman.log | cut -d " " -f4 | tr "\n" " ")

Replicating the exact upgrade is needed to ensure the right scriptlets and hooks will run.

## pacman crashes during an upgrade
In the case that pacman crashes with a "database write" error while removing packages, and reinstalling or upgrading packages fails thereafter, do the following:

# Boot using the Arch USB flash installation medium. Preferably use a recent media so that the pacman version matches/is newer than the system.
# Mount the system's root filesystem, e.g.,  as root, and check the mount has sufficient space with
# Mount the proc, sys and dev filesystems as well:
# If the system uses default database and directory locations, you can now update the system's pacman database and upgrade it via  as root.
#* Alternatively, if you cannot update/upgrade, refer to Pacman/Tips and tricks#Reinstalling all packages.
# After the upgrade, one way to double-check for not upgraded but still broken packages:
# Followed by a re-install of any still broken package via .

## pacman: command not found
If  is a symlink, pacman will try to make a directory instead and thus remove this symlink during self-upgrade. This will cause the update to fail. As a result,  and other contents of the  package will be missing.

Never symlink  because it is controlled by pacman. Use the  option or a bind mount instead; see #Package cache directory.

If you have already encountered this problem and broke your system, you can manually extract  contents from the package to restore pacman and then reinstall it properly; see  and [https://bbs.archlinux.org/viewtopic.php?id=241213 related forum thread for details.

## Manually reinstalling pacman
## Using pacman-static
 is a statically compiled version of pacman, so it will be able to run even when the libraries on the system are not working. This can also come in handy when a partial upgrade was performed and pacman can not run anymore.

## Using a precompiled pacman-static binary when PKGBUILD build fails
In some situations, your system may be too broken to run makepkg or to build the  package (e.g., due to missing or incompatible libraries). In this case, you can download a precompiled pacman-static binary from a trusted source. This static binary does not depend on system libraries and can be used to restore a working pacman on your system.

An outdated binary is provided by https://pkgbuild.com/~morganamilo/pacman-static/x86_64/bin/pacman-static

Download it, make it executable, then:

 # ./pacman-static -Syu pacman

This will update your system and reinstall , fixing broken dependencies related to missing shared libraries.

## Using an external pacman
If even pacman-static does not work, it is possible to recover using an external pacman. One of the easiest methods to do so is by using the archiso and simply using  or  to specify the mount point of the system to perform the operation on. See Chroot#Using chroot on how to mount the necessary filesystems required by .

## By manually extracting
Even if pacman is terribly broken, you can fix it manually by downloading the latest packages and extracting them to the correct locations. The rough steps to perform are:

# Determine the  dependencies to install
# Download each package from a mirror of your choice
# Extract each package to root
# Reinstall these packages with  to update the package database accordingly
# Do a full system upgrade

If you have a healthy Arch system on hand, you can see the full list of dependencies with:

 $ pacman -Q $(pactree -u pacman)

But you may only need to update a few of them depending on your issue. An example of extracting a package is

 # tar -xvpwf package.tar.zst -C / --exclude .PKGINFO --exclude .INSTALL --exclude .MTREE --exclude .BUILDINFO

Note the use of the  flag for interactive mode. Running non-interactively is very risky since you might end up overwriting an important file. Also take care to extract packages in the correct order (i.e. dependencies first). This forum post contains an example of this process where only a couple pacman dependencies are broken.

## "Unable to find root device" error after rebooting
Most likely the initramfs became corrupted during a kernel update (improper use of pacmans  option can be a cause). There are two options; first, try the Fallback entry.

Once the system starts, run this command (for the stock  kernel) either from the console or from a terminal to rebuild the initramfs image:

 # mkinitcpio -p linux

If that does not work, from a current Arch release (CD/DVD or USB stick), mount your root and boot partitions to  and , respectively. Then chroot using arch-chroot:

 # arch-chroot /mnt
 # pacman -Syu mkinitcpio systemd linux

Reinstalling the kernel (the  package) will automatically re-generate the initramfs image with . There is no need to do this separately.

Afterwards, it is recommended that you run , {{ic|umount /mnt/{boot,} }} and .

## "Warning: current locale is invalid; using default "C" locale" error
As the error message says, your locale is not correctly configured. See Locale.

## Missing locales warning messages
When locale files are intentionally removed by tools such as  or ,  may issue warnings about missing locales during package updates.

To suppress these warnings, you can comment out the  option in . Keep in mind that disabling CheckSpace turns off the space-checking functionality for all package installations, so use this workaround only when you have alternative means to monitor disk space.

## pacman does not honor proxy settings
Make sure that the relevant environment variables (,  etc.) are set up. If you use  pacman with sudo, you need to configure sudo to pass these environment variables to pacman. Also, ensure the configuration of dirmngr has  in  to honor the proxy when refreshing the keys.

## How do I reinstall all packages, retaining information on whether something was explicitly installed or as a dependency?
To reinstall all the native packages:  or  (the  option preserves the installation reason by default).

You will then need to reinstall all the foreign packages, which can be listed with .

## "Cannot open shared object file" error
It looks like previous pacman transaction removed or corrupted shared libraries needed for pacman itself.

To recover from this situation, you need to unpack required libraries to your filesystem manually. First find what package contains the missed library and then locate it in the pacman cache (). Unpack required shared library to the filesystem. This will allow to run pacman.

Now you need to reinstall the broken package. Note that you need to use  flag as you just unpacked system files and pacman does not know about it. pacman will correctly replace our shared library file with one from package.

That is it. Update the rest of the system.

## Freeze of package downloads
Some issues have been reported regarding network problems that prevent pacman from updating/synchronizing repositories. [https://bbs.archlinux.org/viewtopic.php?id=65728 When installing Arch Linux natively, these issues have been resolved by replacing the default pacman file downloader with an alternative (see Improve pacman performance for more details). When installing Arch Linux as a guest OS in VirtualBox, this issue has also been addressed by using Host interface instead of NAT in the machine properties.

## Failed retrieving file 'core.db' from mirror
If you receive this error message with correct mirrors, try setting a different name server.

## error: 'local-package.pkg.tar': permission denied
If you want to install a package on an sshfs mount using  and receive this error, move the package to a local directory and try to install again.

## error: could not determine cachedir mount point /var/cache/pacman/pkg
Upon executing, e.g.,  inside a chroot environment an error is encountered:

 error: could not determine cachedir mount point /var/cache/pacman/pkg
 error: failed to commit transaction (not enough free disk space)

This is frequently caused by the chroot directory not being a mountpoint when the chroot is entered. See the note at Install Arch Linux from existing Linux#Downloading basic tools for a solution, and  for an explanation and an example of using bind mounting to make the chroot directory a mountpoint.

## error: GPGME error: No data
If you are unable to update packages and receive this error, then try  before attempting to update.

If removing sync files does not help, check that the sync files are  using  before attempting to update. A router or proxy might corrupt the downloads. Corruption could possibly be HTML type.

If sync files are of the correct type, there might be an issue with the mirror server. Look up the mirror server(s) in use with  and . Paste the first returned url in a browser and check that a file listing is returned. In case the mirror returns an error, comment it in . You may try updating or re-ranking mirrors.

## error: GPGME error: General error and ":: File /var/cache/pacman/pkg/.pkg.tar.zst is corrupted (invalid or corrupted package (PGP signature)).
If this error occurs and you are, for instance, unable to update your system or any package at all, it is possible that you have  set to a blank value, which seems to break the GPG-Flow.

In this case,  or setting it to a arbitrary value will most likely allow to update again, in case any other option above did not do the trick yet. See this post for further details.

## Reinstall broken or out-of-sync packages
One may use the  to check if the installed files of the  package match the files from its database version. For several packages, one may use the following loop to reinstall all packages which have missing file(s):

 # LC_ALL=C.UTF-8 pacman -Qk 2>/dev/null | grep -v ' 0 missing files' | cut -d: -f1 |
     while read -r package; do
         pacman -S "$package" --noconfirm
     done

Suppose that your local database located in  is more up-to-date compared to installed packages in the  filesystem (e.g., because of a partial rollback), then this method is the appropriate one to re-synchronize the root filesystem with the local database.

## Check for missing/corrupted files
In case of accidental deletion of system files or other file anomalies, run this command to see which files are missing from all pacman packages:

 # pacman -Qk $(pacman -Qsq) | grep -v " 0 missing files"

It will print nothing if nothing is missing, and something like this if something is missing:

 X total files, [>=1 missing file(s)

To check for file corruption as well:

 # pacman -Qkk $(pacman -Qsq) | grep -v " 0 altered files"

There will be false positives, especially in /etc/*
