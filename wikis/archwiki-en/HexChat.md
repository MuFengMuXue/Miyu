# HexChat

HexChat is a multi-platform IRC client for GTK.

## Installation
Install . The development version is .

For spell checking install , see Language checking for available dictionaries. Restart HexChat for changes to take an effect.

## Configuration
HexChat stores configuration files in , XChat does so in .

## SSL and SASL
Enable SSL and SASL in Network List () > Network name > Edit. See also Configuring SASL for Hexchat.

## GNOME integration
To use the new Notifications and messaging tray, activate the following options in Settings > Preferences > Chatting > Alerts:

* Show tray balloons
* Blink tray icon (optional)
* Enable system tray icon: unchecked (the icon appears automatically if you have pending notifications)

## Troubleshooting
## Missing tray icon
:See bug report

If HexChat was loaded before the panel containing its icon, for example when the panel is forcibly reloaded, the icon may be invisible. To restore the icon, run:

 $ hexchat --existing --command="set gui_tray 0"
 $ hexchat --existing --command="gui apply"
 $ hexchat --existing --command="set gui_tray 1"
 $ hexchat --existing --command="gui apply"

Or restore the main window with:

 $ hexchat --existing --command="gui show"
