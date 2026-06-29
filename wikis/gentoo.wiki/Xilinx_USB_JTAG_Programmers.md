[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Special Note: This wiki addresses 2 types of JTAG cables: 1. Digilent Xilinx USB JTAG cables 2. Xilinx XUP-USB-JTAG cable as well**

Assuming you have installed the Xilinx installation, this article will guide you on installing Cable Drivers for Xilinx USB JTAB Programmers. If you have problems, please check that you have not done any misstake on the primary installation.

## Contents

-   [[1] [Digilent Xilinx USB JTAG cable]](#Digilent_Xilinx_USB_JTAG_cable)
    -   [[1.1] [Getting what\'s needed]](#Getting_what.27s_needed)
    -   [[1.2] [Digilent Adept Runtime x86/x64]](#Digilent_Adept_Runtime_x86.2Fx64)
    -   [[1.3] [Digilent Adept Utilities x86/x64]](#Digilent_Adept_Utilities_x86.2Fx64)
    -   [[1.4] [Digilent Plugins x86/x64]](#Digilent_Plugins_x86.2Fx64)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Install Digilent Adept Runtime]](#Install_Digilent_Adept_Runtime)
    -   [[2.2] [Install Digilent Adept Utilities]](#Install_Digilent_Adept_Utilities)
    -   [[2.3] [Install Digilent Plugin for Xilinx Design Suites]](#Install_Digilent_Plugin_for_Xilinx_Design_Suites)
        -   [[2.3.1] [64 bits]](#64_bits)
        -   [[2.3.2] [32 bits]](#32_bits)
    -   [[2.4] [Testing]](#Testing)
-   [[3] [Xilinx XUP USB JTAG cable]](#Xilinx_XUP_USB_JTAG_cable)
    -   [[3.1] [Prerequisites]](#Prerequisites)
    -   [[3.2] [Getting drivers]](#Getting_drivers)
        -   [[3.2.1] [Setting up Environment]](#Setting_up_Environment)
    -   [[3.3] [Tweaking udev]](#Tweaking_udev)

## [Digilent Xilinx USB JTAG cable]

### [][Getting what\'s needed]

First of all, this guide assumes you have installed Xilinx ISE (version 13.4 is used here) into the default path of /opt/Xilinx Next, you will need to have GIT installed to get the required libraries. This approach does not use the official Xilinx libraries but a replica of them. You will also need libusb which is required in the compiling of the drivers. On a 64-bit host, you will need to get bin86 and dev86 packages.

### [][Digilent Adept Runtime x86/x64]

Digilent Adept Runtime package is available at [Digilent](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,828&Prod=ADEPT2) website.

Chose the package according to your linux OS. If it's a 32-bit OS, dowload Adept Runtime x86 Linux. If it's 64-bit kernel, download Adept Runtime x64 Linux. The downloaded software package is wrapped in format .tar.gz.

### [][Digilent Adept Utilities x86/x64]

Digilent Adept Runtime package is available at [Digilent](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,828&Prod=ADEPT2) website.

Chose the package according to your linux OS. If it's a 32-bit OS, dowload Adept Utilities x86 Linux. If it's 64-bit kernel, download Adept Utilities x64 Linux. The downloaded software package is wrapped in format .tar.gz.

### [][Digilent Plugins x86/x64]

Download Digilent Plugin for Xilinx Design Suite if you want to download your bitstream from XPS, ISE or iMPACT directly and debug with SDK or Chipscope. Digilent Plugin is alse available at [Digilent](http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,768&Prod=DIGILENT-PLUGIN) website.

Chose the package according to your linux OS. If it's a 32-bit OS, dowload Digilent Plug-in x86 Linux. If it's 64-bit kernel, download Digilent Plug-in x64 Linux. The downloaded software package is wrapped in format .tar.gz.

## [Installation]

First of all, decompress all packages.

`root `[`#`]`tar xzf digilent.adept.runtime_<version>.tar.gz `

`root `[`#`]` tar xzf digilent.adept.utilities_<version>.tar.gz `

`root `[`#`]` tar xzf libCseDigilent_<version>.tar.gz`

#### [Install Digilent Adept Runtime]

Enter directory digilent.adept.runtime\_\<version\>-\ then run the install script

`root `[`#`]`./install.sh`

** Note**\
If you are installing on kernel version grater then 3.0, you need to add the following lines after line 209

The lines should look like this:

[CODE] **install.sh**

    209 cprocUdev=$(ps -e | grep -i -c udevd)
    210
    211 if [ "$" = "3" ]
    212 then
    213        if (( $cprocUdev ))
    214        then
    215               let fUseUdev=1
    216        fi
    217 fi

#### [Install Digilent Adept Utilities]

Enter directory digilent.adept.utilities\_\<version\>-\, and run command the install script. This time we will keep all default locations unchanged.

`root `[`#`]`./install.sh`

#### [Install Digilent Plugin for Xilinx Design Suites]

Enter directory libCseDigilent_2.0.5-\ Enter directory of the Xilinx DS version installed on your computer. There is a pdf under the folder named: Digilent_Plug-in_Xilinx\_\<versionNo\>.pdf. The document tells exactly how to install the Digilent Plugin and how to use it. To install plugin is quite easy, all you need to do is copy the libCseDigilent.so and libCseDigilent.xml Digilent plugins folder

##### [64 bits]

`root `[`#`]`cp libCseDigilent.so <Xilinx_DS_Path>/ISE/lib/lin64/plugins/Digilent/libCseDigilent/ && cp libCseDigilent.xml <Xilinx_DS_Path>/ISE/lib/lin64/plugins/Digilent/libCseDigilent/`

##### [32 bits]

`root `[`#`]`cp libCseDigilent.so <Xilinx_DS_Path>/ISE/lib/lin/plugins/Digilent/libCseDigilent/ && cp libCseDigilent.xml <Xilinx_DS_Path>/ISE/lib/lin/plugins/Digilent/libCseDigilent/`

If there is no dir *Digilent* under [\<Xilinx_DS_Path\>/ISE/lib/lin64/plugins/], just make a new dir with command mkdir.

`root `[`#`]`>mkdir <Xilinx_DS_Path>/ISE/lib/lin64/plugins/Digilent`

### [Testing]

Connect your digilent board to your PC, and check whether Adept utilities can recognize your board. All you need is to run the command **djtgcfg** and see whether your boards pop up.

`user `[`$`]`djtgcfg enum`

Now open Impact

`user `[`$`]`/Xilinx_DS_Path>/ISE/bin/lin/impact&`

See if any FPGA can be found on your JTAG chain.

For now on I belive that you can walk by yourself, and begin to program your device.

## [Xilinx XUP USB JTAG cable]

These drivers and method of using them is verified with ISE 14.5 on Gentoo 64bit. Drivers provided with ISE installation don\'t work with Linux system. Even installing as super user gives an error.

### [Prerequisites]

To follow these instructions git and fxload are required

`root `[`#`]`emerge --ask git fxload`

### [Getting drivers]

Clone the git repository for proper drivers:

`user `[`$`]`git clone `[`git://git.zerfleddert.de/usb-driver`](git://git.zerfleddert.de/usb-driver)

change to the directory where repository is cloned and compile proper drivers

`user `[`$`]`make`

#### [Setting up Environment]

Add compiled driver library to environment path:

`user `[`$`]`export LD_PRELOAD=path/to/USB/driver/folder/usb-driver/libusb-driver.so`

### [Tweaking udev]

Copy proper rule file under udev: For impact to work with compiled drivers \'TEMPNODE\' needs to be changed to \'tempnode\', BUS==\"usb\" needs to be removed and SYSFS needs to be changed to ATTR.

`root `[`#`]`sed /path/to/ISE/installation/folder/14.x/ISE_DS/ISE/bin/lin(64)/xusbdfwu.rules -e 's:TEMPNODE:tempnode:g' | sed 's:BUS=="usb", ::g' | sed 's:SYSFS:ATTR:g' | sudo tee /etc/udev/rules.d/50-xusbdfwu.rules 1>/dev/null`

Copy Xilinx hex files to /usr/share

`root `[`#`]`cp /path/to/installation/folder/Xilinx/ISE/bin/lin/xusb*.hex /usr/share`

Restart udev

`root `[`#`]`/etc/init.d/udev restart`

or, if using systemd

`root `[`#`]`sudo udevadm control --reload`

Now starting impact should detect cable properly.