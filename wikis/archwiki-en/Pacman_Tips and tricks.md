# Pacman/Tips and tricks

For general methods to improve the flexibility of the provided tips or pacman itself, see Core utilities and Bash.

## Maintenance
See also System maintenance.

## Listing packages
## In unused repositories
By default, repositories listed in  are used for syncing, searching, installing and upgrading from them. This can be changed for more versatility, for example by using some repositories only for searching in themSee .

## With version
You may want to get the list of installed packages with their version, which is useful when reporting bugs or discussing installed packages.

* List all explicitly installed packages:
* List all packages in the package group named :
* List all foreign packages (typically manually downloaded and installed or packages removed from the repositories):
* List all native packages (installed from the sync database):
* List all explicitly installed native packages (i.e. present in the sync database) that are not direct or optional dependencies:
* List packages by regex:
* List packages by regex with custom output format (needs ):

## With size
Figuring out which packages are largest can be useful when trying to free space on your hard drive. There are two options here: get the size of individual packages, or get the size of packages and their dependencies.

## Individual packages
The following command will list all installed packages and their individual sizes:

 $ LC_ALL=C.UTF-8 pacman -Qi | awk '/^Name/{name=$3} /^Installed Size/{print $4$5, name}' | LC_ALL=C.UTF-8 sort -h

## Packages and dependencies
To list package sizes with their dependencies,

* Install  and run .
* Run  with the  option.

To list the download size of several packages (leave  blank to list all packages):

 $ expac -S -H M '%k\t%n' packages

To list explicitly installed packages not in the meta package  nor package group  with size and description:

 $ expac -H M "%011m\t%-20n\t%10d" $(comm -23  None found.'"}} The package  provides such hook with a more verbose instructions.}}

## Detecting more unneeded packages
In some cases the method above will not detect all possible unneeded packages. E.g. dependency cycles (also known as "circular dependencies"), excessive dependencies (fulfilled more than once), some non-explicit optionals etc.

To detect such packages:

 $ pacman -Qqd | pacman -Rsu --print -

If you want to remove all packages in the list at once, run the command without  argument.

Sometimes there may be multiple packages providing the same item. For example, there may be multiple packages which provide ttf-font. You may not want all such packages depending on your preference.

To detect packages which provide same item:

 $ awk '/%(NAME|PROVIDES)%/{flag=1;next}/^$/{flag=0}flag{ printf "%s\t%s\n", FILENAME, $0}' /var/lib/pacman/local/*/desc  | sed 's%/var/lib/pacman/local/\(.*\)/desc%\1%g' | sort -k2 | uniq -Df1 | column -etN Package,Provides

Check the output and carefully remove redundant package which you do not require.

## Removing everything but essential packages
If it is ever necessary to remove all packages except the essentials packages, one method is to set the installation reason of the non-essential ones as dependency and then remove all unnecessary dependencies.

First, for all the packages "explicitly installed", change their installation reason to "installed as a dependency":

 # pacman -D --asdeps $(pacman -Qqe)

Then, change the installation reason to "explicitly installed" of only the essential packages, those you do not want to remove, in order to avoid targeting them:

 # pacman -D --asexplicit base linux linux-firmware

Finally, follow the instructions in #Removing unused packages (orphans) to remove all packages that are "installed as a dependency".

## Getting the dependencies list of several packages
Dependencies are alphabetically sorted and doubles are removed.

 $ LC_ALL=C.UTF-8 pacman -Si packages | awk -F'[:' '/^Depends/ {print $2}' | xargs -n1 | sort -u

Alternatively, with :

 $ expac -l '\n' %E -S packages | sort -u

## Listing changed backup files
To list configuration files tracked by pacman as susceptible of containing user changes (i.e. files listed in the PKGBUILD backup array) and having received user modifications, use the following command:

 # pacman -Qii | awk '/\{print $(NF - 1)}'

Running this command with root permissions will ensure that files readable only by root (such as ) are included in the output.

This can be used when doing a selective system backup or when trying to replicate a system configuration from one machine to another.

## Back up the pacman database
The following command can be used to back up the local pacman database:

 $ tar -cjf pacman_database.tar.bz2 /var/lib/pacman/local

Store the backup pacman database file on one or more offline media, such as a USB stick, external hard drive, or CD-R.

The database can be restored by moving the  file into the  directory and executing the following command:

 # tar -xjvf pacman_database.tar.bz2

## Check changelogs easily
When maintainers update packages, commits are often commented in a useful fashion. Users can quickly check these from the command line by installing . This utility lists recent commit messages for packages from the official repositories or the AUR, by using .

## Installation and recovery
Alternative ways of getting and restoring packages.

## Installing packages from a CD/DVD or USB stick
To download packages, or groups of packages:

 # cd ~/Packages
 # pacman -Syw --cachedir "$PWD" base base-devel grub-bios xorg gimp
 # repo-add ./custom.db.tar.zst ./*.pkg.tar.zst

Pacman, which will reference the host installation by default, will not properly resolve and download existing dependencies. In cases where all packages and dependencies are wanted, it is recommended to create a temporary blank DB and reference it with :

 # mkdir /tmp/blankdb
 # pacman -Syw --cachedir "$PWD" --dbpath /tmp/blankdb base base-devel grub-bios xorg gimp
 # repo-add ./custom.db.tar.zst ./*.pkg.tar.zst

Then you can burn the "Packages" directory to an optical disc (e.g. CD, DVD) or transfer it to a USB flash drive, external HDD, etc.

To install:

1. Mount the media:

For an optical disc drive:

 # mount --mkdir /dev/sr0 /mnt/repo

For a USB flash drive, hard disk drive, etc.:

 # mount --mkdir /dev/sdxY /mnt/repo

2. Edit  and add this repository before the other ones (e.g. extra, core, etc.). This is important. Do not just uncomment the one on the bottom. This way it ensures that the files from the CD/DVD/USB take precedence over those in the standard repositories:

3. Finally, synchronize the pacman database to be able to use the new repository:
 # pacman -Syu

## Custom local repository
Use the repo-add script included with pacman to generate a database for a personal repository. Use  for more details on its usage.
A package database is a tar file, optionally compressed. Valid extensions are .db or .files followed by an archive extension of .tar, .tar.gz, .tar.bz2, .tar.xz, .tar.zst, or .tar.Z. The file does not need to exist, but all parent directories must exist.

To add a new package to the database, or to replace the old version of an existing package in the database, run:

 $ repo-add /path/to/repo.db.tar.zst /path/to/package-1.0-1-x86_64.pkg.tar.zst

The database and the packages do not need to be in the same directory when using repo-add, but keep in mind that when using pacman with that database, they should be together. Storing all the built packages to be included in the repository in one directory also allows to use shell glob expansion to add or update multiple packages at once:

 $ repo-add /path/to/repo.db.tar.zst /path/to/*.pkg.tar.zst

If you are looking to support multiple architectures, then precautions should be taken to prevent errors from occurring. Each architecture should have its own directory tree:

The repo-add executable checks whether the package is appropriate. If this is not the case, you will be running into error messages similar to this:

 ==> ERROR: '/home/archie/customrepo/arch/foo-arch.pkg.tar.zst' does not have a valid database archive extension.

repo-remove is used to remove packages from the package database, except that only package names are specified on the command line.

 $ repo-remove /path/to/repo.db.tar.zst pkgname

Once the local repository database has been created, add the repository to  of each system that is to use the repository. An example of a custom repository is in . The repository's name is the database filename with the file extension omitted. In the example above the repository's name simply is repo. Reference the repository's location using a  URL, or via HTTP using .

If willing, add the custom repository to the list of unofficial user repositories, so that the community can benefit from it.

## Network shared pacman cache
See Package proxy cache.

## Recreate a package from the file system
To recreate a package from the file system, use . Files from the system are taken as they are, hence any modifications will be present in the assembled package. Distributing the recreated package is therefore discouraged; see ABS and Arch Linux Archive for alternatives.

## List of installed packages
Keeping a list of all explicitly installed packages can be useful to backup a system or quicken the installation of a new one:

 $ pacman -Qqe > pkglist.txt

To keep an up-to-date list of explicitly installed packages (e.g. in combination with a versioned ), you can set up a hook. Example:

 [Trigger
 Operation = Install
 Operation = Remove
 Type = Package
 Target = *

 When = PostTransaction
 Exec = /bin/sh -c '/usr/bin/pacman -Qqe > /etc/pkglist.txt'

## Install packages from a list
To install packages from a previously saved list of packages, while not reinstalling previously installed packages that are already up-to-date, run:

 # pacman -S --needed - 's built-in file downloader, a separate application can also be used to download packages.

In all cases, make sure you have the latest pacman before doing any modifications.

 # pacman -Syu

## wget
This is very handy if you need more powerful proxy settings than pacmans built-in capabilities.

To use , first install the  package then modify  by uncommenting the following line in the  section:

 XferCommand = /usr/bin/wget --passive-ftp --show-progress -c -q -N %u

Instead of uncommenting the  parameters in , you can also modify the  configuration file directly (the system-wide file is , per user files are ).

## aria2
aria2 is a lightweight download utility with support for resumable and segmented HTTP/HTTPS and FTP downloads. aria2 allows for multiple and simultaneous HTTP/HTTPS and FTP connections to an Arch mirror, which should result in an increase in download speeds for both file and package retrieval.

Install , then edit  by adding the following line to the  section:

 XferCommand = /usr/bin/aria2c --allow-overwrite=true --continue=true --file-allocation=none --log-level=error --max-tries=2 --max-connection-per-server=2 --max-file-not-found=5 --min-split-size=5M --no-conf --remote-time=true --summary-interval=60 --timeout=5 --dir=/ --out %o %u

See  for used aria2c options.

* : The directory to store the downloaded file(s) as specified by pacman.
* : The output file name(s) of the downloaded file(s).
* : Variable which represents the local filename(s) as specified by pacman.
* : Variable which represents the download URL as specified by pacman.

## Other applications
There are other downloading applications that you can use with pacman. Here they are, and their associated XferCommand settings:

* :
* :
* :
* :  (please read the [https://github.com/huydx/hget documentation on the Github project page for more info)
* :  (please read the documentation on the project page for more info)

## Utilities
*
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
