# Bluetooth

Bluetooth is a standard for the short-range wireless interconnection of cellular phones, computers, and other electronic devices. In Linux, the canonical implementation of the Bluetooth protocol stack is BlueZ.

## Installation
# Install the  package, providing the Bluetooth protocol stack.
# Install the  package, providing the bluetoothctl utility. Additionally install  to have the deprecated BlueZ tools as well.
# The generic Bluetooth driver is the  kernel module. Check whether that module is loaded. If it is not, then load the module.
# Start/enable .

## Front-ends
## Console
*
*
*
*

## Graphical
The following packages allow for a graphical interface to customize Bluetooth.

* GNOME Bluetooth — GNOME's Bluetooth tool.
**  provides the back-end ( is now legacy)
**  provides the status monitor applet
**  provides the configuration front-end GUI that can be accessed by typing Bluetooth on the Activities overview, or with the  command.
** You can also launch the  command directly to send files to a remote device.
**  adds a "Send via Bluetooth" entry to Nautilus' right-click menu
** To receive files, open the Bluetooth settings panel; you can only receive whilst the Bluetooth panel is open.
** To add a Bluetooth entry to the Send To menu in Thunar's file properties menu, see instructions here. (The command that needs to be configured is ).
*
*
*
*
*
*

## Pairing
This section describes directly configuring bluez via the  command line tool, which might not be necessary if you are using  an alternative front-end tool (such as GNOME Bluetooth).

The exact procedure depends on the devices involved and their input functionality.  What follows is a general outline of pairing a device using bluetoothctl.

Start the  interactive command. Input  to get a list of available commands.

# (optional) Select a default controller with .
# (optional) Enter  to turn the power to the controller on if the device is set to off. It is on by default; see #Default adapter power state.
# Enter  to get the MAC address of the device with which to pair.
# Enter device discovery mode with  command if device is not yet on the list.
# Turn the agent on with  or choose a specific agent: if you press tab twice after  you should see a list of available agents. A Bluetooth agent is what manages the Bluetooth 'pairing code'. It can either respond to a 'pairing code' coming in, or can send one out. The  should be appropriate in most cases.# Enter  to do the pairing (tab completion works).
# If using a device without a PIN, one may need to manually trust the device before it can reconnect successfully. Enter  to do so.
# Enter  to establish a connection.

An example session may look this way:

## Dual boot pairing
For dual booting Linux systems, as shown in #Saving the configuration simply ensure all files from  are identical on each installation, either by copying or symlinking them.

With Windows or macOS, to pair devices on dual boot setups you need to change the pairing keys on your Linux install to match.

This page only describes the manual method of doing so. To automate the process, see the [https://github.com/x2es/bt-dualboot bt-dualboot project (does not support Bluetooth Low Energy) and the related repositories.  For a semi-automated process, use the bluetooth-dualboot script which does not edit any files, but it helps you run the right commands and cut-and-paste the correct values.

## Setup
To do this, first pair your device on your Arch Linux install. Then reboot into the other OS and pair the device. Now you need to extract the pairing keys, but first switch off the Bluetooth devices to prevent any connection attempts.

## For Windows
You can extract your Bluetooth keys on either Linux or Windows:

## Extracting on Windows
First, boot into Windows.

The registry key containing the link keys may only be accessed by the SYSTEM account, which cannot be logged into. Therefore, you will need Microsoft's PsExec tool from the official Windows Sysinternals site in order to run  as .

Download PsTools, and extract .

In an administrator instance of a command shell, from the location of the extracted EXE, launch the registry editor:

 .\PsExec64.exe -s -i regedit.exe

In the registry editor, navigate to the following registry key:

 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Keys

Within this registry key is one subkey per Bluetooth adapter, named by MAC address. If there are multiple subkeys, and you are unsure of which to use, follow this guide to find the MAC address for the desired Bluetooth adapter.

In the desired adapter's registry key, there is a name-value pair for each paired device, with the name being its MAC address. Additionally, you might see some subkeys named by MAC addresses, each containing name-value pairs with names like  or . These subkeys (if any) are for Bluetooth 5.1 devices. If the device you're trying to share has a subkey, it is a Bluetooth 5.1 device. If it does not have a subkey, only a name-value pair, it is not a Bluetooth 5.1 device.

Right click on the adapter's registry key and export it as a .reg file. This is a text file that you can copy keys from. As mentioned, it contains pairing keys in name-value pairs for non-Bluetooth 5.1 devices, and pairing keys (and some other information) in per-device subkeys for Bluetooth 5.1 devices. Make this file available to your Linux installation and reboot into it.

If the device you want to share is not a Bluetooth 5.1 device, jump to #Saving the configuration. If it is a Bluetooth 5.1 device, you need to make some modifications to the pairing keys and the associated information before finishing up. Refer to #Preparing Bluetooth 5.1 Keys to see how.

## Extracting on Linux
Boot into Arch. Install . Mount your windows system drive. Change to the registry hive directory and start  on the SYSTEM hive:

 $ cd /path/to/windows/system/Windows/System32/config
 $ chntpw -e SYSTEM

Inside the  environment, run:

 > cd CurrentControlSet\Services\BTHPORT\Parameters\Keys

Instead of , you may see  (check using ); use this instead:

 > cd ControlSet00X\Services\BTHPORT\Parameters\Keys

There will probably be just one subkey, whose name is your Bluetooth adapter's MAC address.
Show it with  and  into it:

 > ls
 > cd your-adapter's-mac-address

The subkey names under that adapter are the MAC addresses of the devices the adapter is paired to.
Show them with , then  into each of those you want to dual-pair:

 > ls
 > cd your-device's-mac-address

If this is not a Bluetooth 5.1 device, you will only see the pairing key:

If so, show a hexdump of your device's key using :

The "XX"s are the pairing key. Make note of which keys map to which MAC addresses.

If this is a Bluetooth 5.1 device, then you will see several keys corresponding to the one device:

Refer to #Preparing Bluetooth 5.1 Keys to see how to use these, using  to obtain the requested values.

Finally, to import the key(s) into your Linux installation, proceed to #Saving the configuration.

## For macOS
Boot into macOS:

* For macOS Monterey or newer:
*# Open Keychain Access and search for Bluetooth.
*# Sort by date.
*# If you've recently removed and reconnected the device then you can simply sort the keys by date modified and pick the latest. It is probably called MobileBluetooth (for older Bluetooth devices) or is just an UUID (for Bluetooth 5.1+).
*# Double click on the entry. Check that the MAC address in the Account field matches the MAC address of your device.
*# Click the "Show password" checkbox. You will now need to enter your password, twice.
*# Copy the text in the password field, it's actually an XML file ( )
*# Paste the text in  in your home directory.
* For High Sierra or newer, run the following in a terminal:
* For Sierra or older, run the following in a terminal:

The  file now contains the established Bluetooth keys. For older versions of macOS (High Sierra and older) you will have to reverse the keys before proceeding. For example,  becomes .

If this is a Bluetooth 5.1 device, then there will be more than one key corresponding to one device. Refer to #Preparing Bluetooth 5.1 Keys to see how to use these.

Finally, to import the key(s) into your Linux installation, reboot into Linux and proceed to #Saving the configuration.

## Preparing Bluetooth 5.1 Keys
If you observed the presence of Bluetooth 5.1 keys while following #For Windows or #For macOS, you must apply certain transformations to their values before importing them into Linux. Create the requested files with their appropriate contents, for installation in #Saving the configuration. This process will depend on the device, and some of the values have to be manipulated; code utilities for doing so are provided below.

{| class="wikitable"
! Device !! Source Key and Transformations (Windows) !! Source Key and Transformations (macOS) || Destination Key File
|-
|rowspan="3"|
* Logitech MX Anywhere 3S
* Logitech MX Master 3
* Logitech MX Master 3S
* Logitech MX Keys
* Logitech MX Keys Mini
* Logitech MX Mechanical
* Xbox One S Wireless Controller
|
* Copy .
* Remove the spaces between the hex octets.
|
|
|-
|
* Copy .
* Remove the spaces between the hex octets.
|
|  and
|-
| and  should be
|Random Number and Encrypted Diversifier should be .
|
|-
|rowspan="6"|
* Logitech MX Anywhere 2S
* ELECOM Bitra
|
* Copy .
* Remove the spaces between the hex octets.
|
|
|-
|
* Copy .
* Remove the spaces between the hex octets.
|
|
|-
|
* Copy .
* Remove the spaces between the hex octets.
|
|
|-
|
* Copy .
* Convert the whole number to decimal.
|
|
|-
|
* Copy .
* Convert the whole number to decimal.
|
|
|-
|
* Copy .
* Reverse the order of the octets.
* Convert the whole number to decimal.
|
|
|-
|rowspan="5"|
* Dygma Defy
|
* Copy .
* Remove the spaces (or commas) between the hex octets.
|
|
|-
|
* Copy .
* Remove the spaces (or commas) between the hex octets.
|
|
|-
|
* Copy .
* Convert the whole number from hex to decimal.
|
|
|-
|
* Copy .
* Convert the whole number from hex to decimal.
|
|
|-
|
* Copy .
* Reverse the order of the octets and remove the spaces (or commas).
* Convert the whole number from hex to decimal.
|
|
|-
|rowspan="1"|
* Royal Kludge F68 keyboard is like the Logitech MX Anywhere 2S
|
* Also copy  too.
* Remove the spaces between the hex octets.
|
|
|-
|rowspan="4"|
* ThinkPad TrackPoint Keyboard II
* Pebble M350 mouse
* Logitech G604 Lightspeed mouse
|
* Copy .
* Reverse the order of the octets.
|
* Copy Remote IRK.
* Convert from base64 to hex.
|
|-
|
* Copy .
* Remove the spaces between the hexadecimal octets.
|
* Copy Remote Encryption > Long-term Key.
* Convert from base64 to hex.
|
|-
|
* Copy .
* Reverse the order of the octets.
* Convert the whole number to decimal.
|
* Copy Remote Encryption > Random Number.
* Convert from base64 to a little-endian decimal number (see Python code below).
|
|-
|
* Copy .
* Reverse the order of the octets.
* Convert the whole number to decimal.
|
* Copy Remote Encryption > Encrypted Diversifier.
* Convert from base64 to a little-endian decimal number (see Python code below).
|
|-
|rowspan="3"|Other devices
|
* Copy .
* Remove the spaces between the hex octets.
|
* Copy Remote IRK.
* Convert from base64 to hex.
|
|-
|
* Copy .
* Reverse the order of the octets.
* Convert the whole number to decimal.
|
* Copy Remote Encryption > Long-term Key.
* Convert from base64 to hex.
|
|-
|
* Copy .
* Remove the spaces between the hex octets.
|
* Copy Remote Encryption > Encrypted Diversifier.
* Convert from base64 to hex.
* Reverse the order of the octets.
|
|-
|rowspan="1"|Xbox wireless controller
|
* Copy .
* Remove the spaces between the hex octets.
|
|
|}

Then restart  and  (with ).

You should be able to connect to your device now.

## Configuration
## Default transport 3.0 vs 5.x (low energy)
To force Bluetooth controller to use older Bluetooth transport protocol (e.g. because its simpler to setup dual boot pairing for 3.0 device, than for 5.x BLE device), set  in  in the  section:

Default value is  i.e. both BR/EDR and LE enabled.

## Default adapter power state
As of  5.65, BlueZ' default behavior is to power on all Bluetooth adapters when starting the service or resuming from suspend. If you would like the adapter to not be automatically enabled (e.g. on a portable device where you wish to save battery), set  in  in the  section:

The adapter can still be turned on manually by running  as described in #Pairing.

## Discoverable on startup
If the device should always be visible and directly connectable:

## Wake from suspend
To allow Bluetooth keyboards, mice, etc. to wake the system from suspend. First, check the bios settings and make sure that wake from USB is not disabled. In many cases, Bluetooth from the motherboard is a USB device.

Add a new udev rule for Bluetooth adapter(s) ([https://www.usb.org/defined-class-codes#anchor_BaseClassE0h USB Wireless Controller Base Class, Bluetooth Programming Interface Protocol) to enable wake from suspend:

{{hc|/etc/udev/rules.d/91-bluetooth-wakeup.rules|2=
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", \
    ATTR{bDeviceClass}=="e0", \
    ATTR{bDeviceProtocol}=="01", \
    ATTR{bDeviceSubClass}=="01", \
ATTR{power/wakeup}="enabled"
}}

To automatically re-configure your Bluetooth keyboard after wakeups to e.g. have a different keymap or key press repeat rate (for details, see Xorg/Keyboard configuration#Adjusting typematic delay and rate and xmodmap), create an executable script:

Then create an additional udev rule like above:

{{hc|/etc/udev/rules.d/92-keyboard-reconfiguration-wakeup.rules|2=
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", \
    ATTR{bDeviceClass}=="e0", \
    ATTR{bDeviceProtocol}=="01", \
    ATTR{bDeviceSubClass}=="01" \
RUN+="/your/path/to/configure_keyboard.sh"
}}

## Enabling experimental features
The Bluez stack keeps new, potentially buggy features behind the D-Bus experimental and kernel experimental options. The functionality included under these varies over time, as experimental features are determined to be stable and no longer require the option (as an example: enabling D-Bus experimental interfaces currently allows to report battery level for old headsets). To enable these, uncomment the corresponding line in the configuration:

Alternatively, you can edit the  to add the  or  flag, like this drop-in file:

Either way, you must then restart the .

## Audio
You will typically need to take an additional step to integrate the audio server with Bluetooth. This is detailed in the below sections.

See the Bluetooth headset page for more information about Bluetooth audio and Bluetooth headsets.

## PulseAudio
In order to be able to use audio equipment like Bluetooth headphones or speakers, you need to install the additional  package. Make sure to restart PulseAudio to make the installation take effect: . With a default PulseAudio installation (specifically, using a user instance with the packaged ) you should immediately be able to stream audio from a Bluetooth device to your speakers. If you have a system-wide PulseAudio setup make sure the user running the daemon (usually ) is in the  group and you load the Bluetooth modules in your PulseAudio config:

Optionally, add  if you want to auto-switch all audio to the Bluetooth device.

## PipeWire
PipeWire as of v0.3.19 enables its Bluetooth support by default.

## ALSA
First, ensure that your Bluetooth audio device is correctly paired and connected to the system.

Then, install , start (and enable) the  service, and add your user to the  group.

Run the following command to check if everything is working as intended (replace  and  below):

 $ aplay -D bluealsa:SRV=org.bluealsa,DEV=XX:XX:XX:XX:XX:XX,PROFILE=a2dp FILE.wav

Finally, add the following lines to your :

{{hc|~/.asoundrc|
defaults.bluealsa {
    service "org.bluealsa"
    device "XX:XX:XX:XX:XX:XX"
    profile "a2dp"
}
}}

You can now use the  device to reach your Bluetooth audio device. Volume management is conducted normally via  with the option .

## Bluetooth serial
To get Bluetooth serial communication working on Bluetooth-to-Serial modules (HC-05, HC-06) do the following steps:

Pair your Bluetooth device using  as described above.

Install , as it provides certain functionality which is missing from newer tools.

Bind paired device MAC address to tty terminal:

 # rfcomm bind rfcomm0 MAC_address_of_Bluetooth_device

Now you can open  for serial communication:

 $ picocom /dev/rfcomm0 -b 115200

## Troubleshooting
## General Troubleshooting
## Debugging
In order to debug, first stop .

And then start it with the  parameter:

 # /usr/lib/bluetooth/bluetoothd -n -d

Another option is via the  tool.

## Deprecated BlueZ tools
Eight BlueZ tools [https://git.kernel.org/pub/scm/bluetooth/bluez.git/commit/?id=b1eb2c4cd057624312e0412f6c4be000f7fc3617 were deprecated and removed from , although not all of them were superseded by newer tools. The  package now provides these deprecated tools.

{| class="wikitable"
|-
! Deprecated tool
! Most likely replacement
|-
| gatttool || btgatt-client, D-Bus Gatt API (GattCharacteristic, GattDescriptor, GattManager, GattProfile, and GattService)
|-
| hciattach || btattach
|-
| hciconfig || btmgmt (and bluetoothctl?)
|-
| hcidump || btmon (and btsnoop)
|-
| hcitool || missing, D-Bus Device API available
|-
| rfcomm
| rowspan="2" | missing, implement with D-Bus Profile/ProfileManager API?
|-
| ciptool
|-
|sdptool
| missing, functionality seems to be scattered over different D-Bus objects: Profile, Advertising (LEAdvertisement and LEAdvertisingManager), and the UUIDs arrays in device and adapter.
|}

## Service issues
## systemd: Condition check resulted in Bluetooth service being skipped
 only requires the directory  to exist, which should be created by kernel module , which is only autoloaded by  if it actually finds a working Bluetooth hardware device.

If your  does not exist, check if your kernel Bluetooth module is loaded by . If not, and you believe you have a Bluetooth device, you can try manually starting them by loading the Bluetooth module and restarting .

You should also load your corresponding kernel Bluetooth driver when loading the  module, most likely , but can also be  etc.

Check 's unit status to see whether it started.

See also Debian Bug report logs - #853207.

If  started successfully, there is a chance that you still cannot use Bluetooth normally (e.g.  says something like  when you ). If this happens, try rebooting your computer, and double-check: whether directory  exists; whether  includes correct Bluetooth modules; log messages in the journal; etc.  should pickup your Bluetooth hardware automatically without manual changes again.

## Bluetooth immediately waking up suspend-to-idle devices
On systems capable of suspend-to-idle/S2idle/S0ix/Modern Standby, Bluetooth controllers will stay enabled during sleep. This will usually cause the system to wake up immediately after going to sleep if any Bluetooth device is connected.

To prevent this, you can disable Bluetooth completely before going to sleep - install  and create this file:

Enable this service and check if Bluetooth devices disconnect when going to sleep, and whenever Bluetooth goes back up after waking up the system.

If this workaround is in use, waking up the system with a Bluetooth mouse/keyboard will not work.

## Bluetooth turns off after logout on a headless/server system
This can have various causes:

* Both PulseAudio and PipeWire run as user services by default, which are terminated once the last session ends. Enable lingering for the user to fix this.
* Additionally, when running WirePlumber with PipeWire (which is usually the case), WirePlumber runs a "logind-monitor" which enables Bluetooth on login and disables it on logout. See WirePlumber#Keep Bluetooth running after logout / Headless Bluetooth for a fix.

## Adapter issues
## hcitool scan: Device not found
* On some laptops (e.g. Dell Studio 15, Lenovo Thinkpad X1) you have to switch the Bluetooth mode from HID to HCI. Install the  package, then udev should do this automatically. Alternatively, you can run this command to switch to HCI manually:

 # /usr/lib/udev/hid2hci

* If the device will not show up and you have a Windows operating system on your machine, try booting it and enable the Bluetooth adapter from windows.

* Sometimes also this simple command helps:

 # bluetoothctl power on

## bluetoothctl: No default controller available
First, make sure the device is not being blocked by rfkill. If using USBGuard, make sure it is not blocking the device (see USBGuard#Allow Bluetooth controllers).

Otherwise, consider the following possible causes:

* Some motherboard Bluetooth controllers have a bug which causes this. To see whether this is the issue, run  and check whether it contains  or . If it does, power off your computer and physically unplug the power cable for a few seconds. This forces the controller to reload the firmware, unlike a standard reboot (see bug report).
* Some Intel cards (such as the 8260) are not picked up correctly by the Bluetooth service. In this case, using the deprecated  instead of  might fix the issue.
** Some dongles, such as the CSR clones, have compatibility issues at the kernel level.
* Power saving measures can cause issues, in which case adding the kernel parameter  is a potential solution (see bug report).

Finally, unloading and loading  without options sometimes helps to get the controller back:

## rfkill unblock: Do not unblock
If your device still soft blocked and you run ConnMan, try this:

 $ connmanctl enable bluetooth

## Bluetooth USB dongle
If you are using a USB dongle, you should check that your Bluetooth dongle is recognized. You can do that by running  as root when you have plugged in the USB dongle (or inspecting ). It should look something like the following (look out for hci):

If you only get the first two lines, you may see that it found the device but you need to bring it up.
Example:

Or

To verify that the device was detected you can use  which is part of the . You can get a list of available devices and their identifiers and their MAC address by issuing:

It is possible to check the Bluetooth version as mapped to the HCI version according to the table in the official specification. For example, in the previous output, HCI version 6 is Bluetooth version 4.0.

More detailed information about the device can be retrieved by using the deprecated . ()

## Audio devices start to skip at short distance from dongle
If other devices share the same USB host, they can interrupt communication with audio devices. Make sure it is the only device attached to its bus. For example:

## CSR dongle 0a12:0001
The device  has a regression bug, and currently only works in the kernel version 5.17 and < 6.0. For more information, see Kernel Bug 60824.

## Logitech Bluetooth USB dongle
There are Logitech dongles (ex. Logitech MX5000) that can work in two modes: Embedded and HCI. In embedded mode dongle emulates a USB device so it seems to your PC that you are using a normal USB mouse/keyoard.

If you hold the little red Button on the USB BT mini-receiver it will enable the other mode. Hold the red button on the BT dongle and plug it into the computer, and after 3-5 seconds of holding the button, the Bluetooth icon will appear in the system tray. Discussion

Alternatively, you can install the  package. When you connect your Logitech dongle it will automatically switch.

## Foxconn / Hon Hai / Lite-On Broadcom device
Some of these devices require the firmware to be flashed into the device at boot.

Some firmware is available when searching for broadcom on the AUR, a notable package being , which provides the files for multiple cards.

Alternatively, the firmware can be converted from a Microsoft Windows .hex file into a .hcd using hex2hcd (which is installed with ).

In order to get the right .hex file, try searching the device vendor:product code obtained with lsusb, for example:

 Bus 002 Device 004: ID 04ca:2006 Lite-On Technology Corp. Broadcom BCM43142A0 Bluetooth Device

or

 Bus 004 Device 004: Id 0489:e031 Foxconn / Hon Hai

Alternatively, boot into Windows (a virtual machine installation will suffice) and get the firmware name from the Device Manager utility. If you want to know the model of your device but cannot see it in lsusb, you might see it in lsusb -v as .

The .hex file can be extracted from the downloaded Windows driver without having to run Windows for it. Download the right driver, for example Bluetooth Widcomm. Depending on the format, extracting the files might need  or . To find out which of the many .hex files is the right one for you, look in the file  and search for , where  should be replaced with the product code (the second hex number in lsusb) of your device in upper-case. Underneath you should see the file name of the right .hex file.

Once you have the .hcd file, copy it into  - this filename is suggested by dmesg and it may change in your case so check your dmesg output in order to verify. Then reload the btusb module:

 # rmmod btusb
 # modprobe btusb

The device should now be available. See BBS#162688 for information on making these changes persistent.

## Intel combined Wi-Fi and Bluetooth cards
See Wireless network configuration#Bluetooth coexistence.

## Mediatek MT7921 or MT7961 on dual boot with windows
On dual boot systems, if Bluetooth firmware versions are different for Windows and Linux, the Bluetooth adapter is not working after rebooting to Windows.

The best way to prevent this is updating the Bluetooth drivers (especially firmware) with latest version for each OS.

If you cannot find the latest version driver (or firmware) for Windows, you can copy the latest firmware file  from Arch Linux and extract to Windows (e.g. , you can find the firmware file path in the device manager on Windows).

## Adapter disappears after suspend/resume
First, find vendor and product ID of the adapter. For example:

In this case, the vendor ID is 8087 and the product ID is 0025.

Then, use  to reset the adapter:

 # usb_modeswitch -R -v vendor_ID -p product_ID

## Pairing and connectivity issues
## Computer is not visible
Enable discoverable mode if your computer cannot be discovered from your phone:

 # bluetoothctl discoverable on

Verify that discoverable mode is on:

If the computer still does not show up, try changing the device class in  as follows:

 # Default device class. Only the major and minor device class bits are
 # considered.
 #Class = 0x000100 # Computer Type (from default config)
 Class = 0x100100 # (Object-Transfer Service & Computer Type)

A user reported that this was the only solution to make their computer visible for their phone. LG TVs (and some others) are discoverable from their audio devices, so using  (the soundbar class) will make such devices appear.

See https://bluetooth-pentest.narod.ru/software/bluetooth_class_of_device-service_generator.html to generate Bluetooth device/service classes.

## Device connects, then disconnects after a few moments
A bug introduced in BlueZ 5.83 (still present as of 5.86) causes a disconnection after an extraneous authentication attempt is made and fails. This bug appears to only affect devices with multipoint supportA temporary workaround is to restart . On KDE Plasma, killing or disabling KDE Connect can stop the issue.

If you see messages like the following in the journal, and your device fails to connect or disconnects shortly after connecting:

 bluetoothd: Unable to get connect data for Headset Voice gateway: getpeername: Transport endpoint is not connected (107)
 bluetoothd: connect error: Connection refused (111)

This may be because you have already paired the device with another operating system using the same Bluetooth adapter (e.g., dual-booting).  Some devices cannot handle multiple pairings associated with the same MAC address (i.e., Bluetooth adapters). Follow instructions on #Dual boot pairing for solving this issue.

## Device does not show up in scan
Some devices using Bluetooth low energy do not appear when scanning with bluetoothctl, for example the Logitech MX Master. You can use  to scan it.

Another way to connect them is by installing , then start  and do:

In another terminal:

 # hcitool lescan

Wait until your device shows up, then  hcitool. bluetoothctl should now see your device and pair normally.

## No BLE device can be discovered with Intel Corp. AX200 Bluetooth
It seems that BLE passive scan is broken on this device. See [https://community.intel.com/t5/Wireless/AX200-Passive-BLE-scan-linux/m-p/1227456 upstream bug report for more details.

## Cannot reconnect after sleep
You may notice that you cannot automatically reconnect to a device after it goes to sleep, or after the computer wakes from suspend.

You would for example notice the following errors in your logs:

This could be because the device is not marked as trusted. See #Pairing.

## Device-specific issues
## Bluetooth mouse lags / disconnect / does not respond
See Bluetooth mouse#Troubleshooting.

## Audio device fails to connect with br-connection-profile-unavailable
A Bluetooth audio device will fail to connect if pipewire (rather than pulseaudio-bluetooth) is being used, but an instance of pipewire is not running. Start the  user unit or play some audio to start the pipewire daemon, then try to connect the audio device again.

## Interference between headphones and mouse
If you experience audio stuttering while using a Bluetooth mouse and keyboard simultaneously, you can try the following as referenced in #23 https://bugs.launchpad.net/ubuntu/+source/bluez/+bug/424215

 # hciconfig hci0 lm ACCEPT,MASTER
 # hciconfig hci0 lp HOLD,SNIFF,PARK

## Continually connect/disconnect with TP-LINK UB400 and Xbox controller
Use the settings below:

Then restart the .

You can see relevant discussion on xpadneo but the xpadneo driver is not needed.

## File transfer issues
## gnome-bluetooth
If you see this when trying to enable receiving files in bluetooth-properties:

 Bluetooth OBEX start failed: Invalid path
 Bluetooth FTP start failed: Invalid path

Then make sure that the XDG user directories exist.

## Cannot receive transferred files due to symlink
If incoming file transfers fail on an an otherwise functional Bluetooth connection, the problem may be due to symlinks in your file transfer path.  Logs like this would appear in the journal:

 Jun 18 11:18:13 ember obexdopen(/home/me/.cache/obexd/MOC740): Operation not permitted (1)

If the path shown in the error message contains a symlink, then obexd by default [https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/obexd/plugins/filesystem.c#n90 will not accept it. The behavior can be overridden on initialization using a drop-in file for the  user service:

Then reload the systemd manager configuration of the calling user and restart the  user unit.
