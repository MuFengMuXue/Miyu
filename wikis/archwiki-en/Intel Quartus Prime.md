# Intel Quartus Prime

From the Intel Quartus Prime overview:

:The revolutionary Intel® Quartus® Prime Design Software includes everything you need to design for Intel® FPGAs, SoCs, and complex programmable logic device (CPLD) from design entry and synthesis to optimization, verification, and simulation.

This article focuses on the following Intel FPGA software components:

* Quartus Prime Lite
** Intel FPGA Download Cable (II)
* Questa-Intel FPGA Edition — included with Quartus Prime Lite Edition

## Installation
Quartus Prime Lite and Questa can be installed with the  meta-package. This meta-package will also install device support for every supported device family. To save on disk space once the package is built, you can install only the necessary components. For example:

*  for Quartus Prime Lite
*  for Questa

quartus-free-quartus requires quartus-free-devinfo, which is provided by any one of the packages with a quartus-free-devinfo- prefix. For example, install the  dependency if you have a Cyclone V FPGA.

Quartus II 13.0 Web Edition is "the last version to support Cyclone II and earlier FPGAs", so install quartus-free if support for such devices is needed or  for the SP1 Subscription Edition.

Unlike ModelSim, Questa requires a valid license file even for the free version. Those who do not wish to provide one can install the last version of ModelSim () instead.

quartus-free-quartus uses files in  to extend the  environment variable, so log into a new session to make commands like quartus_sh available.

Being in the  group to program an FPGA (via the USB-Blaster) is optional; logged in users are always allowed access.

## Usage
Run Quartus Prime Lite by running  or selecting its desktop entry. Use the quartus_sh utility to run Quartus Prime Shell. See  for more information.

Run ModelSim by running  or selecting its desktop entry. See  for more information.

## Standard Edition license validation
Configuring the path to your Quartus Prime Standard Edition license file from the Quartus Prime settings interface is not enough for successful license validation. The license validation routine looks for your MAC address on interface , the traditional name for your Ethernet controller. However, network interfaces use predictable names by default—these can vary from machine to machine. Thus, the expected  name must be retained by following Network configuration#Revert to traditional interface names.

Alternatively, a dummy  network interface can be dynamically created by systemd-networkd at boot. This may be desirable for systems without a wired Ethernet adapter. Create the following file (where  is your machine's hostname):

Ensure  is started/enabled afterwards.

See also related articles on the Intel Knowledge Base:

* Why does my Quartus/OpenCL license not work on Red Hat 7.x?
* Why does OpenCL node locked license not work with multiple ethernet port?

## Education license
## Generating license
You can get the licenses you need from:
https://www.intel.com/content/www/us/en/my-intel/fpga-sslc-sign-in.html
You first need to register to get access. Use Student as Profession.
When you have access, sign in and select "Sign up for Evaluation of Free Licenses"
You need to generate two license files.

## Choosing right license
Select "Questa*-Intel® FPGA Starter Edition SW-QUESTA". Edit "# of Sets" to 1 and click
"Get license".
Select +New Computer (if this is your first time here) and fill in the following using a
computer name of your choice and yourself as Primary Admin.

Select Computer Type -> NIC ID

Computer ID -> your MAC address

You find your computer’s NIC ID (Physical address without ‘:‘) using the "Terminal" and typing . This number should then replace 123456789ABC in Computer ID fields. Then click on "Generate License".

You will now receive an email with two license file. You might want to put them in the Quartus program directory, e.g., under "licenses".

## Setting up environment variable
You need three variables:
MGLM_LICENSE_FILE,
LM_LICENSE_FILE and
LS_LICENSE_FILE

For MGLM_LICENSE_FILE and LS_LICENSE_FILE, you need to bind them to the file with the larger content.
For LM_LICENSE_FILE, you need to bind this to the smaller file.

you can bind these in a lot of different ways. But one way to do this is add the following to the /etc/environment :

## Enabling Eclipse and NIOS IDE
Follow this guide from intel. And disregard step "6)" where it mentions an .exe file

https://www.intel.com/content/www/us/en/docs/programmable/683525/21-3/linux-installation.html

## Troubleshooting
## Gray window
Some of the built-in editors in Quartus Prime such as IP editors and Tools > Platform Designer (aka Qsys) only show a blank window with Xmonad or Sway.

See Java#Gray window, applications not resizing with WM, menus immediately closing for the solutions.

## USB-Blaster not working
Run  and depending on the output:

## No JTAG hardware available
If the device is listed by , restart  as root # killall -9 jtagd
 # jtagd

## JTAG chain broken
 1) USB-Blaster [3-2
   Unable to read device chain - JTAG chain broken

Perform the steps under the "Linux" section in https://web.archive.org/web/20251010093308/https://ecen3350.rocks/static/usb-blaster.pdf. Note that the Arch Linux path to  in step 3 should be as follows:

 /opt/intelFPGA/PKGBUILD_mainver/quartus/bin

Steps 3 and 5 should also be performed with root privileges.

Another possible cause may be a missing 32-bit version of  provides this shared object, so make sure it is installed. (This should already be the case since it is a transitive dependency of .)

If the error still persists, try installing .

## Error when scanning hardware - Server error
 Connecting to server(s) [........
 Error when scanning hardware - Server error

A workaround is to edit  or  (depending on whether you want to run  as root or as an unprivileged user) to include the following line:

 Password = "changeme";

Add the server afterwards:

 $ jtagconfig --addserver 127.0.0.1 changeme

If problems still persist, try restarting :

 # killall -9 jtagd
 $ jtagd

## ModelSim
## Failure to access library 'work'
The following error may be encountered when running a simulation in a new directory:

 Error: (vcom-19) Failed to access library 'work' at "work".

This can be resolved by creating the  directory from the ModelSim console ModelSim> vlib work

## Unreachable host
ModelSim may crash with the following error when trying to start a simulation:

 Error: couldn't open socket: host is unreachable
 Trouble making server.

This can be resolved by adding  entries for  as specified in Network configuration#Local network hostname resolution.
