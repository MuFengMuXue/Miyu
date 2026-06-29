# Display manager

A display manager, or login manager, is typically a graphical user interface that is displayed at the end of the boot process in place of the default shell. There are various implementations of display managers, just as there are various types of window managers and desktop environments. There is usually a certain amount of customization and themeability available with each one.

## List of display managers
## Console
*
*
*
*
*
*
*
*
*

## Graphical
*
*
*
*
*
*
*
*
*
*

## Login daemons
*

## Loading the display manager
To enable graphical login at boot, enable the appropriate systemd service:

* atrium —
* GDM —
* LightDM —
* LXDM —
* Plasma Login Manager —
* SDDM —
* SLiM —
* XDM —
** If  is installed, enable  instead.

If the default target to boot into is  then this should work out of the box. If not, you might have to reset a custom  symlink to point to the default . See systemd#Change default target to boot into.

After enabling the display manager's service a symlink  should be set in . You may need to use  to override old symlinks.

## Using systemd-logind
In order to check the status of your user session, you can use loginctl. All polkit actions like suspending the system or mounting external drives will work out of the box.

 $ loginctl show-session $XDG_SESSION_ID

## Session configuration
Many display managers read available sessions from  directory. It contains standard desktop entry files for each desktop environment or window manager. Some display managers use a separate  to list Wayland-specific sessions.

To add/remove entries to your display manager's session list, create/remove the .desktop files in  as desired. A typical .desktop file will look something like:

 Entry
 Name=Openbox
 Comment=Log in using the Openbox window manager (without a session manager)
 Exec=/usr/bin/openbox-session
 TryExec=/usr/bin/openbox-session
 Icon=openbox.png
 Type=Application

## Run ~/.xinitrc as a session
Installing  will provide an option to run your xinitrc as a session. Simply set  as the session in your display manager's settings and make sure that the  file is executable.

## Starting applications without a window manager
You can also launch an application without any decoration, desktop, or window management. For example, to launch , create a  file in  like this:

 Entry
 Name=Web Browser
 Comment=Use a web browser as your session
 Exec=/usr/bin/google-chrome --auto-launch-at-startup
 TryExec=/usr/bin/google-chrome --auto-launch-at-startup
 Icon=google-chrome
 Type=Application

In this case, once you login, the application set with  will be launched immediately. When you close the application, you will be taken back to the login manager (same as logging out of a normal desktop environment or window manager).

It is important to remember that most graphical applications are not intended to be launched this way and you might have manual tweaking to do or limitations to live with (there is no window manager, so do not expect to be able to move or resize any windows, including dialogs; nonetheless, you might be able to set the window geometry in the application's configuration files).

See also xinitrc#Starting applications without a window manager.

## Tips and tricks
## Autostarting
Most display managers source ,  and . For more details, see xprofile.

## Set language for user session
For display managers that use AccountsService the locale for the user session can be set by editing:

where your_locale is a value such as .

Alternatively, you can achieve this using D-Bus:

GNOME and KDE users can also set languages in GNOME or KDE settings.

Log out and then back in again for the changes to take effect.

## Unlock Gnome Keyring / KDE KWallet automatically on autologin with LUKS
Since systemd version 255, pam_systemd_loadkey can be used to unlock a GNOME/Kwallet keyring, if the user password matches the LUKS passphrase of the system. For this to work, you need to enable autologin in the display manager.
