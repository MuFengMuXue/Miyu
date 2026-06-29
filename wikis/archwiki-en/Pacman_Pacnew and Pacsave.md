# Pacman/Pacnew and Pacsave

When pacman removes a package that has a configuration file, it normally creates a backup copy of that configuration file and appends .pacsave to the name of the file. Likewise, when pacman upgrades a package which includes a new configuration file created by the maintainer differing from the currently installed file, it saves a .pacnew file with the new configuration. pacman provides notice when these files are written.

## Why these files are created
A .pacnew file may be created during a package upgrade (,  or ) to avoid overwriting a file which already exists and was previously modified by the user. When this happens, a message like the following will appear in the output of pacman:

 warning: /etc/pam.d/usermod installed as /etc/pam.d/usermod.pacnew

A .pacsave file may be created during a package removal (), or by a package upgrade (the package must be removed first). When the pacman database has a record that a certain file owned by the package should be backed up, it will create a .pacsave file. When this happens pacman outputs a message like the following:

 warning: /etc/pam.d/usermod saved as /etc/pam.d/usermod.pacsave

These files require manual intervention from the user and it is good practice to handle them right after every package upgrade or removal. If left unhandled, improper configurations can result in improper function of the software or the software being unable to run altogether.

## Package backup files
A package's PKGBUILD file specifies which files should be preserved or backed up when the package is upgraded or removed. For example, the PKGBUILD for  contains the following line:

 backup=(etc/pulse/{daemon.conf,default.pa,system.pa})

After installation, this list can be queried from the pacman database using .

To prevent any package from overwriting a certain file, see Pacman#Skip file from being upgraded.

## Types explained
## .pacnew
For each of the #Package backup files being upgraded, pacman cross-compares three md5sums generated from the file's contents: one sum for the version originally installed by the package, one for the version currently in the filesystem, and one for the version in the new package. If the version of the file currently in the filesystem has been modified from the version originally installed by the package, pacman cannot know how to merge those changes with the new version of the file. Therefore, instead of overwriting the modified file when upgrading, pacman saves the new version with a .pacnew extension and leaves the modified version untouched.

Going into further detail, the 3-way MD5 sum comparison results in one of the following outcomes:

; original = X, current = X, new = X : All three versions of the file have identical contents, so overwriting is not a problem. Overwrite the current version with the new version and do not notify the user (although the file contents are the same, this overwrite will update the filesystem's information regarding the file's installed, modified, and accessed times, as well as ensure that any file permission changes are applied).

; original = X, current = X, new = Y : The current version's contents are identical to the original's, but the new version is different. Since the user has not modified the current version and the new version may contain improvements or bugfixes, overwrite the current version with the new version and do not notify the user. This is the only auto-merging of new changes that pacman is capable of performing.

; original = X, current = Y, new = X : The original package and the new package both contain exactly the same version of the file, but the version currently in the filesystem has been modified. Leave the current version in place and discard the new version without notifying the user.

; original = X, current = Y, new = Y : The new version is identical to the current version. Overwrite the current version with the new version and do not notify the user (although the file contents are the same, this overwrite will update the filesystem's information regarding the file's installed, modified, and accessed times, as well as ensure that any file permission changes are applied).

; original = X, current = Y, new = Z : All three versions are different, so leave the current version in place, install the new version with a .pacnew extension and warn the user about the new version. The user will be expected to manually merge any changes necessary from the new version into the current version.

Rarely, when an upgraded package includes a backup file the previous version did not, the situation is correctly handled as X/Y/Y or X/Y/Z, with X being a non-existant value.

## .pacsave
If the user has modified one of the files specified in  then that file will be renamed with a .pacsave extension and will remain in the filesystem after the rest of the package is removed.

## Locating .pac* files
Pacman does not deal with .pacnew files automatically: you must maintain these yourself. A few tools are presented in the next section. To do this manually, you will first need to locate them. When upgrading or removing a large number of packages, updated .pac* files may be missed. To discover whether any .pac* files have been installed, use one of the following:

* To search within  where most global configurations are stored:  or to search within the entire disk replacing  by  in the command above (in which case you may want to selectively skip certain directories to speed up the search).
* If installed, locate can also be used. First re-index the database:  Then run:
* Use pacman's log to find them:  Note that the log does not keep track of the files currently in the filesystem nor the ones that have already been removed; the above command will list all .pac* files that have ever existed on your system. In order to only get the 10 most recent .pac* files, pipe the result to .

## Managing .pac* files
## pacdiff
 provides the simple  tool for managing .pac* files.

It will search for .pacnew, .pacsave and .pacorig files, and will then prompt to take action upon them.

It uses  by default, to search using the  array information from currently installed packages. If this is not sufficient for your use case, you can specify  or  instead, for a more thorough search.

It uses vimdiff by default, but you may specify a different tool with . See List of applications/Utilities#Comparison, diff, merge for other common comparison tools.

## Third-party utilities
A few third-party utilities providing various levels of automation for these tasks are available:

*
*
*
*
*
*
