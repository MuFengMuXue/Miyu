# Gajim

Gajim is a full featured and easy to use XMPP client.

## Installation
Install the  package.

## Configuration
Gajim is a Graphical User Interface (GUI), all configuration is done through the interface under preferences, you can access this via the top left gajim drop down, and selecting preferences or using the  shortcut.

Within the Preferences menu, you can find the following configuration categories:

* General - General behaviour of the client, such as how it should behave when closed.
* Chats - General behaviour of chat windows, such as allowing you to disable status change notifications, or join/leave messages.
* Notification - General behaviour of notifications within the client, allowing you to enable/disable audible notifications.
* Status - General configuration of notifications, such as automatic status changes invoked by events such as inactivity for a certain period of time.
* Style - Configuration of the client theme.
* Advanced - Settings aimed towards more advanced users, allowing purging of message history, changing client proxy settings, and enabling/disabling debug logging

## D-Bus remote control
To enable D-Bus remote control support, go to Advanced menu within Preferences and enable D-Bus Interface, then restart gajim.

## Show/hide roster
If you would like to be able to show/hide the roster using a script or your window manager, you can use the following command:

 $ gajim-remote toggle_roster_appearance

It may be necessary to restart Gajim if this does not work.

## OMEMO support
OMEMO Multi-End Message and Object Encryption is an XMPP Extension Protocol (XEP) for secure multi-client end-to-end encryption. It is an open standard based on Axolotl and PEP and Gajim implemented it.

## Notification sounds
# Install the  package.
# Enable notification sound under Notifications within the Preferences menu, then enable the Play Sounds setting.

## Audio and video call support
Currently, Gajim doesn't support audio and video calls.

## Minimize or close to tray
By default Gajim remains in the taskbar (for Docks) instead of minimizing to tray when closing it, to disable this behavior enable the hide_on_roster_x_button preference.

## Tips and tricks
## Save history of messages
If the Save of Message History is enabled, a file  is created. This is a SQLite database. (Open it with DB Browser for SQLite, install )
To look for a message, first get the  of the contact in table . Click on Tab "Search Data". Choose Table .
Now click the tab "Run SQL" and run the statement

 SELECT time, kind, message FROM logs WHERE jid_id=(the jid_id from table jids) ORDER BY time ASC;

and click the run button. The result ist a list of your messages orderd by time (first message first, latest message at the bottom). The column  shows if the message was sent (Code: 6) or received (Code: 4).

## Troubleshooting
## Fix dark theme
When switching to dark mode in the Preferences does not work, set  and  in .

## Fix emojis
The emojis is Gajim require the Noto font. You need to install  and  to fix this.
