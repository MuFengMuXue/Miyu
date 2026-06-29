+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                                                                                                                                                                                                                                                | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** This is page need to be updated, and legacy users need to use FREE drivers. [Oguzkagan](//wiki.manjaro.org/index.php?title=User:Oguzkagan&action=edit&redlink=1 "User:Oguzkagan (page does not exist)") ([talk](//wiki.manjaro.org/index.php?title=User_talk:Oguzkagan "User talk:Oguzkagan")) ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Catalyst_(Obsolete_-_remove%3F) "Talk:Catalyst (Obsolete - remove?)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
Owners of **ATI/AMD** video cards have a choice between AMD\'s proprietary driver (catalyst) and the [open source driver](//wiki.manjaro.org/index.php?title=ATI&action=edit&redlink=1 "ATI (page does not exist)") (xf86-video-ati). This article covers the proprietary driver.

AMD\'s Linux driver package *catalyst* was previously named *fglrx* (**F**ire**GL** and **R**adeon **X**). Only the package name has changed, while the kernel module retains its original *fglrx.ko* filename. Therefore, any mention of fglrx below is specifically in reference to the *kernel module*, **not the package**.

As of August 2012, binary packages are being offered. Currently, packages are available in the \[basis\] repository. In the past, Catalyst_legacy [has been dropped](http://manjaro.org/2013/03/20/stable-repositories-got-updated-10/) from official Manjaro support because of incomaptiblility with Xorg-Server 1.13-Series. We had to [remove both proprietary drivers](http://forum.manjaro.org/index.php?topic=2898.0) for a short term due change to Xorg-Server 1.14-Series.

## Contents

-   [[1] [Steps to restore free ATI driver]](#Steps_to_restore_free_ATI_driver)
-   [[2] [Prepare the System for Catalyst Drivers]](#Prepare_the_System_for_Catalyst_Drivers)
-   [[3] [Install Catalyst Driver]](#Install_Catalyst_Driver)
-   [[4] [Catalyst / Intel Hybrid Driver]](#Catalyst_.2F_Intel_Hybrid_Driver)
-   [[5] [Troubleshoot]](#Troubleshoot)
    -   [[5.1] [conflicting dependencies]](#conflicting_dependencies)

# [Steps to restore free ATI driver]

1/ Fire up a package manager, search for \"catalyst\" and remove all installed packages starting with it. Also remove \"lxdm\"

2/ Put these in a terminal

    sudo mhwd -i pci video-ati
    sudo pacman -S lxdm xfce4-session

-   This will also reinstall xorg-server. If you can\'t find xorg-server installed, you will have to manually install it before restarting the system. Also replace xfce4-session with your desktop session.

# [Prepare the System for Catalyst Drivers]

It will be necessary to update your system in order to prepare it to use Catalyst drivers. To do so, enter the following command into the terminal:

    sudo pacman -Syyuu mhwd-db-catalyst

\
Once complete, a Catalyst driver can now be installed.

\

# [Install Catalyst Driver]

All the preparations complete, enter the following command in the terminal to automatically detect and install the appropriate Catalyst driver:

    sudo mhwd -a pci nonfree 0300

Following the installation, reboot your system for the changes to take effect.

\

# [][Catalyst / Intel Hybrid Driver]

This method describes installing the non-free catalyst driver with full switching support for Intel chipsets. Currently there is an issue with Xorg 1.14 which prevents X from loading. Here is a workaround I discovered. Confirmed working for AMD 7970m / Intel HD 4000.

\

    sudo pacman -Syyuu

Remove conflicting packages. At this time it is because of the Xorg 1.14 not being properly supported/

    sudo pacman -R xf86-video-intel xf86-video-nouveau xf86-video-ati xorg-server

Install catalyst 13.4.X

    sudo mhwd -i pci video-catalyst

Install fix for running Intel driver and switchable catalyst from the AUR.

    sudo pacman -S base-devel yaourt

    yaourt catalyst-total-pxp
    mhwd-gpu --setgl catalyst

Additional dependencies

    sudo pacman -S qt opencl-headers linux-headers

A bug fix, workaround.

    sudo systemctl enable temp-links-catalyst

Setting up initial configs

    sudo aticonfig --initial -f

Switch to discrete GPU (AMD card)

    sudo aticonfig --px-dgpu

Alternatively, for the Intel card use.

    sudo aticonfig --px-igpu

# [Troubleshoot]

## [conflicting dependencies]

**Error**

------------------------------------------------------------------------

failed to prepare transaction (conflicting dependencies)

xf86-video-ati and catalyst-server are in conflict (xorg-server\<1.14.0)

Not all free drivers are supported by Catalyst-Server. Please uninstall any free drivers with:

     sudo mhwd -r pci video-ati

You may need to remove some packages with pacman:

     sudo pacman -Rs