# Android Debug Bridge

The Android Debug Bridge——is a command-line tool, that can be used to install, uninstall and debug applications, transfer files and access an Android device shell.

See also the official guide.

## Installation
adb is a part of the  package and the Platform-Tools SDK package.

## Usage
## Connect a device
First you must enable Developer Mode on your device. To do so you must:

# Go to Settings > About Phone, tap Build Number seven times until you get a popup that you have become a developer. Build number may be under a menu called Software info on newer Android OS versions.
# Go to Developer Options and make sure Use developer options is on.

## USB
To connect to a real device via adb with USB, you must:

* Plug in your Android device via USB.
* Go to Developer Options > Debugging and enable USB debugging.
* The device will ask to allow the computer with its fingerprint to connect. Checking allowing it permanently option will copy  to the target device  location.
* If adb recognizes your device— shows it as —you are done. Otherwise see the instructions below and the #Troubleshooting section.

## Wi-Fi
To connect to a real device via adb with Wi-Fi, you must:

* Make sure your device is on the same Wi-Fi network as your computer.
* Go to Developer Options > Debugging and enable Wireless debugging. Device IP address and dynamic connection Port will be displayed.
* Tap Pair device with pairing code. Random Pairing code, device IP address and dynamic pairing Port will be displayed. This port will be different than the one provided to connection and will be changed for each pairing attempt.
* Run . See also .
* Run .
* You should see your computer listed under Paired Devices and your device listed in the  output.

Dynamic port for network connection will be changed if you:

* turn off Use wireless debugging and then turn on it again,
* disable Wi-Fi and then reconnect back,
* lock and then unlock your device.

To use specific port for network connection—restart the  daemon on your device so it will listen on the specific port, see also

 $ adb tcpip 5555 && sleep 1 && adb connect IP_address

## Transferring files
You can use adb to transfer files between the device and your computer. To transfer files to the device, use:

 $ adb push what_to_copy where_to_place

To transfer files from the device, use:

 $ adb pull what_to_pull where_to_place

Also see #Tools built on adb.

## udev rules
Each Android device has a USB vendor ID (VID) and product ID (PID). In the following example for HTC Evo vendor ID is 0bb4 and product ID is 0c8d:

See also , Hardware probe and the USB ID repository.

If your device USB ID is not included in the  package, use the following template to create a custom udev rule by replacing  and  with IDs of your device:

{{hc|/etc/udev/rules.d/51-android.rules|2=
ACTION!="remove", SUBSYSTEM=="usb", ATTR{idVendor}=="''VENDOR_ID''", MODE="0660", GROUP="adbusers", ENV{ID_DEBUG_APPLIANCE}="android"
ACTION!="remove", SUBSYSTEM=="usb", ATTR{idVendor}=="''VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID''", SYMLINK+="android_adb"
ACTION!="remove", SUBSYSTEM=="usb", ATTR{idVendor}=="''VENDOR_ID", ATTR{idProduct}=="PRODUCT_ID''", SYMLINK+="android_fastboot"
}}

Then reload the udev rules.

See also #no permissions.

## Backup and restore
You can also backup and restore your device with adb. Moreover, no root user is required to follow the process. The commands below led to backup your device to a single file which can also be successively restored. To see the help help message for  and  parameters, run .

The command parameters list for backup is:

 adb backup  [-shared|-noshared [-system|nosystem The command to create a backup is:

 $ adb backup -apk -shared -all -f backup_file_name.ab

Then confirm the process on your device's display and provide a password whether a backup password has been set before.

The command to restore a previous backup is:

 $ adb restore backup_file_name.ab

## Tools built on adb
*
*
*
*
*
*
*

## Troubleshooting
## Empty device list
Possible causes for your device to not show up.

USB connection:

* Not having enabled USB debugging on your device.
* Using a power only—charge-only—USB cable and not an USB data transfer cable.
* If you added udev rules, reloaded them, replugged your device, and adb still does not detect it— and restart the adb server as root user and check devices again:
:

Network connection:

* Connection was closed, because you use dynamic port for network connection and your device was locked.

## adb: more than one device/emulator
If you have several devices connected—i.e. the output of  contains more than one —then you can use the  environment variable to specify your desired device, for example:

 $ ANDROID_SERIAL=host:non-default_port adbfs mount_point

For more information, see [https://developer.android.com/tools/adb#directingcommands Send commands to a specific device.

## insufficient permissions
If you see following error when running adb:

 E adb     : usb_libusb.cpp:571 failed to open device: Access denied (insufficient permissions)

check if you are in  group.

## no permissions
If the device in the  output shows up with the  label, it probably has different vendor and product IDs with respect to the ones collected by . This can happen for instance when the device uses a custom ROM, or when it is switched from MTP to USB tethering mode, sideload and/or fastboot mode.

Verify the actual device USB ID and add udev rules.

## unauthorized
* If  shows  next to your device, make sure that that device has debugging permission allowed on the device itself:
** An Allow USB Debugging? dialog should be presented when you physically connect the device. Select Always Allow…, then tap OK.
** If the dialog was never presented, try Settings > Developer Options > Revoke USB Debugging Authorizations, then tap OK, and repeat the steps in the #Connect a device section.
* If you still do not see the Allow USB Debugging? dialog, and the device is listed as , then enter the Developer Options on the device and first uncheck USB Debugging and then check it again.

## Multicast DNS
Multicast DNS (mDNS) is not supported by —you will see the following error when running :

 error: unknown host service 'mdns:check'

and the following error when running :

 error: unknown host service 'mdns:services'

To use mDNS, switch to the  SDK package.

If you still encounter  — add the environment variable .
