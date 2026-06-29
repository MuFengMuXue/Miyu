# Palm

This guide is to help Arch users with Palm OS devices, made until 2011. Do not confuse them with Palm-branded devices made since 2018, they bear no relation to the original Palm devices. While installation in Arch is easy, it can be confusing for those who are new.

## Installation
You will need to install one of the various Personal Information Management (PIM) software packages:

*
*

## Finding your device
You can sync in two ways, either by using  (preferred) or by accessing /

## Checking the hardware
If you have a USB connection you can test it with lsusb which lists all the devices connected to the ports.

If your device is missing it may be one of those Palm Pilots (like the Zire 71) that only 'appears' on the system when it is actually transferring. In this case, press the transfer button on the cradle or "Hotsync" from the Palm Menus, type  again, and you should get a display which resembles this.

Then cancel the Hotsync on the Palm.

If you have a Serial Zire, it should be possible to test it by putting the Palm into hotsync and typing {{ic|cat  Preferences > Settings. On KPilot or Kontact it is Settings > Configure KPilot > Device''.

The Device setting should be  or , as noted above.

Next, on JPilot go to File > Install User and type the username on your palm. In KPilot simply set the Pilot User setting in the Device area.

Now, first start a hotsync on your palm, then click the hotsync button in JPilot or KPilot.  If all goes well, it will connect and start synchronizing.
This will be quick, as it just does contacts, addresses, etc.  The standards.
There are no special conduits in the standard Jpilot, such as Documents-To-Go, so either find those on the Internet (if they exist) or make them yourself.

Next, do the same thing, but click the button below, for backup.  On first run, this will take a long time, but well worth while.

That's it! You have successfully setup your palm device on Arch Linux.

## Hotsync over Bluetooth
Palm devices come with built-in networking capabilities, as well as Bluetooth. If you also own a laptop, or have a USB Bluetooth adaptor, syncing over bluetooth, while being noticeably slower, is probably more convenient than keeping your sync cable handy.

First, of course, you have to have bluetooth set up. Bluetooth provides the arch-specific guide to that, its currently quite short, but I had no problems following it. Of course, there is also the forums to ask for help.

Next, there is the actual setup for syncing. Basically, this involves setting up a small LAN over Bluetooth connection. I did this following the guide in the author of which followed the guide in [https://web.archive.org/web/20150906212522/http://howto.pilot-link.org/bluesync/index.html. Anyway, on to the real information.

First we would need to pair the Palm and your PC. If you are using Bluez, then use blueman-manager to search for your Palm (make sure bluetooth is turned on and not hidden), then pair them (the button is labeled 'bond', for some reason or other). You would need to type in a verification pass-key. Alternatively, from the palm, search for your PC's bluetooth and set it as a trusted device.

Next, on your Palm, go to Preferences->Connection and create a new connection, name it "Laptop Bluetooth" or whatever you like, set it to connect to a PC via Bluetooth, and select your PC from the list below. Next, you have to actually setup the network, going through Prefences->Network, create a new network, naming it again anything you want (I use "Linux"), select the connection you just created, and leave the user name and password blank (you could put something here, you would need to change the following steps accordingly though).

To set up your PC, first create the file /etc/ppp/peers/dun, with these contents:-
 115200
 10.0.1.8:10.0.1.40
 local
 ms-dns
 noauth
 debug

As root, edit the file /etc/ppp/pap-secrets, adding this line:-
 mylogin * mypassword *

In a terminal, run dund as root (prefix with sudo if you are not logged in as root). You would need to make sure the bluetooth daemon is already started at this point.
 dund --nodetach --listen --persist --msdun call dun

Click the 'Connect' button under Preferences->Networking for your Palm. In the terminal, some text should start scrolling, indicating a new connection, channels being used, and the sending and receiving of various packets. At this point, your connectivity is working fine.

For the Hotsync specific setup, navigate to 'Hotsync' on your palm, select 'Modem' instead of local. Go to the menu, and change the following preferences:-
 Modem Sync Preferences -> set Network instead of Direct to modem
 LANSync Preferences -> set LANSync instead of Local HotSync
 Primary PC Setup -> Set the Primary PC Name and Address to 10.0.1.8, according to the settings previously in /etc/ppp/peers/dun
 Connection Setup -> select the connection you previously created (Laptop Bluetooth, for example)

Under the Hotsync button, if the name you previously assigned to your network does not show ("Linux" in this example), select that area and it should automatically show "Linux". You are now ready to HotSync. Make sure dund is running, run your preferred sync-ing program using the interface net:any (I use JPilot, under File->Preferences->Settings->Serial Port I select 'other' and specify 'net:any'), and then click on the HotSync icon on your Palm. Enjoy wireless sync-ing.

## Palm T|X
In addition to USB and Bluetooth, the Palm T|X model includes Ethernet connectivity. To sync the device using a direct Ethernet connection with , simply set the serial device to net:any in the Preferences dialog and then hotsync. On the Palm, you will need to select the name/ip address of the machine where  is running and then start the hotsync. Enjoy high speed wireless hotsync-ing.

## Palm Centro
The  module does not currently work with the Palm Centro. It is not needed, as newer software accesses the Centro through . To make the Palm work under Arch, blacklist the  module. You may have to reboot for this change to take effect.

When udev creates a device node for the Centro, it by default assigns it owner and group to root. You need to create a non-root group for udev to use for this device and make sure you are a member:

 # groupadd palm
 # usermod -a -G palm username

You will need to logout and re-login for the new group assignment to take effect. After you do, you should see  in the list of groups when you run the  command.

You now need to tell udev how to assign the Centro to the group  when it is attached. Create the following file:

{{hc|/etc/udev/rules.d/55-palm-centro.rules|2=
ACTION=="add", SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", \
ATTR{idVendor}=="0830", ATTR{idProduct}=="0061", \
NAME="bus/usb/$env{BUSNUM}/$env{DEVNUM}", MODE="0664", GROUP="palm"
}}

Now plug in the device. Verify that a device has been added which has group :

 $ find /dev -group palm

The device name does not really matter, as  will find it when needed.

To sync the device, if using , simply specify  as the serial port in preferences.

## Troubleshooting
If you get a message such as stating that you do not have proper permissions, you probably need to add your user to a group with the proper permissions. This may be 'usb' or 'uucp'.

 # gpasswd -a username usb

or

 # gpasswd -a username uucp

Also, your software may have difficulty finding the device.

 $ ls -l /dev/pilot

or

 $ ls -l /dev/palm

may help you to discover a different name for the device. Output may look like this:

 lrwxrwxrwx 1 root root 8 2002-01-03 16:13 /dev/pilot -> tts/USB1

Now change the Device setting (as above) to  or .
