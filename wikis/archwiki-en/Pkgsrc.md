# Pkgsrc

Pkgsrc is a cross-platform package manager.
It originates from NetBSD and it has support for GNU/Linux and many other UNIX-like operating systems.

## Installation
Next we will install Pkgsrc package manager.
First, you need to fetch the Pkgsrc tree.
There are a few ways we can do this, and the choice is yours.
# You can manually use CVS or Git to clone the Pkgsrc tree from source control.
# You can manually download a snapshot of the Pkgsrc tree, or
# You can install the  package from the AUR, which automatically fetches the latest quarterly snapshot of the Pkgsrc tree.

If you lack root rights on the system you use, you may wish to use an alternative method to fetch the Pkgsrc tree and do an unprivileged bootstrap of Pkgsrc under your home directory.
Please refer to the official Pkgsrc documentation for details on how to do an unprivileged installation.

Instead, we are here going to choose to use the relevant package from the AUR, which requires root rights.

## Installing Pkgsrc
First install the  package from the AUR.
After the package is installed, you need to follow the instructions that were printed by makepkg utility.
In short, you need to do the following steps as root user to bootstrap Pkgsrc.

We need to first navigate to the directory that contains the Pkgsrc tree.
 # cd /usr/pkgsrc/bootstrap
Then we will remove the leftover files from the previous version of the Pkgsrc bootstrap (if they exists).
 # rm -ri work
Finally, we will bootstrap the Pkgsrc by running the script as root user. This will install binaries and other required files under  prefix. Note that the Pkgsrc package definitions are located under  directory.
 # ./bootstrap --prefix /usr/pkg

After the bootstrap script was executed successfully, you should make sure that the Pkgsrc's  and  directories are added to your PATH environment variable. The AUR package should do this automatically. But to have the changes take effect immediately, you may need to reopen your terminal or re-login to your TTY session (sourcing  should also help).

## Installing packages with Pkgsrc
Let's use the  package as an example.
We need to first navigate to the directory that contains the Pkgsrc tree.
 # cd /usr/pkgsrc

Next we will find the directory that contains the desired package.
 # cd shells/tcsh

Then We will execute the install target of the makefile as root user.
 # bmake install

Now tcsh should be installed from Pkgsrc, and the program may be used normally.

## Uninstall Pkgsrc
To uninstall Pkgsrc, you can simply uninstall the AUR package.
To remove the binaries that you have installed with Pkgsrc package manager, you need to manually remove the  directory as well.
