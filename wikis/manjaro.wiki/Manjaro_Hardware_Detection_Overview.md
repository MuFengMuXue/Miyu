Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro_Hardware_Detection_Overview/ru "Обзор Manjaro HardWare Detection (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [mhwd]](#mhwd)
    -   [[2.1] [mhwd Commands]](#mhwd_Commands)
        -   [[2.1.1] [Listing Hardware Information]](#Listing_Hardware_Information)
        -   [[2.1.2] [Listing Installed Driver Information]](#Listing_Installed_Driver_Information)
        -   [[2.1.3] [Listing Available Drivers]](#Listing_Available_Drivers)
-   [[3] [See also]](#See_also)

# [Overview]

[![Mhwd.png](/images/a/a4/Mhwd.png)](//wiki.manjaro.org/index.php?title=File:Mhwd.png)

The **M**anjaro **H**ard**W**are **D**etection (mhwd) command is a unique feature of Manjaro. There are currently two types of mhwd command:

**1. mhwd:** Enables the automatic detection and configuration of computer hardware the system is running on. This includes both hardware connected internally via **[PCI](http://en.wikipedia.org/wiki/Conventional_PCI)** (e.g. graphics cards), and connected externally via **[USB](http://en.wikipedia.org/wiki/USB)** (e.g. flashdrives). **Note:** The mhwd command is still *under development*, and at present is only able to install drivers for graphics cards connected internally via pci.

**2. mhwd-kernel:** Enables the installation and easy management of *multiple* kernels on your system.\

# [mhwd]

Run automatically during the installation process, it allows for Manjaro to work fully on your system \'straight out of the box\', without the need to manually identify and install the necessary drivers or to manually edit the appropriate configuration files. Also usable via the terminal after installation, the features of the mhwd command include:

-   The choice of free (i.e. open-source) or non-free (i.e. proprietary) drivers
-   Identification and listing (general or detailed) of your system\'s hardware
-   Identification and listing (general or detailed) of installed drivers
-   Listing of available drivers for installation (free and proprietary)
-   Support of hybrid graphics cards (e.g. Nvidia Optimus)
-   Easy removal and installation of drivers (selected automatically, or you can identify and choose your own)

\

## [mhwd Commands]

All mhwd commands are undertaken using the terminal. The syntax of a mhwd command is:

    mhwd [option(s)] <config(s)>

The mhwd options available are:

     Option                                           Explanation
     --pci                            list only pci devices and driver configs
     --usb                            list only usb devices and driver configs
     -h/--help                        show help
     -f/--force                       force reinstallation
     -d/--detail                          show detailed info for -l/-li/-lh
     -l/--list                        list available configs for devices
     -la/--listall                        list all driver configs
     -li/--listinstalled                      list installed driver configs
     -lh/--listhardware                   list hardware information
     -i/--install <usb/pci> <config(s)>           install driver config(s)
     -ic/--installcustom <usb/pci>              install custom config(s)
     -r/--remove <usb/pci> <config(s)>            remove driver config(s)
     -a/--auto <usb/pci> <free/nonfree> <classid>   auto install configs for classid
     --pmcachedir                     set package manager cache path
     --pmconfig                       set package manager config
     --pmroot                     set package manager root

\

### [Listing Hardware Information]

To identify and list your computer\'s hardware, the syntax is:

    mhwd -lh [optional: detailed view] [optional: pci or usb devices only]

\
For example, a detailed list of your hardware can be obtained by entering:

    mhwd -lh -d

\
It is also possible to filter your list by devices connected via pci or usb. In this instance, a detailed list will be generated only of hardware with a PCI connection:

    mhwd -lh -d --pci

\

### [Listing Installed Driver Information]

To identify and list Manjaro\'s installed drivers, the syntax is:

    mhwd  -li [optional: detailed view] [optional: pci or usb devices only]

\
For example, a detailed list of your installed drivers can be obtained by entering:

    mhwd -li -d

\
It is also possible to filter your list of installed drivers by whether they are used on hardware connected via pci or usb. In this instance, a detailed list will be generated only for installed drivers used on hardware with a PCI connection:

    mhwd -li -d --pci

\

### [Listing Available Drivers]

**To list all the drivers that are available** (whether appropriate for your system or not), the basic syntax is:

    mhwd -la [optional: pci or usb]

\
For example, a list of all drivers available for just USB devices (and not just those connected to your system) can be obtained by entering:

    mhwd -la --usb

\
**To list only the appropriate drivers that are available for your system**, the basic syntax is:

    mhwd -l [optional: pci or usb]

\
For example, a list of all available drivers specifically for devices connected via pci [on your system] can be obtained by entering:

    mhwd -l --pci

\

# [See also]

-   A guide to using the **mwhd** command to identify, install or remove graphics drivers can be found in the **[Configure Graphics Cards page](//wiki.manjaro.org/index.php?title=Configure_Graphics_Cards "Configure Graphics Cards")**.
-   A guide to using the **mhwd-kernel** command can be found in the **[Manjaro Kernels page](//wiki.manjaro.org/index.php?title=Manjaro_Kernels "Manjaro Kernels")**.