# Logitech Unifying Receiver

The Logitech Unifying Receiver is a wireless receiver using 2.4 GHz band radio communication that can connect up to six compatible wireless mice and keyboards to your computer. The same applies to the newer Logi Bolt wireless technology that comes with newer devices.
The input device that comes with the receiver is already paired with it and should work out of the box through plug and play.
Logitech officially supports pairing of additional devices just through their Windows and macOS software.

Pairing and unpairing on Linux is supported by a number of tools, listed thereafter:

ltunify is a command-line C program that can perform pairing, unpairing and listing of devices. As of January 2024, ltunify does not yet recognize Bolt receivers. Solaar is a graphical Python program that integrates in your system tray and allows you to configure additional features of your input device such as swapping the functionality of Fn keys. It handles Bolt devices as well as unifying devices. libratbag is a configurable mice daemon that allows you to configure your devices, it has a GTK based graphical frontend app, piper.

## Installation
Several solutions are available:
*/
*

The following packages use the  user group, create it if it does not exist, and add users to this group to avoid the need of running these as root:
* or
* or
Do not forget to relogin to apply user's group membership. After installation, run
 # udevadm control --reload-rules
and then replug receiver, or reboot the system. After that you will not need root permissions.

## Usage
pairingtool can only be used for pairing and does not provide feedback, it also needs to know the device name for pairing. ltunify, Solaar and libratbag can detect the receiver automatically.

## ltunify
Examples on unpairing a device, pairing a new device and showing a list of all devices:

 $ ltunify unpair mouse
 Device 0x01 Mouse successfully unpaired
 $ ltunify pair
 Please turn your wireless device off and on to start pairing.
 Found new device, id=0x01 Mouse
 $ ltunify list
 Devices count: 1
 Connected devices:
 idx=1   Mouse   M525

## Solaar
Solaar has a GUI and CLI. Example CLI pairing session:

 $ solaar unpair mouse
 Unpaired 1: Wireless Mouse M525 $ solaar pair
 Pairing: turn your new device on (timing out in 20 seconds).
 Paired device 1: Wireless Mouse M525 [M525:DAFA335E
 $ solaar show
 -: Unifying Receiver with 1 devices
 1: Wireless Mouse M525 [M525:DAFA335E

To disable autostart of Solaar, remove . See Gentoo:Logitech bolt for a udev example.

## libratbag
Currently, piper is not able to pair/manage devices for unifying receivers but libratbag does include a  command line tool that is able to do this.

## pairingtool
To find the device that the receiver has, therefore take a look at the outputs of
 $ ls -l /sys/class/hidraw/hidraw*/device/driver | awk -F/ '/receiver/{print $5}'
This will show the names of your receiver, for example .

Now switch off the device that you want to pair (if it was on) and execute your compiled program with the appropriate device as argument:
 # pairing_tool /dev/hidraw0
 The receiver is ready to pair a new device.
 Switch your device on to pair it (you have thirty seconds to do so).
Now switch on the device you want to pair. After a few seconds your new device should work properly.

## Troubleshooting
## Wrong device (pairing tool only)
On some systems there is more than one device that has the same name. In that case you will receive the following error message when the wrong device is choosen:
 # pairing_tool /dev/hidraw1
 Error: 32
 write: Broken pipe

## Keyboard layout via xorg.conf
With kernel 3.2 the Unifying Receiver got its own kernel module hid_logitech_dj which does not work flawlessly together with keyboard layout setting set via xorg.conf.
A temporary workaround is to use  and set the layout manually. For example for a German layout with no deadkeys one has to execute:
 $ setxkbmap -layout de -variant nodeadkeys
To automate this process one could add this line to xinitrc or the according autostart file of your windows manager respectively desktop environment.

## Logitech touchpad keyboard K400r with unifying receiver M325
The Logitech keyboard K400r with integrated touchpad comes with Logitech unifying receiver M325 so the above mentioned about the keyboard layout will apply here too.

Also the integrated touchpad is recognized as 'pointer' instead of 'touchpad' so you cannot use the Touchpad Synaptics drivers.
Two finger horizontal scrolling and tapclick will work but in order to have a middle mouse button emulated you will have to add

to your evdev.conf.
Now third button is emulated by pressing both buttons simultaneously.

## Solaar 'Permission denied'
Is it possible to have the error:
 $ solaar show
 solaar: error: 13 Permission denied: '/dev/hidraw2'
In this case, you can physically remove the Unifying Receiver and re-insert it, and re-run the command (as described in the second point of installation part on the official site === Wireless Keyboard does not work while booting (cannot enter luks passphrase) ===

While booting it is impossible to input anything with a Logitech wireless Keyboard (e. g. Logitech MK700).
The cause of the problem is the own hid module for Logitech devices since Kernel 3.2.

A workaround is adding  to MODULES in :

 MODULES=(hid-logitech-hidpp)

and regenerate the initramfs.

## MouseJack Vulnerability
Several security vulnerabilities of the system have been reported and you may be in particular affected by the [https://www.bastille.net/research/vulnerabilities/mousejack/affected-devices MouseJack Vulnerability if your firmware has not been updated recently.

It is possible to display the current firmware's version by running:
 ltunify receiver-info

RQR12 firmware with version earlier than  and RQR24 firmware versions earlier than  are affected by this vulnerability and should be updated.

The firmware can be updated using fwupd like so:

 fwupdmgr refresh && fwupdmgr get-updates

If everything looks good, apply the update:

 fwupdmgr update

## Keyboard or mouse does not wake pc from sleep
Follow the Solaar USB installation instructions.

## PC wakes immediately from sleep
This can be a problem if using the logi bolt receiver, to resolve it you can install and run . If you want you can start it hidden by adding it to your autostart programs with

 solaar -w hide

If the problem persists, or installing solaar and its dependencies is not desired, the following udev rule will disable wake events from the Unifying or Bolt receiver. This will resolve the immediate wake issue, leaving the system chassis power button as the wakeup trigger (no wakeup on mouse button click):

{{hc|/etc/udev/rules.d/logitech-receiver.rules|
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="c52b|c548", ATTR{power/wakeup}="disabled"
}}

Alternatively, the following rule enables USB autosuspend for the Bolt receiver. When the receiver is already in the suspended state, before suspending your computer, it does not trigger an immediate wake-up, and you can use the mouse to wake the computer from suspend.
However, this introduces an issue: when the Bolt receiver is suspended, the mouse ignores input until you move it or click a button. For this reason, the autosuspend delay is set to a higher value of 60 seconds. The default kernel value is 2 seconds, and can also be changed globally by the usbcore.autosuspend parameter.
{{hc|/etc/udev/rules.d/logitech-receiver.rules|
ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="c548", ATTR{power/control}="auto", ATTR{power/autosuspend_delay_ms}="60000"
}}

## Lag of the wireless device
Because the receiver uses the 2.4 GHz frequency band also used by Bluetooth and Wi-Fi 802.11, it is possible in some circumstances of heavy Wi-Fi usage close to the receiver to experience lag or disturbances in communication with the devices. This is unlikely because the receiver confines its communication to channels unused by the majority of 802.11 solutions and it is able to quickly change channel within the band if it detects any interference from another device. However, some users have experienced interferences.

Switching on/off the device will force the search for a "quiet" channel and may solve the issue.

This problem can also manifest if there is electrical noise from USB3 sockets on the motherboard, and it is located close to or in one. Moving the receiver to a USB hub or the end of an extension cable may fix this.
