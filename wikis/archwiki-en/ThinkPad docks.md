# ThinkPad docks

Business laptops manufactured by Lenovo and IBM under the ThinkPad brand have a proprietary connector at the bottom of the laptop that is used in junction with docking stations that enable the ThinkPad to be used as a desktop PC.

These docking stations can function in two ways:

* Passive port replicators (no active components)
* Active docks (active components such as USB hubs or USB 3.0 controllers)

Both of them are supported out-the-box by GNOME and KDE and should not require additional software. Otherwise you can use dockd.

## Using dockd
To handle docks outside KDE and GNOME you will need to install a dock daemon that will auto-switch the monitors.
 is a dock daemon that was developed for light desktops and will auto switch the monitor configuration.

## Installing
Install the  package.

The daemon needs to know your current display configuration when the laptop is docked and undocked, so we need to configure the daemon first before using it.

* Insert your ThinkPad into the dock
* Configure the display layouts and resolutions using your desktop environments interface or xrandr
* Write the profile when the ThinkPad is docked
 # dockd --config docked
* Remove the ThinkPad from the dock
* Configure the internal panel resolution and refresh rates using your desktop environments interface or xrandr
* Write the profile when the ThinkPad is undocked
 # dockd --config undocked
* Start/enable  (see acpid if needed).
* If you are using i3, you need to manual autostart dockd as i3 is not XDG Autostart compatible

* Log out and log back in

The daemon should now be configured and ready to use. Insert the ThinkPad into the dock and observe if the daemon switches to your external display automatically.

## Dock and undock hooks
As of dockd 1.21, you can define some hooks that run when the ThinkPad is docked and undocked.

For example, to disable Wi-Fi when docking and enable it when undocking:

## Troubleshooting headset microphone on 4X10E52935 dock
This dock appears to use an OMTP standard wiring for the headset connector instead of the more common CTIA standard. Thus the pins (from tip to sleeve) are left channel, right channel, microphone, ground instead of left channel, right channel, ground, microphone. Adapters can be found by searching "3.5mm OMTP to CTIA adapter" on your favorite e-commerce site.
