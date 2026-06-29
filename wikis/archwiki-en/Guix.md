# Guix

GNU Guix is a package manager that offers transactional, reproducible, per-user package management.

While Guix can be used stand-alone and provide a full GNU distribution and a kernel by itself, you can install the Guix package manager on top of Arch Linux to make Guix available to users while using a more traditional and mature Unix-like system as a base.

See the Guix manual for information on what per-user packaging commands Guix makes available to users.

## Installation
On Arch Linux you can install Guix either using the AUR or manually as described in the Guix Manual.
Installing using the AUR has the advantage that pacman is aware of the package and the extra files in the  file tree. But contrarily to other AUR packages, uninstalling the package does not unwind the entire Guix installation.
Since Guix is a package manager by itself and it can also update itself, you still have to manually uninstall the files installed via Guix (no matter whether you installed the AUR package or the manual installation).
Therefore, after updating Guix once, the AUR advantage really turns into a disadvantage, as there will be many unnecessary files in the  file tree that are part of the Guix AUR package but that are never used by Guix anymore.
Therefore, consider using the manual installation.

## Manual Installation
For the manual installation, see chapter Installation of the Guix manual.
The easiest way is to use the shell installer script linked in there. The installer can also be installed from the AUR as .

As of December 2021 this script installs files into the following locations:
* ,  (the Guix store)
* , , (only symlinks)
*  (a symlink to the current profile)
* , (keys for substitute servers)
* , (sets environment variables to put the current Guix profile first in the PATH)
* , ,  (shell completions for Bash, Zsh, and Fish)

Furthermore it installs and enables a systemd service called , and creates users  ...  and a group .

Now start a new login shell (alternatively reboot your machine) and you can start using Guix:

 $ guix install glibc-locales

## AUR Package Installation
GNU Guix is available in the AUR as . As described in the , the PGP key by the Guix distributor will need to be added first.

Guix makes builds more reproducible by running the build process using an unprivileged build user account. Therefore if you want to be able to build  packages simultaneously (e.g. for serving multiple users at the same time) you should create  build user accounts. as Guix should be able to build simultaneously. The following command does this the way described in the Guix manual:

 # groupadd --system guixbuild
 # uncomment and type e.g.  10  for   n below  -->  have ten users
 # for i in `seq -w 1 n`;
   do
     useradd -g guixbuild -G guixbuild           \
             -d /var/empty -s `which nologin`    \
             -c "Guix build user $i" --system    \
             guixbuilder$i;
   done

Enable/start .

You may want to authorize Guix to download and use binary packages (‘substitutes’) from the Guix Official Substitute Server:

 # guix archive --authorize < /usr/share/guix/ci.guix.gnu.org.pub

## Building packages outside of /tmp
The unit file may need to be extended to use a different  for building if  does not provide enough space (see the Guix manual for details). To use  for building instead of , edit  to add the following lines:

## Uninstalling Guix
Stop and disable  and if necessary .
If you installed Guix as an AUR package, then remove Guix using pacman.

Remove , , , and  if existent.

Now remove all the Guix build users and their group:

 # for i in `seq -w 1 n`; do userdel guixbuilder$i; done
 # groupdel guixbuild

Then remove the Guix store  as well as  and .
Remove stale symlinks in  and .
Also remove  and the shell completion files specific to Guix.
