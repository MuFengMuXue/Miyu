# Pacman/Package signing

To determine if packages are authentic, pacman uses OpenPGP keys in a web of trust model. The current Master Signing Keys are found here. At least three of these Master Signing Keys are used to sign the Developers' and Package Maintainers' own keys. They are then used to sign their packages. Each user also has a unique OpenPGP key, which is generated when you configure . It is this web of trust that links the user's key to the master keys.

Examples of webs of trust:

* Custom packages: Packages made and signed with a local key.
* Unofficial packages: Packages made and signed by a developer. Then, a local key was used to sign the developer's key.
* Official packages: Packages made and signed by a developer. The developer's key was signed by the Arch Linux master keys. You used your key to sign the master keys, and you trust them to vouch for developers.

## Setup
## Configuring pacman
The  option in  determines the level of trust required to install a package with . For a detailed explanation of , see , and the file comments. One can set signature checking globally, or per repository. If  is set globally in the  section, all packages installed with  will require signing. With the  setting from the default , any packages you build, and install with , will not need to be signed using makepkg.

For remote packages, the default configuration will only support the installation of packages signed by trusted keys:

 is a default compiled-in pacman parameter. The default configuration is identical to using the global option of:

 SigLevel = Required DatabaseOptional TrustedOnly

The above can be achieved too on a repository level further below in the configuration, e.g.:

 SigLevel = PackageRequired
 Include = /etc/pacman.d/mirrorlist

explicitly adds signature checking for the packages of the repository, but does not require the database to be signed.  here would turn off a global  for this repository.

## Initializing the keyring
To initialize the pacman keyring run:

 # pacman-key --init

## Managing the keyring
## Verifying the master keys
The initial setup of keys is achieved using:

 # pacman-key --populate

Take time to verify the [https://archlinux.org/master-keys/ Master Signing Keys when prompted as these are used to co-sign (and therefore trust) all other packager's keys.

OpenPGP keys are too large (2048 bits or more) for humans to work with, so they are usually hashed to create a 40-hex-digit fingerprint which can be used to check by hand that two keys are the same. The last eight digits of the fingerprint serve as a name for the key known as the '(short) key ID' (the last sixteen digits of the fingerprint would be the 'long key ID').

## Adding developer keys
The official Developers' and Package Maintainers' keys are signed by the master keys, so you do not need to use pacman-key to sign them yourself. Whenever pacman encounters a key it does not recognize, it will prompt you to download it from a  configured in  (or by using the  option on the command line). Wikipedia maintains a list of keyservers.

Once you have downloaded a developer key, you will not have to download it again, and it can be used to verify any other packages signed by that developer.

## Adding unofficial keys
This method can be utilized to add a key to the pacman keyring, or to enable signed unofficial user repositories.

First, get the key ID () from its owner. Then add it to the keyring using one of the two methods:

# If the key is found on a keyserver, import it with:
# If otherwise a link to a keyfile is provided, download it and then run:

It is recommended to verify the fingerprint, as with any master key or any other key you are going to sign:

 $ pacman-key --finger keyid

Finally, you must locally sign the imported key:

 # pacman-key --lsign-key keyid

You now trust this key to sign packages.

## Debugging with gpg
For debugging purposes, you can access pacmans keyring directly with gpg, e.g.:

 # gpg --homedir /etc/pacman.d/gnupg --list-keys

## Tips and tricks
## Upgrade system regularly
Upgrading the system regularly via pacman#Upgrading packages prevents most signing errors. If delay is unavoidable and system upgrade gets delayed for an extended period, manually sync the package database and upgrade the  package before system upgrade:

 # pacman -Sy --needed archlinux-keyring && pacman -Su

This command is not considered a partial upgrade since it syncs the package database and upgrades the keyring package first. Both must be processed just before starting system upgrade to ensure signatures of all upgraded packages can be properly verified.

## Update system time regularly
When the system time is faulty, signing keys could be considered expired (or invalid) and signature checks on packages will fail. Synchronize the system clock regularly by using the Network Time Protocol daemon.

## Troubleshooting
## Invalid signature errors
pacman-key depends on system time. If your system clock is not synchronized, system installation/upgrade may fail with:

 error: PackageName: signature from "User " is invalid
 error: failed to commit transaction (invalid or corrupted package (PGP signature))
 Errors occurred, no packages were upgraded.

If using ntpd, correct the system time (as root) with  followed by .

Other NTP clients can be used. See time synchronization.

If correction of the system clock does not resolve the failure, try one of the following approaches:

## Removing packages from cache
Some packages could be corrupted or may be unsigned, causing failure. Remove each offending package from the system cache  so it gets freshly downloaded, or clear the entire cache.

## Resetting all the keys
Remove or reset all the keys installed in your system by removing the  directory (as root) and by rerunning  followed by  to re-add the default keys.

## Disabling signature checking
If you are not concerned about package signing, you can disable OpenPGP signature checking completely. Edit  to have the following lines under :

 SigLevel = Never
 #LocalFileSigLevel = Optional
 #RemoteFileSigLevel = Required

You need to comment out any repository-specific  settings because they override the global settings. This will result in no signature checking, which was the behavior before pacman 4. If you do this, you do not need to set up a keyring with pacman-key. You can change those options later if you decide to enable package verification.

## Cannot import keys
There are multiple possible sources of this problem:

* An outdated  package.
* The clock being set to an incorrect date.
* Your ISP blocked the port used to import OpenPGP keys.
* Your pacman cache contains copies of unsigned packages from previous attempts.
*  is not correctly configured.

You might be stuck because of an outdated  package when doing an upgrade synchronization.

Below are a few solutions that could work depending on your case.

## Upgrade the system
See if upgrading the system can fix it first.

## Change keyserver
If you suspect that something is not working right with the keyserver, you could try to switch to the Ubuntu keyserver. To do this, edit  and change the  line to:

 keyserver hkp://keyserver.ubuntu.com

## Clean cached packages
If you suspect that your pacman cache at  might contain unsigned packages, try cleaning the cache manually or run:

 # pacman -Sc

which removes all cached packages that have not been installed.

## Signature is unknown trust
Sometimes when running  you might encounter this error:

 error: package-name: signature from "packager" is unknown trust

This occurs because the 's key used in the package  is not present and/or not trusted in the local pacman-key gpg database.

This can occur when:

* a new packager recently got their key signed, pushes a package, but your keyring does not contain their key yet,
* a key has expired since it was added to your keychain,
* a new master key is introduced to replace a previous one (usually when a master key holder resigns).

Pacman has built-in mechanisms to handle the first two cases. For an unkown key, pacman will attempt to import the key using WKD first; if it fails, pacman goes back to the old keyserver infrastructure (which will probably fail too). Since version 7.1, pacman will automatically refresh known keys from WKD and keyservers when it encounters an expired key.If you encounter the error, mitigate by:

* manually upgrading the archlinux-keyring package prior to the system upgrade, or
* refreshing your keys with , or
* resetting all the keys.

The last two options at your disposal break the chain of trust, and should not be used:

* manually signing the untrusted key locally, or
* setting temporarily  to .

## Updating keys via proxy
In order to use a proxy when updating keys the  option must be set in both  and . See GnuPG#Use a keyserver for more information.

## GPGME error: No data
if you running  and encounter this error:

 error: GPGME error: No data
 error: failed to synchronize all databases (invalid or corrupted database (PGP signature))

Or having download issue via HTTPS. This is because your network needs
authentication. The pacman's request will be redericted to the login page,
causing it downloading the wrong file.

Solution: first switch to a new network, then peform

 rm /var/lib/pacman/sync/*.sig

and try   again.
