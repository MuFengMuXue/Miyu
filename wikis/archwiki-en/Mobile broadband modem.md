# Mobile broadband modem

A number of mobile phone carriers around the world offer internet access via mobile broadband (e.g. LTE, UMTS, EDGE, GSM, etc.).

This article focuses on mobile broadband modems in the format of portable USB devices and mini PCIe cards. For standalone mobile broadband routers, simply connect to them using an interface they provide (e.g. Ethernet or Wi-Fi).

## Device identification
Install .

Examine the output of:

 $ lsusb

and

 $ lspci -nn

which will show the vendor and product IDs of the device. Note that some devices will show two different product IDs at different times as explained below.

## Mode switching
## From mass storage mode
Often these devices will have two modes (1) USB flash memory storage (2) USB modem. The first mode, sometimes known as ZeroCD, is often used to deliver an internet communications program for another operating system and is generally of no interest to Linux users. Additionally some have a slot into which the user can insert an additional flash memory card.

A useful utility for switching these devices into modem mode is . It ships with udev rules  that contain entries for many devices, which it will switch to modem mode upon insertion.

When a device is switched, its product ID may change to a different value. The vendor ID will remain unchanged. This can be seen in the output of .

Some devices are supported in the USB serial kernel module called  (named after the "Option" devices, but not limited to just those) and may be used without usb_modeswitch.

## From router mode
Depending on the device, it may expose an Ethernet network interface or provide Wi-Fi. In that case you will need to have the interface up. If the device has a DHCP server, you can use a DHCP client to match it. Otherwise, you will have to have some knowledge about the network the device expects. Such information might be obtained from its behavior in another OS. Or by searching the web. Or from the drivers, and other information, stored in the initial USB flash memory storage (ZeroCD). Some Huawei HiLink devices, for example, sometime operate at 192.168.8.0/24, with a gateway at 192.168.8.1. They also might have a web interface at http://192.168.8.1.

## Modem mode
In general, at this point you should note if mode switching left you with additional  serial device and a  network interface. You can do that with journalctl or by shell commands such as:

 $ ls /dev/ttyUSB*
 $ ip link

## Remove the PIN
First of all use your SIM card in a normal phone and disable the PIN request if present. If the SIM card asks the PIN wvdial will not work.

Failing that, you can use mmcli (provided by ) or AT commands, to unlock the SIM card.

## Using mmcli
First, list the modems and find the modem's index:

 $ mmcli -L

Look for .

Find the SIM card index:

 $ mmcli -m MODEM_INDEX

Just as with the modem index, look for .

Unlock the SIM card:

 $ mmcli --sim=SIM_INDEX --pin=PIN

Remove the requirement for PIN:

 $ mmcli --sim=SIM_INDEX --pin=PIN --disable-pin

## Using AT commands
Follow the instructions in https://unix.stackexchange.com/a/313878.

## Connection
To connect to the mobile network, use one of the following methods.

## ModemManager
ModemManager is a system daemon which controls WWAN devices and connections.

Install the  and  packages.

Start and enable .

Use  to communicate with the modem.

The simplest way to establish a connection is to use mmclis  option.

First, list the modems and find the modem's index:

 $ mmcli -L

Look for .

Next connect to the mobile network. For example:

 $ mmcli -m MODEM_INDEX --simple-connect="apn=internet.myisp.example"

Replace  with your ISP's provided APN. If a user name and password is required, set them accordingly:

 $ mmcli -m MODEM_INDEX --simple-connect="apn=internet.myisp.example,user=user_name,password=password"

To disconnect from the mobile network run:

 $ mmcli -m MODEM_INDEX --simple-disconnect

See also .

## NetworkManager
NetworkManager uses ModemManager to work with mobile broadband modems. See NetworkManager#Mobile broadband support.

## libmbim
Install . To bring up the modem you can use  which is a wrapper for  calls. First create a profile for mbim-network.

Now connect to the network with:

 # mbim-network /dev/cdc-wdmX start

Then follow Network configuration to bring up the  interface and get an IP address using DHCP.

## pppd
pppd can be used to configure 3g connections. Step by step instruction is available on 3G and GPRS modems with pppd. Optionally,  can be used to simplify the pppd configuration using dialog interface.

## wvdial
See main article: wvdial

## netctl
Netctl can be used to establish a connection using a USB modem. An example configuration file provided by  is located at . Minimally you will probably have to specify

See the netctl article and  for more information.

## Tips and tricks
## Disable mode switching
Some ways to disable  from operating on a device before the device was inserted, for example to be able to read the initial flash memory (ZeroCD), are:

## By the configuration file
## With a udev rule
Masking the udev rule the package is using can be achieved with

 # ln -s /dev/null /etc/udev/rules.d/40-usb_modeswitch.rules

## AT commands
There are some useful commands:

*  - the device is only Modem
*  - device is in modem mode + CD ROM
*  - the device in modem mode + CD ROM + Card Reader
*  - the device in modem mode + Card Reader
*  - enter PIN-code
*  - USSD request, result can be found (probably) in .

Encode  to PDU format:

 $ perl -e '@a=split(//,unpack("b*","*100#")); for ($i=7; $i activate sms reading". Your messages will show up in the window.

Command line script:

A small command line script using gnokii to read SMS on your SIM card (not phone memory) without having to start a GUI:

 $ gnokii --getsms SM 0 end 2>&1|grep Text -A1 -B3|grep -v Text

What it does:

Granted this does not work very well if your SMS contains the word "Text", but you may adapt the script to your liking.

Another option is to use , you can use simple bash script like this one that is also used to write messages or this one below:

{{bc|
#!/bin/sh
#get modem number
MODEMNO=$(mmcli -L | grep -o "Modem/| grep -o [0-9$)
#list all SMS messages, and select this with highest id (usually newest one)
SMSNO=$(mmcli -m ${MODEMNO} --messaging-list-sms | awk '/received/{split($1, ar, /\//); print arexit}')
#read message with highest id
mmcli -m ${MODEMNO} -s ${SMSNO}
}}

## With email like web interface
Some Devices, such as some Huawei HiLink, include an email like web interface for SMS. It is included in the device internal web server, which is used for other purposes too.

## Writing SMS
{{bc|
#!/bin/sh
#get modem number
MODEMNO=$(mmcli -L | grep -o "Modem/[0-9" | grep -o #create sms in modem and get number
SMSNO=$(mmcli -m ${MODEMNO} --messaging-create-sms="text='$1',number=+$2" |  grep -o [0-9*$)
#send message
mmcli -s ${SMSNO} --send
# delete all sent messages
for i in $(mmcli -m ${MODEMNO} --messaging-list-sms | grep " (sent)" | cut -f5 -d' ') ; do
    mmcli -m ${MODEMNO} --messaging-delete-sms=$i
done
}}

You may need give permission by creating file with content like

{{hc|/etc/polkit-1/rules.d/49-nopasswd_mmcli.rules|
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.ModemManager1.Messaging" &&
        subject.isInGroup("uucp"))
    {
        return polkit.Result.YES;
    }
});
}}

## Commands to restart the device
Unplugging, and plugging, the device is sometimes used to restart the USB device. The following describes how to do that from the shell. Doing that from the shell might be useful, if, for example, the plug is at the rear side of the PC. The method described is not just for USB modems. It should be good for many other USB devices.

The important part is that the requirements are for the USB bus, and the port, the device is attached to. There could be one, or more, sub ports too. Suppose I obtained bus 2 and port 4, without sub ports, for my device from the output of . This information is also recorded in the journal. With

 $ cat /sys/bus/usb/drivers/usb/2-4/product

I can verify it is the intended device.

The following sequence will restart the device:

Some more comments are at, for example, https://askubuntu.com/questions/1036341/unplug-and-plug-in-again-a-usb-device-in-the-terminal.

## Troubleshooting
## Connection halts after few minutes running
This problem commonly occurs on some modems which locked by a mobile operator. You can successfully connect to the internet but after few minutes connection halts and your modem reboots. That happens because an operator built a some checks into modem firmware so a modem checks if a branded software is running on your pc, but usually that software is Windows-only, and obviously you do not use it. Fix (it works on ZTE-mf190 at least) is simple - send this command through serial port (use minicom or similar soft):

 AT+ZCDRUN=E\r\n

This command will delete a  file in the modem's filesystem - it will disable such checks.

Another possibility for such disconnections is to help the customer save bandwidth, which might be expensive. With Huawei HiLink devices with a web interface, there might be an option there to set a longer period of inactivity before the connection hangs up.

## Low connection speed
Someone claims that the connection speed under Linux is lower than Windows This is a short summary for possible solutions which are not fully verified.

In most of conditions, the low speed is caused by bad receiver signals and too many people in cell. But you still could use the following method to try to improve the connection speed:

* QoS parameter can be set with the  and  commands. It should also be possible to decrease and limit the connection speed. Add the following  command in :

 Init6 = AT+CGEQMIN=1,4,64,640,64,640
 Init7 = AT+CGEQREQ=1,4,64,640,64,640

* Baud parameter in  could be used to increase the connection speed:

 Baud = 460800

It is advisable to see the baud rate set by the official modem application for Windows (possibly  on Vista).

## Fix image quality
If you are getting low quality images while browsing the web over a mobile broadband connection with the hints  and , follow these instructions:

Install .

Edit  and insert the following two lines:

 AddHeader "Pragma" "No-Cache"
 AddHeader "Cache-Control" "No-Cache"

Start

Configure your browser to use  as a proxy server and you are all done. This is especially useful if you are using, for example, Google Chrome which, unlike Firefox, does not allow you to modify the Pragma and Cache-Control headers.

## ModemManager does not recognize the modem
In case ModemManager does not recognize the modem, check the unit status of . If you get error messages such as  and , you may have to whitelist your device using the [https://www.freedesktop.org/software/ModemManager/api/latest/ref-overview-modem-filter.html ModemManager filter rules.

## FCC locking
The FCC lock is a software lock integrated in WWAN modules shipped by several different laptop manufacturers like Lenovo, Dell, or HP. This lock prevents the WWAN module from being put online until some specific unlock procedure (usually a magic command sent to the module) is performed.

Since release 1.18.4, the ModemManager daemon no longer automatically performs the FCC unlock procedure ModemManager will keep on providing support for the known FCC unlock procedures, but [https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/685 no longer automatically: the user must install and select the FCC unlock procedure needed in the specific laptop being used. This applies to: EM7355, MC8805, MC7355, EM7455, SDX55, EM120.

The  package ships several scripts installed under  and named as  with either the PCI or USB vendor and product IDs. However, they are not used if they are not in the  directory.

For each device the  can be found in the brackets at the end of the line:

 # lspci -nn

To enable unlock script for the device it must be symlinked like so:

 # ln -sft /etc/ModemManager/fcc-unlock.d /usr/share/ModemManager/fcc-unlock.available.d/vid:pid

For a Quectel EM120 modem that would be:

 # ln -sft /etc/ModemManager/fcc-unlock.d /usr/share/ModemManager/fcc-unlock.available.d/1eac:1001

See the ModemManager documentation for more information.

## NetworkManager: Device not available / rfkill block
If NetworkManager persists on that the device (e.g. /dev/cdc-wdm0) is not available while ModemManager can use it, it could either be, that the device is blocked using a hardware switch, by rfkill or just NetworkManager believes that.

Check rfkill with:

 # rfkill
 ID TYPE      DEVICE                   SOFT      HARD
  0 bluetooth tpacpi_bluetooth_sw unblocked unblocked
  1 wwan      tpacpi_wwan_sw      unblocked unblocked
  2 wlan      phy0                unblocked unblocked
  8 bluetooth hci0                unblocked unblocked

The wwan device should be listed as unblocked for both SOFT & HARD. If it is HARD blocked, a hardware switch blocks the device. If it is SOFT blocked, unblock it using:

 # rfkill unblock wwan

If NetworkManager still declares the device not available, it could be that NetworkManager is not synced with rfkill. Check that using:

 $ nmcli radio
 WIFI-HW  WIFI     WWAN-HW  WWAN
 enabled  enabled  enabled  enabled

If WWAN is listed as disabled, enable it using:

 $ nmcli radio wwan on

## ModemManager connects successfully but the interface does not show any IP address
This has been reported to happen on some LTE modems with buggy or incompatible firmware versions. In this scenario, when inspecting the bearer with:

 $ mmcli -m modem index -b 1

It can be seen how the IPv4 configuration section shows no IP address, and may show  as the  despite the associated interface (e.g. ) not being dhcp-capable. In this cases, the modem firmware is not behaving correctly and it should be upgraded.
