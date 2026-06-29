# ZTE MF110/MF190

The ZTE MF110 / MF190 is a USB modem which combines 3G+/3G with EDGE/GPRS in one compact device. It has an integrated micro-SD card reader. It can send data at speeds up to 4.5 Mbps on 3G+ networks and receive data at speeds of up to 7.2 Mbps.

## Configuration
## Switch from CD mode to modem mode on the device
When you first plug the device, it is identified as a USB SCSI CD-ROM. You can find out the name of the device by using dmesg:

The dongle is identified this way:

The easiest way to switch to modem mode is by ejecting the CD-ROM:

 $ eject /dev/sr1

After that, the led will turn off. A few seconds later, it will turn on again and it will be identified as modem by the kernel:

## Disable CD mode on the device
Using a Windows machine, plug in the USB device and go through the short install wizard.  Once done, close the Rogers app that starts up, then head into the Device Manager (Control Panel > System > Hardware > Device Manager).  Under the Ports section, find the COM port that's connected to the USB modem (ignore the Diagnostics mode).  Connect to that COM port through Hyperterminal, found in the Accessories area of the Start Menu.  Connection parameters are:

 Bits per Second: 115200
 Data bits: 8
 Parity: None
 Stop bits: 1
 Flow Control: None

Once connected, type the following commands:

 AT+ZOPRT=5
 AT+ZCDRUN=8

This tells the modem not to use CD mode when it is first plugged into a computer.  Now exit Hypterterminal and remove the USB modem.  You are done with Windows.

## Disable CD mode on the device with wvdial
First remove the  module then run :

 # rmmod usb_storage
 # modprobe usbserial

Edit :

 Defaults
 Modem = /dev/ttyUSB0
 Modem Type = Analog Modem
 ISDN = 0
 Init1 = AT+ZOPRT=5
 Init2 = AT+ZCDRUN=8

Run , it should use those commands and fail to connect. Once it exits, unplug the stick and plug it back in and it should be seen as a modem.

## Setup udev rules
Create the following udev rule:

{{hc|/etc/udev/rules.d/90-zte.conf.rules|2=
# This is the Modem part of the card, let us load usbserial with the correct vendor and product IDs so we get our usb serial devices
ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="19d2", ATTRS{idProduct}=="0124", RUN+="/sbin/modprobe usbserial vendor=0x19d2 product=0x0124", MODE="660", GROUP="network"
# This is the ZeroCD part of the card, remove the usb_storage kernel module so it does not get treated like a storage device
#ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="19d2", ATTRS{idProduct}=="0150", RUN+="/sbin/rmmod usb_storage"
# This is the ZeroCD part of the card
ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="19d2", ATTRS{idProduct}=="0150", RUN+="/usr/bin/eject /dev/sr1"
}}

## Create a wvdial configuration
Wvdial is an easy-to-use frontend to PPPd.  The configuration is fairly easy to comprehend.  Make sure you replace the  line with the node that your USB modem is connected to, you can see that with dmesg.  Save as :

 Defaults

 ; Disable usb CD-ROM
 ; Init1 = AT+ZCDRUN=8

 ; Enable usb CD-ROM
 ; Init1 = AT+ZCDRUN=9

 Modem = /dev/ttyUSB2
 Modem Type = Analog Modem
 ISDN = 0
 Baud = 7200000
 Dial Attempts = 3
 Username = MOVISTAR
 Password = MOVISTAR
 APN = movistar.es
 Phone = *99***#
 Auto Reconnect = off
 Stupid Mode = 1
 Init1 = AT+CPIN=YOUR PIN HERE!
 Init2 = ATZ
 Init6 = AT+CGEQMIN=1,4,64,640,64,640
 Init7 = AT+CGEQREQ=1,4,64,640,64,640

## Connect to the internet
Now just run  to connect:

 # wvdial

If you see output reporting your PPP local and endpoint IP addresses, then it worked.
