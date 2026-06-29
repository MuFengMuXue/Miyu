# SANE

SANE (Scanner Access Now Easy) provides a library and a command-line tool to use scanners under GNU/Linux.

## Installation
Install the  package. Most front-ends and drivers pull this as a dependency anyway, so it is often unnecessary to explicitly install it.

## Scanner drivers
Many modern scanners support "driverless" scanning.You can look for your device's compatibility on [https://github.com/alexpevzner/sane-airscan#compatibility sane-airscan GitHub or Apple AirPrint devices.

Install the  package if the scanner is known to work in "driverless" mode. If your scanner is using USB, also install the  package and start/enable  to allow using IPP protocol over USB connection.

Otherwise, check SANE - Supported Devices and SANE/Scanner-specific problems to see if your scanner will work with a different driver.

Most scanners should work out of the box. If yours does not, see SANE/Scanner-specific problems for installation instructions.

## Frontends
Many frontends exist for SANE, a non-exhaustive list of which can be found on the SANE project website.

*
*
*
*
*
*
*

Some OCR software can scan images using SANE: gImageReader, gscan2pdf, Linux-Intelligent-Ocr-Solution, OCRFeeder, Paperwork.

## Verification
Now you can try to see if sane recognizes your scanner.

 $ scanimage -L

If that fails, run the command again as root to check for permission problems. If that fails as well, check that your scanner is plugged into the computer. You also might have to unplug/plug your scanner for  to recognize your scanner.

Now you can see if it actually works

 $ scanimage --format=png --output-file test.png --progress

If the scanning fails with the message  you may need to specify the device.

Then you would need to run

 $ scanimage --device "pixma:04A91749_247936" --format=tiff --output-file test.tiff --progress

Sane provides many special backend options for numerous scanner types. To see what these are for your device:

 $ scanimage -A

## Firmware
Firmwares usually have the .bin extension.

Firstly you need to put the firmware someplace safe, it is recommended to put it in a subdirectory of .

Then you need to tell sane where the firmware is:

* Find the name of the backend for your scanner from the sane supported devices list.
* Open the file .
* Make sure the firmware entry is uncommented and let the file-path point to where you put the firmware file for your scanner. Be sure that members of the group  can access the  file.

If the backend of your scanner is not part of the sane package (such as  which is part of ), you need to uncomment the relevant entry in  or in .

## Sharing your scanner over a network
You can share your scanner with other hosts on your network who use sane, xsane or xsane-enabled GIMP. To set up the server, first indicate which hosts on your network are allowed access.

Change the  file to your liking, for example:

 # required
 localhost
 # allow local subnet
 192.168.0.0/24

Second, install, start and enable avahi-daemon on your server (if it is not already active) so your scanner can be found by multicast. Or, if your scanner is supported by Airscan installing the  package is an alternative.

If you use iptables, insert the  module to let the firewall track  connections.

Conntrack helper seems to be disabled by default.You can activate it with

 # echo 1 > /proc/sys/net/netfilter/nf_conntrack_helper

To configure this permanently, set the  option for the  module, see Kernel module#Using modprobe.d.

Now start/enable . Your scanner is now available over the network. For more information, see .

## Accessing your scanner from a remote workstation
You can access your network-enabled scanner from a remote Arch Linux workstation.

First, specify the server's host name or IP address in the  file:

 # static IP address
 192.168.0.1
 # or host name
 stratus

Second, depending on what you configured at the server side, install, start and enable avahi-daemon or install sane-airscan at the remote workstation.

Now test your workstation's connection:

 $ scanimage -L

The network scanner should now also show up in some front-ends.

## Windows and macOS clients
Since the Windows port of SANE seems to be [https://web.archive.org/web/20151207111023/http://www.xsane.org/xsane-download.html unsupported, outdated and difficult to get, you can try SANEWinDS or SaneTwain (old).

It is possible to use the Windows or macOS native scan UI with AirSane which could be installed via . To access printers shared that way on Linux,  could be used.

## Troubleshooting
See also SANE/Scanner-specific problems.

## Invalid argument
If you get an "Invalid argument" error with xsane or another sane front-end, this could be caused by one of the following reasons:

## Missing firmware file
No firmware file was provided for the used scanner (see #Firmware for details).

## Wrong firmware file permissions
The permissions for the used firmware file are wrong. Correct them using

 # chown root:scanner /usr/share/sane/SCANNER_MODEL/FIRMWARE_FILE
 # chmod ug+r /usr/share/sane/SCANNER_MODEL/FIRMWARE_FILE

## Multiple backends claim scanner
It may happen, that multiple backends support (or pretend to support) your scanner, and sane chooses one that does not do after all (the scanner will not be displayed by  then). This has happened with older Epson scanners and the  resp.  backends. In this case, the solution is to comment out the unwanted backend in . In the Epson case, that would be to comment out epson2:

It may also be possible that the independent   backend interferes with your  backend (epson scanners). You may get this error right after using the  command. Starting the scanner app (like ) twice can also solve the problem. Otherwise check your  for wrong configurations or remove the  package.

## Communication via xHCI not working (older scanner models)
Some older scanner models do not work when connected via an USB3 port. If you experience this issue, try setting the  environment variable before starting your frontend.If that does not work, try one of the following workarounds:

* Use an USB2 port instead of an USB3 port, if available.
* Disable xHCI via BIOS/EFI. eHCI will consequently be used and communication with the scanner will work. On the downside, USB3 speed can not be reached on any port.
* On (some) intel chipsets the  command can be used to route specific usb ports to either the xHCI or the eHCI controller. See [https://superuser.com/questions/812022/force-a-single-usb-3-0-port-to-work-as-usb-2-0 force-a-single-usb-3-0-port-to-work-as-usb-2-0 (scroll down to where it says "setpci") for further information. With this it is possible to toggle single USB ports with a simple shell script.
* Connect the scanner over the network instead if it is supported.

## Firewall
When network scanning scanner hangs, then invalid argument error occured.

saned uses data port range, so you must enable connections to 6566/tcp and  from  or use conntrack firewall module for sane to enable data ports as described above.

## Slow startup
If you encounter slow startup issue (e.g.  or  does not return results nearly instantly), one of the drivers you do not use may be the culprit.

You can resolve this by editing  and commenting out the scanner drivers you do not use. You can use  to determine which drivers you need:

The parts between the  and the  in the output indicate the driver for the device. For example, if only want to use the Brother scanner and not the webcam or the generic scanner driver, you can comment out everything but the  driver in .

Another reason for slow startup issues might be in the driver-specific configuration file at ; as an example, it has been reported that commenting out  in  solves these slow startup issues for Epson scanners using USB.

## Device busy
If your USB device is listed with  but launching the test  always return the 'Device busy' error, you might try to add your username to the scanner group  then blacklist the  kernel module by writing  in  (it prevents  from loading to support scanning, not needed by xsane and related tools, might also conflict with CUPS). Reboot to finish. In addition to this, some Cannon printers return "device busy" if the scan mode is set to "Computer". Setting this to the "Remote Scanner" mode should fix the issue.[https://alioth-lists.debian.net/pipermail/sane-devel/2014-March/032169.html

## Permission problem
With systemd, the  and  groups are deprecated. No need to add your user to those groups. See Users and groups#Pre-systemd groups for detail.

You can also try to change permissions of usb device but this is not recommended, a better solution is to fix the Udev rules so that your scanner is recognized.

First check connected usb devices with :

 Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
 Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
 Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
 Bus 003 Device 003: ID 04d9:1603 Holtek Semiconductor, Inc.
 Bus 003 Device 002: ID 04fc:0538 Sunplus Technology Co., Ltd
 Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
 Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
 Bus 001 Device 006: ID 03f0:2504 Hewlett-Packard
 Bus 001 Device 002: ID 046d:0802 Logitech, Inc. Webcam C200
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

In our example we see the scanner: . Here  is the vendorID and  is the productID.

Alternatively, running  with root permission will also give you the same vendorID and productID.

Now open  and see if there is a line with the vendorID and productID of your scanner. If there is not any, create the new file , with the following contents:

 ATTRS{idVendor}=="vendorID", ATTRS{idProduct}=="productID", MODE="0664", GROUP="lp", ENV{libsane_matched}="yes"

Save the file, plug out and back in your scanner and the file permissions should be now correct.

Another tip, is that you can add your device (scanner) in backend file:

Add  to  so it looks like this:

 #
 # Configuration file for the hp4200 backend
 #
 #
 # HP4200
 #usb 0x03f0 0x0105
 usb 0x03f0 0x2504

## Parallel port scanners
All devices attached to a parallel port are assumed to be printers, and are given a  group. Either create a udev rule to mark the relevant parallel port as , or add your user to the  user group. CUPS also uses the  group for read-only access to configuration files, so there are potential security implications to adding users to the  group - see CUPS#Connection interfaces for more information.

## avahi-daemon is not mandatory
Some scanner applications may require you to start the avahi-daemon upon startup. This is actually the cause of SANE. If for some reason you do not want to enable the avahi-daemon service because you use a wired scanner or do not need it because your scanner's driver supports networking already on setup, then comment out the  backend in the SANE configuration:

Additionally you can try and edit  and  and comment the lines inside.

Then restart the  daemon.

## Error during device I/O
If you are getting  while trying to scan using an HP scanner, make sure you have  installed (see CUPS/Printer-specific problems#HP).

## Tips and tricks
## scanimage output is not satisfying
When  output is not satisfying, one might run

 $ scanimage --all-options

to request a listing of all available options exposed by the backend. The output may hint the unsatisfying output is due to too low default values, and also state what values can be explicitly set that might improve the result.
