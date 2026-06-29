# Android tethering

Tethering is a way to have internet access on your PC through your smartphone using its network connection. USB tethering and Wi-Fi access point tethering are natively supported. USB reverse tethering—to have internet access on your smartphone through your PC—is also possible.

## Natively
## USB tethering
USB tethering is available since Android 2.2 "Froyo" and usually provides a more reliable connection than Wi-Fi while being faster than Bluetooth. Since USB tethering is a wired method, it also consumes less power than wireless methods for a comparable connectivity quality.

* Connect the phone to your computer via USB (the USB connection mode -- Phone Portal, Memory Card or Charge only -- is not important, but please note that you will not be able to change the USB mode during tethering)
* Enable the tethering option from your phone. This is usually done from one of:
** Settings > Wireless & networks > Internet tethering (or Tethering & portable hotspot, for more recent versions)
** Settings > More... > Tethering & mobile hotspot > USB tethering
* Install the  package. See Mobile broadband modem#Mode switching for more information.
* Follow Network configuration.

If you are using a cellular data plan and you have recently entered a new billing period, you may need to restart your phone.

## Using systemd-networkd with udev
Using systemd-networkd you can automatically adjust the networking to use the phone as the gateway when plugged in.

{{hc|/etc/udev/rules.d/90-android-tethering.rules|2=
# Execute pairing program when appropriate
ACTION=="addremove", SUBSYSTEM=="net", ATTR{idVendor}=="18d1", ENV{ID_USB_DRIVER}=="rndis_host", SYMLINK+="android"
}}

You may have to adjust the  attribute depending on your phone. You can check using udevadm:

 $ udevadm info /sys/class/net/enp0s26u1u2

Then create the corresponding systemd-networkd file:

## Wi-Fi access point
Using an Android phone as a Wi-Fi access point (to a 3G/4G mobile internet connection) is available for devices running Android 2.2 "Froyo" or newer.

Enable it via one of the following:

* Settings > Wireless & networks > Internet tethering > Wi-Fi access point
* Settings > More... > Tethering & mobile hotspot > Mobile Wi-Fi hotspot

## Tethering via Bluetooth
Android (from at least 4.0 onwards, possibly earlier) can provide a Bluetooth personal-area network (PAN) in access point mode.

NetworkManager can perform this action and handle the network initialisation itself; consult its documentation for more details.

Alternatively: pair and ensure you can connect your computer and Android device, as described on Bluetooth, then, substituting the address of the Android device (here given as ), do:

 $ dbus-send --system --type=method_call --dest=org.bluez /org/bluez/hci0/dev_AA_BB_CC_DD_EE_FF org.bluez.Network1.Connect string:'nap'

This will create a network interface .  Finally, configure a network connection on this interface; Android offers DHCP by default.

## USB tethering via Android apps
Many cell carriers treat hotspot data independently from the data used by the phone itself. Unless one is subscribed to a data plan that includes hotspot data, native Android tethering may not be available or will be throttled to impractically slow speeds. Some apps have been created to work around this problem.

## Tetrd
Tetrd is a newer USB tethering app for Android featuring bidirectional tethering and functions without USB debugging or requiring root privileges to run on Linux. Like EasyTether, it requires payment to use its full functionality.

Get the Tetrd Linux server software and install it via:

 # pacman -U tetrd.linux_amd64.pkg.tar.xz

Once installed, Tetrd should be accessible from the applications menu of your desktop environment. Make sure the Tetrd android app is installed on your phone. Then, open Tetrd on your PC and connect your phone. When connected, Tetrd should appear automatically, prompting the user to run in either normal or reverse tethering modes.

## Reverse tethering
Reverse tethering is to provide internet connection to Android through PC.  and Tetrd provide reverse tethering.

Connect your phone to your computer via USB like mentioned above and start:

 $ gnirehtet run

## Tethering with SOCKS proxy
With this method tethering is achieved by port forwarding from the phone to the PC. This is suitable only for browsing. For Firefox, you should set  to  in  ( address bar )

## Tools needed
* The  and  packages
* USB connection cable from your phone to PC
* Either Tetherbot, Proxoid, or Android Proxy Server

## Instructions
## Tetherbot
Tetherbot is an experimental SOCKS proxy and Port Bouncer that should allow you to connect your laptop to the internet using the internet connection (EDGE, 3G or Wifi) of your T-Mobile G1 Cellphone. It is discontinued and its website is down, but still can be accessed from Wayback Machinewhere its APK can also be downloaded from.

In order to do SOCKS proxy via Tetherbot to connect your browser to the Internet, do:

# For your phone, open the application Tetherbot, decline Phone & Storage permissions, and press the Start Socks button
# Forward the port to your local computer:
# Now go to your web browser's proxy settings, set a manual proxy configuration with the proxy host address  and port , leaving the rest blank.

## Proxoid
Follow the instructions demonstrated in the following [https://www.linux-magazine.com/Online/Blogs/Productivity-Sauce/Tether-an-Android-Phone-Using-Proxoid link.

## Android Proxy Server
Currently available on the Google Play store and supports HTTP/HTTPS, Socks5, Shadowsocks, and TCP Relay proxies.

To initiate a SOCKS proxy to connect your browser to the Internet, do:

# Open the app Android Proxy Server, and enable the Socks5 Proxy ticker
# Forward the port to your local computer:
# Now go to your web browser's proxy settings, set a manual proxy configuration with the proxy host address  and port , leaving the rest blank.
