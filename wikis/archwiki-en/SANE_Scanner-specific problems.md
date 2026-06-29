# SANE/Scanner-specific problems

This article contains scanner or manufacturer-specific instructions for SANE.

## Agfa
## Snapscan e40
Firmware  from here is required.

If USB autosuspend is enabled, the printer may need to be turned off and on again before each scan.

## BenQ/Acer
If you own an USB scanner from Acer (now BenQ), you need to download a suitable firmware binary and configure .

* Find out which model you own and take note of the USB ID:

* Go to snapscan main page and see whether your scanner is supported and which firmware you need (e.g, ).
* Search the firmware image on the Internet and download it to .
* Edit the head of  and configure the following two lines:
 firmware /usr/share/sane/snapscan/u176v046.bin
 /dev/usb/scanner0 bus=usb

## Brother
In order to install a Brother scanner or printer/scanner combo you need the right driver. To find the right one, see the FAQ for your model at the Brother Support, i.e. Home > Country > Your model > FAQs & Troubleshooting > Linux > Scanner / Scan Key Tool > Scan using XSane or GIMP. You can also search the web. Or see the information below for more scanners. Or extract each of the AUR packages below. Each package seems to contain an exhaustive list of the models it is suitable to.

Then, install the appropriate package:

*
*
*  (MFC-J5620DW)
*
*

Now, the scanner should be recognized by SANE.

For network scanners, Brother provides a different configuration tool for each brscan version (e.g., brsaneconfig2 for brscan2 compatible devices):

 # brsaneconfig2 -a name=ScannerName model=ScannerModel ip=ScannerIP

Example:

 # brsaneconfig2 -a name=SCANNER_DCP770CW model=DCP-770CW ip=192.168.0.110

To get the IP and node name of your scanner, you can use Nmap:

 $ nmap -sP 10.0.0.0/24

It's also possible to add a scanner via its node name instead of its IP, for example:

 # brsaneconfig4 -a name=Brother_DCP-L3550CDW model=DCP-L3550CDW nodename=BRWC0B5D72A0B87

## Network Scanning
In case of network scanning, e.g. by Wi-Fi, Sane may still be unable to find the scanner. If so, you need to specify the IP address of the scanner in the  file.

Now use  to check whether sane is able to find your scanner. If not, further check that Sane expects this device through the network (see Check that  contains , where the  stands for the brscan version from above. If nothing was found, add  to the end of the file.

## Invalid argument
If all the necessary packages are installed but you still get the "invalid argument" error this could mean that the configuration file has been corrupted. Run the following command (in case of brscan4):

 # brsaneconfig4 -d

The output should narrow down the problem. Most likely the connection is not set up correctly. In case of a network scanner, check if the IP address is right by opening  with an editor. In case of a USB connection, check if the path to the scanner in the configuration file is set up correctly. For that, compare the values of the  command with your configuration file and change them if necessary. You might also try to follow the  suggestion from Network Scanning above even for non-network scanners.

## Scan-key-tool
Brother has released a tool to enable scanning to be triggered by user interaction with the scanner itself (e.g., by selecting one of "Scan to email", "Scan to image", etc. on the scanner's keypad) rather than by an attached computer. This can be set up by installing the  package and starting  using systemd. Note that by default this service runs as the brscan-skey user which is created by the package, whose home directory is located at .

Brother supplies some default scripts that are executed when a scan type is selected on the keypad. These may require the installation of some optional dependencies of the  package. For all options apart from "Scan to email" the resulting output can be found inside , with  the home directory of the user running this tool (so  if started via systemd as a systemwide process).

It is possible to change what action takes place when a given type of scan is selected on the keypad. This is done by editing . For each variable  in , , , , the command

 $ $SCAN_COMMAND $SCANNER_DEVICE $SCANNER_FRIENDLY_NAME

is executed when the corresponding scan type is selected. Note that  is not quoted so may specify more than one positional parameter in the final command that is executed.  refers to the name of the device that should be specified to a sane frontend (e.g. via the  flag when using ), for example .  is the human-readable name of the scanner.

## xsane crashes
If xsane crashes with message "", then you need to create the link .

## Canon
## Scanning over the network with Canon PIXMA or imageCLASS all-in-one printer/scanners
Find out your printer/scanner's IP address, and add it on a new line to  in the format . For imageCLASS printers you may need to use the format  instead.

Sane should now find your device. For more details refer to .

Alternatively,  can be used for some Canon PIXMA all-in-one printer/scanners which are not detected over the network.

## Scanning over the network with the eSCL protocol for Canon MAXIFY printer/scanners
As mentioned in the sane-pixma documentation , Canon seems to be dropping support the BJNP and MFNP protocols in recent scanners. As an alternative, you could try using the eSCL protocol for scanning over the network. To do so, find your printer/scanner's IP address and add a new line to the  configuration file, using the format . The scanner model is used as an identifier, for example the command .

## Epson
## Driver-Backends
For Epson scanners, you can choose between two different backends: "Image Scan v3" (/utsushi) or "Image Scan! for Linux" (/epkowa). A list of supported devices exists for [http://www.sane-project.org/lists/sane-backends-external.html#S-UTSUSHI imagescan/utsushi and iscan/epkowa.

## Image Scan v3
If you have to use Image Scan v3-backend you can install . It should detect supported USB scanners automatically by default. If your scanner is not recognized you can directly edit the  and add the following lines.

 dev1.udi     = esci:usb:vendor_id:product_id
 dev1.name    = foo
 dev1.model   = Model Name of the scanner

If you want to make use of a network scanner you also have to install . Then edit  and enter the ip address of your scanner to it.

 [devices
 myscanner.udi    = esci:networkscan://ip-address-here:1865
 myscanner.vendor = Epson
 myscanner.model  = Model-name

When you then start Image Scan v3 by typing in the command
 $ utsushi
the name of the scanner should be visible in the top left corner. If a connection problem happened, an error dialog will be shown.

## Image Scan! for Linux
* Install the  package.
* Install the appropriate iscan-plugin package for your scanner (for example,  for the Epson Perfection Photo V600)
* Run  so that udev will recognize the device as a scanner and apply appropriate permissions.

For network (including Wi-Fi) scanners, install iscan and , then edit  and add a line of the following format:

 net  Upstream version of iscan did not support 16bpc color depth scanning. Choosing any bit depth other than 8 made iscan stop without warning, leaving the scanner stuck until restarted. To enable 16bpc scanning, iscan used to required to be patched. It could be that an old patch, found in  [https://bbs.archlinux.org/viewtopic.php?pid=1841337#p1841337 this forum thread, will enable 16bpc depth mode.

## Epson DS-6500
Usually this device works with the epsonds-backend. However, there may be an error "Error during device I / O" when scanning multiple pages. If this error occurs, the Image Scan v3 backend can be used and  needs to be installed. If you want to use the network module, the scanner can be configured in the  after installing  as described above.

## Epson Perfection V39
This device (vendor id: 0x04b8, device id: 0x013d) is known to be supported by SANE's epkowa backend. To use this backend, install ,  and .

The latter package provides the firmware  which is required to make the scanner work.

In case of a successful device setup, running  results in:

* the scanner waking up and performing some movements,
* a constantly shining blue led at the device's front, and
* output similar to .

In some cases, the above fails due to improper firmware, provided by .

As stated in this forum thread, using the firmware  provided by  can solve the problem. There seem to exist different incompatible versions of the same firmware.

## Epson Perfection V39II
Install

## Epson Perfection V550 Photo
Install

## Epson Perfection 1270
For Epson Perfection 1270, you also need a firmware named . It can be obtained by installing the Windows driver.

Modify the configuration file of the snapscan backend, . Change the firmware path line with yours:

 # Change to the fully qualified filename of your firmware file, if
 # firmware upload is needed by the scanner
 firmware /mnt/mydata/Backups/firmware/esfw3e.bin

And add the following line in the end or anywhere you like

 # Epson Perfection 1270
 usb 0x04b8 0x0120

You can get such code information () by sane-find-scanner command.

Also add such information lines to  to setup your privilege, like:

 # Epson Perfection 1270
 libusbscanner 0x0003 0x04b8 0x0120 0x0000 0x0000 0x00 0x00 0x00 0x00 0x00 0x00 0x00000000

Replug scanner, you have a working Epson Perfection 1270 now.

To prevent  and hangup of the scanner itself, when trying to scan with ADF (automatic document feed) enabled, I had to remove or comment out all Backends from  and instead just add this to the file:

If you still get the  messages check that the transportation lock of the scanner (on the bottom of the scanner) is open.

## Epson Perfection 1670/2480/2580/3490/3590
Make sure to download the correct firmware for your Epson model. You can get an overview of some models and their drivers here and here. The download links of the firmware are broken, but you can use this link as alternative instead. Make sure to change the firmware filename of the link suiting your model. If you want to download and extract the firmware sources from the official epson sites yourself you can use this guide.

As an alternative you can also install the AUR package  which will download the firmware from the official sources, extract the binary and install those to .

Modify the configuration file of the snapscan backend, . Change the firmware path line with yours:

 # Change to the fully qualified filename of your firmware file, if
 # firmware upload is needed by the scanner
 firmware /usr/share/sane/snapscan/esfw52.bin

Other modifications were not needed for the Epson Perfection 3590 and might not be for other models as well. If you still have problems it can also help if you completely remove the  package.

## EPSON WorkForce printer/scanners over the network
Install  and .

Edit the configuration file . Find the  section and edit the template for . Replace the IP address accordingly. You can find the IP address on your printer screen. For example,

Meanwhile, comment out  in  as it conflicts with ImageScan.

Once this is done you can use any SANE frontend to access this scanner.

## Fujitsu
## Fujitsu fi series
For some of the Fujitsu fi series document scanners, the  proprietary driver offers advanced functionality over the already mature SANE default driver, such as control of an optional imprinter for stamping scanned documents or requesting accurate status of the consumables from the host.

## ScanSnap S300/S300M/S1100/S1300
For the operation of the ScanSnap scanners a firmware file is required, which can be downloaded from here or extracted from the Windows driver. Get the files that you need and put them in the  directory, which should be created if it does not exist. For instance, you should end up with a file called . These files should be owned by the root user.

To make sure that you have the right file in the right place, take note of the device ID:

 # sane-find-scanner
 found possible USB scanner (vendor=0x04c5 product=0x1200 [ScanSnap S1100) at libusb:003:011

There should be a corresponding entry in , such as , which in turn should reference the path of the firmware file that you just added.

For the S300/S300M scanners, the  and  files are interchangeable; the S300 device can use the  file and the S300M device can use the  file.  The file can be renamed to fit the entry in , or that entry can be edited to match the file name.

Alternative download locations for the firmware files: here and here.

Commands to fetch and install the firmware:

  # git clone https://github.com/stevleibelt/scansnap-firmware.git
  # mkdir -p /usr/share/sane/epjitsu
  # cp scansnap-firmware/*.nal /usr/share/sane/epjitsu

## HP
If your HP device is supported by hplip, install the  package.

It comes with several tools:

* hp-setup to add and setup the device
* hp-check to check the installation of all required dependencies to successfully run (a very helpful tool)
* hp-plugin is the 'HPLIP Plugin Download and Install Utility' (plugin also available from ).
* hp-scan is the 'HPLIP Scan Utility'. If you need that tool, you will need to install .

hp-setup runs in GUI mode by default, which requires . You can run the CLI by using the  flag.

If the device is connected by USB, run hp-setup as root and follow the on-screen instructions.

If your device is connected on the network, use  instead.

## Alternative way to scan with network HP scanner
* Find out IP address of your network HP scanner, for example 192.168.1.8
* Make device URI using hp-makeuri utility:

* This URI could be given to xsane or scanimage tools, for example:

 $ xsane "hpaio:/net/DeskJet_3630_series?ip=192.168.1.8"
 $ scanimage --device "hpaio:/net/DeskJet_3630_series?ip=10.12.129.6" --format=png --resolution 300 >scan01.png

## Lexmark
For Lexmark devices printing issues, please read CUPS/Printer-specific problems#Lexmark.

Most Lexmark scanners are still (2019) not supported by SANE, and thus cannot be detected either by  or by . Lexmark provides a non-free driver for GNU/Linux, which is supposed to support all its scanners. Nevertheless, the driver is only distributed for Debian, OpenSUSE, Fedora and Red Hat, but not for Arch. Here is a way to install it.

## Warning
Before following these steps, note that:

* This driver is non-free (copyrighted by Lexmark)
* This hasn’t been widely tested yet (but the driver is supposed to work for all Lexmark scanners)
* The tree does not respect Arch standards — namely, all will be installed in ; you’ll get a  symbolic link; and get symbolic links to the files installed in .
* This process might generate conflicts if you’ve already installed some Lexmark drivers.

## Process
# Ensure Java is installed.
# Download the file containing the driver and save it (eg at ).

## Option 1 : using DPKG
 is the standard package-manager for Debian-based distributions. It should not be used to replace  unless you precisely know what you’re doing.
Simply run as root

 # dpkg -i lexmark.deb

Your scanner should be detected after reboot.

## Option 2 : manual installation
Alternatively, if you dont want to install dpkg or wish to control exactly what is done during install, you can follow these instructions (assuming you’re working in ). Please note that  sums will not be checked, which could cause security issues.
# Extract the  archive, running . File  can be dropped.
# Extract both  and  archives.
#  gives a  directory. As root, move  to .
# As root, run  to perform install. This script will automatically set all files owners an , then set some fonts, drivers and docs tricks. It will also eventually run , creating several symbolic links in your Arch architecture.
# Your scanner should be detected after reboot.

## Option 3 : Using AUR package
Install the  package.

## Supported devices
This process has been successfully tested for the following devices:

* Lexmark MB2236 (USB only; network untested).
* Lexmark MX517de (network only; USB untested).
* Lexmark X204n (network only; USB untested).

## To do
In order to improve Lexmark scanners support, you can:

* Check whether this process works for your computer and device
* Help defining the list of dependencies required for this process
* Create an AUR package with this driver which installation would not mess architecture up. Namely, such a package should not need to create a  symlink, and should be containerized (eg in ).

## Medion
If you own the USB scanner MD 9705 from Medion, you need to download a suitable firmware binary. This firmware file is in the device driver for Windows.

Find out which model you own and take note of the USB ID:

Download the windows driver from https://download.medion.com/downloads/treiber/scamd9705w9xxp.exe

Then enter the following commands to extract the firmware file, and copy it to the location SANE expects it:

 $ unzip scamd9705w9xxp.exe Win2000/Artec48.usb
 # cp Win2000/Artec48.usb /usr/share/sane/artec_eplus48u/Artec48.usb

## Mustek
## BearPaw 2400CU
Works with sane-gt68xx ()

## Samsung
For some Samsung MFP printers you may need to edit .

Example entry:

 #Samsung SCX-3200
 usb 0x04e8 0x3441

Change the printer model as needed.  You can get the idVendor and idProduct code with . See this thread.

To access the scanner over the network rather than the usb interface, add a line to  such as

 #Samsung scx4500w wireless IP network address
 tcp xx.xx.xx.xx

where  is the static IP address of the printer.
