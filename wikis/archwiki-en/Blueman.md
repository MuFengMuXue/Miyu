# Blueman

Blueman is a full featured Bluetooth manager written in Python and using GTK.

## Installation
Install either  or  for the development version.

Be sure to enable the Bluetooth unit and start Blueman with . A graphical settings panel can be launched with .

## Usage
## Autostarting
The following autostart file should have been created: . This means that Blueman should be autostarted with most desktop environments without manual intervention. See the article for your desktop environment or window manager as well as the Autostarting article for further information on autostarting.

## Permissions
To receive files remember to right click on the Blueman tray icon > Local Services > Transfer > File Receiving (Object Push) and tick the Accept files from trusted devices box.

To be able to manage devices, you might need to add your user to the  group, else you might receive the following error when connecting to a device: . This is because the user needs to be authorized to communicate with the Bluetooth daemon via D-Bus - the  group is specified in . For information on adding a user to a group, see Users and groups#Other examples of user management.

From version 2.0.6 the official documentation recommends creating polkit rules in order to avoid polkit agents asking for password on every boot, as root user add the following polkit rules:

{{hc|/etc/polkit-1/rules.d/51-blueman.rules|
/* Allow users in wheel group to use blueman feature requiring root without authentication */
polkit.addRule(function(action, subject) {
    if ((action.id == "org.blueman.network.setup" ||
         action.id == "org.blueman.dhcp.client" ||
         action.id == "org.blueman.rfkill.setstate" ||
         action.id == "org.blueman.pppd.pppconnect") &&
        subject.isInGroup("wheel")) {

        return polkit.Result.YES;
    }
});
}}

Note that users must belong to the  group.

## Mounting Bluetooth devices
The instructions below describe a method for using different file managers with Blueman. The examples in this section focus on Thunar. If you are using a different file manager, substitute thunar with the name of the file manager you are using.

Now you will need to move the script to an appropriate location (e.g., ). After that, mark it as executable.

The last step is to change the line in Blueman tray icon > Local Services > Transfer > Advanced to .

## Blueman and PulseAudio
Users who want to use PulseAudio with a Bluetooth headset, in addition to installing , may want to activate the PulseAudio plugin of Blueman. This automatically loads PulseAudio Bluetooth module after audio device is connected and plays all audio through the Bluetooth headset. For more information see Bluetooth headset.

## Configuration
Configuration is done through  (or gsettings or ) under .

## Disable auto power-on
Blueman automatically enables the Bluetooth adapter () when certain events (on boot, laptop lid is opened, ...) occur. This can be disabled with the  in :

 $ gsettings set org.blueman.plugins.powermanager auto-power-on false

## Receive notifications through a notification daemon
Blueman can send notifications through a notification daemon (e.g. dunst) if present. In case of unavailability of a notification daemon, blueman uses a window-based fallback. This behavior can be configured by toggling the  setting in

 $ gsettings set org.blueman.general notification-daemon true

## Troubleshooting
## No adapters detected
If your Bluetooth applet or manager does not show or detect any Bluetooth adapter, your wireless card may be blocked. Try un-block it using  rfkill.

## Cannot receive files
If you cannot send or receive files and you encounter a python-dbus-exception error similar or exactly like  then it is advised to start the obexd-service manually from  and see if that helps. Since the default permissions assume 755 it is possible to start the daemon from a user-account.

Start it with this line:

 # /usr/lib/bluetooth/obexd -n

Let the terminal in which the command runs open and test if sending files work. Check if you actually receive the file. You can add the command to your autostarter so you will not have to manually start the service every time. Your desktop environment autostarter should be able to run the program once you login. Logout and login and you should be able to receive files without running the line manually now.

Should the error persist or another occur then try using ObexFTP for file transfers instead.
