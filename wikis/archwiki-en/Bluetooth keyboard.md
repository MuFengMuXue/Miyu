# Bluetooth keyboard

This article describes how to set up a Bluetooth HID keyboard with Arch Linux,  version 5.

## Pairing process
Login to the affected computer by a wired keyboard or by ssh.

First, make sure the local Bluetooth controller (e.g. a Bluetooth dongle the built in Bluetooth radio) is recognized:

The above output is from a Raspberry-Pi revision 'B' with archlinux-arm and a Keysonic Bluetooth Dongle.

Three items worth remembering:

* Bluetooth devices (keyboard) and controllers (dongle) need to be paired once.
* The Bluetooth controller needs to be powered up after every boot.
* The Bluetooth controller needs to be told to connect to the keyboard after every boot.

Pairing is a one time process, required only once. There are Bluetooth keyboards sold with a Bluetooth dongle which come already paired, but that is not certain.  We will use the  command from  to pair our dongle and the keyboard.

Power up can be done with , or automatically in , see below.

Same for connecting, either  or  can be used, the latter is more useful for scripting.

We will use bluetoothctl for the pairing process. Run the command to get at the  prompt.

While in bluetoothctl power up the controller:

Next, tell  to look only for keyboards, and make that the default agent:

Next, put your controller (the local dongle) in pairable mode:

Next, put your keyboard in an active mode, where it is discoverable, i.e. pairable. Some keyboards have a special button for this on the underside, or require a special key combination to be pressed. See the documentation of your keyboard. Please note that this discoverability of a device is time limited; some devices are only visible for 30 seconds, other for 2 minutes. Your mileage may vary.

Next, let the controller scan the Bluetooth frequencies for a suitable device:

After a few seconds the address of the keyboard should be listed as found. This line will repeat over and over, but will not stop you from entering new commands.

Next, actually do the pairing. The address used is the Bluetooth MAC address of the keyboard:

Next, make this a trusted device (this allows the device to establish the connection on itself). Again, the Bluetooth MAC address is the address of the keyboard device:

Next and finally connect to the device (keyboard). Again, the Bluetooth MAC address is the address of the keyboard device:

Done. Leave the bluetoothctl utility:

 bluetooth# quit

Now the external device (i.e. keyboard) and the USB Bluetooth dongle are paired permanently, unless you break the pairing intentionally.

## Troubleshooting
## Bluetooth controller does not show up in lsusb
Manually load the generic Bluetooth driver:

 # modprobe btusb

For integrated Bluetooth controller, some are not internally wired through USB, and only appear using lspci.

## Bluetooth controller is not visible in bluetoothctl
Check the unit status of .

If the  prompt is blue and you get  message when powering on the controller with , run bluetoothctl as root.

## Bluetooth keyboard does not work
Start with basic troubleshooting steps : does the device have power; if so, did it connect to the Bluetooth controller? If not, try with another controller or your smartphone to confirm where the issue lies.

## Error: hci0 ACL packet for unknown connection handle 4
Try a reset with

## Alt and Super are swapped
Some keyboards have separate macOS and Windows mode. When the keyboard is connected or when modes change, the Apple mode may activate. Remove the  kernel module and re-connect the keyboard:

 # rmmod hid_apple

If this works, blacklist the module to have a permanent solution.

## Xorg
Device should be added as  and your Xorg should add it automatically if you did not disable such feature.
