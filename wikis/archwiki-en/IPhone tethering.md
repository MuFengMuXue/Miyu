# IPhone tethering

Unless disabled by your provider, it is possible to share your iPhone's mobile data connection over Wi-Fi, USB or Bluetooth:
* Wi-Fi requires no additional configuration provided your computer can connect to wireless networks,
* Instructions for USB and Bluetooth tethering are provided below.

## Tethering over USB
Tethering natively over USB is the optimal choice as it provides a more stable connection and uses less batteries than Bluetooth or Wi-Fi.

To tether your iPhone over USB, you will need to install  and . The usbmuxd package depends on libimobiledevice, which is responsible for performing the low-level connection to iOS devices. The usbmuxd package also includes an udev rule that automatically starts and stops the daemon whenever a device is connected or disconnected. See iOS for more details.

Connect the iOS device and verify that  is automatically started.

Next enable Personal Hotspot on your iPhone and plug it into your computer. At this point you will have a new Ethernet device available and should be able to use any network manager to connect to the internet through the new iPhone Ethernet device, just like you would any other Ethernet connection.

If you are MAC address spoofing you might want to add an exception for the  driver since it does not support MAC cloning:

## Using systemd-networkd
If systemd-networkd is used for network management, you can easily configure it to connect to the internet through the iPhone, as you would with any other adapter.

If for example enp0s26u1u2c4i2 is the name of the network device that is created from the iPhone as displayed by , create the following .network file:

## Troubleshooting
If the iPhone appears in the device list but does not connect, it is possible that you may need to connect your iPhone and pair it with your computer before connecting (iPhones using a PIN unlock?):

 # idevicepair pair

## Driver missing
If you have followed all the above steps and commands:  still does not detect the iPhone, the ipheth driver is probably missing. You can check if you have the driver installed by running the  command. If an error message appears, set the  flag when building the kernel. This problem can occur when building your own kernel.

## Tethering over Bluetooth
Tethering over Bluetooth will drain the batteries relatively quickly, but simultaneous charging from an USB port works well.

## Hardware Requirements
* iPhone running OS 3.0 with tethering enabled. See Settings > General > Network and turn on the tethering option.
* Bluetooth adapter or similar, preferably with EDR (Enhanced Data Rate) for acceptable speeds. Tested with a Belkin F8T016NE.

## Setup
See the main article Bluetooth and setup the bluetooth daemon.

## Gnome/XFCE
Install the Blueman GTK Bluetooth manager.

A Bluetooth icon should appear in your notification area. Note: the icon may not appear if bluetooth was not turned on at startup. Click it, and search for nearby devices, adding your iPhone (note, you may need to have the Bluetooth setting screen up on your iPhone for discovery to work).

Once the iPhone has been added to the devices list, open the Device menu and select pair. This will require the usual entering of a PIN on the computer then the iPhone. Now open the Device menu again, and choose Network Access > Network Access Point. If everything goes well, blueman reports a success and the status bar on your iPhone should glow blue, indicating a successful tether.

Blueman will have created a new network interface, typically bnep0. To connect to it, run the following as root.
 # dhcpcd bnep0

## netcfg
Alternatively,  you can create a netcfg network profile to allow easy tethering from the command line,  without requiring Blueman or Gnome.  Assuming an already paired iPhone with address '00:00:DE:AD:BE:EF',  simply create a profile in  - for example - 'tether':

  CONNECTION="ethernet"
  DESCRIPTION="Ethernet via pand tethering to iPhone"
  INTERFACE="bnep0"
  IPHONE="00:00:DE:AD:BE:EF"
  PRE_UP="pand -E -S -c ${IPHONE} -e ${INTERFACE} -n 2>/dev/null"
  POST_DOWN="pand -k ${IPHONE}"
  IP="dhcp"

Then, execute:
 # netcfg tether

To bring the interface down and un-tether:
 # netcfg down tether
