# Downgrading packages

Before downgrading a single or multiple packages, consider why you wish to do so. If it is due to a bug, follow the bug reporting guidelines. I.e. search the Arch Linux Bugtracker for existing tasks and if there is none, add a new task. It is better to correct bugs, or at least warn other users of possible issues.

## Return to an earlier package version
## Using the pacman cache
If a package was installed at an earlier stage, and the pacman cache was not cleaned, install an earlier version from .

This process will remove the current package and install the older version. Dependency changes will be handled, but pacman will not handle version conflicts. If a library or other package needs to be downgraded with the packages, please be aware that you will have to downgrade this package yourself as well.

 # pacman -U file:///var/cache/pacman/pkg/package-old_version.pkg.tar.zst

Once the package is reverted and confirmed to work, to make  temporarily ignore updates, add the package to the IgnorePkg section of , until the difficulty with the updated package is resolved.

## Downgrading the kernel
In case of issue with a new kernel, the Linux packages can be downgraded to the last working ones #Using the pacman cache. Go into the directory  and downgrade at least ,  and any kernel modules. For example:

 # pacman -U file://linux-6.16.1.arch1-1-x86_64.pkg.tar.zst file://linux-headers-6.16-1-x86_64.pkg.tar.zst file://virtualbox-host-modules-arch-7.2.0-2-x86_64.pkg.tar.zst

## Arch Linux Archive
The Arch Linux Archive is a daily snapshot of the official repositories. It can be used to install a previous package version, or restore the system to an earlier date.

## Rebuild the package
If the package is unavailable, find the correct PKGBUILD and rebuild it with makepkg.

For packages from the official repositories, retrieve the PKGBUILD with ABS and change the software version. Alternatively, find the package on the Packages website, click "View Changes", and navigate to the desired version. The necessary files can then be downloaded from the directory so that the package can be rebuilt.

See also Arch build system#Using the pkgctl tool.

Old AUR packages can be built by checking out an old commit in the AUR package Git repository. For pre-2015 AUR3 PKGBUILDs, see Arch User Repository#Git repositories for AUR3 packages.

## Automation
*
*

## Return from testing
See Official repositories#Disabling testing repositories.
