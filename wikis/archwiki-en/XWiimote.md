# XWiimote

This article is about the Nintendo Wii Remote Linux kernel driver. This driver is part of upstream Linux since version 3.1. It is an easy to use drop-in replacement for the older user-space drivers like cwiid.
You can use your Wii Remote for all purposes with this driver, for instance as an X input device or joystick controller for your Linux games.

## Prerequisites
* Bluetooth
*
* xwiimote kernel driver
* Wii Remote hardware

The most important software required is Bluetooth, please make sure you have read the wiki page about it and you have configured it before proceeding.

The user-space utilities are available as the  package.

The kernel driver (module ) is part of upstream Linux since version 3.1 and it is ever since already included in Arch Linux kernel. However, the module could need to be loaded:

 # modprobe hid-wiimote

Lastly you will need a Wii Remote, this can include (although, are not required) the Nunchuk and Classic Controller attachments.

## hid-wiimote kernel module
If you are using a custom kernel, you can enable the  module with  and the dependencies , ,  and  embedded in your kernel or as modules, previously loaded. Starting with kernel version 3.3, there is an additional configuration option  which is enabled by default. It controls whether wiimote extensions like Nunchuck and Classic Controller should be supported.

## Connect the Wii Remote
You can connect to your Wii Remote like any other Bluetooth device. See Bluetooth for information on pairing Bluetooth devices. The Wii Remote does not need special handling anymore. The BlueZ wiimote plugin handles all peculiarities in the background for you.

The Wii Remote can be put into discoverable mode by pressing the red sync-button behind the battery cover on the back. The Wii Remote will stay in discoverable mode for 20s. You can also hold the 1+2 buttons to put the Wii Remote into discoverable state. However, the first method works more reliably!

If you are asked for PIN input while bonding the devices, then your BlueZ bluetoothd daemon does not include the wiimote plugin. See #BlueZ does not include the wiimote plugin for more information. If this does not help, you can still connect to your Wiimote without pairing/bonding (i.e. not using authentication with a PIN). This should work with any BlueZ version. See #Cannot connect Wiimote if you still cannot connect your Wiimote.

## Device Handling
If your Wii Remote is connected, it will appear with several input devices inside . You can list all Wii Remotes with:

 $ ls /sys/bus/hid/devices

Then you can get additional device details with:

 $ ls /sys/bus/hid/devices//

The default mapping for the input-keys of the Wii Remotes are not very useful. User-space applications exist that re-map the Wii Remote input to more useful keys/actions - available with . If you installed this package you can test your connected Wii Remotes with the  tool:

This will list all connected Wii Remotes:

 $ xwiishow list

If this shows a path to a Wii Remote (lets say ) then you can test the device with:

 $ xwiishow /sys/bus/hid/devices/

Or use the index of the listed device:

 $ xwiishow 1

This will display a picture of the Wii Remote and notify you if buttons are pressed. You can use the  key to enable/disable the rumble motor. Press  to quit the application. You might need to be root to use these tools.

If the Wii Remote is showing button presses in the  tool but not registering otherwise, it is likely you need to add your user to the  group.

 # usermod -aG input username

## X.Org Input Driver
There is an X.Org input driver [https://github.com/dvdhrm/xf86-input-xwiimote available with  which automatically provides an input device to your X clients. Install it and read the related man-page for more information:

 $ man xorg-xwiimote

## Infrared Sources
The Wii Remote includes an infrared camera. To use this camera as a pointer input device, you need an IR-rack as an infrared source. Possible infrared sources are:

* Nintendo Wii Sensor Bar
* Wireless sensor bar - check eBay!
* Small candles (should have about 30cm distance)
* Home made sensor bar (There is currently no user-space application that enables mouse-emulation with the IR-sensor. If you need that, you should consider using the no longer supported cwiid approach. However, the xwiimote tools are under heavy development and will soon support IR mouse-emulation, too.

## Troubleshooting
## The input mapping is very weird
The default mapping maps the Wii Remote keys to the key-constants which resemble the Wii Remote's buttons best. This mapping is quite useless by default. To get better mappings, use the xwiimote userspace tools. Installing  will add an [https://github.com/dvdhrm/xwiimote/blob/master/res/50-xorg-fix-xwiimote.conf Xorg configuration file that disables the default mapping.

## BlueZ does not include the wiimote plugin
Upstream BlueZ includes the optional wiimote plugin since version 4.96. However, it must be enabled explicitly with  during compilation. The Arch Linux package includes the wiimote plugin since  4.96-3. If you are unsure whether your package includes the wiimote plugin, use

 $ grep wiimote /usr/lib/bluetooth/bluetoothd

This should say:

 grep: /usr/lib/bluetooth/bluetoothd: binary file matches

If this matches, then your BlueZ includes the wiimote plugin and no more user-interaction is needed. If this does not match, you need to enable it yourself or work without it. If you do not want to compile your own bluez package, then you can use the Wiimote without this plugin by connecting without pairing/bonding. For instance, when using Blueman or  you need to select Proceed without pairing when adding a new device.

If you want to compile the module on your own, then add  to your configure flags and proceed as usual. See the bluez PKGBUILD for further information.

## Cannot connect Wiimote
The BlueZ packages includes a special wiimote plugin since version  which handles all Wii Remote peculiarities for you. If you cannot pair your Wii Remote like any other device, then you should try connecting without pairing/bonding (i.e. not using authentication with a PIN). If you attempted to connect the device before configuring BlueZ and hid_wiimote correctly then you may need to remove the bluetooth device and start the connection process again. If this still does not work, please report your issue to the upstream developers at XWiimote@GitHub.

Please always use the red sync-button behind the battery cover on the back of the Wii Remote for troubleshooting. This works more reliably than holding the 1+2 buttons.

The Auto-Reconnect feature allows the Wii Remote to reconnect to its last connected host when a key is pressed. This means you do not need to connect your Wii Remote manually each time. However, the Auto-Reconnect feature only works if you paired your Wii-Remote. Connecting without the wiimote plugin will not enable Auto-Reconnect.

## Cannot use Wiimote in Dolphin-emu after pairing with xwiimote
Dolphin uses its own driver so pressing the resync button on the Wiimote while dolphin is running should resync the Wiimote to Dolphin instead of the xwiimote.

## My Wii Remote is still not working
The XWiimote software stack is actively developed. Please report your problems at XWiimote@GitHub.

There are also other projects which provide Wii Remote support for linux. See the Wii Remote article for the cwiid project.

## Wiimote keeps blinking after connecting it
Add  to

See this issue for more information
