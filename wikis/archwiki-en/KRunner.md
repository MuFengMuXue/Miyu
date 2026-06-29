# KRunner

KRunner is an application built into KDE Plasma to perform functions and run commands quickly, and features a "runner" system to customize functions available for use.

## Installation
Install the  package.

## Usage
To open KRunner in Plasma, you can either right-click the desktop and press "run command", or you can use the default keybindings,  or . In some workspaces such as a blank desktop, starting to type will automatically bring up KRunner.

## Open KRunner with the Meta key
KRunner can now be bound to the Meta key directly in System Settings > Shortcuts > Krunner.

## Change position where KRunner is displayed
By default KRunner is displayed at top of screen. To make it appear centered, run

 $ kwriteconfig6 --file krunnerrc --group General --key FreeFloating true

The change will become effective on next login.

## Switch active windows
In Krunner configuration, there is a plug-in configuration button where you can choose needed search source. See the user manual for detail.

If you want to specify krunner search only by active window titles, just enable window plugin and disable the others.

## Full list of windows with search by titles
This approach will require .

# Go to System Settings > Workspace > Shortcuts > Custom Shortcuts.
# Create new Global shortcut -> Command/URL (by right click)
# Tick the checkbox to the right of the name.
# In Trigger tab select the desired key combination.
# In Action tab type
# Create file  with the following content:
# Make file executable and give run permission to all.
Note the space after .

It is possible to specify the search query directly, but repeated search queries will be selected. To avoid this, use a state file to add a space in front of .

Now you are able to get list of opened windows by specified shortcut and search by this list as you type;

## Search by titles without full windows list
This approach is more limited but far less ugly.

# Go to System Settings > Workspace > Shortcuts > Custom Shortcuts.
# Create new Global shortcut -> D-bus Command (by right click)
# Tick the checkbox to the right of the name
# In Trigger tab select the desired key combination
# In Action tab insert the following:
