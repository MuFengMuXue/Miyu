# ZTE MF 823 (Megafon M100-3) 4G Modem

## Installation
As described below,  will likely comes out handy. Install it.

## Device identification
When the device is switched to an  product code you will get:

Here are the USB product codes for this device:

; 1225: Default mode in which the device looks like a USB Mass Storage Device with CD-ROM interface, and a card reader. Corresponds to AT+ZCDRUN=9+AT+ZCDRUN=F

; 1403: A Communication mode in which the device has an wikipedia:RNDIS like interface in addition to the card reader interface. The non recommended kernel module rndis_host might handle such an interface. Corresponds to AT+ZCDRUN=8+AT+ZCDRUN=F.

; 1405: A communication mode in which the device has a wikipedia:USB communications device class interface in addition to the card reader interface. Communications Device Class (CDC) should work in Linux. The cdc_ether kernel module is required. This mode will be the one  will switch the device into.

; 0016: Download Mode. Under the name of ZTE., but simply a mode where available diagnostic port and two command (analog modem port and PC UI devices Huawei). Corresponds to AT+ZCDRUN=E

; 0076: "real" Download Mode. Includes a standard for devices running QC methods.

If your modem does not appear as  (or ), check the USB 3G Modem#Mode switching article.

## Ethernet connection established
When the device has an Ethernet interface the usual Network configuration programs should handle it. When they are, you will see that the LED (Blue - 2G/3G or Green - 4G) on modem is not blinking. To establish a connection, the following link (CGI command) should be entered in a browser:

http://192.168.0.1/goform/goform_set_cmd_process?goformId=CONNECT_NETWORK

To avoid entering this link every time, switch the device to auto-connection mode:

http://192.168.0.1/goform/goform_set_cmd_process?goformId=SET_CONNECTION_MODE&ConnectionMode=auto_dial

If you are setting up internet using a command-line shell you should make request with referrer, as in:

 curl --header "Referer: http://192.168.0.1/index.html" http://192.168.0.1/goform/goform_set_cmd_process?goformId=CONNECT_NETWORK

otherwise you will get response {"result":"faulure"}

## Commands
CGI command for 2G/3G/4G mode selection:

following options available after "=" sign (case-sensetive)

This should be followed by the NETWORK CONNECT CGI command given before.

To switch the modem to FACTORY mode (WARNING! Unable to recieve further CGI commands, connection will be lost!), issue this link:

You may then need to run the following command (as root) in order to access the AT command serial port:

The port should appear as , e.g. . When you discover the command port, you can use your favourite serial terminal emulation program to control the device. The commands below may be especially useful (here shown with modem-cmd):

## Telnet connection
The modem is available for telnet connection:

 telnet 192.168.0.1
 login: root
 password: zte9x15

As you can see, the modem has an embeded Linux system inside. You can even install some ARM-base packages (mc, nano...) or change something in Web-menu. Explore it carefully!

## Possible usage with product code 1403
For some reason this device can get stuck in mode 0016 and fails to switch to any other mode. I was unsuccessful in trying to switch modes using  or sending AT commands to /dev/ttyUSB0 on various Linux systems. I successfully managed to change modes from 0016 to 1403 using Mac OSX. I was then able to use the dongle on Linux.

In mode 0016 on OSX you will see the follow interfaces:

 /dev/tty.ZTEUSBATPort_
 /dev/tty.ZTEUSBModem_
 /dev/tty.ZTEUSBDIAGPort_

You can switch modes to 1403 by sending AT commands to the USBModem_ port by doing:

 screen /dev/tty.ZTEUSBModem_ 9600

 >>ATI
 Manufacturer: ZTE CORPORATION
 Model: MF823
 Revision: MF823_T03
 IMEI: 866948013728723
 +GCAP: +CGSM

 >>AT+CREG?
 +CREG: 0,1
 OK

 >>AT+COPS?
 +COPS: 0,0,"Telstra Mobile",7
 OK

 >>AT+ZCDRUN=8+AT+ZCDRUN=F
 exit download mode result(0:FAIL 1:SUCCESS):1
 OK

Now the device should act as a ethernet interface no matter which system you plug it into.
