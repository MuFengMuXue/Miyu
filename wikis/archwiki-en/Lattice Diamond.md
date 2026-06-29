# Lattice Diamond

Lattice Diamond is a design software for Lattice FPGA architectures.

Arch Linux is not officially supported by Lattice Diamond, but as happens with other HDL suites like Xilinx ISE WebPACK or Xilinx Vivado, most of its features can be used with a bit of hacking.

## Installation
Install . Note that the installation size is around 4 GB, so generating the package might take some time due to the compression stage. If you want to shorten building the package, edit the PKGBUILD file to avoid compressing it.

## Licensing
You can request a free license to Lattice Semiconductor (registration needed). These licenses are node-locked (tied to the MAC of your Ethernet card). Once you have the license file, copy it to  (make sure you change  to the version number installed in your system) to be able to start the Diamond programs.

Note that in case one does have the relevant hardware or wants to uncouple Diamond from it, it is possible to create a dummy Ethernet interface with an arbitrarily chosen MAC address. See MAC address spoofing#Manually, or add a new dummy interface like this:

Load the relevant kernel module and create the interface with the MAC address:

 # modprobe dummy
 # ip link add bond0 type dummy
 # ifconfig bond0 hw ether 10:22:33:44:55:66

Cleanup for after Diamond exits:

 # ip link delete bond0 type dummy
 # rmmod dummy

## Troubleshooting
## Place & Route fails
If Place & Route fails with message , try deleting the  file in the root directory of your project and launch it again. It should now run normally.

## Programming with FTDI cables does not work
Programming FPGAs with FTDI chip based cables will not work if  kernel module is loaded. After plugging the programmer run:

 # rmmod ftdi_sio

Now the programmer should work until you re-attach it again (so you must run the command above every time the programmer is plugged).

## Physical Lattice device is not recognized or makes Diamond crash
The "Lattice Diamond 3.9 Installation Notice for Linux" document describes how to manually setup the serial driver but creating the udev rule as explained in that document does not work. The following rules should work:

{{hc|/etc/udev/rules.d/51-lattice.rules|2=SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="1134", ATTRS{idProduct}=="8001", MODE="0660", TAG+="uaccess", SYMLINK+="lattice-$number"

SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6010", MODE="0660", TAG+="uaccess", SYMLINK+="ftdi-$number", RUN+="/bin/sh -c 'echo $kernel > /sys/bus/usb/drivers/ftdi_sio/unbind'"}}

## Programmer tool is greyed out in Diamond GUI
It is caused by a missing dependency. Install the  package. If it is not sufficient, launch the programmer binary directly to get a report of the missing library ().
