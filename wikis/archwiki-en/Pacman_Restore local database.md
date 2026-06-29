# Pacman/Restore local database

## Symptoms
The local pacman database may need to be restored if:

*  produces no output, while  incorrectly reports that the system is up to date.
* Installing a package with  lists already satisfied dependencies instead of proceeding.

This usually indicates corruption or deletion of .

## Prerequisites
Check if the pacman log file is present:

 $ ls /var/log/pacman.log

If the log file does not exist, this method cannot be used.
Alternatives:
* Xyne's package detection script (may help reconstruct the package list).
* Full system reinstallation, if no other recovery is possible.

## Generating the recovery list
Install  to access .

## Create the recovery script
Save the following script as  and make it executable:

{{hc|pacrecover|
#!/bin/bash -e

# load configuration settings from the makepkg configuration file
. /etc/makepkg.conf

# determine the cache directory from pacman configuration, defaulting to /var/cache/pacman/pkg, remove prefix with sed
PKGCACHE=$( (grep -m 1 '^CacheDir' /etc/pacman.conf || echo 'CacheDir = /var/cache/pacman/pkg') | sed 's/CacheDir = //')

# define directories to search for package files
pkgdirs=("$@" "$PKGDEST" "$PKGCACHE")

# read package name and version from input and construct a search pattern for package files
while read -r -a parampart; do

        # loop through each directory to search for matching package files
        for pkgdir in "${pkgdirsdo

                # check each file matching the pattern in the current directory
                 for i in "$pkgdir"/"${parampart[0}"-"${parampartdo

                        # if a file exists, print its path and stop checking further
                        [ -f "${i}"  && { echo "${i}" ; break; }
                done

                # If no file is found, output the package name to stderr
        done || echo "${parampart0}" 1>&2
done
}}

## Generate package lists
Run:

 $ paclog-pkglist /var/log/pacman.log | ./pacrecover >files.list 2>pkglist.orig

*  – paths to locally available packages.
*  – packages missing from cache (must be downloaded).

Later operation may result in mismatch between files of older versions of package, still present on machine, and files, found in new version. Such mismatches will have to be fixed manually.

Restrict the second list to packages present in repositories:

 $ { cat pkglist.orig; pacman -Slq; } | sort | uniq -d > pkglist

Ensure that base packages are included:

 $ comm -23 > pkglist

Proceed once the contents of both lists are satisfactory, since they will be used to restore pacman's installed package database; .

## Performing the recovery
Define a helper function:

{{hc|recovery-pacman|
recovery-pacman() {
    pacman "$@" \
    --log /dev/null \
    --noscriptlet \
    --dbonly \
    --overwrite "*" \
    --nodeps \
    --needed
}
}}

Option meanings:
* : avoids polluting the log.
* : skips already installed packages.
* : allows installation of cached packages with outdated dependencies.
* , , : restrict pacman to database reconstruction only.

## Steps
# Update sync databases:
# Install locally available packages:
# Install remaining packages from repositories:
# Recreate explicit/implicit install status:
# (Optional) Verify installation:
# (Optional) Identify unowned files: See Pacman/Tips and tricks#Identify files not owned by any package.
# Update all packages:
