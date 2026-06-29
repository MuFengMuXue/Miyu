# Offline installation

This article provides instructions on installing Arch Linux on a system without an Internet connection. To do this, another system with a working Internet connection is required.

First, follow the Installation guide, skipping the steps requiring an internet connection (e.g. Installation guide#Connect to the internet), then continue with this guide instead of following Installation guide#Install essential packages.

## Prepare local repository
Follow Pacman/Tips and tricks#Installing packages from a CD/DVD or USB stick for instructions on preparing a local repository with the necessary files on a separate host installation.

At the very least, for a functioning system, the following packages are recommended:

 # mkdir /tmp/blankdb
 # pacman -Syw --cachedir $PWD --dbpath /tmp/blankdb base linux linux-firmware

Create your custom offline repository:

 # repo-add ./custom.db.tar.zst ./*== Mount and configure ==

Once the repository is prepared, connect the external media to the new installation, and mount it on the newly created root filesystem:

 # mount --mkdir /dev/sdxy /mnt/repo

Edit your archiso  and add a new section:

Comment out  and  so that pacman does not fail on the default repositories.

## Pacstrap
By default, [http://Pacman/Package_signing#Initializing_the_keyring pacman's keyring is initialized in the live session only once NTP is activated (https://bbs.archlinux.org/viewtopic.php?id=283075).
In case NTP cannot be activated (e.g. you don't have internet access), you need to manually run

 pacman-key --init
 pacman-key --populate

After this, you can continue to pacstrap your locally-available packages to the new installation:

 # pacstrap -K /mnt base linux linux-firmware

## Offline installation of packages
## Install from file
In case the offline installation process was only temporary, but requires manual installation of some packages before being able to access a network, see pacman#Additional commands to learn how to install local packages.

Shell globbing can be used to install many packages at once:

 # pacman -U /package/folder/*.tar.zst

## Offline cache
You can put the required files into  and , so as to make  think it has everything it needs to do searches, updates, and installs. The following method is based on two forum threads: The steps are:

# downloading the up to date package databases on a computer with internet access,
# transferring them to the offline computer,
# generating the list of packages required from the offline computer to update it,
# downloading them with their signature on a computer with internet access,
# transferring them to the pacman cache of the offline computer,
# installing the updates.

The following script will download the updated package databases. If needed, change  to any mirror from the [https://archlinux.org/mirrors/status/ mirror status list.

{{hc|download_databases.sh|2=
#!/bin/sh

ARCH="x86_64"
MIRROR="https://mirrors.kernel.org/archlinux/"

wget "${MIRROR}/core/os/${ARCH}/core.db"
wget "${MIRROR}/extra/os/${ARCH}/extra.db"
wget "${MIRROR}/multilib/os/${ARCH}/multilib.db"

# and possibly -uncomment- (if customized in /etc/pacman.conf or pacman.conf.d):

#wget "${MIRROR}/core-testing/os/${ARCH}/core-testing.db"
#wget "${MIRROR}/extra-testing/os/${ARCH}/extra-testing.db"
#wget "${MIRROR}/multilib-testing/os/${ARCH}/multilib-testing.db"

# and -additionally- debug and staging packages.
}}

Make the script executable and run it. You will obtain multiple .db files.

The following steps will be transferring the .db files to the offline PC, making it so you are working with up-to-date package lists (as if you ran ), then generating a list of package required for the update:

 # cp *.db /var/lib/pacman/sync/
 # pacman -Sup --noconfirm > pkglist

You will also need to download the corresponding package signatures, so prepare the list of signatures to download:

 # sed -e 's/\.zst$/.zst.sig/' ../pkglist > ../siglist

Next, bring the two lists with you to a place where you have internet and download the listed packages in an empty directory:

 # wget -nv -i ../pkglist
 # wget -nv -i ../siglist

Take all the  and  files back home, put them in  and finally run:

 # pacman -Su

## Local repository
In case the new system is expected to remain offline or airgapped, it should be configured to expect only local repositories.

## Complete repository
After chrooting into your new installation, edit the new  in the same way as previously (but without the  prefix):

Comment out all other repositories and save. Continue configuring the new system as usual.

From now on any updates to the offline system can be made by bringing an up to date copy of the local repository, mounting it to  and running pacman commands as usual.
