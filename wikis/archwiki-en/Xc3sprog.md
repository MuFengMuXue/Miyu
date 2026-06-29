# Xc3sprog

xc3sprog is a suite of utilities for programming Xilinx FPGAs, CPLDs, and EEPROMs with the Xilinx Parallel Cable and other JTAG adapters

## Installation
Install the  package.

## Devices
## Xilinx USB JTAG
Initially has , after proper initialization becomes .

* install
* extract  from Xilinx ISE
* create:
{{hc|/etc/udev/rules.d/99-xilinx.rules|2=
SUBSYSTEM=="usb", ACTION=="add", ATTR{idVendor}=="03fd", ATTR{idProduct}=="000f", RUN+="/usr/bin/fxload -v -t fx2 -I /path/to/xusb_xlp.hex -D $tempnode"}}
* reload udev rules with  and replug JTAG
* test connection with
