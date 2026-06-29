# GNOME/Tips and tricks

## Keyboard
## Turn on NumLock on login
See Activating numlock on bootup#GNOME

## Hotkey alternatives
A lot of hotkeys can be changed via GNOME Settings. For example, to re-enable the show desktop keybinding:

Settings > Keyboard > Customize Shortcuts > Navigation > Hide all normal windows

However, certain hotkeys cannot be changed directly via Settings. In order to change these keys, use dconf-editor or gsettings. An example of particular note is the hotkey  (the key above  on US keyboard layouts). In GNOME Shell it is pre-configured to cycle through windows of an application, however it is also a hotkey often used in the Emacs editor. It can be changed by using one of the aforementioned tools to modify the switch-group key found in .

## XkbOptions keyboard options
Using the dconf-editor, navigate to the  key under the  schema and add desired XkbOptions (e.g. caps:swapescape) to the list.

See  for all XkbOptions and  for the respective descriptions.

## De-bind the Super key
By default, the  key will open the GNOME Shell overview mode. You can unbind this key by running the command below:

 $ gsettings set org.gnome.mutter overlay-key ''

## Modify Nautilus hotkeys
Since 3.15 it is not possible to use the accel file anymore, but it is possible to rebind keys by utilizing . Install the package and add the following file:

{{hc|~/.local/share/nautilus-python/extensions/modify_keybindings.py|
import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

def rebind():
    app = Gtk.Application.get_default()
    # Search for open_accels and nautilus_application_set_accelerators in:
    #   https://github.com/GNOME/nautilus/blob/master/src/nautilus-files-view.c
    app.set_accels_for_action( "win.back", "BackSpace" )

    # if you want to figure out which hotkey belongs to which action try this:
    # print(f'Alt+Left is: {app.get_actions_for_accel("Left")}')

class BackspaceBack(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass

    def get_widget(self, uri, window):
        rebind()
        return None

}}

Restart Nautilus:

 $ nautilus -q; nautilus

## Disks
GNOME provides a disk utility to manipulate storage drive settings. These are some of its features:

* Enable write cache is a feature that most hard drives provide. Data is cached and allocated at chosen times to improve system performance. You most likely have this feature already enabled by default (not through disk utility). To check, use .
: Settings > Drive Settings > Write Cache > On'
:
* User Session Defaults Enable to use your own options in , and disable to automatically add default and recommended mount options to drives and partitions that are GPT-based.
: Partition Settings > Edit Mount Options > Automatic Mount Options > On'
:

## Hiding applications from the menu
Use the Main Menu application (provided by the  package) to hide any applications you do not wish to show in the menu.

## Screencast recording
GNOME features built-in screencast recording with the  key combination. A red circle is displayed in the right side of the top bar near the system status area, while the recording is in progress. After the recording is finished, a file named  is saved in the  directory.

In order to use the screencast feature, some gst-plugin packages need to be installed. For example, the screencast pipeline depends on the vp8enc and webmmux elements from . If you get an error about missing "pipewiresrc" module when trying to record, install .

The maximum screencast length is 30 seconds by default. This can be changed as follows:

 $ gsettings set org.gnome.settings-daemon.plugins.media-keys max-screencast-length length_in_seconds

Set  to  for unlimited length (per the description of ).

## Screenshot
 by default saves the image in the directory of the last save, which you can query:

 $ gsettings get org.gnome.gnome-screenshot last-save-directory

Instead of using the above directory, you can set an auto save  directory. e.g. for automatically saving screenshots to the 's desktop directory:

 $ gsettings set org.gnome.gnome-screenshot auto-save-directory file:///home/user/Desktop

Check the  man page for more options.

## Log out delay
To eliminate the default 60 second delay when logging out:

 $ gsettings set org.gnome.SessionManager logout-prompt false

## Change animation speed
Gnome shell animation speed may be configured via a "slow down factor". Greater than 1.0 will slow down animations, between 0.0 & 1.0 speeds them up.

## Set slow down factor
To set temporarily open looking glass with Alt-F2 enter  then run, e.g. to speed up animations:

Alternatively use

Slow down factor may be set permanently without an extension with environment variable , e.g.

## Disable animations
Animations may be disabled via the GUI by toggling Settings > Accessibility > Seeing > Reduce Animation.

## Retina (HiDPI) display support
GNOME introduced HiDPI support in version 3.10. If your display does not provide the correct screen size through EDID, this can lead to incorrectly scaled UI elements. As a workaround you can open dconf-editor and find the key  in . Set it to  to get the standard scale.

Also see HiDPI.

## Passwords and keys (PGP Keys)
You can use the Passwords and Keys program  to create a PGP key as it is a front end for GnuPG and installs it as dependency. This may be useful in the future (for instance if to encrypt a file). Create a key as shown below (the process may take about 10 minutes):

File > New > PGP Key > Name > Email > Defaults > Passphrase.

## Terminal
## Change default terminal size
The default size of a new terminal can be adjusted in your profile's preferences. Select Preferences from the menu and select your profile under Profiles to access the settings to change the initial terminal size.

## New terminals adopt current directory
New terminals open in the  directory by default. You can configure the terminal to adopt the current working directory by adding  to your shell configuration file.

## Pad the terminal
To pad the terminal (create a small, invisible border between the window edges and the terminal contents) create the file below:

{{hc|~/.config/gtk-3.0/gtk.css|
vte-terminal,
terminal-window {
    padding: 10px 10px 10px 10px;
    -vte-terminal-inner-border: 10px 10px 10px 10px;
}}}

## Disable blinking cursor
To disable the blinking cursor in GNOME 3.8 and above use:

 $ gsettings set org.gnome.desktop.interface cursor-blink false

To disable the blinking cursor in Terminal only use:

 $ gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$(gsettings get org.gnome.Terminal.ProfilesList default | tr -d \')/ cursor-blink-mode off

Note that , from the package of the same name, must be running for this and other settings changes to take effect in GNOME applications - see GNOME#Configuration.

## Disable confirmation window when closing Terminal
The Terminal will always display a confirmation window when trying to close the window while one is logged in as root. To avoid this, execute the following:
 $ gsettings set org.gnome.Terminal.Legacy.Settings confirm-close false

## Color palette
The Terminal has support to change its color palette to your liking. Simply, go to Preferences, select your profile and finally edit the color palette.

## Terminal color scheme
Install the  package, which provides a set of custom schemes made for the GNOME Terminal. After you choose a scheme (or more than one), run  and input the number(s) of the scheme(s) that you chose.

After installation, go to Preferences of the Terminal, go to the Colors tab and select the name of the color scheme you installed from the left side of the window. You will see a small arrow next to the name, click it and select Set as default.

From here, further configuration can be taken. You may easily change certain colors you do not like.

To remove a scheme, make another one your default if you had that scheme as your default. Then select its name and click Delete.

## Middle mouse button
## Emulation for two-button mice
By default, GNOME 3 disables middle mouse button emulation regardless of Xorg settings (Emulate3Buttons). To enable middle mouse button emulation use:

 $ gsettings set org.gnome.settings-daemon.peripherals.mouse middle-button-enabled true

## Enable Middle-Click-Paste
Since GNOME 50.0 paste of text from the (PRIMARY selection) has been disabled by default. To turn it back on do:

 $ gsettings set org.gnome.desktop.interface gtk-enable-primary-paste true

## Enable button and menu icons
Since GTK 3.10, the GSettings key 'menus-have-icons' has been deprecated. Icons in buttons and menus can still be enabled by setting the following overrides:
 $ gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/ButtonImages': , 'Gtk/MenuImages': }"

## Use custom colours and gradients for desktop background
To use custom colours and gradients for your desktop background, you will first need to set either a transparent picture or else a non-existent picture as your desktop background. For instance, the command below will set a non-existent picture as the background.

 $ gsettings set org.gnome.desktop.background picture-uri none

At this point, the desktop background should be a flat colour - the default colour setting is for a deep blue.

For a different flat colour you need only change the primary colour setting:
 $ gsettings set org.gnome.desktop.background primary-color
where  is a hex value (such as ffffff for white).

For a colour gradient, you will also need to change secondary colour setting  and select a shading type. For instance, if you want a horizontal gradient, execute the following:
 $ gsettings set org.gnome.desktop.background color-shading-type horizontal

If you are using a transparent picture as your background, you can set the opacity by executing the following:
 $ gsettings set org.gnome.desktop.background picture-opacity
where value is a number between 1 and 100 (100 for maximum opacity).

## Transitioning backgrounds
GNOME can transition between different wallpapers at specific time intervals. This is done by creating an XML file specifying the pictures to be used and the time interval. For more information on creating such files, see the following article.

## Custom GNOME sessions
It is possible to create custom GNOME sessions which use the GNOME session manager but start different sets of components (Openbox with tint2 instead of GNOME Shell for example).

Two files are required for a custom GNOME session: a session file in  which defines the components to be started and a desktop entry in  which is read by the display manager. An example session file is provided below:

And an example desktop file:

## Redirect certain URLs to specific web browsers
This shows how to use Chromium for certain types of URLs while maintaining Firefox as default browser for all other tasks.

Make sure  is installed, to use pcregrep.

Setup custom xdg-open:

{{hc|/usr/local/bin/xdg-open|
#!/bin/bash
DOMAIN_LIST_FILE=~/'domains.txt'
OTHER_BROWSER='/usr/bin/chromium-browser'
BROWSER_OPTIONS='' # Optional, for command line options passed to browser
XDG_OPEN='/usr/bin/xdg-open'
DEFAULT_BROWSER='/usr/bin/firefox'

if echo "$1" | pcregrep -q '^https?://'; then
    matching=0
    while read domain; do
	if echo "$1" | pcregrep -q "^https?://${domain}"; then
	    matching=1
	    break
	fi
    done  Default Applications and  set Web to xdg-open web''.

## Removing film holes/film strip from video thumbnails in Nautilus
Nautilus (Files) overlays the film holes/film strip effect on video thumbnails since Gnome 3.12. To remove or override this effect, the environment variable  can be used to reference the path of a compiled resource (in this instance ) and specify the path for the relevant overlay. This environment variable has only been available since GLib 2.50 and will have no effect on versions before this.

Extract  from Nautilus:

 $ gresource extract /usr/bin/nautilus /org/gnome/nautilus/icons/filmholes.png > filmholes.png

Edit  using your preferred editor and remove the film effect from the image, leaving the transparency and dimensions intact, then overwriting the extracted image.

Copy or move the extracted image where desired, such as  and edit , adding the following export, changing  as needed to the location you placed the file:

 export G_RESOURCE_OVERLAYS=/org/gnome/nautilus/icons/filmholes.png=/usr/share/icons/filmholes.png

If  has been installed as a dependency for another file manager that may generate thumbnails, the  line in  should be modified removing the  flag.

To ensure that no thumbnails remain that may already have the film effect embedded, remove the thumbnail cache:

 $ rm -r ~/.cache/thumbnails

Log out and back in to your session and you should no longer have the film holes/film strip effect on your thumbnails in Nautilus.

## GNOME Software integration with pacman
 integration was previously available through a package named gnome-software-packagekit-plugin but has been voluntarily disabled and is considered unsupported.

Apps installed with pacman are shown in but can't be uninstalled from GNOME Software. To not show them set this option and restart GNOME Software:
 $ echo GNOME_SOFTWARE_PLUGINS_BLOCKLIST=appstream > ~/.config/environment.d/gs-disable-appsteam.conf
 $ gnome-software --quit

## Increase volume above and beyond 100%
You can allow over-amplification by running the command below:

 $ gsettings set org.gnome.desktop.sound allow-volume-above-100-percent true

Alternatively, install the extension volume mixer. Then use the mouse to scroll above the volume icon in the top panel to increase the volume above and beyond 100%.

Or, open GNOME Tweaks and toggle General > Over-Amplification.

## Adjust volume in smaller steps
By default, pressing the keyboard's volume keys adjusts the volume by 6%. If smaller steps are desired, holding  while pressing the volume keys adjusts the volume in 2% steps.

Also, as of GNOME 3.36, it is now possible to directly adjust the volume step via a dconf setting. For example, to set the volume step to 2% execute the following:

 $ gsettings set org.gnome.settings-daemon.plugins.media-keys volume-step 2

## Show volume sound percentage next to top panel icon
Install the extension sound percentage to display the current output volume level next to the sound icon in the top panel.

## Launch on discrete GPU
Install  or  and start/enable .

## Window list
If you like having a tasks list on the bottom but dislike the default black color of this extension, first copy its directory:

 $ cp -r /usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/ ~/.local/share/gnome-shell/extensions/

Then edit the CSS to your liking. For example, to make the window list transparent, edit  as follows:

 .bottom-panel {
   background: transparent;
 }
 ...
 .window-button > StWidget,
 .window-picker-toggle > StWidget {
   color: #bbb;
   background-color: transparent;
   ...

## Navigation
To mimic the behavior of Windows when switching between windows, first disable the default which restricts the window switching to those in the current workspace:

 $ gsettings set org.gnome.shell.app-switcher current-workspace-only false

then, bind  and  to switch between windows, and not applications:

 $ gsettings set org.gnome.desktop.wm.keybindings switch-windows "$ gsettings set org.gnome.desktop.wm.keybindings switch-windows-backward "['Tab'"

additionally, one can rebind the switching between applications (this example uses  instead of the default ):

 $ gsettings set org.gnome.desktop.wm.keybindings switch-applications "$ gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "['Tab'"

## Image Viewer
Install  to add support for HEIC image file format install `libheif`.  Image Viewer uses `gdk-pixbuf2` library which lists `libheif` as one of the optional dependencies.

## Dconf (gsettings) database stored as a text-based file
By default, dconf stores its configuration in a binary database blob located at . A dconf profile configuration may override this default if your home directories are stored in NFS, you keep dotfiles in version control, or other reasons. See  for details on creating and using profiles.

Before changing the system-wide default, dump each user's existing dconf database to a text-based keyfile named . It does not appear to be possible to use a different extension. Assuming the default for , that may be done with this command:

Once done, create the default dconf profile as root.

Log out and back in again and verify that changing dconf settings alters the text-based  but not the old binary  file before deleting the binary database.

This setting should incur some minimal extra resource usage. Dconf still uses a binary database in the temporary  directory, but it must recreate it at desktop startup. It must also keep  up to date, and monitor the text file for changes as well.
