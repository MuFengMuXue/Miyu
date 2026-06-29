# Flameshot

Flameshot is a program for taking screenshots. It has an interactive GUI with controls to select the desired capture region, move and resize the capture window, make edits with common drawing tools (pencil, line, rectangle, circle, blur, undo/redo), and choose the output destination (copy to clipboard, save to disk, upload to Imgur, open with another program).

## Installation
Install the  package.

## Troubleshooting
## Sub-commands exit immediately with no output
You can start Flameshot as a background process at any time during your X session:

 $ flameshot &

## No tray icon
There are probably other ways to do this.  Here is just one way.

Install

Then in the gnome tweaks application (may also need to download if you do not have it installed):

# Click on the Extensions tab
# Enable "Topicons plus" so it moves the legacy tray icons to the top panel
# Done!

## Flameshot does not use currently visible windows
You may encounter this issue if you have installed .

Simply remove the  package and make sure there is no dangling X11 configuration for the package under .

Then reboot the system.

This was discussed in an issue on the Flameshot Github repository: https://github.com/flameshot-org/flameshot/issues/1677.

## Fonts render strangely
QT6 changed the default DPI scale factor rounding policy to `Passthrough`.

Set it back to QT5's `Round`:

 env QT_SCALE_FACTOR_ROUNDING_POLICY=Round flameshot gui

## Flameshot starts with an error on Sway / wlroots
When trying to take a screenshot, Flameshot will display the following error:

Flameshot requires the following packages to be installed to work correctly on Wayland:

Once these are installed, you should be able to start Flameshot.

More information can be found on the Sway wiki page

## Flameshot starts with an error on Gnome Wayland
When trying to take a screenshot the first time, Flameshot will request permissions and the Gnome portal will show a permission prompt. If permissions have been denied once, flameshot will never display the dialog again and display the following error:

Permissions can be shown by the  command (note the  here):

To reset the permission and ask again, run the following command (note the single quotes at the end relates to the empty "App" column, it may change if flatpak has a non-empty application ID):

## Flameshot does not work on all monitors of a multi-monitor setup in KDE Plasma on wayland
The flameshot overlay only shows on one of several monitors. A workaround has been suggested in the flameshot github repository.

Basically, KDE plasma needs to be configured to overwrite the initial position of the flameshot overlay window in order for the flameshot overlay to show up on all connected monitors. For this, start the "Window Rules" application and create a new window rule with the following settings:
* "Window Class": flameshot
* "Window Types": normal window
* "Window Title": Exact Match: flameshot
* "Position": Force 0 0
* "Fullscreen": Force No
* "Obey geometry restrictions": Force Yes
* "Keep above other windows": Force Yes

## Flameshot does not work on all monitors of a multi-monitor setup in Sway
The flameshot overlay only shows on one of several monitors. A workaround has been suggested in the flameshot github repository.

The workaround consists of forcing the flameshot window/overlay to launch in floating mode and not in full screen, by adding the following line to your Sway configuration:

 for_window border pixel 0, floating enable, fullscreen disable, move absolute position 0 0

Alternatively, you can force Flameshot to run under xWayland with  but note that, while it fixes the multi-monitor issue, it breaks keyboard shortcuts so Flameshot have to be controlled entirely with the mouse.

## Flameshot does not generate thumbnails in KDE Dolphin
When running Plasma 6, trying to save a picture using dolphin's file picker will show the directory with no thumbnails if other image files are present. Running flameshot in a terminal will show the reason.

 kf.service.services: KServiceTypeTrader: serviceType "ThumbCreator" not found

Installing  solves this problem. [https://forums.opensuse.org/t/dolphin-cant-create-photo-thumbnails-servicetype-thumbcreator-not-found/170259/4

## Global shortcuts do not work on Gnome Wayland
Create a wrapper script that sets the correct environment variable:

{{bc|
cat > $HOME/flameshot-gui  "View and Customize Shortcuts" > "Custom Shortcuts", and click the "+" button. Select the shortcut you want and enter the path to the wrapper script in the "Command" button.
