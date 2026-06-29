# Yakuake

Yakuake is a top-down terminal for KDE in the style of Guake for GNOME, Tilda or the terminal used in Quake.

## Installation
Install the  package.

## Usage
Once installed, you can start Yakuake from the terminal with:

 $ yakuake

After Yakuake has started you can click on configure Yakuake by clicking on the Open Menu button (middle button on the bottom right hand side of the interface) and select Configure Shortcuts to change the hotkey to drop/retract the terminal automatically, by default it is set to .

## Configuration
## Background transparency and blur on Plasma
While most configuration options can be changed from Yakuake GUI, there are some options only accessible from modifying the configuration file, e.g. the option to use blur background under Plasma.

In order to apply blur background for Yakuake, edit the following file:

Then restart Yakuake to apply the change.

## Yakuake scripting
Like Guake, Yakuake allows to control itself at runtime by sending the D-Bus messages. Thus it can be used to start Yakuake in a user defined session. You can create tabs, assign names for them and also ask to run any specific command in any opened tab or just to show/hide Yakuake window, manually in a terminal or by creating a custom script for it.

Example of such a script is given below. This includes opening tabs, renaming tabs, splitting shells, and running commands.

 #!/bin/bash
 # Starting Yakuake based on user preferences. Information based on https://forums.gentoo.org/viewtopic-t-873915-start-0.html
 # Adding sessions from previous website is broken, use this: https://koston.pl/blog/sublime-text-3-cheatsheet-modules-web-develpment/

 # This line is needed in case Yakuake does not accept fcitx inputs.
 /usr/bin/yakuake --im /usr/bin/fcitx --inputstyle onthespot &

 # gives Yakuake a couple seconds before sending dbus commands
 sleep 2

 # Start htop in tab and split to user terminal and run iotop
 TERMINAL_ID_0=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId 0)
 qdbus org.kde.yakuake /yakuake/tabs setTabTitle 0 "user"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 0 "htop"
 qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalLeftRight "$TERMINAL_ID_0"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 1 "iotop"

 # Start split root sessions (password prompt) top and bottom
 SESSION_ID_1=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession)
 TERMINAL_ID_1=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId "$SESSION_ID_1")
 qdbus org.kde.yakuake /yakuake/tabs setTabTitle 1 "root"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 2 "su"
 qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalTopBottom "$TERMINAL_ID_1"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 3 "su"

 # Start irssi in its own tab.
 qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession
 qdbus org.kde.yakuake /yakuake/tabs setTabTitle 2 "irssi"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 4 "ssh home -t 'tmux attach -t irssi; bash -l'"

 # Start split ssh shells in own tab.
 SESSION_ID_2=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession)
 TERMINAL_ID_2=$(qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.terminalIdsForSessionId "$SESSION_ID_2")
 qdbus org.kde.yakuake /yakuake/tabs setTabTitle 3 "work server"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 5 "ssh work"
 qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.splitTerminalLeftRight "$TERMINAL_ID_2"
 qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal 6 "ssh work"

## dbus-send instead of qdbus
You can replace qdbus bundled with Qt with more common dbus-send. For example, to show/hide Yakuake:

 $ dbus-send --type=method_call --dest=org.kde.yakuake /yakuake/window org.kde.yakuake.toggleWindowState

## Tips and tricks
## Show notification when sudo asks password
When you do a long process that requires entering sudo password at the end (for example, when building a package from AUR), you often want to hide yakuake window and do something else. But when you go back to check the status, you see that sudo had exited by timeout.

To avoid that, you can configure yakuake to send system notifications at bell in inactive session. Inactive session is a session on another tab or on current tab but when yakuake is not in focus.

In Yakuake's menu (hamburger button) > Configure Notifications. In that window select Bell in Non-Visible Session and enable Show a message in a popup. Additionally you can set a sound (usually  or ).

Then you need to configure a sudo prompt to use a bell symbol. See Sudo#Add terminal bell to the password prompt.

## Troubleshooting
## True-color programs do not display correctly
See Konsole#True-color programs do not display correctly.
