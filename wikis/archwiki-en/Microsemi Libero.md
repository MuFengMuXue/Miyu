# Microsemi Libero

From Microsemi's website:
: Libero® SoC Design Suite offers high productivity with its comprehensive, easy-to-learn, easy-to-adopt development tools for designing with Microsemi's PolarFire, IGLOO2, SmartFusion2, RTG4, SmartFusion, IGLOO, ProASIC3 and Fusion families.

This article shows how to install the Microsemi Libero FPGA Design Toolchain on Arch Linux.

## Installation
## Preparations
Libero needs about 45GiB free diskspace. The size of the disk where Libero is installed must not exceed 2TB!

## Package installation
Libero depends on some 32-bit packages from multilib. You need to enable the multilib repository if not already done.

Install the following packages:

The License Manager binaries also need package  (as of lmgrd v11.16.6.0)

## Qt5 32-bit dependencies
Parts of Liberos shared libraries also depend on 32-bit Qt5 libraries, namely , ,  and . Sadly they are not available from the multilib repository so we have to add them manually.

Download the 32-bit installer of Qt at Qt 32-bit online installer, make it executable and run it:

 $ ./qt-unified-linux-x86-2.0.5-2-online.run

It should be sufficient to install "Qt 5.5" -> "Desktop gcc".
Set a sane installation path e.g.  where user is your username.

## Extract files
The Installer unpacks its own Java Runtime and by default uses  for temporary files even if it tells you differently. Thus make sure you have enough space available on ! The default size of half the total system memory tmpfs is usually not sufficient for the installation, you have to disable it for installation and reboot the system to apply the change:

From https://www.microsemi.com/product-directory/design-resources/1750-libero-soc#downloads download the "Libero SoC v12.1 for Linux" install file (You need to create an account for that).
Make it executable and run it:

 $ ./Libero_SoC_v12.1_lin.bin -i console

In the installer answer the questions and set a path to extract the files to, e.g.  and .
There is a graphical installer available, just replace  with  in the call above.

## Silent installation
You can also pass the installation parameters to the script on the commandline rather than typing them in. Following an example for a default installation:
 $ ./Libero_SoC_v12.1_lin.bin -i silent \
    -DUSER_INSTALL_DIR=/home/user/programs/microsemi/libero/v12.1/ \
    -DUSER_COMMON_DIR=/home/user/programs/microsemi/common \
    -DCHOSEN_FEATURE_LIST=Synplify,ModelSim,ModelsimPro,Identify,Libero \
    -DCHOSEN_INSTALL_FEATURE_LIST=Synplify,ModelSim,ModelsimPro,Identify,Libero \
    -DCHOSEN_INSTALL_SET=Libero

## Post-Installation
Reenable the tmpfs after the installation and reboot.

Some modifications have to be made for Libero to run on Arch Linux.

Libero tries to load an old version of the motif library. Modify the following files and change the 3 to a 4 in the  block:

Furthermore the outdated  version shipped by Microsemi does not work with the repository version of .
In  do the following to make Libero use your library installed by pacman:
 $ mv libz.so.1 libz.so.1.old
 $ ln -s /lib/libz.so libz.so.1
Repeat the same two commands in  to enable the FlashPro utilities.

By mistake the installer adds double quotes around the common path when defining the vault location. Thus Libero will create a folder called  in the working directory when it is called. To change that either manually edit the file  to remove the double quotes from the line where  is defined:

... or run the commands below to remove the quotes:
 $ cd /home/user/programs/microsemi/libero/v12.1/Libero/data
 $ sed 's/"//g' install.def > tmp.def
 $ cp tmp.def install.def
 $ rm tmp.def

## Launching Libero
When launching Libero some environment variables have to be set.
 LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/user/lib/qt5_32/5.5/gcc/lib
 LM_LICENSE_FILE="port@domain.of.your.license.server"
 SNPSLMD_LICENSE_FILE="port@domain.of.synopsys.license.server"
The  has to include the libraries from the 32-bit Qt installation,  reflects your Libero license server on which the license daemon runs on some port under some url domain.of.your.license.server.  is needed for the Synopsys tools used in Libero, set this to a different server and port if you have multiple license daemons running or to  if not.

With those variabled set Libero is ready to be launched with
 $ /home/user/programs/microsemi/libero/v12.1/Libero/bin/libero

You may want to create a launch script for that:

Do not forget to make it executable.

## Application menu entry
A freedesktop.org application menu entry (which a lot of desktop environments and window managers follow) can be added to the system by creating a  file in your  directory:

## Using a FlashPro programmer
Using a programmer (e.g. the Microsemi FlashPro5) requires two steps: Adding rules to gain device permissions and unloading a conflicting kernel module.

## Adding udev rules
To add the correct permissions for your user to access the programmer add the following file to your Udev ruleset as root:

{{hc|/etc/udev/rules.d/70-microsemi.rules|2=
SUBSYSTEM=="usb", ATTR{idVendor}=="1514", ATTR{idProduct}=="2008", MODE="0666", GROUP="microsemi-prog"
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6001", MODE="0666", GROUP="microsemi-prog"
}}

The group  is just an example, you may replace it by any group your user is in or add a new group and put your user into it with usermod.

You have to log out and in to apply the new group for the session. In a single terminal some can also apply the new group with . To list your groups type  or .

## Removing conflicting kernel module
When plugging in the programmer it identifies as an FTDI serial device and loads the corresponding kernel driver. Liberos software does not work with that kernel driver so we have to unload it:
 # rmmod ftdi_sio

To permanently unload the driver you may add it to your Blacklist:

## Troubleshooting
## Libero crashes with SysXceptError
Libero till version 12.1 does not work on disks larger than 2TB of size. Neither the Libero binaries nor the vault nor your home-folder nor any project may reside on a partition larger than that size. If you cannot change the size of the partition where your home-folder is located start Libero with a different path for your home on a smaller disk:
 $ HOME=/path/to/fake/home libero
Some may add that to the startup-script to apply it on start.
The install and vault locations have to be set on installation or may be edited in  when moving the files afterwards.
