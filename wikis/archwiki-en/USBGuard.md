# USBGuard

USBGuard offers a white/black-listing mechanism for USB-devices. Inspiration for this is drawn from exploits like BadUSB.
It makes use of a device blocking infrastructure included in the Linux kernel and consists of a daemon and some front-ends.

## Installation
Install the  package.

The official Qt applet was removed from USBGuard and substituted with . An unofficial, forked version of the Qt applet is available as .

## Configuration
The main configuration file is found in .

If you want to control the daemon via IPC, be sure to add your username to  or your group to  to make rules persistent. In most cases, you want this.

By default, the  is set to  so that USBGuard evaluates the ruleset for every connected device. This is the most secure setting, which ensures security even when the daemon hits a restart. Alternatively, the key may be set to  in order to block all newly connected devices but leave devices connected before daemon as is. To temporary allow new devices use .

With the key  you can configure the default treatment of devices, if no rules match. The most secure option here is .

For an in-depth documentation of configuration see the very well commented configuration file.

## Rules
To configure USBGuard to your needs, you can edit . However manual editing of the rules is normally not necessary. You can generate a ruleset based on your currently attached USB devices by executing  as root.

The rules syntax is formally explained here.
An example for a hp printer connected via USB can look like this:

 allow id 03f0:0c17 serial "00CNFD234631" name "hp LaserJet 2020" hash "a0ef07fceb6fb77698f79a44a450121m" parent-hash "69d19c1a5733a31e7e6d9530e6k434a6" with-interface { 07:01:03 07:01:02 07:01:01 }

A rule begins with a policy.  whitelists a device,  stops the device from being processed now and  removes the device from the system.
Then follows a set of attributes with their options, as detailed below.

{| class="wikitable"
! Attribute || Description
|-
| id usb-device-id || Match a USB device ID.
|-
| id { usb-device-id ... } || Match a set of USB device IDs.
|-
| hash "value" || Match a hash computed from the device attribute values and the USB descriptor data. The hash is computed for every device by USBGuard.
|-
| hash [operator { "value" ... } || Match a set of device hashes.
|-
| parent-hash "value" || Match a hash of the parent device.
|-
| parent-hash { "value" ... } || Match a set of parent device hashes.
|-
| name "device-name" || Match the USB device name attribute.
|-
| name [operator { "device-name" ... } || Match a set of USB device names.
|-
| serial "serial-number" || Match the USB iSerial device attribute.
|-
| serial { "serial-number" ... } || Match a set of USB iSerial device attributes.
|-
| via-port "port-id" || Match the USB port through which the device is connected. Note that some systems have unstable port numbering which change after the system reboots or certain kernel modules are reloaded (and maybe in other cases). Use the parent-hash attribute if you want to ensure that a device is connected via a specific parent device.
|-
| via-port [operator { "port-id" ... } || Match a set of USB ports.
|-
| with-interface interface-type || Match an interface type that the USB device provides.
|-
| with-interface { interface-type interface-type ... } || Match a set of interface types against the set of interfaces that the USB device provides.

|}

## Usage
USBGuard has a core daemon, a CLI, a DBUS interface and an API via libusbguard.

If you want to use the Qt GUI or another program communicating via DBUS (which includes the GNOME integration), enable and start .

If you only want to communicate via API (with the CLI tool or another software using libusbguard) enable and start .

## CLI
The CLI is available via .

See the according man pages for more info.

## Allow Bluetooth controllers
If USBGuard is set to block all USB devices by default, it will also block  controllers by default since they communicate using a USB bus. Since many motherboards' Bluetooth cards are  controllers, it may not be obvious that Bluetooth is blocked by USBGuard. For Bluetooth to work, you need to set USBGuard to allow these  controllers.

Find and display information about the USB buses in
the system using  (part of ). This should display something like

We are interested in the Bluetooth device. Note its ID (in this case, , but this may vary)
and set USBGuard to allow this ID:

## GNOME integration
GNOME has had USBGuard support baked in [https://www.phoronix.com/scan.php?page=news_item&px=GNOME-3.35.91-Released since 3.36. It requires polkit rule configuration to grant GNOME access, and dconf modification to always block devices as the default is set to allow and only block on lockscreen.

## Grant GNOME access to the USBGuard daemon
Authorize GNOME Shell running under users with the  group assigned access to USBGuard, by creating the following file:

{{hc|/etc/polkit-1/rules.d/70-allow-usbguard.rules|
// Allow users in wheel group to communicate with USBGuard
polkit.addRule(function(action, subject) {
    if ((action.id == "org.usbguard.Policy1.listRules" ||
         action.id == "org.usbguard.Policy1.appendRule" ||
         action.id == "org.usbguard.Policy1.removeRule" ||
         action.id == "org.usbguard.Devices1.applyDevicePolicy" ||
         action.id == "org.usbguard.Devices1.listDevices" ||
         action.id == "org.usbguard1.getParameter" ||
         action.id == "org.usbguard1.setParameter") &&
        subject.active == true && subject.local == true &&
        subject.isInGroup("wheel")) {
            return polkit.Result.YES;
    }
});}}

Changes to polkit rules are picked up automatically by the polkit daemon itself.

## Turn GNOME USB Protection on
If the USBGuard service is present and this setting is enabled, USB devices will be protected as configured in the usb-protection-level setting. Enable it by running the command below:

## Block all USB devices by default
If set to , only when the lock screen is present new USB devices will be rejected; if set to , all new USB devices will always be rejected. Reject all new USB devices by running the command below:

## Related projects
*  (an anti-forensic kill-switch that waits for a change on your USB ports and then immediately shuts down your computer)
*  (kill switch for unknown usb devices (DKMS))
