# Xilinx ISE WebPACK

The Xilinx ISE WebPACK is a complete FPGA/CPLD programmable logic design suite providing:
* Specification of programmable logic via schematic capture or Verilog/VHDL
* Synthesis and Place & Route of specified logic for various Xilinx FPGAs and CPLDs
* Functional (Behavioral) and Timing (post-Place & Route) simulation
* Download of configuration data into target device via communications cable

The development of the ISE WebPACK has been stopped in favor of the Vivado Suite, but it is still useful to develop for older devices not supported by the new suite.

While Arch Linux is not one of the officially supported distributions, many features are known to work on Arch Linux.

## Prerequisites
## Download ISE WebPACK
The Xilinx ISE WebPACK is a freeware software released under a proprietary license which does not allow redistribution. To obtain the install data visit the official download page.

## Dependencies
Several tools included in the ISE Webpack (and the installer itself) depends on . Additionally other tools (e.g. the FPGA editor) requires    .

If you plan to develop software for an embedded ARM core (e.g. for Xilinx Zynq SoC devices), you will want to install the GCC cross-compiler bundled included with the Xilinx Embedded Development Kit (EDK). This compiler requires the  package from the multilib repository and .

## Default shell
During the installation, the Mentor CodeSourcery toolchains for embedded processors can be installed along with the Xilinx tools. This installation silently fails when the default shell is set to dash. Make sure  points to .

This can be checked by running this command:
 $ ls -l /usr/bin/sh

If the output looks like this:

then  already points to . (the default in Arch Linux).

If not, link  to bash:
 # ln -sfT bash /usr/bin/sh

## Installation
## Install from AUR
Install the package , you will have to place the tarball with the installation data in the same folder of the  before starting the building process.

## Manual installation
Extract the tarball containing the installation data:
 $ tar -xvf Xilinx_ISE_DS_Lin_14.7_1015_1.tar

The ISE design tools installer is a Qt application. If you are running the KDE desktop environment, the installer may try to load the "Oxygen" widget theme, which will fail due to the older Qt framework bundled with the Xilinx ISE design tools. You need to remove the  environment variable before executing the installer:
 $ unset QT_PLUGIN_PATH

Then, install the ISE Design Tools:
 $ cd Xilinx_ISE_DS_Lin_14.7_1015_1
 $ ./xsetup

Follow the instructions to install the ISE. By default, the whole application is installed to , so make sure the user running the installer has permissions to write to this directory.

During installation, uncheck the "Install Cable Drivers" option. Leaving it checked will cause errors during the installation.

## Launching the ISE design tools
The ISE design tools include a shell script that modifies the environment variables (mostly  and ). This script must be sourced before starting the ISE tools:
 $ source /opt/Xilinx/14.7/ISE_DS/settings64.sh

Then, the ISE design tools will be found in your  and can be started by typing their name in the terminal (e.g. , , , ...)

## Launching via desktop icons
You can also create a desktop entry at

After that you can copy this file to the  folder and launch ISE tools from the desktop.

## License installation
After requesting a WebPACK license from Xilinx using their Licensing Site, you will be e-mailed a license file. This file can be imported with the Xilinx License Manager (run  from the terminal).

Another way to import the license is to simply copy it to the  or  directory.

## Node-locked licenses
Arch Linux by default uses systemd's Predictable Network Interface Names. This means that your system will most likely not have its network interfaces named ,  and so forth.

However, the Xilinx License Manager looks for these names to find out the system's MAC addresses, which are used for node-locked licenses. If you want to use node-locked licenses, you will have to manually assign to your interface a name in the format expected by the License Manager. Network configuration#Revert to traditional interface names explains how to do so. If your machine does not have a wired Ethernet adapter, then it is possible to use systemd and the  kernel module to create a virtual Ethernet adapter with the proper MAC address. To do this, create the following:

Then, restart the  service.

## Post-installation fixes and tweaks
After installation, a few manual fixes are required to work around problems caused by running the Xilinx tools on a Linux distribution that is not officially supported by Xilinx. Some of these fixes are taken from this forum post.

## Dynamic library fix (libstdc++.so)
The ISE tools supply an outdated version of the libstdc++.so library, which may cause segfaults when using the Xilinx Microprocessor Debugger and prevents the usage of the oxygen-gtk theme. This outdated version is located in two directories within the installation tree:  and . To use Arch's newer version of libstdc++, rename or delete the original files and replace them with symlinks:
 $ cd /opt/Xilinx/14.7/ISE_DS/ISE/lib/lin64/
 $ mv libstdc++.so libstdc++.so.bak
 $ mv libstdc++.so.6 libstdc++.so.6.bak
 $ mv libstdc++.so.6.0.8 libstdc++.so.6.0.8.bak
 $ ln -s /usr/lib/libstdc++.so
 $ ln -s libstdc++.so libstdc++.so.6
 $ ln -s libstdc++.so libstdc++.so.6.0.8

Then, repeat this process in the  directory.

## Digilent USB-JTAG drivers
To use Digilent Adept USB-JTAG adapters (e.g. the onboard JTAG adapter on the ZedBoard) from within the Xilinx design tools, you need to install the Digilent Adept Runtime and Plugin.

Make sure you have installed .

To install the Digilent Adept Runtime, it is recommended to install .

In addition, installing  may do good to configuring your board.

To install the Digilent plugin, you have to copy two files to the ISE plugin directory
 # mkdir -p /opt/Xilinx/14.7/ISE_DS/ISE/lib/lin64/plugins/Digilent/libCseDigilent
 # cd /opt/Xilinx/14.7/ISE_DS/ISE/bin/lin64/digilent/libCseDigilent_2.4.4-x86_64/lin64/14.1/libCseDigilent
 # cp libCseDigilent.{so,xml} /opt/Xilinx/14.7/ISE_DS/ISE/lib/lin64/plugins/Digilent/libCseDigilent
 # chmod -x /opt/Xilinx/14.7/ISE_DS/ISE/lib/lin64/plugins/Digilent/libCseDigilent/libCseDigilent.xml

Finally, add every user that should have access to the Digilent USB-JTAG adapter to the "uucp" group.

To grant access to the USB driver for normal users you may have to add the USB Vendor/Product IDs of your JTAG adapter which can be found with
 $ lsusb | grep Xilinx
to the udev rules in :
 SUBSYSTEM=="usb", ATTRS{idVendor}=="xxxx", ATTRS{idProduct}=="xxxx", GROUP="users", MODE="666"

If it still does not work, you can make further reading in Xilinx_JTAG_Linux. The magic git repository there may be help.

## Xilinx Platform Cable USB-JTAG drivers
Make sure you have installed .
We need to build driver from source (git and some make stuff need to be installed, make will say what programs or libraries are missed):

 $ cd /opt/Xilinx
 # git clone git://git.zerfleddert.de/usb-driver
 $ cd usb-driver/
 $ make

If you using 32-bit version of ISE on 64-bit system, pass "lib32" to make:

 $ make lib32

And install driver (replace 14.7 to your version):

 $ ./setup_pcusb /opt/Xilinx/14.7/ISE_DS/ISE

Or in older versions:

 $ ./setup_pcusb /opt/Xilinx/10.x/ISE

If driver installed correctly and udev rule works, STATUS led should turn on (green or red depending on voltage presence on VREF PIN)

 $ export LD_PRELOAD=/opt/Xilinx/usb-driver/libusb-driver.so

## Locale issues
PlanAhead does not like locales using other literals than '.' as the decimal point (e.g. German, which uses ','). Run the following command before launching PlanAhead:
 $ unset LANG

## Segmentation fault on PlanAhead
When launching PlanAhead to generate a .ucf file, a segmentation fault may occur. The issue seems unrelated to the previous topic. The ISE console will show
 "/opt/Xilinx/14.7/ISE_DS/PlanAhead/bin/rdiArgs.sh: line 64: 14275 Segmentation fault      $RDI_PROG $*"
The problem seems to come from the bundled JRE as described here. To fix the issue, symlink the OpenJDK libjvm.so into the Xilinx's installation directory.
 # pacman -S jre8-openjdk-headless
 # cd /opt/Xilinx/14.7/ISE_DS/PlanAhead/tps/lnx64/jre/lib/amd64/server
 # mv libjvm.so{,-orig}
 # ln -s /usr/lib/jvm/java-8-openjdk/jre/lib/amd64/server/libjvm.so

Remember! newer version of jre such as  (version 17) is not suitable (can lead to error)

## GNU make
XSDK looks for the  executable, which is not present in Arch Linux by default. Create a symlink somewhere in your path, e.g.
 $ ln -s /usr/bin/make /home//bin/gmake

Make sure this directory is in your PATH variable.

## Running Xilinx tools from within KDE
KDE by default defines the QT_PLUGIN_PATH shell variable. Some of the Xilinx ISE tools (ISE, Impact, XPS) are Qt applications, which means that they will search for Qt plugins in the locations defined by this shell variable.

Because the Xilinx tools are compiled against and ship with an older version of the Qt framework which cannot use these plugins, they will crash when launched with this environment variable present.

To fix this issue, run the following command before launching the tools:

 $ unset QT_PLUGIN_PATH

## CORE Generator fails to generate core
In some cases, the CORE Generator will fails to generate a core and output something like this to its console:

 ERROR:sim - Unable to evaluate Tcl file:
    /opt/Xilinx/14.7/ISE_DS/ISE/coregen/ip/xilinx/primary/com/xilinx/ip/clk_wiz_v3_6/generate/run_legacy_tcl_flow.tcl
 ERROR:sim - Failed executing Tcl generator.

## Solution #1
If that happens, make sure you do not have _JAVA_OPTIONS set in your environment. If you normally run coregen with

 $ source /opt/Xilinx/14.7/ISE_DS/settings64.sh && coregen

you need to prepend that with an "unset _JAVA_OPTIONS":

 $ unset _JAVA_OPTIONS && source /opt/Xilinx/14.7/ISE_DS/settings64.sh && coregen

## Solution #2
Solution #1 no longer works due to: coregen's bundled java fails to start. Workaround force using ISE bundled java6 instead of java5.

Backup old version

 $ mv /opt/Xilinx/14.7/ISE_DS/ISE/java/lin64/jre/bin/java /opt/Xilinx/14.7/ISE_DS/ISE/java/lin64/jre/bin/java.old

Add symbolic link to java6

 $ ln -s /opt/Xilinx/14.7/ISE_DS/ISE/java6/lin64/jre/bin/java /opt/Xilinx/14.7/ISE_DS/ISE/java/lin64/jre/bin/java

## Solution #3
If the previous methods fail, try to run the 32-bit version of coregen:

 $ unset _JAVA_OPTIONS && source /opt/Xilinx/14.7/ISE_DS/settings32.sh && coregen
